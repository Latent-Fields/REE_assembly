# Failure Autopsy -- V3-EXQ-701c (INV-050 MEL measurability, recon-only P0 + frozen MEL probe)

- **Generated (UTC):** 2026-06-30T21:16:25Z
- **Scope:** single
- **Status:** confirmed (user-gated 2026-06-30)
- **Run:** `v3_exq_701c_inv050_mel_measurability_recononly_20260629T223011Z_v3`
- **Queue:** V3-EXQ-701c (supersedes V3-EXQ-701b; diagnostic; PROMOTES NOTHING)
- **Claim:** INV-050 (three-drive sleep regulation; the novel content is the THIRD / Model Error Load drive) -- `candidate`, invariant/emergent (emergent_from SD-017), `pending_substrate_reconfirmation: true`
- **Outcome:** FAIL / `evidence_direction: non_contributory` / self-route `mel_not_modulated_by_novelty`
- **This is the pre-registered 701b brake-lock decision point** ("the brake LOCKS only if 701c's recon-only base also fails to yield a clean MEL read" -- failure_autopsy_V3-EXQ-701b_2026-06-29).

## 1. Facts (no interpretation)

The 701b SD-056-destabiliser fix WORKED. Readiness is fully met on the recon-only base:

- **R2** `world_model_converged_p0_seed_fraction` = **1.0** (>= 0.667 floor) -- the recon-only P0 world-forward converged on **3/3 seeds** on the FIXED frozen probe battery (per-seed conv_rel_drop 0.972 / 0.974 / 0.982). The 701b ablation prediction (recon-only converges 3/3) held.
- **R1** `pe_response_range_to_novelty_shock` = **1.15** (>> 0.25 floor) -- the converged frozen model's PE rises ~115% under a max-novelty shock. The positive-control probe genuinely detects novelty.
- `readiness_ok = true`, `criteria_non_degenerate` C2 = true (real cross-seed spread; not pinned).

So this is **NOT a self-route / vacuous FAIL** (contrast 701/701a/701b, which all failed upstream at the readiness/instrument layer). The precondition layer is non-degenerate and the base is valid.

**The single failed sub-criterion.** `c1_pass = false` driven by **`abs_spread_ok = false` ONLY**:

| C1 sub-criterion | value | pass? |
|---|---|---|
| `monotone` (NONE<=LOW<=MED<=HIGH) | NONE 2.032e-5 < LOW 2.193e-5 < MED 2.405e-5 < HIGH 2.712e-5 | **true** |
| `rel_spread_ok` (HIGH >= NONE x 1.25) | rel spread 0.335 vs 0.25 floor | **true** |
| `abs_spread_ok` (HIGH-NONE > 1e-4) | HIGH-NONE = 6.8e-6 vs 1e-4 floor | **false** |

`arm_order_by_novelty` confirms the ordering is by novelty level. MEL **is** cleanly, monotonically modulated by graded waking novelty. The manifest's self-route label `mel_not_modulated_by_novelty` is therefore a **misnomer** for what the data show: MEL **is** modulated; the absolute spread is merely below an inherited floor.

## 2. Floor provenance (the crux)

`ABS_MEL_FLOOR = 1e-4` requires the HIGH-NONE per-arm MEL *difference* to exceed 1e-4.

- **701b** (un-converged recon+contrastive base, conv_frac 0.333): MEL lived at ~1.76e-3 .. 2.96e-3. A 1e-4 floor was ~3-6% of signal -- a reasonable anti-pinned guard, and that base's MEL was **non-monotone** (NONE 1.76e-3, LOW 2.96e-3, MED 2.68e-3, HIGH 1.79e-3).
- **701c** (converged recon-only base): the world-forward actually converged (conv_pe_final ~1.4e-4 .. 1.9e-4), so per-step e3 PE dropped ~**75-100x** to ~2e-5. The floor stayed 1e-4 -- now **~5x the entire `mel_high` magnitude (2.7e-5)** and ~15x the actual HIGH-NONE spread (6.8e-6).

On a converged frozen world-forward where per-step PE lives at ~1e-5, requiring a between-arm *difference* of 1e-4 is **structurally unreachable no matter how strongly novelty modulates MEL.** `ABS_MEL_FLOOR=1e-4` is an inherited constant from a ~100x-larger PE regime; it is mis-scaled for the converged base by construction. (`MONO_TOL` and `arm_means_vary` also key off `ABS_MEL_FLOOR` and inherit the same mis-scale, but did not bind here.)

