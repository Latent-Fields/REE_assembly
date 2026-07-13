# Failure Autopsy — Morning-Digest batch (742 / 744a / 745 / 746 / 746a)

- **Generated (UTC):** 2026-07-13T05:22:21Z
- **Scope:** batch of 5 independent targets (one load-bearing weakens + four supporting adjudications). Not a single convergent cluster — but 742 sits on the recurring foraging-competence wall (724 → 732/732a → 734-737 → 742) and its result *refutes* the 734-737 autopsy's "single missing mechanism = MECH-457" conclusion.
- **Status:** confirmed (interactive gate answered 2026-07-13).
- **Skill:** `/failure-autopsy`. Analysis + handoff only; no claims.yaml / manifest / review_tracker / substrate_queue edits. `/governance` applies.

---

## ① V3-EXQ-742 — MECH-457 — WEAKENS (the load-bearing target)

**Run:** `v3_exq_742_mech457_actor_critic_onoff_20260713T032215Z_v3` · machine `ree-cloud-2` · FAIL · `non_degenerate:true` · self-route `deeper_than_action_learning`.

### Facts (no interpretation)
MECH-457 ON/OFF validation of the first-class RPE actor-critic substrate (`ree_core/action_learning/actor_critic.py`, built 2026-07-12). 8 arms × 2 rungs (D0 724-baseline, D3 hazard-free) × 3 seeds [42,43,44]. Load-bearing DV: D3 actor-critic foraging competence (mean resources/ep, unshaped) vs the 1.0 floor; **MECH-457 supported iff an actor-critic arm clears while `bias_head_baseline` does not.**

D3 results (resources/ep):

| Arm | D3 forage | vs 1.0 floor |
|---|---|---|
| actor_critic_frozen_plain (A0) | 0.20 | sub-floor |
| actor_critic_cotrain_plain (A1) | 0.233 | sub-floor |
| actor_critic_frozen_sf (A2) | 0.267 | sub-floor |
| actor_critic_cotrain_sf (A3) | 0.217 | sub-floor |
| bias_head_baseline (incompetence control) | 0.75 | sub-floor |
| random_walk (floor anchor) | 0.933 | — |
| local_view_greedy (738 fair 5×5-view denominator) | **48.05** | 48× floor |
| greedy_oracle (global anchor) | 57.2 | — |

**Every actor-critic arm forages *below random_walk*.** Normalized to the local-view ceiling the cotrain arm reaches `0.004856` of achievable. Train/eval collapse: train forage recent ~1.19 → eval 0.20 (divergence −0.99) — the policy barely learns to forage even in training (1.2 vs 48 achievable) and what it learns doesn't transfer.

**Readiness — all preconditions MET** (contrast premise holds): D0/D3 `greedy_oracle` clears floor (6.33 / 57.2), D0/D3 `local_view_greedy` clears floor (6.05 / 48.05), `bias_head_baseline` reproduces incompetence at D0 (0.117 < 1.0). So the env is solvable, the raw 5×5 view is sufficient, and the incompetence deficit is present — the ON/OFF read is licensed.

**Failed criterion:** discrimination (no actor-critic arm clears; achievability + control preconditions all pass — the substrate-ceiling *fingerprint*, but see below: this is NOT an env/substrate-wiring ceiling because the raw obs IS sufficient).

**Recording gap (footnote, non-blocking):** manifest lacks top-level `substrate_hash`, `seeds`, `elapsed_seconds`, `recording_schema` (seeds present in `.config`). Not adjudication-blocking (clean 8-arm behavioural read), but a re-run should stamp `manifest_core.stamp_recording_core(...)` per the Experimental Recording Standard so the substrate the arms executed against is confirmable.

### Claim-layer mapping
MECH-457 (candidate, v3_pending): *"Competent action learning REQUIRES a dedicated RPE-driven actor-critic substrate (dorsal-striatal actor + value-baseline critic), distinct from the thin bias_head REINFORCE readout."* depends_on SD-056 (built), MECH-229 (built).

The test let the claim express itself (substrate built, bit-identical OFF, smoke pass; all readiness gates met). What 742 refutes is the **operational / sufficiency reading** the conversion-ceiling campaign ran on — that MECH-457 is *the* competence lever and building it clears the floor. The **necessity** claim is NOT falsified: the actor-critic may still be necessary but not sufficient, gated on an action-adequate input representation and a bootstrappable teaching signal.

Decisive lineage context: the **734-737 conversion-ceiling autopsy** (`failure_autopsy_734-737-conversion-ceiling-competence_2026-07-11`) concluded the wall was *"a single missing mechanism (MECH-457) … five independent non-recoveries each rule out an alternative lever"*, AND flagged as part of the structural property that *"its prediction-trained latent is action-inadequate."* 742 built the predicted fix and it did not fix the wall — so the "single missing mechanism" model is refuted, and the surviving half of that same structural property (**prediction-trained latent is action-inadequate**) is now the leading hypothesis.

