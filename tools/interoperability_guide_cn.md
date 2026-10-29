# 框架训练、模型导出、ONNX 与推理部署：互操作指南

依据：本库已下载并核验的官方文档（括号内为资料编号与文档内页面）。版本以 2026-10-29 为准。
用途：在"用什么框架训练 → 保存成什么格式 → 用什么引擎推理与服务"之间选路，并提前知道每一步的兼容条件与限制。

> 文中凡写"依据"之处，均可在对应资料中找到原文。未能在已下载文档中核实的内容标为"未核实"，不作结论。

---

## 1. 全局关系图

```
训练框架                     中间/交换格式                         推理引擎 / 服务
───────────                 ────────────────                      ─────────────────────────
PyTorch ──torch.export──▶ ExportedProgram(.pt2) ──AOTInductor──▶ 本机 C++/Python 推理
   │   └─torch.onnx.export(dynamo=True)──▶ ONNX ──┐
   │                                              ├─▶ ONNX Runtime（CPU/CUDA/TensorRT/OpenVINO 等 EP）
Transformers ─Optimum ONNX─▶ ONNX ───────────────┤
scikit-learn ─skl2onnx(第三方)─▶ ONNX ───────────┤─▶ TensorRT（解析 ONNX → 引擎 plan，绑定 GPU）
XGBoost/LightGBM ─(onnxmltools 等第三方)─▶ ONNX ─┤─▶ OpenVINO（也可直接读 PyTorch/TF/ONNX）
Keras 3 ─model.export(format=…)─▶ LiteRT/…       ├─▶ OpenCV DNN（readNet/readNetFromONNX）
TensorFlow ─tf.saved_model.save─▶ SavedModel ─────┘─▶ Triton Inference Server（多后端托管）
Transformers ─save_pretrained─▶ HF 格式(safetensors) ─▶ vLLM（OpenAI 兼容服务）
                     └─convert_hf_to_gguf.py─▶ GGUF ─llama-quantize─▶ llama.cpp / llama-server
任意 Python 模型 ───────────────────────────────────▶ BentoML / FastAPI 服务 → Docker → Kubernetes/KServe
```

## 2. 各训练框架的保存与导出

### 2.1 PyTorch 2.15

依据05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`：`2.15/onnx.html`、`2.15/onnx_export.html`、`2.15/export.html` 及 `2.15/torch.compiler_aot_inductor*.html`。

- **ONNX 导出**：`torch.onnx.export(..., dynamo=True)` 在 2.15 中默认基于 torch.export，文档称其为"PyTorch 2.6 及更新版本的最新导出器"。旧的 TorchScript 路径（`dynamo=False`）的若干参数已标为弃用：`training`、`operator_export_type`、`do_constant_folding`、`custom_opsets`、`export_modules_as_functions`、`autograd_inlining` 等。
- **动态形状**：`dynamo=True` 时用 `dynamic_shapes`；`dynamic_axes` 已弃用，只对 `dynamo=False` 有效。
- **opset**：`opset_version` 需按目标运行时支持的 opset 设置（文档原话："You should set opset_version according to the supported opset versions"）。
- **自带验证**：`verify=True` 用 ONNX Runtime 校验导出模型；`report=True`、`dump_exported_program=True` 用于排障。
- **torch.export / AOTInductor**：先把模型捕获为 ExportedProgram，再用 AOTInductor 编译成可部署产物，不经过 ONNX。排障见 `torch.compiler_aot_inductor_debugging_guide.html` 与 minifier 页面。
- **教程**：05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`中有导出与 ONNX 相关篇目。示例见05X01《PyTorch 官方示例（pytorch/examples）》 → `../practice/pytorch_examples_main_en.tar`。

### 2.2 Hugging Face Transformers

