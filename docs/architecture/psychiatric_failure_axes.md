---
nav_exclude: true
---

# Psychiatric Failure Modes as Latent Vulnerability Axes

*Registered 2026-06-09 from the `2026-06-06_psychiatric_genetic_overlap_latent_failure_axes`
thought intake. Home doc for RA-002, ARC-086, Q-064, MECH-371. This doc adds a **second,
cross-cutting index** on top of the per-syndrome failure-mode maps in
[`psychiatric_failure_modes.md`](psychiatric_failure_modes.md); it does not replace them.*

---

## Motivation

A large-scale genomic study (RA-002) finds that 14 clinically distinct psychiatric disorders share
a small set of latent genomic factors that cut across diagnostic boundaries. The REE-relevant
extraction is **not** genetic determinism. It is the **surface-cluster principle**: psychiatric
categories are emergent clusters over overlapping latent vulnerability dimensions, not genetically
discrete natural kinds.

REE already holds this stance — see IMPL-005 (`docs/REE_failure_modes.md`), the
`FAILURE-2026-02-12_COORDINATE-SYSTEM-FOR-COGNITIVE-PATHOLOGY` thought ("orthogonal taxonomy
organised by dynamical failure geometry rather than historical narrative"), INV-061 ("different
failure signatures of the same undertrained mechanism"), and MECH-343/Q-056 (one loop, many
syndrome-analogue failure modes). What this cluster **adds** is an explicit, finite, named
**cross-cutting vulnerability-axis vocabulary** as a *second* formal index over the named failure
modes, a representation of syndromes as weighted axis-vectors, and a p-factor analogue.

> **Guardrail (carried into every claim here).** The axis layer is an **indexing** layer, never a
> **merging** layer. Two failure modes sharing an axis does not make them the same failure.
> Psychosis (MECH-094 / MECH-201), confabulation (MECH-094 recall/completion sense), derealization
> (MECH-200), OCD (SD-034/045/046), the depressive attractor (INV-053/054), and the catatonia
> subtypes (SD-036/MECH-279 vs MECH-343) remain mechanistically distinct. See
> `memory/feedback_psychosis_confabulation_distinction.md`.

---

<a id="ra-002"></a>
## RA-002 — Psychiatric genomic-factor overlap (external anchor, out-of-domain)

