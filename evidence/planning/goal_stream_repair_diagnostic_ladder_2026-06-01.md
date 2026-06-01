# Goal-stream repair: diagnostic ladder + implementation plan + queue proposal

**Date:** 2026-06-01
**Intake:** `thought_intake_2026-06-01_goal_wanting_liking_stream_repair.md`
**Autopsy:** `failure_autopsy_V3-EXQ-626_2026-06-01.md`
**Claim-gap:** `claim_gap_2026-06-01_goal_wanting_liking_stream.md`
**Status:** PROPOSAL. No experiment queued, no substrate code written, no claim registered in
this session. Experiment scripts must be authored via `/queue-experiment`; substrate code via
`/implement-substrate`. This doc is the design those skills would consume.

**Governing principle:** isolate the minimal failing point before building the object layer.
The ladder front-loads cheap, decisive diagnostics (Stage 0-1) and gates the architectural
investment (object-bound incentive token, Stage 2+) on their outcome. Do NOT run a full
ecological behavioural test next.

---

## Deliverable E: staged diagnostic ladder

Each stage lists: purpose, exact acceptance criteria, failure routing, claim_ids policy,
expected manifest fields, and diagnostic-vs-evidence classification.

### Stage 0 -- unit-level GoalState seeding (positive control)
- **Purpose:** prove the substrate gate itself works with ideal forced inputs; make the 626
  Class-1 harness bug structurally impossible to ship again. **No agent loop, no env.**
- **Method:** instantiate `GoalState(GoalConfig(z_goal_enabled=True, drive_floor=0.9,
  drive_weight=2.0))`; call `update(z_world_forced, benefit_exposure=forced, drive_level=forced)`
  over N steps with a fixed `z_world_forced` direction.
- **Acceptance (all must hold):**
  - A0.1 `effective_benefit` crosses `benefit_threshold` for the forced benefit+drive
    (assert internal `effective_benefit > 0.1`).
  - A0.2 `goal_norm()` becomes >= 0.1 within <= 10 forced updates.
  - A0.3 z_goal direction stable: cosine(z_goal_t, z_world_forced) >= 0.9 once seeded.
  - A0.4 decay/floor: with benefit=0 thereafter, z_goal decays toward 0 at ~decay_goal rate;
    with `valence_wanting_floor=0.05`, norm does not drop below floor.
  - A0.5 OFF parity: `z_goal_enabled=False` -> z_goal stays 0 (bit-identical OFF).
- **Failure routing:** any failure = genuine substrate gate regression -> `/failure-autopsy`
  on `GoalState.update` (would contradict 622 S0 + 582a; high-priority).
- **claim_ids policy:** `[]` (diagnostic). Optionally anchors PROP-POSCTRL once it exists.
- **Manifest fields:** this is a **contract test** (`tests/contracts/`), not a queued EXQ. It
  emits pass/fail per assertion, not a manifest.
- **Class:** diagnostic / contract. **No new substrate code required.**

### Stage 1 -- forced benefit + known resource identity (object binding)
- **Purpose:** test L2/L4 -- does a benefit pulse tied to a *single known resource identity*
  produce an object-bound record and a z_goal that points to the object/cue/outcome
  representation (not just agent location)?
