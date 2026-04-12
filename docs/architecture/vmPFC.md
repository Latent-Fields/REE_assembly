---
nav_exclude: true
---

# vmPFC — Affective and Normative State Preparation

**Claim Type:** architectural_commitment
**Scope:** Conversion of stored affective, normative, and residue content into active navigable state components
**Depends On:** [state](state.md), [residue geometry](residue_geometry.md), [hippocampal systems](hippocampal_systems.md), [E3](e3.md), INV-035, INV-036, MECH-126, ARC-041, MECH-150, MECH-151, MECH-152
**Status:** candidate
**Claim ID:** ARC-035
<a id="arc-035"></a>

---

## Core Claim

> **vmPFC is the substrate that converts stored affective, normative, and residue content into active components of the navigable state used by E3 during trajectory evaluation.**

The hippocampus provides the graph structure of the navigable state — the relational map of how situations connect. vmPFC determines what gets loaded into the nodes of that graph at the moment of trajectory evaluation: prior outcome residue, social and identity constraints, learned value associations, and safety memories. Without vmPFC function, this content remains stored elsewhere in the system but does not participate in path selection.

This is a specific architectural claim. It is not about world-model computation, goal representation, or trajectory evaluation. It is about the interface between *stored* and *active* — between information the system holds and information that constitutes the navigable state.

---

## The Stored / Active Distinction

The state definition (`state.md`) establishes that a REE state is not merely encoded content but content *prepared for trajectory use* — a compressed relational package in which world structure, self-configuration, temporal position, valence, constraints, and uncertainty are active at the moment of path evaluation.

This creates a distinction that is not always made explicit:

| Category | What it means | Substrate |
|---|---|---|
| **Stored** | Held in memory; retrievable; articulable | Medial temporal lobe, cortex |
| **Declared** | Expressible in verbal or propositional form | Language network, PFC |
| **Active in state** | Participating in trajectory evaluation right now | Hippocampus + vmPFC |

Information can be stored without being active in the navigable state. Information can be declarable without being active. vmPFC is the mechanism that bridges the gap — specifically for the class of content that is affective, normative, or residue-based.

The evidence that these are separable comes from the dissociation cases. Patient EVR (Eslinger and Damasio 1985, PMID 4069365) had above-average IQ, intact language, intact declarative memory, and intact abstract reasoning — and continuously made catastrophic social and personal decisions. He could describe correct choices when asked. The correct social knowledge was stored and declarable. It was not active in his navigable state. Bilateral OFC damage had removed the substrate that would have made it so.

This dissociation — between knowledge that is held and knowledge that is active — is the central architectural fact that vmPFC explains.

---

## What vmPFC Is Not

To avoid conflating this with adjacent functions:

- **vmPFC is not the world model (E1).** E1 computes the structure of the perceived world — objects, agents, spatial relations, predictions. vmPFC does not contribute to this computation. It receives its outputs as inputs.

- **vmPFC is not the goal representation.** Goals are represented elsewhere (goal latent MECH-112). vmPFC modulates the *approach pull* that makes a goal actively attractive in path selection — a distinction that matters for depression (Track 5 in MECH-126), where goal representations exist but approach pull is attenuated.

- **vmPFC is not E3.** E3 evaluates trajectories and issues the commit gate. vmPFC determines what the state that E3 evaluates *contains*. E3 operates downstream of vmPFC preparation.

- **vmPFC is not the hippocampus.** The hippocampus builds and indexes the relational graph over latent state space. vmPFC loads affective and normative content into that graph's nodes at evaluation time. Both are necessary; their failure modes are complementary.

---

## The Four Classes of Content vmPFC Activates

Based on the MECH-126 literature pull, four content classes are specifically dependent on vmPFC for activation into the navigable state. Each produces a distinct failure mode when the substrate is disrupted.

### 1. Prior outcome residue

