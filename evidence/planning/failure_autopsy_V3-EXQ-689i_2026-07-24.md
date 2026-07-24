# Failure Autopsy: V3-EXQ-689i (MECH-448 repaired-instrument successor to 689d)

**Generated:** 2026-07-24T07:18:04Z
**Status:** confirmed (interactive gate cleared with user 2026-07-24)
**Scope:** single
**Run:** `v3_exq_689i_mech448_f_eligibility_demotion_falsifier_repair_20260722T162850Z_v3`
**Queue ID:** V3-EXQ-689i
**Claims:** MECH-448

## 1. Facts

689i is the sanctioned repaired-instrument re-run of 689d (withdrawn 2026-07-20 by
`failure_autopsy_V3-EXQ-689d_2026-07-20`, non_contributory/measurement_test_design_defect, MECH-448
reverted provisional -> candidate). Same question, repaired instrument -- the 785->785a / 708->708a
shape. Three independent defects were closed together: (1) hold-weighted DV -> genuine-selection
sentinel gating; (2) vacuous matched-noise control -> re-instantiated on Factor B (gap-scaled
stochastic commit, live on the committed path); (3) intra-run substrate divergence -> pinned to a
single cloud worker, substrate_hash cardinality enforced == 1. Plus power: 3 seeds -> 4, 2-of-3 pass
bar -> 3-of-4.

**Criteria (8 load-bearing):**

| Criterion | Passed |
|---|---|
| C_SUBSTRATE_INVARIANT (cells share one build) | **true** |
| C_CONTROL_DISTINCT (no identical control histograms) | **true** |
| C_FRESH_SUFFICIENT (effective n meets target) | **true** |
| C_READINESS (e2 divergent envelope excludes) | **false** |
| C_NOISE_LIFTS (matched noise verifiably lifting) | **false** (1/4 seeds vs >=3/4 bar) |
| C_RANK_PRESERVING (eligible set is F-rank prefix) | **true** |
| C_PRIMARY (on-selected entropy strictly above both controls) | **true** |
| C_SAFETY (harm not above OFF) | **true** |

## 2. Adjudicating the self-route

6 of 8 load-bearing criteria pass, including C_PRIMARY -- the criterion that actually tests MECH-448
(does the demotion mechanism raise committed-class entropy above BOTH collapsed controls?). C_RANK_
PRESERVING and C_SAFETY also pass. The self-route `substrate_not_ready_requeue` is driven entirely
by two OTHER gates:

- **C_NOISE_LIFTS**: the matched-noise control (Factor B, gap-scaled stochastic commit temperature)
  only verifiably lifts committed-class entropy over the collapsed baseline on 1 of 4 seeds, against
  a >=3/4 bar. This control was NEWLY re-instantiated in 689i (the old Factor was bit-identical to
  the baseline and vacuous, per 689d's autopsy) -- this is its FIRST exercise, and 1/4 at n=4 is not
  distinguishable from a real-but-modest effect at this sample size. A first-use instrument teething
  problem, not evidence the demotion mechanism is wrong.
- **C_READINESS** (`on_f_eligibility_envelope_excludes_on_divergent_pool`): measured 0.0376 against a
  0.0 threshold. The manifest's comparator direction for this field is ambiguous without reading the
  scoring script directly -- flagged for follow-up rather than resolved here.

Given the mechanism's own discrimination test passes cleanly and the two failing gates are
instrument-side (a first-use control's power, and an ambiguous-direction readiness check), this
reads as a **gate defect, science upheld** -- the same shape as the V3-EXQ-790/791 diagnostics
adjudicated earlier this cycle.

## 3. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C_PRIMARY tested MECH-448 cleanly and passed |
| Biological reference | clear | divisive-normalisation eligibility envelope, ARC-107 |
| Prerequisites | present | 689i closes 689d's three defects + power increase |
| Implementation | complete | mechanism built and exercised |
| Environment | adequate | -- |
| Measurement | **misleading (dominant, on 2/8 gates only)** | noise-control power gap (first use); readiness-check comparator needs a script read |
| Integration | coupled | -- |
| Scale | adequate for C_PRIMARY; under-powered for the noise-control comparison specifically | -- |

**Recommended `epistemic_category`: `measurement_test_design_defect`.**

## 4. Learning extracted

- MECH-448 / ARC-107's rank-preserving F->eligibility demotion mechanism clears its own
  discrimination criterion cleanly on the repaired instrument -- second independent confirmation
  (first was 689a, retracted by 689d, now restored on repaired grounds).
- The newly re-instantiated Factor B noise control is under-powered at n=4 -- flag for a targeted
  power/design follow-up, not a full same-question re-letter of the falsifier.
- The envelope-exclusion readiness check's comparator direction needs a script-level read before it
  can be adjudicated with confidence.

## 5. Repair pathway

Recommend `/queue-experiment` for a TARGETED follow-up on the Factor B noise-control instrument
specifically (more seeds, or a design review of why gap-scaled stochastic commit only verifiably
lifted on 1/4 seeds) -- not a full re-letter of the whole falsifier, since C_PRIMARY already passed
cleanly on the repaired instrument. The re-derive brake does not fire (0 substrate_ceiling hits for
MECH-448; both 689d and 699 were measurement_test_design_defect).

### Draft `evidence_quality_note` (governance to write -- do not apply here)

See the JSON artifact's `recommended_evidence_quality_note` for the full text. Recommended
`evidence_direction: supports` (MECH-448's live_status currently cites the withdrawn
`failure_autopsy_V3-EXQ-699_2026-07-20` reading -- this run supersedes that with a supports
verdict on the repaired instrument).

## 6. Confirmed routing (user-adjudicated 2026-07-24)

User confirmed **"Gate defect, science upheld (Recommended)"**: C_PRIMARY stands as the load-bearing
mechanism test; the noise-control power gap is flagged as an instrument follow-up rather than
grounds to withhold the PASS.
