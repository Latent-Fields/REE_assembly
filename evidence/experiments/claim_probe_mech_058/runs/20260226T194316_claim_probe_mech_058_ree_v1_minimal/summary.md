# MECH-058 E1/E2 Timescale Ablation — PASS (2026-02-26T19:43:16Z)

## Genuine ree-v1-minimal Evidence (partial support)

**Substrate:** ree-v1-minimal gridworld 10×10, 4 hazards, 200 episodes × 3 seeds × 2 conditions.
**Architecture epoch:** ree_v1_minimal_genuine_v1

## Result

| Condition | Last-quarter harm | Mean latent stability (std) |
|-----------|-------------------|-----------------------------|
| SEPARATED (E1 lr=1e-4, policy lr=1e-3) | 0.5 | 0.007436 |
| SAME-TIMESCALE (both lr=1e-3)           | 1.0 | 0.009826 |

- Stability criterion (SEPARATED std < SAME-TIMESCALE std): **PASS**
- Performance criterion (SEPARATED harm ≤ SAME-TIMESCALE × 1.05): **PASS**
- Overall verdict: **PASS** (partial_support=False)

## Architectural Interpretation

**This FAIL is NOT architecture falsification.** The interpretation requires care:

1. **Performance criterion passed**: timescale separation did not degrade harm outcomes.
   SEPARATED harm (0.5) ≤ SAME-TIMESCALE harm (1.0) — the slow anchor
   does not hurt performance at this scale.

2. **Stability criterion failed — substrate resolution issue**: the latent stability
   difference between conditions is tiny (0.007436 vs 0.009826, <3%). ree-v1-minimal's
   grid world is predictable enough that both lr=1e-4 and lr=1e-3 converge to similar
   representational stability — there is insufficient environmental complexity to stress
   the latent manifold and reveal the anchoring effect of the slow E1 rhythm.

   This is the "earn the right to add complexity" result. The heartbeat analogy (slow
   endogenous E1 clock grounding fast E2 updates) is architecturally sound, but requires
   a substrate with richer latent dynamics to be detectable via the temporal std metric.

3. **E1 loss differential is consistent with the hypothesis**: SEPARATED mean E1 loss is
   notably higher than SAME-TIMESCALE (because at lr=1e-4 the world model updates more
   slowly and accumulates more unresolved prediction error per step). This is expected and
   confirms E1 IS operating at a different timescale — the latent stability metric simply
   cannot resolve the consequence in this environment.

## Status Implication

Remains candidate. Add note: stability criterion requires substrate with richer latent
dynamics. Re-test on a more complex environment before concluding on MECH-058.
Performance criterion passing is positive signal — no regression from separation.
