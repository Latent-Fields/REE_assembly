# Diagnosis-handoff gap investigation (2026-08-26)

**Status:** Investigated, fix implemented and landed.
**Chip:** `chip-20260826-diagnosis-handoff-gap`
**Motivated by:** `chip-20260826-cloud4-to-cloud5-ssh-key-gap-authorise`'s recurrence
note -- the same SSH-key-provisioning finding diagnosed and closed `done` three
times in 11 days, each time handed to a human/later session that never picked
it up.

## 1. The question

`TASK_CHIPS.json`'s `status` field has three values: `open`, `done`,
`withdrawn`. `done` is used for two outcomes that are not the same thing:

1. The work is actually finished -- nothing further needed.
2. This session's *own* part is finished (it diagnosed something, made a
   decision, or completed a partial step), but it explicitly handed a
   **remaining action** to someone/something else -- a human, a later
   session, a manual out-of-band step -- and closed the chip `done` anyway,
   because there was nothing more *this session* could do.

Nothing distinguishes case 2 from case 1 in the schema, and nothing tracks
whether the handed-off action ever actually happened. The brief asked: does
the chip ledger need a status distinct from `done` for this, are there other
historical chips with this shape, and (after a held-out check against >= 3
non-degenerate cases) what is the right fix.

## 2. Method

1. Read the motivating chip's recurrence note and the two prior chips it
   named (`chip-20260816-cloud5-ssh-key-deploy`,
   `chip-20260820-cloud5-heartbeat-stale-ssh-permdenied`) to confirm the
   exact shape of the gap.
2. Scanned all 1719 entries in `TASK_CHIPS.json` for `status: done` chips
   whose `resolution_note` contained handoff-signal language (`no route`,
   `needs a human`, `unfixed`, `awaiting`, `DIAGNOSED, not`, `PENDING`, `not
   yet chipped`, `depends on`, `manual step`, `cannot perform myself`, ...).
   A naive `diagnos|hand.?off` regex over-matched badly (157 hits, dominated
   by "diagnosed AND fixed" false positives); narrowing to phrases that
   assert *incompleteness* specifically brought this down to a workable set.
3. Manually triaged the narrowed set, distinguishing:
   - Genuine handoff gaps (a chip closed `done` with a real, unactioned next
     step for someone else) -- the target shape.
   - Chips that are legitimately `done`: a deliberate decision not to act
     ("DID NOT QUEUE -- correct outcome"), a scoping task whose own brief
     said "scoping first, not a patch" (and whose follow-on *was* picked up
     by a later chip -- `chip-20260816-coordinator-canonical-identity-deploy`
     actually built on `chip-20260815-coordinator-canonical-machine-identity`
     three days later, which is the system working as designed and a useful
     negative control).
   - A different, superficially similar phenomenon: the `refwedge-*` chip
     family (23 occurrences across 11 days as of this writing, two of them
     open right now under `chip-20260826-refwedge-class-persists-post-fix` /
     `chip-20260826-refwedge-class-recurrence-investigation`). Each
     individual `refwedge` chip's diagnosis-to-fix cycle *was* actually
     executed by the closing session (confirmed by reading several
     resolution notes -- e.g. "ran the safe_adopt_ref.py --allow-discard
     call directly instead of waiting"), not handed to an unactioned human
     step. The recurrence there is a self-feeding ROOT CAUSE (each
     throwaway-worktree push leaves the shared ref further behind, so the
     next commit joins an ever-harder-to-prove ahead set) -- already
     recognised and under separate, active investigation. **Deliberately
     excluded from this investigation's scope** to avoid conflating two
     different failure modes that would want two different fixes.
4. For the surviving candidates, verified against **live, current state**
   rather than trusting the resolution note's own account -- this is a
   headless session running on `ree-cloud-5`, which happens to be the
   subject box for one of the candidates, so a direct check was possible.

## 3. Three confirmed, non-degenerate cases

Per CLAUDE.md's "Held-out check before shipping a standing-rule change" and
GOV-HELDOUT-1: the proposed fix is checked against >= 3 real cases the rule
was **not** written from, verifying old and new give **different** answers.
All three below are non-degenerate by that test -- the old regime (no
tracking) produced silent staleness in every one; a mechanism that flags an
unverified handoff after some threshold would have caught all three, at
different lead times.

### Case A -- SSH-key provisioning gap (recurred 3x over 11 days)

- `chip-20260816-cloud5-ssh-key-deploy` (kind: decision) -- authorised
  ree-cloud-5's own outbound key on the hub only (option A of the chip).
  This did **not** cover the cloud-4 -> cloud-5 direction.
- `chip-20260820-cloud5-heartbeat-stale-ssh-permdenied` (kind: work) --
  diagnosed the cloud-4 -> cloud-5 direction specifically. Resolution note:
  *"DIAGNOSED, not fixed (no route to cloud-5's authorized_keys from here)
  ... Root cause is almost certainly a key-provisioning gap ... this box's
  OUTBOUND key ... was never appended to ree-cloud-5's authorized_keys."*
  Closed `done` 2026-08-20T12:37:10Z with an explicit handoff: "a session
  with admin/cloud-5 access to append the key."
- `chip-20260826-cloud4-to-cloud5-ssh-key-gap-authorise` (kind: decision,
  **still open** as of this writing) -- rediscovered the *identical*
  finding 6 days later, via an unrelated symptom (a fleet-health probe
  failing), and named the recurrence explicitly: *"this is the third
  distinct chip on the cloud-4<->cloud-5 SSH-key-gap class in 11 days ...
  The pattern is not the SSH mechanism itself but the HANDOFF."*

Old regime: 6 days of silent staleness, discovered by accident via a
different symptom, not by anything that was watching the handoff.

### Case B -- hcloud read-only token (still unresolved 7 days later, verified live)

`chip-20260819-cloud5-hcloud-readonly-token` closed `done` 2026-08-19T17:36:26Z.
Resolution note ends: *"User's remaining manual step: on ree-cloud-5, generate
a Read-only token in the Hetzner Console, then run 'hcloud context create
ree-cloud5-readonly' and paste it when prompted; verify with 'hcloud context
use ree-cloud5-readonly && hcloud server list' ... Step 3 live verification
NOT executed by this session since it requires the token."*

This investigation is running **on ree-cloud-5**, so the claim was checked
directly rather than trusted:

```
$ hcloud context list
ACTIVE   NAME
$ ls -la ~/.config/hcloud/
(empty directory)
```

Confirmed: **7 days later**, the manual step was never done, and -- unlike
Case A -- nothing has rediscovered it yet. No fleet symptom depends on the
diagnosis-only hcloud token (`remote_pytest.sh`'s wake-and-route fall-through
needs the separate, declined write-scope option), so this gap could sit
indefinitely with zero visible symptom. This is the worst-case instance of
the pattern: not just slow rediscovery (Case A), but potentially **no**
rediscovery at all.

### Case C -- ingress-dispatch architecture decision (fresh, self-aware, nowhere to put that awareness)

`chip-20260826-ingress-dispatch-architecture-decision` closed `done` the same
day (2026-08-26T12:41:04Z, ~9h before this investigation started). Resolution
note: *"User decided (b): authorize cloud->Mac SSH ... Implementation is
PENDING the user's own manual SSH-key-add step (system/security-setting
change I cannot perform myself) ... Follow-on wiring chip needed once
reachability is confirmed; **not yet chipped since it depends on the key
actually being added first.**"*

