# Morning Agenda -- 2026-04-28

Generated: 2026-04-28T04:22:09Z

---

## Queue Status
- Total pending: **2** (Mac: 0 | PC: 0 | EWIN: 0 | any: 2)
- **ALERT: Queue low -- fewer than 3 pending experiments.** Only V3-EXQ-495 (MECH-163 V3 full-completion gate, 1500 min) and V3-EXQ-490b (MECH-269b VsRolloutGate substrate-readiness probe, 320 min) remain. Queue replenishment needed today.
- No machine-pinned items.

---

## Experiments Awaiting Review (12 indexed / 3 runner-only)

The 12 indexed runs are repeat invocations of three experiment types. All PASS, all with per-claim direction overrides set.

### V3-EXQ-484 -- v3_exq_484_sd033a_distractor_resistance -- PASS (5 runs: 2026-04-26 10:11, 10:12; 2026-04-27 01:49, 01:59, 05:44)
- **Claims tested:** SD-033a (candidate, conf 0.879, exp 5 PASS / 0 FAIL, 22 entries), MECH-261 (stable, conf 0.894, 26 entries), MECH-262 (candidate, conf 0.881, 13 entries).
- **Per-claim direction:** all three `supports`.
- **Key metrics (latest run):** task arm drift = 0.567 (gate=1.0); replay arm drift = 0.050 (gate=0.05); planning arm drift = 0.567 (gate=1.0). Replay/task drift ratio ~0.09 -- replay-mode write gate freezes rule_state as predicted.
- **Classification:** evidence (MECH-262 signature ii, distractor-resistance under MECH-261 mode-conditioned write gating).
- **Governance impact if confirmed:** would add 5 supporting genuine_exp entries to MECH-262 (currently candidate, conf 0.881) and reinforce MECH-261 (already stable). SD-033a holds at `hold_pending_v3_substrate` per recommendation queue (substrate-readiness, not promotion).
- **Caveat from manifest notes:** signatures (i) abstraction and (iv) trained-head emergence remain deferred per SD-033a landing decision A2; head is untrained. So this confirms wiring, not learned-rule abstraction.

### V3-EXQ-485 -- v3_exq_485_sd033b_ofc_analog_landing -- PASS (4 runs: 2026-04-26 10:49; 2026-04-27 01:49, 02:00, 05:44)
- **Claims tested:** SD-033b (candidate, conf 0.91, lit-only 5 entries), MECH-261 (stable), MECH-263 (candidate, conf 0.914, lit-only 4 entries; **first experimental evidence**).
- **Per-claim direction:** all three `supports`.
- **Key metrics (latest run):** UC1 instantiation pass; UC2 gate_modulates_update delta=0.082 at gate=1, 0.0 at gate=0; UC3 zero-init contract holds; UC4 backward-compat (None) pass; UC5 reset clears state_code.
- **Classification:** diagnostic (substrate wiring; bias head is frozen-random with last Linear zeroed, so this is a zero-init contract check, not a biological-bias claim).
- **Governance impact if confirmed:** first experimental tag for MECH-263 and SD-033b; would add 4 substrate-wiring genuine_exp entries. Recommendation already queued as `hold_pending_v3_substrate` (pending_user) -- SD-033b/MECH-263 still need behavioural EXQs (devaluation sensitivity, perceptually-identical / task-distinct discrimination) before functional promotion.
- **Caveat from manifest notes:** MECH-263 functional signatures (a) devaluation, (b) same-sensory-input / different-task-role -- explicitly deferred to later EXQs.

### V3-EXQ-493 -- v3_exq_493_mech295_liking_bridge_validation -- PASS (3 runs: 2026-04-27 02:00, 03:38, 08:03)
- **Claims tested:** MECH-295 (candidate, conf 0.883, lit-only 6 entries; **first experimental evidence**), SD-012 (candidate, conf 0.763), SD-014 (candidate, lit-only conf 0.903), SD-015 (candidate, conf 0.747), MECH-117 (stable, conf 0.859).
- **Per-claim direction:** MECH-295 `supports`; SD-012, SD-014, SD-015, MECH-117 explicitly `non_contributory` (architectural prerequisites only -- excluded from scoring).
- **Key metrics (latest run):** UC1 importable; UC2 master-off no-op (bridge None); UC3 write side fires (n_write=30, n_cue=4, final_goal_norm=0.304); UC4 cue-side negative bias gradient ([-0.030, -0.150, -0.270] at low/mid/high prox -- bias_max_abs=0.27); UC5 severed-bridge collapse (bias_max_abs=0.0 with write_value=0.45); UC6 MECH-094 simulation gate honoured.
- **Classification:** diagnostic (substrate wiring + falsifiable cue-side necessity signature; behavioural EXQ-483-style approach_commit recovery deferred to a successor after V3-EXQ-490 lands).
- **Governance impact if confirmed:** first experimental entries for MECH-295. Recommendation already queued as `hold_pending_v3_substrate` (pending_user). Non-contributory tagging on SD-012/014/015/MECH-117 is correct -- this experiment does not test their independent claims.

