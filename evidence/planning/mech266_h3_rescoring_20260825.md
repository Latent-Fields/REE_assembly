# H3 re-scoring -- V3-EXQ-464e / V3-EXQ-467e (mech266_mode_arbitration_saturation)

- **Generated (UTC):** 2026-08-25T10:53:11Z
- **Scope:** zero-cost re-analysis of banked data. No new run.
- **Session:** mech-266-rescore-circling-2d31ca (worktree)
- **Question:** `mech266_mode_arbitration_saturation`, leg **H3-instrument-illposed**
- **Probe:** exactly the one pre-registered in `failure_autopsy_mech266-464e-467e-cluster_2026-08-13`
  Section on the GOV-FANOUT-1 portfolio and restated in the question's `decision.live_gate`:
  *"re-score banked 464e/467e data: per-arm occupancy gate conditioned on regime +
  occupancy-conditioned dwell. No new run required."* **Declared null: re-scoring changes no
  verdict.**

This leg had never actually been executed. `hypothesis_space_registry.v1.json` H3's
`adjudicating_runs` is `[]` and its `resolving_runs` lists only `V3-EXQ-935` -- a *new
experiment* that incidentally exercised a corrected instrument, not a re-scoring of the
original 464e/467e banked data this leg was pre-registered against. This document is that
re-scoring.

---

## 1. Method

Both targets' full per-seed banked data (flat manifest, `per_seed` array -- `mean_dwell`,
`n_switches`, `fraction_in_external_task`, `n_runs`, `total_steps`, `n_episodes` per
arm/ratio-cell) already exist in `evidence/experiments/`:

- `v3_exq_464e_mech266_competing_goals_behavioural_20260813T020141Z_v3.json`
- `v3_exq_467e_mech266_mode_stickiness_behavioural_20260813T001847Z_v3.json`

No simulation was re-run; every number below is a recomputation over these existing fields.

**M1/M2 fix -- readiness (occupancy non-vacuity) gate.** The banked gate computes
`min()` of `fraction_in_external_task` across ALL arms (464e) or ALL ratio arms (467e) per
seed. As the original autopsy's Section 2/3 argued qualitatively, this conflates "mode
unreachable" with "mode reachable but saturated/bimodal", and for 467e is anti-correlated
with the effect under test (a stronger hysteresis effect drives occupancy toward 0 at loose
rails, which is what the gate penalizes). The corrected gate is **regime-conditioned**:
occupancy is read on the single arm/ratio the mechanism actually predicts should show it --
`ARM_ASYM_STICKY_TASK` for 464e, `r=0.10` (tightest rail) for 467e -- rather than minimised
across a range deliberately swept to cross the transition.

**M3 fix -- dwell statistic.** The banked `mean_dwell` accumulates run lengths across ANY
mode change (`_eval_mode_dwell`, `ree-v3/experiments/v3_exq_467e_..._behavioural.py:403-455`),
so it is a valid `external_task`-dwell reading only when the cell is single-mode (occupancy at
or above a ceiling, taken here as 0.9 by symmetry with the existing 0.1 floor). Below the
floor, the recorded `mean_dwell` describes whichever OTHER mode dominates (`internal_planning`
in every case the banked data can confirm -- see Limitation below) and must be excluded from
an `external_task`-dwell comparison rather than compared as if commensurable. Cells strictly
between floor and ceiling are `MIXED`: genuinely graded in principle, but **not decomposable**
from the banked aggregate-only fields (no per-mode-tagged run-length list was recorded), so
they are reported as `undecomposable`, not silently assigned to either mode.

**Limitation, stated rather than assumed away.** 464e's manifest carries `mode_step_counts`
per arm, confirming `internal_replay` and `offline_consolidation` are 0 throughout (only
`external_task` / `internal_planning` are ever occupied). 467e's manifest does not record
`mode_step_counts`, only `fraction_in_external_task`; "the non-`external_task` steps are
`internal_planning`" is inferred by analogy to 464e (same substrate, same commit lineage
modulo an `experiment_queue.json` snapshot -- see the original autopsy's dry-run-gate section),
not independently confirmed for 467e. This does not affect the readiness-gate recomputation
(which only reads `fraction_in_external_task`) or the occupancy-monotonicity check below (same
reason); it affects only the *labelling* of which mode 467e's excluded dwell cells belong to.

