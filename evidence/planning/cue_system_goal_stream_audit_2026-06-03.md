# Cue-System / Goal-Stream Audit -- where does the goal-to-action loop fail?

**Generated:** 2026-06-03T05:57:44Z
**Session:** cue-system-goal-stream-audit-20260603T055744Z
**Scope:** MECH-295 drive->liking->approach cue system, read against the SD-054
scaffolded-onboarding goal-stream failure family (603e/622/626a/603d) AND the
gap4 MECH-295 cascade lineage (490i/490j/493).
**Status:** read-only audit + routing recommendation (Route A). NO claims.yaml /
manifest / evidence_direction / review_tracker / substrate_queue / experiment_queue
edits. NO ree-v3 code change.
**Central question:** Across 603e, 622, 626a, 603d, and the MECH-295 bridge
lineage, where does the goal-to-action loop break?

---

## 0. One-paragraph answer

The break point is **regime-dependent (Lmix)**, and the two regimes have been
conflated in framing. In the **scaffolded-onboarding family (603e / 626 / 626a /
591 / 603a-d)** the loop fails at **Layer A (goal representation): z_goal is
absent**, so the cue layer is *not evaluable at all* (`bridge_cue_fires = 0` on
every arm of 603e because `goal_state` is inactive / `z_goal_norm = 0`). That
absence is downstream of survival/foraging-competence + benefit-input starvation
-- the prerequisite gap the 2026-06-03 cluster autopsy already routed to an
`implement-substrate` AMEND. In the **gap4 cascade family (490j, drive_floor=0.9,
z_goal active)** the loop gets much further: z_goal forms, **the MECH-295 cue side
fires** (`bridge_cue_fires` 138-592), and **the cue bias reaches scoring**
(`approach_cue_score_bias_peak` 0.05-0.43). There the break is at **Layer E
(behavioural expression): `approach_commit_rate` is degenerate (=1.0 in BOTH the
intact and severed-bridge arms)**, so approach occurs by parallel pathways even
with the bridge cut -- which already drove the 2026-05-31 claim narrowing
(necessity -> modulation). The **genuinely unresolved** question is at **Layer C
(cue-to-score-bias authority)**: 490j proved the cue fires and reaches scoring but
could *not* prove it changes the **selected** action, because (a)
`approach_commit_rate` saturates, (b) `dacc_bias_nonzero_steps = 0` so there was no
competing-bias magnitude to compare against, and (c) no selected-candidate-proximity
readout exists. The cue system's *firing* is proven; its *behavioural authority*
is not. That is a measurement/instrumentation gap, not a wiring bug.

---

## 1. Artefact map

