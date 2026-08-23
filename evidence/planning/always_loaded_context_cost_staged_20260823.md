# Always-Loaded Context Cost -- measurement

Status: AWAITING USER REVIEW

Measured 2026-08-23T11:26:12Z, session `elated-jackson-f12eae` (Mac, `DLAPTOP`).
**Measurement only. Nothing was restructured; no rule, skill, or file was edited.**
Recommendations below are recommendations, not applied changes.

Populations measured:
- **2,697** headless `claude -p` (`entrypoint=sdk-cli`) sessions on `ree-cloud-5`, the
  metaworker box (`~/.claude/projects`, 696 project dirs, 1.2 GB, 4,207 transcript files).
- **1,290** interactive sessions on the Mac (`claude-desktop`), as a cross-check.
- **375** direct measurements of the `metaworker-dispatch` SKILL.md load cost.
- This session's own turn-1 usage, as a same-day point check at current file sizes.

---

## Q1 -- Do fresh `claude -p` sessions get prompt-cache hits on these files?

**No. Not at any rate, and not under any timing condition.**

### The headline numbers (n=2,697 headless sessions, `ree-cloud-5`)

| turn-1 quantity | median | p90 |
|---|---|---|
| total prompt tokens | 111,342 | 127,016 |
| `cache_read_input_tokens` | 24,424 | 24,424 |
| `cache_creation_input_tokens` | **86,879** | -- |
| cache-hit ratio | **19.2%** | 23.5% |

100% of sessions get *some* cache read, which is why a naive "is the cache working?"
check reads as a pass. It is not. The ~24k that is read is a **fixed harness prefix**
(system prompt + tool definitions), and the ~87k that is CLAUDE.md is written fresh
every single session at cache-**write** price.

### Proof that the cached part is not the repo files

`cache_read` is a **quantised constant** and is completely independent of how recently
another session started on the same box:

| gap to previous session on same box | n | median `cache_read` | median hit% |
|---|---|---|---|
| < 60 s | 357 | 24,424 | 19.2% |
| 1-5 min | 746 | 16,016 | 18.8% |
| 5-60 min | 1,574 | 24,424 | 20.4% |
| 1-6 h | 11 | 16,016 | 18.9% |
| > 6 h | 9 | 16,016 | 21.2% |

Sessions launched **less than a minute apart** get exactly the same cache read as
sessions **six hours apart**. Across all 2,697 sessions `cache_read` takes only a
handful of distinct values (p0 15,273 / p25 16,016 / p50 24,424 / p99 30,231) -- the
signature of a fixed prefix under a few harness configurations, not of content-dependent
reuse. If CLAUDE.md were entering the shared cache, the `<60s` bucket would separate
from the `>6h` bucket. It does not.

### Same-day point check -- this session's own first turn

At the current CLAUDE.md (244,947 B):

```
turn 1: cache_create=124,450  cache_read= 34,538  TOTAL_PROMPT=158,990  hit=21.7%
turn 3: cache_create=    444  cache_read=158,988  TOTAL_PROMPT=159,434  hit=99.7%
```

Within a session the cache works essentially perfectly (99.7% from turn 3). Across
sessions it does not work at all for this content. **Every new session re-pays the floor.**

### Cross-check: interactive Mac sessions

n=1,290, median turn-1 prompt 120,516, median hit ratio **27.6%** -- same regime, slightly
better only because the interactive harness prefix is larger.

### Consequence for the question you posed

The `~59M tokens/day` branch is the correct one; `~6M` is refuted.
**The lever is cadence (and file size), not worker count.**

---

## Q1b -- Two corrections to the premise

**(a) The floor is larger than ~117k, and it is not the same for every session.**

Measured, `ree-cloud-5`:

| session kind | n | turn-1 `cache_create` | SKILL.md load | **floor per session** |
|---|---|---|---|---|
| dispatcher tick (cwd `~/REE_Working`) | 2,032 | 102,412 | +78,918 | **181,330** |
| chip worker (cwd `.../worktrees/...`) | 665 | 102,412 | not loaded | **102,412** |

