# V3-EXQ-080 -- MECH-029 BreathOscillator Uncommitted Windows

**Status:** FAIL
**Claims:** MECH-029
**Seed:** 42  **Train:** 100 eps  **Eval:** 2 eps  **Steps/ep:** 200
**BreathOscillator:** period=50, sweep_dur=5, sweep_amp=0.25, e3_rate=5

## Results

| Metric | Condition A (oscillator) | Condition B (control) |
|---|---|---|
| z_world_var[sweep] | 0.00004 | 0.00000 |
| z_world_var[inter] | 0.00003 | 0.00002 |
| z_world_var_ratio | 1.1730 | 0.0000 |
| committed_rate[sweep] | 0.000 | 0.000 |
| committed_rate[inter] | 0.000 | 0.000 |
| n_sweep_steps | 40 | 0 |
| harm_pred_std_inter | 0.0000 | 0.0000 |

**Post-train running_variance: 0.5000** (base_threshold=0.400, sweep_threshold=0.300)

## PASS Criteria

| Criterion | Threshold | Result |
|---|---|---|
| C1: z_world_var ratio > 1.05 | 1.05 | PASS |
| C2: committed_rate[sweep] < inter*0.9 | 0.90 | FAIL |
| C3: n_sweep_steps >= 20 | 20 | PASS |
| C4: harm_pred_std_inter > 0.01 | 0.01 | FAIL |
| C5: no fatal errors | -- | PASS |

Criteria met: 3/5 -> **FAIL**

## Interpretation

MECH-029 PARTIAL: Some uncommitted-window signal present but below threshold. Suggest increasing sweep_amplitude or reducing agent training depth to preserve higher running_variance.

## Failure Notes

- C2 FAIL: committed_rate_sweep=0.000 >= 0.9 * inter=0.000. Agent remained committed during sweep -- variance too low for threshold reduction.
- C4 FAIL: harm_pred_std_inter=0.00004 <= 0.01. E3 harm head appears collapsed (constant output).
