# Failure Autopsy -- V3-EXQ-705b (MECH-314 curiosity-conversion under F->eligibility demotion, adaptive floor)

- generated_utc: 2026-06-25T18:53:00Z
- run_id: v3_exq_705b_mech314_curiosity_conversion_demotion_adaptive_floor_20260625T100722Z_v3
- queue_id: V3-EXQ-705b (supersedes V3-EXQ-705)
- claim: MECH-314 (structured-curiosity conversion; candidate)
- status: FAIL / evidence_direction non_contributory (self-routed `conversion_ceiling_persists_despite_demotion`)
- adjudication: CONFIRMED (interactive gate, user-approved)

## 1. Scope

Single-target autopsy. Considered as a possible cluster with V3-EXQ-704 -- **NOT a cluster** (opposite
failure shapes; see the 704 autopsy Step 1). This is the pre-registered **brake-lock terminal off-ramp**
for the MECH-314 curiosity-conversion lineage.

## 2. Facts (no interpretation)

705b is the LETTER successor to 705 (the scientific question is unchanged: does the MECH-314 curiosity
channel convert to committed-action-class diversity when the MECH-448/ARC-107 F->eligibility demotion is
ON and *genuinely excluding*?). 705 self-routed `substrate_not_ready_requeue` because its FIXED 0.30
envelope floor all-admitted (excluded_count==0 on 2/3 seeds) -- the demotion never narrowed the pool. The
confirmed failure_autopsy_V3-EXQ-705_2026-06-25 routed 705b with the fix: `use_f_eligibility_adaptive_floor`
(689e-validated) on every arm + a hardened legC readiness gate (excluded_count>0 required before the lift
is scored).

3 arms x 3 seeds, all `use_f_eligibility_demotion=True` + `use_f_eligibility_adaptive_floor=True`, MECH-314
curiosity as the sole modulatory channel, `curiosity_candidate_source=e2_world_forward` (GAP-A pool).
**`use_go_nogo_constitution` (MECH-449) was OFF** (verified in the script: only demotion + adaptive floor).

**Observed -- the test was finally fair.** All 4 preconditions met:

