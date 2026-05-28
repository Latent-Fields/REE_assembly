---
closure_plan:
  id: behavioral_diversity_isolation
  title: "Behavioural Diversity Isolation"
  registered: 2026-05-25
  scope_claims: [ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a, MECH-314b, MECH-314c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076]
  sibling_plans: [arc_062_rule_apprehension, commitment_closure, sleep_substrate, sd033_governance, goal_pipeline, self_attribution]
  nodes:
    - id: "behavioral_diversity_isolation:GAP-A"
      title: "Theory 1 / Layer A: CEM elite-pool collapse to one action class (ARC-065 SP-CEM child)"
      phase: "P1 falsifier blocked -> upstream substrate work"
      status: blocked_pending_substrate
      severity: medium
      owner_exq: "V3-EXQ-567 (PASS); V3-EXQ-569 + V3-EXQ-573 (non_contributory); V3-EXQ-570 + V3-EXQ-571 + V3-EXQ-609 diagnostics landed; FP-2 falsifier blocked on E2-world-forward per-candidate signal collapse"
      unblocks_claims: [ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H", "arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-28
      resume_condition: "V3-EXQ-567 PASS 2026-05-15 lifts selected_action_entropy 0.012->0.497 and candidate support 1.007->2.810 (ARC-065 SP-CEM child substrate validated main-path). V3-EXQ-569 matched-entropy sweep ran 2026-05-16 and was reclassified non_contributory at governance review: all 6 arms produced identical entropy (~0.496) because bias_fraction=0 for all diversity components -- the structured-vs-random comparison was never activated. V3-EXQ-571 PASS diagnostic confirmed F (forward model) dominates 88-89% of E3 score variance and ALL bias_fractions are machine-epsilon. V3-EXQ-573 10-arm bias-scale sweep (1x/5x/10x) reproduced the identical-arms collapse at 10x scale -> reclassified non_contributory; bias channel does not propagate at scale. V3-EXQ-609 per-candidate spread decomp (methodology fork from 571) surfaced curiosity emitting zero per-candidate vector. Root cause documented 2026-05-25 in evidence/planning/v3_exq_571_root_cause_2026-05-25.md: score_bias plumbing is correct, but the per-candidate signal is STRUCTURALLY ZERO -- all K candidates produce identical z_world after one E2 world-forward step (cand_world_pairwise_dist=0.0000) despite differing first actions. Same root cause as the 2026-05-17 ARC-062 GAP-B autopsy; that fix was scoped only to GatedPolicy. R1.a/R1.b cannot fire while the bias channel structurally carries no per-candidate variance. NEXT STEP is /implement-substrate on E2-world-forward per-candidate signal preservation (extends the 2026-05-17 GAP-B autopsy fix beyond GatedPolicy) -- NOT a /queue-experiment re-issue on the current substrate. After the substrate seam lands, queue V3-EXQ-569a as the matched-entropy FP-2 falsifier successor. IGW-20260528-008 (this node's owning IGW item) is stale and pending the substrate fix."
    - id: "behavioral_diversity_isolation:GAP-B"
      title: "Theory 2 / Layer B: E3 scoring collapses diverse candidates to one (MECH-341)"
      phase: "P3 retune landed -> validation in flight"
      status: in_progress
      severity: load-bearing
      owner_exq: "V3-EXQ-608 (P2 PASS); V3-EXQ-611 FAIL 2026-05-27T13:02Z (C1 substrate-readiness false: entropy_max_abs << gap range + stratified_fired=0 committed-only); V3-EXQ-611b retune validation queued 2026-05-28T17:25Z (claimed DLAPTOP-4.local @17:26:40Z, 6-arm factorial); B_only / ablate_B / ALL_ON behavioural falsifier TBD"
      unblocks_claims: [MECH-341, ARC-062, ARC-065]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-28
      resume_condition: "V3-EXQ-608 P2 diagnostic landed 2026-05-26T02:58Z PASS majority R2a_e3_collapse_confirmed_large_gap; substrate landed 2026-05-27 via /implement-substrate. V3-EXQ-611 substrate-readiness FAILed 2026-05-27T13:02Z on both validation channels: (a) ARM_1/3 entropy_bonus_max_abs 0.023-0.044 << observed mean_top2_class_gap 0.27-1.96 (substrate fires but cannot move selection ordering at scale=0.1 default); (b) ARM_2 n_stratified_fired=0 across all 3 seeds because the committed branch was never entered during measurement and the prior implementation gated stratified_select to the committed path only. Retune landed 2026-05-28 via /implement-substrate (session implement-substrate-mech-341-retune-20260528T165000Z): (a) MODULE CHANGE -- ree-v3/ree_core/predictors/e3_selector.py applies stratified_select on BOTH committed and uncommitted branches; bit-identical when score_diversity is None or sub-flag is False (stratified_select returns None; legacy argmin or multinomial path taken); MECH-094 preserved via existing simulation_mode kwarg; 506/506 contracts PASS post-edit. (b) PARAMETER SWEEP -- V3-EXQ-611b queued (6-arm factorial: 3 option groups OPT1_only/OPT2_only/BOTH x 2 entropy_bias_scale values 1.0/2.0). NO config defaults changed per implement-substrate skill rule; scales passed via per-arm cfg_overrides. Acceptance criteria: C1 stratified_fired > 0 across all OPT2/BOTH seeds (direct test of the call-site expansion); C2 entropy_bonus_max_abs >= 0.7 * scale on majority of seeds in entropy-ON arms; C3 selected_classes >= 2 with frac_pre_ge2 >= 0.5 on majority of seeds; R2.c readiness cleared by at least one arm. NEXT: (1) await V3-EXQ-611b manifest. (2) On PASS, queue B_only / ablate_B / ALL_ON behavioural falsifier on downstream env via /queue-experiment + apply R2.c rule (MECH-341 provisional promotion if B_only produces trajectory_class_count >= 2 with first_action_entropy > 0.3). (3) On FAIL with C1=false, route to /diagnose-errors on e3_selector.py wiring. (4) On FAIL with C1=true and C2/C3=false, route to algorithm-level Option-2 substrate revisit. Cross-link: same Layer-B substrate unblocks arc_062_rule_apprehension:GAP-B (V3-EXQ-543l successor cohort)."
    - id: "behavioral_diversity_isolation:GAP-C"
      title: "Theory 3 / Layer C: missing tonic noise floor (MECH-313 LC-NE analog)"
      phase: "P1"
      status: blocked_pending_substrate
      severity: medium
      owner_exq: "V3-EXQ-544/545 substrate PASS 5/5 (2026-05-10); V3-EXQ-603a/603b/603c all FAIL non_contributory (603c 2026-05-27T11:38Z, 8/12 cells aborted on P1 survival gate); cluster-absorbed into failure_autopsy_V3-EXQ-591_2026-05-27"
      unblocks_claims: [MECH-313, MECH-260, Q-045]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-H"]
      last_updated: 2026-05-28
      resume_condition: "Cluster-absorbed (591 autopsy section 6: fourth member of the substrate-uniform z_goal-zero family alongside 591 / 540 / 590a). Per gov-correction-20260527T175054Z the cluster routes epistemic_category=substrate_ceiling V3 (substrate-enrichment-within-V3), NOT substrate_conditional V4 as the initial 2026-05-27 governance stamp said. V3-EXQ-603c (P0+P1 phased training fix) FAILed non_contributory 2026-05-27T11:38Z: 8/12 cells aborted at the P1 survival gate (median ep length < 75 under target env), only 4 cells reached P2; ARM_2 / ARM_3 entropy lifted ~0.034 / 0.038 above ARM_0 / ARM_1 but FIFO temporal gate failed in all surviving cells; c1 / c2 / c3 all false. The 603-chain (a/b/c) is complete; no V3-EXQ-603d is owed under the current substrate. MECH-341 (e3_score_diversity, Layer-B sibling) landed 2026-05-27 but its substrate-readiness diagnostic V3-EXQ-611 also FAILed non_contributory 2026-05-27T13:02Z, ruling out the naive 'MECH-341 alone rescues GAP-C' hypothesis. Three substrate prerequisites (per 591 autopsy section 7) must clear before V3-EXQ-603d / 591b is queued: (1) MECH-307 default-value recalibration validated -- V3-EXQ-540e routing; (2) goal-pipeline training regime produces non-trivial z_goal in default config -- open; (3) InfantCurriculumScheduler Phase 0->1 exit signal tuned to achievable signal magnitudes -- recommended /implement-substrate target (lower H_pos fraction-of-max threshold from 0.70 toward ~0.20-0.30 OR replace with z_goal-norm / residue-coverage gate). Once (1)-(3) clear, queue V3-EXQ-603d via /queue-experiment with a partial 7-criterion gate revision (C3 trivially saturating, C5 / C6 / C7 sentinel-emitting). FP-2 matched-entropy gate against MATCHED_NOISE arm retained. R3.a / R3.b / R3.c are not applicable until a contributory PASS / FAIL is reached."
    - id: "behavioral_diversity_isolation:GAP-D"
      title: "Theory 4 / Layer D: V_s regional verisimilitude staleness (MECH-269 / MECH-269b)"
      phase: "P1"
      status: pending_governance_stamp
      severity: medium
      owner_exq: "V3-EXQ-550 FAIL/supports MECH-269 (2026-05-11T20:18Z); V3-EXQ-601 PASS/supports MECH-269b (2026-05-21T12:02Z); R4.b reading flagged 2026-05-28 pending governance stamp; Q-040b behavioural sufficiency still open"
      unblocks_claims: [MECH-269, MECH-269b, Q-040]
      depends_on: []
      cross_plan_link: ["arc_062_rule_apprehension:GAP-B"]
      last_updated: 2026-05-28
      resume_condition: "V3-EXQ-550 z_goal monostrategy falsifier landed 2026-05-11T20:18Z with outcome=FAIL but evidence_direction_per_claim={MECH-269: supports} (the wired-but-untrained goal pipeline did NOT break monostrategy at this probe depth, so the substrate-level reading of MECH-269 SURVIVES; the FAIL is about the diagnostic falsifier's PASS criterion not about MECH-269 weakening). V3-EXQ-601 MECH-269b-followup-A staleness-gate wiring PASS 2026-05-21T12:02Z further confirms the substrate path. Both run pairs are in review_tracker.reviewed_run_ids since their landing. R4.b decision-rule reading (V_s pathology confirmed; theory 4 promoted; MECH-269 follow-up substrate work prioritised) was applied to the status table 2026-05-28 by igw-011-gapd-doc-sync session; governance stamp pending at next /governance cycle. Remaining open item: Q-040b behavioural sufficiency (MECH-295 / StepHarness cohort) per substrate_queue -- currently owned by IGW-20260528-016 (goal_pipeline:GAP-4, V3-EXQ-490g Tier-1 retest cohort). Resume signal: when /governance cycle runs and stamps R4.b on V3-EXQ-550 (manifest + claim_evidence already carry supports-MECH-269), advance status from pending_governance_stamp to closed; if R4.a is preferred instead, the supports-MECH-269 per-claim direction in the manifest must be revised first."
    - id: "behavioral_diversity_isolation:GAP-E"
      title: "Theory 5 (deferred): proposal-distribution bias (re-enters candidate set on R_X.c)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-A", "behavioral_diversity_isolation:GAP-B", "behavioral_diversity_isolation:GAP-C", "behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Re-enters candidate set only if R_X.c fires -- i.e. the full 4-substrate stack (Layers A+B+C+D ON) still fails Rung 1 at ALL_ON. Until then, retained as secondary candidate but no falsifier is owed."
    - id: "behavioral_diversity_isolation:GAP-F"
      title: "Theory 6 (deferred): MECH-260 anti-recency contribution to behavioural diversity"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-260]
      depends_on: ["behavioral_diversity_isolation:GAP-C"]
      last_updated: 2026-05-25
      resume_condition: "Partially covered by Q-045 4-arm ablation (MECH-313 OFF / 313 only / 260 only / both ON) under GAP-C's V3-EXQ-603c retest. Promote to non-deferred only if the 4-arm result needs a dedicated MECH-260-vs-MECH-313 redundancy follow-up per R_X.b."
    - id: "behavioral_diversity_isolation:GAP-G"
      title: "Theory 7 (deferred): MECH-314 curiosity weight (Goldilocks calibration)"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-314, MECH-314a]
      depends_on: ["behavioral_diversity_isolation:GAP-B"]
      last_updated: 2026-05-25
      resume_condition: "V3-EXQ-590a annotated pending_retest_after_substrate (MECH-111 broadcast novelty was scalar EMA -> argmax-invariant null on selection). Re-queue as V3-EXQ-590b is gated on MECH-314a per-candidate RBF novelty implementation AND behavioural diversity landing (i.e. resolution of GAP-B). Until both gates clear, theory 7 stays deferred and its falsifier is not queued."
    - id: "behavioral_diversity_isolation:GAP-H"
      title: "Theory 8 (deferred): z_goal config-default confound"
      phase: "P4-extend"
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: []
      depends_on: ["behavioral_diversity_isolation:GAP-D"]
      last_updated: 2026-05-25
      resume_condition: "Confound check on V3-EXQ-550 (Theory 4). If GAP-D's R4-rule application surfaces an ARM_ON >> ARM_OFF asymmetry that maps to z_goal config-default rather than V_s substrate pathology (R4.a), this node becomes the dedicated re-run with z_goal matched across arms. Until GAP-D's R4 disposition lands in governance, theory 8 stays deferred."
