# Literature Synthesis: Imagination-Learning Constraint Principle (ARC-092)

**Date:** 2026-08-28.
**Purpose:** Targeted literature pull grounding ARC-092 -- the ARC-level principle that
simulated/imagined experience may license only LICIT forms of learning (consistency
checking, plan optimisation, schema integration, counterfactual exploration whose output
is a prior for future waking testing) and is FORBIDDEN from driving durable world-model
updates, prediction validation, or novel-fact generation.

**Claim under investigation:** ARC-092.

---

## Entries new to this pull

- **Cai, Mednick, Harrison, Kanady & Mednick 2009** (PNAS, `entries/2026-08-28_arc_092_rem_creativity_priming_cai2009/`)
  -- REM sleep selectively restructures associative links among already-encoded
  (waking-derived) material, with no gain in explicit item memory for the material itself.
  Direct empirical instance of LICIT schema integration: recombination without new-fact
  injection. **Supports.**
- **Friston, Rigoli, Ognibene, Mathys, Fitzgerald & Pezzulo 2015** (Cognitive Neuroscience,
  `entries/2026-08-28_arc_092_active_inference_epistemic_value_friston2015/`)
  -- Formal derivation of expected free energy (extrinsic + epistemic value) as the basis
  for policy selection over imagined/counterfactual outcomes, with the generative model
  itself updated only from real, enacted observations. Formal grounding for why
  counterfactual-exploration-as-prior-formation is a coherent, non-confabulatory LICIT
  category, and for the architectural separation MECH-094's write-gate enforces. **Supports
  (theoretical/normative, not empirical).**

## Cross-linked entries already in the corpus (not re-pulled)

Per the lit-pull skill's rule against duplicating existing pulls, the following entries
already ground pieces of ARC-092's LICIT/FORBIDDEN distinction and are cross-linked rather
than re-collected here:

- **Schapiro et al. 2017** (hippocampal complementary-learning-systems bipathway) --
  `evidence/literature/targeted_review_arc_064_bottom_up_rule_discovery/entries/2026-05-10_arc_064_hippocampal_cls_bipathway_schapiro_2017/`.
  Grounds the LICIT schema-integration mechanism (monosynaptic-pathway-style consolidation
  of statistical structure) that MECH-272/MECH-273 implement.
- **Schnider 2003** (orbitofrontal reality-filter failure -> confabulation) --
  `evidence/literature/targeted_review_papez_circuit_write_gating/entries/2026-04-16_mech_094_confabulation_ongoing_reality_schnider2003/`.
  The clinical FORBIDDEN-side anchor: loss of the provenance/reality-filter gate lets
  imagined/internally-generated content masquerade as validated real-world fact -- exactly
  the failure mode MECH-094's write-gate exists to prevent.
- **Schnider 2013** (orbitofrontal reality filtering) and **Bouzerda-Wahlen 2015**
  (reality-filter vs. source-monitoring dissociation) --
  `evidence/literature/targeted_review_uncommitted_candidate_retention/entries/2026-08-07_mech_487_orbitofrontal_reality_filtering_schnider2013/`
  and `.../2026-08-07_mech_487_reality_filter_vs_source_monitoring_bouzerdawahlen2015/`.
  Same FORBIDDEN-side typing discipline, already pulled for the sibling MECH-487 (retention
  of rejected candidates) claim; the typing requirement is shared machinery between the two
  claims (both need imagined/uncommitted content to carry a fast, separable provenance tag).
- **Botvinick & Plaut 2004** (recurrent-connectionist routine sequential action without
  explicit schema hierarchies) --
  `evidence/literature/targeted_review_rule_apprehension_vocabulary_mapping/entries/2026-05-10_vocab_mapping_no_schema_hierarchy_botvinick_plaut2004/`.
  Grounds schema/script-level computation as an emergent property of a recurrent substrate
  rather than a hand-built hierarchy -- relevant to how a schema-integration operation
  (LICIT) can be implemented without a symbolic rule store.
- **Stickgold & Walker 2013** ("memory triage": sleep-dependent selective consolidation) --
  `evidence/literature/targeted_review_autobiographical_store/entries/2026-06-13_mech_252_253_sleep_memory_triage_stickgold2013/`.
  Grounds why offline/sleep-adjacent consolidation is selective (triage) rather than
  wholesale -- consistent with ARC-092's requirement that schema integration draw only on
  waking-derived trace primitives rather than compounding self-amplification across cycles.

---

## Summary of Evidence

Two new entries (Cai 2009, Friston 2015) plus five cross-linked entries jointly ground both
halves of ARC-092. LICIT-side: Cai 2009 (empirical, human) and Schapiro 2017 /
Stickgold & Walker 2013 (empirical, consolidation) show that sleep/imagination-adjacent
offline processing restructures and selectively consolidates already-encoded material
without adding new item-level knowledge; Friston 2015 (theoretical) and Botvinick & Plaut
2004 (computational) show why and how this kind of recombination is a distinct operation
from a generative-model/world-model update. FORBIDDEN-side: Schnider 2003/2013 and
Bouzerda-Wahlen 2015 (clinical) show what happens when the provenance/reality-filter gate
that keeps this distinction load-bearing fails -- confabulation, i.e. imagined content
contaminating the real-world knowledge store. No entry in this pull weakens ARC-092;
confidence is bounded below 0.8 throughout because every mapping from human/clinical/
theoretical evidence to REE's specific substrate (MECH-094/272/273) is an architectural
analogy, not a direct measurement of ree-v3 code.
