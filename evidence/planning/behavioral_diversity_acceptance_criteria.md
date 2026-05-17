# Behavioural Diversity Acceptance Criteria (REE-v3)

**Created:** 2026-05-15T23:01:02Z  
**Author session:** behavioral-diversity-acceptance-criteria-2026-05-15T230102Z  
**Status:** draft  
**Related claims:** ARC-065, ARC-062, ARC-064, MECH-260, MECH-313, MECH-314, MECH-320, SD-017, SD-003, ARC-033  
**Proposed new claims:** Q-046, Q-047, INV-074  

---

## Purpose

This document defines formal acceptance criteria for behavioural diversity in REE-v3 experiments.
The criteria prevent five categories of false positive that have recurred across the EXQ-443 -- EXQ-567
series:

| False-positive class | Canonical signature | Corrective test |
|----------------------|---------------------|-----------------|
| **FP-1** Random action noise | H(action) > 0 only when temperature is forced up | Re-measure at T=1.0 with noise floor OFF |
| **FP-2** Environment drift alone | Action distribution shifts but follows env change, not policy state | Compare matched-entropy random walk as control |
| **FP-3** Hard-coded policy branches | Apparent switching is a fixed conditional, not a learned cut | Ablate diversity substrates; switch should disappear |
| **FP-4** Metric-only diversity | H(action) high but all trajectories have identical harm / goal profiles | Measure trajectory-class x harm distribution jointly |
| **FP-5** Training-phase artefact | Diversity present during exploration; collapses after convergence | Re-measure after 200+ post-convergence training episodes |

---

## Conceptual taxonomy

### 1. Action entropy

**Definition.** Shannon entropy of the action distribution at a fixed probe state:
`H(a|s_probe) = -sum_a P(a|s_probe) log P(a|s_probe)`

**What it measures.** The marginal stochasticity of action selection.

**What it misses.** A policy with H(a|s)=ln(5) (maximum over 5 actions) is a uniform random
walk. High entropy does not imply that actions are meaningfully differentiated or that the
agent uses different strategies in different contexts.

**Existing claims.** MECH-313 (stochastic noise floor / LC-NE tonic analog) -- targets a
minimum entropy floor. MECH-260 (dACC anti-recency) -- suppresses recent action classes,
raises effective entropy.

**False positives addressed.** FP-1 (temperature forcing), FP-2 (env drift). Neither of
these raises STRUCTURED entropy; they raise undifferentiated noise.

---

### 2. Trajectory diversity

**Definition.** The count of distinct trajectory classes observed across N rollouts from a
given start state, where trajectory class is defined by first-action identity AND the
action-class sequence across k=3 steps (to distinguish trajectories that share a first step
but diverge immediately after).

`TrajDiv(s, N) = |{class(tau) : tau ~ policy(s)}| / N`

**What it measures.** Whether the hippocampal proposal stream generates multiple genuinely
distinct execution templates, not just noise around one dominant class.

**What it misses.** Two distinct classes can still both be harmless random walks. Trajectory
diversity does not imply that the strategies are task-relevant.

**Existing claims.** ARC-065 (behavioural diversity generation pathway) -- the architectural
slot that supplies trajectory diversity. MECH-314 (structured curiosity) -- state-dependent
bonus that should drive exploration of distinct trajectory classes. Support-preserving CEM
work (V3-EXQ-563a/b/c) addressed the substrate-level collapse that prevented trajectory
diversity from appearing.

**False positives addressed.** FP-1, FP-3. A hard-coded branch generates at most N_branch
distinct classes regardless of state; structured diversity should produce a larger set
with coverage growing with training.

---

### 3. Context-sensitive strategy switching

**Definition.** The agent's executed action distribution at state s_A is statistically
distinguishable from its distribution at s_B, where s_A and s_B were chosen to require
different strategies (e.g., reef/foraging vs hazard-avoidance probe states in SD-054).

`Switching(s_A, s_B) = TV(P(a|s_A), P(a|s_B)) > threshold_TV`

**What it measures.** Whether the agent uses context to select among strategies, not merely
noise. This is the operationalisation of MECH-269 V_s applied at the policy level.

**What it misses.** The switch could be driven by the environment changing (FP-2) rather than
the agent's learned context representation. The control condition must hold the environment
fixed and vary only the agent's internal context representation.

**Existing claims.** ARC-062 (rule apprehension gated-policy) -- the downstream consumer
that requires context-sensitive switching. MECH-269 (V_s verisimilitude anchor) -- provides
the representational discriminability that strategy switching requires. Q-045 (MECH-313 vs
MECH-260 independence) -- both upstream of switching.

**False positives addressed.** FP-2 (env drift), FP-3 (hard-coded branches). TV distance
zero across probe states is the pre-Rung-2 failure signature currently blocking ARC-062
(see calibration_debt_index.md).

---

### 4. Learned repertoire diversity

**Definition.** Diversity that (a) increases with training, (b) is retained after training
convergence WITHOUT forced exploration, and (c) survives sleep consolidation cycles without
collapsing toward a single dominant mode.

**What it measures.** Whether diversity is a learned property of the agent, not a transient
feature of the exploration phase. A monostrategy agent can show apparently high diversity
during early training; the question is what the trained policy looks like after convergence.

