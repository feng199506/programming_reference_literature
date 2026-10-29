# AI 框架与工具学习地图：用途、先修知识与推荐顺序

版本以 2026-10-29 从官方仓库标签、发布页或文档站核实的结果为准，逐项见 `tools_catalog_cn.csv`。
"8 个方面"指：① 入门安装 ② 用户指南/核心概念 ③ API 参考 ④ 官方教程/工作流 ⑤ 调试/性能/FAQ ⑥ 保存/导出/部署/互操作 ⑦ 课程 ⑧ 示例源码。
资料标"〔部分资料〕"时，缺失部分（通常是由 docstring 生成的 API 页）在 `tools_catalog_cn.csv` 的"下载范围"列写明。

**同名项目注意**：

- **Triton 编程语言**（triton-lang，GPU 内核 DSL）与 **NVIDIA Triton Inference Server**（推理服务器，2025 年起品牌为 Dynamo Triton）是两个无关项目。
- **Keras 3** 是多后端框架（JAX/PyTorch/TensorFlow），与 TF 2.15 及以前内置的 tf.keras（Keras 2）的保存格式和 API 有差异。
- **Albumentations** 原仓库已停止活跃开发，后续以 **AlbumentationsX** 发布，许可变为 AGPL-3.0/商业双许可。
- **torchaudio** 已进入维护期，解码等功能迁往 TorchCodec。
- **Weights & Biases** 已归入 CoreWeave，在线文档域名已跳转。
- **Evaluate** 官方建议新项目改用 LightEval 等工具。

---

## 1. 科学计算与数据处理

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| NumPy 2.5 | N 维数组、向量化、线性代数基础 | Python 基础 | 〔03D01〕、〔03X01〕 | 1 |
| pandas | 表格数据清洗、分组、时间序列、I/O | NumPy | 〔03D03〕、〔03B02〕 | 2 |
| Matplotlib 3.11 | 绘图与出版级图表 | NumPy | 〔03D04〕、〔03B04〕 | 3 |
| SciPy 1.18 | 优化、积分、稀疏、信号、统计 | NumPy、数值方法 | 〔03D02〕 | 4 |
| Jupyter | 交互式笔记本与 JupyterLab | Python | 〔03D06〕、〔03D05〕 | 与 1 并行 |

## 2. 传统机器学习

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| scikit-learn 1.9 | 预处理、Pipeline、模型选择、评估 | NumPy、pandas、统计 | 〔04D01〕、〔04X01〕、〔04C04〕 | 1（必须先学） |
| XGBoost | 梯度提升树（GPU、分布式、JSON/UBJ 模型格式） | scikit-learn | 〔04D02〕、〔04X02〕 | 2 |
| LightGBM 4.7 | 直方图梯度提升、类别特征 | scikit-learn | 〔04D03〕、〔04X03〕 | 2 |
| CatBoost 1.2.10 | 有序目标统计处理类别特征 | scikit-learn | 〔04D04〕、〔04X04〕 | 2 |

## 3. 深度学习框架

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| PyTorch 2.15 | 张量、autograd、nn、训练、compile、导出 | NumPy、DL 基础 | 〔05D02〕（教程先学）→〔05D01〕→〔05X01〕；课程〔05C01〕〔05C03〕〔05C04〕 | 1（主框架） |
| TensorFlow（2.21） | 图执行、tf.data、SavedModel、分布式策略 | NumPy、DL 基础 | 〔05D05〕、〔05D06〕；课程〔05C04〕 | 选学 |
| Keras 3（3.15） | 多后端高层 API、.keras 格式、model.export | Python、DL 基础 | 〔05D07〕、〔05D08〕 | 选学（入门快） |
| JAX | 函数变换（grad/jit/vmap）、分片并行、导出 | NumPy、函数式思维 | 〔05D09〕；课程〔05C03〕 | 选学（研究/TPU） |

