"""Generate scripts/seeds/C_core_en.json: textbooks, university courses, non-tool official docs/specs and
practice projects for the 16 categories.  Sources probed 2026-10-29 (see search_log_cn.md).

Rules applied: only legally open full texts (author/publisher/university hosted); online-only books are mirrored
for offline reading and labelled with their licence; course packs must include the actual notes/slides/labs
(syllabus or video links alone are never seeded); repos without a licence are not saved.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "seeds" / "C_core_en.json"
S = []
MLDL = "/root/machine_learning_deep_learning_literature/"


def add(id, cat, type, title, authors, year, version, out, get, license, goal, level="入门", prereq="", stack="",
        expect=None, cross=(), school="", material="", use="通读", order=50, note="", complete="完整", scope="",
        reuse=None, lang="en"):
    S.append(dict(id=id, cat=cat, cross=list(cross), type=type, title=title, authors=authors, school=school, year=year,
                  version=version, lang=lang, level=level, prereq=prereq, stack=stack,
                  source=(get or {}).get("repo") or (get or {}).get("start") or ((get or {}).get("urls") or [""])[0]
                  if get else (reuse or {}).get("source", ""),
                  license=license, goal=goal, order=order, out=out, get=get or {"kind": "reuse"}, expect=expect or {},
                  material=material or {"book": "教材/参考书", "course": "课程资料", "docs": "官方文档",
                                        "practice": "实践项目", "paper": "论文"}[type],
                  use=use, note=note, complete=complete, scope=scope, **({"reuse": reuse} if reuse else {})))


def pdf(*urls, **kw):
    return {"kind": "pdf", "urls": list(urls), **kw}


def git(repo, ref=None, paths=None, host="https://github.com/"):
    g = {"kind": "git", "repo": host + repo if not repo.startswith(("http", "git:")) else repo}
    if ref:
        g["ref"] = ref
    if paths:
        g["paths"] = paths
    return g


def mirror(start, include=None, quota=300, level="inf", domains=None, reject_regex=None, wait=0.4, exclude=None,
           no_parent=True):
    g = {"kind": "mirror", "start": start, "quota_mb": quota, "level": level, "wait": wait, "no_parent": no_parent}
    if include:
        g["include"] = include
    if domains:
        g["domains"] = domains
        g["span"] = True
    if reject_regex:
        g["reject_regex"] = reject_regex
    if exclude:
        g["exclude"] = exclude
    return g


def file(*urls, max_mb=800):
    return {"kind": "file", "urls": list(urls), "max_mb": max_mb}


def pdfset(urls=None, index=None, pattern=None, min_files=1):
    g = {"kind": "pdfset", "min_files": min_files}
    if urls:
        g["urls"] = urls
    if index:
        g["index"], g["pattern"] = index, pattern
    return g


def reuse(path, src):
    return {"path": path, "source": src}


B, C, D, X = "books/", "courses/", "official_docs/", "practice/"
NCSA, NCND, CCBY, CCBYSA = "CC BY-NC-SA", "CC BY-NC-ND", "CC BY", "CC BY-SA"
FREE = "免费在线阅读（版权保留，个人离线保存）"

# ============================================================== 01 Python
add("01B01", "01", "book", "Think Python: How to Think Like a Computer Scientist (2nd ed.)", "Allen B. Downey", "2015", "2nd ed. 2.4.0",
    B + "Downey_ThinkPython_2ndEd_en.pdf", pdf("https://greenteapress.com/thinkpython2/thinkpython2.pdf"), "CC BY-NC 3.0",
    "Python 语法、函数、递归、对象、类与调试习惯", prereq="无", stack="Python 3", order=1,
    expect={"title_words": ["Think", "Python"], "min_pages": 200}, note="经典第 2 版；第 3 版（2024）仅以笔记本形式开放，未重复收录")
add("01B02", "01", "book", "Python for Everybody: Exploring Data in Python 3", "Charles R. Severance", "2016", "PDF 当前版",
    B + "Severance_PythonForEverybody_en.pdf", pdf("https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"), NCSA,
    "零基础 Python、文件、正则、网络、数据库与数据可视化入门", prereq="无", stack="Python 3", order=2,
    expect={"title_words": ["Python", "Everybody"], "min_pages": 200})
add("01B03", "01", "book", "Automate the Boring Stuff with Python (3rd ed., online)", "Al Sweigart", "2025", "3rd ed. online",
    B + "Sweigart_AutomateTheBoringStuff_3rdEd_html_en.tar",
    mirror("https://automatetheboringstuff.com/3e/", include=["/3e"], quota=200), NCSA,
    "以自动化脚本练习 Python：文件、正则、表格、PDF、网页抓取", prereq="无", stack="Python 3", order=3,
    expect={"min_docs": 20, "entry": "3e/index.html"})
add("01B04", "01", "book", "Beyond the Basic Stuff with Python", "Al Sweigart", "2020", "online",
    B + "Sweigart_BeyondTheBasicStuff_html_en.tar", mirror("https://inventwithpython.com/beyond/", include=["/beyond"], quota=100),
    NCSA, "代码风格、调试、命名、OOP、项目组织与 Git 的进阶习惯", level="进阶", prereq="Python 基础", stack="Python 3",
    order=4, expect={"min_docs": 15})
add("01B05", "01", "book", "Composing Programs（UC Berkeley CS 61A 教材）", "John DeNero（基于 SICP）", "2024", "online",
    B + "DeNero_ComposingPrograms_html_en.tar", mirror("https://www.composingprograms.com/", quota=100,
                                                       domains=["www.composingprograms.com", "composingprograms.com"]),
    CCBYSA, "函数抽象、高阶函数、迭代器/生成器、对象、解释器", level="入门-进阶", prereq="无", stack="Python 3",
    school="UC Berkeley", order=5, expect={"min_docs": 20}, cross=["02"])
add("01B06", "01", "book", "The Hitchhiker's Guide to Python（项目组织、打包与工具最佳实践）", "Kenneth Reitz, Tanya Schlusser 等",
    "2024", "master 提交", B + "Reitz_HitchhikersGuideToPython_src_en.tar", git("realpython/python-guide", None, ["docs"]),
    NCSA, "项目结构、虚拟环境、测试、文档、打包与常见库选择", level="进阶", prereq="Python 基础", stack="Python 3", order=6,
    use="按需查询", expect={"min_docs": 30}, cross=["06"])
add("01C01", "01", "course", "MIT 6.100L Introduction to CS and Programming Using Python (Fall 2022) OCW 课程包", "Ana Bell",
    "2022", "Fall 2022", C + "MIT_6.100L_Fall2022_OCW_en.zip",
    file("https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/6.100l-fall-2022.zip"),
    "CC BY-NC-SA 4.0", "Python 编程与计算思维完整课程：讲义、课件、作业与解答", school="MIT", prereq="无", stack="Python 3",
    material="课件+讲义+作业（OCW 静态站点包，不含视频文件）", order=10, expect={"min_docs": 20})
add("01C02", "01", "course", "Harvard CS50's Introduction to Programming with Python (CS50P) 讲义与习题", "David J. Malan",
    "2026", "当前版（/python/，2022 版 URL 已重定向至此，页面年份为准）", C + "Harvard_CS50P_NotesProblems_html_en.tar",
    mirror("https://cs50.harvard.edu/python/", include=["/python"], quota=150), "CC BY-NC-SA 4.0",
    "函数、条件、循环、异常、库、单元测试、文件 I/O、正则、OOP", school="Harvard", prereq="无", stack="Python 3",
    material="讲义（notes）+ 习题集（problems）；视频仅为链接未下载", order=11, expect={"min_docs": 30})
add("01C03", "01", "course", "University of Helsinki Python Programming MOOC 2024 课程材料（源仓库）", "University of Helsinki MOOC Center",
    "2024", "programming-24 main 提交", C + "Helsinki_PythonProgrammingMOOC_2024_src_en.tar",
    git("rage/programming-24", None, ["data"]), "CC BY-NC-SA 4.0", "14 个部分的入门到进阶 Python 课程正文与练习说明",
    school="University of Helsinki", prereq="无", stack="Python 3", material="课程正文（Markdown）+ 练习说明", order=12,
    expect={"min_docs": 50, "need_license": False}, note="仓库无 LICENSE 文件；许可依据 mooc.fi 课程站声明")
add("01X01", "01", "practice", "pytudes（Peter Norvig 的 Python 练习与编程问题集）", "Peter Norvig", "2025", "main 提交",
    X + "norvig_pytudes_main_en.tar", git("norvig/pytudes"), "MIT", "用简洁 Python 解决谜题与算法问题，学习惯用法",
    level="进阶", prereq="Python 基础", stack="Python 3", order=20, expect={"min_docs": 20}, cross=["02"])
add("01X02", "01", "practice", "Exercism Python track（练习题、测试与说明）", "Exercism", "2025", "main 提交",
    X + "exercism_python_main_en.tar", git("exercism/python", None, ["exercises", "concepts", "reference", "docs"]), "MIT",
    "按概念递进的 Python 练习，每题附测试", prereq="无", stack="Python 3", order=21, expect={"min_docs": 100})

# ============================================================== 02 DSA
add("02B01", "02", "book", "Algorithms", "Jeff Erickson", "2019", "1st ed. (June 2019)", B + "Erickson_Algorithms_1stEd_en.pdf",
    pdf("https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf"), "CC BY 4.0",
    "递归、回溯、动态规划、贪心、图算法、NP 难度；配套随机算法讲义", level="进阶", prereq="离散数学、一门编程语言",
    school="UIUC", order=1, expect={"title_words": ["Algorithms", "Erickson"], "min_pages": 400})
add("02B02", "02", "book", "Open Data Structures (Python edition)", "Pat Morin", "2013", "0.1Gβ", B + "Morin_OpenDataStructures_Python_en.pdf",
    pdf("https://opendatastructures.org/ods-python.pdf"), "CC BY 2.5", "数组、链表、跳表、哈希、二叉树、堆、图的实现与分析",
    prereq="Python 基础", stack="Python", order=2, expect={"title_words": ["Open", "Data", "Structures"], "min_pages": 200})
add("02B03", "02", "book", "Competitive Programmer's Handbook", "Antti Laaksonen", "2018", "July 2018", B + "Laaksonen_CompetitiveProgrammersHandbook_en.pdf",
    pdf("https://cses.fi/book/book.pdf"), "CC BY-NC-SA 4.0", "竞赛式算法实现：排序、搜索、DP、图、树查询、数论", level="进阶",
    prereq="C++ 或 Python", stack="C++", order=3, expect={"title_words": ["Competitive", "Programmer", "Handbook"], "min_pages": 250})
add("02B04", "02", "book", "Data Structures and Algorithm Analysis (C++ Edition, 3.2)", "Clifford A. Shaffer", "2012", "Edition 3.2",
    B + "Shaffer_DataStructuresAlgorithmAnalysis_Cpp_3.2_en.pdf", pdf("https://people.cs.vt.edu/shaffer/Book/C++3e20120605.pdf"),
    "作者免费分发（版权保留）", "复杂度分析、线性结构、树、排序、文件处理、索引、图", prereq="C++ 基础", stack="C++", school="Virginia Tech",
    order=4, expect={"title_words": ["Data", "Structures", "Algorithm", "Analysis"], "min_pages": 500})
add("02B05", "02", "book", "Mathematics for Computer Science", "Eric Lehman, F. Thomson Leighton, Albert R. Meyer", "2017", "2017 revision",
    B + "Lehman_MathematicsForComputerScience_2017_en.pdf", pdf("https://courses.csail.mit.edu/6.042/spring18/mcs.pdf"),
    "CC BY-SA 3.0", "证明、归纳、图论、计数、离散概率（随机算法分析基础）", prereq="高中数学", school="MIT", order=5, use="按需查询",
    expect={"title_words": ["Mathematics", "Computer", "Science"], "min_pages": 900})
add("02C01", "02", "course", "MIT 6.006 Introduction to Algorithms (Spring 2020) OCW 课程包", "Erik Demaine, Jason Ku, Justin Solomon",
    "2020", "Spring 2020", C + "MIT_6.006_Spring2020_OCW_en.zip",
    file("https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6.006-spring-2020.zip"), "CC BY-NC-SA 4.0",
    "数据结构、排序、图搜索、最短路、动态规划；讲义、习题与解答", school="MIT", prereq="Python、离散数学",
    material="讲义+课件+习题/解答（OCW 包，不含视频文件）", order=10, expect={"min_docs": 20})
add("02C02", "02", "course", "MIT 6.046J Design and Analysis of Algorithms (Spring 2015) OCW 课程包", "Erik Demaine, Srini Devadas, Nancy Lynch",
    "2015", "Spring 2015", C + "MIT_6.046J_Spring2015_OCW_en.zip",
    file("https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/6.046j-spring-2015.zip"),
    "CC BY-NC-SA 4.0", "分治、摊还分析、随机算法、网络流、近似算法、分布式算法", school="MIT", level="进阶", prereq="6.006",
    material="讲义+习题/解答（OCW 包）", order=11, expect={"min_docs": 20})
add("02C03", "02", "course", "Princeton COS 226 Algorithms and Data Structures (Spring 2025) 课件", "Robert Sedgewick, Kevin Wayne 等",
    "2025", "Spring 2025", C + "Princeton_COS226_Spring2025_Slides_en",
    pdfset(index="https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures.php", pattern=r"/lectures/.*\.pdf$", min_files=15),
    "课程网站公开课件（版权保留）", "并查集、排序、优先队列、符号表、平衡树、哈希、图、字符串算法", school="Princeton",
    prereq="Java 基础", stack="Java", material="课件 PDF（不含作业与视频）", order=12, complete="部分",
    scope="仅课件 PDF；作业规格在课程站另行发布，未下载")
add("02X01", "02", "practice", "TheAlgorithms/Python（算法参考实现集）", "The Algorithms 社区", "2025", "master 提交",
    X + "TheAlgorithms_Python_master_en.tar", git("TheAlgorithms/Python"), "MIT", "按主题查阅排序、图、DP、数据结构的 Python 实现",
    prereq="Python", stack="Python", use="按需查询", order=20, expect={"min_docs": 5})
add("02X02", "02", "practice", "algs4：Sedgewick & Wayne《Algorithms, 4th ed.》配套 Java 源码", "Robert Sedgewick, Kevin Wayne", "2024",
    "master 提交", X + "algs4_master_en.tar", git("kevin-wayne/algs4"), "GPL-3.0", "教科书级数据结构与算法参考实现",
    prereq="Java", stack="Java", use="按需查询", order=21, expect={"min_docs": 1})

# ============================================================== 03 scientific computing
add("03B01", "03", "book", "Python Data Science Handbook（笔记本全文）", "Jake VanderPlas", "2016", "1st ed. notebooks（master 提交）",
    B + "VanderPlas_PythonDataScienceHandbook_notebooks_en.tar", git("jakevdp/PythonDataScienceHandbook", None, ["notebooks"]),
    "文本 CC BY-NC-ND 3.0，代码 MIT", "IPython、NumPy、pandas、Matplotlib、scikit-learn 全书", prereq="Python 基础",
    stack="NumPy/pandas/Matplotlib", order=1, expect={"min_docs": 40}, cross=["04"])
add("03B02", "03", "book", "Python for Data Analysis (3rd ed., Open Access 网页版)", "Wes McKinney", "2022", "3rd ed.",
    B + "McKinney_PythonForDataAnalysis_3rdEd_html_en.tar", mirror("https://wesmckinney.com/book/", include=["/book"], quota=150),
    FREE, "pandas 作者撰写的数据清洗、分组、时间序列与 NumPy 基础", prereq="Python 基础", stack="pandas/NumPy", order=2,
    expect={"min_docs": 12})
add("03B03", "03", "book", "Python Programming and Numerical Methods: A Guide for Engineers and Scientists", "Qingkai Kong, Timmy Siauw, Alexandre Bayen",
    "2020", "online（Berkeley）", B + "Kong_PythonProgrammingNumericalMethods_html_en.tar",
    mirror("https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html", include=["/notebooks", "/_static", "/_images"],
           quota=300), "CC BY-NC-ND（以站点声明为准）", "数值误差与浮点、线性代数、插值、数值微积分、ODE、傅里叶",
    school="UC Berkeley", prereq="微积分、线性代数", stack="Python/NumPy/SciPy", order=3, expect={"min_docs": 100})
add("03B04", "03", "book", "Scientific Visualization: Python + Matplotlib", "Nicolas P. Rougier", "2021", "1st ed.",
    B + "Rougier_ScientificVisualizationPythonMatplotlib_2021_en.pdf", pdf("https://inria.hal.science/hal-03427242/document", "https://hal.science/hal-03427242/document"),
    "CC BY-NC-SA 4.0", "Matplotlib 进阶：布局、色彩、动画、出版级图表", level="进阶", prereq="NumPy、Matplotlib 基础",
    stack="Matplotlib", order=4, expect={"title_words": ["Scientific", "Visualization", "Matplotlib"], "min_pages": 150})
add("03B05", "03", "book", "Fundamentals of Data Visualization", "Claus O. Wilke", "2019", "online",
    B + "Wilke_FundamentalsOfDataVisualization_html_en.tar", mirror("https://clauswilke.com/dataviz/", include=["/dataviz"], quota=200),
    "CC BY-NC-ND 4.0", "可视化原则：映射、色彩、比例、分布与不确定性表达", prereq="无", stack="（与工具无关）", order=5,
    expect={"min_docs": 30}, cross=["10"])
add("03C01", "03", "course", "UC Berkeley Data 100 Principles and Techniques of Data Science 课程讲义", "Data 100 Course Staff",
    "2025", "course-notes main 提交", C + "Berkeley_Data100_CourseNotes_src_en.tar", git("DS-100/course-notes"), "CC BY-NC-SA 4.0",
    "pandas、数据清洗、可视化、SQL、建模、交叉验证、特征工程", school="UC Berkeley", prereq="Python、Data 8",
    stack="pandas/Matplotlib/scikit-learn", material="课程讲义（Quarto 源与笔记本）", order=10, expect={"min_docs": 20}, cross=["04"])
add("03C02", "03", "course", "UC Berkeley Data 8 教材 Computational and Inferential Thinking", "Ani Adhikari, John DeNero, David Wagner",
    "2022", "2nd ed.（textbook main 提交）", C + "Berkeley_Data8_Textbook_src_en.tar", git("data-8/textbook", None, ["chapters"]),
    "CC BY-NC-ND 4.0", "表格计算、可视化、随机化、推断、回归与分类入门", school="UC Berkeley", prereq="无",
    stack="Python/datascience", material="课程教材（笔记本源）", order=11, expect={"min_docs": 50})
add("03D10", "03", "docs", "Scientific Python Lectures（社区系统教程）", "Scientific Python 社区（G. Varoquaux 等）", "2025", "main 提交",
    D + "scientific_python_lectures_main_src_en.tar", git("scipy-lectures/scientific-python-lectures"), CCBY,
    "NumPy、SciPy、Matplotlib、优化、图像处理、性能技巧的系统教程", prereq="Python 基础", stack="NumPy/SciPy", order=20,
    expect={"min_docs": 30}, material="系统教程（社区维护）")
add("03D11", "03", "docs", "Apache Parquet 格式规范", "Apache Software Foundation", "2025", "master 提交",
    D + "apache_parquet_format_master_en.tar", git("apache/parquet-format"), "Apache-2.0",
    "列式存储格式：编码、压缩、元数据、逻辑类型", level="进阶", prereq="数据处理基础", stack="Parquet", order=21,
    expect={"min_docs": 5}, cross=["08"], use="按需查询")
add("03X01", "03", "practice", "100 NumPy exercises", "Nicolas P. Rougier", "2025", "master 提交", X + "rougier_numpy_100_master_en.tar",
    git("rougier/numpy-100"), "MIT", "100 道向量化练习（附提示与答案）", prereq="NumPy 基础", stack="NumPy", order=30,
    expect={"min_docs": 3})
add("03X02", "03", "practice", "pandas_exercises", "Guilherme Samora", "2023", "master 提交", X + "guipsamora_pandas_exercises_master_en.tar",
    git("guipsamora/pandas_exercises"), "BSD-3-Clause", "按主题的 pandas 练习（筛选、分组、合并、时间序列、可视化）",
    prereq="pandas 基础", stack="pandas", order=31, expect={"min_docs": 20})
add("03X03", "03", "practice", "From Python to Numpy（向量化专题书与示例）", "Nicolas P. Rougier", "2017", "master 提交",
    X + "rougier_from_python_to_numpy_master_en.tar", git("rougier/from-python-to-numpy"), "CC BY-NC-SA 4.0（文本）/ BSD（代码）",
    "从循环到向量化的思维转换与案例", level="进阶", prereq="NumPy", stack="NumPy", order=32, expect={"min_docs": 5})

# ============================================================== 04 ML programming
add("04B01", "04", "book", "An Introduction to Statistical Learning with Applications in Python", "G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor",
    "2023", "1st ed. (Python)", B + "James_IntroductionStatisticalLearningPython_1stEd_en.pdf", None, "作者网站免费 PDF（版权保留）",
    "重抽样、交叉验证、模型选择、树模型、深度学习的 Python 实验", prereq="概率统计、Python", stack="Python/scikit-learn/ISLP",
    order=1, reuse=reuse("/root/industrial_process_monitoring_literature/books/James_IntroductionStatisticalLearningPython_1stEd_en.pdf", "https://www.statlearning.com/"),
    expect={"title_words": ["Statistical", "Learning", "Python"], "min_pages": 500})
add("04B02", "04", "book", "Data Science and Machine Learning: Mathematical and Statistical Methods", "D. P. Kroese, Z. I. Botev, T. Taimre, R. Vaisman",
    "2019", "1st ed.（作者修订 PDF）", B + "Kroese_DataScienceAndMachineLearning_2019_en.pdf", pdf("https://people.smp.uq.edu.au/DirkKroese/DSML/DSML.pdf"), "作者网站免费 PDF（版权保留）",
    "统计学习与 Python 代码并行讲解：模型评估、正则化、核方法、深度学习", level="进阶", prereq="线性代数、概率",
    stack="Python/NumPy", order=2,
    expect={"title_words": ["Data", "Science", "Machine", "Learning"], "min_pages": 500})
add("04B03", "04", "book", "Patterns, Predictions, and Actions: Foundations of Machine Learning", "Moritz Hardt, Benjamin Recht",
    "2022", "1st ed.", B + "Hardt_PatternsPredictionsActions_2022_en.pdf", None, "CC BY-NC-ND 4.0",
    "数据集、基准、泛化与留出法、因果与序贯决策；理解数据泄漏与评测偏差", level="进阶", prereq="概率统计", order=3,
    reuse=reuse("/root/time_series_literature/books/files/Hardt_PatternsPredictionsActionsFoundationsMac_1steditionarXiv_2022_en.pdf", "https://mlstory.org/"),
    expect={"title_words": ["Patterns", "Predictions", "Actions"], "min_pages": 250})
add("04B04", "04", "book", "Machine Learning in Production: From Models to Products", "Christian Kästner", "2025", "online（CMU 课程教材）",
    B + "Kastner_MachineLearningInProduction_html_en.tar", mirror("https://mlip-cmu.github.io/book/", include=["/book"], quota=200),
    "CC BY-NC-ND 4.0（以站点声明为准）", "需求、数据质量、模型评估、部署、监控、MLOps、负责任工程", level="进阶",
    prereq="机器学习基础、软件工程基础", school="Carnegie Mellon University", order=4, expect={"min_docs": 20}, cross=["14", "06"])
add("04C01", "04", "course", "MIT 6.390 Introduction to Machine Learning 讲义", "MIT 6.390 Staff", "2024", "online notes",
    C + "MIT_6390_LectureNotes_html_en.tar", mirror("https://introml.mit.edu/notes/", include=["/notes", "/_static", "/_images"], quota=150), "MIT 课程网站公开讲义", "回归、分类、特征表示、神经网络、交叉验证的讲义",
    school="MIT", prereq="线性代数、Python", material="讲义", order=10,
    expect={"min_docs": 10})
add("04C02", "04", "course", "CMU 17-445/645 Machine Learning in Production（课件与实验）", "Christian Kästner 等", "2025", "Spring 2025（仓库提交）",
    C + "CMU_17645_MLinProduction_2025_src_en.tar", git("mlip-cmu/s2025"), "CC BY-NC-SA 4.0（以仓库为准）",
    "ML 系统工程：数据管线、测试、部署、监控、安全与公平；含实验说明", school="Carnegie Mellon University", level="进阶",
    prereq="ML 基础、Python", material="课件 + 实验（labs）+ 阅读材料", order=11, expect={"min_docs": 20}, cross=["14"])
add("04C03", "04", "course", "Stanford CS 329S Machine Learning Systems Design (Winter 2022) 讲义", "Chip Huyen", "2022", "Winter 2022",
    C + "Stanford_CS329S_2022_Notes_html_en.tar", mirror("https://stanford-cs329s.github.io/syllabus.html", quota=200, level="2"),
    "课程网站公开讲义（版权保留）", "数据工程、特征、模型开发与离线评估、部署、监控与持续学习", school="Stanford", level="进阶",
    prereq="ML 基础", material="讲义（lecture notes）+ 课件链接页", order=12, expect={"min_docs": 10})
add("04C04", "04", "course", "Inria scikit-learn MOOC: Machine learning in Python with scikit-learn", "Inria（G. Varoquaux, O. Grisel 等）",
    "2024", "main 提交", C + "Inria_scikit-learn_MOOC_src_en.tar", git("INRIA/scikit-learn-mooc"), "CC BY 4.0",
    "预处理管线、交叉验证、超参数调优、模型评估与数据泄漏防范的完整课程（研究机构课程）", school="Inria（研究机构）",
    prereq="Python、NumPy、pandas", stack="scikit-learn", material="课程笔记本 + 测验 + 讲解（研究机构官方课程，非大学）", order=13,
    expect={"min_docs": 50})
add("04X01", "04", "practice", "Made With ML（MLOps 端到端课程项目）", "Goku Mohandas", "2024", "main 提交", X + "madewithml_main_en.tar",
    git("GokuMohandas/Made-With-ML"), "MIT", "数据处理、训练、调优、评估、服务化、CI/CD 的完整参考项目",
    level="进阶", prereq="Python、ML 基础", stack="PyTorch/Ray/MLflow", order=20, expect={"min_docs": 3}, cross=["14"])
add("04X02", "04", "practice", "Cookiecutter Data Science（项目结构模板 v2）", "DrivenData", "2025", "master 提交",
    X + "cookiecutter_data_science_master_en.tar", git("drivendataorg/cookiecutter-data-science"), "MIT",
    "数据科学项目目录、数据分层与可复现约定", prereq="Python", order=21, expect={"min_docs": 5}, cross=["06"])

# ============================================================== 05 DL programming
add("05B01", "05", "book", "Dive into Deep Learning", "Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola", "2023",
    "PyTorch 版 PDF", B + "Zhang_DiveIntoDeepLearning_2023_en.pdf", None, "CC BY-SA 4.0",
    "从张量、自动微分到 CNN/RNN/Transformer、优化与计算性能（多 GPU）的可运行教材", prereq="Python、线性代数",
    stack="PyTorch", order=1, reuse=reuse("/root/time_series_literature/books/files/Zhang_DiveIntoDeepLearning_PyTorchPDF_2023_en.pdf", "https://d2l.ai/"),
    expect={"title_words": ["Dive", "Deep", "Learning"], "min_pages": 800})
add("05B02", "05", "book", "Understanding Deep Learning", "Simon J. D. Prince", "2023", "MIT Press 2023（作者 PDF）",
    B + "Prince_UnderstandingDeepLearning_2023_en.pdf", None, "CC BY-NC-ND（作者网站）", "网络结构、损失、训练、初始化、正则化的原理（配套笔记本）",
    level="进阶", prereq="线性代数、概率", order=2, reuse=reuse("/root/time_series_literature/books/files/Prince_UnderstandingDeepLearning_PDFv503GitHubrelease20260209_2023_en.pdf",
                                                              "https://udlbook.github.io/udlbook/"),
    expect={"title_words": ["Understanding", "Deep", "Learning"], "min_pages": 400})
add("05B03", "05", "book", "The Little Book of Deep Learning", "François Fleuret", "2023", "v1.2",
    B + "Fleuret_LittleBookOfDeepLearning_2023_en.pdf", pdf("https://fleuret.org/public/lbdl.pdf"), "CC BY-NC-SA 4.0",
    "深度学习核心组件的简明速查", order=3,
    expect={"title_words": ["Little", "Book", "Deep", "Learning"], "min_pages": 100}, use="按需查询")
add("05B04", "05", "book", "Machine Learning Engineering Open Book", "Stas Bekman", "2025", "master 提交",
    B + "Bekman_MachineLearningEngineeringOpenBook_src_en.tar", git("stas00/ml-engineering"), "CC BY-SA 4.0",
    "大模型训练工程：调试、检查点、混合精度、网络与存储、分布式训练故障排查", level="进阶-高级", prereq="PyTorch",
    stack="PyTorch/NCCL/SLURM", order=4, expect={"min_docs": 30}, cross=["13", "14"], use="按需查询")
add("05C01", "05", "course", "Stanford CS231n Deep Learning for Computer Vision 课程讲义", "Fei-Fei Li, Justin Johnson 等", "2025",
    "online notes", C + "Stanford_CS231n_Online_LectureNotes_en", None, "课程网站公开讲义（MIT 许可仓库）",
    "反向传播、CNN、训练技巧、PyTorch 实现", school="Stanford", prereq="Python、线性代数", material="讲义", order=10,
    reuse=reuse("/root/ai_undergraduate_graduate_curriculum_literature/courses/Stanford_CS231n_Online_CourseNotes_html_en", "https://cs231n.github.io/"))
add("05C02", "05", "course", "CMU 10-414/714 Deep Learning Systems: Algorithms and Implementation 课件与作业", "Zico Kolter, Tianqi Chen",
    "2024", "Fall 2024 / online", C + "CMU_10714_DLSys_Lectures_en",
    pdfset(index="https://dlsyscourse.org/lectures/", pattern=r"\.pdf$", min_files=10), "课程网站公开课件（版权保留）",
    "自动微分、needle 框架实现、GPU 加速、CNN/RNN/Transformer 实现与优化", school="Carnegie Mellon University", level="进阶",
    prereq="Python、C++、ML 基础", material="课件 PDF（作业框架见实践项目 05X21）", order=11, cross=["13"], complete="部分",
    scope="课程站全部课件 PDF；实现类讲次以 GitHub 笔记本发布（lecture5/8/13 等仓库），未下载")
add("05C03", "05", "course", "University of Amsterdam Deep Learning Course 教程笔记本（UvA DL Notebooks）", "Phillip Lippe 等", "2024",
    "master 提交", C + "UvA_DL_Notebooks_src_en.tar", git("phlippe/uvadlc_notebooks", None, ["docs"]), "MIT",
    "PyTorch/JAX 实现：激活、优化、Transformer、GNN、自监督、多 GPU 训练", school="University of Amsterdam", level="进阶",
    prereq="Python、DL 基础", stack="PyTorch/JAX", material="教程笔记本（课程官方）", order=12, expect={"min_docs": 30})
add("05C04", "05", "course", "MIT 6.S191 Introduction to Deep Learning 实验（labs 仓库，PyTorch 与 TensorFlow 双版本）", "Alexander Amini, Ava Amini",
    "2026", "master 提交", C + "MIT_6S191_Labs_src_en.tar", git("MITDeepLearning/introtodeeplearning"), "MIT",
    "MIT 官方课程实验：音乐生成 RNN、人脸检测去偏、LLM 微调等，分别提供 PyTorch 与 TensorFlow 笔记本", school="MIT",
    prereq="Python、DL 基础", stack="PyTorch/TensorFlow", material="实验笔记本 + 课程工具包（课件/视频在课程站，未下载）",
    order=13, complete="部分", scope="仅实验仓库（labs）；讲座课件与视频未下载", expect={"min_docs": 5})
add("05X01", "05", "practice", "micrograd（最小自动微分引擎）", "Andrej Karpathy", "2020", "master 提交", X + "karpathy_micrograd_master_en.tar",
    git("karpathy/micrograd"), "MIT", "手写标量自动微分与小型神经网络", prereq="Python", stack="Python", order=20,
    expect={"min_docs": 1})
add("05X02", "05", "practice", "Neural Networks: Zero to Hero（笔记本与练习）", "Andrej Karpathy", "2024", "master 提交",
    X + "karpathy_nn_zero_to_hero_master_en.tar", git("karpathy/nn-zero-to-hero"), "MIT",
    "从 micrograd 到 makemore 到 GPT 的逐步实现", prereq="Python", stack="PyTorch", order=21, expect={"min_docs": 3})
add("05X03", "05", "practice", "nanoGPT", "Andrej Karpathy", "2024", "master 提交", X + "karpathy_nanoGPT_master_en.tar",
    git("karpathy/nanoGPT"), "MIT", "最小 GPT 训练/微调代码：数据管线、训练循环、混合精度、DDP、检查点", level="进阶",
    prereq="PyTorch", stack="PyTorch", order=22, expect={"min_docs": 1}, cross=["13"])
add("05X21", "05", "practice", "CMU DLSys needle 作业框架（hw0–hw4 公开模板）", "CMU DLSys Course Staff", "2024", "main 提交",
    X + "dlsys_needle_homework_en", {"kind": "multi_git", "repos": ["https://github.com/dlsyscourse/hw0", "https://github.com/dlsyscourse/hw1",
                                                                   "https://github.com/dlsyscourse/hw2", "https://github.com/dlsyscourse/hw3",
                                                                   "https://github.com/dlsyscourse/hw4"]},
    "以各仓库许可为准", "实现自动微分、NN 模块、CPU/GPU 后端与模型", level="进阶", prereq="Python、C++、CUDA 基础",
    stack="Python/C++/CUDA", order=23, cross=["13"])

# ============================================================== 06 SE & testing
add("06B01", "06", "book", "Software Engineering at Google: Lessons Learned from Programming Over Time", "Titus Winters, Tom Manshreck, Hyrum Wright",
    "2020", "online", B + "Winters_SoftwareEngineeringAtGoogle_html_en.tar",
    mirror("https://abseil.io/resources/swe-book/html/toc.html", include=["/resources/swe-book"], quota=200), "CC BY-NC-ND 4.0",
    "代码评审、测试（单元/集成/大型）、依赖管理、构建系统、CI/CD、弃用", level="进阶", prereq="编程经验", order=1,
    expect={"min_docs": 25})
add("06B02", "06", "book", "Architecture Patterns with Python（Cosmic Python）", "Harry Percival, Bob Gregory", "2020", "online",
    B + "Percival_ArchitecturePatternsWithPython_html_en.tar",
    mirror("https://www.cosmicpython.com/book/preface.html", include=["/book"], quota=100), "CC BY-NC-ND 4.0",
    "领域模型、仓储、服务层、单元工作、事件、依赖注入与测试金字塔", level="进阶", prereq="Python、Flask/SQLAlchemy 基础",
    stack="Python", order=2, expect={"min_docs": 15}, cross=["09"])
add("06B03", "06", "book", "Test-Driven Development with Python (3rd ed., online)", "Harry Percival", "2025", "3rd ed. online",
    B + "Percival_TDDWithPython_3rdEd_html_en.tar", mirror("https://www.obeythetestinggoat.com/book/preface.html", include=["/book"], quota=150),
    "CC BY-NC-ND（以站点声明为准）", "TDD、功能测试、单元测试、Django、部署与 CI", prereq="Python 基础", stack="Python/Django",
    order=3, expect={"min_docs": 20}, cross=["09"])
add("06B04", "06", "book", "The Architecture of Open Source Applications (Vol. I & II)", "Amy Brown, Greg Wilson（编）", "2012",
    "online", B + "Brown_ArchitectureOfOpenSourceApplications_html_en.tar",
    mirror("https://aosabook.org/en/index.html", include=["/en"], quota=200), "CC BY 3.0",
    "真实开源系统（如 Git、LLVM、Mercurial、NumPy 等）的架构剖析", level="进阶", prereq="编程经验", order=4, use="按需查询",
    expect={"min_docs": 40})
add("06B05", "06", "book", "Producing Open Source Software (2nd ed.)", "Karl Fogel", "2023", "2.3xxx（PDF 内版本为准）",
    B + "Fogel_ProducingOpenSourceSoftware_2ndEd_en.pdf", pdf("https://producingoss.com/en/producingoss-a4.pdf"), "CC BY-SA 4.0",
    "协作流程、版本控制、发布、沟通与社区治理", prereq="无", order=5, use="按需查询",
    expect={"title_words": ["Producing", "Open", "Source", "Software"], "min_pages": 150}, cross=["07"])
add("06C01", "06", "course", "MIT 6.031 Software Construction (Spring 2022) 阅读讲义", "MIT 6.031 Staff", "2022", "Spring 2022",
    C + "MIT_6.031_Spring2022_Readings_html_en.tar", mirror("https://web.mit.edu/6.031/www/sp22/", include=["/6.031/www/sp22"], quota=200),
    "CC BY-SA 4.0", "规格、测试、抽象数据类型、不变量、并发、递归数据类型、代码评审", school="MIT", level="进阶",
    prereq="一门编程语言", stack="TypeScript", material="完整阅读讲义（readings）+ 课程页面", order=10, expect={"min_docs": 30})
add("06C02", "06", "course", "CMU 17-313 Foundations of Software Engineering（课件、作业与讲习）", "CMU 17-313 Course Staff",
    "2026", "Fall 2026（main 提交）", C + "CMU_17313_FoundationsSE_src_en.tar",
    git("CMU-313/CMU-313.github.io", None, ["slides", "assignments", "recitations", "specs", "17-313 Fall 2026 Schedule - Lecture Schedule.csv"]),
    "以仓库 LICENSE 为准", "需求、架构、测试与 CI、代码评审、开源协作、DevOps、AI 辅助开发的软件工程课程", school="Carnegie Mellon University",
    level="进阶", prereq="一门编程语言、Git", material="课件 + 作业规格 + 讲习材料（课程官方仓库；不含历史学期归档）", order=11,
    expect={"min_docs": 10})
add("06X01", "06", "practice", "500 Lines or Less（AOSA 小型完整项目集）", "Michael DiBernardo（编）", "2016", "master 提交",
    X + "aosabook_500lines_master_en.tar", git("aosabook/500lines"), "CC BY 3.0（文本）/ MIT（代码，以子项目为准）",
    "阅读 20+ 个小型但完整的系统实现（模板引擎、数据库、爬虫、CI 系统等）", level="进阶", prereq="Python", order=20,
    expect={"min_docs": 20}, cross=["01"])
add("06X02", "06", "practice", "Software Carpentry: Programming with Python（含防御式编程与测试）", "The Carpentries", "2025",
    "main 提交", X + "swcarpentry_python_novice_inflammation_main_en.tar", git("swcarpentry/python-novice-inflammation"), "CC BY 4.0",
    "函数、错误处理、防御式编程、调试与测试的课堂练习", prereq="无", stack="Python", order=21, expect={"min_docs": 15}, cross=["01"])
add("06X03", "06", "practice", "Hypermodern Python Cookiecutter（打包、类型检查、测试与 CI 模板）", "Claudio Jolowicz", "2024",
    "main 提交", X + "cjolowicz_cookiecutter_hypermodern_python_main_en.tar", git("cjolowicz/cookiecutter-hypermodern-python"), "MIT",
    "src 布局、pytest、mypy、ruff/pre-commit、nox、GitHub Actions 发布流程", level="进阶", prereq="Python 打包基础",
    order=22, expect={"min_docs": 5})
add("06D10", "06", "docs", "GitHub Actions 官方文档（github/docs content/actions）", "GitHub", "2026", "main 提交",
    D + "github_actions_docs_main_src_en.tar", git("github/docs", None, ["content/actions", "data/reusables/actions"]), "CC BY 4.0",
    "工作流语法、运行器、缓存、制品、密钥、部署与安全加固", prereq="Git", stack="GitHub Actions", order=30,
    expect={"min_docs": 100}, cross=["14", "16"], use="按需查询")

# ============================================================== 07 Linux / Shell / Git
add("07B01", "07", "book", "The Linux Command Line (5th Internet Edition)", "William E. Shotts", "2019", "19.01",
    B + "Shotts_TheLinuxCommandLine_19.01_en.pdf",
    {"kind": "pdf", "urls": [], "page": "https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download",
         "link_pattern": r"https://downloads\.sourceforge\.net/project/linuxcommand/TLCL/19\.01/TLCL-19\.01\.pdf\?[^\"']+"}, "CC BY-NC-ND 3.0",
    "文件系统、权限、进程、环境、文本处理、Shell 脚本", prereq="无", stack="bash", order=1,
    expect={"title_words": ["Linux", "Command", "Line"], "min_pages": 400})
add("07B02", "07", "book", "Pro Git (2nd ed.)", "Scott Chacon, Ben Straub", "2014", "2.1.450（GitHub release）",
    B + "Chacon_ProGit_2ndEd_2.1.450_en.pdf", pdf("https://github.com/progit/progit2/releases/download/2.1.450/progit.pdf"),
    "CC BY-NC-SA 3.0", "Git 基础、分支、远程协作、GitHub、内部原理与故障恢复", prereq="命令行基础", stack="Git", order=2,
    expect={"title_words": ["Pro", "Git"], "min_pages": 400})
add("07B03", "07", "book", "Advanced Bash-Scripting Guide", "Mendel Cooper", "2014", "10", B + "Cooper_AdvancedBashScriptingGuide_10_en.pdf",
    pdf("https://tldp.org/LDP/abs/abs-guide.pdf"), "公有领域（作者声明）", "Bash 脚本语法、引用、I/O 重定向、调试与大量示例",
    level="进阶", prereq="Shell 基础", stack="bash", order=3, use="按需查询",
    expect={"title_words": ["Advanced", "Bash", "Scripting", "Guide"], "min_pages": 500}, note="经典版本，部分写法已过时，对照 GNU Bash 手册使用")
add("07B04", "07", "book", "The Debian Administrator's Handbook（Debian 12 bookworm）", "Raphaël Hertzog, Roland Mas", "2023", "stable",
    B + "Hertzog_DebianAdministratorsHandbook_stable_html_en.tar", mirror("https://debian-handbook.info/browse/stable/", include=["/browse/stable"], quota=200),
    "CC BY-SA 3.0 / GPL-2.0+", "系统安装、包管理、服务、网络、安全与故障排查", level="进阶", prereq="命令行基础", stack="Debian/Linux",
    order=4, use="按需查询", expect={"min_docs": 100}, note="官网 PDF 链接 404，改存官方在线 HTML 版（browse/stable）")
add("07C01", "07", "course", "MIT The Missing Semester of Your CS Education（讲义源）", "Anish Athalye, Jon Gjengset, Jose Javier Gonzalez Ortiz",
    "2020", "master 提交（含 2020 及后续更新）", C + "MIT_MissingSemester_src_en.tar", git("missing-semester/missing-semester"),
    "CC BY-NC-SA 4.0", "Shell、脚本、编辑器、数据整理、命令行环境、版本控制、调试与性能分析、安全", school="MIT", prereq="无",
    material="讲义正文 + 练习（视频仅链接未下载）", order=10, expect={"min_docs": 15})
add("07C02", "07", "course", "University of Cambridge Unix Tools 课件", "Markus Kuhn", "2024", "Michaelmas 2024",
    C + "Cambridge_UnixTools_Slides_en", pdfset(index="https://www.cl.cam.ac.uk/teaching/2425/UnixTools/materials.html",
                                                pattern=r"(?<!answers)\.pdf$", min_files=1),
    "课程网站公开课件（版权保留）", "Unix 工具链、Shell、正则、构建与版本控制", school="University of Cambridge", prereq="无",
    material="课件 PDF", order=11)
add("07D01", "07", "docs", "GNU Bash Reference Manual", "Free Software Foundation", "2025", "当前版（PDF 内为准）", D + "gnu_bash_manual_en.pdf",
    pdf("https://www.gnu.org/software/bash/manual/bash.pdf"), "GFDL", "Bash 语法、展开、重定向、内建命令的权威参考",
    stack="bash", order=20, use="按需查询", expect={"title_words": ["Bash", "Reference", "Manual"], "min_pages": 150})
add("07D02", "07", "docs", "GNU Coreutils Manual", "Free Software Foundation", "2025", "当前版", D + "gnu_coreutils_manual_en.pdf",
    pdf("https://www.gnu.org/software/coreutils/manual/coreutils.pdf"), "GFDL", "ls/cp/sort/cut 等核心工具参考", order=21,
    use="按需查询", expect={"title_words": ["Core", "GNU", "utilities"], "min_pages": 150})
add("07D03", "07", "docs", "Git 官方参考文档 HTML 包（git-htmldocs 2.56.0）", "Git 项目", "2026", "2.56.0",
    D + "git_htmldocs_2.56.0_en.tar.xz", file("https://mirrors.edge.kernel.org/pub/software/scm/git/git-htmldocs-2.56.0.tar.xz"),
    "GPL-2.0", "全部 git 命令手册页、gittutorial、gitworkflows、gitglossary", stack="Git", order=22, use="按需查询",
    expect={"min_docs": 150, "entry": "git.html"})
add("07D04", "07", "docs", "Linux man-pages 6.20（系统调用与库函数手册源）", "Linux man-pages project", "2026", "6.20",
    D + "linux_man_pages_6.20_en.tar.xz", file("https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-6.20.tar.xz"),
    "多种自由许可（见各页）", "man2 系统调用、man3 库函数、man7 概述（进程、信号、套接字等）", level="进阶", stack="Linux",
    order=23, use="按需查询", expect={"min_docs": 1, "must_have": [r"man2/"]}, cross=["11", "12"])
add("07X01", "07", "practice", "Software Carpentry: The Unix Shell", "The Carpentries", "2025", "main 提交", X + "swcarpentry_shell_novice_main_en.tar",
    git("swcarpentry/shell-novice"), "CC BY 4.0", "带练习的 Shell 课堂教程（导航、管道、循环、脚本、查找）", prereq="无",
    stack="bash", order=30, expect={"min_docs": 10})
add("07X02", "07", "practice", "Software Carpentry: Version Control with Git", "The Carpentries", "2025", "main 提交", X + "swcarpentry_git_novice_main_en.tar",
    git("swcarpentry/git-novice"), "CC BY 4.0", "带练习的 Git 课堂教程（提交、历史、远程、冲突）", prereq="Shell 基础", stack="Git",
    order=31, expect={"min_docs": 10})
add("07X03", "07", "practice", "Linux From Scratch 12.x 书籍源（从源码构建 Linux 系统的实践项目）", "Gerard Beekmans 等", "2025", "trunk 提交",
    X + "lfs_book_trunk_en.tar", git("https://git.linuxfromscratch.org/lfs.git"), "CC BY-NC-SA 2.0（文本）/ MIT（命令）",
    "工具链、包构建、系统启动的完整动手项目", level="高级", prereq="Linux 熟练", order=32, expect={"min_docs": 1, "need_license": False, "must_have": [r"chapter\d+/.*\.xml$"]},
    note="仓库许可声明在书内 appendices，不在根目录 LICENSE")

# ============================================================== 08 DB & data engineering
add("08B01", "08", "book", "Readings in Database Systems (5th ed., Red Book)", "Peter Bailis, Joseph M. Hellerstein, Michael Stonebraker（编）",
    "2015", "5th ed.", B + "Bailis_ReadingsInDatabaseSystems_5thEd_en.pdf",
    pdf("http://www.redbook.io/pdf/redbook-5th-edition.pdf", "https://www.redbook.io/pdf/redbook-5th-edition.pdf"), "CC BY-NC-SA",
    "关系系统、事务、查询优化、分析型与流式系统的导读", level="进阶", prereq="数据库基础", order=1,
    expect={"title_words": ["Readings", "Database", "Systems"], "min_pages": 40})
add("08B02", "08", "book", "Architecture of a Database System", "Joseph M. Hellerstein, Michael Stonebraker, James Hamilton", "2007",
    "FnT Databases 1(2)", B + "Hellerstein_ArchitectureOfADatabaseSystem_2007_en.pdf",
    pdf("http://dsf.berkeley.edu/papers/fntdb07-architecture.pdf", "https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf"),
    "作者网站公开", "进程模型、并行架构、查询处理、存储与事务管理的整体结构", level="进阶", prereq="数据库基础", order=2,
    expect={"title_words": ["Architecture", "Database", "System"], "min_pages": 100})
add("08B03", "08", "book", "Foundations of Databases", "Serge Abiteboul, Richard Hull, Victor Vianu", "1995", "Webdam 版",
    B + "Abiteboul_FoundationsOfDatabases_1995_en.pdf", pdf("http://webdam.inria.fr/Alice/pdfs/all.pdf"), "作者授权免费分发",
    "关系模型、查询语言、依赖与规范化理论", level="高级", prereq="离散数学", order=3, use="按需查询",
    expect={"title_words": ["Conjunctive", "Queries", "Relational"], "min_pages": 600},
    note="PDF 无封面页，以目录开头；目录与正文完整")
add("08B04", "08", "book", "Use The Index, Luke!（SQL 索引与性能）", "Markus Winand", "2024", "online",
    B + "Winand_UseTheIndexLuke_html_en.tar", mirror("https://use-the-index-luke.com/sql/table-of-contents", include=["/sql", "/static"],
                                                    quota=100, reject_regex=r"/(de|fr|es|ja|it)/"),
    FREE, "B-tree 索引、执行计划、连接、排序/分组、分页、写入代价", level="进阶", prereq="SQL 基础", stack="SQL（多数据库）",
    order=4, expect={"min_docs": 30})
add("08B05", "08", "book", "Database Design (2nd ed.)", "Adrienne Watt, Nelson Eng", "2014", "2nd ed.（BCcampus Open Textbook）",
    B + "Watt_DatabaseDesign_2ndEd_html_en.tar", mirror("https://opentextbc.ca/dbdesign01/", include=["/dbdesign01"], quota=100),
    "CC BY 4.0", "数据建模、ER 图、规范化、完整性约束与 SQL", prereq="无", order=5, expect={"min_docs": 15})
add("08C01", "08", "course", "CMU 15-445/645 Database Systems (Fall 2025) 课件与讲义", "Andy Pavlo 等", "2025", "Fall 2025",
    C + "CMU_15445_Fall2025_Slides_en",
    pdfset(index="https://15445.courses.cs.cmu.edu/fall2025/schedule.html", pattern=r"/(slides|notes)/.*\.pdf$", min_files=15),
    "课程网站公开（版权保留）", "存储、缓冲池、索引、查询执行与优化、并发控制、恢复、分布式数据库", school="Carnegie Mellon University",
    level="进阶", prereq="C++、数据结构", material="课件 PDF + 讲义 PDF（项目见 08X01 BusTub）", order=10)
add("08C02", "08", "course", "UC Berkeley CS 186 Introduction to Database Systems 课程讲义", "CS 186 Course Staff", "2025", "online notes",
    C + "Berkeley_CS186_Notes_html_en.tar", mirror("https://cs186berkeley.net/notes/", include=["/notes", "/assets"], quota=100),
    "课程网站公开（版权保留）", "SQL、磁盘与文件、B+ 树、排序/哈希、连接算法、优化、事务与恢复", school="UC Berkeley",
    prereq="数据结构", material="讲义", order=11, expect={"min_docs": 15})
add("08D01", "08", "docs", "PostgreSQL 18 官方文档（A4 PDF）", "PostgreSQL Global Development Group", "2025", "18",
    D + "postgresql_18_docs_a4_en.pdf", pdf("https://www.postgresql.org/files/documentation/pdf/18/postgresql-18-A4.pdf"),
    "PostgreSQL License", "SQL 语言、索引、事务隔离、性能调优、备份恢复、复制", stack="PostgreSQL", order=20, use="教程通读，其余查询",
    expect={"title_words": ["PostgreSQL", "Documentation"], "min_pages": 2000})
add("08D02", "08", "docs", "SQLite 文档包（3.54.1）", "SQLite 开发团队", "2026", "3.54.1", D + "sqlite_doc_3540100_en.zip",
    file("https://www.sqlite.org/2026/sqlite-doc-3540100.zip"), "公有领域", "SQL 方言、查询规划器、WAL、事务与文件格式",
    stack="SQLite", order=21, use="按需查询", expect={"min_docs": 200})
add("08D03", "08", "docs", "Apache Kafka 4.x 官方文档（kafka-site）", "Apache Software Foundation", "2026", "asf-site 提交",
    D + "apache_kafka_site_docs_en.tar", git("apache/kafka-site", "asf-site", ["/*.html", "41", "40", "css", "js", "images"]),
    "Apache-2.0", "消息系统：设计、生产者/消费者、Streams、Connect、运维", level="进阶", stack="Kafka", order=22,
    expect={"min_docs": 30}, cross=["14"], use="按需查询")
add("08D04", "08", "docs", "Apache Flink 2.x 文档源（docs/content）", "Apache Software Foundation", "2026", "release 分支提交",
    D + "apache_flink_docs_src_en.tar", git("apache/flink", None, ["docs/content"]), "Apache-2.0",
    "流处理：DataStream、状态、检查点、时间/水位线、SQL", level="进阶", stack="Flink", order=23, expect={"min_docs": 200},
    cross=["14"], use="按需查询")
add("08X01", "08", "practice", "CMU BusTub（教学关系数据库系统骨架）", "CMU Database Group", "2025", "master 提交", X + "cmu_bustub_master_en.tar",
    git("cmu-db/bustub"), "MIT", "实现缓冲池、B+ 树索引、查询执行器、并发控制", level="进阶", prereq="C++17", stack="C++",
    order=30, expect={"min_docs": 3})
add("08X02", "08", "practice", "DataTalksClub Data Engineering Zoomcamp", "DataTalksClub", "2026", "main 提交",
    X + "datatalksclub_de_zoomcamp_main_en.tar", git("DataTalksClub/data-engineering-zoomcamp"), "以仓库为准（见 LICENSE）",
    "容器化、工作流编排、数据仓库、dbt、批处理（Spark）、流处理（Kafka）的项目式课程", level="进阶", prereq="Python、SQL、Docker",
    order=31, expect={"min_docs": 30}, cross=["14"])
add("09B01", "09", "book", "High Performance Browser Networking", "Ilya Grigorik", "2013", "online（持续更新）",
    B + "Grigorik_HighPerformanceBrowserNetworking_html_en.tar", mirror("https://hpbn.co/", quota=100, level="2"),
    "免费在线阅读（O'Reilly 授权）", "TCP/UDP/TLS、HTTP/1.1/2、WebSocket、SSE、WebRTC 的性能原理", level="进阶",
    prereq="网络基础", order=1, expect={"min_docs": 15}, cross=["11", "10"])
add("09B02", "09", "book", "HTTP/3 explained", "Daniel Stenberg", "2024", "master 提交", B + "Stenberg_HTTP3Explained_src_en.tar",
    git("bagder/http3-explained"), "CC BY 4.0", "QUIC 与 HTTP/3 的动机、连接、流、QPACK 与部署现状（curl 作者撰写）",
    level="进阶", prereq="HTTP/1.1、TCP 基础", order=2, expect={"min_docs": 10}, cross=["11"])
add("09D06", "09", "docs", "Microsoft REST API Guidelines", "Microsoft", "2025", "vNext 分支提交", D + "microsoft_api_guidelines_vnext_en.tar",
    git("microsoft/api-guidelines", "vNext"), "CC BY 4.0", "REST 资源设计、版本化、错误格式、分页、长时操作", level="进阶",
    stack="REST", order=25, expect={"min_docs": 5}, use="按需查询")
add("09D07", "09", "docs", "Google API Improvement Proposals（AIP）", "Google / aip.dev", "2026", "master 提交", D + "google_aip_master_en.tar",
    git("aip-dev/google.aip.dev", None, ["aip"]), "CC BY 4.0（文档，以仓库为准）", "资源导向 API 设计规范：命名、标准方法、分页、过滤、错误、版本",
    level="进阶", stack="REST/gRPC", order=26, expect={"min_docs": 100}, use="按需查询")
add("09B03", "09", "book", "HTTP/2 explained", "Daniel Stenberg", "2015", "master 提交", B + "Stenberg_HTTP2Explained_src_en.tar",
    git("bagder/http2-explained"), "CC BY 4.0", "HTTP/1.1 的瓶颈、HTTP/2 二进制分帧、多路复用、头部压缩与服务端推送", level="进阶",
    prereq="HTTP/1.1", order=3, expect={"min_docs": 5, "need_license": False}, cross=["11"],
    note="仓库无独立 LICENSE 文件；README 声明以 CC BY 4.0 分发")
add("09C01", "09", "course", "Harvard CS50's Web Programming with Python and JavaScript 讲义与项目", "Brian Yu, David J. Malan",
    "2026", "当前版（/web/，2020 版 URL 已重定向至此，页面年份为准）", C + "Harvard_CS50W_NotesProjects_html_en.tar",
    mirror("https://cs50.harvard.edu/web/", include=["/web"], quota=150), "CC BY-NC-SA 4.0",
    "HTML/CSS、Git、Python、Django、SQL/模型/迁移、JavaScript、用户界面、测试与 CI/CD、扩展与安全", school="Harvard",
    prereq="编程基础", stack="Django/JavaScript", material="讲义 notes + 项目规格（视频仅链接）", order=10, expect={"min_docs": 15}, cross=["10"])
add("09C02", "09", "course", "Stanford CS 142 Web Applications 讲义", "Mendel Rosenblum", "2024", "当前学期页面",
    C + "Stanford_CS142_LectureNotes_en", pdfset(index="https://web.stanford.edu/class/cs142/lectures.html", pattern=r"\.pdf$", min_files=10),
    "课程网站公开（版权保留）", "浏览器、DOM、前端框架、HTTP、会话状态、数据库、Web 安全、扩展", school="Stanford", level="进阶",
    prereq="编程基础", material="讲义 PDF", order=11, cross=["10", "16"])
add("09D01", "09", "docs", "Django 6.0 官方文档（HTML 包）", "Django Software Foundation", "2025", "6.0", D + "django_6.0_docs_html_en.zip",
    file("https://media.djangoproject.com/docs/django-docs-6.0-en.zip"), "BSD-3-Clause",
    "教程、模型/ORM、视图、表单、认证、测试、缓存、部署检查清单", stack="Django", order=20, expect={"min_docs": 300},
    use="教程通读，其余查询")
add("09D02", "09", "docs", "Flask 文档源与官方教程示例（pallets/flask）", "Pallets", "2026", "以标签为准（3.x）",
    D + "flask_docs_src_en.tar", git("pallets/flask", None, ["docs", "examples"]), "BSD-3-Clause",
    "应用工厂、蓝图、请求上下文、测试、部署；examples/tutorial 完整示例", stack="Flask", order=21, expect={"min_docs": 40},
    complete="部分", scope="docs/（Sphinx 源；API 页正文由 docstring 生成，未含）+ examples/")
add("09D03", "09", "docs", "HTTP 与 Web 认证核心 RFC 集", "IETF", "1997–2022", "RFC 9110/9111/9112/9113/9114/6749/7519/6455/8446",
    D + "ietf_http_auth_rfcs_en", pdfset(urls=[
        "https://www.rfc-editor.org/rfc/rfc9110.pdf", "https://www.rfc-editor.org/rfc/rfc9111.pdf",
        "https://www.rfc-editor.org/rfc/rfc9112.pdf", "https://www.rfc-editor.org/rfc/rfc9113.pdf",
        "https://www.rfc-editor.org/rfc/rfc9114.pdf", "https://www.rfc-editor.org/rfc/rfc8446.txt",
        "https://www.rfc-editor.org/rfc/rfc6749.txt", "https://www.rfc-editor.org/rfc/rfc7519.txt",
        "https://www.rfc-editor.org/rfc/rfc6455.txt"], min_files=9),
    "IETF Trust（RFC 可自由复制）", "HTTP 语义/缓存/1.1/2/3、TLS 1.3、OAuth 2.0、JWT、WebSocket 标准原文", level="进阶",
    order=22, use="按需查询", cross=["11", "16"])
add("09D04", "09", "docs", "OpenAPI Specification（含 3.1/3.2 版本全文）", "OpenAPI Initiative", "2025", "main 提交",
    D + "openapi_specification_main_en.tar", git("OAI/OpenAPI-Specification", None, ["versions", "src"]), "Apache-2.0",
    "接口描述规范：路径、模式、安全方案、回调", stack="OpenAPI", order=23, expect={"min_docs": 5}, use="按需查询")
add("09D05", "09", "docs", "Celery 文档源（异步任务队列）", "Celery 项目", "2026", "main 提交", D + "celery_docs_src_en.tar",
    git("celery/celery", None, ["docs", "examples"]), "BSD-3-Clause", "任务、Worker、调度、路由、重试与监控", level="进阶",
    stack="Celery", order=24, expect={"min_docs": 60}, complete="部分", scope="docs/（Sphinx 源；API 参考由 docstring 生成，未含）+ examples/")
add("09X01", "09", "practice", "RealWorld（Conduit）API 规范与测试", "RealWorld 社区", "2025", "main 提交", X + "realworld_spec_main_en.tar",
    git("gothinkster/realworld"), "MIT", "统一规范的博客应用后端/前端：认证、CRUD、分页、接口测试", prereq="任一后端框架",
    order=30, expect={"min_docs": 5}, cross=["10"])
add("09X02", "09", "practice", "Full Stack FastAPI Template（官方全栈模板）", "FastAPI（Sebastián Ramírez）", "2026", "master 提交",
    X + "fastapi_full_stack_template_master_en.tar", git("fastapi/full-stack-fastapi-template"), "MIT",
    "FastAPI + SQLModel + PostgreSQL + React + Docker Compose + 测试 + CI 的参考实现", level="进阶", prereq="Python、Docker",
    stack="FastAPI/React/Docker", order=31, expect={"min_docs": 5}, cross=["10", "14"])

# ============================================================== 10 frontend
add("10B01", "10", "book", "Eloquent JavaScript (4th ed.)", "Marijn Haverbeke", "2024", "4th ed.", B + "Haverbeke_EloquentJavaScript_4thEd_en.pdf",
    pdf("https://eloquentjavascript.net/Eloquent_JavaScript.pdf"), "CC BY-NC 3.0", "JavaScript 语言、DOM、事件、异步、Node.js 与项目",
    prereq="无", stack="JavaScript", order=1, expect={"title_words": ["Marijn", "Haverbeke"], "min_pages": 300})
add("10B02", "10", "book", "You Don't Know JS Yet (2nd ed.)", "Kyle Simpson", "2020", "2nd ed. 分支提交", B + "Simpson_YouDontKnowJSYet_2ndEd_src_en.tar",
    git("getify/You-Dont-Know-JS"), "CC BY-NC-ND 4.0", "作用域、闭包、对象与类、类型系统的深入理解", level="进阶",
    prereq="JavaScript 基础", stack="JavaScript", order=2, expect={"min_docs": 10})
add("10B03", "10", "book", "TypeScript Deep Dive", "Basarat Ali Syed", "2023", "master 提交", B + "Basarat_TypeScriptDeepDive_src_en.tar",
    git("basarat/typescript-book"), "CC BY 4.0（以仓库为准）", "TypeScript 类型系统、配置、工程实践与常见坑", level="进阶",
    prereq="JavaScript", stack="TypeScript", order=3, expect={"min_docs": 50})
add("10C01", "10", "course", "University of Helsinki Full Stack Open 课程正文（英文）", "Matti Luukkainen 等", "2025", "source 分支提交",
    C + "Helsinki_FullStackOpen_src_en.tar", git("fullstack-hy2020/fullstack-hy2020.github.io", None, ["src/content"]),
    "CC BY-NC-SA 3.0", "React、状态管理、Node.js/Express REST API、测试、用户管理、GraphQL、TypeScript、CI/CD、容器、关系数据库",
    school="University of Helsinki", prereq="JavaScript 基础", stack="React/Node/TypeScript",
    material="完整课程正文 + 练习说明（多语言源，保留上游结构）", order=10, expect={"min_docs": 100}, cross=["09", "14"])
add("10C02", "10", "course", "MIT 6.4500 Design for the Web: Languages and User Interfaces（课程站点）", "Lea Verou, David Karger",
    "2026", "当前学期站点（页面为准）", C + "MIT_6.4500_DesignForTheWeb_html_en.tar",
    mirror("https://designftw.mit.edu/", quota=300, level="3", reject_regex=r"/go/"), "课程网站公开（版权保留）",
    "HTML/CSS/JS、可用性、可访问性、响应式与组件化 UI 设计；讲次页、作业与工作室练习", school="MIT", level="进阶",
    prereq="编程基础", material="讲次页面/幻灯（HTML）+ 作业说明 + 资源页", order=11, expect={"min_docs": 20, "max_broken": 0.15})
add("10D01", "10", "docs", "MDN Web Docs 内容源（HTML、CSS、JavaScript、HTTP、可访问性、Learn）", "Mozilla 与贡献者", "2026", "main 提交",
    D + "mdn_content_web_core_main_src_en.tar",
    git("mdn/content", None, ["files/en-us/web/html", "files/en-us/web/css", "files/en-us/web/javascript", "files/en-us/web/http",
                              "files/en-us/web/accessibility", "files/en-us/learn_web_development"]),
    "CC BY-SA 2.5（文档）/ CC0（代码示例）", "Web 平台权威参考与学习区教程", stack="HTML/CSS/JS", order=20, expect={"min_docs": 3000},
    use="学习区通读，其余查询", complete="部分", scope="仅 HTML/CSS/JS/HTTP/可访问性/Learn 六个子树（Web API 子树体量过大未收）")
add("10D02", "10", "docs", "TypeScript Handbook 与参考文档源", "Microsoft", "2026", "v2 分支提交", D + "typescript_handbook_src_en.tar",
    git("microsoft/TypeScript-Website", "v2", ["packages/documentation/copy/en"]), "CC BY 4.0（文档）",
    "TypeScript 手册、参考、tsconfig、声明文件", stack="TypeScript", order=21, expect={"min_docs": 80})
add("10D03", "10", "docs", "React 官方文档源（react.dev）", "Meta 与贡献者", "2026", "main 提交", D + "react_dev_docs_main_src_en.tar",
    git("reactjs/react.dev", None, ["src/content/learn", "src/content/reference"]), "CC BY 4.0",
    "组件、状态、Effect、Hooks 参考、服务端组件", stack="React", order=22, expect={"min_docs": 150})
add("10D04", "10", "docs", "WAI-ARIA Authoring Practices Guide（APG）源", "W3C WAI", "2026", "main 提交", D + "w3c_aria_practices_main_en.tar",
    git("w3c/aria-practices", None, ["content"]), "W3C Software and Document License", "可访问组件模式与键盘交互示例",
    level="进阶", stack="HTML/ARIA", order=23, expect={"min_docs": 50}, use="按需查询")
add("10D05", "10", "docs", "D3.js 官方文档源", "Mike Bostock / Observable", "2026", "main 提交", D + "d3_docs_main_src_en.tar",
    git("d3/d3", None, ["docs"]), "ISC", "数据驱动文档：比例尺、坐标轴、形状、交互与过渡", stack="D3", order=24,
    expect={"min_docs": 30}, cross=["03"])
add("10X01", "10", "practice", "TodoMVC（同一应用的多框架实现）", "TodoMVC 社区", "2025", "master 提交", X + "todomvc_master_en.tar",
    git("tastejs/todomvc"), "MIT", "对比不同前端框架的组件、状态管理与测试", prereq="JavaScript", order=30, expect={"min_docs": 5})
add("10X02", "10", "practice", "The Odin Project 课程与项目说明（curriculum）", "The Odin Project", "2026", "main 提交",
    X + "theodinproject_curriculum_main_en.tar", git("TheOdinProject/curriculum"), "CC BY-NC-SA 4.0",
    "HTML/CSS/JS/React/Node 的项目驱动练习与评审标准", prereq="无", order=31, expect={"min_docs": 200})

# ============================================================== 11 systems & networks
add("11B01", "11", "book", "Operating Systems: Three Easy Pieces", "Remzi H. Arpaci-Dusseau, Andrea C. Arpaci-Dusseau", "2023", "v1.10",
    B + "ArpaciDusseau_OSTEP_v1.10_chapters_en",
    pdfset(index="https://pages.cs.wisc.edu/~remzi/OSTEP/", pattern=r"OSTEP/[a-z0-9-]+\.pdf$", min_files=45),
    "作者免费分发（版权保留）", "虚拟化（进程、调度、内存）、并发（线程、锁、条件变量）、持久化（文件系统）", prereq="C 基础",
    school="University of Wisconsin–Madison", order=1, scope="按官网目录逐章下载全部章节 PDF（整本计一次）", cross=["12"])
add("11B02", "11", "book", "Dive into Systems", "Suzanne J. Matthews, Tia Newhall, Kevin C. Webb", "2022", "online",
    B + "Matthews_DiveIntoSystems_html_en.tar", mirror("https://diveintosystems.org/book/index.html", include=["/book"], quota=200),
    "CC BY-NC-ND 4.0", "C、二进制表示、汇编、存储层次、OS、共享内存并行", prereq="编程基础", order=2, expect={"min_docs": 100}, cross=["12"])
add("11B03", "11", "book", "Computer Networks: A Systems Approach", "Larry Peterson, Bruce Davie", "2023", "6.2（master 提交）",
    B + "Peterson_ComputerNetworksSystemsApproach_src_en.tar", git("SystemsApproach/book"), "CC BY 4.0",
    "分层、以太网与无线、IP 与路由、TCP/拥塞控制、应用协议", level="进阶", prereq="编程基础", order=3, expect={"min_docs": 30})
add("11B04", "11", "book", "The Little Book of Semaphores", "Allen B. Downey", "2016", "2.2.1", B + "Downey_LittleBookOfSemaphores_2.2.1_en.pdf",
    pdf("https://greenteapress.com/semaphores/LittleBookOfSemaphores.pdf"), "CC BY-NC-SA 4.0", "同步原语与经典并发问题练习",
    prereq="线程基础", order=4, expect={"title_words": ["Little", "Book", "Semaphores"], "min_pages": 250})
add("11B05", "11", "book", "Beej's Guide to Network Programming", "Brian \"Beej Jorgensen\" Hall", "2025", "当前版（PDF 内为准）",
    B + "Hall_BeejsGuideNetworkProgramming_en.pdf", pdf("https://beej.us/guide/bgnet/pdf/bgnet_usl_c_1.pdf"), "CC BY-NC-ND 3.0",
    "BSD 套接字、TCP/UDP 客户端/服务器、select/poll、非阻塞 I/O", prereq="C 基础", stack="C/POSIX", order=5,
    expect={"title_words": ["Beej", "Network", "Programming"], "min_pages": 80}, cross=["12"])
add("11C01", "11", "course", "MIT 6.1810 Operating System Engineering (Fall 2025) xv6 教材与实验", "Frans Kaashoek, Robert Morris 等", "2025",
    "Fall 2025", C + "MIT_6.1810_Fall2025_Materials_html_en.tar",
    mirror("https://pdos.csail.mit.edu/6.1810/2025/schedule.html", include=["/6.1810/2025"], quota=200, level="2"),
    "课程网站公开（xv6 MIT 许可）", "xv6 教材、讲义、实验（syscall、页表、trap、COW、多线程、网络驱动、锁、文件系统、mmap）",
    school="MIT", level="进阶", prereq="C、体系结构基础", material="xv6 book + 课堂讲义 + 实验说明（视频未下载）", order=10,
    expect={"min_docs": 20})
add("11C02", "11", "course", "CMU 15-213/18-213 Introduction to Computer Systems 课件与讲义", "CMU 15-213 Staff", "2025", "当前学期页面",
    C + "CMU_15213_Slides_en", pdfset(index="https://www.cs.cmu.edu/~213/schedule.html", pattern=r"\.pdf$", min_files=20),
    "课程网站公开（版权保留）", "数据表示、机器级程序、存储层次、链接、异常控制流、虚拟内存、网络与并发编程", school="Carnegie Mellon University",
    prereq="C 基础", material="课件 PDF（实验见 11X03 CS:APP labs）", order=11, cross=["12"])
add("11D01", "11", "docs", "互联网核心协议 RFC 集（IP、TCP、UDP、DNS、QUIC）", "IETF", "1980–2022", "RFC 791/768/9293/1034/1035/9000/8200",
    D + "ietf_core_internet_rfcs_en", pdfset(urls=[
        "https://www.rfc-editor.org/rfc/rfc791.txt", "https://www.rfc-editor.org/rfc/rfc768.txt",
        "https://www.rfc-editor.org/rfc/rfc9293.pdf", "https://www.rfc-editor.org/rfc/rfc1034.txt",
        "https://www.rfc-editor.org/rfc/rfc1035.txt", "https://www.rfc-editor.org/rfc/rfc9000.pdf",
        "https://www.rfc-editor.org/rfc/rfc8200.txt"], min_files=7), "IETF Trust", "网络协议标准原文",
    level="进阶", order=20, use="按需查询")
add("11D02", "11", "docs", "Linux 内核官方文档（Documentation/ 源）", "Linux kernel community", "2026", "master 提交（版本见 Makefile）",
    D + "linux_kernel_documentation_master_src_en.tar", git("torvalds/linux", None, ["Documentation"]), "GPL-2.0（文档以各文件声明为准）",
    "进程调度、内存管理、文件系统、网络、cgroup、管理指南、开发流程", level="进阶-高级", prereq="操作系统基础", order=21,
    expect={"min_docs": 2000, "need_license": False, "must_have": ["Documentation/admin-guide/"]}, use="按需查询",
    note="仓库根 COPYING 不在稀疏范围内时以 LICENSES/ 与各文件 SPDX 头为准")
add("11X02", "11", "practice", "xv6-riscv（MIT 教学操作系统源码）", "MIT PDOS", "2025", "riscv 分支提交", X + "mit_xv6_riscv_en.tar",
    git("mit-pdos/xv6-riscv"), "MIT", "约 6000 行可读的 Unix v6 RISC-V 实现", level="进阶", prereq="C、RISC-V 基础", order=31,
    expect={"min_docs": 0})
add("11X03", "11", "practice", "CS:APP 3e 自学实验包（Data/Bomb/Attack/Cache/Shell/Malloc/Proxy Lab 讲义与自学包）", "Randal E. Bryant, David R. O'Hallaron",
    "2016–2023", "官网当前版本", X + "csapp_3e_selfstudy_labs_en.tar",
    mirror("https://csapp.cs.cmu.edu/3e/labs.html", include=["/3e", "/im"], quota=200, level="1"),
    "作者为自学公开（版权保留）", "位运算、逆向、缓冲区溢出、缓存模拟、Shell、内存分配器、代理服务器", level="进阶",
    prereq="C、15-213 课件", order=32, expect={"min_docs": 2}, cross=["12"],
    note="下载 labs.html 页面直接链接的讲义 PDF 与 self-study tar（不运行）")
add("11X04", "11", "practice", "Nand2Tetris 软件与项目包", "Noam Nisan, Shimon Schocken", "2024", "官网当前包",
    X + "nand2tetris_projects_en", pdfset(index="https://www.nand2tetris.org/project01", pattern=r"\.pdf$", min_files=1),
    "CC BY-NC-SA 3.0", "从逻辑门到计算机、汇编器、虚拟机、编译器与 OS 的 12 个项目说明", prereq="无", order=33,
    complete="部分", scope="项目说明 PDF；官方 IDE 软件包未下载（属工具构建产物）")

# ============================================================== 12 C/C++ & performance
add("12B01", "12", "book", "Modern C", "Jens Gustedt", "2019", "2nd ed.（HAL 免费版）", B + "Gustedt_ModernC_2019_en.pdf",
    pdf("https://inria.hal.science/hal-02383654/document"), "CC BY-NC-ND 4.0", "C17 语言、内存模型、指针、并发与性能习惯",
    level="入门-进阶", prereq="编程基础", stack="C17", order=1, expect={"title_words": ["Modern", "C"], "min_pages": 250},
    note="第 3 版（2024, C23）为出版社商业版，未收录")
add("12B02", "12", "book", "Beej's Guide to C Programming", "Brian \"Beej Jorgensen\" Hall", "2025", "当前版", B + "Hall_BeejsGuideCProgramming_en.pdf",
    pdf("https://beej.us/guide/bgc/pdf/bgc_usl_c_1.pdf"), "CC BY-NC-ND 3.0", "C 语言教程与库参考", prereq="编程基础", stack="C",
    order=2, expect={"title_words": ["Beej", "C", "Programming"], "min_pages": 300})
add("12B03", "12", "book", "Performance Analysis and Tuning on Modern CPUs (2nd ed.)", "Denis Bakhvalov", "2024", "2nd ed.",
    B + "Bakhvalov_PerformanceAnalysisTuningModernCPUs_2ndEd_en.pdf",
    pdf("https://github.com/dendibakh/perf-book/releases/download/2.0_release/PerformanceAnalysisAndTuningOnModernCPUs_SecondEdition.pdf"),
    "CC BY 4.0（以书内声明为准）", "性能测量、PMU、Top-Down 分析、前端/后端/内存瓶颈优化", level="进阶-高级", prereq="C/C++、体系结构",
    stack="perf/VTune", order=3, expect={"title_words": ["Performance", "Analysis", "Tuning"], "min_pages": 250})
add("12B04", "12", "book", "What Every Programmer Should Know About Memory", "Ulrich Drepper", "2007", "1.0", B + "Drepper_WhatEveryProgrammerShouldKnowAboutMemory_2007_en.pdf",
    pdf("https://people.freebsd.org/~lstewart/articles/cpumemory.pdf"), "作者公开（经典）", "缓存、TLB、NUMA、预取与内存访问优化",
    level="进阶", prereq="C、体系结构", order=4, expect={"title_words": ["Every", "Programmer", "Memory"], "min_pages": 100})
add("12B05", "12", "book", "Algorithms for Modern Hardware", "Sergey Slotin", "2022", "online（en.algorithmica.org/hpc）",
    B + "Slotin_AlgorithmsForModernHardware_html_en.tar", mirror("https://en.algorithmica.org/hpc/", include=["/hpc"], quota=200),
    "CC BY-NC 4.0", "SIMD、缓存友好数据结构、分支预测、性能剖析与编译器优化", level="进阶-高级", prereq="C++", order=5,
    expect={"min_docs": 60}, cross=["02"])
add("12B06", "12", "book", "How To Write Shared Libraries", "Ulrich Drepper", "2011", "4.1.2", B + "Drepper_HowToWriteSharedLibraries_2011_en.pdf",
    pdf("https://www.akkadia.org/drepper/dsohowto.pdf"), "作者公开", "ELF、动态链接、符号可见性、重定位与 ABI", level="高级",
    prereq="C、链接基础", order=6, use="按需查询", expect={"title_words": ["Shared", "Libraries"], "min_pages": 40})
add("12C01", "12", "course", "MIT 6.172 Performance Engineering of Software Systems (Fall 2018) OCW 课程包", "Charles Leiserson, Julian Shun",
    "2018", "Fall 2018", C + "MIT_6.172_Fall2018_OCW_en.zip",
    file("https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/6.172-fall-2018.zip"),
    "CC BY-NC-SA 4.0", "位技巧、缓存、向量化、多线程（Cilk）、性能剖析与项目", school="MIT", level="进阶", prereq="C、算法",
    material="课件+讲义+作业/项目说明（OCW 包）", order=10, expect={"min_docs": 20}, cross=["13"])
add("12C02", "12", "course", "Stanford CS 107 Computer Organization & Systems 指南与讲义", "CS 107 Course Staff", "2026", "cs107.1272 学期站点（课程主页当前指向）",
    C + "Stanford_CS107_Guides_html_en.tar", mirror("https://web.stanford.edu/class/archive/cs/cs107/cs107.1272/", include=["/class/archive/cs/cs107/cs107.1272"], quota=300, level="3"),
    "课程网站公开（版权保留）", "C、指针与内存、泛型、汇编、堆分配器；gdb/valgrind/make 指南", school="Stanford", prereq="编程基础",
    material="课程指南（guides）+ 讲义页 + 作业说明", order=11, expect={"min_docs": 15}, cross=["11"])
add("12D01", "12", "docs", "GCC 16.2 手册（PDF）", "Free Software Foundation", "2026", "16.2.0", D + "gcc_16.2.0_manual_en.pdf",
    pdf("https://gcc.gnu.org/onlinedocs/gcc-16.2.0/gcc.pdf"), "GFDL", "编译选项、优化、扩展、内建函数", stack="GCC", order=20,
    use="按需查询", expect={"title_words": ["GCC"], "min_pages": 500})
add("12D02", "12", "docs", "GNU Make Manual", "Free Software Foundation", "2025", "当前版", D + "gnu_make_manual_en.pdf",
    pdf("https://www.gnu.org/software/make/manual/make.pdf"), "GFDL", "规则、变量、函数、递归构建", stack="Make", order=21,
    use="按需查询", expect={"title_words": ["GNU", "make"], "min_pages": 150})
add("12D03", "12", "docs", "GDB 手册（Debugging with GDB）", "Free Software Foundation", "2026", "current", D + "gdb_manual_en.pdf",
    pdf("https://sourceware.org/gdb/current/onlinedocs/gdb.pdf"), "GFDL", "断点、栈、多线程、远程调试、Python 扩展", stack="GDB",
    order=22, use="按需查询", expect={"title_words": ["Debugging", "GDB"], "min_pages": 500})
add("12D04", "12", "docs", "CMake 帮助文档源（含官方教程 Help/guide）", "Kitware", "2026", "以最新 v4.x 标签为准",
    D + "cmake_help_src_en.tar", git("https://gitlab.kitware.com/cmake/cmake.git", None, ["Help"]), "BSD-3-Clause",
    "CMake 教程、命令、变量、属性、模块与工具链参考（reStructuredText 源）", stack="CMake", order=23, expect={"min_docs": 500},
    use="教程通读，其余查询")
add("12D05", "12", "docs", "C++ Core Guidelines", "Bjarne Stroustrup, Herb Sutter（编）", "2026", "master 提交",
    D + "isocpp_cpp_core_guidelines_master_en.tar", git("isocpp/CppCoreGuidelines"), "MIT-style（见 LICENSE）",
    "资源管理、接口、类、并发、性能的现代 C++ 规则", level="进阶", stack="C++", order=24, expect={"min_docs": 1})
add("12D06", "12", "docs", "pybind11 文档源与示例", "pybind11 开发者", "2026", "以标签为准", D + "pybind11_docs_src_en.tar",
    git("pybind/pybind11", None, ["docs"]), "BSD-3-Clause", "C++ 与 Python 互操作：函数/类绑定、类型转换、GIL、构建", level="进阶",
    stack="C++/Python", order=25, expect={"min_docs": 30}, cross=["01"])
add("12D07", "12", "docs", "Cython 文档源", "Cython 开发者", "2026", "master 提交", D + "cython_docs_src_en.tar",
    git("cython/cython", None, ["docs"]), "Apache-2.0", "Cython 语言、类型化内存视图、并行、包装 C 库", level="进阶",
    stack="Cython", order=26, expect={"min_docs": 50}, cross=["01", "03"])
add("12X01", "12", "practice", "perf-ninja（性能优化动手实验）", "Denis Bakhvalov", "2024", "main 提交", X + "dendibakh_perf_ninja_main_en.tar",
    git("dendibakh/perf-ninja"), "以仓库为准", "配合 perf-book 的缓存、向量化、分支、内存优化实验", level="进阶",
    prereq="C++", order=30, expect={"min_docs": 10})
add("12X02", "12", "practice", "pybind11 python_example（扩展模块构建示例）", "pybind11 开发者", "2025", "master 提交",
    X + "pybind_python_example_master_en.tar", git("pybind/python_example"), "BSD-3-Clause", "setuptools/pyproject 构建 C++ 扩展的最小完整工程",
    level="进阶", prereq="C++、Python 打包", order=31, expect={"min_docs": 1})

# ============================================================== 13 GPU & parallel
add("13B01", "13", "book", "Is Parallel Programming Hard, And, If So, What Can You Do About It?", "Paul E. McKenney", "2026",
    "2026.06.21a", B + "McKenney_IsParallelProgrammingHard_2026.06.21a_en.pdf",
    pdf("https://mirrors.edge.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.2026.06.21a.pdf",
        "https://kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.2026.06.21a.pdf"), "CC BY-SA 3.0",
    "共享内存并行：计数、锁、RCU、内存序、形式化验证", level="高级", prereq="C、操作系统", order=1, cross=["11"],
    expect={"title_words": ["Parallel", "Programming", "Hard"], "min_pages": 500})
add("13B02", "13", "book", "Introduction to High Performance Scientific Computing（The Art of HPC 卷 1）", "Victor Eijkhout", "2022",
    "3rd ed.（仓库提交）", B + "Eijkhout_IntroductionHPC_vol1_en.pdf",
    pdf("https://raw.githubusercontent.com/victorEijkhout/TheArtofHPC_pdfs/main/vol1/EijkhoutIntroToHPC.pdf"), "CC BY 4.0",
    "体系结构、浮点、并行计算模型、负载均衡、数值线性代数", level="进阶", prereq="C/Fortran、线性代数", school="TACC, UT Austin",
    order=2, expect={"title_words": ["High", "Performance", "Scientific", "Computing"], "min_pages": 400})
add("13B03", "13", "book", "Parallel Programming for Science and Engineering（The Art of HPC 卷 2：MPI/OpenMP）", "Victor Eijkhout", "2022",
    "仓库提交", B + "Eijkhout_ParallelProgramming_vol2_en.pdf",
    pdf("https://raw.githubusercontent.com/victorEijkhout/TheArtofHPC_pdfs/main/vol2/EijkhoutParallelProgramming.pdf"), "CC BY 4.0",
    "MPI 点对点/集合通信、OpenMP、混合并行的完整教程", level="进阶", prereq="C/C++", school="TACC, UT Austin", order=3,
    expect={"title_words": ["Parallel", "Programming"], "min_pages": 400})
add("13B04", "13", "book", "How to Scale Your Model: A Systems View of LLMs on TPUs", "Jacob Austin 等（Google DeepMind）", "2025", "online（仓库提交）",
    B + "Austin_HowToScaleYourModel_src_en.tar", git("jax-ml/scaling-book"), "以仓库为准",
    "Roofline、分片、数据/张量/流水并行、Transformer 训练与推理的算力-通信分析", level="高级", prereq="深度学习、JAX/PyTorch",
    order=4, expect={"min_docs": 10}, cross=["05", "14"])
add("13C01", "13", "course", "Stanford CS149 Parallel Computing (Fall 2025) 课件", "Kayvon Fatahalian, Kunle Olukotun", "2025", "Fall 2025",
    C + "Stanford_CS149_Fall2025_Slides_en", pdfset(index="https://gfxcourses.stanford.edu/cs149/fall25/lecture/",
                                                   pattern=r"/cs149/fall25content/media/.*\.pdf$", min_files=10) | {"follow": r"/cs149/fall25/lecture/[a-z0-9_-]+/$"},
    "课程网站公开（版权保留）", "多核/SIMD、ISPC、CUDA、同步、缓存一致性、DSL 与硬件加速", school="Stanford", level="进阶",
    prereq="C/C++、体系结构", material="课件 PDF（编程作业见 13X10）", order=10)
add("13C02", "13", "course", "University of Oxford CUDA Programming Course（讲义与实践包）", "Mike Giles, Wes Armour", "2025", "当前版",
    C + "Oxford_CUDA_Course_en", pdfset(index="https://people.maths.ox.ac.uk/gilesm/cuda/", pattern=r"people\.maths\.ox\.ac\.uk/gilesm/cuda/.*\.pdf$", min_files=6),
    "课程网站公开（版权保留）", "CUDA 执行模型、内存层次、规约、库、多 GPU 与性能分析", school="University of Oxford", level="进阶",
    prereq="C/C++", material="讲义 PDF + 练习说明 PDF", order=11)
add("13D10", "13", "docs", "OpenMP API Specification 6.0", "OpenMP ARB", "2024", "6.0", D + "openmp_api_spec_6.0_en.pdf",
    pdf("https://www.openmp.org/wp-content/uploads/OpenMP-API-Specification-6-0.pdf", max_mb=100), "OpenMP ARB 版权（允许复制）",
    "共享内存并行指令、任务、设备卸载规范", level="高级", stack="OpenMP", order=20, use="按需查询",
    expect={"title_words": ["OpenMP", "Application", "Programming", "Interface"], "min_pages": 500})
add("13D11", "13", "docs", "MPI: A Message-Passing Interface Standard 4.1", "MPI Forum", "2023", "4.1", D + "mpi_4.1_standard_en.pdf",
    pdf("https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report.pdf"), "MPI Forum（允许复制）", "消息传递标准全文", level="高级",
    stack="MPI", order=21, use="按需查询", expect={"title_words": ["MPI", "Message", "Passing"], "min_pages": 800}, cross=["14"])
add("13X01", "13", "practice", "llm.c（纯 C/CUDA 的 GPT-2 训练实现）", "Andrej Karpathy", "2024", "master 提交", X + "karpathy_llm_c_master_en.tar",
    git("karpathy/llm.c"), "MIT", "手写 CUDA 内核、混合精度、多 GPU（NCCL）训练循环", level="高级", prereq="C、CUDA、Transformer",
    order=30, expect={"min_docs": 1}, cross=["05"])
add("13X02", "13", "practice", "GPU MODE lectures（讲座笔记本与代码）", "GPU MODE 社区", "2025", "main 提交", X + "gpu_mode_lectures_main_en.tar",
    git("gpu-mode/lectures"), "以仓库为准", "CUDA、Triton、性能剖析、量化与注意力内核的讲座代码", level="进阶", prereq="CUDA/PyTorch",
    order=31, expect={"min_docs": 10})
add("13X10", "13", "practice", "Stanford CS149 编程作业（asst1–asst4 公开仓库）", "Stanford CS149 Staff", "2025", "各仓库默认分支提交",
    X + "stanford_cs149_assignments_en",
    {"kind": "multi_git", "repos": ["https://github.com/stanford-cs149/asst1", "https://github.com/stanford-cs149/asst2",
                                    "https://github.com/stanford-cs149/asst3"]},
    "以各仓库为准", "SIMD/多线程（asst1）、任务调度（asst2）、CUDA 渲染器（asst3）；asst4 无公开仓库", level="进阶", prereq="C++、CUDA", order=32)

# ============================================================== 14 distributed & deployment
add("14B01", "14", "book", "Site Reliability Engineering: How Google Runs Production Systems", "Betsy Beyer 等（编）", "2016", "online",
    B + "Beyer_SiteReliabilityEngineering_html_en.tar", mirror("https://sre.google/sre-book/table-of-contents/", include=["/sre-book", "/img", "/css"],
                                                               quota=200, no_parent=False), "CC BY-NC-ND 4.0",
    "SLO、错误预算、监控、事故响应、发布工程、负载均衡与过载", level="进阶", prereq="系统基础", order=1, expect={"min_docs": 30})
add("14B02", "14", "book", "The Site Reliability Workbook", "Betsy Beyer 等（编）", "2018", "online", B + "Beyer_SiteReliabilityWorkbook_html_en.tar",
    mirror("https://sre.google/workbook/table-of-contents/", include=["/workbook", "/img", "/css"], quota=200, no_parent=False), "CC BY-NC-ND 4.0",
    "SLO 实施、告警、值班、配置管理、金丝雀发布的实践案例", level="进阶", prereq="SRE 基础", order=2, expect={"min_docs": 20})
add("14B03", "14", "book", "Notes on Theory of Distributed Systems", "James Aspnes", "2025", "Yale CPSC 465 notes（PDF 内日期为准）",
    B + "Aspnes_NotesTheoryDistributedSystems_en.pdf", pdf("https://www.cs.yale.edu/homes/aspnes/classes/465/notes.pdf"),
    "作者公开（CC BY-SA，以文内为准）", "消息传递模型、共识、FLP、故障检测、共享内存与随机化算法", level="高级", prereq="算法",
    school="Yale", order=3, expect={"title_words": ["Theory", "Distributed", "Systems"], "min_pages": 300})
add("14B04", "14", "book", "Distributed Systems for Fun and Profit", "Mikito Takada", "2013", "online ebook", B + "Takada_DistributedSystemsForFunAndProfit_html_en.tar",
    mirror("https://book.mixu.net/distsys/ebook.html", include=["/distsys"], quota=30, level="1"), "CC BY-NC-SA 3.0",
    "可扩展性、时间与顺序、复制、一致性模型的简明入门", prereq="无", order=4, expect={"min_docs": 1})
add("14C01", "14", "course", "MIT 6.5840 Distributed Systems (Spring 2026) 讲义与实验", "Robert Morris, Frans Kaashoek 等", "2026", "Spring 2026",
    C + "MIT_6.5840_Spring2026_Materials_html_en.tar",
    mirror("https://pdos.csail.mit.edu/6.824/schedule.html", include=["/6.824"], quota=300, level="2",
           reject_regex=r"\.(mp4|webm)$"),
    "课程网站公开（版权保留）", "MapReduce、Raft、线性一致性、分片 KV、Spanner、Zookeeper 等论文讲义与 Go 实验说明",
    school="MIT", level="进阶", prereq="Go、操作系统", material="课堂讲义（txt/pdf）+ 论文 + 实验说明（视频未下载）", order=10,
    expect={"min_docs": 30, "max_broken": 0.45}, complete="部分",
    scope="课程日程页两层链接内的讲义、论文与实验说明；日程以外页面引用的旧学期论文未下载（链接抽样断链约 40%）")
add("14C02", "14", "course", "University of Cambridge Concurrent and Distributed Systems 讲义", "Martin Kleppmann, David Greaves 等",
    "2024", "2024–25", C + "Cambridge_ConcDisSys_2024_DistSysNotes_en.pdf",
    pdf("https://www.cl.cam.ac.uk/teaching/2425/ConcDisSys/dist-sys-notes.pdf"), "课程网站公开（CC BY-SA，以文内为准）",
    "时钟、广播、复制、共识（Raft）、一致性模型与 CRDT", school="University of Cambridge", level="进阶", prereq="并发基础",
    material="讲义 PDF", order=11, expect={"title_words": ["Distributed", "Systems"], "min_pages": 50})
add("14C03", "14", "course", "Princeton COS 418 Distributed Systems (Fall 2025) 课件与习题课讲义", "Princeton COS 418 Staff",
    "2025", "Fall 2025", C + "Princeton_COS418_Fall2025_Slides_en",
    pdfset(index="https://www.cs.princeton.edu/courses/archive/fall25/cos418/schedule.html", pattern=r"/cos418/docs/.*\.pdf$", min_files=15) | {"max_missing": 3},
    "课程网站公开（版权保留）", "RPC、时钟、复制、Paxos/Raft、事务、一致性、拜占庭容错与大规模系统案例；Go 习题课", school="Princeton",
    level="进阶", prereq="Go、操作系统", material="讲课 PDF + 习题课（precept）PDF；作业代码未下载", order=12, complete="部分",
    scope="日程页链接的全部 PDF；其中课程站自身失效（404）的链接见 state/items/14C03.json 的 missing_upstream_404")
add("14D20", "14", "docs", "Prometheus 文档源（概念、查询、告警、最佳实践）", "Prometheus Authors (CNCF)", "2026", "main 提交",
    D + "prometheus_docs_main_src_en.tar", git("prometheus/docs", None, ["docs"]), "Apache-2.0",
    "指标类型、PromQL、记录/告警规则、导出器与仪表板实践", stack="Prometheus", order=20, expect={"min_docs": 30})
add("14D21", "14", "docs", "OpenTelemetry 文档源", "OpenTelemetry Authors (CNCF)", "2026", "main 提交", D + "opentelemetry_docs_main_src_en.tar",
    git("open-telemetry/opentelemetry.io", None, ["content/en/docs"]), "CC BY 4.0", "追踪、指标、日志信号；Collector；Python 等语言 SDK",
    stack="OpenTelemetry", order=21, expect={"min_docs": 200})
add("14D22", "14", "docs", "Helm 文档源", "Helm Authors (CNCF)", "2026", "main 提交", D + "helm_docs_main_src_en.tar",
    git("helm/helm-www", None, ["docs"]), "CC BY 4.0（以仓库为准）", "Chart 结构、模板、仓库与发布管理", stack="Helm", order=22,
    expect={"min_docs": 30})
add("14D23", "14", "docs", "KServe 文档源（Kubernetes 模型服务）", "KServe 社区", "2026", "main 提交", D + "kserve_website_main_src_en.tar",
    git("kserve/website", None, ["docs"]), "Apache-2.0", "InferenceService、模型存储、自动扩缩、推理协议与生成式模型服务",
    level="进阶", stack="KServe/Kubernetes", order=23, expect={"min_docs": 30})
add("14X10", "14", "practice", "Kubernetes The Hard Way", "Kelsey Hightower", "2025", "master 提交", X + "kubernetes_the_hard_way_master_en.tar",
    git("kelseyhightower/kubernetes-the-hard-way"), "Apache-2.0", "手动搭建集群：证书、etcd、控制平面、网络与冒烟测试", level="进阶",
    prereq="Linux、Kubernetes 基础", order=30, expect={"min_docs": 10})
add("14X11", "14", "practice", "The System Design Primer", "Donne Martin", "2024", "master 提交", X + "system_design_primer_master_en.tar",
    git("donnemartin/system-design-primer", None, ["README.md", "solutions", "LICENSE.txt"]), "CC BY 4.0",
    "缓存、负载均衡、数据库扩展、异步、可用性模式与设计练习题", level="进阶", order=31, expect={"min_docs": 5})
add("15B01", "15", "book", "Introduction to Information Retrieval", "Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze", "2008",
    "online reading edition", B + "Manning_IntroductionInformationRetrieval_2008_en.pdf",
    pdf("https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf"), "作者网站免费 PDF（版权保留）",
    "倒排索引、评分、评测指标、向量空间、聚类：RAG 检索的基础", level="进阶", prereq="线性代数、概率", school="Stanford",
    order=1, expect={"title_words": ["Introduction", "Information", "Retrieval"], "min_pages": 500})
add("15B02", "15", "book", "Speech and Language Processing (3rd ed. draft)", "Daniel Jurafsky, James H. Martin", "2026", "3rd ed. draft (Aug 2026)",
    B + "Jurafsky_SpeechAndLanguageProcessing_3rdEdDraft_aug26_en.pdf", pdf("https://web.stanford.edu/~jurafsky/slp3/ed3book_aug26.pdf", max_mb=100), "作者网站免费草稿", "LLM、提示、检索与 RAG、问答、评测章节",
    level="进阶", prereq="ML 基础", order=2, use="按需查询",
    expect={"title_words": ["Speech", "Language", "Processing"], "min_pages": 500})
add("15B03", "15", "book", "Foundations of Large Language Models", "Tong Xiao, Jingbo Zhu", "2025", "arXiv 版",
    B + "Xiao_FoundationsOfLargeLanguageModels_2025_en.pdf", pdf("https://arxiv.org/pdf/2501.09223"), "arXiv 非独占许可", "预训练、对齐、提示、推理与长上下文",
    level="进阶", prereq="深度学习", order=3, use="按需查询",
    expect={"title_words": ["Foundations", "Large", "Language", "Models"], "min_pages": 150})
add("15C01", "15", "course", "UC Berkeley CS294/194-196 Large Language Model Agents (Fall 2024) 课件", "Dawn Song, Xinyun Chen", "2024", "Fall 2024",
    C + "Berkeley_CS294_LLMAgents_Fall2024_Slides_en",
    pdfset(index="https://rdi.berkeley.edu/llm-agents/f24", pattern=r"\.pdf$", min_files=8), "课程网站公开（版权保留）",
    "推理、规划、工具使用、多智能体、代码智能体、安全", school="UC Berkeley", level="进阶", prereq="LLM 基础",
    material="课件 PDF（视频未下载）", order=10)
add("15C02", "15", "course", "UC Berkeley Advanced Large Language Model Agents (Spring 2025) 课件", "Dawn Song, Xinyun Chen, Kaiyu Yang",
    "2025", "Spring 2025", C + "Berkeley_AdvLLMAgents_Spring2025_Slides_en",
    pdfset(index="https://rdi.berkeley.edu/adv-llm-agents/sp25", pattern=r"\.pdf$", min_files=6), "课程网站公开（版权保留）",
    "推理时扩展、代码生成与验证、Web/计算机使用智能体、安全", school="UC Berkeley", level="高级", prereq="15C01",
    material="课件 PDF", order=11)
add("15C03", "15", "course", "Stanford CS336 Language Modeling from Scratch (Spring 2025) 讲义与作业", "Tatsunori Hashimoto, Percy Liang",
    "2025", "Spring 2025", C + "Stanford_CS336_Spring2025_src_en",
    {"kind": "multi_git", "repos": ["https://github.com/stanford-cs336/spring2025-lectures",
                                    "https://github.com/stanford-cs336/assignment1-basics",
                                    "https://github.com/stanford-cs336/assignment2-systems",
                                    "https://github.com/stanford-cs336/assignment3-scaling",
                                    "https://github.com/stanford-cs336/assignment4-data",
                                    "https://github.com/stanford-cs336/assignment5-alignment"]},
    "以各仓库为准", "分词器、Transformer、GPU 内核与分布式、扩展律、数据、对齐的从零实现", school="Stanford", level="高级",
    prereq="PyTorch、深度学习", material="可执行讲义源 + 作业框架与说明", order=12, cross=["05", "13"], complete="部分",
    scope="讲义仓库 + assignment1–4；assignment5-alignment 仓库无许可证文件未收录")
add("15D10", "15", "docs", "Model Context Protocol 规范与文档", "Model Context Protocol 项目（Anthropic 发起）", "2026", "main 提交",
    D + "mcp_specification_main_en.tar", git("modelcontextprotocol/modelcontextprotocol", None, ["docs", "schema"]), "MIT（以仓库为准）",
    "工具/资源/提示协议、传输、授权、各版本规范与 JSON Schema", level="进阶", stack="MCP", order=20, expect={"min_docs": 50})
add("15D11", "15", "docs", "Language Server Protocol 规范", "Microsoft", "2026", "gh-pages 提交（含 3.17/3.18 规范）",
    D + "lsp_specification_en.tar", git("microsoft/language-server-protocol", "gh-pages", ["_specifications"]), "CC BY 4.0 / MIT",
    "编辑器-语言服务器协议：诊断、补全、代码操作、工作区编辑（IDE 集成基础）", level="进阶", stack="LSP", order=21,
    expect={"min_docs": 10})
add("15D12", "15", "docs", "VS Code 扩展 API 文档源", "Microsoft", "2026", "main 提交", D + "vscode_extension_api_docs_src_en.tar",
    git("microsoft/vscode-docs", None, ["api"]), "CC BY 4.0", "扩展开发、语言特性、Webview、测试与发布（IDE 集成）", level="进阶",
    stack="VS Code", order=22, expect={"min_docs": 50})
add("15D13", "15", "docs", "DSPy 文档源", "Stanford NLP", "2026", "main 提交", D + "dspy_docs_main_src_en.tar", git("stanfordnlp/dspy", None, ["docs"]),
    "MIT", "声明式 LM 程序、模块、优化器与评测", level="进阶", stack="DSPy", order=23, expect={"min_docs": 30},
    complete="部分", scope="docs/ Markdown 源；API 页由 mkdocstrings 生成，未含")
add("15D14", "15", "docs", "OpenAI Agents SDK（Python）文档源与示例", "OpenAI", "2026", "main 提交", D + "openai_agents_python_docs_src_en.tar",
    git("openai/openai-agents-python", None, ["docs", "examples"]), "MIT", "智能体、工具、交接、护栏、追踪；examples 目录",
    level="进阶", stack="Python", order=24, expect={"min_docs": 30}, complete="部分", scope="docs/（ref/ 为 mkdocstrings 指令，API 正文未含）+ examples/")
add("15X01", "15", "practice", "Anthropic Claude Cookbooks", "Anthropic", "2026", "main 提交", X + "anthropic_claude_cookbooks_main_en.tar",
    git("anthropics/claude-cookbooks"), "MIT", "工具调用、RAG、上下文管理、评测、智能体模式的可运行笔记本", level="进阶",
    prereq="Python、LLM API", order=30, expect={"min_docs": 20})
add("15X02", "15", "practice", "OpenAI Cookbook", "OpenAI", "2026", "main 提交", X + "openai_cookbook_main_en.tar",
    git("openai/openai-cookbook", None, ["examples", "articles", "registry.yaml"]), "MIT", "嵌入检索、函数调用、评测、微调示例",
    level="进阶", prereq="Python、LLM API", order=31, expect={"min_docs": 50})
add("15X03", "15", "practice", "SWE-bench（代码智能体评测框架）", "Princeton NLP / SWE-bench 团队", "2026", "main 提交", X + "swe_bench_main_en.tar",
    git("SWE-bench/SWE-bench"), "MIT", "真实 GitHub issue 修复评测：容器化执行隔离、补丁评估", level="高级",
    prereq="Python、Docker", order=32, expect={"min_docs": 5}, cross=["16"])
add("15X04", "15", "practice", "mini-SWE-agent（约百行的参考代码智能体）", "SWE-agent 团队（Princeton/Stanford）", "2026", "main 提交",
    X + "mini_swe_agent_main_en.tar", git("SWE-agent/mini-swe-agent"), "MIT", "最小代码编辑智能体：bash 动作、环境隔离、轨迹与评测",
    level="进阶", prereq="Python", order=33, expect={"min_docs": 5})
add("15X05", "15", "practice", "Aider（终端 AI 结对编程工具源码）", "Paul Gauthier", "2026", "main 提交", X + "aider_main_en.tar",
    git("Aider-AI/aider"), "Apache-2.0", "代码库地图、编辑格式、Git 集成与 lint/test 循环的实现参考", level="高级", prereq="Python",
    order=34, expect={"min_docs": 20})
# ============================================================== 16 secure programming
add("16B01", "16", "book", "Building Secure and Reliable Systems", "Heather Adkins 等（Google）", "2020", "online", B + "Adkins_BuildingSecureReliableSystems_html_en.tar",
    mirror("https://google.github.io/building-secure-and-reliable-systems/raw/toc.html", include=["/building-secure-and-reliable-systems"],
           quota=150), "CC BY-NC-ND 4.0", "最小权限、设计安全、代码审查、测试、部署、事故响应", level="进阶", prereq="系统基础",
    order=1, expect={"min_docs": 20}, cross=["14"])
add("16B02", "16", "book", "Security Engineering (2nd ed.)", "Ross Anderson", "2008", "2nd ed.（作者网站全书免费）",
    B + "Anderson_SecurityEngineering_2ndEd_chapters_en",
    pdfset(index="https://www.cl.cam.ac.uk/archive/rja14/book.html", pattern=r"SEv2-[^/]*\.pdf$", min_files=20), "作者网站免费（版权保留）",
    "协议、访问控制、密码学应用、物理与网络安全、安全经济学", level="进阶", prereq="无", order=2,
    scope="作者网站第 2 版全部章节 PDF；第 3 版为出版社商业版未收", school="University of Cambridge")
add("16B03", "16", "book", "Secure Programming HOWTO", "David A. Wheeler", "2015", "3.72", B + "Wheeler_SecureProgrammingHOWTO_3.72_en.pdf",
    pdf("https://dwheeler.com/secure-programs/Secure-Programs-HOWTO.pdf"), "GFDL / GPL", "输入校验、缓冲区溢出、最小权限、输出编码、密码学误用",
    level="进阶", prereq="C 或任一语言", order=3, expect={"title_words": ["Secure", "Programming"], "min_pages": 150})
add("16B04", "16", "book", "The Cyber Security Body of Knowledge (CyBOK) v1.1", "CyBOK Project（University of Bristol 牵头）", "2021", "1.1.0",
    B + "CyBOK_v1.1.0_en.pdf", pdf("https://www.cybok.org/media/downloads/CyBOK_v1.1.0.pdf"), "Open Government Licence",
    "软件安全、Web 与移动安全、安全生命周期、认证授权、形式化方法等 21 个知识域", level="进阶", prereq="无", order=4,
    use="按需查询", expect={"title_words": ["Cyber", "Security", "Body", "Knowledge"], "min_pages": 800})
add("16C01", "16", "course", "Stanford CS 253 Web Security 课件", "Feross Aboukhadijeh", "2025", "当前版", C + "Stanford_CS253_Slides_en",
    pdfset(index="https://web.stanford.edu/class/cs253/", pattern=r"/class/cs253/lectures/.*\.pdf$", min_files=10), "课程网站公开（版权保留）",
    "同源策略、XSS、CSRF、CSP、Cookie、认证、HTTPS、注入与 Web 安全模型", school="Stanford", level="进阶", prereq="Web 基础",
    material="课件 PDF", order=10, cross=["09", "10"])
add("16C02", "16", "course", "UC Berkeley CS 161 Computer Security 教材（textbook.cs161.org）", "CS 161 Course Staff", "2025", "online",
    C + "Berkeley_CS161_Textbook_html_en.tar", mirror("https://textbook.cs161.org/", quota=100), "课程网站公开（版权保留）",
    "内存安全、密码学、Web 安全、网络安全的课程教材", school="UC Berkeley", prereq="C、网络基础", material="课程教材（HTML）",
    order=11, expect={"min_docs": 30})
add("16C03", "16", "course", "MIT 6.5660 (6.858) Computer Systems Security 讲义与实验说明", "Nickolai Zeldovich 等", "2024", "Spring 2024",
    C + "MIT_6.5660_Spring2024_Materials_html_en.tar",
    mirror("https://css.csail.mit.edu/6.5660/2024/", include=["/6.5660/2024"], quota=150, level="2"),
    "课程网站公开（版权保留）", "权限分离、沙箱、内存安全、Web 安全、网络与系统安全论文讲义与实验", school="MIT", level="高级",
    prereq="操作系统、C", material="讲义/论文阅读页 + 实验说明", order=12, expect={"min_docs": 10, "max_broken": 0.2},
    note="断链抽样主要为 questions.html?q=… 的查询参数页（离线镜像无法保存查询变体）")
add("16D01", "16", "docs", "OWASP Cheat Sheet Series", "OWASP Foundation", "2026", "master 提交", D + "owasp_cheatsheet_series_master_en.tar",
    git("OWASP/CheatSheetSeries", None, ["cheatsheets", "Index.md", "IndexASVS.md", "IndexTopTen.md"]), "CC BY-SA 4.0",
    "输入校验、认证、会话、密钥管理、日志、反序列化等 90+ 主题速查", stack="（通用）", order=20, expect={"min_docs": 80},
    use="按需查询")
add("16D02", "16", "docs", "OWASP ASVS 5.0（应用安全验证标准）", "OWASP Foundation", "2025", "5.0（仓库提交）", D + "owasp_asvs_5.0_src_en.tar",
    git("OWASP/ASVS", None, ["5.0/en"]), "CC BY-SA 4.0", "按章节的可验证安全要求清单（审计与安全测试依据）", level="进阶",
    order=21, expect={"min_docs": 15})
add("16D03", "16", "docs", "OWASP Web Security Testing Guide（WSTG）", "OWASP Foundation", "2026", "master 提交",
    D + "owasp_wstg_master_src_en.tar", git("OWASP/wstg", None, ["document"]), "CC BY-SA 4.0", "Web 安全测试方法与逐项测试用例",
    level="进阶", order=22, expect={"min_docs": 100})
add("16D04", "16", "docs", "NIST SP 800-218 Secure Software Development Framework (SSDF) 1.1", "NIST", "2022", "1.1",
    D + "nist_sp800_218_ssdf_1.1_en.pdf", pdf("https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218.pdf"),
    "美国政府作品（公有领域）", "安全开发实践框架：准备、保护、生产、响应", order=23,
    expect={"title_words": ["Secure", "Software", "Development", "Framework"], "min_pages": 20})
add("16D05", "16", "docs", "NIST SP 800-63B-4 Digital Identity Guidelines: Authentication", "NIST", "2025", "Rev. 4",
    D + "nist_sp800_63b_4_en.pdf", pdf("https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf"),
    "美国政府作品（公有领域）", "认证器、口令策略、多因素认证、会话管理要求", level="进阶", order=24,
    expect={"title_words": ["Digital", "Identity", "Guidelines"], "min_pages": 40})
add("16D06", "16", "docs", "SLSA 供应链安全规范", "OpenSSF", "2026", "main 提交", D + "slsa_spec_main_en.tar", git("slsa-framework/slsa", None, ["spec"]),
    "Community Specification License 1.0", "构建来源证明、构建级别、依赖与供应链威胁", level="进阶", order=25, expect={"min_docs": 20})
add("16D07", "16", "docs", "gVisor 文档源（容器沙箱）", "Google", "2026", "master 提交", D + "gvisor_docs_master_src_en.tar",
    git("google/gvisor", None, ["g3doc"]), "Apache-2.0", "用户态内核沙箱架构、安全模型、运行时配置（执行隔离）", level="高级",
    order=26, expect={"min_docs": 20}, cross=["15", "14"])
add("16D08", "16", "docs", "Bandit 文档源（Python 安全静态分析）", "PyCQA", "2026", "main 提交", D + "bandit_docs_src_en.tar",
    git("PyCQA/bandit", None, ["doc"]), "Apache-2.0", "Python 常见安全问题检测规则与配置", stack="Python", order=27,
    expect={"min_docs": 20}, complete="部分", scope="doc/source（Sphinx 源；插件 API 由 docstring 生成部分未含）")
add("16X01", "16", "practice", "OWASP Juice Shop（含漏洞的现代 Web 应用靶场）", "OWASP Foundation", "2026", "master 提交", X + "owasp_juice_shop_master_en.tar",
    git("juice-shop/juice-shop"),
    "MIT", "注入、XSS、认证缺陷、访问控制等 100+ 挑战（仅阅读源码与说明，不部署）", level="进阶", prereq="Web 基础", order=30,
    expect={"min_docs": 5}, scope="完整仓库（大文件按规则剔除）")
add("16X02", "16", "practice", "OWASP WebGoat（安全教学应用）", "OWASP Foundation", "2026", "main 提交", X + "owasp_webgoat_main_en.tar",
    git("WebGoat/WebGoat"), "GPL-2.0", "按课程组织的漏洞原理与修复练习", level="进阶", prereq="Java、Web 基础", order=31,
    expect={"min_docs": 5})

# ids already used by T_tools_en.json are shifted by +50 (same category/type prefix)
_tool_ids = {x["id"] for x in json.load(open(OUT.parent / "T_tools_en.json"))}
for x in S:
    if x["id"] in _tool_ids:
        x["id"] = x["id"][:3] + f"{int(x['id'][3:]) + 50:02d}"
json.dump(S, open(OUT, "w"), ensure_ascii=False, indent=1)
print(len(S), "core seeds ->", OUT)