---

# Behavioural Diversity Isolation Plan (REE-v3)

**Created:** 2026-05-25T11:46:33Z
**Author session:** diversity-isolation-plan-20260525T114633Z
**Status:** draft (plan-of-record)
**Sibling to:** [`behavioral_diversity_acceptance_criteria.md`](behavioral_diversity_acceptance_criteria.md)
**Related claims:** ARC-065, ARC-062, ARC-064, MECH-260, MECH-269, MECH-269b, MECH-313, MECH-314, MECH-314a/b/c, MECH-320, MECH-341, SD-003, SD-017, SD-029, SD-054, Q-043, Q-044, Q-045, Q-054, Q-055, INV-074, INV-076

---

## Purpose

The acceptance-criteria doc (sibling) defines **what counts as success** for behavioural
diversity in REE-v3. This document defines **how we isolate which of the candidate failure
mechanisms is load-bearing** when diversity fails. The two are complementary:

| Doc | Question answered |
|-----|-------------------|
| `behavioral_diversity_acceptance_criteria.md` | When can we say diversity is real and useful? |
| `behavioral_diversity_isolation_plan.md` (this) | When diversity is absent, which substrate layer is responsible? |

The isolation plan is needed because **diversity failure is multi-causal**: ARC-065 already
commits the architecture to a distributed pathway (LC-NE tonic + frontopolar curiosity +
striatal novelty + hippocampal trajectory sampling), and multiple layers can independently
suppress the observed action-class entropy. Without an isolation matrix, a Rung-1 FAIL is
under-determined: we don't know which substrate to fix next.

