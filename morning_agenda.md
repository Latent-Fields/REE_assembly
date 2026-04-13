# Morning Agenda — 2026-04-13

Generated: 2026-04-13T06:12:45Z (governance.sh freshly run)

---

## Queue Status

- **Total pending: 0** — ALERT: Queue is empty
- ALERT: Queue low -- 0 pending experiments. Experiments should be queued immediately for the runner.
- Last experiments ran: 2026-04-12 (dry/smoke runs 10:15-11:16, EXQ-354 real run 16:24)

---

## Experiments Awaiting Review (8 indexed / 0 runner-only)

> **Important note on dry runs:** 7 of the 8 pending experiments have `_dry_` in their run IDs,
> indicating they were executed as smoke tests (script validation runs), not full experimental
> runs. Their metrics objects are empty `{}`. Their FAIL outcomes confirm substrate gaps still
> present but should not be weighted as independent experimental evidence. EXQ-354 (no `_dry_`)
> is the only genuine scientific run.

---

### [EXQ-354] -- mech112_wanting_liking_confirmation -- PASS
- **Claims tested:** MECH-112 (candidate) -- E3 structured goal latent / behavioral
  wanting-liking dissociation
- **Key metrics:** wanting_l1_fraction=0.96, liking_l1_fraction=0.47, dissociation=0.49,
  wanting_resource_rate=0.15
- **Classification:** evidence (real run, not dry)
- **Governance impact if confirmed:** Supports MECH-112 behavioral dissociation arm. wanting
  signal reliably exceeds liking fraction (wanting_l1=0.96 >> liking_l1=0.47). Strong signal.
  Adds to "supports" side of MECH-112 conflict-resolution pile.
- **Note:** EXQ-328a (same session, same day) FAILED the latent structure aspect of MECH-112.
  These may be testing complementary sub-mechanisms (behavioral dissociation vs. z_goal
  structural representation). Atomic split of MECH-112 worth considering.

---

### [EXQ-326] x3 -- wanting_gradient_nav_fix -- FAIL (3/6 criteria)
*(Three runs: 10:15, 10:17, 10:19 UTC -- all dry)*
- **Claims tested:**
  - SD-015 (candidate -- z_resource encoder): `does_not_support`
  - SD-012 (candidate -- homeostatic drive): `does_not_support`
  - MECH-216 (provisional -- e1_predictive_wanting): `supports`
- **Key metrics:** Empty -- dry run
- **Classification:** diagnostic smoke test confirming SD-015 and SD-012 substrate gaps persist
- **Governance impact if confirmed:** SD-015 and SD-012 continue to fail under nav-fix script.
  Three runs in 4 minutes is a repeated smoke test, not independent evidence. MECH-216 provisional
  status is incidentally corroborated.
- **Note:** 3 near-identical runs in 4 minutes = repeated smoke-test invocations during script
  development. Treat as a single diagnostic datapoint.

---

### [EXQ-328a] x2 -- mech112_zgoal_structured_latent -- FAIL (5/10 criteria)
*(Two runs: 10:25, 11:16 UTC -- both dry)*
- **Claims tested:**
  - MECH-112 (candidate): `does_not_support` (latent z_goal structure)
  - SD-012 (candidate): `does_not_support`
- **Key metrics:** Empty -- dry run
- **Classification:** diagnostic -- z_goal latent structure aspect (distinct from behavioral
  dissociation tested in EXQ-354)
- **Governance impact if confirmed:** Adds opposing evidence for MECH-112 latent representation
  arm. Creates intra-MECH-112 split: EXQ-354 (behavioral) PASS vs EXQ-328a (latent) FAIL.
  SD-012 failure consistent with homeostatic drive substrate gap in substrate_queue.json.

---

### [EXQ-330a] -- sd013_contrastive_counterfactual_frac05 -- FAIL
*(Single run: 10:20 UTC -- dry)*
- **Claims tested:**
  - SD-013 (candidate -- E2_harm_s counterfactual training): `does_not_support`
  - ARC-033 (candidate -- E2_harm_s forward model architecture): `supports`
- **Key metrics:** Empty -- dry run
- **Classification:** diagnostic (SD-013 substrate gap) + evidence corroboration (ARC-033)
- **Governance impact if confirmed:** SD-013 counterfactual perturbation training still not
  producing unbiased signal at frac=0.5. ARC-033 per-claim override supports architecture.

