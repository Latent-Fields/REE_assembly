# Failure Autopsy — MECH-457 GOV-FANOUT-1 discrimination portfolio (V3-EXQ-752 + 753 + 754)

- **Generated:** 2026-07-15T08:27:34Z
- **Scope:** cluster (convergent continuation)
- **Status:** confirmed
- **Cluster slug:** `MECH-457-fanout-752-753-754`
- **Fans out from:** `failure_autopsy_MECH-457-fanout-751-750_2026-07-14.json`
- **Arc:** 734-737 (conversion-ceiling / competence gap) → 742 (ON/OFF: sufficiency weakens, deficit upstream of credit-assignment) → 747/748/749 (H-rep + reward-density REFUTED; cause = RL exploration/credit bootstrap) → 751 (RND clears floor, exploration was the wall; ICM fails) + lit-pull (novelty class rejected as the build; 4 composable classes named) → **752/753/754 (this autopsy): three of those composable classes, all FAIL sub-floor.**
- **Recording:** all three manifests `validate_recording` OK — `substrate_hash` present, seeds [42,43,44], `rec/v1`. **No recording gap.**
- **User decisions (2026-07-15, Step 8 gate):** (1) accept the **cold-start / success-dependence** reading as load-bearing; (2) route **`/implement-substrate` now (build the competent explorer) AND queue H-mode in parallel** as the one genuinely-distinct remaining axis.

---

## Where this sits

The 751/750 autopsy discharged the "expert-vs-exploration" puzzle (exploration was the wall; RND clears the 1.0 floor to 5.22 unsupervised, ICM fails) and, after a landed `/lit-pull` **rejected the novelty class as the build** (coverage-not-competence; duplicates ARC-065/MECH-314), routed to a **GOV-FANOUT-1 combination-aware discrimination portfolio** over four composable classes on distinct axes. **752/753/754 are three of those four legs.** Each was pre-registered to test whether its class **lifts above the RND novelty plateau (5.22)** toward the BC-expert competence (32.72) / local-view ceiling (48.05) — NOT a power-bump of a prior design.

The H-credit×H-return **pair cell (V3-EXQ-756) is still in flight** (`claimed`); the **H-mode** leg (explore/exploit arbitration) was never queued.

---

## Facts — the three legs

Shared controls (consistent across all three runs; env solvable, floor real):

| Control | foraging_competence @D3 |
|---|---|
| `local_view_greedy` (5×5 observability ceiling) | 45.75 / 49.7 / 48.7 |
| `greedy_oracle` (global-info ceiling) | 57.0 / 57.3 / 57.3 |
| `random_walk` (near-floor lower bound) | 1.05 / 0.9 / 0.85 |
| `sparse_zw` (z_world sparse RL baseline, 742 reproduction) | 0.15–0.30 |
| `sparse_raw` | 0.15–0.55 |

Reference cells (prior arc): RND novelty plateau **5.22** (751); BC expert **32.72** (748); ICM **0.22** (751, failed).

Mechanism arms (per-seed foraging_competence @D3):

| Run | Class / axis | z_world arm | raw arm | Load-bearing criterion |
|---|---|---|---|---|
| **752** H-credit | prioritized backward credit sweep (reuses landed hippocampal `backward_credit_sweep`) | 0.2 / 0.45 / 0.3 | 0.25 / 0.4 / 0.35 | `C_hcredit_lifts_above_novelty_plateau` = **FAIL** |
| **753** H-return | Go-Explore state archive + return (teleport via resettable env) | 0.25 / 0.2 / 0.3 | 0.15 / 0.3 / 0.45 | `C_hreturn_lifts_above_novelty_plateau` = **FAIL** |
| **754** H-curriculum | AMIGo goal-frontier (adversarially-motivated intrinsic goals) | 0.15 / 0.2 / 0.15 | 0.15 / 0.1 / 0.3 | `C_hcurriculum_lifts_above_novelty_plateau` = **FAIL** |

**Which criterion failed:** the discrimination / "lift" criterion — not an absolute or negative-control criterion (those all passed: env solvable, controls valid, non-degenerate). Every mechanism arm landed at ~0.15–0.45, i.e. **statistically indistinguishable from vanilla sparse RL, below the 1.0 floor, and far below RND's 5.22 success-independent plateau.** The three classes added *nothing* over the sparse baseline they were meant to beat.

---

## Cluster read — convergent, not N independent bugs

Three independent, well-motivated, distinct-axis mechanism classes each collapse to *exactly* the sparse-RL baseline. That is not three implementation bugs; it is **one structural property**.

**The unifying property (cold-start / success-dependence).** What separates the three failures from the two mechanisms that *did* move competence earlier (RND 5.22, BC 32.72):

