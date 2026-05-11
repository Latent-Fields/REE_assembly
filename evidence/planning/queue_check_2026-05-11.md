# Queue Check -- 2026-05-11 (afternoon ree-diagnose-queue scheduled session, Step 2)

**Session:** diagnose-errors-staging-2026-05-11T1421Z (Step 2: /queue-experiment in automated mode)
**Generated UTC:** 2026-05-11T14:35:00Z

**Outcome:** NO QUEUE ACTION TAKEN. Queue is currently empty. The 14 `status: "proposed"` items at `priority: high` in the proposals index split into three categories, none of which are "queue immediately" candidates for an automated run.

---

## Context

- `ree-v3/experiment_queue.json` currently holds **0 pending items**.
- `experiment_proposals_index.v1.json`: 287 items total, 151 with `status: "proposed"` (14 high, 135 medium, 2 low).
- All 14 high-priority "proposed" items were inspected.

## Categories of the 14 high-priority proposed items

### Category A: Already executed (12 / 14) -- proposals-status hygiene gap

These have scripts on disk AND a matching queue_id (or successor letter) in
`runner_status.json` completed list. The experiment ran; the proposal index
just wasn't updated.

| Proposal ID | Backlog ID | Claim | Suggested type | Successor / queue_id done |
|-------------|------------|-------|----------------|---------------------------|
| EXP-0062 | EVB-0188 | SD-047 | v3_exq_509_sd047_multi_source_substrate_readiness | V3-EXQ-509 PASS |
| EXP-0039 | EVB-0189 | SD-049 | v3_exq_514f_sd049_phase_2_reef_behavioural_validation | V3-EXQ-514f executed |
| EXP-0025 | EVB-0192 | MECH-302 | v3_exq_517_mech302_relief_completion_discriminative | V3-EXQ-517 done |
| EXP-0074 | EVB-0196 | MECH-230 | v3_exq_328b_mech112_zgoal_structured_latent | V3-EXQ-328b done |
| EXP-0075 | EVB-0197 | MECH-229 | v3_exq_326a_wanting_gradient_nav_fix | V3-EXQ-326a done |
| EXP-0061 | EVB-0198 | MECH-304 | v3_exq_519_sd051_conditioned_safety_store_readiness | V3-EXQ-519 done |
| EXP-0036 | EVB-0214 | MECH-204 | v3_exq_541_mech204_precision_recalibration_consumer | V3-EXQ-541 done |
| EXP-0082 | EVB-0234 | MECH-094 | v3_exq_465_mech267_intrusive_simulation_filtering | V3-EXQ-465 done |
| EXP-0071 | EVB-0061 | SD-011 | v3_exq_106_harm_obs_a_temporal_persistence | V3-EXQ-106a (successor) done |
| EXP-0078 | EVB-0062 | MECH-104 | v3_exq_126_mech104_surprise_gate_pair | V3-EXQ-126 done |
| EXP-0058 | EVB-0156 | MECH-166 | v3_exq_436_sd017_context_cond_harm_thresh | V3-EXQ-436 done |
| EXP-0045 | EVB-0161 | ARC-045 | v3_exq_436_sd017_context_cond_harm_thresh | V3-EXQ-436 (shared) done |

**Right action for these:** mark `status: "executed"` in
`experiment_proposals.v1.json` (find by `backlog_id`) and rebuild
the index. Out of scope for `/queue-experiment` automated mode -- this is a
governance / housekeeping task. The indexer's persistence block will carry
the status forward across future governance runs (per
`build_experiment_indexes.py` status-persistence comment).

### Category B: Needs design pass before script (2 / 14)

These have placeholder `suggested_experiment_type` strings indicating a
script has not yet been designed. Per the queue-experiment skill, a script
is required to queue, and writing a new design exceeds the scope of an
automated scheduled run.

#### EXP-0068 / EVB-0065 -- claim_probe_arc_018 (ARC-018)

- Objective: "Run a discriminative support-vs-ablation pair for ARC-018
  with matched seeds and pre-registered thresholds."
- Suggested type: `claim_probe_arc_018` (placeholder; not a script name).
- Claim ARC-018 status in `claims.yaml`: `status: active`,
  `lifecycle_stage: adjudicated`, `adjudication_outcome: retain_ree`,
  `v3_pending: false`. The 2026-03-15 reframe note moved viability mapping
  from E1 to hippocampal action-object geometry; the discriminative
  ablation has to be designed against that reframe.
- `why_now`: `active_conflict` -- some evidence is conflicting per the
  index entry, but no record of which specific runs.
- Substrate readiness: SD-004 (E2 action objects + HippocampalModule
  navigation) is implemented; hippocampal `propose_trajectories` is the
  natural target for ablation. But there is no canonical "rollout viability
  mapping" probe -- the experiment design space is open and the script
  would need to specify (i) what evidence COUNTS as the viability map
  being constructed vs. absent, (ii) which ablation actually disables
  the mechanism without breaking other paths.
- Recommendation: design pass needed before scripting. A 60-90min Mac
  experiment, but the design is the load-bearing part.

