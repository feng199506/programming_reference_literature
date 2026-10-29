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
| NumPy 2.5 | N 维数组、向量化、线性代数基础 | Python 基础 | 03D01《NumPy 2.5 官方文档（用户指南、API 参考、构建与 C API）》 → `../official_docs/numpy_2.5_docs_html_en.tar`、03X01《NumPy 官方教程笔记本（numpy-tutorials）》 → `../practice/numpy_tutorials_main_en.tar` | 1 |
| pandas | 表格数据清洗、分组、时间序列、I/O | NumPy | 03D03《pandas 官方文档（HTML 压缩包）》 → `../official_docs/pandas_stable_docs_html_en.zip`、03B02《Python for Data Analysis (3rd ed., Open Access 网页版)》 → `../books/McKinney_PythonForDataAnalysis_3rdEd_html_en.tar` | 2 |
| Matplotlib 3.11 | 绘图与出版级图表 | NumPy | 03D04《Matplotlib 3.11.2 官方文档（教程、用户指南、示例图库、API）》 → `../official_docs/matplotlib_3.11.2_docs_html_en.tar`、03B04《Scientific Visualization: Python + Matplotlib》（未获取，见 download_failures_cn.csv） | 3 |
| SciPy 1.18 | 优化、积分、稀疏、信号、统计 | NumPy、数值方法 | 03D02《SciPy 1.18 官方文档》 → `../official_docs/scipy_1.18.0_docs_html_en.zip` | 4 |
| Jupyter | 交互式笔记本与 JupyterLab | Python | 03D06《Project Jupyter 总体文档（docs.jupyter.org）》 → `../official_docs/jupyter_docs_main_src_en.tar`、03D05《JupyterLab 4.6 官方文档》〔部分资料〕 → `../official_docs/jupyterlab_4.6.5_docs_src_en.tar` | 与 1 并行 |

