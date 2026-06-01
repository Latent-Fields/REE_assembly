# Thought intake: Goal / wanting / liking stream repair -- object-bound incentive salience before z_goal

**Registered:** 2026-06-01
**Raw thought:** `docs/thoughts/2026-06-01_goal_wanting_liking_stream_repair.md`
**Companion docs (this intake session):**
- `literature_synthesis_2026-06-01_object_bound_incentive_salience.md` (lit pull)
- `claim_gap_2026-06-01_goal_wanting_liking_stream.md` (claim-gap + proposals)
- `failure_autopsy_V3-EXQ-626_2026-06-01.md` (626 harness-bug autopsy)
- `goal_stream_repair_diagnostic_ladder_2026-06-01.md` (Stage 0-4 ladder + impl + queue proposal)
**Plan-of-record this feeds:** `goal_pipeline_plan.md` (this intake adds a GAP-7 candidate and a decision-log entry proposal)
**Scope discipline:** planning artefacts only. No `claims.yaml`, no `experiment_queue.json`, no `ree_core/` edits made in this session. All claim IDs below are PROPOSALS.

---

## 1. Current failure pattern

The goal stream is **wired but produces no persistent, consumer-readable wanted-object
signal** under realistic conditions. The recurring observable is `z_goal_norm ~ 0` and/or
`approach_commit` decoupled from any object identity. But the failures split into two
**structurally different** classes that have been repeatedly conflated:

1. **Harness/measurement failures** -- the experiment never drives the pipeline, so
   z_goal stays at its zero init. The signature is *uniform* zero across every arm,
   including arms that are supposed to be positive controls. (V3-EXQ-626 is this class --
   see Section 4 and the failure autopsy. The EXQ-475 / 483 / 524 "update_z_goal
   omitted / TypeError" superseded family is the same class.)

2. **Substrate/abstraction failures** -- the pipeline IS driven, z_goal forms, but the
   resulting wanting signal is not *object-bound*: it does not differentiate wanting from
   liking, does not bind to resource identity, and does not produce a cue-triggered
   pre-consummatory approach distinct from consummatory liking. (V3-EXQ-514k is the
   cleanest instance: `wanting_liking_dissoc_fraction = 0.0` on all arms even with the
   SD-049 multi-resource env + SD-015 z_resource encoder enabled.)

The two classes require **opposite** next moves. Class 1 is fixed by repairing the test;
Class 2 is fixed by adding the object-bound incentive-salience layer this intake proposes.
The first job of any diagnostic ladder is to *separate* them.

---

## 2. The suspected mistaken abstraction

Current `ree_core/goal.py` (`GoalState.update`) implements, in essence:

```
effective_benefit = benefit_exposure * z_goal_seeding_gain * (1 + drive_weight * drive_trace)
if effective_benefit > benefit_threshold:
    z_goal <- (1 - alpha) * z_goal + alpha * z_world_current   # or z_resource if SD-015 on
```

That is: **a scalar benefit pulse writes the agent's current world latent (location-ish
state) into a single slow attractor.** Wanting is then `goal_proximity(z_world) =
1/(1+MSE(z_world, z_goal))` -- i.e. "how close am I to where I last got fed".

The mistaken abstraction is the identification of **"the place/state I was in when benefit
fired"** with **"the thing I want."** Concretely it conflates four things the biology
keeps separate:

- **liking** (hedonic impact at consumption) with
- **wanting** (incentive salience attributed to a cue/object), and
- **a goal location** (where) with
- **a goal object/affordance** (what).

Because the write target is raw `z_world` at contact, the only "identity" z_goal can carry
is whatever the encoder happens to fold into z_world at that location. SD-015's z_resource
encoder is an attempt to inject object-type features, but seeding still fires off a *scalar*
benefit gate with no binding step between "benefit fired" and "which object/cue caused it".

---

## 3. The corrected chain

```
contact / cue / object encounter
  -> benefit or liking pulse            (consummatory hedonic impact; existing benefit_exposure)
  -> object / resource identity binding (NEW: bind the pulse to a resource/cue token, not to location)
  -> incentive salience / wanted-object token   (NEW: per-object wanting amplitude, decays slowly,
                                                  can be re-triggered by the cue alone)
  -> z_goal candidate / goal pointer     (z_goal written FROM the wanted-object token /
                                          its affordance embedding, not from raw z_world)
  -> persistent goal maintenance         (existing slow attractor + E1 LSTM working memory)
  -> consumer readout by dACC / E3 / commitment   (existing consumers; needs non-zero input + wiring audit)
  -> pre-consummatory approach bias      (cue raises approach BEFORE benefit; existing MECH-295 bridge)
```