---

## 2. Results -- V3-EXQ-464e

### Readiness gate

| seed | sym occ | sym class | sticky occ | sticky class | OLD (min-gate) reachable | NEW (regime-conditioned) reachable |
|---|---|---|---|---|---|---|
| 42 | 0.0000 | unreachable | 1.0000 | saturated | **False** | **True** |
| 43 | 0.0000 | unreachable | 1.0000 | saturated | **False** | **True** |
| 44 | 0.4331 | mixed | 1.0000 | saturated | True | True |

- OLD `occupancy_non_vacuity_fraction` = 0.3333 (threshold 0.6667) -> **NOT MET**
  (`route_reason: external_task_mode_not_occupied`)
- NEW `occupancy_non_vacuity_fraction` = **1.0000** (threshold 0.6667) -> **MET**

**Verdict change: the readiness gate flips from NOT MET to MET.** Under regime-conditioning,
the mode is reachable on 3/3 seeds, not 1/3. `route_reason:
external_task_mode_not_occupied` does not survive re-scoring for this run.

### Load-bearing criteria (C1/C2)

C1 (`asym_task_occupancy > sym`) and C2 (`asym_switches <= sym`) are already per-arm
comparisons and use neither `mean_dwell` nor the min-gate, so M1/M3 do not apply to them
directly. Recomputed directly from the banked per-seed fields (not just the recorded flags),
they are **unchanged**:

| seed | C1 (recomputed) | C1 (recorded) | C2 (recomputed) | C2 (recorded) | maximal-separation (0/1) |
|---|---|---|---|---|---|
| 42 | True | True | True | True | **True** |
| 43 | True | True | True | True | **True** |
| 44 | True | True | True | True | False |

