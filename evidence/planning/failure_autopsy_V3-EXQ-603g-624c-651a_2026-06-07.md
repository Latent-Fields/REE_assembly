# Failure Autopsy (CLUSTER) -- V3-EXQ-603g / 624c / 651a

- **Generated (UTC):** 2026-06-07T15:35:39Z
- **Scope:** cluster (3 targets)
- **Status:** confirmed (user adjudicated 2026-06-07)
- **Routed from:** /governance 2026-06-07T1520Z (all 3 pending FAILs deferred to autopsy)
- **Predecessor autopsies (same day):** failure_autopsy_V3-EXQ-603f / -624b / -651 (all 2026-06-07)

## Cluster thesis

Three structurally-different probes all return **non_contributory**, and all trace to a
single upstream structural property: the **goal-pipeline GAP-2 /
`scaffolded_sd054_onboarding` foraging-and-survival-competence gate is not yet ready**.
Its own readiness probe (603g) re-failed this cycle -- the P1 **survival / hazard-avoidance
learning leg** does not train even when isolated as a dedicated Stage-H (G_H 0/3). This is
**not** three independent bugs; it is one not-ready substrate expressed across three
downstream tests.

The failure shape is the substrate-ceiling fingerprint in every case: the *positive
control / precondition* is what fails, while the actual scientific discrimination either
passes (624c C2 dissociation; 603g goal-formation G0) or cannot be read (651a recovery on a
goal that never formed strongly).

### Convergent-pattern table

| Experiment | Claim(s) | Positive control / precondition | Discrimination criterion | Read |
|---|---|---|---|---|
| 603g | (substrate readiness, no claim) | G0 stage-0 goal-formation **3/3 PASS** | G1 survival **0/3**, G2 contact **1/3**, G_H isolated-hazard **0/3** | goal FORMATION works; survival/hazard LEARNING leg does not train -> substrate not ready |
| 651a | ARC-060 | C1 bank-engaged 3/3, ND off-arm-abandons 2/3 | C3 recovery **0/3** (grid -> weakens) | weaken confounded: z_goal weakly formed (0.302/0.355/0.486, 2 below 0.4 gate) -> nothing to recover |
| 624c | MECH-320, ARC-068 | positive control (w_passive headroom, C1+C5) valid only **2/5** (majority >=3 NOT met) | C2 Niv-vs-Salamone dissociation **PASS on valid seeds** | dissociation held where it could be read; positive control lacked headroom on a majority |

**Two readings named, decision forced.** (a) *substrate enrichment* -- the survival-competence
substrate is genuinely not ready and must land before any downstream verdict; (b) *test-design
ceiling* -- the downstream probes are mis-constructed. The user's adjudication selects (a) as
load-bearing for all three: every target is `pending_retest_after_substrate` behind
`scaffolded_sd054_onboarding`, and 603g's root is reframed (below) as a **deeper survival /
aversion-learning substrate gap**, not a curriculum/budget tweak.

---

## Target 1 -- V3-EXQ-603g (ROOT)

**Facts.** Substrate-readiness probe for `scaffolded_sd054_onboarding`, claim_ids=[]. Single
change vs 603f: an isolated hazard-avoidance Stage-H inserted between P0 and P1 (goal pipeline
frozen, hazards present, foraging minimal, hfa=0, midline spawn). PASS rule = G0 AND G1 AND G2
each >=2/3 seeds. Result: **G0 3/3** (forced-feed lights z_goal: 0.498/0.401/0.558 peak),
**G1 survival 0/3** (P1 median last-window 48/14.5/... ep length, gate 75), **G2 contact 1/3**,
**G_H isolated-hazard survival 0/3** (median last-window 44/15.5/11, gate 75). Self-route label
`substrate_not_engaged`, readiness_route `foraging_competence_open`.

**Claim-layer.** No claim tagged (correct -- substrate readiness gates downstream cohorts,
weights no claim). The G0 positive control proves the goal-FORMATION substrate is intact and
decoupled from the failure; the blocker is isolated to the survival/hazard-avoidance LEARNING
leg.

**Biological reference.** Hazard avoidance in mammals is amygdala (BLA/CeA) fear-conditioning +
PAG defensive output, acquired *developmentally and gradually*, with parental buffering of the
stress axis. The signature "an isolated avoidance stage cannot learn survival within budget"
matches a developmental/curriculum-immaturity reading -- the mechanism exists in brains; our
translation lacks it. **User adjudication: this is deeper than budget.** A bare
isolated-stage-plus-more-episodes approach is the wrong shape; a missing survival /
aversion-learning substrate mechanism is implicated. The closest REE substrate (SD-035 amygdala
analogue, MECH-279 PAG freeze) exists but is not wired into the foraging curriculum as an
avoidance-learning driver. **No biology lit entry exists** for hazard/aversion-avoidance
learning curricula -> the autopsy's primary output is a `/lit-pull` commission.

