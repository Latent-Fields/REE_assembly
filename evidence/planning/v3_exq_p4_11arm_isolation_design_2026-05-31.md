# V3-EXQ-P4 -- Phase P4 Full 11-Arm Isolation Matrix Design

**Created:** 2026-05-31T12:51Z
**Author session:** design-v3-exq-p4-11arm-isolation-20260531T125115Z
**Status:** STAGED -- design doc only; NOT queued. Submission gated on V3-EXQ-614b PASS.
**Reserved queue ID:** V3-EXQ-618 (assignment confirmed at queue-time)
**Plan-of-record parent:** [`behavioral_diversity_isolation_plan.md`](behavioral_diversity_isolation_plan.md) sections "Isolation matrix" + "Experiment sequencing -> Phase P4"
**Closest fork:** [`ree-v3/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py) (3-arm; this design extends ARMS list to 11 entries with identical env + amend + measurement scaffolding)

---

## 1. Purpose

Phase P4 runs the full 11-arm isolation matrix specified by
`behavioral_diversity_isolation_plan.md`. Each arm fixes ON/OFF state for all four
candidate substrates (SP-CEM / MECH-341 / MECH-313 / V_s) on the same env + seed
set so cross-arm comparison is on matched data. Applies the **R_X cross-theory
escalation rules** (R_X.a emergent, R_X.b partial redundancy, R_X.c expand to
theories 5-8). Closes the GAP-B / GAP-A behavioural-diversity story at the
all-axes-at-once layer that the earlier 3-arm phases could not reach.

The 11-arm matrix is the **definitive isolation test** -- it is what tells us
whether observed behavioural diversity at ALL_ON is emergent across substrates
(no single layer load-bearing), partially redundant across substrate pairs, or
genuinely missing (escalate to theories 5-8 / proposal-distribution bias,
MECH-260 anti-recency, MECH-314 curiosity, z_goal config-default).

This is **NOT** a substrate-readiness diagnostic; it is the **behavioural
governance run** that arbitrates R_X.a/b/c on the four ARC-065 child substrates.

---

## 2. Gating dependencies (DO NOT QUEUE UNTIL ALL CLEAR)

| Gate | Description | Current status (2026-05-31T12:51Z) |
|------|-------------|------------------------------------|
| **G1** | **V3-EXQ-614b PASS** (MECH-341 amend re-run on SD-056-amended substrate; 3-arm B_only / ablate_B / ALL_ON falsifier; supersedes 614a) | **PENDING** -- queued 2026-05-31T12:32Z (priority 250). This is the load-bearing gate. P4 fires AFTER 614b PASSes. |
| G2 | V3-EXQ-616 Q-054 entropy_bias_scale sweep | PENDING -- queued 2026-05-31T11:14Z (priority 100). 4-arm scale sweep {1.0, 2.0, 4.0, 8.0} on B_only isolation. Informs MECH-341 scale calibration; P4 reads the load-bearing-scale finding to set `e3_diversity_entropy_bias_scale` for B-ON arms. |
| G3 | V3-EXQ-569a ARC-065 GAP-A R1.b matched-entropy FP-2 | PENDING -- queued 2026-05-31T12:47Z (priority 400). 5-arm SD-056-amended matched-entropy falsifier. Informs whether ARM_A_only is expected to clear Rung 1 in isolation. |
| G4 | Rung 2 SD-054 clearance | Plan-doc cites this as the original P4 gate. Per the closure-plan walk 2026-05-31, GAP-B partial-PASS on R2.c (PASS via C2+C3 at 614a) satisfies the Rung-2 requirement at the diagnostic-probe level. Confirm at queue time. |

**Decision rule for queue-time:** queue P4 only when G1 has landed PASS AND
G2 has landed (any outcome; G2 informs scale, not gate). G3 and G4 are
informative but not load-bearing gates -- P4 can proceed if they remain
PENDING but the rationale in the queue entry must note the gap. **If G1 FAILs**
the routing is to `/diagnose-errors` on the SD-056 amended substrate + MECH-341
integration; P4 stays staged until a successor PASSes.

---

## 3. The 11-arm isolation matrix (exact specs)

All arms share **identical** `env_kwargs`, `SEEDS`, phase budgets, and SD-056
amend lever flags (held constant -- see Section 4). The only between-arm
variation is the 4-substrate ON/OFF dict and the MATCHED_NOISE temperature lift.

| # | arm_id | A SP-CEM | B MECH-341 | C MECH-313 | D V_s | Notes |
|---|--------|:--------:|:----------:|:----------:|:-----:|------|
| 0 | ARM_0_BASE_OFF | off | off | off | off | Rung 0 baseline (ARC-065 architectural-necessity check) |
| 1 | ARM_1_ALL_ON | **on** | **on** | **on** | **on** | Rung 1 target |
| 2 | ARM_2_A_only | **on** | off | off | off | Theory 1 contribution (SP-CEM in isolation; cross-checks V3-EXQ-569a) |
| 3 | ARM_3_B_only | off | **on** | off | off | Theory 2 contribution (MECH-341 in isolation; cross-checks V3-EXQ-614b) |
| 4 | ARM_4_C_only | off | off | **on** | off | Theory 3 contribution (MECH-313 noise floor in isolation) |
| 5 | ARM_5_D_only | off | off | off | **on** | Theory 4 contribution (V_s in isolation; cross-checks V3-EXQ-550 / 601 diagnostic-probe reading) |
| 6 | ARM_6_ablate_A | off | **on** | **on** | **on** | Marginal cost of removing SP-CEM |
| 7 | ARM_7_ablate_B | **on** | off | **on** | **on** | Marginal cost of removing MECH-341 (cross-checks 614b ARM_1) |
| 8 | ARM_8_ablate_C | **on** | **on** | off | **on** | Marginal cost of removing MECH-313 |
| 9 | ARM_9_ablate_D | **on** | **on** | **on** | off | Marginal cost of removing V_s |
| 10 | ARM_10_MATCHED_NOISE | off | off | C-style temp lift only (T=2.5) | off | FP-2 control: structured-vs-noise comparison for Rung 1 |

### Axis -> config-flag mapping (verbatim from 614b _make_agent, extended to MATCHED_NOISE)

```
A_sp_cem (SP-CEM main-path):
  use_support_preserving_cem
  support_preserving_stratified_elites
  support_preserving_ao_std_floor = 0.2 (ON) / 0.0 (OFF)

B_mech341 (E3 score diversity preservation):
  use_e3_score_diversity (master)
  use_e3_diversity_entropy_bonus + use_e3_diversity_stratified_select (both ON when B ON)
  e3_diversity_entropy_bias_scale = MECH341_ENTROPY_BIAS_SCALE
    (read from V3-EXQ-616 Q-054 sweep load-bearing scale; default 2.0 if 616 inconclusive)

C_noise_floor (MECH-313 tonic noise floor):
  use_noise_floor
  noise_floor_alpha = 0.1 (default)
  noise_floor_min_temperature = 1.0 (default)

D_vs (minimal V_s pathology stack -- user-confirmed 2026-05-29 scope):
  use_per_stream_vs
  use_vs_rollout_gating
  vs_gate_snapshot_refresh_threshold = 0.5
  vs_gate_e1_threshold = 0.4
  NO anchor_sets, NO staleness_accumulator, NO event_segmenter, NO invalidation_trigger.

MATCHED_NOISE (ARM_10, FP-2 control per plan-doc Section "Isolation matrix"):
  All four axes OFF.
  Override softmax temperature at e3.select() to T=2.5 uniformly (lifts entropy
  to noise-matched magnitude without invoking any of A/B/C/D mechanisms).
  Implemented via experiment-side override of E3 effective_temperature
  bypassing MECH-313 noise_floor (which is OFF). The lever is a pure
  temperature kwarg pass, not a config flag.
```

### SD-056 amend levers (held constant across ALL 11 arms)

Inherited verbatim from V3-EXQ-614b so the amend is not confounded with the
A/B/C/D axis state. From [`ree-v3/CLAUDE.md`](https://github.com/Latent-Fields/ree-v3/blob/main/CLAUDE.md) "SD-056
multi-step rollout stability amend (2026-05-31)" section:

| Flag | Value | Lever |
|------|-------|-------|
| `e2_action_contrastive_multistep_enabled` | True | (a) primary -- multi-step InfoNCE h=5 |
| `e2_action_contrastive_horizon` | 5 | Dreamer default |
| `e2_rollout_output_norm_clamp_enabled` | True | (b) defensive -- per-step output norm clamp |
| `e2_rollout_output_norm_clamp_ratio` | 2.0 | B2 anchor from V3-EXQ-569e autopsy acceptance |
| `e2_action_contrastive_enabled` | True | t=1 contrastive (substrate baseline) |
| `e2_action_contrastive_weight` | 0.01 | Substrate default |

---

## 4. Acceptance grid (R_X.a / R_X.b / R_X.c)

Per-arm Rung-1 metric (computed on P1 instrumented window):

- `n_unique_selected_classes` (per seed): count of distinct first-action classes
  in the selected-trajectory pool over P1.
- `selected_action_class_entropy_nats` (per seed): Shannon entropy in nats over
  the selected-class distribution.
- **Arm "passes Rung 1"** iff `n_unique_selected_classes >= 2 AND
  selected_action_class_entropy_nats > 0.3` on >= 2/3 seeds (matches 614a / 614b
  C1 thresholds; matches plan-doc R1.a / R1.b / R2.c rules).

### R_X.a -- Emergent across substrates

**Predicate:** `ARM_1_ALL_ON passes Rung 1` AND
`ARM_2_A_only / ARM_3_B_only / ARM_4_C_only / ARM_5_D_only all individually FAIL Rung 1`.

**Routing:** diversity is emergent across the full 4-substrate stack; no single
layer is load-bearing. **Promote ARC-065** on multi-arm evidence; INV-074
plasticity-crystallization invariant fires (architectural-necessity reading).
MECH-341 / MECH-313 / MECH-269b / SP-CEM each retain `supports` direction at
provisional confidence, none upgraded to load-bearing-sole.

### R_X.b -- Partial redundancy

**Predicate:** `ARM_1_ALL_ON passes Rung 1` AND
**two or more** of `ARM_2..5` individually pass Rung 1.

**Routing:** substrates are partially redundant. Open a new Q-claim covering
the redundancy pair (e.g. A-vs-C if ARM_2 and ARM_4 both pass); revisit Q-045
(MECH-313 vs MECH-260 independence) with the new evidence. ARC-065 supports;
the specific substrate-pair redundancy claim becomes the next decision target.

### R_X.c -- Expand to theories 5-8

**Predicate:** `ARM_1_ALL_ON FAILS Rung 1`.

**Routing:** the 4-substrate stack as currently specified is insufficient.
Expand candidate set to theories 5-8 (GAP-E proposal-distribution bias /
GAP-F MECH-260 anti-recency / GAP-G MECH-314 curiosity weight / GAP-H z_goal
config-default confound). De-prioritise further A/B/C/D refinement; the next
governance cycle should promote one of theories 5-8 to active candidate
status. MECH-341 / MECH-313 / MECH-269b stay at their pre-P4 status; ARC-065
becomes `pending_retest_after_substrate` with respect to the
non-current-candidate-set unblock.

### Per-ablation marginal-cost arms (R_X.b refinement)

`ARM_6..9` (ablate_A / B / C / D) provide marginal-cost estimates per substrate:

- If ablate_X FAILS Rung 1 while ALL_ON passes -> X is necessary in the stack
  (consistent with X being load-bearing).
- If ablate_X passes Rung 1 -> X is redundant under combined substrate
  (consistent with R_X.b partial redundancy; X may be a candidate for
  de-prioritisation).

These are read SECONDARILY to the R_X.a/b/c primary disposition.

### MATCHED_NOISE (FP-2 control)

`ARM_10` provides the structured-vs-noise baseline:

- If `ARM_2..5` (any single-substrate arm) **does not strictly exceed**
  `ARM_10` on `selected_action_class_entropy_nats`, FP-2 is not cleared for
  that substrate in isolation -- the substrate's contribution is
  noise-matched, not structurally-driven.
- This is the FP-2 falsifier carried over from V3-EXQ-569 / 569a / 614b
  matched-entropy methodology; applies per-arm to the four single-axis arms.

### Overall outcome interpretation grid (6 rows)

| Row | Pattern | Routing |
|-----|---------|---------|
| R_X.a fires | ALL_ON pass; A/B/C/D singles all fail | /governance ARC-065 promotion + INV-074 fire; close P4 with R_X.a stamp |
| R_X.b fires (one redundant pair) | ALL_ON pass; exactly 2 singles pass | /governance new Q-claim on the redundant pair; ARC-065 supports; close P4 with R_X.b stamp |
| R_X.b fires (broad redundancy) | ALL_ON pass; 3-4 singles pass | /governance redundancy walk; revisit substrate prioritisation across the cluster |
| Single load-bearing | ALL_ON pass; exactly 1 single arm passes, others fail; that arm's ablation FAILS | /governance promote that substrate's claim; ARC-065 supports with single-load-bearing reading |
| R_X.c fires | ALL_ON FAILS | /queue-experiment theories 5-8 cluster; close P4 with R_X.c stamp; ARC-065 pending_retest_after_substrate against new candidate set |
| Internal contradiction | e.g. ALL_ON fails AND multiple singles pass | /failure-autopsy on the 11-arm cluster; do NOT apply R_X stamps until autopsy resolves |

---

## 5. Data plan

### 5.1 Seeds + episode budget

Inherited from 614b lineage for direct cross-cluster manifest comparability:

```
SEEDS                  = [42, 43, 44]
P0_WARMUP_EPISODES     = 30          # encoder + E2 warmup; no instrumentation
P1_MEASUREMENT_EPISODES = 60         # instrumented; per-tick metrics emitted
STEPS_PER_EPISODE      = 200
```

**Total per arm:** 3 seeds * (30 + 60) ep * 200 steps = 54k steps.
**Total run budget:** 11 arms * 54k = 594k steps.

### 5.2 Per-arm matched-data requirement

All 11 arms run on the **same** `env_kwargs` + same `SEEDS`. Per-arm
verdict requires `len(seed_verdicts_passing_per_arm_rung1) >= 2` (matches
`MIN_SEEDS_PER_ARM_FOR_PASS = 2` of the 614b lineage). MATCHED_NOISE has
the same data shape so cross-arm comparison is bit-stable across the FP-2
gate.

### 5.3 Runtime estimate

Per-tick cost matches 614b (3 arms * 54k = 162k steps; observed Mac runtime
~50-60 min on DLAPTOP-4.local @ ~14 steps/sec). Extrapolating linearly:
**~180-220 min on Mac**, or **~70-90 min on ree-cloud-2/3** (~2.3x Mac per
cloud_workers.md). Recommended machine_affinity: "any" (so the cloud-scaler
can pick up the work; surge mode may bring ree-worker-4 online if cloud-2/3
saturate per the 2026-05-31 cloud-preference Lever 2).

**estimated_minutes:** 240 (conservative; budget for cloud-2 CX22 with
contrastive overhead at full P1 budget).

### 5.4 Per-tick metric stack (inherited verbatim from 614b / 611c)

- `selected_action_class_entropy_nats[t]`
- `n_unique_selected_classes[t]`
- `mean_top2_class_gap[t]` (cross-arm comparison anchor against V3-EXQ-608 P2 baseline)
- `frac_pre_ge2[t]` (substrate-operative gate per V3-EXQ-611c)
- `entropy_bonus_max_abs[t]` (when B ON; instrumentation for MECH-341 firing)
- `n_stratified_fired[t]` (when B ON; instrumentation for MECH-341 OPT2 firing)
- `cand_world_pairwise_dist[t]` (instrumentation for SD-056 substrate stability per V3-EXQ-617 PASS)
- `rollout_skipped_nonfinite[t]` (defensive; should stay 0 with multistep amend ON)
- Per-arm headline: `seed_verdict_rung1`, `seed_verdict_fp2_vs_matched_noise`
  (computed at end-of-arm against ARM_10 stats).

### 5.5 Sentinel / instrumentation contract

Manifest must emit `sd056_amend_active` block with all 6 amend flag values
read off the constructed REEConfig. This is the integration-stability
crosscheck that V3-EXQ-617 substrate-readiness PASS still holds at
behavioural-runtime scale on the 11-arm cluster.

---

## 6. V3 substrate tagging requirements (mandatory)

Per [`REE_assembly/CLAUDE.md`](../../CLAUDE.md) "Experiment Result Tagging" and
"evidence_direction: Per-Experiment Default with Optional Per-Claim Overrides":

```
run_id:               must end "_v3"
architecture_epoch:   "ree_hybrid_guardrails_v1"
claim_ids:            ["ARC-065", "MECH-341", "MECH-313", "MECH-269b"]
                      (multi-claim per the 11-arm matrix; ARC-065 is the
                       parent distributed-pathway architecture; MECH-341 /
                       MECH-313 / MECH-269b are the three substrate-side
                       children under test. SP-CEM is the ARC-065 child for
                       Layer A; absorbed into ARC-065 tag rather than tagged
                       separately to avoid double-counting.)
experiment_purpose:   "evidence"  (weighted in confidence + conflict scoring
                       per Phase-3 governance rules)
evidence_direction:   computed from the 6-row interpretation grid (see Sec 4).
                       overall summary value:
                         R_X.a fires           -> "supports" (architectural-necessity)
                         R_X.b fires           -> "supports" (with new Q-claim)
                         Single load-bearing   -> "supports" (with promotion target identified)
                         R_X.c fires           -> "weakens" (4-substrate stack insufficient)
                         Internal contradiction -> "inconclusive"
evidence_direction_per_claim: per-claim direction MANDATORY (multi-claim).
                       Filled from the interpretation grid row that fires.
                       Example R_X.a:
                         {"ARC-065": "supports", "MECH-341": "mixed",
                          "MECH-313": "mixed", "MECH-269b": "mixed"}
                       Example single-load-bearing on B:
                         {"ARC-065": "supports", "MECH-341": "supports",
                          "MECH-313": "non_contributory",
                          "MECH-269b": "non_contributory"}
evidence_direction_note: free-form paragraph citing the interpretation row
                       and per-arm verdict counts.
supersedes:           none (P4 is a phase-extension, not a successor to 614b;
                       614b stays as the 3-arm Phase-P3 anchor evidence)
```

---

## 7. Closest parent fork + skeleton sketch (no full implementation in this session)

### 7.1 Fork choice rationale

**Closest parent:** [`ree-v3/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py`](https://github.com/Latent-Fields/ree-v3/blob/main/experiments/v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py)
(1026 lines).

**Why this fork over alternatives:**

- **vs 614a** (3-arm pre-amend): 614b carries the SD-056 amend levers in
  `_make_agent` exactly as P4 needs them (all 11 arms must hold the amend
  constant). 614a would force re-derivation.
- **vs 611c** (6-arm MECH-341 retune): 611c is OPT1/OPT2/BOTH x scale=1.0/2.0
  factorial -- different axis decomposition, doesn't share the 4-substrate
  isolation framing.
- **vs 616** (Q-054 sweep): 616 sweeps only entropy_bias_scale on B_only;
  single-axis sweep, different design language than the matrix.
- **vs 569a** (5-arm A_only matched-entropy): 569a is single-axis A_only
  weight sweep, not multi-axis isolation.

614b is the **only** existing script that builds the (SP-CEM, MECH-341,
MECH-313, V_s) axis-state dict + applies SD-056 amend constants + reads from
that dict into `REEConfig.from_dims`. P4 forks 614b and extends `ARMS` from
3 entries to 11.

### 7.2 Skeleton structure (NOT a runnable script; queue session writes it)

```python
#!/opt/local/bin/python3
"""
V3-EXQ-618 -- Phase P4 full 11-arm isolation matrix on the SD-056-amended substrate.

Forked from V3-EXQ-614b (3-arm B_only / ablate_B / ALL_ON). This script extends
the ARMS list to the 11-arm matrix specified by
behavioral_diversity_isolation_plan.md Section "Isolation matrix" and applies
the R_X.a/b/c cross-theory escalation rules per Section "Decision rules".

Gates_on_exq: V3-EXQ-614b (MECH-341 amend-and-re-run cycle MUST PASS first).
Informed by: V3-EXQ-616 (Q-054 entropy_bias_scale sweep; sets MECH341_ENTROPY_BIAS_SCALE),
            V3-EXQ-569a (ARC-065 GAP-A R1.b matched-entropy FP-2 falsifier;
                        informs A_only expectation).

(Full pre-registration docstring + interpretation grid copied from this
 design doc Section 4 -- 6 rows: R_X.a / R_X.b one-redundant-pair / R_X.b
 broad-redundancy / single-load-bearing / R_X.c / internal-contradiction.)
"""

from __future__ import annotations
import argparse, json, math, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import torch

from experiment_protocol import emit_outcome
from ree_core.agent import REEAgent
from ree_core.environment.causal_grid_world import CausalGridWorldV2
from ree_core.utils.config import REEConfig

EXPERIMENT_TYPE = "v3_exq_618_p4_isolation_matrix_11arm_sd056_amended"
QUEUE_ID = "V3-EXQ-618"
CLAIM_IDS = ["ARC-065", "MECH-341", "MECH-313", "MECH-269b"]
EXPERIMENT_PURPOSE = "evidence"

# SD-056 amend constants -- IDENTICAL TO V3-EXQ-614b (held across all 11 arms).
SD056_MULTISTEP_CONTRASTIVE = True
SD056_CONTRASTIVE_HORIZON = 5
SD056_OUTPUT_NORM_CLAMP = True
SD056_OUTPUT_NORM_CLAMP_RATIO = 2.0
SD056_T1_CONTRASTIVE_ENABLED = True
SD056_T1_CONTRASTIVE_WEIGHT = 0.01

# Budget -- IDENTICAL TO V3-EXQ-614b lineage.
SEEDS = [42, 43, 44]
P0_WARMUP_EPISODES = 30
P1_MEASUREMENT_EPISODES = 60
STEPS_PER_EPISODE = 200

# Pre-registered behavioural thresholds (R_X.a/b/c per Rung 1).
RUNG1_ENTROPY_THRESHOLD = 0.3
RUNG1_MIN_CLASSES = 2
MIN_SEEDS_PER_ARM_FOR_PASS = 2

# MECH-341 scale: load-bearing value from V3-EXQ-616 Q-054 sweep.
# DEFAULT 2.0 if 616 inconclusive at queue-time. Update at submission.
MECH341_ENTROPY_BIAS_SCALE = 2.0

# V_s thresholds (minimal stack, identical to 614b).
VS_SNAPSHOT_REFRESH_THRESHOLD = 0.5
VS_E1_THRESHOLD = 0.4

# Noise floor (MECH-313) default knobs.
NOISE_FLOOR_ALPHA = 0.1
NOISE_FLOOR_MIN_TEMPERATURE = 1.0

# MATCHED_NOISE control temperature (FP-2 lift).
MATCHED_NOISE_TEMPERATURE = 2.5

# ENV_KWARGS -- IDENTICAL TO V3-EXQ-611/611b/611c/614a/614b lineage.
ENV_KWARGS = dict(
    size=12, num_hazards=4, num_resources=5, hazard_harm=0.05,
    env_drift_interval=5, env_drift_prob=0.1,
    proximity_harm_scale=0.1, proximity_benefit_scale=0.05,
    proximity_approach_threshold=0.2,
    hazard_field_decay=0.5, resource_respawn_on_consume=True,
    toroidal=False, harm_history_len=10,
    reef_enabled=True, n_reef_patches=3, reef_patch_radius=2,
    hazard_food_attraction=0.7,
    reef_bipartite_layout=True, reef_bipartite_axis="horizontal",
    reef_bipartite_agent_band_radius=1,
)


ARMS: List[Dict[str, Any]] = [
    # ARM_0 -- BASE_OFF (Rung 0 baseline)
    {"arm_id": "ARM_0_BASE_OFF", "label": "base_off",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": False,
                        "C_noise_floor": False, "D_vs": False},
     "matched_noise_override": False},
    # ARM_1 -- ALL_ON (Rung 1 target)
    {"arm_id": "ARM_1_ALL_ON", "label": "all_on",
     "substrate_axes": {"A_sp_cem": True, "B_mech341": True,
                        "C_noise_floor": True, "D_vs": True},
     "matched_noise_override": False},
    # ARM_2..5 -- single-substrate (A/B/C/D)_only
    {"arm_id": "ARM_2_A_only", "label": "a_only_sp_cem_isolated",
     "substrate_axes": {"A_sp_cem": True, "B_mech341": False,
                        "C_noise_floor": False, "D_vs": False},
     "matched_noise_override": False},
    {"arm_id": "ARM_3_B_only", "label": "b_only_mech341_isolated",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": True,
                        "C_noise_floor": False, "D_vs": False},
     "matched_noise_override": False},
    {"arm_id": "ARM_4_C_only", "label": "c_only_noise_floor_isolated",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": False,
                        "C_noise_floor": True, "D_vs": False},
     "matched_noise_override": False},
    {"arm_id": "ARM_5_D_only", "label": "d_only_vs_isolated",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": False,
                        "C_noise_floor": False, "D_vs": True},
     "matched_noise_override": False},
    # ARM_6..9 -- ablate_(A/B/C/D)
    {"arm_id": "ARM_6_ablate_A", "label": "ablate_a_bcd_on",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": True,
                        "C_noise_floor": True, "D_vs": True},
     "matched_noise_override": False},
    {"arm_id": "ARM_7_ablate_B", "label": "ablate_b_acd_on",
     "substrate_axes": {"A_sp_cem": True, "B_mech341": False,
                        "C_noise_floor": True, "D_vs": True},
     "matched_noise_override": False},
    {"arm_id": "ARM_8_ablate_C", "label": "ablate_c_abd_on",
     "substrate_axes": {"A_sp_cem": True, "B_mech341": True,
                        "C_noise_floor": False, "D_vs": True},
     "matched_noise_override": False},
    {"arm_id": "ARM_9_ablate_D", "label": "ablate_d_abc_on",
     "substrate_axes": {"A_sp_cem": True, "B_mech341": True,
                        "C_noise_floor": True, "D_vs": False},
     "matched_noise_override": False},
    # ARM_10 -- MATCHED_NOISE (FP-2 control)
    {"arm_id": "ARM_10_MATCHED_NOISE", "label": "matched_noise_temp_2_5",
     "substrate_axes": {"A_sp_cem": False, "B_mech341": False,
                        "C_noise_floor": False, "D_vs": False},
     "matched_noise_override": True},  # override e3 softmax temperature at select-time
]


