# ARC-062 behavioural conversion retest -- GOV-FANOUT-1 portfolio design (2026-07-29)

**Status:** design of record (legs not yet queued -- each leg is built + smoke-tested +
queued in its OWN fresh `/queue-experiment` session via a spawned chip).
**Author session:** `zealous-merkle-f5dfc8` ("ARC-062 route-retest fanout design").
**Provenance chip:** `chip-20260729-arc062-route-retest` (asked to queue THE per-claim
behavioural retest for ARC-062, unblocked by the channel-routing route-range
substrate-readiness diagnostic V3-EXQ-790/791a).
**User direction (2026-07-29):** expand the single routing probe into a **fanout** --
"if there [is] a range surely a fan out is what is needed?" (GOV-FANOUT-1).

This doc is the adversarial design-audit GOV-FANOUT-1 requires **before** queuing. It does
not itself modify `claims.yaml`, the queue, or any other plan doc.

---

## 1. Why a fanout, not one probe

ARC-062 (rule-apprehension weak reading) is a heavily-braked lineage: the re-derive brake
counter returns **21** counted `substrate_ceiling` autopsies. The brake's **release
condition is met** for the routing retest -- the named upstream substrate
(`E3Config.use_modulatory_channel_routing` + `project_channel_range`, ree-v3/CLAUDE.md
"modulatory-bias-selection-authority AMEND", IMPLEMENTED 2026-06-10) is VALIDATED-READY by
**V3-EXQ-791a** (PASS, label `route_range_substrate_ready`, both arms green, C1 load-bearing
passed; user-adjudicated 2026-07-22 via `failure_autopsy_V3-EXQ-790_2026-07-22`). ARC-062
remains `candidate` / `v3_pending` / `pending_retest_after_substrate`, so the retest is owed.

But the open question is a **discrimination among >=3 live hypotheses**, not one named build,
so GOV-FANOUT-1 applies: a single re-posed probe can silently inherit a prior confound and
return a confident-but-wrong verdict (the 732/732a failure mode). The live hypothesis space
for *why the differentiated rule-apprehension bias does not lift committed-class diversity*:

| Hyp | Statement | Design axis | Anchors |
|---|---|---|---|
| **H1** selection-authority coupling gap | the rule-apprehension channel's OWN cross-candidate range never reached the modulatory bias the authority rescales -- it was flattened by the SD-033a consuming head. Every prior 654 run routed `cand_world_summary` (a DIFFERENT channel), never `gated_policy`. | representation / coupling | `failure_autopsy_569f-661-654a_2026-06-10`; CLAUDE.md route-range AMEND ROOT-CAUSE block |
| **H2** F-dominance, downstream of selection | F monopolises ~88-89% of E3 committed-selection variance (V3-EXQ-571); the committed argmin over F-dominated scores is structurally immovable by a single selection-face bias. | algorithm (F-vs-bias arbitration) | 654g/i/j, 714; `failure_autopsy_f-dominance-conversion-cluster_2026-06-20`; 4 inert channels (CRF/OFC/dACC/noise-temp) |
| **H3** competence / action-learning gap | the deficit is diffuse and lives in the ONE invariant 724 never varied: bias-head-only REINFORCE over prediction-trained representations (prediction-rich, action-poor). The agent commits (5 classes, ~1.4 nats) but forages ~=0 res/ep and is contaminated 7-11x/ep. | drive / learning-mechanism | `failure_autopsy_V3-EXQ-719a_2026-07-08`, `failure_autopsy_V3-EXQ-724_2026-07-09` |
| **H4** measurement aliasing | the weak reading is specifically about forming >=2 **context-gated** regimes; marginal committed-class entropy (the 654-lineage DV) may be blind to a **context-conditioned mode-switch** (reef-context vs open-context committed distribution divergence). | measurement | claim `functional_restatement` (reef-context vs open-context heads); 604c broadcast-scalar caution |

Aliasing to break: P-A's canonical FAIL (C1 holds, C2 fails) aliases **H2 <-> H3** -- both
produce "bias reaches committed action but does not convert." P-A alone cannot separate them;
that is exactly why P-B (F-dominance) and P-C (competence, an orthogonal upstream DV) are in
the portfolio. P-D closes the measurement gap so a P-A/P-B/P-C null is not merely a wrong-DV
artifact.

