# Metaworker-learning: outstanding classes, batched pass (staged)

**Status: AWAITING USER REVIEW**
Written 2026-09-18T18:32Z by session `ml-outstanding-classes-20260918` (chip
`chip-20260918-metaworker-learning-all-outstanding-classes`). Nothing below has been built or landed.
Counts are re-derived from live chip resolution notes this session (Step 1 discipline: same root cause,
from resolution notes, withdrawn false positives excluded). Full per-class working (four research passes)
is summarised here; the per-class agent reports were scratch files, so the load-bearing evidence is
quoted inline.

## Verdict table

| Class | Verdict | Why |
|---|---|---|
| P1 refwedge / checkoutdiverged | **DESIGN** (narrow) | Root cause F (DLAPTOP REE_Working pure ref lag, ~9 instances) has no fix landed. |
| P2 staleclaim | **HAND BACK** (optional tuning only) | 47% self-resolve, 29% landed-unclosed bookkeeping, 4% true abandonment. Volume is expected churn. |
| P3 statusregress | **DESIGN + REPAIR** | One genuine coordinator-side bug (commit `70f6849fab`, 22 rows still 19 open). |
| P4 fleet-health | **DESIGN** (build chip exists) | 6 root causes, 1 clean true positive in 22 repair chips. |
| P5 daemondrift | **HAND BACK** | All true positives; restarts stay manual (user decision 2026-09-10). |
| P6a deployeddrift | **HAND BACK** | One cause; Orchestrator sudo redeploy 09-15, no chip since. |
| P6b pausepressure | **WATCH** | Root-caused and built (`394308564`); watch for generation 11. |
| P7 metaworkergc / strandedwt / scriptscorpus / routedwriter | **NOT LEARNING JOBS** | By-design or owned elsewhere; not re-surveyed. |

The shared-fix hypothesis (P4 expectation gate covering P5/P6) fails: P5/P6a are true positives whose
intended actor is a human or consent. The one genuinely shared cause, the generation counter shared by four
chip families, is already fixed.

## P1 -- refwedge / checkoutdiverged

Population: 57 non-withdrawn instance chips (36 DLAPTOP, 21 cloud), 08-15..09-18. Root causes:
A route-A false negatives (~11, fixed 08-18 route C); B prune push default (1-2, fixed 08-19); C the latch
(~30, R1 `f0eab5fc6` 08-28, confounded by coordinator cutover); D checkoutdiverged sync-repair defects
(~7, R1/R2/R3/R5 by 09-07); E IGW tick stale-base commits on REE_assembly (8, fixed 09-16 `b4a44af59`,
`25dc09539`, too early to judge); **F DLAPTOP REE_Working pure ref lag (~9, NO FIX)**.

The healer-topology candidate fits repair LATENCY (DLAPTOP detect lag ~56 min vs 11-15; duration ~4.8h vs
1.3-2.4h) but NOT occurrence: cloud boxes wedged ~9 times with healers resident and stopped after R1/R3/R4.
The better-fitting difference is that DLAPTOP's checkout is human-live, so the automated adopt cannot run;
human authorisation is the residual gate. Routing the audit to cloud healers covers the audit half of up to
~25 instances and prevents 0 occurrences: ship it as a latency/toil fix, not a cure.

**Proposed (in order):**
1. Run the owed R1 re-measure (`chip-20260910-merge-refwedge-class`, never run) before building.
2. `scripts/hygiene_routine_tick.py`: split the wedge chip into an UNPINNED audit chip and a DLAPTOP-pinned,
   human-gated MOVE chip (host-pin text near L742, `_HOST_DECLARATION_MARKERS` near L5995).
3. `scripts/ree_commit.py`: after a throwaway-worktree push on the shared checkout, extend post-push
   convergence to the F shape using existing routes A/B/C only. Fixture: 09-18 g5 (10 ahead, all redundant).
4. Bring the R3 hybrid into the Mac's `ree_git_sync_repair.sh` for clean-tree, known-lag paths.

Explicitly NOT proposed: relaxing the refusal, a heuristic third proof route, a resident Mac healer.

**Held-out check:** only 3 non-degenerate cases (08-25 wedge at 54 ahead; g5 09-18; REE_assembly g8), all
differing on latency not outcome. Three others were identical or self-cleared. Finding: scope item 2 as a
latency/toil change, do not present it as a rate fix.

## P3 -- statusregress

53 chips; ~44-47 detector false positives (legitimate unclaims, self-heals); 5-8 git-side stale-disk clobbers
that self-healed (led to the monotone-terminal guard `ddbafb8243`); **2 real done->open regressions**:
`60a8d779cd` (git-side, self-healed) and `70f6849fab` (2026-09-18, 22 rows genuine, coordinator-side).

