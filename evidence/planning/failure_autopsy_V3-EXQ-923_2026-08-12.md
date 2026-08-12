# Failure Autopsy: V3-EXQ-923 (MECH-267, GOV-FANOUT-1 H1 iteration-count leg)

Generated: `2026-08-12T06:36:36Z`
Status: CONFIRMED (user-adjudicated at Step 8 gate, 2026-08-12)

## 1. Facts reconstruction

**Dry-run gate**: `check_dry_run_citations.py` on both run_ids in this autopsy — 0 dry cited, 2 clean. Neither target is a smoke.

**Run**: `v3_exq_923_mech267_gov_fanout1_h1_iteration_count_20260812T045513Z_v3`, queue_id `V3-EXQ-923`, `experiment_purpose: diagnostic`, `claim_ids: [MECH-267]`, `outcome: FAIL`, `evidence_direction: non_contributory` (diagnostic — always non_contributory regardless of which way the discrimination resolves). 30 seeds. `substrate_hash`, `config`, `seeds`, `machine`/`machine_class`, `elapsed_seconds` all present — Experimental Recording Standard always-core is complete, no recording gap.

**Why this run exists**: it is the H1 leg of a 3-leg GOV-FANOUT-1 discrimination portfolio opened by the confirmed `failure_autopsy_V3-EXQ-869a_2026-08-03` after V3-EXQ-869 (noise-scale mechanism only) and V3-EXQ-869a (noise-scale + horizon-depth) both found the same signature: mode-conditioned CEM proposal content is clean at `num_cem_iterations=1` (manipulation check, C0) and washed out at the production default `num_cem_iterations=3` (C1). 869a's fanout_recommendation named three untested loci — H1 (iteration count), H2 (mode-aware CEM value-function term, needs a substrate build), H3 (hard-partitioned candidate pools, needs a substrate build) — and explicitly authorized this fan-out rather than a fourth sequential letter (re-derive brake note: "AT the RE_DERIVE_BRAKE_THRESHOLD default of 2 [869, 869a]... explicitly NOT a bar to this run").

**Script** (`ree-v3/experiments/v3_exq_923_mech267_gov_fanout1_h1_iteration_count.py`): identical HippocampalModule/HippocampalConfig construction, 30-seed policy, modes-in-predicted-order, primary DV (`mean_raw_std_by_dim`), and both pairwise-gap floors (`FLOOR_DIAGNOSTIC=0.015`, `FLOOR_PRODUCTION=0.01`) to 869/869a. The only change: a third condition, `num_cem_iterations=2`, inserted between the existing iters=1 and iters=3 conditions. Design: 3 (iteration-count) x 4 (mode) x 30 (seed). H1's own pre-registered null (869a's `suggested_probes[0]`): "gaps at iters=2 are as flat as iters=3."