依据05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip` `en/serialization.md`、05D29《Hugging Face Optimum ONNX v0.1.0 文档（Transformers → ONNX 导出与 ONNX Runtime 推理）》 → `../official_docs/hf_optimum-onnx_v0.1.0_docs_built_en.zip`。

- 原生保存：`save_pretrained` / `from_pretrained`，即 HF 格式（权重为 safetensors，另有配置与分词器文件）。vLLM 直接读取这种格式。
- **ONNX**：Transformers 文档指向 **Optimum ONNX**。命令行 `optimum-cli export onnx --model <模型> <输出目录>`，或用 `ORTModelFor…from_pretrained(..., export=True)` 导出后直接在 ONNX Runtime 推理。导出本地模型时，权重与分词器需放在同一目录，并用 `--task` 指定任务。
- **ExecuTorch**（移动/边缘）：通过 Optimum ExecuTorch 的 `optimum-cli export executorch`。本库未单独下载 ExecuTorch 文档（05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip`中有该页）。
- **GGUF**：05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip` `en/quantization/gguf.md` 说明 Transformers 可加载 GGUF。生成 GGUF 见 2.7 节 llama.cpp。

### 2.3 Keras 3 与 TensorFlow

依据05D07《Keras 3 官方指南与示例源（keras-io）》 → `../official_docs/keras_io_master_src_en.tar` `guides/md/serialization_and_saving.md`、`guides/md/litert_export.md`；05D05《TensorFlow 官方指南与教程源（tensorflow/docs site/en）》 → `../official_docs/tensorflow_docs_guides_master_src_en.tar` `site/en/guide/saved_model.ipynb`。

- Keras 3 的保存格式是 `.keras`（zip 包，含配置、权重与编译信息）。文档原话："The only supported format in Keras 3 is the 'Keras v3' format"。旧 H5 与 TF SavedModel 不再作为 `model.save` 的格式。
- **导出**：`model.export(path, format=...)`。已核实 `format="litert"` 可导出 LiteRT（原 TensorFlow Lite）模型，且该指南演示的是 **PyTorch 后端**下的导出。05D08《Keras 3 API 参考（keras.io/api 离线镜像）》 → `../official_docs/keras_api_reference_mirror_en.tar` `api/models/model_saving_apis/export.html` 列出的全部取值为：`"tf_saved_model"`（默认）、`"onnx"`（可用 `opset_version` 指定 opset）、`"openvino"`、`"litert"`、`"torch"`。限制：`format="litert"` 配合 PyTorch 后端时**不支持动态输入形状**，None 维会被替换为 1，必须显式传入覆盖最大运行形状的静态 `input_signature`。JAX 后端导出 `tf_saved_model` 时内部经 jax2tf，可通过 `jax2tf_kwargs` 传参。
- TensorFlow：`tf.saved_model.save(model, dir)` / `tf.saved_model.load(dir)` 生成 SavedModel，可用于 TensorFlow Serving，或由 OpenVINO 直接读取。TF → ONNX 需要第三方工具 tf2onnx（不在本库官方文档范围内，未核实其当前版本支持情况）。

### 2.4 JAX

依据05D09《JAX 官方文档（Read the Docs HTML 包）》 → `../official_docs/jax_latest_docs_html_en.zip`（JAX 官方单页文档，"Exporting and serializing staged-out computations"与 jax.export 模块）：

- `jax.export` 把 JAX 函数导出为 StableHLO，并附带调用元数据（`Exported`），再以 flatbuffers 序列化为字节串，用于持久归档或在别处调用。`jit(...).trace/lower/compile` 的中间结果**不能**直接序列化后跨进程使用。
- 调用约定版本：自 JAX 0.7.0（2025 年 7 月）起默认导出版本 10。
- 兼容窗口：导出物可由**新不超过 6 个月**的 JAX/编译器加载（向后兼容），也可由**旧不超过 3 周**的版本加载（向前兼容）。窗口长度按"导出端与消费端的构建时间"计算。
- 安全：反序列化后的字节串必须是**可信输入**，执行时可能触发已注册的自定义调用。
- 与 TensorFlow 互操作可用 jax2tf（导出为 TF 图，兼容窗口相同）。JAX 没有官方 ONNX 导出器；OpenVINO 把 JAX/Flax 转换列为实验特性（见第 4 节）。

### 2.5 scikit-learn

依据04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar` `1.9/model_persistence.html`：

| 方式 | 文档结论 |
|---|---|
| ONNX | 不需要 Python 对象、只做推理时可能最合适。**注意：并非所有模型都受 ONNX 支持**（转换器为第三方 skl2onnx） |
| skops.io | 比 pickle 系格式更安全，速度较慢，支持的类型较少 |
| pickle / joblib / cloudpickle | 基于 pickle，加载不可信文件有执行任意代码的风险。必须在相同 scikit-learn 与依赖版本下加载 |

### 2.6 梯度提升库