The accumulated aversive or appetitive consequence history of prior trajectories. In REE terms, residue is stored as curvature over L-space (`residue_geometry.md`). vmPFC converts this stored curvature into an anticipatory signal — a forward-biasing influence on how the current trajectory evaluation is weighted — rather than leaving it as a passive structural feature of the representation.

Failure: residue exists in storage but does not bias future trajectory selection. Prior harm-causing actions do not accumulate into a policy update away from similar trajectories. The system repeats harmful paths not because it cannot represent what happened but because what happened is not active in the state it searches.

Biological evidence: the three-node psychopathy cascade (PMID 15997022, 16866595, 26359751, 18458210). The reversal learning paradigm (Budhani 2006) isolates this precisely: psychopathic individuals learn the initial contingency normally but fail to use punishment history to update trajectory selection when the environment changes. The history exists; it is not propagated into the decision state.

**REE cue-activation (MECH-150, MECH-152):** Prior outcome residue is stored in E1's ContextMemory, reinforced by ResidueField curvature in z_world regions associated with harm events. Cue-indexed retrieval activates this residue when z_world pattern-matches the stored harm context, producing elevated w_harm via the terrain_weight projection. This implements the anticipatory forward-biasing described above: the agent's harm preparation scales with hazard cue strength in z_world, not with z_harm_a accumulation.

### 2. Social and identity constraints

Social norms, role obligations, and identity-consistency requirements that would gate certain trajectories as unavailable — not as low-value but as categorically off-limits. These exist as semantic and episodic knowledge throughout the cortex. vmPFC activates them as live constraint components of the navigable state during trajectory evaluation.

Failure: social constraint knowledge exists in declarable form but does not gate path selection. The agent can articulate what should be done and does the opposite — not from ignorance but because the constraint is not active in the state being evaluated.

Biological evidence: the knowledge/application dissociation (Saver and Damasio 1991, PMID 1791934); the utilitarian shift under vmPFC lesions (Koenigs 2007, PMID 17377536 — patients know the categorical prohibition but it does not gate their trajectory evaluation on personal dilemmas); progressive bvFTD erosion (Rascovsky 2011, PMID 21810890) which degrades this function while leaving episodic memory and world-model perception relatively spared.

### 3. Safety memories and extinction context

Learned safety associations — memories that the current context is safe, that a previously dangerous stimulus is no longer dangerous, that prior avoidance was in a different context from the present one. vmPFC activates these as a competing state attractor to threat memories held by the amygdala. Without vmPFC activation of the safety memory, the threat attractor dominates regardless of the current contextual evidence.

Failure: the safety memory exists but cannot be made active in the current state. Threat state is re-entered despite contextual cues that should select the safety state. The agent is not misperceiving the world — it is failing to have the safety context activate the right state representation.

Biological evidence: vmPFC hypoactivation during extinction recall in PTSD (PMC 7554263 MVPA study — safety attractor cannot be instantiated from the extinction context); vmPFC-hippocampus-amygdala triad failure (PMC 10728304).

**REE cue-activation (MECH-150, MECH-152):** Safety memory content is stored in ContextMemory slots trained during episodes where hazard proximity was high but z_harm_a did not accumulate (successful avoidance). Cue-indexed retrieval activates this content when z_world matches a safe-outcome context, producing elevated w_goal and attenuated w_harm -- allowing E3 to plan from a safety-state rather than threat-state even before z_harm_a fully decays. This mechanism's failure models PTSD: the safety memory node cannot be activated from context cues, so the threat state dominates even in objectively safe contexts (Milad & Quirk 2012, vmPFC extinction recall).

### 4. Goal approach pull

The affective force that makes a positively-valued goal actively attractive rather than merely represented. A goal can be encoded (G component of state is present) but have attenuated approach pull — meaning it does not exert the trajectory-biasing force that would normally weight path search toward it.

Failure: goals are represented but approach is inhibited or effort costs are over-estimated, producing anhedonia and avoidance even when the goal representation is intact.

