# Vision-agent reading list

[← Survey homepage](../README.md)

This companion catalogue collects work on visual-agent capabilities and harness infrastructure.

**195 selected papers** · **2024–2026** · **10 categories / 35 topics** · **110 papers with code**

An agent becomes vision-centric when visual observations shape what it inspects, reasons about, remembers, predicts, verifies, or does next. This collection emphasizes active image and video inspection, grounded GUI and robot actions, 3D reasoning, visual world models, and feedback from observed results.

**Selection policy.** We select recent works from the catalogue bibliography for a concrete visual mechanism or a benchmark that directly tests visual agents. Recent publication alone is insufficient. General text-agent frameworks, historical foundations, standalone model primitives, and broad datasets do not automatically enter the reading list. [Selection criteria and decisions](CURATION.md).

**Reading the tables.** The **Vision contribution** column explains why each paper belongs here. Papers appear once under their main contribution and are ordered by year, newest first, then title. There are no star or importance rankings. Years and venues follow the bibliography, so a 2024 conference paper may have an earlier preprint. A dash means no project/code link is recorded.

[📖 Catalogue bibliography](../references.bib) · [📦 Selected catalogue](../data/papers.json) · [🧭 Topic navigation](TOPICS.md) · [🔎 Sources and verification](COVERAGE.md)

Bibliography snapshot **2026-10-05** with **380 citation keys**.

## Suggested starting points

These entry points illustrate different visual mechanisms; they are editorial reading suggestions.

