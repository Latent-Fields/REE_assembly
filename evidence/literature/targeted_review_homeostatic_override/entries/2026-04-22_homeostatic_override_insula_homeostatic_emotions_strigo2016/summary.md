# Strigo & Craig 2016 -- Interoception and Homeostatic Emotions

## Source
Strigo IA, Craig ADB. "Interoception, homeostatic emotions and sympathovagal balance." Phil Trans R Soc B 2016. DOI: 10.1098/rstb.2016.0010

## Key claim
Homeostatic emotions (hunger, thirst, pain, dyspnoea, temperature, fatigue) constitute a unified class routed through posterior-to-anterior insular re-representation. Sympathovagal balance provides a common autonomic substrate that lets these emotions be compared for arbitration.

## Why this matters for REE V3
Two architectural implications:
1. z_harm and drive_level should not be modeled as fully orthogonal channels. They share substrate (homeostatic emotion class) and need to be commensurable for cross-drive arbitration.
2. SD-032a SalienceCoordinator should operate on a common-currency representation, not just compare independent channel magnitudes. The biology suggests there is one such currency (sympathovagal axis or its central analog).

## Failure signatures supporting REE
- **Multi-source integration**: All homeostatic emotions converge in insular cortex. Supports broadcast/integration architecture, not silo'd per-modality processing.
- **Common-currency arbitration**: The fact that the brain HAS a common currency means cross-drive comparisons are computationally tractable. SD-032a arbitration is biologically realisable.

## Caveats
- Architectural-organising-principle level, not specific circuit prediction.
- Insular hierarchy as organising substrate is not explicitly modeled in V3.
