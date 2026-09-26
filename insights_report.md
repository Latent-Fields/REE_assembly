# Project Insights — 2026-09-26

Generated: 2026-09-26T16:09:48Z
Recommendations fixed at: 2026-09-26T16:09:48Z (REE_assembly origin/master `a939bd88094`; `git log --since` re-checked immediately before writing)

> **Provenance.** Full `/dual-insights` run: every section below is re-measured this run (window 2026-08-27 → 2026-09-26, 30 days). This replaces the 2026-09-25 front revision (session `bt0925-insights`), whose lower sections were still the 2026-09-08 measurement. The front section keeps that revision's framing — the native learning loop — because nothing since has retired it; what changed is how far the campaign against it has got. Nothing here promotes or demotes a claim.

---

## Where the front moved since 2026-09-25

### The live front is still the native learning loop: ree_core now carries a default-OFF WakingTrainer, and the coupled-loop repair campaign is gating its members before the integrated acceptance run

The 2026-09-25 census finding stands: at REEConfig defaults ree_core does no waking gradient learning. What moved:

- **The trainer exists, default-OFF.** WakingTrainer skeleton + `harm_eval` member (`cc20be5`), E1 and E2-self members (T1, `d9a865e`), structured babbling source (W2a, `2ea0e3c`), grad-reach guard. Default behaviour is unchanged; nothing is switched on by default.
- **The repair is a campaign, not a queue item.** `evidence/planning/coupled_loop_repair_campaign_plan.md` is the plan of record (integration branch, user decision Q2). Its W3 (E2 world member) and W1-alt (action-space proposals) are built on the branch. A1, the integrated acceptance run, is **held** until the INT-CODEC and INT-ACT member gates pass (rec-20260925-38b81685).
- **Today's pass tests the earliest edge first.** `dynamic_control_discrimination_plan_20260926.md` (DCD2, `41cfe948414`) asks, before any bar, escape route or arbiter is built, whether the control signal carries the condition information at all (H-SV). Two families: commitment (probe C, Mac, pre-registered `4d9980b439a`) and freeze → release → veto (probe F = V3-EXQ-1109, running).
- **User decisions today** (campaign decision log, `f3dc47d8d0f`): 1105b queued as the W5 unblocker; H2/H3 probes on the Mac; ASP gate (c) gets a pre-registered seed extension; the MECH-280 LH-PAG override build is **parked until V3-EXQ-1109 resolves the freeze input**; EMA reset-init stays default-OFF for now.

## The live campaign — what the front rests on, and what is in flight

| run / record | role | state (domain) |
|---|---|---|
| **V3-EXQ-1078** (2026-09-23; autopsy confirmed 2026-09-24) | **1 (lead)** | The entry point of the pass, not a live run: "no loss reaches self_encoder". The evidence-domain stamp is anchored here (D2 for z_world use at E1 and E3, re-stated 2026-09-25). |
| **V3-EXQ-1109** — DCD2 probe F (freeze / veto earliest edge) | 2 | **Running** on ree-cloud-2 (claimed 2026-09-26T15:06Z). F0 decides whether `z_harm_a` tracks hazard proximity when the agent moves. If it does not, the freeze family is a signal-validity failure at the representation edge, and PAG recalibration, a release route or an arbiter would all be cosmetic. |
| **V3-EXQ-1105b** — grounded-valuation null detector re-validation v5 | 3 | **Queued** (ree-v3 `ff5266b`, pre-registration `386d88cfce1`). Supersedes 1105a. It is the W5 unblocker; W5a/W5b stay blocked until it passes. |
| **V3-EXQ-1108** — N2 replay encoder, full dose | 4 | **Done, autopsied** (`53e1291b04a`): neither reading stands; stored-z replay ruled out 5/5; re-encode at control parity. Routed to the orchestrator. |
| H0 reset-as-hidden-controller probe (Mac) | 5 | **MIXED** (`a939bd88094`): reset is the sole exit of the mode register (3/3 seeds, 37/37 exits); freeze leg omitted. |
| Probe C commit-gate discrimination; H2 / N5b shift detector; H3 learning-progress babble end (Mac) | 6 | **Pre-registered today**, before any registered seed (`4d9980b439a`, `f119a7408f2`, `a0e3916abe`). |

Nothing here is claimed as an outcome. The orchestrator `orchestrate-20260924-breakthrough-c2` owns sequencing.

---

## Experiment Health

