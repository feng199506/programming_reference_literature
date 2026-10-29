# 部署与运维学习路线：容器、服务编排、CI/CD、可观测性、故障恢复与模型服务

适合对象：已能写后端服务（`application_path_cn.md` 阶段 3），熟悉 Linux 命令行与 Git 的学习者。
目标：能把服务和模型打包成镜像，用 CI/CD 自动测试发布，部署到 Kubernetes，配置监控告警，处理故障，并为模型选择合适的推理服务方案。

---

## 阶段 1：容器（约 2–3 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 14D10《Docker 官方文档源（docker/docs content）》〔部分资料〕 → `../official_docs/docker_docs_main_src_en.tar` | Docker 文档：get-started → Engine → Build（多阶段构建、缓存）→ Compose |
| 2 | 14D12《Dockerfile 参考（moby/buildkit frontend/dockerfile/docs）》 → `../official_docs/dockerfile_reference_buildkit_master_en.tar` | Dockerfile 指令参考（编写与审阅 Dockerfile 时查询） |
| 3 | 14D13《Docker CLI 命令参考（docker/cli docs/reference）》 → `../official_docs/docker_cli_reference_master_en.tar` | docker CLI 与 dockerd 参考 |
| 4 | 14X07《Docker awesome-compose 示例》 → `../practice/docker_awesome_compose_master_en.tar` | awesome-compose：多服务组合示例 |
| 5 | 09X02《Full Stack FastAPI Template（官方全栈模板）》 → `../practice/fastapi_full_stack_template_master_en.tar` | FastAPI 全栈模板：Compose、测试、CI 的完整工程参考 |
| 安全 | 16D07《gVisor 文档源（容器沙箱）》 → `../official_docs/gvisor_docs_master_src_en.tar` | 容器隔离的局限与 gVisor 沙箱 |

## 阶段 2：CI/CD（约 1–2 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 06D10《GitHub Actions 官方文档（github/docs content/actions）》 → `../official_docs/github_actions_docs_main_src_en.tar` | GitHub Actions：工作流语法、缓存、矩阵、制品、密钥、环境与部署、安全加固 |
| 2 | 06X03《Hypermodern Python Cookiecutter（打包、类型检查、测试与 CI 模板）》 → `../practice/cjolowicz_cookiecutter_hypermodern_python_main_en.tar` | 测试、类型检查、lint、发布一体化流水线模板 |
| 3 | 06B01《Software Engineering at Google: Lessons Learned from Programming Over Time》 → `../books/Winters_SoftwareEngineeringAtGoogle_html_en.tar` | 持续集成、持续交付与发布工程的组织实践（第 23–24 章） |
| 供应链 | 16D06《SLSA 供应链安全规范》 → `../official_docs/slsa_spec_main_en.tar`、16D04《NIST SP 800-218 Secure Software Development Framework (SSDF) 1.1》 → `../official_docs/nist_sp800_218_ssdf_1.1_en.pdf` | SLSA 构建来源证明；NIST SSDF 安全开发实践 |

## 阶段 3：服务编排：Kubernetes（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 14D11《Kubernetes 官方文档源（website content/en）》 → `../official_docs/kubernetes_docs_main_src_en.tar` | Kubernetes 文档：concepts（Pod、Deployment、Service、ConfigMap/Secret、存储）→ tasks → tutorials；reference 查询 |
| 2 | 14X08《Kubernetes 官方示例（kubernetes/examples）》 → `../practice/kubernetes_examples_master_en.tar` | 官方示例 |
| 3 | 14D22《Helm 文档源》 → `../official_docs/helm_docs_main_src_en.tar` | Helm：Chart 打包与发布 |
| 4 | 14X10《Kubernetes The Hard Way》 → `../practice/kubernetes_the_hard_way_master_en.tar` | Kubernetes The Hard Way：手动搭建，理解控制平面与证书 |

## 阶段 4：可观测性、可靠性与故障恢复（约 3–4 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 14B01《Site Reliability Engineering: How Google Runs Production Systems》 → `../books/Beyer_SiteReliabilityEngineering_html_en.tar` | SRE：SLO 与错误预算、监控四大黄金信号、事故响应、事后复盘、过载处理 |
| 2 | 14B02《The Site Reliability Workbook》 → `../books/Beyer_SiteReliabilityWorkbook_html_en.tar` | SLO 实施、告警设计、值班、金丝雀发布的案例 |
| 3 | 14D20《Prometheus 文档源（概念、查询、告警、最佳实践）》 → `../official_docs/prometheus_docs_main_src_en.tar` | Prometheus：指标类型、PromQL、告警规则、命名与仪表板实践 |
| 4 | 14D21《OpenTelemetry 文档源》 → `../official_docs/opentelemetry_docs_main_src_en.tar` | OpenTelemetry：追踪、指标、日志三类信号；Collector；Python SDK |
| 5 | 16B01《Building Secure and Reliable Systems》 → `../books/Adkins_BuildingSecureReliableSystems_html_en.tar` | 可靠性与安全一体的设计、测试、部署与恢复 |
| 论文 | 14P15《The Tail at Scale》 → `../papers/2013_Dean_TailAtScale_en.pdf` | 尾延迟（The Tail at Scale） |

