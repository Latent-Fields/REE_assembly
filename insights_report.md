# Project Insights — 2026-05-17

Generated: 2026-05-17T20:15:16Z

---

## Experiment Health

- **Total runs:** 720 (PASS: 164 | FAIL: 286 | ERROR: 77 | UNKNOWN/other: 193 | error rate: 14.6% of P+F+E)
- **High-iteration experiments** (3+ lettered iterations) — 74 base IDs hit 3+; the heaviest:
  - **EXQ-085 — 14 iterations, ALL 14 FAIL** (SD-015 sorted-RF proximity / position-invariant encoder). No PASS in any iteration. Worst single chain in the project.
  - **EXQ-418 — 13 iterations** (SD-017 action_bias_div). 6 FAIL / 4 UNKNOWN / 2 ERROR / 1 PASS. Eventually cleared via the sleep-substrate Phase 2 line (EXQ-418l + EXQ-565 PASS 2026-05-15).
  - **EXQ-514 — 10 iterations** (SD-049 BG gating under StepHarness). 3 FAIL / 3 UNKNOWN / 1 ERROR / **3 PASS** — resolved.
  - **EXQ-047 — 9 iterations** (MECH-095 TPJ CE routing). 8 FAIL / 1 PASS — resolved late.
  - **EXQ-445 — 9 iterations** (SD-032b dACC reef). 8 UNKNOWN / 1 ERROR — reef-superseded, mostly reclassified non_contributory.
  - EXQ-540 (7, MECH-307, ends PASS), EXQ-433 (7, SD-029 reef), EXQ-074/076 (6 each, MECH-112/116 — ERROR-heavy), EXQ-166 (6, SD-003/ARC-033, all UNKNOWN), EXQ-325/490 (6 each).
- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **MECH-112 — 4 ERROR** (wanting/liking dissociation, EXQ-074 cluster) — top crash magnet.
  - **MECH-163 — 3 ERROR** (dual-system planned/habitual).
  - SD-003 (2), ARC-007 (2), MECH-113 (2), MECH-116 (2), SD-018 (2), SD-012 (2), MECH-188 (2), INV-052 (2).
  - By base EXQ: EXQ-074 (4 ERROR), EXQ-075/076/084 (3 each).
- **Stalled chains** (FAIL/ERROR, never PASS, not in current queue): 146 — but most are *diagnostic probes* whose negative result fed forward into a substrate-plan revision, not true dead ends. Genuine attention items:
  - EXQ-085 — 14× FAIL, SD-015 — no successor queued; the only chain that iterated to exhaustion with zero PASS.
  - Recent diagnostic FAILs feeding the ARC-065 warm-start finding: EXQ-569 / 572 / 573 / 575 (2026-05-16) — superseded by the EXQ-ISEF-001..006 line now in queue.
  - EXQ-549 (ARC-066/MECH-320), EXQ-550 (MECH-269) — FAIL 2026-05-11, no lettered successor.

---

## Substrate Bottlenecks

Substrate queue: 85 entries (45 implemented-ish, 10 ready, 26 with unresolved deps, rest mixed states). `next_implement_substrate` pointer is currently **null** — next target is a governance decision (cleared 2026-04-27, never re-pointed).

- **Ready** (ready flag, no unresolved deps, not yet implemented): SD-019a, SD-037, MECH-269b-followup-A, MECH-204, MECH-307, MECH-258, ARC-058, INF-ENV-001, INF-ENV-003, INF-ENV-004.
- **Blocked** (26, deepest dependency fan-in):
  - SD-033 family — SD-033/b/c/d/e all blocked on MECH-094/261/151/152/235/ARC-035 (OCD-axis cluster, 5 dependents stacked).
  - SD-024/025/026/027/028 — SD-004 / INV-034/37/38 chain.
  - **ARC-065 blocked on Q-043/Q-044/Q-045** (weight + 3-arm + 4-arm ablations); MECH-313/314 each blocked on one of those Q-ablations. This is the live critical path — the diversity/warm-start bottleneck.
