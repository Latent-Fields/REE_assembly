# Friday Governance Prep — 2026-04-17

Generated: `2026-04-17T14:17:55Z`

---

## Pending Experiment Reviews (2)

| Run ID | Outcome | Claims Tested | Notes |
|--------|---------|---------------|-------|
| `v3_exq_321a_mech090_bistable_gate_20260416T200620Z_v3` | FAIL | MECH-090 | Bistable gate hold rate test; needs /diagnose-errors review |
| `V3-EXQ-321a` (runner entry) | UNKNOWN | — | No indexed result file; add to `discussed_experiment_dirs` after discussion |

**Context on EXQ-321a:** The runner shows this as UNKNOWN (no manifest found), but there is a
matching indexed FAIL entry for the same experiment — these are two views of the same run.
Both the FAIL result and the UNKNOWN runner entry must be cleared during the review session.

---

## Promotion/Demotion Agenda (2 items requiring user decision)

Only `pending_user` items are listed. The 33 `applied` items are stable holds — no action needed.

### 1. MECH-230 — `promote_to_provisional` (pending_user)
- **Current status:** candidate
- **Evidence:** overall_conf=0.815, conflict_ratio=0, exp_entries=2, lit_entries=4 (4 supports, 0 weakens, 1 mixed)
- **Context:** EXQ-328b was reclassified `non_contributory` (2026-04-17) — a training-budget
  artifact, not a falsification. Substrate confirmed implemented. Prior FAILs (EXQ-233/238/247/328)
  attributed to pre-step EMA seeding measurement bug.
- **Options:**
  - Promote now (conf=0.815, zero conflict, substrate implemented)
  - Hold until one additional confirming run (more robustness)
  - Hold + targeted literature triangulation

### 2. SD-023 — `promote_to_provisional` (pending_user)
- **Current status:** candidate
- **Evidence:** overall_conf=0.76, conflict_ratio=0.333, exp_entries=2, lit_entries=4 (5 supports, 1 weakens, 0 mixed)
- **Context:** No evidence quality note in current manifest. Moderate evidence base.
- **Options:**
  - Promote now (conf=0.76, low conflict)
  - Hold until one additional confirming run
  - Hold + targeted literature triangulation

---

## Weekend Context

### Queue Depth
- **Total items in queue:** 20 (0 queued/ready, 17 pending, 3 claimed)
- **Claimed items:**
  - `V3-EXQ-325a` — SD-021 descending pain modulation retest (claimed by DLAPTOP-4.local, 2026-04-17T09:08Z — currently running)
  - `V3-EXQ-330a` — SD-013 contrastive counterfactual retest (claimed by DLAPTOP-4.local, 2026-04-14T23:42Z — **stale 39h, may need claim reset**)
  - `V3-EXQ-328b` — MECH-230 z_goal latent structure (claimed by ree-cloud-1, 2026-04-13T08:26Z — **stale 4 days, cloud runner may be offline**)
- **Next up when runner free (top pending):**
  1. `V3-EXQ-326` — SD-015/MECH-216/SD-012 wanting-gradient nav fix
  2. `V3-EXQ-321b` — MECH-090 bistable vs legacy gate (follow-on to EXQ-321a FAIL)
  3. `V3-EXQ-395` — MECH-220 harm hub behavioral probe
  4. `V3-EXQ-375` — MECH-073 valence geometry discriminative pair
  5. `V3-EXQ-326a` — SD-015 nav integration fix (z_resource encoder wiring)

### Blocked SDs
- **SD-011** (dual nociceptive streams): hold_candidate_resolve_conflict. Bridge approach ruled out (EXQ-093/094). z_harm_s forward model (ARC-033) required.
- **SD-012** (homeostatic drive): hold_candidate_resolve_conflict. Seeding works (C1 PASS), but downstream goal-to-behavior pathway fails. Blocker for multiple MECH-112/SD-015/MECH-216 experiments.
- **SD-015** (resource encoder): hold_candidate_resolve_conflict. 11 experiments, conflict_ratio=0.933. EXP-0091 handcrafted resource_indicator test needed.

### Mandatory Decision Checkpoints Due 2026-04-20
The backlog has 59 high-priority items with decision checkpoints due in 3 days. Top claims:
MECH-098, ARC-016, SD-015, MECH-075, SD-005, SD-003, ARC-032, MECH-116.
These are all currently at `hold_candidate_resolve_conflict` or `hold_pending_v3_substrate` —
the checkpoint is a reminder to confirm the hold is still appropriate, not a forced promotion.

### Governance Pipeline Warnings
11 experiments without `evidence_direction_per_claim` on multi-claim manifests (blanket fallback applied):
- EXQ-074e/f (MECH-112/117), EXQ-076e/f (MECH-116/ARC-032), EXQ-243 (INV-045/MECH-123),
  EXQ-242 (SD-017/ARC-045/MECH-166), EXQ-247 (SD-011/SD-012/ARC-033/ARC-030),
  EXQ-038 (ARC-016/MECH-093), EXQ-046 (ARC-007/SD-004)

---

*Read-only prep. No claims modified. No experiments marked reviewed.*
