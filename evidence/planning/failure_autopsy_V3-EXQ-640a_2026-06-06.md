# Failure Autopsy -- V3-EXQ-640a (SD-057 cue-authority gain sweep)

- **Generated (UTC):** 2026-06-06T04:08:44Z
- **Target run_id:** `v3_exq_640a_scaffold_cue_authority_gain_sweep_20260606T013614Z_v3`
- **queue_id:** V3-EXQ-640a
- **machine:** ree-cloud-2
- **scope:** single (measurement-only behavioural diagnostic)
- **status:** confirmed (interactive gate completed 2026-06-06)
- **predecessor:** V3-EXQ-640 (single-point cue_recall_gain=0.2 measurement; autopsy
  `failure_autopsy_V3-EXQ-640_2026-06-05`)
- **routing autopsy applied:** `failure_autopsy_V3-EXQ-640_2026-06-05` Section 7 interpretation grid

## 0. Not a crash

`outcome: PASS` here means only the **measurement-success gates** passed (C1 cue fires on
>= a majority of cells on >= 2/3 seeds; C2 post-cue trace captured). The scientific result is
carried by `evidence_direction: non_contributory`, `claim_ids: []`, `experiment_purpose:
diagnostic`. The non-standard direction value is the diagnosis-pending signal this autopsy
resolves; the interpretation grid is applied here at review (the experiment MEASURES, it does
not adjudicate).

## 1. Scope

Single diagnostic. The experiment is the measurement successor to V3-EXQ-640: a 2-axis factorial
(`cue_recall_gain` {0.2, 1.0, 5.0} x `incentive_drive_kappa_weight` {2.0, 10.0}, 6 cue-on cells +
ARM_OFF reference, 3 seeds 42/43/44 each) over the landed SD-057 cue-recall bridge on the
`scaffolded_sd054_onboarding` substrate (post-cue instrumentation amend, 2026-06-05). The 640
single-point measurement is the (gain=0.2, kappa=2.0) cell of this sweep.

## 2. Facts (no interpretation)

Pre-registered question: do per-cue-fire `cue_zgoal_pull_norm` AND post-cue approach-rate lift
over the within-run background rise **monotonically** as `cue_recall_gain` (and incentive-token
strength) increase?

Per-cell aggregate (sweep_read.cells), pull = `mean_cue_zgoal_pull_norm`,
lift = `mean_approach_lift_over_background`:

| cell | gain | kappa | pull | approach_lift |
|---|---|---|---|---|
| g0.2 k2  | 0.2 | 2.0  | 0.00241 | -0.00244 |
| g1   k2  | 1.0 | 2.0  | 0.00207 | -0.0000131 |
| g5   k2  | 5.0 | 2.0  | 0.00674 | -0.000484 |
| g0.2 k10 | 0.2 | 10.0 | 0.00321 | -0.00588 |
| g1   k10 | 1.0 | 10.0 | 0.00299 | -0.00248 |
| g5   k10 | 5.0 | 10.0 | 0.00432 | -0.00349 |

- `pull_monotonic_nondecreasing_in_gain`: **false** (both kappa rows).
- `approach_lift_monotonic_nondecreasing_in_gain`: **false** (both kappa rows).
- **Approach lift is flat-to-negative in every one of the 6 cue cells.** No cell lifts approach
  above its own within-run background.
- Absolute `mean_zgoal_norm_at_cue_fire`: ~0.52-0.54 (seed 42) / ~0.43-0.45 (seeds 43/44) vs
  ARM_OFF `mean_zgoal_norm_all_steps` = **0.4246**. The cue is firing every step
  (`n_cue_fire_steps == n_steps_total` in every cell) and holds z_goal at a standing elevated
  bound.
- `mean_cue_action_bias_norm`: **null in every cell** (`n_cue_action_bias_present = 0`).
- `p2_contact_rate`: **0.0 in seeds 42 and 43** for most cue-on cells; seed 44 makes contact
  (0.06-0.37). ARM_OFF seeds 43/44 make contact (~0.36).
- `hazard_interrupt_rate`: 0.41-0.92 across cells (P2 env hazard_food_attraction=0.7).

**Which "criterion" was the read:** the experiment's gates are measurement-only and PASSed; the
scientific read is the monotonicity question, which is answered NO on both the pull axis and the
approach-lift axis. The decisive behavioural fact is that **a 25x cue_recall_gain sweep and a 5x
kappa sweep move neither the pull nor the approach lift** -- this was the experiment's designed
near-full-snap probe.

