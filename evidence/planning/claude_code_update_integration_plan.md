# Claude Code 2.1.251-2.1.269 update: integration plan of record

- **Drafted:** 2026-09-14T04:52:17Z (session `claude-code-update-plan-20260914`, Mac DLAPTOP, main checkout)
- **Source:** "This week in Claude Code: /resume on desktop, start sessions from your phone, and more" -- Lydia, Claude Code team, 2026-09-11 (weekly changelog email). Items below are the email's, cross-checked against the local setup, not against the full changelog.
- **Local version at audit:** Claude Code 2.1.269 on the Mac (meets every version floor the email names: 2.1.251, 2.1.257, 2.1.259, 2.1.260, 2.1.261, 2.1.265, 2.1.267). Fleet versions (`ree-cloud-5`, hub) NOT verified -- the WireGuard tunnel was down at audit time (ssh to 10.8.0.5 / 10.8.0.1 timed out). See WI-F.
- **Sits under:** `context_budget_restructure_plan.md` (2026-09-07) and `token_split_measurement_20260907.md`. Several items here are the natural next step of that restructure (prompt retune for Fable 5.1, skill cost measurement, cache-hit measurement) and reuse its measurement tool (`REE_assembly/scripts/token_split_measure.py`) as the done-check.
- **Status legend:** `NONE` = no local impact, recorded so nobody re-audits it; `ADOPT` = leverage the improvement; `FIX` = something local is now stale or wrong; `VERIFY` = a check owed before concluding.

---

## 1. Audit table: what the email says vs what the local setup does