---

## Layer model: where diversity can collapse

Diversity must survive all four layers between candidate generation and observable action.
Failure at any one layer reproduces the monostrategy phenotype downstream.

```
                  ARC-065 distributed diversity-generation pathway
                                    |
                                    v
   [ Layer A: PROPOSAL ]  hippocampal trajectory sampling, CEM candidate pool
                                    |
                                    v
   [ Layer B: SCORING ]    E3 score aggregation across trajectory classes
                                    |
                                    v
   [ Layer C: ACTION-SELECT ]  softmax / argmax over E3-ranked candidates
                                    |
                                    v
   [ Layer D: REPRESENTATION ] V_s anchor sets / regional verisimilitude
                                    | (feeds back into Layer A on next tick)
                                    v
                              observable action stream
```

**Layer D feedback note.** Layer D is not strictly downstream of A-C in a single tick --
state representation in tick t+1 depends on what was committed in tick t. Stale V_s
representations therefore amplify monostrategy across episodes even when Layers A-C are
behaving correctly within any one tick. This is why MECH-269 reads as "monostrategy"
upstream of the action-selection stack despite acting on representations.

---

## The 4 theories (top of the candidate field)

Drawn from the 8-mechanism survey 2026-05-25 (see prior conversation / governance log).
Theories 5-8 (proposal-distribution bias, MECH-260 anti-recency, curiosity weight, z_goal
config-default confound) are retained as secondary candidates but not the focus of this
plan.