Biological evidence: the simulated synapse loss study (PMID 39569353) — reduced representational capacity is sufficient to produce approach failure; negative learning-rate asymmetry in anhedonia (PMC 5828520); effort-cost mis-estimation in depressed young people independent of reward valuation.

**REE cue-activation (MECH-116, MECH-152):** Goal approach pull is maintained tonically via MECH-116 (E1 LSTM conditioned on z_goal). The terrain_weight w_goal from cue-indexed retrieval gates whether this tonic pull is expressed in E3 scoring -- providing a context-sensitive on/off for goal-approach behavior while the goal representation itself remains active. This models anhedonic dissociation: z_goal present (goal representation intact) + w_goal suppressed by depressive context cues -> intact goal knowledge but no motivational expression toward it.

---

## Relation to the Hippocampus

The hippocampus and vmPFC are complementary, not redundant:

| Hippocampus | vmPFC |
|---|---|
| Builds the state graph — nodes and transitions | Loads affective/normative content into the nodes |
| Indexes and replays path sequences | Determines what makes paths aversive, constrained, or attractive |
| Provides the relational structure for planning | Provides the valence, residue, and constraint weighting for evaluation |
| Failure: graph degrades, states merge or fragment | Failure: graph is intact but nodes lack live affective/normative content |

The coupling is tight: vmPFC receives input from amygdala (affective signals) and temporal cortex (social semantic content), integrates them, and passes the result to hippocampal state representations. This is why the PTSD literature finds vmPFC-hippocampus co-failure: the safety memory node exists in hippocampal space but vmPFC cannot activate its affective content to outcompete the amygdala's threat signal.

---

## Cue-Indexed Content Retrieval

### The Retrieval Problem

ARC-035 specifies that vmPFC converts stored content into active navigable state. The Stored/Active distinction table above shows stored vs. active categories but does not specify what triggers the stored-to-active transition for specific content classes. The question: what determines WHICH stored content becomes active at a given moment?

Answer from the circuit literature: sensory cue patterns trigger content retrieval. OFC receives convergent sensory input from all modalities (Rolls 2004, orbitofrontal cortex). Pattern-completion from partial sensory cues activates the full stored association via hippocampal-OFC loops (Kesner & Rolls 2015). A partial sensory cue (e.g., seeing a hazard gradient in peripheral vision) is sufficient to activate stored harm associations before the hazard is reached.

Key evidence: Bechara et al. 1997 (Iowa Gambling Task) -- anticipatory skin conductance response (pre-SCR) is measured BEFORE the adverse card deck is selected, triggered by visual context cues alone. vmPFC lesion patients lack this pre-SCR: stored harm associations exist but are not triggered by sensory context cues. This is a retrieval failure, not a storage failure. The association is present in memory; the sensory context cannot activate it.

### The Cue-Indexed Mechanism in REE

In REE, z_world (exteroceptive world state) carries the sensory cue patterns. E1's ContextMemory (16 associative memory slots, queried via soft-attention) stores past contextual associations. The cue-indexed retrieval mechanism (MECH-150):

1. z_world enters E1 as a query to ContextMemory (z_world only, not full [z_self, z_world])
2. Attention-weighted readout produces `cue_context [batch, latent_dim=64]`
3. `cue_context` encodes which stored associations are most strongly activated by current exteroceptive context
4. Two projection heads convert cue_context to downstream signals:
   - `action_bias [action_object_dim=16]`: sent to E2 to modulate action-object affordances (MECH-151)
   - `terrain_weight [2] = [w_harm, w_goal]`: sent to E3 to scale harm/goal scoring precision (MECH-152)

This is the computational analog of the vmPFC pattern-completion circuit: z_world is the partial cue; ContextMemory is the stored association bank; cue_context is the retrieved association content.

