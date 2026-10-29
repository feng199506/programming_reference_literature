"""Generate scripts/seeds/P_papers_en.json for the research-heavy categories (02, 11, 13, 14, 15).

Each arXiv entry is checked against arXiv metadata (export API, shared rate limit); if the metadata title does not
match the expected title the entry is searched by title, and dropped (logged) if still unmatched.  Classic papers
come from author/official open-access PDFs and are marked 经典 (classic).  Metadata cache: state/arxiv_meta.json.
"""
import json
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import STATE, http, load_json, norm_words, save_json  # noqa: E402

OUT = Path(__file__).resolve().parent / "seeds" / "P_papers_en.json"
META = STATE / "arxiv_meta.json"
NS = {"a": "http://www.w3.org/2005/Atom"}

ARX = {  # cat: [(arxiv_id, expected title)]
    "02": [("2504.17033", "Breaking the Sorting Barrier for Directed Single-Source Shortest Paths"),
           ("2203.00671", "Maximum Flow and Minimum-Cost Flow in Almost-Linear Time"),
           ("2311.11793", "Universal Optimality of Dijkstra via Beyond-Worst-Case Heaps"),
           ("2501.02305", "Optimal Bounds for Open Addressing Without Reordering"),
           ("2203.03456", "Negative-Weight Single-Source Shortest Paths in Near-linear Time"),
           ("2205.05982", "Vectorized and performance-portable Quicksort"),
           ("2009.13569", "Engineering In-place (Shared-memory) Sorting Algorithms"),
           ("2106.05123", "Pattern-defeating Quicksort"),
           ("2210.10173", "Faster Matrix Multiplication via Asymmetric Hashing"),
           ("2111.12800", "Tiny Pointers"),
           ("1712.01208", "The Case for Learned Index Structures"),
           ("1603.09320", "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs")],
    "13": [("2205.14135", "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"),
           ("2307.08691", "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"),
           ("2407.08608", "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"),
           ("2410.20399", "ThunderKittens: Simple, Fast, and Adorable AI Kernels"),
           ("2412.05496", "Flex Attention: A Programming Model for Generating Optimized Attention Kernels"),
           ("2410.10989", "Liger Kernel: Efficient Triton Kernels for LLM Training"),
           ("2502.10517", "KernelBench: Can LLMs Write Efficient GPU Kernels?"),
           ("2402.13499", "Benchmarking and Dissecting the Nvidia Hopper GPU Architecture"),
           ("2304.11277", "PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel"),
           ("2410.06511", "TorchTitan: One-stop PyTorch native solution for production ready LLM pre-training"),
           ("2209.05433", "FP8 Formats for Deep Learning"),
           ("2412.19437", "DeepSeek-V3 Technical Report"),
           ("2104.04473", "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM"),
           ("2006.15704", "PyTorch Distributed: Experiences on Accelerating Data Parallel Training"),
           ("1910.02054", "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"),
           ("1710.03740", "Mixed Precision Training"),
           ("1804.06826", "Dissecting the NVIDIA Volta GPU Architecture via Microbenchmarking")],
    "14": [("2309.06180", "Efficient Memory Management for Large Language Model Serving with PagedAttention"),
           ("2401.09670", "DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving"),
           ("2403.02310", "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve"),
           ("2312.07104", "SGLang: Efficient Execution of Structured Language Model Programs"),
           ("2311.18677", "Splitwise: Efficient generative LLM inference using phase splitting"),
           ("2407.00079", "Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving"),
           ("2211.17192", "Fast Inference from Transformers via Speculative Decoding"),
           ("2401.08671", "DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference")],
    "15": [("2005.11401", "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"),
           ("2210.03629", "ReAct: Synergizing Reasoning and Acting in Language Models"),
           ("2302.04761", "Toolformer: Language Models Can Teach Themselves to Use Tools"),
           ("2310.06770", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"),
           ("2405.15793", "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"),
           ("2407.01489", "Agentless: Demystifying LLM-based Software Engineering Agents"),
           ("2407.16741", "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"),
           ("2402.01030", "Executable Code Actions Elicit Better LLM Agents"),
           ("2307.03172", "Lost in the Middle: How Language Models Use Long Contexts"),
           ("2310.11511", "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"),
           ("2312.10997", "Retrieval-Augmented Generation for Large Language Models: A Survey"),
           ("2309.15217", "RAGAS: Automated Evaluation of Retrieval Augmented Generation"),
           ("2306.05685", "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"),
           ("2303.11366", "Reflexion: Language Agents with Verbal Reinforcement Learning"),
           ("2310.08560", "MemGPT: Towards LLMs as Operating Systems"),
           ("2406.12045", "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"),
           ("2305.15334", "Gorilla: Large Language Model Connected with Massive APIs"),
           ("2004.12832", "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT"),
           ("2004.04906", "Dense Passage Retrieval for Open-Domain Question Answering")],
}

# added after the first build: numbered after the classics so existing ids stay stable
ARX_LATE = {"11": [("?", "Demystifying CXL Memory with Genuine CXL-Ready Systems and Devices"),
                   ("?", "QUIC is not Quick Enough over Fast Internet"),
                   ("?", "An Empirical Study of Rust-for-Linux: The Success, Dissatisfaction, and Compromise")]}

CLASSIC = [  # cat, year, first-author surname, title, authors, venue, urls
    ("02", 2023, "Mankowitz", "Faster sorting algorithms discovered using deep reinforcement learning",
     "Daniel J. Mankowitz et al.", "Nature 618 (2023)", ["https://www.nature.com/articles/s41586-023-06004-9.pdf"]),
    ("11", 2017, "Langley", "The QUIC Transport Protocol: Design and Internet-Scale Deployment", "Adam Langley et al.",
     "SIGCOMM 2017", ["https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46403.pdf"]),
    ("11", 2022, "Crotty", "Are You Sure You Want to Use MMAP in Your Database Management System?",
     "Andrew Crotty, Viktor Leis, Andrew Pavlo", "CIDR 2022", ["https://www.cidrdb.org/cidr2022/papers/p13-crotty.pdf"]),
    ("11", 2016, "Lozi", "The Linux Scheduler: a Decade of Wasted Cores", "Jean-Pierre Lozi et al.", "EuroSys 2016",
     ["https://people.ece.ubc.ca/sasha/papers/eurosys16-final29.pdf"]),
    ("11", 2023, "Haas", "What Modern NVMe Storage Can Do, And How To Exploit It: High-Performance I/O for High-Performance Storage Engines",
     "Gabriel Haas, Viktor Leis", "PVLDB 16(9) 2023", ["https://www.vldb.org/pvldb/vol16/p2090-haas.pdf"]),
    ("11", 2021, "Zhang", "The Demikernel Datapath OS Architecture for Microsecond-scale Datacenter Systems",
     "Irene Zhang et al.", "SOSP 2021", ["https://irenezhang.net/papers/demikernel-sosp21.pdf"]),
    ("11", 2009, "Klein", "seL4: Formal Verification of an OS Kernel", "Gerwin Klein et al.", "SOSP 2009",
     ["https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf"]),
    ("11", 2015, "Kanev", "Profiling a warehouse-scale computer", "Svilen Kanev et al.", "ISCA 2015",
     ["https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44271.pdf"]),
    ("11", 2019, "Kocher", "Spectre Attacks: Exploiting Speculative Execution", "Paul Kocher et al.", "IEEE S&P 2019",
     ["https://arxiv.org/pdf/1801.01203"]),
    ("13", 2019, "Tillet", "Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations",
     "Philippe Tillet, H. T. Kung, David Cox", "MAPL 2019", ["https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf"]),
    ("13", 2008, "Williams", "Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures",
     "Samuel Williams, Andrew Waterman, David Patterson", "UC Berkeley EECS-2008-134（CACM 2009 论文的技术报告版）",
     ["https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.pdf"]),
    ("14", 1978, "Lamport", "Time, Clocks, and the Ordering of Events in a Distributed System", "Leslie Lamport", "CACM 21(7) 1978",
     ["https://lamport.azurewebsites.net/pubs/time-clocks.pdf"]),
    ("14", 2001, "Lamport", "Paxos Made Simple", "Leslie Lamport", "ACM SIGACT News 2001",
     ["https://lamport.azurewebsites.net/pubs/paxos-simple.pdf"]),
    ("14", 2014, "Ongaro", "In Search of an Understandable Consensus Algorithm", "Diego Ongaro, John Ousterhout",
     "USENIX ATC 2014", ["https://raft.github.io/raft.pdf"]),
    ("14", 2004, "Dean", "MapReduce: Simplified Data Processing on Large Clusters", "Jeffrey Dean, Sanjay Ghemawat", "OSDI 2004",
     ["https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf"]),
    ("14", 2007, "DeCandia", "Dynamo: Amazon's Highly Available Key-value Store", "Giuseppe DeCandia et al.", "SOSP 2007",
     ["https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf"]),
    ("14", 2015, "Verma", "Large-scale cluster management at Google with Borg", "Abhishek Verma et al.", "EuroSys 2015",
     ["https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43438.pdf"]),
    ("14", 2013, "Dean", "The Tail at Scale", "Jeffrey Dean, Luiz André Barroso", "CACM 56(2) 2013",
     ["https://www.barroso.org/publications/TheTailAtScale.pdf"]),
]


def short(title, n=5):
    w = [x for x in re.findall(r"[A-Za-z0-9]+", title) if x.lower() not in {"a", "an", "the", "of", "for", "and", "in", "on",
                                                                               "with", "to", "via", "by", "is", "are", "can"}]
    return "".join(x[:1].upper() + x[1:] for x in w[:n])


def fetch_meta(ids, meta):
    need = [i for i in ids if i not in meta]
    for k in range(0, len(need), 40):
        chunk = need[k:k + 40]
        r = http("http://export.arxiv.org/api/query?id_list=" + ",".join(chunk) + f"&max_results={len(chunk)}", timeout=90)
        if r["status"] != 200:
            print("arXiv API", r["status"], r["err"])
            continue
        root = ET.fromstring(r["body"])
        for e in root.findall("a:entry", NS):
            aid = e.find("a:id", NS).text.rsplit("/abs/", 1)[1]
            base, ver = re.match(r"(.+?)(v\d+)?$", aid).groups()
            meta[base] = {"title": " ".join(e.find("a:title", NS).text.split()), "version": ver or "",
                          "published": e.find("a:published", NS).text[:10], "updated": e.find("a:updated", NS).text[:10],
                          "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
                          "comment": (e.find("{http://arxiv.org/schemas/atom}comment") .text
                                      if e.find("{http://arxiv.org/schemas/atom}comment") is not None else ""),
                          "journal_ref": (e.find("{http://arxiv.org/schemas/atom}journal_ref").text
                                          if e.find("{http://arxiv.org/schemas/atom}journal_ref") is not None else "")}
        save_json(META, meta)


def search_title(title):
    q = urllib.parse.quote(f'ti:"{title}"')
    r = http(f"http://export.arxiv.org/api/query?search_query={q}&max_results=3", timeout=90)
    if r["status"] != 200:
        return None
    for e in ET.fromstring(r["body"]).findall("a:entry", NS):
        t = " ".join(e.find("a:title", NS).text.split())
        if match(t, title) >= 0.85:
            return re.match(r"(.+?)(v\d+)?$", e.find("a:id", NS).text.rsplit("/abs/", 1)[1]).group(1)
    return None


def match(a, b):
    wa, wb = set(norm_words(a)), norm_words(b)
    return sum(w in wa for w in wb) / max(1, len(wb))


def main():
    meta = load_json(META, {})
    allids = [i for v in list(ARX.values()) + list(ARX_LATE.values()) for i, _ in v if i != "?"]
    fetch_meta(allids, meta)
    seeds, dropped = [], []
    n = {}
    add_arxiv(ARX, meta, seeds, dropped, n)
    add_classic(seeds, n)
    add_arxiv(ARX_LATE, meta, seeds, dropped, n)
    json.dump(seeds, open(OUT, "w"), ensure_ascii=False, indent=1)
    save_json(STATE / "papers_dropped.json", dropped)
    print(len(seeds), "paper seeds;", "per cat", n, "; dropped", dropped)


def add_arxiv(table, meta, seeds, dropped, n):
    for cat, items in table.items():
        for aid, title in items:
            m = meta.get(aid)
            if not m or match(m["title"], title) < 0.8:
                alt = search_title(title)
                if alt:
                    fetch_meta([alt], meta)
                    aid, m = alt, meta.get(alt)
                if not m or match(m["title"], title) < 0.8:
                    dropped.append((cat, aid, title, (m or {}).get("title", "")))
                    continue
            year = int(m["published"][:4])
            n[cat] = n.get(cat, 0) + 1
            first = m["authors"][0].split()[-1] if m["authors"] else "Anon"
            first = re.sub(r"[^A-Za-z]", "", first) or "Anon"
            recent = m["published"] >= "2023-10-29"
            seeds.append(dict(
                id=f"{cat}P{n[cat]:02d}", cat=cat, cross=[], type="paper", title=m["title"],
                authors="; ".join(m["authors"][:8]) + (" 等" if len(m["authors"]) > 8 else ""), school="", year=str(year),
                version=f"arXiv:{aid}{m['version']}", lang="en", level="高级", prereq="", stack="",
                source=f"https://arxiv.org/abs/{aid}", license="arXiv（以论文页声明为准）", goal="", order=60 + n[cat],
                out=f"papers/{year}_{first}_{short(m['title'])}_en.pdf",
                get={"kind": "pdf", "urls": [f"https://arxiv.org/pdf/{aid}{m['version']}"]},
                expect={"title_words": norm_words(m["title"])[:8], "min_pages": 4, "min_ratio": 0.6},
                material="论文", use="精读/按需", note="", complete="完整",
                paper={"arxiv": aid, "first_public": m["published"], "updated": m["updated"],
                       "venue": m.get("journal_ref") or m.get("comment", "")[:160], "window": "近三年" if recent else "经典/较早"}))


def add_classic(seeds, n):
    for cat, year, first, title, authors, venue, urls in CLASSIC:
        n[cat] = n.get(cat, 0) + 1
        seeds.append(dict(
            id=f"{cat}P{n[cat]:02d}", cat=cat, cross=[], type="paper", title=title, authors=authors, school="", year=str(year),
            version=venue, lang="en", level="高级", prereq="", stack="", source=urls[0], license="作者/机构公开版本",
            goal="", order=60 + n[cat], out=f"papers/{year}_{first}_{short(title)}_en.pdf", get={"kind": "pdf", "urls": urls},
            expect={"title_words": norm_words(title)[:8], "min_pages": 2, "min_ratio": 0.6}, material="论文", use="精读/按需",
            note="", complete="完整", paper={"venue": venue, "first_public": str(year),
                                          "window": "近三年" if year >= 2024 else "经典/较早"}))


if __name__ == "__main__":
    main()
