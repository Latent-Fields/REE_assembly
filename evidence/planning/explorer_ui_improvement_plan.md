# Explorer UI Improvement Plan

**Status:** DRAFT -- awaiting user review/approval. Nothing in this doc beyond the
"Done now" section (below) has been implemented.
**Scope:** `REE_assembly/explorer.html` (~9,600 lines) + its backend `serve.py`
(~6,800 lines). Linked-out pages reachable from the top nav (`/workset`,
`/closure`, `/progress`, `/brain-map`, `/code-atlas`, `/machines`, `/igw`,
`/fishtank_viz.html`) are **separate HTML files with their own JS/CSS** -- out
of scope for this pass except where explicitly noted.
**Author:** Claude (session `determined-ritchie-55a3a6`), 2026-08-02.
**Method:** static read-through of `explorer.html` + `serve.py` (no code
changes beyond the two additive items below), cross-referencing what `serve.py`
computes/reads against what the frontend actually renders, in the same spirit
as the `pending_review_count` badge fix that motivated this review.

---

## Done now (trivial, additive, already landed)

These match the "purely additive, no layout/IA change" bar from the task brief
and were implemented directly. `EXPLORER_VERSION` bumped to `2026-08-02.2`.

1. **Queue cards now render `priority` and a stale-claim warning, if present.**
   `expQueueItemHtml()` (`explorer.html`, was line 7737) gained a `▲ <priority>`
   chip and a `claimStaleHtml()` helper that flags `claimed_by.claimed_at` older
   than 6h (matching the runner's own stale-claim cutoff). **Honest caveat:**
   this is currently a no-op in the browser -- see Finding #1 below, which is
   the reason it's a no-op and the single highest-value fix in this whole
   review. The client-side rendering is left in place because it's harmless
   and forward-compatible: the moment serve.py passes the two fields through,
   these chips light up with zero further frontend work.

No other changes were made to `explorer.html`. Everything below is a proposal.

---

## Finding #1 (top priority): `priority` and `claimed_by` are silently dropped between the queue file and every API that serves it

**File:** `serve.py:5584-5604`, function `_queue_items_from_raw()`.
**Effort: small** (2-line change, one function, two call sites both already
covered by the same fix). **Needs a serve.py restart to take effect** -- not
done in this session since a shared server may have other sessions/tabs
depending on it; flagging for the user to apply when convenient.

This is the *exact same class of gap* as the `pending_review_count` fix that
prompted this review -- a value that already exists in the underlying data and
is already computed/read, but is stripped before it reaches the browser.

`ree-v3/experiment_queue.json` items carry `priority` (e.g. `50`, `40`, `35` on
today's live queue) and `claimed_by: {machine, claimed_at}`. Both
`/api/queue/v3` (file mirror) and `/api/queue/live` (coordinator-DB path, the
default when the coordinator is reachable -- i.e. most of the time) route
every item through the same `_queue_items_from_raw()` normalizer, which
whitelists exactly these output keys:

```python
{"queue_id", "claim_id", "title", "description", "status", "script",
 "estimated_minutes", "machine_affinity", "ree_version"}
```

`priority` and `claimed_by` are silently omitted. Confirmed live via
`curl localhost:8000/api/queue/live` and `/api/queue/v3` on 2026-08-02: neither
endpoint returns either key, on either the coordinator or file-mirror path,
even though the raw queue file plainly has them.

**Consequence:** the frontend has *already* been written as if these fields
arrive -- `expBadgeHtml(qi.status, undefined, qi.claimed_by && qi.claimed_by.machine)`
existed **before** this session's edits and has presumably never actually
fired the "claimed by machine" badge path via the live APIs. This is worth the
user's attention on its own: it suggests a UI affordance that looks wired up
in the source but has been dark in the browser for some time.

**Fix:** add two lines to `_queue_items_from_raw()`:
```python
"priority": item.get("priority"),
"claimed_by": item.get("claimed_by"),
```
Both endpoints share the function, so one edit fixes both. No frontend change
needed beyond what's already landed above (Done now, item 1).

**Related, smaller note:** the frontend also reads `qi.failure_reason`,
`qi.failed_at`, and `qi.status_reason`, none of which exist anywhere in the
current `experiment_queue.json` schema (checked: full key set across all 16
live items is `architecture_epoch, backlog_id, claim_id, claim_ids,
claimed_by, conditions, episodes_per_run, estimated_minutes,
experiment_purpose, experiment_type, machine_affinity, note, priority,
queue_id, script, seeds, status, supersedes, title`). That rendering code may
be forward-looking (written for a schema field that hasn't landed yet) rather
than broken -- flagging for awareness, not proposing a fix, since it's unclear
which side (schema or UI) is meant to catch up.

---

## (a) Sorting

### A1. The primary claims List view (the `List` nav tab, ~967 claims) has no sort control at all
**Effort: small.** `renderTable()` (`explorer.html:6188`) iterates
`applyFilters()`'s output in whatever order the claims arrived from the API --
there is no column-header click-to-sort, no sort-by dropdown, and no
pagination. With ~967 claims and only 4 filter fields (search/type/status/
subject) plus 2 checkboxes to narrow the view, a filtered result set of, say,
150 claims renders in insertion order and has to be scanned top-to-bottom to
find anything ordered by importance.

The table already has a natural sort key in almost every column: `Posterior`
(the Beta-Binomial confidence value), `Conflicts` (count), `Depends On`
(count), `Status`. None are sortable.

**Proposal (needs design discussion, not a trivial fix -- it touches the table
header markup and `renderTable()`'s render loop):** click-to-sort column
headers (ascending/descending toggle, arrow indicator), defaulting to today's
apparent order so nothing changes until a user clicks a header. Cheapest
version: a single "Sort by" `<select>` next to the existing filter row
(ID / Status / Posterior / Conflicts, asc/desc), which avoids any table markup
change and is closer to "additive."

### A2. Queue items are never sorted or displayed by `priority`, despite priority being the field that determines run order
**Effort: small**, and blocked on Finding #1 (the field has to reach the
browser first). Once it does: queue cards currently render in whatever order
the coordinator/file returns (today: by `queue_id` insertion order, e.g.
`V3-EXQ-875, V3-EXQ-862a, V3-EXQ-869a, ...`), which does **not** match the
`priority` values in the same file (`50, 35, ...`). A user glancing at the
Queue section today cannot tell what will actually run next without opening
the raw JSON. Recommend sorting the queue render by `priority` descending
(matching [memory] "priority is HIGHER=runs first"), falling back to today's
order when priority is absent.

### A3. The "current epoch only" filter exists on Map and Governance but not on the primary List view
**Effort: small.** `isCurrentEpochClaim()` / `filterRowsByCurrentEpoch()`
already exist and are wired into `mapEpochOnly` (Map view,
`explorer.html:2436`, default checked) and `govEpochOnly` (Governance view,
`explorer.html:2485`, default checked). The List view's `applyFilters()`
(`explorer.html:6153`) never calls either helper -- so the primary,
default-landing claims browser has no way to hide claims that Map and
Governance already agree are stale-for-the-current-architecture-epoch by
default. This is an inconsistency across views of the *same underlying
concept*, not a missing feature invented from scratch -- wiring it into List
is a small, mechanical addition (one checkbox + one filter predicate, same
pattern as the two existing checkboxes).

### A4. No "has conflict" filter, despite Conflicts being a full table column
**Effort: trivial-to-small** (adds one checkbox to the existing filter row,
same pattern as `v3PendingFilter`/`evidencedFilter`). Flagged as a proposal
rather than done directly because it does add a visible control (small layout
change), per the brief's line between "purely additive with no layout change"
and everything else.

### A5. Experiments > Completed is sorted (fixed, by completion time desc) -- this one is fine
Noted for contrast: `allCompleted.sort(...)` (`explorer.html:8181`) already
sorts sensibly and needs no change. Listed so the plan doesn't read as "nothing
is ever sorted" -- one section already gets this right and is a reasonable
model for the others.

---

## (b) High-importance items buried or not surfaced

### B1. (Superseded by Finding #1 above, listed here for completeness) `claimed_by` staleness on queue items
Once Finding #1 lands, the stale-claim chip added in "Done now" surfaces
exactly the kind of thing the task brief called out by name ("stuck claims").
No further action needed beyond Finding #1 itself.

### B2. `TASK_CLAIMS.json` staleness and orphaned git stashes are **not computed by serve.py at all** -- this is a bigger ask than it looks
Checked directly: `serve.py` has no reference to `TASK_CLAIMS.json` content
(only to the *chip* ledger, `TASK_CHIPS.json`, which is a separate, already-
surfaced concept via the `/workset` "Pending chips" panel). Stale-claim
detection (`scripts/audit_stale_claims.py`) and orphaned-stash detection
(`scripts/audit_stashes.py`) are standalone CLI scripts with no HTTP surface.

**This is different in kind from the `pending_review_count` fix** -- that fix
wired an *existing, already-computed* server value into the UI. Surfacing
claim/stash staleness would mean either (a) serve.py shells out to those
scripts and parses their output on some cadence, or (b) they get a proper
importable function + cheap cache, mirroring how `_closure_pending_review_count()`
or the preflight/writer-health badges are memoised. Both are real backend
work, not a UI tweak.
**Effort: needs-design-discussion.** Worth doing given how well the existing
badge/corner-dock patterns work (see B4), but it's a scoped feature, not a
"surface the hidden field" fix -- flagging rather than building, and it's also
arguably its own chip/task rather than part of an "Explorer UI polish" pass,
since the real work is scripting, not markup.

### B3. Load-bearing blocked closure nodes: partially surfaced, worth checking against Finding #1's pattern
`serve.py` already computes `blocked_load_bearing` counts (line ~3484) and
`pending_review_count` (now badged). The `/closure` page is a separate file
and wasn't audited in this pass (out of scope per the header), but if the user
wants this pass extended, the same "grep serve.py's computed dicts against
what closure.html actually renders" technique used for Finding #1 would be the
right next step there. **Flagging as a possible follow-on, not doing it here**
-- closure.html is a distinct file with its own review surface.

### B4. The two existing "surface hidden state" patterns are good and should be the template for anything new
Worth naming explicitly so future additions (including B2, if built) don't
invent a third pattern:
- **Nav badges** (`govConflictBadge`, `pendingReviewBadge`): small orange count
  badge on a top-nav button, for "there is N of this waiting" signals tied to
  a specific view.
- **Corner dock** (`#cornerDock`, bottom-right, persistent across all views):
  "Claude usage" and "Coordination" (Phase 3 writer health + shadow verdict)
  cards, each collapsible, always visible regardless of which view is active.

Both are already well-suited to different jobs: nav badges for "go look at
view X", corner dock for "ambient health status that matters everywhere."
Any new stale-claim/stash-orphan signal (B2) should pick whichever of these
two fits, rather than adding a third convention.

### B5. Clicking the `pendingReviewBadge` doesn't go anywhere useful
**Effort: small, but touches click behavior -- proposing, not doing.** The
badge's tooltip literally says "see More > Docs > Pending review (inbox)"
(`explorer.html:5518`) rather than taking the user there directly, because the
badge is nested inside the `experimentsViewBtn` button and inherits its click
handler (switches to the Experiments view, not to the doc). A direct win:
make the badge itself (or a click on it) open the Docs view with
`pending_review.md` pre-selected. Small, but it is a behavior change to an
existing control, so left as a proposal rather than bundled into "Done now."

---

## (c) Visual design consistency

### C1. No dark mode / `prefers-color-scheme` support anywhere in the file
**Effort: needs-design-discussion** (large surface area: the whole file is
one light palette). Confirmed: zero occurrences of `prefers-color-scheme` in
9,600 lines. All ~10 `:root` CSS variables (`--bg`, `--ink`, `--accent`, etc.,
`explorer.html:9-20`) are a single warm-light palette. Not flagging this as
urgent -- just noting it's a real gap if the user works at night/prefers dark
UIs, and it would be a substantial, deliberate pass (would need to touch every
ad-hoc inline color too, see C2), not a quick add.

### C2. Dozens of ad-hoc inline hex colors instead of the existing CSS custom properties
**Effort: needs-design-discussion.** The file already defines a reasonable
small palette (`--accent`, `--error`, `--muted`, etc.) but a large fraction of
status/semantic coloring bypasses it with inline hex, e.g. greens
`#2e7d32`/`#2e9e6b`, ambers `#c98a1e`/`#b8860b`/`#e65100`/`#b67923`, reds
`#d9534f`/`#c62828`/`#c0392b`/`#8c2f2f`, plus generic grays `#555`/`#888`/
`#999`/`#666`/`#777`/`#aaa` repeated 5-9 times each for muted text that
`var(--muted)` already exists to express. None of this is broken -- it reads
fine today -- but it means "make all warnings the same amber" or "add dark
mode" both require hunting down every ad-hoc value rather than changing one
variable. Recommend, if the user wants to invest here: add
`--success`/`--warning`/`--danger` alongside the existing `--error`, and
migrate the repeated literals opportunistically (not all at once -- real risk
of an unintended visual change hiding in a mechanical find/replace across a
9,600-line file with no visual regression test).

### C3. The "More" dropdown is exactly the accretion problem named in the task brief
**Effort: needs-design-discussion.** Confirmed: 8 destinations behind one
caret (`explorer.html:2233-2247`) -- 2 in-app views (Docs, Contributors) and 6
external dashboard links (Progress, Brain Map, Code Atlas, Machines, IGW
Routine, Fishtank), each a different visual register (some are pages inside
this same app, most are entirely separate tools/servers). The dropdown does
group them under two labels ("Reference" / "Dashboards"), which helps, but the
underlying issue is that "More" is where *everything that isn't a primary
claim-governance-experiment view* goes, regardless of how different those
things are. Not proposing a specific IA here -- this is squarely a "needs
design discussion" item per the task brief, since reorganizing nav is exactly
the kind of change that shouldn't be done unilaterally. Options worth putting
in front of the user when this gets discussed: split "external dashboards"
into their own top-level affordance distinct from "in-app reference pages";
or promote Docs out of More (it's core reference material, not a peripheral
tool) the same way Workset/Closure already got promoted to top-level buttons.

### C4. The `Docs` picker is a 70-item, 16-group single `<select>`
**Effort: small-to-needs-design-discussion depending on how far to take it.**
Counted directly: `DOC_GROUPS` (`explorer.html:2697`) has 70 `title:` entries
across 16 `label:` groups, all in one native `<select>` with a client-side
text filter (`docSearch`) alongside it. The filter helps, but a flat
70-option dropdown (even grouped) is a dated pattern for this much content;
this is also the exact control the concrete example in the task brief had to
be badge-routed around (3 clicks: More -> Docs -> find "Pending review" in the
dropdown). A searchable list/tree panel (visible titles, not a collapsed
`<select>`) would read better at this scale, but that's a real UI component
change -- proposing, not building.
**Smaller, related, purely a maintenance note (not urging any fix):**
`DOC_GROUPS` is a hardcoded JS array, so every new doc needs a manual
`explorer.html` edit to become reachable via this picker at all -- worth
knowing if the user finds a doc that "isn't in the dropdown."

---

## (d) General usability

### D1. No pagination or row virtualization on the List table
**Effort: small, and pairs naturally with A1.** `renderTable()` builds a `<tr>`
for every filtered claim with no cap -- with the full ~967-claim set and loose
filters, that's up to ~967 DOM rows rendered at once. Not confirmed as a
perceptible perf problem in this pass (no profiling done), but combined with
A1 (no sort) it compounds: a long, unsorted, unpaginated table is the
hardest-to-scan shape a list view can have. If A1 (sort) lands, pagination
becomes less urgent since a sorted "top 20 by X" is usually what's wanted
anyway -- listing both together so the user can decide whether to do one or
both.

### D2. Existing responsive breakpoints are reasonable; not flagging mobile as a gap
Confirmed 3 `@media` breakpoints (900px, 760px, 700px) already handle
header-link collapsing and the corner dock's phone-width behavior, and a
dedicated `mobile_help.html` exists. No action proposed here -- included so
the plan doesn't read as having skipped a mobile check.

### D3. Governance's "What to do now" priority pane is a good pattern the other views lack
`explorer.html:5665-5668` -- a small pane at the top of the Governance view
that reduces the whole agenda to "N urgent things, ranked, with anchor links,
or a green checkmark if there's nothing." List/Experiments/Map have no
equivalent distillation; each requires reading the whole view to know if
anything needs attention. **Not proposing to bolt this onto every view
mechanically** (that would be scope creep the task brief warns against) --
noting it as a good existing pattern worth reusing *if and when* the user
wants a similar at-a-glance summary for, say, the List/claims view specifically.

---

## Summary table

| # | Finding | Bucket | Effort | Status |
|---|---|---|---|---|
| Done-1 | Queue priority + stale-claim chips (client-side) | b | trivial | **Landed** |
| 1 | `priority`/`claimed_by` dropped in `_queue_items_from_raw()` | b | small | Proposed -- top priority |
| A1 | No sort control on List view | a | small | Proposed |
| A2 | Queue not sorted/shown by priority | a | small (blocked on #1) | Proposed |
| A3 | "Current epoch only" filter missing from List | a | small | Proposed |
| A4 | No "has conflict" filter | a | trivial-small | Proposed |
| A5 | Experiments > Completed sort | a | -- | Already fine |
| B2 | Stale TASK_CLAIMS / orphaned stashes not computed server-side | b | needs-design-discussion | Proposed (bigger than it looks) |
| B3 | Closure load-bearing counts | b | -- | Out of scope (separate file) |
| B4 | Nav-badge vs corner-dock convention | b | -- | Documented, no action needed |
| B5 | Pending-review badge doesn't deep-link | b | small | Proposed |
| C1 | No dark mode | c | needs-design-discussion | Proposed |
| C2 | Inline hex colors vs CSS vars | c | needs-design-discussion | Proposed |
| C3 | "More" menu accretion | c | needs-design-discussion | Proposed |
| C4 | Docs picker is a 70-item select | c | small/needs-design-discussion | Proposed |
| D1 | List table has no pagination | d | small | Proposed |
| D2 | Mobile/responsive | d | -- | Already fine |
| D3 | Governance's priority pane as a reusable pattern | d | -- | Noted, no action proposed |

**No unrelated bugs were found** during this review (everything above is a UX
gap or a design-consistency observation, not a correctness defect), so no
separate chip was needed for out-of-scope issues.