---

## 2. The four legs

All legs: run on **cloud** (`machine_affinity: any`; prefer cloud over the Mac -- the 654/689
lineage ran cloud, and arm-reuse fingerprints are cloud-machine-class bound). Each leg is
built + code-reviewed (Step 3.5) + smoke-tested + queue-validated in its OWN fresh
`/queue-experiment` session. Each script must carry the `interpretation.preconditions[]` +
`criteria_non_degenerate{}` machinery and the arm-scoped `precondition_gate` (the 785/790->791a
lesson: never AND a whole-run gate across arms). Clear the E3 diagnostics latch immediately
before every `select_action` and emit `n_latched_ticks` (the ~9x pseudo-replication defect;
791a's corrected denominator is the reference).

### Leg P-A -- H1 (selection-authority coupling) -- THE chip's retest -- `evidence`

- **Axis:** representation / coupling.
- **Template:** `ree-v3/experiments/v3_exq_654j_arc062_gapb_rule_apprehension_nogo_behavioural_falsifier.py`
  (the ARC-062 behavioural-falsifier structure: matched stack, C1a-f readiness, C2
  committed-class entropy lift, three-branch NO-weakens map) **merged with** the routing
  wiring + arm-scoped gate + latch-clearing of
  `ree-v3/experiments/v3_exq_791a_channel_routing_cross_class_magnitude_replication.py`.
- **The single new thing vs 654j:** set
  `use_modulatory_channel_routing=True`, `modulatory_channel_route_source="gated_policy"`
  as a **matched constant on BOTH arms** -- so the rule-apprehension channel's OWN
  per-candidate range is routed into `_modulatory_accum` (identity-routed per CLAUDE.md
  route-range AMEND (3), source list includes `"gated_policy"`), rather than routing
  `cand_world_summary` (654j) while the rule bias flows through the flattening SD-033a head.
- **Swept variable:** `use_candidate_rule_field` (ARM_OFF collapsed legacy rule_state vs
  ARM_ON matured differentiated CRF rule_state), exactly as 654j. Everything else matched.
- **C1 readiness (any fail -> `substrate_not_ready_requeue`, NEVER a weakens):** 654j's C1a-f
  PLUS a **routing readiness gate keyed on the SAME statistic C1 routes on** -- the
  `gated_policy` routed range (`modulatory_channel_route_range`) supra-floor on the ARM whose
  statistic is estimated from it (arm-scoped, 791a pattern; cadence-derived fresh-select floor
  = nominal-window-ticks / `beta_rate_max_steps`; NOT a magnitude proxy -- the 643
  magnitude-vs-range net).
- **C2 load-bearing:** paired-by-seed committed-class-entropy lift ARM_ON over ARM_OFF by
  `C2_LIFT_MARGIN_NATS` on a majority of seeds.
- **Declared null:** C1 confirms the `gated_policy` channel's own range REACHES and MOVES the
  committed argmax, but C2 fails => the coupling gap (H1) is **refuted** as the ceiling; weight
  shifts to H2/H3. (A `non_contributory`, NOT a weakens -- pre-registered.)
- **DV-symmetry invariance declaration (MANDATORY, per the 604c net):** the routed
  `gated_policy` bias is a **per-candidate** vector (identity-routed [K]), NOT a broadcast
  scalar, so it is **not** invariant under the argmax/softmax symmetry of the committed-class
  DV -- 791a's C2 already showed committed-class distribution MOVES on-vs-off. State this per
  arm in the queue note.
- **Claims:** `[MECH-309, ARC-062]`, `experiment_purpose="evidence"`. Only the PASS branch
  weights them (as `supports`); both FAIL branches are pre-registered `non_contributory`.
  Emit `evidence_direction_per_claim`.

### Leg P-B -- H2 (F-dominance, downstream of selection) -- `diagnostic`

- **Axis:** algorithm (the F-vs-bias committed arbitration itself).
- **Question:** is committed-class conversion recoverable ONLY when F's grip on the committed
  argmin is loosened -- i.e. is the ceiling F-dominance per se, independent of which upstream
  bias channel is pushing?
- **Design:** hold the rule-apprehension channel ON **and** `gated_policy`-routed (the P-A
  ON-arm config) as a matched constant; **sweep the F weight / F-dominance directly** in the
  committed argmin as the manipulation (an F-attenuation ladder), reading committed-class
  entropy at each rung.
- **BUILDABILITY CAVEAT (resolve at build time):** MECH-448 (F->eligibility demotion) and
  MECH-449 (Go/No-Go) are the already-built F-*rebalance* selection-face levers, and
  654i/654j armed them as matched constants and still failed C2 -- so P-B must NOT be another
  MECH-448/449 strength sweep (that is the braked design). A **direct F-weight / F-admission
  (MECH-090) attenuation** lever may be a config knob OR may need `/implement-substrate`. The
  P-B build session must first check whether a direct F-attenuation knob exists in
  `ree_core/predictors/e3_selector.py` / `ree_core/utils/config.py`; if it does NOT, P-B is
  `complicated (buildable)` and routes to `/implement-substrate`, not `/queue-experiment` --
  report that and stop (do not force a MECH-448/449 re-run).
- **Declared null:** loosening F still does not let the routed rule-apprehension bias lift
  committed-class entropy => H2-as-sole-cause is refuted (points to H3). If loosening F DOES
  recover conversion, H2 is confirmed as the operative ceiling => the fix is an F-rebalance
  substrate, and ARC-062's behavioural retest is gated behind it.
- **Claims:** `[]`, `experiment_purpose="diagnostic"` (a discriminator; weights nothing).

### Leg P-C -- H3 (competence / action-learning) -- `diagnostic`

- **Axis:** drive / learning-mechanism.
- **Spec already written:** the `policy_learning_discriminator` from
  `failure_autopsy_V3-EXQ-724_2026-07-09.md` section 7 -- arms **B0** (bias-head-only
  REINFORCE, 719a incompetence anchor) / **B1** (full trainable policy/action head with its
  own optimizer, representation permitted to adapt for action) / **B2** (non-REE vanilla RL --
  small PPO/DQN MLP -- on the IDENTICAL observation vector). Load-bearing DV: P2
  `mean_resources_per_episode` vs floor 1.0 on a majority of seeds. Keep 724's hand-coded
  greedy oracle as the positive control; reuse 724's readiness gates (oracle clears floor; B0
  reproduces incompetence; >= MIN_P2_EPISODES per cell). Interpretation grid: B1&B2 clear ->
  H1-action-mechanism (build a policy-learning substrate); B2 clears & B1 fails -> deeper
  REE-stack obstruction; B2 fails -> H2-observation-interface (target the observation
  encoding, a policy build would be wasted); B1 clears & B2 fails -> flag (implausible; check
  leakage).
