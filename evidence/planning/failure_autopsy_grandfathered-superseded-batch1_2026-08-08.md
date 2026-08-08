# Failure Autopsy (cluster, closure pass): Grandfathered legacy FAILs already marked `superseded` (73 runs)

**Generated:** 2026-08-08T17:10:36Z
**Scope:** cluster (73 runs, formalization/closure pass)
**Status:** confirmed (Step 8 interactive gate: user confirmed governance-note-only)

## Context

Part of working down the 547-run "grandfathered" legacy-FAIL backlog (`REE_assembly/evidence/experiments/fail_autopsy_grandfather.json`, seeded 2026-08-08) -- claim-tagged FAILs marked `reviewed` in `review_tracker.json` but never formally autopsied. All 480 V3-suffixed grandfathered runs date 2026-03-18 to 2026-06-21, entirely pre-MECH-457 (first real action-learning substrate, landed 2026-07-12). This batch covers the 73 runs whose manifest already carries `evidence_direction: superseded` -- the REE_assembly indexer has already determined these are inactive evidence, excluded from `claim_evidence.v1.json` scoring.

**This is a formalization pass, not fresh science.** The job was to (a) confirm each supersession is real and reflected in current `claims.yaml`, (b) do a lightweight four-layer read reusing the manifest's own `degeneracy_reason`/`interpretation` fields, and (c) flag any discrepancy. All 73 targets located (8 flat, 65 pack-style manifests); all confirmed `dry_run: false` (including the two `..._dry_...` V3-EXQ-431 runs, checked explicitly -- "_dry" reflects an exploratory short config, not a `--dry-run` flag).

## Recurring failure shapes (all pre-MECH-457, all correctly excluded from scoring already)

- **Runner-regex-bug replay** (~18 runs): a 2026-03-27..03-30 runner bug mis-parsed "Done. Outcome: PASS/FAIL" as UNKNOWN and silently re-ran completed experiments (fixed commit `071f1fc`).
- **Byte-identical duplicate emissions** (~14 runs): same run emitted multiple times by the runner minutes apart, no intervening script commit.
- **2x-substrate-tick / multi-sense confound** (v3_exq_124, v3_exq_143, v3_exq_490c/f): `sense()` or `env.reset()` called extra times inside the eval/training inner loop, decoupling the two arms' substrate dynamics from the manipulation under test.
- **Metric/wiring bugs invalidating an otherwise-clean run** (v3_exq_096, 099, 106, 187, 231, 258/258a, 266/266a, 326, 397/397c, 543b, 680): wrong stats key, unset kwarg, TypeError swallowed by a bare `except`, wrong eval method, sign-inverted metric, or an optimizer that never touched the shared encoder.
- **Pre-implementation claims** (v3_exq_127 sleep, v3_exq_128/134 multimodal): claim genuinely untestable on the V3 substrate at the time -- correctly excluded rather than weighed.

## Per-target disposition table

All 73 runs confirmed clean (real successor exists and is verified present on disk, or claims.yaml independently corroborates the supersession) except the 2 discrepancies noted below. `epistemic_category: measurement_test_design_defect`, `evidence_direction: superseded`, `routing: governance-note-only` for all rows.

