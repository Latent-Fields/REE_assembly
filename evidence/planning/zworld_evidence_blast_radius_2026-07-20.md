# z_world Untrained-Encoder Defect -- EVIDENCE Blast Radius

- **Generated:** 2026-07-20T19:40:42Z
- **Session:** `festive-neumann-b7b7b4`
- **Scope:** ANALYSIS ONLY -- surfaces recommendations for `/governance` to apply. Nothing in
  `claims.yaml`, any manifest, `review_tracker.json`, or `substrate_queue.json` was edited.
- **Defect diagnosis:** `zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` section 6c
- **Fix (landed, DEFAULT OFF `zworld_p0_episodes=0`):** `ree-v3/experiments/_lib/zworld_p0_warmup.py`

---

## Headline

**Three unadjudicated reviewed runs are affected, and all three are already
non-load-bearing for claim confidence** (`claim_ids: []`, `experiment_purpose: diagnostic`,
`evidence_direction: non_contributory` where set). **No claim confidence is mis-weighted and no
promotion rests on a void arm.**

**The residual exposure is not in the claims plane at all -- it is one architecture document.**
`docs/architecture/sd_actor_critic_action_learning.md` section 1 states the V3-EXQ-734 and
V3-EXQ-737 results as load-bearing build-spec facts, including the sentence *"The frozen
prediction latent is a strictly worse action substrate than raw observation"* -- a conclusion
drawn from an arm whose latent was a **frozen random projection**, not a prediction-trained one.
That doc is hand-maintained and **regenerates from nothing**, so no pipeline will ever revisit it.
It is the live instance of the blind spot this audit was asked to find.

`claims.yaml` is **clean**: the MECH-457 entry already carries the correct two-part reading of 737
and names "the x734/737 driver family" defect explicitly (added by the 737a autopsy, 2026-07-20).
No claims-side action is owed.

---

## 1. Scope and exclusions

Six `_train_all_on_agent` callers exist. `_lib/zworld_encoder_guard.py`,
`_lib/zworld_p0_warmup.py`, and `_lib/baselines/exq742_mech457_bias_head_baseline.py` are library
modules, not experiment drivers. The four drivers that produced manifests:

| Driver | Manifests | Disposition |
|---|---|---|
| `v3_exq_728_trained_allon_capability_point.py` | 2 | **Owned** -- `failure_autopsy_V3-EXQ-728_2026-07-20` |
| `v3_exq_737_ree_latent_policy_head_competence_probe.py` | 3 | 1 owned (`737a` autopsy, `20260720T124318Z`); **2 residual** |
| `v3_exq_734_env_difficulty_competence_recovery_sweep.py` | 1 | **1 residual** |
| `v3_exq_742_mech457_actor_critic_onoff.py` | 2 | **Owned** -- MECH-457 campaign, re-posed by `musing-einstein-c80816` |

Residual set audited here: **3 manifests**. This matches the expected small residual.

`v3_exq_734_...py` is the module that **defines** `_train_all_on_agent`; 737 and 742 import it.
Its own docstring (lines 131-145) now documents the defect and the guard's call-site placement,
so the code-side blast radius is closed. Only the evidence side was open.

---

## 2. Affected runs

### 2.1 `v3_exq_734_env_difficulty_competence_recovery_sweep_20260711T092149Z_v3`

- **Driver:** `v3_exq_734_env_difficulty_competence_recovery_sweep.py`
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `interpretation_label: ree_substrate_ceiling`
- **`claim_ids`:** `[]`; `experiment_purpose: diagnostic`; brake-exempt
- **In `reviewed_run_ids`:** **YES**
- **Arms void:** `ree_trained_allon` (the 724-A0 all-ON recipe: P0 world-model warmup + P1
  two-head REINFORCE, e2 frozen in P1 -- the exact optimizer-group set that omits `latent_stack`)
- **Arms unaffected:** `random_walk` (no training), `vanilla_ppo` (PPO over the **raw**
  observation vector -- runs no P0 warmup), `greedy_oracle` (no agent)

