# Failure Autopsy — V3-EXQ-228c (ARC-032)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-10 — user confirmed the implementation-gap reading over a claim-level negative)

## 1. Facts

Manifest: `v3_exq_228c_arc032_theta_bypass_readout_20260809T110214Z_v3`, `claim_ids: [ARC-032]`, `supersedes: V3-EXQ-228b`, `queue_id: V3-EXQ-228c`, `experiment_purpose: evidence`. Run: 9826s (~2.7h), `ree-cloud-2`, 3 seeds `[42,43,45]`, full `scaffolded_sd054_onboarding` curriculum. Recording complete (`validate_recording.py`: 0 always-core gaps), `substrate_hash` present and `substrate_stable_across_run: true`.

This is the second redesign in the 076/228/247/228a/228b lineage, and the first run to fix BOTH measurement-adequacy defects the confirmed `failure_autopsy_V3-EXQ-228b_2026-08-09` identified: (a) E3-tick cache-gating diluted any theta-specific signal ~9x in a full-episode aggregate; (b) 228b measured only a downstream behavioral proxy (resource-collection lift), never claims.yaml's own CONFIRMING DVs (z_goal persistence, goal-proximity-score noise). 228c keeps 228b's proven shared-training/deepcopy-split architecture byte-identical and measures the two named DVs DIRECTLY, restricted to E3-tick steps.

**Criteria:**
| Criterion | frac seeds | pass |
|---|---|---|
| Precondition (goal_norm ≥ 0.05) | 1.00 | **True** |
| C1 persistence (persist_delta ≥ 0.02) | 0.00 | **False** |
| C2 noise (noise_delta ≥ 0.005) | 0.00 | **False** |

`persist_delta_mean = 4.47e-07` (essentially zero); `noise_delta_mean = -0.0671` (reversed sign — ACTIVE is *noisier*, not quieter). `reversed_persist_frac_seeds = 0.33`, `reversed_noise_frac_seeds = 1.00`, `reversed_trend = 1.00`. The manifest's own interpretation registers this as a REVERSED-TREND finding, not dismissed: theta ACTIVE was the *worse* arm on ≥0.67 of seeds.

## 2. Claim-layer mapping

ARC-032 (`docs/claims/claims.yaml`): status `candidate`, `implementation_phase: v3`, `epistemic_category: substrate_conditional`, `depends_on: [MECH-089, MECH-116]`. No `confidence`/`invariant_type`/`emergent_from`/`v3_pending` fields present. `evidence_quality_note` chain shows this is the FIRST time the claim's actual CONFIRMING DVs (persistence, proximity-noise) have ever been measured directly — every prior attempt (076d/e/f, 228/228a, 228b) either failed the precondition or measured a proxy. The test is now fair.

## 3. Biological-reference triage

Closest reference: Sigurdsson et al. 2010 (theta synchrony supports frontal-hippocampal goal maintenance; disruption predicts *degradation*, not null). REE's `ThetaBuffer.summary()` is a flat, unweighted mean over a fixed 10-step window. The deeper literature (Dragoi 2006 theta-sequence compression, Colgin 2016 theta-gamma phase nesting) attributes theta's functional payload specifically to phase/sequence-order encoding, not temporal averaging. This is a formal-definition-style simplification (average-the-signal) standing in for a biologically load-bearing structural property (order-within-cycle), and per SD-003 precedent this divergence is treated as load-bearing, not a caveat.

**Independent corroboration:** MECH-089's own confirmed EXQ-066 (batched theta error 2.28x worse than raw) and EXQ-122 (harm_auc delta = -0.135, adverse) already established that static/uniform theta-averaging measurably *hurts* E3's fine-grained discrimination. 228c's reversed-trend finding is the same signature appearing under a second, independent claim's test.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | test is now fair — both 228b-identified defects fixed |
| Biological reference | clear, implementation diverges | Sigurdsson predicts degradation; flat-mean captures rate not phase/order |
| Prerequisites | present | precondition 1.00 frac |
| Implementation completeness | **partial** — symbol vs functional role | flat-mean "packaging" is complete as code but structurally cannot carry phase/sequence information |
| Environment adequacy | adequate | |
| Measurement adequacy | **adequate now** | E3-tick-restricted, direct DVs — this run's own fix |
| Integration adequacy | coupled, confirmed non-inert | goal_norm_active_mean 0.468, z_goal_stream healthy (active_frac 0.9999) |
| Scale/capacity | adequate | full curriculum budgets, 3 seeds |

