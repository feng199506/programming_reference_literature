# 编程基础学习路线：Python、算法、Linux、Git 与测试

适合对象：零基础或只会写零散脚本的学习者。
目标：能独立写出结构清楚、有测试、用 Git 管理的 Python 小项目，并能在 Linux 命令行下完成日常开发与排障。

使用说明：每条资料后的路径相对于本文件（`guides/`）。标"〔部分资料〕"的条目只保存了说明中的范围。"通读"表示按章节顺序学，"查询"表示遇到问题再翻。

---

## 阶段 0：开发环境与命令行（约 1–2 周，可与阶段 1 并行）

先修条件：无。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 07C01《MIT The Missing Semester of Your CS Education（讲义源）》 → `../courses/MIT_MissingSemester_src_en.tar` | 通读前 6 讲：Shell、脚本、编辑器、数据整理、命令行环境、版本控制。每讲做完练习 |
| 2 | 07X01《Software Carpentry: The Unix Shell》 → `../practice/swcarpentry_shell_novice_main_en.tar` | 跟着课堂练习做一遍：导航、管道、循环、脚本 |
| 3 | 07B01《The Linux Command Line (5th Internet Edition)》 → `../books/Shotts_TheLinuxCommandLine_19.01_en.pdf` | 通读第 1–4 部分；第 5 部分（Shell 脚本）在阶段 2 再读 |
| 查询 | 07D01《GNU Bash Reference Manual》 → `../official_docs/gnu_bash_manual_en.pdf`、07D02《GNU Coreutils Manual》 → `../official_docs/gnu_coreutils_manual_en.pdf`、07D04《Linux man-pages 6.20（系统调用与库函数手册源）》 → `../official_docs/linux_man_pages_6.20_en.tar.xz` | Bash 语法、coreutils 选项、系统调用与 man 手册，按需查询 |

检查点：能用 `find`/`grep`/管道完成文件批处理，能写一个带参数和错误退出码的 Bash 脚本。

## 阶段 1：Python 语法与编程思维（约 4–8 周）

先修条件：阶段 0 的命令行基础。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 01C01《MIT 6.100L Introduction to CS and Programming Using Python (Fall 2022) OCW 课程包》 → `../courses/MIT_6.100L_Fall2022_OCW_en.zip` | 主线课程。按讲次学课件，做全部 problem set（OCW 包内含讲义与作业） |
| 2 | 01B01《Think Python: How to Think Like a Computer Scientist (2nd ed.)》 → `../books/Downey_ThinkPython_2ndEd_en.pdf` | 与课程并行通读。重点读函数、递归、类与调试章节 |
| 3 | 01C02《Harvard CS50's Introduction to Programming with Python (CS50P) 讲义与习题》 → `../courses/Harvard_CS50P_NotesProblems_html_en.tar` | 补充练习：异常、单元测试、文件 I/O、正则、库 |
| 4 | 01B05《Composing Programs（UC Berkeley CS 61A 教材）》 → `../books/DeNero_ComposingPrograms_html_en.tar` | 进阶：高阶函数、迭代器与生成器、对象抽象、解释器（CS 61A 教材） |
| 备选 | 01B02《Python for Everybody: Exploring Data in Python 3》 → `../books/Severance_PythonForEverybody_en.pdf`、01C03《University of Helsinki Python Programming MOOC 2024 课程材料（源仓库）》 → `../courses/Helsinki_PythonProgrammingMOOC_2024_src_en.tar` | 入门节奏更慢的替代路线，二选一即可 |
| 查询 | 01D01《Python 3.15 官方文档（教程、语言参考、标准库、C API、打包与扩展）》 → `../official_docs/python_3.15_docs_html_en.tar.bz2` | Python 3.15 官方文档。教程（tutorial/）可通读，标准库与语言参考按需查询 |

检查点：能解释可变/不可变对象、迭代器协议、异常传播。能用类组织一个 300 行左右的程序。

## 阶段 2：Python 工程化：模块、包、依赖与项目组织（约 2–3 周）