The novel structural commitment is the **incentive-object / goal-candidate layer between
benefit and z_goal**. The biology (Berridge/Robinson incentive salience; Cardinal/Everitt
amygdala-striatal-PFC reward circuit; Schoenbaum/Wilson/Niv OFC value-identity / cognitive
map; Corbit/Balleine specific-PIT) all converge on the same shape: a *cue/object*
representation acquires motivational salience that is (a) dissociable from hedonic
impact and (b) able to trigger approach before consumption. See the lit synthesis.

---

## 4. What is known from 514k / 625 / 626 / 623

| EXQ | Outcome | What it actually shows | Class |
|---|---|---|---|
| **V3-EXQ-626** | FAIL | **Harness bug, not substrate regression.** The bespoke `_run_episode` loop in the 626 script never calls `agent.update_z_goal(...)` (nor `update_liking` / `update_schema_wanting`). `goal_state.update()` is reachable ONLY through `update_z_goal`, so z_goal stayed at its zero init across **all four arms**. Hence ARM_A medians [0,0,0], `bridge_cue_fires=0.0`, `dacc_bias_nonzero=0.0`. C2/C3 are **vacuously** true (every arm is at zero, so "B/C collapsed" is meaningless). The 622 runner (`goal_stream_stages_sd054.py`) DID call `update_z_goal` every step and 622 **S0 PASSed** with `z_goal_norm_peak` 0.28-0.44. So formation is NOT shown to be broken. | 1 (harness) |
| **V3-EXQ-514k** | FAIL (`weakens` SD-049/SD-015; `non_contributory` MECH-229/230) | Pipeline IS driven; `wanting_liking_dissoc_fraction = 0.0` on every arm and seed. Identity probe weak; consumption samples weak. This is the **genuine object-binding gap**: even with multi-resource identity available, wanting target == liking target. Confounded by GAP-2 (SP-CEM monostrategy) per goal_pipeline_plan. | 2 (substrate/abstraction) -- but confounded |
| **V3-EXQ-625** | "PASS" headline / `acceptance_pass = false` | **Governance-suspicious.** The script sets `outcome=PASS` when the six measurement distributions have n>0 (i.e. "I measured cleanly"), but the substrate-readiness gate (C1/C2/C3) is FALSE: hazard events fired in 2/3 seeds yet **every** harm/salience consumer-input channel (`z_harm_a_norm`, `cea_low_freq_magnitude`, `bla_pe_magnitude`, `dacc_pe`, ...) is identically 0.0. This is the **harm-axis** twin of the goal-stream "event does not enter the consumer stream" problem: a scheduled environment event is not propagating into the consumer channels. The headline/acceptance conflict must be flagged for governance, not normalised. | structural (harm axis; sibling pattern) |
| **V3-EXQ-623** | PASS (`supports` MECH-104) | **Positive control.** MECH-104 volatility interrupt produced both a discriminative signal (`delta_var_unexpected` ~0.031 ON vs 0.0 ablated) AND behavioural de-commitment (24-31 decommits ON, 0 ablated), 8/8 criteria. Proves that **when a signal path is correctly wired, REE turns signal into behavioural consequence.** The goal stream's failure is therefore NOT "REE cannot convert signal to behaviour"; it is "the wanted-object signal is either never produced (Class 1) or never object-bound (Class 2)." | positive control |

**The single most important correction this intake makes:** 626 is not evidence that
protected goal formation fails. It is evidence that the 626 harness did not feed the
pipeline. The positive control that formation *can* work is 622 S0 (and V3-EXQ-582a, GAP-3
PASS, mean effective benefit at contact 0.115 > threshold). Do not let 626 license the
conclusion "z_goal collapse is explained by drive/hazard/writer-freeze" -- that diagnosis
was never reached because formation never ran.

---

## 5. What remains uncertain

- Whether, once the harness actually drives the pipeline (626a re-run), protected
  formation reproduces under the 626 reef + dACC config (it did under the 622 SD-054 config;
  the env differs).
- Whether the 514k object-binding gap survives the SP-CEM monostrategy fix (GAP-2 confound)
  or is genuinely an architectural absence. 514k alone cannot adjudicate this.
- Whether the 625 harm-consumer-zero pattern shares a root cause with any goal-stream
  consumer-input zero (i.e. is there a common "event -> consumer channel" wiring fault?).
- Whether an explicit incentive-object layer is *necessary* or whether a correctly-driven,
  correctly-measured existing pipeline already produces dissociation (must be tested, not
  assumed -- see ladder Stage 1-2).
- The right granularity of "object identity" in the grid env (per-cell type tag exists via
  SD-049; whether that is a sufficient "object token" or whether a learned affordance
  embedding is needed).

---

## 6. Why this is V3 scope, not V4

- Every module in the corrected chain already exists in V3 in some form: benefit_exposure
  (env), z_resource encoder (SD-015), GoalState attractor (SD-012/MECH-230), MECH-295
  drive->liking->approach bridge, dACC consumer, residue VALENCE_WANTING/LIKING channels.
  The gap is a **binding step + a write-source change + instrumentation**, not a new
  substrate epoch.