**Four-layer diagnosis.**

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | no claim; substrate readiness |
| Biological reference | partial | amygdala/PAG avoidance learning exists in REE (SD-035/MECH-279) but not driving the curriculum; no lit entry |
| Prerequisites | missing | survival/hazard-avoidance learning leg not learnable as isolated stage at budget |
| Implementation | partial | Stage-H wiring landed (85/85 contracts) but does not produce learning |
| Environment | adequate | midline-spawn hazard band is the intended pressure |
| Measurement | adequate | G1/G2/G_H gates non-degenerate |
| Integration | partially coupled | goal-formation isolates cleanly (G0 3/3); survival leg fails alone AND combined |
| Scale / capacity | likely insufficient | but user judgment: not merely budget -- a deeper mechanism is implicated |

**Routing: /lit-pull (primary) + implement-substrate amend (secondary).** Commission
`targeted_review_hazard_avoidance_learning` (developmental acquisition of avoidance; amygdala/PAG
scaffolding; parental buffering; shaped-aversion curricula in RL) BEFORE further curriculum work.
Amend `scaffolded_sd054_onboarding` with a failure record + a note that budget escalation alone
is judged insufficient and a deeper survival-learning substrate mechanism is implicated, pending
the lit-pull. `ready` stays false. pending_retest_after_substrate.

---

## Target 2 -- V3-EXQ-651a (ARC-060)

**Facts.** FIELD_ONLY vs FIELD_PLUS_BANK blocked-goal-recovery, 3 seeds. Redesign of 651 added
the ND non-degeneracy gate (FIELD_ONLY must abandon the displaced goal before the recovery
comparison is scored). Interpretation grid: C1 met + ND met + C3 not met -> **weakens**. Actual:
C1 3/3, ND 2/3 (majority), **C3 recovery 0/3**. The script self-emitted a weaken; the manifest
**deferred it to non_contributory** pending this autopsy, citing weak z_goal formation
(goal_norm_after_phase_a 0.302/0.355/0.486 -- two of three below the 0.4 formation gate) and
same-day 603g reconfirming the survival/contact ceiling.

**Claim-layer.** ARC-060 (architecture_hypothesis, candidate, v3_pending; depends_on SD-039,
MECH-292/293 etc.). The bank/anchor substrate (SD-039/MECH-292/293) is implemented. The test
*design* is sound. But the experiment did **not** test the claim under conditions where it could
express: blocked-goal recovery is only meaningful if a goal was strongly formed. On a barely-formed
z_goal nothing re-approaches in either arm; the single seed where the bank "helped" (43:
on_reapproach 0.644 vs off 0.375) is precisely the seed where ND was FALSE (off-arm did not
abandon) -- so it does not count. The clean seeds (42, 44; ND true) had goal_norm 0.302/0.486 and
zero re-approach in both arms.

**Biological reference.** Ghost-goal recovery = hippocampal non-local replay biasing re-approach
to a displaced goal (Pfeiffer 2013 goal-biased path search; Gillespie 2021 non-current trace
reactivation; Berridge persistent wanting). For replay to bias behaviour there must first be a
strong goal trace to reactivate. A weakly-formed z_goal = no trace = nothing to recover. The
FAIL is therefore a **confirmed prerequisite** (goal formation must be robust before recovery is
testable), not a falsification of bank-based recovery.

**Four-layer diagnosis (abbrev).** Claim alignment: unclear-but-not-weakened (test could not let
the claim express). Biological reference: clear (Pfeiffer/Gillespie; lit present in
`targeted_review_ghost_goal_search`). Prerequisites: **missing** (robust z_goal formation, gated
by scaffolded_sd054_onboarding GAP-2). Implementation: complete (bank substrate landed).
Measurement: adequate (ND gate works). Scale: n/a.

**Routing: governance (non_contributory, defer weaken).** ARC-060 NOT weakened this cycle.
pending_retest_after_substrate (scaffolded_sd054_onboarding). No new substrate entry -- links to
the existing queued entry. The C3 0/3 weaken is held until z_goal forms robustly on the clean
seeds.

---

## Target 3 -- V3-EXQ-624c (MECH-320, ARC-068)

**Facts.** 4-arm Niv-vs-Salamone dissociation on the MECH-320 w_passive implementation; 5 matched
seeds; positive control gated by strict majority (>=3 valid). Re-spec of 624b (no-op-opportunity-rich
regime via sparser foraging, num_resources 3->2). Result: action_density ARM_0=0.908 ARM_1=0.978;
C1 Niv lift mean +0.071; **C2 dissociation PASS on valid seeds** (strict <0.5); C3 gate_product
1.000; **n_valid 2/5, majority >=3 NOT met**. The script's own notes identify **P0-warmup length,
not env density**, as the dominant headroom lever (denser hazards backfire -- the agent flees,
saturating action_density).