**Why the headline is void.** The load-bearing DV is
`ree_allon_recovers_above_floor_at_some_difficulty`, evaluated **entirely on the void arm**. The
recorded verdict `ree_substrate_ceiling` is defined as *"readiness holds, `ree_trained_allon`
never clears the floor, BUT the matched PPO control does"* -- i.e. the verdict is a **contrast
between a void arm and an intact one**, and is therefore not established. What the run does still
support, on defect-free arms alone, is the weaker and still-useful fact that **`vanilla_ppo`
recovers at D2 while random_walk does not** -- the env is learnable by *a* learner at D2.

The four readiness gates are mixed: `oracle_clears_floor_all_rungs` (6.04),
`hazard_free_rung_achievable` (56.86) and `sufficient_eval_episodes` (20) are all measured on
defect-free arms and **stand**. `baseline_reproduces_incompetence_at_D0` (0.0875 vs 1.0) is
measured on the void arm and **does not stand** -- it reproduced the incompetence of an agent
riding a random projection, which is not evidence about the all-ON recipe.

### 2.2 `v3_exq_737_ree_latent_policy_head_competence_probe_20260711T192837Z_v3`

- **Machine:** `DLAPTOP-4.local`
- **Outcome:** FAIL / `evidence_direction: non_contributory` / `policy_learning_insufficient_or_deeper`
- **`claim_ids`:** `[]`; diagnostic; brake-exempt
- **In `reviewed_run_ids`:** **YES**
- **Arms void:** `ppo_ree_latent` (PPO actor+value over `z_world`), `ree_bias_head` (P1 REINFORCE
  bias head over the same latent)
- **Arms unaffected:** `ppo_raw_obs`, `greedy_oracle`, `random_walk`

### 2.3 `v3_exq_737_ree_latent_policy_head_competence_probe_20260711T222643Z_v3`

- **Machine:** `ree-cloud-1`
- **Outcome:** FAIL / `policy_learning_insufficient_or_deeper` (no `evidence_direction` field set)
- **`claim_ids`:** `[]`; diagnostic; brake-exempt
- **In `reviewed_run_ids`:** **YES**
- **Arms void / unaffected:** identical to 2.2

