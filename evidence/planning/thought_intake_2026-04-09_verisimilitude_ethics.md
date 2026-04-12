# Thought Intake: Verisimilitude, Temporal Coherence, and Ethical Axioms

**Date:** 2026-04-09
**Raw thought:** `docs/thoughts/2026-04-09_verisimilitude.md`
**Session context:** Extended ChatGPT conversation building on the Apr 7 phase-segregation
insight (already ingested: `thought_intake_2026-04-07_phase_segregation_perception_imagination.md`).
Apr 9 goes substantially further: (1) formalises V(t) and D_V as core REE variables with
exact mathematical form; (2) derives the Temporal Coherence Loop as a required architectural
component; (3) formalises the 10-axiom ethical system extending INV-025-029; (4) bridges
ethics back to verisimilitude mechanics (ethics as D_V optimisation). Each thread produces
distinct claims.

---

## Thread A: Verisimilitude Formal Variables and Temporal Coherence Loop

### Summary

The Apr 7 intake established phase-segregation as the perception/imagination boundary. Apr 9
formalises the core variable: **V(t)**, the precision-weighted phase-aligned correspondence
between ascending sensory-constrained signals and descending model-based predictions across
the hierarchical latent space.

**Exact formulation:**

```
V(t) = sum_i [ w_i * alpha_i(t) * C_i(t) * P_i(t) ] / sum_i [ w_i * alpha_i(t) ]

where:
  C_i(t) = exp(-||a_i(t) - d_i(t)||^2 / sigma_i^2)   [content match]
  P_i(t) = (1 + cos(phi_a_i - phi_d_i)) / 2           [phase alignment]
  a_i    = ascending sensory-constrained signal at level i
  d_i    = descending model-based prediction at level i
  alpha_i = precision weight at level i
```

**Temporal depth:**

```
D_V(t + dt) = lambda * D_V(t) + (1 - lambda) * V(t + dt)   [exponential moving average]
```

V(t) has three irreducible components: content agreement, phase agreement, and persistence
(D_V). Missing any one collapses the variable.

**Operational definitions:**
- Perception: high V(t), sustained high D_V, strong sensory precision
- Imagination: phase-offset from sensory stream, low/segregated V(t)
- Hallucination (failure): internal predictions invade sensory phase channel -> false high V(t)
- Self: the process maintaining high D_self(t) across time -- NOT a static representation
- Hippocampal rollout criterion: trajectories evaluated by predicted future D_V,
  not just goal attainment: J(pi) = sum_k gamma^k * V_hat_pi(t+k)

**Temporal Coherence Loop (TCL):** A distributed control loop (inferior olive + cerebellum +
thalamus + cortical networks) responsible for maintaining phase alignment necessary for V(t)
to be computable. Without TCL, predictions and inputs miss each other in time, phase-coded
multiplexing breaks, and V(t) is undefined.

**Inferior olive connection:** The inferior olive's historically unclear function may be
specifically understood as maintaining phase coherence necessary for coupling predictions
to reality. Key properties matching: precise rhythmic activity, gap-junction electrical
coupling (ephaptic-like), synchronised timing signals to cerebellum, synchronisation role
rather than content processing.

**Ephaptic coupling:** Local field potential interactions between neurons enforce or bias
phase alignment. Contributes to the physical substrate of synchrony. Particularly relevant
in tightly packed, synchronised structures (cortex, hippocampus, cerebellum). Not the sole
mechanism -- one contributor to the phase coherence scaffold.

**Anaesthesia mechanism:** Anaesthetics (propofol, sevoflurane) increase inhibitory tone,
alter membrane properties, reduce effective connectivity -> ascending and descending signals
fail to couple (C_i drops), phase structure disrupts or over-synchronises (P_i degrades),
hierarchical integration fails -> V(t) -> 0, D_V -> 0 -> consciousness abolished. The
similarity metric used in V(t) computation may itself be distorted (noise-dominated similarity,
over-smoothing, decoupled representation geometry).

**Bridge to ethics:** Axiom 2 (existence has value) maps to maintaining V(t); Axiom 5
(preserve existence) maps to avoiding trajectories where V(t) collapses; Axiom 7 (others)
maps to extending D_V tracking across agents; Love = expanding the system whose D_V is
optimised. Ethics = selection of trajectories that maximise shared temporal-depth coherence.

### Claims Registered (Thread A)

