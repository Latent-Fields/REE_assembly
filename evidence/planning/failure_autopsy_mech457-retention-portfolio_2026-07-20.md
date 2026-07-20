# Failure Autopsy -- MECH-457 retention portfolio (V3-EXQ-789, read jointly with V3-EXQ-788)

- **Generated:** 2026-07-20T15:30:07Z
- **Session:** `malloc-stack-autopsy-extended-a0e312`
- **Scope:** single FAIL adjudicated (V3-EXQ-789); V3-EXQ-788 (clean PASS) read alongside for the
  joint discrimination but **not** adjudicated here -- it clears at the `/governance` walk.
- **Status:** confirmed (user-gated 2026-07-20)
- **Machine-readable companion:** `failure_autopsy_mech457-retention-portfolio_2026-07-20.json`

---

## Headline

**The retention sub-question is decided: the VALUE ESTIMATOR sets retention; the imitation
auxiliary does not.** The two legs of the GOV-FANOUT-1 retention pair were queued together and
resolve in opposite directions with a large margin between them.

| Leg | Run | Result |
|---|---|---|
| `H-retention-critic` | V3-EXQ-788 (**PASS**) | distributional critic **retains 1.839** of installed competence vs **0.525** scalar; margin 1.314 against a required 0.15 |
| `H-retention-auxiliary-decay` | V3-EXQ-789 (**FAIL**) | **every schedule decays**: retained fraction 0.191 constant / 0.408 annealed / 0.046 off, all under the 0.5 floor, **0/3 seeds retained on all three arms** |

A distributional critic does not merely preserve the installed policy -- at 1.839 it **exceeds**
it, i.e. competence continues to improve under RL refinement. No auxiliary schedule achieves even
half-retention.

---

## 1. Facts (V3-EXQ-789)

**Manifest:** `outcome: FAIL`, `evidence_direction: unknown` (diagnosis-pending marker),
`non_degenerate: true`, `degeneracy_reason: ""`,
`discrimination_verdict: retention_auxiliary_succeeded_then_decayed`.
DIAGNOSTIC by purpose -- promotes and demotes nothing.

**Readiness is clean -- this is not an unready substrate.** Per arm:

| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| `post_bc_install_took` (worst seed, THE load-bearing readiness gate) | **17.75** | 1.0 | true |
| `local_view_greedy_clears_floor_at_d3` | 48.05 | 1.0 | true |
| `greedy_oracle_clears_floor_at_d3` | 57.20 | 1.0 | true |
| `competence_trajectory_readings` (worst cell) | 12 | 2 | true |

`n_seeds_install_took: 3` on the constant arm, `install_took_strict_majority: true`. So there
**was** an installed prior to decay -- the half-life is short, not undefined, and the run
self-routes a retention verdict rather than `substrate_not_ready_requeue`.

**Primary result:**

| Arm | retained_fraction (mean) | per-seed | n retained | half-life (mean) |
|---|---|---|---|---|
| `retaux_constant` | 0.191 | [0.039, 0.419, 0.114] | **0/3** | 416.7 |
| `retaux_annealed` | 0.408 | -- | **0/3** | 333.3 |
| `retaux_off` | 0.046 | -- | **0/3** | 250.0 |

`n_did_not_decay_by_arm`: 0 on every arm. `n_half_life_undefined_by_arm`: 0 on every arm. Every
seed of every schedule installed competence and then lost more than half of it.

**Recording provenance: COMPLETE** -- `recording_schema`, `substrate_hash` (`c71e9af5...`),
`substrate_stable_across_run`, `machine_class`, `elapsed_seconds` (9082.6), full `config`,
explicit `seeds` [42, 43, 44]. The reference band and denominators are recorded
(`local_view_ceiling_738: 48.05`, `bc_expert_748: 32.72`, `greedy_oracle_742: 57.2`,
`rnd_novelty_plateau_751: 5.22`), so the result is interpretable against known anchors.

**Schedule verification passed:** the annealed arm's realised `bc_aux_coef` moved
(`bc_aux_schedule_drop_worst_annealed: 0.5`, `bc_aux_coef_first_worst_annealed: 0.5`), so it did
not alias onto the constant arm. The anti-alias control held too: `use_distributional_critic`
stays False on all three arms, which is 788's locus -- the two legs are genuinely independent
manipulations.

---

## 2. The secondary discrimination is measurement-limited (record, do not re-queue)

`half_life_ordered_by_persistence: true` -- constant 416.7 >= annealed 333.3 >= off 250.0, the
predicted direction. But the criterion **fails**, and the honest reason is resolution:

