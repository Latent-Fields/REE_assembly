# INV-063: P1 fails on the converged base too; and the InfoNCE pinning is a readout-temperature artifact

**Status: AWAITING USER REVIEW. Nothing here has been written to claims.yaml or any other
registry. The four-arm intake ladder was NOT queued.**

- Session `metaworker-science-20260919-inv063-four-arm-intake-ladder` (ree-cloud-4),
  2026-09-19, acting on the user decision of 2026-09-19T21:42:30Z.
- Governance flag raised as instructed: **GFLAG-0364** (`contested_disposition`, INV-063),
  carrying the exact proposed leg-B wording. `claims.yaml` untouched.
- Probe sources + raw output: umbrella branch
  `claude/metaworker-science-20260919-inv063-four-arm-intake-ladder`,
  `scratch/probe_p1_mel_converged.py` / `scratch/p1mel.out`,
  `scratch/probe_infonce_structure.py` / `scratch/infonce.out`.

---

## 1. The instructed stop fired: P1 fails on the converged base

The decision said: *"P1's MEL spread (0.10 vs its 0.25 floor on 1060's base) must be
re-measured on the converged base BEFORE queueing; if it still fails, stop and report the
number."*

Re-measured in V3-EXQ-798a's two-phase form -- recon-only P0 world-forward convergence on the
STABLE no-shift env, then a **FROZEN** MEL window (optimiser withheld) in the arm's own env,
MEL = mean `e3_prediction_error` over 900 steps. 798a's validated ladder unchanged:
`world_rule_shift_interval` {0, 60, 25, 10} at depth 2. 4 arms x 3 seeds.

Convergence reached and confirmed: `conv_rel_drop` **0.9980 / 0.9967 / 0.9992**, comfortably
above the 0.9967 V3-EXQ-1063 recorded as converged.

| seed | NONE | LOW (60) | MED (25) | HIGH (10) | strictly monotone | **relative spread** |
|---|---|---|---|---|---|---|
| 42  | 1.4967e-4 | 1.4878e-4 | 1.6895e-4 | 1.7238e-4 | no | **0.1369** |
| 123 | 8.4377e-5 | 8.7071e-5 | 8.3800e-5 | 1.0222e-4 | no | **0.1802** |
| 456 | 8.4320e-5 | 8.4067e-5 | 9.2530e-5 | 9.4268e-5 | no | **0.1082** |

**0/3 seeds clear P1's 0.25 relative-spread floor. 0/3 are strictly monotone.**
On V3-EXQ-1060's unconverged base the same check gave 0.097 / 0.105 / 0.104. So P1 now fails
on BOTH bases.

**This blocks the four-arm ladder independently of leg B.** P1 gates the INTAKE MANIPULATION
-- the independent variable. Without a graded ladder there is nothing for either leg's DV to
be monotone in, whichever readout leg B uses.

### 1a. The caveat, stated rather than buried

**V3-EXQ-798a's landed run got spread 0.483 / 0.659 / 0.685 and monotone 3/3 at these
identical arm settings, and that result stands.** My P0 deviates from it: 798a drives 5400
steps through the full E3 selection path, this used 3600 steps of a random-action rollout
(chosen because 798a's form is ~3 hours for this grid against ~1 hour, and because V3-EXQ-1063
measured the random-action form reaching the same `conv_rel_drop`). The measurement window is
798a's.

The two runs also differ in MEL LEVEL by ~5x: 798a measured 1.5e-5..3.8e-5, this measures
8.4e-5..1.7e-4. Same knob, same arms, same frozen-window definition. **That discrepancy is
unexplained and is the thing to resolve before the ladder can be queued** -- it is not
established that P1 fails under 798a's own P0. The honest reading is: *under the P0 form this
session could afford, P1 fails; whether it fails under 798a's is untested.*

Resolving it means one run of the ladder's P1 phase with 798a's exact P0 (E3-selection, 5400
steps), ~3 hours of cloud compute. That spend is the user's call.