| # | Theory | Layer | Primary claim | Falsifier EXQ | Status |
|---|--------|-------|---------------|---------------|--------|
| 1 | CEM elite-pool collapse to one action class | A | ARC-065 (SP-CEM child) | V3-EXQ-567 / V3-EXQ-569 | landed 2026-05-17 (main-path); matched-entropy control pending |
| 2 | **E3 scoring collapses diverse candidates to one** | **B** | **MECH-341 (new)** | **TBD (this plan, design below)** | **unclaimed gap until 2026-05-25** |
| 3 | Missing tonic noise floor (LC-NE analog) | C | MECH-313 | V3-EXQ-543b ARM_MECH313_only | substrate landed, matched-entropy gate pending |
| 4 | V_s regional verisimilitude staleness | D | MECH-269 / 269b | V3-EXQ-550 (live falsifier) | falsifier in flight |

**Headline gap.** Theory #2 (E3 scoring) is the highest residual leverage because the other
three either have landed substrate (#1, #3) or have an active falsifier (#4). MECH-341
registered in this pass closes the claim-side of the gap; the experiment design (Section 5)
closes the test-side.

---

## Isolation matrix

Each row is an experiment arm; each column is a substrate ON/OFF. A run produces the row
of outcomes; comparison across rows pins the contribution of each substrate. The matrix is
designed so that *any single substrate ablation against the all-ON baseline gives a
single-substrate contribution estimate*; the all-OFF arm is the Rung-0 substrate-naive
baseline that anchors ARC-065's architectural commitment.

| Arm | SP-CEM (A) | E3 score-diversity (B) | Noise floor MECH-313 (C) | V_s active MECH-269 (D) | Use |
|-----|:----------:|:---------------------:|:------------------------:|:----------------------:|-----|
| BASE_OFF | off | off | off | off | Rung 0 baseline / ARC-065 architectural-necessity check |
| ALL_ON | **on** | **on** | **on** | **on** | Rung 1 target (matched-entropy controlled) |
| A_only | on | off | off | off | Theory 1 contribution (SP-CEM proposal lift in isolation) |
| B_only | off | **on** | off | off | Theory 2 contribution (E3 scoring lift in isolation) |
| C_only | off | off | **on** | off | Theory 3 contribution (noise floor in isolation) |
| D_only | off | off | off | **on** | Theory 4 contribution (V_s in isolation) |
| ablate_A | off | on | on | on | Marginal cost of removing SP-CEM |
| ablate_B | on | off | on | on | Marginal cost of removing E3 diversity preservation |
| ablate_C | on | on | off | on | Marginal cost of removing noise floor |
| ablate_D | on | on | on | off | Marginal cost of removing V_s |
| MATCHED_NOISE | off | off | T=2.5 uniform | off | FP-2 control: structured-vs-noise comparison for acceptance doc Rung 1 |

**Pragmatic note.** The full 11-arm matrix is not required in a single run. Sequencing
(Section 6) reduces this to a phased programme of 3-arm and 4-arm experiments that each
answer one question.

**Layer-B substrate gap.** "E3 score-diversity ON" requires MECH-341 substrate to exist;
until it lands, B columns are vacuously OFF and theories 1/3/4 are the only testable axes.
MECH-341 substrate work is a prerequisite for the full matrix.

---

## Decision rules

Each rule has the form `if (observation) -> (decision)`. Rules are applied in order; the
first matching rule wins.

### Theory 1 (CEM elite-pool collapse)

- **R1.a** If V3-EXQ-569 matched-entropy control shows SP-CEM entropy = noise-matched entropy on
  all diversity metrics (entropy, coverage, trajectory_class_count): theory 1 is **not
  load-bearing on its own**. ARC-065 SP-CEM child substrate marked `non_contributory` for
  diversity (separate from its non-collapse role). Promote attention to theories 2-4.
- **R1.b** If V3-EXQ-569 shows SP-CEM strictly > matched noise on trajectory_class_count
  (FP-2 cleared): theory 1 confirmed as a real contributor; advance to Rung 2 testing.

### Theory 2 (E3 scoring collapse) -- this plan's primary new test

- **R2.a** If pre-MECH-341 trajectory_class_count >= 2 in CEM candidates but post-E3-scoring
  selected class count = 1 for >= 80% of timesteps (measured on SP-CEM-ON, MECH-269-ON
  baseline): theory 2 is confirmed as a real diversity-collapse site. MECH-341 substrate
  becomes priority.
- **R2.b** If post-E3 selected class count tracks pre-E3 candidate class count within +/- 1
  on average: theory 2 is **not load-bearing**. E3 is preserving the diversity it receives;
  the collapse must be at A or C or D. MECH-341 retains as architectural commitment but no
  substrate work is triggered.
- **R2.c** If theory 2 confirmed AND MECH-341 substrate lands AND `B_only` arm produces
  trajectory_class_count >= 2 with first_action_entropy > 0.3: MECH-341 provisional
  promotion candidate.

### Theory 3 (noise floor)

- **R3.a** If MECH-313 ON alone (`C_only` arm) produces matched-entropy-distinguishable lift
  on trajectory_class_count but not on coverage: theory 3 contributes to per-tick entropy
  but not to strategic diversity. Retain MECH-313 as Layer-C substrate but escalate
  attention to theories 2/4.
- **R3.b** If ablate_C arm (drop MECH-313 from ALL_ON) drops trajectory_class_count below 2
  while Rung 1 metrics for ALL_ON pass: MECH-313 is necessary-and-sufficient at Layer C;
  promote on Rung 2 PASS.
- **R3.c** If ablate_C arm leaves Rung 1 metrics unchanged from ALL_ON: MECH-313 is
  redundant under combined substrate -- candidate for de-prioritisation pending broader
  ablation matrix.

### Theory 4 (V_s representation staleness)

- **R4.a** If V3-EXQ-550 ARM_ON >> ARM_OFF on relevant diversity metrics: confounded by
  z_goal config default; V_s pathology not confirmed; theory 4 demoted. Re-run with z_goal
  matched across arms before re-evaluating.
- **R4.b** If V3-EXQ-550 ARM_ON ≈ ARM_OFF: V_s substrate pathology confirmed; theory 4
  promoted; MECH-269 follow-up substrate work prioritised.
- **R4.c** If V3-EXQ-550 ARM_ON crashes: separate substrate bug surfaces; classify as
  failure_autopsy candidate; theory 4 status unchanged until autopsy resolves.

### Cross-theory escalation rules

- **R_X.a** If ALL_ON arm produces Rung 1 PASS but `A_only`, `B_only`, `C_only`, `D_only`
  all individually FAIL Rung 1: diversity is **emergent across substrates** (INV-074
  plasticity-crystallization invariant fires); no single Layer is load-bearing. Promote
  ARC-065 on multi-arm evidence.
- **R_X.b** If two single-substrate arms (e.g., `A_only` and `C_only`) each PASS Rung 1
  independently: substrates are **partially redundant**; revisit Q-045 (MECH-313 vs
  MECH-260 independence) and propose new Q-claim on A-vs-C redundancy.
- **R_X.c** If ALL_ON FAILS Rung 1: the four-substrate stack as currently specified is
  insufficient; **expand candidate set** to theories 5-8 (proposal-distribution bias,
  MECH-260 anti-recency, MECH-314 curiosity weight, z_goal config-default) before further
  Layer-A/B/C/D refinement.

---

## Experiment sequencing

Layer-B (MECH-341) substrate does not yet exist, so the full isolation matrix cannot run
in one pass. Phased approach:

### Phase P1 -- Pre-existing-substrate isolation (executable now)

**Arms:** BASE_OFF, A_only, C_only, D_only, ALL_ON (excluding Layer-B). MATCHED_NOISE
arm for FP-2 control. **6 arms.**

**Target:** Pin which of theories 1, 3, 4 is load-bearing under the current main-path
substrate. Apply R1, R3, R4 decision rules.

**Falsifiers reused:** V3-EXQ-567 (A_only effect already measured), V3-EXQ-569 (matched
noise, queued), V3-EXQ-550 (D_only effect, in flight).

**Required new EXQ:** A 6-arm P1 isolation run combining all three substrates on a single
SD-054 episode set, so the cross-substrate comparison is on matched data. Recommend
queueing as **V3-EXQ-TBD (P1 layer isolation, 6 arms)** -- queue via `/queue-experiment`
skill, not directly.

### Phase P2 -- E3 scoring diagnostic (executable now; no substrate needed)

**Arms:** ALL_ON_now (A+C+D, no MECH-341), instrumented to log:
- per-tick: pre-E3 CEM candidate trajectory_class_count
- per-tick: post-E3 selected trajectory_class_count
- per-tick: E3 score distribution across distinct classes (mean, std, top-2 gap)

**Target:** Apply R2.a / R2.b. **No substrate change**, just instrumentation. If R2.a
fires: MECH-341 substrate work is justified and prioritised. If R2.b fires: MECH-341 stays
architectural-only.

**Required new EXQ:** **V3-EXQ-TBD (P2 E3 score-collapse diagnostic, instrumentation only)**.
Same SD-054 episode set as P1; can be a single-arm probe.

### Phase P3 -- MECH-341 substrate build + B-axis test

**Trigger:** P2 confirms R2.a.

**Substrate work:** Implement MECH-341 (one of: entropy bonus over candidate classes at
E3 aggregation; class-stratified argmax with proportional sampling within class; jittered
tie-breaking when top-K E3 scores are within epsilon). Specific design open -- see
"Substrate design options" below.

**Arms (post-build):** B_only, ablate_B, ALL_ON (now including B). **3 arms.**

**Target:** Apply R2.c. Promote MECH-341 if `B_only` produces Rung 1-comparable diversity
in isolation OR if ablate_B drops Rung 1 metrics significantly.

### Phase P4 -- Full matrix (post-MECH-341 landing)

Run the 11-arm matrix on a downstream env (CausalGridWorld or a new substrate) for
replication and to apply R_X rules. **Blocked on Rung 2 SD-054 clearance + MECH-341 landed.**

---

## Substrate design options for MECH-341 (when P3 triggers)

The claim asserts that E3 must preserve trajectory-class diversity across its scoring step.
There are at least three plausible implementations:

1. **Entropy bonus over candidate classes.** E3 score = harm_score + lambda * H(class | candidates).
   Penalises homogenisation of the candidate pool at scoring time. Risk: lambda is another
   tuning knob; matched-noise control needed.
2. **Class-stratified argmax with within-class proportional sampling.** Stratify candidates
   by first-action class; pick best within each class; sample across classes proportional
   to their best-in-class scores. Preserves all surviving classes; biases toward best
   representative of each.
3. **Jittered tie-breaking near top.** Standard argmax, but when top-K scores are within
   epsilon, sample uniformly across them. Cheapest implementation; only affects diversity
   when E3 scores are nearly tied (which is precisely when diversity is being lost).

These three options are not mutually exclusive (could combine 1+3). Pre-implementation
governance: which to try first should be decided after P2 results, since P2's per-tick E3
score distribution data will tell us whether the collapse is happening at near-ties
(option 3 sufficient) or at large score gaps (option 1 or 2 required).

---

## Status table (resume primitive)

| Theory | Layer | Claim | Substrate status | Falsifier | Result | Decision |
|--------|-------|-------|------------------|-----------|--------|----------|
| 1 CEM collapse | A | ARC-065 (SP-CEM child) | landed 2026-05-17 main-path; **E2-world-forward per-candidate signal collapse identified 2026-05-25 (root cause doc)** | V3-EXQ-567 / V3-EXQ-569 / V3-EXQ-571 / V3-EXQ-573 / V3-EXQ-609 | 567 PASS (entropy 0.012->0.497); 569 + 573 non_contributory (bias channel structurally zero); 570/571/609 diagnostics landed | **R1 falsifier blocked**: per-candidate bias signal structurally zero (all K cands -> identical z_world after one E2 step). Awaiting E2-world-forward substrate fix; V3-EXQ-569a queued after substrate lands |
| 2 E3 scoring | B | **MECH-341** (registered 2026-05-25) | **IMPLEMENTED 2026-05-27 (options 1+2 togglable)** | V3-EXQ-608 P2 (PASS R2a large-gap 2026-05-26); V3-EXQ-611 P3 substrate-readiness diagnostic queued | 608 majority R2a fired; substrate landed; readiness eval pending | apply R2.c on V3-EXQ-611 PASS + B_only / ablate_B successor |
| 3 noise floor | C | MECH-313 | landed | V3-EXQ-543b ARM_MECH313 (pending Q-045 retest) | autopsy 603b: substrate operative but design-blocked | retest via 603c (training-phase fix) |
| 4 V_s stale | D | MECH-269 / 269b | substrate-ready (IGW-021); MECH-269b staleness wiring landed | V3-EXQ-550 (z_goal probe); V3-EXQ-601 (MECH-269b staleness gate) | 550 FAIL/supports MECH-269 2026-05-11T20:18Z; 601 PASS/supports MECH-269b 2026-05-21T12:02Z; both reviewed | **R4.b reading** (V_s pathology supported; theory 4 promoted) flagged 2026-05-28 pending governance stamp; Q-040b behavioural sufficiency still open under goal_pipeline:GAP-4 (V3-EXQ-490g cohort) |

**Update cadence:** every time a P-phase experiment lands, update this table in-place with
the result and the decision-rule outcome. This is the resume primitive across sessions.

### 2026-05-28 GAP-D disposition (pending governance stamp)

V3-EXQ-550 landed 2026-05-11T20:18Z with outcome=FAIL but
`evidence_direction_per_claim={MECH-269: supports}`. The FAIL is on the diagnostic
falsifier's PASS criterion (wired-but-untrained z_goal did NOT materially shift action-class
entropy at this probe depth), which under the manifest's own interpretation grid SUPPORTS
the substrate-level reading of MECH-269 -- the V_s pathology survives. V3-EXQ-601 PASS
2026-05-21T12:02Z (MECH-269b-followup-A staleness-gate wiring) supplies an independent
substrate-path confirmation.