`70f6849fab` changed 1183 rows; 22 went terminal->open with resolution fields nulled, and 1178 lost `archived`
markers. Most likely mechanism (from code, NOT confirmed on the hub -- no DB access from this box):
`upsert_chip` in `ree-v3/coordinator/db.py` Case B (~L546-547, "only git moved -> adopt git") adopts a
differing incoming entry with no terminal check; the terminal guard exists only in the final `else`
(L548-553). Candidate stale sources: shadow-sync `-stale-local` fallback
(`task_claim_chip_shadow_sync.py` L107-121) and the materializer `ingest()`. Confirm from the hub journals
around 12:51-12:55Z and `updated_at` on the 22 rows before building.

**Repair (data, separate from design):** 19 of the 22 still open (3 re-resolved by others). Restore via
`chip_ledger.py resolve --chip-ref <ref> --status done|withdrawn --note ...` (16 done, 2 withdrawn), original
`resolved_at` recorded in the note, lost note text from `70f6849fab^`. Never hand-edit TASK_CHIPS.json.

**Proposed fix:** hoist the terminal-status guard above the Case A/B split in `upsert_chip`; refuse incoming
entries that drop an `archived` marker; mirror the guard in `upsert_task_claim`; refuse the `-stale-local`
fallback once the DB has rendered rows; add a materializer tripwire that fails closed when a render flips
many rows terminal->open.

**Held-out check:** one clean differing case (`70f6849fab` itself); others are controls. A deliberate reopen
(`resolve --status open`, e.g. `0b395755f`) would be newly blocked, which needs a decision on whether reopen
stays supported. Finding: this rule is scoped to its motivating incident; ship as a narrow monotone guard and
say so.

## P4 -- fleet-health

Six root causes in `check_dispatch_fleet_health.py`; precision 1 clean true positive in 22 repair chips
(~33 sessions). Lease-stop case (09-17) shipped nothing. A 09-18 live reading still flags 2 of 2 machines
that are both `retired:true` / deliberately stopped.

**Proposed:** read `dispatcher_pauses.json` and `dispatcher_control.json` before issuing a verdict; add a
non-fault "unobservable"/"expected-stopped" status outside `FAULT_STATUSES`; fix L1046-1054 so unobservable
boxes stop minting repair chips; mirror the Step 1 wording in `metaworker-dispatch` SKILL.md in both
`.claude/` and `.agents/`. This IS the open build chip `chip-20260918-fleethealth-gate-on-declared-expectation`.

**Held-out (differ):** ree-cloud-4 lease stop since 09-14 (old flags ALIVE-STALLED, new silent); both
dispatchers retired since 08-25 (old flags 2/2, new silent); SSH auth gap 08-20 (old faults innocent box, new
observability only). A fourth (scaler power-off) is soft. Adequate: 3 clean cases; the true positive (a
dispatcher that rebooted itself) is flagged either way.

## P2 / P5 / P6 -- handed back

- **P2:** optional tick-side mint grace (keep the 6h audit threshold and G/P auto-close; mint only at age
  >=12h or stale on two ticks >=3h apart). Would suppress ~62/66 self-resolved and all 12 live-owner false
  positives; delays true-abandonment review ~6h. Real gain ~12 adjudications in 6 weeks. All four held-out
  cases come from the motivating window, so run GOV-HELDOUT-1 on August cases first. Never auto-close
  beyond G and P.
- **P5 / P6a:** true positives; restart is human/consent-gated by decision (auto-restart disproven by
  held-out check; auto-redeploy rejected 08-26). Not a detector defect.
- **P6b:** watch for generation 11 only.

## Honest counterweight

Held-out validation and this whole batched pass cost real cycles; two of the three DESIGN items have thin
held-out evidence (P1: latency-only, P3: one case). That is stated rather than padded.

## Ask (one decision chip)

Options: (A) proceed with P3 fix + repair, P4 build (existing chip), P1 steps 1-2 only; hand back P2/P5/P6a;
(B) constrain to the P3 data repair and P4 only; (C) hold everything.

## Outcome addendum (2026-09-18, option A chosen by user in chat)

**Built and landed:** P3 coordinator guard (ree-v3 `7f51dff`) + 16 chips restored done, 1 withdrawn; P4 fleet-health
EXPECTED-STOPPED gate (REE_Working `7d4d64f85`); P1 paste-ready `--allow-discard` prefill in the wedge chip
(hygiene_routine_tick.py, 2 tests, 753 pass). Hub restart to load the P3 guard is NOT done (consent-gated).

