# Failure Autopsy: V3-EXQ-543f

**Generated:** 2026-05-17T14:19:31Z
**Scope:** single
**Status:** confirmed (user-gated 2026-05-17)
**Session:** failure-autopsy-543f-2026-05-17T141151Z

---

## Target

| Field | Value |
|---|---|
| queue_id | V3-EXQ-543f |
| run_id | v3_exq_543f_arc062_onehot_dacc_falsifier_20260517T140320Z_v3 |
| experiment_type | v3_exq_543f_arc062_onehot_dacc_falsifier |
| claim_ids | ARC-062, MECH-309 |
| supersedes | V3-EXQ-543e |
| outcome | FAIL |
| elapsed | 3134 s |

---

## Step 2 -- Reconstructed Failure (Facts Only)

### What was tested

2x2 factorial design across (use_gated_policy, use_dacc):
- ARM_0_baseline: gated OFF, dACC OFF
- ARM_1_dacc_only: gated OFF, dACC ON (dacc_weight=1.0, FIX 2)
- ARM_2_gated_only: gated ON, dACC OFF (use_first_action_onehot=True, FIX 1)
- ARM_3_both: gated ON, dACC ON (both fixes)

V3-EXQ-543f was designed as the first confound-free test of ARC-062 after the 543b/c/d/e
lineage was reclassified non_contributory:
- FIX 1 landed (one-hot augmentation bypasses E2 world-forward compression; pre-flight
  assertion confirmed use_first_action_onehot=True + first_action_dim > 0 on ARM_2/ARM_3)
- FIX 2 landed (dacc_weight=1.0; pre-flight asserts dacc_weight > 0 and
  use_first_action_onehot=True on expected arms)

### Failure criterion

**Discrimination.** PASS rule = D2 AND D3.

| Criterion | Result | Value |
|---|---|---|
| D1 (dACC alone improves reef_fraction) | FAIL | delta ARM_1-ARM_0 = -0.118 |
| D2 (dACC adds to gated) | FAIL | delta ARM_3-ARM_2 = -0.055 |
| D3 (gated adds to dACC) | FAIL | delta ARM_3-ARM_1 = -0.028 |
| D4 (replication 543c) | FAIL | probe gate failed ARM_2/ARM_3 |
| C2 (state dependence) | PASS | ARM_3 mean abs_rho = 0.205 |
| C3 (risk-type dissociation) | FAIL | probe gate failed ARM_2/ARM_3 |
| C4 (cross-seed variation) | PASS | ARM_3 CoV = 0.708 vs ARM_0 = 0.289 |

### The decisive instrument: behavioral divergence probe

ARM_2 and ARM_3 (both gated) show TV distances of **0.0001-0.0006** across all 60 P1
episodes across all 3 seeds. Threshold: 0.05. Gap: four orders of magnitude below threshold.

The probe computes TV between the GatedPolicy's biased action distribution and the uniform
bypass distribution: TV = 0.5 * |softmax(-gated_score_bias/T) - uniform|.

Probe logs confirm all 13-15 probe states are applicable (gated arms generate probe states).
The TV is not zero due to empty probe buffers -- it is zero because gated_score_bias stays
near zero throughout training.

### What the manifest's evidence_direction got wrong

The manifest recorded `ARC-062: weakens`. This is incorrect. See Step 3.

### Interesting positive signals

- **C2 passes ARM_3**: state-dependent behavioral variation associated with the full
  substrate (gated + dACC). Mean abs_rho = 0.205 vs baseline 0.127. Likely dACC-driven.
- **C3 hint**: ARM_3 forage_hazard_rate = 0.325 vs ARM_0 = 0.619 (47.5% relative delta).
  Not criterion-passing (probe gate failed) but indicates the environment carries the
  relevant behavioral variation when both mechanisms are active.
- **Pre-flight assertions**: both substrate fixes confirmed working. The inert gating is
  not caused by the same bugs as 543b/c/d/e.

---

## Step 3 -- Claim Layer Mapping

### ARC-062 (architectural_commitment, candidate, v3_pending)

Claim: A two-head gated architecture with a learned context discriminator constitutes a
viable rule-apprehension layer. Weak reading of the logical-necessity argument in MECH-309.

**Did the experiment test ARC-062 under conditions where it could express itself?**

No. The GatedPolicy training signal in P1 is `_compute_scaffolding_loss`, a purely
self-supervised diversity regularizer:

  loss = -(LAMBDA_HEAD_DIV * head_div_term + LAMBDA_DISC_VAR * disc_var_term)