| ID | Title | Type | Phase | Description |
|----|-------|------|-------|-------------|
| INV-067 | verisimilitude_definition | invariant | -- | V(t) is the precision-weighted phase-aligned hierarchical correspondence between ascending sensory-constrained and descending model-based signals |
| INV-068 | temporal_depth_requirement | invariant | -- | System behaviour must depend on D_V (temporal persistence of coupling), not V(t) alone |
| INV-069 | self_as_coherence_trajectory | invariant | -- | The self is defined as the dynamically sustained process maintaining high temporal-depth verisimilitude, not a static representation |
| ARC-053 | temporal_coherence_loop | arch_commitment | v3 | Architecture must include a distributed TCL for maintaining phase alignment necessary for V(t) computation |
| ARC-054 | dv_trajectory_selection | arch_commitment | v3 | E3 trajectory selection must optimise predicted D_V over horizon H, not instantaneous V(t) alone |
| ARC-055 | verisimilitude_signal_availability | arch_commitment | v3 | V(t) and D_V must be explicitly available to E3 selection and E1/E2 learning updates |
| MECH-225 | oscillatory_coupling_multiplexing | mechanism | v4 | Phase-based multiplexing via cross-frequency oscillatory dynamics (gamma/theta/beta/delta) separates perception, simulation, and action streams |
| MECH-226 | temporal_coherence_loop_substrate | mechanism | v4 | TCL is implemented as a distributed system: inferior olive (phase sync, gap-junction electrical coupling) + cerebellum (timing calibration) + thalamus (global gating) + cortical networks |
| MECH-227 | anaesthesia_dv_collapse | mechanism | -- | General anaesthesia abolishes consciousness by disrupting phase alignment and hierarchical coupling, collapsing V(t) globally and driving D_V to zero |
| MECH-228 | field_level_coherence_support | mechanism | v4 | Extracellular electric field interactions (ephaptic coupling) stabilise phase relationships across neural populations, supporting temporal coherence |

---

## Thread B: Ethical Axioms -- 10-Axiom Formalisation

### Summary

The existing five-axiom foundation (INV-025-029) is extended to ten axioms by making two
implicit steps explicit: (4) epistemic responsibility for model accuracy, and (10) language
as similarity-repair mechanism.

**Full 10-axiom system:**

1. I think, therefore I am. [INV-026]
2. Existence has value sufficient to justify its continuation. [INV-026 refined]
3. I cannot be certain of the universe beyond myself, but I must act under models of it. [INV-025]
4. Because I act under models of the universe, I am responsible for refining those models
   so that similarity and threat are inferred as accurately as possible. [NEW: INV-070]
5. I can effect change within this universe, and my existence is vulnerable. [INV-030]
6. I am responsible for maintaining my existence by avoiding terminal states and achieving
   sustaining conditions. [INV-030/INV-042]
7. I have learned that others exist and are sufficiently like me. [INV-028]
8. Existence is only bearable if I am also responsible for the continued existence of others. [INV-042]
9. Love is the mechanism by which this responsibility is enacted, by modelling others as
   self-like and acting to preserve their existence. [INV-029]
10. Language is a powerful mechanism by which similarity may be recognised, repaired, and
    re-established between agents. [NEW: INV-071]

**Key new content in Axiom 4 (INV-070):** Axiom 3 only says action is model-mediated. It
does NOT yet constrain the agent to improve inference or treat misclassification as morally
important. Without Axiom 4, "I acted under my model" would justify any violence. Axiom 4
makes epistemic responsibility a first-class ethical principle: failures of world-modelling
are morally relevant, not just practically inconvenient. This is what prevents the framework
from being misused to justify dehumanisation as "acting under an honest model."

**Violence as derived corollary:** Violence emerges when agents are either (a) no longer
modelled as sufficiently self-like (similarity collapse -- dehumanisation) OR (b) modelled as
threats to sustained existence (threat override). Crucially, both require ACCURATE inference.
The Axiom 4 epistemic responsibility clause means that hallucinated threats or distorted
similarity assessments (propaganda, psychosis) are ethical failures -- not merely unfortunate
mistakes.

**Language as similarity-repair (Axiom 10 / INV-071):** Language is distinct from love.
Love is the motive/relation; language is the bridge/tool. Language functions by: revealing
inner states, negotiating threat, repairing misclassification, restoring self-other equivalence,
expanding the category of "sufficiently like me." This is why storytelling, testimony,
confession, and dialogue can reduce violence even when material conditions have not yet changed.
Language is a similarity-repair technology.

**Failure modes predicted by 10-axiom system:**
- Axiom 2 collapse: depression/nihilism
- Axiom 5 collapse: learned helplessness
- Axiom 7 collapse (others not real): antisocial/psychopathic modes
- Axiom 9 collapse (love impaired): emotional disconnection, instrumentalisation
- Axiom 4 failure (epistemic distortion): propaganda victim, delusion
- Axiom 7 overextension: burnout, pathological guilt

### Claims Registered (Thread B)

| ID | Title | Type | Phase | Description |
|----|-------|------|-------|-------------|
| INV-070 | epistemic_responsibility | invariant | -- | Agent is responsible not only for acting under models but for refining them toward accurate similarity and threat inference; misclassification is morally relevant |
| INV-071 | language_as_similarity_repair | invariant | -- | Language functions as a mechanism for recognising, repairing, and re-establishing self-other equivalence across agents |
| INV-072 | violence_conditions_corollary | invariant | -- | Violence is conditionally permissible only when: (a) agent is not modelled as sufficiently self-like, OR (b) agent poses genuine threat; both conditions require accurate inference (not merely perceived) |