**(b) `metaworker-dispatch/SKILL.md` is NOT paid by every session.** Of 250 worker
sessions scanned, **zero** loaded it; only 38 (15%) loaded any skill at all
(`queue-experiment` 19, `session-land` 16, `lit-pull` 4, `implement-substrate` 1).
The 222 KB SKILL.md is a **dispatcher-tick cost only** -- but on that tick it is
+78,918 tokens (n=375, mean 73,757, range 35,113-86,018), which makes the dispatcher
floor **181,330**, over 50% larger than the ~117k assumed.

The skill loads on turn 3, as a clean second cache-write step:

```
turn  1 create 102,139 read  24,424 tot 126,563
turn  2 create 102,139 read  24,424 tot 126,563  Skill:metaworker-dispatch
turn  3 create  75,204 read 126,563 tot 201,767   <-- SKILL.md lands here
turn  5 create     225 read 201,767 tot 201,992
```

### Tokens per byte, measured rather than assumed

Two independent methods agree:

1. **Direct** -- SKILL.md is 221,890 B and its load costs a median 78,918 tokens
   => **2.81 chars/token** (n=375).
2. **Regression** -- CLAUDE.md grew 12 KB -> 245 KB between 2026-03 and 2026-08.
   Regressing first-turn prompt tokens on CLAUDE.md size at session time over 1,259
   sessions gives slope 0.378 tok/byte (**2.65 chars/token**), R2 = 0.854, intercept
   62,522 tokens for everything else.

Both are well below the usual ~4 chars/token for prose, because these files are dense
in backticked paths, script names, commit shas and IDs. Applying 2.81:
**CLAUDE.md ~= 87,200 tokens; SKILL.md ~= 78,900 tokens; combined ~= 166,100.**

---

## Q1c -- What it actually costs per day

Current state, worth noting: **the metaworker timer is `disabled` and `inactive` on both
`ree-cloud-4` and `ree-cloud-5` right now**, and no `claude` process is running on either.
The figures below are (i) the empirical cost when it was running, and (ii) the projection
at the configured 5-minute cadence.

Empirical, `ree-cloud-5`, median active day: 95 dispatcher ticks + 30 worker sessions.

| scenario | floor `cache_create` / day |
|---|---|
| empirical median active day (95 + 30) | **20.3 M** |
| busiest observed day (2026-08-22, 299 sessions) | ~48 M |
| 5-min timer, 288 ticks/day, no early exit | **55.3 M** |

This is the *floor only* -- the always-loaded prefix. It excludes all working context.
Whole-session totals on active days ran 1.5-4.2 **billion** raw prompt tokens/day, but
that is dominated by within-session `cache_read` (billed at 0.1x), which is the part that
is already working correctly and is not the target here.

So: the projection matches your ~59M estimate closely, and the empirical figure is
20M -- both an order of magnitude above the ~6M cached-case hypothesis.

---

## Q2 -- Operative rule vs incident archaeology

### Method, and its honest error bar

Blocks split at blank lines (fenced code kept intact), then classified three ways with
increasing aggressiveness, plus a hand-labelled validation set:

| method | CLAUDE.md archaeology | SKILL.md archaeology |
|---|---|---|
| v1, strict marker-only (lower bound) | 49.8% | 35.8% |
| v2, prose-aware (upper bound) | 79.6% | 77.9% |
| **hand-labelled, byte-weighted random sample (n=18)** | **67%** | -- |

The hand sample labelled 12/18 archaeology, 3 mixed, 3 operative. v2 agrees with the hand
labels 13/18 (72%); its errors are asymmetric -- 11/12 recall on archaeology but it
mislabels 2 of 3 genuinely operative blocks as archaeology, so **79.6% is an
over-estimate and 49.8% an under-estimate**.

**Best estimate: archaeology is ~2/3 of both files (95% CI on the n=18 sample is wide,
roughly 41-87%). Operative rule is ~12-17%.** The remainder is structural and mixed.

The v1 `NEUTRAL` bucket (21% of CLAUDE.md) turned out on inspection to be mostly design
rationale -- e.g. "`ree_commit.py` closes the gap structurally: each path is read from
disk exactly once..." -- which is archaeology, not instruction. That is the single
biggest reason the strict marker count understates.

