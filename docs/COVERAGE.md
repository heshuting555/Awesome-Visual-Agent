# Catalogue coverage and provenance

Bibliography snapshot: **2026-10-03**. Original catalogue assembled: **2026-09-27**. Historical link evidence retains its original dates.

| Item | Count |
| --- | ---: |
| Bibliographic keys | 719 |
| Non-paper BibTeX control records (excluded) | 1 |
| Unique works after merging aliases | 717 |
| Topic placements (cross-listings included) | 1118 |
| Framework branches / categories / topics | 2 / 10 / 35 |
| Figure 1 representative works (unique) | 261 |
| Figure 1 representative topic placements | 404 |
| Works with an arXiv link | 679 |
| Works with code links | 331 |
| Works without an identified paper or arXiv link | 12 |
| Works without an identified code link | 386 |

## Data sources and reproducible coverage

- [references.bib](../references.bib) is the unified bibliography; bibliography controls are excluded from paper counts.
- [data/taxonomy.json](../data/taxonomy.json) records the current Figure 1 hierarchy, section labels, ordered topics, and representative citation keys.
- [data/papers.json](../data/papers.json) records unique works, current citation keys, topic assignments, and preserved paper/project/code evidence.
- [data/source-map.json](../data/source-map.json) retains manuscript citation positions and filenames without publishing manuscript prose.
- [data/bibliography-update.json](../data/bibliography-update.json) retains bibliography imports, identity corrections, and alias migrations.
- [data/metadata.json](../data/metadata.json) records counts, snapshot dates, and the bibliography SHA-256.

The renderer checks that every bibliography key belongs to a catalogue work, every work has a valid framework topic and primary topic, and each Figure 1 representative is present in its topic. Cross-listing does not increase the unique-work count. Rebuild with `python3 scripts/build_readme.py` and validate with `python3 scripts/validate_catalog.py`.

## Classification basis

The hierarchy follows Figure 1, including planning and orchestration under harness infrastructure. Representative selections are explicitly identified by the figure. Other placements retain their assignment source and classification method in `papers.json`. A citation in a current manuscript subsection supports that placement; a mapping from an earlier draft preserves a historical topic basis; a title or bibliography-based classification is a curation inference and does not imply full-paper verification. These evidence types are kept distinct. Assignments can cross-list the same work when several mechanisms apply.

| Recorded classification method | Assignment records | Unique works supported |
| --- | ---: | ---: |
| `curated-framework-placement` | 689 | 443 |
| `current-manuscript-citation` | 141 | 123 |
| `figure1-representative` | 404 | 261 |

