# V3-EXQ-201 -- MECH-029: DMN/Reflective Mode Probe (BreathOscillator)

**Status:** FAIL
**Claims:** MECH-029
**Supersedes:** V3-EXQ-080
**Seeds:** [42, 123]  |  **Train:** 500 eps  |  **Eval:** 50 eps  |  **Steps/ep:** 200
**Config:** alpha_world=0.9, nav_bias=0.45, use_event_classifier=True
**BreathOscillator:** period=50, sweep_amp=0.3, sweep_dur=10, e3_rate=5
**Env:** CausalGridWorldV2 size=6, n_hazards=4, use_proxy_fields=True

## Design Rationale

The BreathOscillator (MECH-108) creates periodic uncommitted windows by reducing the
effective commit_threshold during sweep phases. During these windows, E3 is more likely
to be uncommitted (running_variance > effective_threshold). MECH-029 predicts that
uncommitted/reflective mode shows higher z_world variability and more diverse E3 harm
evaluations than committed execution mode.

## Per-Seed Results

| Seed | Committed Steps | Uncommitted Steps | z_world_var_C | z_world_var_U | harm_std_C | harm_std_U | harm_pred_std | Fatal |
|------|----------------|-------------------|---------------|---------------|------------|------------|---------------|-------|
| 42 | 300 | 0 | 0.000955 | 0.000000 | 0.121934 | 0.000000 | 0.1219 | 0 |
| 123 | 10000 | 0 | 0.000124 | 0.000000 | 0.008599 | 0.000000 | 0.0086 | 0 |


## Aggregate (mean across seeds)

| Metric | Committed | Uncommitted |
|--------|-----------|-------------|
| z_world_var | 0.000540 | 0.000000 |
| harm_eval_std | 0.065266 | 0.000000 |

**z_world_var_ratio** (uncommitted/committed) = 0.0000

## PASS Criteria (need 4/5)

| Criterion | Threshold | Result | Value |
|-----------|-----------|--------|-------|
| C1: min(uncommitted_steps) >= 50 | 50 | FAIL | 0 |
| C2: mean(harm_pred_std) > 0.01 | 0.01 | PASS | 0.065266 |
| C3: uncommitted_z_var > committed*1.05 | 1.05x | FAIL | 0.000000 vs 0.000567 |
| C4: harm_std_uncommitted > harm_std_committed | > | FAIL | 0.000000 vs 0.065266 |
| C5: no fatal errors | 0 | PASS | 0 |

Criteria met: 2/5 -> **FAIL**

## Failure Notes

- C1 FAIL: min(uncommitted_step_count)=0 < 50
- C3 FAIL: uncommitted_z_world_var=0.000000 <= committed*1.05=0.000567
- C4 FAIL: harm_eval_std_uncommitted=0.000000 <= harm_eval_std_committed=0.065266