### Where the mass actually is -- this is the actionable part

Concentration is extreme. **Four sections are 65% of CLAUDE.md:**

| bytes | ~tokens | arch% | section |
|---|---|---|---|
| 63,662 | 22,656 | 82% | Claim-first, edit-last |
| 48,210 | 17,157 | 73% | Session Startup Protocol |
| 26,313 | 9,364 | 86% | Housekeeping (every session close) |
| 19,930 | 7,093 | 98% | Running the test suite (route it to a cloud worker) |
| 11,056 | 3,935 | 73% | Worktree / Chipped Sessions |
| 7,535 | 2,681 | 81% | Workers may need waking |
| 7,418 | 2,640 | 82% | Coordinator (Phase 3) |
| 6,105 | 2,173 | 97% | General Rules |

**One section is 68% of the entire SKILL.md:**

| bytes | ~tokens | arch% | section |
|---|---|---|---|
| 150,257 | 53,472 | 79% | Step 4 -- `kind == "work"`: bounded auto-dispatch |
| 16,343 | 5,816 | 76% | Step 5 -- `kind == "decision"` |
| 15,261 | 5,431 | 87% | Step 1 -- Coordination-plane pause check |
| 9,501 | 3,381 | 81% | Use 2 -- the mid-task query |
| 7,226 | 2,572 | 77% | Step 3.5 -- source ready IGW workset items |

Recurring archaeology shapes, all of which have a stable operative core wrapped in a
much larger record: `Confirmed <date> ...` incident narrations, `Why the old idiom was
the bug`, `Scope history`, `Held-out check (GOV-HELDOUT-1)`, `Tests: scripts/test_*.py
(N, time-independent...)`, A/B timing tables, and per-fix root-cause explanations.

### What the floor would become

Holding memory/system prompt constant and shrinking only the two files:

| retained share | dispatcher floor | change | empirical/day | 5-min projection/day |
|---|---|---|---|---|
| today | 181,330 | -- | 20.3 M | 55.3 M |
| 33% retained (hand-calibrated) | **70,050** | **-61%** | 8.0 M | 21.5 M |
| 20% retained (v2) | 48,459 | -73% | 5.6 M | 14.9 M |

Worker sessions fall from 102,412 to roughly 44,000-58,000 on the same assumption.

---

## Recommendations (not applied)

1. **Attack cadence first.** It is the only lever that scales linearly against a floor
   that has zero cross-session reuse. A 5-min timer costs 288 x 181,330 = 55.3 M/day
   in floor alone; 15 min costs 18.4 M; 30 min costs 9.2 M. Worker count barely moves
   this number, because workers are 30/day against 95 dispatcher ticks and do not load
   the SKILL.md at all.

2. **Make the idle tick cheap before making it rarer.** The dominant waste is a tick
   that loads 181k tokens and then finds nothing to dispatch. A cheap pre-check --
   an exit *before* the `Skill` call when the ledger has no open work and no pause is
   held -- would cut a no-op tick from 181,330 to ~102,412 (-44%) with no change to
   either file and no behaviour change on a tick that does have work. This is the
   highest ratio of saving to risk of anything measured here.

3. **Split the four hot sections, not the whole file.** Four CLAUDE.md sections carry
   65% of it and one SKILL.md section carries 68%. Moving the archaeology out of just
   `Claim-first, edit-last` (22.7k tok, 82% archaeology) and `Step 4` (53.5k tok, 79%)
   recovers roughly 60k tokens per dispatcher tick -- about half the total available
   saving -- while leaving 39 other CLAUDE.md sections untouched.

4. **Keep the archaeology, move it.** Every incident record measured here documents a
   real confirmed failure, and several explicitly exist to stop a later session
   "simplifying" a rule back into a bug. The recommendation is a referenced file
   (e.g. `docs/architecture/coordination_plane_incidents.md`) linked from the operative
   rule, **not** deletion. The operative sentence and its pointer stay inline; the
   confirmation, mechanism, measurement table and held-out check move.

