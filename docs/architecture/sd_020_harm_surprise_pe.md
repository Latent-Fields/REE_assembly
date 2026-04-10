# SD-020: z_harm_a Encodes Affective Surprise (Precision-Weighted PE)

**Claim ID:** SD-020  
**Subject:** harm_stream.affective_surprise_pe  
**Status:** IMPLEMENTED 2026-04-10  
**Registered:** 2026-04-08  
**Depends on:** SD-011, SD-019, ARC-016  
**Blocks:** SD-021 (descending modulation requires PE-based z_harm_a)

---

## Problem

Current `compute_harm_accum_loss()` trains z_harm_a on a raw EMA-accumulated harm scalar.
This makes z_harm_a an integrator of absolute harm state, not a surprise detector.

Chen (2023, Front Neural Circuits) establishes that the anterior insula cortex (AIC) —
the biological analog of z_harm_a — responds to "unsigned intensity prediction errors as
a modality-unspecific aversive surprise signal," not to raw stimulus magnitude.

If z_harm_a encodes raw accumulated harm, E3 urgency responds to sustained-but-expected
threat (which the agent may already be handling) rather than unexpected escalation (which
genuinely requires immediate behavioural change).

---

## Solution

Replace the `compute_harm_accum_loss()` training target from raw `accumulated_harm` to a
**precision-weighted prediction error** signal:

```
harm_PE = |accumulated_harm - _harm_obs_ema|  # unsigned PE
precision_norm = min(e3.current_precision / 500.0, 3.0)  # ARC-016 scaling
surprise_target = harm_PE * precision_norm    # precision-weighted surprise
```

The running EMA `_harm_obs_ema` tracks the agent's expected harm. `harm_PE` is the
unsigned deviation — how surprising the current threat level is. The precision weight
(ARC-016 coupling) scales the surprise signal: when the agent is confident and precise,
unexpected harm is more surprising than in a volatile state.

### Config params (REEConfig)

| Param | Type | Default | Purpose |
|-------|------|---------|---------|
| `harm_surprise_pe_enabled` | bool | `False` | switch (False = legacy EMA target) |
| `harm_obs_ema_alpha` | float | `0.1` | EMA smoothing for expected-harm tracker |

### Agent attribute: `_harm_obs_ema`

Initialised to 0.0. Updated inside `compute_harm_accum_loss()` on each call. Tracks
running expected harm magnitude.

---

## Architecture Context

This is a **loss function modification** — no new modules, no new latent fields. The
AffectiveHarmEncoder and z_harm_a are unchanged; only what they are trained to predict
changes. The modification is gated by `harm_surprise_pe_enabled=False` (default),
preserving backward compatibility.

`harm_history_len > 0` (SD-011 second source) must be enabled for this method to be
non-trivial (the aux head must exist). With `harm_history_len=0`, both legacy and PE-mode
return zero (no aux head exists).

---

## What This SD Enables

- z_harm_a encodes affective surprise rather than absolute state
- E3 urgency responds to unexpected threat escalation (correct biological profile)
- SD-021 (descending modulation) can meaningfully attenuate the PE signal during commitment

---

## Biological Grounding

Chen 2023 (Front Neural Circuits): AIC encodes unsigned intensity PEs as modality-nonspecific
aversive surprise. Not raw magnitude. Seymour (2019, Neuron): pain as RL signal is
precision-weighted. Active inference (Friston 2010): high-level affective representations
encode precision-weighted PEs at the level of homeostatic set-points.

ARC-016 (dynamic precision) provides the biological grounding for the precision weighting:
the precision of the harm-PE signal is E3's confidence about the current state — in
uncertain environments, the same harm magnitude is less surprising because the variance is
already high.

---

## Related Claims

- SD-020 (harm_stream.affective_surprise_pe)
- SD-011 (harm_stream.dual_nociceptive_streams)
- SD-019 (harm_stream.affective_nonredundancy — prerequisite)
- ARC-016 (cognitive_modes.control_plane_regimes — precision coupling)
- MECH-220 (cingulate-insula hub coordination)
- Q-036 (question: PE vs magnitude encoding in z_harm_a)