**P1 step 1 -- R1 measurement (item 1 of chip-20260910-merge-refwedge-class), non-withdrawn refwedge chips:**
| window | n | mean ahead at clear | median / mean duration (h) |
|---|---|---|---|
| pre-R1 08-15..08-27 | 27 | 26.0 | 0.8 / 3.0 |
| post-R1 08-28..09-03 | 9 | 19.0 | 1.8 / 3.3 |
| 09-04..09-18 | 11 (all DLAPTOP) | 16.7 | 4.1 / 5.8 |
Rate: ~3.7 episodes per 1000 origin commits since 09-04 (2952 commits) against a predicted ~2.8 -- roughly
unchanged per commit, absolute rate down (2.1/d -> 0.73/d). Cost: mean ahead-count down ~36% (26 -> 16.7), not
"sharply"; duration UP because the post-09-04 population is entirely DLAPTOP, where clearing waits on a human.
Verdict: R1 is not falsified on rate, is only partially supported on cost, and duration is not measurable
across the population shift. Phase-2b cutover confound (same day) cannot be separated. Supports the finding
that the residual is human-authorisation latency.

**P1 step 2 -- scoped DOWN, honestly.** The approved plan was an unpinned AUDIT chip + pinned MOVE chip. A new
chip family touches _KNOWN_HYGIENE_PREFIXES, _EPISODIC_STANDING_PREFIXES, the absence-done set,
dispatch_candidate_order and pause_pressure registries plus the resolve/re-fire hysteresis -- the exact
machinery whose flapping produced this class's history. Shipped instead: the toil half (paste-ready command).
Deferred design if wanted: derive the audit ref post-hoc from the MOVE chip's generation ref inside
`_record_episodic_finding` (no episodic registry entry), resolved by the healer on amending the MOVE chip.

**Not done:** items 2 and 3 of chip-20260910-merge-refwedge-class (no-op-delete re-test; chip_archive proof-route
design fork -> needs a decision chip), so that chip stays open.

## P5 counter-example addendum (2026-09-22, sweet-robinson-b3e2c1)

**The P5 classification above stands; its IMPACT rating does not.** "True positives ... not a detector
defect" is correct and is not being reopened. What this addendum records is a measured case where a
daemondrift finding was not benign observability drift but the **delivery gap suppressing an approved fix
for another class in this same document**.

**The case.** On 2026-09-22, `chip-daemondrift-ree-cloud-1-ree-coordinator-g3` ("ree-coordinator on
ree-cloud-1, 1.0d stale") was the only standing signal that `ree-v3 0ddac64f` (2026-09-19T10:25:21Z,
*"shadow-sync never ingests the mirror working tree; hoist the done guard in upsert_task_claim"*) had never
been loaded. That commit is the **root-cause** fix for the P3 statusregress class adjudicated above -- the
one that stops the generator, as distinct from the restore and the `upsert_chip` guard (`7f51dff`), both of
which were live. Measured: `ree-coordinator` PID 3667893, `ActiveEnterTimestamp` 2026-09-18T18:52:04Z,
`NRestarts=0`, ~3.47 d elapsed; `git log --since=<that> -- coordinator/` as user `ree` returns exactly
`0ddac64f`; hub `db.py` mtime 2026-09-19T10:27:38Z. So P3 shipped, was user-approved, and was **half-live on
the fleet for three days**, and the only artifact saying so was a daemondrift chip triaged as routine.

**What this does and does not ask for.** It does **not** re-propose auto-restart (disproven by held-out
check) or auto-redeploy (rejected 2026-08-26); both stay closed, and the restart remained human-gated in
this case too. The ask is narrower and is about **triage order, not automation**: when a daemondrift chip
names a daemon, it is cheap to ask *what is inert* (`git log --since=<ActiveEnterTimestamp> -- <svc dir>`),
and the answer occasionally promotes a routine hygiene chip into a blocker on already-approved work.

**GOV-HELDOUT-1 is OWED, not done.** This is one case, recorded as evidence; no rule was changed. A future
pass acting on it must find >=3 non-degenerate cases where the old and new triage give different answers,
per CLAUDE.md "Held-out check before shipping a standing-rule change" -- and if it cannot, the finding is
that this is scoped to its own incident.

**Correction to this document's own P1/P3 record.** An earlier pass of this session reported `7f51dff` as
unloaded. That was **wrong**. The hub `ree-v3` ref at the coordinator's process start *was* `7f51dff`
(pulled 18:41:11Z, 11 min prior), so `f2b70bbe91`, `bedef6b` and `7f51dff` were all loaded. The error came
from running `git` on `/home/ree/REE_Working/ree-v3` **as root**, which returns `dubious ownership` and a
false "not an ancestor". **Always `sudo -u ree`** when auditing what the hub has.

**Disposition.** Restart user-authorised 2026-09-22 and routed to the live `/metaworker-orchestrate`
session (chip `chip-20260918-decision-hub-restart-id-collision`, whose own premise was stale and was
amended; claimed 06:11:06Z), sequenced to wait behind an active claim on `coordinator/db.py` by
`brave-solomon-95d478`. That session's heartbeat-trim fix is behaviourally inert on this hub, so the
restart's entire observable payload is `0ddac64f`. The chip's VERIFY LIVE probe was deliberately not run by
anyone: it writes real rows to the live coordination plane, and since the guard code is demonstrably
loaded, an exit-0 result would now indicate a genuine defect rather than an argument for a restart.
