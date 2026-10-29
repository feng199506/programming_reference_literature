"""Probe candidate sources before seeding.

Input lines (stdin or file):  URL            -> HEAD (falls back to ranged GET) status/type/size
                              git REPO_URL    -> newest release-looking tags + default branch HEAD
Usage: python3 -I scripts/probe_en.py [file]
"""
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, __import__("os").path.dirname(__file__))
from common_en import http  # noqa: E402


def vkey(t):
    nums = [int(x) for x in re.findall(r"\d+", t)[:4]]
    return nums + [0] * (4 - len(nums))


def probe_git(repo):
    try:
        out = subprocess.run(["git", "ls-remote", "--tags", "--refs", repo], capture_output=True, text=True,
                             timeout=120, env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin"}).stdout
        head = subprocess.run(["git", "ls-remote", "--symref", repo, "HEAD"], capture_output=True, text=True,
                              timeout=120, env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/usr/bin:/bin"}).stdout
    except Exception as e:
        return f"git {repo} ERR {e}"
    tags = [l.split("refs/tags/")[1] for l in out.splitlines() if "refs/tags/" in l]
    rel = [t for t in tags if re.search(r"\d+\.\d+", t) and not re.search(r"(rc|alpha|beta|dev|pre|a\d|b\d|nightly|post)", t, re.I)]
    rel.sort(key=vkey)
    br = re.search(r"ref: refs/heads/(\S+)\s+HEAD", head)
    sha = head.split()[-2] if head.split() else "?"
    return f"git {repo} | default={br.group(1) if br else '?'}@{sha[:12]} | ntags={len(tags)} | latest={rel[-4:]}"


def probe_url(u):
    r = http(u, method="HEAD", tries=2, timeout=40)
    if r["status"] in (403, 405, 0, 501):
        r = http(u, headers={"Range": "bytes=0-1023"}, tries=2, timeout=40)
    ln = r.get("length")
    size = f"{int(ln) / 1e6:.1f}MB" if ln and ln.isdigit() else "?"
    final = r["url"] if r["url"] != u else ""
    return f"{r['status']} {size} {r['ctype'][:30]} {u} {('-> ' + final) if final else ''} {r['err']}"


def main():
    src = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    lines = [l.strip() for l in src if l.strip() and not l.startswith("#")]

    def one(l):
        return probe_git(l.split(None, 1)[1]) if l.startswith("git ") else probe_url(l)
    with ThreadPoolExecutor(8) as ex:
        for res in ex.map(one, lines):
            print(res, flush=True)


if __name__ == "__main__":
    main()
