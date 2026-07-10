# Failure Autopsy — V3-EXQ-732a (power-fixed H1/H2 policy-learning discriminator; competence question NOT resolved — terminal signal)

**Generated:** 2026-07-10T11:53:40Z
**Scope:** single (diagnostic adjudication)
**Status:** confirmed (interactive gate answered)
**Target:** `v3_exq_732a_policy_learning_discriminator_20260710T103144Z_v3` · queue_id V3-EXQ-732a · `supersedes V3-EXQ-732` · `experiment_purpose=diagnostic` · `claim_ids=[]` · `evidence_direction=non_contributory` · machine `ree-cloud-4` (~3.6 h)
**Parent autopsy:** `failure_autopsy_V3-EXQ-732_2026-07-10` (REJECTED 732's H2 self-route as under-powered; prescribed the four power-fixes 732a implements). Chain: `failure_autopsy_V3-EXQ-719a_2026-07-08` → `_V3-EXQ-724_2026-07-09` → `_V3-EXQ-732_2026-07-10` → **this**.
**Context:** WS-1 of `evidence/planning/ree_ai_design_critique_plan.md` (capability floor before structure); `conversion_ceiling_campaign_plan.md`. MECH-455 (competence-based IM) is the WS-1 target mechanism.

---

## 1. Facts (no interpretation)

732a re-runs the H1/H2 discriminator with the four power-fixes 732's autopsy prescribed: (1) **PPO** minibatched learner at **2000 episodes** (~30x the 732 A2C update budget), applied to BOTH B1 and B2; (2) entropy 0.03 + count-based novelty; (3) explicit FORAGE_BONUS + running-std reward scaling + advantage normalization; (4) a **NEW learner-adequacy readiness gate** (L0 = the same vanilla PPO on a plain sanity env, must clear ≥ 0.5x the sanity oracle before a sub-floor B2 can read as H2). Env/seeds/oracle/B0/floor reused verbatim from 724 (`ENV_KWARGS` size-12, 5 resources, 4 hazards, reef-bipartite, seeds 42/43/44, 200 steps/ep, 20 P2 eps, floor 1.0 res/ep).

**Readiness gates — the NEW one FAILED; all others MET.**

| Gate | Measured | Threshold | Met |
|---|---|---|---|
| oracle_resource_channel_clears_floor (real env) | 6.05 (min) / 6.33 (mean) | ≥ 1.0 | ✓ |
| **learner_adequacy_on_sanity_env** | **0/3 seeds** (L0 0.7 res/ep vs sanity oracle 57.2; per-seed vs 28.6) | **majority (2/3)** | **✗** |
| baseline_reproduces_incompetence (B0) | 0.20 | < 1.0 | ✓ |
| sufficient_p2_episodes | 20 | ≥ 5 | ✓ |

`readiness_met=False → outcome FAIL, self-route (HYPOTHESIS) substrate_not_ready_requeue`; `non_degenerate=False`, `degeneracy_reason=learner_inadequate_on_sanity_env`.

**Per-arm P2 `mean_resources_per_episode` (floor 1.0; seeds 42/43/44):**

| Arm | Role | res/ep (seeds) | mean | reward | n_supra_floor |
|---|---|---|---|---|---|
| B0 REE bias-head REINFORCE all-ON | H0 anchor | 0.25 / 0.00 / 0.35 | **0.20** | −0.86 | 0/3 |
| B1 REE repr + full PPO head | H1 | **1.00** / 0.75 / 0.20 | **0.65** | −0.62 | **1/3** |
| B2 vanilla PPO raw obs (dim 398) | H2 | **0.95** / 0.00 / 0.00 | **0.32** | −0.31 | 0/3 |
| L0 vanilla PPO **sanity env** (dim 373) | adequacy | 0.25 / 0.55 / **1.30** | **0.70** | +1.15 | 1/3 vs 1.0 floor; **0/3 vs 28.6** |
| real-env oracle (privileged) | control | 6.75 / 6.20 / 6.05 | 6.33 | — | 3/3 |
| sanity-env oracle (privileged) | ref | 57.0 / 57.3 / 57.3 | 57.2 | — | — |

`b1_clears_floor=false`, `b2_clears_floor=false` (majority test). Load-bearing criterion `discriminator_resolved_nondegenerate` = **not passed**. The discriminator did NOT resolve H1 vs H2.

## 2. Verified mechanism — the observability asymmetry (the load-bearing structural fact)

The adequacy gate references `0.5 x sanity_oracle = 28.6 res/ep`. That oracle and the learner do **not** see the same world:

- **Learner observation is a 5×5 LOCAL view.** `causal_grid_world.py` `world_obs_dim`: `local_view` 5×5×7=175 + `contamination_view` 25 + `hazard_field_view` 25 + `resource_field_view` 25. On a 12×12 grid the agent sees a 25-cell window. `resource_field_view` (env lines 3029-3044) is a 5×5 slice of `resource_field`, a global distance-decaying gradient (`1/(1+0.5·d)`, `resource_field_decay=0.5`). The gradient is shallow enough to carry a *faint* directional signal toward off-window resources — so the observation is **not strictly blind** — but that signal is weak when far from all resources.
- **Oracle has PRIVILEGED GLOBAL access.** `_oracle_action` (724:570-581) reads `env.resources` — every resource coordinate — takes the global-nearest by Manhattan distance, steps optimally toward it, and retargets instantly on respawn (`resource_respawn_on_consume=True`). Zero exploration cost, no partial observability.

**Consequence:** no 5×5-local-view policy can reach 50% of a teleporting, globally-omniscient oracle. On the *trivial* sanity env (hazards/reef/contamination OFF) the local learner gets **0.7 vs the oracle's 57.2 — 1.2%.** The `28.6` threshold is structurally unreachable, and it is **28× the discriminator's own competence floor (1.0)** — on an *easier* env. **The `learner_adequate=False` degeneracy flag is therefore untrustworthy: the gate built to prevent 732's mis-read reproduces the 732/642 shape (a readiness precondition failing for a structural, not substantive, reason).**

## 3. Adjudication of the three competing reads

**(B) adequacy gate MIS-CALIBRATED — CONFIRMED, primary defect.** Per §2. The privileged-global reference cannot gate a local-view learner. `learner_inadequate_on_sanity_env` does not mean the learner is inadequate at the competence-relevant scale; it means the reference is on the wrong scale. Same failure class as V3-EXQ-642 (`precondition_unmet` from an ill-specified gate) and 732 (a readiness battery producing a spurious verdict).

**(A) learner genuinely fragile — PARTIAL support, and it matters.** Judged against a *fair* bar (the same 1.0 floor, not 28.6), L0 on the trivial sanity env clears on only **1/3** seeds (0.25 / 0.55 / 1.30). A PPO learner at ~30× the 732 update budget, with novelty exploration and reward shaping, *still* only near-clears on one sanity seed. So more power is demonstrably **not the lever** — fragility survived the 30× increase. This is why (i) another power bump is refused.

**(C) partial observability → H2 — real signal, does NOT license H2 (secondary; user-confirmed).** The 57→0.7 chasm on the trivial env implicates the local view as capping absolute *rate* far below a global agent. But at the scale the discriminator actually adjudicates — the **1.0 floor** — the observation is very nearly learnable: **B1 seed 42 = 1.00 (clears), B2 seed 42 = 0.95.** The barrier on seeds 43/44 is seed-variance/under-convergence (A), not a structural observation-encoding ceiling. C therefore does **not** license an observation-encoding build; it over-reads the privileged-oracle gap as an observation verdict. Recorded as a real but non-decisive signal.

## 4. The terminal signal (why this is not another power bump)

732's autopsy pre-registered exactly this recurrence: *"if a properly-powered 732a still fails to resolve H1 vs H2, THAT recurrence is the signal — is the competence question well-posed on this env — NOT another power bump."* That condition is now **met**. This is the **4th diagnostic (719a → 724 → 732 → 732a) bottoming out on the same competence floor**.

The deeper finding: the whole chain's operationalization — *local-view policy foraging-rate vs a global-privileged oracle on CausalGridWorldV2 (reef-bipartite)* — is **observability-confounded**. The metric conflates (policy competence) with (the structural local-view-vs-omniscient-oracle gap). The adequacy gate made the confound explicit by placing both on one axis and revealing the 57→0.7 chasm on even the trivial env. Four diagnostics have now paid down power/instrumentation without moving the question, because the question as posed is not cleanly answerable on this env with this reference.

**Re-derive brake:** the claim-keyed counter is **0** (claim_ids=[], so no claim accumulates `substrate_ceiling`/`non_contributory` autopsies — brake does not fire mechanically). But the **autopsy-stream recurrence** (4th diagnostic on the same floor, each resolving a prior fork yet none reaching a verdict) is the qualitative equivalent, and 732 pre-committed to honoring it. This autopsy therefore **refuses a same-question re-queue (V3-EXQ-732b)** in the brake's spirit.

## 5. Claim-layer mapping

No claim tagged (`claim_ids=[]`, diagnostic, `non_contributory` — **promotes/demotes nothing**, correctly excluded from scoring). Bears on the WS-1 competence floor and the `f_dominance_conversion_ceiling` competence gap; the H1/H2 build-direction fork remains open because the discriminator could not read. Brake-exempt at the claim level; the refusal of (i) comes from the autopsy-stream recurrence, not the claim counter.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (intact) | diagnostic, no claim tested |
| Biological reference | partial | learned local-view sensorimotor foraging vs an omniscient teleport oracle; the operative axis here is test-design/observability, not biology |
| Prerequisites | present | env solvable with privileged access (oracle 6.05); obs carries a faint global resource gradient |
| Implementation | adequate (power-fix landed) | PPO + 30× updates + exploration + reward hygiene all applied as prescribed |
| Environment | **confounded reference** | env solvable, but "solvable by a global oracle" ≠ "solvable by a local-view policy"; the two differ by ~50× on the trivial env |
| Measurement | **design gap (primary)** | adequacy reference is a privileged-global oracle (0.5×), structurally unreachable by any local-view policy and 28× the competence floor → spurious `not ready` |
| Integration | n/a | single-arm learners |
| Scale / capacity | insufficient AND non-monotone | learner fragile even at 30× budget on the trivial env (1/3 seeds) → power is not the remaining lever |

**Recommended reading:** `substrate_not_ready_requeue` is correct that no H1/H2 verdict is licensed — but the unmet precondition is **not** "learner too weak," it is **"the adequacy reference is observability-unfair"** (measurement/environment design gap), compounded by genuine learner fragility. NOT a substrate ceiling. `evidence_direction = non_contributory` is correct for a diagnostic.

## 7. Routing — CONFIRMED (user gate): (iii) pivot + (ii) fair reference. REFUSE (i). Handoff to /governance.

**REFUSED — (i) V3-EXQ-732b same-question power bump.** Forbidden by 732's pre-registration; power already shown non-load-bearing (L0 fragility survived a 30× update increase). A *different-question* probe with a fair reference (new EXQ number, not a 732-letter) is allowed only after the operationalization is fixed.

**PRIMARY — hand /governance a WS-1 re-operationalization decision** (two coupled corrections):

1. **(ii) Observability-fair reference.** Any future competence/adequacy gate must reference a **local-view-achievable ceiling** — a strong local-view learner's asymptote, or a local-view heuristic forager that also sees only the 5×5 window — NOT the global-privileged `_oracle_action`. The `0.5 × global-oracle` reference is structurally unreachable and must not gate any read. (The real-env oracle stays as a *floor-achievability* control only, never as a learner-adequacy denominator.)

2. **(iii) WS-1 target pivot.** The competence-floor question ("can the substrate act at all, independent of whether structure helps") should be re-posed so it is not observability-confounded. Either (a) give the floor-achievability control the *same* local-view the learner has (so "floor" means "reachable by a local-view policy"), or (b) select a competence probe whose achievable ceiling is defined by a local-view agent (WS-2's capability-yardstick V3-EXQ-727 is the natural home — it already reports foraging/survival/goal-reach against `random_walk`/`ree_p0warmup_allon`/`greedy_oracle`; make its adequacy bar local-view-fair). This is a plan-of-record decision for /governance + the user, NOT a same-question re-queue.

**No `substrate_queue` write** (`recommended_substrate_queue_entry.action = none`): neither H1 (action/policy substrate) nor H2 (observation encoding) is confirmed, so no substrate should be queued. The build target is exactly what a *fairly-operationalized* competence probe would decide — and that operationalization is the WS-1 decision above.

### Draft `evidence_quality_note` (governance writes; do not write here)
> V3-EXQ-732a power-fixed policy-learning discriminator (diagnostic, claim_ids=[], non_contributory — promotes/demotes nothing; supersedes V3-EXQ-732). Applied all four 732-autopsy power-fixes (PPO 2000ep ~30x updates on B1+B2; entropy 0.03 + novelty; forage-bonus + reward-std scaling; a learner-adequacy gate). Self-routed `substrate_not_ready_requeue` because the NEW learner-adequacy gate failed (L0 vanilla PPO on the trivial sanity env = 0.7 res/ep, 0/3 seeds ≥ the 0.5×sanity-oracle=28.6 threshold). Autopsy `failure_autopsy_V3-EXQ-732a_2026-07-10` finds the gate MIS-CALIBRATED: its reference is the PRIVILEGED-GLOBAL oracle (`_oracle_action` reads all resource coords + teleport-beelines) while the learner sees only a 5×5 LOCAL view — no local-view policy can reach 50% of a global-omniscient oracle, and 28.6 is 28× the discriminator's own 1.0 competence floor on an EASIER env. Learner is also genuinely fragile (clears the 1.0 floor on only 1/3 sanity seeds even at 30× budget), so more power is not the lever. Read that partial-observability leans H2 is recorded as secondary/non-licensing (B1 & B2 both ≈1.0 on seed 42 → the 1.0 floor is near-reachable; not a structural observation ceiling). This is the 4th diagnostic (719a→724→732→732a) bottoming out on the same observability-confounded competence floor; 732's autopsy pre-registered THIS recurrence as the terminal signal (NOT another power bump). REFUSES a V3-EXQ-732b same-question re-queue. Routed to /governance for a WS-1 re-operationalization: (ii) replace the adequacy reference with a local-view-achievable ceiling (never the global oracle), and (iii) re-pose the competence-floor probe so it is not observability-confounded (give the floor control the learner's 5×5 view, or move the adequacy bar into WS-2's V3-EXQ-727 yardstick). No substrate_queue write (recommended_substrate_queue_entry.action=none) — no H1/H2 target confirmed. Brake-exempt at the claim level (claim_ids=[]); refusal of (i) comes from the autopsy-stream recurrence.

## 8. Learning extracted

1. **A readiness gate is only as fair as its reference frame.** 732's autopsy added a learner-adequacy gate to fix the 732 mis-read — but referenced it to the *privileged-global* oracle, so the gate itself became the new spurious precondition (642/732 shape one level deeper). A local-view learner must be judged against a local-view-achievable ceiling, never an omniscient oracle.
2. **"Oracle clears the floor" proves ENV-achievability, not OBSERVATION-achievability.** The real-env oracle (6.05) and sanity oracle (57.2) both forage with global access; the 57→0.7 gap on the *trivial* env shows how much of "achievability" is privileged access, not policy skill. Floor-achievability controls and learner-adequacy references are different instruments and must not share the same (privileged) denominator.
3. **When power is bumped and the result does not move, power was not the lever.** L0 stayed fragile (1/3 seeds on the trivial env) through a 30× update increase. A 5th power bump is predictably futile; the recurrence itself is the signal.
4. **A diagnostic chain that keeps resolving sub-forks without reaching a verdict is telling you the question is mis-posed, not under-powered.** 719a→724→732→732a each closed a prior fork (un-varied invariant → localization → power → adequacy reference) yet none reached H1 vs H2, because the operationalization (local-view rate vs global oracle) is observability-confounded. The fix is to re-pose the question, not to re-run it harder.
5. **The re-derive brake's claim-keyed counter has a blind spot for `claim_ids=[]` diagnostics.** A pure-diagnostic chain circling the same substrate floor accumulates zero on the claim counter, so the mechanical brake never fires — the recurrence lives in the *autopsy stream*, caught only by a human reading the chain. Worth considering an autopsy-stream recurrence counter (keyed on `bears_on` / plan work-stream) as a diagnostic-side analog.
