# Failure Autopsy: V3-EXQ-906a + V3-EXQ-894b

**Generated:** 2026-08-09T08:52:25Z
**Status:** confirmed (interactive gate completed with user)
**Scope:** two independent single targets (no shared shape -- reported together for session efficiency, not a cluster)

---

## Target 1: V3-EXQ-906a -- Full-Stack Observational Fishtank Showcase

`v3_exq_906a_full_stack_observational_fishtank_20260809T081031Z_v3` -- claim_ids=[] (claim-free diagnostic showcase, does not weight governance) -- FAIL, self-route `full_stack_observational_showcase_degenerate`, precondition `ecology_survivable` unmet (measured 25.375 mean realized segment steps vs 59.6 threshold).

### Facts

906a is a lettered bug-fix of V3-EXQ-906, whose episodes died at ~15 realized steps against a nominal 600-step (actually 500-step-capped) budget. The driver diagnosed and fixed two health-drain bugs before this run: `contamination_spread` (default 0.5, every revisited cell accrues contamination) set to 0.0, and `hazard_harm` (direct hazard-cell contact damage, default 0.5) relaxed to 0.05. An informal dev-time probe of both fixes together showed mean segment length rising from 14.0 to 335.9 steps (24x). The scored run, however, only reached 25.375 mean steps -- a ~70% improvement over 906, nowhere near the probe's figure -- with all 8/8 eval segments ending `health_depleted` and 0/8 reaching the step cap.

The user directly observed the fishtank_viz behaviour and reported the fish's health draining very fast without hitting a hazard, and that a fish should ordinarily survive a long while between food/goal events. This observation, combined with a source read of `causal_grid_world.py`, resolved the discrepancy between the probe and the scored run.

### Root cause (code-confirmed, not speculative)

`causal_grid_world.py` has **three independent** health-drain paths:

1. Direct hazard-cell contact (`hazard_harm`) -- fixed by this driver (0.5 -> 0.05).
2. Contamination accrual (`contamination_spread`) -- fixed by this driver (0.5 -> 0.0).
3. **Proximity-approach damage** (lines ~2445-2469): `elif self.use_proxy_fields and transition_type == "none": ... harm_signal = -proximity_harm_scale * hazard_field[x,y] ... agent_health -= abs(harm_signal)`. This fires on **any step the agent is merely near a hazard's field, with no contact at all**, gated only by `proximity_approach_threshold` (default 0.15). The field itself decays slowly (`hazard_field_decay` default 0.5; `hazard_field[i,j] += 1.0/(1+dist*decay)`), so the 0.15 threshold is crossed at roughly **11 cells' distance** from a hazard -- effectively grid-wide, not a close-range cue.

The driver's `EVAL_ENV_EXTRA_KWARGS` never touched `proximity_harm_scale`, `proximity_approach_threshold`, or `hazard_field_decay` -- only channels (1) and (2). Channel (3) alone is sufficient to explain the observed shortfall: 8/8 health-depleted terminations against only 1 external_hazard event and 0 limb_damage events is inconsistent with discrete contact and consistent with ambient proximity drain, matching the user's direct observation exactly.

### Recording gaps found

`validate_recording.py` flags this manifest as missing `elapsed_seconds`, `config`, and `seeds` from the always-core. Separately, the driver's own docstring promises a companion `_episode_log.json` ("this run's own `_episode_log.json` already carries everything needed [for a future autopsy]") -- **no such file exists on disk** for this run. Both should be fixed in the next iteration, not just the survivability issue.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | claim-free showcase |
| Biological reference | n/a | showcase legibility, not a mechanism under test |
| Prerequisites | present | SD-017/sleep loop and all dependent modules coupled and firing |
| Implementation | partial | fix addressed 2 of 3 independent health-drain channels |
| Environment | inadequate for showcase purpose | proximity radius far broader than a near-miss cue; too few safe cells |
| Measurement | under-instrumented | elapsed_seconds/config/seeds missing; promised episode_log never written |
| Integration | coupled, working | harm-pathway training, z_goal activation, channel variation all functioning |
| Scale | single seed by design | claim-free qualitative showcase, not a powered study |

### User design guidance for the redesign (V3-EXQ-906b)

1. Proximity drain should be a genuinely **close-range** warning cue, not a broad ambient field -- narrow the radius (raise `proximity_approach_threshold` and/or steepen `hazard_field_decay`) and make the per-step drain itself smaller (`proximity_harm_scale` further reduced), on top of the already-applied `hazard_harm`/`contamination_spread` relaxation.
2. The layout should carry plenty of safe space, consistent with (1).
3. Each segment's agent should **spawn on a safe cell**, not merely somewhere in a hazard-sparse layout -- an unsafe spawn risks damage before any action is taken, which is not a learning signal and would reintroduce an early-death floor independent of the radius fix.
4. The overall layout density this driver family inherited from 906 (`num_hazards` etc.) may itself be too hazard-dense for this stage of substrate development. The redesign should provide **significant safe areas and safe traversable paths** from spawn to goals/resources -- a dynamic hazard's movement transiently occluding part of a path is fine (that's a real perturbation worth having), but a path being permanently blocked or absent is not.
5. The fish should be able to **"smell" a hazard's direction before harm begins**, with enough of a gap between sensing and harm for the agent to actually learn to localize and avoid it.

