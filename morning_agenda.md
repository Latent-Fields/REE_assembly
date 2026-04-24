# Morning Agenda -- 2026-04-24

Generated: 2026-04-24T04:21:58Z

---

## Queue Status

- **Total pending: 0** -- **ALERT: Queue is EMPTY**
- Mac (DLAPTOP-4.local): 0 | PC (Daniel-PC): 0 | EWINPC: 0 | any: 0
- **ALERT: Queue empty -- no experiments will run until new ones are queued.**
  - 4 stub scripts (V3-EXQ-445d, V3-EXQ-455a, V3-EXQ-449c, V3-EXQ-476) errored because
    they raise NotImplementedError -- all gated on MECH-284 Phase 3 implementation.
  - Next natural work: implement MECH-284 Phase 3 (per-region staleness accumulator),
    then queue the V_s cascade stubs; or diagnose FAILs below and queue fix iterations.

---

## Experiments Awaiting Review (27 PASS / 6 FAIL indexed | 11 runner-only)

### FAIL Experiments

---

#### [EXQ-397d] -- v3_exq_397d_arc007_matched_endpoint -- FAIL
- **Claims tested:** ARC-007 (status: active, conf: 0.779, prior: 25 supporting / 10 opposing);
  SD-004 (status: implemented, conf: 0.785, prior: 12 supporting / 6 opposing)
- **Evidence direction:** weakens (blanket -- missing evidence_direction_per_claim; governance WARNING issued)
- **Classification:** evidence -- matched-endpoint metric test for hippocampal path planning
- **Governance impact if confirmed:** ARC-007 opposing count increases (currently hold_candidate_resolve_conflict, not pending_user). NOTE: blanket weakens may need per-claim correction if criteria split between ARC-007 and SD-004.
- **Supersedes:** v3_exq_397c_arc007_harder_env -- matched-endpoint metric redesign (residue RBF colocalization confound)
- **Note:** This was the corrected metric for ARC-007. A FAIL here is scientifically significant -- requires /diagnose-errors to determine genuine refutation vs residual metric issue.

---

#### [EXQ-451] -- v3_exq_451_q034_hazard_resource_threshold_retest -- FAIL
- **Claims tested:** Q-034 (status: open, conf: 0.752, prior: 8 supporting / 3 opposing)
- **Evidence direction:** weakens
- **Classification:** evidence -- retest of hazard/resource threshold question
- **Governance impact if confirmed:** Q-034 opposing count rises to 4+; may shift recommendation toward narrow_open_question or conflict resolution.
- **Supersedes:** V3-EXQ-288

---

#### [EXQ-445a] -- v3_exq_445a_sd032b_dacc_full_pipeline -- FAIL
- **Claims tested:** SD-032b (status: candidate, conf: 0.784, prior: 12 supporting / 8 opposing);
  MECH-258 (status: candidate, conf: 0.920, prior: 14 supporting / 1 opposing);
  MECH-260 (status: candidate, conf: 0.895, prior: 7 supporting / 0 opposing)
- **Evidence direction:** weakens (blanket -- missing per-claim direction; governance WARNING issued)
- **Classification:** evidence -- dACC full pipeline test
- **Governance impact if confirmed:** MECH-258/260 have very high lit_conf (0.92/0.895). Blanket weakens on these high-confidence claims is suspicious -- likely a substrate gap (SD-032b), not a MECH-258 refutation. Per-claim direction recommended before accepting.
- **Supersedes:** v3_exq_445_sd032b_dacc_analog

---

#### [EXQ-433c] -- v3_exq_433c_sd029_eventcond_comparator -- FAIL
- **Claims tested:** SD-029 (status: candidate, conf: 0.668, prior: 5 supporting / 5 opposing);
  MECH-256 (status: candidate, conf: 0.834, prior: 7 supporting / 2 opposing)
- **Evidence direction:** inconclusive_insufficient_events
- **Classification:** diagnostic -- event-conditioned comparator with curriculum
- **Governance impact if confirmed:** Inconclusive, not a refutation. SD-029 stays at 5:5 parity. MECH-256 hold_pending_v3_substrate. Needs redesign to guarantee event elicitation.
- **Supersedes:** v3_exq_433b_sd029_extended_interventional

---

