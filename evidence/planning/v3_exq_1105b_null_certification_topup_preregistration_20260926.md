# V3-EXQ-1105b: pre-registered null-certification top-up (pooled). Written BEFORE any 1105b result exists

- **Written:** 2026-09-26T16:04:45Z by orchestrator `orchestrate-20260924-breakthrough-c2`. V3-EXQ-1105b (ree-v3 `ff5266b326`) is queued and pending at the time of writing. No 1105b result, manifest or partial log has been read.
- **Why this exists.** The queueing worker's red-team documented that 1105b's null-certification leg is under-powered. N_cert requires the one-sided 95% Clopper-Pearson upper bound on the false-positive rate to be <= 0.10, which means at most 2 of 64 null fires. If the true rate is about 0.05 (1105a's estimate), certification passes only about 37% of the time. Probabilities of certifying, computed exactly:

| pooled null arms | max fires allowed | P(certify) if FPR = 0.03 | 0.05 | 0.07 |
|---|---|---|---|---|
| 64 (1105b alone) | 2 | 0.70 | 0.37 | 0.17 |
| 128 | 6 | 0.91 | 0.54 | 0.20 |
| **192 (1105b + top-up)** | **12** | 0.99 | **0.83** | 0.41 |

- **Pre-registered rule.** The 1105b bars (P1, P2, N, N_cert) are **unchanged**, and 1105b is scored first exactly as written in its script.
  - **Trigger.** If 1105b's verdict is CANNOT_DETERMINE solely because N_cert fails, meaning P1 is ready, P2 passes and the N point estimate is <= 0.10, then one **null-only top-up** is queued.
  - **Top-up design.** 16 more M2 sign-shuffled null arms on each of the same 8 admitted seeds. The seed admission list and null construction are identical to 1105b's and are reproduced from its screening, so the top-up adds 128 nulls.
  - **Pooled bar.** N_cert is re-evaluated on the POOLED 192 nulls with the same bound (one-sided 95% Clopper-Pearson upper <= 0.10, i.e. at most 12 fires). The pooled N point estimate must also be <= 0.10.
  - **What the verdict becomes.** Certification succeeds only if the pooled bound meets the bar, and only then does 1105b's combined verdict become PASS. If the pooled bound misses, the result stays CANNOT_DETERMINE (not certified). If the pooled point estimate exceeds 0.10, the result is FAIL.
  - **No second top-up** is permitted under this pre-registration.
- **Other outcomes.** If 1105b FAILs P2 or N, or P1 is not ready, no top-up runs, and routing goes back to /failure-autopsy as usual.
- **Not changed.** The GFLAG-0487 battery gate stays closed until a detector validates. The claim tags are unchanged (INV-054, and MECH-523 as a beneficiary co-tag).
