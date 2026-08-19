**Status: AWAITING USER REVIEW. Nothing in this file has been written to
`scripts/ree_commit.py`, `scripts/safe_adopt_ref.py`, or any registry.**

# MM-skew repair: a per-record content probe for append-only JSONL registries

Investigation for `chip-20260819-mm-skew-repair-content-check`, run
2026-08-19T03:17Z-03:25Z on `ree-cloud-5` (worktree
`metaworker-chip-20260819-mm-skew-repair-content-check`). **No code was
changed.** `scripts/ree_commit.py` is currently claim-owned by a concurrent
session (`metaworker-chip-20260818-wire-taskclaim-chipledger-remotetip`,
unrelated task) as of this writing, so a live edit there was not attempted
even setting aside the evidentiary question below. This document is the
handoff.

## 1. The gap, restated precisely

`check_head_worktree_skew()` in `scripts/ree_commit.py` treats an `MM` path
(staged revert of adopted content, *and* an unstaged difference between
worktree and index) as unprovable and leaves it strictly alone --
`_verify_stale_adoption()` returns `None` the moment `git diff --name-only
-- path` is non-empty, before it even looks at content. This is documented,
deliberate, and correct as a **default**: CLAUDE.md's "Deletions are not the
only skew" section states the reasoning -- an `MM` worktree copy might be a
live session's genuine uncommitted work, and `git checkout HEAD -- <path>`
would destroy it.

The gap: **"differs from HEAD" is satisfied by two different situations,
and the current test cannot tell them apart:**

- (a) genuinely-ahead work -- the worktree copy is a superset of HEAD's
  content (every HEAD record present, plus new ones). Protecting it is
  exactly right.
- (b) a worktree copy that is itself a **stale prefix** of an older commit,
  with real new work appended on top of that stale base. It "differs from
  HEAD" just as (a) does, but silently drops however much history moved
  between the stale base and current HEAD if the file is just left alone.

For an **append-only, immutable-record** registry -- write once, never
rewritten, never pruned -- (b) is detectable cheaply: parse HEAD's blob and
the on-disk copy as one-JSON-object-per-line, and check whether every
HEAD record is present verbatim in the worktree copy. Missing HEAD records
is the (b) signature; their absence is impossible under (a).

## 2. The pattern is confirmed, not hypothetical -- two on-path incidents

Both on `scripts/steward/state/steward_ledger.jsonl`, both resolved by hand
with the identical technique (full-record diff against origin, union,
append origin's missing records after the local tail):

1. **`ba35aa53d8`, Mac, 2026-08-18T08:05:22+01:00.** Worktree copy held 29
   lines against HEAD's 65 (37 records missing), attributed to a
   stash/pull/rebase--skip sequence. This was caught **before commit** --
   `ree_commit.py`'s private-index build was about to stage the 37-line
   deletion as a side effect of an unrelated governance-flag commit, and a
   human/session noticed the diff. It did **not** go through
   `check_head_worktree_skew()` at all (that function only runs post-commit
   after a ref move); it is evidence of the same underlying gap one layer
   up -- `ree_commit.py`'s ordinary per-item delta reporter (CLAUDE.md
   "Detection is now mostly automatic") does not cover JSONL, only single
   JSON documents, so nothing but luck caught this one.

2. **`ree-cloud-5`, 2026-08-18T10:47Z, inside `check_head_worktree_skew()`
   itself**, during the `REE_assembly` ref-wedge repair documented in
   `cloud5_refwedge_ree_assembly_audit_20260818.md`. `steward_ledger.jsonl`
   was found `MM`, correctly judged "differs from pre-move HEAD" per the
   documented asymmetry, and left untouched -- the staged revert cleared,
   the worktree copy never inspected further. `WORKSPACE_STATE.md`
   2026-08-18T10:47Z: *"1 `MM` (`steward_ledger.jsonl`) found to DIFFER --
   a live session's uncommitted work -- so **not** restored, only its
   staged revert cleared index-only."* That verdict text reads as
   confident and closed. It was wrong about *why* it differed: the file
   was re-discovered still truncated at 2026-08-18T18:45Z (68 HEAD records
   vs. 4 local), and finally repaired at `c0b8669e26`
   (2026-08-19T00:40:46Z, cherry-picked from `f99b643139`) using the same
   full-record-diff-and-union technique as incident 1. Between 10:47Z and
   00:40Z the file sat silently wrong for roughly 14 hours with no signal
   anywhere that a repair had been declined-as-unprovable rather than
   confirmed-safe.