**What it misses.** The diversity could be learned but still be ethically irrelevant (FP-4).

**Existing claims.** MECH-120 (sleep replay diversity maintenance -- Hebbian winner-take-all
produces monostrategy convergence; sleep replay is the mechanism that resists it).
INV-049 (sleep necessity for model-building agents). SD-017 (sleep phase substrate).
ARC-064 (bottom-up rule discovery -- cross-episode regularity extraction presupposes diverse
behaviour to cluster). ARC-071 (policy composition via repeated grounding -- the mechanism
that converts repeated primitives into atomic chunks, enlarging the effective repertoire).

**False positives addressed.** FP-5 (training-phase artefact). Diversity must survive both
training convergence and sleep consolidation (the latter is the stricter test, since
Hebbian dynamics during replay can preferentially strengthen dominant trajectories).

---

### 5. Ethically meaningful behavioural diversity

**Definition.** Diversity such that distinct trajectory classes have DISTINCT harm and goal
profiles: for at least two trajectory classes tau_1, tau_2:
`|harm(tau_1) - harm(tau_2)| > threshold_harm`   OR
`|goal_reach_rate(tau_1) - goal_reach_rate(tau_2)| > threshold_goal`

AND the diversity generation substrates are upstream-of-and-causally-connected-to the harm /
residue / ethical evaluation layer (SD-003, ARC-033).

**What it measures.** Whether diversity reaches the ethical evaluation layer with enough
spread to make a difference to outcomes. An agent can have high H(action) and high TrajDiv
while every trajectory class produces the same harm profile (e.g., all trajectories avoid
all hazards, or all contact them equally).

**What it misses.** Nothing if correctly measured -- this is the criterion that FP-4 fails.

**Existing claims.** ARC-065 (diversity generation as precondition for rule apprehension) --
rule layer requires diverse behavioural stream to find a discriminative cut. SD-003 (causal
attribution via counterfactual E2 -- requires that the agent has genuinely different
candidate trajectories, not all-identical). ARC-033 (E2_harm_s forward model for SD-003
counterfactual). MECH-269 ethical evaluation (harm trajectory evaluation).

**False positives addressed.** FP-4 (metric-only diversity). A matched-entropy random walk
can produce equal H(action) to a structured diversity agent; the discriminating test is
whether distinct trajectory classes produce distinct harm/goal outcomes.

---

## Rung 0 -- Finite action entropy

### Criterion

`H(a|s_probe) > ln(2)` (more than 1 effective action class) at >=3 probe states, measured
under the TRAINED policy with `use_noise_floor=False` and `dacc_suppression_weight=0.0`
(substrate OFF). The floor must come from the policy distribution itself.

### What counts as PASS

- H > ln(2) at ALL probe states in the clean-substrate OFF condition.
- H is not reduced to argmax (deterministic) by removing all stochasticity substrates.
- The policy retains at least minimal stochasticity after convergence.

### What does NOT count as PASS

- H > ln(2) only when `use_noise_floor=True` or temperature is force-lifted.
- H > ln(2) only during exploration / early training, collapses to argmax by episode 200.
- H computed on random-walk policy used as a baseline; must be the TRAINED policy.

### False positives prevented

FP-1 (temperature forcing), FP-5 (training phase).

### Existing claims

MECH-313 supplies the noise floor substrate; Rung 0 requires that H > ln(2) WITHOUT it.
If Rung 0 fails without MECH-313, that is a substrate-dependency PASS for MECH-313 (it
contributes) but a FAIL for the policy itself.

### Experiments

| Exp ID | Design | Target metric | Status |
|--------|--------|---------------|--------|
| V3-EXQ-544 | MECH-313 substrate-readiness (noise-floor ON vs OFF) | H lift > 0 | PASS 2026-05-10 (substrate, not policy) |
| V3-EXQ-543b arm-class NOISE-OFF | Trained policy, all diversity substrates OFF, 5 seeds | H(a\|s_probe) at convergence | Not yet run |
| V3-EXQ-567 ARM_0 | Normal CEM baseline, no scaffold, no forced bias | selected_action_entropy at test states | PASS 2026-05-15: ARM_0 CEM=0.012 (near-zero) |

**Inference from V3-EXQ-567:** ARM_0 CEM entropy = 0.012 is effectively 0 -- the trained
policy WITHOUT diversity substrates fails Rung 0. This means ARC-065 substrate MUST be
active for Rung 0 to hold. That is a positive finding for ARC-065 necessity (falsifiable
architectural prediction confirmed).

### Governance note

Rung 0 FAIL (policy collapses to argmax without substrate) is NOT a governance FAIL for the
agent architecture -- it confirms the ARC-065 architectural commitment. Document as:
`evidence_direction: supports`, claim `ARC-065`.

Rung 0 PASS (policy retains H without substrate) would be interesting but unexpected given
the current reward structure, which provides no intrinsic diversity pressure.

---

## Rung 1 -- Nonzero trajectory-class diversity

### Criterion

At a fixed start state s_0, across N=50 rollouts of k=5 steps:
- `first_action_entropy > 0.5` nats (more than ~1.6 effective action classes in the CANDIDATE pool)
- `candidate_unique_first_action_classes >= 3` out of 5 possible
- `trajectory_class_count(k=3 step tuples) >= 2` distinct trajectory classes executed