- **Backward credit sweep** needs a *successful trajectory* to propagate credit backward from. At ~0 foraging success there is nothing to sweep.
- **Go-Explore archive/return** needs to *first reach* interesting/rewarding states to archive them. An incompetent policy reaches none → empty/uninformative archive (753's own docstring: RND "DETACHES from the frontier"; the return is "a teleport").
- **AMIGo goal-frontier** proposes intermediate goals the current policy can *just* achieve; from ~0 competence the achievable frontier is trivial and carries no gradient toward foraging.

All three **amplify or restructure signal derived from successful experience.** RND (novelty reward available from step 1) and BC (copy an expert) are the only two classes that are **success-independent**, and they are the only two that broke the floor. So the competence floor is a **cold-start problem**: mechanisms that presuppose task success cannot bootstrap competence from zero; only a **success-independent dense per-step drive** can.

This is biology-resonant: developmentally, **novelty-driven self-directed exploration and imitation both precede and scaffold competent goal-directed (reward-credit) action** — pure reward-credit learning presupposes reward the organism has not yet earned. It is a *discovered dependency / positive-negative*, not a falsification of MECH-457.

**Two live readings (both recorded; the cold-start read is load-bearing per user decision):**
1. **Cold-start / success-dependence (adopted).** Structural property above. Directly specifies the build.
2. **Test-design ceiling (subordinate).** Each class *could* in principle have been under-trained / under-capacity; three independent implementations collapsing to the *identical* sparse baseline argues against three coincident under-trainings, but faithful per-mechanism internals were not line-by-line re-verified in this autopsy (portfolio-gated via `/queue-experiment` code-review + smoke-test).

---

## Claim-layer mapping

- **MECH-457** (mechanism_hypothesis; candidate; v3_pending; depends_on SD-056, MECH-229) — "the action-LEARNING MACHINERY that converts drive into learned control (how action is learned at all)." The three FAILs **do not test the claim's truth** — they discriminate *which* bootstrapping class the machinery needs. They **strengthen the dependency reading** the 747/748/749 autopsy opened: action-learning requires a bootstrappable, **success-independent** action-level signal (novelty-drive / imitation), consistent with O'Doherty/Schultz/Sutton. Necessity NOT falsified; sufficiency of sparse-reward-credit tricks REFUTED. MECH-457 stays **candidate / v3_pending**.
- **INV-088** (invariant; emergent; candidate) — carried on 750/754 as the strategy-diversity readout. Untouched here as claim evidence (the diversity contrast remains starved for a matched-competent policy — same block as 750). Stays **candidate / pending_substrate_reconfirmation**.

Both diagnostics are `experiment_purpose: diagnostic` → **excluded from governance confidence/conflict scoring.** This autopsy records the discrimination + build target, not weighted evidence. **PROMOTES / DEMOTES NOTHING.**

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (dependency)** | refutes sufficiency of sparse-reward-credit bolt-ons; strengthens the success-independent-bootstrap dependency; does not falsify MECH-457 |
| Biological reference | **clear** | novelty-drive + imitation developmentally precede/scaffold reward-credit action; cold-start is a known RL + developmental property, not a claim defect |
| Prerequisites / dependencies | **missing (buildable)** | a success-independent dense per-step drive wired to the foraging policy, with capacity to convert coverage→competence (RND got off-floor only) |
| Implementation completeness | complete (portfolio-gated); per-mechanism internals not re-verified line-by-line | three arms ran deterministically; always-core recorded; identical-to-baseline collapse argues against three coincident bugs |
| Environment adequacy | **adequate** | oracle 57, local-view 48, RND 5.22 all clear the 1.0 floor — the floor is genuine, not an env artifact |
| Measurement adequacy | **adequate** | per-seed competence recorded; RND/BC/ceiling reference bands pre-registered; criterion is a real "lift above plateau" test |
| Integration adequacy | isolated-per-class | each class run alone; the H-credit×H-return pair cell (756) tests additivity and is still in flight |
| Scale / capacity | **insufficient at the current explorer** | the build target: reach *competent* (not merely off-floor) foraging on the 5×5 view |

**Recording-debt vs measurement-debt:** neither. All manifests are recording-complete and the metric was the right one. The gap is a **buildable substrate**, not a blind spot.

---

## Re-derive brake (MOVE-3) — FIRES

- Prior `substrate_ceiling`/`non_contributory` failure-autopsy docs tagging **MECH-457**: **1** (`failure_autopsy_MECH-457-fanout-751-750_2026-07-14`, target 750).
- This autopsy records the three legs as **non_contributory to claim confidence** (diagnostic; PROMOTES/DEMOTES NOTHING) and convergent-on-substrate → the **2nd** such reading (threshold = 2). **Brake fires.**
- **Consequence:** route to **`/implement-substrate`** on the named upstream substrate; **REFUSE** a further same-claim *bolt-on* test re-queue (another credit/return/curriculum-style class circling the same competence floor is exactly the loop the brake exists to stop).
- **Reconciliation with the user's "run H-mode in parallel" decision:** the brake refuses *lettered re-derivation of the same mechanism against the same ceiling*. **H-mode (explore/exploit arbitration) is a genuinely distinct design axis** the prior GOV-FANOUT-1 portfolio already sanctioned, and it runs **in parallel with the build without gating it** — this is the sanctioned diverse-portfolio exemption, not a brake violation. H-mode must NOT block the substrate build.

## GOV-FANOUT-1 — the one remaining distinct axis

The bottleneck is now a **single build** (see below), so the primary route is `/implement-substrate`, not a fresh fan-out. The one remaining live *discrimination* leg is **H-mode**, queued in parallel:

- **H1 (adopted, → build):** the floor is a cold-start needing a success-independent dense drive → build the competent explorer.
- **H-mode leg:** does an explicit **explore/exploit behavioural arbitration** (critic-utility gate) lift above the RND plateau where the three success-dependent classes did not? Distinct axis (behavioural mode, not reward-credit reshaping). Declared null: H-mode arm ≤ RND 5.22 plateau on a strict majority of seeds. Shares the same env/baseline + the 742-sparse and RND-5.22 reference cells.

---

## Routing

| Target | Outcome | Verdict | Routing |
|---|---|---|---|
| V3-EXQ-752 (H-credit) | diagnostic FAIL | non_contributory to confidence; strengthens cold-start dependency | **implement-substrate** (shared build) |
| V3-EXQ-753 (H-return) | diagnostic FAIL | " | **implement-substrate** (shared build) |
| V3-EXQ-754 (H-curriculum) | diagnostic FAIL | " | **implement-substrate** (shared build) |
| — parallel leg — | — | one remaining distinct axis | **queue-experiment**: H-mode explore/exploit arbitration (does NOT gate the build) |

**Recommended substrate_queue entry (governance applies): `action: create`** — a NEW entry, distinct from `f_dominance_conversion_ceiling` (that is the *downstream selection-face* variance-monopoly ceiling — MECH-439/448/449; this is the *upstream competence-floor / cold-start* gap). See JSON `recommended_substrate_queue_entry`.

- **Build target:** a competent unsupervised explorer that **composes the landed ARC-065 / MECH-314 curiosity-novelty substrate as a success-independent bootstrap drive** for the foraging policy (composition, not a new novelty module — honours the lit-pull's duplication objection), **plus adequate policy capacity / training budget to convert coverage→competence** (RND reached only 5.22 ≈ 11% of the 48 ceiling). Targets **floor→competent**, not merely off-floor.
- **Blocks:** MECH-457 (competence floor), INV-088 (the matched-competent policy its strategy-diversity readout is starved for), and is **upstream of** the whole conversion-ceiling cascade behind `f_dominance_conversion_ceiling`.
- **Priority 1** (three fresh failure records + shared upstream competence blocker).

---

## Draft `evidence_quality_note` text for governance (per target — verbatim in JSON)

**MECH-457 (752/753/754):** "2026-07-15 (GOV-FANOUT-1 discrimination portfolio V3-EXQ-752/753/754, diagnostic, claim_ids=[MECH-457(+INV-088 on 754)]; consumed via /governance from failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15). Three composable action-learning classes on distinct axes — H-credit (backward credit sweep), H-return (Go-Explore archive/return), H-curriculum (AMIGo goal-frontier) — each FAIL to lift above the RND 5.22 novelty plateau; all three collapse to the sparse-RL baseline (~0.15–0.45 @D3, below the 1.0 floor), adding nothing over vanilla sparse RL while every readiness precondition holds (oracle 57, local-view 48, random_walk floor). DISCRIMINATED CAUSE (cold-start / success-dependence): all three amplify signal derived from prior task success (credit to propagate / states to archive / achievable frontier), so they cannot bootstrap from ~0 competence; only the two success-INDEPENDENT classes tested in the arc — RND novelty (751, 5.22) and BC imitation (748, 32.72) — break the floor. STRENGTHENS the dependency reading (action-learning needs a success-independent dense per-step bootstrap signal — novelty-drive/imitation — consistent with O'Doherty/Schultz/Sutton); does NOT falsify MECH-457 (necessity intact; sufficiency of sparse-reward-credit tricks refuted). Diagnostic — excluded from confidence/conflict scoring; PROMOTES/DEMOTES NOTHING. Re-derive brake FIRES (2nd non_contributory/convergent MECH-457 autopsy): route = implement-substrate (competent unsupervised explorer composing ARC-065/MECH-314 curiosity as a success-independent bootstrap drive + policy capacity, floor→competent); same-claim bolt-on test re-queue REFUSED. H-mode explore/exploit arbitration queued in parallel as the one remaining distinct axis (does not gate the build). MECH-457 stays candidate/v3_pending. The H-credit×H-return pair cell V3-EXQ-756 was in flight at autopsy time."

**INV-088 (754):** "2026-07-15 (V3-EXQ-754, diagnostic, INV-088 carried): the strategy-diversity readout remains starved — no matched-competent policy exists on either representation (same block as 750). Not weighted against INV-088. Retest is pending_retest_after_substrate on the competent-explorer build. INV-088 stays candidate/pending_substrate_reconfirmation."
