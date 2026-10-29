# 编程参考资料库（programming_reference_literature）最终报告

生成时间：由 `scripts/make_readme_en.py` 根据登记表自动生成。资料访问日期：2026-10-29（UTC）。

覆盖从编程基础到 AI 应用、性能优化与部署的 16 个类别，以及主流 AI 框架与工具的官方文档、教程、课程与示例。只计入完整下载并核验通过的资料。只保存了部分内容的资料单列为"部分资料"，不计入完整数。

## 1. 总体数量

- 已核验资料（全库去重后的独立条目）：**376** 项，其中完整 **348** 项，部分资料 **28** 项。
- 新下载 **371** 项；已有库复用（核验后复制，未移动原库）**5** 项。
- 未获取（失败或待重试）：**7** 项，见 `download_failures_cn.csv`。
- 总体积约 12.8 GB。
- 工具层面：登记 62 个工具/项目，`tools/tools_catalog_cn.csv` 共 126 行（含子模块关联行）。

按资料类型（完整 / 含部分资料合计）：

| 类型 | 完整 | 合计（含部分资料） |
|---|---|---|
| 教材/参考书 | 66 | 66 |
| 大学课程资料 | 37 | 43 |
| 官方文档/系统教程 | 102 | 122 |
| 实验/习题/参考项目 | 67 | 69 |
| 论文/综述 | 76 | 76 |

## 2. 各类别数量与目标

目标：教材 3–5、大学课程 2–4、官方文档 2–5、实践项目 2–5；论文只对 02/11/13/14/15 设 10–20 篇。官方文档按"项目+版本"计数，同一项目的多个部分（如 Docker 文档 + Dockerfile 参考）按条目分别登记。工具文档、示例与课程分别统计，不冲抵教材或论文数量。

| 类别 | 教材 | 课程 | 官方文档 | 实践项目 | 论文 | 未达标项 |
|---|---|---|---|---|---|---|
| 01 Python 编程 | 6 | 3 | 3（+1 部分） | 2 | — | 达标 |
| 02 数据结构与算法 | 5 | 2（+1 部分） | 不适用 | 2 | 13 | 达标 |
| 03 科学计算与数据处理 | 4 | 2 | 7（+1 部分） | 4 | — | 达标 |
| 04 机器学习编程 | 4 | 3 | 7（+1 部分） | 8 | — | 达标 |
| 05 深度学习编程 | 4 | 4（+2 部分） | 20（+2 部分） | 11（+1 部分） | — | 达标 |
| 06 软件工程与测试 | 5 | 2 | 5（+1 部分） | 3 | — | 达标 |
| 07 Linux、Shell 与 Git | 4 | 2 | 4 | 3 | — | 达标 |
| 08 数据库与数据工程 | 4 | 2 | 4 | 2 | — | 达标 |
| 09 后端与 API 开发 | 3 | 2 | 5（+3 部分） | 2 | — | 达标 |
| 10 前端与交互界面 | 3 | 2 | 5（+2 部分） | 2 | — | 达标 |
| 11 计算机系统与网络 | 5 | 2 | 2 | 2（+1 部分） | 10 | 达标 |
| 12 C/C++ 与性能优化 | 5 | 2 | 7 | 2 | — | 达标 |
| 13 GPU 与并行计算 | 4 | 2 | 7（+1 部分） | 5 | 19 | 达标 |
| 14 分布式系统与部署 | 4 | 1（+2 部分） | 14（+3 部分） | 10 | 15 | 大学课程资料缺 1 |
| 15 AI 应用与智能体开发 | 2 | 3（+1 部分） | 5（+4 部分） | 7 | 19 | 教材缺 1 |
| 16 安全编程 | 4 | 3 | 7（+1 部分） | 2 | — | 达标 |

注："大学课程资料"包含少量非大学官方课程（Hugging Face 官方课程、Inria scikit-learn MOOC），其资料形态列已标注。02 类算法没有"官方文档"，不适用。

## 3. 版本与年份分布

版本固定方式：

- 分支提交快照（记录提交号与日期）：130 项
- 官方发布文件（PDF/压缩包，版本见文件）：77 项
- 论文定版（arXiv 版本号/会议版）：76 项
- 站点当前版本离线镜像（记录访问日期）：42 项
- 固定发布标签（tag）：35 项
- 官方构建包（版本号）：11 项
- 已有库复用（原版本）：5 项