## 2. 传统机器学习

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| scikit-learn 1.9 | 预处理、Pipeline、模型选择、评估 | NumPy、pandas、统计 | 04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar`、04X01《scikit-learn 1.9.1 示例源码（examples/）》 → `../practice/scikit-learn_1.9.1_examples_en.tar`、04C04《Inria scikit-learn MOOC: Machine learning in Python with scikit-learn》 → `../courses/Inria_scikit-learn_MOOC_src_en.tar` | 1（必须先学） |
| XGBoost | 梯度提升树（GPU、分布式、JSON/UBJ 模型格式） | scikit-learn | 04D02《XGBoost 稳定版文档（PDF）》 → `../official_docs/xgboost_stable_docs_en.pdf`、04X02《XGBoost 3.4.2 示例与演示（demo/）》 → `../practice/xgboost_3.4.2_demo_en.tar` | 2 |
| LightGBM 4.7 | 直方图梯度提升、类别特征 | scikit-learn | 04D03《LightGBM 稳定版文档（PDF）》 → `../official_docs/lightgbm_stable_docs_en.pdf`、04X03《LightGBM 4.7.0 示例（examples/）》 → `../practice/lightgbm_4.7.0_examples_en.tar` | 2 |
| CatBoost 1.2.10 | 有序目标统计处理类别特征 | scikit-learn | 04D04《CatBoost 1.2.10 官方文档源（英文）》 → `../official_docs/catboost_1.2.10_docs_src_en.tar`、04X04《CatBoost 官方教程（catboost/tutorials）》 → `../practice/catboost_tutorials_master_en.tar` | 2 |

## 3. 深度学习框架

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| PyTorch 2.15 | 张量、autograd、nn、训练、compile、导出 | NumPy、DL 基础 | 05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`（教程先学）→05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`→05X01《PyTorch 官方示例（pytorch/examples）》 → `../practice/pytorch_examples_main_en.tar`；课程05C01《Stanford CS231n Deep Learning for Computer Vision 课程讲义》 → `../courses/Stanford_CS231n_Online_LectureNotes_en`05C03《University of Amsterdam Deep Learning Course 教程笔记本（UvA DL Notebooks）》 → `../courses/UvA_DL_Notebooks_src_en.tar`05C04《MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本）》〔部分资料〕 → `../courses/MIT_6S191_Labs_src_en.tar` | 1（主框架） |
| TensorFlow（2.21） | 图执行、tf.data、SavedModel、分布式策略 | NumPy、DL 基础 | 05D05《TensorFlow 官方指南与教程源（tensorflow/docs site/en）》 → `../official_docs/tensorflow_docs_guides_master_src_en.tar`、05D06《TensorFlow Python API 参考（tensorflow.org/api_docs/python 离线镜像）》〔部分资料〕 → `../official_docs/tensorflow_api_docs_python_mirror_en.tar.gz`；课程05C04《MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本）》〔部分资料〕 → `../courses/MIT_6S191_Labs_src_en.tar` | 选学 |
| Keras 3（3.15） | 多后端高层 API、.keras 格式、model.export | Python、DL 基础 | 05D07《Keras 3 官方指南与示例源（keras-io）》 → `../official_docs/keras_io_master_src_en.tar`、05D08《Keras 3 API 参考（keras.io/api 离线镜像）》 → `../official_docs/keras_api_reference_mirror_en.tar` | 选学（入门快） |
| JAX | 函数变换（grad/jit/vmap）、分片并行、导出 | NumPy、函数式思维 | 05D09《JAX 官方文档（Read the Docs HTML 包）》 → `../official_docs/jax_latest_docs_html_en.zip`；课程05C03《University of Amsterdam Deep Learning Course 教程笔记本（UvA DL Notebooks）》 → `../courses/UvA_DL_Notebooks_src_en.tar` | 选学（研究/TPU） |

## 4. PyTorch 生态

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| torchvision 0.29 | 视觉数据集接口、transforms v2、预训练模型接口 | 05D03《torchvision 0.29 官方文档》 → `../official_docs/torchvision_0.29_docs_html_en.tar` | PyTorch 之后 |
| torchaudio 2.11 | 音频 I/O 与变换（维护期） | 05D04《torchaudio 2.11 官方文档》 → `../official_docs/torchaudio_2.11_docs_html_en.tar` | 按需 |
| torch.distributed / FSDP2 / torchrun | 多卡与多机训练 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar` distributed*.html、fsdp；05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`；05X01《PyTorch 官方示例（pytorch/examples）》 → `../practice/pytorch_examples_main_en.tar` distributed/ | 单卡熟练后 |
| torch.export / torch.onnx | 图捕获、ONNX 导出（2.15 默认 dynamo=True） | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar` export*.html、onnx*.html | 部署前 |
| torch.profiler / torch.compile | 性能剖析与编译优化 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`、05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`、04D08《TensorBoard 2.21.0 官方指南（docs/）》 → `../official_docs/tensorboard_2.21.0_docs_src_en.tar` | 训练变慢时 |

## 5. 计算机视觉

| 工具 | 用途 | 先修 | 资料 |
|---|---|---|---|
| OpenCV 5.0.0 | 图像处理、几何、视频、DNN 推理（可加载 ONNX） | NumPy | 05D10《OpenCV 5.0.0 官方文档（Doxygen HTML 包，含 Python 教程）》 → `../official_docs/opencv_5.0.0_docs_html_en.zip`（含 Python 教程）、05X02《OpenCV 5.0.0 示例（samples/）》 → `../practice/opencv_5.0.0_samples_en.tar` |
| Pillow | 图像读写与基础处理 | Python | 05D11《Pillow 稳定版文档（PDF）》 → `../official_docs/pillow_stable_docs_en.pdf` |
| Albumentations / AlbumentationsX | 数据增强流水线 | NumPy、PyTorch Dataset | 05D12《Albumentations 2.0.8 文档源与 README（原项目，已转维护）》〔部分资料〕 → `../official_docs/albumentations_2.0.8_docs_src_en.tar`〔部分资料〕、05D13《AlbumentationsX 2.5.1 源码仓库（含 README 与示例）》〔部分资料〕 → `../practice/albumentationsx_2.5.1_src_en.tar`〔部分资料〕 |

