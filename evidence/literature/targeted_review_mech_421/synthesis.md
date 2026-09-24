# targeted_review_mech_421 -- REPORT

Timestamp for all entries: 2026-09-24T11:24:37Z. Existing corpus checked first: no record tags MECH-421 directly;
targeted_review_q_074 already holds Webb/Holyoak/Lu 2023 (emergent LLM analogy), Hummel & Holyoak 2003 (LISA)
and Whittington 2020 (TEM). None of those papers is duplicated here.

## Entries

- 2026-09-24_mech_421_rlpfc_relational_integration_christoff2001 -- supports, 0.52 -- RLPFC selectively recruited for 2- vs 1-relational integration (Raven-style); grounds the integration step, not cross-domain mapping.
- 2026-09-24_mech_421_relational_shift_causal_mapping_rattermann1998 -- mixed, 0.45 -- relational shift is real but attributed to relational knowledge growth, not a new mapper; weak discriminator for Q-074.
- 2026-09-24_mech_421_learned_relations_dora_cross_domain_doumas2022 -- mixed, 0.55 -- relations learned unsupervised then zero-shot cross-domain transfer (Breakout->Pong), but via a built-in LISA/DORA binding/mapping mechanism.
- 2026-09-24_mech_421_visipam_learned_reps_explicit_mapping_webb2023 -- mixed, 0.50 -- learned representations + explicit mapping operator beat an end-to-end deep net at zero-shot mapping (same lab as the emergent-LLM paper).
- 2026-09-24_mech_421_llm_analogy_robustness_counterfactual_lewis2025 -- weakens, 0.50 -- GPT analogy performance falls sharply on surface-novel letter-string variants while humans stay high.

## Built-in vs emergent: the key output

The literature does not support either pure horn of Q-074. The best current evidence is for a HYBRID: relational
content (predicates, representations) can be learned from experience (Doumas 2022; Rattermann & Gentner's
knowledge-driven relational shift), but the systems that transfer reliably across surface-dissimilar domains keep an
explicit alignment/binding step (DORA, visiPAM, and LISA already in the Q-074 corpus). The main evidence for full
emergence (LLMs, Webb 2023) degrades on counterfactual/surface-novel variants (Lewis & Mitchell 2025), which is
exactly the "regardless of surface features" property MECH-421 is defined by. Neural data (Christoff 2001; also
Bunge et al. 2005, not entered) show relational integration as a separable load in RLPFC, which is compatible with
either a dedicated operator or a shared integration resource that traversal would use.

## Anchors the claim named

- "relational-reasoning lit-pull (ARR-7)": this pull is a first installment against ARR-7 for MECH-421; MECH-419 not covered.
- Gentner structure-mapping: covered via Rattermann & Gentner 1998. Falkenhainer, Forbus & Gentner 1989 SME (Artificial
  Intelligence 41; DOI 10.1016/0004-3702(89)90077-5) verified via search records (pages given inconsistently as 1-62 / 1-63),
  not entered to stay within the 2-5 limit. Gentner 2010 "Bootstrapping the mind" (Cogn Sci 34(5):752-75, PMID 21564235,
  DOI 10.1111/j.1551-6709.2010.01114.x) verified on PubMed, not entered; it argues a symbol system is needed for full
  analogical ability, which bears on MECH-421's dependency on the V6 symbolic stack.
- Neural substrate: Christoff 2001 entered. Also verified on PubMed, not entered: Bunge et al. 2005 Cereb Cortex 15(3):239-49
  (PMID 15238433; separable retrieval (aLIPC) vs integration (frontopolar)); Wright et al. 2008 Front Hum Neurosci 1:8
  (PMID 18958222; children 6-13 engage RLPFC too late in analogy trials -- RLPFC function matures in adolescence);
  Bazargani et al. 2014 Hum Brain Mapp (PMID 25050424). Krawczyk: not found in the PubMed query tried; not pursued.
- Webb, Holyoak & Lu 2023: already in the Q-074 corpus (not duplicated); its main critique is entered here (Lewis & Mitchell).

## Suggested amendments to claim text (do not edit claims.yaml here)

1. MECH-421 notes: replace the binary "resist an analogy module / first test emergence" with a three-way framing:
   (a) full emergence from traversal, (b) learned relations + dedicated alignment operator (the currently best-supported
   option in the literature), (c) fully hand-built. Q-074's two-arm answer (emergent vs separate operator) should
   acknowledge the hybrid outcome explicitly.
2. Q-074 what_would_answer: add a falsifier requirement -- emergent transfer must survive surface-novel and
   counterfactual source/target pairs (Lewis & Mitchell), otherwise an "emergent" pass may be surface-similarity matching.
3. Developmental note (optional): relational mapping is preceded by an object-similarity default (relational shift) and
   depends on relational knowledge depth; an emergence test should expect and measure a surface-match baseline phase.
4. No wrong citations found in the claim notes (they cite no specific papers).

## Could not verify / caveats

- arXiv, OpenReview, ScienceDirect, Semantic Scholar, PhilPapers and Northwestern pages were all blocked by the proxy.
  Rattermann & Gentner 1998 and Lewis & Mitchell 2025 are verified only via WebSearch result records (multiple
  consistent hits each); full texts not read. Lewis & Mitchell carries no DOI/volume (url to arXiv 2411.14215 instead).
- Validator: scripts/validate_literature.py only checks records inside a repo corpus, so it was run with --repo on a
  throwaway scratch copy (schema + these 5 entries): OK, 5 records checked, 0 findings. All JSON parses.
