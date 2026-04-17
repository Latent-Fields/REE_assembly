# Project Insights — 2026-04-17

Generated: 2026-04-17T19:02:04Z

---

## Experiment Health

- **Total completed runs:** 515 (PASS: 102 | FAIL: 238 | ERROR: 64 | UNKNOWN: 111)
- **V3-only:** PASS: 86 | FAIL: 225 | ERROR: 64 | UNKNOWN: 111 — error rate 17% over scored runs
- **Recent ERROR wave (2026-04-17):** 12 EWIN-PC setup crashes in one cluster (setup exit 0.1–0.2s). All re-queued on Mac with `a`/`b`/`c` suffixes. Clean handoff, not a code-level regression. Root cause: EWIN-PC environment; machine affinity dropped to `"any"` after requeue.

- **High-iteration experiments (4+ lettered iterations — rework hotspots):**
  - EXQ-085 — 14 iterations (MECH-112/SD-012 goal-lift, z_goal seeding)
  - EXQ-047 — 9 iterations
  - EXQ-002, EXQ-020 — 7 iterations each (SD-003 counterfactual, SD-009 contrastive)
  - EXQ-074, EXQ-076, EXQ-166 — 6 iterations each (MECH-113/114, MECH-163)
  - EXQ-016, EXQ-015, EXQ-018, EXQ-023, EXQ-030, EXQ-049, EXQ-046, EXQ-058, EXQ-059, EXQ-075, EXQ-071, EXQ-084 — 4 iterations each
  - 59 base EXQs have ≥3 iterations total

- **Recurring trouble spots (claim_ids in 2+ ERROR entries):**
  - MECH-112: 4 ERRORs (goal-lift / z_goal structure)
  - SD-003: 2 ERRORs (counterfactual attribution — continuing chain)
  - ARC-007, MECH-113, MECH-116, SD-018, MECH-163, SD-012, MECH-188, INV-052: 2 ERRORs each

- **Stalled chains** (FAIL with no successor queued or completed): 130 entries, dominated by early V3 sequence against SD-003 (EXQ-002r6, 006–012, 024, 025) and SD-007/SD-008 (EXQ-020d, 022, 023b). Most of these are now structurally superseded by SD-010/011 redesign; treat as legacy rather than live stalls. Worth sweeping to confirm `evidence_direction: "superseded"` is applied in manifests.

---

## Substrate Bottlenecks

- **Ready SDs (all deps met — implementable now):** SD-013, SD-015, SD-019, SD-020, SD-021, SD-022 (6 total)
- **Blocked SDs:** 0 (queue has no unresolved dependencies)
- **SDs with failure records** (experiments failed awaiting cleaner substrate):
  - SD-015: 3 failures — unblocks MECH-162, Q-030, INV-065; highest leverage
  - SD-022: 2 failures — unblocks SD-019/020/021/MECH-219/Q-036 (broadest downstream reach)
  - SD-013, SD-020, SD-021: 1 each
- **Observation:** All 6 ready SDs have at least one (SD-019 none) failure record — these are exactly the substrate gaps causing the high-iteration rework chains above (EXQ-085, EXQ-074/076, EXQ-166). EXQ-326a, EXQ-332a, EXQ-330a, EXQ-431 (claimed today) are the active iterations on this cluster.

---

## Governance State

- **Claims pending V3 substrate (`v3_pending: true`):** 4 in claims.yaml
- **Pending promotion/demotion decisions:** 38 total entries in queue; 8 `pending_user` (MECH-057a, MECH-230, SD-011, SD-014, SD-023 among them)
- **Evidence superseded / rework markers in claims.yaml:** 34 mentions
- **Dominant recommendation mode:** `hold_candidate_resolve_conflict` — 26+ candidate claims stuck behind unresolved evidence conflicts, not fresh evidence gaps

---

## Literature Coverage

- **Open literature items in evidence_backlog:** 19 (all medium or low priority; **0 priority-1 items open** — P1 coverage is complete)
- **Open lit claims:** onboarding, Q-036, ARC-028, MECH-057, SD-003-prereq, SD-018, MECH-122, Q-019, Q-025–032, Q-037–039
- **Recently covered (from WORKSPACE_STATE last ~30 sessions):** SD-011, SD-014, SD-019, SD-021, SD-022, SD-023, ARC-016, ARC-026, ARC-032, MECH-090 Layer 3, MECH-095, MECH-098, MECH-155, MECH-230, Papez circuit, zebrafish sleep, dementia-attribution, sleep-phase mechanisms

---

## Human-Intervention Patterns

- **Recurrently needed human input:**
  - Governance `pending_user` decisions: 8 currently awaiting review (SD-011/014/023, MECH-057a/230 promotions) — consistent with `feedback_governance_interactive` memory requiring user pause before claim status changes
  - `hold_candidate_resolve_conflict` queue (26+ items): conflict resolution is a known non-headless step
  - Diagnose-errors sessions: 3 in last ~10 days (04-15, 04-17, plus -b scheduled); consistently trigger requeue decisions
- **Low-friction headless tasks:**
  - Lit-pulls: ~25 successful lit-pull sessions in the recent history, all self-contained
  - Implement-substrate: SD-014 h/l valence writes, MECH-090 Layer 1+2, MECH-216, SD-013/015/019/020/021 — landed without rework
  - queue-experiment sessions: typically single-shot
  - sync, morning-digest: routine scheduled runs

---

## Recommendations

1. **Close the ready-SD backlog before opening new hypotheses.** SD-022 unblocks 5 downstream claims and has 2 recorded failures; SD-015 unblocks 3 and has 3. Prioritize the already-claimed iterations (EXQ-326a, EXQ-332a, EXQ-330a, EXQ-431) and verify they land before spawning new EXQ chains. EXQ-085 (14 iterations) and EXQ-047 (9) are the clearest signs of chasing symptoms without the substrate fix.
2. **Sweep stalled FAILs for supersession tagging.** 130 stalled entries dominated by pre-SD-010/011 SD-003 work. Mark `evidence_direction: "superseded"` on manifests where the redesign has made the original hypothesis obsolete, so governance conflict ratios reflect live evidence only. This should reduce the 26-item `hold_candidate_resolve_conflict` queue meaningfully.
3. **Action the 8 `pending_user` governance decisions in one pass.** MECH-230, SD-011, SD-023 are candidate→provisional promotions with applied recommendations; these will cascade unblock downstream claims and are cheap turns compared to another experiment round.