- **MANDATORY STOP-CHECK (may already be built/run):** 724 CONFIRMED-routed this discriminator
  to `/queue-experiment` (suggested id ~V3-EXQ-727). The P-C build session MUST first
  `grep`/`ls` `REE_assembly/evidence/experiments/` for a landed policy-learning /
  vanilla-RL discriminator and `git -C ree-v3 log -S policy_learning_discriminator` before
  authoring. **If it already ran, do NOT re-queue** -- cite it, report its verdict, and route
  H3 to whatever build it localized. Only author if genuinely absent.
- **Declared null:** a full policy head (B1) still cannot forage competently => action-learning
  mechanism is NOT the bottleneck (obs-interface is; build target changes).
- **Claims:** `[]`, `experiment_purpose="diagnostic"`. Brake-exempt (different question).

### Leg P-D -- H4 (measurement aliasing: context-conditioned mode-switch) -- `diagnostic`

- **Axis:** measurement.
- **Question:** does the rule-apprehension channel convert to **context-conditioned**
  committed-class structure that the marginal committed-class-entropy DV (654 lineage) is
  blind to? The weak reading asserts >=2 context-gated regimes (reef-context vs open-context),
  so the correct readout may be the **divergence between per-context committed-class
  distributions**, not the pooled marginal entropy.
- **Design:** P-A's matched stack + `gated_policy` routing; partition P2 ticks by context
  (reef-exposed vs open) using the same context signal the discriminator gates on; DV =
  cross-context committed-class distribution divergence (e.g. TV or JS) in ARM_ON vs ARM_OFF,
  paired by seed. Control per-seed reef/open exposure so the partition is not lost to
  environmental sampling (the 690 R3 environmental-degeneracy lesson: seed 44 had 0 reef
  ticks). Emit a readiness gate that each context partition has adequate n on a majority of
  seeds; below-floor -> `substrate_not_ready_requeue`.
