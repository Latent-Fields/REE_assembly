# Failure autopsy -- V3-EXQ-964 (MECH-482 / SD-102 epistemic-deficit accumulator validation)

- **Status:** `awaiting_human_confirmation` (staging mode -- non-interactive session; routing NOT finalised)
- **Generated:** 2026-08-30T06:34:18Z
- **Run:** `v3_exq_964_mech482_epistemic_deficit_validation_20260829T215030Z_v3`
- **Purpose:** `diagnostic`, `claim_ids: ["MECH-482"]`
- **Dry-run gate:** clean (`dry_run: false`)

## 1. Facts

| Criterion | Load-bearing | Measured | Threshold | Result |
|---|---|---|---|---|
| C1 accumulator becomes live | yes | 1.0 | 0.5 | **PASS** |
| C2 downstream consumer can diverge | yes | 0.0 | > 0.0 | **FAIL** |
| C3 instrument control bit-identical | no | 0.0 | 1e-9 | **PASS** |

Accumulator state, all three seeds:

| Seed | `n_targets` | `n_updates` | `n_readouts` | `n_vacuous_readouts` | `last_n_targets_matched_at_readout` | `yoked_divergence_frac` |
|---|---|---|---|---|---|---|
| 71 | **1** | 59 | 13 | 0 | **32** | 0.0 |
| 101 | **1** | 59 | 20 | 0 | **32** | 0.0 |
| 202 | **1** | 59 | 12 | 0 | **32** | 0.0 |

## 2. The decisive finding -- C2 was unsatisfiable by construction

`EpistemicDeficitAccumulator.readout` (`ree_core/policy/epistemic_deficit.py:319-321`):

```
out = torch.where(matched, deficits[nearest_idx], torch.zeros(K, ...))
```

With `len(self._targets) == 1`, `nearest_idx` is `0` for every candidate, so `deficits[nearest_idx]` is the **same scalar for all K**. And `last_n_targets_matched_at_readout == 32 == K` says every candidate matched. So `out` is a **constant vector**.

The consumer (`ree_core/policy/structured_curiosity.py:541-543`) then applies:

```
lp_contrib = cfg.curiosity_learning_progress_weight * lp_vec
total = total - lp_contrib
```

**Subtracting a constant from every candidate's score cannot move an argmax.** `yoked_divergence_frac == 0.0` was mathematically forced on every tick of every seed. The run carries **zero information** about whether MECH-482's mechanism is selection-relevant.

**C1 and C2 are not independent.** C1's PASS bar is "at least one persistent target AND at least one update" -- satisfied at exactly `n_targets == 1`, the value at which C2 *must* fail. The criterion that certifies readiness is met precisely where the criterion it gates becomes unanswerable.

**Why only one target.** `EpistemicDeficitAccumulator.reset()` clears `_targets` every episode (deliberately -- it mirrors StructuredCuriosity's per-episode LP-EMA clear). Across 3 x 60-step episodes the accumulator never exceeded one target.

**The instrument itself is sound.** C3 (self-yoked, bit-identical) passed on both arm identities, the divergence metric is a genuine per-step comparison of two argmax indices (not a hardcoded zero), and `n_readouts` was non-zero on every seed. Nothing is wrong with the harness; the substrate state never posed the question.

## 3. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear | the run could not express the claim |
| Biological reference | partial | not reached |
| Prerequisites | **missing** | needs >=2 targets AND candidates matching *different* targets |
| Implementation | partial | accumulator populates, consumer wired, but per-episode reset caps it at one target |
| Environment | **too sparse** | 60-step episodes yield too few distinct uncertainty loci |
| Measurement | **misleading** | C1's bar guarantees C2's failure |
| Integration | partially coupled | readout reaches the consumer, but delivers a constant |
| Scale | likely insufficient | 180 candidate ticks/seed, 12-20 readouts |

**Failure-location (GOV-FAILLOC-1): MIXED -- `MEASURES + ENVIRONMENT` (+ implementation).** Measurement and environment are both inadequate, so **REE FAILED is not reachable** and is not asserted.

## 4. Argument raised and withdrawn

**"The `vacuous_readout_rate` readiness gate is blind."** Driver lines 223-227 compute `n_vacuous_readouts / n_readouts if n_readouts > 0 else 0.0` -- so a gate value of `0.0` means *either* "never refused" *or* "never invoked at all", and both pass the `< 0.5` ceiling. **Withdrawn as the cause:** `n_readouts` is 13/20/12, non-zero on every seed. The gate defect is real but was not exercised here; carried forward as a latent instrument finding, not part of this diagnosis.

## 5. Learning extracted

- **A readiness gate must require differentiation, not non-emptiness.** "At least one target exists" certifies the wrong thing. The gate C2 needs is `>= 2` matched targets, or equivalently a non-zero per-candidate deviation range.
- **A negative control establishes specificity, not sensitivity.** C3 proves the divergence detector does not fire spuriously. Nothing here proves it *can* fire. A positive control -- inject a synthetic two-target deficit, confirm the argmax flips -- would have made this zero interpretable immediately.
- **RECORDING GAP.** `StructuredCuriosity` already computes `_last_lp_dev_range = lp_contrib.max() - lp_contrib.min()` -- exactly the quantity that decides this question, and it would have read `0.0`. It was never recorded. Recording it is free and makes the diagnosis self-evident from the manifest.
- `assert_no_structurally_unsatisfiable_gate` is imported by this driver, but it is static over pre-registered specs and cannot see unsatisfiability that **emerges from the runtime state reached**.

## 6. Routing (proposed -- awaiting confirmation)

**`queue-experiment`** -- re-pose the validation (new letter, same question) with:

1. a readiness gate requiring `n_targets >= 2` **and** candidates matching at least two distinct targets (or `_last_lp_dev_range > 0`), evaluated *before* the scored comparison;
2. a **positive control** that injects a synthetic multi-target deficit and asserts the argmax flips;
3. `_last_lp_dev_range` and the accumulator's per-readout target-match counts recorded in the manifest;
4. an accumulation window long enough to build a second target before the per-episode reset.

Supporting substrate entry `sd_epistemic_deficit_multitarget_readiness` (priority 2, severity `degrading`).

**Re-derive brake:** does not fire. MECH-482 has 0 prior `substrate_ceiling` hits under R1-R3; this reading is not `substrate_ceiling`.

## 7. Recommended per-claim disposition

**MECH-482** -- direction `non_contributory`; `epistemic_category` **stays** `substrate_conditional`; status **stays** `candidate`; `recommended_diagnostic_evidence_adjudicated: true`. What changes is the `evidence_quality_note`, which must record that C2 was structurally unsatisfiable at `n_targets == 1` and so does **not** count as a negative result for the claim.

## Adversarial red-team pass (Step 7c) -- NOT RUN

**No independent verifier ran, and no CONFIRMED verdict is claimed.** Step 7c calls for spawning a separate agent (preferably on a different model) to attack the conclusion. This session operates under a standing instruction not to invoke the Agent tool unless the user requests it, and the user did not.

The adversarial discipline was applied in-context instead, and it did change conclusions rather than rubber-stamping them -- six arguments were raised and withdrawn on direct code or docstring reads, each recorded under `arguments_withdrawn`. That is explicitly **weaker** than an independent pass: it shares the drafter's priors by construction, which is the exact property the pass exists to break.

**For governance:** treat every routing recommendation here as unverified by a second reader. The two highest-value targets for an independent check are V3-EXQ-963's claim that sampling starvation is refuted by the 779a comparison, and V3-EXQ-964's claim that C2 was mathematically unsatisfiable at `n_targets == 1`.
