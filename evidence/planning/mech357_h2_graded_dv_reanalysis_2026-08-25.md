# MECH-357 H2 reanalysis -- graded-DV re-read of the already-recorded 603s/603t/603u trajectories

**Date:** 2026-08-25
**Session:** `metaworker-chip-20260825-mech357-h2-reanalysis` (headless)
**Owns:** the H2 probe named in
[`failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16.json`](failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16.json)
`targets[1].fanout_recommendation.suggested_probes[0]` and required by that autopsy's
`recommended_substrate_queue_entry.implementation_hint` ("Do NOT open a fifth pressure
MECHANISM without first running the zero-compute H2 reanalysis in fanout_recommendation").
**Debt class:** `mystery (known data)` on entry, per the autopsy. **Resolved to: the declared
null is REFUTED, but the refutation is sign-reversed from what MECH-357 predicts and its
causal interpretation is genuinely unclear -- this is a live discrimination that needs a
governance/failure-autopsy adjudication, not a `H1/H3 carry the weight` close-out.**
**Changes no claim status, confidence, `epistemic_category`, `evidence_direction`, or
`substrate_queue.json` field. Reanalysis of already-recorded data only -- zero new compute,
no code change, no queue entry.**

---

## Verdict in one paragraph

The autopsy's declared null for H2 was: *"graded DVs also show INTACT ~= LESION across all
three runs -> the ceiling was not the obstruction, and H1/H3 carry the weight."* That null
does **not** hold. Two independently-computed graded readouts -- (1) the whole-Stage-H-window
mean episode length, already persisted for all three arms in every one of the 9 (run x seed)
cells, and (2) a **true per-episode last-10-window mean**, reconstructed from a per-episode
array (`avoidance_efficacy_trajectory[].episode_length`) that turns out to already be recorded
for the INTACT/POSCTRL arms but not for LESION -- both show a **consistent, non-trivial
reversal**: the gated arms (INTACT, POSCTRL) survive **shorter**, not longer, than the
ungated LESION control, in 6 of 6 run-level averages and 16 of 18 individual (run, seed, arm)
comparisons across 603s/603t/603u. The effect is cleanest and most uniform in V3-EXQ-603u
(6/6 cells negative, deficits of 59-98 steps out of a 200-step ceiling), the run the autopsy
spent 19.2 hub-hours on. This is a real, reproducible-across-three-designs discrimination in
the already-recorded data -- just the opposite sign from what MECH-357's confirming
prediction requires, and its causal story is unresolved (plausibly related to the already-
known gate-extinction defect H3, or to the protective-scaffold anneal forcing risky movement
before the policy has learned to navigate, or to something else). **This is exactly the kind
of finding the task brief asks not be self-adjudicated: flagged here for governance /
failure-autopsy, not resolved.**

---

## 1. What data actually exists (an instrumentation-asymmetry finding in its own right)

The task brief, following the autopsy's probe sketch, asked for "the ALREADY-RECORDED
per-episode trajectories of 603s/603t/603u" re-read with a graded DV (mean episode length,
survival fraction, time-to-first-death, hazard-contact rate). Checking what is actually on
disk, under each run's TASK_CLAIMS-scoped resource path
(`REE_assembly/evidence/experiments/v3_exq_603{s,t,u}_.../runs/<run_id>/{manifest.json,
metrics.json,summary.md}`), and the corresponding flat manifest at
`REE_assembly/evidence/experiments/<run_id>.json` (the one the indexer/governance actually
read):

- The **per-run-directory** `manifest.json`/`metrics.json`/`summary.md` files are thin
  (5.6-5.7 KB, empty `metrics.json`, one-line `summary.md`) -- they carry only outcome/status
  and the readiness-precondition block, not per-seed data.
- The **flat manifest** (`v3_exq_603{s,t,u}_..._v3.json`, top-level `evidence/experiments/`)
  carries the real payload: `arm_results` and a `per_seed` list (9 rows: 3 arms x 3 seeds).
