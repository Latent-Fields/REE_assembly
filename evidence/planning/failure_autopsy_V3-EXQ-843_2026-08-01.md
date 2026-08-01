# Failure Autopsy: V3-EXQ-843 (MECH-203 serotonergic replay-salience dose-response, redesign)

**Generated:** 2026-08-01T21:02:08Z
**Run:** `v3_exq_843_mech203_sws_replay_salience_dose_response_20260801T195300Z_v3`
**Queue ID:** V3-EXQ-843
**Claim IDs:** MECH-203
**Status:** confirmed (interactive gate completed with user)
**Machine/elapsed:** ree-worker-3, 2191.5s (~36.5min)

## 1. Facts

**Design.** Per-seed: (1) a waking rollout through a benefit+harm grid world (`CausalGridWorldV2`, `num_hazards=3`, `num_resources=3`, `hazard_harm=0.05`, `resource_benefit=0.05`, 10×10) using the agent's own live policy (`agent.select_action`), accumulating `VALENCE_WANTING` at benefit-contact z_worlds and `VALENCE_HARM_DISCRIMINATIVE` at harm-contact z_worlds in the ResidueField; (2) freeze the valence field, enter SWS; (3) sweep tonic 5-HT (`t5ht`) over `{0.1, 0.3, 0.5, 0.7, 0.9}`, drawing replay windows and calling the real `HippocampalModule._select_valence_weighted_start` at each dose to read whether replay-start selection shifts toward benefit- vs. harm-dominant states as `t5ht` rises. This is a ground-up redesign (new EXQ number, not a lettered fix) of MECH-203, because the only two prior attempts — V3-EXQ-255/256 — are both invalid: an `env.step()` return-order bug broke every episode after one step, so `n_benefit_samples=0` throughout. **MECH-203 has never had a valid test.**

**Dry-run check:** clean (0 dry-run citations).

**Outcome:** FAIL. `non_degenerate: false`. `interpretation_note`: "inadmissible: valence pool degenerate or non-discriminating; MECH-203 selection not scoreable."

**Admissibility (C3) result, all 3 seeds:**

| Seed | n_visited | n_benefit_states | n_harm_states | pool_admissible |
|---|---|---|---|---|
| 42 | 802 | 802 | **0** | false |
| 137 | 4800 | 4800 | **0** | false |
| 2026 | 4745 | 4745 | **0** | false |

Every single visited state across all three seeds — up to 4,800 steps — was classified benefit, never harm. `mean_discriminating_window_fraction = 0.0` (floor 0.10), `max_distinct_benefit_values = 0` (needs ≥3). C1 (benefit dose-response) and C2 (harm complement) could not be evaluated because the field the dose sweep reads from was never populated with any harm-tagged states to begin with.

## 2. Root cause — the agent's own policy is (successfully) hazard-avoiding

The waking rollout drives the environment with `agent.select_action(...)` — the agent's real, live policy, not a random or forced-exploration one. `CausalGridWorldV2` is configured with only 3 hazards on a 10×10 grid at `hazard_harm=0.05` density. A competently-trained policy's whole purpose is to avoid harm contact; with so few, sparse hazards to avoid, a working policy can simply route around all of them indefinitely. That is exactly what happened: zero harm-contact states across three independent seeds and nearly 10,000 combined steps is not a statistical fluke at any plausible non-zero contact rate — it is what a working avoidance policy in a low-density, easily-routable hazard layout looks like.

This is a **protocol design gap**, not a substrate defect and not evidence against MECH-203. The experiment needs the agent to *experience* harm states during the waking rollout in order to test whether tonic 5-HT modulates replay-selection *between* benefit and harm memories — but the current design lets the agent's own competence prevent that exposure from ever occurring.

## 3. Claim-layer mapping

MECH-203 (`serotonergic_replay_salience_tagging`, candidate, `implementation_phase: v3`). `depends_on`: MECH-186 (tonic 5-HT benefit gradient), MECH-121, MECH-165, SD-017. No `evidence_quality_note` exists yet — this is the claim's first-ever run attempt to reach the acceptance-criteria stage (255/256 never got past the broken-episode bug). The claim's own mechanism (drive_state = `[t5ht, 0.5, 1-t5ht, surprise_weight]` reweighting `evaluate_valence`) is read faithfully by this driver from the real `SerotoninModule` and `ResidueField` — the test design is faithful to the claim; the *rollout protocol* that's supposed to feed it harm-tagged states is not.

## 4. Biological-reference triage