This is exactly the user's reading (b): is 1e-4 the right absolute floor given the substrate's per-step PE scale on a frozen converged model? Answer: no -- the converged-model PE simply lives at ~1e-5.

## 3. Claim-layer map

INV-050's directly-testable IV content -- "is accumulated waking prediction error a measurable, graded, manipulable quantity?" -- is, on the relative criteria the design trusts (the V3-EXQ-643 "same kind of statistic C1 routes on" rule), **effectively DEMONSTRATED**: monotone in novelty + relative spread above floor on a VALID converged + novelty-responsive base. This is the strongest MEL-measurability evidence to date and a clean monotone signal that 701b's un-converged base did not have. INV-050 is **UNWEAKENED** (diagnostic, scoring-excluded; status unchanged). The failure sits at the **instrument-calibration** layer (one mis-scaled absolute constant), not at the claim.

## 4. Biological-reference triage

The MEL adaptive-sleep response is a strong existence proof: increased slow-wave activity, spindle density, and hippocampal replay proportional to novelty/learning load (Wilson & McNaughton 1994; Tononi & Cirelli 2003; Stickgold et al. 2001 -- all in the INV-050 notes). 701c exercised the mechanism and it behaved **exactly as biology predicts**: more novelty -> more accumulated prediction error, monotonically. There is **no biological divergence** here; the FAIL is a pure absolute-magnitude artifact. Demotion (the highest threshold: tested fairly + biology supports + still fails) is **not** reached -- the mechanism did not fail; the floor did.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact (effectively strengthened on IV precondition)** | MEL measurable + monotone on relative criteria; INV-050 UNWEAKENED |
| Biological reference | **clear (supports)** | Wilson&McNaughton / Tononi&Cirelli / Stickgold; behaviour matches prediction |
| Prerequisites / dependency | **converged base SUPPLIED; consumer MISSING** | recon-only 3/3 (R2 met) -- 701b fix worked. Missing prereq is downstream: the MEL-consumer (adaptive sleep-cadence / MECH-180); V3-EXQ-677 showed sleep counts scheduler-pinned |
| Implementation completeness | **one mis-calibrated constant** | ABS_MEL_FLOOR=1e-4 inherited from 701b's ~2e-3 regime; structurally unreachable on the ~2e-5 converged base |
| Environment adequacy | **adequate** | graded novelty arms produced graded MEL exactly as designed |
| Measurement adequacy | **relative: adequate; absolute floor: mis-scaled** | the load-bearing finding -- relative monotone signal is clean; the abs floor fires a false-negative |
| Integration adequacy | n/a | single-module frozen probe |
| Scale / capacity | adequate | ~1e-5 per-step PE is the converged world-forward's natural scale, not an inadequacy |

Dominant diagnosis: **instrument floor mis-calibration on a VALID converged base** -> the IV precondition is effectively met; the frontier has advanced from "is MEL measurable?" (now: yes, relatively) to "does MEL drive adaptive sleep cadence?" (blocked on the absent consumer substrate). NOT `substrate_ceiling`; NOT a falsification.

## 6. Re-derive brake -- FIRED (user-confirmed)

701c is the **4th** consecutive `non_contributory` INV-050 diagnostic (701, 701a, 701b, 701c), well past the default threshold 2, and 701b explicitly named **this run** as the lock-point. The brake **FIRES** -- but for a different reason than "ceiling":

- Mechanism: the prior three were instrument repairs (P0 divergence -> exploration-drift confound -> SD-056 destabiliser). 701c finally has a valid converged base AND a clean relative MEL signal. Measurability is **effectively demonstrated**; another measurability letter would re-derive nothing.
- Action: **REFUSE any same-claim measurability re-queue (no 701d).** A one-line floor re-calibration to convert this to a formal PASS adds no scientific information -- it is exactly the same-claim re-test the brake exists to stop.
- Route (in principle): `/implement-substrate` on the MEL-consumer / adaptive-sleep-cadence substrate (MECH-180, SD-017-emergent) -- the consumer that would make the now-measurable MEL signal functional.
- **Substrate-queue action = none (deferral honored).** The user deferred the enrichment build on 2026-06-14 and it **remains deferred** (user-confirmed 2026-06-30). Do NOT create a substrate_queue entry now. Record the floor mis-calibration as a learning note for whoever later builds the consumer test-bed. INV-050 stays measurability-demonstrated / consumer-substrate-blocked.

