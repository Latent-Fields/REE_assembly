# V3-EXQ-946 -- ContextMemory write-ADDRESS informativeness diagnostic

**Status:** PASS  **Label:** context_informative_address_found_at_operating_point
**Purpose:** diagnostic (claim_ids=[]; informs EVB-0628/INV-044 substrate readiness, contextmemory-write-path-addressing-degeneracy)

| Arm | seeds clearing null (z>=2.0) | observed MI range (bits) |
|---|---|---|
| BIAS_W1_0 | 5/5 | 0.0002-0.0006 |
| BIAS_W0_1 | 3/5 | 0.0003-0.0006 |
| BIAS_W0_01 | 1/5 | 0.0001-0.0439 |
| REFRACTORY | 2/5 | 0.0000-0.0171 |

Clearing arms: ['BIAS_W1_0', 'BIAS_W0_1']
