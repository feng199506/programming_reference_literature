# 应用开发学习路线：后端、前端、数据库、RAG 与智能体

适合对象：完成 `beginner_path_cn.md` 阶段 1–5 的学习者。做 AI 应用的读者最好再完成 `ai_programming_path_cn.md` 阶段 1–4。
目标：能设计并实现带认证、异步任务、缓存和接口文档的 Web 服务，配一个可访问的前端。在此基础上搭建 RAG 与工具调用智能体，并能评测其效果。

---

## 阶段 1：HTTP 与 Web 基础（约 2 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 10D51《MDN Web Docs 内容源（HTML、CSS、JavaScript、HTTP、可访问性、Learn）》〔部分资料〕 → `../official_docs/mdn_content_web_core_main_src_en.tar` | MDN 学习区（learn_web_development）通读；HTTP 子树的概览、缓存、Cookie、CORS 必读 |
| 2 | 09B01《High Performance Browser Networking》 → `../books/Grigorik_HighPerformanceBrowserNetworking_html_en.tar`、09B02《HTTP/3 explained》 → `../books/Stenberg_HTTP3Explained_src_en.tar`、09B03《HTTP/2 explained》 → `../books/Stenberg_HTTP2Explained_src_en.tar` | TCP/TLS/HTTP/2、WebSocket 与 SSE 的性能原理（流式响应的底层） |
| 查询 | 09D03《HTTP 与 Web 认证核心 RFC 集》 → `../official_docs/ietf_http_auth_rfcs_en` | HTTP 语义（RFC 9110）、缓存（9111）、HTTP/1.1–3、TLS 1.3、OAuth 2.0、JWT、WebSocket 标准原文 |

## 阶段 2：数据库与数据建模（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 08B05《Database Design (2nd ed.)》 → `../books/Watt_DatabaseDesign_2ndEd_html_en.tar` | ER 建模、规范化、约束（入门） |
| 2 | 08C02《UC Berkeley CS 186 Introduction to Database Systems 课程讲义》 → `../courses/Berkeley_CS186_Notes_html_en.tar` | Berkeley CS 186 讲义：SQL、索引、连接算法、事务与恢复 |
| 3 | 08B04《Use The Index, Luke!（SQL 索引与性能）》 → `../books/Winand_UseTheIndexLuke_html_en.tar` | 索引与执行计划：写出可被索引利用的 SQL |
| 4 | 08D01《PostgreSQL 18 官方文档（A4 PDF）》 → `../official_docs/postgresql_18_docs_a4_en.pdf` | PostgreSQL 18：教程部分通读；事务隔离（MVCC）、索引类型、EXPLAIN、性能提示按需查询 |
| 5 | 08D02《SQLite 文档包（3.54.1）》 → `../official_docs/sqlite_doc_3540100_en.zip` | SQLite：嵌入式场景、WAL 与查询规划器 |
| 进阶 | 08C01《CMU 15-445/645 Database Systems (Fall 2025) 课件与讲义》 → `../courses/CMU_15445_Fall2025_Slides_en`、08B01《Readings in Database Systems (5th ed., Red Book)》 → `../books/Bailis_ReadingsInDatabaseSystems_5thEd_en.pdf` | 数据库内部实现（配合08X01《CMU BusTub（教学关系数据库系统骨架）》 → `../practice/cmu_bustub_master_en.tar`BusTub 实践） |
| 理论 | 08B03《Foundations of Databases》 → `../books/Abiteboul_FoundationsOfDatabases_1995_en.pdf` | 关系理论与查询语言（按需） |

