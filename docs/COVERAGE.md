# Catalogue coverage and provenance

Bibliography snapshot and catalogue update: **2026-09-30**. Original catalogue assembled: **2026-09-27**. Historical evidence retains its original dates.

| Item | Count |
| --- | ---: |
| Bibliographic keys | 609 |
| Non-paper BibTeX control records (excluded) | 1 |
| Unique works after merging aliases | 607 |
| Existing works preserved | 471 |
| Newly imported works | 136 |
| Works with an arXiv link | 580 |
| Works with code links | 329 |
| Works without an identified paper or arXiv link | 9 |
| Works without an identified code link | 278 |

## Organization and bibliography

The main README groups each unique work by bibliography year and normalized venue. Workshops, Findings, Demos, preprints, journals, and official releases are labeled separately. For a verified preprint/published pair, the published record supplies the displayed year, venue, and title. All current BibTeX keys are preserved in references.bib, including the string definitions and bibliography control record.

The [topic archive](TOPICS.md) preserves previous survey-section assignments. New works whose topic has not been reviewed are assigned to the additional-reference appendix. Active-citation positions in [source-map.json](../data/source-map.json) were refreshed from the current manuscript input graph. Filenames and citation positions are retained without publishing manuscript prose.

## Identity corrections and aliases

The historical catalogue used `chen2026reflect` for Reflect-R1 (arXiv:2606.27922). The current bibliography uses that key for Reflect, Revise, Reuse (arXiv:2609.17653). Reflect-R1 is now recorded under `chen2026reflectr1`; these remain separate works with their own links and evidence.

MMBench-GUI and MobileUse each have a preprint title and a published title for the same arXiv identity. Each pair appears once in the README, while both current BibTeX keys are preserved. Historical aliases and original assignment keys remain in the catalogue evidence. The [bibliography update record](../data/bibliography-update.json) lists migrations, imports, and identity repairs.

| Work | Current citation keys |
| --- | --- |
| MMBench-GUI: A Unified Hierarchical Evaluation Framework for Multi-Platform GUI Agents | `bench_mmbenchgui`, `wang2025mmbenchgui` |
| MobileUse: A Hierarchical Reflection-Driven GUI Agent for Autonomous Mobile Operation | `li2026mobileuse`, `li2025mobileuse` |

## Verification scope

The merged bibliography passed syntax, duplicate-key, manuscript-reference, and BibTeX compilation checks in the source workspace. Selected title, author, and publication details were corrected using official arXiv and conference/publisher metadata before import. These checks do not establish that every venue/year label in the full library has been independently re-audited.

arXiv links preserve previously verified identities or official citation-title checks. New code links may come directly from an author abstract; these use `verified_author_supplied_link` and do not claim a fresh repository availability check. Existing repository checks retain their original dates. Project/model pages remain separate from code. Missing links are curation items; working links do not establish experimental reproducibility.

