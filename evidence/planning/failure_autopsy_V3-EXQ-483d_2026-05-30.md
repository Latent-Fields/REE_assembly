# Failure Autopsy: V3-EXQ-483d

- **Scope:** single (references EXQ-483 cohort; does not re-open closed superseded manifests)
- **Status:** confirmed
- **Generated:** 2026-05-30T05:46:16Z
- **Manifest:** `evidence/experiments/v3_exq_483d_sd037_broadcast_gap4_override_signal/v3_exq_483d_sd037_broadcast_gap4_override_signal_20260529T220132Z_v3.json`
- **Run id:** `v3_exq_483d_sd037_broadcast_gap4_override_signal_20260529T220132Z_v3`
- **Queue id:** `V3-EXQ-483d` (supersedes `V3-EXQ-483c`)
- **Claims tagged:** SD-037, MECH-280, MECH-281
- **Outcome:** FAIL
- **Failed criterion:** discrimination (`C3_lift_vs_baseline`)
- **Routing:** implement-substrate (amend SD-037 entry in `substrate_queue.json`)

## 1. Facts reconstruction

Four-arm 2x2 factorial (gabaergic-decay + PAG-freeze-gate axis x broadcast-override axis), three seeds (42, 7, 19). Arms: `OFF_OFF` (baseline), `ON_OFF` (decay+freeze only), `OFF_ON` (override only), `ON_ON` (full GAP-4). Tier-1 acceptance requires the `ON_ON` arm to clear C1 / C2 / C3_approach_commit / C4 in >= 2 seeds AND `goal_norm_peak(ON_ON) > goal_norm_peak(OFF_OFF) + 0.01` in >= 2 seeds (`C3_lift_vs_baseline`).

Result: `pass=false`. Only `C3_lift_vs_baseline=false` (`C3_lift_count=1`). C1 / C2 / C3_approach_commit / C4 all PASS at the top-level acceptance. C2 (the FAIL in 483c) is now solidly PASS: `override_signal_nonzero_steps` saturates at the total step count in every `OFF_ON` and `ON_ON` seed (e.g. seed 42 `ON_ON`: 1658 / 1658).

Per-seed pattern (the load-bearing observation):

| Seed | OFF_OFF action_counts | OFF_ON action_counts | OFF_OFF goal_norm_peak | OFF_ON goal_norm_peak |
|---|---|---|---|---|
| 42 | {0:5,1:502,2:6,3:859,4:7} | {0:5,1:502,2:6,3:859,4:7} | 0.2261 | 0.2261 |
| 7  | {2:1,4:58}                | {2:1,4:58}                | 0.0919 | 0.0919 |
| 19 | {0:303,2:456,4:34}        | {0:303,2:456,4:34}        | 0.2958 | 0.2958 |

The `OFF_OFF` vs `OFF_ON` pair (broadcast_override toggled, all other config held) produces **bit-identical action distributions and bit-identical `goal_norm_peak`** within each seed. The `ON_OFF` vs `ON_ON` pair shows the same bit-identical pattern. `bridge_write_fires` differs marginally (seed 42: 6 vs 7) -- numerical noise downstream of the override path, not a behavioural lever. `dacc_bias_nonzero_steps = 0` across all 12 runs. `approach_commit_rate = 1.0` and `goal_active_fraction = 1.0` in every run (MECH-295 bridge clears them well before the override gets a chance to add anything).

## 2. Claim-layer map

- **SD-037** `regulators.broadcast_override`. status: candidate. v3_pending. Substrate implemented 2026-04-25. Multi-target consumer cascade only partially wired (per MECH-281 implementation_note: "PFC/BLA/beta-gate targets noted in claim title rely on the same override_signal but additional consumer wiring is deferred until those substrates need it"). EXQ-483d is the experiment that surfaces that "need."
- **MECH-280** `pag.lh_override_projection`. status: candidate. v3_pending. Substrate side: PAG `alpha_override` is wired (PAGFreezeGate receives the scaling), but the env does not engage PAG freeze in this run -- there is no committed-freeze state for the exit-threshold scaling to act on. The claim cannot express itself in this env.
- **MECH-281** `orexin.drive_arousal_coupling` (motor-coupling axis). status: candidate. v3_pending. The pre-existing `evidence_quality_note` already documents the EXQ-471/475/483/483a/483b/490/490b/490c/490e/490f/524 cohort as contaminated/superseded by a `update_z_goal` TypeError + StepHarness migration cluster, and adds: "[IGW-20260521-020]: Partial landing (GoalState seeding + SalienceCoordinator) substrate-ready per 483b; PFC/BLA/beta-gate consumers deferred. Cataplexy/PWS behavioural tests still N/A (approach_commit=0)." EXQ-483d clears `approach_commit=0` (now 1.0 via MECH-295 bridge), but produces a fresh wired-but-inert signature on `goal_norm_peak` discrimination.

