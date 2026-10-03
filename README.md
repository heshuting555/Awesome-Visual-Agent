# 🔍 Seeing the Horizon of Vision Agent: A Survey

**Awesome Vision Agents** — papers, benchmarks, projects, and code.

**717 unique works** · **1118 topic placements** · **679 arXiv links** · **331 works with code links** · **719 BibTeX keys**

💡 Welcome! This collection accompanies our survey on vision agents. It covers visual perception and reasoning, agent harnesses, memory, capability evolution, GUI and embodied applications, and evaluation.

📌 Corrections and additions are welcome through [issues](https://github.com/heshuting555/Awesome-Vision-Agent/issues) or pull requests. See the [contribution guide](CONTRIBUTING.md).

[📖 Full bibliography](references.bib) · [📦 Machine-readable catalogue](data/papers.json) · [🧭 Framework taxonomy](data/taxonomy.json) · [🔎 Coverage and provenance](docs/COVERAGE.md) · [🗂 Framework navigation](docs/TOPICS.md)

## Introduction

Papers follow the latest **Figure 1 framework**: **2 branches, 10 categories, and 35 topics**. Internal capabilities cover perception, reasoning, world simulation, evaluation and correction, and evolution. The harness branch covers planning and orchestration, memory, visual tools, verification, and safety. Planning and orchestration are part of the harness.

**Reading the tables.** ★ marks a representative work selected for that topic in Figure 1; these works appear first in the figure’s order. Other works are ordered alphabetically by title. A work may appear in several topics when its mechanisms support several parts of the framework; it appears once within each topic. Unique-work counts merge aliases, while topic-placement counts include these cross-listings. Year and venue remain descriptive table fields. A dash (—) means a name or link has not been identified. Project pages remain separate from code repositories, and evidence and verification dates are retained in the catalogue.

Bibliography snapshot: **2026-10-03**. Classification sources and limits are documented in [coverage notes](docs/COVERAGE.md).

## 📚 Table of Contents

- [Internal Capabilities of Vision-Centric Agents](#branch-internal)
  - [Vision Perception Capability](#category-perception)
    - [Grounded Perception](#topic-vision-perception-grounded) — 77 works
    - [Temporal Perception](#topic-vision-perception-temporal) — 35 works
    - [Spatial Perception](#topic-vision-perception-spatial) — 28 works
  - [Vision Reasoning Capability](#category-reasoning)
    - [Interleaved Multimodal Reasoning](#topic-reasoning-interleaved) — 18 works
    - [Visually Grounded Reasoning](#topic-reasoning-grounded) — 81 works
    - [Tool-Augmented Visual Reasoning](#topic-reasoning-tool-augmented) — 43 works
    - [Programmatic Visual Reasoning](#topic-reasoning-programmatic) — 17 works
  - [Simulation of World Dynamics](#category-world)
    - [Video Simulation](#topic-simulation-video) — 36 works
    - [Spatial Simulation](#topic-simulation-spatial) — 17 works
    - [Latent Simulation](#topic-simulation-latent) — 12 works
    - [Semantic Simulation](#topic-simulation-semantic) — 13 works
  - [Visual Evaluation and Correction Abilities](#category-evaluation)
    - [Visual Evidence Evaluation](#topic-visual-evaluation-evidence) — 13 works
    - [Visually Grounded Process Evaluation](#topic-visual-evaluation-process) — 19 works
    - [Visual Outcome Evaluation](#topic-visual-evaluation-outcome) — 19 works
    - [Visual-Based Self-Correction](#topic-visual-evaluation-self-correction) — 38 works
  - [Evolving Abilities](#category-evolving)
    - [Visual Capability Gap Diagnosis](#topic-evolving-diagnosis) — 17 works
    - [Visual Improvement Signal Generation](#topic-evolving-signals) — 48 works
    - [Vision-Guided Optimization Adaptation](#topic-evolving-optimization) — 104 works
    - [Self-Modification of Visual Interaction Infrastructure](#topic-evolving-infrastructure) — 48 works
- [Harness Infrastructure for Vision-Centric Agents](#branch-external)
  - [Vision Planning and Orchestration Infrastructure](#category-planning)
    - [Task and Workflow Planning](#topic-planning-task-workflow) — 86 works
    - [Trajectory Search and Deliberation](#topic-planning-trajectory-search) — 23 works
    - [Multi-Agent Planning and Coordination](#topic-planning-multiagent-coordination) — 31 works
  - [Vision Memory Infrastructure](#category-memory)
    - [Visual-to-Text](#topic-vision-memory-text) — 14 works
    - [Visual Evidence Store](#topic-vision-memory-evidence) — 19 works
    - [Visual Compression Layer](#topic-vision-memory-compression) — 15 works
    - [Visual Experience Repository](#topic-vision-memory-experience) — 42 works
  - [Visual Tools](#category-tools)
    - [Observation Tools](#topic-visual-tools-observation) — 27 works
    - [Search Tools](#topic-visual-tools-search) — 14 works
    - [Generation Tools](#topic-visual-tools-generation) — 54 works
  - [Vision Verification Infrastructure](#category-verification)
    - [Evidence Verification](#topic-verification-evidence) — 13 works
    - [Process Verification](#topic-verification-process) — 13 works
    - [Outcome Verification](#topic-verification-outcome) — 39 works
  - [Safety Infrastructure](#category-safety)
    - [Visual Information Safeguard](#topic-safety-visual-information) — 9 works
    - [Safety-Constrained Execution](#topic-safety-constrained-execution) — 21 works
    - [Runtime Oversight and Traceability](#topic-safety-runtime-oversight) — 15 works

## 📑 Paper List

<a id="branch-internal"></a>

## Internal Capabilities of Vision-Centric Agents

<a id="category-perception"></a>

### Vision Perception Capability

<a id="topic-vision-perception-grounded"></a>

#### Grounded Perception

77 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | CVPR | ★ CogAgent | [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914) | [Code 1](https://github.com/zai-org/CogVLM) · [Code 2](https://github.com/zai-org/CogAgent) |
| 2024 | ACL | ★ SeeClick | [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) | [Code](https://github.com/njucckevin/SeeClick) |
| 2025 | ICLR | ★ UGround | [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://doi.org/10.48550/arxiv.2410.05243) · [arXiv](https://arxiv.org/abs/2410.05243) | [Project](https://osu-nlp-group.github.io/UGround/) · [Code](https://github.com/OSU-NLP-Group/UGround) |
| 2025 | ICLR | ★ OS-ATLAS | [OS-ATLAS: Foundation action model for generalist GUI agents](https://arxiv.org/abs/2410.23218) | — |
| 2025 | CVPR | ★ ShowUI | [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465) | [Code](https://github.com/showlab/ShowUI) |
| 2025 | arXiv | ★ UI-TARS | [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) | — |
| 2025 | CVPR | ★ Magma | [Magma: A Foundation Model for Multimodal AI Agents](https://arxiv.org/abs/2502.13130) | — |
| 2025 | arXiv | ★ Qwen2.5-VL | [Qwen2.5-VL Technical Report](https://arxiv.org/abs/2502.13923) | [Code](https://github.com/QwenLM/Qwen2.5-VL) |
| 2026 | NeurIPS | ★ GUI-Actor | [GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents](https://arxiv.org/abs/2506.03143) | [Code](https://github.com/microsoft/GUI-Actor) |
| 2026 | NeurIPS | ★ GUI-G1 | [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810) | [Code](https://github.com/Yuqi-Zhou/GUI-G1) |
| 2026 | ICLR | ★ UI-Ins | [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286) | [Code](https://github.com/alibaba/UI-Ins) |
| 2025 | arXiv | ★ RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2019 | ACL | — | [A Corpus for Reasoning about Natural Language Grounded in Photographs](https://aclanthology.org/P19-1644/) | — |
| 2025 | arXiv | Active-o3 | [Active-o3: Empowering multimodal large language models with active perception via grpo](https://arxiv.org/abs/2505.21457) | — |
| 2026 | arXiv | ActiveScope | [ActiveScope: Actively Seeking and Correcting Perception for MLLMs](https://arxiv.org/abs/2606.24292) | [Code](https://github.com/jasmine-ww/ActiveScope) |
| 2025 | arXiv | — | [Adaptive Chain-of-Focus Reasoning via Dynamic Visual Search and Zooming for Efficient VLMs](https://arxiv.org/abs/2505.15436) | [Code](https://github.com/xtong-zhang/Chain-of-Focus) |
| 2025 | EMNLP Demos | AgentCPM-GUI | [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.01391) | [Code](https://github.com/OpenBMB/AgentCPM-GUI) |
| 2026 | ICLR | — | [Agentic Jigsaw Interaction Learning for Enhancing Visual Perception and Reasoning in Vision-Language Models](https://arxiv.org/abs/2510.01304) | [Code](https://github.com/yuzeng0-0/AGILE) |
| 2021 | NeurIPS | — | Align before fuse: Vision and language representation learning with momentum distillation | — |
| 2023 | arXiv | Android in the Wild | [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) | — |
| 2024 | arXiv | AndroidLab | [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://arxiv.org/abs/2410.24024) | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 2025 | CHI | AppAgent | [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) | [Project](https://appagent-official.github.io/) · [Code](https://github.com/TencentQQGYLab/AppAgent) |
| 2026 | arXiv | AutoFocus | [AutoFocus: Uncertainty-Aware Active Visual Search for GUI Grounding](https://arxiv.org/abs/2605.02630) | [Code](https://github.com/Mr-Bigworth/AutoFocus) |
| 2024 | arXiv | BLINK | [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) | — |
| 2023 | ICML | BLIP-2 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | — |
| 2026 | arXiv | BVS | [BVS: Bayesian Visual Search with Multimodal Large Language Model for Fine-grained Perception](https://arxiv.org/abs/2607.03184) | [Code](https://github.com/PKU-ICST-MIPL/BVS_ICML2026) |
| 2026 | ICLR | CP-Agent | [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435) | — |
| 2026 | arXiv | — | [Design Choices That Matter: A Functional ANOVA Analysis for Remote Sensing Multi-Label Classification](https://arxiv.org/abs/2608.04702) | — |
| 2025 | AAAI | Divide, Conquer and Combine | [Divide, Conquer and Combine: A Training-Free Framework for High-Resolution Image Perception in Multimodal Large Language Models](https://github.com/DreamMr/HR-Bench) | [Code](https://github.com/DreamMr/HR-Bench) |
| 2026 | ICLR | DriveAgent-R1 | [DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking](https://arxiv.org/abs/2507.20879) | [Code](https://github.com/wczheng/DriveAgent-R1) |
| 2024 | RSS | DROID | [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://arxiv.org/abs/2403.12945) | [Project](https://droid-dataset.github.io/) · [Code 1](https://github.com/droid-dataset/droid) · [Code 2](https://github.com/droid-dataset/droid_policy_learning) |
| 2025 | CVPR | DyFo | [DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding](https://arxiv.org/abs/2504.14920) | [Code](https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025) |
| 2025 | arXiv | — | [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370) | [Code](https://github.com/YXB-NKU/SE-GUI) |
| 2025 | NAACL Findings | — | [Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement](https://arxiv.org/abs/2405.15973) | — |
| 2023 | NeurIPS | — | [From Pixels to UI Actions: Learning to Follow Instructions via Graphical User Interfaces](https://doi.org/10.48550/arxiv.2306.00245) · [arXiv](https://arxiv.org/abs/2306.00245) | [Code](https://github.com/google-deepmind/pix2act) |
| 2023 | arXiv | — | [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805) | — |
| 2026 | CVPR | GeoMMBench and GeoMMAgent | [GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing](https://arxiv.org/abs/2604.08896) | — |
| 2024 | ICML | — | [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) | [Code](https://github.com/OSU-NLP-Group/SeeAct) |
| 2025 | arXiv | GR00T N1 | [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) | [Project](https://developer.nvidia.com/isaac/gr00t) · [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 2025 | ICLR | GUI-World | [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://arxiv.org/abs/2406.10819) | [Project](https://gui-world.github.io) · [Code](https://github.com/Dongping-Chen/GUI-World) |
| 2026 | arXiv | InternVL-U | [InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing](https://arxiv.org/abs/2603.09877) | [Code](https://github.com/OpenGVLab/InternVL-U) |
| 2024 | CVPR | InternVL | [InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks](https://arxiv.org/abs/2312.14238) | [Code](https://github.com/OpenGVLab/InternVL) |
| 2025 | ICCV | — | [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342) | — |
| 2026 | CVPR | iSHIFT | [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009) | — |
| 2021 | ICML | — | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | [Code](https://github.com/OpenAI/CLIP) |
| 2019 | arXiv | LVIS | [LVIS: A Dataset for Large Vocabulary Instance Segmentation](https://arxiv.org/abs/1908.03195) | — |
| 2025 | arXiv | MAI-UI Technical Report | [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047) | — |
| 2016 | arXiv | — | [Modeling Context in Referring Expressions](https://arxiv.org/abs/1608.00272) | — |
| 2026 | ECCV | MolmoWeb | [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516) | [Project](https://allenai.org/blog/molmoweb) · [Code](https://github.com/allenai/molmoweb) |
| 2026 | ECCV | NeuroRefiner | [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](https://arxiv.org/abs/2608.09636) | — |
| 2026 | Official Release | NVIDIA Isaac GR00T N1.7 | [NVIDIA Isaac GR00T N1.7: A Foundation Model for Generalist Robots](https://github.com/NVIDIA/Isaac-GR00T) | [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 2024 | ECCV | OmniACT | [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553) | — |
| 2026 | ICLR | OmniActor | [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322) | — |
| 2024 | arXiv | — | [On the Effects of Data Scale on UI Control Agents](https://arxiv.org/abs/2406.03679) | — |
| 2026 | CVPR | OVOD-Agent | [OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection](https://arxiv.org/abs/2511.21064) | — |
| 2026 | arXiv | PrecisionCUA | [PrecisionCUA: Iterative Visual Refinement for Pixel-Precise Cursor Grounding in Code Editors](https://arxiv.org/abs/2604.13019) | [Code](https://github.com/microsoft/precision-cua-bench/tree/main) |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |
| 2026 | arXiv | Qwen-UI-Agent Technical Report | [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227) | — |
| 2024 | arXiv | Qwen2-VL | [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191) | [Code](https://github.com/QwenLM/Qwen3-VL) |
| 2025 | arXiv | — | [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631) | [Code](https://github.com/QwenLM/Qwen3-VL) |
| 2026 | CVPR | ReSAM | [ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images](https://arxiv.org/abs/2511.21606) | — |
| 2026 | ICLR | ScaleCUA | [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://doi.org/10.48550/arxiv.2509.15221) · [arXiv](https://arxiv.org/abs/2509.15221) | [Code](https://github.com/OpenGVLab/ScaleCUA) |
| 2025 | ACM MM | ScreenSpot-Pro | [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981) | [Project](https://gui-agent.github.io/grounding-leaderboard) · [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| 2026 | CVPR | — | [See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles](https://arxiv.org/abs/2509.13615) | [Code](https://github.com/ZrW00/StaR) |
| 2022 | arXiv | — | [Towards Large-Scale Small Object Detection: Survey and Benchmarks](https://arxiv.org/abs/2207.14096) | — |
| 2025 | arXiv | UI-TARS-2 Technical Report | [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) | — |
| 2026 | arXiv | — | [UI-Venus-2 Technical Report](https://arxiv.org/abs/2609.00028) | — |
| 2025 | ICCV | UIPro | [UIPro: Unleashing Superior Interaction Capability For GUI Agents](https://arxiv.org/abs/2509.17328) | [Code](https://github.com/ZJULiHongxin/UIPro) |
| 2024 | CVPR | — | [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://doi.org/10.1109/cvpr52733.2024.01243) · [arXiv](https://arxiv.org/abs/2312.14135) | [Code](https://github.com/penghao-wu/vstar) |
| 2023 | NeurIPS | — | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | [Project](https://llava-vl.github.io/) · [Code](https://github.com/haotian-liu/LLaVA) |
| 2024 | ACL | VisualWebArena | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | — |
| 2022 | arXiv | WebShop | [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) | — |
| 2024 | ACL | WebVoyager | [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) | — |
| 2017 | ICML | World of Bits | [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) | — |
| 2025 | arXiv | π_0.5 | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | — |
| 2026 | arXiv | π_0.7 | [π_0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483) | — |

<a id="topic-vision-perception-temporal"></a>

#### Temporal Perception

35 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | ECCV | ★ VideoAgent (Fan) | [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) | [Project](http://videoagent.github.io) · [Code](https://github.com/YueFan1014/VideoAgent) |
| 2024 | ECCV | ★ VideoAgent (Wang) | [VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517) | — |
| 2025 | CVPR | ★ VideoTree | [VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos](https://arxiv.org/abs/2405.19209) | [Project](https://videotree2024.github.io/) · [Code](https://github.com/Ziyang412/VideoTree) |
| 2026 | ICLR | ★ VideoMind | [VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](https://arxiv.org/abs/2503.13444) | [Project](https://videomind.github.io/) · [Code](https://github.com/yeliudev/VideoMind) |
| 2025 | arXiv | ★ VideoAgent2 | [VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT](https://arxiv.org/abs/2504.04471) | — |
| 2025 | arXiv | ★ VideoExplorer | [VideoExplorer: Think With Videos For Agentic Long-Video Understanding](https://arxiv.org/abs/2506.10821) | [Code](https://github.com/RUC-NLPIR/VideoDeepResearch) |
| 2026 | ICLR | ★ M3-Agent | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | [Code](https://github.com/bytedance-seed/m3-agent) |
| 2026 | CVPR | ★ WorldMM | [WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://arxiv.org/abs/2512.02425) | [Project](https://worldmm.github.io) · [Code](https://github.com/wgcyeo/WorldMM) |
| 2025 | ICCV | ★ Embodied VideoAgent | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | [Project](https://embodied-videoagent.github.io/) · [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |
| 2025 | arXiv | ★ StreamVLN | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://arxiv.org/abs/2507.05240) | — |
| 2026 | NeurIPS | ★ VideoChat-R1.5 | [VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception](https://arxiv.org/abs/2509.21100) | — |
| 2026 | CVPR | ★ LensWalk | [LensWalk: Agentic Video Understanding by Planning How You See in Videos](https://arxiv.org/abs/2603.24558) | — |
| 2012 | ECCV | — | A Naturalistic Open Source Movie for Optical Flow Evaluation | — |
| 2025 | arXiv | — | [Agentic Keyframe Search for Video Question Answering](https://arxiv.org/abs/2503.16032) | [Code](https://github.com/fansunqi/AKeyS) |
| 2024 | arXiv | CG-Bench | [CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://arxiv.org/abs/2412.12075) | — |
| 2021 | arXiv | Ego4D | [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058) | — |
| 2025 | arXiv | EgoLife | [EgoLife: Towards Egocentric Life Assistant](https://arxiv.org/abs/2503.03803) | — |
| 2023 | arXiv | EgoSchema | [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://arxiv.org/abs/2308.09126) | — |
| 2026 | arXiv | EVA | [EVA: Efficient Reinforcement Learning for End-to-End Video Agent](https://arxiv.org/abs/2603.22918) | — |
| 2025 | ICLR | GUI-World | [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://arxiv.org/abs/2406.10819) | [Project](https://gui-world.github.io) · [Code](https://github.com/Dongping-Chen/GUI-World) |
| 2023 | ICCV | IntentQA | [IntentQA: Context-aware Video Intent Reasoning](https://github.com/JoseponLee/IntentQA) | [Code](https://github.com/JoseponLee/IntentQA) |
| 2024 | NeurIPS | LongVideoBench | [LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding](https://arxiv.org/abs/2407.15754) | [Code](https://github.com/LongVideoBench/LongVideoBench) |
| 2024 | arXiv | LVBench | [LVBench: An Extreme Long Video Understanding Benchmark](https://arxiv.org/abs/2406.08035) | — |
| 2024 | arXiv | MLVU | [MLVU: Benchmarking Multi-task Long Video Understanding](https://arxiv.org/abs/2406.04264) | — |
| 2023 | arXiv | MVBench | [MVBench: A Comprehensive Multi-modal Video Understanding Benchmark](https://arxiv.org/abs/2311.17005) | — |
| 2024 | arXiv | NaVid | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852) | — |
| 2021 | CVPR | NExT-QA | [NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions](https://openaccess.thecvf.com/content/CVPR2021/papers/Xiao_NExT-QA_Next_Phase_of_Question-Answering_to_Explaining_Temporal_Actions_CVPR_2021_paper.pdf) · [arXiv](https://arxiv.org/abs/2105.08276) | [Code](https://github.com/doc-doc/NExT-QA) |
| 2020 | CVPR | nuScenes | [nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027) | [Code](https://github.com/nutonomy/nuscenes-devkit) |
| 2024 | arXiv | ReXTime | [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://arxiv.org/abs/2406.19392) | — |
| 2020 | arXiv | Room-Across-Room | [Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding](https://arxiv.org/abs/2010.07954) | — |
| 2026 | CVPR | SciEducator | [SciEducator: Scientific Video Understanding and Educating via Deming-Cycle Multi-Agent System](https://arxiv.org/abs/2511.17943) | — |
| 2025 | CVPR | Video-MME | [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075) | [Project](https://video-mme.github.io) |
| 2026 | ICLR | Video-STAR | [Video-STAR: Reinforcing Open-Vocabulary Action Recognition with Tools](https://arxiv.org/abs/2510.08480) | — |
| 2026 | arXiv | VideoAgent | [VideoAgent: All-in-One Framework for Video Understanding and Editing](https://arxiv.org/abs/2606.23327) | [Code](https://github.com/HKUDS/VideoAgent) |
| 2026 | CVPR | VideoARM | [VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding](https://arxiv.org/abs/2512.12360) | [Project](https://milvlg.github.io/videoarm/) · [Code](https://github.com/MILVLG/videoarm) |

<a id="topic-vision-perception-spatial"></a>

#### Spatial Perception

28 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2020 | ECCV | ★ ScanRefer | [ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language](https://arxiv.org/abs/1912.08830) | [Project](https://daveredrum.github.io/ScanRefer/) · [Code](https://github.com/daveredrum/ScanRefer) |
| 2020 | ECCV | ★ ReferIt3D | [ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf) | [Code](https://github.com/referit3d/referit3d) |
| 2025 | arXiv | ★ SpatialVLA | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830) | — |
| 2024 | arXiv | ★ RoboPoint | [RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics](https://arxiv.org/abs/2406.10721) | — |
| 2024 | NeurIPS | ★ SG-Nav | [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189) | [Project](https://bagh2178.github.io/SG-Nav/) · [Code](https://github.com/bagh2178/SG-Nav) |
| 2026 | CVPR | ★ REALM | [REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410) | [Project](https://ChangyueShi.github.io/REALM) · [Code](https://github.com/ChangyueShi/REALM-Code) |
| 2025 | ICCV | ★ Embodied VideoAgent | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | [Project](https://embodied-videoagent.github.io/) · [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |
| 2026 | CVPR | ★ ActiveVLA | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/abs/2601.08325) | — |
| 2025 | ICRA | ★ BUMBLE | [BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation](https://arxiv.org/abs/2410.06237) | [Project](https://robin-lab.cs.utexas.edu/BUMBLE/) · [Code](https://github.com/UT-Austin-RobIn/BUMBLE) |
| 2023 | arXiv | ★ VoxPoser | [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973) | [Project](https://voxposer.github.io) · [Code](https://github.com/huangwl18/VoxPoser) |
| 2024 | arXiv | ★ MOKA | [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | — |
| 2026 | ECCV | ★ Agentic 3D Cognition | [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649) | [Project](https://zhangbo135.github.io/agentic-collaborative-cognition/) |
| 2021 | ICCV | 3D-FRONT | [3D-FRONT: 3D Furnished Rooms With layOuts and semaNTics](https://openaccess.thecvf.com/content/ICCV2021/html/Fu_3D-FRONT_3D_Furnished_Rooms_With_layOuts_and_semaNTics_ICCV_2021_paper.html) | — |
| 2026 | ICML | 3DMedAgent | [3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis](https://arxiv.org/abs/2602.18064) | [Project](http://assistants.Code) · [Code](https://github.com/jinlab-imvr/3DMedAgent) |
| 2020 | arXiv | Beyond the Nav-Graph | [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857) | — |
| 2024 | arXiv | BLINK | [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) | — |
| 2026 | TGRS | DisasterTD | [DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization](https://arxiv.org/abs/2607.24856) | — |
| 2021 | arXiv | — | [Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://arxiv.org/abs/2109.08238) | — |
| 2026 | arXiv | LEGO-Anything | [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380) | — |
| 2025 | arXiv | — | [Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception](https://arxiv.org/abs/2511.15279) | — |
| 2017 | arXiv | Matterport3D | [Matterport3D: Learning from RGB-D Data in Indoor Environments](https://arxiv.org/abs/1709.06158) | — |
| 2025 | RSS | NaVILA | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453) | [Project](https://navila-bot.github.io/) |
| 2020 | CVPR | nuScenes | [nuScenes: A multimodal dataset for autonomous driving](https://arxiv.org/abs/1903.11027) | [Code](https://github.com/nutonomy/nuscenes-devkit) |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |
| 2020 | arXiv | Room-Across-Room | [Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding](https://arxiv.org/abs/2010.07954) | — |
| 2026 | ECCV | TopoAgent | [TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging](https://arxiv.org/abs/2606.29763) | [Code](https://github.com/gm3g11/TopoAgent) |
| 2023 | ICCV | VAD | [VAD: Vectorized Scene Representation for Efficient Autonomous Driving](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_VAD_Vectorized_Scene_Representation_for_Efficient_Autonomous_Driving_ICCV_2023_paper.html) · [arXiv](https://arxiv.org/abs/2303.12077) | [Code](https://github.com/hustvl/VAD) |
| 2017 | arXiv | Vision-and-Language Navigation | [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280) | — |

<a id="category-reasoning"></a>

### Vision Reasoning Capability

<a id="topic-reasoning-interleaved"></a>

#### Interleaved Multimodal Reasoning

18 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | EMNLP | ★ LATTE | [LATTE: Learning to Think with Vision Specialists](https://arxiv.org/abs/2412.05479) | — |
| 2025 | arXiv | ★ OpenThinkIMG | [OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning](https://arxiv.org/abs/2505.08617) | [Code](https://github.com/zhaochen0110/OpenThinkIMG) |
| 2026 | ICLR | ★ DeepEyes | [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://arxiv.org/abs/2505.14362) | [Code](https://github.com/Visual-Agent/DeepEyes) |
| 2026 | NeurIPS | ★ Pixel Reasoner | [Pixel reasoner: Incentivizing pixel space reasoning via curiosity-driven reinforcement learning](https://arxiv.org/abs/2505.15966) | [Project 1](https://tiger-ai-lab.github.io/Pixel-Reasoner/) · [Project 2](https://huggingface.co/spaces/TIGER-Lab/Pixel-Reasoner) · [Code](https://github.com/TIGER-AI-Lab/Pixel-Reasoner) |
| 2026 | ICLR | ★ VTool-R1 | [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255) | [Code](https://github.com/VTOOL-R1/vtool-r1) |
| 2025 | arXiv | ★ PyVision | [PyVision: Agentic Vision with Dynamic Tooling](https://arxiv.org/abs/2507.07998) | [Code](https://github.com/agents-x-project/PyVision) |
| 2025 | arXiv | ★ Thyme | [Thyme: Think Beyond Images](https://arxiv.org/abs/2508.11630) | [Project](https://thyme-vl.github.io/) · [Code](https://github.com/yfzhang114/Thyme) |
| 2026 | ICLR | ★ DeepEyesV2 | [DeepEyesV2: Toward Agentic Multimodal Model](https://arxiv.org/abs/2511.05271) | [Project](https://visual-agent.github.io/) · [Code](https://github.com/Visual-Agent/DeepEyesV2) |
| 2026 | CVPR | ★ CodeV | [CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization](https://arxiv.org/abs/2511.19661) | [Code](https://github.com/RenlyH/CodeV) |
| 2024 | NeurIPS | ★ Visual Sketchpad | [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://doi.org/10.52202/079017-4423) · [arXiv](https://arxiv.org/abs/2406.09403) | [Project](https://visualsketchpad.github.io/) · [Code](https://github.com/Yushi-Hu/VisualSketchpad) |
| 2026 | ICLR | ★ InSight-o3 | [InSight-o3: Empowering Multimodal Foundation Models with Generalized Visual Search](https://arxiv.org/abs/2512.18745) | [Code](https://github.com/m-Just/InSight-o3) |
| 2026 | ICLR | ★ VideoMind | [VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](https://arxiv.org/abs/2503.13444) | [Project](https://videomind.github.io/) · [Code](https://github.com/yeliudev/VideoMind) |
| 2025 | arXiv | GoT | [GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing](https://arxiv.org/abs/2503.10639) | [Code](https://github.com/rongyaofang/GoT) |
| 2026 | ICLR | — | [Latent Visual Reasoning](https://arxiv.org/abs/2509.24251) | [Code](https://github.com/VincentLeebang/lvr) |
| 2026 | ICML | — | [Ophiuchus: Incentivizing Tool-augmented "Think with Images" for Joint Medical Segmentation, Understanding and Reasoning](https://arxiv.org/abs/2512.14157) | [Code](https://github.com/SII-zyj/Ophiuchus) |
| 2025 | arXiv | — | [Qwen Look Again: Guiding Vision-Language Reasoning Models to Re-attention Visual Information](https://arxiv.org/abs/2505.23558) | [Code](https://github.com/Liar406/Look_Again) |
| 2025 | arXiv | — | [Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers](https://arxiv.org/abs/2506.23918) | [Code](https://github.com/zhaochen0110/Awesome_Think_With_Images) |
| 2026 | ECCV | TIR-Bench | [TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning](https://arxiv.org/abs/2511.01833) | [Code](https://github.com/agents-x-project/TIR-Bench) |

<a id="topic-reasoning-grounded"></a>

#### Visually Grounded Reasoning

81 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | CVPR | ★ GCA | [Geometrically-Constrained Agent for Spatial Reasoning](https://arxiv.org/abs/2511.22659) | [Project](https://gca-spatial-reasoning.github.io) · [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2024 | arXiv | ★ ReKep | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |
| 2023 | arXiv | ★ VoxPoser | [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973) | [Project](https://voxposer.github.io) · [Code](https://github.com/huangwl18/VoxPoser) |
| 2024 | arXiv | ★ MOKA | [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | — |
| 2024 | NeurIPS | ★ SG-Nav | [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189) | [Project](https://bagh2178.github.io/SG-Nav/) · [Code](https://github.com/bagh2178/SG-Nav) |
| 2025 | ICRA | ★ BUMBLE | [BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation](https://arxiv.org/abs/2410.06237) | [Project](https://robin-lab.cs.utexas.edu/BUMBLE/) · [Code](https://github.com/UT-Austin-RobIn/BUMBLE) |
| 2026 | ICLR | ★ InSight-o3 | [InSight-o3: Empowering Multimodal Foundation Models with Generalized Visual Search](https://arxiv.org/abs/2512.18745) | [Code](https://github.com/m-Just/InSight-o3) |
| 2026 | CVPR | ★ REALM | [REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410) | [Project](https://ChangyueShi.github.io/REALM) · [Code](https://github.com/ChangyueShi/REALM-Code) |
| 2025 | arXiv | ★ RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2024 | NeurIPS | ★ Visual Sketchpad | [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://doi.org/10.52202/079017-4423) · [arXiv](https://arxiv.org/abs/2406.09403) | [Project](https://visualsketchpad.github.io/) · [Code](https://github.com/Yushi-Hu/VisualSketchpad) |
| 2026 | ICLR | ★ UI-Ins | [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286) | [Code](https://github.com/alibaba/UI-Ins) |
| 2025 | ICCV | ★ RegionFocus | [Visual Test-time Scaling for GUI Agent Grounding](https://arxiv.org/abs/2505.00684) | [Code](https://github.com/tiangeluo/RegionFocus) |
| 2019 | ACL | — | [A Corpus for Reasoning about Natural Language Grounded in Photographs](https://aclanthology.org/P19-1644/) | — |
| 2026 | arXiv | — | [A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692) | — |
| 2026 | KDD | — | [Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory](https://arxiv.org/abs/2603.15280) | — |
| 2026 | ICLR | Agent-X | [Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks](https://arxiv.org/abs/2505.24876) | [Code](https://github.com/mbzuai-oryx/Agent-X) |
| 2026 | ICLR | — | [Agentic Jigsaw Interaction Learning for Enhancing Visual Perception and Reasoning in Vision-Language Models](https://arxiv.org/abs/2510.01304) | [Code](https://github.com/yuzeng0-0/AGILE) |
| 2026 | ECCV | AgentVLN | [AgentVLN: Towards Agentic Vision-and-Language Navigation](https://arxiv.org/abs/2603.17670) | [Code](https://github.com/Allenxinn/AgentVLN) |
| 2026 | ICML | AutoMat | [AutoMat: Physics-Guided Agentic Reasoning for Solving Ill-Posed Inverse Microscopy Problems](https://openreview.net/forum?id=TLroFiKilA) · [arXiv](https://arxiv.org/abs/2505.12650) | [Code](https://github.com/yyt-2378/AutoMat) |
| 2025 | NeurIPS | AutoVLA | [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | [Project](https://autovla.github.io/) · [Code](https://github.com/ucla-mobility/AutoVLA) |
| 2026 | CVPR | AwareVLN | [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://arxiv.org/abs/2605.22816) | [Project](https://gwxuan.github.io/AwareVLN/) · [Code](https://github.com/GWxuan/AwareVLN) |
| 2024 | arXiv | ChartGemma | [ChartGemma: Visual Instruction-tuning for Chart Reasoning in the Wild](https://arxiv.org/abs/2407.04172) | — |
| 2024 | NeurIPS | — | [Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation](https://arxiv.org/abs/2409.09016) | [Code](https://github.com/OpenDriveLab/CLOVER) |
| 2026 | arXiv | — | [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](https://arxiv.org/abs/2607.08497) | [Project](https://caseclose.github.io/cma-harness/) · [Code](https://github.com/caseclose/cma-harness) |
| 2026 | ICLR | CP-Agent | [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435) | — |
| 2025 | NeurIPS | CPathAgent | [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://doi.org/10.52202/085713-3404) · [arXiv](https://arxiv.org/abs/2505.20510) | — |
| 2026 | TGRS | DisasterTD | [DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization](https://arxiv.org/abs/2607.24856) | — |
| 2026 | ICLR | DriveAgent-R1 | [DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking](https://arxiv.org/abs/2507.20879) | [Code](https://github.com/wczheng/DriveAgent-R1) |
| 2026 | CVPR | DriveMoE | [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_DriveMoE_Mixture-of-Experts_for_Vision-Language-Action_Model_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2505.16278) | — |
| 2026 | arXiv | Fast-ThinkAct | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) | — |
| 2025 | arXiv | Game-TARS | [Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents](https://arxiv.org/abs/2510.23691) | — |
| 2025 | arXiv | — | [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://arxiv.org/abs/2510.03342) | — |
| 2023 | arXiv | — | [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805) | — |
| 2026 | ECCV | GenAgent | [GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning](https://arxiv.org/abs/2601.18543) | [Code](https://github.com/deep-kaixun/GenAgent) |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2026 | CVPR | GeoMMBench and GeoMMAgent | [GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing](https://arxiv.org/abs/2604.08896) | — |
| 2024 | ICML | — | [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://arxiv.org/abs/2401.01614) | [Code](https://github.com/OSU-NLP-Group/SeeAct) |
| 2019 | CVPR | GQA | [GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506) | — |
| 2026 | CVPR | IBISAgent | [IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation](https://arxiv.org/abs/2601.03054) | [Code](https://github.com/Yankai96/IBISAgent) |
| 2026 | arXiv | — | [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) | [Project](https://cheng-haha.github.io/GPT-Policy) · [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2023 | ICCV | IntentQA | [IntentQA: Context-aware Video Intent Reasoning](https://github.com/JoseponLee/IntentQA) | [Code](https://github.com/JoseponLee/IntentQA) |
| 2026 | arXiv | Kimi K2.5 | [Kimi K2.5: Visual Agentic Intelligence](https://arxiv.org/abs/2602.02276) | — |
| 2023 | arXiv | — | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) | — |
| 2023 | arXiv | LLM-grounded Diffusion | [LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models](https://arxiv.org/abs/2305.13655) | — |
| 2024 | CVPR | LMDrive | [LMDrive: Closed-Loop End-to-End Driving with Large Language Models](https://arxiv.org/abs/2312.07488) | [Project](https://hao-shao.com/projects/lmdrive.html) · [Code](https://github.com/opendilab/LMDrive) |
| 2023 | arXiv | MathVista | [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://arxiv.org/abs/2310.02255) | — |
| 2026 | ICLR | MedVR | [MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2604.08203) | [Code](https://github.com/alibaba-damo-academy/MedVR) |
| 2026 | ICLR | MMedAgent-RL | [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) | — |
| 2024 | CVPR | MMMU | [MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI](https://arxiv.org/abs/2311.16502) | [Code](https://github.com/MMMU-benchmark/MMMU) |
| 2023 | arXiv | — | [Multimodal Chain-of-Thought Reasoning in Language Models](https://arxiv.org/abs/2302.00923) | [Code](https://github.com/amazon-science/mm-cot) |
| 2026 | arXiv | MuSEAgent | [MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences](https://arxiv.org/abs/2603.27813) | — |
| 2024 | ECCV | NavGPT-2 | [NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](https://arxiv.org/abs/2407.12366) | [Code](https://github.com/GengzeZhou/NavGPT-2) |
| 2025 | RSS | NaVILA | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453) | [Project](https://navila-bot.github.io/) |
| 2021 | CVPR | NExT-QA | [NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions](https://openaccess.thecvf.com/content/CVPR2021/papers/Xiao_NExT-QA_Next_Phase_of_Question-Answering_to_Explaining_Temporal_Actions_CVPR_2021_paper.pdf) · [arXiv](https://arxiv.org/abs/2105.08276) | [Code](https://github.com/doc-doc/NExT-QA) |
| 2024 | arXiv | — | [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) | — |
| 2026 | arXiv | One MLLM, One Call | [One MLLM, One Call: Efficient Zero-Shot Vision-and-Language Navigation via Spatial-Aware Waypoints](https://arxiv.org/abs/2609.06476) | [Code](https://github.com/kkpsq/O2C-Nav-Code) |
| 2025 | arXiv | OneTwoVLA | [OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2505.11917) | — |
| 2024 | arXiv | OpenVLA | [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | — |
| 2023 | arXiv | PaLM-E | [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378) | — |
| 2026 | ICLR | PhyScensis | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://arxiv.org/abs/2602.14968) | — |
| 2023 | CVPR | — | [Planning-oriented Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2212.10156) | — |
| 2025 | ACL Findings | — | [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) | [Project](https://invinciblewyq.github.io/ponder-press-page/) |
| 2025 | arXiv | — | [Qwen Look Again: Guiding Vision-Language Reasoning Models to Re-attention Visual Information](https://arxiv.org/abs/2505.23558) | [Code](https://github.com/Liar406/Look_Again) |
| 2026 | arXiv | Qwen-RobotNav Technical Report | [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) | — |
| 2025 | ICCV | R1-VL | [R1-VL: Learning to Reason with Multimodal Large Language Models via Step-wise Group Relative Policy Optimization](https://arxiv.org/abs/2503.12937) | — |
| 2026 | arXiv | — | [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227) | — |
| 2024 | arXiv | ReXTime | [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://arxiv.org/abs/2406.19392) | — |
| 2026 | Official Release | — | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) | [Project](https://mistral.ai/news/robostral-navigate/) |
| 2023 | CoRL | RT-2 | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | [Project](https://robotics-transformer.github.io/) |
| 2026 | arXiv | RynnBrain | [RynnBrain: Open Embodied Foundation Models](https://arxiv.org/abs/2602.14979) | — |
| 2025 | CVPR | SimLingo | [SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Renz_SimLingo_Vision-Only_Closed-Loop_Autonomous_Driving_with_Language-Action_Alignment_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09594) | — |
| 2018 | arXiv | TallyQA | [TallyQA: Answering Complex Counting Questions](https://arxiv.org/abs/1810.12440) | — |
| 2026 | arXiv | Thinking with Imagination | [Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators](https://arxiv.org/abs/2606.06476) | — |
| 2020 | arXiv | Transporter Networks | [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/abs/2010.14406) | — |
| 2026 | arXiv | — | [Unifying Language-Action Understanding and Generation for Autonomous Driving](https://arxiv.org/abs/2603.01441) | — |
| 2017 | arXiv | Vision-and-Language Navigation | [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280) | — |
| 2026 | ICLR | Vision-r1 | Vision-r1: Incentivizing reasoning capability in multimodal large language models | — |
| 2024 | NeurIPS | Visual CoT | [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://arxiv.org/abs/2403.16999) | [Project](https://hao-shao.com/projects/viscot.html) · [Code](https://github.com/deepcs233/Visual-CoT) |
| 2026 | ICLR | — | [Visual Planning: Let's Think Only with Images](https://arxiv.org/abs/2505.11409) | [Code](https://github.com/yix8/VisualPlanning) |
| 2025 | arXiv | π_0.5 | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | — |
| 2024 | arXiv | π_0 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) | — |

<a id="topic-reasoning-tool-augmented"></a>

#### Tool-Augmented Visual Reasoning

43 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2023 | arXiv | ★ MM-REACT | [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381) | [Project](https://multimodal-react.github.io/) · [Code](https://github.com/microsoft/MM-REACT) |
| 2024 | ECCV | ★ LLaVA-Plus | [LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents](https://arxiv.org/abs/2311.05437) | — |
| 2024 | CVPR | ★ CLOVA | [CLOVA: A Closed-Loop Visual Assistant with Tool Usage and Update](https://arxiv.org/abs/2312.10908) | [Code](https://github.com/clova-tool/CLOVA-tool) |
| 2023 | NeurIPS | ★ AVIS | [AVIS: Autonomous Visual Information Seeking with Large Language Model Agent](https://doi.org/10.52202/075280-0040) · [arXiv](https://arxiv.org/abs/2306.08129) | — |
| 2024 | ECCV | ★ DetToolChain | [DetToolChain: A New Prompting Paradigm to Unleash Detection Ability of MLLM](https://arxiv.org/abs/2403.12488) | — |
| 2025 | ICML | ★ MedRAX | [MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673) | [Code](https://github.com/bowang-lab/MedRAX) |
| 2025 | arXiv | ★ VisTA | [VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection](https://arxiv.org/abs/2505.20289) | — |
| 2025 | arXiv | ★ MMSearch-R1 | [MMSearch-R1: Incentivizing LMMs to Search](https://arxiv.org/abs/2506.20670) | [Code](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) |
| 2026 | ICLR | ★ DeepEyesV2 | [DeepEyesV2: Toward Agentic Multimodal Model](https://arxiv.org/abs/2511.05271) | [Project](https://visual-agent.github.io/) · [Code](https://github.com/Visual-Agent/DeepEyesV2) |
| 2026 | ICLR | ★ VideoZoomer | [VideoZoomer: Reinforcement-Learned Temporal Focusing for Long Video Reasoning](https://arxiv.org/abs/2512.22315) | [Code](https://github.com/zsgvivo/VideoZoomer) |
| 2025 | CVPR | ★ SegAgent | [SegAgent: Exploring Pixel Understanding Capabilities in MLLMs by Imitating Human Annotator Trajectories](https://arxiv.org/abs/2503.08625) | [Code](https://github.com/aim-uofa/SegAgent) |
| 2025 | arXiv | ★ RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2025 | arXiv | — | [A Survey on Agentic Multimodal Large Language Models](https://arxiv.org/abs/2510.10991) | [Code](https://github.com/HJYao00/Awesome-Agentic-MLLMs) |
| 2025 | arXiv | — | [Adaptive Chain-of-Focus Reasoning via Dynamic Visual Search and Zooming for Efficient VLMs](https://arxiv.org/abs/2505.15436) | [Code](https://github.com/xtong-zhang/Chain-of-Focus) |
| 2026 | ICLR | AdaReasoner | [AdaReasoner: Dynamic Tool Orchestration for Iterative Visual Reasoning](https://arxiv.org/abs/2601.18631) | [Code](https://github.com/ssmisya/AdaReasoner) |
| 2025 | arXiv | AutoTool | [AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning](https://arxiv.org/abs/2512.13278) | [Code](https://github.com/Gen-Verse/Open-AgentRL) |
| 2026 | arXiv | Beacon | [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595) | — |
| 2023 | arXiv | — | [Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?](https://arxiv.org/abs/2302.11713) | — |
| 2024 | ICLR | CRITIC | [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) | — |
| 2026 | EACL | DART | [DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning](https://arxiv.org/abs/2512.07132) | [Code](https://github.com/nsivaku/dart) |
| 2026 | arXiv | — | [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/abs/2606.02357) | — |
| 2025 | ICCV | DWIM | [DWIM: Towards Tool-aware Visual Reasoning via Discrepancy-aware Workflow Generation & Instruct-Masking Tuning](https://arxiv.org/abs/2503.19263) | — |
| 2026 | CVPR Findings | — | [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | — |
| 2016 | arXiv | FVQA | [FVQA: Fact-based Visual Question Answering](https://arxiv.org/abs/1606.05433) | — |
| 2024 | NeurIPS | GTA | [GTA: A Benchmark for General Tool Agents](https://doi.org/10.52202/079017-2412) · [arXiv](https://arxiv.org/abs/2407.08713) | [Code](https://github.com/open-compass/GTA) |
| 2023 | NeurIPS | HuggingGPT | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | [Code](https://github.com/microsoft/JARVIS) |
| 2026 | arXiv | Kimi K2.5 | [Kimi K2.5: Visual Agentic Intelligence](https://arxiv.org/abs/2602.02276) | — |
| 2025 | EMNLP | LATTE | [LATTE: Learning to Think with Vision Specialists](https://arxiv.org/abs/2412.05479) | — |
| 2026 | arXiv | MetaForge | [MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand](https://arxiv.org/abs/2606.01801) | — |
| 2025 | arXiv | Octopus | [Octopus: Agentic Multimodal Reasoning with Six-Capability Orchestration](https://arxiv.org/abs/2511.15351) | — |
| 2024 | arXiv | OK-Robot | [OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics](https://arxiv.org/abs/2401.12202) | [Project](https://ok-robot.github.io) · [Code](https://github.com/ok-robot/ok-robot) |
| 2019 | CVPR | OK-VQA | [OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge](https://openaccess.thecvf.com/content_CVPR_2019/html/Marino_OK-VQA_A_Visual_Question_Answering_Benchmark_Requiring_External_Knowledge_CVPR_2019_paper.html) | — |
| 2025 | arXiv | OpenThinkIMG | [OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning](https://arxiv.org/abs/2505.08617) | [Code](https://github.com/zhaochen0110/OpenThinkIMG) |
| 2026 | ICML | — | [Ophiuchus: Incentivizing Tool-augmented "Think with Images" for Joint Medical Segmentation, Understanding and Reasoning](https://arxiv.org/abs/2512.14157) | [Code](https://github.com/SII-zyj/Ophiuchus) |
| 2026 | arXiv | ParaVT | [ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning](https://arxiv.org/abs/2605.20342) | [Project](https://evolvinglmms-lab.github.io/ParaVT/) · [Code](https://github.com/EvolvingLMMs-Lab/ParaVT) |
| 2023 | ICLR | ReAct | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | [Project](https://react-lm.github.io) · [Code](https://github.com/ysymyth/ReAct) |
| 2026 | ICLR | ReTool | [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) | — |
| 2026 | CVPR | — | [Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs](https://arxiv.org/abs/2511.19773) | — |
| 2026 | ECCV | TIR-Agent | [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) | — |
| 2026 | ECCV | TIR-Bench | [TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning](https://arxiv.org/abs/2511.01833) | [Code](https://github.com/agents-x-project/TIR-Bench) |
| 2023 | NeurIPS | — | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | — |
| 2026 | ICLR | Video-STAR | [Video-STAR: Reinforcing Open-Vocabulary Action Recognition with Tools](https://arxiv.org/abs/2510.08480) | — |
| 2026 | arXiv | — | [Visual Reasoning through Tool-supervised Reinforcement Learning](https://arxiv.org/abs/2604.19945) | — |

<a id="topic-reasoning-programmatic"></a>

#### Programmatic Visual Reasoning

17 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2023 | CVPR | ★ VISPROG | [Visual Programming: Compositional visual reasoning without training](https://arxiv.org/abs/2211.11559) | [Code](https://github.com/allenai/visprog) |
| 2023 | ICCV | ★ ViperGPT | [ViperGPT: Visual Inference via Python Execution for Reasoning](https://openaccess.thecvf.com/content/ICCV2023/html/Suris_ViperGPT_Visual_Inference_via_Python_Execution_for_Reasoning_ICCV_2023_paper.html) · [arXiv](https://arxiv.org/abs/2303.08128) | [Project](https://viper.cs.columbia.edu/) · [Code](https://github.com/cvlab-columbia/viper) |
| 2025 | arXiv | ★ PyVision | [PyVision: Agentic Vision with Dynamic Tooling](https://arxiv.org/abs/2507.07998) | [Code](https://github.com/agents-x-project/PyVision) |
| 2025 | arXiv | ★ Thyme | [Thyme: Think Beyond Images](https://arxiv.org/abs/2508.11630) | [Project](https://thyme-vl.github.io/) · [Code](https://github.com/yfzhang114/Thyme) |
| 2026 | CVPR | ★ CodeV | [CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization](https://arxiv.org/abs/2511.19661) | [Code](https://github.com/RenlyH/CodeV) |
| 2026 | ICLR | ★ VTool-R1 | [VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use](https://arxiv.org/abs/2505.19255) | [Code](https://github.com/VTOOL-R1/vtool-r1) |
| 2024 | NeurIPS | ★ Visual Sketchpad | [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://doi.org/10.52202/079017-4423) · [arXiv](https://arxiv.org/abs/2406.09403) | [Project](https://visualsketchpad.github.io/) · [Code](https://github.com/Yushi-Hu/VisualSketchpad) |
| 2026 | CVPR | ★ GCA | [Geometrically-Constrained Agent for Spatial Reasoning](https://arxiv.org/abs/2511.22659) | [Project](https://gca-spatial-reasoning.github.io) · [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2024 | arXiv | ★ ReKep | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |
| 2024 | EMNLP Findings | ★ VDebugger | [VDebugger: Harnessing Execution Feedback for Debugging Visual Programs](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2025 | CVPR | ★ ViUniT | [ViUniT: Visual Unit Tests for More Robust Visual Programming](https://arxiv.org/abs/2412.08859) | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2026 | ICLR | ★ TVP | [Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning](https://arxiv.org/abs/2512.20934) | [Project](https://transductive-visualprogram.github.io/) · [Code](https://github.com/transductive-visualprogram/tvp) |
| 2023 | ICRA | — | [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | [Project](https://code-as-policies.github.io) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| 2025 | arXiv | Code-Vision | [Code-Vision: Evaluating Multimodal LLMs Logic Understanding and Code Generation Capabilities](https://arxiv.org/abs/2502.11829) | [Code](https://github.com/wanghanbinpanda/CodeVision) |
| 2026 | arXiv | LEGO-Anything | [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380) | — |
| 2026 | arXiv | PPTBench | [PPTBench: Can Coding Agents Reconstruct the Visual World through Structured, Editable Slides](https://arxiv.org/abs/2609.29718) | — |
| 2026 | CVPR | — | [Thinking with Programming Vision: Towards a Unified View for Thinking with Images](https://arxiv.org/abs/2512.03746) | [Code](https://github.com/ByteDance-BandAI/CodeVision) |

<a id="category-world"></a>

### Simulation of World Dynamics

<a id="topic-simulation-video"></a>

#### Video Simulation

36 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | ICML | ★ Genie | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | [Project](https://sites.google.com/corp/view/genie-2024/) |
| 2025 | arXiv | ★ Cosmos | [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | — |
| 2025 | CVPR | ★ NWM | [Navigation World Models](https://arxiv.org/abs/2412.03572) | [Project](https://www.amirbar.net/nwm/) · [Code](https://github.com/facebookresearch/nwm/) |
| 2024 | arXiv | ★ GEM | [GEM: A Generalizable Ego-Vision Multimodal World Model for Fine-Grained Ego-Motion, Object Dynamics, and Scene Composition Control](https://arxiv.org/abs/2412.11198) | — |
| 2025 | arXiv | ★ AdaWorld | [AdaWorld: Learning Adaptable World Models with Latent Actions](https://arxiv.org/abs/2503.18938) | — |
| 2025 | arXiv | ★ MineWorld | [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](https://arxiv.org/abs/2504.08388) | — |
| 2026 | ICLR | ★ ViMo | [ViMo: A Generative Visual GUI World Model for App Agents](https://doi.org/10.48550/arxiv.2504.13936) · [arXiv](https://arxiv.org/abs/2504.13936) | [Project](https://ai-agents-2030.github.io/ViMo/) · [Code](https://github.com/ai-agents-2030/ViMo) |
| 2025 | arXiv | ★ Ctrl-World | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) | — |
| 2026 | arXiv | ★ Cosmos Policy | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) | — |
| 2025 | arXiv | ★ Dreamer 4 | [Training Agents Inside of Scalable World Models](https://arxiv.org/abs/2509.24527) | — |
| 2025 | arXiv | ★ UWM | [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://arxiv.org/abs/2504.02792) | — |
| 2026 | arXiv | ★ DreamZero | [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | — |
| 2025 | arXiv | — | [Astra: General Interactive World Model with Autoregressive Denoising](https://arxiv.org/abs/2512.08931) | [Code](https://github.com/EternalEvan/Astra) |
| 2026 | arXiv | — | [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998) | — |
| 2024 | NeurIPS | — | [Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation](https://arxiv.org/abs/2409.09016) | [Code](https://github.com/OpenDriveLab/CLOVER) |
| 2024 | arXiv | — | [Diffusion for World Modeling: Visual Details Matter in Atari](https://arxiv.org/abs/2405.12399) | [Project](https://diamond-wm.github.io) · [Code](https://github.com/eloialonso/diamond) |
| 2025 | arXiv | DreamGen | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](https://arxiv.org/abs/2505.12705) | — |
| 2026 | ICLR | DriveVLA-W0 | [DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796) | [Code](https://github.com/BraveGroup/DriveVLA-W0) |
| 2026 | arXiv | Fast-WAM | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) | — |
| 2024 | arXiv | GR-2 | [GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](https://arxiv.org/abs/2410.06158) | — |
| 2026 | arXiv | — | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | [Project](https://vlaworld.github.io) |
| 2026 | arXiv | PlayWorld | [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552) | [Project](https://kxding.github.io/project/PlayWorld/) · [Code](https://github.com/hku-sail/PlayWorld) |
| 2026 | arXiv | RISE | [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075) | [Project](https://opendrivelab.com/RISE/) · [Code](https://github.com/OpenDriveLab/RISE) |
| 2026 | arXiv | — | [Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends](https://arxiv.org/abs/2606.01164) | [Code](https://github.com/liujiuming123/Awesome-Interactive-World-Model) |
| 2025 | ICML | — | [Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation](https://arxiv.org/abs/2410.05363) | [Project](https://phygenbench123.github.io/) · [Code](https://github.com/OpenGVLab/PhyGenBench) |
| 2024 | ICLR | — | [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](https://arxiv.org/abs/2312.13139) | — |
| 2026 | ICLR | — | [Vid2World: Crafting Video Diffusion Models to Interactive World Models](https://arxiv.org/abs/2505.14357) | [Project](http://knightnemo.github.io/vid2world/) · [Code](https://github.com/thuml/Vid2World) |
| 2026 | ICLR | VideoPhy-2 | [VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation](https://arxiv.org/abs/2503.06800) | [Project](https://videophy2.github.io/) · [Code](https://github.com/Hritikbansal/videophy/tree/main/VIDEOPHY2) |
| 2026 | arXiv | VLAW | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2026 | arXiv | WBench | [WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/abs/2605.25874) | [Project](https://meituan-longcat.github.io/WBench/) · [Code](https://github.com/meituan-longcat/WBench) |
| 2026 | arXiv | WEAVER, Better, Faster, Longer | [WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672) | [Project](https://arnavkj1995.github.io/WEAVER/) · [Code](https://github.com/arnavkj1995/WEAVER) |
| 2026 | ICLR | WMPO | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2511.09515) | [Project](https://wm-po.github.io) · [Code](https://github.com/WM-PO/WMPO) |
| 2026 | arXiv | — | [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | — |
| 2025 | arXiv | World-Env | [World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training](https://arxiv.org/abs/2509.24948) | [Code](https://github.com/amap-cvlab/world-env) |
| 2026 | arXiv | WorldMark | [WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686) | [Code](https://github.com/AlayaLab/WorldMark) |
| 2025 | arXiv | WorldVLA | [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539) | — |

<a id="topic-simulation-spatial"></a>

#### Spatial Simulation

17 works · 8 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | arXiv | ★ DOME | [DOME: Taming Diffusion Model into High-Fidelity Controllable Occupancy World Model](https://arxiv.org/abs/2410.10429) | — |
| 2025 | arXiv | ★ FlowDreamer | [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](https://arxiv.org/abs/2505.10075) | — |
| 2026 | NeurIPS | ★ 3D Persistent WM | [Learning 3D Persistent Embodied World Models](https://arxiv.org/abs/2505.05495) | — |
| 2026 | arXiv | ★ PERSIST | [Beyond Pixel Histories: World Models with Persistent 3D State](https://arxiv.org/abs/2603.03482) | — |
| 2025 | arXiv | ★ PhysTwin | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973) | — |
| 2025 | arXiv | ★ PhysWorld | [PhysWorld: From Real Videos to World Models of Deformable Objects via Physics-Aware Demonstration Synthesis](https://arxiv.org/abs/2510.21447) | — |
| 2026 | arXiv | ★ NGFF | [Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148) | — |
| 2026 | arXiv | ★ ContactGaussian-WM | [ContactGaussian-WM: Learning Physics-Grounded World Model from Videos](https://arxiv.org/abs/2602.11021) | — |
| 2017 | arXiv | CARLA | [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938) | — |
| 2021 | arXiv | — | [Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://arxiv.org/abs/2109.08238) | — |
| 2025 | NeurIPS | LabUtopia | [LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](https://doi.org/10.52202/085713-1158) · [arXiv](https://arxiv.org/abs/2505.22634) | — |
| 2024 | NeurIPS | NAVSIM | [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349) | [Code](https://github.com/autonomousvision/navsim) |
| 2025 | arXiv | — | [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | — |
| 2020 | arXiv | SAPIEN | [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515) | — |
| 2026 | arXiv | Thinking with Imagination | [Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators](https://arxiv.org/abs/2606.06476) | — |
| 2026 | arXiv | WAM4D | [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](https://arxiv.org/abs/2606.14048) | — |
| 2026 | ECCV | WorldAgents | [WorldAgents: Can Foundation Image Models be Agents for 3D World Models?](https://arxiv.org/abs/2603.19708) | [Project 1](https://ziyaerkoc.com/worldagents/) · [Project 2](https://www.youtube.com/watch?v=Mj2FqqhurdI) |

<a id="topic-simulation-latent"></a>

#### Latent Simulation

12 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2018 | arXiv | ★ World Models | [World Models](https://arxiv.org/abs/1803.10122) | [Project](https://worldmodels.github.io/) |
| 2019 | ICML | ★ PlaNet | [Learning Latent Dynamics for Planning from Pixels](https://arxiv.org/abs/1811.04551) | [Code](https://github.com/google-research/planet) |
| 2025 | Nature | ★ DreamerV3 | [Mastering Diverse Control Tasks through World Models](https://www.nature.com/articles/s41586-025-08744-2) · [arXiv](https://arxiv.org/abs/2301.04104) | [Code](https://github.com/danijar/dreamerv3) |
| 2023 | ICLR | ★ IRIS | [Transformers are Sample-Efficient World Models](https://arxiv.org/abs/2209.00588) | [Code](https://github.com/eloialonso/iris) |
| 2024 | ECCV | ★ Think2Drive | [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720) | — |
| 2024 | arXiv | ★ DINO-WM | [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983) | — |
| 2025 | arXiv | ★ V-JEPA 2 | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | [Code](https://github.com/facebookresearch/vjepa2) |
| 2026 | arXiv | ★ LeWM | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312) | — |
| 2025 | arXiv | ★ Raw2Drive | [Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)](https://arxiv.org/abs/2505.16394) | — |
| 2026 | arXiv | ★ AtomVLA | [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519) | — |
| 2026 | arXiv | ★ DriveWorld-VLA | [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| 2026 | arXiv | ★ Future-L1 | [Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video Event Prediction](https://arxiv.org/abs/2606.05769) | [Code](https://github.com/OpenGVLab/Future-L1) |

<a id="topic-simulation-semantic"></a>

#### Semantic Simulation

13 works · 8 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | arXiv | ★ VLWM | [Planning with Reasoning using Vision Language World Model](https://arxiv.org/abs/2509.02722) | — |
| 2025 | arXiv | ★ SWM | [Semantic World Models](https://arxiv.org/abs/2510.19818) | [Project](https://weirdlabuw.github.io/swm) |
| 2026 | ICLR | ★ R-WoM | [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://doi.org/10.48550/arxiv.2510.11892) · [arXiv](https://arxiv.org/abs/2510.11892) | — |
| 2026 | NeurIPS | ★ VAGEN | [VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://arxiv.org/abs/2510.16907) | [Project](https://vagen-ai.github.io) · [Code](https://github.com/mll-lab-nu/VAGEN) |
| 2025 | arXiv | ★ MobileWorldBench | [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) | — |
| 2025 | ICML | ★ WebDreamer | [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559) | — |
| 2026 | arXiv | ★ Code2World | [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | — |
| 2026 | arXiv | ★ MWM | [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347) | — |
| 2026 | ICLR | — | [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | — |
| 2026 | arXiv | ECHO | [ECHO: Terminal Agents Learn World Models for Free](https://arxiv.org/abs/2605.24517) | — |
| 2026 | EMNLP | — | [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388) | — |
| 2026 | arXiv | Qwen-AgentWorld | [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) | — |
| 2026 | arXiv | UI-Oceanus | [UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics](https://arxiv.org/abs/2604.02345) | — |

<a id="category-evaluation"></a>

### Visual Evaluation and Correction Abilities

<a id="topic-visual-evaluation-evidence"></a>

#### Visual Evidence Evaluation

13 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ LookBack | [VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning](https://arxiv.org/abs/2412.02172) | [Project](https://visco-benchmark.github.io/) · [Code](https://github.com/PlusLabNLP/VISCO) |
| 2026 | arXiv | ★ Perceval | [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) | [Code](https://github.com/RUCAIBox/Perceval) |
| 2026 | arXiv | ★ Kestrel | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2025 | CVPR | ★ RLAIF-V | [RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness](https://arxiv.org/abs/2405.17220) | [Code](https://github.com/RLHF-V/RLAIF-V) |
| 2026 | ICLR | ★ VideoMind | [VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](https://arxiv.org/abs/2503.13444) | [Project](https://videomind.github.io/) · [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | ECCV | ★ Reflect-R1 | [Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | arXiv | ★ ViSAGE | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | — |
| 2026 | ICLR | ★ CARE | [CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework](https://arxiv.org/abs/2603.01607) | [Project](https://xypb.github.io/CARE-Project-Page/) · [Code](https://github.com/XYPB/CARE) |
| 2025 | arXiv | ★ GAM-Agent | [GAM-Agent: Game-Theoretic and Uncertainty-Aware Collaboration for Complex Visual Reasoning](https://arxiv.org/abs/2505.23399) | [Code](https://github.com/jushengzhang/Gam-Agent) |
| 2025 | CVPR | ★ ViUniT | [ViUniT: Visual Unit Tests for More Robust Visual Programming](https://arxiv.org/abs/2412.08859) | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2026 | CVPR | ★ CodeV | [CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization](https://arxiv.org/abs/2511.19661) | [Code](https://github.com/RenlyH/CodeV) |
| 2026 | ECCV | ★ VERITAS | [VERITAS: A Multi-Agent Co-Scientist for Verifiable Image-Derived Hypothesis Testing](https://arxiv.org/abs/2604.12144) | [Code](https://github.com/LucZot/veritas) |
| 2026 | ICLR | MedAgent-Pro | [MedAgent-Pro: Towards Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow](https://arxiv.org/abs/2503.18968) | [Code](https://github.com/jinlab-imvr/MedAgent-Pro) |

<a id="topic-visual-evaluation-process"></a>

#### Visually Grounded Process Evaluation

19 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | ECCV | ★ VisCritic | [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525) | — |
| 2025 | CVPR | ★ Code-as-Monitor | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2025 | arXiv | ★ RoboFAC | [RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction](https://arxiv.org/abs/2505.12224) | [Code](https://github.com/MINT-SJTU/RoboFAC) |
| 2026 | CVPR | ★ OS-Oracle | [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](https://arxiv.org/abs/2512.16295) | [Code](https://github.com/numbmelon/OS-Oracle) |
| 2026 | arXiv | ★ GAIA | [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197) | [Code](https://github.com/SeerRay-Lab/GAIA) |
| 2025 | NeurIPS | ★ UI-Genie | [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://doi.org/10.52202/085713-5028) · [arXiv](https://arxiv.org/abs/2505.21496) | [Code](https://github.com/Euphoria16/UI-Genie) |
| 2024 | arXiv | ★ Sentinel | [Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress](https://arxiv.org/abs/2410.04640) | [Project](https://sites.google.com/stanford.edu/sentinel) · [Code](https://github.com/agiachris/sentinel) |
| 2024 | arXiv | ★ AHA | [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://arxiv.org/abs/2410.00371) | [Project](https://aha-vlm.github.io/) · [Code](https://github.com/NVlabs/AHA/tree/main) |
| 2023 | arXiv | ★ REFLECT | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |
| 2024 | EMNLP Findings | ★ VDebugger | [VDebugger: Harnessing Execution Feedback for Debugging Visual Programs](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2026 | arXiv | ★ IntentScore | [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) | — |
| 2025 | NeurIPS | ★ GUI-Reflection | [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://doi.org/10.52202/085713-3409) · [arXiv](https://arxiv.org/abs/2506.08012) | [Project](https://penghao-wu.github.io/GUI_Reflection/) · [Code](https://github.com/penghao-wu/GUI_Reflection) |
| 2026 | arXiv | — | [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | — |
| 2025 | arXiv | FailSafe | [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642) | [Project](https://jimntu.github.io/FailSafe) |
| 2026 | CVPR | FLARE | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | — |
| 2026 | arXiv | Intend, Reflect, Refine | [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913) | — |
| 2026 | CVPR | Progress-Think | [Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Progress-Think_Semantic_Progress_Reasoning_for_Vision-Language_Navigation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.17097) | — |
| 2026 | arXiv | Self-Correcting VLA | [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633) | [Code](https://github.com/Kisaragi0/SC-VLA) |
| 2026 | ICLR | — | [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | [Project](https://sites.google.com/utexas.edu/armor) |

<a id="topic-visual-evaluation-outcome"></a>

#### Visual Outcome Evaluation

19 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ LLaVA-Critic | [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://arxiv.org/abs/2410.02712) | [Project](https://llava-vl.github.io/blog/2024-10-03-llava-critic) · [Code](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2025 | arXiv | ★ EdiVal-Agent | [EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing](https://arxiv.org/abs/2509.13399) | [Code](https://github.com/TianyuCodings/EdiVal) |
| 2026 | ICLR | ★ ProRe | [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823) | [Code](https://github.com/V-Droid-Agent/ProRe) |
| 2026 | CVPR | ★ RetouchIQ | [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) | — |
| 2023 | ICCV | ★ TIFA | [TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering](https://arxiv.org/abs/2303.11897) | [Code](https://github.com/Yushi-Hu/tifa) |
| 2025 | CVPR | ★ SILMM | [SILMM: Self-Improving Large Multimodal Models for Compositional Text-to-Image Generation](https://arxiv.org/abs/2412.05818) | [Project](https://silmm.github.io/) · [Code](https://github.com/LgQu/SILMM) |
| 2025 | arXiv | ★ MARMOT | [Marmot: Object-Level Self-Correction via Multi-Agent Reasoning](https://arxiv.org/abs/2504.20054) | — |
| 2026 | CVPR | ★ VISTA | [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2510.15831) | — |
| 2026 | arXiv | ★ OS-Themis | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) | — |
| 2026 | arXiv | ★ IMAGAgent | [IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection](https://arxiv.org/abs/2603.29602) | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2026 | ICLR | ★ WebGen-Agent | [WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning](https://arxiv.org/abs/2509.22644) | [Code](https://github.com/mnluzimu/WebGen-Agent) |
| 2026 | arXiv | ★ RubSE | [Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation](https://arxiv.org/abs/2608.24138) | — |
| 2026 | arXiv | CoRe | [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](https://arxiv.org/abs/2607.01721) | — |
| 2026 | ICLR | PerfGuard | [PerfGuard: A Performance-Aware Agent for Visual Content Generation](https://arxiv.org/abs/2601.22571) | [Project](https://openreview.net/forum?id=tdN42GTv4S) · [Code](https://github.com/FelixChan9527/PerfGuard) |
| 2026 | arXiv | — | [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230) | — |
| 2026 | ACL | ReLook | [ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding](https://aclanthology.org/2026.acl-long.1167/) | — |
| 2025 | NeurIPS | SketchMind | [SketchMind: A Multi-Agent Cognitive Framework for Assessing Student-Drawn Scientific Sketches](https://doi.org/10.52202/085713-2774) · [arXiv](https://arxiv.org/abs/2507.22904) | — |
| 2023 | NeurIPS | T2i-compbench | [T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation](https://arxiv.org/abs/2307.06350v1) | [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| 2026 | ICML | UI2Code^N | [UI2Code^N: UI-to-Code Generation as Interactive Visual Optimization](https://proceedings.mlr.press/v306/yang26v.html) | — |

<a id="topic-visual-evaluation-self-correction"></a>

#### Visual-Based Self-Correction

38 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ LookBack | [VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning](https://arxiv.org/abs/2412.02172) | [Project](https://visco-benchmark.github.io/) · [Code](https://github.com/PlusLabNLP/VISCO) |
| 2026 | arXiv | ★ Kestrel | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2026 | ECCV | ★ Reflect-R1 | [Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | arXiv | ★ VRRL | [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490) | — |
| 2025 | NeurIPS | ★ GUI-Reflection | [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://doi.org/10.52202/085713-3409) · [arXiv](https://arxiv.org/abs/2506.08012) | [Project](https://penghao-wu.github.io/GUI_Reflection/) · [Code](https://github.com/penghao-wu/GUI_Reflection) |
| 2026 | ACL | ★ Don’t Act Blindly | [Don’t act blindly: Robust gui automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2024 | EMNLP Findings | ★ VDebugger | [VDebugger: Harnessing Execution Feedback for Debugging Visual Programs](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2026 | arXiv | ★ CycleVLA | [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295) | [Project](https://dannymcy.github.io/cyclevla/) · [Code](https://github.com/dannymcy/cyclevla_code) |
| 2025 | CVPR | ★ Phoenix | [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588) | [Code](https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework) |
| 2026 | CVPR | ★ ViFailback | [Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols](https://arxiv.org/abs/2512.02787) | — |
| 2025 | arXiv | ★ MARMOT | [Marmot: Object-Level Self-Correction via Multi-Agent Reasoning](https://arxiv.org/abs/2504.20054) | — |
| 2026 | arXiv | ★ IMAGAgent | [IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection](https://arxiv.org/abs/2603.29602) | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2025 | CASE | — | [A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees](https://arxiv.org/abs/2503.15202) | — |
| 2026 | arXiv | ActiveScope | [ActiveScope: Actively Seeking and Correcting Perception for MLLMs](https://arxiv.org/abs/2606.24292) | [Code](https://github.com/jasmine-ww/ActiveScope) |
| 2026 | arXiv | — | [Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046) | — |
| 2026 | arXiv | AgenticRL | [AgenticRL: Agentic Reinforcement Learning with Self-Refinement for Complex UAV Navigation](https://arxiv.org/abs/2606.03963) | — |
| 2024 | ICLR | CRITIC | [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) | — |
| 2025 | arXiv | FailSafe | [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642) | [Project](https://jimntu.github.io/FailSafe) |
| 2026 | CVPR | FLARE | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | — |
| 2026 | arXiv | Intend, Reflect, Refine | [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913) | — |
| 2025 | ICCV | — | [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342) | — |
| 2026 | arXiv | — | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | [Project](https://vlaworld.github.io) |
| 2025 | IROS | LERa | [LERa: Replanning with Visual Feedback in Instruction Following](https://arxiv.org/abs/2507.05135) | [Project](https://lera-robo.github.io) · [Code](https://github.com/AmpiroMax/LERa?tab=readme-ov-file#-custom-tasks) |
| 2026 | NeurIPS | MobileUse | [MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853) | [Code](https://github.com/MadeAgents/mobile-use) |
| 2026 | NeurIPS | — | [Mulberry: Empowering MLLM with o1-like Reasoning and Reflection via Collective Monte Carlo Tree Search](https://arxiv.org/abs/2412.18319) | [Code](https://github.com/HJYao00/Mulberry) |
| 2026 | arXiv | PrecisionCUA | [PrecisionCUA: Iterative Visual Refinement for Pixel-Precise Cursor Grounding in Code Editors](https://arxiv.org/abs/2604.13019) | [Code](https://github.com/microsoft/precision-cua-bench/tree/main) |
| 2026 | arXiv | — | [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230) | — |
| 2023 | arXiv | REFLECT | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |
| 2023 | NeurIPS | — | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | [Code](https://github.com/noahshinn/reflexion) |
| 2025 | NeurIPS | SceneWeaver | [SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent](https://doi.org/10.52202/085713-4689) · [arXiv](https://arxiv.org/abs/2509.20414) | [Project](https://scene-weaver.github.io/) · [Code](https://github.com/Scene-Weaver/SceneWeaver) |
| 2024 | CVPR | — | [Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090) | — |
| 2026 | arXiv | Self-Correcting VLA | [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633) | [Code](https://github.com/Kisaragi0/SC-VLA) |
| 2026 | ICLR | — | [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | [Project](https://sites.google.com/utexas.edu/armor) |
| 2026 | NeurIPS | — | [Sherlock: Self-Correcting Reasoning in Vision-Language Models](https://arxiv.org/abs/2505.22651) | — |
| 2026 | ICML | UI2Code^N | [UI2Code^N: UI-to-Code Generation as Interactive Visual Optimization](https://proceedings.mlr.press/v306/yang26v.html) | — |
| 2025 | CVPR | V-Stylist | [V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents](https://arxiv.org/abs/2503.12077) | — |
| 2025 | NAACL | — | [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2026 | NeurIPS | VL-Rethinker | [VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning](https://arxiv.org/abs/2504.08837) | — |

<a id="category-evolving"></a>

### Evolving Abilities

<a id="topic-evolving-diagnosis"></a>

#### Visual Capability Gap Diagnosis

17 works · 8 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | arXiv | ★ ViLoMem | [Agentic Learner with Grow-and-Refine Multimodal Semantic Memory](https://arxiv.org/abs/2511.21678) | [Project](https://weihao-bo.github.io/ViLoMeo-page) · [Code](https://github.com/weihao-bo/ViLoMem) |
| 2026 | arXiv | ★ RoboHarness (Li) | [RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060) | [Code](https://github.com/LZY-1021/RoboHarness) |
| 2026 | arXiv | ★ DataEvolver | [DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation](https://arxiv.org/abs/2606.31537) | — |
| 2026 | arXiv | ★ V-Gym | [V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution](https://arxiv.org/abs/2609.34682) | — |
| 2026 | arXiv | ★ SpatialEvo | [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144) | — |
| 2026 | arXiv | ★ EvoSkill-GUI | [Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents](https://arxiv.org/abs/2609.17653) | [Code](https://github.com/ZJU-REAL/EvoSkill-GUI) |
| 2026 | arXiv | ★ VideoResearcher | [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664) | — |
| 2026 | arXiv | ★ MetaVideoAgent | [MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding](https://arxiv.org/abs/2608.04587) | [Code](https://github.com/Alibaba-VELLDEPTH/MetaVideoAgent) |
| 2026 | CVPR | AwareVLN | [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://arxiv.org/abs/2605.22816) | [Project](https://gwxuan.github.io/AwareVLN/) · [Code](https://github.com/GWxuan/AwareVLN) |
| 2026 | arXiv | Beacon | [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595) | — |
| 2024 | arXiv | — | [Core Knowledge Deficits in Multi-Modal Language Models](https://arxiv.org/abs/2410.10855) | [Project](https://williamium3000.github.io/core-knowledge) · [Code](https://github.com/williamium3000/core-knowledge) |
| 2026 | arXiv | — | [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/abs/2606.02357) | — |
| 2026 | arXiv | — | [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718) | — |
| 2026 | arXiv | — | [Position: The Systemic Lack of Agency in Visual Reasoning](https://arxiv.org/abs/2606.14795) | [Project](https://haoychen.github.io/Implicit-Reasoning/) · [Code](https://github.com/HaoyChen/Implicit-Reasoning) |
| 2026 | arXiv | SEA-Eval | [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988) | — |
| 2026 | CVPR | — | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) | — |
| 2026 | arXiv | — | [What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery](https://arxiv.org/abs/2609.31760) | — |

<a id="topic-evolving-signals"></a>

#### Visual Improvement Signal Generation

48 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | arXiv | ★ Agent0-VL | [Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning](https://arxiv.org/abs/2511.19900) | [Code](https://github.com/aiming-lab/Agent0) |
| 2025 | CVPR | ★ RLAIF-V | [RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness](https://arxiv.org/abs/2405.17220) | [Code](https://github.com/RLHF-V/RLAIF-V) |
| 2025 | CVPR | ★ SILMM | [SILMM: Self-Improving Large Multimodal Models for Compositional Text-to-Image Generation](https://arxiv.org/abs/2412.05818) | [Project](https://silmm.github.io/) · [Code](https://github.com/LgQu/SILMM) |
| 2025 | NeurIPS | ★ UI-Genie | [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://doi.org/10.52202/085713-5028) · [arXiv](https://arxiv.org/abs/2505.21496) | [Code](https://github.com/Euphoria16/UI-Genie) |
| 2026 | arXiv | ★ GAIA | [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197) | [Code](https://github.com/SeerRay-Lab/GAIA) |
| 2026 | arXiv | ★ VLAW | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2026 | arXiv | ★ Seed2Scale | [Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation](https://arxiv.org/abs/2603.08260) | — |
| 2025 | arXiv | ★ Video2Policy | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | — |
| 2026 | arXiv | ★ RDA | [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) | — |
| 2026 | arXiv | ★ GenEvolve | [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605) | [Project](https://ephemeral182.github.io/GenEvolve/) · [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2026 | arXiv | ★ V-Gym | [V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution](https://arxiv.org/abs/2609.34682) | — |
| 2026 | arXiv | ★ SpatialEvo | [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144) | — |
| 2026 | arXiv | — | [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376) | [Code](https://github.com/mbzuai-oryx/Ask-Solve-Generate) |
| 2026 | arXiv | BaT | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) | — |
| 2026 | arXiv | BlueLM-GUI Technical Report | [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents](https://arxiv.org/abs/2609.12394) | — |
| 2023 | arXiv | BridgeData V2 | [BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952) | — |
| 2024 | NeurIPS | — | [Calibrated Self-Rewarding Vision Language Models](https://arxiv.org/abs/2405.14622) | [Code](https://github.com/YiyangZhou/CSR) |
| 2026 | arXiv | CoRe | [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](https://arxiv.org/abs/2607.01721) | — |
| 2009 | ICML | — | [Curriculum learning](https://icml.cc/2009/papers/119.pdf) | — |
| 2024 | arXiv | — | [Diving into Self-Evolving Training for Multimodal Reasoning](https://arxiv.org/abs/2412.17451) | [Project](https://mstar-lmm.github.io) · [Code](https://github.com/hkust-nlp/mstar) |
| 2026 | arXiv | Dream-RSI | [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) | [Project](https://github.com/zhengkid/Dream-RSI) |
| 2025 | arXiv | DreamGen | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](https://arxiv.org/abs/2505.12705) | — |
| 2026 | ICLR | DriveVLA-W0 | [DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796) | [Code](https://github.com/BraveGroup/DriveVLA-W0) |
| 2026 | arXiv | EdgeBench | [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155) | — |
| 2026 | arXiv | EE-MCP | [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/abs/2604.09815) | — |
| 2025 | arXiv | — | [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866) | — |
| 2025 | arXiv | EvoLMM | [EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards](https://arxiv.org/abs/2511.16672) | [Code](https://github.com/mbzuai-oryx/EvoLMM) |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2026 | ICLR | GUI-Shift | [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493) | — |
| 2025 | arXiv | Making VLMs More Robot-Friendly | [Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2023 | CoRL | MimicGen | [MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations](https://arxiv.org/abs/2310.17596) | [Project](https://mimicgen.github.io) · [Code](https://github.com/NVlabs/mimicgen) |
| 2026 | arXiv | OS-Themis | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) | — |
| 2025 | ICLR | PathGen-1.6M | [PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://arxiv.org/abs/2407.00203) | [Code](https://github.com/PathFoundation/PathGen-1.6M) |
| 2026 | EMNLP | — | [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388) | — |
| 2025 | arXiv | — | [Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning](https://arxiv.org/abs/2509.16136) | — |
| 2025 | arXiv | RFTF | [RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback](https://arxiv.org/abs/2505.19767) | — |
| 2026 | CVPR Workshops | — | [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | — |
| 2025 | CVPR | — | [Self-Evolving Visual Concept Library using Vision-Language Critics](https://arxiv.org/abs/2504.00185) | — |
| 2026 | arXiv | — | [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167) | — |
| 2026 | ICLR | SPIRAL | [SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2506.24119) | [Code](https://github.com/spiral-rl/spiral) |
| 2026 | arXiv | — | [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | — |
| 2026 | arXiv | UI-Oceanus | [UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics](https://arxiv.org/abs/2604.02345) | — |
| 2025 | ICLR | Video-STaR | [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://arxiv.org/abs/2407.06189) | [Project](https://orrzohar.github.io/projects/video-star/) |
| 2026 | arXiv | VISA | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013) | — |
| 2026 | CVPR | Vision-R1 | [Vision-R1: Evolving Human-Free Alignment in Large Vision-Language Models via Vision-Guided Reinforcement Learning](https://arxiv.org/abs/2503.18013) | — |
| 2026 | ICLR | Vision-sr1 | [Vision-sr1: Self-rewarding vision-language model via reasoning decomposition and multi-reward policy optimization](https://arxiv.org/abs/2508.19652) | [Code](https://github.com/zli12321/Vision-SR1) |
| 2026 | arXiv | — | [When Models Judge Themselves: Unsupervised Self-Evolution for Multimodal Reasoning](https://arxiv.org/abs/2603.21289) | [Code](https://github.com/OPPO-Mente-Lab/LLM-Self-Judge) |
| 2025 | arXiv | World-Env | [World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training](https://arxiv.org/abs/2509.24948) | [Code](https://github.com/amap-cvlab/world-env) |

<a id="topic-evolving-optimization"></a>

#### Vision-Guided Optimization Adaptation

104 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | ECCV | ★ EvoVLA | [EvoVLA: Self-Evolving Vision-Language-Action Model](https://arxiv.org/abs/2511.16166) | [Project](https://aigeeksgroup.github.io/EvoVLA) · [Code](https://github.com/AIGeeksGroup/EvoVLA) |
| 2026 | arXiv | ★ UI-Mem | [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) | [Project](https://ui-mem.github.io) |
| 2025 | arXiv | ★ SEAgent | [SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |
| 2025 | arXiv | ★ Mobile-Agent-E | [Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](https://arxiv.org/abs/2501.11733) | [Project](https://x-plug.github.io/MobileAgent) · [Code](https://github.com/X-PLUG/MobileAgent) |
| 2025 | arXiv | ★ WebCoach | [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997) | — |
| 2026 | arXiv | ★ EvolveNav | [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | — |
| 2026 | arXiv | ★ V-Gym | [V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution](https://arxiv.org/abs/2609.34682) | — |
| 2026 | arXiv | ★ SpatialEvo | [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144) | — |
| 2026 | arXiv | ★ VLAW | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2026 | arXiv | ★ RISE | [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075) | [Project](https://opendrivelab.com/RISE/) · [Code](https://github.com/OpenDriveLab/RISE) |
| 2026 | ICLR | ★ PLD | [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091) | — |
| 2026 | arXiv | ★ GenEvolve | [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605) | [Project](https://ephemeral182.github.io/GenEvolve/) · [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2011 | AISTATS | — | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://proceedings.mlr.press/v15/ross11a.html) · [arXiv](https://arxiv.org/abs/1011.0686) | [Project](https://proceedings.mlr.press/v15/ross11a.html) |
| 2025 | arXiv | — | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | [Project](https://github.com/CharlesQ9/Self-Evolving-Agents) |
| 2025 | EMNLP Demos | AgentCPM-GUI | [AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.01391) | [Code](https://github.com/OpenBMB/AgentCPM-GUI) |
| 2026 | arXiv | AgenticRL | [AgenticRL: Agentic Reinforcement Learning with Self-Refinement for Complex UAV Navigation](https://arxiv.org/abs/2606.03963) | — |
| 2026 | arXiv | — | [Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards](https://arxiv.org/abs/2606.27376) | [Code](https://github.com/mbzuai-oryx/Ask-Solve-Generate) |
| 2025 | NeurIPS | AutoVLA | [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | [Project](https://autovla.github.io/) · [Code](https://github.com/ucla-mobility/AutoVLA) |
| 2026 | arXiv | BaT | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) | — |
| 2026 | arXiv | — | [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](https://arxiv.org/abs/2608.21204) | — |
| 2026 | arXiv | BlueLM-GUI Technical Report | [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents](https://arxiv.org/abs/2609.12394) | — |
| 2025 | NeurIPS | C-NAV | [C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](https://doi.org/10.52202/085713-4206) · [arXiv](https://arxiv.org/abs/2510.20685) | [Project](https://bigtree765.github.io/C-Nav-project) · [Code](https://github.com/BigTree765/C-Nav) |
| 2024 | NeurIPS | — | [Calibrated Self-Rewarding Vision Language Models](https://arxiv.org/abs/2405.14622) | [Code](https://github.com/YiyangZhou/CSR) |
| 2019 | Neural Networks | — | [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) | — |
| 2024 | arXiv | — | [Diving into Self-Evolving Training for Multimodal Reasoning](https://arxiv.org/abs/2412.17451) | [Project](https://mstar-lmm.github.io) · [Code](https://github.com/hkust-nlp/mstar) |
| 2026 | arXiv | Dream-RSI | [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) | [Project](https://github.com/zhengkid/Dream-RSI) |
| 2026 | arXiv | EE-MCP | [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/abs/2604.09815) | — |
| 2025 | arXiv | — | [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866) | — |
| 2024 | arXiv | — | [Efficient Self-Improvement in Multimodal Large Language Models: A Model-Level Judge-Free Approach](https://arxiv.org/abs/2411.17760) | — |
| 2026 | arXiv | ELITE | [ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents](https://arxiv.org/abs/2603.24018) | — |
| 2025 | arXiv | — | [Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370) | [Code](https://github.com/YXB-NKU/SE-GUI) |
| 2025 | NAACL Findings | — | [Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement](https://arxiv.org/abs/2405.15973) | — |
| 2026 | arXiv | EVA | [EVA: Efficient Reinforcement Learning for End-to-End Video Agent](https://arxiv.org/abs/2603.22918) | — |
| 2025 | arXiv | EvoLMM | [EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards](https://arxiv.org/abs/2511.16672) | [Code](https://github.com/mbzuai-oryx/EvoLMM) |
| 2026 | arXiv | EvoMemNav | [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509) | — |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | arXiv | — | [Experience Transfer for Multimodal LLM Agents in Minecraft Game](https://arxiv.org/abs/2604.05533) | — |
| 2025 | arXiv | — | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) | — |
| 2026 | arXiv | — | [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406) | — |
| 2026 | ICLR | GEPA | [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) | [Code](https://github.com/gepa-ai/gepa) |
| 2025 | arXiv | GUI-R1 | [GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458) | — |
| 2026 | ICLR | GUI-Shift | [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493) | — |
| 2026 | arXiv | HarnessForge | [HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems](https://arxiv.org/abs/2606.01779) | [Code](https://github.com/mingju-c/HarnessForge) |
| 2026 | arXiv | ImageEdit-R1 | [ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning](https://arxiv.org/abs/2603.08059) | [Project](https://github.com/zhaoyiran924/ImageEdit-R1) |
| 2026 | ICLR | — | [K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676) | — |
| 2026 | CVPR | LEAD | [LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_LEAD_Minimizing_Learner-Expert_Asymmetry_in_End-to-End_Driving_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2512.20563) | [Code](https://github.com/autonomousvision/lead) |
| 2026 | CVPR | LIBERO-Plus | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf) · [arXiv](https://arxiv.org/abs/2510.13626) | [Code](https://github.com/sylvestf/LIBERO-plus) |
| 2023 | NeurIPS | LIBERO | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | [Project](https://libero-project.github.io) |
| 2025 | arXiv | Making VLMs More Robot-Friendly | [Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2026 | ICLR | MedVR | [MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2604.08203) | [Code](https://github.com/alibaba-damo-academy/MedVR) |
| 2026 | arXiv | MemRL | [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192) | — |
| 2026 | arXiv | MMDynOpt-Agent | [MMDynOpt-Agent: Dynamic Optimization for Multimodal Large Language Model Reasoning via Reinforcement Learning](https://arxiv.org/abs/2608.14026) | [Code](https://github.com/QwenQKing/MMDynOpt-Agent) |
| 2026 | ICLR | MobileRL | [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://doi.org/10.48550/arxiv.2509.18119) · [arXiv](https://arxiv.org/abs/2509.18119) | [Code](https://github.com/THUDM/MobileRL) |
| 2026 | CVPR | OctoT2I | [OctoT2I: A Self-Evolving Agentic Text-to-Image Router](https://arxiv.org/abs/2606.01803) | [Code](https://github.com/JaxJiang2642081986/OctoT2I) |
| 2026 | CVPR | OVOD-Agent | [OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection](https://arxiv.org/abs/2511.21064) | — |
| 2026 | ECCV | — | [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373) | — |
| 2026 | arXiv | — | [Planning with the Views](https://arxiv.org/abs/2605.29563) | [Project](https://viewsuite.github.io) · [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2016 | ICLR | — | [Policy Distillation](https://arxiv.org/abs/1511.06295) | — |
| 2025 | ICCV | R1-VL | [R1-VL: Learning to Reason with Multimodal Large Language Models via Step-wise Group Relative Policy Optimization](https://arxiv.org/abs/2503.12937) | — |
| 2026 | arXiv | Recursive Self-Improvement in AI | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | [Project](https://github.com/deepgrounding/recursive-self-improvement) |
| 2023 | NeurIPS | — | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | [Code](https://github.com/noahshinn/reflexion) |
| 2026 | ACL | ReLook | [ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding](https://aclanthology.org/2026.acl-long.1167/) | — |
| 2026 | CVPR | ReSAM | [ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images](https://arxiv.org/abs/2511.21606) | — |
| 2026 | ICLR | ReTool | [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) | — |
| 2025 | arXiv | RFTF | [RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback](https://arxiv.org/abs/2505.19767) | — |
| 2024 | arXiv | RLDG | [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](https://arxiv.org/abs/2412.09858) | [Project](https://generalist-distillation.github.io) |
| 2026 | arXiv | RLHarness | [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326) | — |
| 2023 | arXiv | RoboCat | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | — |
| 2026 | arXiv | RSIAgent | [RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://arxiv.org/abs/2609.15364) | — |
| 2026 | ICLR | ScaleCUA | [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://doi.org/10.48550/arxiv.2509.15221) · [arXiv](https://arxiv.org/abs/2509.15221) | [Code](https://github.com/OpenGVLab/ScaleCUA) |
| 2026 | CVPR | — | [Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs](https://arxiv.org/abs/2511.19773) | — |
| 2026 | arXiv | SE-GA | [SE-GA: Memory-Augmented Self-Evolution for GUI Agents](https://arxiv.org/abs/2605.16883) | [Code](https://github.com/jinshilong-dev/SE-GA) |
| 2025 | arXiv | SE-VLN | [SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models](https://arxiv.org/abs/2507.13152) | — |
| 2026 | arXiv | SEA-Eval | [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988) | — |
| 2026 | arXiv | — | [Self-Adaptive VLA for Robust Robot Deployment](https://arxiv.org/abs/2609.30092) | — |
| 2026 | ECCV | — | [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](https://arxiv.org/abs/2606.28971) | — |
| 2026 | arXiv | — | [Self-Evolving Visual Questioner](https://arxiv.org/abs/2606.13929) | — |
| 2025 | EMNLP Findings | — | [Self-Improvement in Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2510.02665) | — |
| 2026 | arXiv | — | [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) | [Project](https://selfimproving-agent.github.io/) · [Code](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) |
| 2026 | ICLR | — | [Self-Improving Loops for Visual Robotic Planning](https://arxiv.org/abs/2506.06658) | [Project](https://diffusion-supervision.github.io/silvr/) · [Code](https://github.com/brown-palm/silvr) |
| 2026 | arXiv | SIA | [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | — |
| 2026 | CVPR | — | [Simple Agents Outperform Experts in Biomedical Imaging Workflow Optimization](https://arxiv.org/abs/2512.06006) | [Code](https://github.com/xuefei-wang/simple-agent-opt) |
| 2026 | arXiv | — | [Skill-Guided Continuation Distillation for GUI Agents](https://arxiv.org/abs/2606.18890) | — |
| 2026 | arXiv | SpaceMind | [SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing](https://arxiv.org/abs/2604.14399) | [Code](https://github.com/wuaodi/SpaceMind) |
| 2024 | arXiv | SPIRE | [SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation](https://arxiv.org/abs/2410.18065) | — |
| 2024 | arXiv | THE COLOSSEUM | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191) | — |
| 2026 | arXiv | — | [The Essence of Balance for Self-Improving Agents in Vision-and-Language Navigation](https://arxiv.org/abs/2604.19064) | — |
| 2025 | arXiv | — | [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) | — |
| 2026 | CVPR | — | [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235) | [Code](https://github.com/hehehahi4/CES) |
| 2026 | CVPR | — | [Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning](https://arxiv.org/abs/2512.09706) | [Code](https://github.com/CraftJarvis/OpenHA) |
| 2025 | arXiv | UI-TARS-2 Technical Report | [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) | — |
| 2026 | CVPR | — | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) | — |
| 2025 | ICLR | Video-STaR | [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://arxiv.org/abs/2407.06189) | [Project](https://orrzohar.github.io/projects/video-star/) |
| 2025 | NAACL | — | [Vision-Language Models Can Self-Improve Reasoning via Reflection](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2026 | CVPR | Vision-R1 | [Vision-R1: Evolving Human-Free Alignment in Large Vision-Language Models via Vision-Guided Reinforcement Learning](https://arxiv.org/abs/2503.18013) | — |
| 2026 | ICLR | Vision-sr1 | [Vision-sr1: Self-rewarding vision-language model via reasoning decomposition and multi-reward policy optimization](https://arxiv.org/abs/2508.19652) | [Code](https://github.com/zli12321/Vision-SR1) |
| 2025 | arXiv | VisPlay | [VisPlay: Self-Evolving Vision-Language Models from Images](https://arxiv.org/abs/2511.15661) | [Project](https://bruno686.github.io/VisPlay/) · [Code](https://github.com/bruno686/VisPlay) |
| 2025 | ICCV | Visual-RFT | [Visual-RFT: Visual Reinforcement Fine-Tuning](https://arxiv.org/abs/2503.01785) | [Code](https://github.com/Liuziyu77/Visual-RFT) |
| 2026 | NeurIPS | VL-Rethinker | [VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning](https://arxiv.org/abs/2504.08837) | — |
| 2025 | arXiv | VLN-R1 | [VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.17221) | — |
| 2026 | arXiv | — | [When Models Judge Themselves: Unsupervised Self-Evolution for Multimodal Reasoning](https://arxiv.org/abs/2603.21289) | [Code](https://github.com/OPPO-Mente-Lab/LLM-Self-Judge) |
| 2026 | ICLR | WMPO | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2511.09515) | [Project](https://wm-po.github.io) · [Code](https://github.com/WM-PO/WMPO) |
| 2025 | arXiv | — | [World Model Implanting for Test-time Adaptation of Embodied Agents](https://arxiv.org/abs/2509.03956) | — |
| 2025 | arXiv | π^*_0.6 | [π^*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) | — |

<a id="topic-evolving-infrastructure"></a>

#### Self-Modification of Visual Interaction Infrastructure

48 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | arXiv | ★ VideoResearcher | [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664) | — |
| 2026 | CVPR | ★ META | [META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) | — |
| 2026 | arXiv | ★ EvoSkill-GUI | [Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents](https://arxiv.org/abs/2609.17653) | [Code](https://github.com/ZJU-REAL/EvoSkill-GUI) |
| 2026 | arXiv | ★ VideoHarness-RSI | [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](https://arxiv.org/abs/2608.24302) | [Code](https://github.com/Tencent/VideoHarness-RSI) |
| 2026 | arXiv | ★ MetaVideoAgent | [MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding](https://arxiv.org/abs/2608.04587) | [Code](https://github.com/Alibaba-VELLDEPTH/MetaVideoAgent) |
| 2026 | arXiv | ★ OmniHarness | [OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning](https://arxiv.org/abs/2609.16057) | — |
| 2026 | arXiv | ★ COMFYCLAW | [COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows](https://arxiv.org/abs/2607.01709) | [Code](https://github.com/Moms-Organic-Agent-Lab/comfyclaw) |
| 2026 | arXiv | ★ AutoRef | [AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation](https://arxiv.org/abs/2609.35530) | — |
| 2026 | arXiv | ★ RegenHarness | [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | — |
| 2026 | arXiv | ★ Harness Distillation | [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378) | — |
| 2026 | ICLR | ★ TVP | [Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning](https://arxiv.org/abs/2512.20934) | [Project](https://transductive-visualprogram.github.io/) · [Code](https://github.com/transductive-visualprogram/tvp) |
| 2026 | arXiv | ★ RLHarness | [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326) | — |
| 2025 | arXiv | — | [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | — |
| 2025 | arXiv | — | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | [Project](https://github.com/CharlesQ9/Self-Evolving-Agents) |
| 2025 | ICLR | AFlow | [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | [Code](https://github.com/FoundationAgents/AFlow) |
| 2026 | OpenReview Preprint | — | [Agent harness engineering: A survey](https://openreview.net/forum?id=eONq7FdiHa) | [Project](https://github.com/Picrew/awesome-agent-harness) |
| 2025 | ICLR | — | [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435) | [Project](https://shengranhu.com/ADAS) · [Code](https://github.com/ShengranHu/ADAS) |
| 2026 | ICLR | — | [Darwin Gödel machine: open-ended evolution of self-improving agents](https://arxiv.org/abs/2505.22954) | [Code](https://github.com/jennyzzt/dgm) |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | arXiv | EvoX | [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413) | — |
| 2026 | ICLR | GEPA | [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) | [Code](https://github.com/gepa-ai/gepa) |
| 2025 | ACL | — | [Gödel agent: A self-referential agent framework for recursively self-improvement](https://arxiv.org/abs/2410.04444) | [Code](https://github.com/Arvid-pku/Godel_Agent) |
| 2026 | Blog | — | Harness Engineering for Self-Improvement | — |
| 2026 | arXiv | HarnessForge | [HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems](https://arxiv.org/abs/2606.01779) | [Code](https://github.com/mingju-c/HarnessForge) |
| 2026 | arXiv | — | [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821) | — |
| 2026 | arXiv | HarnessPAI | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | — |
| 2026 | arXiv | HarnessX | [HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249) | [Project](https://darwin-agent.github.io/HarnessX/) · [Code](https://github.com/Darwin-Agent/HarnessX) |
| 2026 | arXiv | — | [Hyperagents](https://arxiv.org/abs/2603.19461) | — |
| 2026 | arXiv | MetaForge | [MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand](https://arxiv.org/abs/2606.01801) | — |
| 2026 | arXiv | MetaRSI / RSI2 | [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396) | — |
| 2026 | arXiv | MetaSkill-Evolve | [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) | — |
| 2026 | arXiv | Omni-SimpleMem | [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.01007) | [Code](https://github.com/aiming-lab/SimpleMem) |
| 2026 | arXiv | Recursive Self-Improvement in AI | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | [Project](https://github.com/deepgrounding/recursive-self-improvement) |
| 2026 | arXiv | — | [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457) | — |
| 2026 | arXiv | Robo-Cortex | [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729) | — |
| 2026 | arXiv | RRSI | [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972) | [Code](https://github.com/google-research/rrsi) |
| 2026 | arXiv | RSIAgent | [RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://arxiv.org/abs/2609.15364) | — |
| 2026 | arXiv | RSIGame | [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045) | — |
| 2026 | arXiv | SCAFFOLD | [SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction](https://arxiv.org/abs/2609.05511) | [Code](https://github.com/BokwaiHo/SCAFFOLD) |
| 2026 | arXiv | Self-Harness | [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498) | [Code](https://github.com/qzzqzzb/Self-Harness) |
| 2025 | EMNLP Findings | — | [Self-Improvement in Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2510.02665) | — |
| 2026 | arXiv | — | [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) | [Project](https://selfimproving-agent.github.io/) · [Code](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) |
| 2026 | arXiv | SIA | [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | — |
| 2026 | arXiv | SoL-Pi | [SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness](https://arxiv.org/abs/2609.20519) | [Project](https://nvlabs.github.io/SoL-Pi/) · [Code](https://github.com/NVlabs/SoL-Pi) |
| 2026 | arXiv | SpaceMind | [SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing](https://arxiv.org/abs/2604.14399) | [Code](https://github.com/wuaodi/SpaceMind) |
| 2026 | arXiv | — | [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873) | [Project](https://github.com/theseus-labs-rsi/awesome-rsi) |
| 2026 | arXiv | — | [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | — |
| 2026 | arXiv | — | [What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery](https://arxiv.org/abs/2609.31760) | — |

<a id="branch-external"></a>

## Harness Infrastructure for Vision-Centric Agents

<a id="category-planning"></a>

### Vision Planning and Orchestration Infrastructure

<a id="topic-planning-task-workflow"></a>

#### Task and Workflow Planning

86 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | ICLR | ★ Agent S | [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://arxiv.org/abs/2410.08164) | [Code](https://github.com/simular-ai/Agent-S) |
| 2025 | arXiv | ★ Agent S2 | [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://arxiv.org/abs/2504.00906) | [Code](https://github.com/simular-ai/Agent-S) |
| 2025 | arXiv | ★ OctoTools | [OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning](https://arxiv.org/abs/2502.11271) | [Project](https://octotools.github.io/) · [Code](https://github.com/octotools/octotools) |
| 2024 | arXiv | ★ Cradle | [Cradle: Empowering Foundation Agents Towards General Computer Control](https://arxiv.org/abs/2403.03186) | [Code](https://github.com/BAAI-Agents/Cradle) |
| 2025 | ICRA | ★ BUMBLE | [BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation](https://arxiv.org/abs/2410.06237) | [Project](https://robin-lab.cs.utexas.edu/BUMBLE/) · [Code](https://github.com/UT-Austin-RobIn/BUMBLE) |
| 2025 | arXiv | ★ RoboChemist | [RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation](https://arxiv.org/abs/2509.08820) | [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) |
| 2026 | arXiv | ★ SCOPE | [SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation](https://arxiv.org/abs/2605.08043) | — |
| 2026 | arXiv | ★ AgentChord | [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/abs/2605.11951) | [Project](https://shengxu.net/AgentChord/) · [Code](https://github.com/EDEM-AI/AgentChord) |
| 2025 | arXiv | ★ ViReSkill | [ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning](https://arxiv.org/abs/2509.24219) | — |
| 2026 | arXiv | ★ RoboHarness (Huang) | [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | — |
| 2026 | arXiv | ★ HarnessWAM | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | — |
| 2026 | arXiv | ★ HarnessPAI | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | — |
| 2025 | CASE | — | [A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees](https://arxiv.org/abs/2503.15202) | — |
| 2025 | ICLR | AFlow | [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | [Code](https://github.com/FoundationAgents/AFlow) |
| 2026 | OpenReview Preprint | — | [Agent harness engineering: A survey](https://openreview.net/forum?id=eONq7FdiHa) | [Project](https://github.com/Picrew/awesome-agent-harness) |
| 2026 | arXiv | — | [Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758) | [Code](https://github.com/YinmingHuang/Awesome-agentic-visual-generation-model) |
| 2026 | ECCV | AgentVLN | [AgentVLN: Towards Agentic Vision-and-Language Navigation](https://arxiv.org/abs/2603.17670) | [Code](https://github.com/Allenxinn/AgentVLN) |
| 2023 | EMNLP | — | [Analyzing Modular Approaches for Visual Question Decomposition](https://doi.org/10.18653/v1/2023.emnlp-main.157) · [arXiv](https://arxiv.org/abs/2311.06411) | [Code](https://github.com/brown-palm/visual-question-decomposition) |
| 2024 | arXiv | AndroidLab | [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://arxiv.org/abs/2410.24024) | — |
| 2025 | CHI | AppAgent | [AppAgent: Multimodal Agents as Smartphone Users](https://arxiv.org/abs/2312.13771) | [Project](https://appagent-official.github.io/) · [Code](https://github.com/TencentQQGYLab/AppAgent) |
| 1999 | Artificial Intelligence | Between MDPs and semi-MDPs | [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | — |
| 2026 | CVPR | CapNav | [CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation](https://arxiv.org/abs/2602.18424) | [Code](https://github.com/makeabilitylab/CapNav) |
| 2026 | CVPR Findings | CarePilot | [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) | — |
| 2026 | arXiv | — | [Clarify Before Executing: A Self-Evolving Agent for Resolving Intent Asymmetry in 3D Tool Orchestration](https://arxiv.org/abs/2607.16352) | [Code](https://github.com/xyzhu1225/CLARE) |
| 2023 | ICRA | — | [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | [Project](https://code-as-policies.github.io) · [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| 2025 | CVPR | ComfyBench | [ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems](https://arxiv.org/abs/2409.01392) | [Code](https://github.com/xxyQwQ/ComfyBench) |
| 2025 | ACL Demos | ComfyUI-Copilot | [ComfyUI-Copilot: An Intelligent Assistant for Automated Workflow Development](https://arxiv.org/abs/2506.05010) | [Code](https://github.com/ATH-MaaS/ComfyUI-Copilot) |
| 2026 | arXiv | — | [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | — |
| 2024 | ICLR | DiLu | [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://arxiv.org/abs/2309.16292) | [Project](https://pjlab-adg.github.io/DiLu/) · [Code](https://github.com/PJLab-ADG/DiLu) |
| 2025 | ICCV | DWIM | [DWIM: Towards Tool-aware Visual Reasoning via Discrepancy-aware Workflow Generation & Instruct-Masking Tuning](https://arxiv.org/abs/2503.19263) | — |
| 2025 | ICLR | EMOS | [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | — |
| 2024 | TPAMI | ETPNav | [ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments](https://arxiv.org/abs/2304.03047) | [Code](https://github.com/MarSaKi/ETPNav) |
| 2026 | ICLR | FaSTA^* | [FaSTA^*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2025 | ICCV | GUIOdyssey | [GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451) | [Code](https://github.com/OpenGVLab/GUI-Odyssey) |
| 2025 | ICLR | HAMSTER | [HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation](https://arxiv.org/abs/2502.05485) | [Project](https://hamster-robot.github.io/) · [Code](https://github.com/liyi14/HAMSTER_beta) |
| 2025 | arXiv | — | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | [Project](https://www.pi.website/research/hirobot) |
| 2026 | ICML | — | [Hierarchical Procedural Meta-Reasoning for Generalizable Multimodal Agents](https://openreview.net/forum?id=v2H2vzRqcr) | — |
| 2023 | NeurIPS | HuggingGPT | [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) | [Code](https://github.com/microsoft/JARVIS) |
| 2026 | ICLR | — | [K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676) | — |
| 2025 | arXiv | — | [Learning Semantic Atomic Skills for Multi-Task Robotic Manipulation](https://arxiv.org/abs/2512.18368) | [Project](https://atom-skill.github.io) |
| 2025 | IROS | LERa | [LERa: Replanning with Visual Feedback in Instruction Following](https://arxiv.org/abs/2507.05135) | [Project](https://lera-robo.github.io) · [Code](https://github.com/AmpiroMax/LERa?tab=readme-ov-file#-custom-tasks) |
| 2024 | CVPR | LMDrive | [LMDrive: Closed-Loop End-to-End Driving with Large Language Models](https://arxiv.org/abs/2312.07488) | [Project](https://hao-shao.com/projects/lmdrive.html) · [Code](https://github.com/opendilab/LMDrive) |
| 2026 | ICLR | LongHorizonUI | [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE) | — |
| 2025 | arXiv | MAI-UI Technical Report | [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047) | — |
| 2024 | ICML | Mastering Text-to-Image Diffusion | [Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs](https://arxiv.org/abs/2401.11708) | [Code](https://github.com/YangLing0818/RPG-DiffusionMaster) |
| 2026 | ICLR | MedAgent-Pro | [MedAgent-Pro: Towards Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow](https://arxiv.org/abs/2503.18968) | [Code](https://github.com/jinlab-imvr/MedAgent-Pro) |
| 2023 | arXiv | Mind2Web | [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) | — |
| 2026 | NeurIPS | MobileUse | [MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation](https://arxiv.org/abs/2507.16853) | [Code](https://github.com/MadeAgents/mobile-use) |
| 2026 | ECCV | MolmoWeb | [MolmoWeb: Open Visual Web Agent and Open Data for the Open Web](https://arxiv.org/abs/2604.08516) | [Project](https://allenai.org/blog/molmoweb) · [Code](https://github.com/allenai/molmoweb) |
| 2024 | arXiv | NaVid | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852) | — |
| 2026 | arXiv | NEWTON | [NEWTON: Agentic Planning for Physically Grounded Video Generation](https://arxiv.org/abs/2605.18396) | [Project](https://Newton026.github.io/newton) · [Code](https://github.com/CUTEPKQ/NEWTON) |
| 2025 | arXiv | NOVA | [NOVA: An Agentic Framework for Automated Histopathology Analysis and Discovery](https://arxiv.org/abs/2511.11324) | [Code](https://github.com/microsoft/nova-agent) |
| 2025 | arXiv | Octopus | [Octopus: Agentic Multimodal Reasoning with Six-Capability Orchestration](https://arxiv.org/abs/2511.15351) | — |
| 2024 | ECCV | OmniACT | [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553) | — |
| 2026 | ICLR | OmniActor | [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322) | — |
| 2025 | ACL Findings | OS-Kairos | [OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents](https://arxiv.org/abs/2503.16465) | [Code](https://github.com/Wuzheng02/OS-Kairos) |
| 2026 | ACL | OS-Symphony | [OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agents](https://arxiv.org/abs/2601.07779) | [Code](https://github.com/OS-Copilot/OS-Symphony) |
| 2026 | ICLR | OSWorld-MCP | [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563) | [Project](https://osworld-mcp.github.io) · [Code](https://github.com/X-PLUG/OSWorld-MCP) |
| 2026 | ICLR | — | [Planning with an Embodied Learnable Memory](https://openreview.net/forum?id=79BOATBal9) | — |
| 2023 | CVPR | — | [Planning-oriented Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2212.10156) | — |
| 2025 | ACL Findings | — | [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) | [Project](https://invinciblewyq.github.io/ponder-press-page/) |
| 2026 | arXiv | Qwen-RobotNav Technical Report | [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) | — |
| 2026 | arXiv | Qwen-UI-Agent Technical Report | [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227) | — |
| 2023 | ICLR | ReAct | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | [Project](https://react-lm.github.io) · [Code](https://github.com/ysymyth/ReAct) |
| 2026 | NeurIPS | — | [Real-Time Execution of Action Chunking Flow Policies](https://arxiv.org/abs/2506.07339) | [Project](https://pi.website/research/real_time_chunking) · [Code](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) |
| 2026 | ICLR | — | [Real-Time Robot Execution with Masked Action Chunking](https://arxiv.org/abs/2601.20130) | [Project](https://remac-async.github.io/) · [Code](https://github.com/hatchetProject/REMAC) |
| 2026 | ECCV | ReDesign | [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](https://arxiv.org/abs/2607.25565) | — |
| 2018 | arXiv | — | [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802) | — |
| 2026 | arXiv | — | [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227) | — |
| 2019 | arXiv | RLBench | [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271) | — |
| 2026 | ECCV | RoboClaw | [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) | [Code](https://github.com/RoboClaw-Robotics/RoboClaw) |
| 2024 | arXiv | RT-H | [RT-H: Action Hierarchies Using Language](https://arxiv.org/abs/2403.01823) | — |
| 2026 | ICLR | ScienceBoard | [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897) | [Project](https://qiushisun.github.io/ScienceBoard-Home/) · [Code](https://github.com/OS-Copilot/ScienceBoard) |
| 2026 | ECCV | — | [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](https://arxiv.org/abs/2606.28971) | — |
| 2026 | ICLR | — | [Self-Improving Loops for Visual Robotic Planning](https://arxiv.org/abs/2506.06658) | [Project](https://diffusion-supervision.github.io/silvr/) · [Code](https://github.com/brown-palm/silvr) |
| 2026 | arXiv | Show-Harness | [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | [Project](https://showlab.github.io/Show-Harness) · [Code](https://github.com/showlab/Show-Harness) |
| 2026 | CVPR | — | [Simple Agents Outperform Experts in Biomedical Imaging Workflow Optimization](https://arxiv.org/abs/2512.06006) | [Code](https://github.com/xuefei-wang/simple-agent-opt) |
| 2024 | CVPR | SkillDiffuser | [SkillDiffuser: Interpretable Hierarchical Planning via Skill Abstractions in Diffusion-Based Task Execution](https://arxiv.org/abs/2312.11598) | — |
| 2024 | NeurIPS | — | [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://doi.org/10.52202/079017-3421) · [arXiv](https://arxiv.org/abs/2407.10956) | [Project](https://spider2-v.github.io) · [Code](https://github.com/xlang-ai/Spider2-V) |
| 2024 | arXiv | SPIRE | [SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation](https://arxiv.org/abs/2410.18065) | — |
| 2026 | ICLR | — | [Towards Multimodal Data-Driven Scientific Discovery Powered by LLM Agents](https://openreview.net/forum?id=kZHSvETWdi) | [Code](https://github.com/usail-hkust/MoSciBench) |
| 2026 | CVPR | — | [Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation](https://arxiv.org/abs/2511.22235) | [Code](https://github.com/hehehahi4/CES) |
| 2024 | ACL | VisualWebArena | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | — |
| 2022 | arXiv | WebShop | [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) | — |
| 2024 | ACL | WebVoyager | [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) | — |
| 2017 | ICML | World of Bits | [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) | — |

<a id="topic-planning-trajectory-search"></a>

#### Trajectory Search and Deliberation

23 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ NWM | [Navigation World Models](https://arxiv.org/abs/2412.03572) | [Project](https://www.amirbar.net/nwm/) · [Code](https://github.com/facebookresearch/nwm/) |
| 2025 | ICML | ★ WebDreamer | [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559) | — |
| 2025 | arXiv | ★ STORM | [STORM: Search-Guided Generative World Models for Robotic Manipulation](https://arxiv.org/abs/2512.18477) | — |
| 2025 | arXiv | ★ VLWM | [Planning with Reasoning using Vision Language World Model](https://arxiv.org/abs/2509.02722) | — |
| 2026 | ICLR | ★ R-WoM | [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://doi.org/10.48550/arxiv.2510.11892) · [arXiv](https://arxiv.org/abs/2510.11892) | — |
| 2026 | arXiv | ★ Agent Alpha | [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995) | — |
| 2025 | arXiv | ★ Scaling Agents | [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250) | — |
| 2026 | ICLR | ★ GTA1 | [GTA1: GUI Test-time Scaling Agent](https://arxiv.org/abs/2507.05791) | [Code](https://github.com/Yan98/GTA1) |
| 2025 | arXiv | ★ RoboMonkey | [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://arxiv.org/abs/2506.17811) | — |
| 2024 | ICML | ★ PIVOT | [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://arxiv.org/abs/2402.07872) | [Project 1](http://pivot-prompt.github.io) · [Project 2](https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo) |
| 2024 | arXiv | ★ ReKep | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |
| 2026 | arXiv | ★ HarnessWAM | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | — |
| 2026 | ICML | — | [Agentic Model Predictive Questioning Control in Visual Design](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | arXiv | — | [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](https://arxiv.org/abs/2608.21204) | — |
| 2026 | ICLR | — | [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | — |
| 2026 | arXiv | — | [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070) | — |
| 2024 | TPAMI | ETPNav | [ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments](https://arxiv.org/abs/2304.03047) | [Code](https://github.com/MarSaKi/ETPNav) |
| 2026 | NeurIPS | — | [Mulberry: Empowering MLLM with o1-like Reasoning and Reflection via Collective Monte Carlo Tree Search](https://arxiv.org/abs/2412.18319) | [Code](https://github.com/HJYao00/Mulberry) |
| 2026 | ICML | — | [Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](https://proceedings.mlr.press/v306/shen26e.html) | — |
| 1998 | Artificial Intelligence | — | [Planning and Acting in Partially Observable Stochastic Domains](https://doi.org/10.1016/S0004-3702(98)00023-X) | — |
| 2026 | arXiv | — | [Planning with the Views](https://arxiv.org/abs/2605.29563) | [Project](https://viewsuite.github.io) · [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2021 | arXiv | — | [Rapid Exploration for Open-World Navigation with Latent Goal Models](https://arxiv.org/abs/2104.05859) | — |
| 2026 | ICLR | — | [Visual Planning: Let's Think Only with Images](https://arxiv.org/abs/2505.11409) | [Code](https://github.com/yix8/VisualPlanning) |

<a id="topic-planning-multiagent-coordination"></a>

#### Multi-Agent Planning and Coordination

31 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | arXiv | ★ Mobile-Agent-E | [Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks](https://arxiv.org/abs/2501.11733) | [Project](https://x-plug.github.io/MobileAgent) · [Code](https://github.com/X-PLUG/MobileAgent) |
| 2026 | ICLR | ★ CoAct-1 | [CoAct-1: Computer-using Multi-Agent System with Coding Actions](https://arxiv.org/abs/2508.03923) | [Code](https://github.com/SalesforceAIResearch/CoAct-1) |
| 2024 | arXiv | ★ AutoRT | [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963) | — |
| 2026 | arXiv | ★ A4VL | [A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning](https://arxiv.org/abs/2603.14052) | [Code](https://github.com/git-disl/A4VL) |
| 2026 | ACL | ★ LongVideoAgent | [LongVideoAgent: Multi-Agent Reasoning with Long Videos](https://arxiv.org/abs/2512.20618) | [Project](https://longvideoagent.github.io/) · [Code](https://github.com/longvideoagent/LongVideoAgent) |
| 2025 | arXiv | ★ GenPilot | [GenPilot: A Multi-Agent System for Test-Time Prompt Optimization in Image Generation](https://arxiv.org/abs/2510.07217) | [Code](https://github.com/27yw/GenPilot) |
| 2025 | arXiv | ★ MARMOT | [Marmot: Object-Level Self-Correction via Multi-Agent Reasoning](https://arxiv.org/abs/2504.20054) | — |
| 2026 | arXiv | ★ IMAGAgent | [IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection](https://arxiv.org/abs/2603.29602) | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2025 | NeurIPS | ★ 4KAgent | [4KAgent: Agentic Any Image to 4K Super-Resolution](https://doi.org/10.52202/085713-5476) · [arXiv](https://arxiv.org/abs/2507.07105) | [Project](https://4kagent.github.io) · [Code](https://github.com/taco-group/4KAgent) |
| 2025 | NeurIPS | ★ PosterAgent | [Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers](https://doi.org/10.52202/085713-0530) · [arXiv](https://arxiv.org/abs/2505.21497) | [Code](https://github.com/Paper2Poster/Paper2Poster) |
| 2025 | NeurIPS | ★ CREA | [CREA: A Collaborative Multi-Agent Framework for Creative Image Editing and Generation](https://doi.org/10.52202/085713-5705) · [arXiv](https://arxiv.org/abs/2504.05306) | — |
| 2026 | ECCV | ★ Agentic 3D Cognition | [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649) | [Project](https://zhangbo135.github.io/agentic-collaborative-cognition/) |
| 2025 | ICML | — | [Agent reviewers: Domain-specific multimodal agents with shared memory for paper review](https://proceedings.mlr.press/v267/lu25p.html) | [Code](https://github.com/AReviewers/AgentReviewers) |
| 2026 | The 4th AI for Visual Arts Workshop | AgentMV | [AgentMV: A State-Guided Multi-Agent Framework for Budget-Aware Music Video Generation](https://arxiv.org/abs/2605.10723) | — |
| 2024 | ICLR | — | [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | — |
| 2026 | CVPR Findings | CarePilot | [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) | — |
| 2026 | EACL | DART | [DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning](https://arxiv.org/abs/2512.07132) | [Code](https://github.com/nsivaku/dart) |
| 2025 | ICLR | EMOS | [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | — |
| 2026 | arXiv | ImageEdit-R1 | [ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning](https://arxiv.org/abs/2603.08059) | [Project](https://github.com/zhaoyiran924/ImageEdit-R1) |
| 2024 | NeurIPS | MDAgents | [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://doi.org/10.52202/079017-2522) · [arXiv](https://arxiv.org/abs/2404.15155) | [Code](https://github.com/mitmedialab/MDAgents) |
| 2025 | NeurIPS | MedAgentBoard | [MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks](https://doi.org/10.52202/085713-4851) · [arXiv](https://arxiv.org/abs/2505.12371) | [Project](https://medagentboard.netlify.app/) · [Code](https://github.com/yhzhu99/MedAgentBoard) |
| 2026 | ICLR | MMedAgent-RL | [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) | — |
| 2026 | ECCV | NeuroRefiner | [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](https://arxiv.org/abs/2608.09636) | — |
| 2025 | ICLR | PARTNR | [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://arxiv.org/abs/2411.00081) | [Code](https://github.com/facebookresearch/partnr-planner) |
| 2025 | ICLR | PathGen-1.6M | [PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://arxiv.org/abs/2407.00203) | [Code](https://github.com/PathFoundation/PathGen-1.6M) |
| 2025 | ICCV | RoboFactory | [RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints](https://arxiv.org/abs/2503.16408) | [Project](https://iranqin.github.io/robofactory/) · [Code](https://github.com/MARS-EAI/RoboFactory) |
| 2026 | arXiv | RoboHarness | [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | — |
| 2026 | CVPR | SciEducator | [SciEducator: Scientific Video Understanding and Educating via Deming-Cycle Multi-Agent System](https://arxiv.org/abs/2511.17943) | — |
| 2025 | NeurIPS | SketchMind | [SketchMind: A Multi-Agent Cognitive Framework for Assessing Student-Drawn Scientific Sketches](https://doi.org/10.52202/085713-2774) · [arXiv](https://arxiv.org/abs/2507.22904) | — |
| 2026 | AAAI | — | [Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916) | — |
| 2025 | CVPR | V-Stylist | [V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents](https://arxiv.org/abs/2503.12077) | — |

<a id="category-memory"></a>

### Vision Memory Infrastructure

<a id="topic-vision-memory-text"></a>

#### Visual-to-Text

14 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | ECCV | ★ VideoAgent (Fan) | [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) | [Project](http://videoagent.github.io) · [Code](https://github.com/YueFan1014/VideoAgent) |
| 2025 | CVPR | ★ VideoTree | [VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos](https://arxiv.org/abs/2405.19209) | [Project](https://videotree2024.github.io/) · [Code](https://github.com/Ziyang412/VideoTree) |
| 2026 | ECCV | ★ EventMemAgent | [EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use](https://arxiv.org/abs/2602.15329) | [Code](https://github.com/lingcco/EventMemAgent) |
| 2026 | CVPR | ★ WorldMM | [WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://arxiv.org/abs/2512.02425) | [Project](https://worldmm.github.io) · [Code](https://github.com/wgcyeo/WorldMM) |
| 2026 | ICLR | ★ M3-Agent | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | [Code](https://github.com/bytedance-seed/m3-agent) |
| 2026 | NeurIPS | ★ GUI-Rise | [GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation](https://arxiv.org/abs/2510.27210) | [Project](https://leon022.github.io/GUI-Rise) · [Code](https://github.com/Leon022/GUI-Rise-code) |
| 2026 | CVPR | ★ AVP | [Active Video Perception: Iterative Evidence Seeking for Agentic Long Video Understanding](https://arxiv.org/abs/2512.05774) | — |
| 2023 | arXiv | ★ REFLECT | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |
| 2026 | arXiv | ★ VAM | [Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval](https://arxiv.org/abs/2605.16481) | [Code](https://github.com/yiliu-li/Visual-Agentic-Memory) |
| 2026 | arXiv | ★ Light-Omni | [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511) | [Project](https://clare-nie.github.io/Light-Omni) · [Code](https://github.com/Clare-Nie/Light-Omni) |
| 2023 | arXiv | ★ MM-REACT | [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381) | [Project](https://multimodal-react.github.io/) · [Code](https://github.com/microsoft/MM-REACT) |
| 2026 | arXiv | ★ MAGIC-Video | [Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning](https://arxiv.org/abs/2605.08271) | [Code](https://github.com/lijiazheng0917/MAGIC-video) |
| 2026 | Official Release | — | [Auditing Prospective Memory in Frozen Language-Model Systems: Causal Mechanisms and the Limits of Naturalistic Trigger Grounding](https://www.preprints.org/manuscript/202608.1081) | [Project](https://www.preprints.org/manuscript/202608.1081) |
| 2023 | ICML | BLIP-2 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | — |

<a id="topic-vision-memory-evidence"></a>

#### Visual Evidence Store

19 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | CVPR | ★ V* | [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://doi.org/10.1109/cvpr52733.2024.01243) · [arXiv](https://arxiv.org/abs/2312.14135) | [Code](https://github.com/penghao-wu/vstar) |
| 2023 | CVPR | ★ VISPROG | [Visual Programming: Compositional visual reasoning without training](https://arxiv.org/abs/2211.11559) | [Code](https://github.com/allenai/visprog) |
| 2026 | arXiv | ★ VAM | [Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval](https://arxiv.org/abs/2605.16481) | [Code](https://github.com/yiliu-li/Visual-Agentic-Memory) |
| 2024 | ECCV | ★ VideoAgent (Fan) | [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) | [Project](http://videoagent.github.io) · [Code](https://github.com/YueFan1014/VideoAgent) |
| 2025 | ICCV | ★ Embodied VideoAgent | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | [Project](https://embodied-videoagent.github.io/) · [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |
| 2026 | CVPR | ★ WorldMM | [WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://arxiv.org/abs/2512.02425) | [Project](https://worldmm.github.io) · [Code](https://github.com/wgcyeo/WorldMM) |
| 2026 | ICLR | ★ M3-Agent | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | [Code](https://github.com/bytedance-seed/m3-agent) |
| 2026 | arXiv | ★ ViSAGE | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | — |
| 2026 | arXiv | ★ V-Mem | [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](https://arxiv.org/abs/2608.01543) | — |
| 2026 | ECCV | ★ MERIT | [Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding](https://arxiv.org/abs/2608.07663) | [Project](https://choi-yeeun.github.io/MERIT/) · [Code](https://github.com/choi-yeeun/MERIT) |
| 2025 | arXiv | ★ VideoExplorer | [VideoExplorer: Think With Videos For Agentic Long-Video Understanding](https://arxiv.org/abs/2506.10821) | [Code](https://github.com/RUC-NLPIR/VideoDeepResearch) |
| 2026 | ECCV | ★ Reflect-R1 | [Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2025 | ICML | — | [Agent reviewers: Domain-specific multimodal agents with shared memory for paper review](https://proceedings.mlr.press/v267/lu25p.html) | [Code](https://github.com/AReviewers/AgentReviewers) |
| 2026 | ACL | Mem-Gallery | [Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents](https://arxiv.org/abs/2601.03515) | [Code](https://github.com/YuanchenBei/Mem-Gallery) |
| 2026 | arXiv | MemCtrl | [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) | — |
| 2025 | arXiv | RoboMemory | [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415) | — |
| 2026 | CVPR | VideoARM | [VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding](https://arxiv.org/abs/2512.12360) | [Project](https://milvlg.github.io/videoarm/) · [Code](https://github.com/MILVLG/videoarm) |
| 2026 | arXiv | — | [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897) | — |
| 2026 | arXiv | WorldMemArena | [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/abs/2605.29341) | [Code](https://github.com/UCSB-AI/WorldMemArena) |

<a id="topic-vision-memory-compression"></a>

#### Visual Compression Layer

15 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2022 | NeurIPS | ★ Flamingo | [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) | — |
| 2026 | ICLR | ★ Memento | [Memento: Toward an All-Day Proactive Assistant for Ultra-Long Streaming Video](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b5f4587a0bdb81ecc6ce9d82320a5c2-Abstract-Conference.html) | — |
| 2025 | arXiv | ★ StreamVLN | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://arxiv.org/abs/2507.05240) | — |
| 2026 | NeurIPS | ★ VLA-Cache | [VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://arxiv.org/abs/2502.02175) | — |
| 2026 | NeurIPS | ★ EfficientVLA | [EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://arxiv.org/abs/2506.10100) | — |
| 2025 | ICCV | ★ SimpAgent | [Less is More: Empowering GUI Agent with Context-Aware Simplification](https://arxiv.org/abs/2507.03730) | — |
| 2025 | CVPR | ★ VideoTree | [VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos](https://arxiv.org/abs/2405.19209) | [Project](https://videotree2024.github.io/) · [Code](https://github.com/Ziyang412/VideoTree) |
| 2026 | ECCV | ★ EventMemAgent | [EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use](https://arxiv.org/abs/2602.15329) | [Code](https://github.com/lingcco/EventMemAgent) |
| 2025 | arXiv | ★ HippoMM | [HippoMM: Hippocampal-inspired Multimodal Memory for Long Audiovisual Event Understanding](https://arxiv.org/abs/2504.10739) | — |
| 2026 | arXiv | ★ Light-Omni | [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511) | [Project](https://clare-nie.github.io/Light-Omni) · [Code](https://github.com/Clare-Nie/Light-Omni) |
| 2026 | arXiv | ★ HyMEM | [Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291) | [Code](https://github.com/NickSiboZhu/HyMEM-GUI-Agent) |
| 2026 | arXiv | ★ VAM | [Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval](https://arxiv.org/abs/2605.16481) | [Code](https://github.com/yiliu-li/Visual-Agentic-Memory) |
| 2026 | arXiv | MemCtrl | [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) | — |
| 2025 | arXiv | MemVerse | [MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627) | [Code](https://github.com/KnowledgeXLab/MemVerse) |
| 2026 | arXiv | — | [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897) | — |

<a id="topic-vision-memory-experience"></a>

#### Visual Experience Repository

42 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | NeurIPS | ★ ICAL | [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://doi.org/10.52202/079017-2418) · [arXiv](https://arxiv.org/abs/2406.14596) | [Project](https://ical-learning.github.io/) · [Code](https://github.com/Gabesarch/ICAL) |
| 2025 | arXiv | ★ ViReSkill | [ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning](https://arxiv.org/abs/2509.24219) | — |
| 2026 | arXiv | ★ HyMEM | [Hybrid Self-evolving Structured Memory for GUI Agents](https://arxiv.org/abs/2603.10291) | [Code](https://github.com/NickSiboZhu/HyMEM-GUI-Agent) |
| 2026 | arXiv | ★ UI-Mem | [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) | [Project](https://ui-mem.github.io) |
| 2026 | CVPR | ★ EchoTrail-GUI | [EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/abs/2512.19396) | — |
| 2026 | arXiv | ★ Darwinian Memory | [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528) | — |
| 2026 | arXiv | ★ RoboHarness (Li) | [RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060) | [Code](https://github.com/LZY-1021/RoboHarness) |
| 2026 | arXiv | ★ KnowAct-GUIClaw | [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/abs/2607.12625) | — |
| 2026 | arXiv | ★ OnEvoMemory | [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749) | — |
| 2026 | arXiv | ★ GenEvolve | [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605) | [Project](https://ephemeral182.github.io/GenEvolve/) · [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2025 | arXiv | ★ ViLoMem | [Agentic Learner with Grow-and-Refine Multimodal Semantic Memory](https://arxiv.org/abs/2511.21678) | [Project](https://weihao-bo.github.io/ViLoMeo-page) · [Code](https://github.com/weihao-bo/ViLoMem) |
| 2026 | AAAI | ★ CA3Mem | [Evolving generalist virtual agents with generative and associative memory](https://ojs.aaai.org/index.php/AAAI/article/view/38300) | — |
| 2026 | NeurIPS | A-MEM | [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | [Code 1](https://github.com/WujiangXu/A-mem) · [Code 2](https://github.com/WujiangXu/A-mem-sys) |
| 2026 | KDD | — | [Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory](https://arxiv.org/abs/2603.15280) | — |
| 2025 | NeurIPS | C-NAV | [C-NAV: Towards Self-Evolving Continual Object Navigation in Open World](https://doi.org/10.52202/085713-4206) · [arXiv](https://arxiv.org/abs/2510.20685) | [Project](https://bigtree765.github.io/C-Nav-project) · [Code](https://github.com/BigTree765/C-Nav) |
| 2024 | ICLR | DiLu | [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://arxiv.org/abs/2309.16292) | [Project](https://pjlab-adg.github.io/DiLu/) · [Code](https://github.com/PJLab-ADG/DiLu) |
| 2025 | arXiv | EgoLife | [EgoLife: Towards Egocentric Life Assistant](https://arxiv.org/abs/2503.03803) | — |
| 2026 | arXiv | ELITE | [ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents](https://arxiv.org/abs/2603.24018) | — |
| 2026 | arXiv | EvoMemNav | [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509) | — |
| 2026 | arXiv | — | [Experience Transfer for Multimodal LLM Agents in Minecraft Game](https://arxiv.org/abs/2604.05533) | — |
| 2026 | ICLR | FaSTA^* | [FaSTA^*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2026 | arXiv | — | [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) | [Project](https://cheng-haha.github.io/GPT-Policy) · [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2026 | ICLR | — | [K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676) | — |
| 2023 | NeurIPS | LIBERO | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | [Project](https://libero-project.github.io) |
| 2026 | arXiv | MementoGUI | [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652) | — |
| 2026 | ACL | Memory-R1 | [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | — |
| 2026 | arXiv | MemRL | [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192) | — |
| 2025 | arXiv | MemVerse | [MemVerse: Multimodal Memory for Lifelong Learning Agents](https://arxiv.org/abs/2512.03627) | [Code](https://github.com/KnowledgeXLab/MemVerse) |
| 2026 | arXiv | MetaSkill-Evolve | [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) | — |
| 2026 | arXiv | MUSE | [MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction](https://arxiv.org/abs/2606.14168) | — |
| 2026 | arXiv | MuSEAgent | [MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences](https://arxiv.org/abs/2603.27813) | — |
| 2026 | arXiv | Omni-SimpleMem | [Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](https://arxiv.org/abs/2604.01007) | [Code](https://github.com/aiming-lab/SimpleMem) |
| 2026 | ICML | — | [Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](https://proceedings.mlr.press/v306/shen26e.html) | — |
| 2026 | ICLR | — | [Planning with an Embodied Learnable Memory](https://openreview.net/forum?id=79BOATBal9) | — |
| 2026 | arXiv | Robo-Cortex | [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729) | — |
| 2025 | arXiv | RoboMemory | [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415) | — |
| 2026 | arXiv | SCAFFOLD | [SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction](https://arxiv.org/abs/2609.05511) | [Code](https://github.com/BokwaiHo/SCAFFOLD) |
| 2026 | arXiv | SE-GA | [SE-GA: Memory-Augmented Self-Evolution for GUI Agents](https://arxiv.org/abs/2605.16883) | [Code](https://github.com/jinshilong-dev/SE-GA) |
| 2025 | arXiv | SE-VLN | [SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models](https://arxiv.org/abs/2507.13152) | — |
| 2025 | CVPR | — | [Self-Evolving Visual Concept Library using Vision-Language Critics](https://arxiv.org/abs/2504.00185) | — |
| 2026 | arXiv | WorldMemArena | [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/abs/2605.29341) | [Code](https://github.com/UCSB-AI/WorldMemArena) |
| 2025 | arXiv | π^*_0.6 | [π^*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) | — |

<a id="category-tools"></a>

### Visual Tools

<a id="topic-visual-tools-observation"></a>

#### Observation Tools

27 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2023 | CVPR | ★ VISPROG | [Visual Programming: Compositional visual reasoning without training](https://arxiv.org/abs/2211.11559) | [Code](https://github.com/allenai/visprog) |
| 2023 | ICCV | ★ ViperGPT | [ViperGPT: Visual Inference via Python Execution for Reasoning](https://openaccess.thecvf.com/content/ICCV2023/html/Suris_ViperGPT_Visual_Inference_via_Python_Execution_for_Reasoning_ICCV_2023_paper.html) · [arXiv](https://arxiv.org/abs/2303.08128) | [Project](https://viper.cs.columbia.edu/) · [Code](https://github.com/cvlab-columbia/viper) |
| 2024 | CVPR | ★ CLOVA | [CLOVA: A Closed-Loop Visual Assistant with Tool Usage and Update](https://arxiv.org/abs/2312.10908) | [Code](https://github.com/clova-tool/CLOVA-tool) |
| 2025 | arXiv | ★ OctoTools | [OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning](https://arxiv.org/abs/2502.11271) | [Project](https://octotools.github.io/) · [Code](https://github.com/octotools/octotools) |
| 2024 | ECCV | ★ DetToolChain | [DetToolChain: A New Prompting Paradigm to Unleash Detection Ability of MLLM](https://arxiv.org/abs/2403.12488) | — |
| 2025 | arXiv | ★ RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2025 | ICML | ★ MedRAX | [MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673) | [Code](https://github.com/bowang-lab/MedRAX) |
| 2025 | arXiv | ★ PyVision | [PyVision: Agentic Vision with Dynamic Tooling](https://arxiv.org/abs/2507.07998) | [Code](https://github.com/agents-x-project/PyVision) |
| 2026 | ICLR | ★ DeepEyes | [DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning](https://arxiv.org/abs/2505.14362) | [Code](https://github.com/Visual-Agent/DeepEyes) |
| 2026 | ICLR | ★ VideoZoomer | [VideoZoomer: Reinforcement-Learned Temporal Focusing for Long Video Reasoning](https://arxiv.org/abs/2512.22315) | [Code](https://github.com/zsgvivo/VideoZoomer) |
| 2025 | CVPR | ★ SegAgent | [SegAgent: Exploring Pixel Understanding Capabilities in MLLMs by Imitating Human Annotator Trajectories](https://arxiv.org/abs/2503.08625) | [Code](https://github.com/aim-uofa/SegAgent) |
| 2026 | CVPR | ★ GCA | [Geometrically-Constrained Agent for Spatial Reasoning](https://arxiv.org/abs/2511.22659) | [Project](https://gca-spatial-reasoning.github.io) · [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2025 | arXiv | Active-o3 | [Active-o3: Empowering multimodal large language models with active perception via grpo](https://arxiv.org/abs/2505.21457) | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 2026 | arXiv | AutoFocus | [AutoFocus: Uncertainty-Aware Active Visual Search for GUI Grounding](https://arxiv.org/abs/2605.02630) | [Code](https://github.com/Mr-Bigworth/AutoFocus) |
| 2026 | ICML | AutoMat | [AutoMat: Physics-Guided Agentic Reasoning for Solving Ill-Posed Inverse Microscopy Problems](https://openreview.net/forum?id=TLroFiKilA) · [arXiv](https://arxiv.org/abs/2505.12650) | [Code](https://github.com/yyt-2378/AutoMat) |
| 2026 | arXiv | BVS | [BVS: Bayesian Visual Search with Multimodal Large Language Model for Fine-grained Perception](https://arxiv.org/abs/2607.03184) | [Code](https://github.com/PKU-ICST-MIPL/BVS_ICML2026) |
| 2025 | CVPR | DyFo | [DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding](https://arxiv.org/abs/2504.14920) | [Code](https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025) |
| 2026 | CVPR Findings | — | [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | — |
| 2026 | CVPR | IBISAgent | [IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation](https://arxiv.org/abs/2601.03054) | [Code](https://github.com/Yankai96/IBISAgent) |
| 2024 | arXiv | Mobile-Agent | [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158) | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2025 | arXiv | NOVA | [NOVA: An Agentic Framework for Automated Histopathology Analysis and Discovery](https://arxiv.org/abs/2511.11324) | [Code](https://github.com/microsoft/nova-agent) |
| 2026 | ICLR | OSWorld-MCP | [OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents](https://arxiv.org/abs/2510.24563) | [Project](https://osworld-mcp.github.io) · [Code](https://github.com/X-PLUG/OSWorld-MCP) |
| 2023 | ICCV | — | [Segment Anything](https://arxiv.org/abs/2304.02643) | [Project](https://segment-anything.com) · [Code](https://github.com/facebookresearch/segment-anything) |
| 2026 | ECCV | TopoAgent | [TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging](https://arxiv.org/abs/2606.29763) | [Code](https://github.com/gm3g11/TopoAgent) |
| 2019 | arXiv | — | [Toward Real-World Single Image Super-Resolution: A New Benchmark and A New Model](https://arxiv.org/abs/1904.00523) | — |
| 2025 | arXiv | — | [Towards Agentic AI for Multimodal-Guided Video Object Segmentation](https://arxiv.org/abs/2508.10572) | — |

<a id="topic-visual-tools-search"></a>

#### Search Tools

14 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2023 | NeurIPS | ★ AVIS | [AVIS: Autonomous Visual Information Seeking with Large Language Model Agent](https://doi.org/10.52202/075280-0040) · [arXiv](https://arxiv.org/abs/2306.08129) | — |
| 2025 | arXiv | ★ MMSearch-R1 | [MMSearch-R1: Incentivizing LMMs to Search](https://arxiv.org/abs/2506.20670) | [Code](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) |
| 2026 | ICLR | ★ WebWatcher | [Webwatcher: Breaking new frontiers of vision-language deep research agent](https://arxiv.org/abs/2508.05748) | — |
| 2026 | ICML | ★ Vision-DeepResearch | [Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models](https://proceedings.mlr.press/v306/huang26bx.html) | — |
| 2026 | arXiv | ★ ProMMSearchAgent | [ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards](https://arxiv.org/abs/2604.20486) | — |
| 2024 | NeurIPS | ★ AvaTaR | [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://arxiv.org/abs/2406.11200) | [Code](https://github.com/zou-group/avatar) |
| 2025 | arXiv | ★ World-To-Image | [World-To-Image: Grounding Text-to-Image Generation with Agent-Driven World Knowledge](https://arxiv.org/abs/2510.04201) | [Code](https://github.com/mhson-kyle/World-To-Image) |
| 2026 | CVPR | ★ EvoGraph-R1 | [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](https://arxiv.org/abs/2607.12764) | — |
| 2024 | ECCV | ★ VideoAgent (Fan) | [VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding](https://arxiv.org/abs/2403.11481) | [Project](http://videoagent.github.io) · [Code](https://github.com/YueFan1014/VideoAgent) |
| 2025 | ICCV | ★ Embodied VideoAgent | [Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding](https://arxiv.org/abs/2501.00358) | [Project](https://embodied-videoagent.github.io/) · [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |
| 2026 | ICLR | ★ M3-Agent | [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | [Code](https://github.com/bytedance-seed/m3-agent) |
| 2026 | arXiv | ★ V-Mem | [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](https://arxiv.org/abs/2608.01543) | — |
| 2023 | arXiv | — | [Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?](https://arxiv.org/abs/2302.11713) | — |
| 2020 | arXiv | — | [What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams](https://arxiv.org/abs/2009.13081) | — |

<a id="topic-visual-tools-generation"></a>

#### Generation Tools

54 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2022 | CVPR | ★ Latent Diffusion | [High-Resolution Image Synthesis with Latent Diffusion Models](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) · [arXiv](https://arxiv.org/abs/2112.10752) | [Code](https://github.com/CompVis/latent-diffusion) |
| 2023 | ICCV | ★ ControlNet | [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543) | [Code](https://github.com/lllyasviel/ControlNet) |
| 2023 | arXiv | ★ IP-Adapter | [IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models](https://arxiv.org/abs/2308.06721) | [Project](https://ip-adapter.github.io) · [Code](https://github.com/tencent-ailab/IP-Adapter) |
| 2023 | CVPR | ★ InstructPix2Pix | [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://arxiv.org/abs/2211.09800) | [Project](https://www.timothybrooks.com/instruct-pix2pix) |
| 2023 | arXiv | ★ Visual ChatGPT | [Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models](https://arxiv.org/abs/2303.04671) | [Code](https://github.com/chenfei-wu/TaskMatrix) |
| 2024 | NeurIPS | ★ GenArtist | [GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing](https://arxiv.org/abs/2407.05600) | [Project](https://zhenyuw16.github.io/GenArtist_page) · [Code](https://github.com/zhenyuw16/GenArtist) |
| 2026 | arXiv | ★ IMAGAgent | [IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection](https://arxiv.org/abs/2603.29602) | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2026 | arXiv | ★ ViMax | [ViMax: Agentic Video Generation](https://arxiv.org/abs/2606.07649) | [Code](https://github.com/HKUDS/ViMax) |
| 2024 | ICML | ★ SceneCraft | [SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code](https://arxiv.org/abs/2403.01248) | — |
| 2026 | ICML | ★ SceneSmith | [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153) | [Project](https://scenesmith.github.io/) · [Code](https://github.com/nepfaff/scenesmith) |
| 2023 | NeurIPS | ★ LayoutGPT | [LayoutGPT: Compositional Visual Planning and Generation with Large Language Models](https://arxiv.org/abs/2305.15393) | [Code](https://github.com/weixi-feng/layoutgpt) |
| 2024 | IUI | ★ LAVE | [LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/abs/2402.10294) | — |
| 2026 | ICML | — | [Agentic Model Predictive Questioning Control in Visual Design](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | arXiv | — | [Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046) | — |
| 2026 | arXiv | — | [Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758) | [Code](https://github.com/YinmingHuang/Awesome-agentic-visual-generation-model) |
| 2026 | The 4th AI for Visual Arts Workshop | AgentMV | [AgentMV: A State-Guided Multi-Agent Framework for Budget-Aware Music Video Generation](https://arxiv.org/abs/2605.10723) | — |
| 2026 | arXiv | — | [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing](https://arxiv.org/abs/2607.08497) | [Project](https://caseclose.github.io/cma-harness/) · [Code](https://github.com/caseclose/cma-harness) |
| 2025 | CVPR | ComfyBench | [ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems](https://arxiv.org/abs/2409.01392) | [Code](https://github.com/xxyQwQ/ComfyBench) |
| 2025 | ACL Demos | ComfyUI-Copilot | [ComfyUI-Copilot: An Intelligent Assistant for Automated Workflow Development](https://arxiv.org/abs/2506.05010) | [Code](https://github.com/ATH-MaaS/ComfyUI-Copilot) |
| 2024 | arXiv | ELLA | [ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment](https://arxiv.org/abs/2403.05135) | [Project](https://ella-diffusion.github.io/) · [Code](https://github.com/TencentQQGYLab/ELLA) |
| 2026 | ICLR | FaSTA^* | [FaSTA^*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2026 | arXiv | FiRe | [FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation](https://arxiv.org/abs/2604.13491) | — |
| 2026 | ECCV | GenAgent | [GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning](https://arxiv.org/abs/2601.18543) | [Code](https://github.com/deep-kaixun/GenAgent) |
| 2024 | ICML | — | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | [Project](https://sites.google.com/corp/view/genie-2024/) |
| 2025 | arXiv | GoT | [GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing](https://arxiv.org/abs/2503.10639) | [Code](https://github.com/rongyaofang/GoT) |
| 2022 | arXiv | — | [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125) | — |
| 2026 | arXiv | InternVL-U | [InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing](https://arxiv.org/abs/2603.09877) | [Code](https://github.com/OpenGVLab/InternVL-U) |
| 2026 | ICML | LiveFigure | [LiveFigure: Generating Editable Scientific Illustration with VLM Agents](https://arxiv.org/abs/2605.23527) | [Code](https://github.com/tsinghua-fib-lab/LiveFigure) |
| 2023 | arXiv | LLM-grounded Diffusion | [LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models](https://arxiv.org/abs/2305.13655) | — |
| 2023 | NeurIPS | MagicBrush | [MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing](https://arxiv.org/abs/2306.10012) | [Project](https://osu-nlp-group.github.io/MagicBrush/) · [Code](https://github.com/OSU-NLP-Group/MagicBrush) |
| 2024 | ICML | Mastering Text-to-Image Diffusion | [Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs](https://arxiv.org/abs/2401.11708) | [Code](https://github.com/YangLing0818/RPG-DiffusionMaster) |
| 2024 | arXiv | Movie Gen | [Movie Gen: A Cast of Media Foundation Models](https://arxiv.org/abs/2410.13720) | — |
| 2026 | arXiv | MUSE | [MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction](https://arxiv.org/abs/2606.14168) | — |
| 2026 | arXiv | NEWTON | [NEWTON: Agentic Planning for Physically Grounded Video Generation](https://arxiv.org/abs/2605.18396) | [Project](https://Newton026.github.io/newton) · [Code](https://github.com/CUTEPKQ/NEWTON) |
| 2026 | CVPR | OctoT2I | [OctoT2I: A Self-Evolving Agentic Text-to-Image Router](https://arxiv.org/abs/2606.01803) | [Code](https://github.com/JaxJiang2642081986/OctoT2I) |
| 2026 | ICLR | PerfGuard | [PerfGuard: A Performance-Aware Agent for Visual Content Generation](https://arxiv.org/abs/2601.22571) | [Project](https://openreview.net/forum?id=tdN42GTv4S) · [Code](https://github.com/FelixChan9527/PerfGuard) |
| 2026 | ICLR | PhyScensis | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://arxiv.org/abs/2602.14968) | — |
| 2025 | ECIR | PlotEdit | [PlotEdit: Natural Language-Driven Accessible Chart Editing in PDFs via Multimodal LLM Agents](https://arxiv.org/abs/2501.11233) | — |
| 2024 | arXiv | — | [Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419) | [Project](https://www.kaggle.com/datasets/googleai/pasta-data) |
| 2025 | ICML | — | [Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty](https://arxiv.org/abs/2412.06771) | [Code](https://github.com/google-deepmind/proactive_t2i_agents) |
| 2026 | arXiv | — | [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230) | — |
| 2026 | ICML | PSBench | [PSBench: Editing Image via GUI Agents in Photoshop](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | ECCV | ReDesign | [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](https://arxiv.org/abs/2607.25565) | — |
| 2024 | NeurIPS | RestoreAgent | [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://doi.org/10.52202/079017-3512) · [arXiv](https://arxiv.org/abs/2407.18035) | — |
| 2026 | arXiv | — | [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147) | — |
| 2026 | CVPR | SAGE | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | [Project](https://research.nvidia.com/labs/dir/sage/) |
| 2026 | CVPR Workshops | — | [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | — |
| 2025 | NeurIPS | SceneWeaver | [SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent](https://doi.org/10.52202/085713-4689) · [arXiv](https://arxiv.org/abs/2509.20414) | [Project](https://scene-weaver.github.io/) · [Code](https://github.com/Scene-Weaver/SceneWeaver) |
| 2024 | CVPR | — | [Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090) | — |
| 2026 | AAAI | — | [Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916) | — |
| 2026 | ECCV | TIR-Agent | [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) | — |
| 2026 | ICML | UI2Code^N | [UI2Code^N: UI-to-Code Generation as Interactive Visual Optimization](https://proceedings.mlr.press/v306/yang26v.html) | — |
| 2026 | arXiv | VideoAgent | [VideoAgent: All-in-One Framework for Video Understanding and Editing](https://arxiv.org/abs/2606.23327) | [Code](https://github.com/HKUDS/VideoAgent) |
| 2026 | ECCV | WorldAgents | [WorldAgents: Can Foundation Image Models be Agents for 3D World Models?](https://arxiv.org/abs/2603.19708) | [Project 1](https://ziyaerkoc.com/worldagents/) · [Project 2](https://www.youtube.com/watch?v=Mj2FqqhurdI) |

<a id="category-verification"></a>

### Vision Verification Infrastructure

<a id="topic-verification-evidence"></a>

#### Evidence Verification

13 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ LookBack | [VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning](https://arxiv.org/abs/2412.02172) | [Project](https://visco-benchmark.github.io/) · [Code](https://github.com/PlusLabNLP/VISCO) |
| 2026 | arXiv | ★ Perceval | [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) | [Code](https://github.com/RUCAIBox/Perceval) |
| 2026 | CVPR | ★ ARM-Thinker | [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](https://arxiv.org/abs/2512.05111) | — |
| 2026 | ICLR | ★ VideoMind | [VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](https://arxiv.org/abs/2503.13444) | [Project](https://videomind.github.io/) · [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | arXiv | ★ Kestrel | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2026 | ECCV | ★ Reflect-R1 | [Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | ICLR | ★ CARE | [CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework](https://arxiv.org/abs/2603.01607) | [Project](https://xypb.github.io/CARE-Project-Page/) · [Code](https://github.com/XYPB/CARE) |
| 2026 | arXiv | ★ ViSAGE | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | — |
| 2026 | ECCV | ★ VERITAS | [VERITAS: A Multi-Agent Co-Scientist for Verifiable Image-Derived Hypothesis Testing](https://arxiv.org/abs/2604.12144) | [Code](https://github.com/LucZot/veritas) |
| 2026 | arXiv | ★ ForgeryVCR | [ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098) | [Code](https://github.com/youqiwong/ForgeryVCR) |
| 2026 | CVPR | ★ GCA | [Geometrically-Constrained Agent for Spatial Reasoning](https://arxiv.org/abs/2511.22659) | [Project](https://gca-spatial-reasoning.github.io) · [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2025 | CVPR | ★ ViUniT | [ViUniT: Visual Unit Tests for More Robust Visual Programming](https://arxiv.org/abs/2412.08859) | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2019 | CVPR | GQA | [GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506) | — |

<a id="topic-verification-process"></a>

#### Process Verification

13 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2025 | CVPR | ★ Code-as-Monitor | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2024 | arXiv | ★ Sentinel | [Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress](https://arxiv.org/abs/2410.04640) | [Project](https://sites.google.com/stanford.edu/sentinel) · [Code](https://github.com/agiachris/sentinel) |
| 2025 | CVPR | ★ ViUniT | [ViUniT: Visual Unit Tests for More Robust Visual Programming](https://arxiv.org/abs/2412.08859) | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2024 | EMNLP Findings | ★ VDebugger | [VDebugger: Harnessing Execution Feedback for Debugging Visual Programs](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2026 | CVPR | ★ OS-Oracle | [OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models](https://arxiv.org/abs/2512.16295) | [Code](https://github.com/numbmelon/OS-Oracle) |
| 2026 | ACL | ★ VeriGUI | [Don’t act blindly: Robust gui automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2026 | ECCV | ★ VisCritic | [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525) | — |
| 2026 | arXiv | ★ IntentScore | [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) | — |
| 2025 | CoRL Workshops | ★ Guardian | [Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models](https://arxiv.org/abs/2512.01946) | [Project](https://openreview.net/forum?id=wps46mtC9B) · [Code](https://github.com/paulpacaud/Guardian-FailCot) |
| 2025 | arXiv | ★ I-FailSense | [I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models](https://arxiv.org/abs/2509.16072) | [Project](https://clemgris.github.io/I-FailSense/) · [Code](https://github.com/clemgris/I-FailSense) |
| 2026 | arXiv | ★ GAIA | [GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models](https://arxiv.org/abs/2601.18197) | [Code](https://github.com/SeerRay-Lab/GAIA) |
| 2023 | arXiv | ★ REFLECT | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |
| 2026 | arXiv | GameWorld | [GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/abs/2604.07429) | [Project](https://gameworld-bench.github.io) · [Code](https://github.com/gameworld-project/gameworld) |

<a id="topic-verification-outcome"></a>

#### Outcome Verification

39 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2023 | ICCV | ★ TIFA | [TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering](https://arxiv.org/abs/2303.11897) | [Code](https://github.com/Yushi-Hu/tifa) |
| 2023 | NeurIPS | ★ GenEval | [GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment](https://arxiv.org/abs/2310.11513) | [Code](https://github.com/djghosh13/geneval) |
| 2024 | CVPR | ★ VBench | [VBench: Comprehensive Benchmark Suite for Video Generative Models](https://arxiv.org/abs/2311.17982) | [Project](https://vchitect.github.io/VBench-project/) · [Code](https://github.com/Vchitect/VBench) |
| 2025 | CVPR | ★ LLaVA-Critic | [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://arxiv.org/abs/2410.02712) | [Project](https://llava-vl.github.io/blog/2024-10-03-llava-critic) · [Code](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2025 | arXiv | ★ EdiVal-Agent | [EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing](https://arxiv.org/abs/2509.13399) | [Code](https://github.com/TianyuCodings/EdiVal) |
| 2025 | arXiv | ★ WISE | [WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation](https://arxiv.org/abs/2503.07265) | [Code](https://github.com/PKU-YuanGroup/WISE) |
| 2026 | CVPR | ★ RetouchIQ | [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) | — |
| 2026 | ICLR | ★ ProRe | [ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration](https://arxiv.org/abs/2509.21823) | [Code](https://github.com/V-Droid-Agent/ProRe) |
| 2026 | arXiv | ★ OS-Themis | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) | — |
| 2026 | arXiv | ★ Universal Verifier | [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/abs/2604.06240) | [Code](https://github.com/microsoft/fara) |
| 2024 | NeurIPS | ★ OSWorld | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) | [Project](https://os-world.github.io) · [Code](https://github.com/xlang-ai/OSWorld) |
| 2025 | ICLR | ★ AndroidWorld | [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573) | [Code](https://github.com/google-research/android_world) |
| 2024 | NeurIPS Datasets and Benchmarks | — | [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving](https://arxiv.org/abs/2406.03877) | [Code](https://github.com/Thinklab-SJTU/Bench2Drive) |
| 2024 | NeurIPS | DISCOVERYWORLD | [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](https://doi.org/10.52202/079017-0324) · [arXiv](https://arxiv.org/abs/2406.06769) | [Code](https://github.com/allenai/discoveryworld) |
| 2025 | ICML | EmbodiedBench | [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560) | [Project](https://embodiedbench.github.io) · [Code](https://github.com/EmbodiedBench/EmbodiedBench) |
| 2024 | arXiv | — | [Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941) | — |
| 2026 | arXiv | GameWorld | [GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents](https://arxiv.org/abs/2604.07429) | [Project](https://gameworld-bench.github.io) · [Code](https://github.com/gameworld-project/gameworld) |
| 2025 | arXiv | GenEval 2 | [GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/abs/2512.16853) | [Code](https://github.com/facebookresearch/GenEval2) |
| 2026 | arXiv | — | [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](https://arxiv.org/abs/2606.15032) | — |
| 2026 | CVPR | LIBERO-Plus | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf) · [arXiv](https://arxiv.org/abs/2510.13626) | [Code](https://github.com/sylvestf/LIBERO-plus) |
| 2023 | NeurIPS | MagicBrush | [MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing](https://arxiv.org/abs/2306.10012) | [Project](https://osu-nlp-group.github.io/MagicBrush/) · [Code](https://github.com/OSU-NLP-Group/MagicBrush) |
| 2026 | CVPR | MMBench-GUI | [MMBench-GUI: A Unified Hierarchical Evaluation Framework for Multi-Platform GUI Agents](https://arxiv.org/abs/2507.19478) | [Code](https://github.com/open-compass/MMBench-GUI) |
| 2026 | ICLR | — | [Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games](https://arxiv.org/abs/2506.03610) | [Project](https://huggingface.co/datasets/KRAFTON/Orak) · [Code](https://github.com/krafton-ai/Orak) |
| 2026 | arXiv | PlayWorld | [PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives](https://arxiv.org/abs/2608.13552) | [Project](https://kxding.github.io/project/PlayWorld/) · [Code](https://github.com/hku-sail/PlayWorld) |
| 2026 | arXiv | PPTBench | [PPTBench: Can Coding Agents Reconstruct the Visual World through Structured, Editable Slides](https://arxiv.org/abs/2609.29718) | — |
| 2026 | ICML | PSBench | [PSBench: Editing Image via GUI Agents in Photoshop](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2025 | arXiv | — | [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | — |
| 2019 | arXiv | RLBench | [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271) | — |
| 2025 | ICLR | ScienceAgentBench | [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://arxiv.org/abs/2410.05080) | [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| 2025 | TPAMI | T2I-CompBench++ | [T2I-CompBench++: An Enhanced and Comprehensive Benchmark for Compositional Text-to-image Generation](https://arxiv.org/abs/2307.06350) | [Project](https://karine-h.github.io/T2I-CompBench-new/) · [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| 2023 | NeurIPS | T2i-compbench | [T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation](https://arxiv.org/abs/2307.06350v1) | [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| 2024 | arXiv | THE COLOSSEUM | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191) | — |
| 2019 | arXiv | — | [Toward Real-World Single Image Super-Resolution: A New Benchmark and A New Model](https://arxiv.org/abs/1904.00523) | — |
| 2025 | ICML | — | [Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation](https://arxiv.org/abs/2410.05363) | [Project](https://phygenbench123.github.io/) · [Code](https://github.com/OpenGVLab/PhyGenBench) |
| 2026 | ICLR | VideoPhy-2 | [VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation](https://arxiv.org/abs/2503.06800) | [Project](https://videophy2.github.io/) · [Code](https://github.com/Hritikbansal/videophy/tree/main/VIDEOPHY2) |
| 2026 | arXiv | WBench | [WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/abs/2605.25874) | [Project](https://meituan-longcat.github.io/WBench/) · [Code](https://github.com/meituan-longcat/WBench) |
| 2026 | arXiv | — | [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) | — |
| 2024 | arXiv | Windows Agent Arena | [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://arxiv.org/abs/2409.08264) | — |
| 2026 | arXiv | WorldMark | [WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686) | [Code](https://github.com/AlayaLab/WorldMark) |

<a id="category-safety"></a>

### Safety Infrastructure

<a id="topic-safety-visual-information"></a>

#### Visual Information Safeguard

9 works · 8 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | arXiv | ★ MINIM | [Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization](https://arxiv.org/abs/2606.13949) | [Code](https://github.com/yyyyhx/MINIM) |
| 2026 | ICLR | ★ VPI-Bench | [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456) | [Code](https://github.com/cua-framework/agents) |
| 2026 | NeurIPS | ★ WASP | [WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks](https://arxiv.org/abs/2504.18575) | [Code](https://github.com/facebookresearch/wasp) |
| 2024 | NeurIPS | ★ AgentDojo | [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352) | [Code](https://github.com/ethz-spylab/agentdojo) |
| 2026 | arXiv | ★ ForgeryVCR | [ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098) | [Code](https://github.com/youqiwong/ForgeryVCR) |
| 2026 | arXiv | ★ Kestrel | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2025 | CVPR | ★ LookBack | [VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning](https://arxiv.org/abs/2412.02172) | [Project](https://visco-benchmark.github.io/) · [Code](https://github.com/PlusLabNLP/VISCO) |
| 2026 | arXiv | ★ Perceval | [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) | [Code](https://github.com/RUCAIBox/Perceval) |
| 2026 | CHI | — | [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight](https://arxiv.org/abs/2509.10723) | — |

<a id="topic-safety-constrained-execution"></a>

#### Safety-Constrained Execution

21 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | RA-L | ★ RoboGuard | [Safety Guardrails for LLM-Enabled Robots](https://arxiv.org/abs/2503.07885) | [Project](https://robo-guard.github.io/) · [Code](https://github.com/KumarRobotics/RoboGuard) |
| 2026 | NeurIPS | ★ SafeVLA | [SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning](https://arxiv.org/abs/2503.03480) | [Project](https://pku-safevla.github.io) · [Code](https://github.com/PKU-Alignment/SafeVLA) |
| 2025 | IROS | ★ SALT | [Robots that Suggest Safe Alternatives](https://arxiv.org/abs/2409.09883) | — |
| 2023 | arXiv | ★ KnowNo | [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928) | [Project](https://robot-help.github.io) · [Code](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| 2026 | ICML | ★ PACT | [PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation](https://arxiv.org/abs/2606.08414) | [Code](https://github.com/thu-ml/PACT) |
| 2025 | arXiv | ★ RoboChemist | [RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation](https://arxiv.org/abs/2509.08820) | [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) |
| 2024 | arXiv | ★ ReKep | [ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation](https://arxiv.org/abs/2409.01652) | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |
| 2025 | ICLR | ★ ConformalDAgger | [Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback](https://arxiv.org/abs/2410.08852) | — |
| 2025 | arXiv | ★ Magentic-UI | [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358) | [Code](https://github.com/microsoft/magentic-ui/tree/magentic-ui-0.1) |
| 2025 | NAACL Demos | ★ CowPilot | [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609) | [Project](https://oaishi.github.io/cowpilot.html) · [Code](https://github.com/oaishi/CowPilot) |
| 2024 | NeurIPS | ★ IntroPlan | [Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity](https://arxiv.org/abs/2402.06529) | [Project](https://introplan.github.io) · [Code](https://github.com/kevinliang888/IntroPlan) |
| 2026 | arXiv | ★ UPS | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) | — |
| 2026 | CVPR | AGENTSAFE | [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697) | — |
| 2026 | CVPR | CapNav | [CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation](https://arxiv.org/abs/2602.18424) | [Code](https://github.com/makeabilitylab/CapNav) |
| 2026 | arXiv | — | [Clarify Before Executing: A Self-Evolving Agent for Resolving Intent Asymmetry in 3D Tool Orchestration](https://arxiv.org/abs/2607.16352) | [Code](https://github.com/xyzhu1225/CLARE) |
| 2026 | ICLR | — | [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670) | — |
| 2025 | NeurIPS | OS-Harm | [OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2506.14866) | [Code](https://github.com/tml-epfl/os-harm) |
| 2026 | NeurIPS | — | [Real-Time Execution of Action Chunking Flow Policies](https://arxiv.org/abs/2506.07339) | [Project](https://pi.website/research/real_time_chunking) · [Code](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) |
| 2026 | arXiv | — | [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147) | — |
| 2022 | arXiv | — | [Socially Compliant Navigation Dataset (SCAND): A Large-Scale Dataset of Demonstrations for Social Navigation](https://arxiv.org/abs/2203.15041) | — |
| 2025 | arXiv | — | [Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models](https://arxiv.org/abs/2503.01876) | — |

<a id="topic-safety-runtime-oversight"></a>

#### Runtime Oversight and Traceability

15 works · 12 Figure 1 representatives.

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2024 | arXiv | ★ Sentinel | [Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress](https://arxiv.org/abs/2410.04640) | [Project](https://sites.google.com/stanford.edu/sentinel) · [Code](https://github.com/agiachris/sentinel) |
| 2025 | CVPR | ★ Code-as-Monitor | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2023 | arXiv | ★ REFLECT | [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | [Project](https://robot-reflect.github.io/) · [Code](https://github.com/real-stanford/reflect) |
| 2024 | EMNLP Findings | ★ VDebugger | [VDebugger: Harnessing Execution Feedback for Debugging Visual Programs](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2026 | arXiv | ★ Universal Verifier | [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/abs/2604.06240) | [Code](https://github.com/microsoft/fara) |
| 2025 | arXiv | ★ FAIL-Detect | [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](https://arxiv.org/abs/2503.08558) | — |
| 2024 | arXiv | ★ AHA | [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://arxiv.org/abs/2410.00371) | [Project](https://aha-vlm.github.io/) · [Code](https://github.com/NVlabs/AHA/tree/main) |
| 2025 | arXiv | ★ I-FailSense | [I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models](https://arxiv.org/abs/2509.16072) | [Project](https://clemgris.github.io/I-FailSense/) · [Code](https://github.com/clemgris/I-FailSense) |
| 2025 | arXiv | ★ RoboFAC | [RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction](https://arxiv.org/abs/2505.12224) | [Code](https://github.com/MINT-SJTU/RoboFAC) |
| 2026 | ACL | ★ VeriGUI | [Don’t act blindly: Robust gui automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2025 | CoRL Workshops | ★ Guardian | [Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models](https://arxiv.org/abs/2512.01946) | [Project](https://openreview.net/forum?id=wps46mtC9B) · [Code](https://github.com/paulpacaud/Guardian-FailCot) |
| 2026 | ACL | ★ RoboFailRing | [RoboFailRing: Retrieval-Augmented and Language Grounding Failure Detection for VLM-enabled Robotic Manipulation](https://aclanthology.org/2026.acl-long.602/) | [Code](https://github.com/DynamicPoet/RoboFailRing) |
| 2025 | NAACL Demos | CowPilot | [CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation](https://arxiv.org/abs/2501.16609) | [Project](https://oaishi.github.io/cowpilot.html) · [Code](https://github.com/oaishi/CowPilot) |
| 2026 | CHI | — | [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight](https://arxiv.org/abs/2509.10723) | — |
| 2026 | ICLR | — | [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670) | — |

## 🙏 Acknowledgements

The table presentation is inspired by [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications). The earlier topic archive also drew on [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). Linked papers and software retain their respective authorship and licenses.

## 📝 Citation

Use [references.bib](references.bib) to cite the individual works. A citation for the survey will be added when its public bibliographic record is available.
