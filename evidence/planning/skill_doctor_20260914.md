<!-- SKILL_DOCTOR_TABLE_VERSION: 2026-09-14.1 -->
# Headless skill-doctor table (WI-J measurement)

**Method note (read this first):** `/skill-doctor` (Claude Code 2.1.269, the installed
version at measurement time; the plan cites 2.1.261) is an interactive slash command that
this session cannot run headlessly. This file is a **headless approximation** built by hand
from the filesystem and this project's own transcript corpus, standing in for a real
`/skill-doctor` run until one can be done interactively (WI-J's own "then, turn off what is
never used" step still requires that follow-up -- this file supplies the measurement half only).
Two things a real `/skill-doctor` run would give that this file cannot: (1) the exact
tokenizer's token count, vs this file's `chars/4` estimate; (2) visibility into whether a
plugin skill's body was ever actually loaded into context on invocation (loading behaviour is
an implementation detail this measurement cannot observe from outside).

**Corpus scanned:**
- 1692 transcript `.jsonl` files across the main checkout project dir
  (`/Users/dgolden/.claude/projects/-Users-dgolden-REE-Working/`) and every matching
  `.claude/worktrees/*` project dir for this repo.
- 906,293 lines scanned, 174,586 JSON-parsed after a cheap
  substring pre-filter (`"Skill"` or a user-role line), 0 parse errors.
- Date range: **2026-06-24 to 2026-09-14**.
- 1692 distinct session files touched (== files_scanned; every file yielded at
  least one timestamped record).
- Detection: a `tool_use` block with `name=="Skill"` (its `input.skill`/`input.name`), OR a
  user-role text block whose stripped text starts with `/<name>`. Two path-shaped false
  positives from the slash-text heuristic (`/Users/.../remote_pytest.sh`,
  `/Users/.../audit_stashes.py` -- literal absolute paths typed in a message, not slash
  commands) were excluded by hand. In this corpus the slash-text path caught **zero** genuine
  skill invocations -- every real invocation surfaced as a `Skill` tool_use block, which is the
  harness's actual representation once a typed `/name` resolves. Cross-validated with a second,
  independent regex pass (`"skill":"<name>"` literal match) -- same counts.
- Scripts: `scan_transcripts.py`, `inventory_skills.py`, `inventory_plugin_ua.py`,
  `compute_plugin_desc.py`, `scheduled_cross_check.py`, `headless_caller_check.py` (all run from
  the scratchpad, not checked in). Est. tokens = `len(chars)/4`, rounded.

---

## Table 1 -- Project skills (`.claude/skills/*/SKILL.md`, dual-mirrored to `.agents/skills/`)

None of these 29 carry YAML frontmatter (CLAUDE.md "Skills" rule, confirmed on disk for all 29).
The description injected into every session's system prompt is therefore just the file's H1 line
(verbatim; confirmed against the live "available skills" listing for this session) -- a few
tokens each, not a real description. Body cost is paid only when the skill is actually invoked.

