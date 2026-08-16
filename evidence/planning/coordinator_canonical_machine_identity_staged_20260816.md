**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml (or whichever registry). No coordinator code was changed.**

# Coordinator canonical machine identity -- scoping investigation

- **Chip:** `chip-20260815-coordinator-canonical-machine-identity`
- **Session:** `metaworker-chip-20260815-coordinator-canonical-machine-identity` (headless, on `ree-cloud-5`)
- **Date:** 2026-08-16T08:29:07Z
- **Bases:** `ree-v3` `origin/main`, `REE_assembly` `origin/master` (both fetched at session start)
- **Outcome:** **Investigated. Recommend a NARROW ingest-boundary change, gated on a human decision. Do NOT canonicalise stored history. Do NOT generalise `EXACT_ALIASES`.**

---

## 0. STOP-CHECK result -- the chip's premise held, with one correction

The chip's stop-check was `grep -rn machine_identity ree-v3/coordinator/ && echo "ALREADY RESOLVES -- stop"`. That grep **hits**, but honouring the stop would have been wrong. The hits are all in the *diagnostic* layer, none in the *data* layer:

| File | Uses | Landed |
|---|---|---|
| `coordinator/phase3_verify.py:38` | `same_machine` | `b0f0674c` |
| `coordinator/phase3_preflight.py:39` | `canonical_machine_name` | `f0c21d1e` |
| `coordinator/deploy/fleet_integrity_check.py:68` | comment only | -- |
| `coordinator/deploy/phase3_wake_fleet.sh:136` | comment only | -- |

```
grep -n "machine_identity\|canonical_machine_name\|same_machine" coordinator/db.py coordinator/app.py
  -> (NO HITS)
```

**`db.py` and `app.py` -- the live claim and command plane -- resolve nothing.** The chip's premise is intact. A previous pass fixed the preflight/verify checkers and stopped there, which means *the tooling that would tell you identity is consistent now canonicalises, while the code that actually keys on identity does not.* That asymmetry is worth naming on its own: the checker can report agreement that the data plane does not enforce.

---

## 1. Enumeration of machine-keyed sites (deliverable 1)

Failure mode is what happens **if the same physical box presents two spellings**.

### 1a. `db.py` -- claim plane

| Line | Site | Comparison | Failure mode |
|---|---|---|---|
| 144 | `_affinity_ok(affinity, machine)` | `affinity == machine` | **Silent miss.** A queue entry pinned `DLAPTOP-4.local` is never claimable by a box reporting `DLAPTOP`. Experiment starves indefinitely; no error anywhere. |
| 239 | `_has_fresh_owner_heartbeat` | `heartbeats WHERE machine=?` keyed on `claimed_by_machine` | **DUPLICATE RUN -- the worst one.** Owner renamed => no row found => "no fresh heartbeat" => claim reads recoverable => reaped from a machine that is *still running the experiment*. |
| 371 | `machine_claim_fenced` | `heartbeats WHERE machine=?` | **Silent miss.** No row => fence not armed => a draining box is granted a fresh claim => the ~10h orphan the fence exists to prevent (V3-EXQ-841). |
| 387 | `record_claim_fence_clear` | upsert on `machine` | **Duplicate.** Clears the fence on the *other* spelling's row; the armed one stays armed. |
| 527 | `machine_has_departed` | `heartbeats WHERE machine=?` | Silent miss. Route (b) reaper never fires => back to the 6h floor. Degradation, not corruption. |
| 559 | `try_claim` | writes `claimed_by_machine=machine` raw | Propagates whichever spelling the runner sent into the claim record. |
| 661 | `release_claim` | `row["claimed_by_machine"] != machine` | **Silent miss.** A box that renamed cannot release its own claim -- refused as "claimed by \<other\>". Claim wedged until the stale reaper. |
| 646 | `apply_git_outcome` | writes raw | Same as `try_claim`. |
| 750 | `claim_verdicts_diverge` | `row[...] == machine` | **False divergence.** Shadow audit reports a spurious `diverged=1`. Observability noise. |
| 779 | `log_claim` | `claim_log.machine` raw | Audit-trail split. Append-only history; see §3. |
| 791 | `record_result` | `results.machine` raw | Provenance split. **Deliberately raw** -- see §3. |
| 809/867/895 | `upsert_heartbeat` / `record_status_payload` / `record_shutdown_notice` | `ON CONFLICT(machine)`, and `machine` is **PRIMARY KEY** (`schema.sql`) | **Duplicate.** Two rows for one box. Downstream: two `runner_heartbeats/*.json` files, one of which never reports again. |
| 1078 | `fetch_pending_commands` | `commands WHERE machine=?` | **Silent miss.** Command sits pending forever. |
| 1089 | `ack_command` | `row["machine"] != machine` | Silent miss. Runner cannot ack a command addressed to its other name. |

