---
closure_plan:
  id: commitment_closure
  title: "Commitment / Closure / Mode-Governance"
  registered: 2026-05-08
  scope_claims: [SD-033a, SD-033b, SD-033c, SD-033d, SD-033e, SD-034, MECH-090, MECH-091, MECH-260, MECH-262, MECH-263, MECH-266, MECH-267, MECH-268]
  sibling_plans: [sd033_governance]
  nodes:
    - id: "commitment_closure:GAP-1"
      title: "SD-033a bias head untrained (Go-side mechanically silent)"
      phase: 1
      status: blocked
      severity: load-bearing
      owner_exq: TBD
      unblocks_claims: [SD-033a, MECH-262, SD-034]
      depends_on: []
      cross_plan_link:
        - "arc_062_rule_apprehension:GAP-A"
        - "arc_062_rule_apprehension:GAP-B"
        - "arc_062_rule_apprehension:GAP-C"
        - "arc_062_rule_apprehension:GAP-D"
      blocking_external: []
      last_updated: 2026-05-09
    - id: "commitment_closure:GAP-2"
      title: "EXP-0157 (V3-EXQ-461) delayed-reward persistence PASS"
      phase: 2
      status: done
      severity: high
      owner_exq: V3-EXQ-461
      unblocks_claims: [SD-033a, MECH-090, SD-034]
      depends_on: []
      completion_note: "V3-EXQ-461 substrate-readiness runner PASS reviewed 2026-05-12; full behavioural delayed-reward arm remains blocked on GAP-3 env extensions."
      last_updated: 2026-05-12
    - id: "commitment_closure:GAP-3"
      title: "CausalGridWorldV2 env extensions (tolerance/counter-evidence/dual-cue)"
      phase: 3
      status: open
      severity: high
      owner_exq: null
      unblocks_claims: [SD-034, MECH-266, MECH-268]
      depends_on: []
      blocking_external: ["env scoping decision Q2"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-4"
      title: "OCD battery completeness (V3-EXQ-460..468)"
      phase: 2
      status: partial
      severity: high
      owner_exq: null
      unblocks_claims: [SD-034, MECH-266, MECH-267, MECH-268]
      depends_on: ["commitment_closure:GAP-2"]
      cross_plan_link: ["sd033_governance:CHK-EXP_PROPOSALS"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-5"
      title: "MECH-090 V_s commit-release pathway (V3-EXQ-481 FAIL)"
      phase: 6
      status: open
      severity: medium
      owner_exq: V3-EXQ-481b
      unblocks_claims: [MECH-090]
      depends_on: []
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-6"
      title: "MECH-260 vs SD-034 No-Go pulse boundary unclear (V4 flag)"
      phase: 8
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-260, SD-034, SD-033a]
      depends_on: ["commitment_closure:GAP-4"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-7"
      title: "MECH-091 phase-reset deferred (SD-006 phase 2)"
      phase: 8
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [MECH-091]
      depends_on: []
      blocking_external: ["SD-006 phase 2 async heartbeat"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-8"
      title: "SD-033b behavioural validation (devaluation + perceptual discrimination)"
      phase: 7
      status: blocked
      severity: medium
      owner_exq: V3-EXQ-485b
      unblocks_claims: [SD-033b, MECH-263]
      depends_on: ["commitment_closure:GAP-3"]
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-9"
      title: "SD-033c/d/e graph-consolidation incomplete"
      phase: 8
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [SD-033c, SD-033d, SD-033e]
      depends_on: []
      last_updated: 2026-05-08
    - id: "commitment_closure:GAP-10"
      title: "StepHarness audit of governance write paths"
      phase: 8
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: []
      depends_on: []
      cross_plan_link: ["sleep_substrate:GAP-6"]
      last_updated: 2026-05-08
---
# Commitment / Closure / Mode-Governance Plan

**Registered:** 2026-05-08
**Status:** active
**Scope:** close the SD-034 closure-operator + MECH-090/091 commitment + MECH-260
recency-suppression + MECH-266/267/268 mode-governance + SD-033a/SD-033b
bias-pathway substrate gaps that together govern when REE *commits*, when it
*holds*, when it *releases*, and when it *disengages* -- and the OCD test
battery (EXP-0156 .. EXP-0164 reserved at V3-EXQ-460..468) that falsifies
them. Sibling plan: [sd033_governance_plan.md](./sd033_governance_plan.md)
remains the OCD-specific test-battery sub-plan (linked from
[Test cohort](#test-cohort) below).

This plan is the durable resume-point for commitment / closure /
mode-governance work across sessions. When work pauses to handle adjacent
paths (sleep substrate; V_s anchor reset; MECH-307 conjunction architecture),
the deviation is logged in the [Decision log](#decision-log) with a resume
condition.

---

## One-line framing

> The Hold latch, the No-Go suppressor, the asymmetric mode register, the
> mode-conditioned proposer, the conflict-saturation cap, and the closure
> operator have all landed. The Go-side bias pathway is untrained, the
> behavioural env that exercises the loop end-to-end is not built, and the
> battery that would falsify the cluster is mostly script_authored but
> unqueued.

The control-plane substrate matured fast between 2026-04-10 and 2026-04-21:
MECH-090 bistable BetaGate (2026-04-10), MECH-260 FIFO action-class
suppression (2026-04-19), SD-033a LateralPFCAnalog with zeroed bias head
(2026-04-20), SD-034 ClosureOperator (2026-04-20), MECH-267 CEM-noise
mode conditioning (2026-04-20), MECH-268 dACC FIFO PE saturation (2026-04-20),
MECH-266 Schmitt-trigger asymmetric hysteresis (2026-04-21). Substrate-
readiness diagnostics PASSed across the cluster (V3-EXQ-460 / 462 / 463 /
464 / 465 / 466 / 467 / 468 sub-tests). SD-034, MECH-266, MECH-267,
MECH-268 promoted candidate -> provisional 2026-04-28.

The gap is not "more substrate"; the gap is (a) training the SD-033a bias
head so the Go side actually moves, (b) extending CausalGridWorld with the
behavioural primitives the OCD battery needs (tolerance-band completion,
counter-evidence injection, dual simultaneously-active resource cue), and
(c) authoring + queueing the rest of the battery.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| [sd033_governance_plan.md](./sd033_governance_plan.md) | Sibling plan: 2026-04-20 GAP MEMO + OCD test battery; serves as OCD-specific test-battery sub-plan under this plan |
| [docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md](../../docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md) | GAP MEMO: "REE-V3 is not missing cognition. It is missing governance." |
| [docs/thoughts/2026-04-20_modes.md](../../docs/thoughts/2026-04-20_modes.md) | Six-step mode-binding implementation sketch |
| [docs/thoughts/2026-04-20_ocd1.md](../../docs/thoughts/2026-04-20_ocd1.md) | Four constraints on closure (terminate, bind, domain-scope, dACC saturation) |
| [docs/thoughts/2026-04-20_ocd3.md](../../docs/thoughts/2026-04-20_ocd3.md) | Eight OCD subtypes mapped to control-plane failures (test-battery source) |
| [docs/thoughts/2026-04-20_ocd4.md](../../docs/thoughts/2026-04-20_ocd4.md) | SD-033 Go/Hold/No-Go gating substrate; explicit test matrix |
| [docs/architecture/control_plane_heartbeat.md](../../docs/architecture/control_plane_heartbeat.md) | MECH-090 / MECH-091 + heartbeat architecture |
| [docs/architecture/sd_033_pfc_subdivision_architecture.md](../../docs/architecture/sd_033_pfc_subdivision_architecture.md) | PFC subdivision cluster, SD-033 / SD-033a / SD-033b / SD-033c / SD-033d / SD-033e |
| [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) | SD-033a bias-pathway design, untrained head |
| [docs/architecture/sd_034_governance_closure_operator.md](../../docs/architecture/sd_034_governance_closure_operator.md) | SD-034 closure operator design (backfilled 2026-04-27) |
| evidence/literature/targeted_review_sd_034 / _connectome_mech_266 / _267 / _268 | 2026-04-27 lit-pulls for the cluster |
| substrate_queue.json SD-034, MECH-266, SD-033a entries | Implementation status anchors |

---

## Existing substrate (do not duplicate)

Lifted from [sd033_governance_plan.md "Existing substrate (not to be
duplicated)"](./sd033_governance_plan.md#existing-substrate-not-to-be-duplicated)
and extended with the post-2026-04-21 landings.

| Function | Component | Location | Status |
|---|---|---|---|
| Hold (bistable commitment latch) | MECH-090 BetaGate (bistable) | `ree-v3/ree_core/heartbeat/beta_gate.py`, `ree_core/agent.py` | active; bistable latch landed 2026-04-10; V3-EXQ-049e PASS, V3-EXQ-049a PASS, V3-EXQ-062b PASS, V3-EXQ-321b PASS |
| Urgency interrupt (hyperdirect analog) | MECH-091 z_harm_a-triggered beta release | `ree-v3/ree_core/agent.py` | implemented; phase-reset arm held on SD-006 phase 2 async |
| No-Go (recency-bias suppression) | MECH-260 `DACCAdaptiveControl._action_history` FIFO | `ree-v3/ree_core/cingulate/dacc.py` | candidate; implemented 2026-04-19; V3-EXQ-445h supports |
| Mode register with hysteresis | SD-032a SalienceCoordinator + MECH-266 Schmitt rails | `ree-v3/ree_core/cingulate/salience_coordinator.py` | provisional; MECH-266 landed 2026-04-21; V3-EXQ-464 + V3-EXQ-467 sub-tests PASS |
| Mode-conditioned write gating | MECH-261 dict-keyed registry | same | stable; promoted 2026-04-25 |
| Mode-conditioned hippocampal proposals | MECH-267 CEM-noise scale on `propose_trajectories` | `ree-v3/ree_core/hippocampal/module.py` | provisional; landed 2026-04-20; V3-EXQ-462 + V3-EXQ-465 sub-tests PASS |
| dACC PE saturation | MECH-268 FIFO outcome-history `f_sat = 1/(1 + s * max(0, n_rec - g))` | `ree-v3/ree_core/cingulate/dacc.py` | provisional; landed 2026-04-20; V3-EXQ-463 + V3-EXQ-468 sub-tests PASS |
| Closure operator (5-part "done" token) | SD-034 ClosureOperator | `ree-v3/ree_core/governance/closure_operator.py` | provisional; landed 2026-04-20; V3-EXQ-460 + V3-EXQ-466 sub-tests PASS x2 |
| Lateral-PFC-analog (rule/goal substrate) | SD-033a LateralPFCAnalog (gate-modulated EMA + frozen-zeroed bias head) | `ree-v3/ree_core/pfc/lateral_pfc_analog.py` | candidate; substrate landed 2026-04-20; **bias head untrained** (frozen-random, last Linear zeroed -> initial bias=0) |
| OFC-analog (state-space / oracle path) | SD-033b OFCAnalog + outcome oracle | `ree-v3/ree_core/pfc_analogs/ofc_analog.py` | candidate; substrate landed 2026-04-25; oracle 2026-05-04; V3-EXQ-485 PASS, V3-EXQ-485a queued |
| AIC-analog descending modulation | SD-032c AICAnalog harm_s_gain | `ree-v3/ree_core/cingulate/aic_analog.py` | candidate (independent of this plan) |
| dACC-analog conflict / pe substrate | SD-032b DACCAdaptiveControl | same | candidate (SD-032b dACC bundle) |
| Hypothesis-tag categorical write gate | MECH-094 (generalised by MECH-261) | distributed | candidate; load-bearing for sleep + replay safety -- shared with [sleep_substrate_plan.md](./sleep_substrate_plan.md) |

---

## Gap inventory

Ten gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | SD-033a bias head untrained: frozen-random with last Linear zeroed -> initial bias = 0; Go-side pathway is mechanically silent until a training protocol lands | load-bearing | MECH-262 rule-selective persistence; SD-034 mode-conditioning gate firing from a real rule_state; full-loop OCD-battery interpretability |
| **GAP-2** | V3-EXQ-461 (EXP-0157 delayed-reward persistence / Hold-axis falsifier) substrate-readiness PASS reviewed; full behavioural successor remains GAP-3 env-infra work | high | OCD battery completeness; SD-033a + MECH-090 + SD-034 Hold-axis evidence |
| **GAP-3** | CausalGridWorldV2 env extensions not built: tolerance-band completion, counter-evidence injection, dual simultaneously-active resource cue, phased rule_state training curriculum | high | SD-034 + MECH-266 + MECH-268 behavioural arms (currently smoke / sub-test only); EXP-0156/0157/0160/0162/0163/0164 full-loop runs |
| **GAP-4** | OCD battery mostly script_authored but unqueued: 460/463/464/466/467/468 authored not queued; 462/465 already executed; 461 unauthored | high | First end-to-end battery run on substrate-as-landed; baseline before behavioural arms land |
| **GAP-5** | MECH-090 V_s -> commit-release pathway substrate-readiness FAIL: V3-EXQ-481 vs_commit_release_count=0 in BOTH ON and OFF arms; release predicate never matches; anchor resets fire (63/31 per seed) but release threshold never met | medium | MECH-090 release-via-V_s pathway empirical validation; tighter coupling between hippocampal anchor invalidation (MECH-269 / MECH-284) and BG beta release |
| **GAP-6** | MECH-260 vs SD-034 No-Go pulse boundary unclear: lit-pull 2026-04-27 recommended routing post-completion negative bias through SD-033a per-candidate bias projection rather than only via MECH-260 action-class FIFO; current implementation does both, with overlapping function | medium (V4 flag) | Cleaner mode-governance separation in V4; not urgent for V3 |
| **GAP-7** | MECH-091 salient-event phase-reset held on SD-006 phase 2 async heartbeat (V3-EXQ-133 reclassified non_contributory 2026-04-22) | low (V4 deferred) | MECH-091 empirical validation; deferred to V4 unless SD-006 phase 2 lands earlier |
| **GAP-8** | SD-033b behavioural validation deferred: substrate-readiness PASS (UC1-UC5) and oracle round-trip PASS (V3-EXQ-485a sub-tests); devaluation sensitivity + perceptually-identical / task-distinct discrimination need env extensions; no behavioural EXQ queued | medium | SD-033b promotion candidate -> provisional via behavioural evidence (currently lit-only at lit_conf 0.863) |
| **GAP-9** | SD-033c / SD-033d / SD-033e graph-consolidation incomplete: SD-033c (vmPFC value integration) registers existing ARC-035 / MECH-151 / MECH-152 / MECH-235 but no consolidation step taken; SD-033d (premotor / SMA) registered but design_doc null; SD-033e (frontopolar) reserves the parallel_goal_deliberation mode name without committing the substrate | low | Claim-graph completeness; V3-scope finishing (not V4-deferred); not gating any V3 evidence path |
| **GAP-10** | StepHarness audit of governance write paths: SD-034 closure pulse, MECH-260 inject_nogo, MECH-268 outcome buffer, SD-033a bias write should all flow through the canonical `sense / update_z_goal / update_residue` sequence enforced by StepHarness landed 2026-05-08 | medium | bit-aligned governance writes; shared concern with [sleep_substrate_plan.md GAP-6](./sleep_substrate_plan.md#gap-inventory) |

---

## Sequenced plan

Eight phases. Each phase is small, verifiable, and unblocks at least one
downstream item. Phases ordered by leverage. Where work depends on adjacent
non-governance paths (sleep substrate; SD-006 async; V_s anchor reset),
that is called out as a deviation in the [Decision log](#decision-log).

### Phase 1: SD-033a bias-head training (GAP-1) -- REFRAMED 2026-05-09

**Status:** blocked on the rule-apprehension cluster's Phase 1 + Phase 2.
The ARC-062 / MECH-309 cluster registered 2026-05-08 reframes this gap:
SD-033a's bias head needs a non-oracle rule signal to train against, and
that signal lives upstream of SD-033a in the apprehension layer. See
[arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
for the parent plan; this Phase 1 closes when that plan's Phase 3
(GAP-C + GAP-D) lands.

The original Phase 1 deliverable list proposed a phased pre-training-on-
rule-cue-curriculum approach. That approach presupposed an oracle
`rule_cue_id` label that, per MECH-309's logical-necessity claim, cannot
exist honestly in REE — trainers weight rules they do not invent. Pre-
training the bias head on oracle labels would produce a substrate that
learns supervised mappings in a lab but has no honest signal source in
deployment. The reframe drops the oracle-curriculum approach in favour
of joint training through ARC-062's discriminator-driven gradient path.

Reframed deliverables (all gated on arc_062_rule_apprehension Phase 1 +
Phase 2 PASS):

1. ARC-062 discriminator output wired into `LateralPFCAnalog.update()`
   source vector as a third projection alongside `delta_proj(z_delta)`
   and `world_pool_weight * world_proj(z_world)`. Owned by
   arc_062_rule_apprehension GAP-C / Phase 3.
2. Bias head's `requires_grad_(True)` and added to E3 optimiser; gradient
   flows from existing E3 path through `score_bias` back to head weights
   — no separate loss term. Owned by arc_062_rule_apprehension GAP-D /
   Phase 3.
3. Master flag `use_lateral_pfc_analog` defaults flipped to True for
   experiments that *also* enable `use_gated_policy` (the ARC-062 flag);
   remains False elsewhere. Replaces the original "rule-cue-tagged
   experiments" condition.
4. Validation EXQ: 2-arm ablation (head trainable vs frozen-zero) on the
   ARC-062 + SD-054 stack. Acceptance: trainable arm shows non-zero
   `score_bias` after N episodes AND non-trivial reef/forage strategy
   split (cross-link to ARC-062's monomodal-collapse falsifier in
   arc_062_rule_apprehension GAP-B / Phase 2).

Contract test: `lateral_pfc_analog.score_bias` non-zero on at least one
candidate after training, zero before.

Original Q1 ("phased vs joint vs frozen-trigger training protocol") is
RETIRED -- joint-with-E3 via gradient-through-score_bias is the only
architecturally honest option once the rule signal is non-oracle. See
[Decision log](#decision-log) 2026-05-09 entry for the full reframing
rationale.

### Phase 2: V3-EXQ-461 EXP-0157 authoring (GAP-2)

The Hold-axis falsifier. Ten-line scope: copy V3-EXQ-462 structure
(rule-binding) and substitute the delayed-reward persistence env hook.
Reserve queue slot V3-EXQ-461 (already in the sd033_governance_plan
reservation table). Author script via `/queue-experiment` skill.

2026-05-12 update: substrate-readiness script authored, queued, executed,
and reviewed as `v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`.
Runner PASSed at 2026-05-12T18:04:25Z with six deterministic sub-tests:
baseline Hold, weakened passthrough, SD-033a/MECH-261 replay-gated
persistence, strengthened Hold, mode-gate table values, and SD-034 terminal
closure. GAP-2 is closed at substrate-readiness level. The full behavioural
delayed-reward task remains Phase 3 env-infra work.

Deliverables:

1. Reserve V3-EXQ-461 in `ree-v3/experiment_queue.json`. **Done 2026-05-12;
   runner PASS reviewed.**
2. Author `v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`
   with the OCD ocd4 row's substrate-readiness acceptance criteria.
   **Done 2026-05-12; dry-run and runner PASS.**
3. Update `manual_proposals.v1.json`: EXP-0157 status `queued` ->
   `executed`; reserved_queue_id `null` -> `V3-EXQ-461`.
   `experiment_proposals.v1.json` is regenerated from the manual source by
   the governance/index pipeline.

Acceptance: substrate-readiness sub-tests PASS (no env extension required
for sub-test version; full behavioural arm depends on Phase 3).

### Phase 3: CausalGridWorldV2 env extensions (GAP-3)

The behavioural-validation gate. The OCD battery is mostly substrate-
readiness diagnostics today. Promoting from provisional -> stable on
SD-034 / MECH-266 / MECH-268 needs env primitives that don't yet exist.

Deliverables:

1. Tolerance-band completion: rule_state completion fires when the agent
   reaches a state within tolerance T of the goal, not exact-match.
   Required by EXP-0156 / EXP-0157 / EXP-0162 behavioural arms.
2. Counter-evidence injection hook: env can introduce a contradicting
   outcome stream against a persistent rule_state. Required by
   EXP-0164 (SD-034 + MECH-268 commitment vs contradiction) full-loop.
3. Dual simultaneously-active resource cue: two competing goal cues
   active in the same episode. Required by EXP-0160 (MECH-266 competing
   goals) and EXP-0163 (MECH-266 mode stickiness) behavioural arms.
4. Phased rule_state training curriculum: a curriculum schedule that
   reliably elicits committed-mode sequences (the same blocker that
   stops V3-EXQ-321 / V3-EXQ-261; see substrate_queue SD-021 / SD-022
   notes).

Acceptance: a single integration smoke run with all four primitives
exercised in one episode produces non-zero committed_steps, non-zero
counter-evidence injection events, and dual cues active for >=10 ticks.

This phase has no claim-validation EXQ; it is env infrastructure.

### Phase 4: SD-034 + closure-coupled behavioural validation (GAP-4 partial)

Once Phase 3 env extensions land, re-queue the substrate-readiness EXQs
under behavioural conditions and add the previously-deferred behavioural
arms.

Deliverables:

1. V3-EXQ-460b (EXP-0156 verified-but-not-released, behavioural):
   tolerance-band completion event triggers closure pulse; agent
   disengages within bounded window. Acceptance: bounded re-evaluation
   count after completion.
2. V3-EXQ-461 (EXP-0157 delayed-reward persistence, full): rule_state /
   goal field persists across delay window; closure fires at delayed
   resolution. Acceptance: rule_state present at delay end +
   closure-pulse signature within 2 ticks of resolution.
3. V3-EXQ-466b (EXP-0162 satisficing): sufficient-but-not-optimal action
   produces correct residue discharge. Acceptance: residue_field
   discharge within domain on satisficing completion;
   not-yet-satisficed arm preserves residue.
4. V3-EXQ-468b (EXP-0164 commitment vs contradiction, full 4-arm
   behavioural): A/B/C/D interaction with counter-evidence injection.
   Acceptance: under sustained counter-evidence, MECH-268 PE caps and
   the SD-034 closure operator does NOT fire on weak local outcomes;
   under genuine completion, both fire together.

These re-runs should also serve as substrate co-validation -- a SD-034
behavioural PASS without any MECH-266/267/268 confound is the cleanest
governance signal.

### Phase 5: MECH-266 + MECH-268 behavioural validation (GAP-4 partial)

Adjacent to Phase 4 but tests the mode-register and dACC layers
specifically.

Deliverables:

1. V3-EXQ-464b (EXP-0160 competing goals, behavioural): with dual
   simultaneously-active resource cue; symmetric vs asymmetric mode
   thresholds. Acceptance: switch-cost asymmetry detectable; symmetric
   baseline matches MECH-259 legacy.
2. V3-EXQ-467b (EXP-0163 mode stickiness, behavioural): 5-arm
   parametric sweep of exit_threshold ratio under sustained mode
   pressure. Acceptance: dose-response curve along the OCD <->
   depression axis (over-binding at exit~0; under-binding at low
   enter_threshold).
3. V3-EXQ-463b (EXP-0159 dACC saturation, 500+ step sustained outcome):
   pe plateau signature across a long identical-outcome stream.
   Acceptance: pe trajectory bounded; saturation factor f_sat falls
   below 0.5 within saturation_window ticks.

### Phase 6: MECH-090 V_s -> commit-release reactivation (GAP-5)

V3-EXQ-481 substrate-readiness FAIL identified that the
`use_vs_commit_release` hook is wired but the release predicate never
matches. Anchor resets fire 63/31 per seed but the release path is inert.

Deliverables:

1. Audit `_committed_anchor_keys` capture in REEAgent: when does a
   commit-entry record an anchor key, and is the key still present in
   `HippocampalRouter` at the moment MECH-269 anchor-reset fires?
2. Either widen the BoundaryEvent rate at commit entry or relax the
   release predicate to require *any* anchor in the committed set to
   mark inactive, not all.
3. V3-EXQ-481b 2-arm ablation (V_s release ON vs OFF) on the same
   curriculum. Acceptance: vs_commit_release_count > 0 in ON arm,
   release fires within bounded window after anchor invalidation.

This phase shares concerns with [sleep_substrate_plan.md GAP-1
(MECH-204)](./sleep_substrate_plan.md#gap-inventory) -- both
involve a captured signal that no consumer reads. Cross-link maintained.

### Phase 7: SD-033b behavioural validation (GAP-8)

After Phase 3 env extensions land, run the deferred behavioural arms.

Deliverables:

1. V3-EXQ-485b devaluation sensitivity (Q-036-style): outcome is
   devalued mid-episode; OFC oracle path's predicted-outcome signal
   updates within bounded ticks.
2. V3-EXQ-485c task-distinct discrimination: perceptually identical
   states with different task roles produce distinct OFC representations.

Acceptance criteria from MECH-263 functional signatures (devaluation
sensitivity, task-role discrimination).

### Phase 8: low-priority V3 finishing + V4 deferrals

V3-scope completion items (do when other phases idle):

* GAP-9 SD-033c / SD-033d / SD-033e graph-consolidation: registration-
  finishing under the SD-033 cluster. SD-033c subsumes existing
  ARC-035 / MECH-151 / MECH-152 / MECH-235 functions (no new
  implementation -- consolidation step). SD-033d maps existing E3
  sequence-selection machinery onto premotor / SMA biology. SD-033e
  reserves the parallel_goal_deliberation mode name without committing
  the substrate. Not gating any other V3 evidence path, but in V3
  scope -- touch when next SD-033 cluster session opens.
* GAP-10 StepHarness audit of governance writes: walk SD-034 / MECH-260
  / MECH-268 / SD-033a write sites against canonical sequence after
  Phase 4 / 5 / 6 land. Sibling concern with sleep plan GAP-6;
  efficient to combine the audit pass.

V4 deferrals (genuinely out of V3 scope):

* GAP-6 MECH-260 vs SD-034 No-Go-pulse routing reconciliation: V4
  reconsideration -- route post-completion negative bias through
  SD-033a per-candidate bias projection (lit-pull 2026-04-27
  recommendation). Not blocking V3 work.
* GAP-7 MECH-091 phase-reset: gated on SD-006 phase 2 async heartbeat;
  deferred until SD-006 phase 2 lands or V4 substrate redesign occurs.

---

## Status table

The resume primitive. Updated every session that touches commitment /
closure / mode-governance work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | blocked (upstream in-progress) | arc_062_rule_apprehension Phase 1 + Phase 2 (GAP-A done; GAP-B in-progress, V3-EXQ-543b queued Mac 120 min, awaiting runner pickup) | Track via [arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md) GAP-A/B/C/D; resume when ARC-062 PASSes monomodal-collapse falsifier (V3-EXQ-543b is the live owner) | TBD | 2026-05-10 |
| GAP-2 | 2 | done | none for substrate-readiness; behavioural successor blocked on GAP-3 | Use Phase 3 env extensions for the full behavioural delayed-reward arm | V3-EXQ-461 | 2026-05-12 |
| GAP-3 | 3 | open | env scoping decision (Q2) | Pick tolerance-window default, scope counter-evidence injection API, dual-cue trigger primitive | env infra (no EXQ) | 2026-05-08 |
| GAP-4 | 2, 4, 5 | partial | tracked under Phase 2 / 4 / 5 | Phase 2 closes battery completeness; Phase 4 / 5 cover behavioural arms | per-phase EXQs | 2026-05-08 |
| GAP-5 | 6 | open | nothing internal; coupled to anchor-reset substrate | Audit `_committed_anchor_keys` capture; widen / relax release predicate; queue 481b | V3-EXQ-481b | 2026-05-08 |
| GAP-6 | 8 | deferred V4 | post Phase-4 PASS; lit-pull 2026-04-27 V4 reconsideration | none in V3 | n/a | 2026-05-08 |
| GAP-7 | 8 | deferred V4 | SD-006 phase 2 async heartbeat | none in V3 unless SD-006 phase 2 lands | n/a | 2026-05-08 |
| GAP-8 | 7 | blocked | Phase 3 env extensions (devaluation hook + task-role discriminability) | After Phase 3 PASS, queue 485b/c | V3-EXQ-485b, 485c | 2026-05-08 |
| GAP-9 | 8 | deferred | low-priority graph completeness | none in V3 | n/a | 2026-05-08 |
| GAP-10 | 8 | open | nothing | Walk governance write sites against StepHarness canonical sequence; combine with sleep-plan GAP-6 audit | substrate audit (no EXQ) | 2026-05-08 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `partial`,
`done`, `deferred`. A `paused` row carries a resume condition in the
[Decision log](#decision-log).

---

## Test cohort

The OCD test battery from [sd033_governance_plan.md SD-033 test
battery](./sd033_governance_plan.md#sd-033-test-battery-ocd4-table) is the
primary falsification cohort for this plan. Sub-plan: that document
remains the canonical OCD-axis breakdown. This plan tracks battery
completeness as a status concern.

### Battery state (2026-05-12)

| Reserved EXQ | Proposal | Subject | Status (proposal) | Status (script) |
|---|---|---|---|---|
| V3-EXQ-460 | EXP-0156 | SD-034 verified-but-not-released | script_authored | substrate-readiness PASS x2 (sub-tests) |
| V3-EXQ-461 | EXP-0157 | MECH-090 + SD-033a + SD-034 delayed-reward persistence | executed; reserved_queue_id=V3-EXQ-461 | substrate-readiness PASS reviewed |
| V3-EXQ-462 | EXP-0158 | MECH-267 rule binding | executed | substrate-readiness PASS (sub-tests) |
| V3-EXQ-463 | EXP-0159 | MECH-268 dACC conflict saturation | script_authored | substrate-readiness PASS (sub-tests) |
| V3-EXQ-464 | EXP-0160 | MECH-266 competing goals | script_authored | substrate-readiness PASS (sub-tests) |
| V3-EXQ-465 | EXP-0161 | MECH-267 intrusive simulation filtering | executed | substrate-readiness PASS (sub-tests) |
| V3-EXQ-466 | EXP-0162 | SD-034 satisficing / residue discharge | script_authored | substrate-readiness PASS x2 (sub-tests) |
| V3-EXQ-467 | EXP-0163 | MECH-266 mode stickiness | script_authored | substrate-readiness PASS (5-arm sweep sub-tests) |
| V3-EXQ-468 | EXP-0164 | SD-034 + MECH-268 commitment vs contradiction | script_authored | substrate-readiness PASS (sub-tests) |

Battery acceptance: all nine reserved EXQs script_authored and queued, all
substrate-readiness sub-tests PASS, and Phase 4 / 5 behavioural arms PASS
on Phase 3 env extensions.

### Other relevant EXQs

| EXQ | Subject | Status | Plan reference |
|---|---|---|---|
| V3-EXQ-049a / 049e / 062b / 321b | MECH-090 BetaGate bistable validation | PASS | foundational; not part of OCD battery |
| V3-EXQ-445h | SD-032b dACC reef + MECH-258/260 supports | PASS (per-claim) | MECH-260 first clean supporting evidence |
| V3-EXQ-481 | MECH-090 V_s -> commit-release substrate-readiness | FAIL (inconclusive) | GAP-5 / Phase 6 |
| V3-EXQ-485 / 485a | SD-033b OFC substrate readiness + oracle round-trip | PASS / queued | GAP-8 / Phase 7 |
| V3-EXQ-456 | SD-033a substrate-landing diagnostic | (per substrate_queue) | GAP-1 / Phase 1 baseline |

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | SD-033a (priority=2, implemented) | SD-033a, MECH-262 | docs/architecture/sd_033a_lateral_pfc_analog.md |
| GAP-2 / Phase 2 | (no separate entry; OCD battery sub-plan) | MECH-090, SD-033a, SD-034 | sd033_governance_plan.md |
| GAP-3 / Phase 3 | (env infra, no claim) | n/a | docs/architecture/causal_gridworld_v2.md (to be authored) |
| GAP-4 / Phase 2, 4, 5 | SD-034, MECH-266, MECH-267, MECH-268 (all priority=2, implemented) | SD-034, MECH-266, MECH-267, MECH-268 | sd033_governance_plan.md |
| GAP-5 / Phase 6 | (no separate entry; cross-link to MECH-269 / MECH-284 / MECH-287 V_s cluster) | MECH-090, MECH-269, MECH-284 | docs/architecture/control_plane_heartbeat.md, docs/architecture/v_s_invalidation_runtime.md |
| GAP-6 / Phase 8 | (V4 flag, no entry yet) | MECH-260, SD-034, SD-033a | sd033_governance_plan.md (V4 reconsideration note) |
| GAP-7 / Phase 8 | (held on SD-006 phase 2) | MECH-091 | docs/architecture/control_plane_heartbeat.md |
| GAP-8 / Phase 7 | SD-033b (priority=2, implemented) | SD-033b, MECH-263 | docs/architecture/sd_033_pfc_subdivision_architecture.md |
| GAP-9 / Phase 8 | SD-033c, SD-033d, SD-033e | SD-033c, SD-033d, SD-033e | docs/architecture/sd_033_pfc_subdivision_architecture.md |
| GAP-10 / Phase 8 | (no entry; audit) | (audit, no claim) | shared with sleep_substrate_plan.md GAP-6 |

The substrate_queue.json edits to update `design_doc` fields for SD-034,
MECH-266, MECH-267, and MECH-268 to point at this plan are made in the same
session as plan registration (see [Decision log](#decision-log)).

---

## Cross-link with sleep plan

[sleep_substrate_plan.md](./sleep_substrate_plan.md) and this plan share
two load-bearing claims:

1. **MECH-094 hypothesis-tag generalisation by MECH-261 mode-conditioned
   write-gate registry.** Sleep plan's GAP-3 (Phase B-E flags default-False)
   and GAP-6 (StepHarness audit) both ride on MECH-094 / MECH-261 staying
   the canonical write-gate primitive across waking and offline phases.
   This plan inherits the same primitive as the closure operator's mode-
   conditioning gate (SD-034 closure blocked in `internal_replay` /
   `offline_consolidation` modes).

2. **Captured-but-unread signal pattern.** Sleep plan GAP-1: MECH-204
   `precision_at_rem_entry` captured at REM entry, never read by any
   consumer. This plan GAP-5: MECH-090 `_committed_anchor_keys` captured
   at commit entry; V_s release predicate never matches. Same architectural
   smell, different substrate.

3. **StepHarness audit (GAP-10 here, GAP-6 in sleep plan).** Combine into
   one audit pass when either plan reaches Phase 5 / Phase 8 -- governance
   write sites and sleep-period write sites both want the same canonical
   `sense / update_z_goal / update_residue` discipline.

Sessions that touch *both* plans (e.g. closure-during-sleep questions, or
V_s read-path work) should update the [Status table](#status-table) on
both this plan and the sleep plan.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-05-16 - Closure-map reconciliation: GAP-1 upstream gate (arc_062:GAP-B) cleared by ARC-065 SP-CEM

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-1 (SD-033a bias head untrained, load-bearing) is gated through
cross_plan_link arc_062:GAP-A/B/C/D. The load-bearing upstream node
arc_062:GAP-B (CEM-candidate-distinguishability) was reconciled
blocked -> open today: V3-EXQ-567 PASS (supports ARC-065) provides the
support-preserving CEM that lifts candidate support 1.007 -> 2.810 and
natural action entropy 0.012 -> 0.497, satisfying the 2026-05-11
substrate-readiness gate. V3-EXQ-563a / 563c independently confirmed the
E3 rule_bias actuator is wired and live (bias-norm wiring confirmed).

GAP-1 itself stays `blocked`: the bias head is still untrained until the
re-issued MECH-309 falsifier lands on SP-CEM, then GAP-C (route
discriminator to LateralPFCAnalog.update source) and GAP-D (add
rule_bias_head.parameters() to the E3 optimiser) close. But the path is
now substrate-unblocked end-to-end -- GAP-1 is no longer waiting on an
unresolved root cause, only on the sequenced GAP-B -> C -> D execution.
GAP-2 remains done (2026-05-12); its dependant GAP-4 dependency is
therefore satisfied (GAP-4 still needs the OCD-battery EXQ scoping).

### 2026-05-12 - GAP-2 V3-EXQ-461 substrate-readiness PASS reviewed

GAP-2 moved `open -> done` at substrate-readiness level. New script:
`ree-v3/experiments/v3_exq_461_mech090_sd033a_delayed_reward_persistence.py`.
Queue entry: `V3-EXQ-461` (priority 2, machine_affinity any, 5 min) was
auto-picked by DLAPTOP-4.local and PASSed in 2.1s. Manual proposal EXP-0157
updated to `executed` with `reserved_queue_id=V3-EXQ-461`.

Scope decision: this is deliberately the substrate-readiness version of the
ocd4 delayed-reward-persistence row, not the full behavioural delayed-reward
task. It validates the contract that the behavioural successor will need:
MECH-090 delay-window Hold, a weakened/no-Hold passthrough contrast,
SD-033a rule_state persistence under the MECH-261 replay gate, a strengthened
Hold threshold contrast, the sd_033a mode-gate table, and SD-034 terminal
closure release. Dry-run and runner execution both PASSed all six sub-tests
on 2026-05-12. Full delay-to-reward behaviour remains blocked on GAP-3
CausalGridWorldV2 env extensions (delay-to-benefit, tolerance-band
completion, counter-evidence, dual-cue primitives).

Resume condition: none for GAP-2 substrate-readiness. Next work is GAP-3 if
the goal is the full behavioural delayed-reward arm.

### 2026-05-09 - GAP-1 reframed as ARC-062-dependent

Phase 1 deliverable 1 (Q1 training protocol) and deliverable 4 (rule-cue
gridworld) both presupposed an oracle `rule_cue_id` label that the
architecture says doesn't exist (MECH-309: trainers weight rules they do
not invent). Per the rule-apprehension cluster registered 2026-05-08
(MECH-309 / ARC-062 / ARC-063), the rule-creating substrate is ARC-062
(V3 weak reading) / ARC-063 (V4 strong reading), not the env. SD-033a
sits *downstream* of that layer in the apprehension → commitment
pipeline.

GAP-1 reclassified `open → blocked` on `arc_062_rule_apprehension:GAP-A/B`
(parent plan-of-record [arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
registered same session). The Phase 1 deliverable list is rewritten so
the bias head is trained jointly with E3 via the existing score-aggregation
gradient path, with the rule signal arriving from ARC-062's discriminator
rather than from an oracle label.

Two preceding lit-pulls 2026-05-09 grounded the architectural decisions:
- Pull A (`targeted_review_arc_062_rule_apprehension/` 8 entries) resolved
  R1 (multi-stream discriminator input), R2 (N=2 heads at Phase 1, V4 caveat
  on continuous mixed-selectivity), R3 (Phase-1 default = score_bias level).
- Pull B (`targeted_review_arc_062_refuge_forage_ecology/` 6 entries)
  resolved R4 (multi-signature tolerance window, PASS rule = at least
  2 of 4 acceptance criteria hold across seeds).

Q1 in [Open questions](#open-questions) is retired by the reframe; joint-
with-E3 via gradient-through-score_bias is the only architecturally honest
option once the rule signal is non-oracle. The plan-doc-default phased-
pre-training option is dropped.

Cross-plan link to `arc_062_rule_apprehension_plan.md` GAP-A / B / C / D
established. Sessions that touch *both* plans should update the
[Status table](#status-table) on both.

### 2026-05-08 - Plan registered

Plan-of-record commitment_closure_plan.md registered. Ten gaps surfaced and
sequenced into eight phases. Sibling sd033_governance_plan.md retained as
the OCD-specific test-battery sub-plan rather than merged: scope overlap
exists but sd033_governance_plan covers (a) the 2026-04-20 GAP MEMO
provenance, (b) lit-pull backlog, (c) the ocd4 test-matrix axis decomposition.
Merging would lose those entry points. Cross-link maintained via [Test
cohort](#test-cohort) and [Source artefacts](#source-artefacts).

substrate_queue.json edits this session: SD-034 + MECH-266 design_doc
redirected from sd033_governance_plan.md to commitment_closure_plan.md.
SD-033b design_doc null -> commitment_closure_plan.md (in scope under
GAP-8 / Phase 7). SD-033c/d/e design_docs null ->
docs/architecture/sd_033_pfc_subdivision_architecture.md -- the
architecture doc IS the substrate spec, which is what design_doc should
point to whether the work is V3-scope or not (correcting an earlier
session draft that used "out of V3 scope" as the rationale; SD-033c/d/e
ARE V3 graph-consolidation work, just lower priority than the active
phases). MECH-267 + MECH-268 lack substrate_queue entries entirely --
flagged in WORKSPACE_STATE for next queue-completeness session.
MECH-204 design_doc retained at sleep_substrate_plan.md. SD-033a
design_doc retained at docs/architecture/sd_033a_lateral_pfc_analog.md.

### 2026-04-21 - MECH-266 asymmetric hysteresis implemented (substrate-prior)

Schmitt-trigger extension to SD-032a SalienceCoordinator. Per-mode
enter/exit threshold dicts; empty -> legacy MECH-259 symmetric. Validation
PASSed: V3-EXQ-464 (EXP-0160) and V3-EXQ-467 (EXP-0163) sub-tests + 5-arm
parametric sweep r in [0.10 .. 2.00].

### 2026-04-20 - SD-034 closure operator implemented (substrate-prior)

ClosureOperator coordinating five sub-signals at rule_state completion:
beta release + targeted No-Go + residue discharge + mode relaxation + PE
reset. Master flag `use_closure_operator` (default False, bit-identical OFF).
Mode-conditioning generalises MECH-094 hypothesis-tag: closure blocked in
internal_replay / offline_consolidation. Validation PASSed: V3-EXQ-460
(EXP-0156) + V3-EXQ-466 (EXP-0162) + V3-EXQ-468 (EXP-0164, coupled with
MECH-268). Lit-pull recommendation 2026-04-27 flagged V4 reconsideration:
route post-completion negative bias through SD-033a per-candidate bias
projection rather than only via MECH-260 action-class FIFO -- captured as
GAP-6 / Phase 8 here.

### 2026-04-20 - MECH-267 mode-conditioned proposals implemented (substrate-prior)

CEM-noise scale on `propose_trajectories` per operating_mode. V3
implementation is mode-conditional exploration *breadth* (CEM std multiplier);
the lit-pull 2026-04-27 recommended additionally modulating look-ahead
*horizon* -- captured as a V4 elaboration. V3-EXQ-462 + V3-EXQ-465
sub-tests PASS.

### 2026-04-20 - MECH-268 dACC PE saturation implemented (substrate-prior)

FIFO outcome-history `f_sat = 1 / (1 + s * max(0, n_rec - g))` (graded
learning-rate adapter, NOT binary cap). Coupling to SD-034: closure.tick()
calls `dacc.reset_episode_pe()`. Validation PASSed: V3-EXQ-463 (EXP-0159) +
V3-EXQ-468 (EXP-0164). Behavioural arms (500+ step sustained outcome /
counter-evidence injection) deferred -- captured as GAP-3 / Phase 3 + Phase 5.

### 2026-04-20 - SD-033a substrate landed; bias head untrained

LateralPFCAnalog with frozen-random last-Linear-zeroed bias head. Initial
score_bias = 0 by construction. Three design alternatives documented (A1
per-candidate vs uniform; A2 frozen-random vs trained; A3 EMA vs recurrent /
synaptic-hold). V3 commits to per-candidate (A1.a). Training protocol
deferred -- the gap that becomes GAP-1 / Phase 1 in this plan.

### 2026-04-19 - MECH-260 dACC FIFO action-class suppression implemented

`DACCAdaptiveControl._action_history` length 8; suppression weight applied
as positive bias (lower-is-better convention -> discourages repeats).
V3-EXQ-445h supports (3/3 seeds). Lit-pull 2026-04-27 V4 reconsideration:
overlap with SD-034 No-Go pulse -- captured as GAP-6.

### 2026-04-10 - MECH-090 BetaGate bistable latch implemented

Gate elevates only on entry to committed state; hippocampal completion
signal triggers release. V3-EXQ-049a / 049e / 062b / 321b PASS. 2026-04-25
V3-EXQ-481 substrate-readiness FAIL on V_s -> commit release pathway --
captured as GAP-5 / Phase 6.

---

## Open questions

Numbered for reference from future sessions.

- **Q1**: ~~SD-033a bias-head training protocol -- joint with E3 vs phased
  pre-training vs frozen until task-conditional trigger?~~ **RETIRED
  2026-05-09.** Resolved by the ARC-062 / MECH-309 cluster reframe: joint-
  with-E3 via gradient-through-score_bias is the only architecturally
  honest option once the rule signal is non-oracle. The phased-pre-
  training-on-rule-cue-curriculum default presupposed an oracle
  `rule_cue_id` label that MECH-309 says cannot exist honestly in REE.
  See [arc_062_rule_apprehension_plan.md](./arc_062_rule_apprehension_plan.md)
  Open Question R1 / R2 / R3 / R4 for the resolved-default values
  (biology-anchored from Pull A + Pull B lit-pulls 2026-05-09).
- **Q2**: Phase 3 tolerance-band completion default -- fixed window
  (T_default ~ 1 step / 1 grid cell) vs adaptive (scaled to env size)?
  Default proposed: fixed window per env config, configurable per
  experiment.
- **Q3**: Multi-rule SD-034 -- when multiple rule_states are committed
  simultaneously (e.g. nested goals), is the per-rule closure pulse
  sufficient or does the architecture need a chained / hierarchical
  closure operator? Default proposed: per-rule pulse for V3; chained
  closure deferred to V4 unless behavioural evidence requires it.
- **Q4**: EXP-0157 (Hold-axis) -- delayed-reward window scaling vs
  distractor density: which dimension to vary first? Default proposed:
  scale window first (cleaner falsifier; distractor density couples to
  Phase 5 dual-cue work).
- **Q5**: MECH-260 FIFO recency suppression vs SD-034 targeted No-Go pulse
  -- functional overlap? Lit-pull 2026-04-27 recommended routing post-
  completion negative bias through SD-033a per-candidate bias projection
  rather than only via MECH-260. V3 retains both; V4 reconsideration
  deferred (GAP-6 / Phase 8).
- **Q6**: V_s release predicate (Phase 6) -- relax to "any anchor in the
  committed set inactive" vs "all inactive" vs "anchor-reset rate above
  threshold"? Default proposed: any-inactive; tighten if it produces
  false-release chatter.

---

## Resume ritual

When picking up commitment / closure / mode-governance work after a
deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that was
   `paused` or `in-progress`.
3. If `paused`, find its entry in the [Decision log](#decision-log) and
   confirm the resume condition has fired.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.
7. If the work touches the [sleep plan](./sleep_substrate_plan.md) cross-
   link concerns (MECH-094 / MECH-261, captured-but-unread signal,
   StepHarness audit), update both plans' status tables.

Sessions that do NOT touch governance / closure / mode-governance work do
not need to read this document. Sessions that DO touch this work read
this document before any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite
entries die with the session; WORKSPACE_STATE.md is recent-work, not
strategic; substrate_queue.json is granular but does not capture phase
ordering or decision rationale; sd033_governance_plan.md is the OCD-
specific test-battery sub-plan, not the strategic envelope. This document
is the strategic envelope.

---

## See also

- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) -- OCD-specific test-battery sub-plan (sibling)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) -- sleep substrate plan (cross-link via MECH-094 / MECH-261 + captured-but-unread pattern)
- [evidence/planning/substrate_queue.json](./substrate_queue.json) -- SD-034, MECH-266, MECH-267, MECH-268, SD-033a, SD-033b queue entries
- [docs/architecture/control_plane_heartbeat.md](../../docs/architecture/control_plane_heartbeat.md) -- MECH-090, MECH-091, heartbeat architecture
- [docs/architecture/sd_033_pfc_subdivision_architecture.md](../../docs/architecture/sd_033_pfc_subdivision_architecture.md) -- SD-033 cluster
- [docs/architecture/sd_033a_lateral_pfc_analog.md](../../docs/architecture/sd_033a_lateral_pfc_analog.md) -- SD-033a substrate spec
- [docs/architecture/sd_034_governance_closure_operator.md](../../docs/architecture/sd_034_governance_closure_operator.md) -- SD-034 design (backfilled 2026-04-27)
- [docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md](../../docs/thoughts/2026-04-20_analysis_of_missing_pieces_and_work_to_do.md) -- GAP MEMO
- [docs/thoughts/2026-04-20_ocd1.md](../../docs/thoughts/2026-04-20_ocd1.md) .. [ocd4.md](../../docs/thoughts/2026-04-20_ocd4.md) -- OCD source thoughts
