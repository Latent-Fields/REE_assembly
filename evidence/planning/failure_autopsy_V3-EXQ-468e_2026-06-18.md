# Failure Autopsy -- V3-EXQ-468e (SD-034 / MECH-268 / MECH-090 de-commit hold / perseveration; beta-engagement amend)

- **Generated / confirmed:** 2026-06-18T14:45:18Z
- **Status:** confirmed (interactive gate; user agreed with all four findings 2026-06-18 and requested the GAP-4 node repoint)
- **Scope:** single target, read as a **cluster with the already-confirmed `failure_autopsy_V3-EXQ-460f_2026-06-18`** (same beta-engagement-amend substrate; the perseveration-side sibling owed by the 460e autopsy)
- **Predecessor:** `failure_autopsy_V3-EXQ-460e_2026-06-17` (owed two successors: 460f [autopsied 2026-06-18] + **468e** [this doc]); lineage `..._SD-034-closure-control-plane-d_2026-06-13`, `..._SD-034-closure-cluster_2026-06-12` (+ ext), `..._V3-EXQ-460b-461b-464b-466b_2026-06-04`
- **Substrate under test:** `commitment-closure-control-plane` (status `amend_implemented_pending_validation`) -- Legs A/B/C landed; **BETA-ENGAGEMENT amend (`use_closure_commit_beta_coupling`, ree-v3 main f4ceea4, 2026-06-17) live this run.**
- **Run:** `v3_exq_468e_sd034_mech268_decommit_hold_behavioural_20260618T060133Z_v3` (supersedes 468d). FAIL, self-route `residual_perseveration_open`, route_reason `criteria_unmet_genuine_weakens`.

---

## One-line verdict

The beta-engagement amend **engaged the substrate fairly** -- both non-vacuity gates cleared (foraging-contact 1.0; commitment-non-vacuity 1.0: the ON arm committed AND a contradiction fired on all 3 seeds), so for the perseveration question the C1/C2 criteria actually drove a verdict. **C1 (`beta_release_near_contradiction`) PASSED on all 3 seeds, ON > OFF (43/16/58 vs 14/10/0)** -- the MECH-268 dACC-PE-saturation -> beta-release pathway works at the **proximal** level. But **C2 (`committed_frac_post_absolute` ON < OFF) FAILED on all 3 seeds because the ON-arm post-contradiction committed fraction is pinned at the 1.0 ceiling on every seed**: the agent stays *fully committed through the entire post-contradiction window despite the beta release*. This is the **same structural property as 460f, seen through an independent DV**: the proximal de-commit/release event fires with the correct sign, but it has **insufficient authority magnitude to move the downstream commitment statistic** -- and the DV is additionally measurement-weak (saturated at ceiling, near-zero dynamic range). The self-stamped **MECH-090 weakens is mis-attributed** (script line 857 ties it mechanically to the overall C2-gated PASS), but MECH-090's actual mechanism -- the bistable latch releasing under contradiction -- is exactly what **C1 measured, and C1 passed**; MECH-090 is an **active** claim and must not be weakened on a downstream-authority fail. Route to `/implement-substrate` **amend** of `commitment-closure-control-plane` (the existing entry; same de-commit-authority-magnitude lever owed from 460f + a **graded within-arm post-contradiction de-commit DV** to replace the 1.0-saturated `committed_frac_post_absolute`); re-issue **468f** alongside 460g. SD-034 / MECH-090 -> `non_contributory` + `pending_retest_after_substrate`; MECH-268 -> `supports` (C1 3/3, narrow positive).

---

## Facts reconstruction

### Non-vacuity gates (both cleared -- the criteria drove a verdict this run)

| Gate | measured | threshold | met |
|---|---|---|---|
| foraging_contact_guard (603n G2+G3) | 1.0 | 0.667 | yes |
| commitment_non_vacuity (ON committed AND contradiction fired) | 1.0 | 0.667 | yes |

`criteria_non_degenerate` = {C1: true, C2: true}; per-seed criteria pass `[false, false, false]`; `route_reason = criteria_unmet_genuine_weakens`.

### Per-seed criteria

C1 = `ARM_SUBSTRATE_ON.beta_release_near_contradiction >= 1`. C2 = `(OFF committed_frac_post_absolute - ON committed_frac_post_absolute) > 0.05`, where `committed_frac_post_absolute = committed_post_steps / post_window_steps in [0,1]`.

