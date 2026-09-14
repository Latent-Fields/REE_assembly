# Failure Autopsy: V3-EXQ-900 (SD-024 DA cluster allocation, representational + functional)

**Generated:** 2026-09-14T12:13:56Z
**Scope:** single
**Trigger:** GFLAG-0246 (evidence_discrepancy, routed to `/failure-autopsy` by governance cycle governance-20260909 wave 3)
**Status:** confirmed

## 1. Facts

- **Manifest:** `REE_assembly/evidence/experiments/v3_exq_900_sd024_da_cluster_allocation_representational_functional_20260808T103846Z_v3.json`
- **Outcome:** PASS, `evidence_direction: supports`, `experiment_purpose: evidence`, `claim_ids: ["SD-024"]`.
- **Recording:** `validate_recording.py` reports the always-core complete (substrate_hash, config, seeds, machine all present). Two advisory (non-blocking) findings: no top-level numeric scalar readout block, and `combination_rule` names criteria at a JSON path (`interpretation.criteria`) the validator's generic scan doesn't check by default -- the criteria ARE recorded, with measured values and thresholds, directly under `interpretation.criteria`; this is a validator-path quirk, not a real recording gap.
- **Dry-run check:** `check_dry_run_citations.py` on the cited run_id: 0 dry cited, 1 clean. Not a smoke.
- **Review status:** already in `review_tracker.json` `reviewed_run_ids` (confirmed via grep) -- does not re-derive into `pending_review.md`, consistent with why this is dispatched as a chip rather than surfaced by the normal worklist.
- **Autopsy coverage:** `check_autopsy_coverage.py V3-EXQ-900` -> AVAILABLE=YES (no prior autopsy).

**Combination rule:** `PASS iff C1 AND C2 AND C4 hold on the POOLED live sample, given a green readiness gate.`

| Criterion | Measured | Threshold | Passed |
|---|---|---|---|
| C1 (da vs cluster_size, Spearman rho) | 0.5327 | >= 0.30 | yes |
| C2 (cluster_size vs density, Spearman rho) | 0.5166 | >= 0.30 | yes |
| C4 (harm asymmetry: 0 cluster allocations on harm field) | 0 of 1403 harm calls | 0 | yes |

Readiness gate (all pre-registered, none derived from this run's own statistics):

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| R1 sweep rho(da,size) | 1.0 | >=0.9 | yes |
| R2 sweep rho(size,density) | 1.0 | >=0.9 | yes |
| R3 pooled expansion events (cluster_size>=2) | 6 | >=5 | yes (margin: 1 event) |
| R4 pooled harm events | 1403 | >=5 | yes |

Independent non-degeneracy check (distinct from the R3 count floor): `criteria_non_degenerate: {C1: true, C2: true, C4: true}`. Recomputed directly from `per_seed_rows`: pooled cluster-size distribution across the 57 live benefit events is `{1: 51, 2: 2, 3: 1, 4: 1, 5: 1, 8: 1}` -- 6 distinct sizes present, genuinely non-degenerate, not merely a count that happens to clear a floor.

**The flagged observation (GFLAG-0246):** the `pooled` block also carries
`mean_benefit_magnitude_across_cluster_sizes_ge2 = 0.5577261900901794` vs
`mean_benefit_magnitude_across_cluster_size_1 = 0.5582475601224338` -- a ~0.09% difference,
recorded but ungated by any criterion.

**Recomputed directly from `per_seed_rows` (not merely re-stated from the pooled block):**

```
n(cluster_size>=2) = 6, n(cluster_size==1) = 51
mean(benefit_magnitude | >=2) = 0.5577261900901794 (stdev 0.00671)
mean(benefit_magnitude | ==1) = 0.5582475601224338 (stdev 0.00920)
benefit_magnitude range, ALL 57 pooled events: [0.530, 0.5736]   (CV ~1.5%)
dopamine_signal range, ALL 57 pooled events:  [0.0053, 0.1815]  (34x span)
```

**Traced to source** (`ree-v3/ree_core/agent.py`, `update_z_goal` -> `residue_field.accumulate_benefit`):
```
accumulate_benefit(z_world, benefit_magnitude=float(benefit_exposure), ...,
                    dopamine_signal=float(benefit_exposure) * float(drive_level))
```
`benefit_magnitude` is the raw environmental reward value at that step (essentially fixed at
`RESOURCE_BENEFIT=0.5` plus small per-step noise) -- it is the multiplicand INTO the dopamine
formula, not an output the allocation mechanism produces. `dopamine_signal` (the quantity that
actually drives `cluster_size = 1 + int(dopamine_signal * da_allocation_scale)`) is the product
of `benefit_magnitude` with `drive_level`, and `drive_level` supplies essentially all of the
34x observed range since `benefit_magnitude` varies by only ~1.5% CV. A magnitude-keyed split
was mathematically never going to show a meaningful gap, independent of whether SD-024's
mechanism works.

## 2. Claim-layer mapping

**SD-024** (`design_decision`, status `candidate`). `depends_on`: SD-004 (implemented), SD-014
(candidate, but not exercised by this driver -- a stale/loose architectural dependency, not a
live-blocking one for this test), MECH-232 (stable; claims.yaml's own implementation_note already
flags the `depends_on` as stale since SD-024 supplies MECH-232's first test rather than being
gated by it).

Claims.yaml's own `what_would_answer` for SD-024 (text added 2026-09-06, commit `ada5d97af0`,
**predating GFLAG-0246** raised 2026-09-09) already splits the falsifier into two parts:

1. **CONFIRMING (mechanism)** -- C1, C2 (MECH-233 asymmetry via C4), C5 (MECH-094 gate) -- already
   satisfied by V3-EXQ-900.
2. **CONFIRMING (the residual, not yet tested)** -- explicitly: *"V3-EXQ-900 measured
   `mean_benefit_magnitude` at cluster>=2 (0.5577) and at cluster==1 (0.5582) as effectively
   identical, so benefit magnitude is not the discriminator in vivo and `drive_level` is the
   untested lever."* This is the exact same number GFLAG-0246 flags, already correctly scoped
   as an open residual requiring a future `da_allocation_scale` x `drive_level` dose-response
   sweep -- not a test this run was designed to run.

The experiment ran under conditions where the claim's mechanism sub-clause could express itself:
real substrate call path (spy-captured, never reconstructed from formula), a real live
`REEAgent`/`CausalGridWorldV2` rollout, non-degenerate pooled sample.

## 3. Biological-reference triage

`evidence/literature/targeted_review_sd_024/` carries five dedicated entries, all pre-dating this
autopsy:

| Source | Direction | Confidence | Relevance to the flagged concern |
|---|---|---|---|
| Retailleau & Morris 2018 | supports | 0.75 | D1-gated map plasticity is real and causal; caveat: evidences reorientation, not density expansion specifically |
| Krishnan et al. 2022 | supports | 0.82 | CA1 dopaminergic ramp is **expectation/proximity-dependent**, not raw-magnitude-dependent -- directly predicts a flat magnitude-keyed split |
| Xiao et al. 2020 | mixed | 0.58 | Reward cells respond mostly to delivery, not expectation -- flags the delivery-vs-expectation question as genuinely open in the literature |
| Duvelle et al. 2019 | weakens | 0.70 | **No modulation of place-cell activity by goal VALUE** in two hippocampal subfields -- also predicts a flat magnitude split |
| Shao et al. 2025 | mixed | 0.55 | A pure gain-modulation alternative mechanism (no allocation) reproduces the same phenomenon -- exactly what C2's weight-independent density read is designed to distinguish from |

**Key finding:** two of the five sources (Krishnan 0.82, Duvelle 0.70) actively **predict** that a
raw reward-magnitude-keyed split should be flat -- the mechanism the literature supports is
expectation/proximity-gated (Krishnan), and value/magnitude specifically has been found NOT to
modulate hippocampal representation in at least one careful study (Duvelle). The V3-EXQ-900
flat-magnitude readout is therefore a **confirmed prediction from the existing evidence record**,
not an anomaly requiring explanation. Biological reference: **clear**, not absent -- GFLAG-0246's
implicit premise that this needed fresh biological grounding does not hold; the grounding already
existed and points the same direction as the run's own numbers.