### 1b. `app.py` -- ingest boundary

Every one of these takes `body.get("machine")` (or the token label) and passes it **straight through**:

| Line | Endpoint | Note |
|---|---|---|
| 409 | `POST /claim` | `machine = body.get("machine") or machine_tok` |
| 467 | `POST /claim/release` | ditto |
| 489 | `POST /heartbeat` | ditto |
| 516 | `POST /status` | ditto |
| 540 | `POST /shutdown_notify` | `machine` **required**, token label never substituted |
| 581 | `POST /claim_fence/clear` | ditto |
| 608 | `POST /commands/issue` | ditto -- **the serve.py path below** |
| 649 | `POST /commands/ack` | `or machine_tok` |
| 679 | `POST /result` | `manifest.get("machine") or machine_tok` |
| 260 | `GET /commands?machine=` | exact match |
| 313 | `GET /shadow/status` | `ORDER BY machine`; a split shows as two machines |

### 1c. Confirmed: `serve.py` forwards raw on the primary channel

`REE_assembly/serve.py:4578 _coordinator_issue_command(machine, ...)` builds `{"machine": machine, ...}` with no resolution (line 4603), and the caller at 6856 passes `host` verbatim. The **git fallback** at 6868 (`append_machine_command`) is the canonicalised path. So the chip's statement is correct, and the asymmetry is the wrong way round: **the primary channel is the unresolved one, the deprecated fallback is the resolved one.**

---

## 2. Quantification (deliverable 2) -- and an honest limit

**I could not query the hub DB.** This session runs headless on `ree-cloud-5`, which is a *metaworker* box (`ree-metaworker.service`, no `ree-runner.service`). It has no SSH key for `ree@91.98.130.117` (`Permission denied (publickey,password)`) and no coordinator bearer token (only `/etc/ree-metaworker-token.env`, an Anthropic token). The coordinator is reachable and healthy over WireGuard -- `GET /health` returns **200** -- but `GET /shadow/status` returns **401**.

So `claim_log`, `commands`, `experiments`, and `results` row counts **could not be re-measured today**. Per the chip's own instruction I am *not* citing CLAUDE.md's 2026-08-15 numbers as current. **This is the one deliverable I could not complete, and it is the single most useful thing for the reviewing human to run.** Exact command, from the Mac:

```bash
ssh ree@91.98.130.117 'python3 -c "
import sqlite3, collections
c = sqlite3.connect(\"/home/ree/REE_Working/ree-v3/coordinator/coordinator.db\")
for tbl, col in ((\"claim_log\",\"machine\"), (\"commands\",\"machine\"),
                 (\"heartbeats\",\"machine\"), (\"results\",\"machine\"),
                 (\"experiments\",\"machine_affinity\"),
                 (\"experiments\",\"claimed_by_machine\")):
    rows = c.execute(\"SELECT %s, COUNT(*) FROM %s GROUP BY 1 ORDER BY 2 DESC\" % (col, tbl)).fetchall()
    print(tbl, col, rows)
"'
```

