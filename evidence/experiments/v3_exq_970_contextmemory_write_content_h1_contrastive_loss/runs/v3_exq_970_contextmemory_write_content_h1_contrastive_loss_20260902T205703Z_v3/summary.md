# V3-EXQ-970 -- ContextMemory write-content H1 (loss-objective-mismatch) contrastive-loss probe, dual regime

**Status:** FAIL  **Label:** h1_content_referencing_objective_not_confirmed_either_regime
**Purpose:** diagnostic (claim_ids=[]; hypothesis_space contextmemory_write_content_discrimination, H1-loss-objective-mismatch)

| Regime | mean Jaccard UNTRAINED | mean Jaccard TRAINED | drop >= 0.25? | p-value | regime gate green | regime H1 pass (perm-test-gated) | bare-margin pass (secondary) |
|---|---|---|---|---|---|---|---|
| A (real-agent, held-out latents) | nan | nan | False | nan | False | False | False |
| B (synthetic, trained clusters) | 0.583 | 0.000 | True | 0.0625 | True | False | True |

H1_content_referencing_objective_succeeds_in_either_regime (OR across regimes, permutation-test-gated): FAIL (bare-margin-only secondary reading: PASS)
Bonferroni-corrected alpha: 0.025
PARTIAL non-vacuity: arm 'Regime_A' failed untrained_baseline_headroom. Arm(s) Regime_B passed the gate in full and ARE scored -- a red arm does NOT vacate a green one (failure_autopsy_V3-EXQ-785_2026-07-19.md sections 2a/8). Read the red arm(s) as unscored, NOT as a refutation.
