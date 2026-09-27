# Awesome Vision Agents

**Seeing the Horizon of Vision Agent: A Survey**

A collection of papers, code, and benchmarks on vision agents, organized by the chapters and subsections of our survey.

**471 unique works** · **454 arXiv entries** · **305 works with code** · **497 BibTeX keys**

## Overview

The collection covers the foundations of vision agents, runtime harnesses, capability acquisition and evolution, applications, evaluation, and open challenges. Section 3 follows the latest paradigm-based organization of visual evidence acquisition, visual memory, and grounded reasoning and planning.

**How to read the tables.** Years follow the bibliography, except for primary-source corrections recorded in the catalogue; arXiv versions may have an earlier date. A dash (—) means that a link has not been identified and verified for this catalogue; it does not mean that a paper or implementation does not exist. Code links come from the paper, its author project, or a repository that identifies the paper. “Unavailable” marks an author-linked repository that could not be accessed at the snapshot date. The same work can appear in several relevant sections; duplicate BibTeX keys are merged in each table.

[Full bibliography](references.bib) · [Machine-readable catalogue](data/papers.json) · [Coverage and provenance](docs/COVERAGE.md) · [Contributing](CONTRIBUTING.md)

## Table of Contents

- [1. Introduction](#section-1)
- [2. Background](#section-2)
  - [2.1. From Visual Models to Vision Agents](#section-2-1)
  - [2.2. Agent Models, Harnesses, and Environments](#section-2-2)
  - [2.3. Runtime Interaction and Capability Evolution](#section-2-3)
- [3. Vision Agent Harnesses](#section-3)
  - [3.1. Active Visual Evidence Acquisition](#section-3-1)
  - [3.2. Visual Memory and State Management](#section-3-2)
  - [3.3. Evidence-Grounded Reasoning and Planning](#section-3-3)
- [4. Capability Acquisition and Evolution in Vision Agents](#section-4)
  - [4.1. From Capability Acquisition to Self-Evolution](#section-4-1)
  - [4.2. Targets of Self-Evolution](#section-4-2)
  - [4.3. Mechanisms and Timescales of Evolution](#section-4-3)
  - [4.4. Toward Recursive Self-Improvement](#section-4-4)
  - [4.5. Challenges in Capability Evolution](#section-4-5)
- [5. Applications of Vision Agents](#section-5)
  - [5.1. Visual Understanding and Reasoning](#section-5-1)
  - [5.2. Visual Generation, Editing, and World Construction](#section-5-2)
  - [5.3. GUI and Digital Environment Interaction](#section-5-3)
  - [5.4. Embodied Agents and Autonomous Systems](#section-5-4)
  - [5.5. Medical](#section-5-5)
  - [5.6. Scientific Agent](#section-5-6)
- [6. Evaluation and Benchmarks](#section-6)
  - [6.1. Evaluating Evidence and State Management](#section-6-1)
  - [6.2. Evaluating Planning and Execution](#section-6-2)
  - [6.3. Evaluating Feedback and Adaptive Control](#section-6-3)
- [7. Challenges and Outlooks](#section-7)
  - [7.1. Open Challenges](#section-7-1)
  - [7.2. Future Directions](#section-7-2)
- [8. Conclusion](#section-8)
- [A. Additional Related References](#section-A)

## Paper List

<a id="section-1"></a>

## 1. Introduction

References for this framing section are listed under their relevant topics in the catalogue.

<a id="section-2"></a>

## 2. Background

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2023 | MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action | [arXiv](https://arxiv.org/abs/2303.11381) · [Project](https://multimodal-react.github.io/) | [Code](https://github.com/microsoft/MM-REACT) |
| 2023 | ReAct: Synergizing Reasoning and Acting in Language Models | [arXiv](https://arxiv.org/abs/2210.03629) · [Project](https://react-lm.github.io) | [Code](https://github.com/ysymyth/ReAct) |
| 2023 | Reflexion: Language Agents with Verbal Reinforcement Learning | [arXiv](https://arxiv.org/abs/2303.11366) | [Code](https://github.com/noahshinn/reflexion) |
| 2023 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | [arXiv](https://arxiv.org/abs/2307.15818) · [Project](https://robotics-transformer.github.io/) | — |
| 2023 | Segment Anything | [arXiv](https://arxiv.org/abs/2304.02643) · [Project](https://segment-anything.com) | [Code](https://github.com/facebookresearch/segment-anything) |
| 2023 | Toolformer: Language Models Can Teach Themselves to Use Tools | [arXiv](https://arxiv.org/abs/2302.04761) | — |
| 2023 | ViperGPT: Visual Inference via Python Execution for Reasoning | [arXiv](https://arxiv.org/abs/2303.08128) · [Project](https://viper.cs.columbia.edu/) | [Code](https://github.com/cvlab-columbia/viper) |
| 2022 | High-Resolution Image Synthesis with Latent Diffusion Models | [arXiv](https://arxiv.org/abs/2112.10752) | [Code](https://github.com/CompVis/latent-diffusion) |
| 2021 | Learning Transferable Visual Models From Natural Language Supervision | [arXiv](https://arxiv.org/abs/2103.00020) | [Code](https://github.com/OpenAI/CLIP) |
| 1998 | Planning and Acting in Partially Observable Stochastic Domains | [Paper](https://doi.org/10.1016/S0004-3702(98)00023-X) | — |

<a id="section-2-1"></a>

### 2.1. From Visual Models to Vision Agents

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | [arXiv](https://arxiv.org/abs/2603.09877) | [Code](https://github.com/OpenGVLab/InternVL-U) |
| 2025 | Qwen2.5-VL Technical Report | [arXiv](https://arxiv.org/abs/2502.13923) | [Code](https://github.com/QwenLM/Qwen2.5-VL) |
| 2025 | Qwen3-VL Technical Report | [arXiv](https://arxiv.org/abs/2511.21631) | [Code](https://github.com/QwenLM/Qwen3-VL) |
| 2024 | InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks | [arXiv](https://arxiv.org/abs/2312.14238) | [Code](https://github.com/OpenGVLab/InternVL) |
| 2024 | Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution | [arXiv](https://arxiv.org/abs/2409.12191) | [Code](https://github.com/QwenLM/Qwen3-VL) |
| 2023 | Gemini: A Family of Highly Capable Multimodal Models | [arXiv](https://arxiv.org/abs/2312.11805) | — |
| 2023 | Visual Instruction Tuning | [arXiv](https://arxiv.org/abs/2304.08485) · [Project](https://llava-vl.github.io/) | [Code](https://github.com/haotian-liu/LLaVA) |

<a id="section-2-2"></a>

### 2.2. Agent Models, Harnesses, and Environments

References for this framing section are listed under their relevant topics in the catalogue.

<a id="section-2-3"></a>

### 2.3. Runtime Interaction and Capability Evolution

References for this framing section are listed under their relevant topics in the catalogue.

<a id="section-3"></a>

## 3. Vision Agent Harnesses

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Agent harness engineering: A survey | [Paper](https://openreview.net/forum?id=eONq7FdiHa) · [Project](https://github.com/Picrew/awesome-agent-harness) | — |
| 2026 | Agentic Collaborative Cognition for Zero-Shot 3D Understanding | [arXiv](https://arxiv.org/abs/2606.24649) · [Project](https://zhangbo135.github.io/agentic-collaborative-cognition/) | — |
| 2026 | Agentic Jigsaw Interaction Learning for Enhancing Visual Perception and Reasoning in Vision-Language Models | [arXiv](https://arxiv.org/abs/2510.01304) | [Code](https://github.com/yuzeng0-0/AGILE) |
| 2026 | Code World Models for General Game Playing | [arXiv](https://arxiv.org/abs/2510.04542) | — |
| 2026 | CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding | [arXiv](https://arxiv.org/abs/2601.02295) · [Project](https://dannymcy.github.io/cyclevla/) | [Code](https://github.com/dannymcy/cyclevla_code) |
| 2026 | Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight | [arXiv](https://arxiv.org/abs/2509.10723) | — |
| 2026 | DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning | [arXiv](https://arxiv.org/abs/2512.07132) | [Code](https://github.com/nsivaku/dart) |
| 2026 | DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2505.14362) | [Code](https://github.com/Visual-Agent/DeepEyes) |
| 2026 | Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition | [arXiv](https://arxiv.org/abs/2607.06256) | — |
| 2026 | Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains | [arXiv](https://arxiv.org/abs/2606.02357) | — |
| 2026 | Don’t act blindly: Robust gui automation via action-effect verification and self-correction | [Paper](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2026 | ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization | [arXiv](https://arxiv.org/abs/2602.14098) | [Code](https://github.com/youqiwong/ForgeryVCR) |
| 2026 | From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2605.11951) · [Project](https://shengxu.net/AgentChord/) | [Code](https://github.com/EDEM-AI/AgentChord) |
| 2026 | GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents | [arXiv](https://arxiv.org/abs/2505.15810) | [Code](https://github.com/Yuqi-Zhou/GUI-G1) |
| 2026 | GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation | [arXiv](https://arxiv.org/abs/2510.27210) · [Project](https://leon022.github.io/GUI-Rise) | [Code](https://github.com/Leon022/GUI-Rise-code) |
| 2026 | GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning | [arXiv](https://arxiv.org/abs/2505.12493) | — |
| 2026 | Imagine Before You Predict: Interleaved Latent Visual Reasoning for Video Event Prediction | [arXiv](https://arxiv.org/abs/2606.05769) | [Code](https://github.com/OpenGVLab/Future-L1) |
| 2026 | In-Context Robot Learning with VLM Agents | [arXiv](https://arxiv.org/abs/2609.19138) · [Project](https://cheng-haha.github.io/GPT-Policy) | [Code](https://github.com/cheng-haha/GPT-Policy) |
| 2026 | iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception | [arXiv](https://arxiv.org/abs/2512.22009) | — |
| 2026 | Latent Visual Reasoning | [arXiv](https://arxiv.org/abs/2509.24251) | [Code](https://github.com/VincentLeebang/lvr) |
| 2026 | Learning 3D Persistent Embodied World Models | [arXiv](https://arxiv.org/abs/2505.05495) | — |
| 2026 | LongVideoAgent: Multi-Agent Reasoning with Long Videos | [arXiv](https://arxiv.org/abs/2512.20618) · [Project](https://longvideoagent.github.io/) | [Code](https://github.com/longvideoagent/LongVideoAgent) |
| 2026 | Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization | [arXiv](https://arxiv.org/abs/2606.13949) | [Code](https://github.com/yyyyhx/MINIM) |
| 2026 | MolmoWeb: Open Visual Web Agent and Open Data for the Open Web | [arXiv](https://arxiv.org/abs/2604.08516) · [Project](https://allenai.org/blog/molmoweb) | [Code](https://github.com/allenai/molmoweb) |
| 2026 | OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds | [arXiv](https://arxiv.org/abs/2509.02322) | — |
| 2026 | OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models | [arXiv](https://arxiv.org/abs/2512.16295) | [Code](https://github.com/numbmelon/OS-Oracle) |
| 2026 | ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic Video Reinforcement Learning | [arXiv](https://arxiv.org/abs/2605.20342) · [Project](https://evolvinglmms-lab.github.io/ParaVT/) | [Code](https://github.com/EvolvingLMMs-Lab/ParaVT) |
| 2026 | Position: The Systemic Lack of Agency in Visual Reasoning | [arXiv](https://arxiv.org/abs/2606.14795) · [Project](https://haoychen.github.io/Implicit-Reasoning/) | [Code](https://github.com/HaoyChen/Implicit-Reasoning) |
| 2026 | ProRe: A Proactive Reward System for GUI Agents via Reasoner-Actor Collaboration | [arXiv](https://arxiv.org/abs/2509.21823) | [Code](https://github.com/V-Droid-Agent/ProRe) |
| 2026 | Real-Time Execution of Action Chunking Flow Policies | [arXiv](https://arxiv.org/abs/2506.07339) · [Project](https://pi.website/research/real_time_chunking) | [Code](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) |
| 2026 | Real-Time Robot Execution with Masked Action Chunking | [arXiv](https://arxiv.org/abs/2601.20130) · [Project](https://remac-async.github.io/) | [Code](https://github.com/hatchetProject/REMAC) |
| 2026 | Safety Guardrails for LLM-Enabled Robots | [arXiv](https://arxiv.org/abs/2503.07885) · [Project](https://robo-guard.github.io/) | [Code](https://github.com/KumarRobotics/RoboGuard) |
| 2026 | SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning | [arXiv](https://arxiv.org/abs/2503.03480) · [Project](https://pku-safevla.github.io) | [Code](https://github.com/PKU-Alignment/SafeVLA) |
| 2026 | Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning | [arXiv](https://arxiv.org/abs/2602.12405) · [Project](https://sites.google.com/utexas.edu/armor) | — |
| 2026 | Show-Harness: Just a VLM Agent Can Play Robots | [arXiv](https://arxiv.org/abs/2609.10522) · [Project](https://showlab.github.io/Show-Harness) | [Code](https://github.com/showlab/Show-Harness) |
| 2026 | SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning | [arXiv](https://arxiv.org/abs/2506.24119) | [Code](https://github.com/spiral-rl/spiral) |
| 2026 | The Art of Building Verifiers for Computer Use Agents | [arXiv](https://arxiv.org/abs/2604.06240) | [Code](https://github.com/microsoft/fara) |
| 2026 | Training High-Level Schedulers with Execution-Feedback Reinforcement Learning for Long-Horizon GUI Automation | [arXiv](https://arxiv.org/abs/2511.22235) | [Code](https://github.com/hehehahi4/CES) |
| 2026 | Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2512.09706) | [Code](https://github.com/CraftJarvis/OpenHA) |
| 2026 | UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning | [arXiv](https://arxiv.org/abs/2510.20286) | [Code](https://github.com/alibaba/UI-Ins) |
| 2026 | VideoAgent: All-in-One Framework for Video Understanding and Editing | [arXiv](https://arxiv.org/abs/2606.23327) | [Code](https://github.com/HKUDS/VideoAgent) |
| 2025 | A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees | [arXiv](https://arxiv.org/abs/2503.15202) | — |
| 2025 | AgentCPM-GUI: Building Mobile-Use Agents with Reinforcement Fine-Tuning | [arXiv](https://arxiv.org/abs/2506.01391) | [Code](https://github.com/OpenBMB/AgentCPM-GUI) |
| 2025 | Agentic Keyframe Search for Video Question Answering | [arXiv](https://arxiv.org/abs/2503.16032) | [Code](https://github.com/fansunqi/AKeyS) |
| 2025 | AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning | [arXiv](https://arxiv.org/abs/2512.13278) | [Code](https://github.com/Gen-Verse/Open-AgentRL) |
| 2025 | BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation | [arXiv](https://arxiv.org/abs/2410.06237) · [Project](https://robin-lab.cs.utexas.edu/BUMBLE/) | [Code](https://github.com/UT-Austin-RobIn/BUMBLE) |
| 2025 | Core Knowledge Deficits in Multi-Modal Language Models | [arXiv](https://arxiv.org/abs/2410.10855) · [Project](https://williamium3000.github.io/core-knowledge) | [Code](https://github.com/williamium3000/core-knowledge) |
| 2025 | CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation | [arXiv](https://arxiv.org/abs/2501.16609) · [Project](https://oaishi.github.io/cowpilot.html) | [Code](https://github.com/oaishi/CowPilot) |
| 2025 | DWIM: Towards Tool-aware Visual Reasoning via Discrepancy-aware Workflow Generation & Instruct-Masking Tuning | [arXiv](https://arxiv.org/abs/2503.19263) | — |
| 2025 | EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents | [arXiv](https://arxiv.org/abs/2410.22662) | — |
| 2025 | Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning | [arXiv](https://arxiv.org/abs/2505.12370) | [Code](https://github.com/YXB-NKU/SE-GUI) |
| 2025 | FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models | [arXiv](https://arxiv.org/abs/2510.01642) · [Project](https://jimntu.github.io/FailSafe) | — |
| 2025 | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | [arXiv](https://arxiv.org/abs/2503.10639) | [Code](https://github.com/rongyaofang/GoT) |
| 2025 | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | [arXiv](https://arxiv.org/abs/2503.14734) · [Project](https://developer.nvidia.com/isaac/gr00t) | [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 2025 | Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models | [arXiv](https://arxiv.org/abs/2512.01946) · [Project](https://www.di.ens.fr/willow/research/guardian/) | [Code](https://github.com/paulpacaud/Guardian-FailCot) |
| 2025 | GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices | [arXiv](https://arxiv.org/abs/2406.08451) | [Code](https://github.com/OpenGVLab/GUI-Odyssey) |
| 2025 | Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models | [arXiv](https://arxiv.org/abs/2502.19417) · [Project](https://www.pi.website/research/hirobot) | — |
| 2025 | I-FailSense: Towards General Robotic Failure Detection with Vision-Language Models | [arXiv](https://arxiv.org/abs/2509.16072) · [Project](https://clemgris.github.io/I-FailSense/) | [Code](https://github.com/clemgris/I-FailSense) |
| 2025 | LATTE: Learning to Think with Vision Specialists | [arXiv](https://arxiv.org/abs/2412.05479) | — |
| 2025 | Learning Semantic Atomic Skills for Multi-Task Robotic Manipulation | [arXiv](https://arxiv.org/abs/2512.18368) · [Project](https://atom-skill.github.io) | — |
| 2025 | Less is More: Empowering GUI Agent with Context-Aware Simplification | [arXiv](https://arxiv.org/abs/2507.03730) | — |
| 2025 | Magentic-UI: Towards Human-in-the-loop Agentic Systems | [arXiv](https://arxiv.org/abs/2507.22358) | [Code](https://github.com/microsoft/magentic-ui/tree/magentic-ui-0.1) |
| 2025 | Marmot: Object-Level Self-Correction via Multi-Agent Reasoning | [arXiv](https://arxiv.org/abs/2504.20054) | — |
| 2025 | MMSearch-R1: Incentivizing LMMs to Search | [arXiv](https://arxiv.org/abs/2506.20670) | [Code](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) |
| 2025 | OctoTools: An Agentic Framework with Extensible Tools for Complex Reasoning | [arXiv](https://arxiv.org/abs/2502.11271) · [Project](https://octotools.github.io/) | [Code](https://github.com/octotools/octotools) |
| 2025 | OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning | [arXiv](https://arxiv.org/abs/2505.08617) | [Code](https://github.com/zhaochen0110/OpenThinkIMG) |
| 2025 | OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents | [arXiv](https://arxiv.org/abs/2503.16465) | [Code](https://github.com/Wuzheng02/OS-Kairos) |
| 2025 | Ponder & Press: Advancing Visual GUI Agent towards General Computer Control | [arXiv](https://arxiv.org/abs/2412.01268) · [Project](https://invinciblewyq.github.io/ponder-press-page/) | — |
| 2025 | Qwen Look Again: Guiding Vision-Language Reasoning Models to Re-attention Visual Information | [arXiv](https://arxiv.org/abs/2505.23558) | [Code](https://github.com/Liar406/Look_Again) |
| 2025 | RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction | [arXiv](https://arxiv.org/abs/2505.12224) | [Code](https://github.com/MINT-SJTU/RoboFAC) |
| 2025 | RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints | [arXiv](https://arxiv.org/abs/2503.16408) · [Project](https://iranqin.github.io/robofactory/) | [Code](https://github.com/MARS-EAI/RoboFactory) |
| 2025 | RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models | [arXiv](https://arxiv.org/abs/2506.17811) | — |
| 2025 | Robots that Suggest Safe Alternatives | [arXiv](https://arxiv.org/abs/2409.09883) | — |
| 2025 | RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations | [arXiv](https://arxiv.org/abs/2512.24023) | — |
| 2025 | Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers | [arXiv](https://arxiv.org/abs/2506.23918) | [Code](https://github.com/zhaochen0110/Awesome_Think_With_Images) |
| 2025 | Thyme: Think Beyond Images | [arXiv](https://arxiv.org/abs/2508.11630) · [Project](https://thyme-vl.github.io/) | [Code](https://github.com/yfzhang114/Thyme) |
| 2025 | Towards Agentic AI for Multimodal-Guided Video Object Segmentation | [arXiv](https://arxiv.org/abs/2508.10572) | — |
| 2025 | UIPro: Unleashing Superior Interaction Capability For GUI Agents | [arXiv](https://arxiv.org/abs/2509.17328) | [Code](https://github.com/ZJULiHongxin/UIPro) |
| 2025 | Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models | [arXiv](https://arxiv.org/abs/2503.01876) | — |
| 2025 | VideoTree: Adaptive Tree-based Video Representation for LLM Reasoning on Long Videos | [arXiv](https://arxiv.org/abs/2405.19209) · [Project](https://videotree2024.github.io/) | [Code](https://github.com/Ziyang412/VideoTree) |
| 2025 | VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection | [arXiv](https://arxiv.org/abs/2505.20289) | — |
| 2025 | World Model Implanting for Test-time Adaptation of Embodied Agents | [arXiv](https://arxiv.org/abs/2509.03956) | — |
| 2024 | AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation | [arXiv](https://arxiv.org/abs/2410.00371) · [Project](https://aha-vlm.github.io/) | [Code](https://github.com/NVlabs/AHA/tree/main) |
| 2024 | AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents | [arXiv](https://arxiv.org/abs/2401.12963) | — |
| 2024 | Closed-Loop Visuomotor Control with Generative Expectation for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2409.09016) | [Code](https://github.com/OpenDriveLab/CLOVER) |
| 2024 | DetToolChain: A New Prompting Paradigm to Unleash Detection Ability of MLLM | [arXiv](https://arxiv.org/abs/2403.12488) | — |
| 2024 | Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity | [arXiv](https://arxiv.org/abs/2402.06529) · [Project](https://introplan.github.io) | [Code](https://github.com/kevinliang888/IntroPlan) |
| 2024 | MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting | [arXiv](https://arxiv.org/abs/2403.03174) | — |
| 2024 | OK-Robot: What Really Matters in Integrating Open-Knowledge Models for Robotics | [arXiv](https://arxiv.org/abs/2401.12202) · [Project](https://ok-robot.github.io) | [Code](https://github.com/ok-robot/ok-robot) |
| 2024 | ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2409.01652) · [Project](https://rekep-robot.github.io/) | [Code](https://github.com/huangwl18/ReKep) |
| 2024 | Unpacking Failure Modes of Generative Policies: Runtime Monitoring of Consistency and Progress | [arXiv](https://arxiv.org/abs/2410.04640) · [Project](https://sites.google.com/stanford.edu/sentinel) | [Code](https://github.com/agiachris/sentinel) |
| 2024 | VDebugger: Harnessing Execution Feedback for Debugging Visual Programs | [arXiv](https://arxiv.org/abs/2406.13444) | [Code](https://github.com/shirley-wu/vdebugger/) |
| 2024 | Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning | [arXiv](https://arxiv.org/abs/2403.16999) · [Project](https://hao-shao.com/projects/viscot.html) | [Code](https://github.com/deepcs233/Visual-CoT) |
| 2023 | Code as Policies: Language Model Programs for Embodied Control | [arXiv](https://arxiv.org/abs/2209.07753) · [Project](https://code-as-policies.github.io) | [Code](https://github.com/google-research/google-research/tree/master/code_as_policies) |
| 2023 | HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face | [arXiv](https://arxiv.org/abs/2303.17580) | [Code](https://github.com/microsoft/JARVIS) |
| 2023 | Multimodal Chain-of-Thought Reasoning in Language Models | [arXiv](https://arxiv.org/abs/2302.00923) | [Code](https://github.com/amazon-science/mm-cot) |
| 2023 | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | [arXiv](https://arxiv.org/abs/2306.15724) · [Project](https://robot-reflect.github.io/) | [Code](https://github.com/real-stanford/reflect) |
| 2023 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | [arXiv](https://arxiv.org/abs/2307.01928) · [Project](https://robot-help.github.io) | [Code](https://github.com/google-research/google-research/tree/master/language_model_uncertainty) |
| 2023 | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | [arXiv](https://arxiv.org/abs/2307.15818) · [Project](https://robotics-transformer.github.io/) | — |
| 2023 | ViperGPT: Visual Inference via Python Execution for Reasoning | [arXiv](https://arxiv.org/abs/2303.08128) · [Project](https://viper.cs.columbia.edu/) | [Code](https://github.com/cvlab-columbia/viper) |
| 2023 | Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models | [arXiv](https://arxiv.org/abs/2303.04671) | [Code](https://github.com/chenfei-wu/TaskMatrix) |
| 2023 | VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models | [arXiv](https://arxiv.org/abs/2307.05973) · [Project](https://voxposer.github.io) | [Code](https://github.com/huangwl18/VoxPoser) |

<a id="section-3-1"></a>

### 3.1. Active Visual Evidence Acquisition

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2025 | Adaptive Chain-of-Focus Reasoning via Dynamic Visual Search and Zooming for Efficient VLMs | [arXiv](https://arxiv.org/abs/2505.15436) | [Code](https://github.com/xtong-zhang/Chain-of-Focus) |
| 2025 | Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining | [arXiv](https://arxiv.org/abs/2412.10342) | — |
| 2025 | ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use | [arXiv](https://arxiv.org/abs/2504.07981) · [Project](https://gui-agent.github.io/grounding-leaderboard) | [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| 2025 | VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT | [arXiv](https://arxiv.org/abs/2504.04471) | — |

<a id="section-3-1-1"></a>

#### 3.1.1. View-Centric Acquisition

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | BVS: Bayesian Visual Search with Multimodal Large Language Model for Fine-grained Perception | [arXiv](https://arxiv.org/abs/2607.03184) | [Code](https://github.com/PKU-ICST-MIPL/BVS_ICML2026) |
| 2026 | DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking | [arXiv](https://arxiv.org/abs/2507.20879) | [Code](https://github.com/wczheng/DriveAgent-R1) |
| 2025 | DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding | [arXiv](https://arxiv.org/abs/2504.14920) | [Code](https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025) |
| 2025 | Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception | [arXiv](https://arxiv.org/abs/2511.15279) | — |

<a id="section-3-1-2"></a>

#### 3.1.2. Target-Centric Acquisition

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | AutoFocus: Uncertainty-Aware Active Visual Search for GUI Grounding | [arXiv](https://arxiv.org/abs/2605.02630) | [Code](https://github.com/Mr-Bigworth/AutoFocus) |
| 2026 | GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents | [arXiv](https://arxiv.org/abs/2506.03143) | [Code](https://github.com/microsoft/GUI-Actor) |
| 2026 | PrecisionCUA: Iterative Visual Refinement for Pixel-Precise Cursor Grounding in Code Editors | [arXiv](https://arxiv.org/abs/2604.13019) | [Code](https://github.com/microsoft/precision-cua-bench/tree/main) |
| 2025 | Visual Test-time Scaling for GUI Agent Grounding | [arXiv](https://arxiv.org/abs/2505.00684) | [Code](https://github.com/tiangeluo/RegionFocus) |

<a id="section-3-1-3"></a>

#### 3.1.3. Time-Centric Acquisition

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning | [arXiv](https://arxiv.org/abs/2603.14052) | [Code](https://github.com/git-disl/A4VL) |
| 2026 | VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning | [arXiv](https://arxiv.org/abs/2503.13444) · [Project](https://videomind.github.io/) | [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | VideoZoomer: Reinforcement-Learned Temporal Focusing for Long Video Reasoning | [arXiv](https://arxiv.org/abs/2512.22315) | [Code](https://github.com/zsgvivo/VideoZoomer) |
| 2025 | VideoExplorer: Think With Videos For Agentic Long-Video Understanding | [arXiv](https://arxiv.org/abs/2506.10821) | [Code](https://github.com/RUC-NLPIR/VideoDeepResearch) |

<a id="section-3-2"></a>

### 3.2. Visual Memory and State Management

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Experience Transfer for Multimodal LLM Agents in Minecraft Game | [arXiv](https://arxiv.org/abs/2604.05533) | — |
| 2026 | Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory | [arXiv](https://arxiv.org/abs/2607.05511) · [Project](https://clare-nie.github.io/Light-Omni) | [Code](https://github.com/Clare-Nie/Light-Omni) |
| 2026 | MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents | [arXiv](https://arxiv.org/abs/2601.20831) | — |
| 2026 | VideoARM: Agentic Reasoning over Hierarchical Memory for Long-Form Video Understanding | [arXiv](https://arxiv.org/abs/2512.12360) · [Project](https://milvlg.github.io/videoarm/) | [Code](https://github.com/MILVLG/videoarm) |
| 2026 | When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents | [arXiv](https://arxiv.org/abs/2608.29897) | — |

<a id="section-3-2-1"></a>

#### 3.2.1. Evidence-Based Visual Memory

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Bridging Modalities, Spanning Time: Structured Memory for Ultra-Long Agentic Video Reasoning | [arXiv](https://arxiv.org/abs/2605.08271) | [Code](https://github.com/lijiazheng0917/MAGIC-video) |
| 2026 | Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding | [arXiv](https://arxiv.org/abs/2608.07663) · [Project](https://choi-yeeun.github.io/MERIT/) | [Code](https://github.com/choi-yeeun/MERIT) |
| 2026 | Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory | [arXiv](https://arxiv.org/abs/2508.09736) | [Code](https://github.com/bytedance-seed/m3-agent) |
| 2026 | Visual Agentic Memory: Enabling Online Long Video Understanding via Online Indexing, Hierarchical Memory, and Agentic Retrieval | [arXiv](https://arxiv.org/abs/2605.16481) | [Code](https://github.com/yiliu-li/Visual-Agentic-Memory) |
| 2026 | WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning | [arXiv](https://arxiv.org/abs/2512.02425) · [Project](https://worldmm.github.io) | [Code](https://github.com/wgcyeo/WorldMM) |
| 2024 | VideoAgent: A Memory-augmented Multimodal Agent for Video Understanding | [arXiv](https://arxiv.org/abs/2403.11481) · [Project](http://videoagent.github.io) | [Code](https://github.com/YueFan1014/VideoAgent) |

<a id="section-3-2-2"></a>

#### 3.2.2. State-Based Visual Memory

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Planning with an Embodied Learnable Memory | [Paper](https://openreview.net/forum?id=79BOATBal9) | — |
| 2026 | ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding | [arXiv](https://arxiv.org/abs/2607.28678) | — |
| 2025 | Embodied VideoAgent: Persistent Memory from Egocentric Videos and Embodied Sensors Enables Dynamic Scene Understanding | [arXiv](https://arxiv.org/abs/2501.00358) · [Project](https://embodied-videoagent.github.io/) | [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |
| 2025 | RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems | [arXiv](https://arxiv.org/abs/2508.01415) | — |

<a id="section-3-2-3"></a>

#### 3.2.3. Experience-Based Visual Memory

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration | [arXiv](https://arxiv.org/abs/2512.19396) | — |
| 2026 | MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents | [arXiv](https://arxiv.org/abs/2605.18652) | — |

<a id="section-3-3"></a>

### 3.3. Evidence-Grounded Reasoning and Planning

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Agentic Retoucher for Text-To-Image Generation | [arXiv](https://arxiv.org/abs/2601.02046) | — |
| 2026 | AgentVLN: Towards Agentic Vision-and-Language Navigation | [arXiv](https://arxiv.org/abs/2603.17670) | [Code](https://github.com/Allenxinn/AgentVLN) |
| 2026 | CoAct-1: Computer-using Multi-Agent System with Coding Actions | [arXiv](https://arxiv.org/abs/2508.03923) | [Code](https://github.com/SalesforceAIResearch/CoAct-1) |
| 2026 | DeepEyesV2: Toward Agentic Multimodal Model | [arXiv](https://arxiv.org/abs/2511.05271) · [Project](https://visual-agent.github.io/) | [Code](https://github.com/Visual-Agent/DeepEyesV2) |
| 2026 | ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition | [arXiv](https://arxiv.org/abs/2607.25565) | — |
| 2026 | VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | [arXiv](https://arxiv.org/abs/2510.16907) · [Project](https://vagen-ai.github.io) | [Code](https://github.com/mll-lab-nu/VAGEN) |
| 2026 | VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning | [arXiv](https://arxiv.org/abs/2503.13444) · [Project](https://videomind.github.io/) | [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | Visual Planning: Let's Think Only with Images | [arXiv](https://arxiv.org/abs/2505.11409) | [Code](https://github.com/yix8/VisualPlanning) |
| 2025 | Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents | [arXiv](https://arxiv.org/abs/2504.00906) | [Code](https://github.com/simular-ai/Agent-S) |
| 2025 | GAM-Agent: Game-Theoretic and Uncertainty-Aware Collaboration for Complex Visual Reasoning | [arXiv](https://arxiv.org/abs/2505.23399) | [Code](https://github.com/jushengzhang/Gam-Agent) |
| 2025 | RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation | [arXiv](https://arxiv.org/abs/2509.08820) · [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) | — |

<a id="section-3-3-1"></a>

#### 3.3.1. Observation-Grounded Reasoning and Evidence Acquisition

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | AdaReasoner: Dynamic Tool Orchestration for Iterative Visual Reasoning | [arXiv](https://arxiv.org/abs/2601.18631) | [Code](https://github.com/ssmisya/AdaReasoner) |
| 2026 | CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization | [arXiv](https://arxiv.org/abs/2511.19661) | [Code](https://github.com/RenlyH/CodeV) |
| 2026 | GTA1: GUI Test-time Scaling Agent | [arXiv](https://arxiv.org/abs/2507.05791) | [Code](https://github.com/Yan98/GTA1) |
| 2026 | InSight-o3: Empowering Multimodal Foundation Models with Generalized Visual Search | [arXiv](https://arxiv.org/abs/2512.18745) | [Code](https://github.com/m-Just/InSight-o3) |
| 2026 | IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents | [arXiv](https://arxiv.org/abs/2604.05157) | — |
| 2025 | PyVision: Agentic Vision with Dynamic Tooling | [arXiv](https://arxiv.org/abs/2507.07998) | [Code](https://github.com/agents-x-project/PyVision) |

<a id="section-3-3-2"></a>

#### 3.3.2. Simulation-Grounded Planning and Lookahead

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement | [arXiv](https://arxiv.org/abs/2602.14968) | — |
| 2026 | R-WoM: Retrieval-augmented World Model For Computer-use Agents | [arXiv](https://arxiv.org/abs/2510.11892) · [Paper](https://doi.org/10.48550/arxiv.2510.11892) | — |
| 2025 | Planning with Reasoning using Vision Language World Model | [arXiv](https://arxiv.org/abs/2509.02722) | — |
| 2025 | STORM: Search-Guided Generative World Models for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2512.18477) | — |

<a id="section-3-3-3"></a>

#### 3.3.3. Execution-Grounded Search and Plan Repair

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents | [arXiv](https://arxiv.org/abs/2602.02995) | — |
| 2026 | OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent | [arXiv](https://arxiv.org/abs/2601.07779) | [Code](https://github.com/OS-Copilot/OS-Symphony) |
| 2026 | WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level Feedback and Step-Level Reinforcement Learning | [arXiv](https://arxiv.org/abs/2509.22644) | [Code](https://github.com/mnluzimu/WebGen-Agent) |
| 2025 | LERa: Replanning with Visual Feedback in Instruction Following | [arXiv](https://arxiv.org/abs/2507.05135) · [Project](https://lera-robo.github.io) | [Code](https://github.com/AmpiroMax/LERa?tab=readme-ov-file#-custom-tasks) |
| 2025 | MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation | [arXiv](https://arxiv.org/abs/2507.16853) | [Code](https://github.com/MadeAgents/mobile-use) |
| 2025 | Scaling Agents for Computer Use | [arXiv](https://arxiv.org/abs/2510.02250) | — |
| 2025 | ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning | [arXiv](https://arxiv.org/abs/2509.24219) | — |

<a id="section-4"></a>

## 4. Capability Acquisition and Evolution in Vision Agents

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents | [arXiv](https://arxiv.org/abs/2603.24018) | — |
| 2026 | EvoVLA: Self-Evolving Vision-Language-Action Model | [arXiv](https://arxiv.org/abs/2511.16166) · [Project](https://aigeeksgroup.github.io/EvoVLA) | [Code](https://github.com/AIGeeksGroup/EvoVLA) |
| 2026 | Pixel Reasoner: Incentivizing Pixel-Space Reasoning with Curiosity-Driven Reinforcement Learning | [arXiv](https://arxiv.org/abs/2505.15966) · [Project](https://tiger-ai-lab.github.io/Pixel-Reasoner/) | [Code](https://github.com/TIGER-AI-Lab/Pixel-Reasoner) |
| 2026 | Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks | [arXiv](https://arxiv.org/abs/2606.27147) | — |
| 2026 | Self-Improvements in Modern Agentic Systems: A Survey | [arXiv](https://arxiv.org/abs/2607.13104) · [Project](https://selfimproving-agent.github.io/) | [Code](https://github.com/selfimproving-agent/awesome-Self-Improving-Agents) |
| 2026 | Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning | [arXiv](https://arxiv.org/abs/2602.08167) | — |
| 2026 | Sherlock: Self-Correcting Reasoning in Vision-Language Models | [arXiv](https://arxiv.org/abs/2505.22651) | — |
| 2026 | SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing | [arXiv](https://arxiv.org/abs/2604.14399) | [Code](https://github.com/wuaodi/SpaceMind) |
| 2026 | Video-STAR: Reinforcing Open-Vocabulary Action Recognition with Tools | [arXiv](https://arxiv.org/abs/2510.08480) | — |
| 2026 | When Models Judge Themselves: Unsupervised Self-Evolution for Multimodal Reasoning | [arXiv](https://arxiv.org/abs/2603.21289) | [Code](https://github.com/OPPO-Mente-Lab/LLM-Self-Judge) |
| 2025 | AFlow: Automating Agentic Workflow Generation | [arXiv](https://arxiv.org/abs/2410.10762) | [Code](https://github.com/FoundationAgents/AFlow) |
| 2025 | G\"odel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement | [arXiv](https://arxiv.org/abs/2410.04444) | [Code](https://github.com/Arvid-pku/Godel_Agent) |
| 2025 | Self-Improvement in Multimodal Large Language Models: A Survey | [arXiv](https://arxiv.org/abs/2510.02665) | — |
| 2024 | Efficient Self-Improvement in Multimodal Large Language Models: A Model-Level Judge-Free Approach | [arXiv](https://arxiv.org/abs/2411.17760) | — |

<a id="section-4-1"></a>

### 4.1. From Capability Acquisition to Self-Evolution

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | ActiveScope: Actively Seeking and Correcting Perception for MLLMs | [arXiv](https://arxiv.org/abs/2606.24292) | [Code](https://github.com/jasmine-ww/ActiveScope) |
| 2026 | Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation | [arXiv](https://arxiv.org/abs/2603.16664) | — |
| 2026 | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | [arXiv](https://arxiv.org/abs/2607.07663) · [Project](https://github.com/deepgrounding/recursive-self-improvement) | — |
| 2026 | The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement | [arXiv](https://arxiv.org/abs/2609.11873) · [Project](https://github.com/theseus-labs-rsi/awesome-rsi) | — |
| 2026 | UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2602.05832) · [Project](https://ui-mem.github.io) | — |
| 2026 | VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use | [arXiv](https://arxiv.org/abs/2505.19255) | [Code](https://github.com/VTOOL-R1/vtool-r1) |
| 2025 | A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence | [arXiv](https://arxiv.org/abs/2507.21046) · [Project](https://github.com/CharlesQ9/Self-Evolving-Agents) | — |
| 2025 | AppAgent: Multimodal Agents as Smartphone Users | [arXiv](https://arxiv.org/abs/2312.13771) · [Project](https://appagent-official.github.io/) | [Code](https://github.com/TencentQQGYLab/AppAgent) |
| 2025 | Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement | [arXiv](https://arxiv.org/abs/2405.15973) | — |
| 2025 | Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks | [arXiv](https://arxiv.org/abs/2501.11733) · [Project](https://x-plug.github.io/MobileAgent) | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2025 | RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback | [arXiv](https://arxiv.org/abs/2505.19767) | — |
| 2025 | The Landscape of Agentic Reinforcement Learning for LLMs: A Survey | [arXiv](https://arxiv.org/abs/2509.02547) | — |
| 2025 | Vision-Language Models Can Self-Improve Reasoning via Reflection | [arXiv](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2025 | Visual-RFT: Visual Reinforcement Fine-Tuning | [arXiv](https://arxiv.org/abs/2503.01785) | [Code](https://github.com/Liuziyu77/Visual-RFT) |

<a id="section-4-2"></a>

### 4.2. Targets of Self-Evolution

<a id="section-4-2-1"></a>

#### 4.2.1. Visual Memory and Knowledge

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval | [arXiv](https://arxiv.org/abs/2607.12764) | — |
| 2026 | Hybrid Self-evolving Structured Memory for GUI Agents | [arXiv](https://arxiv.org/abs/2603.10291) | [Code](https://github.com/NickSiboZhu/HyMEM-GUI-Agent) |
| 2026 | META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) | — |
| 2026 | Planning with the Views | [arXiv](https://arxiv.org/abs/2605.29563) · [Project](https://viewsuite.github.io) | [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2026 | UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2602.05832) · [Project](https://ui-mem.github.io) | — |
| 2026 | VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following | [arXiv](https://arxiv.org/abs/2608.26013) | — |
| 2025 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | [arXiv](https://arxiv.org/abs/2511.21678) · [Project](https://weihao-bo.github.io/ViLoMeo-page) | [Code](https://github.com/weihao-bo/ViLoMem) |
| 2025 | AppAgent: Multimodal Agents as Smartphone Users | [arXiv](https://arxiv.org/abs/2312.13771) · [Project](https://appagent-official.github.io/) | [Code](https://github.com/TencentQQGYLab/AppAgent) |
| 2025 | MemVerse: Multimodal Memory for Lifelong Learning Agents | [arXiv](https://arxiv.org/abs/2512.03627) | [Code](https://github.com/KnowledgeXLab/MemVerse) |
| 2025 | Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks | [arXiv](https://arxiv.org/abs/2501.11733) · [Project](https://x-plug.github.io/MobileAgent) | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2025 | SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models | [arXiv](https://arxiv.org/abs/2507.13152) | — |
| 2025 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | [arXiv](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |

<a id="section-4-2-2"></a>

#### 4.2.2. Tools and Skills

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) | — |
| 2026 | MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand | [arXiv](https://arxiv.org/abs/2606.01801) | — |
| 2026 | Skill-Guided Continuation Distillation for GUI Agents | [arXiv](https://arxiv.org/abs/2606.18890) | — |
| 2026 | VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use | [arXiv](https://arxiv.org/abs/2505.19255) | [Code](https://github.com/VTOOL-R1/vtool-r1) |
| 2025 | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning | [arXiv](https://arxiv.org/abs/2511.19900) | [Code](https://github.com/aiming-lab/Agent0) |
| 2025 | AppAgent: Multimodal Agents as Smartphone Users | [arXiv](https://arxiv.org/abs/2312.13771) · [Project](https://appagent-official.github.io/) | [Code](https://github.com/TencentQQGYLab/AppAgent) |
| 2025 | Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks | [arXiv](https://arxiv.org/abs/2501.11733) · [Project](https://x-plug.github.io/MobileAgent) | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2024 | Cradle: Empowering Foundation Agents Towards General Computer Control | [arXiv](https://arxiv.org/abs/2403.03186) | [Code](https://github.com/BAAI-Agents/Cradle) |
| 1999 | Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning | [Paper](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | — |

<a id="section-4-2-3"></a>

#### 4.2.3. Harness and Workflow

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Clarify Before Executing: A Self-Evolving Agent for Resolving Intent Asymmetry in 3D Tool Orchestration | [arXiv](https://arxiv.org/abs/2607.16352) | [Code](https://github.com/xyzhu1225/CLARE) |
| 2026 | COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows | [arXiv](https://arxiv.org/abs/2607.01709) | [Code](https://github.com/Moms-Organic-Agent-Lab/comfyclaw) |
| 2026 | HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems | [arXiv](https://arxiv.org/abs/2606.01779) | [Code](https://github.com/mingju-c/HarnessForge) |
| 2026 | HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry | [arXiv](https://arxiv.org/abs/2606.14249) · [Project](https://darwin-agent.github.io/HarnessX/) | [Code](https://github.com/Darwin-Agent/HarnessX) |
| 2026 | MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding | [arXiv](https://arxiv.org/abs/2608.04587) | [Code](https://github.com/Alibaba-VELLDEPTH/MetaVideoAgent) |
| 2026 | Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory | [arXiv](https://arxiv.org/abs/2604.01007) | [Code](https://github.com/aiming-lab/SimpleMem) |
| 2026 | Self-Harness: Harnesses That Improve Themselves | [arXiv](https://arxiv.org/abs/2606.09498) | [Code](https://github.com/qzzqzzb/Self-Harness) |
| 2026 | SIA: Self Improving AI with Harness & Weight Updates | [arXiv](https://arxiv.org/abs/2605.27276) | — |
| 2026 | VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models | [arXiv](https://arxiv.org/abs/2608.24302) | [Code](https://github.com/Tencent/VideoHarness-RSI) |
| 2025 | Automated Design of Agentic Systems | [arXiv](https://arxiv.org/abs/2408.08435) · [Project](https://shengranhu.com/ADAS) | [Code](https://github.com/ShengranHu/ADAS) |
| 2024 | AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning | [arXiv](https://arxiv.org/abs/2406.11200) | [Code](https://github.com/zou-group/avatar) |

<a id="section-4-2-4"></a>

#### 4.2.4. Models and Policies

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards | [arXiv](https://arxiv.org/abs/2606.27376) | [Code](https://github.com/mbzuai-oryx/Ask-Solve-Generate) |
| 2026 | AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models | [arXiv](https://arxiv.org/abs/2603.08519) | — |
| 2026 | GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation | [arXiv](https://arxiv.org/abs/2605.21605) · [Project](https://ephemeral182.github.io/GenEvolve/) | [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2026 | Planning with the Views | [arXiv](https://arxiv.org/abs/2605.29563) · [Project](https://viewsuite.github.io) | [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2026 | Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding | [arXiv](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | RISE: Self-Improving Robot Policy with Compositional World Model | [arXiv](https://arxiv.org/abs/2602.11075) · [Project](https://opendrivelab.com/RISE/) | [Code](https://github.com/OpenDriveLab/RISE) |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | SIA: Self Improving AI with Harness & Weight Updates | [arXiv](https://arxiv.org/abs/2605.27276) | — |
| 2026 | Skill-Guided Continuation Distillation for GUI Agents | [arXiv](https://arxiv.org/abs/2606.18890) | — |
| 2026 | Vision-sr1: Self-rewarding vision-language model via reasoning decomposition and multi-reward policy optimization | [arXiv](https://arxiv.org/abs/2508.19652) | [Code](https://github.com/zli12321/Vision-SR1) |
| 2026 | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model | [arXiv](https://arxiv.org/abs/2602.12063) · [Project](https://sites.google.com/view/vla-w) | — |
| 2025 | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning | [arXiv](https://arxiv.org/abs/2511.19900) | [Code](https://github.com/aiming-lab/Agent0) |
| 2025 | Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement | [arXiv](https://arxiv.org/abs/2405.15973) | — |
| 2025 | EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards | [arXiv](https://arxiv.org/abs/2511.16672) | [Code](https://github.com/mbzuai-oryx/EvoLMM) |
| 2025 | Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning | [arXiv](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2025 | MemVerse: Multimodal Memory for Lifelong Learning Agents | [arXiv](https://arxiv.org/abs/2512.03627) | [Code](https://github.com/KnowledgeXLab/MemVerse) |
| 2025 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | [arXiv](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |
| 2025 | Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision | [arXiv](https://arxiv.org/abs/2407.06189) · [Project](https://orrzohar.github.io/projects/video-star/) | — |
| 2025 | Vision-Language Models Can Self-Improve Reasoning via Reflection | [arXiv](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2025 | VisPlay: Self-Evolving Vision-Language Models from Images | [arXiv](https://arxiv.org/abs/2511.15661) · [Project](https://bruno686.github.io/VisPlay/) | [Code](https://github.com/bruno686/VisPlay) |
| 2025 | World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training | [arXiv](https://arxiv.org/abs/2509.24948) | [Code](https://github.com/amap-cvlab/world-env) |
| 2024 | Calibrated Self-Rewarding Vision Language Models | [arXiv](https://arxiv.org/abs/2405.14622) | [Code](https://github.com/YiyangZhou/CSR) |
| 2024 | RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2412.09858) · [Project](https://generalist-distillation.github.io) | — |
| 2023 | RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2306.11706) | — |

<a id="section-4-2-5"></a>

#### 4.2.5. Learning Substrate

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning | [arXiv](https://arxiv.org/abs/2604.09815) | — |
| 2026 | Planning with the Views | [arXiv](https://arxiv.org/abs/2605.29563) · [Project](https://viewsuite.github.io) | [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2026 | ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images | [arXiv](https://arxiv.org/abs/2511.21606) | — |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | Skill-Guided Continuation Distillation for GUI Agents | [arXiv](https://arxiv.org/abs/2606.18890) | — |
| 2026 | VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following | [arXiv](https://arxiv.org/abs/2608.26013) | — |
| 2025 | Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement | [arXiv](https://arxiv.org/abs/2405.15973) | — |
| 2025 | EvoLMM: Self-Evolving Large Multimodal Models with Continuous Rewards | [arXiv](https://arxiv.org/abs/2511.16672) | [Code](https://github.com/mbzuai-oryx/EvoLMM) |
| 2025 | Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning | [arXiv](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2025 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | [arXiv](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |
| 2025 | Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision | [arXiv](https://arxiv.org/abs/2407.06189) · [Project](https://orrzohar.github.io/projects/video-star/) | — |
| 2025 | Vision-Language Models Can Self-Improve Reasoning via Reflection | [arXiv](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2025 | VisPlay: Self-Evolving Vision-Language Models from Images | [arXiv](https://arxiv.org/abs/2511.15661) · [Project](https://bruno686.github.io/VisPlay/) | [Code](https://github.com/bruno686/VisPlay) |
| 2023 | RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2306.11706) | — |
| 2011 | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | [arXiv](https://arxiv.org/abs/1011.0686) · [Paper](https://proceedings.mlr.press/v15/ross11a.html) | — |
| 2009 | Curriculum learning | [Paper](https://icml.cc/2009/papers/119.pdf) | — |

<a id="section-4-3"></a>

### 4.3. Mechanisms and Timescales of Evolution

<a id="section-4-3-1"></a>

#### 4.3.1. Feedback Sources

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation | [arXiv](https://arxiv.org/abs/2603.16664) | — |
| 2026 | Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding | [arXiv](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | RISE: Self-Improving Robot Policy with Compositional World Model | [arXiv](https://arxiv.org/abs/2602.11075) · [Project](https://opendrivelab.com/RISE/) | [Code](https://github.com/OpenDriveLab/RISE) |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | Vision-sr1: Self-rewarding vision-language model via reasoning decomposition and multi-reward policy optimization | [arXiv](https://arxiv.org/abs/2508.19652) | [Code](https://github.com/zli12321/Vision-SR1) |
| 2026 | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model | [arXiv](https://arxiv.org/abs/2602.12063) · [Project](https://sites.google.com/view/vla-w) | — |
| 2025 | Agent0-VL: Exploring Self-Evolving Agent for Tool-Integrated Vision-Language Reasoning | [arXiv](https://arxiv.org/abs/2511.19900) | [Code](https://github.com/aiming-lab/Agent0) |
| 2025 | LLaVA-Critic: Learning to Evaluate Multimodal Models | [arXiv](https://arxiv.org/abs/2410.02712) · [Project](https://llava-vl.github.io/blog/2024-10-03-llava-critic) | [Code](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| 2025 | RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback | [arXiv](https://arxiv.org/abs/2505.19767) | — |
| 2025 | RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness | [arXiv](https://arxiv.org/abs/2405.17220) | [Code](https://github.com/RLHF-V/RLAIF-V) |
| 2025 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | [arXiv](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |
| 2024 | Calibrated Self-Rewarding Vision Language Models | [arXiv](https://arxiv.org/abs/2405.14622) | [Code](https://github.com/YiyangZhou/CSR) |

<a id="section-4-3-2"></a>

#### 4.3.2. Update Operators

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning | [arXiv](https://arxiv.org/abs/2604.09815) | — |
| 2026 | EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval | [arXiv](https://arxiv.org/abs/2607.12764) | — |
| 2026 | GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation | [arXiv](https://arxiv.org/abs/2605.21605) · [Project](https://ephemeral182.github.io/GenEvolve/) | [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2026 | MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand | [arXiv](https://arxiv.org/abs/2606.01801) | — |
| 2026 | Planning with the Views | [arXiv](https://arxiv.org/abs/2605.29563) · [Project](https://viewsuite.github.io) | [Code](https://github.com/mll-lab-nu/ViewAgent) |
| 2026 | Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation | [arXiv](https://arxiv.org/abs/2605.28230) | — |
| 2026 | Self-Correcting VLA: Online Action Refinement via Sparse World Imagination | [arXiv](https://arxiv.org/abs/2602.21633) | [Code](https://github.com/Kisaragi0/SC-VLA) |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | Skill-Guided Continuation Distillation for GUI Agents | [arXiv](https://arxiv.org/abs/2606.18890) | — |
| 2026 | UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2602.05832) · [Project](https://ui-mem.github.io) | — |
| 2026 | VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models | [arXiv](https://arxiv.org/abs/2608.24302) | [Code](https://github.com/Tencent/VideoHarness-RSI) |
| 2026 | VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following | [arXiv](https://arxiv.org/abs/2608.26013) | — |
| 2026 | VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model | [arXiv](https://arxiv.org/abs/2602.12063) · [Project](https://sites.google.com/view/vla-w) | — |
| 2025 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | [arXiv](https://arxiv.org/abs/2511.21678) · [Project](https://weihao-bo.github.io/ViLoMeo-page) | [Code](https://github.com/weihao-bo/ViLoMem) |
| 2025 | Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement | [arXiv](https://arxiv.org/abs/2405.15973) | — |
| 2025 | Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning | [arXiv](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2025 | MemVerse: Multimodal Memory for Lifelong Learning Agents | [arXiv](https://arxiv.org/abs/2512.03627) | [Code](https://github.com/KnowledgeXLab/MemVerse) |
| 2025 | SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from Experience | [arXiv](https://arxiv.org/abs/2508.04700) | [Code](https://github.com/SunzeY/SEAgent) |
| 2025 | Vision-Language Models Can Self-Improve Reasoning via Reflection | [arXiv](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2025 | Visual-RFT: Visual Reinforcement Fine-Tuning | [arXiv](https://arxiv.org/abs/2503.01785) | [Code](https://github.com/Liuziyu77/Visual-RFT) |
| 2024 | RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2412.09858) · [Project](https://generalist-distillation.github.io) | — |
| 2016 | Policy Distillation | [arXiv](https://arxiv.org/abs/1511.06295) | — |

<a id="section-4-3-3"></a>

#### 4.3.3. Adaptation Timescales

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | ActiveScope: Actively Seeking and Correcting Perception for MLLMs | [arXiv](https://arxiv.org/abs/2606.24292) | [Code](https://github.com/jasmine-ww/ActiveScope) |
| 2026 | EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval | [arXiv](https://arxiv.org/abs/2607.12764) | — |
| 2026 | Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation | [arXiv](https://arxiv.org/abs/2603.16664) | — |
| 2026 | Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents | [arXiv](https://arxiv.org/abs/2601.03515) | [Code](https://github.com/YuanchenBei/Mem-Gallery) |
| 2026 | Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation | [arXiv](https://arxiv.org/abs/2605.28230) | — |
| 2026 | SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment | [arXiv](https://arxiv.org/abs/2604.08988) | — |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2602.05832) · [Project](https://ui-mem.github.io) | — |
| 2026 | WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction | [arXiv](https://arxiv.org/abs/2605.29341) | [Code](https://github.com/UCSB-AI/WorldMemArena) |
| 2025 | Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning | [arXiv](https://arxiv.org/abs/2507.08224) | [Code](https://github.com/chan0park/SelfReVision) |
| 2025 | Mobile-Agent-E: Self-Evolving Mobile Assistant for Complex Tasks | [arXiv](https://arxiv.org/abs/2501.11733) · [Project](https://x-plug.github.io/MobileAgent) | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2025 | SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models | [arXiv](https://arxiv.org/abs/2507.13152) | — |
| 2023 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | [arXiv](https://arxiv.org/abs/2306.03310) · [Project](https://libero-project.github.io) | — |
| 2019 | Continual Lifelong Learning with Neural Networks: A Review | [arXiv](https://arxiv.org/abs/1802.07569) | — |

<a id="section-4-4"></a>

### 4.4. Toward Recursive Self-Improvement

<a id="section-4-4-1"></a>

#### 4.4.1. Bounded Closed-loop Self-Improvement

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory | [arXiv](https://arxiv.org/abs/2604.01007) | [Code](https://github.com/aiming-lab/SimpleMem) |
| 2026 | Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | [arXiv](https://arxiv.org/abs/2511.00091) | — |
| 2026 | VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models | [arXiv](https://arxiv.org/abs/2608.24302) | [Code](https://github.com/Tencent/VideoHarness-RSI) |
| 2025 | Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement | [arXiv](https://arxiv.org/abs/2405.15973) | — |
| 2025 | Vision-Language Models Can Self-Improve Reasoning via Reflection | [arXiv](https://arxiv.org/abs/2411.00855) | [Code](https://github.com/njucckevin/MM-Self-Improve) |
| 2025 | Visual-RFT: Visual Reinforcement Fine-Tuning | [arXiv](https://arxiv.org/abs/2503.01785) | [Code](https://github.com/Liuziyu77/Visual-RFT) |

<a id="section-4-4-2"></a>

#### 4.4.2. Recursive Meta-Improvement

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Darwin Gödel machine: open-ended evolution of self-improving agents | [arXiv](https://arxiv.org/abs/2505.22954) | [Code](https://github.com/jennyzzt/dgm) |
| 2026 | Dream-RSI: Recursive Self-Improvement through Evolving Worlds | [arXiv](https://arxiv.org/abs/2609.14858) · [Project](https://github.com/zhengkid/Dream-RSI) | — |
| 2026 | Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | [arXiv](https://arxiv.org/abs/2607.07663) · [Project](https://github.com/deepgrounding/recursive-self-improvement) | — |
| 2026 | SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness | [arXiv](https://arxiv.org/abs/2609.20519) · [Project](https://nvlabs.github.io/SoL-Pi/) | [Code](https://github.com/NVlabs/SoL-Pi) |
| 2026 | The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement | [arXiv](https://arxiv.org/abs/2609.11873) · [Project](https://github.com/theseus-labs-rsi/awesome-rsi) | — |

<a id="section-4-5"></a>

### 4.5. Challenges in Capability Evolution

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Mem-Gallery: Benchmarking Multimodal Long-Term Conversational Memory for MLLM Agents | [arXiv](https://arxiv.org/abs/2601.03515) | [Code](https://github.com/YuanchenBei/Mem-Gallery) |
| 2026 | Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding | [arXiv](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | The Essence of Balance for Self-Improving Agents in Vision-and-Language Navigation | [arXiv](https://arxiv.org/abs/2604.19064) | — |
| 2026 | WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction | [arXiv](https://arxiv.org/abs/2605.29341) | [Code](https://github.com/UCSB-AI/WorldMemArena) |
| 2024 | Calibrated Self-Rewarding Vision Language Models | [arXiv](https://arxiv.org/abs/2405.14622) | [Code](https://github.com/YiyangZhou/CSR) |
| 2024 | Diving into Self-Evolving Training for Multimodal Reasoning | [arXiv](https://arxiv.org/abs/2412.17451) · [Project](https://mstar-lmm.github.io) | [Code](https://github.com/hkust-nlp/mstar) |
| 2023 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | [arXiv](https://arxiv.org/abs/2306.03310) · [Project](https://libero-project.github.io) | — |
| 2019 | Continual Lifelong Learning with Neural Networks: A Review | [arXiv](https://arxiv.org/abs/1802.07569) | — |

<a id="section-5"></a>

## 5. Applications of Vision Agents

<a id="section-5-1"></a>

### 5.1. Visual Understanding and Reasoning

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | DeepEyesV2: Toward Agentic Multimodal Model | [arXiv](https://arxiv.org/abs/2511.05271) · [Project](https://visual-agent.github.io/) | [Code](https://github.com/Visual-Agent/DeepEyesV2) |
| 2026 | Design Choices That Matter: A Functional ANOVA Analysis for Remote Sensing Multi-Label Classification | [arXiv](https://arxiv.org/abs/2608.04702) | — |
| 2026 | DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization | [arXiv](https://arxiv.org/abs/2607.24856) | — |
| 2026 | EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use | [arXiv](https://arxiv.org/abs/2602.15329) | [Code](https://github.com/lingcco/EventMemAgent) |
| 2026 | Geometrically-Constrained Agent for Spatial Reasoning | [arXiv](https://arxiv.org/abs/2511.22659) · [Project](https://gca-spatial-reasoning.github.io) | [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2026 | IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation | [arXiv](https://arxiv.org/abs/2601.03054) | [Code](https://github.com/Yankai96/IBISAgent) |
| 2026 | InSight-o3: Empowering Multimodal Foundation Models with Generalized Visual Search | [arXiv](https://arxiv.org/abs/2512.18745) | [Code](https://github.com/m-Just/InSight-o3) |
| 2026 | LensWalk: Agentic Video Understanding by Planning How You See in Videos | [arXiv](https://arxiv.org/abs/2603.24558) | — |
| 2026 | Memento: Toward an All-Day Proactive Assistant for Ultra-Long Streaming Video | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b5f4587a0bdb81ecc6ce9d82320a5c2-Abstract-Conference.html) | — |
| 2026 | OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection | [arXiv](https://arxiv.org/abs/2511.21064) | — |
| 2026 | REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting | [arXiv](https://arxiv.org/abs/2510.16410) · [Project](https://ChangyueShi.github.io/REALM) | [Code](https://github.com/ChangyueShi/REALM-Code) |
| 2026 | Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding | [arXiv](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning | [arXiv](https://arxiv.org/abs/2512.20934) · [Project](https://transductive-visualprogram.github.io/) | [Code](https://github.com/transductive-visualprogram/tvp) |
| 2026 | VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning | [arXiv](https://arxiv.org/abs/2503.13444) · [Project](https://videomind.github.io/) | [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | VTool-R1: VLMs Learn to Think with Images via Reinforcement Learning on Multimodal Tool Use | [arXiv](https://arxiv.org/abs/2505.19255) | [Code](https://github.com/VTOOL-R1/vtool-r1) |
| 2025 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | [arXiv](https://arxiv.org/abs/2511.21678) · [Project](https://weihao-bo.github.io/ViLoMeo-page) | [Code](https://github.com/weihao-bo/ViLoMem) |
| 2025 | SegAgent: Exploring Pixel Understanding Capabilities in MLLMs by Imitating Human Annotator Trajectories | [arXiv](https://arxiv.org/abs/2503.08625) | [Code](https://github.com/aim-uofa/SegAgent) |
| 2025 | Self-Evolving Visual Concept Library using Vision-Language Critics | [arXiv](https://arxiv.org/abs/2504.00185) | — |
| 2025 | VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning | [arXiv](https://arxiv.org/abs/2412.02172) · [Project](https://visco-benchmark.github.io/) | [Code](https://github.com/PlusLabNLP/VISCO) |
| 2025 | ViUniT: Visual Unit Tests for More Robust Visual Programming | [arXiv](https://arxiv.org/abs/2412.08859) | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2024 | CLOVA: A Closed-Loop Visual Assistant with Tool Usage and Update | [arXiv](https://arxiv.org/abs/2312.10908) | [Code](https://github.com/clova-tool/CLOVA-tool) |
| 2024 | V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs | [arXiv](https://arxiv.org/abs/2312.14135) · [Paper](https://doi.org/10.1109/cvpr52733.2024.01243) | [Code](https://github.com/penghao-wu/vstar) |
| 2024 | VideoAgent: Long-form Video Understanding with Large Language Model as Agent | [arXiv](https://arxiv.org/abs/2403.10517) | — |
| 2024 | Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models | [arXiv](https://arxiv.org/abs/2406.09403) · [Paper](https://doi.org/10.52202/079017-4423) · [Project](https://visualsketchpad.github.io/) | [Code](https://github.com/Yushi-Hu/VisualSketchpad) |
| 2023 | AVIS: Autonomous Visual Information Seeking with Large Language Model Agent | [arXiv](https://arxiv.org/abs/2306.08129) · [Paper](https://doi.org/10.52202/075280-0040) | — |
| 2023 | Visual Programming: Compositional visual reasoning without training | [arXiv](https://arxiv.org/abs/2211.11559) | [Code](https://github.com/allenai/visprog) |

<a id="section-5-2"></a>

### 5.2. Visual Generation, Editing, and World Construction

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Agentic Model Predictive Questioning Control in Visual Design | [Paper](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | Agentic Visual Generation: From Generative Models to Agentic Control | [arXiv](https://arxiv.org/abs/2609.06758) | [Code](https://github.com/YinmingHuang/Awesome-agentic-visual-generation-model) |
| 2026 | Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing | [arXiv](https://arxiv.org/abs/2607.08497) · [Project](https://caseclose.github.io/cma-harness/) | [Code](https://github.com/caseclose/cma-harness) |
| 2026 | CREA: A Collaborative Multi-Agent Framework for Creative Image Editing and Generation | [arXiv](https://arxiv.org/abs/2504.05306) · [Paper](https://doi.org/10.52202/085713-5705) | — |
| 2026 | DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving | [arXiv](https://arxiv.org/abs/2602.06521) | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| 2026 | FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing | [arXiv](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2026 | FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation | [arXiv](https://arxiv.org/abs/2604.13491) | — |
| 2026 | GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning | [arXiv](https://arxiv.org/abs/2601.18543) | Unavailable |
| 2026 | IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection | [arXiv](https://arxiv.org/abs/2603.29602) | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2026 | ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning | [arXiv](https://arxiv.org/abs/2603.08059) · [Project](https://github.com/zhaoyiran924/ImageEdit-R1) | — |
| 2026 | Learning Vision-Language-Action World Models for Autonomous Driving | [arXiv](https://arxiv.org/abs/2604.09059) · [Project](https://vlaworld.github.io) | — |
| 2026 | MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction | [arXiv](https://arxiv.org/abs/2606.14168) | — |
| 2026 | NEWTON: Agentic Planning for Physically Grounded Video Generation | [arXiv](https://arxiv.org/abs/2605.18396) · [Project](https://Newton026.github.io/newton) | [Code](https://github.com/CUTEPKQ/NEWTON) |
| 2026 | OctoT2I: A Self-Evolving Agentic Text-to-Image Router | [arXiv](https://arxiv.org/abs/2606.01803) | [Code](https://github.com/JaxJiang2642081986/OctoT2I) |
| 2026 | PerfGuard: A Performance-Aware Agent for Visual Content Generation | [arXiv](https://arxiv.org/abs/2601.22571) | [Code](https://github.com/FelixChan9527/PerfGuard) |
| 2026 | PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement | [arXiv](https://arxiv.org/abs/2602.14968) | — |
| 2026 | RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward | [arXiv](https://arxiv.org/abs/2602.17558) | — |
| 2026 | SAGE: Scalable Agentic 3D Scene Generation for Embodied AI | [arXiv](https://arxiv.org/abs/2602.10116) · [Project](https://research.nvidia.com/labs/dir/sage/) | — |
| 2026 | SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes | [arXiv](https://arxiv.org/abs/2602.09153) · [Project](https://scenesmith.github.io/) | [Code](https://github.com/nepfaff/scenesmith) |
| 2026 | SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation | [arXiv](https://arxiv.org/abs/2605.08043) | — |
| 2026 | Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution | [arXiv](https://arxiv.org/abs/2606.28971) | — |
| 2026 | Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing | [arXiv](https://arxiv.org/abs/2508.06916) | — |
| 2026 | TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration | [arXiv](https://arxiv.org/abs/2603.27742) | — |
| 2026 | Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends | [arXiv](https://arxiv.org/abs/2606.01164) | [Code](https://github.com/liujiuming123/Awesome-Interactive-World-Model) |
| 2026 | UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics | [arXiv](https://arxiv.org/abs/2604.02345) | — |
| 2026 | Vid2World: Crafting Video Diffusion Models to Interactive World Models | [arXiv](https://arxiv.org/abs/2505.14357) · [Project](http://knightnemo.github.io/vid2world/) | [Code](https://github.com/thuml/Vid2World) |
| 2026 | ViMax: Agentic Video Generation | [arXiv](https://arxiv.org/abs/2606.07649) | [Code](https://github.com/HKUDS/ViMax) |
| 2026 | VISTA: A Test-Time Self-Improving Video Generation Agent | [arXiv](https://arxiv.org/abs/2510.15831) | — |
| 2026 | WAM4D: Fast 4D World Action Model via Spatial Register Tokens | [arXiv](https://arxiv.org/abs/2606.14048) | — |
| 2026 | WEAVER, Better, Faster, Longer: An Effective World Model for Robotic Manipulation | [arXiv](https://arxiv.org/abs/2606.13672) · [Project](https://arnavkj1995.github.io/WEAVER/) | [Code](https://github.com/arnavkj1995/WEAVER) |
| 2026 | World Action Models: The Next Frontier in Embodied AI | [arXiv](https://arxiv.org/abs/2605.12090) | — |
| 2026 | WorldAgents: Can Foundation Image Models be Agents for 3D World Models? | [arXiv](https://arxiv.org/abs/2603.19708) · [Project](https://ziyaerkoc.com/worldagents/) | — |
| 2025 | 4KAgent: Agentic Any Image to 4K Super-Resolution | [arXiv](https://arxiv.org/abs/2507.07105) · [Paper](https://doi.org/10.52202/085713-5476) · [Project](https://4kagent.github.io) | [Code](https://github.com/taco-group/4KAgent) |
| 2025 | Astra: General Interactive World Model with Autoregressive Denoising | [arXiv](https://arxiv.org/abs/2512.08931) | [Code](https://github.com/EternalEvan/Astra) |
| 2025 | ComfyUI-Copilot: An Intelligent Assistant for Automated Workflow Development | [arXiv](https://arxiv.org/abs/2506.05010) | [Code](https://github.com/ATH-MaaS/ComfyUI-Copilot) |
| 2025 | Ctrl-World: A Controllable Generative World Model for Robot Manipulation | [arXiv](https://arxiv.org/abs/2510.10125) | — |
| 2025 | GenPilot: A Multi-Agent System for Test-Time Prompt Optimization in Image Generation | [arXiv](https://arxiv.org/abs/2510.07217) | [Code](https://github.com/27yw/GenPilot) |
| 2025 | Mastering Diverse Control Tasks through World Models | [arXiv](https://arxiv.org/abs/2301.04104) · [Paper](https://www.nature.com/articles/s41586-025-08744-2) | [Code](https://github.com/danijar/dreamerv3) |
| 2025 | PlotEdit: Natural Language-Driven Accessible Chart Editing in PDFs via Multimodal LLM Agents | [arXiv](https://arxiv.org/abs/2501.11233) | — |
| 2025 | Proactive Agents for Multi-Turn Text-to-Image Generation Under Uncertainty | [arXiv](https://arxiv.org/abs/2412.06771) | [Code](https://github.com/google-deepmind/proactive_t2i_agents) |
| 2025 | SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent | [arXiv](https://arxiv.org/abs/2509.20414) · [Paper](https://doi.org/10.52202/085713-4689) · [Project](https://scene-weaver.github.io/) | [Code](https://github.com/Scene-Weaver/SceneWeaver) |
| 2025 | Semantic World Models | [arXiv](https://arxiv.org/abs/2510.19818) · [Project](https://weirdlabuw.github.io/swm) | — |
| 2025 | SILMM: Self-Improving Large Multimodal Models for Compositional Text-to-Image Generation | [arXiv](https://arxiv.org/abs/2412.05818) · [Project](https://silmm.github.io/) | [Code](https://github.com/LgQu/SILMM) |
| 2025 | V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning | [arXiv](https://arxiv.org/abs/2506.09985) | [Code](https://github.com/facebookresearch/vjepa2) |
| 2025 | V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents | [arXiv](https://arxiv.org/abs/2503.12077) | — |
| 2025 | World-To-Image: Grounding Text-to-Image Generation with Agent-Driven World Knowledge | [arXiv](https://arxiv.org/abs/2510.04201) | [Code](https://github.com/mhson-kyle/World-To-Image) |
| 2024 | Diffusion for World Modeling: Visual Details Matter in Atari | [arXiv](https://arxiv.org/abs/2405.12399) · [Project](https://diamond-wm.github.io) | [Code](https://github.com/eloialonso/diamond) |
| 2024 | ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment | [arXiv](https://arxiv.org/abs/2403.05135) · [Project](https://ella-diffusion.github.io/) | [Code](https://github.com/TencentQQGYLab/ELLA) |
| 2024 | GenArtist: Multimodal LLM as an Agent for Unified Image Generation and Editing | [arXiv](https://arxiv.org/abs/2407.05600) · [Project](https://zhenyuw16.github.io/GenArtist_page) | [Code](https://github.com/zhenyuw16/GenArtist) |
| 2024 | Genie: Generative Interactive Environments | [arXiv](https://arxiv.org/abs/2402.15391) · [Project](https://sites.google.com/corp/view/genie-2024/) | — |
| 2024 | LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing | [arXiv](https://arxiv.org/abs/2402.10294) | — |
| 2024 | Mastering Text-to-Image Diffusion: Recaptioning, Planning, and Generating with Multimodal LLMs | [arXiv](https://arxiv.org/abs/2401.11708) | [Code](https://github.com/YangLing0818/RPG-DiffusionMaster) |
| 2024 | Preference Adaptive and Sequential Text-to-Image Generation | [arXiv](https://arxiv.org/abs/2412.10419) · [Project](https://www.kaggle.com/datasets/googleai/pasta-data) | — |
| 2024 | RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models | [arXiv](https://arxiv.org/abs/2407.18035) · [Paper](https://doi.org/10.52202/079017-3512) | — |
| 2024 | SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code | [arXiv](https://arxiv.org/abs/2403.01248) | — |
| 2024 | Self-correcting LLM-controlled Diffusion Models | [arXiv](https://arxiv.org/abs/2311.16090) | — |
| 2023 | Adding Conditional Control to Text-to-Image Diffusion Models | [arXiv](https://arxiv.org/abs/2302.05543) | [Code](https://github.com/lllyasviel/ControlNet) |
| 2023 | InstructPix2Pix: Learning to Follow Image Editing Instructions | [arXiv](https://arxiv.org/abs/2211.09800) · [Project](https://www.timothybrooks.com/instruct-pix2pix) | — |
| 2023 | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | [arXiv](https://arxiv.org/abs/2308.06721) · [Project](https://ip-adapter.github.io) | [Code](https://github.com/tencent-ailab/IP-Adapter) |
| 2023 | LayoutGPT: Compositional Visual Planning and Generation with Large Language Models | [arXiv](https://arxiv.org/abs/2305.15393) | [Code](https://github.com/weixi-feng/layoutgpt) |
| 2023 | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | [arXiv](https://arxiv.org/abs/2306.10012) · [Project](https://osu-nlp-group.github.io/MagicBrush/) | [Code](https://github.com/OSU-NLP-Group/MagicBrush) |
| 2023 | Transformers are Sample-Efficient World Models | [arXiv](https://arxiv.org/abs/2209.00588) | [Code](https://github.com/eloialonso/iris) |
| 2022 | Hierarchical Text-Conditional Image Generation with CLIP Latents | [arXiv](https://arxiv.org/abs/2204.06125) | — |
| 2022 | High-Resolution Image Synthesis with Latent Diffusion Models | [arXiv](https://arxiv.org/abs/2112.10752) | [Code](https://github.com/CompVis/latent-diffusion) |
| 2021 | Learning Transferable Visual Models From Natural Language Supervision | [arXiv](https://arxiv.org/abs/2103.00020) | [Code](https://github.com/OpenAI/CLIP) |
| 2019 | Learning Latent Dynamics for Planning from Pixels | [arXiv](https://arxiv.org/abs/1811.04551) | [Code](https://github.com/google-research/planet) |
| 2018 | World Models | [arXiv](https://arxiv.org/abs/1803.10122) · [Project](https://worldmodels.github.io/) | — |
|  | AgentMV: A State-Guided Multi-Agent Framework for Budget-Aware Music Video Generation | [arXiv](https://arxiv.org/abs/2605.10723) | — |

<a id="section-5-3"></a>

### 5.3. GUI and Digital Environment Interaction

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | CoAct-1: Computer-using Multi-Agent System with Coding Actions | [arXiv](https://arxiv.org/abs/2508.03923) | [Code](https://github.com/SalesforceAIResearch/CoAct-1) |
| 2026 | GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents | [arXiv](https://arxiv.org/abs/2506.03143) | [Code](https://github.com/microsoft/GUI-Actor) |
| 2026 | Hierarchical Procedural Meta-Reasoning for Generalizable Multimodal Agents | [Paper](https://openreview.net/forum?id=v2H2vzRqcr) | — |
| 2026 | Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness | [arXiv](https://arxiv.org/abs/2510.01670) | — |
| 2026 | K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control | [arXiv](https://arxiv.org/abs/2603.00676) | — |
| 2026 | LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent | [Paper](https://openreview.net/forum?id=BK7Mk5d4WE) | — |
| 2026 | MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2509.18119) · [Paper](https://doi.org/10.48550/arxiv.2509.18119) | [Code](https://github.com/THUDM/MobileRL) |
| 2026 | PSBench: Editing Image via GUI Agents in Photoshop | [Paper](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | R-WoM: Retrieval-augmented World Model For Computer-use Agents | [arXiv](https://arxiv.org/abs/2510.11892) · [Paper](https://doi.org/10.48550/arxiv.2510.11892) | — |
| 2026 | ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data | [arXiv](https://arxiv.org/abs/2509.15221) · [Paper](https://doi.org/10.48550/arxiv.2509.15221) | [Code](https://github.com/OpenGVLab/ScaleCUA) |
| 2026 | ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows | [arXiv](https://arxiv.org/abs/2505.19897) · [Project](https://qiushisun.github.io/ScienceBoard-Home/) | [Code](https://github.com/OS-Copilot/ScienceBoard) |
| 2026 | ViMo: A Generative Visual GUI World Model for App Agents | [arXiv](https://arxiv.org/abs/2504.13936) · [Paper](https://doi.org/10.48550/arxiv.2504.13936) · [Project](https://ai-agents-2030.github.io/ViMo/) | [Code](https://github.com/ai-agents-2030/ViMo) |
| 2026 | VisCritic: Visual State Comparison as Process Reward for GUI Agents | [arXiv](https://arxiv.org/abs/2606.24525) | — |
| 2026 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | [arXiv](https://arxiv.org/abs/2506.02456) | [Code](https://github.com/cua-framework/agents) |
| 2025 | Agent S: An Open Agentic Framework that Uses Computers Like a Human | [arXiv](https://arxiv.org/abs/2410.08164) | [Code](https://github.com/simular-ai/Agent-S) |
| 2025 | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | [arXiv](https://arxiv.org/abs/2405.14573) | [Code](https://github.com/google-research/android_world) |
| 2025 | GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior | [arXiv](https://arxiv.org/abs/2506.08012) · [Paper](https://doi.org/10.52202/085713-3409) · [Project](https://penghao-wu.github.io/GUI_Reflection/) | [Code](https://github.com/penghao-wu/GUI_Reflection) |
| 2025 | Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents | [arXiv](https://arxiv.org/abs/2410.05243) · [Paper](https://doi.org/10.48550/arxiv.2410.05243) · [Project](https://osu-nlp-group.github.io/UGround/) | [Code](https://github.com/OSU-NLP-Group/UGround) |
| 2025 | ShowUI: One Vision-Language-Action Model for GUI Visual Agent | [arXiv](https://arxiv.org/abs/2411.17465) | [Code](https://github.com/showlab/ShowUI) |
| 2025 | UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2505.21496) · [Paper](https://doi.org/10.52202/085713-5028) | [Code](https://github.com/Euphoria16/UI-Genie) |
| 2024 | CogAgent: A Visual Language Model for GUI Agents | [arXiv](https://arxiv.org/abs/2312.08914) | [CogVLM](https://github.com/zai-org/CogVLM) · [CogAgent](https://github.com/zai-org/CogAgent) |
| 2024 | Cradle: Empowering Foundation Agents Towards General Computer Control | [arXiv](https://arxiv.org/abs/2403.03186) | [Code](https://github.com/BAAI-Agents/Cradle) |
| 2024 | GPT-4V(ision) is a Generalist Web Agent, if Grounded | [arXiv](https://arxiv.org/abs/2401.01614) | [Code](https://github.com/OSU-NLP-Group/SeeAct) |
| 2024 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | [arXiv](https://arxiv.org/abs/2404.07972) · [Project](https://os-world.github.io) | [Code](https://github.com/xlang-ai/OSWorld) |
| 2023 | From Pixels to UI Actions: Learning to Follow Instructions via Graphical User Interfaces | [arXiv](https://arxiv.org/abs/2306.00245) · [Paper](https://doi.org/10.48550/arxiv.2306.00245) | [Code](https://github.com/google-deepmind/pix2act) |

<a id="section-5-4"></a>

### 5.4. Embodied Agents and Autonomous Systems

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation | [arXiv](https://arxiv.org/abs/2601.08325) | — |
| 2026 | AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions | [arXiv](https://arxiv.org/abs/2506.14697) | — |
| 2026 | AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation | [arXiv](https://arxiv.org/abs/2605.22816) · [Project](https://gwxuan.github.io/AwareVLN/) | [Code](https://github.com/GWxuan/AwareVLN) |
| 2026 | DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving | [arXiv](https://arxiv.org/abs/2510.12796) | [Code](https://github.com/BraveGroup/DriveVLA-W0) |
| 2026 | Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use | [arXiv](https://arxiv.org/abs/2608.14047) | — |
| 2026 | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — | — |
| 2026 | PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation | [arXiv](https://arxiv.org/abs/2606.08414) | [Code](https://github.com/thu-ml/PACT) |
| 2026 | RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks | [arXiv](https://arxiv.org/abs/2603.11558) | [Code](https://github.com/RoboClaw-Robotics/RoboClaw) |
| 2026 | Self-Improving Loops for Visual Robotic Planning | [arXiv](https://arxiv.org/abs/2506.06658) · [Project](https://diffusion-supervision.github.io/silvr/) | [Code](https://github.com/brown-palm/silvr) |
| 2026 | Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures | [arXiv](https://arxiv.org/abs/2603.01063) | — |
| 2026 | WMPO: World Model-based Policy Optimization for Vision-Language-Action Models | [arXiv](https://arxiv.org/abs/2511.09515) · [Project](https://wm-po.github.io) | [Code](https://github.com/WM-PO/WMPO) |
| 2025 | AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning | [arXiv](https://arxiv.org/abs/2506.13757) · [Project](https://autovla.github.io/) | [Code](https://github.com/ucla-mobility/AutoVLA) |
| 2025 | C-NAV: Towards Self-Evolving Continual Object Navigation in Open World | [arXiv](https://arxiv.org/abs/2510.20685) · [Paper](https://doi.org/10.52202/085713-4206) · [Project](https://bigtree765.github.io/C-Nav-project) | [Code](https://github.com/BigTree765/C-Nav) |
| 2025 | Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection | [arXiv](https://arxiv.org/abs/2412.04455) · [Project](https://zhoues.github.io/Code-as-Monitor/) | — |
| 2025 | HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation | [arXiv](https://arxiv.org/abs/2502.05485) · [Project](https://hamster-robot.github.io/) | [Code](https://github.com/liyi14/HAMSTER_beta) |
| 2025 | LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents | [arXiv](https://arxiv.org/abs/2505.22634) · [Paper](https://doi.org/10.52202/085713-1158) | — |
| 2025 | Navigation World Models | [arXiv](https://arxiv.org/abs/2412.03572) · [Project](https://www.amirbar.net/nwm/) | [Code](https://github.com/facebookresearch/nwm/) |
| 2025 | Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction | [arXiv](https://arxiv.org/abs/2504.14588) | [Code](https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework) |
| 2024 | DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models | [arXiv](https://arxiv.org/abs/2309.16292) · [Project](https://pjlab-adg.github.io/DiLu/) | [Code](https://github.com/PJLab-ADG/DiLu) |
| 2024 | DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | [arXiv](https://arxiv.org/abs/2403.12945) · [Project](https://droid-dataset.github.io/) | [droid](https://github.com/droid-dataset/droid) · [droid_policy_learning](https://github.com/droid-dataset/droid_policy_learning) |
| 2024 | LMDrive: Closed-Loop End-to-End Driving with Large Language Models | [arXiv](https://arxiv.org/abs/2312.07488) · [Project](https://hao-shao.com/projects/lmdrive.html) | [Code](https://github.com/opendilab/LMDrive) |
| 2024 | NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models | [arXiv](https://arxiv.org/abs/2407.12366) | [Code](https://github.com/GengzeZhou/NavGPT-2) |
| 2024 | PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs | [arXiv](https://arxiv.org/abs/2402.07872) · [Project](http://pivot-prompt.github.io) | — |
| 2024 | SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation | [arXiv](https://arxiv.org/abs/2410.08189) · [Project](https://bagh2178.github.io/SG-Nav/) | [Code](https://github.com/bagh2178/SG-Nav) |
| 2024 | Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2) | [arXiv](https://arxiv.org/abs/2402.16720) | — |
| 2024 | VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought | [arXiv](https://arxiv.org/abs/2406.14596) · [Paper](https://doi.org/10.52202/079017-2418) · [Project](https://ical-learning.github.io/) | [Code](https://github.com/Gabesarch/ICAL) |
| 2023 | MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations | [arXiv](https://arxiv.org/abs/2310.17596) · [Project](https://mimicgen.github.io) | [Code](https://github.com/NVlabs/mimicgen) |
| 2020 | nuScenes: A multimodal dataset for autonomous driving | [arXiv](https://arxiv.org/abs/1903.11027) | [Code](https://github.com/nutonomy/nuscenes-devkit) |

<a id="section-5-5"></a>

### 5.5. Medical

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | 3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis | [arXiv](https://arxiv.org/abs/2602.18064) · [Project](http://assistants.Code) | [Code](https://github.com/jinlab-imvr/3DMedAgent) |
| 2026 | CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework | [arXiv](https://arxiv.org/abs/2603.01607) · [Project](https://xypb.github.io/CARE-Project-Page/) | [Code](https://github.com/XYPB/CARE) |
| 2026 | CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare | [arXiv](https://arxiv.org/abs/2603.24157) | — |
| 2026 | IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation | [arXiv](https://arxiv.org/abs/2601.03054) | [Code](https://github.com/Yankai96/IBISAgent) |
| 2026 | MedAgent-Pro: Towards Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow | [arXiv](https://arxiv.org/abs/2503.18968) | [Code](https://github.com/jinlab-imvr/MedAgent-Pro) |
| 2026 | MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning | [arXiv](https://arxiv.org/abs/2604.08203) | [Code](https://github.com/alibaba-damo-academy/MedVR) |
| 2026 | MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning | [arXiv](https://arxiv.org/abs/2506.00555) | — |
| 2026 | Ophiuchus: Incentivizing Tool-augmented "Think with Images" for Joint Medical Segmentation, Understanding and Reasoning | [arXiv](https://arxiv.org/abs/2512.14157) | [Code](https://github.com/SII-zyj/Ophiuchus) |
| 2026 | TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging | [arXiv](https://arxiv.org/abs/2606.29763) | [Code](https://github.com/gm3g11/TopoAgent) |
| 2025 | CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic | [arXiv](https://arxiv.org/abs/2505.20510) · [Paper](https://doi.org/10.52202/085713-3404) | — |
| 2025 | MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks | [arXiv](https://arxiv.org/abs/2505.12371) · [Paper](https://doi.org/10.52202/085713-4851) · [Project](https://medagentboard.netlify.app/) | [Code](https://github.com/yhzhu99/MedAgentBoard) |
| 2025 | MedRAX: Medical Reasoning Agent for Chest X-ray | [arXiv](https://arxiv.org/abs/2502.02673) | [Code](https://github.com/bowang-lab/MedRAX) |
| 2025 | NOVA: An Agentic Framework for Automated Histopathology Analysis and Discovery | [arXiv](https://arxiv.org/abs/2511.11324) | [Code](https://github.com/microsoft/nova-agent) |
| 2025 | PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration | [arXiv](https://arxiv.org/abs/2407.00203) | [Code](https://github.com/PathFoundation/PathGen-1.6M) |
| 2024 | MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making | [arXiv](https://arxiv.org/abs/2404.15155) · [Paper](https://doi.org/10.52202/079017-2522) | [Code](https://github.com/mitmedialab/MDAgents) |

<a id="section-5-6"></a>

### 5.6. Scientific Agent

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | AutoMat: Physics-Guided Agentic Reasoning for Solving Ill-Posed Inverse Microscopy Problems | [arXiv](https://arxiv.org/abs/2505.12650) · [Paper](https://openreview.net/forum?id=TLroFiKilA) | [Code](https://github.com/yyt-2378/AutoMat) |
| 2026 | CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations | [arXiv](https://arxiv.org/abs/2606.03435) | — |
| 2026 | GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing | [arXiv](https://arxiv.org/abs/2604.08896) | — |
| 2026 | LiveFigure: Generating Editable Scientific Illustration with VLM Agents | [arXiv](https://arxiv.org/abs/2605.23527) | [Code](https://github.com/tsinghua-fib-lab/LiveFigure) |
| 2026 | NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation | [arXiv](https://arxiv.org/abs/2608.09636) | — |
| 2026 | SciEducator: Scientific Video Understanding and Educating via Deming-Cycle Multi-Agent System | [arXiv](https://arxiv.org/abs/2511.17943) | — |
| 2026 | ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows | [arXiv](https://arxiv.org/abs/2505.19897) · [Project](https://qiushisun.github.io/ScienceBoard-Home/) | [Code](https://github.com/OS-Copilot/ScienceBoard) |
| 2026 | Simple Agents Outperform Experts in Biomedical Imaging Workflow Optimization | [arXiv](https://arxiv.org/abs/2512.06006) | [Code](https://github.com/xuefei-wang/simple-agent-opt) |
| 2026 | Towards Multimodal Data-Driven Scientific Discovery Powered by LLM Agents | [Paper](https://openreview.net/forum?id=kZHSvETWdi) | [Code](https://github.com/usail-hkust/MoSciBench) |
| 2026 | VERITAS: A Multi-Agent Co-Scientist for Verifiable Image-Derived Hypothesis Testing | [arXiv](https://arxiv.org/abs/2604.12144) | [Code](https://github.com/LucZot/veritas) |
| 2025 | Agent reviewers: Domain-specific multimodal agents with shared memory for paper review | [Paper](https://proceedings.mlr.press/v267/lu25p.html) | [Code](https://github.com/AReviewers/AgentReviewers) |
| 2025 | LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents | [arXiv](https://arxiv.org/abs/2505.22634) · [Paper](https://doi.org/10.52202/085713-1158) | — |
| 2025 | Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers | [arXiv](https://arxiv.org/abs/2505.21497) · [Paper](https://doi.org/10.52202/085713-0530) | [Code](https://github.com/Paper2Poster/Paper2Poster) |
| 2025 | ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | [arXiv](https://arxiv.org/abs/2410.05080) | [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| 2025 | SketchMind: A Multi-Agent Cognitive Framework for Assessing Student-Drawn Scientific Sketches | [arXiv](https://arxiv.org/abs/2507.22904) · [Paper](https://doi.org/10.52202/085713-2774) | — |
| 2024 | DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents | [arXiv](https://arxiv.org/abs/2406.06769) · [Paper](https://doi.org/10.52202/079017-0324) | [Code](https://github.com/allenai/discoveryworld) |
| 2024 | Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows? | [arXiv](https://arxiv.org/abs/2407.10956) · [Paper](https://doi.org/10.52202/079017-3421) · [Project](https://spider2-v.github.io) | [Code](https://github.com/xlang-ai/Spider2-V) |

<a id="section-6"></a>

## 6. Evaluation and Benchmarks

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Agent-X: Evaluating Deep Multimodal Reasoning in Vision-Centric Agentic Tasks | [arXiv](https://arxiv.org/abs/2505.24876) | [Code](https://github.com/mbzuai-oryx/Agent-X) |
| 2026 | EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments | [arXiv](https://arxiv.org/abs/2607.05155) | — |
| 2026 | How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position | [arXiv](https://arxiv.org/abs/2606.15032) | — |
| 2026 | VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation | [arXiv](https://arxiv.org/abs/2503.06800) · [Project](https://videophy2.github.io/) | [Code](https://github.com/Hritikbansal/videophy/tree/main/VIDEOPHY2) |
| 2026 | WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation | [arXiv](https://arxiv.org/abs/2605.25874) · [Project](https://meituan-longcat.github.io/WBench/) | [Code](https://github.com/meituan-longcat/WBench) |
| 2026 | WorldMark: A Unified Benchmark Suite for Interactive Video World Models | [arXiv](https://arxiv.org/abs/2604.21686) | [Code](https://github.com/AlayaLab/WorldMark) |
| 2025 | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | [arXiv](https://arxiv.org/abs/2509.13399) | [Code](https://github.com/TianyuCodings/EdiVal) |
| 2025 | GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation | [arXiv](https://arxiv.org/abs/2512.16853) | [Code](https://github.com/facebookresearch/GenEval2) |
| 2025 | T2I-CompBench++: An Enhanced and Comprehensive Benchmark for Compositional Text-to-image Generation | [arXiv](https://arxiv.org/abs/2307.06350) · [Project](https://karine-h.github.io/T2I-CompBench-new/) | [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| 2025 | Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation | [arXiv](https://arxiv.org/abs/2410.05363) · [Project](https://phygenbench123.github.io/) | [Code](https://github.com/OpenGVLab/PhyGenBench) |
| 2025 | WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation | [arXiv](https://arxiv.org/abs/2503.07265) | [Code](https://github.com/PKU-YuanGroup/WISE) |
| 2024 | VBench: Comprehensive Benchmark Suite for Video Generative Models | [arXiv](https://arxiv.org/abs/2311.17982) · [Project](https://vchitect.github.io/VBench-project/) | [Code](https://github.com/Vchitect/VBench) |
| 2023 | Analyzing Modular Approaches for Visual Question Decomposition | [arXiv](https://arxiv.org/abs/2311.06411) · [Paper](https://doi.org/10.18653/v1/2023.emnlp-main.157) | [Code](https://github.com/brown-palm/visual-question-decomposition) |
| 2023 | GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | [arXiv](https://arxiv.org/abs/2310.11513) | [Code](https://github.com/djghosh13/geneval) |
| 2023 | T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation | [arXiv](https://arxiv.org/abs/2307.06350v1) | [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| 2023 | TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering | [arXiv](https://arxiv.org/abs/2303.11897) | [Code](https://github.com/Yushi-Hu/tifa) |
| 2021 | NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions | [arXiv](https://arxiv.org/abs/2105.08276) · [Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Xiao_NExT-QA_Next_Phase_of_Question-Answering_to_Explaining_Temporal_Actions_CVPR_2021_paper.pdf) | [Code](https://github.com/doc-doc/NExT-QA) |
| 2020 | ReferIt3D: Neural Listeners for Fine-Grained 3D Object Identification in Real-World Scenes | [Paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123460409.pdf) | [Code](https://github.com/referit3d/referit3d) |
| 2020 | ScanRefer: 3D Object Localization in RGB-D Scans using Natural Language | [arXiv](https://arxiv.org/abs/1912.08830) · [Project](https://daveredrum.github.io/ScanRefer/) | [Code](https://github.com/daveredrum/ScanRefer) |
| 2019 | GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering | [arXiv](https://arxiv.org/abs/1902.09506) | — |

<a id="section-6-1"></a>

### 6.1. Evaluating Evidence and State Management

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing | [arXiv](https://arxiv.org/abs/2604.08896) | — |
| 2026 | Memento: Toward an All-Day Proactive Assistant for Ultra-Long Streaming Video | [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b5f4587a0bdb81ecc6ce9d82320a5c2-Abstract-Conference.html) | — |
| 2026 | TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning | [arXiv](https://arxiv.org/abs/2511.01833) | [Code](https://github.com/agents-x-project/TIR-Bench) |
| 2025 | Code-Vision: Evaluating Multimodal LLMs Logic Understanding and Code Generation Capabilities | [arXiv](https://arxiv.org/abs/2502.11829) | [Code](https://github.com/wanghanbinpanda/CodeVision) |
| 2025 | GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding | [arXiv](https://arxiv.org/abs/2406.10819) · [Project](https://gui-world.github.io) | [Code](https://github.com/Dongping-Chen/GUI-World) |
| 2025 | MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks | [arXiv](https://arxiv.org/abs/2505.12371) · [Paper](https://doi.org/10.52202/085713-4851) · [Project](https://medagentboard.netlify.app/) | [Code](https://github.com/yhzhu99/MedAgentBoard) |
| 2025 | Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis | [arXiv](https://arxiv.org/abs/2405.21075) · [Project](https://video-mme.github.io) | — |
| 2024 | LongVideoBench: A Benchmark for Long-context Interleaved Video-Language Understanding | [arXiv](https://arxiv.org/abs/2407.15754) | [Code](https://github.com/LongVideoBench/LongVideoBench) |
| 2024 | MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI | [arXiv](https://arxiv.org/abs/2311.16502) | [Code](https://github.com/MMMU-benchmark/MMMU) |
| 2024 | V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs | [arXiv](https://arxiv.org/abs/2312.14135) · [Paper](https://doi.org/10.1109/cvpr52733.2024.01243) | [Code](https://github.com/penghao-wu/vstar) |

<a id="section-6-2"></a>

### 6.2. Evaluating Planning and Execution

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | CapNav: Benchmarking Vision Language Models on Capability-conditioned Indoor Navigation | [arXiv](https://arxiv.org/abs/2602.18424) | [Code](https://github.com/makeabilitylab/CapNav) |
| 2026 | GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents | [arXiv](https://arxiv.org/abs/2604.07429) · [Project](https://gameworld-bench.github.io) | [Code](https://github.com/gameworld-project/gameworld) |
| 2026 | MMBench-GUI: Hierarchical Multi-Platform Evaluation Framework for GUI Agents | [arXiv](https://arxiv.org/abs/2507.19478) | [Code](https://github.com/open-compass/MMBench-GUI) |
| 2026 | Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games | [arXiv](https://arxiv.org/abs/2506.03610) · [Project](https://huggingface.co/datasets/KRAFTON/Orak) | [Code](https://github.com/krafton-ai/Orak) |
| 2026 | OSWorld-MCP: Benchmarking MCP Tool Invocation In Computer-Use Agents | [arXiv](https://arxiv.org/abs/2510.24563) · [Project](https://osworld-mcp.github.io) | [Code](https://github.com/X-PLUG/OSWorld-MCP) |
| 2026 | PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives | [arXiv](https://arxiv.org/abs/2608.13552) · [Project](https://kxding.github.io/project/PlayWorld/) | [Code](https://github.com/hku-sail/PlayWorld) |
| 2026 | PSBench: Editing Image via GUI Agents in Photoshop | [Paper](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows | [arXiv](https://arxiv.org/abs/2505.19897) · [Project](https://qiushisun.github.io/ScienceBoard-Home/) | [Code](https://github.com/OS-Copilot/ScienceBoard) |
| 2026 | TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning | [arXiv](https://arxiv.org/abs/2511.01833) | [Code](https://github.com/agents-x-project/TIR-Bench) |
| 2025 | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | [arXiv](https://arxiv.org/abs/2405.14573) | [Code](https://github.com/google-research/android_world) |
| 2025 | ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems | [arXiv](https://arxiv.org/abs/2409.01392) | [Code](https://github.com/xxyQwQ/ComfyBench) |
| 2025 | EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents | [arXiv](https://arxiv.org/abs/2502.09560) · [Project](https://embodiedbench.github.io) | [Code](https://github.com/EmbodiedBench/EmbodiedBench) |
| 2025 | LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents | [arXiv](https://arxiv.org/abs/2505.22634) · [Paper](https://doi.org/10.52202/085713-1158) | — |
| 2025 | MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks | [arXiv](https://arxiv.org/abs/2505.12371) · [Paper](https://doi.org/10.52202/085713-4851) · [Project](https://medagentboard.netlify.app/) | [Code](https://github.com/yhzhu99/MedAgentBoard) |
| 2025 | PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks | [arXiv](https://arxiv.org/abs/2411.00081) | [Code](https://github.com/facebookresearch/partnr-planner) |
| 2025 | ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | [arXiv](https://arxiv.org/abs/2410.05080) | [Code](https://github.com/OSU-NLP-Group/ScienceAgentBench) |
| 2024 | Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving | [arXiv](https://arxiv.org/abs/2406.03877) | [Code](https://github.com/Thinklab-SJTU/Bench2Drive) |
| 2024 | DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents | [arXiv](https://arxiv.org/abs/2406.06769) · [Paper](https://doi.org/10.52202/079017-0324) | [Code](https://github.com/allenai/discoveryworld) |
| 2024 | GTA: A Benchmark for General Tool Agents | [arXiv](https://arxiv.org/abs/2407.08713) · [Paper](https://doi.org/10.52202/079017-2412) | [Code](https://github.com/open-compass/GTA) |
| 2024 | NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking | [arXiv](https://arxiv.org/abs/2406.15349) | [Code](https://github.com/autonomousvision/navsim) |
| 2024 | OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web | [arXiv](https://arxiv.org/abs/2402.17553) | — |
| 2024 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | [arXiv](https://arxiv.org/abs/2404.07972) · [Project](https://os-world.github.io) | [Code](https://github.com/xlang-ai/OSWorld) |

<a id="section-6-3"></a>

### 6.3. Evaluating Feedback and Adaptive Control

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions | [arXiv](https://arxiv.org/abs/2506.14697) | — |
| 2026 | LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models | [arXiv](https://arxiv.org/abs/2510.13626) · [Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf) | [Code](https://github.com/sylvestf/LIBERO-plus) |
| 2026 | PSBench: Editing Image via GUI Agents in Photoshop | [Paper](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning | [arXiv](https://arxiv.org/abs/2512.20934) · [Project](https://transductive-visualprogram.github.io/) | [Code](https://github.com/transductive-visualprogram/tvp) |
| 2026 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | [arXiv](https://arxiv.org/abs/2506.02456) | [Code](https://github.com/cua-framework/agents) |
| 2026 | WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks | [arXiv](https://arxiv.org/abs/2504.18575) | [Code](https://github.com/facebookresearch/wasp) |
| 2025 | AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents | [arXiv](https://arxiv.org/abs/2405.14573) | [Code](https://github.com/google-research/android_world) |
| 2025 | ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems | [arXiv](https://arxiv.org/abs/2409.01392) | [Code](https://github.com/xxyQwQ/ComfyBench) |
| 2025 | OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents | [arXiv](https://arxiv.org/abs/2506.14866) | [Code](https://github.com/tml-epfl/os-harm) |
| 2025 | VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning | [arXiv](https://arxiv.org/abs/2412.02172) · [Project](https://visco-benchmark.github.io/) | [Code](https://github.com/PlusLabNLP/VISCO) |
| 2024 | DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents | [arXiv](https://arxiv.org/abs/2406.06769) · [Paper](https://doi.org/10.52202/079017-0324) | [Code](https://github.com/allenai/discoveryworld) |
| 2024 | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | [arXiv](https://arxiv.org/abs/2404.07972) · [Project](https://os-world.github.io) | [Code](https://github.com/xlang-ai/OSWorld) |
| 2023 | LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | [arXiv](https://arxiv.org/abs/2306.03310) · [Project](https://libero-project.github.io) | — |

<a id="section-7"></a>

## 7. Challenges and Outlooks

<a id="section-7-1"></a>

### 7.1. Open Challenges

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation | [arXiv](https://arxiv.org/abs/2601.08325) | — |
| 2026 | Agentic Model Predictive Questioning Control in Visual Design | [Paper](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions | [arXiv](https://arxiv.org/abs/2506.14697) | — |
| 2026 | CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare | [arXiv](https://arxiv.org/abs/2603.24157) | — |
| 2026 | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — | — |
| 2026 | FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing | [arXiv](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2026 | LensWalk: Agentic Video Understanding by Planning How You See in Videos | [arXiv](https://arxiv.org/abs/2603.24558) | — |
| 2026 | NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation | [arXiv](https://arxiv.org/abs/2608.09636) | — |
| 2026 | PSBench: Editing Image via GUI Agents in Photoshop | [Paper](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | Reflect-R1: Evidence-Driven Reflection for Self-Correction in Long Video Understanding | [arXiv](https://arxiv.org/abs/2606.27922) | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2026 | RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward | [arXiv](https://arxiv.org/abs/2602.17558) | — |
| 2026 | TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging | [arXiv](https://arxiv.org/abs/2606.29763) | [Code](https://github.com/gm3g11/TopoAgent) |
| 2026 | Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning | [arXiv](https://arxiv.org/abs/2512.20934) · [Project](https://transductive-visualprogram.github.io/) | [Code](https://github.com/transductive-visualprogram/tvp) |
| 2026 | VERITAS: A Multi-Agent Co-Scientist for Verifiable Image-Derived Hypothesis Testing | [arXiv](https://arxiv.org/abs/2604.12144) | [Code](https://github.com/LucZot/veritas) |
| 2026 | VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents | [arXiv](https://arxiv.org/abs/2506.02456) | [Code](https://github.com/cua-framework/agents) |
| 2026 | WMPO: World Model-based Policy Optimization for Vision-Language-Action Models | [arXiv](https://arxiv.org/abs/2511.09515) · [Project](https://wm-po.github.io) | [Code](https://github.com/WM-PO/WMPO) |
| 2026 | WorldAgents: Can Foundation Image Models be Agents for 3D World Models? | [arXiv](https://arxiv.org/abs/2603.19708) · [Project](https://ziyaerkoc.com/worldagents/) | — |
| 2025 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | [arXiv](https://arxiv.org/abs/2511.21678) · [Project](https://weihao-bo.github.io/ViLoMeo-page) | [Code](https://github.com/weihao-bo/ViLoMem) |
| 2025 | Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection | [arXiv](https://arxiv.org/abs/2412.04455) · [Project](https://zhoues.github.io/Code-as-Monitor/) | — |
| 2025 | CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic | [arXiv](https://arxiv.org/abs/2505.20510) · [Paper](https://doi.org/10.52202/085713-3404) | — |
| 2025 | UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2505.21496) · [Paper](https://doi.org/10.52202/085713-5028) | [Code](https://github.com/Euphoria16/UI-Genie) |
| 2025 | VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning | [arXiv](https://arxiv.org/abs/2412.02172) · [Project](https://visco-benchmark.github.io/) | [Code](https://github.com/PlusLabNLP/VISCO) |

<a id="section-7-2"></a>

### 7.2. Future Directions

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | 3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis | [arXiv](https://arxiv.org/abs/2602.18064) · [Project](http://assistants.Code) | [Code](https://github.com/jinlab-imvr/3DMedAgent) |
| 2026 | Agentic Model Predictive Questioning Control in Visual Design | [Paper](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | AutoMat: Physics-Guided Agentic Reasoning for Solving Ill-Posed Inverse Microscopy Problems | [arXiv](https://arxiv.org/abs/2505.12650) · [Paper](https://openreview.net/forum?id=TLroFiKilA) | [Code](https://github.com/yyt-2378/AutoMat) |
| 2026 | CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework | [arXiv](https://arxiv.org/abs/2603.01607) · [Project](https://xypb.github.io/CARE-Project-Page/) | [Code](https://github.com/XYPB/CARE) |
| 2026 | CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations | [arXiv](https://arxiv.org/abs/2606.03435) | — |
| 2026 | FaSTA$^*$: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing | [arXiv](https://arxiv.org/abs/2506.20911) | [Code](https://github.com/tianyi-lab/FaSTAR) |
| 2026 | GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning | [arXiv](https://arxiv.org/abs/2601.18543) | Unavailable |
| 2026 | LensWalk: Agentic Video Understanding by Planning How You See in Videos | [arXiv](https://arxiv.org/abs/2603.24558) | — |
| 2026 | PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement | [arXiv](https://arxiv.org/abs/2602.14968) | — |
| 2026 | PSBench: Editing Image via GUI Agents in Photoshop | [Paper](https://openreview.net/forum?id=O93cZGxYB1) | [Code](https://github.com/zyn1216/PSBench) |
| 2026 | RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward | [arXiv](https://arxiv.org/abs/2602.17558) | — |
| 2026 | Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning | [arXiv](https://arxiv.org/abs/2512.20934) · [Project](https://transductive-visualprogram.github.io/) | [Code](https://github.com/transductive-visualprogram/tvp) |
| 2025 | Agentic Learner with Grow-and-Refine Multimodal Semantic Memory | [arXiv](https://arxiv.org/abs/2511.21678) · [Project](https://weihao-bo.github.io/ViLoMeo-page) | [Code](https://github.com/weihao-bo/ViLoMem) |
| 2025 | C-NAV: Towards Self-Evolving Continual Object Navigation in Open World | [arXiv](https://arxiv.org/abs/2510.20685) · [Paper](https://doi.org/10.52202/085713-4206) · [Project](https://bigtree765.github.io/C-Nav-project) | [Code](https://github.com/BigTree765/C-Nav) |
| 2025 | LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents | [arXiv](https://arxiv.org/abs/2505.22634) · [Paper](https://doi.org/10.52202/085713-1158) | — |
| 2025 | UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents | [arXiv](https://arxiv.org/abs/2505.21496) · [Paper](https://doi.org/10.52202/085713-5028) | [Code](https://github.com/Euphoria16/UI-Genie) |

<a id="section-8"></a>

## 8. Conclusion

References for this framing section are listed under their relevant topics in the catalogue.

<a id="section-A"></a>

## A. Additional Related References

| Year | Title | Paper | Code |
| :---: | --- | :---: | :---: |
| 2026 | Auditing Prospective Memory in Frozen Language-Model Systems: Causal Mechanisms and the Limits of Naturalistic Trigger Grounding | [Paper](https://www.preprints.org/manuscript/202608.1081) | — |

## Acknowledgements

The hierarchical table-of-contents and paper-table presentation is inspired by [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). The categories and bibliography here follow our own survey. Linked papers and software retain their respective authorship and licenses.

## Citation

Use [references.bib](references.bib) to cite the individual works. A citation for the survey will be added when its public bibliographic record is available.
