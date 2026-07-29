# Failure Autopsy: V3-EXQ-822b (SD-078/SD-082) + V3-EXQ-834 (ARC-071/MECH-323)

Generated: `2026-07-29T20:00:13Z`
Scope: single (V3-EXQ-834 only -- see Section 0 for why 822b is not re-adjudicated here)
Status: confirmed

Both targets were selected from the "Diagnostic adjudication required (self-route unverified)"
section of `pending_review.md` (regenerated 2026-07-29T19:36:56Z), both self-routed
`substrate_not_ready_requeue`, both flagged `precondition_unmet` by the indexer.

Dry-run gate (Step 2a): both run_ids checked with `scripts/check_dry_run_citations.py` --
`-- 0 dry cited, 0 dry in named families, 0 ambiguous, 2 clean, 0 unknown`. Neither is a smoke.

---

## 0. V3-EXQ-822b -- ALREADY AUTOPSIED, NOT RE-ADJUDICATED

`v3_exq_822b_sd082_head_internals_diagnostic_20260727T180919Z_v3` already carries a **confirmed**
autopsy: `failure_autopsy_2026-07-28-sweep.json` (generated_utc 2026-07-28T21:04:30Z), target index 0.

That autopsy's finding is more decisive than this session's independent read got to before
discovering it: the run's own `precondition_unmet` flag (`head_diag_samples_sufficient`, 0
tick-sampled reads on the worst cell) only gates the two NEW per-tick diagnostics
(`hidden_dead_relu_frac`, `rule_summary_magnitude_ratio`). It does **not** gate the four
phase-boundary weight-norm snapshots, which are unconditional parameter reads. Those show
`head_untrained_last_layer_static=true` and `on_last_layer_weight_delta_init_to_p1_mean=0.0` in
BOTH 822a and 822b -- the REINFORCE-trained `rule_bias_head`'s last linear layer moved exactly
zero across the full 70-episode P1 phase. That is the confirmed root cause of `propagation_
non_vacuity`'s repeated 0.0 reading, independent of the sample-starved tick diagnostics this
session initially focused on (a plausible but narrower thread: a bare `except Exception: return
None` in `_prop_delta_and_flip_with_diag` that could also explain the zero tick samples, but the
prior autopsy's unconditional-readout finding already answers the decisive question and does not
depend on that swallowed-exception hypothesis being true).

Prior recommendation: `routing: implement-substrate`, `recommended_substrate_queue_entry.action:
amend` (`target_sd_id: SD-082`), tracing why REINFORCE never updates this layer (optimizer
parameter registration / gradient flow through the tanh bound / whether `ADV_MIN_THRESHOLD=0.005`
ever fires). `re_derive_brake.fired: false` (SD-078 has 2 prior non-`substrate_ceiling` autopsies
plus this one, still not `substrate_ceiling` under R3), but the note already flags this as the
third same-shape finding worth a routing consideration.

**Verified 2026-07-29T20:00Z: this recommendation has NOT yet been applied.** No `SD-082` entry
exists in `substrate_queue.json`; the run_id is not in `review_tracker.json` `reviewed_run_ids`.
This is a `/governance` backlog item, not an autopsy gap -- writing a second, independent 822b
adjudication here would risk contradicting or diluting the existing, better-evidenced one. This
session defers to the 2026-07-28 artifact and does not re-score 822b. **Action needed: run
`/governance` to apply the confirmed 2026-07-28 sweep (9 targets, including 822b), not another
autopsy.**

---

## 1. V3-EXQ-834 -- ARC-071 / MECH-323 budget-coupled ceilings

### Facts

- **Run**: `v3_exq_834_arc071_mech323_budget_coupled_ceilings_20260729T002336Z_v3`, queue_id
  V3-EXQ-834, `experiment_purpose: diagnostic`, outcome FAIL, `non_degenerate: false`.
- **Recording provenance**: full always-core present (`recording_schema: rec/v1`, `substrate_hash`,
  `machine: ree-worker-3`, `machine_class`, `elapsed_seconds`, `config`, `seeds`). No recording gap.
- **Design**: 5 arms (STATIC_H50, BOTH_H30, SIZE_H50, DEPTH_H50, BOTH_H50) x 5 seeds (101, 202,
  303, 404, 505), 100 episodes/seed, 60 steps/episode. Baseline module
  `experiments/_lib/baselines/arc071_chunk_budget.py` (new for this lineage, mint run V3-EXQ-834).
- **degeneracy_reason** (verbatim): "Non-vacuity gate RED in EVERY arm: arm 'STATIC_H50' failed
  chunks_formed; arm 'BOTH_H30' failed chunks_formed; arm 'SIZE_H50' failed chunks_formed; arm
  'DEPTH_H50' failed chunks_formed, depth_gain_evaluable_trials; arm 'BOTH_H50' failed
  chunks_formed, depth_gain_evaluable_trials. No arm is scored; this run is NOT a refutation."
