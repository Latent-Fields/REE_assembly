# Failure Autopsy -- V3-EXQ-622 (staged goal-stream curriculum)

**Generated:** 2026-06-01T07:55:01Z
**Session:** failure-autopsy-v3-exq-622-20260601T075501Z
**Scope:** single
**Target:** V3-EXQ-622 (run_id v3_exq_622_goal_stream_staged_sd054_20260531T223804Z_v3)
**Claim IDs:** [] (diagnostic; no claim disposition)
**Status:** confirmed (interactive Step 8 gate passed; routing = implement-substrate AMEND)

---

## 0. Context and supersession state

V3-EXQ-622 was already accepted `non_contributory` at /governance cycle 0542Z and superseded by V3-EXQ-621a at session 0640Z (both flat + runs manifests carry `evidence_direction: superseded`, `superseded_by: V3-EXQ-621a`, no claim_ids; indexer treats as `scoring_excluded`). This autopsy was requested by the user despite the supersession to formalise the S0-PASS / S1+-FAIL decomposition reading as a durable artifact. **No claim disposition is recommended; no manifest field is changed.** The artifact's job is to record the methodology learning and surface a structured implement-substrate amend recommendation for /governance to consume.

---

## 1. Facts reconstruction (manifest verbatim)

3 seeds (42, 43, 44) on the STAGED_GOAL_STREAM condition. Stages S0-S3 with progressive ladder acceptance (`S0 AND S1 AND S2 AND S3` per seed). `evidence_direction` field in the manifest was set to `non_contributory` at write time (carried through to the now-superseded state). Per-seed acceptance:

| Seed | S0 | S1 | S2 | S3 | overall | first_failing_stage |
|------|----|----|----|----|---------|---------------------|
| 42 | PASS | FAIL | FAIL | "PASS" (approach=1.0) | FAIL | S1 |
| 43 | PASS | FAIL | FAIL | FAIL | FAIL | S1 |
| 44 | PASS | FAIL | FAIL | "PASS" (approach=1.0) | FAIL | S1 |

Per-stage headline metrics:

| Seed | Stage | z_goal_peak_max | z_goal_norm_median_last_window | mean_episode_length | approach_commit_rate | bridge_fires/ep | stage_pass |
|------|-------|-----------------|-------------------------------|---------------------|---------------------|-----------------|------------|
| 42 | S0 | 0.281 | 0.059 | 154.7 | 0.0 | 17.5 | TRUE (z_peak>=0.1) |
| 42 | S1 | 0.108 | 0.0089 | 184.8 | 0.0 | 20.8 | FALSE |
| 42 | S2 | 0.0033 | 2.3e-10 | 121.0 | 0.0 | 3.8 | FALSE |
| 42 | S3 | 4.05e-11 | 1.66e-14 | 56.4 | 1.0 | 0.0 | TRUE (approach>=0.01) |
| 43 | S0 | 0.439 | 0.382 | 34.2 | 0.0 | 4.6 | TRUE |
| 43 | S1 | 0.326 | 0.0465 | 31.7 | 0.0 | 4.5 | FALSE |
| 43 | S2 | 0.0256 | 0.0033 | 14.3 | 0.0 | 0.07 | FALSE |
| 43 | S3 | 0.0030 | 4.9e-4 | 13.1 | 1.0 | 2.0 | FALSE (median_len 15 < 60) |
| 44 | S0 | 0.342 | 0.168 | 121.9 | 0.0 | 14.0 | TRUE |
| 44 | S1 | 0.112 | 1.3e-6 | 82.6 | 0.0 | 9.7 | FALSE |
| 44 | S2 | 0.132 | 0.0176 | 63.9 | 0.0 | 2.8 | FALSE |
| 44 | S3 | 0.0094 | 3.3e-6 | 57.6 | 1.0 | 6.9 | TRUE (approach>=0.01) |

**Expected vs observed:** the experiment's script docstring states "PASS on S0 alone supports prereq (2) trainability; full ladder PASS suggests 621 failure was measurement/training wiring not scaffold design. FAIL at S0 -> goal feed insufficient; FAIL at S1+ -> persistence/risk; FAIL at S3 -> arbitration under full SD-054 conflict." Observed: S0 PASS on all 3 seeds; FAIL at S1 on all 3 seeds; failure inflection is at the S0->S1 boundary, before harm food attraction (S2) or full conflict (S3) is introduced.

