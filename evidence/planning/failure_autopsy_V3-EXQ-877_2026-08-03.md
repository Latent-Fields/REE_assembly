# Failure Autopsy: V3-EXQ-877 (MECH-072 full discriminator-gate design)

**Generated:** 2026-08-03T10:34:50Z | **Status:** confirmed | **Scope:** single

## Facts

- Run: `v3_exq_877_mech072_discriminator_gate_full_20260802T214050Z_v3`, FAIL, `weakens`, claims MECH-072.
- `dry_run_checked: true` -- confirmed real run (`check_dry_run_citations.py`: 0 dry cited, 2 clean).
- Criteria: C1 (direction, all seeds) FAIL, C2 (mean delta) FAIL, C3-C7 (harm parity, event counts, harm-forward quality R2=0.920, null-CF sanity) all PASS. `non_degenerate: true`.
- C1 fails on **all 3 seeds**, and in the **reverse** of the hypothesized direction: `gated_false_attr_rate_mean=0.753` vs `ungated_false_attr_rate_mean=0.506` (delta = -0.247, should be positive). This is small in absolute causal_sig terms (env mean 0.018-0.064 vs agent mean -0.016..+0.025, against `GATE_THRESH_CF=0.002`) but consistent across every seed -- not noise.
- The script (`experiments/v3_exq_877_mech072_discriminator_gate_full.py`) computes `causal_sig = E3.harm_eval_z_harm(E2HarmSForward(z_harm_s,a_actual)) - E3.harm_eval_z_harm(E2HarmSForward(z_harm_s,a_stay))` -- a genuine stay-counterfactual comparator, gating residue accumulation on `causal_sig > GATE_THRESH_CF`. This is the FIRST experiment to gate accumulation on this real discriminator (V3-EXQ-431/525 validated the discriminator itself but never connected it to accumulation; V3-EXQ-213's PASS used an absolute `harm_eval(actual) >= GATE_THRESH` magnitude test with **no stay-counterfactual at all** -- confirmed by reading `experiments/v3_exq_213_mech072_foreseeable_harm_gating.py` lines ~425-431).
- `false_attr_rate = residue_env / total_residue`, computed against `ENV_CAUSED = {"env_caused_hazard","contaminated"}` / `AGENT_CAUSED = {"agent_caused_hazard"}`, per `transition_type` from `CausalGridWorldV2`.

## Environment mechanics (read from `ree_core/environment/causal_grid_world.py`)

- `env_caused_hazard` (line 2243): agent moves onto a static, pre-placed hazard tile. Under the counterfactual `a_stay`, `new_x=old_x` (the agent's own current cell), which the same code path clears to empty/contaminated/resource on every step -- never re-assigns `hazard`. So `a_stay` **reliably avoids** this harm; a correctly-functioning stay-comparator should read a genuinely high `causal_sig` here.
- `agent_caused_hazard` (lines 2209-2210, 2245-2249): the agent moves onto a cell whose `contamination_grid` value has crossed `contamination_threshold` (default 2.0). Contamination deposits `+contamination_spread` (0.5) **at the agent's own currently-occupied cell every tick** (line 2495, `contamination_grid[new_x,new_y] += spread`, `new_x,new_y == old_x,old_y` under `a_stay`). So after ~4 ticks of dwelling on one cell, that cell itself crosses threshold and **`a_stay` triggers the harm** on the following tick, exactly as a real move would. `a_stay` does **not** reliably avoid this harm -- continuing to occupy the cell is what causes it.
- Net effect: `env_caused_hazard`/`agent_caused_hazard` label **hazard-object provenance** (did the environment place this tile, or did the agent's own historical footprint create it) -- a **diachronic** axis. `causal_sig` computes **proximal avoidability** (would a different action *this tick* have avoided it) -- an **instantaneous** axis. These axes are anti-correlated for the contamination subtype specifically, and the observed "reversed" causal_sig pattern (higher for nominally-"env_caused", near-zero for nominally-"agent_caused") is the mechanistically-correct behaviour of a properly functioning proximal comparator -- not a broken discriminator.
- Confirms via claims.yaml history: MECH-072's own `evidence_quality_note` records a 2026-03-20 architectural note (EXQ-054 FAIL) that "world-delta magnitude is insufficient to discriminate agent vs environment causation" and proposed a **supervised discriminator trained on (feature, is_agent_caused) oracle labels** as the fix. What was actually built (ARC-033/SD-011's `E2HarmSForward` + counterfactual comparator) is a structurally different, **unsupervised, theory-driven** mechanism (matching SD-003's counterfactual design) that never references the oracle label during training -- so it has no way to learn the environment's provenance-based partition even in principle.

## Claim-layer mapping (claims.yaml)

- MECH-072: candidate/`v3_pending`, depends_on MECH-071 (provisional, "E2 harm prediction better calibrated for agent- vs env-caused") + MECH-060 (provisional). ARC-033 (provisional) and SD-011 (stable) are consumed, not retested here, correctly excluded from `claim_ids`.
- `granularity_debt_cluster.py MECH-072`: 0 prior autopsy targets tag this claim -- this is the first autopsy artifact for MECH-072, so the recurrence trigger and re-derive brake both read 0 prior hits (this run does not itself route to `substrate_ceiling`, so it does not seed a brake count either).

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened-but-questionable | the test's ground-truth partition does not match the axis the mechanism computes; a fair test of MECH-072's own stated mechanism has not yet been run |
| Biological reference | **clear** | comparator/efference-copy self-attribution (Frith; Blakemore & Wolpert sensory attenuation) -- inherently proximal/instantaneous; has no natural mechanism for diachronic (footprint/trace) self-attribution |
| Prerequisites | present | ARC-033/SD-011 independently validated (V3-EXQ-431/525 PASS); MECH-071 provisional |
| Implementation completeness | complete for the intended (proximal) mechanism | causal_sig computation verified sound via C7 null-CF sanity (all seeds < 1e-5) |
| Environment adequacy | **inadequate for this ground-truth partition** | `env_caused_hazard`/`agent_caused_hazard` encode object provenance, not proximal avoidability -- the two are anti-correlated for the contamination mechanic specifically |
| Measurement adequacy | **misleading** | `false_attr_rate` as defined assumes the transition_type partition tracks responsibility; it tracks hazard-object history instead |
| Integration adequacy | isolated correctly | discriminator computation is self-contained and verified (C7) |
| Scale/capacity | adequate | harm_forward_r2=0.92, well above C6=0.05 threshold |

## Learning extracted

1. The environment's `transition_type` ground truth (inherited from V3-EXQ-002/SD-003) conflates two distinct causal axes: **object provenance** (who/what created this hazard, over the run's history) and **proximal avoidability** (would a different action right now have avoided it). MECH-072's counterfactual-comparator design computes the latter; the experiment's scoring assumes the former.
2. This mismatch is structural, not a training/tuning issue: for the contamination mechanic, "stay" is what *causes* the harm to keep recurring, so no amount of additional training would make a genuine stay-counterfactual comparator agree with the "agent_caused_hazard" label.
3. There are two legitimately distinct senses of self-caused harm here -- proximal (this instant's action) and diachronic (this location's history of my presence) -- and only the first has a real biological analogue in the comparator/efference-copy literature. The second likely needs a separate, memory/trace-based mechanism (something closer to habituation or an explicit self-occupancy trace) that nothing in the current substrate implements or claims to.
4. V3-EXQ-213's PASS is not directly comparable: its absolute-magnitude gate has no stay-counterfactual structure, so it never exercised this mismatch. The 213-vs-877 direction disagreement is not evidence that "the proxy passed but the full discriminator regressed" -- it reflects the two gates testing structurally different questions.

## Routing (user-confirmed 2026-08-03)

**epistemic_category:** `measurement_test_design_defect` | **evidence_direction:** `non_contributory` (per-claim: MECH-072) | **routing:** BOTH of the following, per user selection:

1. **`/queue-experiment`** a same-question redesign (new letter, e.g. V3-EXQ-877a) whose ground truth for `false_attr_rate` is derived directly from a proximal-avoidability oracle check (e.g. "would `a_stay` from this pre-action state have produced this harm, replayed against the environment's own step function") rather than the `transition_type` object-provenance labels. This tests MECH-072's actual mechanism fairly.
2. **`/claim-synthesis`** candidate: a new claim for diachronic/footprint-based self-caused-harm attribution (contamination-style, delayed, location-history-dependent), distinct from MECH-072's proximal comparator, requiring its own (likely memory/trace-based) mechanism. MECH-072 itself should NOT be narrowed or demoted on this basis -- it is not the wrong claim, it is a claim that does not (and per its own biological reference, should not) cover this second case.

**Draft `evidence_quality_note` for governance:**
> EXQ-877 FAIL (2026-08-02): first test gating accumulation on the REAL ARC-033/SD-011 counterfactual discriminator (previously only V3-EXQ-213's world_forward magnitude proxy had been gated on). C1 failed on all 3 seeds in the WRONG direction (gated false_attr 0.753 > ungated 0.506). Root cause identified: the environment's env_caused_hazard/agent_caused_hazard transition_type labels track hazard-OBJECT PROVENANCE (env-placed tile vs agent's own historical contamination footprint), not PROXIMAL avoidability (would `a_stay` have avoided this specific harm) -- and these are anti-correlated for the contamination mechanic (contamination accrues on the agent's own currently-occupied cell, so staying causes rather than avoids it). The discriminator's causal_sig computation is verified sound (C7 null-CF sanity, all seeds); it is behaving as a biological proximal comparator (Frith/Blakemore) should. This is a measurement/test-design gap, not falsification -- v3_pending KEPT. Routed: (1) /queue-experiment redesign with a proximal-avoidability ground truth (2) /claim-synthesis candidate for a separate diachronic self-attribution mechanism.

**User gate (2026-08-03):** Confirmed both routings (redesign ground truth + split-off new claim); demotion explicitly declined.
