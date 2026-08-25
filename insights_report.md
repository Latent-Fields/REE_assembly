# Project Insights — 2026-08-25

Generated: 2026-08-25T07:01:44Z
Recommendations fixed at: 2026-08-25T07:01:44Z (REE_assembly `git log --since="90 minutes ago"` showed only `igw-ledger: update` — no autopsy landed mid-run)

---

## Experiment Health

- **Total runs:** 223 (PASS: 81 | FAIL: 137 | ERROR: 5 | **error rate: 2.2%**) — window: 2026-07-26 → 2026-08-24, source: coordinator DB `results` + `experiments` on hub `ree@91.98.130.117` via `scripts/experiment_error_rate.py --days 30`.
  - **0 phantom completions**, 0 unexplained bookkeeping gaps, 0 operator cancellations — so 2.2% is a point estimate, not an interval.
  - PASS rate 36.3% (81/223).
- **Last ERROR recorded fleet-wide** (live per-machine `runner_status/` split, 9 files): `2026-06-11T21:18:10Z`. That split dedupes `completed` by queue_id and is a **numerator cross-check only** — it cannot supply the denominator, and it reported 0 ERROR entries in window while the DB recorded 5.
- **Unmeasurable bucket (stated, not estimated):** transient/infra crashes (exit `137/-9/-11/-15/143`, no sentinel) are intercepted upstream and retried in-queue. They leave no row in any table and are counted in no bucket above. A *deterministic* crash of that class retries forever and is invisible to every source.

**High-iteration chains (3+ lettered iterations), active in this window:**

| chain | iterations in window | outcomes | claim_ids |
|---|---|---|---|
| EXQ-861 | 9 (`.a b c d e f g h`) | 8 FAIL → **861f PASS** | INV-050, MECH-180 (861a/861d also MECH-122) |
| EXQ-836 | 6 (`. a b c d e`) | 6 FAIL | MECH-476 |
| EXQ-436 | 5 (`b c d e f`) | 5 FAIL | SD-017, ARC-045, MECH-166 |
| EXQ-603 | 4 (`r s t u`) | 4 FAIL | MECH-357 |
| EXQ-894 | 4 (`. a b c`) | 4 FAIL | MECH-074d |
| EXQ-906 | 4 (`. a b c`) | 3 PASS, 1 FAIL | (untagged) |
| EXQ-903 / 905 | 4 across two bases | 4 FAIL | MECH-075 |
| EXQ-228 | 3 (`b c d`) | 3 FAIL | ARC-032 |
| EXQ-828 | 3 (`. a b`) | 3 FAIL | INV-091 |
| EXQ-848 | 3 (`. a b`) | 3 FAIL | ARC-005 |
| EXQ-867 | 3 (`. a b`) | 3 FAIL | MECH-321 |
| EXQ-937 (+926a) | 3 | 1 FAIL → 2 PASS | MECH-449, ARC-107 |

All-time across 921 manifests: **448 distinct EXQ bases, 67 with 3+ iterations.** Deepest lineages are EXQ-603 (22 letters), EXQ-460 (15), EXQ-485 (14), EXQ-543 (12), EXQ-514 and EXQ-418 (11 each).

- **Recurring trouble spots** (claim_ids appearing in 2+ ERROR entries): **none.** The 5 ERRORs in window are V3-EXQ-870 (MECH-480), 821a (MECH-457), 918 (untagged), 926 (MECH-449/ARC-107 lineage), 944a (MECH-091) — five distinct bases, five distinct claim sets, no repetition.

