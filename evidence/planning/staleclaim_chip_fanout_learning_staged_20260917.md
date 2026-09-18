# Stale-claim chip fan-out: one session's claim family produces N review chips -- STAGED (not shipped)

**Status: APPROVED (option A) AND SHIPPED 2026-09-18.** User chose option A on the decision
chip. Landed `REE_Working` origin/master **d9d030a98** (verified on origin): `_stale_claim_siblings()`
plus the advisory sibling cross-reference in `_stale_claim_prompt`. Prompt text only -- `chip_ref`,
the mint cap and the `_hygiene_resolution` `(session_id, claimed_at)` join are untouched, so the
grouped-ref leak risk in section 4.2 was never taken. 6 tests added to `StaleClaimFindingsTest`
(including the H1 negative control and an ASCII-output guard); 728 pass in the file;
`run_scripts_tests.sh --changed` green from the main checkout.
The file lock noted below cleared at 2026-09-17T21:06 (their work landed as `394308564`).
Author: `/metaworker-learning` session `learning-20260917-staleclaim-fanout`, 2026-09-17T20:07:05Z.
Subject: `_stale_claim_findings` / `_stale_claim_chip_ref` / `_stale_claim_prompt` (mint side only).
Decision chip: see section 7.

**Contention note, stated up front:** `scripts/hygiene_routine_tick.py` is held right now by live
claim `pausepressure-g10-build-20260917` (opened 2026-09-17T19:39:17Z, "pause-pressure REC-1..4
build"). `task_claim.py check` returned NOT OWNER for this session. Nothing in this document has
been written to that file, and nothing may be until that claim closes. Their in-flight diff was
inspected and does **not** touch the stale-claim path (it is all
`_EPISODIC_REGENERATION_QUIET_HOURS` / `_record_episodic_finding` work; `chip-staleclaim-` is not
in `_EPISODIC_STANDING_PREFIXES`), so there is no design conflict -- only a file lock.

---

## 1. The problem class

CLAUDE.md's **Claim-first, edit-last** rule instructs a session that discovers a new resource
mid-task to open a **second claim entry under a distinct `session_id`**, because
`task_claim.py open` is idempotent per `--session-id` and "has no in-place broaden". The
documented pattern (`inter-governance-brief` SKILL.md Step 1d) produces id families like
`usage-suggestions-plan-f328a0`, `...-design`, `...-impl`, `...-flatfix`.

When such a session goes stale, `_stale_claim_findings` loops `for rec in records` and mints
**one chip per claim record**. The family therefore produces N "Review stale claim" chips, each a
separately clickable dispatch suggestion, which in practice receive **one** adjudication.

The detection is correct -- every one of those claims really is stale. The redundancy is in
**dispatch**, not in detection. That distinction drives the whole design below.

## 2. Measured occurrences (Step 1 -- same root cause, not same symptom)

Corpus: all 137 `chip-staleclaim-*` chips in `TASK_CHIPS.json`, spawn range 2026-08-03 ->
2026-09-17, all `origin: hygiene_tick`.

- **104 families, 33 redundant chips (24.1%)**; 19 multi-chip families.
- Of the 33: **23 are this fan-out** (one session, sibling-suffixed ids) and **10 are a separate
  defect** (same `session_id` re-chipped at a later `claimed_at`; different `chip_ref`, so ledger
  dedupe never collides). The second defect is **out of scope here** and is named in section 6.

Confirmed occurrences of THIS root cause, with the evidence that one adjudication served all N:

| date | family | chips | evidence |
|---|---|---|---|
| 2026-08-20 | `usage-suggestions-plan-f328a0` (+`-design -impl -igwfix -d3 -precheck -backfill2 -flatfix`) | 8 | 8 distinct `claimed_by` session UUIDs |
| 2026-08-22 | `elated-jackson-f12eae` (+`-docs -flaginert`) | 3 | 3 distinct `claimed_by` session UUIDs |
| 2026-09-01 | `metaworker-chip-20260830-ctxmem-...-portfolio` (`-exq-969 -exq-970`) | 2 | 2 distinct `claimed_by` |
| 2026-09-03 | `metaworker-chip-proposal-exp-0853` (+`-experiments-dir -exq-979`) | 3 | resolution note **character-for-character identical** across all 3 |
| 2026-09-10 | (manual merge pass) | 3 | `chip-20260910-merge-staleclaim-triage`, merge criterion "(d) N instances of one procedure ... One session, three determinations" |
| 2026-09-11 | `codex-showcase-build-20260911` (+`-exq1021`) | 2 | resolution note identical verbatim |
| 2026-09-16 | `science-batch4-20260915` (+`-exq-1046`) | 2 | (adjudications DIFFERED -- see 5.2) |

Seven occurrences against a default threshold of 2. The 0853 note states the grouping explicitly:

> "Bucket U resolved: work LANDED. **All three metaworker-chip-proposal-exp-0853\* claims belong
> to one session**; closed 2026-09-03 with closed_at=2026-09-02T18:51:43Z ..."

**Not already fixed.** Redundant share 28.8% (Aug) vs 18.8% (Sept) -- a decline tracking lower
total volume, not a fix. Most recent redundant family: **2026-09-16**, the day before this doc.

## 3. Was per-claim deliberate? (the question that could have closed this)

**No argued decision exists.** The only statement is an undefended assertion in the module
docstring (`hygiene_routine_tick.py:36`): *"this tick calls it, then chips whatever remains
(S/D/B/U/C), one chip per claim"*. No test pins per-claim granularity.

Three prior `chip-staleclaim-` fixes exist and **none** is this root cause -- they must not be
counted as prior attempts at it:

- **2026-08-29 `...-false-remediation-bucket-u`** -- *resolution* side: removed the prefix from
  `_HYGIENE_ABSENCE_DONE_PREFIXES` because absence from one tick's findings was not a sufficient
  done-signal. (Confirmed permanent leak.)
- **2026-08-29 `...-absent-path-stale-file-gap`** -- *resolution* side: a lagging working-tree
  `TASK_CLAIMS.json` let a current box's chip resolve `done` on a stale box; fixed by re-checking
  origin.
- **2026-08-30 detector-FP campaign class 3** -- *temporal* duplication of ONE claim (Orchestrator
  lease C<->D bucket flapping), fixed by hoisting bucket L.

Counter-evidence that grouping is the house idiom, from the same file and the sister skill:
`:3116` *"Grouped by ref so N copies produce ONE chip"*; `:6444` *"One chip per session"*; and
`/metaworker-repair` SKILL.md:526 already places `chip-staleclaim-` in the **"Gather (delay is
safe)"** set. Doctrine already says gather; the producer simply never did.

