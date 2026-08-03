# Failure Autopsy: dACC substrate cluster (V3-EXQ-862a Q-040c + V3-EXQ-870a MECH-480)

**Generated:** 2026-08-03T08:20:00Z
**Status:** awaiting_human_confirmation (staging-mode write — this session is one of several parallel autopsy sessions; routing is drafted, not finalized. Present to the user for the Step 8 interactive gate before `/governance` consumes it.)
**Scope:** cluster (2 targets — different claims, same dACC substrate module `ree_core/cingulate/dacc.py` + adjacent V_s/environment machinery, both authored/run 2026-08-02, both FAIL)

## 0. Pending-review flags and dry-run gate

- `v3_exq_862a_q040c_dacc_pe_weight_delta_correlation_20260802T195935Z_v3` — `pending_review.md` "FAIL (action required)", claim Q-040.
- `v3_exq_870a_mech480_dacc_execution_gain_dissociation_20260802T135309Z_v3` — `pending_review.md` "FAIL (action required)", claim MECH-480.
- **Dry-run gate (manual — `REE_assembly` local checkout is 44 commits behind `origin/master` with an unrelated dirty tree from another session's regen; read `dry_run` directly off each manifest at `origin/master` rather than running `check_dry_run_citations.py` locally against a stale/dirty tree):** both manifests carry `dry_run: null`/absent (falsy). Both pass `validate_recording.py`'s always-core requirements on inspection: `recording_schema: rec/v1`, `substrate_hash` present, `machine`/`machine_class` present, `elapsed_seconds` present (5314.9s / 3533.1s), `seeds` explicit ([42,7,19] / [42,7,13]). Neither is a smoke. `dry_run_unreachable_criterion` lint not applicable — neither is in the `v3_exq_543` lineage the lint targets.

## 1. Facts

### 1a. V3-EXQ-862a (Q-040.c — dACC bias-magnitude vs precision-weighted PE correlation under MECH-269b V_s gating)

**Lineage.** Third letter in a row on the same sub-question. 475b (2026-08-01, confirmed autopsy): PE never computed — `enable_affective_harm_stream` never forwarded, `z_harm_a` stayed structurally `None`, `n_dacc_fires=0` everywhere → `non_contributory`. 862 (2026-08-02, confirmed autopsy): PE now computes (`n_dacc_fires=451`), but `dacc_weight` (the `DACCtoE3Adapter` consumer gain) defaulted to 0.0 and was never set by the driver, so the bias output was the zero vector regardless of PE → `non_contributory` again, second independent bug. 862a's fix: `cfg.dacc_weight = 0.5`, `cfg.dacc_interaction_weight = 0.5` set directly in `_build_arm_config`, plus an extended preflight (`PreflightDaccBiasZero`) asserting peak bias magnitude clears 1e-6 before the full design commits.

**Design.** 3 seeds (42, 7, 19) × 2 arms: `ARM_vs_off` (`use_vs_rollout_gating=False`) vs `ARM_vs_on` (`=True`, plus 490b's smoke-scale gate-threshold overrides `vs_gate_snapshot_refresh_threshold=0.95`, `vs_gate_e1_threshold=0.85`, `vs_gate_e2_threshold=0.85` applied globally across all six V_s-gated streams). Primary DV: per-(seed, arm) Spearman rho between per-tick precision-weighted PE (`bundle["pe"]`) and dACC bias-vector L2 magnitude, over ticks where dACC fired. PASS requires ≥2/3 ON-arm seeds with `|rho| >= 0.3` (detect) AND ≥2/3 OFF-arm seeds with `|rho| < 0.15` (null).

**Outcome: FAIL.** Preconditions both pass (`p1_gate_firing_pass`, `p2_dacc_engagement_pass` both true — `preflight_peak_bias_magnitude=199.4`, engagement confirmed on all 6 cells). But **C3 (`on_detects_correlation`) fails completely: 0/3 ON-arm seeds clear `|rho|>=0.3`.** C4 (OFF-arm null) passes 2/3.

**Code-verified root cause — the manipulation never engaged the pathway the DV reads.** Per-seed, per-arm data:

| Seed | Arm | rho | n_dacc_fires | `vs_gate_held_e1_z_harm_a` | `vs_gate_held_e1_z_beta` | `vs_gate_total_held` |
|---|---|---|---|---|---|---|
| 42 | vs_off | 0.0294 | 734 | — | — | 0 |
| 42 | vs_on | **0.0294** | 734 | **0** (of 128 refreshes) | 119 | 122 |
| 7 | vs_off | -0.0476 | 1946 | — | — | 0 |
| 7 | vs_on | **-0.0476** | 1946 | **0** (of 200) | 191 | 193 |
| 19 | vs_off | -0.1839 | 1326 | — | — | 0 |
| 19 | vs_on | **-0.1839** | 1326 | **0** (of 10) | 1 | 1 |

`rho`, `n_dacc_fires`, `total_eval_steps`, and the full `pe_series`/`bias_magnitude_series` arrays are **bit-identical between arms, per seed** (verified: `pe_series[0]`/`bias_magnitude_series[0]` match to full float32 precision in every seed). `dacc.py:211-214` computes `pe = ||z_harm_a - z_harm_a_pred||` — the claim's entire causal chain runs through the freshness of `z_harm_a` specifically. But `vs_gate_diagnostics` shows **`vs_gate_held_e1_z_harm_a = vs_gate_held_e2_z_harm_a = 0` in every ARM_vs_on cell, across all 3 seeds** — `z_harm_a` was refreshed on literally every gate check (128/128, 200/200, 10/10), never once held stale. What the gate *did* hold, almost exclusively, was `z_beta` (119/122, 191/193, 1/1 of the total-held count). The threshold that gates every stream (`vs_gate_e1_threshold=0.85`, `vs_gate_e2_threshold=0.85`, applied uniformly rather than via the gate's own `e1_threshold_per_stream`/`e2_threshold_per_stream` override dicts) was carried verbatim from V3-EXQ-490b, which calibrated it against a *different* target stream's V_s dynamics. At that threshold, `z_harm_a`'s own V_s apparently never dips below 0.85 in this harness — so the ON arm's "staleness" manipulation landed entirely on `z_beta` (a stream the DV does not read) and never touched `z_harm_a` (the one stream it does). ARM_vs_off (gating fully disabled) and ARM_vs_on (gating enabled but never crossing threshold for the one relevant stream) are therefore **functionally identical for this DV** — which is exactly what the bit-identical series confirm.

**This is a manipulation-check failure, not a substantive result.** C3/C4 compared two arms that never differed on the dimension the primary DV depends on. The P1 precondition (`vs_gate_total_held > 0` on ≥2/3 seeds) passed and gave false confidence, because it aggregates hold-counts across **all six** V_s-gated streams rather than checking the one stream (`z_harm_a`) this specific sub-question needs stale.

### 1b. V3-EXQ-870a (MECH-480 — LOFC-analog execution-gain channel dissociable from dACC-analog strategy authority)

**Lineage.** First letter; supersedes 870 (ERROR — crash-before-manifest, `torch.multinomial` NaN from an unclamped `dacc_weight=3.0` positive-feedback loop, diagnosed via `/diagnose-errors` 2026-08-02). 870a's fix: `dacc_bias_max_abs=2.0` clamp (the 445g/445h/597 precedent value), everything else unchanged.

**Design.** 3 seeds (42, 7, 13) × 2 arms (OFF: `dacc_weight=0`; ON: `dacc_weight=3.0`, clamped). CausalGridWorldV2, 80 steps/episode, resources start left-confined and are geometrically relocated to the right quarter at step 40 (`SWITCH_STEP`) mid-episode; 20 eval episodes. Two DVs read off the unmodified E3 selector: (i) `post_switch_toward_new_frac` — fraction of post-switch ticks with positive (rightward) realized displacement; (ii) `execution_strength` — mean logit margin of genuine E3 selections in the post-switch window (`step >= switch_step`), averaged over `margins` collected only on genuine (non-latched) E3 ticks.

**Outcome: FAIL** (`no_reliable_outcome_sensitivity_effect`; C1 seed_hits=0/3, C2 seed_hits=0/3). The non-degeneracy precondition reads `met: true` (arm-OFF execution-strength range 1.5054 > floor 0.0001) — **but this check silently excludes a NaN seed**, so it "passed" on 2 of 3 OFF-arm seeds, not 3.

**Two distinct, code-verified problems, not one:**

**(a) Survival censoring — the post-switch window is structurally unreached in half the cells.** `execution_strength` is `NaN` (0 margin samples) in exactly the cells where total tick count (`n_latched_ticks + n_genuine_selections`) collapses far below the `20 episodes × 80 steps = 1600` budget:

| Seed | Cond | Total ticks (of 1600 max) | Mean steps/episode | `execution_strength` |
|---|---|---|---|---|
| 42 | OFF | 1145 | 57 | 1.5997 (valid) |
| 42 | ON | **230** | **12** | **NaN** |
| 7 | OFF | **167** | **8** | **NaN** |
| 7 | ON | 1597 | 80 | 2.5296 (valid) |
| 13 | OFF | 1442 | 72 | 0.0943 (valid) |
| 13 | ON | **394** | **20** | **NaN** |

With `SWITCH_STEP=40`, an episode averaging 8-20 steps almost never reaches the post-switch window at all (`done=True` fires well before step 40 in most of the 20 episodes) — so `margins` (post-switch-only, genuine-tick-only) collects nothing, and `execution_strength` is a division of an empty sum, correctly `NaN` by the driver's own arithmetic (`float(sum(margins)/len(margins)) if margins else nan`). This is **not condition-linked** (hits ON for seed42/13, OFF for seed7) — it looks like a seed×condition interaction in how often the agent survives to mid-episode, most plausibly hazard collision given `NUM_HAZARDS=2` is the only other source of early termination in this env. The design has **no per-cell precondition on "episodes reaching switch_step"** — the only non-degeneracy check that exists (arm-OFF execution-strength cross-seed variance) happens to still read `met: true` because it silently drops the one NaN OFF seed (7) from its list comprehension (`if not math.isnan(...)`) rather than flagging reduced N. A precondition passing on 2/3 samples while reporting itself as fully satisfied is a design gap in the acceptance check itself, not only in the environment.

**(b) Even where the window IS reached, the outcome-sensitivity DV reads a near-uniform floor.** Of the 3 cells with full post-switch data (42-OFF, 7-ON, 13-OFF), `post_switch_toward_new_frac` = 0.0, 0.0, and 0.0365 respectively — essentially no agent, in any well-powered cell, shows meaningful locomotion toward the relocated resource region within the post-switch window, regardless of dACC arm. This could reflect (i) a genuine substrate property — REE's trajectory generation may commit to a spatial plan early in the episode and not adaptively revise it when the environment's reward structure changes mid-episode (a real, testable claim about replanning stickiness, independent of dACC) — or (ii) a DV-sensitivity gap: `resource_field_decay=0.5` is fairly steep and `proximity_benefit_scale` (0.12) sits close to `proximity_harm_scale` (0.1), so net displacement direction may be a weak/noisy proxy for "outcome sensitivity" at this env scale. Either way, the near-zero reading in the *well-measured* cells is what actually decides C1 — the censored cells (a) never had a chance to contribute in the first place.

## 2. Claim-layer mapping

**Q-040 / Q-040.c** (`claims.yaml`): open_question, `implementation_phase: v3`, `depends_on: [MECH-269, MECH-269b, SD-032b, SD-037]`. Q-040.c is explicitly the "mechanism-quantification follow-on" sub-question (registered 2026-05-08), scoped to test *whether* dACC's bias magnitude tracks precision-weighted PE, not to re-adjudicate Q-040.a/b (already settled by the 490 cohort per the claim's own notes — "a FAIL here does NOT reopen Q-040a/b"). This FAIL does not touch that settled territory.