### Biological-reference triage
Closest mechanism: dorsal striatum as ACTOR, dissociable from ventral-striatal value CRITIC (O'Doherty 2004), taught by a dopaminergic RPE (Schultz 1997); ML form = actor-critic / policy-gradient with value baseline (Sutton 2000). This is a **faithful biological translation**, not a formal-definition import — the mechanism CLASS has a strong existence proof. But the biological actor depends on: (a) **action-adequate cortical input** (topographic sensorimotor representation), (b) a **dense/shaped RPE teacher**, (c) **developmental scaffolding** (innate approach + curriculum; animals don't learn foraging tabula rasa from sparse reward). 742 provides none: the actor reads the *prediction-trained* `z_world` (not action-adequate), the foraging reward is *sparse and unshaped*, and there is no BC/curriculum warmup. **The FAIL matches what would happen biologically if the actor's input representation and teaching signal were inadequate — a discovered-prerequisite reading, NOT a falsification of the actor-critic mechanism class.**

### Four-layer diagnosis
| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened | "MECH-457 is THE lever / sufficient" refuted; necessity intact |
| Biological reference | clear | faithful translation; brain dependencies (adequate input, shaped RPE, scaffolding) absent |
| Prerequisites | missing | action-adequate input representation and/or bootstrappable teaching signal |
| Implementation completeness | complete | substrate built, trains (train forage moves to ~1.2) — not an impl bug |
| Environment adequacy | adequate | local_view_greedy clears floor at 48; env solvable |
| Measurement adequacy | adequate | 738 fair local-view denominator; readiness gates met (recording-gap footnote aside) |
| Integration adequacy | coupled-but-fails | the `z_world` → policy interface is the suspect seam |
| Scale / capacity | possibly insufficient | 1000 eps; but train forage plateaus at ~1.2, so budget is not the sole story |

**Dominant diagnosis:** a **discrimination bottleneck** between two "deeper-than-action-learning" hypotheses, both upstream of the actor-critic head. Recommended `epistemic_category`: `competence_implementation_gap` (the mechanism REE needs for competence is still missing — but it is upstream of MECH-457, not MECH-457 itself). Recommended `evidence_direction`: **weakens**.

### GOV-FANOUT-1 — discrimination portfolio (user-confirmed)
This is a discrimination, not a single named build → fan out a diverse portfolio, each leg on a different design axis with a declared null. **REFUSE a same-question floor re-pose** (737a/732b-style) — the 734/737 RESOLVED_BY_FANOUT refusal stands and the 742 script pre-registered this refusal.

- **H-rep (representation/observation axis).** Train the actor-critic head directly on the **raw 5×5 `resource_field_view`** (bypass `z_world` entirely — the exact input `local_view_greedy` uses). *Null:* if it clears the 1.0 floor, the prediction-trained `z_world` is action-inadequate — the encoder→policy interface is the wall (build an action-adequate encoder/observation path). If it ALSO fails, an adequate input still can't be learned from → points to H-explore/optimization.
- **H-explore (drive/reward axis).** Keep `z_world` as input but replace the sparse foraging reward with **distance-to-nearest-resource shaping** OR a **behavior-cloning warmup from `local_view_greedy`**. *Null:* if it clears, reward-sparsity/exploration was the wall (policy-gradient could not bootstrap from sparse foraging RPE — train forage never left ~1.2). If it fails, sparsity is not the (sole) wall.
- (Optional H-optim, algorithm axis — only if both above are ambiguous: PPO + entropy bonus / GAE tuning on the raw-view input. Not part of the minimal portfolio.)

Each leg is a **different mechanism** (encoder interface / reward density), not a power-bump of the braked floor design → GOV-FANOUT-1 compliant; `/queue-experiment` Step 2.5b design-audits coverage + verdict-aliasing before queuing.

**Re-derive brake:** does NOT fire — this is the **first** autopsy tagging MECH-457 (0 prior substrate_ceiling/non_contributory autopsies for MECH-457).

### Draft `evidence_quality_note` (governance to write, verbatim)
> V3-EXQ-742 (2026-07-13, evidence, ON/OFF validation) WEAKENS the sufficiency reading: the first-class RPE actor-critic substrate (all 4 arms: frozen/cotrain × plain/SF) forages 0.20–0.27/ep at D3 — below random_walk (0.93) and 0.5% of the local_view_greedy ceiling (48.05) — while every readiness precondition holds (oracle + local-view clear the floor, bias_head reproduces incompetence). Necessity NOT falsified; the deficit sits UPSTREAM of action-learning credit-assignment. Refutes the 734-737 autopsy's "single missing mechanism = MECH-457" conclusion; the surviving structural-property half ("prediction-trained z_world is action-inadequate") is the leading hypothesis. Routed to GOV-FANOUT-1: H-rep (actor on raw 5×5 view) vs H-explore (reward-shaping / BC-warmup). Same-question floor re-pose REFUSED. MECH-457 stays candidate/v3_pending.

