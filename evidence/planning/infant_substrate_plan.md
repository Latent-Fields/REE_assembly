---
closure_plan:
  id: infant_substrate
  title: "Infant Substrate Expansion"
  registered: 2026-05-16
  scope_claims: [INV-055, INV-073, ARC-046, ARC-065, DEV-NEED-001, DEV-NEED-002, DEV-NEED-003, DEV-NEED-004, DEV-NEED-005, DEV-NEED-006, DEV-NEED-007, DEV-NEED-008, MECH-189, MECH-313, MECH-314]
  nodes:
    - id: "infant_substrate:GAP-1"
      title: "Harm gradient env feature (harm_gradient_enabled, graduated harm proximity signal without terminal contact)"
      phase: 1
      status: done
      severity: high
      owner_exq: "V3-EXQ-576"
      unblocks_claims: [DEV-NEED-004, ARC-013]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-2"
      title: "Microhabitat zones env feature (microhabitat_enabled, zone_A/B/C resource+hazard density modulation via Voronoi seed)"
      phase: 1
      status: done
      severity: high
      owner_exq: "V3-EXQ-577"
      unblocks_claims: [DEV-NEED-001, DEV-NEED-003, DEV-NEED-007, ARC-065]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-3"
      title: "Transient benefit patches env feature (transient_benefit_enabled, stochastic high-salience patch spawn for z_goal seeding)"
      phase: 1
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [DEV-NEED-006, MECH-189]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-4"
      title: "Stochastic attractor audit (enumerate CausalGridWorldV2 sources of irreducible randomness; mark or remove before high novelty_bonus_weight deployment)"
      phase: 1
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [DEV-NEED-003, MECH-314]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-5"
      title: "H_pos / zone_coverage telemetry (Shannon entropy of position histogram per episode, per-zone cell coverage fraction)"
      phase: 2
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [DEV-NEED-001, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-6"
      title: "residue_coverage_pct metric (fraction of grid cells with |residue| > threshold; harm_benefit_ratio)"
      phase: 2
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [DEV-NEED-004, DEV-NEED-008]
      depends_on: ["infant_substrate:GAP-1"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-7"
      title: "traj_pairwise_cosine_mean metric (edit/cosine distance across stored trajectories; volumetric coverage estimate)"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-002, DEV-NEED-005, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-8"
      title: "post_sleep_z_goal_retention metric (z_goal.norm ratio before/after sleep integration; replay_diversity_index)"
      phase: 2
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-007, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-9"
      title: "4-phase infant curriculum scheduler (config hook for phase-gated parameter switching; Phase 0 babbling -> Phase 1 benefit -> Phase 2 geography -> Phase 3 gate)"
      phase: 3
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-008, ARC-046]
      depends_on: ["infant_substrate:GAP-1", "infant_substrate:GAP-2", "infant_substrate:GAP-3"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-10"
      title: "EXQ-ISEF-001: harm gradient vs binary-contact residue geography formation speed"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-004, ARC-013]
      depends_on: ["infant_substrate:GAP-1", "infant_substrate:GAP-5", "infant_substrate:GAP-6"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-11"
      title: "EXQ-ISEF-002: transient benefit patches z_goal seeding rate comparison"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-006, MECH-189]
      depends_on: ["infant_substrate:GAP-3", "infant_substrate:GAP-5"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-12"
      title: "EXQ-ISEF-003: microhabitat zones vs homogeneous geography (latent state diversity)"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-001, DEV-NEED-007, ARC-065]
      depends_on: ["infant_substrate:GAP-2", "infant_substrate:GAP-5", "infant_substrate:GAP-7"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-13"
      title: "EXQ-ISEF-004: novelty bonus calibration (Goldilocks sweep; identify optimal novelty_bonus_weight before stochastic attractor capture)"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-003, MECH-314]
      depends_on: ["infant_substrate:GAP-4", "infant_substrate:GAP-5", "infant_substrate:GAP-6"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-14"
      title: "EXQ-ISEF-005: 4-phase curriculum vs flat parameter baselines (gate-criterion satisfaction comparison)"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [DEV-NEED-008, ARC-046]
      depends_on: ["infant_substrate:GAP-9", "infant_substrate:GAP-5", "infant_substrate:GAP-6", "infant_substrate:GAP-7", "infant_substrate:GAP-8"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-15"
      title: "Gate update: replace single z_goal.norm criterion in developmental_curriculum.md with 7-criterion table (3 blocking + 4 advisory) from infant_substrate_expansion.md Section 8"
      phase: 5
      status: open
      severity: governance
      owner_exq: null
      unblocks_claims: [DEV-NEED-008]
      depends_on: ["infant_substrate:GAP-10", "infant_substrate:GAP-11", "infant_substrate:GAP-12", "infant_substrate:GAP-13"]
      last_updated: 2026-05-16
---
# Infant Substrate Expansion Plan

**Registered:** 2026-05-16
**Status:** active
**Scope:** implement the richer infant-stage developmental substrate proposed in
`docs/architecture/infant_substrate_expansion.md`, close the DEV-NEED-001..008
measurement gaps, and replace the single-criterion childhood transition gate with
the 7-criterion table derived from targeted literature pulls.

This plan is the durable resume-point for infant substrate work across sessions.
See [infant_substrate_expansion.md](../../docs/architecture/infant_substrate_expansion.md)
for the full design: compression analysis, evidence table, diversity taxonomy,
feature proposals, curriculum schedule, metrics, and experimental manifests.

---

## One-line framing

> The infant stage has a single gate criterion (z_goal.norm) and a structurally
> homogeneous environment; neither produces the valence geography, trajectory
> diversity, or action-class coverage that DEV-NEED-001..008 require and that
> the childhood/play stage presupposes.

The V_s monostrategy problem (MECH-309) is the proximate driver: EXQ-522
(SD-054 heuristic PASS) proved the substrate can carry diverse behavior, but
every trained-policy run returns non_contributory due to monomodal V_s. That
diagnosis points upstream — the infant stage never produced a diverse behavioral
repertoire to begin with. The current infant environment is compressed in six
distinct ways (Section 2 of the design doc); each compression generates a
specific downstream deficit in the developmental gate.

Literature synthesis (37 new entries, 2026-05-16) converges on: monostrategy
prevention requires structured environment with learnable difficulty at multiple
levels, not just a high novelty_bonus_weight. MECH-314c learning-progress
curiosity (not MECH-314a novelty) produces emergent developmental staging.
Context-rigidity — not entropy collapse — is the measurable failure signature.

---

## Source artefacts

| Artefact | Role |
|---|---|
| [docs/architecture/infant_substrate_expansion.md](../../docs/architecture/infant_substrate_expansion.md) | Full design: compression analysis, evidence table, feature proposals, curriculum, metrics, gates |
| [docs/architecture/developmental_curriculum.md](../../docs/architecture/developmental_curriculum.md) | Current infant stage parameters; gate criterion to be replaced |
| [docs/architecture/developmental_needs_register.md](../../docs/architecture/developmental_needs_register.md) | DEV-NEED-001..008 with gap log and quantitative gate proposals |
| [evidence/planning/behavioral_diversity_acceptance_criteria.md](behavioral_diversity_acceptance_criteria.md) | Rung 0-4 diversity framework; trajectory diversity prerequisites |
| [evidence/literature/targeted_review_developmental_exploration_hippocampal_retrieval/](../literature/targeted_review_developmental_exploration_hippocampal_retrieval/) | 19 entries: babbling, hippocampal retrieval, enrichment/deprivation |
| [evidence/literature/targeted_review_intrinsic_motivation_exploration/](../literature/targeted_review_intrinsic_motivation_exploration/) | 5 entries: Pathak 2017, Burda 2018, Monosov 2024, Oudeyer 2016, Ventura 2024 |
| [evidence/literature/targeted_review_rl_diversity_monostrategy_curriculum/](../literature/targeted_review_rl_diversity_monostrategy_curriculum/) | 6 entries: DIAYN, DvD, PAIRED, MAP-Elites, IMGEP, Narvekar survey |
| [evidence/literature/targeted_review_infant_affordance_valence_map/](../literature/targeted_review_infant_affordance_valence_map/) | 5 entries: Adolph 2019, Keren-Portnoy 2021, Valadi 2020, Berridge 1998, Burnay 2020 |
| ree-v3/ree_core/environment/causal_grid_world.py | Target file for env feature implementation (GAP-1..4) |

---

## Existing substrate (do not duplicate)

Already implemented and usable for infant stage:

| Component | Location | Status |
|---|---|---|
| MECH-313 noise floor (LC-NE tonic analog) | `ree-v3/ree_core/` | PASS 2026-05-10; entropy lift confirmed EXQ-567 |
| MECH-314 structured curiosity bonus (novelty_bonus_weight) | `ree-v3/ree_core/utils/config.py` | Implemented; defaults to 0.0 (must be set for infant stage) |
| MECH-314c learning-progress (e3._running_variance EMA) | `ree-v3/ree_core/predictors/e3_selector.py` | Phase-1 approximation implemented |
| SD-049 multi-resource heterogeneity | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED 2026-05-03/04; resource_introduction_schedule hook available |
| SD-054 reef safe zones + bipartite layout | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED 2026-05-11; heuristic PASS EXQ-522 |
| SD-047 multi-source hazard dynamics | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED |
| SD-048 interoceptive noise | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED (potential stochastic attractor — see GAP-4) |
| SD-029 scheduled external hazard | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED |
| ARC-046 hazard protection (residue_scale_factor ~0.1) | `developmental_curriculum.md` parameter | Specified; residue_scale_factor must be enabled (currently 0.0 default for infant) |
| offline_integration_frequency | `ree-v3/ree_core/utils/config.py` | Available; high sleep:wake ratio for infant (every 10-20 steps) |

---

## Gap inventory

Fifteen gaps across 5 phases. Phases 1-2 (env features + telemetry) are the
minimum prerequisite for any validation run. Phase 3 (curriculum scheduler) is
independent and can be deferred without blocking experiments. Phase 4 runs the
5 candidate experiments from the design doc. Phase 5 closes the governance loop.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | Harm gradient env parameter | high | DEV-NEED-004 gate criterion; residue geography experiments |
| **GAP-2** | Microhabitat zones env parameter | high | DEV-NEED-001/003/007; z_world coverage experiments |
| **GAP-3** | Transient benefit patches env parameter | high | DEV-NEED-006 z_goal seeding experiments |
| **GAP-4** | Stochastic attractor audit | high | Safe deployment of novelty_bonus_weight > 0 |
| **GAP-5** | H_pos / zone_coverage telemetry | high | DEV-NEED-001 blocking gate; EXQ-ISEF experiments |
| **GAP-6** | residue_coverage_pct metric | high | DEV-NEED-004 blocking gate |
| **GAP-7** | traj_pairwise_cosine_mean metric | medium | DEV-NEED-002/005 advisory gate |
| **GAP-8** | post_sleep_z_goal_retention metric | medium | DEV-NEED-007 advisory gate |
| **GAP-9** | 4-phase curriculum scheduler | medium | Emergent developmental staging (Oudeyer 2016) |
| **GAP-10** | EXQ-ISEF-001: harm gradient vs binary-contact | medium | DEV-NEED-004 evidence |
| **GAP-11** | EXQ-ISEF-002: transient benefit z_goal seeding | medium | DEV-NEED-006 / MECH-189 evidence |
| **GAP-12** | EXQ-ISEF-003: microhabitat latent diversity | medium | DEV-NEED-001/007 / ARC-065 evidence |
| **GAP-13** | EXQ-ISEF-004: novelty bonus calibration | medium | MECH-314 calibration |
| **GAP-14** | EXQ-ISEF-005: curriculum vs flat comparison | medium | DEV-NEED-008 / ARC-046 evidence |
| **GAP-15** | Gate criterion update in developmental_curriculum.md | governance | DEV-NEED-008 gate closure |

---

## Sequenced plan

### Phase 1: Environment features (GAP-1, 2, 3, 4)

All four can be implemented in parallel. GAP-4 (audit) is code-read only — no
new implementation, just enumerate `random.*` calls in `causal_grid_world.py`
step() and reset() and classify each as learnable-stochastic vs irreducible.

GAP-1 deliverables: `harm_gradient_enabled: bool`, `harm_gradient_outer_radius: float`,
`harm_gradient_inner_radius: float`, `harm_gradient_scale: float` in
`CausalGridWorldV2.__init__`. Reward computed in `step()` as
`-hazard_harm * (1 - d/r_outer)^2 * scale` for cells within r_outer but outside
r_inner of any hazard. No terminal contact until r_inner.

GAP-2 deliverables: `microhabitat_enabled: bool`, `n_microhabitats: int`,
`zone_A/B/C_resource/hazard_factor: float`, `zone_C_ambient_bonus: float`.
Zone map generated once per episode via Voronoi seed on `reset()`.
Zone-B hazard_factor ~1.8x; zone-C hazard_factor 0.0; zone-C ambient +0.05.

GAP-3 deliverables: `transient_benefit_enabled: bool`, `transient_benefit_prob: float`,
`transient_benefit_duration: int`, `transient_benefit_multiplier: float`.
Spawn logic in `step()`: each step, with probability p, add patch at a
zone-weighted random cell. Patch tracked in episode buffer; expires after N steps.
Contact reward = `resource_benefit * multiplier`.

GAP-4 deliverables: a brief audit note (can live in the design doc or as a
comment block in causal_grid_world.py). Flag SD-048 interoceptive noise as
potential stochastic attractor — its noise scale should be excluded from the
novelty signal computation when novelty_bonus_weight > 0.

---

### Phase 2: Telemetry infrastructure (GAP-5, 6, 7, 8)

GAP-5: Add to `info` dict in `step()` or compute in training loop:
- `pos_entropy`: Shannon entropy of position histogram (rolling 100-step window)
- `zone_coverage`: dict of {zone: fraction cells visited} — requires zone_map
  from GAP-2, OR stub with single zone until GAP-2 lands

GAP-6: Add to training loop or episode summary:
- `residue_coverage_pct`: fraction of grid cells where `abs(residue[y,x]) > threshold`
  (suggested threshold: 0.02 * residue_scale_factor). Requires residue_scale_factor > 0.

GAP-7: At end of each episode, compute over N sampled trajectory pairs:
- `traj_cosine_mean`: mean(1 - cosine_similarity(traj_i, traj_j)) for N random pairs.
  Trajectories represented as flattened (y,x) sequences or action sequences.

GAP-8: After each sleep integration cycle, log:
- `z_goal_before_sleep`: z_goal.norm() at sleep entry
- `z_goal_after_sleep`: z_goal.norm() after `offline_integration_frequency` steps
- `z_goal_retention`: z_goal_after_sleep / z_goal_before_sleep

---

### Phase 3: Curriculum scheduler (GAP-9) — independent

Implement a curriculum_phase counter in REEAgent or training loop that gates
which env parameters are active. Phase boundaries triggered by episode count +
telemetry thresholds (or hard episode count if telemetry unavailable):

```python
# Pseudocode for infant curriculum scheduler
if episode < 100 and H_pos < threshold:
    phase = 0  # babbling
elif z_goal.norm() < 0.3 or benefit_contacts < 5:
    phase = 1  # benefit discovery
elif residue_coverage_pct < 0.10:
    phase = 2  # geography
else:
    phase = 3  # pre-gate
```

Phase 0: novelty_bonus_weight=0.5, E3 planning disabled, no transient benefits,
no harm gradient, no microhabitats, residue_scale_factor=0.0.

Phase 1: +transient_benefit_enabled, +harm_gradient (mild), residue_scale_factor=0.05.

Phase 2: +microhabitat_enabled, harm_gradient full, multi-resource active (food+water),
residue_scale_factor=0.10. SD-054 bipartite active.

Phase 3: all features active. E3 planning at weight 0.1. approach adult parameters.

---

### Phase 4: Validation experiments (GAP-10..14)

Each experiment script follows the `/queue-experiment` skill path. No direct
writes to `experiment_queue.json` outside that skill. Scripts go in
`ree-v3/experiments/` with the EXQ-ISEF-* identifier in the filename; the
actual queue IDs will be assigned at queue time (EXQ-NNN where NNN is next
available).

**EXQ-ISEF-001 (GAP-10)** — harm gradient residue geography speed
- Prereqs: GAP-1, GAP-5, GAP-6
- Criterion: treatment residue_coverage_pct > 2x control at episode 1000

**EXQ-ISEF-002 (GAP-11)** — transient benefit z_goal seeding rate
- Prereqs: GAP-3, GAP-5
- Criterion: treatment median first z_goal.norm() > 0.4 crossing < 0.7x control

**EXQ-ISEF-003 (GAP-12)** — microhabitat latent diversity
- Prereqs: GAP-2, GAP-5, GAP-7
- Criterion: treatment z_world PCA top-3 variance > 1.2x control at episode 1000

**EXQ-ISEF-004 (GAP-13)** — novelty bonus Goldilocks calibration
- Prereqs: GAP-4, GAP-5, GAP-6
- Criterion: identify optimal novelty_bonus_weight ∈ [0.1, 1.0]; report Goldilocks point

**EXQ-ISEF-005 (GAP-14)** — curriculum vs flat comparison
- Prereqs: GAP-9, all telemetry GAPs
- Criterion: treatment passing > 5/7 gate criteria; controls < 5/7

---

### Phase 5: Gate update (GAP-15)

After EXQ-ISEF-001..004 results are reviewed, update `developmental_curriculum.md`
to replace the single `z_goal.norm()` gate with the 7-criterion table. Update
`developmental_needs_register.md` gap log to reflect resolved gaps. Run governance
pipeline to confirm no pending_review items generated by the new evidence.

---

## Status table

| Gap | Status | Owner EXQ | Last updated |
|-----|--------|-----------|-------------|
| GAP-1 Harm gradient env | open | — | 2026-05-16 |
| GAP-2 Microhabitat zones env | done | V3-EXQ-577 | 2026-05-16 |
| GAP-3 Transient benefit patches env | open | — | 2026-05-16 |
| GAP-4 Stochastic attractor audit | open | — | 2026-05-16 |
| GAP-5 H_pos / zone_coverage telemetry | open | — | 2026-05-16 |
| GAP-6 residue_coverage_pct metric | open | — | 2026-05-16 |
| GAP-7 traj_pairwise_cosine_mean | open | — | 2026-05-16 |
| GAP-8 post_sleep_z_goal_retention | open | — | 2026-05-16 |
| GAP-9 Curriculum scheduler | open | — | 2026-05-16 |
| GAP-10 EXQ-ISEF-001 | open | — | 2026-05-16 |
| GAP-11 EXQ-ISEF-002 | open | — | 2026-05-16 |
| GAP-12 EXQ-ISEF-003 | open | — | 2026-05-16 |
| GAP-13 EXQ-ISEF-004 | open | — | 2026-05-16 |
| GAP-14 EXQ-ISEF-005 | open | — | 2026-05-16 |
| GAP-15 Gate criterion update | open | — | 2026-05-16 |

---

## Decision log

### 2026-05-16 — Plan registered

Infant substrate expansion design doc completed after 4 parallel lit-pulls (37
new entries). Plan registered immediately from the design doc's deliverables.
No implementation work has started; all GAPs are open. Phase 1 env features are
the critical path since they are prerequisites for all telemetry and experiments.

The stochastic attractor audit (GAP-4) must precede any novelty_bonus_weight
deployment — Burda 2018 / Pathak 2017 both demonstrate permanent capture of the
curiosity signal by irreducible random stimuli. SD-048 interoceptive noise is the
primary suspect.

The 7-criterion gate (GAP-15) is intentionally deferred until EXQ-ISEF-001..004
results inform which criteria are empirically achievable and at what thresholds.
The thresholds in Section 8 of the design doc are proposals, not commitments.

### 2026-05-16 — GAP-2 implemented (microhabitat zones env feature)

GAP-2 landed in `ree-v3/ree_core/environment/causal_grid_world.py`
(CausalGridWorldV2). Ten env-only `__init__` kwargs, not surfaced through
`REEConfig.from_dims` (SD-047/048/049/054/GAP-1 precedent), all no-op defaults:
`microhabitat_enabled` (master, False), `n_microhabitats` (3), `zone_A/B/C`
resource+hazard factors (1.5/0.3, 0.8/1.8, 0.3/0.0), `zone_C_ambient_bonus`
(0.05), `zone_novelty_decay` (0.95).

`_build_microhabitat_zones()` builds a per-episode Voronoi zone map over
interior cells (n seeds via `self._rng`, nearest-seed assignment); cells
adjacent to a different base zone are promoted to the automatic D border
zone (neutral 1.0/1.0, no ambient). `_pop_zone_weighted()` replaces the
bare `forage_pool.pop()` at the hazard + SD-049 + legacy resource spawn
sites, weighting cell selection by the zone's resource/hazard factor; the
disabled path keeps a bare `pop()` so no extra RNG draws occur (bit-identical
OFF, verified over 300 steps). A zone-C ambient presence bonus is added in
`step()` (after the GAP-1 harm-gradient block, before move) when the agent
enters a zone-C cell with `transition_type == "none"`, decaying
multiplicatively per zone-C visit by `zone_novelty_decay`. Four `info`
diagnostics added (always present, inert when disabled):
`microhabitat_enabled`, `microhabitat_zone_at_agent`,
`microhabitat_zone_c_ambient_this_tick`, `microhabitat_zone_counts`.

Contract tests: `ree-v3/tests/contracts/test_microhabitat_gap2.py`
(11 tests, C1-C5: OFF backward-compat + bit-identical RNG, zone-map
coverage, zone-weighted hazard density bias, zone-C ambient fire+decay,
reset state clearing) -- 11/11 PASS. Full regression suite 367/367
relevant + 7/7 preflight PASS with master OFF (the one failing test,
`test_mech_293_ghost_probes.py::test_c2_master_off_no_op`, is pre-existing
and unrelated -- fails identically with GAP-2 changes stashed). Activation
smoke + 300-step bit-identical-OFF parity PASS.

Validation experiment V3-EXQ-577 queued (substrate-readiness diagnostic,
`experiment_purpose=diagnostic`, `claim_ids=[]` -- mirrors GAP-1 V3-EXQ-576
precedent; GAP-2's `unblocks_claims` are governed by the full infant
pipeline + EXQ-ISEF behavioural runs, not this readiness diagnostic).
2-arm (OFF/ON) x 3 seeds, ~10 min, dry-run smoke 4/4 criteria PASS.
`claims.yaml` NOT modified: GAP-2 alone does not resolve ARC-065
`v3_pending` (gated on the full infant pipeline). Phase-1 critical path
now has GAP-1 + GAP-2 done; GAP-3 (transient benefit patches) and GAP-4
(stochastic attractor audit) remain open.