推荐顺序：Pillow（读写）→ OpenCV 核心模块与 Python 教程 → torchvision transforms v2 → Albumentations（复杂增强）→ OpenCV DNN 推理与 ONNX 互操作。

## 6. Hugging Face 生态

推荐顺序：先学05C50《Hugging Face LLM Course（构建版，含 Transformers/Datasets/Tokenizers/微调/推理）》 → `../courses/hf_llm_course_main_built_en.zip`LLM 课程，再按下列顺序查阅文档。

| 顺序 | 工具 | 用途 | 资料 |
|---|---|---|---|
| 1 | Hub 客户端（huggingface_hub） | 下载/上传模型与数据、缓存、推理客户端 | 05D28《Hugging Face huggingface_hub 客户端文档 v2.4.0》 → `../official_docs/hf_huggingface_hub_v2.4.0_docs_built_en.zip` |
| 2 | Transformers | 预训练模型加载、Pipeline、Trainer、生成、导出 | 05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip`、05X10《Transformers v5.22.0 官方示例脚本（examples/）》 → `../practice/hf_transformers_v5.22.0_examples_en.tar`、05X11《Hugging Face 官方笔记本（huggingface/notebooks）》 → `../practice/hf_notebooks_main_examples_en.tar` |
| 3 | Tokenizers | 快速分词器训练与使用 | 05D22《Hugging Face Tokenizers 文档 v0.23.3》 → `../official_docs/hf_tokenizers_v0.23.3_docs_built_en.zip` |
| 4 | Datasets | 数据加载、映射、流式、Arrow 缓存 | 05D21《Hugging Face Datasets 文档 v5.1.0》 → `../official_docs/hf_datasets_v5.1.0_docs_built_en.zip` |
| 5 | Evaluate | 指标计算（维护说明见首页） | 05D27《Hugging Face Evaluate 文档 v0.4.6》 → `../official_docs/hf_evaluate_v0.4.6_docs_built_en.zip` |
| 6 | Accelerate | 同一脚本跑单卡/多卡/FSDP/DeepSpeed | 05D23《Hugging Face Accelerate 文档（分布式、FSDP/DeepSpeed 集成、调试） v1.15.0》 → `../official_docs/hf_accelerate_v1.15.0_docs_built_en.zip`、05X15《Accelerate v1.15.0 示例（examples/）》 → `../practice/hf_accelerate_v1.15.0_examples_en.tar` |
| 7 | PEFT | LoRA 等参数高效微调、适配器合并 | 05D24《Hugging Face PEFT 文档（LoRA 等参数高效微调） v0.21.0》 → `../official_docs/hf_peft_v0.21.0_docs_built_en.zip`、05X13《PEFT v0.21.2 示例（examples/）》 → `../practice/hf_peft_v0.21.2_examples_en.tar` |
| 8 | TRL | SFT、DPO、GRPO 等后训练 | 05D25《Hugging Face TRL 文档（SFT/DPO/GRPO 等训练器） v1.17.0》 → `../official_docs/hf_trl_v1.17.0_docs_built_en.zip`、05X14《TRL v1.17.0 示例（examples/）》 → `../practice/hf_trl_v1.17.0_examples_en.tar` |
| 9 | Diffusers | 扩散模型推理与训练 | 05D26《Hugging Face Diffusers 文档 v0.42.1》 → `../official_docs/hf_diffusers_v0.42.1_docs_built_en.zip`、05X12《Diffusers v0.42.1 训练/推理示例（examples/）》 → `../practice/hf_diffusers_v0.42.1_examples_en.tar`；课程05C51《Hugging Face Diffusion Models Class（仓库源）》 → `../courses/hf_diffusion_models_class_main_src_en.tar` |

## 7. 模型交换与推理

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| ONNX | 跨框架模型格式（IR + 版本化算子集） | 任一训练框架 | 14D01《ONNX 官方文档（onnx.ai/onnx 离线镜像：概念、Python API、算子）》 → `../official_docs/onnx_docs_site_mirror_en.tar`、14D02《ONNX v1.23.2 规范与设计文档（docs/）》 → `../official_docs/onnx_1.23.2_spec_docs_en.tar`、14X01《ONNX 官方教程仓库（onnx/tutorials）》 → `../practice/onnx_tutorials_main_en.tar` | 1 |
| ONNX Runtime | 跨平台推理引擎，可插拔执行提供程序 | ONNX | 14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar`、14X02《ONNX Runtime 推理示例（onnxruntime-inference-examples）》 → `../practice/onnxruntime_inference_examples_main_en.tar` | 2 |
| TensorRT | NVIDIA GPU 推理优化编译器 | ONNX、CUDA 概念 | 14D04《TensorRT 官方文档（离线镜像）》 → `../official_docs/tensorrt_docs_latest_mirror_en.tar`、14X03《TensorRT OSS v10.16 示例与工具（samples、tools）》 → `../practice/tensorrt_oss_v10.16_samples_en.tar` | 3（NVIDIA 环境） |
| OpenVINO | Intel CPU/GPU/NPU 推理 | ONNX 或 PyTorch | 14D05《OpenVINO 2026.4.1 文档源（articles_en）》〔部分资料〕 → `../official_docs/openvino_2026.4.1_docs_src_en.tar`〔部分资料〕、14X04《OpenVINO Notebooks（官方教程笔记本）》 → `../practice/openvino_notebooks_latest_en.tar` | 3（Intel 环境） |