先修条件：阶段 1。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 01B06《The Hitchhiker's Guide to Python（项目组织、打包与工具最佳实践）》 → `../books/Reitz_HitchhikersGuideToPython_src_en.tar` | 通读"项目结构、虚拟环境、测试、文档"部分 |
| 2 | 01D03《Python Packaging User Guide（PyPA 官方打包指南）》 → `../official_docs/python_packaging_user_guide_main_src_en.tar` | 打包教程与 pyproject.toml 指南：通读 tutorials 和 guides 中的打包部分 |
| 3 | 01D04《uv 文档（Python 包与项目管理器）》〔部分资料〕 → `../official_docs/uv_0.13.6_docs_src_en.tar` | uv：项目、锁文件、Python 版本管理。按"入门 → 概念 → 指南"顺序读 |
| 查询 | 01D02《pip 用户指南与参考》 → `../official_docs/pip_26.2.2_docs_src_en.tar` | pip 用户指南与 CLI 参考 |
| 4 | 01B04《Beyond the Basic Stuff with Python》 → `../books/Sweigart_BeyondTheBasicStuff_html_en.tar` | 代码风格、命名、Git 与项目组织习惯 |
| 5 | 06D05《Python 类型系统规范与指南（typing.python.org 源）》 → `../official_docs/python_typing_docs_main_src_en.tar` | 类型标注：先读 guides，规范（spec）按需查询 |

检查点：用 `src/` 布局建一个可安装的包，依赖锁定，可在新虚拟环境中一键复现。

## 阶段 3：数据结构与算法（约 8–12 周，可与阶段 4 部分并行）

先修条件：Python 基础、离散数学入门（不熟悉可边学边查02B05《Mathematics for Computer Science》 → `../books/Lehman_MathematicsForComputerScience_2017_en.pdf`）。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 02C01《MIT 6.006 Introduction to Algorithms (Spring 2020) OCW 课程包》 → `../courses/MIT_6.006_Spring2020_OCW_en.zip` | 主线课程：讲义 + 习题 + 解答 |
| 2 | 02B02《Open Data Structures (Python edition)》 → `../books/Morin_OpenDataStructures_Python_en.pdf` | 用 Python 实现各数据结构的参考书，与课程同步读 |
| 3 | 02B01《Algorithms》 → `../books/Erickson_Algorithms_1stEd_en.pdf` | 递归、回溯、DP、图算法的深入教材，配合习题 |
| 4 | 02C02《MIT 6.046J Design and Analysis of Algorithms (Spring 2015) OCW 课程包》 → `../courses/MIT_6.046J_Spring2015_OCW_en.zip` | 进阶：随机算法、摊还分析、网络流 |
| 练习 | 02B03《Competitive Programmer's Handbook》 → `../books/Laaksonen_CompetitiveProgrammersHandbook_en.pdf`、02X01《TheAlgorithms/Python（算法参考实现集）》 → `../practice/TheAlgorithms_Python_master_en.tar` | 竞赛式实现训练；参考实现按需查阅，**先自己写再对照** |
| 查询 | 02B04《Data Structures and Algorithm Analysis (C++ Edition, 3.2)》 → `../books/Shaffer_DataStructuresAlgorithmAnalysis_Cpp_3.2_en.pdf`、02C03《Princeton COS 226 Algorithms and Data Structures (Spring 2025) 课件》〔部分资料〕 → `../courses/Princeton_COS226_Spring2025_Slides_en` | 第二视角的教材与课件 |

检查点：能手写哈希表、堆、平衡树（至少一种）。能分析 DP 与图算法的复杂度。

## 阶段 4：Git 与协作（约 1–2 周）

先修条件：阶段 0。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 07X02《Software Carpentry: Version Control with Git》 → `../practice/swcarpentry_git_novice_main_en.tar` | 课堂练习：提交、历史、远程、冲突 |
| 2 | 07B02《Pro Git (2nd ed.)》 → `../books/Chacon_ProGit_2ndEd_2.1.450_en.pdf` | 通读第 1–3、5、7 章；第 10 章（Git 内部原理）用于故障恢复 |
| 查询 | 07D03《Git 官方参考文档 HTML 包（git-htmldocs 2.56.0）》 → `../official_docs/git_htmldocs_2.56.0_en.tar.xz` | 命令手册页，含 gitworkflows、gitglossary |
| 5 | 06B05《Producing Open Source Software (2nd ed.)》 → `../books/Fogel_ProducingOpenSourceSoftware_2ndEd_en.pdf` | 开源协作流程与沟通（按需读） |