## 阶段 3：后端与 API（约 6–8 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 09C01《Harvard CS50's Web Programming with Python and JavaScript 讲义与项目》 → `../courses/Harvard_CS50W_NotesProjects_html_en.tar` | Harvard CS50W：Django、SQL/ORM、测试与 CI、安全与扩展 |
| 2 | 09D51《Django 6.0 官方文档（HTML 包）》 → `../official_docs/django_6.0_docs_html_en.zip` | Django 6.0 官方教程 + 认证、表单、缓存、测试、部署检查清单 |
| 3 | 09D01《FastAPI 0.162.0 文档（英文）与文档示例源码》〔部分资料〕 → `../official_docs/fastapi_0.162.0_docs_src_en.tar` | FastAPI：教程（路径/请求体/依赖注入/安全/OAuth2+JWT/文件上传/后台任务/流式响应/测试）→ 高级指南 → 部署 |
| 4 | 09D02《Flask 文档源与官方教程示例（pallets/flask）》〔部分资料〕 → `../official_docs/flask_docs_src_en.tar` | Flask：应用工厂、蓝图、测试；examples/tutorial 完整示例 |
| 5 | 06B02《Architecture Patterns with Python（Cosmic Python）》 → `../books/Percival_ArchitecturePatternsWithPython_html_en.tar` | 服务层、仓储、单元工作、事件：把业务逻辑与框架解耦 |
| 6 | 09D05《Celery 文档源（异步任务队列）》〔部分资料〕 → `../official_docs/celery_docs_src_en.tar` | Celery：异步任务、重试、调度 |
| 7 | 09D04《OpenAPI Specification（含 3.1/3.2 版本全文）》 → `../official_docs/openapi_specification_main_en.tar`、09D06《Microsoft REST API Guidelines》 → `../official_docs/microsoft_api_guidelines_vnext_en.tar`、09D07《Google API Improvement Proposals（AIP）》 → `../official_docs/google_aip_master_en.tar` | OpenAPI 规范；Microsoft REST API 指南与 Google AIP（资源命名、分页、错误、版本化） |
| 8 | 08D03《Apache Kafka 4.x 官方文档（kafka-site）》 → `../official_docs/apache_kafka_site_docs_en.tar`、08D04《Apache Flink 2.x 文档源（docs/content）》 → `../official_docs/apache_flink_docs_src_en.tar` | 消息系统与流处理（Kafka、Flink），按需 |
| 9 | 09C02《Stanford CS 142 Web Applications 讲义》 → `../courses/Stanford_CS142_LectureNotes_en` | Stanford CS142 讲义：会话、数据库、Web 安全、扩展 |
| 安全 | 16D01《OWASP Cheat Sheet Series》 → `../official_docs/owasp_cheatsheet_series_master_en.tar`、16C01《Stanford CS 253 Web Security 课件》 → `../courses/Stanford_CS253_Slides_en` | 输入校验、认证、会话、CSRF/XSS 的速查与课程 |

**服务测试清单**（依据09D01《FastAPI 0.162.0 文档（英文）与文档示例源码》〔部分资料〕 → `../official_docs/fastapi_0.162.0_docs_src_en.tar`06D01《pytest 稳定版文档（Read the Docs HTML 包）》 → `../official_docs/pytest_stable_docs_html_en.zip`06B02《Architecture Patterns with Python（Cosmic Python）》 → `../books/Percival_ArchitecturePatternsWithPython_html_en.tar`）：用 TestClient 做接口测试；用依赖覆盖替换数据库与外部服务；仓储层用内存实现做单元测试；集成测试连接真实数据库容器。

## 阶段 4：前端与交互界面（约 6–8 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 10B01《Eloquent JavaScript (4th ed.)》 → `../books/Haverbeke_EloquentJavaScript_4thEd_en.pdf` | JavaScript 语言、DOM、事件、异步 |
| 2 | 10C01《University of Helsinki Full Stack Open 课程正文（英文）》 → `../courses/Helsinki_FullStackOpen_src_en.tar`、10C02《MIT 6.4500 Design for the Web: Languages and User Interfaces（课程站点）》 → `../courses/MIT_6.4500_DesignForTheWeb_html_en.tar` | Helsinki Full Stack Open：React → 状态管理 → Node/Express REST → 测试 → TypeScript → CI/CD → 容器；MIT 6.4500：可用性、可访问性与界面设计 |
| 3 | 10D52《TypeScript Handbook 与参考文档源》 → `../official_docs/typescript_handbook_src_en.tar`、10B03《TypeScript Deep Dive》 → `../books/Basarat_TypeScriptDeepDive_src_en.tar` | TypeScript 手册与工程实践 |
| 4 | 10D03《React 官方文档源（react.dev）》 → `../official_docs/react_dev_docs_main_src_en.tar` | React 官方文档：learn 通读，reference 查询 |
| 5 | 10D04《WAI-ARIA Authoring Practices Guide（APG）源》 → `../official_docs/w3c_aria_practices_main_en.tar` | 可访问组件模式与键盘交互（WAI-ARIA APG） |
| 6 | 10D05《D3.js 官方文档源》 → `../official_docs/d3_docs_main_src_en.tar`、03B05《Fundamentals of Data Visualization》 → `../books/Wilke_FundamentalsOfDataVisualization_html_en.tar` | 数据可视化：D3 与可视化原则 |
| 进阶 | 10B02《You Don't Know JS Yet (2nd ed.)》 → `../books/Simpson_YouDontKnowJSYet_2ndEd_src_en.tar` | JS 作用域、闭包、对象与类型的深入理解 |
| 快速 AI 界面 | 10D01《Gradio 6.31.0 指南与演示源码》〔部分资料〕 → `../official_docs/gradio_6.31.0_guides_src_en.tar`、10D02《Streamlit 官方文档源（含 API 参考 JSON）》 → `../official_docs/streamlit_docs_main_src_en.tar` | Gradio 与 Streamlit：模型演示与内部工具 |

