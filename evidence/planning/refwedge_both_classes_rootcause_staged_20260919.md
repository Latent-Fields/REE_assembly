# Refwedge, both classes: root cause (ree-cloud-5 REE_Working g3 + Mac REE_assembly g10)

**Status: AWAITING USER REVIEW**

- Session: `bold-swanson-1789a0` (/metaworker-learning), measured 2026-09-19T10:04Z-10:15Z.
- Chip: `chip-20260919-ml-refwedge-both-classes-rootcause` (supersedes
  `chip-20260919-ml-refwedge-chipledger-git-write-rootcause`).
- Decision chips raised from this doc: see section 8.
- Nothing was built, no ref was moved, no ledger was mutated to reproduce anything. ssh was read-only.

## 0. Answer in five lines

1. **Both classes are one mechanism: a LATCH, fed by interchangeable transient SEEDS.** Every writer that
   still commits client-side falls back to *landing the commit on the local branch* when its push /
   remote-tip landing fails. A locally-landed commit with no `-x` twin and no upstream patch-id is
   unprovable forever, so `ref_convergence` (correctly) refuses, the checkout stops adopting origin, and
   every later write to the same file is built on a base origin never had -- so it conflicts too. One
   transient failure becomes a permanent, self-feeding wedge.
2. **g8, g9 and g10 each had a DIFFERENT seed, and each learning pass removed exactly its own seed.** Both
   prior passes shipped real, deployed, working code (section 3). Neither removed the latch. That is why
   the referral "did not hold": it held for its seed.
3. **So both framings in the g10 referral are half right.** There IS a genuinely unfixed root cause (the
   latch), AND 24-72 h between wedges is the expected rate *while the latch exists*, because transient
   seeds arrive at about that rate (10 `cannot lock ref` fetch races in the Mac IGW log since 2026-08-28
   alone). Removing seeds one at a time will never converge; removing the latch will.
4. **Part 1's "git write not suppressed" is by design, not a regression**: config on ree-cloud-5 is armed
   and correct; the commits come from verbs that have no coordinator transport (`declare-handoff`,
   `resolve --handoff-pending`) plus `dispatch_budget_gate.py`. (Two plain `resolve`s also took the git
   path for a reason not determined from the commits alone -- section 1, open item.) The documented
   Healer procedure tells the healer to use exactly those verbs, so **the remedy for the wedge deposits another unpushable commit on
   the wedged checkout** (7 of the 12 ahead commits on ree-cloud-5 were minted by healers working the wedge).
5. **"Make convergence of provably-redundant commits automatic" does not fit g10**: its 10 unproven commits
   are NOT redundant -- they carry 22 `igw_routine_log.md` lines that exist nowhere on origin. The Healer's
   g10 audit did not cover that file. LIT-0805 is a non-issue (section 5).

## 1. Part 1 -- ree-cloud-5, REE_Working master (g3). Measured.

State at 2026-09-19T10:10Z (read-only ssh): `master...origin/master [ahead 12, behind 202]`.
`~/.ree_coordinator_client.json`: `mode=coordinator`, `suppress_git_write=True`, scope_root correct.
**Not** a missing/stale config, **not** a hollow ack, **not** a partial failure. ree-cloud-4: `[behind 1]`,
clean, same config -- same code, no seed yet.

The 12 ahead commits, oldest first:

| sha | writer | proven? |
|---|---|---|
| `37afd468d` 23:05:13Z | `dispatch_budget_gate.py` "budget tick recorded" | **NO -- the SEED** (no `-x` twin on origin) |
| `205f186b9` `c017d06c6` `431503709` `388fe88af` | same writer | yes (twins `a2ffbb3fe` `7a9b1edbf` `c29ce5a8d` `ad3e904ac`) |
| `13884d506` `70332c20a` `2856bd137` `64a14ebf0` `41cb2f231` | `chip_ledger.py` plain resolve / declare-handoff x3 / plain resolve -- **healer sessions working chip-checkoutdiverged-g2** (the two plain resolves: see open item) | no |
| `d371e448a` | healer resolving **this wedge's own chip** (g3) with `--handoff-pending` | no |
| `3e2fc946f` | healer resolving the **Mac's** `chip-wedgeaudit-...-g10` from ree-cloud-5 | no |

