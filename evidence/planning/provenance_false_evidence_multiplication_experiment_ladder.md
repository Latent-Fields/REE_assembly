# Provenance Error / False-Evidence Multiplication — Experiment Ladder

**Date:** 2026-09-09  
**Status:** planning scaffold; no claim registration, no creature code change, no queue mutation  
**Parent thought:** `docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md`

## Refinements to this ladder (added 2026-09-10; no rung, condition, readout or stop condition below is modified)

The rungs below stand as written. Six companion artifacts refine them and are **not** duplicates of them; read the relevant one before implementing any rung.

| Artifact | Refines | Contributes |
|---|---|---|
| [`provenance_psychosis_literature_pull_20260909.md`](provenance_psychosis_literature_pull_20260909.md) | whole ladder | the clinical source-monitoring baseline; its "not directly established" row on dependent-descendants-as-votes is **corrected** by the supplement below |
| [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) | P1, P2, P3, P6 | hippocampal-campaign audit; the six evidence classes; Break A (nothing joins ancestry-loss mechanisms to cardinality readouts) and Break B; controls `P1-R1`–`P1-R4`, `P3-R1`–`P3-R3` |
| [`provenance_harness_generated_ancestry_design.md`](provenance_harness_generated_ancestry_design.md) | P1 | the generated-ancestry harness: descendant generators, the genealogy representation and its degradation processes, the four conditions defined on that state, and the genealogy contract P3 consumes |
| [`provenance_p3_replay_amplification_design.md`](provenance_p3_replay_amplification_design.md) | P3 | the replay loop, the design matrix, accumulation-versus-compounding split, and the preregistered signatures |
| [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) | P1, P3 | the judgment-class sweep; normative counterweights to the engineering rule; the fluency-versus-cardinality control |
| [`provenance_branch_hippocampal_audit_verification_20260910.md`](provenance_branch_hippocampal_audit_verification_20260910.md) | P1, P3 | verification of the audit; the `MECH-544` demarcation on readout 3; the internally-generated-repetition evidence class; controls `P1-R5`, `P1-R6`, `P3-R4`–`P3-R7` |

## Purpose

Test whether a provenance error can cause one causal lineage to be counted as several independent reasons, thereby raising confidence without adding world evidence.

The programme must distinguish three hypotheses:

```text
H0 source-label-only:
provenance errors alter source attribution but not epistemic weight.

H1 false-independence:
provenance errors inflate effective evidence count and confidence.

H2 recursive amplification:
false-independence compounds across replay/prediction cycles and becomes self-maintaining.
```

No clinical conclusion follows automatically from any synthetic result.

---

## Assay P1 — content-matched provenance corruption

### Fixed content

Create one latent proposition `H` and one seed evidence event `e0`.

Generate four descendants carrying matched H-relevant content:

```text
prediction descendant
replay descendant
retrieved-memory descendant
ambiguous-perception descendant
```

All four descend causally from the same `e0/H` family.

### Conditions

1. `VERIDICAL` — shared ancestry known.
2. `SOFT` — shared ancestry probability degraded.
3. `ABSENT` — ancestry unknown.
4. `FALSE_SPLIT` — descendants incorrectly represented as independent source families.

### Primary readouts

- posterior confidence in H;
- effective source count;
- calibration against world truth;
- additional-query demand;
- deliberative closure time;
- response to one matched disconfirmatory external observation.

### Critical criterion

The test only supports H1 if `FALSE_SPLIT` raises confidence / reduces further information-seeking despite **identical informational content and external evidence**.

If only phenomenological/source labels change, H1 is not supported.

---

## Assay P2 — unknown is not independent

Compare downstream semantics for provenance-unknown evidence:

```text
A. unknown ancestry defaults to independent
B. unknown ancestry defaults to maximally dependent
C. unknown ancestry remains a probability distribution over shared ancestry
```

The desired architecture is not predeclared by intuition alone.

