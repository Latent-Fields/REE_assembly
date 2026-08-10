# Failure Autopsy — V3-EXQ-324d (SD-020)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-10)

## 1. Facts

`v3_exq_324d_sd020_harm_surprise_pe_real_flagpath_20260809T171606Z_v3`, `claim_ids: [SD-020]`, `supersedes: v3_exq_324b_...`. Run: 15012s (~4.2h), `DLAPTOP-5.local` (darwin-arm64, torch2.12.0), 5 seeds `[0,1,2,3,4]`. `validate_recording.py`: 0 always-core gaps, not a dry run.

Governance-commissioned (GFLAG-0005, resolved 2026-08-09T06:24:07Z) after SD-020's promoting run (V3-EXQ-324b) was found to be a standalone bench reimplementation with zero references to `REEAgent`/`harm_surprise_pe_enabled`/`compute_harm_accum_loss` — never the shipped flag path. This run trains `z_harm_a` through the actual shipped loss `agent.compute_harm_accum_loss(accum, latent)` under `harm_surprise_pe_enabled=True`, on the SD-022 `limb_damage_enabled=True` substrate (chosen to fix 324's underpowering — `min_harm_events=344` here vs 10-20 in 324).

**Non-degeneracy gates (all pass cleanly):** `pe_differentiated=1.0` (ARM_OFF ema exactly 0, ARM_ON ema>floor — proves the PE branch fired), `well_powered=1.0` (344+ events/seed, floor 100), `dv_measurable=1.0` (hap_std>floor all ON cells), `manip_had_effect=1.0` (max delta 0.063 ≥ 0.02 epsilon).

**Per-seed result** (need ≥3/5 for PASS): seed 0 (C1 false, C2 false), seed 1 (C1 false, C2 false), seed 2 (C1 true, C2 false), **seed 3 (C1 true, C2 true — only seed passing all three)**, seed 4 (C1 false, C2 false). 1/5 pass. `hap_surprise_corr` per ARM_ON seed: -0.073, -0.134, -0.126, **+0.608**, -0.012 — four seeds cluster near-zero-to-negative, one seed strongly positive.

Self-route: `sd020_real_flagpath_not_supported`, FAIL, `evidence_direction: does_not_support` (as filed).

## 2. Claim-layer mapping

SD-020 (`docs/claims/claims.yaml`): "z_harm_a encodes affective surprise (precision-weighted PE), not raw accumulated harm state." `status: candidate` (already demoted from `stable` via GFLAG-0005), `literature_confidence: 0.915`, `depends_on: [SD-011, SD-019, ARC-016]`. `evidence_quality_note` chronology ends at the 2026-08-09 GFLAG-0005 demotion note, which explicitly states "a genuine test of the real flag path... is owed before any re-promotion." This run IS that owed test.

## 3. Biological-reference triage

Chen 2023 (Front Neural Circuits, anterior insula cortex PE coding) plus 3 other literature entries; `literature_confidence: 0.915` — well-grounded. No biology divergence identified; this is a training/mechanism-reliability question, not an implementation-vs-literature mismatch.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact — first fair test | all non-degeneracy gates clean; this is the genuine test GFLAG-0005 asked for |
| Biological reference | clear | Chen 2023, lit_conf 0.915 |
| Prerequisites | present | |
| Implementation | complete | shipped `compute_harm_accum_loss` under the real flag |
| Environment | adequate | SD-022 substrate fixed the prior underpowering |
| Measurement | adequate | head-readout DV (harm_accum_pred surprise-vs-magnitude preference), not saturation-masked |
| Integration | coupled, non-degenerate | manipulation confirmed to have real effect (max delta 0.063) |
| Scale/capacity | adequate | 344+ harm events/seed |

**Failure-location (GOV-FAILLOC-1):** Implementation, Measurement, and Environment all read adequate/complete — this is the case where REE FAILED *could* be reached on the strict four-layer criteria alone. But the single strong-outlier seed (3, corr +0.608 — 6-10x the magnitude of the other four seeds, correctly signed) is a genuine ambiguity the four-layer table doesn't resolve: is this seed-to-seed training-stability variance in whether the surprise-signal reliably trains, or is it noise around a true null?

## 5. Learning extracted

- First fair, well-powered test of the real shipped implementation: 4/5 seeds show near-zero-or-negative surprise correlation, 1/5 shows a strong positive result.
- All non-degeneracy/manipulation-check gates pass cleanly — this is not a design-defect result.
- The 4-near-null/1-strong-outlier seed shape echoes the same pattern independently observed in V3-EXQ-903a (MECH-075 ventral leg, this same session): reliable signal in some seeds, near-zero-or-negative in others, under an identical config.

## 6. Routing (confirmed at interactive gate)

**User-confirmed disposition:** `non_contributory`, flagging the training-instability pattern rather than treating this as a clean falsification. The single strong outlier (seed 3) leaves genuine seed-variance ambiguity unresolved — this echoes V3-EXQ-903a's shape closely enough that both should be read together as a possible cross-cutting pattern in newly-trained PE/valuation heads before either is trusted as informative.

`epistemic_category: standard` (unchanged — this doesn't assert a substrate gate, it asserts the result isn't yet fully interpretable). `recommended_substrate_queue_entry.action: none`. Status recommendation: SD-020 stays `candidate` (already demoted; this result doesn't itself argue for further downgrade given the flagged ambiguity, but it also does NOT support re-promotion).

**Cross-reference to governance:** consider whether a shared root-cause diagnostic — logging per-seed training trajectories for both the MECH-075 ventral valuation head and SD-020's surprise-PE head — would resolve both open questions at once, since both show the identical "reliable in a minority of seeds, ~0/negative in the rest" shape under otherwise-clean, well-powered, non-degenerate tests.

**Draft evidence_quality_note for governance:**
> [2026-08-10 governance, V3-EXQ-324d, confirmed failure_autopsy_V3-EXQ-324d_2026-08-10]: the genuine real-flag-path test GFLAG-0005 asked for has now run -- all non-degeneracy gates clean (344+ harm events/seed, manipulation confirmed real, DV not saturation-masked). 1/5 seeds pass all three criteria; the other 4 show near-zero-or-negative surprise correlation (-0.07 to -0.13) against one strong positive outlier (seed 3, +0.61). Reclassified non_contributory rather than does_not_support: the seed-variance shape closely echoes V3-EXQ-903a (MECH-075 ventral, a different claim) under otherwise clean, well-powered conditions -- flagged as a possible cross-cutting training-instability pattern in newly-trained PE/valuation heads, worth a shared diagnostic before either result is trusted as informative. Status unchanged (candidate) -- neither re-promoted nor further downgraded pending that diagnostic.

Step 9b: SD-020 does not appear in any existing hypothesis-space qid; no `fanout_recommendation` emitted. Registration deferred.
