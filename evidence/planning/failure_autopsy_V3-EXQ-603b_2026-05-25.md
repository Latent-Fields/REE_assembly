# Failure Autopsy: V3-EXQ-603b (Q-045 / MECH-313 / MECH-260)

**Generated**: 2026-05-25T09:13:34Z
**Scope**: single (with explicit cluster reading across V3-EXQ-603 / 603a / 603b)
**Status**: confirmed
**Autopsy session**: failure-autopsy-603b-20260525T091334Z

---

## 1. Target

| Field | Value |
|---|---|
| run_id | v3_exq_603b_q045_mech313_mech260_four_arm_ablation_20260525T065407Z_v3 |
| queue_id | V3-EXQ-603b |
| claim_ids | Q-045, MECH-313, MECH-260 |
| outcome | FAIL |
| experiment_purpose | evidence |
| supersedes | V3-EXQ-603a |
| manifest evidence_direction | mixed (per-claim: all three "mixed") |

Third iteration in the 603 chain. Both prior iterations were diagnosed
measurement_gap and overridden to non_contributory in the 2026-05-25
governance cycle.

---

## 2. Facts Reconstruction

### Per-seed, per-arm

| ARM | seed 42 | seed 43 | seed 44 | mech260_operative |
|---|---|---|---|---|
| ARM_0 both-off       | entropy 0.0, total_steps 423, measured 0, ~14 step/ep   | entropy 0.449, total_steps 12792, measured 10656, **355 step/ep** | entropy 0.0, total_steps 436, measured 0, ~15 step/ep   | n/a |
| ARM_1 mech313-only   | entropy 0.0, total_steps 421, measured 0                | entropy 0.460, total_steps 12567, measured 10521, **351 step/ep** | entropy 0.0, total_steps 475, measured 0, ~16 step/ep   | n/a |
| ARM_2 mech260-only   | entropy 0.0, total_steps 352, measured 0 (dacc_fwd=51, hist=4, sup=1.0)  | entropy 0.490, total_steps 10764, measured 8821, **294 step/ep** (dacc_fwd=1362, hist=8, sup=1.0) | entropy 0.0, total_steps 370, measured 0 (dacc_fwd=52, hist=7, sup=1.0)  | **true** |
| ARM_3 both-on        | entropy 0.0, total_steps 385, measured 0 (dacc_fwd=55, hist=5, sup=1.0)  | entropy 0.494, total_steps 10764, measured 8821, **294 step/ep** (dacc_fwd=1362, hist=8, sup=1.0) | entropy 0.0, total_steps 380, measured 0 (dacc_fwd=54, hist=6, sup=1.0)  | **true** |

### Mean across seeds (as measured)

| Field | Value |
|---|---|
| entropy_ARM_0 | 0.149637 |
| entropy_ARM_1 | 0.153171 |
| entropy_ARM_2 | 0.163370 |
| entropy_ARM_3 | 0.164556 |
| c1_both_beats_off (>=ARM_0 + 0.05) | False |
| c2_mutually_load_bearing (>=max(ARM_1,ARM_2) + 0.05) | False |
| c3_each_alone_beats_off (e1>e0 AND e2>e0) | True |
| mech260_operative_all_seeds | **True** |
| fifo_temporal_gate_ok_all | **False** |
| overall_pass | False |

### Seed-43-only (effective N=1) deltas vs ARM_0

| Mechanism | Seed-43 delta | Threshold | Verdict |
|---|---|---|---|
| MECH-313 (ARM_1 - ARM_0) | +0.011 | 0.05 | sub-threshold |
| MECH-260 (ARM_2 - ARM_0) | +0.041 | 0.05 | sub-threshold but directionally correct |
| Both (ARM_3 - ARM_0)     | +0.045 | 0.05 | sub-threshold |

### Criteria

| Criterion | Result | Detail |
|---|---|---|
| C1 both-ON beats both-OFF      | False | margin 0.045 < 0.05 ENTROPY_MARGIN |
| C2 mutually load-bearing       | False | ARM_3 - max(ARM_1, ARM_2) below margin |
| C3 each-alone beats off        | True (on the means)  | but driven by seed 43 only; seeds 42/44 are 0.0 across all four arms |
| mech260_operative_all_seeds    | True | dACC FIFO + suppression both fired on every seed, including seeds that died |
| fifo_temporal_gate_ok          | False | seeds 42/44 never reached the 75-step warmup |

