# Claude Code prompt audit -- Fable 5.1 retune (WI-A)

**Generated:** 2026-09-14T06:57:40Z
**Work item:** WI-A of `REE_assembly/evidence/planning/claude_code_update_integration_plan.md`
**Target model:** Claude Fable 5.1 in Claude Code (the 2026-09-11 changelog: Fable 5.1 is "more eager
than Fable 5 ... you may need to tone down prompts and CLAUDE.md instructions written for older models").
**This file edits nothing.** It is the measurement half of the plan; WI-B/B2 is the rewording pass, and
GOV-HELDOUT-1 applies to every edit it lands.

## Method -- skill-guided

`/claude-api prompt-audit` was invoked via the Skill tool and **did** load. It routed to
`shared/prompt-audit.md` in the bundled `claude-api` skill, which was read in full and used as the
primary rule set. Findings are therefore classified by that guide's anti-pattern groups:

| group | what it catches |
|---|---|
| **1a** | Pressure language -- stacked emphasis whose markers have stopped carrying information |
| **1b** | Scaffolds replaced by API features ("think step by step", progress cadences, word caps) |
| **1c** | Over-specification -- step choreography for judgment tasks, repetition-as-reinforcement, strategy coaching |
| **1d** | Fossils -- model-version workarounds, migration-relative phrasing, patch accretion, unenforced rules |
| **1e** | Prohibition clusters -- judged line-by-line **by provenance**, not by whether the model "needs" the guardrail |
| **1f** | Output-shaping choreography -- interim-update cadences and numeric ceilings, removed together |
| **2** | Brittle skill files -- verbosity, wrong degrees of freedom, volatile specifics, history narratives |
| **3** | Tool/skill descriptions -- where the guide's direction is often *add*, not trim |
| **4** | Request config -- not applicable to markdown rule files |

The parent brief's fallback letters (a)-(g) are reported alongside as a second column value, so both
vocabularies resolve. Where a row carries two, both are given (`1a / (a)(b)`).

**The guide's keep list was applied as binding, and it changed outcomes.** Three of its items did most of
the work here: *fragile operations keep exact scripts* (which protects nearly all of the `ree_commit.py`
/ `safe_adopt_ref.py` / HEAD-worktree-skew material in `CLAUDE.md` from being flagged at all);
*prohibitions against current, demonstrated failures stay*; and *working redundancy is not cruft --
propose deduplication only when the duplicates actually **disagree***. That last one is why `AGENTS.md`
is the headline finding and why most cross-file overlap elsewhere is **not** flagged.

**The REE-specific overlay, per the plan's own "why the last column matters":** most emphatic wording
here is incident-derived and carries an `A-nn` (umbrella) or `B-nn` (skill) archaeology pointer. For
those, *tone down* means removing intensity and redundancy, **never the rule**. Every row therefore
carries a **RULE CONTENT THAT MUST SURVIVE** column, and `none -- pure intensity` appears only where the
fragment genuinely carries no rule.

### Scope covered (all five, in plan order)

| # | scope | size | rows |
|---|---|---|---|
| 1 | `/Users/dgolden/REE_Working/CLAUDE.md` | 133,405 chars / ~33,350 tok | 17 |
| 2 | the four >100 KB skills | 526,013 chars / ~131,500 tok | 100 |
| 3 | `ree-v3/CLAUDE.md` + `REE_assembly/CLAUDE.md` | 107,602 chars / ~26,900 tok | 13 |
| 4 | `AGENTS.md` + `NEW_AGENT_START_HERE.md` | 23,378 chars / ~5,840 tok | 10 |
| 5 | headless briefs (DISPATCH_BRIEF template; IGW `spawn_claude()`) | see scope 5 | 6 + 6 cross-listed |

Scope 2 was audited by four parallel Opus subagents, each given the same criteria brief and each
required to read its whole file in chunks; their line citations were spot-checked against the files
before inclusion.

---

# Scope 1 -- `/Users/dgolden/REE_Working/CLAUDE.md`

133,405 chars, ~33,350 tok, 1,155 lines. **Loaded into every session in this workspace**, so a token
here is the most expensive token in the audit.

Measured density: **375 bold spans**, 87 `never`, 28 `must`, 59 `do not`/`don't`, and **51
`Background -- A-nn` archaeology blocks totalling 17,420 chars (~4,350 tok, 13% of the file)**. Hard
ALL-CAPS imperatives are comparatively rare (`NEVER` x2, `MUST` x7, `ALWAYS` x0) -- **the emphasis in
this file is carried by bold, not by caps**, which matters because the guide's own suggested
caps-density grep reports this file as clean when it is not.

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| CLAUDE.md | 349-1069 (51 blocks) | "(not needed to follow the rule, read it before changing it)" -- repeated verbatim 49 times | 1c / (b) | State the convention once under a `## Background pointers` heading and reduce each block to `> A-nn -- <topic> (~N tok)`. | Every rule keeps a resolvable pointer to its own `A-nn` file and that file's token cost, so a session changing the rule can still find its provenance. | the apparatus itself |
| CLAUDE.md | 666 | "**CHIP EVERYTHING ELSE.** All other next-step work gets a chip, including work that a `/governance` or `/failure-autopsy` artifact *points at*" | 1a / (d) | "Chip all other next-step work, including work a `/governance` or `/failure-autopsy` artifact points at but does not perform." | The exception list is exactly two work-types; everything else is chipped, including work merely named by an autopsy. | A-34, A-35 |
| CLAUDE.md | 658 | "**A governance session is a NEXUS and SHOULD spend time spawning lots of work** -- its walk, agenda, and audits are a high-yield source" | 1a / (d) | "Governance sessions are a high-yield source of chippable follow-on; being in one is not a reason to inline it." | Session-type never licenses inlining follow-on; work-type decides. | A-34 |
| CLAUDE.md | 1063 + 1068 | "Do not re-enable the hub heartbeat git writer or its liveness tick" -- stated twice, five lines apart | 1c / (b) | Keep the bulleted prohibition at 1068 and delete the trailing clause of 1063, which already lists the live sources. | The hub heartbeat git writer and its liveness tick stay off; the three live sources are the only ones. | A-93 |
| CLAUDE.md | 98, 380, 391 | "never hand-edit either file, anywhere" / "use the helper, not a hand-edit" / "Never hand-edit `TASK_CLAIMS.json` to do this" | 1c / (b) | State it once at 98 and let 380/391 say only "via `task_claim.py`" without re-arguing the prohibition. | The DB is authoritative, a git-side edit is overwritten by the next render, and a blocking `PreToolUse` hook enforces it. | A-66, A-57 |
| CLAUDE.md | 123, 237, 307, 377, 427, 670, 1063, 1068, 1069 | nine separate "Do NOT re-propose / re-broaden / re-enable / re-install / build tooling for" blocks | 1c / (f) | Collect them under one `## Closed on measurement -- do not re-propose` list of one line each plus its `A-nn`, keeping the mechanism sentence only where the prohibition is non-obvious. | Each item's *reason* (why it was closed, and on what measurement) must survive somewhere reachable -- these are the rules most likely to be "helpfully" re-litigated by an eager model. | A-12, A-20, A-26..A-29, A-34, A-93 |
| CLAUDE.md | 293 | "Never mark a todo item, task, or todo list complete until the actual output/artifact has been verified -- re-check every item (including TodoWrite lists)" | 1c / (c) | "Mark a task complete only when you have seen the artifact it produces; an unrun smoke test or unwritten file means not done." | Completion requires an observed artifact, not an inference -- this is the rule, and it stays. | -- |
| CLAUDE.md | 303 + 307 | "MANUAL DISCIPLINE, deliberately NOT tooling" ... then four lines later "Keep it manual: do NOT build tooling, a hook, or a gate for this check" | 1a / (b) | Drop the heading's "MANUAL DISCIPLINE, deliberately NOT tooling" and keep the single explained sentence at 307. | The held-out check stays manual because rule-editing has no mechanical definition of "correct call"; 3 cases, non-degenerate, and a shortfall is itself the finding. | A-74 |
| CLAUDE.md | 184, 199, 213 | "check for BOTH, and note the second is the dangerous one" / "NOT equally safe to repair, and this is the part to get right" / "the quieter and worse one" | 1a / (a) | Keep one framing sentence ("`M ` is the dangerous variant: it has a working-tree version that may be live work") and drop the other two wrappers. | `D ` repair is unconditional; `M ` requires a content check against the pre-move base before any restore, and `MM` means do not restore at all. | A-10, A-11, A-68 |
| CLAUDE.md | 689-698 | "Do this BEFORE the task below, even if the resource list is a rough first guess" ... "Skipping this step is how two sessions collide unnoticed on the same file." | 1a / (a) | Trim the embedded chip prompt to the two commands plus one line of purpose; this text is re-paid in every chip prompt. | The spawned session opens its TASK_CLAIMS claim and claims the chip as its first action, before reading anything else. | A-36, A-78 |
| CLAUDE.md | 676 | "it fires the moment `spawn_task` returns, in the same turn, regardless of where in the session that happens; it is not gated on reaching this Housekeeping step" | 1c / (b) | Delete -- Concurrency Rules "Claim-first, edit-last" point 1 already states this at length and names chips explicitly. | `chip_ledger.py record` pairs with every `spawn_task` immediately, because a chip is not durable outside the ledger. | -- |
| CLAUDE.md | 121 | "Still worth running `git show --stat HEAD` after a raw-git commit, and for the queue file `git show HEAD:experiment_queue.json ...`" | 1d / (c) | "If you used raw `git`, confirm with `git show --stat HEAD`" -- the paragraph has already said the hook now blocks the failure it guards. | The recovery recipe (re-read, re-apply, validate, re-commit via `ree_commit.py`, push both) stays verbatim. | A-01, A-02 |
| CLAUDE.md | 1012 | "Always queue experiments immediately after writing the script -- never leave them unqueued." | 1a / (a) | "Queue an experiment in the same session you write its script." (Also stated in `AGENTS.md:184` and `ree-v3/CLAUDE.md:286`.) | Scripts do not sit unqueued across sessions. | -- |
| CLAUDE.md | 1020 | "**After fixing an experiment script or queue issue:** Always verify the fix by running a smoke test or dry-run ... before marking the task complete." | 1c / (b) | Delete -- line 293 (Task Completion Verification) and the `/queue-experiment` skill both already require this. | A fix is verified by a dry-run before the task is closed. | -- |
| CLAUDE.md | 819 | "always run a git commit and push to all modified repos before closing the task, unless explicitly told not to" | 1c / (b) | Delete -- the Session Land Protocol's "Definition of done" is the same rule, stated better. | Every touched repo lands on its default branch and is pushed before close. | -- |
| CLAUDE.md | 143-154 | "**Detection is now mostly automatic.**" ... "**Prevention.**" ... "Cheap up-front warning:" -- three labelled sub-blocks on one hazard | 1c / (b) | Merge into one paragraph; the three labels are organisation, not rule. | The `ree_commit.py` per-item delta is a signal not a gate; YAML is not covered; narrow structural append and per-agent temp files are the prevention. | A-05, A-06 |
| CLAUDE.md | 458 | "**Read this FIRST if your cwd is under `REE_Working/.claude/worktrees/<slug>/`**" | 1a / (a) | "If your cwd is under `REE_Working/.claude/worktrees/<slug>/`, read this section before your first edit." | The worktree contains the umbrella repo only; work repos exist only in the main checkout. | A-59 |

**Scope 1: 17 rows.** Estimated saving ~14,400 chars / **~3,600 tok**, of which ~2,600 tok is the
archaeology-block compression alone.

---

# Scope 2 -- the four >100 KB skills

## 2a -- `.claude/skills/queue-experiment/SKILL.md` (154,138 chars, ~38,530 tok, 1,573 lines)

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| queue-experiment/SKILL.md | 1000 | "**If any check fails, fix the script and re-run the whole code review pass.** Iterate until every question above can be answered correctly." | 1c / (c) | "Fix any failed check, then re-check only the items your fix could have affected before moving to the smoke test." | Step 3.5 is a gate: you may not smoke-test with a known-failed check outstanding. | -- |
| queue-experiment/SKILL.md | 881 | "A \"yes, looks fine\" without reading the relevant lines does not count." | 1c / (d) | Delete; the preceding clause ("answer each question below by inspecting the code") already states the requirement. | Each Step 3.5 question is answered by inspecting the code, not from memory of the design. | -- |
| queue-experiment/SKILL.md | 237-257 | "All three previous divergences were found by a corpus scan weeks later, never by review -- 2026-07-20 ... 2026-07-21 ... 2026-09-01" | 2 / (b) | Compress the four dated divergence stories and the self-scope caveat into one sentence plus the existing A-18 pointer, keeping the lockstep instruction and the contract-test name. | Edit all three copies of `_autopsy_counts_toward_brake` together, diffing the whole snippet (predicate AND scan) over the live corpus, in ONE commit; `test_brake_per_claim_lockstep.py` enforces it. | A-18 |
| queue-experiment/SKILL.md | 1447-1560 | a ~100-line inline python heredoc for a check that "never blocks the queue add" | 2 / (b) | Move the heredoc into `REE_assembly/scripts/plan_gap_drift.py` and leave a two-line invocation plus the interpretation note. | Step 9.5 is read-only and informational; it flags nodes by `unblocks_claims` overlap or `owner_exq` predecessor mention; plan-doc edits belong to `/inter-governance-brief` under a TASK_CLAIMS entry. | A-44 |
| queue-experiment/SKILL.md | 1397, 1445 | "### 9. Coordinator-mode health check (MANDATORY)" ... "Informational -- never blocks the queue add." | 1a / (a) | Retitle "Coordinator-mode health check (informational)" so the header stops contradicting its own closing line. | The check runs after the push and WARNs on powered-on workers with no fresh coordinator heartbeat; it never blocks the queue add. | -- |
| queue-experiment/SKILL.md | 435-466 | "A **descriptive** welfare/ethics preflight -- a doc habit, **NOT** an enforced gate (nothing computes or checks it)" | 1d / (b) | Cut Step 2.6 to three sentences and link the canonical artifact for the YAML block and the SENT thresholds. | Any non-`false` involvement flag or a `decision` other than `allow` is a V4-boundary welfare concern: STOP and route via `experiment_ethics_preflight.md` / SENT-0. | A-24 |
| queue-experiment/SKILL.md | 973-974 | "**V3-EXQ-936a** set an absolute bar **~7,900x above the maximum attainable effect** and was logged clean for **three consecutive governance cycles**" | 2 / (b) | Keep the rule and the opt-outs; move the 936a narrative and the flat-readout failure-chain story into a new archaeology note. | Every load-bearing criterion records MEASURED and THRESHOLD as separate numeric fields plus `combination_rule` when more than one; opt out per criterion via `threshold_not_applicable` or driver-wide via `CRITERIA_THRESHOLD_EXEMPT`. | -- |
| queue-experiment/SKILL.md | 184-192, 342-350 | the Step 2.5 stop-gate block appears twice, identical prose plus identical JSON template | 1c / (b) | Replace the second copy with "Apply the Step 2.5 `blocked_substrate` stop-gate, with `blocked_note:` ...". | The brake-holds path sets `status: blocked_substrate` with `blocked_by` and a re-derive-brake `blocked_note`, re-runs `build_experiment_indexes.py`, and routes to `/implement-substrate`. | A-19 |
| queue-experiment/SKILL.md | 712, 725 | "Also record generously beyond the core -- the family-keyed optional payload in standard 3c" (restated 13 lines later in more detail) | 1c / (b) | Delete the trailing sentence at 712. | Record the family-keyed optional payload by default; the burden of proof is on skipping. | A-32 |
| queue-experiment/SKILL.md | 5 | "it MUST go through every step of this skill -- substrate readiness check, code review (Step 3.5), smoke test, **adversarial red-team design review (Step 4.5)**, and queue validation" | 1a / (b) | "A copied script is a draft: it goes through every step of this skill" plus the failure list; drop the step enumeration (restated at 879, 889, 911). | Copy-and-modify has no fast path; the recurring propagated defects are stale `claim_ids`, drifted attribute paths, and hardcoded denominators. | -- |
| queue-experiment/SKILL.md | 595 | "Range-gated criterion -> range readiness; variance-gated -> variance readiness; count-gated -> count readiness." | 1c / (b) | Delete this third restatement -- the bullet already says "MUST be the SAME statistic the load-bearing criterion routes on" with a worked case. | The readiness precondition measures the same statistic the load-bearing criterion routes on, on a positive control where it is non-degenerate. | A-28 |
| queue-experiment/SKILL.md | 166 | "**Name the node first** ... always write the bracket ... `complicated (buildable)` -- a **named build with no open question**" | 2 / (b) | Keep the routing sentences and replace the vocabulary exposition with the CLAUDE.md "Work-graph debt vocabulary" pointer. | A `blocked_substrate` stop routes to `/implement-substrate`, not an experiment; queue only `complex (probe-gated)` nodes. | -- |
| queue-experiment/SKILL.md | 972, 979 | the same seven always-core manifest fields listed twice in one checklist | 1c / (b) | Delete the line-979 bullet. | The seven always-core fields are recorded, preferably via `stamp_recording_core(...)` placed after `arm_results` on multi-arm runs. | -- |
| queue-experiment/SKILL.md | 182-183, 196, 211, 215, 341, 352, 420, 425 | "**Do NOT write the script. Do NOT add a queue entry.**" ... "**Stop here.** Do not continue to Step 3." | 1e / (a) | Define the stop-gate once ("STOP-GATE: no script, no queue entry, report, route, stop") and have Steps 2.5a/2.5b/2.5c invoke it by name with only their own `blocked_note` wording. | Each of the four gates halts authoring, records the block, reports to the user, and routes to `/implement-substrate`. | -- |
| queue-experiment/SKILL.md | 883 | "The questions are grouped by the failure mode they're guarding against. Each has bitten us at least once." | 2 / (a) | Keep the first sentence; drop the second -- every question already carries its own EXQ citation. | The Step 3.5 questions are organised by failure mode. | -- |
| queue-experiment/SKILL.md | 1106 | "Confirmed instances, one or two per family (details in A-17): 862b / 963 / 822c; 642a / 964; 966; 966." | 2 / (f) | Delete the bare-ID line; A-39 already holds the four-family table with its confirmed-instance column. | The red-team pass targets four families of un-attributable result. | A-39, A-17 |
| queue-experiment/SKILL.md | 79-80 | "**the seven mis-blocked rows -- EVB-1185, 1398, 1401, 1408, 1583, 1585, 1595 -- are a separate data repair still owed**" | 1d / (a) | Move the owed data repair to a chip / `substrate_queue` entry; leave the rule as "the indexer bug is fixed; match on both fields". | Match proposals on `(backlog_id, proposal_type)`, never `backlog_id` alone; assert exactly one item matched. | A-19 |
| queue-experiment/SKILL.md | 1095, 1122, 1124, 1193, 1570 | "**Name the model in every report of the verdict.**" (5x) | 1c / (b) | State it once in Step 4.5 and let Step 5's `note` field carry the format example only. | The red-team verdict is recorded with the model that produced it, in the queue entry `note` and the script docstring. | A-17 |
| queue-experiment/SKILL.md | 356-363 | "**Design >=K legs** ... **Queue the legs to run in parallel** ... Add the leg that closes the worst gap." | 1c / (d) | Lead with the gate and drop "Add the leg that closes the worst gap" so the portfolio size stays K, not K+n. | GOV-FANOUT-1: on a braked discrimination, queue >=K parallel legs on different design axes, each declaring its null; single-build bottlenecks are exempt. | -- |
| queue-experiment/SKILL.md | 621 | "**When a design earns a regime-conditioning rule for one precondition, audit EVERY precondition against it.**" | 1a / (d) | "If one precondition needs regime conditioning, check the others in the same design." | A regime-conditioning fix applies design-wide; use `experiments/_lib/precondition_gate.py` rather than hand-rolling. | A-04 |
| queue-experiment/SKILL.md | 1143 | "(Backstop for a session that authored without reserving -- e.g. one served an older, frozen worktree copy of this skill.)" | 1d / -- | Delete; the preceding sentence already states the re-check and A-40 holds the rationale. | Re-verify the EXQ ID against `origin/main` before appending, and re-reserve on a fresh ID if it was taken. | A-40 |
| queue-experiment/SKILL.md | 532 | "**claim_ids accuracy rule (CRITICAL):** Tag only the claims the experiment directly tests with its actual implementation." | 1a / (a) | Drop "(CRITICAL)" -- the closing sentence already gives the reason. | Tag only the claims this implementation directly tests; never inherit `claim_ids` from a prior iteration. | -- |
| queue-experiment/SKILL.md | 616 | "**MULTI-ARM / MULTI-REGIME GATES: condition every precondition on the regimes it is meaningful for, and NEVER AND the gate whole-run (2026-07-19).**" | 2 / (a) | Drop the inline date and the caps run. | Never compute `gate_green = all(...)` across regimes -- one arm's impossible precondition would vacate another arm's valid result. | A-04 |
| queue-experiment/SKILL.md | 1149 | "**Working-tree-vs-HEAD audit (MANDATORY -- closes the 2026-05-27 fleet-wedge atomicity hole):**" | 2 / (a) | Drop the parenthetical date/incident label from the heading; keep the mechanism paragraph and diff commands untouched. | Before appending, diff the working-tree queue_id set against HEAD's and STOP on any foreign entry. | -- |

**2a: 24 rows.** Estimated saving ~11,837 chars / **~2,960 tok** (~7.7% of the file), no rule removed.

## 2b -- `.claude/skills/metaworker-dispatch/SKILL.md` (141,357 chars, ~35,340 tok, 2,264 lines)

Rows tagged **[BRIEF]** live inside the HEADLESS WORKER CONTRACT / DISPATCH_BRIEF template
(lines 1539-1770) that is prepended verbatim into every dispatch; they are cross-listed under scope 5a.

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| metaworker-dispatch/SKILL.md | 120/124, 378/381, 400/404, 936/940, 990/994, 1169/1173, 1200/1204, 1285/1289, 1313/1317, 1356/1360, 1366/1370, 1512/1516, 1787/1791 | 14 adjacent pairs of `> **Background -- B-nn:**` blocks, one immediately after another | 1c / (f) | Merge each adjacent pair into one pointer line naming both notes, per the standing "one archaeology note max" preference. | Every B-nn note stays reachable by id from the rule it belongs to. | 14 pairs |
| metaworker-dispatch/SKILL.md | 203-252 | "This is the ONE thing in this whole file that must be run BEFORE `Skill: metaworker-dispatch` is ever invoked" / "not a substitute for shrinking this file." | 1d / (f) | Cut to the command, the two exit codes, and the one-line interactive-`/loop` usage; drop the self-referential meta, the un-wired resident wrapper, and the fail-open recital. | `dispatch_preexit_check.py check` exists, exit 3 = IDLE = skip the cycle, an interactive `/loop` gates on it, and it fails open to HAS-WORK. | B-32, B-33 |
| metaworker-dispatch/SKILL.md | 1743-1770 | **[BRIEF]** "9. **If your chip's own FIRST-ACTION text tells you to self-claim it and that `chip_ledger.py claim` exits CONTENTION_EXIT" | 1c / (b) | Compress to four lines: compare the claimer to `$(cat .session_uuid)`; match means Step 4c's own pre-claim, proceed; mismatch is a real rival; re-claim with your own uuid. | The uuid comparison, match-vs-mismatch semantics, and refreshing with `--claimed-by "$(cat .session_uuid)"` rather than an invented slug. | B-68, B-69 |
| metaworker-dispatch/SKILL.md | 1915-1918, 1954-1958 | "The matcher is deliberately narrower than a bare substring" vs "**The trigger is intentionally broad**" -- the two paragraphs disagree | 2 / (b) | Keep one statement ("errs toward firing; a false positive costs only a delayed question") and delete the hand-matching instruction, now moot since the check is a script call. | A false negative costs unconsented substrate code, so the check errs toward firing and a borderline hit routes to the decision lane. | B-73 |
| metaworker-dispatch/SKILL.md | 1180-1206, 1208-1250 | "**The discriminator the script encodes** (read by hand only if python is unavailable)" -- prose then table, both full | 1c / (b) | Keep the table and reduce the preceding prose to a one-line-per-verdict action map. | Each verdict's action; USAGE-LIMIT is neither infra nor prompt fault; COMPLETED-UNRESOLVED needs a git check before re-dispatch; GENUINE-KILL goes to journalctl/dmesg. | B-51, B-13, B-14 |
| metaworker-dispatch/SKILL.md | 1655-1665 | **[BRIEF]** "A headless `/thought-digestion` worker once left its entire review artifact untracked in its worktree, where nothing enumerated it for eight days" | 2 / (b) | Delete the incident narrative; the preceding two sentences state the rule and B-65 holds the story. | Untracked worktree content has no git object and is unrecoverable once the worktree is removed. | B-65 |
| metaworker-dispatch/SKILL.md | 2003-2012, 2055-2059 | "Resolve `<Y>` once per cycle from `uname -n`, then canonicalize through `machine_identity.canonical_machine_name()`" (twice) | 2 / (b) | Delete both manual host-resolution paragraphs -- the same block already says to omit `--host` and let `check_host_withhold.py` canonicalize. | Withholding is a routing decision between dispatchers, not discarding work; host comparison goes through `machine_identity`, never a raw `==`. | B-75, B-77 |
| metaworker-dispatch/SKILL.md | 173-176, 193-195, 799-802, 1426-1430 | "**This shim is the entire cross-host path mechanism**" / "Do not \"fix\" a path problem by rewriting paths in a brief." / "VERBATIM IS CORRECT ON BOTH HOSTS" | 1c / (b) | State the verbatim-paths rule once under "Cross-host absolute paths"; reduce the other three to a pointer. | Briefs are written verbatim on both hosts because symlink shims resolve Mac paths; run `check_dispatch_base_paths.py` rather than rewriting a path by hand. | B-30, B-31, B-42 |
| metaworker-dispatch/SKILL.md | 1600-1612 | **[BRIEF]** "**A large Bash-tool `timeout` does NOT cause classifier blocks**" ... "It is **not** a classifier-avoidance measure." ... "**`kill -0 <pid>` on its own is FINE.**" | 1e / (b) | Collapse the three "this is not about the classifier" disclaimers into one sentence at the end of rule 2. | A large Bash-tool timeout and a bare `kill -0` are both fine; only backgrounding-plus-`kill` in one call has a measured block effect. | B-60, B-61, B-62 |
| metaworker-dispatch/SKILL.md | 631-637, 1844-1848 | "**DO NOT withhold an ordinary \"queue this experiment\" chip here.** Adding a NEW queue entry needs no credentials" | 1c / (b) | State the deliverable test and the git-ingress fact once (Step 1's table); cite it in one line each elsewhere. | Only `POST /queue/remove` and terminal-queue_id re-use need `coordinator.env`; a new queue entry reconciles in via git and dispatches anywhere. | B-35, B-23, B-71 |
| metaworker-dispatch/SKILL.md | 443-455 | "**On a STALE-OFFLINE finding: report it in this cycle's summary same as above, but do NOT raise a `/metaworker-repair` chip**" | 1c / (b) | Delete the re-statement of the bucket list directly above it (it even ends "per the bucket description above"); keep the "must not block dispatch" sentence. | STALE/STALLED get a `/metaworker-repair` chip if none is open; STALE-OFFLINE gets none; a finding never stops this cycle's dispatch. | B-37, B-24 |
| metaworker-dispatch/SKILL.md | 8-23 | "Collision-safety is Step 4c's atomic claim, not host identity: the first claim lands, the rest get `CONTENTION_EXIT` and move on." (restated 3 lines later) | 1c / (b) | Delete the second paragraph's opening restatement and keep its non-duplicated cap guidance. | Collision-safety comes from 4c's atomic claim, not host identity; the interactive cap is 2 and concurrent interactive loops do not stack. | B-28 |
| metaworker-dispatch/SKILL.md | 2229-2241 | "read `LAST` from `ssh ree@<cloud-5 ip ...>` ... pick the soonest midpoint `LAST + 150s + k*300s` strictly after the real UTC now" | 1f / -- | "Mac only: if convenient, offset the wakeup off cloud-5's 5-minute grid; otherwise use an ordinary idle delay" -- leave the arithmetic in B-82. | This is load-smoothing only, never a correctness fix; the idle delay stays clamped to 1200-1800s. | B-82 |
| metaworker-dispatch/SKILL.md | 2199-2203 | "**Compact deliberately, every 5-10 cycles, right after Step 3.6's scan.** The harness auto-compacts as context fills anyway" | 1b / (e) | Delete -- a fixed compaction cadence is a scaffold the harness already handles, and the text concedes it. | none -- pure scaffold (the harness auto-compacts). | B-81 |
| metaworker-dispatch/SKILL.md | 1099-1118 | "**THE COOLDOWN IS NOW ARMED FOR YOU -- you have already done it by running the detector.** Since 2026-08-18 ..." | 1d / (a) | Rewrite in the present tense without the migration framing: "The detector arms the cooldown itself and prints a `COOLDOWN:` line; `stamp` is an operator override." | The detector auto-arms on USAGE-LIMIT and prints `COOLDOWN:`; `stamp` writes unconditionally and is for correcting or forcing an arm. | B-49, B-12 |
| metaworker-dispatch/SKILL.md | 1646-1649 | **[BRIEF]** "Measured: sampling 121 of 3,617 `TASK_CHIPS.json` revisions since 2026-08-20 found 48 overwrites that erased a finding" | 2 / (b) | Delete the measurement sentence -- the rule is already stated and the number changes nothing a worker does. | `claim_note` is overwritten by the next claim, so durable pointers go in the commit message and a WORKSPACE_STATE Recent Work line too. | -- |
| metaworker-dispatch/SKILL.md | 58-61, 627, 2166 | "That is unchanged and absolute." / "matching \"The one rule\" above." / "a strictly safer posture that changes nothing above ... full stop." | 1a / (b) | Keep the canonical statement at 48-56 and condition 1's mechanical re-check; delete the three bare re-assertions. | A `kind: "decision"` chip is never dispatched headlessly under any permission mode; when unsure, treat a chip as `decision`. | B-02 |
| metaworker-dispatch/SKILL.md | 1995-2001, 2127-2132 | "If the script is ever unavailable (missing file, import error), fall back to the manual prose reading ... but log that the fallback was used" (twice) | 1c / (b) | Write the fallback rule once near condition 5 and have conditions 6/6b and 6c point at it in half a line. | If a `check_*.py` gate cannot run, read the prompt by hand rather than skipping the condition, and log the fallback. | B-73, B-75, B-79 |
| metaworker-dispatch/SKILL.md | 314, 394, 454, 489 | "do not add `--exit-nonzero` to this invocation" (4x) / "**MUST NOT block or stop dispatch on a finding**" (2x) | 1a / (b) | State once near Step 1's first report-only check: "none of Step 1's checks gate dispatch; never pass `--exit-nonzero`". | No Step 1 check may block dispatch, because the repair for a stale/wedged box is itself carried out by a dispatched session. | B-22, B-34, B-24 |
| metaworker-dispatch/SKILL.md | 1815-1824 | "even though Step 3 already excludes `kind == \"decision\"` items ... it is the actual belt-and-suspenders check ... **This is NOT redundant with the marker check below**" | 1c / (c) | Keep the re-check; cut the justification to one clause ("last point before launch"). | Re-read `kind` on the chip record immediately before constructing the dispatch command; anything but `"work"` routes to Step 5 and is flagged as a Step 3 bug. | -- |
| metaworker-dispatch/SKILL.md | 789-798 | "**Either dispatcher role runs this step** -- the resident's systemd timer, or an interactive session on-demand -- see \"Several dispatchers, one shared claim gate\" at the top" | 1c / (b) | Cut to the pointer plus the one fact not stated at the top (4a is host-local, so each dispatcher keeps its own in-flight count). | 4a is host-local with a per-dispatcher cap; cross-host safety comes from 4c's claim; urgent chips go first. | B-28 |
| metaworker-dispatch/SKILL.md | 978-980 | "**`.dispatch_pid` deliberately stays inside the worktree -- considered and rejected 2026-08-18; do not re-propose moving or mirroring it ...**" | 1d / (f) | Delete; the B-06 pointer immediately below says exactly this, at the same length. | `.dispatch_pid` lives inside the worktree by decision, not accident. | B-06 |
| metaworker-dispatch/SKILL.md | 1417, 1758-1760, 1966-1972 | inline chip-refs and dates: "(chip-20260818-dispatch-inflight-count-pid-reuse-phantom)", "(the 2026-08-09 shape, ...)", "(2026-08-22, chip-...)" | 2 / -- | Strip the inline chip-ids and dates from rule text; each already has a B-nn note carrying the incident. | The mechanical facts each id is attached to: identity-checked in-flight counting, the real-rival case, checking 6 and 6b in one script call. | B-05, B-69, B-76 |
| metaworker-dispatch/SKILL.md | 706-712 | "Read EVERY residual candidate's STOP-CHECK section in ONE turn (not one session per candidate -- that is exactly the cost this step exists to avoid)" | 1c / (d) | "Read as many residual STOP-CHECKs as fit one turn, oldest/highest-tier first" so the cap below is not fighting an EVERY instruction above it. | The reasoning pass is one turn over several candidates, not one session each; verdicts must cite a commit sha, file state or registry field. | B-39 |
| metaworker-dispatch/SKILL.md | 1330-1344 | "This band's relative position is unchanged from pre-2026-08-19 FIFO." / "ties break oldest-`spawned_at`-first, same as before 2026-08-19." | 1d / -- | Delete both migration-relative clauses; state the tie-break as a plain present-tense rule. | Unknown-origin chips sit in the default band (never last); ties break oldest-`spawned_at`-first. | B-55, B-25 |
| metaworker-dispatch/SKILL.md | 1561-1564 | **[BRIEF]** "Rule 1 forbids ending your turn to await an ASYNCHRONOUS EVENT, and that has not changed: no watcher, no background job, no subagent notification will ever wake you." | 1c / (b) | "Rule 1 still applies to asynchronous events; parking is different because it hands off to a named party who comes back." | Parking is an explicit handover and is the one sanctioned way to end a turn; asynchronous waiting is still forbidden. | -- |
| metaworker-dispatch/SKILL.md | 432-433, 439-441 | "An interactive dispatcher (the Mac) writes no orchestrator heartbeat; its absence from the report is expected." (twice, 5 lines apart) | 1c / (b) | Delete the first occurrence; the version five lines later carries the same rule plus its reason. | The Mac writes no orchestrator heartbeat and its absence from the fleet-health report is expected, not a gap. | -- |
| metaworker-dispatch/SKILL.md | 1194, 1206 | "do the same by hand only if python is unavailable (table below)" / "(read by hand only if python is unavailable)" | 1c / (b) | Keep the caveat once, on the table itself. | The table is a manual fallback; normally run `check_deferral_exit.py`. | B-51 |
| metaworker-dispatch/SKILL.md | 1649 | **[BRIEF]** "**An honest unfinished report is a success; a silent exit is not.**" | 1a / (a) | Delete -- rule 5's first sentence ("If you genuinely cannot finish, that is fine and expected") already carries this, without the register. | none -- pure intensity (the rule is stated at the top of rule 5). | -- |
| metaworker-dispatch/SKILL.md | 408, 410 | "and reports, per resident dispatcher:" immediately followed by "Per resident dispatcher it reports:" | 1c / (b) | Delete the duplicated lead-in at 410. | none -- pure editing fossil. | -- |

**2b: 30 rows** (6 of them **[BRIEF]**). Estimated saving ~15,285 chars / **~3,820 tok** per read
(~11% of the file); the [BRIEF] subset alone is ~2,635 chars / **~660 tok re-paid on every dispatch**.

## 2c -- `.claude/skills/failure-autopsy/SKILL.md` (116,603 chars, ~29,150 tok, 923 lines)

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| failure-autopsy/SKILL.md | 11, 64, 70, 127, 145, 182, 197, 277, 289, 298, 347, 360, 367, 371, 381, 384, 460, 466, 472, 531, 552, 555, 575, 580, 584, 587, 707, 711, 721, 726, 768 (31x) | "(~100 tok; not needed to follow the rule, read it before changing it)" | 1c / (b) | State the convention once near the top and reduce each pointer to `See A-nn (~N tok)`. | The archaeology pointers themselves, their token costs, and the read-before-changing convention. | all A-nn |
| failure-autopsy/SKILL.md | 378 | "compare all three over the whole autopsy corpus, not just on an example, and land them in ONE commit." (2,219-char paragraph) | 2 / (b)(f) | Cut to two sentences -- the lockstep requirement plus the diff-the-whole-snippet list -- and move the four dated divergence narratives into a new `A-nn`. | Predicate AND scan stay in lockstep across the two SKILL.md copies and `validate_queue.py::_autopsy_counts_toward_brake`; diff the whole snippet; land in one commit. | A-10, A-26 |
| failure-autopsy/SKILL.md | 909-923 | the Key-rules recap re-states each rule's full mechanism rather than pointing at its step | 1c / (b) | Hold each recap bullet to one line naming the rule and its step; delete the re-stated mechanism from 911, 912, 918, 921. | Every rule named in the recap stays findable: dry-run exclusion, self-route-is-hypothesis, frozen-ledger invariants, re-derive brake threshold and refusal. | -- |
| failure-autopsy/SKILL.md | 88 | "rebuild the index first -- the full derive chain: For accurate *scoping* (correct claim tags, `evidence_direction`, section-1 placement) rebuild the index too" | 1c / (b) | Delete the second half of the line -- **verified: it is a verbatim duplicate of its own first half, an unmerged edit.** | Regenerating alone only DETECTS a target; accurate scoping needs the index rebuilt first, then `generate_pending_review.py`. | -- |
| failure-autopsy/SKILL.md | 269-273, 336, 910 | "**Reach REE FAILED only when Implementation, Measurement, and Environment above each independently read adequate/complete.**" | 1c / (b) | State the threshold once (in the bucket table's "Established when" cell), keep 273's recording instruction, reduce 336 to one sentence. | REE FAILED requires all three independently adequate; record `failure_location{mechanism,measures,environment,ree,net_classification}`; the rule binds `claim_ids: []` prose equally. | A-06 |
| failure-autopsy/SKILL.md | 193 | "confirmed 2026-09-08 (GOV-DRY-1): four grandfathered autopsies each carried `dry_run_checked: true` while citing an unflagged `_dry_` run" | 2 / (b) | Keep the rule and the `_is_dry_run()` definition; move the incident count and dates into A-32, which exists for exactly this. | `_is_dry_run()` = flag truthy OR `_dry_<stamp>` run_id shape; a raw `dry_run` field read is not sufficient; `dry_run_checked: true` means the script was run over every cited id. | A-32 |
| failure-autopsy/SKILL.md | 204, 206, 216 | "**It is a NET, not a SUBSTITUTE -- a clean run does NOT discharge the manual read of the reduction block.**" (3x) | 1c / (c) | Say once, after the lint command, that a silent lint is not an all-clear; delete the other two. | The lint under-fires by design, so whenever a dry manifest is in scope the reduction block must still be read; an unsettable criterion is vacuous, not a negative. | -- |
| failure-autopsy/SKILL.md | 8, 17, 41, 909 | "**A clean, unflagged `experiment_purpose: \"diagnostic\"` PASS is NOT exempt.** Scope by `experiment_purpose`, not by `adjudication`." | 1c / (b) | State once at line 8 with the discriminator; let 17, 41, 909 refer to it. | Any `experiment_purpose: "diagnostic"` result needs this skill, PASS or FAIL, flagged or not; ERROR goes to `/diagnose-errors`. | A-01 |
| failure-autopsy/SKILL.md | 561 | "**If Fable is not available in this session** -- the `model` argument is rejected, or the spawn errors on the override -- re-spawn once" | 1c / (g) | "Prefer `model: \"fable\"`; if the override is rejected, retry once without it -- a same-model pass still counts -- and name the model at the Step 8 gate." | Prefer a different model for the red-team agent; withholding your reasoning is what makes it independent; fall back rather than skip; name the model at the gate. | A-20, A-21 |
| failure-autopsy/SKILL.md | 722 | "if every storable field already holds the value you would end on, deliberately end the string on a clause that is **not** a storable value" (858-char worked example) | 1c / (b) | Reduce to the decision rule plus the single INV-044 example. | Read the claim's current values first; end on a storable value not yet true; when none exists, end on a non-storable clause so the row stays ACTIONABLE. | A-24, A-25 |
| failure-autopsy/SKILL.md | 15, 281, 332, 334, 917 | "For every recommendation, draft the **exact text** of the `evidence_quality_note` governance should write -- but do not write it." (5x) | 1c / (b) | Keep the boundary at 15 and the Key-rules recap at 917 (including the `hypothesis_space_registry` exception); drop the tail from 281, 332, 334. | This skill never edits `claims.yaml`, manifests, `evidence_direction`, `review_tracker.json` or `substrate_queue.json`; the one exception is the frozen ledger at Step 9b. | -- |
| failure-autopsy/SKILL.md | 397-403 | "keep the / # three in lockstep INCLUDING the per-claim branch below; if you touch one, touch all / # three" | 1c / (b) | Replace the five-line comment header with `# R1-R3 predicate -- see the lockstep rule above before editing.` | The recipe is byte-for-byte shared with `/queue-experiment` Step 2.5b and `validate_queue.py`, and the contract test pins it. | A-10, A-26 |
| failure-autopsy/SKILL.md | 574-587 | four consecutive `> **Background -- A-nn:**` pointer blocks (A-18, A-19, A-20, A-21) | 1c / (b) | Collapse into one line naming all four. | All four pointers stay reachable, and the inline sentences they annotate stay in the body. | A-18..A-21 |
| failure-autopsy/SKILL.md | 3 | "*(This skill IS `/diagnostic-autopsy` -- not a related-but-narrower sibling. `/diagnostic-autopsy` is an accepted alias precisely because ...*" | 1c / (b) | "`/diagnostic-autopsy` is an alias for this skill." | `/diagnostic-autopsy` routes here; diagnostic adjudication is a co-equal trigger. | -- |
| failure-autopsy/SKILL.md | 123 | "Scope: the mechanical sibling-claim half of this rule is incident-scoped (V3-EXQ-936, 2026-08-18; every prior re-adjudication was a degenerate held-out case)" | 2 / (f) | Delete; A-27 immediately below is titled for exactly this and carries it. | Nothing beyond A-27 -- the operative rule (full read + bears-on note) is stated above and stands regardless. | A-27 |
| failure-autopsy/SKILL.md | 13 | "section (added the same day, `generate_pending_review.py`) is the blanket, purpose-keyed discovery net for this trigger" | 2 / (b) | "Discovery net: `pending_review.md`'s purpose-keyed diagnostic section, which fires on `experiment_purpose` alone." | `pending_review.md` has an `experiment_purpose`-keyed diagnostic section distinct from the `adjudication`-flag section. | A-01 |
| failure-autopsy/SKILL.md | 838, 867 | "**3b. DISCOVERY-GROWTH (Mode C above).** Permitted only when (i) born resolved -- `resolution` filled in the SAME edit ..." | 1c / (b) | "3b. DISCOVERY-GROWTH -- the Mode C conditions above; reported as advisory, not a (b) flag." | Discovery growth is sanctioned only when born resolved, labelled with a `discovery_growth_events[]` entry, and `initial_frozen_count_at_registration` preserved. | A-30 |
| failure-autopsy/SKILL.md | 33 | "not a fixed property of the session (2026-08-30) / (Single confirmed incident, 2026-08-30; incident-scoped.)" | 2 / (b) | Keep the rule; drop the duplicated date and the parenthetical scope note, or push both into an `A-nn`. | Staging mode is about the user's availability at gate time, so hold the interactive gate if the user is present at Step 8 or at landing; Step 9b stays draft-only. | -- |
| failure-autopsy/SKILL.md | 66 | "`check_autopsy_coverage.py` matches the candidate id against every committed artifact's CONTENT (full-string, never a prefix)" | 1c / (b) | Fold the one operative addition into the bullet at 53 and delete the paragraph; the rest restates 53. | Coverage is decided by artifact content, not filename; an `awaiting_human_confirmation` hit means confirm the draft rather than re-derive. | A-02 |
| failure-autopsy/SKILL.md | 104-105, 916 | "**RE-ADJUDICATION: read the SUPERSEDED artifact IN FULL, and the driver, BEFORE writing the recommendation (2026-08-18, user-instructed).**" | 1a / (a) | "Re-adjudication: read the superseded artifact in full, and the driver, before writing the recommendation." | The full end-to-end read of the superseded artifact and the driver's docstring caveats is required first; the bears-on note and recorded withdrawals stay. | A-27 |
| failure-autopsy/SKILL.md | 861 | "**Read `convergence_class` and `h_fanout_recurrence` together -- neither subsumes the other.**" | 1c / (d) | Move the interpretive coaching into the registry's own `invariants` block or an `A-nn`, leaving the one actionable line at 859. | A fan-out re-entering an already-eliminated axis family is the leg-level re-derive brake: prefer a different family, or state why this leg is not the dead one renamed. | -- |
| failure-autopsy/SKILL.md | 548 | "Do not \"simplify\" the checks: the suppressors and the as-of-`generated_utc` evaluation are the deliverable (script docstring)." | 1e / (f) | Delete; the A-29 pointer directly beneath is titled for this and carries the reason. | The 7b suppressors and as-of-`generated_utc` evaluation must not be removed or simplified. | A-29 |
| failure-autopsy/SKILL.md | 589 | "(7b's suppressors are re-narrowed, never tolerated, if the fire rate exceeds roughly one per three autopsies -- threshold in the script docstring.)" | 1c / -- | Delete -- a maintenance note about the script, not an instruction to the autopsy session. | none -- pure maintenance note; the operative 7b behaviour is at 542-546. | A-29 |
| failure-autopsy/SKILL.md | 753, 804 | "Mode C always attaches to an existing question, so the **growth-restriction check above applies in full** -- clear it before step 1" | 1c / (b) | 753 already lists Mode C as in scope; reduce 804 to "(growth-restriction check applies)". | The growth-restriction check must be cleared before any Mode C append. | A-30 |
| failure-autopsy/SKILL.md | 178 | "And before writing an agent's work off as lost, send it a message on its id -- a stalled agent usually resumes and restates" | 1c / (d) | Delete -- generic agent-handling advice appended to a rule about where subagent output goes, and it invites extra polling on an eager model. | none -- pure tack-on; the rule (every fan-out agent writes to an absolute scratch path) is stated in the preceding sentences. | A-05 |
| failure-autopsy/SKILL.md | 715 | "Three rules for the `change` string, all learned by measurement rather than assumed:" | 1a / (a) | "Three rules for the `change` string:" | The three rules themselves. | A-24, A-25 |
| failure-autopsy/SKILL.md | 468 | "so ALWAYS STAMP IT, including when the verdict is \"no category applies\"." | 1a / (a) | Lower-case it. | Every claim-tagged target carries `recommended_epistemic_category`; an unstamped target is invisible to GOV-CEIL-1 and understates the ceiling count in the brake-suppressing direction. | A-15 |
| failure-autopsy/SKILL.md | 199 | "Then apply, without exception:" | 1a / (a) | "Then apply:" -- the four bullets that follow each carry their own reason. | none -- pure intensity. | -- |

**2c: 28 rows.** Estimated saving ~10,942 chars / **~2,735 tok** (~9.4% of the file).

## 2d -- `.claude/skills/governance/SKILL.md` (113,915 chars, ~28,480 tok, 1,611 lines)

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| governance/SKILL.md | 1415-1419 | "A governance session is a NEXUS -- spend time spawning work." Walk everything this cycle surfaced and `spawn_task` a chip for each concrete, actionable next step | 1c / (d) | "Chip each concrete, actionable next step this cycle surfaced, per `/session-land` Phase 3 filters; spawn nothing rather than invent filler." | Non-`/governance`, non-`/failure-autopsy` follow-on is chipped (not reported inline), under Phase 3's absolute-path / cwd / STOP-CHECK / not-already-in-flight / no-filler filters. | A-43 |
| governance/SKILL.md | 1522-1525, 1575-1588, 1590-1598 | the Key-rules block re-states the failure-autopsy boundary for the fifth time (2,326 chars of recap) | 1c / (b) | Reduce the four recap bullets to one-line pointers at their in-body homes, keeping GOV-APPLY-1 / GOV-DRY-1 / GOV-SUBPATH-1 which have no other home. | The four rules, and that GOV-APPLY-1 / GOV-DRY-1 / GOV-SUBPATH-1 are defined ONLY here and must not be shortened. | A-45, A-46 |
| governance/SKILL.md | 306-312, 320, 420-424, 1499-1503, 1596 | "every diagnostic result, PASS or FAIL, full stop (2026-08-07, user-instructed -- no exemption for a PASS that \"routes no visible decision\")" (5x) | 1c / (b) | State the diagnostic-autopsy gate once at Step 1.5a and cross-reference it from 2b, "Experiment types" and Key rules. | Every diagnostic result needs a confirmed or in-flight `failure_autopsy_*.json` before it can be marked reviewed or drive a governance action; gate on `experiment_purpose == "diagnostic"` alone. | A-26, A-44 |
| governance/SKILL.md | 509, 511, 522, 539, 541, 1514 | "**CRITICAL: Use AskUserQuestion to get the user's view on each experiment before proceeding.**" (6x) | 1a / (a) | Drop the `CRITICAL:` prefixes and the following "Do NOT proceed until the user has responded" lines; one sentence per step. | Steps 2 and 3 are genuine user-decision gates: the user reclassifies evidence/diagnostic, accepts/revises/rejects a confirmed autopsy's routing, and approves each promotion/demotion before any claims.yaml write. | -- |
| governance/SKILL.md | 471-474, 490-491 | "Briefly read the driver script itself for every claim-tagged evidence PASS, however simple it looks" / "Never skip the skim because a PASS \"looks routine\"." | 1c / (a)(d) | Keep the scope sentence and the two things the skim must cover; delete "however simple it looks", the "must not be trusted more than a FAIL" line, and the closing "Never skip" sentence. | The skim is required on every claim-tagged evidence PASS, covers criteria-combination logic AND threshold arithmetic against measured baselines, is logged in `review_log` even when clean, and a defect routes to `/failure-autopsy`. | A-27 |
| governance/SKILL.md | 344-358, 583-591, 928-935, 1582-1588 | "Check top-level `dry_run` FIRST, before reading a metric." plus its full rationale, at four entry points | 1c / (b) | Keep the imperative and the `check_dry_run_citations.py` invocation at each of the three real entry points, but compress each to two lines pointing at one shared rationale paragraph. | Never read a dry manifest into the walk and never stamp `evidence_direction` onto one; the family sweep and the 6a-ii scan have no upstream filter; a confirmed autopsy discharges the check only with `dry_run_checked: true`. | A-06, A-09 |
| governance/SKILL.md | 9, 14-18, 20-22 | "ALWAYS FIRST, unconditional -- even under contention" / "This is the single first action of every governance cycle" / "Register first, THEN pause" | 1a / (a)(b) | Collapse all three into one: "Open the pause claim before anything else, including before checking for conflicts, and always with `--allow-overlap`." | The claim opens before reading TASK_CLAIMS for conflicts and before Step 1; contention never justifies skipping it; `--allow-overlap` is mandatory; `--session-label` literally begins `governance-pause:`. | A-21 |
| governance/SKILL.md | 828-850 | "**NARROW, INCIDENT-SCOPED exception (2026-08-30): a PROSE-ONLY, count-neutral, state-neutral registry correction ...**" (1,873 chars) | 1d / (f) | Compress to the trigger plus the three guard NAMES; point at A-34 for the field lists and instances. | Governance may edit registry prose only when the producer routed it, only if all three guards hold, and never anything that moves a count, state, run list or schema. | A-34 |
| governance/SKILL.md | 102-103, 1449, 1452, 1513 | "It is opened once (Step 0) and closed in exactly one place -- Step 9, via `/session-land`." / "the ONLY point this claim is released" | 1c / (b) | Keep it once at Step 9; reduce the Step 0b and Key-rules copies to a bare cross-reference. | The pause claim survives every AskUserQuestion pause and is closed only at Step 9 via `/session-land`, or `--not-landed` if abandoned. | A-22 |
| governance/SKILL.md | 44, 327, 431, 440, 445, 473, 485, 1224 | "is decided at the walk as today -- surfaced, not blocked" / "*(default -- current behavior)* ... exactly as today" / "the old ... gate is retired" | 1d / -- | Rewrite each migration-relative phrase in the present tense -- "as today" has no referent for a reader who never saw the prior version. | Each rule's actual disposition: an `unverified` flag is surfaced not blocked; route B is the default; an explained FAIL is handled inline; the skim applies to all claim-tagged evidence PASSes. | -- |
| governance/SKILL.md | 784-787, 1096-1098, 1119, 1180, 1237 | "Surface `orphaned`, `ceiling_may_have_lifted` and `ceiling_exhausted` (6a-v-bis) via AskUserQuestion." (repeated per audit) | 1f / (g) | Say once, at the head of 5c/6a-v, that all warn-only overlay findings are batched into a SINGLE AskUserQuestion round rather than one interrupt per audit. | Every ACTIONABLE overlay hit reaches the user for adjudication; none is auto-applied. | A-33, A-36 |
| governance/SKILL.md | 137, 170-176 | "**The trial ledger is the point.** ... After ~3 recorded outcomes the user decides codify-into-its-own-skill vs retune vs drop" | 2 / -- | Keep "record one line in the closing note: fired or quiet, which signals, useful or not"; move the trial-governance meta-paragraph and the GOV-HELDOUT-1 analogy into A-23. | Run `pause_pressure.py --chip` once per cycle; QUIET is one line; PRESSURE is presented with tripped signals plus the manual signal-5 count; the outcome is recorded in the closing note. | A-23 |
| governance/SKILL.md | 613-617 | "the flat copy overrides it **only** when `_is_annotated(flat) and not _is_annotated(pack)` (`:1346`, `:1517`)" | 2 / -- | Keep all three mechanical details verbatim but replace the bare `:1346` / `:1517` / `:1428` / `:3291` line numbers with function names -- line numbers in `build_experiment_indexes.py` rot silently. | Write BOTH flat and pack copies; `evidence_direction_note` is the `_is_annotated` marker without which the write is discarded; a per-claim entry beats the run-level field. | A-07, A-08, A-29 |
| governance/SKILL.md | 325-326 | "**(A) Clear inline now** *(recommended when the promotion/demotion agenda depends on these FAILs)* -- invoke `/failure-autopsy` in **this** session" | 1c / (d) | Add the cost to the recommendation ("... AND the set is small enough to clear inside this cycle's context floor"), keeping (B) as the stated default. | Route A runs `/failure-autopsy` inline in cluster mode under the governance claim; route B is the default when the user does not pick; needs-autopsy work is never chipped. | -- |
| governance/SKILL.md | 105, 108, 137, 178, 231, 276 | "### Step 1 -- Orientation" / "### Step 1a -- Open governance flags" ... then "### 1. Run the pipeline" / "### 1a. Read the Steward escalation verdict" | 2 / -- | Renumber the "Before starting" block (Step 0, 0b, 0c, 0d, 0e) so its labels never collide with the "Steps" block, and move Step 0c back above Step 1. | All six steps and their content; only labels and ordering change. | -- |
| governance/SKILL.md | 485-486 | "(chip-20260908-pending-review-degenerate-evidence-pass, incident V3-EXQ-1007) now surfaces a manifest-level `non_degenerate: false`" | 2 / -- | Drop the inline chip-ref and incident id. | Read that section first, but it does not replace the skim -- it only reports what the driver's own pre-registered check already flagged. | A-27 |
| governance/SKILL.md | 1440-1444 | "report those inline unless the user asks otherwise, exactly as Steps 5c / 6a-v-ter already say" | 1c / (b) | Delete -- 5c, 6a-v-bis and 6a-v-ter state their own disposition, and the sentence admits as much. | GOV-FROZEN-1 recurrences, GOV-DIAG-1 re-poses and GOV-CEIL-1 demotions are reported inline, not chipped. | A-43 |
| governance/SKILL.md | 95-100 | "Never poll silently forever without telling the user what you're waiting on and why." | 1d / (g) | "Say what you are waiting on each poll; after several cycles offer keep-waiting / proceed-anyway / go-resolve via AskUserQuestion." | Read-only orientation is safe during the wait; only the pipeline run and shared-file edits are gated on quiet; the three escalation options and the residual-interleaving caveat. | A-22 |

**2d: 18 rows.** Estimated saving ~6,760 chars / **~1,690 tok** (~6%). The subagent's own note is worth
preserving here: *the larger effect is behavioural rather than volumetric -- rows 1, 5, 11 and 15 each
remove a standing pressure to do MORE work per cycle, which on Fable 5.1 costs far more than the
characters do.*

**Scope 2 total: 100 rows, ~11,205 tok.**

---

# Scope 3 -- the two work-repo `CLAUDE.md` files

## 3a -- `/Users/dgolden/REE_Working/ree-v3/CLAUDE.md` (72,628 chars, ~18,160 tok, 621 lines)

Low pressure-language density (`never` x8, `always` x4). This file is mostly reference content, and its
opening paragraph is itself a model of the right instinct: it records that 1.48 MB of inline substrate
records were moved out after measuring that the median session referenced 2 of 139 feature IDs. The
findings are stale specifics and near-adjacent restatement, not shouting.

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| ree-v3/CLAUDE.md | 256 + 287 | "Every queue entry **must** have `estimated_minutes` set (never omit it)." ... 31 lines later "Always include `estimated_minutes`" | 1a+1c / (a)(b) | Keep 256 as "Every queue entry needs `estimated_minutes`; the runner's auto-calibration refines it." and delete 287. | `estimated_minutes` is required on every entry and is refined by auto-calibration. | -- |
| ree-v3/CLAUDE.md | 296 + 316 | "NEVER re-use an ID that was previously run." ... 20 lines later "never re-queue a failed or completed experiment under the same EXQ ID" | 1a+1c / (a)(b) | Keep the 316 statement (it carries the mechanism) and cut 296 to a cross-reference. | The runner silently skips a `queue_id` already in `runner_status.json`; append a letter instead. | -- |
| ree-v3/CLAUDE.md | 258 vs 284-285 | "**Mac (`DLAPTOP-4.local`)**" in the calibration table, while 285 says `"DLAPTOP"` is canonical and the suffix drift caused a real bug | 2 / (b) | Relabel the calibration row `**Mac (DLAPTOP)**` so the file stops modelling the exact string its own next paragraph warns about. | Affinity resolves through `machine_identity.same_machine()`, not raw hostname equality; `DLAPTOP` is canonical. | A-16 |
| ree-v3/CLAUDE.md | 276-282 | "Throughput pending -- onboarding smoke V3-ONBOARD-smoke-ree-cloud-2 queued." / "Throughput not yet benchmarked (original smoke errored 2026-04-06, -b pending)" | 2 / -- | Replace both with one "uncalibrated -- estimate as cloud-1" line, or delete rows for boxes no longer in the fleet. | Uncalibrated machines are estimated from cloud-1 until their own smoke lands. | -- |
| ree-v3/CLAUDE.md | 265-269 | "GPU NEVER wins at current model scale (world_dim=32): EXQ-070 tested batch 1-512, CPU always faster" | 1a / (a) | Lower-case "never"; the measurement in the same sentence is what carries it. | The measurement, the threshold (`world_dim >= 128`), and the conclusion. | -- |
| ree-v3/CLAUDE.md | 242-253 | "GATE: Do NOT implement or experiment on Level 2 MECH-113 ... until ALL of the following are met: (1) ... (2) ... (3)" | 1e / (f) | **Keep as-is** -- reasoned prohibition with a named release condition; recorded here to show it was examined, not missed. | The three release conditions and why premature Level 2 is uninterpretable. | -- |

**3a: 6 rows** (one an explicit keep). Estimated saving ~1,200 chars / **~300 tok**.

## 3b -- `/Users/dgolden/REE_Working/REE_assembly/CLAUDE.md` (34,974 chars, ~8,745 tok, 485 lines)

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| REE_assembly/CLAUDE.md | 147-161 | "**Phase history:** - **Phase 1 (2026-04-29):** shadow-only ... **Phase 3 (2026-05-01):** cutover landed." | 2 / (f) | Move the 15-line phase history to `evidence/planning/` and keep the one-line current regime; the cutover completed four months ago. | Lit and exp are separate signals; promotion/demotion gates read `experimental_confidence`; the 2D quadrant table. | -- |
| REE_assembly/CLAUDE.md | 118-143 | "The indexer accepts the legacy names too as a one-cycle backwards-compat fallback" / "kept ... for one cycle" (x3) | 1d / -- | Check whether the one-cycle windows (opened 2026-05-01) have closed; if so delete the compat notes, if not date them. | Which key names are current (`min_exp_conf`, `low_exp_conf`, `lit_only_above_cap`) and that `overall_confidence` is emitted but not gated on. | -- |
| REE_assembly/CLAUDE.md | 41 | a single 1,400-char paragraph carrying three numbered incident write-ups inside the evidence-claim rule | 2 / (f) | Keep the rule and the mechanism in two sentences; move the three dated incidents to an archaeology note. | Editing `evidence/**` or `claims.yaml` needs an active claim, because the runner heartbeat's `pull --rebase --autostash` can silently revert uncommitted edits; register before opening, commit or close before walking away. | -- |
| REE_assembly/CLAUDE.md | 191-227 | 37 lines distinguishing `substrate_ceiling` from `substrate_conditional`, opening "the digestion pass that produced this note initially mis-tagged one claim as the other" | 2 / (c) | Keep the two-sentence operational discriminator and the two confirmed examples; move the provenance sentence and the MECH-439 demotion history out. | The discriminator (never-exercised vs exercised-but-absorbed-downstream), both confirmed examples, and that both route to "work on substrate first" for different reasons. | -- |
| REE_assembly/CLAUDE.md | 354-357, 397 | two "**Canonical example of the failure mode (2026-03-22):**" blocks, each a full EXQ-by-EXQ narrative | 1c / (f) | Compress each to one sentence naming the shape; keep numbers only where they pin the shape ("2 false supports, 3 false mixed"). | Per-claim direction overrides exist because one FAIL otherwise marks every tagged claim "weakens"; inherited `claim_ids` propagate silently across iterations. | -- |
| REE_assembly/CLAUDE.md | 385 | "## claim_ids Accuracy Rule (CRITICAL)" | 1a / (a) | Drop "(CRITICAL)" -- the section's own first line ("This is a scientific accuracy issue, not a tagging detail") is the real emphasis and explains itself. | All four tagging rules and the reason: wrong tags corrupt confidence and conflict scores. | -- |
| REE_assembly/CLAUDE.md | 47-48, 59-64 | "bash scripts/governance.sh --v2 # V2 (also syncs from ree-v2/)" and the whole V2 pipeline block | 1d / -- | Demote the V2 pipeline to one line under an "old paths" note -- `ree-v2` is CLOSED per umbrella `CLAUDE.md:9`. | The V3 pipeline commands, which are the live ones. | -- |

**3b: 7 rows.** Estimated saving ~4,760 chars / **~1,190 tok**.

---

# Scope 4 -- `AGENTS.md` and `NEW_AGENT_START_HERE.md`

## 4a -- `/Users/dgolden/REE_Working/AGENTS.md` (20,366 chars, ~5,090 tok, 313 lines)

**This is the single highest-value finding in the audit, and it is not a tone finding.** `AGENTS.md` is
a forked copy of an older `CLAUDE.md` that has drifted, and it is where `NEW_AGENT_START_HERE.md` routes
non-Claude agents. Five of its rules now **actively disagree** with the live ones -- precisely the
condition under which the guide's keep-list item 8 converts "working redundancy" into a real finding.
Each disagreement below was verified against the live system on 2026-09-14.

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| AGENTS.md | (whole file) | 313 lines re-stating umbrella `CLAUDE.md`: ~5,090 tok of duplication carrying five live contradictions | 2 / (b) | **Highest-value single edit in the audit:** reduce `AGENTS.md` to a pointer at `CLAUDE.md` plus genuinely agent-specific content, the way `NEW_AGENT_START_HERE.md` already is. | Non-Claude agents still need a named entry point routing them to the same live rules. | -- |
| AGENTS.md | 73 | "**Write your own claim** to `TASK_CLAIMS.json` BEFORE editing any files. Fields: `session_id` and `claimed_at` = current UTC ISO-8601 time; ..." | 2 / (b) | Replace with the `task_claim.py open` invocation -- **verified: a hand-edit is now refused by the blocking `scripts/protect_task_claims_hand_edit.py` `PreToolUse` hook**, so this instruction sends an agent into a wall. | Claim before editing; the claim carries session_id, label, task and resources. | A-66 |
| AGENTS.md | 301 | "Current held claims: ARC-007, ARC-016, ARC-018, MECH-025, MECH-033, Q-007." | 2 / -- | Delete the list and use the umbrella file's lookup one-liner -- **verified: the real held set is 530 claims and none of these six is in it.** | v3_pending / `implementation_phase: v3` claims cannot be promoted until V3 evidence exists; look the set up, never trust a pinned list. | -- |
| AGENTS.md | 93, 202, 288 | "see `REE_assembly/AGENTS.md`" / "See `ree-v3/AGENTS.md` Troubleshooting section for the canonical incident." | 2 / -- | Repoint to `REE_assembly/CLAUDE.md` and `ree-v3/CLAUDE.md` -- **verified: neither `AGENTS.md` exists.** | The pointer targets: the manual governance commands, and the re-used-ID incident. | -- |
| AGENTS.md | 9 | "`ree-v2` \\| V2 substrate — real experiments, transitioning to V3" | 2 / -- | "V2 substrate -- CLOSED (all experiments complete)", matching umbrella `CLAUDE.md:9`. | The repo map's role column must state each repo's live status. | -- |
| AGENTS.md | 252-255 | "**Stubs for future work** ... `recover_stale_claims()` — currently logs stale claims but doesn't auto-reset them" | 1d / -- | Delete -- umbrella `CLAUDE.md` documents `recover_stale_claims()` as live with two recovery routes and a 6h floor that must not be lowered. | The 6h `COORDINATOR_STALE_HOURS` floor and why absence of telemetry is not abandonment. | -- |
| AGENTS.md | 229-251 | "The section below is preserved for the pre-Phase-3 / fallback path." plus 22 lines of git-based claiming | 1d / (f) | Delete the preserved legacy section and keep the Phase-3 note -- the umbrella file moved this material to `docs/reference/multi-machine-coordination.md`. | Phase 3 is authoritative: the coordinator's `/claim` endpoint arbitrates and `sync_daemon` is the sole git writer. | A-93 |
| AGENTS.md | 47-49, 128, 198-200 | "bash scripts/governance.sh --v2 # V2", the `ree-v2` push row, "Experiment design + queuing \\| `ree-v3`, `ree-v2`" | 1d / -- | Strip `ree-v2` from the live tables; it is CLOSED. | The V3 pipeline command and the per-repo push commands that are still live. | -- |
| AGENTS.md | 19 | "## IMPORTANT: Active Working Directory" | 1a / (a) | "## Active Working Directory" -- the section's own "ALL active repos live inside" sentence carries it. | `/Users/dgolden/REE_Working/` is the only tree to read, write or push from; the iCloud path is stale. | -- |

**4a: 9 rows.** Estimated saving ~16,000 chars / **~4,000 tok**, plus the removal of five active
contradictions -- the larger of the two effects.

## 4b -- `/Users/dgolden/REE_Working/NEW_AGENT_START_HERE.md` (3,012 chars, ~750 tok, 51 lines)

**Substantially clean, and reported as such.** One screen, low emphasis (`never` x1, no caps stack, no
archaeology blocks), and every reference resolves -- verified 2026-09-14 that all nine skills in its
routing table exist and both `.cursor/rules/ree-session-land.mdc` copies are present. The guide's rule
that "an audit that finds nothing should change nothing" applies; **this file is the shape the other
entry points should converge on, not away from.**

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| NEW_AGENT_START_HERE.md | 45 | "Re-read immediately before write: `experiment_queue.json`, `TASK_CLAIMS.json`, `review_tracker.json`, `WORKSPACE_STATE.md`, `docs/claims/claims.yaml`." | 2 / -- | Drop `TASK_CLAIMS.json` and add `evidence/**` -- umbrella `CLAUDE.md` explicitly excludes `TASK_CLAIMS.json` from the exposed-files set (coordinator-authoritative, hook-blocked) and includes `evidence/planning/`. | Re-read a shared file immediately before writing it. | A-94 |

**4b: 1 row.** Estimated saving ~50 chars / **~12 tok**.

---

# Scope 5 -- the headless briefs

## 5a -- DISPATCH_BRIEF template, `.claude/skills/metaworker-dispatch/SKILL.md` (Step 4c area)

The HEADLESS WORKER CONTRACT at lines 1539-1770 is prepended verbatim into every `DISPATCH_BRIEF.md`,
so every character is re-paid on every dispatch. **Six rows, cross-listed in scope 2b and marked
[BRIEF] there:** lines 1743-1770 (contract rule 9 CONTENTION_EXIT), 1655-1665 (the eight-day untracked
artifact narrative), 1600-1612 (three separate "not a classifier-avoidance measure" disclaimers),
1646-1649 (the 121-of-3,617 revision measurement), 1561-1564 (rule 1b re-listing rule 1), and 1649
("An honest unfinished report is a success; a silent exit is not.").

Together they remove ~2,635 chars / **~660 tok from every dispatch**. At this fleet's cycle volumes
that is the highest-leverage subset in the audit despite being a fifth of one file's rows -- and it is
exactly the target the plan's item 17 (`cost-optimize`, "one measured change at a time") named.

## 5b -- IGW spawn prompt, `scripts/igw_routine_tick.py` `spawn_claude()` / `write_start_here()`

The prompt an auto-spawned IGW worker receives is assembled in `write_start_here()` (line 3364) from
the ledger item's `agent_brief` plus module-level templates, then passed to `claude -p` by
`spawn_claude()` (line 3510). The **boilerplate** portion -- paid on every spawn, on top of the
per-item brief -- is 4,495 chars / **~1,123 tok**: `_QUEUE_EXPERIMENT_GUARDRAIL` (~399 tok,
`/queue-experiment` items only), `_DONE_STEP_HEADLESS_INTRO` (~135) or `_DONE_STEP_INTERACTIVE_INTRO`
(~120), and `_DONE_STEP_BODY` (~468).

| file | line(s) | quoted fragment (<=25 words) | criterion | proposed rewording (one sentence) | RULE CONTENT THAT MUST SURVIVE | archaeology |
|---|---|---|---|---|---|---|
| igw_routine_tick.py | 3336 + 3273 | "## MANDATORY: run the full /queue-experiment skill" and "## MANDATORY: Final step -- run /session-land's Headless variant" -- both headings in one brief | 1a / (a) | Drop "MANDATORY:" from both headings; a two-heading brief where both are marked mandatory has flattened its own priority. | Run the full skill end to end including code review and smoke test; run `/session-land`'s Headless variant before `complete`. | -- |
| igw_routine_tick.py | 3319-3321 | "Do NOT skip this step. Without it the ledger entry stays completed_resumable, the worktree is kept as unfinished indefinitely" | 1a / (a)(b) | Keep the consequence sentence, drop "Do NOT skip this step." -- the heading already says it is the final step. | Skipping `complete` leaves the entry `completed_resumable`, keeps the worktree, and can cause a re-spawn. | -- |
| igw_routine_tick.py | 3307-3309 | "confirmed repeatedly: IGW-20260719-189, -20260902-239, -20260903-245, -20260905-235, -20260907-233" | 2 / (f) | "confirmed on five entries to date" -- the ids are unresolvable from inside a fresh worktree anyway. | `--outcome AUTO` misfiles a normal landing as NO_OP because it only sees this worktree's branch; pick the outcome yourself. | -- |
| igw_routine_tick.py | 3275-3280 | "Before calling `complete` below, run `/session-land`'s **Headless variant** ... -- NOT the full skill. This is a headless `spawned` IGW session: there is no user..." | 1c / (b) | "Run `/session-land`'s Headless variant (not the full skill -- Phase 5c needs a user, and there is none)." | Headless sessions take the Headless variant because Phase 5c's `archive_session` requires a live user. | -- |
| igw_routine_tick.py | 3290 | "Do not assume your work is committed -- verify it: `git status` in every repo you touched" | 1c / (c) | **Keep** -- a re-verification loop guarding a real, repeatedly-observed failure (uncommitted work at headless close); passes keep-list item 5. | Verify commits in every touched repo; write a `NOT LANDED:` line rather than leaving work uncommitted. | -- |
| igw_routine_tick.py | 3357-3358 | "Marking blocked_substrate (or queuing one well-formed experiment) is a COMPLETE outcome -- do not force-queue something just to look productive." | -- | **Do not tone down; strengthen if anything.** The one anti-eagerness instruction in the whole brief, aimed at exactly the failure mode Fable 5.1 makes likelier. | A blocked_substrate marking is a complete outcome; a vacuous FAIL is not a verdict. | -- |

**5b: 6 rows** (two explicit keeps). Estimated saving ~1,000 chars / **~250 tok per spawn**.

---

# Summary

## Counts per file

| scope | file | rows | est. tok saved | when paid |
|---|---|---|---|---|
| 1 | `CLAUDE.md` | 17 | ~3,600 | **every session** |
| 2a | `queue-experiment/SKILL.md` | 24 | ~2,960 | on skill trigger |
| 2b | `metaworker-dispatch/SKILL.md` | 30 | ~3,820 | on skill trigger (+660/dispatch) |
| 2c | `failure-autopsy/SKILL.md` | 28 | ~2,735 | on skill trigger |
| 2d | `governance/SKILL.md` | 18 | ~1,690 | on skill trigger |
| 3a | `ree-v3/CLAUDE.md` | 6 | ~300 | every ree-v3 session |
| 3b | `REE_assembly/CLAUDE.md` | 7 | ~1,190 | every assembly session |
| 4a | `AGENTS.md` | 9 | ~4,000 | every non-Claude agent session |
| 4b | `NEW_AGENT_START_HERE.md` | 1 | ~12 | agent entry |
| 5b | `igw_routine_tick.py` brief templates | 6 | ~250 | **every IGW spawn** |
| | **TOTAL** | **146** | **~20,560 tok** | |

(Scope 5a's six rows are counted inside 2b, not double-counted here.)

By criterion letter, across all scopes: **(b) restatement is the dominant finding at roughly half of all
rows**, then (a) intensity, then (f) collapsible negative lists, then (d) thoroughness nudges. **(e) --
reasoning rituals -- returned exactly one hit in 146 rows** (`metaworker-dispatch:2199`, a fixed
compaction cadence), which is a genuinely good result: this corpus was never written in the
"think step by step" idiom. **(g) returned three**, all of which were examined and two of which were
kept as genuine user-decision gates rather than permission-asking.

## Estimated total token saving

**~20,560 tokens** if every proposal is applied, with **no rule content removed** -- roughly 9% of the
~228,000 tokens across the nine audited surfaces. The distribution matters more than the total:

- ~3,600 tok comes off the file loaded into **every session in this workspace**.
- ~4,000 tok comes off `AGENTS.md`, and takes five active contradictions with it.
- ~660 tok comes off **every dispatch** and ~250 tok off **every IGW spawn** -- these compound with
  fleet volume in a way the one-time figures do not.

**And the volumetric figure is the smaller half of the case.** The behavioural findings -- the chip-volume
nudges, the re-verification loops, the "read EVERY / however simple it looks / iterate until" family --
change how much work a session does per cycle. On a model described as more eager than its predecessor,
that cost is not measured in the characters removed.

## Top 10 highest-value rewordings

1. **`AGENTS.md` -> a pointer** (4a, whole file). ~4,000 tok and five live contradictions, one of which
   (the hand-edit claim instruction at :73) now walks an agent straight into a blocking hook.
2. **The chip-volume cluster** -- `CLAUDE.md:666` "CHIP EVERYTHING ELSE", `CLAUDE.md:658` and
   `governance/SKILL.md:1415` "a governance session is a NEXUS -- spend time spawning work". Three
   instructions to generate more work, on a model that already will. Keep the routing rule; drop the
   exhortation.
3. **The 51 archaeology-disclaimer blocks in `CLAUDE.md`** (~2,600 tok, every session) and the parallel
   31 in `failure-autopsy` (~420 tok). One stated convention replaces 80 repetitions.
4. **The DISPATCH_BRIEF / HEADLESS WORKER CONTRACT trim** (5a). ~660 tok on every dispatch.
5. **`queue-experiment:1000`** "re-run the whole code review pass. Iterate until every question above can
   be answered correctly." An unbounded re-verification loop written to force a lazy model to re-check;
   on an eager one it is an invitation to loop.
6. **`governance` six `CRITICAL:` AskUserQuestion prefixes** (509, 511, 522, 539, 541, 1514). The gates
   are real and stay; the markers have stopped carrying information precisely because there are six.
7. **`queue-experiment:1447-1560`**, the ~100-line inline heredoc for a check that "never blocks the
   queue add" -> a script file. ~3,750 chars, the largest single block in the audit.
8. **The PASS-skim intensity family** -- `governance:471-474/490-491` ("however simple it looks",
   "Never skip the skim because a PASS looks routine") and `queue-experiment:881` ("a 'yes, looks fine'
   ... does not count"). The skims stay; the goading goes.
9. **`AGENTS.md:301`'s hardcoded V3-pending list.** Six claim ids, none of which is among the 530 actually
   held -- a factually wrong instruction that the umbrella file's own rule ("look it up rather than
   trusting a hardcoded list") was written to prevent.
10. **`REE_assembly/CLAUDE.md:147-161` phase history plus the three "for one cycle" compat notes.** A
    completed 2026-05-01 cutover still narrated in the present tense, with backwards-compat windows
    that were scoped to one cycle and have had eighteen.

## Rules that should NOT be toned down at all

1. **`CLAUDE.md:297` Scope Discipline and `CLAUDE.md:299` Narrow Edits Only.** These are the umbrella
   file's only two global do-LESS rules, and they are aimed at exactly the behaviour the changelog
   warns about. On Fable 5.1 they should if anything be *strengthened* -- Narrow Edits Only in
   particular, since its failure mode (an unnecessary full regen sweeping a thousand files) is the
   canonical over-eager action in this repo.
2. **`queue-experiment` Step 4.5 line 1120 -- "One pass. Do NOT iterate to CLEAR (that manufactures a
   clean verdict). Re-spawn exactly once..."** A do-LESS constraint on an agent-spawning step. An eager
   model's natural move is to re-spawn until the reviewer says CLEAR, which is precisely the
   verdict-manufacturing this forbids.
3. **`failure-autopsy`'s refuse-to-manufacture family (lines 96, 202, 737) and its honest-grading clause
   (563).** "Do not manufacture a target"; "the autopsy has no target: say so ... and stop"; "inflating
   CONTESTED to justify the pass destroys the signal, and grading generously to avoid a costly
   conclusion destroys it equally." The Fable 5.1 failure mode for this skill is producing an
   adjudication where the evidence does not support one. Keep the bluntness.
4. **`metaworker-dispatch` contract rule 1 (1550-1560) -- "NEVER end your turn to await an asynchronous
   event ... `Monitor`'s own tool result says 'Keep working -- do not poll or sleep.' That guidance ...
   is exactly backwards here. Ignore it. Poll."** This overrides a *contradicting tool result the worker
   will actually receive*, against five measured worker deaths. It needs to be louder than the thing it
   is arguing with; the volume is the mechanism.
5. **`governance` lines 219-225 ("bound it by WAVES PLUS A CONTEXT FLOOR, never by a target count") and
   244-264 (the `while read` file list plus "Always sanity-check the file count before calling
   `ree_commit.py`").** The first is the only global brake on governance cycle size. The second is a
   fragile destructive operation where exactly one script is safe and the failure mode -- a
   silently-blank file list walking the whole working tree -- is repo-wide; keep-list items 3 and 5
   both apply, and the guide is explicit that prescriptive text is *correct* there.

A sixth, noted because it sits in a headless brief where nothing else pushes back:
**`igw_routine_tick.py:3357` -- "do not force-queue something just to look productive."** It is the only
anti-eagerness sentence in the IGW spawn prompt.

## Handoff to WI-B2

Every row above is a proposal, not an edit. WI-B2's held-out check (GOV-HELDOUT-1) applies per section:
find at least 3 historical cases the rule was NOT written from **where the old and new wording give
different answers**, confirm the new wording gives the right call, and record the outcome in the commit
message. Rows whose "RULE CONTENT THAT MUST SURVIVE" cell names an `A-nn`/`B-nn` note should have that
note re-read before the rewrite, per the convention those pointers exist to enforce.

Land in small commits, one section each, through `ree_commit.py`; mirror any skill edit to
`.agents/skills/`; then re-run `audit_worktree_skills.py --self` so live worktrees see the drift banner.
