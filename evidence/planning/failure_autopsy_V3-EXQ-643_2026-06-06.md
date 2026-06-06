# Failure Autopsy — V3-EXQ-643 (modulatory-authority validation)

- **Generated:** 2026-06-06T11:49:30Z
- **Scope:** single
- **Status:** confirmed (user-confirmed "as stated" at the interactive gate)
- **Run:** `v3_exq_643_modulatory_authority_validation_20260606T113132Z_v3`
- **Queue:** V3-EXQ-643 · **purpose:** diagnostic · **claim_ids:** [] · **outcome:** FAIL
- **Validates substrate:** `modulatory-bias-selection-authority` (implemented 2026-06-03; `implemented_pending_validation`, priority 1)

## 1. Facts (no interpretation)

3 arms, identical curiosity-ALL_ON + MECH-341 entropy + SD-056 config; the only
difference is `use_modulatory_selection_authority`:

| Arm | authority | gain | active_frac | scale_factor | bias_abs_mean | bias_changed_sel_frac |
|-----|-----------|------|-------------|--------------|---------------|------------------------|
| ARM_A | off | 0.5 | 0.0 | 0.0 | 0.0236 | 0.00064 |
| ARM_B | on | 0.5 | **0.0** | **0.0** | 0.0245 | 8.7e-5 |
| ARM_C | on | 0.8 | **0.0** | **0.0** | 0.0272 | 0.0062 |

3 seeds (42/43/44). Acceptance: **C0 non-degeneracy PASS** (3/3 seeds B and C);
**C1 authority-active FAIL** (`c1_mechanism_active_seeds_B=0`, `_C=0`); **C2
changes-selection FAIL** (rank_change 0/0); **C3 dose-response FAIL**
(`scale_factor_B_mean=scale_factor_C_mean=0.0`). `overall_pass=false`.

The manifest self-routes `evidence_direction=does_not_support` (a
modulatory-bias-selection-authority falsification).

**Failed criterion class:** absolute / precondition (C1 authority-active). The
authority mechanism **never fired** even with its flag True, so the
discrimination criteria (C2/C3) were untestable.

## 2. Root cause (code-confirmed)

The authority block — `ree-v3/ree_core/predictors/e3_selector.py:781-792`:

```
if self.config.use_modulatory_selection_authority:
    modulatory_total = scores - scores_raw
    modulatory_range = (modulatory_total.max() - modulatory_total.min())
    if modulatory_range > self.config.modulatory_authority_min_range_floor:   # 1e-6
        scale_factor = (gain * raw_score_range) / modulatory_range
        scores = scores_raw + scale_factor * modulatory_total
        modulatory_authority_active = True
```

- **Flag-not-reaching is ruled out.** `from_dims` threads the flag
  (`config.py:4049-4052` → `config.e3.use_modulatory_selection_authority=True`)
  and the selector reads `E3Config` (`e3_selector.py:107`). In the ON arms the
  flag is True.
- `scale_factor=0.0` **exactly** in the ON arms ⇒ the
  `modulatory_range > 1e-6` guard was **False on every tick**.
- C0 passed on bias **magnitude** (~0.024 mean-abs), but the gate needs
  cross-candidate **range**. `active_frac=0.0` always ⇒ the modulatory bias is
  **uniform across the K candidates to within 1e-6** — a per-*tick* scalar added
  equally to all candidates, with **zero per-*candidate* differentiation**.
- `bias_changed_selection_frac=0.006` (C) is exact-tie epsilon (a sub-floor range
  can still flip an exact numerical tie), consistent with range < 1e-6.

**"Rescaling a zero range is still zero"** — the authority-layer analogue of the
604a "scaling zero is still zero" finding.

## 3. Adjudication — the self-route is a hypothesis (642 pattern)

`does_not_support` **mislabels the cause**. The authority mechanism was not
falsified — it was **never exercised**, because its input (cross-candidate
modulatory range) is below floor. A `does_not_support` self-route on a
substrate-readiness validation must be checked against whether the mechanism
actually *fired*; `active_frac=0 / scale_factor=0` is **precondition_unmet**, not
falsification. The `modulatory-bias-selection-authority` substrate stays
`implemented_pending_validation` — **not falsified, not cleared**.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | diagnostic, claim_ids=[]; does NOT falsify MECH-314/320/341 — their committed-selection authority stays *pending validation*, not weakened |
| Biological reference | clear (class) | neuromodulatory (dACC curiosity / DA vigor) bias on selection is real; REE's range-rescale is an engineering arbitration, not a formal import. A modulator biases *toward differing options*; with no per-option contrast it has nothing to act on |
| Prerequisites | **missing** | per-candidate modulatory variance — same per-candidate-collapse root cause as `behavioral_diversity_isolation:GAP-B` (identical z_world across candidates → identical bias). `MECH-314a-Phase-2-impl` per-candidate novelty did not deliver cross-candidate range in 643 |
| Implementation | complete & correct | the rescale-to-(gain·raw_range) code runs as designed; the failure is a structural precondition (range > floor). Symbol-vs-role: has the symbol, cannot perform the role without input variance |
| Environment | adequate | reef-bipartite contact-making env |
| Measurement | **under-instrumented** | C0 asserts MAGNITUDE non-degeneracy, not cross-candidate RANGE — so the validation cannot distinguish "falsified" from "starved". Load-bearing test-design gap |
| Integration | isolated-in-effect | authority layer downstream of a per-candidate-uniform modulatory signal → structurally uncoupled from selection |
| Scale | n/a | — |

