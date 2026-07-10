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

Later kinds (SHP-3) will add the projector's own `status_snapshot/v1` records —
the derived `live` head per node at each `governance.sh` run — onto the **same log**,
so "what did we believe the front was on DATE" becomes answerable. SHP-3 also wires the
query API (`serve.py`) and the generated `*_history.md` sidecars over this log.

> This log is authoritative history. Do not rewrite lines. To correct a record, append
> a new one.
