# AI 编程学习路线：科学计算、机器学习、深度学习与实验管理

适合对象：已完成 `beginner_path_cn.md` 阶段 1–2（Python 基础与工程化），并具备线性代数、概率统计入门知识的学习者。
目标：能写出无数据泄漏的机器学习训练管线，能用 PyTorch 从张量写到分布式训练与混合精度，并能管理实验、数据版本与检查点。

工具版本均为 2026-10-29 时点的官方当前版本，详见 `../tools/tools_catalog_cn.csv`。

---

## 阶段 1：数组计算与向量化（约 3–4 周）

先修条件：Python 基础、线性代数入门。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 03B01《Python Data Science Handbook（笔记本全文）》 → `../books/VanderPlas_PythonDataScienceHandbook_notebooks_en.tar` | 通读 IPython、NumPy、pandas、Matplotlib 部分（笔记本形式，边读边运行**自己的**环境） |
| 2 | 03D01《NumPy 2.5 官方文档（用户指南、API 参考、构建与 C API）》 → `../official_docs/numpy_2.5_docs_html_en.tar` | NumPy 2.5：先读 user/absolute_beginners、广播、索引、ufunc；API 参考按需查询 |
| 3 | 03D10《Scientific Python Lectures（社区系统教程）》 → `../official_docs/scientific_python_lectures_main_src_en.tar` | 系统教程：NumPy 进阶、SciPy、优化技巧 |
| 4 | 03X03《From Python to Numpy（向量化专题书与示例）》 → `../practice/rougier_from_python_to_numpy_master_en.tar` | 向量化思维专题：从循环到数组表达式 |
| 练习 | 03X51《100 NumPy exercises》 → `../practice/rougier_numpy_100_master_en.tar`、03X01《NumPy 官方教程笔记本（numpy-tutorials）》 → `../practice/numpy_tutorials_main_en.tar` | 100 道向量化练习；NumPy 官方教程笔记本 |

检查点：能消除 Python 循环，理解视图与副本、广播规则和 dtype 溢出。

## 阶段 2：数值稳定性与科学计算（约 2–3 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 03B03《Python Programming and Numerical Methods: A Guide for Engineers and Scientists》 → `../books/Kong_PythonProgrammingNumericalMethods_html_en.tar` | 浮点误差、截断误差、线性方程组、插值、数值积分与 ODE（Berkeley 教材） |
| 2 | 03D02《SciPy 1.18 官方文档》 → `../official_docs/scipy_1.18.0_docs_html_en.zip` | SciPy 1.18：linalg、optimize、integrate、sparse、stats 的用户指南 |
| 查询 | 02B05《Mathematics for Computer Science》 → `../books/Lehman_MathematicsForComputerScience_2017_en.pdf` | 概率与离散数学基础 |

检查点：能解释 log-sum-exp、条件数和灾难性抵消，会选用合适的 SciPy 求解器。

## 阶段 3：表格数据、可视化与数据格式（约 3–4 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 03B02《Python for Data Analysis (3rd ed., Open Access 网页版)》 → `../books/McKinney_PythonForDataAnalysis_3rdEd_html_en.tar` | pandas 作者的教程：清洗、分组、时间序列 |
| 2 | 03D03《pandas 官方文档（HTML 压缩包）》 → `../official_docs/pandas_stable_docs_html_en.zip` | pandas 官方文档：用户指南（索引、合并、分组、窗口、I/O、写时复制）按需查询 |
| 3 | 03C02《UC Berkeley Data 8 教材 Computational and Inferential Thinking》 → `../courses/Berkeley_Data8_Textbook_src_en.tar`、03C01《UC Berkeley Data 100 Principles and Techniques of Data Science 课程讲义》 → `../courses/Berkeley_Data100_CourseNotes_src_en.tar` | Berkeley Data 8 → Data 100：从表格计算到数据清洗、SQL、建模 |
| 4 | 03B05《Fundamentals of Data Visualization》 → `../books/Wilke_FundamentalsOfDataVisualization_html_en.tar` | 可视化原则（与工具无关） |
| 5 | 03D04《Matplotlib 3.11.2 官方文档（教程、用户指南、示例图库、API）》 → `../official_docs/matplotlib_3.11.2_docs_html_en.tar` | Matplotlib 3.11 文档与示例图库（出版级可视化教材 Rougier 版因 HAL 访问验证未获取） |
| 6 | 03D11《Apache Parquet 格式规范》 → `../official_docs/apache_parquet_format_master_en.tar` | Parquet 格式规范：列式存储、编码与压缩 |
| 7 | 03D05《JupyterLab 4.6 官方文档》〔部分资料〕 → `../official_docs/jupyterlab_4.6.5_docs_src_en.tar`、03D06《Project Jupyter 总体文档（docs.jupyter.org）》 → `../official_docs/jupyter_docs_main_src_en.tar` | Jupyter / JupyterLab 使用与配置 |
| 练习 | 03X02《pandas_exercises》 → `../practice/guipsamora_pandas_exercises_master_en.tar` | pandas 分主题练习 |