**故障恢复要点**（依据14B01《Site Reliability Engineering: How Google Runs Production Systems》 → `../books/Beyer_SiteReliabilityEngineering_html_en.tar`14B02《The Site Reliability Workbook》 → `../books/Beyer_SiteReliabilityWorkbook_html_en.tar`16B01《Building Secure and Reliable Systems》 → `../books/Adkins_BuildingSecureReliableSystems_html_en.tar`）：发布可回滚（金丝雀/渐进）；数据有备份且定期演练恢复；告警基于用户可感知的 SLO；事故后写无责复盘并跟踪改进项。

## 阶段 5：分布式系统基础（约 6–8 周，可与阶段 3–4 并行）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 14B04《Distributed Systems for Fun and Profit》 → `../books/Takada_DistributedSystemsForFunAndProfit_html_en.tar` | 入门：可扩展性、时间与顺序、复制与一致性 |
| 2 | 14C02《University of Cambridge Concurrent and Distributed Systems 讲义》 → `../courses/Cambridge_ConcDisSys_2024_DistSysNotes_en.pdf` | Cambridge 讲义：时钟、广播、复制、Raft、一致性模型、CRDT |
| 3 | 14C01《MIT 6.5840 Distributed Systems (Spring 2026) 讲义与实验》〔部分资料〕 → `../courses/MIT_6.5840_Spring2026_Materials_html_en.tar`、14C03《Princeton COS 418 Distributed Systems (Fall 2025) 课件与习题课讲义》〔部分资料〕 → `../courses/Princeton_COS418_Fall2025_Slides_en` | MIT 6.5840：MapReduce、Raft、分片 KV 的讲义与实验说明；Princeton COS 418：RPC、Paxos/Raft、事务与拜占庭容错课件 |
| 4 | 14P09《Time, Clocks, and the Ordering of Events in a Distributed System》 → `../papers/1978_Lamport_TimeClocksOrderingEventsDistributed_en.pdf`、14P10《Paxos Made Simple》 → `../papers/2001_Lamport_PaxosMadeSimple_en.pdf`、14P11《In Search of an Understandable Consensus Algorithm》 → `../papers/2014_Ongaro_SearchUnderstandableConsensusAlgorithm_en.pdf`、14P12《MapReduce: Simplified Data Processing on Large Clusters》 → `../papers/2004_Dean_MapReduceSimplifiedDataProcessingLarge_en.pdf`、14P13《Dynamo: Amazon's Highly Available Key-value Store》 → `../papers/2007_DeCandia_DynamoAmazonSHighlyAvailable_en.pdf`、14P14《Large-scale cluster management at Google with Borg》 → `../papers/2015_Verma_LargeScaleClusterManagementAt_en.pdf` | Lamport 时钟、Paxos、Raft、MapReduce、Dynamo、Borg（经典论文） |
| 5 | 14B03《Notes on Theory of Distributed Systems》 → `../books/Aspnes_NotesTheoryDistributedSystems_en.pdf` | 理论：共识、FLP、故障检测（按需） |
| 6 | 14X11《The System Design Primer》 → `../practice/system_design_primer_master_en.tar` | 系统设计练习：缓存、负载均衡、数据库扩展 |
| 7 | 08D03《Apache Kafka 4.x 官方文档（kafka-site）》 → `../official_docs/apache_kafka_site_docs_en.tar`、08D04《Apache Flink 2.x 文档源（docs/content）》 → `../official_docs/apache_flink_docs_src_en.tar` | Kafka 与 Flink：消息与流处理系统运维 |

## 阶段 6：模型服务与推理部署（约 4–6 周）