**Failure-location (GOV-FAILLOC-1):** Implementation reads `partial`, not `complete` — MECHANISM FAILED is not established (that bucket requires a complete implementation still failing). This is not a REE-failed or clean mechanism-failed reading; it is a biology-divergence implementation gap.

## 5. Learning extracted

- The claim's decisive DVs, measured directly and fairly for the first time, show no effect on persistence and a *reversed* effect on noise (theta ACTIVE noisier, not quieter).
- This converges with MECH-089's independently-confirmed EXQ-066/EXQ-122 findings: flat-mean theta-averaging measurably degrades E3's fine-grained discrimination.
- Biology (Dragoi 2006, Colgin 2016) attributes theta's functional payload to phase/sequence-order structure, which `ThetaBuffer.summary()`'s flat mean cannot represent by construction.
- Driver flags a known open substrate defect (SD-E3-SCORER-COMPLETION, since resolved 2026-08-09T08:27Z, likely active for only part of this run given timing) — noted, not treated as a confound on these specific DVs (persistence/noise are computed independent of the untrained scorer heads that defect concerned).

## 6. Routing (confirmed at interactive gate)

**User-confirmed disposition:** implementation gap, not a claim-level falsification. `evidence_direction: weakens` (the flat-mean operationalization specifically — not a falsification of the broader frontal-hippocampal-theta-packaging claim). `epistemic_category: substrate_conditional` (unchanged from current claims.yaml — the claim's answer remains gated on a substrate build).

Routing: `/implement-substrate` — a phase/sequence-order-aware ThetaBuffer summary (e.g. weighting or preserving within-window ordinal structure rather than a flat mean), grounded in Dragoi 2006 / Colgin 2016. `recommended_substrate_queue_entry.action: create` (no existing substrate_queue.json entry names ARC-032 or this mechanism). Exact source location of `ThetaBuffer.summary()` was not resolved in this fact-gathering pass — `/implement-substrate` scoping should locate it (likely in `ree_core/hippocampal.py` or an E1-output-packaging module, per MECH-089's ownership).

Not routed to demotion: biology does not support the AS-IMPLEMENTED flat-mean approach, so this is not "tested fairly + biology supports the mechanism + still fails" against the general claim — it supports a *different* implementation.

**Draft evidence_quality_note for governance:**
> [2026-08-10 governance, V3-EXQ-228c, confirmed failure_autopsy_V3-EXQ-228c_2026-08-10]: the redesign owed by the 228b autopsy (E3-tick-restricted, direct persistence/proximity-noise DVs) has now run. Precondition met (1.00 frac). Both primary criteria FAILED 0/3 seeds, with a REVERSED trend registered as a finding (theta ACTIVE noisier on 3/3 seeds, less persistent on 1/3) — converging with MECH-089's confirmed EXQ-066/EXQ-122 findings that static/uniform theta-averaging measurably hurts E3's fine-grained discrimination. Biology (Dragoi 2006, Colgin 2016) attributes theta's functional payload to phase/sequence-order structure; ThetaBuffer's flat unweighted mean cannot represent this by construction — a biology-divergence implementation gap, not a claim falsification. epistemic_category stays substrate_conditional. Routing: /implement-substrate for a phase/sequence-order-aware theta summary. Status unchanged (candidate).

Step 9b: no existing hypothesis-space qid names ARC-032 (confirmed by predecessor autopsy); no `fanout_recommendation` emitted here either. Registration deferred, consistent with prior practice.
