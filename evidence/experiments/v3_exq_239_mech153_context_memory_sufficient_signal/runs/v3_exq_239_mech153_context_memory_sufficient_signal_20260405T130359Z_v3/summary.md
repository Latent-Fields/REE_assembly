# V3-EXQ-239 -- MECH-153 Context Memory Sufficient Signal Test

**Status:** FAIL
**Claims:** MECH-153
**Seeds:** [42, 7, 11, 99, 31]
**Supersedes:** EXQ-187a (inconclusive: lambda=0.1, 150 warmup eps insufficient)

## Context

EXQ-187a was diagnosed as inconclusive (not a code bug): context_memory.write()
was correctly called, but lambda=0.1 with 150 warmup episodes was insufficient
to produce differentiated context vectors (cosine_sim=1.0). This experiment
uses 5x stronger supervised signal (lambda=0.5) and 3x longer warmup (500 eps).

## Design

**SUPERVISED:** lambda_terrain=0.5, 500 warmup eps x 200 steps.
CE terrain-class loss (3 classes: OPEN/ROCKY/FOREST) flowing through extract_cue_context()
and ContextMemory. context_memory.write() called each step.

**ABLATED:** lambda_terrain=0.0 (no supervised loss). Same warmup setup.
Tests whether unsupervised context representations differentiate without supervision.

## Key Results

| Condition | mean cosine_sim | mean terrain_acc |
|---|---|---|
| SUPERVISED | 1.0000 | 0.6043 |
| ABLATED | 1.0000 | 0.6043 |
| Difference (ABLATED - SUP) | -0.0000 | -- |

## Pass Criteria

| Criterion | Result | Notes |
|---|---|---|
| C1: SUP cosine_sim<0.95 (3/5 seeds) | FAIL | 0/5 seeds |
| C2: mean_cosine_diff>0.02 | FAIL | diff=-0.0000 |
| C3: SUP terrain_acc>0.55 (3/5 seeds) | PASS | 4/5 seeds |
| C4: ABL cosine_sim>=0.98 (3/5 seeds) | PASS | 5/5 seeds |

PASS rule: C1 AND (C2 OR C3) AND C4. **FAIL**

## Per-Seed Results

  SUP seed=42: cosine_sim=0.9999999403953552 terrain_acc=0.7054 C1=FAIL C3=PASS
  SUP seed=7: cosine_sim=0.9999999403953552 terrain_acc=0.5980 C1=FAIL C3=PASS
  SUP seed=11: cosine_sim=0.9999999403953552 terrain_acc=0.5502 C1=FAIL C3=PASS
  SUP seed=99: cosine_sim=0.9999999403953552 terrain_acc=0.5100 C1=FAIL C3=FAIL
  SUP seed=31: cosine_sim=1.000000238418579 terrain_acc=0.6581 C1=FAIL C3=PASS

  ABL seed=42: cosine_sim=1.0 terrain_acc=0.7054 C4=PASS
  ABL seed=7: cosine_sim=1.0 terrain_acc=0.5980 C4=PASS
  ABL seed=11: cosine_sim=1.0 terrain_acc=0.5502 C4=PASS
  ABL seed=99: cosine_sim=0.9999999403953552 terrain_acc=0.5100 C4=PASS
  ABL seed=31: cosine_sim=0.9999999403953552 terrain_acc=0.6581 C4=PASS
