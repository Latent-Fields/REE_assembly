# V3-EXQ-969 -- ContextMemory gumbel_learned write-address selection, H2-operating-point sweep

**Status:** FAIL  **Label:** h2_no_operating_point_improves_content_discrimination_null_holds
**Purpose:** diagnostic (claim_ids=[]; validates substrate_queue contextmemory-write-path-addressing-degeneracy, H2 leg)

Untrained baseline (Phase A, n=10): mean_jaccard=0.850 (readiness PASS)

| Config | weight | mean Jaccard | delta vs baseline | p-value (method) | counts as discovery |
|---|---|---|---|---|---|
| GUMBEL_TRAINED_W0P5 | 0.5 | 1.000 | +0.150 | 1.0000 (exact_sign_flip) | no |
| GUMBEL_TRAINED_W0P1 | 0.1 | 0.917 | +0.067 | 0.7857 (exact) | no |
| GUMBEL_TRAINED_W2P0 | 2.0 | 0.917 | +0.067 | 0.7857 (exact) | no |
| GUMBEL_TRAINED_W8P0 | 8.0 | 0.889 | +0.039 | 0.6250 (exact) | no |

H2_any_operating_point_improves_content_discrimination: FAIL (alpha_corrected=0.0125 across N_CONFIGS_TESTED=4)
Phase A paired sign (n=10): 2 wrong-direction, 0 correct-direction, 8 tied
