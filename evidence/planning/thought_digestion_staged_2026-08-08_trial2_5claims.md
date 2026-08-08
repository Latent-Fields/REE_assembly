# STAGED (not applied): `/thought-digestion` drafts (trial 2) for INV-004, SD-033e, MECH-264, INV-073, MECH-138

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

- Drafted: 2026-08-08 (see per-section timestamps; wave in flight at commit time)
- Session: `metaworker-chip-20260808-thoughtdigestion-trial2-5` (headless dispatch chip,
  `[chip_ref: chip-20260808-thoughtdigestion-trial2-5]`)
- Base: `REE_assembly` `2a256cef32`
- Mode: **unattended / draft-only**, per `.claude/skills/thought-digestion/SKILL.md`
  "Unattended / overnight mode". Wave size = 5, one wave. Write policy:
  draft-only-stage-for-review. Nothing minted to `claims.yaml` or
  `manual_proposals.v1.json`.

**Deviation from the skill, stated plainly:** the skill's overnight-mode step 2 says to stage
drafts to an *untracked* scratchpad file. That is correct for an interactive overnight `/loop`
where the same live user returns to the same session. It is WRONG for a headless `claude -p`
worker in a throwaway git worktree: an untracked file there is orphaned the instant the process
exits, and the worktree is GC-eligible the moment this chip resolves with a clean tree
(`scripts/hygiene_routine_tick.py` flags it; a dispatcher then removes it). That is exactly what
destroyed trial 1's review artifact (`chip-20260807-thoughtdigestion-trial-5`) -- an untracked
file at the worktree root, reaped before the user could read it. So this trial stages to a
TRACKED `evidence/planning/` path, committed pathspec-limited under this session's active
TASK_CLAIMS entry (which also stops the runner-heartbeat autostash from reverting it before
commit). It touches nothing else. This mirrors the proven pattern in
`thought_digestion_staged_2026-08-07_mech485_q090.md`.

**WIP NOTE (this commit):** skeleton committed for durability while the 5 drafting agents are
in flight. Per-claim sections are appended as agents return; the final commit carries all five.

---

## GOVERNANCE FLAGS (read first, separate from the per-claim drafts)

_(populated after the wave returns; `NONE` if nothing qualifies)_

---

## Per-claim drafts

_(appended as the wave completes)_
