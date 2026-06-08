# Provisional failure-autopsy scaffold: V3-EXQ-603i

**Date:** 2026-06-08  
**Status:** provisional / manual scaffold / not governance-applied  
**Experiment:** V3-EXQ-603i — relief/safety escape-affordance bridge validation  
**Result:** FAIL  
**Route:** `substrate_not_ready_requeue`  
**Evidence direction:** `non_contributory`  
**Claim effect:** do **not** weaken SD-059 / MECH-358; do **not** validate SD-059 / MECH-358  
**Return required:** yes — run a formal failure autopsy and biological-fidelity review when local token/compute budget allows.  
**Routing update:** the initial human placeholder sequence (`603j/603k/603l`) was superseded by the actual new-number readiness diagnostic `V3-EXQ-653`; do not treat those placeholder suffixes as queued experiment identities.

## Purpose

This note preserves the interpretation of V3-EXQ-603i until the formal failure-autopsy machinery can be run. It is deliberately not a governance-applied autopsy. It should not promote, weaken, or validate any claim.

## Executive interpretation

V3-EXQ-603i did not falsify the relief/safety escape-affordance bridge.

It failed before the bridge could be meaningfully adjudicated.

The base defensive chain was present: Pavlovian freezing and the instrumental-avoidance gate engaged. The goal-formation positive control also passed. However, the bridge did not produce survival improvement and did not meet its non-vacuity requirement. The result therefore points to a missing prerequisite substrate: a trained state-action-threat representation capable of supporting escape affordance credit.

Plain reading:

```text
The bridge may be conceptually right, but the organism cannot yet represent “where out is.”
```

## Known facts from the 603i manifest

### Base defensive substrate engaged

The base arm showed that the 603h chain was present:

```text
pag_freeze_and_ilpfc_gate_engage_on_base = met
measured = 1.0
threshold = 0.666...
```

Interpretation:
- Pavlovian threat response was not inert.
- The instrumental-avoidance gate was not inert.
- The failure is not simply “the defensive stack is disconnected.”

### Goal formation was not the primary failure

The Stage-0 forced-feed goal positive control passed:

```text
stage0_forced_feed_lights_zgoal_on_base = met
measured = 0.666...
threshold = 0.666...
```

Interpretation:
- The goal pipeline can still light under controlled conditions.
- 603i should not be read as a primary goal-formation failure.

### Bridge non-vacuity failed

The load-bearing failed precondition was:

```text
each_enabled_bridge_half_fires_nonvacuously = unmet
measured = 0.0
threshold = 0.666...
```

Interpretation:
- The relief/safety bridge could not be tested as intended.
- The detector/credit mechanism starved.
- The manifest routes this to `substrate_not_ready_requeue`, not bridge falsification.

### Survival did not improve

The key bridge and control outcomes were:

```text
primary_pass = false
best_bridge_g_h_frac = 0.0
best_bridge_clears = false
best_bridge_beats_base = false
readiness_met = false
bridge_halves_nonvacuous = false
nav_control_clears = false
relief_clears = false
safety_clears = false
both_clears = false
```

Interpretation:
- Fixed relief/safety bridge did not rescue hazard-stage survival.
- Safety did not fire.
- Relief fired in some arms/seeds but did not translate into survival.
- Navigation-control also failed, pointing to a navigation/survival-competence ceiling.

## Provisional diagnosis

The missing substrate is not simply:

```text
more relief gain
more safety gain
higher E3 bias
longer budget
```

The missing substrate is more likely:

```text
post-603i escape-affordance linkage over action-consequence structure
```

This should probably reuse existing E2 / cerebellar-analogue action-consequence prediction rather than duplicate a new fast predictor immediately. The current working hypothesis is:

```text
E2 predicts.
Hippocampus indexes viability.
Relief/safety label the consequence.
E3 selects under bounded threat-gated bias.
```

This reuse-vs-duplicate decision remains a revisitable biological-fidelity bet. If a trained discriminative E2 still cannot support escape-vs-harm-worsening discrimination, or if escape prediction interferes with E2’s primary world-transition objective, a dedicated escape-specialised predictive circuit may be biologically justified.

## Biological-fidelity questions to return to

A future formal autopsy / biological-fidelity review should check:

```text
- Does the interpretation preserve the distinction between Pavlovian threat response and instrumental avoidance?
- Does it distinguish freeze suppression from directed escape?
- Does it distinguish relief from safety?
- Does it distinguish relief/safety heads from the representation substrate they require?
- Does it avoid collapsing safety into low harm?
- Does it avoid crediting no-op/freeze as escape?
- Does it correctly place fast prediction in E2 / cerebellar forward modelling rather than duplicating it prematurely?
- Does it correctly place path/route viability in hippocampal indexing rather than in the affect heads?
- Does it identify whether the missing substrate is local escape affordance, broader navigation, or hippocampal relational mapping?
- Does the reuse-E2 bet hold, or does biology/experiment require a dedicated duplicated-motif escape predictor?
```

## Build implication already taken

The immediate post-603i implementation should be treated as a prerequisite scaffold, not validation:

```text
post-603i E2 escape-affordance linkage
    ↓
readout over detached E2 action-consequence features
    ↓
optional features for trainable relief/safety heads
    ↓
bounded threat-gated E3 bias
```

The immediate readiness diagnostic was subsequently allocated a **new experiment identity**, `V3-EXQ-653`, because it tested a new substrate module rather than directly rerunning the 603 behavioural bridge test. Its queue commit reports `linker_readout_ready` after strict validation, dry-run, and 3-seed full-budget gate checks.

## Current successor route after V3-EXQ-653

```text
V3-EXQ-603i:
    fixed arithmetic relief/safety bridge could not be adjudicated;
    route = substrate_not_ready_requeue.

V3-EXQ-653:
    new-number E2 escape-affordance linker/readout readiness microdiagnostic;
    claim_ids = [];
    reported linker_readout_ready.

Next local /queue-experiment step:
    queue the next available V3-EXQ as a 603-lineage full behavioural bridge re-test
    with E2 escape-affordance linker features attached to the trainable relief/safety heads.
```

A handoff request for that next local queue step is recorded at:

```text
REE_assembly/evidence/planning/queue_request_post_653_603_lineage_full_bridge_retest_2026-06-08.md
```

## Governance note

This note is a provisional interpretation scaffold only. It is not a reviewed failure autopsy. It has no queue effect, no confidence effect, and no claim-status effect. It exists so that a future formal autopsy can compare against the preserved interpretation rather than reconstructing it from chat context.