### What I *could* measure -- the phase3 git mirrors

`runner_heartbeats/` and `runner_status/` **are** the `heartbeats` table materialised by `phase3_heartbeat_writer`, so they are a direct proxy for that table's key set.

`heartbeats` key set (from `runner_heartbeats/`, `origin/master`): `DLAPTOP-4.local`, `ree-cloud-1`, `ree-cloud-2`, `ree-cloud-3`, `ree-cloud-4`, `ree-cloud-5`. **No split -- one row per box.**

Each payload carries **both** a resolved `machine` and a raw `hostname`, and they disagree on three of six boxes:

| file | `machine` | `hostname` (raw `gethostname()`) |
|---|---|---|
| `DLAPTOP-4.local.json` | `DLAPTOP-4.local` | **`DLAPTOP-5.local`** |
| `ree-cloud-1.json` | `ree-cloud-1` | **`ree-worker-1`** |
| `ree-cloud-3.json` | `ree-cloud-3` | **`ree-worker-3`** |
| `ree-cloud-2/4/5.json` | matches | matches |

**This is the central finding of the investigation.** The coordinator's raw string matching is currently safe *only because every runner is launched with an explicit `--machine` override that pre-resolves the name upstream*. The DB is clean (CLAUDE.md's 10533-vs-0) not because the coordinator canonicalises, but because deployment convention compensates for it. That invariant is real but external to the coordinator.

It is not purely hand-typed, which is better than the chip assumed: `coordinator/deploy/systemd_dropin_drift.py:433` already asserts `ExecStart` pins `--machine <affinity>` and reports `DIFFERENT` when absent. So there **is** a guard -- on the workers' systemd units.

`experiment_queue.json` on `origin/main` currently holds **0 items**, so there is no live `machine_affinity` / `claimed_by.machine` data to measure.

One apparent split I checked and **withdraw**: `runner_status/` contains both `ree-cloud-3.json` and `ree-worker-3.json`. The latter was last written **2026-05-19 by the legacy `auto-sync:` runner pusher**; `ree-cloud-3.json` is live `phase3-heartbeats:` (2026-08-15). It is pre-Phase-3 residue, not a live coordinator split.

### The dated hazard -- this is scheduled, not hypothetical

| event | when |
|---|---|
| Mac heartbeat last written, `machine=DLAPTOP-4.local`, `state=running`, `current_exq=V3-EXQ-906c` | **2026-08-09 19:52Z** |
| `machine_identity.py` + runner wiring landed (`eba199da`) | **2026-08-15 08:27Z** |

`experiment_runner._get_machine_name()` (line 2957) is now `canonical_machine_name(override or gethostname())` -- **it canonicalises the override too**. So the Mac's runner has not restarted since the resolver landed, and **on its next start it will POST `machine=DLAPTOP`, not `DLAPTOP-4.local`.** Against today's coordinator that means:

1. a **new** `heartbeats` row `DLAPTOP` (PK is `machine`), leaving `DLAPTOP-4.local` as a row that never reports again -- and a stale `runner_heartbeats/DLAPTOP-4.local.json` beside a new `DLAPTOP.json`;
2. any claim still recorded `claimed_by_machine='DLAPTOP-4.local'` becomes **unreleasable** by the Mac (`release_claim`, line 681) and **reapable out from under it** (`_has_fresh_owner_heartbeat`, line 239);
3. queue entries pinned `machine_affinity: "DLAPTOP-4.local"` stop matching (`_affinity_ok`, line 145);
4. pending `commands` rows addressed to `DLAPTOP-4.local` become undeliverable.

Blast radius today is limited -- the queue is empty and `V3-EXQ-906c` is no longer in it. **The mechanism is unchanged by that luck.** This fires on the next Mac runner start with a non-empty queue.

