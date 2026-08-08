# Failure Autopsy: Round-6 grandfathered-backlog closure sweep, 108 targets

**Generated:** 2026-08-08T20:16:08Z
**Scope:** cluster (round-6 grandfathered-backlog sweep — a closure sweep, not fresh diagnosis)
**Status:** confirmed (no Step 8 gate needed — every disposition in this file reaffirms an already-confirmed prior finding under a corrected run_id, except Q-001 which is genuinely new and non-controversial)

## What this round actually found

Round 5 closed 120 of the 228 grandfathered run_ids remaining after round 4. Regenerating `pending_review.md` afterward still showed 115 (later recomputed exactly as 108 by direct corpus diff). Investigating why revealed the real finding of this round: **the overwhelming majority of the "remaining" 108 run_ids were already correctly diagnosed by rounds 3–5** — they never needed fresh research at all. They stayed in the backlog for one of three reasons:

1. **Naming-convention duplicates.** The same physical manifest exists under both a prefix-timestamp directory form and a suffix-timestamp form; an earlier round diagnosed one form and the other form's distinct run_id string was never separately stubbed.
2. **Prose-only citations.** An earlier round's `cross_reference_note` correctly said "already covered, cite only" — but a prose citation is invisible to `pending_review.md`'s blind-spot check, which only clears a run when its exact run_id appears in a `targets[].run_id` field.
3. **Malformed target run_ids — the consequential class.** In several earlier rounds (mine, this session, rounds 3–5), a target was written with a *hand-composed* run_id rather than one copied verbatim from the manifest listing — missing timestamp digits, an abbreviated `experiment_type` suffix, or in one case (Q-034) a fabricated middle segment that never existed anywhere in the corpus. The diagnosis itself was correct; the citation string simply never matched the real file. This is the same failure shape as the skill's own "reviewed ≠ manifest-corrected" warning, one level up: *targeted ≠ actually-matchable*.

**No fresh scientific work was needed for 107 of 108 targets** — every one restates an already-confirmed finding under the corrected, verbatim-copied run_id, with an explicit citation to which prior round/file established it. The 397d finding (round 4's most consequential result — the persistent `hippo_quality_gap` signature flagged for governance re-review) is reaffirmed here under its corrected run_id, unchanged in substance.

## The one genuinely new item

**Q-001 (EXQ-146, entity-binding discriminative pair)**: never diagnosed anywhere in the corpus before this round. Read directly: claims.yaml's own `what_would_answer` field for Q-001 already states the FAIL is "uninformative because V3 had no persistent bindable substrate and no training budget to grow one — a FAIL on the current substrate self-routes substrate-not-ready, not a falsification of emergence." The hard precondition (ARC-006, an object-file-like persistent buffer) is unbuilt. `precondition_unmet`, `weakens`, `governance-note-only`.

## Notable corrected citations (by consequence)

- **397d (ARC-007/SD-004)**: round 4's target run_id was `v3_exq_397d_arc007_matched_endpoint_20260423T_v3` — missing the `202213Z` timestamp entirely. The real manifest is `v3_exq_397d_arc007_matched_endpoint_20260423T202213Z_v3`. This is round 4's single most consequential finding (a cross-formulation-invariant signature possibly undercutting a standing governance dismissal) and it silently dropped out of the "confirmed" coverage set because of an eight-character omission.
- **MECH-111's full lineage (141/141b/141c×2/141d)**: round 4's `141b` target cited `...20260508T193500Z_v3` — a timestamp that **does not exist anywhere on disk** (round 5's batch3 agent confirmed this independently). All 5 lineage members are re-stubbed here under their verbatim-copied run_ids.
- **Q-034's full lineage (288/451×2/526)**: round 4's targets used a fabricated middle segment (`..._q034_monostrategy_lock_...`) that never matched any real `experiment_type`. Round 5's batch4 agent found this by exact Unix-epoch-timestamp matching; the content was always correct, only the citation string was wrong.
- **MECH-095/MECH-099's 098b pair**: round 4 recorded the date as `20260326T...` (March 26); the only physical manifests are dated `20260327T...` (March 27), confirmed via exhaustive search — a date typo, not a truncation.
- **dACC's full 9-run family, SD-021's 325a family (4), MECH-075's 192a/230 (4), INV-054's 278/435 (3), MECH-095/SD-047's EXQ-510, MECH-089's EXQ-066, SD-032c's EXQ-325d**: all truncated-suffix or truncated-timestamp variants of the same class, all correctly diagnosed originally.

## Biological-reference triage

Not the governing layer here — every prior diagnosis's biological grounding carries forward unchanged; this round only corrects citation strings and adds one genuinely new (Q-001, biological grounding present via ARC-006's object-file literature).

## Re-derive brake state

No new brake firings — every `substrate_ceiling`-adjacent target in this file (dACC family, 325a family, EXQ-011/089, Q-007's 051 duplicate, EXQ-510, 098b's 155605Z) reaffirms a brake that was already fired and routed by an earlier round. This file changes no routing decisions, only closes citation gaps.

## Recommended routing summary

All 108: `governance-note-only`, restating each prior round's original routing verbatim. Q-001: `governance-note-only`, `precondition_unmet` on ARC-006.

## Learning extracted

1. **A target run_id must be copied verbatim from the manifest listing (`ls`/`find` output), never hand-composed from a claim-family naming pattern.** Every malformed citation in this entire backlog sweep — across three different prior rounds, multiple different claim families — traced back to exactly this one authoring habit. Recommend this become a standing convention for `/failure-autopsy` going forward, and possibly a cheap mechanical lint (`check_dry_run_citations.py`-style) that verifies every `targets[].run_id` resolves to a real on-disk manifest before a file is marked `confirmed`.
2. The grandfathered-backlog sweep's own coverage-detection mechanism (`pending_review.md`'s blind-spot net) is exactly as strict as it needs to be — it caught every one of these gaps, including gaps in *this skill's own prior output*, not just gaps in the underlying science. That is working as designed, even though it meant a "closure" round instead of a "discovery" round.
3. A prose-only "already covered, cite only" disposition in a `cross_reference_note` is not equivalent to a formal target stub for the purposes of clearing the backlog net — every future round should default to writing a lightweight stub (as this round now has, and as round 5's 689c precedent established) rather than a prose-only citation, even when zero new diagnosis is owed.
