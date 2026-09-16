# Organism-Level Validation Doctrine

**Date:** 2026-09-16  
**Status:** methodological planning scaffold; no claim, build, governance, or experiment-queue mutation  
**Parent thought:** `docs/thoughts/2026-09-16_local_mechanism_success_vs_organism_level_intelligence.md`  
**Purpose:** prevent local mechanistic evidence from being over-interpreted as organism-level intelligence, while preserving a route from local science to eventual integrated validation.

---

## 1. Governing principle

> **Evidence should receive no broader jurisdiction than the experiment earned.**

A local mechanism result can establish a local mechanism result.

It does not automatically establish:

- native use by the intended consumer;
- closed-loop behavioural benefit;
- transfer to a different ecology;
- developmental adequacy;
- compatibility with the rest of REE;
- adaptive recovery when the world changes;
- general intelligence.

This doctrine is an **umpire**, not a new ruler. It does not require every experiment to test the whole organism. It requires progress summaries and architectural decisions to state clearly which validation domains have and have not been crossed.

---

## 2. Validation domains

These are **orthogonal evidence domains**, not a scalar ladder.

### D0 — Instrument validity

Question:

> Did the experiment actually measure or manipulate what it says it measured or manipulated?

Examples:

- positive control can move the dependent variable;
- negative/self-yoked control is stable;
- measurement is non-destructive when required;
- readout denominator and sample size are real;
- no tautological criterion;
- no hidden oracle leakage.

A D0 PASS says nothing by itself about the mechanism.

### D1 — Local mechanism validity

Question:

> Does the proposed local mechanism or representation have the claimed property?

Examples:

- information preservation;
- cue differentiation;
- replay fidelity;
- provenance discrimination;
- communication-subspace structure;
- selection authority.

### D2 — Local causal consequence

Question:

> Does manipulating the mechanism change the intended downstream computation?

Examples:

- receiver output changes;
- E3 top preference changes;
- a communication bridge changes native consumer prediction;
- provenance-aware weighting changes effective evidence cardinality.

Decodability alone does not clear D2.

### D3 — Closed-loop behavioural consequence

Question:

> Does the mechanism improve the organism's behaviour in a live closed loop rather than merely a frozen endpoint or external readout?

Readouts may include:

- resources acquired;
- hazards avoided;
- regret;
- trajectory value;
- recovery speed;
- protected-boundary violations;
- task completion.

### D4 — Ecological generalisation

Question:

> Does the effect survive when the world family changes rather than merely when the random seed changes?

Environment changes should be predeclared and preferably orthogonal.

### D5 — Developmental validity

Question:

> Does the mechanism work when acquired through a plausible developmental route, and does developmental history matter when final architecture is held constant?

### D6 — Integrated compatibility and simplification

Question:

> Does the mechanism remain useful in the assembled organism, and can redundant machinery be removed without losing the function?

A useful mechanism should not be protected from deletion merely because it once passed an isolated assay.

### D7 — Adaptive recovery

Question:

> When a previously useful internal model becomes wrong, can the organism discover the mismatch, seek useful information, update and recover without being told which subsystem failed?

This is the strongest organism-level domain in the present doctrine.

---

## 3. Mandatory interpretation rule

Every major result synthesis should include an explicit line of the form:

```text
Evidence domain reached: D?
Domains not tested: ...
```

This need not appear in every raw experiment manifest. It should appear when a result is promoted into:

- a roadmap claim;
- an architectural recommendation;
- a milestone statement;
- a progress summary;
- a decision to make a mechanism default-on;
- an assertion that REE itself has become more competent.

Example:

```text
A frozen-latent decoder result may establish D1.
It does not establish D2-D7.
```

Another:

```text
A live E3 selection perturbation may establish D2.
It still does not establish ecological transfer or organismal recovery.
```

The purpose is to make the inference boundary visible, not to punish local science.

---

## 4. Seeds versus worlds

### Rule

> **Random-seed replication and ecological replication must be reported separately.**

Suggested reporting:

```text
stochastic replication: N seeds
world-family replication: N environment families / N orthogonal perturbation classes
```

### Frozen ecological suite — future requirement

A later REE organism-level suite should include controlled variation in at least several of:

- map geometry;
- hazard prevalence and topology;
- resource prevalence and topology;
- cue-to-consequence mapping;
- transition dynamics;
- temporal delays;
- observation/sensor layout;
- action costs;
- affordance structure;
- partial observability;
- social/non-social actor structure when available.

The suite should be frozen before it is used as a promotion target, otherwise it can become another training distribution.

---

## 5. Developmental-history check

When a mechanism plausibly depends on co-adaptation, interface learning or developmental scaffolding, use matched-final-state designs.

Minimum useful arms:

```text
A  small/final architecture from birth
B  overcomplete or scaffolded development -> final architecture
C  overcomplete throughout
D  final architecture discovered by B, reinitialised from birth
E  correct mechanism introduced only after maturity
```

