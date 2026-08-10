# Failure Autopsy — V3-EXQ-603s (MECH-357)

**Generated:** 2026-08-10T06:27:24Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-10)

## 1. Facts

`v3_exq_603s_instrumental_avoidance_freeze_incompatible_hazard_20260809T161324Z_v3`, `claim_ids: [MECH-357]`, `predecessor_run_id: v3_exq_603r_...`. Run: 24622s (~6.8h), `ree-cloud-4`, 3 seeds `[42,43,44]`, 3 arms (ARM_LESION / ARM_INTACT / ARM_POSCTRL). `validate_recording.py`: 0 always-core gaps, not a dry run.

**Recording-integrity note (raised, not treated as invalidating):** `substrate_stable_across_run: False`, `substrate_identity.drifted_since_resolved: True` — recorded `substrate_hash` (`8ab857...`) does not match the hash on disk at stamp time (`40a2b6...`) on `ree-cloud-4`. At the interactive gate the user confirmed adjudicating this run's finding at face value (the two-sided guard's own criteria are internally consistent regardless of the drift) while flagging the drift as a separate infra concern for follow-up, not as grounds to discard a 6.8h cloud run.

**Two-sided discriminative-headroom guard (this run's own design, built specifically to catch the 603r ceiling mode):**

| Precondition | measured | threshold | met |
|---|---|---|---|
| Pavlovian freeze present (LESION) | 1.0 | 0.667 | True |
| ilPFC gate engages+suppresses (INTACT) | 1.0 | 0.667 | True |
| Stage0 forced-feed z_goal (INTACT) | 0.667 | 0.667 | True |
| **discriminative_headroom_below_lesion_fails_gate** | 0.333 | 0.333 | **False (FAILED)** |
| **survivability_exists_above_posctrl_clears_gate** | 0.667 | 0.667 | **True (PASSED)** |

Self-route: `pressure_insufficient_lesion_ceiling_requeue`. `G_H_INTACT_frac` (0.6667) is *tied with* `G_H_LESION_frac` (0.6667) — the discrimination criterion fails on an exact tie, not a near-miss. `avoidance_efficacy` is numerically ~0 across all three arms (values ~1e-87 to ~1e-132), suggesting the avoidance-credit learner is not meaningfully engaging in this run independent of the pressure question.

This is the second consecutive attempt (after `V3-EXQ-603r`, confirmed `measurement_test_design_defect`) to reintroduce environmental pressure severe enough to force the Pavlovian-instrumental conflict — 603r used a static hazard field, 603s added mobile predators via aggressive environment drift (`env_drift_interval=1, env_drift_prob=0.6` vs the `(5, 0.3)` defaults every prior consumer is bit-identical to). Neither made LESION fail its own negative control.

## 2. Claim-layer mapping

MECH-357 (`docs/claims/claims.yaml`): infralimbic-PFC-analog freeze-suppression + instrumental-avoidance gate, `status: candidate`, `implementation_phase: v3`, `v3_pending: true`, `epistemic_category: standard`, `depends_on: [SD-058, MECH-279, SD-035, SD-011]`. `evidence_quality_note` ends at the 2026-08-09 note for V3-EXQ-603r ("tested twice now, under two different confound sets, both inconclusive by design defect rather than by the mechanism itself. Status unchanged.") — not yet updated for 603s.

## 3. Biological-reference triage

Re-derive brake count (R1-R3 convention, run this session): **zero** confirmed `substrate_ceiling` reads anywhere in the corpus for MECH-357; the only prior confirmed autopsy tagging it (603r) reads `measurement_test_design_defect`. Granularity-debt cluster check: 1 prior target, `claim_alignment: unclear`, "NO target reads weakened -- not granularity debt, regardless of count." Neither standing check fires.

Biological reference unchanged from the 603r autopsy's own triage (partial — active-avoidance paradigms in the literature rely on genuine threat unpredictability to produce the Pavlovian-instrumental conflict the gate is meant to resolve; a static or continuously-drifting field may not reproduce the *discrete, sudden* threat-onset structure those paradigms use).

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | test infrastructure (two-sided guard) worked as designed; still can't discriminate |
| Biological reference | partial | active-avoidance literature relies on discrete/sudden threat onset; unclear whether continuous env-drift reproduces this |
| Prerequisites | present | all three readiness preconditions met at 1.0/0.667 |
| Implementation | partial | avoidance-efficacy numerically ~0 across all arms independent of the pressure question |
| Environment | too_sparse_pressure_still_insufficient | second consecutive config-only pressure increase still doesn't force the conflict |
| Measurement | adequate (two-sided guard functioning) | correctly caught the LESION-still-clears failure mode it was built for |
| Integration | coupled but confounded | |
| Scale/capacity | not implicated | |

**User's hypothesis (recorded, to be incorporated into substrate scoping):** episodes may not be long enough, and/or the mobile-predator pressure may lack truly sudden, discrete novel-threat events needed for measurability — as opposed to smooth continuous drift. This is a genuinely distinct lever from "needs full agent-directed pursuit AI" and should be investigated as part of (or ahead of) the substrate-build scoping below, since it may be achievable through environment-mechanics/episode-length redesign rather than requiring new pursuit-AI code.

**Failure-location (GOV-FAILLOC-1):** Environment reads "still insufficient" (not established adequate); Implementation reads partial (avoidance-efficacy near-zero everywhere). REE FAILED is not established — this is an environment/implementation-adequacy gap, mixed.

## 5. Learning extracted

- Two consecutive config-only pressure escalations (static field, then aggressive mobile-predator drift) both fail to make the LESION arm fail its own negative control; the discrimination criterion failed on an exact tie this time, not even a near-miss.
- `avoidance_efficacy` is numerically ~0 across ALL arms in this run, independent of the LESION/INTACT/POSCTRL distinction — a second, separate signal that the avoidance-credit learner may not be meaningfully engaging.
- A substrate-hash drift was recorded mid-run; adjudicated at face value per user confirmation, flagged separately as an infra concern.
- User's hypothesis: episode length and/or event-suddenness (discrete threat onset vs continuous drift) may be the missing ingredient, distinct from full agent-directed pursuit AI.

## 6. Routing (confirmed at interactive gate)

**User-confirmed disposition:** the config-only lever space (drift interval/probability) appears exhausted at two attempts — escalate to `/implement-substrate`. Per the user's hypothesis, this substrate work should scope BOTH options before committing to full agent-directed pursuit AI: (a) genuine agent-directed predator pursuit (previously scoped as "not config-buildable" when 603s was designed), and (b) an environment-mechanics investigation into episode length and discrete/sudden novel-threat-event timing as a cheaper, config-adjacent alternative that may achieve the same discriminative pressure without requiring new pursuit-AI code.

`evidence_direction: non_contributory` (self-route `pressure_insufficient_lesion_ceiling_requeue` is itself informative about the environment, not the mechanism — consistent with the predecessor's classification pattern). `epistemic_category: standard` (unchanged). `recommended_substrate_queue_entry.action: create` — no existing substrate_queue.json entry covers this specific env-mechanics/pursuit-pressure gap (the related `escape-affordance-bridge` entry depends on MECH-357 being testable but doesn't build this pressure mechanism itself). `severity`: left unset — this defect blocks MECH-357's own test design; it has not been shown to corrupt evidence for any other claim.

Separately flagged (not part of this claim's verdict): the `substrate_stable_across_run: False` / hash-drift finding on `ree-cloud-4` — recommend a follow-up check on whether a concurrent code change landed on that worker mid-run.

**Draft evidence_quality_note for governance:**
> [2026-08-10 governance, V3-EXQ-603s, confirmed failure_autopsy_V3-EXQ-603s_2026-08-10]: second consecutive config-only pressure escalation (603r static field, 603s mobile predators via aggressive env-drift) still fails to make LESION fail its own negative control -- this time on an exact tie (0.6667 vs 0.6667), not a near-miss. avoidance_efficacy numerically ~0 across all three arms independent of the LESION/INTACT/POSCTRL question. non_contributory -- the config-only pressure lever space appears exhausted. Routed to /implement-substrate, scoped to investigate BOTH genuine agent-directed predator pursuit AND an episode-length/event-suddenness environment-mechanics redesign before committing to full pursuit-AI implementation. Recording-integrity note: this run's substrate_hash showed drift on ree-cloud-4 (substrate_stable_across_run=false) -- adjudicated at face value, flagged separately for infra follow-up. Status unchanged (candidate/v3_pending).

Step 9b: no existing hypothesis-space qid names MECH-357; no `fanout_recommendation` emitted (this is a single-lever "escalate the build" routing, not a multi-hypothesis discrimination). Registration deferred.