### Manifest evidence_direction (as written by script)

- Q-045: mixed
- MECH-313: mixed
- MECH-260: mixed
- evidence_direction: mixed

The script's `_evidence_direction_per_claim` logic emitted "mixed" on the
C3=True / C2=False branch with each sub-mechanism below margin. These
"mixed" tags are not load-bearing once the discrimination criterion has
N=1 effective; the recommended override is non_contributory.

---

## 3. Root Cause

### Direct cause of FAIL: failed discrimination criterion with N=1 effective

Two of three seeds (42 and 44) terminate at ~12-16 step/ep across all four
arms (total_steps 352-475 over 30 episodes). The pre-registered 75-step
FIFO_WARMUP_STEPS gate is never reached, so measured_steps=0 and entropy
contribution from those seeds is 0.0 on every arm.

Only seed 43 produces ~294-355 step/ep episodes and clean measured_steps
in the 8.8k-10.6k range. On seed 43 the mechanisms behave as predicted
(directionally correct, MECH-260 lift > MECH-313 lift > 0), but every
single per-claim and overall delta is sub-threshold (margin 0.05) and
N=1 cannot dissociate Q-045.

### Why Fix B did not extend seeds 42/44 survival

The autopsy V3-EXQ-603 retest spec for 603b added two fixes to 603a:

- Fix A (autopsy spec): STEPS_PER_EPISODE 200 -> 500 (outer step budget).
- Fix B (env-side review): hazard_harm 0.05 -> 0.02, predicted to give
  ~182 step/ep episodes (vs ~14 at 0.05) based on contact-rate arithmetic.

Fix B did not work: seeds 42/44 episodes are still ~12-16 steps, identical
to 603a. The Fix B calculation assumed contact rate dominated the health-
depletion path. The env actually depletes `agent_health` from multiple
sources:

```
ree_core/environment/causal_grid_world.py:
  line 1374:  contact_harm = self.hazard_harm
  line 1388:  self.agent_health = max(0.0, self.agent_health - abs(harm_signal))
  line 1394:  self.agent_health = max(0.0, self.agent_health - self.contaminated_harm)
  line 1569:  self.agent_health = max(0.0, self.agent_health - abs(harm_signal))
  line 2024:  done = self.agent_health <= 0.0 or self.steps >= 500
```

`harm_signal` carries the proximity-harm contribution (env config
`proximity_harm_scale=0.1`, **unchanged** by Fix B); on every step where
the agent sits near a hazard without contacting it, `agent_health` still
drops by ~0.1. Plus `contact_harm` (now 0.02) on direct contact. Plus
contaminated cells. Fix B lowered ONE channel; the others remained intact.

### Why seeds 42/44 die but seed 43 survives

The env config for 603b includes the full SD-054 enrichment cluster:

- `reef_enabled=True`, `n_reef_patches=3`, `reef_patch_radius=2`
- `reef_bipartite_layout=True`, `reef_bipartite_axis="horizontal"`,
  `reef_bipartite_agent_band_radius=1` (agent spawns in mid-rows only;
  reef bottom, food top)
- `hazard_food_attraction=0.7` (hazards bias-drift toward food cells at
  drift ticks)
- `num_hazards=4`, `num_resources=5`, `proximity_harm_scale=0.1`

The agent is **untrained**. ARC-062 gated_policy is enabled with random
init + symmetry-broken head bias (offset=0.05). The CEM proposer
(SD-055 differentiable + SP-CEM) samples action-object distributions
from a randomly-initialised policy. On seed 43 the random init happens
to produce action proposals that keep the agent near reef or in
sparsely-hazarded cells; on seeds 42/44 the same random init produces
action proposals that drive the agent into food rows (the top half of
the bipartite layout) where `hazard_food_attraction=0.7` causes hazards
to converge on the food-corridor. Sustained proximity at
`proximity_harm_scale=0.1` depletes `agent_health` to 0 in ~10-14 steps
regardless of Fix B's contact_harm reduction.

This is **not** a code bug in 603b. The substrate behaviour is correct;
the experiment design (untrained inference on SD-054-enriched env)
cannot survive seed-init-dependent path-dependence.

### MECH-260 substrate is operative on every seed