## 4. PyTorch 生态

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| torchvision 0.29 | 视觉数据集接口、transforms v2、预训练模型接口 | 〔05D03〕 | PyTorch 之后 |
| torchaudio 2.11 | 音频 I/O 与变换（维护期） | 〔05D04〕 | 按需 |
| torch.distributed / FSDP2 / torchrun | 多卡与多机训练 | 〔05D01〕 distributed*.html、fsdp；〔05D02〕；〔05X01〕 distributed/ | 单卡熟练后 |
| torch.export / torch.onnx | 图捕获、ONNX 导出（2.15 默认 dynamo=True） | 〔05D01〕 export*.html、onnx*.html | 部署前 |
| torch.profiler / torch.compile | 性能剖析与编译优化 | 〔05D01〕、〔05D02〕、〔04D08〕 | 训练变慢时 |

## 5. 计算机视觉

| 工具 | 用途 | 先修 | 资料 |
|---|---|---|---|
| OpenCV 5.0.0 | 图像处理、几何、视频、DNN 推理（可加载 ONNX） | NumPy | 〔05D10〕（含 Python 教程）、〔05X02〕 |
| Pillow | 图像读写与基础处理 | Python | 〔05D11〕 |
| Albumentations / AlbumentationsX | 数据增强流水线 | NumPy、PyTorch Dataset | 〔05D12〕〔部分资料〕、〔05D13〕〔部分资料〕 |

推荐顺序：Pillow（读写）→ OpenCV 核心模块与 Python 教程 → torchvision transforms v2 → Albumentations（复杂增强）→ OpenCV DNN 推理与 ONNX 互操作。

## 6. Hugging Face 生态

推荐顺序：先学〔05C50〕LLM 课程，再按下列顺序查阅文档。

| 顺序 | 工具 | 用途 | 资料 |
|---|---|---|---|
| 1 | Hub 客户端（huggingface_hub） | 下载/上传模型与数据、缓存、推理客户端 | 〔05D28〕 |
| 2 | Transformers | 预训练模型加载、Pipeline、Trainer、生成、导出 | 〔05D20〕、〔05X10〕、〔05X11〕 |
| 3 | Tokenizers | 快速分词器训练与使用 | 〔05D22〕 |
| 4 | Datasets | 数据加载、映射、流式、Arrow 缓存 | 〔05D21〕 |
| 5 | Evaluate | 指标计算（维护说明见首页） | 〔05D27〕 |
| 6 | Accelerate | 同一脚本跑单卡/多卡/FSDP/DeepSpeed | 〔05D23〕、〔05X15〕 |
| 7 | PEFT | LoRA 等参数高效微调、适配器合并 | 〔05D24〕、〔05X13〕 |
| 8 | TRL | SFT、DPO、GRPO 等后训练 | 〔05D25〕、〔05X14〕 |
| 9 | Diffusers | 扩散模型推理与训练 | 〔05D26〕、〔05X12〕；课程〔05C51〕 |

## 7. 模型交换与推理

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| ONNX | 跨框架模型格式（IR + 版本化算子集） | 任一训练框架 | 〔14D01〕、〔14D02〕、〔14X01〕 | 1 |
| ONNX Runtime | 跨平台推理引擎，可插拔执行提供程序 | ONNX | 〔14D03〕、〔14X02〕 | 2 |
| TensorRT | NVIDIA GPU 推理优化编译器 | ONNX、CUDA 概念 | 〔14D04〕、〔14X03〕 | 3（NVIDIA 环境） |
| OpenVINO | Intel CPU/GPU/NPU 推理 | ONNX 或 PyTorch | 〔14D05〕〔部分资料〕、〔14X04〕 | 3（Intel 环境） |

## 8. 大模型推理与部署

| 工具 | 用途 | 资料 | 选择建议 |
|---|---|---|---|
| vLLM | GPU 上高吞吐 LLM 服务（PagedAttention、OpenAI 兼容 API） | 〔14D06〕〔部分资料〕；论文〔14P01〕 | GPU 服务首选 |
| llama.cpp | C/C++ 本地推理、GGUF 量化、llama-server | 〔14D07〕 | CPU/边缘/本地 |
| Triton Inference Server | 多框架模型服务、动态批处理、模型仓库 | 〔14D08〕、〔14X05〕 | 多模型、多后端统一服务 |
| BentoML | Python 服务定义、打包与部署 | 〔14D09〕、〔14X06〕 | 业务逻辑与模型一起打包 |

