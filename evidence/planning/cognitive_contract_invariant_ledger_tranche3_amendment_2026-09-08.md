# Cognitive-contract invariant ledger — tranche 3 amendment

**Date:** 2026-09-08  
**Applies to:** `evidence/planning/cognitive_contract_invariant_ledger.v1.json` (schema 1.1)  
**Status:** evidence-led amendment record; preserve until folded into the next canonical ledger rewrite  
**Evidence source:** `cognitive_contract_literature_pull_tranche3_2026-09-08.md`  
**Experiment freeze:** `cognitive_contract_narrowing_stack_preregistration_2026-09-08.md`

This file records changes that should be applied to the ledger after tranche 3. It is deliberately separate rather than silently rewriting the earlier evidence state. The prior ledger remains an audit snapshot of the first two tranches.

---

## 1. CCI-001 identity — KEEP, sharpen

**Old working ambiguity:** identity was partly described using sameness/equivalence language.

**New definition:**

> **Token continuity / identity:** whether a representation at one time/state concerns the persisting token represented at another time/state.

**New comparative support:** same/different concept learning in animals does not by itself establish token identity, but object/individual persistence literature is relevant. Do not use abstract SAME evidence as a substitute for token-continuity evidence.

**Status:** admitted, moderate confidence, architectural candidate.

**Double-dissociation prediction:** identity lesion should damage persistence, credit assignment and memory binding while potentially sparing same/different transfer.

---

## 2. CCI-006 equivalence/similarity — KEEP SEPARATE from identity

**New comparative evidence:**
- Wright & Katz 2006, *Mechanisms of same/different concept learning in primates and avians*, DOI `10.1016/j.beproc.2006.03.009`, PMID 16621333.
- comparative SAME/DIFFERENT literature in pigeons, primates and other taxa.

**New definition:**

> **Equivalence / similarity:** whether distinct tokens stand in a same/different/like relation that can transfer to novel fillers.

**Status:** admitted; confidence raised from moderate-high toward high-recurrence/moderate-primitive.

**Double-dissociation prediction:** equivalence lesion should spare token tracking while degrading analogy, category transfer, schema reuse and relational generalisation.

**Do not merge CCI-001 and CCI-006 before the double dissociation is tested.** A later relation algebra may unify them; that is an output, not an assumption.

---

## 3. CCI-007 relational topology — SHARPEN AND PROMOTE as first primary assay

`Relational structure` is too broad. Replace it operationally with:

> **Predictive relational topology / transition structure:** enough information about adjacency, reachability and action-conditioned transition structure that a receiving system can recover behaviourally relevant connectivity and structural equivalence despite changes in surface coordinates.

Permitted formal targets include:
- adjacency/reachability `A(i,j)`;
- `P(s' | s,a)` or an action-conditional sufficient transform;
- successor-like predictive occupancy representation;
- a lower-dimensional representation demonstrably sufficient for the same relations.

**New neural support:** Garvert et al. 2017 eLife `10.7554/eLife.17086` — hippocampal-entorhinal geometry tracked an implicit non-spatial transition graph.

**New AI support:** Webb et al. 2024 relational bottleneck, DOI `10.1016/j.tics.2024.04.001`; Campbell & Cohen 2024 relational abstraction (`arXiv:2402.18426`).

**Status:** admitted, high confidence as a candidate relation family. **Primitive encoding not established.**

**Experiment role:** first primary held-out relation in the narrowing-stack pre-registration.

---

## 4. CCI-003 reality_status — SPLIT; parent becomes composite convenience label

The combined label obscures at least two separable jobs.

### New candidate CCI-015 — provenance/source/ownership

**Definition:**

> Evidence about how a representation was generated or constrained: externally sampled versus internally generated, self versus other source/ownership, retrieved versus newly simulated where recoverable.

