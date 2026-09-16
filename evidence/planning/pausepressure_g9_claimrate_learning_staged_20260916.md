# Pause-pressure gate, generation 9: the claim-rate collapse -- root-cause pass

**Status: AWAITING USER REVIEW. Nothing in this file has been written to any script, skill, or registry.**

- Produced by: `/metaworker-learning`, chip `chip-20260916-learning-pausepressure-g9-claimrate`, session `eloquent-jepsen-5f6242` (Mac, `DLAPTOP`).
- Authorized by: user decision 2026-09-16 (orchestrate-20260916-1305 decision lane): route `chip-pausepressure-dlaptop-g9` to `/metaworker-learning` rather than re-fix the instance or accept the backlog as parked. The net-sink decision chip `chip-20260916-curation-net-sink-trend-decision` (recorded_7d 368 -> 379 -> 372 -> 402 over four cycles) was folded in.
- Written: 2026-09-16T19:15Z. All ledger numbers below are from `TASK_CHIPS.json` + `chip_archive/` as materialized at that time; the gate's own live read is `pause_pressure.py --json --skip-remote`.
- Prior passes in this class, which this doc builds on and does not repeat: `pause_pressure_recurrence_rootcause_staged_20260902.md` (g3, the origin split; g4 addendum; g5 hold lane) and `curated_pause_window_agenda_20260911.md` (g6, decision D1 and criteria C2.6/C2.7). The rescope chip `chip-20260911-pausepressure-rescope-claim-rate` built the capacity arm on 2026-09-14 (REE_Working `e6dff8abdc`).

---

## Summary

Three separable findings.

1. **The number the gate reports ("claim_rate 1.6%") cannot measure what it was built to measure.** The capacity arm is a STOCK ratio (chips open right now that carry `claimed_by`) over a population that turns over in minutes: a claimed authored chip is resolved a median **0.3 h** after claim (p90 1.1 h, n=1211). So the ratio is "sessions in flight / open pool" and reads 0-10% under *any* throughput. Replayed against the ledger, it read **0.0-3.3% on every sampled day from 2026-08-23 to 08-31** -- the fleet's healthiest fortnight, when 82-86% of fresh authored chips were being claimed within 72 h. The 10% threshold (C2.6) was calibrated on the g7 snapshot (118/2) and held-out-checked only against g5/g6/g7, all from the same period; it has no positive control and is unreachable in healthy operation. This is the same mis-typing the queuefloor g10 pass named for the queue floor ("a stock threshold reporting a flow deficit"), and the mirror image of R12's "an arm that reads 0 forever": this one reads PRESSURE forever.

