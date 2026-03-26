# SD-010: Harm Stream Separation

**Claim ID:** SD-010
**Subject:** `harm_stream.nociceptive_separation`
**Status:** Implemented
**Registered:** 2026-03-19 (after V2 governance cycle)
**Implemented:** 2026-03-20 (EXQ-056c/058b/059c PASS)
**Depends on:** SD-005, SD-007, ARC-027

---

## Problem

After SD-005 introduced the z_self/z_world split, E3 was still evaluating harm via z_world.
This caused two inseparable problems:

1. **Residue contamination:** ResidueField accumulates `world_delta` to track causal footprint.
   If z_world also encodes harm proximity, the residue field becomes a harm-proximity map rather
   than a causal-attribution map. These are different things — the agent may cause no harm in a
   hazard-dense environment, and may cause significant harm in a sparse one.

2. **Counterfactual collapse:** SD-003 self-attribution requires `E2.world_forward(z_world, a_cf)`
   to predict how world-state changes under a counterfactual action. This only works if z_world
   tracks world structure, not harm. E2 cannot simultaneously predict world-state dynamics
   AND harm proximity from a single z_world signal.

3. **Reafference interference:** SD-007 applies a perspective-correction to z_world
   (subtract agent-caused optical-flow change). Harm proximity is agent-relative by definition —
   applying reafference correction to a harm signal would incorrectly subtract the agent's approach
   to a hazard from the harm signal, reducing the harm estimate as the agent gets closer. This is
   backwards.

Root cause cluster: EXQ-027b (reafference over-correction), EXQ-043/044 (calibration collapse),
EXQ-047 (SD-005 calibration shortfall) all traced back to fused z_world carrying harm signal.

---

## Solution

Dedicated harm sensory pathway, independent of z_world processing:

```python
# CausalGridWorldV2 observation dict
{
    "body_state":   [...],   # proprioceptive -> z_self encoder
    "world_state":  [...],   # exteroceptive -> z_world encoder (NO harm included)
    "harm_obs":     [...]    # harm proximity -> HarmEncoder -> z_harm (SD-010)
}

# LatentStack.encode() produces:
LatentState(
    z_self   = self_encoder(body_state),
    z_world  = world_encoder(world_state),   # clean; no harm contamination
    z_harm   = harm_encoder(harm_obs),        # SD-010: dedicated harm stream
    ...
)
```

`HarmEncoder` is a lightweight MLP trained with direct supervision on proximity labels.
`E3.harm_eval(z_harm)` takes z_harm as primary input — NOT z_world.
Reafference correction (SD-007) applies only to z_world; z_harm is explicitly excluded.

---

## Implementation Notes

**CausalGridWorldV2** (`ree_core/environment/causal_grid_world.py`):
- Emits `harm_obs` channel alongside `world_state`
- `harm_obs` = proximity-weighted hazard density in agent field of view
- Ground truth label: `transition_type ∈ {agent_caused_hazard, env_caused_hazard, resource, none}`
  (preserved from V2; still used for SD-003 attribution evaluation)

**HarmEncoder** (`ree_core/latent/stack.py`):
- `HarmEncoder(harm_obs_dim → harm_dim)`
- Trained on proximity labels (supervised, not reconstruction)
- No reafference correction applied

**E3Selector** (`ree_core/predictors/e3_selector.py`):
- `harm_eval(z_harm: Tensor) → Tensor` — primary harm assessment method
- Dynamic precision: `precision = running_mean(E3_prediction_error_variance)` over z_harm
- Commit threshold derived from precision (ARC-016)

---

## What SD-010 Enables

- **Clean z_world for residue:** ResidueField now accumulates `world_delta` (actual causal
  footprint) without harm-proximity contamination.
- **SD-003 counterfactual on world stream:** `E2.world_forward(z_world, a_cf)` is now
  interpretable — it predicts how world structure changes, not how harm changes.
- **ARC-016 dynamic precision:** E3 prediction error variance over z_harm is a meaningful signal
  for commit threshold adjustment.
- **Precondition for SD-011:** SD-010 defines the single z_harm stream. SD-011 splits it into
  z_harm_s (sensory-discriminative) + z_harm_a (affective-motivational).

---

## Evidence

| Experiment | Outcome | Criteria met | Notes |
|---|---|---|---|
| EXQ-058b | PASS | 5/5 | ARC-027 foundational validation. Pearson r_z_harm high. |
| EXQ-056c | PASS | 4/5 | SD-010 reafference isolation retest. r_z_harm=0.914. Clean separation confirmed. |
| EXQ-059c | PASS | 4/5 | MECH-102 via SD-010. contact_rate_reduction ~10x. Approach-gradient avoidance confirmed. |

Prior experiments (EXQ-027b, EXQ-043, EXQ-044, EXQ-047) FAILed and traced back to fused z_world
as root cause. SD-010 resolved all three FAIL clusters.

---

## What SD-010 Does NOT Solve

SD-010 implements a single z_harm stream. This single stream conflates two neurobiologically
incommensurable signals:
- Sensory-discriminative harm (immediate proximity/intensity — forward-predictable)
- Affective-motivational harm (accumulated homeostatic deviation — integrative, NOT predictable)

Consequence: the SD-003 counterfactual redesign requires SD-011 (dual nociceptive streams) because
`HarmBridge(z_world → z_harm)` has bridge_r2=0 (z_world ⊥ z_harm by SD-010 design — architectural
impossibility confirmed by EXQ-093/094). See `sd_011_dual_nociceptive_streams.md`.

---

## Related Claims

- **SD-010** — this design decision
- **ARC-027** — harm stream as dedicated sensory pathway (architectural requirement)
- **SD-011** — dual nociceptive stream extension (PENDING)
- **ARC-033** — SD-003 counterfactual requires E2_harm_s forward model (PENDING)
- **MECH-102** — approach-gradient harm avoidance (validated via SD-010)
- **ARC-016** — dynamic precision from E3 prediction error
- **SD-005** — z_self/z_world split (prerequisite)
- **SD-007** — reafference correction (co-designed; does NOT apply to z_harm)
