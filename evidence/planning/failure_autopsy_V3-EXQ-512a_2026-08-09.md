# Failure Autopsy — V3-EXQ-512a re-adjudication (SD-048's sole supporting evidence)

**Generated:** 2026-08-09T07:41:14Z
**Scope:** single (re-adjudication of a standing PASS, per chip `chip-20260809-v3exq512a-reexamination`)
**Status:** confirmed (interactive gate run 2026-08-09 — user confirmed reclassifying `supports` -> `non_contributory`)

## 0. Why this autopsy exists

`failure_autopsy_V3-EXQ-902_2026-08-09` found that the C2/`quiet_gap` statistic used across
SD-048's whole evidence lineage (511/512/512a/902) collapses to a tautology whenever the
"quiet" comparison bucket is empty (`n_quiet_steps=0` -> `_safe_mean([]) == 0.0` -> the gap
reduces to `residual_body_noise - 0.0`, i.e. it reports the residual itself, not a real
comparison). That autopsy identified V3-EXQ-512a as carrying the identical signature in all 3
seeds but explicitly deferred re-adjudicating it (out of scope for that pass) and flagged it
for a follow-up. This autopsy is that follow-up.

## 1. Facts

**Manifest**: `v3_exq_512a_sd048_comparator_gap_recalibrated_20260504T093916Z_v3`
(`REE_assembly/evidence/experiments/v3_exq_512a_sd048_comparator_gap_recalibrated_20260504T093916Z_v3.json`
— predates the per-run `runs/` pack convention; the `runs/` pack for this run_id exists but
carries a stub-only `manifest.json`/empty `metrics.json`, so the flat file is the substantive
record). `claim_ids: ['SD-048']`, `experiment_purpose: evidence`, `result: PASS`,
`evidence_direction: supports`, `supersedes: v3_exq_512_..._20260504T005756Z_v3` (V3-EXQ-512,
which FAILED C3 at default scale=1.0).

**Driver**: `ree-v3/experiments/v3_exq_512a_sd048_comparator_gap_recalibrated.py`. Two arms, 3
seeds each (42/43/44). ARM_A: SD-048 on, `interoceptive_noise_scale=3.0` (3x default). ARM_B:
SD-048 off (sanity baseline). Pre-registered interpretation grid (script docstring, lines
32-51): **PASS = C1 AND C2 AND C3** -> "Mechanism confirmed... Evidence direction: supports
(mechanism proof, not calibration proof)". **FAIL (C1 or C3 fails)** -> routes ARC-058/ARC-033
toward `substrate_conditional`. C2 (ARM_B forward_r2 sanity) is uncontested and not examined
further here — its role is only to confirm the forward model can learn the substrate at all
when SD-048 is off; it says nothing about self/other discrimination.

Criteria as coded (`_evaluate`, lines 400-406):
- **C1** `selectivity_gap = residual_body_noise - residual_agent > 0.0`, required on
  `ceil(3 * 2/3) = 2` of 3 seeds.
- **C2** ARM_B `forward_r2 >= 0.5` on 2/3 seeds (uncontested, both arms clear R^2~0.97-0.99).
- **C3** `(residual_body_noise - residual_quiet) >= 0.005` AND `n_body_noise_steps > 0`, on 2/3
  seeds.

**Verified directly against the manifest's per-seed `results_arm_a_sd048_on` array** (not taken
on 902's word):

| seed | n_body | n_agent | **n_quiet** | res_body | res_agent | **res_quiet** | selectivity_gap (C1) | quiet_gap (C3) |
|---|---|---|---|---|---|---|---|---|
| 42 | 298 | 114 | **0** | 0.058497 | 0.057024 | **0.0** | +0.001472 (pass) | 0.058497 (pass) |
| 43 | 270 | 115 | **0** | 0.060795 | 0.061461 | **0.0** | **-0.000666 (FAIL, wrong sign)** | 0.060795 (pass) |
| 44 | 305 | 115 | **0** | 0.042958 | 0.040853 | **0.0** | +0.002105 (pass) | 0.042958 (pass) |
| mean | | | | | | | **+0.000971** | **+0.054083** |

