# Failure Autopsy — V3-EXQ-902 (SD-048 default-scale calibration sweep)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single (with a flagged re-examination of V3-EXQ-512a)
**Status:** confirmed (interactive gate run 2026-08-09 — user confirmed reclassifying 902 AND flagging 512a's standing `supports` verdict for re-examination)

## 1. Facts

Manifest `v3_exq_902_sd048_default_scale_calibration_sweep_20260809T002118Z_v3`, `claim_ids: ['SD-048']`, `experiment_purpose: evidence`. 4-arm sweep (ARM_0 off / ARM_1 0.25x / ARM_2 1.0x-default / ARM_3 4.0x), re-queued after being absent from `experiment_queue.json` for ~3 months following V3-EXQ-512a, which proved the mechanism at a tuned `noise_scale=3.0` but left `v3_pending` TRUE pending this default-scale sweep.

Criteria: C1 `selectivity_gap = residual_body_noise - residual_agent > 0`; C2 `quiet_gap = residual_body_noise - residual_quiet >= 0.005`; C4 `forward_r2 >= 0.5` (ARM_0 sanity). PASS requires ARM_2 (default) to clear C1+C2, plus ARM_0 to clear C4.

| Arm | scale | C1 | C2 | C4 | mean sel_gap | mean quiet_gap | n_body/n_agent/n_quiet |
|---|---|---|---|---|---|---|---|
| ARM_0 | 0.0 | 0/3 (trivially correct) | 0/3 | 3/3 | 0.0 | -0.027 | 0/0/~391 |
| ARM_1 | 0.25x | 2/3 PASS | 0/3 FAIL | 3/3 | 0.00326 (largest) | -0.0008 | **2**/7/403 |
| ARM_2 (default) | 1.0x | 3/3 PASS | **0/3 FAIL** | 3/3 | 0.00157 | -0.00151 | 286/114/**5** |
| ARM_3 | 4.0x | 2/3 PASS | 3/3 PASS | 3/3 | 0.00058 (smallest) | 0.0665 | 291/114/**0** |

Failed criterion at the deciding arm (ARM_2): C2, discrimination.

**Load-bearing finding**: at ARM_3, `n_quiet_steps = 0` in all three seeds — `residual_quiet` is reported as exactly 0.0, so `quiet_gap = residual_body_noise - 0.0` verbatim (bit-for-bit, e.g. seed 42: 0.07137503 both fields). ARM_3's C2 "pass" is not a comparison against an undisturbed baseline at all — there is no undisturbed baseline left; the metric collapses to a tautology once residuals reach the 0.05-0.07 range this arm produces. Mechanism (`causal_grid_world.py:4655-4763`): `interoceptive_noise_scale` multiplies both perturbation amplitude AND trigger probability, so at scale >=~3 the noise generator's own trigger frequency mechanically squeezes the "quiet" (no-event) tick category toward zero — a property of how the generator scales, not of the comparator.

**This defect predates 902**: V3-EXQ-512a's own ARM_A (scale=3.0) — SD-048's *only* currently-standing positive evidence, `evidence_direction: supports` — has the identical signature: `n_quiet_steps=0` in all 3 seeds, `residual_quiet=0.0` in all 3 seeds. Its C3 "PASS" (quiet_gap=0.054 mean, 3/3 seeds, the deciding criterion for its `supports` verdict) is the same tautology. Undetected at the time (512a predates the 2026-07-12 recording standard; nothing flagged it).

`check_degeneracy()`'s `non_degenerate: true` is technically correct but incomplete: it tests cross-seed variance of the reported gap (is it pinned at a constant?), not sample-count degeneracy of the underlying bucket the gap divides against. ARM_3's three quiet_gap values have real cross-seed spread, so the check correctly passes by its own definition while being blind to every one of those values being computed from an empty comparison bucket.

**Second, independent drift**: the architecture doc's own C2 (`docs/architecture/sd_048_interoceptive_noise_dynamics.md`) is defined as "forward model residual is larger for body-noise events than for agent-caused events, in matched-amplitude conditions" — essentially the same self/other comparison as C1, not a comparison against an undisturbed quiet state. The driver's own docstring is honest that it substitutes a quiet-baseline proxy "for comparability," carried forward unquestioned since V3-EXQ-511. This substitution changed what C2 actually tests (from "does the comparator discriminate self vs other" to "is noise-injection detectable above doing nothing") — and it is exactly this substituted metric that goes degenerate.

Reverse degeneracy at the low end: ARM_1's C1 pass rests on `n_body_noise_steps = 2` per seed — an essentially anecdotal sample. ARM_2's C2 fail is the one cell with a real, non-collapsed-but-thin quiet sample (n=5).

Dry-run check: clean.

## 2. Claim-layer mapping

SD-048 (`design_decision`, `candidate`, `v3_pending: true`) already separates precondition (confirmed 2026-05-03, unaffected), calibration question (default parameterization detectable), and falsifying branch (flat collapse -> route ARC-058 to `substrate_conditional`) in its own `what_would_answer`. 902 lands in none of the pre-registered grid cells cleanly:

- Not "ARM_2 PASS, ARM_0 FAIL" (validated) — ARM_2 fails C2.
- Not a genuine flat curve either — C1 (unaffected by the quiet-bucket defect) shows a small but real positive gap in most cells (2/3, 3/3, 2/3 seeds across the ON arms). Recomputing `any_on_arm_pass` with ARM_3's vacuous C2 excluded flips the label toward "falsified/flat," but that fallback assumed a genuine flat curve on *both* metrics, which C1 contradicts.

**This run does not demote SD-048 as a mechanism, and does not cleanly confirm the default-parameterization-only reading either** — it demotes confidence in the instrument the entire 511->512->512a->902 chain has used to decide the calibration question.

`claim_alignment: unclear` — the deciding criterion did not let the claim express itself honestly across most of the manipulated range.

## 3. Biological-reference triage

Reafference discrimination (self vs externally-caused sensory/body-state change via efference copy) — von Holst & Mittelstaedt 1950 reafference principle; cerebellar forward-model literature (Wolpert/Miall/Kawato); corollary-discharge dysfunction in psychosis (Frith; Ford & Mathalon); interoceptive-predictive-coding accounts of allostasis (Seth; Barrett; Craig). Literature is present: `evidence/literature/targeted_review_reafference_streams/`, and the claim's own `evidence_quality_note` records 6 entries at `literature_confidence 0.86`. No new `/lit-pull` warranted.

The empirical pattern found (signal only detectable once injected noise clears the forward model's own natural prediction-error floor) is itself biologically sensible — a signal-detection-theoretic requirement seen in real sensory systems (self-tickling attenuation only once external force is discriminable above baseline variability, Blakemore/Frith). Not evidence the mechanism is biologically misconceived; evidence the instrument needs an SNR-respecting design.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | deciding criterion not honestly evaluable across most of the scale range; C1 shows weak-but-real signal broadly |
| Biological reference | present | von Holst/Mittelstaedt reafference principle; 6 lit entries, conf 0.86; SNR-detectability finding is consistent with biological signal-detection accounts |
| Dependency prerequisites | present | SD-011 (z_harm_a), SD-022 (agent-caused variance) both implemented; precondition explicitly confirmed |
| Implementation completeness | complete (substrate) / defective (measurement) | environment's noise injection + event classification works exactly as documented; the experiment driver's C2 statistic is the defective part |
| Environment adequacy | inadequate for this criterion at this scale range | env couples noise magnitude and trigger-frequency to the same `scale` knob, mechanically depleting the quiet-tick category as scale rises |
| Measurement adequacy | under-instrumented / structurally flawed | `_safe_mean` returns 0.0 for an empty bucket with no minimum-n guard; C2 itself is a drift from the architecture doc's own pre-registered definition |
| Integration adequacy | coupled, not the locus of the problem | agent/encoder/forward-model integration not implicated; C4 sanity passes cleanly (R^2~0.99) |
| Scale/capacity | not the locus of the problem | data-sufficiency/criterion-design issue, not representational capacity |

## 5. Learning extracted

1. The C2/quiet_gap proxy used across the entire SD-048 evidence lineage (511/512/512a/902) collapses to a tautology whenever the quiet bucket is empty, which the noise generator's own trigger-frequency scaling makes structural at scale >=~3x.
2. This is not new to 902 — V3-EXQ-512a's currently-standing `supports` verdict rests on the identical n_quiet_steps=0 pattern and should be reconsidered.
3. `check_degeneracy()`'s cross-seed variance check does not catch sample-count degeneracy of an underlying event bucket a gap statistic divides against — a generalizable tooling gap worth a companion minimum-group-size guard (out of scope for this autopsy to build).
4. The implemented C2 is itself a drift from the architecture doc's own pre-registered C2 (body-noise vs matched-amplitude agent-caused), silently substituted for a quiet-baseline comparison since V3-EXQ-511 "for comparability."
5. C1 (unaffected by the quiet-bucket defect) shows a small but consistently positive gap across most ON-arm cells — arguing against a flat-curve/no-signal falsification reading.
6. Worth a follow-up check (not chased down here): SD-047, built on the same 4-arm noise-level sweep protocol, may share this exact `_safe_mean`-without-n-guard pattern.

## 6. Routing (confirmed)

**902**: reclassified `epistemic_category: measurement_test_design_defect`, `evidence_direction: non_contributory` (was filed `weakens`). Routing: `/queue-experiment`, new EXQ number (this changes what the criterion measures, not merely a parameter) — add a minimum-sample guard on any bucket a gap/ratio statistic divides against (mark unscoreable rather than substituting 0.0); restore a genuine matched-amplitude C2 per the architecture doc, or decouple a distinct "detectability sanity" criterion's sampling from the noise-trigger frequency. `recommended_substrate_queue_entry.action: none` — not a substrate gap.

**512a**: flagged for re-examination under the same lens per user confirmation — its `supports` verdict should not continue standing unqualified while it rests on the identical artifact. This autopsy does not itself re-adjudicate 512a (out of scope — a separate target), but records the finding so governance/a future autopsy session picks it up rather than re-discovering it.

`status: candidate`, `v3_pending: true` held unchanged pending a redesigned criterion.

**Step 9b**: no existing hypothesis-space qid names SD-048; no `fanout_recommendation` emitted. Registration deferred.

## 7. Evidence quality note (for governance to apply)

> V3-EXQ-902's own FAIL (ARM_2/default fails C2) should not be read as weakening SD-048, and its self-route ("validated, calibration off") should not be read as confirming it either. Both readings depend on a C2/"quiet_gap" statistic (residual_body_noise - residual_quiet) that has no minimum-sample guard on the quiet bucket; at scale >= ~3-4x (including this run's own ARM_3, and V3-EXQ-512a's ARM_A at scale=3.0, which is SD-048's current sole "supports" evidence) n_quiet_steps=0 in every seed, so the statistic collapses to residual_body_noise minus a zero placeholder rather than a real comparison. C1 (body-noise vs agent-caused, unaffected by this defect) shows a small but consistently positive gap across most cells, so this is not a flat-curve falsification either. Reclassified to measurement_test_design_defect; hold status: candidate/v3_pending: true unchanged pending a redesigned criterion (see routing) that (a) guards minimum sample size and (b) restores the architecture doc's own matched-amplitude C2 definition rather than the quiet-baseline proxy substituted since V3-EXQ-511. **V3-EXQ-512a's "supports" verdict should be reconsidered under the same lens rather than continuing to stand unqualified** -- flagged here for a follow-up autopsy or governance re-adjudication, not resolved in this pass.
