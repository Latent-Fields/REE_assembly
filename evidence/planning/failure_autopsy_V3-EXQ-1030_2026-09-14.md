# Failure autopsy (diagnostic adjudication) -- V3-EXQ-1030, waypoint_field_consumer_reach H2

- **Status:** `confirmed` -- Step 8 gate held with the user 2026-09-16 (account-handover walkthrough session; recorded 2026-09-16T12:22:00Z; Opus red-team CONTESTED, findings applied first). See "Step 8 gate outcome" at the end. Originally staged headless: Status: `awaiting_human_confirmation` -- STAGING-MODE DRAFT, headless. Routing is NOT finalised; the Step 8 interactive gate is OWED. ...
- **Generated (UTC):** 2026-09-14T23:46:07Z
- **Session:** `autopsy-staging-trio-20260914` (dispatched by metaworker orchestrator `orchestrate-20260914-2323`)
- **Scope:** single
- **Target:** `v3_exq_1030_mech428_inv086_waypoint_field_zworld_decodability_20260914T125657Z_v3` (queue_id `V3-EXQ-1030`)
- **Trigger:** BOTH -- a FAIL, and `experiment_purpose: diagnostic`.
- **Dry-run gate:** `check_dry_run_citations.py` on the target run_id and `V3-EXQ-1030`: `0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown`. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- **Step 9b:** the registry was **NOT** written (staging mode). The intended append is recorded under `hypothesis_space_ledger_pending` in the JSON.

---

## 1. Facts (no interpretation)

### 1a. What the run is

V3-EXQ-1030 is the **H2 leg** (`axis: representation`, `hid: H-wpfield-zworld-interface`) of the two-leg GOV-FANOUT-1 portfolio opened by the confirmed `failure_autopsy_V3-EXQ-1004_2026-09-05`, registered in `hypothesis_space_registry.v1.json` under `qid: waypoint_field_consumer_reach`. The sibling H1 leg (`axis: drive`) is V3-EXQ-1039.

The question the leg poses, verbatim from the registry: V3-EXQ-1004 showed the SD-WAYPOINT-FIELD observable makes the pending waypoint's direction decodable and behaviourally sufficient **for a supervised reader over the raw observation** (0.575 -> 0.841 imitation accuracy). Does that same directional signal survive REE's own `observation -> z_world` compression, or is it lost before E1/E2/E3 ever see it?

**Declared null (pre-registered):** the z_world accuracy lift (ON minus OFF) is indistinguishable from zero *while the raw-observation lift is large* -- which would locate the residual navigation blockage at the encoder rather than at the environment. Meeting the null **supports** H2.

### 1b. Design

Two arms (`field_off` / `field_on`) x 5 seeds (42-46). Per (seed, arm) cell: SD-070 P0a warmup of the world encoder on a dedicated env (200 episodes, resource-proximity target, generic -- never tasked on waypoints); freeze the whole latent stack; roll out a **uniform-random** policy on a second dedicated env for 40 episodes x 150 steps; fit single-layer linear probes (cross-entropy, **episode-level** 80/20 split) for the oracle 5-way waypoint direction from (i) `z_world` via `agent.sense()` -- the DV, (ii) the narrow 25/50-dim raw slice -- the C0 positive control, (iii) `split_encoder.world_encoder(raw world_state)` directly -- the F5a diagnostic, and (iv) the agent's absolute grid quadrant from `z_world` -- the R3 readiness control.

The driver carries a six-finding cross-model red-team block (F1-F6, all applied). `_FieldMaskedEnv` (F2) always builds the wide field-enabled env and zeroes the trailing 25 `world_state` columns under OFF, so both arms are byte-identical at init and differ only in field CONTENT.

### 1c. What the manifest reports

| Readout | OFF | ON | lift |
|---|---|---|---|
| raw probe (C0) | 0.3606 | 0.6612 | **+0.3006** |
| z_world probe (DV / C1) | 0.3832 | 0.4023 | **+0.0191** |
| z_world direct probe (F5a diag) | 0.4838 | 0.5086 | +0.0249 |
| quadrant probe (R3) | 0.5513 | 0.5555 | +0.0042 |

**Criteria as emitted:**

- `C0_raw_positive_control`: **met**, `measured 1.0` vs `threshold 0.6`; per-seed raw lift 0.2139-0.4239 (42: 0.2851, 43: 0.2139, 44: 0.4239, 45: 0.2675, 46: 0.3128), all five clearing the 0.15 floor.
- `C1_zworld_lift_null` (load-bearing): **`met: false`**, but its own cells read `measured: 0.8`, `threshold: 0.6`, `n_seeds_met: 4`, `required_seeds: 3`. Per-seed z_world lift: 42 `-0.0305`, 43 `-0.0155`, 44 `+0.1201`, 45 `-0.0204`, 46 `+0.0420`; four of five inside the +/-0.05 null band.

**Readiness / preconditions as emitted:**

