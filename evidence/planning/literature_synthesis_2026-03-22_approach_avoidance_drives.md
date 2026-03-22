# Literature Synthesis: Approach/Avoidance Drive Architecture
# Claims: INV-032, ARC-030, MECH-111, MECH-112, MECH-113, Q-021

**Date:** 2026-03-22
**Source:** PubMed searches (5 topic areas)
**Linked intake:** thought_intake_2026-03-22_approach_avoidance_drives.md

---

## MECH-111 — drive.epistemic_value_novelty

### Key Papers

**Wang et al. 2024** — "Dopamine encoding of novelty facilitates efficient uncertainty-driven exploration"
- PMID 38626219, DOI [10.1371/journal.pcbi.1011516](https://doi.org/10.1371/journal.pcbi.1011516)
- Direct and indirect striatal pathways together estimate mean AND variance of reward distributions. Mesolimbic dopaminergic neurons provide **transient novelty signals** that facilitate uncertainty-driven exploration. The novelty signal is distinct from the reward prediction error signal -- it encodes *variance* not just mean.
- Architectural implication: MECH-111's novelty drive maps directly onto dopaminergic novelty encoding. In REE, this suggests the novelty signal is not simply repurposed E1 prediction error but a distinct signal class encoding *uncertainty about reward distribution*, not reward itself.

**Kakade & Dayan 2002** — "Dopamine: generalization and bonuses"
- PMID 12371511, DOI [10.1016/s0893-6080(02)00048-5](https://doi.org/10.1016/s0893-6080(02)00048-5)
- Dopamine multiplexes: TD prediction error signal AND exploration/shaping bonuses (novelty bonuses). Novelty responses guide exploration by acting as intrinsic reward for encountering novel states. "Transient membrane effects of the dopamine-like signal on striatal firing substantially shorten the reaction time in the planning task."
- Architectural implication: The novelty bonus is architecturally separate from the harm/goal error signal. It operates on the commit threshold directly (lowering it for novel states) rather than through the goal attractor channel.

**Ogasawara et al. 2022** — "A primate temporal cortex-zona incerta pathway for novelty seeking"
- PMID 34903880, DOI [10.1038/s41593-021-00950-1](https://doi.org/10.1038/s41593-021-00950-1)
- Novelty seeking in primates is regulated by the **zona incerta (ZI)**, NOT by dopamine neurons in SN (traditionally associated with reward seeking). ZI is activated by *predictions of novelty* before action. ZI inactivation reduces novelty seeking. The anterior ventral medial temporal cortex (object vision/memory) is the source of novelty predictions.
- Architectural implication: Novelty seeking has its **own distinct neural circuit**, separate from reward dopamine. In REE, this suggests MECH-111 needs its own latent channel (possibly routed through z_beta or a dedicated z_novel) rather than being implemented as a signed E1 error.

**Suri, Bargas & Arbib 2001** — "Modeling functions of striatal dopamine modulation in learning and planning"
- PMID 11311788, DOI [10.1016/s0306-4522(00)00554-6](https://doi.org/10.1016/s0306-4522(00)00554-6)
- "Lack of dopamine-like novelty responses decreases the number of exploratory acts, which impairs planning capabilities." The model without novelty responses loses planning capability. Novelty is not decorative -- it is architecturally necessary for planning.
- Architectural implication: Directly supports MECH-111's claim. An REE agent without novelty drive will lose planning capability over time, not just exploration -- confirming the behavioral flatness prediction (Q-021).

### Architectural Shape for MECH-111

The literature supports MECH-111 but refines the mechanism:
- Novelty drive is **not** E1 prediction error repurposed as positive valence
- It is a **distinct signal class** encoding uncertainty/variance rather than mean reward error
- It has its own neural circuit (ZI pathway in primates) rather than sharing circuitry with harm or reward
- It acts on **commit threshold** (lowering it for novel states) and on **action proposal weighting** (up-weighting unexplored trajectories)
- In REE: best implemented as a variance signal from E1 (uncertainty about predictions) that feeds E3 commit threshold modulation alongside the harm signal -- not as a standalone latent but as a modulator

---

## ARC-030 — architecture.approach_avoidance_symmetry

### Key Papers

**Cox et al. 2015** — "Striatal D1 and D2 signaling differentially predict learning from positive and negative outcomes"
- PMID 25562824, DOI [10.1016/j.neuroimage.2014.12.070](https://doi.org/10.1016/j.neuroimage.2014.12.070)
- Human PET: D1 binding (direct pathway) predicts approach learning; D2 binding (indirect pathway) predicts avoidance learning. Dopamine precursor depletion improved learning from negative outcomes. "Bidirectional modulatory role for striatal dopamine in reward and avoidance learning via segregated D1 and D2 cortico-striatal pathways."
- Architectural implication: The D1/D2 dissociation is confirmed at the individual differences level in humans. ARC-030 (Go/NoGo symmetry) is well-supported. Approach and avoidance learning are mediated by separable pathways with distinct receptor populations.

**Bariselli et al. 2018** — "A competitive model for striatal action selection"
- PMID 30300636, DOI [10.1016/j.brainres.2018.10.009](https://doi.org/10.1016/j.brainres.2018.10.009)
- Reviews Go/NoGo models, proposes **competitive model**: dMSNs (D1) and iMSNs (D2) are tuned to the **same actions** and compete to determine behavioral response. It is NOT that direct=approach actions and indirect=avoidance actions. Rather, both pathways evaluate the same action candidates and the population balance determines whether the action is expressed.
- **Critical architectural implication**: Approach and avoidance are not parallel pipelines selecting from different action inventories. They are **competing evaluations of the same trajectory proposals**. The hippocampal planner proposes trajectories; both the harm channel (NoGo/indirect) and the goal channel (Go/direct) evaluate those proposals; the commitment gating reflects the competition. This is already consistent with MECH-106 (commit threshold asymmetrically modulated by valence) and ARC-016 (precision-to-commitment wiring) -- the precision signal is the *balance* of Go and NoGo evaluation.

**Hikida et al. 2012** — "Pathway-specific modulation of nucleus accumbens in reward and aversive behavior"
- PMID 23248274, DOI [10.1073/pnas.1220358110](https://doi.org/10.1073/pnas.1220358110)
- D1 receptor activation (direct pathway) controls reward learning; D2 receptor inactivation (indirect pathway) controls aversive learning. Pathway-specific pharmacological dissociation. NMDA, adenosine A2a, and CB1 receptors all contribute to indirect-pathway aversive learning LTP.
- Architectural implication: The indirect/NoGo pathway has multiple neuromodulatory inputs beyond D2 (adenosine, endocannabinoids). In REE, the harm channel (SD-010 nociceptive stream) may need to integrate multiple signal types beyond just harm proximity.

### Architectural Shape for ARC-030

The competitive model (Bariselli 2018) is the key architectural constraint:
- Approach and avoidance evaluate the **same trajectory proposals** from hippocampus
- The commit threshold (MECH-106, ARC-016) is the competition balance point
- ARC-030 implementation: add a Go/goal evaluation channel alongside the existing NoGo/harm evaluation channel in E3
- The two channels read from the same trajectory proposals (value-flat per Q-020), produce opposing modulation signals, and the precision-weighted difference determines commitment
- This means MECH-112 (goal attractor) and SD-010 (nociceptive stream) are symmetric inputs to the **same E3 commitment gate**

---

## MECH-112 — drive.goal_state_attractor

### Key Papers

**Barch & Dowd 2010** — "Goal representations and motivational drive in schizophrenia"
- PMID 20566491, DOI [10.1093/schbul/sbq068](https://doi.org/10.1093/schbul/sbq068)
- Negative symptoms in schizophrenia = failure to use internal representations of emotional experiences, previous rewards, and motivational goals to drive behavior. "Relatively intact hedonics but impairment in wanting." Distinguishes **liking** (hedonic response on receipt) from **wanting** (motivational drive toward future states). Schizophrenia negative symptoms = impaired wanting, preserved liking.
- **Critical architectural implication**: MECH-112 is specifically about "wanting" -- the prospective goal representation that drives trajectory selection BEFORE reaching the goal, not the valence response WHEN the goal is achieved. REE's existing valence architecture (z_beta positive valence, MECH-106 threshold modulation) may encode "liking" but lacks "wanting". Goal state representation must be prospective and persistent, not just a hedonic response.

**Hollerman, Tremblay & Schultz 2000** — "Involvement of basal ganglia and orbitofrontal cortex in goal-directed behavior"
- PMID 11105648, DOI [10.1016/S0079-6123(00)26015-9](https://doi.org/10.1016/S0079-6123(00)26015-9)
- Striatal neurons provide "neural representation of the goal" -- they integrate behavioral acts with reward outcomes. Orbitofrontal cortex encodes motivational significance of different rewards. Different striatal subpopulations activate at different stages: at conditioned stimuli, preceding reinforcers, following reinforcers.
- Architectural implication: Goal representation is distributed across time in the trajectory. The hippocampal terrain navigation needs subgoal representations at multiple points in the trajectory, not just at the final state.

**Rusu & Pennartz 2019** — "Learning, memory and consolidation mechanisms for behavioral control in hierarchically organized cortico-basal ganglia systems"
- PMID 31617622, DOI [10.1002/hipo.23167](https://doi.org/10.1002/hipo.23167)
- Hippocampus codes and memorizes world state representations; limbic-affective loop (ventral striatum) controls action selection in dorsomedial PFC-striatal loop. "Frontal corticothalamic circuits form a high-level loop for memory processing that initiates and temporally organizes nested activities in lower-level loops, including the hippocampus and the ripple-associated replay it generates."
- Architectural implication: The goal representation is hierarchical -- high-level limbic-affective goals modulate selection in the dorsomedial loop, which in turn modulates sensorimotor. In REE terms: z_world goal attractors should be set by a higher-level "limbic" signal (possibly z_beta positive valence combined with goal state memory in the hippocampal map), which then modulates E3 trajectory evaluation, which then modulates E2 execution.

**Culbreth et al. 2023** — "Computational neuroimaging study of reinforcement learning and goal-directed exploration in schizophrenia"
- PMID 36752156, DOI [10.1017/S0033291722003993](https://doi.org/10.1017/S0033291722003993)
- Schizophrenia: reduced reward-seeking, negative symptoms correlated with loss-avoidance behavior. "A bias toward loss avoidance learning." Exploration capacity intact but reward-seeking reduced. Rostrolateral PFC encodes uncertainty-driven exploration; ventral striatum encodes expected value.
- **Critical architectural implication for Q-021**: Schizophrenia negative symptoms are the clinical analog of a pure-avoidance architecture. The behavioral signature -- reduced reward-seeking with preserved or elevated loss-avoidance -- is exactly what Q-021 predicts would emerge from training on harm signals only. This provides empirical grounding for Q-021 as a real phenomenon.

### Architectural Shape for MECH-112

The liking/wanting distinction (Barch & Dowd) is the key constraint:
- Goal state attractor = "wanting" system: prospective, persistent, drives trajectory selection toward future states
- Distinct from "liking" system (hedonic response at goal receipt -- already partially encoded in z_beta)
- Implementation: A persistent goal state latent in E3's domain (z_goal, or a sub-component of z_world) that encodes predicted future coherence. The hippocampal terrain becomes attractive in regions near z_goal, not just repulsive near z_harm.
- The goal state should be persistent across trajectory steps (like a sustained motivational set), not just a terminal state reward signal

---

## MECH-113 — drive.homeostatic_self_coherence

### Key Papers

**Seth & Friston 2016** — "Active interoceptive inference and the emotional brain"
- PMID 28080966, DOI [10.1098/rstb.2016.0007](https://doi.org/10.1098/rstb.2016.0007)
- Interoceptive inference = inversion of a generative model of internal and external milieu. Bodily states regulated by descending predictions. "Physiological homeostasis and allostasis, early cybernetic ideas of predictive control and hierarchical generative models in predictive processing" unified. Sense of embodied self emerges from interoceptive inference.
- Architectural implication: Self-maintenance in FEP terms = the agent inverting a generative model of its own bodily/computational states. For REE: the agent's z_self model IS its self-maintenance model. Coherent z_self = agent maintaining its Markov blanket. The Markov blanket framing and the z_self coherence signal framing converge: maintaining z_self fidelity IS maintaining the Markov blanket.

**Petzschner et al. 2021** — "Computational Models of Interoception and Body Regulation"
- PMID 33378658, DOI [10.1016/j.tins.2020.09.012](https://doi.org/10.1016/j.tins.2020.09.012)
- Three levels: homeostatic (reflex-based), allostatic (predictive/anticipatory), goal-directed (flexible context-dependent). All three correspond to distinct generative models in active inference. Allostasis = change in prior beliefs/setpoints, not just reactive control.
- Architectural implication: MECH-113's self-maintenance signal may operate at multiple levels -- a reactive homeostatic signal (z_self entropy monitoring) AND an allostatic signal (anticipatory setpoint adjustment). The allostatic level is particularly interesting: it means the agent can anticipate upcoming coherence threats and prepare, not just react.

**Stephan et al. 2016** — "Allostatic Self-efficacy: A Metacognitive Theory of Dyshomeostasis-Induced Fatigue and Depression"
- PMID 27895566, DOI [10.3389/fnhum.2016.00550](https://doi.org/10.3389/fnhum.2016.00550)
- Proposes a **third level** beyond homeostasis and allostasis: **allostatic self-efficacy** -- metacognitive monitoring of the brain's own capacity to regulate itself. Dyshomeostasis + low self-efficacy = learned helplessness and depression. "Chronic dyshomeostasis triggers a generalized belief of low self-efficacy and lack of control."
- **Critical architectural implication**: This provides the direct link between MECH-113 failure and Q-021 (behavioral flatness). An agent whose self-maintenance fails experiences dyshomeostasis; the metacognitive layer registers low allostatic self-efficacy; this generalizes to behavioral inhibition (learned helplessness). In REE terms: failing z_self coherence → low self-efficacy signal → suppressed commit threshold → behavioral flatness. This is Q-021's mechanistic explanation, derived from MECH-113.

**Barrett, Quigley & Hamilton 2016** — "An active inference theory of allostasis and interoception in depression"
- PMID 28080969, DOI [10.1098/rstb.2016.0011](https://doi.org/10.1098/rstb.2016.0011)
- Depression = disorder of allostasis -- a "locked in" brain insensitive to its sensory context. Locked-in brain = model generates predictions that override sensory input; fails to update allostatic setpoints. This is the opposite of what MECH-113 should provide: a functioning self-maintenance system should keep the agent responsive and able to update.
- Architectural implication: The "locked in" failure mode (depression/behavioral flatness) is what happens when the self-maintenance signal fails or is absent. Behavioral flatness in REE (Q-021) = locked-in harm-avoidance model that generates avoidance predictions overriding any approach signals.

**Tschantz et al. 2022** — "Simulating homeostatic, allostatic and goal-directed forms of interoceptive control using active inference"
- PMID 35051559, DOI [10.1016/j.biopsycho.2022.108266](https://doi.org/10.1016/j.biopsycho.2022.108266)
- Active inference simulations of all three interoceptive control levels. The generative model structure differs between levels. Provides concrete simulation methodology for MECH-113.
- Architectural implication: REE's MECH-113 experiment design can draw on this methodology -- simulate both framings (z_self coherence signal vs Markov blanket resistance) and compare performance on a task requiring self-maintenance under perturbation.

### Architectural Shape for MECH-113

The three-level framework (homeostatic/allostatic/metacognitive) from Stephan & Petzschner provides a richer structure than the two framings originally proposed:
1. **Level 1 -- homeostatic**: Reactive z_self entropy monitoring. Self-maintenance error = deviation of z_self entropy from baseline.
2. **Level 2 -- allostatic**: Predictive setpoint adjustment. E1/E2 update prior expectations about z_self drift, enabling anticipatory self-regulation.
3. **Level 3 -- allostatic self-efficacy (metacognitive)**: E3 monitors its own capacity to regulate the lower levels. This is the mechanism linking MECH-113 failure to Q-021 behavioral flatness.

The two original framings (z_self signal vs Markov blanket) correspond to levels 1 and 3 respectively. Both need testing, and they may be complementary rather than competing.

---

## Q-021 — drive.behavioral_flatness_under_pure_avoidance

### Clinical Analogues (from above papers)

**Schizophrenia negative symptoms** (Barch & Dowd 2010, Culbreth et al. 2023):
- Reduced reward-seeking with preserved/elevated loss-avoidance = clinical analog of pure-avoidance architecture
- "Wanting" impairment with intact "liking" = prospective goal drive absent, hedonic response preserved
- Neural substrate: impaired prefrontal-striatal goal representation with partially intact harm-avoidance circuitry

**Depression as dyshomeostasis** (Barrett 2016, Stephan 2016):
- Locked-in avoidant brain = behavioral flatness + inability to approach
- Mechanistic path: dyshomeostasis → low allostatic self-efficacy → generalized behavioral inhibition → learned helplessness
- This maps onto the Q-021 prediction: pure-avoidance training → no approach gradient → quiescent policy

### Experimental Design for Q-021

Two-agent ablation:
- **Agent A (control)**: All three approach drives enabled -- MECH-111 novelty signal, MECH-112 goal attractor, MECH-113 self-maintenance
- **Agent B (ablated)**: All three approach drives disabled -- harm-avoidance only (SD-010 nociceptive stream active, no approach channels)
- Train both on same environment (CausalGridWorldV3 with positive goal states and hazard states)
- Measure over training: policy entropy, action rate, goal-state visit frequency, harm-state visit frequency
- Prediction: Agent B converges to lower policy entropy, lower action rate, near-zero goal-state visits

Secondary question: Minimum approach signal set. Test single-drive variants:
- B+MECH-111 only (novelty only): Does exploration without goal-directed behavior prevent collapse?
- B+MECH-112 only (goal only): Does goal drive without novelty/self-maintenance prevent collapse?
- B+MECH-113 only (self-maintenance only): Does homeostatic coherence alone prevent collapse?

---

## Summary: Architectural Implications for the New Claims Cluster

The literature converges on a richer picture than the original framing:

1. **Go/NoGo is a competition, not two pipelines** (Bariselli 2018). Approach and avoidance evaluate the **same trajectories**. The commit threshold is the competition balance point. ARC-030 should be implemented as a dual-evaluation of hippocampal trajectory proposals, not as separate trajectory generation for approach vs avoidance.

2. **Novelty drive is a distinct circuit** (Ogasawara 2022). Not E1 error repurposed. Needs its own latent channel or modulator (possibly via z_beta arousal) encoding uncertainty/variance about reward, not mean reward itself.

3. **Wanting vs liking dissociation** (Barch & Dowd 2010). Goal representation = "wanting" (prospective, persistent motivational drive toward future states). REE may have "liking" (z_beta valence at goal receipt) but lacks "wanting". MECH-112 must be prospective and persistent.

4. **Three-level self-maintenance** (Stephan 2016, Petzschner 2021). Homeostatic (reactive z_self monitoring), allostatic (predictive setpoint), metacognitive (self-efficacy monitoring). The metacognitive level links MECH-113 failure directly to Q-021 behavioral flatness via the allostatic self-efficacy mechanism.

5. **Behavioral flatness has a clinical name**: schizophrenia negative symptoms (avolition) = impaired wanting with preserved liking. Depression = locked-in avoidant state. Both are empirically documented failure modes of pure-avoidance architectures. Q-021 is not speculative -- it has clinical instantiation.
