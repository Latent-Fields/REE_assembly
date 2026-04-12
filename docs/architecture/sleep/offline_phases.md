---
nav_exclude: true
---

# Offline Phase Architecture

This file documents REE's offline consolidation phases.

**2026-04-05 roadmap update:** A minimal sleep-phase infrastructure (SD-017) is now **V3 scope**. The four full sub-phases (MECH-120-123) remain V4. See `sd_017_sleep_phase_architecture.md` for the V3 design.

## V3 Minimal Offline Phases (SD-017)

| Phase | Name | Function | Status |
|-------|------|----------|--------|
| SWS-analog | Schema/slot consolidation | Hippocampus-to-cortex replay; installs context templates (slot-formation, MECH-166) | V3 required |
| REM-analog | Causal attribution replay | Fills context slots with co-correlational evidence; slot-filling phase (MECH-166) | V3 required |

## Sub-phases

| Phase | Claim | Biological Analog | V3 Prerequisite |
|---|---|---|---|
| SWS denoising | MECH-120 | Synaptic homeostasis (Tononi SHY) | MECH-094 tag |
| NREM replay | MECH-121 | SWR + spindles + slow oscillation | MECH-092 replay |
| Spindles | MECH-122 | Thalamo-cortical spindle bursts | MECH-089 ThetaBuffer (bidirectional) |
| REM recalibration | MECH-123 | REM precision prior (Hobson/Friston) | MECH-094 tag, ARC-016 |

## Phase Ordering Rationale and V4 Rewiring Specification (INV-045)

The V4 sub-phase sequence is not arbitrary. Each phase is in its position because of what must be true before it can run. This makes the ordering a **V4 engineering constraint**, not a design choice — and each phase directly specifies the rewiring the REE substrate requires.

| Phase | Claim | Failure mode addressed | Why this position | Rewiring required |
|-------|-------|----------------------|-------------------|-------------------|
| 0: Sensory gate | MECH-122 | New input corrupts in-progress schema installation; context templates shift during consolidation | Must be first — nothing downstream can run while perception is live | Input gate on E1 latent stack; ThetaBuffer paused for new observations |
| 1: SHY normalisation | MECH-120 | Replaying into a landscape dominated by recent high-salience experiences reinforces the dominant trace rather than consolidating diverse content | Must precede replay — homeostasis must flatten attractors before replay repopulates them | Normalisation pass over E1/E2/E3 weights decaying toward mean; dominant attractor suppression |
| 2: NREM schema replay | MECH-121 + MECH-165 | You cannot fill context slots that do not exist (INV-044); world model only represents what was done, never what was possible | Must precede REM — schema installation produces the stable attractors that attribution replay fills; replay diversity (MECH-165) must enter the schema now | Hippocampus-to-cortex directed replay; balanced scheduler (forward + reverse + non-dominant paths); ContextMemory templates updated |
| 3: Spindle coordination | MECH-122 | E1 state cannot be consolidated into E3 in reverse direction; ThetaBuffer is waking-only in V3 | After schema is installed, bidirectional packaging transfers E1 updates for long-horizon integration | ThetaBuffer gains reverse-direction mode; theta-packaged E1 updates transferred to hippocampus |
| 4: REM recalibration | MECH-123 | Next waking cycle starts with priors calibrated to the previous episode; early evidence is over/under-weighted | Must be last — resetting precision priors before replay would change how that evidence is weighted during replay | z_beta suppressed (aminergic suppression); E1 runs unconstrained (no harm gate); commitment_threshold and precision_ema_alpha recalibrated from episode natural range |

**Key derivation:** This sequence was not taken from sleep biology. It was derived from asking what an agent needs to reliably know what its actions mean across contexts. The biological NREM→REM sequence converges on the same order because the failure modes are the same. That convergence is evidence for both the biological account and the computational one.

---

## Failure Mode

MECH-124: consolidation-mediated option-space contraction (Walker PTSD analog).
Prevention requires balanced replay scheduling and MECH-094 tag throughout.

## See Also

- `v3_v4_transition_boundary.md` -- V3 static setpoints and V4 dynamic mechanisms
- `default_mode.md` -- MECH-092 quiescent replay (V3 prerequisite for all sub-phases)
- `control_plane_heartbeat.md` -- MECH-089 ThetaBuffer (V3 scaffolding for MECH-122)
- `medications_dementia.md` -- INV-048, MECH-173-177: pharmacological pipeline disruption and disease-modifying predictions
