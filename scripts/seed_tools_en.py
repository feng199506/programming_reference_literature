"""Generate scripts/seeds/T_tools_en.json: versioned official docs, official examples and official
(non-university) courses for the mainstream AI frameworks/tools.  Versions pinned 2026-10-29 from
`git ls-remote` / official download listings (see search_log_cn.md).

aspects: 1 入门安装 2 用户指南/核心概念 3 API 参考 4 官方教程/工作流 5 调试/性能/FAQ
         6 保存/导出/部署/互操作 7 官方或大学课程 8 示例源码
complete: "完整" = built official docs incl. API reference;
          "部分" = source docs whose API reference is generated from docstrings at build time (not included),
                   or a documented scope subset — counted as 部分资料, never as complete.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "seeds" / "T_tools_en.json"
S = []


def add(id, cat, tool, title, org, ver, out, get, aspects, complete, scope, license, entry="", expect=None,
        cross=(), type="docs", project=None, level="入门-进阶", prereq="Python 基础", note="", order=50,
        material="官方文档", use="按需查询"):
    exp = dict(expect or {})
    if entry:
        exp.setdefault("entry", entry)
    S.append(dict(id=id, cat=cat, cross=list(cross), type=type, tool=tool, project=project or tool, title=title,
                  authors=org, school="", year=ver.get("date", "") if isinstance(ver, dict) else "",
                  version=ver["v"] if isinstance(ver, dict) else ver, lang="en", level=level, prereq=prereq,
                  stack=tool, source=get.get("repo") or get.get("start") or (get.get("urls") or [""])[0],
                  license=license, goal=scope, order=order, out=out, get=get, expect=exp, aspects=aspects,
                  complete=complete, scope=scope, material=material, use=use, note=note, entry=entry))


def gh(repo):
    return f"https://github.com/{repo}"


def git(repo, ref=None, paths=None, built=False, timeout=3600):
    g = {"kind": "git", "repo": gh(repo)}
    if ref:
        g["ref"] = ref
    if paths:
        g["paths"] = paths
    if built:
        g["built_html"] = True
        g["license_from_project"] = True
    if timeout != 3600:
        g["timeout"] = timeout
    return g


def hf(lib, ver):
    return {"kind": "hfdoc", "lib": lib, "ver": ver}


def mirror(start, include=None, quota=600, domains=None, level="inf", exclude=None, reject_regex=None, wait=0.3):
    g = {"kind": "mirror", "start": start, "quota_mb": quota, "level": level, "wait": wait}
    if include:
        g["include"] = include
    if domains:
        g["domains"] = domains
        g["span"] = True
    if exclude:
        g["exclude"] = exclude
    if reject_regex:
        g["reject_regex"] = reject_regex
    return g


def file(*urls, max_mb=800):
    return {"kind": "file", "urls": list(urls), "max_mb": max_mb}


BSD, MIT, APL, CC4 = "BSD-3-Clause", "MIT", "Apache-2.0", "CC BY 4.0"
OD = "official_docs/"
PR = "practice/"

# ------------------------------------------------------------------ 01 Python / packaging
add("01D01", "01", "Python", "Python 3.15 官方文档（教程、语言参考、标准库、C API、打包与扩展）", "Python Software Foundation",
    "3.15（docs.python.org 3.15 HTML 归档，补丁版以归档内 index 为准）", OD + "python_3.15_docs_html_en.tar.bz2",
    file("https://docs.python.org/3/archives/python-3.15-docs-html.tar.bz2"), [1, 2, 3, 4, 5, 6], "完整",
    "整个 docs.python.org/3.15 HTML 归档：tutorial/ library/ reference/ c-api/ extending/ howto/ faq/",
    "PSF-2.0（文档 PSF 许可）", entry="index.html", expect={"min_docs": 400, "must_have": ["tutorial/", "c-api/", "extending/"]},
    cross=["06", "12"], order=1, use="通读教程，其余按需查询", level="入门-高级", prereq="无")
add("01D02", "01", "pip", "pip 用户指南与参考", "Python Packaging Authority", "26.2.2", OD + "pip_26.2.2_docs_src_en.tar",
    git("pypa/pip", "26.2.2", ["docs"]), [1, 2, 3, 5], "完整", "pip 仓库 docs/html（Sphinx/MyST 源，CLI 参考由同目录 rst 指令生成参数表）",
    MIT, entry="docs/html/index.md", expect={"min_docs": 40}, cross=["06"], order=5)
add("01D03", "01", "Python Packaging User Guide", "Python Packaging User Guide（PyPA 官方打包指南）", "Python Packaging Authority",
    "main 提交（无版本号，按提交日期记录）", OD + "python_packaging_user_guide_main_src_en.tar",
    git("pypa/packaging.python.org", None, ["source"]), [1, 2, 4, 6], "完整",
    "仓库 source/：tutorials、guides、discussions、specifications（打包规范全文）", "CC BY-SA 3.0", entry="source/index.rst",
    expect={"min_docs": 60}, cross=["06"], order=6)
add("01D04", "01", "uv", "uv 文档（Python 包与项目管理器）", "Astral", "0.13.6", OD + "uv_0.13.6_docs_src_en.tar",
    git("astral-sh/uv", "0.13.6", ["docs"]), [1, 2, 3, 4, 5], "部分",
    "仓库 docs/（MkDocs Markdown：入门、概念、指南、参考）；CLI/设置参考页由代码生成，未含", "MIT OR Apache-2.0",
    entry="docs/index.md", expect={"min_docs": 40}, cross=["06"], order=7)

# ------------------------------------------------------------------ 03 scientific python
add("03D01", "03", "NumPy", "NumPy 2.5 官方文档（用户指南、API 参考、构建与 C API）", "NumPy Developers", "2.5",
    OD + "numpy_2.5_docs_html_en.tar", git("numpy/doc", None, ["2.5"], built=True), [1, 2, 3, 4, 5], "完整",
    "numpy/doc 仓库中 numpy.org/doc/2.5 的官方构建 HTML", BSD, entry="2.5/index.html",
    expect={"min_docs": 1500, "must_have": ["2.5/reference/", "2.5/user/"]}, order=10)
add("03X01", "03", "NumPy", "NumPy 官方教程笔记本（numpy-tutorials）", "NumPy Developers", "main 提交",
    PR + "numpy_tutorials_main_en.tar", git("numpy/numpy-tutorials"), [4, 8], "完整", "完整仓库（Jupyter/MyST 笔记本源，不含数据集下载）",
    BSD, expect={"min_docs": 10}, type="practice", material="官方示例/教程源码", order=11)
add("03D02", "03", "SciPy", "SciPy 1.18 官方文档", "SciPy Developers", "1.18.0", OD + "scipy_1.18.0_docs_html_en.zip",
    file("https://docs.scipy.org/doc/scipy-1.18.0/scipy-html-1.18.0.zip"),
    [1, 2, 3, 4], "完整", "docs.scipy.org 官方 HTML 压缩包 scipy-html-1.18.0.zip（1.18.1 未单独发布文档，内容以 1.18.0 为准）", BSD,
    entry="index.html", expect={"min_docs": 1000, "max_broken": 0.08}, order=12)
add("03D03", "03", "pandas", "pandas 官方文档（HTML 压缩包）", "pandas Development Team", "以压缩包内版本为准（下载 stable）",
    OD + "pandas_stable_docs_html_en.zip", file("https://pandas.pydata.org/docs/pandas.zip"), [1, 2, 3, 4, 5], "完整",
    "pandas.pydata.org 官方提供的整站 HTML 压缩包", BSD, entry="index.html", expect={"min_docs": 1000}, order=13)
add("03D04", "03", "Matplotlib", "Matplotlib 3.11.2 官方文档（教程、用户指南、示例图库、API）", "Matplotlib Development Team",
    "3.11.2", OD + "matplotlib_3.11.2_docs_html_en.tar",
    git("matplotlib/matplotlib.github.com", None, ["3.11.2"], built=True, timeout=7200), [1, 2, 3, 4, 8], "完整",
    "matplotlib.github.com 仓库 3.11.2 目录（官方构建 HTML，含 gallery）", "Matplotlib License (PSF-based)",
    entry="3.11.2/index.html", expect={"min_docs": 1500}, order=14)
add("03D05", "03", "Jupyter", "JupyterLab 4.6 官方文档", "Project Jupyter", "4.6.5", OD + "jupyterlab_4.6.5_docs_src_en.tar",
    git("jupyterlab/jupyterlab", "v4.6.5", ["docs"]), [1, 2, 4, 5], "部分",
    "仓库 docs/source（用户指南/扩展开发，Sphinx 源；扩展 API 的 TypeDoc 参考需构建，未含）", BSD,
    entry="docs/source/index.md", expect={"min_docs": 40}, order=15)
add("03D06", "03", "Jupyter", "Project Jupyter 总体文档（docs.jupyter.org）", "Project Jupyter", "main 提交",
    OD + "jupyter_docs_main_src_en.tar", git("jupyter/jupyter", None, ["docs"]), [1, 2, 5], "完整",
    "仓库 docs/source（安装、Notebook/Kernel/生态说明）", BSD, entry="docs/source/index.md", expect={"min_docs": 10},
    project="Jupyter (docs.jupyter.org)", order=16)

# ------------------------------------------------------------------ 04 classical ML + experiment management
add("04D01", "04", "scikit-learn", "scikit-learn 1.9 官方文档（用户指南、API、示例图库）", "scikit-learn developers", "1.9",
    OD + "scikit-learn_1.9_docs_html_en.tar", git("scikit-learn/scikit-learn.github.io", None, ["1.9"], built=True, timeout=7200),
    [1, 2, 3, 4, 5, 6, 8], "完整", "scikit-learn.github.io 仓库 1.9 目录（官方构建 HTML，含 auto_examples 与模型持久化章节）",
    BSD, entry="1.9/index.html", expect={"min_docs": 1000, "must_have": ["model_persistence"]}, order=20)
add("04X01", "04", "scikit-learn", "scikit-learn 1.9.1 示例源码（examples/）", "scikit-learn developers", "1.9.1",
    PR + "scikit-learn_1.9.1_examples_en.tar", git("scikit-learn/scikit-learn", "1.9.1", ["examples"]), [8], "完整",
    "仓库 examples/ 全部示例脚本", BSD, expect={"min_docs": 1, "must_have": [r"examples/.*\.py$"]}, type="practice",
    material="官方示例源码", order=21)
add("04D02", "04", "XGBoost", "XGBoost 稳定版文档（PDF）", "XGBoost Contributors / DMLC", "stable（PDF 内版本为准，对应 3.4.x）",
    OD + "xgboost_stable_docs_en.pdf", {"kind": "pdf", "urls": ["https://xgboost.readthedocs.io/_/downloads/en/stable/pdf/"]},
    [1, 2, 3, 4, 5, 6], "完整", "Read the Docs 官方构建 PDF（全部章节含 Python API 参考）", APL,
    expect={"title_words": ["xgboost"], "min_pages": 150}, order=22)
add("04X02", "04", "XGBoost", "XGBoost 3.4.2 示例与演示（demo/）", "XGBoost Contributors", "3.4.2", PR + "xgboost_3.4.2_demo_en.tar",
    git("dmlc/xgboost", "v3.4.2", ["demo"]), [8], "完整", "仓库 demo/（指南示例脚本，不含大数据）", APL,
    expect={"must_have": [r"demo/guide-python/"]}, type="practice", material="官方示例源码", order=23)
add("04D03", "04", "LightGBM", "LightGBM 稳定版文档（PDF）", "Microsoft", "stable（PDF 内版本为准，对应 4.7.x）",
    OD + "lightgbm_stable_docs_en.pdf", {"kind": "pdf", "urls": ["https://lightgbm.readthedocs.io/_/downloads/en/stable/pdf/"]},
    [1, 2, 3, 4, 5], "完整", "Read the Docs 官方构建 PDF（参数、Python API、调参、GPU）", MIT,
    expect={"title_words": ["lightgbm"], "min_pages": 80}, order=24)
add("04X03", "04", "LightGBM", "LightGBM 4.7.0 示例（examples/）", "Microsoft", "4.7.0", PR + "lightgbm_4.7.0_examples_en.tar",
    git("microsoft/LightGBM", "v4.7.0", ["examples"]), [8], "完整", "仓库 examples/", MIT, type="practice",
    material="官方示例源码", expect={"must_have": ["examples/python-guide"]}, order=25)
add("04D04", "04", "CatBoost", "CatBoost 1.2.10 官方文档源（英文）", "Yandex / CatBoost", "1.2.10",
    OD + "catboost_1.2.10_docs_src_en.tar", git("catboost/catboost", "v1.2.10", ["catboost/docs/en"]), [1, 2, 3, 4, 5, 6],
    "完整", "仓库 catboost/docs/en（YFM Markdown，catboost.ai/docs 的源；参数与 Python API 页为手写 Markdown）", APL,
    entry="catboost/docs/en/toc.yaml", expect={"min_docs": 200}, order=26)
add("04X04", "04", "CatBoost", "CatBoost 官方教程（catboost/tutorials）", "Yandex / CatBoost", "master 提交",
    PR + "catboost_tutorials_master_en.tar", git("catboost/tutorials"), [4, 8], "完整", "完整教程仓库（笔记本）", APL,
    type="practice", material="官方示例/教程源码", expect={"min_docs": 10}, order=27)
add("04D05", "04", "MLflow", "MLflow 3.17.2 文档源（Docusaurus）", "MLflow Project (LF AI & Data)", "3.17.2",
    OD + "mlflow_3.17.2_docs_src_en.tar", git("mlflow/mlflow", "v3.17.2", ["docs/docs", "docs/api_reference/source"]),
    [1, 2, 4, 5, 6], "部分", "docs/docs（经典 ML 与 GenAI 指南、部署、模型格式）+ docs/api_reference/source（Sphinx 源；API 正文由 docstring 生成，未含）",
    APL, entry="docs/docs/classic-ml/index.mdx", expect={"min_docs": 200}, order=40)
add("04X05", "04", "MLflow", "MLflow 3.17.2 示例（examples/）", "MLflow Project", "3.17.2", PR + "mlflow_3.17.2_examples_en.tar",
    git("mlflow/mlflow", "v3.17.2", ["examples"]), [8], "完整", "仓库 examples/", APL, type="practice",
    material="官方示例源码", expect={"min_docs": 5}, order=41)
add("04D06", "04", "DVC", "DVC 官方文档源（dvc.org 仓库 content/docs）", "Iterative / DVC 维护方", "main 提交（对应 DVC 3.67.x）",
    OD + "dvc_docs_main_src_en.tar", git("iterative/dvc.org", None, ["content/docs"]), [1, 2, 3, 4, 5], "完整",
    "content/docs：安装、入门、用户指南、命令参考（全部为手写 Markdown）", APL, entry="content/docs/index.md",
    expect={"min_docs": 150, "must_have": ["content/docs/command-reference"]}, order=42)
add("04D07", "04", "Weights & Biases", "W&B 官方文档源（wandb/docs）", "Weights & Biases（CoreWeave 旗下）", "main 提交",
    OD + "wandb_docs_main_src_en.tar", git("wandb/docs", None, ["models", "guides", "ref", "get-started.mdx", "index.mdx",
                                                              "quickstart.mdx", "tutorials", "support", "platform"]),
    [1, 2, 3, 4, 5], "完整", "wandb/docs 仓库英文主体（Mintlify MDX；SDK 参考 ref/ 已生成提交）", "Apache-2.0（以仓库 LICENSE 为准）",
    expect={"min_docs": 200}, order=44)
add("04X07", "04", "Weights & Biases", "W&B 官方示例（wandb/examples）", "Weights & Biases", "master 提交",
    PR + "wandb_examples_master_en.tar", git("wandb/examples"), [4, 8], "完整", "完整示例仓库（笔记本与脚本）", MIT, type="practice",
    material="官方示例源码", expect={"min_docs": 20}, order=45)
add("04D08", "04", "TensorBoard", "TensorBoard 2.21.0 官方指南（docs/）", "TensorFlow Authors", "2.21.0",
    OD + "tensorboard_2.21.0_docs_src_en.tar", git("tensorflow/tensorboard", "2.21.0", ["docs"]), [1, 2, 4, 5], "完整",
    "仓库 docs/：入门、标量/图像/图/超参/性能剖析笔记本与调试器 V2 指南", APL, entry="docs/get_started.ipynb",
    expect={"min_docs": 10}, cross=["05"], order=46)

# ------------------------------------------------------------------ 05 deep learning frameworks
add("05D01", "05", "PyTorch", "PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）", "PyTorch Foundation",
    "2.15", OD + "pytorch_2.15_docs_html_en.tar", git("pytorch/docs", "site", ["2.15"], built=True, timeout=7200),
    [1, 2, 3, 5, 6], "完整", "pytorch/docs 仓库（docs.pytorch.org 发布分支）2.15 目录的官方构建 HTML", BSD,
    entry="2.15/index.html", expect={"min_docs": 1500, "must_have": ["2.15/distributed", "2.15/export", "2.15/onnx",
                                                                    "2.15/profiler"]}, order=1, level="入门-高级")
add("05D02", "05", "PyTorch", "PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）", "PyTorch Foundation",
    "gh-pages 提交（按提交日期记录）", OD + "pytorch_tutorials_html_en.tar",
    git("pytorch/tutorials", "gh-pages", ["*.html", "_static", "_images", "_sources", "beginner", "intermediate", "advanced",
                                          "recipes", "prototype", "unstable", "_sphinx_design_static"], built=True, timeout=7200),
    [1, 4, 5, 6, 7], "完整", "docs.pytorch.org/tutorials 发布分支的构建 HTML（不含 _downloads 下的笔记本压缩包）", BSD,
    entry="index.html", expect={"min_docs": 200, "max_broken": 0.10}, project="PyTorch Tutorials", order=2)
add("05X01", "05", "PyTorch", "PyTorch 官方示例（pytorch/examples）", "PyTorch Foundation", "main 提交",
    PR + "pytorch_examples_main_en.tar", git("pytorch/examples"), [8], "完整", "完整仓库（MNIST、ImageNet、DDP/FSDP、C++ 前端等）",
    BSD, type="practice", material="官方示例源码", expect={"must_have": ["distributed/"]}, order=3)
add("05D03", "05", "torchvision", "torchvision 0.29 官方文档", "PyTorch Foundation", "0.29", OD + "torchvision_0.29_docs_html_en.tar",
    git("pytorch/vision", "gh-pages", ["0.29"], built=True), [1, 2, 3, 4, 8], "完整",
    "pytorch/vision gh-pages 0.29 目录（构建 HTML，含 transforms v2 与 gallery）", BSD, entry="0.29/index.html",
    expect={"min_docs": 200}, order=4)
add("05D04", "05", "torchaudio", "torchaudio 2.11 官方文档", "PyTorch Foundation", "2.11", OD + "torchaudio_2.11_docs_html_en.tar",
    git("pytorch/audio", "gh-pages", ["2.11.0"], built=True), [1, 2, 3, 4], "完整", "pytorch/audio gh-pages 2.11.0 目录（构建 HTML；2.11 为指向它的链接）",
    "BSD-2-Clause", entry="2.11.0/index.html", expect={"min_docs": 50}, order=5,
    note="torchaudio 自 2.8 起进入维护期并移除/迁移大量功能（解码迁至 TorchCodec），以文档内说明为准")
add("05D05", "05", "TensorFlow", "TensorFlow 官方指南与教程源（tensorflow/docs site/en）", "TensorFlow Authors / Google",
    "master 提交（对应 TF 2.21）", OD + "tensorflow_docs_guides_master_src_en.tar",
    git("tensorflow/docs", None, ["site/en/guide", "site/en/tutorials", "site/en/install", "site/en/README.md"]),
    [1, 2, 4, 5, 6, 8], "完整", "site/en/guide、tutorials、install（可运行笔记本与 Markdown，含 SavedModel、分布式、性能剖析、TF Lite 导出）",
    APL, expect={"min_docs": 100, "must_have": ["saved_model", "distributed"]}, order=10)
add("05D06", "05", "TensorFlow", "TensorFlow Python API 参考（tensorflow.org/api_docs/python 离线镜像）", "TensorFlow Authors / Google",
    "tensorflow.org 当前稳定版（镜像页内版本为准，对应 2.21）", OD + "tensorflow_api_docs_python_mirror_en.tar.gz",
    mirror("https://www.tensorflow.org/api_docs/python/tf", include=["/api_docs/python", "/static", "/_static"], quota=6000,
           exclude=["/api_docs/python/tf/compat"],
           reject_regex=r"(\?hl=|\?authuser=|/_d/|/s/opensearch|\.(png|jpg|gif|svg)$)", wait=0.2),
    [3], "部分", "tensorflow.org/api_docs/python 下 tf.* API 页的部分镜像：排除 tf.compat；wget 在 90 分钟超时处停止，已抓取约 3900 页（含 tf.raw_ops、tf.keras、tf.math/nn/data/distribute 等），其余页面缺失；因中断未做链接本地化（页面可离线阅读，页间链接仍指向 tensorflow.org）；不含图片；gzip 压缩", APL,
    entry="api_docs/python/tf.html", expect={"min_docs": 2000, "max_broken": 0.6}, project="TensorFlow", order=11)
add("05D07", "05", "Keras", "Keras 3 官方指南与示例源（keras-io）", "Keras Team / Google", "master 提交（对应 Keras 3.15）",
    OD + "keras_io_master_src_en.tar", git("keras-team/keras-io", None, ["guides", "examples", "templates"]),
    [1, 2, 4, 5, 6, 8], "完整", "guides/、examples/（.py 源 + 生成的 .md）、templates/（入门与 API 页模板）", APL,
    expect={"min_docs": 200, "must_have": ["guides/md/", "examples/vision/md/"]}, order=12)
add("05D08", "05", "Keras", "Keras 3 API 参考（keras.io/api 离线镜像）", "Keras Team / Google", "keras.io 当前版本（3.15）",
    OD + "keras_api_reference_mirror_en.tar", mirror("https://keras.io/api/", include=["/api", "/css", "/js", "/img", "/getting_started"],
                                                     quota=400), [1, 3, 6], "完整", "keras.io/api/ 全部 API 页面 + 入门页", APL,
    entry="api/index.html", expect={"min_docs": 200, "max_broken": 0.10}, project="Keras", order=13)
add("05D09", "05", "JAX", "JAX 官方文档（Read the Docs HTML 包）", "JAX Authors / Google", "latest（构建内版本为准，对应 jax 0.12）",
    OD + "jax_latest_docs_html_en.zip", file("https://docs.jax.dev/_/downloads/en/latest/htmlzip/"), [1, 2, 3, 4, 5, 6], "完整",
    "Read the Docs 官方 HTML 包（单页构建 singlehtml：全部章节合并于 index.html；教程、sharding/分布式、API 参考、导出与序列化）", APL, entry="index.html",
    expect={"min_docs": 1, "link_check": False}, order=14)
add("05D10", "05", "OpenCV", "OpenCV 5.0.0 官方文档（Doxygen HTML 包，含 Python 教程）", "OpenCV team", "5.0.0",
    OD + "opencv_5.0.0_docs_html_en.zip", file("https://github.com/opencv/opencv/releases/download/5.0.0/opencv-5.0.0-docs.zip"),
    [1, 2, 3, 4, 6], "完整", "GitHub release 附带的完整文档包（模块 API、C++/Python 教程、DNN 模块 ONNX 导入）", APL,
    entry="index.html", expect={"min_docs": 2000, "link_check": False}, order=20)
add("05X02", "05", "OpenCV", "OpenCV 5.0.0 示例（samples/）", "OpenCV team", "5.0.0", PR + "opencv_5.0.0_samples_en.tar",
    git("opencv/opencv", "5.0.0", ["samples"]), [8], "完整", "仓库 samples/（python、cpp、dnn 示例；大于 5MB 的数据文件剔除）", APL,
    type="practice", material="官方示例源码", expect={"must_have": ["samples/python/"]}, order=21)
add("05D11", "05", "Pillow", "Pillow 稳定版文档（PDF）", "Jeffrey A. Clark and contributors", "stable（PDF 内版本为准，对应 13.0）",
    OD + "pillow_stable_docs_en.pdf", {"kind": "pdf", "urls": ["https://pillow.readthedocs.io/_/downloads/en/stable/pdf/"]},
    [1, 2, 3, 4], "完整", "Read the Docs 官方构建 PDF（手册、参考、图像格式）", "MIT-CMU", expect={"title_words": ["pillow"],
                                                                                          "min_pages": 100}, order=22)
add("05D12", "05", "Albumentations", "Albumentations 2.0.8 文档源与 README（原项目，已转维护）", "Albumentations Team", "2.0.8",
    OD + "albumentations_2.0.8_docs_src_en.tar", git("albumentations-team/albumentations", "2.0.8", ["docs", "README.md"]),
    [1, 2, 4], "部分", "仓库 README 与 docs/（变换列表与贡献说明；albumentations.ai 在线文档已转向 AlbumentationsX，未整站保存）",
    MIT, expect={"min_docs": 2}, order=23, note="原 albumentations 仓库已停止活跃开发，后续版本以 AlbumentationsX（AGPL-3.0/商业双许可）发布，执行时以 README 声明为准")
add("05D13", "05", "Albumentations", "AlbumentationsX 2.5.1 源码仓库（含 README 与示例）", "Albumentations Team", "2.5.1",
    PR + "albumentationsx_2.5.1_src_en.tar", git("albumentations-team/AlbumentationsX", "2.5.1"), [1, 8], "部分",
    "完整源码仓库（README、docs、benchmark；在线文档未整站保存）", "AGPL-3.0 / 商业双许可（以仓库为准）", type="practice",
    material="官方源码与示例", expect={"min_docs": 2}, project="AlbumentationsX", order=24)
for i, (lib, ver, tool, title, asp, mh) in enumerate([
        ("transformers", "v5.21.1", "Transformers", "Transformers 文档（含 API、导出与推理部署）", [1, 2, 3, 4, 5, 6], ["main_classes"]),
        ("datasets", "v5.1.0", "Datasets", "Datasets 文档", [1, 2, 3, 4, 5], ["package_reference"]),
        ("tokenizers", "v0.23.3", "Tokenizers", "Tokenizers 文档", [1, 2, 3], ["api"]),
        ("accelerate", "v1.15.0", "Accelerate", "Accelerate 文档（分布式、FSDP/DeepSpeed 集成、调试）", [1, 2, 3, 4, 5], ["package_reference"]),
        ("peft", "v0.21.0", "PEFT", "PEFT 文档（LoRA 等参数高效微调）", [1, 2, 3, 4, 6], ["package_reference"]),
        ("trl", "v1.17.0", "TRL", "TRL 文档（SFT/DPO/GRPO 等训练器）", [1, 2, 3, 4], ["trainer"]),
        ("diffusers", "v0.42.1", "Diffusers", "Diffusers 文档", [1, 2, 3, 4, 5, 6], ["api/"]),
        ("evaluate", "v0.4.6", "Evaluate", "Evaluate 文档", [1, 2, 3, 4], ["package_reference"]),
        ("huggingface_hub", "v2.4.0", "Hub 客户端（huggingface_hub）", "huggingface_hub 客户端文档", [1, 2, 3, 4], ["package_reference"])]):
    add(f"05D{20 + i}", "05", tool, f"Hugging Face {title} {ver}", "Hugging Face", ver, OD + f"hf_{lib}_{ver}_docs_built_en.zip",
        hf(lib, ver), asp, "完整", f"hf-doc-build 官方构建包 {lib}/{ver}.zip（en 子目录：渲染后的 Markdown 含 API 正文 + 页面片段）",
        APL, expect={"min_docs": 20, "must_have": [f"{lib}/{ver}/en/"] + [f"/en/.*{m}" for m in mh]}, order=30 + i,
        note=("Evaluate 官方已推荐新项目改用 LightEval 等工具，库仍可用（以文档首页声明为准）" if lib == "evaluate" else
              "hf-doc-build 中 v5.22.0 构建包缺少 en 目录（仅含译文），故取 v5.21.1 完整构建" if lib == "transformers" else ""))
add("05D29", "05", "Transformers", "Hugging Face Optimum ONNX v0.1.0 文档（Transformers → ONNX 导出与 ONNX Runtime 推理）", "Hugging Face",
    "v0.1.0", OD + "hf_optimum-onnx_v0.1.0_docs_built_en.zip", hf("optimum-onnx", "v0.1.0"), [1, 2, 3, 4, 6], "完整",
    "hf-doc-build 官方构建包 optimum-onnx/v0.1.0.zip（en：导出指南、支持架构、ORTModel API）", APL,
    expect={"min_docs": 10, "must_have": ["optimum-onnx/v0.1.0/en/"]}, project="Optimum ONNX", order=39,
    note="Transformers v5 文档的 serialization 页指向 Optimum ONNX 作为官方 ONNX 导出路径")
for i, (repo, ref, paths, tool, title) in enumerate([
        ("huggingface/transformers", "v5.22.0", ["examples"], "Transformers", "Transformers v5.22.0 官方示例脚本（examples/）"),
        ("huggingface/notebooks", None, None, "Transformers", "Hugging Face 官方笔记本（huggingface/notebooks）"),
        ("huggingface/diffusers", "v0.42.1", ["examples"], "Diffusers", "Diffusers v0.42.1 训练/推理示例（examples/）"),
        ("huggingface/peft", "v0.21.2", ["examples"], "PEFT", "PEFT v0.21.2 示例（examples/）"),
        ("huggingface/trl", "v1.17.0", ["examples"], "TRL", "TRL v1.17.0 示例（examples/）"),
        ("huggingface/accelerate", "v1.15.0", ["examples"], "Accelerate", "Accelerate v1.15.0 示例（examples/）")]):
    add(f"05X{10 + i}", "05", tool, title, "Hugging Face", ref or "main 提交",
        PR + f"hf_{repo.split('/')[1]}_{(ref or 'main')}_examples_en.tar", git(repo, ref, paths), [8], "完整",
        "官方仓库示例目录（不下载模型权重/数据集）", APL, type="practice", material="官方示例源码", expect={"min_docs": 1}, order=40 + i)

# ------------------------------------------------------------------ official (non-university) courses tied to tools
add("05C50", "05", "Transformers", "Hugging Face LLM Course（构建版，含 Transformers/Datasets/Tokenizers/微调/推理）", "Hugging Face",
    "main 构建包", "courses/hf_llm_course_main_built_en.zip", hf("course", "main"), [7, 4], "完整",
    "hf-doc-build course/main.zip（全部章节；仅保留其中英文与中文在包内原样）", APL, expect={"min_docs": 50}, type="course",
    material="官方课程（非大学）", project="Hugging Face LLM Course", order=60, use="通读")
add("15C50", "15", "smolagents / Agents", "Hugging Face Agents Course（仓库源）", "Hugging Face", "main 提交",
    "courses/hf_agents_course_main_src_en.tar", git("huggingface/agents-course", None, ["units/en", "README.md", "LICENSE"]),
    [7, 4, 8], "完整", "units/en 全部单元（MDX 与笔记本）", APL, expect={"min_docs": 30}, type="course",
    material="官方课程（非大学）", project="Hugging Face Agents Course", order=60, use="通读")
add("05C51", "05", "Diffusers", "Hugging Face Diffusion Models Class（仓库源）", "Hugging Face", "main 提交",
    "courses/hf_diffusion_models_class_main_src_en.tar", git("huggingface/diffusion-models-class"), [7, 4, 8], "完整",
    "完整课程仓库（各单元 Markdown 与笔记本）", APL, expect={"min_docs": 10}, type="course", material="官方课程（非大学）",
    project="Hugging Face Diffusion Models Class", order=61, use="通读")

# ------------------------------------------------------------------ 13 GPU programming & training optimisation
add("13D01", "13", "CUDA", "CUDA Toolkit 核心指南 PDF 集（编程指南、最佳实践、PTX ISA）", "NVIDIA", "CUDA 13.x（PDF 内版本为准）",
    OD + "cuda_toolkit_guides_pdf_en", {"kind": "pdfset", "urls": [
        "https://docs.nvidia.com/cuda/pdf/CUDA_C_Programming_Guide.pdf",
        "https://docs.nvidia.com/cuda/pdf/CUDA_C_Best_Practices_Guide.pdf",
        "https://docs.nvidia.com/cuda/pdf/ptx_isa_9.0.pdf",
        "https://docs.nvidia.com/cuda/pdf/CUDA_Installation_Guide_Linux.pdf",
        "https://docs.nvidia.com/cuda/pdf/CUDA_Runtime_API.pdf"], "min_files": 5},
    [1, 2, 3, 5], "完整", "docs.nvidia.com/cuda/pdf 下 5 份官方 PDF", "NVIDIA 文档许可（仅个人保存）", order=1, level="进阶-高级",
    prereq="C/C++、计算机体系结构", use="编程指南通读，其余查询")
add("13D02", "13", "CUDA", "Nsight Compute / Nsight Systems 性能分析文档（离线镜像）", "NVIDIA", "当前版本（镜像页内为准）",
    OD + "nsight_profiling_docs_mirror_en.tar",
    mirror(["https://docs.nvidia.com/nsight-compute/index.html", "https://docs.nvidia.com/nsight-systems/index.html"],
           include=["/nsight-compute", "/nsight-systems", "/_static"], quota=500, level="4"),
    [5], "完整", "docs.nvidia.com/nsight-compute 与 nsight-systems 文档页（深度 4）", "NVIDIA 文档许可（仅个人保存）",
    entry="index.html", expect={"min_docs": 20, "max_broken": 0.15}, project="CUDA", order=2)
add("13X01", "13", "CUDA", "NVIDIA cuda-samples v13.4", "NVIDIA", "v13.4", PR + "cuda_samples_v13.4_en.tar",
    git("NVIDIA/cuda-samples", "v13.4"), [8], "完整", "完整仓库（不编译不运行）", BSD, type="practice", material="官方示例源码",
    expect={"must_have": ["cpp/"]}, order=3)
add("13D03", "13", "Triton 编程语言", "Triton 编程语言官方文档（triton-lang.org 构建 HTML，含教程）", "OpenAI / Triton 社区",
    "main 构建（gh-pages 提交日期记录；对应 v3.9 之后）", OD + "triton_lang_docs_main_html_en.tar",
    git("triton-lang/triton", "gh-pages", ["main"], built=True), [1, 2, 3, 4], "完整",
    "gh-pages 分支 main/ 目录（入门、矩阵乘/融合注意力等教程、Python API）", MIT, entry="main/index.html",
    expect={"min_docs": 30}, order=10, note="Triton 编程语言（GPU 内核 DSL），与 NVIDIA Triton Inference Server 无关")
add("13X02", "13", "Triton 编程语言", "Triton v3.9.0 教程源码（python/tutorials）", "OpenAI / Triton 社区", "v3.9.0",
    PR + "triton_lang_v3.9.0_tutorials_en.tar", git("triton-lang/triton", "v3.9.0", ["python/tutorials"]), [4, 8], "完整",
    "仓库 python/tutorials", MIT, type="practice", material="官方示例源码", expect={"must_have": ["python/tutorials/"]}, order=11)
add("13D04", "13", "DeepSpeed", "DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源）", "DeepSpeed (LF AI & Data)", "0.19.8",
    OD + "deepspeed_0.19.8_docs_src_en.tar", git("deepspeedai/DeepSpeed", "v0.19.8", ["docs"]), [1, 2, 4, 5], "部分",
    "docs/_tutorials、_pages（ZeRO、配置 JSON、推理）+ docs/code-docs（Sphinx 源；API 正文由 docstring 生成，未含）", APL,
    expect={"min_docs": 60, "must_have": ["docs/_tutorials/"]}, order=12)
add("13D05", "13", "DeepSpeed", "DeepSpeed API 参考（deepspeed.readthedocs.io 离线镜像）", "DeepSpeed", "latest（页内版本为准）",
    OD + "deepspeed_api_rtd_mirror_en.tar", mirror("https://deepspeed.readthedocs.io/en/latest/", include=["/en/latest"], quota=200),
    [3], "完整", "deepspeed.readthedocs.io/en/latest 全部页面", APL, entry="index.html", expect={"min_docs": 20},
    project="DeepSpeed", order=13)
add("13X03", "13", "DeepSpeed", "DeepSpeedExamples", "DeepSpeed", "master 提交", PR + "deepspeed_examples_master_en.tar",
    git("deepspeedai/DeepSpeedExamples"), [8], "完整", "完整示例仓库（训练/推理/压缩）", APL, type="practice",
    material="官方示例源码", expect={"min_docs": 10}, order=14)
add("13D06", "13", "NCCL", "NCCL 用户指南（离线镜像）", "NVIDIA", "当前版本（页内为准）", OD + "nccl_user_guide_mirror_en.tar",
    mirror("https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/index.html", include=["/deeplearning/nccl/user-guide"],
           quota=100), [1, 2, 3, 5], "完整", "NCCL 用户指南全部页面（集合通信、环境变量、排障）", "NVIDIA 文档许可（仅个人保存）",
    entry="index.html", expect={"min_docs": 15}, order=15)

# ------------------------------------------------------------------ 14 model exchange, inference & deployment
add("14D01", "14", "ONNX", "ONNX 官方文档（onnx.ai/onnx 离线镜像：概念、Python API、算子）", "ONNX (LF AI & Data)", "当前站点（对应 1.23.x）",
    OD + "onnx_docs_site_mirror_en.tar", mirror("https://onnx.ai/onnx/", include=["/onnx"], quota=600),
    [1, 2, 3, 4, 6], "完整", "onnx.ai/onnx/ 下全部页面（intro、api、operators、repo-docs）", APL, entry="onnx/index.html",
    expect={"min_docs": 300, "max_broken": 0.08}, order=1)
add("14D02", "14", "ONNX", "ONNX v1.23.2 规范与设计文档（docs/）", "ONNX", "1.23.2", OD + "onnx_1.23.2_spec_docs_en.tar",
    git("onnx/onnx", "v1.23.2", ["docs"]), [2, 3, 6], "完整", "仓库 docs/（IR.md、Operators.md、Versioning、PythonAPIOverview 等）", APL,
    expect={"must_have": [r"docs/IR\.md", r"docs/Operators\.md"]}, project="ONNX", order=2)
add("14X01", "14", "ONNX", "ONNX 官方教程仓库（onnx/tutorials）", "ONNX", "main 提交", PR + "onnx_tutorials_main_en.tar",
    git("onnx/tutorials"), [4, 6, 8], "完整", "完整仓库（各框架转换教程笔记本）", APL, type="practice", material="官方示例源码",
    expect={"min_docs": 10}, order=3, note="仓库更新较少，部分转换器已过时，以 README 为准")
add("14D03", "14", "ONNX Runtime", "ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）", "Microsoft",
    "gh-pages 提交（对应 1.31.x）", OD + "onnxruntime_docs_ghpages_en.tar", git("microsoft/onnxruntime", "gh-pages", ["docs"]),
    [1, 2, 3, 4, 5, 6], "完整", "gh-pages docs/：安装、执行提供程序、性能调优、模型优化/量化、各语言 API（python API 为构建 HTML）", MIT,
    entry="docs/index.md", expect={"min_docs": 150, "must_have": ["docs/performance", "docs/execution-providers",
                                                                  "docs/api/python"]}, order=4)
add("14X02", "14", "ONNX Runtime", "ONNX Runtime 推理示例（onnxruntime-inference-examples）", "Microsoft", "main 提交",
    PR + "onnxruntime_inference_examples_main_en.tar", git("microsoft/onnxruntime-inference-examples"), [8], "完整",
    "完整示例仓库（Python/C++/C#/移动端/量化）", MIT, type="practice", material="官方示例源码", expect={"min_docs": 20}, order=5)
add("14D04", "14", "TensorRT", "TensorRT 官方文档（离线镜像）", "NVIDIA", "latest（页内版本为准，对应 10.x）",
    OD + "tensorrt_docs_latest_mirror_en.tar",
    mirror("https://docs.nvidia.com/deeplearning/tensorrt/latest/index.html", include=["/deeplearning/tensorrt/latest"],
           quota=800), [1, 2, 3, 5, 6], "完整", "docs.nvidia.com/deeplearning/tensorrt/latest 全部页面（安装、开发者指南、API、性能、ONNX 解析）",
    "NVIDIA 文档许可（仅个人保存）", entry="index.html", expect={"min_docs": 50, "max_broken": 0.10}, order=6)
add("14X03", "14", "TensorRT", "TensorRT OSS v10.16 示例与工具（samples、tools）", "NVIDIA", "v10.16", PR + "tensorrt_oss_v10.16_samples_en.tar",
    git("NVIDIA/TensorRT", "v10.16", ["samples", "tools", "quickstart"]), [4, 8], "完整", "samples/、tools/（Polygraphy 等）、quickstart/",
    APL, type="practice", material="官方示例源码", expect={"must_have": ["samples/"]}, order=7)
add("14D05", "14", "OpenVINO", "OpenVINO 2026.4.1 文档源（articles_en）", "Intel", "2026.4.1", OD + "openvino_2026.4.1_docs_src_en.tar",
    git("openvinotoolkit/openvino", "2026.4.1", ["docs/articles_en", "docs/snippets", "docs/optimization_guide"]),
    [1, 2, 4, 5, 6], "部分", "docs/articles_en（RST 源：安装、模型转换、推理、优化）；Python/C++ API 参考由构建生成，未含", APL,
    expect={"min_docs": 300}, order=8)
add("14X04", "14", "OpenVINO", "OpenVINO Notebooks（官方教程笔记本）", "Intel", "latest 分支提交", PR + "openvino_notebooks_latest_en.tar",
    git("openvinotoolkit/openvino_notebooks", "latest"), [4, 8], "完整", "完整仓库（教程笔记本，不含模型）", APL, type="practice",
    material="官方示例源码", expect={"min_docs": 50}, order=9)
add("14D06", "14", "vLLM", "vLLM v0.32.0 文档源与示例", "vLLM 项目", "0.32.0", OD + "vllm_0.32.0_docs_src_en.tar",
    git("vllm-project/vllm", "v0.32.0", ["docs", "examples"]), [1, 2, 4, 5, 6, 8], "部分",
    "docs/（入门、部署、服务、配置、设计）+ examples/；API 参考页由 mkdocstrings 生成，未含", APL,
    entry="docs/README.md", expect={"min_docs": 150}, order=20)
add("14D07", "14", "llama.cpp", "llama.cpp b11985 文档、工具说明与示例", "ggml-org", "b11985", OD + "llama.cpp_b11985_docs_src_en.tar",
    git("ggml-org/llama.cpp", "b11985", ["docs", "examples", "tools", "grammars", "gguf-py/README.md"]),
    [1, 2, 4, 5, 6, 8], "完整", "docs/（构建、后端、量化）、tools/（server、quantize 等 README 与源码）、examples/", MIT,
    expect={"min_docs": 40, "must_have": ["docs/build.md", "tools/server/README.md"]}, order=21)
add("14D08", "14", "Triton Inference Server", "NVIDIA Triton Inference Server v2.73.0 文档（server/docs）", "NVIDIA", "2.73.0",
    OD + "triton_inference_server_2.73.0_docs_src_en.tar", git("triton-inference-server/server", "v2.73.0", ["docs", "qa/README.md"]),
    [1, 2, 3, 4, 5, 6], "完整", "仓库 docs/（用户指南、模型仓库/配置、协议、性能分析器、后端），即 NVIDIA 文档站的源", BSD,
    entry="docs/index.md", expect={"min_docs": 60}, order=22,
    note="推理服务器（NVIDIA，2025 起品牌为 Dynamo Triton），与 Triton 编程语言无关")
add("14X05", "14", "Triton Inference Server", "Triton Inference Server 官方教程（tutorials）", "NVIDIA", "main 提交",
    PR + "triton_inference_server_tutorials_main_en.tar", git("triton-inference-server/tutorials"), [4, 8], "完整",
    "完整教程仓库（概念指南、部署示例）", BSD, type="practice", material="官方示例源码", expect={"min_docs": 20}, order=23)
add("14D09", "14", "BentoML", "BentoML 文档（docs.bentoml.com 离线镜像）", "BentoML", "latest（页内版本为准，对应 1.4.40）",
    OD + "bentoml_docs_mirror_en.tar", mirror("https://docs.bentoml.com/en/latest/", include=["/en/latest"], quota=400),
    [1, 2, 3, 4, 6], "完整", "docs.bentoml.com/en/latest 全部页面（含 API 参考）", APL, entry="index.html",
    expect={"min_docs": 60, "max_broken": 0.10}, order=24)
add("14X06", "14", "BentoML", "BentoML v1.4.40 示例（examples/）", "BentoML", "1.4.40", PR + "bentoml_1.4.40_examples_en.tar",
    git("bentoml/BentoML", "v1.4.40", ["examples"]), [8], "完整", "仓库 examples/", APL, type="practice", material="官方示例源码",
    expect={"min_docs": 5}, order=25)
add("14D10", "14", "Docker", "Docker 官方文档源（docker/docs content）", "Docker Inc.", "main 提交", OD + "docker_docs_main_src_en.tar",
    git("docker/docs", None, ["content/manuals/engine", "content/manuals/compose", "content/manuals/build", "content/get-started",
                              "content/guides", "content/reference/dockerfile.md", "content/reference/compose-file",
                              "content/manuals/desktop/setup", "data/engine-cli", "data/buildx"], timeout=5400),
    [1, 2, 4, 5, 6], "部分", "Engine、Build、Compose、入门与指南、Compose 文件参考；Dockerfile/CLI 参考在构建时自 buildkit 与 docker/cli 引入，另见 14D12/14D13", "Apache-2.0",
    expect={"min_docs": 300, "must_have": ["content/manuals/engine/"]}, cross=["07"], order=30)
add("14D12", "14", "Docker", "Dockerfile 参考（moby/buildkit frontend/dockerfile/docs）", "Docker Inc. / Moby", "master 提交",
    OD + "dockerfile_reference_buildkit_master_en.tar", git("moby/buildkit", None, ["frontend/dockerfile/docs"]), [3], "完整",
    "Dockerfile 指令参考、语法与构建检查规则（docs.docker.com/reference/dockerfile 的源）", APL,
    expect={"must_have": ["frontend/dockerfile/docs/reference.md"]}, order=30)
add("14D13", "14", "Docker", "Docker CLI 命令参考（docker/cli docs/reference）", "Docker Inc.", "master 提交",
    OD + "docker_cli_reference_master_en.tar", git("docker/cli", None, ["docs/reference"]), [3], "完整",
    "docker 全部子命令参考与 dockerd 参考（docs.docker.com CLI 参考页的源）", APL, expect={"min_docs": 100}, order=30)
add("14X07", "14", "Docker", "Docker awesome-compose 示例", "Docker Inc.", "master 提交", PR + "docker_awesome_compose_master_en.tar",
    git("docker/awesome-compose"), [8], "完整", "完整仓库（多服务 Compose 示例）", "CC0-1.0", type="practice",
    material="官方示例源码", expect={"min_docs": 20}, order=31)
add("14D11", "14", "Kubernetes", "Kubernetes 官方文档源（website content/en）", "Kubernetes Authors (CNCF)", "main 提交（对应当前发布版）",
    OD + "kubernetes_docs_main_src_en.tar", git("kubernetes/website", None, ["content/en/docs"], timeout=5400),
    [1, 2, 3, 4, 5, 6], "完整", "content/en/docs：概念、任务、教程、参考（kubectl 与 API 参考页已生成提交）", "CC BY 4.0",
    expect={"min_docs": 800, "must_have": ["content/en/docs/reference/kubernetes-api"]}, order=32)
add("14X08", "14", "Kubernetes", "Kubernetes 官方示例（kubernetes/examples）", "Kubernetes Authors", "master 提交",
    PR + "kubernetes_examples_master_en.tar", git("kubernetes/examples"), [8], "完整", "完整仓库", APL, type="practice",
    material="官方示例源码", expect={"min_docs": 10}, order=33)

# ------------------------------------------------------------------ 15 retrieval & AI apps
add("15D01", "15", "Sentence Transformers", "Sentence Transformers 文档（sbert.net 离线镜像）", "UKP Lab / Hugging Face",
    "当前站点（对应 v6.2.0）", OD + "sentence_transformers_sbert_mirror_en.tar",
    mirror("https://www.sbert.net/index.html", include=["/docs", "/examples", "/_static", "/_images", "/"], quota=400,
           reject_regex=r"/(_modules)/"), [1, 2, 3, 4, 6], "完整", "sbert.net 全站（用户指南、包参考、示例说明）", APL,
    entry="index.html", expect={"min_docs": 80, "max_broken": 0.10}, order=1)
add("15X01", "15", "Sentence Transformers", "Sentence Transformers v6.2.0 示例（examples/）", "UKP Lab / Hugging Face", "6.2.0",
    PR + "sentence_transformers_6.2.0_examples_en.tar", git("UKPLab/sentence-transformers", "v6.2.0", ["examples"]), [8], "完整",
    "仓库 examples/（训练、检索、重排）", APL, type="practice", material="官方示例源码", expect={"min_docs": 10}, order=2)
add("15D02", "15", "FAISS", "FAISS Wiki（官方使用文档）", "Meta AI (FAIR)", "wiki 提交", OD + "faiss_wiki_en.tar",
    git("facebookresearch/faiss.wiki"), [1, 2, 4, 5], "完整", "GitHub wiki 全部页面（入门、索引选择、GPU、FAQ、调优）", MIT,
    expect={"min_docs": 30, "need_license": False}, order=3)
add("15X02", "15", "FAISS", "FAISS v1.15.1 教程与基准（tutorial/、benchs/）", "Meta AI (FAIR)", "1.15.1",
    PR + "faiss_1.15.1_tutorial_en.tar", git("facebookresearch/faiss", "v1.15.1", ["tutorial", "benchs", "INSTALL.md"]), [4, 8],
    "完整", "tutorial/（Python/C++）、benchs/、INSTALL.md", MIT, type="practice", material="官方示例源码",
    expect={"must_have": ["tutorial/python"]}, order=4)
add("15D03", "15", "LangChain", "LangChain / LangGraph 官方文档源（docs.langchain.com）", "LangChain Inc.", "main 提交（对应 langchain 1.4.x）",
    OD + "langchain_docs_main_src_en.tar", git("langchain-ai/docs", None, ["src/oss"]), [1, 2, 4, 5, 6], "部分",
    "src/oss（LangChain、LangGraph Python/JS 指南与集成页，MDX）；API 参考在 reference.langchain.com 单独生成，未含", MIT,
    expect={"min_docs": 200}, order=5)
add("15D04", "15", "LlamaIndex", "LlamaIndex v0.14.25 文档源（含示例笔记本）", "LlamaIndex Inc.", "0.14.25",
    OD + "llamaindex_0.14.25_docs_src_en.tar", git("run-llama/llama_index", "v0.14.25", ["docs/src", "docs/examples"]),
    [1, 2, 4, 6, 8], "部分", "docs/src（框架指南）+ docs/examples（笔记本）；api_reference 由 mkdocstrings 生成，未含", MIT,
    expect={"min_docs": 300}, order=6)

# ------------------------------------------------------------------ 09/10 app & UI
add("09D01", "09", "FastAPI", "FastAPI 0.162.0 文档（英文）与文档示例源码", "FastAPI（Sebastián Ramírez）", "0.162.0",
    OD + "fastapi_0.162.0_docs_src_en.tar", git("fastapi/fastapi", "0.162.0", ["docs/en", "docs_src"]), [1, 2, 3, 4, 5, 6, 8],
    "部分", "docs/en（教程、高级用户指南、部署）+ docs_src（全部示例代码）；docs/en/docs/reference 为 mkdocstrings 指令，正文未含",
    MIT, entry="docs/en/docs/index.md", expect={"min_docs": 150, "must_have": ["docs/en/docs/tutorial/", "docs/en/docs/deployment/"]},
    order=1)
add("10D01", "10", "Gradio", "Gradio 6.31.0 指南与演示源码", "Gradio（Hugging Face）", "6.31.0", OD + "gradio_6.31.0_guides_src_en.tar",
    git("gradio-app/gradio", "gradio@6.31.0", ["guides", "demo"]), [1, 2, 4, 6, 8], "部分",
    "guides/（全部指南 Markdown）+ demo/（演示源码）；组件 API 参考由 docstring 生成，未含", APL,
    expect={"min_docs": 80}, cross=["15"], order=30)
add("10D02", "10", "Streamlit", "Streamlit 官方文档源（含 API 参考 JSON）", "Snowflake / Streamlit", "main 提交（对应 1.66）",
    OD + "streamlit_docs_main_src_en.tar", git("streamlit/docs", None, ["content", "python"]), [1, 2, 3, 4, 5, 6], "完整",
    "content/（入门、概念、部署、知识库）+ python/streamlit.json（各版本 API 文档串）", APL,
    expect={"min_docs": 200}, cross=["15"], order=31)

# ------------------------------------------------------------------ 06 testing & tooling
add("06D01", "06", "pytest", "pytest 稳定版文档（Read the Docs HTML 包）", "pytest-dev", "stable（包内版本为准，对应 9.2）",
    OD + "pytest_stable_docs_html_en.zip", file("https://docs.pytest.org/_/downloads/en/stable/htmlzip/"), [1, 2, 3, 4, 5], "完整",
    "Read the Docs 官方 HTML 包（单页构建：全部章节合并于 index.html，含入门、how-to、fixture、插件、API 参考）", MIT, entry="index.html", expect={"min_docs": 1, "link_check": False},
    order=1)
add("06D02", "06", "mypy", "mypy 稳定版文档（Read the Docs HTML 包）", "mypy 项目", "stable（包内版本为准，对应 2.4）",
    OD + "mypy_stable_docs_html_en.zip", file("https://mypy.readthedocs.io/_/downloads/en/stable/htmlzip/"), [1, 2, 3, 5], "完整",
    "Read the Docs 官方 HTML 包（单页构建：全部章节合并于 index.html）", MIT, entry="index.html", expect={"min_docs": 1, "link_check": False}, order=2)
add("06D03", "06", "Pyright", "Pyright 1.1.414 文档（docs/）", "Microsoft", "1.1.414", OD + "pyright_1.1.414_docs_src_en.tar",
    git("microsoft/pyright", "1.1.414", ["docs"]), [1, 2, 3, 5], "完整", "仓库 docs/（配置、类型推断、类型概念）", MIT,
    expect={"min_docs": 20}, order=3)
add("06D04", "06", "Ruff", "Ruff 0.17.3 文档（docs/）", "Astral", "0.17.3", OD + "ruff_0.17.3_docs_src_en.tar",
    git("astral-sh/ruff", "0.17.3", ["docs"]), [1, 2, 5], "部分", "仓库 docs/（配置、linter、formatter、编辑器集成）；规则逐条页面由代码生成，未含",
    MIT, expect={"min_docs": 10}, order=4)
add("06D05", "06", "typing", "Python 类型系统规范与指南（typing.python.org 源）", "Python typing council", "main 提交",
    OD + "python_typing_docs_main_src_en.tar", git("python/typing", None, ["docs"]), [2, 3], "完整",
    "docs/spec（类型系统规范全文）+ docs/guides", "PSF-2.0", expect={"min_docs": 20}, order=5)

json.dump(S, open(OUT, "w"), ensure_ascii=False, indent=1)
print(len(S), "tool seeds ->", OUT)
