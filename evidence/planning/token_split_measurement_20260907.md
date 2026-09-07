# Token-split measurement: is tool-output compression (Headroom) worth adopting?

**Measured:** 2026-09-07T17:36:04Z
**Question:** Of the tokens actually billed against the Claude subscription limit, what
fraction is fixed prompt overhead vs tool output? Decides whether a tool-output
compression layer (github.com/headroomlabs-ai/headroom) addresses a binding constraint.

**Verdict: NO. Do not adopt Headroom.** Its addressable surface is 20.6% of the input
budget, best case ~11.7% net saving, realistically ~4-6%. Trimming the two oversized
`CLAUDE.md` files reaches ~11.2% for free, permanently, with no lossy layer and no new
failure surface. For the highest-cost sessions the gap is far wider still (below).

---

## Method

Every `assistant` record in a Claude Code transcript carries the API's own usage numbers,
so total input tokens for turn *i* are known exactly:

```
T_i = input_tokens + cache_read_input_tokens + cache_creation_input_tokens
```

The context at turn *i* is a constant baseline **B** (system prompt + CLAUDE.md + skill
and tool definitions -- never stored in the transcript) plus conversation content
accumulated so far, which **is** stored and countable in characters:

```
T_i = B + C_i / r        (C_i = cumulative conversation chars, r = chars/token)
```

Two unknowns, many turns -> solved by ordinary least squares per session. Both B and r
are therefore *calibrated against ground truth*, not assumed. Conversation content is
then attributed by category and weighted by how many turns re-read it, because prompt
caching still charges `cache_read` on every turn.

Script: `scripts/token_split.py` (session scratchpad; reproduced in full below is not
necessary -- the method is the four lines above).

### Fit quality -- and one vacuity trap avoided

The first fit diagnostic compared *summed* fitted vs measured tokens and reported 0.0%
error at every percentile. That check is **vacuous**: OLS with an intercept forces the
sum of residuals to zero by construction, so the sums match identically no matter how bad
the fit is. Replaced with genuine per-turn diagnostics:

| diagnostic | value |
|---|---|
| R^2, median across 280 sessions | **0.9954** |
| R^2, p10 | 0.9818 |
| per-turn abs residual / actual, median | **0.9%** |
| per-turn abs residual / actual, p90 | 2.1% |

The decomposition is trustworthy to ~1% per turn.

### Corpus

`~/.claude/projects/**/*.jsonl`, REE_Working project dirs, last 21 days, >20 KB.
1,782 candidates -> 1,486 with a usable fit.

**Restricted to the post-fix regime** (first turn >= 2026-08-29) for all headline
numbers: **295 sessions, 38,828 assistant turns, 11.47 B billed input tokens.** Why the
restriction is in the next section.

`ree-worker-4` (the resident metaworker-dispatch box) was `off` at measurement time, so
headless numbers come from the 24 `sdk-cli` sessions present locally, not from that box.

---

## Finding 0 -- a defect that was already fixed, and why it had to be excluded

Across 2026-08-20..27, `PreToolUse:Bash` emitted a `hook_success` attachment averaging
**3,570 chars** on essentially every Bash call, and **97% of them (12,098 / 12,436) carried
a Python traceback** -- `json.decoder.JSONDecodeError: Invalid \escape`, from an inline
`python3 -c` that mangled backslashes in the tool-input JSON. ~11 M chars of raw traceback
text were injected into context in the sampled window alone.

**This stopped dead on 2026-08-28** (zero occurrences since), matching
`.claude/settings.json.bak-echo-printf-20260828T055424Z` in the repo root -- the
`echo`->`printf` fix. It is **already repaired; no action is owed.**

It is recorded here for two reasons. First, it was worth ~19% of the input budget while
live, which is *more than Headroom's entire best case* -- a datapoint on where the real
money is. Second, including it would have inflated the "harness injection" share and
biased this measurement toward the wrong conclusion. Hence the post-2026-08-29 cut.

---

## Finding 1 -- current composition of the billed input budget

295 post-fix sessions, 38,828 turns, 11.47 B input tokens. Median fixed baseline
**92,078 tokens per turn**; median 91 turns per session.

| category | share of billed input |
|---|---|
| **FIXED PROMPT** (system + CLAUDE.md + skills + tool defs) | **39.57%** |
| **tool results** (Bash / Read / Grep / MCP output) | **20.55%** |
| harness injections (nested memory, skill & tool listings) | 19.59% |
| assistant tool *calls* (params) | 9.71% |
| user prompts | 9.19% |
| assistant prose | 1.00% |
| assistant thinking | 0.36% |
| system-reminders | 0.02% |

