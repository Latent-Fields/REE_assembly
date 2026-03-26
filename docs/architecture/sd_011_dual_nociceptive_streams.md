# SD-011: Dual Nociceptive Streams

**Claim ID:** SD-011
**Subject:** `harm_stream.dual_nociceptive_streams`
**Status:** PENDING — current primary implementation bottleneck
**Registered:** 2026-03-24
**Depends on:** SD-010, ARC-027
**Blocks:** SD-003 redesign (EXQ-093/094 confirmed infeasibility of z_world → z_harm bridge)

---

## Problem

SD-010 introduced a single z_harm stream (harm proximity → HarmEncoder → z_harm). This resolves
the z_world contamination problem but reveals a second-order problem: a single z_harm stream
conflates two neurobiologically incommensurable nociceptive pathways (Melzack & Casey 1968;
Craig 2002/2009).

### Neurobiological Dissociation

The two-pathway model is experimentally confirmed by Rainville et al. (1997, *Science*) — the
gold-standard dissociation study. Hypnotic modulation of unpleasantness selectively modulates
ACC (affective-motivational pathway) without affecting S1 (sensory-discriminative). The two
pathways produce different neural signatures, different clinical presentations, and different
behavioral functions.

| Property | z_harm_s (sensory-discriminative) | z_harm_a (affective-motivational) |
|---|---|---|
| Biological analog | Lateral spinothalamic tract → VPL → S1/S2 | Medial pathway → CM/PF → ACC/insula/amygdala |
| Fiber type | A-delta (fast, sharp, localized) | C-fiber (slow, diffuse, persistent) |
| Signal content | Immediate proximity/intensity | Accumulated homeostatic deviation / unpleasantness |
| Temporal dynamics | Fast, discriminative | Slow, integrative (EMA tau ≈ 10–30 steps) |
| Forward-predictable? | YES — moving away from hazard reduces proximity | NO — accumulated deviation does not reverse quickly |
| Role in SD-003 | Counterfactual attribution target | NOT used in counterfactuals |
| Role in E3 | Input to harm attribution | Input to commit urgency / motivational gating |

### Why EXQ-093/094 Found bridge_r2=0

SD-010 places z_world ⊥ z_harm by design — the harm stream is explicitly separated from world
processing. Consequently, `HarmBridge(z_world → z_harm)` is architecturally infeasible:
z_world has no information about harm proximity, by construction.

EXQ-093 FAIL (bridge_r2=0) and EXQ-094 FAIL (100x regression) confirmed this.
**This is not a bug and not fixable by architecture tuning.** The SD-003 counterfactual must be
redesigned to operate within the harm stream, not across the z_world/z_harm boundary.

---

## Solution

Split z_harm into two dedicated streams:

```
harm_obs_s (immediate proximity) → HarmEncoderS → z_harm_s   [sensory-discriminative]
harm_obs_a (EMA accumulator)     → HarmEncoderA → z_harm_a   [affective-motivational]
```

### Required Implementation Changes

**(a) CausalGridWorldV2** — add `harm_obs_a`:
```python
# Alongside existing harm_obs (renamed harm_obs_s):
harm_obs_a = EMA(harm_obs_s, tau=10-30_steps)   # accumulated homeostatic deviation
```

**(b) HarmEncoderS + HarmEncoderA:**
```python
z_harm_s = HarmEncoderS(harm_obs_s)   # rename current HarmEncoder
z_harm_a = HarmEncoderA(harm_obs_a)   # new; trains on accumulated harm signal
```

**(c) LatentState** — add z_harm_a field:
```python
@dataclass
class LatentState:
    z_self:   Tensor   # proprioceptive / interoceptive
    z_world:  Tensor   # exteroceptive world model
    z_harm_s: Tensor   # sensory-discriminative harm (SD-010/011)
    z_harm_a: Tensor   # affective-motivational harm (SD-011)
    z_beta:   Tensor   # affective latent (shared)
    ...
```

