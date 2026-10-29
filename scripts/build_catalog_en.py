"""Build the Chinese registers from seeds + per-item state (no network):
  catalog_cn.csv              every item that downloaded and verified (完整 or 部分资料)
  progress_cn.csv             per category x type counts vs targets
  download_failures_cn.csv    failed / not attempted items with reasons
  tools/tools_catalog_cn.csv  one row per tool x material item
  state/summary.json          numbers used by README_cn.md
Usage: python3 -I scripts/build_catalog_en.py
"""
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_en import CATS, ROOT, STATE, TYPES, item_state, save_json  # noqa: E402
from fetch_en import load_seeds  # noqa: E402

TARGET = {"book": (3, 5), "course": (2, 4), "docs": (2, 5), "practice": (2, 5), "paper": (10, 20)}
PAPER_CATS = {"02", "11", "13", "14", "15"}
NO_DOCS_CATS = {"02"}  # algorithms: no "official documentation" exists
ASPECTS = {1: "入门安装", 2: "用户指南/概念", 3: "API 参考", 4: "教程/工作流", 5: "调试/性能/FAQ",
           6: "保存/导出/部署/互操作", 7: "课程", 8: "示例源码"}

# tool -> (方向, 官方归属/状态说明); rows also link sub-tools that live inside another project's docs
TOOL_DIR = {
    "NumPy": "科学计算与数据处理", "SciPy": "科学计算与数据处理", "pandas": "科学计算与数据处理", "Matplotlib": "科学计算与数据处理",
    "Jupyter": "科学计算与数据处理", "scikit-learn": "传统机器学习", "XGBoost": "传统机器学习", "LightGBM": "传统机器学习",
    "CatBoost": "传统机器学习", "PyTorch": "深度学习", "TensorFlow": "深度学习", "Keras": "深度学习", "JAX": "深度学习",
    "torchvision": "PyTorch 生态", "torchaudio": "PyTorch 生态", "OpenCV": "计算机视觉", "Pillow": "计算机视觉",
    "Albumentations": "计算机视觉", "Transformers": "Hugging Face 生态", "Datasets": "Hugging Face 生态",
    "Tokenizers": "Hugging Face 生态", "Accelerate": "Hugging Face 生态", "PEFT": "Hugging Face 生态", "TRL": "Hugging Face 生态",
    "Diffusers": "Hugging Face 生态", "Evaluate": "Hugging Face 生态", "Hub 客户端（huggingface_hub）": "Hugging Face 生态",
    "ONNX": "模型交换与推理", "ONNX Runtime": "模型交换与推理", "TensorRT": "模型交换与推理", "OpenVINO": "模型交换与推理",
    "vLLM": "大模型推理与部署", "llama.cpp": "大模型推理与部署", "Triton Inference Server": "大模型推理与部署",
    "BentoML": "大模型推理与部署", "CUDA": "GPU 编程与训练优化", "Triton 编程语言": "GPU 编程与训练优化",
    "DeepSpeed": "GPU 编程与训练优化", "NCCL": "GPU 编程与训练优化", "Sentence Transformers": "检索与 AI 应用",
    "FAISS": "检索与 AI 应用", "LangChain": "检索与 AI 应用", "LlamaIndex": "检索与 AI 应用", "TensorBoard": "实验与数据管理",
    "MLflow": "实验与数据管理", "DVC": "实验与数据管理", "Weights & Biases": "实验与数据管理", "FastAPI": "应用与部署基础",
    "Gradio": "应用与部署基础", "Streamlit": "应用与部署基础", "Docker": "应用与部署基础", "Kubernetes": "应用与部署基础",
    "pytest": "测试与工程工具", "mypy": "测试与工程工具（类型检查）", "Pyright": "测试与工程工具（类型检查）",
    "Ruff": "测试与工程工具（代码检查/格式化）", "typing": "测试与工程工具（类型系统规范）", "Python": "测试与工程工具（语言/打包基础）",
    "pip": "测试与工程工具（打包与环境）", "uv": "测试与工程工具（打包与环境）",
    "Python Packaging User Guide": "测试与工程工具（打包与环境）", "smolagents / Agents": "检索与 AI 应用",
}
# sub-tools documented inside another project's (already counted) doc set
SUBTOOLS = [
    ("torch.distributed（DDP/FSDP/torchrun）", "PyTorch 生态", ["05D01", "05D02", "05X01"], [1, 2, 3, 4, 5, 8],
     "PyTorch 2.15 文档 distributed*.html、fsdp、elastic/torchrun 页；教程 distributed 分区；examples/distributed"),
    ("torch.export / torch.onnx（模型导出）", "PyTorch 生态", ["05D01", "05D02"], [2, 3, 4, 6],
     "PyTorch 2.15 文档 export*.html、onnx*.html；教程中导出与 ONNX 相关篇目"),
    ("torch.profiler / 性能分析", "PyTorch 生态", ["05D01", "05D02", "04D08"], [3, 4, 5],
     "PyTorch 文档 profiler.html、torch.compile 排障；教程 profiler 篇；TensorBoard profiling 笔记本"),
    ("torch.compile", "PyTorch 生态", ["05D01", "05D02"], [2, 3, 4, 5], "PyTorch 文档 torch.compiler*.html 与编译排障页"),
    ("分布式训练官方工具（汇总）", "GPU 编程与训练优化", ["05D01", "05D23", "13D04", "13D05", "13D06", "05X15"], [1, 2, 3, 4, 5, 8],
     "torch.distributed、Accelerate、DeepSpeed、NCCL 文档与示例"),
]