---

## ② V3-EXQ-744a — INV-088 — WEAKENS

**Run:** `v3_exq_744a_inv088_world_goal_evaluator_dv_coupling_20260712T144028Z_v3` · FAIL · `non_degenerate:true` · `substrate_hash` present · 8 seeds.

**Facts.** Higher-seed (3→8) re-estimate of 744's inconclusive, EXTENDS (does not supersede) 744. Preconditions met (PC_iv_moved / PC_dv_decodable / PC_target_var all true). `mean_delta_r2` fell 0.232 (744) → **0.130** (below the 0.15 floor AND the 2×SD=0.278 effect-size gate); C2 monotone fails (ρ 0.687 < 0.8); C3 noise-fit floor passes. Per-seed Δr² highly variable (0.42, 0.19, 0.31 … alongside 0.015, −0.009). `benefit_corroborates:false`.

**Claim.** INV-088 (candidate, emergent from ARC-001/003/019): *E3's z_world-reading evaluator quality is strictly bounded by z_world differentiation.* The DV-coupling test manipulates differentiation (IV moved) and measures evaluator-quality gain.

**Diagnosis.** Met-precondition C1/C2 FAIL = genuine **weakens**. NOT a substrate ceiling (preconditions met, target has variance). The coupling is **real-but-weak / high-variance** — present (mean 0.130 > 0; several strongly-positive seeds) but below the pre-registered effect-size floor with intrinsically high per-seed CV. This is the definitive higher-n read the 744 inconclusive was waiting for: it weakens the STRONG "strictly bounded / quality gain tracks differentiation" reading; it does not demote INV-088 by itself (candidate status). Biology: an emergent representation-quality bound; the evaluator head evidently has enough capacity to noise-fit even poorly-differentiated z_world, so the bound is loose rather than tight.

**Routing:** `/governance` — record weakens, first weighted entry for INV-088 (744 was inconclusive/not weighted).

**Draft note:** *V3-EXQ-744a (2026-07-12, 8-seed re-estimate of the 744 inconclusive, EXTENDS 744) WEAKENS the strong bound reading: mean_delta_r2=0.130 fails the 0.15 floor and the 2×SD effect-size gate with preconditions met; monotone C2 fails (ρ=0.69). The world/goal-evaluator↔z_world-differentiation coupling is real-but-weak and high-variance, not a clean threshold effect. First weighted entry for INV-088; stays candidate.*

---

## ③ V3-EXQ-746 — INV-089 — STARVED / SUPERSEDED (scoring-exclude)

**Run:** `v3_exq_746_inv089_harm_eval_z_harm_calibrated_bound_20260712T142637Z_v3` · FAIL · **`non_degenerate:false`** · `evidence_direction:"unknown"` · superseded by 746a.

**Facts.** `preconditions_met:false` — z_harm differentiation gradient did not move (mean IV Δ −0.184 ≤ 0; rank ρ −0.150 ≤ 0) and the state target was not decodable-in-principle from mature z_harm (decode r² −0.196 < 0.05). DV blew up numerically (seed-3 −6.3e7, seed-47 −5.79) — the sparse single-cell target + un-clipped DV head produced non-finite excursions.

**Diagnosis.** STARVED bound test (bound never got off the ground — IV inert + DV undecodable + numerical blow-up), NOT a falsification. Correctly superseded by 746a (which fixes: denser primary target, raw-std precondition, gradient-clipped DV head). Route: **`/governance` marks it `evidence_direction: superseded`** so the indexer scoring-excludes it (does not weight toward INV-089 confidence/conflict).

**Routing:** `/governance` (supersession bookkeeping; no claim weight).

---

## ④ V3-EXQ-746a — INV-089 — WEAKENS

**Run:** `v3_exq_746a_inv089_harm_eval_z_harm_calibrated_bound_v2_20260712T170011Z_v3` · FAIL · `non_degenerate:true` · `supersedes:V3-EXQ-746` · `extends:V3-EXQ-743` · primary_target `dens`.

**Facts.** Corrected calibrated bound. Primary target = local neighbourhood density (dense → high raw variance). Preconditions met (IV Δ +0.032, IV-mature decode 0.398, target var). Load-bearing C1/C2/C3 all FAIL: `C1_dv_monotone` false (mean_dv_rho −0.525 vs ≥0.8), `C2_bound_coupling` false (mean_couple_rho −0.075 vs ≥0.8), `C3_dv_reliable` false; `mean_dv_delta` −34.5 (bound did not rise/track maturation). Secondary targets (at_agent, next_step) starved (preconditions unmet), non-gating.