- **Stalled chains** (FAIL with no successor): **None — every candidate chain has an autopsy, an owner, or a successor.**

  The Phase-A2 liveness check was executed per claim (not inferred) against all 15 claims carrying FAIL-only chains in this window: MECH-476, MECH-074d, SD-017, ARC-045, MECH-166, MECH-357, ARC-032, INV-091, ARC-005, MECH-321, MECH-075, MECH-471, MECH-091, MECH-236, MECH-480. **Leg 2 (autopsy coverage, searched by file CONTENTS, not filenames) came back non-empty for all 15** — range 3 autopsies (MECH-480) to 62 (SD-017). Several also cleared other legs: SD-017/ARC-045/MECH-166 carry a `done` task claim (IGW-20260823-229) and 2–3 commits in the last 7 days; MECH-091 and MECH-236 carry 6 commits each in 7 days. No claim came back empty on all four legs, so nothing qualifies as stalled.

- **Data-quality observations (verified, not inferred):**
  - **V3-EXQ-861f ran twice** — `20260823T210058Z` and `20260824T023853Z`, both PASS, two manifests on disk, two DB rows. Owned by open chip `chip-20260824-exq861f-duplicate-run-stale-claim-reap` (stale-claim reap mid-run).
  - **Rework volume:** of 921 manifests, 391 declare a `supersedes` field and 78 are marked `evidence_direction: superseded`.

---

## Substrate Bottlenecks

`evidence/planning/substrate_queue.json` — 161 entries. Counts below use the canonical boolean `ready` and `depends_on_unresolved` fields, not the free-text `status` field (which carries prose paragraphs on ~40 entries and cannot be tallied).

- **Ready: 79 / 161.** Of those, **exactly 1 is ready and not yet implemented**: `scaffolded-curriculum-hazard-rebalance` (1 failure record) — rebalance scaffolded_sd054_onboarding hazard-stage exposure. Every other ready entry is already implemented/validated.
- **Not ready with unresolved dependencies: 40.** Deepest dependency fan-in: SD-026 (5 deps), SD-027 (5), SD-033 (6+), SD-028 (5), SD-025 (3). Highest failure-record load among them: SD-049-PHASE-2 (fr=9), MECH-256 (fr=10, blocked on MECH-269).
- **Not ready with NO unresolved dependencies: 42** — these are gated on something other than a declared dependency (evidence, governance decision, or a `ready_blocked_by` note). Notables: `f_dominance_conversion_ceiling` (fr=26), ARC-062 (fr=11), ARC-065 (fr=8), SD-037 (fr=6).

**SDs with the heaviest failure records** (experiments that failed because the substrate was absent or incomplete) — 94 of 161 entries carry at least one:

| SD | failure records | state |
|---|---|---|
| `scaffolded_sd054_onboarding` | 28 | ready, implemented (603n PASS) |
| `f_dominance_conversion_ceiling` | 26 | not ready, no unresolved deps |
| `modulatory-bias-selection-authority` | 16 | implemented |
| `ARC-062` | 11 | phase 1 implemented, evidence-gated |
| `MECH-256` | 10 | candidate_v3_pending, blocked on MECH-269 |
| `v4_loop_segregation` | 10 | implemented, promotes nothing |
| `SD-016` | 9 | implemented |
| `SD-049-PHASE-2` | 9 | phase 2 implemented |
| `ARC-065` | 8 | ceiling lifted (569i PASS) |

Cross-referencing against the high-iteration chains above: the two heaviest failure-record nodes (`scaffolded_sd054_onboarding`, `f_dominance_conversion_ceiling`) are **not** the drivers of this window's FAIL volume — this window's repeat-FAIL chains (861/836/436/603r-u/894) are each already carried by a confirmed autopsy, and their substrate entries are implemented rather than missing.

---

## Governance State

