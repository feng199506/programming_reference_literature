# 下载与解压恢复说明（编程参考资料库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含以下内容，不含教材、课程、官方文档、论文和实践项目全文：
  - 根目录的总报告与登记表：`README_cn.md`、`catalog_cn.csv`、`progress_cn.csv`、`download_failures_cn.csv`、`search_log_cn.md`；
  - `guides/`（学习路线与实践指南）、`tools/`（AI 框架工具目录、学习地图与互操作说明）；
  - 脚本 `scripts/` 和断点状态 `state/`；
  - 本说明、分包索引和改名明细。

  仓库原有的 `main` 分支没有改动。这个分支的父提交是 `main`。`main` 上原有的 pandas 文档 `.zip` 和 Python 文档 `.tar.bz2` 不在这个分支里，它们在下面的 Release 包中。
- **Release `programming-full-20261029`**：9 个独立的不压缩 `.tar` 包，合起来就是完整的资料库。

Release 页面：https://github.com/feng199506/programming_reference_literature/releases/tag/programming-full-20261029

## 1. 包列表

包按路径顺序切分，内容范围如下（文件名前缀都是 `programming_reference_literature_20261029_`，后缀都是 `_cn_en.tar`）：

| 包 | 内容范围（按路径顺序） |
|---|---|
| `batch001` | 根目录报告与登记表、`scripts/`、`state/`、`books/` 全部，以及 `courses/` 的开头部分（到 Berkeley CS294 课件的一部分） |
| `batch002` | `courses/` 中间部分（Berkeley CS294 其余课件，到 MIT 6.031） |
| `batch003` | `courses/` 中间部分（MIT 6.046J，到 Stanford CS253 课件的一部分） |
| `batch004` | `courses/` 其余部分、`guides/`，以及 `official_docs/` 的开头部分（到 KServe 网站文档） |
| `batch005` | `official_docs/` 中间部分（Kubernetes 文档起，到 ONNX 规范文档） |
| `batch006` | `official_docs/` 中间部分（ONNX 网站镜像起，到 PyTorch 2.15 文档） |
| `batch007` | `official_docs/` 其余部分（PyTorch 教程起），`papers/` 全部，`practice/` 的开头部分 |
| `batch008` | `practice/` 中间部分（Anthropic Cookbook 起，到 ONNX 教程） |
| `batch009` | `practice/` 其余部分，`tools/` |

每个文件属于哪个包，见 `archive_index_cn.csv`。它是 UTF-8 带 BOM 编码，可直接用 Excel 打开，共 1,353 行，每行一个文件。

- 每个包都可以**单独解压**，不需要拼接。
- 包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包没有压缩，所需磁盘空间约等于包的大小。全部解压约需 **12.2 GiB**。如果还要展开里面的文档镜像、课程包和示例包（见第 4 节），建议预留 35 GiB。

## 2. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 9 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\programming\`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断时，可以在浏览器的下载列表里点“恢复”，或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，核对每个包的大小。在文件属性窗口里看“大小”一项的字节数，不要看“占用空间”。

## 3. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**，目标目录用短路径，例如 `D:\programming\`。

1. 在下载文件夹中，按住 Ctrl 选中 9 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\programming\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 点确定。

