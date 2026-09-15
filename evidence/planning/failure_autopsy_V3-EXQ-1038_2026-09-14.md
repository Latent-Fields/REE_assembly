# Failure autopsy (diagnostic adjudication) -- V3-EXQ-1038, ARC-131 coalition endogenous-recruitment rate

- **Status:** `awaiting_human_confirmation` -- **STAGING-MODE DRAFT**, headless. Routing is NOT finalised; the Step 8 interactive gate is OWED.
- **Generated (UTC):** 2026-09-15T00:09:49Z
- **Session:** `autopsy-staging-trio-20260914` (dispatched by metaworker orchestrator `orchestrate-20260914-2323`)
- **Scope:** single
- **Target:** `v3_exq_1038_arc131_coalition_endogenous_recruitment_rate_probe_20260914T201122Z_v3` (queue_id `V3-EXQ-1038`, backlog_id `EVB-1242`)
- **Trigger:** `experiment_purpose: diagnostic`. A **PASS**, unflagged -- exactly the case the blanket diagnostic trigger exists for.
- **Dry-run gate:** `check_dry_run_citations.py` on the run_id and `V3-EXQ-1038`: `0 dry cited, 0 dry in named families, 0 ambiguous, 1 clean, 0 unknown`. `dry_run_checked: true`, `excluded_dry_run_ids: []`.
- **Step 9b:** nothing owed -- see section 10.

---

## 1. Facts (no interpretation)

### 1a. What the run is

ARC-131 asserts that **installability** -- whether a mechanism actually expresses itself once composed into the whole organism -- is a competence dissociable from isolated component-level validation. Its `notes` cite coalition control as a concrete illustrative case: REE-v3 "has typed control demands, coalition templates and a controller, but it is inert until manually called and no endogenous monitor invokes it."

`chip-20260902-arc131-coalition-endogenous-recruitment-driver` (ree-v3 `88c7c3332c`) landed that missing monitor: an endogenous trigger inside `REEAgent.select_action`, gated by `use_endogenous_coalition_trigger` (**default off**), which reads the previous tick's E3 candidate-score margin (`sorted[1] - sorted[0]`) and calls `request_coalition()` when it falls below `endogenous_coalition_margin_threshold` (default **0.05**). Contract tests W9-W13 prove it *can* fire (`margin_threshold=1e6`) and *can* be suppressed (`-1.0`).

V3-EXQ-1038 asks the question those tests cannot: **does it fire at the shipped default in a live full-loop run, and how often?**

### 1b. Design

7 seeds (0-6) x 30 episodes x 100 ticks, on a 5x5 `CausalGridWorldV2` (1 hazard, 1 resource) with an **untrained** agent taking random forward passes -- the driver is explicit that no performance claim is made or needed, since the DV is a direct read of `agent._endogenous_coalition_request_count`. Before each seed's main measurement, a **40-tick positive-control burst at `margin_threshold=1e6`** (matching contract test W11) establishes that the call path and comparison machinery work outside the synthetic harness.

The driver carries its own cross-model red-team block (fable, CONTESTED, 4 findings F1a/F1b/F2/F3b, all dispositioned by fix). Those fixes matter to this autopsy and are assessed in section 5.

### 1c. What the manifest reports

**Criteria** -- exactly one entry:

| Criterion | load_bearing | passed | measured | threshold |
|---|---|---|---|---|
| `C0_readiness_control_fires` | **true** | true | 1.0 | 1.0 |

`interpretation.label: endogenous_recruitment_engaged_at_default_threshold`. Preconditions: `endogenous_trigger_mechanism_live` met (1.0/1.0). `outcome: PASS`. `evidence_direction: non_contributory`.

**Readout:** `frac_seeds_recruited 1.0` (7/7), `overall_frac_episodes_recruited 0.4905`, `overall_mean_request_rate_per_episode 0.7381`, `pooled_median_e3_margin 0.5785` over 2730 samples, `default_margin_threshold 0.05`, `control_fire_fraction 1.0`.

**Per seed** (the table the readout summarises away):