## Paper links still to identify

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2026 | Blog | — | Harness Engineering for Self-Improvement | — |
| 2026 | Official Release | NVIDIA Isaac GR00T N1.7 | [NVIDIA Isaac GR00T N1.7: A Foundation Model for Generalist Robots](https://github.com/NVIDIA/Isaac-GR00T) | [Code](https://github.com/NVIDIA/Isaac-GR00T) |
| 2026 | Official Release | — | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) | [Project](https://mistral.ai/news/robostral-navigate/) |
| 2026 | ICLR | Vision-r1 | Vision-r1: Incentivizing reasoning capability in multimodal large language models | — |
| 2021 | NeurIPS | — | Align before fuse: Vision and language representation learning with momentum distillation | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |

<details>
<summary>Code links still to identify</summary>

| Year | Venue | Paper Abbr | Paper Title | Project/Code |
| :---: | :---: | :---: | --- | :---: |
| 2026 | CVPR | — | [Active Video Perception: Iterative Evidence Seeking for Agentic Long Video Understanding](https://arxiv.org/abs/2512.05774) | — |
| 2026 | CVPR | ActiveVLA | [ActiveVLA: Injecting Active Perception into Vision-Language-Action Models for Precise 3D Robotic Manipulation](https://arxiv.org/abs/2601.08325) | — |
| 2026 | KDD | — | [Advancing Multimodal Agent Reasoning with Long-Term Neuro-Symbolic Memory](https://arxiv.org/abs/2603.15280) | — |
| 2026 | arXiv | — | [Agent Alpha: Tree Search Unifying Generation, Exploration and Evaluation for Computer-Use Agents](https://arxiv.org/abs/2602.02995) | — |
| 2026 | OpenReview Preprint | — | [Agent harness engineering: A survey](https://openreview.net/forum?id=eONq7FdiHa) | [Project](https://github.com/Picrew/awesome-agent-harness) |
| 2026 | ECCV | — | [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649) | [Project](https://zhangbo135.github.io/agentic-collaborative-cognition/) |
| 2026 | ICML | — | [Agentic Model Predictive Questioning Control in Visual Design](https://openreview.net/forum?id=hvrnTzLyM7) | — |
| 2026 | arXiv | — | [Agentic Retoucher for Text-To-Image Generation](https://arxiv.org/abs/2601.02046) | — |
| 2026 | arXiv | AgenticRL | [AgenticRL: Agentic Reinforcement Learning with Self-Refinement for Complex UAV Navigation](https://arxiv.org/abs/2606.03963) | — |
| 2026 | The 4th AI for Visual Arts Workshop | AgentMV | [AgentMV: A State-Guided Multi-Agent Framework for Budget-Aware Music Video Generation](https://arxiv.org/abs/2605.10723) | — |
| 2026 | CVPR | AGENTSAFE | [AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions](https://arxiv.org/abs/2506.14697) | — |
| 2026 | CVPR | ARM-Thinker | [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](https://arxiv.org/abs/2512.05111) | — |
| 2026 | arXiv | AtomVLA | [AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models](https://arxiv.org/abs/2603.08519) | — |
| 2026 | Official Release | — | [Auditing Prospective Memory in Frozen Language-Model Systems: Causal Mechanisms and the Limits of Naturalistic Trigger Grounding](https://www.preprints.org/manuscript/202608.1081) | [Project](https://www.preprints.org/manuscript/202608.1081) |
| 2026 | arXiv | BaT | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) | — |
| 2026 | arXiv | — | [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](https://arxiv.org/abs/2608.21204) | — |
| 2026 | arXiv | BlueLM-GUI Technical Report | [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents](https://arxiv.org/abs/2609.12394) | — |
| 2026 | CVPR Findings | CarePilot | [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) | — |
| 2026 | ICLR | — | [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | — |
| 2026 | arXiv | — | [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070) | — |
| 2026 | arXiv | CoRe | [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](https://arxiv.org/abs/2607.01721) | — |
| 2026 | ICLR | CP-Agent | [CP-Agent: Context-Aware Multimodal Reasoning for Cellular Morphological Profiling under Chemical Perturbations](https://arxiv.org/abs/2606.03435) | — |
| 2026 | CHI | — | [Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight](https://arxiv.org/abs/2509.10723) | — |
| 2026 | arXiv | — | [Darwinian Memory: A Training-Free Self-Regulating Memory System for GUI Agent Evolution](https://arxiv.org/abs/2601.22528) | — |
| 2026 | arXiv | DataEvolver | [DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation](https://arxiv.org/abs/2606.31537) | — |
| 2026 | arXiv | — | [Design Choices That Matter: A Functional ANOVA Analysis for Remote Sensing Multi-Label Classification](https://arxiv.org/abs/2608.04702) | — |
| 2026 | CVPR | — | [Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols](https://arxiv.org/abs/2512.02787) | — |
| 2026 | arXiv | — | [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | — |
| 2026 | TGRS | DisasterTD | [DisasterTD: Disaster Toponym Disambiguation Using Multimodal LLMs and Cross-View Geolocalization](https://arxiv.org/abs/2607.24856) | — |
| 2026 | arXiv | — | [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/abs/2606.02357) | — |
| 2026 | ACL | — | [Don’t act blindly: Robust gui automation via action-effect verification and self-correction](https://aclanthology.org/2026.acl-long.1335/) | — |
| 2026 | arXiv | Dream-RSI | [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) | [Project](https://github.com/zhengkid/Dream-RSI) |
| 2026 | CVPR | DriveMoE | [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_DriveMoE_Mixture-of-Experts_for_Vision-Language-Action_Model_in_End-to-End_Autonomous_Driving_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2505.16278) | — |
| 2026 | CVPR | EchoTrail-GUI | [EchoTrail-GUI: Building Actionable Memory for GUI Agents via Critic-Guided Self-Exploration](https://arxiv.org/abs/2512.19396) | — |
| 2026 | arXiv | EdgeBench | [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155) | — |
| 2026 | arXiv | EE-MCP | [EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning](https://arxiv.org/abs/2604.09815) | — |
| 2026 | NeurIPS | EfficientVLA | [EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models](https://arxiv.org/abs/2506.10100) | — |
| 2026 | arXiv | ELITE | [ELITE: Experiential Learning and Intent-Aware Transfer for Self-improving Embodied Agents](https://arxiv.org/abs/2603.24018) | — |
| 2026 | arXiv | EVA | [EVA: Efficient Reinforcement Learning for End-to-End Video Agent](https://arxiv.org/abs/2603.22918) | — |
| 2026 | CVPR | EvoGraph-R1 | [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](https://arxiv.org/abs/2607.12764) | — |
| 2026 | CVPR Findings | — | [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | — |
| 2026 | arXiv | EvolveNav | [EvolveNav: Proactive Preflection and Self-Evolving Memory for Zero-Shot Object Goal Navigation](https://arxiv.org/abs/2606.18235) | — |
| 2026 | AAAI | — | [Evolving generalist virtual agents with generative and associative memory](https://ojs.aaai.org/index.php/AAAI/article/view/38300) | — |
| 2026 | arXiv | EvoMemNav | [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509) | — |
| 2026 | ECCV | EvoWorld | EvoWorld: A World-Model-Centric Framework for Continuous Self-Evolution of Modular Embodied Skills | — |
| 2026 | arXiv | EvoX | [EvoX: Meta-Evolution for Automated Discovery](https://arxiv.org/abs/2602.23413) | — |
| 2026 | arXiv | — | [Experience Transfer for Multimodal LLM Agents in Minecraft Game](https://arxiv.org/abs/2604.05533) | — |
| 2026 | arXiv | Fast-ThinkAct | [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) | — |
| 2026 | arXiv | FiRe | [FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation](https://arxiv.org/abs/2604.13491) | — |
| 2026 | CVPR | FLARE | [FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645) | — |
| 2026 | arXiv | — | [Generalized Agent Iteration: One Formal Framework for Iterative Policy Improvement and Recursive Self-Improvement](https://arxiv.org/abs/2609.13406) | — |
| 2026 | Official Release | — | [Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) | [Project](https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/) |
| 2026 | CVPR | GeoMMBench and GeoMMAgent | [GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing](https://arxiv.org/abs/2604.08896) | — |
| 2026 | ICLR | GUI-Shift | [GUI-Shift: Enhancing VLM-Based GUI Agents through Self-supervised Reinforcement Learning](https://arxiv.org/abs/2505.12493) | — |
| 2026 | arXiv | — | [Hard Vision, Easy Vision: What GPT-6 Astra Reveals Across Computer Vision](https://arxiv.org/abs/2609.35718) | — |
| 2026 | Blog | — | Harness Engineering for Self-Improvement | — |
| 2026 | arXiv | — | [Harnessing Agentic Evolution](https://arxiv.org/abs/2605.13821) | — |
| 2026 | ICML | — | [Hierarchical Procedural Meta-Reasoning for Generalizable Multimodal Agents](https://openreview.net/forum?id=v2H2vzRqcr) | — |
| 2026 | arXiv | — | [How Should World Models Be Evaluated for Embodied Decision-Making? A Decision-Making-Centric Position](https://arxiv.org/abs/2606.15032) | — |
| 2026 | arXiv | — | [Hyperagents](https://arxiv.org/abs/2603.19461) | — |
| 2026 | arXiv | ImageEdit-R1 | [ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning](https://arxiv.org/abs/2603.08059) | [Project](https://github.com/zhaoyiran924/ImageEdit-R1) |
| 2026 | arXiv | IntentScore | [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) | — |
| 2026 | CVPR | iSHIFT | [iSHIFT: Lightweight Slow-Fast GUI Agent with Adaptive Perception](https://arxiv.org/abs/2512.22009) | — |
| 2026 | ICLR | — | [Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness](https://arxiv.org/abs/2510.01670) | — |
| 2026 | ICLR | — | [K^2-Agent: Co-Evolving Know-What and Know-How for Hierarchical Mobile Device Control](https://arxiv.org/abs/2603.00676) | — |
| 2026 | arXiv | — | [Kestrel: Grounding Self-Refinement for LVLM Hallucination Mitigation](https://arxiv.org/abs/2603.16664) | — |
| 2026 | arXiv | KnowAct-GUIClaw | [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/abs/2607.12625) | — |
| 2026 | NeurIPS | — | [Learning 3D Persistent Embodied World Models](https://arxiv.org/abs/2505.05495) | — |
| 2026 | arXiv | — | [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | [Project](https://vlaworld.github.io) |
| 2026 | CVPR | LensWalk | [LensWalk: Agentic Video Understanding by Planning How You See in Videos](https://arxiv.org/abs/2603.24558) | — |
| 2026 | ICLR | LongHorizonUI | [LongHorizonUI: A Unified Framework for Robust long-horizon Task Automation of GUI Agent](https://openreview.net/forum?id=BK7Mk5d4WE) | — |
| 2026 | arXiv | MemCtrl | [MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents](https://arxiv.org/abs/2601.20831) | — |
| 2026 | ICLR | — | [Memento: Toward an All-Day Proactive Assistant for Ultra-Long Streaming Video](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b5f4587a0bdb81ecc6ce9d82320a5c2-Abstract-Conference.html) | — |
| 2026 | arXiv | MementoGUI | [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/abs/2605.18652) | — |
| 2026 | ACL | Memory-R1 | [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | — |
| 2026 | CVPR | META | [META: Meta Evolution of Tool Trajectory Adaptation for Long-Video Understanding](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_META_Meta_Evolution_of_Tool_Trajectory_Adaptation_for_Long-Video_Understanding_CVPR_2026_paper.html) | — |
| 2026 | arXiv | MetaForge | [MetaForge: A Self-Evolving Multimodal Agent that Retrieves, Adapts, and Forges Tools On Demand](https://arxiv.org/abs/2606.01801) | — |
| 2026 | arXiv | MetaRSI / RSI2 | [MetaRSI / RSI2: A Meta-Recursive Self-Improving System for Recursive Self-Improving Systems Themselves](https://arxiv.org/abs/2609.06396) | — |
| 2026 | arXiv | MetaSkill-Evolve | [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) | — |
| 2026 | ICLR | MMedAgent-RL | [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) | — |
| 2026 | arXiv | MUSE | [MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction](https://arxiv.org/abs/2606.14168) | — |
| 2026 | arXiv | MuSEAgent | [MuSEAgent: A Multimodal Reasoning Agent with Stateful Experiences](https://arxiv.org/abs/2603.27813) | — |
| 2026 | ECCV | NeuroRefiner | [NeuroRefiner: Morphology-Aware Multi-Agent Refinement for 3D Fluorescence Microscopy Neuron Segmentation](https://arxiv.org/abs/2608.09636) | — |
| 2026 | ICLR | OmniActor | [OmniActor: A Generalist GUI and Embodied Agent for 2D&3D Worlds](https://arxiv.org/abs/2509.02322) | — |
| 2026 | arXiv | OmniHarness | [OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning](https://arxiv.org/abs/2609.16057) | — |
| 2026 | arXiv | OnEvoMemory | [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749) | — |
| 2026 | arXiv | OS-Themis | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) | — |
| 2026 | CVPR | OVOD-Agent | [OVOD-Agent: A Markov-Bandit Framework for Proactive Visual Reasoning and Self-Evolving Detection](https://arxiv.org/abs/2511.21064) | — |
| 2026 | ECCV | — | [Paying More Attention to Visual Tokens in Self-Evolving Large Multimodal Models](https://arxiv.org/abs/2606.27373) | — |
| 2026 | ICLR | PhyScensis | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://arxiv.org/abs/2602.14968) | — |
| 2026 | ICLR | — | [Planning with an Embodied Learnable Memory](https://openreview.net/forum?id=79BOATBal9) | — |
| 2026 | CVPR | Progress-Think | [Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Progress-Think_Semantic_Progress_Reasoning_for_Vision-Language_Navigation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.17097) | — |
| 2026 | arXiv | — | [Proprio: Latent Self-Scoring and Inference-Time Refinement for Physically Plausible Video Generation](https://arxiv.org/abs/2605.28230) | — |
| 2026 | arXiv | Qwen-RobotNav Technical Report | [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) | — |
| 2026 | arXiv | Qwen-UI-Agent Technical Report | [Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric Foundation GUI Agents](https://arxiv.org/abs/2607.28227) | — |
| 2026 | ICLR | R-WoM | [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://doi.org/10.48550/arxiv.2510.11892) · [arXiv](https://arxiv.org/abs/2510.11892) | — |
| 2026 | arXiv | RDA | [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) | — |
| 2026 | arXiv | — | [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378) | — |
| 2026 | arXiv | Recursive Self-Improvement in AI | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | [Project](https://github.com/deepgrounding/recursive-self-improvement) |
| 2026 | arXiv | — | [Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457) | — |
| 2026 | ECCV | ReDesign | [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](https://arxiv.org/abs/2607.25565) | — |
| 2026 | arXiv | RegenHarness | [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | — |
| 2026 | CVPR | ReSAM | [ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images](https://arxiv.org/abs/2511.21606) | — |
| 2026 | ICLR | ReTool | [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) | — |
| 2026 | CVPR | RetouchIQ | [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) | — |
| 2026 | arXiv | — | [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227) | — |
| 2026 | arXiv | RLHarness | [RLHarness: Co-evolving Procedural Skills with Reinforcement Learning for Long-horizon Multimodal Reasoning](https://arxiv.org/abs/2609.32326) | — |
| 2026 | arXiv | Robo-Cortex | [Robo-Cortex: A Self-Evolving Embodied Agent via Dual-Grain Cognitive Memory and Autonomous Knowledge Induction](https://arxiv.org/abs/2605.18729) | — |
| 2026 | Official Release | — | [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) | [Project](https://mistral.ai/news/robostral-navigate/) |
| 2026 | arXiv | RSIAgent | [RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments](https://arxiv.org/abs/2609.15364) | — |
| 2026 | arXiv | — | [Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation](https://arxiv.org/abs/2608.24138) | — |
| 2026 | arXiv | — | [Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks](https://arxiv.org/abs/2606.27147) | — |
| 2026 | CVPR | SAGE | [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | [Project](https://research.nvidia.com/labs/dir/sage/) |
| 2026 | CVPR | — | [Scaling Agentic Reinforcement Learning for Tool-Integrated Reasoning in VLMs](https://arxiv.org/abs/2511.19773) | — |
| 2026 | CVPR Workshops | — | [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | — |
| 2026 | CVPR | SciEducator | [SciEducator: Scientific Video Understanding and Educating via Deming-Cycle Multi-Agent System](https://arxiv.org/abs/2511.17943) | — |
| 2026 | arXiv | SCOPE | [SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation](https://arxiv.org/abs/2605.08043) | — |
| 2026 | arXiv | SEA-Eval | [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988) | — |
| 2026 | arXiv | — | [Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation](https://arxiv.org/abs/2603.08260) | — |
| 2026 | arXiv | — | [Self-Adaptive VLA for Robust Robot Deployment](https://arxiv.org/abs/2609.30092) | — |
| 2026 | ECCV | — | [Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution](https://arxiv.org/abs/2606.28971) | — |
| 2026 | arXiv | — | [Self-Evolving Visual Questioner](https://arxiv.org/abs/2606.13929) | — |
| 2026 | ICLR | — | [Self-Improving Vision-Language-Action Models with Data Generation via Residual RL](https://arxiv.org/abs/2511.00091) | — |
| 2026 | ICLR | — | [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) | [Project](https://sites.google.com/utexas.edu/armor) |
| 2026 | arXiv | — | [Self-Supervised Bootstrapping of Action-Predictive Embodied Reasoning](https://arxiv.org/abs/2602.08167) | — |
| 2026 | NeurIPS | — | [Sherlock: Self-Correcting Reasoning in Vision-Language Models](https://arxiv.org/abs/2505.22651) | — |
| 2026 | arXiv | SIA | [SIA: Self Improving AI with Harness & Weight Updates](https://arxiv.org/abs/2605.27276) | — |
| 2026 | arXiv | — | [Skill-Guided Continuation Distillation for GUI Agents](https://arxiv.org/abs/2606.18890) | — |
| 2026 | arXiv | SpatialEvo | [SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments](https://arxiv.org/abs/2604.14144) | — |
| 2026 | AAAI | — | [Talk2Image: A Multi-Agent System for Multi-Turn Image Generation and Editing](https://arxiv.org/abs/2508.06916) | — |
| 2026 | arXiv | — | [The Essence of Balance for Self-Improving Agents in Vision-and-Language Navigation](https://arxiv.org/abs/2604.19064) | — |
| 2026 | arXiv | — | [The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement](https://arxiv.org/abs/2609.11873) | [Project](https://github.com/theseus-labs-rsi/awesome-rsi) |
| 2026 | arXiv | — | [The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | — |
| 2026 | ECCV | TIR-Agent | [TIR-Agent: Training an Explorative and Efficient Agent for Image Restoration](https://arxiv.org/abs/2603.27742) | — |
| 2026 | arXiv | UI-Mem | [UI-Mem: Self-Evolving Experience Memory for Online Reinforcement Learning in Mobile GUI Agents](https://arxiv.org/abs/2602.05832) | [Project](https://ui-mem.github.io) |
| 2026 | arXiv | UI-Oceanus | [UI-Oceanus: Scaling GUI Agents with Synthetic Environmental Dynamics](https://arxiv.org/abs/2604.02345) | — |
| 2026 | arXiv | — | [Unifying Language-Action Understanding and Generation for Autonomous Driving](https://arxiv.org/abs/2603.01441) | — |
| 2026 | CVPR | — | [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) | — |
| 2026 | ICLR | Video-STAR | [Video-STAR: Reinforcing Open-Vocabulary Action Recognition with Tools](https://arxiv.org/abs/2510.08480) | — |
| 2026 | NeurIPS | VideoChat-R1.5 | [VideoChat-R1.5: Visual Test-Time Scaling to Reinforce Multimodal Reasoning by Iterative Perception](https://arxiv.org/abs/2509.21100) | — |
| 2026 | arXiv | VideoResearcher | [VideoResearcher: Self-Improving Tool Design for Long-Video Understanding](https://arxiv.org/abs/2609.19664) | — |
| 2026 | arXiv | VISA | [VISA: Agentic Self-Evolving Data Synthesis for Multimodal Instruction Following](https://arxiv.org/abs/2608.26013) | — |
| 2026 | arXiv | ViSAGE | [ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding](https://arxiv.org/abs/2607.28678) | — |
| 2026 | ECCV | VisCritic | [VisCritic: Visual State Comparison as Process Reward for GUI Agents](https://arxiv.org/abs/2606.24525) | — |
| 2026 | CVPR | Vision-R1 | [Vision-R1: Evolving Human-Free Alignment in Large Vision-Language Models via Vision-Guided Reinforcement Learning](https://arxiv.org/abs/2503.18013) | — |
| 2026 | ICLR | Vision-r1 | Vision-r1: Incentivizing reasoning capability in multimodal large language models | — |
| 2026 | CVPR | VISTA | [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2510.15831) | — |
| 2026 | arXiv | — | [Visual Reasoning through Tool-supervised Reinforcement Learning](https://arxiv.org/abs/2604.19945) | — |
| 2026 | NeurIPS | VL-Rethinker | [VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning](https://arxiv.org/abs/2504.08837) | — |
| 2026 | NeurIPS | VLA-Cache | [VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching](https://arxiv.org/abs/2502.02175) | — |
| 2026 | arXiv | VLAW | [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) | [Project 1](https://sites.google.com/view/vla-w) · [Project 2](https://sites.google.com/view/vlaw-arxiv) |
| 2026 | arXiv | WAM4D | [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](https://arxiv.org/abs/2606.14048) | — |
| 2026 | ICLR | — | [Webwatcher: Breaking new frontiers of vision-language deep research agent](https://arxiv.org/abs/2508.05748) | — |
| 2026 | arXiv | — | [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) | — |
| 2026 | arXiv | — | [What Stops Recursive Self-Improvement in Robotics? Lessons from 123 Rounds of Agentic Skill Discovery](https://arxiv.org/abs/2609.31760) | — |
| 2026 | arXiv | — | [When History Is Multimodal: Rethinking Context Management for Long-Horizon Agents](https://arxiv.org/abs/2608.29897) | — |
| 2026 | arXiv | — | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) | — |
| 2026 | arXiv | — | [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | — |
| 2026 | ECCV | WorldAgents | [WorldAgents: Can Foundation Image Models be Agents for 3D World Models?](https://arxiv.org/abs/2603.19708) | [Project 1](https://ziyaerkoc.com/worldagents/) · [Project 2](https://www.youtube.com/watch?v=Mj2FqqhurdI) |
| 2026 | arXiv | π_0.7 | [π_0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483) | — |
| 2025 | arXiv | — | [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228) | — |
| 2025 | arXiv | — | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | [Project](https://github.com/CharlesQ9/Self-Evolving-Agents) |
| 2025 | CASE | — | [A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees](https://arxiv.org/abs/2503.15202) | — |
| 2025 | arXiv | Active-o3 | [Active-o3: Empowering multimodal large language models with active perception via grpo](https://arxiv.org/abs/2505.21457) | — |
| 2025 | arXiv | — | [Can We Detect Failures Without Failure Data? Uncertainty-Aware Runtime Failure Detection for Imitation Learning Policies](https://arxiv.org/abs/2503.08558) | — |
| 2025 | CVPR | Code-as-Monitor | [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | [Project](https://zhoues.github.io/Code-as-Monitor/) |
| 2025 | ICLR | — | [Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback](https://arxiv.org/abs/2410.08852) | — |
| 2025 | NeurIPS | CPathAgent | [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://doi.org/10.52202/085713-3404) · [arXiv](https://arxiv.org/abs/2505.20510) | — |
| 2025 | NeurIPS | CREA | [CREA: A Collaborative Multi-Agent Framework for Creative Image Editing and Generation](https://doi.org/10.52202/085713-5705) · [arXiv](https://arxiv.org/abs/2504.05306) | — |
| 2025 | arXiv | Ctrl-World | [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125) | — |
| 2025 | ICCV | DWIM | [DWIM: Towards Tool-aware Visual Reasoning via Discrepancy-aware Workflow Generation & Instruct-Masking Tuning](https://arxiv.org/abs/2503.19263) | — |
| 2025 | ICLR | EMOS | [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | — |
| 2025 | NAACL Findings | — | [Enhancing Visual-Language Modality Alignment in Large Vision Language Models via Self-Improvement](https://arxiv.org/abs/2405.15973) | — |
| 2025 | arXiv | FailSafe | [FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models](https://arxiv.org/abs/2510.01642) | [Project](https://jimntu.github.io/FailSafe) |
| 2025 | arXiv | — | [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) | — |
| 2025 | arXiv | — | [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://arxiv.org/abs/2510.03342) | — |
| 2025 | arXiv | GUI-R1 | [GUI-R1 : A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458) | — |
| 2025 | arXiv | — | [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | [Project](https://www.pi.website/research/hirobot) |
| 2025 | ICCV | — | [Iris: Breaking GUI Complexity with Adaptive Focus and Self-Refining](https://arxiv.org/abs/2412.10342) | — |
| 2025 | NeurIPS | LabUtopia | [LabUtopia: High-Fidelity Simulation and Hierarchical Benchmark for Scientific Embodied Agents](https://doi.org/10.52202/085713-1158) · [arXiv](https://arxiv.org/abs/2505.22634) | — |
| 2025 | EMNLP | LATTE | [LATTE: Learning to Think with Vision Specialists](https://arxiv.org/abs/2412.05479) | — |
| 2025 | arXiv | — | [Learning Semantic Atomic Skills for Multi-Task Robotic Manipulation](https://arxiv.org/abs/2512.18368) | [Project](https://atom-skill.github.io) |
| 2025 | ICCV | — | [Less is More: Empowering GUI Agent with Context-Aware Simplification](https://arxiv.org/abs/2507.03730) | — |
| 2025 | arXiv | — | [Look, Zoom, Understand: The Robotic Eyeball for Embodied Perception](https://arxiv.org/abs/2511.15279) | — |
| 2025 | CVPR | — | [Magma: A Foundation Model for Multimodal AI Agents](https://arxiv.org/abs/2502.13130) | — |
| 2025 | arXiv | — | [Marmot: Object-Level Self-Correction via Multi-Agent Reasoning](https://arxiv.org/abs/2504.20054) | — |
| 2025 | RSS | NaVILA | [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453) | [Project](https://navila-bot.github.io/) |
| 2025 | arXiv | OneTwoVLA | [OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning](https://arxiv.org/abs/2505.11917) | — |
| 2025 | ICLR | OS-ATLAS | [OS-ATLAS: Foundation action model for generalist GUI agents](https://arxiv.org/abs/2410.23218) | — |
| 2025 | arXiv | — | [Planning with Reasoning using Vision Language World Model](https://arxiv.org/abs/2509.02722) | — |
| 2025 | ECIR | PlotEdit | [PlotEdit: Natural Language-Driven Accessible Chart Editing in PDFs via Multimodal LLM Agents](https://arxiv.org/abs/2501.11233) | — |
| 2025 | ACL Findings | — | [Ponder & Press: Advancing Visual GUI Agent towards General Computer Control](https://arxiv.org/abs/2412.01268) | [Project](https://invinciblewyq.github.io/ponder-press-page/) |
| 2025 | ICCV | R1-VL | [R1-VL: Learning to Reason with Multimodal Large Language Models via Step-wise Group Relative Policy Optimization](https://arxiv.org/abs/2503.12937) | — |
| 2025 | arXiv | — | [Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning](https://arxiv.org/abs/2509.16136) | — |
| 2025 | arXiv | RFTF | [RFTF: Reinforcement Fine-tuning for Embodied Agents with Temporal Feedback](https://arxiv.org/abs/2505.19767) | — |
| 2025 | arXiv | RoboChemist | [RoboChemist: Long-Horizon and Safety-Compliant Robotic Chemical Experimentation](https://arxiv.org/abs/2509.08820) | [Project](https://zzongzheng0918.github.io/RoboChemist.github.io/) |
| 2025 | arXiv | RoboMemory | [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415) | — |
| 2025 | arXiv | RoboMonkey | [RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models](https://arxiv.org/abs/2506.17811) | — |
| 2025 | IROS | — | [Robots that Suggest Safe Alternatives](https://arxiv.org/abs/2409.09883) | — |
| 2025 | arXiv | RSAgent | [RSAgent: Learning to Reason and Act for Text-Guided Segmentation via Multi-Turn Tool Invocations](https://arxiv.org/abs/2512.24023) | — |
| 2025 | arXiv | — | [Scaling Agents for Computer Use](https://arxiv.org/abs/2510.02250) | — |
| 2025 | arXiv | SE-VLN | [SE-VLN: A Self-Evolving Vision-Language Navigation Framework Based on Multimodal Large Language Models](https://arxiv.org/abs/2507.13152) | — |
| 2025 | CVPR | — | [Self-Evolving Visual Concept Library using Vision-Language Critics](https://arxiv.org/abs/2504.00185) | — |
| 2025 | EMNLP Findings | — | [Self-Improvement in Multimodal Large Language Models: A Survey](https://arxiv.org/abs/2510.02665) | — |
| 2025 | arXiv | — | [Semantic World Models](https://arxiv.org/abs/2510.19818) | [Project](https://weirdlabuw.github.io/swm) |
| 2025 | CVPR | SimLingo | [SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment](https://openaccess.thecvf.com/content/CVPR2025/html/Renz_SimLingo_Vision-Only_Closed-Loop_Autonomous_Driving_with_Language-Action_Alignment_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09594) | — |
| 2025 | NeurIPS | SketchMind | [SketchMind: A Multi-Agent Cognitive Framework for Assessing Student-Drawn Scientific Sketches](https://doi.org/10.52202/085713-2774) · [arXiv](https://arxiv.org/abs/2507.22904) | — |
| 2025 | arXiv | SpatialVLA | [SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model](https://arxiv.org/abs/2501.15830) | — |
| 2025 | arXiv | STORM | [STORM: Search-Guided Generative World Models for Robotic Manipulation](https://arxiv.org/abs/2512.18477) | — |
| 2025 | arXiv | StreamVLN | [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://arxiv.org/abs/2507.05240) | — |
| 2025 | arXiv | — | [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) | — |
| 2025 | arXiv | — | [Towards Agentic AI for Multimodal-Guided Video Object Segmentation](https://arxiv.org/abs/2508.10572) | — |
| 2025 | arXiv | UI-TARS-2 Technical Report | [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544) | — |
| 2025 | arXiv | UI-TARS | [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) | — |
| 2025 | arXiv | — | [Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models](https://arxiv.org/abs/2503.01876) | — |
| 2025 | CVPR | V-Stylist | [V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents](https://arxiv.org/abs/2503.12077) | — |
| 2025 | CVPR | Video-MME | [Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis](https://arxiv.org/abs/2405.21075) | [Project](https://video-mme.github.io) |
| 2025 | ICLR | Video-STaR | [Video-STaR: Self-Training Enables Video Instruction Tuning with Any Supervision](https://arxiv.org/abs/2407.06189) | [Project](https://orrzohar.github.io/projects/video-star/) |
| 2025 | arXiv | — | [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | — |
| 2025 | arXiv | VideoAgent2 | [VideoAgent2: Enhancing the LLM-Based Agent System for Long-Form Video Understanding by Uncertainty-Aware CoT](https://arxiv.org/abs/2504.04471) | — |
| 2025 | arXiv | ViReSkill | [ViReSkill: Vision-Grounded Replanning with Skill Memory for LLM-Based Planning in Lifelong Robot Learning](https://arxiv.org/abs/2509.24219) | — |
| 2025 | arXiv | VisualToolAgent (VisTA) | [VisualToolAgent (VisTA): A Reinforcement Learning Framework for Visual Tool Selection](https://arxiv.org/abs/2505.20289) | — |
| 2025 | arXiv | VLN-R1 | [VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.17221) | — |
| 2025 | arXiv | WebCoach | [WebCoach: Self-Evolving Web Agents with Cross-Session Memory Guidance](https://arxiv.org/abs/2511.12997) | — |
| 2025 | arXiv | — | [World Model Implanting for Test-time Adaptation of Embodied Agents](https://arxiv.org/abs/2509.03956) | — |
| 2025 | arXiv | π^*_0.6 | [π^*_0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759) | — |
| 2025 | arXiv | π_0.5 | [π_0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) | — |
| 2024 | arXiv | AutoRT | [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963) | — |
| 2024 | ICLR | — | [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | — |
| 2024 | ICLR | CRITIC | [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738) | — |
| 2024 | ECCV | DetToolChain | [DetToolChain: A New Prompting Paradigm to Unleash Detection Ability of MLLM](https://arxiv.org/abs/2403.12488) | — |
| 2024 | arXiv | — | [Efficient Self-Improvement in Multimodal Large Language Models: A Model-Level Judge-Free Approach](https://arxiv.org/abs/2411.17760) | — |
| 2024 | ICML | — | [Genie: Generative Interactive Environments](https://arxiv.org/abs/2402.15391) | [Project](https://sites.google.com/corp/view/genie-2024/) |
| 2024 | IUI | LAVE | [LAVE: LLM-Powered Agent Assistance and Language Augmentation for Video Editing](https://arxiv.org/abs/2402.10294) | — |
| 2024 | ECCV | LLaVA-Plus | [LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents](https://arxiv.org/abs/2311.05437) | — |
| 2024 | arXiv | MOKA | [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | — |
| 2024 | arXiv | NaVid | [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852) | — |
| 2024 | arXiv | — | [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) | — |
| 2024 | ECCV | OmniACT | [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553) | — |
| 2024 | arXiv | OpenVLA | [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | — |
| 2024 | ICML | PIVOT | [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://arxiv.org/abs/2402.07872) | [Project 1](http://pivot-prompt.github.io) · [Project 2](https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo) |
| 2024 | arXiv | — | [Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419) | [Project](https://www.kaggle.com/datasets/googleai/pasta-data) |
| 2024 | NeurIPS | RestoreAgent | [RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models](https://doi.org/10.52202/079017-3512) · [arXiv](https://arxiv.org/abs/2407.18035) | — |
| 2024 | arXiv | RLDG | [RLDG: Robotic Generalist Policy Distillation via Reinforcement Learning](https://arxiv.org/abs/2412.09858) | [Project](https://generalist-distillation.github.io) |
| 2024 | arXiv | RoboPoint | [RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics](https://arxiv.org/abs/2406.10721) | — |
| 2024 | arXiv | RT-H | [RT-H: Action Hierarchies Using Language](https://arxiv.org/abs/2403.01823) | — |
| 2024 | ICML | SceneCraft | [SceneCraft: An LLM Agent for Synthesizing 3D Scenes as Blender Code](https://arxiv.org/abs/2403.01248) | — |
| 2024 | CVPR | — | [Self-correcting LLM-controlled Diffusion Models](https://arxiv.org/abs/2311.16090) | — |
| 2024 | CVPR | SkillDiffuser | [SkillDiffuser: Interpretable Hierarchical Planning via Skill Abstractions in Diffusion-Based Task Execution](https://arxiv.org/abs/2312.11598) | — |
| 2024 | arXiv | SPIRE | [SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation](https://arxiv.org/abs/2410.18065) | — |
| 2024 | ECCV | — | [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving (in CARLA-v2)](https://arxiv.org/abs/2402.16720) | — |
| 2024 | ECCV | VideoAgent | [VideoAgent: Long-form Video Understanding with Large Language Model as Agent](https://arxiv.org/abs/2403.10517) | — |
| 2024 | ACL | VisualWebArena | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | — |
| 2024 | ACL | WebVoyager | [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://arxiv.org/abs/2401.13919) | — |
| 2024 | arXiv | π_0 | [π_0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) | — |
| 2023 | NeurIPS | AVIS | [AVIS: Autonomous Visual Information Seeking with Large Language Model Agent](https://doi.org/10.52202/075280-0040) · [arXiv](https://arxiv.org/abs/2306.08129) | — |
| 2023 | ICML | BLIP-2 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) | — |
| 2023 | arXiv | — | [Gemini: A Family of Highly Capable Multimodal Models](https://arxiv.org/abs/2312.11805) | — |
| 2023 | CVPR | InstructPix2Pix | [InstructPix2Pix: Learning to Follow Image Editing Instructions](https://arxiv.org/abs/2211.09800) | [Project](https://www.timothybrooks.com/instruct-pix2pix) |
| 2023 | NeurIPS | LIBERO | [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310) | [Project](https://libero-project.github.io) |
| 2023 | arXiv | PaLM-E | [PaLM-E: An Embodied Multimodal Language Model](https://arxiv.org/abs/2303.03378) | — |
| 2023 | CVPR | — | [Planning-oriented Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Planning-Oriented_Autonomous_Driving_CVPR_2023_paper.html) · [arXiv](https://arxiv.org/abs/2212.10156) | — |
| 2023 | arXiv | RoboCat | [RoboCat: A Self-Improving Generalist Agent for Robotic Manipulation](https://arxiv.org/abs/2306.11706) | — |
| 2023 | CoRL | RT-2 | [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | [Project](https://robotics-transformer.github.io/) |
| 2023 | NeurIPS | — | [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) | — |
| 2022 | NeurIPS | — | [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198) | — |
| 2022 | arXiv | — | [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125) | — |
| 2021 | NeurIPS | — | Align before fuse: Vision and language representation learning with momentum distillation | — |
| 2019 | Neural Networks | — | [Continual Lifelong Learning with Neural Networks: A Review](https://arxiv.org/abs/1802.07569) | — |
| 2019 | CVPR | GQA | [GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506) | — |
| 2018 | arXiv | — | [World Models](https://arxiv.org/abs/1803.10122) | [Project](https://worldmodels.github.io/) |
| 2016 | ICLR | — | [Policy Distillation](https://arxiv.org/abs/1511.06295) | — |
| 2011 | AISTATS | — | [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://proceedings.mlr.press/v15/ross11a.html) · [arXiv](https://arxiv.org/abs/1011.0686) | [Project](https://proceedings.mlr.press/v15/ross11a.html) |
| 2009 | ICML | — | [Curriculum learning](https://icml.cc/2009/papers/119.pdf) | — |
| 1999 | Artificial Intelligence | Between MDPs and semi-MDPs | [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | — |
| 1998 | Artificial Intelligence | — | [Planning and Acting in Partially Observable Stochastic Domains](https://doi.org/10.1016/S0004-3702(98)00023-X) | — |
| 1991 | Artificial Intelligence | — | Animate vision | — |
| 1990 | ICPR | — | Purposive and qualitative active vision | — |

</details>
