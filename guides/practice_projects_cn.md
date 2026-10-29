# 实践项目索引：按难度列出配套项目与评价方式

说明：

- 本库只保存项目源码、说明和许可证，不执行来源代码，也不下载数据集与模型权重。动手时请在自己的隔离环境中按项目 README 安装依赖。
- 难度：★ 入门（完成对应路线前两阶段即可）；★★ 进阶；★★★ 高级。
- 评价方式说明怎样判断"做完了、做对了"，优先使用项目自带的测试或评分脚本。

---

## ★ 入门

| 项目 | 对应路线/先修 | 内容 | 评价方式 |
|---|---|---|---|
| 01C01《MIT 6.100L Introduction to CS and Programming Using Python (Fall 2022) OCW 课程包》 → `../courses/MIT_6.100L_Fall2022_OCW_en.zip` 中的 problem set | 编程基础 阶段 1 | Python 基础编程作业 | 对照 OCW 包内的作业说明自测；可读性用 Ruff 检查 |
| 01X02《Exercism Python track（练习题、测试与说明）》 → `../practice/exercism_python_main_en.tar` | 编程基础 阶段 1 | 按概念递进的 Python 练习 | 每题自带测试，全部通过即完成 |
| 07X01《Software Carpentry: The Unix Shell》 → `../practice/swcarpentry_shell_novice_main_en.tar`、07X02《Software Carpentry: Version Control with Git》 → `../practice/swcarpentry_git_novice_main_en.tar` | 编程基础 阶段 0/4 | Shell 与 Git 课堂练习 | 完成每课 challenge，能脱离讲义复述命令 |
| 03X51《100 NumPy exercises》 → `../practice/rougier_numpy_100_master_en.tar`、03X02《pandas_exercises》 → `../practice/guipsamora_pandas_exercises_master_en.tar` | AI 编程 阶段 1/3 | NumPy 向量化、pandas 分主题练习 | 不写 Python 循环得到与参考答案一致的结果 |
| 06X02《Software Carpentry: Programming with Python（含防御式编程与测试）》 → `../practice/swcarpentry_python_novice_inflammation_main_en.tar` | 编程基础 阶段 5 | 防御式编程、调试与测试 | 为每个函数补充断言与 pytest 用例 |
| 05X51《micrograd（最小自动微分引擎）》 → `../practice/karpathy_micrograd_master_en.tar` | AI 编程 阶段 5 | 标量自动微分引擎 | 自己的实现与 PyTorch 梯度在随机表达式上数值一致（误差 < 1e-6） |
| 10X01《TodoMVC（同一应用的多框架实现）》 → `../practice/todomvc_master_en.tar` | 应用开发 阶段 4 | 同一 Todo 应用的多框架实现 | 自选框架重写一遍，功能对照规范 |

## ★★ 进阶

