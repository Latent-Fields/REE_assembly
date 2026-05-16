# Infant Substrate Expansion Design
<!-- version: 2026-05-16.2 -->
<!-- author: claude-sonnet-4-6, session infant-substrate-expansion-2026-05-16T111412Z -->

## Status

**Draft — 2026-05-16.** Based on targeted lit-pulls commissioned 2026-05-16; three lit-pull agents
still writing (affordance/valence, intrinsic motivation, RL diversity). Evidence table includes all
completed summaries; action column will be refined once affordance/valence agent completes.

---

## 1. Purpose and Scope

The infant stage (INV-055, ARC-046) must produce three things before the childhood/play phase can
begin: (a) a seeded valence map, (b) a behavioural repertoire broad enough to support trajectory
diversity, and (c) z_goal initialised by at least one high-salience benefit contact. The current V3
substrate compresses developmental possibilities in ways that make all three harder to achieve. This
document identifies those compression points, synthesises the relevant empirical and computational
literature, and proposes substrate features, curriculum parameters, and gate criteria to address
them.

**Goal:** increase exploratory diversity, accidental benefit encounters, valence-map richness,
transition diversity, replay usefulness, and behavioural repertoire breadth WITHOUT increasing
premature strategic convergence, catastrophic residue, sparse-reward collapse, early E3 rigidity,
or monostrategy basin lock-in.

---

## 2. Current Infant-Stage Compression Analysis

The CausalGridWorldV2 with default infant-stage parameters exhibits the following structural
compressions. Each generates a specific downstream deficit.

### 2.1 Identity Compression: Single Resource Type (default)

**Symptom:** z_goal always carries the same identity signature regardless of which resource the
agent contacts. `MECH-189` requires that high-salience benefit under high contextual complexity
seeds z_goal — but when all benefits are identical, contextual complexity doesn't differentiate,
and the z_goal seeding is weak or degenerate.

**Downstream deficit:** z_goal remains uninitialised or weakly seeded until very long training,
because there is no z_goal identity recovery signal to concentrate gradient on.

**Status:** SD-049 `multi_resource_heterogeneity_enabled` with `resource_introduction_schedule`
addresses this, but is not yet default-enabled for infant stage.

### 2.2 Harm Signal Compression: Binary Hazard Contact

**Symptom:** Harm is all-or-nothing. Either the agent avoids hazards completely (and the harm
residue field is never populated) or it contacts them (catastrophic). There is no graded harm zone
that produces mild residue without termination risk.

**Downstream deficit:** The residue field (ARC-013) cannot develop geographic curvature during
infancy. Sleep consolidation has nothing useful to consolidate. z_harm develops no gradient signal
— only a step function at hazard contact.

**Status:** No current substrate feature addresses this. SD-011 dual nociceptive streams are
implemented but both streams are activated only on contact, not proximity.

### 2.3 Spatial Compression: Homogeneous Geography

**Symptom:** All gridworld cells are equivalent except for the transient placement of hazards and
resources (which drift under SD-047). There are no spatially distinct microhabitats — no region
that is intrinsically safer, richer, or more novel than another.

**Downstream deficit:** Shannon entropy of visited positions can be high (broad coverage) without
any ecologically meaningful structure. Replay is uniform (no state-value gradient to bias replay
scheduler). The agent never learns that "different places mean different things."

**Status:** SD-054 reef safe zones + bipartite layout partially address this, but reef patches are
safety zones without additional resource differentiation.

### 2.4 Action-Class Compression: No Functional Distinction Between Actions

**Symptom:** With 5 actions (4 cardinal + noop), all movement actions are functionally equivalent
(same dynamics, same consequences) and noop is always suboptimal (energy_decay continues). There
is no action that has a qualitatively different consequence from any other.

**Downstream deficit:** Action-class entropy collapses. Once the policy learns to avoid hazards
and collect resources, the 4 cardinal directions become symmetric and interchangeable — only
local geometry matters. This produces monostrategy without any action-specific learning.

**Status:** The V4 harness spec (v4_developmental_harness_spec.md) introduces carry/push/use
actions with distinct affordance bundles. That is V4. V3 needs a lighter-weight approximation.

### 2.5 Temporal Compression: No Non-Terminal Consequences

**Symptom:** Every adverse event is either no-consequence (missed resource) or near-terminal
(hazard contact). There are no events that have persistent consequences short of termination.

**Downstream deficit:** The infant agent never learns from graded feedback — it learns only binary
avoid/pursue. The transition database is impoverished. Replay is dominated by termination-adjacent
trajectories (high salience, low diversity) or unremarkable mid-episode sequences.

### 2.6 Reward Compression: Sparse Accidental Benefit

**Symptom:** The only benefit signal is explicit resource contact. There are no ambient low-level
benefit signals that can be encountered "accidentally" during broad exploration.

**Downstream deficit:** z_goal seeding requires a high-salience benefit contact (MECH-189). If
resource placement is uniform-random, early episodes may have no resource contacts, and z_goal
stays near-zero for hundreds of episodes. The childhood transition gate is blocked not because
the agent is developmentally unready but because the environment never delivered the necessary
experience.

---

## 3. Literature Evidence Table

Format: Source | Key finding | REE relevance | DEV-NEED IDs | Claim IDs | Conf | Action

---

### 3.1 Motor Babbling and Sensorimotor Exploration

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Leitao & Gahr (2024) PNAS | Premature babbling causally OPENS the sensory template acquisition window; motor exploration is upstream of perceptual encoding | Exploration epoch cannot be skipped or compressed — it opens the representational window for later hippocampal retrieval | DEV-NEED-001, DEV-NEED-002 | ARC-065, INV-073 | 0.76 | Refines ARC-065: exploration epoch must precede residue consolidation, not overlap with it |
| Doupe & Kuhl (1999) Annu Rev Neurosci | BG-driven motor variability is necessary for repertoire formation; pharmacological silencing = monostrategy; critical period is partly self-closing | Establishes developmental window during which exploration must be broad. Monostrategy is the experimentally confirmed outcome of abbreviated exploration | DEV-NEED-001, DEV-NEED-005 | ARC-065, MECH-309 | 0.78 | Supports ARC-065; adds critical-period temporal constraint to infant gate criteria |
| Warlaumont & Finnegan (2016) PLoS ONE | Computational model: intrinsic reward (auditory salience of own output) necessary for diversity; loss of reward signal → monostrategy | Without an intrinsic diversity reward, infant RL collapses to lowest-effort attractor — mirrors EXQ-561 V3 monostrategy findings | DEV-NEED-001, DEV-NEED-003 | ARC-065, MECH-313, MECH-314 | 0.70 | Supports MECH-313 (noise floor) + MECH-314 (structured curiosity); both must be active at start of infant stage |
| Fuchs (2026) Annals NYAS | Canonical babbling requires 3-way motor/respiratory/vocal coordination; piecemeal single-system exploration leaves representation incomplete | Infant exploration must cover multiple action combinations, not single-mode actions; diversity is multi-dimensional from the start | DEV-NEED-001, DEV-NEED-005 | ARC-065, INV-073 | 0.68 | Suggests action-combination diversity metric as gate criterion |
| Garcia-Guzman (2026) Nature family | Spontaneous infant movements optimise for dynamic excitation, NOT goal-directed reaching; distinct functional mode with higher kinematic variability | Infant exploration phase is not degraded goal-seeking — it is a separate mode optimising for body-dynamic discovery | DEV-NEED-001, DEV-NEED-002 | ARC-065, INV-073 | 0.82 | Strongly supports separate infant exploration mode with different objective from childhood; suggests disabling E3 goal-planning during infant phase |
| Dolinskaya et al. (2021) Neurosci Lett | Inter-limb coordination gradients accumulate continuously during spontaneous phase; structure appears before goal-directed onset | Latent-state diversity accumulates during exploration — structure does not appear suddenly at goal onset | DEV-NEED-001, DEV-NEED-007 | ARC-065, MECH-314 | 0.75 | Supports running diversity metrics during infant phase; confirms gradual accumulation predicts readiness |

