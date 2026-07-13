# Failure Autopsy — MECH-457 GOV-FANOUT-1 discrimination portfolio (V3-EXQ-747 / 748 / 749)

- **Generated (UTC):** 2026-07-13T18:33:20Z
- **Scope:** cluster (3-leg discrimination portfolio)
- **Status:** confirmed (user-adjudicated, interactive gate)
- **Claim:** MECH-457 (`action_learning_as_first_class_actor_critic_substrate`) — candidate / v3_pending
- **Fans out from:** `failure_autopsy_morning-digest-742-744a-745-746-746a_2026-07-13.json` (target V3-EXQ-742)
- **Routing (confirmed):** `/lit-pull` (developmental scaffolding / observational action acquisition / exploration under sparse reward), with the H-optim leg preserved as the next discrimination.

---

## 1. Facts — the full portfolio matrix

D3 forage/episode. Floor = 1.0. Denominators: `local_view_greedy = 48.05`, `greedy_oracle = 57.2`, `random_walk = 0.933`. All three legs `experiment_purpose: diagnostic`, `claim_ids: [MECH-457]`, and carry the always-core recording (top-level `substrate_hash`, `seeds [42,43,44]`, `recording_schema rec/v1`, `elapsed_seconds`, `machine_class linux-x86_64-py3.10`) — the 742 recording debt is fixed.

| Input \ Teacher | sparse | dense **shaping** (potential-based) | dense **BC** (imitate `local_view_greedy`) |
|---|---|---|---|
| **z_world** | 742: 0.20–0.27 FAIL *(cited, not re-run)* | 748: **0.217 FAIL** (per-seed 0.30/0.20/0.15) | 748: **32.72 PASS** (per-seed 35.85/39.70/22.60; action-match acc 0.802) |
| **raw 5×5 view** | 747: **0.217 FAIL** (per-seed 0.25/0.15/0.25) | 749: **0.767 FAIL** (per-seed 0.45/1.30/0.55) | 749: **20.93 PASS** (per-seed 17.75/26.15/18.90; action-match acc 0.872) |

Per-leg self-routed labels (hypotheses, not verdicts):
- **747** (`FAIL`): `rawview_sparse_insufficient`
- **748** (`PASS`): `dense_teacher_on_zworld_clears_sparsity_was_the_wall`
- **749** (`PASS`): `conjunction_clears_need_adequate_input_and_dense_teacher`

Every leg's readiness preconditions held (`local_view_greedy` and `oracle` both clear the 1.0 floor at D3; criteria non-degenerate). No crash — all ran to completion.

## 2. What the portfolio discriminated

- **H-rep REFUTED** ("prediction-trained z_world is action-inadequate / discards action-relevant geometry"). Two independent refutations: (i) raw view under sparse reward (747: 0.217) ≈ z_world under sparse (742: 0.20–0.27) — the richer input does not help; (ii) under BC, **z_world (32.72) beats the raw view (20.93)**. Once the RL bottleneck is removed, z_world is a fine — indeed better — control substrate.
- **"Reward density was the wall" REFUTED.** Potential-based dense **shaping** fails on *both* representations (0.217, 0.767 — both sub-floor). A denser *scalar* reward does not rescue policy-gradient in-budget.
- **Verdict-aliasing corrected.** 748's self-route `..._clears_sparsity_was_the_wall` conflates two distinct causes because it groups shaping+BC under "dense teacher": (a) "reward sparsity was the wall" (FALSE — shaping failed on both inputs) vs (b) "the RL exploration/credit-assignment loop is the wall, and only an expert's *action-level* targets bypass it" (TRUE — only BC passed). The load-bearing reading is (b).
- **Discriminated cause:** the actor-critic RL **cannot bootstrap** competent foraging in-budget on either representation, even with dense shaping. Only **behavior-cloning** — supervised imitation of an expert, which sidesteps RL exploration entirely — clears the floor. The wall is **learning-signal / exploration**, not input representation and not reward density.

## 3. Claim-layer map

MECH-457 is the action-**learning machinery** (how action is learned at all), not the drive (MECH-455) and not action decomposition (SD-004/ARC-021/SD-045). The portfolio does **not** falsify it: given an adequate action-level teaching signal (BC), the substrate produces competent — even superior — control. Sufficiency stays refuted (742); the newly-refuted sub-hypothesis is that *representation* is the fix. The machinery is **functional-when-taught**. MECH-457 stays `candidate` / `v3_pending`; `epistemic_category` unchanged; sufficiency `weakens`, with an added *strengthened-dependency* finding.

## 4. Biological-reference triage (load-bearing: dependency strengthened, not falsification)

