# DLAPTOP umbrella wedge: route C bootstrap adoption, 2026-08-18

**Status: COMPLETED OPERATION RECORD. Nothing here awaits user action.** No registry
was edited beyond the recovery commits named below, all of which are on
`REE_Working` `origin/master`.

Session `metaworker-chip-20260818-adopt-origin-to-deploy-route-c`
(chip `chip-20260818-adopt-origin-to-deploy-route-c`).

## The bootstrap deadlock

`chip-20260818-dispatch-registry-commit-rate-wedges-umbrella` shipped ROUTE C in
`scripts/ref_convergence.py` (`REE_Working` `b5cb4153`), which moves the unit of proof
from the COMMIT to the RANGE, comparing parsed items of allowlisted whole-file JSON
registries by declared unique key. It was on `origin/master` and **not deployed on
DLAPTOP**, because a wedged checkout is by definition one that has not adopted origin.
The wedge blocked deployment of its own remedy.

Measured at session start (2026-08-18T08:2xZ):

| probe | result |
|---|---|
| `git show origin/master:scripts/ref_convergence.py \| grep -c 'route C'` | 15 |
| `grep -c 'route C' scripts/ref_convergence.py` | **0** |
| `ref_convergence.py --check` | **WEDGED** (ahead 36, 18 unproven, 0.7h, 18 refusals) |

## Per-commit content audit -- 9 of 18 unproven were GENUINELY STRANDED (50%)

Every unproven commit was audited by CONTENT against `origin/master`, never by file
shape: `TASK_CLAIMS.json` by `(session_id, claimed_at)`, `TASK_CHIPS.json` by
`chip_ref`, `RECOMMENDATION_LOG.jsonl` by added-line set, always via
`git show <sha>^:<path>` / `git show <sha>:<path>`.

| verdict | n | meaning |
|---|---|---|
| UPSTREAM | 5 | keyed entry byte-identical on origin |
| SUPERSEDED | 2 | origin holds a strictly LATER state of the same entry (identity fields identical, `active` -> `done`) |
| PRUNE-ONLY | 2 | removals of `done` entries origin still carries; idempotent housekeeping, re-prunable |
| **STRANDED** | **9** | **content absent from origin -- landed, not discarded** |

**This contradicts the chip brief's expectation.** The brief predicted "MOST" would be
already-upstream, citing the root-cause audit's 13-of-18. The measured figure here is
9 of 18 stranded (50%), squarely in line with CLAUDE.md's "a refusal is roughly a coin
flip" and with the 2026-08-15 sample (15 of 33, 45%). **Recorded as sample (iv)**
alongside samples (i) 0-of-4, (ii) 15-of-33 and (iii) 3-of-10 in CLAUDE.md. A
shape-based argument ("it is just TASK_CHIPS/TASK_CLAIMS bookkeeping") would have
permanently dropped all 9.

### The 9 stranded commits, landed oldest-first onto origin

Cherry-picked with `-x` (so each carries a route-B backref) in a throwaway worktree,
rebased onto the moving tip, pushed as `REE_Working` `5042c448..8b5fa075`:

| sha | content recovered |
|---|---|
| `f431aaf508` `5f0b6106b1` `889327c576` `c42c68bd46` `3a386d8a88` `c8c84f4372` | 6 `RECOMMENDATION_LOG.jsonl` entries (937a direction, 937 scope, Routing, Category fix, Ledger legs, Stale routing). Origin had 126 lines, local 132. |
| `dea3f58bf4` | `cranky-driscoll-126a36` `completion_note` amendment + `completion_note_history` (origin held `null`) |
| `39ee48f49e` | **`governance-paused-bb6e76` -- an ACTIVE governance pause lock**, absent from origin entirely. A live session's coordination-plane lock was invisible to every consumer that reads origin. |
| `80ec1b3cda` | `chip-20260818-adopt-origin-to-deploy-route-c` `urgency: true` |

Two whole-file registry conflicts were resolved SEMANTICALLY (take target state, add
only this commit's keyed delta), never by whole-file overwrite; each resolution was
verified as a pure addition (16 added lines, 0 removed) before continuing. Pre-push
verification confirmed 0 origin entries dropped from `TASK_CLAIMS.json` (100 -> 101),
`TASK_CHIPS.json` (955 -> 955) or `RECOMMENDATION_LOG.jsonl` (126 -> 132).

## Adoption

`safe_adopt_ref.py` requires acknowledgement of EVERY ahead commit, not only the
unproven ones -- its independent recomputation stays the gate. Final list: 38 commits,
29 route-A/B-proven by `ref_convergence.py` plus the 9 audited above.

    master moved 3c8a95f857 -> e038f243e5 (adopted origin/master)

Post-move skew repair (automatic, via `ree_commit.check_head_worktree_skew`):
materialised 2 never-written files (`scripts/test_ref_convergence_route_c.py`,
`scripts/test_confirmer_verdict_behind_origin_push.py` -- staged DELETIONS) and
discarded 12 staged REVERTS. One residual `M ` on `TASK_CLAIMS.json` was left
unverified by the tool and repaired by hand per CLAUDE.md: worktree content matched
the pre-move base `3c8a95f857` exactly (stale adoption lag), and HEAD was confirmed a
strict superset (92 -> 102 entries, 0 would-be-lost) before `git checkout HEAD --`.

## Deadlock broken -- both STOP-CHECK probes

| probe | before | after |
|---|---|---|
| `grep -c 'route C' scripts/ref_convergence.py` | 0 | **15** |
| `ref_convergence.py --check` | WEDGED (ahead 36, 18 unproven), exit 4 | **`no refusal state; converging normally`, exit 0** |

Checkout ended `ahead 0`.

## Route C under live accumulation -- NOT yet observed, stated plainly

The chip asked whether unproven stays near 0 on the next accumulation. **This session
could not observe it.** The checkout was polled at ~20s intervals for 2 minutes after
adoption and stayed at `ahead 0` the whole time -- no new local commits accrued in the
window, so there was no fresh batch for route C to prove. The claim that route C keeps
unproven near 0 rests on the pre-existing 17->1 measurement in
`chip-20260818-dispatch-registry-commit-rate-wedges-umbrella`, not on anything measured
here. What IS established here is narrower and sufficient for the chip's purpose: the
route C code is now present and running on DLAPTOP, and the checkout converges.

Note the mechanism that made 6 of the 9 strandings possible is itself route-C-shaped:
`RECOMMENDATION_LOG.jsonl` is an append-only JSONL registry, and
`chip-20260818-routec-jsonl-recommendation-log` is already open against exactly that
gap.