资料年份（教材为版次年份，文档/源码为版本或快照年份，论文为首次公开年份）：

| 年份 | 数量 |
|---|---|
| 2022 年及以前 | 91 |
| 2023 | 31 |
| 2024 | 42 |
| 2025 | 55 |
| 2026 | 54 |

论文 76 篇：近三年（2023-10-29 之后首次公开）23 篇，经典/较早 53 篇（单列标注）。

## 4. 从基础到应用与部署的覆盖

| 阶段 | 学习路线 | 覆盖情况 |
|---|---|---|
| 编程基础 | `guides/beginner_path_cn.md` | Python、算法、Linux/Shell、Git、测试：教材、课程、官方文档、练习齐全 |
| AI 编程 | `guides/ai_programming_path_cn.md` | NumPy/SciPy/pandas/Matplotlib/Jupyter → scikit-learn 与梯度提升 → PyTorch/TF/Keras/JAX → HF 生态 → 实验与数据管理 |
| 应用开发 | `guides/application_path_cn.md` | HTTP、数据库、Django/FastAPI/Flask、前端（MDN/React/TS）、RAG、工具调用与代码智能体 |
| 系统与性能 | `guides/systems_performance_path_cn.md` | C、机器级程序、链接与构建、OS 与并发、网络、CPU 性能、CUDA/Triton、训练系统优化 |
| 部署 | `guides/deployment_path_cn.md` | Docker、CI/CD、Kubernetes、Prometheus/OpenTelemetry、SRE、分布式基础、模型服务 |
| 实践 | `guides/practice_projects_cn.md` | 按难度分三级的项目与评价方式 |
| 核心入口 | `guides/core_reading_list_cn.md` | 每类优先教材/课程/官方参考 |
| 工具 | `tools/tools_learning_map_cn.md`、`tools/interoperability_guide_cn.md` | 工具用途与顺序；训练→导出→ONNX→推理部署的兼容条件 |

### 4.1 重点工具资料链完整度

| 工具 | 资料编号 | 完整性 | 覆盖方面（并集） |
|---|---|---|---|
| PyTorch | 05C01、05C02、05C03、05C04、05D01、05D02、05X01、15C03 | 完整、部分 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码；课程；调试/性能/FAQ |
| TensorFlow | 05C04、05D05、05D06 | 完整、部分 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码；课程；调试/性能/FAQ |
| Keras | 05D07、05D08 | 完整 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码；调试/性能/FAQ |
| OpenCV | 05D10、05X02 | 完整 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码 |
| Transformers | 05C50、05D20、05D29、05X10、05X11 | 完整 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码；课程；调试/性能/FAQ |
| ONNX | 14D01、14D02、14X01 | 完整 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码 |
| ONNX Runtime | 14D03、14X02 | 完整 | API 参考；保存/导出/部署/互操作；入门安装；教程/工作流；用户指南/概念；示例源码；调试/性能/FAQ |

## 5. 缺失、失败、残缺与待核实

### 5.1 未获取（失败/待重试）

| 编号 | 标题 | 原因（摘要） |
|---|---|---|
| 03B04 | Scientific Visualization: Python + Matplotlib | https://inria.hal.science/hal-03427242/document: 不是 PDF 文件头 / https://hal.science/hal-03427242/document: 不是 PDF 文件头 |
| 04C03 | Stanford CS 329S Machine Learning Systems Design (Winter 2022) 讲义 | 课程讲义与课件全部为 Google Docs/Slides 链接，课程站无可下载文件；按规则（视频/外链不算已下载课程）不计入 |
| 05X21 | CMU DLSys needle 作业框架（hw0–hw4 公开模板） | 各作业仓库均无许可证文件；按"许可证允许时保存源码"规则未收录（已移出库目录） |
| 08B02 | Architecture of a Database System | http://dsf.berkeley.edu/papers/fntdb07-architecture.pdf: 404 HTTP 404 / https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf: 0 URLError: <urlopen error [SS |
| 12B01 | Modern C | https://inria.hal.science/hal-02383654/document: 不是 PDF 文件头 |
| 13X10 | Stanford CS149 编程作业（asst1–asst4 公开仓库） | 各作业仓库均无许可证文件；按"许可证允许时保存源码"规则未收录（已移出库目录） |
| 15B01 | Introduction to Information Retrieval | https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf: 0 URLError: <urlopen error [Errno 113] No route to host> |

### 5.2 部分资料（已核验，但只保存了说明中的范围）