## 8. 大模型推理与部署

| 工具 | 用途 | 资料 | 选择建议 |
|---|---|---|---|
| vLLM | GPU 上高吞吐 LLM 服务（PagedAttention、OpenAI 兼容 API） | 14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar`〔部分资料〕；论文14P01《Efficient Memory Management for Large Language Model Serving with PagedAttention》 → `../papers/2023_Kwon_EfficientMemoryManagementLargeLanguage_en.pdf` | GPU 服务首选 |
| llama.cpp | C/C++ 本地推理、GGUF 量化、llama-server | 14D07《llama.cpp b11985 文档、工具说明与示例》 → `../official_docs/llama.cpp_b11985_docs_src_en.tar` | CPU/边缘/本地 |
| Triton Inference Server | 多框架模型服务、动态批处理、模型仓库 | 14D08《NVIDIA Triton Inference Server v2.73.0 文档（server/docs）》 → `../official_docs/triton_inference_server_2.73.0_docs_src_en.tar`、14X05《Triton Inference Server 官方教程（tutorials）》 → `../practice/triton_inference_server_tutorials_main_en.tar` | 多模型、多后端统一服务 |
| BentoML | Python 服务定义、打包与部署 | 14D09《BentoML 文档（docs.bentoml.com 离线镜像）》 → `../official_docs/bentoml_docs_mirror_en.tar`、14X06《BentoML v1.4.40 示例（examples/）》 → `../practice/bentoml_1.4.40_examples_en.tar` | 业务逻辑与模型一起打包 |

## 9. GPU 编程与训练优化

| 工具 | 用途 | 先修 | 资料 | 推荐顺序 |
|---|---|---|---|---|
| CUDA | GPU 编程模型与工具链 | C/C++、体系结构 | 13D01《CUDA Toolkit 核心指南 PDF 集（编程指南、最佳实践、PTX ISA）》 → `../official_docs/cuda_toolkit_guides_pdf_en`、13D02《Nsight Compute / Nsight Systems 性能分析文档（离线镜像）》 → `../official_docs/nsight_profiling_docs_mirror_en.tar`、13X01《NVIDIA cuda-samples v13.4》 → `../practice/cuda_samples_v13.4_en.tar`；课程13C01《Stanford CS149 Parallel Computing (Fall 2025) 课件》 → `../courses/Stanford_CS149_Fall2025_Slides_en`13C02《University of Oxford CUDA Programming Course（讲义与实践包）》 → `../courses/Oxford_CUDA_Course_en` | 1 |
| Triton 编程语言 | 用 Python 写分块 GPU 内核 | PyTorch、CUDA 概念 | 13D03《Triton 编程语言官方文档（triton-lang.org 构建 HTML，含教程）》 → `../official_docs/triton_lang_docs_main_html_en.tar`、13X02《Triton v3.9.0 教程源码（python/tutorials）》 → `../practice/triton_lang_v3.9.0_tutorials_en.tar` | 2 |
| NCCL | GPU 集合通信 | 分布式训练概念 | 13D06《NCCL 用户指南（离线镜像）》 → `../official_docs/nccl_user_guide_mirror_en.tar` | 3 |
| DeepSpeed | ZeRO、混合精度、流水并行 | PyTorch 分布式 | 13D04《DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源）》〔部分资料〕 → `../official_docs/deepspeed_0.19.8_docs_src_en.tar`〔部分资料〕、13D05《DeepSpeed API 参考（deepspeed.readthedocs.io 离线镜像）》 → `../official_docs/deepspeed_api_rtd_mirror_en.tar`、13X03《DeepSpeedExamples》 → `../practice/deepspeed_examples_master_en.tar` | 3 |
| 分布式训练官方工具（汇总） | torch.distributed / Accelerate / DeepSpeed / NCCL | 见上 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`、05D23《Hugging Face Accelerate 文档（分布式、FSDP/DeepSpeed 集成、调试） v1.15.0》 → `../official_docs/hf_accelerate_v1.15.0_docs_built_en.zip`、13D04《DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源）》〔部分资料〕 → `../official_docs/deepspeed_0.19.8_docs_src_en.tar`、13D06《NCCL 用户指南（离线镜像）》 → `../official_docs/nccl_user_guide_mirror_en.tar` | — |