The diagnostic counters confirm dACC fires on every seed, including
the doomed ones:

- seed 42 ARM_2: dacc_forward_calls=51, dacc_history_len_max=4, dacc_max_suppression=1.0
- seed 43 ARM_2: dacc_forward_calls=1362, dacc_history_len_max=8, dacc_max_suppression=1.0
- seed 44 ARM_2: dacc_forward_calls=52, dacc_history_len_max=7, dacc_max_suppression=1.0

`mech260_operative_all_seeds = True`. This is not a call-path bug
(unlike V3-EXQ-603) and not a substrate non-firing bug. The FIFO does
fill on seeds 42/44; it just fills during the doomed 12-step lifespan
and never contributes to the measurement window.

---

## 4. Claim-Layer Map

| Claim | Type | Status | Did this test let it express? |
|---|---|---|---|
| MECH-260 | mechanism_hypothesis (cingulate.dacc_bias_suppression) | candidate, v3_pending | Partial -- substrate operative on every seed, but discrimination requires N>=2 surviving seeds; effective N=1 here |
| MECH-313 | mechanism_hypothesis (policy.stochastic_noise_floor) | candidate_substrate_landed, v3_pending | Partial -- substrate operative; +0.011 on seed 43 is below noise floor of N=1 |
| Q-045 | open_question (anti_monostrategy.substrate_independence_lc_vs_dacc) | open | NO -- N=1 effective cannot dissociate two mechanisms |

Notes:
- MECH-260's valid evidence record is **unaffected**: EXQ-445h (C3 3/3
  seeds, training run, separate env config) remains the valid support.
  Recording 603b "mixed" against MECH-260 would corrupt the claim's
  evidence record with a sub-threshold N=1 result.
- MECH-313 has no prior evidence; 603b is its first evidence run and
  produces a directionally-correct but unmeasurable signal on N=1.
- Q-045's spec explicitly names "SD-054 reef substrate with ARC-062
  gated-policy enabled" as the falsifier environment. 603b honours that
  spec literally. The autopsy finding is that the spec presupposes a
  trained policy where untrained inference was assumed sufficient.

---

## 5. Biological-Reference Triage

### MECH-260 (dACC anti-recency)

**Closest mechanism**: Scholl & Kolling 2015 dACC + lateral aPFC actively
suppress recency-biased choices; Kennerley 2006 dACC multi-trial action-
history integration.
**Biological faithfulness**: high. FIFO suppression is a biologically
grounded implementation; this autopsy does not find biology divergence.
**Failure shape**: substrate fires; measurement window does not open
on 2/3 seeds. Not a biological-reference failure.

### MECH-313 (LC-NE tonic noise floor)

**Closest mechanism**: Aston-Jones & Cohen 2005 LC tonic mode; Haarnoja
2018 SAC entropy-bonus computational analog.
**Biological faithfulness**: moderate. Temperature lift is a reasonable
proxy. Lit-pull (Pull 1 R2, lit_conf 0.84) confirms LC-NE tonic substrate
load-bearing.
**Failure shape**: substrate fires; tiny +0.011 lift on seed 43 is
substantially smaller than MECH-260's +0.041, consistent with the
mechanism being smaller-magnitude (the lit-pull explicitly NOT pinning
magnitude). Not a biological-reference failure.

### Q-045 (LC-NE vs dACC substrate independence)

**Literature**: Tervo et al. 2014 (LC -> ACC stochastic-mode switching);
Pull 1 R3 verdict "architecturally distinct but functionally
overlapping". Pull-Resolved verdict is COUPLED-NOT-COLLAPSED. The biology
predicts dissociation is possible under sufficient discrimination power.
**Failure shape**: structural test failure (N=1 effective). The biology
is testable; the *experiment* could not deliver power.

**No biology divergence to register.** No formal-definition import to
re-evaluate. The autopsy diagnosis is on the experimental design layer,
not the claim or biology layers.

---