| Skill | Body KB | Body tok (est) | Desc tok (est) | Interactive invocations | Sessions | Last used | Headless/scheduled callers | Never invoked interactively |
|---|---:|---:|---:|---:|---:|---|---|:---:|
| `queue-experiment` | 150.5 | 38,410 | 4 | 259 | 259 | 2026-09-11 | igw_routine_tick.py, metaworker-dispatch SKILL.md, route-exq-723a-jlens-build-decision |  |
| `metaworker-dispatch` | 138.0 | 35,254 | 5 | 0 | 0 | — | metaworker-dispatch SKILL.md | **FLAG** |
| `failure-autopsy` | 113.9 | 29,014 | 4 | 45 | 45 | 2026-09-11 | check-v3-exq-697-residue-separability, exq-700b-autopsy-then-governance, failure-autopsy-owed-sweep, failure-autopsy-sweep, metaworker-dispatch SKILL.md, route-exq-723a-jlens-build-decision |  |
| `governance` | 111.2 | 28,354 | 4 | 10 | 8 | 2026-09-04 | exq-700b-autopsy-then-governance, igw_routine_tick.py, metaworker-dispatch SKILL.md, ree-friday-governance-prep, ree-governance-cycle |  |
| `session-land` | 77.1 | 19,734 | 3 | 424 | 420 | 2026-09-14 | failure-autopsy-sweep, igw-intent-soak-eval-flag-flip, igw_routine_tick.py, metaworker-dispatch SKILL.md, ree-lit-pull-am-b, ree-morning-digest-b, ree-token-split-remeasure, ree-zombie-session-reaper |  |
| `morning-digest` | 62.8 | 15,987 | 4 | 20 | 20 | 2026-09-14 | — |  |
| `account-handover` | 51.3 | 13,144 | 4 | 3 | 3 | 2026-09-11 | metaworker-dispatch SKILL.md |  |
| `metaworker-orchestrate` | 42.4 | 10,860 | 6 | 9 | 3 | 2026-09-02 | metaworker-dispatch SKILL.md |  |
| `thought-digestion` | 41.6 | 10,645 | 4 | 21 | 21 | 2026-09-08 | metaworker-dispatch SKILL.md |  |
| `metaworker-repair` | 41.6 | 10,640 | 4 | 5 | 4 | 2026-09-08 | metaworker-dispatch SKILL.md |  |
| `diagnose-errors` | 33.3 | 8,504 | 6 | 6 | 6 | 2026-08-25 | exq-700b-autopsy-then-governance, failure-autopsy-sweep, igw_routine_tick.py, route-exq-723a-jlens-build-decision |  |
| `dual-insights` | 28.2 | 7,172 | 3 | 2 | 2 | 2026-08-19 | — |  |
| `humanizer` | 26.3 | 6,722 | 9 | 0 | 0 | — | — | **FLAG** |
| `implement-substrate` | 25.1 | 6,406 | 7 | 69 | 69 | 2026-09-11 | igw_routine_tick.py, metaworker-dispatch SKILL.md, route-exq-723a-jlens-build-decision |  |
| `inter-governance-brief` | 20.3 | 5,196 | 6 | 1 | 1 | 2026-08-02 | — |  |
| `cross-field` | 18.3 | 4,663 | 8 | 0 | 0 | — | — | **FLAG** |
| `steward` | 17.0 | 4,333 | 2 | 0 | 0 | — | — | **FLAG** |
| `lit-pull` | 16.7 | 4,270 | 6 | 53 | 53 | 2026-09-14 | igw_routine_tick.py, metaworker-dispatch SKILL.md |  |
| `claim-synthesis` | 15.0 | 3,840 | 4 | 8 | 8 | 2026-09-07 | — |  |
| `thought-ingestion` | 14.9 | 3,824 | 4 | 5 | 5 | 2026-09-08 | — |  |
| `cowork` | 13.3 | 3,390 | 5 | 0 | 0 | — | — | **FLAG** |
| `update-docs` | 10.2 | 2,590 | 5 | 33 | 33 | 2026-09-14 | nightly-documentation-update |  |
| `metaworker-learning` | 9.8 | 2,519 | 5 | 3 | 3 | 2026-09-08 | — |  |
| `zombie-reaper` | 9.7 | 2,460 | 3 | 1 | 1 | 2026-08-27 | ree-zombie-session-reaper |  |
| `claim-target` | 7.3 | 1,852 | 3 | 0 | 0 | — | — | **FLAG** |
| `view-experiments` | 4.0 | 1,024 | 4 | 0 | 0 | — | — | **FLAG** |
| `sync` | 2.8 | 727 | 2 | 12 | 12 | 2026-09-07 | — |  |
| `worktree-sessions` | 2.8 | 717 | 4 | 1 | 1 | 2026-08-27 | — |  |
| `list-skills` | 2.7 | 689 | 5 | 1 | 1 | 2026-08-02 | — |  |
| **TOTAL (29)** | **1108.1** | **282,940** | **133** | **991** | | | | |

---

## Table 2 -- Plugin skills, grouped by plugin

