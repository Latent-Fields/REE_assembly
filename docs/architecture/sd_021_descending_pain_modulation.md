# SD-021: Descending Pain Modulation — Commitment-Gated z_harm_s Attenuation

**Status:** candidate  
**Implementation phase:** v3  
**Implemented:** 2026-04-10  
**Depends on:** SD-011, SD-020, ARC-016, MECH-090  
**Unblocks:** MECH-220 (pain-as-control-signal validation)

---

## Claim

When E3 is committed to a trajectory that passes through expected harm (beta_gate elevated,
MECH-090), the sensory-discriminative harm stream `z_harm_s` is precision-downweighted by an
attenuation factor `descending_attenuation_factor`. The affective stream `z_harm_a` is NOT
attenuated — affective load persists through commitment.

This implements the biological descending inhibitory pain modulation pathway:
pgACC → PAG → RVM → dorsal horn. The pathway provides top-down suppression of nociceptive
input during volitional action through expected harm. The agent commits to a trajectory
*because* it has already evaluated the harm; re-weighting the sensory signal during execution
prevents the harm from derailing an already-chosen plan.

---

## Biological Basis

Chen (2023, Front Neural Circuits) documents the descending pain modulatory system as a
precision-weighted control pathway, not a simple suppression gate. The key features:

1. **Selectivity**: Only z_harm_s (sensory-discriminative, A-delta analog) is attenuated.
   z_harm_a (affective-motivational, C-fiber analog) persists. This maps to the clinical
   observation that committed athletes feel pain but are not derailed by it — the motivational
   urgency signal (z_harm_a) persists but the sensory discrimination signal (z_harm_s) is
   gated down.

2. **Commitment-dependence**: The pathway activates during volitional action through known
   hazards, not during passive harm exposure. MECH-090 BetaGate elevation is the REE
   correlate of the committed-action state.

3. **Precision mechanism**: The gate does not eliminate z_harm_s; it reduces its effective
   precision weight. In REE terms this is implemented as a scalar multiplication:
   `z_harm_s_gated = z_harm_s * descending_attenuation_factor` where
   `0 < descending_attenuation_factor < 1`.

---

## Architecture

### Data flow

```
env.harm_obs
    |
    v
HarmEncoder --> z_harm_s (LatentState)
                    |
                    v [if beta_gate.is_elevated AND harm_descending_mod_enabled]
                z_harm_s * descending_attenuation_factor
                    |
                    v
              E3 harm_eval, E2_harm_s forward model
```

`z_harm_a` is unaffected — it flows from `AffectiveHarmEncoder` without attenuation.

### Config parameters (REEConfig)

```python
harm_descending_mod_enabled: bool = False        # master switch (default: off)
descending_attenuation_factor: float = 0.5       # 0=full suppression, 1=no suppression
```

### Implementation location

`ree-v3/ree_core/agent.py`, `REEAgent.sense()`:

```python
if (getattr(self.config, "harm_descending_mod_enabled", False)
        and self.beta_gate.is_elevated
        and new_latent.z_harm is not None):
    attn = getattr(self.config, "descending_attenuation_factor", 0.5)
    new_latent.z_harm = new_latent.z_harm * attn
```

Note: `z_harm` field holds `z_harm_s` (the sensory-discriminative stream). `z_harm_a` is in
`LatentState.z_harm_a` and is not modified.

---

## Validation Experiment (EXQ-325)

**Design:** Two conditions, 200 episodes each, 3 seeds.

- **CONTROL:** `harm_descending_mod_enabled=False` (current behaviour)
- **DESCENDING:** `harm_descending_mod_enabled=True`, `descending_attenuation_factor=0.5`

Both conditions use `limb_damage_enabled=True` (SD-022) to provide a genuine causal harm
stream that is not fully predictable from position alone.

**Metrics:**

| Metric | Target |
|--------|--------|
| `z_harm_s_norm_committed` | < `z_harm_s_norm_uncommitted` (within DESCENDING condition) |
| `z_harm_a_norm_committed` | Not significantly different from `z_harm_a_norm_uncommitted` |
| `benefit_ratio` | DESCENDING >= CONTROL (descending mod should not hurt navigation) |
| `n_committed_steps` | DESCENDING >= CONTROL (committed episodes should not shorten) |

Pass criterion C1: z_harm_s is measurably lower during committed episodes than uncommitted.
Pass criterion C2: z_harm_a shows no corresponding attenuation.
Pass criterion C3: Task performance is maintained or improved (descending mod frees E3 from
re-evaluating already-committed harm).

**Note:** Requires SD-020 (harm surprise PE) to have a well-shaped z_harm_s signal; the
descending attenuation is most interpretable when z_harm_s encodes precision-weighted PE
rather than raw accumulated harm.

---

## Relationship to Other Claims

| Claim | Relationship |
|-------|-------------|
| SD-011 | Provides the dual-stream split; z_harm_s and z_harm_a are separate targets |
| SD-020 | z_harm_s should encode PE (not raw magnitude) before descending attenuation is meaningful |
| ARC-016 | Precision weighting framework; attenuation factor could be precision-scaled in V4 |
| MECH-090 | BetaGate elevation identifies the committed state that triggers attenuation |
| MECH-220 | Downstream claim: pain as control signal; SD-021 is the prerequisite substrate |

---

## Forward Notes

The current implementation applies a fixed scalar `descending_attenuation_factor`. A richer
V4 implementation would modulate this factor dynamically via ARC-016 precision:
`alpha_eff = base_factor * (1 - precision_scale * current_precision / max_precision)`.
Under high-precision (confident) commitment, attenuation would be stronger; under uncertain
commitment, it would be lighter. This is the `harm_nonredundancy_precision_scale` analog
for the descending pathway.