## 7. Learning extracted

- The 701b SD-056-destabiliser fix is **validated end-to-end**: recon-only P0 converges 3/3 on the frozen battery (R2 1.0) and the converged model's PE responds to novelty (R1 1.15). The instrument chain is finally clean.
- On the valid base, **MEL is measurable and cleanly monotone in graded novelty** (rel spread 0.33 > 0.25) -- the strongest MEL-measurability evidence to date, and monotone where 701b's un-converged base was not.
- `ABS_MEL_FLOOR=1e-4` is **mis-calibrated** for a converged frozen world-forward (per-step PE ~1e-5): the absolute-spread floor must scale to the converged base's PE (e.g. a relative-only floor, or abs floor ~1e-6) for any future consumer test-bed. Logged as an instrument note; NOT acted on as a re-queue.
- INV-050's frontier has moved: measurability is demonstrated; the open question is functional sufficiency (does MEL drive sleep cadence?), which is **untestable until the MEL-consumer scheduler exists** (deferred).

## 8. Routing (user-confirmed)

- **Adjudication:** (b) floor mis-calibration -> IV precondition effectively MET. INV-050 UNWEAKENED, status unchanged.
- **Re-derive brake:** FIRED. Refuse same-claim re-queue (no 701d). `recommended_substrate_queue_entry action = none` (2026-06-14 deferral honored / remains deferred).
- **Governance to apply:** append the evidence_quality_note below to INV-050; set/keep `pending_retest_after_substrate` pointed at the adaptive sleep-cadence / MEL-consumer (MECH-180); status unchanged. This skill does not edit claims.yaml.
- **Not routed:** no `/queue-experiment` (brake), no `/lit-pull` (biology already present + supportive), no demotion (biology supports the mechanism), no `/claim-synthesis` (the recurrence here is same-granularity instrument repair, not granularity debt -- INV-050 is not several claims).

## Draft evidence_quality_note (for governance; do not write here)

> V3-EXQ-701c (2026-06-30, recon-only P0 + frozen MEL probe, supersedes 701b; confirmed failure_autopsy_V3-EXQ-701c_2026-06-30) -> non_contributory, INV-050 UNWEAKENED (diagnostic, scoring-excluded; status unchanged). The 701b SD-056-destabiliser fix WORKED: readiness fully met -- R2 conv_seed_fraction=1.0 (recon-only base converged 3/3 on the frozen battery) + R1 pe_response=1.15 (>>0.25). On this VALID converged + novelty-responsive base MEL is CLEANLY MONOTONE in graded novelty (NONE 2.03e-5 < LOW 2.19e-5 < MED 2.41e-5 < HIGH 2.71e-5), relative spread 0.33 > 0.25 -- the strongest MEL-measurability evidence to date and a clean monotone signal 701b's un-converged base lacked. C1 FAILED on ONE sub-criterion only: abs_spread_ok=false, because ABS_MEL_FLOOR=1e-4 (inherited from 701b's ~2e-3 PE regime) is structurally unreachable on the converged base, where per-step PE lives at ~2e-5 and the 1e-4 spread floor is ~5x the entire signal. ADJUDICATION (user-confirmed 2026-06-30): floor MIS-CALIBRATION, NOT a measurability ceiling and NOT a falsification (biology supports MEL: Wilson&McNaughton 1994 / Tononi&Cirelli 2003 / Stickgold 2001). The IV precondition (MEL measurable + monotonic) is EFFECTIVELY MET on the relative criteria the design trusts (V3-EXQ-643 rule). The frontier has advanced: measurability is demonstrated; the gate is now the ABSENT MEL-CONSUMER substrate (adaptive sleep-cadence / MECH-180; V3-EXQ-677 showed sleep counts scheduler-pinned), whose build was deferred by the user 2026-06-14 and REMAINS deferred. Re-derive brake FIRED (4th non_contributory INV-050 diagnostic; the named 701b lock-point): REFUSE any same-claim measurability re-queue (no 701d); recommended_substrate_queue_entry action=none (deferral honored); the floor mis-calibration is recorded as a learning note for whoever later builds the consumer test-bed. pending_retest_after_substrate: adaptive sleep-cadence / MEL-consumer (MECH-180).