| Precondition | measured | threshold | met |
|---|---|---|---|
| R1 `raw_observation_decodability_replicated` | 1.0 | 0.6 | yes |
| R2 `zworld_encoder_trained_all_cells` | 1.0 | 1.0 | yes |
| R3 `zworld_probe_extracts_known_signal` | **0.4** | 0.6 | **no** |

`interpretation.label: substrate_not_ready_requeue`; `measurable: false`; `unmet_preconditions: ["zworld_probe_extracts_known_signal"]`. `outcome: FAIL`. `non_degenerate: true`, `degenerate_metrics: {}`.

`evidence_direction: non_contributory` and `evidence_direction_per_claim: {INV-086: non_contributory, MECH-428: non_contributory}` are emitted **unconditionally**, with a note saying so -- the driver carries the claim tags as read-across only, exactly as the 1004 autopsy instructed. (This is a direct fix of the `claim_directions` dead-letter that the 1004 autopsy recorded; the correct field is now emitted.)

### 1d. Recording provenance

`validate_recording.py`: 1 manifest, **1 always-core gap -- `elapsed_seconds` missing**. Everything else present: `recording_schema: rec/v1`, `substrate_hash 85adf63e...`, `substrate_commit 3d92cd2d` (`dirty: true`, one path `experiments/_lib/baselines/arc019_curriculum_gating.py`, not on this driver's code path), `substrate_stable_across_run: true`, `substrate_identity`, full `config`, explicit `seeds`, `machine: ree-cloud-4`, `machine_class: linux-x86_64-py3.10-torch2.12.0+cpu`.

### 1e. Expected vs observed

**Expected** (if the design worked): either the z_world lift comes in near zero while raw is large (PASS, H2 supported) or it tracks the raw lift (FAIL, H2 refuted, blockage is elsewhere). **Observed:** the z_world lift *is* near zero and raw *is* large -- superficially the PASS branch -- but the run self-routed FAIL because the readiness control that exists to certify the probe can read z_world at all came in at 4/10 cells against a 6/10 bar.

**Which criterion failed: none, scientifically.** C1 was **suppressed**, not missed. `_score` computes `c1 = measurable and (len(null_seeds) >= need)` (driver line 719), and `measurable` is false when any readiness check fails -- so the load-bearing flag reads `false` while the criterion's own reported cells read met (0.8 >= 0.6; 4 >= 3).

---

## 2. Claim-layer mapping

| Claim | type | status | epistemic_category | Read |
|---|---|---|---|---|
| INV-086 | invariant (emergent) | candidate | standard | **not exercised** |
| MECH-428 | mechanism | candidate | standard | **not exercised** |

INV-086's `what_would_answer` requires a regime where MECH-116 working-memory maintenance has measurably decayed, with all intermediate feedback channels (MECH-216/217 proxy-wanting, MECH-426 progress-velocity, MECH-427 subgoal-credit) ablated and singly restored. MECH-428's requires a seeding-sparse regime with `z_goal_norm` measured against a 626b-style forced-seed control.

This run instantiates **no REE agent acting toward a reward, no z_goal, no GoalState, no feedback channel, and a frozen latent stack**. The learners are single-layer linear probes over frozen features and a uniform-random rollout. Neither regime is touched, and the driver says so in its own docstring and in the manifest's `evidence_direction_note`. Claim-id accuracy is therefore **correct-but-peripheral**: the tags are inherited read-across labels from the portfolio's parent, honestly declared as such. No claim-layer field moves on this run.

---

## 3. Biological-reference triage

**Closest reference mechanism:** thalamocortical / early sensory-cortical compression preserving behaviourally-relevant spatial gradients into the representations downstream evaluative and motor systems read.

**Faithful translation or formal import?** Faithful in kind -- this is not a Pearl/Shannon/optimal-control import; it is a bottleneck-capacity question about a real encoder.

**The biologically load-bearing observation:** in real brains a sensory bottleneck's content is shaped by *what the organism is trained to act on*. Here the bottleneck (`split_encoder.world_encoder`) is trained by a **generic** anti-collapse recipe (SD-070 P0a, resource-proximity target) and is *never* tasked on waypoints. Asking whether an untasked gradient survived an untasked bottleneck is asking a question whose biological answer is "probably not, and that is not a defect". So even once the instrument is repaired, **a clean H2 null would be weaker evidence for an interface DEFECT than the leg's framing assumes** -- it may simply be the reference mechanism behaving correctly. The leg's framing should be tightened accordingly at re-queue; this is a *narrowing*, not a refutation.

`lit_status: partial` -- no `targeted_review_` entry for encoder-bottleneck gradient preservation, but the mechanism is not a formal import, so a `/lit-pull` commission is not the primary output here.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not exercised** | read-across co-tags only; declared unconditionally by the driver |
| Biological reference | **partial** | faithful in kind; the untasked-bottleneck caveat above narrows H2's framing |
| Dependency prerequisites | **present** | SD-WAYPOINT-FIELD validated (1004); SD-070 P0a ran; R2 encoder-moved 10/10 |
| Implementation completeness | **partial** | the *driver's readiness instrument* is defective; the substrate under test is intact |
| Environment adequacy | **adequate** | paired `_FieldMaskedEnv` design confirmed working end-to-end (see 5c) |
| Measurement adequacy | **under-instrumented** | **the dominant layer** -- two independent defects, sections 5a and 5b |
| Integration adequacy | **isolated** | by design; latent stack frozen, no consumer exercised |
| Scale / capacity | **likely insufficient (probe), adequate (substrate)** | ~8 held-out episodes/cell; 150 Adam steps on unstandardised 32-dim EMA features |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Reads from | Established? |
|---|---|---|
| MECHANISM FAILED | Implementation completeness = `partial` | **not established** |
| MEASURES FAILED | Measurement adequacy = `under-instrumented` | **not established** |
| ENVIRONMENT FAILED | Environment adequacy = `adequate` | **established** |
| REE FAILED | all three | **false** |

**Net classification: MEASURES -- single-bucket, NOT chargeable to REE.** The measurement apparatus is inadequate, so the mechanism bucket cannot be reached and nothing here licenses any organism-level or claim-level failure read. The environment row reads `adequate`, which under the skill's own table establishes only that the environment is *not* the excuse -- it does not add to a REE read while the other two are unestablished.

---

## 5. The diagnosis

### 5a. R3's threshold FORM suppressed C1; its TARGET is present but layout-bound -- the 'not in the feature space' argument below is WITHDRAWN [CORRECTED at the 2026-09-16 cross-model red-team pass (Opus), F1]; 5b is now the load-bearing basis

R3 decodes the agent's **absolute grid quadrant** out of `z_world`, on the driver's stated premise (`_quadrant_label` docstring) that the target is *"structurally present in `world_state` regardless of the waypoint field (agent position is reflected in the local view), so it must be decodable from z_world if the probe pipeline can extract anything at this scale at all."*

**That premise is false, and the environment source says so verbatim.** `CausalGridWorldV2._get_observation_dict` puts `agent_x / size` and `agent_y / size` in **`body_state[0]` and `body_state[1]`**. `world_state` is composed exclusively of **agent-centred 5x5 windows**: `local_view` (5x5x7 = 175), `contamination_view` (25), `hazard_field_view` (25), `resource_field_view` (25), `waypoint_proximity_field_view` (25) = 275. And `z_world` is computed from `world_state` alone (`split_encoder.world_encoder(world_state)`; the driver's own `_direct_zworld` confirms the path).

Absolute position is reachable from `world_state` only via:
- **(a) the out-of-bounds wall pattern** when the agent is within 2 cells of a wall -- the local view marks out-of-bounds cells with a one-hot `wall` entity channel (not, as an earlier draft of this section said, with zero padding; the mechanism is corrected, the conclusion is unchanged). The env is non-toroidal by default -- but on a 12x12 grid the interior 8x8 (about **44% of cells**) sees no wall at all, and the cue that does exist names an *edge*, not a quadrant.
- **(b) episode-specific hazard/resource layout** carried by the proximity-field windows -- which an **episode-level** train/test split (F4, correctly applied) deliberately makes non-generalising.

So R3 tests a signal that is weakly, non-uniformly and partly non-generalisably present -- not one that "must be decodable". **The manifest carries the fingerprint:**

- quadrant **TRAIN** accuracy is **0.521-0.612 in all 10 cells** -- the probe cannot fit the supposedly-present signal even on its own training data;
- on seed 43 the quadrant **test** accuracy (0.762) **exceeds train** (0.521) by 0.24, and on seed 43 OFF the test majority-class rate is 0.495 -- a statistic driven by which 8 episodes landed in the test split, not by competence.

**Consequence:** R3's failure does not establish that the probe pipeline is blind, and R3's success would not have established that it works. It could not certify probe competence in either direction, so the `substrate_not_ready_requeue` self-route reached the right conclusion ("do not read this run") through a control that was not entitled to deliver it.

### 5b. The trap: invalidating R3 does NOT flip the verdict to "C1 met, H2 supported"

The tempting next step is to discard R3, read C1's own cells (4/5 seeds inside the null band, required 3), and declare H2 supported. **That is wrong**, because removing the guard does not remove the hazard it was built for. The driver's own red-team F1 named the failure mode exactly: *an under-fit or scale-starved z_world probe reads OFF ~ ON ~ majority-class in both arms, which satisfies C1's null BY CONSTRUCTION regardless of what z_world actually encodes.*

**That hazard is realised in this manifest.** The z_world probe's held-out accuracy sits **at or below its own test majority-class rate in 6 of 10 cells**:

| cell | z_world acc | test majority | margin |
|---|---|---|---|
| 44 OFF | 0.2297 | 0.4982 | **-0.269** |
| 44 ON | 0.3498 | 0.4982 | **-0.148** |
| 46 OFF | 0.4161 | 0.5175 | **-0.101** |
| 45 ON | 0.3810 | 0.4626 | **-0.082** |
| 45 OFF | 0.4014 | 0.4626 | **-0.061** |
| 46 ON | 0.4580 | 0.5175 | **-0.059** |
| 43 ON | 0.3990 | 0.3782 | +0.021 |
| 43 OFF | 0.4145 | 0.3782 | +0.036 |
| 42 ON | 0.4238 | 0.2835 | +0.140 |
| 42 OFF | 0.4543 | 0.2835 | +0.171 |

A near-zero difference between two sub-majority numbers is not a measured null. **The run is genuinely uninterpretable -- the driver's verdict is right, its stated reason is not.**

### 5c. The fitting budget is not scale-matched across the spaces it is compared over

All four probes share `PROBE_STEPS = 150` full-batch Adam steps at `PROBE_LR = 5e-3` on **unstandardised** features -- but the raw probe reads a 25/50-dim slice bounded in [0,1] while the z_world probes read a 32-dim 0.9-EMA latent whose scale is set by `world_precision_logit` and whatever P0a left behind. The consequence is visible in the train-accuracy column:

| probe | train acc range (10 cells) |
|---|---|
| raw (ON arm only) | **0.743 - 0.828** |
| z_world via `sense()` (the DV) | **0.487 - 0.576** |
| z_world direct (diagnostic) | 0.539 - 0.692 |
| quadrant (R3) | 0.521 - 0.612 |

(The band is quoted per probe, not as one "z_world-path" range: the direct path fits materially better than the sense() path, which is itself the finding in 5e.)

A comparison whose positive control is fit to 0.83 and whose DV is fit to 0.52 is not controlled for fitting adequacy, whatever it reports.

### 5d. What the design got RIGHT, and should keep

The `_FieldMaskedEnv` pairing (red-team F2) worked end to end, and the manifest proves it: `label_counts` is byte-identical across arms within every seed (e.g. seed 42: 359/289/269/223/0 in both), `world_obs_dim` is 275 in both arms, and `field_cols_weight_delta` is **exactly 0.0 in all five OFF cells** -- a masked-to-zero input column receives exactly zero gradient -- against 2.018-2.160 in all five ON cells. The ON/OFF contrast is genuinely paired at the trajectory level. Keep this.

(Per-column reading of the ON deltas, recorded but **not** load-bearing: the 25 field columns move with norm ~2.09 against ~11.0 for the other 250 -- about 0.19 of the other block's norm where an iid per-column expectation gives sqrt(25/250) ~ 0.32. Suggestive that P0a moves the field columns *less* than the rest, consistent with an untasked channel. A norm ratio is not a per-column effect size and must not be read as a measurement.)

### 5e. First quantified cost of the SD-070 `agent.sense()` pre-projection (F5a)

`agent.sense()` feeds `world_state` through `agent.world_obs_encoder` -- a separately-initialised Linear+ReLU that **nothing in the corpus ever trains** -- before `split_encoder.world_encoder`, which is what P0a actually trains, on *raw* `world_state`. The driver added `zworld_direct_probe` to disambiguate the two loss sites, and it delivers:

the direct probe beats the sense()-path probe on the **identical label, identical episode split, identical fitting budget and identical frozen encoder** in **8 of 10 cells** -- mean **0.4838 vs 0.3832 (OFF, +0.101)** and **0.5086 vs 0.4023 (ON, +0.106)**.

This is a paired within-cell contrast and is the strongest evidence yet that the untrained pre-projection destroys real information before the trained encoder sees it, on the pathway every production consumer (E1/E2/E3) reads. **Two caveats keep it from being a verdict:** the direct path has no known-signal anchor of its own in this run either, and *both* paths show a near-null ON-OFF lift (direct-path per-seed lifts -0.003, +0.044, +0.072, 0.000, +0.012). It locates an absolute information loss, not the specific loss of the waypoint gradient.

### 5f. `p0a_holdout` is not a substitute positive control, though it looks like one

Across all 40 (cell x head) readings `p0a_holdout` reports balanced accuracies of **0.9869-1.0000** with `mean_lift ~0.58` on hazard_present / resource_present / hazard_distance / resource_distance. It is tempting to cite this as proof that z_world is richly informative and therefore that the probe must be the limiter. **It cannot carry that weight:** `ZWorldP0Trainer._holdout_report` splits with a flat `torch.randperm` over samples, **not by episode**, so it is exposed to precisely the within-episode near-duplicate leakage that F4 made this driver's own probes split by episode to avoid; and it reads `_z_world_path` (the direct path) through the *trainer's own* heads, not the sense() features the DV uses. Its label balance also makes the raw number flattering (see 7, change 1). What it does establish is narrower and still useful: **the z_world path is not collapsed or degenerate.**

### 5g. A precondition gate can make a criterion's cells read "met" while its flag reads false

`criteria.C1_zworld_lift_null` reads `met: false` beside `measured: 0.8 / threshold: 0.6 / n_seeds_met: 4 / required_seeds: 3`, because `_score` folds the readiness gate into the criterion boolean while computing the criterion's reported cells independently of it. Any downstream reader comparing measured against threshold gets the opposite answer from the flag. Cheap, generalisable repair: emit `suppressed_by: <precondition name>` on the criterion block rather than only flipping `met`.

---

## 6. Cluster pattern

Not a cluster. Single target. No un-autopsied sibling shares this failure shape this tick.

---

## 7. Learning extracted and repair pathway

**Work-graph debt class: `complicated (buildable)`.** The repair is a named build with no open question. No fact is missing and no frame is wrong, so this is *not* a probe-gated spike; it is a driver fix. That classification is what makes an **alphabetic** re-queue the right instrument: the scientific question is unchanged, only the implementation of its readiness apparatus was wrong.

**Routing override, stated explicitly** (Step 7c red-team F4): the skill's work-graph list maps `complicated (buildable)` to the missing/immature-substrate row (`/implement-substrate`). That mapping is **not** followed for the primary routing, deliberately -- the skill's own Step 7 routing *table* sends a "measurement / environment / test-design gap" to `/queue-experiment`, and the buildable work on the critical path is a **driver instrument**, not substrate. The substrate half of this autopsy **is** routed to `/implement-substrate`, via the `create` entry in section 7b below. The two routes are complementary, not in conflict.

**Primary routing: `/queue-experiment` -> `V3-EXQ-1030a`** (same-question implementation fix).

Required changes:

1. **Replace R3's target AND its threshold form** -- both halves are required. *(a) Target:* a label genuinely present in `world_state` and generalising across episodes -- the natural family is the SD-018/SD-070 P0a scene-structure targets (`hazard_present` / `resource_present` / `hazard_distance` / `resource_distance` via `scene_structure_targets`), carried by the hazard/resource field windows by construction and the very content P0a optimises. *(b) Threshold:* it must be **majority-relative, never an absolute floor**. Those labels are severely imbalanced and this run's own manifest proves it -- `p0a_grounding_label_balance` reads `hazard_distance [0.0, 0.078, 0.197, 0.725]` and `resource_distance [0.0, 0.115, 0.241, 0.645]`, bucket 0 carrying **exactly zero** mass in both. A constant-majority predictor therefore scores 0.725 / 0.645 and would clear a 0.55-style absolute floor in **every** cell without decoding anything -- an unfailable positive control by construction, the same defect class as the R3 being replaced, merely inverted (R3 could never pass; this would never fail). **This was caught by the Step 7c red-team against the first draft of this very recommendation, not by the 7b mechanical checks, which have no view of label balance.** Keep the quadrant probe as a non-load-bearing diagnostic if desired; it must not gate anything.
2. **Measure R3 through the same pipeline as the DV** -- same sense()-path features, same episode-level split, same fitting budget, same seeds. This is exactly why the existing `p0a_holdout` cannot stand in for it (5f).
3. **Scale-match the fitting** -- standardise features per probe (or fit to convergence with per-space early stopping) and report each probe's train accuracy as a first-class readiness number beside its held-out accuracy.
4. **Add a DV-floor readiness check** -- require the z_world probe to clear *its own* test majority-class rate by a declared margin in a declared fraction of cells *before* the ON-OFF null is read at all. This is the check that would have caught the realised F1 hazard directly rather than by proxy, and its absence is why the run had to lean on the mis-specified R3.
5. **Decide and declare the status of the direct path up front** (Step 7c red-team F3). The sense()-path DV is the right primary readout -- it is the pathway production consumers read. But on the **direct** path, seeds 42, 43 and 46 clear their own majority-class rate in *both* arms with ON-OFF lifts of -0.003, +0.044 and +0.012 -- so a DV-floor check like [4] would be satisfied there at 3 of 5 seeds, and C1's null would then be met at 3/3 of the qualifying seeds. That is **not** a verdict on this run (the direct path has no known-signal anchor here either, and the pre-registered DV is the sense() path), but 1030a must state beforehand whether the direct path is **co-primary with its own criterion** or stays a diagnostic. Deciding that after seeing the numbers is the thing to avoid.
6. **Emit suppression explicitly** -- `suppressed_by` on a criterion a precondition kills (5g).
7. **Stamp `elapsed_seconds`** via `stamp_recording_core` (Experimental Recording Standard 2026-07-12 section 3b). Recording-debt, not measurement-debt: fix in the successor, never by re-running. It recurred across two consecutive drivers in this lineage (1004 and 1030), which suggests the gap is in the shared emit path, not in either author.

**Explicitly NOT recommended:**

- Do **not** re-queue this as a MECH-428 or INV-086 test -- the run is claim-free in substance.
- Do **not** open a new EXQ number -- the scientific question is unchanged.
- Do **not** propose **V3-EXQ-1039** (the H1 sibling leg; driver `ree-v3/experiments/v3_exq_1039_mech428_inv086_waypoint_field_consumer_drive_signal.py` already exists on disk and the entry is already queued as of 2026-09-14, not yet scored) or **V3-EXQ-884b** (MECH-428's C1 redesign, being built by another live session as of 2026-09-14). Both are **in flight with live owners**.
- Do **not** read this run as evidence for or against H2. **The leg stays alive.**

**No `fanout_recommendation` is emitted, deliberately.** The existing two-leg portfolio is unchanged and correct; the H2 leg simply has not been resolved. Growing an already-registered question's denominator here would be exactly the padding the frozen-set invariants exist to prevent.

### 7b. Substrate routing -- `create` (flipped from `none` by the red-team)

The first draft set `recommended_substrate_queue_entry.action: none`, on the rationale that the `agent.sense()` pre-projection gap was "already recorded by the 1004 autopsy" and that a `create` would duplicate it. **Both halves of that rationale are false**, and the Step 7c red-team caught it with a cheap confirmer: `grep -c world_obs_encoder` returns **0** on both `failure_autopsy_V3-EXQ-1004_2026-09-05.md` and `.json`, and **0** on `evidence/planning/substrate_queue.json`. The finding originates in the **V3-EXQ-1030 driver's own red-team block (F5a)** -- this run's instrument, not a prior adjudication -- so nothing tracks it and there is nothing to duplicate.

A second false absolute in the same place, inherited from the driver's F5a prose: `world_obs_encoder` is **not** a layer "nothing in the corpus ever trains". 85 drivers under `ree-v3/experiments` build an optimiser over `agent.parameters()`, which includes it. The true, **lineage-scoped** claim is: **0 of the 34 drivers that call `run_zworld_p0` train it** (the only one of the 34 that even names it is this driver, in its red-team block), so within the SD-070 P0a lineage the training path (`_z_world_path`, raw `world_state`) and the inference path (`sense()`, via the pre-projection) diverge with nothing reconciling them.

So: **`action: create`**, `sd_id_suggested: SD-ZWORLD-SENSE-PATH-PARITY`, priority 2, with this run's paired +0.10 measurement as the initial `failure_record_entry`.

**`severity: degrading`, deliberately NOT `corrupting`** -- and the distinction is load-bearing because of blast radius. `corrupting` STOP-gates any new `/queue-experiment` whose driver touches `substrate_paths`, matched at *module* granularity -- and `ree_core/agent.py` is entered by essentially every REE driver, so a `corrupting` stamp here would gate the entire experiment programme, including this autopsy's own repair and the sibling H1 leg. That is the same asymmetry the confirmed 1004 autopsy reasoned through for `causal_grid_world.py`. On the merits `degrading` is also right: the pre-projection does not make a metric read as a clean null that is secretly invalid -- it uniformly *attenuates* decodability on the sense() path, and for a question about what the *production* path carries, measuring through the production path is correct rather than corrupting. What is defective is that the training and inference paths diverge.

Three existing entries already unblock these claims and **none** covers this gap or needs amending on this evidence: `waypoint-proximity-field-observable` (validated by 1004; this run re-confirms rather than reopens it), `SD-094` (satisfied -- `subgoal_arrival_position_check=True`, no policy trained toward reward), `SD-092` (not on this code path at all).

### Re-derive brake (MOVE-3)

**Does not fire.** R1-R3 recipe run 2026-09-14 over the confirmed corpus: **MECH-428 = 1 hit** (`failure_autopsy_V3-EXQ-884_2026-08-03`, run `v3_exq_884_...20260803T022131Z_v3`); **INV-086 = 0 hits**. Identical to the count 1004 recorded. This autopsy adds 0 -- its per-claim categories are declared `standard`, which the counter's per-claim short-circuit excludes. Below the threshold of 2, so no re-queue is refused; substantively correct, since MECH-428 has still never had a single non-precondition-unmet test and the re-queue recommended here is not a test of either claim.

### Granularity-debt recurrence trigger

**Does not fire.** `granularity_debt_cluster.py`, 2026-09-14:

- **MECH-428** -- 2 tagging targets across 2 files: `failure_autopsy_V3-EXQ-1004_2026-09-05` (non_contributory / standard / alignment free-text "not exercised") and `failure_autopsy_V3-EXQ-884_2026-08-03` (non_contributory / precondition_unmet / alignment "unclear"). Distribution: `other=1, unclear=1`.
- **INV-086** -- 1 tagging target (the 1004 one). Distribution: `other=1`.

**No target reads `weakened`** on either claim. The reader's caution about free-text alignment was discharged by reading both strings: the 1004 string says the claim was *not exercised* (the opposite of weakened), and the 884 string is a literal "unclear" attributing the failure to a substrate bug. Per the skill's own rule -- a cluster with no `weakened` target is measurement or implementation debt, not granularity debt -- the trigger does not fire. Nor do the signatures differ structurally: all three targets share one shape (claim not exercised / precondition unmet).

---

## 8. Draft `evidence_quality_note` for governance

> [2026-09-14, V3-EXQ-1030, FAIL(self-routed substrate_not_ready_requeue), diagnostic] H2 leg (representation axis) of the waypoint_field_consumer_reach fan-out opened by the confirmed failure_autopsy_V3-EXQ-1004_2026-09-05. READ-ACROSS ONLY for this claim, unconditionally and by the driver's own declaration -- no REE agent in subgoal-mode navigation, no z_goal, no feedback-channel ablation, no forced-seed control, so neither INV-086's nor MECH-428's what_would_answer regime is instantiated. The run is ALSO uninterpretable on its own DV: the load-bearing C1 null was suppressed by readiness R3, and R3's target (absolute grid quadrant) is PRESENT in world_state but LAYOUT-BOUND (wall channel + layout-relative field windows: raw world_state fits quadrant to train 0.91-0.94 on 5/5 seeds; on the same sense()-path z_world the quadrant probe clears its own test majority in 9 of 10 cells, mean +0.10, vs 4 of 10 for the DV), so R3 DID certify probe competence -- what failed was R3's ABSOLUTE threshold form, which a majority-relative threshold passes at margins up to 0.075, in which case C1 would have been read (4 null seeds >= 3) [CORRECTED at the 2026-09-16 cross-model red-team pass (Opus), F1 -- the draft's 'target not in the feature space' claim is withdrawn]. Independently, the z_world probe sits at or below its own test majority-class rate in 6 of 10 cells, so the near-zero ON-OFF lift is a difference between two floor-pinned numbers, not a measured null. H2 therefore remains ALIVE and unresolved. Nothing about either claim's status, confidence or retest state moves on this run.

---

## 9. Step 7b mechanical pre-routing checks

Run against the draft: **2 fires initially, both acted on, 0 after.**

- **C1** -- "driver for these claims already on disk, never scored, unmentioned": `v3_exq_1039_mech428_inv086_waypoint_field_consumer_drive_signal`. **Acted on**: the driver is now named verbatim in `in_flight_work_not_to_re_propose`. The honest disposition is that it is the *other leg of this same portfolio*, in flight with a live owner -- not a repair this autopsy should route.
- **C2** -- "`action: none` while 3 entries already unblock these claims, unmentioned": `SD-092`, `SD-094`, `waypoint-proximity-field-observable`. **Acted on**: all three are now named in the substrate-entry note with a per-entry reason none needs amending (see the JSON).

C5 and C7 reported `inapplicable`. Note the skill's rule: **`inapplicable` is not "no fire"**.

---

## 10. Step 9b -- frozen ledger (DRAFTED ONLY, staging mode)

`hypothesis_space_registry.v1.json` was **not written**. Growth-restriction check: `waypoint_field_consumer_reach` carries `growth_restriction: ""` (present but empty) -- **no STOP condition**, nothing to carry to the Step 8 gate. Recorded explicitly because an absent check is indistinguishable from a passed one.

Intended edit is **Mode B, and a deliberate NON-resolution**: `H-wpfield-zworld-interface` stays **`alive`**; record `resolving_runs: ["V3-EXQ-1030"]`, `control_passed: false`, `met_elimination_bar: false`, `resolved_utc: null`, and a `basis` string stating why the run did not discriminate. Per the Step 9b state-mapping table, a `non_contributory` run that does not discriminate leaves the leg alive.

**No denominator move.** `initial_frozen_count` stays 2, `initial_frozen_count_at_registration` stays 2, no hypothesis added or removed, no `fanout_growth_events` / `discovery_growth_events` entry owed. Also drafted: a `decision.observation_bottleneck` string -- *there is no validated readout that can certify, through the same pipeline and split as the DV, that a linear probe can extract any cross-episode-generalising signal from the sense()-path z_world at this scale* -- which is Dimension-4 content, not a leg.

Full block: `hypothesis_space_ledger_pending` in the JSON.

---

## 11. Step 7c red-team

**Verdict: CONTESTED.** Run on **Fable 5.1** while this drafting session runs on **Opus** -- so it is a **cross-model** pass. (The agent's own summary line self-described it as "same-model"; that self-description is wrong and is corrected here so the verdict is not later discounted.) Findings file: `redteam_1030.md` in the session scratchpad; full disposition in the JSON `red_team` block.

**Two verdict-moving findings, both applied:**

- **F1** -- the `action: none` substrate disposition rested on two false facts. Confirmer run, both confirmed. **Applied:** action flipped `none` -> `create` with an explicit `degrading`-not-`corrupting` rationale, the claim re-scoped to the 34-driver `run_zworld_p0` lineage, and the whole correction recorded in `provenance_correction` rather than swapped in silently (section 7b above).
- **F2** -- the drafted R3 replacement kept an **absolute** floor on labels whose own balance makes a constant-majority predictor clear it, i.e. it would have installed an unfailable positive control -- the mirror image of the defect being repaired. Confirmer run against this run's own `p0a_grounding_label_balance`, confirmed. **Applied:** required change 1 now demands a majority-relative threshold as an explicit second half (section 7 above).

**Three non-moving findings applied:** F3 (declare the direct path's status up front -> new required change 5), F4 (state the work-graph routing override -> section 7 preamble), F5 hygiene (p0a_holdout range corrected to 0.9869-1.0000; out-of-bounds cells corrected from "zero padding" to a one-hot `wall` channel; the train-accuracy band re-scoped to the sense() path specifically; the garbled raw-lift list corrected; V3-EXQ-1039 corrected from "being queued" to already queued).

**Verified sound and left standing:** the R3 mis-specification itself (independently reproduced, with no missed route to absolute position -- the red-team additionally checked that `_zone_map` is `None` and that layouts are re-randomised per reset); 6/10 cells at-or-below majority; 8/10 direct-path wins at +0.1006 / +0.1063; quadrant hits 4/10; the C1 suppression mechanism at driver line 719; the brake counts (MECH-428 = 1, INV-086 = 0) reproduced via the `validate_queue` predicate; the granularity trigger not firing; the `-> stamp this artifact` tails being parser-recognised and not-yet-true; the alphabetic 1030a instrument; and the Step 9b ledger block matching the skill's state-mapping table.

**The contest was entirely on RECOMMENDATIONS, not on the science** -- which is the measured pattern for this pass. Note the standing caution in both directions: a CONFIRMED verdict would not have proved the artifact clean, and this CONTESTED one does not impugn the diagnosis.

---

## 12. What is OWED before this can be applied

1. **The Step 8 interactive gate** -- this draft's routing is a proposal, not a decision.
2. **Nothing was marked reviewed**; `review_tracker.json`, `claims.yaml`, `substrate_queue.json`, the queue and the registry are all untouched by this session.
3. Per CLAUDE.md, this autopsy **does not `spawn_task` its own follow-on**. `/governance` chips V3-EXQ-1030a once Step 2b ratifies the routing.

## 13. Step 7c -- adversarial red-team pass, second (run 2026-09-16T12:19:13Z, model Opus, cross-model): VERDICT **CONTESTED**, seven findings applied

**F1 (assertion + required change):** the 5a claim that R3's quadrant target is not in `world_state` is false; raw `world_state` fits quadrant to train 0.91-0.94 on every seed and the quadrant probe on z_world clears its own test majority in 9 of 10 cells (mean +0.10, vs 4/10 for the DV). R3 is layout-bound, not absent; what failed is its absolute threshold, and the draft's own majority-relative fix applied to this run's data passes R3 at margins up to 0.075, after which C1 reads met (4 null seeds). The verdict does NOT flip: 5b's DV-floor argument stands alone now. `required_changes[0]` rewritten to keep R3's target. **F2:** the sense/direct probes are evaluated on different held-out episode sets (split seeds seed..seed+3), so the 'identical split' pairing claim is corrected; majority-adjusted gap +0.1015, 8/10 cells, the `create` stands. **F3:** the CREATE title's 'divergence costing ~0.10' is an unstated-premise attribution (an untrained random Linear+ReLU loses separability by itself); reworded, discriminating probe named. **F4:** `depends_on_unresolved: ['SD-070']` was a dangling id (no such sd_id; the SD-070 entry is `sd_zworld_warmup_optimizer_group`, validated) -- cleared. **F5:** `dv-dynamic-range-precondition-class` already carries the DV-headroom gate on `p0_readiness_gate`; the DV-floor check and the lint question are routed there. **F6:** V3-EXQ-1039 scored 2026-09-15 (PASS, `training_signal_does_not_convert_h1_not_supported`): H1 resolved negative; in-flight and fan-out text updated; no growth. **F7:** on the pre-registered sense() DV 2 of 5 seeds clear their own majority (both null): underpowered, not uninterpretable.

## Step 8 gate outcome -- CONFIRMED 2026-09-16T12:22:00Z

CONFIRMED as recommended, with red-team corrections F1-F7 applied (F1 withdrew the 'R3 target not in the feature space' claim; 5b DV-floor argument is the sole basis): direction non_contributory, category standard, no claim-field moves on INV-086 or MECH-428 (pending_retest_after_substrate stays true on MECH-428); substrate CREATE SD-ZWORLD-SENSE-PATH-PARITY (untrained world_obs_encoder pre-projection on the sense() path; attribution unmeasured -- run the discriminating probe before choosing the fix; depends_on_unresolved cleared; DV-floor check routed to dv-dynamic-range-precondition-class); ledger leg H-wpfield-zworld-interface stays alive with V3-EXQ-1030 recorded (applied at confirmation); routing queue-experiment (V3-EXQ-1030a: keep R3's target, majority-relative threshold, one split, >=3 seeds clearing the DV floor; governance chips it).