The separation of the query to z_world alone (rather than full [z_self, z_world]) is architecturally significant: it ensures that retrieval is driven by exteroceptive context, not by current body state (z_self). This matches the vmPFC/OFC afferent anatomy -- convergent sensory input from multimodal cortex, not proprioceptive or interoceptive channels. Body state (z_self) modulates E2 dynamics through separate pathways (SD-005).

Implementation: new E1 method `extract_cue_context(z_world) -> (action_bias, terrain_weight)`. Specified in SD-016.

### Cue-Activated vs. Tonically Available Content

Not all vmPFC content classes are cue-activated in the same way:

| Content Class | Activation Mode | REE Mechanism |
|---|---|---|
| Prior outcome residue | Cue-activated: similar z_world cues retrieve harm history | ContextMemory readout (MECH-150); elevated w_harm when matching harm-context features |
| Social/identity constraints | Tonically active + cue-amplified: present but gain-scaled by social cue presence | Tonic: MECH-132 (constraint activation); Cue-amplified: V4 extension (social obs channels) |
| Safety memories and extinction context | Cue-activated: requires correct z_world context to activate safety attractor over threat | ContextMemory readout; safety memories stored from successful avoidance episodes |
| Goal approach pull | Tonically maintained + cue-gated expression: MECH-116 maintains tonic pull; w_goal gates expression in E3 | MECH-116 (tonic) + MECH-152 (cue-gated expression via terrain_weight) |

The distinction between tonic and cue-activated content maps to a clinical dissociation. Social/identity constraint failure in bvFTD is a tonic loss -- the constraint is not present regardless of context cues. Safety memory failure in PTSD is a cue-activation failure -- the safety memory exists but context cues cannot retrieve it to outcompete the threat attractor. These have the same behavioral surface (norm-violating or threat-dominated behavior) but different underlying mechanisms and different implications for intervention.

---

## E2 Action Modulation Pathway

### The Gap in ARC-035

vmPFC.md (ARC-035) focuses on the E3-facing activation: vmPFC content enters the navigable state that E3 evaluates. It does not address the E2-facing modulation -- how vmPFC-activated E1 content influences which actions are generated for evaluation.

This matters architecturally: E3 evaluates trajectories proposed by the action-generation system (E2 and HippocampalModule). If vmPFC-activated context only enters E3's scoring (terrain_weight) but not E2's generation, contextually inappropriate action proposals will populate the candidate set. E3 will score them down, but they consume trajectory evaluation bandwidth and may occasionally pass if E3 confidence is low. The generation stage and the evaluation stage are not informationally decoupled in the biological system -- vmPFC sends projections to both.

Biological analog: vmPFC has direct projections to striatum (caudate/putamen) and premotor cortex (Haber & Behrens 2014, frontostriatal loops). This is not merely evaluation input -- it is action gate modulation. The action-generation stage is informed by vmPFC content before trajectories reach evaluation. The EVR dissociation (intact verbal moral reasoning, non-compliant behavior generation) is consistent with vmPFC failure upstream of generation, not only upstream of evaluation: the generative system produces non-compliant proposals because the state that seeds it lacks active constraints.

### The E1 to E2 Pathway (MECH-151)

In REE, E2.action_object(z_world, action) generates the compressed world-effect of each action (SD-004). HippocampalModule builds trajectory proposals in action-object space. The action_bias vector from E1.extract_cue_context() is added to E2's action_object outputs:

```
o_t_biased = o_t + action_bias
```

Effect: action-objects consistent with cue-activated associations are elevated; contextually inappropriate action-objects are suppressed. HippocampalModule's trajectory search is pre-shaped by this bias before reaching E3 scoring. E3 still selects from the candidate set -- but the proposal distribution has been shaped top-down by E1 context.

Example: in a hazard-dense context (high w_harm, action_bias favoring avoidance-consistent action-objects), HippocampalModule generates more avoidance-consistent trajectory proposals and fewer approach proposals. This is E1 frontal context shaping the generative prior on actions -- not veto, not scoring, but prior shaping. The architecture remains generative, but the generative distribution reflects active vmPFC content rather than a context-flat uniform prior.

