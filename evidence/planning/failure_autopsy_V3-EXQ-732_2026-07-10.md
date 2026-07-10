# Failure Autopsy — V3-EXQ-732 (H1/H2 policy-learning discriminator; H2 self-route NOT confirmed)

**Generated:** 2026-07-10T06:24:33Z
**Scope:** single (diagnostic adjudication)
**Status:** confirmed (interactive gate answered)
**Target:** `v3_exq_732_policy_learning_discriminator_20260710T014857Z_v3` · queue_id V3-EXQ-732 · `experiment_purpose=diagnostic` · `claim_ids=[]` · `evidence_direction=non_contributory` · machine `ree-cloud-4`
**Parent:** `failure_autopsy_V3-EXQ-724_2026-07-09` (competence_deficit_diffuse; prescribed 732 as the brake-exempt H1/H2 discriminator). Grandparent: `failure_autopsy_V3-EXQ-719a_2026-07-08` (first direct competence measurement).
**Context:** WS-1 of `evidence/planning/ree_ai_design_critique_plan.md` (capability floor before structure); `conversion_ceiling_campaign_plan.md`.

---

## 1. Facts (no interpretation)

732 is the H1/H2 discriminator 724 prescribed. Three arms, env/seeds/oracle/B0 anchor reused **verbatim** from 724 (`ENV_KWARGS` size-12, 5 resources, 4 hazards, reef, seeds 42/43/44, 200 steps/ep, 20 P2 eval eps, floor = 1.0 res/ep).

- **B0** `ree_biashead_reinforce_allon` — 724 A0 incompetence anchor (all-ON REE, P0 e2 warmup, P1 two-head REINFORCE, encoder frozen).
- **B1** `ree_repr_full_a2c_head` (**H1 test**) — REE all-ON encoder P0-warmed then **frozen**; a **full trainable trunk+A2C head** (own Adam) over `z_self (+) z_world` learns the action.
- **B2** `vanilla_a2c_rawobs` (**H2 test**) — vanilla A2C, matched trunk+head, over the **raw observation vector** (`body_state + world_state + harm_obs + harm_obs_a + harm_history`, dim **398**); no REE machinery.

**Matched learner (design choice, on the record):** B1 and B2 share the SAME online A2C — `trunk_hidden 128, lr 1e-3, gamma 0.99, entropy_beta 0.01, value_coef 0.5, grad_clip 1.0`, **P1 = 200 episodes** — so the B1-vs-B2 contrast isolates the representation front-end with no algorithm confound. The A2C update is **end-of-episode Monte-Carlo** (discounted-return baseline) → **~200 gradient updates total** over ~40k env steps.

**Readiness gates — all MET.** Greedy nearest-resource **oracle clears floor at 6.05** (min/ep; env achievable with *privileged* access). **B0 reproduces incompetence** (0.20 < 1.0). Every cell logged 20 P2 episodes.

Per-arm P2 `mean_resources_per_episode` (floor 1.0; seeds 42/43/44):

| Arm | Role | res/ep (seeds) | mean | reward | n_supra_floor |
|---|---|---|---|---|---|
| B0 bias-head REINFORCE all-ON | H0 anchor | 0.25 / 0.00 / 0.35 | **0.20** | −0.86 | 0/3 |
| B1 REE repr + full A2C head | H1 | 0.00 / 0.00 / 0.35 | **0.12** | −0.52 | 0/3 |
| B2 vanilla A2C raw obs | H2 | **0.65** / 0.40 / 0.00 | **0.35** | −0.39 | 0/3 |
| oracle (privileged) | + control | 6.75 / 6.20 / 6.05 | 6.33 | — | 3/3 |

`b1_clears_floor=false`, `b2_clears_floor=false`. Load-bearing criterion `discriminator_resolved_nondegenerate` = passed (arms distinct, oracle clears, B0 reproduces). **Self-route (HYPOTHESIS): `H2_observation_interface_unlearnable`** (readiness met AND B2 sub-floor).

## 2. The load-bearing structural fact (what the self-route could not see)

**B2's budget was set for the CONTRAST, not for learnability.** The script states the shared 200-episode budget exists "so the contrast isolates the representation front-end." That budget answers *"does the REE representation help at ~40k steps?"* — **not** *"is the observation learnable by any policy at this scale?"* The H2 label ("unlearnable by ANY policy at this scale") over-claims relative to what B2 measured.

**Three converging tells that the observation IS learnable and B2 was simply under-converged:**