**Seed.** Two budget ticks 8 s apart (23:05:13Z, 23:05:21Z) while origin had just advanced (another box's
tick `d7d035251` 23:04:37Z). `dispatch_budget_gate.py:708-733` commits via
`ree_commit.py --bot --retry-push-on-reject` (no `--to-remote-tip`; the two are mutually exclusive). The
first tick's retry never produced a twin; its event reached origin folded into the second tick's twin
`a2ffbb3fe` (whole-file JSON, structurally merged). Content is on origin; the commit is unprovable.
`metaworker_dispatch_budget_log.json` is in neither `ref_convergence.REGISTRY_SPECS` nor
`reconcile_wedge_content.RECONCILABLE`, so `reconcile --check` REFUSES on sight and nothing can ever
adjudicate it. Wedge clock started 23:05:25Z -- 12 s after the seed.

**Amplifier.** `chip_ledger.py` verbs (file:line in the main checkout, 2026-09-19):

- Always git-path, no coordinator transport: `declare-handoff` (3815), `verify-handoff` (3887),
  `amend-urgency` (4455), `archive` (4742); and any `resolve` carrying `--handoff-pending` or a confirmer
  verdict (gate at 3714-3715). The coordinator has no `handoff_pending` column and no endpoint field
  (`ree-v3/coordinator/schema.sql:207-242`, `app.py:401-408`); the field survives renders only because
  `entry_json` is stored verbatim and `_carry_unmodelled` (`db.py:1014-1053`) re-attaches it -- after the
  local commit has reached origin and been *ingested*. No landing, no field.
- `unclaim`, `attach`, `archive` never pass `to_remote_tip` at all.
- `.claude/skills/metaworker-repair/SKILL.md:558-561` (Step 4b rule 3) instructs:
  "Finished your part, a human must do the rest -> `resolve --handoff-pending` (or `declare-handoff`...)".
  Step 3c makes that the *expected* outcome of a blocked wedge audit. On a wedged box each such call is
  one more local commit: three `declare-handoff`s on the same chip row guarantee the 2nd and 3rd conflict
  against the stranded 1st (same latch as the log file in Part 2).
- A-94's verb table is stale in two places (`attach`/`amend-prompt` gained transports 2026-09-01) and omits
  `amend-urgency`, `resolve --handoff-pending`, `episode`.

**Open item (not determined):** `13884d506` (`resolve ... -> done`) and `64a14ebf0` (`resolve
chip-statusregress-... -> withdrawn`) show no `handoff_pending` change in their diffs, so they should have
been suppressible. Candidates: the ack-verification fall-through (3738), the `local_miss` branch (3507), or
a confirmer verdict. The WARNING that names the reason goes to the healer session's stderr, which is not
logged anywhere on the box. Whoever builds F4 should make the git-path fall-through reason part of the
commit message trailer so the next audit can read it from `git log`. Each such commit also rewrites
several OTHER rows (origin-merge sweep on a 202-behind file), which is what makes them conflict later.

**Third live instance, found in passing:** the Mac's own `/Users/dgolden/REE_Working` is WEDGED right now
(`ref_convergence --check`: ahead 26, 2 unproven, 8.9 h, 24 refusals). 23 of 26 are patch-id-proven
`dispatcher_control.json` lease commits; the unproven ones are `chips: strip 1377 archived chip(s)` (the
`archive` verb -- always-git, never remote-tip), `WORKSPACE_STATE: scheduled rotation`, and an igw-tick
reaper `claim: close`. Same class, third writer population.

## 2. Part 2 -- the Mac, REE_assembly master (g10). Measured.

State at 2026-09-19T10:13Z: `[ahead 17, behind 32]`, origin `32368daafcd`. `git cherry`:

- **7 proven (`-`)**: three lit-pulls, three `nooarche` commits, one EXP status commit -- all landed on origin
  under a twin sha by push-retry. Harmless; they would converge on their own.
- **10 unproven (`+`)**: every one is `REE Automation (Mac)` `igw-ledger: update|spawn|complete`, and
  **every one touches exactly one file: `evidence/planning/igw_routine_log.md`.** Zero unproven commits
  touch any coordinator-suppressed IGW path (ledger, assignments, workset, proposals) -- suppression works;
  the log is the one IGW path still written client-side (`igw_log_suppress_git_write: False` on the Mac,
  every sibling flag `True`).

**Seed** (`~/Library/Logs/ree_igw_routine.launchd.log`, tick 2026-09-19T04:39:39Z):

```
ree_commit: to-remote-tip: fetch failed on attempt 1/5: error: cannot lock ref
 'refs/remotes/origin/master': is at 9c0e0ae... but expected 1c4a63c... -- falling back to local landing
```

A benign race with a concurrent `git fetch` (the other fetch *succeeded* -- the ref was already current).
`land_at_remote_tip` (`ree_commit.py:2826-2829`) returns `_fallback(...)` on the FIRST fetch failure despite
its own 5-attempt loop: "attempt 1/5" is printed and attempts 2-5 never run. Commit `3a0250e73a` became
local HEAD. This seed has occurred 10 times since 2026-08-28 on this box.

**Latch.** From the next tick on (06:03Z, 07:08Z, 08:14Z, 09:19Z -- 12 fallbacks so far): the new log commit's
parent O is a *local* blob origin never had. The g9 rule `_append_extension` (`ree_commit.py:3720-3723`)
requires `A.startswith(O)` (origin extends the base). Here it is the mirror: origin `A` is a byte-prefix of
`O`. Rule declines -> "GENUINE conflict, staying fatal" -> local fallback -> +1-3 commits per hour. At
06:41Z a session hand-landed 3 of the stranded lines on origin (`20d11d1a947`) in a different order, after
which local is no longer even a line-order superset -- aggravation, not cause.

**Content at risk:** 22 log lines present in local HEAD and absent from origin (0 lines the other way).
They are also in the coordinator spool (`GET /igw_log/pending`: 907 rows, 825 `client_git_write=true`).

**Why the "end state" is not available today:** flipping `igw_log_suppress_git_write` needs the hub's
`ree-assembly-git-writer` timer. It is **not installed on the hub** (`systemctl list-unit-files`: only
`ree-task-claim-chip-git-writer`, shadow-sync, live-status, sync-repair, backup). The 907-row spool has
never been drained by a writer. Arming the flag now would black-hole every log line.

## 3. What g8 and g9 shipped, and whether each held

| Referral | Marked done because | Landed | Deployed on Mac | Seed it removed | Held |
|---|---|---|---|---|---|
| g8 `...learning-route-g8` | a **decision** (route + converge once); fix came via child chip `...igw-tick-remote-tip-decision` | REE_Working `b4a44af59` -- IGW tick lands via `--to-remote-tip`, CAS `noop`, timeout rescue ref. Earlier same week: `08fabdb21`, `8b5d0ac53` (workset regen) | yes (ancestor of local HEAD; on-disk line 931 emits the flags) | stale-base CAS batch re-landing origin's own bytes | for that seed: yes. Wedge recurred in ~7 h via a new seed |
| g9 `...g9-learning-route` | a **decision** (accept doc, spawn follow-up `...g9-post-fix-strand`) | REE_Working `25dc09539` -- `_append_extension` + `verify_cherry_pick_faithful`, 10 tests; 6 strands landed `a464ad1b37b..981e4d09d18` | yes | log committed twice per run -> EOF superset conflict | for that seed: yes. Recurred in 2.4 d via a new seed |
| g10 (this) | -- | nothing yet | -- | seed = transient fetch ref-lock race | -- |

"Fix on origin but not running on the Mac" was checked and is **not** the explanation: the umbrella's
merge-base is only ~10 h old and no fix commit is missing from local HEAD.