**These two are the ORIGINAL 737 H1 discriminator runs**, and they are structurally identical to
the `20260720T124318Z` run the `737a` autopsy adjudicated -- same five arms, same config
(`p0_warmup_episodes: 200`, no `zworld_p0_episodes`), and near-identical numbers
(`d3_ppo_ree_latent` 0.217 / 0.283 vs the autopsy's 0.217). The 737a autopsy's reasoning
therefore **transfers to them verbatim**; it simply never named them, because its declared scope
was "single run".

That transfer includes the autopsy's finding (1): `ppo_raw_obs` is a defect-free control and its
sub-floor score (0.567 / 0.417 against a 1.0 floor, on an env where local-view greedy reaches
48.05) is intact evidence that **the D3 bottleneck is policy learning**. The 07-11 pair
independently replicates that on two different machines.

---

## 3. Citation audit -- who leans on these runs

| Citing artifact | Cites | Status |
|---|---|---|
| `docs/claims/claims.yaml` (MECH-457) | 737, 734 | **CLEAN** -- carries the two-part reading + names the "x734/737 driver family" defect; explicitly says "Do NOT record H1 as confirmed on the strength of 737 alone" |
| `evidence/planning/ree_ai_design_critique_plan.md` (WS-1 `fanout_recurrence_metabolized`) | 737a/728 | **CLEAN** -- 2026-07-20 note already records the 0/61 finding and the "evidentially void" framing |
| `evidence/planning/substrate_queue.json` | 734, 737 | **CLEAN** -- `sd_zworld_warmup_optimizer_group` (priority 1, ready) + the re-run ladder |
| `docs/architecture/sd_actor_critic_action_learning.md` §1 | **734 + 737** | **STALE -- action owed (see §4)** |
| `docs/roadmap.md` Status Snapshots | 734, 737 | **No action** -- dated historical snapshots, correct as of their timestamp; not live status rows |
| `evidence/planning/hypothesis_space{,_registry}.v1.json` | 734, 737 | **No action** -- the `competence_floor` question is owned by the MECH-457 re-pose |
| `evidence/planning/mech457_retention_portfolio_2026-07-18.md` | 734 | **Owned** by the MECH-457 campaign |

---

## 4. The one live finding: `sd_actor_critic_action_learning.md` section 1

The design doc for the MECH-457 actor-critic substrate opens by deriving its build spec from the
734/737 portfolio. Three of its bullets rest on void arms:

- **V3-EXQ-734 bullet** -- *"REE all-ON recovers at no rung; PPO control recovers at D2 ->
  difficulty is not the lever."* The second clause stands; the first is the void arm.
- **V3-EXQ-737 bullet**, marked **LOAD-BEARING FAIL** -- *"a real trainable PPO actor + value
  baseline over REE's frozen `z_world` scored 0.217 res/ep @D3 ... The frozen prediction latent
  is a strictly worse action substrate than raw observation."*

That last sentence is the sharpest instance of the defect's evidential reach. It reads as a
finding about **prediction-trained representations being action-inadequate**. What was actually
measured is a **randomly-initialised projection** being action-inadequate -- which is close to
tautological and licenses nothing about REE's latent. The doc also drew the correct conclusion
for the wrong reason: `ppo_raw_obs` genuinely does beat `ppo_ree_latent` in these runs, but the
comparison is "raw observation vs random projection", not "raw observation vs learned latent".

This matters more than a stale sentence because §1 is the **stated justification for building
MECH-457's actor-critic at all**, and because line 274 pins a substrate parameter to it
(*"Trunk width 128 matches the validated V3-EXQ-734/737 PPO net"* -- that pin is unaffected; it is
an architectural width, not a result).

**Recommendation for `/governance` (do not apply from this document):** add a defect caveat to
§1 of `docs/architecture/sd_actor_critic_action_learning.md`, scoped to the two REE-latent
bullets, leaving the 738 anchor and the `ppo_raw_obs` reading intact. Draft text:

> **2026-07-20 defect caveat (V3-EXQ-780 / 737a / 728).** The `ree_trained_allon`,
> `ree_bias_head` and `ppo_ree_latent` arms cited in this section ran on a `z_world` that was
> never prediction-trained: the P0/P1 warmup in the `x734` `_train_all_on_agent` driver family
> builds three optimizer groups (e2, lateral-PFC bias head, OFC devaluation head) and none
> covers `latent_stack` (measured 0 of 4 world-encoder and 0 of 61 `latent_stack` tensors
> changed). Those arms therefore compared raw observation against a **frozen random projection**,
> not against a learned REE latent, and the claim that "the frozen prediction latent is a
> strictly worse action substrate than raw observation" is **NOT established**. The
> `ppo_raw_obs`, `vanilla_ppo`, `greedy_oracle`, `random_walk` and V3-EXQ-738 anchors are
> structurally unaffected and stand -- including the reading that the D3 bottleneck is policy
> learning. Retest owed: V3-EXQ-734b / 737b (SD-070 adoption validation, `zworld_p0_episodes=60`).

---

## 5. Recommended manifest dispositions (drafted, NOT applied)

None of the three runs should be `evidence_direction: superseded` **yet** -- supersession is
earned by the corrected re-run landing, and `V3-EXQ-734a` (claimed), `V3-EXQ-734b` and
`V3-EXQ-737b` (both pending) are already queued for exactly that. The correct interim action is
an `evidence_direction_note` amendment recording the defect, so that a reader of the manifest is
not left with an unqualified `ree_substrate_ceiling` verdict.

Because all three are already `non_contributory` / `claim_ids: []`, **no confidence recomputation
and no index rebuild is required** -- these runs weight nothing today.

Draft note text, to append to each of the three manifests' `evidence_direction_note`:

> **2026-07-20 Z_WORLD DEFECT AMENDMENT (analysis: `zworld_evidence_blast_radius_2026-07-20.md`;
> diagnosis: `zworld_bc_install_failure_V3-EXQ-780_2026-07-19.md` s6c).** The P0/P1 warmup in this
> driver's `_train_all_on_agent` family builds three optimizer groups (e2, lateral-PFC bias head,
> OFC devaluation head), NONE covering any `latent_stack` parameter, so `split_encoder.world_encoder`
> was never stepped and `z_world` remained a FROZEN RANDOM PROJECTION -- silently, no error.
> Measured on two independent drivers: 0 of 4 world-encoder and 0 of 61 `latent_stack` tensors
> changed, bit-identical. **Void arms: {ARMS}.** **Unaffected arms: {ARMS}** (no P0 warmup: raw-
> observation learners, scripted oracle, random walk) -- their readings stand. The headline verdict
> `{LABEL}` rests on a void arm and is NOT established. Retest owed via `{RERUN}`. This run remains
> `claim_ids: []` / diagnostic / `non_contributory` -- it weighted no claim before this amendment and
> weights none after it. PROMOTES/DEMOTES NOTHING.