where:
- head_div_term: E[(head_0_bias - head_1_bias)^2] -- pushes heads apart
- disc_var_term: Var[discriminator(z_world, z_self, z_harm_a)] -- pushes discriminator to vary

Neither term is connected to candidate-selection outcomes. The composed gated_score_bias
= w * head_0 + (1-w) * head_1 can remain near zero even when head_div_term is achieved,
because with discriminator initialized near w=0.5, the symmetric divergence of the two
heads (head_0 -> +X, head_1 -> -X) cancels in the composition.

**Verdict: non_contributory for ARC-062.** The architecture was never tested in conditions
where the claim could express itself (no outcome signal). Evidence direction should be
reclassified from "weakens" to "non_contributory". No confidence change. No conflict-ratio
movement.

**Confirmed by user (2026-05-17):** non_contributory for both ARC-062 and MECH-309.

### MECH-309 (mechanism_hypothesis, candidate, v3_pending)

Claim: Monomodal policy collapse is the predicted equilibrium without a rule-apprehension
layer; a gated-policy architecture should break it where standard E3 does not.

The gated policy never enacted discriminative candidate selection, so MECH-309's prediction
was not tested. Manifest's "non_contributory" is correct.

### Claim tag accuracy

`ARC-062: weakens` in the manifest was inherited without re-evaluation. The experiment
was the *first confound-free test* of ARC-062 -- the claim had never been under valid test
before -- so failing to produce behavioral divergence does not implicate the architecture
when the training procedure had no way to teach it outcome-coupled selection.

---

## Step 4 -- Biological Reference Triage

**Closest mechanism:** Lateral PFC rule-coding units. Bongard & Nieder 2010 (PNAS): PFC
neurons encode rules abstractly, generalising to unseen instances. Miller & Cohen 2001
(Annu Rev Neurosci): sustained PFC activity biases posterior regions toward rule-appropriate
responses.

**Is this a formal-definition import?** Partially. The two-head + soft-discriminator
architecture is ML-inspired (MoE). The ARC-062 lit-pull (discharged 2026-05-09, see
evidence/literature/targeted_review_arc_062_rule_apprehension/) provides biological grounding.

**Key biological dependency that is absent:** Reward-dependent abstraction pressure.
Bongard & Nieder 2010: rule-cell representations emerge under task contingencies that make
abstract rule application rewardable. PFC rule-coding units are not learned via diversity
regularization -- they are learned when the animal is rewarded for applying the correct rule.
The equivalent in REE is outcome-coupled credit assignment for candidate selection.

**Lit synthesis anticipation:** The ARC-062 lit synthesis (targeted_review_arc_062_rule_apprehension/SYNTHESIS.md) explicitly noted:
"ARC-062 may need an explicit rule-discrimination loss on the encoder rather than relying
on policy-loss back-propagation alone."
The diversification regularizer is exactly this kind of attempt, but disconnected from
outcomes. No new lit-pull is needed -- the existing lit already identifies this gap.

**Lit status:** Present and discharged (Pull A + Pull B, 2026-05-09).

---

## Step 5 -- Four-Layer Diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | gated heads had correct input but no outcome signal; ARC-062 never expressed itself |
| Biological reference | partial | architecture matches PFC/BG gating; reward-dependent plasticity analog absent from training |
| Prerequisites | missing | outcome-coupled credit assignment for candidate selection |
| Implementation | partial | heads built + input correct (one-hot fix working), but P1 training procedure decoupled from outcomes |
| Environment | adequate | SD-054 has reef/forage pressure; C3 hint (ARM_3 forage_hazard_rate 0.325 vs 0.619) confirms environment carries discriminative signal |
| Measurement | adequate | TV probe correctly detects inert gating; C2/C4 confirm residual behavioral differentiation exists |
| Integration | isolated | gated policy trained via diversity loss only; not wired to candidate-outcome returns |
| Scale | unknown | irrelevant until training signal is fixed |

**Dominant diagnosis:** `implementation_gap` -- specifically a *training signal gap*.

The P1 diversification loss achieves its internal objective (head-level diversity is
pressured) while the composed behavioral output (gated_score_bias) can remain near-zero
whenever discriminator weight w ~ 0.5, which is its initialized value and stays there
without an outcome signal anchoring w to a meaningful discriminative cut.

**Recommended epistemic_category:** `implementation_gap`

---

## Learning Extracted

