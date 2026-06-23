# Failure Autopsy: V3-EXQ-703 (MECH-276 scientist-attribution feedstock substrate-readiness diagnostic)

- **generated_utc:** 2026-06-23T22:51:50Z
- **status:** confirmed
- **confirmed_by:** user (interactive /failure-autopsy gate 2026-06-23: "queue-experiment re-queue, converged P0 + cf_margin recalibration")
- **scope:** single
- **run_id:** v3_exq_703_mech276_scientist_attribution_readiness_20260623T075231Z_v3
- **queue_id:** V3-EXQ-703
- **claim_ids:** [] (diagnostic; PROMOTES NOTHING; does NOT promote MECH-275, which stays substrate_conditional)
- **outcome:** FAIL
- **self_route_label:** substrate_not_ready_requeue (R1 world_forward_r2 + R2 cf_margin straddle both unmet)
- **adjudication flag:** precondition_unmet
- **self_route_is_correct_disposition:** true (re-queue, NOT a substrate-verdict)
- **machine:** ree-cloud-2

## 1. Scope

V3-EXQ-703 is the substrate-readiness diagnostic for the MECH-276 scientist-agent
counterfactual-backed attribution feedstock (the waking-phase mechanism that feeds the
MECH-275 sleep-phase Bayesian aggregator; landed 2026-06-23 as
`ree_core/attribution/scientist_attribution_buffer.py`). It is the readiness probe that
gates the SEPARATE MECH-275 sleep-aggregation promotion run (and re-adding MECH-275 to
`sleep_substrate:GAP-3b` `unblocks_claims`). The MECH-275 promotion run V3-EXQ-702
(2026-06-23) had to DROP MECH-275 from its tag set because MECH-276 was unbuilt; this
build is the owed upstream, and 703 is its readiness gate.

A MECH-276 build chip already exists (spawned 2026-06-23 by the V3-EXQ-702 session). This
autopsy adjudicates WHY the readiness PROBE failed, not whether MECH-276 should be built.

## 2. Facts reconstruction (no interpretation)

### Preconditions (self-route source)

| Precondition | measured | threshold | met |
|---|---|---|---|
| `world_forward_r2_trained` (R1) | -0.0547 (mean of per-seed R2) | 0.20 (>= on >= 2/3 seeds) | NO (1/3) |
| `cf_margin_straddles_feedstock` (R2) | 0.0 seeds straddle | 2.0 (>= 2/3) | NO (0/3) |

Per-seed `R1_world_forward_r2`: seed 42 = **-0.688**, seed 7 = **-0.057**, seed 123 =
**+0.581**. Only seed 123 clears 0.20. The aggregate "measured" -0.0547 is the mean.

`R2_straddle_per_seed`: `[false, false, false]`. In ARM_CF_BACKED, every seed:
`mech276_n_counterfactual_backed = 0.0`, `mech276_n_correlational_skipped = 239/241/239`.
With `cf_margin = 0.30` and `mech276_mean_cf_contrast = 0.200 / 0.161 / 0.117`, ALL records
fall below the backed threshold -> all skipped, none backed -> no straddle. This holds EVEN
on the converged seed 123 (cf_contrast 0.117 < margin 0.30).

### Load-bearing criterion (the tell)

`posterior_discrimination_cf_vs_correlational` = **passed (true)**.
`discrimination_per_seed = [true, true, true]`; `posterior_deltas = [0.0112, 0.0076, 0.0053]`
all >= the 1e-3 floor. `criteria_non_degenerate`: `discrimination_feedstock_differs = true`,
`discrimination_aggregator_updated = true`. The CF arm skipped 239/241/239 correlational
records vs the CORRELATIONAL arm's 0; the aggregator ran 800 updates / 47-74 posteriors in
every arm.

**Expected vs observed:** the probe expected a TRAINED world_forward (R1) + a straddling
cf_margin (R2) BEFORE reading the load-bearing discrimination. Observed: the discrimination
fired cleanly and non-degenerately, but the two readiness preconditions did not clear, so the
script self-routed `substrate_not_ready_requeue` (the correct, pre-registered disposition for
an unmet readiness gate -- NEVER a substrate-verdict label).

**Which criterion failed:** a PRECONDITION (positive control + feedstock-discriminability
gate), not the discrimination/load-bearing criterion. This is the readiness-gate fingerprint,
not the substrate-ceiling fingerprint.

## 3. Claim-layer mapping

claim_ids = []. The run promotes nothing and weakens nothing; it is a diagnostic
(experiment_purpose=diagnostic, scoring-excluded). MECH-275 stays candidate /
substrate_conditional / v3_pending; MECH-276 stays candidate / v3_pending. The FAIL cannot
weigh against any claim -- there is no claim to mis-falsify. The only question is the
disposition of the diagnostic itself.

## 4. Biological-reference triage