| 编号 | 标题 | 范围说明 |
|---|---|---|
| 01D04 | uv 文档（Python 包与项目管理器） | 仓库 docs/（MkDocs Markdown：入门、概念、指南、参考）；CLI/设置参考页由代码生成，未含 |
| 02C03 | Princeton COS 226 Algorithms and Data Structures (Spring 2025) 课件 | 仅课件 PDF；作业规格在课程站另行发布，未下载 |
| 03D05 | JupyterLab 4.6 官方文档 | 仓库 docs/source（用户指南/扩展开发，Sphinx 源；扩展 API 的 TypeDoc 参考需构建，未含） |
| 04D05 | MLflow 3.17.2 文档源（Docusaurus） | docs/docs（经典 ML 与 GenAI 指南、部署、模型格式）+ docs/api_reference/source（Sphinx 源；API 正文由 docstring 生成，未含） |
| 05C02 | CMU 10-414/714 Deep Learning Systems: Algorithms and Implementation 课件与作业 | 课程站全部课件 PDF；实现类讲次以 GitHub 笔记本发布（lecture5/8/13 等仓库），未下载 |
| 05C04 | MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本） | 仅实验仓库（labs）；讲座课件与视频未下载 |
| 05D06 | TensorFlow Python API 参考（tensorflow.org/api_docs/python 离线镜像） | tensorflow.org/api_docs/python 下 tf.* API 页的部分镜像：排除 tf.compat；wget 在 90 分钟超时处停止，已抓取约 3900 页（含 tf.raw_ops、tf.keras、tf.math/nn/data/distribute 等），其余页面缺失；因中断未做链接本地化（页面可离线阅读，页间链接仍指向 tensorflow.org）；不含图片；g |
| 05D12 | Albumentations 2.0.8 文档源与 README（原项目，已转维护） | 仓库 README 与 docs/（变换列表与贡献说明；albumentations.ai 在线文档已转向 AlbumentationsX，未整站保存） |
| 05D13 | AlbumentationsX 2.5.1 源码仓库（含 README 与示例） | 完整源码仓库（README、docs、benchmark；在线文档未整站保存） |
| 06D04 | Ruff 0.17.3 文档（docs/） | 仓库 docs/（配置、linter、formatter、编辑器集成）；规则逐条页面由代码生成，未含 |
| 09D01 | FastAPI 0.162.0 文档（英文）与文档示例源码 | docs/en（教程、高级用户指南、部署）+ docs_src（全部示例代码）；docs/en/docs/reference 为 mkdocstrings 指令，正文未含 |
| 09D02 | Flask 文档源与官方教程示例（pallets/flask） | docs/（Sphinx 源；API 页正文由 docstring 生成，未含）+ examples/ |
| 09D05 | Celery 文档源（异步任务队列） | docs/（Sphinx 源；API 参考由 docstring 生成，未含）+ examples/ |
| 10D01 | Gradio 6.31.0 指南与演示源码 | guides/（全部指南 Markdown）+ demo/（演示源码）；组件 API 参考由 docstring 生成，未含 |
| 10D51 | MDN Web Docs 内容源（HTML、CSS、JavaScript、HTTP、可访问性、Learn） | 仅 HTML/CSS/JS/HTTP/可访问性/Learn 六个子树（Web API 子树体量过大未收） |
| 11X04 | Nand2Tetris 软件与项目包 | 项目说明 PDF；官方 IDE 软件包未下载（属工具构建产物） |
| 13D04 | DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源） | docs/_tutorials、_pages（ZeRO、配置 JSON、推理）+ docs/code-docs（Sphinx 源；API 正文由 docstring 生成，未含） |
| 14C01 | MIT 6.5840 Distributed Systems (Spring 2026) 讲义与实验 | 课程日程页两层链接内的讲义、论文与实验说明；日程以外页面引用的旧学期论文未下载（链接抽样断链约 40%） |
| 14C03 | Princeton COS 418 Distributed Systems (Fall 2025) 课件与习题课讲义 | 日程页链接的全部 PDF；其中课程站自身失效（404）的链接见 state/items/14C03.json 的 missing_upstream_404 |
| 14D05 | OpenVINO 2026.4.1 文档源（articles_en） | docs/articles_en（RST 源：安装、模型转换、推理、优化）；Python/C++ API 参考由构建生成，未含 |
| 14D06 | vLLM v0.32.0 文档源与示例 | docs/（入门、部署、服务、配置、设计）+ examples/；API 参考页由 mkdocstrings 生成，未含 |
| 14D10 | Docker 官方文档源（docker/docs content） | Engine、Build、Compose、入门与指南、Compose 文件参考；Dockerfile/CLI 参考在构建时自 buildkit 与 docker/cli 引入，另见 14D12/14D13 |
| 15C03 | Stanford CS336 Language Modeling from Scratch (Spring 2025) 讲义与作业 | 讲义仓库 + assignment1–4；assignment5-alignment 仓库无许可证文件未收录 |
| 15D03 | LangChain / LangGraph 官方文档源（docs.langchain.com） | src/oss（LangChain、LangGraph Python/JS 指南与集成页，MDX）；API 参考在 reference.langchain.com 单独生成，未含 |
| 15D04 | LlamaIndex v0.14.25 文档源（含示例笔记本） | docs/src（框架指南）+ docs/examples（笔记本）；api_reference 由 mkdocstrings 生成，未含 |
| 15D13 | DSPy 文档源 | docs/ Markdown 源；API 页由 mkdocstrings 生成，未含 |
| 15D14 | OpenAI Agents SDK（Python）文档源与示例 | docs/（ref/ 为 mkdocstrings 指令，API 正文未含）+ examples/ |
| 16D08 | Bandit 文档源（Python 安全静态分析） | doc/source（Sphinx 源；插件 API 由 docstring 生成部分未含） |

