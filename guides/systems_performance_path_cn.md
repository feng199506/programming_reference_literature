# 系统与性能学习路线：计算机系统、C/C++、并发、GPU 与性能优化

适合对象：完成 Python 基础，准备深入底层、写高性能代码或 GPU 内核的学习者。
目标：理解程序从源码到机器执行的全过程，能用测量驱动优化 CPU 与 GPU 代码，能写正确的并发程序与基础 CUDA/Triton 内核，并能为 Python 写扩展。

---

## 阶段 1：C 语言与机器级表示（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 12B02《Beej's Guide to C Programming》 → `../books/Hall_BeejsGuideCProgramming_en.pdf` | C 语言教程与库参考（通读教程部分） |
| 2 | 11B02《Dive into Systems》 → `../books/Matthews_DiveIntoSystems_html_en.tar` | Dive into Systems：C、二进制表示、汇编、存储层次、OS 与共享内存并行 |
| 3 | 11C02《CMU 15-213/18-213 Introduction to Computer Systems 课件与讲义》 → `../courses/CMU_15213_Slides_en` | CMU 15-213 课件：数据表示 → 机器级程序 → 存储层次 → 链接 → 异常控制流 → 虚拟内存 → 网络与并发 |
| 4 | 12C02《Stanford CS 107 Computer Organization & Systems 指南与讲义》 → `../courses/Stanford_CS107_Guides_html_en.tar` | Stanford CS107 指南：gdb、valgrind、make、内存与泛型 |
| 实验 | 11X03《CS:APP 3e 自学实验包（Data/Bomb/Attack/Cache/Shell/Malloc/Proxy Lab 讲义与自学包）》 → `../practice/csapp_3e_selfstudy_labs_en.tar` | CS:APP 自学实验：Data/Bomb/Attack/Cache/Shell/Malloc/Proxy Lab |
| 查询 | 12D01《GCC 16.2 手册（PDF）》 → `../official_docs/gcc_16.2.0_manual_en.pdf`、12D02《GNU Make Manual》 → `../official_docs/gnu_make_manual_en.pdf`、12D03《GDB 手册（Debugging with GDB）》 → `../official_docs/gdb_manual_en.pdf` | GCC、Make、GDB 官方手册 |

## 阶段 2：编译、链接与构建系统（约 2–3 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 12B06《How To Write Shared Libraries》 → `../books/Drepper_HowToWriteSharedLibraries_2011_en.pdf` | ELF、动态链接、符号可见性与 ABI |
| 2 | 12D04《CMake 帮助文档源（含官方教程 Help/guide）》 → `../official_docs/cmake_help_src_en.tar` | CMake 官方教程（Help/guide/tutorial）→ 命令与目标属性参考 |
| 3 | 12D05《C++ Core Guidelines》 → `../official_docs/isocpp_cpp_core_guidelines_master_en.tar` | 现代 C++ 资源管理、接口与并发规则 |
| 4 | 12D06《pybind11 文档源与示例》 → `../official_docs/pybind11_docs_src_en.tar`、12D07《Cython 文档源》 → `../official_docs/cython_docs_src_en.tar`、12X02《pybind11 python_example（扩展模块构建示例）》 → `../practice/pybind_python_example_master_en.tar` | Python 扩展：pybind11 与 Cython 文档，配一个可构建的扩展模块工程 |
| 查询 | 01D01《Python 3.15 官方文档（教程、语言参考、标准库、C API、打包与扩展）》 → `../official_docs/python_3.15_docs_html_en.tar.bz2` | Python 文档的 extending/ 与 c-api/ 两部分 |

## 阶段 3：操作系统、进程、线程与并发（约 6–8 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 11B01《Operating Systems: Three Easy Pieces》 → `../books/ArpaciDusseau_OSTEP_v1.10_chapters_en` | OSTEP：虚拟化 → 并发 → 持久化，全书通读并做课后作业 |
| 2 | 11C01《MIT 6.1810 Operating System Engineering (Fall 2025) xv6 教材与实验》 → `../courses/MIT_6.1810_Fall2025_Materials_html_en.tar`、11X02《xv6-riscv（MIT 教学操作系统源码）》 → `../practice/mit_xv6_riscv_en.tar` | MIT 6.1810：xv6 教材与实验（系统调用、页表、trap、COW、锁、文件系统） |
| 3 | 11B04《The Little Book of Semaphores》 → `../books/Downey_LittleBookOfSemaphores_2.2.1_en.pdf` | 同步原语与经典并发问题练习 |
| 4 | 13B01《Is Parallel Programming Hard, And, If So, What Can You Do About It?》 → `../books/McKenney_IsParallelProgrammingHard_2026.06.21a_en.pdf` | 共享内存并行深入：锁、RCU、内存序（按需） |
| 查询 | 07D04《Linux man-pages 6.20（系统调用与库函数手册源）》 → `../official_docs/linux_man_pages_6.20_en.tar.xz`、11D02《Linux 内核官方文档（Documentation/ 源）》 → `../official_docs/linux_kernel_documentation_master_src_en.tar` | man2/man7：进程、信号、线程、futex、epoll；Linux 内核文档（调度、内存管理、cgroup、网络） |
| 论文 | 11P03《The Linux Scheduler: a Decade of Wasted Cores》 → `../papers/2016_Lozi_LinuxSchedulerDecadeWastedCores_en.pdf`、11P06《seL4: Formal Verification of an OS Kernel》 → `../papers/2009_Klein_SeL4FormalVerificationOSKernel_en.pdf`、11P08《Spectre Attacks: Exploiting Speculative Execution》 → `../papers/2019_Kocher_SpectreAttacksExploitingSpeculativeExecution_en.pdf` | 调度器缺陷、seL4 形式化验证、Spectre |

