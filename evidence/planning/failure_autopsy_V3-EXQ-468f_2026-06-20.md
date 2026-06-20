# Failure Autopsy -- V3-EXQ-468f (SD-034 / MECH-268 / MECH-090 de-commit hold / perseveration; de-commit-MAGNITUDE substrate)

- **Generated / confirmed:** 2026-06-20T06:43:37Z
- **Status:** confirmed (interactive gate; user confirmed both load-bearing dispositions 2026-06-20)
- **Scope:** single target, read as a **cluster with V3-EXQ-460h** (the de-commit-side sibling, autopsied in a parallel live session 2026-06-20) -- both are closure-coupling non-vacuity FAILs on the same de-commit-MAGNITUDE-amended substrate
- **Run:** `v3_exq_468f_sd034_mech268_decommit_hold_behavioural_20260619T224456Z_v3` (supersedes 468e). FAIL, self-route `substrate_not_ready_requeue`, route_reason `closure_coupling_or_contradiction_not_engaged`.
- **Manifest:** `REE_assembly/evidence/experiments/v3_exq_468f_sd034_mech268_decommit_hold_behavioural_20260619T224456Z_v3.json`
- **Predecessors / lineage:** 468e (`failure_autopsy_V3-EXQ-468e_2026-06-18`) -> 460f (`..._V3-EXQ-460f_2026-06-18`) -> 460g (`..._V3-EXQ-460g_2026-06-19`, the 7th SD-034-closure autopsy that surfaced the magnitude-lever-suppresses-the-coupling-metric finding + routed to `/claim-synthesis`). The SD-034 closure umbrella was decomposed 2026-06-19 into **MECH-445 (coupling engagement)** + **MECH-446 (de-commit magnitude)** (`claim_synthesis_SD-034-closure_2026-06-19.md`).

---

## One-line verdict

468f is **non_contributory** for all three tagged claims (SD-034 / MECH-268 / MECH-090) with **NO weakens** -- and it is *doubly* non-contributory. (1) Its load-bearing precondition `closure_coupling_and_contradiction_nonvacuous` was genuinely unmet (the closure->beta coupling did not engage), so neither load-bearing criterion drove a verdict (both `criteria_non_degenerate` C1/C2 = false; 0/3 criteria pass). (2) It measured that precondition with **`sd034_n_closure_coupled_elevations`** -- the per-ENTRY counter the **460g de-commit-MAGNITUDE lever structurally suppresses** (the S5 entanglement) -- and did **not** adopt the **460h refractory-independent `sd034_n_closure_commit_intent` certifier** built specifically to fix that. So 468f is the perseveration-side sibling that lagged the 460g->460h instrumentation upgrade: it re-ran the perseveration question on the magnitude-amended substrate using the very counter that substrate zeroes. Route: re-issue **468g** with the refractory-independent gate; substrate_queue **amend** (append the 468f failure record + the instrumentation-lag note). 468g stays gated on the genuine shared substrate gap -- **MECH-445 coupling under-engages on natural strong-commit seeds** (460h certified it on only 1/3 seeds even with the correct counter).

---

## Facts reconstruction (facts only)

### Acceptance / readiness gates

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard (603n G2+G3) | 0.667 | 0.667 | yes |
| rule_bias_head_trained (Leg-C anti-460d) | 1.0 | 0.667 | yes |
| **closure_coupling_and_contradiction_nonvacuous** (load-bearing) | **0.0** | 0.667 | **NO** |
| within_arm_window_nonvacuous | 1.0 | 0.667 | yes |

`route_reason = closure_coupling_or_contradiction_not_engaged`; `interpretation.label = substrate_not_ready_requeue`; `criteria_non_degenerate = {C1: false, C2: false}`; per-seed criteria pass `[false, false, false]`; guard-passing seeds 2/3 (seeds 42, 43; seed 44 fails the contact guard at z_goal_norm_at_contact_peak 0.399 < 0.4).

### Per-seed ON-arm closure-coupling + occupancy