All three must hold simultaneously. Rung 1 requires the hippocampal PROPOSAL stream to
produce diverse candidates; it is NOT enough for the noise floor to randomise final selection
from a single-class proposal.

### What counts as PASS

- CEM proposal pool contains >=3 distinct first-action classes (candidate support, not just softmax noise).
- Post-CEM action selection selects from >=2 distinct classes across the N rollouts.
- Rung 0 holds simultaneously (policy is already above entropy floor).

### What does NOT count as PASS

- High H(a) from noise floor operating on a SINGLE-class candidate pool (the EXQ-563 CEM
  collapse failure: entropy=0 in candidates, noise randomises final pick but all candidates
  agree on the same first action).
- `trajectory_class_count >= 2` only when `use_action_class_scaffold_candidates=True`
  (forced scaffold); must hold on the naturalistic CEM path.
- Diversity in candidates that collapses to one class after E3 scoring (score collapse).

### False positives prevented

FP-1 (temperature forcing), FP-2 (env drift -- control with matched-entropy arm),
FP-3 (hard-coded branches -- ablate ARC-065 and check whether classes disappear).

### Existing claims

ARC-065 (parent), MECH-314 (structured curiosity produces differentiated proposals),
support-preserving CEM (V3-EXQ-563a/b/c work). Q-043 (weight calibration).

### Matched-entropy control

**Critical.** Rung 1 PASS requires comparing against a MATCHED-ENTROPY random-walk arm
(e.g., temperature=2.5 uniform policy with identical action entropy to ARM_1 SP-CEM).
If the matched-entropy control produces EQUIVALENT trajectory_class_count, the diversity
is indistinguishable from noise (FP-2). The structured diversity claim requires that
ARC-065 substrates produce MORE USEFUL trajectory diversity than entropy-matched noise.

V3-EXQ-569 (queued 2026-05-15) is the matched-entropy sweep for this purpose.

### Experiments

| Exp ID | Design | Target metric | Status |
|--------|--------|---------------|--------|
| V3-EXQ-563 | Forced actuator test | candidate_first_action_entropy=0.0 all arms | FAIL (CEM collapse) |
| V3-EXQ-563a | Scaffold actuator retest | scaffold: min_unique_classes=5 | PASS (with scaffold) |
| V3-EXQ-563b | Support-preserving CEM | candidate diversity lift | PASS (P2: support increases) |
| V3-EXQ-563c | Stratified CEM + ao_std_floor | 7-arm wiring diagnostic | Queued 2026-05-15 |
| V3-EXQ-567 | Natural entropy SP-CEM | selected_action_entropy: ARM_0=0.012, ARM_1=0.497 | PASS 2026-05-15 (entropy lift) |
| V3-EXQ-569 | 6-arm matched-entropy sweep | SP-CEM vs entropy-matched noise-floor T=2.5 | Queued 2026-05-15 |

**Rung 1 current status:** V3-EXQ-567 confirmed ARM_1 SP-CEM entropy = 0.497 vs ARM_0
CEM = 0.012. V3-EXQ-569 will determine whether this lift exceeds matched entropy (the FP-2
false positive test). If V3-EXQ-569 PASS: Rung 1 cleared for ARC-065.

### Governance note

Rung 1 PASS on V3-EXQ-569 (SP-CEM structured diversity beats matched entropy on any
diversity OR coverage metric) counts as FIRST supporting evidence for ARC-065
(candidate -> provisional trajectory, requires independent replication on different env).

Rung 1 FAIL (matched-entropy control matches SP-CEM) means ARC-065 child mechanism
implementations have not yet produced usable diversity -- the architectural commitment
remains but needs substrate redesign. Classify as `non_contributory` not `does_not_support`.

---

## Rung 2 -- State-contingent strategy switching

### Criterion

At two PROBE-STATE PAIRS (s_reef, s_forage) and (s_safe, s_hazard) on the SD-054 reef
substrate:
- `TV(P(a|s_reef), P(a|s_forage)) > 0.3` (total variation distance > 30%)
- `TV(P(a|s_safe), P(a|s_hazard)) > 0.3`
- Ablation check: switching distance DECREASES when ARC-065 substrates (MECH-313, MECH-314,
  MECH-260) are all OFF -- confirms that switching is not hard-coded

Rung 2 requires Rung 1 as a prerequisite. Without a diverse candidate pool, TV distance
between probe states will be near zero regardless of the evaluation.

### What counts as PASS

- TV > 0.3 at both probe-state pairs, measured on the FULLY TRAINED policy.
- Ablating ARC-065 substrates reduces TV below threshold (establishes ARC-065 as necessary).
- The switching is NOT explained by a deterministic function of a single action-class
  probability (must rule out hard-coded `if s == s_reef: return action_5`).
- Switching persists across seeds (>= 3 random seeds).

### What does NOT count as PASS

- TV > 0.3 driven by a single action dominating in one probe state but not the other
  (single-action displacement is not strategy switching; it is preference shift).
- TV > 0.3 in early training only; must be present at convergence.
- TV > 0.3 that does NOT decrease when ARC-065 is OFF (indicates hard-coded branch, FP-3).
- TV > 0.3 explained entirely by env difficulty difference (e.g., s_hazard has fewer safe
  actions by env rule) -- the FP-2 environment-drift false positive.