## 10. 检索与 AI 应用

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| Sentence Transformers | 嵌入与重排模型的使用与训练 | 15D01《Sentence Transformers 文档（sbert.net 离线镜像）》 → `../official_docs/sentence_transformers_sbert_mirror_en.tar`、15X01《Sentence Transformers v6.2.0 示例（examples/）》 → `../practice/sentence_transformers_6.2.0_examples_en.tar` | 1 |
| FAISS | 向量索引与相似度检索 | 15D02《FAISS Wiki（官方使用文档）》 → `../official_docs/faiss_wiki_en.tar`、15X02《FAISS v1.15.1 教程与基准（tutorial/、benchs/）》 → `../practice/faiss_1.15.1_tutorial_en.tar` | 2 |
| LlamaIndex | 面向 RAG 的数据接入、索引与查询引擎 | 15D04《LlamaIndex v0.14.25 文档源（含示例笔记本）》〔部分资料〕 → `../official_docs/llamaindex_0.14.25_docs_src_en.tar`〔部分资料〕 | 3（二选一或都学） |
| LangChain / LangGraph | LLM 应用链、智能体与有状态图编排 | 15D03《LangChain / LangGraph 官方文档源（docs.langchain.com）》〔部分资料〕 → `../official_docs/langchain_docs_main_src_en.tar`〔部分资料〕 | 3 |

## 11. 实验与数据管理

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| TensorBoard | 训练曲线、超参、剖析可视化 | 04D08《TensorBoard 2.21.0 官方指南（docs/）》 → `../official_docs/tensorboard_2.21.0_docs_src_en.tar` | 1 |
| MLflow | 实验追踪、模型注册、模型格式与服务 | 04D05《MLflow 3.17.2 文档源（Docusaurus）》〔部分资料〕 → `../official_docs/mlflow_3.17.2_docs_src_en.tar`〔部分资料〕、04X05《MLflow 3.17.2 示例（examples/）》 → `../practice/mlflow_3.17.2_examples_en.tar` | 2 |
| DVC | 数据与管线版本控制 | 04D06《DVC 官方文档源（dvc.org 仓库 content/docs）》 → `../official_docs/dvc_docs_main_src_en.tar` | 2 |
| Weights & Biases | 托管实验追踪、扫参、制品 | 04D07《W&B 官方文档源（wandb/docs）》 → `../official_docs/wandb_docs_main_src_en.tar`、04X07《W&B 官方示例（wandb/examples）》 → `../practice/wandb_examples_master_en.tar` | 选学 |

## 12. 应用与部署基础