**MECH-480** (`claims.yaml`): candidate, `claim_level: mechanistic`, registered 2026-08-02 (same day as its first two runs), `depends_on: [SD-032b, MECH-258, MECH-260]`. Its own `what_would_answer` explicitly anticipates SD-032b's known `substrate_ceiling` trap (SD-032b/MECH-260 are floor-locked on committed-action-entropy per `failure_autopsy_V3-EXQ-445h_2026-06-19`, gated on the still-open F-dominance/MECH-439 conversion ceiling) and *deliberately* designs its execution-strength DV (logit margin, not committed-action diversity) to route around it. **That design choice worked** — this FAIL does not reproduce the SD-032b ceiling signature (no floor-locked committed-action entropy anywhere in this manifest); it hit a different, more mundane environment/instrumentation gap instead (survival censoring + DV floor effect, §1b above).

**Did the experiments let the claims express themselves?** For both: no. 862a never varied the specific channel (`z_harm_a` staleness) its DV reads, so Q-040.c's mechanism was never actually put to the test this round. 870a's censoring problem means half its cells never reached the manipulation window, and even the surviving cells may be measuring a DV too coarse to detect the effect MECH-480 predicts. Neither FAIL is evidence against its claim; both are instrumentation/design gaps that need repair before either claim gets a real test.