## 3. Reading the metrics correctly (before claim mapping)

1. **The per-fire `cue_zgoal_pull_norm` is ~0 because of saturation, not weakness.** The cue
   fires on every step and holds z_goal at its pulled bound (~0.5 absolute vs 0.42 OFF). The
   per-fire incremental delta is small because z_goal is already there. The *absolute*
   `zgoal_norm_at_cue_fire` (the truer readout) IS elevated above the OFF reference. **The cue
   does reach z_goal.** This is the key correction: the literal branch-3 reading ("cue_pull
   primitive under-powered / clipped") is undercut by the saturation -- the pull metric was the
   wrong instrument for "does the cue move z_goal."
2. **The null `cue_action_bias_norm` is the SD-016 `cue_action_proj` (`agent._cue_action_bias`),
   which is independently documented as ungrounded** (ree-v3/CLAUDE.md SD-016: action_bias ~= 0.0
   unless `use_differentiable_cem=True`). It is a *separate* known issue, not the cue-recall
   mechanism's fault, and does not bear on the cue-recall -> z_goal -> MECH-295-approach path.
3. **The load-bearing finding is the approach lift.** `post_cue_approach_rate` =
   `sum_move_improved_postcue_steps / n_postcue_eval_steps`, where `move_improved = dist_after <
   dist_before` (Manhattan distance to nearest resource). Even immediately post-cue, the agent is
   no more likely to move toward a resource than its own background -- across the entire 25x5
   sweep.

## 4. Biological-reference triage

- **Closest mechanism:** cue-triggered wanting / sign-tracking / Pavlovian-instrumental transfer
  (PIT) -- Berridge 2009; Corbit & Balleine 2005/2011. A cue retrieving an incentive value biases
  *approach*.
- **Faithful translation vs formal import:** faithful translation (SD-057 L6 cue-recall is
  anchored to specific PIT, not a formal-definition import). No biology-lit gap drives this
  autopsy; lit grounding already exists (SD-057 design doc + targeted reviews).
- **Dependency-absence signature:** YES. REE's translation lands the cue -> incentive-retrieval
  -> z_goal step (incentive salience) but the **z_goal -> approach (instrumental-transfer /
  PIT-expression) step is silent**. In biology PIT expression requires an intact instrumental
  pathway with authority over action selection; in REE that is **MECH-295 liking-bridge + E3
  goal_proximity**. The failure matches "the instrumental-transfer pathway is present but does not
  translate the elevated incentive into action selection" -- a discovered-prerequisite signature,
  not a falsification of the cue-recall claim.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (diagnostic) | implicitly probes SD-057/MECH-347 (L6 cue authority) + MECH-346/MECH-295 (z_goal->approach). Mechanism DID express (cue fired, z_goal elevated) -> the negative result is contributory about the propagation layer, not a falsification of cue-recall. |
| Biological reference | clear | PIT: cue->incentive lands; incentive->approach (instrumental transfer) silent -- missing-dependency signature. |
| Prerequisites | missing / immature | GAP-2 foraging competence: 2/3 seeds zero contact under the harsh P2 env. |
| Implementation | partial | cue_pull -> z_goal works (z_goal elevated); MECH-295/E3 goal_proximity lacks selection authority to convert elevated z_goal into approach; SD-016 cue_action_proj separately ungrounded (null action bias). |
| Environment | wrong pressures (for this measure) | P2 hazard_food_attraction=0.7 makes the cued food hazard-attracting; high hazard_interrupt_rate (0.41-0.92) -> the very approach being measured is harm-penalised. |
| Measurement | misleading (partially) | per-fire pull saturates (cue every step); absolute z_goal norm is the truer readout and shows elevation. The monotonicity question on pull is partly answered "metric saturated." |
| Integration | **isolated -- headline** | z_goal elevated but does not propagate to E3 action selection across the full 25x5 sweep. |
| Scale / capacity | adequate | 25x gain / 5x kappa ruled magnitude out -- the designed probe. |

**Recommended epistemic_category:** `substrate_ceiling` (the substrate has the cue->z_goal
wiring but the z_goal->approach propagation under the current MECH-295 / E3-goal_proximity
substrate does not carry behavioural authority at the granularity the cue-recall claim needs;
the right response is substrate enrichment of the selection-authority layer, not more cue-gain
experiments). Paired with `pending_retest_after_substrate` (see Section 7 re-test gate).

**638b hard-constraint: CONFIRMED -- do NOT build V3-EXQ-638b.** Cue authority over z_goal is
present and magnitude is not the bottleneck; the 638b interoceptive need-gating substrate gates
*cue firing*, which would not fix a *z_goal -> approach propagation* gap.

## 6. Cluster note

Not run as a cluster, but the shape is convergent with the recently-routed
`modulatory-bias-selection-authority` cluster (604a/624a/614d, autopsy 2026-06-03): small fixed
modulatory biases (~0.05-0.1) added to primary scores with a much larger raw_score_range never
change the committed argmin ("drowning"). The MECH-295 cue/approach bias is another modulatory
channel exhibiting the same shape here -- z_goal is elevated but the approach bias has no
authority over E3 selection. This convergence is the load-bearing structural read: the bottleneck
is the **selection-authority layer**, shared across curiosity (MECH-314), vigor (MECH-320),
within-class diversity (MECH-341), and now cue-recall approach (MECH-295/SD-057).

## 7. Learning extracted + repair pathway

**Learning:**
1. SD-057 cue-recall reaches z_goal (absolute z_goal elevated ~0.5 vs 0.42 OFF; cue fires every
   step) -- *positive* evidence the L6 cue->z_goal wiring is intact. The cue-recall claim is NOT
   falsified.
2. The bottleneck is **z_goal -> approach propagation**: approach lift is flat/negative across a
   25x gain x 5x kappa sweep. Magnitude at the cue-pull stage is ruled out as the cause.
3. The propagation gap is the **same selection-authority shape** as the 604a/624a/614d cluster --
   modulatory bias drowning against larger primary scores at E3.select.
4. The per-fire `cue_zgoal_pull_norm` metric saturates and is the wrong instrument for "does the
   cue reach z_goal"; future readouts should use absolute z_goal-at-cue-fire vs an OFF reference.
5. The clean propagation re-test is confounded by GAP-2 foraging competence (2/3 seeds zero
   contact) and the hazard-attracting P2 env penalising the measured approach.

**Repair pathway (user-confirmed at the interactive gate):**
- **Primary routing: `implement-substrate` (amend) on `modulatory-bias-selection-authority`.**
  The cue-recall approach bias (MECH-295 + cue-driven z_goal) is a modulatory channel that needs
  the gap-relative selection authority the substrate provides. Add a 640a failure record so the
  substrate's validation surface covers the cue-recall approach channel (alongside the
  MECH-314/320/341 levers it already unblocks).
