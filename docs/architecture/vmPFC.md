# vmPFC — Affective and Normative State Preparation

**Claim Type:** architectural_commitment
**Scope:** Conversion of stored affective, normative, and residue content into active navigable state components
**Depends On:** [state](state.md), [residue geometry](residue_geometry.md), [hippocampal systems](hippocampal_systems.md), [E3](e3.md), INV-035, INV-036, MECH-126
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

### 2. Social and identity constraints

Social norms, role obligations, and identity-consistency requirements that would gate certain trajectories as unavailable — not as low-value but as categorically off-limits. These exist as semantic and episodic knowledge throughout the cortex. vmPFC activates them as live constraint components of the navigable state during trajectory evaluation.

Failure: social constraint knowledge exists in declarable form but does not gate path selection. The agent can articulate what should be done and does the opposite — not from ignorance but because the constraint is not active in the state being evaluated.

Biological evidence: the knowledge/application dissociation (Saver and Damasio 1991, PMID 1791934); the utilitarian shift under vmPFC lesions (Koenigs 2007, PMID 17377536 — patients know the categorical prohibition but it does not gate their trajectory evaluation on personal dilemmas); progressive bvFTD erosion (Rascovsky 2011, PMID 21810890) which degrades this function while leaving episodic memory and world-model perception relatively spared.

### 3. Safety memories and extinction context

Learned safety associations — memories that the current context is safe, that a previously dangerous stimulus is no longer dangerous, that prior avoidance was in a different context from the present one. vmPFC activates these as a competing state attractor to threat memories held by the amygdala. Without vmPFC activation of the safety memory, the threat attractor dominates regardless of the current contextual evidence.

Failure: the safety memory exists but cannot be made active in the current state. Threat state is re-entered despite contextual cues that should select the safety state. The agent is not misperceiving the world — it is failing to have the safety context activate the right state representation.

Biological evidence: vmPFC hypoactivation during extinction recall in PTSD (PMC 7554263 MVPA study — safety attractor cannot be instantiated from the extinction context); vmPFC-hippocampus-amygdala triad failure (PMC 10728304).

### 4. Goal approach pull

The affective force that makes a positively-valued goal actively attractive rather than merely represented. A goal can be encoded (G component of state is present) but have attenuated approach pull — meaning it does not exert the trajectory-biasing force that would normally weight path search toward it.

Failure: goals are represented but approach is inhibited or effort costs are over-estimated, producing anhedonia and avoidance even when the goal representation is intact.

Biological evidence: the simulated synapse loss study (PMID 39569353) — reduced representational capacity is sufficient to produce approach failure; negative learning-rate asymmetry in anhedonia (PMC 5828520); effort-cost mis-estimation in depressed young people independent of reward valuation.

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