- **Self-route label**: `substrate_not_ready_requeue`. **Failed criterion: readiness precondition
  (`chunks_formed`), not a discrimination or absolute/negative-control criterion.**

### The key measurement (per-seed, per-arm; identical pattern in every arm)

| seed | symbol throughput/ep | chunks formed (range across arms) |
|---|---|---|
| 101 | 11.07 | 28-42 |
| 202 | **9.10** | **0 (every arm)** |
| 303 | 7.87 (right at the 7.5 floor) | 8 (every arm) |
| 404 | 12.08 | 25-44 |
| 505 | 10.20 | 14 (every arm) |

Seed 202 is the sole zero. Its throughput (9.10/ep) sits **mid-pack**, above seed 303's 7.87/ep
-- and seed 303 (the seed with the *lowest* throughput of the five) still formed 8 chunks in
every arm. So seed 202's failure is not explained by "too few symbols" (the failure mode the
`symbol_buffer_per_episode` precondition and the V3-EXQ-810 predecessor defect were built to
catch, and which this baseline's own docstring explicitly re-derives a margin against). It matches
instead the *other* side of the margin the baseline module's docstring explicitly names: "too many
symbols raises key DIVERSITY, and a specific n-gram then recurs across trials less often, which is
what `min_repetitions` actually requires" (`arc071_chunk_budget.py:67-69`). 4 of 5 seeds (80%)
formed chunks robustly (8 to 44 each) -- the mechanism itself is working.

### Gate-design finding

The `chunks_formed` (and `depth_gain_evaluable_trials`) readiness preconditions are evaluated at
**worst-cell-across-all-5-seeds** (100%). The run's own `SEED_PASS_FRACTION = 3.0/5.0` (0.6) is
defined and used for the actual load-bearing scoring criteria (C2, C4) -- but readiness is stricter
than the criteria it exists to protect. A single seed's zero-chunk outcome vacates the entire run
even though 80% of seeds clear the bar the criteria themselves would have accepted.

