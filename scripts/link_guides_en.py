"""Render guide drafts (scripts/guide_src/*.md) into guides/ and tools/: every 〔ID〕 token becomes
"ID 《title》 → `local/path`" plus a status tag taken from the verified state, so guides only point at
material that actually exists.  Unknown ids are reported and rendered as （编号无效）.
Usage: python3 -I scripts/link_guides_en.py
"""
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_en import ROOT, item_state  # noqa: E402
from fetch_en import load_seeds  # noqa: E402

SRC = ROOT / "scripts" / "guide_src"
TOKEN = re.compile(r"〔([0-9]{2}[A-Z][0-9]{2})(?:\|([^〕]*))?〕")
DEST = {"tools_learning_map_cn.md": "tools", "interoperability_guide_cn.md": "tools"}


def main():
    seeds = {s["id"]: s for s in load_seeds()}
    bad, missing = set(), set()
    for src in sorted(SRC.glob("*_cn.md")):
        text = src.read_text(encoding="utf-8")

        def sub(m):
            iid, label = m.group(1), m.group(2)
            s = seeds.get(iid)
            if not s:
                bad.add(iid)
                return f"{iid}（编号无效）"
            st = item_state(iid)
            title = label or s["title"]
            if st.get("status") != "ok":
                missing.add(iid)
                return f"{iid}《{title}》（未获取，见 download_failures_cn.csv）"
            tag = "" if s.get("complete", "完整") == "完整" else "〔部分资料〕"
            rel = os.path.relpath(ROOT / s["out"], ROOT / DEST.get(src.name, "guides"))
            return f"{iid}《{title}》{tag} → `{rel}`"
        out = TOKEN.sub(sub, text)
        dest = ROOT / DEST.get(src.name, "guides") / src.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(out, encoding="utf-8")
        print("wrote", dest.relative_to(ROOT))
    if bad:
        print("UNKNOWN ids:", sorted(bad))
    if missing:
        print("referenced but not obtained:", sorted(missing))


if __name__ == "__main__":
    main()
