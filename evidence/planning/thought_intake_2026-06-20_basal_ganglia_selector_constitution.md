# Thought intake: basal-ganglia-like selector constitution for E3 committed-action conversion

**Date:** 2026-06-20  
**Status:** thought intake / post-689a design-pressure note; not an implementation request  
**Proposed location:** `evidence/planning/thought_intake_2026-06-20_basal_ganglia_selector_constitution.md`  
**Primary trigger:** MECH-439 / F-dominance committed-action conversion ceiling cluster; concern that E3 committed selection may require a broader basal-ganglia-like action-selection constitution rather than further upstream gain increases.  
**Related work:** `failure_autopsy_f-dominance-conversion-cluster_2026-06-20`, `biology_grounding_convergence_v4_plan.md` BG-2, `behavioral_diversity_isolation:GAP-I`, V3-EXQ-689a, V3-EXQ-571, V3-EXQ-654g, V3-EXQ-485h, V3-EXQ-625e, V3-EXQ-445h, ARC-106.

---

## 1. Purpose of this note

This note records a design pressure, not a build decision.

The current governance position is correct: V3-EXQ-689a should complete before any new selector design is implemented. 689a is the pre-registered discriminator between the optimistic reading that a conflict-graded near-tie lever is sufficient and the pessimistic reading that the current selector has a deeper residual ceiling.

However, the convergent F-dominance cluster raises a broader architectural concern that should not be lost while waiting for 689a:

> The E3 committed selector may require a more basal-ganglia-like action-selection constitution, rather than additional upstream signal strength or isolated modulatory patches.

This note preserves that concern so it can be evaluated after 689a lands.

---

## 2. Existing governance already captures part of the issue

The F-dominance cluster autopsy already records that the closest biological reference is the basal-ganglia action-selection bottleneck, especially the hyperdirect / subthalamic nucleus conflict-graded hold mechanism.

The current implemented lever under test in 689a is a minimal translation of that reference:

```text
conflict-graded shortlist / k = f(F-gap)
commit-temperature modulation / T = f(F-gap)
```

This is appropriate as a first discriminative test. It asks whether a near-tie, gap-sensitive widening/hotting mechanism can create committed-action-class diversity strict-above gap-blind controls.

This note does not supersede that plan. It asks what follows if that minimal lever is insufficient or only non-specifically helpful.

---

## 3. Architectural concern

The repeated cluster pattern is:

```text
upstream signal forms
signal is measurable
signal reaches E3 / authority / accumulator
committed action does not change reliably
```

Across mechanistically distinct channels, this suggests that the failure is not primarily at the level of signal generation.

The concern is that the current selector may still behave too much like:

```text
candidate actions
→ scalar score dominance
→ committed argmax
```

when the required architecture may be closer to:

```text
candidate actions
→ eligibility set
→ Go / No-Go pressures
→ conflict-sensitive hold
→ threshold modulation
→ recurrent competition
→ context-sensitive arbitration
→ commitment permission
→ post-commit latch / release
```

The problem may therefore be constitutional rather than parametric.

That is, the core issue may not be that upstream advisors are too weak, but that the rules by which candidate actions become eligible to win are under-specified.

---

## 4. Basal-ganglia-like translation target

The target is not anatomical mimicry. It is a functional translation of basal-ganglia-like action selection.

Candidate functional components:

| Biological reference function | REE translation candidate |
|---|---|
| Direct pathway / Go | Action-channel promotion when evidence, value, drive, rule, or safety conditions make an action eligible. |
| Indirect pathway / No-Go | Suppression of unsafe, stale, perseverative, irrelevant, or low-viability action channels. |
| Hyperdirect / subthalamic nucleus hold | Conflict-sensitive global hold, threshold increase, candidate-set widening, or commitment delay when top candidates are close or when cross-channel conflict is high. |
| Striatal channel competition | Parallel candidate-action channels compete, rather than all pressure collapsing into one scalar monarch. |
| Pallidal output gate | Final disinhibition / permission-to-commit mechanism rather than simple argmax. |
| Dopaminergic modulation | Learning / salience / expected-future-update signal, not a simple reward-maximisation scalar. |
| Thalamocortical recurrence | Recurrent refinement of candidate availability before commitment. |
| Contextual loops | Different action domains may require different arbitration regimes while sharing a common commitment interface. |

Potential REE mechanism classes:

```text
eligibility mask
bounded Go pressure
bounded No-Go pressure
conflict hold / threshold raise
candidate-set widening
rank-preserving F demotion
divisive normalisation
contextual arbitration mode
post-commit stability / de-commit latch
```

---

## 5. Relation to 689a outcomes

This note should be interpreted only after 689a produces a manifest and adjudication.

### 5.1 689a gap-concentrated PASS

If A1B1 lifts committed-action-class entropy strict-above both collapsed controls and gap-blind controls, and the lift is gap-concentrated:

```text
Interpretation:
  Minimal hyperdirect-like conflict grading may be sufficient for the V3 tract.

Action:
  Do not immediately redesign the selector.
  Refine / validate the existing lever.
  Retest downstream channels currently gated behind MECH-439.
```

The basal-ganglia constitution note remains useful as a later grounding roadmap, but not as an immediate V3 rewrite.

### 5.2 689a uniform lift / gap-blind controls match

If A1B1 improves committed diversity but gap-blind controls match it:

```text
Interpretation:
  The selector can be moved, but the load-bearing factor is not conflict grading.
  Wider or hotter selection may be helping non-specifically.

Action:
  Do not treat conflict grading as validated.
  Escalate to selector-constitution analysis.
  Consider rank-preserving F->eligibility demotion, divisive normalisation, or broader eligibility-set governance.
```

This is the strongest case for turning this note into a formal design proposal.

### 5.3 689a readiness OK but no lift

If readiness is met but neither A1B1 nor relevant controls lift committed diversity:

```text
Interpretation:
  Near-tie shortlist / commit-temperature modulation is insufficient.
  The bottleneck may lie in deeper action gating, commitment permission, or post-commit latch dynamics.

Action:
  Evaluate whether the next target is:
    A. constitutional selector redesign, or
    B. commitment / de-commit latch grounding (BG-3 in biology_grounding_convergence_v4_plan).
```

This outcome would make a detailed basal-ganglia-like selector design note high priority, but still not necessarily prove the whole selector must be rewritten before checking the commit-latch branch.

### 5.4 689a readiness failure

If readiness fails:

```text
Interpretation:
  The current test did not adequately engage the intended mechanism.

Action:
  Do not infer that basal-ganglia-like selector reform is required from this result alone.
  Repair readiness / measurement / substrate engagement and rerun or redesign the falsifier.
```

---

## 6. Design principle

The design principle should be stated explicitly:

```text
Do not simply increase upstream gain.
Do not merely make modulatory channels louder.
Instead, specify the constitutional rules by which candidate actions become eligible, inhibited, held, widened, and committed.
```

The key distinction is:

```text
signal strength
vs
lawful access to action selection
```

Many recent failures suggest that signal strength can exist without lawful access to committed action.

---

## 7. Proposed post-689a work products

Depending on the 689a result, possible work products are:

1. **Targeted literature review**  
   Basal ganglia / subthalamic nucleus / hyperdirect pathway / conflict-modulated decision thresholds / Go-NoGo action selection.

2. **Selector constitution design note**  
   A formal architecture proposal specifying eligibility, Go/No-Go, hold, threshold, widening, arbitration, and commitment stages.

3. **Minimal selector amendment**  
   If 689a passes gap-concentrated: refine the current conflict-graded shortlist and avoid premature broad redesign.

4. **Rank-preserving F-to-eligibility demotion experiment**  
   If 689a gives uniform lift or fails despite readiness: test whether F can remain informative without monopolising final rank.

5. **Commit-latch branch review**  
   If signals reach candidate availability but still fail post-selection commitment, evaluate BG-3 / commitment-maintenance-release grounding.

---

## 8. Proposed acceptance criteria for a future selector-constitution experiment

A future selector-constitution experiment should not count as success merely because action entropy increases.

It should require:

```text
1. Non-vacuity: upstream channels form and reach the selector.
2. Selector engagement: eligibility / hold / Go-NoGo variables vary as intended.
3. Specificity: the relevant channel changes action only under conditions where it should.
4. Gap sensitivity or conflict sensitivity: if claimed, effect scales with measured conflict / top-F gap.
5. Gap-blind controls: non-specific widening/hotting does not explain the lift.
6. Safety: harmful or irrelevant action classes are not globally disinhibited.
7. Retest transfer: at least one previously gated downstream channel converts after the selector change.
8. No premature global-noise solution: increased stochasticity alone does not count as architectural repair.
```

The key discriminant is not entropy alone but **lawful, channel-specific, context-appropriate conversion into committed action**.

---

## 9. Risks

### 9.1 Overbuilding risk

A broad selector redesign before 689a would violate current governance discipline and risk solving the wrong problem.

### 9.2 Cargo-cult biology risk

Basal ganglia terminology should not be imported decoratively. Each biological analogue must have a functional role, a divergence ledger, and a falsifier.

### 9.3 Noise-as-diversity risk

Making action selection more stochastic can mimic success. Any redesign must distinguish adaptive action access from random action entropy.

### 9.4 Upstream invalidation risk

Some channels may still have local upstream failures. A constitutional selector repair should not be used to avoid local signal-quality work where readiness is not met.

### 9.5 Commitment instability risk

Increasing eligibility and conflict-hold machinery may create indecision, oscillation, or fragile commitments if not coupled to stable post-commitment latch dynamics.

---

## 10. Minimal recommendation

Do not implement a new selector constitution now.

Do preserve this design pressure and sequence it behind 689a.

Recommended governance posture:

```text
Before 689a:
  hold as thought intake only.

After 689a PASS gap-concentrated:
  refine minimal hyperdirect-like lever; do not broaden prematurely.

After 689a uniform-lift or readiness-met-no-lift:
  promote this note to a formal selector-constitution design proposal.

After 689a readiness failure:
  repair the falsifier before drawing architectural conclusions.
```

---

## 11. Candidate future title if promoted

If promoted from thought intake to formal design work:

```text
E3 selector constitution: basal-ganglia-like eligibility, conflict-hold, and commitment-gate architecture
```

Potential claim family:

```text
MECH-439a: F-share bound at committed argmax
MECH-439b: conflict-graded hold / shortlist sufficiency
MECH-439c: residual ceiling requiring F-to-eligibility demotion
MECH-439d: Go/No-Go eligibility constitution for committed-action conversion
```

Claim synthesis should determine whether these are genuinely independent children or merely design alternatives.

---

## 12. One-sentence summary

The current E3 selector may require a basal-ganglia-like constitutional action-gating architecture, but this should remain a dormant design-pressure note until V3-EXQ-689a determines whether the already-built conflict-graded lever is sufficient, nonspecifically helpful, or inadequate.
