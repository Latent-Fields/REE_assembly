# ree-cloud-5 `REE_Working` `master` ref-convergence wedge -- audit and clearance, 2026-08-18

**Outcome: CLEARED.** `ref_convergence.py --check` on `/home/ree/REE_Working` exits 0;
the branch is `[behind 0, ahead 0]` against `origin/master`.

Session `metaworker-chip-refwedge-ree-cloud-5-ree-working-master-since-2026-08-18t08-24-35z`
(headless, ree-cloud-5), chip `chip-refwedge-ree-cloud-5-ree-working-master-since-2026-08-18t08-24-35z`.
Sibling write-up for the same box's `REE_assembly` wedge, cleared ~1h earlier:
`cloud5_refwedge_ree_assembly_audit_20260818.md`.

**The refusal was correct and was NOT relaxed.** No heuristic third proof route was added;
`ref_convergence.py` and `safe_adopt_ref.py` are unmodified. It was cleared by doing the
operator work the refusal exists to demand.

---

## 1. The numbers were stale on arrival, by an order of magnitude

| | ahead | unproven | age | refusals |
|---|---|---|---|---|
| chip text (08:24:35Z wedge start, written 08:35Z) | 14 | 3 | 0.2h | 9 |
| session start (10:58Z) | 82 | 37 | 2.6h | 35 |
| at the ref move (11:05Z) | 87 | 39 | -- | -- |

The chip's own warning to re-measure is load-bearing: acting on its three named shas
(`2aa898ea54`, `af5018acdf`, `c585258820`) would have addressed under 8% of the range.
The growth is the self-sustaining residual CLAUDE.md documents -- once ahead by one, every
later push is non-fast-forward and re-enters the push-retry path, adding another orphan.
Measured here at roughly **+25 ahead commits/hour**.

## 2. The audit -- content, never shape

Two independent facts made this tractable, and both were *measured*, not assumed:

1. **All 37 unproven commits (later 38 of 39) touch only `TASK_CHIPS.json` and
   `TASK_CLAIMS.json`.** Established by enumerating `git show --name-only` over the
   unproven set -- not by reading commit subjects.
2. Both are allowlisted registries, so `ref_convergence.py --audit` (route C) applies
   and its per-item content comparison is **complete coverage** of that range, not a sample.

Route C's verdict: of ~944 registry items across 37 commits, exactly **4** were absent
from `origin/master`. Each was then compared by hand, local tip vs `origin/master`:

| registry | key | local status | upstream |
|---|---|---|---|
| `TASK_CHIPS.json` | `chip-refwedge-ree-cloud-5-ree-working-master-since-2026-08-18t08-24-35z` | `open`, claimed | **absent** |
| `TASK_CHIPS.json` | `chip-metaworkergc-chip-20260818-cooldown-s-42392e416ccd` | `open` | **absent** |
| `TASK_CLAIMS.json` | `metaworker-chip-20260818-safeadopt-allowdiscard-argv-silent-noop` @`10:00:20Z` | `done`, full completion note | **absent** |
| `TASK_CLAIMS.json` | `metaworker-chip-refwedge-ree-cloud-5-ree-assembly-master-since-2026-08-18t05-20-27z` @`10:19:46Z` | **`active`** | **absent** |

**This is the CLAUDE.md rule paying for itself again.** A shape argument -- "39 commits of
`chip_ledger`/`task_claim` bookkeeping on whole-file JSON, i.e. the known false-negative
shape, therefore safe to discard" -- would have been right about 35 of 39 and wrong about
four, and the four include a **live sibling session's ACTIVE claim** (dropping it breaks
arbitration for a session still running) and this chip's own ledger entry (whose entire
purpose is to survive its session). Same direction as the sibling `REE_assembly` audit,
where 212 of 213 were content-safe and the 213th was real.

## 3. Landing -- structural append, because cherry-pick is what stranded them

`git cherry-pick -x` is the documented route and is **not usable here**: these are
whole-file rewrites of a 5.5 MB, 944-item registry against a diverged origin, which is
precisely the conflict that stranded them in the first place. A conflicting cherry-pick
leaves no upstream patch-id and no `-x` backref, so nothing can ever prove it -- the
permanent-refusal mechanism.

Landed instead as a **narrow structural append** from a throwaway worktree at
`origin/master`: parse each registry, append the missing item if and only if its key is
still absent, re-serialise with the writers' own `json.dumps(data, indent=2) + "\n"`,
push. Retry loop re-derives from a fresh `origin/master` on rejection, so a concurrent
push cannot be clobbered.

`REE_Working` **`4768a2faec`** on `origin/master`. Diff is **50 insertions / 0 deletions**
in `TASK_CHIPS.json` and **24 / 0** in `TASK_CLAIMS.json` -- append-only by construction;
no existing item modified or removed. Verified afterwards that all four keys are present
on `origin/master`, alongside this session's own claim.

Re-audit then reported: **"Registry net effect of the ahead range IS fully present upstream."**

## 4. The one non-registry commit

