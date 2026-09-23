---
title: Papez Circuit (Functional Analog)
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 11
---

# Papez Circuit (Functional Analog)

**Claim Type:** mechanism_hypothesis  
**Scope:** Provenance gating / reality filtering via a Papez-like loop  
**Depends On:** ARC-007, ARC-018, ARC-003, ARC-005  
**Status:** provisional  
**Claim ID:** MECH-037
<a id="mech-037"></a>

---

REE can treat a **Papez-like loop** as a functional **reality-filtering / provenance-gating** mechanism rather than a
direct anatomical claim. The core idea is that E1-generated content should not reach high-precision commitment unless
retrieval-coupled filtering, running concurrently with encoding, supports it with hippocampal trace structure and
temporal context. This reduces confabulation-like failure where internally generated content is treated as real
without adequate provenance.

> **Architecture decision (2026-09-23, GFLAG-0340, option A, user-accepted).** This page used to carry two
> incompatible accounts: an "operational" sequential gate (read a trace store, then license commitment) and a
> concurrent affective retrieval-augmentation account. MECH-037 could not get a falsifier that could fail while both
> stood. The **retrieval-augmentation account is adopted**. The sequential-gate account is kept below as history
> only. The literature favours the concurrent account: Theze 2017 finds OFC-MTL theta coherence at 200-330 ms, while
> Liverani 2015 (temporal-order judgment dissociates from reality filtering from 310 ms) and Bouzerda-Wahlen 2015
> (context source monitoring has no expression in the 200-300 ms window) place the sequential gate's nominated inputs
> downstream of any sequential gate window (lit pull REE_assembly 983bf73c8f3).

## Adopted architecture: affective retrieval-augmentation

The loop is a **retrieval-augmentation stage** upstream of commitment, in which filtering and encoding are concurrent
and coupled:

- hippocampal systems retrieve relational traces,
- relay/loop dynamics stabilize temporal context,
- cingulate-like conflict/valence signals reweight retrieval eligibility,
- entorhinal interface returns a context-shaped candidate bundle back to cortical manifolds.

In REE terms, this is not "RAG as static lookup." It is **precision- and valence-modulated retrieval under viability
constraints** before E3 commitment.

Boundary clarification:

- the loop can amplify or suppress candidate trajectories,
- but it does not mint authority writes (`POL`/`ID`/`CAPS`) and does not bypass E3/verifier commit checks.

## History: the superseded "operational" (sequential gate) interpretation

Superseded 2026-09-23 (GFLAG-0340). Retained for provenance only; do not design against it.

- **Provenance gating:** E1 hypotheses are held at low precision unless a hippocampal trace / ordering signal is present.
- **Commitment filter:** E3 commitment is licensed only when provenance gating is satisfied.
- **Control-plane bias:** the control plane can down-weight untraced content or mark it as speculative.

Why it was dropped: it treats trace/ordering presence as a precondition checked *before* commitment, but the human
signals it nominates (temporal-order judgment, source monitoring) measure as slow processes *downstream* of that
window, so a falsifier built on it cannot distinguish a working gate from no gate.

## Failure mode

When provenance gating fails, E1 content can be committed without trace support, producing confabulation-like behavior:
high-confidence narratives that lack appropriate temporal or source grounding.

## Operational checklist (retrieval-augmentation)

- **Input signals:** hippocampal relational-trace retrieval, relay/loop temporal-context stabilisation, and
  cingulate-like conflict/valence signals, read *concurrently* with candidate formation, not as a precondition
  checked after it.
- **Filtering:** conflict/valence signals reweight the retrieval eligibility and precision of candidate trajectories in
  the same window as encoding. Untraced or conflict-flagged content is down-weighted in the returned candidate bundle,
  not blocked at a later licensing step.
- **Commitment rule:** E3 commits over the context-shaped candidate bundle. The loop never mints authority writes
  (`POL`/`ID`/`CAPS`) and never bypasses E3/verifier commit checks.
- **Instrument:** per-commitment precision/confidence, not correctness alone. The falsifier DV is the rise in
  high-confidence commitments of ungrounded content when the loop's reweighting is degraded (MECH-037
  `what_would_answer`).
- **Control-plane knobs:** tune the reweighting gain (false positive vs false negative tolerance) per mode.
- **Failure cues:** rising incoherence plus high-confidence commitments whose candidate bundle lacked trace support.

## Notes

This is a **functional analog** inspired by the Papez circuit’s role in memory networks and confabulation studies, not a
one-to-one anatomical mapping.

---

## Open Questions

None noted in preserved sources.

## Related Claims (IDs)

- MECH-037
- ARC-007
- ARC-018
- ARC-003
- ARC-005
- MECH-034

## References / Source Fragments

- `docs/thoughts/2026-02-09_papez_circuit_reality_filtering.md`
- `docs/thoughts/2026-02-17_papez_RAG.md`