## 3. Biological-reference triage

**Q-040 / dACC PE-bias coupling.** Closest reference: Shenhav et al. 2013 (Expected Value of Control, dACC) and Shenhav 2016 (dACC choice-difficulty/value-control) — both already in `targeted_review_q_040` alongside Brown & Braver 2007 (error-likelihood/risk) and Hayden 2011 (unsigned RPE → behavioural adjustment), plus Treuting 2025 (causal ACC adaptive RL). Biological reference is **clear** and pre-existing; the FAIL is squarely an instrumentation gap, not a biology-translation question — no new lit-pull is owed here.

**MECH-480 / LOFC-analog execution-gain dissociation.** Closest reference: Asaoka, Pagano & Hayashi 2026 (Nat Commun, dissociable ACC-retrosplenial "strategy authority" vs lateral-OFC-central-striatal "execution gain/vigor" circuits) — already cited in `claims.yaml` via targeted search, closing the claim's own flagged `/lit-pull` follow-up. **However, there is no `evidence/literature/targeted_review_mech_480/` directory** with a formal record/summary entry — the citation lives only as prose in `claims.yaml`'s `notes` field. This is a minor, secondary gap (the paper is identified and the translation is a direct one-to-one mechanism mapping, not a formal-concept import needing deeper biological grounding), but worth a `/lit-pull` commission to formalize the entry so it is queryable the way every other cingulate-adjacent claim's literature is.