## 9. GPU 编程与训练优化

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| CUDA | GPU 编程模型与工具链 | C/C++、体系结构 | 〔13D01〕、〔13D02〕、〔13X01〕；课程〔13C01〕〔13C02〕 | 1 |
| Triton 编程语言 | 用 Python 写分块 GPU 内核 | PyTorch、CUDA 概念 | 〔13D03〕、〔13X02〕 | 2 |
| NCCL | GPU 集合通信 | 分布式训练概念 | 〔13D06〕 | 3 |
| DeepSpeed | ZeRO、混合精度、流水并行 | PyTorch 分布式 | 〔13D04〕〔部分资料〕、〔13D05〕、〔13X03〕 | 3 |
| 分布式训练官方工具（汇总） | torch.distributed / Accelerate / DeepSpeed / NCCL | 见上 | 〔05D01〕、〔05D23〕、〔13D04〕、〔13D06〕 | — |

## 10. 检索与 AI 应用

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| Sentence Transformers | 嵌入与重排模型的使用与训练 | 〔15D01〕、〔15X01〕 | 1 |
| FAISS | 向量索引与相似度检索 | 〔15D02〕、〔15X02〕 | 2 |
| LlamaIndex | 面向 RAG 的数据接入、索引与查询引擎 | 〔15D04〕〔部分资料〕 | 3（二选一或都学） |
| LangChain / LangGraph | LLM 应用链、智能体与有状态图编排 | 〔15D03〕〔部分资料〕 | 3 |

## 11. 实验与数据管理

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| TensorBoard | 训练曲线、超参、剖析可视化 | 〔04D08〕 | 1 |
| MLflow | 实验追踪、模型注册、模型格式与服务 | 〔04D05〕〔部分资料〕、〔04X05〕 | 2 |
| DVC | 数据与管线版本控制 | 〔04D06〕 | 2 |
| Weights & Biases | 托管实验追踪、扫参、制品 | 〔04D07〕、〔04X07〕 | 选学 |

## 12. 应用与部署基础

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| FastAPI | 类型驱动的异步 Web API | 〔09D01〕〔部分资料〕、〔09X02〕 | 1 |
| Gradio | 模型演示界面 | 〔10D01〕〔部分资料〕 | 2 |
| Streamlit | 数据应用与内部工具 | 〔10D02〕 | 2 |
| Docker | 容器镜像与 Compose | 〔14D10〕〔部分资料〕、〔14D12〕、〔14D13〕、〔14X07〕 | 3 |
| Kubernetes | 容器编排 | 〔14D11〕、〔14X08〕 | 4 |

## 13. 测试与工程工具

| 工具 | 用途 | 资料 |
|---|---|---|
| pytest | 单元/集成测试、fixture、插件 | 〔06D01〕 |
| mypy / Pyright | 静态类型检查 | 〔06D02〕、〔06D03〕；规范〔06D05〕 |
| Ruff | lint 与格式化 | 〔06D04〕〔部分资料〕 |
| pip / uv / 打包指南 | 依赖安装、环境与项目管理、打包发布 | 〔01D02〕、〔01D04〕〔部分资料〕、〔01D03〕、〔01D01〕（venv） |

---

## 资料缺口（工具层面）

- 公开可下载的**大学课程**主要覆盖 PyTorch、TensorFlow、JAX 与 CUDA。OpenCV、ONNX、TensorRT、OpenVINO、vLLM、MLflow、DVC 等没有找到可完整下载的大学课程，只能依靠官方教程与示例。
- 部分工具官方只提供由 docstring 生成的在线 API 页、没有离线包（FastAPI、LangChain、LlamaIndex、vLLM、Gradio、OpenVINO、Ruff、uv、MLflow 等）。本库保存版本化文档源，标为部分资料。
- 具体失败与待补项见 `../download_failures_cn.csv`。