**Evidence:** source-monitoring literature; Dijkstra et al. 2022 perceptual-reality-monitoring review; Dijkstra et al. 2025 Neuron `10.1016/j.neuron.2025.05.015` shows perception and imagination share perceptual machinery and are discriminated using signal/cue evidence plus frontal reality judgement.

**Classification:** architectural candidate, moderate confidence.

### New candidate CCI-016 — branch/obtaining/update status

**Definition:**

> Whether represented content is currently treated as obtaining, a candidate, a simulation, a counterfactual, or committed for belief/action update.

**Evidence:** developmental modal/alternative-state work; E2 counterfactual and MECH-094/365 lineage inside REE; memory/future imagination overlap supports separating content-generation machinery from branch/status.

**Classification:** architectural candidate, moderate confidence.

### Parent CCI-003

Retain `reality_status` only as a convenient composite label for historical continuity. It should **not** be treated as a primitive candidate in Thought 2.

---

## 5. Coarse cognitive modes — explicitly demote from primitive candidacy

The following should be analysed as **composites over factorial coordinates**, unless contrary evidence appears:

- PERCEPTION
- MEMORY
- IMAGINATION
- PREDICTION

Leading factorial basis:

```text
CONTENT
+ source/generation evidence
+ temporal relation
+ branch/obtaining/update status
+ ownership/agent source
+ epistemic confidence
```

Memory/future-imagination overlap and perception/imagination overlap both favour this decomposition.

**Pre-registered test:** compare cross-context generalisation of the factorial probes with direct coarse-mode probes. Do not assume the factorial model wins.

---

## 6. CCI-004 agency — KEEP AS COMPOSITE TARGET, not primitive

Evidence remains strong that agency matters, but current best decomposition is:

```text
source/ownership
+ action
+ predicted consequence
+ causal/control relation
+ counterfactual comparison
```

**Action:** Thought 2 should distinguish `agency is contract-critical` from `AGENCY is a primitive contract coordinate`.

**Status:** candidate composite; high recurrence, primitive status weak.

---

## 7. CCI-011 negation/absence — RENAME and sharpen

Replace the broad target `negation_absence` with:

### CCI-011 revised — non-obtaining / expected absence

**Definition:**

> The distinction between `unknown whether X`, `expected X but X did not occur`, and `X is represented as not obtaining` remains recoverable.

**New comparative/neural evidence:** omission responses across species/modalities; Yaron et al. 2026, DOI `10.1111/ejn.70566`, PMID 42210581. Reward-prediction-error paradigms provide timed responses to omitted expected outcomes.

**Developmental/language evidence:** McDermott-Hinman et al. 2026, DOI `10.1037/xge0001938`, supports a linguistic rather than conceptual bottleneck in learning English negation words; Szabó & Kovács 2025 keeps open whether infants possess full logical negation versus narrower rejection/non-existence concepts.

**Interpretation:** strong evidence for representing **non-occurrence/absence relative to expectation**; insufficient evidence for a universal language-like logical NOT primitive.

**Status:** candidate; moderate confidence; possible operator derived from prediction + expectation + mismatch.

---

## 8. CCI-009 value/valence — OPEN A FORMAL RIVAL HYPOTHESIS

Do not promote scalar VALUE merely because REE requires harm/benefit evaluation.

### H1 — signed-value basis

A signed evaluative relation is itself one of the most compressed invariant coordinates.

### New candidate CCI-017 — viability/preference relation (H2)

**Definition:**

> The representation preserves relation to an admissible/preferred/viable region or homeostatic constraint; signed reward/value can be derived from movement toward/away from that region.

**Evidence:** Keramati & Gutkin 2014 eLife `10.7554/eLife.04811` derives primary reward from homeostatic-need fulfilment / drive reduction. Viability theory constrains trajectories to admissible sets without requiring a total scalar ranking of all viable states. Active-inference accounts likewise require preferences but do not prove a universal scalar value coordinate.

**Classification:** embodied/agentic candidate, moderate-high relevance.