- XGBoost 3.4.2（04D02《XGBoost 稳定版文档（PDF）》 → `../official_docs/xgboost_stable_docs_en.pdf`"Introduction to Model IO"）：自 2.1.0 起默认模型格式为 UBJSON，`booster.save_model('model.json')` 或 `.ubj` 按扩展名选格式。使用类别特征时**必须**用 JSON/UBJSON 保存，否则信息丢失。文档另有"模型与内存快照的向后兼容说明"，pickle 快照不保证跨版本。
- LightGBM04D03《LightGBM 稳定版文档（PDF）》 → `../official_docs/lightgbm_stable_docs_en.pdf`、CatBoost04D04《CatBoost 1.2.10 官方文档源（英文）》 → `../official_docs/catboost_1.2.10_docs_src_en.tar`：各自有原生文本/二进制模型格式与导出章节，按需查阅。CatBoost 文档含导出为 ONNX、CoreML 等格式的章节。

### 2.7 大语言模型专用格式

- **GGUF / llama.cpp**（14D07《llama.cpp b11985 文档、工具说明与示例》 → `../official_docs/llama.cpp_b11985_docs_src_en.tar` `tools/quantize/README.md`）：先 `python convert_hf_to_gguf.py --outfile <模型>-bf16.gguf --outtype bf16 <HF 模型>` 得到高精度 GGUF，再 `llama-quantize <in>.gguf <out>.gguf Q4_K_M` 量化。服务端用 `tools/server`（llama-server）。
- **vLLM 0.32**（14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar`）：读取 HF 格式。量化（14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar` `docs/features/quantization/README.md`）推荐用 LLM Compressor 生成 FP8/INT8/INT4，另支持 AWQ、GPTQ、bitsandbytes 等。**GGUF 支持已迁移到树外插件 vllm-gguf-plugin，文档明确为"高度实验、未充分优化、可能与其他功能不兼容"**。对外接口为 OpenAI 兼容服务器（`docs/serving/online_serving/openai_compatible_server.md`）。

## 3. ONNX 版本体系与兼容条件

依据14D02《ONNX v1.23.2 规范与设计文档（docs/）》 → `../official_docs/onnx_1.23.2_spec_docs_en.tar` `docs/Versioning.md`、`docs/IR.md`，14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar` `docs/reference/compatibility.md`。

- ONNX 模型同时带 **IR 版本**与**各算子域的 opset 版本**。运行时必须同时支持两者。
- `Versioning.md` 版本表摘录：ONNX 1.20 → IR 13 / opset 25；1.21 → IR 13 / opset 26；1.22 → IR 13 / opset 27；**1.23 → IR 14 / opset 28**（ai.onnx.ml opset 均为 5）。
- ONNX Runtime 官方兼容表（`compatibility.md`）**只更新到 ORT 1.20**（对应 ONNX 1.16.1、opset 21、IR 10）。ORT 1.21–1.31 的支持范围需查对应 release 说明，本库未下载 release notes，**未核实**。
- 实务规则：
  1. 导出时显式设置 `opset_version`，取训练端与目标运行时都支持的值，不盲目用最高版本。
  2. 导出后用 ONNX Runtime 对比原框架输出（PyTorch 可直接 `verify=True`）。
  3. 动态维度用 `dynamic_shapes` 声明，否则形状会被固化。
  4. 自定义算子需在导出端注册转换，并在运行端提供实现。

## 4. 推理引擎与服务的兼容条件和限制

| 目标 | 输入格式 | 关键兼容条件 / 限制 | 依据 |
|---|---|---|---|
| ONNX Runtime | ONNX | 支持的 opset/IR 受 ORT 版本限制（见第 3 节）。通过执行提供程序（EP）切换硬件。1.19 起 GPU 包默认 CUDA 12。量化见 `docs/performance/model-optimizations/quantization.md` | 14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar` |
| ORT + TensorRT EP | ONNX | 文档建议**同时注册 CUDAExecutionProvider**，让 TensorRT 不支持的节点回退到 CUDA。可配置子图最小规模、转储子图、引擎缓存 | 14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar` `execution-providers/TensorRT-ExecutionProvider.md` |
| TensorRT | ONNX（经 ONNX Parser）→ 引擎（plan） | 支持矩阵页（`getting-started/support-matrix.html`）写明：**不开启硬件兼容模式时，引擎不能跨 GPU 架构移植**；开启后可在多个架构上运行，取决于兼容级别。**版本兼容**：以 version-compatible 标志构建的引擎可在受支持的更新运行时上运行，跨大版本只支持 TensorRT 10 引擎 → 11 运行时、8 → 10 两种组合，其他均不支持。Triton 文档同样指出 plan 与计算能力绑定。排障用 Polygraphy | 14D04《TensorRT 官方文档（离线镜像）》 → `../official_docs/tensorrt_docs_latest_mirror_en.tar`、14D08《NVIDIA Triton Inference Server v2.73.0 文档（server/docs）》 → `../official_docs/triton_inference_server_2.73.0_docs_src_en.tar`、14X03《TensorRT OSS v10.16 示例与工具（samples、tools）》 → `../practice/tensorrt_oss_v10.16_samples_en.tar` |
| OpenVINO | PyTorch、TensorFlow、TensorFlow Lite、ONNX、PaddlePaddle；JAX/Flax 为实验特性 | 用 `openvino.convert_model` + `save_model`，或命令行 `ovc`。**PyTorch 与 JAX/Flax 只能用 Python API 转换**。PyTorch 也可通过 `torch.compile` 的 OpenVINO 后端运行 | 14D05《OpenVINO 2026.4.1 文档源（articles_en）》〔部分资料〕 → `../official_docs/openvino_2026.4.1_docs_src_en.tar` `openvino-workflow/model-preparation.rst` |
| OpenCV DNN | ONNX 等 | 有"PyTorch 分割模型转换后由 OpenCV DNN 推理"的官方教程。层支持范围以 OpenCV 版本为准 | 05D10《OpenCV 5.0.0 官方文档（Doxygen HTML 包，含 Python 教程）》 → `../official_docs/opencv_5.0.0_docs_html_en.zip` `pytorch_segm_tutorial_dnn_conversion.html` 等 |
| Triton Inference Server | ONNX、TensorRT plan、PyTorch、OpenVINO（model.xml/.bin）、Python 后端等 | ONNX 模型的支持范围等于 Triton 内置 ORT 的支持范围；**过旧的 opset 或含不支持类型的算子不被支持**；不同 PyTorch 版本导出的模型可能因 opset 变化而不受支持。TensorRT 模型需按计算能力提供 plan（`cc_model_filenames`） | 14D08《NVIDIA Triton Inference Server v2.73.0 文档（server/docs）》 → `../official_docs/triton_inference_server_2.73.0_docs_src_en.tar` `docs/user_guide/model_repository.md` |
| vLLM | HF 格式（+ 量化格式） | GGUF 需外部插件且为实验性。并行与量化选项见文档 | 14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar` |
| llama.cpp | GGUF | 需先转换再量化。量化类型与精度、速度的权衡见 quantize README | 14D07《llama.cpp b11985 文档、工具说明与示例》 → `../official_docs/llama.cpp_b11985_docs_src_en.tar` |
| BentoML | 任意 Python 可加载模型 | 服务以 Python 定义，打包为 Bento/容器 | 14D09《BentoML 文档（docs.bentoml.com 离线镜像）》 → `../official_docs/bentoml_docs_mirror_en.tar` |