**Enablement note (measurement finding, corrects an assumption in the plan text):**
`~/.claude/plugins/installed_plugins.json` / `enabledPlugins` in `~/.claude/settings.json` list
only **two** marketplace-installed plugins for this user: `github@claude-plugins-official` and
`understand-anything@understand-anything` (directory marketplace,
`/Users/dgolden/understand-anything`). `bio-research`, `engineering`, and `anthropic-skills` are
**not** in that registry and have **no on-disk `SKILL.md`** anywhere under `~/.claude/plugins/`,
`~/.local/share/claude/`, or the rest of the home directory (confirmed by a full-tree
`find -iname SKILL.md` and a `strings` pass over the 2.1.269 binary, which contains no plaintext
match for their body content, only 6 hits for the literal token `anthropic-skills` and 0 for
`engineering:`). They are bundled directly into the Claude Code binary as default/built-in
plugins, not fetched or cached as files -- so **body byte-size for these three groups is not
measurable from outside an interactive `/skill-doctor` run**; only their description-line cost is
measurable, taken verbatim from this session's own injected "available skills" system-reminder
text (i.e., a real, currently-injected value, not a reconstruction).
`github@claude-plugins-official` (installed, enabled) ships **zero** skills -- it is MCP-tool-only
(no `SKILL.md` under its cache dir) -- so it contributes no description-token cost and is omitted
as an empty group below.

### understand-anything (9 skills, on-disk, frontmatter `description:` measured directly)

| Skill | Body KB | Body tok (est) | Desc tok (est) | Interactive invocations | Sessions | Last used |
|---|---:|---:|---:|---:|---:|---|
| `understand-anything:understand` | 44.5 | 11,358 | 30 | 30 | 30 | 2026-09-14 |
| `understand-anything:understand-domain` | 8.0 | 2,048 | 47 | 0 | 0 | — |
| `understand-anything:understand-dashboard` | 7.3 | 1,877 | 20 | 0 | 0 | — |
| `understand-anything:understand-knowledge` | 6.0 | 1,543 | 41 | 0 | 0 | — |
| `understand-anything:understand-diff` | 4.3 | 1,097 | 28 | 0 | 0 | — |
| `understand-anything:understand-figma` | 4.0 | 1,029 | 49 | 0 | 0 | — |
| `understand-anything:understand-explain` | 3.5 | 890 | 24 | 0 | 0 | — |
| `understand-anything:understand-onboard` | 3.5 | 884 | 22 | 0 | 0 | — |
| `understand-anything:understand-chat` | 3.3 | 826 | 24 | 0 | 0 | — |
| **Subtotal (9)** | | **21,552** | **285** | **30** | | |

### bio-research (6 skills, **body not on-disk -- description only**)

| Skill | Body | Desc tok (est) | Interactive invocations | Sessions | Last used |
|---|---|---:|---:|---:|---|
| `bio-research:scvi-tools` | N/A (bundled in binary) | 180 | 0 | 0 | — |
| `bio-research:scientific-problem-selection` | N/A (bundled in binary) | 146 | 0 | 0 | — |
| `bio-research:instrument-data-to-allotrope` | N/A (bundled in binary) | 145 | 0 | 0 | — |
| `bio-research:nextflow-development` | N/A (bundled in binary) | 90 | 0 | 0 | — |
| `bio-research:single-cell-rna-qc` | N/A (bundled in binary) | 80 | 0 | 0 | — |
| `bio-research:start` | N/A (bundled in binary) | 68 | 0 | 0 | — |
| **Subtotal (6)** | | **709** | **0** | | |

### engineering (10 skills, **body not on-disk -- description only**)

| Skill | Body | Desc tok (est) | Interactive invocations | Sessions | Last used |
|---|---|---:|---:|---:|---|
| `engineering:architecture` | N/A (bundled in binary) | 70 | 0 | 0 | — |
| `engineering:documentation` | N/A (bundled in binary) | 67 | 0 | 0 | — |
| `engineering:incident-response` | N/A (bundled in binary) | 66 | 0 | 0 | — |
| `engineering:debug` | N/A (bundled in binary) | 64 | 0 | 0 | — |
| `engineering:code-review` | N/A (bundled in binary) | 62 | 0 | 0 | — |
| `engineering:standup` | N/A (bundled in binary) | 62 | 0 | 0 | — |
| `engineering:system-design` | N/A (bundled in binary) | 62 | 0 | 0 | — |
| `engineering:deploy-checklist` | N/A (bundled in binary) | 61 | 0 | 0 | — |
| `engineering:testing-strategy` | N/A (bundled in binary) | 59 | 0 | 0 | — |
| `engineering:tech-debt` | N/A (bundled in binary) | 58 | 0 | 0 | — |
| **Subtotal (10)** | | **631** | **0** | | |