5. **Treat this as a standing-rule change when it is enacted.** Per General Rules, a
   rewrite of CLAUDE.md's rule text needs the GOV-HELDOUT-1 held-out check: at least 3
   historical cases where inlined-vs-referenced wording would give different calls.
   The `Scope history` blocks are the obvious corpus, and the risk to test is precisely
   whether a session that does not follow the reference makes the error the inline text
   was preventing.

### Open, not measured here

- Whether the harness re-reads CLAUDE.md per session or the platform cache TTL is the
  binding constraint. The data shows no reuse either way, but the two have different fixes.
- Whether `AGENTS.md` and the other 27 skills carry the same ratio.
- The 2026-08-19 `chip_ledger.py archive` precedent (strip fat fields, keep the row,
  origin-authoritative) is the closest existing pattern in this repo to what is proposed
  in (4) and is worth reading before designing the split.

---

# ADDENDUM -- 2026-08-23T14:38:47Z

Still AWAITING USER REVIEW. Added after user review of the body above raised three design
questions. Measuring them found **a material error in the body's own cost model**, corrected
first below. Same session, same populations, no file restructured.

## CORRECTION 1 -- the floor is re-read on EVERY turn, so it is ~57% of spend, not a one-time cost

The body treats the floor as a turn-1 `cache_create` charge (hence "20.3 M/day"). That is the
**write** only. The always-loaded content sits in the prompt prefix, so **every subsequent turn
re-reads it** as `cache_read`. Its true contribution is

    floor x (1.25 once, as cache_create)  +  floor x 0.10 x (every later turn, as cache_read)

Simulated on **real per-turn data, deduplicated by assistant message id**, over the 200 largest
dispatcher transcripts (median 47 real turns): shrinking the floor to 33% of its current size cuts
**total session cost by a median 57.4% (mean 57.2%; aggregate 279 M -> 121 M base-equivalent,
-56.6%)**, pricing `cache_create` at 1.25x and `cache_read` at 0.10x of base input.

So the "20.3 M/day floor" in the body is a **floor-write** figure and understates the true cost of
this content by roughly 5x. **Restructuring is a ~57% cut to total spend, not a ~12-20% one.**
Recommendations 3 and 4 in the body are correspondingly more valuable than stated there.

## CORRECTION 2 -- the no-op pre-exit (body recommendation 2) is NARROW, not the top item

The body calls the pre-`Skill` exit "the highest ratio of saving to risk of anything measured
here". Measured properly, it is not. Ticks are **not** idle:

| dispatcher ticks (n=2,032, unbiased) | share | share of dispatcher spend |
|---|---|---|
| <=4 turns (would benefit from a pre-exit) | 1.5% | ~0.0% |
| 5-9 turns | 0.0% | ~0.0% |
| 20+ turns | 92.3% | 98.3% |

And of the 150 largest dispatcher transcripts, **76% perform a dispatch/spawn action**, at a median
of 8 tool-calls per tick. (That sample is size-biased toward busy ticks; the table above is not.)

A tick that dispatches needs the skill, so a pre-exit cannot avoid loading it. The right lever is
that the SKILL.md costs roughly `98,648 (write) + 78,918 x 0.10 x 8 turns = ~162,000`
base-equivalent tokens **per tick regardless**, so **shrinking the file beats pre-exiting it**:
a 67% cut saves ~108,000 per tick on ~100% of ticks, where the pre-exit saves ~162,000 on the
~24% that do not dispatch. Keep the pre-exit -- it is cheap and correct -- but build it **after**
the file work, not first.

## FINDING 3 -- cost per turn is FLAT to 200+ turns, so long/persistent sessions are safe

There is no quadratic penalty from accumulating context; context management caps it.

| real turns | 17 | 205 |
|---|---|---|
| cache_read per turn | 89,522 | 189,284 (2.11x) |
| **base-equivalent cost per turn** | **21,759** | **22,344 (1.03x)** |

Cost per turn is flat at ~22,000-27,000 across the whole range (n=2,697). A session that stays
alive and does N units of work therefore pays the floor **write** once instead of N times, with no
growth penalty. Batching N items saves `(N-1) x 226,663` base-equivalent (the write at 1.25x); it
does **not** save the per-turn re-read, which is why it is worth less than shrinking the files.
Both are worth doing and they compose.

