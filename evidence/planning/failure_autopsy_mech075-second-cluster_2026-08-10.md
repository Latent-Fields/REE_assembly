# Failure Autopsy — MECH-075 second cluster (V3-EXQ-903a, V3-EXQ-905a)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** cluster
**Status:** confirmed (interactive gate run 2026-08-10)

## 1. Facts

Both runs are the recalibrated successors of the runs adjudicated in `failure_autopsy_mech075-vta-lc-cluster_2026-08-09` (confirmed). Neither is in the live queue (both FAIL, removed on completion per queue convention). Both pass `validate_recording.py` cleanly (0 always-core gaps), neither is a dry run.

### V3-EXQ-903a (ventral/VTA-RPE leg)
`v3_exq_903a_mech075_ventral_vta_rpe_probe_20260809T160911Z_v3`, `claim_ids: [MECH-075]`, `supersedes: v3_exq_903_...`. Recalibration vs 903: seeds 3→5 `[42,7,123,5,17]`, majority 2/3→3/5, POSCTRL episodes 5→10, added per-seed episode-length/termination-cause recording.

Result: **still fails the readiness gate on majority.** P0a (grounding-corr floor 0.15): seeds 42 (0.5314) and 7 (0.5179) pass; seeds 123 (0.0452), 5 (-0.0034), 17 (0.1103) fail. 2/5 < majority (3). `n_c1_pass=4/5` (manipulation check clears), `n_c2_pass=1/5` (basin narrowing). Self-route: `substrate_not_ready_requeue`, FAIL, `evidence_direction: inconclusive`.

### V3-EXQ-905a (dorsal/LC-arousal leg)
`v3_exq_905a_mech075_dorsal_lc_arousal_probe_20260809T130730Z_v3`, `claim_ids: [MECH-075]`, `supersedes: v3_exq_905_...`. Recalibration vs 905: `LC_GAIN` re-derived 2.0→80.0 (from observed V3-EXQ-905 eval-phase `arousal_ema` distribution, target `mode_scale≈1.2`).

Result: P0 PASSES (arousal_ema 0.0043, 4.3x floor). C1 (manipulation check) PASSES 3/3 — mean|delta_t| clears the floor cleanly, confirming the re-derived gain produces a genuinely differential signal this time. C2 (basin_width widening, load-bearing) **FAILS 0/3**: per-seed gaps `[-0.0, +0.0, +2.6e-5]` against basin widths of ~0.0133-0.0151 — GATED and ABLATED basin_width are identical to 4+ decimal places in 2/3 seeds. Self-route: `dorsal_lc_arousal_no_attractor_widening`, FAIL, `evidence_direction: weakens`.

## 2. Claim-layer mapping

MECH-075 (`docs/claims/claims.yaml`): "Basal ganglia perform dopaminergic gain/threshold setting on hippocampal attractor dynamics." Status `candidate`, `epistemic_category: standard`, `depends_on: [Q-019, ARC-021, MECH-043, MECH-073]`. No claims.yaml sub-ids exist for dorsal/ventral — both legs live inside one claim's `what_would_answer` bifurcation. `evidence_quality_note` currently ends at the 2026-08-09 governance note covering the PREDECESSOR (unlettered) 903/905 runs; not yet updated for 903a/905a.

## 3. Biological-reference triage

**Ventral (903a):** VTA-RPE grounding of valuation, per Duszkiewicz et al. 2018 (conf 0.70). Clear reference; the finding concerns training reliability, not a biology divergence.

**Dorsal (905a):** LC-arousal gain modulation, citing Kempadoo 2016, Galvez-Marquez 2022 (conf 0.78-0.80), Lemon & Manahan-Vaughan 2006 (conf 0.82). The predecessor cluster autopsy already flagged a construct-validity gap here: this literature grounds LC-arousal in *plasticity-timescale* effects (a learning-rate/consolidation construct), not a *decision-time* CEM-candidate-spread construct. 905a's result — a clean differential manipulation (C1) with zero effect on the decision-time geometry metric (C2) — is independent corroboration of exactly that mismatch: the manipulation does something, it just doesn't touch what C2 measures.

## 4. Four-layer diagnosis

### V3-EXQ-903a (ventral)
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | test still can't run fairly — readiness gate fails on majority |
| Biological reference | clear | Duszkiewicz 2018 |
| Prerequisites | **missing** | grounding correlation swings +0.53 to -0.003 across seeds with identical config |
| Implementation | partial | valuation-head grounding to reward doesn't reliably converge across seeds |
| Environment | unclear | can't rule out env-driven variance vs training instability without a dedicated probe |
| Measurement | adequate now | recording fixed, seeds/POSCTRL increased |
| Integration | isolated/immature | |
| Scale/capacity | possibly insufficient | only 20 P0 episodes for readiness measurement |