| 工具 | 用途 | 资料 | 推荐顺序 |
|---|---|---|---|
| FastAPI | 类型驱动的异步 Web API | 09D01《FastAPI 0.162.0 文档（英文）与文档示例源码》〔部分资料〕 → `../official_docs/fastapi_0.162.0_docs_src_en.tar`〔部分资料〕、09X02《Full Stack FastAPI Template（官方全栈模板）》 → `../practice/fastapi_full_stack_template_master_en.tar` | 1 |
| Gradio | 模型演示界面 | 10D01《Gradio 6.31.0 指南与演示源码》〔部分资料〕 → `../official_docs/gradio_6.31.0_guides_src_en.tar`〔部分资料〕 | 2 |
| Streamlit | 数据应用与内部工具 | 10D02《Streamlit 官方文档源（含 API 参考 JSON）》 → `../official_docs/streamlit_docs_main_src_en.tar` | 2 |
| Docker | 容器镜像与 Compose | 14D10《Docker 官方文档源（docker/docs content）》〔部分资料〕 → `../official_docs/docker_docs_main_src_en.tar`〔部分资料〕、14D12《Dockerfile 参考（moby/buildkit frontend/dockerfile/docs）》 → `../official_docs/dockerfile_reference_buildkit_master_en.tar`、14D13《Docker CLI 命令参考（docker/cli docs/reference）》 → `../official_docs/docker_cli_reference_master_en.tar`、14X07《Docker awesome-compose 示例》 → `../practice/docker_awesome_compose_master_en.tar` | 3 |
| Kubernetes | 容器编排 | 14D11《Kubernetes 官方文档源（website content/en）》 → `../official_docs/kubernetes_docs_main_src_en.tar`、14X08《Kubernetes 官方示例（kubernetes/examples）》 → `../practice/kubernetes_examples_master_en.tar` | 4 |

## 13. 测试与工程工具

| 工具 | 用途 | 资料 |
|---|---|---|
| pytest | 单元/集成测试、fixture、插件 | 06D01《pytest 稳定版文档（Read the Docs HTML 包）》 → `../official_docs/pytest_stable_docs_html_en.zip` |
| mypy / Pyright | 静态类型检查 | 06D02《mypy 稳定版文档（Read the Docs HTML 包）》 → `../official_docs/mypy_stable_docs_html_en.zip`、06D03《Pyright 1.1.414 文档（docs/）》 → `../official_docs/pyright_1.1.414_docs_src_en.tar`；规范06D05《Python 类型系统规范与指南（typing.python.org 源）》 → `../official_docs/python_typing_docs_main_src_en.tar` |
| Ruff | lint 与格式化 | 06D04《Ruff 0.17.3 文档（docs/）》〔部分资料〕 → `../official_docs/ruff_0.17.3_docs_src_en.tar`〔部分资料〕 |
| pip / uv / 打包指南 | 依赖安装、环境与项目管理、打包发布 | 01D02《pip 用户指南与参考》 → `../official_docs/pip_26.2.2_docs_src_en.tar`、01D04《uv 文档（Python 包与项目管理器）》〔部分资料〕 → `../official_docs/uv_0.13.6_docs_src_en.tar`〔部分资料〕、01D03《Python Packaging User Guide（PyPA 官方打包指南）》 → `../official_docs/python_packaging_user_guide_main_src_en.tar`、01D01《Python 3.15 官方文档（教程、语言参考、标准库、C API、打包与扩展）》 → `../official_docs/python_3.15_docs_html_en.tar.bz2`（venv） |

---

## 资料缺口（工具层面）

- 公开可下载的**大学课程**主要覆盖 PyTorch、TensorFlow、JAX 与 CUDA。OpenCV、ONNX、TensorRT、OpenVINO、vLLM、MLflow、DVC 等没有找到可完整下载的大学课程，只能依靠官方教程与示例。
- 部分工具官方只提供由 docstring 生成的在线 API 页、没有离线包（FastAPI、LangChain、LlamaIndex、vLLM、Gradio、OpenVINO、Ruff、uv、MLflow 等）。本库保存版本化文档源，标为部分资料。
- 具体失败与待补项见 `../download_failures_cn.csv`。