- Reading `ree-v3/experiments/scaffolded_sd054_onboarding.py` `run_hazard_avoidance()`
  (`:2530-2705`) against what the driver script (`ree-v3/experiments/
  v3_exq_603u_instrumental_avoidance_agent_pursuit.py` `_run_seed_arm()`) actually persists
  into `per_seed`, confirms:
  - `HazardAvoidanceResult.episode_lengths: List[int]` (line 764) -- the full 40-episode
    per-episode-length array -- **is computed in memory but never copied into the manifest**.
    The driver only pulls `hz.mean_episode_length`, `hz.median_last_window_episode_length`,
    `hz.n_episodes` (`v3_exq_603u..._agent_pursuit.py:584-586`). This array is gone forever
    for all three arms across all three runs; it cannot be recovered from recorded data.
  - **BUT** a second, independent per-episode record exists for the gated arms only:
    `avoidance_efficacy_trajectory` (built at `scaffolded_sd054_onboarding.py:2660-2667`,
    one dict per Stage-H episode with `episode`, `episode_length`, `avoidance_efficacy`,
    `n_credit`, `n_decay`, `n_freeze_suppressed`), captured **only when `agent.
    instrumental_avoidance` exists** (`if _gate is not None:`). LESION has `use_ia=False` ->
    no gate object -> this list is `[]`. INTACT and POSCTRL both have `use_ia=True` -> full
    40-entry trajectories, confirmed present and length-40 for all 6 (arm, seed) x 3 runs =
    18 cells checked.
  - This is an **asymmetric instrumentation gap**, not previously named in the autopsy or
    either prior scoping note: a genuine per-episode readout exists for the two gated arms
    (as an accidental byproduct of the gate's own diagnostic logging) but not for the
    negative control. A fully symmetric, three-arm per-episode reanalysis is **not**
    reconstructable from what is on disk; see the caveat in SS3 below.
  - Neither `episode_lengths` nor `avoidance_efficacy_trajectory` records intra-episode
    step-level events, so **time-to-first-death and hazard-contact-rate -- two of the four
    DVs the autopsy's probe sketch named -- cannot be reconstructed at all**, for any arm,
    from any of the three runs. Computing them would require a new instrumented re-run, which
    is outside this task's zero-compute scope and outside what H2 asked for.

**Net: of the four candidate graded DVs the autopsy named, only "mean episode length" is
actually recoverable from recorded data -- in two different windowings (whole-run, and a
true last-10-episode mean for the gated arms) -- and "survival fraction" is partially
recoverable (gated arms only). This narrower recoverable set is what SS2-SS4 report.**

## 2. Whole-Stage-H-window mean episode length (all three arms, symmetric, wrong window)

`hazard_stage_mean_episode_length` (mean over all 40 Stage-H episodes) is recorded for every
arm in every cell and is genuinely graded (not saturated the way `hazard_stage_median_last_
window` is). Paired by seed within each run:

| run | seed | LESION mean | INTACT mean | POSCTRL mean | INTACT-LESION | POSCTRL-LESION |
|---|---|---|---|---|---|---|
| 603s | 42 | 131.32 | 144.25 | 146.32 | +12.93 | +15.00 |
| 603s | 43 | 107.05 | 5.97 | 62.30 | -101.08 | -44.75 |
| 603s | 44 | 141.18 | 144.50 | 5.97 | +3.32 | -135.20 |
| 603t | 42 | 145.95 | 105.67 | 149.88 | -40.27 | +3.93 |
| 603t | 43 | 136.28 | 5.95 | 49.25 | -130.33 | -87.03 |
| 603t | 44 | 150.95 | 80.15 | 105.80 | -70.80 | -45.15 |
| 603u | 42 | 126.55 | 130.32 | 102.38 | +3.77 | -24.17 |
| 603u | 43 | 131.30 | 99.80 | 69.53 | -31.50 | -61.78 |
| 603u | 44 | 131.40 | 93.25 | 111.22 | -38.15 | -20.18 |

Pooled over the 9 matched cells: INTACT-LESION mean diff = **-43.6** (positive in 3/9);
POSCTRL-LESION mean diff = **-44.4** (positive in 2/9). Per-run averages (mean of the 3
seed-diffs): 603s INTACT -28.3 / POSCTRL -55.0; 603t INTACT -80.5 / POSCTRL -42.8; 603u
INTACT -22.0 / POSCTRL -35.4. **All 6 run-level averages are negative** -- the gated arms
underperform LESION on this DV in every one of the three independently-designed pressure
mechanisms, not just on average across noisy seeds.

**Caveat, load-bearing:** this mean is dominated by early-Stage-H episodes, not the
pre-registered scoring window. Cross-checking against `median_last_window` shows 21 of the
27 cells hit the exact 200-step ceiling in the scored (last-10) window regardless of arm, so
most of this whole-run gap reflects the gated arms taking **longer to converge** during
training (more early mortality before the policy learns to navigate), not necessarily a
difference in final avoidance capability. This is itself a new, previously-unquantified
finding, but it does not by itself answer the pre-registered discrimination question. SS3
answers that question directly.

## 3. Scoring-window comparison, using the TRUE last-10-episode mean (not the saturated median)

For the six gated-arm cells per run, the recovered `avoidance_efficacy_trajectory` gives an
exact per-episode length for the last 10 Stage-H episodes -- the actual pre-registered
scoring window (`HAZARD_STAGE_STABILITY_WINDOW=10`). Comparing each gated arm's **true
last-10-episode mean** against LESION's `median_last_window` (LESION's own best-available
scored readout, since no per-episode array exists for it -- see the asymmetry caveat below):