#### [EXQ-418a] -- v3_exq_418a_sd016_sd017_context_conditioned_action -- FAIL
- **Claims tested:** SD-017 (status: provisional, conf: 0.689, prior: 5 supporting / 5 opposing)
- **Evidence direction:** does_not_support
- **Classification:** evidence -- context-conditioned action integration test
- **Governance impact if confirmed:** SD-017 is provisional at 5:5 parity. A "does_not_support" FAIL pushes to 5:6 opposing; may trigger provisional -> candidate demotion. URGENT: verify whether EXQ-418a ran with the SD-016 cue_action_proj fix active (EXQ-449b PASS at 02:17Z, EXQ-418a at 02:19Z -- very tight).
- **Supersedes:** V3-EXQ-418

---

#### [EXQ-137] -- v3_exq_137_mech097_pps_commit_locus_pair -- FAIL
- **Claims tested:** MECH-097 (status: candidate, conf: 0.590, prior: 1 supporting / 1 opposing)
- **Evidence direction:** mixed
- **Classification:** evidence -- peripersonal space commit locus pairing (re-instrumented)
- **Governance impact if confirmed:** MECH-097 conf stays low (~0.59, 1:1 -> mixed). No immediate governance action needed.

---

### PASS Experiments (27 runs, 9 distinct types)

#### [EXQ-456/460/462/463/464/465/466/467/468] -- OCD battery (SD-033a / SD-034 cluster) -- PASS (multiple seeds)

| Experiment | Claims | Seeds |
|-----------|--------|-------|
| EXQ-456 (sd033a_lateral_pfc) | MECH-261, MECH-262, SD-033a | 3 |
| EXQ-460 (sd034_verified_not_released) | MECH-260, MECH-261, SD-034 | 2 |
| EXQ-462 (mech267_rule_binding) | MECH-262, MECH-267, SD-033a | 4 |
| EXQ-463 (mech268_dacc_conflict) | MECH-258, MECH-268, SD-032b, SD-034 | 2 |
| EXQ-464 (mech266_competing_goals) | MECH-259, MECH-266, SD-032a | 2 |
| EXQ-465 (mech267_intrusive_filtering) | MECH-094, MECH-261, MECH-267 | 4 |
| EXQ-466 (sd034_satisficing) | MECH-094, SD-034 | 2 |
| EXQ-467 (mech266_mode_stickiness) | MECH-266, SD-032a | 2 |
| EXQ-468 (sd034_mech268_commitment) | MECH-090, MECH-268, SD-034 | 2 |

- **Classification:** evidence (SD-032a, SD-033a, SD-034) / diagnostic (MECH cluster)
- **Governance impact if confirmed:** SD-032a multi-seed PASS across EXQ-464/467 supports promote_to_provisional recommendation (current conf 0.861, 21:0). MECH-261 similarly strong (21:0, conf 0.863). Most MECH claims remain hold_pending_v3_substrate -- PASS evidence accumulates but governance hold stands.

---

#### [EXQ-470a] -- v3_exq_470a_sd029_balanced_curriculum -- PASS
- **Claims tested:** SD-029 (status: candidate, conf: 0.668, prior: 5 supporting / 5 opposing)
- **Classification:** evidence -- SD-029 balanced curriculum with lowered hazard_harm
- **Governance impact if confirmed:** SD-029 shifts to 6:5 supporting. hold_pending_v3_substrate remains.

---

#### [EXQ-447] -- v3_exq_447_sd032d_pcc_stability -- PASS
- **Claims tested:** MECH-259 (status: candidate, conf: 0.754, prior: 3 supporting / 0 opposing);
  SD-032d (status: candidate, hold_pending_v3_substrate)
- **Classification:** evidence -- PCC stability test
- **Governance impact if confirmed:** MECH-259 rises to 4:0 (conf ~0.78+); supports promote_to_provisional recommendation.

---

#### [EXQ-449b] -- v3_exq_449b_sd016_cue_action_proj_consumer_fix -- PASS
- **Claims tested:** SD-016 (status: provisional)
- **Classification:** evidence -- SD-016 cue_action_proj consumer fix validation
- **Governance impact if confirmed:** SD-016 provisional gets additional support. action_bias_std 2.7e-8 -> 2.957e-3 confirms fix works.

---

## Errors to Diagnose (4 stub-script ERRORs | 7 UNKNOWN state mismatches)

### Stub ERRORs (all gated on MECH-284 Phase 3)