Cross-checked against the sibling mint run **V3-EXQ-810a** (`arc071_chunk_accumulator_readiness`,
PASS), which ran on the **identical substrate build** (`substrate_hash
12dc9bfda051930e4b090e18fe9c375b3174a7991b7622a6f24debc9c0170882`, both started within 8 seconds
of each other on 2026-07-28). 810a validated the chunk-accumulator mechanism works, using a
*different* baseline module (`arc071_chunking`, 8 seeds, 72 steps/episode, 120 episodes) than 834's
own (`arc071_chunk_budget`, 5 seeds, 60 steps/episode, 100 episodes). 834's own docstring already
anticipated the V3-EXQ-810 defect class and built a readiness gate against it -- and the gate is
doing its job (correctly declining to score a run where one seed didn't form chunks) -- but its
100%-of-seeds bar is not what the rest of this run's own design treats as sufficient evidence.

### Claim-layer map

| Claim | Status | depends_on | v3_pending |
|---|---|---|---|
| ARC-071 | candidate | ARC-069, MECH-163 | true |
| MECH-323 | candidate | ARC-071, MECH-094, MECH-322, SD-014, SD-039, MECH-269 | true |

Both `experiment_purpose: diagnostic` -- excluded from confidence/conflict scoring regardless of
this run's outcome. `recommended_evidence_direction: unknown` (unchanged from the manifest).

### Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (diagnostic-purpose; not scored either way) | mechanism itself shows no sign of failure on 4/5 seeds |
| Biological reference | clear | procedural/motor-sequence chunking (striatal chunking literature) is well-established; nothing here implicates the biology |
| Prerequisites | present | V3-EXQ-810a already validated the chunk-accumulator readiness fix on this identical substrate build |
| Implementation | complete for the mechanism; the readiness **gate** is the defective piece | 4/5 seeds form 8-44 chunks; the accumulator/crystallization logic is functioning |
| Environment | adequate | resource-and-hazard grid, num_hazards=2 (deliberately, per the baseline docstring, to avoid the perfectly-periodic E3 tick that starved V3-EXQ-810) |
| Measurement | under-instrumented at the gate level | `chunks_formed`/`depth_gain_evaluable_trials` readiness use worst-cell (100% of seeds) where the run's own scoring criteria use `seed_pass_fraction=0.6` |
| Integration | isolated | no cross-module coupling issue; single-seed anomaly within one baseline's own accumulator |
| Scale | adequate | 100 episodes x 5 seeds x 5 arms is the declared design, not a truncation |

### Recommended epistemic category

`measurement_test_design_defect` -- the readiness gate's threshold (100% of seeds) is inconsistent
with the tolerance the run's own scoring criteria already declare acceptable (60% of seeds), and
seed 202's outlier is more consistent with legitimate high-diversity variance (explicitly
anticipated by the baseline's own docstring) than with a recurrence of the true V3-EXQ-810
"chunk-accumulator-silent" defect, which 810a already confirmed fixed on this same substrate.

### Repair pathway

`complex (probe-gated) / mystery (known data)` -- the data already exists (5 seeds, clear
per-seed chunk counts); the readiness-gate *frame* is what's wrong, not a missing measurement.
No new run is needed to see this; the fix is to the precondition logic itself, then a re-run to
confirm scoring proceeds.

**Routing: `/queue-experiment`, same-question re-run, alphabetic suffix (V3-EXQ-834a).** Change:
evaluate `chunks_formed` and `depth_gain_evaluable_trials` readiness at `seed_pass_fraction`
(>=60% of seeds clearing the floor), consistent with how C2/C4 already score, rather than at
worst-cell. Do NOT route to `/implement-substrate` -- 810a already validated the underlying
mechanism on the identical substrate build; there is no substrate gap to fill, only a gate-logic
fix in the driver script.

### Draft `evidence_quality_note` (for governance to apply, NOT written by this skill)

> V3-EXQ-834 (2026-07-29, ARC-071/MECH-323 budget-coupled-ceilings diagnostic) self-routed
> `substrate_not_ready_requeue`: the `chunks_formed` readiness precondition failed in every arm
> because seed 202 formed zero chunks. However 4/5 seeds (80%) formed chunks robustly (8-44 each),
> comfortably clearing this run's own `seed_pass_fraction=0.6` tolerance used for its scoring
> criteria. Seed 202's throughput (9.10 symbols/episode) was mid-pack -- not the lowest -- so this
> does not reproduce the V3-EXQ-810 "too few symbols" defect that V3-EXQ-810a already confirmed
> fixed on the identical substrate build (`substrate_hash 12dc9bf...`, both started within 8s of
> each other). Read as `measurement_test_design_defect`: the readiness gate (100%-of-seeds,
> worst-cell) is stricter than the criteria it protects (60%-of-seeds). Recommend
> `/queue-experiment` V3-EXQ-834a with the readiness gate re-evaluated at `seed_pass_fraction`
> rather than worst-cell. `pending_retest_after_substrate: false` -- no substrate work is needed.

### Re-derive brake

Not fired. Prior autopsies against ARC-071/MECH-323: V3-EXQ-810 (`failure_autopsy_backlog_2026-07-24`,
category `competence_implementation_gap`, non_contributory) and V3-EXQ-810a (PASS, no autopsy
target). Neither is `substrate_ceiling` under R3; this target's own recommended category
(`measurement_test_design_defect`) is also not `substrate_ceiling`. Count = 0. Threshold (2) not
reached; no refusal of a same-question re-queue is warranted (and V3-EXQ-834a is exactly that
same-question re-queue, which the brake does not block).

### Granularity-debt recurrence trigger

Checked via `scripts/granularity_debt_cluster.py` for both ARC-071 and MECH-323 (targets whose own
`claim_ids` name the claim, not a planning-dir grep):

- ARC-071: 1 target (`failure_autopsy_backlog_2026-07-24`, run=V3-EXQ-810), alignment `unclear`.
- MECH-323: 2 targets (`failure_autopsy_2026-07-28-sweep` run=V3-EXQ-829, alignment `strengthened`
  [MECH-323 retention structure] / weakened only on MECH-324's specific quantitative prediction;
  and `failure_autopsy_backlog_2026-07-24` run=V3-EXQ-810, alignment `unclear`).

**Does not fire.** No target for either claim reads `weakened` on MECH-323/ARC-071 itself (the one
`weakened` reading in the MECH-323 cluster is scoped to MECH-324's quantitative prediction, not to
MECH-323). This is measurement/implementation debt, not granularity debt -- consistent with the
`measurement_test_design_defect` category above.

### Learning extracted

1. A readiness/vacuity gate can be **stricter than the scoring criteria it exists to protect** --
   here, worst-cell-across-100%-of-seeds versus the run's own declared 60% `seed_pass_fraction`.
   This is a distinct failure mode from the "gate correctly catches a real substrate defect"
   pattern (V3-EXQ-810) and needs to be checked for on every readiness precondition, not assumed
   uniform with the scoring logic just because both live in the same driver.
2. Comparing a flagged run against a **sibling mint run on the identical `substrate_hash`**
   (810a, started within 8 seconds of 834) is a fast, decisive way to rule out "the substrate
   regressed" as an explanation when a new driver's own readiness gate fails -- if the sibling
   passed on the same substrate build, the defect is very unlikely to be a substrate regression.
3. A baseline module's own docstring anticipating a specific failure mode (here: the
   diversity-vs-repetition margin) is worth checking against the *actual* per-seed data before
   accepting a readiness gate's verdict at face value -- the docstring's own reasoning is what
   identified this as likely benign variance rather than a new defect.
