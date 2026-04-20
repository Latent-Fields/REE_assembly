# Morning Agenda -- 2026-04-20

Generated: `2026-04-20T04:25:23Z`

---

## Queue Status

- **Total pending: 0** | Claimed: 1 (V3-EXQ-447 by ree-cloud-2, SD-032d PCC stability)
- **ALERT: Queue empty -- no pending experiments. Queue experiments before starting the runner.**
- V3-EXQ-447 claimed by ree-cloud-2: deterministic 2-min PCC stability validation, expect PASS soon.
- V3-EXQ-325b FAIL is in runner_status but has no indexed evidence file (flat JSON not written to REE_assembly). Likely a runner output-path issue. Note for next session.

---

## Experiments Awaiting Review (4 indexed / 2 runner-only)

### [V3-EXQ-446] -- v3_exq_446_sd032a_salience_coordinator -- PASS
- **Claims tested:** SD-032a (candidate, V3-pending), MECH-259 (candidate, V3-pending), MECH-261 (candidate, V3-pending)
- **Key metrics:** operating_mode entropy=1.268 nats (COORD_ON vs 0 COORD_OFF); synthetic pe=10 triggers mode_switch (effective_threshold=1.0); 8/8 write-gate values in [0,1]; V4 register_target() works (SD-033e gate=0.499); backward compat max_entropy_delta=0.0
- **Classification:** diagnostic (wiring/integration validation)
- **Governance impact if confirmed:** First V3 experimental support for SD-032a, MECH-259, MECH-261. Salience coordinator substrate is functional. Lifts them toward provisional if reviewed positively -- but the PASS criteria were primarily structural/wiring, not behavioural. Need a follow-on experiment that tests mode-switching under realistic training conditions.

---

### [V3-EXQ-433a] -- v3_exq_433a_sd029_eventcond_comparator_scripted -- FAIL (10/13 criteria)
- **Claims tested:** SD-029 (candidate, conf=0.324, 0 pass/1 fail exp runs), MECH-256 (candidate, conf=0.804, lit-only)
- **Supersedes:** EXQ-433 (event-distribution collapse issue fixed by scripted-eval protocol)
- **Key metrics:** C1 PASS: forward_r2 = 0.984--0.9998 across 4 seeds; C2 FAIL: attenuation_ratio = 0.95--1.14 (expected 0.3--0.7 partial attenuation); C3 PASS: approach_snr = 76--962 across seeds
- **evidence_direction_per_claim:** SD-029: does_not_support | MECH-256: supports
- **Classification:** evidence (directly tests SD-029 single-pass comparator hypothesis)
- **Governance impact if confirmed:** MECH-256 forward model well-evidenced. SD-029 C2 failure means the trained model shows NO differential attenuation of self vs externally-caused harm residuals. Residual means for env_caused (~0.17--0.33) and agent_caused (~0.19--0.31) are nearly identical across all 4 seeds. The Shergill 2003 partial-attenuation pattern (expected ratio 0.3--0.7) is not present. Interpretations: (a) SD-029 wrong -- comparator does not attenuate; (b) 80-episode training insufficient; (c) substrate treats hazard events symmetrically regardless of causal origin. Recommend /diagnose-errors before queuing SD-029b.

---

### [V3-EXQ-445] -- v3_exq_445_sd032b_dacc_analog -- FAIL
- **Claims tested:** SD-032b (candidate, V3-pending, conf=0.89 lit-only), MECH-258 (candidate, conf=0.886 lit-only), MECH-260 (candidate, conf=0.72 lit-only), ARC-033 (provisional, conf=0.832, 6 pass/8 fail), ARC-058 (candidate, no exp entries)
- **Key metrics:** C1 PASS: harm_a forward_r2=0.840--0.937 in 3/3 seeds; C2 FAIL: entropy_ON == entropy_OFF == 0.0 (monostrategy -- single action chosen 3487/3487 times regardless of dACC on/off); C3 PASS: MECH-260 no collapse (ON >= OFF); C4 diagnostic: ARC-058 vs ARC-033 indistinguishable at mean_r2=0.899 both arms
- **evidence_direction_per_claim:** SD-032b: mixed | MECH-258/260/ARC-033/ARC-058: supports
- **Classification:** diagnostic (tests dACC behavioral effect; discriminates ARC-033 vs ARC-058)
- **Governance impact if confirmed:** C2 FAIL is a monostrategy collapse. The dACC score_bias fires (mean_score_bias_abs=86k--3.4M) but does not shift action selection because the policy is degenerate (zero entropy). The E2_harm_a substrate trains well; the behavioral gate is the problem. This is likely a bias scale issue (score_bias hugely dominates Q-values but the monostrategy is impenetrable). Recommend: /diagnose-errors then V3-EXQ-445a with clipped/attenuated dACC bias_scale before concluding SD-032b fails.