Headless `claude -p` sessions (n=24) are *more* prompt-dominated, not less:
**43.93% fixed prompt, 22.04% tool results, 6.96% injections.**

**~59% of every token billed is instructional context -- prompt, memory, listings --
before any work product exists.** Tool output, Headroom's entire target, is one fifth.

---

## Finding 2 -- `ree-v3/CLAUDE.md` is 1.47 MB

| file | size | approx tokens |
|---|---|---|
| **`ree-v3/CLAUDE.md`** | **1,472,458 chars** | **~368,000** |
| `CLAUDE.md` (umbrella) | 155,014 chars | ~38,750 |
| `AGENTS.md` | 20,366 chars | ~5,090 |
| `REE_assembly/CLAUDE.md` | 34,974 chars | ~8,740 |

`ree-v3/CLAUDE.md` is **9.5x the umbrella file** and is injected as a `nested_memory`
attachment whenever a session touches ree-v3. It alone is 52.3% of all harness-injection
volume.

Splitting the corpus on whether that injection occurred is the sharpest result here:

| | loads `ree-v3/CLAUDE.md` (n=25) | does not (n=270) |
|---|---|---|
| median billed input **per session** | **30,616,496** | 17,315,876 |
| fixed prompt share | 37.68% | 39.83% |
| **harness-injection share** | **51.30%** | 15.28% |
| **tool-result share** | **6.32%** | 22.48% |

Those sessions cost **1.8x more per session** and are the ones where Headroom is least
applicable: its target shrinks to **6.32%** of their budget while injected instructions
take **51.30%**.

---

## Decision table

Levers ranked by share of total input budget recovered, post-fix corpus:

| lever | saving | risk |
|---|---|---|
| Headroom, tool results -57% (their *best* published case, SRE debugging) | 11.71% | lossy layer, proxy, new failure surface |
| **Both CLAUDE.md trims together** | **11.24%** | **none** |
| Trim `ree-v3/CLAUDE.md` 1.47 MB -> 300 KB | 8.20% | none |
| Headroom, tool results -21% (their code-search case) | 4.32% | as above |
| Trim umbrella `CLAUDE.md` 155 KB -> 80 KB | 3.04% | none |

Headroom's published range is 21%-57%; the 57% figure is their SRE-log scenario. REE's
tool output is mostly git porcelain, grep hits and python stdout, and the genuinely large
JSON registries (`TASK_CHIPS.json` 10.5 MB, `claims.yaml` 7 MB) are already accessed
through CLI helpers rather than dumped into context. **The low end of their range is the
honest planning estimate for this workload: ~4-6%.**

---

## Recommendation

1. **Do not adopt Headroom.** Confirmed by measurement, not by caution. It targets one
   fifth of the budget, and the part of the budget it targets is the part this project has
   *already* engineered down with CLI helpers. Set against that: compression is lossy by
   design, and the concurrency doctrine in `CLAUDE.md` depends on byte-exact reads --
   `git status` porcelain *codes* (` M` vs `M ` vs ` D` vs `D `, where one repair destroys
   what the other restores), `git show <base>:<path> | diff -q`, byte-identical vendored
   copies, `chip_ledger.py record` refusing a `--prompt` that does not *literally* contain
   its marker. CCR retrieval does not rescue this: the model must know it lost something
   to fetch it, and not-knowing is the failure mode.

2. **Trim `ree-v3/CLAUDE.md` (1.47 MB).** Largest single lever, zero risk, and the
   umbrella file's own A-01..A-94 archaeology extraction is the proven pattern to apply.
   Highest-value target: the 25 sessions that load it cost 1.8x the rest.

3. **Continue the umbrella `CLAUDE.md` archaeology extraction.** Already working; 3.04%
   more available.

4. If tool-output compression is still wanted later, the only shape that does not fight the
   doctrine is **Headroom's MCP mode as an opt-in tool** a session deliberately calls on a
   known-bulky read -- no proxy, no interception, nothing compressed without being asked.
   Treat as `complex (probe-gated)`, not as an implementation.

## Negative control

If this measurement had shown tool results >50% of the budget and the fixed prompt <15%,
the recommendation would have flipped to adopting Headroom in proxy mode. It did not:
the ratio is almost exactly inverted.