### V3-EXQ-905a (dorsal)
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (narrow) | fair test of the decision-time operationalization specifically |
| Biological reference | partial — construct-validity gap | LC-arousal literature grounds plasticity-timescale, not decision-time, effects |
| Prerequisites | present | P0 4.3x floor |
| Implementation | complete, correctly calibrated | LC_GAIN properly re-derived this time; C1 confirms differential signal |
| Environment | adequate | |
| Measurement | adequate | |
| Integration | coupled, stable | |
| Scale/capacity | adequate | |

**Failure-location (GOV-FAILLOC-1):** neither leg reaches REE FAILED. 903a: Implementation not complete (prerequisites missing) — not established. 905a: Implementation reads complete, but Biological reference reads only `partial` (construct-validity gap) — MECHANISM FAILED is not cleanly established either; net reading is "weakens the specific operationalization, flags a construct mismatch."

## 5. Two distinct findings, not one structural property

This is not a single cluster-level pattern the way the 2026-08-09 cluster was (both prior runs shared "an inherited, unrederived gain constant"). Here:
- **903a** is a training-reliability/prerequisites problem (readiness gate unstable across seeds).
- **905a** is a construct-validity problem (manipulation confirmed real, decisive metric doesn't move) with a correctly-calibrated manipulation.

They are reported together only because they share the claim and the CEM-noise-scale-via-gain mechanism family (MECH-267); each routes differently.

## 6. Routing (confirmed at interactive gate)

**903a:** User-confirmed disposition — route to a **diagnostic spike** (`/queue-experiment`, `experiment_purpose: diagnostic`) logging per-episode valuation-head training trajectory (grounding correlation over P0 episodes, per seed) rather than a third combined readiness+main-criteria attempt. Two attempts at "more seeds" have not closed the gate; the open question is WHY grounding is seed-dependent. `epistemic_category: standard`, `evidence_direction: inconclusive`, `recommended_substrate_queue_entry.action: none` (diagnostic needed before any substrate action is warranted). Cross-reference: this run shows the same "reliable in some seeds, ~0/negative in others" shape independently observed in V3-EXQ-324d (SD-020) this same session — flagged as a possible cross-cutting training-instability pattern in newly-trained PE/valuation heads, worth a shared root-cause investigation across both claims if the diagnostic confirms instability rather than a ventral-specific issue.

**905a:** User-confirmed disposition — `evidence_direction: weakens` for the CEM-decision-time operationalization specifically (not MECH-075's dorsal leg broadly). Route to `/lit-pull`, targeted review checking whether LC-NE arousal's literature role is decision-time (as currently operationalized) or plasticity/consolidation-timescale (which would mean the current construct is a genuine mismatch, requiring a re-operationalization rather than further gain-tuning). `epistemic_category: standard` (mapping `measurement_test_design_defect`-adjacent construct-validity language to the valid enum per the vocab audit). `recommended_substrate_queue_entry.action: none` pending the lit-pull outcome.

**Draft evidence_quality_note (both legs, verbatim for governance):**
> [2026-08-10 governance, V3-EXQ-903a+905a, confirmed failure_autopsy_mech075-second-cluster_2026-08-10]: V3-EXQ-903a (ventral, recalibrated 5 seeds/majority 3): readiness gate STILL fails on majority (2/5, grounding corr swings +0.53 to -0.003 across seeds) — self-routed substrate_not_ready_requeue, CONFIRMED correct. Second consecutive attempt at "more seeds" has not closed the gate; routed to a targeted diagnostic (per-episode training-trajectory logging) rather than a third combined attempt. V3-EXQ-905a (dorsal, LC_GAIN correctly re-derived 2.0->80.0): manipulation now clearly differential (C1 3/3) but the decisive metric (basin_width) shows literally zero effect (2/3 seeds identical to 4+ decimals) — weakens the CEM-decision-time operationalization specifically; flags a construct-validity gap (LC-arousal literature grounds plasticity-timescale effects, not decision-time). Routed to /lit-pull. epistemic_category standard for both. Status unchanged (candidate).

Step 9b: no existing hypothesis-space qid names MECH-075 (confirmed by predecessor autopsy); no `fanout_recommendation` emitted. Registration deferred.
