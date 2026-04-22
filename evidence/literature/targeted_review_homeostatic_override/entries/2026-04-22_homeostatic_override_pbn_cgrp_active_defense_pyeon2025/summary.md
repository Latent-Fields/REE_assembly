# Pyeon et al 2025 -- PBN CGRP Active Defense Modulation

## Source
Pyeon Y, Cho J, Chung S, Choi J-H, Jo YS. "Parabrachial CGRP neurons modulate active defensive behavior under a naturalistic threat." eLife 2025. DOI: 10.7554/eLife.101523

## Key claim
PBN CGRP neurons encode threat intensity through firing duration and amplitude in response to a predator-like robot. Bidirectional chemogenetic manipulation amplifies (activation) or blunts (inhibition) active flight responses, with relatively preserved passive freezing.

## Why this matters for REE V3
For MECH-279 (PAG GABAergic freeze gate): PBN CGRP looks like the upstream threat-amplitude sensor that feeds the PAG threshold gate. The continuous-to-discrete conversion (continuous PBN firing -> discrete behavioural mode commit) is the architectural pattern V3 needs at the harm-arbitration boundary.

## Failure signatures supporting REE
- **Continuous upstream, discrete downstream**: PBN CGRP fires continuously with threat intensity, but flight commits at threshold. Two-stage architecture.
- **Gain-modulator, not command**: Bidirectional manipulation modulates rather than commands behaviour. Consistent with broadcast architecture rather than dedicated trigger line.
- **Active vs passive defense dissociation**: Manipulation affects active flight more than passive freeze, suggesting separable downstream channels even from a single upstream source.

## Caveats
- Acute threat only; sustained-threat dynamics (V3-EXQ-471 condition) not characterised.
- Whether PBN CGRP itself decays under sustained threat or is overridden downstream remains open.
