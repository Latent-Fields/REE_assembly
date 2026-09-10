# Provenance Error / False-Evidence Multiplication — Experiment Ladder

**Date:** 2026-09-09  
**Status:** planning scaffold; no claim registration, no creature code change, no queue mutation  
**Parent thought:** `docs/thoughts/2026-09-09_provenance_errors_false_evidence_multiplication_and_psychosis.md`

## Refinements to this ladder (added 2026-09-10)

Six companion artifacts refine the rungs below and are **not** duplicates of them; read the relevant one before implementing any rung. The rungs stand as written **except** for three changes applied inline from the judgment-class tranche's §7 recommendations, listed under "Applied inline" below.

| Artifact | Refines | Contributes |
|---|---|---|
| [`provenance_psychosis_literature_pull_20260909.md`](provenance_psychosis_literature_pull_20260909.md) | whole ladder | the clinical source-monitoring baseline; its "not directly established" row on dependent-descendants-as-votes is **corrected** by the supplement below |
| [`provenance_false_evidence_multiplication_campaign_supplement_20260910.md`](provenance_false_evidence_multiplication_campaign_supplement_20260910.md) | P1, P2, P3, P6 | hippocampal-campaign audit; the six evidence classes; Break A (nothing joins ancestry-loss mechanisms to cardinality readouts) and Break B; controls `P1-R1`–`P1-R4`, `P3-R1`–`P3-R3` |
| [`provenance_harness_generated_ancestry_design.md`](provenance_harness_generated_ancestry_design.md) | P1 | the generated-ancestry harness: descendant generators, the genealogy representation and its degradation processes, the four conditions defined on that state, and the genealogy contract P3 consumes |
| [`provenance_p3_replay_amplification_design.md`](provenance_p3_replay_amplification_design.md) | P3 | the replay loop, the design matrix, accumulation-versus-compounding split, and the preregistered signatures |
| [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) | P1, P2, P3, P6, and the engineering rule | the judgment-class sweep; normative counterweights to the engineering rule; the fluency-versus-cardinality control. **Partly applied inline — see below.** |
| [`provenance_branch_hippocampal_audit_verification_20260910.md`](provenance_branch_hippocampal_audit_verification_20260910.md) | P1, P3 | verification of the audit; the `MECH-544` demarcation on readout 3; the internally-generated-repetition evidence class; controls `P1-R5`, `P1-R6`, `P3-R4`–`P3-R7` |

**Applied inline (2026-09-10), from the tranche §7 recommendations 2, 3 and 4:**

| Where | Change | Recommendation |
|---|---|---|
| **Purpose** | new subsection *The engineering rule, restated* — the rule is about representing dependency structure, not discounting descendants | rec. 4 |
| **P2** | fourth comparator **D** (explained dependence) added to the three-way comparison, with the fixed-discount divergence rule | rec. 2 |
| **P6** | Pilditch 2020 named as a second competitor of a different kind, and a scoring requirement that penalises over-discounting | rec. 3 |

Recommendation 1 (P1's fluency-versus-cardinality control) is applied in the P1 **design** document as `P1-R7` rather than here, since the rung's condition and readout structure is unchanged by it. Recommendation 5 (the clinical gap) is an observation and queues nothing. Nothing above registers, promotes or modifies a claim.

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

### The engineering rule, restated (2026-09-10)

The branch's rule — *a hypothesis must not cite its own descendants as independent witnesses* — is correct in its **negative** form and wrong if read as *"descendants should be collapsed to one vote"*.

**Pilditch, Hahn, Fenton & Lagnado 2020** (*Dependencies in evidential reports: The case for informational advantages*, Cognition 204:104343, [DOI 10.1016/j.cognition.2020.104343](https://doi.org/10.1016/j.cognition.2020.104343), PMID 32599310) prove by construction that the traditional treatment of dependence as redundancy conflates the *structure* of a dependency network with the *observations* across it: where a structural dependency exists but observations are partial or contradicting, dependent reports support a hypothesis **more** than the independent case would. Maximal discounting is then the larger error.

The rule this ladder holds is therefore about **representation, not discounting**:

> A system must represent the dependency structure among its evidence and condition on it. It must not *infer* independence from the absence of a recorded dependency.

This is a stronger rule than the original, and it is the one P2 actually tests. It is also why P6's scoring must penalise over-discounting as well as under-discounting (see P6 below). No readout, condition or stop condition below is changed by this restatement — it fixes what a passing architecture is required to do, not what is measured. Source: [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) §3.3 and §7 rec. 4.

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
D. dependence is EXPLAINED -- the system is given a reason for the repetition,
   and the reason is varied (added 2026-09-10)
```

The desired architecture is not predeclared by intuition alone.

**On comparator D (added 2026-09-10; tranche §3.2 and §7 rec. 2).** Ambiguity about the independence relation is the empirically identified trigger for the human effect, so the supplement's promotion of `ABSENT`/`SOFT` over `FALSE_SPLIT` is confirmed and can be stated more strongly. **Connor Desai, Fai, Lee & Hayes 2026** (*Explaining away the illusion of consensus*, Mem Cognit 54(5):1667–1687, [DOI 10.3758/s13421-025-01831-9](https://doi.org/10.3758/s13421-025-01831-9), PMID 41563579; four experiments, not preregistered) shows the dependent-consensus discount is **not a fixed quantity**: it is an inference about *why* the repetition happened, and it moves in **both** directions on the reason given — raised by a positive explanation ("the source is especially reliable"), lowered by a negative one ("the repetition was intended to sway opinion") — whether the explanation is supplied by the experimenter or generated by the participant.

Comparator D therefore varies the *reason*, not just the presence, of the dependency record, in at least a positive-reason and a negative-reason condition against a bare-dependency baseline.

> **An architecture whose response to dependence is a fixed discount already diverges from the human pattern**, whatever its calibration score. Report that divergence as a divergence, not as a pass or a fail — the same treatment the supplement §5.4 requires for a `FALSE_SPLIT`-only inflation.

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

### Named competitors — two, of different kinds (2026-09-10)

**E30** (Rule & O'Leary 2022) is the first: self-healing codes track a drifting representation with no explicit lineage, so **lineage-free tracking can match explicit genealogy**.

**Pilditch 2020** (PMID 32599310) is the second and is a *different kind* of competitor — not an alternative mechanism but an argument that the target is mis-specified: **maximal discounting of dependent evidence is sometimes normatively worse than treating it as independent** (see "The engineering rule, restated" above).

**Consequence for P6's scoring, and it is a requirement rather than a note.** The scoring structure must include cases in which **dependent-but-partial observations are more informative than independent ones**, so that an over-discounting architecture is **penalised rather than rewarded**. Construct these from Pilditch 2020's own worked examples: a structural dependency present, with the observations across it partial or contradicting.

A scoring set built only from redundant-dependence cases makes "discount everything dependent" the winning strategy, which is the wrong target — it would score highest exactly the architecture the restated engineering rule rejects, and P6 would report a false winner with no internal signal that anything was wrong.

Source: [`provenance_judgment_class_literature_tranche.md`](provenance_judgment_class_literature_tranche.md) §3.3 and §7 rec. 3.

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