Did the experiment test the claims under conditions where they could express themselves? Mostly no -- two of the three live consumer pathways (PAG exit-threshold scaling, SalienceCoordinator mode reweight) are dormant in this env / config, and the third (GoalState seeding amplification) is dominated by the MECH-295 bridge contribution to `effective_drive`. The override produces a saturated `override_signal` but has nowhere to land where it would move `goal_norm_peak` against the bridge baseline.

## 3. Biological-reference triage

Closest mammalian reference: lateral-hypothalamic orexin / hypocretin neurons recruited under sustained drive + nociceptive load, broadcasting to multiple targets in parallel -- PAG (escape-from-freeze), NAc / VTA (motivational gain), BLA / CeA (affective salience), mPFC (deliberative bias), LC (arousal). Dependencies of the working reference circuit include: (i) a target system actually in the gate-engaged state the orexin signal modulates (PAG must be in freeze for the alpha_override scaling to matter); (ii) downstream consumers wired and listening; (iii) a sustained-load env that recruits the orexin system at a behaviourally-relevant magnitude. Lit-pull `targeted_review_orexin_kinetics/synthesis.md` already supports the multi-target architectural commitment (Mileykovskiy 2005, Lee 2005, Karnani 2020, Johnson 2012, Carter 2009).

The REE substrate is a faithful translation of the multi-target architectural commitment. What is missing is exactly the multi-target *delivery* in the validation test. The biology does not predict that turning on a single-target orexin proxy in an env that recruits none of its targets would change `goal_norm_peak`; it predicts behavioural divergence only when the targets are engaged. EXQ-483d does not falsify the biology; it shows that the validation surface is impoverished.

This is the load-bearing finding: the failure resembles what would happen biologically if the orexin system fired correctly but PAG was not in freeze, the salience network was offline, and mPFC / BLA were not listening -- i.e., it is a discovered dependency on consumer-side substrate state, not a falsification of the broadcast.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear -- test cannot express the claim | env doesn't engage PAG freeze; SalienceCoordinator not enabled; sleep-onset gating not active; only goal-seeding-gain path is live |
| Biological reference | clear | orexin multi-target broadcast; literature wants behavioural divergence only when consumer targets are engaged |
| Prerequisites | partially missing | `use_salience_coordinator` off; PAG-engaging env condition absent; PFC/BLA/beta-gate consumers deferred; MECH-286 wired but `use_mech286_sleep_onset_gate` not asserted in the ARM config |
| Implementation completeness | partial | per MECH-281 note: "PFC/BLA/beta-gate targets ... deferred until those substrates need it" -- 483d is the result that demonstrates the need |
| Environment adequacy | wrong pressures | fishtank standard env does not generate sustained threat or drive saturation that recruits the override mechanism with a behavioural lever |
| Measurement | under-instrumented | `goal_norm_peak` is dominated by SD-012 + MECH-295 bridge contributions to `effective_drive`; even when override doubles the multiplier, the bridge already saturates the seeding |
| Integration | partially coupled but inert | regulator-to-consumer wiring is effectively single-channel; the only live channel (goal-seeding-gain) is downstream of MECH-295 which already pegs approach_commit at 1.0 |
| Scale / capacity | adequate | not a model-capacity issue |

**Recommended `epistemic_category`:** `substrate_ceiling`. The substrate is V3-tractable in principle -- the consumer-cascade substrates are landed (MECH-282 LPB, MECH-286 sleep onset gate, SalienceCoordinator, PAG freeze gate). What is missing is the wiring + env + config that makes the override mechanism load-bearing at the validation surface. The right response is consumer-cascade substrate work, not more experiments on the existing impoverished surface.

## 5. Cluster context (single-scope reference only)