| seed | guard | n_hook_fires | **sd034_n_closure_coupled_elevations** | episodes_with_contradiction | mean_pre_committed_occ | mean_post_committed_occ | C1 | C2 |
|---|---|---|---|---|---|---|---|---|
| 42 | yes | 3 | **0** | 6 | 1.0 | 1.0 | pass | fail |
| 43 | yes | 4 | **0** | 4 | 1.0 | 1.0 | pass | fail |
| 44 | no | 1 | **0** | 5 | 1.0 | 1.0 | pass | fail |

The env-completion hook **fired** on every ON-arm seed (n_hook_fires 3/4/1), but produced **zero** closure-coupled beta elevations. Committed occupancy is pinned at 1.0 both pre- and post-contradiction (the de-commit DV has nothing to register a drop against), and `decommit_gap = 0.0` on every seed.

### C1 "passes" 3/3 but is degenerate

C1 (`beta_release_near_contradiction >= 1`) is true on all three seeds (releases 12/7/31 ON), but `criteria_non_degenerate.C1 = false`: with `sd034_n_closure_coupled_elevations = 0`, those releases are the **natural** commit/release cycle, not the closure-coupled latch release the test means to read. So C1's pass carries no MECH-268/MECH-090 signal.

---

## Root cause (code-confirmed): the suppressed-counter S5 entanglement

`note_closure_coupled_elevation()` (the increment of `sd034_n_closure_coupled_elevations`) is called **only inside** the bistable `elevate()` if-block, guarded by `not self.beta_gate.is_elevated` (`ree-v3/ree_core/agent.py:6082-6094`):

```
if (_commit_for_beta and not self.beta_gate.is_elevated
        and self.beta_gate.should_admit_elevation(...) and _readiness_admits):
    self.beta_gate.elevate()
    if _closure_commit_active and not result.committed:
        self.beta_gate.note_closure_coupled_elevation()   # per-ENTRY only
```

Once the closure-coupled commit latches beta elevated for the long committed run, the per-entry counter freezes. 468f's substrate carries the **460g de-commit-MAGNITUDE lever** (`closure_decommit_hold_scale_with_run=0.1`, cap 60; manifest substrate string + `pre_registered_thresholds.closure_decommit_hold_*`), whose refractory **blocks re-elevation** (`closure_operator.py:502, 530-548`), so the counter can never re-fire as a transition either.

This is exactly the failure the **460g autopsy** named ("strong-refractory-suppresses-the-coupling-metric") and the **460h refractory-independent commit-intent certifier** was landed to fix: `note_closure_commit_intent()` (counter `sd034_n_closure_commit_intent`) is called **before** the elevate/refractory gate (`agent.py:6080-6081`), certifying the closure-plane commit INTENT regardless of whether the latch is held elevated or the magnitude refractory blocks re-elevation. **468f never references that counter** (grep over the 468f script: zero matches) -- it keys its load-bearing non-vacuity gate on the suppressed per-entry counter.

---

## Cluster reading (468f + 460h)

| | non-vacuity counter | coupling certified | reading |
|---|---|---|---|
| **V3-EXQ-460h** (MECH-445/446) | refractory-**independent** `sd034_n_closure_commit_intent` (the 460h fix) | **1/3** guard seeds (`coupling_nonvacuity_fraction = 0.333`) | genuine coupling-engagement gap -- MECH-445 under-engages on natural strong-commit seeds |
| **V3-EXQ-468f** (SD-034/MECH-268/MECH-090) | per-**ENTRY** `sd034_n_closure_coupled_elevations` (suppressed by the magnitude lever) | **0/3** | measurement artifact on top of the same gap; cannot even see it |

