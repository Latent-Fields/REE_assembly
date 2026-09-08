# Wave 6 -- campaign programme: consolidate and complete the open IGW + chip-ledger work (2026-09-08, evening)

**Status: PLAN OF RECORD. Ledger actions in section 6 applied by the writing session. Section 7 lists the decisions only the user can make; nothing in sections 2-5 is gated on them except where a row says so.**

- Written: 2026-09-08T19:42Z-20:10Z by session `campaign-w6-20260908` (Mac `DLAPTOP`, main checkout; `TASK_CLAIMS` claim `campaign-w6-20260908`). No experiment was queued by this session.
- User instruction: look at another campaign-based consolidation and completion of the available IGW and spawn_task ledger jobs.
- Sources read: `igw_routine_ledger.json` (190 entries: 105 completed, 81 completed_resumable, 1 staged, 3 spawn_failed; 139 dispositions; tick NOT paused, hourly, last two ticks "no eligible item"), `igw_routine_tick.py status` (27 ready / 24 spawnable / 3 suppressed by permanent disposition), `inter_governance_workset.v1.json` (19:00Z: 245 items; ready lanes = 20 plan-reconcile rows the tick skips, 5 experiment, 1 lit, 1 ops), `igw_assignments.json` (471 rows, 0 live), the LIVE chip ledger via `chip_ledger.py list --status open --live` (78 open at 19:47Z, down from 111 at 07:13Z; 61 resolved today = 52 done + 9 withdrawn; 6 claimed by live sessions), `hold_lane.v1.json` (45 held, review 2026-09-11), `TASK_CLAIMS.json` (13 active at 19:42Z, all W5 science sessions or their reservations), `pending_review.md` on ORIGIN (15:31Z: **0 pending**), `ree-v3/experiment_queue.json` on origin (0 pending, 2 claimed: V3-EXQ-1010 on DLAPTOP, V3-EXQ-1011 on ree-cloud-3), FLEET_STATUS (19:41Z: hub daemons all CURRENT), `substrate_queue.json` (SD-018 amend `amend_implemented_pending_validation`, ready=True), `CURRENT_FRONT.md` (07:23Z), `ref_convergence.py --dry-run/--audit` on REE_assembly.
- Predecessor: [`science_wave_campaign_plan_20260908.md`](science_wave_campaign_plan_20260908.md) (wave 5, written 07:05Z today). Its execution record is section 0 here.

---

## 0. What happened in wave 5 (facts, 2026-09-08T07:16Z -> 19:45Z)