### 5.3 结构性缺口

- 见第 2 节"未达标项"列，以及 `tools/tools_learning_map_cn.md` 末尾的工具层面缺口说明。
- 以下资料因访问限制未获取，也未绕过：HAL 机器人验证（Modern C、Rougier 可视化）、Berkeley 证书错误（Architecture of a Database System）、需填邮箱领取的 van Steen《Distributed Systems》。详见 `search_log_cn.md` 第 4 节。
- 无许可证文件的源码仓库不保存（见 `search_log_cn.md` 第 5 节）。

## 6. 目录与登记表

```
programming_reference_literature/
├── README_cn.md                 本报告
├── catalog_cn.csv               全部已核验资料（编号、类别、类型、版本、许可证、本地路径、完整性、提交号…）
├── progress_cn.csv              各类别 × 类型的完成数与目标
├── download_failures_cn.csv     失败与待重试条目
├── search_log_cn.md             检索方法、版本核实与取舍决定
├── books/  courses/  official_docs/  practice/  papers/
├── guides/                      7 份中文学习路线与索引
├── tools/                       tools_catalog_cn.csv、tools_learning_map_cn.md、interoperability_guide_cn.md
├── scripts/                     种子清单、下载核验、登记与报告脚本（*_en.py）
└── state/                       每个条目的核验状态（state/items/<编号>.json）与日志
```

命名：自建文件在扩展名前加语言后缀（`_en`/`_cn`）。完整上游项目与文档包保持内部原始结构，外层归档加后缀（如 `pytorch_2.15_docs_html_en.tar`）。tar 包内保留上游路径，入口文件见 `tools/tools_catalog_cn.csv` 的"入口文件"列。

## 7. 续跑命令

```bash
cd /root/programming_reference_literature
# 1) 重新生成种子（修改 scripts/seed_*_en.py 后）
python3 -I scripts/seed_tools_en.py && python3 -I scripts/seed_core_en.py && python3 -I scripts/seed_papers_en.py
# 2) 下载与核验（已完成条目自动跳过；--retry-failed 重试失败项；各 --kind 通道可并行，同一条目有锁）
python3 -I scripts/fetch_en.py run --kind pdf,pdfset,file,hfdoc,reuse,git,multi_git --retry-failed
python3 -I scripts/fetch_en.py run --kind mirror --retry-failed
python3 -I scripts/fetch_en.py status            # 汇总与失败原因
# 3) 生成登记表、指南与报告
python3 -I scripts/build_catalog_en.py && python3 -I scripts/link_guides_en.py && python3 -I scripts/make_readme_en.py
```

## 8. 本轮边界

- 只收集整理：未执行任何来源代码，未安装项目依赖，未部署，未上传 GitHub，未删除本地资料。
- 未下载视频、数据集、模型权重、依赖缓存或构建产物。源码包中的大文件按规则剔除并记录在 `state/items/<编号>.json`。
- 按要求未安排整库哈希扫描或上传后回验。单个文件的 SHA256 只在下载时顺带记录在状态文件中。