Closest mechanism: dorsal striatum = actor, ventral = critic, dopaminergic RPE teacher (O'Doherty 2004; Schultz 1997; Sutton 2000). Faithful class translation. The 742 autopsy named three stripped dependencies; the portfolio refines each:

| Biological dependency | Portfolio verdict |
|---|---|
| (1) action-adequate cortical input | **Not the wall** — refuted; z_world under BC > raw view |
| (2) dense/shaped RPE teaching signal | **Refined** — a denser *scalar* reward is insufficient (shaping failed); an *action-level* teaching target (BC) is what works |
| (3) developmental scaffolding (innate approach + curriculum + imitation) | **Strengthened** — BC is the ML analog of observational/scaffolded action acquisition, and it is the arm that clears the floor |

So the FAIL of the sparse/shaped arms **plus** the PASS of the BC arms is *positive evidence* for a bootstrappable **action-level teaching signal / developmental scaffold** as a dependency of action-learning. This is a positive-negative result, contributory and informative — **not** non-contributory, **not** substrate_ceiling.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact-but-refined | sufficiency refuted (742); representation-inadequacy sub-hypothesis refuted here; machinery functional-when-taught |
| Biological reference | clear | faithful translation; failure = stripped-dependency signature (no innate approach / curriculum / imitation; sparse reward) |
| Prerequisites | missing | bootstrappable action-level teaching signal (imitation warmup / curriculum / innate approach prior). `depends_on` SD-056, MECH-229 present |
| Implementation | complete | substrate built; BC arm demonstrates it learns competent control |
| Environment | adequate | env solvable (oracle 57.2, local_view_greedy 48.05); both representations learnable under BC |
| Measurement | adequate | 742 recording debt fixed — all three legs carry the always-core |
| Integration | z_world->policy interface NOT the wall | the RL-bootstrapping/exploration loop is |
| Scale | budget not the sole story | BC clears in the same budget — it is the learning signal, not compute |

**Recommended `epistemic_category`:** `competence_implementation_gap` (unchanged from 742), with the cause now discriminated: a missing **bootstrappable teaching signal / developmental scaffold** — NOT input representation (refuted) and NOT reward density (refuted).

## 6. Cluster read

Shape: a 2×3 (representation × teacher) grid where FAIL/PASS splits **cleanly on the teacher axis, not the representation axis** — both representations fail under sparse and shaping, both pass under BC. This is **one structural property**, not three independent results: *unsupervised policy-gradient RL cannot bootstrap this task in-budget; supervised imitation can, on either input.* That convergence across representations is the load-bearing signal.

## 7. Learning extracted

1. H-rep ("prediction-trained z_world is action-inadequate") is **refuted**: z_world under BC (32.72) beats the raw 5×5 view (20.93); raw view under sparse ≈ z_world under sparse.
2. "Reward density is the wall" is **refuted**: potential-based dense shaping fails sub-floor on both representations. Only an *action-level* teaching target (BC) clears the floor.
3. The discriminated cause is the **RL exploration / credit-assignment bootstrap** — only imitation bypasses it. This *strengthens* the dependency reading (action-learning needs a bootstrappable teaching signal / developmental scaffold), consistent with the biology.
4. One live discrimination remains, on the **algorithm axis** neither leg isolated: is an expert teacher **necessary**, or is vanilla policy-gradient exploration merely too weak — would a stronger *unsupervised* explorer (PPO+entropy / intrinsic motivation) clear it without an oracle to clone? This decides the build target (better-explorer vs imitation/curriculum scaffold).

## 8. Routing (user-confirmed at the interactive gate)

**`/lit-pull` first.** Ground the literature on (a) developmental scaffolding / observational (imitation) action acquisition in dorsal-striatal control, and (b) exploration under sparse reward (intrinsic motivation / entropy-regularized policy gradient / count-based exploration), to decide whether the owed build is a **better unsupervised explorer** or an **imitation/curriculum scaffold** *before* committing compute. The H-optim leg (stronger unsupervised exploration, no expert) is the empirical discrimination the lit should inform — queue it after the lit-pull lands, not before.

- **No substrate entry named this cycle** (`recommended_substrate_queue_entry.action: none`): the build target (better-explorer vs scaffold) is exactly what the lit-pull + H-optim leg must decide. Do NOT amend/create the `f_dominance_conversion_ceiling` substrate entry until then.
- **Re-derive brake:** does NOT fire (0 prior `substrate_ceiling`/`non_contributory` autopsies on MECH-457; 742 was `competence_implementation_gap`/`weakens`).
- MECH-457 stays `candidate` / `v3_pending`.

## 9. Draft `evidence_quality_note` (for `/governance` to write — do NOT write from this skill)

> 2026-07-13 (GOV-FANOUT-1 discrimination portfolio V3-EXQ-747/748/749, diagnostic, claim_ids=[MECH-457]; consumed via /governance from failure_autopsy_MECH-457-fanout-747-748-749_2026-07-13): the two-axis fanout (representation × teacher) REFUTES H-rep and the reward-density reading. Reward SHAPING rescues neither representation (z_world shaped 0.217, raw shaped 0.767 — both sub-floor 1.0/ceiling 48.05); only behavior-cloning clears the floor, on BOTH inputs (z_world+BC 32.72, raw+BC 20.93), and z_world+BC > raw+BC — so the prediction-trained z_world is NOT action-inadequate. The discriminated cause is the RL exploration/credit-assignment bootstrap (only imitation bypasses it), not representation and not reward density. This STRENGTHENS a dependency reading: action-learning requires a bootstrappable action-level teaching signal / developmental scaffold (BC = observational-acquisition analog), consistent with the O'Doherty/Schultz/Sutton biology. MECH-457 stays candidate/v3_pending, competence_implementation_gap; sufficiency weakens, dependency strengthened. One live discrimination remains on the algorithm axis (is an expert teacher necessary, or is unsupervised exploration merely too weak). Routed to /lit-pull (developmental scaffolding / exploration under sparse reward) to decide the build target before any substrate commit; H-optim leg preserved as the next empirical discrimination. No substrate_queue entry amended/created this cycle.