---

### [V3-EXQ-397] -- v3_exq_397_arc007_path_memory_ablation -- FAIL (3rd attempt: EXQ-397b)
- **Claims tested:** ARC-007 (active, conf=0.78, 4 pass/6 fail out of 35 runs), SD-004 (implemented, conf=0.785)
- **Key metrics:** hippo_quality_gap_intact=-1.640 (expected > 0; intact is WORSE than ablated); ablation_degradation=-1.640; world_forward_r2=0.9658; terrain_loss 0.291->0.000 (residue correctly zeroed)
- **Classification:** evidence (tests ARC-007 path memory necessity via hippocampal ablation)
- **Governance impact if confirmed:** Third 397-series variant with paradoxical negative quality gap (intact worse than ablated). Terrain_loss collapses to 0 (ablation works mechanically) but navigation quality improves on ablation. ARC-007 is still well-supported by EXQ-114 (PASS, 99.2% harm reduction MAP_NAV vs MAP_ABLATED). The 397 series may be testing a different pathway. The hippo_quality_gap metric is a candidate for inversion/calibration error. Needs /diagnose-errors: metric definition, whether intact training is stable, and whether the ablation condition is actually running correctly.

---

## Errors to Diagnose (1)

- **V3-EXQ-325c**: SD-032c AIC-analog operating-mode descending modulation -- ERROR -- needs /diagnose-errors
  - V3-EXQ-325b (predecessor) is also FAIL in runner_status but has no indexed evidence file. Both runs lack evidence files in REE_assembly. Likely a runner output-path issue introduced when SD-032c was implemented. Check the experiment script output path and runner working directory.

---

## Governance Agenda (15 pending_user items)

### Action item (1):

- **SD-020** (provisional) -- Recommendation: **promote_to_stable**
  - Evidence: 7 supporting, 0 weakens, 2 mixed | conf=0.912 | 6 exp + 5 lit entries | conflict_ratio=0
  - Clean promotion. No conflict, strong support across experimental and literature evidence.

### V3-substrate holds (13 newly registered -- expected, no urgent action):

All registered 2026-04-19 as part of SD-032 + SD-033 cluster. No user action needed unless scientific concern.

| Claim | Rec |
|-------|-----|
| ARC-058, MECH-256, MECH-258, MECH-259, MECH-260, MECH-261, MECH-264, MECH-265 | hold_pending_v3_substrate |
| SD-029, SD-032a, SD-032b, SD-032d, SD-032e | hold_pending_v3_substrate |

### Conflict resolution (1):

- **MECH-220** (candidate) -- Recommendation: **hold_candidate_resolve_conflict**
  - Evidence: 4 supporting, 1 weakens | conf=0.737
  - EXQ-395 reclassified non_contributory (substrate gap) in yesterday's governance. The 1 weakening run may remain pending_retest_after_substrate until SD-032 experiments retest.

---

## Literature Pull Candidates (Top 5)

All medium priority; all newly registered claims with no existing targeted reviews.

| # | Backlog ID | Claim | Subject |
|---|-----------|-------|---------|
| 1 | EVB-0107 | MECH-259 | Salience-network switch threshold |
| 2 | EVB-0109 | MECH-256 | Forward-model comparator for self-attribution |
| 3 | EVB-0110 | Q-036 | Variables beyond temporal integration for affective state |
| 4 | EVB-0111 | SD-029 | Single-pass agency attribution via z_harm_s comparator |
| 5 | EVB-0112 | SD-032a | Salience-network coordinator |

Note: MECH-256 and SD-029 are directly implicated in EXQ-433a FAIL. A lit-pull for MECH-256 (biological grounding of partial attenuation, Shergill 2003 force threshold) is timely given the C2 failure.

---

## Serve.py Status

- **RUNNING on port 8000** (Python process 82280)

---

## Blocked Items

None. No TASK_CLAIMS collisions. governance.sh ran cleanly (2 new run-packs converted: V3-EXQ-445, V3-EXQ-446).

---

## Suggested Session Priorities

1. **Queue experiments** (critical -- queue empty). Candidates: V3-EXQ-445a (dACC bias scale fix), V3-EXQ-325d (SD-032c fix), V3-EXQ-448 (SD-032e pACC -- already scripted), V3-EXQ-397c (ARC-007 metric fix).
2. **Review EXQ-433a** -- SD-029 does_not_support. Decide whether falsification or maturity issue before queuing follow-on.
3. **Governance** -- SD-020 promote_to_stable (clean, no prerequisites).
4. **/diagnose-errors** -- V3-EXQ-325c (output path) + V3-EXQ-445 (dACC bias scale).
