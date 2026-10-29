# 检索与决策日志（programming_reference_literature）

访问日期：2026-10-29（UTC）。本日志记录检索方法、版本核实方式、取舍依据，以及与"合法公开、完整下载"规则有关的决定。逐项结果见 `catalog_cn.csv` 与 `download_failures_cn.csv`。

## 1. 检索与核实方法

| 对象 | 方法 |
|---|---|
| 工具版本 | 对每个官方仓库执行 `git ls-remote --tags`，取最新稳定标签（排除 rc/alpha/beta/dev），并与官方下载页或文档站的版本目录交叉核对 |
| 官方构建文档 | 依次查找：官方离线包（Python、pandas、SciPy、Django、SQLAlchemy、SQLite、OpenCV release 附件）→ 官方构建 HTML 仓库（pytorch/docs、numpy/doc、scikit-learn.github.io、matplotlib.github.com、vision/audio/tutorials/triton 的 gh-pages）→ Hugging Face 官方构建包数据集 hf-doc-build → Read the Docs 官方 PDF/HTML 包 → 版本化文档源（标签下的 docs/）→ 离线镜像（wget，限定路径、遵守 robots） |
| 教材 | 作者、出版社或大学主页的合法开放全文；只在线开放的书籍做离线镜像并注明许可 |
| 课程 | 只收大学官方站点或官方仓库中实际可下载的讲义、课件、实验包。只有大纲、视频链接或 Google Docs 链接的课程不计入 |
| 论文 | arXiv 条目先用 arXiv API 元数据核对标题，56 条全部一致；经典论文取作者或机构公开版本 |
| 复用 | 先在同机已有文献库中查找同一文件，核验后复制（源库只读，不移动、不删除） |

## 2. 关键版本核实结果（2026-10-29）

- Python 3.15（docs.python.org 下载页只提供 3.15 归档；cpython 最新标签 v3.15.2）。
- NumPy 2.5、SciPy 1.18.0 文档（1.18.1 未单独发布文档）、pandas 文档压缩包（stable）、Matplotlib 3.11.2。
- scikit-learn 1.9（1.9.1 标签）、XGBoost 3.4.2、LightGBM 4.7.0、CatBoost 1.2.10。
- PyTorch 2.15（pytorch/docs 的 site 分支已有 2.15 目录）、torchvision 0.29、torchaudio 2.11.0、TensorFlow 2.21、Keras 3.15、JAX 0.12。
- OpenCV 5.0.0（release 附带完整文档包）。4.14.0 的 release 没有文档包附件。
- Transformers 5.22.0 是最新标签，但 hf-doc-build 中 v5.22.0.zip 只有译文、缺少 en 目录，因此文档取 v5.21.1 完整构建，示例取 v5.22.0。
- ONNX 1.23.2、ONNX Runtime 1.31.1（文档取 gh-pages 当前版）、TensorRT OSS v10.16、OpenVINO 2026.4.1。
- vLLM 0.32.0、llama.cpp b11985、Triton Inference Server 2.73.0、BentoML 1.4.40。
- CUDA 13.x 文档、cuda-samples v13.4、Triton 语言 v3.9.0（文档为 main 构建）、DeepSpeed 0.19.8。
- Sentence Transformers 6.2.0、FAISS 1.15.1、LangChain 1.4.7（文档仓库 main）、LlamaIndex 0.14.25。
- MLflow 3.17.2、DVC 3.67.x、W&B（文档仓库 main）、TensorBoard 2.21.0。
- FastAPI 0.162.0、Gradio 6.31.0、Streamlit 1.66（文档仓库 main）、Docker 与 Kubernetes 文档仓库 main。
- pytest 9.2、mypy 2.4、Pyright 1.1.414、Ruff 0.17.3、uv 0.13.6、pip 26.2.2。

## 3. 项目状态与易混淆项（执行时核实）

