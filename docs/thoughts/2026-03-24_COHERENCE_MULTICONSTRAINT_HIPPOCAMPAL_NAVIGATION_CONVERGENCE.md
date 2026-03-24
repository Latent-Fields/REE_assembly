Status: processed

Processed in:
- docs/architecture/e3.md (section 4a: multi-constraint viability selection criterion; MECH-125 reference)
- docs/architecture/hippocampal_systems.md (External Literature Convergence section: Doeller 2010, Constantinescu 2016, Garvert 2017, Behrens 2018, Whittington 2020)
- docs/claims/claims.yaml (MECH-125: coherence.multiconstraint_viability, candidate, v3)

---

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

## 3. Historical Context and Convergence Note

The user noted: "I cannot recall when I started thinking of thoughts as journeys within the mind and
mapping with clearly hippocampal systems but have talked about this for a long time."

### What the Euronews article actually was

The 2026-03-22 article is prize journalism, not a research announcement. Doeller received the
2026 Leibniz Prize (Germany's top research award). The underlying landmark paper is his 2010 Nature
paper demonstrating grid-cell-like fMRI signals in humans during virtual navigation. There is no
separate 2025-2026 paper behind the article -- it summarises ~15 years of work.

### The scientific literature timeline

The idea of hippocampus as general abstract-space navigation engine has a long history:

  Tolman (1948) -- "Cognitive maps in rats and men", Psychological Review
    First formal map-not-habit-chains argument. Title deliberately extends to humans.

  O'Keefe & Nadel (1978) -- The Hippocampus as a Cognitive Map (Oxford University Press)
    Place cells ground the cognitive map in hippocampus. Dominant framework for ~30 years.
    Still spatial-specific at this stage.

  Cohen & Eichenbaum (1993) -- Memory, Amnesia, and the Hippocampal System (MIT Press)
    Relational Memory Theory: hippocampus = arbitrary relational binding, not space per se.
    Spatial navigation is one special case. Contested but serious alternative for ~20 years.

  Hafting, Moser et al. (2005) -- Grid cells in entorhinal cortex, Nature
    Neural mechanism for the map. Nobel Prize 2014 (shared with O'Keefe).

  Doeller, Barry, Burgess (2010) -- Evidence for grid cells in humans, Nature
    Grid-cell-like fMRI signal in humans. His core Leibniz Prize contribution.

  ** Constantinescu, O'Reilly, Behrens (2016) -- Organizing conceptual knowledge with a
     gridlike code, Science **
    WATERSHED. Grid cells fire in hexagonal patterns for abstract "bird morphology space"
    (neck-length x leg-length). First direct evidence that the specifically spatial coding
    mechanism (grid cells) operates for non-spatial abstract concepts. This is the paper that
    makes the abstract-map claim hard to dismiss.

  Garvert, Dolan, Behrens (2017) -- A map of abstract relational knowledge in the
    hippocampal-entorhinal cortex, eLife
    Non-spatial, unconsciously-learned graph structure represented map-like in hippocampus.

  Behrens, Muller, Whittington et al. (2018) -- What is a cognitive map? Organizing knowledge
    for flexible behavior, Neuron
    High-profile synthesis. General relational geometry engine view enters mainstream.

  Whittington, Muller, Mark, Behrens et al. (2020) -- The Tolman-Eichenbaum Machine, Cell
    Computational unification. Spatial cognition = special case of general relational learning.
    Named to honour both Tolman and Eichenbaum. The abstract-map view becomes the leading
    theoretical framework. ~2020 is when this becomes mainstream, not fringe.

"Thoughts as journeys" as a cognitive metaphor: Cicero's Method of Loci (~50 BCE),
Lakoff & Johnson Metaphors We Live By (1980). Spatial metaphors structuring abstract thought
are ~2000 years old as a conscious technique, ~46 years old as cognitive science.

### Corrected framing: independent convergence, not priority

REE's earliest recorded mention (2026-02-08_residue_paths_cognitive_map.md: "map of thoughts")
postdates the neuroscience literature by 6+ years (Behrens 2018, Whittington 2020).
The Euronews article postdates it by 44 days, but that is prize journalism -- not a new result.

The more accurate and more interesting claim is:

  REE arrived at the same architectural picture (hippocampus = relational trajectory simulator,
  latent manifold as navigable terrain, commit gate over simulated paths) through design
  reasoning rather than literature review -- independently, from a different direction.

That is convergent evidence, not priority. The 2018-2020 neuroscience mainstream and REE's
architectural design converged on the same structure from opposite starting points.

REE internal evidence of the framing:
- docs/thoughts/2026-02-08_residue_paths_cognitive_map.md: "map of thoughts" (earliest)
- docs/architecture/hippocampal_systems.md: viability map indexed by E2 action-object coords
- docs/architecture/valenced_hippocampal_map.md (MECH-073): navigable terrain of attractors
- docs/architecture/residue_geometry.md: "residue is both a geometric map and a record of traversal"
- docs/thoughts/2026-02-12_DEPRESSIVE-PATH-PRUNING-HIPPOCAMPAL-ROLLBACK.md: trajectory space pruning
- docs/thoughts/2026-02-15_hippocampal_backward_shift.md: hippocampus tracks commitment boundary
- docs/thoughts/2026-02-25_task_loop_extraction_and_latent_field_ethics.md: PathGraph as navigable object

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
  Add literature convergence note for ARC-007 / ARC-018:
  - Constantinescu, O'Reilly, Behrens (2016) Science -- grid cells for abstract conceptual space
  - Garvert, Dolan, Behrens (2017) eLife -- abstract relational map in hippocampal-entorhinal cortex
  - Behrens et al. (2018) Neuron -- "What is a cognitive map?" general relational geometry engine
  - Whittington et al. (2020) Cell -- Tolman-Eichenbaum Machine, spatial = special case of relational
  Note: Euronews 2026-03-22 article is prize journalism for Doeller Leibniz Prize, not a new paper.
  Underlying work anchored on Doeller, Barry, Burgess (2010) Nature.

- docs/claims/claims.yaml
  Register new MECH candidate: coherence.multiconstraint_viability (lowest-veto decision rule).
  Depends on: MECH-112, MECH-113, ARC-018.