**Blocker/re-derive-brake checks performed by the script author before queuing** (both documented in the script docstring, confirmed by direct source read): `num_cem_iterations` is a plain int consumed by `for _iteration in range(self.config.num_cem_iterations)` (`ree_core/hippocampal/module.py:1899`) with no special-casing of 1 or 3 — no substrate blocker. Re-derive brake: not fired against this leg (a discrimination diagnostic on a different design axis than either braked run is the explicit carve-out, per 869a's own routing).

**Result**:

| Criterion | Gaps (planning-task, task-replay, replay-consolidation) | Floor | Passed |
|---|---|---|---|
| C_mechanism_activation_check | both `noise_scale_active` and `horizon_scale_active` true, `effective_horizon` varies by mode {2,3,4} | — | yes |
| C0 (manipulation check, iters=1) | 0.0546 / 0.0918 / 0.0311 | 0.015 (lower) | yes — reproduces 869/869a's clean C0 |
| **C_H1 (load-bearing, iters=2)** | **-0.0028 / 0.0023 / ~0.000006** | **0.01 (lower)** | **NO — H1's own null met** |
| C1 (context, iters=3) | 0.0008 / 0.0024 / -0.0037 | 0.01 (lower) | no — reproduces 869a's iters=3 reading almost exactly |
| C2 (secondary, non-gating) | 2/30 seeds full ordering at iters=2 | — | context only |

Outcome: `FAIL` (H1's own criterion did not clear), `interpretation.label = h1_refuted_gaps_at_iters2_as_flat_as_iters3`. `criteria_non_degenerate` is `true` for every criterion — the C_H1 near-zero gaps are not a degenerate/empty reading, they are the substantive finding.

## 2. Claim-layer mapping

MECH-267 (mode-conditioned hippocampal trajectory proposals — `HippocampalModule.propose_trajectories` must condition on `operating_mode`) — status `provisional`, `implementation_phase: v3`, `pending_retest_after_substrate: true`. This diagnostic is a **context tag only**: `experiment_purpose=diagnostic` excludes it from governance confidence/conflict scoring, and it does not test whether mode-conditioning exists (869/869a's own manipulation checks and this run's C0/mechanism-activation confirm it does, at iters=1) — it discriminates BETWEEN causal explanations for an already-established production-settings wash-out. **Claim alignment: intact.** The test let the discrimination express itself fairly (identical seeds/DV/floors to the priors it is directly comparable against; both upstream mechanisms confirmed active at runtime, not just per config).

## 3. Biological-reference triage

Inherited from 869/869a, not re-litigated here: mode-conditioned hippocampal proposal generation (differentiated content for planning / task-execution / replay / consolidation) maps to state-dependent hippocampal replay content, well-supported in the literature those prior autopsies cite. That biology bears on WHETHER mode-conditioning should exist, which is not in question in this run — the open question here is purely a CEM elite-refit selection-algorithm implementation-locus question (does more or fewer refit passes change whether the algorithm preserves the content difference), which is a computational/architectural question, not a biological-fidelity one. No new lit-pull is owed by this leg.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | Context tag only; diagnostic discriminates causal loci, does not adjudicate MECH-267 itself. |
| Biological reference | clear (inherited) | Mode-differentiated hippocampal content is biologically grounded; not re-tested here. |
| Developmental/dependency prerequisites | present | Both `mode_noise_scale` and `mode_horizon_scale` confirmed active at runtime via `mechanism_activation` (identical instrumentation to 869a). |
| Implementation completeness | complete | `num_cem_iterations=2` exercises the exact same code path as 1/3 (`module.py:1899`); no missing code, no special-casing, confirmed by source read pre-authoring. |
| Environment adequacy | adequate | Identical construction to 869/869a, already validated adequate for this question. |
| Measurement adequacy | adequate | Identical DV and floors to 869/869a; C0 clears cleanly (0.031–0.092 vs 0.015 floor), confirming instrument sensitivity; C_H1 gaps are ~0, an order of magnitude below the 0.01 floor — not a marginal/borderline reading. |
| Integration adequacy | coupled but unstable | Differentiation present after 1 elite-refit pass, gone after 2, unchanged after 3 — content survives exactly one refit pass regardless of how many more follow. |
| Scale/capacity | adequate | 30 seeds, identical seed formula to 869/869a. |

**Failure-location summary (GOV-FAILLOC-1)**: Implementation, Measurement, and Environment each independently read complete/adequate — none is the confound. The wash-out at iters=2 is therefore attributable to the CEM elite-refit **mechanism itself** (its selection/refit procedure), not to a coding bug, a blind metric, or an inadequate test environment. Net classification: **MECHANISM FAILED** (localized to the CEM elite-refit selection procedure in `HippocampalModule`, not "REE failed" at the organism level — this is one sub-mechanism within one claim's implementation).

## 5. Learning extracted

1. **H1 (iteration-count) is refuted.** The wash-out is not a function of how many elite-refit passes run — it occurs by the second pass and does not worsen (or improve) with a third. This is a genuine, informative negative (not a wasted run): it rules out the cheapest possible fix (just run fewer CEM iterations in production) and narrows the live hypothesis space from 3 legs to 2.
2. **H-mech267-fewer-iters is eliminated** in the frozen pre-registration ledger (`mech267_content_persistence_cem_refit`).
3. **H2 (mode-aware CEM value-function term) and H3 (hard-partitioned candidate pools) remain the only live loci**, and both require a substrate build that does not exist in `ree_core` today.
4. Content differentiation survives exactly the first elite-refit pass and is gone by the second — consistent with the elite-refit's cross-mode pooling/averaging dominating quickly, which is suggestive (not dispositive) toward H3 (shared elite pools mixing across modes) over H2 (a missing scoring term), but this run does not discriminate between them — that is exactly what H2/H3 substrate builds would need to test.

## 6. Repair pathway

**Node classification**: `complicated (buildable)` — for whichever of H2/H3 the next session pursues, the fix is a named build (a new mode-dependent value-function term, or a hard-partitioned elite-refit path), not an open scientific question about what the right test is.

**Routing: `/implement-substrate`.** User-confirmed at Step 8: create a substrate_queue entry **unscoped between H2 and H3** — neither locus has been scoped for feasibility/cost yet, so a future session/governance cycle picks between them (or does both) rather than this autopsy pre-selecting one. `recommended_substrate_queue_entry.action = "create"` (see JSON).

**Re-derive brake**: does not fire on this target. MECH-267's ceiling-hit count under R1–R3 (substrate_ceiling only) is 0 — both 869 and 869a read `competence_implementation_gap`/`non_contributory`, not `substrate_ceiling`, and this target reads `standard` (a diagnostic discrimination leg, non-gating). The brake's own carve-out ("a diagnostic whose purpose is to discriminate WHY the ceiling holds... is not the re-derive loop") continues to apply, unchanged from 869a's analysis.

**No `fanout_recommendation` from this target** — H2 and H3 are already-existing legs of 869a's portfolio; no new portfolio is needed. The frozen ledger's `mech267_content_persistence_cem_refit` question already carries them as `alive` hypotheses.

## 7. Draft evidence_quality_note (not written — governance's call)

None recommended for `claims.yaml` MECH-267 — this is a diagnostic, non-gating, and the claim's own status/confidence is unaffected. If governance wants a pointer, suggested text: *"GOV-FANOUT-1 portfolio (opened by failure_autopsy_V3-EXQ-869a_2026-08-03) update: H1 (iteration-count) eliminated by V3-EXQ-923 (confirmed failure_autopsy_V3-EXQ-923_2026-08-12) — production-settings content wash-out is not iteration-count dependent. H2 (mode-aware scoring) and H3 (partitioned pools) remain the only live loci, both pending a substrate build."*
