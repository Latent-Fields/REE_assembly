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

## Failure Mode

MECH-124: consolidation-mediated option-space contraction (Walker PTSD analog).
Prevention requires balanced replay scheduling and MECH-094 tag throughout.

## See Also

- `v3_v4_transition_boundary.md` -- V3 static setpoints and V4 dynamic mechanisms
- `default_mode.md` -- MECH-092 quiescent replay (V3 prerequisite for all sub-phases)
- `control_plane_heartbeat.md` -- MECH-089 ThetaBuffer (V3 scaffolding for MECH-122)
