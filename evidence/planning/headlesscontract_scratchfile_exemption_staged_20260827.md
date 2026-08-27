**Status: AWAITING USER REVIEW**

# `.headless_contract.md` / `HEADLESS_CONTRACT.md` missing from `METAWORKER_SCRATCH_FILES`

Session: `cool-sutherland-9d984d` (DLAPTOP), `/metaworker-learning`, 2026-08-27T06:56Z.
Source chip: `chip-20260827-strandedwt-headlesscontract-missing-from-scratch-exemption`
(raised by Healer cycle `healer-cloud5-20260827-0420` on ree-cloud-5, 2026-08-27T04:25Z).

## 1. Confirmed recurrence (Step 1 of `/metaworker-learning`)

Same root cause, not just same symptom: `scripts/hygiene_routine_tick.py`'s
`_worktree_uncommitted_entries()` (line 3658) excludes a fixed allowlist,
`METAWORKER_SCRATCH_FILES` (line 1717, currently
`{".dispatch_pid", "DISPATCH_BRIEF.md", "claude.log", ".session_uuid"}`), from
what counts as "uncommitted work" in a metaworker-dispatch worktree. Any
dispatcher-written scratch file NOT on that list is treated as possibly-real
stranded work and raises a `chip-strandedwt-*` finding once its worktree goes
idle past `STRANDED_MIN_IDLE_HOURS`.

`.session_uuid` was added to the set on 2026-08-18
(`chip-20260818-hygienetick-sessionuuid-scratchfile`, `kind: work`, a direct
`/metaworker-repair` patch) after it caused two false-positive stranded-work
chips. `.headless_contract.md` (and the earlier-dispatcher spelling
`HEADLESS_CONTRACT.md`) is the same defect shape -- a dispatcher-injected
file, gitignored by the `.claude/worktrees/` blanket ignore, that can never
have a git object -- recurring under a different filename the 2026-08-18 fix
did not happen to cover.

**Independently re-verified, not just taken from the chip's own tldr:**