## 阶段 4：网络（约 3–4 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 11B03《Computer Networks: A Systems Approach》 → `../books/Peterson_ComputerNetworksSystemsApproach_src_en.tar` | 计算机网络系统方法：分层、IP、路由、TCP 拥塞控制、应用协议 |
| 2 | 11B05《Beej's Guide to Network Programming》 → `../books/Hall_BeejsGuideNetworkProgramming_en.pdf` | 套接字编程：TCP/UDP 服务端与客户端、poll/select |
| 3 | 09B01《High Performance Browser Networking》 → `../books/Grigorik_HighPerformanceBrowserNetworking_html_en.tar` | HTTP/2、TLS 与浏览器网络性能 |
| 查询 | 11D01《互联网核心协议 RFC 集（IP、TCP、UDP、DNS、QUIC）》 → `../official_docs/ietf_core_internet_rfcs_en`、09D03《HTTP 与 Web 认证核心 RFC 集》 → `../official_docs/ietf_http_auth_rfcs_en` | IP、TCP、UDP、DNS、QUIC、HTTP 标准原文 |
| 论文 | 11P01《The QUIC Transport Protocol: Design and Internet-Scale Deployment》 → `../papers/2017_Langley_QUICTransportProtocolDesignInternet_en.pdf`、11P10《QUIC is not Quick Enough over Fast Internet》 → `../papers/2023_Zhang_QUICNotQuickEnoughOver_en.pdf`、11P05《The Demikernel Datapath OS Architecture for Microsecond-scale Datacenter Systems》 → `../papers/2021_Zhang_DemikernelDatapathOSArchitectureMicrosecond_en.pdf` | QUIC 部署与高速网络下的性能问题、Demikernel 微秒级数据通路 |

## 阶段 5：CPU 性能分析与优化（约 4–6 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 12B04《What Every Programmer Should Know About Memory》 → `../books/Drepper_WhatEveryProgrammerShouldKnowAboutMemory_2007_en.pdf` | 缓存、TLB、NUMA 与预取（理解一切优化的前提） |
| 2 | 12B03《Performance Analysis and Tuning on Modern CPUs (2nd ed.)》 → `../books/Bakhvalov_PerformanceAnalysisTuningModernCPUs_2ndEd_en.pdf` | 测量方法、PMU、Top-Down 分析、前端/后端/内存瓶颈 |
| 3 | 12C01《MIT 6.172 Performance Engineering of Software Systems (Fall 2018) OCW 课程包》 → `../courses/MIT_6.172_Fall2018_OCW_en.zip` | MIT 6.172：位技巧、缓存友好、向量化、Cilk 并行、性能项目 |
| 4 | 12B05《Algorithms for Modern Hardware》 → `../books/Slotin_AlgorithmsForModernHardware_html_en.tar` | SIMD、缓存友好数据结构、分支预测 |
| 实验 | 12X01《perf-ninja（性能优化动手实验）》 → `../practice/dendibakh_perf_ninja_main_en.tar` | perf-ninja 逐项优化实验 |
| 论文 | 11P07《Profiling a warehouse-scale computer》 → `../papers/2015_Kanev_ProfilingWarehouseScaleComputer_en.pdf`、11P02《Are You Sure You Want to Use MMAP in Your Database Management System?》 → `../papers/2022_Crotty_YouSureYouWantUse_en.pdf`、11P04《What Modern NVMe Storage Can Do, And How To Exploit It: High-Performance I/O for High-Performance Storage Engines》 → `../papers/2023_Haas_WhatModernNVMeStorageDo_en.pdf`、11P09《Demystifying CXL Memory with Genuine CXL-Ready Systems and Devices》 → `../papers/2023_Sun_DemystifyingCXLMemoryGenuineCXL_en.pdf` | 仓库级计算机剖析；mmap 与数据库；现代 NVMe I/O；CXL 内存实测 |