### Structural finding sharpening point 5 (code-confirmed)

Verified against source: the agent's hazard-field **sensory** observation is a hardcoded 5x5 local patch centered on the agent (`causal_grid_world.py:3655-3656`, `range(-2,3)` -- radius **2 cells**), fed into `world_parts` as part of the actual observation the agent receives. The proximity-**harm**-onset radius (from `proximity_approach_threshold=0.15` against `hazard_field_decay=0.5`) is roughly **11 cells** for a single hazard source -- far larger than the sensory window.

This is exactly backwards from the "smell before harm" structure the user is asking for: the agent currently takes unseeable ambient proximity damage across roughly cells 3-11 out (no signal at all in its 5x5 window that far away), and only gains any sensory signal once already deep inside a zone well past where harm has been accruing. **The fix is a relationship between two radii, not a single-knob shrink**: the sensing radius needs to exceed the harm-onset radius with a genuine gap between them (e.g. sensing effective out to ~3-4 cells via the existing window mechanism, harm onset tightened to ~1-2 cells) -- not just uniformly reducing `proximity_harm_scale` as point 1 above describes in isolation. Both should be specified together in the V3-EXQ-906b redesign.

### Secondary finding: unbounded residue-valence accumulator

The survivability fix's own side effect -- sustained continuous exposure via this driver's CONTINUITY REDESIGN -- made a previously-invisible substrate limitation newly observable: `RBFLayer.update_valence()` in `ree_core/residue/field.py` is an unclamped `+=` with no decay, fed every step MECH-307 split-surprise crosses threshold. With only 32 RBF centers, a long-lived agent revisiting the same regions drives the same centers' valence unboundedly -- `z_world_norm` measured ~150-320 and excite/dread in the hundreds here, vs ~0.5-0.7 at smoke scale. No scored claim currently exercises long-horizon continuity, so nothing is corrupted yet, but registering it now (severity: degrading) means it's tracked before a claim-bearing experiment trips over it.

### Routing (user-confirmed)

- **Primary:** `/queue-experiment` V3-EXQ-906b -- same-question redesign relaxing `proximity_harm_scale`/`proximity_approach_threshold`/`hazard_field_decay` per the user's guidance above, safe spawn placement, and stamping the missing recording-core fields + confirming the episode_log write path actually fires.
- **Secondary:** `recommended_substrate_queue_entry` (action: create, SD-RESIDUE-VALENCE-BOUND, severity: degrading) for the unbounded residue accumulator, independent of the showcase's own fix.

---

## Target 2: V3-EXQ-894b -- MECH-074d BLA Trainable Attribution Head (post-substrate retest)

`v3_exq_894b_mech074d_bla_trainable_attribution_head_20260809T081623Z_v3` -- claim_ids=[MECH-074d] -- FAIL/weakens, self-route `mech074d_trainable_head_does_not_recover_attribution_gate`.

### Facts

This is the post-substrate retest routed by the confirmed `failure_autopsy_V3-EXQ-894a_2026-08-08`, which diagnosed MECH-074d's non-trainable threshold-rule attribution as a `competence_implementation_gap` and routed `/implement-substrate` (SD-035 amend: build the deferred learnable attribution head). That build landed 2026-08-09 (`ree-v3 25e04cf5f5`, `d2c8d6f2f0`) as `BLAAttributionHead`, and `substrate_queue.json`'s SD-035 entry recorded the prior failure_record item as `built_pending_retest` pointing at this queue_id.

4 arms x 3 seeds (42/43/45), sigma held fixed at 1.0 (894a already closed the sigma-sweep question). `ARM_REMAP_OFF` (control) and `ARM_HEAD_FIXED` (within-run replication of 894a) both behaved as expected -- `ARM_HEAD_FIXED` reproduced 894a's sigma=1.0 signature (C1 1/3, C2 1/3), confirming this run is a valid comparison baseline (`fixed_replicates_894a=True`).

`ARM_HEAD_TRAINED` (914 optimiser updates) and `ARM_HEAD_TRAINED_LONG` (1998 updates, ~2x budget) both:
- **Recovered C1 (attribution_selectivity) fully**: 0/3 -> 3/3 seeds, mean mass_excess 0.085 (fixed) -> 0.575/0.635 (trained).
- **Did NOT recover C2 (context_differentiated_addressing)** -- the actual Moita 2004 dissociation this claim is about: stayed 0/3 seeds in both arms; jaccard_gap delta vs the fixed rule is -0.006 (short) / -0.025 (long) -- essentially flat to slightly *worse* with more training.
- Head-attention entropy **rose** with more training (0.456 -> 0.627), i.e. moved toward more diffuse, not more peaked.

