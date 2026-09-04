# STAGED (not applied): `/thought-digestion v3-closure` -- 2026-09-04 unattended campaign

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

**Started:** 2026-09-04T21:02:59Z · **Session:** `thought-digestion-v3-20260904` (Mac, main checkout, no worktree)
**Mode:** unattended / staged-for-review, GROUPED (wave-of-groups, edge-first, `cap=5 floor=3.0`, lettered
families atomic, a group edge must include at least one STRUCTURAL signal -- token overlap alone never
reaches the floor). Draft-only: every wave's agent output is appended here verbatim; the user reviews the
whole batch once and the orchestrator applies only what is approved, then `build_claims_json.py` + commit.

**Deviation from the skill, stated plainly:** the skill's generic "Unattended / overnight mode" says to
stage to an untracked scratch file. This campaign stages to THIS tracked file instead, committed
pathspec-limited under the session's own TASK_CLAIMS entry, because untracked staging was lost once before
(chip-20260807-thoughtdigestion-trial-5: worktree GC'd before the drafts were read). The pattern follows
`thought_digestion_staged_2026-08-08_trial2_5claims.md`.

**Scope:** `closure_status.md` "Remaining work to close v3" (33) + "Assembly frontier" (10) -> 41 core
claim ids, expanded one hop along `depends_on` (240), intersected with the undigested backlog
(no `what_would_answer`, no `digestion_note`, `implementation_phase` not in v4/v5/v6/post_v5), plus
lettered-family closure -> **47 claims in 21 groups (10 solos)**. Wave 1 of 2026-08-27 (17 claims,
REE_assembly 25c05dbd6e) is already applied and therefore excluded.

**Prior drafts found and handed to agents (extract-before-invent):** MECH-485 (loop branch
`thought-loop/digestion-2026-08-25`, with the user's own `human_review_note`); ARC-113 (pilot wave
`thought_digestion_v3closure_wave1_drafts_20260826.md`, never applied).

| group | members | fan-in | why grouped |
|---|---|---|---|
| G1 | MECH-181, MECH-353, MECH-354, SD-017, SD-083 | 24 | SD-017 sleep-phase hub: SD-083/MECH-354/MECH-181 all `depends_on` it; MECH-353~354 same batch + namespace |
| G2 | MECH-074, MECH-074a-d | 8 | lettered family (amygdala read/write head split) -- atomic |
| G3 | MECH-104, MECH-106, MECH-234, MECH-250, SD-105 | 2 | control-plane commitment namespace; 104->106 `depends_on`; interrupt/release/entropy-floor siblings |
| G4 | ARC-048, INV-057, MECH-182, MECH-192 | 5 | ARC-048->MECH-192 `depends_on`; signal-legibility namespace |
| G5 | ARC-120, ARC-121, SD-034 | 12 | ARC-121->SD-034 `depends_on`; earned-authority / shared epistemic state |
| G6 | MECH-294, MECH-341, MECH-442 | 11 | MECH-442 `depends_on` both; action-diversity through commit |
| G7 | MECH-206, MECH-288, SD-084 | 10 | MECH-288->SD-084 `depends_on`; hippocampal comparator / event-segment |
| G8 | ARC-057, SD-024, SD-025 | 8 | SD-024<->SD-025 and ARC-057->SD-025 `depends_on`; DA / curiosity |
| G9 | MECH-349, MECH-527 | 3 | rule-mint / attractor-escape namespace |
| G10 | ARC-061, SD-047 | 1 | ARC-061->SD-047 `depends_on`; reafference comparators |
| G11 | ARC-029, MECH-025b (+MECH-025 read-only context) | 0 | committed/uncommitted modes namespace |
| solos | MECH-273, MECH-258, MECH-485, ARC-113, ARC-037, INV-104, INV-063, MECH-332, MECH-474, SD-063 | -- | no structural edge >= floor to any other undigested claim |

---

## GOVERNANCE FLAGS (collected across waves -- read these FIRST)

_(appended as waves land)_

---
