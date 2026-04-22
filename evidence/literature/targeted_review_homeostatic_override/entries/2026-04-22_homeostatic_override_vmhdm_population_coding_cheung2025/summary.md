# Cheung et al 2025 -- VMHdm Population Coding of Predator Imminence

## Source
Cheung KYM, Kennedy A, Nair A, Anderson DJ. "Population coding of predator imminence in the hypothalamus." Neuron 2025. DOI: 10.1016/j.neuron.2025.02.003

## Key claim
VMHdm population dynamics encode predator imminence as a continuous variable. Two anti-correlated subpopulations within VMHdm encode threat-presence vs threat-absence, with their relative activation tracking how close the predator is.

## Why this matters for REE V3
Two architectural points:
1. z_harm should be continuous (population code) upstream, with threshold conversion at downstream arbiters (consistent with MECH-279).
2. The anti-correlated "safety" subpopulation suggests V3 needs an explicit z_safety channel, not just absence-of-harm. Currently V3 lacks this degree of freedom.

## Failure signatures supporting REE
- **Anti-correlated subpopulations**: VMHdm itself implements a winner-take-all-like arbitration before broadcasting downstream.
- **Continuous coding**: Threat is not binary at the source. Thresholding is a downstream operation.
- **Imminence ramping**: Population activity ramps with imminence rather than switching at a threshold; the switch behaviour is downstream.

## Caveats
- Anti-correlation analysis confined to VMHdm; broader network (PBN, CeA, BNST) not characterised.
- Acute presentation only; sustained-threat dynamics relevant to V3-EXQ-471 not addressed.