MECH-233 (harm/benefit asymmetry) is separately grounded via Jimenez 2018 (BLA vs VTA pathways,
cited in the claim's own notes) -- not re-derived here since C4 is a clean, well-powered
(1403 harm calls) negative existential.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact for C1 (representational) + C4 (asymmetry); unclear for the functional-propagation sub-clause | test let the claim's mechanism sub-clauses express itself; the "functional" half of the label is NOT actually discharged by the combination rule as computed -- see Section 5/9 |
| Biological reference | clear on the core phenomenon | 5-entry targeted lit review exists; Krishnan supports the SD-012 scaling formula (does not predict magnitude-insensitivity); Duvelle predicts the OPPOSITE of the substrate's linear formula on the magnitude axis, untested here (corrected after red-team, see Section 9 Defect B) |
| Prerequisites | present | SD-004 implemented, MECH-232 stable; SD-014 (candidate) not exercised by this driver |
| Implementation | complete | allocation + harm-path asymmetry exercised via spy recorders on the real call path; the density READ used for gating (delta) is a code-level substitution not reflected in the driver's own pre-registered acceptance text |
| Environment | adequate | SD-024 is explicitly a workaround for ARC-057's environment-richness constraint; this design is deliberately wall-independent, so environmental sparsity does not bear on C1/C4 |
| Measurement | adequate for C1/C4; MISLEADING for C2 | manifest field `C2_cluster_size_vs_density` is computed on `density_delta`, not the pre-registered raw `density` -- confirmed by direct recompute: raw-density rho = 0.1775 (<0.30); delta is substantially arithmetic in cluster_size and jitter geometry (see Section 9 Defect A) |
| Integration | coupled | real REEAgent + real CausalGridWorldV2 episode loop for the live P1 rollout; only the P0 sweep and bandwidth diagnostic (correctly excluded from the gate) use throwaway isolated ResidueField instances |
| Scale/capacity | likely insufficient for PRECISION, adequate for the pre-registered GATE | R3 floor (5) cleared by exactly 1 event (6 measured); C1 is leave-one-out robust (min 0.495) -- not a construction artifact, but a thin sample for point-estimate precision |

**Failure-location (GOV-FAILLOC-1):** not applicable in the standard sense -- this is a PASS, not
a FAIL, and no bucket reads "REE FAILED." Recorded for completeness: Implementation adequate,
Measurement adequate, Environment adequate (for what this run tests) -- if anything this
strengthens the PASS rather than triggering a failure-location classification.

## 5. Adjudication of GFLAG-0246's specific ask (CORRECTED after adversarial red-team, Section 9)

**This section was substantially revised after the Step 7c red-team pass found the initial
draft's central rebuttal was itself wrong. The correction is folded in below rather than left
as a separate contradicted draft; see Section 9 for the full contest.**

> "Adjudicate whether the flat benefit-magnitude readout falsifies, qualifies, or is simply out
> of scope for SD-024's functional clause, and whether a 6-event expansion arm can carry it."

**Falsifies:** No. `benefit_magnitude` is not a functional readout of the allocation mechanism's
output at all -- it is the mechanism's INPUT (the environmental reward value, near-constant at
CV~1.6%), not something the mechanism produces or modulates. A flat split on a near-constant input
carries no information for or against the claim, by construction. **Confirmed independently by
the red-team pass (Section 9); this specific sub-finding stands.**

**Qualifies, but not in the way GFLAG-0246 itself points at.** The flag's OWN cited evidence (the
flat `benefit_magnitude` split) is a red herring, as above. But GFLAG-0246's underlying WORRY --
"NOTHING in the rule tests the FUNCTIONAL half" -- turns out to be **substantially correct**,
reached via a different route the flag did not name. The manifest's own recorded criterion
`C2_cluster_size_vs_density` (measured 0.5166, PASS) is **not** computed on the raw `density`
field the driver's own "PRE-REGISTERED ACCEPTANCE" section names (lines 97-100, 155-157: "C2
rho(cluster_size, density) >= RHO_LIVE_MIN") -- it is computed on `density_delta`, the
event-marginal contribution (`evaluate()` line 722; documented in code comments, lines 462-471 and
717-722, as a fix for a field-history confound found during a pre-run probe). Recomputed directly
from `per_seed_rows`: **`rho(cluster_size, RAW density) = 0.1775`, below the 0.30 bar**, on this
run's own live data. Further, `density_delta` is substantially an ARITHMETIC function of
`cluster_size` and the fixed jitter/bandwidth geometry -- confirmed: the single-center delta is
1.0 to 6 decimal places for all 51 such events, and the per-cluster delta matches
`exp(-E[||jitter||^2]/(2*bw^2)) ~= 0.49` per allocated center almost exactly -- so C2-on-the-delta
is close to a re-run of the P0 synthetic sweep (R2, rho=1.0) with live jitter noise added, not an
independent test of whether allocation propagates into the STANDING density signal field.py's own
docstring identifies as "the signal the SD-025 curiosity drive follows." At the smallest cluster
size (n=2), one of two observed events reads LOWER density at the contact point than a single
center would (delta 0.958 < 1.000) -- direct evidence against "more centers -> more density read
here" as a live-tested proposition, not merely a hypothetical concern.

