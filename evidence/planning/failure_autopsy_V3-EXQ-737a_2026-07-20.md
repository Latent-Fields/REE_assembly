# Failure Autopsy -- V3-EXQ-737a (REE-latent policy-head competence probe)

- **Generated:** 2026-07-20T15:30:07Z
- **Session:** `malloc-stack-autopsy-extended-a0e312`
- **Scope:** single run -- diagnostic, `brake_exempt: true`, `claim_ids: []`
- **Status:** confirmed (user-gated 2026-07-20)
- **Machine-readable companion:** `failure_autopsy_V3-EXQ-737a_2026-07-20.json`

---

## Headline

**Two findings, and the second is a live substrate defect whose fix is no longer gated.**

1. **The control arm also fails, and that is the informative part.** PPO on **raw observations**
   reaches 0.567 at D3 against a 1.0 competence floor, on an environment where local-view greedy
   achieves **48.05** from the same view. The failure is in **policy learning**, not
   representation.
2. **`z_world` was never prediction-trained.** The guard measured **0 of 4 world-encoder tensors
   and 0 of 61 `latent_stack` tensors changed** after 200 P0 episodes: the P0/P1 warmup has no
   optimizer group covering `latent_stack`. The `ppo_ree_latent` arm therefore ran PPO on a
   **frozen random projection**, not on a learned REE representation.

The V3-EXQ-783 autopsy (status `confirmed`, 2026-07-18) **resolves the dependency that previously
gated the fix**: it establishes SD-070 as the working training route, with world-path weight-delta
**7** and PR retention 0.658, explicitly contrasted against *"the x734 configuration's 0/61"* --
which is exactly what 737a measured. The build is now `complicated (buildable)`.

---

## 1. Facts

**Manifest:** `outcome: FAIL`, `evidence_direction: null`, `claim_ids: []`,
`experiment_purpose: diagnostic`, `brake_exempt: true`
(`"competence localization probe; claim_ids=[]; not a conversion/de-commit falsifier"`),
`interpretation.label: policy_learning_insufficient_or_deeper`,
`label_qualifier: zworld_arm_ran_on_frozen_random_projection`.

**Per-rung foraging competence** (floor 1.0, 3 seeds):

| Arm | D0_baseline_724 | maj. supra-floor | D3_hazard_free | maj. supra-floor |
|---|---|---|---|---|
| `ree_bias_head` | 0.117 | false (0/3) | 0.750 | false (1/3) |
| `ppo_ree_latent` | 0.333 | false (0/3) | **0.217** | false (0/3) |
| `ppo_raw_obs` (control) | 0.867 | **true (2/3)** | **0.567** | false (0/3) |
| `greedy_oracle` | 6.333 | true (3/3) | **57.2** | true (3/3) |
| `random_walk` | 0.267 | false | -- | -- |

`readiness.readiness_met: true` -- both oracle rungs clear the floor and the bias head reproduces
724's incompetence at D0, so the probe's own scaffolding is sound.

**Recording provenance: COMPLETE** -- `recording_schema`, `substrate_hash` (`3d99e3c3...`),
`machine_class`, `elapsed_seconds` (25653.6, i.e. ~7.1 h), full `config`, explicit `seeds`.

**The guard record** (`recorded_preconditions`, and `diagnostics.zworld_encoder_guard`):

```
zworld_world_encoder_trained: measured 0.0, threshold 0.0, comparator ">", met: false
  n_world_encoder_tensors: 4    n_world_encoder_changed: 0
  n_latent_stack_tensors:  61   n_latent_stack_changed:  0
  p0_episodes: 200
```

---

## 2. The probe's own question: what it does and does not settle