| # | Email item (version) | What was found locally | Impact | Disposition |
|---|---|---|---|---|
| 1 | **Fable 5.1 in Claude Code**; "more eager than Fable 5", retune effort, tone down prompts/CLAUDE.md written for older models; `/claude-api prompt-audit` | Fable 5.1 is already the session model here and is already used as the cross-model red-team in `/governance` and `/failure-autopsy` (WORKSPACE_STATE 2026-09-05). Umbrella `CLAUDE.md` is 133,405 chars (~33k tok), 290 bold spans, 23 hard imperatives (NEVER/MUST/ALWAYS/DO NOT); project skills total ~1.1 MB with four over 100 KB (`queue-experiment` 154 KB, `metaworker-dispatch` 141 KB, `failure-autopsy` 116 KB, `governance` 114 KB). No `prompt-audit` has been run. | HIGH -- this is the cost and behaviour lever | **ADOPT** -> WI-A (audit), WI-B (retune) |
| 2 | **`/effort` remembered per model** under `modelSettings` in user settings; changing effort mid-session no longer invalidates the cache on Fable 5.1 (2.1.260) | `~/.claude/settings.json` has NO `modelSettings`; effort is whatever the harness default is, on every model. | MEDIUM -- free cost lever | **ADOPT** -> WI-B |
| 3 | **`CLAUDE_CODE_SUBAGENT_MODEL`** env picks the default subagent model; `/tasks` shows each subagent's model | Not set. Skills pass an explicit `model:` on four `Agent` calls (`fable` red-team in queue-experiment Step 3.6 and failure-autopsy Step 7; `sonnet` campaign bundles and `opus` chip runs in metaworker-orchestrate). Memory `feedback-subagent-economy-by-model` (2026-09-03) already records the pattern: Sonnet for rule-following drafts, Opus for registry dedupe, main model reviews and lands. Un-annotated `Agent` calls (the majority) inherit the session model, i.e. Fable 5.1 for every Explore/fan-out agent. | MEDIUM -- cost | **ADOPT** -> WI-B; also **FIX** -> WI-D (the "different model" red-team is now same-model when the session is on Fable) |
| 4 | (implied by 1) model aliases | `scripts/dispatch_remote_launch.py` `_RECOMMENDED_MODEL_ALIASES["fable"] = "claude-fable-5"` -- a chip whose title says "Recommended model: fable" launches a headless worker on Fable 5, not 5.1. `WORK_TYPE_MODEL_DEFAULTS` are all opus/sonnet (fine). | LOW-MEDIUM | **FIX** -> WI-E |
| 5 | **`bypassPermissions` ignored in project `.claude/settings.json`** (2.1.257) | Nothing relies on it. Project `permissions.defaultMode` is `auto`; every headless launch (`igw_routine_tick.py`, `dispatch_remote_launch.py`, metaworker-dispatch Step 4c, `claude_account.py` probes) uses `--permission-mode auto`; the worker settings template carries no `permissions` block at all. | NONE | **NONE** -- recorded; do not re-audit |
| 6 | **Parallel sessions no longer overwrite each other's `~/.claude.json`** (2.1.259): fixed spurious workspace-trust re-asks and MCP/project state going missing | 30 umbrella worktrees + 7 work-repo worktrees on the Mac; the metaworker runs many concurrent `claude -p` on `ree-cloud-5`. CLAUDE.md's "one-time-per-machine approval" paragraph for the `ree-working` MCP server describes exactly the symptom this fixes. | LOW (fix is automatic once the binary is current) | **VERIFY** -> WI-F (fleet on >= 2.1.259; retire any local workaround) |
| 7 | **Session naming + SessionStart/SessionEnd hooks** that write id/name/dir to a file, and a boot script that resumes them all (Will Laves pattern) | Naming is already mandatory (`/rename`, Worktree Session Naming section). But `sync_worktree_session_registry.py` DISCOVERS the session by newest `*.jsonl` mtime + first user snippet -- a heuristic. There is no `SessionEnd` hook anywhere; the existing `SessionStart` hook only audits worktree skill staleness. No resume-all script exists; the resume rule is manual (`cd <wt> && claude --resume`). | MEDIUM -- directly serves the registry and the restart problem | **ADOPT** -> WI-G |
| 8 | **`PreModelSwitch` / `PostModelSwitch` hooks** (2.1.251) | None configured. `audit_hook_gating.py` audits PreToolUse only (its live corpus and latent check both read `hooks.PreToolUse`). Cross-model red-team verdicts must "name the model" -- today that is self-reported prose. | LOW-MEDIUM | **ADOPT** -> WI-G (log switches to the same session ledger); **FIX** -> WI-H (extend the gating audit before any non-PreToolUse hook that can exit non-zero exists) |
| 9 | **Prompt-cache statistics in `/cost`** and in the status-line `prompt_cache` payload; fewer cache misses after `/model` and `--resume` (2.1.267) | No `statusLine` configured. `token_split_measure.py` measures input COMPOSITION (fixed-prompt share), not cache hit rate; the two are complementary and the restructure plan's projected ~12% saving was never checked against realized cache behaviour. The `--resume` fix benefits the worktree resume rule automatically. | MEDIUM -- measurement | **ADOPT** -> WI-I |
| 10 | **`/skill-doctor`** (2.1.261): per-skill context cost and invocation frequency, flags never-used skills | 29 project skills (dual-mirrored `.claude/` + `.agents/`, parity confirmed), plus bundled `anthropic-skills:*`, `engineering:*`, `bio-research:*`, `understand-anything:*` plugin skills, most of which this project never invokes. Never measured. `context_budget_restructure_plan.md` WI-2 moved umbrella CLAUDE.md sections INTO skills, so skill descriptions are now a larger share of the fixed prompt. | MEDIUM -- measurement first | **ADOPT** -> WI-J |
| 11 | **`model:` / `effort:` in skill frontmatter** work again in interactive sessions (2.1.259, 2.1.267) | Project skills have NO frontmatter at all (CLAUDE.md "Skills" rule: none unless confirmed working). Scheduled-task SKILL.md files DO carry `name:`/`description:` frontmatter and work, so frontmatter parsing is confirmed on this install. | MEDIUM -- lets heavy skills pin their own effort/model | **VERIFY then ADOPT** -> WI-C |
| 12 | **`--plugin-dir` takes a folder of plugins** (2.1.265) | Two plugins enabled (`github@claude-plugins-official`, `understand-anything` from a directory marketplace). No plugin development in flight. | NONE | **NONE** |
| 13 | **Word-editing keys match Bash by default** (Ctrl+W, Alt+F/D) (2.1.261) | No `~/.claude/keybindings.json`; `keybindingFlavor` never set. Behaviour change is user-facing only. | NONE (muscle memory) | **NONE** -- user note only |
| 14 | **Live `/diff` panel in fullscreen** (2.1.260; needs `/tui fullscreen`, a git repo, >= 110 cols); select lines to attach to the next prompt | User settings already have `"tui": "fullscreen"`. Every repo is git. Not referenced by any skill; `/session-land` Phase 1 and the read-modify-write "confirm every hunk is yours" rule both do a diff review by `git show`. | LOW-MEDIUM -- workflow | **ADOPT** -> WI-K |
| 15 | **Desktop: pop any pane into its own window; Files pane with tabs + inline PDF/Office/spreadsheet preview; output styles on desktop; SSH sessions remember a host password** | Desktop app is the primary surface (this session runs in it). Lit-pull sessions read PDFs; the Files pane preview is directly useful. SSH to the fleet uses key auth (`BatchMode=yes`), so the password feature is moot. | LOW | **ADOPT** -> WI-K (operator notes only) |
| 16 | **Computer use runs in the background on desktop** (beta, Pro/Max, macOS 15+) | Not part of any REE workflow. `computer-use` MCP is present but unused by skills. | NONE | **NONE** |
| 17 | **`/claude-api cost-optimize` and `hillclimb`** | `cost-optimize` ("one measured change at a time") is the right frame for the headless briefs (`DISPATCH_BRIEF.md`, IGW spawn prompts) which are re-sent per worker. `hillclimb` needs an eval; the skill-eval machinery exists (`anthropic-skills:skill-creator`) but no REE skill has an eval suite. | LOW now, MEDIUM after WI-A | **DEFER** -> after WI-A/WI-J (noted in WI-B) |
| 18 | **VS Code model picker / slash commands / output styles** (2.1.257) | VS Code is not a surface used for REE work. | NONE | **NONE** |

---

## 2. Work items

Ordering principle: **measure before rewording** (WI-A, WI-I, WI-J are read-only and cheap), **settings changes first** (WI-B is a two-key JSON edit with no repo impact), and **held-out checks on every standing-rule edit** (GOV-HELDOUT-1 applies to WI-B's rewording and to WI-C/WI-G's rule additions -- record the outcome on each edit).

Every WI is chip-shaped (self-contained, absolute paths, START-TIME STOP-CHECK = `task_claim.py check --resources <its paths>`). None is `/governance` or `/failure-autopsy` work, so all are chippable under the Housekeeping rule.

### WI-A -- Run `/claude-api prompt-audit` over the Claude Code setup (measure)