### 3.2 Environmental Enrichment and Deprivation

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Wang et al. (2017) Behav Brain Res | Novelty enrichment reduces never-tried-option failures; social enrichment alone INCREASES perseveration; effects dissociable | Type of enrichment matters, not quantity. Novelty-specific enrichment populates the option library; other types may not | DEV-NEED-003, DEV-NEED-005 | ARC-065, INV-073 | 0.64 | Suggests environment must provide novelty-type enrichment (distinct zones, varying layout) not just added stimulation |
| Li (2007) Behav Pharmacol | Isolation-reared rats: initial strategy acquisition normal; strategy UPDATE impossible; clozapine partially rescues | Developmental exploration poverty produces permanent monostrategy in adulthood; cannot switch strategies even when contingencies change | DEV-NEED-001, DEV-NEED-005 | MECH-309, INV-073 | 0.68 | Confirms MECH-309 developmental mechanism; supports treating monostrategy as permanent deficit if infant substrate is impoverished |
| Ventura et al. (2024) CA3 flexibility | Environmental enrichment → greater CA3 spatial tuning and enhanced contextual remapping; flat environments → poor representational differentiation | Environment structure during early exploration determines downstream hippocampal representational flexibility | DEV-NEED-003, DEV-NEED-007 | ARC-065, ARC-007 | 0.65 | Supports geographically structured infant environment; flat CausalGridWorld produces flat z_world coverage |
| Adolph (2017/2019) Psych Learn Mem | Behavioral flexibility requires varied motor experience BEFORE RL narrows repertoire; posture-specific; environmental variation necessary | INV-073 instantiated: exploration epoch must cover all action modalities before goal pursuit. Impoverished substrate → narrow option library | DEV-NEED-001, DEV-NEED-004 | INV-073, INV-055, ARC-065 | 0.78 | Strongly supports disabling goal-directed training during infant phase; supports diverse action coverage metric |

### 3.3 Curiosity and Intrinsic Motivation

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Pathak et al. (2017) ICML | Forward-model PE in learned feature space drives exploration; fails with stochastic attractors ("noisy TV problem") | MECH-314c is well-founded, but stochastic elements in infant env will capture novelty bonus; audit env for random attractors | DEV-NEED-003, DEV-NEED-006 | MECH-314, ARC-065 | 0.75 | Action: audit CausalGridWorldV2 infant params for stochastic attractors; fix before turning up novelty_bonus_weight |
| Burda et al. (2018) ICLR | Large-scale confirmation of curiosity-driven learning; noisy TV = permanent novelty trap | novelty_bonus_weight at max is INSUFFICIENT if env has irreducible random elements; structured env required | DEV-NEED-003, DEV-NEED-006 | MECH-314, ARC-065 | 0.78 | Critical design constraint: structured environment required alongside novelty bonus; not a parameter fix |
| Oudeyer (2016) IEEE Trans Cog Dev Syst | Learning-progress curiosity (not novelty) produces emergent developmental stage ordering in robots | MECH-314c learning-progress sub-flavour is the key for staged development; pure novelty-max does not sequence stages | DEV-NEED-008, DEV-NEED-001 | MECH-314, ARC-046 | 0.76 | Supports making MECH-314c the primary infant-stage curiosity signal; pure MECH-314a novelty is secondary |
| Monosov (2024) Neuron review | Novelty-based (striatal) and uncertainty-based (frontopolar) curiosity circuits anatomically dissociable in primates | MECH-314a/b split is biologically justified; combining them into one mechanism would miss dissociation | DEV-NEED-003 | MECH-314, Q-044 | 0.82 | Supports maintaining MECH-314a/b sub-flavour distinction; early calibration of both required during infant stage |
| Kidd & Hayden (2015) Neuron | Curiosity follows Goldilocks principle: neither too simple nor too complex maximises exploration | Infant environment difficulty gradient must be tunable to current competence level; flat difficulty produces no differential exploration | DEV-NEED-003, DEV-NEED-006 | MECH-314, ARC-065 | 0.78 | Suggests difficulty-graduated infant environment; some always-mastered, some at competence edge, some aspirational |

### 3.3b Additional Sensorimotor Findings (babbling agent, 2026-05-16)

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Denisova & Zhao (2017) Sci Rep | Context-inflexibility (not raw variability level) predicts ASD delay; healthy infants show different movement distributions across contexts; at-risk infants do not | Pathological failure mode = context-rigidity, not entropy collapse. Rung 2 (context-sensitive switching) required from the very start of infant phase, not only later | DEV-NEED-001, DEV-NEED-005 | ARC-065, Q-046 | 0.79 | **Refines gate criterion**: action_entropy_by_zone must differ across zones, not just global entropy > ln(3) |
| Griffin et al. (2026) Brain Sci | Spiking model: Phase 1 (Hebbian self-org via babbling) builds action-perception cell assemblies WITHOUT reward; Phase 2 (dopamine) consolidates subset. Phase 1 MUST precede Phase 2 or there is no option diversity for reward to select from | Mechanistic justification for two-phase infant design. REE currently applies E3 scoring from step 1 — this model says a reward-free Phase 0 is mechanistically necessary, not just helpful | DEV-NEED-001, DEV-NEED-002 | ARC-065, INV-073 | 0.76 | **Suggests missing claim**: explicit Phase 0 = reward-free Hebbian diversity phase before any E3/reward weighting; candidate ARC-claim |
| Gliga (2018) Front Psychol | Infants exhibit 3 distinct variability forms: (1) deliberate hypothesis testing, (2) environmental variance probing, (3) sensorimotor contingency discovery — these are NOT one mechanism | Diversity is a family of 3 distinct probing strategies, mapping to MECH-313 (noise floor), MECH-314a/b (novelty/uncertainty), MECH-314c (learning progress). All three needed | DEV-NEED-001, DEV-NEED-003 | MECH-313, MECH-314 | 0.72 | Refines: do not collapse 3 diversity mechanisms into single `novelty_bonus_weight` parameter |
| Kaplan & Oudeyer (2007) Front Neurosci | Tonic dopamine encodes learning progress (rate of PE reduction); agent avoids both predictable AND unpredictable contexts, concentrating in zone of maximal expected learning progress | REE infant stage requires tonic (learning-rate) signal distinct from phasic (reward) signal. E1 prediction error rate derivative is the signal; currently absent | DEV-NEED-003, DEV-NEED-008 | MECH-314, ARC-065 | 0.73 | **Suggests implementation**: running E1 loss derivative as MECH-314c learning-progress signal broadcast to exploration bonus |