## 5. 选型建议（由上述约束推出）

1. **跨平台、CPU 优先、模型较小（传统 ML、CNN、小型 Transformer）**：ONNX + ONNX Runtime。先在 CPU EP 上验证正确性，再换 GPU EP。
2. **NVIDIA GPU、追求最低延迟**：ONNX → TensorRT（或 ORT 的 TensorRT EP 加 CUDA EP 回退）。部署机与构建机的 GPU 架构、TensorRT 版本要一致。
3. **Intel 硬件（CPU/iGPU/NPU）**：OpenVINO，PyTorch 模型用 Python API 直接转换。
4. **多模型、多框架统一服务**：Triton Inference Server，模型仓库中按后端放置 ONNX/plan/OpenVINO/Python 模型。
5. **LLM 在线服务（GPU）**：vLLM（HF 格式 + 推荐的量化方案），OpenAI 兼容接口便于应用接入。
6. **LLM 本地或离线、CPU、边缘**：llama.cpp + GGUF 量化。
7. **业务逻辑复杂、需要快速上线**：BentoML 或 FastAPI 包装模型，Docker 打包，Kubernetes/KServe 编排（14D10《Docker 官方文档源（docker/docs content）》〔部分资料〕 → `../official_docs/docker_docs_main_src_en.tar`14D11《Kubernetes 官方文档源（website content/en）》 → `../official_docs/kubernetes_docs_main_src_en.tar`14D23《KServe 文档源（Kubernetes 模型服务）》 → `../official_docs/kserve_website_main_src_en.tar`）。

## 6. 导出后的验证清单

