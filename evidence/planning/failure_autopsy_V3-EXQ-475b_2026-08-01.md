# Failure Autopsy: V3-EXQ-475b (Q-040.c dACC PE-weight delta correlation)

**Generated:** 2026-08-01T12:54:47Z
**Run:** `v3_exq_475b_q040c_dacc_pe_weight_delta_correlation_20260801T050027Z_v3`
**Queue ID:** V3-EXQ-475b
**Claim IDs:** Q-040
**Status:** confirmed

## 1. Facts

**Design.** First-ever queuing of Q-040.c (mechanism-quantification sub-question, named in claims.yaml since 2026-05-08 but never actually run). Tests whether dACC's per-step bias magnitude tracks precision-weighted forward-PE when MECH-269b V_s-rollout-gating is ON vs OFF. 3 seeds (42/7/19) × 2 arms (ARM_vs_off, ARM_vs_on).

**Outcome:** FAIL. Self-route: `substrate_not_ready_requeue`. `non_degenerate: false`, `degeneracy_reason: "dacc_bias_magnitude_series: no groups"`.

**Preconditions:**
- P1 (gate-firing, MECH-269b engaged): **PASS** — 2/3 seeds show the V_s rollout gate holding candidates (`vs_gate_total_held` > 0 in ARM_vs_on).
- P2 (dACC engagement, `dacc_bias_nonzero_steps > 0` on ≥2/3 seeds, both arms): **FAIL** — 0/6 runs (3 seeds × 2 arms) show ANY dACC engagement. `n_dacc_fires = 0` in every single row, meaning `agent._dacc_last_bundle` was `None` on every tick across ~1000+ eval steps per run.

## 2. Root cause (code-traced, not left as an unexplained gate failure)

`ree_core/agent.py` gates dACC's forward pass with:
```
if self.dacc is not None and z_harm_a is not None:
```
`self.dacc` is instantiated (since `use_dacc=True` is set), so the failure must be `z_harm_a is None` on every tick. Traced to `experiments/_lib/goal_pipeline_tier1.py::build_config()`:

```python
def build_config(env, arm, *, enable_affective_harm_stream: bool = False):
    ...
    if arm.gap4_operating:
        gs_kwargs = dict(...)  # no harm-stream flags here
        if enable_affective_harm_stream:
            gs_kwargs.update(use_harm_stream=True, use_affective_harm_stream=True, z_harm_a_dim=HARM_A_DIM, ...)
        cfg = REEConfig.goal_stream(**gs_kwargs)
```

The 475b driver's `_build_arm_config` calls `build_config(env, gap4_arm)` **without** `enable_affective_harm_stream=True`. Since the parameter defaults `False`, the `if enable_affective_harm_stream:` block — which is what actually wires `use_harm_stream`/`use_affective_harm_stream`/`z_harm_a_dim` into the config — never executes. `z_harm_a` stays structurally `None` for the entire run.

**This is the exact failure mode `build_config`'s own docstring names by precedent**: *"the gap4 (goal_stream) branch historically did NOT forward the SD-011 flags, so z_harm_a stayed None on every latent... the V3-EXQ-620 / V3-EXQ-625 measurement artifact diagnosed 2026-06-01."* The 475b driver walked directly into a documented footgun.

## 3. Claim-layer mapping

Q-040 (candidate). Q-040a/b were independently settled by the 490 cohort (GAP-4 closed by re-scope, governance_2026_06_09). Q-040c is a narrower quantification sub-question, unaffected by this FAIL's disposition of Q-040a/b.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | run tested nothing about the claim — dACC never engaged |
| Biological reference | not assessed | mechanism never exercised |
| Prerequisites | present | MECH-269b V_s gating (P1) confirmed engaging correctly |
| Implementation | **driver bug** | missing `enable_affective_harm_stream=True` in the config call |
| Environment | n/a | |
| Measurement | n/a — precondition caught it correctly | |
| Integration | n/a | dACC never fired, so no integration to assess |
| Scale | n/a | |

## 5. Why this is a driver bug, not a substrate ceiling

P1 passing cleanly (2/3 seeds) while P2 fails completely (0/6) isolates the defect precisely: the upstream V_s-gating substrate works exactly as intended; the problem is a single missing config flag downstream of it. This is not a scale, environment, or substrate-readiness issue — it is deterministic given the config, and would fail identically on any re-run without the fix.

## 6. Learning extracted

1. P2 failing at exactly 0/N (not a marginal near-miss) is itself diagnostic of a structural precondition never being met — worth a code trace before assuming "insufficient power."
2. The gap4-operating branch requires an explicit opt-in (`enable_affective_harm_stream=True`) that the non-gap4 branch doesn't need — a documented asymmetry that this driver missed despite the warning being in the module's own docstring.
3. A cheap smoke-test assertion (`n_dacc_fires > 0`) before committing to the full 6-run design would have caught this in minutes.

## 7. Routing

**Evidence direction: `non_contributory`** — confirmed. This run does not weigh on Q-040c either way.

**Routing: `/queue-experiment`** — same-question re-queue as V3-EXQ-475c with the one-line fix (`enable_affective_harm_stream=True`), plus a pre-flight smoke assertion that dACC actually fires before committing to the full run.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for Q-040 — does not fire.