Both incidents are the *identical* mechanism CLAUDE.md's "The mechanism
also runs in the REGRESSION direction" paragraph already documents for
`TASK_CHIPS.json` (a ref-repair leaving a stale, pre-resolution snapshot on
disk that a later mutation then faithfully commits) -- this is that same
shape, on a file where nothing currently detects it.

## 3. A negative control that confirms the scope boundary

`ree-cloud-5`, `REE_Working` umbrella, 2026-08-18T18:08Z (chip
`chip-20260816-registry-residual-dirt-cloud5`):
`docs/worktree_session_registry.md` + `worktree_session_registry.json` were
found `MM` with HEAD, index, and worktree **each holding a different
copy**. The session resolved it by hand -- comparing `generated_at`
timestamps and path-flavour (`Users-dgolden` vs `/home/ree`) -- and
**deliberately overrode** the generic MM rule, restoring from HEAD, because
the unstaged layer was proven to be derived, machine-local, uncommitted-
anywhere regen output from a script now gated off on that box.

This is **not** a case the proposed check should fire on, and it wouldn't:
`worktree_session_registry.json` is a **wholesale-regenerated current-state
snapshot** (every run overwrites the whole file with a fresh fleet map), not
an append-only immutable log. A full-record-membership test is meaningless
for it -- "records" don't persist across regenerations at all, so "missing
records" would be the normal case on every diff, not a defect signature.
This is exactly why the recommendation below is an **explicit allowlist of
confirmed append-only files**, not a heuristic that sniffs file shape
(JSONL-parseable, list-of-objects, etc.) and fires generically. The same
principle already governs `ref_convergence.py`'s `REGISTRY_SPECS` (route C,
see section 4) -- allowlist, not heuristic.

## 4. Relevant existing infrastructure -- reuse, don't duplicate

`scripts/ref_convergence.py` already solves an adjacent (not identical)
problem: **route C** proves whether a *local-only ahead commit* is safe to
discard by comparing parsed, keyed items of an allowlisted whole-file JSON
registry against origin. It was extended to a JSONL `kind` on 2026-08-18
(`REE_Working` `4af03b71`, chip `chip-20260818-routec-jsonl-recommendation-
log`) specifically to cover `RECOMMENDATION_LOG.jsonl` -- and that chip's
own resolution note is instructive: it investigated `RECOMMENDATION_LOG.jsonl`
for a declared unique key, found `(session_id, timestamp_utc)` collides 9/129
times on live data, and **deliberately left it undeclared** rather than force
a key that doesn't hold. `REGISTRY_SPECS` and `_parse_jsonl_registry` now
exist as reusable, tested (115 tests) infrastructure, but route C's model is
built for **mutable** registries -- items that get legitimately rewritten in
place (a claim's `completion_note`, a chip's `status`) -- which is why it
needs a declared identity *key* distinct from full-record content.

`steward_ledger.jsonl` does **not** have that problem and should **not** be
forced into route C's keyed model. Checked directly against the live file
(75 records, 2026-08-19): `(finding_id, ts)` is unique across the 51 rows
that carry a `finding_id` (`refine`/`suppress`/`autofix`), but the `run`
(24 rows) and `ratchet` (2 rows) actions carry **no `finding_id` at all** --
so no single field-pair spans every row shape. The file does not need one:
it is documented (steward README, `governance.sh` Step 3m commit) as a pure
**append-only, write-once, never-rewritten** audit trail, so the correct
identity for a record is simply **its own canonical content** --
`json.dumps(obj, sort_keys=True)` (or a hash of it) -- with no key field
required. This is a strictly simpler, different primitive from route C's,
better suited to this file's actual invariant, and it is exactly what both
manual repairs (`ba35aa53d8`, `c0b8669e26`) already did by hand: diff full
records, not fields.

