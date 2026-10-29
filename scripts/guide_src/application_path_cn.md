# 应用开发学习路线：后端、前端、数据库、RAG 与智能体

适合对象：完成 `beginner_path_cn.md` 阶段 1–5 的学习者。做 AI 应用的读者最好再完成 `ai_programming_path_cn.md` 阶段 1–4。
目标：能设计并实现带认证、异步任务、缓存和接口文档的 Web 服务，配一个可访问的前端。在此基础上搭建 RAG 与工具调用智能体，并能评测其效果。

---

## 阶段 1：HTTP 与 Web 基础（约 2 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔10D51〕 | MDN 学习区（learn_web_development）通读；HTTP 子树的概览、缓存、Cookie、CORS 必读 |
| 2 | 〔09B01〕、〔09B02〕、〔09B03〕 | TCP/TLS/HTTP/2、WebSocket 与 SSE 的性能原理（流式响应的底层） |
| 查询 | 〔09D03〕 | HTTP 语义（RFC 9110）、缓存（9111）、HTTP/1.1–3、TLS 1.3、OAuth 2.0、JWT、WebSocket 标准原文 |

## 阶段 2：数据库与数据建模（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔08B05〕 | ER 建模、规范化、约束（入门） |
| 2 | 〔08C02〕 | Berkeley CS 186 讲义：SQL、索引、连接算法、事务与恢复 |
| 3 | 〔08B04〕 | 索引与执行计划：写出可被索引利用的 SQL |
| 4 | 〔08D01〕 | PostgreSQL 18：教程部分通读；事务隔离（MVCC）、索引类型、EXPLAIN、性能提示按需查询 |
| 5 | 〔08D02〕 | SQLite：嵌入式场景、WAL 与查询规划器 |
| 进阶 | 〔08C01〕、〔08B01〕 | 数据库内部实现（配合〔08X01〕BusTub 实践） |
| 理论 | 〔08B03〕 | 关系理论与查询语言（按需） |

## 阶段 3：后端与 API（约 6–8 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔09C01〕 | Harvard CS50W：Django、SQL/ORM、测试与 CI、安全与扩展 |
| 2 | 〔09D51〕 | Django 6.0 官方教程 + 认证、表单、缓存、测试、部署检查清单 |
| 3 | 〔09D01〕 | FastAPI：教程（路径/请求体/依赖注入/安全/OAuth2+JWT/文件上传/后台任务/流式响应/测试）→ 高级指南 → 部署 |
| 4 | 〔09D02〕 | Flask：应用工厂、蓝图、测试；examples/tutorial 完整示例 |
| 5 | 〔06B02〕 | 服务层、仓储、单元工作、事件：把业务逻辑与框架解耦 |
| 6 | 〔09D05〕 | Celery：异步任务、重试、调度 |
| 7 | 〔09D04〕、〔09D06〕、〔09D07〕 | OpenAPI 规范；Microsoft REST API 指南与 Google AIP（资源命名、分页、错误、版本化） |
| 8 | 〔08D03〕、〔08D04〕 | 消息系统与流处理（Kafka、Flink），按需 |
| 9 | 〔09C02〕 | Stanford CS142 讲义：会话、数据库、Web 安全、扩展 |
| 安全 | 〔16D01〕、〔16C01〕 | 输入校验、认证、会话、CSRF/XSS 的速查与课程 |

**服务测试清单**（依据〔09D01〕〔06D01〕〔06B02〕）：用 TestClient 做接口测试；用依赖覆盖替换数据库与外部服务；仓储层用内存实现做单元测试；集成测试连接真实数据库容器。