### 3.3c Additional Curiosity/RL Diversity Findings (safe-exploration agent, 2026-05-16)

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| MAP-Elites (Mouret & Clune, 2015) | Behavioral descriptor defines cells; local competition within cells prevents all-but-one dominant strategy. The behavioral descriptor is the KEY design choice for structural diversity | REE has no explicit behavioral descriptor definition. Without it, CEM candidate diversity cannot be measured volumetrically (DvD finding); candidates collapse to dominant attractor | DEV-NEED-005 | ARC-065, MECH-309 | 0.75 | **Suggests missing claim**: define behavioral descriptor for REE navigation domain: (zone_profile, reward_mode, episode_phase) — currently absent from ARC-065/MECH-31x |
| IMGEP (Forestier et al., JMLR 2022) | Learning-progress-driven goal selection generates automatic curriculum of increasing complexity. Cold-start: agent needs initial competence on some goals before progress signal is meaningful | REE's residue field + schema salience = natural home for IMGEP-like learning-progress proxy. Track per-region wanting saturation rate (not just wanting level) as curriculum signal | DEV-NEED-003, DEV-NEED-008 | MECH-314, ARC-065 | 0.77 | **Suggests implementation metric**: per-schema learning-progress rate as modulator of schema salience; actionable without architectural change |
| Narvekar et al. (2020) JMLR survey | Difficulty-based curricula do NOT prevent monostrategy if all tasks require same strategy. Diversity-based curricula (by behavioral type) do. Adaptive curricula outperform fixed schedules | behavioral_diversity_acceptance_criteria.md Rung ladder is diversity-based (correct design). Rung ordering by behavioral mode rather than difficulty is the literature-correct choice | DEV-NEED-008 | ARC-065, Q-046 | 0.72 | Validates Rung 0-4 structure; curriculum must be triggered by behavioral competence plateau, not episode count |

### 3.4 Affordance Learning and Early Valence (affordance/valence agent, 2026-05-16)

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Burnay et al. (2020) Dev Sci | Crawling experience predicts drop-off avoidance in walkers; posture-specific. Water cliff elicits more exploration than real cliff — intrinsic attractive valence despite danger signal | Valence of harm-adjacent features is not purely aversive: some features attract despite danger proximity. Infant substrate needs mixed-valence zones (safe but adjacent to harm), not just binary safe/unsafe | DEV-NEED-004, DEV-NEED-001 | INV-055, ARC-013 | 0.70 | Supports microhabitat zone B (moderate resources + elevated hazard) as distinct from pure safe zone; mixed valence is developmentally informative |
| Valadi et al. (2020) Iran J Child Neurology | Environment affordance richness (variety of stimulation) → significantly broader developmental outcomes across motor, problem-solving, and communication; effect independent of SES | Environment structure during early exploration determines breadth of competencies. V3 infant env richness has downstream consequences for ALL developmental dimensions, not just motor | DEV-NEED-003, DEV-NEED-005 | ARC-065, INV-073 | 0.65 | Supports multi-zone/multi-resource infant environment; richness of stimulation variety is the key dimension (not SES-dependent quantity) |
| Keren-Portnoy & Tomasello (2021) Infancy | Infants detect and act on action-outcome contingencies rapidly without social mediation; accidental-contact-to-repetition cycle bootstraps action patterns within minutes | Contingency learning is fast: if infant substrate delivers sufficient benefit contact frequency, z_goal seeding should occur within relatively few episodes. Transient benefit patches address this | DEV-NEED-006 | MECH-189, INV-055 | 0.73 | Strengthens case for transient benefit patches; confirms rapid contingency learning without caregiver input is possible and expected |
| Berridge (1998) Neurosci Biobehav Rev | Wanting/liking dissociation: dopamine mediates approach motivation (wanting) independently of pleasure (liking). Hedonic liking reactions present from birth (innate). Wanting bootstraps from accidental contact independent of calibrated liking | Benefit contacts should generate a wanting-type signal (approach motivation, z_goal seeding) before liking is calibrated. Infant stage can bootstrap z_goal from accidental contacts alone | DEV-NEED-006 | MECH-189, SD-014 | 0.72 | Strongly supports transient benefit patches for z_goal seeding; wanting is separable from and earlier than liking — early contacts suffice |

### 3.5 Safe Exploration and RL Diversity

| Source | Key finding | REE relevance | DEV-NEED | Claims | Conf | Action |
|--------|-------------|----------------|----------|--------|------|--------|
| Eysenbach et al. (2019) ICLR DIAYN | Optimal DIAYN: partition state space evenly across skills; each skill mode occupies structurally distinct region | Formalises the no-monostrategy condition: distinct behavioural modes must occupy non-overlapping state-space partitions | DEV-NEED-005, DEV-NEED-003 | ARC-065, Q-046, MECH-309 | 0.80 | Suggests partition-coverage metric for infant gate: do distinct trajectory classes occupy distinct z_world regions? |
| Parker-Holder et al. (2020) NeurIPS DvD | Apparent diversity (pairwise distance) != effective diversity (volume); population can be spread but degenerate | Current V3 entropy metrics may be measuring apparent diversity; need volumetric trajectory coverage | DEV-NEED-005, DEV-NEED-007 | Q-046, ARC-065 | 0.78 | Refines Rung 1 metric: volumetric coverage of trajectory space, not just pairwise distance or action entropy |
| Dennis et al. (2020) NeurIPS PAIRED | Fixed bipartite environment still produces monostrategy if one attractor is easier; need difficulty calibrated to agent competence | SD-054 bipartite layout is necessary but not sufficient; relative salience must track agent performance | DEV-NEED-005, DEV-NEED-008 | ARC-065, Q-046 | 0.76 | Suggests curriculum parameter tracking which behavioral modes are underperforming; adjust relative attractor salience during infant stage |

---

## 4. Six Diversity Types: Infant-Stage Taxonomy

For the infant stage, **not all diversity types are targets**. The following table specifies
which types are active targets, which are excluded, and why.

