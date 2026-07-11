---
title: "SHP Process Retrospective"
nav_exclude: true
---

# Status/History Plane Separation (SHP) — Process Retrospective

**Pipeline id:** `status_history_plane` (see `status_history_plane_separation_design.md`)
**Written:** 2026-07-11
**Author session:** mystifying-bose-6bb813 (SHP-2 executor)
**Promotes/demotes:** NOTHING — this is a process retrospective, not a claim.

> **Deliberately carries NO `closure_plan:` frontmatter** — a tooling/governance
> retrospective, not a v3-substrate closure plan; must not be auto-discovered by
> `generate_closure_snapshot.py` or counted toward the v3 closure %.

---

## 1. Outcome

The whole SHP program (SHP-0 … SHP-7) is complete and verified on `origin/master`:

| Phase | What | Verified deliverable |
|---|---|---|
| SHP-0/1 | Audit + contract + read-only shadow projector | `project_status_head.py` |
| **SHP-2** | Collapse **every** closure-plan blob → `live:`+`join:` | diff-vs-blob at-risk refs **→ 0**; status-plane drift **0/98** |
| SHP-3 | Snapshot-append + both-views | `governance.sh` Step 3c-bis-4 (change-only append + committed sidecars); `serve.py` Q2=both query |
| SHP-4 | Port to `claims.yaml` | `live_status` derived on all 878 claims (reading-drift 0); `last_reviewed` record-once; `claims_live_status_drift.py` |
| SHP-5 | Architecture-doc `**Status:**` from claims.yaml | `apply_status_frontmatter.py` + `claims_doc_drift.py` |
| SHP-6 | Entry-doc routing | generated `CURRENT_FRONT.md` |
| SHP-7 | Retire abandoned manual docs | `generate_status_stubs.py` |

SHP-2 was executed across three sessions (`vigorous-yalow` + this one); SHP-3/SHP-4
were completed in parallel background sessions fanned out from `spawn_task` chips and
landed the same day. `validate_claims --strict` OK; status-plane drift `0/98` still
holds after SHP-3/4 landed.

---

## 2. What the process got right (keep as a pattern)

1. **Non-destructive razor enforced *in code*.** `shp2_collapse_plan.py` REFUSES to
   collapse any node not first lifted verbatim into the append-only
   `status_snapshot.v1.jsonl`. Every collapse is therefore reversible from the log —
   the difference between a migration and a data-loss event.
2. **Body-byte-identical gate is a proof, not a vibe.** Hashing the plan body *below*
   the frontmatter before/after proves the collapse touched ONLY frontmatter. Cheap,
   strong, run every plan (`db354a93`, `054aa352`, `005daaa6`, `f9636f7d`, `39087937`,
   `0342ab21`).
3. **Drift-as-re-projection.** `check_closure_drift.py` re-derives every collapsed
   `live:` and compares to the stored value — the derived fields stay falsifiable
   against their source events.
4. **One shared projection path.** Collapse, drift-check, governance, and the SHP-4
   `live_status` derivation all route through `build_projections` — they cannot
   silently disagree.
5. **Fan-out worked.** SHP-2 → chips → SHP-3/SHP-4 completed in parallel, claim-
   arbitrated against file conflicts; the program closed in one sitting.

---

## 3. Friction / weaknesses observed (all operational, not design)

1. **Stale git locks are a recurring hazard.** A `.git/index.lock` blocked commits
   **twice** (~50 min stale, from crashed background writers on the shared Mac
   checkout). Cleared by hand after confirming no live git process. Structural to
   editing coordination data against a live shared checkout.
   **Fix landed:** age-gated stale-lock pre-check folded into the `/session-land`
   skill (clear only when >5 min old AND no live `git commit/add/rebase/merge/pull/push`
   process). Longer-term option: do coordination-data edits from an isolated worktree.
2. **`git commit -- <pathspec> -m "msg"` ate the `-m`** — everything after `--` is a
   pathspec, so the message and flag became (nonexistent) pathspecs; one wasted commit.
   **Fix landed:** `/session-land` skill now states the rule **`-m` before `--`**.
3. **Perpetually-dirty working tree.** Derived artifacts (closure_status/drift/
   dashboard) regenerate on every verify run and are correctly left uncommitted — which
   makes the `git show --stat HEAD` = "exactly the files I intended" post-commit gate
   *load-bearing*, not optional.
4. **No wrapper — 4 tools + 6 gates by hand, per plan.** Fine for 7 plans with care;
   invites a skipped gate at scale, and the same manual shape recurred in SHP-4.
   **Fix landed:** `scripts/shp2_collapse_and_verify.py` runs backfill → collapse →
   all 5 gates for ONE plan and exits non-zero on any gate failure (it does **not**
   loop over plans — honours the design doc's "do not batch blindly"). Smoke-tested:
   PASS on an already-collapsed plan (idempotent no-op), exit 1 on a missing plan.

---

## 4. Design note (why sequencing mattered)

SHP-2 *without* SHP-3 is a latent staleness window: collapsed `live:` blocks are
derived but stored in-file, guarded only by a **warn-only** drift check between
governance runs. Landing SHP-3 (regenerate + change-only append every cycle) the same
day closed the loop. General lesson: when you collapse a hand-maintained field to a
derived one, wire the regenerator in the same push, or the derived value silently rots
with only a soft guard.

---

## 5. One open signal

`claims_live_status_drift` reports `provenance_drift=1` (a single claim whose
`live_status` provenance differs from the re-derived value) — warn-only; everything
else clean (`reading_drift=0`, `unstamped=0`, `validate_claims --strict` OK). Worth a
human glance next governance cycle; belongs to SHP-4's high-contention `claims.yaml`
domain, so not edited here uninvited.

---

## 6. Reusable checklist (for any future field collapse of this shape)

1. Register a `TASK_CLAIMS` claim covering the target path **before** editing (heartbeat
   autostash reverts uncommitted `evidence/`/`docs/claims/` edits without an active claim).
2. `scripts/shp2_collapse_and_verify.py --plan <plan> --by "<label>"` — one plan; read the result.
3. Land pathspec-limited: `git commit -m "..." -- <plan> <log>` (**`-m` before `--`**);
   then `git show --stat HEAD` = exactly the files intended.
4. Leave derived artifacts (closure snapshot/drift/dashboard) for governance (derive-only).
5. Update the design-doc status table (the resume primitive) in the same commit.
