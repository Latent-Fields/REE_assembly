# Queue Check -- 2026-04-29 (afternoon scheduled)

**Session:** ree-diagnose-queue (afternoon scheduled, automated mode)
**Generated UTC:** 2026-04-29T14:20:00Z
**Result:** **NOTHING QUEUED** -- no substrate-ready proposed candidate without redundant or design-blocked friction.

---

## Summary

| Metric | Value |
|--------|-------|
| Pending queue depth | 0 items |
| `status: "proposed"` experimental items in index | 65 |
| High-priority "proposed" items | 3 |
| High-priority items substrate-ready AND not already covered by recent PASS | 0 |
| Medium-priority items substrate-ready AND with no script | many (need triage) |

The proposals index is not advancing because the auto-pipeline keeps regenerating "proposed" rows for claims that have already produced PASS evidence. The right next step is a governance housekeeping pass to mark executed proposals, not an automated re-queue.

---

## High-priority proposals -- per-item status

### EVB-0061 (claim SD-011, suggested `v3_exq_106_harm_obs_a_temporal_persistence`)

- **Status:** still `proposed` in `experiment_proposals.v1.json` (no `executed_by` field).
- **Reality:** **V3-EXQ-106a PASS** on 2026-04-28T17:14:10Z (queued by yesterday's ree-diagnose-queue afternoon run; smoke had been 4/4 PASS).
- **Substrate:** SD-011 promoted candidate -> provisional 2026-04-18; conf 0.874 + lit 0.844.
- **Recommended action:** governance housekeeping -- mark EVB-0061 `status: "executed"`, `executed_by: "V3-EXQ-106a"`, `executed_queue_id: "V3-EXQ-106a"`, then re-run `build_experiment_indexes.py` so the proposal stops re-surfacing. **Not a queue-experiment task.**

### EVB-0062 (claim MECH-104, suggested `v3_exq_126_mech104_surprise_gate_pair`)

- **Status:** still `proposed`.
- **Reality:** V3-EXQ-126 PASS on 2026-04-21T20:23Z (`v3_exq_126_mech104_surprise_gate_pair/`, claim_ids=`["MECH-104"]`). MECH-104 status=`active`, conf 0.88.
- **Substrate:** MECH-104 already active and validated; multiple supporting runs (V3-EXQ-062 / 062a / 062b / 204 / 365) on file.
- **Recommended action:** same as EVB-0061 -- mark executed via governance housekeeping. Re-running an identical script would add a redundant evidence point without scientific gain.

### EVB-0065 (claim ARC-018, suggested `claim_probe_arc_018`)

- **Status:** still `proposed`. **No script exists** matching the suggested name.
- **Substrate:** ARC-018 `status: active`, `v3_pending: false`, `adjudication_decision_status: applied`. Substrate appears ready, contradicting the older MEMORY note that listed ARC-018 as v3_pending. (The `claims.yaml` value is authoritative; the memory line is stale.)
- **Why not auto-queueable:** the proposal is a claim-probe boilerplate -- "Run a discriminative support-vs-ablation pair for ARC-018" -- with generic acceptance criteria. There is no concrete experimental design, no script template, no clear primary-vs-ablation conditions specified. **This is a design task, not an instrumentation task.** It would need: a 4-arm ablation around HippocampalModule trajectory proposals, phased training protocol, pre-registered thresholds for `trajectory_residue_alignment` (or whatever the operational metric is), and an explicit ARC-018 mechanism-under-test statement. Outside automated-mode scope.

---

## Medium-priority proposals -- substrate-readiness sweep

Only the items where claim status was checked are listed. `v3_pending: true` rules out auto-queueing in V3.

| EVB | Claim | claims.yaml status | Substrate? | Action |
|-----|-------|--------------------|------------|--------|
| EVB-0072 | ARC-035 | candidate | likely ready | needs design |
| EVB-0073 | SD-033e | candidate, `implementation_phase: v4`, `v3_pending: false` | **V4-deferred** | block |
| EVB-0074 | MECH-074 | candidate, `v3_pending: true` | **blocked** | block |
| EVB-0075 | MECH-294 | candidate, `v3_pending: true` | **blocked** | block |
| EVB-0076 | ARC-060 | candidate, `v3_pending: true` | **blocked** | block |
| EVB-0077 | MECH-172 | candidate | likely ready (lit_conf 0.894) | needs design |
| EVB-0078 | MECH-265 | candidate, `implementation_phase: v4`, `v3_pending: true` | **V4-deferred** | block |
| EVB-0079 | MECH-275 | candidate, `v3_pending: true` | **blocked** | block |
| EVB-0080 | INV-057 | candidate (lit_conf 0.897) | likely ready | needs design |
| EVB-0081 | MECH-183 | candidate (lit_conf 0.831) | likely ready | needs design |

5 of 10 medium-priority items checked are explicitly substrate-blocked (V3-pending or V4-deferred). The remaining 5 are "candidate" claims with no specific experimental script -- each requires a discriminative-pair design before queueing. None are minor-instrumentation tasks.

---

## What IS the operational next-up (not from the proposals index)

Per `WORKSPACE_STATE.md` and the 2026-04-29T11:40Z update-docs-pm entry, the actual next experiment is:

**V3-EXQ-490d (planned)** -- Q-040b strong-reading falsifiable test using the **MECH-284 staleness-into-V_s-gate wiring** that landed 2026-04-29T06:03Z. Drops the smoke-threshold override (0.85/0.85/0.95) and tests `use_vs_gate_staleness_lookup` ON vs OFF at matched 0.4 thresholds. PASS supports the strong reading of MECH-269b stale-stream-discrimination via V_s gating; FAIL routes evidence further upstream.

This is human-curated work that does not surface in `experiment_proposals.v1.json`. It needs:
- A new script `experiments/v3_exq_490d_mech269b_staleness_into_gate.py` (likely modelled on 490c with the override flag flipped).
- Acceptance criteria (C1-C4) defined in the script header.
- ~60-90 min queue estimate based on 490c.
- claim_ids=`["MECH-269b", "MECH-284", "Q-040"]` (re-evaluate per claim_ids accuracy rule -- the experiment specifically tests staleness gating, so MECH-284 is the dominant test).

Recommended for an interactive session, not an automated /queue-experiment run.

---

## Summary of automated-mode actions

| Action | Status |
|--------|--------|
| Find substrate-ready proposed candidate | NONE -- 3/3 high-priority items either redundant (PASS evidence exists, just not propagated to index) or design-blocked. |
| Queue 1 candidate | **NOT DONE** (no appropriate target) |
| Smoke test | n/a |
| Write queue_check note | DONE -- this file |
| Push commits | pending (REE_assembly only -- queue_check note + earlier diagnose_staging files) |

## Recommended human follow-up (priority order)

1. **Governance housekeeping pass** -- mark EVB-0061 and EVB-0062 as `executed` in `experiment_proposals.v1.json` so the auto-pipeline stops resurfacing claims that already PASS. Then re-run `build_experiment_indexes.py`.
2. **Queue V3-EXQ-490d manually** -- the 06:03Z MECH-284 substrate landing makes the Q-040b strong reading testable for the first time without smoke threshold overrides. Highest scientific value next-up.
3. **EVB-0065 (ARC-018) design** -- if priority warrants, schedule a design session for `claim_probe_arc_018`.
4. **Proposals indexer triage** -- 65 still-proposed items is too noisy. Worth a focused governance walk to either mark executed or redirect to specific substrate-aware probes.