- `retention_probe_every: 250`, so **half-life is quantised to multiples of 250 episodes**.
  Per-seed values on the constant arm are literally `[750, 250, 250]`.
- The observed spread across arms is **166.7 episodes -- smaller than one measurement quantum.**
- The pre-registered margin (`half_life_margin_episodes: 450`, 0.15 of budget) is 1.8 quanta.

So the ordering is directionally consistent and **numerically unresolvable at this probe
resolution**. It should be read as neither support nor refutation of a schedule effect.

**Two DVs disagree, and this is worth recording.** Half-life orders constant > annealed > off,
while retained_fraction orders **annealed (0.408) > constant (0.191) > off (0.046)**. Half-life
measures when competence *first* halves; retained_fraction measures where it *ends up*. They
dissociate, and with 0/3 retained on every arm neither ordering changes the primary verdict. A
successor pursuing the schedule question would need to state which DV it is powering for.

---

## 3. Claim-layer mapping

`MECH-457`. Both runs are **DIAGNOSTIC** by declared purpose and promote/demote nothing; they
resolve pre-registered legs of the `competence_floor` question rather than weighting the claim.

The joint result is the substantive one. V3-EXQ-780 had already established that a *persistent
but fixed* auxiliary (`bc_aux_coef=0.5` throughout) still lost competence 20.933 -> 11.667, which
is what motivated testing the SCHEDULE dimension. 789 closes that dimension: **no schedule of the
imitation auxiliary rescues retention.** 788 then shows the actual lever is the value estimator.

This is a positive, decision-grade finding and should be surfaced as such rather than buried under
789's FAIL: the retention failure that has dogged the competence-floor campaign has a identified
cause and a working fix.

---

## 4. Biological-reference triage

- **Closest reference mechanism:** the distinction between an imitation/observational teaching
  signal and a value-based reinforcement signal in skill retention -- corticostriatal consolidation
  where an acquired policy is maintained by a value estimator rather than by continued
  demonstration.
- **Missing-dependency signature? YES, and it is the informative kind.** The failure looks exactly
  like what happens biologically when a skill is acquired by demonstration but has no value
  signal maintaining it: acquisition succeeds, then the behaviour extinguishes as the ongoing
  objective competes it away. 789's own hypothesis label states this
  ("the imitation auxiliary is out-competed by the RL objective over training"), and the data
  match: install takes on 3/3, then decays on 3/3, at every auxiliary weight.
- **This makes 789 a positive-negative result.** Its elimination of the auxiliary axis is
  *evidence for* the value-estimator dependency that 788 independently confirms. The two legs
  corroborate rather than merely partition.

---

## 5. Four-layer diagnosis (V3-EXQ-789)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened** (for the auxiliary leg specifically) | tested fairly; install took on 3/3, every schedule decayed |
| Biological reference | clear | matches demonstration-without-value-maintenance extinction |
| Prerequisites | present | BC install floor cleared; local-view and oracle anchors clear |
| Implementation | complete | schedule verification passed; anti-alias control held |
| Environment | adequate | D3, reference band fully recorded |
| Measurement | **adequate for the primary DV, under-instrumented for the secondary** | retained_fraction decisive; half-life quantised at 250 episodes vs a 166.7 spread |
| Integration | coupled | read jointly with 788 by design |
| Scale | adequate | 3 seeds x 3 arms, 12 trajectory readings on the worst cell |