2. **A real decline exists and it is dated: the cloud consumer left the loop on 2026-09-02.** Measured as a FLOW -- the share of authored work chips claimed within 72 h of spawn -- the rate was **77-92%** for cohorts spawned 2026-08-22 to 09-04 and **39-59%** for every cohort since. Weekly claims by host: cloud boxes claimed **81, 155, 133** chips in the three weeks to 09-02, then **2** and **35** (the 35 all inside the user's one 8 h lease window on 09-14). The Mac's own claiming was flat (114-184 chips/week from ~55 distinct sessions). The mint was flat too (217-276 authored work chips/week). Remove ~140 cloud claims/week from a ~250/week mint and the open pool grows from ~25 to ~80-95, which is exactly what happened. Nothing on the authoring side changed; a consumer was switched off.

3. **Half the residue is science-class work that no dispatcher lane can ever take, and that resolves as refusal when it IS claimed.** Of the 63 actionable chips, `dispatch_candidate_order.classify()` puts **33 in the science tier** and 30 in the default/infra tier. The campaign ledger landed today refuses science members by construction ("science stays on the Mac decision lane"); the cloud dispatcher in campaign mode therefore never sees them; the Mac's science pass launches only on a per-launch user decision and pre-flighted **0 of 8 today** (GFLAG-0293/0294/0295: overlap gate refuses every agent-stepping design; a structurally biased statistic; a substrate API that does not exist). Of 114 science chips claimed in the last 14 days, resolution notes cite `gflag`/`blocked`/`refus` in 75 and "queued V3-EXQ" in **4**. More claiming would convert these chips to refusals, not experiments. Their problem is supply quality, already the subject of `queuefloor_recurrence_rootcause_staged_20260915.md` section 3b (the refusal write-back gap), and the pause gate should stop counting them as a capacity deficit.

**Is today's campaign ledger sufficient?** No. It is (a) a housekeeping-bundle lane only, capped at 6 members, refusing science and non-`work` kinds -- so it can address at most the 30 infra chips, never the 33 science ones; (b) empty (`scripts/dispatch_campaigns.json`: zero campaigns) and inert on the hub until `chip-20260916-campaign-ledger-hub-restart` is run; and (c) its candidate-set default, landed separately today (REE_Working `9ac89d46a`), makes a leased cloud dispatcher list **nothing but `urgency:true` chips** until an orchestrator has curated a bundle. So the expected cloud claim count after the hub restart, with no curation and no lease, is zero. The expected rate once it is used: the 09-14 window is the calibration point -- 35 cloud claims and 29 Mac claims in one day, roughly the whole infra half of today's backlog -- but only for bundles an orchestrator has written and only while a lease is open.

---

## 1. Recurrence check (skill Step 1): genuine, and this is the fourth distinct defect

| Gen | Fired | Trip (as recorded) | Response | Defect it exposed |
|---|---|---|---|---|
| g1-g4 | 08-29 .. 09-02 | recorded_7d 716-1016, open 72-195 | four backlog curations | un-attributed aggregate (fixed 09-02: origin split) |
| g5 | 09-05/06 | authored open 104 | hold lane | curated-and-held read as uncurated (fixed 09-06: hold lane) |
| g6 | 09-09 | recorded_7d 291 | curated pause agenda 09-11 (D1: "grant leases or accept parked") | backlog arms blind to execution capacity (capacity arm built 09-14) |
| g7 | 09-11 | open 68, recorded 300 | duplicate of g6 | -- |
| g8 | 09-14T23:38 | **claim_rate 8.6% (6/70)**, wedge 93 | user: no third root-cause pass | fired 2 h after the user deliberately STOPPED both cloud dispatchers |
| g9 | 09-16T13:12 | **claim_rate 1.6% (1/64)**, wedge 90 | this pass | same stop still in force |

Same root cause across g8 and g9, and it is not the same as g1-g5's: each of those was the backlog arm mis-reading a population; g8/g9 are the capacity arm reading a *policy* (dispatchers STOP by user decision) as a *fault*, through a statistic that would have tripped regardless. Threshold for this skill is 2; this is 2 on the capacity arm specifically and 9 on the chip.

The gate's prior-generation-remedy tracker (C-III) is also worth reading straight: `prior_generation_remedy` for g9 reports `ever_claimed: None, remedy_ref: None` -- g8's remedy was a user instruction, not a chip -- so the tracker cannot distinguish "remedy never ran" from "no remedy chip was minted", which is the same limitation C2.6's second clause was written to cover.

## 2. What the volume actually is (skill Step 2, measured)

**Actionable open pool, 2026-09-16T19:15Z: 63 chips** (gate: 65 authored actionable, 16 held, 2 of the 65 are `kind: decision`).

| Slice | Count | Who authored it |
|---|---|---|
| spawned 2026-09-16 | 17 | orchestrate-20260916-1305 science passes (9 `Queue ...` chips at 13:58Z), two autopsy staging chips, this chip |
| spawned 2026-09-10 | 17 | governance-apply `gflag*` chips (7 at 07:19-07:47Z), six `merge-*` curation chips (21:52Z), two implement-substrate |
| spawned 2026-09-14/15 | 19 | orchestrate-20260914-2153 / 20260915 decision-lane follow-on, MECH substrate registrations |
| older than 7 days | 23 | 2026-08-14 .. 09-09; includes two "queue once X lands" chips, MECH-035/037/039/065/468 substrate builds |

By dispatch class: **33 science / 30 default-infra / 0 housekeeping** (the `hygiene_tick` family is excluded by the origin split). By origin: 44 `spawn_task` (clickable in a UI, 46 of 81 open authored carry a `task_id`), 37 `headless` (never clickable; claimable only by a dispatcher or an orchestrator bundle).

**Flow, weekly, authored work chips** (spawn week; claimed = ever claimed):

| Week | Minted | Ever claimed | Done | Withdrawn | Still open |
|---|---|---|---|---|---|
| 08-12..08-19 | 376 | 296 (79%) | 355 | 19 | 2 |
| 08-19..08-26 | 256 | 185 (72%) | 243 | 11 | 2 |
| 08-26..09-02 | 312 | 216 (69%) | 285 | 19 | 8 |
| 09-02..09-09 | 287 | 189 (66%) | 236 | 40 | 11 |
| 09-09..09-16 | 233 | 124 (53%) | 142 | 33 | 58 |

**Claims by host, weekly (claim week):**

| Week | Total | Mac (`DLAPTOP`) | Cloud (`ree-cloud-4/5`) | Distinct Mac sessions |
|---|---|---|---|---|
| 08-19..08-26 | 191 | 36 | **155** | 24 |
| 08-26..09-02 | 199 | 66 | **133** | 56 |
| 09-02..09-09 | 186 | 184 | **2** | 54 |
| 09-09..09-16 | 149 | 114 | **35** (all 09-14, 10:34-22:47Z) | 56 |

Daily cloud claims: 31, 6, 27, 39 (08-26..29), 0, 0, 45, 9 (09-01/02), then **zero on every day except 09-14**. `dispatcher_control.json` shows every box `requested_state: stop`; the cloud entries were written 2026-09-14T21:48Z by `orchestrate-20260913-1643` ("user's 8h dispatch window complete"). Every Orchestrator cycle since records "dispatchers STOP throughout, no lease granted", one with the reason "no queueable science existed to dispatch, and the work that could run ran as local subagents" (`WORKSPACE_STATE.md`). The lease fails closed by design (the 2026-08-23 runaway); this is a policy, working as built.

**Stock vs flow, replayed** (STOCK = the capacity arm's own predicate over the population open at 00:00 on day D; FLOW = share of the cohort spawned in [D-10, D-3] claimed within 72 h):

| Day | Open | Claimed now | STOCK | FLOW n | FLOW |
|---|---|---|---|---|---|
| 08-23 | 17 | 0 | 0.0% | 378 | 84.1% |
| 08-25 | 28 | 0 | 0.0% | 355 | 85.1% |
| 08-27 | 13 | 0 | 0.0% | 293 | 81.9% |
| 08-29 | 30 | 1 | 3.3% | 225 | 79.1% |
| 08-31 | 25 | 0 | 0.0% | 242 | 78.5% |
| 09-02 | 55 | 6 | 10.9% | 242 | 80.2% |
| 09-04 | 88 | 4 | 4.5% | 258 | 81.0% |
| 09-06 | 104 | 1 | 1.0% | 303 | 64.4% |
| 09-08 | 66 | 5 | 7.6% | 236 | 54.7% |
| 09-10 | 94 | 1 | 1.1% | 260 | 49.6% |
| 09-12 | 95 | 0 | 0.0% | 276 | 54.0% |
| 09-14 | 80 | 3 | 3.8% | 296 | 49.0% |
| 09-16 | 79 | 1 | 1.3% | 270 | 52.2% |

The STOCK column never rises above 11% in five weeks and is uncorrelated with the FLOW column. The FLOW column steps from ~80% to ~50% between the 09-04 and 09-08 readings -- cohorts spawned 08-29..09-05 vs 09-01..09-08 -- i.e. as the cloud consumer disappeared. Split by class the step is in both: science 92% -> 39-47%, other 77% -> 50-59%.

**Signal 3 (`wedge_repairs_7d 78 > 2`, all `not_repaired`)** is a different class and is left alone here: 48 refusals on the Mac's shared `REE_assembly` checkout and 30 on `REE_Working`, every one `reconcile_wedge_content: REFUSING -- the ahead range touches N path(s) outside the reconcilable allowlist` (REE_assembly currently ahead 10 / behind 16). That is the refwedge class, routed on 2026-09-16 to its own pass (`chip-20260916-refwedge-class-learning-pass`, recommendation ledger 297). It contributes to this chip's trip line but not to its subject.

## 3. Root cause

**Proximate:** the capacity arm's predicate is a stock ratio over a fast-turnover population, so it fires at any throughput; g8 and g9 were minted with it as their headline number, 2 h and 40 h after the dispatchers were deliberately stopped, and the verdict text ("grant dispatch leases") nags about a standing user decision. C2.6 anticipated exactly this -- "claim rate >= 10% ... **or** dispatchers deliberately STOP and the gate's backlog arms suspended accordingly" -- but only the first clause was built. The gate reads chips; it does not read `dispatcher_control.json`.

**Underlying, and the thing the gate should have been able to say:** since 2026-09-02 the only consumer of authored chips is the Mac (orchestrator subagent bundles plus interactive sessions, ~55 sessions and ~120-180 claims a week), against a mint of ~250 a week that did not change. The cloud dispatchers that used to take ~140 a week are STOP by policy, and as of today their candidate set is a curation ledger that is empty and structurally excludes the science half of the backlog. So "1.6%" was a false number attached to a true sentence, and the true sentence was: *the mint is sized for two consumers and one of them has been off for two weeks; the half of the residue that is science-class has no lane at all and mostly refuses when run.*

**Why five generations of remedy missed it, stated once:** each fix so far (origin split, hold lane, capacity arm) corrected what the gate *counts*; none gave it a read on *who is consuming* -- the lease file, the campaign ledger, the class split. A gate that measures accumulation and cannot see consumption will always route to the accumulation side.

## 4. Proposed durable fix (NOT built; consent-gated per skill Step 4)

All three parts touch `scripts/pause_pressure.py` (+ `scripts/test_pause_pressure.py`); no threshold on any existing arm changes; nothing is installed on the hub or workers; no lease is granted.

**C1 -- retype the capacity arm as a matured flow rate.** `claim_flow_72h` = share of authored `kind: work` chips spawned in `[now-10d, now-3d]` that were claimed within 72 h of spawn (the 3-day lag lets a cohort mature; the 10-day window keeps n ~250). Trip below **0.60** -- below the healthy floor (77-92%, nine readings) and above every collapsed reading (39-59%, six readings); report the numbers on the tripped line. Keep the stock ratio as an informational `claims_in_flight` count, never a trip. Rate is `None` on an empty cohort, as now.

**C2 -- make the arm policy-aware (C2.6's second clause).** Read `dispatcher_control.json` (fail-open: unreadable file = no suppression). If every non-`local` box is `requested_state: stop`, the capacity arm does not trip; it reports `capacity: cloud dispatch STOP by policy since <requested_at> (<requested_by>)` alongside the flow number, so the decline stays visible without minting a generation against a decision already taken. A lease that is `run` but expired counts as stop (the file's own semantics).

**C3 -- report the actionable backlog by dispatch class.** Split `open_chips_authored_actionable` into science / other using `dispatch_candidate_order.classify()` (import fail-open: no split). The tripped line for the backlog arm names both numbers, and the minted chip text says which lane can take each half: infra -> a curated campaign + lease; science -> the Mac decision lane, with its recent refusal share. This is reporting only; it changes no threshold.

Cost, stated rather than skipped: C1 adds a second time window and a maturation lag to a script whose value is being seconds-fast and mechanical; a 3-day lag means a collapse is seen 3 days late (the 09-14 window would have lifted the reading only by 09-17). C2 couples the gate to a file whose semantics belong to `dispatcher_control.py`, and suppressing a trip on policy is the kind of thing that can hide a real starvation if the policy is forgotten -- which is why C2 reports rather than silences, and why C1's number still prints. C3 imports a 1,200-line ordering module for one classifier call; if `classify()` changes shape the split degrades to "unknown", not a crash.

**Explicitly not proposed here:** raising `max_claude_sessions`/granting leases (a user cost decision, option 2 below); changing `CLAIM_RATE_MIN` in place (the number is the wrong type, so retuning it is the symptom fix the chip forbids); any change to the campaign ledger, `proposal_backlog_dripfeed.py` (cap 5, decided 09-15) or the queue floor; anything about signal 3.

## 5. Held-out check (GOV-HELDOUT-1)

Cases the fix was NOT written from (it was derived from the g9 reading and the g7/g8 snapshots). Old = the capacity arm as built (stock < 10%); new = C1 (flow < 60%) with C2. Only cases where the two give different verdicts count.

1. **2026-08-23 .. 08-31 (five daily snapshots, one regime).** Old: 0.0-3.3% -> PRESSURE on capacity every day. New: flow 78-85% -> QUIET. History: the fleet was consuming 130-155 chips/week on the cloud alone; g1 fired 08-29 on the *backlog* arm and the user chose "Science first, then pause" (recommendation ledger, 08-29T15:27Z) -- no one thought capacity was the problem. New gives the right call. **Non-degenerate.**
2. **2026-09-06 (g5).** Old: 1.0% -> PRESSURE on capacity. New: flow 64% -> QUIET (above 60, and the cloud lease was not the question that week). History: g5's root cause was the hold lane -- a counting defect -- and the user's disposition was "Note it, don't action in-cycle" (ledger 09-06T16:24Z). A capacity trip would have added a wrong remedy to a right diagnosis. **Non-degenerate**, but marginal (64% vs 60%): stated so the threshold is read as a trial value.
3. **2026-09-14T23:38 (g8).** Old: 8.6% -> PRESSURE, 2 h after `orchestrate-20260913-1643` wrote `stop` for both boxes. New: flow 49% -> C1 would trip, but C2 reports "STOP by policy since 21:48Z" instead of tripping. History: the user's response was "do NOT spawn a 3rd root-cause pass" -- treated as noise. **Non-degenerate for C2**, degenerate for C1 alone.
4. **Positive control -- 2026-09-10/12 (g7 window, 118 open / 2 claimed).** Old: PRESSURE. New: flow 50-54% -> PRESSURE, and C2 does not suppress it: the stop entry then in force was `local` only (08-30), the cloud entries were not written until 09-14. The fix must not silence this one, and it does not.

Two clean non-degenerate cases for C1 (1, 2), one for C2 (3), one positive control. C1's third case is missing for a structural reason: the healthy regime is the only pre-decline data and it is one regime, so it is stated here as one case with five samples rather than five cases. Per the CLAUDE.md discipline that is itself a finding -- **C1's 0.60 threshold is shipped as a trial value scoped to the two regimes observed**, with the retune trigger stated: revisit after the first cloud lease window post-landing, when a third regime exists.

This check cost about a quarter of the session and it changed the proposal: an earlier draft had C2 *suppress* the arm outright when dispatchers are STOP; case 4 (the g7 window, where `local` was STOP but the cloud entries were not yet written) showed that a naive "any stop entry" test would have silenced the one real collapse, which is why C2 keys on the cloud entries specifically and reports rather than silences.

## 6. What was NOT done here, deliberately

- Nothing was built or landed. Skill Step 4 admits no "obviously safe" carve-out for `scripts/`.
- `scripts/pause_pressure.py` thresholds untouched; no hub or worker install; no lease granted.
- `chip-pausepressure-dlaptop-g9` was already resolved by the Orchestrator at 18:59Z and is not re-resolved.
- The 33 science-class chips are not triaged here. Their disposition belongs to the queuefloor g10 refusal write-back design and the Orchestrator's decision lane, not to this gate.
- The wedge signal (78 unrepaired refusals) is left to `chip-20260916-refwedge-class-learning-pass`.

## 7. Decision chip

`chip-20260916-decision-pausepressure-capacity-arm-retype` (kind `decision`, origin `headless`) carries the options: (1) build C1+C2+C3 as designed; (2) build them AND adopt a standing curated-campaign lease window (a cost decision this pass does not make); (3) suspend the capacity arm entirely per C2.6's second clause and accept the backlog as parked; (4) hold. Recommendation: (1).