| run | seed | LESION `median_last10` | INTACT true `last10_mean` | diff | POSCTRL true `last10_mean` | diff |
|---|---|---|---|---|---|---|
| 603s | 42 | 200.0 | 161.0 | -39.0 | 141.1 | -58.9 |
| 603s | 43 | 5.5 | 5.9 | +0.4 | 121.5 | +116.0 |
| 603s | 44 | 200.0 | 180.4 | -19.6 | 6.0 | -194.0 |
| 603t | 42 | 200.0 | 160.7 | -39.3 | 121.3 | -78.7 |
| 603t | 43 | 200.0 | 6.0 | -194.0 | 160.7 | -39.3 |
| 603t | 44 | 200.0 | 82.8 | -117.2 | 121.9 | -78.1 |
| 603u | 42 | 200.0 | 121.8 | -78.2 | 101.9 | -98.1 |
| 603u | 43 | 200.0 | 121.6 | -78.4 | 121.5 | -78.5 |
| 603u | 44 | 200.0 | 102.0 | -98.0 | 141.2 | -58.8 |

Pooled: INTACT `last10_mean` - LESION `median_last10` = **-73.7** (positive in only 1/9);
POSCTRL - LESION = **-63.2** (positive in only 1/9). **In V3-EXQ-603u specifically -- the run
the autopsy's fanout was scoped around, 19.2 hub-hours -- all 6 gated-arm cells are negative,
with a tight, consistent deficit of 59-98 steps (out of the 200-step ceiling) and no
exceptions.** This is the cleanest signal in the entire dataset.

**Asymmetry caveat, stated plainly:** LESION's column here is a *median* (its only available
scored readout), while INTACT/POSCTRL's columns are *true means* recovered from actual
per-episode data. Since the gated arms' own last-10 windows are themselves visibly bimodal
(e.g. 603s seed 42 INTACT last-10 = `[200,200,200,200,200,200,6,200,4,200]` -- true mean 161
vs. median 200), it is plausible LESION's last-10 window is *also* internally bimodal and its
true mean would sit below its median of 200 too. If so, the true INTACT/POSCTRL-vs-LESION gap
could be **narrower** than the numbers above (which likely overstate LESION relative to a
true apples-to-apples reading) -- but the *direction* is independently corroborated by SS2's
fully-symmetric whole-run-mean comparison, which used a true mean on both sides and found the
same sign in all 6 run-level averages. Recovering LESION's true last-10 mean would require a
new instrumented re-run (the gate object that captures per-episode data does not exist when
`use_ia=False`); that is out of scope for a zero-compute reanalysis.

## 4. Survival fraction within the last-10 window (gated arms only, no LESION comparator)

As a bonus graded DV recoverable from the same trajectory (episodes >= 75 steps, the
survival-gate threshold, within the last 10 episodes):

| run | INTACT per-seed survival_frac | POSCTRL per-seed survival_frac |
|---|---|---|
| 603s | 0.80, 0.00, 0.90 | 0.70, 0.60, 0.00 |
| 603t | 0.80, 0.00, 0.40 | 0.60, 0.80, 0.60 |
| 603u | 0.60, 0.60, 0.50 | 0.50, 0.60, 0.70 |

