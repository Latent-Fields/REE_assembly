# Convergence as a General Computational Signal — Experiment Ladder

**Date:** 2026-09-09  
**Status:** preregistration-oriented planning scaffold; no queue mutation  
**Parent thought:** `docs/thoughts/2026-09-09_convergence_as_general_computational_signal.md`  
**Formal notes:** `docs/thoughts/2026-09-09_convergence_signal_formal_notes.md`

## Purpose

Do not test this idea first inside the full REE organism.

The quantities are too easy to make tautological. A clean synthetic ladder should establish whether independence-aware convergence has any value above ordinary reliability weighting, common-currency integration or Bayesian confidence before the signal is allowed near action authority.

---

## Stage 0 — measurement range

### Question

Can proposed convergence metrics distinguish known support topologies?

### Construct

Create synthetic evaluator outputs with controlled:

- accuracy;
- confidence calibration;
- pairwise error correlation;
- source ancestry clusters;
- task relevance;
- number of supporters;
- magnitude of dissent.

### Required states

At minimum:

1. one strong source, weak followers;
2. several independent moderate sources agreeing;
3. several correlated clones agreeing;
4. two equal opposing coalitions;
5. reliable minority versus weak majority;
6. broad weak agreement;
7. random/no-information evaluators.

### PASS condition

A candidate metric must separate these regimes in the intended ordering without using the ground-truth label directly.

A metric that calls correlated clones “strong independent convergence” fails here.

---

## Stage 1 — standard combiner benchmark

### Baselines

Compare:

- argmax of strongest evaluator;
- unweighted sum;
- majority vote;
- confidence-weighted sum;
- reliability-weighted arbitration;
- an oracle / Bayesian combiner where assumptions permit;
- independence-aware convergence augmentation.

### Primary question

Does adding convergence improve anything after reliability is already known?

### Primary readouts

- held-out decision accuracy;
- calibration;
- expected loss;
- robustness under distribution shift;
- robustness under evaluator dropout.

### Interpretation

If convergence adds nothing beyond reliability-aware aggregation, the strong architectural version should weaken immediately.

---

## Stage 2 — correlated consensus trap

### Construct

Five evaluators appear to support action A.

Four share one hidden upstream representation error. One independent evaluator supports B.

Manipulate the common upstream error so that the four clones become confidently wrong.

### Registered comparison

```text
raw vote / raw sum
vs
reliability-only
vs
ancestry/covariance-aware convergence
```

### Critical criterion

The convergence-aware system should not increase confidence merely because duplicated evidence is numerically abundant.

This is the most important anti-groupthink discriminator.

---

## Stage 3 — minority expert / asymmetric consequence

### Construct

A large weak coalition favours A. A highly reliable specialist favours B only in one narrow context.

Then create a protected-harm variant in which B is a reliable veto against a catastrophic tail.

### Questions

1. Can relevance/reliability outweigh raw consensus?
2. Can a protected veto remain non-commensurable with ordinary positive votes?
3. Does convergence remain useful as a meta-signal without becoming a majority rule?

### Failure signature

If a large coalition can numerically buy off a reliable protected veto, the architecture is unsafe.

---

## Stage 4 — value of computation / information hunger

### Construct

Offer several unresolved questions with matched current uncertainty.

Question types:

- Q1 updates one isolated model;
- Q2 updates several highly correlated models;
- Q3 updates several genuinely independent models;
- Q4 is very uncertain but irreducible/noisy;
- Q5 has lower uncertainty but potentially changes the current action.

### Baselines

- uncertainty seeking;
- novelty;
- expected information gain;
- learning progress;
- decision-relevant expected value of information;
- cross-model leverage / convergence-aware allocation.

### Critical test

Does the convergence-aware agent allocate limited queries/compute toward Q3 when doing so improves several independent models, **without** being distracted by Q4's irreducible uncertainty?

### REE connection

This is the first clean test of the idea that several information-hunger drives can “pull” toward the same unknown and thereby justify more research effort.

---

## Stage 5 — closure / stopping

### Construct

An agent can continue deliberating at a cost.

Create matched aggregate confidence states with different support topology:

- A: one strong model supplies almost all support;
- B: several independent models moderately converge;
- C: several correlated models converge;
- D: active unresolved specialist dissent.

### Question

Does convergence topology improve the decision of **when to stop thinking** over confidence and expected information gain alone?

