# V3-EXQ-049a -- MECH-090: Beta-Gated Policy Propagation (corrected, bistable-aware)

**Status:** PASS
**Claim:** MECH-090 -- beta gate holds E3 policy output during committed action, releases when uncommitted
**Design:** Two-condition -- trained agent (C1/C3) vs fresh agent (C2/C4)
**Mode:** Legacy (beta_gate_bistable=False); bistable mode tested in EXQ-321a
**Fixes applied:**
  1. select_action() used in eval (EXQ-049 wiring fix)
  2. Direct update_running_variance(wf_err) in training (EXQ-049c deadlock fix)
**Supersedes:** V3-EXQ-049
**alpha_world:** 0.9  |  **Warmup:** 400 eps  |  **Eval:** 50 eps/condition  |  **Seed:** 0

## Root Cause Chain

1. **EXQ-049** -- eval called `e3.select()` directly: gate never wired (hold_count=0)
2. **EXQ-049b** -- gate wired, but variance frozen (no update_running_variance call)
3. **EXQ-049c** -- post_action_update called, but _committed_trajectory guard re-deadlocks
4. **EXQ-049d** -- direct update_running_variance(wf_err): deadlock broken. C1 PASS.
   C2 FAIL: trained agent is always committed, n_uncommitted_steps=0
5. **EXQ-049e** -- two-condition design: PASS
6. **EXQ-049a** (this) -- two-condition design with full fix chain + dry-run + explicit
   bistable-mode documentation; supersedes EXQ-049 formally

## EXQ-038 Relation

EXQ-038 showed commit_stable=0.0 at ALL hazard_harm levels. Root cause: commit_threshold
was 0.003 (25000x below actual running_variance~0.33 post-training), so committed=False
was constant. This is a threshold calibration failure (Mode B), not a wiring failure.
The threshold was recalibrated to 0.40 in EXQ-049d and later. EXQ-038 tests a different
question (does variance scale with hazard_harm?) and remains unresolved.

## Condition A -- Trained Agent

| Metric | Value |
|--------|-------|
| Final running_variance (post-train) | 0.000001 |
| Mean committed fraction (train) | 1.000 |
| Committed steps (eval) | 10000 |
| Uncommitted steps (eval) | 0 |
| committed_hold_concordance | 1.000 |
| hold_count | 10347 |

## Condition B -- Fresh Agent

| Metric | Value |
|--------|-------|
| precision_init (= running_variance) | 0.500000 |
| Committed steps (eval) | 0 |
| Uncommitted steps (eval) | 10000 |
| uncommitted_release_concordance | 1.000 |
| propagation_count | 1250 |

## PASS Criteria

| Criterion | Source | Result | Value |
|---|---|---|---|
| C1: trained committed_hold_concordance > 0.6 | Cond A | PASS | 1.000 |
| C2: fresh uncommitted_release_concordance > 0.5 | Cond B | PASS | 1.000 |
| C3: trained hold_count > 0 | Cond A | PASS | 10347 |
| C4: fresh propagation_count > 0 | Cond B | PASS | 1250 |
| C5: No fatal errors | Both | PASS | 0 |

Criteria met: 5/5 -> **PASS**