### Cross-cutting note on the indexed pending set
- Multiple runs per experiment type are due to scheduled task invocations on both machines; outputs are reproducible across re-runs (same metrics on identical seeds). Reviewing one run per type covers the evidence; the rest are duplicates that still need to be either tagged reviewed (via run_ids) or excluded from scoring as duplicate-of-latest at /governance time.

---

## Errors to Diagnose (3)

These ERROR entries have no queued or completed lettered successor:

- **V3-EXQ-008**: SD-003 Larger World + 3x3 Observation -- ERROR (Non-zero exit code 1) -- 2026-03-17. Old V3 SD-003 attribution probe; needs `/diagnose-errors`. Claim: SD-003.
- **V3-EXQ-455a**: SD-032a salience coordinator behavioural -- V_s-enabled re-run -- ERROR (immediate exit) -- 2026-04-23 on DLAPTOP-4.local. Needs `/diagnose-errors`. Claim: SD-032a.
- **V3-EXQ-449c**: MECH-074b BLA retrieval bias on action selection -- V_s-gated -- ERROR (immediate exit) -- 2026-04-24 on DLAPTOP-4.local. Needs `/diagnose-errors`. Claim: MECH-074b.

The 449c / 455a fast-fail pattern (~0.05-0.1s) suggests an import or argparse-time error -- likely a quick fix once diagnosed.

---

## Governance Agenda (10 pending_user recommendations)

| Claim | Status | Recommendation | Conf | Sup/Weak |
|-------|--------|----------------|------|----------|
| **MECH-266** | candidate | **promote_to_provisional** | 0.853 | 5 / 0 |
| **MECH-267** | candidate | **promote_to_provisional** | 0.896 | 4 / 0 |
| **MECH-268** | candidate | **promote_to_provisional** | 0.851 | 2 / 0 |
| **SD-034** | candidate | **promote_to_provisional** | 0.856 | 5 / 0 |
| MECH-057b | candidate | hold_pending_v3_substrate | 0.870 | 3 / 0 |
| MECH-263 | candidate | hold_pending_v3_substrate | 0.914 | 4 / 0 |
| SD-033b | candidate | hold_pending_v3_substrate | 0.910 | 4 / 0 |
| Q-025 | open | narrow_open_question | 0.632 | 1 / 0 |
| Q-026 | open | narrow_open_question | 0.617 | 0 / 1 |
| Q-040 | open | narrow_open_question | 0.840 | 4 / 0 |

Four promotion-eligible claims -- MECH-266, MECH-267, MECH-268, SD-034 -- are all part of the SD-033 governance plan registered 2026-04-20. MECH-263 and SD-033b are likely candidates for promotion once SD-033b functional EXQs land (devaluation, task-role discrimination).

---

## Literature Pull Candidates (Top 5)

| # | Backlog ID | Claim | Priority | Recommendation | Existing entries |
|---|-----------|-------|----------|----------------|-----------------|
| 1 | EVB-0127 | onboarding | medium | collect_targeted_evidence | 0 |
| 2 | EVB-0128 | MECH-057 | medium | collect_targeted_evidence | 3 |
| 3 | EVB-PINNED-Q019 | Q-019 | medium | (pinned) | 1 |
| 4 | EVB-0139 | Q-027 | low | collect_targeted_evidence | 0 |
| 5 | EVB-0140 | Q-028 | low | collect_targeted_evidence | 0 |

12 backlog items currently flag `evidence_needed: literature`; only 5 above are highest-priority. Q-027 / Q-028 also need a paired experimental cycle per `next_action`.

---

## Serve.py Status
- **RUNNING** on port 8000 (PID 48594).

---

## Blocked Items

None. No TASK_CLAIMS collisions; governance.sh ran cleanly. Indexer surfaced 14 informational WARNINGs about manifests missing `evidence_direction_per_claim` (blanket directions applied) -- all are pre-existing manifests, not new ones.