The closest reference is the harm-tagging half of the same mechanism family: MECH-099 (residue field marking harm-dense experiences for replay, supported by O'Neill 2010 and Huelin Gorriz 2023) — already claim-registered and biologically grounded. MECH-203's benefit-tagging complement (serotonergic gating of approach/reward-salient replay) is a natural symmetric extension and is not itself in question here; the failure is entirely a rollout-protocol design gap (no harm exposure), not a biology-translation gap. No dedicated `targeted_review_mech_203` literature entry exists yet, but this autopsy does not recommend one — the mechanism's plausibility isn't what failed; the ability to generate a harm-tagged sample to test it against is.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | driver reads the real drive_state formula faithfully; no misalignment |
| Biological reference | clear (by extension from MECH-099's harm-tagging half) | not the failure locus |
| Prerequisites | present | SerotoninModule, ResidueField, HippocampalModule replay-start selection all live and called directly |
| Implementation | complete for the selection-readout half | the SWS/dose-sweep machinery itself is correctly wired |
| Environment | **inadequate** | 3 hazards / 0.05 density on a 10×10 grid, routed by a competent avoidant policy, structurally yields near-zero harm contact |
| Measurement | adequate | correctly detects and reports the resulting degeneracy rather than manufacturing a false verdict |
| Integration | n/a | selection readout never reached, gated correctly at admissibility |
| Scale | not the limiting factor | up to 4,800 steps/seed did not help, because the issue is exposure *policy*, not exposure *duration* |

## 6. Learning extracted

1. **MECH-203 remains fully untested after three attempts**, for two structurally different reasons: V3-EXQ-255/256 (implementation bug, `env.step()` tuple-order mismatch) and V3-EXQ-843 (environment/protocol design — the agent's own competence prevents harm exposure). Neither is evidence for or against the claim.
2. **A trained, avoidant policy driving the waking rollout is fundamentally the wrong tool for generating harm-tagged samples**, regardless of episode count or step budget — this is a design property, not something more compute fixes. A redesign needs either (a) an explicit non-avoidant/forced-exploration phase for harm-sample generation, (b) a denser or less-escapable hazard layout, or (c) direct injection of harm-labeled synthetic states into the pool rather than relying on organic contact.
3. `sleep_substrate_plan.md`'s own stale "EXQ-255/256 PASS; adequate" note (flagged in this driver's own docstring as already known-stale) should be corrected now that neither the original pair nor this redesign has produced a valid test — worth a doc fix alongside the next redesign so a future session doesn't re-trust that line.

## 7. Recommended routing

**Recommended `epistemic_category`:** `measurement_test_design_defect` (environment/protocol adequacy — the rollout cannot generate the sample the acceptance criteria need).

**Recommended `evidence_direction`:** `non_contributory` (scoring_excluded via `non_degenerate: false` — self-route is correct and should stand as-is).

**Recommended `evidence_quality_note`** (draft text for governance):
> [2026-08-01 failure-autopsy, V3-EXQ-843, confirmed]: third consecutive invalid MECH-203 test. Admissibility (C3) failed on all 3 seeds — `n_harm_states=0` across up to 4,800 visited states per seed — because the waking rollout is driven by the agent's own (successfully hazard-avoiding) policy through a low-density hazard layout (3 hazards, 5% harm density, 10×10 grid), which structurally routes around all harm contact. This is an environment/protocol design gap, not evidence against the claim: the SWS replay-selection machinery itself (SerotoninModule drive_state, ResidueField valence, HippocampalModule `_select_valence_weighted_start`) is correctly wired and was never reached. MECH-203 has NEVER had a valid test — V3-EXQ-255/256 were invalidated by an `env.step()` return-order bug (n_benefit_samples=0), and this redesign is invalidated by zero harm exposure. `evidence_direction: non_contributory`, `non_degenerate: false`. `sleep_substrate_plan.md`'s existing "EXQ-255/256 PASS; adequate" note is stale and should be corrected.

**Routing:** `/queue-experiment` — a redesign (new letter, V3-EXQ-843b) that guarantees harm exposure during the waking rollout independent of the agent's own avoidance competence: options include (a) a dedicated forced-exploration/non-avoidant phase for pool-building, (b) increasing hazard density/inescapability enough that avoidance cannot be perfect, or (c) directly labeling/injecting a minimum quota of harm-contact states rather than relying purely on organic visitation. Also flag the `sleep_substrate_plan.md` stale-note correction as a small documentation fix to bundle with the redesign.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for MECH-203 (both prior issues are `measurement_test_design_defect`, not `substrate_ceiling`) — does not fire.

Granularity-debt recurrence trigger: does not fire — no target in MECH-203's autopsy history reads `claim_alignment: weakened`; both prior issues (255/256, 843) are measurement/protocol debt, not a signal the claim itself is too coarse.