| Artefact | Role | Key fact carried |
|---|---|---|
| `v3_exq_603e_..._scaffolded_sd054_20260603T040310Z_v3.json` | **primary** | corrected re-issue of 603d; FAIL / non_contributory / SUBSTRATE_FAILURE; `z_goal_norm_peak=0.0` on all 15 cells; `bridge_cue_fires=0` on all arms; c4_z_goal_engaged=false; c5_h_pos_coverage=false |
| `v3_exq_490j_..._severed_bridge_baseline_20260531T112417Z_v3.json` | **primary** | the cue-EVALUABLE run; gap4 substrate, z_goal active (goal_active_fraction=1.0); cue fires + reaches scoring; `approach_commit_rate=1.0` in BOTH arms; FAIL / weakens; drove MECH-295 necessity->modulation narrowing |
| `v3_exq_490i_..._gap4_tier1_20260530T184434Z_v3.json` | lineage/context | predecessor of 490j; ARM_0 baseline contamination + uncalibrated cross-seed budgets (why 490j fixed the harness) |
| `v3_exq_493_..._liking_bridge_validation_20260427T080304Z_v3.json` | lineage/context | MECH-295 substrate-landing isolation; evidence_direction=supports; UC1-UC6 PASS (write-side fires, cue-side monotone-negative bias, severed-bridge collapse to 0); diagnostic |
| `v3_exq_622_..._goal_stream_staged_sd054_20260531T223804Z_v3.json` | **primary** (per brief) | staged S0-S3 decomposition; S0 PASS (z_goal trainable in isolation), S1+ FAIL (z_goal persistence collapses under anneal); superseded by 621a; claim_ids=[] |
| `v3_exq_626a_..._developmental_window_diagnostic_20260601T201354Z_v3.json` | lineage/context | P0 positive control forms z_goal on only 1/3 seeds (seed 44=0.19); formation is foraging-gated; claim_ids=[] |
| `v3_exq_626_..._developmental_window_diagnostic_20260601T152729Z_v3.json` | appendix | predecessor of 626a; omitted update_z_goal (z_goal zero everywhere; harness bug) |
| `failure_autopsy_V3-EXQ-603d_2026-06-01.md` | lineage/context | found scheduler never called update_z_goal (Class-1 wiring artifact); routed the AMEND that produced 603e |
| `failure_autopsy_V3-EXQ-622_2026-06-01.md` | lineage/context | localised 622 to z_goal persistence under anneal/risk, not absence of goal feed |
| `failure_autopsy_V3-EXQ-603e-626a-622_2026-06-03.md` | **primary** (sibling, this morning) | terminal cluster diagnosis: z_goal=0 downstream of survival/foraging-competence + benefit-input starvation; wiring layer CLOSED+verified; routed implement-substrate AMEND |
| `mech_295_drive_liking_approach_bridge.md` | reference (design) | weak-reading commitment; cue-side gain = f(drive * goal_proximity); severed-bridge falsifier; gates min_drive_to_fire / min_z_goal_norm_to_fire |
| `goal_pipeline_plan.md` (GAP-4) | reference (plan-of-record) | GAP-4 owns MECH-295 cascade behavioural validation; 490 cohort runs on gap4 substrate where z_goal IS active; explicitly NOT the prereq-(2) z_goal-collapse owner |
| `sd_054_scaffolded_onboarding_substrate_design.md` | reference (plan-of-record) | scaffolded onboarding owns prereq (2) (z_goal in default-ish config); AMEND 2026-06-02 wired update_z_goal |
| `ree-v3/ree_core/agent.py` select_action (lines 3550-3646) | reference (code) | cue wiring verified intact: m295_bias from cand_proximities -> added to dacc_score_bias -> e3.select |
| `ree-v3/ree_core/regulators/mech295_liking_bridge.py` | reference (code) | compute_approach_cue_score_bias gates: simulation_mode / gain==0 / drive<min_drive_to_fire (default 0.01); cue side fires on drive*candidate_proximities |

---

## 2. Evidence table (per key run)

Legend: Y=yes, N=no, P=partial, U=unknown. "Cue evaluable?" = is the MECH-295 cue
path in a state where its behaviour can be read at all.

| Run | regime | z_goal formed? | z_goal persisted? | goal_state active? | bridge_cue_fires>0? | approach_commit_rate>0? | candidate proximity instrumented? | MECH-295 score-bias instrumented? | action diversity adequate? | cue evaluable? | interpretation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **603e** | scaffolded onboarding (hfa=0.7) | N (peak 0.0 all 15 cells) | N/A | N (z_goal_enabled set, but z_goal never seeded ecologically) | N (0 all arms) | partial (ARM_2/3 entropy 0.70; approach not recorded) | N | N | P (entropy 0.70 in 2 arms; argmax-collapse elsewhere) | **N (L0)** | substrate_failure label is upstream input-starvation; cue not testable |
| **626a** | developmental-window P0 control | P (1/3 seeds; seed44=0.19) | N | P (only seed 44) | U (not recorded) | U | N | N | U | **N (L0, 2/3 seeds)** | ecological z_goal formation is foraging-gated |
| **622** | staged S0-S3 curriculum | Y at S0 (peak 0.28-0.44) | N (collapses 1-6 OOM at S1) | Y at S0 | partial (S0 bridge_fires/ep 4.6-17.5) | N (approach_commit_rate=0 at S0-S2; =1.0 at S3 with z_goal~1e-14) | N | N | U | **P (S0 only)** | goal feed works in isolation; persistence collapses under anneal -> cue loses its input |
| **490j ARM_1** (gap4, intact) | gap4 (drive_floor=0.9) | Y (goal_norm_peak 0.09-0.30) | Y (goal_active_fraction=1.0) | Y | **Y (138 / 592 / 178)** | Y (=1.0, saturated) | N (proximities computed, not exposed) | **Y** (cue peak 0.05/0.43; calls 150-885; write peak 0.0066-0.29) | P (action_entropy 0.14-0.71; one seed monostrategy) | **Y** | cue fires + reaches scoring; behavioural effect unmeasurable (approach saturates) |
| **490j ARM_0** (severed bridge) | gap4, z_goal_enabled=False | N (goal_active_fraction=0) | N | N | N (0) | N | Y (zero baseline, sentinel clean) | Y (zero) | P | Y (as control) | severed bridge baseline clean; **approach_commit_rate STILL =1.0** -> approach by other means |
| **493** (isolation) | forced drive/benefit | Y (forced) | N/A | Y | Y (UC3/UC4) | N/A (unit probe) | Y (UC4 monotone prox->bias) | Y (UC4/UC5) | N/A | Y (isolated) | bridge wired correctly in isolation; severed-bridge collapse confirmed (UC5) |

