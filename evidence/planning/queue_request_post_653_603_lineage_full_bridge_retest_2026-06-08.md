# Queue request: post-653 return to 603-lineage full behavioural bridge retest

**Date:** 2026-06-08  
**Status:** queue-request / handoff only / not queued by this note  
**Reason for handoff:** ChatGPT GitHub connector can write repository files but cannot run the local `/queue-experiment` skill, validators, dry-runs, or full-budget smoke checks. This note preserves the exact intended queue request for a local agent/session to apply.

## Context

V3-EXQ-603i landed as `FAIL` with route `substrate_not_ready_requeue`, `evidence_direction = non_contributory`, and no claim weakening. It showed that the fixed relief/safety escape-affordance bridge could not be adjudicated because the upstream representation/linkage for "where out is" under threat was not ready.

V3-EXQ-653 then queued and locally smoke-tested a new-number, claim-free readiness microdiagnostic for the post-603i E2 escape-affordance linker/readout. The 653 queue commit reports:

```text
validate_experiments --strict OK
--dry-run PASS
3-seed full-budget gate check all gates 3/3
label = linker_readout_ready
```

Therefore the correct next step is to return to the 603 behavioural lineage, but only as a full behavioural re-test **using the linker substrate confirmed by 653**, not as a re-run of the original fixed arithmetic bridge alone.

## Queue request prompt