- **Method:** minimal env: 1 resource identity, no hazards, no reef complexity, fixed benefit
  pulse on contact. Drive the pipeline via the shared `update_z_goal`-driven runner. Two arms:
  - ARM_LOC (today's substrate): z_goal seeded from raw z_world at contact.
  - ARM_OBJ (proposed substrate, flag ON): z_goal seeded from the object token / z_resource.
- **Acceptance:**
  - A1.1 (both arms) z_goal_norm_peak >= 0.1 (positive control inherited from Stage 0).
  - A1.2 object-bound record written: after the agent leaves the resource cell, an
    object-keyed wanting record is retrievable and non-zero (ARM_OBJ).
  - A1.3 location-invariance: z_goal direction at two different contact *positions* with the
    same identity has cosine >= 0.8 in ARM_OBJ; ARM_LOC shows materially lower cosine
    (the discriminator).
- **Failure routing:**
  - A1.1 fails -> back to Stage 0 / harness (Class-1).
  - A1.2/A1.3 fail in ARM_OBJ but pass parity in ARM_LOC -> object-binding substrate not
    delivering; `/failure-autopsy` on the binding write-site (PROP-BIND-obj falsifier hit).
- **claim_ids policy:** `[]` while diagnostic; becomes evidence-bearing for PROP-BIND-obj /
  PROP-GOALPTR / MECH-230 amendment ONLY once the substrate is registered and the arm directly
  tests it.
- **Manifest fields:** `z_goal_norm_peak_per_seed`, `object_record_nonzero_fraction`,
  `z_goal_location_invariance_cosine` (ARM_OBJ vs ARM_LOC), `mean_episode_length`.
- **Class:** diagnostic (substrate-readiness for the object layer).

### Stage 2 -- cue-triggered pre-consummatory wanting
- **Purpose:** test L3/L6/L9 -- after one benefit encounter, re-presenting the cue (no benefit)
  raises *wanting* before consumption while *liking* stays tied to consumption.
- **Method:** Stage-1 env + a cue re-presentation event (present resource cue at distance,
  block consumption). Measure wanting amplitude and approach bias at cue onset vs a no-cue
  control.
- **Acceptance:**
  - A2.1 wanting (z_goal-driven goal_proximity along candidates, or token amplitude) rises at
    cue onset BEFORE any benefit pulse (delta vs no-cue control > 0 on >= 2/3 seeds).
  - A2.2 approach bias (E3 goal-score contribution / approach_commit_at_high_z_goal) increases
    at cue onset before consumption.
  - A2.3 liking (VALENCE_LIKING / benefit_eval) does NOT rise at cue onset (stays near 0 until
    consumption) -- the dissociation.
  - A2.4 (stretch) identity selectivity: with 2 identities, cue for X raises approach to X more
    than to Y (`wanting_liking_dissoc_fraction` / specific-PIT analogue > 0).
- **Failure routing:**
  - A2.1/A2.2 fail -> incentive-token recall path absent or starved (PROP-INCENT-token /
    PROP-CUEWANT falsifier); route to substrate amend.
  - A2.3 fails (liking also rises at cue) -> liking is leaking into the cue path; binding
    contaminates hedonic channel; autopsy.
- **claim_ids policy:** `[]` while substrate is provisional; evidence-bearing for
  PROP-INCENT-token / PROP-CUEWANT / MECH-117 retest only after registration + direct test.
- **Manifest fields:** `wanting_at_cue_onset_delta`, `approach_at_cue_onset_delta`,
  `liking_at_cue_onset`, `wanting_liking_dissoc_fraction`, per-seed arrays.
- **Class:** diagnostic, becomes evidence-bearing post-registration.

### Stage 3 -- consumer readout
- **Purpose:** test L7 -- does a non-zero z_goal/wanted signal reach dACC/E3/commitment and
  change behaviour? (Directly addresses the wiring-map finding that dACC does not read z_goal.)
- **Method:** Stage-1/2 env, hold z_goal non-zero (seeded or injected via `z_goal_inject`),
  consumer-enabled vs consumer-ablated arms; keep env simple.
- **Acceptance:**
  - A3.1 consumer receives non-zero goal/wanting input (instrument the consumer's input, not
    just its output) on >= 2/3 seeds.
  - A3.2 behaviour differs consumer-on vs ablated under matched z_goal (approach selectivity or
    commitment delta beyond noise).
- **Failure routing:** A3.1 passes but A3.2 fails -> consumer reads but does not act on it;
  this is the 626 interpretation-grid row "non-trivial z_goal does not reach dACC" -> autopsy
  on E3 score_bias composition + dACC sub-weights + PROP-CONSUME falsifier.
- **claim_ids policy:** `[]` diagnostic; evidence for PROP-CONSUME post-registration.
- **Manifest fields:** `consumer_input_nonzero_fraction`, `behaviour_delta_consumer_on_vs_off`,
  `approach_selectivity`.
- **Class:** diagnostic.

### Stage 4 -- ecological reintroduction (LAST, gated)
- **Purpose:** only after Stages 0-3 pass, re-introduce ecological complexity in order:
  (a) drive anneal, (b) hazards, (c) writer-freeze / developmental-window, (d) behavioural
  diversity (603d successors).
- **Acceptance:** this is where the ORIGINAL 626 question (which axis collapses a *formed*
  z_goal) becomes answerable. Re-use 626's C2/C3/C4 axis-dissociation design, but now with a
  guaranteed non-zero control (Stage 0/1 positive control wired into the harness).
- **Failure routing:** per 626 interpretation grid (drive-anneal vs hazard vs writer-freeze).
- **claim_ids policy:** `[]` for the axis diagnostic; the downstream behavioural validation
  (MECH-229 non-degenerate) is the evidence-bearing successor, gated on GAP-2 SP-CEM.
- **Class:** diagnostic (axis) -> evidence (behavioural validation).

**Ladder gate rule:** do not advance a stage until the prior stage's acceptance holds. Stage 4
is explicitly NOT the next step.

---

## Deliverable F: implementation plan (smallest patch set for Stage 0-2)

Ordered smallest-first. Each item lists files, contracts, OFF-parity guarantee, rollback.

### F0. Stage-0 contract test (NO substrate change) -- DO FIRST
- **File:** `ree-v3/tests/contracts/test_goalstate_forced_seed_positive_control.py` (new).
- **Change:** assertions A0.1-A0.5 against `GoalState` directly. No production code touched.
- **OFF-parity:** N/A (test-only).
- **Rollback:** delete the test.
- **Why first:** institutionalises the positive control that 626 lacked; zero risk.

### F1. Harness fix for 626 -> 626a (NO substrate change)
- **File:** new experiment script via `/queue-experiment` (e.g.
  `v3_exq_626a_goal_pipeline_developmental_window_diagnostic.py`), OR extend the 622
  `GoalStreamStagesRunner` with per-phase drive_floor/HFA/writer-freeze mutation.
- **Change:** add `agent.update_z_goal(benefit_exposure=benefit, drive_level=drive)` (and, if
  testing liking dissociation, `update_liking`) into the per-step loop, after `env.step`,
  reading `benefit_exposure` from `obs_dict`/`body_state[11]` and `drive` from
  `compute_drive_level`. Add a P0 positive-control assertion: ARM_A `z_goal_norm_peak >= 0.1`
  on >= 2/3 seeds before trusting any axis criterion.
- **OFF-parity:** N/A (experiment script).
- **Rollback:** none needed; 626a supersedes 626.
- **Authoring path:** `/queue-experiment` (mandatory for experiment scripts).

### F2. Object-bound incentive token -- substrate nucleus (Stage 1-2), flag-gated
Smallest coherent substrate change for L2/L3/L4. Authored via `/implement-substrate`.
- **Files:**
  - `ree-v3/ree_core/goal.py`: extend `GoalConfig` with
    `use_incentive_object_binding: bool = False` (default OFF, bit-identical). Add an optional
    `object_id: Optional[Hashable] = None` and `z_object: Optional[Tensor] = None` to
    `GoalState.update(...)`. When binding ON and benefit fires: store/refresh a per-object
    record `{object_id: (token_amplitude, z_object_or_z_resource)}` with slow decay; write
    z_goal from `z_object` (the pointer) instead of raw z_world. When OFF or `object_id is
    None`: **exactly today's behaviour**.
  - `ree_core/agent.py` `update_z_goal(...)`: pass through `object_id` / `z_object` from the
    env info (SD-049 `info["sd049_resource_type_at_agent"]` / consumed-type tag) and the
    z_resource encoder output, gated by the same flag.
  - `ree_core/utils/config.py`: `from_dims` passthrough for `use_incentive_object_binding`.
- **New method (Stage-2 recall):** `GoalState.recall_cue(object_id, drive_level)` -> raises
  wanting amplitude from the stored token * `(1 + drive_weight * drive)` WITHOUT a benefit
  pulse (lit A4 Zhang 2009 kappa-at-recall). Flag-gated; no-op when binding OFF.
- **Contracts:** `tests/contracts/test_incentive_object_binding.py`:
  - C1 OFF parity: with flag OFF, `update` produces bit-identical z_goal to current code
    (regression-lock against a saved fixture).
  - C2 binding: with flag ON + object_id, a per-object record is created and retrievable.
  - C3 location-invariance: z_goal from z_object is position-independent (A1.3).
  - C4 recall: `recall_cue` raises wanting from stored token without benefit; zero if no
    stored token.
  - C5 decay/floor unaffected.
- **OFF-parity guarantee:** master flag default False; all new args default None. Full
  contract + preflight suite must be green with flag OFF (bit-identical), per the GAP-1/GAP-3
  landing precedent.
- **Rollback:** flag default False already disables it; hard rollback = revert the goal.py /
  agent.py / config.py commit. No data migration (per-object store is in-memory episode state).
- **Gate:** do NOT author F2 until F0 + F1 (626a) confirm Class-1 vs Class-2 separation and
  Stage-1 ARM_LOC vs ARM_OBJ is well-posed. F2 is the architectural investment the ladder
  gates.

### F3 (deferred, NOT now): consumer-readout wiring (L7) + amygdala cue binding
- Only after Stage 3 shows a consumer-reading gap. Touches dACC/E3 score composition and the
  amygdala `cue_features` stub. Explicitly out of the Stage 0-2 minimal patch set.

**Net minimal patch set for Stage 0-2:** F0 (test) + F1 (harness/626a) now; F2 (flag-gated
object token) only after F0/F1 confirm the diagnosis. No broad refactor of goal.py.

---

## Deliverable G: queue proposal

Conventions: highest existing EXQ number is 626 (queue currently holds V3-EXQ-592e,
V3-EXQ-624). Lettered iteration for the harness fix (same scientific question, wrong
implementation -> append letter). New numbers for new questions. **These are proposals;
actual queueing and ID allocation go through `/queue-experiment` at write time (check max ID
then).**

| Proposed ID | Name | Purpose | claim_ids | experiment_purpose | supersedes | est. runtime | Gate |
|---|---|---|---|---|---|---|---|
| (contract, not EXQ) | `test_goalstate_forced_seed_positive_control` | Stage 0 unit positive control | n/a | contract | n/a | seconds | none -- do first |
| **V3-EXQ-626a** | goal_pipeline developmental-window diagnostic, harness-fixed | Re-run 626 WITH `update_z_goal` driven + P0 positive-control assert; recover ARM_A formation; only then read axis criteria | `[]` | diagnostic | **V3-EXQ-626** | ~ same as 626 (4 arms x 3 seeds x 90 ep) | F0 passed |
| **V3-EXQ-627** | object-binding Stage-1 (ARM_LOC vs ARM_OBJ) | L2/L4: does object-pointer seeding give location-invariant, identity-bound z_goal vs raw z_world? | `[]` (diagnostic) | diagnostic | null | ~2 arms x 3 seeds, simple env, short | F2 substrate landed (flag) |
| **V3-EXQ-628** | cue-triggered wanting Stage-2 | L3/L6/L9: cue re-presentation raises wanting+approach before benefit; liking stays consummatory; identity selectivity | `[]` (diagnostic) | diagnostic | null | ~3 seeds, cue-recall env | V3-EXQ-627 ARM_OBJ passes |
| **V3-EXQ-629** | consumer-readout Stage-3 | L7: does non-zero z_goal reach dACC/E3 and change behaviour (on vs ablated)? | `[]` (diagnostic) | diagnostic | null | ~2 arms x 3 seeds | Stage 2 passes |
| (later) V3-EXQ-514-successor | MECH-229 non-degenerate wanting/liking dissociation | evidence-bearing behavioural validation on object-bound substrate | `["MECH-229","MECH-230","SD-049","SD-015","MECH-117"]` | evidence | (514k superseded note) | Stage 0-3 pass + GAP-2 SP-CEM in main path |

**Queue policy notes:**
- 626a uses `supersedes: V3-EXQ-626` in both the queue entry and the manifest; the 626
  manifest stays as-is with `evidence_direction: non_contributory` (diagnostic, claim_ids=[]).
  Do NOT erase 626 -- it is the documented harness-bug incident.
- 627/628/629 are diagnostic (`claim_ids=[]`) so they cannot directly update claim support, per
  the CLAIM_IDS accuracy rule. Only the 514-successor carries claim_ids, and only after the
  object-bound substrate exists and the monostrategy confound is removed.
- Do NOT queue 627+ until F2 lands behind its flag and its contracts are green.

---

## Sequencing summary (smallest next coherent steps)

1. **Now:** F0 Stage-0 contract test (zero risk) + author **V3-EXQ-626a** via `/queue-experiment`
   (harness fix). This recovers the positive control and adjudicates Class-1 vs Class-2.
2. **If 626a recovers ARM_A formation** (expected, given 622 S0): the "626 formation failure"
   is closed as a harness bug; the real open question is the object-binding gap (514k).
3. **Then:** `/implement-substrate` F2 (flag-gated object token) + contracts; queue
   V3-EXQ-627 (Stage 1).
4. **Gate everything else** (Stage 2-4, 514-successor) on those outcomes. Stage 4 ecological
   tests are LAST.
