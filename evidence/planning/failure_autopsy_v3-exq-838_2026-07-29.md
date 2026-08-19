# Failure Autopsy — V3-EXQ-838 (Q-081, cross-stream recording)

- **Generated (UTC):** 2026-07-29T21:57:54Z
- **Scope:** single (third in the Q-081 bit-identical-arms chain: 824 → 824a → 838)
- **Status:** confirmed
- **Run:** `v3_exq_838_q081_cross_stream_recording_20260729T173347Z_v3`
- **Queue id:** V3-EXQ-838 · **Purpose:** evidence · **Claim:** Q-081
- **Outcome:** FAIL · self-route `substrate_not_ready_requeue` · `evidence_direction: unknown` · `non_degenerate: false`
- **Dry-run gate:** clean (`check_dry_run_citations.py` → 0 dry). **Recording:** `validate_recording.py` OK (always-core complete; note substrate drift below).

## 1. Facts (no interpretation)

Four arms — **INTACT** (off), **IEI_PERMUTE**, **CIRCULAR_SHIFT**, **SUPPRESS** — a temporal recording-stream ablation family, 5 seeds (0-4). DV = **RV(z_world, operating_mode)** (`primary_pair`), `secondary_reduce = norm`.

All four arms produced **bit-identical** rv values at every seed:

```
rv_intact       = [0.15587, 0.15615, 0.19986, 0.04763, 0.07453]
rv_iei_permute  = [0.15587, 0.15615, 0.19986, 0.04763, 0.07453]   (identical)
rv_circular_shift = [0.15587, 0.15615, 0.19986, 0.04763, 0.07453] (identical)
rv_suppress     = [0.15587, 0.15615, 0.19986, 0.04763, 0.07453]   (identical)
```

`mean_delta = 0.0`, `sd_delta = 0.0`. Self-route `substrate_not_ready_requeue`. **Failed criterion = precondition**: `arm_statistics_not_degenerately_bit_identical` measured 0.0 (0/5 seeds non-identical) vs threshold 1.0, and `yoked_arms_preserved_by_construction_fraction` measured 0.0 vs 0.6. The reach-check itself passed: `landmark_arm_behavioural_reach = 1.0`; `sufficient_valid_seeds_for_delta_sd = 5.0` (met). `validate_the_null` ruled out the artefactual statistic on all 5 seeds. `substrate_stable_across_run = false` is a *post-run* process-snapshot drift (recorded `ae03f0…` vs on-disk-now `1a52fd…`); `per_cell_hashes_disagree = false` and only one distinct cell hash — all cells ran against `ae03f0…`, so the drift does not invalidate the run.

## 2. The chain — this is the THIRD consecutive bit-identical result on (z_world, operating_mode)

| Run | Reach lever enabled | Manipulation family | Result | Prior verdict |
|---|---|---|---|---|
| **824** | `use_invalidation_trigger` | landmark removal (ON/REMOVED) | bit-identical, 5 seeds | measurement_test_design_defect (`failure_autopsy_V3-EXQ-824_2026-07-26`) — no reach to the pair |
| **824a** | + `use_anchor_sets=True` | landmark removal | reach-check *passes*, still bit-identical | measurement_test_design_defect (`failure_autopsy_2026-07-28-sweep`) — reach-check is a coarse blanket proxy; recommended substrate `Q081-REACH-CHECK-PAIR-SPECIFIC` ("add `use_per_region_vs=True` and re-verify") |
| **838** | + **`use_per_region_vs=True`** (script L274-275, both levers on) | temporal recording ablation (permute/shift/suppress) | **still bit-identical, 5 seeds** | this autopsy |