也可以逐个解压：每个包都右键 → WinRAR → **解压文件…**，目标路径都填同一个 `D:\programming\`。不要用“解压到 programming_reference_literature_20261029_batch00X_cn_en\”这个菜单项，它会给每个包各建一个子文件夹，目录结构就被拆散了。

解压后的目录结构：

```
D:\programming\
├─ README_cn.md、catalog_cn.csv、progress_cn.csv、download_failures_cn.csv、search_log_cn.md
├─ books\ courses\ official_docs\ papers\ practice\
├─ guides\ tools\
├─ scripts\
└─ state\
```

### Windows 兼容处理

发布包里的文件名都已经处理过，在 Windows 下解压发布包不会因为文件名报错。第一层的 1,353 个文件都不需要改名，最长相对路径 112 个字符。资料库的本地原件没有改动，每一处改动都逐条记在 `windows_rename_map_cn.csv` 里。

43 个内层归档在发布包中重新打包了，其余内容不变（39 个 `.tar`、1 个 `.tar.gz`、2 个 `.tar.xz`、1 个 `.zip`，压缩格式保持不变）：

- **文件名带 Windows 不允许的字符**：主要是网页离线镜像里形如 `style.css?v=…` 的样式、脚本和字体文件，以及 Linux man-pages 中形如 `gnu::aligned.3attr` 的文件名。
  - 涉及的镜像：TensorRT、NVIDIA Nsight、NCCL、DeepSpeed、BentoML、ONNX 网站、Sentence Transformers、Keras、Faiss Wiki；教材《Database Design》《Python Programming and Numerical Methods》《Python for Data Analysis》《Fundamentals of Data Visualization》《Machine Learning in Production》网页版；Harvard CS50P / CS50W、MIT 6.5660 / 6.5840 / 6.1810 / 6.031 / 6.390、Stanford CS107 课程网页。
  - 名字里的 `?`、`:` 等字符改成 `_`，网页中的对应链接同步改写。
- **同一目录下只差大小写的文件**：TensorFlow API 文档镜像（20 个，`.tar.gz`）、PyTorch 教程镜像（5 张图片）、SciPy 1.18.0 文档 `.zip`（2 个）、Linux man-pages（2 个，例如 `NAN.3` 与 `nan.3`）、Norvig pytudes（1 个）。在 Windows 下它们会互相覆盖，因此后一个加了 `_case2` 后缀，网页中的引用同步改写。
- **符号链接**：Windows 普通用户无法创建符号链接，WinRAR 会报错“需要管理员权限”。
  - 14 个指向包内普通文件的链接，改成了目标文件的副本。
  - 29 个已去掉，原链接目标逐条记在改名明细里：
    - 失效的链接，例如 Hugging Face 示例包里指向示例目录之外的文件。
    - 指向目录的链接，例如 man-pages 根目录的 `man1` … `man9` 快捷方式，实际页面仍在 `man/man1` … `man/man9` 中。
- 合计 417 个文件改名，43 个符号链接改为副本或去掉。因此这 43 个归档的字节数与资料库原件不同，这是正常的。
- 其余 194 个内层归档已逐个检查，没有上述问题，没有改动：171 个 `.tar`、22 个 `.zip`、1 个 `.tar.bz2`。

## 4. 内层归档（.tar / .zip / .tar.xz 等）

资料库本身就把很多资料整包保存，包括官方文档的 HTML 离线镜像或源码、课程网页与课程包（MIT OCW 等 `.zip`）、实践项目快照。解压发布包之后，它们仍是单个文件，需要时再单独解开：

- 解开方法：右键该文件 → WinRAR → **解压到 “文件名\”**。WinRAR 可以直接解开 `.tar.gz`、`.tar.xz`、`.tar.bz2`。
- HTML 镜像解开后，用浏览器打开其中的 `index.html`。

**长路径提示**：有 3 个内层归档的包内路径超过 200 个字符，这是上游内容自身的目录结构，没有改动：

- Stanford CS336 讲义仓库 `courses/Stanford_CS336_Spring2025_src_en/spring2025-lectures_b98b08a_en.tar`，最长 249 个字符，是讲义的图片缓存；
- OpenVINO 2026.4.1 文档，最长 215 个字符；
- MDN Web 文档，最长 203 个字符。

WinRAR 可以正常解出这类长路径，但资源管理器可能无法打开最深的文件。建议把这几个包解到很短的目录（例如 `D:\L\`）。如需在资源管理器或其他工具中处理，可在 Windows 10/11 中开启长路径支持：注册表 `HKLM\SYSTEM\CurrentControlSet\Control\FileSystem` 下的 `LongPathsEnabled` 设为 1。

## 5. Linux / macOS

```bash
mkdir -p ~/programming
for f in programming_reference_literature_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/programming || echo "FAILED: $f"; done
```

## 6. 资料状态说明（来自资料库自身的报告，与打包无关）

- **只计已核验条目**：全库去重共 376 项，其中完整 348 项、部分资料 28 项。部分资料单列，不计入完整数，详见 `README_cn.md` 和 `catalog_cn.csv`。
  - 按类型（含部分资料）：教材 66、大学课程资料 43、官方文档/系统教程 122、实践项目 69、论文 76。
  - 另有 62 个 AI 框架与工具的版本化文档链，目录在 `tools/tools_catalog_cn.csv`。
- **未达标 2 处**：14 分布式系统与部署的大学课程资料缺 1 项，15 AI 应用与智能体开发的教材缺 1 项。
- **未获取 7 项**：记录在 `download_failures_cn.csv`，不计入，也没有对应文件。其中 2 项是无许可证的作业仓库，按规则未收录。
- **快照时间**：本次按 2026-10-29 21:43（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。资料库最后一次写入是在 21:38。

## 7. 完整性说明

- 本次发布只登记了上传状态：GitHub API 显示附件为 `uploaded`，且远端大小等于本地大小。**没有**做下载回验和哈希校验。
- 资料库本身没有整库的 SHA-256 清单。
- 资料库中的资料文件都已打包，没有遗漏。只排除了以下不属于资料的内容：
  - 本地 `.git/`，约 51 MB；
  - `scripts/__pycache__/` 中的 2 个 `.pyc`；
  - `state/` 下 374 个空的 `.lock` 锁文件，是下载脚本的并发锁。