| seed | C1 release ON / OFF | C2 ON cfp_abs / OFF cfp_abs | decommit_gap | C1 | C2 |
|---|---|---|---|---|---|
| 42 | 43 / 14 | **1.0** / 1.0 | 0.0 | PASS | FAIL |
| 43 | 16 / 10 | **1.0** / 1.0 | 0.0 | PASS | FAIL |
| 44 | 58 / 0 | **1.0** / 0.0 | -1.0 | PASS | FAIL |

C1 passes 3/3 (ON>OFF every seed). C2 passes 0/3.

### Two load-bearing observations

**(1) The release fires with the correct sign; commitment does not follow.** `beta_release_near_contradiction` is higher on the substrate-ON arm on all three seeds (43/16/58 vs 14/10/0), and the closure-coupled elevation diagnostic `sd034_n_closure_coupled_elevations` fired 535 on seed 44's ON arm. So the dACC-saturation -> beta-release machinery (MECH-268) is doing real proximal work. But `committed_frac_post_absolute` on the ON arm is **1.0 on all three seeds** -- the agent re-commits and stays committed for essentially the whole post-contradiction window (`mean_committed_post` 192.86 / 195 / 195 against `total_post_steps/episodes` of the same magnitude). The release events happen *near* the contradiction but do not unstick the committed trajectory: **de-commit authority is sub-threshold against natural re-commitment.**

**(2) The C2 DV re-pinned at the ceiling.** 468c read a cap-pinned post/pre **ratio** (could never drop below 0.85); the 468d->468e redesign switched to the **absolute** post-contradiction committed fraction to escape that pin -- but it re-saturated at 1.0 on the ON arm. The DV is not structurally degenerate (it *can* vary: seed 44 OFF = 0.0), so this is **not** a `non_degenerate=false` vacuous-criterion case -- it is a genuine behavioural result (full perseveration despite release) compounded by a measurement that has near-zero headroom to register a *partial* de-commit. A graded within-arm DV (time-to-recommit, or committed fraction in a tight window immediately after each release event) would have the dynamic range this one lacks. Seed 44's ON=1.0 > OFF=0.0 is not evidence the wrong way -- OFF simply never committed there, so its 0.0 is a non-commit artifact, not a de-commit.

### claim_ids accuracy: MECH-090 weakens is mis-attributed

Script line 855-857 maps: `SD-034 = supports if (C1 and C2)`, `MECH-268 = supports if C1`, **`MECH-090 = supports if overall PASS else weakens`**. So MECH-090's direction is mechanically tied to the C2-gated overall pass -- but MECH-090 is the **bistable beta latch**, and the thing that tests its mechanism here (does the latch release under sustained counter-evidence?) is **C1, which passed 3/3 with ON>OFF**. The C2 fail is about whether the release produces behavioural de-commitment, which is de-commit **authority** (SD-034 / substrate territory), not the latch. MECH-090 is `active` (not candidate). A downstream-authority C2 fail must not weaken it -- this is the EXQ-048 / MECH-057b inherited-criterion failure-mode class, and exactly parallel to the MECH-261 mis-attribution the 460f autopsy corrected.

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | SD-034 partial / MECH-268 exercised+passed (C1) / **MECH-090 NOT fairly tested for C2** | SD-034 de-commit DV ran, non-vacuous, but expressed no hold. MECH-268 proximal release PASS 3/3. MECH-090 latch-release is what C1 tested (passed); its weakens is script-tied to the C2-gated overall, not its mechanism. |
| Biological reference | clear | Sustained counter-evidence -> task-set disengagement (Collins & Frank 2014 set-shift; Rich & Shapiro 2009 strategy switch). The release fires (OFC/dACC) but does not unstick the committed motor program -- release authority must scale with how strongly the agent would otherwise re-commit; a proximal release pulse against strong natural re-commitment is sub-threshold. |
| Prerequisites | present (Legs A/B/C + beta coupling) | residual = de-commit **authority magnitude**, not a missing leg. |
| Implementation | partial | The release lowers the latch briefly near the contradiction but does not drive `committed_frac_post` off the ceiling. |
| Environment | adequate | guard 3/3; contradictions fire on all seeds (episodes_with_contradiction 7/8/9 ON). |
| Measurement | **under-instrumented** | `committed_frac_post_absolute` saturates at 1.0 on the ON arm -> near-zero range to detect a partial de-commit. A graded post-release DV is needed (the 468c->468e cap-pin moved from 0.85 to 1.0 but did not lift). |
| Integration | partially coupled | Coupling -> beta release engaged on every seed (the 460e fix held) BUT the release is decoupled (by authority magnitude) from a measurable drop in committed fraction. |
| Scale / capacity | adequate | eval=15; releases + contradictions fire. Not the binding gap. |