## 4. What the obvious fix would break (and why it is rejected)

The intuitive fix -- **one chip per session, grouped `chip_ref`** -- is unsafe. Three blockers:

1. **It breaks the resolution join.** `_hygiene_resolution`'s bespoke staleclaim branch recovers
   `(session_id, claimed_at)` via `_staleclaim_session_from_prompt` and matches **one exact claim
   by BOTH fields**, refusing to resolve while `status == "active"`. CLAUDE.md is explicit that
   *"The claim key is `(session_id, claimed_at)`"*. A grouped chip needs all-of-N partial-remedy
   semantics that do not exist today.
2. **It can create a silent permanent leak.** `chip_ledger.cmd_record` dedups on `chip_ref`
   **unconditionally and status-blind** for a task_id-less producer -- *"once wrongly resolved, the
   minting pass can never re-raise the same finding."* A grouped ref chipped once could never
   re-raise when a NEW claim joins that session. That is strictly worse than the redundancy it
   cures, and it is the same failure family as the confirmed 2026-08-29 leak.
3. **The siblings do not share a `session_id` at all.** Because CLAUDE.md mandates a *distinct id*
   per extra claim, `-experiments-dir` / `-exq-979` / `-flatfix` are genuinely different session
   ids. There is no existing key that could collapse them; any grouping is a **heuristic over id
   shape**, and a wrong heuristic merge in a *ref* is unrecoverable.

## 5. Proposed fix (minimal), and the held-out check that shaped it

### 5.1 The change

Keep **one chip per claim, chip_ref unchanged, resolution path untouched.** Add to
`_stale_claim_prompt` only: a **sibling cross-reference** listing the other stale claims detected
in the same tick that belong to the same family, with an instruction to adjudicate them together
and resolve each sibling `chip_ref`.

Sibling predicate, deliberately narrow: **B is a sibling of A only when B == `A-<suffix>` and A's
full `session_id` is ITSELF a stale claim record in the same tick.**