| 项目 | 对应路线/先修 | 内容 | 评价方式 |
|---|---|---|---|
| 01X01《pytudes（Peter Norvig 的 Python 练习与编程问题集）》 → `../practice/norvig_pytudes_main_en.tar` | 编程基础 + 算法 | Norvig 的谜题与算法笔记本 | 先独立解题，再对比简洁性与复杂度 |
| 02X01《TheAlgorithms/Python（算法参考实现集）》 → `../practice/TheAlgorithms_Python_master_en.tar`、02X02《algs4：Sedgewick & Wayne《Algorithms, 4th ed.》配套 Java 源码》 → `../practice/algs4_master_en.tar` | 算法 | 参考实现（Python / Java） | 自己实现后，用参考实现做对拍测试 |
| 06X01《500 Lines or Less（AOSA 小型完整项目集）》 → `../practice/aosabook_500lines_master_en.tar` | 软件工程 | 20+ 个小而完整的系统（模板引擎、数据库、CI 系统等） | 选 2–3 个重写，写测试覆盖其核心行为 |
| 06X03《Hypermodern Python Cookiecutter（打包、类型检查、测试与 CI 模板）》 → `../practice/cjolowicz_cookiecutter_hypermodern_python_main_en.tar` | 软件工程 | 打包 + 类型检查 + 测试 + CI 模板 | 把自己的项目迁移到该结构，CI 全绿 |
| 04X51《Made With ML（MLOps 端到端课程项目）》 → `../practice/madewithml_main_en.tar` | AI 编程 阶段 4/7 | 端到端 MLOps：数据、训练、调优、评估、服务、CI/CD | 复现基线指标；离线评估与服务化接口测试都通过 |
| 04X52《Cookiecutter Data Science（项目结构模板 v2）》 → `../practice/cookiecutter_data_science_master_en.tar` | AI 编程 阶段 4 | 数据科学项目结构 | 用模板组织一个项目，`make` 或脚本一键复现 |
| 04X01《scikit-learn 1.9.1 示例源码（examples/）》 → `../practice/scikit-learn_1.9.1_examples_en.tar`、04X02《XGBoost 3.4.2 示例与演示（demo/）》 → `../practice/xgboost_3.4.2_demo_en.tar`、04X03《LightGBM 4.7.0 示例（examples/）》 → `../practice/lightgbm_4.7.0_examples_en.tar`、04X04《CatBoost 官方教程（catboost/tutorials）》 → `../practice/catboost_tutorials_master_en.tar` | AI 编程 阶段 4 | scikit-learn 与梯度提升官方示例 | 改写为严格的 Pipeline + 交叉验证版本，检查无泄漏 |
| 05X52《Neural Networks: Zero to Hero（笔记本与练习）》 → `../practice/karpathy_nn_zero_to_hero_master_en.tar`、05X03《nanoGPT》 → `../practice/karpathy_nanoGPT_master_en.tar` | AI 编程 阶段 5 | 从 makemore 到 GPT；nanoGPT | 在小数据集上复现损失曲线；加入 AMP、检查点续训并验证结果一致 |
| 05X01《PyTorch 官方示例（pytorch/examples）》 → `../practice/pytorch_examples_main_en.tar`、05X10《Transformers v5.22.0 官方示例脚本（examples/）》 → `../practice/hf_transformers_v5.22.0_examples_en.tar`、05X11《Hugging Face 官方笔记本（huggingface/notebooks）》 → `../practice/hf_notebooks_main_examples_en.tar` | AI 编程 阶段 5–6 | PyTorch 与 Hugging Face 官方示例 | 选一个任务替换数据集完成微调，记录实验到 MLflow/W&B |
| 05C04《MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本）》〔部分资料〕 → `../courses/MIT_6S191_Labs_src_en.tar` | AI 编程 阶段 5–6 | MIT 6.S191 实验（PyTorch 与 TF 双版本） | 两种框架分别完成同一实验，比较实现差异 |
| 09X01《RealWorld（Conduit）API 规范与测试》 → `../practice/realworld_spec_main_en.tar` | 应用开发 阶段 3 | RealWorld API 规范 | 用 FastAPI 或 Django 实现，跑通规范自带的 API 测试集 |
| 09X02《Full Stack FastAPI Template（官方全栈模板）》 → `../practice/fastapi_full_stack_template_master_en.tar` | 应用开发 + 部署 | FastAPI 全栈模板 | 阅读后自建同构项目：认证、迁移、测试、Compose、CI |
| 10X02《The Odin Project 课程与项目说明（curriculum）》 → `../practice/theodinproject_curriculum_main_en.tar` | 应用开发 阶段 4 | Odin Project 前端/全栈项目 | 按课程项目说明与评审标准自评 |
| 08X02《DataTalksClub Data Engineering Zoomcamp》 → `../practice/datatalksclub_de_zoomcamp_main_en.tar` | 数据工程 | 容器、编排、数仓、dbt、Spark、Kafka 项目式课程 | 完成课程最终项目，管线可重复运行 |
| 14X04《OpenVINO Notebooks（官方教程笔记本）》 → `../practice/openvino_notebooks_latest_en.tar`、14X02《ONNX Runtime 推理示例（onnxruntime-inference-examples）》 → `../practice/onnxruntime_inference_examples_main_en.tar`、14X05《Triton Inference Server 官方教程（tutorials）》 → `../practice/triton_inference_server_tutorials_main_en.tar` | 部署 阶段 6 | OpenVINO / ONNX Runtime / Triton 推理示例 | 导出自己的模型，比较原框架与推理引擎的输出误差与延迟 |
| 15X51《Anthropic Claude Cookbooks》 → `../practice/anthropic_claude_cookbooks_main_en.tar`、15X52《OpenAI Cookbook》 → `../practice/openai_cookbook_main_en.tar` | 应用开发 阶段 5–6 | 工具调用、RAG、评测示例 | 搭建一个带评测集的 RAG，报告检索召回与答案正确率 |
| 16X01《OWASP Juice Shop（含漏洞的现代 Web 应用靶场）》 → `../practice/owasp_juice_shop_master_en.tar`、16X02《OWASP WebGoat（安全教学应用）》 → `../practice/owasp_webgoat_main_en.tar` | 安全编程 | 漏洞靶场（只读源码与挑战说明） | 在隔离环境中部署后逐项完成挑战，并给出修复补丁 |

## ★★★ 高级