- **Declared null:** ARM_ON shows no greater cross-context committed-class divergence than
  ARM_OFF => the marginal-entropy DV was not merely aliasing a context-switch; the conversion
  really is absent (strengthens the H2/H3 reading over a measurement artifact).
- **Claims:** `[]`, `experiment_purpose="diagnostic"` (a measurement-adequacy probe; if it
  fires positive it would motivate an `evidence` re-pose with the context DV).

---

## 3. Adversarial coverage + aliasing audit

- **Coverage:** H1 (P-A), H2 (P-B), H3 (P-C), measurement-aliasing (P-D) -- the full live
  hypothesis space plus the DV-adequacy check. No live hypothesis is untested.
- **Aliasing:** the dangerous alias is H2<->H3 inside P-A's canonical FAIL. P-C's DV
  (`resources/ep`, a competence readout) is **orthogonal to and upstream of** the
  committed-class DV, so it de-aliases H3 regardless of P-A/P-B. P-B isolates H2 by making F
  the swept variable rather than the bias channel. P-D removes the "wrong DV" alias from any
  null.
- **Verdict aliasing within P-C:** handled by B2 (vanilla-RL on identical obs) separating
  "action-mechanism" from "observation-interface" -- the 724 grid.
- **Each leg declares its null** (above) so a `non_contributory` leg is informative, not
  wasted -- the price GOV-FANOUT-1 accepts for an early un-confounded answer.

## 4. Parallelism, brake, and scope notes

- Queue all buildable legs `machine_affinity: any` to run in parallel on idle cloud workers.
- **Re-derive brake:** P-A clears the brake via the substrate-built release condition (cite
  `use_modulatory_channel_routing`/`project_channel_range` + `failure_autopsy_V3-EXQ-790` +
  V3-EXQ-791a in its queue note). P-B/P-C/P-D are brake-exempt (P-B tests a different
  mechanism / may route to `/implement-substrate`; P-C/P-D are diagnostics asking different
  questions, `claim_ids=[]`).
- **NO batching across the OTHER four claims** the 790 autopsy unblocked (ARC-065 / MECH-294 /
  MECH-309 / MECH-341) -- each is its own separate `/queue-experiment` session per the chip.
  (MECH-309 is co-tagged on P-A because ARC-062's PASS branch is jointly MECH-309 support --
  that is the same test, not a batch.)
- **`arm_fingerprint` + `stamp_recording_core` + generous recording** mandatory on every leg
  (multi-arm). Each leg's OFF/baseline arm should be emitted reuse-eligible
  (`include_driver_script_in_hash=False`) as the lineage mint.

## 5. References

- Chip provenance + readiness: `failure_autopsy_V3-EXQ-790_2026-07-22.md`,
  `evidence/experiments/v3_exq_791a_channel_routing_cross_class_magnitude_replication_20260723T044051Z_v3.json`.
- Substrate: `ree-v3/CLAUDE.md` "modulatory-bias-selection-authority AMEND ... (569f/661/654a,
  2026-06-10)" (lines ~10583-10668); route source list line ~10629 (`"gated_policy"`).
- ARC-062 lineage: `docs/claims/claims.yaml` id ARC-062; `arc_062_rule_apprehension_plan.md`
  (GAP-A done / GAP-B in-progress).
- Hypothesis anchors: `failure_autopsy_V3-EXQ-719a_2026-07-08`,
  `failure_autopsy_V3-EXQ-724_2026-07-09`, `failure_autopsy_569f-661-654a_2026-06-10`,
  `failure_autopsy_f-dominance-conversion-cluster_2026-06-20`.
- Templates: `v3_exq_654j_arc062_gapb_rule_apprehension_nogo_behavioural_falsifier.py`,
  `v3_exq_791a_channel_routing_cross_class_magnitude_replication.py`.
- Method: GOV-FANOUT-1 (`docs/claims/claims.yaml`); `/queue-experiment` SKILL Step 2.5b.

---

