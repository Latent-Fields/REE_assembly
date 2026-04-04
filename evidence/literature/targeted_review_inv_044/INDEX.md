# Targeted Review: INV-044 -- Bayesian Prior-Before-Posterior Necessity

**Claim:** INV-044 -- Approximate Bayesian contextual inference is architecturally impossible to co-compute with online encoding: prior construction (schema formation -- which context distinctions are structurally relevant) must precede posterior inference (attribution -- which evidence belongs to which context slot); a system attempting both online produces a degenerate prior that makes attribution uninformative regardless of training duration.

**Session:** lit-pull-inv044-mech166-arc045-2026-04-05
**Date:** 2026-04-05

## Research Question

Is there computational and neuroscientific evidence that schema formation (prior construction) must precede causal attribution (posterior inference), and that co-computing them in a single online pass produces degenerate context representations?

## Key Questions Addressed

1. Formal computational grounding for prior-before-posterior necessity -- YES (Sanders 2020, hidden state inference framework)
2. Neural substrate of two-stage schema/prior then slot-filling/posterior architecture -- YES (Morton 2020, parahippocampal hierarchy)
3. Causal evidence that prior structure (schema) must be maintained for efficient posterior inference (slot-filling) -- YES (Finnie 2018, ACC maintenance enables NMDAR-independent learning)

## Entries

| Entry ID | Authors | Year | Evidence Direction | Confidence | Claims |
|----------|---------|------|-------------------|------------|--------|
| 2026-04-05_inv_044_remapping_hidden_state_inference_sanders2020 | Sanders, Wilson, Gershman | 2020 | supports | 0.90 | INV-044 |
| 2026-04-05_inv_044_common_event_structure_inference_morton2020 | Morton, Schlichting, Preston | 2020 | supports | 0.76 | INV-044 |
| 2026-04-05_inv_044_schema_enables_learning_finnie2018 | Finnie et al. | 2018 | supports | 0.72 | INV-044 |

## Summary Assessment

All 3 entries support INV-044. The evidence package covers:
- Formal computational grounding: hidden state inference requires pre-formed prior over context partitions (Sanders 2020 -- primary grounding paper)
- Neural substrate of two-stage architecture: parahippocampal hierarchy encodes schema separately from slot-level representations (Morton 2020)
- Causal evidence: prior structure must be maintained before efficient slot-filling is possible; disrupting prior reinstates prior-absent inference mode (Finnie 2018)

**Main gap remaining:** No paper directly implements a co-computing system to demonstrate the degeneracy prediction. The failure mode (degenerate prior -> uninformative attribution regardless of training duration) is supported by the formal structure of the Bayesian models but not demonstrated in a head-to-head empirical comparison.