- **Claims registry:** 1019 claims in `docs/claims/claims.yaml` — 751 `candidate`, 96 `provisional`, 68 `active`, 38 `open`, 21 `stable`, 17 `legacy`, 9 `candidate_substrate_landed`, 7 `implemented`, 5 `resolved`, 3 `retired`.
- **Claims pending V3 substrate (`v3_pending: true`): 239.**
- **Pending promotion/demotion decisions: 2** — `Q-094` and `Q-095`, both `hold_pending_v3_substrate`, both `pending_user`. 192 of 194 decision rows read `applied`. This backlog is genuinely small; the file's long tail is the "Decision Details" rationale section, not unapplied work.
- **Evidence superseded (rework): 78 runs** marked `superseded`; 391 manifests declare a `supersedes` link.
- **`pending_review.md` is stale and understates the true count — see Recommendations.** The file reads `Pending: **0** item(s) ... All experiments reviewed`, but it was generated `2026-08-22T13:45:22Z` against `last_review_utc 2026-08-22T13:23:53Z`, and **6 manifests have landed since and appear in neither `reviewed_run_ids` (2847) nor `discussed_experiment_dirs` (1189)**: `861g`, `861h`, `910b`, `946`, and both `861f` duplicates.

---

## Literature Coverage

- **Priority-1 backlog items still open: 0.** `evidence/planning/evidence_backlog.v1.json` (generated 2026-08-23T06:11:34Z) holds 417 items — 123 `high` priority, and **zero of them are `open`** (all `in_progress` or `covered`).
- **Total open items: 137** — all `medium` priority. Status split: 203 `in_progress`, 137 `open`, 77 `covered`.
- **Literature items in the backlog: 0.** `evidence_needed` reads `experimental` on 416 of 417 items; the single exception (`EVB-PINNED-Q019`, Q-019) has an empty `evidence_needed` and is already `covered`. **The backlog's literature channel is empty, not backlogged.**
- **Corpus:** 458 entries under `evidence/literature/`; newest are `targeted_review_q_095`, `targeted_review_q_094`, `targeted_review_inv_013`, `targeted_review_sd_099`.
- **Recent coverage (from WORKSPACE_STATE, in window):** 29 session blocks reference a lit-pull, spread across 2026-08-11 → 2026-08-24. The most recent scheduled run (`ree-lit-pull-am`, 2026-08-24T06:05:46Z) recorded **NO PULL — selector returned NONE_AVAILABLE, correctly**, which is consistent with the drained backlog channel above rather than with a broken selector.

---

## Human-Intervention Patterns

Derived from 583 dated session blocks in `WORKSPACE_STATE.md` covering 2026-07-26 → 2026-08-25.

**Tasks that recurrently required human input or repair:**
- **Git/coordination-plane repair — the dominant intervention class.** 179 of 583 session blocks (**30.7%**) contain at least one documented friction signature: `wedge` ×136, `skew` ×34, `throwaway worktree` ×26, `autostash` ×18, `swept` ×17, `read-modify-write` ×16, `index.lock` ×1. This is the single largest recurring draw on session attention in the window.
- **Metaworker dispatch supervision.** The window's session log is numerically dominated by `metaworker-dispatch` cycle entries from the two resident dispatchers (`ree-cloud-4-metaworker` ~cycle 733, `ree-cloud-5` ~cycle 3800). A recurring `STALLED` fleet-health false-positive required repeated human adjudication and is now itself chipped twice (`chip-20260822-metaworkerlearning-stall-coverage-gap-recurrence` records it as the second occurrence).
- **Queue refill.** The experiment queue reached depth 0 and required a human/chip decision about what to queue next — it does not refill itself.

**Low-friction, effectively headless:**
- **Failure autopsy.** 173 autopsy documents landed in the window with a median turnaround of 0 days (see `dual_insights_report.md`); coverage of this window's FAIL chains is complete.
- **Scheduled lit-pull.** Ran to completion and correctly declined to pull when nothing was available, with no intervention.
- **Producer ticks** (`proposal_routine_tick`, `hygiene_routine_tick`) ran clean across essentially every dispatch cycle in the log.

---

## Recommendations

Three of the four candidate actions this analysis surfaced are **already owned by open chips** and are therefore *not* recommended (gate 1 — recommending owned work sends a session to duplicate it). They are listed under "Already owned" below so the coverage is visible.

