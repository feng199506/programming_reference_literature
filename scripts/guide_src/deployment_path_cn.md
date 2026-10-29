# 部署与运维学习路线：容器、服务编排、CI/CD、可观测性、故障恢复与模型服务

适合对象：已能写后端服务（`application_path_cn.md` 阶段 3），熟悉 Linux 命令行与 Git 的学习者。
目标：能把服务和模型打包成镜像，用 CI/CD 自动测试发布，部署到 Kubernetes，配置监控告警，处理故障，并为模型选择合适的推理服务方案。

---

## 阶段 1：容器（约 2–3 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔14D10〕 | Docker 文档：get-started → Engine → Build（多阶段构建、缓存）→ Compose |
| 2 | 〔14D12〕 | Dockerfile 指令参考（编写与审阅 Dockerfile 时查询） |
| 3 | 〔14D13〕 | docker CLI 与 dockerd 参考 |
| 4 | 〔14X07〕 | awesome-compose：多服务组合示例 |
| 5 | 〔09X02〕 | FastAPI 全栈模板：Compose、测试、CI 的完整工程参考 |
| 安全 | 〔16D07〕 | 容器隔离的局限与 gVisor 沙箱 |

## 阶段 2：CI/CD（约 1–2 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔06D10〕 | GitHub Actions：工作流语法、缓存、矩阵、制品、密钥、环境与部署、安全加固 |
| 2 | 〔06X03〕 | 测试、类型检查、lint、发布一体化流水线模板 |
| 3 | 〔06B01〕 | 持续集成、持续交付与发布工程的组织实践（第 23–24 章） |
| 供应链 | 〔16D06〕、〔16D04〕 | SLSA 构建来源证明；NIST SSDF 安全开发实践 |

## 阶段 3：服务编排：Kubernetes（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔14D11〕 | Kubernetes 文档：concepts（Pod、Deployment、Service、ConfigMap/Secret、存储）→ tasks → tutorials；reference 查询 |
| 2 | 〔14X08〕 | 官方示例 |
| 3 | 〔14D22〕 | Helm：Chart 打包与发布 |
| 4 | 〔14X10〕 | Kubernetes The Hard Way：手动搭建，理解控制平面与证书 |

## 阶段 4：可观测性、可靠性与故障恢复（约 3–4 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔14B01〕 | SRE：SLO 与错误预算、监控四大黄金信号、事故响应、事后复盘、过载处理 |
| 2 | 〔14B02〕 | SLO 实施、告警设计、值班、金丝雀发布的案例 |
| 3 | 〔14D20〕 | Prometheus：指标类型、PromQL、告警规则、命名与仪表板实践 |
| 4 | 〔14D21〕 | OpenTelemetry：追踪、指标、日志三类信号；Collector；Python SDK |
| 5 | 〔16B01〕 | 可靠性与安全一体的设计、测试、部署与恢复 |
| 论文 | 〔14P15〕 | 尾延迟（The Tail at Scale） |

**故障恢复要点**（依据〔14B01〕〔14B02〕〔16B01〕）：发布可回滚（金丝雀/渐进）；数据有备份且定期演练恢复；告警基于用户可感知的 SLO；事故后写无责复盘并跟踪改进项。

## 阶段 5：分布式系统基础（约 6–8 周，可与阶段 3–4 并行）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔14B04〕 | 入门：可扩展性、时间与顺序、复制与一致性 |
| 2 | 〔14C02〕 | Cambridge 讲义：时钟、广播、复制、Raft、一致性模型、CRDT |
| 3 | 〔14C01〕、〔14C03〕 | MIT 6.5840：MapReduce、Raft、分片 KV 的讲义与实验说明；Princeton COS 418：RPC、Paxos/Raft、事务与拜占庭容错课件 |
| 4 | 〔14P09〕、〔14P10〕、〔14P11〕、〔14P12〕、〔14P13〕、〔14P14〕 | Lamport 时钟、Paxos、Raft、MapReduce、Dynamo、Borg（经典论文） |
| 5 | 〔14B03〕 | 理论：共识、FLP、故障检测（按需） |
| 6 | 〔14X11〕 | 系统设计练习：缓存、负载均衡、数据库扩展 |
| 7 | 〔08D03〕、〔08D04〕 | Kafka 与 Flink：消息与流处理系统运维 |

## 阶段 6：模型服务与推理部署（约 4–6 周）

先修条件：`ai_programming_path_cn.md` 阶段 5，本路线阶段 1–3。导出格式的选择先读 `../tools/interoperability_guide_cn.md`。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔04B04〕 | 从模型到产品：部署、监控、数据漂移、MLOps 全景 |
| 2 | 〔04C02〕 | CMU ML in Production 课件与实验 |
| 3 | 〔14D01〕、〔14D02〕 | ONNX：IR、算子集版本、Python API |
| 4 | 〔14D03〕、〔14X02〕 | ONNX Runtime：执行提供程序（CPU/CUDA/TensorRT/OpenVINO）、图优化、量化、性能调优 |
| 5 | 〔14D04〕、〔14X03〕 | TensorRT：ONNX 解析、精度（FP16/INT8/FP8）、引擎构建与 Polygraphy 排障 |
| 6 | 〔14D05〕、〔14X04〕 | OpenVINO：模型转换（PyTorch/ONNX/TF）、CPU/GPU/NPU 推理与优化 |
| 7 | 〔14D08〕、〔14X05〕 | Triton Inference Server：模型仓库、配置、动态批处理、多后端、性能分析器（与 Triton 编程语言无关） |
| 8 | 〔14D06〕 | vLLM：OpenAI 兼容服务、并行与量化、部署（Docker/K8s） |
| 9 | 〔14D07〕 | llama.cpp：GGUF 转换与量化、llama-server、CPU/GPU 后端 |
| 10 | 〔14D09〕、〔14X06〕 | BentoML：服务定义、打包、自适应批处理、部署 |
| 11 | 〔14D23〕 | KServe：在 Kubernetes 上服务模型 |
| 12 | 〔09D01〕、〔10D01〕、〔10D02〕 | 轻量服务与演示：FastAPI 包装模型；Gradio/Streamlit 界面 |
| 论文 | 〔14P01〕、〔14P03〕、〔14P02〕、〔14P05〕、〔14P06〕、〔14P04〕、〔14P07〕、〔14P08〕 | PagedAttention(vLLM)、Sarathi-Serve、DistServe、Splitwise、Mooncake、SGLang、推测解码、DeepSpeed-FastGen |

**模型服务选型速记**（依据上表官方文档，详见互操作指南）：

- 传统 ML 或小型网络、需跨语言或在 CPU 上运行：导出 ONNX，用 ONNX Runtime。
- NVIDIA GPU 上追求极致延迟：ONNX → TensorRT 引擎（与 GPU 架构、TensorRT 版本绑定），可由 Triton Inference Server 托管。
- Intel CPU/GPU/NPU：OpenVINO。
- 大语言模型的 GPU 服务：vLLM（OpenAI 兼容接口、PagedAttention）。
- 大语言模型的本地/CPU/边缘部署：llama.cpp（GGUF 量化）。
- 需要把 Python 业务逻辑与模型一起打包：BentoML，或 FastAPI + Docker。