---

## 3. Where resolution belongs (deliverable 3)

**Recommendation: canonicalise at the INGEST BOUNDARY ONLY. Leave all stored history untouched.**

### Canonicalise (mutable coordination state -- these decide behaviour)

- `POST /heartbeat`, `/status`, `/shutdown_notify`, `/claim_fence/clear` -> canonicalise before `upsert_heartbeat` / `record_status_payload` / `record_shutdown_notice` / `record_claim_fence_clear`.
- `POST /claim`, `/claim/release` -> canonicalise before `try_claim` / `evaluate_claim` / `release_claim`.
- `POST /commands/issue`, `GET /commands`, `POST /commands/ack` -> canonicalise both the issue and the fetch side, **or neither**. Canonicalising one alone converts a *delivered* command into an undeliverable one.
- `_affinity_ok` -> `same_machine(affinity, machine)`, mirroring `experiment_runner._affinity_matches` (line 2976) which already does exactly this.
- `serve.py:_coordinator_issue_command` -> resolve, matching what the git fallback already does.

### Do NOT canonicalise (append-only provenance -- these record what happened)

- **`results.machine`.** CLAUDE.md is explicit that result manifests are "aliased on READ, never rewritten," because editing one to claim a run happened under a name the box was not reporting is falsifying provenance. `results` is that same record in DB form.
- **`claim_log.machine`.** The chip asks whether the same argument applies. **It does, and slightly more strongly.** `claim_log` is the *shadow audit* -- one row per claim attempt recording what git decided vs what the coordinator would have. Its entire purpose is to be a faithful record of what was reported at the time. Rewriting it would destroy the only evidence that a split ever occurred -- which is precisely the evidence CLAUDE.md's 10533-vs-0 argument rests on.
- **No backfill / migration of existing rows.** The alias runs forward (`DLAPTOP-4.local` -> `DLAPTOP`), so historical rows keep resolving on read. Nothing needs rewriting for matching to work.

### The residue this leaves, stated rather than papered over

Ingest-only canonicalisation means the *live* `heartbeats` row for the Mac migrates from `DLAPTOP-4.local` to `DLAPTOP` on first post-change heartbeat, and the old row is orphaned. That is the same one-off telemetry-filename residue `machine_identity.py` already documents (lines 105-111): let the stale pair age out, or delete once the DB holds no rows under the old name. **Do not hand-rename the file** -- it is materialised from the DB and would be reverted on the next tick.

### Sequencing note

There is a genuine ordering choice. If the coordinator canonicalises *before* the Mac's runner restarts, then the moment it restarts both sides already agree and the transition is clean. If the runner restarts first, the coordinator briefly holds two rows. **The cheaper order is coordinator-first**, which argues for deciding this before the Mac's next runner start rather than after.

---

## 4. Risk of getting it wrong (deliverable 4)

**The catastrophic failure is collapsing two genuinely distinct boxes.** `ree-cloud-1..5` and `ree-worker-1..4` differ only in a trailing digit that *is* their whole identity. Collapsing them would give the fleet one shared heartbeat row (PK `machine`), make every claim collide, and route every experiment's affinity to the wrong box -- a fleet-wide outage, not a cosmetic bug.

`machine_identity` is already built against exactly this: `SUFFIX_BLIND_BASES` is an **allowlist** holding one entry (`dlaptop`), and `canonical_machine_name` is an exact passthrough for everything else. Roughly half of `tests/contracts/test_machine_identity.py` (22 tests) are negative controls pinning the fleet as distinct -- `test_cloud_fleet_names_pass_through_unchanged`, `test_worker_fleet_names_pass_through_unchanged`, `test_distinct_cloud_workers_are_distinct_machines`, `test_unknown_numbered_host_is_not_collapsed`.