Score:

- calibration;
- regret;
- ability to use genuinely independent new evidence;
- resistance to duplicate-evidence inflation.

This operationalizes the Assay-005 lesson that uncertain provenance should remain uncertainty-bearing rather than be hardened prematurely.

---

## Assay P3 — replay amplification

Hold world evidence fixed after time `t0`.

Allow repeated replay/reinstatement cycles:

```text
0, 1, 2, 4, 8, 16 replay events
```

Cross with provenance condition.

### Dangerous signature

```text
confidence(H) rises monotonically with replay count
while external evidence remains fixed
```

specifically in provenance-corrupted conditions.

Healthy replay may improve representation quality or retrieval without increasing the number of independent observations.

### Falsifier

If replay count does not interact with provenance integrity, the recursive-amplification hypothesis H2 weakens.

---

## Assay P4 — counterevidence recovery

First induce a provenance-corrupted confidence state, then present strong true disconfirmatory evidence.

Measure:

- belief reversal threshold;
- number of corrective observations required;
- whether corrupted descendants continue to vote after parent hypothesis weakens;
- whether re-linking genealogy restores calibration without deleting content.

This distinguishes an error-tolerant system from one that merely prevents initial confidence inflation.

A useful mechanism should permit recovery.

---

## Assay P5 — hallucination-like source assignment versus delusion-like confidence

Build two independent readouts:

```text
source readout:
P(external | representation)

epistemic readout:
P(H | evidence graph)
```

Manipulate provenance and self-generation prediction separately.

A 2×2 design can ask whether:

- external-source assignment can change without confidence inflation;
- confidence inflation can occur without external-source phenomenology;
- both can co-occur under a broader provenance/self-monitoring failure.

This is crucial for not collapsing hallucination-like and delusion-like phenomena into one mechanism.

---

## Assay P6 — dependency estimation without explicit lineage IDs

Explicit ancestry tags may be unrealistic or too expensive.

Test whether shared ancestry can be inferred from:

- residual/error covariance;
- shared latent provenance;
- temporal co-reactivation;
- common prediction ancestry;
- response to ablation/dropout;
- context-conditioned dependency estimates.

Compare explicit genealogy, inferred soft genealogy and no genealogy.

This is the bridge toward a live REE shadow diagnostic.

---

## Shadow-only REE stage

Only after P1–P6 establish a non-tautological measurement.

Observe without changing action:

```text
candidate belief / trajectory
source families contributing
shared-ancestor probabilities
replay / prediction / observation status
existing confidence / precision
future external evidence
later action reversal
```

Ask whether false-independence features predict:

- overconfidence;
- later correction;
- extra rollout value;
- harmful or low-value action;
- persistence across sleep/replay;
- sensitivity to provenance-aware ablation.

No causal authority at this stage.

---

## Global red-team controls

Every assay must include some combination of:

- content held constant across provenance conditions;
- genuine independent confirmations as a positive control;
- duplicated but correctly linked evidence;
- unknown provenance distinct from independent provenance;
- false negative ancestry links as well as false positive links;
- confidence miscalibration controls;
- no replay condition;
- world-evidence reversal;
- source-label readout separated from belief-confidence readout;
- no explicit pathology bonus or handcrafted psychosis scalar.

---

## Stop conditions

The false-evidence-multiplication branch should be weakened or abandoned if:

- provenance corruption changes source labels but not epistemic weighting;
- dependence can be handled equally well without genealogy or ancestry estimation;
- replay does not amplify false independence;
- confidence inflation disappears once ordinary calibration is corrected;
- or the effect only appears when pathology is explicitly programmed into the confidence rule.

A negative result would still be informative by separating source-monitoring phenomena from evidence-cardinality errors.

## Compact target

> **Hold content fixed. Corrupt only genealogy. If one causal lineage begins to behave like several independent witnesses, provenance has become an epistemic variable rather than merely a source label.**
