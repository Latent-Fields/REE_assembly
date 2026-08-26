---
title: Rule Distinguishability Maintenance (CRF locus)
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 19
---

# Rule Distinguishability Maintenance (CRF locus)

**Status:** architecture stub for candidate claims MECH-437 / MECH-438 (candidate / substrate_conditional / implementation_phase v4 / version_relevance v4_v5). Registered 2026-06-17 from a REE_convergence intake. **V4-leaning; off the V3 critical path — blocks no V3 closure node.** Decide-whether-to-build is a later governance step.

## Problem (the necessity is clear, the mechanism is not)

The `arc_062_rule_apprehension` closure work (nodes GAP-B / GAP-K; claims MECH-309 / ARC-062 / ARC-063) repeatedly hits a CandidateRuleField (CRF) conflict-gate lockout. In `ree-v3/ree_core/policy/candidate_rule_field.py`, `gate_and_select` uses

```
theta = 0.15 + 0.25 * (n_matched - 1)
```

When 7–8 minted rules co-match a context, `theta ≈ 1.65`, far above the maintenance floor (`≈ 0.45`), so every rule is gated out and `crf_frac_active` collapses to 0 (654-lineage; `failure_autopsy_V3-EXQ-654d_2026-06-16`). The **necessity** that minted rules be mutually distinguishable to remain selectable is established. The **mechanism** for achieving and maintaining that distinguishability is not: the current amends (`crf_mature_context_match_threshold` sharpening, `crf_tolerance_conflict_cap`, `crf_maintenance_couple_to_theta`) are point fixes, not a principled mechanism.

## Convergence provenance

Intake thread: **rule distinguishability** (REE_convergence, 2026-06-17). Two complementary external mechanisms, promotion packet `CPKT-RULE-DISTINGUISHABILITY-20260617`:

- **DreamCoder** (Ellis et al. 2021; arXiv 2006.08381; RSTA 2023) — wake-sleep library learning. Minted abstractions are kept distinguishable by a periodic non-gradient **refactoring/compression** step under an MDL objective. *Maintenance-side.* → MECH-437.
- **DreamerV3** (Hafner et al. 2023; arXiv 2301.04104) — categorical discrete latent codebook (32 categoricals × 32 classes, straight-through). World-state keys are separable **by construction**, bounding collision by codebook capacity. *Construction-side.* → MECH-438.

Comparison artifacts: `REE_convergence/sources/dreamcoder/comparison_table.md`, `REE_convergence/sources/dreamer-v3/codebook_key_separability.md`, `REE_convergence/reports/2026-06-17_rule_distinguishability_synthesis.md`.

## MECH-437 — distinguishability as a maintained property (maintenance-side)

A periodic, non-gradient **consolidation/refactor operator** over the minted-rule pool: compress / merge near-duplicate rules, retire rules that never reach selection, and re-separate the survivors under an MDL-style separability objective, so the steady-state co-match count `mean n_matched` stays low enough that `theta(n_matched)` sits below the availability ceiling. Distinguishability becomes the maintained quantity; the gate stops being the only lever. Would reuse the ARC-063 sleep-vs-waking refinement asymmetry (waking-light + sleep-heavy) and the MECH-272/273/285 sleep cluster.

**Falsifier:** if a periodic MDL-driven consolidation pass over the minted-rule pool yields no improvement in `crf_frac_active` / committed-class entropy vs a no-consolidation baseline on a substrate where >5 rules co-match (the lockout regime), the maintained-distinguishability mechanism is falsified (the fix is elsewhere — e.g. minting too many rules, or the gate functional form itself).

## MECH-438 — separable-key codebook (construction-side)

Assign minted-rule **context keys** in a quantised / categorical codebook that is separable by construction (DreamerV3 categorical-latent analog), bounding the number of rules that co-match any context (`n_matched`) up front, so `theta(n_matched)` stays below the availability ceiling — rather than letting overlapping continuous context tags produce unbounded co-match counts and gating reactively.

**Risk (the construction-side failure mode):** a codebook too coarse collapses genuinely-distinct rules onto one key, destroying the discriminability the rule-apprehension layer exists to provide (the same differentiation-vs-persistence tension ARC-063 already names).

**Falsifier:** if quantising context keys onto a categorical codebook does not reduce `mean n_matched` below the lockout threshold, OR reduces it only by collapsing distinct rules onto one key (measured as a drop in committed-class entropy / route diversity), constructive key-separability is falsified.

## Relationship to the cluster

- **MECH-309** — the diagnostic these mechanisms ultimately serve (monomodal collapse without a rule-apprehension layer).
- **ARC-062** — weak-reading gated-policy slot (the selector half).
- **ARC-063** — strong-reading CandidateRuleField; the CRF locus these mechanisms operate on. The `crf-availability-maintenance` substrate_queue item is the existing point-fix line; MECH-437/438 are the principled-mechanism candidates behind it.
- **ARC-064** — the bottom-up regularity-mint source that populates the pool these mechanisms keep separable.

MECH-437 (maintenance) and MECH-438 (construction) are **complementary**: construction bounds the steady-state co-match count; maintenance cleans the residue and retires dead units. Both target the CRF conflict-gate lockout.