## 6. Four-Layer Diagnosis Table

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | measurement gap | MECH-260 + MECH-313 substrates operative; N=1 effective prevents discrimination |
| Biological reference | clear | Scholl & Kolling 2015, Kennerley 2006, Aston-Jones & Cohen 2005, Tervo 2014; no divergence |
| Prerequisites | partial -- design level | Q-045 spec presupposes survivable episodes on the SD-054 env; untrained-inference + SD-054 enrichment produces seed-dependent rapid termination |
| Implementation completeness | complete | NoiseFloor, dACC (FIFO + suppression), gated_policy + SP-CEM all instantiated and verified firing |
| Environment adequacy | wrong pressures for the experiment's policy regime | `proximity_harm_scale=0.1` (untouched by Fix B) + `hazard_food_attraction=0.7` + `reef_bipartite_layout=True` combine with untrained policy to kill 2/3 seeds before warmup |
| Measurement adequacy | adequate when episode survives | entropy + ARM-vs-ARM_0 + 75-step FIFO temporal-gate + per-claim direction logic all correct |
| Integration adequacy | OK on seed 43 | mech260 + mech313 + gated_policy + SP-CEM compose cleanly when episodes survive |
| Scale / capacity | inadequate | untrained gated-policy at random init on SD-054 cannot deliver discriminative power with 30 episodes per arm |

**Dominant diagnosis**: measurement_gap (third in the 603 cluster).

**Recommended `epistemic_category`**: measurement_gap. The cluster shape
(three consecutive measurement_gaps) suggests the 603 chain has hit a
substrate-ceiling-adjacent regime on the EXPERIMENTAL-DESIGN side -- the
substrate is fine, but the experimental design (untrained inference on
enriched env) cannot deliver the claim's required power.

---

## 7. Cluster Pattern (603 / 603a / 603b)

Three consecutive iterations, each substrate-correcting the prior gap,
each exposing a deeper structural issue.

| Iteration | Failed criterion | Dominant diagnosis | Surviving seeds | Per-claim seed-43 result |
|---|---|---|---|---|
| V3-EXQ-603   | every criterion | call-path bypass (act_with_split_obs misses dacc.record_action)              | 3/3 but ARM_2 == ARM_0 structurally        | substrate non-operative on ARM_2/ARM_3 |
| V3-EXQ-603a  | discrimination  | 75-step FIFO warmup not cleared in seeds 42/44 (episodes ~14 steps)         | 1/3 (seed 43)                              | similar to 603b on seed 43 |
| V3-EXQ-603b  | discrimination  | hazard_harm 0.05->0.02 did not extend seeds 42/44 survival (still ~14 step) | 1/3 (seed 43)                              | MECH-313 +0.011, MECH-260 +0.041, both +0.045 (sub-threshold) |

**Convergent failure shape**: each retest validates the prior
substrate-fix (603a verified Fix-1 call-path fixed mech260_operative=True;
603b verified Fix B applied) but a deeper layer of the experimental
design then exposes a new measurement gap. The substrate is fine across
the chain; the experimental design (Q-045 spec literally interpreted on
the V3 substrate, with the implicit assumption of survivable untrained-
inference episodes) is the structural blocker.

**Two readings** of the cluster shape:

1. **Design-fixable**: with a P0/P1 training phase added before
   measurement, the gated_policy will not be random-init and seed-
   dependent path-dependence disappears. This is the user-confirmed
   route (603c with training).
2. **Substrate-conditional**: if even a P0/P1-trained policy still
   shows seed-dependent rapid termination on the SD-054 enrichment,
   the question is structurally untestable in V3 and Q-045 should
   move to `epistemic_category=substrate_conditional`.

The first reading is the prior, but the second is the falsifier route
if 603c also produces a 1/3-survivor manifest.

---

## 8. Learning Extracted

1. **Q-045 spec implicit dependency on policy-training regime.** The spec
   ("SD-054 reef substrate with ARC-062 gated-policy enabled") was
   registered in the context of trained-policy ARC-062 falsifiers
   (V3-EXQ-543 chain). Running the same env config under untrained
   inference is the structural mismatch the 603 chain has been
   discovering. Future experiment specifications mentioning SD-054 +
   ARC-062 should explicitly name the policy-training regime.

2. **Fix-arithmetic must trace all health-depletion paths.** The Fix B
   prediction (hazard_harm 0.02 -> ~182 step/ep) was derived from
   contact_harm alone. The env has at least three independent depletion
   paths (`hazard_harm` direct contact, `proximity_harm_scale` gradient,
   `contaminated_harm` ground state). Any future env-side fix targeting
   episode length must consider the joint depletion surface, not the
   single channel being adjusted.

