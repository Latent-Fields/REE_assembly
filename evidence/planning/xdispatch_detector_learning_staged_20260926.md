# Cross-dispatch collision detector -- durable fix (metaworker-learning)

**Status: AWAITING USER REVIEW**

- Session: `mwlearn-20260926-1044`, 2026-09-26
- Chip: `chip-20260925-xdispatch-detector-metaworker-learning`
- Prior generations: `chip-crossdispatch-fleet` (2026-09-23), `chip-crossdispatch-fleet-g2` (2026-09-25)
- Prior design: `crossdispatcher_collision_detection_feasibility_staged_20260818.md`
- Data: `origin/master:TASK_CHIPS.json` @ 86d7047ce (2026-09-26T10:43Z), 4515 chips, 82 with `claim_note_history`, 208 history entries.

## 1. Recurrence: genuine, one root cause

Gen 1 and gen 2 both fired on `_crossdispatch_collision_events()` (`scripts/hygiene_routine_tick.py:11974`). Gen 2 audited 0 of 6 events as genuine. Re-measured across the whole ledger: the predicate counts **25** events in total, and **all 25 are self-releases** (`unclaim`). Gen 2 split its 6 events three ways: self-release, orchestrator-to-worker handoff, and campaign handback. That split does not hold. Gen 2 compared each history entry against the row's *current* claimant, which is the same mistake the detector makes. Reconstructing each transition from the next history entry shows every "handoff" was a release, followed minutes or hours later by an unrelated fresh claim:

- `mech320`: released 11:58:24, next claim 17:06:20.
- `igw-222`: released 08:15:15, next claim 10:22:11.
- `ctxmem-livetap`: released 11:53:16, next claim 13:49:20.

## 2. Premises, re-measured

| Premise (chip text) | Verdict | Evidence |
|---|---|---|
| (a) The self-release (unclaim) case over-counts | **Confirmed**, and it is the *only* mechanism | After an unclaim, `row.claimed_by` is None, so `prev_claimant != current_claimant` always passes. |
| (b) Same-family orch->worker handoffs over-count | **Refuted** | Every instance was a release, not an overwrite. |
| (c) Campaign attempt-slug handbacks over-count | **Refuted** | Same as (b). |
| `previous_claimed_host` appears in no live entry | **Confirmed**: 0 of 208 entries, 71 of them written after 3d90bd2e4 landed | See below. |
| The cause is `coordinator_claim()` not writing history | **Refuted**. The cause is on the hub side. | See below. |

On the host field:

- **Client.** Under the coordinator-armed default, `cmd_claim` and `cmd_unclaim` return at the suppression branch before `apply_fn` runs. The history writer that 3d90bd2e4 extended (`chip_ledger.py:4194`, `:4305`) therefore runs only on the degraded git path.
- **Hub.** On the live path the history is written by `ree-v3/coordinator/db.py:1642` `_claim_note_history_after()`. It records `{superseded_at, previous_note, previous_claimed_by, previous_claimed_at}`, with no host and no successor.
- **Materializer.** `_chip_entry_from_row` renders the blob verbatim, so the field would appear if the hub wrote it.
- **Schema.** `claim_note_history_json` is a TEXT blob, so adding a field needs no migration.
- **Tests.** 3d90bd2e4's tests exercise only the git path.

## 3. Root cause

1. **Wrong successor (primary).** A history entry records who was *superseded*, not who superseded them. The detector stands in the row's claimant at scan time as the successor. That is wrong after every unclaim (it is None) and for every entry except the last. **Fixing the host field alone clears 0 of 25 events.** A release has no successor host, so the detector falls back to the proxy.
2. **Missing host (secondary).** The hub helper never carried `previous_claimed_host`, as shown in section 2.
3. **Structural blind spot.** Since the 2026-08-28 cutover, a chip claim is an atomic hub mutex. `try_claim_chip` (`db.py:1714-1722`) refuses any rival claim that is not stale; the hub treats a claim as stale after 6h and the client after 3h. So a distinct-claimant overwrite within the 300s window is impossible by construction, and the race loser's 409 (`app.py:365-384`) is never persisted. **Once fixed correctly, the history-sourced detector will read about 0 forever. It cannot see the collision it is named for.** The feasibility doc's §3a already notes that `CONTENTION_EXIT` leaves no trace. Its §5 quantified a different quantity: overlap between claims by different dispatchers.

The tests (`test_hygiene_routine_tick.py` ~9928-9990) use single-entry fixtures in which the row's current claimant *is* the successor. The fixtures supply exactly the assumption that fails in production. That is why the tests passed and the detector still over-counted (CLAUDE.md "the test half").

## 4. Proposed fix

**Step 1: derive each transition's successor. Client-only, low risk.** In `_crossdispatch_collision_events`, walk each row's `claim_note_history` with an index and derive the successor for entry `i`:

- `h["superseded_by"]` if present (step 2 adds it);
- otherwise, the next entry's `previous_claimed_by` when its `previous_claimed_at == h.superseded_at`;
- otherwise, if the next entry has a null claimant, treat it as a **release**;
- for the last entry: `row.claimed_by` when `row.claimed_at == superseded_at`. If `row.claimed_by` is None, it is a release. Anything else is **unknown**.

Count an event only when the successor is known, non-None and different from `previous_claimed_by`. Compare hosts between the predecessor and the *successor*, both passed through `machine_identity.canonical_machine_name`, because the hub renders raw hosts.

Tests to add:
- an unclaim, which must not count;
- A -> release -> B, where the release does not count and B is a fresh claim;
- A -> B within the window with different hosts, which counts;
- the same with the same host, which does not count;
- A -> B -> A;
- the documented limitation that a silent release with an empty note leaves no entry.

Run against gen 2's six events, the old detector counts 6 and the new one counts 0. The new test must FAIL on the old code. Measured over all 208 live entries: 124 releases, 84 claims, 0 unknown. The count drops from 25 to 0.

**Step 2: record the transition on the hub. `ree-v3/coordinator`, medium risk.** `_claim_note_history_after(row, new_note, superseded_at, superseded_by=None)` adds three keys:
- `previous_claimed_host` = `row["claimed_host_raw"] or row["claimed_host"]`;
- `superseded_by` = the new claimant from `try_claim_chip`, or None from `unclaim_chip`;
- `superseded_by_host`.

Mirror the same keys in `chip_ledger.py` `cmd_claim` and `cmd_unclaim` so the entry shape stays byte-identical on both paths. Add a case to `coordinator/test_task_claim_chip_mutations.py`.

The change is additive JSON with no migration, and it can be done in a single session, so it lands directly on `main`. It still requires:
- `coordinator/phase3_preflight.py`;
- the coordinator test run on a worker;
- a **hub `ree-coordinator` restart**.

Without step 2, step 1 is exact for every existing entry, because none has shown an unknown successor. Step 2 is what keeps it exact for entries written from now on.

**Step 3 (decision): what should the detector measure?** Given root cause 3, pick one:

- **3a. Re-source it from persisted refusals.** Record each hub `already_claimed` refusal (refused claimant, host, time, holder) in a small table. The detector then reads that table. It is the only source that can see a real cross-host race under the mutex. This is a new hub table plus an endpoint or materialized field, which is the largest change.
- **3b. Retire the history-sourced finding.** Keep step 1 so the code is correct and quiet, and document that the finding is structurally near-zero. Remove it from the recurrence-chip pipeline, so it stops generating gen-N chips.
- **3c. Leave it quiet.** Ship step 1 (and 2) only, and let a correct detector read 0.

Recommendation: **steps 1 and 2 now, and 3c now.** Decide between 3a and 3b later, only if cross-dispatch overlap becomes a live question. The feasibility doc's §5 overlap metric (pairs of claims by different dispatchers within W, not necessarily on the same chip) is the better-posed quantity if one is wanted.

## 5. Held-out check (GOV-HELDOUT-1)

None of these cases are among gen 2's six or gen 1's events. On each of them the old and new predicates disagree.

| Chip | Transition | Gap | Old | New | Correct |
|---|---|---|---|---|---|
| chip-20260826-coordinator-migration-phase1-deploy | 31a18d31 took the chip over a stale claim at 18:23:51, then released it at 18:28:21 with a STOP-CHECK note | 270s | count | skip | skip: self-release |
| chip-20260910-zworld-exogenous-event-channel | a metaworker-science session claimed, then released at 2026-09-18T23:59:20 | 237s | count | skip | skip |
| chip-20260918-exq541d-mech204-f1-guard-validation | abdec20b claimed, then released at 2026-09-20T11:47:23 | 120s | count | skip | skip |
| chip-20260818-mech152-redesign-queue-gated | a momentary claim made solely to restore a regressed note via unclaim | 1s | count | skip | skip |

Result: **passes on 4 non-degenerate cases**, plus 6 more of the same shape: sd097-config-knob, autopsy-v3-exq-1095, fromdims-alphaworld-sd008, mmskew-recurrence-postdecision-learning, unwritten-edge-discovery-skill, and proposal-exp-0736-paced.

**The check has a limit, and it is recorded here rather than hidden:** the cases disagree in one direction only.
- The ledger has **no genuine cross-host collision** at any gap. The only 2 overwrites by a different claimant are stale overrides, at 22.9 days and 3.2h, and both predicates agree on both.
- So the half of the new predicate that should count a real collision is untested on live data. It can be pinned only with synthetic fixtures, and under the mutex it may never fire. That limit is the reason step 3 is posed as a decision rather than assumed.

Cost counterweight: step 2 costs a hub restart plus a coordinator test run on a worker. Step 1 alone removes every observed false positive.

## 6. Open questions

1. History is written only when the claim note *changes*. A claimant who releases silently with an empty note leaves no entry. Should the hub write an entry on every change of claimant, or add a separate `claim_transitions` field? Deferred; the chip does not need it.
2. After this lands, should the recurrence-chip pipeline stop treating this finding as a recurrence source? That falls under 3b.