| Visual mechanism | Start here |
| --- | --- |
| Active visual search | [V*](https://doi.org/10.1109/cvpr52733.2024.01243) |
| Visual GUI grounding | [GUI-Actor](https://proceedings.neurips.cc/paper_files/paper/2025/hash/16130af940e9dabb43c726119bd3b42e-Abstract-Conference.html) |
| Thinking with images | [DeepEyes](https://arxiv.org/abs/2505.14362) |
| Executable visual reasoning | [PyVision](https://arxiv.org/abs/2507.07998) |
| Visual world models for control | [DreamZero](https://arxiv.org/abs/2602.15922) |
| Original visual evidence as memory | [VISTA (visual harness)](https://arxiv.org/abs/2610.02200) |
| Visual navigation with verified goals | [NavHarness (adaptive goals)](https://arxiv.org/abs/2609.39915) |
| Checking observed action effects | [VeriGUI](https://aclanthology.org/2026.acl-long.1335/) |
| Visual-agent evaluation | [VisualWebArena](https://arxiv.org/abs/2401.13649) |

## 📚 Table of Contents

- [Internal Capabilities of Vision-Centric Agents](#branch-internal)
  - [Vision Perception Capability](#category-perception)
    - [Grounded Perception](#topic-vision-perception-grounded) — 10 papers
    - [Temporal Perception](#topic-vision-perception-temporal) — 7 papers
    - [Spatial Perception](#topic-vision-perception-spatial) — 6 papers
  - [Vision Reasoning Capability](#category-reasoning)
    - [Interleaved Multimodal Reasoning](#topic-reasoning-interleaved) — 7 papers
    - [Visually Grounded Reasoning](#topic-reasoning-grounded) — 7 papers
    - [Tool-Augmented Visual Reasoning](#topic-reasoning-tool-augmented) — 6 papers
    - [Programmatic Visual Reasoning](#topic-reasoning-programmatic) — 6 papers
  - [Simulation of World Dynamics](#category-world)
    - [Video Simulation](#topic-simulation-video) — 8 papers
    - [Spatial Simulation](#topic-simulation-spatial) — 5 papers
    - [Latent Simulation](#topic-simulation-latent) — 5 papers
    - [Semantic Simulation](#topic-simulation-semantic) — 5 papers
  - [Visual Evaluation and Correction Abilities](#category-evaluation)
    - [Visual Evidence Evaluation](#topic-visual-evaluation-evidence) — 4 papers
    - [Visually Grounded Process Evaluation](#topic-visual-evaluation-process) — 4 papers
    - [Visual Outcome Evaluation](#topic-visual-evaluation-outcome) — 4 papers
    - [Visual-Based Self-Correction](#topic-visual-evaluation-self-correction) — 5 papers
  - [Evolving Abilities](#category-evolving)
    - [Visual Capability Gap Diagnosis](#topic-evolving-diagnosis) — 4 papers
    - [Visual Improvement Signal Generation](#topic-evolving-signals) — 5 papers
    - [Vision-Guided Optimization Adaptation](#topic-evolving-optimization) — 5 papers
    - [Self-Modification of Visual Interaction Infrastructure](#topic-evolving-infrastructure) — 6 papers
- [Harness Infrastructure for Vision-Centric Agents](#branch-external)
  - [Vision Planning and Orchestration Infrastructure](#category-planning)
    - [Task and Workflow Planning](#topic-planning-task-workflow) — 9 papers
    - [Trajectory Search and Deliberation](#topic-planning-trajectory-search) — 6 papers
    - [Multi-Agent Planning and Coordination](#topic-planning-multiagent-coordination) — 6 papers
  - [Vision Memory Infrastructure](#category-memory)
    - [Visual-to-Text](#topic-vision-memory-text) — 4 papers
    - [Visual Evidence Store](#topic-vision-memory-evidence) — 6 papers
    - [Visual Compression Layer](#topic-vision-memory-compression) — 5 papers
    - [Visual Experience Repository](#topic-vision-memory-experience) — 7 papers
  - [Visual Tools](#category-tools)
    - [Observation Tools](#topic-visual-tools-observation) — 5 papers
    - [Search Tools](#topic-visual-tools-search) — 5 papers
    - [Generation Tools](#topic-visual-tools-generation) — 7 papers
  - [Vision Verification Infrastructure](#category-verification)
    - [Evidence Verification](#topic-verification-evidence) — 3 papers
    - [Process Verification](#topic-verification-process) — 4 papers
    - [Outcome Verification](#topic-verification-outcome) — 7 papers
  - [Safety Infrastructure](#category-safety)
    - [Visual Information Safeguard](#topic-safety-visual-information) — 3 papers
    - [Safety-Constrained Execution](#topic-safety-constrained-execution) — 5 papers
    - [Runtime Oversight and Traceability](#topic-safety-runtime-oversight) — 4 papers

## 📑 Selected Papers

The catalogue groups papers by internal visual capabilities and harness infrastructure.

<a id="branch-internal"></a>

## Internal Capabilities of Vision-Centric Agents

<a id="category-perception"></a>

### Vision Perception Capability

<a id="topic-vision-perception-grounded"></a>

#### Grounded Perception

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICML | [ACTIVE-o3: Empowering MLLMs with active perception via pure reinforcement learning](https://proceedings.mlr.press/v306/zhu26bi.html) | Learn active perception through visual inspection actions | — |
| 2026 | ICLR | [UI-Ins: Enhancing GUI grounding with multi-perspective instruction as reasoning](https://arxiv.org/abs/2510.20286) | Multi-perspective visual reasoning for instruction grounding | [Code](https://github.com/alibaba/UI-Ins) |
| 2025 | NeurIPS | [GUI-Actor: Coordinate-free visual grounding for GUI agents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/16130af940e9dabb43c726119bd3b42e-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.03143) | Coordinate-free attention-based GUI grounding | [Code](https://github.com/microsoft/GUI-Actor) |
| 2025 | ICLR | [Navigating the digital world as humans do: Universal visual grounding for GUI agents](https://doi.org/10.48550/arxiv.2410.05243) · [arXiv](https://arxiv.org/abs/2410.05243) | Universal visual grounding across desktop and mobile interfaces | [Project](https://osu-nlp-group.github.io/UGround/) · [Code](https://github.com/OSU-NLP-Group/UGround) |
| 2025 | arXiv | [RSAgent: Learning to reason and act for text-guided segmentation via multi-turn tool invocations](https://arxiv.org/abs/2512.24023) | Iterative segmentation through visual tool calls | — |
| 2025 | Proc. ACM Int. Conf. Multimedia (MM) | [ScreenSpot-Pro: GUI grounding for professional high-resolution computer use](https://arxiv.org/abs/2504.07981) | Evaluate grounding on professional high-resolution screens | [Project](https://gui-agent.github.io/grounding-leaderboard) · [Code](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) |
| 2025 | CVPR | [ShowUI: One vision-language-action model for GUI visual agent](https://arxiv.org/abs/2411.17465) | Visual token selection and vision-language-action GUI control | [Code](https://github.com/showlab/ShowUI) |
| 2024 | CVPR | [CogAgent: A visual language model for GUI agents](https://arxiv.org/abs/2312.08914) | Screenshot understanding and visual GUI action grounding | [Code 1](https://github.com/zai-org/CogVLM) · [Code 2](https://github.com/zai-org/CogAgent) |
| 2024 | ACL | [SeeClick: Harnessing GUI grounding for advanced visual GUI agents](https://arxiv.org/abs/2401.10935) | Ground instructions to clickable screen coordinates | [Code](https://github.com/njucckevin/SeeClick) |
| 2024 | CVPR | [V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs](https://doi.org/10.1109/cvpr52733.2024.01243) · [arXiv](https://arxiv.org/abs/2312.14135) | Search image regions for fine-grained visual evidence | [Code](https://github.com/penghao-wu/vstar) |

<a id="topic-vision-perception-temporal"></a>

#### Temporal Perception

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [LensWalk: Agentic Video Understanding by Planning How You See in Videos](https://arxiv.org/abs/2603.24558) | Plan how to inspect video before answering | — |
| 2026 | ICLR | [VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](https://arxiv.org/abs/2503.13444) | Localize and verify temporal evidence with a video agent | [Project](https://videomind.github.io/) · [Code](https://github.com/yeliudev/VideoMind) |
| 2026 | ICLR | [VideoZoomer: Reinforcement-learned temporal focusing for long video reasoning](https://arxiv.org/abs/2512.22315) | Learn where to resample dense clips for temporal detail | [Code](https://github.com/zsgvivo/VideoZoomer) |
| 2025 | arXiv | [Agentic keyframe search for video question answering](https://arxiv.org/abs/2503.16032) | Agent-controlled keyframe search for video questions | [Code](https://github.com/fansunqi/AKeyS) |
| 2025 | arXiv | [VideoExplorer: Think with videos for agentic long-video understanding](https://arxiv.org/abs/2506.10821) | Explore video evidence through iterative tool use | [Code](https://github.com/RUC-NLPIR/VideoDeepResearch) |
| 2024 | arXiv | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852) | Use video observations to choose navigation actions | — |
| 2024 | ECCV | [VideoAgent: Long-Form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517) | Iteratively retrieve video evidence for long-form understanding | — |

<a id="topic-vision-perception-spatial"></a>

#### Spatial Perception

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ActiveVLA_Injecting_Active_Perception_into_Vision-Language-Action_Models_for_Precise_3D_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2601.08325) | Active viewpoint selection for precise 3D manipulation | — |
| 2026 | CVPR | [REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting](https://arxiv.org/abs/2510.16410) | Agentic reasoning, segmentation, and editing in Gaussian-splat scenes | [Project](https://ChangyueShi.github.io/REALM) · [Code](https://github.com/ChangyueShi/REALM-Code) |
| 2025 | arXiv | [Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception](https://arxiv.org/abs/2511.15279) | Control visual zoom and viewpoint for embodied perception | — |
| 2025 | arXiv | [SpatialVLA: Exploring spatial representations for visual-language-action model](https://arxiv.org/abs/2501.15830) | Encode spatial representations for visual robot actions | — |
| 2024 | arXiv | [RoboPoint: A vision-language model for spatial affordance prediction for robotics](https://arxiv.org/abs/2406.10721) | Predict spatial affordances from visual observations | — |
| 2024 | NeurIPS | [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189) | Build online 3D scene graphs for object navigation | [Project](https://bagh2178.github.io/SG-Nav/) · [Code](https://github.com/bagh2178/SG-Nav) |

<a id="category-reasoning"></a>

### Vision Reasoning Capability

<a id="topic-reasoning-interleaved"></a>

#### Interleaved Multimodal Reasoning

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [CodeV: Code with images for faithful visual reasoning via tool-aware policy optimization](https://arxiv.org/abs/2511.19661) | Interleave images and executable code for visual reasoning | [Code](https://github.com/RenlyH/CodeV) |
| 2026 | ICLR | [DeepEyes: Incentivizing"thinking with images" via reinforcement learning](https://arxiv.org/abs/2505.14362) | Interleave text reasoning with image crops and magnification | [Code](https://github.com/Visual-Agent/DeepEyes) |
| 2026 | ICLR | [DeepEyesV2: Toward Agentic Multimodal Model](https://arxiv.org/abs/2511.05271) | Combine multimodal reasoning with agentic tool interaction | [Project](https://visual-agent.github.io/) · [Code](https://github.com/Visual-Agent/DeepEyesV2) |
| 2026 | ECCV | [TIR-Bench: A Comprehensive Benchmark for Agentic Thinking-with-Images Reasoning](https://arxiv.org/abs/2511.01833) | Evaluate agentic thinking with images and visual tools | [Code](https://github.com/agents-x-project/TIR-Bench) |
| 2025 | NeurIPS | [Pixel Reasoner: Incentivizing pixel space reasoning via curiosity-driven reinforcement learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c38f54740062529aa4117a04b583f3c-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.15966) | Choose pixel-space inspection actions while reasoning | [Project 1](https://tiger-ai-lab.github.io/Pixel-Reasoner/) · [Project 2](https://huggingface.co/spaces/TIGER-Lab/Pixel-Reasoner) · [Code](https://github.com/TIGER-AI-Lab/Pixel-Reasoner) |
| 2025 | NeurIPS | [VideoChat-R1.5: Visual test-time scaling to reinforce multimodal reasoning by iterative perception](https://proceedings.neurips.cc/paper_files/paper/2025/hash/acb94e709f02895fd98b5867f0b184f3-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2509.21100) | Iterative perception for video reasoning at test time | — |
| 2024 | NeurIPS | [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://doi.org/10.52202/079017-4423) · [arXiv](https://arxiv.org/abs/2406.09403) | Interleave reasoning with generated visual sketches | [Project](https://visualsketchpad.github.io/) · [Code](https://github.com/Yushi-Hu/VisualSketchpad) |

<a id="topic-reasoning-grounded"></a>

#### Visually Grounded Reasoning

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICLR | [DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking](https://arxiv.org/abs/2507.20879) | Active visual perception and hybrid reasoning for driving | [Code](https://github.com/wczheng/DriveAgent-R1) |
| 2026 | arXiv | [GroundingVLN: Reasoning and Acting with Grounding for Vision-Language Navigation](https://arxiv.org/abs/2609.18581) | Ground navigation reasoning and actions in observed scenes | — |
| 2025 | ICRA | [BUMBLE: Unifying reasoning and acting with vision-language models for building-wide mobile manipulation](https://arxiv.org/abs/2410.06237) | Ground reasoning and actions in building-wide visual observations | [Project](https://robin-lab.cs.utexas.edu/BUMBLE/) · [Code](https://github.com/UT-Austin-RobIn/BUMBLE) |
| 2025 | CVPR | [SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Renz_SimLingo_Vision-Only_Closed-Loop_Autonomous_Driving_with_Language-Action_Alignment_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09594) | Align visual driving observations with language and actions | — |
| 2025 | arXiv | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | Generalize vision-language-action control to open-world tasks | — |
| 2024 | arXiv | [MOKA: Open-world robotic manipulation through mark-based visual prompting](https://arxiv.org/abs/2403.03174) | Convert mark-based visual prompts into robot actions | — |
| 2024 | arXiv | [ReKep: Spatio-temporal reasoning of relational keypoint constraints for robotic manipulation](https://arxiv.org/abs/2409.01652) | Plan manipulation using visual relational keypoint constraints | [Project](https://rekep-robot.github.io/) · [Code](https://github.com/huangwl18/ReKep) |

<a id="topic-reasoning-tool-augmented"></a>

#### Tool-Augmented Visual Reasoning

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICLR | [AdaReasoner: Dynamic tool orchestration for iterative visual reasoning](https://arxiv.org/abs/2601.18631) | Dynamically orchestrate tools for iterative visual reasoning | [Code](https://github.com/ssmisya/AdaReasoner) |
| 2025 | EMNLP | [LATTE: Learning to think with vision specialists](https://arxiv.org/abs/2412.05479) | Reason with vision specialists rather than a fixed image view | — |
| 2025 | ICML | [MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673) | Invoke chest X-ray specialists for image-grounded reasoning | [Code](https://github.com/bowang-lab/MedRAX) |
| 2025 | arXiv | [OpenThinkIMG: Learning to think with images via visual tool reinforcement learning](https://arxiv.org/abs/2505.08617) | Learn visual tool use through reinforcement learning | [Code](https://github.com/zhaochen0110/OpenThinkIMG) |
| 2025 | arXiv | [VisualToolAgent (VisTA): A reinforcement learning framework for visual tool selection](https://arxiv.org/abs/2505.20289) | Learn which visual inspection tool to select | — |
| 2024 | ECCV | [LLaVA-Plus: Learning to use tools for creating multimodal agents](https://arxiv.org/abs/2311.05437) | Learn to select and use visual specialist tools | — |

<a id="topic-reasoning-programmatic"></a>

#### Programmatic Visual Reasoning

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [Geometrically-Constrained Agent for Spatial Reasoning](https://arxiv.org/abs/2511.22659) | Apply geometric constraints in agentic spatial reasoning | [Project](https://gca-spatial-reasoning.github.io) · [Code](https://github.com/gca-spatial-reasoning/gca) |
| 2026 | ICLR | [Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning](https://arxiv.org/abs/2512.20934) | Evolve spatial reasoning tool libraries from experience | [Project](https://transductive-visualprogram.github.io/) · [Code](https://github.com/transductive-visualprogram/tvp) |
| 2025 | arXiv | [PyVision: Agentic vision with dynamic tooling](https://arxiv.org/abs/2507.07998) | Create executable inspection tools for visual evidence on demand | [Code](https://github.com/agents-x-project/PyVision) |
| 2025 | CVPR | [ViUniT: Visual unit tests for more robust visual programming](https://arxiv.org/abs/2412.08859) | Test visual programs with image-answer unit tests | [Code](https://github.com/SalesforceAIResearch/visual-unit-testing) |
| 2024 | ICML | [SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code](https://arxiv.org/abs/2403.01248) | Generate Blender scene code and inspect rendered 3D layouts | — |
| 2024 | EMNLP Findings | [VDebugger: Harnessing execution feedback for debugging visual programs](https://arxiv.org/abs/2406.13444) | Debug visual programs using stepwise execution feedback | [Code](https://github.com/shirley-wu/vdebugger/) |

<a id="category-world"></a>

### Simulation of World Dynamics

<a id="topic-simulation-video"></a>

#### Video Simulation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998) | Couple causal visual world modeling with robot control | [Code](https://github.com/robbyant/lingbot-va) |
| 2026 | arXiv | [Computer-Using World Model](https://arxiv.org/abs/2602.17365) | Predict post-action screen states for computer-use planning | — |
| 2026 | arXiv | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) | Fine-tune video models for visuomotor control and planning | — |
| 2026 | ICLR | [ViMo: A Generative Visual GUI World Model for App Agents](https://proceedings.iclr.cc/paper_files/paper/2026/hash/beb0f70e479c495f1903ffdea40adef6-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2504.13936) | Model future visual GUI states for app interaction | [Project](https://ai-agents-2030.github.io/ViMo/) · [Code](https://github.com/ai-agents-2030/ViMo) |
| 2026 | arXiv | [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | Turn action-conditioned video prediction into robot policies | — |
| 2025 | arXiv | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) | Control video world-model rollouts for manipulation | — |
| 2025 | arXiv | [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539) | Couple predicted visual states with autoregressive robot actions | — |
| 2024 | ICML | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | Generate action-conditioned interactive visual environments | [Project](https://sites.google.com/corp/view/genie-2024/) |

<a id="topic-simulation-spatial"></a>

#### Spatial Simulation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Beyond Pixel Histories: World Models with Persistent 3D State](https://arxiv.org/abs/2603.03482) | Predict with persistent 3D state beyond pixel histories | — |
| 2026 | arXiv | [ContactGaussian-WM: Learning Physics-Grounded World Model from Videos](https://arxiv.org/abs/2602.11021) | Learn physics-grounded scene dynamics from video | — |
| 2025 | NeurIPS | [Learning 3D persistent embodied world models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/970f59b22f4c72aec75174aae63c7459-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.05495) | Maintain persistent 3D state for embodied world modeling | — |
| 2025 | arXiv | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973) | Reconstruct deformable objects and simulate their physical behavior | — |
| 2024 | arXiv | [DOME: Taming Diffusion Model into High-Fidelity Controllable Occupancy World Model](https://arxiv.org/abs/2410.10429) | Predict controllable 3D occupancy for driving scenes | — |

<a id="topic-simulation-latent"></a>

#### Latent Simulation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519) | Post-train robot actions with predictive visual latent world models | — |
| 2026 | arXiv | [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) | Align visual latent dynamics with driving actions | [Code](https://github.com/liulin815/DriveWorld-VLA) |
| 2025 | Nature | [Mastering Diverse Control Tasks through World Models](https://www.nature.com/articles/s41586-025-08744-2) · [arXiv](https://arxiv.org/abs/2301.04104) | Learn pixel-based control through latent imagined rollouts | [Code](https://github.com/danijar/dreamerv3) |
| 2025 | arXiv | [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/abs/2506.09985) | Predict in visual latent space for robot planning | [Code](https://github.com/facebookresearch/vjepa2) |
| 2024 | arXiv | [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983) | Plan with world models over pretrained visual features | — |

<a id="topic-simulation-semantic"></a>

#### Semantic Simulation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | Predict GUI states through renderable code | — |
| 2026 | arXiv | [MobileDreamer: Generative Sketch World Model for GUI Agent](https://arxiv.org/abs/2601.04035) | Forecast spatial GUI element sketches for lookahead actions | — |
| 2025 | arXiv | [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) | Evaluate semantic state transitions for mobile GUI agents | — |
| 2025 | arXiv | [Planning with reasoning using vision language world model](https://arxiv.org/abs/2509.02722) | Plan with a vision-language model of environment dynamics | — |
| 2025 | NeurIPS | [VAGEN: Reinforcing world model reasoning for multi-turn VLM agents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fc6688d75adde86b9df910769c1d02e3-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2510.16907) | Reinforce world-state reasoning in multi-turn visual interaction | [Project](https://vagen-ai.github.io) · [Code](https://github.com/mll-lab-nu/VAGEN) |

<a id="category-evaluation"></a>

### Visual Evaluation and Correction Abilities

<a id="topic-visual-evaluation-evidence"></a>

#### Visual Evidence Evaluation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization](https://arxiv.org/abs/2602.14098) | Inspect forensic image traces for grounded authenticity reasoning | [Code](https://github.com/youqiwong/ForgeryVCR) |
| 2026 | arXiv | [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) | Detect perception errors with visual process reward models | [Code](https://github.com/RUCAIBox/Perceval) |
| 2026 | ECCV | [Reflect-R1: Evidence-driven reflection for self-correction in long video understanding](https://arxiv.org/abs/2606.27922) | Reflect on localized evidence to correct long-video answers | [Code](https://github.com/ShuimuChen-hyq/Reflect-R1) |
| 2025 | CVPR | [VISCO: Benchmarking Fine-Grained Critique and Correction Towards Self-Improvement in Visual Reasoning](https://arxiv.org/abs/2412.02172) | Critique perceptual errors and revisit supporting image evidence | [Project](https://visco-benchmark.github.io/) · [Code](https://github.com/PlusLabNLP/VISCO) |

<a id="topic-visual-evaluation-process"></a>

#### Visually Grounded Process Evaluation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) | Judge whether computer actions match the intended workflow | — |
| 2026 | ECCV | [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525) | Compare visual states to reward GUI action progress | — |
| 2025 | NeurIPS | [GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior](https://proceedings.neurips.cc/paper_files/paper/2025/hash/937ae0e83eb08d2cb8627fe1def8c751-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.08012) | Learn reflection over multimodal GUI action trajectories | [Project](https://penghao-wu.github.io/GUI_Reflection/) · [Code](https://github.com/penghao-wu/GUI_Reflection) |
| 2024 | arXiv | [AHA: A vision-language-model for detecting and reasoning over failures in robotic manipulation](https://arxiv.org/abs/2410.00371) | Detect and explain robot failures from visual observations | [Project](https://aha-vlm.github.io/) · [Code](https://github.com/NVlabs/AHA/tree/main) |

<a id="topic-visual-evaluation-outcome"></a>

#### Visual Outcome Evaluation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICLR | [PerfGuard: A Performance-Aware Agent for Visual Content Generation](https://openreview.net/forum?id=tdN42GTv4S) · [arXiv](https://arxiv.org/abs/2601.22571) | Evaluate visual generation against requested performance constraints | [Project](https://openreview.net/forum?id=tdN42GTv4S) · [Code](https://github.com/FelixChan9527/PerfGuard) |
| 2026 | ICLR | [ProRe: A Proactive Reward System for GUI Agents via Reasoner--Actor Collaboration](https://arxiv.org/abs/2509.21823) | Actively probe GUI states when completion evidence is insufficient | [Code](https://github.com/V-Droid-Agent/ProRe) |
| 2025 | arXiv | [EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing](https://arxiv.org/abs/2509.13399) | Judge edit compliance, content preservation, and visual quality | [Code](https://github.com/TianyuCodings/EdiVal) |
| 2025 | CVPR | [LLaVA-Critic: Learning to Evaluate Multimodal Models](https://arxiv.org/abs/2410.02712) | Learn visual judgments for multimodal model outputs | [Project](https://llava-vl.github.io/blog/2024-10-03-llava-critic) · [Code](https://github.com/LLaVA-VL/LLaVA-NeXT) |

<a id="topic-visual-evaluation-self-correction"></a>

#### Visual-Based Self-Correction

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [CycleVLA: Proactive self-correcting vision-language-action models via subtask backtracking and minimum Bayes risk decoding](https://arxiv.org/abs/2601.02295) | Recover manipulation through visually grounded subtask backtracking | [Project](https://dannymcy.github.io/cyclevla/) · [Code](https://github.com/dannymcy/cyclevla_code) |
| 2026 | ACL | [Don’t act blindly: Robust GUI automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | Compare intended and observed GUI action effects before repair | — |
| 2026 | arXiv | [IMAGAgent: Orchestrating Multi-Turn Image Editing via Constraint-Aware Planning and Reflection](https://arxiv.org/abs/2603.29602) | Reflect on intermediate images to repair constrained edits | [Code](https://github.com/hackermmzz/IMAGAgent) |
| 2025 | CVPR | [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588) | Reflect on motion to correct fine-grained robotic actions | [Code](https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework) |
| 2025 | Proc. Conf. Nations Americas Chapter Assoc. Comput. Linguistics: Hum. Lang. Technol. (NAACL-HLT), vol. 1, Long Papers | [Vision-language models can self-improve reasoning via reflection](https://arxiv.org/abs/2411.00855) | Improve visual reasoning through reflection on image-grounded answers | [Code](https://github.com/njucckevin/MM-Self-Improve) |

<a id="category-evolving"></a>

### Evolving Abilities

<a id="topic-evolving-diagnosis"></a>

#### Visual Capability Gap Diagnosis

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://arxiv.org/abs/2605.22816) | Diagnose navigation uncertainty through self-aware visual reasoning | [Project](https://gwxuan.github.io/AwareVLN/) · [Code](https://github.com/GWxuan/AwareVLN) |
| 2026 | arXiv | [Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents](https://arxiv.org/abs/2609.17653) | Diagnose GUI skill failures and revise reusable procedures | [Code](https://github.com/ZJU-REAL/EvoSkill-GUI) |
| 2026 | ACL | [RoboFailRing: Retrieval-Augmented and Language Grounding Failure Detection for VLM-enabled Robotic Manipulation](https://aclanthology.org/2026.acl-long.602/) | Retrieve visually grounded robot failure cases for diagnosis | [Code](https://github.com/DynamicPoet/RoboFailRing) |
| 2026 | CVPR | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) | Learn driving improvements from observed action failures | — |

<a id="topic-evolving-signals"></a>

#### Visual Improvement Signal Generation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605) | Distill contrasted image-generation experience into improvement signals | [Project](https://ephemeral182.github.io/GenEvolve/) · [Code](https://github.com/MeiGen-AI/GenEvolve) |
| 2026 | arXiv | [V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution](https://arxiv.org/abs/2609.34682) | Co-evolve visual reasoning skills and training data | — |
| 2026 | arXiv | [VLAW: Iterative co-improvement of vision-language-action policy and world model](https://arxiv.org/abs/2602.12063) | Co-improve robot policies and visual world models | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2025 | NeurIPS | [UI-Genie: A Self-Improving Approach for Iteratively Boosting MLLM-based Mobile GUI Agents](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dd1577afd396928ed64216f3f1fd5556-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.21496) | Iteratively improve GUI agents with learned critic feedback | [Code](https://github.com/Euphoria16/UI-Genie) |
| 2025 | arXiv | [Video2policy: Scaling up manipulation tasks in simulation through Internet videos](https://arxiv.org/abs/2502.09886) | Use visual internet demonstrations to expand robot training tasks | — |

<a id="topic-evolving-optimization"></a>

#### Vision-Guided Optimization Adaptation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | Adapt object navigation with preflection and evolving visual memory | — |
| 2026 | ECCV | [EvoVLA: Self-evolving vision-language-action model](https://arxiv.org/abs/2511.16166) | Evolve robot vision-language-action policies | [Project](https://aigeeksgroup.github.io/EvoVLA) · [Code](https://github.com/AIGeeksGroup/EvoVLA) |
| 2026 | ICLR | [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b6aaffec941f98930753fa6d6de7263-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2509.18119) | Online reinforcement learning for mobile visual GUI interaction | [Code](https://github.com/THUDM/MobileRL) |
| 2026 | ICLR | [Self-improving vision-language-action models with data generation via residual RL](https://arxiv.org/abs/2511.00091) | Improve VLA manipulation using residual-RL-generated data | — |
| 2026 | ICLR | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6605c7d1c1ae1521b328d036df5be1ae-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2511.09515) | Optimize VLA policies with visual world-model rollouts | [Project](https://wm-po.github.io) · [Code](https://github.com/WM-PO/WMPO) |

<a id="topic-evolving-infrastructure"></a>

#### Self-Modification of Visual Interaction Infrastructure

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [COMFYCLAW: Self-evolving skill harnesses for image generation workflows](https://arxiv.org/abs/2607.01709) | Evolve executable skills for image-generation workflows | [Code](https://github.com/Moms-Organic-Agent-Lab/comfyclaw) |
| 2026 | arXiv | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | Evolve robot programs and collect improved visual rollout data | — |
| 2026 | arXiv | [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | Gate robot harness updates with execution evidence | — |
| 2026 | arXiv | [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326) | Co-evolve procedural scaffolds and multimodal reasoning policies | — |
| 2026 | arXiv | [VideoHarness-RSI: Recursive Harness Self-Improvement for Long-Video Understanding with Frozen Vision-Language Models](https://arxiv.org/abs/2608.24302) | Evolve long-video harnesses with frozen vision-language models | [Code](https://github.com/Tencent/VideoHarness-RSI) |
| 2026 | arXiv | [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664) | Improve the tool design used to inspect long videos | — |

<a id="branch-external"></a>

## Harness Infrastructure for Vision-Centric Agents

<a id="category-planning"></a>

### Vision Planning and Orchestration Infrastructure

<a id="topic-planning-task-workflow"></a>

#### Task and Workflow Planning

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](https://arxiv.org/abs/2609.15195) | Orchestrate training-free visual navigation through an agent harness | — |
| 2026 | arXiv | [Qwen-CUA: Native Computer Use for (almost) Everything](https://arxiv.org/abs/2608.02352) | Native visual computer use across task environments | — |
| 2026 | arXiv | [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389) | Augment robot perception to support long-horizon task execution | — |
| 2026 | arXiv | [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) | Organize long-horizon robotic tasks with agentic execution | [Code](https://github.com/RoboClaw-Robotics/RoboClaw) |
| 2026 | arXiv | [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | Coordinate robot policies with VLM observations and feedback | [Project](https://showlab.github.io/Show-Harness) · [Code](https://github.com/showlab/Show-Harness) |
| 2025 | arXiv | [Agent S2: A compositional generalist-specialist framework for computer use agents](https://arxiv.org/abs/2504.00906) | Coordinate visual GUI specialists for computer-use workflows | [Code](https://github.com/simular-ai/Agent-S) |
| 2025 | ICML | [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html) · [arXiv](https://arxiv.org/abs/2412.04454) | Execute GUI workflows through pure visual observations | [Project](https://aguvis-project.github.io/) · [Code](https://github.com/xlang-ai/aguvis) |
| 2025 | NeurIPS | [OpenCUA: Open Foundations for Computer-Use Agents](https://proceedings.neurips.cc/paper_files/paper/2025/file/cc7ae529e945226b0d52ea4ac478c4f3-Paper-Conference.pdf) · [arXiv](https://arxiv.org/abs/2508.09123) | Open visual computer-use models, trajectories, and training foundations | [Project](https://opencua.xlang.ai/) · [Code](https://github.com/xlang-ai/OpenCUA) |
| 2025 | arXiv | [UI-TARS: Pioneering automated GUI interaction with native agents](https://arxiv.org/abs/2501.12326) | Ground multi-step native GUI interaction in screen observations | — |

<a id="topic-planning-trajectory-search"></a>

#### Trajectory Search and Deliberation

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Agent alpha: Tree search unifying generation, exploration and evaluation for computer-use agents](https://arxiv.org/abs/2602.02995) | Search computer-use trajectories with generation and evaluation | — |
| 2026 | ICLR | [GTA1: GUI test-time scaling agent](https://arxiv.org/abs/2507.05791) | Scale GUI action selection through test-time search | [Code](https://github.com/Yan98/GTA1) |
| 2026 | arXiv | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | Deliberate over world-action predictions before robot execution | — |
| 2025 | CVPR | [Navigation World Models](https://arxiv.org/abs/2412.03572) | Imagine navigation observations to evaluate future routes | [Project](https://www.amirbar.net/nwm/) · [Code](https://github.com/facebookresearch/nwm/) |
| 2025 | arXiv | [STORM: Search-Guided Generative World Models for Robotic Manipulation](https://arxiv.org/abs/2512.18477) | Search predicted visual futures for robotic manipulation | — |
| 2024 | ICML | [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://proceedings.mlr.press/v235/nasiriany24a.html) · [arXiv](https://arxiv.org/abs/2402.07872) | Iteratively compare visually prompted robot action candidates | [Project 1](http://pivot-prompt.github.io) · [Project 2](https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo) |

<a id="topic-planning-multiagent-coordination"></a>

#### Multi-Agent Planning and Coordination

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [A Multi-Agent Perception-Action Alliance for Efficient Long Video Reasoning](https://arxiv.org/abs/2603.14052) | Coordinate perception and action agents for video reasoning | [Code](https://github.com/git-disl/A4VL) |
| 2026 | ACL | [LongVideoAgent: Multi-agent reasoning with long videos](https://arxiv.org/abs/2512.20618) | Coordinate agents to reason over long-video evidence | [Project](https://longvideoagent.github.io/) · [Code](https://github.com/longvideoagent/LongVideoAgent) |
| 2026 | arXiv | [MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization](https://arxiv.org/abs/2609.30609) | Coordinate shot conditions and policies for consistent video generation | — |
| 2026 | arXiv | [NavHarness: Adaptive Goals for Agentic Vision-Language Navigation](https://arxiv.org/abs/2609.39915) | Coordinate goals, visual navigation, verification, and memory agents | — |
| 2026 | ECCV | [VERITAS: A Multi-agent Co-scientist for Verifiable Image-Derived Hypothesis Testing](https://arxiv.org/abs/2604.12144) | Coordinate verifiable image-derived scientific hypothesis testing | [Code](https://github.com/LucZot/veritas) |
| 2024 | arXiv | [AutoRT: Embodied foundation models for large scale orchestration of robotic agents](https://arxiv.org/abs/2401.12963) | Orchestrate robotic agents using scene observations and constraints | — |

<a id="category-memory"></a>

### Vision Memory Infrastructure

<a id="topic-vision-memory-text"></a>

#### Visual-to-Text

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Vision-Language-Action Autonomous Driving Agent with Language-based Memory](https://arxiv.org/abs/2609.38641) | Use language-based memory inside visually grounded driving control | — |
| 2026 | arXiv | [What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612) | Track the current workflow role and status of GUI-observed values | — |
| 2024 | ECCV | [VideoAgent: A memory-augmented multimodal agent for video understanding](https://arxiv.org/abs/2403.11481) | Turn observed video content into searchable memory for reasoning | [Project](http://videoagent.github.io) · [Code](https://github.com/YueFan1014/VideoAgent) |
| 2024 | NeurIPS | [VLM Agents Generate Their Own Memories: Distilling Experience into Embodied Programs of Thought](https://doi.org/10.52202/079017-2418) · [arXiv](https://arxiv.org/abs/2406.14596) | Distill visual action experience into embodied programs of thought | [Project](https://ical-learning.github.io/) · [Code](https://github.com/Gabesarch/ICAL) |

<a id="topic-vision-memory-evidence"></a>

#### Visual Evidence Store

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ECCV | [Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding](https://arxiv.org/abs/2608.07663) | Retrieve multimodal episodic evidence for ultra-long video questions | [Project](https://choi-yeeun.github.io/MERIT/) · [Code](https://github.com/choi-yeeun/MERIT) |
| 2026 | arXiv | [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](https://arxiv.org/abs/2608.01543) | Route memory retrieval across visual and other modalities | — |
| 2026 | arXiv | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | Construct and repair evidence-grounded long-video memories | — |
| 2026 | arXiv | [VISTA: A Visual Harness for Reasoning in an Interactive World](https://arxiv.org/abs/2610.02200) | Preserve original observations and actively retrieve visual details | [Project](https://vista-research.github.io/) · [Code](https://github.com/joshhhhhan/VISTA) |
| 2026 | CVPR | [WorldMM: Dynamic Multimodal Memory Agent for Long Video Reasoning](https://arxiv.org/abs/2512.02425) | Retrieve dynamic multimodal memory for long-video reasoning | [Project](https://worldmm.github.io) · [Code](https://github.com/wgcyeo/WorldMM) |
| 2025 | ICCV | [Embodied VideoAgent: Persistent memory from egocentric videos and embodied sensors enables dynamic scene understanding](https://arxiv.org/abs/2501.00358) | Store object-centered video, depth, and pose evidence persistently | [Project](https://embodied-videoagent.github.io/) · [Code](https://github.com/Embodied-VideoAgent/embodied-videoagent) |

<a id="topic-vision-memory-compression"></a>

#### Visual Compression Layer

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511) | Merge long-video multimodal context hierarchically | [Project](https://clare-nie.github.io/Light-Omni) · [Code](https://github.com/Clare-Nie/Light-Omni) |
| 2026 | arXiv | [Screenshots or Tools? Eliciting Tool Use and Managing Multimodal Context in Hybrid GUI-MCP Computer-Use Agents](https://arxiv.org/abs/2608.03327) | Manage screenshot context when mixing GUI and MCP tools | — |
| 2025 | ICCV | [Less is more: Empowering GUI agent with context-aware simplification](https://arxiv.org/abs/2507.03730) | Prune screenshot elements and compress GUI interaction history | — |
| 2025 | arXiv | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://arxiv.org/abs/2507.05240) | Reduce historical visual context during streaming navigation | — |
| 2025 | NeurIPS | [VLA-Cache: Efficient vision-language-action manipulation via adaptive token caching](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f062da1973ac9ac61fc6d44dd7fa309f-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2502.02175) | Reuse computation for visually unchanged VLA tokens | — |

<a id="topic-vision-memory-experience"></a>

#### Visual Experience Repository

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [Hybrid self-evolving structured memory for GUI agents](https://arxiv.org/abs/2603.10291) | Update structured memory through visual GUI experience | [Code](https://github.com/NickSiboZhu/HyMEM-GUI-Agent) |
| 2026 | arXiv | [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652) | Learn multimodal memory control for long-horizon GUI tasks | — |
| 2026 | arXiv | [NavHarness: Towards Lifelong Embodied Navigation](https://arxiv.org/abs/2609.34276) | Consolidate maps and corrected visual search experience across tasks | — |
| 2026 | arXiv | [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749) | Learn memory retention from robot rollout outcomes | — |
| 2026 | arXiv | [RoboHarness: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation](https://arxiv.org/abs/2603.24060) | Adapt frozen VLA policies with retrieved success and failure experience | [Code](https://github.com/LZY-1021/RoboHarness) |
| 2026 | arXiv | [UI-Mem: Self-evolving experience memory for online reinforcement learning in mobile GUI agents](https://arxiv.org/abs/2602.05832) | Accumulate reusable GUI workflows and subtask experience | [Project](https://ui-mem.github.io) |
| 2025 | arXiv | [ViReSkill: Vision-grounded replanning with skill memory for llm-based planning in lifelong robot learning](https://arxiv.org/abs/2509.24219) | Reuse visually grounded plans and skills for robot replanning | — |

<a id="category-tools"></a>

### Visual Tools

<a id="topic-visual-tools-observation"></a>

#### Observation Tools

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICML | [3DMedAgent: Unified Perception-to-Understanding for 3D Medical Analysis](https://proceedings.mlr.press/v306/wang26o.html) · [arXiv](https://arxiv.org/abs/2602.18064) | Connect 3D medical perception tools with agentic understanding | [Project](http://assistants.Code) · [Code](https://github.com/jinlab-imvr/3DMedAgent) |
| 2025 | NeurIPS | [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://doi.org/10.52202/085713-3404) · [arXiv](https://arxiv.org/abs/2505.20510) | Inspect high-resolution pathology regions through agentic visual analysis | — |
| 2024 | CVPR | [CLOVA: A Closed-LOop Visual Assistant with Tool Usage and Update](https://arxiv.org/abs/2312.10908) | Inspect images with tools and update the visual assistant | [Code](https://github.com/clova-tool/CLOVA-tool) |
| 2024 | arXiv | [Mobile-Agent: Autonomous multi-modal mobile device agent with visual perception](https://arxiv.org/abs/2401.16158) | Combine OCR and icon detection for screen-based mobile actions | [Code](https://github.com/X-PLUG/MobileAgent) |
| 2024 | NeurIPS | [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://doi.org/10.52202/079017-3512) · [arXiv](https://arxiv.org/abs/2407.18035) | Diagnose image degradation and orchestrate restoration tools | — |

<a id="topic-visual-tools-search"></a>

#### Search Tools

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ICLR | [InSight-o3: Empowering Multimodal Foundation Models with Generalized Visual Search](https://arxiv.org/abs/2512.18745) | Generalize active visual search in multimodal reasoning | [Code](https://github.com/m-Just/InSight-o3) |
| 2026 | ICML | [Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models](https://proceedings.mlr.press/v306/huang26bx.html) | Train multimodal deep research with visual evidence acquisition | — |
| 2026 | ICLR | [Webwatcher: Breaking new frontiers of vision-language deep research agent](https://arxiv.org/abs/2508.05748) | Coordinate visual and textual search for multimodal research | — |
| 2025 | arXiv | [MMSearch-R1: Incentivizing LMMs to search](https://arxiv.org/abs/2506.20670) | Learn when to acquire image and text search evidence | [Code](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) |
| 2025 | arXiv | [World-To-Image: Grounding Text-to-Image Generation with Agent-Driven World Knowledge](https://arxiv.org/abs/2510.04201) | Retrieve visual world knowledge to support image generation | [Code](https://github.com/mhson-kyle/World-To-Image) |

<a id="topic-visual-tools-generation"></a>

#### Generation Tools

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | ECCV | [GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning](https://arxiv.org/abs/2601.18543) | Use multimodal reasoning to coordinate text-to-image generation | [Code](https://github.com/deep-kaixun/GenAgent) |
| 2026 | ICML | [LiveFigure: Generating Editable Scientific Illustration with VLM Agents](https://proceedings.mlr.press/v306/shao26f.html) · [arXiv](https://arxiv.org/abs/2605.23527) | Generate editable scientific illustrations with visual agents | [Code](https://github.com/tsinghua-fib-lab/LiveFigure) |
| 2026 | arXiv | [OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning](https://arxiv.org/abs/2609.16057) | Learn symbolic policies for visual generation workflows | — |
| 2026 | ICML | [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://proceedings.mlr.press/v306/pfaff26a.html) · [arXiv](https://arxiv.org/abs/2602.09153) | Generate simulation-ready indoor scenes through agentic authoring | [Project](https://scenesmith.github.io/) · [Code](https://github.com/nepfaff/scenesmith) |
| 2026 | arXiv | [ViMax: Agentic Video Generation](https://arxiv.org/abs/2606.07649) | Plan and generate multi-scene videos with agentic workflows | [Code](https://github.com/HKUDS/ViMax) |
| 2025 | NeurIPS | [SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent](https://doi.org/10.52202/085713-4689) · [arXiv](https://arxiv.org/abs/2509.20414) | Synthesize 3D scenes with an extensible, reflective agent | [Project](https://scene-weaver.github.io/) · [Code](https://github.com/Scene-Weaver/SceneWeaver) |
| 2024 | NeurIPS | [GenArtist: Multimodal LLM as an agent for unified image generation and editing](https://arxiv.org/abs/2407.05600) | Inspect intermediate images while orchestrating generation and editing | [Project](https://zhenyuw16.github.io/GenArtist_page) · [Code](https://github.com/zhenyuw16/GenArtist) |

<a id="category-verification"></a>

### Vision Verification Infrastructure

<a id="topic-verification-evidence"></a>

#### Evidence Verification

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [ARM-Thinker: Reinforcing multimodal generative reward models with agentic tool use and visual reasoning](https://arxiv.org/abs/2512.05111) | Ground reward judgments with crops and document evidence | — |
| 2026 | ICLR | [CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework](https://arxiv.org/abs/2603.01607) | Link multimodal medical reasoning to accountable evidence checks | [Project](https://xypb.github.io/CARE-Project-Page/) · [Code](https://github.com/XYPB/CARE) |
| 2026 | ICLR | [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435) | Ground cellular morphology reasoning in visual profiling evidence | — |

<a id="topic-verification-process"></a>

#### Process Verification

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [OS-Oracle: A comprehensive framework for cross-platform GUI critic models](https://arxiv.org/abs/2512.16295) | Critique proposed GUI actions before execution | [Code](https://github.com/numbmelon/OS-Oracle) |
| 2026 | ICLR | [OSWorld-MCP: Benchmarking MCP Tool Invocation in Computer-Use Agents](https://proceedings.iclr.cc/paper_files/paper/2026/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2510.24563) | Evaluate tool invocation in visually grounded computer-use workflows | [Project](https://osworld-mcp.github.io) · [Code](https://github.com/X-PLUG/OSWorld-MCP) |
| 2025 | CVPR | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | Monitor tracked geometry with executable visual constraint checks | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2025 | CoRL Workshops | [Guardian: Detecting robotic planning and execution errors with vision-language models](https://openreview.net/forum?id=wps46mtC9B) · [arXiv](https://arxiv.org/abs/2512.01946) | Separate robot planning errors from visually observed execution errors | [Project](https://openreview.net/forum?id=wps46mtC9B) · [Code](https://github.com/paulpacaud/Guardian-FailCot) |

<a id="topic-verification-outcome"></a>

#### Outcome Verification

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf) · [arXiv](https://arxiv.org/abs/2510.13626) | Stress-test visual-language-action robustness under perturbations | [Code](https://github.com/sylvestf/LIBERO-plus) |
| 2026 | ICLR | [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897) | Evaluate multimodal scientific workflow completion | [Project](https://qiushisun.github.io/ScienceBoard-Home/) · [Code](https://github.com/OS-Copilot/ScienceBoard) |
| 2025 | ICLR | [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/01a83bc2f2732a58e6aa731e659e7101-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2405.14573) | Verify mobile task completion through device-state checks | [Code](https://github.com/google-research/android_world) |
| 2025 | CVPR | [ComfyBench: Benchmarking LLM-based Agents in ComfyUI for Autonomously Designing Collaborative AI Systems](https://arxiv.org/abs/2409.01392) | Evaluate executable ComfyUI workflows assembled by agents | [Code](https://github.com/xxyQwQ/ComfyBench) |
| 2025 | ICML | [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560) | Evaluate vision-driven embodied agents across action environments | [Project](https://embodiedbench.github.io) · [Code](https://github.com/EmbodiedBench/EmbodiedBench) |
| 2024 | NeurIPS | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972) | Verify real computer task completion with execution-based evaluators | [Project](https://os-world.github.io) · [Code](https://github.com/xlang-ai/OSWorld) |
| 2024 | ACL | [VisualWebArena: Evaluating multimodal agents on realistic visual web tasks](https://arxiv.org/abs/2401.13649) | Evaluate agents on tasks requiring visual web evidence | — |

<a id="category-safety"></a>

### Safety Infrastructure

<a id="topic-safety-visual-information"></a>

#### Visual Information Safeguard

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | arXiv | [MINIM: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization](https://arxiv.org/abs/2606.13949) | Sanitize sensitive screen content before remote agent inference | [Code](https://github.com/yyyyhx/MINIM) |
| 2026 | ICLR | [VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents](https://arxiv.org/abs/2506.02456) | Test malicious instructions embedded in rendered GUI observations | [Code](https://github.com/cua-framework/agents) |
| 2025 | NeurIPS | [WASP: Benchmarking web agent security against prompt injection attacks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1c9818387f5dd0a0bc151214660f059d-Abstract-Datasets_and_Benchmarks_Track.html) · [arXiv](https://arxiv.org/abs/2504.18575) | Evaluate prompt injection through web-agent observations | [Code](https://github.com/facebookresearch/wasp) |

<a id="topic-safety-constrained-execution"></a>

#### Safety-Constrained Execution

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | IEEE Robot. Autom. Lett. | [Safety guardrails for LLM-enabled robots](https://arxiv.org/abs/2503.07885) | Enforce grounded robot plan constraints with safety guards | [Project](https://robo-guard.github.io/) · [Code](https://github.com/KumarRobotics/RoboGuard) |
| 2025 | arXiv | [Magentic-UI: Towards human-in-the-loop agentic systems](https://arxiv.org/abs/2507.22358) | Combine visual computer use with action guards and human control | [Code](https://github.com/microsoft/magentic-ui/tree/magentic-ui-0.1) |
| 2025 | arXiv | [RoboChemist: Long-horizon and safety-compliant robotic chemical experimentation](https://arxiv.org/abs/2509.08820) | Enforce experiment protocols during embodied chemical tasks | [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) |
| 2025 | IROS | [Robots that suggest safe alternatives](https://arxiv.org/abs/2409.09883) | Propose feasible robot alternatives when requested actions are unsafe | — |
| 2025 | NeurIPS | [SafeVLA: Towards safety alignment of vision-language-action model via constrained learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2503.03480) | Align vision-language-action policies with execution constraints | [Project](https://pku-safevla.github.io) · [Code](https://github.com/PKU-Alignment/SafeVLA) |

<a id="topic-safety-runtime-oversight"></a>

#### Runtime Oversight and Traceability

| Year | Venue | Paper | Vision contribution | Project / Code |
| :---: | :---: | --- | --- | :---: |
| 2026 | CVPR | [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697) | Evaluate embodied-agent behavior under hazardous instructions | — |
| 2025 | arXiv | [Can we detect failures without failure data? uncertainty-aware runtime failure detection for imitation learning policies](https://arxiv.org/abs/2503.08558) | Calibrate runtime failure signals from robot execution data | — |
| 2025 | Proc. Conf. Nations Americas Chapter Assoc. Comput. Linguistics: Hum. Lang. Technol. (NAACL-HLT), Syst. Demonstrations | [CowPilot: A framework for autonomous and human-agent collaborative web navigation](https://arxiv.org/abs/2501.16609) | Pause and override agent actions during visual web navigation | [Project](https://oaishi.github.io/cowpilot.html) · [Code](https://github.com/oaishi/CowPilot) |
| 2024 | arXiv | [Unpacking failure modes of generative policies: Runtime monitoring of consistency and progress](https://arxiv.org/abs/2410.04640) | Monitor action consistency and visually assessed robot progress | [Project](https://sites.google.com/stanford.edu/sentinel) · [Code](https://github.com/agiachris/sentinel) |

## Contributing

Suggest papers or corrections through [issues](https://github.com/heshuting555/Awesome-Visual-Agent/issues) or pull requests. Include the specific visual contribution and a primary source. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Acknowledgements

Table presentation draws on [Awesome-3DGS-Applications](https://github.com/heshuting555/Awesome-3DGS-Applications); the original collection also drew on [Awesome-Agentic-MLLMs](https://github.com/HJYao00/Awesome-Agentic-MLLMs). Linked papers and software retain their respective authorship and licenses.

## Citation

Use [references.bib](../references.bib) to cite individual works.