## 4. Four-layer diagnosis

| Layer | V3-EXQ-862a (Q-040.c) | V3-EXQ-870a (MECH-480) |
|---|---|---|
| Claim alignment | unclear — manipulation never engaged | unclear — DV under-powered in half the design |
| Biological reference | clear (Shenhav 2013/2016, Hayden 2011, Treuting 2025 — pre-existing) | clear but not yet formalized (Asaoka 2026 — cited in claims.yaml, no `targeted_review_mech_480` entry) |
| Developmental/dependency prerequisites | present — MECH-269b V_s gating IMPLEMENTED and confirmed firing (P1 pass); dACC PE computation confirmed firing (P2 pass) | present — SD-032b dACC substrate, E3 selector, CausalGridWorldV2 all implemented and exercised |
| Implementation completeness | complete — `dacc.py`, `vs_rollout_gate.py` both work exactly as documented | complete — the `dacc_bias_max_abs` clamp fix from 870 landed correctly (preflight confirms it reached the adapter) |
| Environment adequacy | adequate for engagement; **inadequate for the specific manipulation** — `z_harm_a`'s own V_s dynamics never cross the borrowed 0.85 threshold in this harness | **inadequate** — 2-hazard grid produces highly variable, seed×condition-dependent early episode termination that the design does not gate on |
| Measurement adequacy | **defect** — DV (rho of PE vs bias) is sound, but the arm-defining precondition (`vs_gate_total_held`) is too coarse (aggregates 6 streams) to confirm the ONE stream the DV needs staled | **defect** — non-degeneracy check silently drops a NaN seed instead of flagging reduced N; outcome-sensitivity DV may also be under-sensitive even when measured |
| Integration adequacy | isolated — two independently-gated stages (PE computation, bias consumption) both confirmed to fire; the gap is a third, orthogonal stage (which specific stream gets staled) | isolated — DV computation, episode termination, and dACC gain are three separate mechanisms whose interaction (does the agent survive long enough) was not itself gated |
| Scale/capacity | not implicated | not implicated (compute budget is not the bottleneck — episode length is) |