| Queue ID | Notes |
|----------|-------|
| **V3-EXQ-445d** | v3_exq_445d_sd032b_dacc_with_vs -- NotImplementedError stub |
| **V3-EXQ-455a** | v3_exq_455a_sd032a_salience_with_vs -- NotImplementedError stub |
| **V3-EXQ-449c** | v3_exq_449c_mech074b_bla_retrieval_bias -- NotImplementedError stub |
| **V3-EXQ-476** | v3_exq_476_mech269_vs_validation_probe -- NotImplementedError stub |

These need MECH-284 Phase 3 (per-region staleness accumulator) before they can run. Do not re-queue until that substrate is implemented.

### UNKNOWN state mismatches (7)

V3-EXQ-471, V3-EXQ-470a, V3-EXQ-447a, V3-EXQ-445e, V3-EXQ-433c, V3-EXQ-449b, V3-EXQ-418c appear as UNKNOWN in runner_status.json. Indexed results exist in evidence/ for EXQ-470a, EXQ-433c, EXQ-449b, EXQ-418a -- these are state mismatches rather than missing results. Safe to mark discussed after reviewing indexed manifests above.

---

## Governance Agenda (36 pending_user recommendations)

### Promotions ready for decision (6)

| Claim | Current status | Recommendation | Supporting / Opposing | Conf |
|-------|---------------|---------------|----------------------|------|
| **MECH-094** | provisional | promote_to_stable | 13 / 0 | 0.868 |
| **SD-035** | provisional | promote_to_stable | 3 / 0 | 0.828 |
| **MECH-261** | candidate | promote_to_provisional | 21 / 0 | 0.863 |
| **SD-032a** | candidate | promote_to_provisional | 21 / 0 | 0.861 |
| **SD-032e** | candidate | promote_to_provisional | 3 / 1 | 0.830 |
| **MECH-259** | candidate | promote_to_provisional | 3 / 0 | 0.754 |

### Conflict holds (3 pending_user)

| Claim | Recommendation |
|-------|---------------|
| **ARC-045** | hold_candidate_resolve_conflict |
| **MECH-166** | hold_candidate_resolve_conflict |
| **MECH-220** | hold_candidate_resolve_conflict |

### V3 substrate holds (27 pending_user)

Bulk cluster -- all hold_pending_v3_substrate. Includes V_s invalidation stack
(MECH-269/284/285/287/288), OCD battery claims (MECH-256/258/260/262/264/265/266/267/268),
SD-029/032b/032c/032d/033a/034/036, ARC-058, MECH-072/074. Standard acknowledgment -- no action
until V3 substrate evidence arrives.

---

## Literature Pull Candidates (Top 5 -- all medium priority)

| # | Backlog ID | Claim | Priority | Existing entries |
|---|-----------|-------|----------|-----------------|
| 1 | EVB-0120 | MECH-262 | medium | 0 |
| 2 | EVB-0121 | onboarding | medium | 0 |
| 3 | EVB-0122 | MECH-257 | medium | 0 |
| 4 | EVB-0123 | MECH-057 | medium | 8 (existing) |
| 5 | EVB-0124 | SD-003-prereq | medium | 7 (existing) |

No high-priority literature gaps in the active backlog. MECH-262 and MECH-257 are the cleanest targets (no existing entries).

---

## Serve.py Status

- **RUNNING on port 8000** (PID 11285)

---

## Blocked Items

None. Governance.sh ran cleanly (9 new run-packs converted, 877 total runs indexed).

### Key Flags

- **SD-017 demotion risk:** EXQ-418a FAIL (does_not_support) shifts SD-017 from 5:5 to 5:6. SD-017 is currently provisional. Verify the SD-016 substrate fix (EXQ-449b, 02:17Z) was active when EXQ-418a ran (02:19Z) -- if not, EXQ-418a should be superseded rather than accepted as evidence.

- **Multi-claim blanket weakens:** EXQ-397d and EXQ-445a lack evidence_direction_per_claim. Governance applied blanket weakens to high-confidence claims (MECH-258 conf=0.920, MECH-260 conf=0.895). Before next governance cycle, add per-claim direction fields to these manifests.

- **MECH-284 Phase 3 is the current implementation blocker:** All 4 queued V_s cascade experiments are stubs until it lands. Queue will remain at 0 until either (a) Phase 3 is implemented, or (b) new unrelated experiments are queued.