检查点：熟练使用分支、rebase、cherry-pick、bisect，能用 reflog 恢复误操作。

## 阶段 5：测试与代码质量（约 2–3 周）

先修条件：阶段 1–2。

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 06D01《pytest 稳定版文档（Read the Docs HTML 包）》 → `../official_docs/pytest_stable_docs_html_en.zip` | pytest：入门 → how-to（fixture、参数化、临时目录、monkeypatch） |
| 2 | 06B03《Test-Driven Development with Python (3rd ed., online)》 → `../books/Percival_TDDWithPython_3rdEd_html_en.tar` | TDD 全流程：功能测试、单元测试、重构 |
| 3 | 06X02《Software Carpentry: Programming with Python（含防御式编程与测试）》 → `../practice/swcarpentry_python_novice_inflammation_main_en.tar` | 防御式编程、断言、调试、测试的课堂练习 |
| 4 | 06D02《mypy 稳定版文档（Read the Docs HTML 包）》 → `../official_docs/mypy_stable_docs_html_en.zip`、06D03《Pyright 1.1.414 文档（docs/）》 → `../official_docs/pyright_1.1.414_docs_src_en.tar`、06D04《Ruff 0.17.3 文档（docs/）》〔部分资料〕 → `../official_docs/ruff_0.17.3_docs_src_en.tar` | 类型检查（mypy、Pyright）与 lint/格式化（Ruff）配置 |
| 5 | 06X03《Hypermodern Python Cookiecutter（打包、类型检查、测试与 CI 模板）》 → `../practice/cjolowicz_cookiecutter_hypermodern_python_main_en.tar` | 把 pytest、mypy、Ruff、pre-commit、CI 组合成模板，对照自己的项目 |
| 6 | 06C02《CMU 17-313 Foundations of Software Engineering（课件、作业与讲习）》 → `../courses/CMU_17313_FoundationsSE_src_en.tar` | CMU 17-313：测试与 CI、代码评审、开源协作、DevOps 的课件与作业（进阶） |

检查点：项目有单元测试与覆盖率报告，类型检查与 lint 无报错，提交前自动运行检查。

---

## 资料使用方式速览

- **通读**：01C01《MIT 6.100L Introduction to CS and Programming Using Python (Fall 2022) OCW 课程包》 → `../courses/MIT_6.100L_Fall2022_OCW_en.zip`、01B01《Think Python: How to Think Like a Computer Scientist (2nd ed.)》 → `../books/Downey_ThinkPython_2ndEd_en.pdf`、02C01《MIT 6.006 Introduction to Algorithms (Spring 2020) OCW 课程包》 → `../courses/MIT_6.006_Spring2020_OCW_en.zip`、02B01《Algorithms》 → `../books/Erickson_Algorithms_1stEd_en.pdf`、07C01《MIT The Missing Semester of Your CS Education（讲义源）》 → `../courses/MIT_MissingSemester_src_en.tar`、07B02《Pro Git (2nd ed.)》 → `../books/Chacon_ProGit_2ndEd_2.1.450_en.pdf`、06B03《Test-Driven Development with Python (3rd ed., online)》 → `../books/Percival_TDDWithPython_3rdEd_html_en.tar`
- **按需查询**：01D01《Python 3.15 官方文档（教程、语言参考、标准库、C API、打包与扩展）》 → `../official_docs/python_3.15_docs_html_en.tar.bz2`、07D01《GNU Bash Reference Manual》 → `../official_docs/gnu_bash_manual_en.pdf`、07D03《Git 官方参考文档 HTML 包（git-htmldocs 2.56.0）》 → `../official_docs/git_htmldocs_2.56.0_en.tar.xz`、07D04《Linux man-pages 6.20（系统调用与库函数手册源）》 → `../official_docs/linux_man_pages_6.20_en.tar.xz`、02X01《TheAlgorithms/Python（算法参考实现集）》 → `../practice/TheAlgorithms_Python_master_en.tar`、02B05《Mathematics for Computer Science》 → `../books/Lehman_MathematicsForComputerScience_2017_en.pdf`
- **衔接下一路线**：完成阶段 1–5 后，进入 `ai_programming_path_cn.md`（科学计算与 ML），或 `application_path_cn.md`（Web 与应用）。
