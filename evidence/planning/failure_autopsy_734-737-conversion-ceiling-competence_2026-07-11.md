# Failure Autopsy (CLUSTER) — GOV-FANOUT-1 conversion-ceiling competence portfolio

- **Generated (UTC):** 2026-07-11T22:20:51Z
- **Scope:** cluster synthesis over 4 diagnostics (V3-EXQ-734/735/736/737) + cross-reference to the reviewed PASS V3-EXQ-738
- **bears_on:** `ree_ai_design_critique_plan:WS-1`, `f_dominance_conversion_ceiling`, `conversion_ceiling_campaign_plan:CAMPAIGN`
- **All targets:** `claim_ids=[]`, `experiment_purpose: diagnostic`, brake-exempt. PROMOTES/DEMOTES NOTHING; governance applies.
- **Status:** confirmed (user-adjudicated at the Step 8 gate 2026-07-11)

---

## 1. Why this is a cluster, and the recurrence it closes

The conversion-ceiling campaign (`conversion_ceiling_campaign_plan.md`) drove all four conversion faces (selection, de-commit, valuation, arbitration) to terminal, and they converged onto **one** upstream question — the **competence floor**: can the REE substrate forage at all (mean resources/ep vs a 1.0 floor)? The all-ON agent forages ~0, below the floor at which *any* gating/conversion structure is even measurable.

The first attempt to localize this was a **4-deep sequential chain** — `719a → 724 → 732 → 732a` — which GOV-DIAG-1 flagged at N=4 and `732a` pre-registered as terminal (refusing a `732b` same-question power-bump). The chain's last two legs were confounded (a global teleport oracle used as the learner-adequacy denominator vs a 5×5 local-view learner). Per **GOV-FANOUT-1 (WS-14)**, the sequential chain was replaced by a **diverse-axis portfolio**. This autopsy is the consumer-side adjudication of that portfolio's collective answer.

---

## 2. Facts — what each leg measured (no interpretation)

| Run | Axis | Self-route | Key numbers | Preconditions |
|---|---|---|---|---|
| **738** (PASS, x-ref) | measurement/observation | `local_view_achievable` | greedy 5×5 local-view forager: **6.05 @D0, 48.05 @D3** (floor 1.0); global oracle 57.2; random 0.93 | n/a (PASS anchor) |
| **734** | env difficulty | `ree_substrate_ceiling` | REE all-ON recovers at **no** rung; PPO control recovers at **D2**; oracle 6.04; baseline D0 0.088 | all met |
| **735** | drive/reward balance | `reward_balance_not_the_lever` | **no** approach-weighting arm supra-floor; oracle 6.05; control 0.17 | all met |
| **736** | curriculum | `substrate_not_ready_requeue` **[precondition_unmet]** | curriculum-premise gate `agent forages EASY` = **1.0 vs threshold 3.0 → FAILED**; hard/easy oracle clear floor | premise FAILED |
| **737** (load-bearing FAIL) | representation | `policy_learning_insufficient_or_deeper` | **D3 ppo_ree_latent = 0.217** (< random 0.267; < ppo_raw_obs 0.567); D3 oracle 57.2; bias-head 0.68 | all met |

**Which criterion failed:** every leg's *achievability / negative-control* precondition PASSES (oracle clears floor; local-view greedy clears floor; control reproduces incompetence) while every *discrimination* criterion FAILS. That "controls pass, discrimination fails across structurally-different axes" is the substrate-ceiling fingerprint — here **localized**, not diffuse.

---

## 3. Claim-layer map

No target tags a claim (`claim_ids=[]` throughout) — these are pure localization diagnostics, so nothing weighs against a claim directly. The synthesis instead **moves the candidate MECH-457** and reconciles the `conversion_ceiling_campaign_plan` / WS-1 nodes.

**MECH-457** (`action_learning_as_first_class_actor_critic_substrate`, candidate, v3_pending) carries an explicit gate: its promotion is *"gated on the V3-EXQ-737 H1 discriminator (a real trainable policy/actor head + value baseline over REE's frozen z_world recovering foraging competence above the 1.0 floor)."* **737 is that discriminator, and it FAILed.** This refutes the *frozen-latent + bolt-on actor* instantiation while leaving the *mechanism* (a first-class RPE actor-critic is missing) intact and, if anything, strengthened.

---

