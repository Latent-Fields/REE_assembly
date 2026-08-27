**Status: DECIDED AND LANDED.** Option 1 (structural fix, Section 4) chosen via
decision chip `chip-20260825-hygiene-declaration-structural-fix-decision`
(resolved done 2026-08-26T04:43:35Z). Built and landed `REE_Working`
origin/master `6866cd6d` (`_ensure_host_declared` + 9 tests). This doc is kept
as the design record and held-out check, not an open proposal.

# Structural fix for machine-local hygiene prompts missing a host declaration

`/metaworker-learning` design doc for `chip-20260822-hygiene-machinelocal-prompts-declare-no-host`
(Occurrence 2 of a class already patched once). Session:
`chip-20260825-metaworkerlearning-hygiene-host-declaration`.

## 1. The class, restated precisely

`scripts/hygiene_routine_tick.py` classifies certain hygiene findings as
**machine-local** (subject exists on exactly one box) via
`_MACHINE_LOCAL_RESOLVE_PREFIXES` -- this classification already gates
*resolution* (`_chip_is_this_box`, so only the minting box may resolve such a
chip). But a machine-local chip's **prompt** is a separate piece of text,
built at a different call site inside the same source function, and nothing
ties the two together. When a mint site forgets to call the reusable
`_host_declaration(host, subject)` helper, the resulting chip is correctly
*gated for resolution* but is dispatched to any box with no warning that it
is on the wrong one -- and on a cloud worker the `/Users/dgolden -> /home/ree`
root symlink means a Mac-shaped absolute path resolves silently to that box's
own checkout rather than erroring. A session that "confirms" the finding
cleared on the wrong box produces a false "done" that `cmd_record`'s
unconditional chip_ref dedup then makes **permanent** -- the tick can never
re-raise the same chip_ref.

## 2. Confirmed occurrences (recurrence, not a first-time bug)

1. **2026-08-18, `chip-20260818-strandedwt-prompt-declares-no-host`.**
   `chip-strandedwt-*` (source 12, stranded worktree work) was host-qualified
   in its *ref* but not its *prompt*. Fixed in `REE_Working` `271e9d9f`, which
   created `_host_declaration(host, subject)` and wired it into
   `_stranded_prompt` -- ONE call site.
2. **2026-08-22, `chip-20260822-hygiene-machinelocal-prompts-declare-no-host`
   (this task's origin).** `chip-refwedge-*` (source 13, ref-convergence
   wedge) recurred with the identical defect: host-qualified ref, undeclared
   prompt. Live near-miss: `chip-refwedge-ree-cloud-5-ree-working-master-
   since-2026-08-21t23-41-57z` was worked from DLAPTOP; the session avoided a
   false clear only because the two shas its prompt named did not resolve in
   the Mac umbrella at all, prompting an incidental ssh to the real box.
   Nothing in the chip's own text would have caught a session that skipped
   that step.

Two confirmed occurrences of the identical root cause (forgot to call
`_host_declaration` at a machine-local mint site) clears the default
recurrence threshold (2) from `/metaworker-learning` Step 1.

## 3. A per-callsite audit already missed a THIRD gap -- found during this session

The 2026-08-22 chip's own survey mapped every `_host_declaration(` call site
to its enclosing function and reported "4 of 9 machine-local hygiene source
families lack the declaration": `_ref_convergence_wedge_findings`,
`_worktree_skills_findings`, `_clinical_guard_findings`,
`_removed_worktree_live_worker_findings`.

Re-deriving that map from scratch this session (grep for every
`_host_declaration(` call site, then checked every member of
`_MACHINE_LOCAL_RESOLVE_PREFIXES` against it) found a **5th** gap the prior
survey's own dedicated search missed: **`_coordinator_backup_findings`**
(source 20, `_HYGIENE_COORDBACKUP_PREFIX`, ~line 6460) has no
`_host_declaration` call anywhere in its body. Its chip_ref is host-qualified
(`"%s%s" % (_HYGIENE_COORDBACKUP_PREFIX, canon.lower())`) and its repair
commands are Mac-specific (`launchctl`, `~/REE_Backups`), so a session that
worked it on a cloud box would hit `launchctl: command not found` rather than
a silent false-clear -- lower severity than the refwedge case, but the same
defect shape, and it was never chipped live (zero `chip-coordbackup-*` rows
exist yet), so nobody had reason to notice.

**This is the concrete evidence for the structural direction.** A survey
session specifically hunting for "which machine-local sources lack the
declaration" still missed one instance. A per-callsite fix is not
self-auditing: it depends on someone re-deriving the full family list
correctly every time, and the record shows that has now failed twice (the
2026-08-18 fix wired one call site and left four; the 2026-08-22 survey
enumerating those four missed a fifth).

Full current tally (12 prefixes in `_MACHINE_LOCAL_RESOLVE_PREFIXES`, 7
covered / 5 missing):