## 5. Cluster pattern

**Shape.** Two structurally different bugs (a globally-applied, wrongly-calibrated per-stream threshold vs. an environment survival-censoring gap) — **not** the same defect. But both share **one convergent structural property**: each experiment's own precondition/acceptance-gate checks for engagement **in aggregate** (any of six V_s streams held; any nonzero execution-strength sample from 2 of 3 seeds) rather than **on the specific slice the primary DV actually reads** (the `z_harm_a` stream specifically; the post-switch window specifically, per cell). Both preflight/precondition checks reported "met" and let the full-budget run proceed, when in each case the aggregate signal was masking that the load-bearing slice never engaged.

**Reading.** This is a **test-design/instrumentation convention gap**, not two independent flukes and not a substrate ceiling — both driver scripts are recently-authored (2026-08-02), both build on a shared authoring convention (borrowing threshold/precondition values from a prior sibling experiment — 490b's global gate thresholds; the standard non-degeneracy list-comprehension pattern), and both times the convention was coarse enough to miss a per-channel or per-cell failure. Worth naming explicitly for future `/queue-experiment` authoring in this dACC-adjacent cohort: **a precondition should assert engagement of the specific substrate slice (stream / time-window / cell) the primary DV consumes, not merely "some" nonzero engagement somewhere in the design.**

## 6. Learning extracted

1. **A stream-level V_s gate threshold borrowed wholesale from a different target experiment does not transfer.** `vs_gate_e1_threshold=0.85`/`e2_threshold=0.85` was calibrated in V3-EXQ-490b for whatever stream *that* experiment needed staled; here it happens to sit below `z_beta`'s typical V_s but above `z_harm_a`'s — so the "held" budget lands entirely on the wrong stream. The gate's own `e1_threshold_per_stream`/`e2_threshold_per_stream` override dicts exist precisely to avoid this and were not used.
2. **An aggregate "any stream held" / "any nonzero sample" precondition is structurally blind to a per-channel or per-cell failure.** Both 862a's P1 and 870a's non-degeneracy check passed while the specific slice each experiment's DV depends on never actually engaged (862a) or was reached in only half the cells (870a).
3. **A `NaN`-filtering list comprehension in an acceptance check silently reduces N without flagging it.** 870a's non-degeneracy check reports `met: true` off 2 of 3 OFF-arm seeds with no record that one seed contributed nothing.
4. **Recording gap, not measurement gap, for 870a's episode-termination diagnosis**: the manifest does not record *why* an episode terminated early (hazard collision vs other `done` conditions) — a re-run should record termination cause per episode so the seed×condition-dependent censoring pattern is diagnosable rather than merely detectable.
5. MECH-480's own execution-strength DV design (routing around SD-032b's committed-action-entropy floor-lock) is validated as sound in principle — this FAIL did not reproduce that known ceiling. The problem is upstream of the DV (survival to the measurement window), not the DV's construct validity.
6. MECH-480 has no formalized `targeted_review_mech_480` literature entry yet, despite a specific paper (Asaoka 2026) already identified — a `/lit-pull` commission would close this cleanly (low priority; not blocking the FAIL diagnosis).

