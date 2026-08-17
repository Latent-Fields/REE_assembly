# `/metaworker-support` sister skill — design research + split recommendation

**Status: AWAITING USER REVIEW -- no skill file has been created yet.**
Chip: `chip-20260817-metaworker-support-skill-design`. Researched and drafted 2026-08-17 by
headless session `github-write-access-setup-88d6ec` (worktree
`.claude/worktrees/github-write-access-setup-88d6ec`). This is a research + design artifact
only, per explicit user instruction to settle the split question before any build. A decision
chip (`chip-20260817-metaworker-support-split-decision`, see bottom of this doc) presents the
open question to a live mediator session; no skill directory has been created.

---

## 0. The ask, in one paragraph

The user wants a sister skill to `/metaworker-dispatch` that monitors the two dispatch surfaces
(interactive Mac, ree-cloud-5's resident systemd timer) and their shared coordination state
(`TASK_CHIPS.json`, `TASK_CLAIMS.json`, `WORKSPACE_STATE.md`, umbrella git health), diagnoses
problems, fixes small ones directly, turns *repeated* problems into durable tooling/doc changes
rather than one-off patches, gates high-risk/high-impact/high-token-spend work behind a real
decision, and saves its own context via subagents. The user explicitly asked whether one skill
is right or whether a split (they suggested `/metaworker-repair`, `/metaworker-learning`,
`/repo-development`, or "some other division") is cleaner, and asked for that question to be
raised before any build.

---

## 1. Research findings

### 1a. metaworker-dispatch/SKILL.md is already a living incident log

The skill (2140 lines) contains roughly two dozen dated, quantified incident write-ups spanning
2026-08-02 through 2026-08-15 — dispatcher collision near-misses, a zsh glob-abort bug, a
2-theory-refuted queue-entry erasure mystery, a false-positive misdiagnosis written into the
ledger as fact, five vanished headless workers that produced the "never end turn to await an
async event" rule, a measured classifier-block base rate (41/10,718 Bash calls, 0.38%,
concentrated in destructive-shaped commands), an untracked-file permanent-loss incident that
produced the "commit + push before resolving" rule, and condition 5 itself (below). Several
entries explicitly record a CLAUDE.md-mandated held-out check *changing* the shipped rule
(SKILL.md:1194-1196, 1216-1225, 2036-2043) — this is exactly the "session hits a problem, writes
it up, sometimes formalizes it" loop the user's ask names as currently opportunistic rather than
owned by any skill (CLAUDE.md "the durable machinery from learning pattern... only as a passive
byproduct").

**This is the single strongest piece of evidence for what `/metaworker-support`'s hardest job
actually is**: not detecting problems (mostly already automated, see 1c) but *recognizing when a
problem has recurred enough to deserve durable machinery, and building that machinery under
real consent* — the thing every one of these SKILL.md entries did by hand, incident by incident,
with no owning process.

### 1b. Condition 5 — the existing consent-gate precedent to mirror

SKILL.md:1611-1616 (Step 4c, sixth of six dispatch pre-checks), quoted:

> "If the chip's `prompt` directs the session to run `/implement-substrate` (or otherwise
> instructs inserting/modifying `ree_core` substrate code), do NOT headless-dispatch it --
> regardless of its recorded `kind` or `origin`. Route it through the SAME real-consent
> mechanism as Step 5's decision lane for THIS cycle instead: a mediator raises a real
> `AskUserQuestion` ... what would be built, what file(s), the plan, options covering proceed /
> constrain / hold ... a headless resident batch-reports it per Step 5c and does not dispatch."

It exists because `kind: "work"` alone doesn't catch substrate-insertion work mislabeled as
routine (confirmed bypass, SKILL.md:1640-1663: `/governance` spawned two `kind: work` chips that
wrote 686 lines of new `ree_core` substrate headlessly with zero human ever seeing a plan,
caught by accident). Trigger is deliberately broad — false-negative cost (unconsented code)
judged worse than false-positive cost (an extra question).

**Decision-chip content bar** a mediator's `AskUserQuestion` must clear (SKILL.md:1834-1844):
what skill/file(s) would be touched, a plain-English paragraph of the actual change (not a bare
`tldr`), the duplicate-check result if any, and named options covering at least
launch-now/withdraw/hold-and-decide-later. The worker-authored chip prompt itself needs "the
whole question, self-contained: what was found, what the options are, what each would cost, and
what this worker recommends" (SKILL.md:146-149) plus the literal `[chip_ref: ...]` marker.