```text
/queue-experiment

Queue the next available V3-EXQ experiment as a 603-lineage full behavioural bridge re-test after V3-EXQ-653 readiness PASS.

Do not reuse the 653 number. Do not necessarily call this 603j unless the queue system convention says full behavioural re-tests inside a lineage keep the 603 stem. It should explicitly reference:
- originating failure: V3-EXQ-603i
- substrate-readiness dependency: V3-EXQ-653 linker_readout_ready
- lineage: V3-EXQ-603 SD-054 scaffolded onboarding / hazard-survival / relief-safety escape-affordance bridge lineage

Working title:
Post-653 603-lineage full behavioural relief/safety bridge re-test with E2 escape-affordance linker features

Purpose:
V3-EXQ-603i could not adjudicate the relief/safety bridge because upstream escape-affordance representation was not ready. V3-EXQ-653 has now shown, in a controlled forced-choice microdiagnostic, that the post-603i E2 escape-affordance linker/readout can learn a controlled "where out is" signal and expose bounded threat-gated bias. This experiment returns to the full 603 behavioural Stage-H / scaffolded SD-054 context to test whether the linker-enabled trainable relief/safety pathway can now improve hazard-stage survival.

Claim handling:
- claim_ids = [] unless governance has explicitly registered a new linker/bridge claim before queuing.
- Diagnostic / substrate-integration test.
- Do not validate SD-059 / MECH-358 automatically.
- Do not weaken SD-059 / MECH-358 automatically.
- Do not validate or weaken MECH-302 / MECH-303 / MECH-304 automatically.
- PASS is not V3 closure by itself.
- FAIL is not bridge falsification unless readiness/non-vacuity gates are met and failure routing says so.

References:
- REE_assembly/evidence/planning/provisional_failure_autopsy_V3-EXQ-603i_2026-06-08.md
- ree-v3/docs/substrate_plans/post_603i_e2_escape_affordance_linkage.md
- ree-v3/experiments/v3_exq_653_e2_escape_affordance_linker_readiness_microdiagnostic.py
- ree-v3/experiments/v3_exq_603i_escape_affordance_bridge_validation.py
- ree-v3/ree_core/pfc/e2_escape_affordance_linker.py
- ree-v3/ree_core/pfc/trainable_escape_affordance_learner.py

Architecture to preserve:
E2 predicts.
Hippocampus indexes viability.
Relief/safety label the consequence.
E3 selects under bounded threat-gated bias.

The run must not create a new standalone fast predictor. It should use the post-603i E2EscapeAffordanceLinker and TrainableEscapeAffordanceLearner surfaces already present in ree-v3.

Suggested implementation:
Create a new experiment script by copying/adapting V3-EXQ-603i rather than modifying 603i in place.

Suggested script name:
experiments/v3_exq_<NEW>_post653_603_lineage_linker_bridge_retest.py

Use the same scaffolded SD-054 / Stage-H behavioural structure as V3-EXQ-603i unless local validators require a narrower budget. Keep the same seeds [42, 43, 44] unless standard queue policy says otherwise.

Suggested arms:

1. ARM_BASE_IA_ONLY
   - SD-058 / MECH-357 instrumental-avoidance gate ON
   - PAG freeze gate ON
   - fixed arithmetic bridge OFF
   - trainable relief/safety learner OFF
   - E2 escape-affordance linker OFF
   Purpose: baseline 603h/603i-style action-release without directed escape learning.

2. ARM_TRAINABLE_HEADS_COMPACT_ONLY
   - trainable relief/safety learner ON
   - E2 escape-affordance linker OFF
   - fixed arithmetic bridge OFF
   Purpose: tests whether trainable relief/safety heads alone, using compact raw features, can lift Stage-H survival.

3. ARM_LINKER_READOUT_E3_BIAS
   - E2 escape-affordance linker ON
   - use_e2_escape_linker_e3_bias ON
   - use_e2_escape_linker_for_relief_safety OFF
   - trainable relief/safety learner OFF
   - fixed arithmetic bridge OFF
   Purpose: tests whether linker/readout viability bias alone can improve hazard survival.

4. ARM_LINKER_TO_TRAINABLE_RELIEF_SAFETY
   - E2 escape-affordance linker ON
   - use_e2_escape_linker_for_relief_safety ON
   - trainable relief/safety learner ON
   - use_e2_escape_linker_e3_bias OFF unless the learner cannot emit E3 bias without it
   - fixed arithmetic bridge OFF
   Purpose: primary biological-composition arm: E2/action-consequence linker provides features; relief/safety heads label; E3 receives bounded bias through the learner.

5. ARM_LINKER_PLUS_HEADS_COMBINED_BIAS
   - E2 escape-affordance linker ON
   - use_e2_escape_linker_for_relief_safety ON
   - use_e2_escape_linker_e3_bias ON
   - trainable relief/safety learner ON
   - fixed arithmetic bridge OFF
   Purpose: optional, only if local review thinks combined bias is safe and interpretable. Tests maximal post-653 integration.

6. ARM_NAV_CONTROL
   - same as V3-EXQ-603i navigation-control positive control
   - bridge/linker/head settings should be chosen deliberately; likely BASE only unless testing whether handed-refuge plus linker changes survival.
   Purpose: distinguish bridge/linker failure from deeper navigation/survival ceiling.

Optional historical comparator if budget allows:
ARM_FIXED_RELIEF_SAFETY_BRIDGE_BOTH
   - original arithmetic EscapeAffordanceBridge both relief+safety ON
   - linker OFF
   - trainable heads OFF
   Purpose: confirm 603i fixed-bridge failure shape remains comparable. Do not include if it makes the experiment too expensive.

Primary gates:
- G0: Stage-0 z_goal positive control passes on >=2/3 seeds.
- G_BASE: PAG/freezing and ilPFC/instrumental-avoidance gate engage on base arm >=2/3 seeds.
- G_LINKER_NV: linker non-vacuity: linker receives E2 feature ticks and optimizer steps / positive escape updates on enabled linker arms >=2/3 seeds.
- G_HEAD_NV: trainable relief/safety learner non-vacuity: optimizer steps and relief/safety targets fire on enabled head arms >=2/3 seeds.
- G_H: hazard-stage survival gate: median last-window episode length over Stage-H >= pre-registered 603i threshold, preferably 75 unless budget changes require explicit amended threshold.
- G_PRIMARY: best post-653 linker/head arm clears G_H in >=2/3 seeds and beats ARM_BASE_IA_ONLY.
- G_NAV: navigation-control interpretation gate, same role as 603i.

Secondary diagnostics:
Record all previous 603i diagnostics plus:
- e2_escape_linker_n_updates
- e2_escape_linker_n_optimizer_steps
- e2_escape_linker_n_positive
- e2_escape_linker_n_negative
- e2_escape_linker_n_noop_skipped
- e2_escape_linker_n_sim_skipped
- e2_escape_linker_n_bias_fires
- e2_escape_linker_n_e2_feature_ticks
- e2_escape_linker_best_class
- e2_escape_linker_max_escape_prediction
- e2_escape_linker_viability_max
- trainable_escape_n_optimizer_steps
- trainable_escape_n_relief_positive
- trainable_escape_n_relief_negative
- trainable_escape_n_safety_positive
- trainable_escape_n_safety_negative
- trainable_escape_n_bias_fires
- trainable_escape_max_relief_prediction
- trainable_escape_max_safety_prediction
- per-arm E3 bias max/mean if available
- per-action first-action distribution if available

Readiness / non-vacuity routing:
If linker-enabled arms do not instantiate, receive E2 features, or optimizer-step:
- route substrate_not_ready_requeue / linker integration wiring failure.

If trainable relief/safety learner enabled arms do not optimizer-step or receive targets:
- route substrate_not_ready_requeue / affect-head non-vacuity failure.

If no-op/freeze receives escape credit:
- route biological-fidelity failure.

If bias fires when safe:
- route threat-gating failure.

If learning occurs under simulation/hypothesis-tag mode:
- route MECH-094 boundary failure.

Outcome interpretation:
PASS:
- A post-653 linker/head arm clears hazard survival >=2/3 and beats base, with linker/head non-vacuity gates met.
- Interpretation: post-603i E2 escape-affordance linkage plus trainable relief/safety pathway can lift the 603 hazard-survival behavioural leg under this scaffold.
- Next route: formal governance/failure-autopsy review before claim changes; then decide whether to mark relevant substrate queue item ready or queue broader SD-054 closure retest.

FAIL with readiness unmet:
- Do not weaken bridge claims.
- Run failure autopsy on this experiment and route to linker wiring / head wiring / feature geometry.

FAIL with readiness met and NAV_CONTROL passes:
- Environment survivable; linker/head bridge insufficient in this scaffold. Run failure autopsy; consider temporal credit, E2 feature geometry, bias authority, relief/safety separation, or duplicated-motif predictor.

FAIL with readiness met and NAV_CONTROL fails:
- Deeper navigation/survival competence ceiling persists. Route to navigation/hippocampal viability mapping rather than further bridge tuning.

Important:
Run local validation before committing:
- validate_experiments --strict
- --dry-run PASS
- arm fingerprint validation
- if possible, one seed smoke before full queue

Do not queue this if the script cannot be generated and validated locally.
```

## Note

This file is a handoff artifact, not an actual queue item. The next local agent/session should use the `/queue-experiment` skill so the script, queue entry, validators, and dry-run are generated together.
