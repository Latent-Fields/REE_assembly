# V3-EXQ-943 -- ContextMemory write-address selection, real-agent validation

**Status:** PASS  **Label:** write_address_fix_validated_under_real_agent
**Purpose:** diagnostic (claim_ids=[]; validates substrate_queue contextmemory-write-path-addressing-degeneracy)

| Arm | seeds >= 2 occupied | n_write_calls range |
|---|---|---|
| LEGACY | 2/5 | 2933-3187 |
| BIAS | 5/5 | 2933-3187 |
| REFRACTORY | 5/5 | 2933-3187 |

C1_BIAS: PASS (5/5 >= 3 required)
C1_REFRACTORY: PASS (5/5 >= 3 required)