## FINDING 4 -- "already-done" is 17.7% of chips, and those sessions run FULL length

Two different populations, easily conflated:

- **Cheap no-ops** -- sessions exiting in <=9 turns: **2% of sessions, ~0% of spend.** Negligible.
  Fallback work for these would recover almost nothing.
- **Already-done discoveries** -- of 1,444 chips resolved `done`, **255 (17.7%)** have a
  resolution note saying the work was already landed, obsolete, or superseded. These do **not**
  exit early; they run a full session (~1.3 M base-equivalent) to reach that verdict.

So the preflight-triage chip's premise holds, but the mechanism is **earlier detection**, not
fallback work: the waste is a full-length investigation, not an idle session.

## FINDING 5 -- all-skills census (this closes an "open, not measured" item, cheaply)

29 files, 1,471,355 B = **523,614 tokens, 70% archaeology = 364,575 tokens recoverable.**
The ratio is **not** uniform -- large skills are archaeology-heavy, small ones are lean -- so the
fix targets a handful of files.

| ~tokens | arch% | recoverable | file |
|---|---|---|---|
| 87,170 | 79% | 69,156 | CLAUDE.md (always loaded) |
| 78,964 | 78% | 61,336 | metaworker-dispatch |
| 58,910 | 73% | 43,044 | queue-experiment |
| 49,257 | 80% | 39,178 | failure-autopsy |
| 51,236 | 66% | 33,869 | governance |
| 35,572 | 74% | 26,372 | session-land |
| 24,165 | 78% | 18,874 | account-handover |
| 23,297 | 60% | 13,978 | morning-digest |

**Six files carry 272,955 of the 364,575 recoverable tokens (75%).** At the other end,
`view-experiments` is 3% archaeology, `sync` 17%, `inter-governance-brief` 24%, `zombie-reaper`
34% -- these need nothing, and a blanket policy applied to them would be wasted effort.

Caveat, unchanged from the body: the classifier's ARCH share is an upper bound (72% agreement with
hand labels, over-calling archaeology on genuinely operative blocks). Treat the per-file
percentages as a ranking, which they are reliable for, rather than as precise targets.

## Revised recommendation ordering

1. **Split the six archaeology-heavy files** (CLAUDE.md + the five large skills). ~57% of total
   spend, 75% of it in six files. This is now clearly first, not third.
2. **Preflight batch triage** -- 17.7% of chip sessions are full-length already-done discoveries.
3. **Persistent/batching sessions** -- saves one floor write per avoided session, no growth
   penalty; safe and additive.
4. **No-op pre-exit** -- keep, but narrow; build after (1).
5. **Budget ledger** -- unchanged; it is a safety net, not a saving.

## On the remaining "open, not measured" items

- **All 27 other skills** -- now measured, above. It cost one classifier run. Not expensive.
- **Whether the harness re-reads CLAUDE.md per session, or the platform cache TTL binds** --
  genuinely not cheap to separate, and **it does not change any decision here**: the observed
  reuse is zero either way, and every recommendation above is a size or count reduction that pays
  off identically under both explanations. Recommend leaving it unmeasured.
- **AGENTS.md** -- measured: 7,432 tokens, 61% archaeology, 4,512 recoverable. Small; low priority.

---

# PLAN OF ACTION

Added 2026-08-23T15:05:58Z, after user review of the body and addendum. Ordering follows the
addendum's revised ranking, not the body's. Steps 1-3 are the ~57% lever; steps 4-6 are the
three already-chunked chips; step 7 checks whether any of it worked.

**Sequencing constraint that shapes everything below:** an open chip that declares a SKILL.md as
a `--resources` path will arbitrate against a split session touching the same file (CLAUDE.md
"Conflict resolution"). Audited 2026-08-23 across 34 open chips:

| skill | ~tok recoverable | declared-resource collision |
|---|---|---|
| queue-experiment | 43,044 | **clear** |
| governance | 33,869 | **clear** |
| session-land | 26,372 | **clear** |
| account-handover | 18,874 | **clear** |
| thought-digestion | 9,183 | **clear** |
| failure-autopsy | 39,178 | chip-20260821-phase3writers-failureautopsy-skill-edit |
| metaworker-dispatch | 61,336 | chunk 1 + chip-20260823-dispatch-preflight-only-checks-umbrella |
| morning-digest | 13,978 | chip-20260823-morning-digest-scheduler-misfire |