The EXQ-483 chain is a five-iteration thread on the same architectural surface (483 / 483a / 483b / 483c / 483d). MECH-281's existing `evidence_quality_note` already supersedes 483 / 483a / 483b / 490-cohort with a `[update_z_goal_typeerror_swallowed]` contamination tag plus a StepHarness migration directive. 483c was the first corrected re-run; it FAILed on C2 (`dACC bias` -- a measurement-side bug). 483d corrected that measurement bug (switched C2 to `override_signal_nonzero_steps` on the regulator directly) and PASSes C2 cleanly, but exposes a *fresh* discrimination failure on `C3_lift_vs_baseline` with the wired-but-inert shape described above. This is structurally consistent with the SD-037 substrate_queue's pre-existing prediction: "if still flat, blocker is upstream of SD-037 (MECH-295 bridge), not override wiring." That prediction is now closed by 483d.

Per user direction (`/failure-autopsy the unreviewed`, single scope), I do not re-open the closed superseded manifests; the autopsy applies to 483d only and the cluster is referenced for context.

## 6. Learning extracted

- The wired-but-inert pattern is now confirmed at the SD-037 validation surface: the regulator fires correctly (C2 saturated) but produces zero behavioural lever in this env / config.
- The MECH-295 bridge contribution dominates `effective_drive` at the goal-seeding site, so override amplification at this site cannot produce a discriminative `goal_norm_peak` lift against the bridge baseline. The override needs an *additional* live consumer pathway (PAG exit-threshold under freeze, SalienceCoordinator mode reweight, or PFC/BLA bias) to deliver a behavioural lever.
- The SD-037 substrate_queue's `prediction` field captured exactly this outcome ahead of the run. The substrate-queue metric_trajectory observation infrastructure worked: it told governance the failure mode was upstream of SD-037 wiring before the run. The autopsy closes the prediction and routes the next substrate step.
- The env adequacy gap is real: a sustained-threat env that engages PAG freeze is a substrate prerequisite for any future override behavioural test, not just a nice-to-have.

## 7. Recommended `evidence_quality_note` (governance to write -- do not write here)

> EXQ-483d (supersedes 483c). Substrate fires correctly: `override_signal_nonzero_steps` saturates at total step count in every `OFF_ON` / `ON_ON` seed (C2 cleanly PASS). However `action_counts` and `goal_norm_peak` are bit-identical across the broadcast_override axis within each seed (`OFF_OFF` vs `OFF_ON`; `ON_OFF` vs `ON_ON`), and `C3_lift_vs_baseline` fails (lifts=1/3). MECH-295 bridge dominates `effective_drive` at the goal-seeding site; PAG-freeze and SalienceCoordinator consumer pathways are dormant in this env / config. Substrate-ceiling: SD-037 wired but inert at the validation surface. Closes the SD-037 substrate_queue's pre-existing prediction ("if still flat, blocker is upstream of SD-037, not override wiring"). Hold pending consumer-cascade substrate work (SalienceCoordinator enable + PAG-engaging env condition + PFC/BLA/beta-gate consumers per MECH-281 implementation_note). Pair with `pending_retest_after_substrate`. Apply per-claim: SD-037 evidence_direction `non_contributory`; MECH-280 / MECH-281 evidence_direction `non_contributory` (claims could not express themselves -- their targets were not engaged). Set `pending_retest_after_substrate: true` on all three.

## 8. Recommended routing -- implement-substrate (amend SD-037 entry)

The SD-037 substrate_queue entry already exists and is already `implementation_status: implemented`. The autopsy emits a `failure_record_entry` for governance to append to its `metric_trajectory.observations` plus a recommended update to `current_blocker` / `prediction`. No new substrate_queue entry is needed.

The deferred behavioural-validation EXQ (the queue-experiment alternative) needs the consumer cascade to be `use_salience_coordinator=True` AND a PAG-engaging env condition AND (per MECH-281 note) at least one of the PFC / BLA / beta-gate consumers wired to read `override_signal`. That EXQ is appropriate only after substrate work above is landed. Side note: the EXQ-471 successor (`V3-EXQ-475`-style combined SD-036 + MECH-279 substrate landing) provides the PAG-engaging env path for behavioural validation.

## 9. Routing for the other unreviewed item (out of scope here)

The other entry on `pending_review.md` is `V3-EXQ-612b` (ERROR). ERROR routes to `/diagnose-errors`, not this skill. Flagged in the session report; not actioned in this autopsy.