| seed | episodes recruited | frac | mean req/ep | total req | margin median | frac of margin samples <= 0.05 | n margin samples |
|---|---|---|---|---|---|---|---|
| 5 | 30/30 | **1.000** | **2.000** | 60 | **0.0183** | 0.856 | 390 |
| 2 | 29/30 | 0.967 | 1.333 | 40 | 0.1873 | 0.160 | 450 |
| 0 | 26/30 | 0.867 | 1.233 | 37 | 0.1368 | 0.197 | 390 |
| 6 | 7/30 | 0.233 | 0.233 | 7 | 1.636 | 0.022 | 360 |
| 1 | 4/30 | 0.133 | 0.133 | 4 | **11.157** | 0.011 | 360 |
| 3 | 4/30 | 0.133 | 0.133 | 4 | 3.818 | 0.010 | 390 |
| 4 | 3/30 | 0.100 | 0.100 | 3 | 2.210 | 0.010 | 390 |

(Margin medians independently recomputed; see section 5f on the 1.6% convention difference against the manifest's own figures.)

### 1d. Recording provenance

`validate_recording.py`: 1 manifest, **2 always-core gaps -- `elapsed_seconds` and `config`**. Present: `recording_schema: rec/v1`, `substrate_hash 28bdb912...`, `substrate_commit f85cfaf6` (`dirty: false`), `substrate_stable_across_run: true`, `substrate_identity`, explicit `seeds`, `machine: ree-cloud-2`, `machine_class: linux-x86_64-py3.10-torch2.12.0+cpu`, `enabled_default_off_flags` (`use_coalition_controller: true`, `use_endogenous_coalition_trigger: true`, `e3.goal_weight: 1.0`, `heartbeat.breath_period: 50`) sourced from `process_observed_config`.

**The missing `config` is the serious one** -- see 5f.

### 1e. Expected vs observed, and which criterion "failed"

**None.** This is a PASS, and the PASS is real: the positive control fired on every seed. But it is narrow in a way the manifest does not advertise -- `outcome = "PASS"` is assigned **unconditionally** in the driver's scoring block, on the line after the three-way label selection, so the verdict cannot vary with the measurement. The PASS certifies **instrument liveness**, and nothing about ARC-131.

---

## 2. Claim-layer mapping

| Field | ARC-131 |
|---|---|
| claim_type | `architectural_commitment` |
| status | `candidate` |
| epistemic_category | `standard` |
| implementation_phase | v3 |
| depends_on | MECH-457, MECH-459, ARC-120 |
| coupled_with | ARC-130 |
| **evidence** | **`[]` -- empty** |
| `evidence_quality_note` | absent |
| `diagnostic_evidence_adjudicated` | **absent (key not present)** |
| `what_would_answer` | absent |

**Did the experiment test the claim under conditions where it could express itself? No -- and it did not try to.** ARC-131 is a general architectural claim about a *property* (installability) being dissociable from isolated validation. Testing it requires a **dissociation**: a mechanism passing component-level validation and measurably failing to express in the composed agent, contrasted against one that does. This run measures one mechanism's recruitment rate. Its `outcome` cannot vary with the result. `non_contributory` is correct and the driver already stamps it.

**Claim-id accuracy:** the tag is appropriate but must not be over-read. What the run legitimately does is update the *factual state of ARC-131's own motivating example* -- see 5e -- which is a smaller thing than evidence about the claim.

---

## 3. Biological-reference triage

**Closest reference mechanism:** dACC conflict monitoring recruiting upstream cognitive control (Botvinick et al. 2001; Shenhav et al. 2013 EVC), with the decision variable read as a near-tie margin between top options (Hanes & Schall 1996). The call site cites exactly this literature, and the deliberate one-tick lag is correctly analogised to the Gratton conflict-adaptation effect.

**Faithful translation or formal import?** Faithful in kind -- this is not a formal-definition import, and `lit_status: present`. **No `/lit-pull` commission is owed.**

**The load-bearing divergence is in the decision variable.** Biological conflict monitoring adapts to the ambient difficulty distribution -- indeed the Gratton effect the driver itself cites *is* a demonstration of history-dependent, adaptive recruitment. REE's trigger compares a raw score difference to a hardcoded constant. Under the biological reference, a recruitment rate that varies 10x across otherwise-identical agents purely because their score scale differs is not "the mechanism engaging"; it is the threshold being mis-calibrated for most of them.

**And REE already contains the fix.** `SD-E3-CHANNEL-COMMENSURABILITY` (MECH-439, `ree_core/predictors/e3_selector.py`, IMPLEMENTED 2026-09-07) performs per-channel divisive normalisation against a running EMA of each channel's cross-candidate standard deviation, behind `E3Config.use_e3_channel_commensurability` (default `False`). **That flag is absent from this run's `enabled_default_off_flags`, so the operator was off.**

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **not exercised** | no dissociation scored; `outcome` cannot vary with the result |
| Biological reference | **partial** | faithful in kind; the decision variable diverges (section 3) |
| Dependency prerequisites | **present** | controller, templates, trigger and contract tests all in place |
| Implementation completeness | **complete** for what it claims | the trigger is wired, reachable, and fires; the gap is its decision *rule* |
| Environment adequacy | **too sparse** | 5x5 grid, untrained agent -- and the environment *generates* the readout (5b) |
| Measurement adequacy | **misleading** | **the dominant layer** -- three independent defects, 5b/5c/5d |
| Integration adequacy | **coupled but unstable** | the trigger is coupled to E3's raw score scale, and that coupling decides the result |
| Scale / capacity | **adequate** | 7 seeds x 30 episodes x 100 ticks, 2730 margin samples; seed correctly taken as the independent unit |

### Failure-location summary (GOV-FAILLOC-1)

| Bucket | Established? |
|---|---|
| MECHANISM FAILED | not established (implementation reads `complete`, but nothing failed) |
| MEASURES FAILED | **not established** (measurement reads `misleading`) |
| ENVIRONMENT FAILED | **not established** (environment reads `too sparse`) |
| REE FAILED | **false** |

**Net: MIXED (MEASURES + ENVIRONMENT), not chargeable to REE.** This is a PASS, so no organism-level failure read is in play at all; the classification is recorded because the skill requires it before any prose could describe REE as having failed, and nothing here does.

---

## 5. The diagnosis

### 5a. The only load-bearing criterion is the positive control

`criteria` contains exactly one entry, and it is the `margin_threshold=1e6` guaranteed-fire burst. The driver then assigns `outcome = "PASS"` unconditionally, regardless of which of its three measurement labels fired. This is a **defensible design for a pure measurement diagnostic** -- and it is precisely why a diagnostic PASS is never exempt from this skill, because to any downstream reader who does not open the driver, the manifest presents as a clean load-bearing PASS on a claim-tagged run.

### 5b. Recruitment is scale-determined, not conflict-determined -- the headline finding

Per-seed median E3 margin spans **0.0183 to 11.157 -- a 609x range** -- against a **fixed** 0.05 threshold. Recruitment then follows the margin distribution almost deterministically:

| frac of margin samples <= 0.05 | 0.856 | 0.197 | 0.160 | 0.022 | 0.011 | 0.010 | 0.010 |
|---|---|---|---|---|---|---|---|
| frac of episodes recruiting | 1.000 | 0.867 | 0.967 | 0.233 | 0.133 | 0.133 | 0.100 |

With ~12-15 fresh E3 evaluations per episode, a per-sample rate `p` predicts an episode rate of `1-(1-p)^13`, which reproduces the four low-rate seeds within a few points (`p=0.011 -> 0.134` predicted vs **0.133** observed; `p=0.022 -> 0.251` vs **0.233**).

So the DV is a near-deterministic readout of where an **untrained random-init network's score scale** happens to sit relative to a hardcoded constant.

**The driver anticipated this confound but pre-committed it to one direction only.** Its F1b/F2 note says -- correctly -- that *"a 'dormant' reading alongside margins that sit far above 0.05 supports a scale/calibration reading; a 'dormant' reading with margins hovering near 0.05 supports a genuine near-tie-rate reading."* Both clauses are conditioned on a **dormant** outcome. The observed outcome is **engaged**, and the confound is exactly as strong in that direction: the engaged verdict is carried entirely by the 3 of 7 seeds whose margins sit near the threshold, while the other 4 have median margins **32x to 223x** the threshold. A pre-registered confound analysis that names only one of two possible outcomes is a coin-flip away from not applying, and this run landed on the side it did not cover.

### 5c. The routing statistic destroys the run's own most informative signal

The label routes on `frac_seeds_recruited` -- the fraction of seeds with `total_requests > 0` across 30 episodes. The bar is **one request in thirty episodes**. Observed 7/7 -> "engaged".

But the per-seed recruitment fractions are sharply **bimodal** -- {0.867, 0.967, 1.000} against {0.100, 0.133, 0.133, 0.233}, with **no seed in between** -- and that bimodality is the actual finding.

Red-team F3b was **right** that the seed is the independent sampling unit (a static untrained network makes within-seed episodes correlated draws). But the per-seed statistic it then chose is maximally insensitive: it collapses a 609x scale spread and a 10x recruitment-rate spread into one bit per seed. Correct diagnosis of the independence problem, wrong choice of the seed-level summary.

### 5d. Readout (a) is arithmetically censored at 2, and the most informative seed is pinned on it

`mean_request_rate_per_episode` was introduced per red-team F1a specifically so it would be *"a genuinely distinct statistic"* from the binary readout (b), with `TICKS_PER_EPISODE` raised 20 -> 100 to give "~9 eligible evaluations/episode".

But the trigger is **debounced while a coalition of the same demand_type is already active** (`_ect_already_active`, `ree_core/agent.py`), and `coalition_max_duration_ticks` defaults to **50** (`ree_core/utils/config.py:3899`). So 100 ticks/episode admits **at most 2** requests, whatever the demand.

The manifest confirms the bound exactly: across all 210 episodes the per-episode count is 0, 1 or 2 and **never 3** (histogram `{0: 107, 1: 51, 2: 52}`), and **seed 5 -- by far the highest-demand seed -- sits at exactly 2 in all 30 of its episodes** (`{2: 30}`).

F1a's fix made (a) formally distinct from (b) but left it with a dynamic range of three values and a hard ceiling that the one high-demand seed saturates. The fix is to report requests per **eligible opportunity**, or to raise `TICKS_PER_EPISODE` well above `coalition_max_duration_ticks` -- not to raise ticks from 20 to 100 and stop.

**Related, smaller:** evaluation opportunity is not equal across seeds. At identical episode and tick budgets, fresh-E3-result counts were 390 / 360 / 450 / 390 / 390 / 390 / 360 -- **12.0 to 15.0 per episode, a 25% spread** -- which feeds the recruitment rate independently of the margin distribution. Small against the 609x scale effect, and it changes no conclusion here, but a successor reporting per-episode rates inherits it.

### 5e. ARC-131's own motivating example is now partly stale -- and the correction is a narrowing

ARC-131's `notes` describe coalition control as inert "until manually called and **no endogenous monitor invokes it**". The second half is no longer true.

But the example survives in a narrower and arguably more interesting form: `use_endogenous_coalition_trigger` **defaults to `False`** (`ree_core/agent.py`: `getattr(config, "use_endogenous_coalition_trigger", False)`), and **exactly one driver in the whole `ree-v3/experiments` corpus enables it -- this one**. (`use_coalition_controller` is enabled by **4** real drivers -- v3_exq_886, 970, 972, 1038. An earlier count of 6 included two `__pycache__/*.pyc` files; a recursive grep over an experiments tree counts compiled artifacts unless they are excluded, and a figure quoted into a claim note is exactly where that must not happen.)

So the **capability** now exists and the **default composition** still does not recruit it -- which is precisely ARC-131's own distinction between a mechanism being possible and the whole agent entering the states in which it operates. Governance should refresh the note to that split rather than strike the example.

**Citation hygiene:** the driver says *"Its own blocked_note names coalition control..."*. ARC-131 has **no `blocked_note` key** (its keys are claim_level, claim_type, coupled_with, depends_on, epistemic_category, evidence, id, implementation_phase, live_status, notes, polarity, registered_utc, source, status, subject, title, version_relevance). The content is real and lives in `notes`. Substantively harmless; procedurally not, since a reader following the citation finds nothing.

### 5f. Recording gap -- and this one is the serious kind

Missing **both `elapsed_seconds` and `config`**. A missing `config` means the run is not reproducible from its own manifest, and that the parameters which *generate* the headline finding are unrecorded -- `coalition_max_duration_ticks` (50, the request ceiling), `e3_steps_per_tick` (10, the evaluation cadence), the grid and dimension parameters. This autopsy had to recover all of them from `ree_core` and the driver source. Recording-debt, not measurement-debt: fix via `stamp_recording_core` in the successor, never by re-running blind. **This is the second manifest in this staging batch missing always-core fields**, which points at the shared emit path rather than at either author.

**Median convention** (recorded so a recompute does not look like a discrepancy): the manifest computes `sorted(x)[len(x)//2]`, the upper of the two middle order statistics, not the averaged median. Independent recomputation agrees within 1.6% on every seed (seed 0: 0.138954 vs 0.136772; pooled: 0.578491 vs 0.578079). No conclusion depends on it. Separately, **`pooled_median_e3_margin` is a mixture statistic across seeds whose scales differ 609-fold and should not be quoted as "the" margin scale** -- the per-seed medians are the meaningful figures, and the manifest does record them.

---

## 6. Cluster pattern

Not a cluster. Single target; no sibling shares this shape this tick.

---

## 7. Learning extracted and repair pathway

**Two halves, two debt classes** -- corrected per Step 7c red-team F3, which caught the first draft calling both `complicated (buildable)`.

1. **The measurement redesign is `complicated (buildable)`** -- every required change below is a named driver edit with no open question. Primary routing is `/queue-experiment`, which is where the Step 7 routing *table* sends a measurement / test-design gap; stated explicitly as an **override** of the work-graph list's mapping of `complicated (buildable)` to `/implement-substrate`.
2. **The substrate half is `complex (probe-gated)`**, and V3-EXQ-1038a's commensurability arm **is** the probe. Enabling the already-built operator needs no new code, so the one genuinely new build -- a scale-relative recruitment threshold -- is scheduled if and only if the probe shows normalisation alone is insufficient. The SD-091 amend records the finding and the gating; it does not queue that build now.

**Primary routing: `/queue-experiment` -> `V3-EXQ-1038a`** (alphabetic: the scientific question is unchanged; the measurement's construction was wrong).

1. **Make the scale an ARM, not a nuisance -- and set the flag on the path that actually reads it.** Add a second arm with E3 channel-commensurability ON against the current default-off arm, everything else fixed. *Declared null:* cross-seed spread in per-seed recruitment fraction does not shrink under normalisation -- which would mean the 609x margin spread is not what drives recruitment after all.

   **Mechanical warning, and it is load-bearing** (Step 7c red-team F4): `use_e3_channel_commensurability` is an **`E3Config`** field (`ree_core/utils/config.py:1073`, default `False`), **not** a `REEConfig.from_dims` keyword. `from_dims` ends in a `**kwargs` sink (`config.py:8408`) its body never reads, so passing the flag there is **silently dropped** and the ON arm would be bit-identical to the control -- an arm inert by construction, which is exactly the defect class this autopsy exists to repair. This is the known [memory] `reference-reeconfig-from-dims-silent-kwargs` failure mode, and `config.py`'s own comments at 8374-8401 name it. Use V3-EXQ-1012a's pattern: set `cfg.e3.use_e3_channel_commensurability = True` on the built config (1012a line 355), **read it back off the live object** as a readiness assert -- `bool(getattr(agent.e3.config, "use_e3_channel_commensurability", False))` (1012a line 357) -- and additionally assert the operator actually **engaged** (its running channel-scale estimates left warm-up), not merely that the flag is set. An ON arm that silently equals its OFF arm must fail readiness, not report a null.

   **State the operator's own status in the driver.** `SD-E3-CHANNEL-COMMENSURABILITY` is folded into the `f_dominance_conversion_ceiling` entry and, since the 2026-09-10 `/governance` amendment GFLAG-0234, is marked **"IMPLEMENTED but UNVALIDATABLE AS SPECIFIED"** -- its original readiness target was found to be an arithmetic identity of the operator (shares tend to 1/k), and the amended target is a **selection-level** DV (commit-flip rate under shadow OFF/ON scoring on the same tick and candidate set). That makes this arm *more* valuable, not less -- a consumer-side behavioural reading is exactly the non-tautological evidence the rung now needs -- but it must be described as exercising an operator whose own validation is **open**, never as relying on a validated one.
2. **Route on a statistic that can express bimodality.** Drop `frac_seeds_recruited` as the routing statistic (bar: one request in thirty episodes; it read 1.0 on a bimodal distribution). Route on the per-seed recruitment-fraction *distribution*; keep ever-recruited as descriptive context. Keep F3b's correct insight that the seed is the independent unit -- change only the seed-level summary.
3. **Remove the ceiling from readout (a).** Report requests per **eligible opportunity** (requests / fresh-E3-results), which also fixes the unequal-opportunity problem, and/or raise `TICKS_PER_EPISODE` well above `coalition_max_duration_ticks`. Verify by asserting no seed sits at the arithmetic maximum in every episode -- seed 5 did exactly that here.
4. **Normalise or report evaluation opportunity per seed** (360-450 fresh E3 results at identical budgets).
5. **Record the margin distribution relative to the threshold**, not only in absolute units -- the sub-threshold *fraction* is what actually predicts recruitment.
6. **Stamp `config` and `elapsed_seconds`** via `stamp_recording_core`.
7. **State in the driver that the PASS criterion is the readiness control and cannot vary with the measurement** -- a `combination_rule` string of the kind V3-EXQ-1030's manifest carries makes this legible without changing behaviour.

**Explicitly NOT recommended:**

- Do **not** re-run this as a test *of* ARC-131. A single mechanism's recruitment rate is one instance and cannot test a general claim about installability; a genuine ARC-131 test needs a **dissociation**.
- Do **not** queue **V3-EXQ-886** (the coalition 4-arm performance-recovery falsifier) off the back of this. The 1038 driver's own reason for leaving 886 unqueued -- it needs a goal-directed, online-adapting agent competence the naive harness does not supply -- is unaffected by anything found here.
- Do **not** read the PASS as evidence for ARC-131, or `endogenous_recruitment_engaged_at_default_threshold` as an architectural property. It is a property of an untrained random-init score scale on a 5x5 grid.
- Do **not** pass `use_e3_channel_commensurability` to `REEConfig.from_dims(...)` -- it falls into the `**kwargs` sink and is silently dropped (change 1 above).
- Do **not** schedule the scale-relative-threshold substrate build alongside the re-queue -- it is probe-gated on 1038a's arm.

### 7b. Substrate routing -- `amend` SD-091

`SD-091` already exists in `substrate_queue.json` at status `implemented_smoke_pass_falsifier_designed_blocked_substrate_harness_confound`, unblocking `['SD-091', 'MECH-481']`, with **0 failure records and NULL `substrate_paths`**. Three things to record on it:

1. **Status fact.** V3-EXQ-1038 is the first live full-loop exercise of the endogenous trigger and it fires -- 7/7 seeds recruit at least once at the shipped default, and the 1e6 control fires on every seed.
2. **Populate `substrate_paths`** (currently null): `ree_core/agent.py::REEAgent.select_action` and `ree_core/claustrum/coalition_controller.py`.
3. **The defect**, and why this is an amend rather than a new entry: the trigger thresholds an **absolute** margin against a score REE already knows to be non-commensurable. The `f_dominance_conversion_ceiling` entry (severity **`corrupting`**, status `build_owed`, **27** failure records, paths naming `e3_selector.py::score_trajectory`) owns exactly that problem -- confirmed `failure_autopsy_V3-EXQ-571c_2026-09-02` measured one channel holding 0.98-0.99999 of cross-candidate variance in 15 of 16 cells. **The endogenous coalition trigger is a new downstream consumer of that same unnormalised score**, and this run is the first measurement of what the monopoly does to it.

**Severity `degrading` -- recommended, but flagged to the Step 8 gate as the most contestable call in this artifact.** The first draft argued it from a precedent that the Step 7c red-team showed was cited **backwards**.

*What the precedent actually says.* `SD-ORIENTING-DECISION-SCALE`'s own `severity_note` reads, verbatim: *"degrading (residual): the ORIGINAL corrupting-severity norm-vs-value scale mismatch (Component 4/5) is FIXED and validated by regression test. V3-EXQ-910a's retest surfaced a SEPARATE, lesser residual defect in decision_counts persistence-window logging."* So a norm-vs-value **scale mismatch in `select_action` was stamped `corrupting`**; the `degrading` on that entry belongs to a *logging* residual. That is a **counter-precedent**, not support.

*Why `degrading` is still recommended,* on arguments independent of the precedent: **(a) merits** -- the defect does not manufacture a result that looks valid and is not. The trigger fires, the counter counts, and the 1e6 control rules out an instrument defect, so the **existence** finding survives intact; what is compromised is the **magnitude** of any rate readout, which is what `degrading` names. The orienting-decision case differs on exactly this point: there the scale mismatch decided the *override itself*. **(b) blast radius** -- Step 2.5c matches an open `corrupting` entry at *module* granularity and `ree_core/agent.py` is entered by essentially every REE driver, so a corrupting stamp would STOP-gate the entire programme including this autopsy's own repair (the same asymmetry the confirmed 1004 autopsy reasoned through for `causal_grid_world.py`).

*The gate should decide.* The merits argument is real and so is the counter-precedent; a staging draft should hand a genuinely contestable severity call to the human rather than settle it.

**A `corrupting` severity field does not imply a live gate** (red-team F2, and the first draft leaned on the opposite). The draft argued `degrading` was safe here because the corrupting classification "is already on record upstream where it belongs" -- pointing at `f_dominance_conversion_ceiling`. That is **true as a field and false as a gate**: `check_substrate_path_overlap.py` decides OPEN vs CLOSED from the entry's `status` **string** against a closed set including `validated`, and that entry's status is the long `mech448_lead_lever_BUILT_VALIDATED_PROMOTED_provisional__...` token, which matches **CLOSED**. Running the gate's own script shows it gating nothing and absent from its open list, despite `severity: corrupting` and `status_phase: build_owed`. **Consequence, a governance finding in its own right and not this autopsy's to fix:** nothing currently gates new experiments consuming the unnormalised E3 score, even though the entry owning that defect is classified corrupting and still owes a build.

**The `f_dominance_conversion_ceiling` entry is NOT amended here:** a 28th failure record restating what its own V3-EXQ-571c evidence already establishes adds nothing, and the new information is about a downstream consumer, which is SD-091's business.

**How much is actually left to build -- corrected, the first draft over-scoped it** (red-team F3). Half the work is **already built**: the trigger reads `result.scores`, and `score_trajectory` divisively normalises those very terms when the flag is on (`e3_selector.py`, `_comm_on` at 1509 and the selection-level path at 3060). So merely **enabling** the existing operator already changes the margin the trigger sees -- no new code. The only genuinely new build is the *second* option, a scale-relative threshold, and whether it is needed at all is exactly what 1038a's arm decides. **So this entry's build is `complex (probe-gated)`, not `complicated (buildable)`, and is gated on V3-EXQ-1038a** -- `priority_suggested` lowered 3 -> 4 accordingly. Do not schedule the threshold rework alongside the re-queue.

### Re-derive brake (MOVE-3)

**Does not fire.** R1-R3 recipe run 2026-09-15 over the confirmed corpus: **ARC-131 = 0 hits** -- no prior autopsy target anywhere names it in its own `claim_ids`. This autopsy adds 0 (per-claim category `standard`, excluded by the per-claim short-circuit). Far below the threshold of 2.

### Granularity-debt recurrence trigger

**Does not fire.** `granularity_debt_cluster.py`: ARC-131 has **0 tagging targets across 0 files**. This is the first autopsy target to name it, so there is no recurrence to read and no alignment distribution to weigh. A cluster of one cannot fire the trigger.

### `pending_retest_after_substrate` -- deliberately FALSE

This autopsy does **not** recommend a substrate-limitation reading awaiting a build. The `non_contributory` direction is because the run does not *test* ARC-131 at all, not because a substrate ceiling blocked an otherwise well-posed test; setting the flag would assert that a future build makes *this* design answer ARC-131, which it would not. The paired narrow-supports check is likewise not engaged: ARC-131's `evidence` list is **empty**, so there are no existing "supports" whose narrowness could be at issue.

---

## 8. Draft `evidence_quality_note` for governance

> [2026-09-14, V3-EXQ-1038, PASS, diagnostic] First live-run exercise of SD-091/MECH-481's endogenous coalition-recruitment trigger (landed ree-v3 88c7c3332c), which had no live caller of request_coalition() before it. NOT a test of ARC-131: the single load-bearing criterion is the guaranteed-fire readiness control at margin_threshold=1e6, the driver assigns PASS unconditionally of the measurement, and no isolated-vs-composed dissociation is scored -- non_contributory. What it DOES establish is a factual update to ARC-131's own motivating example, which the claim's `notes` currently describe as "inert until manually called and no endogenous monitor invokes it": an endogenous monitor now exists and fires in 7/7 seeds at the shipped default threshold of 0.05. That update is PARTIAL in exactly ARC-131's own capability-vs-composition terms -- `use_endogenous_coalition_trigger` defaults to False and exactly 1 driver in the ree-v3 corpus enables it (this one), so the DEFAULT composition still does not recruit the controller. Read the recruitment RATE with care: it is scale-determined, not architectural. The per-seed median E3 margin spans 0.0183 to 11.16 (a 609x range) against the fixed 0.05 threshold, and per-seed recruitment tracks the fraction of margin samples below that absolute threshold almost exactly (0.856 of samples -> 100% of episodes; 0.011 -> 13.3%). The "engaged" verdict is carried entirely by the 3 of 7 seeds whose untrained random-init score scale happens to sit near the threshold; the other 4 recruit in 10-23% of episodes. E3's channel-commensurability operator (MECH-439, SD-E3-CHANNEL-COMMENSURABILITY, implemented 2026-09-07) exists to normalise precisely that scale and was OFF in this run.

**Two distinct applications are owed** (see `per_claim_recommendation`): set `diagnostic_evidence_adjudicated: true` (the key is currently **absent**) and write the note above (`evidence_quality_note` is currently **absent**, `evidence` is **empty** -- this would be ARC-131's first entry); and **separately**, refresh the stale half of the `notes` paragraph per 5e.

---

## 9. Step 7b mechanical pre-routing checks

`fire_count: 0`. C5 and C7 reported `inapplicable` -- and the skill's rule that **`inapplicable` is not "no fire"** applies: C5 is prose-keyed and C7 needs an arm-structured result array, so neither could look. Section 7c carries the load.

---

## 10. Step 9b -- frozen ledger: nothing owed

Step 9b fires when the autopsy either emits a `fanout_recommendation` or adjudicates a leg of a registered question. **Neither holds**, so it is skipped cleanly.

- No fan-out is emitted: the open question routes to one named build, which is the skill's own stated exemption.
- The registry carries no question whose `claims` include ARC-131, and no hypothesis whose `adjudicating_runs` name V3-EXQ-1038 -- so this run adjudicates nothing pre-registered.
- The growth-restriction check is therefore not engaged either (it applies only to a leg attaching to an already-registered question).

Recorded explicitly rather than left silent, because an absent check is indistinguishable from a passed one.

---

## 11. Step 7c red-team

**Verdict: CONTESTED.** Run on **Fable 5.1** while this drafting session runs on **Opus** -- a **cross-model** pass. Findings file: `redteam_1038.md` in the session scratchpad; full disposition in the JSON `red_team` block.

**Four verdict-moving findings, all applied:**

- **F1** -- the `SD-ORIENTING-DECISION-SCALE` severity precedent was cited **backwards**. Confirmed from that entry's own `severity_note`. *Applied:* false precedent removed, entry re-cited honestly as a counter-precedent, `degrading` re-argued on merits and blast radius alone, and the call explicitly handed to the Step 8 gate (section 7b).
- **F2** -- "the corrupting classification is on record upstream" is true as a *field*, false as a *gate*. *Applied:* claim withdrawn, the recommendation no longer leans on upstream protection, and the gap surfaced to governance as a finding in its own right (section 7b).
- **F3** -- the substrate half was over-scoped as `complicated (buildable)`; half the work is already built. *Applied:* reclassified `complex (probe-gated)` with 1038a's arm as the probe, build explicitly gated, priority lowered 3 -> 4 (sections 7 and 7b).
- **F4** -- `required_changes[0]` could have produced an **arm inert by construction** via the `from_dims` `**kwargs` sink. *Applied:* the change now names the assignment path, a read-back readiness assert, and an engagement assert, with an explicit do-not (change 1 above).

**Considered and not adopted:** F5, the skill's leave-severity-unset clause -- it covers a defect nothing has exercised yet, and this run exercised it; the severity question goes to the gate instead.

**Verified sound and left standing:** the 609x spread and the sub-threshold-fraction relationship; the `1-(1-p)^13` argument (independently recomputed -- seeds 1/3/4/6 predicted 0.135/0.125/0.125/0.253 vs observed 0.133/0.133/0.100/0.233); the ceiling of 2 (independently derived, including that dissolution here is timeout-only since no `agent_state`/`completion_condition` is passed, that the trigger runs before `coalition.tick()`, and that a third request would need >= 103 ticks); seed 5 at exactly 2 in all 30 episodes and the `{0:107, 1:51, 2:52}` histogram; the flag-OFF inference; exactly-one-driver and default-False; all four ARC-131 field claims (so the `-> diagnostic_evidence_adjudicated: true` tail is storable and not already true); Step 9b's 0 hits; amend-not-create on SD-091; `pending_retest_after_substrate: false`; and the 1004 blast-radius precedent.

**One red-team claim was itself wrong on a fact** and is corrected rather than absorbed: it reported `v3_exq_886` as also enabling the endogenous trigger. It does not -- 886 sets only `use_coalition_controller`, at its lines 526 and 901. A red-team finding is a pointer to verify, in both directions.

**Both this pass and V3-EXQ-1030's contested only the RECOMMENDATIONS, never the science** -- the measured pattern for this check.

---

## 12. What is OWED before this can be applied

1. **The Step 8 interactive gate** -- this draft's routing is a proposal, not a decision.
2. **Nothing was marked reviewed.** `review_tracker.json`, `claims.yaml`, `substrate_queue.json`, the queue and the registry are untouched by this session.
3. Per CLAUDE.md, this autopsy **does not `spawn_task` its own follow-on**. `/governance` chips V3-EXQ-1038a and the SD-091 amend once Step 2b ratifies the routing.
