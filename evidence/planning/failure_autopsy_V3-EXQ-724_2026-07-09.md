# Failure Autopsy — V3-EXQ-724 (competence_deficit_diffuse)

**Generated:** 2026-07-09T21:23:45Z
**Scope:** single (diagnostic adjudication)
**Status:** confirmed (interactive gate answered)
**Target:** `v3_exq_724_competence_localization_diagnostic_20260709T211405Z_v3` · queue_id V3-EXQ-724 · `experiment_purpose=diagnostic` · `claim_ids=[]` · `evidence_direction=non_contributory`
**Parent:** `failure_autopsy_V3-EXQ-719a_2026-07-08` (first direct competence measurement; prescribed 724 as the brake-exempt competence-localization diagnostic)
**Context:** WS-1 of `evidence/planning/ree_ai_design_critique_plan.md` (capability floor before structure).

---

## 1. Facts (no interpretation)

724 is a one-factor-at-a-time (OFAT) localization anchored on the 719a incompetent config. Readiness gates all MET: a hand-coded greedy nearest-resource **oracle clears the 1.0 res/ep floor at 6.05** (env achievable), the **baseline reproduces incompetence** (0.25 < 1.0), and every cell logged ≥ 20 P2 episodes.

Per-arm P2 `mean_resources_per_episode` (floor = 1.0; seeds 42/43/44):

| Arm | Isolated factor | res/ep (seeds) | mean | reward | contam/ep |
|---|---|---|---|---|---|
| A0 baseline (719a all-ON, P1short, frozen) | reproduce incompetence | 0.0 / 0.0 / 0.75 | 0.25 | −0.88 | 9.8 |
| A1 P1long, frozen | (a) thin P1 training budget | 0.25 / 0.0 / 0.65 | 0.30 | −0.81 | 9.2 |
| A2 P1short, **encoder unfrozen** | (b) frozen world model | 0.20 / 0.0 / 0.45 | 0.22 | −0.88 | 9.9 |
| A3 **minimal** (gating stripped) | (c) all-ON mechanism interference | 0.20 / 0.0 / 0.20 | 0.13 | −0.78 | 6.7 |
| A4 recovery (minimal + P1long + unfrozen) | combined ceiling | 0.20 / 0.0 / 0.35 | 0.18 | −0.77 | 7.4 |

Load-bearing criterion `single_factor_arm_recovers_competence`: **FALSE**. `recovery_ceiling_supra_floor`: **FALSE** (A4 also sub-floor). Self-route: **`competence_deficit_diffuse`**. The agent *acts* — it commits to 5 distinct classes at ~1.4 nats entropy — but forages ≈0 resources and is contaminated 7–11×/episode. Not frozen; **uniformly incompetent action**.

## 2. The load-bearing structural fact (what 724 could not see)

Every arm shares **one invariant that 724 never varied**: the policy is learned **only through a thin `bias_head` REINFORCE** over representations trained for **prediction** (SD-056 e2 world-forward contrastive), not for **action**. Confirmed in the script: action learning is `bias_head` REINFORCE across all arms; A2/A4 toggle `requires_grad` on the *encoder* only; no arm adds a trainable policy/action head. A3 keeps the SP-CEM planner + z_goal/resource-proximity drives but removes the gating superstructure — and was the *worst* arm.

"Diffuse across {P1 budget, encoder freeze, mechanism count}" therefore reads most parsimoniously as: **the deficit lives in the un-varied constant** — the policy-learning mechanism itself (bias-head-only REINFORCE over prediction-only representations), not in any factor the OFAT design manipulated.

## 3. Claim-layer mapping

No claim tagged (`claim_ids=[]`, diagnostic). Bears on the `f_dominance_conversion_ceiling` competence gap that renders every committed-action DV undefined (the shared root of the 654h/485i/625e/460h/460i `substrate_not_ready` wall, per 719a). **Brake-exempt**: asks "why is the integrated agent incompetent at foraging," a different question than ARC-062/MECH-309 ("does committed action collapse to one class"). This autopsy tags no claim and recommends no lettered re-test — the re-derive brake does not apply and is not fired.

## 4. Biological-reference triage

Closest reference: a **learned sensorimotor policy** (dorsal-striatal RPE-driven action learning) over perceptual representations. REE trains rich *prediction* (e2 world-forward contrastive, encoder) but learns *action* only via a bias head. In brains, action learning is a substantial learning system, not a bias term on a prediction model. **Divergence (load-bearing):** REE's action-learning capacity is impoverished relative to its prediction-learning capacity — a translation gap, not (yet) a falsified mechanism. Lit status: partial (motor-learning / actor-critic grounding not pulled for this substrate).

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (intact) | diagnostic, no claim tested |
| Biological reference | partial / formal-import | prediction-rich, action-poor translation; dorsal-striatal action learning under-instantiated |
| Prerequisites | missing | no first-class policy-learning substrate (SD) exists |
| Implementation | **stub (prime suspect)** | bias-head-only REINFORCE is the shared, un-varied invariant |
| Environment | **unknown (untested)** | oracle wins via *privileged* nearest-resource access; whether the agent's *observation* affords resource localization is untested; contamination 7–11/ep hints obs/drives may not separate resource from hazard |
| Measurement | design gap | 724 blind to the shared invariant and to H2 (no learned non-REE control) |
| Integration | not the story | stripping gating (A3) was worst, not best — refutes "mechanisms suppress foraging" |
| Scale / capacity | likely insufficient | bias-head policy capacity + non-action-adapted representation |

