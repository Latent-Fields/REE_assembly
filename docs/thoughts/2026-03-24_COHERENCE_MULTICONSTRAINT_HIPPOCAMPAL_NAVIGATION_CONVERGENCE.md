Status: raw

Source: ChatGPT conversation, 2026-03-24 (user-submitted thought intake)
Triggered by: Euronews article -- Doeller / Max Planck group, 2026-03-22
  "Breakthrough in brain research: German researcher discovers brain navigational system"

---

## 1. The External Finding (Doeller / Max Planck)

The article concerns Christian Doeller's group at Max Planck Institute for Human Cognitive and Brain Sciences.
The key claim is NOT a new structure -- it is a new understanding of how the hippocampal + entorhinal system is used:

- The brain uses the same navigation system it uses for physical space to organise memory and knowledge.
- Grid cells fire in hexagonal patterns not only for physical space but for:
  - sound frequency
  - social hierarchies
  - conceptual relationships
  - task structure
- So the grid is a general metric for relationships, not just distance in space.
- Navigation integrates multisensory signals (vestibular, proprioceptive, motor efference copy, visual landmarks).
  If hippocampus is damaged, other systems can compensate using body-based cues -- the map is distributed,
  hippocampus indexes it.
- Hippocampus "flickers" between current map / stored map / predicted map -- this is trajectory simulation.

Core claim of the finding:
  The hippocampal system is a general "navigation engine" for abstract spaces, not just physical space.

---

## 2. Convergence with REE

| Function | Neuroscience model | REE model |
|----------|--------------------|-----------|
| Map of environment | Place and grid cells | Latent manifold (E1 world model) |
| Direction | Head direction cells | Trajectory vector |
| Paths | Hippocampal sequences | Trajectory rollout |
| Memory | Stored as locations in map | Stored as positions in latent space |
| Planning | Simulated paths | E3 trajectory evaluation |
| Generalisation | Conceptual spaces | Object-token manifold |
| Decision | Value-tagged paths | Valence-weighted trajectories |

REE hippocampus = cognitive map + trajectory simulator.
Modern neuroscience hippocampus = cognitive map + trajectory simulator.
These are conceptually very close.

What neuroscience model still distributes across separate systems:
  Map -> simulate -> choose (distributed across hippocampus, PFC, basal ganglia, valuation systems)

What REE adds:
  Map -> simulate -> coherence test -> commit -> act (explicit architecture with commitment boundary)

REE is a systems architecture model built around the hippocampal substrate.
The novelty is the fusion of hippocampal trajectory simulation + basal ganglia commitment + control plane
into one architecture for coherent action selection across time.

---

## 3. Historical Priority Note

The user noted: "I cannot recall when I started thinking of thoughts as journeys within the mind and
mapping with clearly hippocampal systems but have talked about this for a long time."

Earliest confirmed REE repo evidence:

  File: docs/thoughts/2026-02-08_residue_paths_cognitive_map.md (Status: processed)
  Key line: "The residual is the map and path taken that hippocampal structures records.
             This is how it can be like an actual map and a map of thoughts."

This is 44 days before the Euronews article (2026-03-22).

The REE architecture develops this further:
- docs/architecture/hippocampal_systems.md: viability map as navigable terrain indexed by E2 action-object coords
- docs/architecture/valenced_hippocampal_map.md (MECH-073): navigable terrain of attractors/repellers
- docs/architecture/residue_geometry.md: "residue is both a geometric map and a record of traversal"
- 2026-02-12_DEPRESSIVE-PATH-PRUNING-HIPPOCAMPAL-ROLLBACK.md: trajectory space pruning / rollout collapse
- 2026-02-15_hippocampal_backward_shift.md: hippocampus tracks moving boundary of commitment (ethical space)
- 2026-02-25_task_loop_extraction_and_latent_field_ethics.md: PathGraph as navigable object

The "thoughts as journeys" framing is embedded in REE architecture from at least 2026-02-08,
predating the Doeller paper's public reporting.

---

## 4. Coherence Evaluator Formalization

Question from the conversation: "What brain structure corresponds to the REE coherence evaluator?"

Answer: there is no single structure. Coherence is a process that emerges from agreement across:

| System | REE analogue | Coherence contribution |
|--------|-------------|----------------------|
| DLPFC | Frontal goal latent (MECH-112) | Goal representation / planning horizon |
| OFC / vmPFC | Harm-benefit evaluation | Outcome value / trade-off |
| Amygdala | Harm model | Threat / aversive salience |
| ACC | Error / conflict signal | Conflict monitoring, effort cost |
| Insula | Interoceptive signal | Bodily prediction error, cost signal |
| TPJ / mPFC | Agency + social model | Social model violation check |
| DMN (mPFC-PCC-hippocampus) | Identity / autobiographical memory | Identity continuity |
| Basal ganglia | Commit gate | Action release when coherence is met |
| Neuromodulators | Control plane | Precision, urgency, gain |

