# Dispatch Bundle: Weekly Handoff Format Update (2026-02-14)

Purpose: align `ree-experiments-lab` and `ree-v1-minimal` to the shared weekly handoff packet format used by `REE_assembly`.

Reference template (normative):

- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`

---

## Prompt 1: `ree-experiments-lab`

```md
You are Codex operating in `ree-experiments-lab`.

Goal: update weekly handoff reporting to match REE_assembly's shared producer handoff template.

Reference (normative):
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/CROSS_REPO_SYNC_POLICY.md`

Required deliverables:
1. Add weekly handoff report output in this repo using the template sections and required columns exactly.
2. Create one current-cycle handoff report file from latest runs.
3. Wire CI to fail if the weekly handoff report is missing required sections/columns.
4. Ensure report includes:
   - contract lock reference/hash
   - schema validation status
   - deterministic seed status
   - hook coverage status (or `N/A` if not applicable)
   - run-pack inventory table
   - claim summary table
   - open blockers

Acceptance checks:
1. Weekly handoff file is present and matches template section names.
2. Every listed run row includes `evidence_direction` and `pack_path`.
3. CI fails if required handoff fields are removed.
4. Output a concise summary with:
   - file path for weekly handoff report
   - CI check command/workflow name
   - any unresolved blockers

Constraints:
- Keep changes scoped to reporting/process/CI for handoff formatting.
- Do not refactor unrelated experiment logic.
```

---

## Prompt 2: `ree-v1-minimal`

```md
You are Codex operating in `ree-v1-minimal`.

Goal: update weekly handoff reporting to match REE_assembly's shared producer handoff template for parity/backstop lane reporting.

Reference (normative):
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/planning/WEEKLY_HANDOFF_TEMPLATE.md`
- `/Users/dgolden/Documents/GitHub/REE_assembly/evidence/experiments/CROSS_REPO_SYNC_POLICY.md`

Required deliverables:
1. Add weekly handoff report output in this repo using the template sections and required columns exactly.
2. Create one current-cycle handoff report file from latest qualification/parity runs.
3. Wire CI to fail if the weekly handoff report is missing required sections/columns.
4. Ensure report includes:
   - contract lock reference/hash
   - schema validation status
   - deterministic seed status
   - hook coverage status (or `N/A` if not applicable)
   - run-pack inventory table
   - claim summary table
   - open blockers

Parity-specific requirement:
- Include a short parity note in blockers or summary:
  - where `ree-v1-minimal` agrees/disagrees with latest `ree-v2` qualification outcomes (if available this cycle).

Acceptance checks:
1. Weekly handoff file is present and matches template section names.
2. Every listed run row includes `evidence_direction` and `pack_path`.
3. CI fails if required handoff fields are removed.
4. Output a concise summary with:
   - file path for weekly handoff report
   - CI check command/workflow name
   - parity note status
   - unresolved blockers

Constraints:
- Keep changes scoped to reporting/process/CI for handoff formatting.
- Do not refactor unrelated harness logic.
```