The decision chip at the bottom of this doc is built to this bar, not a bare summary.

### 1c. hygiene_routine_tick.py already owns the cheap, frequent monitoring loop

`scripts/hygiene_routine_tick.py` wraps 9+ read-only audits (`audit_stale_claims.py`,
`audit_stashes.py`, `audit_vendored_copies.py`, `audit_worktree_skills.py`, plus its own
NOT-LANDED scan, metaworker-worktree GC scan, `substrate_queue.json` write-back-drift scan,
chip-ledger integrity scan, ref-convergence wedge-detection scan, staged-revert-skew scan, and
stranded-work scan) and turns their actionable findings into `kind: "work"` chips. It runs as
**Step 2 of every `/metaworker-dispatch` cycle** (SKILL.md:478, `hygiene_routine_tick.py
--push`) — cadence is whatever the dispatch cycle runs at, not an independent cron.

Measured against the live `TASK_CHIPS.json` (875 chips total): **95 `origin: "hygiene_tick"`
chips**, 76 done / 16 open / 3 withdrawn, across 11 categories — GC candidate (47), stale-claim
review (15), stranded uncommitted work (11), `substrate_queue` status drift (6), chip-ledger
integrity (5), NOT LANDED (3), ref-convergence wedge *detection* (3), vendored-copy drift (1),
staged-revert skew (1), rebase-state finding (1), IGW workset staleness (1). This machinery is
proven, cheap (all local git/file operations, no SSH, no network beyond the final push), and
already scheduled — it should not be duplicated.

**Confirmed gaps — problem classes with NO hygiene_tick coverage today**, cross-checked against
`TASK_CHIPS.json` titles for `classifier|deferral|safe_adopt_ref|refwedge|clinical.hours`:

1. **Classifier-block / kill-vs-deferral scanning is entirely reactive.** `check_deferral_exit.py`
   exists, correctly classifies a dead worker's transcript (DEFERRAL-EXIT / GENUINE-KILL /
   CLASSIFIER-BLOCK / USAGE-LIMIT / SELF-RESOLVED / COMPLETED-UNRESOLVED / INDETERMINATE, and
   after 2026-08-15 correctly separates 1120/2243 previously-INDETERMINATE transcripts into
   USAGE-LIMIT), but nothing runs it proactively/fleet-wide. Every fix chip for this class in
   `TASK_CHIPS.json` is `spawn_task`/`headless` origin — a human or session noticed by hand.
2. **Clinical-hours / commit-guard authorship-correctness bugs have no scan.** E.g. the
   confirmed detached-HEAD false-negative in `pre-push.local`'s bot-authorship exemption check
   (being fixed by sibling chip `chip-20260817-durable-fix-dispatch-grid-rescue-tooling`,
   currently **open/in-progress**) surfaced only because a live session hit it and self-reported.
3. **Ref-wedge detection exists; *closing* it does not.** hygiene_tick's "Ref-convergence WEDGE"
   category (3 chips) only reports that `ref_convergence.py --check` is refusing to converge —
   it does not run the per-commit content audit or grant `safe_adopt_ref.py --allow-discard`.
   That step appears as separate manually-authored `headless` chips, and the wedge recurred at
   least twice under the same title stem (`refwedge-ree-working-master-recurred-2`), each
   recurrence needing fresh manual authorization. This matches the user's own account: ~15+
   ref-wedge episodes in the motivating session, each requiring a full audit + authorization
   dance.
