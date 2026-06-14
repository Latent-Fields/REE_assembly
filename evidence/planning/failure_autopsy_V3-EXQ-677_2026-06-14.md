# Failure Autopsy — V3-EXQ-677 (MECH-180 novelty-adaptive sleep upregulation)

- **Generated:** 2026-06-14T16:07:16Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated in the decision-brief follow-up)
- **Run:** `v3_exq_677_mech180_novelty_sleep_upregulation_probe_20260613T161241Z_v3`
- **Queue:** V3-EXQ-677 · **Claim:** MECH-180 · **Machine:** DLAPTOP-4.local
- **Routing:** governance (hold v3_pending) + implement-substrate recommendation (deferred per user)

## 1. Facts (no interpretation)

Two arms × 3 seeds (42/123/456). HIGH_NOVELTY = frequent env drift (`env_drift_interval=3`) + context switching every 5 eps; LOW_NOVELTY = stable env (`env_drift_interval=999`), no switching. 100 episodes, sleep cycle every 10 eps.

| Criterion | Result | Measured |
|---|---|---|
| C1_manipulation_check | **FAIL** | HIGH E1 pred-error 6.539e-4 vs LOW 6.531e-4 → **diff 8.81e-7** (threshold 0.01) |
| C2_sws_upregulation | **FAIL** | HIGH SWS 80 vs LOW SWS 80 → ratio 1.0 (threshold 1.25) |
| C3_rem_upregulation | **FAIL** | HIGH REM 60 vs LOW REM 60 → ratio 1.0 (threshold 1.25) |
| C4_substrate_functional | PASS | SWS 80 ≥ 3, REM 60 ≥ 2 (sleep machinery runs) |
| C5_agent_functional | **FAIL** | goal_success 0.0 in both arms (threshold 0.03) |

Producer self-reported `non_degenerate: false` — `cumulative_sws_writes` constant 80 (zero spread), `cumulative_rem_rollouts` constant 60 (zero spread).

## 2. Claim-layer map

MECH-180 (mechanism_hypothesis → held candidate): "novel environments / high-MEL episodes adaptively upregulate the learning-drive component of sleep (SWA power, spindle density, replay rate) proportional to novelty / prediction-error load." `depends_on` INV-050, MECH-120/121/122. exp_conf 0 (no prior genuine experiments), lit_conf 0.887 (Wilson&McNaughton 1994; Tononi&Cirelli 2003; Stickgold 2001; Louie&Wilson 2001).

**Did the experiment let the claim express itself? No.** The independent variable never moved the E1 prediction-error signal the claim is about (C1), and the dependent variable (sleep amount) is structurally incapable of responding because sleep count is set by the fixed `sleep_interval=10` schedule, not by any novelty/PE signal. The script's own interpretation grid routes "C1 FAIL → non_contributory (manipulation failed)".

## 3. Biological-reference triage

Closest reference: experience-dependent sleep homeostasis — local SWA increases after high-learning wake (Tononi & Cirelli synaptic-homeostasis; Huber 2004 local SWA after a learning task), and novelty-biased replay (Wilson & McNaughton). The biology is an existence proof for the **class** of mechanism. The REE substrate has the *symbol* of sleep (SWS/REM phases run) but not the *functional role* MECH-180 names: there is no channel by which preceding-wake prediction-error load scales the amount/depth of the subsequent offline phase. This is a faithful-translation **gap**, not a falsification.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not tested) | the claim could not express itself; C1 manipulation failed |
| Biological reference | clear | experience-dependent SWA homeostasis + novelty-biased replay; reference mechanism exists |
| Prerequisites / dependency | missing | no wake→sleep PE-accumulator coupling; sleep cadence is schedule-driven |
| Implementation completeness | partial / stub | sleep phases execute but offline-resource *amount* is a fixed constant |
| Environment adequacy | unknown | the drift/switch manipulation did not register as an E1 PE difference — env pressure not reaching the measured signal |
| Measurement adequacy | misleading | C2/C3 read a scheduler-fixed counter (zero variance) — the metric can never discriminate |
| Integration adequacy | isolated | novelty pathway and sleep-resource allocation are not coupled |
| Scale / capacity | n/a | goal_success 0 indicates the agent also never solved the task (separate, see note) |

**Recommended epistemic_category (autopsy):** `substrate_ceiling` — V3-tractable in principle, but the current substrate is too coarse (fixed sleep cadence) to deliver the distinction. **User disposition:** hold `v3_pending` instead (frames it as "wait for the sleep-cadence enrichment build"), which suppresses the same recs and is coherent because the enrichment is V3 substrate work.

## 5. Learning extracted

- The C2/C3 metrics are **vacuous by construction** on the current substrate: SWS/REM counts derive from `sleep_interval`, not from any novelty/PE signal, so they have zero cross-arm variance regardless of behaviour. Any future MECH-180 test must instrument an *adaptive* sleep-resource variable, not the scheduled count.
- The novelty manipulation (env drift + context switch) did not produce a measurable E1 prediction-error difference (C1) — the manipulation itself needs validation before it can drive a sleep response. Possibly the drift magnitude is absorbed by the world model within an episode, or the measured `mean_e1_prediction_error` is averaged over a window that washes out the novelty transient.
- `goal_success = 0` in both arms is a separate baseline-health concern shared with the MECH-057b baseline-collapse finding (V3-EXQ-672a) — worth a cross-check of whether this env/training config produces a functional agent at all.

## 6. Repair pathway

**implement-substrate** (primary, deferred per user) + **queue-experiment redesign** once substrate lands.

Draft `evidence_quality_note` for governance (already applied to claims.yaml `governance_2026_06_14`): MECH-180 held `v3_pending`; V3-EXQ-677 non_contributory + degenerate (manipulation failed; sleep counts scheduler-pinned, zero variance); exp_conf stays 0; promotes/demotes nothing.

## 7. Recommended substrate_queue entry (NOT written — enrichment decision deferred)

```json
{
  "action": "create",
  "sd_id_suggested": "sleep-cadence-pe-driven-upregulation",
  "title": "PE/novelty-driven scaling of offline-update resources (adaptive sleep cadence)",
  "implementation_hint": "Add a wake-phase prediction-error / MEL accumulator that scales the AMOUNT (depth/count) of the subsequent offline phase, so SWS-write and REM-rollout budgets vary with preceding-wake novelty instead of being fixed by sleep_interval. Likely an enrichment of the existing sleep cluster (MECH-272 routing gate / MECH-285 replay sampler) rather than a wholly new module.",
  "unblocks_claims": ["MECH-180"],
  "depends_on_unresolved": ["INV-050", "MECH-121", "MECH-285 (replay sampler, queued)"],
  "priority_suggested": 3,
  "failure_record_entry": {
    "run_id": "v3_exq_677_mech180_novelty_sleep_upregulation_probe_20260613T161241Z_v3",
    "experiment_type": "v3_exq_677_mech180_novelty_sleep_upregulation_probe",
    "metric": "SWS/REM upregulation ratio HIGH/LOW = 1.0 (zero variance; scheduler-fixed counts)",
    "target": "ratio >= 1.25 with a non-degenerate (variance-bearing) adaptive sleep-resource metric"
  }
}
```

`pending_retest_after_substrate: true`. No remaining "supports" to check for narrow-pathway illusion (MECH-180 had zero genuine experiments before this run).
