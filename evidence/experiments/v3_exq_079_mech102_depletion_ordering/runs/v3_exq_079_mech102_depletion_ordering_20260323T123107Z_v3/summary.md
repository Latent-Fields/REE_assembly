# V3-EXQ-079 -- MECH-102 Depletion Ordering

**Status:** FAIL
**Claims:** MECH-102
**Backlog:** EVB-0013
**Decision:** hybridize
**Seeds:** [42, 7]
**alpha_world:** 0.9  (SD-008)
**Warmup:** 400 eps  **Eval:** 60 eps x 2 policies

## Discriminative Pair

| Condition | grid | hazards | density |
|-----------|------|---------|--------|
| SPARSE    | 10x10 | 2     | ~2%    |
| DENSE     | 7x7   | 8     | ~16%   |

## Results

| Metric | SPARSE | DENSE |
|--------|--------|-------|
| contact_rate_ethical | 0.0012 | 0.0039 |
| contact_rate_random  | 0.0572 | 0.1580 |
| contact_rate_reduction | 0.979 | 0.975 |

Anticipatory signal (DENSE, n_ethical_contacts=83):
- precontact_ethical: 0.7796
- precontact_random:  0.7851
- baseline_ethical:   0.7767
- anticipatory_delta: +0.0029
- ethical_vs_random:  -0.0054

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: reduction_sparse > 0.70 | PASS | 0.979 |
| C2: reduction_dense > 0.25  | PASS | 0.975 |
| C3: anticipatory_delta > 0.01 | FAIL | +0.0029 |
| C4: ethical_vs_random > 0.005 | FAIL | -0.0054 |

Criteria met: 2/4 -> **FAIL**

## Per-Seed (SPARSE)

  seed=42: reduction=0.978 ethical_rate=0.0013 random_rate=0.0590 anticipatory_delta=+0.0109 n_ethical=15
  seed=7: reduction=0.980 ethical_rate=0.0011 random_rate=0.0554 anticipatory_delta=+0.0009 n_ethical=13

## Per-Seed (DENSE)

  seed=42: reduction=0.975 ethical_rate=0.0041 random_rate=0.1646 anticipatory_delta=-0.0023 n_ethical=42
  seed=7: reduction=0.975 ethical_rate=0.0037 random_rate=0.1515 anticipatory_delta=+0.0080 n_ethical=41

## Failure Notes

- C3 FAIL: anticipatory_delta=+0.0029 <= 0.01. Harm_eval is not elevated before ethical contacts. Agent may be committing to contact without cost-awareness build-up (surprise vs anticipation).
- C4 FAIL: ethical_vs_random=-0.0054 <= 0.005. Ethical contacts show no more anticipation than random contacts. Last-resort distinction absent -- contacts are equally accidental.
