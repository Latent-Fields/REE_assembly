# V3-EXQ-034 — ARC-025 Three-Engine Irreducibility Ablation

**Status:** PASS
**Claims:** ARC-025, SD-003, MECH-071
**World:** CausalGridWorldV2 (proximity_scale=0.05, harm_scale=0.02)
**alpha_world:** 0.9  (SD-008)
**Seed:** 0
**Warmup:** 500 episodes  **Eval:** 50 episodes

## Claim Being Tested

ARC-025 (architecture.three_engine_irreducibility): the three-engine architecture (E1+E2+E3)
is irreducible. Removing any single engine collapses a distinct capacity that the full system
holds. Two engines are tested here:

- **E3** (harm evaluator): ablating E3 should collapse calibration (harm detection).
- **E2** (world forward model): ablating E2 should collapse attribution (causal signature).

## Ablation Design

| Condition   | Training                        | Eval modification                          |
|-------------|--------------------------------|--------------------------------------------|
| full        | E2.world_forward + E3.harm_eval trained | None — normal pipeline              |
| e3_ablated  | E2 trained; E3 harm_eval SKIPPED | harm_eval → constant 0.5               |
| e2_ablated  | Both E2 + E3 trained normally  | world_forward → identity (ignores action)  |

## Set A — Calibration (harm_eval by transition type)

| Transition type        | full   | e3_ablated | e2_ablated |
|------------------------|--------|------------|------------|
| none (locomotion)      | 0.3652 | 0.5000 | 0.3652 |
| hazard_approach        | 0.5567 | 0.5000 | 0.5567 |
| env_caused_hazard      | 0.5849 | 0.5000 | 0.5849 |
| agent_caused_hazard    | 0.4724 | 0.5000 | 0.4724 |

| Metric                   | full   | e3_ablated | e2_ablated |
|--------------------------|--------|------------|------------|
| calibration_gap_approach | **0.1915** | 0.0000 | 0.1915 |
| calibration_gap_contact  | 0.1635 | 0.0000 | 0.1635 |
| harm_pred_std            | 0.1570 | 0.0000 | 0.1570 |

## Set B — Attribution (SD-003 causal signature)

| Transition type     | full      | e3_ablated | e2_ablated |
|---------------------|-----------|------------|------------|
| none (locomotion)   | -0.074152 | 0.000000 | 0.000000 |
| hazard_approach     | 0.005271 | 0.000000 | 0.000000 |
| env_caused_hazard   | -0.029201 | 0.000000 | 0.000000 |
| agent_caused_hazard | 0.017314 | 0.000000 | 0.000000 |

| Metric          | full      | e3_ablated | e2_ablated |
|-----------------|-----------|------------|------------|
| attribution_gap | **0.034472** | 0.000000 | 0.000000 |

## World-Forward R²

| Condition   | wf_r2 |
|-------------|-------|
| full        | 0.9472 |
| e3_ablated  | 0.9483 |
| e2_ablated  | 0.9472 |

(E2 trains normally in all three conditions; wf_r2 should be similar across conditions.)

## Training Counts

| Condition   | approach events | contact events |
|-------------|----------------|----------------|
| full        | 8125 | 463 |
| e3_ablated  | 8125 | 463 |
| e2_ablated  | 8125 | 463 |

## PASS Criteria

| Criterion | Result | Value |
|-----------|--------|-------|
| C1: cal_gap_approach_full > e3_abl + 0.05  (E3 load-bearing for calibration) | PASS | 0.1915 vs 0.0000 + 0.05 |
| C2: attribution_gap_full > e2_abl + 0.01   (E2 load-bearing for attribution) | PASS | 0.034472 vs 0.000000 + 0.01 |
| C3: cal_gap_approach_full > 0.10           (full system calibration works)  | PASS | 0.1915 |
| C4: attribution_gap_full > 0               (full attribution direction correct) | PASS | 0.034472 |
| C5: n_approach_eval >= 50                  (sufficient approach steps)       | PASS | 832 |

Criteria met: 5/5 → **PASS**