1. **数值一致性**：同一批输入下，原框架与目标引擎输出的最大绝对误差与相对误差在容差内。FP16/INT8 时要另设容差，并在验证集上比较精度指标。
2. **形状与批大小**：覆盖最小、典型、最大输入形状，以及动态批大小。
3. **算子覆盖**：检查导出日志与运行时日志中的回退/不支持节点（ORT 可转储子图分配；TensorRT 用 Polygraphy 检查）。
4. **性能**：在目标硬件上测延迟分位数与吞吐，记录引擎版本、opset、精度与批大小。
5. **版本锁定**：在部署清单中记录训练框架、导出器、ONNX、运行时（ORT/TensorRT/OpenVINO）与驱动/CUDA 的版本。
6. **安全**：不加载来源不明的 pickle 类模型文件（04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar`的持久化页面已提示），优先使用 safetensors、ONNX、skops 等不执行代码的格式。

## 7. 相关资料速查

- 导出端：05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip`05D29《Hugging Face Optimum ONNX v0.1.0 文档（Transformers → ONNX 导出与 ONNX Runtime 推理）》 → `../official_docs/hf_optimum-onnx_v0.1.0_docs_built_en.zip`05D07《Keras 3 官方指南与示例源（keras-io）》 → `../official_docs/keras_io_master_src_en.tar`05D08《Keras 3 API 参考（keras.io/api 离线镜像）》 → `../official_docs/keras_api_reference_mirror_en.tar`05D05《TensorFlow 官方指南与教程源（tensorflow/docs site/en）》 → `../official_docs/tensorflow_docs_guides_master_src_en.tar`05D09《JAX 官方文档（Read the Docs HTML 包）》 → `../official_docs/jax_latest_docs_html_en.zip`04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar`04D02《XGBoost 稳定版文档（PDF）》 → `../official_docs/xgboost_stable_docs_en.pdf`04D03《LightGBM 稳定版文档（PDF）》 → `../official_docs/lightgbm_stable_docs_en.pdf`04D04《CatBoost 1.2.10 官方文档源（英文）》 → `../official_docs/catboost_1.2.10_docs_src_en.tar`
- 格式：14D01《ONNX 官方文档（onnx.ai/onnx 离线镜像：概念、Python API、算子）》 → `../official_docs/onnx_docs_site_mirror_en.tar`14D02《ONNX v1.23.2 规范与设计文档（docs/）》 → `../official_docs/onnx_1.23.2_spec_docs_en.tar`14X01《ONNX 官方教程仓库（onnx/tutorials）》 → `../practice/onnx_tutorials_main_en.tar`
- 运行时：14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar`14X02《ONNX Runtime 推理示例（onnxruntime-inference-examples）》 → `../practice/onnxruntime_inference_examples_main_en.tar`14D04《TensorRT 官方文档（离线镜像）》 → `../official_docs/tensorrt_docs_latest_mirror_en.tar`14X03《TensorRT OSS v10.16 示例与工具（samples、tools）》 → `../practice/tensorrt_oss_v10.16_samples_en.tar`14D05《OpenVINO 2026.4.1 文档源（articles_en）》〔部分资料〕 → `../official_docs/openvino_2026.4.1_docs_src_en.tar`14X04《OpenVINO Notebooks（官方教程笔记本）》 → `../practice/openvino_notebooks_latest_en.tar`05D10《OpenCV 5.0.0 官方文档（Doxygen HTML 包，含 Python 教程）》 → `../official_docs/opencv_5.0.0_docs_html_en.zip`
- 服务：14D08《NVIDIA Triton Inference Server v2.73.0 文档（server/docs）》 → `../official_docs/triton_inference_server_2.73.0_docs_src_en.tar`14X05《Triton Inference Server 官方教程（tutorials）》 → `../practice/triton_inference_server_tutorials_main_en.tar`14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar`14D07《llama.cpp b11985 文档、工具说明与示例》 → `../official_docs/llama.cpp_b11985_docs_src_en.tar`14D09《BentoML 文档（docs.bentoml.com 离线镜像）》 → `../official_docs/bentoml_docs_mirror_en.tar`14X06《BentoML v1.4.40 示例（examples/）》 → `../practice/bentoml_1.4.40_examples_en.tar`14D23《KServe 文档源（Kubernetes 模型服务）》 → `../official_docs/kserve_website_main_src_en.tar`
- 论文：14P01《Efficient Memory Management for Large Language Model Serving with PagedAttention》 → `../papers/2023_Kwon_EfficientMemoryManagementLargeLanguage_en.pdf`（PagedAttention）、14P07《Fast Inference from Transformers via Speculative Decoding》 → `../papers/2022_Leviathan_FastInferenceFromTransformersSpeculative_en.pdf`（推测解码）、13P11《FP8 Formats for Deep Learning》 → `../papers/2022_Micikevicius_FP8FormatsDeepLearning_en.pdf`（FP8 格式）