1. **Run `/governance` to clear the review-marking backlog and regenerate `pending_review.md`.** *(Verified unowned; gates 1–4 all pass.)*
   `pending_review.md` currently asserts `Pending: 0 — All experiments reviewed. Nothing pending.` while 6 manifests that landed after its 2026-08-22T13:45Z generation are in neither `reviewed_run_ids` nor `discussed_experiment_dirs`: `v3_exq_861g`, `v3_exq_861h`, `v3_exq_910b`, `v3_exq_946`, and both `v3_exq_861f` duplicates. Session Startup Protocol step 6 tells every session to consult this file before starting other work, so a stale "nothing pending" is a live blind spot rather than cosmetic drift.
   - *Gate 1 (liveness):* no open chip and no active TASK_CLAIMS entry covers `pending_review` or `review_tracker` regeneration (the single incidental chip hit, `chip-20260823-diagnose-v3exq944a-runner-error`, is about a runner error and does not own this).
   - *Gate 2 (right target):* the target is the governance review-marking step plus `scripts/generate_pending_review.py`, not a substrate node.
   - *Gate 3 (not applied):* `review_tracker.json` `last_review_utc` is `2026-08-22T13:23:53Z`, confirmed older than all 6 runs.
   - *Gate 4 (not brake-refused):* not applicable — this is a bookkeeping regen, not a claim iteration.
   - Note this is **not** a science backlog: 861g/861h/910b were autopsied on 2026-08-23. Autopsy deliberately does not mark runs reviewed; governance does. What is outstanding is the governance half, not the adjudication.

2. **No substrate-build recommendation this cycle.** The one ready-and-unimplemented node (`scaffolded-curriculum-hazard-rebalance`) carries a diagnosis of record — its `status` field states `diagnosis_done_NO_SUBSTRATE_CHANGE_WARRANTED_2026-08-08`, adjudicated and user-confirmed, with the real primary FAIL routed to G0 foraging instead. Recommending a build there would be recommending work an autopsy already found unwarranted (gate 2). No other node is both ready and unbuilt.

3. **No literature recommendation this cycle.** There are 0 open priority-1 literature items and 0 literature items of any priority in the backlog; the scheduled selector correctly returned `NONE_AVAILABLE` on 2026-08-24. Worth a governance look — but as a *question about the backlog generator*, not a pull: `evidence_needed` reads `experimental` on 416 of 417 items, so it is not currently established whether the literature channel is genuinely drained or simply not emitted by the generator. That distinction is `complex (probe-gated)`, and the probe is cheap; it is stated here rather than converted into a build task.

**Already owned — reported, not recommended:**
- *Queue empty.* `ree-v3/experiment_queue.json` has held `items: []` since 2026-08-23T21:04:19Z (~34h as of this report), and ran at only 1–5 items throughout the window. Owned by `chip-20260823-queue-refill-fresh-design`. The two pre-registered live gates in `hypothesis_space_registry.v1.json` are the natural fills for it: the **return-decomposition diagnostic** for `conversion_ceiling_root` (its declared `live_gate`, "1 discriminative experiment", not yet queued) and the **regime-matched re-test** for `e3_fdominance_causal_discrimination` (H1–H4 all undetermined behind the H0 selector-regime confound found by V3-EXQ-925).
- *Umbrella `scripts/` test corpus RED.* 8 files red on trunk, each individually chipped (`chip-scriptscorpus-dlaptop-*`): `test_count_inflight_workers`, `test_dev_doctor_worktrees`, `test_hygiene_routine_tick`, `test_ree_metaworker_heartbeat`, `test_ref_convergence`, `test_task_claim_amend_renew_orphan_guard`, `test_task_claim_mutation_lock`, `test_taskclaims_writer_lock`.
- *Duplicate 861f run* — `chip-20260824-exq861f-duplicate-run-stale-claim-reap`.
- *V3-EXQ-944a runner ERROR* — `chip-20260823-diagnose-v3exq944a-runner-error`.
- *`git-sync NEEDS_HUMAN: REE_Working`* — `chip-gitsyncverdict-dlaptop-ree-working`.