**Recommended `epistemic_category`: `standard`. Recommended `evidence_direction`: `weakens`**
(for `H-retention-auxiliary-decay`; the manifest's `unknown` was a diagnosis-pending placeholder).

---

## 6. Learning extracted

1. **Retention is set by the value estimator, not by the teaching signal's persistence.** A
   distributional critic retains 1.839 of installed competence while every auxiliary schedule
   retains under 0.5. This is the campaign's answer to why installed competence decayed.
2. **A distributional critic does more than preserve -- it improves.** Retained fraction above 1.0
   means competence continued rising under RL refinement after the BC install, which is a stronger
   result than the leg's PASS criterion required.
3. **Queuing a fan-out pair as a PAIR is what made this decidable in one cycle.** 788 and 789 share
   the reference build and hold `use_distributional_critic` fixed off in 789 as an anti-alias
   control, so the two manipulations do not confound each other and the contrast is clean.
4. **A DV read off a trajectory cannot resolve an effect smaller than its probe interval.** Half-life
   quantised at 250 episodes cannot adjudicate a 166.7-episode spread. Set the probe interval from
   the smallest effect the criterion is meant to detect, not from compute convenience.
5. **When two DVs of the same construct disagree in ordering, say so.** Half-life and
   retained_fraction rank the arms differently here; both are consistent with the primary verdict
   (0/3 retained everywhere), but a successor must declare which one it powers for.
6. **A branched None is worth the design cost.** Recording `undefined_no_install` and
   `did_not_decay` as distinct statuses rather than coercing them is what lets this run assert
   "short half-life" instead of "no measurement" -- both counts are 0, which is itself part of the
   verdict.

---

## 7. Routing

**No re-queue. Close the auxiliary axis** (user-confirmed 2026-07-20).

- **`H-retention-auxiliary-decay` -> ELIMINATED.** The full bar is met: control passed (install
  took 3/3, positive controls clear), `non_degenerate: true`, adjudicated direction `weakens`.
- **The 788 critic result supersedes the axis.** Pursuing auxiliary schedules further would
  optimise a lever shown to be the wrong one while the working lever is already identified.
- **The schedule sub-question is recorded as unresolvable at this resolution, not re-queued.** If
  it is ever reopened, it needs `retention_probe_every` cut to roughly 50 and a declared choice of
  DV. There is currently no reason to spend that compute.
- **No `/implement-substrate`.** Nothing is blocked; the substrate delivered the install and the
  trajectory.

**Re-derive brake:** does not fire. MECH-457 has 0 `substrate_ceiling` hits under the R1-R3
convention, and this autopsy recommends `standard` rather than a ceiling.

**Follow-on the pipeline already owns (reported, NOT chipped):** two `competence_floor` legs remain
`alive` -- `H-retention-consolidation` (whose substrate `mech457_policy_kl_anchor` is already
`implemented` in `substrate_queue.json`) and `H-consummation-binding`. Both are pre-registered and
will be re-derived by the next `/governance` walk.

### Draft `evidence_quality_note` for governance (do NOT apply from this skill)

> 2026-07-20 (failure autopsy, V3-EXQ-789 read jointly with V3-EXQ-788): the MECH-457 retention
> sub-question is decided -- the VALUE ESTIMATOR sets retention, the imitation auxiliary does not.
> 789 tested the auxiliary's persistence schedule (constant 0.5 / annealed 0.5->0.0 / off) with
> `use_distributional_critic` held False on all arms as an anti-alias control. Readiness was clean
> (post-BC install took on 3/3 seeds, worst 17.75 against a 1.0 floor; local-view greedy 48.05;
> oracle 57.2; non_degenerate true), so this is a real null: retained fraction 0.191 / 0.408 /
> 0.046 against a 0.5 floor with 0/3 seeds retained on EVERY arm, and 0 arms failing to decay.
> V3-EXQ-788 independently shows a distributional critic retains 1.839 of installed competence
> (exceeding it) against 0.525 scalar, margin 1.314 against a required 0.15. Together these
> eliminate `H-retention-auxiliary-decay` and confirm `H-retention-critic`. Both runs are
> DIAGNOSTIC and weight no claim. The schedule sub-question is NOT resolved and is not re-queued:
> half-life is quantised at the 250-episode probe interval while the observed cross-arm spread is
> 166.7 episodes, so the (directionally correct) ordering constant >= annealed >= off is below one
> measurement quantum. Note also that half-life and retained_fraction rank the arms differently.

---

## 8. Ledger delta (Step 9b)

**Mode B (resolve only)** on question `competence_floor`. No growth event; no denominator change.

- `H-retention-auxiliary-decay`: `alive` -> **`eliminated`**, `resolving_runs: ["V3-EXQ-789"]`,
  `evidence_direction: weakens`, `epistemic_category: standard`, `control_passed: true`,
  `non_degenerate: true`, `met_elimination_bar: true`,
  `resolved_utc: 2026-07-20T11:21:03Z` (the run's own completion date).

`H-retention-critic` is left untouched here: V3-EXQ-788 is a clean PASS with no adjudication flag,
so per the skill it clears at the `/governance` walk rather than through an autopsy. Its
resolution is governance's to apply.

---

*Adjudicated by session `malloc-stack-autopsy-extended-a0e312`. Inputs: the V3-EXQ-789 manifest
(interpretation.preconditions, headline, per_arm_retention, reference_band, denominators,
load_bearing_dv, notes); the V3-EXQ-788 manifest (headline, discrimination_verdict) for the joint
read only; `hypothesis_space_registry.v1.json` question `competence_floor`;
`substrate_queue.json` (`mech457_policy_kl_anchor`, `sd_actor_critic_action_learning`).*