## 阶段 4：前端与交互界面（约 6–8 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔10B01〕 | JavaScript 语言、DOM、事件、异步 |
| 2 | 〔10C01〕、〔10C02〕 | Helsinki Full Stack Open：React → 状态管理 → Node/Express REST → 测试 → TypeScript → CI/CD → 容器；MIT 6.4500：可用性、可访问性与界面设计 |
| 3 | 〔10D52〕、〔10B03〕 | TypeScript 手册与工程实践 |
| 4 | 〔10D03〕 | React 官方文档：learn 通读，reference 查询 |
| 5 | 〔10D04〕 | 可访问组件模式与键盘交互（WAI-ARIA APG） |
| 6 | 〔10D05〕、〔03B05〕 | 数据可视化：D3 与可视化原则 |
| 进阶 | 〔10B02〕 | JS 作用域、闭包、对象与类型的深入理解 |
| 快速 AI 界面 | 〔10D01〕、〔10D02〕 | Gradio 与 Streamlit：模型演示与内部工具 |

## 阶段 5：RAG 与检索（约 4–6 周）

先修条件：阶段 3，`ai_programming_path_cn.md` 阶段 4–5（至少会用 PyTorch / Transformers）。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔15B01〕 | 信息检索基础：倒排索引、评分、评测指标（P/R、MAP、NDCG） |
| 2 | 〔15P01〕、〔15P18〕、〔15P19〕 | RAG 原始论文、DPR、ColBERT（稠密检索与后期交互） |
| 3 | 〔15D01〕、〔15X01〕 | Sentence Transformers：嵌入模型、检索与重排、微调 |
| 4 | 〔15D02〕、〔15X02〕 | FAISS：索引选择、IVF/HNSW/PQ、GPU、调参 FAQ |
| 5 | 〔02P12〕 | HNSW 原理论文 |
| 6 | 〔15D04〕、〔15D03〕 | LlamaIndex 与 LangChain：数据加载、索引、检索器、查询引擎、链与图（LangGraph） |
| 7 | 〔15P11〕、〔15P10〕、〔15P09〕 | RAG 综述、Self-RAG、长上下文中的位置效应（上下文管理依据） |
| 8 | 〔15P12〕、〔15P13〕 | RAG 评测（RAGAS）与 LLM-as-a-judge |

## 阶段 6：工具调用、智能体与代码编辑（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 〔15C01〕、〔15C02〕 | Berkeley LLM Agents 课程课件：推理、规划、工具、代码智能体、安全 |
| 2 | 〔15C50〕 | Hugging Face Agents Course：smolagents、LlamaIndex、LangGraph 智能体实践 |
| 3 | 〔15P02〕、〔15P03〕、〔15P08〕、〔15P14〕、〔15P15〕、〔15P17〕 | ReAct、Toolformer、CodeAct、Reflexion、MemGPT（记忆/上下文管理）、Gorilla（API 调用） |
| 4 | 〔15D10〕 | Model Context Protocol：工具/资源/提示、传输与授权 |
| 5 | 〔15D14〕、〔15X51〕、〔15X52〕 | OpenAI Agents SDK、Claude 与 OpenAI Cookbook（工具调用、RAG、评测示例） |
| 6 | 〔15D13〕 | DSPy：把提示工程变成可优化的程序 |
| 7 | 〔15X04〕、〔15X05〕 | 代码编辑智能体参考实现：mini-SWE-agent（极简）、Aider（编辑格式、仓库地图、Git 集成） |
| 8 | 〔15P04〕、〔15P05〕、〔15P06〕、〔15P07〕、〔15X03〕 | SWE-bench、SWE-agent、Agentless、OpenHands；评测框架与容器化执行隔离 |
| 9 | 〔15P16〕 | τ-bench：工具-用户交互评测 |
| 10 | 〔15D11〕、〔15D12〕 | IDE 集成：LSP 规范、VS Code 扩展 API |
| 隔离 | 〔16D07〕 | gVisor：用户态内核沙箱（执行不可信代码） |

**智能体工程要点**（依据上表资料）：

1. 工具接口要窄、参数可校验、返回可截断。
2. 上下文按"系统指令 → 任务 → 检索片段 → 历史"分层管理，长文档优先检索而非整篇塞入。
3. 代码执行放进容器或 gVisor 沙箱，限制网络与文件系统。
4. 用固定任务集和自动判分持续评测，修改提示或工具后回归测试。

衔接：服务化与部署见 `deployment_path_cn.md`。安全要求见 `core_reading_list_cn.md` 的安全部分。