| Diversity type | Definition | Infant-stage target? | Rationale |
|----------------|------------|---------------------|-----------|
| **Exploration diversity** | Shannon entropy of visited positions (H_pos) | YES, primary | Substrate must be traversed broadly before residue geography can be formed |
| **Strategic diversity** | Trajectory class count / CEM candidate distinctness | NO (deferred to Rung 1/childhood) | Premature strategic diversity = E3 convergence before valence map exists; this is the failure mode we avoid |
| **Valence diversity** | Residue field coverage: distinct harm + benefit residue signatures over latent space | YES, primary | Infant stage must populate harm/benefit geography; without it, sleep consolidation has nothing to consolidate |
| **Trajectory diversity** | Edit-distance or cosine distance across stored trajectories (Rung 1 prerequisite) | YES, latent seed | Diverse trajectories must exist in hippocampal store before E3 can draw from them at childhood onset |
| **Action-class diversity** | Entropy of action usage across ALL classes (not just at probe states) | YES, secondary | Without action-class coverage, some action classes never appear in trajectories; later stages cannot discover their affordances |
| **Latent-state diversity** | Coverage breadth of z_world across episodes | YES, primary | This is what Ventura 2024 CA3 remapping and Adolph 2017 posture-specificity both target; foundation for downstream representational flexibility |

---

## 5. Proposed Substrate Features

### 5.1 Graduated Harm Zones (Non-Terminal Hazard Gradients)

**Proposal:** Introduce `harm_gradient_enabled` mode where cells within radius r_outer of a hazard
exert mild negative reward (0.05–0.15) proportional to distance, without terminal contact until
radius r_inner. Terminal contact only at r_inner (existing behaviour).

**Mechanism:** At each step, compute distance to nearest hazard. If d < r_outer: apply
`harm_gradient_reward = -hazard_harm * (1 - d/r_outer)^2 * harm_gradient_scale`. If d < r_inner:
existing terminal contact logic.

**Diversity benefits targeted:** Valence diversity (mild harm residue populates field geography);
transition diversity (graduated approach/retreat rather than binary avoid/contact); replay utility
(approach-then-retreat sequences are diverse and informative).

**V3-testable:** YES — environment parameter change only.

**Parameters:**
```python
harm_gradient_enabled: bool = False       # off by default
harm_gradient_outer_radius: float = 2.0  # cells
harm_gradient_inner_radius: float = 0.5  # existing contact boundary
harm_gradient_scale: float = 0.3         # fraction of hazard_harm applied at outer boundary
```

**Gate relevance:** Residue field coverage (`residue_coverage_pct`) now measurable without
requiring terminal hazard contacts.

---

### 5.2 Microhabitat Zones (Structured Spatial Ecology)

**Proposal:** Divide the gridworld into 3–4 functionally distinct zones with persistent but
softly-enforced identities:

- **Zone A (Forage zone):** Higher baseline resource density, lower hazard density.
  Lower novelty signal (zone is "familiar"). Maps to reef-excluded area in SD-054.
- **Zone B (Risk zone):** Moderate resources, elevated hazard density. Mild harm gradient active.
  Higher novelty signal (zone is "challenging").
- **Zone C (Novelty zone):** Low resources, no hazards, mild positive ambient signal for presence.
  Distinct from forage zone but rewarding in a different way.
- **Zone D (Transition zone):** Borders between zones. Resources and hazards at intermediate
  densities. Zone identity less clear — promotes exploration of boundaries.

**Mechanism:** Soft zone identities via `zone_map[y][x]` (computed once per episode from a
random zone-boundary Voronoi seed). Zone assignment determines per-cell baseline resource spawn
probability and hazard spawn probability. Zone-A cells: `resource_prob *= zone_A_resource_factor`,
`hazard_prob *= zone_A_hazard_factor` (default: resource=1.5x, hazard=0.3x).

**Diversity benefits targeted:** Latent-state diversity (spatially distinct z_world signatures
per zone); valence diversity (harm/benefit geography becomes structurally predictable, unlike
random placement); replay utility (zone-crossing transitions are high-information for residue
consolidation).

**V3-testable:** YES — extends SD-054 zone concept with per-zone resource/hazard modulation.

**Parameters:**
```python
microhabitat_enabled: bool = False
n_microhabitats: int = 3              # A, B, C (D = borders, automatic)
zone_A_resource_factor: float = 1.5
zone_A_hazard_factor: float = 0.3
zone_B_resource_factor: float = 0.8
zone_B_hazard_factor: float = 1.8
zone_C_resource_factor: float = 0.3
zone_C_hazard_factor: float = 0.0
zone_C_ambient_bonus: float = 0.05   # positive presence signal
zone_novelty_decay: float = 0.95     # ambient bonus decays if zone visited too often
```

---

### 5.3 Transient Benefit Patches (Accidental Benefit Mechanism)

**Proposal:** Add time-limited high-salience benefit patches that appear and disappear
stochastically. Appearance probability higher in zone A and zone C. Duration 10–30 steps.
Benefit value 2–5x standard resource (to ensure high salience for z_goal seeding).

**Mechanism:** At each step, with probability `transient_benefit_prob`, spawn a transient patch
at a random cell weighted toward zone A/C. Patch persists for `transient_benefit_duration` steps.
Reward on contact: `resource_benefit * transient_benefit_multiplier`. No terminal contact.

**Diversity benefits targeted:** z_goal seeding (DEV-NEED-006): accidental contact with
high-salience patch provides the MECH-189 seeding condition without requiring the agent to pursue
explicit goals. Accidental encounters are by definition diverse in location and timing.

**V3-testable:** YES — new environment feature.

**Parameters:**
```python
transient_benefit_enabled: bool = False
transient_benefit_prob: float = 0.02     # per-step appearance probability
transient_benefit_duration: int = 20     # steps patch remains
transient_benefit_multiplier: float = 3.0  # relative to standard resource_benefit
transient_benefit_zone_weight: list = [0.4, 0.2, 0.3, 0.1]  # A, B, C, border preference
```

**Gate relevance:** Enables measurement of "accidental benefit contact frequency" as proxy for
z_goal seeding opportunity.

---

### 5.4 Action Diversity Scaffolding (Lightweight V3 Approximation)

**Proposal:** Without adding V4 action types, create weak functional differentiation between
existing actions by introducing:
- **Directional wind:** A per-episode drift vector that makes movement in one direction slightly
  cheaper and movement against it slightly costlier (energy_decay differential ±0.005 per step).
  Rotates every N episodes. This means optimal traversal strategy changes direction-by-direction.
- **Zone-gated noop bonus:** A small positive reward for noop within zone C (novelty zone) — makes
  noop strategically useful in a specific spatial context.

**Mechanism:** `wind_direction` is sampled at episode start. Actions moving with wind: energy
penalty reduced by `wind_assist_factor`; actions against wind: energy penalty increased by
`wind_resist_factor`. The optimal traversal pattern changes across episodes, preventing a single
movement pattern from dominating.