先修条件：`ai_programming_path_cn.md` 阶段 5，本路线阶段 1–3。导出格式的选择先读 `../tools/interoperability_guide_cn.md`。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 04B04《Machine Learning in Production: From Models to Products》 → `../books/Kastner_MachineLearningInProduction_html_en.tar` | 从模型到产品：部署、监控、数据漂移、MLOps 全景 |
| 2 | 04C02《CMU 17-445/645 Machine Learning in Production（课件与实验）》 → `../courses/CMU_17645_MLinProduction_2025_src_en.tar` | CMU ML in Production 课件与实验 |
| 3 | 14D01《ONNX 官方文档（onnx.ai/onnx 离线镜像：概念、Python API、算子）》 → `../official_docs/onnx_docs_site_mirror_en.tar`、14D02《ONNX v1.23.2 规范与设计文档（docs/）》 → `../official_docs/onnx_1.23.2_spec_docs_en.tar` | ONNX：IR、算子集版本、Python API |
| 4 | 14D03《ONNX Runtime 官方文档（onnxruntime.ai/docs 源 + 已构建 API 页）》 → `../official_docs/onnxruntime_docs_ghpages_en.tar`、14X02《ONNX Runtime 推理示例（onnxruntime-inference-examples）》 → `../practice/onnxruntime_inference_examples_main_en.tar` | ONNX Runtime：执行提供程序（CPU/CUDA/TensorRT/OpenVINO）、图优化、量化、性能调优 |
| 5 | 14D04《TensorRT 官方文档（离线镜像）》 → `../official_docs/tensorrt_docs_latest_mirror_en.tar`、14X03《TensorRT OSS v10.16 示例与工具（samples、tools）》 → `../practice/tensorrt_oss_v10.16_samples_en.tar` | TensorRT：ONNX 解析、精度（FP16/INT8/FP8）、引擎构建与 Polygraphy 排障 |
| 6 | 14D05《OpenVINO 2026.4.1 文档源（articles_en）》〔部分资料〕 → `../official_docs/openvino_2026.4.1_docs_src_en.tar`、14X04《OpenVINO Notebooks（官方教程笔记本）》 → `../practice/openvino_notebooks_latest_en.tar` | OpenVINO：模型转换（PyTorch/ONNX/TF）、CPU/GPU/NPU 推理与优化 |
| 7 | 14D08《NVIDIA Triton Inference Server v2.73.0 文档（server/docs）》 → `../official_docs/triton_inference_server_2.73.0_docs_src_en.tar`、14X05《Triton Inference Server 官方教程（tutorials）》 → `../practice/triton_inference_server_tutorials_main_en.tar` | Triton Inference Server：模型仓库、配置、动态批处理、多后端、性能分析器（与 Triton 编程语言无关） |
| 8 | 14D06《vLLM v0.32.0 文档源与示例》〔部分资料〕 → `../official_docs/vllm_0.32.0_docs_src_en.tar` | vLLM：OpenAI 兼容服务、并行与量化、部署（Docker/K8s） |
| 9 | 14D07《llama.cpp b11985 文档、工具说明与示例》 → `../official_docs/llama.cpp_b11985_docs_src_en.tar` | llama.cpp：GGUF 转换与量化、llama-server、CPU/GPU 后端 |
| 10 | 14D09《BentoML 文档（docs.bentoml.com 离线镜像）》 → `../official_docs/bentoml_docs_mirror_en.tar`、14X06《BentoML v1.4.40 示例（examples/）》 → `../practice/bentoml_1.4.40_examples_en.tar` | BentoML：服务定义、打包、自适应批处理、部署 |
| 11 | 14D23《KServe 文档源（Kubernetes 模型服务）》 → `../official_docs/kserve_website_main_src_en.tar` | KServe：在 Kubernetes 上服务模型 |
| 12 | 09D01《FastAPI 0.162.0 文档（英文）与文档示例源码》〔部分资料〕 → `../official_docs/fastapi_0.162.0_docs_src_en.tar`、10D01《Gradio 6.31.0 指南与演示源码》〔部分资料〕 → `../official_docs/gradio_6.31.0_guides_src_en.tar`、10D02《Streamlit 官方文档源（含 API 参考 JSON）》 → `../official_docs/streamlit_docs_main_src_en.tar` | 轻量服务与演示：FastAPI 包装模型；Gradio/Streamlit 界面 |
| 论文 | 14P01《Efficient Memory Management for Large Language Model Serving with PagedAttention》 → `../papers/2023_Kwon_EfficientMemoryManagementLargeLanguage_en.pdf`、14P03《Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve》 → `../papers/2024_Agrawal_TamingThroughputLatencyTradeoffLLM_en.pdf`、14P02《DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving》 → `../papers/2024_Zhong_DistServeDisaggregatingPrefillDecodingGoodput_en.pdf`、14P05《Splitwise: Efficient generative LLM inference using phase splitting》 → `../papers/2023_Patel_SplitwiseEfficientGenerativeLLMInference_en.pdf`、14P06《Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving》 → `../papers/2024_Qin_MooncakeKVCacheCentricDisaggregatedArchitecture_en.pdf`、14P04《SGLang: Efficient Execution of Structured Language Model Programs》 → `../papers/2023_Zheng_SGLangEfficientExecutionStructuredLanguage_en.pdf`、14P07《Fast Inference from Transformers via Speculative Decoding》 → `../papers/2022_Leviathan_FastInferenceFromTransformersSpeculative_en.pdf`、14P08《DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference》 → `../papers/2024_Holmes_DeepSpeedFastGenHighThroughputText_en.pdf` | PagedAttention(vLLM)、Sarathi-Serve、DistServe、Splitwise、Mooncake、SGLang、推测解码、DeepSpeed-FastGen |

**模型服务选型速记**（依据上表官方文档，详见互操作指南）：

- 传统 ML 或小型网络、需跨语言或在 CPU 上运行：导出 ONNX，用 ONNX Runtime。
- NVIDIA GPU 上追求极致延迟：ONNX → TensorRT 引擎（与 GPU 架构、TensorRT 版本绑定），可由 Triton Inference Server 托管。
- Intel CPU/GPU/NPU：OpenVINO。
- 大语言模型的 GPU 服务：vLLM（OpenAI 兼容接口、PagedAttention）。
- 大语言模型的本地/CPU/边缘部署：llama.cpp（GGUF 量化）。
- 需要把 Python 业务逻辑与模型一起打包：BentoML，或 FastAPI + Docker。
