# Failure autopsy: V3-EXQ-517b (MECH-302 relief-completion discriminative pair)

- generated_utc: 2026-05-30T08:28:45Z
- scope: cluster (V3-EXQ-517 / 517a / 517b -- three attempts of the same discriminative pair)
- status: confirmed
- claim under test: MECH-302 (relief.completion_event_reuses_goal_achievement_pipeline)
- target queue_id: V3-EXQ-517b (3rd attempt; supersedes 517a which supersedes 517)
- proposal context: EXP-0029 (auto-stub "discriminative support-vs-ablation pair for MECH-302" -- this autopsy closes it)

## 1. Facts (no interpretation yet)

### 1.1 Manifest read

V3-EXQ-517b/runs/v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3/manifest.json
status=FAIL, evidence_direction=non_contributory, evidence_direction_per_claim={"MECH-302": "non_contributory"}, claim_ids_tested=["MECH-302"], experiment_purpose=evidence.

Flat JSON (v3_exq_517b_*_v3.json):
- ARM_A (use_suffering_derivative_comparator=True, valence_liking_enabled=True): 3 seeds (42/43/44), all p1_events=0 and p1_writes=0. C1 (events >= 3) FAIL on all 3 seeds; C2 (writes >= 2) FAIL on all 3 seeds; C3 (ARM_B events == 0) and C4 (ARM_B writes == 0) PASS trivially because ARM_A is the ON arm and the criteria target ARM_B.
- ARM_B (comparator OFF): 3 seeds, all p1_events=0, p1_writes=0. C1+C2+C3+C4 PASS on all 3 seeds (no events expected when comparator disabled).
- Overall criteria: a_seeds_pass=0/3, b_seeds_pass=3/3, a_pass_rate=0.0 < 2/3 threshold -> overall_pass=false.
- Config: comp_window_length=30, comp_drop_threshold=0.005, comp_min_initial_norm=0.01; p0_episodes=30, p1_episodes=40, steps_per_episode=300; env_size=12, n_hazards=3, n_resources=2, limb_damage_enabled (implied via body_obs_dim=17, harm_obs_a_dim=7); heal_rate=0.002/step (per script docstring); seeds=[42,43,44]; elapsed=3670.7s.

metrics.json: `{"schema_version": "metrics/v1", "values": {}}` -- empty.
summary.md: only `Status: FAIL (4/12 criteria)`. No per-condition_results, no failure_signatures.

### 1.2 Predecessor manifests

V3-EXQ-517 (first attempt, 2026-05-04, three manifests):
- Config (per 517b script docstring): window=5, threshold=0.05, min_initial_norm=0.02.
- Result: 0 events ARM_A. The 5-step window cannot resolve 0.002/step healing dynamics (norm-delta over 5 steps < 0.05).

V3-EXQ-517a (2026-05-04T22:20:32Z; recalibration):
- Config: window=30, threshold=0.005, min_initial_norm=0.01; steps_per_episode=150 (HALF of 517b).
- ARM_A: seeds 42/43/44 -> mean_arm_a_p1_events=0.3333, mean_arm_a_p1_writes=0.3333 (1 event + 1 write across 3 seeds).
- ARM_B: 0 events, 0 writes; C3+C4 PASS trivially.
- Overall a_pass_rate=0.0 -> FAIL, evidence_direction=non_contributory.

V3-EXQ-517b (2026-05-06T01:35:15Z; second recalibration):
- Same comparator params as 517a. Only delta from 517a: steps_per_episode 150 -> 300.
- ARM_A events: 0.33/seed (517a) -> 0.00/seed (517b). Doubling episode length DECREASED ARM_A firings.

### 1.3 Script read