**Claim.** INV-089 (provisional, promoted on 743's positive control): *harm_eval_z_harm quality is strictly bounded by z_harm differentiation, a maturation trajectory distinct from z_world's.*

**Diagnosis.** Met-precondition C1/C2/C3 FAIL = genuine **weakens**. First weighted *bound-test* entry for INV-089 (743 was the positive control that promoted candidate→provisional; this is the first evidence that harm_eval quality does NOT track z_harm differentiation on a met-precondition dense target). NOT a substrate ceiling; NOT a demotion by itself, but it directly pressures the "strictly bounded" reading. The author's `re_derive_brake` note is honoured (INV-089 substrate_ceiling autopsies: 0; z_harm observable, not a z_world-decode 740b confound).

**Routing:** `/governance` — record weakens for INV-089; pair with the 746 supersession.

**Draft note:** *V3-EXQ-746a (2026-07-12, corrected calibrated bound, SUPERSEDES starved 746, EXTENDS 743) WEAKENS: on the met-precondition dense target the harm_eval_z_harm quality bound does not rise monotonically (C1 ρ=−0.53) or track z_harm differentiation (C2 couple ρ=−0.08); mean_dv_delta=−34.5. First met-precondition bound-test evidence against the strict-bound reading; INV-089 stays provisional pending governance weigh-in.*

---

## ⑤ V3-EXQ-745 — MECH-456 — NON_CONTRIBUTORY (brake NOT fired — threshold raised)

**Run:** `v3_exq_745_rebinding_ecological_patchflip_20260712T162519Z_v3` · FAIL · `non_degenerate:true` · self-route `substrate_not_ready_requeue`.

**Facts.** World-driven patch-set-flip test-bed with an ecological behavioural DV on the policy-coupled `couple()` path. Readiness gate UNMET: the `couple()` perturbation is behaviourally inert — disabling the binding does not move foraging (the load-bearing positive control `couple_authority` below floor), and/or min_overtakes 0<8 / a config never visited / oracle below achievability. Per the V3-EXQ-478 precedent, a null ON-vs-FROZEN DV2 on a couple-inert substrate is `substrate_ceiling`, NOT a rebinding refutation → declared null, non_contributory, not weighted.

**Claim.** MECH-456 (provisional, epistemic_category substrate_conditional): *entity binding is continuously re-evaluated (rebinding), the entity-layer analogue of MECH-269(b) anchor-reset.* Substrate BUILT + converged (`cross_stream_binding_substrate`, `rebinding-harness-p0-coverage-decoupling`). The gap 745 surfaces: no substrate entry gives the `couple()` path **behavioural (foraging) authority** — the binder is measurable (DV1 affinity tracks config above shuffle) but behaviourally inert.

**Re-derive brake — evaluated, NOT fired (user decision 2026-07-13).** MECH-456 now has 3 substrate-limited autopsies (733, 733a survival-onboarding axis; 745 world-flip / ecological couple-path axis). The default threshold (2) is crossed, but the user **raised `RE_DERIVE_BRAKE_THRESHOLD` for MECH-456 to 3**, accepting the 745 author's argument that this is a genuinely different measurement axis (not a re-run of the braked survival-onboarding axis) and the substrate is being legitimately explored across axes. So 745 routes as **plain non_contributory** with no brake fire and no forced implement-substrate / re-test refusal. **The next MECH-456 substrate-limited autopsy (4th, any axis) fires the brake** — record kept so the standing scan (`check_granularity_debt_recurrence.py`) sees the raised threshold.

**Routing:** `/governance` records non_contributory (not weighted). A re-queue is *permitted* (brake not fired) but MUST target a substrate whose `couple()` path carries foraging authority — else it re-hits this exact couple-inert wall. Advisory only; not a forced implement-substrate this cycle.

---

## Summary table

| Target | Claim | Direction | Dominant diagnosis | Routing |
|---|---|---|---|---|
| 742 | MECH-457 | weakens | competence_implementation_gap (upstream of actor-critic) | GOV-FANOUT-1 (H-rep raw-view / H-explore reward-shaping); refuse floor re-pose |
| 744a | INV-088 | weakens | real-but-weak coupling below effect-size floor | governance (first weighted entry) |
| 746 | INV-089 | superseded | starved bound (preconditions unmet + numerical blow-up) | governance (scoring-exclude, superseded by 746a) |
| 746a | INV-089 | weakens | met-precondition bound C1/C2/C3 fail | governance (first bound-test weakens) |
| 745 | MECH-456 | non_contributory | couple-inert substrate (readiness gate unmet) | governance (non_contributory); brake NOT fired (threshold→3); re-queue must give couple() foraging authority |