## Erratum (2026-07-31, `/queue-experiment` build session for Leg P-A, chip
`chip-20260729-arc062-pa-route-gatedpolicy`) -- **Leg P-A's premise is factually
wrong; NOT queued.**

Leg P-A (Section 2) claims that setting `modulatory_channel_route_source=
"gated_policy"` routes **"the rule-apprehension channel's OWN per-candidate
range"** -- i.e. the SAME channel `use_candidate_rule_field` (the swept
variable) differentiates via `LateralPFCAnalog.compute_bias` / the
`CandidateRuleField`. **This is not what the code does.**

CODE-CONFIRMED (ree-v3, checked at build time):
- `modulatory_channel_route_source == "gated_policy"` routes `_bdc_gp`
  (`ree_core/agent.py:7414`), which is the output of `self.gated_policy(...)`
  -- the **ARC-062 Phase-1 `GatedPolicy` module**
  (`ree_core/policy/gated_policy.py`), NOT `LateralPFCAnalog`.
- `GatedPolicy`'s own module docstring is explicit: *"There is no connection
  to SD-033a LateralPFCAnalog in Phase 1 -- that wiring is Phase 3 ... This
  module has NO internal state buffer (no EMA, no rule_state)."*
  (`ree_core/policy/gated_policy.py` lines ~48-92). Its forward-pass inputs
  are `z_world`, `z_self`, `z_harm_a`, per-candidate feature summaries, and
  first-action one-hots -- none of which is `rule_state` or any
  `CandidateRuleField` output.
- The rule-apprehension bias P-A's swept variable (`use_candidate_rule_field`)
  actually varies is `LateralPFCAnalog.compute_bias`'s output, separately
  stashed as `_bdc_lpfc` (`ree_core/agent.py:6557`) -- and
  `modulatory_channel_route_source` has **no `"lateral_pfc"` / `"lpfc"`
  option**. The full valid-source list (`ree_core/agent.py:7405-7418` and
  `ree-v3/CLAUDE.md` line ~10728) is exactly `cand_world_summary` /
  `curiosity` / `gated_policy` / `mech295` / `coherence` -- the CRF/lateral_pfc
  channel is not among the routable sources.

CONSEQUENCE: because `GatedPolicy`'s bias does not depend on
`use_candidate_rule_field` at all, routing `"gated_policy"` as a matched
constant on both arms would add an **unrelated, equally-present-on-both-arms**
bias term. It would not make the swept CRF channel's range "reach" the
committed argmax as H1 claims -- the CRF-differentiated signal still reaches
the committed action **only** via the pre-existing `_bdc_lpfc` ->
`dacc_score_bias` summation path that 654j already used, unchanged. Queuing
P-A as literally specified would not test H1; it would silently retest
654j's own mechanism with cosmetic config noise added.

**Correct path (not performed here -- out of `/queue-experiment` scope):**
add a `modulatory_channel_route_source == "lateral_pfc"` (or `"lpfc"`)
branch identity-routing `_bdc_lpfc`, mirroring the existing `"gated_policy"` /
`"curiosity"` / `"mech295"` / `"coherence"` identity-routed branches
(`ree_core/agent.py:7412-7418`). This is a small, well-scoped substrate
addition (`complicated (buildable)`, not `complex (probe-gated)`) -- route
`/implement-substrate`, then re-author Leg P-A against the corrected source
name. Until then Leg P-A as designed here is **not buildable as specified**
and should not be queued. Chip `chip-20260729-arc062-pa-route-gatedpolicy`
resolved without queuing; a follow-on chip was spawned for the substrate
addition + design correction.

Legs P-B/P-C/P-D are unaffected by this finding (none of them depend on
`modulatory_channel_route_source="gated_policy"` routing the rule-apprehension
channel).

---

## P-B buildability resolution (2026-07-31, `/queue-experiment` build session
for Leg P-B, chip `chip-20260729-arc062-pb-fdominance`) -- **direct F-weight
attenuation knob CONFIRMED ABSENT; not queued.**