**But the chip is right that a coordinator-side change must be tested against that, not assume it.** The property to pin coordinator-side is: *for every pair of distinct fleet names, ingest canonicalisation must still produce distinct DB keys.* That is a new contract test in `coordinator/`, not an inherited one.

Second risk, specific to the command channel: **canonicalising the issue side without the fetch side (or vice versa) silently breaks command delivery** -- turning a working path into a silent miss. Both must land together, and a test must assert issue->fetch round-trips across a drifted name pair.

Third, the mundane one: **`coordinator/` is not collected by a bare `pytest tests/` run.** The gate must be `remote_pytest.sh` (which names all six roots) plus `python3 coordinator/phase3_preflight.py`, on a cloud worker, per CLAUDE.md.

---

## 5. The `EXACT_ALIASES` / `ree-worker-N` <-> `ree-cloud-N` question (deliverable 5)

`EXACT_ALIASES` is empty, so `same_machine("ree-worker-3", "ree-cloud-3")` is **False** today, while the two names denote one physical box (hcloud name vs affinity name). Measured above: `ree-cloud-1` and `ree-cloud-3` both report a `hostname` that is their `ree-worker-N` spelling.

**Recommendation: do NOT generalise this now. Keep it separate from the coordinator change.**

The reason is not caution, it is that the current state is a **deliberate, contract-pinned decision**, not an oversight. `tests/contracts/test_machine_identity.py:93`:

```python
def test_hub_dual_naming_is_deliberately_NOT_handled_here():
    # The hub really is one box answering to both, but that accommodation lives
    # in runner_remote_control._PHASE3_HUB_HOSTNAMES and is scoped to one gate.
    # Folding it in here would silently rename the hub's heartbeat file. Keep the
    # two mechanisms separate.
    assert not mi.same_machine("ree-cloud-1", "ree-worker-1")
```

Adding `EXACT_ALIASES` entries would **fail that test by design** and would rename the hub's heartbeat file as a side effect. It also edits the canonical resolver, requiring the contract suite plus re-vendoring all three copies together (`ree-v3/` canonical -> `REE_assembly/`, `scripts/`) and an `audit_vendored_copies.py` run.

Crucially, it is **not needed for the coordinator fix**: the runners already send the `ree-cloud-N` affinity spelling via `--machine`, enforced by `systemd_dropin_drift.py`. The `ree-worker-N` spelling never reaches the coordinator as a `machine` value -- only as the informational `hostname` field. **Bundling this into the coordinator change would add the one genuinely fleet-dangerous edit to an otherwise narrow fix.**

If it is wanted later, it is its own chip, with its own held-out check against that test's stated rationale.

---

## 6. Recommendation summary

| | |
|---|---|
| **Do** | Canonicalise at the coordinator ingest boundary (`app.py` handlers + `_affinity_ok`), and in `serve.py:_coordinator_issue_command`. |
| **Do** | Land command-channel issue + fetch + ack together, or not at all. |
| **Do** | Add a coordinator-side contract test that distinct fleet names stay distinct keys. |
| **Don't** | Canonicalise or backfill `results.machine` or `claim_log.machine` -- provenance. |
| **Don't** | Add `EXACT_ALIASES` entries -- separate, contract-pinned, fleet-dangerous. |
| **Don't** | Hand-rename telemetry files -- DB-materialised, reverted next tick. |
| **Gate** | `integration/<slug>` branch; `remote_pytest.sh` (all six roots) + `coordinator/phase3_preflight.py`; **not** the laptop, **not** a bare `tests/`. |
| **Timing** | Cheaper before the Mac's next runner restart than after. |

**Estimated size:** small -- roughly a one-line resolution at ~11 ingest points plus one `_affinity_ok` change, one `serve.py` line, and a new coordinator contract test. The investigation, not the patch, was the hard part.

**This session deliberately did not implement it.** The chip asked for a human decision before behaviour change; being headless, that decision is carried by chip `chip-20260816-coordinator-identity-ingest-decision`.