## 2. The decision's premise: D2 is recorded unciteable by the run it comes from

The decision cites *"D2 InfoNCE improves 3/3 on the converged base, D1 MSE 0/3"*. D1 0/3 is
solid. D2's 3/3 carries a qualification the decision did not have:

V3-EXQ-1063 PRE-REGISTERED an InfoNCE readability condition -- set BEFORE the run, from
V3-EXQ-1060's landed numbers -- and **D2 FAILED it**. The landed manifest records
`criteria_non_degenerate.D2_converged_base_infonce_improves = false`, and its own
`degeneracy_reason` says verbatim that D2 and D4 *"are degenerate and must NOT be cited in
either direction."*

- measured InfoNCE headroom 0.02152 against a required 0.20794 (5% of ln K)
- the readout sat at **99.48%** of its chance value ln(64) = 4.158883
- D2's cross-seed SD (2.458e-3) is **78% of its own mean** (3.171e-3)

So the 3/3 was a sign test on a statistic pinned at chance. Three positives out of three is a
1/8 outcome under a fair coin -- suggestive, not significant at any conventional level, and
the pre-registered gate says this readout could not carry the test.

## 3. But that is FIXABLE, and this is the new result

Measured this session on a converged base (`conv_rel_drop` 0.998 / 0.997 / 0.999), inspecting
the readout's own [K,K] squared-distance matrix:

**The representation DOES discriminate.** Diagonal squared distance 1.5e-4..2.4e-4 against
off-diagonal 2.1e-3..3.6e-3 -- the correct target is ~10-15x closer than the average
distractor. The signal is present.

**The pinning is entirely the readout TEMPERATURE.** `world_forward_contrastive_loss` forms
`logits[i,j] = -||pred_j - target_i||^2 / tau` (`e2_fast.py:396-403`) and defaults to
`tau = 0.1` (`:359`). Dividing distances of order 1e-3 by 0.1 gives logit spreads of ~0.03 --
far too flat to separate. Headroom below ln(K), by temperature:

| tau | seed 42 | seed 123 | seed 456 |
|---|---|---|---|
| 1.0 | 0.08% | 0.06% | 0.05% |
| **0.1 (shipped)** | **0.75%** | **0.57%** | **0.52%** |
| 0.01 | 5.44% | 4.34% | 4.30% |
| **1e-3** | **23.88%** | **21.61%** | **23.45%** |
| 1e-4 | 35.02% | 48.26% | 42.69% |
| 1e-5 | numerically broken (loss ABOVE ln K) | same | same |

At `tau = 1e-3` the readout clears the 5%-of-ln(K) readability floor on all three seeds with
4x margin. `temperature` is an explicit argument to the loss, so this is a READOUT
re-specification, not a substrate change.

**Two caveats.** (a) `offdiag.min - diag.max` is NEGATIVE on all three seeds, so the task is
not perfectly separable -- which is desirable here (it leaves dynamic range) but means the
readout is not a clean accuracy measure. (b) The loss's docstring says it is built for *"K
sibling CEM candidates SHARING z_world_0 but differing in first action a_i"* -- an
ACTION-discrimination task. V3-EXQ-1060 and 1063 both call it on the frozen battery, i.e. 64
DIFFERENT states carrying only 5 distinct action classes between them
(measured histograms [14,11,11,14,14] / [18,12,9,15,10] / [11,13,11,16,13]). The task as
called is STATE-identity discrimination. Well-formed, but not the one the helper was designed
for, and the amendment wording should say which task leg B means.

## 3a. C1/C2 reachability on InfoNCE, verified from 1063's recorded numbers

Asked for by the Orchestrator's correction of 2026-09-19T22:30Z. Answer: **not
determinable from V3-EXQ-1063 -- and moot, because section 1 blocks the ladder upstream of
either criterion.**

