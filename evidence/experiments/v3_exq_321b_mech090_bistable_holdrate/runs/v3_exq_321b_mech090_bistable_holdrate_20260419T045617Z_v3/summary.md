# V3-EXQ-321b -- MECH-090: Bistable vs Legacy Gate Hold Rate

**Status:** PASS
**Seeds passing:** 3/3
**Claim:** MECH-090 -- beta gate bistable latch holds commitment without flickering

## Design
Single shared training (LEGACY mode, 400 eps) -> deepcopy into BISTABLE and
LEGACY eval clones. Both clones start with identical trained weights and identical low
running_variance. Gate mode is the ONLY difference.

## Results

| Seed | Bistable hold_rate | Legacy hold_rate | C1 | C2 | C3 | Pass |
|------|-------------------|-----------------|----|----|-----|------|
| 42 | 1.000 | 0.540 | Y | Y | Y | PASS |
| 43 | 1.000 | 0.540 | Y | Y | Y | PASS |
| 44 | 1.000 | 0.520 | Y | Y | Y | PASS |

Mean bistable hold_rate: 1.000
Mean legacy hold_rate:   0.533