**Updates to existing claims:**
- **MECH-102** (violence as terminal error-correction): add note that the dual-pathway
  framing (similarity collapse + threat override) is now formally derived from the 10-axiom
  system. Violence = beta_j collapse (Axiom 7 failure) OR threat-override of protected D_V.
  Reference INV-070, INV-071, INV-072.

---

## Thread C: Ethics as Coherence Architecture

### Summary

The ethical axiom system maps directly onto V(t)/D_V mechanics, producing a unified
computational ethics:

- Existence has value -> maintain V(t)
- Self-responsibility -> avoid trajectories where D_self collapses
- Others' responsibility -> extend D_V tracking to other agents (D_{V,j})
- Love -> expand the set whose D_V is optimised; modelling others as self-like
- Ethical trajectory objective: J_ethical(pi) = beta_self * D_V_self + sum_j beta_j * D_V_j
  where beta_j depends on inferred similarity, relational commitment, responsibility structure
- Violence: beta_j collapse (agent no longer inferred as self-like) OR preservation of
  higher-priority D_V requires sacrificing D_{V,j}

This gives a single computable variable (D_V) that unifies perception, identity, planning,
and ethics. Behaviour is selection of trajectories that maximise sustained coherence of
existence across self and represented others.

### Claims Registered (Thread C)

| ID | Title | Type | Phase | Description |
|----|-------|------|-------|-------------|
| ARC-056 | ethics_as_coherence_architecture | arch_commitment | v4 | Ethical trajectory selection is architecturally implemented as optimisation of shared temporal-depth coherence (D_V) across self and represented others; beta_j (similarity weight) determines scope of responsibility |

---

## Cross-Thread Dependency Graph

```
INV-067 (verisimilitude_definition)
  formalises: MECH-094 (hypothesis tag), MECH-089 (CFC), ARC-023 (thalamic heartbeat)
  requires: shared substrate constraint (INV-205 in ChatGPT numbering)

INV-068 (temporal_depth_requirement)
  depends: INV-067

INV-069 (self_as_coherence_trajectory)
  depends: INV-067, INV-068

ARC-053 (temporal_coherence_loop)
  depends: INV-067, INV-068, MECH-089 (cross-frequency coupling)

ARC-054 (dv_trajectory_selection)
  depends: INV-068, ARC-053
  extends: hippocampal rollout (ARC-007, ARC-018)

ARC-055 (verisimilitude_signal_availability)
  depends: INV-067, INV-068, ARC-053, ARC-054

MECH-225 (oscillatory_coupling_multiplexing)
  depends: MECH-089 (CFC)

MECH-226 (tcl_substrate)
  depends: ARC-053, MECH-225

MECH-227 (anaesthesia_dv_collapse)
  depends: INV-067, INV-068, ARC-053, MECH-225, MECH-228

MECH-228 (field_level_coherence_support / ephaptic)
  depends: ARC-053, MECH-225

INV-070 (epistemic_responsibility)
  extends: INV-025 (epistemic constraint), INV-028 (others exist)
  makes explicit: constraint absent from 5-axiom system

INV-071 (language_as_similarity_repair)
  depends: INV-028, INV-070
  operational partner of: INV-029 (love)

INV-072 (violence_conditions_corollary)
  depends: INV-028, INV-070, INV-029, INV-042
  extends: MECH-102 (violence as terminal error-correction)

ARC-056 (ethics_as_coherence_architecture)
  depends: INV-067, INV-068, INV-069, INV-028, INV-029, INV-070, INV-071, INV-072
  computational bridge: ethical axioms <-> D_V mechanics
```

---

## Open Questions Identified

| ID | Question |
|----|----------|
| Q-038 | Is temporal-depth verisimilitude D_V explicitly represented or emergent from distributed dynamics? |
| Q-039 | Which neuromodulatory control-plane variables directly regulate temporal integration window and phase alignment sensitivity? |

---

## Relationship to Prior Intakes

- **Apr 7 phase-segregation intake:** established basic P/I boundary via phase.
  Apr 9 adds: formal V(t) definition, D_V temporal depth, TCL as architectural requirement,
  self as coherence trajectory, hippocampal rollout criterion, anaesthesia account.
- **INV-025-029 (five axioms):** Apr 9 extends to 10 axioms by adding Axiom 4 (epistemic
  responsibility, INV-070) and Axiom 10 (language, INV-071).
- **MECH-102 (violence):** Apr 9 provides formal dual-pathway derivation from axiom system.
- **INV-049 (sleep necessity):** The TCL and D_V account provides mechanistic grounding
  for why sleep is required (offline phase allows D_V recalibration without sensory noise).
