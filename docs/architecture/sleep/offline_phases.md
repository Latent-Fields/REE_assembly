# Offline Phase Architecture

This file documents the four sub-phases of REE's offline consolidation mode (MECH-030).

Sub-phases are V4 scope. This document serves as the location anchor for claims.

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