---

### [EXQ-353] -- arc033_sd003_interventional_vs_observational -- FAIL
*(Single run: 10:24 UTC -- dry)*
- **Claims tested:**
  - ARC-033 (candidate): `supports`
  - SD-003 (validated): `supports`
  - SD-013 (candidate): `does_not_support`
- **Key metrics:** Empty -- dry run
- **Classification:** diagnostic (SD-013 gap) + evidence corroboration (ARC-033, SD-003)
- **Governance impact if confirmed:** SD-013 is the consistent failure point across EXQ-330a
  and EXQ-353. ARC-033 and SD-003 accumulate per-claim support from interventional design.
  SD-003 already validated -- additional corroboration only.

---

## Errors to Diagnose (0)

All 51 ERROR entries in runner_status.json have successors (lettered iterations or completed
follow-up runs). No unresolved errors requiring /diagnose-errors.

---

## Governance Agenda (0 pending_user decisions)

All 35+ recommendations in promotion_demotion_recommendations.md have `decision_status: applied`.
No governance decisions queued for user review.

Current landscape (informational -- no action needed):
- `promote_to_provisional` (applied 2026-03-29): MECH-057a
- `hold_candidate_resolve_conflict` (applied): ARC-026, ARC-030, ARC-032, ARC-033, ARC-041,
  ARC-042, INV-054, MECH-070, MECH-073, MECH-075, MECH-093, MECH-098, MECH-099, MECH-111,
  MECH-112, MECH-116, MECH-118, MECH-120, MECH-128, MECH-150, MECH-153, MECH-155, MECH-165,
  MECH-186, MECH-188, SD-011, SD-012, SD-013, SD-015
- `narrow_open_question` (applied): Q-019, Q-021, Q-022, Q-023, Q-024, Q-033
- `hold_pending_v3_substrate` (applied): MECH-072, MECH-135

---

## Literature Pull Candidates (Top 5)

| # | Claim | Priority | Subject | Existing dir? |
|---|-------|----------|---------|---------------|
| 1 | SD-013 | high | E2_harm_s counterfactual perturbation training requirement | No -- top priority |
| 2 | Q-036 | medium | (evidence_backlog item) | No |
| 3 | SD-019 | medium | (evidence_backlog item) | No |
| 4 | SD-022 | medium | (evidence_backlog item) | No |
| 5 | ARC-028 | medium | (evidence_backlog item) | No |

Also in medium backlog: MECH-057 (no dir), SD-003-prereq (targeted_review_sd_003 exists).

SD-013 is the clear top target: persistent dry-run failure today (EXQ-330a + EXQ-353), high
backlog priority, no existing targeted_review_sd_013 directory. A /lit-pull SD-013 session
would complement upcoming SD-013 experimental fixes.

---

## Serve.py Status

- RUNNING on port 8000

---

## Key Priorities for Today

1. **Queue experiments -- CRITICAL.** Queue is empty.
   - EXQ-330b: SD-013 fix (counterfactual perturbation signal not reaching threshold; run
     /diagnose-errors on EXQ-330a first to identify root cause)
   - EXQ-326a: nav-fix follow-up for SD-015 / SD-012 gaps
   - EXQ-328b: mech112 z_goal latent structure with SD-012 homeostatic fix
   - Note: EXQ-321a and EXQ-325a were written in yesterday's cowork session -- check whether
     they are actually present in the queue (queue shows 0 entries; these may have been removed
     after dry-run failures)

2. **Review EXQ-354 PASS.** Mark as reviewed, accept MECH-112 behavioral supports. Note the
   MECH-112 behavioral/latent split and decide whether atomic split is warranted.

3. **Batch-review dry runs (EXQ-326 x3, EXQ-328a x2, EXQ-330a, EXQ-353).** Quick batch
   classification as non_contributory (dry runs, no real metrics). They confirm substrate gaps
   are still active; no new scientific signal.

4. **Consider /lit-pull SD-013.** Highest-priority unmet literature target.

---

## Blocked Items

None. No TASK_CLAIMS collisions. All previous claims are `done`.

---

*Pipeline: governance.sh run at 06:11 UTC. 8 new run-packs synced. 445 claims total.
ree-v3 pull encountered transient git error (bad object refs/heads/main 2) but local repo
shows up to date with origin/main -- no data loss.*
