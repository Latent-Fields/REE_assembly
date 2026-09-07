# Context-budget restructure: plan of record

**Opened:** 2026-09-07T17:55:42Z
**Status:** proposed -- not started
**Evidence base:** [`token_split_measurement_20260907.md`](token_split_measurement_20260907.md)
(REE_assembly `b36526f715`). Every figure below comes from that measurement; nothing here
is re-derived or estimated independently.

**Goal:** recover ~14% of the fleet's billed input-token budget, losslessly, by
re-granularizing instructional context behind loading mechanisms that already exist.

**Non-goal:** adopting a tool-output compression layer. That was measured and declined --
addressable surface 20.6% of budget, realistic saving 4-6%, and it puts a lossy layer
between the model and the byte-exact reads the concurrency doctrine depends on.

---

## 1. The finding this rests on

Post-fix corpus: 295 sessions, 38,828 assistant turns, 11.47 B billed input tokens.
Fit quality R^2 median 0.9954, per-turn residual median 0.9%.

**~59% of every token billed is instructional context before any work product exists.**

The single worst offender:

| file | size | approx tokens |
|---|---|---|
| **`ree-v3/CLAUDE.md`** | **1,472,082 chars** | **~368,000** |
| `CLAUDE.md` (umbrella) | 154,611 chars | ~38,650 |

`ree-v3/CLAUDE.md` is 214 top-level sections of **per-feature substrate records**
(SD-082, SD-063, ARC-110, MECH-463, ...), 139 distinct feature IDs, median section
~5,900 chars. It is injected whole as a `nested_memory` attachment whenever a session
touches `ree-v3/`.

**The decisive measurement -- how much of it a loading session actually uses:**

> Across the 25 post-fix sessions that loaded it, the **median session referenced 2 of
> the 139 feature IDs (1.4%)**. Mean 3.3, max 20. **Nine of 25 referenced zero.**

Those sessions cost a median **30.6 M** billed input tokens against **17.3 M** for
sessions that do not load it -- 1.8x -- and harness injections are **51.30%** of their
budget.

---

## 2. Why the fix is NOT a new loader

Two lazy-loading mechanisms already exist and already work:

1. **Skills already do progressive disclosure.** The 29 `SKILL.md` files total
   ~1,088,000 chars (~272,000 tokens) of body, but the *measured* fixed baseline is
   ~92,000 tokens in total. Bodies demonstrably do not load up front -- only descriptions.
2. **Nested `CLAUDE.md` is already directory-triggered.** Only 25 of 295 sessions ever
   loaded `ree-v3/CLAUDE.md`. The trigger is working as designed.

**The defect is the granularity of what sits behind those triggers, not the triggers.**
Building a per-skill context loader would add a mechanism to solve a problem that is
actually a content-layout problem.

The umbrella `CLAUDE.md` already contains the proven template: the **`A-01`..`A-94`
skill-archaeology pattern** -- a one-line pointer carrying a token cost and a
"not needed to follow the rule, read it before changing it" note, with the content in a
separate file read on demand.

---

## 3. Why the key is FEATURE, not SKILL

The original framing was per-skill context. The measurement does not support it as the
primary key:

| sessions | count | share of budget |
|---|---|---|
| invoke **no** skill | 173 (58.6%) | 21.0% |
| invoke **exactly 1** skill | 68 (23.1%) | 29.0% |
| invoke **2+** skills | 54 (18.3%) | **50.1%** |

Only 23% are single-skill. `session-land` alone appears in 87 sessions -- it is the
near-universal closing skill, which is why `<work skill> + session-land` is both the
commonest shape and half the budget. **Keying context on skill identity would miss most
of the spend.**

And the umbrella file is mostly not skill-specific:

| section | share of file | scopable to a skill? |
|---|---|---|
| Concurrency Rules | 23.3% | **no** -- every session that writes |
| Session Startup Protocol | 15.5% | **no** |
| Session Land Protocol | 14.4% | **no** -- 87 sessions run it |
| Worktree / Chipped Sessions | 6.0% | **no** |
| General Rules + Git Policy | 5.0% | **no** |
| test suite, scripts corpus, coordinator, experiments, governance, misc | **~29%** | **yes** |