def _make_env(seed: int) -> CausalGridWorldV2:
    return CausalGridWorldV2(seed=seed, **ENV_KWARGS)


def _make_agent(env: CausalGridWorldV2, axes: Dict[str, bool]) -> REEAgent:
    # IDENTICAL to V3-EXQ-614b _make_agent; the axes dict already covers all
    # 11-arm states (the MATCHED_NOISE override is applied at e3.select() time
    # via the temperature kwarg, NOT via _make_agent).
    # ... (full body forked verbatim from 614b; SD-056 amend lever flags
    #      applied uniformly; A/B/C/D axes read into REEConfig.from_dims)
    ...


def _run_arm(arm: Dict[str, Any], seed: int, p0_eps: int, p1_eps: int,
             steps_per_ep: int) -> Dict[str, Any]:
    # IDENTICAL P0+P1 loop structure to V3-EXQ-614b _run_arm. New override
    # block: when arm["matched_noise_override"] is True, override the
    # e3 softmax temperature to MATCHED_NOISE_TEMPERATURE for the duration of
    # the arm (lifted via REEAgent.select_action's existing
    # effective_temperature kwarg passing path; bypass MECH-313 noise_floor
    # which is OFF on this arm anyway).
    env = _make_env(seed)
    agent = _make_agent(env, arm["substrate_axes"])
    if arm["matched_noise_override"]:
        # Stash temperature override on agent for the select_action site to read.
        agent._matched_noise_temp_override = MATCHED_NOISE_TEMPERATURE  # noqa
    # ... (P0 warmup + P1 instrumented; per-tick metric emission via
    #      _per_class_score_stats / _entropy_from_counts helpers reused
    #      verbatim from 614b)
    ...


