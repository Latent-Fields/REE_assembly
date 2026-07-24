# Failure Autopsy: V3-EXQ-786a DV degeneracy (MECH-163 leg 1 re-adjudication)

**Generated:** 2026-07-24T07:30:45Z
**Status:** confirmed (interactive gate cleared with user 2026-07-24)
**Scope:** single (re-adjudication of an already-confirmed target)
**Run:** `v3_exq_786a_mech163_dual_system_recruitment_20260721T113809Z_v3`
**Queue ID:** V3-EXQ-786a
**Claims:** MECH-163
**Supersedes:** `failure_autopsy_V3-EXQ-786a_2026-07-22` (confirmed `weakens`)

## 1. Why this re-adjudication exists

The DV degeneracy was discovered 2026-07-22 by session `hopeful-panini-cf272d` while building the
SD-081 dualsystem-arbitration substrate (MECH-477) -- it was the reason 811's design deliberately
diverged from 786a's. The finding was recorded in `WORKSPACE_STATE.md` ("THE FINDING THAT MATTERS
MOST...") with the explicit note that re-adjudicating 786a "is `/failure-autopsy` + `/governance`
work ... applied nowhere." This is exactly the un-adjudicated-terminal-set blind spot governance's
own Step 1.5a exists to close, except it never even reached `pending_review.md` -- 786a was already
in `reviewed_run_ids` under the old (now-withdrawn) verdict, so the standard walk could not surface
it. Found this cycle only by reading `WORKSPACE_STATE.md` narrative context, not by any automated
scan.

## 2. Facts -- verified independently, not taken on report

`evaluate_trajectory` scoring in the driver (`experiments/v3_exq_786a_mech163_dual_system_
recruitment.py:598`, function `_depth_scores`):

```python
full.append(float(agent.residue_field.evaluate_trajectory(world_seq)[0].item()))
first.append(float(agent.residue_field.evaluate_trajectory(world_seq[:, :1, :])[0].item()))
```

`world_seq[:, :1, :]` is index 0 of the world-state sequence -- the CURRENT state, shared by every
candidate before any trajectory diverges. Independently confirmed at the source-code level (not
merely from the prior session's WORKSPACE_STATE note): this slice is structurally identical across
all 32 candidates.

**Consequence for the recruitment DV** (`recruitment = 1 - spearman(full, first)`): `first` is a
CONSTANT vector. A Spearman rank correlation against a constant reduces to a comparison between the
genuine full-horizon ranking and an ARBITRARY stable-sort tie-break ordering of ties -- pure noise,
not signal. The prior session's own re-derivation confirmed this on 786a's actual `_depth_scores`:
`n_unique = 1` across all 32 candidates, range exactly 0 on every scored tick.

**The noise has a specific, checkable distribution.** Simulating the tie-break-Spearman process over
200 draws at K=32 gives mean 1.0173, sd 0.1871. The manifest's actual seed-0 familiar-condition
`recruitment_rate` is **1.01725**, per-layout sds 0.149-0.207 -- matching the simulated noise
distribution to **five significant figures**. This is not a plausible coincidence; it is the
manifest reporting exactly what a degenerate DV would report.

**Why the readiness gate did not catch it.** `candidate_score_range_non_degenerate` gates the
FULL-HORIZON score range only (verified: the driver's `score_ranges` list is built from `full`, not
from `first`). The degenerate first-step vector was never checked, so the run passed readiness
cleanly and self-reports `non_degenerate: true` -- correctly, for the one thing it checks, and
silently wrong for the DV that actually needed it.

## 3. Adjudicating the self-route

`no_differential_recruitment` (flat response, recruitment delta mean 0.00435, Cohen's d 0.047) was
the self-route, and the original 786a autopsy read this as the "no-arbitrator" signature -- a flat
response being exactly what two pathways WITHOUT an arbitrator should produce. That reading assumed
the DV could, in principle, have detected a non-flat response if one existed.

**It could not have.** A DV that is guaranteed to return noise-around-a-fixed-mean by construction
cannot discriminate "flat because no arbitrator" from "flat because the instrument cannot see
differential recruitment at all." **Verdict: WITHDRAWN as a gate defect -- but unlike the
790/791/689i gate defects earlier this cycle, the underlying science is NOT upheld here.** Those
defects left a load-bearing criterion that still passed cleanly on the corrected denominator. Here
there is no criterion left standing: the entire recruitment statistic is noise.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear -- not tested | MECH-163 leg (1) could not express itself through this instrument regardless of ground truth |
| Biological reference | clear, not at issue | dual-systems well-evidenced; irrelevant to this purely-instrumentation finding |
| Prerequisites | n/a | -- |
| Implementation | n/a | defect is in the diagnostic script, not the substrate |
| Environment | n/a | -- |
| Measurement | **DEGENERATE (dominant)** | constant first-step vector -> Spearman-vs-tie-break noise; readiness gate checked only the full-horizon range |
| Integration | n/a | -- |
| Scale | n=8, irrelevant | the DV carries no signal at any sample size |

**Recommended `epistemic_category`: `measurement_test_design_defect`.**

## 5. Learning extracted

1. A Spearman correlation against a constant vector produces NOISE with a specific, simulatable
   distribution -- not an obviously-degenerate "0" or "nan" that a naive check would catch. It can
   look like a clean, well-behaved null on visual inspection of the manifest.
2. A readiness gate must check EVERY input to a difference/ratio/correlation statistic, not just the
   more prominent one. `candidate_score_range_non_degenerate` gated the full-horizon range and missed
   the first-step vector the same statistic also depends on.
3. This is the SECOND consecutive iteration of this diagnostic family (786 -> 786a) found to carry a
   measurement defect on re-derivation rather than at design time. Budget explicit toy-case
   verification for a third iteration before trusting a clean-looking manifest.

## 6. Repair pathway

**MECH-163 leg (1) reverts to experimentally UNTESTED** (its pre-786a state: literature-only, 9
supports, 0 experimental entries), pending a non-degenerate re-test. `V3-EXQ-811` does NOT
substitute for this -- it tests whether adding an explicit arbitrator (MECH-477) produces
differential recruitment, which is a different (though related) question from whether the bare dual
pathways show it.

**MECH-477 is NOT undermined by this finding.** Its motivating OBSERVATION (786a's flat response)
is weakened as a rationale for having registered the claim, but 811's own design was built
specifically to correct this exact defect (`HABIT_DEPTH=2` rather than the degenerate depth-1 read,
plus new readiness gates on the habit vector's own range and distinct-value fraction) and measured a
real, non-degenerate effect (Cohen's d 0.999 ON vs -0.158 OFF, per the confirmed
`failure_autopsy_V3-EXQ-811_2026-07-24`). MECH-477 stands on 811's own merits.

Recommend `/queue-experiment` for a genuine leg-1 re-test using the same readiness-gate pattern 811
introduced (gate the DV's OWN input vector's range/distinct-fraction, not a proxy quantity), if
leg (1) is to be tested again -- new letter, same question, repaired instrument (the 785->785a /
708->708a shape).

### Draft `evidence_quality_note` (governance to write -- do not apply here)

See the JSON artifact's `recommended_evidence_quality_note` for the full text.

## 7. Confirmed routing (user-adjudicated 2026-07-24)

User confirmed **"Autopsy inline now (Recommended)"** -- this document closes the debt named in
`WORKSPACE_STATE.md` 2026-07-22 and never routed. `weakens` -> `non_contributory` for MECH-163;
MECH-477 unaffected (stands on V3-EXQ-811's independent, non-degenerate evidence).