### False positives prevented

FP-2 (env drift), FP-3 (hard-coded branches).

### Existing claims

ARC-062 (gated policy heads + context discriminator -- requires Rung 2 to learn distinct
rules per context). MECH-269 (V_s discriminability -- the representational prerequisite
for TV distance being nonzero). Q-045 (independence of MECH-313 vs MECH-260 -- the
substrate combination experiment here tests both). ARC-065 ablation test directly falsifies
the ARC-065 architectural commitment.

**Current blocking status.** ARC-062 is stuck at pre-Rung-2: TV distance is exactly zero
across all seeds/windows/probe states (calibration_debt_index.md 2026-05-15). The CEM
collapse upstream is the root cause. Rung 2 is therefore BLOCKED on Rung 1 clearance.

### Required new experiment (post-Rung 1 clearance)

| Exp ID | Design | Target metric | Status |
|--------|--------|---------------|--------|
| V3-EXQ-543b (redesigned) | 4-arm: ARC-065-OFF / MECH-313-only / MECH-260-only / all-ON; SD-054 reef; ARC-062 gated-policy ON | TV distance at (s_reef, s_forage) and (s_safe, s_hazard) | Not yet run; blocked on Rung 1 |
| V3-EXQ-543c (redesigned) | Curiosity arms (314a/b/c individual ablations) on SD-054 | TV distance by sub-flavour | Not yet run |

### Governance note

Rung 2 PASS on V3-EXQ-543b is the primary evidence target for ARC-062 (rule apprehension).
A PASS here promotes ARC-062 from candidate to provisional (candidate -> provisional
requires: ARC-065 Rung 1 PASS, MECH-269 V_s substrate active, TV > 0.3 on both probe pairs).

Rung 2 FAIL (TV=0 even with ARC-065 ON) means V_s discriminability is inadequate -- the
representational layer is not separating reef/forage context enough for the policy to
switch. This would be evidence for the monostrategy / MECH-269 failure mode being upstream
of ARC-065 itself.

Rung 2 FAIL with `ablation TV = baseline TV` (ablating ARC-065 does not change TV) is an
FP-3 diagnosis -- the switching is hard-coded and ARC-065 does not contribute.

---

## Rung 3 -- Persistence after training/replay

### Criterion

For an agent that has cleared Rung 2:
- After 200 ADDITIONAL training episodes with NO forced exploration (no scaffold, no
  diversity substrate boost beyond default), Rung 1 metrics (entropy, TrajDiv) remain
  within 50% of their Rung-1-clearance values.
- After 5 SLEEP CYCLES (SD-017 SWS consolidation passes), Rung 2 metrics (TV distance)
  remain within 50% of their Rung-2-clearance values AND are not reduced to a single
  dominant strategy.
- These two checks must hold simultaneously.

### What counts as PASS

- Rung 1 and Rung 2 metrics stable across 200+ post-convergence episodes.
- Sleep consolidation does not eliminate the TV distance between probe-state pairs.
- If sleep CHANGES the diversity profile (e.g., shifts which strategies survive), that is
  ACCEPTABLE as long as TrajDiv >= 2 and TV > 0.3 still hold.

### What does NOT count as PASS

- Diversity present in episodes 0-100 (exploration) but <10% of Rung-1 values by
  episode 300 (FP-5: training phase artefact).
- Sleep consolidation collapses the policy to a single dominant strategy (Hebbian
  winner-take-all during replay eroding the diversity that ARC-065 produced).
- Diversity retained at Rung 1 / Rung 2 level only because sleep is DISABLED -- must
  also hold WITH sleep active.

### False positives prevented

FP-5 (training-phase artefact).

### Existing claims

MECH-120 (Hebbian winner-take-all produces monostrategy convergence; the RISK this Rung
tests). Sleep replay diversity maintenance -- the hypothesis that offline replay resists
monostrategy. INV-049 (sleep as mathematical necessity for model-building agents). SD-017
(sleep phase substrate). The Rung 3 test is the FIRST direct empirical test of whether
SD-017 + INV-049 together preserve rather than erode learned diversity.

**Proposed new claim Q-047** (see Section below).

### Required new experiment

| Exp ID | Design | Target metric | Status |
|--------|--------|---------------|--------|
| V3-EXQ-TBD (Rung-3-persistence) | Run agent to convergence with ARC-065 ON; measure Rung 1/2 metrics at convergence; run 200 more eps with exploration OFF; measure again; then run 5 sleep cycles; measure again | TrajDiv, TV at three time points | Not yet run; requires Rung 1 + Rung 2 clearance + SD-017 sleep substrate calibration |

SD-017 is currently at Rung 5 (read-side consumer confirmed by V3-EXQ-565 PASS
2026-05-15). Rung 6 (metric changes) is the next gate. Rung 3 experiment is therefore
BLOCKED on SD-017 Rung 6 clearance.

### Governance note

Rung 3 PASS is required before any diversity-related claim can be promoted beyond
`provisional` to `stable`: a claim's diversity evidence is only weight-bearing if the
diversity PERSISTS after training.