Key cross-run reading: **603e/626a/622 sit at L0/persistence (z_goal absent or
collapsing -> cue uninstrumentable ecologically), while 490j is the ONE run where
z_goal was reliably active and the cue was therefore actually exercised.** Any
statement about MECH-295 cue authority must be made from 490j/493, not from the
z_goal=0 family.

---

## 3. Failure localisation

Per-regime classification against the L0-L5 ladder:

| Regime | Layer | Evidence |
|---|---|---|
| 603e / 626 / 626a / 591 / 603a-d | **L0** -- upstream z_goal absent, cue layer not evaluable | z_goal_norm_peak=0.0 (603e all 15 cells); bridge_cue_fires=0; 626a forms z_goal 1/3 seeds; root cause survival/foraging-competence + benefit starvation (cluster autopsy 2026-06-03) |
| 622 | **L0->persistence boundary** -- z_goal forms (S0) then collapses (S1+) before the cascade regime is reached | S0 z_goal 0.28-0.44 PASS; S1 median z_goal 0.0089/0.0465/1.3e-6 FAIL under drive_floor anneal 0.9->0.2 + mild hazard |
| 490j (gap4) | **NOT L0/L1/L2** -- z_goal active, cue fires (L1 cleared), cue bias reaches scoring (L2 cleared). Break is at **L5** (behavioural metric degenerate) with the **C/L4 authority question unmeasured** | cue fires 138-592; score-bias peak 0.05-0.43 reaches dacc_score_bias; approach_commit_rate=1.0 in BOTH arms (L5 degenerate); dacc_bias=0 + no selected-proximity readout (C/L4 unmeasured) |

**Overall: Lmix.** The system is L0 in the scaffolded-onboarding regime
(where most recent FAILs live) and simultaneously, in the gap4 regime where the
cue IS evaluable, it clears L1+L2 but stalls at an **unmeasured Layer C/L4
(does the cue bias change the SELECTED candidate?)** masked by a degenerate Layer
E metric. The two are not in conflict: they are different regimes, and the gap4
regime is the only one that can currently test cue authority.

---

## 4. Specific current hypothesis (stated, with the prior weighed)

The session prior was:

> "Natural z_goal formation/persistence is still too fragile, so MECH-295 is often
> not evaluable in 603e-like conditions; however, the cue system also needs explicit
> authority instrumentation because prior isolation PASS does not prove natural
> cue-to-E3 behavioural authority."

**The audit supports this prior, and sharpens both halves with the 490j evidence:**

1. **Fragility half -- confirmed and located.** In the scaffolded-onboarding regime
   z_goal is absent/collapsing (603e=0; 626a 1/3 seeds; 622 collapses at S1), so
   MECH-295 is genuinely not evaluable there (`bridge_cue_fires=0`). This is owned
   upstream (survival/foraging-competence + benefit-input AMEND already routed by
   the 2026-06-03 cluster autopsy) and is NOT a cue-system defect.