**Which criterion failed:** S1's discrimination criterion `z_goal_norm_median_last_window >= 0.05 AND median_episode_length >= 40.0` failed via the `z_goal_norm_median_last_window` axis on all 3 seeds (0.0089 / 0.0465 / 1.3e-6 vs floor 0.05). Median episode length cleared the 40.0 floor on all 3 seeds at S1 (200 / 35 / 58). The collapse is in `z_goal` persistence, not in survivability.

**Methodology gap (measurement-validity):** S3's `approach_commit_rate >= 0.01` criterion is trivially satisfied by 2/3 seeds (criterion is "fires at least once in 30 episodes" -- approach_commit_rate=1.0 in seeds 42 and 44 despite z_goal at 1e-14 and 1e-3 respectively). The criterion does not gate on z_goal being non-trivial, so S3 cannot distinguish "z_goal-driven approach" from "approach by other means with collapsed z_goal."

---

## 2. Claim-layer mapping

V3-EXQ-622's `claim_ids = []` (diagnostic, per script docstring). No claim disposition is in scope. The interpretive reach is to `behavioral_diversity_isolation:GAP-C` prereq (2) ("goal-pipeline training regime produces non-trivial z_goal in default config") and to the `scaffolded_sd054_onboarding` substrate that owns that prereq.

The substrate-readiness PASS on V3-EXQ-621a (2026-06-01T05:55Z; per-claim non_contributory on Q-045 / MECH-313 / MECH-260 under the substrate-readiness diagnostic pattern; cleared GAP-C prereq (2) via C1 + C3 path with C2 z_goal floor unmet) is the load-bearing prior result. V3-EXQ-622's S0-PASS / S1+-FAIL pattern does NOT overturn that PASS at the substrate-readiness layer -- 621a's PASS was on a 4-arm substrate-readiness diagnostic, not a behavioural-runtime z_goal-persistence test. The two results are at different epistemic layers and both hold.

---

## 3. Biological-reference triage

**Reference mechanism:** mammalian goal maintenance under threat / arousal. vmPFC / dlPFC sustain goal representations against amygdala / LC-NE / dACC competing pressures via top-down gain control. The relevant biological dependencies (per the V3 substrate set already implemented):

- vmPFC goal maintenance (MECH-260, MECH-260 dACC bias suppression) -- implemented.
- LC-NE tonic arousal coupling (MECH-313 stochastic noise floor) -- substrate-landed; behavioural validation gated.
- 5-HT salience modulation of goal-seeding gain (MECH-203 SerotoninModule, MECH-204 SR-3) -- implemented.
- Drive-trace EMA (SD-012 sustained-drive amendment 2026-05-17) -- implemented.

**Formal-import check:** the staged-curriculum scaffolding (P0 frozen goal pipeline -> P1 annealed gates -> P2 measurement) is an instructional-curriculum pattern (Bengio 2009 automated curriculum learning), not a formal-definition import. The biology-divergence load-bearing question does not apply at the curriculum layer; it applies to whether the substrate the curriculum is annealing CAN sustain goal representations under the post-anneal regime.

**Missing-dependency signature:** the S1 collapse pattern (median z_goal drops 1-6 orders of magnitude when drive_floor anneals 0.9->0.2 and a mild hazard is introduced, in the SAME tick that median episode length stays at 200 in seed 42 and 35 in seed 43) resembles what happens biologically when goal maintenance has no sustained-gain mechanism: in the absence of vmPFC top-down hold under competing threat input, goal representations decay at their default time-constant (5-HT-modulated; in the SD-012 GoalState code, `decay_goal = 0.005` default) without compensatory replenishment from drive-trace at low drive_floor. The lit-anchor is Loffler 2018 (controllability selectively reduces suffering but not unpleasantness; vmPFC goal-representation maintenance under aversive context is a separate substrate from harm-stream processing) plus Knutson 2001 (NAcc anticipation under reward + threat conjunction; goal representations are gain-modulated).