**Diversity benefits targeted:** Action-class diversity (all 5 action classes now have
situationally distinct consequences); trajectory diversity (different wind vectors require
different episode-level traversal strategies, even to reach the same goal).

**V3-testable:** YES — environment parameter change.

**Parameters:**
```python
directional_wind_enabled: bool = False
wind_assist_factor: float = 0.005       # energy_decay reduction with-wind
wind_resist_factor: float = 0.005       # energy_decay increase against-wind
wind_rotation_interval: int = 50        # episodes between direction change
noop_zone_bonus_enabled: bool = False
noop_zone: str = "C"                    # zone where noop carries ambient bonus
noop_zone_bonus: float = 0.03
```

---

### 5.5 Dynamic Episode Map Seeds (Per-Episode Distinctness)

**Proposal:** Currently SD-047 provides multi-source hazard drift within an episode. Add a
per-episode structural seed that varies the starting configuration: zone boundaries, initial
resource/hazard placement, and agent start position. Already partially implemented in existing
`reset()` but lacks zone-identity persistence.

**Mechanism:** Episode seed = `hash(episode_id)` used to generate zone boundaries + hazard
starting positions. Ensures each episode's structure is meaningfully distinct while respecting
zone statistics. Increases trajectory diversity across episodes without disrupting within-episode
consistency.

**V3-testable:** YES — trivial parameter; likely already partially present.

**Parameters:**
```python
structural_diversity_seed: bool = True   # default on
structural_diversity_strength: float = 1.0  # 0=fixed layout, 1=fully variable
```

---

### 5.6 Stochastic-Attractor Audit (Pre-Condition for Curiosity Bonus Deployment)

**Proposal (design constraint, not a feature):** Before enabling `novelty_bonus_weight > 0` in
infant stage, audit the CausalGridWorldV2 for all stochastic attractors. Per Burda (2018) / Pathak
(2017), any irreducibly random element with accessible variance will capture the MECH-314c
learning-progress signal permanently.

**Audit checklist:**
- [ ] Hazard drift direction: is it purely stochastic or Markovian? (SD-047 hazard_drift)
- [ ] Resource respawn: is respawn purely random or predictable? (resource_respawn)
- [ ] SD-048 interoceptive noise: is this variance exploitable by curiosity signal?
- [ ] Any `random.random()` calls in step() that affect obs but not env dynamics?

**Action:** For each identified stochastic element, either (a) make it Markovian (predictable
with uncertainty) rather than purely random, or (b) exclude it from the novelty signal computation.

---

## 6. Infant Curriculum Schedule

Four phases, triggered by episode count + telemetry thresholds.

### Phase 0 — Motor Babbling (Episodes 0–100)

**Goal:** Generate a minimally structured transition database. E3 disabled or near-random.
No goal-directed training. Exploration mode only.

**Active features:** MECH-313 (noise floor), MECH-314a (novelty bonus), dynamic episode seeds.
**Disabled features:** MECH-314c (learning-progress), harm gradients (too early for residue
geography), transient benefit patches (too salient — would pull policy before babbling completes).

**Parameters:**
```python
novelty_bonus_weight: 0.5    # moderate, not max; MECH-313 noise floor active
commit_threshold: 1.0        # near-never-commit (sweep_amplitude=1.0)
residue_scale_factor: 0.0    # no residue accumulation yet
e3_planning_enabled: False   # or E3 random-action mode
offline_integration_frequency: 10  # every 10 steps; high sleep:wake ratio
harm_gradient_enabled: False
transient_benefit_enabled: False
```

**Exit condition:** H_pos > 0.70 * ln(grid_size^2) AND episode count >= 100

---

### Phase 1 — Benefit Discovery (Episodes 100–500)

**Goal:** First z_goal seeding events. Begin populating benefit side of residue field.

**Active features:** Add transient benefit patches, multi-resource heterogeneity (food only,
water introduced at episode 300). Mild harm gradient introduced. MECH-314c begins.

**Parameters:**
```python
novelty_bonus_weight: 0.7
transient_benefit_enabled: True
transient_benefit_multiplier: 3.0
harm_gradient_enabled: True
harm_gradient_scale: 0.15      # mild; enough to generate benefit/harm contrast, not dangerous
multi_resource_heterogeneity_enabled: True
resource_introduction_schedule: {"food": 0, "water": 200}  # ep offset within this phase
offline_integration_frequency: 20
residue_scale_factor: 0.05     # begin gentle residue accumulation
```

**Exit condition:** z_goal.norm() > infant_goal_threshold_low (e.g. 0.3) AND
accidental_benefit_contacts >= 5 during the last 100 episodes.

---

### Phase 2 — Harm/Benefit Geography (Episodes 500–2000)

**Goal:** Full residue geography. Multiple competing behavioral attractors (zone A vs zone C).
Action-class diversity develops.

**Active features:** Microhabitat zones, directional wind, full harm gradient, full SD-049
(food + water + novelty). Bipartite SD-054 if monostrategy detected (see gate).

**Parameters:**
```python
novelty_bonus_weight: 0.5      # reduce from Phase 1; structured curiosity takes over
microhabitat_enabled: True
directional_wind_enabled: True
harm_gradient_scale: 0.30
multi_resource_heterogeneity_enabled: True
resource_introduction_schedule: {"food": 0, "water": 0, "novelty": 100}  # ep offset in phase
offshore_integration_frequency: 50
residue_scale_factor: 0.10     # ARC-046 protected rate (~10% adult)
reef_bipartite_layout: True    # activate to test for monostrategy
```

**Monostrategy sentinel:** If action_entropy < ln(2) for 200 consecutive episodes, activate
`reef_bipartite_layout=True` AND temporarily increase zone_B hazard density (relative attractor
salience adjustment per PAIRED principle).

**Exit condition:** See Section 8 (Gate Criteria).

---

### Phase 3 — Pre-Childhood Readiness (Episodes 2000+)

**Goal:** All gate criteria passing. Sleep consolidation quality confirmed. Replay is diverse.

**Active features:** All Phase 2 features. Offline consolidation frequency reduced to adult rate.
E3 planning enabled at reduced weight. Slow E3 annealing begins.

**Parameters:**
```python
e3_planning_weight: 0.1   # gradual, starting from 0.0
offline_integration_frequency: 100  # approach adult default
residue_scale_factor: 0.15  # still protected but approaching adult
```

**Exit condition:** All 7 infant gate criteria passing (Section 8).

---

## 7. New Telemetry Metrics

The following metrics must be computed and logged during infant training. Existing framework
provides `obs_dict` and `info` at each step; these metrics are computed in the training loop or
a parallel monitor.

### 7.1 Exploration Diversity Metrics

```python
H_pos                  # Shannon entropy of position histogram (per episode + rolling window)
unique_cells_visited   # count of distinct cells visited in last N episodes
zone_coverage          # fraction of each zone's cells visited in last N episodes
```

### 7.2 Valence Diversity Metrics

