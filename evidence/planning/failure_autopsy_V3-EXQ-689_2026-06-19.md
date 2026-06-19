# Failure Autopsy -- V3-EXQ-689 (MECH-439 F-dominance conflict-grade 2x2 falsifier)

- **Generated (UTC):** 2026-06-19T19:12:42Z
- **Run:** `v3_exq_689_mech439_conflict_grade_2factor_falsifier_20260619T185949Z_v3` (machine ree-cloud-2)
- **Queue:** V3-EXQ-689 (experiment_purpose=evidence; MECH-439's FIRST falsifier)
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `non_degenerate: true`
- **Self-route:** `substrate_not_ready_requeue` (a `precondition_unmet` flag -- adjudicated here)
- **Status:** confirmed (interactive, user-ratified 2026-06-19)

---

## 1. Facts -- reconstruction (no interpretation)

A 2x2 conflict-grade treatment grid + 2 controls on the GAP-A-ready foraging substrate
(SD-056 online-trained `e2.world_forward` + ARC-065 GAP-A `candidate_summary_source=e2_world_forward`
+ route-range routing + top-k shortlist), 3 seeds x 6 arms.

- **Factor A** -- conflict-graded shortlist width: `k = clamp(round(k_max - (k_max-1)*gap_norm), 1, K)` (k_max=6).
- **Factor B** -- gap-scaled entropy-regularized commit: `T_eff = base_T + 1.5*(1 - gap_norm)` (peak 2.5).
- `gap_norm` = normalized top-F gap (best-vs-second-best primary score) in [0,1]; bin 0 = near-tie, bin 3 = decisive.

### Gates (ARM_A1B1 = both levers ON, the PRIMARY cell)

| Gate | Statistic | Value | Threshold | Met? |
|---|---|---|---|---|
| Readiness (a) route-range | `modulatory_channel_route_range_mean` | 0.566 | 0.01 | YES |
| Readiness (b) e2 divergence | `cand_world_pairwise_dist_mean` | 0.164 | 0.03 | YES |
| Readiness (c) **grading non-vacuity** | k varies / T_eff varies / **gap spans >=3 bins** | k 3/3, T_eff 3/3, **gap_spread 0/3** | -- | **NO** |
| C1 e2-divergent | load-bearing | -- | -- | PASS |
| C_PRIMARY entropy strict-above BOTH controls | seeds >=2/3 | 2/3 | 2/3 | PASS |
| **C_FGAP** lift correlates with F-gap | load-bearing falsifier | `fgap_computable=false`, bins_used=2 | slope over >=3 bins | **FAIL (uncomputable)** |

`readiness_ok=False` (grading non-vacuity failed) -> the verdict resolver self-routes
`substrate_not_ready_requeue` before any criterion verdict is reached.

### The failed precondition, in detail

`gap_spread_seeds = 0` (needed >=2 seeds with `n_populated_gap_bins >= GAP_MIN_POPULATED_BINS=3`).
ARM_A1B1 `gap_bin_tick_counts` (bins are [near-tie ... decisive]; a bin counts only at >=50 ticks):

| seed | bin0 | bin1 | bin2 | bin3 | populated |
|---|---|---|---|---|---|
| 42 | 321 | 36 | 4 | 1 | 1 |
| 43 | 3706 | 92 | 11 | 0 | 2 |
| 44 | 119 | 11 | 5 | 9 | 1 |

The top-F gap is **pinned in the near-tie bin** on all three seeds. Only 1-2 bins clear the
50-tick floor; never 3 -> the per-gap-bin entropy regression has no x-axis spread -> C_FGAP is
uncomputable (`a1b1_gap_bins_used=2`, `fgap_computable=false`).

### Committed-entropy detail (the fragile C_PRIMARY)

`selected_action_class_entropy` per seed:

| seed | PROPOSER_CTRL | MATCHED_NOISE | ARM_A1B1 | A1B1 strict-above both? |
|---|---|---|---|---|
| 42 | 1.129 | 1.129 | **1.426** | YES (genuine lift) |
| 43 | 0.0047 | 0.0047 | **0.0182** | YES (near-zero -> near-zero, technical; A1B1 = 3799/3809 ticks one class) |
| 44 | 0.817 | 0.817 | **0.427** | NO (regression -- below control) |

`MATCHED_NOISE` (proposer source @ flat T=2.5) produced **identical** committed entropy to
`PROPOSER_CTRL` -> a hot flat softmax over the collapsed channel does **not** lift
(`negative_control_does_not_lift=true`). ARM_A1B1 mean entropy 0.624 is actually **below** the
control mean 0.650; C_PRIMARY passes only on the per-seed strict-above count, which is fragile.

---

## 2. Claim-layer mapping

**MECH-439** (`claims.yaml`): `claim_type: mechanism_hypothesis`, `status: candidate`,
`epistemic_category: standard` (explicit -- the claim's own notes assert *"V3-tractable now ... this
is testable, NOT substrate_ceiling"*), `implementation_phase: v3`.

The claim's **own pre-registered falsifier** maps directly onto C_PRIMARY: *"a selection lever that
lifts committed-action-class entropy strict-above BOTH collapsed-proposer and matched-noise controls
on >=2/3 seeds WITHOUT reducing F's E3 variance share refutes the F-monopoly framing; conversely,
persistent flat committed entropy under any diversity channel while F-share stays >0.85 supports it."*

So a clean C_PRIMARY 2/3 strict-above-both would be a **refutation** signal. But (a) the experiment
gates readiness FIRST, so it never reached a verdict; (b) the 2/3 is fragile (1 genuine, 1 technical,
1 regression); and (c) the load-bearing C_FGAP check that distinguishes *real conflict-grading*
(gap-concentrated) from a *uniform lift* (bigger fixed shortlist / hotter flat softmax) is
**uncomputable**. The experiment therefore neither supports nor refutes MECH-439.

**`claim_ids` accuracy:** `claim_ids=[MECH-439]` only -- correct. ARC-065/MECH-341/ARC-062/MECH-309/
MECH-294 are depends_on, untouched. This is the **first autopsy to TARGET MECH-439** (the 445h and
485g autopsies, both 2026-06-19, only *reference* MECH-439 as the upstream conversion-ceiling cause of
their own floor-locked criteria; they target SD-032b / MECH-258 / MECH-260 / ARC-058 / SD-033b). No
granularity-debt recurrence.

---

## 3. Biological-reference triage

Closest mammalian mechanism: **BG hyperdirect (STN) conflict-graded commitment threshold** -- the STN
raises the decision threshold under response conflict / near-ties (Frank 2006; Cavanagh & Frank 2011),
exactly the "grade the committed decision by the normalized top-F gap" principle the two levers render.
Faithful biological translation (not a formal-definition import); the class has a working existence
proof. The failure resembles **no** missing-dependency biological signature -- it is a measurement /
test-design gap, not a translation gap.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact (untested at load-bearing level) | C_FGAP uncomputable; C_PRIMARY fragile. Neither supported nor weakened. |
| Biological reference | clear | BG hyperdirect conflict-grade (Frank 2006 / Cavanagh 2011). |
| Prerequisites | present | route-range 0.566, e2 pairwise_dist 0.164, C1 divergent -- all met. |
| Implementation | complete (levers fire) | `k_effective` varied 3/3, `t_eff` varied 3/3 -- both factors engaged. |
| **Environment** | **wrong pressure (the gap)** | foraging F-gap pinned near-tie; no decisive-vs-tie variation. |
| **Measurement** | **under-instrumented for the falsifier** | C_FGAP needs >=3 gap bins; near-tie regime gives <=2. Readiness gate conflated "levers engaged" with "falsifier computable." |
| Integration | coupled | levers compose with the GAP-A stack. |
| Scale | adequate | P0=60 (proven 569i budget); thousands of P1 ticks. Higher P0 cannot open an ecology-pinned gap. |

**Dominant diagnosis: environment + measurement (test-design).** The self-route's stated cause
("monostrategy-pinned gap -> grading could not act") is **wrong** -- the grading DID act. The true
cause is the foraging F-gap is structurally concentrated in the near-tie bin, which is **itself a
manifestation of the F-dominance MECH-439 asserts** (F monopolizes selection -> candidates near-tied
in F most of the time). The test design did not anticipate that the phenomenon under test would
collapse the gap-distribution its own falsifier requires.

`recommended_epistemic_category: standard` (UNCHANGED -- the substrate works; the claim is explicitly
V3-tractable, not substrate_ceiling).

---

## 5. Learning extracted

1. The conflict-grade levers **engage** on the GAP-A-ready foraging substrate -- both factors vary 3/3.
2. ARM_A1B1 committed entropy lifts strict-above both controls on 2/3 seeds (partial positive), but
   **fragile** (1 genuine / 1 near-zero technical / 1 regression) and **not** the load-bearing falsifier.
3. The load-bearing C_FGAP falsifier (gap-concentrated vs uniform lift) is **uncomputable** -- the
   foraging F-gap is pinned in the near-tie bin (<=2 populated bins; slope needs >=3).
4. The near-tie gap concentration is itself a manifestation of the F-dominance under test.
5. The self-route prescription ("re-queue at higher P0") is **misdirected** -- compute cannot open an
   ecology-pinned gap.
6. **Readiness-gate lesson (generalisable):** the grading-non-vacuity precondition bundled "levers
   engaged" (k/T_eff vary) with "falsifier computable" (gap spans >=3 bins). These should be separate
   gates; a levers-engaged + falsifier-uncomputable run should route to measurement-redesign, never
   `substrate_not_ready_requeue`.

---

## 6. Repair pathway + routing (user-ratified)

**Routing: `/queue-experiment` redesign -- V3-EXQ-689a (supersedes V3-EXQ-689).** Same scientific
question (MECH-439's first falsifier); the implementation/measurement is redesigned so C_FGAP becomes
computable on the F-dominated foraging regime.

- **NOT** `/implement-substrate` (substrate works; MECH-439 is `standard`/V3-tractable, not
  `substrate_ceiling`; `recommended_substrate_queue_entry.action = none`).
- **NOT** governance demotion (load-bearing falsifier unevaluated; the partial C_PRIMARY is ambiguous).
- **NOT** `/diagnose-errors` (ran to completion, clean).
- **NOT** re-queue at higher P0 (the manifest self-route prescription -- misdirected).

### 689a redesign spec

**LEAD mechanism -- gap-blind control arms (user-selected):** add `ARM_FIXED_KMAX` (k pinned at
k_max=6, gap-blind) and `ARM_FIXED_HOT_T` (T pinned at the peak base+alpha=2.5, gap-blind -- distinct
from `MATCHED_NOISE`, which keeps the *collapsed proposer* source). conflict-grade is load-bearing
**iff** ARM_A1B1 (gap-SCALED both levers) beats BOTH gap-blind controls. If a fixed-large-k /
fixed-hot-T arm lifts committed entropy as much as the gap-scaled version, the lift is **not**
conflict-grading -- this is the arm-contrast that **sidesteps the uncomputable per-gap-bin regression**.
(`MATCHED_NOISE` already showed flat-T over a collapsed channel doesn't lift; the missing piece is a
fixed-k=6 control for Factor A.)

**Supporting (secondary):**
- Quantile-adaptive gap binning (bins by gap quantiles matched to the near-tie distribution, so even a
  concentrated gap yields >=3 populated bins) -- retains the regression falsifier as a secondary readout.
- Decouple the readiness gate: separate "levers engaged" from "gap-spread for the regression" so a
  levers-engaged + regression-uncomputable run routes to measurement-redesign, not a P0 re-queue.

**Non-vacuity preserved:** keep the route-range + e2-divergence + levers-engaged readiness gates;
below floor still self-routes `substrate_not_ready_requeue` (never a false weakens).

### Draft `evidence_quality_note` for governance (do NOT write here; `/governance` applies it)

> V3-EXQ-689 (MECH-439 FIRST falsifier) self-routed substrate_not_ready_requeue on the
> grading-non-vacuity precondition (gap_spread 0/3 seeds; F-gap pinned in the near-tie bin,
> a1b1_gap_bins_used=2 < 3). ADJUDICATED (failure_autopsy_V3-EXQ-689_2026-06-19) as a
> test-design/measurement gap, NOT substrate-under-trained: the GAP-A readiness preconditions PASSED
> (route_range 0.566, e2 pairwise_dist 0.164, C1 divergent) and BOTH conflict-grade levers ENGAGED
> (k_effective varied 3/3, t_eff varied 3/3). The failed precondition's stated cause
> ('monostrategy-pinned gap') is wrong: the grading DID act; the true cause is the foraging F-gap is
> structurally concentrated in the near-tie bin, so the load-bearing C_FGAP gap-correlation falsifier
> (real conflict-grading vs uniform bigger-k/hotter-T lift) is UNCOMPUTABLE. This near-tie
> concentration is itself a manifestation of the F-dominance MECH-439 asserts. C_PRIMARY passed 2/3
> but FRAGILE (seed42 genuine 1.426 vs 1.129; seed43 near-zero->near-zero technical 0.0182 vs 0.0047;
> seed44 a REGRESSION 0.427 vs 0.817); matched-noise flat-T did not lift. Re-queue at higher P0 will
> NOT fix an ecology-pinned gap. Routed /queue-experiment (V3-EXQ-689a redesign): LEAD with gap-BLIND
> control arms (FIXED-k_max + FIXED-peak-T at matched magnitude) so 'gap-concentrated vs uniform lift'
> is an arm contrast; supporting: quantile-adaptive gap binning + decouple 'levers engaged' from
> 'falsifier computable' in the readiness gate. MECH-439 stays candidate / standard / V3-tractable --
> neither supported nor weakened (load-bearing falsifier unevaluated).

---

## 7. Routing summary

| Field | Value |
|---|---|
| failed_criterion | readiness precondition (grading non-vacuity; gap-spread) |
| self-route adjudication | precondition unmet, but its STATED CAUSE is wrong (levers engaged; ecology-pinned gap) |
| dominant diagnosis layer | environment + measurement (test-design) |
| biological-reference verdict | clear (BG hyperdirect conflict-grade; faithful) |
| recommended evidence_direction | non_contributory (corrected note) |
| recommended epistemic_category | standard (unchanged) |
| pending_retest_after_substrate | false |
| narrow_supports_flag | false |
| routing | /queue-experiment -> V3-EXQ-689a (gap-blind control arms) |
| claim disposition | MECH-439 stays candidate -- neither supported nor weakened |
