# Dual-System Insights — 2026-07-26

Generated: 2026-07-26T14:00:17Z
Companion to `/insights` (REE_assembly/insights_report.md) — this report never edits
that skill or its output, and vice versa. (That report's own "pending decisions: 0"
stat was corrected to 12 while gathering data for this run — see its Correction
section, 2026-07-26T13:59:47Z.)

---

## REE-side (cognitive substrate)

**Competence-floor campaign (MECH-457 / INV-088 cluster, hero question `competence_floor`).**
17 hypotheses registered since 2026-07-13: **11 eliminated, 3 confirmed, 2 split, 1
alive.** This is the most heavily-fanned-out live question in the registry. Today's
run (V3-EXQ-819) attempted the newest leg (`H-zworld-trained-instrument` — does
competence lift now that the encoder actually trains, post-780 fix) but a non-vacuity
gate vacated it on a single near-miss seed; re-queued as **819a** (already queued and
claimed). Re-derive brake **does not fire** (0 `substrate_ceiling` readings under the
current R3 convention — the whole campaign reads `competence_implementation_gap` /
`measurement_test_design_defect`, i.e. real progress via elimination, not a stuck
loop). This is REE actually narrowing: 11 of 17 candidate mechanisms for
competence-retention are now ruled out.

**Conversion-ceiling campaign (F-dominance cluster, hero question `conversion_ceiling_root`).**
6 hypotheses since 2026-07-11: 2 eliminated, **4 still alive** — `H-observation-interface`
(the current live-root reading, per the 813 autopsy: latent-actor forages, raw-obs
actor doesn't) is the survivor after `H-policy-learning` was eliminated and
`H-objective-misspecification` displaced. Substrate-queue node
`f_dominance_conversion_ceiling` carries **26 failure-record entries** — the second
highest in the whole queue — but the selection-face half was already lifted
(MECH-448/449 built + validated + PROMOTED provisional, 2026-06-22); the residual is
squarely the observation-interface question, not an unowned pile of FAILs.

**High-iteration chains, by what they say about the mechanism (not who owns them):**

| Chain | Claim | Current status | Confidence trend across the chain |
|---|---|---|---|
| V3-EXQ-603 | MECH-358, SD-059 | `candidate`, v3_pending | holding — incremental substrate build (escape-affordance-bridge), not a confidence swing |
| V3-EXQ-514 | SD-049 | `candidate`, v3_pending | holding — 793a (today) closed `inconclusive`, no status change; real park is the foraging-competence prerequisite |
| V3-EXQ-460 | SD-034 | `provisional` | **gaining** — closure-commit-entry built + validated (460o/460p) |
| V3-EXQ-485 | SD-033b | `candidate` | holding/blocked — SD-033e successor built, co-blocked on V3-EXQ-724 |
| V3-EXQ-085 | MECH-071 `provisional`; SD-015 `candidate` (implemented); ARC-030 `candidate` | **gaining** — SD-015 substrate landed despite many `mixed`/`weakens` measurement iterations along the way |
| V3-EXQ-543 | ARC-062 | `candidate`, v3_pending | holding — `hold_pending_v3_substrate`, no movement |
| V3-EXQ-047 | SD-005 `implemented`; MECH-095 `candidate` | **gaining** — reached `supports` at 047k (TPJ routing, larger N) before continuing |

Three of seven chains are net-gaining ground on the actual mechanism despite heavy
lettering; the rest are genuinely holding on a real blocker, not silently stalling.

**Ready-and-unbuilt substrate:** re-checked fresh this run — still **0** of 55
`ready: true` entries. No REE-side buildable backlog exists right now.

---

## REE_assembly-side (governance throughput)

**Autopsy turnaround** (72 autopsies in the last 30 days with a resolvable
FAIL-landed → autopsy-generated timestamp pair, extracted from each autopsy's own
`Generated` header and earliest cited run-id timestamp): **median 9.8h**, fastest 0.2h,
slowest **1019.2h (42.5 days)** — `failure_autopsy_V3-EXQ-604c_2026-07-20`, a genuine
case, not a measurement artifact (spot-checked): the run PASSED on 2026-06-07 and sat
unexamined until a 2026-07-20 *retrospective* sweep for a systematic measurement-defect
class (D3 intra-run substrate divergence) caught it. The tail is a deliberate backward
sweep, not neglect — but it is real elapsed time between a result landing and it being
trustworthy.

**Decision backlog age** (`promotion_demotion_recommendations.md`, 12 `pending_user`
rows; age = git `-S<claim_id>` first-appearance proxy against the file, approximate):

| Claim | Recommendation | Approx. age |
|---|---|---|
| Q-084 | `hold_candidate_resolve_conflict` | ~118 days (since 2026-03-30) |
| MECH-329 | `hold_candidate_resolve_conflict` | ~43 days (since 2026-06-13) |
| MECH-457 | (fanout-driven hold) | ~16 days (since 2026-07-10) |
| SD-024 | — | ~5 days (since 2026-07-21) |
| ARC-112, INV-091, MECH-466, Q-081, Q-082, SD-076 | — | ~2 days (since 2026-07-24) |
| MECH-321, MECH-323 | — | <1 day (today's autopsy + this morning's lit-pull) |

Median ~2 days, long tail to 118. **The two worth naming specifically** (per the
skill's cross-reference step, below): Q-084 and MECH-329 are both
`hold_candidate_resolve_conflict` — the decision type that most needs an actual human
judgment call, not a routine promotion — and both have been waiting far longer than
the median.

**Claim churn** (`TASK_CLAIMS.json` — note this file is a *rolling, pruned* window per
its own housekeeping script, not a full history, so rates below describe the unpruned
window only): 41 entries on file, 11 active / 30 done. Opened last 7d: 40; closed last
7d: 30. **All 11 currently-active claims exceed the documented 6-hour staleness
threshold** (youngest 36.4h, oldest 189.7h / 7.9 days) — per
`feedback_heartbeat_stale_not_abandoned` memory, stale is not evidence of abandonment
(especially for Mac-local sessions), but it does mean the file currently offers no
signal distinguishing a live multi-day build from a forgotten claim; that
discrimination has to come from elsewhere (WORKSPACE_STATE, git activity).

**Concurrency friction rate:** of ~41 WORKSPACE_STATE entries in the trailing ~25-day
window (same tail `/insights` reads), **16 (~39%)** document at least one of the
signatures CLAUDE.md names as real friction (throwaway-worktree landing, a swept
foreign edit, read-modify-write contamination, HEAD/worktree skew, a stale
`index.lock`). This is the barrier-analysis number the framing memo asked for: shared-
trunk contention costs roughly 2 in 5 recent sessions actual landing friction, not
just "many sessions exist."

**Literature-pull cadence:** at least 4 identifiable pull sessions in the window
(2026-07-19, 2026-07-22 [10-search programme close], 2026-07-25 [Q-083/Q-084
scheduled], and **this morning** 2026-07-26 ~07:06–07:10 [MECH-321/MECH-323,
`targeted_review_connectome_mech_321`/`_323`] — not yet reflected in the WORKSPACE_STATE
tail `/insights` read). 45 `evidence/literature/` directories touched in the last 30
days total.

---

## Where the two overlap

**MECH-457 — a real REE-side ceiling, compounded by a REE_assembly-side hold.** The
competence-floor question is genuinely hard science (17 hypotheses, 11 eliminated,
still actively narrowing) — but it has also sat as a `pending_user` promotion/demotion
decision for ~16 days while multiple confirmed autopsies accumulated underneath it.
Worth distinguishing in any future recommendation: the *science* here is moving
normally; the *decision* about what that science means for MECH-457's claim status is
what's lagging.

**Q-084 — the inverse case: no hard problem left, just a stale decision.** REE-side,
this claim is already settled for now (`substrate_conditional`/v4, do-not-build,
confirmed by 2026-07-25 literature). REE_assembly-side, it's the single oldest item in
the entire decision backlog (~118 days, `hold_candidate_resolve_conflict`). There is no
science blocking this one — only a governance call that has never been made.

No other node this cycle shows both a real REE-side ceiling and REE_assembly-side lag
at the same time; the rest of the high-iteration chains and decision-backlog rows are
each slow for one reason, not both.