Per-run substitutions:

| Run | Void arms | Unaffected arms | Label | Retest |
|---|---|---|---|---|
| `v3_exq_734_..._20260711T092149Z_v3` | `ree_trained_allon` | `random_walk`, `vanilla_ppo`, `greedy_oracle` | `ree_substrate_ceiling` | V3-EXQ-734a / 734b |
| `v3_exq_737_..._20260711T192837Z_v3` | `ppo_ree_latent`, `ree_bias_head` | `ppo_raw_obs`, `greedy_oracle`, `random_walk` | `policy_learning_insufficient_or_deeper` | V3-EXQ-737b |
| `v3_exq_737_..._20260711T222643Z_v3` | `ppo_ree_latent`, `ree_bias_head` | `ppo_raw_obs`, `greedy_oracle`, `random_walk` | `policy_learning_insufficient_or_deeper` | V3-EXQ-737b |

**`review_tracker.json`: leave untouched.** All three are correctly recorded as reviewed --
they *were* reviewed. The defect does not un-review them; per
`feedback_reviewed_does_not_mean_autopsy_applied`, reviewed status and adjudication status are
separate planes, and removing them would only make them re-surface as pending without recording
why.

---

## 6. Also worth recording: the 2026-07-11 cluster autopsy

`failure_autopsy_734-737-conversion-ceiling-competence_2026-07-11.{md,json}` adjudicated 734 and
737 together and concluded the deficit was a *"single missing mechanism = MECH-457"*. That
conclusion was **already refuted on independent grounds** by V3-EXQ-742 (2026-07-13, recorded in
the MECH-457 claim entry: all four actor-critic arms sub-floor with readiness met, so the deficit
sits upstream of action-learning credit-assignment).

The z_world defect is a **second, and mechanistically prior**, invalidation of the same autopsy:
its two load-bearing inputs were both void-armed. No action is owed -- the autopsy's conclusion is
already retracted in the live claim text, and re-opening a superseded autopsy adds nothing. It is
noted here so a future reader who finds that autopsy does not have to re-derive why it is stale.

---

## 7. What this audit did NOT find

- **No PASS run outside the already-owned set.** The confirmed instance that motivated this audit
  (`v3_exq_728_..._20260709T224533Z_v3`, PASS + reviewed + closed WS-3) is the only one of its
  shape, and it is adjudicated.
- **No claim whose confidence is mis-weighted.** Every residual run is `claim_ids: []` +
  diagnostic + non_contributory.
- **No plan-doc status row that a corrected re-run would flip.** The only stale plan-doc
  reference is the `sd_actor_critic` design-doc prose in §4, which is a justification narrative,
  not a status row.

---

## 8. Summary of recommendations (for `/governance`)

1. **Amend** `docs/architecture/sd_actor_critic_action_learning.md` §1 with the §4 caveat text.
   *(The one action with real content.)*
2. **Amend** the `evidence_direction_note` on the three manifests in §5. Do not set
   `superseded` until 734b / 737b land.
3. **Leave** `review_tracker.json`, `claims.yaml`, and `substrate_queue.json` unchanged -- all
   three are already correct.

**PROMOTES NOTHING. DEMOTES NOTHING.**
