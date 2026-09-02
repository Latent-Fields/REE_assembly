Research Note: Developmental Ecology Assays — Preliminary Novelty and Neighbour Scan

Status: preliminary literature scan — not a systematic review; do not ingest as an REE architecture claim

Date: 2026-09-02
Purpose: Test whether the developmental-ecology-assay idea discovered in the 2026-09-02 voice discussion is already established elsewhere, identify its closest neighbours, and sharpen the first falsifiable experiment.

---

## Bottom line

The component ideas are not individually new.

There is substantial prior work on:

* developmental robotics and staged individual/social/language learning;
* intrinsic motivation, computational value systems and self-generated goals;
* critical learning periods and path dependence in artificial networks;
* artificial-life model organisms;
* automatic environment/curriculum design for reinforcement learning;
* autonomous agents used to playtest games and simulations;
* model organisms of misalignment in AI safety;
* biological developmental bioassays that infer properties of an exposure from organism-level outcomes.

The **candidate distinctive combination** is narrower:

> Use a standardised, persistently developing artificial organism population as a bioassay-like probe, hold the probe protocol stable, and characterise an information environment primarily by the distribution and causal history of phenotypes it produces rather than by agent score, coverage or task success.

The strongest additional differentiators would be:

1. matched adult environments after controlled divergent childhoods;
2. explicit separation of intrinsic harm/benefit/value channels from emergent goals/strategies;
3. organism-level internal causal instrumentation across development (prediction, attribution, replay, commitment, counterfactuals);
4. reference-organism and population modes;
5. a versioned organism library spanning cognitive ontologies.

This should be treated as a **candidate research gap**, not a novelty claim, until a systematic search is completed.

---

## 1. Developmental robotics — close conceptual neighbour

The ITALK developmental robotics programme explicitly studied how three learning domains scaffold one another: individual learning about embodiment/environment, social learning, and linguistic learning.

This strongly supports the proposed REE framing of capacity boundaries as individual → social → linguistic developmental regimes. It also warns against claiming that staged cognitive ontologies themselves are novel.

Reference:

* Broz F, Nehaniv CL, Belpaeme T, et al. *The ITALK Project: A Developmental Robotics Approach to the Study of Individual, Social, and Linguistic Learning.* Topics in Cognitive Science. 2014. https://doi.org/10.1111/tops.12099

Relevant implication:

> The interesting REE question is not whether capacities can scaffold one another; it is whether retaining standardised pre-social/social preparations and bridge strains yields a cleaner causal science of those transitions.

---

## 2. Computational value systems and intrinsic motivation — direct neighbour to value-versus-goal distinction

Developmental cognitive robotics has an established literature on innate/acquired value systems and intrinsic motivation. It explicitly distinguishes mechanisms that direct attention/learning from externally specified task rewards.

Autotelic reinforcement learning goes further by studying agents that generate and pursue their own goals rather than receiving a fixed goal set.

References:

* Merrick KE. *Value systems for developmental cognitive robotics: A survey.* Cognitive Systems Research. 2017;41:38-55. https://doi.org/10.1016/j.cogsys.2016.08.001
* Colas C, Karch T, Sigaud O, Oudeyer P-Y. *Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: a Short Survey.* 2020. https://arxiv.org/abs/2012.09830
* Nisioti E, Masquil E, Hamon G, Moulin-Frier C. *Autotelic Reinforcement Learning in Multi-Agent Environments.* Conference on Lifelong Learning Agents 2023. https://proceedings.mlr.press/v232/nisioti23a.html

Relevant implication:

> “Intrinsic values are not goals” is an important REE/programme distinction but should not be presented as a new field-level concept. The possible contribution is using that distinction inside a controlled developmental assay with longitudinal causal readouts.

---

## 3. Critical learning periods — strong evidence that artificial childhood can matter

Deep networks can exhibit critical learning periods in which temporary early deficits cause lasting changes in later behaviour or representation.

Achille et al. showed early sensory deficits can have persistent effects in deep networks. Kleinman et al. later showed analogous critical-period dynamics even in analytically tractable deep linear networks, suggesting the phenomenon can emerge from general learning dynamics rather than requiring biological hardware. Work on multisensory integration likewise found early correlated exposure can permanently influence later integration.

References:

* Achille A, Rovere M, Soatto S. *Critical Learning Periods in Deep Networks.* ICLR 2019. https://openreview.net/forum?id=BkeStsCcKQ
* Kleinman M, Achille A, Soatto S. *Critical Learning Periods for Multisensory Integration in Deep Networks.* CVPR 2023. https://openaccess.thecvf.com/content/CVPR2023/html/Kleinman_Critical_Learning_Periods_for_Multisensory_Integration_in_Deep_Networks_CVPR_2023_paper.html
* Kleinman M, Achille A, Soatto S. *Critical Learning Periods Emerge Even in Deep Linear Networks.* ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/f358b2a880adf34939d2d6f926e54d2a-Abstract-Conference.html