**测量驱动优化流程**（依据12B03《Performance Analysis and Tuning on Modern CPUs (2nd ed.)》 → `../books/Bakhvalov_PerformanceAnalysisTuningModernCPUs_2ndEd_en.pdf`12C01《MIT 6.172 Performance Engineering of Software Systems (Fall 2018) OCW 课程包》 → `../courses/MIT_6.172_Fall2018_OCW_en.zip`）：

1. 固定输入与环境，多次测量取统计量。
2. 先用剖析器找热点，再用硬件计数器判断瓶颈类型。
3. 一次只改一处，改完回归测量。
4. 记录基线与每次改动的收益。

## 阶段 6：并行计算与 GPU 编程（约 8–10 周）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 13C01《Stanford CS149 Parallel Computing (Fall 2025) 课件》 → `../courses/Stanford_CS149_Fall2025_Slides_en` | Stanford CS149 课件：SIMD/多核 → ISPC → CUDA → 同步与一致性 → DSL 与加速器 |
| 2 | （CS149 作业仓库无许可证，未收录） | 作业说明见课程站；可用13X52《GPU MODE lectures（讲座笔记本与代码）》 → `../practice/gpu_mode_lectures_main_en.tar`13X51《llm.c（纯 C/CUDA 的 GPT-2 训练实现）》 → `../practice/karpathy_llm_c_master_en.tar`替代练习 |
| 3 | 13D01《CUDA Toolkit 核心指南 PDF 集（编程指南、最佳实践、PTX ISA）》 → `../official_docs/cuda_toolkit_guides_pdf_en` | CUDA 编程指南（执行模型、内存层次、同步）+ 最佳实践指南；PTX ISA 与 Runtime API 按需查询 |
| 4 | 13C02《University of Oxford CUDA Programming Course（讲义与实践包）》 → `../courses/Oxford_CUDA_Course_en` | Oxford CUDA 课程：规约、扫描、库、多 GPU 的讲义与练习 |
| 5 | 13X01《NVIDIA cuda-samples v13.4》 → `../practice/cuda_samples_v13.4_en.tar` | cuda-samples：按主题阅读（不需要全部编译） |
| 6 | 13D02《Nsight Compute / Nsight Systems 性能分析文档（离线镜像）》 → `../official_docs/nsight_profiling_docs_mirror_en.tar` | Nsight Compute / Nsight Systems：内核级与系统级剖析 |
| 7 | 13D03《Triton 编程语言官方文档（triton-lang.org 构建 HTML，含教程）》 → `../official_docs/triton_lang_docs_main_html_en.tar`、13X02《Triton v3.9.0 教程源码（python/tutorials）》 → `../practice/triton_lang_v3.9.0_tutorials_en.tar` | Triton 编程语言：向量加 → 融合 softmax → 矩阵乘 → 融合注意力教程（**注意**：与 Triton Inference Server 无关） |
| 8 | 13X52《GPU MODE lectures（讲座笔记本与代码）》 → `../practice/gpu_mode_lectures_main_en.tar`、13X51《llm.c（纯 C/CUDA 的 GPT-2 训练实现）》 → `../practice/karpathy_llm_c_master_en.tar` | GPU MODE 讲座代码；llm.c 手写 CUDA 训练 |
| 9 | 13B02《Introduction to High Performance Scientific Computing（The Art of HPC 卷 1）》 → `../books/Eijkhout_IntroductionHPC_vol1_en.pdf`、13B03《Parallel Programming for Science and Engineering（The Art of HPC 卷 2：MPI/OpenMP）》 → `../books/Eijkhout_ParallelProgramming_vol2_en.pdf`、13D10《OpenMP API Specification 6.0》 → `../official_docs/openmp_api_spec_6.0_en.pdf`、13D11《MPI: A Message-Passing Interface Standard 4.1》 → `../official_docs/mpi_4.1_standard_en.pdf` | HPC 体系、MPI/OpenMP 教程与标准 |
| 论文 | 13P19《Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures》 → `../papers/2008_Williams_RooflineInsightfulVisualPerformanceModel_en.pdf`、13P18《Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations》 → `../papers/2019_Tillet_TritonIntermediateLanguageCompilerTiled_en.pdf`、13P17《Dissecting the NVIDIA Volta GPU Architecture via Microbenchmarking》 → `../papers/2018_Jia_DissectingNVIDIAVoltaGPUArchitecture_en.pdf`、13P08《Benchmarking and Dissecting the Nvidia Hopper GPU Architecture》 → `../papers/2024_Luo_BenchmarkingDissectingNvidiaHopperGPU_en.pdf` | Roofline 模型、Triton 编译器、Volta/Hopper 微基准 |
| 论文 | 13P01《FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness》 → `../papers/2022_Dao_FlashAttentionFastMemoryEfficientExact_en.pdf`、13P02《FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning》 → `../papers/2023_Dao_FlashAttention2FasterAttentionBetter_en.pdf`、13P03《FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision》 → `../papers/2024_Shah_FlashAttention3FastAccurateAttention_en.pdf`、13P04《ThunderKittens: Simple, Fast, and Adorable AI Kernels》 → `../papers/2024_Spector_ThunderKittensSimpleFastAdorableAI_en.pdf`、13P05《Flex Attention: A Programming Model for Generating Optimized Attention Kernels》 → `../papers/2024_Dong_FlexAttentionProgrammingModelGenerating_en.pdf`、13P06《Liger Kernel: Efficient Triton Kernels for LLM Training》 → `../papers/2024_Hsu_LigerKernelEfficientTritonKernels_en.pdf`、13P07《KernelBench: Can LLMs Write Efficient GPU Kernels?》 → `../papers/2025_Ouyang_KernelBenchLLMsWriteEfficientGPU_en.pdf` | FlashAttention 1–3、ThunderKittens、FlexAttention、Liger Kernel、KernelBench（算子实现与性能分析案例） |