3. **Substrate firing is necessary but not sufficient.**
   `mech260_operative_all_seeds=True` on a manifest where 2/3 seeds
   produced measured_steps=0 is a load-bearing diagnostic: it tells us
   the substrate is fine and the failure is upstream (env / policy /
   warmup). A future autopsy template question: "Did the substrate
   fire? If yes, did it fire IN THE MEASUREMENT WINDOW?"

4. **MECH-260's EXQ-445h evidence remains the canonical support**;
   nothing in 603b weakens it. The 603b "mixed" tag in the manifest is
   a script-logic artifact of C3=True on a manifest dominated by N=1
   data and must not enter governance scoring.

5. **Cluster pattern itself is the load-bearing signal.** Each
   individual 603 FAIL would look like a tunable problem; the
   convergent shape across three iterations is the diagnostic that
   the experimental DESIGN (not the substrate, not the env config in
   isolation, not the script logic) is structurally mismatched.

---

## 9. Repair Pathway

**Routing (user-confirmed at interactive gate, 2026-05-25T09:1?Z)**:
**/queue-experiment for V3-EXQ-603c with P0/P1 training phase added.**

Keep the env config (SD-054 reef + bipartite + hazard_food_attraction)
literally faithful to the Q-045 spec. The redesign target is the policy-
training regime, not the env. Add a P0/P1 training phase so the
gated_policy is no longer at random init when measurement begins.

### Required fixes for 603c

**Fix C (REQUIRED)**: Add P0 + P1 training phase before measurement.
Reference implementations:
- V3-EXQ-543k/l ARC-062 GAP-B falsifier uses P0 encoder warmup ->
  P1 outcome-coupled REINFORCE on gated heads + discriminator.
- V3-EXQ-321b training pattern (Phase E3 training loop).
- experiments/committed_mode_curriculum.py harness helper landed
  2026-05-17 (commitment_closure:GAP-11) provides
  `run_p0_warmup()` / `run_p1_consolidation()` / `run_p2_eval()`
  with seed-stability guard and mid-probe abort gate.

Recommended structure for 603c (subject to standard
`/queue-experiment` skill code-review + smoke):
```
P0: 50-100 episodes on easy env (SD-054 reef, no hazard_food_attraction
    in P0; or use the curriculum helper's "easy env" default).
    Train E1+E2+gated_policy until running_variance < 0.1.
P1: 30-50 episodes on target env (full SD-054 enrichment as in 603b).
    Continue outcome-coupled gradient on gated_policy heads +
    discriminator. Verify episode survival >= 75 steps for all seeds
    AT END OF P1 (the gate); fall back to substrate_conditional if
    not.
P2 (the measurement): same 4-arm structure as 603/603a/603b; frozen
   policy; 30 episodes per arm; FIFO_WARMUP_STEPS=75 unchanged.
```

**Fix D (RECOMMENDED)**: Pre-measurement seed-stability gate. At the
end of P1, abort the run with a clean diagnostic message if any seed
produced episodes averaging <75 steps over the final 10 episodes of
P1. This avoids burning the full P2 measurement budget when the
underlying policy/env regime is still not survivable.

**Fix E (RECOMMENDED)**: Keep STEPS_PER_EPISODE=500 + FIFO_WARMUP_STEPS=75
+ all four arms + per-claim ARM-vs-ARM_0 logic unchanged from 603b.
None of those layers are at fault; the issue is upstream.

### Alternative routing (NOT user-confirmed; recorded for completeness)

- **Redesign-env route** (REJECTED at gate): would drop SD-054 enrichment
  and run on legacy CausalGridWorld. Rejected because Q-045 spec
  explicitly names "SD-054 reef substrate with ARC-062 gated-policy"
  and changing the env would test a different scientific question.
- **Substrate_conditional route** (RESERVED as 603c fallback): if 603c
  with P0/P1 training also produces a 1/3-survivor manifest, Q-045
  routes to `epistemic_category=substrate_conditional` and the 603
  chain halts.

---

## 10. Recommended Governance Writes

These are RECOMMENDATIONS ONLY. /governance applies them interactively.

### Manifest overrides (next /governance cycle)