- **Total runs:** 142 (PASS: 68 | FAIL: 72 | ERROR: 2 | **error rate: 1.4%**) — window 2026-08-27T18:47Z → 2026-09-26T10:02Z, source: coordinator DB via `scripts/experiment_error_rate.py --days 30`. **0 phantom completions**, so 1.4% is a point estimate. One operator cancellation excluded (V3-EXQ-1105, pulled as non-falsifiable by construction, redesigned as 1105a).
  - Down from 2.6% (4/152) on 2026-09-08. PASS rate 47.9% (68/142), about flat against 48.7%.
  - 115 distinct EXQ bases; **63% of runs are diagnostic** (up from 55%) — a front being localised, not tested.
  - Coordinator lifetime (since 2026-05-21): 820 results — 311 PASS, 502 FAIL, 7 ERROR.
- **Last ERROR recorded fleet-wide:** the tool's per-machine split is retired and reads "(none on record)". The two DB ERRORs are **V3-EXQ-591g** (diagnostic, ARC-019 precondition; superseded by 591h PASS) and **V3-EXQ-1066** (the script declares ARC-029). 1066 was not re-lettered: the driver is marked DO-NOT-QUEUE, and a claimed chip owns its diagnosis (per the 1070a autopsy). The 09-08 pattern "every ERROR re-lettered to a PASS within a day" no longer holds.
- **Unmeasurable bucket:** transient/infra crashes (exit `137/-9/-11/-15/143`, no sentinel) are retried in-queue and leave no row anywhere. A deterministic crash of that class would be invisible.

**High-iteration chains (3+ lettered iterations lifetime, active in window): 12** (17 on 09-08). `claim_ids` did not drift across letters in any of them, and no FAIL in them counts against its claim: the per-claim directions are non_contributory, inconclusive, mixed or superseded.

| chain | letters (lifetime) | in-window outcome | claims |
|---|---|---|---|
| EXQ-603 | 23 | **603v PASS** | MECH-357 |
| EXQ-861 | 10 | **861i PASS** | INV-050, MECH-180 |
| EXQ-436 | 8 | 436g FAIL | SD-017, ARC-045, MECH-166 |
| EXQ-591 | 8 | 591g ERROR → **591h PASS** | (diagnostic; ARC-019 precondition) |
| EXQ-822 | 7 | 822c PASS → d / e / f FAIL; 822g refused at autopsy | SD-078, SD-082 |
| EXQ-642 | 4 | a / b FAIL → **642c PASS** | (diagnostic) |
| EXQ-964 | 3 | FAIL, FAIL → **964b PASS** | MECH-482 |
| EXQ-1043 | 3 | 3 FAIL; further same-design letters refused | MECH-537 |
| EXQ-1057 | 3 | FAIL, FAIL → **1057b PASS** | MECH-017 |
| EXQ-571, 862, 871 | 3+ | one in-window run each | — |

New since 09-08: 1043, 1057, 964. Dropped out of the window: 906, 910, 937, 944, 228, 894.

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries): **none.**
- **FAIL volume is mostly not evidence against a claim.** Only about 5 of the 72 FAILs weaken or fail to support their claim. Top by count:
  - untagged diagnostics: 14
  - SD-082: 5 — only 1046 weakens it
  - SD-078: 3 — consumer failures sharing the tag (its own evidence reads supports via 806)
  - **SD-106: 3 — a real weakening**, stated in its evidence note
  - SD-032a: 3, all non_contributory; continues as 1109
  - MECH-537: 3 — a clean mixed result with every readiness gate green
  - MECH-017: 3 — resolved by 1057b PASS
- **Stalled chains:** **None — all candidate chains have an owner, an autopsy, or a successor.** 52 candidates: 50 whose latest letter is a FAIL with no successor letter, plus 963a (963b refused at red-team) and 1105a (1105b queued). That is up from 14, driven by the dense 09-14..09-26 diagnostic wave. The four-leg liveness check was run per candidate. Leg (b), autopsies searched by contents, is non-empty for **all 52**: 38 have their own autopsy and 14 appear in a cluster autopsy. Classified: **continued 18** (e.g. 822f → 1028/1029, 1030 → 1093, 1048 → 1057b, 1067/1107/1090 → 1109), **owned 20** (an open chip names the run), **adjudicated 12**. The thinnest rest on the autopsy alone: 862b, 959, 971, 994, 991 and 999a. No re-derive brake fired in the window. Autopsies explicitly refused further same-design letters for 822g, 935b, 1043 and 1039b.
- **Rework volume (lifetime):** 4,792 manifests (3,005 run-pack + 1,787 flat). **370 carry `evidence_direction: superseded`** and 516 declare `supersedes` (272 / 432 on 09-08). File mtimes are checkout times, so an in-window split is not measurable.

---

## Substrate Bottlenecks

