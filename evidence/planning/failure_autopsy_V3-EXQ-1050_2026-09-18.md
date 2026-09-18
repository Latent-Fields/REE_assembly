# Failure autopsy -- V3-EXQ-1050 (MECH-021 subjective-now horizon integration)

Generated 2026-09-18T18:41:55Z. Status: confirmed (user, interactive gate). Red-team: opus, CONTESTED on learning claims, disposition survived.

## 1. Facts
- Run `v3_exq_1050_mech021_subjective_now_horizon_integration_20260918T010410Z_v3`, purpose evidence, outcome FAIL, evidence_direction unknown, self-route `substrate_not_ready_requeue`, non_degenerate false. Dry-run gate: 0 dry, 1 clean (check_dry_run_citations.py); dry_run_checked true. Recording core complete (validate_recording OK).
- C1 (future horizon, load-bearing): pooled arf(D30)-arf(D1) = +0.0759 (>= 0.05) but seeds_positive 2/3 (seed0 -0.174, seed1 +0.161, seed2 +0.222) -> fail on sign-consistency. Recomputed exactly from cells (tick-weighted 1316/1212/1542).
- C2 (past window, load-bearing): NOT MEASURED. All 3 ARM_WIN10 cells failed theta_summary_divergence (median L2 8.5e-6 / 3.7e-5 / 6.3e-5 vs floor 1e-3). C3 unmeasurable.
- ARM_WIN1 and ARM_WIN10 produced equal per-episode contacts (7/7, 6/6, 7/7; approach steps 104/92/87 in both).
- E3 fired on 2380 of 2400 steps (n_latched 20) vs nominal every 10.
- Seed 0 warm-up hazard_survival_gate failed (hazard_median_last_window 8.5) yet its cells were scored green; its arf falls with depth (0.449 -> 0.275).

## 2. Claim layer
MECH-021 (provisional, lit_conf 0.81 from 5 lit entries, exp 0; quadrant plausible_unproven). depends_on ARC-008, ARC-005. Claim's own precondition -- the theta window must integrate more than one E1 step -- was not met in effect. Neither FALSIFYING nor CONFIRMING branch reached. No epistemic_category currently set.

## 3. Biological triage
Graded temporal-integration windows (Chaudhuri 2015 timescale hierarchy) plus forward-model depth; targeted_review_mech_021 exists. Not a formal-definition import. No missing-dependency signature identified beyond the substrate observations below.

## 4. Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | C2 never instrumented; C1 sign-inconsistent |
| Biological reference | partial | lit present; translation of a graded window |
| Prerequisites | present | seed-0 warm-up survival gate failed but scored |
| Implementation | partial | window wired, fed, consumed; effect negligible (~1e-5) |
| Environment | partial | static hazards, eval 3 hazards vs warm-up 1, autocorrelated in-band ticks |
| Measurement | partial | P5 gate worked; no warm-up-survival gate; norm ceiling 1e6 non-binding |
| Integration | coupled but inert in effect | see learning |
| Scale | unknown | |

Failure-location (GOV-FAILLOC-1): MIXED (mechanism, measures, environment all partial); not chargeable to REE.

## 5. Learning extracted
1. Window is fed (divergence median strictly > 0 refutes a feed defect) and consumed, but moves the summary ~1e-5 against ~1e-1 for one action: consumed but rank-invariant, not literally inert (seed-2 max rolled norm 97.4 vs 108.8).
2. Fourth cause found by red-team: E3 tick rate collapsed to ~every step, so the cross-rate regime never occurred and in-band ticks are adjacent-step pseudo-replicates.
3. Live causes: H2 z_world temporal under-differentiation; H4 E3-rate collapse. H3 refuted, H1 constrained (n_inband mod 119 = 7/22/114).
4. C1 curves non-monotone; seed 1 lifts by D=10 (+0.165), seeds 0 and 2 only at/after D=20; rolled-norm drift cannot be ruled out for those.
5. Recording gap: z_world step delta, z0 norm, e3 tick trace, position trace not recorded. Readiness gap: no warm-up-survival gate.
6. Manifest combination_rule string omits the non-degeneracy branch (literal reading = weakens); code routes unknown.

## 6. Routing (confirmed by user)
non_contributory, epistemic_category standard (MECH-021 currently has none), no substrate entry, re-derive brake not fired (0 prior MECH-021 tagging targets), granularity-debt trigger does not fire. Route: /queue-experiment same-question re-run (letter 1050a): diagnose E3 rate, make the window span a real cross-rate interval, add warm-up-survival and z_world-norm-ratio gates, record the four missing readouts. Governance chips it. Step 7b pre-routing checks: 0 fires. Step 9b: no registered hypothesis-space question for MECH-021 and no fanout_recommendation (one recording probe discriminates H2/H4), so nothing registered.

Draft evidence_quality_note: see JSON recommended_evidence_quality_note.
