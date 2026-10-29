"""Render README_cn.md (final report) from catalog_cn.csv / progress_cn.csv / download_failures_cn.csv /
tools/tools_catalog_cn.csv / state/summary.json.  Run after build_catalog_en.py.
Usage: python3 -I scripts/make_readme_en.py
"""
import csv
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_en import CATS, ROOT, STATE  # noqa: E402
from fetch_en import load_seeds  # noqa: E402


def rd(path):
    with open(ROOT / path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def version_kind(seed):
    g = seed["get"]
    k = g.get("kind")
    if seed.get("reuse"):
        return "已有库复用（原版本）"
    if k == "git":
        ref = g.get("ref", "")
        if ref and ref not in ("gh-pages", "site", "asf-site", "main", "master", "latest", "v2", "vNext"):
            return "固定发布标签（tag）"
        return "分支提交快照（记录提交号与日期）"
    if k == "multi_git":
        return "分支提交快照（记录提交号与日期）"
    if k == "hfdoc":
        return "官方构建包（版本号）"
    if k == "mirror":
        return "站点当前版本离线镜像（记录访问日期）"
    if seed["type"] == "paper":
        return "论文定版（arXiv 版本号/会议版）"
    return "官方发布文件（PDF/压缩包，版本见文件）"


def main():
    cat = rd("catalog_cn.csv")
    prog = rd("progress_cn.csv")
    fails = rd("download_failures_cn.csv")
    tools = rd("tools/tools_catalog_cn.csv")
    summ = json.load(open(STATE / "summary.json", encoding="utf-8"))
    seeds = {s["id"]: s for s in load_seeds()}
    ok_ids = {r["资料编号"] for r in cat}
    L = []
    w = L.append
    w("# 编程参考资料库（programming_reference_literature）最终报告")
    w("")
    w("生成时间：由 `scripts/make_readme_en.py` 根据登记表自动生成。资料访问日期：2026-10-29（UTC）。")
    w("")
    w("覆盖从编程基础到 AI 应用、性能优化与部署的 16 个类别，以及主流 AI 框架与工具的官方文档、教程、课程与示例。"
      "只计入完整下载并核验通过的资料。只保存了部分内容的资料单列为\"部分资料\"，不计入完整数。")
    w("")
    w("## 1. 总体数量")
    w("")
    w(f"- 已核验资料（全库去重后的独立条目）：**{summ['verified_items']}** 项，其中完整 **{summ['complete']}** 项，部分资料 **{summ['partial']}** 项。")
    w(f"- 新下载 **{summ['new']}** 项；已有库复用（核验后复制，未移动原库）**{summ['reused']}** 项。")
    w(f"- 未获取（失败或待重试）：**{summ['failed_or_todo']}** 项，见 `download_failures_cn.csv`。")
    w(f"- 总体积约 {summ['bytes_mb'] / 1024:.1f} GB。")
    w(f"- 工具层面：登记 {summ['tools']} 个工具/项目，`tools/tools_catalog_cn.csv` 共 {summ['tool_rows']} 行（含子模块关联行）。")
    w("")
    w("按资料类型（完整 / 含部分资料合计）：")
    w("")
    w("| 类型 | 完整 | 合计（含部分资料） |")
    w("|---|---|---|")
    for t, n in summ["by_type"].items():
        w(f"| {t} | {summ['by_type_complete'].get(t, 0)} | {n} |")
    w("")
    w("## 2. 各类别数量与目标")
    w("")
    w("目标：教材 3–5、大学课程 2–4、官方文档 2–5、实践项目 2–5；论文只对 02/11/13/14/15 设 10–20 篇。官方文档按\"项目+版本\"计数，"
      "同一项目的多个部分（如 Docker 文档 + Dockerfile 参考）按条目分别登记。工具文档、示例与课程分别统计，不冲抵教材或论文数量。")
    w("")
    w("| 类别 | 教材 | 课程 | 官方文档 | 实践项目 | 论文 | 未达标项 |")
    w("|---|---|---|---|---|---|---|")
    for r in prog:
        def cell(t):
            n, p = r[f"{t}（完整）"], r[f"{t}（部分）"]
            return f"{n}" + (f"（+{p} 部分）" if p != "0" else "")
        gaps = [f"{t.split('/')[0]}{r[f'{t}状态']}" for t in ("教材/参考书", "大学课程资料", "官方文档/系统教程", "实验/习题/参考项目", "论文/综述")
                if r[f"{t}状态"].startswith("缺")]
        docs_cell = "不适用" if r["官方文档/系统教程目标"] == "不适用" else cell("官方文档/系统教程")
        w(f"| {r['类别']} | {cell('教材/参考书')} | {cell('大学课程资料')} | {docs_cell} | "
          f"{cell('实验/习题/参考项目')} | {cell('论文/综述') if r['论文/综述目标'] != '不设配额' else '—'} | {'；'.join(gaps) or '达标'} |")
    w("")
    w("注：\"大学课程资料\"包含少量非大学官方课程（Hugging Face 官方课程、Inria scikit-learn MOOC），其资料形态列已标注。02 类算法没有\"官方文档\"，不适用。")
    w("")
    w("## 3. 版本与年份分布")
    w("")
    vk = Counter(version_kind(seeds[i]) for i in ok_ids if i in seeds)
    w("版本固定方式：")
    w("")
    for k, n in vk.most_common():
        w(f"- {k}：{n} 项")
    w("")
    by_year = Counter()
    for r in cat:
        y = (r["年份"] or "")[:4]
        if y.isdigit():
            by_year["2022 年及以前" if int(y) <= 2022 else y] += 1
    w("资料年份（教材为版次年份，文档/源码为版本或快照年份，论文为首次公开年份）：")
    w("")
    w("| 年份 | 数量 |")
    w("|---|---|")
    for y in sorted(by_year, key=lambda x: (x != "2022 年及以前", x)):
        w(f"| {y} | {by_year[y]} |")
    w("")
    papers = [r for r in cat if r["类型"] == "论文/综述"]
    recent = sum(r["时间窗口"] == "近三年" for r in papers)
    w(f"论文 {len(papers)} 篇：近三年（2023-10-29 之后首次公开）{recent} 篇，经典/较早 {len(papers) - recent} 篇（单列标注）。")
    w("")
    w("## 4. 从基础到应用与部署的覆盖")
    w("")
    w("| 阶段 | 学习路线 | 覆盖情况 |")
    w("|---|---|---|")
    w("| 编程基础 | `guides/beginner_path_cn.md` | Python、算法、Linux/Shell、Git、测试：教材、课程、官方文档、练习齐全 |")
    w("| AI 编程 | `guides/ai_programming_path_cn.md` | NumPy/SciPy/pandas/Matplotlib/Jupyter → scikit-learn 与梯度提升 → PyTorch/TF/Keras/JAX → HF 生态 → 实验与数据管理 |")
    w("| 应用开发 | `guides/application_path_cn.md` | HTTP、数据库、Django/FastAPI/Flask、前端（MDN/React/TS）、RAG、工具调用与代码智能体 |")
    w("| 系统与性能 | `guides/systems_performance_path_cn.md` | C、机器级程序、链接与构建、OS 与并发、网络、CPU 性能、CUDA/Triton、训练系统优化 |")
    w("| 部署 | `guides/deployment_path_cn.md` | Docker、CI/CD、Kubernetes、Prometheus/OpenTelemetry、SRE、分布式基础、模型服务 |")
    w("| 实践 | `guides/practice_projects_cn.md` | 按难度分三级的项目与评价方式 |")
    w("| 核心入口 | `guides/core_reading_list_cn.md` | 每类优先教材/课程/官方参考 |")
    w("| 工具 | `tools/tools_learning_map_cn.md`、`tools/interoperability_guide_cn.md` | 工具用途与顺序；训练→导出→ONNX→推理部署的兼容条件 |")
    w("")
    w("### 4.1 重点工具资料链完整度")
    w("")
    focus = ["PyTorch", "TensorFlow", "Keras", "OpenCV", "Transformers", "ONNX", "ONNX Runtime"]
    trows = defaultdict(list)
    for r in tools:
        trows[r["工具"]].append(r)
    w("| 工具 | 资料编号 | 完整性 | 覆盖方面（并集） |")
    w("|---|---|---|---|")
    for t in focus:
        rs = trows.get(t, [])
        asp = sorted({a.strip() for r in rs for a in r["覆盖方面"].split(";") if a.strip()})
        w(f"| {t} | {'、'.join(r['资料编号'] for r in rs)} | {'、'.join(sorted({r['完整性'] for r in rs}))} | {'；'.join(asp)} |")
    w("")
    w("## 5. 缺失、失败、残缺与待核实")
    w("")
    w("### 5.1 未获取（失败/待重试）")
    w("")
    if fails:
        w("| 编号 | 标题 | 原因（摘要） |")
        w("|---|---|---|")
        for r in fails:
            w(f"| {r['资料编号']} | {r['标题']} | {r['原因'][:160].replace('|', '/').replace(chr(10), ' ')} |")
    else:
        w("无。")
    w("")
    w("### 5.2 部分资料（已核验，但只保存了说明中的范围）")
    w("")
    w("| 编号 | 标题 | 范围说明 |")
    w("|---|---|---|")
    for r in cat:
        if r["完整性状态"].startswith("部分"):
            w(f"| {r['资料编号']} | {r['标题']} | {r['范围说明'][:200]} |")
    w("")
    w("### 5.3 结构性缺口")
    w("")
    w("- 见第 2 节\"未达标项\"列，以及 `tools/tools_learning_map_cn.md` 末尾的工具层面缺口说明。")
    w("- 以下资料因访问限制未获取，也未绕过：HAL 机器人验证（Modern C、Rougier 可视化）、Berkeley 证书错误（Architecture of a Database System）、"
      "需填邮箱领取的 van Steen《Distributed Systems》。详见 `search_log_cn.md` 第 4 节。")
    w("- 无许可证文件的源码仓库不保存（见 `search_log_cn.md` 第 5 节）。")
    w("")
    w("## 6. 目录与登记表")
    w("")
    w("```")
    w("programming_reference_literature/")
    w("├── README_cn.md                 本报告")
    w("├── catalog_cn.csv               全部已核验资料（编号、类别、类型、版本、许可证、本地路径、完整性、提交号…）")
    w("├── progress_cn.csv              各类别 × 类型的完成数与目标")
    w("├── download_failures_cn.csv     失败与待重试条目")
    w("├── search_log_cn.md             检索方法、版本核实与取舍决定")
    w("├── books/  courses/  official_docs/  practice/  papers/")
    w("├── guides/                      7 份中文学习路线与索引")
    w("├── tools/                       tools_catalog_cn.csv、tools_learning_map_cn.md、interoperability_guide_cn.md")
    w("├── scripts/                     种子清单、下载核验、登记与报告脚本（*_en.py）")
    w("└── state/                       每个条目的核验状态（state/items/<编号>.json）与日志")
    w("```")
    w("")
    w("命名：自建文件在扩展名前加语言后缀（`_en`/`_cn`）。完整上游项目与文档包保持内部原始结构，外层归档加后缀（如 `pytorch_2.15_docs_html_en.tar`）。"
      "tar 包内保留上游路径，入口文件见 `tools/tools_catalog_cn.csv` 的\"入口文件\"列。")
    w("")
    w("## 7. 续跑命令")
    w("")
    w("```bash")
    w("cd /root/programming_reference_literature")
    w("# 1) 重新生成种子（修改 scripts/seed_*_en.py 后）")
    w("python3 -I scripts/seed_tools_en.py && python3 -I scripts/seed_core_en.py && python3 -I scripts/seed_papers_en.py")
    w("# 2) 下载与核验（已完成条目自动跳过；--retry-failed 重试失败项；各 --kind 通道可并行，同一条目有锁）")
    w("python3 -I scripts/fetch_en.py run --kind pdf,pdfset,file,hfdoc,reuse,git,multi_git --retry-failed")
    w("python3 -I scripts/fetch_en.py run --kind mirror --retry-failed")
    w("python3 -I scripts/fetch_en.py status            # 汇总与失败原因")
    w("# 3) 生成登记表、指南与报告")
    w("python3 -I scripts/build_catalog_en.py && python3 -I scripts/link_guides_en.py && python3 -I scripts/make_readme_en.py")
    w("```")
    w("")
    w("## 8. 本轮边界")
    w("")
    w("- 只收集整理：未执行任何来源代码，未安装项目依赖，未部署，未上传 GitHub，未删除本地资料。")
    w("- 未下载视频、数据集、模型权重、依赖缓存或构建产物。源码包中的大文件按规则剔除并记录在 `state/items/<编号>.json`。")
    w("- 按要求未安排整库哈希扫描或上传后回验。单个文件的 SHA256 只在下载时顺带记录在状态文件中。")
    (ROOT / "README_cn.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("README_cn.md written:", len(L), "lines")


if __name__ == "__main__":
    main()