`_safe_mean` (driver lines 355-356): `return float(sum(xs)/len(xs)) if xs else 0.0`. With
`res_quiet = []` in all three seeds (`n_quiet_steps=0`), `mean_quiet = _safe_mean([]) = 0.0`
exactly — bit-identical to the manifest's `residual_quiet: 0.0` in every seed. **C3 as coded is
therefore `residual_body_noise - 0.0 >= 0.005`, i.e. "is the forward-model residual under
noise bigger than 0.005" — not a comparison against any actual undisturbed-tick data**, because
there is no undisturbed-tick data left at scale=3.0. This is the identical defect V3-EXQ-902
found in its own ARM_3 (scale=4.0x), confirmed here by direct inspection of 512a's own raw
per-seed numbers and driver source rather than by extension from 902's finding.

C3's 3/3 "pass" carries no information: `residual_body_noise` (a forward-model prediction
residual under active noise injection) is essentially guaranteed to clear an absolute
0.005 floor whenever noise is injected at all — it is not testing whether the comparator can
tell a noise-tick apart from a quiet tick, because C3's own quiet operand is a placeholder, not
a measurement.

**C1 is the only load-bearing criterion the defect does not touch** (it compares body-noise
residual against agent-caused residual, both non-empty buckets: n_body=270-305, n_agent=
114-115). It is thin: mean effect **0.00097**, roughly 1.5-2% of the residual magnitudes
themselves (~0.043-0.061); 2 of 3 seeds pass, exactly at the required minimum fraction
(`ceil(3*2/3)=2`); and **seed 43's sign is reversed** (agent-caused residual is *larger* than
body-noise residual at that seed) — the sole seed the mechanism should discriminate most
cleanly on, since it has the most body-noise steps (270) relative to agent steps (115) of the
three.

**Dry-run check**: `check_dry_run_citations.py` on both `v3_exq_512a_..._v3` and
`v3_exq_902_..._v3` -> `2 clean, 0 dry cited`. Neither run is a smoke.

## 2. Claim-layer mapping

SD-048 (`design_decision`, `candidate`, `v3_pending: true`, `epistemic_category: standard`).
`claims.yaml`'s own `what_would_answer` already documents 512a as "a first confirming data
point" pending the still-unrun default-scale calibration sweep (which V3-EXQ-902 turned out to
be, and which itself FAILED at ARM_2/default on the same defective criterion). The governance
note (2026-08-09, post-902) already states: "V3-EXQ-512a's standing supports verdict rests on
the IDENTICAL n_quiet_steps=0 artifact and needs its own re-examination... SD-048's evidentiary
basis is currently resting on a statistic that may not have been measuring what it claims to at
the one scale where it 'worked'." This autopsy performs that re-examination.

Per the driver's own pre-registered grid, **PASS requires C1 AND C3 together** — the design
never contemplated "C3 passes because there is no quiet-bucket data to compare against."
Removing C3 as invalidated leaves the pre-registered grid's own conjunction unsatisfied; this
is not a case where a secondary/incidental criterion can be dropped and the primary one still
carries the verdict, because C1 and C3 were both designed as necessary, independent legs of the
architectural claim (self-vs-agent discrimination, and body-noise-vs-quiet discrimination).

`claim_alignment: unclear` — the deciding criterion (C3) did not let the claim express itself
at all (it measured nothing at scale=3.0), and the one intact criterion (C1) is too thin and
sign-inconsistent across seeds to independently establish discrimination.

## 3. Biological-reference triage