This is the clearest evidence for the diagnosis: the closing session
*already knew* it was creating exactly this gap (a done chip with an
unactioned dependency) and had no structured way to say so beyond prose in a
note that nothing re-reads. Too fresh (as of this writing) to know whether it
would have recurred like Case A or gone silent like Case B -- included as the
held-out check's non-degenerate case for "the closer is aware of the gap in
real time," which the other two do not test.

## 4. Why not a fourth `status` value

Considered and rejected. `VALID_STATUS = ("open", "done", "withdrawn")` and
`TERMINAL_STATUS = ("done", "withdrawn")` are read by every dispatch-facing
consumer in the ledger: `dispatch_candidate_order.load_open_work_chips`,
`check_dispatch_fleet_health`'s backlog scan, GC sweeps
(`metaworkergc-*`), hygiene-tick recurrence checks, `/workset`,
`morning-digest`, and more. A fourth status (e.g. `handed_off`) would need
every one of those consumers individually decided for: is a handed-off chip
dispatchable again? GC-eligible? Counted in backlog? The honest answer for
nearly all of them is "yes, treat it exactly like `done`" -- a
handoff-pending chip's own work really is finished, and nobody should
re-dispatch it. That argues for **not** touching `status` at all, and
instead adding a narrow, separately-read tracker for the one thing that
actually differs: whether the external action was verified.

This also matches the codebase's own established pattern for "make a backlog
visible without touching core state" -- `audit_orphan_chips.py`,
`audit_stale_claims.py`, and the other `audit_*.py` scripts are all
report-only readers layered on top of unchanged core fields, not schema
changes.

## 5. Fix implemented

Landed in `REE_Working` `8bf57be6` (origin/master) and `TASK_CHIPS.json`
commits `7481c8de21` / `0d5e645702`. See `scripts/chip_ledger.py`'s own
"HANDOFF-PENDING" docstring section for the authoritative reference; summary:

- **New field**, not a new status: `handoff_pending` on every chip (`None`
  by default). Set via `resolve --status done --handoff-pending
  "<description>"` at close time, or retroactively via `declare-handoff
  --chip-ref REF --description "..."` on an already-`done` chip.
- **`{description, since, declared_by, status, last_checked_at,
  last_checked_by, last_checked_note}`** where `status` is one of `pending`
  (the only non-terminal value), `confirmed_done`, `abandoned`.