# university / official courses that teach a tool (aspect 7), linked by id
TOOL_COURSES = {
    "PyTorch": ["05C01", "05C02", "05C03", "05C04", "15C03"], "TensorFlow": ["05C04"], "JAX": ["05C03"],
    "scikit-learn": ["04C04", "03C01"], "pandas": ["03C01", "03C02"], "NumPy": ["03C01"], "CUDA": ["13C01", "13C02"],
    "Docker": ["10C01"], "FastAPI": [], "Kubernetes": [], "MLflow": ["04C02"], "LangChain": ["15C50"], "LlamaIndex": ["15C50"],
}


def size_mb(st):
    return round((st.get("bytes") or 0) / 1e6, 1)


def main():
    seeds = load_seeds()
    rows, fails, tool_rows = [], [], []
    prog = defaultdict(Counter)
    partial = defaultdict(Counter)
    new = reused = 0
    years = Counter()
    for s in seeds:
        st = item_state(s["id"])
        status = st.get("status", "todo")
        if status == "ok" and not (ROOT / s["out"]).exists():
            status, st = "failed", dict(st, error="状态为通过但本地文件不存在（需重新下载）")
        if status != "ok":
            fails.append({"资料编号": s["id"], "类别": f"{s['cat']} {CATS[s['cat']]}", "类型": TYPES[s["type"]],
                          "标题": s["title"], "尝试来源": s.get("source", ""),
                          "状态": "未尝试" if status == "todo" else "下载/核验失败",
                          "原因": (st.get("error") or "")[:500], "访问日期": st.get("access_date", "")})
            continue
        complete = s.get("complete", "完整")
        if complete == "完整":
            prog[s["cat"]][s["type"]] += 1
        else:
            partial[s["cat"]][s["type"]] += 1
        if st.get("reused_from"):
            reused += 1
        else:
            new += 1
        y = str(s.get("year") or "")[:4]
        if y.isdigit():
            years[y] += 1
        commit = st.get("commit", "")
        if st.get("parts"):
            commit = "; ".join(f"{p['repo'].rsplit('/', 1)[-1]}@{p['commit'][:12]}" for p in st["parts"])
        paper = s.get("paper", {})
        rows.append({
            "资料编号": s["id"], "类别": f"{s['cat']} {CATS[s['cat']]}",
            "交叉类别": "; ".join(f"{c} {CATS[c]}" for c in s.get("cross", [])), "类型": TYPES[s["type"]],
            "资料形态": s.get("material", ""), "标题": s["title"], "作者或机构": s.get("authors", ""), "学校": s.get("school", ""),
            "年份": s.get("year", ""), "版本": s.get("version", ""), "语言": "英文" if s.get("lang") == "en" else s.get("lang"),
            "难度": s.get("level", ""), "先修要求": s.get("prereq", ""), "技术栈": s.get("stack", "") or s.get("tool", ""),
            "官方来源": s.get("source", ""), "下载地址": st.get("download_url", "") or st.get("reused_from", ""),
            "本地路径": s["out"], "完整性状态": "完整（已核验）" if complete == "完整" else "部分资料（已核验，范围见说明）",
            "核验结果": st.get("verify", ""), "范围说明": s.get("scope", ""), "许可证": s.get("license", ""),
            "学习目标": s.get("goal", ""), "推荐顺序": s.get("order", ""), "使用方式": s.get("use", ""),
            "访问日期": st.get("access_date", ""), "源码提交号": commit, "提交日期": st.get("commit_date", ""),
            "大小MB": size_mb(st), "来源方式": f"已有复用（{st['reused_from']}）" if st.get("reused_from") else "新下载",
            "首次公开": paper.get("first_public", ""), "发表渠道": paper.get("venue", ""), "时间窗口": paper.get("window", ""),
            "备注": s.get("note", "")})
        if s.get("tool"):
            tool_rows.append({
                "工具": s["tool"], "方向": TOOL_DIR.get(s["tool"], ""), "项目分组": s.get("project", s["tool"]),
                "资料编号": s["id"], "资料类型": {"docs": "官方文档", "practice": "官方示例源码", "course": "官方课程"}[s["type"]],
                "标题": s["title"], "官方归属": s.get("authors", ""), "版本": s.get("version", ""),
                "完整性": "完整" if complete == "完整" else "部分", "覆盖方面": "; ".join(ASPECTS[a] for a in s.get("aspects", [])),
                "下载范围": s.get("scope", ""), "入口文件": (st.get("info") or {}).get("entry", "") or s.get("entry", ""),
                "本地路径": s["out"], "源码提交号": commit, "访问日期": st.get("access_date", ""), "状态说明": s.get("note", "")})
    ok_ids = {r["资料编号"] for r in rows}
    for name, direction, ids, asp, scope in SUBTOOLS:
        have = [i for i in ids if i in ok_ids]
        tool_rows.append({"工具": name, "方向": direction, "项目分组": "（包含于其他项目文档）", "资料编号": "; ".join(have),
                          "资料类型": "官方文档（子模块）", "标题": "见关联资料编号", "官方归属": "", "版本": "随所属项目",
                          "完整性": "随所属项目", "覆盖方面": "; ".join(ASPECTS[a] for a in asp), "下载范围": scope,
                          "入口文件": "", "本地路径": "; ".join(r["本地路径"] for r in rows if r["资料编号"] in have),
                          "源码提交号": "", "访问日期": "", "状态说明": "" if len(have) == len(ids) else
                          "部分关联资料未下载成功：" + ",".join(sorted(set(ids) - set(have)))})

    for tool, cids in TOOL_COURSES.items():
        for cid in cids:
            r = next((x for x in rows if x["资料编号"] == cid), None)
            if not r:
                continue
            tool_rows.append({"工具": tool, "方向": TOOL_DIR.get(tool, ""), "项目分组": "（关联课程）", "资料编号": cid,
                              "资料类型": "大学/官方课程（关联）", "标题": r["标题"], "官方归属": r["学校"] or r["作者或机构"],
                              "版本": r["版本"], "完整性": "完整" if r["完整性状态"].startswith("完整") else "部分",
                              "覆盖方面": "课程", "下载范围": r["范围说明"] or r["资料形态"], "入口文件": "",
                              "本地路径": r["本地路径"], "源码提交号": r["源码提交号"], "访问日期": r["访问日期"],
                              "状态说明": "课程使用或讲授该工具"})

    def write(path, recs, fields=None):
        path = ROOT / path
        path.parent.mkdir(parents=True, exist_ok=True)
        fields = fields or (list(recs[0].keys()) if recs else ["空"])
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(recs)

    rows.sort(key=lambda r: r["资料编号"])
    write("catalog_cn.csv", rows)
    write("download_failures_cn.csv", fails,
          ["资料编号", "类别", "类型", "标题", "尝试来源", "状态", "原因", "访问日期"])
    tool_rows.sort(key=lambda r: (r["方向"], r["工具"], r["资料编号"]))
    write("tools/tools_catalog_cn.csv", tool_rows)
    prog_rows = []
    for c in CATS:
        rec = {"类别": f"{c} {CATS[c]}"}
        for t, (lo, hi) in TARGET.items():
            n, p = prog[c][t], partial[c][t]
            target = f"{lo}–{hi}" if t != "paper" or c in PAPER_CATS else "不设配额"
            if t == "docs" and c in NO_DOCS_CATS:
                target = "不适用"
            rec[f"{TYPES[t]}（完整）"] = n
            rec[f"{TYPES[t]}（部分）"] = p
            rec[f"{TYPES[t]}目标"] = target
            gap = "" if (t == "paper" and c not in PAPER_CATS) or target == "不适用" else ("达标" if n >= lo else f"缺 {lo - n}")
            rec[f"{TYPES[t]}状态"] = gap
        prog_rows.append(rec)
    write("progress_cn.csv", prog_rows)
    tools = {r["工具"] for r in tool_rows if r["项目分组"] not in ("（包含于其他项目文档）", "（关联课程）")}
    summary = {"verified_items": len(rows), "complete": sum(r["完整性状态"].startswith("完整") for r in rows),
               "partial": sum(r["完整性状态"].startswith("部分") for r in rows), "new": new, "reused": reused,
               "failed_or_todo": len(fails), "by_type": dict(Counter(r["类型"] for r in rows)),
               "by_type_complete": dict(Counter(r["类型"] for r in rows if r["完整性状态"].startswith("完整"))),
               "years": dict(sorted(years.items())), "tools": len(tools), "tool_rows": len(tool_rows),
               "bytes_mb": round(sum(r["大小MB"] for r in rows), 1)}
    save_json(STATE / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