- SD-049 already provides per-resource identity tags in the single-agent grid env. The
  incentive-object layer can be built on the existing single-agent substrate.
- The 514k row-6 falsifier branch (goal_pipeline_plan Phase 2) is the only thing that
  escalates to V4 (multi-agent ecology), and only *on flat failure of the object-binding
  retest*. We are not there: the retest under a correctly-driven, monostrategy-fixed
  substrate has not been run.
- 623 shows the V3 signal->behaviour machinery is intact, so the missing piece is
  representational/binding, addressable in V3.

V4 territory (explicitly out of scope here): multi-agent social incentive, ecological
competition for resources, mature goal hierarchies with sub-goal planning.

---

## 7. What must NOT be claimed yet (hard guardrails)

- **Do not** mark the goal stream "closed."
- **Do not** claim wanting/liking dissociation has been demonstrated. 514k shows the
  opposite (dissoc fraction 0.0); no experiment has shown dissociation on a non-degenerate,
  object-bound substrate.
- **Do not** claim z_goal collapse has been *explained* by drive anneal / hazard /
  writer-freeze. 626 never formed z_goal (harness bug), so its C2/C3/C4 axis dissociations
  are vacuous. The explanation is pending a correctly-driven re-run.
- **Do not** treat 625 as a clean PASS. The headline PASS conflicts with
  `acceptance_pass=false`; flag for governance.
- **Do not** ratify any proposed claim (Section in claim_gap doc) as supported. Proposals
  are candidates pending evidence from the ladder.
- **Do not** run a full ecological behavioural test as the next step.
- **Do not** broad-refactor goal.py before Stage 0-1 isolate the minimal failing point.

---

## 8. Concise closure map for the goal stream

Each link is annotated with its current substrate status and the diagnostic that owns it.

| # | Link | Substrate today | Owning diagnostic (proposed) | Claim(s) |
|---|---|---|---|---|
| L0 | benefit pulse exists & crosses threshold | `env.benefit_exposure` + GoalState gate; GAP-3 PASS (582a) | Stage 0 unit | SD-012, MECH-306 |
| L1 | forced seed -> non-zero, stable z_goal | `GoalState.update` (exists) | **Stage 0 unit** (no new code) | MECH-230 |
| L2 | benefit binds to **object identity** (not location) | **MISSING** (writes raw z_world / z_resource at contact, no binding step) | **Stage 1** | **PROP: MECH-BIND-obj** |
| L3 | incentive-salience / wanted-object **token** | **MISSING** (no per-object wanting amplitude) | **Stage 1-2** | **PROP: MECH-INCENT-token** |
| L4 | z_goal written FROM token/affordance pointer | partial (z_resource seeding is closest) | **Stage 1** | MECH-230 amend; **PROP: MECH-GOALPTR** |
| L5 | persistent goal maintenance | slow attractor + E1 LSTM (MECH-116) | Stage 0/1 decay check | MECH-116, ARC-032 |
| L6 | cue-triggered wanting BEFORE consumption | MECH-295 bridge (isolation PASS) but cue=env? no cue-recall path | **Stage 2** | MECH-295; **PROP: MECH-CUEWANT** |
| L7 | consumer readout (dACC/E3/commitment) non-zero & consequential | E3 goal_weight + MECH-295 + MECH-307; dACC does NOT read z_goal directly | **Stage 3** | **PROP: MECH-CONSUME** |
| L8 | pre-consummatory approach bias | beta gate + approach_commit | Stage 3 | ARC-030, MECH-229 |
| L9 | wanting != liking dissociation | NOT shown (514k = 0.0) | Stage 2-4 (after L2-L3) | MECH-117, MECH-229 |

**Closure thesis:** the broken links are **L2-L3** (object binding + incentive token) and
the **measurement/wiring** around L1 and L7. L0/L1/L5 are substrate-present; L6/L8 are
present-but-starved. The minimal repair is L2-L3 plus a clean L1 positive control and an
L7 wiring audit -- NOT a new mature goal ecology.

---

## 9. Proposed plan-of-record updates (NOT yet applied)

- Add **GAP-7** to `goal_pipeline_plan.md`: "Object-bound incentive-salience layer (L2-L3)
  + harness-positive-control re-establishment (L1) + consumer-readout wiring audit (L7)."
  Severity: load-bearing for MECH-229 non-degenerate retest. Depends on: 626a harness fix
  (Class-1 separation) and GAP-2 SP-CEM (monostrategy confound).
- Add a decision-log entry recording the 626 harness-bug finding and the Class-1/Class-2
  split.
- These are PROPOSALS for the governance owner; this session does not edit the plan body.