- **What:** In an interactive session on the main checkout, run `/claude-api prompt-audit` scoped, in this order: (1) `/Users/dgolden/REE_Working/CLAUDE.md`; (2) the four >100 KB skills; (3) `ree-v3/CLAUDE.md` and `REE_assembly/CLAUDE.md`; (4) `AGENTS.md` + `NEW_AGENT_START_HERE.md`; (5) the headless briefs (`DISPATCH_BRIEF.md` template in metaworker-dispatch Step 4c, the IGW spawn prompt in `igw_routine_tick.py spawn_claude()`). Write findings to `REE_assembly/evidence/planning/claude_code_prompt_audit_20260914.md` -- one row per flagged instruction: file, line, what the audit says is older-model-shaped, and the **rule content that must survive** any rewording.
- **Why the last column matters:** most of the emphatic wording in `CLAUDE.md` (the 23 hard imperatives, the "Do NOT re-propose ..." blocks) is incident-derived and each carries an `A-nn` archaeology pointer. "Tone down" means removing intensity and redundancy, never the rule. The audit output alone cannot make that distinction; the findings file must.
- **Does NOT edit anything.** Output is the findings file only.
- **Done-check:** findings file exists, covers all five scopes, and every row has the survive-column filled.
- **Effort:** one session, Fable 5.1 medium.

### WI-B -- Retune the harness for Fable 5.1: effort per model, subagent default, then the rewording pass (adopt)

Two halves, landed separately.

**B1 -- settings only (no repo change, no held-out check needed).** Add to `~/.claude/settings.json` (user scope, the Mac; NOT the project file, which is gitignored and propagated to worktrees and workers by `sync_worktree_settings.py` / `install_worker_claude_settings.py`):

```json
{
  "modelSettings": {
    "claude-fable-5-1": { "effortLevel": "medium" },
    "claude-opus-5":    { "effortLevel": "high" }
  },
  "env": {
    "CLAUDE_CODE_SUBAGENT_MODEL": "opus"
  }
}
```

Rationale: the email's own operating point (Fable medium, Opus high) is the starting point, and the 2026-09-03 memory already says Opus is the right default for the heavy draft subagents while the main session stays on Fable. Explicit `model:` on an `Agent` call (the four sites in item 3) still wins. Verify with `/tasks` during a fan-out that subagents show `opus`. Then run `/effort` once on each model so the values are confirmed persisted. Revisit `medium` after WI-I gives a cache and cost figure; do not tune by feel.

**B2 -- rewording pass over WI-A's findings (standing-rule edit; GOV-HELDOUT-1 applies).** For each finding: draft the toned-down wording; find >= 3 historical cases the rule was NOT written from (`git log -p` on the section, the `A-nn` archaeology files, WORKSPACE_STATE Recent Work); confirm the new wording gives the same call on each; record the outcome in the commit message. Land in small commits, one section each, through `ree_commit.py`. Mirror any skill edit to `.agents/skills/`. Then re-run `audit_worktree_skills.py --self` so live worktrees see the drift banner.

- **Done-check for B2:** `token_split_measure.py --report --since <B2 landing date>` one week later shows fixed-prompt share not higher than the 2026-09-07 post-restructure figure (the re-measure task scheduled 2026-09-14T08:00Z gives the baseline), and no `/governance` or `/queue-experiment` session in that week reports a rule regression. Add a dated "Re-measure" block to this file, same shape as `context_budget_restructure_plan.md`.
- **Risk:** the one real risk in this whole plan. A toned-down rule that a more eager model then skips is the exact failure the emphatic wording was added to stop. The held-out check is the mitigation; the archaeology pointers are the evidence corpus. Do not batch B2 with anything else.
- **Defer:** `/claude-api cost-optimize` on the headless briefs (item 17) runs AFTER B2, one measured change at a time, against the IGW/metaworker cost figures the coordinator DB already records.

### WI-C -- Confirm skill frontmatter, then let heavy skills pin `effort:` / `model:` (verify, then adopt)

- **Step 1 (verify):** add `---\nname: claim-target\ndescription: <its H1 line>\neffort: medium\n---` to the smallest skill (`claim-target`, 7 KB), mirror to `.agents/`, and confirm in a fresh interactive session that (a) it still appears in the skills list with the same name, (b) `/claim-target` still invokes, (c) the effort shows in `/cost` or `/effort` output for that turn. If any of (a)-(c) fails, revert and stop: the CLAUDE.md "no frontmatter" rule stands and this WI closes as NOT ADOPTED with the observation.
- **Step 2 (adopt, only if Step 1 passes):** pin `effort: high` on `governance`, `failure-autopsy`, `queue-experiment` (their red-team and code-review passes are where eagerness costs the most) and `effort: medium` on the bookkeeping skills (`morning-digest`, `session-land`, `update-docs`, `sync`). Do NOT pin `model:` on any skill yet -- the headless launchers (`dispatch_remote_launch.py`) already own model routing per work type and a frontmatter `model:` would be a second, unreconciled router. Then edit the CLAUDE.md "Skills" paragraph from "no YAML frontmatter unless confirmed working" to "frontmatter confirmed 2026-09-xx for `name`/`description`/`effort`; `model:` deliberately not used (see WI-C)". GOV-HELDOUT-1 applies to that edit.
- **Done-check:** Step 1 outcome recorded here; if adopted, `ls .claude/skills .agents/skills` parity still holds and `audit_worktree_skills.py --self` is clean on the main checkout.

### WI-D -- Make the cross-model red-team actually cross-model when the session is on Fable (fix)

- **What:** `queue-experiment` SKILL.md ~line 1095 and `failure-autopsy` SKILL.md ~line 561 say "run it on a DIFFERENT model -- pass `model: "fable"`". Written when the drafting session was Opus. With Fable 5.1 now the interactive default, that `Agent` call is a SAME-model pass, and the skills' own fallback text ("a same-model pass is valid; skipping is not") means nobody notices. Reword both to: "pass the `model` that is NOT the session model: `opus` when this session is on Fable, `fable` when it is on Opus; name which in the verdict". Keep the existing fallback.
- **Held-out check:** the 2026-09-05 governance cycle (five Fable-red-teamed Opus drafts, all CONTESTED) is the motivating case; find three others in WORKSPACE_STATE where the red-team model was named, and confirm the new wording would have picked a different model in each. Record the outcome.
- **Done-check:** both skills reworded in both mirrors; `grep -n 'model: "fable"' .claude/skills/*/SKILL.md` returns only lines that also name the opus alternative.

