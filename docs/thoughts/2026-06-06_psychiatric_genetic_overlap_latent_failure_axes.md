Status: processed
Intake: evidence/planning/thought_intake_2026-06-06_psychiatric_genetic_overlap_latent_failure_axes.md
Processed in:
- `evidence/planning/thought_intake_2026-06-06_psychiatric_genetic_overlap_latent_failure_axes.md` (Stage-2 structured intake; 2026-06-09; primary source VERIFIED = Grotzinger et al., Nature Genetics 2025, DOI 10.1038/s41588-025-02494-7; NO claims.yaml registration -- failure-mode-axis compass, candidates A-E recorded for future registration only)
Source email date: 2026-03-31
Source email subject: REE: Mapping the genetic landscape across 14 psychiatric disorders - Nature
Source saved-item attribution: Daniel Golden
Current action: preserve as thought intake only
Primary source status: VERIFIED (was source-check partial) -- primary paper located: Grotzinger A. D. et al., "Genetic overlap across 14 psychiatric disorders," Nature Genetics 2025, DOI 10.1038/s41588-025-02494-7 (five genomic factors / 238 variants); the direct share.google link was still not opened but the paper + five-factor finding are confirmed via the journal + Harvard Gazette / Mass General Brigham / Live Science / WaPo coverage
Near-term relevance: psychiatry / failure-mode architecture compass; not a REE-v3 implementation target unless later linked to existing failure-mode claims
Downstream repo candidate: Latent-Fields/ai-cognitive-failure-taxonomy

---

# THOUGHT INTAKE: Psychiatric genetic overlap as latent vulnerability-axis evidence

## 0. Summary claim

A saved REE email pointed to a Nature-linked item titled "Mapping the genetic landscape across 14 psychiatric disorders". The direct `share.google` link was not opened during intake. Secondary coverage identifies a Nature study reporting large-scale genetic overlap across 14 psychiatric disorders, grouping them into several broad genomic factors rather than clean one-disorder / one-cause categories.

The REE-relevant point is not genetic determinism.

The useful architectural idea is:

> psychiatric categories may be surface expressions of overlapping latent vulnerability axes rather than discrete boxes.

This fits REE's existing framing of psychiatric pathology as failure modes of an architecture: breakdowns in prediction, control-plane modulation, self-other coupling, residue integration, commitment gating, precision routing, and offline integration may combine in different proportions to produce different clinical syndromes.

Daniel's added framing during intake:

> Our psychiatric definitions may better be clustered along these latent vulnerability axes.

This may be especially relevant for `Latent-Fields/ai-cognitive-failure-taxonomy`, because that repository is explicitly concerned with mapping AI cognitive failure modes to clinical psychopathology and computational psychiatry.

---

## 1. Why this belongs in REE_assembly

This belongs in `REE_assembly` as a psychiatry / architecture thought because it supports an important modelling stance:

- do not force psychiatric failure modes into one-to-one modules
- do not treat diagnoses as clean natural kinds
- model vulnerability as interacting latent axes
- preserve transdiagnostic mechanisms
- treat named syndromes as emergent clusters in cognifold/control-plane failure space

This may eventually inform REE's failure-mode documentation, but should not create immediate substrate work.

---

## 2. Why this may also belong in ai-cognitive-failure-taxonomy

The `ai-cognitive-failure-taxonomy` repository currently lists named failure modes such as confabulatory completion, belief fixation, feedback entrapment, commitment dysregulation, provenance collapse, precision misallocation, residue blindness, goal proxy lock-in, agency attribution failure, and modulatory signal without selection authority.

Those entries are useful named clusters, but this thought suggests an additional layer:

> failure modes may need to be indexed not only by named syndrome-like entries, but also by latent vulnerability axes that cut across entries.

Possible taxonomy-level axes:

- precision / confidence allocation
- commitment threshold / action-release authority
- provenance / source tagging
- agency attribution
- residue / consequence persistence
- goal / salience / incentive coupling
- self-other coupling
- offline integration / replay / contextualisation
- social-contagion / cross-agent coupling
- global instability / p-factor-like vulnerability

This would make the taxonomy more clinically faithful: diagnoses and AI failure modes can remain named entries, but the underlying explanatory structure would be transdiagnostic and axis-based.

---

## 3. Proposed classification

Likely classifications:

- **open question:** should REE failure-mode predictions be represented as latent axis combinations rather than diagnosis-specific mappings?
- **mechanism hypothesis:** psychiatric phenotypes may emerge from overlapping disruptions to control-plane, prediction, residue, salience, agency, and commitment systems.
- **architecture note candidate:** REE failure-mode docs should distinguish mechanistic axes from diagnostic labels.
- **taxonomy extension candidate:** `ai-cognitive-failure-taxonomy` may need a latent-axis layer beneath named failure-mode entries.

This should not be promoted directly to an invariant.

---

## 4. Relation to existing REE architecture

Potential mappings:

| Psychiatric-genetics framing | REE analogue |
|---|---|
| broad genetic overlap across diagnoses | shared vulnerability axes across failure modes |
| genomic factors | latent failure dimensions |
| p-factor / general psychopathology | global instability / broad control-plane vulnerability |
| disorder-specific surface syndromes | emergent attractors in symptom/failure-mode space |
| pleiotropy | one mechanism influencing multiple REE capacities |
| comorbidity | overlapping failure-axis activation |
| genetic risk not equal to disease inevitability | predisposition + environment + developmental timing + plasticity |

---

## 5. REE-specific hypothesis

REE's psychiatry predictions may become stronger if diagnoses are treated as surface clusters rather than primary explanatory units.

For example:

- psychosis may involve precision-routing and commitment-threshold instability, but not all psychosis has the same axis weights
- depression may involve residue accumulation and offline-integration failure, but also motivational, interoceptive, social, or fatigue axes
- mania may involve commitment-gating collapse, but may also include goal-stream amplification, reward/salience dominance, sleep/offline disruption, and reduced decommit friction
- obsessive-compulsive presentations may involve excessive threat/residue persistence, failed decommit, and over-weighted action responsibility, but the same axes may participate elsewhere

The architectural stance should be:

> diagnoses are useful clinical handles, but REE should model the underlying interacting failure axes.

---

## 6. Important cautions

Do not reduce psychiatric illness to genetics.

Do not treat genetic overlap as proof that diagnoses are meaningless.

Do not imply that individual clinical presentations can be read from polygenic categories.

Do not treat genomic factors as direct equivalents of REE mechanisms.

Do not make this a REE-v3 implementation target without a clear link to existing failure-mode claims.

The useful extraction is:

> psychiatric categories may be emergent clusters over overlapping latent vulnerability axes.

---

## 7. External anchors

Secondary coverage checked during intake:

- Live Science, "5 genetic 'signatures' underpin a range of psychiatric conditions". Reports that a Nature study published 2025-12-10 analysed more than 1 million participants and grouped 14 psychiatric conditions into five major genetic groups. https://www.livescience.com/health/genetics/5-genetic-signatures-underpin-a-range-of-psychiatric-conditions
- Washington Post, "Science shows very different psychiatric disorders might have the same cause". Reports that the study analysed data from more than 6 million people including over 1 million with psychiatric diagnoses, identified 238 genetic variants, and found five broad categories including substance use, internalising, neurodevelopmental, compulsive, and psychotic-mood groupings. https://www.washingtonpost.com/health/2026/01/01/psychiatric-disorders-genetic-bipolar-schizophrenia/

Primary lookup terms for future agent:

```text
Andrew Grotzinger Nature 2025 14 psychiatric disorders five genomic factors 238 variants chromosome 11 DRD2
```

Primary source still needs direct verification before claim extraction.

---

## 8. Proposed next extraction

If the Nature paper is verified, consider adding a failure-mode architecture note:

```text
docs/architecture/psychiatric_failure_axes.md
```

Questions for that note:

- Should REE maintain diagnosis labels only as surface examples?
- What are the core latent failure axes already present in the architecture?
- Can each clinical syndrome be represented as a weighted combination of axis failures?
- Does REE need a transdiagnostic vulnerability map?
- How should comorbidity be represented without exploding the claim registry?

For `ai-cognitive-failure-taxonomy`, consider a separate note or issue:

```text
docs/latent_vulnerability_axes.md
```

or:

```text
Issue: Add latent vulnerability-axis layer beneath named failure modes
```

---

## 9. Guardrail for future agents

If a future agent tries to convert this into a genetic-determinist claim, stop and reframe.

The correct near-term extraction is:

> model psychiatric failure modes as overlapping latent vulnerability axes.

The incorrect extraction is:

> map each diagnosis to one gene, one circuit, or one REE module.