**Recommended `epistemic_category`:** not `substrate_ceiling` in the un-measurable sense — a genuine **competence/implementation gap** with a concrete testable next cut. Manifest `evidence_direction=non_contributory` is correct for a diagnostic (promotes/demotes nothing).

## 6. The open fork this autopsy resolves next

- **H1** — the deficit is in **REE's action-generation stack** (bias-head policy over prediction-only representations; possibly also planner/drives). A real trainable policy head would recover competence.
- **H2** — the **env/observation interface is unlearnable by any policy** at this scale (the oracle only wins on privileged access the agent's observation may not afford). No policy substrate would help; the target is the observation encoding.

724 cannot distinguish these because it has no *learned* non-REE control and never varied the policy mechanism.

## 7. Routing — CONFIRMED: `/queue-experiment` (H1/H2 discriminator)

User scientific judgment at the interactive gate: **queue the discriminator before committing to any build** (matches 719a's "localize before build"; H2 is cheap to rule out and expensive to skip).

### Redesign spec — `policy_learning_discriminator` (new EXQ number; suggest ~V3-EXQ-727, `/queue-experiment` assigns the real id)

Different scientific question than the conversion-ceiling claims → **new number, brake-exempt, `claim_ids=[]`, `experiment_purpose=diagnostic`, `non_contributory`.**

- **Env:** identical to 724 (same `ENV_KWARGS`, seeds 42/43/44, steps/episode, P2 protocol). Keep the hand-coded oracle as the positive control.
- **Arms:**
  - **B0** — 724 A0 baseline (bias-head-only REINFORCE, all-ON). Incompetence anchor.
  - **B1 (H1 test)** — REE stack with a **full trainable policy/action head** (not bias-head-only) trained by REINFORCE/actor-critic, representation permitted to adapt for action (e.g. an action-value or policy head with its own optimizer). Everything else as B0.
  - **B2 (H2 test)** — **non-REE vanilla learned policy** (small PPO or DQN MLP) on the *identical observation vector*, no REE machinery. Comparable training budget.
- **Load-bearing DV:** P2 `mean_resources_per_episode` vs floor 1.0, majority of seeds.
- **Interpretation grid:**
  - **B2 clears ∧ B1 clears → H1 (policy-learning mechanism):** bias-head-only was the bottleneck → build a proper action/policy-learning substrate under `f_dominance_conversion_ceiling`.
  - **B2 clears ∧ B1 fails → deeper H1:** the REE stack *beyond* the policy head obstructs even a full head → narrow to planner/drives/gating; do not build the head alone.
  - **B2 fails (vanilla RL also sub-floor) → H2 (observation/env interface):** target is the observation encoding, **not** the policy — a policy-learning build would be wasted.
  - **B1 clears ∧ B2 fails → flag** (REE full-head beating vanilla RL on identical obs is implausible; check for leakage/privileged input).
- **Readiness gates** (reuse 724's): oracle clears floor; B0 reproduces incompetence; ≥ MIN_P2_EPISODES per cell.

### Draft `evidence_quality_note` (governance writes; do not write here)
> V3-EXQ-724 competence-localization diagnostic (non_contributory, promotes/demotes nothing). Diffuse across the three OFAT factors (P1 budget A1, encoder-freeze A2, mechanism count A3, and combined A4 — all sub-floor; oracle 6.05 clears the 1.0 floor). Autopsy (failure_autopsy_V3-EXQ-724_2026-07-09) localizes the deficit to the ONE invariant 724 never varied: bias-head-only REINFORCE policy learning over prediction-trained representations. Routed to /queue-experiment for a policy-learning discriminator (REE full-policy-head arm + non-REE vanilla-RL control on identical observation) to resolve H1 (REE action stack) vs H2 (observation interface unlearnable) BEFORE any competence-substrate build. Brake-exempt (different question, no claim tagged).

**No substrate_queue write yet** (`recommended_substrate_queue_entry.action = none`): the build target (policy-learning substrate vs observation encoding) is exactly what the discriminator decides. `f_dominance_conversion_ceiling` remains the parent SD once the discriminator lands.

## 8. Learning extracted

1. The competence deficit is **invariant to** training budget, encoder plasticity, and mechanism count (and their combination) — so it lives in the shared un-varied constant: **bias-head-only policy learning over prediction-only representations**.
2. REE's architecture is **prediction-rich, action-poor**: it trains a substantial world model but learns action via a bias head — a biological translation gap vs dorsal-striatal action learning.
3. The all-ON gating layer does **not** suppress foraging (A3 stripped it and got *worse*) — kills the "mechanisms veto action" hypothesis for this substrate.
4. 724's OFAT design had a **blind spot**: it varied everything except the policy-learning mechanism and included no learned non-REE control, so it could report "diffuse" without seeing the shared cause. Design lesson for future localization diagnostics: include a non-REE learned control and vary the learning mechanism, not just its inputs.
