# Failure Autopsy: V3-EXQ-869 (MECH-267, mode-conditioned hippocampal proposal content persistence)

**Generated:** 2026-08-02T10:14:48Z
**Run:** `v3_exq_869_mech267_mode_conditioning_content_persistence_20260802T035422Z_v3`
**Queue ID:** V3-EXQ-869
**Claim IDs:** MECH-267
**Status:** confirmed
**Supersedes:** none

## 1. Facts

**Design.** Well-powered (**30 seeds**), pre-registered decision rule stated up front in the manifest (`combination_rule`): the primary DV is FAIL/non_contributory only if the manipulation check itself is degenerate; else PASS/supports iff the mean pairwise raw_std gaps between mode-conditioned proposal distributions clear a floor at production settings (`num_cem_iterations=3`); else FAIL/weakens. Two gating criteria:

- **C0 (manipulation check, iters=1):** confirms the 462/465-established wiring finding reproduces at the *content* level (raw proposal distributions differ by mode before any CEM elite-refit). Mean gaps: internal_planning−external_task 0.0546, external_task−internal_replay 0.0918, internal_replay−offline_consolidation 0.0311 — all clear the 0.015 floor. **PASSED.**
- **C1 (production content persistence, iters=3):** same gaps measured after 3 CEM elite-refit iterations (matching realistic deployed settings). Mean gaps: −0.0003, +0.0035, −0.0037 — essentially flat, all below the 0.01 floor. **FAILED.**
- **C2 (non-gating, per-seed corroboration):** 0 of 30 seeds show the full predicted mode ordering.

**Outcome:** FAIL. `non_degenerate: True`. Label: `mode_conditioning_content_effect_washed_out_by_elite_refit`.

Confirmed non-dry via `check_dry_run_citations.py`.

## 2. This is a clean, well-powered, informative FAIL — but the implementation only covers half of what the claim asserts

MECH-267's own claim text states the `operating_mode` vector should bias proposal content along **at least two** axes: "(a) candidate set... (b) **horizon depth** (shallower in external_task, longer in internal_planning)... (c) tagging." The claim's `implementation_note` in claims.yaml is explicit that only one of these was actually built: *"HippocampalConfig... the CEM proposal std is scaled by... `mode_noise_scale`... Lit-pull recommendation (2026-04-27) suggested operating_mode modulate look-ahead horizon at proposal generation; the V3 implementation modulates CEM noise scale instead — different mechanism with similar effect (mode-conditional exploration breadth vs depth). V4 reconsideration could add explicit horizon modulation alongside the existing noise-scale mechanism."*

This is a self-acknowledged implementation gap dating to the mechanism's original build (2026-04-20), not something this autopsy is inferring after the fact. It matters directly for interpreting 869's result: **noise-scale modulation only changes the initial sampling spread of the CEM proposal distribution, not the structure of what states are reachable/considered.** CEM's elite-refit process iteratively resamples toward the highest-scoring candidates under a (mode-independent, per the current implementation) value function. If the value function used to select elites does not itself depend on mode, then with enough refit iterations the elite set converges toward the same mode-independent optimum regardless of the initial noise-scale — exactly the observed pattern (real difference at iters=1, washed out by iters=3). A horizon-depth mechanism (changing what trajectory lengths are even proposed, not just their sampling variance) would not be subject to the same washing-out dynamic, because it changes the candidate *space*, not merely its initial spread.

## 3. Biological reference

MECH-267 is well-grounded: Pfeiffer & Foster 2013 (goal-directed forward replay), Tambini 2019 (task-relevant reactivation bias), Olafsdottir 2018 (state-dependent replay content review), Mattar & Daw 2018 (prioritized memory access — gain/need both depend on mode via the goal hierarchy), Wikenheiser & Redish 2015 (theta-cycle look-ahead distance scales with goal distance — directly supports horizon-depth as a real biological mechanism, the one *not* implemented here). The biology supports mode-conditioned content robustly; the FAIL is about an incomplete instantiation, not a biology mismatch.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **claim not tested under conditions where it could fully express itself** | only 1 of ≥2 claimed mechanisms (noise-scale) was implemented and tested; horizon-depth was explicitly deferred at build time |
| Biological reference | strong, multi-source | 5 supporting literature entries, including one (Wikenheiser & Redish 2015) directly evidencing the untested mechanism |
| Prerequisites | present | SD-032a (SalienceCoordinator), MECH-261 write-gating, MECH-092 — all implemented per the claim's depends_on |
| Implementation | **partial** — noise-scale only, horizon-depth explicitly deferred at 2026-04-20 build time | this is the load-bearing gap |
| Environment | adequate, well-powered | 30 seeds, clean pre-registered manipulation check |
| Measurement | excellent | C0/C1 separation cleanly isolates "wiring present" from "survives production refit" |
| Integration | plausible causal mechanism identified | CEM elite-refit toward a mode-independent value function structurally erases an initial-noise-only bias |
| Scale | n/a | |

## 5. Learning extracted

1. A claim asserting multiple sub-mechanisms should be tracked as partially- vs fully-implemented; testing against only the implemented subset and reading a FAIL as pressure on the whole claim risks under-crediting the untested part.
2. CEM (and similar iterative-refit optimizers) can structurally wash out an *initial-distribution-only* manipulation if the downstream selection criterion is mode-independent — worth generalizing as a design principle for any future mode-conditioning mechanism implemented purely as a sampling-noise multiplier.
3. The manipulation-check-vs-production-settings split (C0 vs C1) is a strong pattern worth reusing elsewhere: it cleanly separates "the wiring exists" from "the effect survives realistic downstream processing," which a single aggregate criterion would have conflated.

## 6. Routing (user-confirmed 2026-08-02)

**User confirmed:** treat as an implementation gap (horizon-depth modulation never built), not claim pressure against MECH-267 itself.

**Recommended `epistemic_category`:** `competence_implementation_gap` (the claim's own asserted mechanism was only partially built; the untested half is directly literature-supported).
**Recommended `evidence_direction`:** `non_contributory` (informative about implementation completeness, not evidence against mode-conditioned hippocampal proposals as a claim).

**Routing: `/implement-substrate`** — build horizon-depth modulation for `HippocampalModule.propose_trajectories` (per the claim's own text and the original 2026-04-27 lit-pull recommendation, deferred at 2026-04-20 build time to "V4 reconsideration"). `pending_retest_after_substrate: true` — once built, retest content persistence under production CEM settings with both mechanisms active.

Re-derive brake: 0 prior autopsies for MECH-267 — first-ever autopsy target. Does not fire.

Granularity-debt recurrence trigger: checked via `granularity_debt_cluster.py MECH-267` — 0 prior tagging targets. Does not fire.