| Wave-5 lane | Outcome |
|---|---|
| HK-G / HK-F / HK-I (Sonnet subagent bundles) | **16 of 18 landed by 07:56Z**, ~370-410k tokens per bundle. Leftovers: `chip-20260901-igwworkset-md-mergegap` (blocked by a concurrent claim, now free -- first pick below) and the scripts-corpus sweep, routed to `/metaworker-learning` (`chip-20260908-scripts-corpus-timeouts-learning`, in flight; root cause = launchd ProcessType Background; decision chip `chip-20260908-scriptscorpus-qos-decision` raised 19:32Z). |
| HK-E registry bookkeeping | **6 of 6 done** (18:40Z). WI-1 dropped-record recovery ALSO landed (`ree-v3 dedcc2ce24`, 255/155 records, link audit 255/255/0) -- only its test pin is still owed. settings.local wildcard remainder done (18:28Z). |
| HK-H fleet ops (Opus healer) | **6 of 6 done** (18:55Z): hub daemons restarted once with the OPERATOR_GUIDE pre-flight (all CURRENT), deployed-script drift detector built (hygiene source 29), cloud-5 GC 154 swept (worktrees 430->276), cloud-4 failsafe race fixed. Decision chip `chip-20260908-decision-daemondrift-class-drift-aware-restart` OPEN. A fresh `chip-metaworkergc-sweep-79-*` fired at 18:51Z (must run on its own box). |
| L literature bundle | **4 of 4 done** (19:01Z): 31 entries, verify-and-bank only; seven findings owed to `/governance` recorded in the WORKSPACE_STATE entry. |
| S2a queue-fill | **0 of 4 queued -- all four REFUSED WITH A RECORD** (884a: MECH-428 C1 cannot fail; 997a: FUSED arm has no substrate path; ARC-021 H2: MERGED arm crashes on step 2, new defect; 642d: two of six repairs not instantiable). GFLAG-0227..0230. The one unblocked leg was chipped and then queued by the fresh-fill session as **V3-EXQ-1011** (ARC-021 H3, running on ree-cloud-3). |
| S2b queue-fill (live, `angry-pascal-6fd799`) | Pre-flight 17:27Z (3 GREEN, 999a AMBER). **V3-EXQ-1013** (SD-031 portfolio) queued and already ran (manifest 19:09Z, unreviewed); 822f, 999a and the 983 repertoire spike are in flight with slot reservations. |
| S1 z_world front (live) | Fresh-fill session queued **V3-EXQ-1010** (1008's over-capacity decoder sweep, running on DLAPTOP) and 1011; **V3-EXQ-1012 BLOCKED** (E3 commensurability rung-3 readiness target is tautological, `088fbec4c9`) and **V3-EXQ-1007a BLOCKED** (C1 satisfied by construction, `cc863e458b`). `xenodochial-austin-8c5984` is landing **V3-EXQ-1015** (MECH-465 warmup-budget dispersion sweep, item 3). Items 4 (SD-018 amend validation -- the amend itself is implemented, `amend_implemented_pending_validation`, ready=True) and 5 (regulatory anchoring matched-aux) untouched. |
| S4 zero-compute closure | Item 1 **done** (SD-056 confirm ADJUDICATED DO-NOT-QUEUE, `00ac2f910e`). Items 2-4 released, campaign chip open/unclaimed. |
| Governance | Cycle `governance-20260908-0703` closed 15:38Z: 6 results walked to **0 pending**; one inline autopsy (1007). Pause-pressure trial FIRED again, NOTED not actioned. The IGW tick was resumed (Paused: False). |
| Coordination plane | REE_assembly shared checkout **WEDGED from 16:56Z** (ahead 35 / behind 45; every W5 session cherry-picked through throwaway worktrees). **Cleared 19:50Z by this session**: per-commit content audit of the 9 unproven shas (8 false negatives or superseded derived regens, 1 genuine strand = five IGW log lines from the tick's 19:06Z commit TIMEOUT, cherry-picked as `0a4c13f9ee`), then `safe_adopt_ref.py --allow-discard` of all 35; skew repair materialised 5 never-written files and discarded 14 armed staged reverts. Two tooling defects found on the way are chipped below. |

Fleet: DLAPTOP running 1010, ree-cloud-3 running 1011 (scaler woke it), cloud-4 offline, cloud-5 heartbeat stale ("dispatching", 140h). Hub daemons CURRENT. Dispatchers STOP. Queue 0 pending / 2 claimed.

---

## 1. What the ledgers actually hold now, and where the tokens go

**Chip ledger (live, 78 open):** 6 claimed by the two live science sessions (S1/S2b and their member chips); 45 in the hold lane until 2026-09-11 (substrate builds, proposal-exp chips, the three audit chips, HK-D coordination-plane residue, two Remote-Control research sessions); 4 decision chips; 1 GC-sweep chip that must run on its own box. That leaves **22 open, unclaimed, un-held chips** -- the whole available spawn_task backlog -- and every one of them is placed in a bundle or a click lane below.

**IGW ledger:** the tick's own re-spawn class is closed (W4 HK-A) and its outcome mix is 111 USEFUL_LANDED / 49 NO_OP / 19 DUPLICATE / 4 ERROR. Nothing in it is an un-owned job: the 81 `completed_resumable` rows are finished sessions kept resumable, not work; the 3 `spawn_failed_no_session` are pre-HK-A. The live residue is (a) **one staged item**, `IGW-20260831-225` (`/implement-substrate` for `sd_epistemic_deficit_multitarget_readiness`, MECH-482), staged 8 days because the skill requires human assent -- a section 7 decision; (b) three spawnable experiment proposals (INV-104, INV-095, MECH-002) that the last two hourly ticks did not spawn ("no eligible item") -- a gate verdict, checked in section 2 HK-J; (c) 20 plan-reconcile rows the tick skips by design (V4+/prose items) -- not a lane. **So the IGW side needs one decision and one diagnosis, not a campaign.**

The three levers of wave 5 still hold (Sonnet bundles for housekeeping; pace science by governance cadence; fill the starved queue). Two things moved today: the queue-fill lane turned out to be **refusal-bound, not compute-bound** (4 of 4 S2a successors refused, 2 of 4 fresh-fill designs blocked -- each refusal is a correct, recorded outcome and costs an Opus session), and adjudication is CLEAR (0 pending on origin), so the pacing gate is wide open: **queue freely up to six un-adjudicated results.**

---

## 2. Campaign HK -- housekeeping, Sonnet bundles (supervised subagents; launched by this session)

Each bundle: one Sonnet subagent of `campaign-w6-20260908`, <= 6 items sharing a class, own `TASK_CLAIMS` claim, per-item STOP-CHECK, `chip_ledger.py claim` on start, land each item separately with `ree_commit.py --push` (the checkout is converged -- direct pushes work again), resolve the member chip as it lands, targeted tests only. Excluded from every bundle: `experiment_queue.json` (two live queue sessions), `evidence/experiments/**` regen (indexer left to the next governance run).

| Bundle | Class | Items (member chips) | Launch |
|---|---|---|---|
| **HK-J** coordination-plane scripts | `scripts/` writers and gates | `chip-20260901-igwworkset-md-mergegap` (W5 first pick), `chip-20260908-ree-root-resolver`, `chip-20260908-autopsy-step2a-dry-check-runid-shape`, `chip-20260908-pending-review-degenerate-evidence-pass`, `chip-20260908-refconv-suggested-adopt-line-incomplete` (NEW: `ref_convergence.py`'s printed `safe_adopt_ref --allow-discard` recipe lists only the UNPROVEN shas, but `safe_adopt_ref.py` proves by sha alone and refuses the 26 patch-id-proven ones too -- the printed recipe cannot be followed), `chip-20260908-ree-commit-push-retry-worktree-leak` (NEW: four `$TMPDIR/ree_commit_push_*/wt` throwaway worktrees left registered on REE_assembly from today's failed push-retries, none live). Plus a READ-ONLY diagnosis: why the tick reports "no eligible item" against 24 spawnable (run `claim_queue_gate_reason` / `item_untestable_reason` for INV-104, INV-095, MECH-002 and record the verdicts in the WORKSPACE_STATE entry). | Sonnet subagent, now |
| **HK-K** registry / claims bookkeeping | narrow field writes on `claims.yaml`, proposals, docs | `chip-20260908-revalidate-unblocked-proposals-160-236-465`, `chip-20260908-arc047-substrate-sufficiency-caveat`, `chip-20260908-digest-apply-gov-equiv-sharpen`, `chip-20260903-impl022-uncertainty-nondissipation-field`, `chip-20260901-gflag0091-unblocks-claims-edge-repair`, `chip-20260908-mutlegib-citation-fixes`; budget permitting `chip-20260904-refwedge-r1-rate-cost-remeasure`, `chip-20260905-inv077-reaudit`. No status/confidence change anywhere; a `task_claim.py open` exit 3 on `claims.yaml` means skip that item and report. | Sonnet subagent, now |
| **HK-L** ree-v3 harness + substrate-adjacent code | `ree-v3/experiments/**`, `ree_core` module stubs, docs tests | `chip-20260908-contextmemory-harness-encoder-gradient` (science-critical: unblocks the MECH-152 redesign and the V3-EXQ-939 decision), `chip-20260907-dv-floor-control-check-2b`, `chip-20260827-capability-contract-plasticity-vocab`, `chip-20260908-wi1-substrate-split-dropped-records` (recovery landed `dedcc2ce24`; ONLY the test pin remains). Contracts on a cloud worker via `remote_pytest.sh`, never on the Mac. | Sonnet subagent, now |

Verification for the campaign: after HK-J lands, the coordinator (or the next session) runs `scripts/run_scripts_tests.sh --changed` from the MAIN checkout and records the red count against the 8 FAIL / 14 TIMEOUT daily baseline (the daily run's reds are the ProcessType Background class, decision chip pending).

---

## 3. Science campaigns

Pacing rule unchanged from wave 5: queue freely while un-adjudicated results on ORIGIN are <= 6 (now 1: V3-EXQ-1013, plus 1010/1011/1015 when they land); prefer `experiment_purpose: evidence`; every session declares `dv_headroom` where a range is measured; red-team in the FOREGROUND. Two queue sessions are live (`angry-pascal-6fd799` S2b, `xenodochial-austin-8c5984` S1) -- a new queue session must reserve its EXQ id with its own `task_claim.py open` on `ree-v3/experiment_queue.json/V3-EXQ-<id>` and re-verify the next free id across queue, experiments/ and evidence/.

### S5a -- zero-compute closure remainder (`chip-20260908-w5-s4-zero-compute-closure` items 2 + 4) -- Opus subagent, launched now

| # | Item | Note |
|---|---|---|
| 1 | `chip-20260908-inv092-falsifier-panel-refinement` + `chip-20260908-inv093-suppression-sibling-readiness` -- `/claim-synthesis` over the 09-08 INV-092 lit-pull (four concrete falsifier corrections; mirror to INV-093), then the INV-093 substrate-readiness verification pass (EXP-0717 is already blocked_substrate on origin -- verify, do not re-mark). One session, both chips. | `claims.yaml` narrow edits; no status change |
| 2 | `chip-20260905-mech095-sd047-valid-retest-design` -- design artifact only (why each prior attempt was invalid; the valid retest). | writes `evidence/planning/` only |

### S5b -- design-gap lane (`chip-20260908-w6-s5b-design-gaps`) -- Opus, click

`chip-20260903-exq981a-mech027-requeue` (check the inverted hazard-band assignment FIRST; the 09-04 record lists three source-verified blockers), `chip-20260903-exq991-redesign-action-level-dv` (pick an action-level readout with demonstrated free-policy range, measure the range, derive C1 from it), 963b's SD-105 freeze/share API (registration only). Each ends in a ratified design + queue write, or a refusal with a record. Queue writes allowed (pacing gate open); reserve ids as above.

### S6 -- successor tail + S1 item 5 (`chip-20260908-w6-s6-successor-tail`) -- Opus, click, after S2b lands

| Item | Gate / note |
|---|---|
| `chip-20260905-waypoint-consumer-reach-portfolio` | DESIGN FIX only first -- the corrected H2 fails its own headroom gate; read `2a67c36dcf`, `8bd564d9ff`, `0c74ba26d2`, and `exq_wpfield_h2_dv_range_probe_20260907.md` before touching the driver |
| `chip-20260901-gflag0080-mech235-arbitration-rerun` | none; cheap (re-run with the harm signal logged) |
| `chip-20260904-regulatory-anchoring-matched-aux` (S1 item 5) | 1008's result is on origin; "matched" must match content-at-encode, not geometry. Skip if `xenodochial-austin-8c5984` has taken it (check its claim history first) |
| `chip-20260904-arc046-infant-zgoal-reachability-probe` | >= 1500 ep; only if ARC-019 is wanted this month (budget) |
| S1 item 4: SD-018 amend validation contrast | the MECH-535 direction-blind ambitendency ON/OFF on 978's boards IS the validation; design once the 1010 result is adjudicated |

### Not a campaign: held (unchanged, review 2026-09-11)

The 45 `hold_lane.v1.json` entries stand: substrate builds (`mech035`, `mech494`, `mech039`, `mech037`, `mech065`, `mech468`, `mech157`, `mech320`, `zgoal-parent`, `arc131`, `mech057b`), the 8 `chip-proposal-exp-*` + 3 `-paced`, the three audit chips, HK-D residue, `sleep-integrated-world-model-update-validation`, `compute-ledger-v2`, `mech267-persist-injection-state`, `intake-hygiene-register`, the two Remote-Control research sessions, `queue-causal-sleep-matched-arm`, `mech152-redesign-queue-gated` (governance decides on 972a; HK-L item 1 is its substrate prerequisite). `chip-20260907-flag-registry-commit-time-gate` stays decide-or-leave.

---

## 4. Decision lane and metaworker routing

- **Decision chips** (raise as real `AskUserQuestion`s in the next user-present turn): `chip-20260908-scriptscorpus-qos-decision` (recommend A: ProcessType Interactive, keep nice 10, pinned by a test), `chip-20260908-decision-daemondrift-class-drift-aware-restart` (recommend A: one `/metaworker-learning` pass for a consent-gated drift-aware restart), `chip-20260906-decision-pausepressure-hold-lane` (keep), `chip-pausepressure-dlaptop-g5` (resolve with the root-cause note).
- **`chip-refwedge-dlaptop-ree-assembly-master-g3`** resolved done by this session with the root cause: the wedge is manufactured by (i) `ree_commit.py --push` silently no-op'ing on a diverged checkout while every session lands via cherry-pick (so the local branch accretes proven-but-unrecognised commits) and (ii) the IGW tick committing locally when its own push TIMES OUT (the one genuine strand today). HK-J item 5 removes the third contributor -- an operator recipe that cannot be followed. If it fires a 4th time, that is the `/metaworker-learning` trigger the chip text asks for; the class note is recorded on the chip.
- **`chip-metaworkergc-sweep-79-*`**: on-box work; left open and unclaimed for the owning box's dispatcher or the next Healer pass on that box. Dispatchers stay STOP.
- **IGW tick:** stays running (hourly). Its three spawnable proposals are gate-checked by HK-J; the staged `IGW-20260831-225` is section 7.

---

## 5. Dispatch recipe and expected shape

| Slot | Sessions | Depends on |
|---|---|---|
| Now (~20:10Z) | HK-J, HK-K, HK-L as Sonnet subagents; S5a as an Opus subagent | checkout converged (done) |
| When S2b lands | S5b (click), then S6 (click) | queue depth >= 4 so the scaler wakes a second worker |
| Next governance cycle | review 1013 (evidence run); 1010/1011/1015 as they land; apply HK-K's narrow writes; the seven W5-L findings; MECH-542's INV-011 decomposition; INV-092/093 `experiment_gate` fields; ratify HK-L's harness fix so the MECH-152 redesign and V3-EXQ-939 can move | user present |

Expected: 3 Sonnet bundles (~400k tokens each, 16 items) + 1 Opus S5a now; 2 Opus click sessions later. Every one of the 22 available chips is either in a bundle, in a click lane, or (4 decision chips + 1 on-box chip) named in section 4.

---

## 6. Ledger actions taken by this session

- Cleared the REE_assembly wedge (section 0) and resolved `chip-refwedge-dlaptop-ree-assembly-master-g3` done with the audit + root cause.
- Recorded 2 defect chips found during the repair (`chip-20260908-refconv-suggested-adopt-line-incomplete`, `chip-20260908-ree-commit-push-retry-worktree-leak`) -- both consumed by HK-J.
- Recorded 2 campaign click chips: `chip-20260908-w6-s5b-design-gaps`, `chip-20260908-w6-s6-successor-tail`. Member chips untouched (never-preclaim rule); the subagent bundles claim their own members on start.
- `hold_lane.v1.json` NOT regenerated: the held set and its review date are unchanged.
- Launched HK-J, HK-K, HK-L (Sonnet) and S5a (Opus) as supervised subagents.

---

## 7. Decisions for the user

1. **`IGW-20260831-225`** -- the only staged IGW item: an `/implement-substrate` build of `sd_epistemic_deficit_multitarget_readiness` (MECH-482), staged since 08-31 because the skill needs human assent. Substrate builds are HELD by the wave-5 rule (not on the 39-of-43 chain). Either launch it (`igw_routine_tick.py launch IGW-20260831-225`) or disposition it so the tick stops carrying it.
2. **The four decision chips** in section 4 (recommendations given).
3. **Power / dispatch:** ree-cloud-3 is running V3-EXQ-1011 (woken by the scaler), cloud-4 off, cloud-5 ON with a stale heartbeat. Nothing changed here. The on-box GC chip needs either a dispatcher lease on that box or a Healer pass.
4. **S5b / S6 are click lanes** (each needs a foreground red-team and queue writes while two queue sessions are live). Say so if you want the coordinator to run them as Opus subagents instead.
5. **Governance-owned, first on the next cycle:** the seven W5-L literature findings (IMPL-026 narrowing to REM, MECH-544 source-attribution, StateBridge same-model-only, the metadata corrections), MECH-542's INV-011 decomposition, the `experiment_gate` structured field.