The user's proposed definition (accepted):
  "The path that minimises harm, achieves goal, and maintains ongoing function and memory"
  = multi-constraint viability function

Formal definition of coherence:
  A trajectory is coherent if it does not produce a veto-level error signal in any major evaluation system
  across: goal space, harm space, identity space, resource space.

Decision rule:
  NOT: choose trajectory with highest reward
  BUT: choose trajectory with lowest veto + acceptable goal progress

This is viability theory / constraint satisfaction across time, not reward maximisation.

It explains why short-term reward maximisation fails as an objective -- an action can have high
immediate reward while failing the harm, identity, or resource constraints, producing internal
contradiction that surfaces as "this feels wrong" even when reward is high.

The ACC (anterior cingulate cortex) and insula are strong candidates for the coherence error signal:
- ACC: conflict monitoring, effort estimation, error likelihood
- Insula: interoceptive cost, bodily prediction error

So: ACC + insula may produce the coherence veto signal.
The basal ganglia commit gate opens when no major system sustains a veto.

---

## 5. Psychiatric Conditions as Coherence Evaluation Imbalance

Speculative hypothesis -- not yet a formal claim. Flagged for future consideration.

| Condition | Coherence imbalance |
|-----------|---------------------|
| Mania | False coherence: goal weight >> harm weight, harm model suppressed |
| Depression | Harm weight >> goal weight, trajectory space collapsed (path pruning) |
| Anxiety | Uncertainty >> commit threshold, veto signal chronically active |
| Psychopathy | Harm model underweighted or absent from veto check |
| OCD | Error / conflict signal overweighted, veto threshold never cleared |
| ADHD | Commit threshold / precision instability, inconsistent veto gating |
| Addiction | Short-horizon reward overweighted vs long-horizon coherence constraints |

If the coherence evaluator is the real selection mechanism, psychiatric conditions can be framed as
coherence evaluation imbalance rather than reward function distortions.
This fits clinical phenomenology better than reward-based accounts for many of these conditions.

This mapping is noted here but NOT claimed -- it is a hypothesis requiring separate evaluation.

---

## 6. Claims Touched

### Existing claims supported / reinforced

- ARC-007 (hippocampal path memory and replay):
  Doeller/Max Planck confirms hippocampus indexes abstract relational trajectories, not just spatial.
  Strong external literature support for ARC-007.

- ARC-018 (hippocampal rollouts + post-commitment viability mapping):
  "Navigation through abstract spaces" = REE rollout over E2 action-object coordinates + E3 viability map.
  The flickering between current / stored / predicted maps is exactly ARC-018's counterfactual rollout.

- MECH-112 (goal latent z_goal as structured attractor):
  User's identification of frontal goal latent as key coherence component matches MECH-112 exactly.
  Goal achievement alone is not coherence, but it is a necessary component.

- MECH-113 (self-maintenance error signal / D_eff coherence):
  Insula + ACC as coherence error signal maps to MECH-113's interoceptive self-maintenance layer.
  The multi-constraint framing extends MECH-113 beyond D_eff to cross-space veto evaluation.

### New candidate claim (not yet registered)

Proposed: MECH-1xx (next available after MECH-113)
Subject: coherence.multiconstraint_viability
Title: "E3 trajectory selection implements multi-constraint viability evaluation rather than scalar reward maximisation"

Core content:
  - A trajectory is selected when it passes the lowest-veto + acceptable-progress check across all
    evaluation systems, not when it produces maximum reward.
  - This is distinct from MECH-113 (which measures internal latent coherence via D_eff).
  - It is the explicit formalization of REE's selection criterion as multi-constraint viability
    over goal space, harm space, identity space, and resource space.
  - The biological correlate is: commit gate (basal ganglia) opens when ACC conflict, insula cost,
    amygdala threat, goal-distance (MECH-112), and identity checks all fall below veto threshold simultaneously.

Status: flag for claims.yaml registration in next governance pass.
Depends on: MECH-112, MECH-113, ARC-018, SD-005

---

## 7. Processing Targets (when processed)

- docs/architecture/e3.md
  Add "veto rule" framing to trajectory selection section:
  "The selection rule is lowest-veto + acceptable goal progress, not maximum reward."

- docs/architecture/hippocampal_systems.md
  Add note: Doeller / Max Planck (2026) finding provides external literature support for
  hippocampus-as-abstract-navigation-engine framing in ARC-007 and ARC-018.

- docs/claims/claims.yaml
  Register new MECH candidate: coherence.multiconstraint_viability (lowest-veto decision rule).
  Depends on: MECH-112, MECH-113, ARC-018.