2. **Authority half -- confirmed, and now precisely scoped.** 490j is the proof that
   "isolation PASS (493) does not establish natural behavioural authority": on the
   gap4 substrate where z_goal IS active, the cue *fires* and its bias *reaches
   scoring*, yet the behavioural necessity test FAILED (approach_commit_rate=1.0 in
   both intact and severed arms) -- forcing the 2026-05-31 narrowing of MECH-295
   from necessity to modulation. The open question is no longer "does the cue
   fire?" (yes) or "does the bias reach E3?" (yes) but **"does the cue bias change
   the SELECTED candidate's proximity, and is its magnitude competitive with the
   other score-bias channels?"** -- which 490j could not answer because
   `dacc_bias_nonzero_steps=0` (no competitor to compare against) and there was no
   selected-candidate-proximity readout. That is a missing-instrumentation gap, not
   a wiring bug (agent.py select_action wiring verified intact; 490j proves the cue
   path is live).

---

## 5. Do-not-overclaim ledger (explicit)

- **MECH-295 is NOT weakened by 603e's z_goal=0.** 603e is non_contributory /
  SUBSTRATE_FAILURE with `bridge_cue_fires=0` because the goal representation was
  never active; the cue had nothing to act on. This is not evidence about the cue.
- **The cue system is NOT marked failed.** In the only regime where it is
  evaluable (490j), it fires and reaches scoring. Its *behavioural authority* is
  unproven, which is different from failed.
- **The goal stream is NOT globally dead.** 622 S0 PASS (z_goal trainable in
  isolation) and 490j goal_active_fraction=1.0 both show the stream can be active.
- **603e is NOT treated as claim-weighting evidence.** It is diagnostic /
  non_contributory; this audit does not convert it into any claim delta.
- **490j's existing `weakens` tag is NOT re-litigated here.** It was applied
  2026-05-31 at the behavioural-necessity layer with the narrowing already recorded
  in claims.yaml; this audit neither strengthens nor reverses it. It is cited only
  to locate the open authority question.
- **No claims.yaml edit in this phase.** (Governance constraint.)

---

## 6. Phase 2 -- routing decision: **Route A** (queue a minimal cue-authority diagnostic)

**Why not the other routes:**

- **Not Route C (substrate amend).** The audit found no wiring bug. agent.py
  select_action (lines 3550-3646) computes `m295_bias` from `cand_proximities`,
  optionally adds the MECH-307 conjunction read, and composes it additively into
  `dacc_score_bias` which is passed to `e3.select`. 490j empirically confirms the
  path is live (`bridge_cue_fires` and `approach_cue_score_bias_calls` both
  non-zero; severed-bridge arm cleanly zero). The master flag, goal-gate, drive
  floor (0.01) and z_goal-norm floor (0.05) are all consistent with the gap4 regime
  where z_goal_norm 0.09-0.30 clears the floor. No threshold mismatch, no
  off/simulation suppression, no candidate-shape bug surfaced.
- **Not Route B (instrumentation-only in ree_core).** The missing telemetry
  (selected-candidate proximity, candidate-proximity distribution, competing-bias
  magnitudes) is capturable **experiment-side** with the exact eval-time
  monkeypatch/probe pattern 490j already used to record the bridge magnitudes (490j
  `design_notes.direct_bridge_magnitude_probe`). A core change is not required and
  would be larger blast radius than warranted.
- **Not Route D (defer entirely).** The scaffolded-onboarding *regime* is blocked
  (Section 7 records that), but the cue authority question is testable *now* in the
  gap4 regime where z_goal is reliably active. Deferring everything would leave the
  load-bearing authority question (which already narrowed the claim once) unanswered
  for no reason.