**Verdict:** the failure is consistent with a missing-or-mistuned dependency on the GoalState side, not with a falsified architectural commitment to the goal stream itself. S0 PASS is positive evidence that the goal-feed substrate works in isolation. S1+ FAIL is positive evidence that the persistence layer is under-specified for the anneal trajectory the curriculum uses.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|-------|--------|-------|
| Claim alignment | N/A | no claim_ids on 622; diagnostic |
| Biological reference | clear | vmPFC goal maintenance under threat; failure matches missing-sustained-gain signature, not biology divergence |
| Developmental / dependency prerequisites | partial | scaffolded_sd054_onboarding substrate IS implemented; GoalState decay + drive-trace EMA + 5-HT salience all implemented; but the anneal trajectory of drive_floor 0.9->0.2 combined with risk_floor introduction at S1 is below what the persistence mechanism can sustain at the configured decay/EMA constants |
| Implementation completeness | partial | S0 substrate fully wired; S1+ persistence-arbitration layer functional but mistuned for the curriculum's anneal rate |
| Environment adequacy | adequate | staged curriculum localises failure precisely; S0->S1 boundary is the inflection |
| Measurement adequacy | partial | S3's `approach_commit_rate >= 0.01` criterion is uninformative (2/3 seeds trivially satisfy despite z_goal at 1e-14 / 1e-3); does not gate on z_goal-driven approach |
| Integration adequacy | failure-relevant | the failure IS at the integration of goal-stream + drive + risk-arbitration, not within any one module |
| Scale / capacity | N/A | substrate scale uninvolved |

**Recommended `epistemic_category`:** `substrate_ceiling`. The substrate-readiness PASS on 621a cleared the GAP-C prereq (2) gate at the substrate-readiness layer; 622's staged decomposition shows the substrate is below what z_goal persistence under behavioural-runtime anneal trajectories needs. Standard `substrate_ceiling` response: substrate enrichment via /implement-substrate amend, not more experiments on the existing substrate. NOTE: this is a recommendation only; no manifest field is being changed (the supersession bookkeeping already decided 622 is excluded from indexer scoring).

---

## 5. Cluster pattern

Single. V3-EXQ-622 is the only staged-curriculum decomposition in the 622/621a lineage. The broader family (591 / 540-series / 590a / 603-series substrate-uniform z_goal-zero) is structurally distinct (those are static-config substrate-readiness FAILs; 622 is a decomposition into a working S0 + collapsing S1+). 622's relationship to the family is diagnostic-additive: it tells us WHICH sub-mechanism in the family failure is load-bearing (persistence under anneal), not that there is a new failure shape to cluster.

The closest cluster-relevant comparison is the 2026-05-03 `substrate_ceiling_cross_claim_pattern.md` shape ("negative-control / absolute criterion passes; discrimination criteria fail") -- 622 instantiates that pattern at the staged-curriculum layer (S0 negative-control PASS; S1+ discrimination FAIL).

---

## 6. Repair pathway and routing

**Routing (interactive Step 8 gate, confirmed):** `implement-substrate` AMEND on `scaffolded_sd054_onboarding`.

**Rationale:** substrate-readiness PASS on 621a established that the SD-054 onboarding scheduler can produce a substrate-readiness signal at the substrate-readiness layer. 622 establishes that the P1 anneal trajectory drives a z_goal collapse before the behavioural-runtime regime is reached. The substrate exists and is wired; what is under-specified is the anneal rate of `drive_floor` (P0 frozen at 0.9, anneal to 0.2 across 30 episodes) and the timing of `risk_floor` introduction relative to that anneal. The amend lives at the anneal-curriculum layer, not at a new SD entry, because the substrate IS the same scheduler -- the failure is in its tuning, not its architectural shape.

**Recommended `evidence_quality_note` for /governance to append to the scaffolded_sd054_onboarding substrate_queue implementation_log** (exact text; not applied here):

> "V3-EXQ-622 (staged S0-S3 goal-stream decomposition diagnostic, superseded by 621a per /governance cycle 0542Z, no claim_ids) showed the goal-stream substrate is trainable in isolation (S0 PASS all 3 seeds: z_goal_peak 0.281 / 0.439 / 0.342 vs floor 0.10) but z_goal collapses 1-6 orders of magnitude at S1 (drive_floor anneal 0.9->0.2 + mild hazard introduction; z_goal_median 0.0089 / 0.0465 / 1.3e-6 vs floor 0.05) on all 3 seeds. Failure is in the persistence / arbitration layer between goal-stream and drive + risk pressure, not in the goal feed. Substrate-readiness PASS on 621a holds at the substrate-readiness layer; the behavioural-runtime layer needs the P1 anneal curriculum revised. Candidate amend axes (substrate-design only, lit-anchored sensitivity analysis pending): (a) slower or staged `drive_floor` anneal (e.g. 0.9->0.5->0.2 across more episodes), (b) decoupled `risk_floor` introduction (delay until z_goal stabilises post-anneal), (c) sustained-drive EMA recalibration at low drive_floor (drive_ema_alpha may need to fall below 1.0 at low drive levels so the trace persists rather than collapsing to the floor each tick). NOT a substrate redesign; the existing scaffolded_sd054_onboarding scheduler's P1 anneal logic is the surface. S3's approach_commit_rate criterion (>=0.01) is methodology-uninformative -- supersession bookkeeping already excludes 622 from scoring."