Assignment-record counts may exceed topic placements when several sources support the same work/topic pair. `legacy_sections` and `legacy_assignments` preserve old section evidence; the [legacy chapter archive](TOPICS.md#legacy-manuscript-chapter-archive) remains available without defining the current main grouping.

## Identity corrections and aliases

Current citation keys and historical aliases remain attached to catalogue identities. A verified preprint/published pair appears as one work; current BibTeX keys remain available in the bibliography. The historical key `chen2026reflect` was used for Reflect-R1 (arXiv:2606.27922); the current bibliography uses it for Reflect, Revise, Reuse (arXiv:2609.17653). Reflect-R1 is recorded separately under `chen2026reflectr1`.

| Work | Current citation keys |
| --- | --- |
| MMBench-GUI: A Unified Hierarchical Evaluation Framework for Multi-Platform GUI Agents | `bench_mmbenchgui`, `wang2025mmbenchgui` |
| MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation | `li2025mobileuse`, `li2026mobileuse` |

## Verification scope

Bibliography syntax, duplicate keys, catalogue coverage, and framework membership are checked during the update. Paper metadata and previously verified links retain their supporting sources and dates. These checks do not mean that every full paper, venue/year label, or repository has been independently re-audited.

An author-supplied code URL uses `verified_author_supplied_link`; it does not claim a fresh repository availability check. Existing repository checks retain their original dates. New URLs copied directly from the unified bibliography use `bibliography_supplied`; this records their source and does not claim a fresh availability or identity check. Missing links remain curation items, and a working link does not establish reproducibility.

## Paper links still to identify

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2012 | ECCV | — | A Naturalistic Open Source Movie for Optical Flow Evaluation | — |
| 2021 | NeurIPS | — | Align before fuse: Vision and language representation learning with momentum distillation | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 2025 | AAAI | Divide, Conquer and Combine | [Divide, Conquer and Combine: A Training-Free Framework for High-Resolution Image Perception in Multimodal Large Language Models](https://github.com/DreamMr/HR-Bench) | [Code](https://github.com/DreamMr/HR-Bench) |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2026 | Blog | — | Harness Engineering for Self-Improvement | — |
| 2023 | ICCV | IntentQA | [IntentQA: Context-aware Video Intent Reasoning](https://github.com/JoseponLee/IntentQA) | [Code](https://github.com/JoseponLee/IntentQA) |
| 2026 | Official Release | NVIDIA Isaac GR00T N1.7 | [NVIDIA Isaac GR00T N1.7: A Foundation Model for Generalist Robots](https://github.com/NVIDIA/Isaac-GR00T) | [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |
| 2026 | Official Release | — | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) | [Project](https://mistral.ai/news/robostral-navigate/) |
| 2026 | ICLR | Vision-r1 | Vision-r1: Incentivizing reasoning capability in multimodal large language models | — |

<details>
<summary>Code links still to identify</summary>

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2021 | ICCV | 3D-FRONT | [3D-FRONT: 3D Furnished Rooms With layOuts and semaNTics](https://openaccess.thecvf.com/content/ICCV2021/html/Fu_3D-FRONT_3D_Furnished_Rooms_With_layOuts_and_semaNTics_ICCV_2021_paper.html) | — |
| 2019 | ACL | — | [A Corpus for Reasoning about Natural Language Grounded in Photographs](https://aclanthology.org/P19-1644/) | — |
| 2012 | ECCV | — | A Naturalistic Open Source Movie for Optical Flow Evaluation | — |
| 2026 | arXiv | — | [A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692) | — |
| 2011 | AISTATS | — | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://proceedings.mlr.press/v15/ross11a.html) · [arXiv](https://arxiv.org/abs/1011.0686) | [Project](https://proceedings.mlr.press/v15/ross11a.html) |
| 2025 | arXiv | — | [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | — |
| 2025 | arXiv | — | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | [Project](https://github.com/CharlesQ9/Self-Evolving-Agents) |
| 2025 | CASE | — | [A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees](https://arxiv.org/abs/2503.15202) | — |
| 2026 | CVPR | — | [Active Video Perception: Iterative Evidence Seeking for Agentic Long Video Understanding](https://arxiv.org/abs/2512.05774) | — |
| 2025 | arXiv | Active-o3 | [Active-o3: Empowering multimodal large language models with active perception via grpo](https://arxiv.org/abs/2505.21457) | — |
| 2026 | CVPR | ActiveVLA | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/abs/2601.08325) | — |
| 2025 | arXiv | AdaWorld | [AdaWorld: Learning Adaptable World Models with Latent Actions](https://arxiv.org/abs/2503.18938) | — |
| 2026 | KDD | — | [Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory](https://arxiv.org/abs/2603.15280) | — |
| 2026 | arXiv | — | [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995) | — |
| 2026 | OpenReview Preprint | — | [Agent harness engineering: A survey](https://openreview.net/forum?id=eONq7FdiHa) | [Project](https://github.com/Picrew/awesome-agent-harness) |
| 2026 | ECCV | — | [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649) | [Project](https://zhangbo135.github.io/agentic-collaborative-cognition/) |
| 2026 | ICML | — | [Agentic Model Predictive Questioning Control in Visual Design](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | arXiv | — | [Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046) | — |
| 2026 | arXiv | AgenticRL | [AgenticRL: Agentic Reinforcement Learning with Self-Refinement for Complex UAV Navigation](https://arxiv.org/abs/2606.03963) | — |
| 2026 | The 4th AI for Visual Arts Workshop | AgentMV | [AgentMV: A State-Guided Multi-Agent Framework for Budget-Aware Music Video Generation](https://arxiv.org/abs/2605.10723) | — |
| 2026 | CVPR | AGENTSAFE | [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697) | — |
| 2021 | NeurIPS | — | Align before fuse: Vision and language representation learning with momentum distillation | — |
| 2023 | arXiv | Android in the Wild | [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) | — |
| 2024 | arXiv | AndroidLab | [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://arxiv.org/abs/2410.24024) | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 2026 | CVPR | ARM-Thinker | [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](https://arxiv.org/abs/2512.05111) | — |
| 2026 | arXiv | AtomVLA | [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519) | — |
| 2026 | Official Release | — | [Auditing Prospective Memory in Frozen Language-Model Systems: Causal Mechanisms and the Limits of Naturalistic Trigger Grounding](https://www.preprints.org/manuscript/202608.1081) | [Project](https://www.preprints.org/manuscript/202608.1081) |
| 2026 | arXiv | AutoRef | [AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation](https://arxiv.org/abs/2609.35530) | — |
| 2024 | arXiv | AutoRT | [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963) | — |
| 2023 | NeurIPS | AVIS | [AVIS: Autonomous Visual Information Seeking with Large Language Model Agent](https://doi.org/10.52202/075280-0040) · [arXiv](https://arxiv.org/abs/2306.08129) | — |
| 2026 | arXiv | BaT | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) | — |
| 2026 | arXiv | Beacon | [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595) | — |
| 1999 | Artificial Intelligence | Between MDPs and semi-MDPs | [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | — |
| 2026 | arXiv | — | [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](https://arxiv.org/abs/2608.21204) | — |
| 2026 | arXiv | Beyond Pixel Histories | [Beyond Pixel Histories: World Models with Persistent 3D State](https://arxiv.org/abs/2603.03482) | — |
| 2020 | arXiv | Beyond the Nav-Graph | [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857) | — |
| 2024 | arXiv | BLINK | [BLINK: Multimodal Large Language Models Can See but Not Perceive](https://arxiv.org/abs/2404.12390) | — |
| 2023 | ICML | BLIP-2 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | — |
| 2026 | arXiv | BlueLM-GUI Technical Report | [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents](https://arxiv.org/abs/2609.12394) | — |
| 2023 | arXiv | BridgeData V2 | [BridgeData V2: A Dataset for Robot Learning at Scale](https://arxiv.org/abs/2308.12952) | — |
| 2024 | ICLR | — | [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | — |
| 2023 | arXiv | — | [Can Pre-trained Vision and Language Models Answer Visual Information-Seeking Questions?](https://arxiv.org/abs/2302.11713) | — |
| 2025 | arXiv | — | [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](https://arxiv.org/abs/2503.08558) | — |
| 2026 | CVPR Findings | CarePilot | [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) | — |
| 2017 | arXiv | CARLA | [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938) | — |
| 2026 | arXiv | — | [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998) | — |
| 2024 | arXiv | CG-Bench | [CG-Bench: Clue-grounded Question Answering Benchmark for Long Video Understanding](https://arxiv.org/abs/2412.12075) | — |
| 2024 | arXiv | ChartGemma | [ChartGemma: Visual Instruction-tuning for Chart Reasoning in the Wild](https://arxiv.org/abs/2407.04172) | — |
| 2026 | ICLR | — | [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | — |
| 2025 | CVPR | Code-as-Monitor | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2026 | arXiv | Code2World | [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | — |
| 2025 | ICLR | — | [Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback](https://arxiv.org/abs/2410.08852) | — |
| 2026 | arXiv | ContactGaussian-WM | [ContactGaussian-WM: Learning Physics-Grounded World Model from Videos](https://arxiv.org/abs/2602.11021) | — |
| 2019 | Neural Networks | — | [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) | — |
| 2026 | arXiv | — | [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070) | — |
| 2026 | arXiv | CoRe | [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](https://arxiv.org/abs/2607.01721) | — |
| 2026 | arXiv | Cosmos Policy | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) | — |
| 2025 | arXiv | — | [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | — |
| 2026 | ICLR | CP-Agent | [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435) | — |
| 2025 | NeurIPS | CPathAgent | [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://doi.org/10.52202/085713-3404) · [arXiv](https://arxiv.org/abs/2505.20510) | — |
| 2025 | NeurIPS | CREA | [CREA: A Collaborative Multi-Agent Framework for Creative Image Editing and Generation](https://doi.org/10.52202/085713-5705) · [arXiv](https://arxiv.org/abs/2504.05306) | — |
| 2024 | ICLR | CRITIC | [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) | — |
| 2025 | arXiv | Ctrl-World | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) | — |
| 2009 | ICML | — | [Curriculum learning](https://icml.cc/2009/papers/119.pdf) | — |
| 2026 | CHI | — | [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight](https://arxiv.org/abs/2509.10723) | — |
| 2026 | arXiv | — | [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528) | — |
| 2026 | arXiv | DataEvolver | [DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation](https://arxiv.org/abs/2606.31537) | — |
| 2026 | arXiv | — | [Design Choices That Matter: A Functional ANOVA Analysis for Remote Sensing Multi-Label Classification](https://arxiv.org/abs/2608.04702) | — |
| 2024 | ECCV | DetToolChain | [DetToolChain: A New Prompting Paradigm to Unleash Detection Ability of MLLM](https://arxiv.org/abs/2403.12488) | — |
| 2026 | CVPR | — | [Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols](https://arxiv.org/abs/2512.02787) | — |
| 2026 | arXiv | — | [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | — |
| 2024 | arXiv | DINO-WM | [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983) | — |
| 2026 | TGRS | DisasterTD | [DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization](https://arxiv.org/abs/2607.24856) | — |
| 2026 | arXiv | — | [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/abs/2606.02357) | — |
| 2024 | arXiv | DOME | [DOME: Taming Diffusion Model into High-Fidelity Controllable Occupancy World Model](https://arxiv.org/abs/2410.10429) | — |
| 2026 | ACL | — | [Don’t act blindly: Robust gui automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2026 | arXiv | Dream-RSI | [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) | [Project](https://github.com/zhengkid/Dream-RSI) |
| 2025 | arXiv | DreamGen | [DreamGen: Unlocking Generalization in Robot Learning through Video World Models](https://arxiv.org/abs/2505.12705) | — |
| 2026 | CVPR | DriveMoE | [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_DriveMoE_Mixture-of-Experts_for_Vision-Language-Action_Model_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2505.16278) | — |
| 2025 | ICCV | DWIM | [DWIM: Towards Tool-aware Visual Reasoning via Discrepancy-aware Workflow Generation & Instruct-Masking Tuning](https://arxiv.org/abs/2503.19263) | — |
| 2026 | arXiv | ECHO | [ECHO: Terminal Agents Learn World Models for Free](https://arxiv.org/abs/2605.24517) | — |
| 2026 | CVPR | EchoTrail-GUI | [EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/abs/2512.19396) | — |
| 2026 | arXiv | EdgeBench | [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155) | — |
| 2026 | arXiv | EE-MCP | [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/abs/2604.09815) | — |
| 2025 | arXiv | — | [Efficient Multi-turn RL for GUI Agents via Decoupled Training and Adaptive Data Curation](https://arxiv.org/abs/2509.23866) | — |
| 2024 | arXiv | — | [Efficient Self-Improvement in Multimodal Large Language Models: A Model-Level Judge-Free Approach](https://arxiv.org/abs/2411.17760) | — |
| 2026 | NeurIPS | EfficientVLA | [EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://arxiv.org/abs/2506.10100) | — |
| 2021 | arXiv | Ego4D | [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058) | — |
| 2025 | arXiv | EgoLife | [EgoLife: Towards Egocentric Life Assistant](https://arxiv.org/abs/2503.03803) | — |
| 2023 | arXiv | EgoSchema | [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://arxiv.org/abs/2308.09126) | — |
| 2026 | arXiv | ELITE | [ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents](https://arxiv.org/abs/2603.24018) | — |
| 2025 | ICLR | EMOS | [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | — |
| 2025 | NAACL Findings | — | [Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement](https://arxiv.org/abs/2405.15973) | — |
| 2026 | arXiv | EVA | [EVA: Efficient Reinforcement Learning for End-to-End Video Agent](https://arxiv.org/abs/2603.22918) | — |
| 2024 | arXiv | — | [Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941) | — |
| 2026 | CVPR | EvoGraph-R1 | [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](https://arxiv.org/abs/2607.12764) | — |
| 2026 | CVPR Findings | — | [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | — |
| 2026 | arXiv | EvolveNav | [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | — |
| 2026 | AAAI | — | [Evolving generalist virtual agents with generative and associative memory](https://ojs.aaai.org/index.php/AAAI/article/view/38300) | — |
| 2026 | arXiv | EvoMemNav | [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509) | — |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | arXiv | EvoX | [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413) | — |
| 2026 | arXiv | — | [Experience Transfer for Multimodal LLM Agents in Minecraft Game](https://arxiv.org/abs/2604.05533) | — |
| 2025 | arXiv | FailSafe | [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642) | [Project](https://jimntu.github.io/FailSafe) |
| 2026 | arXiv | Fast-ThinkAct | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) | — |
| 2026 | arXiv | Fast-WAM | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) | — |
| 2025 | arXiv | — | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) | — |
| 2026 | arXiv | FiRe | [FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation](https://arxiv.org/abs/2604.13491) | — |
| 2022 | NeurIPS | — | [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) | — |
| 2026 | CVPR | FLARE | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | — |
| 2025 | arXiv | FlowDreamer | [FlowDreamer: A RGB-D World Model with Flow-based Motion Representations for Robot Manipulation](https://arxiv.org/abs/2505.10075) | — |
| 2016 | arXiv | FVQA | [FVQA: Fact-based Visual Question Answering](https://arxiv.org/abs/1606.05433) | — |
| 2025 | arXiv | Game-TARS | [Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents](https://arxiv.org/abs/2510.23691) | — |
| 2024 | arXiv | GEM | [GEM: A Generalizable Ego-Vision Multimodal World Model for Fine-Grained Ego-Motion, Object Dynamics, and Scene Composition Control](https://arxiv.org/abs/2412.11198) | — |
| 2025 | arXiv | — | [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://arxiv.org/abs/2510.03342) | — |
| 2023 | arXiv | — | [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805) | — |
| 2026 | arXiv | — | [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406) | — |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2024 | ICML | — | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | [Project](https://sites.google.com/corp/view/genie-2024/) |
| 2026 | CVPR | GeoMMBench and GeoMMAgent | [GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing](https://arxiv.org/abs/2604.08896) | — |
| 2019 | CVPR | GQA | [GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506) | — |
| 2024 | arXiv | GR-2 | [GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](https://arxiv.org/abs/2410.06158) | — |
| 2025 | arXiv | GUI-R1 | [GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458) | — |
| 2026 | ICLR | GUI-Shift | [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493) | — |
| 2021 | arXiv | — | [Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://arxiv.org/abs/2109.08238) | — |
| 2026 | arXiv | — | [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718) | — |
| 2026 | Blog | — | Harness Engineering for Self-Improvement | — |
| 2026 | arXiv | — | [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821) | — |
| 2026 | arXiv | HarnessPAI | [HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166) | — |
| 2026 | arXiv | HarnessWAM | [HarnessWAM: Bridging Prediction and Deliberation in World Action Models](https://arxiv.org/abs/2608.09516) | — |
| 2025 | arXiv | — | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | [Project](https://www.pi.website/research/hirobot) |
| 2026 | ICML | — | [Hierarchical Procedural Meta-Reasoning for Generalizable Multimodal Agents](https://openreview.net/forum?id=v2H2vzRqcr) | — |
| 2022 | arXiv | — | [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125) | — |
| 2025 | arXiv | HippoMM | [HippoMM: Hippocampal-inspired Multimodal Memory for Long Audiovisual Event Understanding](https://arxiv.org/abs/2504.10739) | — |
| 2026 | arXiv | — | [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347) | — |
| 2026 | arXiv | — | [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](https://arxiv.org/abs/2606.15032) | — |
| 2026 | arXiv | — | [Hyperagents](https://arxiv.org/abs/2603.19461) | — |
| 2026 | arXiv | ImageEdit-R1 | [ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning](https://arxiv.org/abs/2603.08059) | [Project](https://github.com/zhaoyiran924/ImageEdit-R1) |
| 2023 | CVPR | InstructPix2Pix | [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://arxiv.org/abs/2211.09800) | [Project](https://www.timothybrooks.com/instruct-pix2pix) |
| 2026 | arXiv | Intend, Reflect, Refine | [Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving](https://arxiv.org/abs/2606.22913) | — |
| 2026 | arXiv | IntentScore | [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) | — |
| 2025 | ICCV | — | [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342) | — |
| 2025 | ICML | — | [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559) | — |
| 2026 | CVPR | iSHIFT | [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009) | — |
| 2026 | ICLR | — | [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670) | — |
| 2026 | ICLR | — | [K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676) | — |
| 2026 | arXiv | — | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2026 | arXiv | Kimi K2.5 | [Kimi K2.5: Visual Agentic Intelligence](https://arxiv.org/abs/2602.02276) | — |
| 2026 | arXiv | KnowAct-GUIClaw | [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/abs/2607.12625) | — |
| 2025 | NeurIPS | LabUtopia | [LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](https://doi.org/10.52202/085713-1158) · [arXiv](https://arxiv.org/abs/2505.22634) | — |
| 2025 | EMNLP | LATTE | [LATTE: Learning to Think with Vision Specialists](https://arxiv.org/abs/2412.05479) | — |
| 2024 | IUI | LAVE | [LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/abs/2402.10294) | — |
| 2026 | NeurIPS | — | [Learning 3D Persistent Embodied World Models](https://arxiv.org/abs/2505.05495) | — |
| 2023 | arXiv | — | [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705) | — |
| 2026 | arXiv | — | [Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148) | — |
| 2025 | arXiv | — | [Learning Semantic Atomic Skills for Multi-Task Robotic Manipulation](https://arxiv.org/abs/2512.18368) | [Project](https://atom-skill.github.io) |
| 2026 | arXiv | — | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | [Project](https://vlaworld.github.io) |
| 2026 | arXiv | LEGO-Anything | [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380) | — |
| 2026 | CVPR | LensWalk | [LensWalk: Agentic Video Understanding by Planning How You See in Videos](https://arxiv.org/abs/2603.24558) | — |
| 2025 | ICCV | — | [Less is More: Empowering GUI Agent with Context-Aware Simplification](https://arxiv.org/abs/2507.03730) | — |
| 2026 | arXiv | LeWorldModel | [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312) | — |
| 2023 | NeurIPS | LIBERO | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | [Project](https://libero-project.github.io) |
| 2024 | ECCV | LLaVA-Plus | [LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents](https://arxiv.org/abs/2311.05437) | — |
| 2023 | arXiv | LLM-grounded Diffusion | [LLM-grounded Diffusion: Enhancing Prompt Understanding of Text-to-Image Diffusion Models with Large Language Models](https://arxiv.org/abs/2305.13655) | — |
| 2026 | ICLR | LongHorizonUI | [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE) | — |
| 2025 | arXiv | — | [Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception](https://arxiv.org/abs/2511.15279) | — |
| 2024 | arXiv | LVBench | [LVBench: An Extreme Long Video Understanding Benchmark](https://arxiv.org/abs/2406.08035) | — |
| 2019 | arXiv | LVIS | [LVIS: A Dataset for Large Vocabulary Instance Segmentation](https://arxiv.org/abs/1908.03195) | — |
| 2025 | CVPR | — | [Magma: A Foundation Model for Multimodal AI Agents](https://arxiv.org/abs/2502.13130) | — |
| 2025 | arXiv | MAI-UI Technical Report | [MAI-UI Technical Report: Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2512.22047) | — |
| 2025 | arXiv | — | [Marmot: Object-Level Self-Correction via Multi-Agent Reasoning](https://arxiv.org/abs/2504.20054) | — |
| 2023 | arXiv | MathVista | [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts](https://arxiv.org/abs/2310.02255) | — |
| 2017 | arXiv | Matterport3D | [Matterport3D: Learning from RGB-D Data in Indoor Environments](https://arxiv.org/abs/1709.06158) | — |
| 2026 | arXiv | MemCtrl | [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) | — |
| 2026 | ICLR | — | [Memento: Toward an All-Day Proactive Assistant for Ultra-Long Streaming Video](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b5f4587a0bdb81ecc6ce9d82320a5c2-Abstract-Conference.html) | — |
| 2026 | arXiv | MementoGUI | [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652) | — |
| 2026 | ACL | Memory-R1 | [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | — |
| 2026 | arXiv | MemRL | [MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory](https://arxiv.org/abs/2601.03192) | — |
| 2026 | CVPR | META | [META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) | — |
| 2026 | arXiv | MetaForge | [MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand](https://arxiv.org/abs/2606.01801) | — |
| 2026 | arXiv | MetaRSI / RSI2 | [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396) | — |
| 2026 | arXiv | MetaSkill-Evolve | [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) | — |
| 2023 | arXiv | Mind2Web | [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) | — |
| 2025 | arXiv | MineWorld | [MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft](https://arxiv.org/abs/2504.08388) | — |
| 2024 | arXiv | MLVU | [MLVU: Benchmarking Multi-task Long Video Understanding](https://arxiv.org/abs/2406.04264) | — |
| 2026 | ICLR | MMedAgent-RL | [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) | — |
| 2025 | arXiv | MobileWorldBench | [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) | — |
| 2016 | arXiv | — | [Modeling Context in Referring Expressions](https://arxiv.org/abs/1608.00272) | — |
| 2024 | arXiv | MOKA | [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | — |
| 2024 | arXiv | Movie Gen | [Movie Gen: A Cast of Media Foundation Models](https://arxiv.org/abs/2410.13720) | — |
| 2026 | arXiv | MUSE | [MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction](https://arxiv.org/abs/2606.14168) | — |
| 2026 | arXiv | MuSEAgent | [MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences](https://arxiv.org/abs/2603.27813) | — |
| 2023 | arXiv | MVBench | [MVBench: A Comprehensive Multi-modal Video Understanding Benchmark](https://arxiv.org/abs/2311.17005) | — |
| 2024 | arXiv | NaVid | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852) | — |
| 2025 | RSS | NaVILA | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453) | [Project](https://navila-bot.github.io/) |
| 2026 | ECCV | NeuroRefiner | [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](https://arxiv.org/abs/2608.09636) | — |
| 2024 | arXiv | — | [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) | — |
| 2025 | arXiv | Octopus | [Octopus: Agentic Multimodal Reasoning with Six-Capability Orchestration](https://arxiv.org/abs/2511.15351) | — |
| 2019 | CVPR | OK-VQA | [OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge](https://openaccess.thecvf.com/content_CVPR_2019/html/Marino_OK-VQA_A_Visual_Question_Answering_Benchmark_Requiring_External_Knowledge_CVPR_2019_paper.html) | — |
| 2024 | ECCV | OmniACT | [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553) | — |
| 2026 | ICLR | OmniActor | [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322) | — |
| 2026 | arXiv | OmniHarness | [OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning](https://arxiv.org/abs/2609.16057) | — |
| 2024 | arXiv | — | [On the Effects of Data Scale on UI Control Agents](https://arxiv.org/abs/2406.03679) | — |
| 2025 | arXiv | OneTwoVLA | [OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2505.11917) | — |
| 2026 | arXiv | OnEvoMemory | [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749) | — |
| 2024 | arXiv | OpenVLA | [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | — |
| 2025 | ICLR | OS-ATLAS | [OS-ATLAS: Foundation action model for generalist GUI agents](https://arxiv.org/abs/2410.23218) | — |
| 2026 | arXiv | OS-Themis | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) | — |
| 2026 | CVPR | OVOD-Agent | [OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection](https://arxiv.org/abs/2511.21064) | — |
| 2023 | arXiv | PaLM-E | [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378) | — |
| 2026 | ECCV | — | [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373) | — |
| 2026 | ICLR | PhyScensis | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://arxiv.org/abs/2602.14968) | — |
| 2025 | arXiv | PhysTwin | [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://arxiv.org/abs/2503.17973) | — |
| 2025 | arXiv | PhysWorld | [PhysWorld: From Real Videos to World Models of Deformable Objects via Physics-Aware Demonstration Synthesis](https://arxiv.org/abs/2510.21447) | — |
| 2024 | ICML | PIVOT | [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://arxiv.org/abs/2402.07872) | [Project 1](http://pivot-prompt.github.io) · [Project 2](https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo) |
| 2026 | ICML | — | [Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation](https://proceedings.mlr.press/v306/shen26e.html) | — |
| 1998 | Artificial Intelligence | — | [Planning and Acting in Partially Observable Stochastic Domains](https://doi.org/10.1016/S0004-3702(98)00023-X) | — |
| 2026 | ICLR | — | [Planning with an Embodied Learnable Memory](https://openreview.net/forum?id=79BOATBal9) | — |
| 2025 | arXiv | — | [Planning with Reasoning using Vision Language World Model](https://arxiv.org/abs/2509.02722) | — |
| 2023 | CVPR | — | [Planning-oriented Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2212.10156) | — |
| 2025 | ECIR | PlotEdit | [PlotEdit: Natural Language-Driven Accessible Chart Editing in PDFs via Multimodal LLM Agents](https://arxiv.org/abs/2501.11233) | — |
| 2026 | EMNLP | — | [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388) | — |
| 2016 | ICLR | — | [Policy Distillation](https://arxiv.org/abs/1511.06295) | — |
| 2025 | ACL Findings | — | [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) | [Project](https://invinciblewyq.github.io/ponder-press-page/) |
| 2026 | arXiv | PPTBench | [PPTBench: Can Coding Agents Reconstruct the Visual World through Structured, Editable Slides](https://arxiv.org/abs/2609.29718) | — |
| 2024 | arXiv | — | [Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419) | [Project](https://www.kaggle.com/datasets/googleai/pasta-data) |
| 2026 | CVPR | Progress-Think | [Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Progress-Think_Semantic_Progress_Reasoning_for_Vision-Language_Navigation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.17097) | — |
| 2026 | arXiv | ProMMSearchAgent | [ProMMSearchAgent: A Generalizable Multimodal Search Agent Trained with Process-Oriented Rewards](https://arxiv.org/abs/2604.20486) | — |
| 2026 | arXiv | — | [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230) | — |
| 2025 | arXiv | — | [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | — |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |
| 2026 | arXiv | Qwen-AgentWorld | [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) | — |
| 2026 | arXiv | Qwen-RobotNav Technical Report | [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) | — |
| 2026 | arXiv | Qwen-UI-Agent Technical Report | [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227) | — |
| 2026 | ICLR | R-WoM | [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://doi.org/10.48550/arxiv.2510.11892) · [arXiv](https://arxiv.org/abs/2510.11892) | — |
| 2025 | ICCV | R1-VL | [R1-VL: Learning to Reason with Multimodal Large Language Models via Step-wise Group Relative Policy Optimization](https://arxiv.org/abs/2503.12937) | — |
| 2021 | arXiv | — | [Rapid Exploration for Open-World Navigation with Latent Goal Models](https://arxiv.org/abs/2104.05859) | — |
| 2025 | arXiv | Raw2Drive | [Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)](https://arxiv.org/abs/2505.16394) | — |
| 2026 | arXiv | RDA | [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) | — |
| 2026 | arXiv | — | [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378) | — |
| 2026 | arXiv | Recursive Self-Improvement in AI | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | [Project](https://github.com/deepgrounding/recursive-self-improvement) |
| 2026 | arXiv | — | [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457) | — |
| 2026 | ECCV | ReDesign | [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](https://arxiv.org/abs/2607.25565) | — |
| 2026 | arXiv | RegenHarness | [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | — |
| 2018 | arXiv | — | [Reinforcement Learning on Web Interfaces Using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802) | — |
| 2026 | ACL | ReLook | [ReLook: Vision-Grounded RL with a Multimodal LLM Critic for Agentic Web Coding](https://aclanthology.org/2026.acl-long.1167/) | — |
| 2026 | CVPR | ReSAM | [ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images](https://arxiv.org/abs/2511.21606) | — |
| 2024 | NeurIPS | RestoreAgent | [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://doi.org/10.52202/079017-3512) · [arXiv](https://arxiv.org/abs/2407.18035) | — |
| 2026 | ICLR | ReTool | [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) | — |
| 2026 | CVPR | RetouchIQ | [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) | — |
| 2026 | arXiv | — | [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227) | — |
| 2025 | arXiv | — | [Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning](https://arxiv.org/abs/2509.16136) | — |
| 2024 | arXiv | ReXTime | [ReXTime: A Benchmark Suite for Reasoning-Across-Time in Videos](https://arxiv.org/abs/2406.19392) | — |
| 2025 | arXiv | RFTF | [RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback](https://arxiv.org/abs/2505.19767) | — |
| 2019 | arXiv | RLBench | [RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271) | — |
| 2024 | arXiv | RLDG | [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](https://arxiv.org/abs/2412.09858) | [Project](https://generalist-distillation.github.io) |
| 2026 | arXiv | RLHarness | [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326) | — |
| 2026 | arXiv | Robo-Cortex | [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729) | — |
| 2023 | arXiv | RoboCat | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | — |
| 2025 | arXiv | RoboChemist | [RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation](https://arxiv.org/abs/2509.08820) | [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) |
| 2026 | arXiv | RoboHarness | [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | — |
| 2025 | arXiv | RoboMemory | [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415) | — |
| 2025 | arXiv | RoboMonkey | [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://arxiv.org/abs/2506.17811) | — |
| 2024 | arXiv | RoboPoint | [RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics](https://arxiv.org/abs/2406.10721) | — |
| 2026 | Official Release | — | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) | [Project](https://mistral.ai/news/robostral-navigate/) |
| 2025 | IROS | — | [Robots that Suggest Safe Alternatives](https://arxiv.org/abs/2409.09883) | — |
| 2020 | arXiv | Room-Across-Room | [Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding](https://arxiv.org/abs/2010.07954) | — |
| 2025 | arXiv | RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2026 | arXiv | RSIAgent | [RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://arxiv.org/abs/2609.15364) | — |
| 2026 | arXiv | RSIGame | [RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement](https://arxiv.org/abs/2609.39045) | — |
| 2023 | CoRL | RT-2 | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | [Project](https://robotics-transformer.github.io/) |
| 2024 | arXiv | RT-H | [RT-H: Action Hierarchies Using Language](https://arxiv.org/abs/2403.01823) | — |
| 2026 | arXiv | — | [Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation](https://arxiv.org/abs/2608.24138) | — |
| 2026 | arXiv | RynnBrain | [RynnBrain: Open Embodied Foundation Models](https://arxiv.org/abs/2602.14979) | — |
| 2026 | arXiv | — | [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147) | — |
| 2026 | CVPR | SAGE | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | [Project](https://research.nvidia.com/labs/dir/sage/) |
| 2020 | arXiv | SAPIEN | [SAPIEN: A SimulAted Part-based Interactive ENvironment](https://arxiv.org/abs/2003.08515) | — |
| 2026 | CVPR | — | [Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs](https://arxiv.org/abs/2511.19773) | — |
| 2025 | arXiv | — | [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250) | — |
| 2026 | CVPR Workshops | — | [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | — |
| 2024 | ICML | SceneCraft | [SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code](https://arxiv.org/abs/2403.01248) | — |
| 2026 | CVPR | SciEducator | [SciEducator: Scientific Video Understanding and Educating via Deming-Cycle Multi-Agent System](https://arxiv.org/abs/2511.17943) | — |
| 2026 | arXiv | SCOPE | [SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation](https://arxiv.org/abs/2605.08043) | — |
| 2025 | arXiv | SE-VLN | [SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models](https://arxiv.org/abs/2507.13152) | — |
| 2026 | arXiv | SEA-Eval | [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988) | — |
| 2026 | arXiv | — | [Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation](https://arxiv.org/abs/2603.08260) | — |
| 2026 | arXiv | — | [Self-Adaptive VLA for Robust Robot Deployment](https://arxiv.org/abs/2609.30092) | — |
| 2024 | CVPR | — | [Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090) | — |
| 2026 | ECCV | — | [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](https://arxiv.org/abs/2606.28971) | — |
| 2025 | CVPR | — | [Self-Evolving Visual Concept Library using Vision-Language Critics](https://arxiv.org/abs/2504.00185) | — |
| 2026 | arXiv | — | [Self-Evolving Visual Questioner](https://arxiv.org/abs/2606.13929) | — |
| 2025 | EMNLP Findings | — | [Self-Improvement in Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2510.02665) | — |
| 2026 | ICLR | — | [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091) | — |
| 2026 | ICLR | — | [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | [Project](https://sites.google.com/utexas.edu/armor) |
| 2026 | arXiv | — | [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167) | — |
| 2025 | arXiv | — | [Semantic World Models](https://arxiv.org/abs/2510.19818) | [Project](https://weirdlabuw.github.io/swm) |
| 2026 | NeurIPS | — | [Sherlock: Self-Correcting Reasoning in Vision-Language Models](https://arxiv.org/abs/2505.22651) | — |
| 2026 | arXiv | SIA | [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | — |
| 2025 | CVPR | SimLingo | [SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Renz_SimLingo_Vision-Only_Closed-Loop_Autonomous_Driving_with_Language-Action_Alignment_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09594) | — |
| 2025 | NeurIPS | SketchMind | [SketchMind: A Multi-Agent Cognitive Framework for Assessing Student-Drawn Scientific Sketches](https://doi.org/10.52202/085713-2774) · [arXiv](https://arxiv.org/abs/2507.22904) | — |
| 2026 | arXiv | — | [Skill-Guided Continuation Distillation for GUI Agents](https://arxiv.org/abs/2606.18890) | — |
| 2024 | CVPR | SkillDiffuser | [SkillDiffuser: Interpretable Hierarchical Planning via Skill Abstractions in Diffusion-Based Task Execution](https://arxiv.org/abs/2312.11598) | — |
| 2022 | arXiv | — | [Socially Compliant Navigation Dataset (SCAND): A Large-Scale Dataset of Demonstrations for Social Navigation](https://arxiv.org/abs/2203.15041) | — |
| 2026 | arXiv | SpatialEvo | [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144) | — |
| 2025 | arXiv | SpatialVLA | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830) | — |
| 2024 | arXiv | SPIRE | [SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation](https://arxiv.org/abs/2410.18065) | — |
| 2025 | arXiv | STORM | [STORM: Search-Guided Generative World Models for Robotic Manipulation](https://arxiv.org/abs/2512.18477) | — |
| 2025 | arXiv | StreamVLN | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://arxiv.org/abs/2507.05240) | — |
| 2026 | AAAI | — | [Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916) | — |
| 2018 | arXiv | TallyQA | [TallyQA: Answering Complex Counting Questions](https://arxiv.org/abs/1810.12440) | — |
| 2024 | arXiv | THE COLOSSEUM | [THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation](https://arxiv.org/abs/2402.08191) | — |
| 2026 | arXiv | — | [The Essence of Balance for Self-Improving Agents in Vision-and-Language Navigation](https://arxiv.org/abs/2604.19064) | — |
| 2025 | arXiv | — | [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) | — |
| 2026 | arXiv | — | [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873) | [Project](https://github.com/theseus-labs-rsi/awesome-rsi) |
| 2026 | arXiv | — | [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | — |
| 2024 | ECCV | — | [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720) | — |
| 2026 | arXiv | Thinking with Imagination | [Thinking with Imagination: Agentic Visual Spatial Reasoning with World Simulators](https://arxiv.org/abs/2606.06476) | — |
| 2026 | ECCV | TIR-Agent | [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) | — |
| 2023 | NeurIPS | — | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | — |
| 2019 | arXiv | — | [Toward Real-World Single Image Super-Resolution: A New Benchmark and A New Model](https://arxiv.org/abs/1904.00523) | — |
| 2025 | arXiv | — | [Towards Agentic AI for Multimodal-Guided Video Object Segmentation](https://arxiv.org/abs/2508.10572) | — |
| 2022 | arXiv | — | [Towards Large-Scale Small Object Detection: Survey and Benchmarks](https://arxiv.org/abs/2207.14096) | — |
| 2025 | arXiv | — | [Training Agents Inside of Scalable World Models](https://arxiv.org/abs/2509.24527) | — |
| 2020 | arXiv | Transporter Networks | [Transporter Networks: Rearranging the Visual World for Robotic Manipulation](https://arxiv.org/abs/2010.14406) | — |
| 2026 | arXiv | UI-Mem | [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) | [Project](https://ui-mem.github.io) |
| 2026 | arXiv | UI-Oceanus | [UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics](https://arxiv.org/abs/2604.02345) | — |
| 2025 | arXiv | UI-TARS-2 Technical Report | [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) | — |
| 2025 | arXiv | UI-TARS | [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) | — |
| 2026 | arXiv | — | [UI-Venus-2 Technical Report](https://arxiv.org/abs/2609.00028) | — |
| 2026 | ICML | UI2Code^N | [UI2Code^N: UI-to-Code Generation as Interactive Visual Optimization](https://proceedings.mlr.press/v306/yang26v.html) | — |
| 2025 | arXiv | — | [Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models](https://arxiv.org/abs/2503.01876) | — |
| 2025 | arXiv | Unified World Models | [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://arxiv.org/abs/2504.02792) | — |
| 2026 | arXiv | — | [Unifying Language-Action Understanding and Generation for Autonomous Driving](https://arxiv.org/abs/2603.01441) | — |
| 2024 | ICLR | — | [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](https://arxiv.org/abs/2312.13139) | — |
| 2026 | CVPR | — | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) | — |
| 2026 | arXiv | V-Gym | [V-Gym: Enhancing Agentic Visual Reasoning via Skill-Data Co-Evolution](https://arxiv.org/abs/2609.34682) | — |
| 2026 | arXiv | V-Mem | [V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory](https://arxiv.org/abs/2608.01543) | — |
| 2025 | CVPR | V-Stylist | [V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents](https://arxiv.org/abs/2503.12077) | — |
| 2025 | CVPR | Video-MME | [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075) | [Project](https://video-mme.github.io) |
| 2026 | ICLR | Video-STAR | [Video-STAR: Reinforcing Open-Vocabulary Action Recognition with Tools](https://arxiv.org/abs/2510.08480) | — |
| 2025 | ICLR | Video-STaR | [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://arxiv.org/abs/2407.06189) | [Project](https://orrzohar.github.io/projects/video-star/) |
| 2025 | arXiv | — | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | — |
| 2025 | arXiv | VideoAgent2 | [VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT](https://arxiv.org/abs/2504.04471) | — |
| 2024 | ECCV | VideoAgent | [VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517) | — |
| 2026 | NeurIPS | VideoChat-R1.5 | [VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception](https://arxiv.org/abs/2509.21100) | — |
| 2026 | arXiv | VideoResearcher | [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664) | — |
| 2025 | arXiv | ViReSkill | [ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning](https://arxiv.org/abs/2509.24219) | — |
| 2026 | arXiv | VISA | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013) | — |
| 2026 | arXiv | ViSAGE | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | — |
| 2026 | ECCV | VisCritic | [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525) | — |
| 2017 | arXiv | Vision-and-Language Navigation | [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280) | — |
| 2026 | ICML | Vision-DeepResearch | [Vision-DeepResearch: Incentivizing DeepResearch Capability in Multimodal Large Language Models](https://proceedings.mlr.press/v306/huang26bx.html) | — |
| 2026 | CVPR | Vision-R1 | [Vision-R1: Evolving Human-Free Alignment in Large Vision-Language Models via Vision-Guided Reinforcement Learning](https://arxiv.org/abs/2503.18013) | — |
| 2026 | ICLR | Vision-r1 | Vision-r1: Incentivizing reasoning capability in multimodal large language models | — |
| 2026 | CVPR | VISTA | [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2510.15831) | — |
| 2026 | arXiv | — | [Visual Reasoning through Tool-supervised Reinforcement Learning](https://arxiv.org/abs/2604.19945) | — |
| 2026 | arXiv | — | [Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning](https://arxiv.org/abs/2607.02490) | — |
| 2025 | arXiv | VisualToolAgent (VisTA) | [VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection](https://arxiv.org/abs/2505.20289) | — |
| 2024 | ACL | VisualWebArena | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | — |
| 2026 | NeurIPS | VL-Rethinker | [VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning](https://arxiv.org/abs/2504.08837) | — |
| 2026 | NeurIPS | VLA-Cache | [VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://arxiv.org/abs/2502.02175) | — |
| 2026 | arXiv | VLAW | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2025 | arXiv | VLN-R1 | [VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.17221) | — |
| 2026 | arXiv | WAM4D | [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](https://arxiv.org/abs/2606.14048) | — |
| 2025 | arXiv | WebCoach | [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997) | — |
| 2022 | arXiv | WebShop | [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) | — |
| 2024 | ACL | WebVoyager | [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) | — |
| 2026 | ICLR | — | [Webwatcher: Breaking new frontiers of vision-language deep research agent](https://arxiv.org/abs/2508.05748) | — |
| 2026 | arXiv | — | [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) | — |
| 2020 | arXiv | — | [What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams](https://arxiv.org/abs/2009.13081) | — |
| 2026 | arXiv | — | [What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery](https://arxiv.org/abs/2609.31760) | — |
| 2026 | arXiv | — | [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897) | — |
| 2026 | arXiv | — | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) | — |
| 2024 | arXiv | Windows Agent Arena | [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://arxiv.org/abs/2409.08264) | — |
| 2026 | arXiv | — | [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | — |
| 2026 | arXiv | — | [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | — |
| 2025 | arXiv | — | [World Model Implanting for Test-time Adaptation of Embodied Agents](https://arxiv.org/abs/2509.03956) | — |
| 2018 | arXiv | — | [World Models](https://arxiv.org/abs/1803.10122) | [Project](https://worldmodels.github.io/) |
| 2017 | ICML | World of Bits | [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) | — |
| 2026 | ECCV | WorldAgents | [WorldAgents: Can Foundation Image Models be Agents for 3D World Models?](https://arxiv.org/abs/2603.19708) | [Project 1](https://ziyaerkoc.com/worldagents/) · [Project 2](https://www.youtube.com/watch?v=Mj2FqqhurdI) |
| 2025 | arXiv | WorldVLA | [WorldVLA: Towards Autoregressive Action World Model](https://arxiv.org/abs/2506.21539) | — |
| 2025 | arXiv | π^*_0.6 | [π^*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) | — |
| 2025 | arXiv | π_0.5 | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | — |
| 2026 | arXiv | π_0.7 | [π_0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483) | — |
| 2024 | arXiv | π_0 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) | — |

</details>
