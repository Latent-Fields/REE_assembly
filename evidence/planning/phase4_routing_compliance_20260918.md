# PHASE-4 routing compliance measurement (DP-12)

- **Measured:** 2026-09-18T10:49:31Z, on DLAPTOP, session `dp12-routing-compliance`
- **Chip:** `chip-20260918-dp12-routing-compliance-measurement`
- **Answers:** `phase4_commit_intake_design.md` DP-12, which gates section 10 step 8
  (the doctrine/decommission pass) on this count.
- **Scope limit, stated up front:** this is a MEASUREMENT. It changes no flag,
  restricts no remote, and retires no doctrine. Section 8 is untouched.

## 0. What DP-12 asked, and the one-line answer

> Does every writer of a routed file actually route?

**No.** Five of the ten flipped files have a clean record since their route went
live; five do not. One file -- `evidence/planning/experiment_proposals.v1.json`
-- is **4.4% routed**: its flag is armed, the hub is applying intents, and 58 of
the 68 commits to it since the route went live came from writers that have no
coordinator call site at all, on three different boxes. Retiring that file's
defences on the strength of its armed flag is precisely the net-negative case
DP-12 describes.

## 1. Method

Read-only over `git log`; no service built, no DB written. Two repos:
`REE_Working` (umbrella) and `REE_assembly`.

### 1.1 The discriminator is NOT the commit-message prefix

The chip proposed recognising hub-writer commits by their `phase2b-registry:` /
`phase3:` / `phase3-queue:` prefixes. **That is correct only for the
append/registry materializer.** The CAS route (`/intent/replace`,
`ree-v3/coordinator/git_intent.py`) applies the commit on the hub using the
CLIENT's own message, so a fully-routed CAS commit carries the client's prefix
(`igw-ledger: ...`) and is indistinguishable from a git-path commit by subject.
Using prefixes alone would have scored every routed igw commit as non-compliant.

What the CAS route does add is a pair of **trailers**, from
`git_intent.py:_trailer_message()`:

```
igw-ledger: complete igw-246-literature-proposal-for-mech-039

session_id: igw_routine_tick
machine: DLAPTOP-4.local
```

Committed by `REE Automation (Hub)`. So the classifier is:

| bucket | test |
|---|---|
| `hub_materializer` | subject starts `phase2b-registry:` |
| `hub_cas_intent` | committer contains `Hub` AND body has both `session_id:` and `machine:` trailers |
| `hub_phase3` | subject starts `phase3:` / `phase3-queue:` -- a hub writer, but the PRE-EXISTING Phase-3 daemon, not a phase-4 route |
| non-hub git write | everything else; sub-classified below |

### 1.2 Degraded-fallback vs never-routed

DP-2 makes the git path a permanent, by-design degrade route, so a git commit is
only a DP-12 hazard if the writer could never have routed in the first place.
The test used is **structural: does the writing tool contain a
`coordinator_transport` call site for that path?**

- **Routing-capable** (git commit therefore = degraded fallback):
  `task_claim.py` (9 refs), `chip_ledger.py` (20), `igw_routine_tick.py` (20),
  `append_workspace_state_entry.py` (9), `record_recommendation_outcome.py` (5),
  `dispatch_campaigns.py` (13) -- all in `REE_Working/scripts/`.
