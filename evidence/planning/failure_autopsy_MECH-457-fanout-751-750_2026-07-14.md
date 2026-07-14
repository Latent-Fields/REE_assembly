# Failure Autopsy — MECH-457 GOV-FANOUT-1 continuation (V3-EXQ-751 + V3-EXQ-750)

- **Generated:** 2026-07-14T17:27:43Z
- **Scope:** cluster (convergent continuation)
- **Status:** confirmed
- **Cluster slug:** `MECH-457-fanout-751-750`
- **Fans out from:** `failure_autopsy_MECH-457-fanout-747-748-749_2026-07-13.json`
- **Routed by:** /governance session `nifty-cerf-c06cab`, REE_assembly commit `5563f7546b` (pending_review=2; 751/750 synced mid-cycle, routed to /failure-autopsy)
- **Recording:** both manifests complete (`validate_recording` OK — `substrate_hash 2eff4545…`, seeds [42,43,44], `rec/v1`). **No recording gap.**

---

## Where this sits

The 747/748/749 autopsy REFUTED **H-rep** (z_world+BC 32.72 > raw+BC 20.93) and **reward-density** (shaping sub-floor on both inputs), and discriminated the cause as the **RL exploration / credit-assignment bootstrap** — only behavior-cloning (an expert action-target) cleared the floor. It left **one live discrimination on the algorithm axis**: *is an expert teacher necessary, or was unsupervised exploration merely too weak?* — and deferred the substrate build (`action=none`) pending exactly the H-optim leg. **V3-EXQ-751 is that leg.** V3-EXQ-750 is the parallel INV-088 strategy-diversity readout on the same 2×2.

---

## TARGET 1 — V3-EXQ-751 (H-optim leg D) — diagnostic PASS, adjudicated VALID

### Facts

| Item | Value |
|---|---|
| Outcome | PASS |
| Load-bearing criterion | `C_any_unsupervised_explorer_clears_floor_at_D3` = **passed** |
| Preconditions | local_view_greedy 48.05 ≥ 1.0 ✓ · greedy_oracle 57.2 ≥ 1.0 ✓ · non_degenerate ✓ · all `criteria_non_degenerate` true |
| **RND arm** (Random Network Distillation, learned novelty) | **5.22 forage, 3/3 seeds supra-floor** → cleared |
| **ICM arm** (forward-model curiosity) | 0.22 forage, 0/3 supra-floor → **did NOT clear** (≈ sparse baseline 0.30) |
| Sparse z_world baseline (742 reproduction) | 0.30, sub-floor (expected band [0.20,0.27]; +0.03 drift, still sub-floor) |
| Reference | BC expert (748) 32.72 · local_view_greedy ceiling 48.05 · oracle 57.2 |
| ICM vs RND intrinsic reward | ICM 0.069 **higher** than RND 0.030 — yet ICM gained no competence |

### Adjudication — self-route CONFIRMED and REFINED

Self-route `stronger_unsupervised_explorer_clears_floor_exploration_was_the_wall` is a **valid, non-vacuous, preconditions-met** diagnostic PASS (NOT `precondition_unmet`, NOT `vacuous_pass`). The pre-registered criterion routes on *any* unsupervised explorer clearing the 1.0 floor with no expert / no BC; RND cleared it on a strict majority of seeds. Two refinements the raw label hides (per user decision, foregrounded):

1. **Only RND worked; ICM failed.** The working signal is **learned novelty** (random-target distillation), not forward-model curiosity. ICM had *higher* intrinsic reward but no competence gain — the classic degenerate-forward-model failure in a hard-to-model view. The build seed is **RND-family, not ICM**.
2. **RND clears only the FLOOR.** 5.22 is ~6× the floor but ~16% of the BC expert (32.72) and ~11% of the local-view observability ceiling (48.05). Unsupervised novelty gets you *off the floor*, not to *competent* foraging.

**Aliasing check — passes.** RND intrinsic reward is task-agnostic state novelty (no oracle, no task-reward shaping), so the competence gain is genuine coverage, not reward leakage. ICM's higher intrinsic reward with zero competence gain confirms the two arms are measuring novelty vs curiosity, not leaked task signal. Mild baseline drift (0.30 vs [0.20,0.27]) noted, but the baseline stays sub-floor so the discrimination holds.