## 阶段 5：RAG 与检索（约 4–6 周）

先修条件：阶段 3，`ai_programming_path_cn.md` 阶段 4–5（至少会用 PyTorch / Transformers）。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 15B01《Introduction to Information Retrieval》（未获取，见 download_failures_cn.csv） | 信息检索基础：倒排索引、评分、评测指标（P/R、MAP、NDCG） |
| 2 | 15P01《Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks》 → `../papers/2020_Lewis_RetrievalAugmentedGenerationKnowledgeIntensive_en.pdf`、15P18《ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT》 → `../papers/2020_Khattab_ColBERTEfficientEffectivePassageSearch_en.pdf`、15P19《Dense Passage Retrieval for Open-Domain Question Answering》 → `../papers/2020_Karpukhin_DensePassageRetrievalOpenDomain_en.pdf` | RAG 原始论文、DPR、ColBERT（稠密检索与后期交互） |
| 3 | 15D01《Sentence Transformers 文档（sbert.net 离线镜像）》 → `../official_docs/sentence_transformers_sbert_mirror_en.tar`、15X01《Sentence Transformers v6.2.0 示例（examples/）》 → `../practice/sentence_transformers_6.2.0_examples_en.tar` | Sentence Transformers：嵌入模型、检索与重排、微调 |
| 4 | 15D02《FAISS Wiki（官方使用文档）》 → `../official_docs/faiss_wiki_en.tar`、15X02《FAISS v1.15.1 教程与基准（tutorial/、benchs/）》 → `../practice/faiss_1.15.1_tutorial_en.tar` | FAISS：索引选择、IVF/HNSW/PQ、GPU、调参 FAQ |
| 5 | 02P12《Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs》 → `../papers/2016_Malkov_EfficientRobustApproximateNearestNeighbor_en.pdf` | HNSW 原理论文 |
| 6 | 15D04《LlamaIndex v0.14.25 文档源（含示例笔记本）》〔部分资料〕 → `../official_docs/llamaindex_0.14.25_docs_src_en.tar`、15D03《LangChain / LangGraph 官方文档源（docs.langchain.com）》〔部分资料〕 → `../official_docs/langchain_docs_main_src_en.tar` | LlamaIndex 与 LangChain：数据加载、索引、检索器、查询引擎、链与图（LangGraph） |
| 7 | 15P11《Retrieval-Augmented Generation for Large Language Models: A Survey》 → `../papers/2023_Gao_RetrievalAugmentedGenerationLargeLanguage_en.pdf`、15P10《Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection》 → `../papers/2023_Asai_SelfRAGLearningRetrieveGenerate_en.pdf`、15P09《Lost in the Middle: How Language Models Use Long Contexts》 → `../papers/2023_Liu_LostMiddleHowLanguageModels_en.pdf` | RAG 综述、Self-RAG、长上下文中的位置效应（上下文管理依据） |
| 8 | 15P12《Ragas: Automated Evaluation of Retrieval Augmented Generation》 → `../papers/2023_Es_RagasAutomatedEvaluationRetrievalAugmented_en.pdf`、15P13《Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena》 → `../papers/2023_Zheng_JudgingLLMAsJudgeMT_en.pdf` | RAG 评测（RAGAS）与 LLM-as-a-judge |

