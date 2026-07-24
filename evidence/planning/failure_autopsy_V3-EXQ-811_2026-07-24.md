# Failure Autopsy: V3-EXQ-811 (MECH-477 / MECH-163 dual-system arbitration falsifier)

**Generated:** 2026-07-24T05:11:04Z
**Status:** confirmed (interactive gate cleared with user 2026-07-24)
**Scope:** single
**Run:** `v3_exq_811_mech477_dualsystem_arbitration_falsifier_20260723T054309Z_v3`
**Claims:** MECH-477, MECH-163

## 1. Facts reconstruction

V3-EXQ-811 is the falsifier for SD-081 (`e3.dualsystem_uncertainty_arbitration`), built 2026-07-22 in direct
response to V3-EXQ-786a's diagnosis that MECH-163's flat-response null was the signature of "two pathways with
no arbitrator." The experiment compares `arb_off` (arbitrator disabled) vs `arb_on` (arbitrator enabled) on the
786a recruitment design, across 8 seeds x familiar/novel layouts.

**Manifest self-route:** `outcome=FAIL`, `evidence_direction=non_contributory` (both claims), `interpretation.label
= substrate_not_ready_requeue`, `non_degenerate=False`. The cited cause: both arms failed
`full_score_range_non_degenerate`, `habit_score_range_non_degenerate`, and `habit_score_distinct_fraction` --
the exact three-part readiness gate this experiment's own precondition literally names *"THE GATE V3-EXQ-786a
LACKED."* On its face this looks like a repeat of 786a's constant-vector degeneracy, this time surviving the
new gate.

**But the substantive criteria already read clean in the raw manifest:**

| Criterion | Load-bearing | Passed | Detail |
|---|---|---|---|
| C1_recruitment_delta_greater_with_arbitrator | yes | **true** | 7 divergent seeds, 6/7 ON greater (85.7%); Cohen's d 0.999 (ON) vs -0.158 (OFF); robustness bar clears ON (mean 0.156, lower bound 0.097 > margin 0.02), fails OFF (mean -0.020, lower bound -0.065) |
| C2_arbitration_weight_novelty_shift | no | true | measured 0.194 vs threshold 0.01 |
| arbitration_live_non_degenerate | -- | true | 1.0 (100% of ON-arm ticks) |
| arbitration_habit_uncertainty_source_is_familiarity | -- | true | 1.0 |
| arbitration_weight_uncertainty_coupling | -- | true | 1.0 |

A run whose load-bearing discrimination criterion passes this cleanly, while every readiness/coupling check on
the mechanism itself also passes at or near 100%, should not simultaneously be reading as wholly vacuous. That
contradiction is the tell.

## 2. The bug

Only the range/distinctness readiness fields fail; the actual discrimination (`recruitment_rate`) does not.
Both come from the same aggregation function in `experiments/_lib/baselines/mech477_dualsystem_arbitration.py`:

```python
"recruitment_rate": float(np.mean(recruitments)) if recruitments else None,        # correct
...
"min_full_score_range": float(min(full_ranges)) if full_ranges else 0.0,           # BUG
"min_habit_score_range": float(min(habit_ranges)) if habit_ranges else 0.0,        # BUG
"min_habit_distinct_frac": float(min(habit_distinct_fracs)) if habit_distinct_fracs else 0.0,  # BUG
```

A cell (one arm x seed x condition x layout combination) with **zero scored ticks** has empty `full_ranges` /
`habit_ranges` / `habit_distinct_fracs` lists. `recruitment_rate` correctly reports `None` for such a cell, which
downstream aggregation filters out (`rates = [r["recruitment_rate"] for r in rows if r["recruitment_rate"] is not
None]`). The three range/distinctness fields instead report `0.0` -- indistinguishable from a genuine
degenerate-candidate reading of exactly zero.

**20 of 128 cells (15.6%) scored zero ticks** -- skewed toward the `novel` condition (16/64, 25%) vs `familiar`
(4/64, 6.25%), and `arb_on` (13/64) vs `arb_off` (7/64). This is plausibly just shorter episodes on unpracticed
layouts (not investigated further here), not a substrate defect.