Rung 3 FAIL (sleep erodes diversity) would be a significant architectural finding: it would
mean SD-017 sleep, as currently implemented, is working AGAINST ARC-065. This is the
scenario MECH-120 predicts as a risk. If this occurs: classify as `does_not_support` for
sleep-maintains-diversity, but note the finding as constructive for diagnosing the
sleep-diversity interaction.

---

## Rung 4 -- Diversity usable by harm/residue/ethical evaluation

### Criterion

For an agent that has cleared Rung 3:
1. **Harm separation.** Across trajectory classes tau_1, ..., tau_k identified in Rung 1,
   at least two classes must have harm profiles that differ by > threshold_harm:
   `mean_harm(tau_i) - mean_harm(tau_j) > 0.15` for some (i, j) pair.
2. **Goal separation.** At least two classes must have goal-reach rates that differ by
   > threshold_goal: `|goal_reach(tau_i) - goal_reach(tau_j)| > 0.10`.
3. **Counterfactual availability.** In at least N_cf=10 episodes per 100, the SD-003
   counterfactual evaluation fires on a DIVERSE candidate set (at least 2 distinct classes
   among CEM candidates at the evaluation point).
4. **ARC-065 contribution.** Ablating ARC-065 substrates reduces harm separation (criterion
   1) below threshold -- confirming that ARC-065 diversity generation causally contributes
   to ethical evaluation quality.

All four must hold.

### What counts as PASS

- The trained policy's trajectory diversity includes classes that materially differ in harm
  and goal outcome.
- SD-003 counterfactual evaluation is not always operating on near-identical candidates.
- Removing the diversity generation substrates measurably degrades ethical evaluation quality.

### What does NOT count as PASS

- H(action) high but all trajectory classes contact hazards equally (FP-4: entropy without
  ethical structure).
- Harm separation achieved because one trajectory class is a trivial null-action (no-op vs
  any active action automatically differs in hazard-contact rate); must be two ACTIVE
  trajectory classes.
- Criterion 4 satisfied only trivially (ablating diversity collapses H to argmax which then
  always selects the worst strategy -- the baseline is the wrong comparison point; ablation
  should be compared against the BEST single strategy, not the random walk).

### False positives prevented

FP-4 (metric-only diversity).

### Existing claims

SD-003 (causal attribution via counterfactual E2 -- Rung 4 directly tests whether SD-003
can access diverse candidates). ARC-033 (E2_harm_s forward model -- the tool SD-003 uses).
MECH-269 (ethical evaluation via trajectory harm assessment). ARC-065 (architectural
commitment being directly tested at the ethical-evaluation level).

**Proposed new claim INV-074** (see Section below).

### Required new experiment

| Exp ID | Design | Target metric | Status |
|--------|--------|---------------|--------|
| V3-EXQ-TBD (Rung-4-ethics) | Rung 3 agent; extract trajectory classes from CEM candidates at each E3 evaluation; compute harm + goal profiles per class; measure counterfactual-evaluation firing rate on diverse-candidate episodes; ablation arm with ARC-065 OFF | harm_separation, goal_separation, cf_diverse_candidate_rate, ablation_harm_delta | Not yet run; requires Rung 3 clearance |

SD-029 (monomodal collapse measurement, currently blocked on MECH-269 V_s resolution) is
the companion governance experiment for Rung 4. Rung 4 PASS is a prerequisite for SD-029
to be interpretable.

### Governance note

Rung 4 PASS provides the primary evidence target for SD-003 (causal attribution).
Partial Rung 4 (criteria 1-2 pass but 3-4 fail) means the policy has ETHICALLY
DIFFERENTIATED behaviour but the counterfactual architecture is not accessing it -- this is
a wiring failure, not a diversity failure. Classify partial as `non_contributory` for
SD-003 but `supports` for ARC-065.

Rung 4 FAIL with all criteria near-zero means ARC-065 diversity has not reached the
ethical evaluation layer. Priority: check whether E3 scoring is sorting by harm (are
harm-differentiated trajectories being selected for?) or whether they are being
AVERAGED AWAY in the CEM elite selection.

---

## Proposed new claims

### Q-046 -- Minimum trajectory-class diversity for ARC-062 context discriminator

```yaml
id: Q-046
title: "What is the minimum trajectory-class diversity floor (Rung 1 first_action_entropy
  threshold) required for the ARC-062 context discriminator to learn a reliable discriminative
  cut between reef and foraging contexts? Is the current SP-CEM entropy lift of 0.497 nats
  sufficient, or is a higher floor required?"
claim_type: open_question
subject: policy.diversity_generation.arc062_minimum_diversity_floor
polarity: open
status: open
implementation_phase: v3
claim_level: mechanistic
registered_utc: "2026-05-15"
depends_on:
  - ARC-065
  - ARC-062
  - MECH-313
  - MECH-314
notes: >
  ARC-062 requires a diverse behavioural stream to find a discriminative cut. The
  minimum entropy threshold for this is theoretically bounded below by the mutual
  information between context (reef/forage) and action, but is practically unknown
  for the V3 SD-054 substrate.

  Resolution path: parametric entropy sweep (noise_floor_min_temperature,
  curiosity_novelty_weight) measuring ARC-062 discriminator accuracy as a function of
  upstream first_action_entropy. Expect a phase transition: below some entropy floor the
  discriminator cannot learn; above it, accuracy rises monotonically.

  Current evidence: V3-EXQ-567 ARM_1 SP-CEM = 0.497 nats. Whether this is above or
  below the ARC-062 threshold is unknown. V3-EXQ-543b (Rung 2 experiment) will answer
  this question empirically.
evidence_quality_note: >
  Proposed 2026-05-15. No experimental evidence yet.
location: evidence/planning/behavioral_diversity_acceptance_criteria.md
```