Same reference as 902: von Holst & Mittelstaedt (1950) reafference principle / corollary
discharge; cerebellar forward-model literature (Wolpert/Miall/Kawato); interoceptive-predictive-
coding accounts of allostasis (Seth, Barrett, Craig); self-tickling attenuation / corollary-
discharge dysfunction in psychosis (Blakemore/Frith, Ford & Mathalon). Literature present:
`evidence/literature/targeted_review_reafference_streams/`, 6 entries, `literature_confidence
0.86`. No divergence identified — a signal-detection-theoretic requirement (self/other
discrimination only above a detectability floor) is itself biologically expected, not evidence
the mechanism is misconceived. No new `/lit-pull` warranted; this is an instrument problem, not
a biology problem.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | C3 measured nothing at this scale (tautological); C1 alone too thin/sign-inconsistent to carry the verdict |
| Biological reference | present | von Holst/Mittelstaedt; 6 lit entries, conf 0.86; no divergence |
| Dependency prerequisites | present | SD-011, SD-022 implemented; precondition confirmed operationally by 511/512/512a |
| Implementation completeness | complete (substrate) / defective (measurement) | env noise injection + event tagging works as documented; C3's `_safe_mean`-without-n-guard is the defective part, identical to 902 |
| Environment adequacy | inadequate for C3 at this scale | at scale=3.0 the noise generator's own trigger-frequency scaling empties the quiet-tick bucket (same mechanism as 902's ARM_3) |
| Measurement adequacy | structurally flawed (C3) / marginal (C1) | C3 is a tautology; C1 is real but has an effect size (~2% of residual magnitude) and seed count too small to be decisive on its own |
| Integration adequacy | coupled, not implicated | C2/ARM_B sanity clean (R^2 0.97-0.99 both arms) |
| Scale/capacity | not the locus of the problem | this is a criterion-design issue, not a representational-capacity issue |

## 5. Adjudication

The experiment's own pre-registered PASS logic (C1 AND C2 AND C3) cannot be honestly evaluated
as designed, because C3 never measured what it was built to measure at this noise scale. With
C3 excluded as uninformative (neither confirming nor refuting — it is a placeholder
comparison), the remaining architecturally-relevant criterion is C1 alone, and C1 does not
clear a reasonable bar for "supports" on its own: threshold-minimum pass fraction (2/3, the
lowest possible under `PASS_FRACTION_REQUIRED=2/3`), a mean effect size on the order of 1-2% of
the residual magnitude, and a sign reversal on the seed with the most body-noise exposure.

This mirrors 902's own reclassification exactly, and for the identical underlying instrument
defect: **neither `weakens` nor `supports` is a trustworthy read of this run.** It is not
evidence against SD-048 (C1's central tendency is still positive, and 902's broader sweep found
the same weak-but-positive C1 pattern across most ON arms, so this is not an outlier reading).
It is also not clean evidence for SD-048 at the strength "supports" implies — the run cannot
distinguish "the mechanism works and C1's weak positive is a small true effect" from "the
mechanism doesn't yet produce a reliable, discriminable signal at any of the scales tried, and
C1's marginal positive tendency is noise that happens to lean the hypothesized direction."

**Consequence for SD-048's evidentiary basis**: V3-EXQ-512a was SD-048's only current
`supports` evidence. With this reclassification, SD-048 has **no clean confirming experimental
result** — only a confirmed-implemented, non-degenerate substrate (511, non_contributory) and
two now-non_contributory behavioural attempts (512a here; 902 already reclassified) whose
shared instrument cannot yet honestly test the claim. This is a different, more consequential
finding than 902's own (902 already knew it was reclassifying a FAIL to non_contributory,
leaving 512a as the one clean support standing; this autopsy removes that support too).

## 6. Routing (confirmed)

**Reclassify V3-EXQ-512a**: `evidence_direction: supports -> non_contributory`,
`epistemic_category` stays `standard` (per current `/failure-autopsy` guidance — "standard" is
the behaviour-preserving mapping for a measurement/test-design finding; do NOT write
"measurement_test_design_defect", which is an out-of-enum value already flagged for backfill
elsewhere, see `chip-20260809-epistemic-category-vocab-audit`). `status: candidate`,
`v3_pending: true` held unchanged.

**No new `/queue-experiment` action from this autopsy.** V3-EXQ-902 already routed the correct
fix (new EXQ number: minimum-sample guard on any bucket a gap statistic divides against, mark
unscoreable rather than substituting 0.0; restore the architecture doc's own matched-amplitude
C2/C3 definition or decouple a distinct detectability-sanity criterion's sampling from the
noise-trigger frequency). That single redesigned experiment, once run, is what will actually
answer whether SD-048's mechanism works at any scale — including retroactively answering what
512a's ARM_A (scale=3.0) should have shown. Recommending a second, duplicate redesign here
would just re-state 902's own Step 6 outcome.

`recommended_substrate_queue_entry.action: none` — not a substrate gap, same as 902.