- Live-queried `TASK_CHIPS.json` directly (not the chip's cached count): of
  90 resolved `chip-strandedwt-*` chips, **39** (43%) have a resolution note
  citing `.headless_contract.md` or `HEADLESS_CONTRACT.md` as the sole or
  primary stranded content, dated 2026-08-18 through **2026-08-27 (today)**,
  on both `ree-cloud-5` and `ree-cloud-4`. This is ongoing, not a closed
  historical cluster.
- Confirmed in code: `_worktree_uncommitted_entries()` (line 3693) filters
  by exact `rel in METAWORKER_SCRATCH_FILES` membership, and neither
  spelling of the contract filename is a member. Confirmed the file is
  written by the current dispatcher's `HEADLESS WORKER CONTRACT` block
  (`.claude/skills/metaworker-dispatch/SKILL.md` "HEADLESS WORKER CONTRACT")
  and is gitignored via the `.claude/worktrees/` pattern in `.gitignore` --
  so `[no git object]` is by design, not a symptom of anything wrong.
- This exceeds the skill's default recurrence threshold (2) by a wide
  margin, and the module's own stated bar for adding a name --
  "ADD A NAME ONLY ON MEASUREMENT, never on resemblance" -- is squarely met.

## 2. Held-out check (GOV-HELDOUT-1)

**Old wording:** `METAWORKER_SCRATCH_FILES` has 4 members, neither contract
spelling included -> every dispatched worktree whose only remaining content
is the contract file (after its real work landed, or if it never wrote any)
raises a `chip-strandedwt-*` finding.
**New wording:** add `.headless_contract.md` and `HEADLESS_CONTRACT.md` ->
those worktrees raise nothing.

These give different answers, so the check is non-degenerate. Sampled all
39 confirmed historical resolution notes (not a subset) for any case where
the file's content was found to differ from the canonical boilerplate, or
where real work was bundled alongside it and might be masked by a coarser
fix:

- **0 of 39** describe content differing from the dispatcher's canonical
  `HEADLESS WORKER CONTRACT` block. Every note that inspected the file
  byte-compared it against the live copy in
  `.claude/skills/metaworker-dispatch/SKILL.md` (or a sibling worktree's
  copy) and found it identical or a stale-but-verbatim prior revision.
  Representative language across independent sessions/hosts/dates:
  "byte-identical", "diffed line-by-line ... verbatim", "byte-for-byte
  dispatch-harness copy", "genuinely worthless: no recovery needed".
- **Masking risk is structurally absent, not just empirically absent**: the
  exemption is applied per-entry (`if rel in METAWORKER_SCRATCH_FILES:
  continue` inside a per-path loop), not per-worktree. A worktree carrying
  both the contract file AND a genuine uncommitted deliverable still raises
  a chip for the deliverable -- only the exact-named scratch path is
  dropped. Confirmed against the code path directly (section 1 above), not
  inferred from the notes.
- **Negative control (the module's own, still valid):** the parallel case
  this same file documents for `.session_uuid` -- adding a name that turns
  out to be wrong would show up as `test_that_control_is_not_vacuous_one_
  real_file_still_strands` (in `scripts/test_hygiene_routine_tick.py`)
  going green when it should be red. That test is not touched by this
  change and continues to assert a lone genuine file still strands.
- I could not find any of the 39 cases where the OLD rule was actually
  correct (i.e. where the contract file was the right thing to flag). All
  39 are cases where new gives the right call and old did not. Per the
  skill's own instruction, that absence is itself worth stating rather than
  manufacturing a counterexample that doesn't exist.

**Honest counterweight:** this held-out check reads 39 resolution notes
written by many independent sessions rather than re-deriving byte-identity
myself from scratch. That is a real limitation -- it trusts those sessions'
own diffs rather than an independent re-diff against the SKILL.md history at
each point in time. I judge this acceptable here because (a) the sessions
used the same verification method (diff against the canonical SKILL.md
block or a sibling worktree) independently, across different hosts and
dates, without coordinating, and (b) the structural per-entry-exemption
argument above does not depend on the notes being right at all. It would not
be acceptable for a fix with a narrower evidence base or a riskier failure
mode (see MOVE-3 discipline: verify, don't just cite prior verification).

## 3. Recommended fix

In `scripts/hygiene_routine_tick.py`:
```python
METAWORKER_SCRATCH_FILES = frozenset({".dispatch_pid", "DISPATCH_BRIEF.md",
                                      "claude.log", ".session_uuid",
                                      ".headless_contract.md",
                                      "HEADLESS_CONTRACT.md"})
```
Plus the doc-comment update immediately above it (same paragraph style as
the existing `.session_uuid` note, naming this fix's measurement).

In `scripts/test_hygiene_routine_tick.py`, mirroring the existing
`.session_uuid` pattern exactly (module docstring there explains why the
literal-list form is required, not a set-derived one):
- Add both names to the literal `SCRATCH_NAMES` tuple (line 4515) --
  `test_the_scratch_set_still_holds_exactly_the_pinned_names` fails until
  this is done, which is the intended reminder.
- `test_a_worktree_holding_only_dispatcher_scratch_is_NOT_stranded` already
  iterates `self.SCRATCH_NAMES`, so both new names are covered automatically
  once added to the tuple -- no new test body needed there.

No change needed to the module docstring at lines 151/160 (it references
the constant by name rather than restating its members, confirmed by
reading both lines).

**Explicitly out of scope:** `.chip_prompt.txt` appears in 2 of the 90
resolved notes (always alongside `.headless_contract.md`, never alone).
2 occurrences is below this module's own measurement bar and below this
skill's own recurrence threshold applied independently to that filename --
noting it here rather than folding it in un-measured. If it recurs again,
it is a fresh `/metaworker-repair` candidate (or a second `/metaworker-
learning` pass if it also reaches genuine recurrence).

## 4. Blast radius

`METAWORKER_SCRATCH_FILES` is read by three call sites, all covered by the
change: `_git_worktree_is_dirty` (worktree-GC dirtiness gate),
`_worktree_uncommitted_entries` (the stranded-work detector this chip is
about), and `_gc_removal_commands` (the GC cleanup command list, which
already derives from the constant rather than restating it, so the new
names are picked up in `rm -f` automatically). This is `scripts/`, shared
fleet-wide machinery per CLAUDE.md's Step 4 gate -- hence the decision chip,
not a self-approved land.