4. **Cross-dispatcher-cycle collision detection has no dedicated scan.** Only one artifact trace
   exists (`chip-20260809-metaworker-cycles-overlap`), caught incidentally via the chip-ledger-
   integrity category, not a purpose-built detector. Separately: **the cross-dispatcher timing-
   offset scheme the user describes (querying cloud-5's timer grid, offsetting by the midpoint)
   is not documented anywhere in metaworker-dispatch/SKILL.md at all** — confirmed by a full read
   of the file. It genuinely exists only in the motivating session's own context, which is
   exactly the gap the sibling chip `chip-20260817-durable-fix-dispatch-grid-rescue-tooling`
   (Deliverable A) is persisting. That chip is **still open** as of this writing — the
   /metaworker-support design should assume it lands independently and not re-derive it.

**Answering the user's own explicit question — should monitoring fold into
`hygiene_routine_tick.py` instead of a new skill?** Yes, for *detection*. The four gaps above are
each a new finding-source function of the same shape as the 11 that already exist (read-only
scan → idempotent chip). Extending `hygiene_routine_tick.py` with 3-4 new sources is a smaller,
lower-risk, more consistent change than standing up a parallel monitoring skill that duplicates
its scheduling, its chip-dedup logic, and its coordination-plane-pause gating. This is scoped as
a build task for whichever session answers the decision chip, not attempted here.

**No, for repair and no, for durable-fix building.** Closing a ref wedge needs a genuine
per-commit content audit and (per CLAUDE.md and every `safe_adopt_ref.py --allow-discard`
precedent) is classifier-blocked, needing live judgment — a per-cycle script cannot do this.
Building fleet-wide tooling needs the held-out-check discipline and real consent (condition 5's
whole reason for existing) — also not a per-cycle script's job.

### 1d. account-handover/SKILL.md — closest existing precedent, real but partial overlap

Single-incident skill (2026-08-15: hung `claude login`/`logout` over SSH, a push-credential
silent-failure mechanism, a hostname-drift bug undetected ~3 weeks). Reactive, not a monitoring
loop — invoked when a human is actually doing an account/credential switchover. Its
**human-task-only section keys on the *action*, not on a settings.json permission list**
(SKILL.md:150-164): (1) the ref-move itself (`safe_adopt_ref.py --allow-discard`, classifier-
refused; `--dry-run` allowed — "agent dry-runs and prints the exact command, a human runs it"),
(2) editing `.claude/settings.json` (deliberately human-gated beyond what the classifier
technically requires), (3) adjudicating a `unique_work_present` verdict on a stranded claim.

**Real, named overlaps** with a prospective `/metaworker-support`: push-credential
silent-failure detection ("ahead-count is the credential canary, not exit code") generalizes to
any coordination-file drift-detection; structural diff by entry identity (never textual, never
by commit count) is directly reusable for any `TASK_CLAIMS.json`/`TASK_CHIPS.json` repair;
rescue-stranded-entries-structurally (append missing entry from origin's copy, never a blind
`git checkout --`) is the exact repair pattern a ref-wedge-closing skill needs; the "provisioning
gotcha" (a dormant hook activating on adopt) is a machinery-integrity check of the same shape.

**Recommendation: stays a clean sibling, cross-referenced, not absorbed or superseded.**
account-handover is scoped to account/credential/auth switchover specifically (OAuth mechanics,
billing-pool selection, hostname canonicalization — none of which a coordination-machinery-repair
skill needs to own). The new skill should reuse account-handover's structural-diff and
rescue-not-revert techniques (cite it, don't reimplement it) but trigger off a different signal
(a hygiene_tick finding or an ad hoc anomaly report, not "a human is switching accounts").

### 1e. session-land/SKILL.md — the housekeeping precedent already resolves the duplication question

The Headless variant *explicitly skips* stash audit, vendored-copy audit, stale-claim
prune/reap, and worktree-skill audit — "because these four are already covered fleet-wide by
`hygiene_routine_tick.py` on a tighter cadence... duplicating adds write contention on
`TASK_CLAIMS.json`/`TASK_CHIPS.json` for no marginal coverage" (session-land/SKILL.md:~150-165).
This is the same reasoning applied above in 1c and confirms the design direction: any new
skill's monitoring half should defer to hygiene_tick, never re-scan the same ground.

Phase 3's chip-spawning rule is unambiguous and, per CLAUDE.md, a **closed exception list**:
"chip everything except `/governance` work and `/failure-autopsy` work," because those two
"re-derive their own worklist every cycle" from a self-refreshing, disk-truth artifact
(`pending_review.md` regenerated fresh every invocation). **A prospective `/metaworker-support`
does not automatically qualify for this exception** — it would need its own genuine
self-refreshing-worklist mechanism (which `hygiene_routine_tick.py`'s idempotent chip-dedup
arguably already provides for the *detection* half) and its own held-out justification before
CLAUDE.md's exception list is widened to include it. **This design does not propose adding a
third skill to that list**; whoever builds this should treat new-skill follow-on work under the
ordinary chip-everything-else default unless a later, separately-justified change says otherwise.

### 1f. failure-autopsy/SKILL.md — the re-derive-brake pattern is the right shape for "durable fix from recurrence"

Scoped specifically to completed experiments (FAIL / diagnostic outcomes) — not crashes, not
machinery failures — so there's no scope overlap with a machinery-support skill. But its
**MOVE-3 "re-derive brake"** (SKILL.md:264-337, 680) is precisely the escalation shape the user's
ask names: on the Nth (`RE_DERIVE_BRAKE_THRESHOLD`, default 2) `substrate_ceiling`/
`non_contributory` reading for the *same claim*, it is a **hard gate, not a suggestion** — route
to a durable build (`/implement-substrate`) and **explicitly refuse** another same-question
re-queue, with the counting convention (R1-R3) itself arrived at only after three sibling
sessions independently invented divergent counting rules on the same day and had to be
reconciled. Producer (`failure-autopsy`) and consumer (`/queue-experiment` Step 2.5, which
enforces the refusal) are split.

**This is the design pattern `/metaworker-learning` (below) should mirror**: count occurrences
of the same *problem class* (not experiment claim) across repair-chip resolution notes, and on
the Nth occurrence, hard-gate against "just patch it again" and route to durable-fix design +
consent instead. The brake's own history (arrived at only after a live counting disagreement)
is itself evidence that this counting convention needs to be worked out deliberately, not
assumed — flagged as an open design detail below, not resolved here.

### 1g. No existing in-session subagent-delegation pattern in this skill family

metaworker-dispatch is single-threaded within each dispatcher role. Its whole model of
"delegate work" is spawning independent **child OS processes** (headless `claude -p` via
`nohup`, one per dispatched chip/worktree), governed by `chip_ledger.py`/`TASK_CLAIMS.json`, not
in-session `Agent`-tool subagent calls. Zero `Agent`/`Task` tool usage anywhere in the 2140-line
file. **If `/metaworker-support` (in whatever split) wants genuine in-session subagent
delegation for its own context economy, that is a new pattern for this skill family**, not a
reuse of an existing one — worth naming explicitly rather than assuming precedent exists.

Concretely, **this very design session is the worked example**: 4 parallel `Agent`-tool research
agents (metaworker-dispatch incident extraction, account-handover/session-land/failure-autopsy
overlap, diagnostic-script survey, hygiene-chip coverage survey) fed one synthesized design doc,
exactly the shape a `/metaworker-learning`-type skill would need for its own "mine past
incidents across a 2000+ line skill file, an 875-chip ledger, and CLAUDE.md's very long
Concurrency Rules section" research phase.

---

## 2. The split question

### Option A — Monolithic `/metaworker-support`

One skill: monitor, diagnose, fix small things, build durable fixes, gate on consent, all in one
flow.

**Against:**
- **Cadence mismatch.** Monitoring is (or should be, per 1c) a cheap ~5-minute-cadence scan;
  durable-fix-building is rare, expensive, and needs deep multi-file research (1g). One skill
  invoked at one cadence structurally cannot serve both well — either the cheap path gets bloated
  with rarely-needed durable-fix machinery, or the durable-fix path inherits a monitoring-loop's
  thin, single-shot framing.
- **Permission-shape mismatch.** Routine monitoring needs zero consent; small fixes need little;
  fleet-wide tooling/doc changes need CLAUDE.md's held-out-check discipline *and* a real decision
  chip (1b, 1f). A single skill would need very different guard rails active depending on which
  sub-task it's doing at a given moment — a design smell the user's own ask names explicitly.
- **Duplicates hygiene_routine_tick.py's monitoring job** (1c, 1e) unless carefully scoped to
  avoid it, which argues for keeping monitoring separate from the skill entirely.

### Option B — User's suggested split: `/metaworker-repair`, `/metaworker-learning`, `/repo-development`

As offered by the user, three skills matching: reactive fixing, recurrence-driven durable-fix
building, and general repo-development work.

**Assessment of the third leg, `/repo-development`:** research found **no existing concept**
this maps onto — not `/update-docs` (docs-focused), not `/governance` (claims/governance-focused).
Its natural content (drafting + landing a scripts/skills change) is *already* the second half of
what `/metaworker-learning` would do (design the durable fix, get consent, build it). Splitting
that build step into its own skill adds an extra hand-off with no clear boundary — what
distinguishes "a `/metaworker-learning`-recommended fix" from "general repo-development"? Nothing
identified in this research. **Recommend folding this into `/metaworker-learning`'s scope rather
than standing it up separately.**

### Option C — Recommended: two skills, plus extending existing machinery, not three new ones

- **Extend `hygiene_routine_tick.py`** with the four new finding-source categories from 1c
  (classifier-block/deferral scan, clinical-hours/guard authorship-correctness check, ref-wedge
  *age/recurrence* tracking, cross-dispatcher-collision detection). Not a new skill — a
  same-shaped addition to existing, proven, already-scheduled machinery. This is the answer to
  the user's own "maybe foldable into hygiene_routine_tick.py" question: **yes, for detection.**

- **`/metaworker-repair`** (new skill, reactive shape mirroring account-handover, 1d): invoked
  either manually or auto-dispatched off a hygiene_tick finding that needs judgment to *close*
  (not just detect) — ref-wedge authorization, classifier-block-triggered stranded-work rescue,
  clinical-hours guard bug fixes, cross-dispatcher-collision remediation. Small, low-risk fixes
  proceed directly; anything matching condition 5's shape (touches shared `scripts/`,
  `.claude/settings.json`, git hooks, or needs privileged host access) raises a decision chip
  per the 1b content bar instead of silently attempting it. Cross-references account-handover
  for shared technique (structural diff, rescue-not-revert) without absorbing its scope.

- **`/metaworker-learning`** (new skill, rare/high-judgment shape mirroring failure-autopsy's
  re-derive brake, 1f): fired when the same problem class recurs past a threshold (mirrors
  `RE_DERIVE_BRAKE_THRESHOLD`) — either a human notices, or `/metaworker-repair` itself flags a
  repeat. Mines the incident history already embedded in metaworker-dispatch/SKILL.md,
  `TASK_CHIPS.json` resolution notes, and `WORKSPACE_STATE.md` (via parallel subagents — 1g),
  drafts a durable-fix design against CLAUDE.md's held-out-check discipline, and **raises a
  decision chip before landing anything that touches shared fleet-wide machinery** — exactly the
  process this very research task followed. Absorbs the "build the durable fix" work Option B's
  `/repo-development` would have owned, since there's no daylight between them.

**Why two new skills rather than one covering both repair+learning:** the cadence and
permission-shape arguments against Option A apply with equal force to a repair+learning
merger — repair is frequent/small/often-unsupervised-safe, learning is rare/large/always-consent-
gated. They also cleanly satisfy the subagent-separability requirement (1g, user's own stated
constraint): each is independently a well-bounded delegation target — `/metaworker-dispatch`
could dispatch a repair chip to one, a learning chip to the other, and each could itself fan out
subagents internally for its own research/diagnosis phase without the other's very different
consent posture leaking in.

---

## 3. Recommendation

**Ship Option C**: extend `hygiene_routine_tick.py` with the four new detection sources (no new
skill), and build two new skills — `/metaworker-repair` and `/metaworker-learning` — not three,
folding the user's suggested `/repo-development` into `/metaworker-learning`'s build phase.

### 3a. `hygiene_routine_tick.py` extension (not a skill — a scripts/ change)

- **Reads:** worker transcripts under `~/.claude/projects/` (via `check_deferral_exit.py`,
  batch mode over recently-dispatched chip session_ids), `scripts/git-hooks/pre-push.local`
  execution state, `ref_convergence.py --check` output (already wired), chip
  `spawned_at`/`claimed_at` timestamps across both dispatch surfaces.
- **Touches unsupervised:** nothing beyond the existing pattern — writes idempotent `kind: work`
  chips only, same as its 11 existing sources. No new consent surface needed; this is strictly
  additive detection.
- **Invocation:** automatic, inherits Step 2 of every `/metaworker-dispatch` cycle. No separate
  scheduling.
- **Build note:** this itself is a `scripts/` change touching fleet-wide-shared machinery, so
  building it should go through whatever the resolved split recommends for `/metaworker-repair`
  or `/metaworker-learning`'s own consent posture — or, if built before either skill exists, a
  plain decision chip in the existing style. Not attempted in this design session.

### 3b. `/metaworker-repair`

- **Reads:** open hygiene_tick findings (the 4 new categories + relevant existing ones like
  ref-convergence-wedge), `TASK_CHIPS.json`/`TASK_CLAIMS.json` current state, the diagnostic
  scripts from 1c/research (never reimplements them — orchestrates `check_deferral_exit.py`,
  `ref_convergence.py --check`, `safe_adopt_ref.py --dry-run`, `audit_hook_gating.py`).
- **Allowed unsupervised:** narrow claim/chip-ledger repairs via `task_claim.py`/
  `chip_ledger.py` (which have their own arbitration safety), structural rescue of stranded
  entries (account-handover's pattern), running any diagnostic script in read-only/`--dry-run`
  mode, closing out a hygiene_tick finding once genuinely resolved.
- **Needs a decision chip (condition-5-shaped):** `safe_adopt_ref.py --allow-discard` (the actual
  ref move — already established as needing a live per-commit audit), any edit to
  `scripts/git-hooks/*` or `.claude/settings.json`, anything requiring privileged host-local
  `sudo` on cloud-5 (mirrors the stalled `metaworker_cycles_overlap_flock_fix` precedent — a
  human-task-only action by the classifier's own design, not a gap to route around), any fix
  estimated to cost more than a small, bounded token budget.
- **Invocation:** manual, or auto-dispatched as a `kind: work` headless chip when a
  hygiene_tick finding in one of the four new "needs judgment to close" categories fires —
  reuses the existing chip-dispatch machinery rather than inventing new scheduling.
- **Subagents:** optional, for parallel diagnosis on a single incident (e.g., checking ref state
  and claim state simultaneously) — not structurally required the way `/metaworker-learning`'s
  research phase is.

### 3c. `/metaworker-learning`

- **Reads:** metaworker-dispatch/SKILL.md's incident history, `TASK_CHIPS.json` resolution notes
  for the recurring problem class, `WORKSPACE_STATE.md`, CLAUDE.md's Concurrency Rules section
  (as prior-art for the held-out-check discipline it must itself follow).
- **Allowed unsupervised:** drafting a design doc (exactly this artifact's own shape —
  `evidence/planning/<slug>_staged_<date>.md` headed AWAITING USER REVIEW), running the
  ≥3-historical-case held-out check CLAUDE.md already mandates for any standing-rule change.
- **Needs a decision chip:** landing any change to shared `scripts/`, `.claude/skills/`,
  `.agents/skills/`, or CLAUDE.md itself — no exception. This is condition 5's exact shape
  applied to meta-machinery instead of `ree_core` substrate, and this document is itself an
  instance of the rule it's proposing.
- **Occurrence-counting convention:** an open design detail, not resolved here — failure-autopsy's
  own R1-R3 convention (1f) needed real reconciliation work after three sessions independently
  disagreed; whoever builds `/metaworker-learning` should expect the same and budget for it
  rather than assuming a threshold trivially falls out of the chip ledger's existing fields.
- **Invocation:** manual (a human notices recurrence) or triggered by `/metaworker-repair`
  flagging a repeat via a decision chip (mirroring MOVE-3's producer role) — never auto-dispatched
  headlessly for the build phase.
- **Subagents:** structurally required for its research phase — this design session is the
  worked example (1g).

### 3d. Explicitly out of scope for this design

- No skill file is created in this session (per the user's own instruction).
- The `hygiene_routine_tick.py` extension is scoped, not built.
- The occurrence-counting threshold for `/metaworker-learning`'s recurrence gate is named as an
  open question, not resolved.
- Whether `/metaworker-repair`/`/metaworker-learning` should join CLAUDE.md's `/governance`+
  `/failure-autopsy` chip-exception list is explicitly **not** proposed (1e) — left to a future,
  separately-justified change if it turns out to be needed.

---

## 4. Sources

- `.claude/skills/metaworker-dispatch/SKILL.md` (2140 lines, full read)
- `.claude/skills/account-handover/SKILL.md` (221 lines, full read)
- `.claude/skills/session-land/SKILL.md` (879 lines, full read — Headless variant + Phase 3)
- `.claude/skills/failure-autopsy/SKILL.md` (682 lines, full read)
- `scripts/check_deferral_exit.py`, `ref_convergence.py`, `safe_adopt_ref.py`,
  `audit_stashes.py`, `audit_vendored_copies.py`, `dev-doctor.sh`, `audit_stale_claims.py`,
  `audit_worktree_skills.py`, `audit_hook_gating.py`, `hygiene_routine_tick.py` (surveyed)
- `TASK_CHIPS.json` (875 chips, queried structurally — not read whole)
- `CLAUDE.md` Concurrency Rules section (already in session context, cited throughout)
- Sibling chip `chip-20260817-durable-fix-dispatch-grid-rescue-tooling` (read in full; **status:
  open** as of this writing — this design assumes it lands independently)