---

### Q-047 -- Sleep consolidation: diversity-preserving or diversity-eroding?

```yaml
id: Q-047
title: "Does sleep consolidation (SD-017 SWS phase) preserve the trajectory-class diversity
  achieved by ARC-065 during waking, or does Hebbian winner-take-all dynamics during replay
  erode it? Is sleep a net positive or net negative for learned behavioural diversity?"
claim_type: open_question
subject: policy.sleep_consolidation.diversity_effect
polarity: open
status: open
implementation_phase: v3
claim_level: mechanistic
registered_utc: "2026-05-15"
depends_on:
  - ARC-065
  - SD-017
  - MECH-120
  - INV-049
notes: >
  The monostrategy literature (MECH-120) predicts that Hebbian reinforcement during sleep
  replay preferentially strengthens the most-recently or most-heavily-weighted trajectories.
  If ARC-065 diversity generation operates only during waking, sleep could systematically
  undo the diversity achieved by the waking substrates.

  Two mechanisms could resist this:
    (a) ARC-065 substrates (MECH-313 noise floor, MECH-314 curiosity) could also operate
        during the waking period between sleep cycles, re-seeding diversity before the next
        consolidation pass.
    (b) Sleep replay itself could be DESIGNED to replay diverse trajectories (priority
        sampling from the full trajectory class distribution, not just the most-recent or
        most-rewarded). This is the claim MECH-120 makes but REE has not yet tested whether
        SD-017 implements it.

  Resolution path: Rung 3 experiment (see main text) -- measure TrajDiv and TV at three
  time points (post-waking-convergence, post-200-no-exploration-episodes, post-5-sleep-cycles).
  The trajectory from Rung 2 through Rung 3 will answer this directly.

  Resolution outcomes:
    - Sleep preserves diversity: supports SD-017, INV-049, MECH-120-as-risk-mitigated.
    - Sleep erodes diversity: falsifies MECH-120-as-mechanism (or indicates replay sampling
      is not diverse); ARC-065 must also operate during consolidation (new MECH proposal).
    - Sleep INCREASES diversity: surprising; would indicate replay samples across a broader
      trajectory class distribution than waking policy -- possible if offline replay
      samples from a broader episodic memory than the on-policy stream.
evidence_quality_note: >
  Proposed 2026-05-15. No experimental evidence yet.
location: evidence/planning/behavioral_diversity_acceptance_criteria.md
```

---

### INV-074 -- Behavioural diversity as a structural prerequisite for ethical counterfactual evaluation

```yaml
id: INV-074
title: "Behavioural diversity is a structural prerequisite for ethical counterfactual
  evaluation. A system with monomodal policy cannot instantiate the counterfactual evaluation
  that ethical judgment requires, because the 'could have done otherwise' comparison requires
  that the agent's candidate trajectory pool contains at least two distinct trajectory classes
  with distinct harm profiles."
claim_type: invariant
invariant_type: universal
subject: ethics.diversity_prerequisite_for_counterfactual_evaluation
polarity: asserts
status: candidate
implementation_phase: v3
claim_level: universal
registered_utc: "2026-05-15"
depends_on:
  - ARC-065     # diversity generation pathway that instantiates the prerequisite
  - SD-003      # counterfactual evaluation mechanism that requires diverse candidates
  - ARC-033     # E2_harm_s forward model (the comparator SD-003 uses)
notes: >
  The argument is mathematical, not merely empirical. If P(a|s) is monomodal (all
  probability mass on action a*), the CEM elite pool contains only trajectories beginning
  with a*. The counterfactual `E2(z_t, a_cf)` for a_cf != a* is never evaluated in the
  on-policy candidate distribution. SD-003 cannot find a counterfactual if there is none
  in the proposal pool.

  This is distinct from the claim that a monomodal agent is unsafe (which is empirical);
  the claim is that a monomodal agent is CONSTITUTIVELY INCAPABLE of the counterfactual
  comparison that SD-003 requires. Safety could be coincidental (if the monostrategy
  happens to be harmless); but genuine ethical reasoning requires that the agent CHOSE
  the harmless trajectory over alternatives, not merely executed it.

  Invariant type: universal (holds across all substrates, all environments, by construction).
  Falsification would require showing that SD-003 can produce ethical counterfactuals from
  a monomodal proposal pool -- which would require a different formulation of SD-003.

  Rung 4 acceptance criteria (Section above) operationalise this invariant:
    criterion 3 (cf_diverse_candidate_rate) directly tests whether SD-003 fires on a
    diverse pool; criterion 4 (ARC-065 ablation reduces harm separation) tests whether
    ARC-065 is what supplies the pool's diversity.

  Biology anchor: the "could have done otherwise" standard in moral philosophy (Fischer &
  Ravizza 1998 reasons-responsiveness; Kane 1996 ultimate responsibility) maps directly
  to the requirement that the agent's deliberation process generates genuine alternatives.
  A policy with deterministic monomodal output produces only one action regardless of
  reasons; it cannot be reasons-responsive.

  Cross-reference: INV-034 (goal maintenance necessary for ethical agency) -- INV-074 is
  the companion claim on the DIVERSITY side. INV-034 is about sustaining the ethical
  GOAL across time; INV-074 is about whether the CANDIDATE GENERATION process can produce
  material for ethical comparison.
evidence_quality_note: >
  Proposed 2026-05-15. Mathematical / logical argument. Lit-pull recommended before
  promotion beyond candidate:
    - Fischer & Ravizza 1998 (reasons-responsiveness, moral responsibility)
    - Kane 1996 (ultimate responsibility)
    - Bratman 1987 (planning theory of rational action -- relates trajectory planning to
      ethical commitment)
    - Dennett 1984 (elbow room -- philosophical review of counterfactual and alternative
      possibilities arguments)
  These are philosophy-of-agency anchors; the computational analog is the SD-003 claim.
  Rung 4 acceptance test is the empirical side.
location: evidence/planning/behavioral_diversity_acceptance_criteria.md
```