**Structural property (one gap, two channels):** the closure->beta coupling under-engages on the foraging substrate's natural strong-commit seeds. 460h shows this through the correct counter (1/3); 468f reproduces the 460g instrumentation-suppression finding through the perseveration DV (0/3). These are **not two independent bugs** -- they are the de-commit-side and perseveration-side renderings of one MECH-445 coupling-engagement gap, already decomposed by the 460g `/claim-synthesis`. 460h is being autopsied in a parallel live session; this artifact stays distinct and cross-references it.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | SD-034 unclear / MECH-268 NOT fairly tested / **MECH-090 NOT fairly tested** | the closure coupling never engaged, so no claim could express itself; C1's "pass" is degenerate (natural release, not closure-coupled) |
| Biological reference | clear | sustained counter-evidence -> task-set disengagement (Collins & Frank 2014; Rich & Shapiro 2009). The reference mechanism never fired here -- the BG-like closure->beta coupling did not engage, so the de-commit had nothing to release |
| Prerequisites | present-but-inert | Legs A/B/C + beta-engagement + magnitude lever all landed; the residual is that the coupling does not *engage* on strong-natural-commit seeds (MECH-445), AND the perseveration script measures it with the suppressed counter |
| Implementation | **measurement gap** | the load-bearing non-vacuity gate keys on `sd034_n_closure_coupled_elevations` (suppressed by the magnitude refractory) instead of the landed `sd034_n_closure_commit_intent` (460h) |
| Environment | adequate | contradictions fire on every ON seed (episodes_with_contradiction 6/4/5); guard 2/3 |
| Measurement | **under-instrumented / wrong counter** | suppressed per-entry counter + occupancy DV pinned at the 1.0 ceiling (nothing committed-then-released to measure when coupling never engages) |
| Integration | isolated | the env-completion hook fires but does not couple to a measurable beta elevation (coupled_elev 0; commit-intent uninstrumented) |
| Scale / capacity | adequate | eval=15 episodes; releases + contradictions fire; not the binding gap |

**Recommended epistemic_category:** no change to any claim's category. The self-route `substrate_not_ready_requeue` is **correct** for 468f (precondition genuinely unmet; do NOT read as a substrate_ceiling or a weakens). SD-034 stays provisional, MECH-268 candidate, MECH-090 active -- all `non_contributory` + `pending_retest_after_substrate`.

---

## Recurrence check (granularity-debt / `/claim-synthesis`)

This is the latest in the SD-034 closure lineage (468e -> the 460c..460h chain). The granularity-debt was **already actioned**: the 460g autopsy routed the cluster to `/claim-synthesis`, which decomposed SD-034 into MECH-445 (coupling) + MECH-446 (magnitude) on 2026-06-19. 468f is the perseveration-side confirmation of the **same** MECH-445 coupling-engagement gap, not a structurally-new signature -- so **no new `/claim-synthesis` is owed**. The actionable residual is (a) the 468-lineage instrumentation lag (fixed by the 468g re-issue) and (b) the shared MECH-445 coupling-engagement gap (owned by the substrate_queue entry + the parallel 460h adjudication).

---

## Learning extracted

- 468f's coupling non-vacuity gate keys on `sd034_n_closure_coupled_elevations`, the per-ENTRY counter the 460g de-commit-MAGNITUDE refractory structurally suppresses. The perseveration script (468-lineage) did NOT adopt the 460h refractory-independent `sd034_n_closure_commit_intent` certifier; the de-commit script (460-lineage) did. This is an instrumentation lag across the two parallel lineages on the same substrate.
- Because the coupling never engaged (coupled_elev 0 / commit-intent uninstrumented), C1's 3/3 "pass" is degenerate (natural release, not closure-coupled) -- so unlike 468e (non-degenerate C1, narrow MECH-268 supports), 468f carries **no** MECH-268 positive. All three claims non_contributory.
- Cluster with 460h: the genuine binding gap is **MECH-445 coupling engagement** -- the closure->beta coupling certifies on only 1/3 seeds even with the correct counter (460h). A 468g re-issue with the refractory-independent gate will keep self-routing `substrate_not_ready_requeue` until MECH-445 coupling clears >= 2/3 seeds; this is the real substrate work, not a perseveration-DV problem.
- MECH-090 protection (carried from the 468e autopsy): MECH-090 is `active`; its mechanism (latch release under contradiction) is what C1 tests, and a degraded/degenerate C1 must not weaken it. 468e's narrow MECH-268 positive (on the pre-magnitude beta-engagement substrate, non-degenerate C1) is NOT invalidated by 468f and stays as adjudicated.

---

## Repair pathway (user-confirmed routing)