### Four-layer diagnosis (751)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened-and-refined** | resolves the fork: expert NOT necessary; machinery functional-when-explored, not only functional-when-taught |
| Biological reference | **clear** | RND = novelty-driven intrinsic motivation (developmental self-directed exploration precedes expert scaffolding); ICM failure is an RL implementation property, not a claim problem |
| Prerequisites | identified | the bootstrappable action-level signal can be a self-generated novelty drive, not necessarily an external teacher |
| Implementation | complete | arms ran clean; always-core recorded |
| Environment | adequate | oracle 57.2, local-view 48.05 clear the floor |
| Measurement | adequate | per-seed competence + intrinsic-reward traces recorded |
| Integration | adequate | z_world→policy under a learned intrinsic signal reaches supra-floor |
| Scale | **insufficient at the current explorer** | RND clears floor but is far below BC/ceiling — the build target |

### Verdict + routing (751)
**Expert teacher NOT necessary** — vanilla policy-gradient was too weak; a learned-novelty drive (RND) bootstraps off the floor. **But the mechanism CLASS for the floor→competent gap is NOT settled by 751** (novelty clears the floor ≠ a novelty bonus closes the gap; the 742/748 baseline already had entropy + count-based novelty and stayed sub-floor). Route: **`/lit-pull`** (user decision 2026-07-14) scoped to class-choice + composition-vs-duplication against the landed REE exploration substrate — **no substrate_queue entry this cycle.** Re-derive brake does NOT fire (0 prior). GOV-FANOUT-1: the open item is a *literature/design* class-choice, not yet a queued experiment portfolio.

---

## TARGET 2 — V3-EXQ-750 (INV-088 strategy-diversity readout) — FAIL, NON_CONTRIBUTORY

### Facts

| Item | Value |
|---|---|
| Outcome | FAIL |
| Load-bearing precondition `dense_pair_matched_competent` | **NOT met** — `min(majority_supra_floor(z_world_dense), majority_supra_floor(raw_dense)) = 0`, threshold 1 |
| z_world dense (shaped RL) | 0.217, 0/3 supra-floor |
| raw dense (shaped RL) | 0.767, 1/3 supra-floor |
| Instrument calibration | H_greedy(random_walk) 2.32 − H_greedy(constant) 0.0 = **2.32 bits > 1.0** ✓ (works) |

### Adjudication — non_contributory / starved CONFIRMED

Precondition unmet → the decisive INV-088 contrast (748 z_world+dense vs 749 raw+dense at matched competence) cannot be read. Two nested causes:

1. **Teacher-variant mismatch (design).** 750's "dense" arms are dense-reward-**shaping** RL (`shaping_coef=1.0`) — the *sub-floor* variant already shown starved in 748/749. The arms that actually cleared the floor there were **BC** (behavior cloning), which 750 did not use. The 2×2 label "dense teacher = PASS" conflated BC (the arm that passed) with shaping (the arm that failed). So the precondition was doomed by construction.
2. **Even BC wouldn't give a clean read.** A behavior-cloned policy's action distribution reflects the *imitated expert's* diversity, not the representation's intrinsic diversity-affording capacity (both z_world+BC and raw+BC clone the same expert). The teacher **launders** INV-088's contrast. A clean representation→diversity read at matched competence needs matched-competent **unsupervised** policies on *both* representations → **the same explorer build 751 motivates**, plus the raw-view explorer arm 751 did not run.

**Confound flag — NOT evidence.** At sub-floor competence, z_world arms collapsed to near-monostrategy (H_greedy 0.31, effective_actions ~1.3, histograms like `[0,4000,0,0,0]`) while raw arms kept more spread (0.99–1.36). Direction is *opposite* to INV-088's prediction — but this is a **training-collapse artifact**, exactly why matched competence is the load-bearing gate. Weights against **neither** MECH-457 nor INV-088.

### Four-layer diagnosis (750)

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **untested** | precondition gate blocks the contrast; NON_CONTRIBUTORY |
| Biological reference | n/a | readout starved before it can bear on the question |
| Prerequisites | **missing** | matched-competent unsupervised policies on both representations (the 751 explorer build) |
| Implementation | complete | 2×2 reran deterministically; instrument validated on controls |
| Environment | adequate | oracle 57.2, local-view 48.05 clear the floor |
| Measurement | instrument adequate but **starved** | H_greedy registers a real 2.32-bit spread on calibration; decisive cells are competence-starved |
| Integration | n/a | gated at the competence precondition |
| Scale | dense-shaped arms sub-floor for the same RL-exploration-bootstrap reason as 748/749 shaping arms | the 751 build target |

