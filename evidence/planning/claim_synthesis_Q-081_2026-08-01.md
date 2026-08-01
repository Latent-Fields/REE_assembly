# Claim Synthesis: Q-081 measured-pair reframe

Date: 2026-08-01
Session: elastic-merkle-e0cca8 (chip chip-20260801-q081-reframe)
Skill: /claim-synthesis, applied per the governance-walk recommendation carried in
V3-EXQ-849's own interpretation and the 2026-08-01 evidence_quality_note on Q-081.

## 1. Cluster assembled

Direct nomination: Q-081, RV(z_world, operating_mode) measured pair.

| Run | Outcome | evidence_direction | Finding |
|---|---|---|---|
| V3-EXQ-824 | non_contributory | measurement_test_design_defect | `use_invalidation_trigger` alone has no causal reach to z_world/operating_mode (source-trace confirmed) |
| V3-EXQ-824a | non_contributory | measurement_test_design_defect | `use_anchor_sets` fix: reach-check MET (`landmark_arm_behavioural_reach=1.0`) -- confirms *some* causal path to z_world -- yet `rv_primary` still bit-identical across all 5 seeds |
| V3-EXQ-838 | non_contributory | measurement_test_design_defect | + `use_per_region_vs=True` + a second (temporal) manipulation family: still bit-identical across all 5 seeds |
| V3-EXQ-849 | PASS (diagnostic) | non_contributory (n/a -- reach-scan, not a recording run) | Purpose-built precursor-level reach probe against `agent.salience._input_signals`, 2 manipulation families (`iei_permute`, `jitter`), 9/10 non-degenerate cells: **zero** named salience input signal ever diverges between INTACT and either manipulated arm |

Four structurally different manipulation families (a consumer-flag scan, an
anchor-sets fix, a per-region-VS fix + second manipulation family, and a
purpose-built precursor reach-scan), all converging on the same result: **no
reach from any config lever to the specific (z_world, operating_mode) pair.**

## 2. Discrimination gate (Step 3)

All four runs carry an explicit `measurement_test_design_defect` /
`non_contributory (reach-scan, n/a)` reading, and the registry's own
evidence_quality_note already says so in terms: "four consecutive
measurement-defect / no-reach results, not evidence for or against." This is
the skill's **vacuous-criterion / test-design debt** bucket, not granularity
debt:

- Not substrate-not-ready: the substrate is fully built and ready (the
  landmark-removal arm, the anchor/per-region-VS consumers, and the
  purpose-built reach probe all exist and ran cleanly).
- Not a genuine single-point falsification: nothing about the *claim*
  (shared cross-stream organisation vs rate separation) has been tested at
  all -- the manipulation never reached the compared statistic, so there is
  no falsifying signal to demote on.
- It is a **mismeasurement**: the chosen DV pair sits on a wiring path the
  substrate does not carry variance across. Four tries fixing the lever
  side of that pair; zero tries reframing the pair itself.

**Verdict: EXCLUDE from the granularity-debt signal. Do not decompose Q-081
into finer child claims (Step 3 STOP).** The correct action is to fix the
test -- reframe the measured pair -- not to register new claims. This section
of the synthesis therefore does the thing the skill's own discipline points
at: identify the correct pair, rather than manufacture a child claim out of
a measurement artefact.

## 3. Why (z_world, operating_mode) specifically has zero reach -- mechanistic finding

Read `ree-v3/ree_core/cingulate/salience_coordinator.py`
(`SalienceCoordinator.tick()`, ~line 375-465): `operating_mode` is a softmax
over logits computed from a **closed, named set** of `_input_signals` scalars
-- `dacc_pe`, `dacc_foraging`, `dacc_difficulty`, `drive_level`, `is_offline`,
`pcc_stability`, `aic_salience`, `cea_fast_prime`, `cea_mode_prior`,
`external_task_drive`, `override_signal`, `pacc_autonomic`. **None of these
scalars is, or is derived from, z_world or any landmark/boundary-structure
quantity.** This is not a bug the four experiments were chasing -- it is a
real architectural gap: the salience/mode-selection subsystem's precursor
set has no wired edge from the hippocampal/landmark stream at all. The
`vs_rollout_gate -> E3 -> operating_mode` chain hypothesised in
`substrate_queue.json`'s `Q081-REACH-CHECK-PAIR-SPECIFIC` implementation_hint
does not exist as a literal call chain -- checked below.

## 4. What IS confirmed reachable from the same manipulation lever

The landmark/boundary-structure manipulation lever (the one all four runs
used, varying only which consumer flags were enabled) changes
`per_stream_vs` / `per_region_vs` -- the MECH-269/MECH-284 staleness scores
computed off boundary-event structure. Grepping `ree_core/agent.py` for every
consumer of `vs_rollout_gate` (the only regulator that reads
`per_stream_vs`) finds exactly three gate call sites, none of which is E3:

1. **`vs_rollout_gate.gate(latent_state, per_stream_vs, side="e1", ...)`**
   (agent.py ~4859): gates **both `z_self` and `z_world`** before they are
   concatenated into `total_state` and fed to E1's forward call. This is a
   direct, single-hop, confirmed-in-code path from the exact staleness
   statistic the manipulation lever moves onto E1's own input -- but it is
   z_world affecting *z_world's own* downstream representation, which is
   within-stream, not a cross-stream organisation test (Q-081 needs
   heterogeneous streams, not a tautology).
2. **`vs_rollout_gate.gate_stream("z_goal", ..., side="e1")`** (agent.py
   ~4895), gated on `goal.e1_goal_conditioned` (default `True`) and
   `goal_state.is_active()`: per-stream-VS-staleness-gated pass-through of
   `z_goal` into E1's prior. **z_goal is a genuinely different subsystem**
   (goal stream, not world-model stream) and is one of the signals Q-081's
   own audit checklist names.
3. **`vs_rollout_gate.gate_stream("z_harm_a", ..., side="e2")`** (agent.py
   ~8267): same staleness-gated pass-through, feeding `E2_harm_a`'s forward
   prediction. **z_harm_a is also a genuinely different subsystem**
   (affective/harm stream) and is also named on the audit checklist.

No `side="e3"` gate call exists anywhere in `agent.py` -- E3 candidate
scoring and commitment state are **not** wired to `vs_rollout_gate` at all,
which is *why* 838's own implementation_hint's hypothesised
`vs_rollout_gate -> E3 -> operating_mode` chain carried no variance: the
middle link does not exist as stated. That also rules out "E3 candidate
scores + commitment state" as a reframe target via this lever -- it would
need a different manipulation path, not just a different DV.

## 5. Recommendation

**Reframe Q-081's measured pair to RV(z_world, z_goal) or RV(z_world,
z_harm_a)**, not RV(z_world, operating_mode). Both:

- are genuinely cross-stream (world-model vs goal-stream / world-model vs
  affective-stream), preserving the question Q-081 actually asks
  (shared organisation across *heterogeneous* streams, not a within-stream
  tautology);
- have a confirmed, single-hop, already-coded causal path from the exact
  `per_stream_vs` staleness statistic the existing landmark-manipulation
  lever (used unmodified across 824/824a/838/849) is confirmed to move;
- are both already named in Q-081's own original audit checklist (z_goal,
  z_harm_a were always in scope -- operating_mode was one candidate among
  several, not the only one the claim commits to).

Between the two, **z_goal is the stronger first candidate**: it requires
only the already-default-on `e1_goal_conditioned` flag plus an active
`goal_state`, versus z_harm_a's dependency on `e2_harm_a` being configured.
Lower precondition surface = fewer ways for a fifth run to come back
degenerate/inconclusive for reasons unrelated to the science.

**Do not run a full recording pass on the new pair yet.** The registry's own
established discipline (V3-EXQ-849's raison d'etre) is: build a cheap
pre-flight reach probe for the SPECIFIC new pair first, and gate any full
run on it. `q081_pair_reach_check.py` is hardcoded to
`agent.salience._input_signals` / `operating_mode` and does not generalise
as-is -- a parallel probe module reading `E1`'s gated `z_goal` input (or
`GoalState.z_goal` pre/post `gate_stream`) against the same manipulation
arms would be a small, analogous build (same matched-arm-construction and
non-degeneracy-guard discipline as `q081_pair_reach_check.py`), not a new
recording pass. This is `/queue-experiment` scoped work, not done here.

**The direct-write substrate path (a genuine operating_mode WRITE consumer)
remains untested and out of scope for any config-lever probe**, exactly as
V3-EXQ-849 flagged. Given (z_world, z_goal) / (z_world, z_harm_a) offer a
confirmed-reachable route to the *same underlying question* at much lower
cost, that substrate-build path is not the next move -- it would only become
relevant if a z_goal/z_harm_a pre-flight probe ALSO comes back zero-reach,
which would be a first for this cluster (the manipulation's own confirmed
consumer, unlike operating_mode's disjoint precursor set).

## 6. Disposition

- Q-081 itself: **not decomposed**. Stays a single `candidate` open_question;
  this is a within-claim operationalization fix (which pair its
  `what_would_answer` / notes point at), not a new claim.
- No child claims registered (Step 3 STOP -- test-design debt, not
  granularity debt).
- Recommended `claims.yaml` edit (pending user approval, per skill Step 7):
  amend Q-081's `notes` with a dated entry recording this reframe decision
  and updating `what_would_answer` to name RV(z_world, z_goal) [primary] /
  RV(z_world, z_harm_a) [fallback] as the pre-flight-probe-gated pair,
  superseding "RV(z_world, operating_mode)" as the sole operationalization.
- Follow-on (chip separately, not built here): a `/queue-experiment` task to
  build the z_goal pre-flight reach probe (parallel to
  `q081_pair_reach_check.py`) and, contingent on it clearing non-degeneracy
  and finding reach, a full recording pass on RV(z_world, z_goal).