- **Re-test gate (GAP-2 confound):** the clean propagation re-test is `blocked_pending` the
  in-flight `scaffolded_sd054_onboarding` foraging-competence residual delivering non-zero contact
  on >= 2/3 seeds (so the approach-lift measurement is meaningful). Until then the propagation gap
  is diagnosed but not cleanly re-measurable.
- **Do NOT build V3-EXQ-638b** (hard constraint confirmed by this autopsy).

**Draft `evidence_quality_note` governance MAY attach (this skill does NOT write it):**

- For MECH-295 / SD-057 (MECH-346/MECH-347): "V3-EXQ-640a (cue-authority gain sweep, diagnostic,
  claim_ids=[]) confirmed SD-057 cue-recall reaches z_goal (absolute z_goal_norm_at_cue_fire ~0.5
  vs 0.42 OFF; cue fires every step) but a 25x cue_recall_gain x 5x kappa sweep produced NO
  post-cue approach-lift over within-run background in any of 6 cells -- the z_goal -> approach
  propagation (MECH-295 liking-bridge / E3 goal_proximity) lacks selection authority over E3.
  Same selection-authority shape as the 604a/624a/614d modulatory-bias cluster. Magnitude at the
  cue-pull stage ruled out. epistemic_category substrate_ceiling on the propagation layer;
  pending_retest_after_substrate (modulatory-bias-selection-authority validation) AND blocked on
  GAP-2 foraging competence (2/3 seeds zero contact). NOT evidence against the cue-recall claim
  (the cue->z_goal step is intact); NOT a 638b build trigger."

## 8. Interactive gate

AskUserQuestion answered 2026-06-06:
- Routing primary = **Propagation gap (MECH-295/E3)** (branch 2).
- GAP-2 confound = **Re-test gate** (record propagation-gap diagnosis as primary; mark clean
  re-test blocked_pending GAP-2 foraging-competence substrate delivering non-zero contact).