- **SDs with failure records** (experiments failed against them):
  - **MECH-256 — 10 failure records** (event-conditioned comparator; candidate_v3_pending, blocked on MECH-204/269/307). Biggest substrate-attributed failure sink.
  - SD-016 — 4 (parked_pending_env_entropy_precondition).
  - SD-015 — 3 (EXQ-085's claim; ties the 14-FAIL chain to a substrate gap, not just a script bug).
  - SD-029, SD-049, MECH-307 — 3 each.

---

## Governance State

- **Total claims:** 645
- **Claims pending V3 substrate** (`v3_pending: true`): 109 (plus 223 with `implementation_phase: v3`).
- **Pending promotion/demotion decisions:** 0 — all 108 rows in the decision queue are `applied` (last generated 2026-05-17T12:26Z). 148 hold_pending_v3_substrate, 56 hold_candidate_resolve_conflict, 19 narrow_open_question, 1 promote — all resolved/applied.
- **Evidence superseded (rework):** ~119 manifest files marked `evidence_direction: superseded`. Persistent rework load, concentrated in the reef/monostrategy supersession chains (EXQ-433/445/325/490) and the SD-017 sleep-substrate line.

---

## Literature Coverage

This project does not track literature through the evidence backlog (251 backlog items: 250 `experimental`, only **1** `literature`). Literature is tracked via `evidence/literature/targeted_review_*` dirs and lit-pull sessions.

- **Targeted-review dirs on disk:** 281 — very broad coverage.
- **Only open literature backlog item:** EVB-PINNED-Q019 (Q-019 BG three-loop gating — O'Reilly & Frank 2006, Hazy 2007, Aron 2007, Brittain & Brown 2014, Buckner 2008, Crick/Zikopoulos). Long-pinned, still open.
- **Recently covered (from WORKSPACE_STATE):** ARC-067 (boredom, 8 entries, 2026-05-10), ARC-066 (tonic vigor, parallel), ARC-068 (opportunity cost), INV-044/MECH-166/ARC-045, SD-033a (Johnson 2016). ARC-066/067/068 child-MECH design now complete (MECH-330/331; ARC-068 collapsed into MECH-320) — biology-before-formal gate cleared for that family.

---

## Human-Intervention Patterns

From WORKSPACE_STATE session history (2026-05-04 → 2026-05-17):

- **Recurrently needed human input:**
  - **diagnose-errors / failure-autopsy** — recurring. EXQ-577 autopsy explicitly paused for user routing ("both — enrich + relax"); ERROR-chain fix sessions recur every few days.
  - **Substrate/cluster registration** — non_deficit_action_drives (ARC-066/067/068) and policy_primitive_granularity (ARC-069/070/071) clusters were both user-triggered from phenomenology observations, then required design pauses and slot-split governance flags (ARC-067 → MECH-330/331).
  - **ARC-065 diversity/warm-start** — repeatedly bounced back to the user: smallest-patch confirmation (v_t_floor), warm-start gate diagnosis, EXQ-573 null-result interpretation. The dominant open investigation.
- **Low-friction headless tasks:**
  - **lit-pull** — completed cleanly in every recent session (ARC-067, ARC-066, INV-044 cluster) with no rework.
  - **infant_substrate GAP closures** (GAP-7..14) — GAP-10..14 each written, smoke-passed, queued in single sessions on 2026-05-17 without intervention.
  - **nightly update-docs** and **governance-cycle** — running clean, 0 indexed pending at each cycle.

---

## Recommendations

1. **Resolve the ARC-065 / Q-043-044-045 critical path.** It blocks ARC-065, MECH-313, MECH-314 and is the diagnosed dominant bottleneck (warm-start failure: diversity biases are literally zero at cold start, not miscalibrated). The EXQ-ISEF-001..006 line is queued/claimed to address it — prioritise reviewing those on completion before any Q-043/044/045 retest.
2. **Retire or escalate EXQ-085 (SD-015).** 14 consecutive FAILs with no successor and 3 SD-015 substrate failure records: either commission an SD-015 substrate redesign via /implement-substrate or formally close the chain. Iterating the script further is not productive.
3. **Unblock MECH-256 (10 failure records).** It is the largest failure sink and gates SD-029/SD-032 comparator work; its blockers (MECH-204, MECH-269, MECH-307) are all either ready or implemented — sequence those to clear it.
4. **Triage MECH-112 ERROR recurrence** (4 ERRORs in the EXQ-074 cluster) through /diagnose-errors — it is the single most crash-prone claim and likely an attribute-path/API drift issue per the copy-and-modify failure mode.
5. **Re-point `next_implement_substrate`.** Null since 2026-04-27; 10 ready substrate items (SD-019a, MECH-204, MECH-307, MECH-258, ARC-058, INF-ENV-001/003/004) are available with no live pointer directing implement-substrate sessions.
