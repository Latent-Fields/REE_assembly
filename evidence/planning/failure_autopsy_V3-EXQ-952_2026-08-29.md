# Diagnostic-PASS adjudication: V3-EXQ-952 (SD-075 phasic warmup rescue) — 2026-08-29

**Run:** `v3_exq_952_sd075_phasic_warmup_rescue_diagnostic_20260828T211302Z_v3` · PASS · diagnostic · claim_ids [] · seeds [11,23,29] · ree-worker-1 · self-route `phasic_warmup_rescue_confirmed` · non_degenerate true
**Status:** confirmed (interactive gate 2026-08-29; session autopsy-batch-20260829)
**Dry-run check:** clean (manifest dry_run=false; full pre-registered constants).

## Facts

Answers exactly the retest-design question SD-075's implementation note deferred: with the convergence gate ON, does agent training let `n_events_converged` clear MIN_EVENT_TICKS=10, where an untrained agent gets 0 in both continuity modes? Grid: {warmup 0, 40} × 779b's three starvation-category seeds (11 mild / 23 event-starved canonical / 29 severe), SD-075 carry mode held fixed, threshold inherited verbatim from 779b R1 (not retuned). Result: warmed {16, 12, 42} (min 12 ≥ 10 on every seed) vs control {3, 0, 0}. DV read from the regulator's own counter (phasic_surprise_burst.py:327-361). Recording complete.

## Why the PASS is genuine (each vacuous-pass family checked)

- **Arms genuinely differ**; per-seed treated variance real (12–42); DV pinned in neither arm.
- **Controls genuinely exposed**: control seed 23 had 570 converged ticks with 0 events; even the thinnest control (seed 29, 45 ticks) would have expected ~10 events at the treated rate (P(0) ≈ 1e-5, red-team recompute) — the control zeros are informative on all three seeds, not exposure-starved.
- **Direction survives rate normalization**: seed 23 treated 12/67 = 0.179 events/converged-tick vs control 0/570.
- **Threshold provenance inherited**, not fitted; R0 positive control (burst_level_max = 1.0 grid-wide) is a capability precondition, not the scored criterion.
- **Pre-warmup event count inverts** (controls 17–19, warmed 4–8) — matching the stated hypothesis that the untrained PE stream is early-lifetime transient noise.

**Isolation gap (red-team, recorded):** the regulator's 30-tick gate is lifetime-denominated and does not re-arm per episode under reset mode, so carry mode's *marginal* contribution over reset was not isolated — training also restructures episode length (control seed 23: 87 episodes of ~6.9 steps, the exact 779b binding-axis signature; warmed: 3–14 long episodes), and an identical rescue might have occurred under reset once episodes are long. This does not touch the pre-registered JOINT question (training + carry), and the recommended retest inherits both conditions. Cheap confirmer if the isolation ever matters: a 3-cell reset+warmup arm.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | claim-free by explicit GFLAG-0077 rationale (779-lineage mis-tagging) |
| Biological reference | partial | LC-NE phasic signalling is the parent; this probes an instrumentation gate |
| Prerequisites | present | SD-075 implemented 2026-07-19; SD-074 warmup; all cells cache-miss |
| Implementation | complete | regulator's own counter; SD-075 config fixed grid-wide |
| Environment | adequate | byte-identical to 779b except the two SD-075 fields |
| Measurement | adequate | inherited threshold; pre-registered non-degeneracy; controls exposed |
| Integration | coupled | real REEAgent + warmup + regulator in the live loop |
| Scale | adequate | min-over-seeds conjunctive read on 3 deliberately-hard seeds |

**Failure-location: n/a** — no failure; PASS adjudicated genuine.

## Disposition (user-confirmed)

- Self-route label **accurate at its stated scope**: a new-number MECH-063(ii) retest using carry mode + warmup exposure is now evidence-supported (queueing it remains a governance decision, per the run's own interpretation summary).
- Direction non_contributory, category `standard` (claim-free diagnostic).
- **Substrate entry amend** (`sd_phasic_ema_episode_continuity` / SD-075): mark the 779b failure record (`v3_exq_779b_mech063_tonic_phasic_dissociation_20260718T233554Z_v3`) **resolved** — carry + warmup=40 clears the failure mode on all three starvation seeds; consider flipping `ready`. The 779b brake's own artifact anticipated exactly this post-substrate retest (`pending_retest_after_substrate: true`); it refused only a lettered 779c.
- **Routing: queue-experiment** — the new-number retest (claims per governance, plausibly [MECH-063, SD-069] with per-claim directions). Not spawned by this session (2026-07-30 rule).

**Re-derive brake:** MECH-063's brake (count 3) fired at 779b and is *honoured*, not re-fired: this run is not the braked retest, and its recommendation is the new-number redesign the brake explicitly permits now that SD-075 is built.

**7b:** 0 fires (claim-keyed checks inapplicable). **7c:** CONFIRMED; run_id placeholder fixed and isolation gap recorded per red-team.

## Learning extracted

1. The re-derive brake worked end to end: 779b's brake refused the cheap re-run, routed to /implement-substrate (SD-075), and this diagnostic converted the build into an evidence-supported retest design at probe cost.
2. When a treatment jointly moves the DV's mechanism and a structural covariate that is itself the diagnosed binding axis, the joint effect answers a retest-design question — record the mediation honestly (and the isolation gap explicitly) rather than calling it a confound.
3. Formalising a never-run scratch spike into a queue-visible diagnostic is the correct path; the spike alone would have answered nothing durably.