1. **B2 was the BEST arm** (0.35 > B0 0.20 > B1 0.12) on the **raw** observation with **zero REE machinery**. If the observation genuinely did not afford resource localization, the raw-obs arm could not lead.
2. **B2 seed 42 foraged in 12/20 episodes** (mean 0.65, per-ep `[1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,2,0]`); seed 43 in 6/20 (0.40). That is a **rising, partially-learned** foraging distribution — the opposite of an unlearnable interface (which looks like B0 seed-43's flat 20×0).
3. **The cross-seed spread 0.65 / 0.40 / 0.00 is the fingerprint of a high-variance, under-converged Monte-Carlo learner** (~200 updates, entropy 0.01), not a structural ceiling (a ceiling is uniformly ~0 across seeds).

**Compounding confound:** net episode reward is **negative across all arms** (B2 −0.39, B0 −0.86), dominated by contamination penalties (3.6–11.6 contaminations/ep). With ~200 MC updates against a net-negative signal, the policy gradient mostly encodes "avoid contamination," not "forage" — a credit-assignment problem stacked on the budget starvation.

**Readiness-battery hole (the generalizable design lesson).** 732's readiness gates validate **env-achievability** (oracle 6.05) and **premise reproduction** (B0 sub-floor), but include **no gate proving the learner+budget can solve foraging at all**. Absent that gate, a sub-floor B2 conflates *"unlearnable observation"* with *"under-powered learner."* This is the same class of blind spot 724 had (no learned non-REE control) — one level deeper.

## 3. Claim-layer mapping

No claim tagged (`claim_ids=[]`, diagnostic, `non_contributory` — **promotes/demotes nothing**, correctly excluded from scoring). Bears on the WS-1 competence floor and the `f_dominance_conversion_ceiling` competence gap. **Brake-exempt** (asks the H1/H2 build-direction question, tags no claim, recommends no lettered re-test of any claim). The re-derive brake's claim-keyed counter is 0 and does **not** fire; moreover the confirmed routing is a re-queue that **refuses** to declare a ceiling — the brake's *intent* (do not build on an unconfirmed ceiling) is satisfied a fortiori.

## 4. Biological-reference triage

Closest reference: a **learned sensorimotor foraging policy** (dorsal-striatal RPE-driven action learning) over a perceptual field. The autopsy question here is not primarily biological — it is a **test-power** question: whether a standard learner, given a fair budget, extracts resource location from the 398-dim observation. The 724 divergence (REE prediction-rich / action-poor) remains the live *architectural* hypothesis (H1); 732 does not adjudicate it because the H1 arm (B1) was starved by the same budget. Lit status: partial (motor-learning / actor-critic grounding not pulled for this substrate; not the blocker here).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (intact) | diagnostic, no claim tested |
| Biological reference | partial | not the operative axis this run; test-power is |
| Prerequisites | present | env solvable (oracle 6.05); obs contains world_state (resource field the REE encoder senses) |
| Implementation | **test under-powered (prime suspect)** | ~200 MC gradient updates, entropy 0.01, net-negative reward; budget set for the contrast, not learnability |
| Environment | adequate | oracle clears floor; proximity shaping present |
| Measurement | **design gap** | readiness battery validates env-achievability but not learner-adequacy → sub-floor B2 mis-reads as "unlearnable" |
| Integration | n/a | single-arm learners, no cross-module interaction under test |
| Scale / capacity | **insufficient (learner budget)** | 40k steps / 200 MC updates far below vanilla-RL foraging convergence; B2 still climbing (seed-42 12/20) |

**Recommended reading:** `precondition_unmet` → **`substrate_not_ready_requeue`** in REE terms (NOT `substrate_ceiling`). The unmet precondition is *learner-adequacy*: the H2 control was not trained enough to license an "unlearnable" verdict. Direct analog of the canonical **V3-EXQ-642** incident (self-routed `substrate_ceiling` but P0 never trained the substrate → correct route was re-queue). Manifest `evidence_direction = non_contributory` is correct for a diagnostic.

## 6. Adjudication of the load-bearing fork the user posed

- **(A) Genuinely unlearnable observation → `/implement-substrate` on the observation encoding.** **REJECTED for now.** Not licensed: B2 was the best arm, showed partial foraging (12/20 seed 42), and was starved to ~200 MC updates. Building an observation encoder on this evidence would build on an **unconfirmed ceiling** — precisely the 642 failure mode.
- **(B) B2's failure is a training-budget / exploration artifact → scale + re-run before any build.** **CONFIRMED** (user gate). The oracle proves the env is solvable with *privileged* nearest-resource access; it does **not** bound learnability-from-*observation* at 40k steps. All three arms were under-budgeted, so 732 resolves **neither** H1 nor H2 — it is **under-powered, not decisive**.

## 7. Routing — CONFIRMED: `/queue-experiment` → V3-EXQ-732a (power-fix re-run). NO build.

Same scientific question (H1 vs H2 / is the observation learnable), implementation defect = insufficient learner power → **alphabetic suffix `V3-EXQ-732a`**, `supersedes: V3-EXQ-732`, brake-exempt, `claim_ids=[]`, `experiment_purpose=diagnostic`, `non_contributory`.

### Redesign spec — `policy_learning_discriminator` re-power (732a)

- **Env / seeds / oracle / B0 anchor:** identical to 732/724 (same `ENV_KWARGS`, seeds 42/43/44, 200 steps/ep, 20 P2 eps, floor 1.0, greedy oracle positive control).
- **Primary lever (user-selected): off-policy / minibatched learner + bigger budget.** Replace the end-of-episode Monte-Carlo A2C (**~200 updates** — the core defect) with **PPO or DQN** doing **minibatched updates per rollout** (many gradient steps per env-step), at a budget **10–50× larger** (a budget at which vanilla RL is *known* to solve comparable gridworld foraging). Apply the SAME upgraded learner+budget to **both B1 and B2** so the representation-front-end contrast stays powered and fair.
- **Exploration:** stronger than entropy_beta 0.01 — raise entropy and/or add a count-based / novelty exploration bonus (helps the sparse-until-first-resource phase).
- **Reward-signal hygiene (recommended):** normalize / rescale returns so the foraging signal is not drowned by contamination penalties (net-negative reward across all 732 arms is a credit-assignment red flag). Do not silently change the DV — keep P2 `mean_resources_per_episode` as the load-bearing statistic.
- **NEW readiness gate (closes the 732 hole): learner-adequacy.** Before any sub-floor is read as an H2 verdict, the vanilla control must clear foraging (>= X% of oracle) on a plain sanity foraging env within the budget. If the control cannot solve even the sanity env, the run is `substrate_not_ready_requeue` (learner still too weak) — NOT an H2 verdict.
- **Interpretation grid (unchanged logic, now powered):**
  - Powered B2 clears floor → **observation IS learnable → H1** (the deficit is REE's action stack; build the action/policy substrate under `f_dominance_conversion_ceiling`, informed by MECH-455 competence-based IM). B1-vs-B2 delta then says whether the REE representation helps or hurts (H1 vs deeper-H1).
  - Powered B2 sub-floor **with the learner-adequacy gate passed** → **H2 confirmed** → THEN route `/implement-substrate` on the observation encoding.
  - B1 clears ∧ B2 sub-floor → flag leakage.

### Draft `evidence_quality_note` (governance writes; do not write here)
> V3-EXQ-732 policy-learning discriminator (diagnostic, claim_ids=[], non_contributory — promotes/demotes nothing). Self-routed `H2_observation_interface_unlearnable` (b1/b2 sub-floor, readiness met). Autopsy `failure_autopsy_V3-EXQ-732_2026-07-10` REJECTS the H2 verdict as UNCONFIRMED: the shared 200-episode / ~40k-step Monte-Carlo A2C budget was set for the B1-vs-B2 contrast, not for learnability; the H2 arm B2 (vanilla raw-obs) was the BEST arm (0.35) and foraged in 12/20 episodes on seed 42 (partial-learning signature, not an unlearnable interface); net reward was negative across all arms (contamination-dominated credit-assignment confound); and 732's readiness battery validates env-achievability (oracle 6.05) but has NO learner-adequacy gate — so a sub-floor B2 conflates "unlearnable observation" with "under-powered learner" (direct analog of the V3-EXQ-642 precondition-unmet incident). 732 is UNDER-POWERED, resolving neither H1 nor H2. Routed to /queue-experiment for V3-EXQ-732a (supersedes 732): re-run the discriminator with an off-policy/minibatched learner (PPO/DQN) at 10-50x budget + stronger exploration + a learner-adequacy readiness gate, BEFORE any observation-encoding build. No substrate_queue write (recommended_substrate_queue_entry.action=none) — the build target is exactly what the powered re-run decides. Brake-exempt (no claim tagged).

**No `substrate_queue` write** (`recommended_substrate_queue_entry.action = none`): H2 is not confirmed, so no observation-encoding substrate should be queued. The build target is exactly what the re-powered discriminator decides.

## 8. Learning extracted

1. **A "sub-floor control" is only an "unlearnable" verdict if the control was trained enough to succeed** — 732's B2 was starved to ~200 Monte-Carlo updates and was still the best, partially-foraging arm (seed-42 12/20). The observation is learnable; the learner was under-powered.
2. **A discriminator's budget must be sized for the harder of its questions.** 732's budget was set for the B1-vs-B2 *contrast* (equal starvation reads out as "the representation doesn't help"), which is too small to answer the *learnability* question the H2 branch needs. When one arm's null carries a "ceiling" verdict, that arm needs enough budget to *falsify* the ceiling.
3. **Readiness batteries need a learner-adequacy gate, not just an env-achievability gate.** Oracle-clears-floor proves the ENV is solvable with privileged access; it does NOT prove the LEARNER can extract the solution from the observation at the given budget. Missing that gate is what let a starved control self-route to `unlearnable`. (724 had the analogous hole: no learned non-REE control; 732 has: no *adequately-trained* one.)
4. **Monte-Carlo A2C at ~200 updates is the wrong learner for a "can it be learned at all" control** — its ~200 high-variance gradient steps + net-negative contamination-dominated reward guarantee under-convergence. An off-policy / minibatched learner (PPO/DQN) with many updates per env-step is the fair control.
5. **The 719a→724→732 chain is a healthy localization drill-down** (each resolves a fork the prior left open), NOT a re-derive loop — but 732a is now the *third* diagnostic routing to re-queue. If a properly-powered 732a still fails to resolve H1 vs H2, that recurrence itself becomes the signal (revisit whether the competence question is well-posed on this env), not another power bump.