Staged-but-never-built from g8: F-B (origin-tip identity guard in `ree_commit`'s default path). Inter-wedge
gaps g1..g10: 7.1 d, 10.9 h, 2.7 h, 7.0 h, 1.2 h, 4.3 d, 24.1 h, 7.3 h, 2.4 d. The 2026-08-26 investigation
already predicted a stable floor (~2.8 episodes per 1000 origin commits) and that per-seed fixes cut cost,
not rate; measured on `chip-20260910-merge-refwedge-class`: "ahead-count -36%, rate ~unchanged".

## 4. Writers that authored the unproven commits, g8 / g9 / g10 / cloud-5 g3

| Episode | Unproven-commit writer | File | Seed |
|---|---|---|---|
| g8 | IGW tick, ledger/assignments CAS batch | `igw_routine_ledger.json`, `igw_assignments.json` | stale-base duplicate of origin's bytes |
| g9 | IGW tick, log | `igw_routine_log.md` | double commit per run under remote-tip |
| g10 | IGW tick, log | `igw_routine_log.md` | fetch ref-lock race -> immediate fallback |
| cloud-5 g3 | budget tick (1) + healer handoff verbs (7) | `metaworker_dispatch_budget_log.json`, `TASK_CHIPS.json` | two ticks 8 s apart during an origin advance |
| Mac umbrella (live) | `chips archive/strip`, WS rotation, reaper close | `TASK_CHIPS.json`, `WORKSPACE_STATE.md`, `TASK_CLAIMS.json` | not traced |

Lit-pull / regen / human sessions: present in the ahead ranges every time, **always proven** (push-retry
twins). They are not a cause.

## 5. LIT-0805 / MECH-064 -- not actually in the discard set

`LIT-0805` is in local HEAD only because **origin removed it**, not because an ahead commit added it:
`git log origin/master..HEAD -S'"LIT-0805"'` on the proposals files returns nothing. It existed at the
merge-base `e561d95a375`; origin's regen `75ac3af3984` (07:23:50Z) dropped it 55 min after the MECH-064
lit-pull landed on origin (`94286de2a93`, byte-identical to local `55dad3fc30a`). Proposals are fully
re-derived each regen by `build_experiment_indexes.py` (`_ProposalIdAllocator` keeps ids stable; the item
set is derived). A `literature_review` placeholder whose literature has landed is removed by design; the same
regen rewrote `EXP-0804.why_now` from `missing_literature_evidence` to `lit_only_above_cap`. Nothing
hand-authored lives on that row. The Healer's ambiguity came from diffing HEAD-vs-origin *trees* rather
than per-commit content. **Recommendation: treat as resolved -- adopting origin is the correct state.**

The real land-vs-discard question is the 22 log lines (section 2). Put to the user as decision chip D1.

## 6. Proposed fixes

Ordered by leverage. F1 is a plain bug; F2-F5 change write semantics and are gated on D2.

- **F1 -- retry the transient fetch failure (plain bug).** `land_at_remote_tip`: on `fetch` rc != 0, sleep
  briefly and `continue` to the next of the existing 5 attempts; fall back only when attempts are exhausted.
  Failing test first (stub `git fetch` to fail once with the ref-lock text, assert no local landing and a
  successful remote-tip landing). User-facing semantics unchanged: the loop and its message already promise
  5 attempts. Removes the g10 seed. *Not landed in this session* -- /metaworker-learning Step 4 allows no
  "obviously safe" carve-out for `ree_commit.py`; it is folded into D2 as the minimum option.
- **F2 -- non-latching fallback (removes the latch for append-shaped writers).** New opt-in
  `ree_commit.py --no-local-fallback`: when remote-tip cannot land, pin the built commit under
  `refs/ree-rescue/<caller>/<sha>` (mechanism already exists: `_rescue_unreferenced_commit`), leave the
  branch ref alone, exit 1. Content stays on disk (the documented persistent-dirty trade) and the next tick
  retries from a base origin actually has, so `_append_extension` keeps applying. Adopt in
  `igw_routine_tick._ree_commit` for the log path and in `dispatch_budget_gate.py`. Deliberately NOT for
  `chip_ledger.py`: disk-differs-from-HEAD is the trigger of `_recover_orphaned_ledger_write`, whose
  misfire is still open.
- **F3 -- budget tick.** `dispatch_budget_gate.py`: `--to-remote-tip` (+F2) instead of
  `--retry-push-on-reject`; add `metaworker_dispatch_budget_log.json` (keyed by event id) to
  `REGISTRY_SPECS` and `RECONCILABLE` so an already-stranded tick is adjudicable. This is a keyed
  structural proof, not the closed heuristic reverse-apply route (Closed on measurement item 4 untouched).
- **F4 -- handoff verbs get a coordinator transport.** `/chip/handoff` (declare/verify) and a
  `handoff_pending` field on `/chip/resolve`, written into `entry_json`; then these verbs follow the same
  verified-ack-then-suppress pattern as the rest. Ledger write-semantics change -> ree-v3 `coordinator/`
  (single-session scope; integration branch not needed) + hub deploy. Until it lands, F5.
- **F5 -- interim skill text** (`metaworker-repair` Step 4b rule 3, both skill dirs): "If
  `ref_convergence.py --repo REE_Working --check` reports WEDGED on the box you are on, do not run
  `--handoff-pending` / `declare-handoff` there; resolve plainly (suppressed) and put the hand-off text in
  `--note`, prefixed `HANDOFF:`." Cost: the handoff-staleness tracker does not see those chips until F4.
- **F6 -- end state for the log (follow-on, not now):** deploy `ree_assembly_git_writer` on the hub, drain
  the 907-row spool, soak, then flip `igw_log_suppress_git_write`. Removes the last client-side IGW writer.
  Hub infra -> belongs to the orchestrator lane; chip only after D2.
- **Not proposed:** automatic `--adopt`. The 2026-08-19 decision wired `reconcile --check` only and declined
  gated `--adopt` "before (b) has run and its verdicts checked against human calls". That check has never
  been done; it is a precondition for revisiting, and g10 shows the unproven set is often genuinely
  unlanded content, where auto-adopt would be auto-loss.

## 7. GOV-HELDOUT-1 check (F5 is the only standing-text change)

Cases where old and new wording give different calls, not used to write the rule:

1. `13884d506` + 3x `declare-handoff` on `chip-checkoutdiverged-ree-cloud-5-...-g2` (00:46-01:52Z): old ->
   4 stranded commits; new -> 0. New is right.
2. `3e2fc946f` -- ree-cloud-5 healer resolving the **Mac's** wedge-audit chip: old -> strands on cloud-5;
   new -> suppressed. New is right.
3. `chip-refwedge-ree-cloud-5-ree-working-master-g2` (2026-09-02, 16 ahead): resolution note archived/stripped;
   cannot confirm handoff verbs were the writer. **Not countable.**

Result: **2 countable cases, both from the same 9-hour episode as the motivating incident.** That is the
finding: F5 is scoped to its incident. It is therefore proposed only as a narrow, explicitly interim rule
conditioned on a machine-checkable predicate (`--check` says WEDGED), to be deleted when F4 lands -- not as
a general rule. Cost of the check: ~10 min; it caught over-breadth (an unconditional "never use handoff
verbs on a cloud box" draft was dropped).

F1-F4 are code with tests, not standing text; their held-out evidence is section 4's table: F2 gives a
different (non-wedging) outcome on g9, g10 and cloud-5 g3's budget seed, none of which it was designed from
except g10.

## 8. Decision chips

- **D1 `chip-20260919-refwedge-g10-igwlog-lines-land-vs-discard`** -- LIT-0805 resolved as a non-issue; the
  22 `igw_routine_log.md` lines: land first then adopt (recommended), adopt and accept the loss (lines remain
  in the coordinator spool), or hold.
- **D2 `chip-20260919-refwedge-latch-removal-build-decision`** -- proceed F1-F5 (recommended) / constrain to
  F1+F3 / hold.