This is independently corroborated by a **pre-existing, already-governance-visible flag**:
GFLAG-0249 (raised the same cycle, 2026-09-09, status `resolved`) states verbatim: *"V3-EXQ-900's
PASS label asserts a FUNCTIONAL half that no criterion tests while the one functional
discriminator recorded is flat to 0.09 percent (GFLAG-0246)"* and its resolution explicitly defers
"whether the bar turns out unattainable may invalidate the run's VERDICT" to a future governance
decision. This autopsy IS that decision for this one instance: it does not invalidate the PASS's
representational (C1) and asymmetry (C4) evidence, but it does invalidate the label's functional
half and the current claims.yaml C2 characterization ("measured 0.517", stated without noting it
is the delta-based figure).

**Out of scope:** No longer the right characterization for the CORE concern (see above) -- it IS
in scope, and the combination rule genuinely does not test it. It remains true that the STRONGER,
downstream-behavioural-consequence sense of "functional" (does the density difference change
committed action) is a separate, correctly out-of-scope residual per claims.yaml's own
`what_would_answer` (2026-09-06) and SD-025's falsifier -- that part of the original draft's
reasoning stands.

**Six-event expansion arm:** Sufficient to clear the pre-registered non-degeneracy gate (verified
independently: 6 distinct cluster sizes present in the pooled sample), and the readiness
thresholds were fixed before the run and attainable in either direction. The red-team's
leave-one-out check shows C1 is robust to dropping any single expansion event (minimum 0.495,
still clears 0.30) -- the PASS does not hinge on one event, on its own DV. It carries no
information toward the functional/C2 question, but that is Defect A above, not a sample-size
problem.

**Net adjudication:** narrow-supports. The PASS robustly confirms the REPRESENTATIONAL (C1) and
MECH-233 ASYMMETRY (C4) sub-clauses of SD-024. It does NOT establish, on this run's own
pre-registered terms, that the resulting structural difference propagates into the standing
density signal the rest of the substrate reads -- the properly-operationalized version of that
test (raw density) measures below threshold. SD-024 stays candidate; `evidence_direction` stays
`supports` (narrowed, not reversed) because the two clauses that DO hold are real, well-powered,
and claim-confidence-bearing in their own right.

## 6. Repair pathway

**No substrate build, no re-queue, no lit-pull is owed.** `add_residue_cluster` behaves exactly as
specified; the n=2 density-reduction is a parameter-geometry fact (jitter 0.3 in 16-d vs bandwidth
1.0), not a code defect -- it should be recorded, not built against. The five-entry lit review is
sufficient; the earlier draft's problem was in reading two of those entries, not in their
existence.

**The owed action is a corrected governance note**, not merely a confirming one: update SD-024's
`evidence_quality_note` to record (i) the flat-magnitude finding is cleared and uninformative, (ii)
the manifest's C2 field is delta-based, not the pre-registered raw-density statistic, which
measures 0.18 and fails, (iii) the PASS is therefore `narrow_supports: true` for C1+C4 only, and
(iv) the residual dose-response sweep (already identified in claims.yaml) should ALSO vary
`benefit_magnitude` at pinned `drive_level` (the axis Duvelle 2019 and the substrate's own formula
make opposite predictions on), alongside the already-planned `drive_level` sweep -- full text under
`recommended_evidence_quality_note` in the JSON artifact. SD-024 stays `candidate`. This future
sweep is not queued from this autopsy (per CLAUDE.md's rule that a `/failure-autopsy` session does
not chip follow-on that depends on its own not-yet-governance-reviewed finding) -- governance chips
it once this artifact is ratified.

**GFLAG-0246 resolution recommendation:** resolve as `resolved` (the flag's core concern is
substantially validated, not dismissed), resolution_note citing this artifact and stating plainly
that GFLAG-0246 was right about the underlying worry and wrong only about which recorded number was
the functional discriminator. This also closes, for this one instance, the "may invalidate the
run's VERDICT" question GFLAG-0249 (already resolved, same cycle) deferred to a future governance
decision -- cite both flags in the resolution. The SEPARATE V3-EXQ-795 concern GFLAG-0246 also
raises (diagnostic PASS, no confirmed autopsy, tags SD-024+SD-025) is out of scope for this
single-target dispatch and is already independently surfaced by `pending_review.md`'s purpose-keyed
diagnostic-autopsy-required section for the next `/governance` cycle -- not chipped from here, per
Scope Discipline.

## 7. Granularity-debt / re-derive-brake checks

