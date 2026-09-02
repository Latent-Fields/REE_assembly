# Failure autopsy -- V3-EXQ-395 / MECH-220 harm hub

Generated 2026-09-02T05:04:59Z. Status: **confirmed** (interactive gate, 2026-09-02).
Red-team pass: Fable, verdict **CONFIRMED**.
Re-adjudication of `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` (a self-described
closure stub: "No re-diagnosis").

## Scope and the dry-run gate

Four manifests exist for this experiment type. **Three are genuine `--dry-run` smokes and are NOT
targets**: `..._dry_20260413T074905Z`, `..._dry_20260413T075033Z`, `..._dry_20260413T075133Z`.
The target is the real run `v3_exq_395_mech220_harm_hub_20260418T202544Z_v3`.

The smokes are hard to detect and this is worth recording. None carries a `dry_run` field -- the
`pack_writer` chokepoint that stamps it postdates these runs by three months -- and the driver
writes the module CONSTANTS into the manifest (`"eval_episodes": EVAL_EPISODES`, driver:768-770)
rather than the reduced values actually executed. So all three assert 100/100/100 episodes while
having run 3/3/5. `total_steps` is what gives them away: 254-300 per condition against 5918-5982
for the real run. `check_dry_run_citations.py` cannot catch this class.

## Facts

| | real run | dry smokes |
|---|---|---|
| `mean_harm_rate_delta` | **exactly 0.0** | exactly 0.0 (all three) |
| `mean_z_harm_a_norm_delta` | 0.1091 | 0.1069 / 0.1111 / 0.1111 |
| `harm_events`, `total_steps` | identical per seed per arm | identical per seed per arm |
| `substrate_hash` | absent | absent |

Corroboration is stronger than equal means: `harm_events` AND `total_steps` are bit-identical
between arms in all 12 run x seed pairs (seed 42: 174/5982 both arms). The arms produced
identical trajectories, not merely equal aggregate rates.

Criteria: PASS requires C1 AND (C2 OR C3). C1 is a hard conjunct, so `delta = 0.0` forces FAIL
regardless of C2 and C3 -- both of which passed in every seed.

## The mechanism: an additive constant cannot change an argmin

`_hub_guided_action` (`ree-v3/experiments/v3_exq_395_mech220_harm_hub.py:457-492`) reads
`agent._current_latent.z_harm` and `.z_harm_a` -- values with **no dependence on the candidate
cell `(nx,ny)` or the loop index `i`**. No simulated step is performed and the `obs_harm` /
`obs_harm_a` arguments are never used in the body. So `harm_pred` (:484) is the same scalar `K`
for all five candidates and the score reduces to

    combined(i) = K + haz_prox(i) - 0.5 * res_prox(i)

`argmin_i` is invariant to `K`. **The hub cannot change the selected action at any `hub_weight`.**
Verified independently: `hub()` and `harm_eval_z_harm` are pure, nothing writes `_current_latent`
inside the loop, and the `random.randint` fallback is unreachable since `(0,0)` is always valid.

The driver never calls `agent.act` or `agent.select_action` (zero grep matches), so the real
consumer path -- where `z_harm_a` genuinely is wired (`agent.py:6471-6474, 6505, 7367, 9124,
10355-10358`) -- was entirely bypassed. C3 moved because it measures the manipulation directly;
C1 is exactly 0.0 because it measures a quantity the manipulation cannot reach.

## Two escalations found this pass

1. **MECH-220's mechanism has no substrate implementation.** `HarmHub` does not exist anywhere in
   `ree-v3/ree_core` (grep empty). The only hub that has ever existed is the inline module inside
   this experiment driver. Four runs argued about a mechanism that lives in a test file.
2. **The claim's only `weakens` evidence comes from two smokes.** `claim_evidence.v1.json` carries
   `weakens` for `..._dry_074905Z` and `..._dry_075133Z` with `scoring_excluded=None` -- both
   counted -- while the real run is correctly excluded as `non_contributory` and the third smoke
   as `superseded`. MECH-220 reads `direction_counts weakens: 2`, `genuine_exp_count: 0`.

## The stale hold

MECH-220's note says the null was a "Symptom of missing SD-032b ... V3-EXQ-445 queued as retest.
Claim held pending that retest." That attribution is not supportable -- SD-032b's consumer pathway
is irrelevant to a driver that never routes through it -- and the hold is undischargeable on its
own terms: the 445 lineage ran across 7 letters (445, 445a/b/c/f/g/h), every run FAIL /
`non_contributory`, and **not one tags MECH-220**.

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | intact (untested) |
| Biological reference | partial -- 4 lit entries; the cited "Chen (2023)" is absent from the corpus |
| Prerequisites | present at claim level; irrelevant, the driver bypasses them |
| Implementation | **absent** -- no HarmHub in `ree_core` |
| Environment | adequate |
| Measurement | misleading -- C1 measures what the manipulation cannot reach |
| Integration | isolated |
| Scale | adequate |

**Failure-location (GOV-FAILLOC-1): MEASURES.** Not chargeable to REE -- the substrate mechanism
was never exercised.

## Routing (confirmed at gate)

`queue-experiment`. Exclude the two smoke entries from the index; replace the stale hold; set
`epistemic_category: standard`. A successor must measure upstream of the argmin, or expect the
MECH-439 conversion ceiling. Building a real `HarmHub` in `ree_core` is a prerequisite for any
run that claims to test MECH-220 -- recorded here, not routed, per the gate.