**Pre-registered comparison:** measure whether signed value or viability/preference geometry transfers better under harm/resource rescaling while retaining behavioural preference.

REE's harm/benefit machinery remains operationally load-bearing whichever hypothesis wins.

---

## 9. CCI-005 confidence/precision — RETAIN; collapse translation-confidence primitive

Fleming 2024 supports confidence as a metacognitive inference about an object/state/decision.

Therefore provisional simplification:

> **Translation confidence is confidence whose object is a translation/reconstruction.**

Do not add a distinct primitive `TRANSLATION_CONFIDENCE` unless a lesion/learning result demonstrates that ordinary confidence machinery cannot serve the bridge.

However the **substrate gap remains real**: V3 may not currently compute confidence in meaning preservation at an inter-engine boundary even if no new kind of confidence is required.

**Status:** candidate control/meta-representational field; moderate confidence.

---

## 10. CCI-014 priority/relevance — DEMOTE from presumptive contract membership

Parr & Friston 2019 distinguish attentional gain/precision from salience; priority-map literature combines bottom-up salience with task relevance.

Current best interpretation:

> priority/relevance is downstream resource-allocation metadata that may be recomputable locally from value, uncertainty, goals and urgency.

**Status:** candidate/not-yet-required.

**Admission condition:** demonstrate a boundary where preserving the other admitted relations while deleting priority causes a deficit that the receiving system cannot reconstruct locally.

---

## 11. Relational bottleneck — add as external positive control, not a contract claim

Webb et al. 2024 explicitly constrain processing to relations rather than input attributes and report abstraction/generalisation benefits. Campbell & Cohen 2024 report factorised/approximately orthogonal feature dimensions under such a relational inductive bias without pre-specified symbolic primitives.

This is the closest neighbouring artificial-learning programme identified so far.

It **must not** be treated as independent confirmation that REE's contract will emerge spontaneously, because the relation-selective bottleneck is imposed.

Its proper role is experimental:

- positive-control arm D = imposed relational bottleneck;
- target arm E = unlabeled multi-consumer narrowing;
- if E approaches D without relation labels, evidence supports emergence;
- if only D works, stronger inductive bias may be necessary.

---

## 12. Revised working hierarchy after tranche 3

### Tier 1 — strongest candidate relations

1. token continuity / identity;
2. equivalence / similarity;
3. predictive relational topology / transition structure;
4. temporal order / persistence;
5. provenance / source / ownership (CCI-015);
6. branch / obtaining / update status (CCI-016);
7. causal / control relation (to be separated from composite agency in the next ledger rewrite);
8. epistemic confidence / precision.

### Tier 2 — plausible operator/agentic relations

9. non-obtaining / expected absence;
10. ordered magnitude / comparison;
11. viability / preference relation (CCI-017).

### Tier 3 — likely composites or boundary-specific derived fields

- agency;
- perception / memory / imagination / prediction;
- goal;
- commitment;
- exact number;
- kind / part;
- salience / priority.

### Explicitly not justified as primitives

- a universal scalar `VALUE`;
- a universal scalar `AGENCY`;
- explicit modal logic;
- a language-like `NOT` token;
- named human grammatical categories merely because they recur;
- named neural modules.

---

## 13. Next canonical-ledger action

When Thought 2 is authored/ingested, rewrite the canonical JSON ledger so that:

- CCI-003 becomes a historical composite parent;
- CCI-015 provenance/source and CCI-016 branch/status become first-class records;
- CCI-011 is renamed non-obtaining/expected absence;
- CCI-017 viability/preference is added as the rival to scalar-value primitiveness;
- causal/control receives its own record rather than remaining hidden inside CCI-004 agency;
- CCI-014 is marked not-yet-required/control metadata;
- the relational-bottleneck positive-control literature is attached to CCI-007 and the experimental design, not misregistered as evidence of spontaneous emergence.

Negative and demoting results in this amendment must survive that rewrite.
