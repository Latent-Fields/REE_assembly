# Failure Autopsy: MECH-025/Q-007/MECH-116/ARC-032/MECH-099/ARC-030/ARC-038/SD-019/SD-020, 24 nominal / 2 formal targets

**Generated:** 2026-08-08T19:22:21Z
**Scope:** cluster (6 threads, round-4 grandfathered-backlog sweep)
**Status:** confirmed (Step 8 interactive gate: user confirmed `substrate_ceiling` for Q-007's EXQ-200 over leaving it open for a 4th attempt)

## Overview

22 of this batch's 24 nominal run_ids are already-digested historical evidence (naming-convention duplicates, prior-round citations, or claims.yaml prose already reaching the correct diagnosis). Two genuinely needed fresh adjudication.

## Thread A -- MECH-025 doing-mode (4 runs, fully deferred)

`050`, `050`-dup (naming duplicate), `050b`, `199`: all defer entirely to the already-closed `mech-025-dv-redesign-cf8c06` session's V3-EXQ-876/876a work, per the standing caution against competing routing on this exact lineage. claims.yaml's note (as of 2026-08-03) already gives the definitive read: `doing_mode_delta` is consistently negative (4/5 seeds), opposite the predicted sign, `non_contributory`/`measurement_test_design_defect` -- V3-EXQ-876a is already queued implementing the corrected DV (reversed Thura & Cisek 2014 convergence sign). No new work owed. `governance-note-only`, cite the 876a lineage.

## Thread B -- Q-007 z-beta/valence precision (3 runs: 2 covered, 1 fresh) -- FIRST FORMAL CEILING STAMPING

`051` and its naming-duplicate: fully digested, verbatim match to claims.yaml's own EXQ-051 note (pearson_r=-0.0285/-0.0329, 3/5 criteria met). `051c`: digested (C1 PASS, C2/C3 FAIL, r=0.000, mean_rv flat at 0.500).

**`200` (genuinely new)**: never mentioned in Q-007's claims.yaml note despite being the same-day (later) successor -- self-declares "Supersedes: V3-EXQ-051c" in its own summary.md. Same rv-to-z_beta pathway now wired (`volatility_signal_dim=1`), but the result is **worse than its predecessor**: C1 FAIL (was PASS in 051c), C2 FAIL (r=0.0888, still <0.3), C3 FAIL, 0/3 criteria met -- `mean_rv` is *higher in the stable condition (0.0055) than volatile (0.0052)*, backwards from the intended direction.

**Trajectory**: 051 (r=-0.03, 3/5) -> 051c (partial C1 pass, r=0.000) -> 200 (0/3, regression). Three distinct engineering attempts at the identical Pearson-correlation DV, zero clean passes, most recent attempt *regressing* rather than converging. **Step 8 decision (user-confirmed, recommended option)**: categorize `substrate_ceiling` on first formal stamping (matches the sd029-arc030-cluster file's own precedent for "first stamping already exceeds threshold" reasoning) -- fold EXQ-200 in at this category and route to `/implement-substrate` (a controlled test-bed redesign isolating whether the rv-injection mechanism or the volatility calibration is the fault), explicitly refusing a 4th same-question letter.

## Thread C -- MECH-116/ARC-032 E1 goal-conditioning + theta-bypass (4 runs, fully covered)

`076d` (criteria 1/4, budget too short), `076e` (criteria 0/3, `goal_dim` unset bug), `076f` (bug fixed, still 0/3, reclassified non_contributory -- wrong DV, decay rate not prediction error), `228a` (z_goal precondition failure, `non_contributory`) -- all explicitly digested in claims.yaml's exhaustive note. **V3-EXQ-228b is already queued**, explicitly `supersedes: V3-EXQ-228a`, on a validated substrate (`goal_norm >> 0.05`). Frame 228a as closed historical evidence feeding an already-in-flight redesign, not a fresh open question. `governance-note-only`, no new work.

## Thread D -- MECH-099 three-stream (2 runs) + ARC-030 138a (already-addressed)

`098` (Run 1: `auc_delta=0.0000`) and `098` (Run 2, 400ep warmup: `auc_delta=-0.0384`, lateral head underperforms baseline): both verbatim-matched to claims.yaml, both `evidence_direction: weakens` on manifest matching the note. `138a`@043647Z: confirmed already-addressed via `failure_autopsy_grandfathered-sd029-arc030-cluster_2026-08-08.json` (named in that file's `excluded_dry_run_ids` as a degenerate manual sanity invocation, warmup=2/eval=1). The standing claims.yaml correction from that prior round (criteria_met stated as 2/5 but the run's own summary.md says 1/5) remains outstanding -- restated here for visibility, not re-flagged as new. `governance-note-only`.

## Thread E -- ARC-038 schema assimilation (4 runs: 3 covered, 1 fresh)

`191` (budget-ceiling confound, digested), `355` (ENABLED=ABLATED bit-identical, digested), `355a` (optimizer-isolated, still bit-identical, reclassified non_contributory 2026-04-19 -- MECH-261 write-gating-propagation failure).

**`267` (genuinely new)**: manifest self-marks non_contributory ("ENABLED and ABLATED conditions produced completely identical metrics across all 3 seeds... pending /diagnose-errors"), but never walked into ARC-038's own evidence_quality_note -- mentioned only in passing, bundled into an unrelated INV-049/sleep-substrate diagnosis line. Chronologically the second attempt (between 191 and 355), shows the **identical** bit-identical-conditions signature that 355/355a later got correctly explained as a MECH-261 write-gating-propagation defect (landed 2026-04-22, four days after 355a). Since 267 predates MECH-261 by 12 days, the same explanation applies retroactively.

**Live finding**: MECH-261 has been stable for 3+ months as of this autopsy (2026-08-08, per the 2026-08-07 currency check already in claims.yaml) -- a proper retest per the already-drafted three-arm design in claims.yaml's `what_would_answer` field is now unblocked, not still blocked.

**Recommended (267)**: `measurement_test_design_defect`, `non_contributory`, fold into ARC-038's note with the same explanation as 355/355a, `governance-note-only` -- flag the retest opportunity to `/queue-experiment` separately (per the existing spec, not queued here per scope discipline).

## Thread F -- SD-019/SD-020/SD-011/Q-036 (5 runs) + ARC-030 331_dry (already-addressed)

`323`x2 (SD-019, `mixed`, both digested verbatim), `324`x2 (SD-020/SD-011/Q-036, all already governance-reclassified per-claim with explicit splits, digested verbatim). `331_dry`: confirmed already-addressed via `failure_autopsy_grandfathered-sd029-arc030-cluster_2026-08-08.json` (`excluded_dry_run_ids`, self-declared dry by content). `governance-note-only`, confirmation only.

## Biological-reference triage

All 8 claims touched (MECH-025, Q-007, MECH-116, ARC-032, MECH-099, ARC-038, SD-019, SD-020) have present targeted literature reviews. No fresh `/lit-pull` gap.

## Re-derive brake state (R1-R3)

MECH-025=1, Q-007=1 (before this stamping), MECH-116=3, ARC-032=3, MECH-099=2, ARC-038=0, SD-019=0, SD-020=1 -- none at threshold before this round. **Q-007 fires with this round's stamping of EXQ-200** (first formal `substrate_ceiling` for the claim, justified by the 3-attempt regression trajectory rather than a bare count); routed to `/implement-substrate`, refusing a 4th same-question letter.

## Recommended routing summary

- **Thread A**: `governance-note-only`, defer to 876a.
- **Thread B**: `governance-note-only` fold-in for the note + `/implement-substrate` for the redesign; explicit re-queue refusal.
- **Thread C**: `governance-note-only`, defer to 228b.
- **Thread D**: `governance-note-only`, cite prior round for 138a, restate standing claims.yaml correction.
- **Thread E**: `governance-note-only` fold-in; flag retest-now-unblocked for `/queue-experiment` separately.
- **Thread F**: `governance-note-only`, confirmation only.

## Learning extracted

1. A run's own self-diagnosis (267's "non_contributory pending /diagnose-errors") can sit undigested in a claim's note for months even when the explanation for a chronologically-later sibling already applies retroactively -- worth checking every self-flagged run against its family's eventual resolution, not just the ones formally cited.
2. A first-time formal `substrate_ceiling` stamping is legitimate when the attempt trajectory itself shows the brake's trigger shape (regression rather than convergence across 3 attempts), even though no individual attempt was previously stamped -- consistent with the sd029-arc030-cluster file's own precedent this round.
3. This batch was overwhelmingly a confirmation pass (22/24 already correctly digested) -- a useful data point on how much of the grandfathered backlog is genuinely fresh vs. structurally re-cited, now visible across 5 rounds of this sweep.