**(d) E2_harm_s** — new forward model (ARC-033):
```python
class E2HarmS:
    def forward(self, z_harm_s: Tensor, a: Tensor) -> Tensor:
        """Predict z_harm_s at next step: moving away from hazard reduces proximity."""
```
This is the correct SD-003 counterfactual mechanism. Architecture mirrors `E2.world_forward`.

**(e) E3Selector** — separate inputs:
```python
# Attribution (SD-003 redesign):
z_harm_s_actual = E2_harm_s(z_harm_s, a_actual)
z_harm_s_cf     = E2_harm_s(z_harm_s, a_cf)
causal_sig = harm_eval(z_harm_s_actual) - harm_eval(z_harm_s_cf)

# Commit gating (ARC-016 / motivational urgency):
urgency = E3.urgency_from_affective(z_harm_a)   # accumulated threat state scales commit threshold
```

---

## SD-003 Redesign After SD-011

The SD-003 counterfactual pipeline validated at EXQ-030b (world_forward_r2=0.947) confirmed
the counterfactual architecture is sound. It must now be applied to z_harm_s specifically:

```python
# OLD (pre SD-010): operated on z_world -- no longer valid
z_world_cf  = E2.world_forward(z_world, a_cf)
causal_sig  = E3.harm_eval(z_world_actual) - E3.harm_eval(z_world_cf)

# NEW (post SD-011): operates on z_harm_s
z_harm_s_cf = E2_harm_s(z_harm_s, a_cf)
causal_sig  = E3.harm_eval(z_harm_s_actual) - E3.harm_eval(z_harm_s_cf)
```

**Critical constraint:** Do NOT attempt `HarmBridge(z_world → z_harm_s)` counterfactuals.
bridge_r2=0 is architectural (z_world ⊥ z_harm by SD-010 design). EXQ-093/094 confirmed this.

---

## What SD-011 Enables

- **SD-003 counterfactual**: E2_harm_s provides a learnable forward model on z_harm_s; the
  counterfactual pipeline is now complete within the harm stream
- **ARC-016 dynamic precision via z_harm_a**: accumulated threat state (`z_harm_a` variance)
  provides a biologically grounded signal for commit threshold scaling — more precisely than
  the previous z_world-derived precision
- **MECH-112 wanting/liking balance**: z_harm_a as affective urgency stream pairs with z_goal
  (wanting/approach) for D1/D2 balance in ARC-030
- **INV-007 (language cannot override harm)**: z_harm_a as a separate persistent channel that
  is not subject to linguistic modulation or reafference correction

---

## Experiments Blocked by SD-011 Absence

The following experiments have FAILed primarily because the single z_harm stream is insufficient
for the SD-003 counterfactual redesign or for separating attribution from motivational gating:
EXQ-093, EXQ-094, and approximately 10 additional EXQ numbers pending SD-011 implementation.

These will be re-queued after SD-011 implementation with appropriate `"supersedes"` fields.

---

## Related Claims

- **SD-011** — this design decision
- **SD-010** — prerequisite (single harm stream that SD-011 splits)
- **ARC-027** — harm stream as dedicated sensory pathway
- **ARC-033** — E2_harm_s forward model for SD-003 counterfactual
- **SD-003** — self-attribution counterfactual (redesign target)
- **ARC-016** — dynamic precision (benefits from z_harm_a as urgency signal)
- **ARC-030** — D1/D2 approach-avoidance balance (z_harm_a as avoidance channel)
- **MECH-112** — wanting/liking dissociation (z_harm_a as affective counterpart)

## References

- Melzack & Casey (1968): Gate control theory — discriminative vs affective pain
- Craig (2002, 2009): Interoceptive cortex, affective-motivational pain in ACC/insula
- Rainville et al. (1997, *Science*): Hypnotic modulation of unpleasantness modulates ACC,
  not S1 — gold-standard dissociation between the two pathways