## 阶段 7：训练系统优化（约 4 周，衔接深度学习）

| 顺序 | 资料 | 用法 |
|---|---|---|
| 1 | 05D01《PyTorch 2.15 官方文档（含 torch.distributed、torch.export、ONNX 导出、profiler、编译）》 → `../official_docs/pytorch_2.15_docs_html_en.tar` | PyTorch：torch.compile、AOTInductor、CUDA 语义、profiler、AMP |
| 2 | 05D02《PyTorch 官方教程（构建 HTML，含入门、分布式、导出、性能剖析）》 → `../official_docs/pytorch_tutorials_html_en.tar` | PyTorch 教程中的性能剖析与分布式篇目 |
| 3 | 13B04《How to Scale Your Model: A Systems View of LLMs on TPUs》 → `../books/Austin_HowToScaleYourModel_src_en.tar` | 算力-通信分析：数据/张量/流水并行（以 TPU 为例，原理通用） |
| 4 | 13D04《DeepSpeed 0.19.8 文档（教程站点源 + Read the Docs API 源）》〔部分资料〕 → `../official_docs/deepspeed_0.19.8_docs_src_en.tar`、13D05《DeepSpeed API 参考（deepspeed.readthedocs.io 离线镜像）》 → `../official_docs/deepspeed_api_rtd_mirror_en.tar`、13X03《DeepSpeedExamples》 → `../practice/deepspeed_examples_master_en.tar` | DeepSpeed ZeRO、配置与示例 |
| 5 | 13D06《NCCL 用户指南（离线镜像）》 → `../official_docs/nccl_user_guide_mirror_en.tar` | NCCL：集合通信、环境变量、排障 |
| 6 | 05B04《Machine Learning Engineering Open Book》 → `../books/Bekman_MachineLearningEngineeringOpenBook_src_en.tar` | 大模型训练工程手册（按需查询） |
| 论文 | 13P15《ZeRO: Memory Optimizations Toward Training Trillion Parameter Models》 → `../papers/2019_Rajbhandari_ZeROMemoryOptimizationsTowardTraining_en.pdf`、13P13《Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM》 → `../papers/2021_Narayanan_EfficientLargeScaleLanguageModel_en.pdf`、13P14《PyTorch Distributed: Experiences on Accelerating Data Parallel Training》 → `../papers/2020_Li_PyTorchDistributedExperiencesAcceleratingData_en.pdf`、13P09《PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel》 → `../papers/2023_Zhao_PyTorchFSDPExperiencesScalingFully_en.pdf`、13P10《TorchTitan: One-stop PyTorch native solution for production ready LLM pre-training》 → `../papers/2024_Liang_TorchTitanOneStopPyTorchNative_en.pdf`、13P16《Mixed Precision Training》 → `../papers/2017_Micikevicius_MixedPrecisionTraining_en.pdf`、13P11《FP8 Formats for Deep Learning》 → `../papers/2022_Micikevicius_FP8FormatsDeepLearning_en.pdf`、13P12《DeepSeek-V3 Technical Report》 → `../papers/2024_DeepSeekAI_DeepSeekV3TechnicalReport_en.pdf` | ZeRO、Megatron-LM、PyTorch DDP、FSDP、TorchTitan、混合精度、FP8、DeepSeek-V3 |

衔接：推理侧的内核与服务优化见 `deployment_path_cn.md` 与 `../tools/interoperability_guide_cn.md`。