**No claim disposition recommended.** 622 has `claim_ids = []`; nothing to weigh.

**S3 methodology note (separate from substrate amend):** if any staged-curriculum successor is queued, S3's `approach_commit_rate` criterion should be replaced or paired with a z_goal-driven-approach criterion (e.g. approach_commit_rate conditional on `z_goal_norm > threshold` at commit tick). The current criterion does not discriminate goal-driven approach from approach-by-other-means with collapsed z_goal. This is a /queue-experiment-time concern, not a substrate amend; flagging here for the next staged-curriculum script author.

---

## 7. Learning extracted

1. **Goal-stream substrate trainable in isolation** (S0 PASS all 3 seeds). Confirms the goal feed mechanism works.
2. **Failure inflection is at the S0->S1 boundary** -- before harm food attraction or full conflict. The minimum sufficient pressure to collapse z_goal is `drive_floor 0.9->0.2 anneal + mild hazard`.
3. **z_goal persistence collapses 1-6 orders of magnitude under that pressure**, while episode survivability stays intact (median ep length 200 / 35 / 58 at S1). The collapse is in goal representation, not in agent survival.
4. **S3's approach_commit_rate criterion is methodology-uninformative** -- two seeds satisfy it trivially with z_goal at 1e-14 / 1e-3. Staged-curriculum successors should use a z_goal-conditioned criterion.
5. **Substrate-readiness PASS does not transfer to behavioural-runtime persistence under anneal trajectories** -- this is a generalisable point about substrate-readiness diagnostics vs behavioural-runtime measurements.

---

## 8. Pending behavioural follow-on (out-of-scope this session)

V3-EXQ-603d (GAP-C behavioural cluster validation -- substrate-readiness prereqs (1) + (2) + (3) cleared; queued via /queue-experiment) is the load-bearing behavioural test for the post-anneal regime. If 603d reproduces a z_goal-persistence collapse in the behavioural-runtime regime, the substrate amend recommended here becomes load-bearing for 603d's interpretation. If 603d shows behavioural diversity without z_goal collapse, then 622's S1 failure may be specific to the staged-curriculum scaffolding rather than the substrate's behavioural-runtime capability. The amend recommendation in Section 6 is conservative -- it lands a substrate-design refinement that does not depend on 603d's outcome, but its priority should be re-evaluated after 603d returns.

---

## 9. Provenance

- Manifest: `REE_assembly/evidence/experiments/v3_exq_622_goal_stream_staged_sd054_20260531T223804Z_v3.json` (verdict=null at top-level, outcome=FAIL, evidence_direction=superseded, superseded_by=V3-EXQ-621a, no claim_ids).
- Script: `ree-v3/experiments/v3_exq_622_goal_stream_staged_sd054.py` (340 lines; interpretation grid in docstring lines 9-21).
- Queue entry: `ree-v3/experiment_queue.json` (entry per WORKSPACE_STATE.md log; supersedes V3-EXQ-621 not 621a).
- Triage memo: `REE_assembly/evidence/planning/z_goal_collapse_triage_2026-05-31.md` (the routing document that established the substrate-side fix already exists in scaffolded_sd054_onboarding).
- Predecessor: V3-EXQ-621a substrate-readiness PASS 2026-06-01T05:55Z (cleared GAP-C prereq (2) at the substrate-readiness layer).
- Supersession decisions: /governance cycle 0542Z (close 405218ede1, non_contributory accepted) + supersession session 0640Z (close a86117a9d2, evidence_direction=superseded applied to both flat + runs manifests).
- Routing decision: confirmed via Step 8 interactive gate this session (option = "implement-substrate AMEND on scaffolded_sd054_onboarding").
- Companion JSON artifact: `failure_autopsy_V3-EXQ-622_2026-06-01.json`.