**Settled:** the bottleneck at D3 is **policy learning**, not representation. `ppo_raw_obs` is the
clean discriminating control -- it is unaffected by the encoder defect, it receives the raw
observation with no REE representation in its path, and it still cannot clear the floor while a
hand-written greedy policy reading the same 5x5 view reaches 48.05 (V3-EXQ-738's anchor). The
environment is demonstrably solvable from that view; PPO does not learn it within this budget.
That is the "prediction-rich, action-poor" localization the probe set out to test, and it survives.

**Not settled:** whether REE's *learned* representation supports competence. The `ppo_ree_latent`
arm is confounded -- it measured what a frozen random projection of the observation supports. Its
0.217 must not be read as evidence about z_world. The manifest is explicit and correct about this
in `interpretation.zworld_arm_reading`.

**A design decision worth endorsing.** The guard entries are carried under
`recorded_preconditions`, deliberately **not** under the adjudicating flat `preconditions` list,
because the REE_assembly indexer returns whole-run `precondition_unmet` on the first unmet flat
entry -- which would have buried an interpretable run behind a confound affecting only one of
three arms. The entries still carry honest `measured`/`threshold`/`met`, so any recompute agrees
with the guard's own verdict. This is the correct handling of a partial confound, and it is the
opposite of the whole-run vacuity flattening the V3-EXQ-785 autopsy criticised.

---

## 3. The substrate defect

**Mechanism.** The P0/P1 warmup has no optimizer group covering `latent_stack`. All 61 latent-stack
tensors are bit-identical after 200 episodes of a phase whose stated job is to train the world
model. So `z_world` is a frozen random projection wherever this training path is used.

**This is the second confirmed strike.** `zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` §6c
already found **all six `_train_all_on_agent` callers exposed** and names V3-EXQ-737 among them,
alongside `v3_exq_728_trained_allon_capability_point.py` (which defines its own copy at `:481`) and
`v3_exq_734`. Its warning stands: *a "trained all-on capability point" whose world encoder is a
frozen random projection is not measuring the capability its name claims.*

**Blast radius.** Any experiment on this training path that assumes a prediction-trained `z_world`
silently measures a random projection instead. There is no error and no warning -- only the guard
detects it, and per the 780 doc §6d the guard **landed as a shared module but had not been adopted
by any driver** at 2026-07-19T21:26Z. 737a is a driver that *did* adopt it, which is why the defect
is visible here at all.

**The gate is now open.** The 780 doc deferred the fix as "downstream of the V3-EXQ-783
adjudication". That adjudication is complete and `confirmed`, and its findings are:

- *"z_world under-differentiation is a TRAINING fault, not a DIMENSIONALITY fault"* -- training
  lifts CR at both dims (t = +7.26, +13.11); dimensionality lifts nothing at either training state.
- *"SD-070 works: world-path weight-delta 7 (vs the x734 configuration's 0/61) with PR retention
  0.658, against the prescribed pre-SD-070 P0's collapse to PR ~1.06, and P0/P1 phase separation
  preserved exactly."*
- Q-002's remedy clause *"resolve via SD-005 / higher-dim z_world"* is **REFUTED** as a route.

So the build is fully specified: **adopt the SD-070 training path in the `x734` / 737 driver
family**, which still runs the 0/61 configuration. No open question remains --
`complicated (buildable)`, not `complex (probe-gated)`.

**Do not reach for the naive fix.** Per the 780 doc, "just enable prescribed P0" is refuted
in-corpus by SD-070 (it collapses PR to ~1.06). The fix has two parts: a gradient path, and a
supervision target that is not action-uninformative. SD-070 supplies both.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | `claim_ids: []`; localization probe, promotes and demotes nothing |
| Biological reference | n/a for the defect | the finding is an implementation fault, not a translation question |
| Prerequisites | **missing** | the warmup phase does not train the encoder it is named for |
| Implementation | **partial / defective** | 0 of 61 latent-stack tensors move; no optimizer group covers them |
| Environment | adequate | solvable from the local view at 48.05 (738 anchor); oracle 57.2 |
| Measurement | **under-instrumented** | no trained-policy positive control, so policy-capacity and representation-quality cannot be fully separated |
| Integration | **partially coupled** | the guard detects but the driver family has not adopted the working training path |
| Scale | **likely insufficient** | PPO at this budget fails on raw obs where greedy reaches 48.05 |

**Recommended `epistemic_category`: `competence_implementation_gap`.
Recommended `evidence_direction`: `non_contributory`** (no claim tags; the run weights nothing).

---

## 5. Learning extracted

1. **A detection guard is worth nothing until a driver calls it.** The guard landed on
   2026-07-19 and 737a is the run that adopted it; that adoption is the only reason a 7.1-hour run
   is interpretable rather than quietly wrong. Landing a guard and adopting it are separate pieces
   of work and must be tracked separately.
2. **Record a confound rather than gating on it when it affects a subset of arms.** Putting the
   guard under `recorded_preconditions` kept the unaffected `ppo_raw_obs` control readable, where
   a flat gating entry would have returned whole-run `precondition_unmet` and buried it.
3. **A failing CONTROL arm can be more informative than the treatment arm.** `ppo_ree_latent` was
   confounded and says nothing; `ppo_raw_obs` failing at 0.567 against a 48.05 greedy anchor on the
   same view is what localizes the bottleneck to policy learning.
4. **A phase named for training an encoder is not evidence it trains one.** "P0 world-model
   warmup" ran 200 episodes and moved zero tensors. Weight-delta instrumentation on a training
   phase is cheap and should be default, not a diagnostic added after a campaign goes wrong.
5. **A resolved upstream adjudication should be re-checked before repeating "blocked".** The 780
   doc's deferral to V3-EXQ-783 was correct when written and stale by the time 737a ran; 783 had
   already confirmed SD-070 works. Deferrals need a re-check trigger, or they outlive their cause.

---

## 6. Routing

**(a) `/implement-substrate` -- priority 1** (user-confirmed 2026-07-20).
`recommended_substrate_queue_entry.action: create`. No existing `substrate_queue.json` entry covers
this gap (119 entries checked; the nearest, `sd_actor_critic_action_learning`, is `implemented` and
addresses the actor, not the encoder training path). The entry carries this run as its first
failure record, with V3-EXQ-780 as the prior strike.

**(b) `/queue-experiment` -- V3-EXQ-737b after the encoder fix lands** (user-confirmed).
Same question, alphabetic suffix. Two required changes:
  1. Re-run on the SD-070 training path so `ppo_ree_latent` measures a *learned* representation.
     Assert a non-zero world-path weight delta as a **gating** precondition on that arm.
  2. Add a **policy-learning positive control** -- a trained policy known to clear the floor at
     D3 -- so representation-quality and policy-learning-capacity can be separated. Without it a
     null on the REE latent remains aliased with "PPO cannot learn this at this budget", which is
     what limits the present run.

**Not routed:** no `/lit-pull` (the finding is an implementation fault); no claim weighting
(`claim_ids: []`).

**Re-derive brake:** not applicable -- the manifest declares `brake_exempt: true` with a recorded
reason, and the run carries no claim tags.

---

## 7. Ledger delta (Step 9b)

**None owed.** V3-EXQ-737a is a *localization* probe, not the adjudicator of any pre-registered
leg. The `competence_floor` question's representation leg (`H-rep`) was already eliminated by
V3-EXQ-747/749, and this run's confounded latent arm is not evidence about it either way.
Registering or resolving anything from this run would misattribute a frozen-random-projection
measurement to a representation hypothesis. Skipped cleanly.

---

*Adjudicated by session `malloc-stack-autopsy-extended-a0e312`. Inputs: the V3-EXQ-737a manifest
(per_rung, headline, readiness, interpretation.recorded_preconditions,
interpretation.zworld_arm_reading, notes, brake_exempt_reason);
`zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` §6c/§6d;
`failure_autopsy_V3-EXQ-783_2026-07-18.json` (status confirmed);
`substrate_queue.json` (119 entries, no covering entry); V3-EXQ-738's 48.05 local-view anchor.*