**Recommended epistemic_category:** `substrate_conditional` (the authority
substrate depends on an upstream per-candidate-variance substrate not yet
delivering). No claim carries this — the run is claimless.

## 5. Learning extracted

1. The modulatory-bias-selection-authority substrate (range-rescale) is
   **necessary-but-not-sufficient**: it cannot deliver committed authority while
   the upstream modulatory bias is uniform across candidates. The bottleneck is
   one layer up — per-candidate modulatory differentiation.
2. A **magnitude** non-degeneracy check (C0) does not establish the precondition
   for an authority test that gates on cross-candidate **range**. The
   non-degeneracy check must match the gate's quantity.
3. **Fourth convergent instance** of the modulatory-signal-does-not-reach-
   committed-selection pattern: 604a (curiosity bias=0), 624a (vigor v_t equal
   both arms), 614d (within-class temperature, no committed lift), 643 (authority
   rescale starved of range). One structural property — scoring/modulatory-layer
   signals carry no per-candidate variance at committed selection.
4. A `does_not_support` / falsification self-route on a substrate-readiness
   validation must be checked against whether the mechanism *fired*
   (`active_frac` / `scale_factor`). 642 pattern, now recurring at the authority
   layer.

## 6. Routing (user-confirmed)

- **Primary — `implement-substrate` (action = amend):** append 643 as a
  `failure_record` to the existing `modulatory-bias-selection-authority`
  substrate_queue entry (its named validation); keep `ready=false`; add a
  per-candidate-modulatory-variance dependency to `depends_on_unresolved`; update
  the `implementation_hint` to record that the range-rescale is starved of
  cross-candidate range. `pending_retest_after_substrate=true`.
- **Secondary — `/queue-experiment` 643a:** corrected re-validation with a
  **range-based P0 readiness gate** — assert cross-candidate `modulatory_range >
  min_range_floor` on a positive control *before* C1, per the trivial-prediction
  readiness-gate convention landed 2026-06-06. Below-floor self-routes
  `substrate_not_ready_requeue`, never `does_not_support`. 643a is gated on the
  per-candidate-modulatory-variance substrate landing (do not re-run on the
  current substrate — 643 already proved the authority block has zero range to
  act on).
- **Evidence direction:** recommend correcting the manifest from
  `does_not_support` to **`non_contributory`** (diagnostic, claimless; does not
  weight MECH-314/320/341).

## 7. Draft evidence-direction note (governance applies — do not write here)

> V3-EXQ-643 (diagnostic, claim_ids=[]) is the substrate-readiness validation of
> the modulatory-bias-selection-authority substrate. C0 modulatory non-degeneracy
> PASS (bias magnitude ~0.024) but C1 authority-active FAIL:
> modulatory_authority_active_frac=0.0 and scale_factor_mean=0.0 in BOTH
> authority-ON arms (gain 0.5 and 0.8) — the authority range-rescale
> (e3_selector.py:781-792, gated on cross-candidate modulatory_range >
> min_range_floor 1e-6) never fired. Adjudicated
> (failure_autopsy_V3-EXQ-643_2026-06-06) as PRECONDITION_UNMET, NOT a
> falsification: the flag reaches E3Config (from_dims config.py:4049-4052) and the
> block is correct, but the modulatory contribution is uniform across the K
> candidates to within 1e-6 (a per-tick scalar added equally, zero per-candidate
> range), so the range-rescale has nothing to rescale — "rescaling a zero range is
> still zero". The substrate is NOT falsified and NOT cleared; it stays
> implemented_pending_validation. The unmet upstream prerequisite is per-candidate
> modulatory variance (same per-candidate-collapse root cause as
> behavioral_diversity_isolation:GAP-B). non_contributory; does not weight
> MECH-314/320/341. pending_retest_after_substrate.