ree-v3/experiments/v3_exq_517b_mech302_relief_completion_discriminative_pair.py:
- HYPOTHESES UNDER TEST: SufferingDerivativeComparator fires on sustained z_harm_a norm descent and the relief-completion pipeline reuses MECH-057a commitment-release + MECH-094 VALENCE_LIKING write.
- INTERPRETATION GRID (from docstring): C1 ARM_A events >= 3/seed (comparator fires); C2 ARM_A writes >= 2/seed (write path intact); C3 ARM_B events == 0 (no events when disabled); C4 ARM_B writes == 0.
- The script docstring claims the recalibration "captures ~0.06 total healing per limb axis" over a 30-step window -- numerically well above the 0.005 drop_threshold.
- Body damage substrate: limb_damage_enabled=True (SD-022), heal_rate=0.002/step, damage_increment=0.15 per hazard hit; harm_obs_a sourced from body damage state (7 dims).

### 1.4 Queue entry

V3-EXQ-517b: claim_ids=["MECH-302"], experiment_purpose="evidence", supersedes V3-EXQ-517a, predecessor of EXP-0029 line item (no predecessor bug referenced; "longer episodes" is the stated recalibration).

### 1.5 Expected vs observed

Expected: ARM_A fires comparator on at least 3 hazard-contact -> heal sequences per seed (per 40 ep x 300 steps = 12000 ticks of measurement). With heal_rate=0.002/step, a single damaged limb fully heals in ~500 steps; 30-step window captures cumulative healing of 0.06 (> 0.005 threshold) if z_harm_a tracks damage-state monotonically during a healing interval.

Observed: 0 events, 0 writes across all 3 seeds in 517b. 517a (150 steps) produced exactly 1 event in 12 seed-episodes.

### 1.6 Failed criterion category

