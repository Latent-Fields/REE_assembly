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
      status: done
      severity: high
      owner_exq: "V3-EXQ-578"
      unblocks_claims: [DEV-NEED-006, MECH-189]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-4"
      title: "Stochastic attractor audit (enumerate CausalGridWorldV2 sources of irreducible randomness; mark or remove before high novelty_bonus_weight deployment)"
      phase: 1
      status: done
      severity: high
      owner_exq: "audit-note (infant_substrate_expansion.md S5.6; code-read only, no EXQ)"
      unblocks_claims: [DEV-NEED-003, MECH-314]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-5"
      title: "H_pos / zone_coverage telemetry (Shannon entropy of position histogram per episode, per-zone cell coverage fraction)"
      phase: 2
      status: done
      severity: high
      owner_exq: "V3-EXQ-579"
      unblocks_claims: [DEV-NEED-001, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-6"
      title: "residue_coverage_pct metric (fraction of grid cells with |residue| > threshold; harm_benefit_ratio)"
      phase: 2
      status: done
      severity: high
      owner_exq: "V3-EXQ-580"
      unblocks_claims: [DEV-NEED-004, DEV-NEED-008]
      depends_on: ["infant_substrate:GAP-1"]
      last_updated: 2026-05-16
    - id: "infant_substrate:GAP-7"
      title: "traj_pairwise_cosine_mean metric (edit/cosine distance across stored trajectories; volumetric coverage estimate)"
      phase: 2
      status: done
      severity: medium
      owner_exq: "V3-EXQ-584"
      unblocks_claims: [DEV-NEED-002, DEV-NEED-005, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-17
    - id: "infant_substrate:GAP-8"
      title: "post_sleep_z_goal_retention metric (z_goal.norm ratio before/after sleep integration; replay_diversity_index)"
      phase: 2
      status: done
      severity: medium
      owner_exq: "V3-EXQ-585"
      unblocks_claims: [DEV-NEED-007, DEV-NEED-008]
      depends_on: []
      last_updated: 2026-05-17
    - id: "infant_substrate:GAP-9"
      title: "4-phase infant curriculum scheduler (config hook for phase-gated parameter switching; Phase 0 babbling -> Phase 1 benefit -> Phase 2 geography -> Phase 3 gate)"
      phase: 3
      status: done
      severity: medium
      owner_exq: "V3-EXQ-586"
      unblocks_claims: [DEV-NEED-008, ARC-046]
      depends_on: ["infant_substrate:GAP-1", "infant_substrate:GAP-2", "infant_substrate:GAP-3"]
      last_updated: 2026-05-17
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
| SD-048 interoceptive noise | `ree-v3/ree_core/environment/causal_grid_world.py` | IMPLEMENTED (CONFIRMED primary stochastic attractor — GAP-4 audit; mask from novelty signal when novelty_bonus_weight > 0) |
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
| GAP-2 Microhabitat zones env | done (redraw guard added) | V3-EXQ-577a PASS (supersedes V3-EXQ-577) | 2026-05-16 |
| GAP-3 Transient benefit patches env | done | V3-EXQ-578 | 2026-05-16 |
| GAP-4 Stochastic attractor audit | done | audit-note | 2026-05-16 |
| GAP-5 H_pos / zone_coverage telemetry | done | V3-EXQ-579 | 2026-05-16 |
| GAP-6 residue_coverage_pct metric | done | V3-EXQ-580 | 2026-05-16 |
| GAP-7 traj_pairwise_cosine_mean | done | V3-EXQ-584 (queued) | 2026-05-17 |
| GAP-8 post_sleep_z_goal_retention | done | V3-EXQ-585 (queued) | 2026-05-17 |
| GAP-9 Curriculum scheduler | done | V3-EXQ-586 (queued) | 2026-05-17 |
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

### 2026-05-16 — GAP-5 implemented (pos_entropy / zone_coverage telemetry)

`CausalGridWorldV2.step()` now emits four always-present info keys:
`pos_telemetry_enabled`, `pos_entropy` (Shannon entropy in nats of the agent
position histogram over a rolling `pos_entropy_window`, default 100; `-1.0`
sentinel when disabled/empty), `pos_entropy_window` (echo), and `zone_coverage`
(`{zone_id: visited_fraction}` over the GAP-2 `_zone_map` zones 0..3 when
microhabitat is enabled, else a single-zone-0 stub over the interior; `{}` when
disabled). New env-only kwargs `pos_telemetry_enabled` / `pos_entropy_window` /
`zone_coverage_stub_single_zone` (not surfaced through `REEConfig.from_dims`,
matching the GAP-1/2/3 + SD-047/48/49 precedent).

Departure from the GAP-1/2/3 "default OFF / bit-identical OFF" precedent:
`pos_telemetry_enabled` **defaults ON**. The precedent exists because those
substrates draw RNG and/or change env dynamics; GAP-5 telemetry does neither, so
agent behaviour, RNG sequences, and results are bit-identical whether ON or OFF.
GAP-5 is the DEV-NEED-001 blocking gate, so defaulting ON means the EXQ-ISEF
experiments get H_pos / zone_coverage without a flag flip. The master switch is
retained for the contract OFF path and zero-overhead runs.

Validation: 14/14 contract tests in
`ree-v3/tests/contracts/test_pos_telemetry_gap5.py` (C1 OFF inert +
bit-identical layout, C2 entropy correctness incl. window cap / 0-entropy /
ln(K), C3 GAP-2 zone_coverage, C4 single-zone stub, C5 reset clears) PASS;
full 398/398 contracts+preflight regression-clean. Validation EXQ
**V3-EXQ-579** queued (substrate-readiness diagnostic, ARM_OFF / ARM_ON_STUB /
ARM_ON_ZONES; dry-run 5/5 criteria PASS). GAP-5 unblocks DEV-NEED-001 and
DEV-NEED-008; GAP-6/7/8 telemetry remain open.

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

### 2026-05-16 — GAP-3 implemented (transient benefit patches env feature)

GAP-3 landed in `ree-v3/ree_core/environment/causal_grid_world.py`
(CausalGridWorldV2), implemented in parallel with the GAP-2 session (user
authorised concurrent work; GAP-3 is an independent code block + separate
contract-test file). Four env-only `__init__` kwargs, not surfaced through
`REEConfig.from_dims` (SD-047/048/049/054/GAP-1/GAP-2 precedent), all no-op
when the master is off: `transient_benefit_enabled` (master, False),
`transient_benefit_prob` (0.02), `transient_benefit_duration` (15),
`transient_benefit_multiplier` (2.0).

Each `step()`, after the env-drift block and before subgoal timeout
(agent-independent, on the env clock), expiry runs first (patches whose
`spawn_step + duration` has elapsed are dropped: grid cell cleared,
removed from `self.resources` + tracking), then a single Bernoulli spawn
attempt at `transient_benefit_prob`. `_spawn_transient_benefit()` picks an
empty interior cell (zone-weighted via `_pop_zone_weighted` when GAP-2
microhabitat zones are active, uniform shuffle otherwise; reef cells
excluded), tags it as a resource entity so the proximity field and
perception treat it as a high-salience benefit, and registers it in
`self.resources` + `self._transient_benefits` (with expiry) +
`self._transient_benefit_cells`. The resource-contact branch detects a
transient cell and pays `resource_benefit * transient_benefit_multiplier`
(overriding the SD-049 per-type amplitude; transient patches are
intentionally not SD-049 typed). All RNG draws are guarded by the master
switch so seed sequences for existing experiments are bit-identical when
disabled. Six `info` diagnostics added (always present, inert when
disabled): `transient_benefit_enabled`, `transient_benefit_n_active`,
`transient_benefit_n_spawned`, `transient_benefit_n_contacted`,
`transient_benefit_n_expired`, `transient_benefit_contact_this_tick`.

Contract tests: `ree-v3/tests/contracts/test_transient_benefit_gap3.py`
(12 tests, C1-C5: OFF backward-compat + bit-identical RNG over reset AND
stepped trajectory, spawn-every-tick at prob=1.0 with correct expiry
bookkeeping, single-patch expiry exactly `duration` steps after spawn,
contact-reward multiplier + plain-resource-unaffected, reset state
clearing) -- 12/12 PASS. Full regression suite 376 passed + 7/7 preflight
with master OFF (the one failing test,
`test_mech_293_ghost_probes.py::test_c2_master_off_no_op`, is pre-existing
and unrelated -- fails identically with GAP-3 changes stashed on a clean
HEAD). Instrumented run confirms conservation: at prob=1.0/duration=3,
`n_active` stabilises at 3 and `n_expired` increments in lockstep with
`n_spawned`.

Validation experiment V3-EXQ-578 queued (substrate-readiness diagnostic,
`experiment_purpose=diagnostic`, `claim_ids=[]` -- mirrors GAP-1 V3-EXQ-576
/ GAP-2 V3-EXQ-577 precedent; GAP-3's `unblocks_claims` DEV-NEED-006 /
MECH-189 are governed by the full infant pipeline + EXQ-ISEF behavioural
runs, not this readiness diagnostic). 2-arm (OFF/ON) x 3 seeds, ~12 min,
dry-run smoke 4/4 criteria PASS (C1 spawn-rate band, C2 ARM_0 fully
silent, C3 patches expire, C4 contact multiplier exact). `claims.yaml`
NOT modified: GAP-3 alone does not resolve any `v3_pending` (gated on the
full infant pipeline). Phase-1 critical path now has GAP-1 + GAP-2 + GAP-3
done; GAP-4 (stochastic attractor audit) is the last open Phase-1 node.

### 2026-05-16 — GAP-4 completed (stochastic attractor audit)

GAP-4 is code-read only (no implementation, no EXQ). Every RNG call site in
`CausalGridWorldV2.reset()` / `step()` was enumerated and classified
learnable-stochastic vs irreducible. Full audit (enumeration table + verdict +
binding action) written into `docs/architecture/infant_substrate_expansion.md`
section 5.6 (the pre-existing audit placeholder, checklist replaced with the
completed audit).

Key facts: one seeded master RNG (`causal_grid_world.py:607`) -> runs are
reproducible; the attractor concern is within-episode irreducible entropy a
curiosity signal cannot predict away (Burda 2018 / Pathak 2017 noisy-TV).
Verdict: **SD-048 interoceptive noise is the confirmed primary irreducible
stochastic attractor** -- Source 1 autonomic i.i.d. Gaussian on `harm_obs_a`
every tick (`:2631`) and the Poisson sensitisation onset (`:2609`); fatigue
AR(1) (`:2575`) is a partial attractor. SD-047 weather innovation (`:2399`) +
transient Poisson (`:2415`) are secondary partial attractors. Reset/spawn/
respawn/hazard-drift randomness are learnable-stochastic (no risk). All
SD-047/SD-048 noise is OFF by default; risk materialises only with
`novelty_bonus_weight > 0` (the infant config). Confirms the plan's
pre-registered suspicion.

Binding constraint passed downstream to GAP-13 (EXQ-ISEF-004,
`depends_on` GAP-4): MECH-314a (z_world RBF novelty) is structurally safe --
z_world does not carry `harm_obs_a`. The exposure is MECH-314b/c, which
consume `e3._running_variance` (PE) that SD-048 autonomic noise inflates;
when `use_structured_curiosity AND interoceptive_noise_enabled` the PE feed
to 314b/c must exclude / low-pass the harm-stream PE component (option (b)
exclude-from-novelty; option (a) make-Markovian is unavailable for i.i.d.
readout noise). An explicit config-coupling assertion must be wired BEFORE
GAP-13 runs. `claims.yaml` NOT modified (audit only; no claim resolved --
DEV-NEED-003 / MECH-314 governed by the full infant pipeline). Phase 1
(GAP-1..4) is now complete; the critical path advances to Phase 2 telemetry
(GAP-5..8).

### 2026-05-16 — GAP-6 implemented (residue_coverage_pct / harm_benefit_ratio telemetry)

GAP-6 differs structurally from GAP-5: the residue field is **agent-side**
(`ree-v3/ree_core/residue/field.py` `ResidueField`), not env-side. There is
no residue grid in `causal_grid_world.py`, so GAP-6 is **not** an env
`info`-dict telemetry key like GAP-5 — it is a read-only metric over the
agent's `ResidueField`. This matches the plan's "add to training loop or
episode summary" wording and the EXQ-575 precedent
(`residue_coverage_pct = active_centers / 32`).

Landed as one additive, read-only method
`ResidueField.get_coverage_telemetry(residue_scale_factor=1.0)` returning
native python floats/ints: `residue_coverage_pct`,
`residue_coverage_threshold`, `residue_active_centers`,
`residue_n_centers`, `harm_benefit_ratio`, `harm_total`, `benefit_total`.
`residue_coverage_pct` = fraction of harm-residue RBF centers that are
active AND `abs(weight) > 0.02 * max(residue_scale_factor, 1e-8)` (the
plan's grid-cell `abs(residue)>thr` definition mapped to the RBF basis —
the V3 substrate has no literal (y,x) grid). `harm_benefit_ratio` =
`total_residue / total_benefit` when the benefit terrain is enabled and
benefit has accumulated; a single `-1.0` sentinel otherwise (benefit
terrain off, or zero benefit accumulated — GAP-5 sentinel precedent).

Non-invasive by construction: `get_statistics()` is deliberately left
**unchanged** (EXQ-575 and other callers depend on its exact 4-key set);
the new method mutates no field state and nothing in the agent/env hot
path calls it, so every existing run is **bit-identical**. No config
change, no `from_dims` surface, no env change. No MECH-094 concern (pure
read; no simulation/replay/memory write). No phased training (no encoder).

Contract tests: `ree-v3/tests/contracts/test_residue_coverage_gap6.py`
(12 tests, C1 surface + get_statistics intact, C2 coverage correctness
incl. sub-threshold exclusion / scale-factor scaling / 0.0-clamp, C3
harm_benefit_ratio sentinels, C4 non-invasive + idempotent, C5 bounds)
— 12/12 PASS. Full regression 403/403 contracts + 7/7 preflight green.

Validation experiment **V3-EXQ-580** queued (substrate-readiness
diagnostic, `experiment_purpose=diagnostic`, `claim_ids=[]` — mirrors the
GAP-1 V3-EXQ-576 / GAP-5 V3-EXQ-579 precedent). 2-arm (ARM_0 binary
hazard contact / ARM_1 GAP-1 `harm_gradient_enabled=True`) x 3 seeds,
512-center field so the every-tick-in-band ARM_1 signal does not saturate
to the sparse on-contact ARM_0 value; dry-run smoke 5/5 criteria PASS
(C0 well-formed, C1 ARM_1 strictly > ARM_0 by >= 0.01 all seeds,
C2 -1.0 sentinel both arms, C3 non-invasive, C4 ARM_0 has harm residue).
`claims.yaml` NOT modified: GAP-6 alone does not resolve any
`v3_pending` (DEV-NEED-004 / DEV-NEED-008 are governed by the full
infant pipeline + EXQ-ISEF behavioural runs, not this readiness
telemetry). Phase-2 telemetry now has GAP-5 + GAP-6 done; GAP-7
(traj_pairwise_cosine_mean) and GAP-8 (post_sleep_z_goal_retention)
remain open.

### 2026-05-16 — GAP-2 degenerate-seeding redraw guard (V3-EXQ-577 autopsy "enrich" half)

The V3-EXQ-577 (gap2_microhabitat_validation) failure autopsy
(`failure_autopsy_EXQ-577_2026-05-16`) found C2 was a **false-negative**:
~2-3% of stochastic episodes land the 3 Voronoi seeds close enough that
one whole base niche (0/1/2) is consumed by the boundary→D (zone 3)
promotion. C1/C3/C4 PASS — the GAP-2 mechanism is functionally correct;
this is an **enrichment** (defense in depth for the infant
niche-discrimination curriculum DEV-NEED-001/003/007 / EXQ-ISEF-003),
not a bug fix of broken logic. User-confirmed routing: "both — enrich +
relax"; this entry is the enrich half.

`_build_microhabitat_zones` (`ree-v3/ree_core/environment/causal_grid_world.py`)
was refactored into a deterministic capped-retry guard: the verbatim
pre-guard draw+Voronoi+boundary→D logic moved into a pure
`_draw_microhabitat_zone_map` helper; a `_count_surviving_base_zones`
helper counts distinct base codes (0..n_seeds-1, excluding the D
ecotone) surviving in the interior. After promotion, if fewer than
`n_seeds` base zones survive, the seeds are redrawn via `self._rng`
(fully deterministic given the per-episode seed) up to a cap; the first
non-degenerate draw wins, and on cap exhaustion the best (most-surviving)
draw is kept and a diagnostic surfaced. One env-only `__init__` kwarg
`microhabitat_max_seed_redraws` (default 8; NOT surfaced through
`REEConfig.from_dims` — SD-047/048/049 + GAP-1/2/3/5 precedent; `0` is
an escape hatch reproducing pre-guard map behaviour). Two always-present
`step()` info keys added (`microhabitat_redraw_count`,
`microhabitat_redraw_exhausted`; 0/False when disabled) so the relax-half
EXQ can read the collapse-frequency statistic.

Bit-identical OFF preserved by construction: `_build_microhabitat_zones`
is only called on the enabled path; the disabled path
(`_zone_map=None`, bare `pool.pop()`) is untouched — zero extra RNG
draws OFF (300-step default-vs-explicit-OFF parity PASS). The common
~97-98% enabled case accepts the first draw and consumes `self._rng`
exactly as the pre-guard code did; only the ~2-3% degenerate episodes
draw extra RNG (the intended enrichment; the ON path has no
bit-identical contract).

Verification: `ree-v3/tests/contracts/test_microhabitat_gap2.py`
extended with C6 (3 tests: 300-episode autopsy-repro zero-collapse +
guard-engaged + no-exhaustion, inert-when-disabled info keys, cap=0
escape hatch) — 14/14 PASS. Full regression 413/413 contracts + 7/7
preflight green; `validate_queue.py` OK. Guard-efficacy smoke at the
exact autopsy config (size=14, seeds 0/1/2, 100 eps, 6 hazards):
**pre-guard cap=0 → 7/300 collapses** (exactly the autopsy's
missing_012 = 2+2+3), **post-guard cap=8 → 0/300 collapses**, 6 redraws
engaged, 0 exhausted. Threshold met: base-zone-collapse rate ~0 over
100 episodes/seed with strict per-episode {0,1,2} presence.

`claims.yaml` NOT modified: GAP-2 alone resolves no `v3_pending`
(same precedent as the original GAP-2/GAP-6 entries; ARC-065 et al. are
governed by the full infant pipeline). Validation experiment
**V3-EXQ-577a** queued via `/queue-experiment` (corrected C2:
per-episode well-formedness + ≥2 base zones + zone 3 present, {0,1,2}
asserted aggregated over episodes, base-zone-collapse frequency reported
as a diagnostic stat; `supersedes: gap2_microhabitat_validation`). The
local runner (DLAPTOP-4.local) auto-claimed and ran it immediately —
**V3-EXQ-577a PASS** (`v3_exq_577a_gap2_microhabitat_validation_20260516T230804Z_v3`,
non-dry, 3/3 seeds C1-C4 True; diagnostic `base_zone_collapse_count=0`
/ `collapse_rate=0.0` / `redraws=1` per seed / `exhausted=0` — the guard
engages once per seed and drives residual collapse to exactly zero over
100 eps/seed). Status-table owner-EXQ reconciled to V3-EXQ-577a (PASS,
per autopsy §7). Governance still owns the V3-EXQ-577 manifest
reclassification to `evidence_direction: superseded` (autopsy §7
explicitly defers that to the governance pass — not applied here).
GAP-5 flag (autopsy learning #3): the GAP-5 `zone_coverage` consumer
must still tolerate a base zone with 0 cells — now effectively
impossible post-guard but the consumer remains defensively correct
either way.

### 2026-05-17 -- GAP-7 implemented (traj_pairwise_cosine_mean telemetry)

`CausalGridWorldV2` now emits three always-present info keys for
trajectory diversity: `traj_telemetry_enabled`, `traj_pairwise_cosine_mean`
(mean(1 - cosine_similarity) over up to `traj_n_pairs` random pairs drawn
from a rolling buffer of up to `traj_max_stored` episode-level position
histograms; `-1.0` sentinel when disabled or fewer than 2 episodes stored),
and `traj_n_episodes_stored` (current buffer length). New env-only kwargs:
`traj_telemetry_enabled` (default True), `traj_max_stored` (20),
`traj_n_pairs` (20). Not surfaced through `REEConfig.from_dims` (same
precedent as GAP-5/6 and all harm_gradient_*/microhabitat_* params).

Representation: trajectories stored as normalised position histograms
(fraction of steps at each grid cell; fixed-length `size*size` float32
vectors). Cosine similarity computed between histogram pairs; 1 - sim
gives pairwise diversity distance. Pair sampling uses a separate
`_traj_pair_rng` (seeded from env seed) that does not touch `self._rng`,
so env dynamics are bit-identical ON vs OFF.

`_traj_store` persists across episodes (cleared only at fresh env
construction); `_traj_current` is per-episode (cleared by `reset()` and
`reset_to()`). The metric updates once per episode on the `done=True`
step and the cached value is returned on all intermediate steps.

Matching GAP-5 precedent: `traj_telemetry_enabled` defaults ON (no RNG
draws, no dynamics feedback -> bit-identical). Advisory gate criterion is
`traj_pairwise_cosine_mean > 0.3` (DEV-NEED-002/005 column in the 7-criterion
gate table).

Contract tests: `ree-v3/tests/contracts/test_traj_pairwise_cosine_gap7.py`
(13 tests: C1 OFF sentinels + bit-identical layout, C2 store growth +
cap + sentinel-until-2, C3 update timing, C4 cosine metric properties,
C5 reset semantics) -- **13/13 PASS**. Full regression **460/460**
contracts + preflight green.

Validation experiment **V3-EXQ-584** queued (substrate-readiness
diagnostic, `experiment_purpose=diagnostic`, `claim_ids=[]`). Two-arm
(ARM_0 OFF / ARM_1 ON) x 3 seeds, 5 episodes per arm per seed. Dry-run
smoke: 6/6 verdicts PASS, all C0-C4 criteria met, mean_metric_arm1=0.95
(random actions in 12x12 grid with hazards produce highly diverse
trajectories -- expected, validates metric is live). `claims.yaml` NOT
modified: GAP-7 alone does not resolve any `v3_pending` (DEV-NEED-002/005
are governed by the full EXQ-ISEF validation runs and gate-criterion
satisfaction, not this readiness telemetry). Phase-2 telemetry: GAP-5/6/7
done; GAP-8 (post_sleep_z_goal_retention) remains open.

### 2026-05-17 -- GAP-8 implemented (post_sleep_z_goal_retention + replay_diversity_index)

GAP-8 differs structurally from GAP-5/6/7: it is not an env `info`-dict
metric or a training-loop computation -- it is telemetry on the sleep
integration cycle itself. Landed as two additions to
`SleepLoopManager._run_cycle()` in
`ree-v3/ree_core/sleep/phase_manager.py`:

1. **`_safe_z_goal_norm(agent)` static method** -- non-invasive read of
   `agent.goal_state._z_goal.norm().item()`; returns -1.0 sentinel when
   `goal_state` is absent or `_z_goal` is None. Placed alongside the
   existing `_build_evidence_snapshot` / `_extract_region_key` helpers.

2. **Before/after z_goal capture** -- `_z_goal_before` captured immediately
   before `agent.run_sleep_cycle()`, `_z_goal_after` immediately after.
   Four metrics written into the `merged` return dict:
   `post_sleep_z_goal_before`, `post_sleep_z_goal_after`,
   `post_sleep_z_goal_retention` (ratio, or -1.0 when before <= 1e-8),
   `replay_diversity_index` (len(replayed_regions)/n_draws, or -1.0 when
   no routed draws occurred this cycle).

`replay_diversity_index` computes from `replayed_regions` (already
collected upstream for MECH-284 partial-decay) and `sws_routed_draws`
(already computed for MECH-272 anchor-channel). Zero new data structures.

Non-invasive by construction: `_safe_z_goal_norm` only reads; nothing
in the hot path calls it during waking steps; the four new dict keys
do not conflict with any pre-existing metric name. Sleep cycle semantics
and all existing metrics are bit-identical.

Contract tests: `ree-v3/tests/contracts/test_z_goal_retention_gap8.py`
(7 tests: C1 sentinel when no goal_state, C2 correct norm from seeded
_z_goal, C3 all four keys always present, C4 -1.0 sentinels on no-goal/
no-sampler path, C5 retention ~1.0 when seeded (sleep preserves z_goal),
C6 replay_diversity_index in [0,1] when draws occur, C7 pre-GAP-8 SWS
keys still present) -- **7/7 PASS**. Full regression **467/467**
contracts + preflight green.

Validation experiment **V3-EXQ-585** queued (`experiment_purpose=diagnostic`,
`claim_ids=[]`). Two-arm (ARM_0 no-goal / ARM_1 goal-seeded) x 3 seeds.
Dry-run smoke 4/4 criteria PASS: C1 ARM_0 before/after/retention all -1.0,
C2 ARM_0 replay_div -1.0, C3 ARM_1 retention=1.0 > 0.95, C4 ARM_1
before=0.6 > 0.1. `claims.yaml` NOT modified: GAP-8 alone does not
resolve any `v3_pending` (DEV-NEED-007/008 governed by the full infant
pipeline + EXQ-ISEF behavioural runs). Phase-2 telemetry: all of GAP-5,
GAP-6, GAP-7, GAP-8 now done.

### 2026-05-17 -- GAP-9 implemented (4-phase infant curriculum scheduler)

GAP-9 is an experiment-harness helper (NOT a ree_core substrate
scheduler), following the commitment_closure GAP-11 O-1 precedent.
Implemented as `ree-v3/experiments/infant_curriculum.py`:
`InfantCurriculumScheduler` class.

**Design:** phase-only-advance state machine with episode-count hard
minimums (phase 0->1: ep >= 100; 1->2: ep >= 500; 2->3: ep >= 2000) and
optional telemetry gates (H_pos threshold 0.70*ln(grid_cells) for 0->1;
z_goal.norm() >= 0.30 AND benefit_contacts_window >= 5 for 1->2;
residue_coverage_pct >= 0.15 for 2->3). When a metric is None, hard
episode count governs (fallback). Phases never retreat.

**`env_kwargs(phase)`** returns CausalGridWorldV2 constructor kwargs:
- Phase 0: all infant features OFF.
- Phase 1: `harm_gradient_enabled=True, harm_gradient_scale=0.15,
  transient_benefit_enabled=True`.
- Phase 2+: adds `microhabitat_enabled=True, harm_gradient_scale=0.30`.

**`config_overrides(phase)`** returns agent config override dict:
- `novelty_bonus_weight`: 0.5 / 0.7 / 0.5 / 0.5 (phases 0-3).
- `residue_scale_factor`: 0.0 / 0.05 / 0.10 / 0.15 (strictly increasing).
- `offline_integration_frequency`: 10 / 20 / 50 / 100 (strictly increasing).

**Contract tests:** `ree-v3/tests/contracts/test_infant_curriculum_gap9.py`
(16 tests: C1 fresh start, C2 hard transitions x3, C3 H_pos gate blocks
+ ep-min, C4 z_goal gate blocks, C5 no retreat, C6 env_kwargs x4 phases,
C7 config_overrides ordering, C8 phase_changed flag, C9 full walk + summary,
C10 benefit_contacts window gate) -- **16/16 PASS**. Full regression
**483/483** contracts + preflight green.

**Validation experiment V3-EXQ-586** queued (`experiment_purpose=diagnostic`,
`claim_ids=[]`). Two arms x 3 seeds: ARM_0 hard-count only (transitions at
100/500/2000); ARM_1 synthetic-telemetry gated (delayed transitions at
150/650/2000 -- demonstrates H_pos gate delays 0->1, z_goal gate delays
1->2). C2 env constructor per phase + C3 feature flags + C4 config
ordering also checked. Dry-run **5/5 criteria PASS**: C0 ARM_0 transitions
correct, C1 ARM_1 delayed transitions correct, C2 env constructor OK,
C3 feature flags correct, C4 config ordering correct. `claims.yaml` NOT
modified (GAP-9 alone does not resolve any `v3_pending`; DEV-NEED-008 and
ARC-046 governed by the full infant pipeline + EXQ-ISEF validation).
Phase 3 curriculum scheduler: GAP-9 done; GAP-10..14 (EXQ-ISEF experiments)
remain open.