`evidence/planning/substrate_queue.json`: **268 entries** (177 on 09-08). 96 `ready: true`, 172 not. 17 implemented in the last 30 days, including today's MECH-268 dacc-PE scale normalisation (`c41f9d1`) and the MECH-288 slow-scale BOCPD rail (`1d66991`, `22aadc0`). 130 of 268 carry a failure record; the newest is dated today.

- **Ready and not built: 5** (plus 3 registration-only entries, which are not build-authorised):

  | entry | priority | owner at generation | note |
  |---|---|---|---|
  | `MECH-279` (PAG freeze gate amend) | 1 | IGW-20260926-214, staged 14:20Z, chip open | its own hint names a confirmer "before relying on it"; that confirmer is V3-EXQ-1109, running now (see Recommendations) |
  | `suffering-derivative-comparator-refractory` (SD-050 event latch) | — | IGW-20260924-224, launched manually | in flight; its first commit was withdrawn today for sitting on a stale base and is being re-committed |
  | `sd036-eval-replicate-determinism` | — | IGW-20260925-221, staged, chip open | — |
  | **`noop-class-defaults-up`** | **2** | **none** | registered today by governance (GFLAG-0508 resolution). Six `*_noop_class` defaults still point at class 0 (UP); severity "degrading"; design-first |
  | `spcem-onmanifold-floor-token` | 3 | none | severity "cosmetic" (the floor fires on 0.8% of states at dim 32) |

- **Blocked:** 172 not ready; 51 carry a populated `depends_on_unresolved`, and some of that text is stale.
- **Failure-record load:** the heaviest nodes are unchanged from 09-08 (`scaffolded_sd054_onboarding`, `f_dominance_conversion_ceiling`, `modulatory-bias-selection-authority`). None of this window's repeat-FAIL chains names a missing build as its cause.

---

## Governance State

- **Claims pending V3 substrate:** `v3_pending: true` on **269** (261 on 09-08) of 1,215 claims.
- **Pending promotion/demotion decisions: 0.** 299 decision rows, all applied (MECH-535 / 536 applied since 09-08). The file is `evidence/experiments/promotion_demotion_recommendations.md`.
- **Governance flags: 561 total — 530 resolved, 27 superseded, 4 open** (114 open on 09-08). The backlog has drained: this week's governance cycles resolved batches of 74/86 and 13/16 with user sign-off. The 4 open are all `evidence_discrepancy`, and the oldest is 2 days old: GFLAG-0453 (MECH-094 / ARC-065), 0454 (SD-081 / MECH-477), 0503 (MECH-033), 0561 (the GFLAG-0508 scoring-triage successor, 8 claims).
- **`pending_review.md`: 0 items.**
- **Stale registry text found this run, not flagged:** `conversion_ceiling_root` (the hero question) has a `live_gate` that still reads "QUEUED as V3-EXQ-1010 ... RUNNING ... H-F alive". 1010 ran on 2026-09-09, H-F is confirmed, and the child question `zworld_actor_adequacy_locus` is closed to fan-out (2026-09-23) with 0 alive hypotheses and `decided_utc` still null. The `/progress` dashboard shows this `live_gate` as the hero's gate line, so it displayed a gate the front had moved past. *(Fixed after generation, 2026-09-26T16:22Z — see Recommendation 4.)*
- **Closure:** v3 weighted progress **72.3%**, 34 nodes remaining (73.0% / 33 on 09-08).
- **`TASK_CLAIMS.json`** keeps about 2 days (21 active, 4 stale by the 6 h rule at generation). The materializer's lifetime counter is about 3,020 claims (1,161 on 09-08), roughly 100 claims a day.

---

## Literature Coverage

- **Priority-1 backlog items still open: none.** None of the 114 high-priority items needs literature.
- `evidence_backlog.v1.json`: **458 literature-needed items (440 open, 18 in progress)**, down from 510 on 09-08. This is the first shrink since the generator started emitting literature items (08-25).
- **Corpus:** 611 entries under `evidence/literature/` (509 on 09-08, about +5.6 a day). 143 were touched in the last 30 days.
- **Covered in recent sessions:** 132 `lit-pull` commits in 30 days, touching about 219 claim ids. The last 7 days (IGW-driven): MECH-110, ARC-116 / 117, MECH-109, MECH-084, MECH-080, ARC-114, MECH-082, INV-069, ARC-136 / 111 / 109, MECH-452, ARC-103 / 104 / 105, ARC-099 / 100, MECH-066 / 067, ARC-098.

---

## Human-Intervention Patterns