## 4. Biological-reference triage

- **Closest mechanism:** dorsal striatum as ACTOR, dissociable from a ventral-striatal value-prediction CRITIC (O'Doherty et al. 2004), taught by a dopaminergic reward-prediction-error signal (Schultz, Dayan & Montague 1997); D1/D2 opponent credit assignment as a later refinement (Collins & Frank 2014, OpAL).
- **Faithful translation vs formal import:** REE currently learns action only as a **thin bias_head REINFORCE readout** over a **prediction-trained** encoder (SD-056 e2 world-forward contrastive). Biologically, action learning is *a substantial dedicated learning system*, not a bias term on a world model. This is a **translation gap**, not a formal-import divergence — so the routing is a build, not a `/lit-pull` on a misimported formalism.
- **Missing-dependency signature:** the FAIL is exactly what you would expect if the dorsal-striatal actor / RPE-teacher subsystem were absent — the world model is rich (REE predicts well) but nothing converts prediction into competent action. That is a discovered prerequisite, not a falsification.

---

## 5. Four-layer diagnosis (cluster-dominant)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | strengthened (MECH-457) | 737 is MECH-457's own promotion-gate discriminator; its FAIL localizes the deficit to exactly the missing system MECH-457 names, and refines the build spec (no frozen latent). |
| Biological reference | clear | dorsal-striatal actor + value critic + dopaminergic RPE teacher; well-grounded, buildable. |
| Prerequisites | present | `depends_on` SD-056 (BUILT: e2 encoder) and MECH-229 (BUILT/provisional: VALENCE_WANTING) both in the V3 substrate → MECH-457 is buildable now, no probe gate. |
| Implementation completeness | absent | no dedicated action-learning system exists; only the bias_head readout. |
| Environment adequacy | adequate | 738: a trivial greedy policy forages 6–48× the floor from the 5×5 local view. The env is NOT the wall. |
| Measurement adequacy | adequate (fixed) | the global-oracle confound that broke 732a is retired; 738 supplies the local-view-achievable ceiling as the fair denominator. |
| Integration adequacy | coupled but action-inert | modules integrate (all-ON runs) but the integrated policy cannot act; a bolted-on actor on the frozen latent underperforms raw obs. |
| Scale / capacity | not the lever | 734 (difficulty), 735 (reward), and 737's raw-obs control at 1000 PPO episodes all fail to move it. |

**Recommended `epistemic_category`:** `competence_implementation_gap` (the 737 load-bearing leg); the difficulty/reward legs read `substrate_ceiling`; 736 is `substrate_not_ready_requeue` (vacuous).

---

## 6. Cluster pattern (load-bearing output)

**One structural property, not five bugs.** Each leg independently rules out an alternative lever, and they converge:

- NOT **observability** — 738 (greedy local-view forages 6–48× floor).
- NOT **difficulty** — 734 (no rung rescues REE's native stack).
- NOT **reward-balance** — 735 (no approach-weighting arm recovers).
- NOT **curriculum** — 736 vacuous (can't forage even the easy env).
- NOT **a missing readout head over the existing representation** — 737 (a real actor+critic on the **frozen** z_world scores *below random* and *below the same actor on raw pixels*).

**What remains:** the deficit is a **missing first-class action-learning system (MECH-457)** *and* the **action-inadequacy of the frozen prediction latent** (737: 0.217 < 0.567 — REE's z_world is a *worse* action substrate than raw obs). "Prediction-rich, action-poor" is now sharpened from "needs a policy head" to "needs a dedicated RPE actor-critic that **co-shapes** the representation."

**The one honest confound (surfaced, resolved at portfolio level).** In 737 `ppo_raw_obs` **also** stayed sub-floor (0.567 < 1.0), so 737 *alone* cannot separate "latent action-inadequacy" from "PPO-from-scratch too sample-inefficient in 1000 episodes." Resolution: 738 shows the env is trivially forageable by a hand-coded policy → the wall is action-**learning** sample-efficiency/credit-assignment, which *is* MECH-457's thesis; the latent<raw ordering adds action-adequacy on top. Both readings route to the **same build**, differing only on *how much* the encoder must co-adapt — folded into a **frozen-vs-co-trained-encoder ablation arm** inside the MECH-457 validation (user-directed).

---

## 7. Learning extracted

1. The campaign's competence floor localizes to a **missing action-learning system (MECH-457)** — not observation, difficulty, reward-balance, or curriculum.
2. REE's frozen prediction-trained z_world is a **strictly worse action substrate** than raw obs for a learned actor → latent **action-inadequacy**, not merely a missing head.
3. MECH-457's build spec is refined: the RPE actor-critic must **co-shape/augment** the representation, not ride a frozen latent.
4. The **GOV-FANOUT-1 portfolio worked as designed** — a diverse-axis fan-out resolved a 4-deep sequential discrimination the sequential chain could not.
5. 736's `precondition_unmet` is vacuous as a curriculum verdict but reinforces the floor.

---

## 8. Repair pathway / routing (user-confirmed 2026-07-11)

**Node classification:** `complicated (buildable)` — MECH-457 is named, biologically grounded, and both dependencies are built. The one open probe (does a bolt-on actor on the frozen latent suffice?) has been **answered** by 737 (no) → the node is buildable, not probe-gated.

- **PRIMARY → `/implement-substrate` MECH-457.** Build a first-class RPE-driven actor-critic action-learning substrate (dorsal-striatal actor + value-baseline critic), architecturally distinct from the bias_head REINFORCE. **Build spec (refined by 737):** the actor must NOT ride a frozen z_world; the action-learning loss co-shapes/augments the representation. Validation experiment **must** carry a **frozen-vs-co-trained-encoder ablation arm**. Success = all-ON agent forages above the 1.0 floor (majority of seeds) at D3, using the **local-view-achievable ceiling (738)** as the fair denominator, never the global teleport oracle. `substrate_queue` **action = create** (`sd_actor_critic_action_learning`, priority 1 — blocks the whole campaign + MECH-457 promotion). See the JSON `recommended_substrate_queue_entry`.
- **SECONDARY → convergence-demand intake (user-directed).** In parallel, commission a `REE_convergence` intake on external action-learning / representation-for-action frameworks (successor representations; world-model-with-action — Dreamer / MuZero action-value; decision-transformer; representation-learning-for-RL) to inform *how* to make the representation action-adequate — the exact gap 737 exposed. This de-risks the co-shaping design; it does **not** gate the build (the build proceeds in parallel).
- **REFUSED:** any further same-question competence-floor **lettered re-test** (no `737a` / `732b`-style re-pose). The discrimination is settled by the portfolio — the sanctioned next test is the **MECH-457 ON/OFF validation** (new EXQ, new claim MECH-457, different mechanism), not another letter circling the floor.

**Re-derive brake:** mechanically not fired (`claim_ids=[]` → claim-keyed counter 0), but the **autopsy-stream recurrence** (719a→724→732→732a→this) is now marked **RESOLVED_BY_FANOUT** with `refused_requeue: true`. This is not "stuck, stop spinning" — it is "the discrimination is settled, proceed to build, do not re-litigate."

**Draft `evidence_quality_note` (for governance to write on MECH-457 — do NOT write here):**
> Promotion-gate discriminator V3-EXQ-737 (trainable PPO actor+value head over frozen z_world) RAN and FAILED at D3 (0.217 res/ep, below the 1.0 floor and below both random and the same actor on raw obs). Combined with V3-EXQ-738 (greedy local-view forages 6–48× floor → obs is not the wall), 734 (difficulty), and 735 (reward-balance) — all non-recoveries — the conversion-ceiling competence floor localizes to MECH-457: a missing first-class RPE actor-critic action-learning system, and the frozen prediction latent is action-inadequate for a bolted-on actor. Refutes the "frozen latent + bolt-on head" instantiation; the mechanism stands. Build spec refined: the actor-critic must co-shape the representation (frozen-vs-co-trained ablation owed). Routed to /implement-substrate (substrate_queue: sd_actor_critic_action_learning) + a parallel convergence intake. Diagnostic, claim_ids=[]; PROMOTES/DEMOTES NOTHING here.

**Campaign-plan reconciliation (for governance):** annotate `conversion_ceiling_campaign_plan.md :CAMPAIGN` — WS-1 competence discrimination **RESOLVED** by the 734/735/736/737/738 portfolio → localized to the MECH-457 action-learning substrate; the conversion route of record (MECH-448 selection face) is upstream-blocked on this floor being lifted. Nodes stay `assembling` (build owed); no % credit for an unbuilt substrate.