---

## Claim-to-rung mapping

| Rung | Claims required | Claims tested | New claims |
|------|----------------|---------------|------------|
| **Rung 0** | MECH-313 (substrate), trained policy | ARC-065 architectural necessity | -- |
| **Rung 1** | ARC-065, MECH-314, support-preserving CEM | ARC-065 (first support candidate), Q-043 | Q-046 (ARC-062 min floor) |
| **Rung 2** | ARC-062, MECH-269, Q-044, Q-045 | ARC-062 (primary evidence target), ARC-065 (ablation) | -- |
| **Rung 3** | SD-017, MECH-120, INV-049 | SD-017 (diversity preservation test), MECH-120 (risk test) | Q-047 (sleep-diversity direction) |
| **Rung 4** | SD-003, ARC-033, MECH-269 | SD-003 (primary target), INV-074 | INV-074 (counterfactual prerequisite) |

---

## Governance sequencing

The rungs are strictly ordered. A higher rung's experiment is non-contributory if a lower
rung has not been cleared.

```
Rung 0  <- Always measurable (policy entropy at any point in training)
Rung 1  <- Requires CEM candidate support fix (V3-EXQ-563c / V3-EXQ-569 PASS)
Rung 2  <- Requires Rung 1 PASS + MECH-269 V_s substrate active
Rung 3  <- Requires Rung 2 PASS + SD-017 Rung 6 clearance
Rung 4  <- Requires Rung 3 PASS + SD-003 substrate active (E2 counterfactual wired)
```

Current V3 position (2026-05-15): Rung 1 PARTIAL (V3-EXQ-567 entropy lift confirmed;
V3-EXQ-569 matched-entropy control pending). Rungs 2-4 blocked.

**2026-05-17 update -- SP-CEM landed as the main-path default.** The ARC-065
hippocampal-trajectory-sampling child substrate (support-preserving + stratified
CEM) was promoted from opt-in to the default REE-v3 action path: config defaults
flipped to the V3-EXQ-567 ARM_1 combination (`use_support_preserving_cem=True`,
`support_preserving_stratified_elites=True`, `support_preserving_ao_std_floor=0.2`)
in both the `HippocampalConfig` dataclass and `REEConfig.from_dims`. Governance
consequences: (1) every NEW experiment now measures behaviour under SP-CEM unless
it explicitly pins the legacy flags False/False/0.0 -- the monostrategy confound
that made SD-029, ARC-062 Rung 2, goal_pipeline GAP-2/4 and self_attribution
GAP-1/2/3 non_contributory is removed at the substrate level; (2) the Rung-1
gate is now strictly the matched-entropy control (V3-EXQ-569), not "is SP-CEM
enabled"; (3) this is a SUBSTRATE landing, NOT a promotion -- ARC-065 stays
candidate / v3_pending pending Rung-1 matched-entropy PASS + multi-env
replication. Pre-2026-05-17 default-config runs were under the legacy collapsing
CEM and their monostrategy signatures must not be force-mapped (non-standard
directions rule). See ree-v3/CLAUDE.md "ARC-065 SP-CEM Main-Path Landing
(2026-05-17)" and claims.yaml ARC-065 implementation_note.

### Promotion/demotion rules

**Supporting evidence** for ARC-065 requires Rung 1 PASS on matched-entropy-controlled
experiment. The V3-EXQ-567 PASS counts as first support (candidate -> provisional
trajectory) but not confirmation.

**Provisional promotion** for ARC-065 requires:
- Rung 1 PASS on V3-EXQ-569 (structured > entropy-matched noise).
- Independent replication on a second env substrate (not just SD-054 reef).

**Stable promotion** for ARC-065 requires:
- Rung 2 PASS (context-sensitive switching attributable to ARC-065).
- Rung 3 PASS (persistence after training/sleep).

**SD-003 evidence** requires Rung 4 PASS.

**ARC-062 evidence** requires Rung 2 PASS.

**Demotion criterion for ARC-065:** If V3-EXQ-569 shows structured diversity = entropy-
matched noise on ALL metrics (entropy, coverage, trajectory_class_count, harm_separation),
ARC-065's specific child mechanisms (MECH-313/314/260/320) are not adding structure above
noise. Classify as `does_not_support` on the specific claims but retain the architectural
commitment (ARC-065) as open -- the implementation may be wrong, not the commitment.