1. **Evidence disposition (governance applies):** SD-034 -> `non_contributory`; MECH-268 -> `non_contributory` (C1 degenerate -- no narrow positive on this substrate); MECH-090 -> `non_contributory` (protect the active latch; degenerate C1 must not weaken it). All three keep `pending_retest_after_substrate`. **NO weakens.** Confirms the manifest self-stamp (`evidence_direction_per_claim` already `non_contributory` for all three).
2. **468e:** stays as adjudicated -- NOT flipped to superseded/scoring-excluded. 468e ran on the pre-magnitude beta-engagement substrate with a non-degenerate C1; 468f (different substrate, suppressed counter) does not invalidate it. The manifest `supersedes: V3-EXQ-468e` is forward lineage tracking only.
3. **substrate_queue `action=amend`** on `commitment-closure-control-plane`: append the 468f failure record + an instrumentation-lag note (the perseveration script must adopt the landed `sd034_n_closure_commit_intent` certifier). Status stays `amend_implemented_pending_validation`; `ready` stays false. No NEW substrate need -- the counter already exists in ree_core (460h amend); the shared coupling-engagement gap (MECH-445) is already recorded via 460g/460h.
4. **Re-issue (separate `/queue-experiment` session):** **468g** -- the perseveration retest with the non-vacuity gate re-keyed to `sd034_n_closure_commit_intent > 0` (NOT `sd034_n_closure_coupled_elevations`), mirroring 460h, plus re-tagged `claim_ids` (MECH-445 as the coupling-engagement precondition; the perseveration question for SD-034/MECH-268/MECH-090). Gated on MECH-445 coupling clearing >= 2/3 seeds. Do NOT re-author 468d/468e.
5. **pending_retest_after_substrate:** TRUE for SD-034 / MECH-268 / MECH-090 until 468g returns a contributory PASS on the engaged substrate.

---

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-468f (supersedes 468e; de-commit-MAGNITUDE-amended substrate): FAIL, self-route substrate_not_ready_requeue. The load-bearing coupling non-vacuity precondition was unmet (sd034_n_closure_coupled_elevations = 0 on all 3 ON-arm seeds despite the env-completion hook firing 3/4/1), so neither load-bearing criterion drove a verdict (criteria_non_degenerate C1/C2 both false; 0/3 criteria). Autopsy (failure_autopsy_V3-EXQ-468f_2026-06-20, confirmed): doubly non-contributory -- (1) the closure->beta coupling genuinely did not engage on the foraging substrate's natural strong-commit seeds (the MECH-445 gap; cluster with V3-EXQ-460h, which certified coupling on only 1/3 seeds via the correct counter), AND (2) 468f keyed its gate on sd034_n_closure_coupled_elevations, the per-ENTRY counter the 460g de-commit-magnitude refractory structurally suppresses (the S5 entanglement), instead of the landed 460h refractory-independent sd034_n_closure_commit_intent certifier -- a 468-lineage instrumentation lag. C1's 3/3 "pass" is degenerate (natural release, not closure-coupled), so -- unlike 468e -- 468f carries no narrow MECH-268 positive. SD-034 / MECH-268 / MECH-090 -> non_contributory + pending_retest_after_substrate (protect active MECH-090; 468e's narrow MECH-268 positive on the prior beta-engagement substrate is not invalidated). Re-issue 468g with the non-vacuity gate re-keyed to sd034_n_closure_commit_intent, gated on MECH-445 coupling engagement >= 2/3 seeds.

---

## Routing decision (user-confirmed)

1. **Disposition:** non_contributory all three, no weakens, pending_retest_after_substrate (confirmed at the interactive gate).
2. **Routing:** queue-experiment 468g (refractory-independent gate) + substrate_queue amend (failure record + instrumentation-lag note) (confirmed).
3. **Cluster:** 460h is being autopsied in a parallel live session; this artifact cross-references it and stays distinct. Combined substrate gap = MECH-445 coupling engagement.
4. **No new `/claim-synthesis`:** the SD-034 -> MECH-445/446 decomposition (2026-06-19) already covers this; 468f is the perseveration-side confirmation.