~64% is genuinely universal. So skill-scoping is a real but *secondary* lever, and
`ree-v3/CLAUDE.md` -- keyed on feature ID -- is the primary one.

---

## 4. Work items

### WI-1 (primary): `ree-v3/CLAUDE.md` -> thin index + per-feature files

Split the 214 sections into `ree-v3/docs/substrate/<FEATURE-ID>.md`, leaving an index of
headings plus whatever preamble is genuinely universal to ree-v3 work.

- 214 headings as an index is ~17 KB (~4,300 tok) against ~368,000 tok today.
- Pointer form: copy the umbrella's archaeology annotation exactly -- feature ID, one-line
  summary, approximate token cost, and when to read it.
- **Byte-exactness is a hard requirement.** Extracted section content must be
  byte-identical to what it replaced; verify mechanically (concatenate the extracted files
  in original order and diff against the original file) rather than by inspection.

**Expected saving: ~9.2% of total fleet budget; ~46% for the 25 sessions that load it.**

### WI-2 (secondary): umbrella `CLAUDE.md` -> move skill-specific sections into SKILL.md

Candidates, with their share of the umbrella file:

| section | share | destination |
|---|---|---|
| Running the test suite (cloud routing) | 9.0% | `implement-substrate`, `queue-experiment` |
| Running the umbrella `scripts/` test corpus | 3.6% | (sessions editing `scripts/`) |
| Coordinator (Phase 3) | 4.3% | `metaworker-*`, fleet work |
| Multi-Machine Experiment Coordination | 3.1% | `queue-experiment` |
| Experiment Scripts + Runner + EXQ Versioning | 4.4% | `queue-experiment`, `diagnose-errors` |
| Governance Pipeline + Experiment Review Tracking + V3-Pending Gate | 1.3% | `governance` |
| Dev Doctor, Explorer, MCP server, Recommendation ledger, Literature Pulls | ~3.5% | respective skills |

**Expected saving: ~29% of the umbrella file ~= 4.8% of total budget.**

**Do NOT move:** Concurrency Rules, Session Startup Protocol, Session Land Protocol,
Worktree / Chipped Sessions, General Rules, Git Policy, Timestamps, Python, ASCII-only,
Shell Portability, Hooks, High-Contention Files. A rule `session-land` needs is universal
by definition, and 59% of sessions invoke no skill at all.

### Combined

| lever | saving | risk |
|---|---|---|
| WI-1 | ~9.2% | none |
| WI-2 | ~4.8% | none |
| **both** | **~14%** | **none** |
| *(Headroom best case, for comparison)* | *11.7%* | *lossy, proxy, new failure surface* |
| *(Headroom realistic here)* | *4-6%* | *as above* |

The restructure beats the compression layer's best case and roughly triples its realistic
case, without a lossy layer.

---

## 5. Constraints and known failure modes

1. **The pointer must carry enough signal that the model knows when to follow it.** This
   is the live risk of the archaeology pattern: a rule that is now one line away can be
   *missed* rather than merely deferred. The umbrella's existing annotation form
   (`~N tok; not needed to follow the rule, read it before changing it`) is the mitigation
   and should be copied verbatim in shape.
2. **GOV-HELDOUT-1 applies.** WI-2 edits standing rules. Before landing, check the new
   layout against >=3 historical cases the wording was NOT written from, counting only
   cases where old and new give *different* answers. If 3 such cases cannot be found, say
   so explicitly rather than shipping the check as a rubber stamp.
3. **Byte-exactness on extraction** (WI-1) -- verify by mechanical recomposition, not by
   reading.
4. **`ree-v3` is the executable-code plane.** A change this size spanning sessions belongs
   on a short-lived `integration/<slug>` branch per Git Policy, deleted on merge. It
   touches no coordination data, so it must not be batched with any `evidence/**` or
   `experiment_queue.json` edit.
5. **Land incrementally.** WI-1 is naturally sliceable by feature ID; land verified slices
   rather than one 214-file commit.

---

## 6. Negative control

If a loading session had referenced a *large* share of `ree-v3/CLAUDE.md`'s feature
sections, WI-1 would be wrong -- the file would be earning its place and splitting it
would just add indirection. It does not: median 2 of 139, and 9 of 25 sessions referenced
none. If a future re-measure shows the median session referencing >30% of sections, revisit.
