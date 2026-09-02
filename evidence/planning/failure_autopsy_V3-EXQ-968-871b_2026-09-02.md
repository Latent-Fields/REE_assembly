# Failure autopsy -- V3-EXQ-968 (SD-E1 residual A/B) + V3-EXQ-871b (MECH-090 short-circuit)

Generated 2026-09-02T05:04:59Z. Status: **confirmed** (interactive gate, 2026-09-02).
Red-team pass: Fable -- 968 **CONFIRMED**, 871b **CONTESTED** (contest accepted; artifact revised).

Both are `experiment_purpose: diagnostic` PASSes with self-routed labels. Neither manifest carries
`interpretation.preconditions[]`, so the indexer's adjudication flag never fired on either -- they
reached this skill through the purpose-keyed net, which is exactly what that net is for.
Dry-run gate: both clean (968 has no `dry_run` key; 871b explicit `false`).

## V3-EXQ-968 -- "residual_no_material_difference" is a threshold artifact

**PASS certifies readiness, not a result.** `status = "PASS"` (driver:1170) and `"passed": True`
(:1176) are hardcoded literals; the only reachable FAIL is P0-readiness-unmet (:1092).

**The arms genuinely differed** -- all four `arm_fingerprint`s are distinct and the flag is plumbed
(driver:347 -> `config.py:8077` -> `e1_deep.py:629,957,975`). So this is not an inert manipulation.

**The effect is large and opposite in sign across seeds.** Recomputed from `per_seed_lift`:

| seed | lift | vs bar 3.0 |
|---|---|---|
| 42 | 0.005909 / 0.002673 = **2.2108** | misses by 26% |
| 123 | 0.000923 / 0.002717 = 0.3396, i.e. inverse **2.9443** | misses by **1.86%** |

Raw `cr_rollout_spread_h1_*` ratios are 2.2926 and 0.3616, both formed RES/ABS with the same sign
flip echoed in the `action_probe` spreads -- **no ratio inversion; the opposite-direction reading
is real.** Both bars are missed narrowly in opposite directions, so `n_exceeds = 0` and
`n_below = 0`, and the label falls through to the final `else:` branch. The driver's own
`mixed_across_seeds` label needed one seed to clear 3.0.

The 3.0 bar is floor-bound: `max(3.0, 2.0 x 1.01637) = 3.0`, where the noise ratio is estimated
from **2 samples**. Logged unfixed as red-team finding (4) in the queue note (ree-v3 `4b3b312`).

Lineage precedent: the confirmed V3-EXQ-965 autopsy -- 968's own declared `source_autopsy` -- had
already recorded that this driver family's C1 control arm is analytically pinned.

**Governance impact is nil**: `claim_ids: []` and the run sits in `unlinked_runs`. Recorded so the
label does not later get read as a null. Honest caveat: at n=2, "sign-heterogeneous effect" and
"seed-unstable residual arm" are not distinguishable (ARM_residual varies 6.4x across seeds vs
1.6% for ARM_absolute).

## V3-EXQ-871b -- "shortcircuit_working_confirmed" overstates, but less than first drafted

**(1) No control arm.** Both `arm_results` rows are `A_HIER_S5` with both probe flags true. The
"pre-fix 0.0" baseline is asserted by construction (driver:344-347), and 871a could not have
measured it (`chunk_max_size=2` yields zero opportunities).

**(2) The confirming numerator was never at risk.** `opportunity_continuation_rate` is exactly 1.0
in both cells, 0 counter-examples in 77 ticks. The driver predicate (:665-673) coincides with the
substrate gate (`agent.py:7202-7222`) on step-idx and chunk-source; the only escape is a beta
release, and **`beta_elevated` is true on 959/959 ticks in both cells**. The gate's beta conjunct
is constant where the design requires it to vary.

**(3) The prescribed DV IS measured, and sits at its mechanical floor.** This corrects the first
draft, which said it "remains unmeasured". 871b computes `n_genuine_commits / n_e3_ticks`:
83/94 = 0.883 and 53/99 = 0.535 (871a: 113/103, 103/93). Decomposing the 83 over `tick_records`
gives **73 exhausted-chunk E3 ticks + 10 episode starts + 0 opportunity re-commits** -- so the
driver's own <=0.5 working ceiling was arithmetically unreachable in seed 101 by any short-circuit
behaviour. The right reading is not "the DV was substituted away" but "the DV is at floor and
cannot discriminate at this chunk supply".

MECH-090's registered non-degeneracy precondition (`n_genuine_commits_identity_based <
n_e3_ticks + n_episodes_probe`) **is** satisfied -- 83<104, 53<99 -- so the 871a defect signature
is genuinely absent and the wiring fix is genuinely exercised. C2 is nonetheless direction-agnostic
(`shortcircuit_inert_confirmed` also passes), so PASS certifies that a discrimination was reached,
not that the fix works.

## Four-layer summary

| Layer | 968 | 871b |
|---|---|---|
| Claim alignment | n/a (claim-free) | unclear -- precondition met, DV at floor |
| Implementation | complete, genuinely plumbed | complete, path exercised |
| Measurement | misleading (hardcoded PASS; else-branch label) | misleading (1.0 rate; beta constant) |
| Integration | coupled | **isolated -- no control arm** |
| Scale | under-powered (2-sample noise floor) | under-powered (77 ticks) |

**Failure-location (GOV-FAILLOC-1): MEASURES for both.** Neither is chargeable to REE.

## Routing (confirmed at gate)

Both `queue-experiment`. For 968: re-read as a heterogeneity finding, not a null; the successor
needs a noise floor estimated from more than 2 samples. For 871b: a successor needs a real control
arm and a chunk supply under which the DV can exceed its floor. MECH-090's substrate hold is
discharged; ARC-071 keeps `substrate_conditional` but **re-grounded on LEG 3's missing
chunk-boundary instrument** -- its LEG 2 justification is now stale. The existing
`mech317-action-chunk-boundary-instrument` substrate entry is on point and is named rather than
duplicated.