| Field | V3-EXQ-603b manifest | Recommended override |
|---|---|---|
| evidence_direction | mixed | non_contributory |
| evidence_direction_per_claim["Q-045"] | mixed | non_contributory |
| evidence_direction_per_claim["MECH-313"] | mixed | non_contributory |
| evidence_direction_per_claim["MECH-260"] | mixed | non_contributory |
| epistemic_category | (unset) | measurement_gap |

Both the flat JSON (`v3_exq_603b_q045_mech313_mech260_four_arm_ablation_20260525T065407Z_v3.json`)
and the run manifest (`runs/v3_exq_603b_q045_mech313_mech260_four_arm_ablation_20260525T065407Z_v3/manifest.json`)
should receive the override; index rebuilt afterwards.

### evidence_quality_note additions (next /governance cycle)

#### MECH-260

```
[2026-05-25 autopsy V3-EXQ-603b]: MEASUREMENT GAP (third in the 603
chain). Substrate confirmed operative across all three seeds:
mech260_operative_all_seeds=true, dACC FIFO + suppression both fire
(dacc_forward_calls up to 1362, dacc_history_len_max=8,
dacc_max_suppression=1.0). However 2/3 seeds (42, 44) terminated at
~12-16 step/ep on every arm despite Fix B (hazard_harm 0.05 -> 0.02);
FIFO_WARMUP_STEPS=75 never reached, measured_steps=0. Seed 43 only:
ARM_2 - ARM_0 = +0.041 (sub-threshold; margin 0.05), directionally
correct. The "mixed" direction in the manifest is N=1 noise and must
not enter governance scoring. EXQ-445h (C3 3/3 seeds on a separate
env, training run) remains the valid MECH-260 support. Pending retest:
V3-EXQ-603c with P0/P1 training phase added.
```

#### MECH-313

```
[2026-05-25 autopsy V3-EXQ-603b]: MEASUREMENT GAP (third in the 603
chain; MECH-313's first evidence run). NoiseFloor substrate fires;
seed 43 only: ARM_1 - ARM_0 = +0.011 entropy lift, directionally
correct but well below the 0.05 ENTROPY_MARGIN. 2/3 seeds (42, 44)
produced measured_steps=0 due to early episode termination. Effective
N=1. Non-contributory; pending retest V3-EXQ-603c with P0/P1
training phase.
```

#### Q-045

```
[2026-05-25 autopsy V3-EXQ-603b]: NON-CONTRIBUTORY. With effective N=1
(seeds 42/44 produced measured_steps=0), Q-045's MECH-313-vs-MECH-260
collapse question is structurally untestable from this run. Both
mechanisms verified operative on the surviving seed (seed 43); per-
claim deltas all sub-threshold. The third measurement_gap in the 603
chain. Pending retest V3-EXQ-603c with P0/P1 training phase. If 603c
also produces a 1/3-survivor manifest, consider routing Q-045 to
epistemic_category=substrate_conditional pending a V4 substrate that
makes untrained-inference survival on SD-054 enrichment a clean
prerequisite.
```

### Pending-retest flag

Add `pending_retest_after_substrate: true` (or
`pending_retest_after_redesign: true` if the flag set permits) on
MECH-260, MECH-313, Q-045 so the governance pipeline does not draw
inferences from these three claims until 603c manifest lands.

### Substrate / experiment queue entry

Not required: 603c is an experiment redesign at the experiment-script
layer, not a substrate enrichment. Queue via /queue-experiment with
the build instructions in Section 9.

---

## 11. Confirmed Routing

**User judgment (interactive gate, 2026-05-25T09:1?Z)**:

- **Routing**: ADD P0/P1 TRAINING PHASE to 603c (keep SD-054 env per
  Q-045 spec; redesign the policy-training regime, not the env).
- **Manifest writes**: ALL THREE CLAIMS NON_CONTRIBUTORY +
  pending_retest_after_redesign on MECH-260 / MECH-313 / Q-045.
  Manifest overrides applied via next /governance cycle (consistent
  with 603/603a precedent).

**Routing destinations**:

- V3-EXQ-603c: /queue-experiment (separate session per standard /skill
  path). Build instructions in Section 9.
- Manifest overrides + evidence_quality_notes: /governance (next cycle).
- 603 chain halts at 603c outcome: contributory PASS -> Q-045 resolves;
  another 1/3-survivor measurement_gap -> Q-045 routes to
  substrate_conditional.

---