## Step 1 -- pilot the split on ONE skill, and establish the convention (IN PROGRESS)

Pilot: **`queue-experiment`** -- largest recoverable of the collision-clear files, and its
operative core (write a script, smoke it, queue it) is sharply separable from its incident record.

Deliverables:
  (a) a convention: archaeology lives at `docs/skill_archaeology/<skill>.md` in the umbrella repo
      -- ONE copy, deliberately NOT inside `.claude/skills/` or `.agents/skills/`, because those
      two trees must stay byte-identical and putting it there would duplicate the archaeology
      rather than remove it;
  (b) the split itself, with every moved block reachable by an inline pointer;
  (c) a measured before/after token count;
  (d) a validation that the operative core is intact -- every mandatory step, command, path and
      hard prohibition still present in the SKILL.md itself, not only in the referenced file.

## Step 2 -- apply the validated convention to the collision-clear skills

`governance`, `session-land`, `account-handover`, `thought-digestion`. ~88,000 further tokens.
Do NOT start before step 1 (d) passes -- the point of a pilot is that the convention can still
change cheaply.

## Step 3 -- CLAUDE.md (69,156 recoverable, and the only always-loaded file)

Highest per-session value and highest risk, so it goes last of the file work.
**This is a standing-rule change and therefore REQUIRES the GOV-HELDOUT-1 held-out check**
(CLAUDE.md General Rules): test the proposed inline-vs-referenced wording against >=3 historical
cases it was not written from, where inline and referenced give DIFFERENT calls. The `Scope
history` blocks are the ready-made corpus. The specific risk to test is whether a session that
does not follow the pointer makes the error the inline text was preventing. If 3 differing cases
cannot be found, narrow the change and say so rather than shipping it as general.

Four sections are 65% of the file and should be split first:
`Claim-first, edit-last` (22,656 tok, 82% arch) · `Session Startup Protocol` (17,157, 73%) ·
`Housekeeping (every session close)` (9,364, 86%) · `Running the test suite` (7,093, 98%).

## Step 4 -- chunk 2 chip: hygiene batching

`chip-20260823-hygiene-batch-one-chip-per-family`. Independent, parallel-safe, and the only
*daily recurring* saving (7 x 102,412 per corpus round). Can run at any time, including alongside
steps 1-3.

## Step 5 -- chunk 1 chip: dispatch admission gate, WITH the metaworker-dispatch split folded in

`chip-20260823-preflight-batch-triage-of-candidate-chips`, build order (b) budget gate,
(c) batch triage, (d) host-preference ordering, then (a) no-op pre-exit.
**Fold the metaworker-dispatch SKILL.md split (61,336 tok, the single largest recoverable) into
this same session.** That chip already claims both copies of that file, so a separate split
session would arbitrate against it and stop. This is the same merge logic that produced chunk 1
in the first place.

## Step 6 -- chunk 3 chip: remote-tip default flip

`chip-20260823-remotetip-flip-ledger-writer-defaults`. Independent, parallel-safe, user-authorised.

## Step 7 -- re-measure, and publish the delta

Re-run the turn-level simulation against post-split transcripts and compare to the predicted
~57%. The prediction is a simulation, not an observation; it has not yet been tested against a
real post-split session. Treat any step that does not move the measured number as a finding about
the model, not a rounding error.

## Explicitly NOT in this plan

- Deleting any archaeology. Every incident record measured here documents a confirmed failure and
  several exist specifically to stop a later session simplifying a rule back into a bug.
  Everything moves; nothing is dropped.
- Splitting the lean skills (`view-experiments` 3% archaeology, `sync` 17%,
  `inter-governance-brief` 24%, `zombie-reaper` 34%). A blanket policy across all 29 files would
  spend effort where there is nothing to recover.
- Separating "harness re-reads per session" from "cache TTL binds" -- see the body's open items.
  Observed reuse is zero either way and every step above pays off identically under both.