| Prefix | Function | Declared? |
|---|---|---|
| `_HYGIENE_GC_PREFIX` | `_metaworker_worktree_gc_findings` / `_gc_sweep_prompt` | YES |
| `chip-stash-` | `_stash_findings` | YES |
| `chip-stashrebase-` | `_stash_findings` (same function) | YES |
| `chip-worktreeskills-` | `_worktree_skills_findings` | **NO** |
| `_HYGIENE_REFWEDGE_PREFIX` | `_ref_convergence_wedge_findings` | **NO** |
| `_HYGIENE_STRANDED_PREFIX` | `_stranded_prompt` | YES (the 2026-08-18 fix) |
| `_HYGIENE_CLINICALGUARD_PREFIX` | `_clinical_guard_findings` | **NO** |
| `_HYGIENE_WTREMOVED_PREFIX` | `_removed_worktree_live_worker_findings` | **NO** |
| `_HYGIENE_SCRIPTSCORPUS_PREFIX` | `_scripts_corpus_findings` | YES |
| `_HYGIENE_UNLANDED_PREFIX` | `_unlanded_prompt` | YES |
| `_HYGIENE_COORDBACKUP_PREFIX` | `_coordinator_backup_findings` | **NO** (newly found) |
| `_HYGIENE_GITSYNCVERDICT_PREFIX` | `_git_sync_repair_findings` | YES |

## 4. Proposed fix -- structural (option b in the originating chip), not a 5th patch

Add one function and one call in `run_tick`'s existing per-finding loop
(the loop already iterates every finding immediately before
`chip_ledger.cmd_record` -- `scripts/hygiene_routine_tick.py` around line
7024), rather than hand-wiring the 5 missing call sites individually:

```python
_HOST_DECLARATION_MARKERS = ("THIS CHIP MUST RUN ON ", "MINTING HOST UNKNOWN.")


def _ensure_host_declared(finding: dict) -> dict:
    """Structural backstop: any finding whose chip_ref falls under
    `_MACHINE_LOCAL_RESOLVE_PREFIXES` gets a host declaration even if its own
    mint site never called `_host_declaration` -- see
    chip-20260822-hygiene-machinelocal-prompts-declare-no-host, and the 5th
    gap (`_coordinator_backup_findings`) this backstop's own design process
    found that a dedicated per-callsite survey missed.

    Gates on PREFIX MEMBERSHIP, not on remembering a call at the mint site --
    the same "guard for the day someone admits the prefix" instinct
    `_MACHINE_LOCAL_RESOLVE_PREFIXES`'s own comments already apply to
    *resolution*, applied here to the *prompt* half of the same finding. A
    future prefix added to that tuple without wiring `_host_declaration` at
    its mint site is still declared, here, unconditionally.

    IDEMPOTENT -- a prompt that already carries either exact marker
    `_host_declaration` emits is left untouched, never double-declared.
    """
    ref = finding.get("chip_ref", "")
    if not ref.startswith(_MACHINE_LOCAL_RESOLVE_PREFIXES):
        return finding
    prompt = finding.get("prompt", "")
    if any(m in prompt for m in _HOST_DECLARATION_MARKERS):
        return finding
    declaration = "\n".join(_host_declaration(None, finding.get("title") or ref))
    finding = dict(finding)
    finding["prompt"] = declaration + "\n" + prompt
    return finding
```

`run_tick`'s recording loop:

```python
    chipped, errors = [], []
    for f in all_findings:
        f = _ensure_host_declared(f)
        if dry_run:
            ...
```

`_host_declaration(None, subject)` resolves the host the same way every
existing call site does implicitly (`chip_ledger.local_host()`, canonicalized)
-- correct here because `run_tick` runs synchronously on one box per
invocation, so every finding in `all_findings` was generated on the box
running this tick.

**This does not replace the per-callsite pattern** -- sources that already
call `_host_declaration` themselves (with a specific, subject-appropriate
sentence) are untouched, because the marker check makes the backstop a no-op
for them. It only fires for a finding that reaches the recording loop with no
declaration at all, which after this fix can only be a *future* omission --
this closes 3, 4 and 5 (worktreeskills, clinicalguard, wtremoved, refwedge,
coordbackup) as well as anything not yet imagined.

## 5. Held-out check (CLAUDE.md "Held-out check before shipping a standing-rule change")

Non-degeneracy: a case counts only if OLD (current code, no backstop) and
NEW (with `_ensure_host_declared`) give different answers.

**21 of 21 `chip-refwedge-*` rows in `TASK_CHIPS.json` are real historical
cases where OLD and NEW differ**, none of which were used to construct the
fix (the fix was derived from `_MACHINE_LOCAL_RESOLVE_PREFIXES` membership,
not from reading these rows). Verified directly against the ledger:

```
$ python3 -c "... every chip-refwedge-* prompt ..."
21/21 have NEITHER 'THIS CHIP MUST RUN ON' NOR 'MINTING HOST UNKNOWN'
```

Three examined in detail:

1. `chip-refwedge-ree-cloud-5-ree-working-master-since-2026-08-21t23-41-57z`
   -- the exact occurrence-2 near-miss (Section 2 above). OLD: no
   declaration; a DLAPTOP session's own confirmation command
   (`ref_convergence.py --check`) would have returned a clean exit 0 about
   the wrong box. NEW: `_ensure_host_declared` would have prepended "THIS
   CHIP MUST RUN ON ree-cloud-5" -- correct, since the finding was minted by
   a `ree-cloud-5` tick and the resolving session, once it did ssh there,
   confirmed the wedge was genuinely real and clearable only on that box.