Not the failing layer. The MECH-276 mechanism (counterfactual-backed attribution =
`||z_obs - E2(z_prev,a)||` with a counterfactual contrast `||E2(z_prev,a) - E2(z_prev,a_cf)||`
gating which attributions reach the MECH-275 aggregator) is a faithful single-pass-comparator
instantiation (SD-031 E2WorldForward + the MECH-256 comparator family), grounded in the
Frith/Shergill/Blakemore agency-comparator literature. The failure is UPSTREAM of any
MECH-275/276 mechanism: a diagnostic positive control (the P0 world-forward) did not train,
and a threshold (cf_margin) was set outside the achievable contrast distribution. No biology
divergence is implicated.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (intact) | diagnostic, claim_ids=[]; never a weakens. Correctly non_contributory. |
| Biological reference | clear; not the failing layer | comparator mechanism is sound; failure is upstream (untrained P0 + threshold). |
| Prerequisites / dependency | **missing (diagnostic-internal)** | a CONVERGED P0 E2WorldForward -- the valid base the comparator's discrimination depends on. It trained on only 1/3 seeds (R2 -0.688/-0.057/+0.581). |
| Implementation completeness | **partial** | the MECH-276 buffer + the `only_counterfactual_backed` cf-gate are CORRECT (discrimination + non-degeneracy PASS); the gap is the P0 training that feeds the comparator + the cf_margin calibration. |
| Environment adequacy | adequate | CausalGridWorldV2 is genuinely action-conditional (the script's stated design reason). |
| Measurement adequacy | under-instrumented for convergence | the readiness probe is sound, but the P0 budget/regime does not deliver a converged base on >= 2/3 seeds, so R1 has nothing valid to read; cf_margin is fixed at 0.30 above the ~0.12-0.20 contrast band. |
| Integration adequacy | n/a | single-module readiness diagnostic. |
| Scale / capacity | likely insufficient P0 | N_P0_TRANSITIONS=600, N_P0_TRAIN_STEPS=300; per-seed R2 ranges to -0.688 -- the SD-056 world-forward did not train to a usable R2. |

**Dominant diagnosis layer:** prerequisite/implementation -- an untrained P0 world-forward
(the V3-EXQ-642 untrained-substrate confound), with a secondary cf_margin mis-calibration.
**Recommended epistemic_category:** n/a (diagnostic; no claim status change).

## 6. Cross-check vs failure_autopsy_V3-EXQ-701_2026-06-23

Same `world_forward-not-trained-as-primary` signature. 701 (INV-050 MEL-measurability
diagnostic) failed its R2 `world_model_converged` gate at conv_rel_drop = -2.60 -- the SD-056
P0 world-forward DIVERGED because its P0 trained the SD-056 InfoNCE action-divergence
contrastive loss ALONE with no reconstruction anchor (the e2.world_forward "NOT trained as
E2 primary objective" path). The 701 -> 701a fix added the world-forward reconstruction MSE
as the PRIMARY P0 loss (`L_E2 = L_recon + w_contrast * L_contrast`), raised CONV_EPISODES
20 -> 60, and added a per-seed R2 readiness gate (interpret the downstream criteria ONLY on
seeds whose P0 converged).

703 shows the IDENTICAL family at the comparator-readiness layer: `_train_world_forward`
(experiments/v3_exq_703_...py:197) optimises `e2w.compute_loss(pred, zn) +
e2w.compute_interventional_loss(...)` -- the SD-013 interventional MARGIN term (action-spread)
ALONGSIDE the forward MSE, but the regime/budget still leaves the held-out R2 negative on
2/3 seeds. The fix is the same shape as 701a: make the world-forward reconstruction the
decisive P0 objective on this readiness harness, raise the P0 budget, gate per-seed on R2
convergence, and -- additionally -- recalibrate cf_margin within the (now-meaningful)
cf_contrast distribution.

The self-route is a hypothesis, not a verdict (the canonical V3-EXQ-642 rule): the branch's
assumption (substrate ready / world_forward trained) was actually UNMET because the P0 did
not converge, so the correct route is RE-QUEUE, not enrichment. The passing discrimination +
non-degeneracy positively RULE OUT the "MECH-276 feedstock genuinely absent" reading.

## 7. Learning extracted

1. 703's two unmet preconditions are downstream of an untrained P0 world-forward (R1, 1/3
   seeds converge) -- the V3-EXQ-642 / 701 confound -- NOT a missing MECH-276 feedstock. The
   load-bearing discrimination criterion + non-degeneracy PASS, so the feedstock buffer +
   the `only_counterfactual_backed` lever demonstrably work.
2. cf_margin (0.30) is independently mis-calibrated ABOVE the cf_contrast distribution
   (~0.117-0.200) -- so even the one converged seed (123) skips every record and yields no
   straddle. The re-queue must recalibrate cf_margin into the achievable band (~0.15), AND
   the band itself only becomes meaningful once the P0 world-forward trains.
3. The decisive next test: a converged-P0 + recalibrated-cf_margin re-run. If R1+R2 then
   clear and the discrimination still holds, the MECH-276 feedstock readiness is confirmed
   and the SEPARATE MECH-275 sleep-aggregation promotion run is unblocked. If R1+R2 clear
   and the discrimination COLLAPSES on the trained comparator, THAT would be the genuine
   MECH-275-aggregator-insensitivity ceiling (route then to substrate enrichment + fire a
   re-derive brake on the clean reading) -- not reachable from this confounded run.

## 8. Routing

**queue-experiment** (re-queue with a converged P0 + cf_margin recalibration; mirrors
701 -> 701a). No `substrate_queue` entry. No re-derive brake (claim_ids=[]; no claim to count;
re-queue, not a substrate_ceiling reading -- mirrors the 701 autopsy).

### Recommended re-queue spec (NEW letter, e.g. V3-EXQ-703a; supersedes V3-EXQ-703)

- **P0 convergence:** train the E2WorldForward so the world-forward RECONSTRUCTION is the
  decisive P0 objective on the readiness harness (the 701a pattern: forward MSE primary;
  keep the SD-013 interventional margin as a smaller auxiliary so action-spread does not
  dominate and degrade absolute one-step R2). Raise `N_P0_TRANSITIONS` / `N_P0_TRAIN_STEPS`
  (and/or N_P0 episodes) until held-out R2 >= 0.2 on >= 2/3 seeds.
- **Per-seed R2 readiness gate:** interpret R2 (cf_margin straddle) and the load-bearing
  discrimination ONLY on seeds where R1 (`world_forward_r2 >= 0.2`) passes -- a per-seed gate,
  not a run-level one (the 701a discipline). Self-route `substrate_not_ready_requeue` if R1
  does not clear >= 2/3.
- **cf_margin recalibration:** set `cf_margin` within the trained-comparator cf_contrast
  distribution (measured ~0.12-0.20 on this run; aim ~0.15) so the CF arm has BOTH backed
  AND correlational-skipped records (the straddle). The script's own grid already prescribes
  this on an R2 miss.
- **Keep:** the MECH-276 feedstock buffer, the `only_counterfactual_backed` lever, the
  MECH-275 aggregator posterior read, claim_ids=[] (diagnostic), commitment-free.
- **Decisive outcome:** R1+R2 met + discrimination holds -> mech276_feedstock_readiness
  confirmed -> unblock the SEPARATE MECH-275 sleep-aggregation promotion run + re-add MECH-275
  to `sleep_substrate:GAP-3b` `unblocks_claims`. R1+R2 met + discrimination COLLAPSES ->
  substrate_ceiling (aggregator insensitive to the feedstock difference) -> route to
  substrate enrichment + fire the re-derive brake on that clean reading.

### recommended_evidence_quality_note (governance should write; do not write here)

> V3-EXQ-703 (2026-06-23, failure-autopsy): MECH-276 scientist-attribution feedstock
> readiness diagnostic, non_contributory CONFIRMED (diagnostic, claim_ids=[], scoring-excluded;
> PROMOTES NOTHING; MECH-275 stays substrate_conditional). Self-route substrate_not_ready_requeue
> is correct per the pre-registered grid: BOTH readiness preconditions unmet -- R1
> world_forward_r2 -0.0547 (SD-056 P0 world-forward trained on only 1/3 seeds; per-seed R2
> -0.688/-0.057/+0.581) and R2 cf_margin straddle 0/3 (cf_margin 0.30 above the ~0.12-0.20
> cf_contrast band, so zero records cross the backed threshold even on the converged seed).
> Both trace to the same world-forward-not-trained-as-primary confound as V3-EXQ-701 (642
> family), NOT a missing MECH-276 feedstock -- the load-bearing posterior-discrimination
> criterion + criteria_non_degenerate PASS (the only_counterfactual_backed lever measurably
> gates what reaches the MECH-275 aggregator). Route: re-queue (new letter) with a
> reconstruction-primary converged P0 + a per-seed R2 gate + cf_margin recalibrated into the
> trained cf_contrast distribution; no substrate_queue entry; no re-derive brake. If a
> converged-P0 successor then clears R1+R2 but the discrimination COLLAPSES, THAT is the
> genuine MECH-275-aggregator-insensitivity ceiling and routes to substrate enrichment.

## 9. Evidence protection

MECH-275 / MECH-276 are diagnostic-gated and unweakened by this run. 703 is a diagnostic
(scoring-excluded) with a clean substrate_not_ready_requeue self-route (non_contributory,
never a weakens) -- no claim status change. The recommended action is a queue-experiment
re-queue with a converged P0 + cf_margin recalibration; governance applies the disposition +
marks 703 reviewed.