**Route A is preferred per the brief** ("the best output may be a clean audit plus
a tiny diagnostic proposal"): a minimal cue-authority diagnostic that holds
z_goal/drive/candidates under controlled gap4-like conditions, adds the
selection-level instrumentation 490j lacked, and isolates cue authority without
re-testing the whole goal pipeline.

> NOTE: per CLAUDE.md mandatory-skill-path, the actual experiment script + queue
> entry MUST be created via `/queue-experiment`. This document provides the
> **proposal text + skeleton only**; it does NOT write to `ree-v3/experiments/`
> or `experiment_queue.json`.

---

## 7. Blocked regime (recorded, not actioned here)

The **scaffolded-onboarding regime** cue work is blocked until
`scaffolded_sd054_onboarding` goal persistence is amended and revalidated.
**Exact unblock condition:** the 2026-06-03 cluster-autopsy AMEND lands a P0/P1
survival/foraging scaffold reaching >= 2/3 foraging-competent seeds AND a
forced-benefit Stage-0 z_goal warmup, and the re-issue (603f) shows
`z_goal_norm_peak > 0.4` AND `bridge_cue_fires > 0` on >= 2/3 seeds in P2. Until
then, any ecological MECH-295 read in that regime returns `bridge_cue_fires=0` and
is non_contributory by construction. V3-EXQ-631 (below) deliberately uses the
**gap4 regime** (drive_floor=0.9) instead, where z_goal is reliably active, so it
is NOT blocked on the scaffolded-onboarding AMEND.

---

## 8. V3-EXQ-631 -- cue-authority diagnostic PROPOSAL (Route A)

ID check: `631` is free -- no script `v3_exq_631_*` exists (only 630), no queue
entry, no `claim:`/`queue:` history references it; it was pre-allocated once on
2026-06-02 for a MECH-342 follow-on but that work landed as V3-EXQ-629 and 631 was
explicitly DEFERRED/freed (see commitment_closure_plan governance_2026_06_02b note
and TASK_CLAIMS plan-gap4-drift-629 completion note).

**Title:** `V3-EXQ-631 MECH-295 cue-authority diagnostic (selection-level, gap4 z_goal-active)`
**experiment_purpose:** `diagnostic` (NOT evidence; does NOT weight claims by default)
**claim_ids:** `[]` (diagnostic; isolates cue authority, does not adjudicate MECH-295)
**machine_affinity:** `any`
**priority:** above 614d (set above the current max so the draining fleet picks it up)
**predecessor (not supersedes):** V3-EXQ-490j (490j is `weakens`/evidence on the
necessity claim; 631 is a diagnostic on the *authority/measurement* gap 490j exposed)

**Design (3 arms minimum, 3 seeds, gap4 operating config drive_floor=0.9 +
use_mech295_liking_bridge=True + use_dacc=True so a competing bias exists to
compare against -- closing the 490j dacc_bias=0 gap):**

1. **ARM_0_severed_bridge** -- `mech295_liking_to_approach_cue_gain=0.0` (cue side
   cut; write side intact), gap4 substrate. Reproduces 490j ARM_0 baseline.
2. **ARM_1_cue_on_natural** -- full gap4 operating bridge with natural z_goal (as
   490j ARM_1). The cue-ON-with-natural-z_goal arm.
3. **ARM_2_cue_on_controlled_zgoal** -- POSITIVE CONTROL: forced supra-threshold
   z_goal/drive (the `test_c6`-style forced `_benefit_and_drive` seeding) so cue
   authority is testable even on seeds where natural z_goal is weak. Guarantees a
   non-degenerate candidate-proximity surface.

**Mandatory INVALID_HARNESS / non_contributory branch:** if `goal_state` is
inactive OR `candidate_proximity` has zero variance in > 1/3 seeds OR the MECH-295
cue path is not instantiated, route the manifest to `non_contributory`
(`interpretation_label=INVALID_HARNESS`) -- do NOT emit a FAIL that could be read
as cue-system falsification (the 603e lesson).

**New telemetry the diagnostic MUST record (the 490j gap), capturable
experiment-side via the 490j monkeypatch/probe pattern -- no ree_core change):**

- `goal_state.is_active` per measurement tick + `z_goal_norm` per tick.
- `effective_drive` used by MECH-295 (post-pACC `eff_drive_m295`).
- bridge write-side value per tick (already in 490j: `mech295_anticipatory_liking_write_*`).
- cue-side `m295_bias` summary: min/max/mean + **nonzero fraction** (per arm).
- **candidate_proximity distribution: min/max/mean/std** (NEW vs 490j).
- **competing score-bias magnitudes: dACC, OFC, lateral_pfc, MECH-295, harm,
  base E3 score** -- captured from the agent's `_dacc_last_bias` / score-decomp
  caches (NEW vs 490j; the load-bearing Layer-C readout).
- **selected candidate proximity** (proximity of the candidate E3 actually picked)
  vs pool mean proximity (NEW vs 490j; the Layer-C3/L4 readout).
- whether `e3.select` received the combined `score_bias` (assert non-None when
  cue is ON).

**Pre-registered acceptance gates (diagnostic; informative not claim-weighting):**

