# Coordinator Cutover Durability Review

**Reviewed:** 2026-08-30T10:12:09Z, session `cycle-review-20260830-g1` (user-present), Fable 5.
**Chip:** chip-20260828-cutover-durability-review. **Method:** adversarial re-derivation of each
protection the synchronous git writes provided, against the code as of REE_Working
`origin/master` @ the 2026-08-30 tip and ree-v3 `origin/main` (line-level verification by a
dedicated research pass; file:line cites throughout are from it), plus this session's own live
incident evidence from executing Campaigns C and D on the same machinery earlier today.

**Two stale premises in the chip brief, corrected first:** (1) the umbrella wedge cited as live
was cleared 2026-08-30T06:32Z (healer, user-authorised, per-commit content audit) — the working
tree read for this review is current; (2) "nobody has audited this change" was true on 08-28 but
the intervening W-campaigns landed substantial hardening (post-commit self-verification for all
mutating subcommands `e31d83f1d`, hollow-ack verification extended to close + chip verbs
`92b234f76`/`269e518d3`, coordinator-side arbitration for `check` `f13123fb3`, tombstoned renews
`047307a`, 3-way-merge ingest authority `ce50a937b9`, remote-tip wedge gate `f0eab5fc6`). This
review consolidates what REMAINS, and credits what moved.

## Summary verdict table

| Protection | Old mechanism | New fate | Severity |
|---|---|---|---|
| (a) Claim-first durability | same-step commit+push (strand-prone, A-17) | **MOVED-BETTER**: DB row committed under `BEGIN IMMEDIATE` before the 200 (db.py:1034); materializer renders ≤2min; atomic 1-of-N arbitration server-side | PASS |
| (a') Ack honesty | commit visible in git log | **DEGRADED-THEN-FIXED**: hollow-ack incident (amend, 2026-08-28) → per-verb ack verification + local pre-resolution; **residual: `renew` has NO ack verification** | MEDIUM (renew) |
| (b) Chip survival past session death | git-tracked TASK_CHIPS.json | **MOVED-EQUIVALENT**: DB + render; claim_rescue layer proven live 2026-08-30 (splice-into-origin with containment/key-conflict/adopt guards, claim_rescue.py:34-104); W5a episodic chips are coordinator-ONLY by documented design | PASS |
| (c) Sweep/RMW-contamination detection | ree_commit per-item delta on client commits | **SPLIT**: coordinator path — no client commit exists and the materializer is reset-hard+rematerialize (immune); **fallback path — hazards survive unchanged**, confirmed post-cutover (`f34963462f`, 7-row destructive delete) | HIGH (fallback; owner exists) |
| (d) Consumers of git state | fresh-by-construction after own commit | **DEGRADED-THEN-FIXED** for the detector population (statusregress 52-chip 100%-FP class, staleclaim C_no_trace, strandedwt registry diffs — all fixed 2026-08-30); `close --from-commit` unaffected; prune correctly skipped; `chip_ledger list` defaults to the local render (opt-in `--live`) | LOW residual |
| (e) Cross-machine visibility | push→pull of the file | **MOVED with a measured gap**: hub render timer 2min (state-change-only, "visibility lag not a race window") **but the second leg — each box's umbrella pull — has NO periodic puller anywhere in code**; measured unbounded 2026-08-29 (27 of 145 entries absent locally, 6 active). `open`/`check` now consult the coordinator; **`chips_open_work` (a scaler shutdown veto input) reads the LOCAL file** | MEDIUM |
| (f) Unreachable-hub behaviour | n/a (git was primary) | **SURVIVES**: transport `post()` never raises — every failure → `None` → byte-identical git fallback (coordinator_transport.py:351-390, 5s timeout); per-verb suppression allowlists are narrow; only 409 and renew's `would_lose_ownership` are binding refusals; accept-then-git-fail is compensated (release-after-failed-open/claim) | PASS |
| (g) Hub single point of failure | none (git was distributed) | **GUARDED, with named residue**: scaler HUB_NAME skip verified; WAL + explicit transactions; materializer oneshot+timer resumes idempotently from DB; ingest-before-render makes each render a superset of origin; daily DB pull-backup to the Mac (no Hetzner snapshots — that measurement is the backup's raison d'être). DB loss ⇒ current STATE reconstructs from git (shadow-sync git→DB), but claim_log (29.7k rows), command audit, drift history, and >24h-aged done-claims do NOT | MEDIUM (accepted trade, documented) |
| (h) Wedge interaction | commit strand → wedge inputs | **IMPROVED**: suppression removes claim/chip writes from the strandable population entirely. Live evidence today: 5 of this session's 6 umbrella pushes of OTHER files stranded under materializer churn and needed throwaway-worktree recovery, while ZERO claim/chip writes stranded — the strand pressure moved to ordinary commits racing the materializer. R1 re-measure due 2026-09-04 | LOW (monitored) |

## Non-PASS findings

### F1 (HIGH, existing owner): the git-fallback path retains every pre-cutover loss hazard
The fallback is deliberately byte-identical to the old path — that is its virtue when the hub is
down and its hazard the rest of the time. Confirmed post-cutover instance: `f34963462f`, a
`record` that printed "already recorded" yet committed a 7-row destructive delete (the A-05
sweep class), PLUS the statusregress detector's structural deletion blindness (rows present only
in the parent are never iterated — established by today's campaign research and recorded in its
design doc). **Owners already exist — do not re-route:**
chip-20260828-chipledger-noop-record-committed-destructive-delete (consolidated plan C.3) and
the deletion-blindness residual recorded in detector_fp_campaign_staged_20260830.md.