Applying the decision rules in this doc:

- **R4.a** (ARM_ON >> ARM_OFF, z_goal config-default confound, theory 4 demoted) -- does NOT
  fire. The manifest reads supports-MECH-269, not weakens.
- **R4.b** (ARM_ON ~ ARM_OFF, V_s pathology confirmed, theory 4 promoted, MECH-269 follow-up
  substrate work prioritised) -- **fires**. This is the disposition flagged here for the
  next /governance cycle to stamp.
- **R4.c** (ARM_ON crashes) -- does NOT fire. No crash recorded in the 550 manifest.

This is a doc-sync update; no claims.yaml or manifest edit is performed in this pass.
review_tracker.json already contains both 550 run pairs (2026-05-11T19:01Z + 20:18Z) and
both 601 run pairs (2026-05-21T11:47Z + 12:02Z). The next /governance cycle picks up the
manifest's supports-MECH-269 per-claim direction automatically; the R4.b promotion is a
governance-level decision (held in the recommendations queue as a `held_promotion` or
applied directly per category gating in the indexer) rather than a new experiment.

Q-040b behavioural sufficiency (MECH-295 / StepHarness cohort) is the only remaining open
item under GAP-D and is currently owned by IGW-20260528-016 (goal_pipeline:GAP-4,
V3-EXQ-490g Tier-1 retest cohort). GAP-D therefore transitions from `in_progress` to
`pending_governance_stamp`; close to `done` after the next /governance cycle.