### Verdict + routing (750)
**NON_CONTRIBUTORY / starved** — does not weight against either claim. Route: **re-queue after substrate** (`pending_retest_after_substrate = true`), blocked on the **same** (now class-undecided) matched-competent unsupervised-competence build the 751 target routes to `/lit-pull`, extended to reach matched competence on **both** z_world and raw 5×5 view. No substrate entry this cycle. INV-088 stays candidate/pending_substrate_reconfirmation; MECH-457 stays candidate/v3_pending.

---

## Cluster read

Not a substrate-ceiling shared-shape cluster — a **convergent continuation**. 751 (diagnostic PASS) *positively demonstrates* the seed; 750 (FAIL, non_contributory) is *starved for* it. Both point at **one buildable substrate**: a better unsupervised novelty-driven explorer (RND-family) that reaches competent foraging on both representations. One build unblocks both.

- **Structural property:** `complicated (buildable)` execution backlog behind a now-**discharged** `complex (probe-gated) / puzzle (known rules)` node — the 747/748/749 "expert-vs-exploration" puzzle is answered (exploration was the wall).
- **Granularity-debt does NOT fire.** The prior MECH-457 autopsies (734-737 → 742 → 747/748/749 → 751) *converge* on one cause, progressively refined, rather than scattering across distinct sub-mechanisms. The claim is not coarse; it is blocked on a single buildable substrate. Route = `implement-substrate`, not `claim-synthesis`.

---

## Recommended substrate_queue entry (governance applies)

**`action: none` — DEFERRED pending `/lit-pull`** (user decision 2026-07-14). The original recommendation (`create mech457_unsupervised_novelty_explorer`) was **superseded**: 751 licenses only that a *learned novelty signal clears the floor*, not that a novelty bonus closes the floor→competent gap, and a novelty module **risks duplicating the landed ARC-065 / MECH-314 curiosity substrate.** The build-target **class is open** and is a literature/design question, not a settled build.

**Candidate classes for the floor→competent gap (for the lit-pull to weigh):**

| Class | Shape | REE status / duplication risk |
|---|---|---|
| Intrinsic-motivation / novelty-drive (RND, pseudo-counts, info-gain/EFE, empowerment) | scalar reward add-on | **High overlap** — ARC-065 *stable*, MECH-314 *substrate_ceiling* (landed), MECH-313, MECH-455; lit dossier already exists |
| Behavioural-mode explore/exploit arbitration | mode/gating variable | Partial (tonic vigor, frontopolar modes) — not a first-class arbitrator |
| Options / skills / temporal abstraction (DIAYN, HRL) | reusable sub-behaviours | None |
| Go-Explore / archive-based | state archive + return | None; composes with hippocampal replay |
| Credit-assignment / reverse-replay | fixes sparse-long-horizon credit | **Exists** — hippocampal `backward_credit_sweep` |
| Curriculum / goal-generation (BC is one instance) | training-regime | Partial |

The candidate `mech457_unsupervised_novelty_explorer` is retained in the JSON as `candidate_sd_id_if_novelty_class_selected` — **one option, not the decision.** 750's retest is a `pending_retest_after_substrate` dependent of whatever class the lit-pull selects. No entry created this cycle.

---

## Draft `evidence_quality_note` text for governance

Both are drafted verbatim in the JSON (`recommended_evidence_quality_note` per target). Both diagnostics are **excluded from governance confidence/conflict scoring** (`experiment_purpose: diagnostic`); the notes record the discrimination + build target, not weighted evidence. No claim status changes: MECH-457 stays candidate/v3_pending (competence_implementation_gap); INV-088 stays candidate/pending_substrate_reconfirmation.

## Routing summary

| Target | Outcome | Verdict | Routing |
|---|---|---|---|
| V3-EXQ-751 | diagnostic PASS | expert NOT necessary; RND clears floor unsupervised (ICM fails; floor not ceiling); **build-class undecided** | **lit-pull** (class-choice + duplication check); substrate entry deferred |
| V3-EXQ-750 | FAIL | non_contributory / starved; precondition unmet | **lit-pull (shared)** → substrate → re-queue; `pending_retest_after_substrate` |

> **Update 2026-07-14 (user decision):** original routing (`implement-substrate` / create novelty-explorer entry) superseded by **`/lit-pull` first**, scoped to which mechanism class closes the floor→competent gap and whether it composes with vs duplicates the landed ARC-065/MECH-314/hippocampal-replay substrate. No substrate entry created this cycle.