- **Never-routed** (no call site exists):
  - `chip_ledger.py cmd_archive` -- **0** `coordinator_transport` refs inside the
    function. The section-5 row for the archiver ("coordinator-side archive verb;
    git-side strip retired") is aspirational; the strip still runs on git.
  - `rotate_workspace_state.py` -- **0** refs in the whole file.
  - **Every writer in `REE_assembly/scripts/`.** `grep -rl coordinator_transport
    REE_assembly/scripts/` returns **zero files**. The governance regen, the
    morning digest, `/lit-pull`, `/queue-experiment`'s STOP-GATE and every
    session that hand-edits a proposal are structurally incapable of routing,
    regardless of what the client flags say.

### 1.3 Windows

Three, and the middle one is the trap:

- **`since_route_live`** (per file, from its first hub-applied commit) -- the
  decision-relevant window, and the one section 8 should read.
- **30d / 14d** (trailing, as the chip asked) -- reported for completeness, but
  for any file whose route went live inside the window these MIX pre-cutover
  history with post-cutover non-compliance. `TASK_CLAIMS.json` reads 63.8% routed
  over 30d and 96.9% since route live; the 67 "never-routed" commits in its 30d
  column are all `prune_task_claims_done.py` and wedge-recovery commits dated on
  or before the 2026-08-28 cutover, which stopped that day. The 30d number is not
  a compliance figure.

## 2. Results

`hub` = materializer + CAS intent. `degr` = degraded fallback (routing-capable
writer took the git path). `never` = writer with no coordinator call site.
`route%` = hub / total.

### 2.1 Since route live (the decision-relevant window)

| file | flag | live since | total | hub | ph3 | degr | **never** | route% |
|---|---|---|---:|---:|---:|---:|---:|---:|
| `TASK_CLAIMS.json` | `suppress_git_write` | 2026-08-28 | 3148 | 3050 | 0 | 98 | **0** | 96.9% |
| `TASK_CHIPS.json` | `suppress_git_write` | 2026-08-28 | 2104 | 1996 | 0 | 89 | **19** | 94.9% |
| `WORKSPACE_STATE.md` | `workspace_state_*` | 2026-09-01 | 688 | 616 | 0 | 53 | **19** | 89.5% |
| `RECOMMENDATION_LOG.jsonl` | `recommendation_log_*` | 2026-09-06 | 118 | 117 | 0 | 1 | **0** | 99.2% |
| `scripts/dispatch_campaigns.json` | `dispatch_campaigns_*` | 2026-09-17 | 7 | 5 | 0 | 2 | **0** | 71.4% |
| `evidence/planning/igw_routine_ledger.json` | `igw_ledger_*` | 2026-09-07 | 129 | 128 | 0 | 1 | **0** | 99.2% |
| `evidence/planning/igw_assignments.json` | `igw_assignments_*` | 2026-09-07 | 120 | 120 | 0 | 0 | **0** | 100.0% |
| `evidence/planning/inter_governance_workset.v1.json` | `igw_workset_*` | 2026-09-07 | 85 | 73 | 0 | 2 | **10** | 85.9% |
| `evidence/planning/inter_governance_workset.md` | `igw_workset_*` | 2026-09-07 | 84 | 72 | 0 | 2 | **10** | 85.7% |
| `evidence/planning/experiment_proposals.v1.json` | `igw_proposals_*` | 2026-09-08 | 68 | 3 | 6 | 1 | **58** | **4.4%** |
| `evidence/planning/igw_routine_log.md` | `igw_log_*` = **false** | never | -- | 0 | 0 | -- | -- | 0% |

### 2.2 Trailing windows (as requested; see 1.3 before using these)

| file | 30d tot / hub / degr / never | 14d tot / hub / degr / never |
|---|---|---|
| `TASK_CLAIMS.json` | 4781 / 3050 / 1664 / 67 | 1903 / 1854 / 49 / 0 |
| `TASK_CHIPS.json` | 4657 / 1996 / 2606 / 55 | 1228 / 1183 / 34 / 11 |
| `WORKSPACE_STATE.md` | 1508 / 616 / 665 / 227 | 534 / 497 / 23 / 14 |
| `RECOMMENDATION_LOG.jsonl` | 378 / 117 / 256 / 5 | 154 / 117 / 37 / 0 |
| `scripts/dispatch_campaigns.json` | 10 / 5 / 5 / 0 | 10 / 5 / 5 / 0 |
| `igw_routine_ledger.json` | 250 / 128 / 121 / 1 | 161 / 128 / 33 / 0 |
| `igw_assignments.json` | 227 / 120 / 102 / 5 | 142 / 120 / 22 / 0 |
| `inter_governance_workset.v1.json` | 271 / 73 / 167 / 31 | 110 / 73 / 24 / 13 |
| `inter_governance_workset.md` | 271 / 72 / 167 / 32 | 109 / 72 / 24 / 13 |
| `experiment_proposals.v1.json` | 186 / 3 / 8 / 167 | 96 / 3 / 4 / 83 |
| `igw_routine_log.md` (flag false) | 703 / 0 / 699 / 4 | 313 / 0 / 313 / 0 |

## 3. The non-compliant writers, named

### 3.1 `experiment_proposals.v1.json` -- the finding (58 never-routed, 3 boxes)

Its flag `igw_proposals_suppress_git_write` is `true` and the path IS in
`git_intent.ROUTING`, but only **3** commits have ever been hub-applied. The tick
(`_commit_proposals()`) is one writer among many; the rest are governance and
skill sessions committing through `ree_commit.py` from `REE_assembly`, which has
no coordinator client at all. Committers since 2026-09-08:
`REE Automation (Mac)` 26, `nooarche` 24, **`REE Cloud Worker` 9** -- a
second box, which is the multi-box shape DP-12 names.

Representative:

```
046eaaac236 2026-09-18T11:49 [REE Automation (Mac)] lit-pull ARC-094 object stage: 4 entries ...
7f5e1b99d5f 2026-09-18T08:26 [REE Automation (Mac)] proposals: mark EXP-0783 (MECH-038) blocked_substrate ...
1d203be9d24 2026-09-17T09:02 [REE Automation (Mac)] queue-experiment STOP-GATE: EXP-0755 (MECH-018) blocked_substrate ...
f4aa63b088b 2026-09-17T12:28 [nooarche]            governance: set EXP-0753 execution provenance (GFLAG-0308)
346ebff3540 2026-09-17T19:19 [nooarche]            governance regen: derive-only pipeline output (cycle 2026-09-17 PM)
b234edd8645 2026-09-14T17:13 [REE Cloud Worker]    EXP-0046 (Q-081) blocked_substrate: ...
05da93d4d80 2026-09-14T15:51 [REE Cloud Worker]    INV-093: stage policy_chunking formation-eagerness redesign ...
```

Note also the 6 `phase3:` commits: the Phase-3 governance-derive daemon is a
THIRD writer of this path, independent of the phase-4 route.

### 3.2 `inter_governance_workset.{v1.json,md}` -- 10 never-routed

All from the same source: the derive-only governance regen (9, committer
`nooarche`) plus one `morning-digest` run. The tick's own writes route
correctly (73 of 85). The regen rewrites the workset as derived output and has
no coordinator call site, so every governance cycle re-races the tick on a file
the tick believes is hub-owned.

### 3.3 `WORKSPACE_STATE.md` -- 19 never-routed

16 are `rotate_workspace_state.py`, a clean daily 04:45 cron rewriting the whole
file. This is a *shape* mismatch, not neglect: the WS route is an APPEND
endpoint and rotation is a whole-file truncation, so there is no verb for it.
The remaining 3 are a `reconcile:` strand re-land and two session commits.

### 3.4 `TASK_CHIPS.json` -- 19 never-routed

18 are `chips: strip N archived chip(s)` -- `chip_ledger.py cmd_archive`, daily
at 04:30 via `com.ree.chiparchive`. Section 5 already anticipates this row
("git-side strip retired") and section 5's C7 note already calls out the
resurrection risk of a git-side strip racing the DB-authoritative render. The
verb is not built; the strip still runs on git, daily, against the single
highest-traffic routed file on the fleet.

### 3.5 `igw_routine_log.md` -- the control, and the predicted incident

`igw_log_suppress_git_write` is the one flag still `false`, so its 313 git
commits in 14 days are **by design** (pre-flip dual-write), not non-compliance.
It is nonetheless the clearest demonstration of the split-brain the chip
predicted: `igw_routine_tick` routes the ledger and assignments through the hub
while git-writing the log, so a single logical tick lands as two commits on two
different writers. `d0472b49175` (2026-09-18T11:36, log, Mac, git) and
`60fa0651870` (2026-09-18T10:35, ledger, Hub, CAS trailers) are the same
`igw-246` completion. The Mac-side copy carries
`(cherry picked from commit da7c714f...)` -- it had to be re-landed after being
stranded. At the time of measurement the file is `M` (dirty) in the shared
checkout, which is the state the 2026-09-18 staged-revert incident arose from.

Once `igw_log_suppress_git_write` flips, this writer's 313 commits/14d move to
the hub; until it does, the igw slice is not a slice, it is a pair.

## 4. Decommission verdict per file (input to section 8; NOT applied here)

Criterion used, from the chip: **zero never-routed commits since the route went
live.** Degraded-fallback commits do not disqualify -- DP-2 makes them the
design.

| file | never-routed | section-8 verdict |
|---|---:|---|
| `TASK_CLAIMS.json` | 0 | **candidate** |
| `RECOMMENDATION_LOG.jsonl` | 0 | **candidate** |
| `igw_routine_ledger.json` | 0 | **candidate** |
| `igw_assignments.json` | 0 | **candidate** |
| `scripts/dispatch_campaigns.json` | 0 | **candidate, but only 7 commits / 1 day of route life** -- clean by absence of evidence, not by evidence of absence. Do not decommission on this window. |
| `TASK_CHIPS.json` | 19 | **NOT ready** -- build the archive verb first |
| `WORKSPACE_STATE.md` | 19 | **NOT ready** -- rotation has no verb |
| `inter_governance_workset.v1.json` / `.md` | 10 each | **NOT ready** -- governance regen unrouted |
| `experiment_proposals.v1.json` | 58 | **NOT ready by a wide margin** (4.4% routed) |
| `igw_routine_log.md` | n/a | not routed at all; flag still false |

The four clean candidates share a property worth stating: each has essentially
ONE writer, and that writer lives in `REE_Working/scripts/`. Every non-compliant
file has at least one writer in `REE_assembly/scripts/` or a cron that rewrites
rather than appends. **Compliance tracks writer topology, not flag state.**

## 5. The structural finding, above the per-file counts

DP-12 frames the hazard as "one non-compliant writer on one box". The measurement
says the shape is narrower and more tractable than that:

**Every never-routed commit in this measurement comes from one of exactly three
populations**, and none of them is a stray session that forgot:

1. **`REE_assembly/scripts/` writers** -- zero files in that directory import
   `coordinator_transport`. The coordinator client exists only in the umbrella
   repo. Any routed path that a REE_assembly tool also writes is structurally
   un-routable today.
2. **Whole-file rewriters with no matching verb** -- `rotate_workspace_state.py`
   against an append-only endpoint, `cmd_archive` against a registry with no
   archive verb. Both are clean, scheduled, single-purpose crons; neither is
   misbehaving.
3. **Human/session editorial commits** on `experiment_proposals.v1.json` and the
   workset, which are governance's normal work.

That is good news for enforcement and bad news for the flag-as-signal: none of
these is fixed by instruction or by push restriction, and all three are visible
statically. **The armed flag is not evidence the route is exclusive** -- for
`experiment_proposals.v1.json` it is 95.6% wrong.

A cheap standing check follows from (1): `grep -rL coordinator_transport` over
the writers of each routed path. It would have flagged proposals and the workset
the day their flags were armed.

## 6. Residuals and what this measurement cannot see

- **Degraded-fallback is inferred, not observed.** git log cannot distinguish
  "hub was unreachable" from "this verb has no coordinator mirror" (CLAUDE.md
  A-94). The supporting evidence is temporal: `TASK_CLAIMS.json`'s 98
  degraded commits since cutover cluster hard (40 on the cutover day itself, 29
  on 2026-09-14, 9 on 2026-09-16, **0 on 09-17 and 09-18**), which is an outage
  signature rather than a structural gap, and all four verbs involved
  (`open` 61, `close` 47, `amend` 4, `renew` 5) do have mirrors.
- **The authoritative source was not reachable.** `git_intent.record_git_intent`
  logs every submitted intent with its verdict (`not_routed`,
  `validation_failed`, `cas_conflict`, applied) into the hub DB, and that table
  would settle the degraded-vs-structural question directly. There is no read
  endpoint for it in `ree-v3/coordinator/app.py`, and this box has no ssh key
  for the hub. **Recommended follow-on: add a read-only
  `GET /intent/log` (or run the query hub-side) and re-run section 6's
  degraded-fallback split against it.** That is the one piece of machinery this
  measurement would justify building.
- **Boxes other than DLAPTOP were not inspected.** Client flags are per-machine
  (`~/.ree_coordinator_client.json`, gitignored). The flags quoted here are the
  Mac's. A worker with different flags would show up in this measurement only
  through its commits -- which is how `REE Cloud Worker` was caught on
  proposals -- but a worker with an armed flag and an unreachable hub is
  indistinguishable here from a compliant one.
- **Merge commits were excluded** (`--no-merges`). Checked: all 24 merge
  commits touching `WORKSPACE_STATE.md` over 30d have a `Merge ` subject (branch
  merges and origin re-merges), none is an editorial write.
- **Cherry-picks were checked for double-counting.** Many non-hub commits carry
  `(cherry picked from ...)`; in every sampled case the source commit exists
  locally but is NOT an ancestor of `origin/master`, so each logical write is
  counted once.

## 7. Re-scope note (the chip's conditional)

The chip asked to re-scope if push had already been restricted on the remote.
Checked at measurement time:

```
gh api repos/Latent-Fields/ree-v3/branches/main/protection
-> 404 "Branch not protected"
```

**Not restricted.** DP-12's urgency premise is unchanged: any key can still push
anything to either default branch. Nothing in this session altered that, and the
DP-2/push-restriction tension remains a user decision, untouched here.

## 8. Reproducing this

The classifier is ~120 lines over `git log` and was deliberately not landed as a
tool (DP-12 asks for a measurement, not a service). To reproduce, for any routed
path:

```bash
# routed commits (CAS): committer is the Hub AND the body carries both trailers
git -C <repo> log --format='%H %cn%n%B' -- <path> | grep -B2 '^machine: '
# hub materializer (append/registry):
git -C <repo> log --oneline -- <path> | grep '^[0-9a-f]* phase2b-registry:'
# everything else is a non-hub git write; classify by whether the writing tool
# contains a coordinator_transport call site:
grep -rl coordinator_transport REE_Working/scripts/ REE_assembly/scripts/
```

---

## 9. Addendum 2026-09-18: finding (1) has been acted on -- the counts have not

Added by `chip-20260918-phase4-assembly-writer-routability`, after this report
was landed. **Everything above is left exactly as measured.** This section
records only what has CHANGED since, because one statement above is now false
and a later reader reproducing section 8 will get a different answer than the
body describes.

### 9.1 What changed

Section 5 finding (1) said: "`grep -rl coordinator_transport
REE_assembly/scripts/` returns **zero files**. The coordinator client exists
only in the umbrella repo." **That is no longer true.** As of `REE_assembly`
`2a17374bc6` that directory contains:

- `scripts/coordinator_transport.py` -- vendored BYTE-IDENTICAL from the
  canonical `REE_Working/scripts/` copy, registered in
  `scripts/audit_vendored_copies.py` `VENDOR_SETS` (set `coordinator_transport`)
  so the existing drift audit and its direction rule now guard it. A cross-repo
  `sys.path` import was rejected for the reason root CLAUDE.md step 7a gives for
  `graceful_timeout.py`: it fails silently off the Mac, and here the silent
  fallback IS the git path -- i.e. this report's own defect, except invisible,
  because the flag would still read armed. Vendoring duplicates no state: the
  config and bearer token live in `~/.ree_coordinator_client.json`, in `$HOME`,
  outside any repo, so both copies read one config and one token.
- `scripts/assembly_coordinator.py` -- the gated adapter REE_assembly writers
  are meant to call. DP-10 holds by construction: `routing_armed()` is
  `enabled() and in_scope(UMBRELLA_ROOT)`, with `UMBRELLA_ROOT` derived from
  `__file__`, so a fixture clone outside the real tree computes a root that is
  not `scope_root` and stays on the git path. Verified against this box's live
  suppression-armed config. **No widening of the canonical `in_scope()` was
  needed or made** -- widening it to accept containment under `scope_root` was
  considered and rejected as a broadening of the arming condition, which is the
  one thing DP-10 exists to prevent.

The standing check this report's section 5 asked for is now
`REE_Working/scripts/audit_routed_path_writers.py`, wired into
`hygiene_routine_tick.py` (fleet cadence, not session-start: the defect is
structural and changes only when a writer or a flag changes).

### 9.2 What did NOT change -- do not read 9.1 as a compliance improvement

**No writer was converted.** Re-running section 8's structural test today shows
`generate_inter_governance_workset.py` and `igw_assignments_lib.py` still have
no call site. Every per-file count in section 2 stands as measured, and every
section-4 verdict stands. What changed is that the fix is now *possible* in this
repo; none of it is *applied*.

### 9.3 Correction carried forward from DP-12

DP-12 named remote-side push restriction as "the only uniform lever". This
report's own section 5 refutes that and the refutation should travel with it:
all three non-compliant populations are STRUCTURAL, so branch protection would
fix none of them. Section 7 confirms push is still unrestricted; that remains a
user decision and is untouched.

### 9.4 A blind spot in the new check, found while wiring it

`audit_routed_path_writers.py` is **FILE-granular**, and section 3.4's finding
is FUNCTION-granular. `chip_ledger.py` carries 20 `coordinator_transport`
references elsewhere in the file, so the whole file scores as routing-capable
and `cmd_archive`'s zero references are masked: the new check reports
`TASK_CHIPS.json` as clean. **The daily git-side strip is still unrouted** --
section 3.4 remains the live account of it, and the check will not re-raise it.
Chipped separately as `chip-20260918-phase4-chip-archive-verb`; the rotation
gap in section 3.3 is `chip-20260918-phase4-ws-rotation-verb`. The check states
its other two blind spots (session-level `ree_commit.py` commits, and paths where
no writer matched at all) in its own output.

### 9.5 `/intent/replace` health, for whoever picks up section 10 step 4

Probed 2026-09-18 with a deliberately invalid repo (no write performed): it
returned a structured `400 not_routed`, not the 500 seen for five days during
the DP-11 deploy gap. The endpoint and the `submit_intent_replace` transport
wrapper are both live. `ree_commit.py` still has zero references to the intake,
so section 10 step 4 remains UNBUILT.