### Readout

Total trajectory value including deliberation cost, missed opportunity and decision error.

### Link

Direct child of the August “persistence must earn continuation” thought.

---

## Stage 6 — synthetic insight task

### Construct

Build tasks with several superficially distinct prediction problems generated by one hidden shared structure.

The agent initially learns separate local rules. Later it is offered or discovers a representation that captures the common relation.

Control tasks:

- compression that loses predictive information;
- one-view improvement only;
- gradual improvement across views;
- sudden but incorrect re-description;
- superficial confidence/reward burst without representational change.

### Candidate computational insight criteria

A successful abstraction should yield some combination of:

- held-out prediction gain or preservation;
- reduced rule/model complexity;
- transfer to a novel domain generated by the shared structure;
- several effectively independent views becoming explainable by the same relation;
- robustness under removal of one original view.

### Critical distinction

The experiment should identify **computational restructuring** before attaching an Aha-like internal signal to it.

---

## Stage 7 — diversity pressure

### Construct

Train an ensemble of evaluators under three regimes:

1. no diversity pressure;
2. explicit agreement reward;
3. preserved diversity plus convergence detection.

### Question

Does rewarding agreement directly collapse the evaluators into correlated clones?

### Readouts

- pairwise residual correlation;
- unique failure coverage;
- distribution-shift robustness;
- effective independent source count;
- task competence;
- convergence discriminability.

### Expected useful result

The best system should not be the one with maximum disagreement or maximum agreement. It should preserve different routes while detecting when those routes lawfully converge.

---

## Stage 8 — REE shadow diagnostic

Only after Stages 0–7 establish a non-tautological signal.

### Candidate existing channels

Observe, do not yet modify:

- harm / benefit / goal / residue / resource-related action pressures;
- E1/E2 trajectory evaluations;
- hippocampal prior/retrieval support;
- selector eligibility / Go-No-Go variables;
- uncertainty / curiosity signals;
- protected vetoes.

### Shadow outputs

At each decision point log:

```text
aggregate pull
convergence topology
source dependency estimate
structured dissent
veto state
future action
future outcome
```

### First question

Does measured convergence predict anything independently useful about:

- action stability;
- competence;
- harmful error;
- value of additional rollout;
- later reversal;
- sensitivity to channel ablation?

No causal use yet.

---

## Stage 9 — compute allocation only

If the shadow signal earns predictive value, first causal role should be **resource allocation**, not action authority.

Potential intervention:

```text
high independent convergence on an unresolved relationship
→ allocate one additional diagnostic rollout / probe / query
```

or:

```text
high action convergence + low dissent + no veto
→ reduce additional deliberation budget
```

Compare against ordinary uncertainty/value-of-computation policies.

This is safer and more diagnostic than letting the signal directly select actions.

---

## Stage 10 — action-selection contribution

Only if previous stages justify it.

A convergence term may modulate:

- commitment threshold;
- eligibility persistence;
- tie-breaking;
- deliberation termination;
- confidence in a candidate.

It should **not** override protected vetoes.

### Acceptance burden

A causal action-selection contribution must show:

1. held-out behavioural gain;
2. no rise in catastrophic/protected-boundary errors;
3. gain beyond reliability-weighted common-currency baselines;
4. robustness to correlated-source traps;
5. no collapse of evaluator diversity;
6. effect disappears when source identities/dependency structure are permuted in the way the hypothesis predicts.

---

## Global red-team controls

Every stage should consider:

- same upstream error copied across sources;
- one evaluator directly reading another;
- confidence miscalibration;
- scale differences;
- class imbalance;
- zero-information channels;
- perfectly correlated clones;
- a dominant source hidden inside a coalition;
- task leakage through the convergence estimator;
- metric definitions that mathematically force convergence;
- intervention that changes evaluators while claiming only to measure them.

---

## Stop conditions for the programme

The strong convergence-signal programme should be paused or reframed if:

- reliability-aware aggregation consistently matches it;
- dependence correction cannot be estimated without using forbidden oracle information;
- cross-model leverage fails to improve information allocation;
- insight measures reduce to confidence/reward/fluency;
- diversity collapses whenever convergence is made useful;
- the only successful implementation is a high-capacity meta-controller that simply relearns the task.

A negative result here would still be valuable: it would tell REE that plural constitutional arbitration is sufficient without a new convergence construct.
