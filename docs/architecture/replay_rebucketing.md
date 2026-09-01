---
title: "Replay-Driven Rebucketing (MECH-529)"
parent: "Memory & Hippocampus"
grandparent: Architecture
nav_order: 16
status: candidate
status_asof: 2026-09-01
status_claim: MECH-529
---

# Replay-Driven Rebucketing: Decision Relevance as Pressure on E1

Source thought: `docs/thoughts/2026-08-31_replay_rebucketing_decision_relevance.md`; intake:
`evidence/planning/thought_intake_2026-08-31_replay_rebucketing_decision_relevance.md`.

## MECH-529 {#mech-529}

The slow return path `decision consequences → evidence about representational sufficiency →
later E1 reorganisation`. Accumulated consequential-divergence evidence drives
split / merge / feature-reweighting / relation-discovery / boundary-revision /
abstraction-change over E1 equivalence classes, via replay of NON-CONTIGUOUS episodes under
a common evaluative frame (retrospective representation learning). Candidate rebucketings
are counterfactually tested before adoption (does the distinction improve predictions under
relevant alternative actions?), and consequential revisions preferentially complete in a
decoupled/sleep phase whose job includes RE-INDEXING episodic traces so autobiographical
addressability survives ("safe maintenance of the representational coordinate system").
Hard constraint: E3 communicates typed insufficiency signals (prediction/consequence
mismatch, harm/goal error, veto/conflict, divergent outcomes from apparently equivalent
states) — never category labels. E3 must not become E1's teacher (non-oracular). Functional
mapping to pattern separation ("this difference predicts different futures; stop treating
as equivalent") and pattern completion ("these cues identify useful common structure") —
offered as functional mapping, not a biological account of DG/CA3.

Version-placement pressure on ARC-134/MECH-521 (corrigible grain), MECH-507/512
(revisable equivalence/grain), MECH-508 (revisable attractors), and sleep/replay re-indexing
is adjudicated by the GOV-V4CUT-1 prerequisite-cut audit, preferring claim SPLITS over
wholesale relabelling.

**F3 disposition (2026-09-01, GFLAG-0103):** of the audit's two proposed plumbing
pull-forwards, only the non-oracularity half split off cleanly, as MECH-530 below. The
index-continuity half ("re-indexing... so autobiographical addressability survives") stays
inside MECH-529's v4 scope: no episodic-index/addressability concept exists anywhere in
ree_core, and the audit's stated justification -- testable against the SD-017/SD-068 harness
-- does not hold on inspection (SD-017 measures ContextMemory slot differentiation, SD-068
measures per-phase content-fidelity; neither tracks trace addressability across a reindexing
event). Index continuity is meaningful, in MECH-529's own terms, only *post-rebucketing* --
which needs the ARC-134 P0 operator this page's substrate floor already names as unbuilt. See
MECH-529's 2026-09-01 UPDATE note in claims.yaml for the full reasoning.

## MECH-530 {#mech-530}

Split from MECH-529's own "Hard constraint" above. E3's decision-outcome signals to any
downstream consumer -- including a future rebucketing mechanism such as MECH-529 -- are typed,
continuous insufficiency measures (prediction/consequence mismatch, harm/goal cost,
veto/conflict magnitude and count, commit/threshold state), never semantic category labels.
Unlike the index-continuity half above, this is independently v3-testable today: verified by
direct inspection of `ree-v3/ree_core/predictors/e3_selector.py` (2026-09-01) that
`SelectionResult` and the live `last_score_diagnostics` surface are exclusively
tensor/float/bool/int-typed, with no category-label-shaped field anywhere in E3's current
output. The contract holds now, without requiring MECH-529's rebucketing loop (or ARC-134 P0)
to exist -- and is what needs to keep holding as more downstream consumers are added. A
contract test pinning this against future additions to the diagnostic surface has not yet been
written.
