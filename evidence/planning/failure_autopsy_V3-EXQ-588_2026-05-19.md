# Failure Autopsy — V3-EXQ-588 (EXQ-ISEF-002 transient benefit z_goal seeding)

- **Generated (UTC):** 2026-05-19T21:53:32Z
- **Scope:** single
- **Status:** confirmed (interactive gate, user-confirmed 2026-05-19)
- **Run:** `v3_exq_588_isef002_transient_benefit_zgoal_seeding_20260518T222457Z_v3`
- **Queue:** V3-EXQ-588 · **Purpose:** evidence · **claim_ids:** MECH-189
- **Outcome:** FAIL · manifest `evidence_direction: does_not_support` (pre-set; governance held pending this autopsy)
- **Not a crash.** Ran to completion. Autopsy, not `/diagnose-errors`.

---

## 1. Facts (no interpretation)

**Scientific question (script):** Does `transient_benefit_enabled=True` (multiplier=3.0) produce earlier
`z_goal.norm() > 0.4` crossing than uniform resource placement?

**Design:** ARM_0 control (`transient_benefit_enabled=False`) vs ARM_1 treatment (patches ON).
Fresh agent per arm x seed; agent persists 1000 episodes x 200 steps. N=5 seeds.
Agent: `z_goal_enabled=True`, `alpha_world=0.9`, `drive_weight=2.0`; GoalConfig defaults
`drive_ema_alpha=1.0`, `drive_floor=0.0`, `benefit_threshold=0.1`.

### Criterion results

| Criterion | Role | Result | Detail |
|---|---|---|---|
| **C1** | primary gate | **FAIL** | ARM_0 median first-crossing = **1001** (sentinel); ARM_1 median = **1001**; threshold = 700.7 (0.7 x ARM_0) |
| C2 | informational | PASS | ARM_1 mean transient contacts/ep **0.029** vs ARM_0 **0.000** |
| C3 | informational | PASS | ARM_1 mean `active_episode_fraction` **0.413** vs ARM_0 **0.237** |

**Failed criterion type:** discrimination in name only -- both arms **tied at never crossing**
the 0.4 developmental gate. This is not "patches slower than control"; it is "neither arm
reaches the gate in 1000 episodes."

### Per-seed first-crossing (episode index; 1001 = never)

| Seed | ARM_0 | ARM_1 | ARM_1 final z_goal.norm |
|---|---|---|---|
| 42 | 1001 | 1001 | 0.0011 |
| 43 | 1001 | 1001 | ~0 |
| 44 | 1001 | 1001 | ~0 |
| 45 | 1001 | 1001 | 0.017 |
| 46 | 1001 | 1001 | ~0 (peak mid-run 0.139, decayed) |

All five seeds x both arms: `first_crossing_episode = 1001`.

### Script interpretation grid match

From `v3_exq_588_isef002_transient_benefit_zgoal_seeding.py`:

> **C1 FAIL: similar first-crossing both arms** -> Patches alone insufficient; z_goal encoder
> or MECH-189 write path may be the bottleneck; queue goal-seeding pipeline diagnostic.

C2/C3 passing confirms patches **do** spawn contacts and raise shallow goal activation
(`is_active()`), but not the C1 endpoint.

---

## 2. Claim-layer mapping

### MECH-189 (tagged)

- **Claim text:** Child-phase high-salience benefit contacts under high contextual complexity
  write to **persistent ContextMemory** as super-ordinal goal anchors (SD-016 / MECH-150/151).
- **Status:** candidate, confidence 0.0, v3_pending path via development cluster.
- **Lit (parallel, not blended):** Rovee-Collier 1987 (accidental contingency discovery);
  Berridge & Robinson 1998 (wanting/liking). lit_conf ~0.7; exp_conf from this run should
  **not** weigh.

**Did the experiment test MECH-189 under conditions where it could express itself?** **No.**

EXQ-588 measures within-episode `GoalState` attractor norm (MECH-112 / SD-012 / DEV-NEED-006
infant gate), not ContextMemory super-ordinal writes. The correct tags would include
MECH-329 (wanting precedes liking), MECH-112, and/or `claim_ids=[]` diagnostic for
`infant_substrate:GAP-11` / DEV-NEED-006. Tagging MECH-189 alone mis-attributes a
goal-pipeline bootstrap failure to a child-phase memory-consolidation claim.

**Governance conflict note:** indexer `conflict_ratio=0.667` with one `does_not_support`
from this run is **illusory** -- the run does not test the claim's operative substrate
(ContextMemory write path + contextual complexity gate).

### Related completed diagnostic (context)

**V3-EXQ-582a PASS** (2026-05-19, `claim_ids=[]`, supersedes 582): `drive_floor=0.9`
lifts `effective_benefit` at contact and fires seeding in 3/3 seeds; `drive_floor=0.0`
(OFF) gives **0** seedings -- same contact-sparsity regime as 588's ARM_0. EXQ-588 did
**not** enable `drive_floor` or `drive_ema_alpha < 1.0`, so it re-ran the pre-amendment
collapse stack while only adding env-side patches.

---

## 3. Biological-reference triage

| Field | Assessment |
|---|---|
| Closest mechanism | Incentive salience / accidental contingency learning (infant vocal/kick
  operant discovery; mesolimbic wanting) |
| Dependencies in real brains | Sustained wanting trace after sparse reward; repeated
  action-outcome pairing; caregiver/salient context (not tested here) |
| Formal-definition import? | **No** -- engineering patches + latent norm gate |
| Lit status | **Present** on MECH-189 anchors; biology supports the *class* of mechanism |
| Failure vs missing dependency? | **Missing dependency signature:** sparse contacts +
  EMA-smoothed `benefit_exposure` + satiation-at-contact drive collapse + `benefit_threshold`
  0.1 prevent reliable `GoalState.update()` pulls; `decay_goal` erodes norms before 0.4.
  Patches increase contact rate (~0.03/ep) but not enough to close the SD-012 gate. |

