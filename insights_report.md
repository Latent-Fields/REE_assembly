# Project Insights — 2026-06-19

Generated: 2026-06-19T14:11:25Z

> **Data-freshness caveat:** `runner_status.json` was last written `2026-06-09T06:00Z` —
> ~10 days stale. Under Phase 3 the coordinator DB is the authoritative run-state store and
> `runner_status.json` is no longer the live mirror. The experiment-health counts below are
> therefore a trailing snapshot through 2026-06-09; the most recent runs (688/MECH-044,
> 468e, 514s, 654-series) appear only in `pending_review.md`, not in the counts. Treat the
> rates as trend indicators, not a current census.

---

## Experiment Health

- **Total runs (through 2026-06-09):** 840 — PASS: 283 | FAIL: 437 | ERROR: 87 | UNKNOWN: 32 | INCONCLUSIVE: 1
  - **Error rate:** 10.8% (87 / 807 PASS+FAIL+ERROR) — within normal band; not dominated by crashes.
  - FAIL:PASS ≈ 1.5:1, expected for a falsification-first programme (FAIL = ran to completion, criteria not met).

- **High-iteration chains** (distinct lettered iterations ≥ 5 — repeated diagnose/redesign cycles).
  *Claim attribution drifts across letters; counts are continuity flags, not single-claim verdicts:*
  - **EXQ-085 — 14 iterations, all FAIL.** Tagged MECH-071 only at 085c; the chain's FAILs are goal-navigation, not harm-calibration (canonical claim-drift trap). Migrated to SD-015 → 622/626 ladder under a new number; not abandoned.
  - **EXQ-514 — 13 iterations** (SD-049). Reached PASS at 514g/h/i, then forked to the non-degenerate identity-distinct-wanting retest (514j/k/l FAIL) and continues live as 514s (MECH-436 drive-coupling, in pending_review). Healthy iteration toward a moving target, not a stall.
  - **EXQ-418 — 13 iterations.**
  - **EXQ-543 — 10 iterations** (MECH-309 → ARC-062). 543 PASS, then 543b–543k all FAIL after re-tag to ARC-062 — the ARC-062 multi-rule-context ceiling (10 failure records in substrate_queue).
  - **EXQ-490 — 10 iterations** (MECH-269b → Q-040 → MECH-295). Q-040 cohort contaminated+superseded 2026-05-07; resolved to PASS at 490k under MECH-295.
  - **EXQ-445 / 047 — 9 each.**
  - **EXQ-603 — 8 iterations** (Q-045 / scaffolded_sd054). Reached PASS at 603j; readiness flipped true 2026-06-11 (603n).
  - **EXQ-610 — 6 iterations** (INV-074 crystallization-necessity). 610/610a ERROR → 610b–610f FAIL; longest unresolved retest chain.

- **Recurring trouble spots** (claim_ids in ≥ 2 ERROR entries):
  - **UNTAGGED — 39 ERRORs** (largest class by far; addressed by the 2026-06-06 validate_queue WARN-on-claimless-entry change, but legacy residue remains).
  - **MECH-112 — 4 ERRORs**; **MECH-163 — 3 ERRORs**; then 2 each: SD-018, SD-012, SD-003, MECH-188, MECH-116, MECH-113, INV-052, ARC-007.

- **Stalled chains** (FAIL with no same-number successor; verify migration before shelving):
  - **EXQ-085** — 14 FAIL, no same-base successor. Per the no-rerun policy it migrated to SD-015 → 622/626; confirm the successor before treating 085 as dead.
  - **EXQ-610f** (INV-074) — latest is FAIL; crystallization-necessity retest unresolved across 6 letters. Check whether the MECH-341 substrate is now deemed sufficient (making crystallization unnecessary) vs. a genuine open retest.
  - **EXQ-543k** (ARC-062) — latest FAIL; gated on the multi-rule-context substrate (still blocked, see below).
  - *Live (not stalled):* 514s, 688 (MECH-044), 654e are in `pending_review.md` awaiting adjudication, not abandoned.

---

## Substrate Bottlenecks

- **Ready to build now** (`ready: true`, not yet implemented): **MECH-258**, **ARC-058** (both `candidate_v3_pending`). Everything else flagged ready is already `implemented`/`validated`.
- **Highest failure-record concentration** (experiments that failed because the substrate was missing/insufficient):
  - **scaffolded_sd054_onboarding — 28 failure records** (now `ready: true`, readiness flipped 2026-06-11 via 603n; the long tail was the cue-to-action selection-authority ceiling).
  - **modulatory-bias-selection-authority — 15** (implemented; the dominant E3-selection bottleneck — F monopolises 88–89% of selection variance per V3-EXQ-571).
  - **MECH-256 — 10** (blocked_by MECH-269); **ARC-062 — 10** (the 543 chain); **ARC-065 — 7**; **commitment-closure-control-plane — 6**; **SD-037 — 6**; **crf-availability-maintenance — 5**; **SD-016 — 5**.