### F2 (MEDIUM, NEW): `renew` is the one suppressed verb with no ack verification
Every other suppressed verb verifies the coordinator's echoed entry before trusting suppression
(the 2026-08-28 hollow-ack campaign); `renew` trusts the bare `"ok"` (task_claim.py:4893, no
`verify_renew_coordinator_ack` exists). Partially bounded by design — the CLI passes
`new_claimed_at` explicitly and the server tombstone-closes the old stamp — but the
malformed/wrong-row ack class that bit `amend` is unchecked here. Routed to the consolidated
update plan as Campaign C item C.7 (not flagged via governance_flag.py: that registry is the
claims-evidence plane; this is coordination infra, and the plan is the standing router).

### F3 (MEDIUM, NEW): the drift log has no reader and `diverged=1` no alarm
`task_claim_chip_drift_log` (written by the 10-min shadow-sync, deliberately not by the
materializer) is the designed detection channel for DB↔git divergence — including the DB-side
corruption class that fix (ii) of the detector campaign accepts as its blind spot — and grep
finds NO programmatic consumer; it is "durable soak evidence a human reads", which post-soak
means nobody. A hygiene-tick source reading the last N drift rows and chipping on `diverged=1`
is the natural shape. Routed to the plan as C.8.

### F4 (MEDIUM, NEW): render visibility's second leg is unbounded, and one scaler veto rides it
The hub half of the visibility gap is bounded (2-min timer); the per-box half is not — no
periodic umbrella puller exists in code, so a box sees new registry state only when something
happens to pull (healer cycles do, opportunistically). Two consequences already observed: the
2026-08-29/30 false NOT-THE-OWNER stops (client-side re-check fixed today, `41ef73e7f`), and an
unmeasured blind window on ree-cloud-4's `chips_open_work` scaler-shutdown veto
(ree_metaworker_heartbeat.py:1556 reads the LOCAL file). **This is also where hub load becomes a
durability input**: at today's measured hub load 4.0 (2 vCPU, an experiment at 143% CPU beside
the coordinator + writers + materializer), every leg — API latency, render cadence adherence,
push success — degrades together. Recommendation, endorsing the user's own 2026-08-30 proposal:
**retire the hub from the experiment pool** (graceful stop after V3-EXQ-959 completes, then
disable ree-runner on cloud-1). Routed to the plan as D.7, pending the user's go.

### F5 (LOW, residue notes)
- `chip_ledger.py list` defaults to the local render; `--live` exists but is opt-in — readers
  that need freshness must know to ask (documented, acceptable).
- `PRAGMA synchronous` is never set explicitly; power-loss durability rests on SQLite's default
  (FULL) — assumed, not measured. One-line explicitness would close the question.
- chip `attach`/`amend-prompt`/handoff/`archive` have no coordinator mirror at all (CLAUDE.md
  already documents this); the archive's route-C unprovability has an owner
  (chip-20260828-chiparchive-uncovered-by-every-proof-route, plan C.5).
- Runtime arming state (`~/.ree_coordinator_client.json` per box, `REGISTRY_WRITER_MODE` on
  cloud-1) and the shadow-sync timer's live enablement are machine-local and were not verified
  from code; a fleet spot-check belongs in the next healer cycle, not this review.

## Overall verdict
The cutover's core promise — the ack IS durable, arbitration IS atomic, and the materializer
IS lossless-by-construction (ingest-before-render, verbatim entry_json, push-gated bases) —
**holds, and in several dimensions the new topology is strictly stronger than the git path it
replaced** (no strandable claim writes, 1-of-N arbitration, claim_rescue). The genuine remaining
exposure is concentrated in three places: the deliberately-preserved fallback path (F1, owned),
the unbounded second leg of render visibility (F4, coupled to hub load), and two small
verification/alarm gaps (F2, F3). Nothing found warrants rollback; everything found has a named
owner or a plan slot.