No change: both criteria pass 3/3 both before and after correction, and 2/3 seeds remain
flagged maximal-separation (matches the manifest's own `criteria_non_degenerate: {C1: false,
C2: false}` -- i.e. every seed independently reads as degenerate, consistent with the driver's
own vacuous-pass flag).

---

## 3. Results -- V3-EXQ-467e

### Readiness gate

| seed | occ-by-r `[0.1, 0.5, 1.0, 1.5, 2.0]` | OLD (min-gate) reachable | NEW (r=0.10) reachable |
|---|---|---|---|
| 42 | `[1.0, 0.0, 0.0, 0.0, 0.0]` | **False** | **True** |
| 43 | `[0.8073, 0.0, 0.0, 0.0, 0.0]` | **False** | **True** |
| 44 | `[1.0, 0.0, 0.0, 0.0, 0.0]` | **False** | **True** |

- OLD `occupancy_non_vacuity_fraction` = 0.0000 -> **NOT MET**
- NEW `occupancy_non_vacuity_fraction` = **1.0000** -> **MET**

**Verdict change: the readiness gate flips from NOT MET (0/3) to MET (3/3).** The original
"not occupied" read was an artifact of requiring occupancy above floor at *every* rail
including the loosest (r=2.00) -- exactly the M2 defect (a gate anti-correlated with its own
predicted effect).

### Load-bearing criteria (C1/C2), occupancy-conditioned dwell

| seed | valid (saturated) external_task cells | count | C1/C2 decidable? |
|---|---|---|---|
| 42 | `{r=0.10: dwell=119.667}` | 1 | **No -- undecidable** (need >= 2 same-regime points) |
| 43 | `{}` (r=0.10 is `mixed`, occ=0.8073, undecomposable) | 0 | **No -- undecidable** |
| 44 | `{r=0.10: dwell=184.583}` | 1 | **No -- undecidable** (need >= 2 same-regime points) |

Every other cell (`r>=0.5`, all seeds) is `unreachable` (occ=0.0) and its recorded
`mean_dwell` describes `internal_planning`, not `external_task` -- excluded, not compared.

**Verdict change: C1 (`dwell_monotone_non_increasing_in_r`) and C2
(`low_r_dwell_ge_ratio_times_high_r`) move from a recorded definite FAIL (3/3 seeds) to
UNDECIDABLE (3/3 seeds) under occupancy-conditioned dwell.** This is not a flip to PASS -- it
is a flip to *no comparison is available*, because at most one ratio per seed ever has a
genuine external_task-dwell reading. The original FAIL was produced by comparing `external_task`
dwell at r=0.10 against `internal_planning` dwell at r>=0.50 (exactly M3, confirmed
mechanically here rather than only argued qualitatively).

### Occupancy itself, as a regime-agnostic-safe DV

Unlike dwell, `fraction_in_external_task` is unambiguous regardless of which mode dominates
(it does not need mode-conditioning). Monotonicity in occupancy:

| seed | occ-by-r | monotone non-increasing |
|---|---|---|
| 42 | `[1.0, 0.0, 0.0, 0.0, 0.0]` | True |
| 43 | `[0.8073, 0.0, 0.0, 0.0, 0.0]` | True |
| 44 | `[1.0, 0.0, 0.0, 0.0, 0.0]` | True |

Holds trivially on all 3 seeds -- any step-down function is monotone. Recorded here because it
is the one C1-shaped statistic the banked data CAN decide cleanly, but flagged explicitly as
uninformative: it cannot discriminate graded arbitration (H1) from structural bang-bang (H2),
which is exactly what V3-EXQ-935's later dose-response sweep was needed to settle (H2
subsequently eliminated, `failure_autopsy_V3-EXQ-935_2026-08-18`).

---

## 4. Does the declared null survive? No.

H3's declared null was **"re-scoring changes no verdict."** It is refuted on both targets:

1. **Readiness/routing layer (both 464e and 467e):** the non-vacuity gate flips NOT-MET ->
   MET. `route_reason: external_task_mode_not_occupied` -- the stated *cause* of both runs'
   `substrate_not_ready_requeue` self-route -- does not survive regime-conditioning. This
   directly confirms, with a recomputed number rather than only narrative argument, Section 2
   of the original cluster autopsy ("the self-route is factually wrong").
2. **467e's load-bearing criteria:** flip from a definite FAIL (3/3 seeds, both C1 and C2) to
   UNDECIDABLE (3/3 seeds) under occupancy-conditioned dwell. The original FAIL read was an
   artifact of comparing dwell across mismatched modes, not evidence against a graded
   hysteresis effect.
3. **464e's load-bearing criteria are unchanged** (pass 3/3, degenerate 2/3 both before and
   after) -- these never depended on `mean_dwell` or the min-gate, so M1/M3 correctly do not
   touch them. Not every verdict in the cluster was an instrumentation artifact; only the
   readiness/routing layer on both runs, and 467e's dwell-based criteria specifically.

**Reading for H3 (instrumentation ill-posed):** supported, on the SPECIFIC banked data this
leg was pre-registered against. This is complementary to, not redundant with, the existing
2026-08-18 basis update (which found V3-EXQ-935's own corrected instrument still uncovered
real graded structure, so "instrument ill-posedness is not the whole story"). Both are true
at once: the ORIGINAL 464e/467e instrument was genuinely defective in the ways M1/M2/M3
identified (this document), AND a properly-conditioned NEW measurement (935) still finds a
real, cap-dependent, graded effect underneath the correction. H3 stays `alive`, neither
eliminated nor the sole explanation -- this closes out the one specific test ("re-score
banked data") the leg was defined by, on the data it was defined against, rather than leaving
it permanently untested while a different run (935) accumulates against `resolving_runs`.

**Answer to the question's `decision.distance_phrase`** ("One zero-cost re-scoring (H3) away
from knowing whether the substrate question is even well-posed"): **yes, well-posed** -- the
readiness gate correctly reads the mode as reachable on both runs once regime-conditioned, and
464e's criteria (unaffected by the identified defects) are a genuine, if degenerate,
maximal-separation pass. The substrate question was never "is there anything here to measure"
(the original gate's answer); it is "is what's there graded or structural" -- which is exactly
what H1/H2 (and V3-EXQ-935) went on to address independently of this re-scoring.

---

## 5. Recommended registry update (not applied by this document)

Append to `H3-instrument-illposed.resolution.basis` in
`evidence/planning/hypothesis_space_registry.v1.json`, dated, citing this file -- following
the existing pipe-separated append convention. `state` stays `alive` (unchanged: neither
eliminated -- real defects confirmed -- nor confirmed as sole cause -- 935 already showed
graded structure survives correction too). No claim-layer (`claims.yaml`) disposition change
is proposed here; that is `/governance` territory and is left to the next cycle to apply or
decline, per the standing chip-scope rule (`CLAUDE.md` Housekeeping).
