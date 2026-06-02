# Project Insights — 2026-06-02

Generated: 2026-06-02T06:28:02Z

---

## Experiment Health

- **Total completed runs:** 794 (PASS: 195 | FAIL: 319 | ERROR: 87 | UNKNOWN: 193)
  - **Error rate:** 87 / (195+319+87) = **14.5%** (ERROR / PASS+FAIL+ERROR, UNKNOWN excluded)
  - **DATA-QUALITY FLAG:** 193 runs (24% of all rows) are `UNKNOWN`. This is the
    `experiment_runner.py:1394` silent-drop bug (cloud-worker result loss). UNKNOWN rows
    carry no usable scientific signal and inflate iteration counts. Before requeueing any
    "lost" run, check `evidence/` for an actual manifest (per `reference_cloud_workers`).

- **High-iteration experiments** (3+ lettered iterations — repeated diagnose/autopsy cycles):
  - **EXQ-085 — 14 iterations** (085, b, c, e–o) — all **FAIL** — claims: MECH-071 — *never passed; longest dead chain* — **[2026-06-02 CORRECTION: heuristic artifact. Only 6 of 14 iterations carry MECH-071; 085h–085o re-tagged SD-015/ARC-030. MECH-071's criterion (C3) PASSED throughout; FAILs are C2 goal-navigation. MECH-071 RETAINED provisional. See evidence/planning/exq085_mech071_disposition_2026-06-02.md]**
  - **EXQ-418 — 13 iterations** (SD-016 / SD-017) — mixed; 418f PASS, rest FAIL/UNKNOWN/ERROR
  - **EXQ-514 — 12 iterations** (SD-049) — 514g/h/i PASS, then 514j/k FAIL again
  - **EXQ-543 — 10 iterations** (MECH-309 → ARC-062) — 543 PASS then 9 consecutive FAIL on ARC-062
  - **EXQ-490 — 9 iterations** (Q-040 / MECH-269b / MECH-295) — all UNKNOWN/FAIL, none passed
  - **EXQ-445 — 9 iterations** — almost entirely UNKNOWN (data-quality, not science)
  - **EXQ-047 — 9 iterations** (SD-005 / MECH-095) — resolved: 047k PASS
  - Others ≥4: 540, 433, 325, 166, 076, 074, 397, 020, 612, 603, 563, 517, 476, 449, 324, 321, 254, 253

- **Recurring trouble spots** (claim_ids in 2+ ERROR entries):
  - **MECH-112 — 4 ERRORs** (top offender)
  - **MECH-163 — 3 ERRORs**
  - 2 ERRORs each: SD-018, SD-012, SD-003, MECH-188, MECH-116, MECH-113, INV-052, ARC-007
  - (39 ERROR rows have no claim_id attached — attribution gap)

- **Stalled chains** (terminal FAIL, no successor in current 3-item queue):
  - EXQ-085o — FAIL — MECH-071 — no fix queued (chain abandoned after 14 tries) — **[2026-06-02 CORRECTION: 085o is SD-015-tagged, not MECH-071; chain MIGRATED to SD-015 → active V3-EXQ-622/626/626a ladder, not abandoned. See disposition memo.]**
  - EXQ-490g — FAIL — Q-040/MECH-295 — no successor
  - EXQ-543k — FAIL — ARC-062 — gated on `543k_598`, no live successor
  - EXQ-616 — FAIL (2026-05-31) — Q-054 — no successor
  - EXQ-514k — FAIL (2026-06-01) — SD-049 — no successor
  - EXQ-603d — FAIL (2026-06-01) — Q-045 — no successor (recent; may be in flight)
  - *Active (not stalled):* EXQ-626→626a queued, EXQ-610a→610c queued

---

## Substrate Bottlenecks

- **Ready SDs** (`ready: true`, not yet implemented/validated):
  - SD-019a (harm_stream.immediate_affective_valence, prio 2)
  - SD-033b (pfc.ofc_analog_outcome_structure, prio 2)
  - MECH-258 (z_harm_a precision-weighted PE, prio 1, candidate_v3_pending)
  - ARC-058 (Shared HarmForwardTrunk — *competes with ARC-033*, prio 1)
  - MECH-090 (BetaGate commit-entry conjunction — validation V3-EXQ-592d queued)
  - scaffolded_sd054_onboarding (goal-pipeline training regime, prio 1, amend_pending)

- **Blocked SDs** (waiting on dependencies — 30 total). Deepest dependency knots:
  - SD-033 cluster (SD-033/b/c/d/e) — all gated on MECH-261 + MECH-094/ARC-035
  - SD-025 — blocked on 5 deps (SD-024, SD-004, ARC-057, MECH-111, INV-051)
  - SD-026/027/028 — INV-034/037/038 + MECH-007 chain
  - MECH-256 → blocked on MECH-269; MECH-257 → blocked on MECH-256 — **[2026-06-02 CORRECTION: not a stale edge. Base MECH-269 landed 2026-04-22 but the V_s-monostrategy blocker persisted (MECH-256 failures run through 2026-05-08) and live V_s work moved to the MECH-269b lineage (269b + followup-A implemented-but-unvalidated). `ready_blocked_by` confirms genuine. Correct fix = retarget the dep to MECH-269b, NOT delete.]**
  - ARC-064 / SD-054 / MECH-316/317/318 — all gated on **ARC-062 Phase 3 wiring**

- **SDs with failure records** (experiments failed because of missing/incomplete substrate):
  - **MECH-256 — 10 failures** (candidate_v3_pending, blocked on MECH-269) — *worst* — **[2026-06-02 CORRECTION: the 10 failures are the V_s-monostrategy substrate-ceiling pattern (shared across the 433/470/537 cluster), not MECH-256-specific bugs. Mechanism is wired end-to-end; genuine blocker is the upstream V_s work (MECH-269b lineage). See MECH-256 note above.]**
  - **ARC-062 — 9 failures** (phase_1, evidence-gated 543k/598) — drives the EXQ-543 chain — **[2026-06-02 CORRECTION: NOT a missing-substrate ceiling. The "rule-creator substrate" framing (543l/598b records) was superseded by the user-confirmed V3-EXQ-598 autopsy (2026-05-29): blocker is behavioral-diversity collapse, owned by the EXISTING ARC-065 (foundational upstream of ARC-062) + SD-056 (E2 action-divergence), which landed + passed falsifiers 569d/617 (2026-05-31). Remaining ARC-062 path is experimental (GAP-B re-falsifier), not new substrate. Scoping memo: evidence/planning/arc062_rule_creator_scoping_2026-06-02.md.]**
  - **SD-037 — 6 failures** (status `null` — not cleanly implemented; drove EXQ-418/490 churn) — **[2026-06-02 CORRECTION: SD-037 WAS implemented (implementation_status=implemented, implemented_utc 2026-04-25, readiness V3-EXQ-483b PASS, axis-a 620b PASS); only the top-level status field was a stale null, now fixed to `implemented` (commit eb6884b365). The 6 failure_records are env-curriculum tuning (axis-b sustained-window C3, V3-EXQ-625b autopsy), NOT substrate.]**
  - **scaffolded_sd054_onboarding — 6 failures** (amend_pending)
  - SD-016 — 4 (parked, env-entropy precondition); SD-049 — 4 (phase_1)
  - 3 each: SD-015, SD-029, MECH-307

- **Cross-reference (substrate ↔ high-iteration churn):**
  - ARC-062 (9 substrate failures) ⇒ EXQ-543 chain (10 iterations, 9 FAIL) — **[2026-06-02: the shared cause is behavioral-diversity collapse (ARC-065/SD-056 domain), now landing — see ARC-062 correction above]**
  - SD-037 (6 failures, never cleanly landed) ⇒ EXQ-418 (13 iter) + EXQ-490 (9 iter) churn — **[2026-06-02 CORRECTION: SD-037 was cleanly landed 2026-04-25; the churn is env-curriculum, not substrate]**
  - SD-049 (4 failures) ⇒ EXQ-514 chain (12 iterations)

---

## Governance State

- Claims marked `v3_pending: true` in claims.yaml: **116**
- Promotion/demotion decisions still **open**: **13** (109 already applied)
  - Standing recommendation mix: 150 `hold_pending_v3_substrate`, 50 `hold_candidate_resolve_conflict`, 1 `promote`
- Evidence superseded (rework manifests, `evidence_direction: "superseded"`): **249 runs**
- Substrate queue: 92 entries — 47 implemented, 9 candidate_v3_pending, plus a long tail of
  phase-1/partial states.

---

## Literature Coverage

- Explicit literature gaps in evidence_backlog (`evidence_needed` includes literature): **10 open**
  - medium: MECH-341, ARC-046, MECH-333, MECH-282, MECH-286, MECH-339, MECH-340, Q-054, Q-019
  - low: Q-055
  - (No priority-1/"high" items among the literature-gap subset — lit coverage is not the bottleneck.)
- Literature corpus is deep: **295 entries** under `evidence/literature/` (recent: goal/wanting-liking
  consolidation synthesis, object-bound incentive salience, V_s foundation reviews).
- Recent lit-pull targets (from WORKSPACE_STATE): goal/wanting/liking stream repair,
  object-bound incentive salience (2026-06-01).
- Note: all 258 evidence_backlog items show `status: open` — the backlog is not being
  status-closed as items are addressed, so "open" count is not a reliable progress signal here.

---

## Human-Intervention Patterns

Recent session-type distribution (last ~120 WORKSPACE_STATE headers):

| Session type | Count | Friction profile |
|---|---|---|
| queue-experiment | 20 | low — runs headless, skill-gated |
| **failure-autopsy** | 20 | **high** — diagnostic, needs user adjudication of root cause |
| governance | 16 | medium-high — pauses for user decisions per `feedback_governance_interactive` |
| diagnose-errors | 13 | high — claim_id disputes, fix-design choices |
| implement-substrate | 11 | high — most require plan/architecture confirmation pause |
| inter-governance-brief | 7 | medium |
| lit-pull / update-docs / morning-digest | low | low — headless-clean |

- **Recurrently needs human input:**
  - **failure-autopsy + diagnose-errors (33 of recent sessions combined)** — the dominant
    work mode is now *fixing failing experiments*, not running new ones. Most need user
    sign-off on root-cause classification (harness-bug vs substrate-regression) and on the
    recommended substrate-queue entry. E.g. V3-EXQ-626 (harness bug), 592f (MECH-090 admission-only).
  - **implement-substrate** — architecture-doc decisions (e.g. MECH-314a-Phase-2 awaiting user
    assent on Candidate 5A vs alternatives) repeatedly stall on user choice.
- **Low-friction headless tasks:** lit-pull, queue-experiment, morning-digest, update-docs,
  insights — these complete cleanly without disputes.

---

## Recommendations

1. **Triage the UNKNOWN backlog before any more requeues.** 193/794 runs (24%) are UNKNOWN from
   the cloud-worker silent-drop bug. Many high-iteration "chains" (EXQ-445, parts of 490/418/514)
   are inflated by lost results, not real scientific failures. Sweep `evidence/` for orphan
   manifests and reclassify; fix `experiment_runner.py:1394` to stop the leak.
   **[2026-06-02 PARTIALLY DONE: triage ran (unknown_results_triage_2026-06-02.md) — 183/193 relinked
   to real manifests, 0 disagreements, only 10 genuinely lost. The root-cause `experiment_runner.py:1394`
   fix is STILL OPEN (chip queued).]**

2. **Unblock the ARC-062 Phase-3 wiring keystone.** ARC-062 has 9 substrate failures, drives the
   EXQ-543 chain (10 iterations, 9 FAIL), and is the named blocker for ARC-064, SD-054,
   MECH-316/317/318. It is the single highest-leverage substrate item. SD-037 (6 failures, status
   `null`) is second — it never cleanly landed yet drove the EXQ-418/490 churn; either finish it
   or formally park it.
   **[2026-06-02 CORRECTED — scoped, memo evidence/planning/arc062_rule_creator_scoping_2026-06-02.md]:**
   ARC-062 needs NO new substrate. Per the user-confirmed V3-EXQ-598 autopsy (2026-05-29) the blocker
   is behavioral-diversity collapse, owned by the EXISTING ARC-065 + SD-056 — both landed + passed
   falsifiers (569d/617, 2026-05-31). Next ARC-062 action is a GAP-B re-falsifier on that substrate
   (`/queue-experiment`), gated on ARC-065's Q-043/44/45 ablations (Q-045=603e, 614d already queued).
   SD-037 was ALSO mis-flagged: it was cleanly implemented 2026-04-25; only the status field was a
   stale null, now fixed (eb6884b365). Real next step here is queue-experiment, not implement-substrate.

3. **Resolve MECH-256 / MECH-269 dependency knot.** MECH-256 carries 10 failure records and is
   blocked on MECH-269 (which itself has 2). This chain (→ MECH-257) is the deepest failure-loaded
   dependency in the substrate queue.
   **[2026-06-02 CORRECTION: not a "knot to clear." The dep is genuine — base MECH-269 landed
   2026-04-22 but the V_s-monostrategy blocker persisted and moved to the MECH-269b lineage. The 10
   failures are the shared V_s-ceiling pattern, not MECH-256 bugs. Correct action = retarget the dep
   edge to MECH-269b (the unresolved V_s work), deferred to the V_s-cluster owner.]**

4. **Close the EXQ-085 / MECH-071 chain.** 14 FAIL iterations, no successor, no PASS — formally
   declare it stalled (new number with a different hypothesis, or shelve MECH-071) rather than
   leaving it as open churn.
   **[2026-06-02 RESOLVED — user-approved disposition, memo evidence/planning/exq085_mech071_disposition_2026-06-02.md]:**
   Do NOT shelve MECH-071. MECH-071's calibration gradient (C3) PASSED in every iteration and is
   validated by EXQ-026/029; the recurring FAIL is C2 goal-navigation, owned by SD-015/MECH-112/ARC-030.
   The 8 MECH-071-tagged 085 manifests were reclassified `non_contributory` for MECH-071. The chain is
   closed as **migrated** (→ SD-015 → active V3-EXQ-622/626/626a), not stalled. The `/insights` Step 2
   heuristic has been updated (claim-continuity + per-criterion caveats) to prevent recurrence.

5. **Clear the 13 open promotion/demotion decisions** and adopt status-tracking on
   evidence_backlog (all 258 items still read `open`), so governance progress is measurable.
   **[2026-06-02 CORRECTION + PARTIALLY DONE: the "13 open" are all Q-claim narrowing reviews
   (Q-021/022/023/024/033/036/037/040/041/043/044) under `narrow_open_question` / `hold_pending_v3_substrate`
   with recommendation already `applied` — open *questions*, not pending promote/demote calls. The
   evidence_backlog status-tracking landed elsewhere (commit "backlog: derive evidence_backlog status
   open/in_progress/covered/superseded").]**