This is advisory prompt text. It cannot mis-resolve a chip, cannot suppress a future finding, and
cannot break the composite-key join, because it changes no key and no status logic.

### 5.2 Held-out check (GOV-HELDOUT-1)

Rule tested against 4 families it was NOT written from (it was written from f328a0, 0853,
codex-showcase). Non-degeneracy: in each, old and new behaviour differ.

| # | held-out case | old | new | right call? |
|---|---|---|---|---|
| H1 | `metaworker-chip-20260819-{hygienetick-wire-fleet-stash-sweep, batch-the-worktree-gc, runscriptstests-symlink-false-positive, e3-last-scores-prearbitration-staleness}` | 4 chips | **naive stem rule MERGES all 4 -- WRONG**, these are 4 different tasks from one dispatch batch | **CAUGHT AN OVER-BROAD RULE.** No claim `metaworker-chip-20260819` exists -> narrowed predicate correctly declines to merge |
| H2 | `science-batch4-20260915` + `-exq-1046` | 2 chips | cross-reference added; base exists so they ARE flagged siblings | **Partially wrong but harmless.** Their adjudications genuinely differed (base `withdrawn` as superseded by `account-handover-20260916`; sibling auto-`done`). Advisory text costs a glance; a forced ref-merge would have produced a wrong single outcome. **This case is the argument for advisory-over-merge.** |
| H3 | `daily-20260903-exq997-mech162` + `-exq-997` | 2 chips | cross-reference added | **Right but worthless.** Both auto-resolved (`-- remedied`); no session was ever dispatched, so the fix saves nothing here. Caps the benefit. |
| H4 | `elated-jackson-f12eae` + `-docs` + `-flaginert` | 3 chips, **3 distinct sessions dispatched** | 1 session adjudicates 3 | **Right, and this is the real win.** |

**Outcome: the check CAUGHT AN OVER-BROAD RULE** (H1) and forced the narrowing in 5.1; H2 forced
advisory-cross-reference over forced-merge. Recorded per CLAUDE.md as the claim's admissible
evidence.

### 5.3 Honest counterweight

- The headline "33 redundant chips" **overstates the harm**. Only **11 redundant sessions** are
  provably dispatched (4 of 19 multi-chip families show >1 distinct `claimed_by`). 58 of 137
  staleclaim chips auto-resolve at zero human cost (H3).
- So the realistic saving is **order 11 sessions over 6 weeks (~2/week)**, not 33.
- The fix is advisory text: an adjudicator may ignore it, so realized saving will be lower still.
- Held-out validation cost real cycles here and is not free; it is also what stopped H1 shipping.

A reasonable reviewer could conclude ~2 sessions/week does not justify touching a path with a
confirmed permanent-leak history. **That is a legitimate HOLD, and is offered as an option.**

## 6. Explicitly out of scope

- The **same-id re-spawn** defect (10 chips: `insights-7fd98a` x4, `orchestrate-20260828-1940` x3,
  `cool-sutherland-9d984d` x2, ...). Different root cause (a later `claimed_at` yields a new
  `chip_ref`, so dedupe never fires). Not designed for here; chip separately if wanted.
- Anything on the resolution side. Untouched by design.
- `scripts/hygiene_routine_tick.py` edits of any kind while `pausepressure-g10-build-20260917`
  holds the file.

## 7. Decision required

Options put to the user in the decision chip:

- **A. Proceed (minimal)** -- ship 5.1 as specified: prompt-only sibling cross-reference, narrowed
  predicate, per-claim refs and resolution untouched. Tests added alongside
  `StaleClaimFindingsTest` using that class's injected-data pattern (monkeypatched
  `audit_stale_claims.audit`, no real git repo). Must wait for the file lock to clear.
- **B. Constrain** -- ship 5.1 but ALSO require the sibling list be capped (e.g. name at most 5
  siblings + a count) to bound prompt growth on a family like f328a0's 8.
- **C. Hold** -- do nothing; ~2 sessions/week is under the bar for touching this path. Record the
  finding in the doc only.
- **D. Wider** -- also fix the same-id re-spawn defect in section 6 (larger, touches the ref
  scheme, and re-opens the leak risk in 4.2).

Recommendation: **A**, on the grounds that it is prompt-text-only and provably cannot reach the
resolution machinery -- with **C** a defensible call on cost.