**First, a units correction the correction itself needs.** The figure **0.2079 is NOT what
C2 requires.** It is `0.05 * ln(64)` -- the READABILITY floor V3-EXQ-1063 pre-registered
(`INFONCE_HEADROOM_FLOOR_FRAC = 0.05`), which asks whether the readout can carry a sign test
*at all*. C2's 20%-of-highest-arm term is `0.20 * (highest arm's DV)` =
`0.20 * 3.171e-3` = **6.343e-4**, expressed in DV units. Two different quantities. The
correction's *conclusion* -- that InfoNCE may lack dynamic range -- is right, but it is right
for the readability reason, not the C2 reason, and the two must not be merged because only
one of them is measured.

| question | determinable from 1063? | number |
|---|---|---|
| Is the readout READABLE (headroom vs 5% of ln K)? | **yes** | 0.02152 vs 0.20794 -- **fails by 9.66x**, at the shipped `tau=0.1` |
| Is **C1** (monotone across 4 intake arms) reachable? | **no** | 1063 ran NO ladder, so it holds no arm-to-arm effect size |
| Is **C2**'s 20%-of-highest-arm term reachable? | yes, in principle | 6.343e-4, against a DV of 3.171e-3 |
| Is **C2**'s `2 x SD(arm-to-arm DELTA)` term reachable? | **no** | 1063 has ONE arm per (base, lever) cell, so it contains **zero** arm-to-arm differences |

The only related quantity 1063 records is the cross-seed SD of a per-arm **LEVEL**:
2.458e-3, which is **77.5% of the DV's own mean**. If the arm-to-arm *difference* SD were as
large as that level SD, C2's margin would be 4.916e-3 = **1.55x the entire DV** and C2 would
be unreachable. If seed effects largely cancel in the difference -- plausible, since all four
arms of a seed share one base and one battery -- it could be far smaller. **1063 cannot
distinguish those, and no amendment is needed to C2's rule: it self-computes from the
four-arm run's own data.**

**The MSE alternative is noisier, not less noisy.** D3 (unconverged base, MSE) is 2/3 positive
with mean 2.966e-3 and cross-seed SD 3.579e-3 -- `SD/|mean| = 1.21`, i.e. its cross-seed
scatter EXCEEDS its own mean, against 0.775 for InfoNCE on the converged base.

**And a readout with more range already is recorded** -- it is the same InfoNCE at a
re-specified temperature (section 3): headroom 21.6-23.9% of ln K at `tau = 1e-3` against
0.5-0.8% at the shipped `tau = 0.1`.

**None of which unblocks anything**, because section 1's P1 failure is upstream of every one
of these: it gates the intake manipulation, so no choice of leg-B readout gives the ladder an
independent variable.

## 4. What this leaves open for the user

1. **P1.** Spend ~3 hours re-measuring the ladder's P1 phase under 798a's exact P0 to find out
   whether the failure is real or an artifact of the cheaper P0 -- or accept that the intake
   ladder is not currently gradeable and route INV-063 to `substrate_conditional` via its own
   escape hatch.
2. **Leg B's readout.** If leg B stays InfoNCE, the amendment in GFLAG-0364 should pin the
   readout temperature (`tau = 1e-3` on the evidence above) and say whether the task is state-
   identity or action discrimination. At the shipped `tau = 0.1` the readout cannot carry
   C1/C2 at all.
3. **C2's margin.** The registered rule (`max(2 x pooled cross-seed SD of the arm-to-arm
   delta, 20% of the highest arm's DV)`) IS fully fixed and self-computes from the four-arm
   run's own data, so no amendment is needed for it. But it **cannot be set from V3-EXQ-1063**,
   which contains no arm-to-arm difference at all -- only a per-arm level. The level SD is 78%
   of the DV mean; whether the arm-to-arm difference SD is comparable or much smaller (seed
   effects largely cancelling) is not determinable from 1063.