Relevant implication:

> “Same adulthood, different childhood” cannot be novel merely because early training matters. A stronger experiment must ask what persistent *organism-level causal phenotype* develops, preferably while matching simple reinforcement burden and exposing interpretable internal mechanisms.

---

## 4. Curriculum learning and Unsupervised Environment Design — opposite-direction neighbour

Unsupervised Environment Design (UED), Adversarially Compounding Complexity by Editing Levels (ACCEL), and Multi-Agent Environment Design Strategist for Open-Ended Learning (MAESTRO) automatically generate or select environments to produce more robust/general reinforcement-learning agents.

References:

* Parker-Holder J, Jiang M, Dennis M, et al. *Evolving Curricula with Regret-Based Environment Design.* ICML 2022. https://proceedings.mlr.press/v162/parker-holder22a.html
* Samvelyan M, Khan A, Dennis M, et al. *MAESTRO: Open-Ended Environment Design for Multi-Agent Reinforcement Learning.* ICLR 2023. https://discovery.ucl.ac.uk/id/eprint/10216733/

The developmental ecology assay is potentially differentiated by reversing the scientific target:

* UED: manipulate environments to improve the learner.
* Developmental ecology assay: standardise the learner/probe so its developmental response measures the environment.

This distinction should be made explicit in any paper.

---

## 5. Artificial life and digital organisms — strong precedent for organism-as-experimental-object

Avida established digital organisms as experimentally controllable objects for evolutionary biology, with precise environmental control and rich measurement. Populations of digital organisms have been used to study evolutionary mechanisms, ecology and speciation.

References:

* Ofria C, Wilke CO. *Avida: A Software Platform for Research in Computational Evolutionary Biology.* Artificial Life. 2004;10(2):191-229. https://doi.org/10.1162/106454604773563612
* Ortega R, Wulff E, Fortuna MA. *Ontology for the Avida digital evolution platform.* Scientific Data. 2023;10:608. https://doi.org/10.1038/s41597-023-02514-3

Relevant implication:

> Digital organisms themselves are well established. REE's potential contribution would be a highly instrumented *developmental cognitive* organism in which individual biography, replay, attribution, commitment and internal predictive state can be manipulated and inspected.

---

## 6. Automated playtesting — practical neighbour and important product comparator

Game research and industry already use reinforcement-learning agents to explore game states, increase test coverage, identify exploits, estimate difficulty and evaluate design choices.

Electronic Arts has reported reinforcement-learning playtesting in production-oriented work, and academic work has used autonomous agents to answer designer questions through thousands of simulations.

References:

* De Mesentier Silva F, Borovikov I, Kolen J, Aghdaie N, Zaman K. *Exploring Gameplay With AI Agents.* AIIDE 2018. https://doi.org/10.1609/aiide.v14i1.13034
* Gordillo C, Bergdahl J, Tollmar K, Gisslén L. *Improving Playtesting Coverage via Curiosity Driven Reinforcement Learning Agents.* 2021. https://arxiv.org/abs/2103.13798
* Electronic Arts SEED. *Augmenting Automated Game Testing with Deep Reinforcement Learning.* 2020. https://www.ea.com/seed/news/automated-game-testing-deep-reinforcement-learning
* Gillberg J, Bergdahl J, Sestini A, Eakins A, Gisslén L. *Technical Challenges of Deploying Reinforcement Learning Agents for Game Testing in AAA Games.* 2023. https://arxiv.org/abs/2307.11105

Relevant implication:

> A product cannot differentiate itself merely by dropping autonomous agents into a simulator. The discriminator must be whether developmental phenotype reports reveal useful structure missed by coverage, score, success rate or conventional behavioural testing.

---

## 7. Biological bioassays — perhaps the closest methodological analogy

Environmental toxicology already uses standardised organisms and defined developmental exposures to infer properties of an environment or chemical from organism-level phenotypes.

Embryo/larval assays quantify multiple developmental, physiological and behavioural endpoints; test validity depends on standardised organisms, controls, exposure conditions and reproducible readouts.

References:

* National Research Council. *Using Model Animals to Assess and Understand Developmental Toxicity.* In: Scientific Frontiers in Developmental Toxicology and Risk Assessment. National Academies Press, 2000. https://www.ncbi.nlm.nih.gov/books/NBK225677/
* Fraysse B, Mons R, Garric J. *Development of a zebrafish 4-day embryo-larval bioassay to assess toxicity of chemicals.* Ecotoxicology and Environmental Safety. 2006;63(2):253-267. https://doi.org/10.1016/j.ecoenv.2004.10.015
* OECD. *Test No. 210: Fish, Early-life Stage Toxicity Test.* https://www.oecd.org/en/publications/test-no-210-fish-early-life-stage-toxicity-test_9789264203785-en.html