**838 is a decisive test of the 824a substrate hypothesis, and it refutes it.** The script was purpose-built for it (L34-42): "make_agent() enables BOTH use_anchor_sets=True (z_world reach) AND use_per_region_vs=True (operating_mode reach) … if RV STILL does not move even with use_per_region_vs on, 838 self-routes substrate_not_ready_requeue cleanly (informative, not a false negative)." The documented reach path — `apply_invalidation_broadcasts_to_regions → vs_rollout_gate → E3 → operating_mode`, gated on `use_per_region_vs` (agent.py:4686-4692) — **does not carry variance to operating_mode**. Enabling `use_per_region_vs=True` is now confirmed **insufficient** to move RV(z_world, operating_mode), and a *second, structurally different* manipulation family (temporal ablation, vs 824's spatial removal) hit the identical degeneracy on the identical pair.

## 3. Claim-layer map (Q-081)

Q-081's Outcome A (genuinely shared cross-stream organisation) vs Outcome B (wired-but-independent streams) **still cannot be adjudicated** — the DV never moved. Claim alignment **unclear**. The run is informative about the *test*, not the *claim*: it narrows the solution space (the `use_per_region_vs` reach approach is out) without bearing on A vs B.

## 4. Biological-reference triage

Q-081 is a cross-stream-organisation question (structure-destroying / surrogate-null paradigm, Chang/Nastase/Hasson 2022; Lancaster et al. 2018), not a single literature-grounded mechanism, so there is no missing-dependency biological signature to match. `is_formal_import: false`; divergence n/a. The defect is REE-internal (the measured pair is unreachable by the levers available), not a biology/architecture mismatch.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | Q-081 A vs B unadjudicable; DV never moved |
| Biological reference | n/a | cross-stream-organisation question, not one mechanism |
| Prerequisites | **partial** | z_world reach confirmed (anchor_sets); operating_mode's sensitivity now **refuted** even with `use_per_region_vs` on |
| Implementation | **partial** | the intended operating_mode reach path (agent.py:4686-4692) does not carry variance |
| Environment | adequate | 5 valid seeds, `z_goal_stream` active (active_frac 0.65, no writer defect) |
| Measurement | **misleading — measured pair appears unreachable** | core finding; bit-identical across two manipulation families |
| Integration | n/a | not reached |
| Scale | adequate | 5 valid seeds |

**Recommended `epistemic_category`: `standard`** (measurement/test-design defect, not substrate_ceiling — see GOV-CAT-1 fix note below; consistent with 824/824a's own diagnosis) · **`evidence_direction`: `non_contributory`**.

> **GOV-CAT-1 fix (2026-08-19):** this section originally recommended `measurement_test_design_defect`, which is not one of the eight valid `epistemic_category` enum values (`answer_state`, `derivational`, `governance_rule`, `out_of_domain`, `standard`, `substrate_ceiling`, `substrate_coherence`, `substrate_conditional`) — see `REE_assembly/scripts/validate_claims.py`. The `.json` artifact's `recommended_epistemic_category` is corrected to `standard` with the failure-mode diagnosis preserved verbatim in a new `recommended_epistemic_category_note` field (the diagnosis in this `.md` is otherwise unchanged). `standard` is behaviour-preserving with the settled convention (a measurement/precondition-unmet finding is not an assertion that Q-081's answer is gated on substrate work), matches `re_derive_brake.not_fired_reason` on this same target, and matches Q-081's own stored `epistemic_category: standard` in `claims.yaml` (set 2026-08-01, MEASURED-PAIR REFRAME, which retired this exact pair for the same reason).

## 6. Learning extracted

- **`use_per_region_vs=True` is refuted as the operating_mode reach fix.** The 824a substrate recommendation ("add use_per_region_vs and re-verify") has been tested end-to-end and does not move RV(z_world, operating_mode). The remaining reach hypotheses are unproven.
- **Two structurally different manipulation families (spatial landmark removal, temporal recording ablation) hit the identical degeneracy on the identical pair.** This is strong evidence that the *measured pair* is the problem, not any one manipulation — operating_mode may be architecturally not downstream of these manipulations at all.
- **The recommended `Q081-REACH-CHECK-PAIR-SPECIFIC` substrate entry was never written to `substrate_queue.json`** (governance has not swept the 824a sweep autopsy). 838 supplies fresh evidence that any such entry must be *empirical* (a cheap pre-flight reach probe), not a blanket flag-flip.
- **Cost discipline:** 838 ran ~83 min (`elapsed_seconds ≈ 4986`) to re-establish a bit-identical result. A cheap low-episode reach pre-flight would have surfaced the degeneracy in a fraction of that — the `arm_statistics_not_degenerately_bit_identical` precondition already exists; it should gate a pre-flight, not a full run.

## 7. Repair pathway — routing (user-confirmed)

Node class: **`complex (probe-gated)`** — the open question is a **discrimination**, not one already-named build, so a single sequential re-pose risks inheriting the confound and building the wrong substrate on a laundered artifact (GOV-FANOUT-1). The re-derive brake does **not** formally fire (R3 counts only `substrate_ceiling`), but this is the third same-shape failure and the last one tested the best-known fix — so **another blind full re-run of the same pair is refused.**

**Routing: `/queue-experiment` — a CHEAP low-episode reach pre-flight probe** that checks whether *any* available lever moves `rv_primary` on operating_mode BEFORE any full run, plus a **fanout_recommendation** discriminating:

- **H1 (build reach, axis=substrate):** operating_mode *can* be made reachable via a mechanism not yet tried (`use_per_region_vs` already refuted) → if the probe finds a working lever, route `/implement-substrate` to build it.
- **H2 (reframe pair, axis=measurement):** operating_mode is not downstream of these manipulations; RV(z_world, operating_mode) is the wrong DV → reframe Q-081 onto a confirmed-reachable pair.

The single cheap reach-scan discriminates the two (a lever that moves operating_mode → H1; none does → H2), so governance/`/queue-experiment` may run it as one pre-flight rather than two full legs. **Surface to governance:** create the `Q081-REACH-CHECK-PAIR-SPECIFIC` substrate need (as 824a recommended), now amended with 838's refutation of the `use_per_region_vs` fix and the requirement that reach be verified empirically per-pair before any full run.

### Draft `evidence_quality_note` (governance to write — do NOT write here)

> V3-EXQ-838 (2026-07-29) is Q-081's third consecutive bit-identical-arms result on RV(z_world, operating_mode) and is non_contributory: it enabled BOTH use_anchor_sets=True and use_per_region_vs=True (the exact 824a-recommended fix) plus a structurally different manipulation family (temporal recording ablation: IEI_PERMUTE/CIRCULAR_SHIFT/SUPPRESS), yet all four arms produced bit-identical rv at every one of 5 seeds (mean_delta=0.0, sd_delta=0.0) with the reach-check passing (landmark_arm_behavioural_reach=1.0) (failure_autopsy_v3-exq-838_2026-07-29). This refutes the 824a substrate hypothesis: use_per_region_vs=True does NOT grant operating_mode reach. Q-081 Outcome A vs B remains unadjudicable; the measured pair appears unreachable by every lever tried across 824/824a/838. Next step is a cheap empirical per-pair reach pre-flight, not another full run; a Q081-REACH-CHECK-PAIR-SPECIFIC substrate need should be created/tracked with this refutation recorded.

## 8. Granularity-debt / re-derive brake

- **Re-derive brake:** does **not** formally fire — R3 counts only `substrate_ceiling`; Q-081's chain is `measurement_test_design_defect` (824, 824a, 838). **But** this is the third same-shape (bit-identical) failure and the routing REFUSES another blind full re-run of the same pair — the spirit of the brake applied at the test-design level, same precedent the 824a autopsy flagged.
- **Granularity-debt trigger:** does **not** fire — Q-081's autopsy cluster is measurement/instrument debt (no target reads `claim_alignment: weakened`); it is a reachability defect, not a coarse claim needing decomposition.

## 9. Hypothesis-space ledger (Step 9b)

Creates registry question `q081-cross-stream-shared-organisation` (claims: Q-081), pre-registering the fan-out legs H1 (build-reach, alive) and H2 (reframe-pair, alive) and recording the refuted reach approach `H-reach-per-region-vs` (resolving_run 838; state left **alive** because 838 is `non_degenerate: false` — a precondition-unmet run narrows the solution space but does not clear the elimination bar). `initial_frozen_count = 3`. See the JSON `fanout_recommendation` and the registry append.