### WI-E -- Update the `fable` alias in the headless launcher (fix)

- **What:** `scripts/dispatch_remote_launch.py` line 249: `"fable": "claude-fable-5"` -> `"claude-fable-5-1"`. Check `scripts/test_dispatch_remote_launch.py` for a pinned expectation and update it in the same commit. Consider whether `chip_ledger.py record --model` validates against the same alias table (grep `claude-fable` across `scripts/`).
- **Also:** decide whether any `WORK_TYPE_MODEL_DEFAULTS` entry should move to Fable 5.1 now that it exists in `/model`. Recommendation: no -- keep the headless fleet on Opus/Sonnet until WI-I gives a per-model cost figure; the email itself warns Fable 5.1 "tends to spin up many subagents", which on an unattended worker is a cost multiplier with no one watching.
- **Done-check:** `run_scripts_tests.sh test_dispatch_remote_launch.py` green from the main checkout; landed on `REE_Working` master.

### WI-F -- Fleet version check and workaround retirement (verify)

- **What:** when the tunnel is up: `ssh ree@10.8.0.5 'claude --version'` and the same on any other box that runs `claude -p` (hub if `igw_routine_tick.py` spawns there). Anything below 2.1.259 still has the parallel-session `~/.claude.json` clobber (item 6) and below 2.1.267 the `--resume` cache miss (item 9). Bring them to >= 2.1.269 with `claude update` under the `ree` user; re-run `install_worker_claude_settings.py` afterwards only if the settings file was disturbed (it should not be).
- **Then:** re-read the CLAUDE.md MCP paragraph ("One-time-per-machine approval required ... shared across all worktrees") against a fresh worktree on the current binary. If the re-ask no longer happens, leave the paragraph (it is still true) but drop any session note that treats a re-ask as expected. Check memory for an entry recording the re-trust symptom and retire it if found.
- **Done-check:** a one-line version table (box, version, date) appended to this file.

### WI-G -- Session ledger hooks: `SessionStart` / `SessionEnd` / `PostModelSwitch` write one JSONL line each (adopt)

- **What:** a new `scripts/session_ledger_hook.py` that reads the hook stdin payload and appends `{ts, event, session_id, session_name, cwd, worktree_slug, model}` to `/Users/dgolden/REE_Working/.claude/session_ledger.jsonl` (gitignored, per-machine). Wire it in `.claude/settings.json` under `SessionStart`, `SessionEnd` and `PostModelSwitch`. **Hard constraints, all inherited:** always `exit 0` (read-only detection class, same as `worktree_edit_guard.py`); un-worktree `$CLAUDE_PROJECT_DIR` the same way the existing hooks do; interpreter fallback `/opt/local/bin/python3` then PATH; pass `audit_hook_gating.py` (after WI-H extends it) before `sync_worktree_settings.py` will propagate it.
- **Consumers, in order of value:** (1) `sync_worktree_session_registry.py` prefers the ledger's `session_name` for a slug over the jsonl-mtime heuristic (keep the heuristic as fallback); (2) a new `scripts/resume_sessions.sh` that lists the last `SessionStart` per worktree with no matching `SessionEnd` and prints (or runs, with `--run`) `cd <wt> && claude --resume <id>` per line -- the Will Laves boot script, which the 2.1.267 resume cache fix makes cheap; (3) the cross-model red-team verdicts (WI-D) can cite the ledger's `PostModelSwitch` line instead of prose.
- **Worker template:** add `SessionStart`/`SessionEnd` ONLY (not `PostModelSwitch`, which never fires headless) to `scripts/claude_settings_worker.json` -- read-only, exit-0, so it meets the template's own admission rule -- and let `count_inflight_workers.py` / `check_worker_launch.py` consider it as a liveness signal in a later change, not this one.
- **Held-out check:** the rule text added to CLAUDE.md (one sentence under Worktree Session Naming pointing at the ledger) is small; still run it against three past registry mis-labels from `docs/worktree_session_registry.md` history.
- **Done-check:** `scripts/test_session_ledger_hook.py` in the umbrella corpus; `audit_hook_gating.py` green; registry regen picks up a name from the ledger for at least one live worktree.

### WI-H -- Extend `audit_hook_gating.py` to every hook event that can exit non-zero (fix, prerequisite for WI-G)

- **What:** the audit's live corpus and latent check read only `hooks.PreToolUse`. `SessionStart`, `SessionEnd`, `PostToolUse`, `PreModelSwitch` (which CAN block a switch) and `PostModelSwitch` are unaudited. Generalise: for every event, run each hook against a benign canary payload for that event and require exit 0 unless the hook demonstrably reads its input first. Keep the CLAUDE.md "Hooks" rule text as is (it already says "A PreToolUse hook that can exit non-zero MUST gate on the tool input first"); widen it to "any hook" only after the audit covers any hook -- same commit, GOV-HELDOUT-1 recorded.
- **Done-check:** `run_scripts_tests.sh --changed` green from the main checkout; `sync_worktree_settings.py --dry-run` still accepts the current settings file.

### WI-I -- Status line with model / effort / cache hit rate, and a cache-hit column in the token-split re-measure (adopt)