**Re-derive brake**: not applicable — this is a `standard`/measurement-instrument finding, not
a `substrate_ceiling` reading, so the brake's counting convention (R3: only `substrate_ceiling`
counts) does not apply here.

**Granularity-debt recurrence check**: ran `granularity_debt_cluster.py SD-048` before this
autopsy — 1 prior target (902), `claim_alignment: unclear`, **no target reads `weakened`**, so
the trigger correctly does not fire on the existing cluster. Adding this target (also
`unclear`, `non_contributory`) does not change that: both 902 and 512a attribute their result to
the *same single instrument defect*, not to structurally different failure signatures circling
an over-broad claim. This is measurement/implementation debt, not granularity debt — do not
route to `/claim-synthesis`.

**Step 9b**: no existing hypothesis-space qid names SD-048 (confirmed, grep of
`hypothesis_space_registry.v1.json`); no `fanout_recommendation` emitted by this autopsy (this
is a re-adjudication of a single existing result, not a discrimination portfolio). Registration
not applicable.

## 7. Evidence quality note (for governance to apply)

> V3-EXQ-512a's standing `supports` verdict does not survive re-examination under the same lens
> as V3-EXQ-902. Verified directly against the manifest's per-seed data and the driver source:
> ARM_A (scale=3.0) has `n_quiet_steps=0` in all 3 seeds, so `residual_quiet=0.0` exactly
> (`_safe_mean([])==0.0`, no minimum-sample guard) and the C3/quiet_gap criterion
> (`residual_body_noise - residual_quiet >= 0.005`) reduces to `residual_body_noise >= 0.005`
> verbatim — not a comparison against any real undisturbed-tick data, the identical tautology
> V3-EXQ-902 found in its own ARM_3. C3 was one of two architecturally load-bearing criteria in
> the driver's own pre-registered PASS = C1 AND C2 AND C3 grid (C2 is only the ARM_B sanity
> check). The one criterion the defect does not touch, C1 (selectivity_gap, body-noise vs
> agent-caused), is too thin to independently sustain "supports": mean effect 0.00097 (~1.5-2%
> of the ~0.05 residual magnitude), 2/3 seeds pass at exactly the minimum required fraction, and
> seed 43 (the seed with the most body-noise exposure, 270 steps) has the WRONG SIGN
> (-0.00067). **Reclassified `supports` -> `non_contributory`** (same read as 902's own
> reclassification, same underlying instrument defect): this run is neither clean evidence for
> nor against SD-048. `epistemic_category` held at `standard`; `status: candidate`,
> `v3_pending: true` unchanged. **Consequence: SD-048 currently has no clean confirming
> experimental result** — V3-EXQ-512a was its only `supports` evidence, and V3-EXQ-902 was
> already reclassified `weakens -> non_contributory` for the same reason. The fix (a redesigned
> criterion with a minimum-group-size guard, restoring the architecture doc's own
> matched-amplitude comparison) was already routed to `/queue-experiment` by V3-EXQ-902's
> autopsy; no duplicate routing is added here.

## 8. Contention note (process, not scientific)

This session's coordination-plane pause claim (the second, broader claim `/failure-autopsy`
Step 1 asks for, to defer the cloud-metaworker while diagnosing) could not be acquired:
`task_claim.py open` arbitrated exact-match contention on `REE_assembly/docs/claims/claims.yaml`,
`REE_assembly/evidence/planning/substrate_queue.json`, and `ree-v3/experiment_queue.json`
against three concurrently active ordinary WORK claims (`mech-322-evidence-confirm-bc9fbf`,
`metaworker-chip-20260809-sd035-attribution-head`,
`metaworker-chip-20260809-sd-e3-scorer-completion`) — none of which are themselves pause locks,
they are unrelated sessions whose own resource lists happen to name the same broad governance
files. Nothing was written for the pause claim (arbitration refused before any commit), so
there was nothing to reverse. This autopsy proceeded without the metaworker pause: none of its
own writes touch `claims.yaml`, `substrate_queue.json`, or `experiment_queue.json` (only this
artifact pair, the hypothesis-space ledger if applicable, and `WORKSPACE_STATE.md`/
`TASK_CLAIMS.json`), so the pause's protective purpose was not load-bearing for this
particular session's work. Flagged for the user's visibility, not as a blocker.
