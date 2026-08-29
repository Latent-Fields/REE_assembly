# V3-EXQ-956 -- ContextMemory gumbel_learned write-address selection, real-agent validation

**Status:** FAIL  **Label:** gumbel_learned_occupancy_only_content_discrimination_not_confirmed
**Purpose:** diagnostic (claim_ids=[]; validates substrate_queue contextmemory-write-path-addressing-degeneracy, THIRD mechanism)

| Arm | seeds >= 2 occupied | mean probe Jaccard | n_write_calls range |
|---|---|---|---|
| LEGACY | 2/5 | 0.536 | 1432-1598 |
| GUMBEL_UNTRAINED | 5/5 | 0.400 | 1446-1576 |
| GUMBEL_TRAINED | 5/5 | 0.667 | 1446-1576 |

C1 (occupancy, both GUMBEL arms): PASS
C2 (content-discrimination, mean Jaccard trained <= untrained - 0.25): FAIL (untrained=0.400, trained=0.667)