```python
residue_coverage_pct   # fraction of 10x10 grid cells with |residue| > threshold
residue_harm_cells     # count of cells with harm residue > 0.05
residue_benefit_cells  # count of cells with benefit residue > 0.05
harm_benefit_ratio     # residue_harm_cells / residue_benefit_cells; target 0.3–3.0
```

### 7.3 Action-Class Diversity Metrics

```python
action_entropy_global       # H over full episode action histogram
action_entropy_by_zone      # separate H_pos for zone A, B, C (detects zone-specific repertoire)
action_class_coverage       # bitmask: which action classes used at least once per episode
```

### 7.4 Trajectory Diversity Metrics (Rung 1 prerequisites)

```python
traj_pairwise_cosine_mean   # mean cosine distance over N sampled trajectory pairs
traj_volume_estimate        # log-det of trajectory kernel matrix (DvD-style; approximated)
traj_zone_crossing_count    # trajectory transitions crossing zone boundaries per episode
```

### 7.5 z_goal and Latent Diversity Metrics

```python
z_goal_norm             # existing; target > infant_goal_threshold
z_goal_identity_count   # distinct resource-type identity signatures (from SD-049)
z_world_coverage_norms  # PCA variance in z_world over last N timesteps (latent coverage)
```

### 7.6 Sleep Consolidation Quality

```python
post_sleep_z_goal_retention     # z_goal.norm() ratio before/after sleep integration
residue_consolidation_delta     # change in residue field magnitude after sleep
replay_diversity_index          # diversity of trajectories selected for replay (by zone/type)
```

---

## 8. Enriched Infant-Stage Gate Criteria

Replaces the single existing criterion (`z_goal.norm() > infant_goal_threshold`).

All 7 criteria must pass before childhood transition is approved. Criteria 1–3 are blocking;
criteria 4–7 are advisory (flag if missing but allow transition with supervisor override).

| # | Criterion | Threshold | Blocking? | DEV-NEED addressed |
|---|-----------|-----------|-----------|-------------------|
| 1 | z_goal.norm() > threshold | 0.4 (existing) | YES | DEV-NEED-006 |
| 2 | H_pos > 0.65 * ln(grid_cells) | rolling 100-ep | YES | DEV-NEED-001 |
| 3 | residue_coverage_pct > 0.15 | at least 15% of cells | YES | DEV-NEED-004 |
| 4 | action_entropy_global > ln(3) AND entropy differs across zones (H_zone_A vs H_zone_B KL > 0.05) | >= 3 effective actions; context-sensitive | advisory | DEV-NEED-001, DEV-NEED-005 |
| 5 | harm_benefit_ratio in [0.2, 5.0] | harm and benefit both present | advisory | DEV-NEED-004 |
| 6 | post_sleep_z_goal_retention > 0.85 | z_goal survives sleep | advisory | DEV-NEED-007 |
| 7 | traj_pairwise_cosine_mean > 0.3 | trajectory library non-trivially diverse | advisory | DEV-NEED-002, DEV-NEED-005 |

**Notes:**
- Criterion 2 requires NEW telemetry (H_pos infrastructure).
- Criterion 3 requires residue field to be enabled during infant phase (`residue_scale_factor > 0`);
  currently ARC-046 protection sets this to ~0. Proposed: enable at 0.05 from Phase 1 onward.
- Criterion 6 is novel and requires post-sleep z_goal retention logging.
- Criteria 4 and 5 replace the implicit "behavioral entropy below ceiling" from developmental_curriculum.md
  with explicit actionable thresholds.

---

## 9. Developmental-Gate Update Recommendations for DEV-NEED Register

The following updates to `developmental_needs_register.md` are recommended. The register currently
lacks quantitative thresholds for most infant-stage DEV-NEEDs.

| DEV-NEED | Current status | Recommended update |
|----------|----------------|-------------------|
| DEV-NEED-001 (sensorimotor grounding) | No quantitative gate | Add H_pos > 0.65 * ln(grid_cells) as blocking gate; add zone_coverage > 0.60 as advisory |
| DEV-NEED-002 (transition database) | No quantitative gate | Add traj_pairwise_cosine_mean > 0.3; add zone_crossing_count > 5/ep as advisory |
| DEV-NEED-003 (curiosity calibration) | After V_s diversity | Add: must confirm MECH-313 + MECH-314 active at Phase 0 onset; add stochastic-attractor audit as pre-condition |
| DEV-NEED-004 (residue geography) | No quantitative gate | Add residue_coverage_pct > 0.15 as blocking; add harm_benefit_ratio in [0.2, 5.0] as advisory |
| DEV-NEED-005 (repertoire breadth) | After V_s diversity | Add action_entropy_global > ln(3) as advisory; add note: strategic diversity explicitly excluded until Rung 1 cleared |
| DEV-NEED-006 (z_goal seeding) | z_goal.norm() gate exists | Strengthen: also require accidental_benefit_contacts >= 5 in last 100 eps; transient benefit patches facilitate |
| DEV-NEED-007 (sleep consolidation) | No quantitative gate | Add post_sleep_z_goal_retention > 0.85; add replay_diversity_index measurement |
| DEV-NEED-008 (transition gate) | Exists but partial | Replace with 7-criterion table in Section 8 |

---

## 10. Candidate Experimental Manifests

### EXQ-ISEF-001: Harm Gradient Baseline
**Scientific question:** Does enabling `harm_gradient_enabled=True` during infant stage produce
measurable residue field coverage (criterion 3) faster than binary-contact baseline?

**Design:** Compare:
- Control: standard infant params, binary hazard contact
- Treatment: `harm_gradient_enabled=True, harm_gradient_scale=0.30`
- N=5 seeds each; 2000 episodes each

**Primary metric:** `residue_coverage_pct` at episode 500, 1000, 2000.
**Secondary metrics:** `harm_benefit_ratio`, `H_pos`.
**Success criterion:** Treatment coverage > 2x control at episode 1000.
**V3-testable:** YES

```json
{
  "queue_id": "EXQ-ISEF-001",
  "description": "Harm gradient vs binary-contact: residue geography formation speed",
  "script": "experiments/infant_harm_gradient_baseline.py",
  "claim_ids": ["DEV-NEED-004", "ARC-013"],
  "architecture_epoch": "ree_hybrid_guardrails_v1",
  "estimated_duration_min": 30,
  "machine_affinity": "any",
  "tags": ["infant_substrate", "harm_gradient", "residue_geography"]
}
```

### EXQ-ISEF-002: Transient Benefit Patch z_goal Seeding Rate
**Scientific question:** Does `transient_benefit_enabled=True` produce earlier z_goal.norm()
threshold crossing (criterion 1) and more accidental benefit contacts?

**Design:** Compare:
- Control: standard infant params, uniform resource placement
- Treatment: `transient_benefit_enabled=True, transient_benefit_multiplier=3.0`
- N=5 seeds each; 1000 episodes each