`cd9ce645dd` -- a merge of the sibling's `claude/metaworker-chip-refwedge-ree-cloud-5-ree-assembly-master-...`
branch, landing exactly **one** `WORKSPACE_STATE.md` Recent Work line. Route C does not
apply. Hand-audited: `git diff cd9ce645dd^1 cd9ce645dd` is that single line, and the line
is present verbatim in `origin/master:WORKSPACE_STATE.md` (exact-line `grep -Fqx`).
Content-safe to discard.

With that, every commit the move would discard had its content proven upstream.

## 5. The ref move, and a skew repair that needed the documented asymmetry

`safe_adopt_ref.py --repo /home/ree/REE_Working --branch master --allow-discard <87 shas>`,
one sha per argv element (this checkout's frozen copy predates the whitespace-split fix of
`chip-20260818-safeadopt-allowdiscard-argv-silent-noop`, where a joined argument
acknowledges nothing). Pre-move `f3d8d800d0` -> `origin/master` `2678741f90`. Exit 0.
Backup branch `backup/refwedge-working-20260818T1100Z` taken first (local-only).

Given `chip-20260818-safeadopt-skew-repair-not-restartable` -- where a 2-minute caller
timeout killed the repair mid-flight and left 32 staged reverts armed while `ahead/behind`
read 0/0 -- the call was run in the foreground under a 900s shell-level timeout and the
skew was re-verified by hand afterwards. It completed:

- **2 `D ` materialised**: `scripts/reconcile_wedge_content.py`, `scripts/test_reconcile_wedge_content.py`
- **15 `M ` staged reverts discarded**, including `scripts/safe_adopt_ref.py`,
  `scripts/igw_routine_tick.py`, `scripts/hygiene_routine_tick.py`,
  `scripts/dispatch_usage_cooldown.py`, `scripts/remote_pytest.sh`, both copies of
  `metaworker-dispatch/SKILL.md`
- **2 left UNTOUCHED** (`TASK_CLAIMS.json`, `WORKSPACE_STATE.md`) -- the tool correctly
  refused to guess. Resolved under the documented asymmetry: `git show <pre-move-sha>:<path>
  | diff -q -` matched **byte-identically** for both, i.e. stale adoption lag with nothing
  local to lose, so `git checkout HEAD -- <paths>` was the correct repair. Had either
  differed it would have been a live session's work and only the staged revert cleared.

Final state: `git status --porcelain | grep -vE "^ M"` empty; the only residue is the two
` M` paths `worktree_session_registry.json` / `docs/worktree_session_registry.md`, which
are the known machine-scoped-registry standing dirt on non-owner boxes (CLAUDE.md,
Session Land housekeeping step 5) and were correctly left alone.

## 6. Finding: the repair tool cannot reach a wedged box -- a bootstrap gap

`scripts/reconcile_wedge_content.py` is purpose-built for exactly this repair
(`chip-20260818-wedge-content-reconciler-tool`). It was **not usable here**, and not
because it refused:

| event | time |
|---|---|
| this wedge began | 2026-08-18T**08:24:35**Z |
| `reconcile_wedge_content.py` landed on origin (`187a3823`) | 2026-08-18T**10:19:49**Z |

It landed **1h55m after the tree froze**, so it was absent from the local branch
(`git cat-file -e` fails on both the pre-move sha and the backup branch) -- the box could
not run the tool built to unwedge it. It appeared on disk only as an artifact of the very
ref move it was supposed to perform: it is one of the two `D ` paths the skew repair
materialised in section 5.

**This is a structural constraint on the open decision chip
`chip-20260818-reconciler-autorepair-wiring-decision`, and that chip does not state it.**
Its options (b) "wire in `--check` only" and (c) "wire in `--adopt`, gated" both assume
`hygiene_routine_tick.py` on the wedged box can invoke the tool. But the wedge freezes
`scripts/`, so any box that wedges before a given version of the tool lands can never run
that version -- the repair capability arrives exactly where it cannot be used. It is the
same class as the already-recorded observation in `chip-20260818-cloud5-reeworking-master-wedge-frozen`
("frozen at a pre-fix `hygiene_routine_tick.py`, and that version can never re-chip"),
generalised from the *detector* to the *repair*.

The gap is not fatal to (b)/(c) -- it bounds them. A wired tool still helps every box that
wedges *after* it is deployed, which over time is most of them; what it cannot do is
self-heal the population already frozen. Whatever option is taken should say so, and the
residual manual path (this document) should stay documented rather than be treated as
superseded. Chipped as `chip-20260818-reconciler-unreachable-on-wedged-box`.

## 7. What was NOT done

- No change to `ref_convergence.py`, `safe_adopt_ref.py`, `ree_commit.py` or any guard.
- No `claims.yaml` edit, no queue edit, no experiment queued.
- `ree-v3` and `REE_assembly` on this box were checked and are clean (`--check` exit 0,
  `REE_assembly` 0/0); no action taken on them.
- The backup branch `backup/refwedge-working-20260818T1100Z` is local-only and can be
  deleted once this is read; it points at the pre-move tip `cd9ce645dd`.