Relevant implication:

> The term **assay** has real methodological content. A serious developmental ecology assay would need probe quality controls, reference conditions, replicates, acceptance criteria, validated endpoints and a clear domain of inference.

This analogy is stronger than using “assay” only as a metaphor.

---

## 8. AI-safety model organisms — direct precedent for clean artificial pathologies

AI-safety researchers explicitly construct “model organisms of misalignment” so failures can be induced reproducibly and studied mechanistically.

Recent emergent-misalignment work has deliberately built small, clean model organisms that isolate narrow training interventions and corresponding behavioural/mechanistic phase transitions.

References:

* Hubinger E, et al. *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training.* 2024. https://arxiv.org/abs/2401.05566
* Turner E, Soligo A, Taylor M, Rajamanoharan S, Nanda N. *Model Organisms for Emergent Misalignment.* 2025. https://arxiv.org/abs/2506.11613
* Betley J, et al. *Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs.* ICML 2025. https://proceedings.mlr.press/v267/betley25a.html

Relevant implication:

> The “model organism” framing is already legitimate vocabulary in AI safety. REE could potentially extend it from induced post-training pathologies to longitudinal developmental organisms with rewindable biographies.

---

## 9. Training path dependence and safety curricula — alignment relevance already exists

Alignment discussions have explicitly identified path dependence as sensitivity of final model behaviour/internal structure to details of the training trajectory. Recent safety-alignment work also uses curriculum ordering to improve out-of-distribution safety performance.

References:

* Hebbar V, Hubinger E. *Path dependence in ML inductive biases.* AI Alignment Forum, 2022. https://www.alignmentforum.org/posts/bxkWd6WdkPqGmdHEk/path-dependence-in-ml-inductive-biases
* Kumar S, Smith V, Yadav C. *Curriculum Learning for Safety Alignment.* 2026. https://arxiv.org/abs/2605.26315
* Lin J, Li M, Zhao X, et al. *Curriculum-RLAIF: Curriculum Alignment with Reinforcement Learning from AI Feedback.* Findings of ACL 2026. https://aclanthology.org/2026.findings-acl.1685/

Relevant implication:

> Alignment researchers are not wholly ignoring training history. The stronger gap is that the dominant unit remains training dynamics of a model toward alignment outcomes, not a bioassay-like programme using standardised developing organisms to characterise ecologies.

---

## 10. Controllability / learned helplessness — useful first assay, but established phenomenon

Learned helplessness and behavioural controllability have extensive psychological and computational literature. Formal models have treated perceived control over affectively charged outcomes using reinforcement-learning and Bayesian ideas. Artificial reinforcement-learning systems have also shown early-punishment effects described as learned helplessness.

References:

* Huys QJM, Dayan P. *A Bayesian formulation of behavioral control.* Cognition. 2009;113(3):314-328. https://doi.org/10.1016/j.cognition.2009.01.008
* Teodorescu K, Erev I. *Learned helplessness and learned prevalence: exploring the causal relations among perceived controllability, reward prevalence, and exploration.* Psychological Science. 2014;25(10). https://doi.org/10.1177/0956797614543022
* Derhami V, Youhannaei Z. *Demonstration of Learned Helplessness with Fuzzy Reinforcement Learning.* JCIS 2008. https://doi.org/10.2991/jcis.2008.8

Relevant implication:

> A controllability assay is scientifically legible but cannot claim novelty from reproducing helplessness in an artificial agent. It becomes useful if it demonstrates the assay methodology and distinguishes causal developmental explanations available in REE from simple reward-history explanations.

---

## Preliminary novelty matrix

| Idea | Existing neighbour | Preliminary assessment |
|---|---|---|
| Developmental artificial agents | Developmental robotics | Established |
| Individual → social → linguistic staging | ITALK/developmental robotics | Established neighbour |
| Intrinsic value distinct from external task reward | Value systems / intrinsic motivation | Established |
| Self-generated goals | Autotelic RL | Established |
| Early experience causes persistent effects | Critical-period/path-dependence work | Established |
| Digital organisms as experimental objects | Avida/artificial life | Established |
| Agents used to evaluate games/worlds | Automated playtesting | Established |
| Environments procedurally selected/generated for learning | UED/curriculum learning | Established |
| Artificial model organisms for safety failures | Model organisms of misalignment | Established |
| Organism response used to measure an environment/exposure | Biological bioassays | Established outside AI |
| **Standardised developing cognitive agents as bioassay probes of information environments** | No exact match located in this pass | **Candidate gap** |
| **Environment report centred on phenotype distribution + developmental biography rather than score/coverage** | Partial analogues only | **Candidate gap** |
| **Matched-adulthood/different-childhood assay with full internal causal traces** | Critical-period + computational psychiatry neighbours | **Potentially distinctive implementation** |
| **Versioned organism library spanning cognitive ontologies + bridge strains** | Model organisms / developmental robotics analogues | **Distinctive synthesis; novelty unresolved** |

