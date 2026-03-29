# V3-EXQ-140 -- MECH-094 Hypothesis Tag Write Gate Discriminative Pair

**Status:** FAIL
**Claims:** MECH-094
**Decision:** retire_ree_claim
**Seeds:** [42, 123]
**Conditions:** TAG_GATE_ON vs TAG_GATE_ABLATED
**Warmup:** 400 real eps + 800 replay eps  **Eval:** 50 real + 100 replay eps
**Env:** CausalGridWorldV2 size=6, 4 hazards, nav_bias=0.45
**Replay:** n_replay_per_ep=2, noise_std=0.1 (offset-seed env)

## Design

MECH-094 asserts the hypothesis tag is a categorical write gate separating simulation from committed residue updates. The experiment controls whether replay harm events are allowed to train the harm_eval head (proxy for phi(z) write pathway).

TAG_GATE_ON: replay harm is tagged (hypothesis_tag=True); only real harm trains harm_eval buffer.

TAG_GATE_ABLATED: tag absent; replay harm accumulates alongside real harm (PTSD contamination mechanism: replayed content writes as if real).

Key metric: contamination_gap = harm_eval_score(replay harm) - harm_eval_score(replay safe).
Low contamination_gap: tag suppresses replay routing (MECH-094 ON).
High contamination_gap: tag loss allows replay routing (ablation = PTSD model).

Secondary: real_harm_gap = harm_eval_score(real harm) - harm_eval_score(real safe). Should be high in both conditions (real harm always trains both).

## Pre-Registered Thresholds

C1: contamination_gap_ON <= 0.02 both seeds  (tag gate suppresses replay; near-zero contamination)
C2: contamination_gap_ABLATED >= 0.04 both seeds  (tag loss produces contamination)
C3: per-seed delta_contamination (ABLATED-ON) >= 0.03 both seeds  (discriminative gap)
C4: real_harm_gap_ON >= 0.03 both seeds  (real harm still learned with tag ON)
C5: n_real_harm_min >= 15 and n_replay_harm_min >= 15  (data quality)

## Results

| Condition | contam_gap | real_harm_gap | n_real_harm | n_replay_harm |
|-----------|------------|---------------|-------------|---------------|
| TAG_GATE_ON      | 0.0449 | 0.0322 | 533 | 1079 |
| TAG_GATE_ABLATED | 0.0307 | 0.0464 | 533 | 1079 |

**delta_contamination per seed: [-0.0153, -0.0131]**

## PASS Criteria

| Criterion | Result | Value |
|---|---|---|
| C1: contam_gap_ON <= 0.02 (all seeds) | FAIL | 0.0449 |
| C2: contam_gap_ABLATED >= 0.04 (all seeds) | FAIL | 0.0307 |
| C3: per-seed delta >= 0.03 (all seeds) | FAIL | [-0.0153, -0.0131] |
| C4: real_harm_gap_ON >= 0.03 (all seeds) | FAIL | 0.0322 |
| C5: n_harm_min >= 15 | PASS | real=533 replay=1079 |

Criteria met: 1/5 -> **FAIL**

## Interpretation

MECH-094 NOT supported at V3 proxy level: contam_gap_ON=0.0449 (C1 FAIL), contam_gap_ABLATED=0.0307 (C2 FAIL), delta_contamination=[-0.0153, -0.0131] (C3 FAIL). The V3 proxy (noisy replay in offset-seed env) may not generate sufficiently distinct replay harm signal to test the write-gate mechanism. Consider: (a) sharper replay/real contrast (higher replay_noise_std or structurally different replay env); (b) more episodes; (c) checking whether harm_eval baseline is dominated by training data volume rather than routing source.

## Per-Seed

TAG_GATE_ON:
  seed=42: contam_gap=0.0476 real_harm_gap=0.0437 n_real_harm=533 n_replay_harm=1086
  seed=123: contam_gap=0.0421 real_harm_gap=0.0207 n_real_harm=546 n_replay_harm=1089

TAG_GATE_ABLATED:
  seed=42: contam_gap=0.0323 real_harm_gap=0.0417 n_real_harm=547 n_replay_harm=1079
  seed=123: contam_gap=0.0290 real_harm_gap=0.0510 n_real_harm=547 n_replay_harm=1092

## Failure Notes

- C1 FAIL: TAG_GATE_ON contamination_gap > 0.02 in seeds [42, 123] -- tag gate does not suppress replay harm from harm_eval
- C2 FAIL: TAG_GATE_ABLATED contamination_gap < 0.04 in seeds [42, 123] -- tag loss does not produce measurable contamination; check replay harm volume
- C3 FAIL: per-seed delta_contamination [-0.0153, -0.0131] < 0.03 -- no discriminative contamination difference; tag gate has no effect at V3 proxy scale
- C4 FAIL: real_harm_gap_ON < 0.03 in seeds [123] -- real harm not learned even with tag ON; increase nav_bias or warmup
