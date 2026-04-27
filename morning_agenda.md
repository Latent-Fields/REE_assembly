# Morning Agenda -- 2026-04-27

Generated: 2026-04-27T04:20:05Z

---

## Queue Status
- Total pending: **0** (Mac: 0 | PC: 0 | EWIN: 0 | any: 0)
- 3 items currently `claimed` (running on remote machines):
  - `V3-EXQ-433d` -- claimed by DLAPTOP-4.local at 2026-04-27T01:21:39Z (SD-029 / MECH-256 event-conditioned comparator)
  - `V3-EXQ-418e` -- claimed by ree-cloud-1 at 2026-04-27T01:48:54Z (SD-016 Path 1 diversification loss 4-arm)
  - `V3-EXQ-490` -- claimed by ree-cloud-2 at 2026-04-27T01:49:09Z (MECH-269b symmetric V_s gating on E1/E2 cortical regions)
- **ALERT: Queue empty.** Once the three claimed runs complete the runners will idle. New experiments should be queued today, especially Mac-affinity and PC-affinity items.

---

## Experiments Awaiting Review (0 indexed / 4 runner-only)

No PASS/FAIL/INCONCLUSIVE results pending discussion. The four runner-only entries below are flagged for /diagnose-errors review (not for governance evidence).

### Runner-only pending (no indexed manifest)
- `V3-EXQ-484` -- UNKNOWN
- `V3-EXQ-485` -- UNKNOWN
- `V3-EXQ-493` -- UNKNOWN
- `V3-EXQ-490` -- ERROR (note: V3-EXQ-490 is also currently re-claimed by ree-cloud-2 -- prior attempt errored, retry in flight)

---

## Errors to Diagnose (3)

After cross-referencing against `experiment_queue.json` (no queued fix) and `runner_status.json` completed list (no successful lettered successor):

- **`V3-EXQ-008`** -- ERROR -- 2026-03-17 -- needs /diagnose-errors (oldest stranded ERROR; no successor anywhere)
- **`V3-ONBOARD-smoke-EWIN-PC`** -- ERROR -- onboarding smoke for EWIN-PC machine; first-experiment gate has not yet passed
- **`V3-ONBOARD-smoke-ree-cloud-1`** -- ERROR -- onboarding smoke for ree-cloud-1; first-experiment gate has not yet passed

The two onboarding smoke ERRORs mean those machines have not formally cleared the contributor onboarding pipeline test even though they are now claiming scientific work. Worth resolving before further attribution accrues against them.

---

## Governance Agenda (0 pending_user recommendations)

`promotion_demotion_recommendations.md` lists 77 claims under the Decision Queue, but every entry has `decision_status: applied`. No new pending_user recommendations were emitted by this morning's pipeline run. Substrate-change section: "No substrate status changes this run. No dependent invariants flagged."

Standing context (held holds, not new asks):
- Large `hold_pending_v3_substrate` cohort across MECH-269/270/272/273/275/280-295 and SD-032b-c-d/033a/034/036/037/039 -- mechanical holds; nothing to do until V3 substrate landings unlock them.
- `hold_candidate_resolve_conflict` cohort (ARC-026/030/032/038/041/042, MECH-073/075/093/098/099/111/112/116/118/120/128/150/153/165/186/188/220, INV-054, SD-012/015/021) -- waiting on conflict-resolution experiments, not a user decision.
- `SD-023` is the one structurally promotion-eligible item (recommendation: `promote_to_provisional`, decision_status: `applied`) -- worth verifying nothing is stalled there before queuing more.

---

## Literature Pull Candidates (Top 5)

| # | Backlog ID | Claim | Priority | Recommendation | Existing entries |
|---|------------|-------|----------|----------------|-----------------|
| 1 | EVB-0126 | onboarding | medium | collect_targeted_evidence | 0 |
| 2 | EVB-0127 | MECH-281 | medium | collect_targeted_evidence | 0 |
| 3 | EVB-0128 | SD-037 | medium | collect_targeted_evidence | 1 |
| 4 | EVB-0129 | MECH-057 | medium | collect_targeted_evidence | 2 |
| 5 | EVB-0130 | SD-003-prereq | medium | collect_targeted_evidence | 0 |

(All 18 backlog entries needing literature are at priority `medium`; no high-priority literature gaps in current scoring.)

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 20421).

---

## Blocked Items
- None. No TASK_CLAIMS collisions; governance.sh ran cleanly.
- Indexer emitted 14 WARNINGs about manifests with multiple claim_ids missing `evidence_direction_per_claim` (blanket `non_contributory` / `superseded` applied). These are pre-existing manifests, not blockers; flagged for cleanup if/when those claims are revisited.

---

## Suggested Order of Operations
1. Queue new experiments (queue is empty and three runners will go idle within hours).
2. Resolve the two onboarding smoke ERRORs so EWIN-PC and ree-cloud-1 have validated pipeline credentials.
3. Triage `V3-EXQ-008` (oldest stranded ERROR -- /diagnose-errors).
4. Once the three running experiments land, run the standard review cycle.