| run_id (short) | claim_ids | superseded_by / basis | note |
|---|---|---|---|
| 038 (×5 emissions, 03-19..04-13) | ARC-016, MECH-093 | v3_exq_018b (relative-threshold, 2026-07-25 rescore) | absolute-threshold-era precision sweep |
| 018 (03-20) | ARC-016 | v3_exq_018b | absolute-threshold config |
| 059 (03-20) | ARC-016, MECH-090 | v3_exq_060 (committed-BetaGate PASS) | fixed-threshold BetaGate precursor |
| 046 (03-23) | ARC-007, SD-004 | v3_exq_046 (later same day) | byte-identical runner re-emission, 246.5min later |
| 047g (03-23) | SD-005 | v3_exq_047g (later same day) | identical signature, 64.4min later |
| 049d (03-21) | MECH-090 | v3_exq_049d (later same day) | identical signature, 5.5min later |
| 051c (03-30) | Q-007 | v3_exq_051c (later) | runner-regex-bug replay of an older legitimate run |
| 054 (03-20) | MECH-072 | v3_exq_054 (later same day) | identical signature, 576.2min later |
| 071d (×2, 04-01) | ARC-024, MECH-071, SD-003 | v3_exq_071d_...20260328T181225Z | runner-regex-bug replay |
| 072b (04-02) | Q-021 | v3_exq_072b_...20260328T135541Z | runner-regex-bug replay |
| 073b (04-02) | MECH-111 | v3_exq_073b_...20260328T145319Z | runner-regex-bug replay |
| 074c (03-27) | MECH-112, MECH-117 | v3_exq_074d | resource_respawn bug: 0 resource visits in all conditions |
| 074e (03-28) | MECH-112, MECH-117 | v3_exq_074e_...20260327T070014Z | runner-regex-bug replay |
| 075d (04-02) | MECH-113 | v3_exq_075d_...20260328T155739Z | runner-regex-bug replay |
| 076d (03-27) | ARC-032, MECH-116 | v3_exq_076d_...20260327T065549Z | identical signature, 2.1min later |
| 076e (×2, 03-28/04-04) | ARC-032, MECH-116 | v3_exq_076e_...20260327T143027Z; v3_exq_076f | replay + E1Config.goal_dim never set (fixed in 076f) |
| 084d (×2, 03-29/04-02) | MECH-118, MECH-119, Q-022 | v3_exq_084d_...20260328T160649Z | runner-regex-bug replay |
| 085 (03-23) | INV-034, MECH-071 | v3_exq_085_...20260323T185618Z | dedup + non_contributory for MECH-071 (goal-nav != harm-calib); see discrepancy #1 |
| 096 (03-25) | ARC-007/016, MECH-089/090/093/094, SD-005/006 | successor 096a (PASS) | 2 implementation bugs (wrong stats key, wrong eval method) invalidated C5 |
| 099 (03-26) | MECH-098 | v3_exq_099a (FAIL) | collection filter bug: only 8 of 2000+ locomotion steps collected |
| 104, 104b (×2), 105 (03-28) | MECH-135 | superseded by EXQ-103/108 PASS | pre-diagnostic artifact: untrained agent, empty metrics |
| 106 (×3, 03-28) | SD-011 | successor 106a (PASS) | pre-fix: harm_obs_a_ema reset bug in env.reset() |
| 124 (03-28) | MECH-033 | -- | env.reset() inside inner loop corrupted E2 world_forward warmup training |
| 125 (03-29) | ARC-029 | v3_exq_125_...20260329T010106Z | runner-regex-bug replay |
| 126 (04-20) | MECH-104 | 2026-04-21 rerun (6/6 PASS) | duplicate-queue-ID issue |
| 127 (03-29) | MECH-030 | -- | sleep not implemented in V3; post-training-phase sim doesn't test claim |
| 128 (03-29) | MECH-103 | -- | no multimodal (auditory) input in V3; artificial channel not representative |
| 134 (03-29) | MECH-103 | -- | no multimodal (somatosensory) input in V3 |
| 143 (03-29) | MECH-118 | -- | eval loop calls sense() 2x in ON arm only -- substrate-rate confound |
| 145 (03-29) | SD-003, SD-007, SD-008 | v3_exq_145_...20260329T215806Z | identical signature, 873min later |
| 166a (03-29) | ARC-033, SD-003, SD-011 | v3_exq_166e (PASS) | C2 structurally impossible in obs-space |
| 182 (03-31) | ARC-041, MECH-150 | v3_exq_182a | wrong experiment script ran (queue entry later corrected) |
| 187 (04-01) | ARC-042, MECH-153 | v3_exq_187a | context_memory.write() never called during training |
| 231 (04-04) | MECH-106 | v3_exq_231a | PERSISTENT/REACTIVE conditions produced identical commit values |
| 232 (×5, 04-04) | ARC-026 | v3_exq_232_...20260405T091846Z | 1 of 5 byte-identical emissions of a ZeroDivisionError-truncated run (20/1500 eps) |
| 238 (04-04) | MECH-112, SD-012 | v3_exq_238_20260404T185519Z | identical signature, 1.9min later |
| 258, 258a (×3, 04-xx) | MECH-205 | v3_exq_258b | _rbf_layer attr bug + pe_ema_alpha too fast; pe_surprise_threshold ~53x too high |
| 266, 266a (×3, 04-10/11) | Q-020 | v3_exq_266a supersedes 266 | action-object round-trip selection defect: argmax pinned to constant class |
| 326 (04-13) | MECH-216, SD-012, SD-015 | v3_exq_326a | use_resource_encoder kwarg never wired + pre-step EMA seeding bug |
| 397, 397c (×3, 04-19/21) | ARC-007, SD-004 | successor 397d | hippo_quality_gap metric confounded in resource-hazard-colocated envs |
| 431 (×2, "_dry_", 04-17) | SD-003, SD-013 | 20260417T152531Z (full run) | near-zero event counts (n_agent=0); exploratory, replaced by full run -- NOT a `--dry-run` smoke (checked explicitly) |
| 433c (04-23) | MECH-256, SD-029 | 433d/433e | non-canonical `inconclusive_insufficient_events` direction mis-normalized by indexer |
| 490c (04-29) | Q-040 | -- | update_z_goal TypeError silently swallowed by bare except -> z_goal pinned at 0 |
| 490f (05-07) | Q-040 | -- | same TypeError-swallow bug, cohort-wide |
| 514 (05-04) | MECH-229, MECH-230, SD-015, SD-049 | failure_autopsy_V3-EXQ-538a | pre-enrichment starved config re-run; see discrepancy #2 |
| 543b (05-10) | ARC-062, MECH-309, SD-029 | v3_exq_543c | candidate_features built from initial_z_world (uniform softmax by arithmetic) |
| 623 (06-01) | MECH-104 | v3_exq_623_...20260601T152050Z | incomplete/empty early run; canonical full run PASSes |
| 672 (06-12) | MECH-057b | v3_exq_672a | user-adjudicated supersession per EXQ policy |
| 680 (06-14) | MECH-423 | v3_exq_680a | P0 optimizer held only head params -> encoder never trained -> arms identical by construction |