## 阶段 6：工具调用、智能体与代码编辑（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 15C01《UC Berkeley CS294/194-196 Large Language Model Agents (Fall 2024) 课件》 → `../courses/Berkeley_CS294_LLMAgents_Fall2024_Slides_en`、15C02《UC Berkeley Advanced Large Language Model Agents (Spring 2025) 课件》 → `../courses/Berkeley_AdvLLMAgents_Spring2025_Slides_en` | Berkeley LLM Agents 课程课件：推理、规划、工具、代码智能体、安全 |
| 2 | 15C50《Hugging Face Agents Course（仓库源）》 → `../courses/hf_agents_course_main_src_en.tar` | Hugging Face Agents Course：smolagents、LlamaIndex、LangGraph 智能体实践 |
| 3 | 15P02《ReAct: Synergizing Reasoning and Acting in Language Models》 → `../papers/2022_Yao_ReActSynergizingReasoningActingLanguage_en.pdf`、15P03《Toolformer: Language Models Can Teach Themselves to Use Tools》 → `../papers/2023_Schick_ToolformerLanguageModelsTeachThemselves_en.pdf`、15P08《Executable Code Actions Elicit Better LLM Agents》 → `../papers/2024_Wang_ExecutableCodeActionsElicitBetter_en.pdf`、15P14《Reflexion: Language Agents with Verbal Reinforcement Learning》 → `../papers/2023_Shinn_ReflexionLanguageAgentsVerbalReinforcement_en.pdf`、15P15《MemGPT: Towards LLMs as Operating Systems》 → `../papers/2023_Packer_MemGPTTowardsLLMsAsOperating_en.pdf`、15P17《Gorilla: Large Language Model Connected with Massive APIs》 → `../papers/2023_Patil_GorillaLargeLanguageModelConnected_en.pdf` | ReAct、Toolformer、CodeAct、Reflexion、MemGPT（记忆/上下文管理）、Gorilla（API 调用） |
| 4 | 15D10《Model Context Protocol 规范与文档》 → `../official_docs/mcp_specification_main_en.tar` | Model Context Protocol：工具/资源/提示、传输与授权 |
| 5 | 15D14《OpenAI Agents SDK（Python）文档源与示例》〔部分资料〕 → `../official_docs/openai_agents_python_docs_src_en.tar`、15X51《Anthropic Claude Cookbooks》 → `../practice/anthropic_claude_cookbooks_main_en.tar`、15X52《OpenAI Cookbook》 → `../practice/openai_cookbook_main_en.tar` | OpenAI Agents SDK、Claude 与 OpenAI Cookbook（工具调用、RAG、评测示例） |
| 6 | 15D13《DSPy 文档源》〔部分资料〕 → `../official_docs/dspy_docs_main_src_en.tar` | DSPy：把提示工程变成可优化的程序 |
| 7 | 15X04《mini-SWE-agent（约百行的参考代码智能体）》 → `../practice/mini_swe_agent_main_en.tar`、15X05《Aider（终端 AI 结对编程工具源码）》 → `../practice/aider_main_en.tar` | 代码编辑智能体参考实现：mini-SWE-agent（极简）、Aider（编辑格式、仓库地图、Git 集成） |
| 8 | 15P04《SWE-bench: Can Language Models Resolve Real-World GitHub Issues?》 → `../papers/2023_Jimenez_SWEBenchLanguageModelsResolve_en.pdf`、15P05《SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering》 → `../papers/2024_Yang_SWEAgentAgentComputerInterfaces_en.pdf`、15P06《Agentless: Demystifying LLM-based Software Engineering Agents》 → `../papers/2024_Xia_AgentlessDemystifyingLLMBasedSoftware_en.pdf`、15P07《OpenHands: An Open Platform for AI Software Developers as Generalist Agents》 → `../papers/2024_Wang_OpenHandsOpenPlatformAISoftware_en.pdf`、15X03《SWE-bench（代码智能体评测框架）》 → `../practice/swe_bench_main_en.tar` | SWE-bench、SWE-agent、Agentless、OpenHands；评测框架与容器化执行隔离 |
| 9 | 15P16《$τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains》 → `../papers/2024_Yao_BenchBenchmarkToolAgentUser_en.pdf` | τ-bench：工具-用户交互评测 |
| 10 | 15D11《Language Server Protocol 规范》 → `../official_docs/lsp_specification_en.tar`、15D12《VS Code 扩展 API 文档源》 → `../official_docs/vscode_extension_api_docs_src_en.tar` | IDE 集成：LSP 规范、VS Code 扩展 API |
| 隔离 | 16D07《gVisor 文档源（容器沙箱）》 → `../official_docs/gvisor_docs_master_src_en.tar` | gVisor：用户态内核沙箱（执行不可信代码） |

**智能体工程要点**（依据上表资料）：

1. 工具接口要窄、参数可校验、返回可截断。
2. 上下文按"系统指令 → 任务 → 检索片段 → 历史"分层管理，长文档优先检索而非整篇塞入。
3. 代码执行放进容器或 gVisor 沙箱，限制网络与文件系统。
4. 用固定任务集和自动判分持续评测，修改提示或工具后回归测试。

衔接：服务化与部署见 `deployment_path_cn.md`。安全要求见 `core_reading_list_cn.md` 的安全部分。