**Claim-layer.** MECH-320 (tonic_vigor_coupling_score_bias, candidate_substrate_landed, v3_pending;
depends_on ARC-066/068, MECH-313); ARC-068 (action.opportunity_cost_no_op_penalty, candidate,
v3_pending). The scientific question -- w_passive insensitive to parametric *movement* cost (Niv
2007 opportunity-cost-on-time) but distinct from MECH-258/SD-032b effort cost (Salamone 2003) --
**held on every valid seed** (C2 PASS). The failure is purely that the positive control (a
competitive no-op candidate existing) fired on only 2/5 seeds.

**Biological reference.** Tonic vigor / average-reward-rate opportunity cost (Niv 2007). The
mechanism is fine; the test bed must present neutral near-tie states where a no-op is competitive
on a majority of seeds. environment/measurement adequacy.

**Routing: BLOCK on 603g substrate (user adjudication).** Rather than re-queue a regime tweak
(longer P0) now, 624c is treated as **pending_retest_after_substrate** behind
`scaffolded_sd054_onboarding`: the positive-control headroom (low baseline action_density with a
competitive no-op) depends on genuine foraging competence, which is exactly what the GAP-2 gate
must deliver. non_contributory. **Record the C2 dissociation holding on valid seeds as a NARROW
positive signal for ARC-068/MECH-320 -- do NOT promote** (narrow, single-regime, positive control
sub-majority). No new substrate entry.

---

## Draft evidence_quality_notes (governance applies; do not write here)

- **603g (substrate readiness):** "V3-EXQ-603g (Stage-H ON) re-failed the foraging-competence gate:
  G0 goal-formation 3/3, but G1 survival 0/3 and G_H isolated-hazard 0/3 -- the survival/hazard-
  avoidance learning leg does not train even as a dedicated isolated stage at this budget. User
  adjudication 2026-06-07: this is a DEEPER survival/aversion-learning substrate gap, not a budget
  tweak. Routed /lit-pull targeted_review_hazard_avoidance_learning BEFORE further curriculum work;
  scaffolded_sd054_onboarding ready stays false. pending_retest_after_substrate."
- **ARC-060 (651a):** "V3-EXQ-651a self-emitted a weaken (C3 recovery 0/3 with ND 2/3) but it is
  confounded by weak z_goal formation (goal_norm 0.302/0.355/0.486, two below the 0.4 gate; the one
  bank-positive seed is the ND-false seed). On a barely-formed goal nothing re-approaches in either
  arm, so the null reflects weak z_goal, not discrete-bank inadequacy. ARC-060 NOT weakened this
  cycle; non_contributory; pending_retest_after_substrate (scaffolded_sd054_onboarding GAP-2).
  Adjudicated /failure-autopsy 2026-06-07."
- **MECH-320 / ARC-068 (624c):** "V3-EXQ-624c non_contributory: positive control (competitive no-op
  candidate) valid on only 2/5 seeds (majority >=3 not met), so the run cannot certify. The C2
  Niv-vs-Salamone dissociation HELD on every valid seed (strict <0.5) -- a narrow positive signal
  for w_passive movement-cost insensitivity, NOT promotable (single-regime, sub-majority positive
  control). Per user adjudication 2026-06-07, blocked as pending_retest_after_substrate behind
  scaffolded_sd054_onboarding rather than a regime re-queue: positive-control headroom depends on
  genuine foraging competence (GAP-2)."

## Learning extracted

1. The goal-pipeline GAP-2 / `scaffolded_sd054_onboarding` substrate is the single upstream gate
   blocking ARC-060, MECH-320/ARC-068, and SD-054-readiness work; it is a **cluster bottleneck**, not
   three separate problems.
2. The survival/hazard-avoidance learning leg is the precise locus -- goal FORMATION already works
   (603g G0 3/3). Isolating the leg (Stage-H) proved the leg, not the budget, is the blocker.
3. User judgment reframes the fix as a **deeper substrate mechanism** (avoidance-learning driver),
   commissioning biology lit BEFORE more curriculum iteration -- avoiding the SD-003-style
   "philosophy-right / mechanism-wrong, iterate the caveat" trap.
4. 651a confirms a prerequisite (robust goal formation gates recovery testing) rather than weakening
   ARC-060 -- a positive-for-the-dependency result, not a falsification.
5. 624c shows the science (C2 dissociation) is trending supportive but cannot be certified until the
   foraging substrate gives the positive control majority headroom.