- **What:** a `scripts/statusline.sh` (registered via `statusLine` in user settings) printing `model | effort | ctx used | cache hit % | last-miss reason` from the status-line JSON (`prompt_cache` fields, per the email). Keep it dependency-free (`jq` or python one-liner) and never non-zero. Second half: extend `REE_assembly/scripts/token_split_measure.py --report` with cache hit/miss counts per session from the transcript JSONL usage blocks (`cache_read_input_tokens`, `cache_creation_input_tokens`), so the restructure's projected saving and the realized cache behaviour are reported side by side. The re-measure task scheduled for 2026-09-14T08:00Z runs the current script; this WI lands after it and becomes the baseline for WI-B2's done-check.
- **Done-check:** status line visible in a fresh session; `--report` prints a cache column; the number is quoted in WI-B2's re-measure block.

### WI-J -- Run `/skill-doctor`, record the table, turn off what is never used (measure, then adopt)

- **What:** in an interactive session, run `/skill-doctor`; paste its table (skill, context cost, invocation count, flagged) into `REE_assembly/evidence/planning/skill_doctor_20260914.md`. Then: (1) plugin skills never invoked in this project (`bio-research:*`, `engineering:*`, most `anthropic-skills:*`) -- disable at plugin level in user settings, not by deleting; (2) project skills flagged never-invoked -- do NOT delete (they are invoked by scheduled tasks and headless workers that `/skill-doctor` cannot see: `morning-digest`, `zombie-reaper`, `metaworker-*`); instead mark them `user-invocable`-only via frontmatter once WI-C confirms frontmatter, which removes their description from the auto-invoke prompt while keeping the slash command; (3) feed the per-skill context cost back into `context_budget_restructure_plan.md` WI-2 as the measured cost of having moved CLAUDE.md sections into skills.
- **Done-check:** the table file exists; the fixed-prompt share in the next `token_split_measure.py` run is not higher; every skill turned off is listed with the reason.

### WI-K -- Operator notes: `/diff` panel, pane pop-out, Files pane, resume-all (adopt, docs only)

- **What:** a short `docs/reference/claude-code-operator-notes.md` (umbrella `docs/reference/`, alongside the existing routing/coordination references), NOT new CLAUDE.md prose (memory `feedback-no-fallback-doctrine-bloat`). Contents: `/diff` in fullscreen as the pre-commit hunk review for the read-modify-write "confirm every hunk is yours" rule and for `/session-land` Phase 1 (select the foreign hunk, attach it to the prompt, that IS the surfacing step); pop the diff or terminal pane to the second screen during long `/governance` cycles; Files pane preview for lit-pull PDFs; `resume_sessions.sh` from WI-G; the Ctrl+W/Alt-F/Alt-D keybinding change. Add one pointer line to `/session-land` Phase 1 and to the CLAUDE.md read-modify-write "Manual detection" paragraph ("or select the hunks in `/diff`") -- both are pointers, not rules, so GOV-HELDOUT-1 is not triggered.
- **Done-check:** file exists and is linked from the two places named.

---

## 3. Sequencing

| Phase | WIs | Gate to next phase |
|---|---|---|
| 0 -- today, zero-risk | B1 (settings), E (alias fix), F (when tunnel up) | B1 values persisted (`/effort` on each model); E tests green |
| 1 -- measure | A (prompt-audit), J (skill-doctor), I (status line + cache column) | three findings files exist; baseline numbers recorded here |
| 2 -- retune | D (red-team model), C (frontmatter verify -> adopt), B2 (rewording, one section per commit) | GOV-HELDOUT-1 outcome recorded on every standing-rule commit; one-week re-measure block appended |
| 3 -- automation | H (audit extension) then G (session ledger hooks + resume-all) | `audit_hook_gating.py` green; registry regen reads the ledger |
| 4 -- docs | K | linked from `/session-land` Phase 1 and the CLAUDE.md pointer |

Phase 2 is the only phase with a real regression risk and is the only one that must not be batched with anything else.

---

## 4. Explicitly NOT doing

- **Not moving the headless fleet to Fable 5.1** (WI-E rationale): unattended workers plus a model that spawns more subagents is a cost multiplier with nobody watching. Revisit with WI-I numbers.
- **Not pinning `model:` in skill frontmatter** (WI-C): the launcher already routes by work type; two routers would drift.
- **Not touching `bypassPermissions`** anywhere: nothing uses it (item 5).
- **Not deleting any skill** on a `/skill-doctor` "never invoked" flag: scheduled and headless invocations are invisible to it (WI-J).
- **Not building a hook or gate for the held-out check** during B2: CLAUDE.md says that check stays manual, and B2 is where that rule earns its keep.

---

## 5. Verification log