**Primary metric:** Episode at which `z_goal.norm() > 0.4` first achieved.
**Secondary metrics:** `accidental_benefit_contacts`, `z_goal_identity_count`.
**Success criterion:** Treatment median first-crossing < 0.7x control median.
**V3-testable:** YES

```json
{
  "queue_id": "EXQ-ISEF-002",
  "description": "Transient benefit patches: z_goal seeding rate comparison",
  "script": "experiments/infant_transient_benefit_seeding.py",
  "claim_ids": ["DEV-NEED-006", "MECH-189"],
  "architecture_epoch": "ree_hybrid_guardrails_v1",
  "estimated_duration_min": 25,
  "machine_affinity": "any",
  "tags": ["infant_substrate", "z_goal_seeding", "transient_benefit"]
}
```

### EXQ-ISEF-003: Microhabitat vs Homogeneous Geography (Latent Diversity)
**Scientific question:** Does the 3-zone microhabitat structure produce greater z_world coverage
breadth and higher traj_pairwise_cosine_mean than homogeneous geography at matched episode count?

**Design:** Compare:
- Control: standard infant params, SD-054 reef only (two-zone)
- Treatment: `microhabitat_enabled=True, n_microhabitats=3`
- N=5 seeds each; 2000 episodes each

**Primary metric:** PCA variance in z_world (top 5 components) at episode 500, 1000, 2000.
**Secondary metrics:** `traj_pairwise_cosine_mean`, `zone_coverage`.
**Success criterion:** Treatment PC-1 through PC-3 all > 1.2x control at episode 1000.
**V3-testable:** YES — requires microhabitat feature implementation first.

```json
{
  "queue_id": "EXQ-ISEF-003",
  "description": "Microhabitat zones vs homogeneous: latent state diversity comparison",
  "script": "experiments/infant_microhabitat_latent_diversity.py",
  "claim_ids": ["DEV-NEED-001", "DEV-NEED-007", "ARC-065"],
  "architecture_epoch": "ree_hybrid_guardrails_v1",
  "estimated_duration_min": 45,
  "machine_affinity": "any",
  "tags": ["infant_substrate", "microhabitat", "latent_diversity", "z_world_coverage"]
}
```

### EXQ-ISEF-004: Stochastic Attractor Audit — Curiosity Bonus Calibration
**Scientific question:** At what `novelty_bonus_weight` value does the curiosity signal become
captured by stochastic elements (noisy-TV analogues) vs driving productive exploration?

**Design:** Grid search `novelty_bonus_weight` in [0.1, 0.3, 0.5, 0.7, 1.0] with:
- `interoceptive_noise_enabled=True` (stochastic element)
- `microhabitat_enabled=True` (structured environment for comparison)
- N=3 seeds per weight; 1000 episodes each

**Primary metric:** `residue_coverage_pct` and `H_pos` as functions of novelty_bonus_weight.
**Success criterion:** Identify optimal weight where both metrics are maximised (Goldilocks point).
**V3-testable:** YES

```json
{
  "queue_id": "EXQ-ISEF-004",
  "description": "Novelty bonus weight calibration: stochastic attractor risk assessment",
  "script": "experiments/infant_novelty_bonus_calibration.py",
  "claim_ids": ["MECH-314", "DEV-NEED-003"],
  "architecture_epoch": "ree_hybrid_guardrails_v1",
  "estimated_duration_min": 60,
  "machine_affinity": "any",
  "tags": ["infant_substrate", "curiosity_calibration", "stochastic_attractor"]
}
```

### EXQ-ISEF-005: Full Infant Curriculum vs Flat Parameters
**Scientific question:** Does the 4-phase curriculum (Section 6) produce better gate-criterion
satisfaction at episode 2000 than a flat best-single-parameter setting?

**Design:** Compare:
- Control A: flat `novelty_bonus_weight=0.7`, all features on from episode 0
- Control B: flat `novelty_bonus_weight=0.5`, standard infant params
- Treatment: 4-phase curriculum as specified in Section 6
- N=5 seeds; 2000 episodes each

**Primary metric:** Fraction of 7 gate criteria passing at episode 2000.
**Success criterion:** Treatment passing > 5/7 criteria; at least Controls A and B passing < 5/7.
**V3-testable:** YES — requires curriculum scheduler implementation.

```json
{
  "queue_id": "EXQ-ISEF-005",
  "description": "4-phase infant curriculum vs flat parameter baselines: gate-criterion comparison",
  "script": "experiments/infant_curriculum_vs_flat.py",
  "claim_ids": ["DEV-NEED-008", "ARC-046"],
  "architecture_epoch": "ree_hybrid_guardrails_v1",
  "estimated_duration_min": 90,
  "machine_affinity": "any",
  "tags": ["infant_substrate", "curriculum", "developmental_gate"]
}
```

---

## 11. V3/V4/Environment Extension Classification

| Feature | V3-testable? | Requires env extension? | Requires V4? | Notes |
|---------|-------------|------------------------|--------------|-------|
| Harm gradient zones | YES | YES (env change) | No | Low-complexity env change |
| Microhabitat zones | YES | YES (env change) | No | Extends SD-054 zone concept |
| Transient benefit patches | YES | YES (env change) | No | New env feature |
| Directional wind | YES | YES (env change) | No | Lightweight action differentiation |
| Dynamic episode seeds | YES | NO (already partial) | No | Trivial change |
| 4-phase curriculum scheduler | YES | YES (training loop) | No | Requires curriculum schedule hook |
| 7-criterion gate checker | YES | NO (telemetry only) | No | Python monitoring code |
| H_pos, residue_coverage telemetry | YES | NO (training loop add) | No | Instrumentation |
| Traj volume metric (DvD-style) | YES | NO (training loop add) | No | Numerically approximate |
| Post-sleep z_goal retention | YES | NO (training loop add) | No | Needs sleep-phase logging |
| Caregiver valence scaffolding (INV-043) | No | No | YES (V4) | Multi-agent required |
| Social enrichment (DEV-NEED-014) | No | No | YES (V4) | Multi-agent required |
| Loveability internalization (DEV-NEED-017) | No | No | YES (V4) | Multi-agent required |
| Full affordance object bundles (MECH-278) | No | Partial (V4 spec) | YES (V4) | V4 harness required |

---

## 12. Design Principle Summary

**The central insight from this synthesis:** The V_s monostrategy problem is not solvable by
parameter tuning alone. Turning up `novelty_bonus_weight` to maximum (a) risks noisy-TV capture
if the environment contains irreducible stochastic elements (Burda 2018), (b) produces novelty
coverage without developmental staging if `MECH-314c` learning-progress is absent (Oudeyer 2016),
and (c) fails entirely if the environment is structurally homogeneous — exploration covers the
space without forming the distinct attractor signatures that prevent monostrategy collapse (Ventura
2024, Dennis 2020, Li 2007).

