# Scoping note: a standing audit for skill-improvement candidates

Status: **scoping only, not built.** Registered 2026-08-01. No TASK_CLAIMS entry needed to read
this; open one against this path before editing it.

## Origin

A session compared the last 10 confirmed `/failure-autopsy` artifacts against a pilot of 10
recent clean PASSes, close-reading manifest + driver + claims.yaml for each. Roughly half of
`learning_extracted` items across the FAIL sample are **non-outcome findings** — reusable code
bugs, schema-legibility gaps, stale cross-referenced docs, methodology/statistic caveats — not
diagnosis of the specific result. The PASS pilot found the same class of finding exists in clean
PASSes too (1-2 of 6 closely read), but only surfaces when the driver source is actually opened,
which nothing currently forces for a clean PASS.

Two concrete findings from that session were folded directly into skill checklists the same day:

- `/queue-experiment` Step 3.5 gained three pre-run checks (combination-logic legibility,
  floor-clamp risk, config-branch parity + decisive-readout smoke assertion extended to
  `evidence`-purpose scripts) — commit `b793056`.
- `/governance` Step 2b gained a "open the driver, not just the manifest" prompt for clean PASSes
  — same session.

Both of those were single-incident additions, added because a human was watching in real time and
judged them worth it immediately. That is not a standing process — it doesn't run again on its
own, and doesn't scale past what one session happens to notice. This note scopes what a *standing*
version would need, without committing to build it yet.

## The pattern to reuse, not invent

This repo already has the exact shape needed, twice: **GOV-GRAN-1** (granularity-debt recurrence)
and **GOV-CAT-1** (missing epistemic-category completeness) are both a *reactive* trigger a human
check fires inline, backed by a *standing* corpus-wide sweep script that catches what the reactive
trigger misses. Both are threshold-gated (don't act on one occurrence), both are WARN-only /
read-only (never auto-edit the governed artifact), and both report their own coverage rather than
silently under-claiming. Scoping "audit skills for improvement candidates" is instantiating that
same pattern one level up — auditing the *checklists themselves*, not the claims — not designing
something new.

## Corpus: already exists, nothing new to build here

Checked before writing this note (see the parent session's finding): there is **no new artifact
type needed**.

- `REE_assembly/evidence/planning/failure_autopsy_*.json` — `targets[].learning_extracted[]` is
  already structured, per-target free text. 294 confirmed files as of 2026-08-01.
- `REE_assembly/evidence/experiments/review_tracker.json` — `review_log[].context` and
  `discussion_notes[]` are durable, timestamped, free-text prose per governance cycle, covering
  PASSes too (not just FAILs). Less structured than `learning_extracted` (per-cycle blob, not
  per-run array) but real and already accumulating, especially now that governance Step 2b prompts
  for driver-level PASS findings.

Both are read-only inputs to whatever mines them. Neither needs a schema change to start.

## Open design decisions (in priority order — the first is the one worth resolving before anything else)

1. **Recurrence threshold before a finding becomes a checklist proposal.** Mirror
   `RE_DERIVE_BRAKE_THRESHOLD` (default 2): one occurrence is a note, N occurrences across
   independent runs/sessions is a candidate. Today's two additions were made on N=1 each, which is
   below the bar this repo otherwise holds itself to elsewhere. Pick N (probably 2, matching the
   existing convention) and decide whether severity can substitute for count (a single
   high-generality finding vs. two low-generality ones).

2. **Detection mechanism.** Given this repo's convention — deterministic scripts for standing
   scans, LLM judgment reserved for where it's load-bearing — the natural shape is a periodic LLM
   sweep over autopsy/`review_log` entries *since the last sweep* (pointer-based, mirroring how
   `check_granularity_debt_recurrence.py` avoids full-corpus rescans), clustering by finding type
   and flagging clusters that cross the threshold. A pure-keyword/heuristic version (what this
   session did by hand for n=10) is cheaper but brittle — free text doesn't tag itself by finding
   category the way `evidence_direction` does.

3. **Propose, don't auto-apply.** A checklist candidate should land as a chip/proposal a human
   reviews before it edits a skill file — skills are shared, high-blast-radius, every-future-
   session files. What happened this session (live edit, same turn) only worked because the user
   was watching and could immediately correct a bad addition; a standing scan running unattended
   does not have that safety net.

4. **Bloat is the concrete risk, not a hypothetical one.** This repo already names the failure
   mode elsewhere — the worktree-skill-staleness audit explicitly discusses staying "the right side
   of the banner-everyone-skips line." `/queue-experiment` Step 3.5 is already ~100 lines a human
   is asked to read "end-to-end" per script. An accretion-only trigger makes the checklist
   eventually unreadable and self-defeating. Any standing audit needs a **pruning/consolidation**
   counterpart from day one — e.g. periodically asking "which Step 3.5 items have fired zero times
   in N months of authored scripts" — not just a growth mechanism. This is arguably the single
   biggest reason not to build the accretion half first without the pruning half designed
   alongside it.

5. **Effectiveness feedback loop.** Once a checklist item is added, track whether the pattern it
   was written for actually stops recurring in scripts/PASSes authored after that date. Testable
   and falsifiable, consistent with how this repo audits everything else it builds — and it's the
   only honest way to tell a genuinely load-bearing checklist item from one that read well in the
   moment but never fires again.

## What this note is NOT proposing

Not a new artifact schema (corpus already exists). Not an automated skill-editing pipeline (item 3
above rules that out by design). Not a broadening of `/failure-autopsy` to run on every PASS (the
prior conversation in this thread already reasoned through why that's the wrong shape — cost
without matching the failure-diagnosis machinery to a PASS's actual needs).

## Recommended next step, if this gets picked up

Smallest reversible probe: a one-off manual sweep (not a standing script yet) of all 294 confirmed
`failure_autopsy_*.json` files' `learning_extracted[]`, clustered by finding type, to see whether
recurrence (>=2 independent incidents of the *same* underlying pattern) is common enough to justify
building the standing scan at all. If most non-outcome findings turn out to be one-off and never
recur, the standing-audit machinery isn't worth building — the reactive path (a human folding a
finding into a checklist when they happen to notice, as this session did twice) may already be
sufficient. Decide that before writing any script.