| Date | WI | Outcome |
|---|---|---|
| 2026-09-14 | audit | Table in section 1 built from: `claude --version`; `~/.claude/settings.json`; project `.claude/settings.json` hook inventory; `scripts/claude_settings_worker.json`; grep of `--permission-mode` / `bypassPermissions` across `scripts/`, `.claude/skills/`, `ree-v3/`; skill frontmatter scan (none); `wc -c` on CLAUDE.md and all SKILL.md; `dispatch_remote_launch.py` model tables; `sync_worktree_session_registry.py` discovery path; scheduled-task list (20 tasks, 5 enabled). Fleet ssh timed out -- WI-F owed. |
| 2026-09-14 | B1 | DONE by hand (orchestrator session `claude-code-update-run-20260914`): `~/.claude/settings.json` now carries `modelSettings` (claude-fable-5-1 medium, claude-opus-5 high) and `env.CLAUDE_CODE_SUBAGENT_MODEL=opus`; backup saved beside it. Not yet confirmed via `/effort` in an interactive session. |
| 2026-09-14 | E | DONE. REE_Working `c1204daff` (origin/master): fable alias -> `claude-fable-5-1`; regression test added; no other alias table found in `scripts/` or `ree-v3/dispatch`. `WORK_TYPE_MODEL_DEFAULTS` unchanged. |
| 2026-09-14 | F | OWED. Tunnel down at both attempts: WireGuard.app running but the tunnel not activated on the Mac (no 10.8.0.x address on any utun; route to 10.8.0.1 leaves via en0). Re-run when the tunnel is toggled on. |
| 2026-09-14 | A | DONE. REE_assembly `7b3f4bcfee`: `claude_code_prompt_audit_20260914.md`, method = the real `/claude-api prompt-audit` guidance (loaded via the Skill tool), 146 rows (CLAUDE.md 17, four skills 100, ree-v3/REE_assembly CLAUDE.md 13, AGENTS.md+NEW_AGENT 10, headless briefs 6), ~20.5k tok removable with no rule content lost. Headline: **AGENTS.md is a drifted fork of CLAUDE.md with five live contradictions** (its claim step says hand-edit TASK_CLAIMS.json, which a blocking hook refuses; its V3-pending list names six claims none of which is in the real held set) -- the first B2 commit should replace it with a pointer. Do-not-tone-down list recorded in the file. |
| 2026-09-14 | J | DONE. REE_assembly `a3ef49feb4`: `skill_doctor_20260914.md` (headless approximation; 1,692 transcripts, 2026-06-24..09-14). Always-present description cost ~2,940 tok/turn, of which project skills 133 and bundled plugin skills 2,807 (bio-research 709, engineering 631, anthropic-skills 1,182 -- ALL THREE zero invocations ever, and built into the 2.1.269 binary rather than installed plugins, so disabling is a config question, not a file edit). `metaworker-dispatch` (141 KB) shows zero Skill invocations in the corpus despite being designed for `/loop` -- worth a real `/skill-doctor` look. Six project skills never invoked and with no headless caller: claim-target, cowork, cross-field, humanizer, steward, view-experiments (kept). |
| 2026-09-14 | I | DONE. REE_Working `655510eb4c` (`scripts/statusline.sh` + test; field names verified against the statusline docs) and REE_assembly `9ff48d8bea` (`token_split_measure.py --report` prompt-cache section, add-only, 0 pre-existing lines changed). `statusLine` registered in `~/.claude/settings.json` by the orchestrator. **Baseline (`--since 2026-09-08`, 19 sessions, 1,684 turns): cache-read share 97.18%, creation 2.81%, uncached 0.01%; median per-turn cache-read 99.05%; cold-turn misses 0/1,665.** This is the figure B2 is judged against. |
| 2026-09-14 | D | DONE. REE_Working `499af56f1e`: queue-experiment Step 3.6 and failure-autopsy Step 7 now pass the model that is NOT the session model (opus on a Fable session, fable on Opus/Sonnet); fallback and name-the-model kept; both mirrors identical. GOV-HELDOUT-1: 3 differing post-cutover cases found (2026-09-07 hopeful-solomon, 2026-09-07 cool-sutherland, 2026-09-09 wizardly-meninsky) -- passed cleanly, not incident-scoped. |
| 2026-09-14 | H | DONE. REE_Working `8911b5652`: `audit_hook_gating.py` audits every event in a settings file (unknown events audited, not skipped); PreToolUse verdicts unchanged (pinned by test); findings gain `event`, `--json` gains `events_audited`. 48 tests. The CLAUDE.md "Hooks" rule text NOT widened (standing-rule edit -> B2). |
| 2026-09-14 | G | DONE. REE_Working `fcb4a9d8c`: `session_ledger_hook.py` (+21 tests), `resume_sessions.sh`, registry consumer in `sync_worktree_session_registry.py` (ledger name preferred, heuristic fallback), worker template gains SessionStart/SessionEnd (audit OK, 33 tests), `.gitignore` for the ledger. Orchestrator wired SessionStart+SessionEnd+PostModelSwitch into the Mac `.claude/settings.json`: `audit_hook_gating` OK across 5 events (59 canaries); `sync_worktree_settings.py` propagated to 30 worktrees; one real SessionEnd payload run through the installed command: rc 0, correct line appended. CLAUDE.md pointer sentence added under Worktree Session Naming (pointer, no held-out check). |
| 2026-09-14 | K | DONE. REE_Working `2c35d5a9d5`: `docs/reference/claude-code-operator-notes.md`; pointer line in `/session-land` Phase 1 (both mirrors, line 172); CLAUDE.md read-modify-write "Manual detection" paragraph gained a parenthetical pointer to `/diff`. |
| 2026-09-14 | C | DONE (later same day, user-approved). Step 1 verified live: with frontmatter, `claim-target` still listed (description now from frontmatter instead of the bare H1) and `/claim-target` invoked normally; effort effect not observable headless. Step 2 landed REE_Working `a32bb4d83f`: `effort: high` on governance / failure-autopsy / queue-experiment, `effort: medium` on morning-digest / session-land / update-docs / sync, `name`+`description` on all eight; both mirrors identical; no `model:` anywhere. CLAUDE.md "Skills" sentence updated to record the confirmation. |
| 2026-09-14 | B2 | DONE for the top-10 (user chose top-10 scope and per-section review; both matched the recommendation, logged). Drafted by six draft-only subagents in the scratchpad, each section shown to the user with its before/after and held-out record, all eight approved, applied as patches against the live files, one commit per section. REE_Working origin/master: `e46055f4f` AGENTS.md -> pointer + NEW_AGENT_START_HERE re-read list (#1/#9; 0 differing, pure de-dup); `50cc26e49` CLAUDE.md 51 archaeology blocks -> one-line `> Background:` pointers with the convention stated once + two chip-volume sentences (#2/#3; 6 differing cases, routing rule byte-preserved; -983 tok/session -- the audit's 2.6k assumed dropping link targets, kept); `8b4170beb` queue-experiment bounded re-review, "looks fine" fold, 99-line check -> `scripts/plan_gap_drift.py` (#5/#7/#8; 4 differing for #5, 0 for #8 recorded as intensity-only); `5b90fb782` governance one CRITICAL kept of six, PASS-skim goading removed, NEXUS reworded (#2/#6/#8; 3/0/1 differing, each recorded); `bd693362e` failure-autopsy 31 blocks -> pointers (#3; exempt); `c78df635d` dispatch brief -376 tok/dispatch, contract rule 1 byte-identical, ONE AUDIT DELETION OVERRULED by the held-out check (the /thought-digestion override a worker got right stays), 121-of-3,617 measurement moved to B-64 (#4). REE_assembly `48437f0961`: phase history -> current-state paragraph, text preserved in `evidence/planning/lit_exp_decoupling_option_e_phase_history.md`; the three "for one cycle" compat notes KEPT because their code paths are still live in `build_experiment_indexes.py` (#10). Not done: the remaining 136 audit rows outside the top-10 (deferred, not rejected). Done-check owed: `token_split_measure.py --report --since 2026-09-15` in a week against the WI-I baseline (cache-read 97.18%, cold misses 0). |
| 2026-09-14 | B2 round 2 | DONE -- the remaining 136 rows plus the Hooks-rule widening, user-approved per file (all eight items and the three flagged sub-items). REE_Working: `c4b3502e4` CLAUDE.md (13 rows + `## Closed on measurement -- do not re-propose` section, net +145 tok by user choice; Hooks rule: any event, blocking events named, exit-0 class named); `b4a7ca8fa` queue-experiment (21 rows, ~765 tok); `5353929cb` governance (15 rows, ~344 tok; one audit proposal overruled); `d119d519f` failure-autopsy (26 rows, ~1,145 tok; @561 skipped); `9102e5b4b` metaworker-dispatch (24 rows, ~1,830 tok/read); `93fa1665f` igw_routine_tick.py (4 rows, ~80 tok/spawn, tests green). ree-v3 `6a4b433` CLAUDE.md (5 rows). REE_assembly `dde7cd5a62` CLAUDE.md (5 rows). Held-out records in each commit; three drafts were corrected by their own checks before review (queue-experiment 2.5c; governance row 12; IGW row 4 pinned substrings). Chipped: `chip-20260914-evb-litreview-blocked-repair`. Audit status: 146/146 rows dispositioned (applied, applied-partially with reason, kept by decision, or skipped with reason). |
| 2026-09-14 | B2 (prior) | HELD for user review. Inputs ready: WI-A findings file (146 rows, survive-column filled, do-not-tone-down list) and the WI-I cache baseline. Recommended first commit: replace AGENTS.md with a pointer to CLAUDE.md + NEW_AGENT_START_HERE.md (fixes five live contradictions, not a tone change). Second: the archaeology-disclaimer convention (49 verbatim repeats in CLAUDE.md, 31 in failure-autopsy -> one stated convention). Then the chip-volume exhortations. One section per commit, GOV-HELDOUT-1 on each. Also pending from H: widening the "Hooks" rule from PreToolUse to any event. |
| 2026-09-14 | F (later same day) | DONE, one step handed to the user. Root cause of the unreachable fleet: the Mac's `wg-gui` WireGuard tunnel had been DELETED from WireGuard.app (~2026-09-13T09Z; `scutil --nc status wg-gui` -> `No service`; watchdog bounced a non-existent service 223x). No import file existed (key lived in the app). Re-keyed: new Mac key `xe32t/+VDFlOkn3bsCEeECm+rAk4CRrky6LjEQlfoSc=` at `10.8.0.11` (`~/wireguard/wg-gui.conf`), hub `.11` peer swapped (backup `wg0.conf.bak-mac-rekey-20260914`); the user ran the hub step by hand (classifier denies remote writes), first with the `NEWPUB` placeholder left in (hub briefly had no `.11` peer), then corrected. Tunnel verified: hub 44 ms, coordinator `/health` ok, fresh handshake. Fleet versions: hub has no Claude (retired runner, by design); workers 2/3 powered off; **ree-cloud-4 2.1.251 -> 2.1.270 and ree-cloud-5 2.1.247 -> 2.1.270 via `claude update`** with zero live headless sessions (cloud-4's first attempt timed out downloading, second succeeded). Both were below the 2.1.259 parallel-session fix and the 2.1.267 resume-cache fix until now. Neither box uses `bypassPermissions`; both project settings carry only the SessionStart/PreToolUse detection hooks. **Worker settings installed (~10:10Z, same session):** `install_worker_claude_settings.py` refuses a DIFFERENT existing file by design and wants `--force`; on each box the installed file was first verified to be a strict subset of the new template (no installed-only keys or hooks), then `--force` run. Both `ree-cloud-4` and `ree-cloud-5` now report `installed and current` with `SessionStart`/`SessionEnd`/`PreToolUse`; the installer also refreshed their worktree copies. Bash-tool gotcha hit twice: zsh does not word-split `$h` in `for h in "name ip"; set -- $h`, producing an empty ssh host that reads as "Host key verification failed" -- use explicit addresses. |
| 2026-09-14 | side-finding | Every subagent's claim open/close ran on the git fallback (hub unreachable) and each swept the others' uncommitted TASK_CLAIMS entries (remedy (a), preserved, named in completion notes). Separately, the umbrella shared checkout has been refusing ref convergence since 2026-09-13T18:09Z (35 ahead / 55 behind by the end of this run); pushes succeed via the throwaway-worktree retry, but the checkout's working copy no longer receives origin's changes. Already chipped: `chip-checkoutdiverged-dlaptop-ree-working-master-g5`. Operator work per `cloud5_stale_scripts_wedge_staged_20260814.md` sections 5-6. |

