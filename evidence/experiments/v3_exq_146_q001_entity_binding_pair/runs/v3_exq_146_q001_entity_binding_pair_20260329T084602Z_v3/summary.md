# V3-EXQ-146 -- Q-001 Entity Emergence and Binding Discriminative Pair

**Status:** FAIL
**Claims:** Q-001
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** ENTITY_BINDING_ON vs ENTITY_ABLATED
**Warmup:** 300 eps x 200 steps  **Eval:** 100 eps x 200 steps
**Env:** CausalGridWorldV2 size=10, 3 hazards, 4 resources nav_bias=0.35

## Design

Q-001 asks what mechanisms produce entity emergence and binding in the REE latent stack. The candidate mechanism under test: z_self attentional gating (self-maintenance active) enables entity persistence in z_world by focusing world encoder attention on entity-linked features (ARC-006).

ENTITY_BINDING_ON: z_self active, self_maintenance_weight=0.1.
ENTITY_ABLATED: z_self zeroed after each sense() call, maint_weight=0.0.
Entity events: |mean(delta_obs_world)| > 0.02 (hazard drift steps from CausalGridWorldV2 env_drift_prob=0.3).

## Pre-Registered Thresholds

C1: BINDING entity_event_response >= 0.05 (both seeds)
C2: ABLATED entity_event_response <= 0.15 (both seeds)
C3: per-seed event_response gap (BINDING-ABLATED) >= 0.02 (both seeds)
C4: BINDING entity_tracking_persistence >= 0.7 (both seeds)
C5: per-seed persistence gap (BINDING-ABLATED) >= 0.05 (both seeds)

## Results

| Condition | event_response | event_snr | persistence | baseline_delta |
|-----------|----------------|-----------|-------------|----------------|
| ENTITY_BINDING_ON | 0.0431 | 1.999 | 0.9999 | 0.0217 |
| ENTITY_ABLATED    | 0.0431 | 1.999 | 0.9999 | -- |

**Per-seed event_response gap (BINDING - ABLATED): [0.0, 0.0]**
**Per-seed persistence gap (BINDING - ABLATED): [0.0, 0.0]**

### ENTITY_BINDING_ON per seed
  seed=42: event_response=0.0435 snr=2.168 persistence=0.9999 baseline_delta=0.0201 n_events=1349
  seed=123: event_response=0.0427 snr=1.831 persistence=0.9999 baseline_delta=0.0233 n_events=1317

### ENTITY_ABLATED per seed
  seed=42: event_response=0.0435 snr=2.168 persistence=0.9999 baseline_delta=0.0201 n_events=1349
  seed=123: event_response=0.0427 snr=1.831 persistence=0.9999 baseline_delta=0.0233 n_events=1317

## PASS Criteria

| Criterion | Result |
|-----------|--------|
| C1: BINDING event_response >= 0.05 (both seeds) | FAIL |
| C2: ABLATED event_response <= 0.15 (both seeds) | PASS |
| C3: event_response_gap(BINDING-ABLATED) >= 0.02 (both seeds) | FAIL |
| C4: BINDING persistence >= 0.7 (both seeds) | PASS |
| C5: persistence_gap(BINDING-ABLATED) >= 0.05 (both seeds) | FAIL |

Criteria met: 2/5 -> **FAIL**

## Interpretation

Q-001 BINDING MECHANISM NOT CONFIRMED: z_self attentional gating does NOT produce detectable improvements in entity event responsiveness or persistence. event_response: BINDING=0.0431 vs ABLATED=0.0431. persistence: BINDING=0.9999 vs ABLATED=0.9999. Only 2/5 criteria met. The current V3 architecture's entity binding may emerge primarily from world-encoder temporal dynamics (alpha_world EMA + event contrastive supervision) rather than z_self attentional gating. This constrains Q-001's answer: binding in this architecture is encoder-internal, not z_self-gated.

## Failure Notes

- C1 FAIL: BINDING event_response [0.0435, 0.0427] < 0.05 -- even with z_self active, world encoder does not respond to entity events; check EVENT_DELTA_THRESH (may be too large for this env's drift amplitude), or increase nav_bias so agent encounters hazard events more frequently.
- C3 FAIL: event_response_gap [0.0, 0.0] < 0.02 -- z_self ablation has minimal effect on entity responsiveness; z_self is not the dominant attentional gate for entity binding; consider that entity emergence may be primarily a world-encoder-internal mechanism (temporal EMA + event contrastive supervision from SD-009).
- C5 FAIL: persistence_gap [0.0, 0.0] < 0.05 -- persistence improvement from z_self gating is below threshold; world encoder EMA may already produce most available persistence.