1. **The diversification regularizer conflates head-level and behavioral diversity.**
   The loss maximizes (head_0 - head_1)^2 but the behavioral output is
   w * head_0 + (1-w) * head_1. When w ~ 0.5 and head_0 = +X, head_1 = -X, the composed
   bias is zero regardless of X. The regularizer achieves its own goal without changing
   behavior -- a training design error, not a substrate failure.

2. **The one-hot augmentation (FIX 1) and dacc_weight fix (FIX 2) both landed correctly.**
   Pre-flight assertions confirm this. The substrate is no longer the bottleneck. The
   bottleneck is the training procedure.

3. **C2/C4 passing with dACC active is informative.** ARM_3 (gated + dACC) shows
   genuine state-dependent behavioral variation and high cross-seed diversity. This is
   likely dACC-driven, not gated-head-driven, but it confirms the substrate + environment
   combination is capable of generating discriminative behavioral signal. An outcome-coupled
   loss would have material to train on.

4. **C3 hint is non-trivial.** ARM_3 forage_hazard_rate = 0.325 vs ARM_0 = 0.619 is a
   47.5% relative reduction. This means the combined architecture is visiting hazardous
   forage zones less. The probe gate failure means this cannot count as evidence, but it
   is consistent with the architecture doing something when both components are active.

---

## Repair Pathway

**Routing: /queue-experiment** as V3-EXQ-543g.

Same scientific question: can a two-head gated architecture with learned context discriminator
break monomodal collapse on SD-054 substrate?

Same 2x2 factorial structure. Same acceptance criteria. **Only change: redesign P1 loss
to include outcome-coupled credit assignment for candidate selection.**

### Candidate P1 loss designs for 543g

**Option A (recommended): Advantage-weighted candidate supervision**
- During P1 episodes, store (probe_state_snapshot, candidate_selected_index, episode_return)
- After each episode, identify which arm (head_0 or head_1 side) the discriminator weight
  w most favoured for the selected candidate
- Compute advantage = return - mean_return_across_seeds_this_arm
- Use advantage-weighted CE loss: push gated head to prefer higher-return candidates
  in probe states from high-advantage episodes
- Keep disc_var_term as secondary regularizer (with reduced lambda)
- Remove head_div_term (it is not needed once outcome signal exists)

**Option B: Policy gradient on GatedPolicy**
- Treat candidate selection as a discrete action with a dedicated GatedPolicy policy gradient
- After each episode, compute returns; use REINFORCE (with baseline) to update GatedPolicy
  parameters: grad += advantage * log_prob(candidate_selected | gated_score_bias)
- Simpler to implement but higher variance

**Note for /queue-experiment skill:**
- Keep P0/P1/P2 phased structure (P0=40 warmup, P1=60 outcome-coupled, P2=8 eval)
- Same probe buffer (world_states[1] from SD-054 bipartite layout)
- New EXQ number = 543g (same scientific question, bug fix in training procedure)

---

## Recommended Writes (for /governance -- do not apply here)

### ARC-062 evidence_quality_note addition

Append to existing note:
"V3-EXQ-543f (2026-05-17): reclassified non_contributory (confirmed user-gated, see failure
autopsy failure_autopsy_EXQ-543f_2026-05-17). Both substrate fixes from 543e autopsy landed
(pre-flight assertions confirmed). Inert gating (TV 0.0001-0.0006 across all seeds, threshold
0.05) caused by training signal gap: P1 diversification loss (head_div + disc_var) is
self-supervised only and provides no outcome-coupled gradient to the gated heads. The
architecture was never tested under conditions where it could express itself. No confidence
change. No conflict-ratio movement. ARC-062 architectural commitment remains untested.
Routing: V3-EXQ-543g with outcome-coupled P1 loss (advantage-weighted candidate supervision)."

### ARC-062 evidence_direction_note

"V3-EXQ-543f: non_contributory not weakens. Training signal gap: P1 diversification
regularizer has no outcome coupling. Architecture untested in confound-free conditions.
See failure_autopsy_EXQ-543f_2026-05-17."

### Manifest evidence_direction update

governance should set evidence_direction_per_claim.ARC-062 = "non_contributory" (from
"weakens") in the manifest and rebuild the index. MECH-309 stays non_contributory.

---

## Status

Confirmed by user 2026-05-17. Routing: /queue-experiment V3-EXQ-543g with
outcome-coupled GatedPolicy P1 loss. GAP-C and GAP-D remain blocked pending 543g.