Section 2's own buildability caveat asked the P-B build session to check
`ree_core/predictors/e3_selector.py` / `ree_core/utils/config.py` for a
direct F-weight/F-admission (MECH-090) attenuation lever, distinct from
MECH-448/449, before authoring. This is that check -- it is a resolution of
an open question the design correctly flagged, not a premise error (unlike
P-A's erratum above).

CODE-CONFIRMED (ree-v3, checked at build time):

- `E3TrajectorySelector.score_trajectory` (`e3_selector.py:1118-1261`) computes
  `score = f + lambda_eff * m + self.config.rho_residue * phi`, then
  optionally subtracts/adds `benefit_weight * b`, `goal_weight * g`,
  `pe_confidence_weight * pen`, `self_viability_weight * sv_pen`. `f =
  self.compute_reality_cost(trajectory)` enters with an **implicit
  coefficient of 1.0** -- every other term in the sum has a dedicated
  `*_weight` config field that can be dialed down; F does not. There is no
  `f_weight`, `reality_cost_weight`, or any other config field anywhere in
  `e3_selector.py` / `config.py` that scales F's contribution to the score
  itself.
- MECH-090 (`docs/architecture/mech_090_commit_entry_predicate.md`,
  `HeartbeatConfig.use_commit_readiness_gate` /
  `commit_readiness_floor` in `beta_gate.py`) is **not** a scoring-weight
  lever at all -- it gates whether BetaGate *elevates into* committed mode
  based on the post-hoc score margin (top1 vs top2), after the committed
  argmin has already been decided. It cannot attenuate F's role in
  *choosing* the argmin; it only conditions whether the choice, once made,
  is allowed to propagate. Re-reading the prompt's "F-weight/MECH-090
  attenuation" as two candidate levers for the same idea, MECH-090 does not
  qualify.
- The two attenuation-shaped levers that DO exist near F are both excluded
  by design: MECH-448/449 (`e3_selector.py:1449-1686`,
  `_f_eligibility_envelope` / `_go_nogo_eligibility_gate`) act on
  **eligibility** (which candidates survive to compete), not on F's weight
  in the score itself -- and 654i/654j already armed them as matched
  constants and still failed C2, which is exactly why the prompt excludes
  them. `use_natural_commit_urgency_release` +
  `natural_commit_gap_entry_sensitivity` (`config.py:3630-3662`) is the
  **duration face** (how long a commit is held, explicitly documented as
  "PARALLEL to the selection-face MECH-448") -- it does not touch which
  candidate wins the argmin either.

CONSEQUENCE: no config knob exists today that lets P-B "hold the routed
rule-apprehension channel ON and sweep the F weight / F-admission directly in
the committed argmin" as specified. Per Section 2's own caveat, **P-B is
`complicated (buildable)`, not `complex (probe-gated)`** -- the missing piece
is a literal `f_weight: float = 1.0` (no-op default) coefficient on the `f`
term in `score_trajectory`, analogous in shape to `benefit_weight` /
`goal_weight` / `rho_residue`, threaded through `REEConfig` the same way. This
is architecturally different from MECH-448 (eligibility) and the duration-face
levers, and touches the single most heavily-used scoring path in the
substrate (every E3 selection call), so it is not a "just add a field and
default it to 1.0" drive-by change -- it needs its own SD doc, phased design
review, and backward-compat smoke test per `/implement-substrate` Steps 1-5,
not a rushed inline build here.

**Not queued.** A follow-on chip (`chip-20260731-arc062-pb-fweight-knob`) was
spawned to scope and build the `f_weight` config lever via
`/implement-substrate`; Leg P-B should be re-authored against it once landed.

Legs P-A/P-C/P-D are unaffected by this finding (P-C/P-D do not touch F's
weight in the score at all; P-A's blocker is the separate `lateral_pfc` route
source gap above).

---

## P-C STOP-CHECK resolution (2026-07-31, `/queue-experiment` build session
for Leg P-C, chip `chip-20260729-arc062-pc-policy-learning-discriminator`) --
**the discriminator already ran (twice), is confounded/terminal, and the H1/H2
question it targets is already resolved by later evidence. Not queued.**

Section 2's own mandatory stop-check asked the P-C build session to search
`REE_assembly/evidence/experiments/` and `git -C ree-v3 log -S
policy_learning_discriminator` before authoring anything, and to cite+route
rather than re-queue if a landed run is found. This is that check.