Engagement checks (the instrument's own vacuity guards) all pass cleanly: `trainable_heads_trained_past_warmup`, `baseline_store_matched_across_arms`, `attr_mass_excess_varies_across_head_arms`, `dv_varies_across_arms`, `remap_fires_in_trained_arms` -- this is a genuine, non-degenerate, well-powered null on C2 specifically, not a vacuous or under-instrumented run.

### The substrate's own docstring predicts this exact shape

`ree_core/amygdala/attribution_head.py`, design decision #3 (written when the head was built, before this run): *"The MSE and entropy terms are in DELIBERATE tension, and that tension is what earns C2. The entropy penalty pushes `a` toward peaked (C1)... What rules that out is the MSE term... Keep entropy_weight small; a large value buys C1 at C2's expense and reproduces seed 43 [894a's context-blind-deterministic signature]."*

That is precisely what 894b measured: C1 recovered fully, C2 did not move, and the failure pattern (a consistently peaked-but-context-blind attribution) matches the named risk. This reframes the diagnosis: trainability alone was **not** the missing ingredient (H0 confirmed on the narrow "does a trainable head exist and differ from the fixed rule" question) -- the load-bearing open question is now the loss-term balance (`entropy_weight` relative to the variance-normalised MSE term), a tuning/calibration gap rather than an architecture-absence gap.

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | H1 (trainability recovers C1+C2) only partially holds |
| Biological reference | clear | Moita et al. 2004 |
| Prerequisites | present | SD-011, ARC-033, SD-035 all present and coupled |
| Implementation | complete | head exists, trains, is warm, differs measurably from the fixed rule |
| Environment | adequate | matched-baseline restore design carried over unchanged from 894a |
| Measurement | adequate | extensive engagement checks all pass; minor gap -- `entropy_weight`'s value itself not recorded in config |
| Integration | coupled but unstable on C2 specifically | C1/C2 dissociate exactly as the module's own docstring warned |
| Scale | adequate | 3 seeds x 2 training budgets rules out "needs more experience" cleanly |

### Granularity-debt recurrence check

Read via `granularity_debt_cluster.py MECH-074d` (targets whose own `claim_ids` name the claim, not a topical-neighbourhood grep): 3 targets now (894 intact, 894a weakened, 894b weakened). **Does not fire** -- the three autopsies show progressively *converging* diagnosis (dilution confound refuted at 894a -> trainability-alone refuted at 894b, loss-balance now implicated), not structurally different failure signatures. This reads as a claim being systematically narrowed toward its true bottleneck, not a coarse claim needing to be split.

### Re-derive brake check

Neither 894 nor 894a nor 894b read `substrate_ceiling` (all `competence_implementation_gap`/`standard`-family reads) -- per the R1-R3 counting convention, the brake only counts `substrate_ceiling` hits, so it **does not fire** here regardless of the 3-iteration count.

### Substrate_queue update

`resolves_prior_failure_record`: the existing SD-035 failure_record item (run_id `v3_exq_894a_...`, `resolved: "built_pending_retest"`) is marked **superseded** -- its target (a trainable head existing and clearing C1+C2) was met on the "build" half but not the "clears C2" half, so a narrower, more specific target (retuned entropy_weight/MSE balance) replaces it rather than closing it. A new failure_record entry is added naming that narrower target.

### Routing (user-confirmed)

`/implement-substrate` amend, SD-035, priority 1 (concrete, well-specified fix -- the module's own docstring already names the lever): retune `entropy_weight`/MSE balance, re-test on the same validated C1-C4 instrument, and this time stamp the swept `entropy_weight` value into the manifest config. **MECH-074d stays provisional/pending_retest_after_substrate, not demoted.**

---

## Session notes

**Blocking side-issue, not part of either target's diagnosis:** `TASK_CLAIMS.json` was found transiently corrupted at session start (commit `9901f0e7`, a concurrent-write race between two `task_claim.py` invocations on the shared main checkout). Another session had already repaired it (commit `fc3f4c20`, self-documented in its own `completion_note`) before this session needed to act -- confirmed the local working tree and `origin/master` are both valid (132 claims) and moved on. No action was required from this session beyond verification.

**Claims opened:** `mel-dose-sweep-inv-051-6b93d7-autopsy` (artifact resources) and `mel-dose-sweep-inv-051-6b93d7-autopsy-pause` (coordination-plane pause, `ree-v3/experiment_queue.json` excluded from the pause resource list -- owned by a concurrent session, `metaworker-chip-20260809-mech357-freeze-incompatible-hazard`, doing unrelated real queue work; not needed for this diagnosis).