## Discrepancy findings (2, both benign -- no action beyond a note)

1. **V3-EXQ-085 (INV-034/MECH-071):** manifest's top-level `evidence_direction` is `superseded`, but `claim_evidence.v1.json` carries per-claim directions `mixed`(INV-034)/`non_contributory`(MECH-071), both `scoring_excluded: invalid_run` rather than `superseded`. Not a real discrepancy -- both readings converge on "excluded from scoring," reflecting two independently-true reasons (duplicate emission + wrong-layer test, per `evidence/planning/exq085_mech071_disposition_2026-06-02.md`). No action.
2. **V3-EXQ-514:** manifest's `evidence_direction_note` is `null` (unlike every other row), though `claims.yaml`'s note (via `failure_autopsy_V3-EXQ-538a`) independently and thoroughly corroborates the supersession. Recommend governance backfill the manifest note from the existing claims.yaml text for corpus consistency -- not a scoring or claims.yaml problem.

## Recommended epistemic_category / evidence_direction / routing

All 73: `epistemic_category: measurement_test_design_defect`, `evidence_direction: superseded` (confirms existing state), `routing: governance-note-only`. No claims.yaml edits, no re-queues, no substrate work indicated by this batch -- this closure pass exists purely to give governance a formal artifact citing what was already correctly determined.

## Learning extracted

- The early V3 era (2026-03..04) carried a real runner bug (regex mis-parse of completion status) that produced a large fraction of this batch's "duplicate" signature -- already fixed (`071f1fc`), historical only.
- Several genuine implementation bugs (wiring, metric-sign, kwarg-not-passed) were caught and fixed within the same EXQ lineage in every case -- the corpus's own iteration discipline worked as intended even before this formal autopsy net existed.
- No case in this batch pointed to a missing or non-existent successor run; all named successors verified present on disk.
