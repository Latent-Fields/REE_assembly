# Behavioural Diversity Isolation Plan (REE-v3)

**Created:** 2026-05-25T11:46:33Z
**Author session:** diversity-isolation-plan-20260525T114633Z
**Status:** draft (plan-of-record)
**Sibling to:** [`behavioral_diversity_acceptance_criteria.md`](behavioral_diversity_acceptance_criteria.md)
**Related claims:** ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a/b/c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076

---

## Purpose

The acceptance-criteria doc (sibling) defines **what counts as success** for behavioural
diversity in REE-v3. This document defines **how we isolate which of the candidate failure
mechanisms is load-bearing** when diversity fails. The two are complementary:

| Doc | Question answered |
|-----|-------------------|
| `behavioral_diversity_acceptance_criteria.md` | When can we say diversity is real and useful? |
| `behavioral_diversity_isolation_plan.md` (this) | When diversity is absent, which substrate layer is responsible? |

The isolation plan is needed because **diversity failure is multi-causal**: ARC-065 already
commits the architecture to a distributed pathway (LC-NE tonic + frontopolar curiosity +
striatal novelty + hippocampal trajectory sampling), and multiple layers can independently
suppress the observed action-class entropy. Without an isolation matrix, a Rung-1 FAIL is
under-determined: we don't know which substrate to fix next.

---

## Layer model: where diversity can collapse

Diversity must survive all four layers between candidate generation and observable action.
Failure at any one layer reproduces the monostrategy phenotype downstream.

```
                  ARC-065 distributed diversity-generation pathway
                                    |
                                    v
   [ Layer A: PROPOSAL ]  hippocampal trajectory sampling, CEM candidate pool
                                    |
                                    v
   [ Layer B: SCORING ]    E3 score aggregation across trajectory classes
                                    |
                                    v
   [ Layer C: ACTION-SELECT ]  softmax / argmax over E3-ranked candidates
                                    |
                                    v
   [ Layer D: REPRESENTATION ] V_s anchor sets / regional verisimilitude
                                    | (feeds back into Layer A on next tick)
                                    v
                              observable action stream
```

**Layer D feedback note.** Layer D is not strictly downstream of A-C in a single tick --
state representation in tick t+1 depends on what was committed in tick t. Stale V_s
representations therefore amplify monostrategy across episodes even when Layers A-C are
behaving correctly within any one tick. This is why MECH-269 reads as "monostrategy"
upstream of the action-selection stack despite acting on representations.

---

## The 4 theories (top of the candidate field)

Drawn from the 8-mechanism survey 2026-05-25 (see prior conversation / governance log).
Theories 5-8 (proposal-distribution bias, MECH-260 anti-recency, curiosity weight, z_goal
config-default confound) are retained as secondary candidates but not the focus of this
plan.

| # | Theory | Layer | Primary claim | Falsifier EXQ | Status |
|---|--------|-------|---------------|---------------|--------|
| 1 | CEM elite-pool collapse to one action class | A | ARC-065 (SP-CEM child) | V3-EXQ-567 / V3-EXQ-569 | landed 2026-05-17 (main-path); matched-entropy control pending |
| 2 | **E3 scoring collapses diverse candidates to one** | **B** | **MECH-341 (new)** | **TBD (this plan, design below)** | **unclaimed gap until 2026-05-25** |
| 3 | Missing tonic noise floor (LC-NE analog) | C | MECH-313 | V3-EXQ-543b ARM_MECH313_only | substrate landed, matched-entropy gate pending |
| 4 | V_s regional verisimilitude staleness | D | MECH-269 / 269b | V3-EXQ-550 (live falsifier) | falsifier in flight |

