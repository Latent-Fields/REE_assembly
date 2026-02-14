# Literature Summary: 2026-02-14_q011_prioritized_replay_vs_entropy_floor_natneuro2018

## Claims Tested

- `Q-011`
- `ARC-018`
- `MECH-033`

## Source

- Mattar MG, Daw ND (2018), *Prioritized memory access explains planning and hippocampal replay*.
- URL: `https://www.nature.com/articles/s41593-018-0232-z`

## Mapping to REE

- The model explains replay scheduling via **gain** and **need** priorities instead of a fixed entropy floor.
- This maps to REE as: rollout diversity can emerge from utility-prioritized sampling rather than enforcing a global minimum rollout entropy.
- That weakens `Q-011` interpreted as a hard architectural requirement for a minimum entropy floor.

## Caveats and Mapping Limits

- This is a computational account constrained by replay phenomena, not a direct test of REE control policy.
- The result does not prove deterministic replay should dominate in all contexts.
- It leaves open whether local anti-collapse heuristics are still needed in some regimes.

## Direction and Confidence

- `evidence_direction`: `weakens`
- `confidence`: `0.66`
- Rationale: strong conceptual alignment against a hard entropy-floor requirement, with moderate abstraction distance to REE implementation details.