| 项目 | 对应路线/先修 | 内容 | 评价方式 |
|---|---|---|---|
| 11C01《MIT 6.1810 Operating System Engineering (Fall 2025) xv6 教材与实验》 → `../courses/MIT_6.1810_Fall2025_Materials_html_en.tar` 实验 + 11X02《xv6-riscv（MIT 教学操作系统源码）》 → `../practice/mit_xv6_riscv_en.tar` | 系统 阶段 3 | xv6 内核实验 | 课程实验自带 `make grade` 评分脚本（自建环境运行） |
| 11X03《CS:APP 3e 自学实验包（Data/Bomb/Attack/Cache/Shell/Malloc/Proxy Lab 讲义与自学包）》 → `../practice/csapp_3e_selfstudy_labs_en.tar` | 系统 阶段 1 | CS:APP 七个实验 | 各实验自带的评分驱动（driver/autograder） |
| 11X04《Nand2Tetris 软件与项目包》〔部分资料〕 → `../practice/nand2tetris_projects_en` | 系统入门 | 从逻辑门到编译器的 12 个项目 | 官方测试脚本与比较文件 |
| 08X01《CMU BusTub（教学关系数据库系统骨架）》 → `../practice/cmu_bustub_master_en.tar` | 数据库内部 | 缓冲池、B+ 树、执行器、并发控制 | 仓库自带测试；与08C01《CMU 15-445/645 Database Systems (Fall 2025) 课件与讲义》 → `../courses/CMU_15445_Fall2025_Slides_en`项目说明对照 |
| 12X01《perf-ninja（性能优化动手实验）》 → `../practice/dendibakh_perf_ninja_main_en.tar` | 性能 阶段 5 | 逐项性能优化实验 | 每个实验自带基准，达到目标加速比 |
| 13X51《llm.c（纯 C/CUDA 的 GPT-2 训练实现）》 → `../practice/karpathy_llm_c_master_en.tar` | GPU 阶段 6 | 纯 C/CUDA 训练 GPT-2 | 与 PyTorch 参考实现的损失与梯度对齐 |
| 13X52《GPU MODE lectures（讲座笔记本与代码）》 → `../practice/gpu_mode_lectures_main_en.tar`、13X02《Triton v3.9.0 教程源码（python/tutorials）》 → `../practice/triton_lang_v3.9.0_tutorials_en.tar` | GPU 阶段 6 | GPU MODE 讲座代码、Triton 教程 | 自写内核正确性对照 PyTorch，并用 Nsight 报告带宽/算力利用率 |
| 15C03《Stanford CS336 Language Modeling from Scratch (Spring 2025) 讲义与作业》〔部分资料〕 → `../courses/Stanford_CS336_Spring2025_src_en` 作业 | AI + 系统 | 从零实现分词器、Transformer、内核、数据与对齐 | 作业仓库自带测试 |
| 14C01《MIT 6.5840 Distributed Systems (Spring 2026) 讲义与实验》〔部分资料〕 → `../courses/MIT_6.5840_Spring2026_Materials_html_en.tar` 实验说明 | 分布式 阶段 5 | MapReduce、Raft、分片 KV（Go） | 实验自带测试，需反复运行以发现并发缺陷 |
| 14X10《Kubernetes The Hard Way》 → `../practice/kubernetes_the_hard_way_master_en.tar` | 部署 阶段 3 | 手工搭建 Kubernetes 集群 | 完成最终冒烟测试 |
| 07X03《Linux From Scratch 12.x 书籍源（从源码构建 Linux 系统的实践项目）》 → `../practice/lfs_book_trunk_en.tar` | Linux 进阶 | 从源码构建完整 Linux 系统 | 系统可引导，书中各包测试通过 |
| 15X03《SWE-bench（代码智能体评测框架）》 → `../practice/swe_bench_main_en.tar`、15X04《mini-SWE-agent（约百行的参考代码智能体）》 → `../practice/mini_swe_agent_main_en.tar`、15X05《Aider（终端 AI 结对编程工具源码）》 → `../practice/aider_main_en.tar` | 智能体 阶段 6 | SWE-bench 评测框架与代码智能体参考实现 | 在 SWE-bench Lite 子集上测通过率；记录轨迹并做失败分析 |

## 评价方式通用建议

1. **正确性**：优先用项目自带测试。没有测试时先写测试再实现。
2. **可复现**：固定依赖版本与随机种子，一条命令复现结果。
3. **性能**：报告基线、硬件、测量方法与多次运行的统计量。
4. **工程质量**：类型检查、lint、CI 全绿。README 写清运行方式与已知限制。