### anthropic-skills (11 skills, **body not on-disk -- description only**)

| Skill | Body | Desc tok (est) | Interactive invocations | Sessions | Last used |
|---|---|---:|---:|---:|---|
| `anthropic-skills:docx` | N/A (bundled in binary) | 254 | 0 | 0 | — |
| `anthropic-skills:pptx` | N/A (bundled in binary) | 240 | 0 | 0 | — |
| `anthropic-skills:xlsx` | N/A (bundled in binary) | 237 | 0 | 0 | — |
| `anthropic-skills:pdf` | N/A (bundled in binary) | 109 | 0 | 0 | — |
| `anthropic-skills:morning` | N/A (bundled in binary) | 85 | 0 | 0 | — |
| `anthropic-skills:skill-creator` | N/A (bundled in binary) | 80 | 0 | 0 | — |
| `anthropic-skills:schedule` | N/A (bundled in binary) | 52 | 0 | 0 | — |
| `anthropic-skills:explain-usage` | N/A (bundled in binary) | 48 | 0 | 0 | — |
| `anthropic-skills:import-memory` | N/A (bundled in binary) | 35 | 0 | 0 | — |
| `anthropic-skills:consolidate-memory` | N/A (bundled in binary) | 23 | 0 | 0 | — |
| `anthropic-skills:setup-claude` | N/A (bundled in binary) | 19 | 0 | 0 | — |
| **Subtotal (11)** | | **1182** | **0** | | |

---

## Summary

### Always-present description-token cost, by group

| Group | Skills | Desc tok (est) | Scope of injection |
|---|---:|---:|---|
| Project (`.claude/skills/`) | 29 | 133 | every session opened in this repo (any path under `/Users/dgolden/REE_Working`) |
| Plugin: understand-anything | 9 | 285 | every session for this user (all projects, plugin is user-scoped) |
| Plugin: bio-research (built-in, not in plugin registry) | 6 | 709 | every session for this user |
| Plugin: engineering (built-in, not in plugin registry) | 10 | 631 | every session for this user |
| Plugin: anthropic-skills (built-in, not in plugin registry) | 11 | 1182 | every session for this user |
| Plugin: github (installed, enabled) | 0 | 0 | ships MCP tools only, no skills |
| **Plugin subtotal** | **36** | **2807** | |
| **GRAND TOTAL** | **65** | **2940** | |

Not tabulated (out of WI-J's named plugin scope but observed in this session's own injected
skills list, for completeness): 17 further Claude Code core/built-in skills with no plugin
prefix (`design`, `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`,
`update-config`, `keybindings-help`, `code-review`, `simplify`, `fewer-permission-prompts`,
`loop`, `schedule`, `claude-api`, `workflow-authoring`, `run`, `init`, `security-review`) --
rough lower-bound estimate from truncated description text: **~630 desc tok**, not included in
the grand total above since precise text wasn't captured for every one.

### Plugins with ZERO invocations in the corpus (candidates to disable at plugin level -- recommendation only, per WI-J; this file does not disable anything)

- **bio-research** (6 skills, 0 invocations) -- REE_Working is neurobiology-adjacent by subject
  matter but the project's own literature/data pipeline is bespoke (`/lit-pull`, PubMed efetch,
  `claims.yaml`); none of the 6 bio-research skills (instrument-data-to-allotrope, nextflow,
  scientific-problem-selection, scvi-tools, single-cell-rna-qc, start) matches a workflow this
  repo actually runs.
- **engineering** (10 skills, 0 invocations) -- generic SWE skills (architecture, code-review,
  debug, deploy-checklist, documentation, incident-response, standup, system-design, tech-debt,
  testing-strategy) that this project's own skill set (`/session-land`, `/queue-experiment`,
  `/diagnose-errors`, `/failure-autopsy`) already covers in REE-specific form.
- **anthropic-skills** (11 skills, 0 invocations) -- office-document and account-utility skills
  (`docx`, `pptx`, `xlsx`, `pdf`, `morning`, `schedule`, `explain-usage`, `consolidate-memory`,
  `import-memory`, `setup-claude`, `skill-creator`); REE's own deliverables are markdown/JSON/git,
  not office documents. **Caveat:** `anthropic-skills:schedule` and `anthropic-skills:skill-creator`
  are plausibly useful outside REE work on this same account; disabling is a per-plugin, not
  per-skill, action, so this is a real tradeoff, not a free cut.