---

## What does NOT count as diversity evidence (summary table)

| Observation | Why it does not count | Rung falsified |
|-------------|----------------------|----------------|
| H(a\|s) > ln(2) with noise_floor ON, argmax without | Temperature forcing (FP-1) | Rung 0 |
| entropy lift matched by T=2.5 random walk | Not structured (FP-2) | Rung 1 |
| TV(s_reef, s_forage) > 0.3 but ablating ARC-065 doesn't change TV | Hard-coded branch (FP-3) | Rung 2 |
| diversity in episodes 1-100, argmax by ep 300 | Training artefact (FP-5) | Rung 3 |
| TrajDiv >= 2 but harm(tau_1) == harm(tau_2) | Metric-only diversity (FP-4) | Rung 4 |
| diverse candidates, but cf_diverse_candidate_rate < 10% | Diversity not reaching SD-003 | Rung 4 |
| sleep preserves entropy but TV(probe) collapses | Sleep erodes contextual structure | Rung 3 |

---

## Open questions (not yet Q-claims)

1. **Minimum Rung 4 threshold for SD-029.** SD-029 monomodal-collapse measurement requires
   the agent to generate balanced agent-vs-env event distributions (C2/C3 measurement). The
   minimum harm_separation and goal_separation required for SD-029 to be interpretable is
   not yet specified. SD-029 has been reclassified `non_contributory` pending MECH-269 V_s
   -- but the additional Rung 4 criterion should be added to its precondition list.

2. **Multi-env Rung 1 replication.** Whether SP-CEM entropy lift generalises beyond SD-054
   reef to CausalGridWorld or other substrates is untested. Rung 1 replication on a second
   substrate would strengthen ARC-065 promotion path.

3. **Optimal sleep replay sampling for diversity preservation.** If Q-047 resolves as
   sleep-erodes-diversity, the remediation is a MECH claim about priority sampling in sleep
   replay (sample proportionally across trajectory class distribution, not top-reward). This
   is a candidate child MECH for SD-017 / MECH-120 that should be pre-designed before the
   Rung 3 experiment runs, so the remediation is ready if needed.

4. **Should diversity sprint experiments test on a warmed rather than cold-start agent?**
   EXQ-573 (bias-scale sweep, 2026-05-16) showed all 10 arms bit-for-bit identical: MECH-314a
   produces zero bias because ResidueField is empty at cold start, MECH-320 produces zero bias
   because EWMA has not built up, and MECH-313 temperature-lift is irrelevant because random-
   network scores are near-uniform. The zero-differential is not a calibration failure; it is
   the correct behaviour at developmental stage 0. The question is whether the diversity sprint
   should be redesigned to pre-warm the agent (e.g., N episodes of novelty-bonus exploration to
   populate ResidueField and build EWMA) before measuring MECH-313/314/320 contributions.
   Resolution path: design a two-phase protocol (warm-up + diversity measurement) and confirm
   that bias components become non-zero in the second phase before re-running the scale sweep.
   See DEV-NEED-029 in developmental_needs_register.md for the related developmental gate question.

5. **Is there a developmental gate specifying when ARC-065 diversity mechanisms first fire?**
   ARC-065 child mechanisms (MECH-313, MECH-314a, MECH-320) are all developmental: they require
   a warm substrate (populated ResidueField, built-up EWMA, trained E3 scores) before producing
   non-zero effects. There is currently no formal gate criterion specifying the minimum waking
   experience (episodes, residue coverage, EWMA warmup time) required for these mechanisms to
   contribute. Without such a gate, diversity sprint experiments may run at the wrong
   developmental stage and return null results that are methodologically correct but
   scientifically uninformative. Candidate gate criteria: ResidueField coverage > threshold,
   EWMA v_raw > epsilon, E3 score variance > noise floor. See DEV-NEED-029 in
   developmental_needs_register.md.

6. **Does v_t_floor have a place as a developmental bootstrapping tool (infant stage)?**
   Setting `tonic_vigor_v_t_floor > 0` bypasses the EWMA warm-up requirement and gives MECH-320
   an immediate action/noop discrimination bias from episode 1. This does NOT resolve the Rung 1
   diversity metrics (action-type entropy is unchanged) but it could serve as a bootstrapping
   mechanism during the infant-to-childhood transition: providing a positive gradient toward any
   action over noop before EWMA has accumulated enough signal to drive the full vigor coupling.
   The v_t_floor would function analogously to ARC-046's reduced hazard magnitudes -- a
   curriculum parameter that attenuates the developmental warmup cost for one specific mechanism.
   Resolution path: add v_t_floor as a named infant-stage parameter in developmental_curriculum.md
   with a note that it is distinct from the adult MECH-320 mechanism; evaluate whether the
   developmental_needs_register.md MECH-320 entry should carry an infant-stage proxy note.

---

*This document is the plan-of-record for behavioural diversity governance in REE-v3.*
*Update acceptance criterion thresholds (threshold_TV, threshold_harm, threshold_goal) once*
*calibration data from V3-EXQ-569 and subsequent experiments is available.*
