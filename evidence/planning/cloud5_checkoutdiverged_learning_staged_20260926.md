# ree-cloud-5 checkout divergence: the recurrence was apparent, not genuine (metaworker-learning)

**Status: AWAITING USER REVIEW**

- **Session:** `mwlearn-20260926-1044`, 2026-09-26.
- **Chip:** `chip-20260924-learning-cloud5-checkoutdiverged-rootcause-v2`.
- **Decision of record:** `chip-20260924-decision-checkoutdiverged-cloud5-puller-recurrence-learning-route`, option (a).
- **Prior work on this class:** `checkoutdiverged_class_rootcause_20260902.md` (R1-R5, all built), `checkoutdiverged_automated_exit_20260907.md` and `checkoutdiverged_r5_divergence_scope_20260907.md`. The fixes F1-F5 landed in umbrella `24b2325e3` on 2026-09-19.
- **Box inspection:** read-only ssh on 2026-09-26 around 10:50Z. Nothing was restarted and no ref was moved.

## 1. Headline: the premise is false for the incidents that triggered this pass

The chip counted four occurrences on REE_Working and three on REE_assembly. The three most recent do not show the puller failing:

- 2026-09-24, REE_Working 3 behind / 0 ahead.
- 2026-09-24, REE_assembly 9 behind / 0 ahead.
- 2026-09-25T23:04, REE_assembly 1 behind / 0 ahead.

In each case the Healer ran `fetch` and `rev-list --count` at a moment between two successful puller runs. It then treated ordinary inter-poll lag as an occurrence. **The defect is in how the Healer classifies what it sees, not in the puller.**

### Evidence from the box's own logs

- **2026-09-24, REE_Working 3/0 (Healer around 03:57Z).** `ree-metaworker-autosync` logged "adopted origin/master, ok" at 03:08, 03:18, 03:29, 03:40 and 03:50. The checkout was three commits into a normal 10-minute window.
- **2026-09-24, REE_assembly 9/0.** `ree-git-sync-repair` logged `OK (ahead=0 behind=0)` at 03:39, then `SYNCED (was behind 6)` at 04:11. REE_assembly's puller runs every **30 minutes**, not 10. The chip got both the period and the repo wrong.
- **2026-09-25T23:04, REE_assembly 1/0.** sync-repair logged `SYNCED (was behind 9)` at 22:44 and `SYNCED (was behind 1)` at 23:15. Every run from 19:08 to 00:48 was SYNCED, with between 2 and 10 commits behind per run. That is REE_assembly's normal advance rate.
- **The hygiene tick** is `ree-hygienetick.service`, which runs locally on the box every 900s. It took 211 `checkout_divergence` readings after 2026-09-23T18:00. Every one was `scan_ok: True, stuck: 0`. The state file now holds `entries: {}`.

### The Healer contradicts itself on this same shape

- 09-24T11:01 on cloud-4: it called 1/0, 7/0 and 3/0 "ordinary lag".
- 09-26T09:08 on cloud-5: it called 2/0 "normal cadence, not a stuck puller".
- 09-25T23:09 on cloud-5: it called 1/0 the "3rd occurrence".

The skill gives it no criterion to decide by, so it decides by prose judgement.

## 2. The genuine occurrences, all already cleared, with different root causes

| Window | Repo | Cause | Status |
|---|---|---|---|
| 2026-08-29 (g1) | REE_Working | 08-28 cutover removed the write traffic that incidentally kept checkouts fresh (D1) | R4 fixed it: sync-repair on all boxes |
| 2026-09-18T23:16 to 09-20T03:55 (g2/g3) | REE_Working | Local dispatch-budget-tick commits put the box *ahead*; autosync correctly REFUSED | F1-F5 fixed it. Since then: 852 "ok" verdicts, 0 REFUSED, 0 `refs/ree-rescue` refs |
| 2026-09-19T07:38 to 09-20T07:30 (about 24h) | REE_assembly | `BEHIND_NOT_SYNCED -- ff blocked by uncommitted tracked change(s)`: derived-index files (`INDEX.md`, `claim_evidence.v1.json`, ...) left dirty in the box's shared checkout | Cleared. **The producer is still unidentified** (section 5, Q1) |

**The fixes held.** F1-F5 is an ancestor of HEAD on the box, and the budget gate carries `--no-local-fallback`.

No two of these share a root cause. **Under this skill's Step 1 test, the puller-recurrence class does not have two genuine occurrences of the same cause.** So no puller fix is warranted.

## 3. What does recur: the Healer's occurrence counting

The Healer miscounted three times from the same cause, a point-in-time "behind" count read as "not advancing": 09-24 REE_Working, 09-24 REE_assembly and 09-25T23:04 REE_assembly. That misclassification then produced this chip and its decision chip. That is a genuine recurrence (threshold 2), and it is what this pass fixes.

