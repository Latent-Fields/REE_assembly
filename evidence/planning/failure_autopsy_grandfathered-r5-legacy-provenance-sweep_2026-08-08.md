# Failure Autopsy: Round-5 legacy/archived-provenance sweep (MECH-058/059/060/056, Q-008/009, V2 singletons), 53 targets

**Generated:** 2026-08-08T19:37:15Z
**Scope:** cluster (round-5 grandfathered-backlog sweep, provenance theme)
**Status:** confirmed (Step 8: user confirmed excluding MECH-058's 13 archived-repo runs from evidentiary weight)

## Overview

Across round 5's five parallel batches (228 remaining grandfathered run_ids), roughly 60 run_ids collapsed to one structural pattern: legacy evidence generated before, or against, substrate the project has since archived or superseded. This file consolidates all of them.

## MECH-058 (16 targets: 3 genuine, 13 synthetic-scaffolding)

MECH-058 is `status: retired`, `superseded_by: MECH-069`. Its own claims.yaml note already narrates the 3 genuine-substrate runs verbatim (V1 EXQ-002/`claim_probe_mech_058`, V2 EXQ-019/`e1_e2_terrain_timescale_v2`, V3 EXQ-019/`v3_exq_019_timescale_v3`): "Both FAILs consistent with supersession: the test was ill-posed. LR separation != functional domain separation." All three formalized as `test_design_defect`, `governance-note-only`, no re-queue (claim is retired; MECH-069 is the live thread).

The remaining 13 (6 `bridge_v2_mech_058_anchor_drift_extreme_shift_*`, 2 `mech_058_oscillatory_shift_anchor_decay_*`, 2 `mech_058_shift_spike_replay_pressure_*`, 3 `exp_00{02,13,15}_*`) all carry `source_repo.name: "ree-experiments-lab"` — the repo CLAUDE.md marks **ARCHIVED, "synthetic scaffolding only, do not use."** `evidence_class: "exploratory_simulation"`; the `exp_00NN` summaries literally read "Synthetic exploratory simulation run generated from proposal metadata." **Step 8 (user-confirmed, recommended option): exclude all 13 from evidentiary weight** — reclassify `non_contributory` rather than the currently-recorded `weakens`, matching the project's own archived-repo convention.

## MECH-059 (13 targets: 1 genuine, 12 archived) and MECH-056 (3 targets: 1 genuine, 2 archived)

Same shape as MECH-058's second sub-cluster. MECH-059's one genuine ree-v1-minimal run (`claim_probe_mech_059`, FAIL, mixed) is formalized as-is (status=active, 0 prior substrate_ceiling stampings — no brake concern). The remaining 12 (6 `bridge_v2_mech_059_adversarial_uncertainty_gaming_*`, 2 `exp_00{14,17}_*`, 2 `mech_059_ambiguity_fog_dispersion_*`, 2 `mech_059_ood_noise_burst_ensemble_*`) are ree-experiments-lab archived — `non_contributory`, excluded from weight. MECH-056's genuine `claim_probe_mech_056` run (status=provisional) is formalized; its two `exp_00{04,11}_*` siblings are archived — `non_contributory`.

## Q-008 and Q-009 legacy singletons

`exp_0015_20260216T150514802604Z` (Q-008, already `status: legacy`) and `exp_0015_20260217T180028221014Z` (Q-009, currently `weakens`) are both ree-experiments-lab archived-repo runs. Recommend `non_contributory` for both — Q-009's is a live correction (currently scored as real weakening evidence for an unarchived claim despite the manifest's own summary literally describing itself as synthetic).

## MECH-060 (14 targets, one structural non-event)

All 14 (6 `bridge_v2_mech_060_cross_channel_contamination_stress_*`, 4 `exp_00{03,15,19,21}_*`, 2 `mech_060_leakage_prompt_injection_*`, 2 `mech_060_memory_patch_cross_talk_*`) share `source_repo: "ree-experiments-lab"`, `runner.name: "ad-hoc-stress-generator"`, `commit: "uncommitted"`. MECH-060's own claims.yaml note already fully explains this: "Prior 137 synthetic runs (ree-v2/ree-experiments-lab, archived 2026-02-26) are invalid... Genuine ree-v1-minimal experiment completed 2026-02-27 (EVB-0043, EXQ-005): PASS... counted support is `20260314T235933_write_locus_contamination_v2`." Recommend `evidence_direction: superseded` (not the currently-recorded `weakens`) for all 14, matching the claim's own stated convention. `governance-note-only`, no re-queue.

## Legacy ree-v2/v1-minimal singletons (6)

- `20260227T085822_claim_probe_mech_060_ree_v1_minimal` (MECH-060, MECH-067): underpowered 1-seed/5-episode pilot, superseded 15 minutes later same day by a 3-seed/200-episode PASS (the run claims.yaml actually cites).
- `20260315T125844_rollout_viability_mapping_v2` (ARC-018): V2 conceptual-framing failure, ARC-018's own note documents this exact experiment class as "a conceptual failure of the original claim framing, not a substrate or tuning issue" — superseded by V3 EXQ-042/EXQ-053 PASSes. Recommend `evidence_direction: superseded` to match ARC-018's own convention.
- `20260315T183757_causal_attribution_calibration_v2` (MECH-071): **explicitly unresolved** — no supersession language exists in MECH-071's note for this specific V2 run (unlike ARC-018's parallel case). Flagged for governance to decide whether the blanket V2-supersession convention applies or whether V2 causal-attribution methodology needs separate review.
- `20260308T114644_path_memory_ablation_v2` (ARC-007, SD-004): manifest's own note already explains this as pre-SD-004 (HippocampalModule unbuilt), superseded by V3-EXQ-114 PASS (99.2% harm reduction), already excluded from scoring.
- `20260315T205715_selective_residue_attribution_v2` (MECH-072): pre-SD-005-split legacy predecessor of the already-covered V3 MECH-072 lineage's world-delta-gating defect (bit-identical metrics to that lineage's signature).

## Biological-reference triage

Not the governing layer for this file — every item resolves at the provenance/supersession layer, not the biology layer. Where biology is cited (MECH-058/059/060's underlying mechanisms), it is already established elsewhere and untouched by this sweep.

## Re-derive brake state

No target in this file recommends `substrate_ceiling`. **The brake does not fire anywhere in this file.**

## Recommended routing summary

All 53 targets: `governance-note-only`. No re-queue recommended anywhere — every item is either an archived-repo exclusion, a supersession-chain formalization, or (one case, MECH-071's V2 run) an explicit unresolved flag for governance judgment.

## Learning extracted

1. Repository provenance (archived vs. active) is itself a load-bearing epistemic signal this backlog sweep had not previously applied systematically — MECH-058 and MECH-060 alone account for 27 of this file's 53 targets, both cleanly resolved by checking `source_repo.name` against CLAUDE.md's repo map.
2. The "reviewed FAIL, never formally autopsied" backlog trigger does not distinguish real substrate evidence from synthetic scaffolding — a useful refinement for future sweeps would be to pre-filter by `source_repo` before dispatching research agents, since roughly a quarter of this round's total volume resolved to the same one-line disposition.
3. One genuine unresolved item survived disciplined checking (MECH-071's V2 causal-attribution run) — worth noting that not every V2-era run automatically inherits the same supersession convention; each claim's own note needs checking individually.
