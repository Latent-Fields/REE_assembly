# Failure Autopsy -- V3-EXQ-590c (MECH-314 per-candidate novelty Goldilocks under 569i top-k)

- **Generated (UTC):** 2026-06-24T22:05:33Z
- **Run:** `v3_exq_590c_mech314_novelty_goldilocks_20260624T105537Z_v3` (machine ree-cloud-2)
- **Queue id:** V3-EXQ-590c -- supersedes V3-EXQ-590b (FAIL/non_contributory 2026-06-11)
- **claim_ids:** [MECH-314, DEV-NEED-003] -- `experiment_purpose=evidence`
- **Manifest verdict:** FAIL; `evidence_direction=non_contributory`; `interpretation.label=substrate_not_ready_requeue`
- **Status:** confirmed (interactive gate, user-adjudicated 2026-06-24)
- **Scope:** single

The 2026-06-24T21:42Z `/governance` cycle deferred this FAIL to autopsy under the standing
directive: a FAIL needs an autopsy before its `evidence_direction` is decided -- the
self-route is a hypothesis, not a verdict. This autopsy VERIFIES the self-route. It finds the
self-route's stated REASON is confounded but its CONCLUSION (non_contributory) is correct for
a stronger reason, recommends `substrate_ceiling` over the manifest's `substrate_not_ready`,
and FIRES the re-derive brake (4th MECH-314 ceiling autopsy).

---

## 1. Facts -- what the run measured

Sweep over `curiosity_novelty_weight` in {0.0, 0.05, 0.25, 1.0} (arms W000/W005/W025/W100),
3 seeds, with the GAP-A / modulatory-bias-selection-authority stack held CONSTANT
(`use_modulatory_selection_authority=True`, `modulatory_authority_gain=1.0`,
`use_modulatory_shortlist_then_modulate=True`, `modulatory_shortlist_mode=top_k`, k=3).
DV = committed-action-class entropy. MECH-314 curiosity is the SOLE modulatory channel;
`curiosity_candidate_source=e2_world_forward` on the 648a-validated substrate.

Four readiness preconditions, one failed:

| precondition | measured | threshold | met |
|---|---|---|---|
| e2_world_forward_action_divergence_non_vacuity (cand pairwise dist @ highest-weight arm) | 0.121 | > 0.02 | yes |
| curiosity_bias_range_supra_floor (per-candidate range @ highest-weight arm = W100) | 0.0 | >= 1e-4 | NO |
| committed_class_entropy_range_across_weight_arms_supra_floor | 0.312 | >= 0.05 | yes |
| rolled_out_zworld_magnitude_bounded | 0.306 | < 1e6 | yes |

Goldilocks DV: control W000 = 0.7269; best W005/W025 = 0.7459; W100 collapses to 0.4337
(inverted-U upper arm). Best-arm lift over control = 0.019 < 0.05 margin, on 1/3 seeds.

Per-arm curiosity bias range (mean): W000 0.0 / W005 0.0032 / W025 0.0160 / W100 0.0.

## 2. Reconstruction -- two facts the manifest summary does not reconcile

**(a) The failed precondition reads the arm the design guarantees will read ~0.**
The script docstring (lines 40-43, 85) labels ARM_W100 the "clamp-saturation regime":
"weight too HIGH -> the curiosity bias saturates the +/-bias_scale clamp for ~all candidates
-> flat again." But the `curiosity_bias_range_supra_floor` precondition is computed at
`highest_weight_arm = max(ARMS, key=weight)` = W100 (lines 692-710). The non-vacuity gate
routes through the one arm the inverted-U design expects to flatten. W100 seeds 42/43 are
bit-identical to the W000 control (0.10705 / 0.709609, same h_pos, same ep_h_pos_last5) -- the
clamp pins every candidate to the same ceiling, range -> 0, and the within-top-3 argmin falls
back to the F-only tie-break, reproducing the control trajectory.