- Triton 编程语言（triton-lang/triton）与 NVIDIA Triton Inference Server（triton-inference-server/server）是两个无关项目，分别登记。
- Albumentations 原仓库在 2.0.8 后停止活跃开发，新版本以 AlbumentationsX（AGPL-3.0/商业双许可）发布，两者分别登记并注明。
- torchaudio 处于维护期，以文档内说明为准。
- docs.wandb.ai 已跳转到 CoreWeave 文档站，因此保存 wandb/docs 官方仓库。
- Evaluate 首页建议新项目改用 LightEval 等工具。
- ONNX Runtime 官方兼容性表只更新到 1.20。更新版本的 opset 支持需查对应 release 说明（已写入互操作指南）。
- vLLM 0.32 的 GGUF 支持已迁移到树外插件 vllm-gguf-plugin，且仍为实验性（见其 docs/features/quantization/gguf.md）。

## 4. 访问限制与未绕过的情况

- HAL（hal.science / inria.hal.science）对本脚本的请求返回"Making sure you're not a bot"验证页。未绕过，因此 Modern C（Gustedt）与 Scientific Visualization（Rougier）未获取。
- dsf.berkeley.edu 的 HTTPS 证书链不完整，HTTP 返回 404。未关闭证书校验，Architecture of a Database System 未获取。
- nlp.stanford.edu 在检索时段无法连接（No route to host），Introduction to Information Retrieval 待重试。
- Read the Docs 下载接口多次返回 429。脚本按 Retry-After 退避，并把 RTD 主机请求间隔拉长到 15 秒后重试。
- van Steen & Tanenbaum《Distributed Systems》第 4 版需填写邮箱领取个性化 PDF，属于表单获取，未收录。
- Szeliski、Bishop 2024 等需登录或表单的资料不在本库范围内。
- SourceForge 下载页给出直链。按页面给出的直链下载，属于正常用户流程。

## 5. 许可证取舍

- 源码仓库没有许可证文件的不保存（"许可证允许时保存源码"）。据此剔除：dbt-labs/jaffle-shop、remzi-arpacidusseau/ostep-projects、emichael/dslabs、langchain-ai/rag-from-scratch、iterative/example-get-started。
- 以课程正文为主、许可声明在课程站而非仓库内的（Helsinki Python MOOC），按站点声明保存并在备注注明。
- 构建产物仓库（gh-pages、numpy/doc 等）本身不含 LICENSE，许可证按所属项目登记。
- 多仓库课程作业逐仓库检查许可证：CMU DLSys hw0–hw4、Stanford CS149 asst1–3 均无许可证，整体未收录（已移出库目录）；Stanford CS336 的 assignment5-alignment 无许可证未收录，其余 5 个仓库保留，该课程标为部分资料。

## 6. 课程资料的取舍

- MIT OCW 课程使用官方"Download course"压缩包（静态站点，不含视频文件）。
- 课程站点上的课件、讲义 PDF 按页面链接逐个下载，并保留页面顺序文件 `_chapter_order_en.txt`。
- 只有部分材料可下载的课程标为"部分资料"，并写明范围。例如 Princeton COS 226 只有课件，CMU DLSys 的实现类讲次是 GitHub 笔记本。
- Stanford CS 329S 的讲义与课件全部是 Google Docs 链接，课程站没有可下载文件，因此不计入。

## 7. 规模控制

- 不下载视频、数据集、模型权重、依赖缓存或构建产物。源码包中单个文件超过 25 MB，或疑似权重/数据/二进制且超过 5 MB 的文件被剔除，剔除清单记录在各条目状态文件的 `dropped_large_files` 字段。
- TensorFlow API 镜像每页约 1.2 MB（内联导航）。含 tf.compat.v1 的全量约 8 GB，因此排除 tf.compat 命名空间。第一次镜像被另一通道的启动清理打断后重跑，wget 在 90 分钟超时处停止，共抓取 3903 页（原始 4.3 GB，gzip 后 265 MB）。因中断未做链接本地化，按部分资料登记。