def _compute_seed_verdict_rung1(arm_metrics: Dict[str, Any]) -> bool:
    # n_unique_selected_classes >= 2 AND selected_action_class_entropy_nats > 0.3
    ...


def _compute_arm_verdict(seed_verdicts: List[bool]) -> bool:
    # sum(seed_verdicts) >= MIN_SEEDS_PER_ARM_FOR_PASS
    ...


def _apply_r_x_interpretation(arm_verdicts: Dict[str, bool],
                               matched_noise_stats: Dict[str, Any]) -> Dict[str, Any]:
    # 6-row interpretation grid from design doc Section 4:
    #   row 1: R_X.a fires
    #   row 2: R_X.b one-redundant-pair
    #   row 3: R_X.b broad-redundancy
    #   row 4: single load-bearing
    #   row 5: R_X.c fires
    #   row 6: internal contradiction
    # Returns interpretation_label + evidence_direction_per_claim dict.
    ...


def main() -> Tuple[Optional[str], Optional[str]]:
    # Argparse for --dry-run; build manifest; emit_outcome with
    # supersedes=None + experiment_purpose=evidence + per-claim direction
    # filled from _apply_r_x_interpretation.
    ...


if __name__ == "__main__":
    main()
```

**What lands at queue-time (NOT this session):**

1. Fill in `_make_agent` body verbatim from 614b.
2. Fill in `_run_arm` P0+P1 loop verbatim from 614b + MATCHED_NOISE temperature
   override path.
3. Fill in `_apply_r_x_interpretation` from Section 4 6-row grid.
4. Smoke-test 11 arms x 1 seed x 2+2 ep x 30 steps `--dry-run`.
5. Validate via `validate_experiments.py` AST PASS + `validate_queue.py` PASS.
6. /queue-experiment with the staged queue entry (Section 8 below) + smoke
   evidence in completion_note.

---

## 8. Staged draft queue entry (NOT inserted; submit via /queue-experiment when G1 PASSes)

```json
{
  "queue_id": "V3-EXQ-618",
  "title": "Phase P4 -- full 11-arm isolation matrix; R_X.a/b/c arbitration on ARC-065 child substrates",
  "priority": 90,
  "status": "pending",
  "machine_affinity": "any",
  "estimated_minutes": 240,
  "claim_id": "ARC-065",
  "claim_ids": ["ARC-065", "MECH-341", "MECH-313", "MECH-269b"],
  "experiment_purpose": "evidence",
  "experiment_type": "v3_exq_618_p4_isolation_matrix_11arm_sd056_amended",
  "gates_on_exq": "V3-EXQ-614b",
  "design_doc": "REE_assembly/evidence/planning/v3_exq_p4_11arm_isolation_design_2026-05-31.md",
  "note": "Phase P4 of behavioral_diversity_isolation_plan.md -- the full 11-arm isolation matrix (BASE_OFF / ALL_ON / A_only / B_only / C_only / D_only / ablate_A/B/C/D / MATCHED_NOISE) covering all 4 ARC-065 child substrate layers (SP-CEM A / MECH-341 B / MECH-313 C / V_s D). Applies R_X.a (emergent across substrates) / R_X.b (partial redundancy) / R_X.c (expand to theories 5-8) cross-theory escalation rules. SD-056 amend levers (multistep h=5 + output norm clamp ratio=2.0 + t=1 contrastive at weight 0.01) held constant uniformly across all 11 arms so amend on/off is not confounded with A/B/C/D axis state -- identical pattern to V3-EXQ-614b. Env IDENTICAL to V3-EXQ-611/611b/611c/614a/614b (size=12, num_hazards=4, num_resources=5, hazard_food_attraction=0.7, reef_bipartite_layout=True, harm_history_len=10) for direct cross-cluster manifest comparability. Budget: 11 arms x 3 seeds x 90 ep x 200 steps = 594k steps; ~240 min on cloud-2/3 CX22. Acceptance: per-arm Rung 1 (n_unique_selected_classes >= 2 AND selected_action_class_entropy_nats > 0.3 on >= 2/3 seeds); overall interpretation via 6-row grid in design doc Section 4. MECH341_ENTROPY_BIAS_SCALE READ FROM V3-EXQ-616 Q-054 sweep load-bearing-scale result at queue-time (default 2.0 if 616 inconclusive). MATCHED_NOISE arm uses softmax temperature T=2.5 lifted at e3.select() override path (bypasses MECH-313 noise_floor which is OFF). Gates_on_exq=V3-EXQ-614b: P4 does NOT fire until 614b (MECH-341 amend-and-re-run cycle) PASSes; queue submission BLOCKED until then per behavioral_diversity_isolation_plan.md Phase P4 gating. claim_ids=[ARC-065, MECH-341, MECH-313, MECH-269b]; evidence_direction_per_claim filled from the interpretation row that fires (see design doc Section 6 tagging requirements). SP-CEM is the Layer A ARC-065 child; absorbed into ARC-065 tag to avoid double-counting (ARC-065 + a separate Layer-A claim would over-credit). Cross-link: behavioral_diversity_isolation_plan.md GAP-A/B/C/D nodes + design doc v3_exq_p4_11arm_isolation_design_2026-05-31.md."
}
```

**Why priority 90 (one rung below V3-EXQ-616's priority=100):** P4 is the
broadest test of the cluster (11 arms x 3 seeds x 90 ep = 240+ min) and
depends on 614b having PASSed; running it before the cluster's lighter
in-flight EXQs would consume budget before the load-bearing signals
(614b GAP-B reading + 616 Q-054 scale + 569a GAP-A R1.b) have landed. Priority
90 puts P4 below 616 (Q-054 sweep, priority 100) and well below 569a (GAP-A
R1.b, priority 400) and 614b (GAP-B re-run, priority 250) -- the correct
ordering for "this fires once the cluster's lighter falsifiers settle."
User-confirmed acceptable per chip ("priority equal to or one rung below
V3-EXQ-616").

---

## 9. Dependencies + cross-plan links

### 9.1 In-flight gating dependencies (Section 2 expanded)

- **V3-EXQ-614b** (PRIMARY gating EXQ; PASS required): MECH-341 amend
  re-run on SD-056-amended substrate. queued 2026-05-31T12:32Z @ priority 250.
  Loop: P4 fires AFTER 614b PASS. If 614b FAILs, P4 stays staged; routing
  changes to whatever 614b's failure mode reveals (likely /diagnose-errors
  on SD-056 + MECH-341 integration before re-staging P4).
- **V3-EXQ-616** (INFORMATIVE; sets B-scale knob): Q-054 entropy_bias_scale
  sweep on B_only. queued 2026-05-31T11:14Z @ priority 100. At queue-time
  read the load-bearing scale from 616 manifest and set
  `MECH341_ENTROPY_BIAS_SCALE`. Default 2.0 if 616 inconclusive.
- **V3-EXQ-569a** (INFORMATIVE; informs ARM_2_A_only expectation): ARC-065
  GAP-A R1.b matched-entropy FP-2 falsifier. queued 2026-05-31T12:47Z @
  priority 400. Read at queue-time to set FP-2 expectation on ARM_2.
- **V3-EXQ-569e autopsy** (CONTEXTUAL; routes 569e mixed-direction): SD-056
  multistep amend exists BECAUSE of 569e INSTRUMENTATION_FAILURE; P4 is
  the second behavioural test of the amended substrate (after 614b).
- **V3-EXQ-617** (CONTEXTUAL; substrate-readiness anchor): SD-056 amend
  substrate-readiness PASS 2026-05-31T11:31Z. Confirms SD-056 stable at
  the synthetic-batch layer; P4 + 614b are the behavioural-layer verifies.

### 9.2 Cross-plan links

- **arc_062_rule_apprehension:GAP-B** -- same SD-056-amended substrate; P4's
  result on ARM_3_B_only (B-only) directly informs whether the ARC-062
  GAP-B V3-EXQ-543l successor cohort should expect contributory readings
  under the stabilised substrate.
- **arc_062_rule_apprehension:GAP-H** -- ARC-065 substrate work; P4 closes
  the loop on whether SP-CEM (Layer A) is independently sufficient (ARM_2
  reading).
- **commitment_closure_plan.md** -- GAP-4 substrate-readiness (MECH-090 R-c)
  is unrelated to P4's substrate scope; no cross-plan dependency.
- **goal_pipeline:GAP-4** -- z_goal-collapse blocker is upstream of GAP-C
  in the diversity plan but does NOT block P4 (Layer C and Layer D both
  have V3-EXQ-544 / 545 / 550 / 601 substrate-readiness PASSes; the
  z_goal-collapse is a separate substrate-ceiling cluster).

### 9.3 Downstream beneficiaries (post-P4 routing)

- **ARC-065 governance state:** the R_X stamp lands in claims.yaml at the
  next /governance cycle; routes ARC-065 v3_pending flag based on which
  row of the 6-row grid fires.
- **MECH-341 / MECH-313 / MECH-269b:** per-claim direction overrides
  applied per Section 6; promotion / demotion happens at the next
  /governance cycle.
- **Theories 5-8 cluster** (if R_X.c fires): GAP-E / GAP-F / GAP-G / GAP-H
  in behavioral_diversity_isolation_plan.md become active candidate
  substrates; next /queue-experiment session targets one of them
  (proposal-distribution bias / MECH-260 anti-recency / MECH-314 curiosity /
  z_goal config-default).

---

## 10. What this design doc does NOT do

- **Does not write the experiment script.** Skeleton sketch only; full
  implementation lands in the /queue-experiment session after G1 (614b)
  PASSes.
- **Does not insert into experiment_queue.json.** Draft queue entry staged
  in Section 8; submission via /queue-experiment when gates clear.
- **Does not pin MECH341_ENTROPY_BIAS_SCALE.** Final value comes from
  V3-EXQ-616 Q-054 sweep at queue-time; this doc fixes 2.0 as the fallback
  default.
- **Does not address theories 5-8.** Those are gated on R_X.c firing in
  P4; if R_X.a or R_X.b fires, theories 5-8 remain deferred candidates.
- **Does not redefine acceptance criteria.** Rung 0-4 framework in
  `behavioral_diversity_acceptance_criteria.md` and decision rules in
  `behavioral_diversity_isolation_plan.md` are authoritative; this design
  doc inherits and applies them.

---

## 11. Submission checklist (for the queue session that fires this)

When V3-EXQ-614b PASSes:

1. Re-read 614b manifest to confirm PASS interpretation row + per-claim
   directions for context.
2. Re-read V3-EXQ-616 manifest if landed; read load-bearing scale; set
   `MECH341_ENTROPY_BIAS_SCALE` accordingly.
3. Re-read V3-EXQ-569a manifest if landed; read FP-2 result for A_only
   expectation; record in queue entry note.
4. Fork v3_exq_614b_mech341_p3_behavioural_falsifier_3arm_sd056_amended.py
   to v3_exq_618_p4_isolation_matrix_11arm_sd056_amended.py.
5. Extend ARMS list per Section 3 (11 entries).
6. Add MATCHED_NOISE temperature override path in `_run_arm`.
7. Add `_apply_r_x_interpretation` function implementing the 6-row grid.
8. Add per-claim direction emission per Section 6.
9. Smoke 11 arms x 1 seed x 2+2 ep x 30 steps `--dry-run`.
10. `validate_experiments.py` AST PASS + `validate_queue.py` PASS.
11. Append queue entry per Section 8 (read priority + position before pushing
    to coordinate with concurrent sessions).
12. Push pathspec-limited to ree-v3 main.
13. Mark this design doc `status: SUBMITTED` and append the run-time
    queue-time decisions (scale, FP-2 expectation, machine_affinity
    confirmation).

---

*Plan-of-record cross-link: [`behavioral_diversity_isolation_plan.md`](behavioral_diversity_isolation_plan.md)*
*Submission gate: V3-EXQ-614b PASS.*
*Reserved ID: V3-EXQ-618.*