The top-level aggregation (`_worst()`, a deliberate true min-across-cells "so a single out-of-band cell hides
inside an in-band mean") then propagates ANY single zero-tick cell's spurious `0.0` through every level, zeroing
the whole run's readiness verdict for BOTH arms -- regardless of how the other 108/128 (84%) cells read.

## 3. Manual re-derivation (no new run needed)

Re-aggregating the manifest's own per-cell data, excluding only the 20 zero-tick cells, with the identical
worst-case statistic the code intended:

| Gate | Corrected value | Floor | Verdict |
|---|---|---|---|
| worst full_score_range | 0.0022034645080566406 | 1e-6 | **PASS** |
| worst habit_score_range | 9.34302806854248e-06 | 1e-6 | **PASS** (close, but genuinely above floor) |
| worst habit_distinct_fraction | 0.875 | 0.5 | **PASS** |

All three non-vacuity gates clear once the zero-tick cells are correctly excluded rather than contaminating the
minimum with a false zero. This is fully reproducible from the committed manifest alone -- no new experiment was
needed to reach this number.

**Recording-debt vs measurement-debt:** this is measurement debt, not recording debt. All always-core recording
fields are present (`recording_schema=rec/v1`, `substrate_hash`, `machine`/`machine_class`, `elapsed_seconds`,
full `config`, explicit `seeds`) -- `validate_recording.py` finds no gap. The raw per-cell data needed for a
correct verdict was already fully recorded for every non-empty cell; the defect is purely in the aggregation
function's empty-cell default, not in what was captured at run time.

## 4. Claim-layer mapping

**MECH-477** (`dual_system_uncertainty_arbitration`, candidate, `v3_pending=true`, depends_on MECH-163/ARC-071/ARC-007):
registered 2026-07-22 via `/claim-synthesis` decomposition of MECH-163, grounded in Daw/Niv/Dayan 2005 (already
lit-satisfied before registration, conf 0.79, `is_formal_import=false`). SD-081 substrate landed same day. This is
its **first experimental test**. Prior evidence: 0 experimental, 9 lit (inherited via MECH-163's targeted review).

**MECH-163** (`candidate`, narrowed-in-place to leg 1 2026-07-22, `weakens` from 786a): the dual-system-existence
leg. 786 (2026-07-19) was `measurement_test_design_defect` (non_contributory); 786a (2026-07-21, confirmed) found
a genuine flat response but on a **degenerate DV** (later discovered by the SD-081 build itself: the first-step
habit vector was constant across all 32 candidates, so the "flat response" measured tie-break noise, not the
phenomenon) -- yet 786a's own `weakens` still stands because the manipulation check for THAT run passed cleanly;
the degeneracy finding bears on interpretation, not on 786a's own adjudication, which is separate `/governance`
work not touched here.

## 5. Biological-reference triage

Closest mechanism: prefrontal/striatal arbitration between model-based (goal-directed) and model-free (habitual)
control by relative reliability/uncertainty (Daw, Niv & Dayan 2005). Faithful biological translation, not a
formal-definition import -- already reviewed and satisfied inside MECH-163's own lit folder (conf 0.79 primary +
6 corroborating refs: Balleine & O'Doherty 2010, Dolan & Dayan 2013, Niv 2009, Fraser 2023, Miller 2017, Vikbladh
2019) before MECH-477 was even registered. No divergence identified; no new `/lit-pull` owed for the core
grounding (a top-up -- Lee/Shimojo/O'Doherty 2014, Daw 2011 -- is already noted as owed-but-non-blocking on
MECH-477's own record).

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear as labelled / **intact once corrected** | C1 passed 6/7 seeds, d 0.999 ON vs -0.158 OFF |
| Biological reference | clear | Daw/Niv/Dayan 2005, already lit-satisfied, not a formal import |
| Developmental / dependency prerequisites | present | SD-081 landed 2026-07-22, default OFF, bit-identical when OFF |
| Implementation completeness | complete | arbitration_live_non_degenerate 1.0, arb_source 1.0, coupling 1.0 |
| Environment adequacy | adequate | manipulation check AUC 0.848/0.904 vs 0.70 floor; 15.6% zero-tick cells noted, non-blocking |
| Measurement adequacy | **misleading -- the defect** | empty-cell 0.0 default vs correct None on the adjacent field |
| Integration adequacy | coupled, stable | rho_w_vs_relative_uncertainty=1.0 (arithmetic identity, sanity), rho_w_vs_u_habit_alone=0.646 (genuine responsiveness) |
| Scale / capacity | adequate | 8 seeds, robust effect size |

## 7. Re-derive brake / granularity-debt checks

- **Re-derive brake: does not fire.** Neither 786 (`measurement_test_design_defect`) nor 786a (`standard`) nor
  this corrected 811 reading (`measurement_test_design_defect`) carries `recommended_epistemic_category:
  substrate_ceiling` for MECH-163 or MECH-477 -- R3 of the counting convention excludes non-ceiling
  `non_contributory` readings, so no re-queue refusal applies.
- **Granularity-debt trigger: does not need to re-fire.** `scripts/granularity_debt_cluster.py MECH-163` shows 2
  prior targets (786 unclear, 786a weakened). The 2026-07-22 `/claim-synthesis` decomposition already split
  exactly this gap out as MECH-477/478/479. This autopsy is evidence the decomposition correctly identified the
  missing mechanism, not a signal that further splitting is owed.
- **Hypothesis-space registry (Step 9b): skipped deliberately.** No `fanout_recommendation` was emitted (a single
  mechanism test with a diagnosed implementation bug, not a GOV-FANOUT-1 portfolio of >=2 rival hypotheses on
  different design axes), and no existing registry question references MECH-477 or MECH-163. Forcing a new
  rival-hypothesis question into a schema built for discrimination portfolios risked a low-quality entry; left
  unregistered rather than mis-populate the frozen ledger. Flag for human override if this reading is wrong.

## 8. Learning extracted

1. The non-vacuity gate's empty-cell default (`0.0`) is inconsistent with the adjacent `recruitment_rate`
   field's correct default (`None`) in the same aggregation function -- an implementation gap, not a substrate
   or biology gap.
2. The manifest's own per-cell data was rich enough to re-derive a corrected verdict without a fresh run, because
   the bug is a pure aggregation-default defect and the raw per-tick data was genuinely computed for non-empty
   cells.
3. MECH-477 (SD-081 arbitration) has its first genuine, robust experimental support once the false self-route is
   corrected -- the Daw/Niv/Dayan biological translation is working as designed.
4. Zero-tick cells cluster in the novel condition and `arb_on` arm (secondary, non-blocking observation) -- worth
   a footnote for whoever designs V3-EXQ-811a.

## 9. Interactive gate (user confirmed 2026-07-24)

- **811's own verdict:** reclassify now from the manual re-derivation (not gated on a fresh re-run) -- the
  re-derivation is fully reproducible from the committed manifest alone.
- **MECH-163 weighting:** the OFF-arm flat response gets **no additional weight** on MECH-163 -- it is a
  necessary control for the MECH-477 test, not an independent fair test of MECH-163's already-narrowed leg-1
  claim. Record as context alongside 786a's existing `weakens`, not as a second data point.
- **Bug-fix routing:** `/queue-experiment` same-question alphabetic-suffix re-run (**V3-EXQ-811a**) with the
  aggregation bug fixed, so a clean manifest exists going forward -- even though 811's own verdict is already
  settled by this autopsy's re-derivation.

## 10. Repair pathway

- **Routing: `/queue-experiment`** -- same scientific question, implementation-only fix (empty-cell default
  `0.0` -> `None` + exclude, matching the already-correct `recruitment_rate` pattern in the same function), new
  letter **V3-EXQ-811a**, not a new EXQ number.
- **`recommended_substrate_queue_entry.action = "none"`** -- no substrate gap; SD-081 works as designed. This is
  a script-level bug in `experiments/_lib/baselines/mech477_dualsystem_arbitration.py`, not a substrate need.
- **Draft `evidence_quality_note`** (for governance to apply, verbatim available in the JSON artifact): applies
  `supports` to MECH-477 (first genuine experimental evidence; `v3_pending` gate should be reconsidered), and
  records this run as `non_contributory` / no-additional-weight context for MECH-163.

## Machine-readable artifact

See `failure_autopsy_V3-EXQ-811_2026-07-24.json` (schema `failure_autopsy/v1`) in this directory.
