# Failure Autopsy: V3-EXQ-924 (claim-free diagnostic PASS, E3 score-variance decomp post-SD-E3-SCORER-COMPLETION)

Generated: `2026-08-12T06:36:36Z`
Status: CONFIRMED (user-adjudicated at Step 8 gate, 2026-08-12)

## 1. Facts reconstruction

**Dry-run gate**: `check_dry_run_citations.py` on both run_ids in this autopsy — 0 dry cited, 2 clean. Not a smoke.

**Run**: `v3_exq_924_e3_score_variance_decomp_scorer_fix_remeasure_20260812T051115Z_v3`, queue_id `V3-EXQ-924`, `experiment_purpose: diagnostic`, `claim_ids: []` (by design — matches the V3-EXQ-571/609/858 precedent for this instrumentation family), `outcome: PASS`. `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` all present — Experimental Recording Standard always-core complete.

**Why this run exists** (per the script docstring, session `mech357-pressure-scoping-11e9c9`, F-dominance causal-localisation scoping): every existing MECH-439/ARC-062 F-dominance measurement (V3-EXQ-571 and its many descendants: 689d, 689i, 699/699b, 705b, 707*, 709/711/713, 719a, 852, 858) ran **before** commit `193bbec` (SD-E3-SCORER-COMPLETION, 2026-08-09). Verified directly against that commit's diff: prior to it, `compute_reality_cost()` and `compute_harm_cost_fallback()` unconditionally subtracted the output of two untrained `nn.Sequential` heads (touched by no loss anywhere in `ree_core`) — pure random-init noise added into literal F and the harm-fallback term on the live selection path, in every run in that lineage, with no flag to disable it (the flag did not exist before this commit). So no prior F-dominance figure reflects the literal F that exists today. This run answers, cheaply, whether that matters before the larger frozen-state/frozen-candidate causal-replay diagnostic (V3-EXQ-925, already queued/claimed by the same session) is built.

**Design**: reuses V3-EXQ-571's exact `temporal_fraction` formula (var(component)/var(sum-of-components), for direct numeric comparability to the historical 88–89% figure) plus V3-EXQ-609's per-candidate inter-candidate-spread state classification. New vs. both predecessors: a `scorer_state` dimension — every (arm, seed) cell runs BOTH `fixed` (`e3_include_untrained_fallback_scorers=False`, current default/live path) and `legacy` (`=True`, bit-identical reproduction of pre-2026-08-09 behaviour per the fix commit's own docstring), so the delta the fix makes is measured **within the same run, on the same substrate revision** — not inferred by comparing against a stale historical manifest with no `substrate_hash`. 2 arms (`ARM_0_baseline`, `ARM_1_diversity_stack`) x 2 scorer states x 3 seeds = 12 cells, no training (frozen random-init weights, fixed policy stepping the env — architectural instrumentation, not a behavioural/learning experiment).

**GOV-REUSE-1 check** (performed before authoring, per script docstring): only V3-EXQ-571's own two manifests carry a comparable readout, both unverifiable (no recoverable `substrate_hash` — predate the 2026-07-12 recording standard). Not reusable; this run was necessary.

**Sample-size integrity** (`outcome_note`): E3 fires only every `heartbeat.e3_steps_per_tick` env steps (default 10) and its decomposition latches between fires — confirmed empirically during authoring (bit-identical across 7 consecutive calls before changing). Of `N_STEPS=600` env steps per cell, the script explicitly separates 918 genuine fresh E3 selections from 6282 latched (non-fresh) ticks that were correctly skipped, across all 12 cells combined. This is the load-bearing sample-size-integrity safeguard this family of experiments needs (per `CLAUDE.md` "Sample-size integrity" and V3-EXQ-571's own root-cause doc, which found the original mean-collapsed metric structurally blind to per-candidate signal).

**Headline result** (`scorer_fix_deltas`):

| Arm | `temporal_fraction[f]` fixed | legacy | delta (fixed − legacy) |
|---|---|---|---|
| ARM_0_baseline | 0.9610 | 0.8815 | **+0.0795** |
| ARM_1_diversity_stack | 0.9604 | 0.8950 | **+0.0654** |

`non_degenerate: true`, `degenerate_metrics: {}` for the run overall.

**PASS bar**: "decomp data collected in every one of the 2 arms x 2 scorer states" — a measurement-completeness check, not a hypothesis-test threshold. The script's own docstring states this explicitly ("this is a measurement run, not a hypothesis test with a pass/fail bar"). No `interpretation` block, no `preconditions[]`, no `criteria[]` in the manifest — this run genuinely has no adjudicable gate to check for vacuousness in the sense the indexer's `precondition_unmet`/`vacuous_pass` flags cover; what this autopsy owes is confirming the *measurement itself* (not a pass/fail bar) is trustworthy.

## 2. Claim-layer mapping

`claim_ids: []` by design (matches V3-EXQ-571/609/858 precedent for this instrumentation family) — no claim to map. This run is scoping/calibration for the not-yet-run V3-EXQ-925 frozen-replay causal harness, which is itself the discriminating experiment for the pre-registered `H-f-dominance` hypothesis in `hypothesis_space_registry.v1.json`'s `conversion_ceiling_root` question (currently `alive`, `adjudicating_runs: ["V3-EXQ-737"]`). V3-EXQ-924 does not resolve that hypothesis — it measures whether a scorer bug matters before the causal harness is built, it does not causally manipulate F.

## 3. Biological-reference triage

Not applicable — this is instrumentation of an artificial selection algorithm's internal score decomposition (E3's temporal-fraction variance split), not a claim about a biological mechanism.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free diagnostic) | — |
| Biological reference | n/a | Architectural instrumentation, not a biology-fidelity question. |
| Prerequisites | present | SD-E3-SCORER-COMPLETION (`193bbec`) landed 2026-08-09; both scorer states (fixed/legacy) reproduce documented, verified behaviour per the fix commit's own docstring. |
| Implementation completeness | complete | Reuses validated 571/609 formulas verbatim; explicit fresh-selection-only sample-size safeguard (918 genuine vs 6282 latched, correctly separated). |
| Environment adequacy | adequate | Same `CausalGridWorld`, 8x8 grid, 1 hazard, matching predecessors. |
| Measurement adequacy | adequate | `non_degenerate: true`, `degenerate_metrics: {}`; GOV-REUSE-1 checked first (no reusable prior fingerprint — this run genuinely necessary); within-run fixed-vs-legacy comparison on the same substrate revision avoids the historical cross-revision confound. |
| Integration adequacy | coupled | Both scorer states measured in the same run, same seeds, same substrate_hash — isolates the fix's effect from arm/seed noise cleanly. |
| Scale/capacity | adequate | 3 seeds x 2 arms x 2 scorer states, ~918 genuine fresh E3 selections total — consistent with 571/609's own sampling design. |