No prior `failure_autopsy_*.json` names SD-024 (`grep -l '"SD-024"' failure_autopsy_*.json` ->
empty) -- this is the first autopsy touching this claim. Re-derive brake: N/A (0 prior
substrate_ceiling hits). Granularity-debt recurrence: N/A (no recurrence cluster; count = 1).

## 8. Hypothesis-space ledger (Step 9b)

No `fanout_recommendation` emitted (no live discrimination bottleneck among named rivals) and no
pre-registered hypothesis in `hypothesis_space_registry.v1.json` matches this run (`da_density_
approach` and `curiosity_diversity_vs_amplifier` are both distinct, unrelated questions). Step 9b
does not apply -- skipped cleanly.

## 9. Adversarial red-team pass (Step 7c)

**Run on a different model from the drafting session** (drafting session: Sonnet 5; red-team
agent: Fable 5.1), per the skill's cross-model requirement. The agent was given the raw manifest,
driver source, and the draft's STATED CONCLUSION only, with the drafting reasoning withheld; it
was instructed to read the manifest and driver and recompute at least one load-bearing number
itself before reading the draft.

**VERDICT: CONTESTED.**

> The draft's headline answer to GFLAG-0246's literal ask -- "the flat `mean_benefit_magnitude`
> split does NOT falsify SD-024" -- is CORRECT and I confirm it. But two of the things the
> autopsy ASSERTS on the way to that answer are wrong against the artifact's own cells and the
> cited sources.
>
> **Defect A (gate that cannot discriminate by construction, graded "adequate").** C2 is not a
> test of "functional": it is computed on `density_delta`, which is identically 1.0 for every
> single-center event and is `n x mean-kernel-at-jitter` for a cluster -- an arithmetic
> consequence of `compute_local_density`'s kernel sum, and exactly the statistic the P0 readiness
> sweep (R2) already certifies. The pre-registered form of C2, `rho(cluster_size, density)`,
> measures 0.177 on this manifest, below the 0.30 bar; the driver's own comment records that it
> was swapped to the delta after a pre-queue probe found 0.18 on a 57-event live sample. The
> draft praises the swap as "a genuinely careful design choice" and rests its central "functional
> is already operationalised and passing" argument on C2. GFLAG-0246's original reading ("nothing
> in the rule tests the functional half") is substantially right.
>
> **Defect B (inference on an unstated premise / literature over-read).** The draft calls the
> flat split "a confirmed prediction from the existing evidence record" (Krishnan, Duvelle). The
> Krishnan summary says nothing about magnitude-independence (it supports the SD-012
> `benefit x drive` scaling). The Duvelle summary predicts value-insensitivity of biology and
> explicitly says that if REE's density scales with `benefit_magnitude` "that is a divergence
> from the biology" -- and the substrate formula commits to exactly that scaling. The run has no
> `benefit_magnitude` variance so it confirms nothing either way.

Full findings, including the recomputed-number table (every load-bearing number recomputed
independently from `per_seed_rows`, matching the draft's arithmetic in every case except the two
defects above), per-seed and leave-one-out robustness checks, cheap confirmers, and honest bounds
on the red-team's own inference, are preserved at
`REE_assembly/evidence/planning/redteam_failure_autopsy_V3-EXQ-900_2026-09-14.md` (landed alongside
this artifact).

**Both defects were independently verified by the primary autopsy author before being folded into
Sections 3-6 above** (direct recompute of `rho(cluster_size, density)` = 0.1774784301256333;
direct read of `field.py` `compute_local_density`/`add_residue_cluster`, confirming
`density_delta` is deterministic in cluster_size and jitter geometry to within floating-point
precision for single centers; direct read of the Krishnan and Duvelle `summary.md` files;
independent discovery that GFLAG-0249, already resolved the same cycle, states the exact same
characterization verbatim and names GFLAG-0246 as the linked instance).

The red-team's own honest-bounds section notes it could not confirm whether the "Step 4 probe"
that motivated the delta swap used the identical live sample this run measured, or a
coincidentally-matching one (deterministic seeding makes either possible) -- immaterial to the
finding, since either way the DV was redefined after the pre-registered form was observed to fail
at this configuration, and the docstring's formal acceptance text was never updated to match.

**Net effect on the autopsy: Sections 3-6 above were rewritten to incorporate both defects.** No
part of the red-team pass reversed the top-line "does not falsify" answer to GFLAG-0246's literal
question; it corrected WHY, and surfaced a materially more important finding (the C2 mismatch)
than the one the flag itself pointed at.