**Not lit-pull.** Biology does not refute transient salient benefits seeding approach
motivation; the translation stack is incomplete.

### Mechanistic detail (code-verified)

On transient patch contact: `contact_benefit = resource_benefit (0.3) * multiplier (3.0) = 0.9`.
`harm_signal > 0` updates `benefit_exposure` EMA with `nociception_ema_alpha=0.1` ->
increment ~**0.09** from zero on a single contact. `GoalConfig.benefit_threshold = 0.1` ->
**first contact often fails to trigger** `GoalState.update()`. Simultaneously,
`agent_energy` restores on contact -> `drive_level = 1 - energy` collapses -> SD-012
multiplier ~1.0. `decay_goal=0.005` every step erodes any brief norm (seed 46 peaked
0.139 mid-run, ended ~0).

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **could-not-express** | MECH-189 = ContextMemory super-ordinal writes; run = infant z_goal.norm gate |
| Biological reference | **clear** | wanting/contingency learning supported; failure not biological falsification |
| Prerequisites | **missing** | goal_pipeline:GAP-3 SD-012 stack (`drive_floor` / sustained drive trace) not in 588 config; 582a shows floor required for seeding in sparse-contact regime |
| Implementation | **partial** | GAP-3 env patches **work** (C2); GoalState path **inert** for 0.4 gate without SD-012 amendments |
| Environment | **too sparse for gate** | ~0.03 transient contacts/ep; patches help but insufficient for norm 0.4 x 1000 ep |
| Measurement | **adequate but high gate** | C1=0.4 is DEV-NEED-006 proposal threshold; C3 `is_active()` true while C1 false (norm can stay <<0.4) |
| Integration | **partially coupled** | env->body[11]->update_z_goal chain live but gated off at threshold+drive |
| Scale | adequate | 2M steps sufficient if gate were reachable |

**Recommended `epistemic_category`:** `non_contributory` (user-confirmed)

**Recommended `evidence_direction`:** `non_contributory` for MECH-189 (overrides manifest
`does_not_support`)

**`pending_retest_after_substrate`:** true -- retest infant patch benefit only after
goal-seeding diagnostic passes with SD-012 amendments + instrumentation.

**`narrow_supports_flag`:** false (no support to preserve)

---

## 5. Learning extracted

1. **Transient benefit patches are necessary but not sufficient** for the infant z_goal gate:
   C2/C3 prove env implementation; C1 proves the write path cannot reach 0.4 under default
   GoalConfig in this contact-density regime.

2. **The blocking prerequisite is the goal-seeding pipeline, not MECH-189.** EXQ-582/582a
   already localized SD-012 sustained-drive collapse; 588 is consistent -- patches without
   `drive_floor` (or equivalent) do not change the outcome.

3. **Claim tag error is load-bearing for governance.** A `does_not_support` on MECH-189 from
   this run would falsely weaken a child-phase memory claim from an infant attractor test.

4. **Positive signal (non-governance):** treatment raises `is_active()` fraction -- patches
   should remain in infant curriculum Phase 1 env kwargs once SD-012 stack is fixed.

---

## 6. Repair pathway (user-confirmed)

**Routing:** `/queue-experiment` -- goal-seeding pipeline diagnostic (EXQ-588b or next ID
per skill):

- `claim_ids=[]`, `experiment_purpose=diagnostic`
- Arms: OFF (`drive_floor=0`, `drive_ema_alpha=1.0`) vs floor arm (`drive_floor=0.9`, per 582a)
  vs floor + `transient_benefit_enabled=True`
- Log per contact: `benefit_exposure`, `drive_level`, `effective_benefit`, seeding fired,
  `z_goal.norm()`
- Primary: seeding fires in >=2/3 seeds post-warmup with patches+floor; secondary: norm
  trajectory toward 0.4 (may still need longer horizon or gate recalibration)

**Do NOT** re-queue as MECH-189 evidence until ContextMemory write path exists.

**NOT:** lit-pull, governance demotion, implement-substrate as first move (582a already
validated floor in substrate; diagnostic confirms combination).

---

## 7. Draft evidence_quality_note (for `/governance`)

> "V3-EXQ-588 FAIL (infant_substrate:GAP-11): non_contributory for MECH-189. Both arms
> median first-crossing=1001 (never reached z_goal.norm>0.4); C1 discrimination tied at
> failure, not 'patches slower than control.' C2/C3 PASS: patches generate contacts
> (0.029/ep) and higher is_active() fraction (0.41 vs 0.24) -- env GAP-3 works; GoalState
> gate not reachable with default SD-012 (benefit_threshold 0.1 + EMA alpha 0.1 + drive
> collapse at contact + decay). MECH-189 tests child-phase ContextMemory super-ordinal
> writes; this run tests infant within-episode attractor (MECH-112/DEV-NEED-006) -- claim
> could not express. Consistent with EXQ-582 substrate-ceiling and EXQ-582a PASS on
> drive_floor=0.9. Route: goal-seeding pipeline diagnostic (floor + patches + contact
> instrumentation) before any MECH-189 retest. pending_retest_after_substrate=true.
> lit/exp not blended."

---

## 8. Governance actions checklist

- [ ] Manifest `evidence_direction` / per-claim MECH-189 -> `non_contributory` + note above
- [ ] Mark run reviewed in `review_tracker.json`
- [ ] Clear MECH-189 `hold_candidate_resolve_conflict` once note applied (conflict was
      illusory from mis-tagged run)
- [ ] Queue goal-seeding diagnostic via `/queue-experiment` (separate session)