### Re-measure (2026-09-24)

chip `chip-20260915-token-split-remeasure-b2`, session `orchb0924-h3`. Window: sessions started
2026-09-15..09-24 (the B2/B2-round-2 rewording landed 2026-09-14). Method:
`REE_assembly/scripts/token_split_measure.py --report`, both `--since 2026-09-15` and trailing
(no `--since`, 21-day mtime window); umbrella `CLAUDE.md` and the four large skills also checked
by static `wc -c` against their WI-A pre-B2 baseline and their post-B2-round-2 landed size
(`git show <landing-sha>:<path> | wc -c`), since the dynamic script has no per-skill breakdown
(only `nested_memory` CLAUDE.md paths).

**`--since 2026-09-15`: 294/1638 candidates fitted, 47,096 turns.** Per-turn R^2 median **0.9977**
(p10 0.9925), residual 0.8% -- a real, non-vacuous fit (CLAUDE.md docstring's own trap: never read
the summed-error check). Sample is not thin (>>30 fitted).

| figure | WI-I baseline (since 2026-09-08, 2026-09-14) | this re-measure (since 2026-09-15) | delta |
|---|---|---|---|
| FIXED PROMPT share | 34.81% (section 7.2, context_budget_restructure_plan.md) | **35.19%** | +0.38 pp -- HELD, not a regression |
| cache READ share | 97.18% | 97.06% | -0.12 pp -- HELD |
| cache CREATION share | 2.81% | 2.94% | +0.13 pp |
| median per-turn cache-read share | 99.05% | 99.31% | +0.26 pp -- improved |
| cold-turn misses | 0/1,665 (0.00%) | 36/46,802 (0.08%) | small new nonzero rate, still low |