**ID-CONFIRMED:** the autopsy's suggested id (~V3-EXQ-727) was never used for
this discriminator -- V3-EXQ-727 landed as `capability_yardstick_calibration`
(2026-07-09), an unrelated WS-3 item. The actual `policy_learning_discriminator`
scripts are `V3-EXQ-732` (`ree-v3` `1ab745d`, 2026-07-10) and its power-fixed
follow-up `V3-EXQ-732a` (`ree-v3` `613caab`, 2026-07-10) -- both matching the
autopsy section 7 spec's B0/B1/B2 arm design and DV
(`mean_resources_per_episode` vs the 1.0 floor) exactly.

**Already run, and TERMINAL:**
- `V3-EXQ-732` self-routed `H2_observation_interface_unlearnable`
  (`b1_clears_floor: false`, `b2_clears_floor: false`).
- `V3-EXQ-732a` (power bump) hit `substrate_not_ready_requeue`: its
  learner-adequacy readiness gate referenced the **privileged global oracle**
  as the competence denominator while the learner sees only a 5x5 local view
  -- the same observability confound documented in
  `failure_autopsy_V3-EXQ-732a_2026-07-10` and memory
  `reference-competence-floor-observability-confound`. That autopsy declared
  the 719a->724->732->732a chain **terminal** and the H1/H2 read
  **UNRESOLVED** by this design, and the pre-registered same-question power
  bump **V3-EXQ-732b was explicitly REFUSED** by the re-derive brake.
- Re-queuing the literal B0/B1/B2 spec here would therefore re-run a design
  already known to be confounded and already terminated by its own autopsy --
  exactly the re-derive loop `/queue-experiment` Step 2.5b exists to stop
  (`claim_ids=[]` on this diagnostic zeroes the claim-keyed counter, but the
  autopsy-stream recurrence brake still fired; see chip `task_11019ac9` /
  memory `reference-governance-pipeline-derive-only`).

**Superseded, not merely blocked:** the underlying scientific question (is
the bottleneck the policy-learning mechanism, H1, or the observation/latent
interface, H2?) has since been **definitively answered by a different, later,
cleaner design** -- `V3-EXQ-813` (survival-zeroed PPO probe, 2026-07-24),
which removed the reward-objective confound the 732 chain never controlled
for and used the same corrected local-view-vs-global-oracle readiness gate
732a's autopsy demanded. Per `hypothesis_space_registry.v1.json`:
`H-policy-learning` -> **`state: "eliminated"`**
(`resolving_runs: [V3-EXQ-737b, V3-EXQ-742a, V3-EXQ-813]`,
`resolved_utc: 2026-07-24T14:33:33Z`, basis: "PPO on raw observations CLEARS
the D3 hazard-free floor (9.033 >> 1.0) while PPO on the REE latent does not
(0.5), under the identical W3_survival_zeroed objective... the policy-learning
stage is NOT the bottleneck"; a self-routed `substrate_not_ready` on an unmet
manipulation-check was overridden per user-confirmed judgment, per
`failure_autopsy_backlog_2026-07-24`). `H-observation-interface` is now the
surviving live root, corroborated by the SD-070-encoder-warmup 734 re-run
(REE all-ON recovers at no difficulty rung; vanilla PPO recovers at D2).

**CONSEQUENCE:** ARC-062's H3 (competence / action-learning) is **not** an
open question needing Leg P-C's B0/B1/B2 discriminator -- it is already
resolved, by evidence more recent and less confounded than what P-C would
produce. H3 routes to whatever build `H-observation-interface` implies
(representation / observation-encoding, `conversion_ceiling_root`,
MECH-457-tagged), not to another policy-vs-vanilla-RL discriminator.

**Not queued.** No follow-on `/queue-experiment` or `/implement-substrate`
chip spawned from this resolution -- `H-observation-interface` is already the
tracked live frontier in `hypothesis_space_registry.v1.json` /
`competence_floor_reposing_2026-07-25.md` (R4: prediction-trained vs
random-projection `z_world`, routed as registry delta D12, owned by the
standing `competence_floor` re-posing thread), so spawning a duplicate chip
here would race an already-owned worklist item rather than add new coverage.

Legs P-A/P-B/P-D are unaffected by this finding.

---

## P-D resolution (2026-07-31, `/queue-experiment` build session for Leg P-D,
chip `chip-20260729-arc062-pd-context-modeswitch`) -- **premise HELD (unlike
P-A/P-B); QUEUED as `V3-EXQ-847`.**

