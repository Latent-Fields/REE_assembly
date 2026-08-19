# Project Insights — 2026-08-19

Generated: 2026-08-19T16:56:36Z
Recommendations fixed against: REE_assembly `b77451c289` (2026-08-19T16:50:45Z) — `git log --since="1 hour ago"` re-checked immediately before writing the Recommendations section; the only non-heartbeat commits in that hour were `8c2bcc3356` (workset UI), `1bb8444cfb` (learned_cross_loop_arbitration DV-instrument addendum) and `d31cbb6086` (igw-ledger), none of which supersede anything recommended below.

---

## Experiment Health

- **Total classified runs: 268** (PASS: 89 | FAIL: 175 | ERROR: 4 | error rate: **1.5%**, upper bound **2.9%** with 4 phantom completions unclassified) — window 2026-07-20T11:21Z to 2026-08-19T14:24Z, source: coordinator DB (`experiment_error_rate.py --days 30`). The true rate lies in **[1.5%, 2.9%]**; quote the interval, not the point estimate.
  - Operator cancellations (deliberate `/queue/remove`): **0** — excluded from both numerator and denominator.
  - The 4 phantoms are all pre-2026-07-23 (`V3-EXQ-734b`, `734a`, `728a`, `699a`); no phantom has been recorded in the last **27 days**.