Trailing (no `--since`, 1532/1638 fitted, 285,823 turns, pre-restructure-dominated -- context only
per the section 7.2 convention): FIXED PROMPT 38.77%, cache READ 97.64%, median per-turn
cache-read 99.47%. Consistent direction with the `--since` figures.

**Static file-size check -- the leading indicator, and the actual finding of this re-measure.**
The dynamic SHARE figures above read as flat/held, but the underlying FILES that feed the fixed
prompt have regrown substantially in the 10 days since the B2-round-2 landing (`c4b3502e4` +
siblings, 2026-09-14) -- three of five now exceed even the PRE-B2 bloated baseline the whole
rewording effort was measured against:

| file | pre-B2 (WI-A audit, 2026-09-14) | post-B2-round-2 landed | now (2026-09-24) | vs post-B2 | vs pre-B2 |
|---|---|---|---|---|---|
| `.claude/skills/queue-experiment/SKILL.md` | 154,138 | 147,839 (`b4a7ca8fa`) | 169,682 | **+14.8%** | **+10.1% (worse than before B2)** |
| `.claude/skills/governance/SKILL.md` | 113,915 | 112,688 (`5353929cb`) | 128,712 | **+14.2%** | **+13.0% (worse than before B2)** |
| `.claude/skills/failure-autopsy/SKILL.md` | 116,603 | 110,103 (`d119d519f`) | 119,946 | +9.0% | +2.9% (worse than before B2) |
| `.claude/skills/metaworker-dispatch/SKILL.md` | 141,357 | 132,496 (`9102e5b4b`) | 143,666 | +8.4% | +1.6% (worse than before B2) |
| `CLAUDE.md` (umbrella) | -- (not separately audited pre-B2 by this table) | 132,010 (`c4b3502e4`) | 139,030 | +5.3% | n/a |

All five files have regrown past their B2-round-2 trimmed size within 10 days; queue-experiment
and governance have regrown past their ORIGINAL pre-rewording size, i.e. the rewording's static
gain on those two is already fully erased and reversed. This has not yet shown up as a SHARE
regression in the dynamic measurement above (fixed-prompt share is flat) because the fitted
window's session mix and other context (tool results, harness injections) also moved, diluting
it -- but it is the mechanism section 6's "restful" framing warned about and is the reason this
chip exists rather than a one-off check.

**Regression check.** `grep -n "regression" WORKSPACE_STATE.md` since 2026-09-15 (14 hits):
none concern the B2 rewording itself or a governance/queue-experiment rule content regression --
they cover unrelated topics (EXP-id staleness fix, GOV-APPLY-1 override blindness, a negative
instrument's own false positive, etc.). `grep -n "reworded\|rewording"` since 2026-09-15: the
only hits are unrelated claim-content rewordings (ARC-094, MECH-013), not skill/CLAUDE.md rule
content. **No governance or queue-experiment session has reported a rule regression from the B2
wording changes in this window.**

**Verdict.** The rewording HELD on every dynamic share/cache figure measured (fixed-prompt share
+0.38pp, cache-read share -0.12pp, both within noise; per-turn cache-read median and miss rate
both fine) -- no evidence of the projected gain reversing YET in the numbers that actually gate
governance's WI-I baseline, and no session has reported a content/rule regression. But the static
file-size check (not part of the original WI-I instrument, added here because the dynamic SHARE
is a lagging indicator of file growth) shows the underlying skills and CLAUDE.md regrowing fast
enough that two of the four large skills are already net WORSE than before B2 ever ran, only 10
days post-landing. **Recommend, do not build:** re-run this same check again in 2-3 weeks: if the
fixed-prompt SHARE has by then moved materially off 34.8-35.2%, the file-size regrowth is the
explanation, and the fix is a second, lighter B2-style trim pass -- not a change to the OLS
instrument or the rewording rule itself (out of scope for a measurement chip; GOV-HELDOUT-1
would apply to any rule-text change).