- **Deeply blocked clusters** (long unresolved dependency chains — the structural ceiling on V3 progress):
  - **SD-033 family** (SD-033/b/c/d/e) — all blocked on MECH-094 + MECH-261 + ARC-035 (the contextual-memory / write-gate-policy cluster, off the V3 critical path).
  - **SD-026/027/028** — blocked on INV-034/037/038 + MECH-007.
  - **ARC-064/MECH-316/317/318** — blocked on the **multi-rule-context substrate** + ARC-062 Phase-3 wiring (same root as the 543 chain).
  - **MECH-314a-Phase-2** — blocked on a **user architecture decision** (Candidate 5A vs 5B/5C/3), not on code.

---

## Governance State

- **Claims pending V3 substrate** (`v3_pending: true`): **214**.
- **Pending promotion/demotion decisions requiring user action** (`decision_status: pending_user`): **4** — **MECH-442** (hold pending V3 substrate), **Q-054** (narrow open question), **Q-055**, **Q-056** (hold pending V3 substrate). The other 143 decisions are auto-`applied` (held/suppressed).
- **Evidence superseded** (rework — manifests with `evidence_direction: "superseded"`): **43** runs. Correctly excluded from scoring by the indexer.
- **Recommendation mix:** 25 `hold_candidate_resolve_conflict`, 20 `held_v4_by_architectural_commitment`, 8 `narrow_open_question`, remainder `applied`.

---

## Literature Coverage

- **Priority-1 (high) backlog items still open: 0.** All 82 high-priority backlog items need **experimental** (not literature) evidence — 51 in_progress, 31 covered. Literature is not the bottleneck.
- **Open literature items: 15** — all **low** priority (the Q-059…Q-077 cluster). 1 literature item covered.
- **351 literature directories** present under `evidence/literature/`.
- **Recently covered** (from WORKSPACE_STATE): RHM-6 (MECH-129/164 relational-harm + love-as-care), DRV-3 (MECH-394/SD-060 drive-arbitration → minted MECH-435), plus AE-9/ABM-9/GDL-8/eth8/PA-7 concurrent V4/V5 pulls. Lit-pull is running smoothly and headless.

---

## Human-Intervention Patterns

- **Architecture/design decisions are the real gate, not literature or compute:**
  - **MECH-314a-Phase-2** is blocked purely on a user architecture choice (Candidate 5A vs alternatives).
  - The **B+D memory-allocation-gate** candidate claims are explicitly held for a user fold-vs-separate / amend-vs-new decision.
  - 4 `pending_user` governance decisions outstanding.
- **Claim-attribution disputes recur in diagnose/autopsy work** — the 085 (MECH-071 drift), 543 (MECH-309→ARC-062), and 490 (MECH-269b→Q-040→MECH-295) chains all required re-tagging mid-chain. Several recent sessions (640a, 569g/i, 654d) were dedicated to adjudicating self-routed diagnostic labels (precondition_unmet / vacuous_pass) before they could drive governance — this is now a formal gate (`pending_review.md` flags 3 such self-routes today).
- **Duplicate-spawn / already-done sessions** — multiple WORKSPACE entries (IGW-029 NO-OP, 640a autopsy already complete, GAP-A 569h route done by 3 sessions) show parallel sessions re-doing landed work. The IGW respawn-loop fix (2026-06-04, COOLDOWN_HOURS=48) addressed the auto-spawn side.
- **Low-friction headless tasks:** lit-pull (no disputes in recent sessions), queue-experiment (smoke+validate gates catch issues pre-queue), insights/morning-digest.

---

## Recommendations

1. **Resolve the 4 `pending_user` governance decisions** (MECH-442, Q-054, Q-055, Q-056) and the **MECH-314a-Phase-2 architecture choice** — these are the only items blocked purely on human input, and MECH-314a unblocks a Phase-2 substrate chain. Highest leverage, zero compute.
2. **Build the two ready substrates: MECH-258 and ARC-058** (`ready: true`, `candidate_v3_pending`). They are the only unimplemented features with all deps met. ARC-058 also unblocks MECH-257.
3. **Adjudicate the MECH-044 (688) / 654e / 514s pending-review items** before they age — 3 carry untrusted self-route labels (`precondition_unmet`) that must be autopsied, not trusted, before clearing any `v3_pending` flag or minting substrate. Run `/failure-autopsy` per `proposal_diagnostic_adjudication_gate`.
4. **Decide INV-074's status explicitly** — 610f is the longest unresolved retest chain (6 letters, ERROR→FAIL). Either confirm MECH-341 makes crystallization unnecessary (close the chain) or redesign; don't leave it spinning.
5. **Attack the dominant bottleneck, not the symptoms** — modulatory-bias-selection-authority (15 failure records; F monopolises 88–89% of E3 selection variance, V3-EXQ-571). The 543/ARC-062 and scaffolded_sd054 failure tails both terminate at the same selector. Per the conversion-ceiling synthesis, attack channel B (top-k shortlist, 569i thin margin) or rebalance F, rather than queuing more downstream diversity probes that drown at the selector.