From the newest 93 dated `WORKSPACE_STATE.md` entries (2026-09-25T09:04Z → 2026-09-26T15:12Z). `WORKSPACE_STATE.md` is written newest-first, so this run read the top of the file. The skill's "last 200 lines" instruction reads the oldest surviving entries instead; see Recommendations.

- **Tasks that recurrently required human input:**
  - **Breakthrough-campaign design forks** — the dominant driver now. Numbered open questions (U/O/Q) run through nearly every `bt09xx` entry; today's held-list review settled seven (a)–(g) in one pass.
  - **Governance batch approvals** — two large flag-resolution batches this week (74/86, 13/16), each needing explicit sign-off.
  - **Usage-limit and capacity checkpoints** — the 4 `NOT LANDED:` entries all trace to one orchestrator budget stop (09-25 10:50Z); 3 of the 4 later landed.
- **Low-friction headless tasks:**
  - **lit-pull** — 1–2 sessions a day, IGW-driven, no friction observed.
  - **metaworker Healer cycles** — 5 of 5 ran headless (2 found a skew and auto-repaired it). On 09-08 this family was the largest human-touch category.
  - **failure-autopsy** — confirmed and applied without pause; only the governance disposition needs the user.
  - **thought-digestion / ingestion** — batched, few per-item touches.
- **Concurrency friction:** 5 of 93 sessions (about 5%) show a genuine hit: 2 Healer skew repairs (ree-cloud-5 third recurrence; ree-cloud-4 stale-staged-revert discard), 1 validation-cache index skew, 1 fleet-capacity stall, 1 claim-arbitration deferral. That is not comparable to 09-08's 42.8%, which came from a 605-entry, 30-day window. It is also after the fact: today's shared-checkout incident (a `ree_commit` push-retry leaving staged reverts in the ree-v3 index, and a stale rebase lock) is not yet logged there.

---

## Recommendations

1. **The gate is the coupled-loop repair campaign's integrated acceptance run A1, held until the member gates pass and the W5 null detector re-validates (V3-EXQ-1105b, queued)**. The orchestrator `orchestrate-20260924-breakthrough-c2` owns the sequencing, and today's user decisions set the next steps (campaign plan decision log, `f3dc47d8d0f`). **No new action is recommended here.** Adding one would duplicate owned work.
2. **Build `noop-class-defaults-up` (`/implement-substrate`, design-first).** Priority 2, severity "degrading": six `*_noop_class` defaults still send the agent UP whenever their mechanism emits a no-op. That is the GFLAG-0508 defect class which `1fc8816` fixed only for the PAG freeze and orienting. Gates: no IGW entry, chip or task claim names it (checked 16:05Z); governance routed it today, so the target is right; unapplied; no brake. It needs a design choice (default to the stay class behind a contract, or require the class per driver), not a silent default edit.
3. **Hold the MECH-279 amend until V3-EXQ-1109's F0 leg reads.** IGW staged it at 14:20Z, 40 minutes after the DCD2 plan stated that if `z_harm_a` is input-insensitive, "MECH-279 amend is then the wrong target". The amend's own hint names a confirmer "before relying on it", and 1109 is that confirmer, running now. The user already parked the sibling MECH-280 build on the same condition. Clicking the open chip `chip-igw-214-substrate-ready-mech-279` before 1109 reads risks building against the wrong edge.
4. **`/governance`: re-state the hero question's `live_gate`** (`conversion_ceiling_root` still reads "V3-EXQ-1010 RUNNING, H-F alive"), and record the decision on `zworld_actor_adequacy_locus` (closed to fan-out 2026-09-23, 0 alive, `decided_utc` null). The `/progress` dashboard's hero gate line shows it.
   **Done after generation (2026-09-26T16:22Z, user-instructed):** the locus decision is recorded (`decision_log.v1.jsonl@2026-09-26T16:22:29.678100Z`, scope: locus only), and the root question's `live_gate` / `distance_phrase` are re-stated in `hypothesis_space_registry.v1.json` with a `decision_note` naming the prior text. `hypothesis_space.v1.json` and `CURRENT_FRONT.md` were regenerated.

**Considered and not recommended:**
- **Fix this skill's Phase A1** to read `WORKSPACE_STATE.md` from the top (it is written newest-first). This is a standing-rule change, so it needs a GOV-HELDOUT-1 check; offered as a follow-up rather than done in a read-only run.
- **`spcem-onmanifold-floor-token`:** cosmetic; the interim reporting rule covers it.
- **Stale metaworker rows** (`ree-cloud-4-metaworker`, `ree-cloud-5`, "dispatching", about 41 h): the open chip on the dispatcher-pause review point covers them.
- **SD-106's real weakening:** it is autopsied and routed; no further action from here.