检查点：能写出可复现的数据清洗脚本（而非只在笔记本里），能为数据选择合适的存储格式。

## 阶段 4：机器学习编程（约 6–8 周）

先修条件：阶段 1–3，概率统计。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 04C04《Inria scikit-learn MOOC: Machine learning in Python with scikit-learn》 → `../courses/Inria_scikit-learn_MOOC_src_en.tar` | Inria scikit-learn MOOC：预处理管线、交叉验证、超参搜索、评估，**含数据泄漏专题** |
| 2 | 04B01《An Introduction to Statistical Learning with Applications in Python》 → `../books/James_IntroductionStatisticalLearningPython_1stEd_en.pdf` | ISLP：重抽样、模型选择、树模型；每章 Python 实验 |
| 3 | 04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar` | scikit-learn 1.9：用户指南的 Pipeline/ColumnTransformer、模型选择与评估、常见陷阱（common pitfalls）、模型持久化 |
| 4 | 04C01《MIT 6.390 Introduction to Machine Learning 讲义》 → `../courses/MIT_6390_LectureNotes_html_en.tar` | MIT 6.390 讲义：特征表示、正则化、神经网络入门 |
| 5 | 04B03《Patterns, Predictions, and Actions: Foundations of Machine Learning》 → `../books/Hardt_PatternsPredictionsActions_2022_en.pdf` | 数据集、基准与留出法的局限：理解评测偏差和泄漏 |
| 6 | 04D02《XGBoost 稳定版文档（PDF）》 → `../official_docs/xgboost_stable_docs_en.pdf`、04D03《LightGBM 稳定版文档（PDF）》 → `../official_docs/lightgbm_stable_docs_en.pdf`、04D04《CatBoost 1.2.10 官方文档源（英文）》 → `../official_docs/catboost_1.2.10_docs_src_en.tar` | 梯度提升三件套：XGBoost、LightGBM、CatBoost 的参数、类别特征、GPU、模型导出 |
| 示例 | 04X01《scikit-learn 1.9.1 示例源码（examples/）》 → `../practice/scikit-learn_1.9.1_examples_en.tar`、04X02《XGBoost 3.4.2 示例与演示（demo/）》 → `../practice/xgboost_3.4.2_demo_en.tar`、04X03《LightGBM 4.7.0 示例（examples/）》 → `../practice/lightgbm_4.7.0_examples_en.tar`、04X04《CatBoost 官方教程（catboost/tutorials）》 → `../practice/catboost_tutorials_master_en.tar` | 官方示例源码，学完一节就对照一个示例 |
| 查询 | 04B02《Data Science and Machine Learning: Mathematical and Statistical Methods》 → `../books/Kroese_DataScienceAndMachineLearning_2019_en.pdf` | 数学推导与 Python 代码并行的参考书 |

**数据切分与泄漏防范清单**（依据04C04《Inria scikit-learn MOOC: Machine learning in Python with scikit-learn》 → `../courses/Inria_scikit-learn_MOOC_src_en.tar`04D01《scikit-learn 1.9 官方文档（用户指南、API、示例图库）》 → `../official_docs/scikit-learn_1.9_docs_html_en.tar`04B03《Patterns, Predictions, and Actions: Foundations of Machine Learning》 → `../books/Hardt_PatternsPredictionsActions_2022_en.pdf`）：

1. 先切分再拟合预处理器，预处理放入 Pipeline，在交叉验证内部拟合。
2. 时间序列用时间顺序切分，不打乱。分组数据用 GroupKFold。
3. 超参数搜索用嵌套交叉验证，或保留独立测试集。测试集只用一次。
4. 特征工程中的目标编码、缺失值填补、标准化都属于"拟合"，必须在训练折内完成。

## 阶段 5：深度学习编程（约 8–10 周）

先修条件：阶段 4，微积分、线性代数。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 05X51《micrograd（最小自动微分引擎）》 → `../practice/karpathy_micrograd_master_en.tar` | 先手写一个标量自动微分引擎，理解反向传播 |
| 2 | 05B01《Dive into Deep Learning》 → `../books/Zhang_DiveIntoDeepLearning_2023_en.pdf` | 主教材（PyTorch 版）：张量 → 自动微分 → MLP/CNN/RNN/Transformer → 优化 → 计算性能 |
| 3 | 05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar` | PyTorch 官方教程：Learn the Basics → 自定义 Dataset/DataLoader → 保存加载 → 混合精度（AMP）→ 分布式入门 |
| 4 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar` | PyTorch 2.15 文档：nn、optim、autograd、amp、checkpoint、torch.compile 页按需查询 |
| 5 | 05C01《Stanford CS231n Deep Learning for Computer Vision 课程讲义》 → `../courses/Stanford_CS231n_Online_LectureNotes_en`、05C03《University of Amsterdam Deep Learning Course 教程笔记本（UvA DL Notebooks）》 → `../courses/UvA_DL_Notebooks_src_en.tar` | Stanford CS231n 讲义；UvA DL 教程笔记本（PyTorch/JAX，含多 GPU） |
| 6 | 05X52《Neural Networks: Zero to Hero（笔记本与练习）》 → `../practice/karpathy_nn_zero_to_hero_master_en.tar`、05X03《nanoGPT》 → `../practice/karpathy_nanoGPT_master_en.tar` | 从 makemore 到 GPT；nanoGPT 训练循环、AMP、DDP、检查点 |
| 7 | 05B02《Understanding Deep Learning》 → `../books/Prince_UnderstandingDeepLearning_2023_en.pdf`、05B03《The Little Book of Deep Learning》 → `../books/Fleuret_LittleBookOfDeepLearning_2023_en.pdf` | 原理补充与速查 |
| 8 | 05C02《CMU 10-414/714 Deep Learning Systems: Algorithms and Implementation 课件与作业》〔部分资料〕 → `../courses/CMU_10714_DLSys_Lectures_en` | 进阶：自己实现深度学习框架（自动微分、GPU 后端） |
| 9 | 05C04《MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本）》〔部分资料〕 → `../courses/MIT_6S191_Labs_src_en.tar` | MIT 6.S191 实验：PyTorch 与 TensorFlow 双版本对照 |

**训练循环调试清单**（依据05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar`05B04《Machine Learning Engineering Open Book》 → `../books/Bekman_MachineLearningEngineeringOpenBook_src_en.tar`05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar`）：

1. 先在一个 batch 上过拟合，确认损失能降到接近 0。
2. 检查数据管线：打印样本与标签，确认归一化和数据增强正确。
3. 用 `torch.autograd.detect_anomaly` 与梯度范数监控定位 NaN 和梯度爆炸。
4. 混合精度用 autocast + GradScaler（fp16）或 bf16。检查点同时保存模型、优化器、调度器、随机数状态与 step。

## 阶段 6：其他框架与生态（按需选学）

| 方向 | 资料 |
|---|---|
| TensorFlow / Keras | 05D05《TensorFlow 官方指南与教程源（tensorflow/docs site/en）》 → `../official_docs/tensorflow_docs_guides_master_src_en.tar`（指南与教程）、05D06《TensorFlow Python API 参考（tensorflow.org/api_docs/python 离线镜像）》〔部分资料〕 → `../official_docs/tensorflow_api_docs_python_mirror_en.tar.gz`〔部分资料〕（API）、05D07《Keras 3 官方指南与示例源（keras-io）》 → `../official_docs/keras_io_master_src_en.tar`（Keras 3 指南与示例）、05D08《Keras 3 API 参考（keras.io/api 离线镜像）》 → `../official_docs/keras_api_reference_mirror_en.tar`（Keras API） |
| JAX | 05D09《JAX 官方文档（Read the Docs HTML 包）》 → `../official_docs/jax_latest_docs_html_en.zip` |
| 计算机视觉 | 05D10《OpenCV 5.0.0 官方文档（Doxygen HTML 包，含 Python 教程）》 → `../official_docs/opencv_5.0.0_docs_html_en.zip`（OpenCV 5.0）、05X02《OpenCV 5.0.0 示例（samples/）》 → `../practice/opencv_5.0.0_samples_en.tar`、05D03《torchvision 0.29 官方文档》 → `../official_docs/torchvision_0.29_docs_html_en.tar`（torchvision）、05D11《Pillow 稳定版文档（PDF）》 → `../official_docs/pillow_stable_docs_en.pdf`（Pillow）、05D12《Albumentations 2.0.8 文档源与 README（原项目，已转维护）》〔部分资料〕 → `../official_docs/albumentations_2.0.8_docs_src_en.tar`05D13《AlbumentationsX 2.5.1 源码仓库（含 README 与示例）》〔部分资料〕 → `../practice/albumentationsx_2.5.1_src_en.tar`（Albumentations / X） |
| 音频 | 05D04《torchaudio 2.11 官方文档》 → `../official_docs/torchaudio_2.11_docs_html_en.tar`（torchaudio，注意维护期说明） |
| Hugging Face | 05C50《Hugging Face LLM Course（构建版，含 Transformers/Datasets/Tokenizers/微调/推理）》 → `../courses/hf_llm_course_main_built_en.zip`（LLM 课程，建议通读）→05D20《Hugging Face Transformers 文档（含 API、导出与推理部署） v5.21.1》 → `../official_docs/hf_transformers_v5.21.1_docs_built_en.zip`→05D21《Hugging Face Datasets 文档 v5.1.0》 → `../official_docs/hf_datasets_v5.1.0_docs_built_en.zip`05D22《Hugging Face Tokenizers 文档 v0.23.3》 → `../official_docs/hf_tokenizers_v0.23.3_docs_built_en.zip`→05D23《Hugging Face Accelerate 文档（分布式、FSDP/DeepSpeed 集成、调试） v1.15.0》 → `../official_docs/hf_accelerate_v1.15.0_docs_built_en.zip`→05D24《Hugging Face PEFT 文档（LoRA 等参数高效微调） v0.21.0》 → `../official_docs/hf_peft_v0.21.0_docs_built_en.zip`05D25《Hugging Face TRL 文档（SFT/DPO/GRPO 等训练器） v1.17.0》 → `../official_docs/hf_trl_v1.17.0_docs_built_en.zip`→05D26《Hugging Face Diffusers 文档 v0.42.1》 → `../official_docs/hf_diffusers_v0.42.1_docs_built_en.zip`；示例05X10《Transformers v5.22.0 官方示例脚本（examples/）》 → `../practice/hf_transformers_v5.22.0_examples_en.tar`05X11《Hugging Face 官方笔记本（huggingface/notebooks）》 → `../practice/hf_notebooks_main_examples_en.tar` |

## 阶段 7：实验管理、数据版本与分布式训练入门（约 3–4 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 04D08《TensorBoard 2.21.0 官方指南（docs/）》 → `../official_docs/tensorboard_2.21.0_docs_src_en.tar` | TensorBoard：标量、超参、性能剖析 |
| 2 | 04D05《MLflow 3.17.2 文档源（Docusaurus）》〔部分资料〕 → `../official_docs/mlflow_3.17.2_docs_src_en.tar`、04X05《MLflow 3.17.2 示例（examples/）》 → `../practice/mlflow_3.17.2_examples_en.tar` | MLflow：追踪、模型注册、模型格式与部署 |
| 3 | 04D06《DVC 官方文档源（dvc.org 仓库 content/docs）》 → `../official_docs/dvc_docs_main_src_en.tar` | DVC：数据与管线版本化 |
| 4 | 04D07《W&B 官方文档源（wandb/docs）》 → `../official_docs/wandb_docs_main_src_en.tar`、04X07《W&B 官方示例（wandb/examples）》 → `../practice/wandb_examples_master_en.tar` | Weights & Biases 文档与示例（注意其已归入 CoreWeave，文档站域名有变化） |
| 5 | 04X51《Made With ML（MLOps 端到端课程项目）》 → `../practice/madewithml_main_en.tar`、04X52《Cookiecutter Data Science（项目结构模板 v2）》 → `../practice/cookiecutter_data_science_master_en.tar` | MLOps 端到端项目与项目结构模板 |
| 6 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar` + 05X01《PyTorch 官方示例（pytorch/examples）》 → `../practice/pytorch_examples_main_en.tar` | torch.distributed：DDP → FSDP2（fully_shard）→ torchrun；examples/distributed |
| 7 | 05D23《Hugging Face Accelerate 文档（分布式、FSDP/DeepSpeed 集成、调试） v1.15.0》 → `../official_docs/hf_accelerate_v1.15.0_docs_built_en.zip`、13D04《DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源）》〔部分资料〕 → `../official_docs/deepspeed_0.19.8_docs_src_en.tar`、13D06《NCCL 用户指南（离线镜像）》 → `../official_docs/nccl_user_guide_mirror_en.tar` | Accelerate、DeepSpeed、NCCL：多卡训练的常用官方工具 |
| 8 | 05B04《Machine Learning Engineering Open Book》 → `../books/Bekman_MachineLearningEngineeringOpenBook_src_en.tar` | 大规模训练的调试、检查点与故障排查手册（按需查询） |

衔接：模型导出与推理部署见 `../tools/interoperability_guide_cn.md` 与 `deployment_path_cn.md`。GPU 内核与性能优化见 `systems_performance_path_cn.md`。