- **`verify-handoff --chip-ref REF --status <pending|confirmed_done|
  abandoned> --note "..."`** is the only way the tracker's own status moves.
  `pending` (re-passed) just re-timestamps the check, resetting the audit
  clock without asserting anything is fixed. A move between the two
  terminal values requires `--force`, same discipline as `resolve --force`
  on the chip's own status. Every status transition is recorded in
  `status_history`, never a silent overwrite.
- **`scripts/audit_handoff_gaps.py`** -- report-only reader (matches
  `audit_orphan_chips.py`'s own conventions): scans every `done` chip with
  `handoff_pending.status == "pending"`, buckets FRESH/STALE by age since
  `last_checked_at` (or `since` if never checked) against a threshold
  (default 24h), `--json`/`--exit-nonzero` for gating. Deliberately does
  **not** auto-raise a follow-up chip in v1 -- `audit_orphan_chips.py`
  defers its own auto-action the same way, pending observation of the
  report-only output against the real backlog; the same reasoning applies
  here and a second false-positive-rate question (a handoff genuinely still
  pending vs. one the closer forgot to `verify-handoff` after it cleared) is
  not yet answered by any real usage.
- Tests: `scripts/test_chip_ledger_handoff_pending.py` (18 tests, real
  git-repo harness, same pattern as
  `test_chip_ledger_resolve_terminal_guard.py`) and
  `scripts/test_audit_handoff_gaps.py` (15 tests, pure unit tests over
  `scan()` with an injected `now` -- time-independent -- including a direct
  replay of all three cases above as a held-out check pinned in code, not
  just prose).
- No regression: the full pre-existing `test_chip_ledger*.py` /
  `test_audit_orphan_chips.py` suite and `test_test_provenance.py`'s corpus
  check were re-run against the change; all pass (two pre-existing,
  unrelated `test_test_provenance.py` corpus failures on
  `test_dispatch_budget_gate.py` / `test_hygiene_queue_floor_and_mint_cap.py`
  predate this session by hours and are untouched by it).

### Demonstrated against real data

Backfilled the two still-relevant live cases (Case A's own chip is
superseded by its own open successor, so backfilling it would be historical
noise; Case B and Case C are live) and ran the audit:

```
== STALE (>= 24.0h unverified) (1) ==
  chip-20260819-cloud5-hcloud-readonly-token -- Install hcloud on ree-cloud-5 ...
    age: 172.3h (since 2026-08-19T17:36:26Z, last checked never)

== FRESH (1) ==
  chip-20260826-ingress-dispatch-architecture-decision -- Decide how ingress-gated ...
    age: 9.3h (since 2026-08-26T12:41:04Z, last checked never)
```

Case B -- the worst-case, silent-forever instance -- is immediately visible
as STALE the moment the audit is run, which is exactly the failure mode this
investigation was asked to close.

## 6. What this does not fix

- **Retroactive, not automatic.** Only chips explicitly declared via
  `--handoff-pending` or `declare-handoff` are tracked. A closer who forgets
  to use it reproduces the exact gap this investigation describes -- the
  fix changes what is *possible* to track, not what is *guaranteed*.
  `declare-handoff` exists specifically so a later auditor (a human, a
  hygiene-tick pass, another headless session) can backfill a chip whose
  closer didn't use `--handoff-pending` at resolve time, same as this
  session did for Cases B and C above.
- **No auto-escalation.** The audit is report-only; nothing currently wires
  it into `hygiene_routine_tick.py`'s ~5-minute cadence to auto-raise a
  follow-up chip for a STALE finding, unlike some other audit sources in
  that tick. This is a deliberate v1 scope limit (see Section 5), not an
  oversight -- wiring an auto-raise into the tick is exactly the kind of
  standing-behavior change that itself deserves observation of the
  report-only output first, per the same held-out-check discipline this
  investigation was asked to apply.
- **Does not touch the CLAUDE.md housekeeping section's chip-closing
  guidance.** Whether to require `--handoff-pending` as standard practice
  (a CLAUDE.md wording change) is a separate, higher-visibility decision
  left to a future session/user to ratify against this investigation's
  held-out check, rather than made unilaterally by a single headless worker
  editing the umbrella's governing document.

## 7. Recommended follow-on (not chipped by this session -- see below)

- Wire `audit_handoff_gaps.py --json` into `hygiene_routine_tick.py` as a
  new source, mirroring source 17/18's own pattern (report findings ->
  stable per-chip TASK_CHIPS.json work chip, never auto-repair), once the
  report-only output has been observed for a few days against the real
  backlog.
- Consider whether CLAUDE.md's chip-lifecycle section (Session Land Protocol
  "Every `spawn_task` call MUST be immediately paired with...") should name
  `--handoff-pending` as standard practice when resolving `done` with a
  real, unactioned dependency. This investigation's Section 3 is the
  held-out check such a wording change would need.

Not chipped: this investigation's own chip
(`chip-20260826-diagnosis-handoff-gap`) already covers "propose/implement a
fix," and the two items above are both small enough, and closely enough
coupled to this session's own context, that spawning a fresh chip for either
would mean a future session re-deriving everything already written here. Both
are named explicitly so a future session (or this ledger's own audit, once
observed) can pick them up directly.
