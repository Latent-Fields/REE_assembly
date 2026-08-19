**Status: LANDED (code), AWAITING USER REVIEW (this writeup's recommendation).
The code described here (the `ree_commit_once()` sha-tracking fix and the
`--to-remote-tip` CLI wiring on `task_claim.py`/`chip_ledger.py`) is on
`REE_Working` `origin/master` as of `307de8d3d0` -- it is fully opt-in
(default off) and inert unless a caller explicitly passes the new flag, so
no existing writer's behavior changed. What is under review here is the
SEPARATE decision of whether/when any caller should flip `--to-remote-tip`
on by default, which this document deliberately does NOT do.**

# Wiring `--to-remote-tip` into task_claim.py / chip_ledger.py (2026-08-19)

Chip: `chip-20260818-wire-taskclaim-chipledger-remotetip`, the follow-on this
chip's own prompt named from
[`remote_tip_bookkeeping_writes_staged_20260818.md`](remote_tip_bookkeeping_writes_staged_20260818.md)
section 6 -- "the caller-wiring blocker found by tracing the contract" -- and
section 10's recommendation ("do not wire ... without first fixing the
`ree_commit_once()` / `verify_landed()` sha-tracking contract").

## 1. The contract fix

`ree_commit_once()` (`scripts/task_claim.py`, shared by `chip_ledger.py`)
determined whether a commit landed, and which sha to read committed content
back from, by comparing `head_sha(repo)` before and after the `ree_commit.py`
subprocess call. Under `--to-remote-tip`, on SUCCESS local HEAD never moves
(that is the whole point of the mode), so before == after and the old code
returned the STALE pre-write sha.

Fixed by capturing stdout ONLY when `to_remote_tip and push` (so every other
call is byte-identical to before -- see section 5's negative control) and
parsing `land_at_remote_tip()`'s own machine-parseable
`ree_commit: to-remote-tip sha=<40-hex>` line
(`_parse_remote_tip_sha()`, a `re.MULTILINE` search, not a full-string match,
because the line appears in two shapes -- the idempotent "already on origin"
path prints it as a second line after a status line, the ordinary success
path appends trailing text after the sha). On the fallback (failure) path,
`land_at_remote_tip()` never prints this line at all, so the existing
before/after `head_sha()` diffing (unconditional, unchanged) is what still
raises `CommitLandedLocally` -- see section 4 below for why this composition
is safe by construction rather than merely tested.

## 2. The CLI wiring

`--to-remote-tip`, opt-in, default off, added to:

* `task_claim.py`: `open`, `close`, `amend` (the three CLAUDE.md's own
  section-2 audit named as mechanically-safe -- keyed by
  `(session_id, claimed_at)`, which `_verify_keyed_merge_faithful` can prove).
  Deliberately NOT on `renew`/`dedupe` (out of scope per the chip's own task
  list, and both share the `common` parser group with the three that DO get
  it -- adding it to `common` would have advertised a flag that silently does
  nothing for those two).
* `chip_ledger.py`: `record`, `resolve`, `claim`, `amend-prompt`,
  `amend-urgency` (keyed by `chip_ref`). Deliberately NOT on
  `unclaim`/`attach`, same reasoning.

`mutate_and_commit()` in both files validates `to_remote_tip and not push`
BEFORE acquiring the mutation lock and dies with a clear message (mirroring
`ree_commit.py`'s own `--to-remote-tip requires --push` validation one level
up, so a misuse is a clear CLI error rather than a confusing subprocess
failure). This validation checks the REQUESTED push, not a later
`push_gate`-downgraded one -- see section 4's held-out case for why that is
the correct place to check.

## 3. A live production bug this same change introduced, and fixed the same day

Both files' `cmd_record`/`cmd_resolve`/`cmd_claim`/`cmd_open`/`cmd_close`/
`cmd_amend` initially read `args.to_remote_tip` as a hard attribute access.
`chip_ledger.py`'s `push_explicit_of()` already documents, in its own
docstring, that `hygiene_routine_tick.py` / `proposal_routine_tick.py` /
`igw_routine_tick.py` build an `argparse.Namespace` BY HAND and call
`cmd_record()`/`cmd_resolve()`/`cmd_claim()` directly, never through
`build_parser().parse_args()` -- so those Namespaces never carry a
`to_remote_tip` attribute at all. A hard access is therefore not a
hypothetical failure mode; it is `push_explicit_of()`'s own precedent,
inverted.

This shipped anyway, briefly, because the intermediate WIP commit that got
merged onto this box's `master` (see section 6 on how) still had the naive
hard-access form. **Confirmed live**: `hygiene_routine_tick.py`'s dispatch
cycle 3138 (2026-08-19T17:44Z) hit 21 `AttributeError` on
`args.to_remote_tip`, one per chip it tried to auto-resolve that cycle, and
auto-recorded its own chip about it
(`chip-20260819-chipledger-cmdresolve-toremotetip-namespace-attr`). Fixed by
switching all 8 call sites to `getattr(args, "to_remote_tip", False)`,
matching `push_explicit_of()`'s existing pattern exactly, with a comment at
the `chip_ledger.py cmd_record` site naming the three in-process callers so
the next similar flag addition does not repeat this. That auto-recorded chip
is resolved `done`, noting the fix.

**This is itself a live illustration of GOV-HELDOUT-1's value, discovered
the hard way rather than found by discipline**: the held-out check in
section 4 below treats "in-process callers with a hand-built Namespace" as
one of its two surviving cases specifically because this is documented,
pre-existing repo history (`push_explicit_of()`'s docstring) that the naive
version failed. It should have been checked BEFORE shipping the naive
version; it was instead checked (and fixed) only after production feedback
supplied the same evidence a deliberate check would have.

## 4. Held-out check (GOV-HELDOUT-1)

**2 differing cases found, not 3 -- reported honestly per the rule's own
escape hatch.** The MOTIVATING case (section 1's sha-tracking contract
break) is excluded from the count, per the same reasoning
`remote_tip_bookkeeping_writes_staged_20260818.md` section 8 uses for its own
check: it is what this fix was written FROM, not an independent case to
validate against.

**Differing:**

1. **In-process callers building `argparse.Namespace` by hand** (section 3
   above). OLD (a hard `args.to_remote_tip` access) breaks
   `hygiene_routine_tick.py` / `proposal_routine_tick.py` /
   `igw_routine_tick.py`'s calls into `chip_ledger.cmd_record`/`cmd_resolve`/
   `cmd_claim` with `AttributeError` -- confirmed, not hypothetical, by the
   live 2026-08-19T17:44Z incident. NEW (`getattr(args, "to_remote_tip",
   False)`) does not. This is `push_explicit_of()`'s own documented
   precedent for the identical shape of hazard, so the check is against a
   real historical case in this file's own history, not an invented one.
2. **The 2026-08-09 triple-insertion incident** (`CommitLandedLocally`,
   `task_claim.py`'s own module docstring). A plausible-but-wrong
   implementation of the sha-parsing fix would try `_parse_remote_tip_sha()`
   unconditionally (including on a non-zero exit, where
   `land_at_remote_tip()`'s fallback path prints no `sha=` line and instead
   does an ordinary local CAS) and could therefore MISS the
   `before != after` condition that raises `CommitLandedLocally`, silently
   returning a wrong sha instead of flagging the "committed but not pushed"
   state the 2026-08-09 incident's fix depends on. The shipped code
   structurally cannot do this: sha-parsing is attempted only inside
   `if p.returncode == 0:`, and the existing `if before and after and after
   != before: raise CommitLandedLocally` check is unconditional and
   unchanged below it. Verified by composition (the fallback case never
   reaches the parsing branch, by construction) plus by the pre-existing
   `test_task_claim_retry_duplicate_commits.py` / `test_task_claim_
   retry_restore.py` suites (16 tests covering exactly this incident) still
   passing unmodified in behavior (their monkeypatches needed a
   signature-only update for the new kwarg, not a semantic one -- see
   section 5). Not separately re-driven end-to-end under
   `to_remote_tip=True` specifically with a genuine forced conflict (that
   would need a 2-writer fixture beyond what this session built); named as a
   residual gap rather than claimed as full coverage.

**Search for a third came up empty.** The two cases above are both
pre-existing, documented incidents in this same pair of files
(`push_explicit_of()`'s docstring; `CommitLandedLocally`'s docstring) --
which is also why a third was hard to find: this session did not identify
another comparably-documented historical incident in `task_claim.py`/
`chip_ledger.py` whose old/new call would differ under this specific change.
Per the rule: this change is validated against two concrete precedents in
the same files, not against a broader historical record, and should be read
accordingly.

**A separate, non-incident-based check that materially shaped scope** (noted
per the same convention `remote_tip_bookkeeping_writes_staged_20260818.md`
section 8 uses): the orphan-push withhold guard
(`make_orphan_push_gate()`/`entry_is_orphaned()`) can downgrade `push` from
True to False AFTER `mutate_and_commit()`'s up-front `to_remote_tip and not
push` validation has already passed. Traced this rather than assumed it:
the validation deliberately checks the REQUESTED push (asked for by the
caller), not the possibly-withheld one, so a withheld push silently makes
`--to-remote-tip` a no-op for that attempt (the flag is only appended to the
`ree_commit.py` invocation `if push:`) rather than crashing or forcing a
push past the withhold. Verified end-to-end:
`test_task_claim_remote_tip.py::RemoteTipOrphanGuardInteractionTest` --
`open --no-push` (so the entry never reaches origin), then
`close --to-remote-tip --push` (explicit), asserts the close still commits
LOCALLY (content correct), the push is withheld exactly as it would be
without `--to-remote-tip`, nothing reaches origin, and the command exits
`ORPHAN_PUSH_EXIT` (5) because `--push` was explicit -- the identical
contract `close` already has without this flag.

## 5. Tests

`scripts/test_task_claim_remote_tip.py` (14 tests) and
`scripts/test_chip_ledger_remote_tip.py` (7 tests), real bare remotes, real
checkouts, real `ree_commit.py` subprocess calls -- no mocking of git
itself. Time-independent, ASCII-only.

* `ParseRemoteTipShaTest` (5): both success-line shapes; absent on the
  fallback's differently-shaped output; absent on `None`/empty; a malformed
  or short "sha=" value does not false-match.
* `RemoteTipOpenTest` / `RemoteTipCloseTest` / `RemoteTipAmendTest` (6): local
  branch ref byte-identical before/after a successful `--to-remote-tip` call;
  content lands on the real remote; **the regression this chip exists to
  fix** -- `close`'s post-commit self-check (`verify_landed()`, FATAL) does
  NOT report a false `SELF-CHECK FAILED`, and `open`'s (WARNING) does not
  report a false `SELF-CHECK WARNING` either.
* `RemoteTipOrphanGuardInteractionTest` (1): section 4's held-out design
  case, above.
* `RemoteTipRecordTest` / `RemoteTipResolveTest` (3, chip_ledger): same local-
  ref and remote-landing properties for `record`/`resolve`.
* `InProcessCallerNamespaceTest` (2, chip_ledger): section 3's production
  hazard, reproduced directly -- a hand-built `Namespace` missing
  `to_remote_tip` entirely, passed straight to `cmd_record()`/`cmd_resolve()`,
  does not raise.
* `RemoteTipNegativeControlTest` (2, one per file) -- **the load-bearing
  negative controls**: a caller NOT passing `--to-remote-tip` still advances
  local HEAD immediately on success, unchanged from before this parameter
  existed.
* `--to-remote-tip requires --push` validation (2, one per file).

**Existing suites, re-run in full, not just the touched files** (per the
chip's own instruction): all 32 pre-existing `test_task_claim_*.py` /
`test_chip_ledger_*.py` files, plus the two new ones (34 total) -- 34/34
green. Plus `test_hygiene_routine_tick.py`, `test_proposal_routine_tick.py`,
`test_igw_spawn_chip_crosswrite_and_resolve.py` (the three files that
exercise the REAL in-process-Namespace callers named in section 3) -- 3/3
green. 37/37 total, run from the main checkout (not a worktree) for correct
module provenance per CLAUDE.md's "Running the umbrella `scripts/` test
corpus" section.

**7 existing test files needed a signature-only update**, not a behavioral
one: their monkeypatched `commit()` stand-ins had a fixed 3-argument
signature (`message, push, bot`), which broke once the real call sites
started passing `to_remote_tip=...` as a keyword. Fixed by adding
`to_remote_tip=False` (or `**kwargs` where already present) and forwarding
it to the real `commit()` where the stand-in delegates to it. This is the
"real, separate testing pass" `remote_tip_bookkeeping_writes_staged_20260818.md`
section 6 point 4 named as necessary before wiring: `test_task_claim_
overlap.py`, `test_task_claim_claim_rescue_wiring.py`, `test_task_claim_
retry_restore.py`, `test_task_claim_retry_duplicate_commits.py`,
`test_chip_ledger_orphan_recovery.py`, `test_chip_ledger_claim_rescue_
wiring.py`, `test_chip_ledger_confirmer_gate.py`.

## 6. Recommendation

* **The flag is landed and usable now** -- `origin/master` `307de8d3d0`.
  Opt-in, tested, and the negative controls prove every existing caller
  (including the three real in-process callers that build `Namespace` by
  hand) is unaffected when the flag is not passed.
* **Do not flip any caller's default to pass `--to-remote-tip`
  automatically.** This chip's task was explicit that making the flag
  USABLE is the deliverable, not making it the default, and the held-out
  check above is scoped to two cases in these two files -- not validated
  against the broader historical record the way
  `remote_tip_bookkeeping_writes_staged_20260818.md` section 8 already
  flagged for the underlying mechanism itself.
* **Consistent with that document's own section 10**: once wired (done
  here), the natural next step is a soak period on manual/low-stakes
  invocations before considering flipping either script's default. Nothing
  in this session's work shortens that soak period or substitutes for it --
  a caller-level default flip is a separate, future decision.
* **Follow-on, not attempted here** (same as the prior document): fixing
  `governance_flag.py`'s / `confirmer_verdict.py`'s registry keying gap
  (tracked as `chip-20260816-reecommit-idfields-registry-keys`) before
  considering `--to-remote-tip` for those two callers -- their registries
  still lack a working unique key for `_verify_keyed_merge_faithful` to
  prove against, exactly as section 2 of the prior document found.