**Granularity-debt recurrence check (Q-040.c only — MECH-480 is a first run, no prior history):** `granularity_debt_cluster.py Q-040` was not run (this session's `REE_assembly` checkout is 44 behind origin with an unrelated dirty tree; running the script against it risks a stale read). By hand: 475b, 862, 862a are three targets on Q-040.c, all reading `non_contributory` (no `weakened`) with three *different* bug classes (PE never computed → consumer weight zero → manipulation never engaged). Per the skill's own rule, a cluster with **no** target reading `weakened` is measurement/instrumentation debt, not granularity debt — the trigger does **not** fire. This is a recurring **instrumentation-debt** pattern on one sub-question, not evidence the claim needs splitting.

**Re-derive brake:** does not fire for either claim. Neither target's `recommended_epistemic_category` is `substrate_ceiling` (both are `measurement_test_design_defect`); R3 excludes non-ceiling non-contributory reads from the brake's count regardless of how many letters have accumulated.

## 7. Repair pathway and recommended routing

Both are `complicated (buildable)` — the fix in each case is a **named, narrowly-scoped instrumentation/threshold correction with no open scientific question**, not a spike and not a substrate build. `recommended_substrate_queue_entry.action: none` for both — `ree_core` itself (dacc.py, vs_rollout_gate.py, the E3 selector, CausalGridWorldV2) all work exactly as documented; the gaps are in the experiment drivers.

**V3-EXQ-862a → `/queue-experiment` same-question letter (862b).** Fix: set `hc.e1_threshold_per_stream = {"z_harm_a": <value calibrated against z_harm_a's own empirical V_s distribution, likely well below 0.85>}` (and the matching `e2_threshold_per_stream`) instead of the blanket 0.85; add a stream-specific P1' precondition asserting `vs_gate_held_e1_z_harm_a + vs_gate_held_e2_z_harm_a > 0` on ≥2/3 ON-arm seeds specifically (not just `vs_gate_total_held`), so the driver self-routes `substrate_not_ready_requeue` rather than burning a full 6-cell budget again if the per-stream threshold still misses.

**V3-EXQ-870a → `/queue-experiment` same-question letter (870b).** Fix: (a) record per-episode termination cause (hazard collision vs other) in the manifest; (b) add a per-cell precondition — minimum fraction of the 20 episodes reaching `switch_step` (e.g. ≥50%) — that self-routes `substrate_not_ready_requeue` when unmet, rather than silently producing `NaN`/defaulted-0.0 DVs; (c) fix the non-degeneracy check to require valid (non-NaN) data from all 3 OFF seeds, or explicitly report `n_valid_seeds` alongside `met`; (d) consider whether hazard density/placement or episode length needs adjusting so agents reliably survive to the post-switch window, and/or whether a magnitude-based (not sign-only) displacement DV would be more sensitive to genuine but small outcome-sensitivity effects.

Draft `evidence_quality_note` text for governance (per target, for `claims.yaml`):

> **Q-040** — `[2026-08-03 failure_autopsy, V3-EXQ-862a, confirmed]`: 862a fixed both prior config bugs (475b's z_harm_a wiring, 862's dacc_weight=0 consumer gain) and both preconditions pass, but the ON/OFF manipulation itself never engaged: code-verified (`vs_gate_held_e1/e2_z_harm_a = 0` across all 3 seeds), the borrowed 490b threshold (0.85, applied globally) never crosses for `z_harm_a`'s own V_s — the ON arm's held-budget lands entirely on `z_beta` instead. PE and bias-magnitude series are bit-identical between arms per seed. `non_contributory` — this is a third, independent manipulation-check gap, not a substrate finding; Q-040.c's mechanism-quantification question remains untested. Route: same-question letter (862b) with per-stream threshold calibration + a `z_harm_a`-specific engagement precondition.

> **MECH-480** — `[2026-08-03 failure_autopsy, V3-EXQ-870a, confirmed]`: first V3 run. FAIL is a design/measurement gap, not evidence against the dissociation hypothesis: in 3/6 seed×arm cells, evaluation episodes terminate (mean 8-20 of 80 steps) well before the contingency switch at step 40, leaving `execution_strength=NaN` and near-zero post-switch data; the design's only non-degeneracy check silently passes on 2/3 (not 3/3) OFF seeds due to NaN-filtering. In the 3 well-powered cells, `post_switch_toward_new_frac` reads near-zero regardless of arm — a floor effect that may reflect either genuine replanning-stickiness or DV insensitivity, but the censored cells never had a chance to inform C1 at all. `non_contributory`. The execution-strength DV design itself (avoiding SD-032b/MECH-260's committed-action-entropy floor-lock) is validated as sound — this FAIL does not reproduce that known ceiling. Route: same-question letter (870b) with a per-cell switch-step-reached precondition and termination-cause recording.

## 8. Interactive gate (STOP — awaiting user confirmation)

Presenting to the user in this session's chat response: facts, claim-layer mapping, four-layer table, cluster read, and the two draft `evidence_direction: non_contributory` / `epistemic_category: measurement_test_design_defect` recommendations with routing to same-question letters 862b / 870b. Awaiting confirmation or redirection before `/governance` applies anything to `claims.yaml` / `review_tracker.json`.