Grotzinger A. D. et al., "Genetic overlap across 14 psychiatric disorders," *Nature Genetics*
(2025), DOI [10.1038/s41588-025-02494-7](https://www.nature.com/articles/s41588-025-02494-7).
Genomic SEM across 14 disorders in >1 million individuals; the majority of case-vs-control genetic
variance is captured by **five shared genomic factors** — **Compulsive; Schizophrenia-bipolar
(psychotic-mood); Neurodevelopmental; Internalizing; Substance-use** — spanning **238 variants**,
with factor-specific biology (oligodendrocyte genes enriched in the Internalizing factor) acting
early in brain development.

`epistemic_category: out_of_domain`. The test domain is a human-genetics cohort; **no REE substrate
distinguishes genomic factors**, so this is never cited as REE mechanism evidence — it is an
external corroboration anchor for the surface-cluster principle and motivates ARC-086 / Q-064 /
MECH-371. **Anti-determinism guardrail:** genetic overlap is not proof diagnoses are meaningless,
and individual presentations cannot be read from polygenic factors.

---

<a id="arc-086"></a>
## ARC-086 — Two-axis failure-mode index (named mode × latent vulnerability axis)

REE's failure-mode taxonomy is indexed on **two axes at once**:

1. **Named failure mode** — the existing mechanistically-distinct entries (psychosis, confabulation,
   derealization, OCD, depressive attractor, catatonia subtypes, …). *What breaks.*
2. **Latent vulnerability axis** — a finite, named set of dimensions that cut **across** the named
   entries. *Along which shared dimension the vulnerability sits.*

**Candidate axis set** (descriptive; refine as the registry matures):

| Axis | Closest existing REE substrate |
|---|---|
| precision / confidence allocation | ARC-005 control plane, MECH-251 precision family |
| commitment threshold / action-release authority | E3 commit boundary, MECH-090/342, SD-034 |
| provenance / source tagging | MECH-094, MECH-037, INV-011 |
| agency attribution | (self-vs-other authorship tagging; cross-ref taxonomy repo) |
| residue / consequence persistence | ARC-013 residue geometry, SD-010/SD-011 |
| goal / salience / incentive coupling | INV-034, MECH-112/116, SD-012, MECH-186-188 |
| self-other coupling | ARC-010 social cluster, Steve cluster (MECH-182/193 …) |
| offline integration / replay | INV-045/049, MECH-121/273/285 |
| social-contagion / cross-agent coupling | (multi-agent; V4/V5) |
| global instability (p-factor analogue) | **no existing claim → MECH-371** |

Named clinical syndromes are **emergent clusters — weighted combinations — over these axes**, not
primitive kinds; comorbidity is overlapping axis activation; pleiotropy is one mechanism loading
multiple axes.

`claim_type: architectural_commitment`, `status: candidate`, `epistemic_category:
substrate_conditional` (explicit, mirroring ARC-085): a candidate organizing principle whose
weighted-vector read-out (Q-064) has no V3 substrate. The documentation indexing can begin now; the
vector substrate is V4/V5. depends_on IMPL-005, INV-061, MECH-343, RA-002.

---

<a id="q-064"></a>
## Q-064 — Syndrome as a weighted axis-vector? (open question)

Should a clinical syndrome be represented as a **weighted vector over the ARC-086 axes** (comorbidity
= axis-overlap; pleiotropy = one mechanism loading multiple axes) rather than as the current
per-syndrome locus mappings? `epistemic_category: answer_state`. Two sharp sub-questions:

- **Registry economy** — comorbidity as overlapping axis activation must not require a combinatorial
  blow-up of claim entries.
- **Predisposition vs expression** — genetic-risk ≠ inevitability maps to *axis-predisposition +
  environment + developmental timing + plasticity*; the representation must separate "which axes are
  fragile" from "which failure mode is currently expressed."

Resolvable in REE only once the ARC-086 vector substrate exists (V4/V5); off the V3 critical path.

---

<a id="mech-371"></a>
## MECH-371 — Global-instability / control-plane vulnerability axis (p-factor analogue)

A single broad dimension of **control-plane regulatory fragility** — instability in
precision/gain/threshold setpoint regulation (ARC-005) rather than any one comparator or stream —
loads **across all** failure modes, raising joint susceptibility, distinct from and orthogonal to
any single-axis failure. This is the **general-psychopathology / p-factor analogue**, and it is the
one axis in the ARC-086 set with **no existing REE home** (the other axes map onto owned substrate;
see the table above).

`claim_type: mechanism_hypothesis`, `status: candidate`, `epistemic_category: substrate_conditional`,
V4/V5. RA-002's shared-variance finding and the Caspi & Moffitt p-factor literature motivate the
dimension; a brief general-psychopathology lit-pull would sharpen it before any promotion.
**Guardrail:** a global-instability axis is an additional orthogonal loading — it does *not* claim
all psychopathology is one thing, and it does not erase the distinctness of the specific failure
modes. depends_on ARC-086, ARC-005, RA-002.

---

## Cross-repo

This cluster also seeds a **latent-vulnerability-axis layer** in the separate
`Latent-Fields/ai-cognitive-failure-taxonomy` repository (a `docs/latent_vulnerability_axes.md` layer
beneath that repo's named failure-mode entries). That work lives in that repo, not in `claims.yaml`.

---

## Status

All four claims are `status: candidate` and promotion-suppressed by epistemic category
(out_of_domain / substrate_conditional / answer_state). None promote or demote any existing claim.
Off the V3 / GAP-7 critical path; no experiment is queued (a probe would be vacuous — there is no
multi-axis-vulnerability substrate in V3, and RA-002 is out-of-domain).