Section 2's P-D design line reads "P-A's matched stack + gated_policy
routing." Per P-A's erratum above, that routing claim is factually wrong
(`modulatory_channel_route_source="gated_policy"` does not route the
rule-apprehension/CRF channel -- it identity-routes the unrelated
`GatedPolicy` module output). This build session independently verified
P-D's OWN premise rather than taking the doc's text at face value (per the
sibling-chip instruction), and it holds:

**CODE-CONFIRMED (ree-v3, this session):**
- SD-054 reef/open bipartite geometry is a real, already-live substrate
  primitive (`ree_core/environment/causal_grid_world.py`), already present
  unchanged in `v3_exq_654j`'s own `ENV_KWARGS`.
- `_is_reef_half(env)` + `_tv_distance(counts_a, counts_b)` -- the exact
  partition-and-divergence machinery P-D needs -- already exist and are
  proven live in `experiments/v3_exq_690_q054_arc062_diversity_floor_sweep.py`
  (`tv_reef_forage` per seed-arm), ported verbatim into the new script.
- V3-EXQ-690's own manifest confirms the partition is non-degenerate on this
  exact env config for seeds 42/43 (n_reef_ticks/n_forage_ticks both clear a
  10-tick floor) while seed 44 recorded `n_reef_ticks=0` under 690's
  *different* (noise-temperature-swept) policy -- the documented "690 R3"
  environmental-degeneracy lesson, not a P-D-specific finding.
- **GOV-REUSE-1 check:** V3-EXQ-690 reports the identical `tv_reef_forage`
  statistic per seed-arm, but its swept variable is
  `noise_floor_min_temperature`, never `use_candidate_rule_field` -- a
  different manipulation, so 690's manifest cannot answer H4. No other
  manifest or queue entry combines the reef/open partition with the CRF
  ON/OFF sweep. Not recoverable by reanalysis; proceeded to a new run.

**CONSEQUENCE:** unlike P-A (false premise, not queued) and P-B (missing
knob, routed to `/implement-substrate`), P-D's design is buildable as
specified -- MINUS the gated_policy routing addition, which this build
omitted entirely (a matched-constant bias term with no bearing on a
paired-by-seed ARM_ON-vs-ARM_OFF comparison; P-A's erratum already states
"P-D unaffected... does not depend on gated_policy routing mattering", and
this build makes that concrete by never wiring the route). The script is
otherwise a straight adaptation of the already-run `v3_exq_654j` matched
stack (MECH-448 demotion + MECH-449 active No-Go both kept as matched-stack
constants; swept variable `use_candidate_rule_field` unchanged) plus a new
context-partitioned readout (`tv_context_divergence`, paired-by-seed
ARM_ON-vs-ARM_OFF lift) layered on the same P2 measurement window, with a new
C1g readiness precondition (context partition adequate on a majority of
seeds, both arms) guarding the seed-44-style degeneracy before any H4
reading is drawn.

Code review also applied the fanout doc's own Section 2 preamble mandate
(clear the E3 diagnostics latch before every `select_action` + emit
`n_latched_ticks`) to the inherited MECH-448/449 diagnostics reads -- this
clears two `validate_experiments.py` advisory WARNs (stale-e3-diagnostics,
hold-weighted-readout) that the unmodified `v3_exq_654j` template still
carries uncorrected; does not affect the primary DV, which reads the
committed action directly rather than the latched diagnostics dict.

**Queued** as `V3-EXQ-847` (`experiments/
v3_exq_847_arc062_pd_context_modeswitch_committed_class_divergence.py`,
`claim_ids: []`, `experiment_purpose: "diagnostic"`, brake-exempt,
`machine_affinity: "any"`), `ree-v3` commit `4057be48fe`, confirmed present
in the coordinator's `/queue/active`. `validate_experiments.py --strict`:
OK (1 pre-existing advisory anchor-reachability WARN, also present on the
unmodified 654j template -- inherited, not new). `--dry-run`: both arms
complete, manifest written and cleaned up, no crash; C1/C1g correctly read
`False` on the tiny dry-run dose (expected -- 2 P2 episodes cannot clear the
readiness floors, matching 654j's own dry-run behaviour).

Legs P-A/P-B/P-C are unaffected by this finding.