2. `chip-refwedge-ree-working-master` (the earliest surviving refwedge row,
   pre-dating even host-qualified *refs* -- resolved before the 2026-08-15
   ref-qualification fix). OLD: no declaration, no host in the ref either.
   NEW: `_ensure_host_declared` still fires (gated on the *prefix*, not on
   ref shape) and declares whatever `chip_ledger.local_host()` resolves to
   at mint time -- degraded gracefully to `MINTING HOST UNKNOWN.` on a box
   where identity cannot be resolved, matching `_host_declaration`'s own
   documented fail-open behaviour, never a wrong declaration.
3. Pre-fix `chip-strandedwt-*` rows (11 rows, spawned 2026-08-16T10:27Z
   through 2026-08-17T08:25Z, i.e. before `271e9d9f` landed 2026-08-18-19).
   OLD: no declaration (matches the confirmed occurrence-1 defect). NEW:
   would have declared automatically, even before the hand-fix existed --
   the backstop would have prevented occurrence-1 outright, not just
   occurrence 2.

**Idempotency / regression check (not a differing case, but required before
shipping):** 43 post-fix `chip-strandedwt-*` rows (spawned 2026-08-19T07:22Z
onward) already carry `THIS CHIP MUST RUN ON`. Confirmed the marker check in
`_ensure_host_declared` matches `_host_declaration`'s own exact opening
phrases, so these are left byte-for-byte untouched -- no double declaration.

**Negative control (must NOT change):** every non-machine-local prefix
(`chip-staleclaim-`, `chip-sqdrift-`, `chip-planfm-`, `chip-ledgerint-`,
`chip-vendordrift-`, `chip-notlanded-`, `chip-statusregress-`) is absent from
`_MACHINE_LOCAL_RESOLVE_PREFIXES` by inspection (Section 3's table is
exhaustive over that tuple), so `_ensure_host_declared`'s `startswith` gate
never fires for them -- pinned by a test asserting exactly this for one
representative (`chip-staleclaim-`).

**Honest counterweight (per CLAUDE.md, must not be dropped):** this
structural check cost real time -- the full call-site remap in Section 3,
plus reading all 21 refwedge rows plus the 43 post-fix stranded rows -- and
found one thing worth the cost (the 5th gap) rather than several. A narrower
session might have shipped the 4-call-site patch faster and moved on; the
recurrence itself is the argument that the extra cost was worth paying here,
not a claim that it always will be.

## 6. What this does NOT do

- Does not touch `_chip_is_this_box` / the resolution gate -- that side is
  already correct and this doc does not propose changing it.
- Does not backfill declarations into already-minted, already-open chips
  (there are currently zero open `chip-refwedge-*`/`chip-worktreeskills-*`/
  `chip-clinicalguard-*`/`chip-wtremoved-*`/`chip-coordbackup-*` rows to
  backfill -- verified against the live ledger this session; if that changes
  before this lands, note it in the decision chip rather than silently
  re-deriving).
- Does not add a 6th machine-local family or change
  `_MACHINE_LOCAL_RESOLVE_PREFIXES`'s membership.

## 7. Tests (to be written only after the decision chip is answered)

Following `scripts/test_hygiene_routine_tick.py`'s existing convention
(class-per-source, `test_the_prompt_declares_the_minting_host`,
`test_the_declaration_is_the_FIRST_thing_in_the_prompt`, etc. -- see e.g.
lines 2245-2307, 4736-4825):

- One test per currently-undeclared family (`_worktree_skills_findings`,
  `_ref_convergence_wedge_findings`, `_clinical_guard_findings`,
  `_removed_worktree_live_worker_findings`, `_coordinator_backup_findings`)
  asserting the finding's prompt, AFTER `_ensure_host_declared`, contains
  `THIS CHIP MUST RUN ON` (or `MINTING HOST UNKNOWN` under an unresolvable
  identity, matching the existing `_HOST_DECLARATION_MARKERS`-style tests).
- `test_ensure_host_declared_is_idempotent_on_an_already_declared_prompt` --
  feed it a finding whose prompt already contains the marker; assert byte
  equality before/after.
- `test_ensure_host_declared_never_touches_a_non_machine_local_finding` --
  the negative control from Section 5, run against `chip-staleclaim-`.
- A meta-test in the spirit of the existing
  `test_the_gated_prefix_set_is_the_minting_sites_own_constants` (line 3759):
  assert `run_tick`'s recording loop calls `_ensure_host_declared` on every
  finding before `cmd_record` -- so a future refactor of that loop cannot
  silently drop the backstop.

Run per CLAUDE.md "Running the umbrella `scripts/` test corpus", from the
MAIN CHECKOUT for a trunk verdict:
```
/Users/dgolden/REE_Working/scripts/run_scripts_tests.sh test_hygiene_routine_tick.py
```
