# Failure Autopsy: SD-003/MECH-112/dACC (SD-032b/MECH-258/MECH-260) grandfathered batch, 28 nominal / 2 genuinely new

**Generated:** 2026-08-08T19:22:21Z
**Scope:** cluster (3 threads, round-4 grandfathered-backlog sweep)
**Status:** confirmed (Step 8 interactive gate not required for this file -- no judgment-revising finding; the round's cross-cutting Step 8 items live in the misc1/misc2/N-cluster files)

## Overview

This batch is dominated by repository structure, not new science: ~89% of its 28 nominal run_ids are re-citations of runs already formally autopsied under the other on-disk naming convention (prefix-timestamp `claim_probe_<claim>/runs/` vs suffix-timestamp `<experiment_type>/runs/`, both filed for the same physical run). Only 2 of 28 are genuinely new evidence.

## Thread A -- SD-003 (10/10 duplicates, zero new evidence)

All 10 batch ids are the prefix-timestamp form of runs already confirmed under the suffix-timestamp form in `failure_autopsy_grandfathered-sd003-cluster_2026-08-08.json`. Verified for all 10: identical `timestamp_utc`, `claim_ids_tested`, `status=FAIL`. One cosmetic hygiene finding (not a re-diagnosis): the first pair's `evidence_direction_per_claim` differs between the two on-disk copies (suffix copy carries a per-claim mixed/supports breakdown; prefix copy states all four claims `weakens`) -- a stale-copy sync gap, worth a governance correction, not new evidence.

## Thread B -- dACC / SD-032b / MECH-258 / MECH-260 (9/9 duplicates, zero new evidence)

All 9 batch ids duplicate the already-confirmed `failure_autopsy_V3-EXQ-445h_2026-06-19.json` cluster autopsy (predating this round's grandfathered files -- found only via a full-corpus grep, not the 4 named round-3 files alone). That autopsy's own text explicitly names this batch's `445h` run at the `...063313Z` timestamp as "the duplicate run" of its formal target. All 9 batch manifests already carry the governance-applied correction fields (`non_degenerate_per_claim`, `pending_retest_after_substrate_per_claim`, `degeneracy_reason`) that autopsy's Step 9 wrote across the whole lineage.

**Peripheral finding for governance**: a *later* file (`failure_autopsy_f-dominance-conversion-cluster_2026-06-20.json`) blanket-applied `substrate_ceiling` across all three co-tagged claims (SD-032b, MECH-258, MECH-260) with no per-claim map. MECH-258's C1 (forward-model R^2) was never floor-locked in the 445-lineage data -- claims.yaml carries no ceiling category for MECH-258 today, and this looks like a peripheral-co-tag miscount rather than a deliberate stamping. Not corrected here (this skill never edits claims.yaml); flagged for governance to fix.

## Thread C -- MECH-112 (9 batch ids: 4 dry, 3 near-dup, 1 pattern-matched twin, 1 genuinely new)

MECH-112 is a **deprecated claim ID** (claims.yaml, 2026-04-13 atomic split -> MECH-229 behavioral wanting/liking + MECH-230 z_goal latent structure). Every item below inherits this stale-tag caveat.

- **Dry-run quad** (`238` @185519Z, `328_dry` @155804Z, `328a` @102503Z, `328a` @111655Z): all self-declare dry/smoke in `evidence_direction_note` text (`"Dry-run / smoke test output... Not a real experiment run"`, `"Non-contributory pending full run"`, `"Dry run (3 eps x 10 steps): smoke test only"`). Schema-side `dry_run` boolean absent (pre-2026-07 manifest gap) -- automated checker reports these clean/unflagged, confirming manual content verification remains necessary for this era. All 4 already named in the wanting-liking cluster's `excluded_dry_run_ids`.
- **Near-duplicates** (`074f` x2 @001929Z/@002135Z, `235` @1775399046): content-identical `evidence_direction_note` to already-covered same-family siblings (`074f` triplet: "ran without serotonergic substrate MECH-186/187/188 absent... non_contributory"; `235`: middle of 3 same-day seed runs, other two already `substrate_ceiling`/non_contributory). Same disposition applies, no fresh diagnosis.
- **527 (new, pattern-matched)**: twin of the already-covered `527_..._080028Z_v3` ("cleanest never-touched specimen" per the wanting-liking cluster autopsy -- stale tag, claim deprecated, metrics.json empty, never referenced in claims.yaml). Recommended: `measurement_gap`, `non_contributory`, `governance-note-only`.
- **257 (genuinely new)**: `v3_exq_257_sd018_resource_prox_validation_20260406T171952Z_v3`, co-tagged SD-018/ARC-030/MECH-112, sole run in its family, no prior autopsy artifact. `z_goal_norm~1e-10` in 2/3 seeds (SD-012 homeostatic-drive substrate absent) blocks resource-proximity head training. Manifest already carries an informal 2026-04-09 governance note reaching the same read; SD-018=weakens maintained since the implementation was directly tested even though behavior could not be demonstrated. Recommended: `precondition_unmet`, `non_contributory`, `pending_retest_after_substrate: true`, `governance-note-only` -- the SD-012 gap is already owned elsewhere (same gap blocking the whole MECH-229/230 family), no new substrate_queue entry needed.

## Biological-reference triage

SD-003, dACC lineage (SD-032b/MECH-258/MECH-260), and MECH-112/SD-018 all have present, previously-established biological references (already fully cited in the artifacts this batch cross-references). No fresh `/lit-pull` gap found in this batch.

## Re-derive brake state (R1-R3)

Neither of the 2 genuinely-new targets (257, 527) is recommended `substrate_ceiling` -- 257 is `precondition_unmet` (excluded from the R3 count by convention) and 527 is `measurement_gap`. **The brake does not fire anywhere in this batch.**

## Recommended routing summary

- **Thread A (SD-003)**: no action, cite existing sd003-cluster autopsy; flag the evidence_direction_per_claim sync-gap to governance as hygiene.
- **Thread B (dACC)**: no action, cite existing V3-EXQ-445h autopsy; flag the MECH-258 peripheral-co-tag miscount to governance.
- **Thread C (MECH-112)**: dry quad and near-dups, no action (cite existing). 527, `governance-note-only`. 257, `governance-note-only` (SD-012 gap already tracked).

## Learning extracted

1. A full-corpus grep (not just the round-3 named files) was necessary to find dACC's real covering artifact (`V3-EXQ-445h`, a pre-existing standalone file outside the grandfathered-file set) -- the same lesson the misc2 batch (this round) independently re-learned for `396a`/`108`.
2. The prefix/suffix dual-directory-naming trap accounted for 19 of this batch's 28 nominal run_ids -- the single largest source of apparent-but-not-real "new" targets across this round.
3. A blanket per-run `substrate_ceiling` stamp across co-tagged claims (the f-dominance-conversion-cluster file's MECH-258 miscount) is exactly the hazard `recommended_epistemic_category_per_claim` exists to prevent -- worth a governance sweep for other instances of the same shortcut.
