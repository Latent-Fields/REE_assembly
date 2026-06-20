# Targeted review: the commit / de-commit latch -- biology grounding (commit/release-DURATION face)

**Date:** 2026-06-20
**Owning node:** `biology_grounding_convergence_v4:BG-3` (commitment / de-commit latch grounding L1 -> L3)
**Cluster claims:** SD-034 (closure operator), MECH-090 (BG-beta commitment gate), MECH-342 (commit-maintenance-release), MECH-445 (closure->beta coupling), MECH-446 (de-commit-authority magnitude)
**Grounding framework:** ARC-106 (brain-like construction; ladder L0..L3, divergence ledger, REQUIRED psychiatric-failure-mode column)
**Why now (trigger):** V3-EXQ-689a routed **readiness-met / no-lift** on the conflict-graded selector 2x2. Per the BG-3 readiness_gate, that routing makes the **commit latch** the live grounding front: the selection-face levers (conflict-graded width `k`, commit-temperature `T`) act at SELECTION and do not shorten/lengthen latch occupancy, so the residual ceiling is on the duration face (the ~2400-2600-step natural-commit latch occupancy that swamps the de-commit -- 460h / GAP-I `governance_2026_06_20`).

## Scope -- and what this review is NOT

This is the **commit/release-DURATION face** of the F-dominance front: how a committed action is *sustained* and then *released*, and what sets the *duration* of the hold. It is deliberately **distinct** from the **SELECTION face** -- Go/No-Go opponency, STN-hyperdirect conflict hold, pallidal permission gate, value divisive normalisation -- which is grounded in the parallel `targeted_review_connectome_mech_439` extension (owned by the ARC-107 selector-constitution lit-pull, MECH-448/449). Where the two faces meet (the indirect/No-Go pathway as the locus of the over-maintenance pole), this review cross-references rather than duplicates.

It also does not duplicate three existing reviews it sits beside:
- `targeted_review_connectome_mech_445` -- beta-band status-quo signal (Engel & Fries 2010) + transient beta bursts (Echeverria 2022): the **coupling/oscillation** substrate of MECH-445, not the duration law.
- `targeted_review_commit_boundary_belief_lock` -- post-decision dissonance / belief-lock (the *cognitive* commitment-consolidation face).
- `targeted_review_play_commitment_loop_personality_window` -- the developmental commitment/personality window (INV-075).

## The five anchors