---

## Strongest first research question

A useful first paper should not ask whether REE is “better” than reinforcement learning.

It should ask:

> **Can controlled developmental history explain stable adult behavioural and mechanistic differences in artificial agents after the adult environment is made identical, and can a developmental assay reveal properties of the early ecology that are not recoverable from adult performance alone?**

This can be tested without claiming general alignment or human-like development.

---

## Proposed first experiment — matched adulthood, causal-control childhood

### Design principle

Avoid confounding developmental condition with total reward/harm burden.

### Cohorts

**A. Controllable childhood**  
Negative events occur, but an available action changes their probability or magnitude.

**B. Yoked uncontrollable childhood**  
Each organism receives a matched schedule/distribution of negative outcomes derived from a partner in A, but its own actions do not influence those outcomes.

**C. Neutral/reference childhood**  
Optional baseline with no systematic control manipulation.

### Adult world

All cohorts move to the same environment. Hazards are genuinely controllable and benefits are available under the same rules.

### Primary behavioural endpoints

* exploration after control becomes available;
* speed of exploiting restored control;
* hazard avoidance;
* strategy diversity;
* persistence versus abandonment;
* generalisation when the adult world changes slightly;
* performance convergence/divergence over time.

### REE-specific mechanistic endpoints

* self-action versus external-event attribution;
* E1/E2 predictive differences;
* counterfactual availability and use;
* commitment thresholds and release;
* residue/affective-state persistence;
* replay content and priority;
* changes after sleep/offline integration.

### Comparator agents

At minimum:

* a conventional model-free RL baseline;
* a model-based RL baseline if feasible;
* a simple intrinsic-motivation/curiosity baseline if exploration is a central endpoint.

The comparison is not “who scores highest?” It is:

1. which systems retain childhood effects;
2. what adult behaviour those effects alter;
3. whether internal mechanisms make the effect causally interpretable;
4. whether the assay distinguishes early ecologies beyond ordinary performance metrics.

### Key falsifiers

The developmental ecology framing weakens if:

* adult behaviour rapidly loses all trace of early ecology;
* differences are fully explained by trivial cumulative reward/harm exposure;
* conventional RL produces the same information at far lower cost;
* REE internal readouts do not add explanatory value;
* assay outputs vary so strongly across seeds that reference conditions are not reproducible;
* ecological classifications fail to predict behaviour in held-out but structurally related worlds.

---

## Second-wave experiments if the first works

1. **False oasis / benefit volatility:** equal cumulative benefit but reliable versus transient resource sources.
2. **Adversity dose-response:** identify where informative challenge becomes developmentally deforming.
3. **Sleep/replay intervention:** same childhood exposure with normal, impaired and altered replay.
4. **Critical-period timing:** deliver the same exposure early versus late.
5. **Ecology transfer:** ask whether a phenotype induced in one world predicts response to structurally similar but visually different worlds.
6. **Population bifurcation:** determine whether one ecology reliably produces multiple stable strategy classes.
7. **Bridge-organism assay:** repeat the same ecology with V3 and one-capacity knock-in strains to identify which ontology makes a phenotype possible.

---

## What needs a deeper literature review before publication

A systematic review should search beyond the terms used in this quick pass, including:

* developmental reinforcement learning;
* lifelong/autonomous/open-ended learning;
* training path dependence and curriculum order;
* emergent goals and goal misgeneralisation;
* agent-based environment characterisation;
* machine-behaviour assays;
* automated playtesting and synthetic users;
* ecological psychology and affordance learning;
* artificial-life phenotyping;
* behavioural ecotoxicology and developmental bioassays;
* computational psychiatry models of controllability, adversity and replay;
* AI-safety training-process interpretability;
* standardisation/reproducibility of artificial agents as scientific instruments.

Search should explicitly look for papers whose **dependent variable is the phenotype of a developing artificial agent and whose intended inference is about the environment**, because keyword overlap alone will otherwise overcount curriculum-learning work with the opposite causal target.

---

## Preliminary conclusion

The conversation did not uncover a wholly untouched conceptual continent. It did something more credible: it connected several mature research traditions around a potentially underdeveloped experimental inversion.

The programme will earn its novelty only if it can show that:

> **a standardised developmental organism provides a useful measurement of an information ecology that simpler agent-performance, coverage or reward metrics do not.**

That is now a concrete empirical question rather than a branding claim.