Interpretation:

- `B > A` may reflect optimisation, architecture discovery or developmental history;
- `B > D` is stronger evidence that the developmental path itself mattered;
- `B > E` suggests late insertion cannot substitute for co-development;
- `C > B` may mean the proposed mature bottleneck is simply too restrictive.

Do not infer developmental necessity from a mature-agent repair alone.

---

## 6. Dynamic-interface check

A fixed bridge/subspace result should trigger a dynamic follow-up when the proposed mechanism claims general inter-system legibility.

Candidate factors:

- receiver identity;
- receiver state;
- task context;
- reference frame;
- phase / temporal window;
- sleep versus wake;
- developmental stage;
- action candidate;
- uncertainty/control state.

A useful report should distinguish:

```text
fixed information content
fixed bridge availability
receiver-conditioned accessibility
time-gated accessibility
native causal use
```

The dynamic check is not mandatory for every local representation study. It becomes mandatory before a fixed communication structure is interpreted as a general interface solution.

---

## 7. Integration and deletion pressure

### Rule

> **Construction earns a later obligation to attempt simplification.**

Once several local repairs are simultaneously present, create deletion/simplification assays.

Candidate arms:

- full current bundle;
- remove one mechanism;
- remove a set of apparently redundant mechanisms;
- replace a high-capacity bridge with a lower-capacity one;
- repair upstream and remove downstream compensation;
- reinitialise a supposedly unnecessary component;
- distil two overlapping routes into one.

Primary questions:

1. Which mechanisms remain causally necessary after integration?
2. Which have become redundant?
3. Which compensations are masking an upstream defect?
4. Does simplification improve transfer or stability?
5. Does removal expose a hidden dependency that local assays missed?

A successful deletion should be recorded as a positive architectural result, not as lost work.

---

## 8. `H-other` / model-misspecification requirement

Important discriminating experiment families should preserve an explicit model-misspecification route.

Suggested routing:

```text
registered H1 ... Hn explain outcome adequately
    -> adjudicate among them

none explains full outcome / incompatible interactions appear
    -> H-other / model misspecification
    -> rotate the claim or expand the hypothesis partition before another rescue run
```

`H-other` should not be used as a lazy catch-all after an ordinary null.

It becomes relevant when the **pattern itself** is outside the registered explanatory family.

Signals include:

- contradictory per-seed mechanism signatures;
- strong context interaction omitted from the model;
- non-monotonic effects that all hypotheses assumed monotonic;
- multiple registered hypotheses simultaneously required;
- timing/development explaining variance none of the static hypotheses can;
- repeated rescue clauses without hypothesis-space closure.

---

## 9. Scientific-machinery audit

Before interpreting a sudden change in experimental throughput or verdict pattern as creature progress, check whether the change came from:

```text
creature code
experiment driver
measurement/instrument
queue/governance predicate
evidence-index interpretation
```

If a governance or instrumentation change alters what can run or how a result is classified, record that separately from organismal progress.

Suggested language:

```text
science-enabling infrastructure change
```

rather than:

```text
creature improvement
```

unless the creature itself changed and was validated.

---

## 10. Adaptive Recovery Battery — future assay family

**Status:** design seed only; do not queue from this document.

### Core question

> Can REE recover when a previously useful internal model becomes materially wrong, without an oracle naming the broken subsystem or supplying the replacement policy?

### Candidate perturbation classes

#### AR-1 — Cue remapping

A familiar cue changes its consequence while the physical affordance remains available.

Tests belief revision rather than simple obstacle handling.

#### AR-2 — Resource contingency reversal

A formerly useful resource becomes low-value or costly and another becomes preferable.

Tests value/update interaction and behavioural recovery.

#### AR-3 — Hidden transition change

Action-to-outcome dynamics change without an explicit mode flag.

Tests predictive-model mismatch detection and relearning.

#### AR-4 — Memory/provenance corruption

A plausible but misleading stored event or source genealogy is introduced under controlled conditions.

Tests whether the system treats internal evidence as revisable rather than recursively self-confirming.

#### AR-5 — Interface drift

One subsystem undergoes a controlled representational transformation while local information content is preserved.

Tests mutual legibility, replay/interface maintenance and bridge adaptation.

#### AR-6 — Sensor/affordance change

A previously reliable sensory or motor relation becomes unavailable or remapped.

Tests whether REE can discover a new route rather than repeating the old one.

### Required constraints

The experimenter must not provide:

- the identity of the failed module;
- a one-hot “world changed” flag;
- the correct new policy;
- a privileged oracle target unavailable to the organism;
- unlimited brute-force retraining that bypasses the intended architecture.

### Candidate readouts

Measure separately:

- mismatch-detection latency;
- uncertainty/calibration change;
- information-seeking or diagnostic-compute allocation;
- number and type of counterfactuals/rollouts recruited;
- representational or model update;
- behavioural regret during recovery;
- time/experience to regain competence;
- preservation of still-valid knowledge;
- transfer to a second related perturbation;
- recurrence after sleep/replay;
- whether the recovery required a hard-coded fallback.

### Controls

At minimum compare against:

- no-adaptation baseline;
- ordinary retraining baseline;
- oracle-labelled failure baseline as an upper engineering control;
- random exploration;
- matched environmental noise with no true regime change;
- explicit cue indicating the change, to establish task reachability.

### Strong falsifiers

An apparent recovery does **not** count as organism-level adaptive recovery if:

- a fixed fallback policy solves the perturbation;
- the experimenter directly identifies the failed subsystem;
- adaptation is simply full-policy retraining from reward with no use of the proposed REE machinery;
- behaviour improves while internal beliefs remain demonstrably wrong in the same way;
- the agent catastrophically forgets the previous valid regime and cannot distinguish contexts;
- the recovered behaviour does not transfer even minimally to a related perturbation;
- the challenge was solvable by a local reflex that never required mismatch detection.

---

## 11. Proposed minimal-working-intelligence gate

Do **not** make this a claim or milestone automatically. It is a candidate acceptance doctrine for later ratification.

A minimal working intelligence event would require:

1. **Baseline competence:** the organism has a stable useful policy/model before perturbation.
2. **Real mismatch:** the perturbation makes that policy/model materially wrong.
3. **No failure label:** the organism is not told which module or belief is wrong.
4. **Discrepancy response:** behaviour or internal allocation changes because the mismatch is detected.
5. **Information-directed adaptation:** the organism preferentially samples, computes or retrieves information relevant to resolving the mismatch.
6. **Internal update:** at least one relevant model/representation/interface changes in the direction predicted by the recovery hypothesis.
7. **Behavioural recovery:** useful closed-loop competence returns above a preregistered threshold.
8. **Knowledge retention:** still-valid prior knowledge is not simply erased.
9. **Transfer:** some recovery advantage appears on a second unseen perturbation from the same structural family.
10. **Ablation attribution:** removing the proposed adaptive machinery reduces or abolishes the recovery advantage.

Passing one tiny-world challenge would not establish general intelligence.

It would establish something narrower and valuable:

> **REE demonstrated an integrated, non-oracular adaptive episode in which its own working model became wrong and the organism recovered through its internal cognitive machinery.**

That would be a qualitatively different milestone from accumulating local PASSes.

---

## 12. Progress-report template

For major REE progress summaries, use a compact adjudication like:

```text
LOCAL MECHANISM:
What changed and what was actually established?

CAUSAL CONSEQUENCE:
Did it change the intended downstream computation?

CLOSED LOOP:
Did organism behaviour improve?

GENERALISATION:
Seeds only, or changed ecology too?

DEVELOPMENT:
Was developmental history tested or merely assumed?

INTEGRATION / DELETION:
Does the mechanism coexist with the rest of REE, and has simplification been attempted?

ADAPTIVE RECOVERY:
Any evidence the organism can detect and recover from being wrong?

MODEL ESCAPE:
What live H-other / misspecification possibility remains?
```

This template is intentionally qualitative. Do not collapse it into a single score unless a specific bounded benchmark requires one.

---

## 13. Immediate application to the current programme

This doctrine does not demand a new organism-wide experiment immediately.

Current interface, authority, representation, replay and provenance experiments should continue because they are resolving necessary local uncertainty.

Immediate changes are interpretive:

1. progress reports distinguish local mechanism movement from creature-level competence;
2. important discriminators preserve `H-other` when appropriate;
3. environment-family generalisation becomes a named debt rather than being implied by seeds;
4. developmental-history dependence is tested when an interface is proposed as mature architecture;
5. accumulated mechanism bundles eventually receive deletion/simplification challenges;
6. the Adaptive Recovery Battery remains a future assay family until enough substrate exists to make it non-vacuous.

---

## 14. Stop conditions / anti-Goodhart rules

Pause or redesign organism-level validation if:

- the ecological suite becomes part of routine training and is no longer held out;
- recovery tasks become predictable scripts with bespoke fallback policies;
- one composite intelligence score starts hiding failures on protected axes;
- organism-level PASS depends on an external decoder more capable than the native consumer;
- adding more mechanisms always improves the benchmark only because the benchmark rewards their presence;
- a developmental assay changes final capacity as well as developmental history and cannot separate them;
- a deletion challenge is never attempted because every mechanism has become institutionally protected;
- `H-other` is routinely converted into “try the same hypothesis with more compute.”

---

## Compact rule

> **Local evidence should stay local until closed-loop consequence is shown. Closed-loop consequence should stay ecological-specific until transfer is shown. Transfer should stay developmental-specific until developmental history is tested. And none of these should be called organism-level intelligence until REE can encounter a world in which its own model is wrong, discover that fact, and recover without being handed the answer.**