| # | Paper | Evidence class | Axis it grounds | Claims | Direction | Conf |
|---|-------|----------------|-----------------|--------|-----------|------|
| 1 | Resulaj, Kiani, Wolpert & Shadlen 2009, *Changes of mind in decision-making*, Nature [DOI](https://doi.org/10.1038/nature08275) | behavioral_human | Change-of-mind / bounded post-commit reversal window (de-commit exists) | MECH-446, SD-034 | supports | 0.66 |
| 2 | Jin, Tecuapetla & Costa 2014, *Basal ganglia subcircuits ... parsing and concatenation of action sequences*, Nat Neurosci [DOI](https://doi.org/10.1038/nn.3632) | electrophysiology_single_unit | BG commitment maintenance + start/stop boundary signals | MECH-090, SD-034, MECH-342 | supports | 0.63 |
| 3 | Thura, Cabana, Feghaly & Cisek 2022, *Integrated neural dynamics of sensorimotor decisions and actions*, PLoS Biol [DOI](https://doi.org/10.1371/journal.pbio.3001861) | electrophysiology_single_unit | Commitment as state-transition; **what TIMES commitment** (graded BG/pallidal urgency) | MECH-342, MECH-090 | mixed | 0.60 |
| 4 | Loh, Rolls & Deco 2007, *A dynamical systems hypothesis of schizophrenia*, PLoS Comput Biol [DOI](https://doi.org/10.1371/journal.pcbi.0030228) | computational_model | **One stability parameter sets duration AND both psychiatric poles** | MECH-090, MECH-342 | supports | 0.62 |
| 5 | Seif 2025, *Does Dysregulation Of The Indirect Pathway Contribute To The Pathophysiology Of Catatonia ...*, Clin Neuropsychiatry [DOI](https://doi.org/10.36131/cnfioritieditore20250306) | theoretical_review | Over-maintenance clinical pole (catatonia = No-Go over-pressure) | SD-034, MECH-446 | supports | 0.50 |

(Anchor 2 cites Jin & Costa 2010, *Start/stop signals emerge in nigrostriatal circuits during sequence learning*, Nature [DOI](https://doi.org/10.1038/nature09263), as its boundary-signal predecessor.)

## What the biology says, mapped to the cluster (L1 -> L2)

- **Commitment is a held-but-releasable state, not an irreversible argmin** (Resulaj 2009). Biology keeps a bounded reversal/release window open after commitment. -> grounds **MECH-446** (de-commit authority) and **SD-034** (closure release): the latch must support release, and release is normal architecture, not failure.
- **The latch has recorded entry / maintenance / release components** (Jin 2014; Jin & Costa 2010). Start/stop neurons bracket a committed sequence (commit-entry = MECH-090 gate close; commit-release = SD-034 done-token); a separate sustained population holds across the whole sequence (= the MECH-090 maintained routing state, modulated by MECH-342). -> grounds the three-part **MECH-090 / SD-034 / MECH-342** structure.
- **Commitment is a discrete state-transition whose TIMING is set by a graded urgency signal carried by the pallidum** (Thura 2022). The BG output REE abstracts is exactly where commitment timing lives. -> grounds **MECH-090** (commitment as a state-transition / gate flip) and **MECH-342** (release should be graded/state-dependent, not a fixed timeout).
- **A single stability parameter sets how long a state is held, and mis-setting it produces opposite clinical poles** (Loh/Rolls/Deco 2007). Shallow basin -> early collapse / distractibility; deep basin -> over-stable / perseverative. -> grounds REE's premise that **one duration parameter** governs the latch and that the **two-poled psychiatric column** is the natural consequence.
- **Over-maintenance has a concrete clinical face in indirect-pathway (No-Go) over-pressure** (Seif 2025). -> grounds the **over-maintenance pole** and ties it to the same No-Go machinery as MECH-260/MECH-449.

## Divergence ledger (ARC-106) -- the load-bearing entry first

| # | REE mechanism | Biological reference | Divergence | Load-bearing? | Ablation falsifier |
|---|---------------|----------------------|------------|---------------|--------------------|
| D1 | **Commitment DURATION set by a tuned, committed-run-scaled beta-gate refractory** (MECH-090/MECH-446 timer) | Commitment timing set by a **graded, dynamically-rising BG/pallidal urgency** signal (Thura 2022); maintenance lasts **as long as the concatenated action executes** (Jin 2014) | REE times the hold with a **hand-set refractory clock**; biology times it with an **online graded urgency** and/or makes maintenance **co-extensive with the behaviour**. This is the "tuned, not bio-sourced" divergence the BG-3 node names. | **YES (the headline)** | A refractory-independent / urgency-graded release lever changes committed-epoch length and lifts the de-commit DV where the fixed refractory does not (460i-successor on the commit-entry-decisiveness rung). If a graded-release lever beats the fixed refractory, D1 is confirmed load-bearing; if not, the refractory is adequate and D1 is decorative. |
| D2 | **De-commit triggered by a closure/completion TOKEN** (SD-034 done-token; MECH-445 coupling) | Reversal triggered by **evidence still in the processing pipeline** at commitment (Resulaj 2009) | REE's release trigger is a discrete closure event; biology's is continued evidence accumulation. Shared FUNCTION (bounded release), different trigger. | Medium | A closure-token-gated release reproduces the bounded, error-biased reversal pattern (release more likely to correct than to spoil). If REE's closure release fires indiscriminately of correctness, the mapping is decorative. |
| D3 | **Single commitment-gated routing VARIABLE** (MECH-090) | **Two pathways** (direct/indirect) doing different things during maintenance vs termination (Jin 2014) | REE collapses direct/indirect into one variable, losing a structural "hold this / brake that" dissociation. Justified by inspectability (the seam makes closure act on a named object). | Low-medium (justified simplification) | A two-pathway latch expresses a hold/brake dissociation a single variable cannot. Build only if a single variable demonstrably cannot reach the de-commit DV (sequenced behind D1). |
| D4 | **Discrete gate flip** between an E3 selection event and a downstream routing variable | Commitment as a **continuous fall-off from a deliberation manifold** within one integrated system (Thura 2022) | REE keeps an explicit selection/commit seam; biology shows a smooth trajectory. Justified by inspectability. | Low (justified simplification) | n/a for the duration question; logged for completeness. |

**D1 is the divergence this node exists to resolve.** Anchors 2 and 3 jointly say biology does not appear to keep a *separate* latch-duration clock: maintenance is either co-extensive with the executing action (Jin) or timed by an online urgency signal (Thura). REE's separate, tuned refractory is therefore a genuine departure -- and the 460h/GAP-I finding (selection-face levers `k`/`T` do not shorten latch occupancy) is the V3 symptom of exactly this: REE has no graded duration lever, only a fixed refractory.

## Psychiatric-failure-mode column (ARC-106 REQUIRED)

| Component | Break | Disorder analog | Anchor |
|-----------|-------|-----------------|--------|
| Latch duration / refractory **too long** (over-maintenance) | held state cannot be released; de-commit too weak to overcome maintained occupancy | **Rigidity / perseveration; catatonia** (stupor, rigidity, stereotypies) = indirect-pathway / No-Go over-pressure | Seif 2025; deep-attractor pole of Loh/Rolls/Deco 2007 |
| Latch duration / refractory **too short** (under-maintenance) | held state collapses early; commitment cannot be sustained against noise | **Distractibility / disorganisation**; unstable goal maintenance | Loh/Rolls/Deco 2007 (shallow basin -> instability/distractibility) |
| De-commit / reversal window **absent or too weak** | cannot correct a committed error | perseverative error, failure of self-correction | Resulaj 2009 (loss of the error-biased change-of-mind) |
| De-commit / reversal window **too open** | reverses commitments biology would reaffirm | vacillation, impaired follow-through | Resulaj 2009 (the reaffirm/reverse balance) |

Honesty guardrail (ARC-106): catatonia is multi-determined and benzodiazepine-responsive; this column states what disorder each break *resembles*, not that REE's latch *is* the disorder mechanism. A speculative mapping that would mislead a clinician is worse than none.

## Grounding-ladder status after this review

- **Before:** BG-3 at **L1** (functional-analogy-named; "beta-gate refractory" was an analogy with no lit anchor and the divergence was tuned-not-sourced by assertion).
- **After this review:** BG-3 at **L2** (literature-anchored: each cluster component has >=1 biological anchor; the load-bearing D1 divergence is explicitly stated with a named falsifier; the two-poled psychiatric column is anchored). **Not L3** -- L3 requires the divergence to be *validated on a REE falsifier* (the 460i-successor on the commit-entry-decisiveness / graded-release lever), which is gated behind the GAP-I selection-face front and not yet run.

## Hand-off / next steps (not done here)

1. **L2->L3 is gated on a REE experiment, not more literature.** The D1 falsifier is the 460i-successor (refractory-independent / graded-release lever vs the fixed refractory) on the `f_dominance_conversion_ceiling` commit-entry-decisiveness rung. Do **not** queue it on the current selector before GAP-I closes (it will re-confirm the ceiling -- same gate as the selection-face retests).
2. This grounding is **unconditional** (BG-3 needed its L2 anchor regardless of 689c). The *build* decisions (MECH-445/446 substrate levers) remain gated on the GAP-I / 689c outcome.
3. Cross-linked into: BG-3 `completion_note` (`biology_grounding_convergence_v4_plan.md`) and the ARC-107 design note (`arc_107_selector_constitution_design_2026-06-20.md`, the commit/release-duration face / risk s9.5 "commitment instability").
