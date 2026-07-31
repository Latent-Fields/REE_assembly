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