| precondition | measured | threshold | met |
|---|---|---|---|
| gapA_e2_world_forward_action_divergence | 0.1070 | 0.02 | yes |
| curiosity_bias_range at non-saturation arm (w=0.25) | 0.00549 | 0.0001 | yes (fixes the 590c confound) |
| **f_eligibility_demotion_non_degeneracy (excluded_count)** | **14.45** | **>0** | **yes (vs 705's all-admit 0.0)** |
| rolled_out_zworld_magnitude_bounded | 0.216 | < 1e6 | yes |

Load-bearing criterion `mech314_committed_diversity_lift_over_f_only_and_noise` (non-degenerate per
`criteria_non_degenerate`): **passed = false** -- no committed-class-entropy lift over the demotion-ON
F-only + matched-noise controls. `metrics.json` empty; `interpretation` block is the source of truth.

## 3. Claim-layer mapping

MECH-314 asserts the structured-curiosity channel adds committed-action-class diversity. 705b is the first
*fair* test of that under the built ARC-107 demotion lever: the 705 all-admit confound is fixed (adaptive
floor excludes 14.45 candidates), the 590c saturation-arm confound is fixed (range read at the
non-saturation w=0.25 arm), the GAP-A pool is divergent. **Under all of that, the curiosity channel still
produced no lift.** This is the manifest's pre-registered `conversion_ceiling_persists_despite_demotion`
off-ramp, encoded verbatim in `interpretation.routing`:

> "legC MET (demotion genuinely excludes, excluded_count>0 on >=2/3 seeds) but no lift over the
> demotion-ON F-only + matched-noise controls -> the 705b autopsy fires the re-derive brake (6th) +
> routes to MECH-449 Go/No-Go (double-gated) / V4. non_contributory; NOT a falsification of MECH-314."

The claim is **not falsified**: the ceiling is upstream/architectural (a single rank-preserving eligibility
gate -- demotion -- arbitrating within the F-eligible set). MECH-314 stays candidate / unweakened /
pending_retest_after_substrate.

## 4. Biological-reference triage

Closest reference: frontopolar / rostrolateral-PFC uncertainty-driven curiosity (the behavioural-diversity
generation pathway, ARC-065). Curiosity in real brains drives *exploration*; the *conversion* of that
drive into committed-action-class diversity is gated downstream by the BG selector -- in REE's terms the
Go/No-Go eligibility constitution (MECH-449), not the demotion lever alone. The 705b failure matches a
**missing downstream dependency** (active No-Go converting a channel that rank-preserving demotion
structurally cannot), not a broken curiosity channel. This is the exact shape the substrate_queue already
records for the OFC devaluation case (485k->MECH-449): "demotion-alone converts the passive discrimination
signature but cannot express the active No-Go." Biological reference: **clear**; the failure is a
discovered prerequisite, not a falsification.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | MECH-314 not falsified; ceiling is upstream |
| Biological reference | clear | curiosity drives exploration; conversion gated by BG Go/No-Go (MECH-449) |
| Dependency / prerequisites | **missing in this test** | MECH-449 Go/No-Go was OFF; only demotion (MECH-448) active |
| Implementation completeness | complete (for what was armed) | demotion + adaptive floor correct; curiosity channel correct |
| Environment adequacy | adequate | GAP-A divergent pool, 3/3 |
| Measurement adequacy | adequate | fair, non-degenerate; the 705/590c confounds are fixed |
| Integration adequacy | single-gate | only the demotion eligibility gate active; the second (Go/No-Go) gate not composed |
| Scale / capacity | adequate | demotion genuinely excludes (14.45) |

**Dominant diagnosis:** `substrate_ceiling` -- the curiosity channel reaches the eligible shortlist and the
demotion genuinely narrows it, but committed-action-class diversity does not lift, because rank-preserving
demotion within the F-eligible set cannot, on its own, convert the curiosity channel to committed
authority. This is the MECH-439 F-dominance conversion ceiling, now established on a *fair* demotion test.

## 6. Re-derive brake (FIRES -- pre-registered 6th)

MECH-314 ceiling/non_contributory autopsy lineage (substrate_ceiling / non_contributory reads tagging
MECH-314):

1. failure_autopsy_EXQ-572-573_2026-05-17
2. failure_autopsy_604a-624a-630_2026-06-03
3. failure_autopsy_gapA-cluster-604b-648a-649_2026-06-07
4. failure_autopsy_V3-EXQ-590c_2026-06-24  (4th -- brake FIRED; routed to demotion-ON re-test)
5. failure_autopsy_V3-EXQ-705_2026-06-25   (5th -- brake NOT fired: confounded all-admit, not a clean ceiling; brake-LOCK recorded)
6. **this (705b)** -- 6th, the clean ceiling = the pre-registered brake-lock TRIGGER -> **FIRES**

**Consequence:** the brake **refuses a 705c demotion-only same-substrate letter** (another iteration of
the curiosity channel under the same single-gate demotion substrate is forbidden).

## 7. Routing (user-confirmed) -- corrected for the built MECH-449

The pre-registration named "route to MECH-449 Go/No-Go (double-gated) / V4". **Correction established
during this autopsy:** MECH-449 is **already BUILT, validated, and promoted to provisional** (`use_go_nogo_
constitution` in e3_selector.py; falsifier V3-EXQ-689g PASSED 3/3 seeds, conversion_rate 1.0,
constitution_excluded_median 4.0; status provisional / epistemic_category standard / v3). 705b ran with
Go/No-Go OFF. So the forward path is **not** an implement-substrate build -- the substrate exists.

- **Forward path: brake-EXEMPT /queue-experiment** -- re-test MECH-314 curiosity-conversion **DOUBLE-GATED**
  (`use_f_eligibility_demotion=True` AND `use_go_nogo_constitution=True`, curiosity the sole modulatory
  channel). This is a *different substrate condition* than the demotion-only lineage that accumulated the
  6 ceiling autopsies, so it is brake-exempt (the brake refuses same-substrate letters, not a new-substrate
  test). Precedent: the 485k->MECH-449 OFC devaluation route, and the 705/590c brake-release logic when the
  upstream substrate is built+validated. 689h already showed demotion x Go/No-Go compose ADDITIVELY (no
  interference), so the composition is well-posed.
- **recommended_substrate_queue_entry: action=none** (MECH-449 built 2026-06-21; no gap).
- **V4 / ARC-110 loop-segregation is the escalation ONLY if the double-gated re-test also fails to convert.**
- MECH-314: stays candidate / unweakened / pending_retest_after_substrate (behind the MECH-449 double-gated test).

## 8. Recommended governance writes (autopsy does NOT apply these)

- evidence_direction: `non_contributory` (already self-routed; SOUND -- no correction).
- recommended_epistemic_category: `substrate_ceiling`.
- MECH-314: no status change; stays candidate; pending_retest_after_substrate = true.
- Draft `evidence_quality_note` (governance to write):
  "V3-EXQ-705b (MECH-314 curiosity-conversion under MECH-448 demotion + 689e adaptive floor) is the first
  FAIR test of the curiosity channel under a genuinely-excluding demotion (excluded_count 14.45 vs 705's
  all-admit 0.0; 590c saturation-arm confound also fixed). With GAP-A pool divergent and the demotion
  genuinely narrowing, committed-action-class entropy still did not lift over demotion-ON F-only +
  matched-noise -> conversion_ceiling_persists_despite_demotion. non_contributory; MECH-314 UNWEAKENED
  (the ceiling is upstream -- a single rank-preserving eligibility gate; not a falsification of curiosity).
  epistemic_category substrate_ceiling; pending_retest_after_substrate. Re-derive brake FIRED (6th MECH-314
  ceiling autopsy, pre-registered brake-lock trigger): refuses a 705c demotion-only same-substrate letter.
  Forward path = brake-EXEMPT /queue-experiment double-gated re-test (demotion + the BUILT MECH-449 Go/No-Go
  constitution, which was OFF in 705b); substrate action=none (MECH-449 built+validated 689g); V4 ARC-110
  loop-segregation only if the double-gated test also fails."