- **C0 evaluability:** goal_state active OR controlled-z_goal positive-control
  active; `candidate_proximity` non-zero variance in >= 2/3 seeds; MECH-295 cue
  path instantiated + telemetry present. (FAIL C0 -> INVALID_HARNESS / non_contributory.)
- **C1 cue fires:** MECH-295 cue-side nonzero fraction > 0 in cue-ON arms;
  cue-side bias magnitude differs from ARM_0_severed_bridge.
- **C2 cue reaches scoring:** combined `score_bias` shifts in the expected
  direction (more negative = more attractive) for high-proximity candidates.
- **C3 selection-level effect:** selected-candidate proximity higher in cue-ON
  arms than in ARM_0_severed_bridge by a pre-registered margin (the new
  load-bearing test 490j could not run).
- **C4 behavioural sanity (informative, NOT decisive):** approach_commit_rate or
  movement-toward-target changes in the expected direction. **Failure here alone
  does not falsify cue authority if C1-C3 pass** -- because 490j already showed
  approach_commit_rate is a degenerate/saturated metric contaminated by parallel
  approach pathways.

**Interpretation grid (one row per plausible outcome -> next action):**

| Outcome | Reading | Next action |
|---|---|---|
| C0 fails | cue not evaluable even in gap4 + positive control | route INVALID_HARNESS; escalate to /failure-autopsy on candidate-proximity degeneracy |
| C0-C2 pass, C3 fails | cue fires + reaches scoring but does NOT change the selected action -> bias is numerically swamped or applied to the wrong candidate set | /governance: this is the load-bearing evidence that MECH-295's modulation is sub-threshold at E3; consider score-bias scaling or candidate-set audit (NOT a behavioural re-sweep) |
| C0-C3 pass, C4 fails | cue HAS selection-level authority but behaviour masked by monostrategy/parallel pathways | confirms the 490j degeneracy reading; authority established at selection layer; behavioural test needs diversity substrate (ARC-065/SD-056), not a cue fix |
| C0-C4 pass | cue authority established end-to-end | /governance: candidate evidence to revisit the 2026-05-31 necessity->modulation narrowing |

**Diagnostic constraints honoured:** isolates cue authority (does not re-test goal
pipeline persistence, harm, commitment, or behavioural diversity jointly);
diagnostic purpose; claim_ids=[] (no default claim weighting); INVALID_HARNESS
branch present; reports whether cue-side bias reaches E3 and whether selected
candidate proximity increases; does not rely solely on approach_commit_rate.

**Script skeleton:** intentionally NOT written here (deferred to /queue-experiment,
which runs the mandatory code-review + smoke-test pass). The harness is a direct
fork of `v3_exq_490j_mech295_cascade_gap4_tier1_severed_bridge_baseline.py`
(same gap4 config, same severed-bridge ARM_0, same eval-time bridge-compute
monkeypatch) + the three new telemetry readouts above + ARM_2 forced-z_goal
positive control + the C0 INVALID_HARNESS guard.

---

## 9. Summary of session outputs

- **Files read:** 603e manifest; 603d/622/603e-626a-622 autopsies; sd_054
  onboarding design; goal_pipeline_plan (GAP-4); mech_295 bridge design;
  490j/490i/493/626a manifests; agent.py select_action cue wiring;
  mech295_liking_bridge.py config + cue method.
- **Route:** **A** -- queue a minimal cue-authority diagnostic (V3-EXQ-631).
- **Cue system currently evaluable?** Only in the gap4 regime (490j). NOT in the
  scaffolded-onboarding regime (z_goal=0). In gap4 it fires + reaches scoring;
  its selection-level authority is unmeasured.
- **Code changed?** No.
- **New experiment queued?** No -- a V3-EXQ-631 **proposal** is recorded here;
  actual queuing is deferred to `/queue-experiment` per the mandatory skill path.
- **Exact remaining blocker:** (a) cue-authority resolution is blocked on running
  V3-EXQ-631 (Layer-C selection-level instrumentation never collected); (b) the
  scaffolded-onboarding-regime cue read is blocked on the 2026-06-03 cluster-autopsy
  AMEND (survival/foraging-competence + forced-benefit Stage-0 z_goal warmup ->
  603f shows z_goal_norm_peak>0.4 AND bridge_cue_fires>0 on >=2/3 seeds).