**Conclusion: reuse route C's JSONL *line-splitting* convention (skip blank
lines, refuse on unparseable/non-dict lines) for consistency, but do NOT
route this through `REGISTRY_SPECS`/route C's keyed-item model.** This is a
separate, smaller primitive, living in (or alongside) the MM-repair code,
not the ref-convergence discard-proof code -- the two answer different
questions (`ref_convergence`: "is this *local commit* safe to discard
because origin already has it", this: "is this *worktree file*, already
decided to stay untouched, missing history HEAD holds").

## 5. Recommended design (not implemented)

Advisory-only. **Never changes which paths get auto-restored or left
alone** -- it only adds detail to the message already printed for
`mod_unverified` paths in `check_head_worktree_skew()`.

```python
# New, small, explicit allowlist -- confirmed append-only/immutable JSONL
# registries only. Do NOT auto-discover by file shape (see section 3 --
# the worktree_session_registry.json negative control is exactly the file
# a shape-based sniff would wrongly match).
APPEND_ONLY_JSONL_PATHS = {
    "scripts/steward/state/steward_ledger.jsonl",   # REE_assembly
    # candidates NOT yet added -- append-mode confirmed by their writers
    # (record_decision.py, promote_status_history.py) but NOT yet backed by
    # a real incident; add only once one recurs, per GOV-HELDOUT-1 below:
    #   evidence/decisions/decision_log.v1.jsonl
    #   evidence/planning/status_history/status_snapshot.v1.jsonl
    #   evidence/planning/hypothesis_space_timeseries.v1.jsonl
}

def _append_only_missing_records(repo, path, base_sha):
    """For an allowlisted append-only JSONL path, return the list of HEAD
    records (raw text, canonicalised) that are ABSENT from the on-disk
    worktree copy -- i.e. records a stale-prefix worktree copy is missing.
    Empty list means the worktree copy is a superset of HEAD (pure-ahead,
    or unchanged). Returns None if the path isn't allowlisted, either side
    fails to parse as JSONL-of-objects, or git can't read the blob -- i.e.
    "cannot prove", not "nothing missing". Callers must not treat None as
    "no gap found".
    """
    if path not in APPEND_ONLY_JSONL_PATHS:
        return None
    head_raw, rc, _ = git(repo, "show", "%s:%s" % (base_sha, path), check=False)
    if rc != 0:
        return None
    try:
        local_raw = open(os.path.join(repo, path), encoding="utf-8").read()
    except OSError:
        return None
    head_lines = _canonical_jsonl_lines(head_raw)   # None on any parse failure
    local_lines = _canonical_jsonl_lines(local_raw)
    if head_lines is None or local_lines is None:
        return None
    local_set = set(local_lines)
    return [l for l in head_lines if l not in local_set]
```

Wired into `check_head_worktree_skew()`'s existing `mod_unverified` branch
(the loop already prints "staged modification(s) left UNTOUCHED"): for each
`p in mod_unverified`, additionally call
`_append_only_missing_records(repo, p, "HEAD")` (or the appropriate
pre-move base when one is available) and, when it returns a non-empty list,
print a **second, distinctly-worded, louder** message instead of / in
addition to the existing generic one -- something like:

```
ree_commit: APPEND-ONLY REGISTRY GAP -- <path> is missing N of M records
present in HEAD. This is NOT plain 'ahead' skew: the worktree copy is a
stale prefix with local work appended on top. Left UNTOUCHED (per the MM
asymmetry) but a union repair is needed, not a plain restore:
    git -C <repo> show "HEAD:<path>" > /tmp/head_copy.jsonl
    # diff each local record's full JSON against /tmp/head_copy.jsonl,
    # keep every local-only record, append after HEAD's tail (matches
    # REE_assembly ba35aa53d8 / c0b8669e26)
```

When the list is empty, the existing generic message is left as-is (still
correctly ambiguous -- an empty gap doesn't distinguish "genuinely ahead"
from "byte-identical", both of which are fine to leave alone).

**Explicitly out of scope for this recommendation:**
- No auto-repair / auto-union. The union step stays a human/session
  action, same as today -- only the diagnosis is upgraded from silent to
  loud.
- No change to `D `/` D`/plain `M ` repair paths.
- No change to `REGISTRY_SPECS`/route C.
- No blanket "any JSONL file" heuristic -- allowlist only, and the
  allowlist starts at exactly one entry with a confirmed incident.

## 6. Held-out check (GOV-HELDOUT-1) -- reported honestly, falls short of 3

CLAUDE.md requires >=3 historical cases, non-degenerate (old and new logic
actually differ), before landing a change to standing-rule-adjacent
tooling like this. What this investigation found:

- **2 clean, non-degenerate, on-path cases** where the *exact* proposed
  check (evaluated against `check_head_worktree_skew`'s live decision)
  would have differed from current behaviour: the 2026-08-18T10:47Z
  `ree-cloud-5` MM-protect (old: silent, generic "left untouched"; new:
  loud "44 of 68 records missing, union needed" -- would have prompted
  same-cycle repair instead of a 14-hour-later rediscovery), and, at one
  remove, `ba35aa53d8` (old: nothing detects it until incidental
  pre-commit diff review; new: the same probe, if it also ran on ordinary
  commits rather than only post-move MM paths, would have caught it
  directly -- noted honestly as *not* the same code path, see section 2
  item 1).
- **1 valid negative control** (section 3) confirming the allowlist-only
  scope is the right one and a shape-based heuristic would have misfired.
- **No third genuinely independent incident.** Both positive cases are the
  *same file*, within a 17-hour window, plausibly the same underlying root
  cause (repeated `ree-cloud-5` ref-wedge repairs clobbering the tree
  under one tracked append-only path, per the open, unresolved chip
  `chip-20260818-steward-ledger-truncated-cloud5`'s own hypothesis).

Per CLAUDE.md's own escape hatch ("If you cannot find 3 such cases, that is
itself the finding -- the rule is probably scoped to its motivating
incident"): **this is scoped to its motivating incident.** That is not a
reason to discard the design -- it argues for exactly the narrow shape
recommended in section 5 (one-entry allowlist, advisory-only, zero change
to any auto-repair decision), not for a general "any append-only registry"
rule. Recommend landing scoped to `steward_ledger.jsonl` alone if/when
implemented, and only widening the allowlist (decision_log.v1.jsonl etc.)
after a real incident on one of them, per the same discipline -- not
speculatively from this write-up.

## 7. Why this wasn't implemented in this session

`scripts/ree_commit.py` carries an active `TASK_CLAIMS.json` claim from
`metaworker-chip-20260818-wire-taskclaim-chipledger-remotetip` (unrelated
task: "wire remote-tip into task_claim/chip_ledger"), opened
2026-08-19T01:38:54Z, still active when this session's `task_claim.py open`
was arbitrated at 2026-08-19T03:17:54Z. Per CLAUDE.md's arbitration rule,
losing sessions must not implement and must hand over findings via
`completion_note` -- this document is that handover, expanded to design
depth since the finding is code-shaped rather than a one-line fact.

## 8. Recommendation

1. A human (or a future session, once `scripts/ree_commit.py` is free)
   reviews sections 4-6 and decides whether the advisory-only, one-entry-
   allowlist version in section 5 is worth landing given the held-out
   shortfall in section 6.
2. If yes: implement `_append_only_missing_records()` and its call site in
   `check_head_worktree_skew()`'s `mod_unverified` branch, add tests
   (real git repos in a tempdir, mirroring the existing
   `_verify_stale_adoption`/`_verify_deletion_skew` test style), and land
   through the normal claim -> `ree_commit.py` flow.
3. If no (held-out shortfall judged disqualifying): this document stands
   as the record of the investigation, and the next `steward_ledger.jsonl`
   truncation (if the root-cause chip `chip-20260818-steward-ledger-
   truncated-cloud5` isn't independently closed first) becomes the third
   case.