The cause is in `.claude/skills/metaworker-repair/SKILL.md` Step 3, in the table row "Checkout has stopped FOLLOWING origin (behind, not advancing)" (line 205). The tool it names is `fetch` + `rev-list --left-right --count`, which measures *behind*. It never measures *not advancing*. The row's own title asks a question its tool cannot answer.

## 4. Proposed fix

**A1. Add a read-only `--divergence-status` flag to `scripts/hygiene_routine_tick.py`.**

- It prints `_divergence_findings(dry_run=True)`'s per-repo state from `logs/hygiene_checkout_divergence_state.json`: the recorded origin sha, `first_seen_at`, `stuck_hours`, `_divergence_threshold_hours(repo)`, and a verdict `following` / `lagging (<N>h of <T>h)` / `stuck`.
- It writes nothing, does not commit, and does not fetch.
- It reuses the detector rather than re-deriving it.
- Tests follow `test_hygiene_routine_tick.py`'s injected-state pattern:
  - a state entry older than the threshold, with origin sha not reached, must print `stuck`;
  - one younger than the threshold must print `lagging`;
  - a reached sha must print `following`;
  - an absent or unreadable state file prints `cannot-determine`, not `following`. This is the negative-instruments rule.

**A2. Skill text: `metaworker-repair/SKILL.md` row 205, the `chip-checkoutdiverged-*` bullet (around line 657), and the mirror in `.agents/skills/metaworker-repair/SKILL.md`.**

- The row's tool becomes `hygiene_routine_tick.py --divergence-status` run on the box, with `fetch`/`rev-list` kept only to size the gap.
- Rule text: *a behind count alone is inter-poll lag, not an occurrence.* Count "stopped following", or a recurrence for learning-chip or amend purposes, only when one of these holds:
  - the detector says `stuck`; or
  - two samples at least one puller period apart show HEAD not advancing while origin did.
- The puller periods are 10 minutes for autosync on REE_Working and 30 minutes for sync-repair on REE_assembly and ree-v3.
- Fast-forwarding lag is still allowed and zero-risk. It is logged as "inter-poll lag" and never used to amend a learning chip.
- Persistence comes from the reached-sha clock. A puller's log verdict is only supplementary: held-out case H4 shows sync-repair once logged "OK" while syncing nothing.

**Explicitly not proposed:**

- **No change to the puller, units or scripts on the box.** Nothing there failed.
- **No dirt exemption in sync-repair** for the 09-19 REE_assembly block. The incoming commits touch those same files, so ff-only would refuse anyway, and discarding dirt is a new judgement call. The fix belongs at whichever producer ran a regen in the shared checkout without committing, which the Narrow Edits rule already forbids.

## 5. Held-out check (GOV-HELDOUT-1)

None of these cases are the motivating incidents.

| # | Case | Old (point-in-time count) | New (persistence) | Correct? |
|---|---|---|---|---|
| H1 | cloud-4 Healer, 2026-09-24T11:01: REE_Working 1/0, REE_assembly 7/0, ree-v3 3/0 | 3 occurrences | lag | New is right: that Healer judged it lag and no chip followed |
| H2 | cloud-5 Healer, 2026-09-26T09:08: REE_Working 2/0 | occurrence #5 | lag (autosync had run 8 minutes earlier, per the log) | New is right |
| H3 | cloud-4 Healer, 2026-09-20T04:51: REE_Working 2/0, fast-forwarded | occurrence | lag | New is right on the classification; the fast-forward was harmless either way |
| H4 | `chip-20260819-gitsyncrepair-reports-ok-while-not-syncing`: puller logged "OK (behind=N)" while not syncing | occurrence | puller-verdict variant says "following" (**wrong**); reached-sha variant says `stuck` (right) | **Caught an over-broad first draft.** It is why A2 makes the reached-sha clock primary |
| C | cloud-5 REE_assembly, 09-19T07:38 to 09-20T07:30 | occurrence | occurrence (24h stuck) | Degenerate control: both versions fire, as they should |

**Result:** passes on 3 non-degenerate cases (H1-H3). H4 caught an over-broad candidate. One caveat: H1-H3 are all Healer notes, so they test the classification rule, not an automated detector.

**Cost counterweight:** a new CLI flag plus tests, and a skill edit mirrored to two directories. It is small, but it adds one step to every Healer divergence triage.

## 6. Open questions (not built here)

1. Which process left derived-index dirt in cloud-5's REE_assembly checkout around 2026-09-19 07:10-07:38Z? It is not established. Candidate: an indexer or governance regen run on the box.
2. While the umbrella checkout was wedged (402 behind), the hygiene tick read a stale local `TASK_CHIPS.json`, logged "already recorded", and so suppressed a g2 for the 24h REE_assembly block. Should episodic re-minting read the ledger through the coordinator? This is a separate detection gap and a candidate for its own chip.
3. What should happen to this chip? Recommendation: resolve `done` once A1/A2 are decided, with the note "premise false: puller did not fail at 09-24/09-25; recurrence was classifier miscounting; fix A1/A2".