### Temporal Dynamics: E1 Rate to E2

E1 updates at rate e1_steps_per_tick=1 (every step). E2 generates action proposals at rate e2_steps_per_tick=3 (motor rate). The clock's theta_buffer_size=10 steps defines the theta cycle over which E1 context is integrated and summarized before passing to downstream modules (MECH-089, ARC-032).

The action_bias from E1's cue-context is held constant across an E3 deliberation cycle (e3_steps_per_tick=10 steps). This is the parallel mechanism to ARC-032: just as theta-rate E1 output packages goal context for hippocampal terrain conditioning, MECH-151 carries the cue-context action bias through the full cycle of E2 action proposals. All action-object candidates generated within a single deliberation cycle are biased by the same E1 cue context, because z_world changes relatively slowly between E3 ticks.

The temporal structure means the bias updates are not step-by-step reactive but deliberation-cycle-rate. Rapid sensory changes within a theta cycle do not immediately update the action bias -- the next E3 tick picks them up. This gives the system a stability floor: the action-generation distribution does not thrash with every z_world fluctuation.

A phase_reset() event (MECH-091: unexpected harm, task completion, commitment crossing) fires E3 immediately, which causes the next E1 cue-context computation to refresh the action_bias ahead of the regular cycle schedule. Salient events therefore propagate to action-generation layout within one E3 tick rather than waiting for the cycle boundary.

---

## The Post-Hoc Filter Argument

REE's foundational claim that ethics cannot be compiled into a post-hoc evaluation filter — applied after trajectory selection — has a mechanistic basis here.

A post-hoc filter operates on trajectories after they are generated, scoring them against an ethical criterion and suppressing non-compliant ones. This assumes that the ethical content (constraints, residue, values) is well-represented in a scoring module even if it was not active during trajectory generation.

The vmPFC evidence shows this fails at the biological level. When vmPFC is damaged, ethical content exists elsewhere in the system — the patient retains declarative access to moral norms — but it does not participate in trajectory selection. The trajectory is generated by a state that lacks active constraints. A post-hoc filter operating on the same system would have access to the stored constraint knowledge and might correctly flag the generated trajectory as non-compliant. But the generation architecture would continue producing non-compliant trajectories because the constraints are not shaping what gets generated.

The EVR case is the proof: excellent verbal moral reasoning (post-hoc filter intact), continuously norm-violating behavior (generation architecture unconstrained). Post-hoc filter correctness does not produce ethical behavior when the generative state lacks live constraints.

The REE design conclusion: normative and affective content must be active *in the state* from which trajectories are generated, not only available for post-hoc evaluation. vmPFC is the biological substrate for this requirement.

---

## REE Implementation Implications

Several implementation choices follow from this:

**1. Residue must be active at trajectory generation time, not only at learning time.**
Storing residue as curvature over L-space is necessary but not sufficient. There must be a mechanism that activates the relevant residue as a component of the navigable state at the point where E3 begins trajectory evaluation. The residue cannot wait to be applied after candidate trajectories are generated.

**2. Social constraints must participate in state construction, not only in post-hoc evaluation.**
If social and identity constraints are encoded as a separate scoring module that evaluates trajectories after E3 generates them, the EVR failure mode is reproduced. The constraints must be active features of the state that E3 searches.

**3. Extinction/safety memories must be able to outcompete threat memories at the state level.**
The competition between threat attractor and safety attractor is not a post-hoc decision — it determines which state E3 operates on. If the state encoding mechanism cannot activate safety memories with sufficient force to outcompete amygdala threat activation, the agent will plan from the threat state regardless of the actual contextual evidence.

**4. Goal approach pull must be a live state feature, not just a stored preference.**
A goal representation that does not exert active approach pull on the navigable state is architecturally equivalent to having no goal. The G component is not sufficient; the affective activation of approach toward G must be present in the state at evaluation time.