**Headline gap.** Theory #2 (E3 scoring) is the highest residual leverage because the other
three either have landed substrate (#1, #3) or have an active falsifier (#4). MECH-341
registered in this pass closes the claim-side of the gap; the experiment design (Section 5)
closes the test-side.

---

## Isolation matrix

Each row is an experiment arm; each column is a substrate ON/OFF. A run produces the row
of outcomes; comparison across rows pins the contribution of each substrate. The matrix is
designed so that *any single substrate ablation against the all-ON baseline gives a
single-substrate contribution estimate*; the all-OFF arm is the Rung-0 substrate-naive
baseline that anchors ARC-065's architectural commitment.

| Arm | SP-CEM (A) | E3 score-diversity (B) | Noise floor MECH-313 (C) | V_s active MECH-269 (D) | Use |
|-----|:----------:|:---------------------:|:------------------------:|:----------------------:|-----|
| BASE_OFF | off | off | off | off | Rung 0 baseline / ARC-065 architectural-necessity check |
| ALL_ON | **on** | **on** | **on** | **on** | Rung 1 target (matched-entropy controlled) |
| A_only | on | off | off | off | Theory 1 contribution (SP-CEM proposal lift in isolation) |
| B_only | off | **on** | off | off | Theory 2 contribution (E3 scoring lift in isolation) |
| C_only | off | off | **on** | off | Theory 3 contribution (noise floor in isolation) |
| D_only | off | off | off | **on** | Theory 4 contribution (V_s in isolation) |
| ablate_A | off | on | on | on | Marginal cost of removing SP-CEM |
| ablate_B | on | off | on | on | Marginal cost of removing E3 diversity preservation |
| ablate_C | on | on | off | on | Marginal cost of removing noise floor |
| ablate_D | on | on | on | off | Marginal cost of removing V_s |
| MATCHED_NOISE | off | off | T=2.5 uniform | off | FP-2 control: structured-vs-noise comparison for acceptance doc Rung 1 |

**Pragmatic note.** The full 11-arm matrix is not required in a single run. Sequencing
(Section 6) reduces this to a phased programme of 3-arm and 4-arm experiments that each
answer one question.

**Layer-B substrate gap.** "E3 score-diversity ON" requires MECH-341 substrate to exist;
until it lands, B columns are vacuously OFF and theories 1/3/4 are the only testable axes.
MECH-341 substrate work is a prerequisite for the full matrix.

---

## Decision rules

Each rule has the form `if (observation) -> (decision)`. Rules are applied in order; the
first matching rule wins.

### Theory 1 (CEM elite-pool collapse)

- **R1.a** If V3-EXQ-569 matched-entropy control shows SP-CEM entropy = noise-matched entropy on
  all diversity metrics (entropy, coverage, trajectory_class_count): theory 1 is **not
  load-bearing on its own**. ARC-065 SP-CEM child substrate marked `non_contributory` for
  diversity (separate from its non-collapse role). Promote attention to theories 2-4.
- **R1.b** If V3-EXQ-569 shows SP-CEM strictly > matched noise on trajectory_class_count
  (FP-2 cleared): theory 1 confirmed as a real contributor; advance to Rung 2 testing.

### Theory 2 (E3 scoring collapse) -- this plan's primary new test

- **R2.a** If pre-MECH-341 trajectory_class_count >= 2 in CEM candidates but post-E3-scoring
  selected class count = 1 for >= 80% of timesteps (measured on SP-CEM-ON, MECH-269-ON
  baseline): theory 2 is confirmed as a real diversity-collapse site. MECH-341 substrate
  becomes priority.
- **R2.b** If post-E3 selected class count tracks pre-E3 candidate class count within +/- 1
  on average: theory 2 is **not load-bearing**. E3 is preserving the diversity it receives;
  the collapse must be at A or C or D. MECH-341 retains as architectural commitment but no
  substrate work is triggered.
- **R2.c** If theory 2 confirmed AND MECH-341 substrate lands AND `B_only` arm produces
  trajectory_class_count >= 2 with first_action_entropy > 0.3: MECH-341 provisional
  promotion candidate.

### Theory 3 (noise floor)

- **R3.a** If MECH-313 ON alone (`C_only` arm) produces matched-entropy-distinguishable lift
  on trajectory_class_count but not on coverage: theory 3 contributes to per-tick entropy
  but not to strategic diversity. Retain MECH-313 as Layer-C substrate but escalate
  attention to theories 2/4.
- **R3.b** If ablate_C arm (drop MECH-313 from ALL_ON) drops trajectory_class_count below 2
  while Rung 1 metrics for ALL_ON pass: MECH-313 is necessary-and-sufficient at Layer C;
  promote on Rung 2 PASS.
- **R3.c** If ablate_C arm leaves Rung 1 metrics unchanged from ALL_ON: MECH-313 is
  redundant under combined substrate -- candidate for de-prioritisation pending broader
  ablation matrix.

### Theory 4 (V_s representation staleness)

- **R4.a** If V3-EXQ-550 ARM_ON >> ARM_OFF on relevant diversity metrics: confounded by
  z_goal config default; V_s pathology not confirmed; theory 4 demoted. Re-run with z_goal
  matched across arms before re-evaluating.
- **R4.b** If V3-EXQ-550 ARM_ON ≈ ARM_OFF: V_s substrate pathology confirmed; theory 4
  promoted; MECH-269 follow-up substrate work prioritised.
- **R4.c** If V3-EXQ-550 ARM_ON crashes: separate substrate bug surfaces; classify as
  failure_autopsy candidate; theory 4 status unchanged until autopsy resolves.

### Cross-theory escalation rules

- **R_X.a** If ALL_ON arm produces Rung 1 PASS but `A_only`, `B_only`, `C_only`, `D_only`
  all individually FAIL Rung 1: diversity is **emergent across substrates** (INV-074
  plasticity-crystallization invariant fires); no single Layer is load-bearing. Promote
  ARC-065 on multi-arm evidence.
- **R_X.b** If two single-substrate arms (e.g., `A_only` and `C_only`) each PASS Rung 1
  independently: substrates are **partially redundant**; revisit Q-045 (MECH-313 vs
  MECH-260 independence) and propose new Q-claim on A-vs-C redundancy.
- **R_X.c** If ALL_ON FAILS Rung 1: the four-substrate stack as currently specified is
  insufficient; **expand candidate set** to theories 5-8 (proposal-distribution bias,
  MECH-260 anti-recency, MECH-314 curiosity weight, z_goal config-default) before further
  Layer-A/B/C/D refinement.

---

## Experiment sequencing

Layer-B (MECH-341) substrate does not yet exist, so the full isolation matrix cannot run
in one pass. Phased approach:

### Phase P1 -- Pre-existing-substrate isolation (executable now)

**Arms:** BASE_OFF, A_only, C_only, D_only, ALL_ON (excluding Layer-B). MATCHED_NOISE
arm for FP-2 control. **6 arms.**

**Target:** Pin which of theories 1, 3, 4 is load-bearing under the current main-path
substrate. Apply R1, R3, R4 decision rules.

**Falsifiers reused:** V3-EXQ-567 (A_only effect already measured), V3-EXQ-569 (matched
noise, queued), V3-EXQ-550 (D_only effect, in flight).

**Required new EXQ:** A 6-arm P1 isolation run combining all three substrates on a single
SD-054 episode set, so the cross-substrate comparison is on matched data. Recommend
queueing as **V3-EXQ-TBD (P1 layer isolation, 6 arms)** -- queue via `/queue-experiment`
skill, not directly.

### Phase P2 -- E3 scoring diagnostic (executable now; no substrate needed)

**Arms:** ALL_ON_now (A+C+D, no MECH-341), instrumented to log:
- per-tick: pre-E3 CEM candidate trajectory_class_count
- per-tick: post-E3 selected trajectory_class_count
- per-tick: E3 score distribution across distinct classes (mean, std, top-2 gap)

**Target:** Apply R2.a / R2.b. **No substrate change**, just instrumentation. If R2.a
fires: MECH-341 substrate work is justified and prioritised. If R2.b fires: MECH-341 stays
architectural-only.

**Required new EXQ:** **V3-EXQ-TBD (P2 E3 score-collapse diagnostic, instrumentation only)**.
Same SD-054 episode set as P1; can be a single-arm probe.

### Phase P3 -- MECH-341 substrate build + B-axis test

**Trigger:** P2 confirms R2.a.

**Substrate work:** Implement MECH-341 (one of: entropy bonus over candidate classes at
E3 aggregation; class-stratified argmax with proportional sampling within class; jittered
tie-breaking when top-K E3 scores are within epsilon). Specific design open -- see
"Substrate design options" below.

**Arms (post-build):** B_only, ablate_B, ALL_ON (now including B). **3 arms.**

**Target:** Apply R2.c. Promote MECH-341 if `B_only` produces Rung 1-comparable diversity
in isolation OR if ablate_B drops Rung 1 metrics significantly.

### Phase P4 -- Full matrix (post-MECH-341 landing)

Run the 11-arm matrix on a downstream env (CausalGridWorld or a new substrate) for
replication and to apply R_X rules. **Blocked on Rung 2 SD-054 clearance + MECH-341 landed.**

---

## Substrate design options for MECH-341 (when P3 triggers)

The claim asserts that E3 must preserve trajectory-class diversity across its scoring step.
There are at least three plausible implementations:

1. **Entropy bonus over candidate classes.** E3 score = harm_score + lambda * H(class | candidates).
   Penalises homogenisation of the candidate pool at scoring time. Risk: lambda is another
   tuning knob; matched-noise control needed.
2. **Class-stratified argmax with within-class proportional sampling.** Stratify candidates
   by first-action class; pick best within each class; sample across classes proportional
   to their best-in-class scores. Preserves all surviving classes; biases toward best
   representative of each.
3. **Jittered tie-breaking near top.** Standard argmax, but when top-K scores are within
   epsilon, sample uniformly across them. Cheapest implementation; only affects diversity
   when E3 scores are nearly tied (which is precisely when diversity is being lost).

These three options are not mutually exclusive (could combine 1+3). Pre-implementation
governance: which to try first should be decided after P2 results, since P2's per-tick E3
score distribution data will tell us whether the collapse is happening at near-ties
(option 3 sufficient) or at large score gaps (option 1 or 2 required).

---

## Status table (resume primitive)

| Theory | Layer | Claim | Substrate status | Falsifier | Result | Decision |
|--------|-------|-------|------------------|-----------|--------|----------|
| 1 CEM collapse | A | ARC-065 (SP-CEM child) | landed 2026-05-17 main-path | V3-EXQ-567 / V3-EXQ-569 | 567 PASS (entropy 0.012->0.497); 569 queued | matched-entropy gate pending |
| 2 E3 scoring | B | **MECH-341** (registered 2026-05-25) | not implemented | P2 diagnostic TBD | -- | queue P2 next |
| 3 noise floor | C | MECH-313 | landed | V3-EXQ-543b ARM_MECH313 (pending Q-045 retest) | autopsy 603b: substrate operative but design-blocked | retest via 603c (training-phase fix) |
| 4 V_s stale | D | MECH-269 / 269b | substrate-ready (IGW-021) | V3-EXQ-550 | running | apply R4.a / R4.b / R4.c on landing |

**Update cadence:** every time a P-phase experiment lands, update this table in-place with
the result and the decision-rule outcome. This is the resume primitive across sessions.

---

## New claims registered with this plan (2026-05-25)

| Claim | Title (abbreviated) | Type | Status |
|-------|---------------------|------|--------|
| MECH-341 | e3_scoring_preserves_trajectory_class_diversity | mechanistic_implementation | candidate, v3_pending |
| Q-054 | minimum trajectory-class diversity floor for ARC-062 (was proposed as Q-046) | open_question | open |
| Q-055 | sleep consolidation: diversity-preserving vs eroding (was proposed as Q-047) | open_question | open |
| INV-076 | behavioural diversity as structural prerequisite for ethical counterfactual evaluation (was proposed as INV-074 -- ID taken 2026-05-17 by plasticity-crystallization invariant) | invariant (universal) | candidate |

Q-054, Q-055, INV-076 supersede the 2026-05-15 "proposed new claims" in the
acceptance-criteria doc (Q-046, Q-047, INV-074); their original IDs were never registered
and INV-074 was subsequently taken by a different, broader claim about plasticity
crystallization. The new IDs preserve the original scientific intent under the next
available IDs in their respective ranges.

---

## What this plan does NOT do

- **Does not redefine acceptance criteria.** The Rung 0-4 framework in the sibling
  acceptance-criteria doc is authoritative. This plan layers an isolation analysis on top of
  it.
- **Does not commit to a MECH-341 implementation.** P2 diagnostic results determine which
  of the three design options (Section "Substrate design options") to build.
- **Does not address theories 5-8.** Those remain candidate mechanisms and re-enter the
  candidate set only if R_X.c fires (full 4-substrate stack insufficient).
- **Does not queue experiments directly.** All EXQ entries flagged here go through
  `/queue-experiment` for code-review + smoke-test discipline.

---

*This document is the plan-of-record for behavioural diversity ISOLATION (which substrate*
*layer is responsible when diversity fails). For acceptance criteria, see the sibling*
*`behavioral_diversity_acceptance_criteria.md`.*