C1 (ARM_A absolute firing criterion) and C2 (ARM_A absolute write criterion) FAIL. C3 + C4 (ARM_B negative-control) PASS but trivially (the test is "does the ON arm fire while the OFF arm does not?" -- without OFF passing it's not informative).

This is **not** the canonical substrate-ceiling fingerprint ("negative control passes, discrimination criterion fails"). It is a different fingerprint: **the ON arm cannot fire at all**. Discrimination is undefined because there is nothing to discriminate.

## 2. Claim-layer mapping

MECH-302 (claims.yaml): claim_type=mechanism_hypothesis, status=candidate, v3_pending=true, exp_conf=0.368, lit_conf=0.897. Substrate IMPLEMENTED 2026-05-04 (SufferingDerivativeComparator wired). No epistemic_category set on the claim.

The experiment does test the claim under conditions where the claim could express itself IF the env reliably delivered a hazard-contact -> heal sequence with z_harm_a tracking damage. Whether the env actually delivers this is the load-bearing question; see Section 4.

claim_ids tagging: clean. V3-EXQ-517b tags only MECH-302; this is the test-of-record for that claim. No inherited tags from a predecessor (the 517 series is self-superseding).

## 3. Biological-reference triage

Closest mammalian reference for MECH-302: **dopaminergic relief / safety signal** at termination of an aversive state (Tanimoto / Heisenberg 2004 fly olfactory relief learning; Roesch / Calu / Schoenbaum 2007 ventral striatal relief firing). The biological reference is a **phasic** dopaminergic burst at the moment suffering ends, NOT a continuous integration over a 30-step window of declining harm signal. This is dissociated from goal-achievement reward in striatal recordings but uses the same downstream consequence (commit-release-equivalent + valence write).

Translation check: REE's SufferingDerivativeComparator is a windowed-derivative detector on z_harm_a.norm() -- the mathematical shape is "rolling-window slope detector". This is a faithful FUNCTIONAL translation: it fires at relief onset given suitable input dynamics. It is not a formal-definition import (no Pearl / Shannon / control-theory primitive being imposed); it is direct mechanistic translation. lit_conf=0.897 corroborates -- the biology is well-anchored.

Critical biological observation: the dopaminergic relief signal in the literature fires on **discrete onset/offset suffering events** (shock termination, hazard removal). In the biological references, the experimenter constructs the suffering trajectory; the animal cannot avoid it. **REE's substrate puts a trained avoidance policy in the loop between the env and the comparator**. The biological reference does not include this layer.

This points to a missing prerequisite at the env layer (Section 4), not at the comparator layer.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | The mechanism (windowed-derivative comparator) is correctly translated from biology; the test would express the claim if the env delivered the dynamics. |
| Biological reference | clear | Tanimoto/Heisenberg 2004, Roesch/Calu/Schoenbaum 2007. The reference fires on discrete onset/offset suffering. |
| Developmental / dependency prerequisites | present | SD-011 (z_harm_a dual nociceptive streams), SD-022 (limb damage substrate), MECH-057a (commitment-release pipeline) all implemented and validated. |
| Implementation completeness | complete | SufferingDerivativeComparator wired at ree-v3/ree_core/comparator/suffering_derivative_comparator.py with MECH-094 sim-gate; valence-liking write path intact (substrate-readiness V3-EXQ-515 PASS 2026-05-04). |
| **Environment adequacy** | **inadequate** | The env can produce limb damage in principle, but with limb_damage_enabled=True + heal_rate=0.002/step + a trained avoidance policy, **the policy learns to avoid hazards** during P0 warmup (30 ep). In P1 measurement (40 ep) the agent rarely contacts hazards; without damage accumulation there is no z_harm_a norm > min_initial_norm=0.01 to start a window; the comparator never arms. Doubling p1 steps (150 -> 300) gives the policy MORE time to avoid -- hence FEWER events at longer episodes (the 517a -> 517b empirical decrease 0.33 -> 0.00 events/seed). This is the same shape as SD-029 monomodal-collapse: the trained policy filters out the very events the discriminative pair needs to test. |
| Measurement adequacy | adequate | C1/C2 thresholds are reasonable IF the env delivered suffering trajectories. The thresholds are not the bottleneck. metrics.json is empty (a separate diagnostic gap, but does not affect interpretation here -- per-condition_results already in the flat JSON manifest). |
| Integration adequacy | coupled but unstable | Comparator + body-damage env + trained agent integrate correctly; the joint dynamics filter out test conditions. Each module is correct in isolation. |
| Scale / capacity | adequate | Substrate-side capacity is fine; the test gap is at the env layer. |

**Dominant diagnosis layer: environment adequacy.**

Recommended epistemic_category: **substrate_ceiling**. The claim is V3-tractable in principle, but the substrate (causal_grid_world_v3 + trained avoidance policy + slow continuous healing) cannot deliver suffering trajectories at the granularity the comparator needs.

## 5. The 517 -> 517a -> 517b empirical trajectory

| Attempt | window | drop_threshold | min_initial_norm | steps_per_episode | ARM_A events / seed |
|---|---|---|---|---|---|
| V3-EXQ-517 | 5 | 0.05 | 0.02 | 150 (assumed) | 0.00 |
| V3-EXQ-517a | 30 | 0.005 | 0.01 | 150 | 0.33 |
| V3-EXQ-517b | 30 | 0.005 | 0.01 | 300 | 0.00 |

Three readings:
1. The 517 -> 517a recalibration (widen window, lower threshold, lower min_norm) gained 1 event over 3 seeds at 150 steps -- this is real, but it is a Lazarus event in a system that should be firing 3+ events per seed. The substrate is on the verge of being able to fire, but not at the threshold required.
2. The 517a -> 517b extension (double episode length from 150 to 300) LOST that single event -- if longer episodes meant more time for damage to accumulate and heal, events should have risen. They fell to zero. This is the load-bearing observation: more time means more time-to-avoid for the trained policy, not more time-to-recover-from-damage.
3. There is no parameter-tuning move available on the comparator side that fixes this. Lowering min_initial_norm further (e.g. 0.001) would add noise events when z_harm_a fluctuates near zero (false-fire risk -- the 517a single firing on seed 42 may itself have been a noise event, not a real relief detection). Lowering drop_threshold below 0.005 reaches the level of per-step EMA jitter and contaminates the signal. Widening the window past 30 captures more healing per cycle but also includes more noise from non-healing periods.

The empirical trajectory rules out a 517c parameter-tuning fix.

## 6. Cluster pattern

Within the 517 family the pattern is convergent: three attempts at the same discriminative pair, three FAILs, with the substrate progressively unable to fire as episode length grows.

Cross-claim cluster: SD-029 monomodal-collapse pattern (the policy can't generate balanced agent-vs-env event distributions to populate C2/C3 measurement bins) is the same structural shape -- a trained policy filtering out test conditions. Both are substrate-ceiling at the env-policy interaction layer. The MECH-302 case is more severe because SD-029 at least gets events, just not balanced ones; MECH-302 gets zero events.

This is **not N independent bugs**; it is **one structural property**: causal_grid_world_v3 + a trained avoidance policy filters out the very dynamics that the comparator needs to test. Future discriminative pairs that depend on the agent regularly experiencing suffering (or any other adversarial state the policy can learn to avoid) will hit the same wall.

## 7. Learning extracted + repair pathway

**Learnings:**
- The SufferingDerivativeComparator substrate is wired correctly; substrate-readiness V3-EXQ-515 PASSed 2026-05-04. The bottleneck is NOT in the comparator implementation.
- The discriminative-pair test design treats the env as a constant source of suffering trajectories, but a trained avoidance policy is a filter that removes those trajectories. This is an unrecognised prerequisite of MECH-302's discriminative test in causal_grid_world_v3.
- 517a's single firing (1 event across 3 seeds at 150 steps) is not "the comparator on the verge of firing reliably"; it is a chance event in a system whose median behaviour is zero firings. Parameter relaxation does not move the median; only changing the env can.
- The 517 -> 517a -> 517b trajectory is the canonical refutation of "let's tune the parameters one more time." Three attempts, each with more permissive parameters, three FAILs.

**Repair pathway: substrate-ceiling -> env / measurement-harness redesign.**

Two architecturally-distinct options for a 517c -- decision is governance scope, not autopsy scope:

(A) **Scheduled-suffering env curriculum** (parallel to SD-029's `scheduled_external_hazard`): add a `scheduled_limb_damage_enabled` env knob that periodically injects damage into a random limb regardless of agent action. Forces periodic damage-accumulation followed by healing, supplying the comparator with detectable z_harm_a trajectories. This is the minimum-invasive env-side fix. Architecturally similar to the SD-029 hazard-injection curriculum that was added to unblock C3/C4 self-attribution measurement. Does not require a new env design; reuses CausalGridWorldV2 with an env kwarg addition.

(B) **Scripted-eval harness** (orthogonal to env): bypass the trained policy entirely. Construct synthetic z_harm_a trajectories (damage step -> heal step ramp) via direct sense() injection or env reset_to(), then check whether the comparator fires. Tests the substrate-readiness signature (already validated by V3-EXQ-515), not the trained-agent behavioural signature. Useful as a sanity-check but does NOT validate the claim's behavioural prediction. Should be a confirmation that the wiring still works at higher P1 budgets; not a replacement for the behavioural test.

Recommended primary route: (A). It preserves the discriminative-pair shape, lands a reusable env knob, and parallels an existing precedent (SD-029 scheduled_external_hazard).

Routing: **implement-substrate** with action="amend" against the existing MECH-302 substrate_queue entry (no new SD-id needed; the gap is on the env side, not on the comparator substrate itself, but the failure_record on MECH-302 is the right anchor for the env-injection follow-on).

## 8. Recommended substrate_queue.json amendment

action: amend
target: MECH-302 (existing entry at substrate_queue.json line 2305-2331)
failure_record_entry to append:
```json
{
  "run_id": "v3_exq_517b_mech302_relief_completion_discriminative_pair_20260506T013515Z_v3",
  "experiment_type": "v3_exq_517b_mech302_relief_completion_discriminative_pair",
  "metric": "ARM_A p1_events 0.00/seed across 3 seeds at window=30 / threshold=0.005 / min_initial_norm=0.01 / steps_per_episode=300; predecessor 517a at 150 steps got 0.33/seed -- doubling episode length DECREASED events (substrate-ceiling: trained avoidance policy filters out hazard-contact trajectories regardless of comparator parameter tuning)",
  "target": "ARM_A p1_events >= 3/seed; ARM_A p1_writes >= 2/seed under a scheduled-suffering env curriculum (parallel to SD-029 scheduled_external_hazard) that forces periodic limb-damage accumulation independent of agent avoidance"
}
```
implementation_log update: append "substrate_ceiling diagnosis 2026-05-30 (failure_autopsy_V3-EXQ-517b): three discriminative-pair attempts FAILed because causal_grid_world_v3 + trained avoidance policy filters out the very trajectories the comparator needs. Comparator substrate-readiness validated by V3-EXQ-515 (PASS 2026-05-04) is intact; gap is on the env side. Recommended next step: env-side `scheduled_limb_damage_enabled` curriculum modelled on SD-029 `scheduled_external_hazard`, then re-queue 517c against the new env knob."

pending_retest_after_substrate: true (gated on the env-side substrate enrichment; closes only after a successor 517c manifest PASSes ARM_A C1+C2 with the env curriculum active).

## 9. Recommended evidence_quality_note (governance writes)

For MECH-302 in claims.yaml:
> "Substrate IMPLEMENTED 2026-05-04 (V3-EXQ-515 substrate-readiness PASS). Three behavioural-validation discriminative-pair attempts (V3-EXQ-517 / 517a / 517b, 2026-05-04 / 2026-05-04 / 2026-05-06) all FAILed at ARM_A C1+C2 with 0-0.33 events/seed across all parameter relaxations. 517a -> 517b doubling of episode length DECREASED ARM_A events. Failure autopsy (failure_autopsy_V3-EXQ-517b_2026-05-30) attributes the failure to substrate_ceiling at the env-policy-interaction layer: causal_grid_world_v3 plus a trained avoidance policy filters out hazard-contact -> heal sequences before the SufferingDerivativeComparator can arm. Recommended response: env-side substrate enrichment (scheduled limb-damage curriculum) modelled on SD-029 scheduled_external_hazard, then re-queue as 517c. pending_retest_after_substrate=true."

Recommended evidence_direction-per-claim update on the 517b manifest: leave as `non_contributory` (already set). No retroactive supersession of 517a needed -- that manifest is also non_contributory and was reviewed.

epistemic_category recommendation: `substrate_ceiling` on MECH-302 -- the claim is V3-tractable but the current env substrate is too coarse to deliver the needed distinctions. Closure threshold under standard / Phase-3 gating accordingly suppressed (promote / demote suppressed; the right response is substrate enrichment, not more parameter tuning on the existing comparator).

## 10. Routing decision

**Routing: implement-substrate (env-side curriculum amendment).**

Not: queue-experiment (no parameter-tuning move is available without substrate change).
Not: lit-pull (biology is well-anchored; lit_conf=0.897).
Not: governance-demotion (claim alignment intact; substrate has just-shown-incomplete environment-side dependency, not a refuted mechanism).
Not: diagnose-errors (ran to completion, no crash).

Auto-stub proposal **EXP-0029** ("discriminative support-vs-ablation pair for MECH-302") is closed by this autopsy as **deferred_pending_substrate_or_env_redesign**. Re-issuing the same discriminative-pair call under the current env produces another 0-event FAIL. The proposal should be re-spawned (or a successor created) only after the scheduled-suffering env curriculum lands.

## 11. STOP-path check (per task prompt)

The task prompt asks: does the 517b manifest show the comparator was on the verge of firing such that a small parameter nudge would solve it?

Answer: **no**. Three attempts moved monotonically toward more permissive parameters; the third produced fewer events than the second. The empirical signature is that the trained policy filters out test conditions -- a property no parameter relaxation can fix. The STOP path does not apply.

Proceed with deferred_pending_substrate_or_env_redesign closure of EXP-0029.