- **Corroborating per-machine split:** 0 ERROR entries recorded fleet-wide in-window (`runner_status/*.json`, 8 files read). `fleet_last_error_recorded` in that split remains 2026-06-11 — a slower-refreshing secondary source, not a contradiction of the DB figure (the frozen monolithic `runner_status.json` was not used, per this skill's forbidden-sources rule).
- **PASS rate moved the wrong way vs the last run.** 2026-08-08: 94 PASS / 186 FAIL / 281 classified (33.5% PASS). Today: 89 PASS / 175 FAIL / 268 classified (**33.2% PASS**). Flat, not degrading — but the *ERROR* rate rose from 0.36% to 1.5% (1 → 4 recorded ERRORs). All four ERRORs and all four phantoms predate 2026-07-23, so this is a window-boundary artifact (the 30-day window rolled *onto* an older cluster), not a new instability.
- **High-iteration experiments (3+ lettered iterations): 65 chains** across 910 manifests. The 12 largest, with last-manifest date and disposition:
  - **EXQ-603** — 22 iterations (`` … `u`) — SD-059/MECH-358 escape-affordance-bridge. Last run 2026-08-15. **Active** — the longest-lived chain in the corpus and still moving.
  - **EXQ-460** — 15 iterations — SD-034/MECH-260/261 → closure-commit-entry. Last 2026-06-24. Terminal PASS; resolved.
  - **EXQ-485** — 14 iterations — SD-033b/MECH-263 (OFC analog). Last 2026-06-22. Continues under new numbers (EXQ-696 lineage).
  - **EXQ-543** — 12 iterations — ARC-062/MECH-309/INV-074/MECH-334/SD-029. Last 2026-05-26. Migrated into the F-dominance conversion-ceiling campaign (EXQ-695/714/719/851/863/925/936 lineage).
  - **EXQ-514** — 11 iterations — MECH-436/SD-049 Phase 2. Last 2026-06-20. Terminal `supports`; resolved.
  - **EXQ-418** — 11 iterations — SD-016/SD-017. Last 2026-06-05. Explicitly parked (`parked_pending_env_entropy_precondition`).
  - **EXQ-689** — 10 iterations — MECH-448/449. Last 2026-07-24. Active cluster member; the MECH-449 leg continued today via **V3-EXQ-937b** (manifest `20260819T142133Z`).
  - **EXQ-654** — 10 iterations — ARC-062/MECH-309, CRF/F-dominance. Last 2026-06-22. Substrate entry closed ("no further CRF amend owed"); question migrated.
  - **EXQ-569** — 8 iterations — ARC-065/MECH-341. Last 2026-06-16. Terminal `supports`; ceiling lifted.
  - **EXQ-610** — 7 iterations — INV-074/MECH-313/333/334/341. Last 2026-06-08. Migrated.
  - **EXQ-445** — 7 iterations — SD-032b (DACC). Last 2026-05-08. Continues via the `dacc-cluster-862a-870a` autopsy → EXQ-870a.
  - **EXQ-836** — 6 iterations. Last 2026-08-01. Active.
- **Recurring trouble spots (claim_ids in 2+ ERROR entries): None** — 0 runner-status ERROR entries recorded fleet-wide in-window, so there is no per-claim ERROR distribution to read.
- **Stalled chains (FAIL with no successor queued): None.**
  This deserves an explicit caveat this cycle, because the naive test is now *trivially* satisfied: **`ree-v3/experiment_queue.json` currently holds 0 items**, so *every* chain in the corpus has "no successor queued" by inspection. The queue is empty because everything queued has **run** (the most recent completion, V3-EXQ-937b, landed at 14:21Z today), not because work was dropped.
  24 chains have a last manifest older than 2026-06-20. Five representative claims drawn from the oldest of those (MECH-204/EXQ-541, MECH-320/EXQ-563, MECH-342/EXQ-592, MECH-333/EXQ-610, SD-017/EXQ-418) were put through the full four-leg liveness check, and **not one came back empty on all four**:
  - `MECH-204` — 0 task claims, **23 autopsies**, 31 manifests, 1 commit in 14d → adjudicated + continued.
  - `MECH-320` — 0 task claims, **30 autopsies**, 43 manifests → adjudicated.
  - `MECH-342` — 0 task claims, **21 autopsies**, 18 manifests, 1 commit in 14d → adjudicated + continued.
  - `MECH-333` — 0 task claims, **25 autopsies**, 20 manifests → adjudicated.
  - `SD-017` — **2 task claims**, 56 autopsies, 68 manifests, 3 commits in 14d → owned, adjudicated *and* continued.
  A claim is stalled only if all four legs come back empty. None did.

---

## Substrate Bottlenecks

**The data-quality caveat raised in the 2026-08-08 report has NOT been resolved, and it has grown.** `substrate_queue.json` now holds **161 entries** (up from 146). It still carries three mutually-disagreeing readiness signals:
- a boolean `ready` field — **79 true / 82 false**;
- a structured `implementation_status` field — **`None` on 95 of 161 entries** (59% unpopulated, up from 57%);
- a free-text `status` field that has become the *de facto* record and is now unusable as a category: it has **41 distinct values across 161 entries**, of which several are multi-hundred-word narrative paragraphs pasted into the status slot (`scaffolded_sd054_onboarding`, `crf-availability-maintenance`, `f_dominance_conversion_ceiling` and `v4_loop_segregation` each carry a status string longer than this paragraph).

Any count below is therefore an **upper bound and a triage hint, not a build list**.

- **`ready: true` and no structured `implementation_status`: 34 entries** — an upper bound. Spot-checking immediately falsifies part of it: `modulatory-bias-selection-authority` (16 failure records) appears in that set but its free-text status reads `implemented`, and `crf-availability-maintenance` (5 records) reads "substrate amend is DONE... no further CRF amend owed". A `/implement-substrate` prioritisation pass trusting the structured field alone would go build already-built machinery.
- **No `implementation_status` and a named unresolved dependency: 68 entries** — e.g. `SD-033`/`SD-033c/d/e` (blocked on MECH-094/151/152/235/261/264/265), `SD-026/027/028` (blocked on INV-009/034/037/038, MECH-007/081/089), `MECH-256` (blocked on MECH-269, 10 failure records).
- **Top failure-record counts** (bottleneck signal independent of the `ready`/`implementation_status` ambiguity):
  - `scaffolded_sd054_onboarding` — **28** — implemented; readiness flipped true 2026-06-11.
  - `f_dominance_conversion_ceiling` — **26** — **not a build gap**: status text reads "cross-loop arbitration-reweighting route EXHAUSTED (709/711/713, autopsied 2026-07-05) — no new build owed". See `dual_insights_report.md`.
  - `modulatory-bias-selection-authority` — **16** — implemented; resolved via ARC-065/EXQ-569i.
  - `ARC-062` — **11** — implemented; active validation campaign.
  - `MECH-256` — **10** — genuinely blocked on MECH-269.
  - `v4_loop_segregation` — **10** — implemented; "V3_CLOSURE_REQUIRED… PROMOTES_NOTHING".
  - `SD-049-PHASE-2` — **9** — text corrected 2026-08-07; residual is downstream governance depth, not a build.
  - `mech457_competence_bootstrap_explorer` — **7** — `blocked_pending_discrimination` (see the hero-question state in `dual_insights_report.md`).
- **Highest-priority genuinely-unbuilt candidates** (`ready: true`, priority 1, free-text status not claiming implementation): `SD-047` (multi-source environmental dynamics, 2 failure records), `SD-048` (interoceptive noise dynamics, 0), `sd_actor_critic_action_learning` (1), `MECH122-CONTENT-PACKAGING-SPINDLE-SELECTION` (4), `SD-MECH267-CEM-SELECTION-FIX` (2), `SD-ORIENTING-DECISION-SCALE` (2), `SD-QUEUE-SEED-ENFORCEMENT` (2). Offered as a triage starting point, **not** as a verified build list — see Recommendation 2.

---

## Governance State

- Claims pending V3 substrate (`v3_pending: true`): **239** (was 235 on 2026-08-08; +4 in 11 days).
- Pending promotion/demotion decisions: **2 of 195** Decision Queue rows — `ARC-107` (`promote_to_provisional`, `pending_user`) and `MECH-152` (`demote_to_candidate`, `discussing`). 193 rows are `applied`.
  - **Both are genuinely aged, unlike the two open rows in the last report.** `ARC-107` first entered this file on **2026-06-20** (`95840b7ae3`) — ~60 days pending. `MECH-152` has been cycling in and out since **2026-04-01** (`2445c9105c`), most recently re-raised 2026-08-12 (`e6c643ee6a`). The 2026-08-08 report described its two open rows as "live, not aged debt"; that description does **not** transfer to this pair.
- Evidence superseded (rework): **339** manifests carry `evidence_direction: "superseded"` (was 76 on 2026-08-08 — a 4.5x jump that reflects a re-tagging sweep, not 263 new re-runs; the manifest corpus itself grew only from ~880 to 910).
- `pending_review.md`: **1** item pending — `v3_exq_936_mech439_f_variance_share_under_f_demotion` (PASS, 2026-08-17, MECH-439). Generated 2026-08-18T14:11Z.
- IGW workset: **235 items** — 160 blocked, 23 ready, 18 in progress, 11 assembling, 8 partial, 5 closed, 4 blocked-pending-substrate, 2 pending.

---

## Literature Coverage

- **Priority-1 literature backlog items still open: none.** `evidence_backlog.v1.json` (412 items, regenerated 2026-08-18T21:27Z) now lists **`evidence_needed: ["experimental"]` on 411 of 412 items and `[]` on the remaining one — zero items request literature at all.** That is a change from 2026-08-08 (3 literature-needed items) and it is worth naming explicitly: the backlog is no longer a source of literature-pull targets, so lit-pull demand is now driven entirely by governance/autopsy routing rather than by the backlog generator.
- Backlog status overall: 203 in_progress, 134 open, 75 covered; priority 127 high / 285 medium.
- **Literature-pull cadence is the healthiest signal in this report: 127 `targeted_review_*` directories landed in the last 30 days.** Most recent: 2026-08-19 (`sd_087`, `q_088`, `connectome_sd_005`, `connectome_mech_029`), 2026-08-18 (`q_093`, `mech_054`, `connectome_mech_186/053/033`, `arc_032`), 2026-08-17 (`q_092`), 2026-08-16 (`mech_467`, `connectome_mech_151`). The connectome sub-series is running as a systematic sweep rather than one-off pulls.

---

## Human-Intervention Patterns

Derived from the 70 date-stamped session entries in `WORKSPACE_STATE.md` since 2026-07-20.

- **Skill mix in the window** (from session headers): `/failure-autopsy` 9, `/session-land` 2, `/queue-experiment` 2, `/governance` 2, `/thought-digestion` 1, `/metaworker-dispatch` 1, `/lit-pull` 1, `/dual-insights` 1. The remainder are chip-driven repair/infrastructure sessions — which is itself the finding: **the majority of logged sessions in this window were coordination-plane repair, not science.**
- **Recurrently requires human input:** `/governance` Step 2/3 promotion-demotion decisions (the two aged rows above are exactly this — they sit `pending_user`/`discussing` because nothing else can close them), and `/failure-autopsy` Step 8 routing confirmation.
- **Low-friction, headless-safe:** `/lit-pull` (127 reviews landed with 1 logged session entry — i.e. almost entirely automated), IGW-automated sessions, and metaworker-dispatch cycles, which log as one-line CLEAR entries.

---

## Recommendations

*Fixed against REE_assembly `b77451c289` (16:50:45Z today); `git log --since="1 hour ago"` re-checked immediately before writing this section — nothing landed after that commit that supersedes any item below.*

1. **Close the two aged governance decisions — `ARC-107` (pending_user since ~2026-06-20) and `MECH-152` (discussing, cycling since 2026-04-01).** These are the entire Decision Queue backlog (2 of 195 rows) and both are now measurably old, unlike the pair in the last report. Gates: liveness — both rows still open in the 2026-08-18T21:27Z regeneration; correct target — this file *is* the routing artifact for these decisions, no autopsy names a different one; not already applied — both rows read non-`applied`; not brake-refused — neither is under a re-derive brake.
2. **Backfill `substrate_queue.json`'s `implementation_status` against its free-text `status` — this was Recommendation 2 on 2026-08-08 and it has since got worse, not better.** `None` count went 83/146 (57%) → 95/161 (59%); the free-text field now carries 41 distinct values including four multi-paragraph narratives. This is a **data-hygiene** finding, not a substrate build: a `/implement-substrate` pass trusting the structured field would be misdirected to at least two demonstrably-built entries (`modulatory-bias-selection-authority`, `crf-availability-maintenance`). Recommending it twice in a row is deliberate — the repeat is the evidence that it is not self-correcting.
3. **No literature-coverage action needed; instead, note that the backlog generator has stopped emitting literature targets at all.** 0 of 412 backlog items request literature, against 127 targeted reviews landed in the same 30 days. Lit-pull throughput is high and backlog-independent. Worth a governance decision on whether `evidence_backlog.v1.json` *should* still route literature, but that is a question to raise, not a defect to fix.

*No substrate-build recommendation is made from the high-iteration chains this run.* All 12 largest chains trace to a terminal resolution, an explicit documented park, or an active already-owned campaign; the five aged-chain claims put through the full four-leg liveness check all returned owners, autopsies or successors. *No stalled-chain finding is made* — and the reason the naive test would have produced a false positive this cycle (empty queue ⇒ every chain trivially "has no successor queued") is stated in Experiment Health above.
