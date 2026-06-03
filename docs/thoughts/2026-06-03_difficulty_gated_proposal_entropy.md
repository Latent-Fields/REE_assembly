# Difficulty-gated proposal entropy

**Status:** WORKING HYPOTHESIS — not an established mechanism. Available for future
governance, experiment design, and substrate work. Do not cite as evidence.

**Registered:** 2026-06-03
**Claims:** `MECH-343` (mechanism), `Q-056` (the discriminating empirical question)
**Experiment proposal:** `EXP-0176` (`evidence/planning/manual_proposals.v1.json`)
**Working names:** *difficulty-gated proposal entropy* / *controlled proposal entropy
under goal blockage* / *stuck-state entropy widening with constrained commitment*

---

## 1. Hypothesis

When goal progress stalls, the agent should increase **proposal entropy upstream of
action selection**, while preserving goal/harm constraints and **delaying commitment**
until one candidate clears threshold. This should produce wider *internal* exploration
without behavioural chaos.

The distinction the hypothesis exists to preserve:

| | path |
|---|---|
| **Bad version** | hard problem → random actions |
| **Good version** | hard problem → wider internal proposals → more candidate diversity → longer arbitration → selective committed action |

This is **controlled entropy, not noise**. A difficult or blocked goal state should not
trigger more random behaviour; it should trigger a controlled, time-limited widening of
the candidate-proposal distribution, with more arbitration before commitment, and a
narrowing back down once a workable candidate is found.

## 2. Biological analogy

Human problem-solving may involve increased neural variability / network flexibility
during difficult cognitive work. Functionally this can be read as broader
hippocampal/cortical candidate generation plus longer prefrontal/basal-ganglia
arbitration before commitment. The load-bearing claim is **controlled** entropy under
preserved constraints — distinct from a state-independent noise floor and from a
constant high temperature.

## 3. Computational formulation (REE terms)

**Inputs / triggers (stuck-state signal):**

- repeated failure to improve goal progress;
- high conflict between candidate actions;
- low score margin at Ethics Engine 3;
- low committed-action diversity;
- plateau / stuck-state signal;
- high uncertainty with **preserved** goal salience.

**Mechanism (the loop):**

1. increase candidate proposal entropy / within-class sampling temperature;
2. expand the candidate rollout set (hippocampal/world-model prospective rollouts, ARC-018 / CEM);
3. increase arbitration time / number of candidate comparisons;
4. **maintain** goal, harm, and constraint scoring throughout;
5. release action **only** when candidate score margin / commitment threshold is met (MECH-090 / MECH-342);
6. **reduce** entropy after successful commitment or goal progress.

The narrowing/arbitration side at the scoring step is MECH-341 (E3 must preserve
candidate-class diversity rather than collapse the pool). The commitment threshold is
MECH-090 (commit-entry predicate / score-margin admission) and MECH-342
(maintenance/commitment release). The proposal-widening side is the
not-yet-designed difficulty-gated regulator over ARC-018 rollout generation.

**Expected positive signature:**

- candidate entropy increases under difficult/stuck conditions;
- committed-action entropy increases **only where useful**;
- goal progress improves;
- harm does not increase;
- random churn does not increase;
- commitment latency may rise during hard problems but falls again after solution discovery.

## 4. Pathological signatures (psychiatry / cognitive-failure bridge)

Cross-referenced in [`docs/architecture/psychiatric_failure_modes.md`](../architecture/psychiatric_failure_modes.md).

| Signature | Failure locus |
|---|---|
| entropy increases but behaviour unchanged | **selection-authority failure** (the current `modulatory-bias-selection-authority` bottleneck) |
| entropy increases and behaviour becomes random/harmful | **arbitration failure** |
| entropy does not increase despite stuck state | **proposal-generation rigidity** |
| entropy increases but never narrows | **manic / disorganised-exploration analogue** |
| proposals widen but commitment never occurs | **catatonic / abulic action-release analogue** |

This hypothesis is one candidate route from catatonic-like inert cognition toward
controlled exploratory cognition.

## 5. Experiment direction (`EXP-0176`, deferred to `/queue-experiment`)

Hard-goal / blocked-path environment with matched easy-goal controls.

**Arms:**

1. entropy-gating OFF;
2. entropy-gating ON under stuck-state;
3. entropy ALWAYS high;
4. entropy high but goal/harm constraints ablated (diagnostic only, if safe and useful).

**Metrics:** candidate proposal entropy; committed-action entropy; score-margin
distribution; number of arbitration cycles before commitment; goal progress; harm
rate; action churn; time-to-first-workable-path; entropy reduction after successful
path discovery.

**Main prediction (tracked as `Q-056`):** the stuck-gated entropy arm (2) should
outperform **both** entropy-off (1) and entropy-always-high (3) — flexible exploration
without collapse into random behaviour. Arm 1 should show proposal rigidity / staying
stuck; arm 3 should show disorganised exploration / no narrowing.

> **614d is necessary but not sufficient.** V3-EXQ-614d / MECH-341 tests only whether
> within-class temperature can lift *committed-action* diversity — i.e. whether controlled
> variability can reach committed action rather than staying trapped upstream. It is a
> possible early substrate for this hypothesis, but it does **not** prove the whole loop
> (stuck-state gating → proposal widening → constrained arbitration → narrowing →
> commitment → decay).

## 6. Connection to current REE-v3 findings

- **V3-EXQ-614d / MECH-341** — testing whether within-class temperature affects
  committed-action diversity. Tests one piece of the loop (can controlled variability
  reach committed action), not the gating or the narrowing.
- **MECH-314 / MECH-320 failures (V3-EXQ-604a / 624a, 2026-06-03 cluster autopsy)** —
  modulatory signals exist but lack **selection authority** at E3 (bias fires but never
  changes argmax). Captured as the new `modulatory-bias-selection-authority` substrate
  gap. This is the **selection-authority bottleneck** the hypothesis depends on.
- **MECH-342 failure (V3-EXQ-629)** — the system fails to *naturally commit* when score
  margins are too flat (mean score_margin ~70× below the MECH-090 admission floor). The
  hypothesis needs a working commitment threshold for its narrowing/release step.
- **z_goal / foraging failures (V3-EXQ-603e cluster)** — goal representations need
  ecological reward-contact and developmental scaffolding before they can guide
  behaviour. The hypothesis assumes *preserved goal salience* during stuck-state; that
  precondition is itself substrate-gated.

## 7. Why this is not yet a substrate task

`MECH-343` is registered `epistemic_category: substrate_conditional` — promotion/demotion
suppressed — because it is blocked on two upstream substrates not yet built:

1. the `modulatory-bias-selection-authority` regulator (gives modulatory/diversity
   signals genuine authority at `E3.select`); and
2. a difficulty-gated proposal-entropy regulator (stuck-state detector + transient
   CEM temperature / candidate-count gain + decay), which has no design doc yet.

When (1) lands, the loop becomes partially testable; (2) is the dedicated substrate this
hypothesis would eventually motivate. The experiment script is deferred to
`/queue-experiment` per the mandatory skill path.