**(b) The channel is demonstrably alive at moderate weight.** W005=0.0032 and W025=0.0160 both
clear the 1e-4 floor and scale ~5x with weight (0.25/0.05). So the manifest's stated reason --
"the MECH-314 per-candidate novelty channel emits an identically-flat per-candidate signal, so
the top-k argmin has nothing to arbitrate on" -- is FALSE as written. The signal is not
identically flat; W100=0.0 is a clamp artifact, not a dead channel. This is the 648a/649
lesson recurring (a modulatory bias's readiness gate must check cross-candidate RANGE at the
arm that matters, not where the pool collapses) and a sibling of the 642 / 701a
confounded-precondition pattern (an unmet branch assumption mislabels the cause).

**(c) But the deeper conclusion still holds, for a stronger reason.** committed_class_entropy
is bit-identical between W005 and W025 (0.745859 each, per seed: 0.920523 / 0.242969 /
1.074085) despite a 5x difference in bias magnitude. The within-top-3 argmin does not move.
Where the channel is unconfounded and alive, it reaches the shortlist and still cannot convert
to committed diversity -- drowned at the F-dominated argmin (MECH-439; F monopolises 88-89% of
E3 selection variance, V3-EXQ-571). The 569i top-k conversion path the queue entry banked on to
release the brake WAS exercised (the bias is no longer 0.0-contribution as in 604a); the
bottleneck simply moved one link downstream to the same F-dominance ceiling 590a/590b/604a/648a
all hit.

**Failed criterion class:** discrimination (Goldilocks lift), gated behind a confounded
readiness precondition. The genuine signal is the W005-vs-W025 no-conversion, not the W100
clamp reading.

## 3. Claim-layer mapping

- **MECH-314** (`structured_curiosity_bonus`, ARC-065 child, candidate). The experiment did NOT
  let the claim express itself: the per-candidate novelty bias reaches the committed shortlist
  but is overwhelmed at the F-dominated argmin before it can shift committed action. An
  implementation/selection-substrate ceiling, not claim pressure. UNWEAKENED.
- **DEV-NEED-003** is a developmental-need gate, NOT a `claims.yaml` id -- it accrues no
  confidence. Only MECH-314 could score, and it scores non_contributory. UNWEAKENED.
- `claim_ids` accuracy: re-evaluated from scratch (the queue entry correctly dropped 590b's
  MECH-314a tag); [MECH-314, DEV-NEED-003] is the right tag set.

## 4. Biological-reference triage

MECH-314 structured curiosity = frontopolar/striatal exploration drive. The reference mechanism
is intact (a novelty bonus that biases candidate evaluation); the failure matches what happens
biologically when an exploratory bias is gated downstream by a dominant value/limbic signal --
the bias is present and graded but cannot reach committed action because the selection
bottleneck (BG/pallidal arbitration) is monopolised by the primary value channel. That is the
F-dominance signature, and its biologically-faithful break is the basal-ganglia rank-preserving
F->eligibility demotion already built as MECH-448/ARC-107 (`use_f_eligibility_demotion`,
provisional). Not a formal-import divergence; no `/lit-pull` owed.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test could not let MECH-314 express itself; drowned at the F-argmin |
| Biological reference | clear | exploratory bias gated downstream by dominant value signal; break = BG demotion |
| Prerequisites / dependency | present-but-insufficient | 569i top-k + GAP-A divergent pool both healthy (cand dist 0.121); the missing prerequisite is the F-dominance break, not the conversion path |
| Implementation completeness | complete | channel emits real per-candidate range (W005/W025); not a wiring null |
| Environment adequacy | adequate | harm-free foraging env; GAP-A pool divergent |
| Measurement adequacy | under-instrumented (confounded precondition) | curiosity_bias_range_supra_floor reads the clamp-saturation arm; should read a non-saturation arm or max-across-arms |
| Integration adequacy | coupled-but-overwhelmed | bias reaches the top-k shortlist but the argmin tracks F |
| Scale / capacity | adequate | inverted-U is real (W100 collapse); not a budget issue |