This confirms the coarse median-based pass/fail gate is discarding real structure exactly as
H2 hypothesized: e.g. 603u INTACT seed 44 and POSCTRL seed 42 both land on the design's
"intermediate" `median_last_window` values (103.0, 102.0) precisely because their last-10
survival fraction sits at 0.50 -- a real 50/50 split the binary gate cannot see either way.
**No LESION-side survival fraction exists to compare against** (SS1's asymmetry), so this
table documents that finer structure exists, without being able to say whether LESION's own
finer structure would look better, worse, or the same.

## 5. What this does and does not settle

**Settled:** the declared null ("graded DVs also show INTACT ~= LESION ... H1/H3 carry the
weight") is refuted on every graded readout recoverable from the already-recorded data. The
data is not "approximately equal" under any re-aggregation tried here -- it discriminates,
consistently, across three independently-designed pressure mechanisms, in the direction of
LESION outperforming the gated arms.

**Not settled, and explicitly NOT adjudicated by this session per the task brief:**

- **Which epistemic reading this deserves.** MECH-357's own pre-registered acceptance frame
  (`v3_exq_603u_..._agent_pursuit.py:88-96`) defines a FALSIFYING outcome as "readiness met,
  primary fails" -- which is closer to what this reanalysis surfaces than the run's own
  `non_contributory` self-classification, since a real (if reversed) effect is present in
  data the coarse gate called a wash. Whether that reframes any of the three runs'
  `evidence_direction` is a governance call, not one made here.
- **Causal mechanism.** Two live candidate stories, neither tested here: (a) this is
  downstream of the already-known, already-in-flight H3 gate-extinction defect (eligibility
  trace underflows to ~1e-120 by the scoring window; `n_freeze_suppressed` counts of 46-151
  were confirmed in the worst cells above, meaning the gate suppressed freeze many times
  *early*, while `avoidance_scaffold_floor` was still high, then went numerically silent by
  the scoring window) -- i.e. the gated arms may be paying an early-training cost (forced
  movement before the policy can navigate safely) for a mechanism that has stopped
  functioning by the time it is measured; or (b) something about `scaffold_avoidance_driver_
  enabled`'s extra training-loop machinery (independent of the freeze-suppression behavior
  itself) destabilizes the shared policy. Distinguishing these needs the in-flight
  eligibility-trace fix (H3 track, explicitly out of scope here) to land and a re-run, not a
  further reanalysis of this data.
- **Whether a fifth pressure-mechanism experiment is warranted.** Per the autopsy's own
  routing (`refused_requeue: true`, four pressure mechanisms already exhausted) and per this
  reanalysis (the ceiling was not hiding an *unfavorable-to-null* result -- it was hiding a
  reversed one), a fifth pressure-magnitude experiment (H1) is not motivated by this finding
  either. **No experiment is queued by this session.**

## 6. Recommendation

**Flag this prominently for the next `/governance` or `/failure-autopsy` cycle.** This is a
live, reproducible discrimination in already-adjudicated data (V3-EXQ-603s/603t/603u are all
closed as `non_contributory`), not a confirmation of the declared null -- it should not be
read as clearing the way for `H1`/`H3`-only routing without a human/governance decision on
what the reversed-sign finding means for MECH-357's `evidence_direction` and for the
`mech357-freeze-incompatible-pressure-mechanism` / `mech357-avoidance-efficacy-eligibility-
trace-imbalance` substrate_queue entries (neither edited by this session, per the task
brief). Suggested next steps for that cycle to weigh, not act on here:
1. Decide whether V3-EXQ-603u (and/or 603s/603t) should be re-read as `weakens` rather than
   `non_contributory`, given a real discrimination now exists in the recorded data.
2. Consider whether the driver's own `_run_seed_arm` should be amended to also persist
   `HazardAvoidanceResult.episode_lengths` for **all** arms (not just derive a proxy via the
   gate's trajectory for two of three) -- a one-line addition that would close the SS1/SS3
   asymmetry for any future retest, independent of the H3 fix.
3. Weigh this finding alongside the in-flight eligibility-trace fix
   (`ree-v3/ree_core/pfc/infralimbic_avoidance_gate.py`, active claim
   `closure-maps-correctness-807268`) before deciding whether a post-fix 603u re-run (already
   planned as the H3 probe) should also add the episode_lengths persistence fix from (2) so
   the re-run does not repeat this same asymmetry.

## Provenance

- **Zero new compute.** No experiment run, no queue entry, no dry-run. All numbers above are
  re-aggregations of fields already present in the three runs' flat manifests
  (`v3_exq_603{s,t,u}_..._v3.json`) and the `scaffolded_sd054_onboarding.py` source read to
  confirm what those fields actually measure.
- **Files read:** the three flat manifests; the three per-run-directory packs (`manifest.json`
  /`metrics.json`/`summary.md`); `ree-v3/experiments/v3_exq_603u_instrumental_avoidance_
  agent_pursuit.py` (full); `ree-v3/experiments/scaffolded_sd054_onboarding.py` (`:2530-2705`,
  `run_hazard_avoidance`); `failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16
  .json` (full); `mech357_avoidance_efficacy_plan.md`; `mech357_freeze_incompatible_pressure_
  scoping_2026-08-10.md` (for prior-art / naming-convention cross-check -- it independently
  used `mean_ep_len` on 603s and reached a different, non-conflicting conclusion about
  within-seed bimodality; this note extends that analysis to the cross-arm comparison the
  prior note did not attempt).
- **Files deliberately NOT written:** `docs/claims/claims.yaml`, `evidence/planning/
  substrate_queue.json`, `TASK_CLAIMS.json` (status field), any experiment manifest, any
  `ree-v3` code. Per the task brief, this session does not set `epistemic_category` or
  `evidence_direction` and does not queue a new experiment.
- **TASK_CLAIMS:** opened under session-id `metaworker-chip-20260825-mech357-h2-reanalysis`,
  covering the three run directories and this plan doc, before any file was read.