**Failure-location / vacuous-pass check**: this run has no organism-level "REE failed/succeeded" narrative to gate (GOV-FAILLOC-1's buckets do not apply — there is no claim, no pass/fail hypothesis bar). The relevant question this skill's diagnostic-PASS trigger exists for is narrower: **is the PASS vacuous?** No — the PASS criterion (data collected in all cells) is trivially satisfiable by construction *only if the run completes without crashing and returns non-empty decomp*; what makes the underlying measurement non-vacuous is the independently-checked `non_degenerate: true` / `degenerate_metrics: {}` plus the explicit fresh-vs-latched sample-size safeguard, not the PASS bar itself. Confirmed non-vacuous.

## 5. Learning extracted

1. **Removing the untrained-scorer noise INCREASES literal F's measured share of E3 temporal score variance**, it does not decrease or explain it away: ARM_0 0.961 (fixed) vs 0.881 (legacy), Δ=+0.080; ARM_1 0.960 vs 0.895, Δ=+0.065.
2. **The historical 88–89% F-dominance figure (V3-EXQ-571, pre-fix) was, if anything, an underestimate** of F's dominance under the scorer that is actually live today — the untrained-scorer noise was diluting F's apparent share, not inflating it.
3. This rules out one candidate confound for the ongoing F-dominance causal-localization work: the scorer bug is not the explanation for why F appears to dominate E3 selection variance; whatever is driving F-dominance, it is not an artifact the 2026-08-09 fix resolves.
4. Directly informs V3-EXQ-925 (frozen-replay causal harness, already queued and claimed by session `mech357-pressure-scoping-11e9c9`) — that harness can proceed on the corrected (`fixed`) scorer state with confidence the pre-fix noise is not confounding its baseline.

## 6. Repair pathway

No repair owed — this is a clean, informative measurement run, not a failure. **Routing: none / context for V3-EXQ-925.** No `claims.yaml` action (claim-free by design). No substrate gap identified (`recommended_substrate_queue_entry.action = "none"` — the substrate fix this run measures is already landed; nothing further to build here).

User confirmed at Step 8: **PASS is genuine, no claim-layer action** — declined the additional option of retroactively flagging every pre-`193bbec` F-dominance-adjacent run with a conservative-estimate caveat; that remains available as a follow-up note for whichever session/governance cycle next touches those runs, but is not actioned by this autopsy.

## 7. Draft evidence_quality_note

Not applicable — `claim_ids: []`, nothing for governance to write to `claims.yaml`.