- **understand-anything** is NOT zero -- `understand-anything:understand` alone has 30 invocations
  across 30 sessions (most recent 2026-09-14); its 8 sibling skills (chat/dashboard/diff/domain/
  explain/figma/knowledge/onboard) are individually at zero but sit under the same enabled plugin,
  so plugin-level disable is not applicable here.

### Project skills with zero interactive invocations

**Must stay (do not delete) -- headless/scheduled callers exist even though `/skill-doctor`-style
detection would flag them:** none of the true zero-interactive skills below have a confirmed
headless/scheduled caller in this pass. See the `metaworker-dispatch` note directly below --
it is the one skill this measurement expected to find a caller for and did not.

- **Zero interactive invocations, zero headless/scheduled caller found:** `claim-target`, `cowork`, `cross-field`, `humanizer`, `steward`, `view-experiments`.
  Per CLAUDE.md WI-J's own "Explicitly NOT doing" list, absence of a caller in this pass is
  NOT grounds to delete -- a scheduled task or headless script that doesn't literally spell the
  skill name (e.g. invokes it only via a human-typed `/name` in a session this corpus doesn't
  cover, or via a differently-worded reference) would be invisible to both this scan and to
  `/skill-doctor` itself.
- **`metaworker-dispatch`** (141 KB, the 2nd-heaviest body) is a genuine anomaly worth surfacing:
  zero `Skill` tool_use invocations AND zero literal `/metaworker-dispatch` slash-text in the
  entire corpus (cross-checked two independent ways), yet the skill is extensively *discussed*
  (the bare string "metaworker-dispatch" appears in 1,132 of the 1,692 transcript files) and is
  explicitly designed for interactive use via `/loop 5m /metaworker-dispatch` per its own SKILL.md.
  `dispatch_remote_launch.py` and `igw_routine_tick.py` both reference it only in prose/docstrings
  (they reimplement its Step 4c directly in Python rather than invoking the skill), so neither is
  a real headless caller. Two readings: (a) it genuinely runs only from sessions/paths this scan
  doesn't cover, or (b) the `/loop`-wrapped invocation pattern doesn't surface as a `Skill`
  tool_use or literal slash-text in the transcript at all. Worth a real `/skill-doctor` check.

### Top 5 heaviest bodies (measurable-on-disk skills only -- project + understand-anything; the
three built-in plugins have no measurable on-disk body)

| Rank | Skill | Body KB | Body tok (est) |
|---|---|---:|---:|
| 1 | `queue-experiment` | 150.5 | 38,410 |
| 2 | `metaworker-dispatch` | 138.0 | 35,254 |
| 3 | `failure-autopsy` | 113.9 | 29,014 |
| 4 | `governance` | 111.2 | 28,354 |
| 5 | `session-land` | 77.1 | 19,734 |

---

## Feeds back to `context_budget_restructure_plan.md` WI-2

WI-2 moved umbrella CLAUDE.md sections into skills; this measurement gives the number that move
cost in always-present terms. The **description-token share is small**: 133 tok for all
29 project skills (avg 4.6 tok/skill) against a CLAUDE.md that runs many
thousands of tokens on its own -- because none of the 29 carry frontmatter, their injected
"description" is just an H1 title, not a real trigger description. The **real fixed-prompt cost
of the plugin layer is far larger and orthogonal to WI-2**: 2807 tok across the 36
plugin skills (understand-anything real descriptions average 31.7 tok/skill --
~14x a project skill's, because they DO carry real frontmatter descriptions; anthropic-skills
averages 107.5 tok/skill). So WI-2's own budget question ("did moving CLAUDE.md
content into skills reduce the always-present floor") reads cleanly at 133 tok added by
the project-skill descriptions themselves; the 2807 tok of plugin-description floor
sits above and independent of that move, and WI-C's plan to add `effort:`/frontmatter to project
skills should budget for the description-length jump this measurement shows plugin skills already
pay -- a real, human-authored description costs roughly 15-50x an H1-only one.