**Recommended epistemic_category:** `substrate_ceiling` -- the substrate carries the wiring the claims assert (release fires under contradiction, C1) and expresses it proximally, but not at the de-commit-authority magnitude (or DV sensitivity) needed to move post-contradiction commitment off the ceiling. The response is substrate/DV enrichment, not more runs on the current parameterization, and not demotion. Paired with `pending_retest_after_substrate`.

---

## Cluster reading (460f + 468e)

Both ran on the beta-engagement amend; both cleared all non-vacuity gates (fair engagement for the first time in the lineage); both show the **same structural property through independent DVs**:

| | proximal de-commit event (fires, correct sign) | distal commitment DV (unmoved) | DV weakness |
|---|---|---|---|
| **460f** | seed-42 occupancy drop -33.5%; `sd034_n_closure_coupled_elevations` 36/52 | between-arm `mean_beta_elevated_steps` ON !< OFF on 2/3 | swamped by ~530-560 natural-commit elevated steps; unpaired between-arm |
| **468e** | `beta_release_near_contradiction` ON>OFF on 3/3 | `committed_frac_post_absolute` ON pinned at 1.0 on 3/3 | saturated at ceiling; near-zero dynamic range |

**Structural property:** the de-commit / release machinery fires but lacks the **authority magnitude** to move a downstream commitment statistic, and both DVs are additionally measurement-weak (one swamped by baseline, one saturated at ceiling). Two readings, both live: (a) **substrate enrichment** -- give the release real authority over the latch (scale the hold with committed-run length, or convert to an active MECH-342-style maintenance-release pressure that drives the latch DOWN); (b) **test-design** -- both DVs need graded within-arm formulations. The 460f autopsy chose BOTH; **468e confirms the 460f reading via an independent DV.** This is convergent evidence for ONE substrate gap, not two independent bugs.

---

## Recurrence check (granularity-debt / `/claim-synthesis` trigger)

This is the latest in the SD-034 closure lineage (cluster 2026-06-12 -> -d 2026-06-13 -> 460e 2026-06-17 -> 460f 2026-06-18 -> 468e). 468e is **not a structurally-new signature**: it is the perseveration-side sibling owed from 460e, and it reproduces the 460f de-commit-authority gap through a different DV. So it is **convergent evidence for the one structural property** (de-commit authority magnitude), **NOT granularity debt** -- consistent with the 460e/460f autopsies; `/claim-synthesis` is not the route yet. **BUT the 460f watch-item hardens:** two independent DV instrumentations now fail at the same authority gap. The pre-registered tip-point stands -- **if the post-amend retests (460g / 468f) still fail with a structurally-different signature, route the SD-034 closure cluster to `/claim-synthesis`.**

---

## Learning extracted

- The beta-engagement coupling (460e fix) engages the **release** on every seed (468e C1 3/3, ON>OFF) -- engagement is no longer the blocker on the perseveration side, just as it was no longer the blocker on the de-commit-occupancy side (460f).
- The de-commit / release has the **correct sign** but **insufficient authority magnitude**: a release pulse near a contradiction does not drive `committed_frac_post` off the 1.0 ceiling against strong natural re-commitment. Same residual as 460f's swamped occupancy refractory.
- The C2 `committed_frac_post_absolute` DV **re-pinned at 1.0** -- the 468c->468e cap-pin escape (post/pre ratio -> absolute fraction) moved the pin from 0.85 to 1.0 but did not lift it. The DV needs a graded within-arm post-release formulation with real dynamic range. Not strictly degenerate (it can vary -- seed 44 OFF=0.0), so it scores; but it is measurement-weak for a partial de-commit.
- **claim_ids hygiene:** MECH-090 (active) must not be weakened by a C2-authority fail; the mechanism the run tests for MECH-090 is the latch *release* (C1), which passed. Mirror of the 460f MECH-261 mis-attribution.

## Repair pathway (user-confirmed routing)

`/implement-substrate` **amend** on the existing `commitment-closure-control-plane` substrate_queue entry (do NOT duplicate; it already holds the 460f de-commit-authority deliverable). 468e ADDS to that same amend:

- **(a) de-commit authority magnitude** -- shared with 460f: scale the de-commit hold with committed-run length, OR convert the de-commit into an active maintenance-release-pressure event (MECH-342 `CommitMaintenanceRelease`-style) that drives the latch DOWN rather than briefly blocking re-elevation, so a release near a contradiction actually lowers `committed_frac_post`;
- **(b) graded within-arm post-contradiction de-commit DV** -- replace the 1.0-saturated `committed_frac_post_absolute` with a graded measure that has dynamic range on the ON arm (time-to-recommit after a release event, or committed fraction in a tight post-release window), isolating the de-commit from the natural-re-commit baseline.

Retest gate (after amend): on >= 2/3 guard seeds with the coupling engaged, the graded post-contradiction de-commit measure drops on the ON arm AND ON < OFF on the (now-sensitized) statistic. Re-issue as **468f** (alongside 460g).

## Draft evidence_quality_note (governance applies; this skill does not write it)

> V3-EXQ-468e (supersedes 468d): the beta-engagement amend (use_closure_commit_beta_coupling) cleared both non-vacuity gates (foraging-contact 1.0; commitment-non-vacuity 1.0 -- ON committed AND contradiction fired 3/3), so the C1/C2 perseveration criteria drove a verdict. C1 (beta_release_near_contradiction) PASSED 3/3 with ON>OFF (43/16/58 vs 14/10/0) -- the MECH-268 dACC-saturation -> beta-release pathway works proximally. C2 (committed_frac_post_absolute ON < OFF) FAILED 3/3 because the ON-arm post-contradiction committed fraction is pinned at 1.0 on every seed (agent stays fully committed through the post-contradiction window despite the release; seed-44 ON=1.0 vs OFF=0.0 is a non-commit artifact, not de-commit). Autopsy (failure_autopsy_V3-EXQ-468e_2026-06-18, confirmed): same structural property as 460f via an independent DV -- the de-commit/release fires with correct sign but sub-threshold authority magnitude, and the absolute committed-fraction DV re-pinned at the 1.0 ceiling (the 468c->468e cap-pin escape moved 0.85->1.0 but did not lift). SD-034 -> non_contributory + pending_retest_after_substrate (substrate-limited: de-commit-authority magnitude + graded-DV power). MECH-090 -> non_contributory: its weakens is mis-attributed (script ties it to the C2-gated overall, but the run tests MECH-090's latch RELEASE via C1, which passed 3/3) -- protect the active claim; record C1 (latch releases under contradiction, ON>OFF) as a narrow non-scoring positive for its release semantics. MECH-268 -> supports (C1 3/3, narrow positive). Substrate amend: commitment-closure-control-plane de-commit-authority-magnitude lever (shared with 460f) + a graded within-arm post-contradiction de-commit DV; re-issue 468f alongside 460g.

---

## Routing decision (user-confirmed)

1. **substrate_queue `action=amend`** on `commitment-closure-control-plane`: append the 468e failure record + the graded-post-contradiction-DV deliverable (mechanism (a) de-commit-magnitude lever shared with 460f + (b) graded within-arm post-contradiction de-commit DV replacing the 1.0-saturated `committed_frac_post_absolute`). Status stays `amend_implemented_pending_validation`; `ready` stays false. (Governance applies; this skill does not write substrate_queue.)
2. **Evidence disposition (governance applies):** SD-034 -> `non_contributory` + keep `pending_retest_after_substrate`. MECH-090 -> `non_contributory` (mis-attributed weakens corrected; protect the active claim) + keep `pending_retest_after_substrate`; C1 release recorded as a narrow non-scoring positive. MECH-268 -> `supports` (C1 3/3, narrow non-promoting positive observation).
3. **pending_retest_after_substrate:** TRUE for SD-034 + MECH-090 (and via the closure cluster, the shared substrate) until the post-amend 468f re-queue returns a contributory PASS.
4. **Plan-node:** `commitment_closure:GAP-4` -- **reconciled this session** (the stale claim that blocked the 460f session is cleared): owner_exq advanced to record 468e run+adjudicated; `governance_2026_06_18b` note added; resume_condition repointed owed successors 460g + **468f** (468e is no longer "owed" -- it ran).
5. **Owed successors:** 460g (de-commit retest on the sensitized within-arm DV) + **468f** (perseveration retest on the graded post-contradiction DV) -- both gated on the `/implement-substrate` amend landing; separate `/queue-experiment` sessions. Do NOT re-author 460d/468d/460e/468e (superseded).

`commitment_closure:GAP-4` stays in-progress; closes when 460g + 468f return contributory PASSes on the amended substrate (subject to the MECH-342 v3_pending gate).