**The correct frame:** The infant environment must contain learnable structure at multiple difficulty
levels (Kidd & Hayden 2015 Goldilocks principle) — some regions always-mastered, some at
competence edge, some aspirational. Without this structure, no curiosity or diversity mechanism
can prevent collapse. The substrate proposals above create this structure via microhabitats, harm
gradients, and transient benefit patches.

**The temporal constraint:** Based on Leitao & Gahr (2024), Doupe & Kuhl (1999), and Garcia-Guzman
(2026), the motor exploration epoch (Phase 0/1) must be protected from goal-directed training.
Garcia-Guzman 2026 establishes that spontaneous exploration is not degraded goal-seeking — it is
a distinct functional mode. Premature E3 activation during this phase is the mechanism by which
the critical window closes too early. Griffin et al. (2026) provides the computational mechanism:
Phase 0 must build action-perception cell assemblies by Hebbian co-activity before reward weighting
begins, or there is no option diversity for reward to select from.

**The curriculum principle:** Fixed bipartite environments (SD-054) will still produce monostrategy
if relative attractor salience is not calibrated to agent competence (PAIRED principle, Dennis 2020).
The sentinel mechanism in Phase 2 (detect monostrategy → adjust zone salience) is a manual
approximation of this curriculum principle within V3's single-environment constraint.

**The context-rigidity failure mode:** Denisova & Zhao (2017) establishes that the pathological
outcome of insufficient exploration is not low entropy but context-rigidity: the agent produces
the same action distribution regardless of context (zone, state, task-demand). This is a stronger
criterion than global entropy. Gate criterion 4 must therefore be zone-specific: `H(action|zone_A)`
and `H(action|zone_B)` must differ, not just `H(action)` must exceed a threshold.

**The wrong diversity level:** DIAYN (Eysenbach 2019) and DvD (Parker-Holder 2020) independently
show that step-level novelty and pairwise trajectory distance are insufficient diversity metrics.
What is needed is trajectory-level discriminability (are state distributions under different modes
distinguishable?) and volumetric coverage (do candidates span behavioral space or cluster?). This
means MECH-314 as currently implemented at the step level is not the diversity signal needed for
monostrategy prevention — it is a necessary but insufficient component.

**The missing ingredient:** REE has no behavioral descriptor — a compact trajectory-level
characterisation of which behavioral mode was active during an episode (MAP-Elites, Mouret & Clune
2015). Without this, CEM candidate diversity cannot be measured volumetrically, and the system
cannot detect degenerate clustering that pairwise metrics miss. This is a structural gap that no
parameter change can fill.

**The wanting/liking entry point for z_goal:** Berridge & Robinson (1998) and Keren-Portnoy (2021)
together establish that goal anchor formation proceeds via the WANTING pathway independently of
LIKING calibration. An infant agent exposed to accidental benefit contacts will rapidly generate
approach motivation (wanting) even before the consummatory value is calibrated. Transient benefit
patches are the operational mechanism for triggering this pathway in the V3 substrate.

---

## 13. Suggested Missing Claims

These candidate claims emerged from the literature synthesis and are not currently registered in
claims.yaml. They are not proposed for registration in this session — flagged for governance review.

### Candidate ARC-claim: Phase 0 Reward-Free Exploration Epoch

**Source grounding:** Griffin et al. (2026) + Doupe & Kuhl (1999) + Garcia-Guzman (2026).

**Claim statement:** A gradient-based training substrate must include a reward-free Phase 0 during
which action-outcome associations are built by Hebbian co-activity before reward-weighted learning
begins. Activating E3 scoring from step 1 collapses the option library before it is populated.

**Why not registered yet:** Would require ARC-046 revision. Needs discussion with user on whether
to fold into ARC-046 (infant phase spec) or register as a standalone ARC.

### Candidate MECH-claim: Wanting-Before-Liking Sequencing

**Source grounding:** Berridge & Robinson (1998) + Keren-Portnoy & Tomasello (2021).

**Claim statement:** During the infant stage, VALENCE_WANTING (approach motivation, goal anchor
seeding) is activated by accidental benefit contacts before VALENCE_LIKING is calibrated. Goal
anchor formation does not require prior liking calibration; wanting is the entry point.

**Why not registered yet:** MECH-189 covers the benefit-contact seeding mechanism but does not
specify the wanting-before-liking temporal ordering. Would be a child claim of MECH-189.

### Candidate MECH-claim: Novelty-Approach as Accidental-Benefit Bridge

**Source grounding:** Burnay et al. (2020) water cliff + Gliga (2018) hypothesis-testing variability.

**Claim statement:** Novelty-driven approach to mixed-valence regions (attractive-but-risky) is the
primary mechanism by which accidental benefit contacts are generated in the infant stage. An infant
environment with only safe exploration zones and purely dangerous zones will not produce this bridge.

**Why not registered yet:** The mechanism spans INV-055, MECH-189, and ARC-013 without being
cleanly owned by any. Candidate for a new MECH bridging exploration and residue seeding.

### Candidate MECH-claim: Behavioral Descriptor Specification Requirement

**Source grounding:** MAP-Elites (Mouret & Clune, 2015) + DIAYN (Eysenbach 2019).

**Claim statement:** Structural prevention of monostrategy requires an explicit behavioral descriptor
that characterises which behavioral mode was active during an episode. Without a defined descriptor,
diversity metrics degenerate to pairwise distance (which does not detect degenerate clustering) and
CEM candidates cannot be scored for volumetric coverage.

**Why not registered yet:** ARC-065 MECH-31x cluster does not include this requirement explicitly.
Would be a MECH child of ARC-065.

---

## 14. Appendix: DEV-NEED Readiness Impact Summary

After implementing the proposals in this document:

| DEV-NEED | Before | After | Change |
|----------|--------|-------|--------|
| DEV-NEED-001 | H_pos metric missing; no quantitative gate | H_pos gate + zone_coverage gate added; Phase 0/1 protect babbling | Blocking gate added |
| DEV-NEED-002 | No transition quality metric | traj_pairwise_cosine_mean + zone_crossing_count | Advisory gate added |
| DEV-NEED-003 | No stochastic-attractor check | Audit pre-condition + Goldilocks calibration experiment | Implementation de-risked |
| DEV-NEED-004 | residue_coverage_pct not measured | Blocking gate at 0.15; harm_gradient enables geography without terminal risk | Blocking gate added |
| DEV-NEED-005 | No action diversity gate | action_entropy_global > ln(3) advisory; strategic diversity explicitly excluded | Advisory gate added; scope clarified |
| DEV-NEED-006 | z_goal.norm() gate only | + accidental_benefit_contacts gate; transient patches deliver seeding events | Gate strengthened |
| DEV-NEED-007 | No sleep quality measurement | post_sleep_z_goal_retention + replay_diversity_index | New telemetry |
| DEV-NEED-008 | Single criterion | 7-criterion table; 3 blocking + 4 advisory | Full gate operationalised |