#### EXP-0174 -- v3_exq_NNN_env_complexity_gate (SD-016)

- Objective: "Test whether V3's current or enriched environments produce
  enough world-state information for downstream attribution, SD-016 cue
  retrieval, and sleep/self-model aggregation to operate. This is an
  environment-readiness gate, not direct claim-confidence evidence. It
  follows V3-EXQ-418f/g/h, which showed SD-016 substrate mechanics can
  work while z_world remains too near-constant to drive behaviour."
- Suggested type: `v3_exq_NNN_env_complexity_gate` (placeholder; not a
  script name).
- Claim SD-016 status in `claims.yaml`: `status: implemented`.
  `implementation_phase: v3`. CLAUDE.md notes that `cue_terrain_proj` is
  trained-and-working but `cue_action_proj` is UNRESOLVED pending EXP-0155
  (an open diagnostic about why the supervised MSE doesn't make
  action_bias_divergence non-zero).
- This proposal is genuinely about a Level-1 measurement: how much
  z_world variance does the V3 env provide, and is that enough for
  downstream cue retrieval / attribution / aggregation? The 418f/g/h
  cluster already showed z_world is too low-variance in the default
  CausalGridWorldV2 config -- this proposal asks for a structured
  comparison across env variants (SD-023 landmarks; SD-047 multi-source
  dynamics; SD-054 reef; SD-049 multi-resource heterogeneity).
- Design open questions: which env variants to compare, what z_world
  variance / entropy metrics to measure, what counts as "enough" (the
  gate criterion).
- Substrate readiness: SD-023 / SD-047 / SD-049 / SD-054 all
  IMPLEMENTED per CLAUDE.md (2026-04-09 / 2026-05-03 / 2026-05-03 /
  2026-05-04 respectively). All substrate features are in place.
- Recommendation: ~90min experiment once designed, but the design pass
  (which env variants to sweep, which metrics to record, what the gate
  criterion is) is again the load-bearing part. Could be a good follow-on
  to the cluster of substrate-readiness diagnostics that just landed.

### Category C: Duplicate / structural index quirks (none in this run)

(EXP-0174 actually appears TWICE in the index -- once as `status: executed`
for claim INV-046, once as `status: proposed` for claim SD-016. The
index entry reuses the proposal_id `EXP-0174` for two different proposals;
this is an indexer / proposals-file structural quirk worth surfacing
to governance.)

## Why no queue action was taken

Automated mode is supposed to queue ONE highest-priority substrate-ready
candidate that has a script ready to run. The intersection of (high
priority AND substrate-ready AND has-script AND not-already-executed) is
EMPTY at the moment of this check:

- 12 / 14 high-priority items already executed (Cat A).
- 2 / 14 lack scripts AND lack detailed designs (Cat B).

Writing a new experiment design + script for either Category B item is
substantive design work that should not run unattended in an automated
scheduled session.

## Recommendations for the user

1. **Mark the 12 Category A proposals executed.** Find each in
   `experiment_proposals.v1.json` by `backlog_id`, set
   `status: "executed"` + `executed_by` + `executed_queue_id`, and re-run
   `python evidence/experiments/scripts/build_experiment_indexes.py`
   from `REE_assembly/`. After this, the high-priority "proposed" count
   in the index drops from 14 to 2, accurately reflecting reality.

2. **Schedule a design session for EXP-0174 / SD-016 env_complexity_gate.**
   This is the more concrete of the two Category B items -- the
   substrate landscape (SD-023 / SD-047 / SD-049 / SD-054) is mature
   enough that a 2-3-arm env-variance sweep with z_world entropy / variance
   metrics is well-defined. The result feeds directly into the SD-016
   substrate-readiness story by quantifying what the cue_terrain_proj
   path has to work with.

3. **Consider whether EXP-0068 / ARC-018 claim_probe is still the right
   way to test ARC-018.** The proposal is generated from a generic
   "discriminative support-vs-ablation pair" template; given the 2026-03-15
   reframe (viability map lives in hippocampal action-object geometry,
   not E1 prediction error), it may be that the natural ARC-018 test
   is now embedded in MECH-163-class experiments (dual-system
   hippocampal planning, e.g. V3-EXQ-495a in the diagnose-staging
   queue) rather than a standalone probe.

4. **Investigate the EXP-0174 duplicate proposal_id.** Two distinct
   proposals (INV-046 attribution failure reframe, SD-016 env complexity
   gate) share `proposal_id: EXP-0174` in the index. This is likely an
   indexer key-collision; the underlying `experiment_proposals.v1.json`
   may be the cleaner source. Worth raising at the next governance pass.

## Related parallel actions (from Step 1 diagnose-errors staging)

The same scheduled session also identified 2 Mac-pinned reruns awaiting
confirmation (V3-EXQ-495a, V3-EXQ-538a) in
`REE_assembly/evidence/planning/diagnose_staging.json`. If those are
approved by the user, the queue will be re-populated from that path
before any of the Category B / Cat C design work above lands.