---

---

## New claims registered with this plan (2026-05-25)

| Claim | Title (abbreviated) | Type | Status |
|-------|---------------------|------|--------|
| MECH-341 | e3_scoring_preserves_trajectory_class_diversity | mechanistic_implementation | candidate, v3_pending |
| Q-054 | minimum trajectory-class diversity floor for ARC-062 (was proposed as Q-046) | open_question | open |
| Q-055 | sleep consolidation: diversity-preserving vs eroding (was proposed as Q-047) | open_question | open |
| INV-076 | behavioural diversity as structural prerequisite for ethical counterfactual evaluation (was proposed as INV-074 -- ID taken 2026-05-17 by plasticity-crystallization invariant) | invariant (universal) | candidate |

Q-054, Q-055, INV-076 supersede the 2026-05-15 "proposed new claims" in the
acceptance-criteria doc (Q-046, Q-047, INV-074); their original IDs were never registered
and INV-074 was subsequently taken by a different, broader claim about plasticity
crystallization. The new IDs preserve the original scientific intent under the next
available IDs in their respective ranges.

---

## What this plan does NOT do

- **Does not redefine acceptance criteria.** The Rung 0-4 framework in the sibling
  acceptance-criteria doc is authoritative. This plan layers an isolation analysis on top of
  it.
- ~~**Does not commit to a MECH-341 implementation.** P2 diagnostic results determine which
  of the three design options (Section "Substrate design options") to build.~~ Superseded
  2026-05-27: V3-EXQ-608 P2 majority `R2a_e3_collapse_confirmed_large_gap` (large-gap,
  ruling out option 3 jittered tie-breaking) routed the substrate-design phase to options
  1 + 2. Both landed as togglable sub-flavours under one master in
  `ree-v3/ree_core/predictors/e3_score_diversity.py`. Design doc:
  `REE_assembly/docs/architecture/mech_341_e3_score_diversity_preservation.md`.
- **Does not address theories 5-8.** Those remain candidate mechanisms and re-enter the
  candidate set only if R_X.c fires (full 4-substrate stack insufficient).
- **Does not queue experiments directly.** All EXQ entries flagged here go through
  `/queue-experiment` for code-review + smoke-test discipline.

---

*This document is the plan-of-record for behavioural diversity ISOLATION (which substrate*
*layer is responsible when diversity fails). For acceptance criteria, see the sibling*
*`behavioral_diversity_acceptance_criteria.md`.*
