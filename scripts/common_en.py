"""Shared helpers for programming_reference_literature: paths, per-host rate limiting
(cross-process flock, same file protocol as the sibling *_literature libraries so the
arXiv budget is shared), HTTP with bounded retries, atomic JSON state per item.

Downloaded content is untrusted: it is written under STAGING / the library tree and
never imported or executed. Run every script with `python3 -I`.
"""
import fcntl
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
STATE = ROOT / "state"
ITEMS = STATE / "items"
CACHE = Path(os.environ.get("PRL_CACHE", "/root/.cache/prl_lit"))
STAGING = CACHE / "staging"
PYLIB = CACHE / "pylib"
LOCK_DIR = Path("/tmp/lmm_ratelimit")
UA = "Mozilla/5.0 (compatible; programming_reference_literature/1.0; personal reference collection, low request rate)"
ACCESS_DATE = time.strftime("%Y-%m-%d", time.gmtime())

INTERVAL = {"arxiv.org": 4.0, "export.arxiv.org": 4.0, "api.github.com": 2.0}

CATS = {
    "01": "Python 编程", "02": "数据结构与算法", "03": "科学计算与数据处理",
    "04": "机器学习编程", "05": "深度学习编程", "06": "软件工程与测试",
    "07": "Linux、Shell 与 Git", "08": "数据库与数据工程", "09": "后端与 API 开发",
    "10": "前端与交互界面", "11": "计算机系统与网络", "12": "C/C++ 与性能优化",
    "13": "GPU 与并行计算", "14": "分布式系统与部署", "15": "AI 应用与智能体开发",
    "16": "安全编程",
}
TYPES = {"book": "教材/参考书", "course": "大学课程资料", "docs": "官方文档/系统教程",
         "practice": "实验/习题/参考项目", "paper": "论文/综述"}


def host_key(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    return "arxiv.org" if host.endswith("arxiv.org") else host


def wait(key, interval):
    LOCK_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_DIR / re.sub(r"[^A-Za-z0-9._-]", "_", key), "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        raw = f.read().strip()
        try:
            last = float(raw) if raw else 0.0
        except ValueError:
            last = 0.0
        delay = interval - (time.time() - last)
        if delay > 0:
            time.sleep(min(delay, interval))
        f.seek(0)
        f.truncate()
        f.write(str(time.time()))


def http(url, method="GET", timeout=120, tries=3, headers=None, dest=None, max_bytes=None):
    """GET/HEAD. Returns dict(status, body|None, url, ctype, length, err). With dest, streams to file."""
    key = host_key(url)
    err = ""
    for attempt in range(tries):
        wait(key, INTERVAL.get(key, 1.0))
        try:
            h = {"User-Agent": UA, "Accept": "*/*", **(headers or {})}
            req = urllib.request.Request(url, headers=h, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                info = {"status": r.status, "url": r.geturl(), "ctype": r.headers.get("Content-Type", ""),
                        "length": r.headers.get("Content-Length"), "err": "",
                        "last_modified": r.headers.get("Last-Modified", "")}
                if method == "HEAD":
                    info["body"] = None
                    return info
                if dest:
                    n = 0
                    tmp = Path(str(dest) + ".part")
                    with open(tmp, "wb") as out:
                        while True:
                            chunk = r.read(1 << 20)
                            if not chunk:
                                break
                            n += len(chunk)
                            if max_bytes and n > max_bytes:
                                raise ValueError(f"exceeds max_bytes {max_bytes}")
                            out.write(chunk)
                    os.replace(tmp, dest)
                    info["body"] = None
                    info["bytes"] = n
                else:
                    info["body"] = r.read()
                return info
        except urllib.error.HTTPError as e:
            err = f"HTTP {e.code}"
            if e.code == 429:
                time.sleep(30 * (attempt + 1))
                continue
            if e.code in (500, 502, 503, 504):
                time.sleep(5 * (attempt + 1))
                continue
            return {"status": e.code, "body": None, "url": url, "ctype": "", "length": None, "err": err}
        except Exception as e:  # network errors, timeouts
            err = f"{type(e).__name__}: {e}"
            time.sleep(3 * (attempt + 1))
    return {"status": 0, "body": None, "url": url, "ctype": "", "length": None, "err": err}


def load_json(path, default=None):
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def save_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, p)


def item_state(item_id):
    return load_json(ITEMS / f"{item_id}.json", {})


def save_item_state(item_id, st):
    save_json(ITEMS / f"{item_id}.json", st)


def norm_words(s):
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return [w for w in s.split() if len(w) > 2 and w not in {"the", "and", "for", "with", "from", "into"}]


def use_pypdf():
    if str(PYLIB) not in sys.path:
        sys.path.insert(0, str(PYLIB))
    import pypdf  # noqa: E402
    import logging
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    return pypdf
