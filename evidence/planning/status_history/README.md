---
title: "Status-history append-only log"
nav_exclude: true
---

# `status_history/` — the append-only status-plane log

Part of **`status_history_plane`** (see
[`../status_history_plane_separation_design.md`](../status_history_plane_separation_design.md)).

## `status_snapshot.v1.jsonl`

Append-only, one JSON record per line. This is the **history plane** for status:
records are written once, never edited, never regenerated.

Current record kinds:

- **`shp2_backfill_lift`** (SHP-2) — written by
  [`../../../scripts/shp2_backfill_snapshot.py`](../../../scripts/shp2_backfill_snapshot.py)
  immediately **before** a closure-plan node's hand-written `phase:` / `owner_exq:` /
  `awaiting:` blobs are collapsed to the two-plane `live:` + `join:` schema. It is the
  non-destructive migration razor (design §5): the full raw node is archived verbatim
  (`archived_node`) and the un-derivable governance-apply `master <hash>` provenance is
  pulled out into `at_risk_history_bits`, so the collapse loses nothing. Idempotent
  (one record per `node_id`); PROMOTES/DEMOTES NOTHING.

- **`status_projection`** (SHP-3) — written by
  [`../../../scripts/promote_status_history.py`](../../../scripts/promote_status_history.py),
  wired into `governance.sh` (Step 3c-bis-4). Each cycle appends the projector's own
  derived `live` head per node at that run's timestamp — the `status_snapshot/v1` record
  contract term 4 calls for — onto **this same log**, so "what did we believe the front
  was on DATE" is answerable (take the newest record whose `projected_utc <= DATE`).
  Append is **change-only**: a node is written only when its projected `live` differs
  from its most recent `status_projection` record (a stable run with no new events
  appends ZERO), mirroring the state-change-only heartbeat design that retired the
  git-history-bloating liveness tick. PROMOTES/DEMOTES NOTHING.

## `history/` — committed per-plan `*_history.md` sidecars

Regenerated each `governance.sh` run by `promote_status_history.py` (via the shared
`project_status_head.write_history_sidecars`): one pointer-index sidecar per closure
plan, **newest last**, over this log + the autopsy/manifest/decision events. Server-free
human view of the history plane. Generated; never hand-edited.

## Query API (Q2=both)

`serve.py` `/api/status_history?node=<node_id>` (or `?claim=<claim_id>`) returns BOTH the
collapsed-plan `live:` head (status plane, read from the `*_plan.md` frontmatter) AND the
appended `status_snapshot/v1` history slice + SHP-2 backfill-lift archive (history plane,
read from this log) — the design's "Q2 = BOTH" query.

> This log is authoritative history. Do not rewrite lines. To correct a record, append
> a new one.