**Recommended `epistemic_category`: `substrate_ceiling`** -- the claim is V3-tractable in
principle, but the current E3 selection substrate (F-dominated committed argmin) is too coarse
to let the per-candidate novelty channel reach committed action. NOT `substrate_not_ready` (the
manifest's `substrate_not_ready_requeue` implies a GAP-A-readier re-run would help; it would
not -- the channel already reaches the shortlist on the GAP-A-ready substrate).

## 6. Re-derive brake -- FIRES (user-confirmed)

Prior MECH-314 substrate_ceiling / non_contributory autopsies:
`failure_autopsy_EXQ-572-573_2026-05-17`, `failure_autopsy_604a-624a-630_2026-06-03`,
`failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07`. This is the 4th (threshold = 2).

The queue entry RELEASED the brake ex ante, arguing the 569i top-k conversion path + ARC-065
GAP-A made 590c a "conversion-path re-issue, not a same-granularity re-test." The result
falsifies that release argument: the conversion path was exercised and the bottleneck reasserted
as the same F-dominance ceiling. Per MOVE-3 the brake fires now.

- REFUSE a 590d same-design curiosity-weight sweep against the bare F-dominated argmin. That is
  exactly the lettered-iteration loop the brake exists to stop (590a -> 590b -> 590c).
- Route: implement-substrate on the F-dominance break (`f_dominance_conversion_ceiling`
  substrate; MECH-448/ARC-107 `use_f_eligibility_demotion`, already BUILT + provisional, the
  selection-face ceiling already LIFTED on the GAP-A foraging substrate). The substrate exists --
  so the actionable next step is the demotion-ON re-test, a different-substrate redesign that is
  brake-EXEMPT, NOT another weight sweep.
- The MECH-314 curiosity-conversion re-test belongs in the existing downstream-behavioural-retest
  family the f_dominance entry already carries (654h/485i/445h/625e) -- re-test committed-class
  diversity with `use_f_eligibility_demotion` (and/or the MECH-439 689-lineage conflict-grade
  levers) ON, the curiosity channel as the modulatory input.

**Secondary learning (for whoever re-issues, not a re-queue trigger):** the readiness
precondition should read the per-candidate range at a non-saturation arm (or max-across-arms),
not the highest-weight clamp-saturation arm. This does not change the verdict -- W005-vs-W025
already demonstrate no conversion -- but it removes the confound that mislabelled the cause.

## 7. Draft `evidence_quality_note` (governance writes; do not write here)

> V3-EXQ-590c (non_contributory, scoring-excluded): MECH-314 per-candidate novelty Goldilocks
> under the 569i top-k path. The self-routed substrate_not_ready reason is confounded -- the
> curiosity_bias_range precondition reads the clamp-saturation arm (W100=0 by design) while
> W005/W025 carry real per-candidate range (0.0032/0.0160). But the channel, where alive, still
> does not convert: committed_class_entropy is bit-identical W005-vs-W025 (5x bias difference,
> zero argmin change; lift 0.019<0.05 margin, 1/3 seeds) -- the F-dominance conversion ceiling
> (MECH-439), downstream of the now-exercised 569i top-k conversion path. Recommended
> epistemic_category=substrate_ceiling. MECH-314 + DEV-NEED-003 UNWEAKENED. Re-derive brake
> FIRED (4th MECH-314 ceiling autopsy): refuse a same-design 590d weight sweep; the owed work is
> a MECH-314 curiosity-conversion re-test with the F-eligibility demotion (MECH-448/ARC-107) ON,
> in the f_dominance_conversion_ceiling downstream-retest family.

## 8. Routing decision (confirmed)

- `evidence_direction`: non_contributory (MECH-314 + DEV-NEED-003 UNWEAKENED).
- `epistemic_category`: substrate_ceiling (governance recommendation; not written by this skill).
- routing: implement-substrate -- `f_dominance_conversion_ceiling` (amend with the 590c failure
  record); re-derive brake FIRED, same-claim weight-sweep re-queue REFUSED; the demotion-ON
  conversion re-test is the brake-exempt next step.