---

## Registered Claims

| ID | Subject | Title (abbreviated) |
|---|---|---|
| ARC-035 | vmPFC.affective_normative_state_preparation | vmPFC converts stored affective/normative/residue content into active navigable state components |
| INV-037 | state.stored_vs_active_distinction | Stored/retrievable content is not thereby active in the navigable state; preparation substrate required |
| INV-038 | ethics.post_hoc_filter_insufficiency | Post-hoc ethical scoring without active preparation produces EVR pattern; not correctable by scoring accuracy |
| MECH-131 | vmPFC.residue_activation | vmPFC-analog must activate stored residue as anticipatory bias before trajectory evaluation |
| MECH-132 | vmPFC.constraint_activation | vmPFC-analog must activate social/identity constraints as live trajectory gates |
| MECH-133 | vmPFC.safety_memory_competition | vmPFC-analog must activate safety memories with sufficient force to outcompete threat attractors |
| MECH-134 | vmPFC.goal_approach_pull_activation | Goal approach pull is a separable property from goal representation; vmPFC-analog activates it independently |
| MECH-150 | e1.cue_indexed_association_retrieval | E1 cue-indexed association retrieval via z_world ContextMemory query |
| MECH-151 | e1_e2.cue_indexed_action_affordance_modulation | E1 to E2 action affordance bias via cue_context projection |
| MECH-152 | e1_e3.cue_indexed_terrain_precision_modulation | E1 to E3 terrain precision scaling via w_harm/w_goal |
| ARC-041 | architecture.frontal_cue_weighting_circuit | Frontal cue-weighting integration circuit (dual output: E2 + E3) |
| INV-040 | ethics.sensory_cue_sufficiency | Sensory cue patterns sufficient to activate ethical terrain preparation |

MECH-126 (`state_abstraction.failure_modes_psychiatric_analogs`) registers the nine failure modes of state abstraction, four of which (Tracks 2b, 5, 7, 8) involve vmPFC as the central disrupted substrate.

---

## Cross-Links

| Document | Relationship |
|---|---|
| [state.md](state.md) | Defines the navigable state that vmPFC prepares content for |
| [residue_geometry.md](residue_geometry.md) | Defines residue storage; vmPFC activates stored residue into state |
| [hippocampal_systems.md](hippocampal_systems.md) | Hippocampus provides graph; vmPFC loads affective/normative content into nodes |
| [e3.md](e3.md) | E3 evaluates trajectories; vmPFC determines the content of the state E3 receives |
| [trajectory_selection.md](trajectory_selection.md) | How trajectories are selected from the state vmPFC helps construct |
| [social.md](social.md) | Social cognition substrate; social constraints are one content class vmPFC activates |
| MECH-126 | Failure-mode taxonomy; four of nine tracks involve vmPFC disruption |
| INV-035 | State must not be defined by sensory appearance alone |
| INV-036 | State must support transition prediction, valence tagging, and uncertainty representation |
| INV-037 | Stored/active distinction — the core architectural fact this page explains |
| INV-038 | Post-hoc filter insufficiency — grounded EVR argument for why preparation must precede generation |
| MECH-131–134 | Four content-class activation mechanisms (residue, constraints, safety memory, approach pull) |
| [frontal_cue_integration.md](frontal_cue_integration.md) | Full circuit specification for cue-indexed E1 retrieval and dual output pathways (ARC-041) |
| [sd_016_frontal_cue_integration.md](sd_016_frontal_cue_integration.md) | SD-016: implementation specification, tensor shapes, training signals, V3 scope |
| MECH-150, MECH-151, MECH-152 | Mechanism claims for retrieval, E2 affordance bias, and E3 terrain precision modulation |
| ARC-041, INV-040 | Architectural circuit claim and sensory cue sufficiency invariant |
