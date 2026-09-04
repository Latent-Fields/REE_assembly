# STAGED (not applied): `/thought-digestion v3-closure` -- 2026-09-04 unattended campaign

**Status: AWAITING USER REVIEW. Nothing in this file has been written to `claims.yaml`.**

**Started:** 2026-09-04T21:02:59Z · **Session:** `thought-digestion-v3-20260904` (Mac, main checkout, no worktree)
**Mode:** unattended / staged-for-review, GROUPED (wave-of-groups, edge-first, `cap=5 floor=3.0`, lettered
families atomic, a group edge must include at least one STRUCTURAL signal -- token overlap alone never
reaches the floor). Draft-only: every wave's agent output is appended here verbatim; the user reviews the
whole batch once and the orchestrator applies only what is approved, then `build_claims_json.py` + commit.

**Deviation from the skill, stated plainly:** the skill's generic "Unattended / overnight mode" says to
stage to an untracked scratch file. This campaign stages to THIS tracked file instead, committed
pathspec-limited under the session's own TASK_CLAIMS entry, because untracked staging was lost once before
(chip-20260807-thoughtdigestion-trial-5: worktree GC'd before the drafts were read). The pattern follows
`thought_digestion_staged_2026-08-08_trial2_5claims.md`.

**Scope:** `closure_status.md` "Remaining work to close v3" (33) + "Assembly frontier" (10) -> 41 core
claim ids, expanded one hop along `depends_on` (240), intersected with the undigested backlog
(no `what_would_answer`, no `digestion_note`, `implementation_phase` not in v4/v5/v6/post_v5), plus
lettered-family closure -> **47 claims in 21 groups (10 solos)**. Wave 1 of 2026-08-27 (17 claims,
REE_assembly 25c05dbd6e) is already applied and therefore excluded.

**Prior drafts found and handed to agents (extract-before-invent):** MECH-485 (loop branch
`thought-loop/digestion-2026-08-25`, with the user's own `human_review_note`); ARC-113 (pilot wave
`thought_digestion_v3closure_wave1_drafts_20260826.md`, never applied).

| group | members | fan-in | why grouped |
|---|---|---|---|
| G1 | MECH-181, MECH-353, MECH-354, SD-017, SD-083 | 24 | SD-017 sleep-phase hub: SD-083/MECH-354/MECH-181 all `depends_on` it; MECH-353~354 same batch + namespace |
| G2 | MECH-074, MECH-074a-d | 8 | lettered family (amygdala read/write head split) -- atomic |
| G3 | MECH-104, MECH-106, MECH-234, MECH-250, SD-105 | 2 | control-plane commitment namespace; 104->106 `depends_on`; interrupt/release/entropy-floor siblings |
| G4 | ARC-048, INV-057, MECH-182, MECH-192 | 5 | ARC-048->MECH-192 `depends_on`; signal-legibility namespace |
| G5 | ARC-120, ARC-121, SD-034 | 12 | ARC-121->SD-034 `depends_on`; earned-authority / shared epistemic state |
| G6 | MECH-294, MECH-341, MECH-442 | 11 | MECH-442 `depends_on` both; action-diversity through commit |
| G7 | MECH-206, MECH-288, SD-084 | 10 | MECH-288->SD-084 `depends_on`; hippocampal comparator / event-segment |
| G8 | ARC-057, SD-024, SD-025 | 8 | SD-024<->SD-025 and ARC-057->SD-025 `depends_on`; DA / curiosity |
| G9 | MECH-349, MECH-527 | 3 | rule-mint / attractor-escape namespace |
| G10 | ARC-061, SD-047 | 1 | ARC-061->SD-047 `depends_on`; reafference comparators |
| G11 | ARC-029, MECH-025b (+MECH-025 read-only context) | 0 | committed/uncommitted modes namespace |
| solos | MECH-273, MECH-258, MECH-485, ARC-113, ARC-037, INV-104, INV-063, MECH-332, MECH-474, SD-063 | -- | no structural edge >= floor to any other undigested claim |

---

## GOVERNANCE FLAGS (collected across waves -- read these FIRST)

_(appended as waves land)_

---

## GROUP REPORTS (appended as they land; verbatim agent output)

---

<!-- G2 appended 2026-09-04T21:17:34Z -->
## G2 -- MECH-074 lettered family (amygdala as read/write head for the valenced hippocampal map)  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the group brief says a lettered family is atomic and that the key question is whether the parent MECH-074 is now a pure index. **My view: it is NOT.** The parent carries a residual assertion of its own -- that the head's authority over the hippocampal map *decomposes into two independently sufficient routes* (write-STRENGTH and write-ADDRESS) -- and that assertion has been directly tested. `V3-EXQ-888` (2026-08-04, PASS/supports, 3/3 seeds, non-degenerate) registers `C1_head_authority` and `C4_separability` against **MECH-074 itself**, with `C3` alone against MECH-074a and `C2` alone against MECH-074b (`evidence/experiments/v3_exq_888_mech074_readwrite_head_route_dissociation_20260804T075257Z_v3.json`, `criteria[].claim`; `combination_rule`: "C4 (separability) is the load-bearing criterion for the PARENT claim MECH-074"). So disposition (e)/(g) is **wrong** for the parent: it has its own falsifier, its own criteria, and `claim_evidence.v1.json` gives it `genuine_exp_count: 1, exp_conf 0.705, evidence_quadrant confirmed_established`. What it does *not* have is any residual role as an evidence router -- the routing job named in its `evidence_quality_note` is done.

- **(i) same-claim / merge candidates:** **none.** MECH-074a and MECH-074b were the plausible merge pair (both are "BLA biases which traces win"), and the merge is empirically refuted rather than merely judged unlikely: 888's four-arm design isolates them (`ARM_TAG_OFF` = arousal tag off, encoding gain live -> strength route only -> MECH-074a; `ARM_GAIN_FLAT` = gain flattened, per-trace tags live -> address route only -> MECH-074b) and **both single-route arms independently clear the margin on 3/3 seeds** (address-route delta vs OFF 0.1506 / 0.0909 / 0.1061; strength-route delta vs OFF 0.3249 / 0.1769 / 0.2491; margin 0.03; OFF arm flat, |AOR_z| <= 0.0107). Two routes, separately sufficient -- do not merge. MECH-074c is a different module (CeAAnalog, scalar/fast) and MECH-074d a different operation (remap), no merge pressure. The one *outward* merge pressure worth naming is MECH-074d <-> **MECH-153** (see (iv)), and it is a dependency, not a merge.

- **(ii) contradictions / undercut premises:**
  1. **MECH-074b's own load-bearing literature now partially undercuts its locus.** A targeted review landed 2026-08-07 (`evidence/literature/targeted_review_mech_074b/`, 4 entries, none of them in the claim's `source` list) and one entry is scored **mixed/weakening**: Roozendaal & McGaugh 2011 -- "the best-established amygdala memory effect is on CONSOLIDATION ... at RETRIEVAL the amygdala/glucocorticoid effect is documented as IMPAIRING, not a positive per-trace enhancement" (`entries/2026-08-07_mech_074b_consolidation_vs_retrieval_roozendaal2011/record.json`, confidence 0.62). That is a locus dispute *between MECH-074b and MECH-074a*: the same paper is MECH-074a's top citation and supports it. It does not refute 074b (888 shows the address route has real in-substrate authority), but 074b's registered claim of a *retrieval-time* per-trace weight now carries a named literature cost that its block does not record.
  2. **MECH-074b's premise depends on MECH-074a's write path.** `w_i = 1 + alpha * arousal_tag_i` is undefined if the encoding-time tag is never written (`bla_retrieval_tag_at_encoding`, default True, exposed as False specifically to reproduce the named scalar-failure signature -- `ree_core/amygdala/bla.py:187-191`). A 074b null is uninterpretable unless the tag-write precondition is reported green; 888 reports it as `address_route_nonuniform` (retrieval_bias range 0.429 vs floor 0.01).
  3. **MECH-074c's selectivity leg is undercut by its own substrate.** `CeAAnalog.tick()` is a pure function of `||LowFreq(z_harm_a)||_1 / n` (`ree_core/amygdala/cea.py`, "Selectivity constraint" docstring: "because z_harm_a is the SD-011 affective stream, magnitude there IS affective valence load"). So "must fire on harm-affective valence, not generic arousal" cannot be a property of this module -- a magnitude-matched non-harm drive fires identically **by arithmetic**. V3-EXQ-895 recorded exactly this (`interpretation.selectivity_leg.why_not_gated`, DV-symmetry artifact class). MECH-074c is therefore a **fused claim**: legs 1-2 + fast:slow are REE/CeA legs; leg 3 is an SD-011 encoder leg wearing a CeA label.

- **(iii) shared falsifier:** **yes -- V3-EXQ-888's route-dissociation instrument is the family's shared falsification apparatus for the parent, 074a and 074b, and its precondition block should be cross-referenced rather than re-derived.** The five readiness gates are: `n_traces_sufficient` (>= 8; measured 40), `gt_arousal_spread` (buffer std of the ground-truth arousal label >= 0.02; measured 0.067-0.097 -- **the single statistic every AOR routes on**, since all four AORs are differences of means of `gt_arousal`, so zero spread forces every AOR to 0 no matter how the sample is weighted), `buffer_gt_alignment` (== 1.0), `strength_route_nonuniform` (memory_strength range >= 0.05; measured 1.07), `address_route_nonuniform` (retrieval_bias range >= 0.01; measured 0.429), plus the `OFF_AOR_Z_FLAT_MAX <= 0.02` instrument control. MECH-074b's and MECH-074a's drafts below point at this block instead of restating it.

- **(iv) cross-cutting finding:** **three, and the third is the most consequential thing in this report.**
  1. *Confound now RESOLVED, and must not be re-introduced.* The strength/address confound between 074a and 074b was real (before 888, a single-arm ON/OFF result on either claim was uninterpretable because both routes move the same DV). 888's 2x2 dissolved it. **Any future 074a or 074b run must keep both single-route arms**; a two-arm ON/OFF successor would silently re-create the confound.
  2. *Confound LIVE, and it invalidates the embodied reading of MECH-074c.* In the only embodied measurement of the CeA fast route (895's non-gating `SELECTIVITY_PROBE`, 4 seeds, 2044 ticks), **`embodied_fire_count = 0` on every seed**, with `lf_harm_max = 0.216` against `cea_fast_route_threshold = 0.5`. All five of 895's gated criteria (C1-C5) therefore come from **driven/synthetic arms**; in the live loop `fast_prime` is identically zero. MECH-074c's `provisional` status rests on a mechanism that has never fired in an embodied run. This is the family's largest non-degeneracy hazard and is the first line of 074c's draft below.
  3. *MECH-074d's four-fold failure is a KNOWN, ALREADY-REGISTERED precondition failure owned by another claim.* 894c's decisive reading was that within- and cross-context Jaccard were **identical (1.0000 exactly) in 10/15 cells** -- the attribution head selects a deterministic, context-invariant target set. **MECH-153** (candidate, registered 2026-03-31) says precisely this about the input side: "without this objective, hazard-proximate and hazard-distal context vectors remain near-identical (cosine_sim approximately 1.0), leaving the MECH-150 retrieval pathway functionally silent", and adds the framing that matters here -- "**This is an implementation precondition, not a claim that MECH-150 is false.**" The signatures match (0.9999 cosine / 1.0000 Jaccard) and SD-035's own 2026-08-09 addendum already states the mechanism: "the legacy ContextMemory write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, **which defeats ANY attribution rule**". The supervised context-labeling objective MECH-153 requires is **not built** -- no `context_label` / `supervised_context` knob exists anywhere in `ree-v3/ree_core/` (verified with `/usr/bin/grep`), and its own validation run V3-EXQ-504 returned `inconclusive`. So MECH-074d is not a claim whose mechanism failed four times; it is a claim whose *input* has never existed, tested four times.

- **Currency findings (stale notes, landed blockers, unreviewed results):**
  1. **MECH-074 parent `v3_pending: true` is STALE.** Substrate landed 2026-04-21; the parent now has a reviewed, non-degenerate experimental PASS of its own (888). Its `live_status.evidence` still reads `decision:MECH-074@2026-04-25 ... hold_pending_v3_substrate`, and its `evidence_quality_note` still says "v3_pending until BLAAnalog + CeAAnalog substrate lands". Both conditions are discharged.
  2. **888 IS reviewed** -- `review_tracker.json` carries it in **both** `reviewed_run_ids` and `discussed_experiment_dirs`. SD-035's `what_would_answer` (written in the 2026-08-07 digestion pass) still describes it as "STILL PENDING REVIEW as of this digestion pass". Stale.
  3. **MECH-074b `v3_pending: true` is STALE and its `live_status` carries NO evidence block at all**, despite 888's C2 passing 3/3 seeds against it and `claim_evidence.v1.json` giving it `pass_runs 1, exp_conf 0.705, overall 0.794, evidence_quadrant confirmed_established`. Its note's condition ("v3_pending until substrate lands and EXQ-B+ follow-up is queued") is doubly discharged.
  4. **MECH-074b's `source` list is two lit-pulls stale** -- the whole `targeted_review_mech_074b/` (4 entries, 2026-08-07: Mather 2011, Sutherland & Mather 2012, Roozendaal & McGaugh 2011 *mixed*, Adolphs 2001) is absent from the block.
  5. **MECH-074a's note says "this is the first [experimental entry]"** -- there are now **two** (V3-EXQ-659 2026-06-09, V3-EXQ-888 2026-08-04) and the quoted `exp_conf 0.775` has drifted to **0.755**. The promotion gate it names (`exp_conf >= 0.80 AND >= 4 entries`) is still unmet, so the status is right and only the note is wrong.
  6. **SD-035 `metric_trajectory` note "MECH-074b retrieval_bias hippocampal-consumer wiring deferred (substrate produces signal but HippocampalModule does not yet read)" is STALE** -- `HippocampalModule.get_exploration_arousal_tags()` and retrieval_bias-weighted sampling exist (`ree-v3/ree_core/hippocampal/module.py:2920-3021`) and are fed from `ree-v3/ree_core/agent.py:10548` and `:12567`.
  7. **SD-035's data-flow spec is WRONG about one consumer, and this bounds MECH-074b.** The spec says "E3.select (BLA retrieval_bias reweights candidate proposals)". In code the only consumers are `hippocampal.diverse_replay(...)` (gated on `replay_diversity_enabled`, MECH-165) and the REM reverse-replay pass. **`retrieval_bias` never reaches `E3.select`.** So the address route is exercised on the *replay-sampling* path only -- which is exactly what 888 could measure, and is why 888 is a composition result, not a readout result.
  8. **MECH-074c's code pointer is dead**: "urgency interrupt at ree-v3/ree_core/agent.py:869-886" now lands in the `ConditionedSafetyStore` block (agent.py has grown past 12k lines). The deferred migration into `fast_prime` is still not done.
  9. **MECH-074c's "fast:slow ratio out of scope pending SD-032c AIC comparator wiring" is STALE as to the blocker** -- `AICAnalog` exists and is constructed in the agent (`ree_core/cingulate/aic_analog.py`; `agent.py:792-803`, `aic_urgency_threshold`), emitting `aic_salience` + `urgency_signal` per tick. The comparator is now `complicated (buildable)`. The *real* blocker is finding (iv)(2): the CeA gate never fires embodied.
 10. **SD-035's 2026-08-09 addendum's "STILL OWED: the MECH-074d implementation_note in claims.yaml was NOT written" is still owed** -- MECH-074d carries no `implementation_note` field today.
 11. **MECH-074d's owed fix has a live workstream that post-dates 894c but has produced nothing scored against the claim.** `ree-v3 76cbf84` "repair ContextMemory.write() deterministic single-slot fixed point" (2026-08-19), then V3-EXQ-943 (PASS), 946 (PASS, label `context_informative_address_found_at_operating_point`), 956 (FAIL), 969/970 (FAIL, 970 = `h1_content_referencing_objective_not_confirmed_either_regime`), 971, 972 (PASS, label **`h4_supported_representation_undifferentiated`**). **Every one is `evidence_direction: non_contributory` with `claim_ids: null`** -- diagnostics, not evidence, and none tests MECH-074d. The gate is not discharged.
 12. **Nothing from this family is queued.** `ree-v3/experiment_queue.json` holds 3 items (V3-EXQ-1002, 983a, 993a); none touches MECH-074*. The family also does not appear in `docs/CURRENT_FRONT.md` or `evidence/planning/closure_status.md` -- it is off the live closure front, which is priority context for all five dispositions below.

---

### MECH-074 -- Amygdala functions as read/write head for valenced hippocampal map (parent, split into 074a-d)

**Recommended disposition:** (a) testable now -- the parent is **not** a pure index: it owns the two-route-separability assertion, 888 confirmed it on the replay-sampling path at 3/3 seeds, and the one genuinely open residual is whether that separability survives on a *second, independent* readout consumer.
**Extracted from:** V3-EXQ-888's own `combination_rule` and `criteria[].claim` mapping (C1 + C4 are registered against this claim), plus SD-035's `what_would_answer` residual-gap section. Not drafted fresh.
**Currency check:** `evidence/experiments/v3_exq_888_..._20260804T075257Z_v3.json` (PASS, 3/3 seeds, `non_degenerate: true`, `degeneracy_reason: ""`); reviewed -- present in `review_tracker.json` `reviewed_run_ids` **and** `discussed_experiment_dirs`; `claim_evidence.v1.json` MECH-074 `genuine_exp_count 1 / exp_conf 0.705 / confirmed_established`. Substrate present and wired (`ree_core/amygdala/bla.py`, `cea.py`; master knob `use_amygdala_analog=False`, per-module `use_bla_analog`/`use_cea_analog` default True *under* the master). Consumer audit found the spec's third consumer (E3.select) **absent** -- see currency finding 7. Reverse-deps checked: MECH-074a-d, MECH-078, MECH-361, SD-035.
**epistemic_category (proposed):** `standard` (no change; currently unset and inferred as `standard` from `mechanism_hypothesis` -- leave inferred).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: reuse V3-EXQ-888's readiness block verbatim; do not re-derive it. All five must be reported green in-run: n_traces >= 8; buffer std of the ground-truth arousal label >= 0.02 (this is the statistic EVERY AOR routes on -- all four AORs are differences of means of gt_arousal, so zero spread forces every AOR to 0 regardless of weighting); buffer/label index alignment == 1.0; memory_strength range across buffer traces >= 0.05 (the strength route cannot move a weighted sample if encoding_gain does not vary); retrieval_bias range across buffer traces >= 0.01 (same for the address route). Plus the instrument control: the fully-OFF arm must be flat, |AOR_z(OFF)| <= 0.02 on every seed (888 measured -0.0006 / -0.0107 / +0.0063). For a run on a NEW consumer, add: the consumer must be shown to actually receive a non-uniform weight vector -- HippocampalModule silently ignores a retrieval_bias whose numel does not equal the buffer length (hippocampal/module.py:2964), so a length mismatch degenerates to uniform sampling with no error.
> CONFIRMING: four arms at matched seeds (FULL / TAG_OFF = strength route only / GAIN_FLAT = address route only / OFF). Head authority: AOR_z(FULL) - AOR_z(OFF) >= 0.03 on >= 2/3 seeds. Separability: BOTH single-route arms independently clear the same floor -- AOR_z(TAG_OFF) - AOR_z(OFF) >= 0.03 AND AOR_z(GAIN_FLAT) - AOR_z(OFF) >= 0.03. On a NEW consumer (E3.select proposal reweighting, once wired per SD-035's data-flow spec) the address-route arm must clear 0.06, i.e. 2x the across-seed SD of that arm's delta as measured in 888 (0.0313), because the 0.03 absolute floor sits at exactly 1 SD there and would not distinguish replication from noise; the strength-route arm's observed SD is 0.0740, so its replication floor is 0.15.
> FALSIFYING: FULL clears but NEITHER single-route arm does -- authority without separability, i.e. one undifferentiated write channel rather than a read/write head with two routes, which is the parent's specific residual assertion and the only thing it still claims beyond the children. Also falsifying: the OFF arm is not flat (|AOR_z| > 0.02), which voids the instrument rather than the claim; or, on the new consumer, both single-route deltas fall below their replication floors with all preconditions green -- separability would then be a property of the replay-sampling path only, and the parent's scope should be narrowed to that path in text rather than left general.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074 read/write-head route separability on a SECOND readout consumer (E3.select proposal reweighting)`
- related_claims: MECH-074, MECH-074a, MECH-074b, SD-035, ARC-007, MECH-073, MECH-165 (the `replay_diversity_enabled` gate that currently owns the only live consumer)
- acceptance_checks: (1) 888's five readiness gates green per arm; (2) OFF-arm flatness |AOR_z| <= 0.02; (3) head authority delta >= 0.03 on >= 2/3 seeds; (4) both single-route arms >= their replication floors (0.06 address / 0.15 strength); (5) a wiring precondition that `retrieval_bias.numel() == n_candidates` at the E3 consumer, reported, not assumed.
- Note the prerequisite: this run cannot be written until the E3.select consumer named in SD-035's data-flow spec actually exists. Until then this is `complicated (buildable)` on a small wiring change, not `complex (probe-gated)`.
**depends_on additions (if any):** none. (Optionally `MECH-165` as a *note*, since `replay_diversity_enabled` currently gates the only live consumer of the address route -- but that is a wiring fact, not a conceptual dependency.)
**GOVERNANCE FLAG:** `stale_note` -- MECH-074 still carries `v3_pending: true` and a `live_status.evidence` of `decision:...@2026-04-25 hold_pending_v3_substrate/applied`, while its two stated release conditions (substrate lands; EXQ-A/B-equivalent evidence) are both discharged and it now holds a reviewed PASS of its own (888, exp_conf 0.705, `confirmed_established`). Recommend clearing `v3_pending` and refreshing `live_status.evidence` to point at 888. **Also `promotion_review`:** with one genuine supporting run and no weakening runs, `candidate -> provisional` is a live question for the governance pass -- flagged, not applied, and explicitly not a `shown` recommendation.

---

### MECH-074a -- BLA analogue applies an arousal-dependent multiplicative gain to HippocampalModule write strength

**Recommended disposition:** (a) testable now -- the claim's own registered falsifier has a **two-sided** form ("threat-context recall improves ... OR neutral recall is harmed") and the second side has never been measured by any run, because AOR is a composition statistic that cannot separate "threat recall improved" from "neutral recall displaced".
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause, restated identically in `ree-v3/ree_core/amygdala/bla.py` ("Falsification signatures (per sub-claim): MECH-074a"), plus SD-035's `what_would_answer` residual gap (ii) which already names this exact unexecuted run.
**Currency check:** two genuine experimental entries now, not one -- V3-EXQ-659 (2026-06-09, PASS/supports, arousal-over-representation PRIMARY-minus-ABLATION 0.135/0.033/0.213) and V3-EXQ-888 C3 (2026-08-04, strength-route deltas 0.325/0.177/0.249, 3/3). `claim_evidence.v1.json`: `genuine_exp_count 2, pass_runs 2, fail_runs 0, exp_conf 0.755, overall 0.784, confirmed_established`. Promotion gate (`exp_conf >= 0.80 AND >= 4 entries`) still unmet -- status `provisional` is correct. Substrate live: inverted-U gain in `bla.py` (`encoding_gain_max 2.5`, `arousal_threshold_on 0.4`, `arousal_peak 0.7`, window 18000 / half-life 3600 -- all matching the claim's registered numbers), per-episode peak gain carried to the trace as `memory_strength` (`agent.py:3903`). The zero-sum compensation form the second falsifier half would route to already exists as `bla_retrieval_bias_compensation` (default 0.0, `bla.py:463-469`).
**epistemic_category (proposed):** `standard` (leave inferred).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: (1) BLA must actually tick in the live loop -- report `bla_n_ticks > 0`; this is the exact defect that vacated V3-EXQ-474's C2-C5 (an env.step 5-tuple unpacking bug left `bla_n_ticks = 0` and turned the run into synthetic BLAAnalog.tick() unit tests). (2) The gain must VARY: per-episode peak encoding_gain range across the buffer >= 0.05 (888's MS_RANGE_FLOOR), with at least one episode above `bla_arousal_threshold_on = 0.4` and not every threat episode pinned at the inverted-U peak -- a saturated gain is a constant and tests nothing. (3) BOTH DVs must be live: threat-item recall and neutral-item recall each strictly between floor and ceiling in the gain=1 baseline, so that a DECREMENT in neutral recall is measurable at all. (4) The DV must be RECALL ACCURACY on a probe, NOT the arousal-over-representation statistic used by V3-EXQ-659 and V3-EXQ-888. This is the load-bearing precondition: AOR is a share-of-a-fixed-budget measure, so an AOR increase and a neutral-recall decrement are the SAME event expressed twice -- the existing evidence therefore cannot address the second half of this claim's own falsifier even in principle.
> CONFIRMING: two arms at matched seeds -- ARM_GAIN (use_amygdala_analog=True, use_bla_analog=True, defaults) vs ARM_GAIN_1 (`override_bla_encoding_gain` pinned to 1.0, everything else bit-identical). Threat-context recall accuracy delta >= max(0.05 absolute, 1 SD of the across-seed delta) on >= 2/3 seeds, AND neutral recall delta > -0.02 on the same seeds. Both halves required -- a threat-recall gain alone is not a PASS of this falsifier as registered.
> FALSIFYING: with preconditions green, threat-recall delta below the floor on >= 2/3 seeds -- the encoding-gain arithmetic buys replay-composition bias (659/888) but no recall benefit, and the claim's mapping from write strength to retrievability is mis-specified. SEPARATELY falsifying the arithmetic but not the mechanism: threat gain bought at neutral cost (neutral recall delta <= -0.05), which is the claim's own named second failure mode and routes to `bla_retrieval_bias_compensation` (0.1-0.3, the zero-sum form already implemented and default-off) rather than to abandoning the claim.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074a live-loop threat-vs-neutral recall under BLA encoding gain (the unexecuted half of SD-035 EXQ-B)`
- related_claims: MECH-074a, MECH-074, SD-035, MECH-073, ARC-007
- acceptance_checks: `bla_n_ticks > 0`; per-episode peak-gain range >= 0.05 with >= 1 episode above 0.4 and no saturation at 2.5; baseline neutral recall non-degenerate (not 0.0 or 1.0); C1 threat-recall delta >= max(0.05, 1 SD) on >= 2/3 seeds; C2 neutral-recall delta > -0.02 on the same seeds; C3 bit-identical control with `use_amygdala_analog=False` (already contract-guarded by `tests/test_flag_inertness.py` probe F-P1 and `tests/contracts/test_feature_flag_boot_matrix.py` `tpj_and_amygdala` row).
**depends_on additions (if any):** none.
**GOVERNANCE FLAG:** `stale_note` -- the `evidence_quality_note` asserts "this is the first [experimental entry]" and `exp_conf now 0.775`; there are now two entries (659, 888) and `exp_conf` is 0.755. The promotion gate is still unmet so status does not move; only the note needs refreshing, plus a `live_status.evidence` pointer to 888 alongside 659.

---

### MECH-074b -- BLA writes a content-selective per-trace arousal tag and applies a per-trace retrieval weight vector (NOT a scalar gain)

**Recommended disposition:** (a) testable now, on a **narrowed** residual -- 888 already answered the "the address route has independent authority and is not scalar-equivalent" leg; what remains untested is the actual LaBar & Cabeza dissociation (central/gist vs peripheral items *within* an emotional event), and one further leg (trace-age growth) is not implemented at all and should be split out rather than silently carried.
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause; `bla.py`'s MECH-074b falsification signature ("...or if a uniform retrieval boost produces the same behaviour (scalar-equivalent), the content-selective form has collapsed"); and 888's `ARM_GAIN_FLAT` design, whose preconditions this draft cross-references rather than re-derives.
**Currency check:** the claim reads as untested (`v3_pending: true`, `live_status` with no `evidence` block) but is not: 888's C2 is registered against MECH-074b and passes 3/3 seeds (`claim_evidence.v1.json`: `pass_runs 1, fail_runs 0, exp_conf 0.705, overall 0.794, confirmed_established`). The implementation risk the block flags ("Requires HippocampalModule to carry a per-trace arousal_tag field") is **closed**: the tag is written per trajectory (`agent.py:3904`, `hippocampal/module.py:2885/2917/3142`), read back via `get_exploration_arousal_tags()` (module.py:2920), turned into `w_i = 1 + alpha*tag_i` at `bla.py:459-469` (`alpha` default 0.6, in the claim's [0.3, 1.0] band), and consumed as sampling weights at `module.py:2951-3021`. **But** the consumer coverage is narrower than SD-035's spec: `retrieval_bias` reaches `diverse_replay` (gated on `replay_diversity_enabled`) and the REM reverse-replay pass only -- it never reaches `E3.select` (currency finding 7). A 2026-08-07 targeted lit-pull (4 entries, one mixed/weakening on the retrieval locus) is absent from the block's `source`. The claim's "BLA contribution grows with trace age (20 min -> 1 week)" leg has **no implementation**: `arousal_tag` is a static scalar written once at encoding, with no age term anywhere in `bla.py` or `hippocampal/module.py`.
**epistemic_category (proposed):** `standard` for the claim as a whole (leave inferred). Flagging separately that the **trace-age-growth leg is `substrate_conditional`** and should be carried in a `digestion_note` or split to its own id rather than left inside a `standard` claim, where it silently drags on any promotion.
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION: see MECH-074's own what_would_answer for the shared readiness block (n_traces, gt_arousal spread, buffer/label alignment, both route-nonuniformity floors, OFF-arm flatness) -- do not re-derive it. Two additions specific to this claim: (a) the arousal tag must be written AT ENCODING (`bla_retrieval_tag_at_encoding=True`); the module exposes False precisely to reproduce the named scalar failure signature, so that setting is the NEGATIVE CONTROL ARM, not a misconfiguration. (b) The environment/harness must expose CENTRAL/GIST vs PERIPHERAL items WITHIN the same episode, each with independently measurable recall. Without (b) the run re-measures 888's between-trace threat-vs-neutral contrast, which is already answered and is NOT the LaBar & Cabeza central/peripheral dissociation this claim is about; a "PASS" obtained that way would be vacuous with respect to the residual.
> CONFIRMING: three arms at matched seeds -- ARM_VECTOR (per-trace w_i = 1 + alpha*tag_i, alpha in [0.3, 1.0]), ARM_SCALAR (uniform w = 1 + alpha*mean(tag) across all traces; equivalently `bla_retrieval_tag_at_encoding=False`), ARM_OFF. Confirming requires ALL THREE of: (1) in ARM_VECTOR, central/gist recall advantage over peripheral items of 1.3x-2.0x relative to the neutral baseline (the claim's own registered target magnitude) on >= 2/3 seeds; (2) ARM_SCALAR's dissociation indistinguishable from ARM_OFF's (delta below 0.02) -- the scalar form must NOT reproduce it; (3) ARM_OFF's dissociation flat within |0.02|.
> FALSIFYING: ARM_SCALAR reproduces ARM_VECTOR's dissociation within the margin -- the content-selective form is not load-bearing and the claim collapses to a scalar retrieval gain, which is the failure signature the claim was registered to exclude. Independently falsifying: ARM_VECTOR's dissociation misses the floor with all preconditions green -- the per-trace weight then has composition authority over the replay SAMPLE (888) but no authority over item-level READOUT, and the claim should be narrowed to the sampling path rather than retained as a retrieval-weight claim. NOT falsified by, and not testable as, the "BLA contribution grows with trace age" leg: no age term exists in the substrate, so that leg is substrate_conditional on an unbuilt trace-age input and must not be scored in this run.
**Proposal sketch (only for a/d):**
- title: `V3-EXQ-<next>: MECH-074b central/peripheral dissociation under vector vs scalar BLA retrieval bias`
- related_claims: MECH-074b, MECH-074a (supplies the encoding-time tag; a 074b null is uninterpretable if the tag write is not green), MECH-074, SD-035, ARC-007
- acceptance_checks: shared 888 readiness block; `bla_retrieval_tag_at_encoding` true in ARM_VECTOR / false in ARM_SCALAR with all else bit-identical; within-episode central vs peripheral item recall both non-degenerate in ARM_OFF; C1 vector dissociation 1.3x-2.0x on >= 2/3 seeds; C2 scalar-arm dissociation <= 0.02 above OFF; C3 OFF flatness.
**depends_on additions (if any):** none required (MECH-074a is already listed, correctly, with the right rationale comment). Optionally record MECH-165 as the current gate on the only live consumer.
**GOVERNANCE FLAG (two):**
- `stale_note` -- `v3_pending: true` and an empty `live_status` on a claim that holds a reviewed 3/3-seed PASS (888 C2), `exp_conf 0.705`, `confirmed_established`; and the block's `source` omits the entire 2026-08-07 `targeted_review_mech_074b/` pull. Recommend clearing `v3_pending`, adding a `live_status.evidence` pointer to 888, and folding in the four lit entries.
- `evidence_discrepancy` -- one of those new lit entries (Roozendaal & McGaugh 2011, `evidence_direction: mixed`, confidence 0.62) explicitly weakens this claim's RETRIEVAL locus while supporting MECH-074a's encoding locus: "the best-established amygdala memory effect is on CONSOLIDATION ... at RETRIEVAL the amygdala/glucocorticoid effect is documented as IMPAIRING". The claim text does not record this, and a governance pass should decide whether 074b's locus needs narrowing (e.g. to a *sampling-priority* rather than *retrieval-enhancement* form) before more experiment budget goes to it.

---

### MECH-074c -- CeA analogue emits a fast subcortical priming signal (fast_prime), distinct from MECH-046's cortical mode-prior write

**Recommended disposition:** (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = the **SD-011 AffectiveHarmEncoder magnitude regime** (`||LowFreq(z_harm_a)||_1/n` never reaches `cea_fast_route_threshold` in an embodied run), which is itself an instance of the V3 observation->z_world binding constraint. Legs 1-2 are genuinely answered in the *driven* regime and should not be re-run; everything the claim asserts about *in-loop* function is untestable until the gate fires.
**Extracted from:** the claim's own 3-leg "Falsifiable:" clause; V3-EXQ-895's `evidence_scope_note` (which self-declares the PARTIAL scope) and `interpretation.selectivity_leg` (which banks the readiness denominator for a successor, explicitly so the successor "need not re-derive it"). Drafted by narrowing those, not from a blank page.
**Currency check:** V3-EXQ-895 (2026-08-08) is PASS/supports with all five criteria green -- C1 onset latency 0 steps (<= 2), C2 fitted half-life 4.0 (in [3,5]), C3 retained fraction at override-window end 0.297 (<= 0.50), C4 cortical confirmation holds 1.0 retained with arm separation 0.703 (>= 0.40), C5 max |fast_prime| 0.8 <= `mode_prior_log_odds_max` -- and `non_degenerate: true`. **But** its non-gating embodied probe records `embodied_fire_count = 0` on all 4 seeds (570 / 720 / 638 / 116 ticks), `lf_harm_max` 0.202 / 0.093 / 0.216 / 0.122 against `cea_fast_route_threshold = 0.5`, and `fast_prime_max = 0.0` everywhere. So the gated criteria are driven-regime results. Two of the claim's own scope notes have gone stale: the SD-032c AIC comparator now **exists** (`ree_core/cingulate/aic_analog.py`, constructed at `agent.py:792-803`), so the fast:slow leg is buildable; and the `agent.py:869-886` urgency-interrupt pointer no longer resolves. `claim_evidence.v1.json`: `genuine_exp_count 1, pass_runs 0 recorded as fail 0, exp_conf 0.714, overall 0.735, confirmed_established`.
**epistemic_category (proposed):** `substrate_conditional` -- **contested; see the flag.** The strict discriminator asks whether the mechanism has ever been exercised: in the regime the claim is *about* (embodied, in-loop, prefiguring cortical output) it never has -- zero fires, so there is no signal for anything downstream to absorb, which rules out `substrate_ceiling`. The counter-argument is that legs 1-2 hold real positive driven-regime evidence, and this category suppresses promote/demote on a `provisional` claim.
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION -- this is the whole finding, not a formality: the CeA fast gate must actually FIRE in the regime being measured, at its REGISTERED threshold. The only embodied measurement to date (V3-EXQ-895's non-gating SELECTIVITY_PROBE, 4 seeds, 2044 ticks total) recorded embodied_fire_count = 0 on every seed with max ||LowFreq(z_harm_a)||_1/n = 0.216 against cea_fast_route_threshold = 0.5, and fast_prime identically 0.0. Any embodied MECH-074c run must therefore report fire_count > 0 with the threshold at default before any DV is read; a run that LOWERS the threshold to force firing measures the threshold, not the claim, and must be reported non_contributory. Legs 1 (onset latency) and 2 (decay under cortical non-confirmation, plus overridability and boundedness) are ALREADY ANSWERED in the driven regime by V3-EXQ-895 (C1 0 steps <= 2; C2 half-life 4.0 in [3,5]; C3 0.297 <= 0.50; C4 hold 1.0 / separation 0.703; C5 0.8 bound) -- do not re-run them; cite 895.
> CONFIRMING (the residual, in-loop leg): with the gate firing at its registered threshold in an embodied run, fast_prime's onset must PRECEDE the AIC/dACC comparator's threshold crossing on the same harm event by >= 3 sim steps on >= 2/3 seeds (the claim's registered 1-2 vs 5-10 step spec, i.e. the ~5:1 fast:slow ratio floored conservatively), while |fast_prime| stays <= cea_mode_prior_log_odds_max so the fast route never dominates cortex, and cortical confirmation arriving inside the override window still holds the pulse (>= 0.90 retained) as it does under driven input.
> FALSIFYING: with the gate firing, fast_prime and the AIC crossing are simultaneous, or AIC leads -- the signal is not functionally a PRIME (it arrives too late to prefigure cortical output), which is the module's own registered MECH-074c failure signature. Also falsifying: in-loop, the pulse proves non-overridable (cortical confirmation cannot flip it within the 5-10 step window) -- the override discipline that bounds this claim would then be false in the only regime that matters.
> LEG 3 IS NOT A MECH-074c LEG (fused-claim finding, stated here so it stops being re-litigated): "CeA must fire on harm-affective valence, not generic arousal" cannot be tested as a CeA-module manipulation, because CeAAnalog.tick() is a pure function of ||LowFreq(z_harm_a)||_1/n -- a magnitude-matched non-harm drive fires IDENTICALLY by arithmetic (the DV-symmetry artifact class, per failure_autopsy_V3-EXQ-604c and 895's own interpretation.selectivity_leg). Selectivity is a property of the upstream SD-011 AffectiveHarmEncoder. That leg should be re-registered against SD-011 with 895's already-banked readiness denominator: mean AUROC against the same hazard-proximity label of 0.674 (encoder input), 0.622 (CeA gate statistic), 0.540 (generic activation), reference floor 0.60 -- i.e. the encoder's own harm-discriminativeness is currently only marginally above the floor, which is the real question hiding inside this leg.
**Proposal sketch (only for a/d):** n/a -- not (a). If the encoder regime is ever raised (or a threat-dense curriculum reaches the gate), the successor is fully specified above and 895 already banked its denominator, so it is `complicated (buildable)` at that point rather than a fresh design.
**depends_on additions (if any):** none strictly needed -- SD-011, SD-032c and MECH-046 are already listed. Recommend a `digestion_note` recording that leg 3 belongs to SD-011 and that the fast:slow leg is now unblocked on the SD-032c side (AICAnalog exists) and blocked only on the firing precondition.
**GOVERNANCE FLAG (two):**
- `contested_disposition` -- proposing `epistemic_category: substrate_conditional` on a `provisional` claim suppresses promote/demote. The case for it: the claim's in-loop content has never been exercised (0 fires embodied). The case against: legs 1-2 hold genuine driven-regime PASSes and 895 is already scored `supports`. Governance should choose explicitly rather than let the tag drift; a middle option is to leave the category inferred and record the firing precondition as a `digestion_note`, which preserves the evidence reading while still preventing a vacuous successor.
- `stale_note` -- (i) "Urgency interrupt at ree-v3/ree_core/agent.py:869-886" no longer resolves (that range is now the ConditionedSafetyStore block); the deferred migration into `fast_prime` is still undone. (ii) The 2026-08-08 note's "fast:slow ratio ... out of scope pending SD-032c AIC comparator wiring" is stale as to the blocker -- AICAnalog is built and wired; the actual blocker is the never-firing embodied gate.

---

### MECH-074d -- BLA emits a remap_signal on harm-PE spike when predictor-attribution flags specific latent codes (partial, ~one-third remap)

**Recommended disposition:** (c) substrate-blocked -- **`substrate_conditional`**, blocking substrate = **MECH-153's supervised context-labeling objective** (unbuilt) over the SD-016 / E1 `ContextMemory` store. The four consecutive negative results are a *precondition* failure of the attribution head's INPUT, not four independent refutations of the remap mechanism, and MECH-153 registered this exact failure signature five months earlier for a different consumer.
**Extracted from:** the claim's `functional_restatement` "Falsifiable:" clause; the four autopsy records already inline in the block (894 / 894a / 894b / 894c); and SD-035's `substrate_queue.json` OPEN failure_record, whose target I quote verbatim rather than re-invent -- "an entropy-weight/loss-formulation change, OR a verified context-discriminating input signal to the attribution head, that clears C1 AND C2 on >= 2/3 seeds without relying on scalar loss-term retuning alone".
**Currency check:** the substrate is built and works mechanically -- `ree_core/amygdala/bla.py` remap gate plus the learnable `ree_core/amygdala/attribution_head.BLAAttributionHead` (landed 2026-08-09, `ree-v3 25e04cf5f5` + `d2c8d6f2f0`, default-off via `bla_attribution_head='contribution_threshold'`); 894/894a established compute/fire/write/partiality are correct across four PE-sigma thresholds. `claim_evidence.v1.json`: `genuine_exp_count 4, pass_runs 0, fail_runs 4, exp_conf 0.414, plausible_unproven`; demotion `provisional -> candidate` applied 2026-08-16 -- **that demotion is not disputed here.** What IS new since 894c (2026-08-10): (a) `ree-v3 76cbf84` "repair ContextMemory.write() deterministic single-slot fixed point" (2026-08-19); (b) a ContextMemory write-address workstream -- V3-EXQ-943 PASS, 946 PASS (`context_informative_address_found_at_operating_point`), 956 FAIL, 969 FAIL, 970 FAIL (`h1_content_referencing_objective_not_confirmed_either_regime`), 971, 972 PASS (`h4_supported_representation_undifferentiated`). **All seven carry `evidence_direction: non_contributory` and `claim_ids: null`** -- none is scored against MECH-074d, so the owed fix is NOT delivered. And the deeper input: MECH-153's required supervised context-labeling objective is **not built** -- no `context_label` / `supervised_context` symbol anywhere in `ree-v3/ree_core/` (verified with `/usr/bin/grep`), and its validation run V3-EXQ-504 returned `inconclusive`. SD-035's 2026-08-09 addendum independently states the mechanism: the legacy ContextMemory write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, "which defeats ANY attribution rule".
**epistemic_category (proposed):** `substrate_conditional` -- **this is a proposal to RE-TAG, and the reasoning must be read with its history.** The 894c autopsy deliberately moved this claim `substrate_conditional -> standard` in order to expose it to the ordinary promotion/demotion pass; that pass ran on 2026-08-16 and the demotion was applied. The exposure purpose is therefore **spent**, and leaving it `standard` now means each future cycle re-litigates a demotion that has already happened on a claim whose input mechanism does not exist. The strict discriminator supports the tag: the attribution head has never been exercised with a context-discriminating input, so there is no signal for a downstream mechanism to absorb (which is what `substrate_ceiling` would require).
**Draft `what_would_answer`:**
> NON-DEGENERACY PRECONDITION -- the attribution head must be given a context-DISCRIMINATING input, and the run must PROVE it in-run before scoring anything. V3-EXQ-894c's decisive reading was that within-context and cross-context Jaccard similarity were IDENTICAL (1.0000 exactly) in 10/15 cells -- the head had converged to a deterministic, context-INVARIANT target set. That is the same signature MECH-153 registered on 2026-03-31 for the E1 ContextMemory store (cosine_sim 0.9999 between hazard-proximate and hazard-distal context vectors, 0/3 seeds), and SD-035's own 2026-08-09 addendum states the legacy write path homogenises the slot bank to off-diagonal cosine 1.0000 within ~24 episodes, "which defeats ANY attribution rule". So a retest is VACUOUS unless it first reports, sustained over the scoring window: off-diagonal ContextMemory slot cosine <= 0.90, AND within-context vs cross-context Jaccard separable at all (not both exactly 1.0). The MECHANICAL half needs no further testing -- 894 and 894a established that candidates compute, the gate fires under `use_e2_harm_a=True`, writes land, and partiality holds, across four PE-sigma thresholds; a fifth run of that is redundant compute.
> CONFIRMING: under a store that PASSES the differentiation precondition, and at some operating point, C1 attribution_mass_excess > 0.05 AND C2 context_jaccard_gap > 0.05 on >= 2/3 seeds, with the partiality half still holding (fraction of perturbed codes ~0.33, not wholesale). This is SD-035's open failure_record target verbatim; do not weaken it, and do not substitute C1 alone -- C1 recovered fully under the trained head in 894b (0/3 -> 3/3) while C2, the actual Moita 2004 dissociation this claim is about, stayed at 0/3, so C1 alone is a known false-positive route.
> FALSIFYING: with the differentiation precondition demonstrably GREEN, C2 still stays at 0/3 seeds -- the Moita 2004 contextual-vs-auditory dissociation is then not reproducible by an attribution-gated remap in this architecture, and the claim is refuted on its critical half rather than deferred again. Note what would survive that: the partiality half (~one-third remap, not wholesale replacement) held on 2/3 seeds in 894 and could be retained as a narrowed residual claim about remap SHAPE with the attribution-gating half withdrawn. Four routes are already closed by measurement and must not be re-proposed: PE-threshold recalibration/dilution (894a, Spearman -1.0 monotone), trainability alone (894b, doubled budget), entropy_weight/MSE scalar retune (894c, swept [0.02, 0.01, 0.005, 0.001], `passing_arm_ids=[]`, and the predicted C1-vs-C2 tradeoff came out INVERTED at spearman -1.0), and a fifth mechanical-gate readiness run.
**Proposal sketch (only for a/d):** n/a -- not (a). The next artifact owed is a BUILD (MECH-153's supervised context-labeling objective, or a validated substitute from the 943/946/956/969-972 write-address workstream), not an experiment. V3-EXQ-946's `context_informative_address_found_at_operating_point` is the single most promising existing lead and is the thing a `/implement-substrate` chip should be pointed at.
**depends_on additions (if any):** **add `MECH-153`** (E1 ContextMemory requires a supervised context-labeling objective; without it context vectors stay near-identical) and **`SD-016`** (the E1 z_world ContextMemory query path that owns the store). This is the single most load-bearing edit this group recommends: it converts four apparently independent refutations into one named, already-registered, already-owned upstream precondition, and it makes the dependency machine-readable so the next governance pass does not re-derive it.
**GOVERNANCE FLAG (three):**
- `contested_disposition` -- MECH-153's own registration says of the identical failure signature: "**This is an implementation precondition, not a claim that MECH-150 is false.**" By that precedent MECH-074d's four weakens results measure an absent input, not a false mechanism. This does **not** argue for reversing the 2026-08-16 demotion (`exp_conf 0.414`, `conflict_ratio 0.80` are real and the demotion "records what the evidence already shows"); it argues for re-tagging `epistemic_category` to `substrate_conditional` so the claim stops being re-demoted for a precondition it cannot satisfy, and for routing it to `/implement-substrate` rather than `/queue-experiment`. Governance to ratify or reject; not applied here.
- `evidence_discrepancy` -- SD-035's open failure_record target ("a verified context-discriminating input signal") has had a substantial workstream land against it since 894c (ree-v3 `76cbf84` plus V3-EXQ-943/946/956/969/970/971/972, 2026-08-19 to 2026-09-02), yet every one of those runs is `non_contributory` with `claim_ids: null`, so nothing has updated MECH-074d or the SD-035 entry. The `resolved: open` record and the claim's `pending_retest_after_substrate: true` are both accurate but neither reflects that the fix is being actively probed and that V3-EXQ-972 reports `h4_supported_representation_undifferentiated` -- i.e. current evidence points at the representation, not the head.
- `stale_note` -- SD-035's `status_note_addendum_20260809` records "STILL OWED: the MECH-074d implementation_note in claims.yaml was NOT written" (deferred at the time because another session held a binding arbitration verdict on claims.yaml). It is still not written; the trainable-head build record lives only in `docs/architecture/sd_035_amygdala_analog.md` "Second pass: trainable attribution head". Additionally, SD-035's `metric_trajectory` still asserts "MECH-074b retrieval_bias hippocampal-consumer wiring deferred (substrate produces signal but HippocampalModule does not yet read)", which is false as of the current tree.

---

### Cross-group note for the orchestrator (not a disposition)

SD-035 itself is not in this group but is the parent substrate for all five claims and accumulated four stale statements found during this pass (currency findings 2, 6, 7, 10). Two of them -- the E3.select consumer that the spec asserts and the code does not implement, and the "HippocampalModule does not yet read" line -- would each change how a reviewer reads MECH-074b. If any group is digesting SD-035, these belong there; otherwise they are worth a single `stale_note` flag on SD-035 in their own right.

---

<!-- G4 appended 2026-09-04T21:17:34Z -->
## G4 -- signal legibility / language-as-externalisation cluster  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** The assigned rationale was
  co-occurrence scoring (ARC-048 <-> MECH-192 = 6.00 via `depends_on` + "functional states /
  requires"; INV-057 <-> MECH-192 = 4.00; INV-057 <-> MECH-182 = 3.79 via the shared
  social-signal namespace). My own view after reading the live blocks is sharper and changes
  the whole shape of the pass: **all four members are the fan-out around a single hub claim,
  MECH-191, which has ALREADY been digested** and carries a fully-worked `what_would_answer`
  using an explicit Leg A (testable now, receiver-free) / Leg B (blocked on the social stack)
  split. MECH-191 `depends_on` MECH-182 (it is registered as "extends MECH-182 from one signal
  to the full repertoire"); INV-057, MECH-192 and ARC-048 all `depends_on` MECH-191. So this
  group is not four independent falsifier-drafting jobs. It is **one already-written falsifier
  plus three positioning decisions relative to it**, and the single most valuable thing this
  pass can do is stop three claims re-deriving a test that exists, and identify the one genuinely
  new manipulation the group is missing (MECH-192's signal-side ablation). Standing instruction 1
  (extract before inventing) and 6 (cross-reference rather than re-derive) do most of the work here.

- **(i) same-claim / merge candidates:**
  - **MECH-192 <-> MECH-191 Leg B / MECH-183: PARTIAL absorption, propose merge, do NOT retire.**
    MECH-192 as registered ("z_beta leakage can only produce functional state-matching if the
    perceived signal maps onto a corresponding internal state") is close to **analytic** -- it
    reads as a definitional truth about what a mapping is, not an empirical assertion. Its
    necessity framing is already covered by MECH-191's Leg B falsifier clause (receiver decoding
    "drops toward chance when the receiver's own homologous internal-state machinery is
    ablated/absent") and by MECH-183's OTHER_SELFLIKE ON/OFF 2x2. **The residual is real but
    narrow, and nobody currently owns it: MECH-191 Leg B ablates the RECEIVER; MECH-192's own
    content requires ablating the SIGNAL** (an energy- and information-matched scramble at fixed
    coupling). Those are different manipulations and the receiver-side one does not test the
    signal-side one. Disposition (g) below, with the narrowed residual written out.
  - **INV-057 <-> MECH-191 Leg A: FUSED, not merge.** INV-057's architectural consequence
    ("stereotyped signals are causally generated by their referent states, not conventional") is
    MECH-191 Leg A's assertion verbatim; INV-057 adds nothing REE-side beyond it. What INV-057
    uniquely owns is the *evidential move* from comparative ethology, which no REE substrate can
    settle. Disposition (c2), with the REE leg explicitly assigned to MECH-191.
  - **MECH-182 <-> MECH-191 Leg A: overlapping but NOT merge.** MECH-191's own notes say it
    "extends MECH-182 from one signal to the full repertoire", so MECH-182 looks like the
    single-signal special case. It is not: MECH-191 Leg A is **receiver-free and learning-free**
    (it asserts causal production only), whereas MECH-182's whole novelty over the classical
    acoustic literature (Andics 2014, Balint 2022) is the **learning** step (cross-modal
    association acquired from self-experience) and the **generalisation** step (same feature in
    another agent). Neither is in MECH-191. Keep both.
  - **ARC-048 <-> INV-003: FUSED, not merge.** ARC-048's premise leg ("language is not a separate
    cognitive system") is INV-003's assertion, already digested as a `derivational` code-path
    audit. Its consequence leg (the bootstrap requires functional states to pre-exist as
    referents; language is a *bandwidth increase over the same channel*) is ARC-048's alone and
    is the falsifiable part. Two-leg template written out below, as the group brief asked.

- **(ii) contradictions / undercut premises:** No outright contradiction, but **one real
  premise-undercut that changes a falsifier and that neither claim states.** INV-057 argues
  "legible without species-specific learning, therefore causally generated, therefore not
  conventional" -- it treats *not socially conventional* as interchangeable with *not learned*.
  MECH-182 says the harm-signal mapping **is** learned: acquired privately from self-experience
  by the harm attribution stream. These are compatible only under a distinction neither claim
  makes -- **socially conventional (acquired by transmission from conspecifics) vs individually
  learned from self-experience with one's own homologous state.** This is not pedantry: it
  changes what falsifies INV-057. Under the naive reading, "cross-species reading requires prior
  exposure" falsifies INV-057; under the sharpened reading it does not (self-experience with
  one's own state *is* the exposure, and that is precisely MECH-182's mechanism). INV-057's
  falsifier must therefore be stated over CONVENTION, not over LEARNING, or MECH-182 falsifies
  INV-057 by construction. I have written it that way below.

  Second, softer undercut: **ARC-048's premise presupposes a pre-linguistic externalisation
  channel already exists** ("language adds bandwidth to a channel that already exists"). MECH-191
  Leg B's finding -- re-confirmed by me on 2026-09-04 -- is that no such channel exists in
  `ree_core/` at all. So ARC-048's non-degeneracy precondition is **strictly stronger than
  INV-003's**: INV-003 needs a language mechanism; ARC-048 needs a language mechanism AND a
  pre-linguistic channel to measure bandwidth *against*. Without the denominator, "higher
  bandwidth" is not a measurable predicate.

- **(iii) shared falsifier:** Yes, and it is already written. **MECH-191's `what_would_answer`
  Leg B RELEASE CONDITION** -- ARC-047 (scent/broadcast channel) plus ARC-010/MECH-031/MECH-032
  (other-agent modelling) -- is the identical gate for MECH-182 Leg B, MECH-192, and ARC-048's
  channel prerequisite. All three should point at it verbatim rather than restate it. Separately,
  **MECH-191's Leg A non-degeneracy precondition** (the internal-state channel and the candidate
  signal-analog event must BOTH show non-degenerate variance across the run -- state activates
  and goes quiescent, event fires and fails to fire) is the reusable precondition shape for
  MECH-182 Leg A and for ARC-048's referent-partition gate. And **MECH-183's already-drafted
  rejected-proxy list** is reusable as a negative control across the group: proxy (a)
  "simulated other-distress cues without an actual other-agent model" and proxy (b) "cross-modal
  z_beta activation from a correlated same-agent cue" are both explicitly non-diagnostic for the
  social claims -- but note that **proxy (b) IS the correct test for MECH-182 Leg A**, and
  MECH-183's own text says so ("tests sensory association learning, i.e. MECH-182"). That is the
  single most useful extraction in this group: MECH-182's Leg A design already exists in the
  registry, written by someone else, and labelled with MECH-182's id.

- **(iv) cross-cutting finding:** Two, and both are group-level.
  1. **The entire 2026-04-05/06 "Steve" cohort is epistemic-category orphaned.** MECH-182,
     MECH-192, MECH-193, ARC-048 and INV-057 carry **no `epistemic_category` and no
     `implementation_phase`**. The indexer therefore *infers*: `standard` for the three
     `mechanism_hypothesis` entries (exp_conf required for promotion; `lit_only` / `low_exp` /
     discrepancy flags fire normally) and `substrate_coherence` for INV-057 (promote/demote
     suppressed, as though it were a foundational REE design choice). Every structurally
     identical claim registered *later* carries the explicit tags -- ARC-047, MECH-405, MECH-505,
     MECH-506, MECH-194, ARC-115, ARC-117, ARC-118 are all `substrate_conditional` +
     `implementation_phase: v5`. Consequence: the cohort generates **permanent lit-only
     promotion-queue noise on claims that are structurally unbuildable in V3**, and INV-057's
     suppression is right by accident and wrong by reason. One tagging pass fixes all five.
  2. **Mutual confound -- the group has a mandatory run ORDER.** A null on MECH-192 is
     uninterpretable unless MECH-183 is pinned (a flat legibility response cannot be
     distinguished from "there is no leakage to modulate"); a null on MECH-183 is uninterpretable
     unless MECH-191 Leg A is pinned (a signal that is not state-specific carries nothing to
     leak). The chain **MECH-191 Leg A -> MECH-183 -> MECH-192** must be established in that
     order, and MECH-182 Leg B sits downstream of the same chain. Any proposal that runs a
     legibility or generalisation manipulation before Leg A passes is vacuous by construction.

- **Currency findings** (each verified this pass, 2026-09-04):
  1. **All four members have ZERO experimental evidence.** `evidence/experiments/claim_evidence.v1.json`:
     ARC-048 `exp_conf 0.0`, 2 lit entries, `lit_conf 0.746`; INV-057 `exp_conf 0.0`, 5 lit
     entries, `lit_conf 0.862`; MECH-182 `exp_conf 0.0`, 3 lit, `0.708`; MECH-192 `exp_conf 0.0`,
     3 lit, `0.787`. All four `evidence_quadrant: plausible_unproven`, `genuine_exp_count: 0`,
     `fail_runs: 0`. Each one's `latest_run_id` is a **2026-04 literature entry, not a run**
     (e.g. INV-057 and MECH-192 both point at
     `2026-04-06_mech_192_dog_recognize_emotion_multimodal_albuquerque2016`).
  2. **The one experiment manifest that names MECH-191 does not count.**
     `evidence/experiments/v3_exq_723_jlens_dispositional_readout_diagnostic_20260709T151028Z_v3.json`
     states verbatim: `experiment_purpose=diagnostic, EXCLUDED from governance scoring;
     claim_ids=[] -- SD-064 global-workspace claim + MECH-191 signal-legibility referenced for
     CONTEXT only`. No group member has any run-level evidence at all.
  3. **Substrate re-confirmed absent (independent re-check of MECH-191 Leg B's and MECH-183's
     2026-08-08 findings).** `grep -ril` over `/Users/dgolden/REE_Working/ree-v3/ree_core/` returns
     **zero** hits for `other_agent`, `multi_agent`, `OTHER_SELFLIKE`, `attribution_stream`,
     `empathy`, `vocal`, `timbre`, `acoustic`. Same for
     `/Users/dgolden/REE_Working/ree-v3/experiments/_lib/`. `z_beta` exists but is documented in
     `ree_core/latent/stack.py:14` as `z_beta [beta_dim] -- affective latent (arousal/valence;
     integrates self + world signals)` -- a **SELF** stream in the shared stack, exactly as
     MECH-183 recorded. **Trap flagged so the next pass does not repeat it:** the sole `legib`
     hit under `ree_core/` is `ree_core/agent.py:10050`, a comment reading "provenance is legible
     at the call site" -- unrelated to signal legibility. Do not read it as substrate.
  4. **Nothing is queued to build.** `evidence/planning/substrate_queue.json` has **zero**
     entries for ARC-048, INV-057, MECH-182, MECH-192, MECH-191, MECH-183, ARC-047 or MECH-041.
  5. **Plan-orphan status, split.** MECH-191 IS in `fast_empathy_v5_plan.md` `scope_claims`
     (`[ARC-010, MECH-031, MECH-112, SD-011, MECH-183, MECH-191, MECH-359, MECH-360]`).
     **MECH-192, MECH-182, MECH-193 and INV-057 are in NO plan's `scope_claims`**, despite being
     the direct siblings of the two that are. **ARC-048 is NOT in
     `language_emergence_bootstrap_v6_plan.md` `scope_claims`** (`[ARC-009, INV-003, INV-007,
     MECH-010, MECH-014, MECH-308]`) despite being registered explicitly as "the pre-linguistic
     bridge to INV-003", and despite that plan's node `LANG-2` being literally "the pre-linguistic
     substrate inventory communication needs before it can bootstrap".
  6. **STALE: a reassignment flag was raised and never applied.** `fast_empathy_v5_plan.md`
     decision log, 2026-06-10: "Reassignment flags raised for the existing social claims this plan
     builds on whose subject is intrinsically social (ARC-010, MECH-031, MECH-183, MECH-191)."
     As of 2026-09-04 **neither MECH-183 nor MECH-191 carries an `implementation_phase` field in
     `claims.yaml`** -- contrast ARC-047 and MECH-405, which both carry `implementation_phase: v5`.
  7. **STALE: the 2026-04-06 intake's own Next Step 4 is unexecuted.** It says "social.md should
     gain stubs for MECH-191/192/193 and ARC-048 when social extension work begins".
     `docs/architecture/social.md` (mtime 2026-08-30, so actively maintained -- it has *since*
     grown MECH-505 and MECH-506 sections) contains **zero** occurrences of MECH-191, MECH-192,
     MECH-193, ARC-048, INV-057 or MECH-182. The only adjacent hits are MECH-183/MECH-405 inside
     the MECH-505 text. This is a gap in a live file, not a dormant file.
  8. **KNOB finding, decisive for MECH-182.** The learner MECH-182's mechanism runs in --
     `BLAAttributionHead`, `ree-v3/ree_core/amygdala/attribution_head.py` (SD-035 / MECH-074d) --
     **exists but is DEFAULT-OFF**: `ree_core/utils/config.py:6017` sets
     `bla_attribution_head: str = "contribution_threshold"`, i.e. the fixed **non-trainable**
     rule. That module's own docstring states the fixed rule "has no learned component ... and no
     mechanism by which it could become more selective with experience". Furthermore its
     selectivity sits at a **documented competence floor**: V3-EXQ-894 (FAIL, weakens) and
     V3-EXQ-894a (FAIL, weakens, 4-point sigma sweep) with autopsy
     `failure_autopsy_V3-EXQ-894a_2026-08-08` diagnosing `competence_implementation_gap`
     (per-seed: one selective, one context-blind-deterministic, one null, stable at every
     threshold). Any MECH-182 learning test on default config is vacuous.
  9. **NEW downstream consumer for ARC-048.** ARC-118 (registered 2026-08-01, "worldly reference
     is inherited through the world model") `depends_on: [ARC-048, INV-003]` and is tagged
     `substrate_conditional` / `implementation_phase: v5` / `version_relevance: v5_v6`. ARC-048's
     own epistemic status is currently **less specified than its own dependent's**.

---

### GROUP-LEVEL GOVERNANCE FLAGS

**GOVERNANCE FLAG -- `stale_note`:** The 2026-04-05/06 "Steve" cohort (MECH-182, MECH-192,
MECH-193, ARC-048, INV-057) carries no `epistemic_category` and no `implementation_phase`, so the
indexer infers `standard` for the three mechanism_hypotheses and fires `lit_only`/`low_exp` flags
perpetually against claims that are structurally unbuildable in V3, while INV-057 gets
`substrate_coherence` suppression for the wrong reason. Every later-registered structural twin
(ARC-047, MECH-405, MECH-505, MECH-506, MECH-194, ARC-115, ARC-117, ARC-118) carries explicit
`substrate_conditional` + `v5`. Recommend a single tagging pass across the cohort; per-claim
proposals below. MECH-193 is out of my group but is in the same cohort and same condition --
flagged here so it is not missed.

**GOVERNANCE FLAG -- `stale_note`:** `fast_empathy_v5_plan.md`'s 2026-06-10 decision-log entry
records reassignment flags raised for MECH-183 and MECH-191; neither claim has an
`implementation_phase` field in `claims.yaml` as of 2026-09-04. The flag was raised and never
applied. (MECH-183 and MECH-191 are read-only context for me -- no draft, no disposition; this is
a plan/registry consistency finding only.)

**GOVERNANCE FLAG -- `stale_note`:** The 2026-04-06 intake's Next Step 4 (social.md stubs for
MECH-191/192/193 and ARC-048) is unexecuted against a file that has been actively maintained since
(`docs/architecture/social.md`, mtime 2026-08-30, gained MECH-505/MECH-506 sections). Zero
references to any of the four. Also: MECH-192, MECH-182, MECH-193 and INV-057 appear in no plan's
`scope_claims`, and ARC-048 is missing from `language_emergence_bootstrap_v6_plan.md`
`scope_claims` / node LANG-2 despite being the registered pre-linguistic bridge to INV-003.

---

### ARC-048 -- Language is a high-bandwidth externalization of pre-existing functional states, not a separate cognitive system

**Recommended disposition:** (c) substrate-blocked, `substrate_conditional` -- the falsifiable
leg needs BOTH a symbol channel (MECH-014 / LANG-3, absent) and a pre-linguistic externalisation
channel to measure bandwidth against (ARC-047, absent), so it is gated on two unbuilt substrates,
not one, and the premise leg is already owned and already digested by INV-003.

**Extracted from:** the claim's own `notes` (the Steve-yelp / Daniel-sentence referent pair);
the 2026-04-06 intake section 3 "The language bootstrap"
(`evidence/planning/thought_intake_2026-04-06_steve_signal_legibility_language_bootstrap.md`);
INV-003's already-drafted `what_would_answer` (for the premise leg and the audit-target framing);
MECH-191's Leg A/Leg B template (for structure). Not drafted fresh.

**Currency check:** (a) INV-003's 2026-08-07 finding -- no `language` / `symbol_channel` /
`communication_channel` / `message_passing` implementation under `ree_core/` -- re-confirmed by my
own greps 2026-09-04; the only language artifacts remain the `LANGUAGE_EXPLICITATION` enum label
in `ree_core/claustrum/control_demand.py` (no implementation) and the "doesn't exist yet in
ree_core" comment in `ree_core/claustrum/coalition_templates.py`. (b) The *pre-linguistic* channel
ARC-048 additionally needs is ARC-047's seven scent fields -- `claims.yaml` ARC-047 is `candidate`,
`confidence: 0.0`, `implementation_phase: v5`, and my grep confirms zero broadcast/scent-emission
implementation under `ree_core/`. (c) ARC-048 has 2 literature entries, `exp_conf 0.0`,
`plausible_unproven`; no run has ever named it. (d) ARC-048 is absent from
`language_emergence_bootstrap_v6_plan.md` `scope_claims` and from node LANG-2's enabling-conditions
checklist, though LANG-2 is exactly the node its content belongs to. (e) ARC-118 (2026-08-01)
already `depends_on` ARC-048 and is tagged `substrate_conditional` / v5.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v6`, `version_relevance: v5_v6` -- matching ARC-118's tagging and the
`language_emergence_bootstrap_v6` tier; governance to arbitrate v5 vs v6, since the channel
prerequisite is a v5 node and the language layer is v6).

**Draft `what_would_answer`:**

> **ARC-048 IS FUSED -- a metaphysical premise plus an operational consequence, with opposite
> ownership. Split them; do not test the group as one thing.**
>
> **LEG A -- THE PREMISE ("language is not a separate cognitive system"). NOT ARC-048's to
> answer. Already owned, already digested.** This is INV-003's assertion ("language emerges as
> functional self-representation, not a bolt-on"), and INV-003 already carries a full
> `what_would_answer` specifying the resolution route: a **code-path audit** (category
> `derivational`), not a trained behavioural experiment, run against whatever function turns agent
> state into emitted symbols and received symbols into agent-state updates, asking whether that
> path reads from and writes to the shared self-representational latent substrate (z_self,
> `ree_core/latent/stack.py`, `ree_core/latent/self_recurrence.py`) or is architecturally
> isolated. **See INV-003's own `what_would_answer` for the precondition, the audit target, and
> both verdict conditions. Do not re-derive them here.** ARC-048 adds nothing to Leg A and must
> not be credited or debited by its outcome.
>
> **LEG B -- THE OPERATIONAL CONSEQUENCE (the falsifiable part ARC-048 alone owns).** Two
> independent, separately-measurable predictions follow from "language is a bandwidth increase
> over an existing functional-state channel, and the bootstrap requires functional states to
> pre-exist as referents":
>
> **NON-DEGENERACY PRECONDITION (strictly stronger than INV-003's -- three gates):**
> (1) A signalling mechanism that both emits and consumes symbols must exist and execute -- the
> same gate INV-003 states, confirmed unmet 2026-08-07 and re-confirmed 2026-09-04. The
> designated landing site is MECH-014's minimal signalling channel, instantiated at
> `language_emergence_bootstrap_v6:LANG-3` (status `blocked`).
> (2) **A PRE-LINGUISTIC externalisation channel must ALSO exist**, because "higher bandwidth than
> the existing channel" has no denominator without one and prediction B2 has no baseline
> partition. That channel is ARC-047's scent/broadcast fields; see MECH-191's own
> `what_would_answer` Leg B RELEASE CONDITION for the exact substrate list -- **do not re-derive
> it.** This gate is what makes ARC-048 harder than INV-003, and it is the reason ARC-048 cannot
> ride INV-003's audit.
> (3) The functional-state channels used as the referent partition must each show non-degenerate
> cross-episode variance -- z_harm_a, z_goal, and z_beta valence must each activate AND go
> quiescent within the run (the same variance shape MECH-191 Leg A's precondition specifies). A
> referent partition with a channel pinned always-on or always-off is degenerate and the mutual
> information in B2 is undefined at the floor; the run self-routes `substrate_not_ready`.
>
> **CONFIRMING (B1 -- ORDERING / referent precedence):** with the signalling channel open, an
> agent whose functional-state channels are ablated or floored fails to stabilise ANY signal,
> while a matched agent with intact functional states and no prior signalling history does
> stabilise signals -- i.e. the referents are load-bearing for bootstrap, not incidental.
> **CONFIRMING (B2 -- ISOMORPHISM / bandwidth-monotonicity):** the emergent signal repertoire's
> discriminative partition is a **refinement** of the pre-linguistic functional-state partition --
> higher resolution over the SAME referents (the yelp -> "my leg hurts when I walk on wet grass"
> relation in the claim's own notes) -- not a cross-cut of it. Metric: mutual information between
> emitted-signal identity and functional-state identity exceeds MI between signal identity and an
> entropy-matched task-arbitrary partition (e.g. tokens keyed to grid coordinates), by a margin
> scaled on the SD of the cross-seed delta plus an absolute floor, on at least 2/3 seeds.
>
> **FALSIFYING (B1):** signals stabilise just as readily over an arbitrary non-functional-state
> referent set as over functional states -- language is then a general symbol-learning capacity
> and ARC-048's "pre-existing functional-state referents" requirement is doing no work.
> **FALSIFYING (B2):** the emergent partition **cross-cuts** the functional-state partition (the
> signals carve the task, not the state space), or MI with functional states is
> indistinguishable from MI with the entropy-matched arbitrary partition -- language is then a
> separate channel that merely co-exists with the functional-state channel, not a
> bandwidth increase over it, which is precisely the "separate cognitive system" reading ARC-048
> denies.
>
> **Note on what does NOT falsify ARC-048:** expressive breadth or grammaticality of the emergent
> signalling. INV-003 already records that fluency is a different question; the same exclusion
> applies here, and more sharply, because ARC-048's claim is about the referent architecture, not
> the channel's expressive power.

**Proposal sketch (only for a/d):** n/a -- not proposing an experiment; both gates are unmet and
`substrate_queue.json` carries no entry for any of the required substrate.

**depends_on additions (if any):** add **ARC-047** (the pre-linguistic broadcast channel that
precondition (2) requires -- currently a hard prerequisite that appears nowhere in ARC-048's
`depends_on`) and **MECH-014** (the minimal signalling channel precondition (1) requires).
Existing `[INV-003, MECH-191, MECH-192]` all stay.

**GOVERNANCE FLAG:** `stale_note` -- ARC-048 is registered as the pre-linguistic bridge to INV-003
but is absent from `language_emergence_bootstrap_v6_plan.md` `scope_claims`
(`[ARC-009, INV-003, INV-007, MECH-010, MECH-014, MECH-308]`) and from node `LANG-2`'s
enabling-conditions checklist, which is the exact node its content belongs to. Recommend adding
ARC-048 to that plan's `scope_claims` and naming "functional states pre-exist as referents" as an
explicit LANG-2 enabling condition. Second, `contested_disposition` -- ARC-048 currently carries no
`epistemic_category`/`implementation_phase` while its own dependent ARC-118 is
`substrate_conditional`/v5; the parent should not be less specified than the child.

---

### INV-057 -- Cross-species signal legibility evidences that stereotyped signals are functionally specific (causally generated), not socially conventional

**Recommended disposition:** (c2) `out_of_domain` -- this is a **fused** claim whose evidential leg
is comparative ethology that no REE substrate at any level can settle, and whose architectural leg
is already asserted and already digested as MECH-191 Leg A; reframe to name MECH-191 as the owner
of the REE leg and record the out-of-domain proof obligation here.

**Extracted from:** the claim's own `notes` (the Albuquerque 2016 / Molnar 2010 / Ekman 2009
argument as written); the 2026-04-06 intake's INV-057 block and its literature section; MECH-191's
already-drafted Leg A (for the architectural leg, which I point at rather than restate). Not
drafted fresh.

**Currency check:** (a) INV-057 has 5 evidence entries, **all literature**
(`lit:empirical_behavioral` x2, `lit:review_historical`, `lit:review_neuroscience`,
`lit:review_systematic`), `exp_conf 0.0`, `genuine_exp_count 0`, quadrant `plausible_unproven`; its
`latest_run_id` is the Albuquerque 2016 literature entry, not a run. (b) Because it is
`claim_type: invariant` + `invariant_type: universal` with **no explicit `epistemic_category`**,
the indexer resolves it to `substrate_coherence` -- "foundational design choices that ARE the
substrate" -- which is the wrong description of an empirical argument from dog-human communication
studies. The promote/demote suppression it currently receives is correct in effect and wrong in
reason, which means it will be re-litigated by every future governance walk. (c) INV-057 appears in
no plan's `scope_claims`. (d) Precedent for the reframe exists in-registry: 17 claims carry
explicit `epistemic_category: out_of_domain`, including one invariant (INV-062) and the SOC-HUM-1..4
cohort, which pairs `out_of_domain` with a `functional_restatement` field; RA-001/002/003 are the
`claim_type: research_anchor` precedent. (e) INV-057 has a downstream consumer: ARC-117
(`related_claims: [..., MECH-192, INV-057, MECH-191]`), so it must not be retired.

**epistemic_category (proposed):** `out_of_domain`
(and see the governance flag: `claim_type` review toward `research_anchor` is warranted but is
deliberately NOT proposed as an in-place edit -- `REE_assembly/CLAUDE.md` says do not change
`claim_type` in place. The explicit `epistemic_category` is the safe, sufficient action now.)

**Draft `what_would_answer`:**

> **INV-057 IS FUSED and its title gives it away: it is EVIDENTIAL in form ("X evidences that
> Y"), not architectural. An invariant should assert Y; INV-057 asserts the inference X |- Y.
> Split the two legs; only Leg 1 belongs to INV-057.**
>
> **LEG 2 -- THE ARCHITECTURAL CONSEQUENCE Y ("stereotyped signals are causally generated by
> their referent states, not conventional"). NOT INV-057's to answer.** This is MECH-191 Leg A's
> assertion verbatim, and MECH-191 already carries the full REE-side test: per-signal specificity
> of the internal-state channel against the other state channels and a quiescent baseline, plus a
> state-variable ablation that must collapse the corresponding signal-analog event, for the four
> signals whose internal-state correlate exists in `ree_core/` today (whine/z_goal,
> huff/E3-discard-at-breath-cadence, yelp/z_harm_a, tail-wag/z_beta-positive-valence). **See
> MECH-191's own `what_would_answer` Leg A -- its non-degeneracy precondition, its specificity
> and ablation criteria, and its falsifier. Do not re-derive them here.** INV-057 must not be
> separately credited or debited by that outcome; a MECH-191 Leg A pass is not additional
> evidence for INV-057, it is the same evidence counted once.
>
> **LEG 1 -- THE EVIDENTIAL PREMISE X (INV-057's own, and out of REE's domain). This is a
> literature observation, not an experiment. No substrate at any level helps.**
>
> **PROOF OBLIGATION / LITERATURE OBSERVATION:** the observation must hold that cross-species
> affective reading occurs **without species-specific training or convention exposure** --
> Albuquerque 2016 (dogs integrate face + voice to recognise human emotion, untrained,
> cross-modal); Molnar 2010 (perceivers **blind from birth** classify emotional valence from dog
> barks, which is the load-bearing case because it removes any visual-convention learning route);
> Ekman 2009 (the Darwinian universality review). The formal move INV-057 makes is: if the
> mapping were socially conventional, cross-species reading would require separate,
> species-pair-specific learning; it does not; therefore the signal is a causal product of the
> state.
>
> **SHARPENING REQUIRED BEFORE THIS IS FALSIFIABLE, and it is not optional -- as written the
> claim is falsified by its own sibling.** INV-057 uses "not socially conventional" as though it
> meant "not learned". MECH-182 asserts that the harm-signal mapping IS learned -- privately,
> from self-experience, by the harm attribution stream. The two are consistent only under the
> distinction **socially conventional (acquired by transmission from conspecifics, hence
> species-pair-specific) vs individually learned from self-experience with one's own homologous
> internal state (hence available to any architecture that has the homologous state)**. INV-057's
> falsifier must be stated over CONVENTION, not over LEARNING. Under the naive reading, a finding
> that legibility requires prior exposure falsifies INV-057; under the sharpened reading it does
> not, because self-experience with one's own state IS the relevant exposure -- and that is
> exactly MECH-182's mechanism.
>
> **COUNTEREXAMPLE (what would refute Leg 1), in descending order of decisiveness:**
> (1) **The domestication confound resolved against the claim** -- the cleanest available
> counterexample and one the claim's current notes never state. Dogs are the *worst* test case:
> ~15k years of co-evolution with humans could plausibly have selected for human-directed
> signalling, which is a shared-history explanation, not a functional-specificity one. A
> well-powered failure to replicate automatic cross-species affect reading in a **non-domesticated,
> phylogenetically distant species pair** would show the effect is carried by co-evolutionary
> history, not by causal generation from shared functional states.
> (2) A well-powered demonstration that naive perceivers with no prior exposure to the emitting
> species perform at chance, and that accuracy is a monotone function of species-specific
> exposure -- convention/statistical learning, not causal generation.
> (3) A demonstration that the acoustic/behavioural features carrying the effect are **arbitrary
> with respect to the production physiology** -- i.e. that the same functional state produces
> systematically different signals across populations with matched physiology, which is what a
> conventional signal looks like and what a causally-generated one cannot be.
>
> **CONFIRMING (Leg 1):** replication of the blind-perceiver and untrained cross-modal results,
> extended to at least one non-domesticated species pair, with accuracy invariant to prior
> exposure to the emitting species.
>
> **NOTE ON SCOPE:** no REE run, of any substrate generation, can confirm or falsify Leg 1. A
> MECH-191 Leg A pass is a REE-internal *analogue* of the causal-generation conclusion, not
> evidence about biology. Treating REE evidence as confirmation of Leg 1 (or biological evidence
> as confirmation of the REE leg) is the fusion this split exists to prevent.

**Proposal sketch (only for a/d):** n/a.

**depends_on additions (if any):** none. `[MECH-191]` is correct and is exactly the pointer Leg 2
needs.

**GOVERNANCE FLAG:** `contested_disposition` -- INV-057 is `claim_type: invariant` /
`invariant_type: universal`, so with no explicit `epistemic_category` the indexer resolves
`substrate_coherence` and suppresses promote/demote as if it were a foundational REE design
choice. It is not: it is an argument from comparative ethology with 5 literature entries and zero
experimental entries, and its architectural half is already owned by MECH-191. Recommend setting
`epistemic_category: out_of_domain` explicitly, and opening a separate review of whether
`claim_type` should become `research_anchor` (precedent RA-001/002/003; SOC-HUM-1..4 show the
`out_of_domain` + `functional_restatement` pattern). Not proposed as an in-place `claim_type` edit
-- `REE_assembly/CLAUDE.md` forbids that; it needs the supersede-with-new-claim route or an
explicit governance decision. **Do not retire or merge INV-057:** ARC-117 lists it in
`related_claims`, and the argument-form content (legibility-as-evidence-for-functional-specificity)
is genuinely not stated anywhere else.

---

### MECH-182 -- Vocalization timbre as learned cross-modal harm-approach signal, generalizing to other-agent vocalizations

**Recommended disposition:** (c) substrate-blocked, `substrate_conditional` -- but with the most
useful finding in the group attached: **Leg A is blocked on ONE small build (an arousal-modulated
self-produced observable that re-enters the agent's own observation) plus a knob flip, NOT on the
whole ARC-047 social stack**, which makes it the group's cheapest unblock; only Leg B needs the
full social substrate.

**Extracted from:** **MECH-183's already-drafted `what_would_answer`, rejected-proxy (b)** --
"cross-modal z_beta activation from a correlated same-agent cue (tests sensory association
learning, i.e. MECH-182, not social attribution)". That proxy was rejected *for MECH-183's
purposes* and explicitly labelled as testing MECH-182; for MECH-182 it is the correct design and
it was already written. Plus the 2026-04-05 intake's seven structural steps
(`evidence/planning/thought_intake_2026-04-05_steve_dog_emotional_mirroring.md`, MECH-182 section),
which supply the Leg A / Leg B cut (steps 1-4 vs steps 5-7). Plus MECH-191's Leg A precondition
shape. Not drafted fresh.

**Currency check:** (a) MECH-182 has 3 literature entries (`lit:neuroimaging_comparative` x2,
`lit:review`), `exp_conf 0.0`, `genuine_exp_count 0`, `plausible_unproven`; latest entry is the
2026-04-05 Yu 2024 rodent-contagion literature record, not a run. (b) **The learner exists but is
default-off and floored** -- `BLAAttributionHead`, `ree-v3/ree_core/amygdala/attribution_head.py`
(SD-035 / MECH-074d) implements the trainable attribution head, but
`ree_core/utils/config.py:6017` sets `bla_attribution_head: str = "contribution_threshold"`, the
fixed non-trainable rule; that module's own docstring says the fixed rule "has no learned
component ... and no mechanism by which it could become more selective with experience". Its
selectivity is additionally at a documented competence floor: V3-EXQ-894 and V3-EXQ-894a both
FAIL/weakens, autopsy `failure_autopsy_V3-EXQ-894a_2026-08-08` = `competence_implementation_gap`,
per-seed pattern (one selective, one context-blind-deterministic, one null) stable across a
4-point sigma sweep. (c) **The signal does not exist at all** -- zero `vocal` / `timbre` /
`acoustic` / `cross_modal` hits under `ree_core/` (2026-09-04); `BreathOscillator`
(`ree_core/heartbeat/clock.py`, MECH-108) is a cyclic internal phase counter, **not** an emitted
or re-perceived observable, so it does not satisfy the requirement despite being the nearest
existing thing. `body_obs` exists (`ree_core/latent/stack.py`, `ree_core/agent.py`,
`ree_core/environment/causal_grid_world.py`) and is the plausible carrier if one were built.
(d) Leg B's substrate (other-agent model, OTHER_SELFLIKE, attribution stream) re-confirmed absent
2026-09-04 -- identical to MECH-183's and MECH-191 Leg B's findings. (e) MECH-182 is in no plan's
`scope_claims`, though its generalisation MECH-191 is in `fast_empathy_v5_plan.md`.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v5` for consistency with MECH-405/ARC-047, noting that Leg A alone
could be pulled earlier if the self-observable is built -- governance may prefer to record that
asymmetry rather than tag the whole claim v5).

**Draft `what_would_answer`:**

> **MECH-182 IS CONJUNCTIVE across a LEARNING step and a GENERALISATION step, with very different
> readiness -- split it, mirroring MECH-191's Leg A/Leg B pattern. The intake's own seven
> structural steps give the cut: steps 1-4 are Leg A, steps 5-7 are Leg B.**
>
> **LEG A -- SELF-EXPERIENCE CROSS-MODAL LEARNING (intake steps 1-4). Blocked on one small build
> plus a knob, not on the social stack.** The assertion: an arousal-modulated, self-produced
> observable becomes, through experience, a learned predictor of harm-approach, acquired by the
> harm attribution stream. This is the leg carrying MECH-182's novelty -- the acoustic substrate
> itself is already documented (Andics 2014, Balint 2022); what is novel is that the mapping is
> *learned from self-experience*.
>
> **NON-DEGENERACY PRECONDITION (Leg A) -- three gates, all currently unmet:**
> (1) **A self-produced observable must exist**: some agent-emitted quantity that (i) is modulated
> by arousal (the natural carrier is z_beta, which is live in `ree_core/latent/stack.py` as the
> shared affective latent) and (ii) **re-enters the agent's own observation stream** so that an
> association can be learned over it. Confirmed absent 2026-09-04: no vocal/timbre/acoustic
> channel anywhere under `ree_core/`, and `BreathOscillator` (`ree_core/heartbeat/clock.py`) is an
> internal phase counter that is neither emitted nor re-perceived and therefore does **not**
> satisfy this gate.
> (2) **The trainable attribution head must be ON and above its competence floor**:
> `bla_attribution_head` must be set to `"trainable"` -- it **defaults to
> `"contribution_threshold"`** (`ree_core/utils/config.py:6017`), a fixed rule which by its own
> module docstring cannot acquire a cue-outcome association at all. A run on the default knob
> tests a fixed threshold and can neither confirm nor falsify a LEARNED association; it must
> self-route `substrate_not_ready`. Additionally the head's attribution selectivity must clear the
> V3-EXQ-894a competence floor on at least 2/3 seeds (autopsy
> `failure_autopsy_V3-EXQ-894a_2026-08-08`, `competence_implementation_gap`) -- otherwise a null
> is attributable to the head, not to the claim.
> (3) **Joint non-degenerate variance** (same shape as MECH-191 Leg A's precondition): the
> candidate observable must vary with arousal across the run, AND harm-approach episodes must both
> occur and fail to occur. An observable pinned to a constant, or a harm-approach rate at 0 or 1,
> tests nothing.
>
> **CONFIRMING (Leg A):** with gates (1)-(3) satisfied, the agent's harm-approach signal (the
> z_harm_a forward model, `ree_core/predictors/e2_harm_a.py`) comes to be driven by the
> self-observable at a lead time it did **not** have at initialisation -- predictive gain from the
> observable rises across training and exceeds a **shuffled-observable control** by a margin
> scaled on the SD of the cross-seed delta plus an absolute floor, on at least 2/3 seeds -- AND
> ablating the observable channel (not merely decorrelating it) degrades harm-approach lead time
> back toward the shuffled control. The association must be shown **acquired**: a matched agent
> trained with the observable held constant must NOT show the gain.
>
> **FALSIFYING (Leg A):** the predictive gain is already present at initialisation -- the mapping
> is architectural, not learned, which falsifies the "learned from self-experience" step that is
> MECH-182's entire novelty over the classical acoustic literature; OR, with the head trainable
> and the floor cleared, the gain never rises above the shuffled-observable control across
> training on at least 2/3 seeds -- which falsifies the cross-modal association itself.
>
> **LEG B -- CROSS-AGENT GENERALISATION (intake steps 5-7). BLOCKED, identical gate to MECH-191
> Leg B.** The assertion: the learned association transfers, so the same feature in ANOTHER
> agent's output activates the observer's harm-approach signal via the attributed other-model.
> **RELEASE CONDITION: see MECH-191's own `what_would_answer` Leg B RELEASE CONDITION -- ARC-047
> (broadcast channel) plus ARC-010/MECH-031/MECH-032 (other-agent modelling), both re-confirmed
> absent 2026-09-04. Do not re-derive it; MECH-182 implies no build beyond what MECH-183/MECH-191
> already require.** Do **not** substitute a scripted-partner or simulated-other-distress proxy:
> MECH-183's own `what_would_answer` already evaluated and rejected that (its proxy (a)) as
> non-diagnostic -- a PASS would not validate and a FAIL would not invalidate.
> **CONFIRMING (Leg B, once substrate exists):** the same observable carried by an OTHER agent
> activates the observer's harm-approach signal, and the transfer is gated by OTHER_SELFLIKE
> tagging (present vs absent) rather than by raw feature similarity.
> **FALSIFYING (Leg B):** transfer occurs at statistically indistinguishable magnitude with
> OTHER_SELFLIKE off as on -- this falsifies the "via the attributed other-model" step and reduces
> MECH-182 to plain stimulus generalisation, which is not a novel claim.
>
> **ORDER CONSTRAINT:** Leg B is uninterpretable before Leg A passes. If the self-experience
> association was never learned, there is nothing to generalise, and a Leg B null measures the
> absent Leg A rather than the generalisation step.

**Proposal sketch (only for a/d):** n/a as a queueable experiment -- but recording the **cheapest
unblock in the group** for the substrate queue, since it is materially smaller than everything
else here: a single self-produced, arousal-modulated observable that is written into the agent's
own observation (natural carrier: a scalar derived from z_beta, delivered alongside `body_obs`),
plus flipping `bla_attribution_head` to `"trainable"` and clearing the V3-EXQ-894a floor. That
combination makes MECH-182 Leg A testable **without any multi-agent substrate at all**. It should
be a `substrate_queue.json` entry; it currently is not one.

**depends_on additions (if any):** add **MECH-074d / SD-035** (the `BLAAttributionHead` the
learning step actually runs in -- MECH-182 names "the harm attribution stream" in prose but has no
dependency on the mechanism that implements it, which is why the default-off knob and the
competence floor went unnoticed against this claim) and **ARC-047** (Leg B's broadcast channel).
Existing `[INV-005, MECH-031, MECH-032]` all stay.

**GOVERNANCE FLAG:** `stale_note` -- MECH-182's registered mechanism ("this cross-modal
association is learned from self-experience by the harm attribution stream") presumes an
attribution learner that is (a) **default-off** (`ree_core/utils/config.py:6017`,
`bla_attribution_head = "contribution_threshold"`, the fixed non-trainable rule) and (b) at a
**documented competence floor** (V3-EXQ-894 / V3-EXQ-894a both FAIL/weakens, autopsy
`failure_autopsy_V3-EXQ-894a_2026-08-08` = `competence_implementation_gap`). Neither fact is
recorded against MECH-182, and either alone would make a Leg A run vacuous. Per
`REE_Working/CLAUDE.md` ("a claim can be `active` while its knob is default-off; check the knob,
not the status"), this belongs in the claim's own text.

---

### MECH-192 -- Signal legibility is prerequisite for fast empathy coordination: z_beta leakage (MECH-183) requires perceivable signals that map onto observer's own functional states

**Recommended disposition:** (g) **merge with sibling -- PROPOSE ONLY: PARTIAL absorption into
MECH-191 Leg B / MECH-183, retaining a narrowed residual.** As registered the claim is close to
analytic and its empirical content is already covered twice over; the residual that is genuinely
unowned is the **signal-side** ablation (energy- and information-matched scramble at fixed
coupling), which neither MECH-191 Leg B (which ablates the RECEIVER) nor MECH-183 (which ablates
the COUPLING) performs.

**Extracted from:** MECH-191's already-drafted Leg B (the receiver-ablation falsifier that absorbs
MECH-192's necessity framing); MECH-183's already-drafted `what_would_answer` (the OTHER_SELFLIKE
ON/OFF 2x2 that absorbs the coupling half, and the rejected-proxy list); the 2026-04-06 intake
section 1 "The legibility condition" and the MECH-192 block. The residual manipulation is the one
piece I derived, and only because the extraction showed nobody owns it.

**Currency check:** (a) MECH-192 has 3 literature entries, `exp_conf 0.0`, `genuine_exp_count 0`,
`plausible_unproven`; `latest_run_id` is the Albuquerque 2016 literature entry. (b) Its named
dependency **MECH-183 has no experimental evidence either** (`exp_conf 0.0`, 5 lit entries) and
its `what_would_answer` records the substrate as confirmed absent (IGW-200 feasibility assessment
`exp_0137_mech_183_feasibility_assessment.md`, 2026-06-11), which I independently re-confirmed
2026-09-04. So MECH-192's prerequisite-of-a-prerequisite is itself unpinned. (c) MECH-192 has
three reverse-references -- **ARC-048 `depends_on: [..., MECH-192]`**, ARC-115
`related_claims`, ARC-117 `related_claims` -- so a full retirement would strand ARC-048; partial
absorption is the only safe route. (d) MECH-192 is in no plan's `scope_claims`, despite MECH-183
and MECH-191 both being in `fast_empathy_v5_plan.md`'s. (e) MECH-192 has become the registry's
standing example of "the nearest live analogue is z_beta leakage, which is affective not
propositional" -- both ARC-115 and ARC-117 use it that way in their notes, which is a further
reason to keep the id alive.

**epistemic_category (proposed):** `substrate_conditional`
(with `implementation_phase: v5`, matching MECH-405/MECH-505/ARC-047).

**Draft `what_would_answer` (for the NARROWED RESIDUAL):**

> **AS REGISTERED, MECH-192 IS NEARLY ANALYTIC and therefore not yet falsifiable.** "z_beta
> leakage can only produce functional state-matching if the perceived signal maps onto a
> corresponding internal state in the observer" is a statement about what a mapping *is*, not an
> empirical prediction -- there is no world in which an unmapped signal produces state-matching.
> Its empirical content appears only when legibility becomes a **graded, manipulable variable**.
> That narrowing is the claim, and it is what the residual below states.
>
> **NARROWED RESIDUAL CLAIM:** coordination benefit from z_beta leakage is **monotone in signal
> legibility, holding attribution coupling and channel information fixed**. This is the
> SIGNAL-side ablation. It is distinct from -- and not tested by -- MECH-191 Leg B (which ablates
> the RECEIVER's homologous internal-state machinery) or MECH-183 (which ablates the COUPLING via
> OTHER_SELFLIKE ON/OFF). Nobody currently owns it.
>
> **NON-DEGENERACY PRECONDITION -- three gates, and the first two are NOT MECH-192's to satisfy:**
> (1) **MECH-191 Leg A must have PASSED.** The emitter's signal must first be shown to be a
> causal, state-specific product of the internal state; otherwise "legibility" of that signal has
> no referent and the manipulation measures channel noise. **See MECH-191's own
> `what_would_answer` Leg A precondition and criteria; do not re-derive them here.**
> (2) **MECH-183 must be PINNED.** The z_beta leakage channel must be demonstrated live and
> attribution-gated (its OTHER_SELFLIKE ON/OFF x distress-present/absent 2x2). **See MECH-183's
> own `what_would_answer`; do not re-derive it.** Grading legibility over an unpinned leakage
> channel is uninterpretable in **both** directions: a null cannot distinguish "legibility does
> not matter" from "there is no leakage to modulate", and a positive cannot distinguish leakage
> from ordinary perceptual inference.
> (3) **MECH-192's OWN gate, and the one that makes the claim falsifiable at all:** legibility
> must be manipulable as a graded variable **while attribution coupling is held fixed AND channel
> information is matched** -- i.e. a permuted/scrambled signal carrying identical information
> content and identical channel energy but no state-homology, versus the true signal, across at
> least three graded levels. Both arms must produce non-zero, non-identical coordination-cost
> variance. **Without the information-matched scramble the claim is unfalsifiable by
> construction** (any degradation is attributable to lost information rather than lost
> legibility), which is precisely the defect the current registration has.
>
> **CONFIRMING:** coordination cost (or observer state-matching accuracy) is **monotone in signal
> legibility** across the graded levels, with coupling strength and channel information held
> constant, on at least 2/3 seeds; the true-signal vs matched-scramble gap exceeds a margin scaled
> on the SD of the cross-seed delta plus an absolute floor; AND the monotone relation **survives
> ablating the observer's explicit inference/prediction pathway** toward the other's state, so the
> effect is on the leakage channel rather than on inference (the same dissociation MECH-183's
> CONFIRMING clause (2) demands, applied to the signal side).
>
> **FALSIFYING:** coordination is statistically indistinguishable between the true signal and the
> information-matched scramble at fixed coupling -- legibility is doing no work, the benefit is
> carried by information availability plus coupling alone, and MECH-192's "prerequisite" framing
> is false as an empirical claim; OR coordination tracks coupling strength but is **flat in
> legibility** across the full graded range -- same conclusion, and MECH-192 collapses entirely
> into MECH-183 with nothing left over.
>
> **RELEASE CONDITION: identical to MECH-191 Leg B -- ARC-047 (broadcast channel) plus
> ARC-010/MECH-031/MECH-032 (other-agent modelling). See MECH-191's own text. MECH-192 implies no
> build beyond what MECH-183/MECH-191 already require, plus the scramble control, which is an
> experiment-design item, not substrate.**

**Merge proposal detail (disposition (g)), for the orchestrator to route:**
- **Surviving id:** MECH-192 (narrowed), and MECH-191 (absorbing).
- **Absorbed id:** none retired. This is **partial** absorption with a narrowed residual, exactly
  the shape the brief anticipates.
- **What text moves to MECH-191 Leg B's rationale:** the necessity statement ("z_beta leakage can
  only produce functional state-matching if the perceived signal maps onto a corresponding
  internal state in the observer") and the cross-species explanatory framing (Albuquerque 2016,
  Silva 2011, "explains why fast empathy works cross-species without shared language"). Both are
  rationale for MECH-191 Leg B's receiver-ablation falsifier and read as duplication where they
  currently sit.
- **What STAYS as MECH-192:** the graded signal-side legibility manipulation with an
  information-matched scramble at fixed coupling -- the residual above. Retitle in the direction
  of "coordination benefit from z_beta leakage is monotone in signal legibility at fixed
  attribution coupling".
- **Reverse-deps needing repointing:** **none if the residual is retained** (which is the
  recommendation). For completeness, were MECH-192 retired outright, three references would need
  repointing: `ARC-048.depends_on`, `ARC-115.related_claims`, `ARC-117.related_claims` -- and
  ARC-048 would be stranded, since ARC-048's "functional states as referents" premise leans on
  MECH-192's legibility condition. That is an additional reason not to retire.

**depends_on additions (if any):** add **ARC-047** (the broadcast channel the release condition
names). Existing `[MECH-183, MECH-191]` are both correct and are exactly the two pointers gates (1)
and (2) need.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-192 as registered is near-analytic and its
empirical content is covered by MECH-191 Leg B (receiver ablation) and MECH-183 (coupling
ablation); the partial-merge proposal above narrows it to the one manipulation nobody owns (the
signal-side, information-matched scramble at fixed coupling). Requires a governance decision on
retitle + text migration, not a silent edit. Second, `stale_note` -- MECH-192 appears in no plan's
`scope_claims` although both of its `depends_on` targets (MECH-183, MECH-191) are in
`fast_empathy_v5_plan.md`'s; recommend adding it there so the residual arm is tracked against
`fast_empathy_v5:EMP-4` (the A/B/C/D dissociation node), which is the node it belongs to.

---

<!-- G7 appended 2026-09-04T21:17:34Z -->
## G7 -- hippocampal comparator / event-segment / persistent program handle  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the brief groups them on
  MECH-288 <-> SD-084 = 4.32 (SD-084 `depends_on` MECH-288; the program handle persists across
  event segments) and MECH-206 <-> MECH-288 = 3.28 (same hippocampal namespace, both comparators
  emitting a boundary/surprise signal). Both links hold, but the sharper axis after research is a
  **three-stage pipeline all three claims sit on**: `latent / PE stream -> a graded mismatch
  readout -> a consumer that must actually read it`. Each claim owns a different stage, and
  **two of the three have a hole at the consumer end while the third is the one case where that
  hole was found and closed**. SD-084's whole content is "the consumer could not see the signal
  because the handle was torn down every tick"; MECH-206's consumer (replay output) is verified
  to have *no reader anywhere in `ree_core/`*; MECH-288's consumers are built but the claim has
  been credited by exactly one synthetic run while its substrate ran live in 23 indexed
  experiments. That reframing is what drives the dispositions below.

- **(i) same-claim / merge candidates:** **No merge recommended for any pair**, but there is a
  real, already-half-acknowledged convergence to record. MECH-288's own `notes` state that
  MECH-287's "upstream anchor-side comparator stage" (Vinogradova 2001 CA1/CA3 mismatch + O'Mara
  2009 + Lisman & Grace 2005) "is best read as the BIOLOGICAL substrate that MECH-288
  instantiates computationally", and `ree_core/regulators/invalidation_trigger.py`'s module
  docstring has already executed that collapse in code ("The upstream CA1/CA3 mismatch comparator
  substrate ... is collapsed here to a subscription on the MECH-288 boundary queue"). **MECH-206
  is the third face of that same biological comparator** -- CA3 pattern-completed prediction vs
  entorhinal actual, graded output -- pointed at a *third* consumer (surprise-buffer write /
  replay priority) rather than at the region partition (MECH-288) or the broadcast trigger
  (MECH-287). So the correct architectural reading is **one graded mismatch readout with three
  consumers at three thresholds**, not three comparators. I do **not** propose merging MECH-206
  into MECH-288 because MECH-206 carries content MECH-288 does not have anywhere: the
  **bidirectional connectivity shift** (CA1-EC up / CA1-CA3 down = *retrieval suppression of the
  now-erroneous prediction*), which is a second, dissociable functional leg with no analogue in
  the segmenter. Recommended instead: `related_claims` cross-links MECH-206 <-> MECH-288 <->
  MECH-287, and a governance note folding MECH-206 into the MECH-287/MECH-288 architectural
  reconciliation that MECH-288's notes already opened and left as "a downstream governance
  decision". SD-084 is a different claim class entirely (lifetime of a handle on E3Selector) --
  no merge pressure in either direction.

- **(ii) contradictions / undercut premises:** two, both real, neither a logical contradiction.
  1. **MECH-206's premise that a graded PE magnitude is what ranks episodes for replay is
     undercut *in the built substrate* by this group's own MECH-288.** The only replay-priority
     ranker that exists in `ree_core/` is `ree_core/sleep/replay_sampler.py` (MECH-285 Phase B),
     and it draws seed anchors "with probability proportional to a softmax over the frozen
     staleness signal" -- i.e. keyed on MECH-284 staleness over `RegionKey = (scale, segment_id)`,
     **which is MECH-288's segment ID**. The functional slot MECH-206 claims for a graded CA1 PE
     signal already has an incumbent occupant sourced from MECH-288's region partition. This is
     not a contradiction (both could be true; biology plausibly uses both), but it means
     **MECH-206's falsifier must be *discriminative* against staleness-priority**, not merely
     confirmatory of PE-priority. Drafted that way below.
  2. **MECH-288's canonical "PE-spike is the primary trigger" is not what the observation path
     actually runs.** `ree_core/agent.py:5448` calls
     `event_segmenter.step(latent_dict=..., pe_dict=None, t=...)`. `event_segmenter.py:139-142`
     documents the consequence: with no `pe_dict` the fast scale falls back to
     `agg(t) = sum_s ||z_s(t) - z_s(t-1)||`, a **latent-delta magnitude, not prediction error**.
     So on the observation stream as wired today the fast/inner scale is a *change* detector, not
     the PE-threshold detector Verdict 1 named primary (Zacks 2007 EST). The rollout stream is
     different: `ree_core/policy/policy_decomposition.py:581` does pass `pe=pe_signature`. This
     undercuts the "PE-proportional" framing that MECH-206 and MECH-288 share, and it is the
     single most important non-degeneracy precondition for any MECH-288 test.

- **(iii) shared falsifier:** yes, one precondition serves all three and should be written once
  on MECH-288 and cross-referenced. Call it the **LIVE GRADED-MISMATCH PRECONDITION**: *the
  statistic actually driving the mechanism under test must (a) be the quantity the claim names
  (forward prediction error, not a latent-delta proxy -- assert `pe_dict` is supplied and
  non-empty on the stream under test), and (b) have non-zero cross-tick variance and a
  non-saturated dynamic range over the measurement window.* MECH-206's draft below points at
  MECH-288's copy of this rather than re-deriving it. SD-084's own precondition is the
  reachability half of the same idea and is already discharged (V3-EXQ-839).

- **(iv) cross-cutting finding:** **two mutual confounds, and one template.**
  *Confound 1:* a null on MECH-206 is uninterpretable until a replay CONSUMER exists --
  `substrate_queue.json` entry `mech092-replay-consumer-missing` records, VERIFIED against source
  2026-09-01, that `Agent._do_replay` (agent.py:10366) computes `replay_trajs` and "ENDS at
  :10428 without ever reading the variable", with "no reader of replay output anywhere" in
  `ree_core/`. Every downstream consequence MECH-206 predicts is measured on replay output.
  *Confound 2:* a null on any MECH-288 downstream falsifier is uninterpretable while the
  observation-path fast scale is running the latent-delta fallback (see (ii).2) -- a null would
  be about a detector the claim does not describe. *Template:* SD-084 is the worked example of
  exactly this failure mode caught and fixed -- V3-EXQ-830 recorded
  `decomp_n_evaluated_midexec = 0` in all 10 cells against `precommit` 1862-2618, was correctly
  diagnosed `competence_implementation_gap` **not** `substrate_ceiling`, and the repair made the
  hook reachable (V3-EXQ-839: 415 vs 0). The group's lesson, stated once: **before any of these
  claims is read as ceilinged, check that its consumer exists and reads.**

- **Currency findings (all verified this pass, with the file checked):**
  1. **MECH-288's substrate is BUILT and the Phase-2 integration half of its promotion bar has
     LANDED** -- `ree_core/hippocampal/event_segmenter.py` exists; `substrate_queue.json` shows
     `MECH-269 | implemented`, `MECH-284 | implemented`, `MECH-287 | implemented`,
     `MECH-288 | implemented`. The claim's `evidence_quality_note` (2026-07-14) still describes
     "integration into Phase 2 (ii)+(iii)+(iv) downstream substrate plus the falsifiable
     predictions" as the open gate. **Half of that gate is now closed**; only the falsifiable
     predictions remain. Stale as written.
  2. **`use_event_segmenter` defaults to `False`** (`ree_core/utils/config.py:2761`) -- MECH-288
     is `provisional` with a default-OFF knob, exactly the "check the knob, not the status" case.
     It is nonetheless enabled in **23 indexed runs** (scan of `evidence/experiments/*.json`
     configs), from V3-EXQ-646 (2026-06-06) through V3-EXQ-938 (2026-08-18).
  3. **None of those 23 runs carries `MECH-288` in `claim_ids`.** `claim_evidence.v1.json` gives
     MECH-288 `experimental_confidence 0.66` from `genuine_exp_count: 1` -- the single synthetic
     isolation run V3-EXQ-757 -- against `literature_confidence 0.86` / 11 lit entries, quadrant
     `confirmed_established`, `overall_confidence 0.81`. The live substrate has been running
     under 22 other experiments and credits the claim nowhere. Flagged.
  4. **The rollout-side caller MECH-288's own code says does not exist, exists.**
     `event_segmenter.py:34` reads "nothing yet calls with `input_stream="rollout"` until
     ARC-070/MECH-321 lands"; `policy_decomposition.py:532/546/581` calls
     `boundary_on(stream="rollout", ...)`, and V3-EXQ-938 records
     `boundary_fires_mean_pe_arm 276.95` / `boundary_fires_mean_yoked_arm 287.325` over 40 seeds.
     Substrate docstring stale; the claim's 2026-07-24 note is correct.
  5. **MECH-206 has ZERO indexed evidence of any kind** -- `claim_evidence.v1.json` returns
     `null` for MECH-206 (its two `source:` literature records are filed under MECH-205's
     targeted review and credited there). Its dependency MECH-205 is `stable` (2 PASS / 1 FAIL,
     exp_conf 0.668); MECH-092 exp_conf 0.66; MECH-256 exp_conf 0.0. The 2026-09-01 `SD-003 ->
     MECH-256` repoint on MECH-206's `depends_on` is present and correctly annotated in the live
     block.
  6. **MECH-206's own comparator has no substrate and no substrate_queue entry.** Grep of
     `ree_core/` finds no `surprise_buffer` / `SurpriseBuffer` symbol and no CA1-style
     two-channel comparator; the only CA1 reference is `invalidation_trigger.py`'s docstring
     saying that comparator is *collapsed away* into a BoundaryEvent subscription. What does
     exist is MECH-205's single-channel path: `config.surprise_gated_replay` (default `False`,
     `config.py:3350`) writing a PE-magnitude scalar into the `VALENCE_SURPRISE` residue channel
     (`agent.py:10677-10726`), with `pe_surprise_threshold` promoted to `1e-5` by GFLAG-0075 on
     2026-09-01. That is a *graded PE tag*; it is not a two-channel prediction-vs-actual
     comparator and it does not write a ranked buffer.
  7. **`closure_status.md:409` is NOT stale (checked, and I am recording the negative result).**
     The row `hippocampal_planning_v4:HPL-6` reads "MECH-205 surprise buffer + MECH-206 CA1 PE
     comparator present (sleep_substrate stack)" in the *prerequisite* column of a row whose
     status is `blocked` -- it states an unmet precondition, not a presence assertion. No flag.
  8. **SD-084's substrate is present and its validating run has landed and been reviewed.**
     `E3Selector._persistent_committed_trajectory` set at `e3_selector.py:4122`, declared
     `:543`; flag `use_persistent_committed_program_handle` default `False`
     (`config.py:5380`); consumer union at `agent.py:6799-6811`; liveness invariant enforced
     unconditionally at `agent.py:6771-6772` (`if not self.beta_gate.is_elevated: ... = None`)
     immediately upstream of its only consumer. `V3-EXQ-839` manifest: `outcome PASS`,
     `total_midexec_on 415`, `total_midexec_off 0`, `n_on_cells_attributable_with_midexec 4/4`,
     `negative_control_expectation_held true`, `non_degenerate true`. In
     `review_tracker.json`'s `reviewed_run_ids`. Contract
     `tests/contracts/test_mech321_midexec_natural_reachability.py` present.
  9. **SD-084's 2026-08-10 routing note is stale and its chip_ref does not exist.** The note
     says "Routing: queue a successor MECH-321 R4 EVIDENCE experiment (new EXQ,
     claim_ids=[MECH-321]) testing the behavioural/task effect ... Chipped
     `chip-20260810-mech321-r4-behavioural-effect`." That experiment **already ran nine days
     earlier**: `v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3`,
     `claim_ids: ["MECH-321"]`, `outcome FAIL`, `evidence_direction weakens`,
     `non_degenerate true`, label `midexec_decomposition_does_not_reduce_harm`
     (`harm_delta_mean_post_divergence -0.00326`, `rel_improvement -0.0696`,
     `effect_size_ok false`), and it is in `reviewed_run_ids`. Grep of `TASK_CHIPS.json` finds
     **no** `chip-20260810-mech321-r4-behavioural-effect`; the real chip is
     `chip-20260731-mech321-r4-successor`, `status done`, resolved `2026-07-31T19:23:09Z` --
     i.e. resolved the day *before* 844 ran. Flagged.
 10. **SD-084 carries `evidence: []` and `claim_evidence.v1.json` returns `null` for it**, which
     is *correct by construction* (V3-EXQ-839 was declared `claim_ids: []` so it weights
     nothing) but means the index shows a validated design decision as evidence-free. Flagged as
     an attribution question for governance, not as a defect in the run.

---

### MECH-206 -- CA1 acts as a PE-proportional comparator that writes episodes to the surprise buffer

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`** (not
`substrate_ceiling`): the CA1-equivalent two-channel comparator the claim's own "REE architectural
implication" paragraph specifies has never been built, and the consumer its predictions are
measured on (replay output) is verified to have no reader anywhere in `ree_core/`, so zero
non-degenerate attempts have been possible and none has been banked either way.

**Extracted from:** the claim's own `notes` -- its two explicit `Predicts:` clauses ("(1)
disrupting CA1 activity specifically (not CA3 or DG) should impair surprise buffer population
while leaving forward replay intact; (2) the CA1 mismatch signal during replay should correlate
with which features the agent subsequently treats as causally relevant") and the load-bearing
gradedness argument ("A binary match/mismatch flag would not support the priority ordering
MECH-205 requires"). Non-degeneracy precondition cross-referenced from MECH-288 rather than
re-derived (see preamble (iii)). Discriminative arm added from the MECH-285 incumbent found this
pass.

**Currency check:** (a) `claim_evidence.v1.json` -> MECH-206 is `null`: no experimental and no
literature entries credited to it. (b) `grep -rln "surprise_buffer\|SurpriseBuffer" ree_core/` ->
no matches; the only `CA1` string in `ree_core/` is
`ree_core/regulators/invalidation_trigger.py:15`, which states the CA1/CA3 comparator is
*collapsed* into a MECH-288 BoundaryEvent subscription with "No PE or latent input". (c) What
does exist is MECH-205's single-channel write: `config.surprise_gated_replay` default `False`
(`ree_core/utils/config.py:3350`), `pe_surprise_threshold 1e-5` (`:3365`, raised from 0.001 by
GFLAG-0075 2026-09-01), writing to `VALENCE_SURPRISE` at `agent.py:10677-10726`. (d) The
downstream is dead: `substrate_queue.json` -> `mech092-replay-consumer-missing`,
`status: proposed_REGISTRATION_ONLY_not_a_build_authorisation`, `unblocks_claims: [MECH-092,
MECH-205]`, implementation_hint verified against source 2026-09-01. (e) The only *built*
replay-priority ranker is `ree_core/sleep/replay_sampler.py` (MECH-285 Phase B), which ranks on
MECH-284 staleness keyed on `(scale, segment_id)` -- MECH-288's key -- is explicitly "a NO-OP
CONSUMER", and is default-off (`use_mech285_sampler`). (f) `closure_status.md:409` HPL-6 lists
"MECH-205 surprise buffer + MECH-206 CA1 PE comparator present" as an *unmet prerequisite* of a
`blocked` row -- consistent with all of the above, not a contradicting note.

**epistemic_category (proposed):** `substrate_conditional`

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three conjuncts, all measured on the run's own data; the run is
> unreadable until all three hold).**
> (1) *Comparator exists and both channels are live.* A CA1-equivalent submodule must receive two
> genuinely distinct inputs on the same tick -- a CA3-like pattern-completed anchor
> representation and an entorhinal-like actual/variation representation -- and the run must
> report non-zero cross-tick variance in BOTH channels separately, plus a channel-decorrelation
> floor (|corr(ch_CA3, ch_EC)| < 0.95 over the window). A single-channel residual computed from
> one stream is MECH-256's comparator, not this claim's: if only one channel varies, the run
> self-routes `substrate_not_ready_requeue` and says nothing about MECH-206.
> (2) *The mismatch statistic is PE, not a latent delta.* See MECH-288's own
> `what_would_answer` LIVE GRADED-MISMATCH PRECONDITION -- **do not re-derive it**. The identical
> hazard applies here: `agent.py:5448` currently passes `pe_dict=None` to the one comparator-ish
> substrate that exists, which silently degrades it to `sum_s ||z_s(t) - z_s(t-1)||`
> (`event_segmenter.py:139-142`). Any MECH-206 test must assert its mismatch input is forward
> prediction error and record which quantity it used.
> (3) *The consumer reads.* Replay output must be consumed by something. As of 2026-09-01
> (`substrate_queue.json:mech092-replay-consumer-missing`, verified against source) `_do_replay`
> discards `replay_trajs` and no reader exists in `ree_core/`, so every DV below is currently
> unmeasurable. The run must report a non-zero count of replayed episodes that reached a
> consumer; a zero here is a substrate verdict, never a claim verdict.
>
> **CONFIRMING (two legs; leg A is the priority claim, leg B the suppression claim -- the claim
> is fully confirmed only by both, and leg A alone is the weaker "PE-tagging" reading).**
> *Leg A -- graded PE ranks replay, and does so better than the incumbent staleness ranker.*
> Three arms at matched seeds and matched replay budget: (i) CA1-comparator PE-magnitude
> priority; (ii) MECH-285 staleness priority (`replay_sampler.py`, the built incumbent); (iii)
> BINARISED CA1 priority -- the same comparator thresholded to a match/mismatch flag, which is
> the claim's own stated null ("a binary flag would not support the priority ordering MECH-205
> requires"). CONFIRMED requires BOTH: (a) rank correlation between per-episode CA1 mismatch
> magnitude and post-replay forward-model improvement on that episode's content, Spearman
> rho >= 0.3 with the 95% CI excluding 0 across >= 6 seeds; AND (b) arm (i) beats arm (iii) on
> forward-PE reduction per replay slot by a margin exceeding max(1.0 x SD of the per-seed delta,
> an absolute floor of 2% relative), with consistent sign across seeds. Arm (ii) is reported as
> the competitive baseline: MECH-206 is confirmed *as the priority signal* only if (i) is not
> beaten by (ii); if (ii) wins, MECH-206 survives only as a tagging mechanism and the priority
> claim is transferred to MECH-284/MECH-288.
> *Leg B -- retrieval suppression (Bein 2020 bidirectional shift).* On high-mismatch ticks the
> agent's reliance on the pattern-completed prediction must FALL within the same or the next
> tick: the weight/gate on the CA3-like channel into downstream selection drops monotonically
> with mismatch magnitude, with a non-zero negative slope whose CI excludes 0, and the effect
> must be specific -- no equivalent drop on a matched control channel (the EC-like actual input,
> which Bein 2020 predicts should go UP).
>
> **FALSIFYING.**
> With all three preconditions green: (a) mismatch magnitude does not rank-order post-replay
> improvement (rho CI includes 0), OR the graded arm is statistically indistinguishable from the
> BINARISED arm (iii) -- the latter is the sharpest falsifier available, because it directly
> refutes the claim's load-bearing gradedness argument while leaving "CA1 tags surprising
> episodes" intact; (b) the CA3-channel reliance does not fall with mismatch, or falls
> symmetrically on the control channel (no bidirectional shift -- a generic arousal/gain effect,
> not the claimed connectivity dissociation); (c) a CA1-specific lesion impairs forward replay
> as much as it impairs buffer population (the claim's Predict-(1) requires the dissociation, not
> just the impairment). Any of (a)+(b) together refutes the claim as stated; (a) alone with (b)
> holding demotes it to "CA1 tags, something else ranks".

**Proposal sketch (only for a/d):** n/a -- blocked. What must land first, in order:
(1) a replay CONSUMER (`mech092-replay-consumer-missing`, currently REGISTRATION-ONLY and
explicitly *not* a build authorisation; note its own scope-honesty caveat that it unblocks
MECH-092's benefit half and MECH-205 leg (iii) only); (2) a two-channel CA1-equivalent comparator
submodule, which has **no substrate_queue entry at all** and needs one before it can be built.
Until (1) and (2), MECH-206 is `complex (probe-gated)` only in the trivial sense that the probe
cannot be run.

**depends_on additions (if any):** none required (MECH-205 / MECH-092 / MECH-256 are correct, and
the 2026-09-01 SD-003 -> MECH-256 repoint is sound). Recommend adding `related_claims:
[MECH-288, MECH-287, MECH-285]` -- MECH-288/MECH-287 as the same-comparator convergence (preamble
(i)), MECH-285 as the incumbent occupying the replay-priority slot (preamble (ii).1).

**GOVERNANCE FLAG:** `contested_disposition` -- **MECH-206's functional slot has an incumbent
from within its own dependency graph.** The claim argues a graded CA1 PE readout is required to
rank episodes for replay ("a binary match/mismatch flag would not support the priority ordering
MECH-205 requires"). The only replay-priority ranker actually built,
`ree_core/sleep/replay_sampler.py` (MECH-285 Phase B), ranks by MECH-284 staleness keyed on
MECH-288 `(scale, segment_id)` -- a different signal for the same job. Governance should decide
whether MECH-206 is (i) an alternative to be tested discriminatively against MECH-285 (leg A arm
(ii) above), or (ii) complementary (tagging vs region-staleness at different timescales), and
record the decision on both claims. Also worth recording that MECH-206's comparator has no
`substrate_queue.json` entry, so it is currently invisible to the build pipeline.

---

### MECH-288 -- Event-segment detection: two-level hierarchical detector emitting outer.inner segment IDs

**Recommended disposition:** **(a) testable now** -- the substrate is built, live in-agent, and
its downstream Phase-2 consumers are all `implemented`; what has never been run is the claim's
own **primary** falsifiable prediction (boundary alignment with task-natural transitions at
above-chance rate with a bounded false-positive rate), and that is a V3-tractable experiment that
can be authored today against instrumentation the fleet already emits.

**Extracted from:** the claim's own `functional_restatement`, which already carries three
pre-registered falsifiers -- "Falsifiable (primary)" (boundary at task-natural event transitions
above chance, bounded FP rate over a noise baseline, with the hierarchical slow/fast alignment
split), "Falsifiable (secondary, downstream usefulness)" (anchor-set partitions keyed on
segment_ids beat uniform place-binning on anchor-reset latency, re-running EXQ-475 with MECH-288 +
MECH-269), and "Falsifiable (tertiary, MECH-287 coupling)" (lesioning MECH-288 silently lesions
MECH-287's broadcast trigger while tonic-arousal modulation survives). My job here is to turn
those into house structure and to add the non-degeneracy precondition they lack -- **not** to
design a new test. The precondition is new and is the substantive addition.

**Currency check:** (a) Substrate BUILT: `ree_core/hippocampal/event_segmenter.py`
(`BoundaryEvent`, `boundary_on()`, per-stream isolated detectors). (b) Default-OFF:
`use_event_segmenter: bool = False` at `ree_core/utils/config.py:2761` -- status `provisional`,
knob off. (c) Downstream Phase 2 (ii)/(iii)/(iv) ALL LANDED per `substrate_queue.json`:
`MECH-269 implemented`, `MECH-284 implemented`, `MECH-287 implemented` ("Invalidation trigger --
Phase 2(iv) ... BoundaryEvent subscriber"), `MECH-288 implemented`; the claim's 2026-07-14
`evidence_quality_note` still frames that integration as an open gate. (d) The claim's tertiary
falsifier is now *architecturally guaranteed* rather than open:
`ree_core/regulators/invalidation_trigger.py` docstring -- "The trigger is a BoundaryEvent
subscriber, NOT an independent comparator ... Trigger output is strictly a function of
(boundary_events, config). No PE or latent input", with the dissociation named as its own test
C5. (e) Exercised live in **23 indexed runs** (config scan of `evidence/experiments/*.json`),
V3-EXQ-646 -> V3-EXQ-938; V3-EXQ-938 records `boundary_fires_mean_pe_arm 276.95` /
`boundary_fires_mean_yoked_arm 287.325` over 40 seeds. (f) **None** of the 23 credits MECH-288:
`claim_evidence.v1.json` -> `genuine_exp_count 1`, `experimental_confidence 0.66`, sole
`latest_run_id` V3-EXQ-757 (2026-07-14, PASS/supports, action-free synthetic isolation),
`literature_confidence 0.86` / 11 entries, `overall_confidence 0.81`,
`evidence_quadrant confirmed_established`. (g) V3-EXQ-757 is in `reviewed_run_ids`. (h) **Spec
divergence found this pass:** `agent.py:5448` passes `pe_dict=None`, so the observation-path fast
scale runs the documented latent-delta fallback `sum_s ||z_s(t)-z_s(t-1)||`
(`event_segmenter.py:139-142`) rather than the PE-threshold detector Verdict 1 names primary;
the rollout path does pass PE (`policy_decomposition.py:581`). (i) Stale substrate docstring:
`event_segmenter.py:34` says nothing calls `input_stream="rollout"` yet -- `policy_decomposition.py`
does, and has since ARC-070/MECH-321 landed.

**epistemic_category (proposed):** `standard` (V3-tractable; substrate built and exercised; the
missing element is a run that measures the claim's own prediction, not substrate enrichment --
so explicitly **not** `substrate_ceiling` and **not** `substrate_conditional`).

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (the LIVE GRADED-MISMATCH PRECONDITION; MECH-206 and any other
> consumer claim should cross-reference this text rather than re-derive it).** Four conjuncts,
> all asserted from the run's own manifest:
> (1) *The segmenter is on and firing.* `use_event_segmenter=True` and boundary fires > 0 on
> BOTH scales in the measurement window on every measured cell. (V3-EXQ-938's
> `boundary_fires_mean_* ~= 277-287` shows this instrumentation already exists.)
> (2) *The trigger under test is the trigger the claim names.* The run MUST record which fast-scale
> input it used. `agent.sense()` currently calls `step(..., pe_dict=None, ...)`
> (`agent.py:5448`), which per `event_segmenter.py:139-142` degrades the fast scale to a
> latent-delta magnitude `sum_s ||z_s(t) - z_s(t-1)||`, NOT the PE-spike trigger of Verdict 1.
> A run that leaves `pe_dict` unset is testing the latent-change detector and must say so; it
> cannot be read as evidence for or against the PE-threshold commitment.
> (3) *Specificity is asserted per scale, not pooled.* Per V3-EXQ-757's own recorded caveat, the
> fast/inner PE-threshold scale "fires ~15% on ANY stationary z-score stream by construction",
> so it is a gradedness readout only. Any hit-rate gate must be stated separately for slow/outer
> (specificity-bearing) and fast/inner (descriptive), and the fast scale's ~15% construction
> floor must be the chance baseline it is compared against -- never 0.
> (4) *Ground-truth boundaries are independently defined.* The task-natural transition labels
> (goal-cell arrival, harm onset, mode switch, episode-phase change) must be emitted by the
> environment/harness, not derived from any quantity the detector itself consumes; otherwise the
> alignment metric is circular.
>
> **CONFIRMING (primary -- the claim's own pre-registered prediction, now made measurable).**
> An agent with MECH-288 enabled produces boundaries aligned to task-natural transitions above
> chance with a bounded false-positive rate, hierarchically split as the claim specifies:
> (a) *slow/outer* boundaries align with high-level task transitions (goal switch, episode-phase
> change) -- hit rate within a +/-2-tick tolerance window exceeding the shuffled-label chance
> baseline by more than max(1.0 x SD of the per-seed hit-rate delta, an absolute floor of 0.15
> in hit-rate units), consistent in sign across >= 6 seeds; (b) false-positive rate on a matched
> stationary/noise stretch stays below a pre-registered ceiling (V3-EXQ-757's C288_silence
> generalised to the in-agent case -- there it was 27 A-slow vs 0 B-slow); (c) *fast/inner*
> boundaries align with within-segment perceptual transitions (place-field crossing, action
> subgoal completion) above the ~15% construction floor of precondition (3), reported with its
> own CI. *Secondary (downstream usefulness), unchanged from the claim text:* per-region V_s
> readouts keyed on segment_ids produce more informative anchor-set partitions than uniform
> place-binning, measured by anchor-reset latency (the claim names re-running EXQ-475 with
> MECH-288 + MECH-269 enabled). *Tertiary (MECH-287 coupling), now near-vacuous by construction:*
> lesioning MECH-288 silently lesions MECH-287's broadcast trigger while tonic modulation
> survives -- `invalidation_trigger.py` is a pure BoundaryEvent subscriber with "No PE or latent
> input", so this is a code-level contract, not an open empirical question; keep it as a
> regression test (its C5), not as promotion evidence.
>
> **FALSIFYING.**
> With all four preconditions green: (a) slow/outer boundary times are statistically
> indistinguishable from the shuffled-label baseline -- the detector fires, but not *where the
> events are*; or (b) the false-positive rate on the stationary stretch is high enough that the
> above-chance alignment in (a) is explained by firing rate alone (formally: alignment fails once
> the chance baseline is rate-matched to the observed fire rate -- this is the sharpest
> falsifier, and it is the in-agent generalisation of the specificity caveat V3-EXQ-757 already
> flagged); or (c) the hierarchy does not separate -- slow and fast boundaries align with the
> same class of transition at the same rate, refuting Verdict 2's two-scale commitment and
> reducing the substrate to a single detector with a redundant second parameterisation; or (d)
> segment-keyed anchor partitions do not beat uniform place-binning on anchor-reset latency,
> which would refute the *reason the claim exists* (that the V_s invalidation cluster needs a
> substrate-native region partition) even if the boundaries themselves are well-placed. (d)
> alone is the disposition-changing one: it would move MECH-288 from "the region partition" to
> "a boundary detector in search of a consumer".

**Proposal sketch (only for a/d):**
- **Title:** `V3-EXQ-<next> -- MECH-288 in-agent boundary alignment: slow/fast segment boundaries
  vs task-natural transitions, rate-matched chance baseline`
- **related_claims:** `MECH-288` (primary, `claim_ids: ["MECH-288"]` -- the point of the run),
  bears_on `MECH-269`, `MECH-284`, `MECH-287`, `ARC-070`.
- **acceptance_checks:**
  1. **Precondition gates** (all four above), each with a measured value and threshold in the
     manifest's `interpretation.preconditions` block, per house recording standard.
  2. **`pe_dict` declaration gate:** the run states explicitly, per arm, whether the fast scale
     received forward PE or ran the latent-delta fallback. Recommend running BOTH as arms -- this
     is cheap, it directly adjudicates the spec/substrate divergence flagged below, and a
     difference between them is itself a finding.
  3. **C1 (slow alignment):** hit rate vs +/-2-tick tolerance window, against a **rate-matched
     shuffled-label** baseline (not a naive uniform baseline), >= 6 seeds, effect gate
     `max(1.0 x SD of per-seed delta, 0.15 absolute)`.
  4. **C2 (bounded FP):** false-positive rate on a matched stationary stretch below a
     pre-registered ceiling; the in-agent analogue of V3-EXQ-757's C288_silence.
  5. **C3 (hierarchy separation):** slow-vs-fast alignment profiles differ across the two
     transition classes (a scale x transition-class interaction), fast scale compared against its
     own ~15% construction floor.
  6. **Negative control:** `use_event_segmenter=False` arm -- zero BoundaryEvents, zero
     MECH-287 broadcasts, bit-identical action sequences, so a null in C1 can never be confused
     with an inert arm.
  7. Ground-truth transition labels emitted by the harness and recorded in the manifest, per
     precondition (4).

**depends_on additions (if any):** none. `MECH-269 / MECH-284 / MECH-287 / ARC-070` are all
correct and all now `implemented`. (Note the deps are downstream *consumers*, not upstream
prerequisites -- unusual but deliberate and documented in the inline comments; leave it.)

**GOVERNANCE FLAG 1:** `stale_note` -- **MECH-288's promotion bar is half-satisfied and the
claim text does not say so.** The `evidence_quality_note` (2026-07-14) states the
promote-to-active gate as "integration into Phase 2 (ii)+(iii)+(iv) downstream substrate plus the
falsifiable predictions above". `substrate_queue.json` now shows MECH-269, MECH-284, MECH-287 and
MECH-288 all `implemented`, and `invalidation_trigger.py` implements the Verdict-3 subscriber
architecture exactly. The integration half has landed; only the falsifiable predictions remain.
Recommend an appended note recording that, so the next governance cycle does not re-read the gate
as wholly open. Related, lower priority: `ree_core/hippocampal/event_segmenter.py:34` still says
nothing calls `input_stream="rollout"`, contradicted by `policy_decomposition.py:532/546/581`;
and the same file's header still calls MECH-288 "candidate v3_pending" though it is `provisional`
with `v3_pending: false` since 2026-07-14.

**GOVERNANCE FLAG 2:** `evidence_discrepancy` -- **the shipped fast-scale trigger is not the
trigger the claim commits to, on the observation path.** MECH-288's Verdict 1 makes "PE-spike the
primary trigger (Zacks 2007 EST canonical)" and the title names a "PE-threshold detector on the
fast scale (z_world+z_self)". `ree_core/agent.py:5448` calls
`event_segmenter.step(latent_dict=..., pe_dict=None, t=...)`, and `event_segmenter.py:139-142`
documents that with no `pe_dict` the aggregator falls back to
`sum_s ||z_s(t) - z_s(t-1)||` -- a latent-delta magnitude. So every one of the 23 indexed runs
that enabled the segmenter exercised, on the observation stream, a **latent-change** detector,
not the PE detector. (The rollout stream is unaffected: `policy_decomposition.py:581` passes
`pe=pe_signature`.) Governance should decide whether to (i) wire the observation-side `pe_dict`
and re-baseline, or (ii) amend the claim to state that the observation-side fast scale is a
latent-change detector by design with PE reserved for the rollout stream. Either way the
divergence should be on the claim before any run is read as testing the PE commitment.

**GOVERNANCE FLAG 3:** `promotion_review` -- **evidence attribution gap.** MECH-288 sits at
`experimental_confidence 0.66` from `genuine_exp_count: 1` (V3-EXQ-757, an action-free synthetic
isolation test) while its substrate ran live inside 22 further indexed experiments, none of which
names MECH-288 in `claim_ids`. Two questions for governance: (i) should any of those 22 (e.g.
V3-EXQ-904 PASS/supports, or V3-EXQ-938's `boundary_fires_mean_*` instrumentation over 40 seeds)
be credited as bearing on MECH-288 retrospectively via `bears_on`; and (ii) note the index-vs-
registry mismatch -- `docs/assets/data/claims.json` reports MECH-288 as
`assembly_state: "mature"`, `epistemic_stance: "shown"` off `overall_confidence 0.81`, while the
registry status is `provisional` with an explicitly open promote-to-active gate. This is a
derived-vs-registry reading gap of exactly the shape that has caused mis-promotions before, and
it is worth an explicit adjudication rather than leaving the two artifacts disagreeing.

---

### SD-084 -- e3.persistent_committed_program_handle: a committed-program handle that survives per-tick teardown

**Recommended disposition:** **(a) testable now** -- with the important qualification that the
question SD-084 was registered to answer (is the MECH-321 R4 mid-execution hook *reachable* under
the standard driver loop?) has **already been answered affirmatively and cleanly** by V3-EXQ-839,
so the falsifier below is written as the claim's **standing regression + residual** condition: the
untested half is the **liveness INVARIANT** the claim's own title asserts, which no run has ever
measured. Digestion is not promotion, so I recommend no status change here; the appropriate
status move (and the `evidence: []` attribution problem) is raised as a flag for `/governance`.

**Extracted from:** the claim's own `implementation_note` -- the V3-EXQ-839 acceptance criterion
taken verbatim from `failure_autopsy_V3-EXQ-830_2026-07-29.md`
(`decomp_n_evaluated_midexec > 0` on a standard `select_action -> update_residue` loop with no
hand-injected preconditions), the two pre-registered seed tiers (ATTRIBUTABLE 3/47/71/89;
NEGATIVE CONTROL 23/53), and the title's own liveness assertion ("Liveness is an INVARIANT
(reaped whenever the beta gate is not elevated), not a list of clear sites: agent.py has ten
`beta_gate.release()` sites and only five clear `_committed_trajectory`"). The residual falsifier
is that last sentence turned into a measurement. Sibling cross-reference: MECH-321's existing
`what_would_answer` owns the *behavioural* question ("does aborting a stale committed macro
improve task performance") -- SD-084's draft deliberately does not re-derive it.

**Currency check:** (a) Substrate present and matches the note exactly: declaration
`e3_selector.py:543`, set at commit entry `e3_selector.py:4122`, flag
`use_persistent_committed_program_handle: bool = False` at `config.py:5380`, consumer union at
`agent.py:6799-6811` (F-driven handle checked first, so the OFF path is byte-for-byte the legacy
`_mid_traj = self.e3._committed_trajectory`). (b) **The liveness invariant is enforced
structurally**, unconditionally, at `agent.py:6771-6772` -- `if not self.beta_gate.is_elevated:
self.e3._persistent_committed_trajectory = None` -- placed immediately upstream of its only
consumer, with a 25-line comment explaining why an invariant beats a list of clear sites. Counted
this pass: **10 real `self.beta_gate.release()` call sites** in `agent.py` (6604, 6669, 6731,
6897, 6993, 7025, 7040, 7069, 7114, 9853 -- the grep also returns 2 comment lines) against **7**
explicit `_persistent_committed_trajectory = None` clears (3650, 6680, 6737, 6772, 6907, 6999,
10673), so 4-5 release sites are covered by the invariant alone, exactly as the note describes.
(c) V3-EXQ-839 landed and PASSED: `total_midexec_on 415`, `total_midexec_off 0`,
`n_on_cells_attributable_with_midexec 4/4` (matching pre-registration exactly),
`negative_control_expectation_held true`, `non_degenerate true`,
`mean_action_divergence_frac_attributable_tier 0.159`. In `reviewed_run_ids`. (d) Contract
`tests/contracts/test_mech321_midexec_natural_reachability.py` present in `ree-v3`. (e)
`claim_evidence.v1.json` -> SD-084 is `null` and the registry block carries `evidence: []` --
correct by construction (`claim_ids: []` on the diagnostic, by design) but it leaves a validated
claim reading as evidence-free. (f) **The routing note is stale** -- see the flag below.

**epistemic_category (proposed):** `standard`. Explicitly **not** `substrate_ceiling`: the
2026-08-10 governance note already recorded "Recommended epistemic_category: standard (not
substrate_ceiling -- nothing ceilinged)", and the V3-EXQ-830 diagnosis was
`competence_implementation_gap` -- the mechanism was never reachable, not tested and found
wanting. That distinction is the group's template finding (preamble (iv)) and should be preserved
on the claim.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION (three conjuncts; conjuncts 1-2 are DISCHARGED and are retained
> as the standing regression gate, conjunct 3 is what the residual test below adds).**
> (1) *Multi-action programs are committed at all.* At least one cell of EACH arm commits a
> multi-action ARC-071 chunk (`len(remaining) > 1`, gate (6) of the mid-execution conjunction).
> A seed that commits none is `substrate_not_ready_requeue`, never a substrate verdict -- this is
> exactly what the V3-EXQ-839 NEGATIVE CONTROL tier (seeds 23, 53) exists to demonstrate rather
> than assert. STATUS: met (839: `total_multi_action_commits 793`; 844 carried the identical
> precondition, measured 139 on the worst OFF cell against threshold 0).
> (2) *Pre-commit decomposition is live.* `decomp_n_evaluated_precommit > 0` -- a zero means the
> decomposition machinery is not running at all, a config error rather than a finding. STATUS:
> met (844: 1724 on the worst OFF cell; V3-EXQ-830: 1862-2618).
> (3) *Commit identity is instrumented (NEW -- the residual test needs this and no run has it).*
> Every consumed handle must be recorded together with a commit-epoch/identity token
> (`chunk_sequence` + the commit tick that installed it) and the beta-elevation epoch current at
> consumption time, so a consumed handle can be checked against the commit it claims to point at.
> Without this field the staleness DV below is unmeasurable and the run says nothing.
>
> **CONFIRMING (two legs).**
> *Leg A -- REACHABILITY (discharged; retained as regression).* With the flag ON, the
> mid-execution hook fires under a standard `select_action -> update_residue` loop with nothing
> hand-injected: `decomp_n_evaluated_midexec > 0` on the attributable tier, and `== 0` in the OFF
> arm with the arms otherwise bit-identical on the negative-control tier. CONFIRMED 2026-07-29 by
> V3-EXQ-839 (415 vs 0; 4/4 attributable seeds; 23/53 bit-identical as pre-registered) and pinned
> by `tests/contracts/test_mech321_midexec_natural_reachability.py`. Any future run showing the
> ON-arm midexec count returning to 0 refutes the claim's central assertion and means the
> teardown has been reinstated somewhere.
> *Leg B -- LIVENESS INVARIANT (the residual, never measured).* The claim's title asserts that
> liveness is an invariant, not a list of clear sites, because `agent.py` has ten
> `beta_gate.release()` sites and only some clear the handle; the invariant is the single
> unconditional reap at `agent.py:6771-6772`. CONFIRMED requires: across a run with the flag ON
> and >= 6 seeds, **zero** hook fires consume a handle whose commit-identity token differs from
> the commit currently holding beta elevated -- i.e. `n_stale_handle_consumptions == 0` with a
> non-zero denominator (>= 100 total fires, so the zero is not vacuous). The load-bearing
> adversarial condition is a beta elevation arising from a path OTHER than the commit that
> installed the handle (MECH-091 safety release/re-elevation, the rung-6 duration release, the
> SD-034 closure de-commit, and the E3-tick non-commit release are the named candidates); the
> run must demonstrate at least one such elevation occurred, or the zero is untested rather than
> earned.
>
> **FALSIFYING.**
> (a) *Leg A:* the ON-arm midexec count is 0 while preconditions (1)-(2) are green -- the handle
> is not surviving the teardown and the claim is simply false. (b) *Leg B (the live risk):* any
> non-zero `n_stale_handle_consumptions` -- the hook fires against a program whose commit has
> been released, which the note itself names as the failure the invariant exists to prevent
> ("gate (2) below would then re-open on a LATER, unrelated commit with the dead program still
> installed"). Because a mid-execution fire RELEASES THE COMMIT LATCH and aborts the remaining
> macro (the claim's own NOT-A-PURE-DIAGNOSTIC warning), a stale consumption is not a cosmetic
> defect: it aborts a *live, unrelated* committed program. (c) *Vacuity check that would void
> the whole reading:* the adversarial elevation of Leg B never occurs in the run, so the zero is
> a zero-denominator artifact -- report as `substrate_not_ready_requeue`, not as CONFIRMED.
> **Out of scope, deliberately:** whether the now-reachable hook IMPROVES task outcome. That is
> MECH-321's question -- see MECH-321's own `what_would_answer`, do not re-derive it here -- and
> it has already been answered negatively once (V3-EXQ-844 FAIL/weakens,
> `midexec_decomposition_does_not_reduce_harm`). A behavioural null on MECH-321 does **not**
> falsify SD-084; SD-084 asserts reachability and liveness, not benefit, and conflating the two
> is precisely the `competence_implementation_gap` / `substrate_ceiling` confusion this claim was
> registered to resolve.

**Proposal sketch (only for a/d):**
- **Title:** `V3-EXQ-<next> -- SD-084 handle-liveness invariant: no stale committed-program handle
  is ever consumed by the MECH-321 R4 hook` (DIAGNOSTIC; `claim_ids: ["SD-084"]` -- **not** `[]`
  this time, see flag below).
- **related_claims:** `SD-084` (primary), bears_on `MECH-321`, `ARC-071`, `MECH-090`, `MECH-091`.
- **acceptance_checks:**
  1. Preconditions (1)-(3) above, with (3) implemented as a new manifest field pairing each hook
     fire with `(commit_tick, chunk_sequence_hash, beta_elevation_epoch)`.
  2. **C1:** `n_stale_handle_consumptions == 0` over >= 6 seeds with `n_total_midexec_fires >=
     100` (839's 415 shows this volume is attainable).
  3. **C2 (adversarial coverage, the anti-vacuity gate):** >= 1 beta elevation per seed arising
     from a non-commit path -- otherwise the run self-routes `substrate_not_ready_requeue`.
  4. **C3 (regression):** Leg A re-asserted -- ON midexec > 0 on the attributable tier, OFF == 0,
     negative-control tier bit-identical between arms. Reuse V3-EXQ-839's seed tiers verbatim
     (3/47/71/89 attributable; 23/53 negative control) so the comparison is like-for-like; seed
     47 is the documented cleanest cell (OFF/ON identical on multi-action commits 30, total
     commits 72, precommit 343).
  5. Behavioural delta recorded as **non-gating payload only** (839's precedent), since a
     mid-execution fire changes committed action sequences by design.

**depends_on additions (if any):** none. `MECH-321 / ARC-070 / ARC-071 / MECH-288` are all
correct: MECH-288 is genuinely upstream here (the hook's trigger is
`event_segmenter.boundary_on(stream="rollout", ...)` via `policy_decomposition.py:581`), which
also confirms the group's 4.32 edge is a real substrate dependency, not just topic adjacency.
*Asked explicitly by the brief:* **ARC-113 does NOT depend on SD-084** -- ARC-113's `depends_on`
is `[ARC-062, ARC-063, MECH-338, MECH-316, ARC-069, ARC-070, ARC-071]`. The relationship is
indirect (SD-084 -> MECH-321 -> ARC-070/ARC-071 -> ARC-113), and SD-084 does bear on ARC-113's
"counterfactual simulation -> behavioural interaction -> outcome comparison" stage boundary by
making mid-execution re-evaluation of a committed program reachable at all. No `depends_on` edit
recommended; ARC-113 is being digested elsewhere and this is offered only as context for that
agent's use.

**GOVERNANCE FLAG 1:** `stale_note` -- **SD-084's 2026-08-10 routing block directs work that had
already been done nine days earlier, and cites a chip_ref that does not exist.** The block reads:
"Routing: queue a successor MECH-321 R4 EVIDENCE experiment (new EXQ, claim_ids=[MECH-321])
testing the behavioural/task effect of the now-reachable hook ... Chipped
`chip-20260810-mech321-r4-behavioural-effect`." That experiment is
`v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3` -- `claim_ids: ["MECH-321"]`,
`outcome FAIL`, `evidence_direction weakens`, `non_degenerate true`, interpretation label
`midexec_decomposition_does_not_reduce_harm` (`harm_delta_mean_post_divergence -0.00326`,
`rel_improvement -0.0696`, `effect_size_ok false`, `rel_floor_ok false`) -- which ran
**2026-08-01**, is in `reviewed_run_ids`, and used this claim's own `behavioural_delta` block as
its design template exactly as the routing asked. Grep of `TASK_CHIPS.json` finds **no**
`chip-20260810-mech321-r4-behavioural-effect`; the actual chip is
`chip-20260731-mech321-r4-successor`, `status done`, resolved `2026-07-31T19:23:09Z`. Two
corrections needed: (i) append to SD-084's `implementation_note` that the routed successor RAN and
returned FAIL/weakens for MECH-321 (with the run_id), so no future session re-queues it; (ii) drop
or correct the non-existent chip_ref. Note the FAIL is for **MECH-321**, not SD-084 -- SD-084's
own reachability claim is untouched by it, and MECH-321's `what_would_answer` already absorbs
844 correctly. This is a records defect, not an evidence defect.

**GOVERNANCE FLAG 2:** `promotion_review` -- **a validated design decision reads as evidence-free.**
SD-084 is `status: candidate_substrate_landed`, `evidence: []`, and `claim_evidence.v1.json`
returns `null` for it, while its validating diagnostic V3-EXQ-839 PASSed cleanly (415 vs 0,
attributability 4/4 as pre-registered, negative control held, non_degenerate), was CONFIRMED by
`failure_autopsy_V3-EXQ-839_2026-07-30`, was ratified by governance on 2026-08-10, and is in
`reviewed_run_ids`. The zero-evidence reading is an artifact of the (correct, deliberate)
`claim_ids: []` on a diagnostic. Governance should decide whether to (i) add V3-EXQ-839 to
SD-084's `evidence` / `bears_on` so the registry reflects the validation without weighting a
diagnostic as claim evidence, and/or (ii) advance the status now that the substrate is landed AND
its acceptance criterion is measured. I make no promotion recommendation -- digestion is not
promotion -- but leaving a validated claim indistinguishable from an unvalidated one is the exact
condition that produced the SD-084 defect in the first place (a mechanism that had never executed
and looked, from the registry, as though it had).

---

<!-- G1 appended 2026-09-04T21:18:57Z -->
## G1 -- sleep-phase (SD-017) hub cluster  (agent report)

### Group preamble

**Why these are together (restate, then my own view).** The assignment grouped these on
`depends_on` edges into SD-017 (SD-083 6.25, MECH-354 6.00, MECH-181 5.04) plus a
same-namespace/same-batch edge MECH-353 <-> MECH-354 (5.00). Restated: SD-017 is the offline-phase
hub and the other four are, on paper, its consumers.

**My own view: the structural edges are real but two of them are DEAD or MIS-LABELLED, and the
group's actual common property is something else entirely.** The live shape is:

- **SD-083's SD-017 edge is a PROSPECTIVE PORT edge, and the port is now unreachable.** SD-083 lives
  in the `mech457` retention TESTBED (`experiments/_lib/mech457_offline_consolidation.py`), *not* in
  `ree_core/sleep/`; the sleep plan records this deliberately ("What landed (NOT in this plan's
  substrate)", `sleep_substrate_plan.md` 2026-07-29 entry). The cognifold port into the SD-017 sleep
  loop is gated on "836b and/or 836c score SUPPORTED". Both scored `weakens`, both redesigns
  (836d/836e) scored `weakens`, and the consumer claim MECH-476 is now **`status: retired`**. The
  trigger can never fire.
- **MECH-354's SD-017 edge is genuinely live and is ALREADY PARTIALLY BUILT outside this group** --
  as `SD-SLEEP-ENTRY-PRESSURE` (`EntryPressureAccumulator` in `ree_core/sleep/mel_consumer.py`,
  ree-v3 `63e70d622c`, 2026-08-26): a Borbely Process-S running SUM with an offline `discharge()` on
  every completed sleep cycle. That is MECH-354's SLOW variant, with the wrong integrand.
- **MECH-181's SD-017 edge is live and its substrate is now complete on BOTH sides** (SD-MEL-PRODUCER
  validated 2026-07-30; SD-MEL-CONSUMER capability proven 2026-07-08).
- **MECH-353 has essentially no SD-017 content** and sits in the group only via the MECH-354 batch
  edge. That is fine -- it earns its place a different way (see (iii)/(iv)).

**The property this group actually shares: every one of them has failed, or is at risk of failing, at
the INSTRUMENT rather than at the mechanism.** 642a/642b (peak against a hard clamp), the whole
436b..436g lineage (whole-bank cosine, occupancy, write content), 969-972 (a 2-cluster Jaccard whose
attainable p-floor exceeds its own alpha), 836b (a fixed margin not scaled to per-arm noise). SD-083
is the sole exception, and it is the only one whose instrument telemetry is clean end to end. That is
why every draft below leads with a precondition about the DV's **resolvable range**, not merely about
the knob being on.

**(i) Same-claim / merge candidates.**
- **MECH-353 vs MECH-354: NOT the same claim, no merge.** Different antecedent (external constraint
  with capacity RETAINED vs. cost accumulated from one's own successful effort), opposite pole
  (assert/escalate vs. stop/disengage), different family (SD-029 comparator vs. SD-012 homeostatic).
  They share only the MECH-342 release ACTUATOR, which both claims already say explicitly. Keep
  separate.
- **MECH-354 -- PARTIAL-ABSORPTION candidate at an already-BUILT mechanism OUTSIDE the group**
  (brief rule 4g's second case). `SD-SLEEP-ENTRY-PRESSURE` already instantiates the *form* MECH-354's
  slow leg asserts: a time-integrating Process-S SUM, single crossing threshold, offline discharge on
  completed sleep, refractory floor on fire rate, default-off (`use_entry_pressure`). What it does
  NOT instantiate is MECH-354's *content*: the integrand is waking **prediction error** (MEL), not
  **effort**; there is one bound, not two; and there is no in-task STOP emission. **Expect PARTIAL
  absorption with a narrowed residual**, not supersession -- see the merge block under MECH-354.
- **SD-083 vs SD-017: no merge**, and the separation is load-bearing (different substrate, different
  optimisee -- SD-083 consolidates the testbed actor-critic `RepAgent` policy, the `ree_core/sleep/`
  cluster acts on E1/E2/E3 latents only, verified in the plan 2026-07-29).
- **MECH-181 vs SD-017 / MECH-180: no merge.** MECH-181 is a lifespan-scale consumer, not a
  granularity variant. But MECH-181 IS internally FUSED (out-of-domain epidemiology leg + testable
  REE leg) and should be SPLIT -- see its section.

**(ii) Contradictions / undercut premises.**
- **SD-083's premise is undercut at the root.** Its title and `implementation_note` define it as the
  instrument that "Unblocks MECH-476's two blocked_substrate falsifier arms". MECH-476 is
  `status: retired`, `superseded_by: [MECH-459, MECH-460]`, with `live_status.evidence.verdict`
  (2026-08-01): "WITHDRAWN per the claim's own pre-registered falsifier ... all three arms
  (dose/836a, novelty-tagging/836d, interval/836e) independently confirm retention invariant to the
  manipulated variable". SD-083 therefore currently `depends_on` a retired claim, and its own stated
  onward purpose is discharged. This does not falsify SD-083 -- the instrument did what it asserted --
  but it means SD-083's disposition must be argued on instrument validity, not on service to MECH-476.
- **SD-017's own live finding constrains MECH-181's test design.** SD-017's 2026-08-30 entry shows
  the ONLINE write path alone collapses the ContextMemory bank from mean pairwise slot cosine 0.000
  (NO_WRITES) to 0.9992 (written). So MECH-181's REE leg must NOT be posed on any ContextMemory
  differentiation DV -- it would inherit SD-017's own ceiling. It must ride the MEL -> sleep-cadence
  DV (`sws_n_writes` / `rem_n_rollouts`), which is instrument-clean and un-pinned since GAP-5b.
- **MECH-353 and MECH-354 predict OPPOSITE behaviour on a shared observable.** Repeated failure to
  achieve an intended outcome over a long window: MECH-353 predicts assert/escalate (with
  ARC-016-gated DECOMMIT only after the window), MECH-354 predicts stop-and-recover. Not a
  contradiction between the claims (the antecedents differ), but a mutual confound in any single
  experiment -- see (iv).

**(iii) Shared falsification condition -- there are TWO, and both are worth cross-referencing rather
than re-deriving.**

1. **HEADROOM ON A BOUNDED ACCUMULATOR.** The canonical statement is `failure_autopsy_V3-EXQ-642a_2026-08-30`'s
   `learning_extracted[1]`, quoted verbatim in the 642b autopsy: *"A criterion built on a PEAK of a
   hard-clamped integrator is degenerate whenever the integrator can reach its clamp ... Prefer a DV
   with headroom (mean, time-to-threshold, area under the accumulation curve) or record the
   saturation fraction alongside the peak."* This binds **MECH-353** (`z_block_cap` 1.5), **MECH-354**
   (two bounds, by construction), **MECH-181** (`mel_duration_factor` clamped to [0.5, 3.0]) and
   **SD-083** (`capture_max`, saturated at 0.989 by N=900). MECH-354's and MECH-181's drafts point at
   MECH-353's precondition (1) rather than restating it.
2. **OFFLINE-PHASE LIVENESS + PRODUCER-SUPRA-NOISE.** Shared by **SD-017** and **MECH-181**: the
   offline pass must fire (non-zero `sws_n_writes` / `rem_n_rollouts` in the ON arm, exactly 0 in the
   OFF arm -- the 436c/436d counters), AND the waking signal driving it must be measurably
   above-reference (V3-EXQ-718a's ecological MEL ~1e-5, noise-level and scrambled vs the novelty
   label, is the vacuity signature). SD-017's entire seven-run 436 lineage is a history of exactly
   these preconditions failing.

**(iv) Cross-cutting findings.**
1. **Mutual confound, asymmetric in time.** Today MECH-353 is UNCONFOUNDED by fatigue *by
   construction* -- no fatigue accumulator exists, so nothing competes for the disengage observable.
   The reverse will not hold: once MECH-354's accumulator is built, its stop/disengage DV is
   confounded by MECH-353's ARC-016-gated DECOMMIT, which fires on the same observable from the
   opposite antecedent. **Standing constraint recorded in MECH-354's draft precondition (2):** any
   MECH-354 run must set `use_blocked_agency=False` or pin `z_block`. A null on MECH-354 measured
   with z_block live would be uninterpretable.
2. **The whole group's blocker is migrating UPSTREAM in one direction, toward the
   observation -> z_world -> E1/E2 interface.** SD-017's ceiling moved write-ADDRESSING (436f) ->
   write-CONTENT (436g, 2026-08-30) -> INPUT DISTRIBUTION (V3-EXQ-972, 2026-09-02: train-time
   write-stream latents at separability 0.0281). Independently, SD-MEL-PRODUCER's fix was also an
   upstream one -- the world had to invalidate LEARNED STRUCTURE (action-map re-permutation) rather
   than add noise, because `E2.world_forward(z_world, a)` is what has to become wrong. Two
   independent threads in this group converge on the same interface.
3. **"Knob live" is not "knob efficacious", and SD-083 is the clean demonstration.** In V3-EXQ-836e
   the offline penalty was installed on 10/10 seeds in every ON arm and its coefficient varied 14x
   (0 -> 52.8 -> 86.5 -> 98.9), yet `retained_fraction` was flat (0.712 / 0.707 / 0.860 / 0.723); in
   836d the WEAKER-penalty arm retained MORE (0.950 unpaired vs 0.834 paired). **Every draft in this
   group therefore needs a POTENCY precondition, not just a liveness precondition** -- a
   demonstration that the mechanism's magnitude reaches the DV -- otherwise a null is uninterpretable.
   This is the single most reusable finding of the pass.

**Currency findings (each verified against the named file/run this session).**

| # | Finding | Source checked |
|---|---|---|
| C1 | **SD-083 `implementation_note` "NOT YET VALIDATED by experiment: V3-EXQ-836b (INTERVAL) and V3-EXQ-836c (NOVELTY) exercise it" is STALE.** All four ran: 836b + 836c 2026-07-29, redesigns 836d + 836e 2026-08-01. All `non_degenerate: true`. All four manifests name `"substrate": "SD-083 offline policy-consolidation window (ree-v3 42ab95f688)"`. | `evidence/experiments/v3_exq_836{b,c,d,e}_*.json` |
| C2 | **SD-083's consumer claim MECH-476 is RETIRED** (2026-08-01, `superseded_by: [MECH-459, MECH-460]`). SD-083 `depends_on` a retired claim, and its cognifold-port trigger ("836b/836c SUPPORTED", `sleep_substrate_plan.md` 2026-07-29) is unreachable. | `claims.yaml` MECH-476; `sleep_substrate_plan.md` |
| C3 | **SD-083 has `evidence: []` and NO entry in `claim_evidence.v1.json`**, despite four non-degenerate runs whose declared substrate IS SD-083. The runs carry `claim_ids: ["MECH-476"]` only. | `claims.yaml`; `evidence/experiments/claim_evidence.v1.json` |
| C4 | **MECH-353 `evidence_quality_note` "NO experimental evidence yet" is STALE in one direction.** Three runs have landed (642 2026-06-06, 642a 2026-08-29, 642b 2026-08-31). `v3_pending: true` remains CORRECT, but the reason has changed from "no run" to "the criterion is arithmetically dead". | `evidence/experiments/v3_exq_642*.json` |
| C5 | **MECH-353 `implementation_note` ends at "V3-EXQ-642b queued 2026-08-31 ... v3_pending remains TRUE until [it] passes".** 642b RAN and FAILED; governance ratified `non_contributory` on 2026-09-01 from confirmed `failure_autopsy_V3-EXQ-642b_2026-09-01` (REE_assembly `5ff838702b`). The note has no landing entry for it. | 642b manifest `evidence_direction_note`; autopsy .md |
| C6 | **DECISIVE, and not the falsifier question: on 642b's OWN recorded data, with the SAME pre-registered margins, swapping `z_block_peak` -> `z_block_mean` gives C1 and C2 PASS on 3/3 seeds** (separations 0.681 / 0.590 / 0.771 vs a 0.20 margin; BLOCK means 0.767-0.835 vs a 0.20 floor). No new run is needed to know the answer; a **claim-carrying** run is needed to bank it -- all of 642/642a/642b carry `claim_ids: []`. | `failure_autopsy_V3-EXQ-642b_2026-09-01.md` sections 1-2 |
| C7 | **MECH-181's mechanism now has VALIDATED substrate on BOTH sides.** `SD-MEL-CONSUMER` status `implemented`, capability PROVEN 2026-07-08 (718a injection positive control: graded MEL -> exact-monotone offline duration, DV [9,13,18,24,30,38] tracking injected [0.6..2.5], all seeds). `SD-MEL-PRODUCER` status `implemented`, **`ready: true`, `validated_utc: 2026-07-30`** (V3-EXQ-798a PASS, `producer_validated_graded_learnable`). The 2026-07-08 "producer parked" reading was UN-PARKED by the user 2026-07-21. | `substrate_queue.json` both entries |
| C8 | **SD-017 `evidence_quality_note` ends 2026-08-30 with "Routed instead to the already-frozen hypothesis_space portfolio `contextmemory_write_content_discrimination` (H1-H4, none yet queued)" -- STALE.** H1-H4 were queued and RAN as V3-EXQ-969/970/971/972, returning 2026-09-02; `failure_autopsy_contextmemory-write-content-cluster_2026-09-03.md` confirmed 2026-09-03. Verdict: none of the four adjudicated its leg (instrument resolution floor); H4 is the load-bearing measurement. | that autopsy |
| C9 | **The blocking substrate entry has moved on from SD-017's own scoping.** `contextmemory-write-path-addressing-degeneracy` is still `implemented_pending_validation` but now carries a NON-EMPTY `depends_on_unresolved` naming **SD-070 (raise z_world entropy)**, added 2026-09-03. SD-017's `pending_retest_after_substrate` scoping ("after-WRITE-PATH-CONTENT") is one level behind. | `substrate_queue.json` |
| C10 | **MECH-354: no substrate exists, and no substrate_queue entry either.** `grep -ri fatigue ree-v3/ree_core/` returns only (a) `CausalGridWorldV2`'s AR(1) observation-noise nuisance term (`fatigue_enabled/_ar_coeff/_noise_scale/_contribution_weight` -- an SD-048 interoceptive-noise source) and (b) `PCCConfig.fatigue_weight`, which SUBTRACTS SD-012 `drive_level` from a stability estimate. Neither accumulates with effort, neither has bounds, neither emits STOP. **`ARC-078` has ZERO occurrences in `ree_core/`.** | `ree-v3/ree_core/`; `substrate_queue.json` |
| C11 | **MECH-354's SLOW (Process-S) leg is PARTIALLY BUILT outside the group.** `SD-SLEEP-ENTRY-PRESSURE` (`EntryPressureAccumulator`, `ree_core/sleep/mel_consumer.py`, ree-v3 `63e70d622c`, 2026-08-26, default-off `use_entry_pressure`): a running SUM over per-step waking demand, `discharge()` on every completed sleep cycle, plus a `steps_since_sleep` refractory floor. Its own docstring names Borbely Process-S -- the same anchor MECH-354 cites. **Integrand is prediction error, not effort; one bound, not two; no in-task STOP.** | `ree-v3/ree_core/sleep/mel_consumer.py`; `sleep_substrate_plan.md` GAP-9 follow-up row |
| C12 | **SD-017 received a literature entry TODAY** (`2026-09-04_sd_017_computational_role_sleep_reorganization_yoshida2023`, `latest_timestamp_utc 2026-09-04T14:36:16Z`). Standing: exp=3 genuine (2 supports / 1 weakens), lit=19, exp_conf 0.652, lit_conf 0.908, quadrant `confirmed_established`. Worth knowing before any confidence read. | `claim_evidence.v1.json` |
| C13 | **MECH-353's own falsifier demands an ablation arm that has NEVER been run.** Its `functional_restatement` says the claim is falsified "if blocked-action behaviour is fully explained by existing harm + suffering + decommit machinery". 642, 642a and 642b all compare BLOCK vs CONTROL *with* `use_blocked_agency: true` (run-level `enabled_default_off_flags`). There has been no `use_blocked_agency=False` necessity arm. | 642b manifest `enabled_default_off_flags`; MECH-353 `functional_restatement` |

---

### SD-017 -- REE-v3 requires a minimal sleep-phase infrastructure: an SWS-analog phase (bidire...

**Recommended disposition:** (c) substrate-blocked, **`substrate_ceiling` -- UNCHANGED and correct**
(built, exercised seven times, readiness gates now clean, and the signal is absorbed by a downstream
shared mechanism), but the BLOCKING SUBSTRATE has moved and the claim's `pending_retest_after_substrate`
scoping should be re-scoped a fifth time, from "after-WRITE-PATH-CONTENT" to "after the write-content
INSTRUMENT redesign AND an input-separability probe".

**Extracted from:** the claim's own `notes` ("context representations remain undifferentiated
(cosine_sim -> 1.0)") plus the 2026-08-30 governance entry in `evidence_quality_note` (WAKING_ONLY
0.9993; NO_WRITES 0.000 vs 0.9992 once written) and the 436d-methodology-check's Recommendation #4,
whose six DV repairs 436e implemented. Nothing here is invented; this is the lineage's own accumulated
precondition list turned into house structure.

**Currency check:** verified (a) `evidence_quality_note` is current through 2026-08-30 and **stale
from 2026-09-02** -- the H1-H4 portfolio it calls "none yet queued" ran as V3-EXQ-969/970/971/972
(`failure_autopsy_contextmemory-write-content-cluster_2026-09-03.md`, confirmed 2026-09-03); (b) the
blocking substrate entry `contextmemory-write-path-addressing-degeneracy` is still
`implemented_pending_validation` and gained a `depends_on_unresolved` naming SD-070 on 2026-09-03;
(c) a fresh literature entry landed 2026-09-04 (C12). **That cluster autopsy explicitly instructs (its
section 9, item 3): "Do NOT set any `evidence_direction` or `epistemic_category` on SD-017 / ARC-045 /
MECH-166 from these runs -- they are claim-free."** This draft respects that: it changes the
falsifier's PRECONDITIONS, not the claim's evidence stamps.

**epistemic_category (proposed):** `substrate_ceiling` (unchanged).

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (four gates; the first three are met on the current substrate, the
> fourth is the one this claim now fails):
> (a) OFFLINE-PHASE LIVENESS -- pooled `sws_n_writes >= 1` and `rem_n_rollouts >= 1` in the sleep-ON
> arm and exactly 0 in WAKING_ONLY (the 436c/436d counters; 436c measured 800 / 600). A run that
> discards `run_sleep_cycle()`'s metrics dict cannot distinguish "write never fired" from "fired with
> no effect" and is inadmissible (the 436b recording gap).
> (b) WRITE-PATH LIVENESS AND OCCUPANCY -- non-zero waking write-path calls in BOTH arms (436f: 15,078)
> AND `n_occupied_slots >= 2` on `>= 3/5` seeds (436e's `sufficient_occupancy_for_c1` gate). This is
> MET only with `E1Config.contextmemory_write_usage_balancing` ON: 436g measures 16/16 occupancy on
> 5/5 seeds. No driver in `ree-v3/experiments/` sets that flag by default, so a driver written today
> silently runs the legacy argmin path and reproduces the 1-of-16 fixed point.
> (c) METRIC INTEGRITY -- the statistic must be computed over OCCUPIED slots only, with similarity and
> occupancy reported SEPARATELY and NEVER as a product (the whole-bank `slot_cosine_sim` scores a
> 12-well-separated-slot arm WORSE, 0.076, than a single-slot arm, 0.009 -- anti-correlated with what
> this claim predicts); and `context_memory.memory.requires_grad_(False)` so Adam drift cannot
> manufacture spread (the NO_WRITES arm is the run-time-derived null, tolerance 4.0 sigma; 436f
> measured max |z| = 1.67). The derived `sws_slot_diversity` (1 - `slot_cosine_sim`) inherits the same
> confound and is equally inadmissible.
> (d) INPUT-SIDE SEPARABILITY FLOOR -- the write-stream latents ENTERING `ContextMemory.write` must
> carry class structure the bank could differentiate on. Assert this with a HELD-OUT LINEAR PROBE
> (logistic regression, safe-vs-dangerous) on the recorded train-time latents, beating its own
> permuted-label null. V3-EXQ-972 measures the uncentred separability at 0.0281 (intra-class safe
> 0.9804, intra-class dangerous 0.9713, inter-class 0.9478) -- the SD-008 under-differentiation cone,
> measured at TRAINING time for the first time in this lineage -- and the 2026-09-03 cluster autopsy
> states that an uncentred cosine "does not support the stronger 'there is no structure for any
> objective to condition on'". Until this probe clears, any slot-differentiation contrast is measuring
> the input cone, not sleep.
>
> CONFIRMING: with (a)-(d) all met, in a run whose DV can resolve GRADED change (the 2-cluster
> occupied-set Jaccard is disqualified: 72 of 89 cells in the 969-972 portfolio can return only 0.0 or
> 1.0; use a mutual-information statistic over the full contingency table with `PROBE_CLUSTERS >= 4`
> and report the FRESH-cluster generalization readout as load-bearing) -- occupied-slot mean pairwise
> cosine in SWS_THEN_REM is LOWER than in a write-matched WAKING_ONLY arm by at least
> `max(1.5 * SD(per-seed paired delta), 0.05 absolute)`, on `>= 3/5` seeds, sign-consistent across
> seeds, leave-one-out stable, with OCCUPANCY MATCHED between arms so the reduction is content and not
> recruitment. SD-017's own directional prediction is the WAKING_ONLY end -- an undifferentiated bank
> without the offline phases -- and that half is ALREADY CONFIRMED at 0.9993 (V3-EXQ-436g, 2026-08-30).
>
> FALSIFYING: with (a)-(d) all met, a resolving DV, and adequate power (the 2026-08-19 pre-registered
> probe derives n = 38-2485 for a cosine contrast depending on the effect, so either meet that n or use
> a deterministic DV instead), the occupied-slot similarity contrast is null or REVERSED (sleep >=
> waking) on `>= 3/5` seeds and leave-one-out stable. Explicitly NOT falsifying: any of the seven
> 436-lineage results to date (436, 436a, 436b, 436c, 436d, 436e, 436f, 436g) -- every one failed
> upstream of the comparison, at (a), (b), (c) or a bug, which is precisely why `evidence_direction` on
> all of them is `non_contributory`.

**Proposal sketch:** N/A (disposition c). The owed work is a BUILD, not an experiment:
`contextmemory-write-path-addressing-degeneracy`'s own `implementation_hint` item (1) -- replace the
2-cluster Jaccard with a mutual-information statistic over the full contingency table, `PROBE_CLUSTERS
>= 4`, record per-draw contingency tables, size held-out splits as a FRACTION of realised class count
(970's `N_HELDOUT=200` against ~180 realised dangerous states was unreachable in 12/12 cells), and
assert objective convergence as a precondition. The re-derive brake stands at 4 substrate_ceiling hits
for SD-017 and a V3-EXQ-436h is REFUSED.

**depends_on additions (if any):** none to `claims.yaml`. Recommend instead that
`pending_retest_after_substrate` be re-scoped in the note to name BOTH the instrument redesign and the
SD-070 input-separability gate, so the scoping matches the substrate entry's own
`depends_on_unresolved` (C9).

**GOVERNANCE FLAG:** `stale_note` -- SD-017's `evidence_quality_note` closes on 2026-08-30 with
"Routed instead to the already-frozen hypothesis_space portfolio
`contextmemory_write_content_discrimination` (H1-H4, none yet queued)". H1-H4 were queued and returned
2026-09-02 as V3-EXQ-969/970/971/972; `failure_autopsy_contextmemory-write-content-cluster_2026-09-03`
is confirmed. The material update for this claim is that the ceiling has MOVED one level upstream --
from write-CONTENT to the INPUT DISTRIBUTION (H4/V3-EXQ-972, separability 0.0281), with the hedge that
H4's uncentred cosine cannot distinguish "no structure" from "no linearly-separated structure", the
cheap confirmer being a held-out linear probe. Append the landing; **do not** set
`evidence_direction`/`epistemic_category` from those four claim-free runs (that autopsy forbids it
explicitly).

---

### MECH-181 -- Cognitive reserve (produced by education, bilingualism, complex occupation, so...

**Recommended disposition:** **(c2) out_of_domain -- the claim is FUSED, and should be SPLIT**; the
epidemiology + clinical-PSG leg is `out_of_domain` and belongs in its own `research_anchor` /
`literature_synthesis` claim, while the reframed REE leg is **(a) testable now** on substrate that is
validated on both sides as of 2026-07-30.

**Extracted from:** the claim's own `notes` -- its stated mechanism chain ("complex, socially engaging,
novel activities generate substantial daily prediction error ... This drives MECH-180 (adaptive sleep
upregulation), maintaining strong SWS replay and REM simulation capacity") is already, verbatim, the
SD-MEL-PRODUCER -> SD-MEL-CONSUMER pathway that exists in `ree_core/sleep/mel_consumer.py`. The
falsifier below is that chain instrumented, plus MECH-181's own distinctive "reserve" content (matched
insult, differential retention). The out-of-domain leg is the `notes`' "Novel prediction" paragraph.

**Currency check:** verified against `substrate_queue.json` and `ree_core/`:
- `SD-MEL-CONSUMER` status `implemented`; consumer capability PROVEN 2026-07-08 (confirmed
  `failure_autopsy_V3-EXQ-718a_2026-07-08`): the injection positive control shows graded MEL ->
  exact-monotone graded offline duration, DV `[9,13,18,24,30,38]` tracking injected `[0.6..2.5]` on all
  seeds.
- **`SD-MEL-PRODUCER` status `implemented`, `ready: true`, `validated_utc: 2026-07-30`** -- V3-EXQ-798a
  PASS, `producer_validated_graded_learnable` (confirmed `failure_autopsy_V3-EXQ-798a_2026-07-30`). The
  knob is `world_rule_shift_enabled/_interval/_depth/_scope` on `CausalGridWorldV2`
  (`ree_core/environment/causal_grid_world.py` ~line 755+): it periodically re-permutes the
  action -> displacement map so `E2.world_forward(z_world, a)` becomes systematically wrong until
  re-learned. This is the FIX for the exact failure MECH-181's chain previously hit.
- The 2026-07-08 "ecological demonstration re-parked" note is superseded: the user **UN-PARKED** it on
  2026-07-21 (`SD-MEL-PRODUCER.note`). The re-derive brake that fired in 2026-07-08 refused a
  *same-environment* re-grade (no V3-EXQ-718b); the new environment is the sanctioned entry point,
  named in SD-MEL-CONSUMER's own note ("the entry point is a NEW graded-MEL environment/test-bed").
- The ecological end-to-end MECH-180 run that the producer entry says it now enables is described as
  "still-gated, separately-queued" and is **NOT in `ree-v3/experiment_queue.json`** (3 items:
  V3-EXQ-1002, 983a, 993a). It is owed and unqueued.

**epistemic_category (proposed):** `standard` **for the reframed REE leg**. If governance declines the
split and keeps the claim as written (dementia incidence at matched pathological burden; PSG response
to enrichment sessions), then `out_of_domain` is the correct stamp and no REE experiment can move it.
This is a real fork and should be decided explicitly rather than inherited.

**Draft `what_would_answer`** (REE leg; the out-of-domain leg's proof obligation is stated after it):

> NON-DEGENERACY PRECONDITION (five gates):
> (1) PRODUCER SUPRA-REFERENCE -- the graded-enrichment arms must produce a measured waking MEL
> gradient ABOVE the calibrated stable-base reference. The vacuity signature is V3-EXQ-718a's: measured
> ecological MEL ~1e-5, noise-level and SCRAMBLED with respect to the novelty label, with
> `conv_rel_drop ~0.98`. Grade novelty with SD-MEL-PRODUCER's `world_rule_shift_*` knob (action-map
> re-permutation), NEVER with `env_drift_interval` -- V3-EXQ-677 measured a high-vs-low mean-PE
> difference of 8.8e-07 against a 0.01 threshold on that knob, because moving hazards adds sampling
> noise, not learning load.
> (2) THE GRADIENT MUST BE LEARNING LOAD, NOT NOISE -- elevated PE counts only if it DECAYS within a
> stationary window; `steps_since_world_rule_shift` is emitted in env `info` for exactly this. A
> matched-PE OBSERVATION-NOISE negative-control arm must NOT reproduce the effect (grading observation
> noise produces a monotone MEL ladder by construction on any substrate -- the DV-symmetry artifact
> class, and the reason V3-EXQ-798a carried this control).
> (3) CONSUMER LIVE AND UN-PINNED -- `use_mel_consumer=True`, and cumulative `sws_n_writes` /
> `rem_n_rollouts` must VARY across arms. The vacuity signature is V3-EXQ-677's scheduler-pinned
> SWS=80.0/80.0, REM=60.0/60.0 with zero cross-arm variance.
> (4) HEADROOM -- `mel_duration_factor` is clamped to `[mel_duration_factor_min 0.5,
> mel_duration_factor_max 3.0]`. If the top arm saturates at 3.0 the contrast is a cap artefact; report
> the per-arm saturation fraction alongside the factor. This is the same shape as MECH-353's
> precondition (1) -- see MECH-353's own `what_would_answer`, do not re-derive.
> (5) CHANNEL ATTRIBUTION -- an ENRICHED arm with `use_mel_consumer=False` must show the SAME
> offline-phase duration as an IMPOVERISHED arm with the consumer off, so any enrichment effect is
> attributable to the MEL channel rather than to enrichment changing episode length or boundary count
> (note that under the boundary-only trigger, episode count IS sleep count -- `sleep_substrate:GAP-9`).
>
> CONFIRMING (two legs; both are required, and the second is MECH-181's distinctive content over
> MECH-180):
> (i) MAINTENANCE -- across `>= 3` enrichment levels (impoverished / moderate / enriched) at `>= 5`
> seeds, measured above-reference waking MEL is monotone in enrichment level, AND cumulative
> offline-phase work (`sws_n_writes + rem_n_rollouts`) is monotone in MEASURED MEL -- not in the
> novelty LABEL, the distinction on which V3-EXQ-718's C1 failed 0/3 while its C2 passed 3/3 -- on
> `>= 3/5` seeds.
> (ii) RESERVE -- after a MATCHED degradation insult applied identically to both histories (a fixed
> ablation of ContextMemory slots, or fixed noise injected into the E3 attribution path; identical
> magnitude, identical schedule, applied after the enrichment phase), the ENRICHED-history agent
> retains more attribution/competence than the IMPOVERISHED-history agent, by
> `max(1.5 * SD(per-seed paired delta), an absolute floor derived from the consumer-OFF arm's spread)`,
> on `>= 3/5` seeds. This is the only leg that tests "reserve" rather than "responsiveness", and it is
> what makes MECH-181 more than a restatement of MECH-180.
>
> FALSIFYING: with (1)-(5) met, ANY of --
> (i) offline-phase work is flat or non-monotone in MEASURED MEL (the maintenance chain does not close);
> (ii) at matched insult, enriched and impoverished histories show no retention difference (there is no
> reserve, only responsiveness);
> (iii) DECISIVE -- the retention difference SURVIVES with `use_mel_consumer=False`. MECH-181 asserts
> specifically that the protection runs THROUGH the MEL-driven sleep loop; a difference that persists
> with the loop disabled is an environment/exposure effect and refutes the claim's mechanism even
> though it would leave the epidemiology untouched.

**Out-of-domain leg, stated so it is not lost in the split.** Proof obligation: the epidemiological
premise (education, bilingualism, occupational complexity and social engagement reduce clinical
dementia incidence and delay onset at MATCHED pathological burden -- Stern 2009, Lancet Neurology) and
the clinical prediction (enrichment sessions produce measurable PSG change -- increased SWA, increased
spindle density -- on following nights, within weeks and BEFORE any cognitive improvement is
measurable, distinguishing restored learning drive from improved mood). A counterexample is a
controlled enrichment trial in early dementia showing cognitive/mood benefit with NO PSG change on the
same timescale, or PSG change with no dose-relation to enrichment intensity. No REE substrate at any
level bears on either; this resolves by literature and by clinical trial, and per the epistemic-category
table these belong as `research_anchor` / `literature_synthesis` rather than as a mechanism hypothesis.

**Proposal sketch (leg (a) of the split):**
- **title:** "MECH-181/MECH-180 ecological cognitive-reserve chain: graded world-rule-shift novelty ->
  above-reference waking MEL -> graded offline-phase work -> differential retention at matched insult"
- **related_claims:** MECH-181 (primary), MECH-180, INV-050, INV-049, SD-017, MECH-204
- **acceptance_checks:** all five preconditions above emitted as explicit P0 gates (producer
  supra-reference with the decay check; the matched-PE noise negative control; consumer un-pinned;
  saturation fraction reported; consumer-OFF attribution arm); `claim_ids` naming MECH-181 and MECH-180
  with per-claim direction; monotonicity scored against MEASURED MEL not the novelty label;
  `>= 5` seeds; leave-one-out reported in-line.
- **Sequencing note:** leg (i) is runnable TODAY with zero new build (both substrates validated, all
  knobs present). Leg (ii) needs a small insult harness (slot ablation / E3 noise injection), which is
  `complicated (buildable)`, not probe-gated. Do not mint this as a fresh lineage if the
  "still-gated, separately-queued MECH-180 ecological end-to-end run" is scheduled -- MECH-181's leg (i)
  IS that run plus a per-claim tag, and leg (ii) is one extra phase on the same driver.

**depends_on additions (if any):** none in `claims.yaml`. Record `SD-MEL-PRODUCER` and
`SD-MEL-CONSUMER` in an `implementation_note` (they are substrate-queue ids, not claims).

**GOVERNANCE FLAG:** `stale_note` -- the standing "INV-050 / MECH-180 MEL producer is parked / blocked"
reading (SD-MEL-CONSUMER's 2026-07-08 re-park note, and the corresponding session memory) is superseded
twice over: the user un-parked it 2026-07-21, and `SD-MEL-PRODUCER` reached `ready: true` /
`validated_utc: 2026-07-30` on V3-EXQ-798a PASS. MECH-181's REE leg is no longer substrate-blocked, and
the ecological end-to-end run that both substrate entries name as owed is **not in the live queue**.
Secondary: MECH-181 is FUSED (out-of-domain epidemiology + testable REE mechanism) -- recommend a split
decision at governance, since the epistemic_category depends entirely on which leg the claim is taken to
assert.

---

### MECH-353 -- Blocked-agency / control-failure affect stream (z_block): an integrated readou...

**Recommended disposition:** **(a) testable now** -- the substrate is built, calibrated and
demonstrably working; all three failures to date are one measurement defect (a peak statistic against a
hard clamp), and the deciding statistic is ALREADY in the 642b manifest passing 3/3 at the
pre-registered margins.

**Extracted from:** the claim's own `functional_restatement` "Falsifiable:" clause (the assert/persist
signature, the z_harm_a dissociation under matched controllability, and the "fully explained by
existing machinery" necessity condition), sharpened by `failure_autopsy_V3-EXQ-642b_2026-09-01` sections
2-4. This is extraction, not fresh design.

**Currency check:** verified:
- `evidence_quality_note`'s "NO experimental evidence yet" is stale as to RUNS (642 2026-06-06, 642a
  2026-08-29, 642b 2026-08-31) though correct as to BANKED evidence -- all three carry `claim_ids: []`,
  so `claim_evidence.v1.json` has **no MECH-353 entry at all** and `v3_pending: true` correctly stands.
- `implementation_note` ends at "V3-EXQ-642b queued 2026-08-31 ... v3_pending remains TRUE until [it]
  passes"; 642b RAN and FAILED, and governance ratified `non_contributory` 2026-09-01 from confirmed
  `failure_autopsy_V3-EXQ-642b_2026-09-01`. The note has no landing entry.
- **The substrate WORKS.** Against the 642a autopsy's own stated success target, CONTROL-arm
  `z_block_mean` fell from 1.26-1.35 (legacy absolute floor) to **0.064-0.177** of a 1.5 cap, and
  BLOCK-CONTROL mean separation improved **4.1x-9.3x**. Readiness gates all met: `world_forward` C0
  probe margin 0.508-0.624 against a 0.1 floor, `world_encoder` tensors moved 4/4 on every seed.
  C0 PASS 3/3, C3 (assert-not-withdraw) PASS 3/3.
- `substrate_queue` entry `sd_blocked_agency_mismatch_floor_calibration` is
  `implemented_pending_validation`, severity deliberately LEFT at `corrupting` -- because CONTROL
  `z_block_peak` still reaches 1.500 on 3/3 seeds, so any NEW experiment reading a peak-shaped
  blocked-agency DV still gets a zero separation that LOOKS like a valid negative. That is the live
  trap this draft's precondition (1) exists to close.
- The `z_goal_stream.writer_defect` flag on 642b is a **detector false positive** (the driver pins the
  goal directly, `GOAL_PIN=0.5`, bypassing the counted writer) -- do not treat it as a recording gap.

**epistemic_category (proposed):** `standard`. **Explicitly NOT `substrate_ceiling`** -- the claim's own
`live_status.evidence` from the 2026-06-06 autopsy already directs this ("characterise as a measurement
/ test-design gap, NOT substrate_ceiling. Do not record substrate_ceiling on any claim from this run"),
and 642a/642b reconfirm the same shape: readiness gates pass, no downstream mechanism absorbs the
signal, the criterion is arithmetically dead.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (four gates):
> (1) HEADROOM ON THE DECIDING STATISTIC -- the criterion must NOT read `z_block_peak`, nor any max or
> difference-of-maxima against `z_block_cap` (1.5, `ree_core/affect/blocked_agency.py:153`). Both arms
> touched exactly 1.500 on 3/3 seeds in BOTH 642a and 642b, so `z_block_separation` was 0.0 by
> arithmetic regardless of behaviour. Use `z_block_mean` (or time-above-threshold, or area under the
> accumulation curve) and REPORT the per-arm saturation fraction alongside it.
> (1b) DO NOT SUBTRACT A STRUCTURALLY-ZERO TERM -- 642's C2 was
> `(z_block_sep - z_harm_a_sep) >= C2_MARGIN`, and `z_harm_a_sep` is a structural 0.0 because harm is
> held at zero by design in this env, so C2 merely inherited C1's zero with nothing to offset it. State
> the dissociation POSITIVELY: "z_block separates on a headroom statistic AND z_harm_a does not", each
> tested against its own margin.
> (2) DETECTOR READINESS (already met; keep as a gate) -- the SD-029 comparator must be discriminative:
> `world_forward` C0 probe margin `>= 0.1` on the P0a+P0b-trained substrate (642b measured
> 0.508/0.532/0.624), and P0 warmup must have MOVED `split_encoder.world_encoder` tensors (642b: 4/4 on
> every seed), i.e. z_world is a prediction-trained encoder and not a frozen random projection. An
> untrained encoder makes the whole detector vacuous -- that was V3-EXQ-642's original 2026-06-06
> failure.
> (3) CALIBRATION LIVE -- `blocked_agency_outcome_mismatch_floor_mode = "baseline_relative"`, and the
> CONTROL arm's `z_block_mean` must sit well below cap. 642b: 0.064-0.177 of 1.5 (PASS). 642a's legacy
> absolute mode: 1.26-1.35 (the vacuity signature -- z_block accumulating on ordinary world-model error).
> (4) THE RUN MUST CARRY `claim_ids: ["MECH-353"]`. V3-EXQ-642, 642a and 642b are all claimless
> diagnostics, so however they score they bank nothing for or against this claim. This is why
> `claim_evidence.v1.json` has no MECH-353 entry despite three completed runs.
>
> CONFIRMING: in `CausalGridWorldV2` with `scheduled_action_block_*` (external move-cancel, no damage,
> no layout change) and with harm and goal-value held constant, on `>= 3/5` readiness-cleared seeds:
> (i) `z_block_mean(BLOCK) - z_block_mean(CONTROL) >= 0.20` with `z_block_mean(BLOCK) >= 0.20` -- 642b's
> already-recorded values are 0.681 / 0.590 / 0.771 and 0.767-0.835, i.e. 3/3 on the same margins;
> (ii) DISSOCIATION -- `z_harm_a` shows no separation of comparable magnitude under the same
> manipulation, and under a MATCHED controllability manipulation with capacity-belief COLLAPSED the
> response flips to the SD-019b withdraw signature (the hand-off the claim asserts) rather than
> persisting as assert;
> (iii) BEHAVIOUR -- the BLOCK arm shows effort escalation and/or alternative-action search relative to
> CONTROL (the MECH-320 vigor signature; C3 in 642a/642b, already PASS 3/3), with DECOMMIT (MECH-342,
> ARC-016-gated) appearing only after the assertion window rather than in place of it;
> (iv) NECESSITY -- an arm with `use_blocked_agency=False` and everything else identical does NOT
> reproduce the BLOCK-arm behavioural signature.
>
> FALSIFYING: with (1)-(4) met, ANY of --
> (i) `z_block` fails to separate BLOCK from CONTROL on a headroom statistic under a genuine external
> block;
> (ii) it separates but `z_harm_a` separates by a comparable amount under the same manipulation (the
> signal is harm re-labelled, not a distinct stream);
> (iii) DECISIVE, and the leg this lineage has NEVER run: the `use_blocked_agency=False` arm reproduces
> the blocked-action behaviour using only the existing harm (SD-011) + suffering (SD-019b) + decommit
> (MECH-342/ARC-016) machinery. The claim's own falsifier text names exactly this condition, and every
> run to date has compared BLOCK vs CONTROL with `use_blocked_agency: true` at run level -- so the
> necessity question is untested.

**Proposal sketch (a):**
- **title:** "V3-EXQ-642c -- MECH-353 z_block discriminative validation on a HEADROOM statistic, with a
  `use_blocked_agency=OFF` necessity arm"
- **related_claims:** MECH-353 (primary, direction to be scored); bears_on SD-029, MECH-112, MECH-320,
  MECH-342, ARC-016, SD-011, SD-019b, SD-070, SD-056
- **acceptance_checks:**
  1. `claim_ids: ["MECH-353"]` -- NOT a claimless diagnostic (the single most important change from
     642/642a/642b).
  2. C1/C2 recomputed on `z_block_mean` at the UNCHANGED pre-registered margins (`C1_MARGIN 0.20`,
     `Z_BLOCK_MIN 0.20`, `C2_MARGIN 0.20`) -- moving the STATISTIC off a provably dead one is not the
     same as moving a threshold to fit a result, and the 642b autopsy makes exactly this distinction.
  3. Per-arm `z_block` SATURATION FRACTION recorded alongside every statistic.
  4. C2 restated positively (z_block separates AND z_harm_a does not), not as a difference of
     separations.
  5. NEW ARM: `use_blocked_agency=False` necessity ablation, scored on the behavioural DV.
  6. Seeds raised from 3 to 5 (642b's `SEED_PASS_FRACTION` is 0.667; at n=3 that is 2 seeds).
  7. P0 gates retained verbatim from 642a/642b (`world_forward_c0_margin_supra_floor >= 0.1`,
     `zworld_world_encoder_trained`), plus `blocked_agency_outcome_mismatch_floor_mode ==
     "baseline_relative"` asserted in the manifest.
- **Note for the author:** the answer is very likely already known (C6). The purpose of the run is to
  BANK it under a claim id on a criterion that can express it, and to settle (iv)/(iii), which no
  existing data touches.

**depends_on additions (if any):** consider adding **SD-070** and **SD-056** to MECH-353's `depends_on`.
Both are hard preconditions of the detector -- `implementation_note` already says "the action-outcome
comparator is only discriminative once the encoder + action-conditional world_forward (SD-056) are
trained" -- and both appear in every 642-lineage run's `bears_on` while being absent from the claim's
`depends_on`.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- V3-EXQ-642b's own manifest already contains the deciding
statistic and it PASSES: swapping `z_block_peak` -> `z_block_mean` at the SAME pre-registered margins
gives C1 and C2 on 3/3 seeds (separations 0.681 / 0.590 / 0.771 vs a 0.20 margin; BLOCK means
0.767-0.835 vs a 0.20 floor), while the recorded `outcome` is FAIL and `evidence_direction` is
`non_contributory`. This is not a request to re-score 642b -- it is claimless and correctly banks
nothing -- but the gap between "what the substrate demonstrably does" and "what the registry records"
is now 3 runs and ~3 months wide, and a single claim-carrying V3-EXQ-642c on a headroom statistic could
clear MECH-353's `v3_pending`. Secondary: the substrate entry
`sd_blocked_agency_mismatch_floor_calibration` remains `implemented_pending_validation` with severity
`corrupting` precisely because the peak trap is still live for any NEW experiment -- the fix is a
headroom-DV REQUIREMENT on this substrate, not a severity downgrade.

---

### MECH-354 -- Effort/fatigue stop-recover homeostatic accumulator: a two-bound (hysteretic) ...

**Recommended disposition:** **(c) substrate-blocked, `substrate_conditional`** -- the two-bound
hysteretic effort accumulator does not exist anywhere in `ree_core/`, has no `substrate_queue` entry,
and its named consumer ARC-078 has zero occurrences in the substrate, so zero non-degenerate
experimental attempts are currently possible and no evidence has been or could have been banked either
way. (A PARTIAL-absorption merge proposal for the SLOW leg follows, PROPOSE-ONLY.)

**Extracted from:** the claim's own `functional_restatement` "Falsifiable:" clause, which already names
the three legs (a) time-on-task independent of harm/controllability, (b) incentive-reversibility, (c)
rest-recovery. The draft turns those into house structure and adds the preconditions the group's
measurement history makes mandatory.

**Currency check:** verified against `ree-v3/ree_core/` and `substrate_queue.json`:
- **No fatigue accumulator exists.** `grep -ri fatigue ree-v3/ree_core/` returns exactly two families,
  neither of which is MECH-354's: (a) `CausalGridWorldV2`'s `fatigue_enabled / fatigue_ar_coeff 0.995 /
  fatigue_noise_scale / fatigue_contribution_weight` -- an AR(1) *observation-noise* drift term, i.e.
  the SD-048 interoceptive nuisance source, explicitly a stochastic attractor audited by `INF-ENV-004`;
  and (b) `PCCConfig.fatigue_weight 0.5` in `ree_core/cingulate/pcc_analog.py`, which SUBTRACTS SD-012
  `drive_level` from a stability estimate (`stability -= fatigue_weight * drive`). Neither accumulates
  with effort, neither has bounds, neither emits STOP, neither recovers with rest.
- **`ARC-078` has ZERO occurrences in `ree_core/`.** The claim's named cost/benefit consumer is
  unimplemented.
- **No `substrate_queue` entry exists** for MECH-354 or for an effort/fatigue accumulator. So this is
  not even "queued but unbuilt" -- it is unregistered.
- The environment DOES have a decoupled effort axis to build against:
  `effort_harm_coupling_enabled / _scale / _depletion_weight` and the Q-080.b control lever
  `effort_benefit_asymmetry` (`causal_grid_world.py` ~line 755), the latter explicitly documented as
  the positive control proving the effort machinery is non-vacuous.

**epistemic_category (proposed):** `substrate_conditional`. **Blocking substrate (unregistered, name it
when queueing):** a two-bound hysteretic effort/time-on-task accumulator on the SD-012 homeostatic side
(hosted by the SD-048 interoceptive channel), emitting an in-task STOP into MECH-342 as a NEW deficit
input alongside the R-c execution-readiness deficit, with the recover half on SD-012/SD-017 and an
ARC-078 cost/benefit consumer.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION (five gates; gate (0) is currently UNMET and every gate below it is
> conditional on the build):
> (0) EXISTENCE -- an F accumulator with TWO bounds must exist and be reachable from the agent loop.
> It does not today: `ree_core/` contains no effort-driven accumulator, `ARC-078` appears nowhere, and
> the only two things named "fatigue" are an environment observation-noise AR(1) term and a PCC
> stability subtrahend reading SD-012 `drive_level`. Until (0) is satisfied this claim is untestable in
> principle, not merely unqueued.
> (1) TWO-BOUND LIVENESS AND HEADROOM -- BOTH bounds must be reached and neither pinned: each seed must
> show F crossing the UPPER bound at least once AND recovering to the LOWER bound at least once, with
> the fraction of steps spent at each bound reported. An F pinned at either bound reproduces the exact
> V3-EXQ-642a/642b degeneracy -- see MECH-353's own `what_would_answer` precondition (1) for the full
> statement of why a bounded-accumulator DV must have headroom; do not re-derive it here.
> (2) DISCONFOUNDING FROM z_block (MECH-353) -- the run MUST set `use_blocked_agency=False`, or pin
> `z_block` to a constant. MECH-353's ARC-016-gated DECOMMIT fires on the SAME observable
> (disengagement) from the OPPOSITE antecedent (external block with capacity retained). With both live,
> a stop/disengage DV cannot attribute, and a null on MECH-354 would be uninterpretable.
> (3) HARM AND CONTROLLABILITY PINNED -- `z_harm_a` and the SD-019b/Q-036 escapability gate held
> constant across the time-on-task axis. If they drift, the disengage is the suffering pole, which is
> precisely the DEV-NEED-002 conflation this claim exists to cure.
> (4) THE EFFORT AXIS MUST BE REAL AND DECOUPLED FROM HARM -- use `CausalGridWorldV2`'s
> `effort_harm_coupling_enabled=False` setting so effort cost is not a harm proxy, and run the Q-080.b
> `effort_benefit_asymmetry > 0` positive control to prove the effort machinery is non-vacuous before
> reading any negative result.
>
> CONFIRMING (three legs, matching the claim's own (a)/(b)/(c); all three are required, since (a) alone
> is shared with the suffering pole):
> (a) TIME-ON-TASK -- disengagement hazard rises monotonically with time-on-task at FIXED harm and FIXED
> controllability, on `>= 3/5` seeds, effect `>= max(1.5 * SD(per-seed delta), an absolute floor derived
> from the F-OFF arm's spread)`.
> (b) INCENTIVE-REVERSIBILITY -- raising incentive at a FIXED accumulated F measurably delays or cancels
> the STOP. This is the leg that discriminates the Boksem-Tops cost/benefit recalibration account from a
> pure-depletion account, which predicts no incentive effect at fixed F.
> (c) REST-RECOVERY, THE DECISIVE DISSOCIATOR -- after a rest / offline phase, re-engagement latency and
> disengagement hazard return toward baseline, AND a matched suffering/learned-helplessness arm
> (uncontrollable aversion, SD-011/SD-019b) run on the SAME DV shows NO rest-recovery. Without the
> matched comparison arm this leg is not a dissociation, only a description.
>
> FALSIFYING: with the accumulator built and (1)-(4) met, ANY of --
> (i) (a) holds but (b) and (c) do not -- the stop is neither incentive-reversible nor rest-recoverable,
> so on its OWN decisive dissociator the signal is indistinguishable from the SD-011 suffering pole and
> MECH-354's claim to be a separate stream on the SD-012 side is refuted;
> (ii) (c) holds but the matched helplessness arm ALSO recovers with rest -- rest-recovery is then not
> the dissociator the claim rests on;
> (iii) PARSIMONY -- feeding the EXISTING SD-012 `drive_level` (which MECH-342 and the PCC already read)
> directly into MECH-342 as a deficit input reproduces (a), (b) and (c) without any two-bound hysteretic
> accumulator. MECH-354 asserts the "smallest computational form" is Meyniel's two-bound accumulator; if
> a one-bound leaky drive suffices, the claim is over-specified and should be narrowed rather than
> confirmed.

**Proposal sketch (only for a/d):** N/A -- disposition (c). The owed work is an `/implement-substrate`
build with no open question (`complicated (buildable)`), which should be REGISTERED in
`substrate_queue.json` first, since no entry exists today.

**depends_on additions (if any):** add **MECH-353** to MECH-354's `depends_on` -- not as a dependency of
the mechanism but as a recorded CONFOUND edge, since precondition (2) makes MECH-354's testability
conditional on z_block's state. If governance prefers not to overload `depends_on` with confound edges,
record it in `notes` instead, but record it somewhere machine-visible: it is the kind of constraint that
gets rediscovered by a failed run.

**MERGE PROPOSAL (g) -- PROPOSE ONLY, partial absorption with a narrowed residual.**
- **Surviving mechanism (already BUILT, outside the group):** `SD-SLEEP-ENTRY-PRESSURE` --
  `EntryPressureAccumulator` in `ree-v3/ree_core/sleep/mel_consumer.py` (ree-v3 `63e70d622c`,
  2026-08-26, default-off `use_entry_pressure`; `sleep_substrate_plan.md` GAP-9 follow-up row).
- **Partially absorbed:** MECH-354's SLOW "sleep-pressure (Process-S) variant whose recover phase is
  offline (SD-017)". The built mechanism already supplies: a time-integrating running SUM over per-step
  waking demand that grows monotonically with waking steps; a crossing threshold
  (`entry_pressure_threshold`, scaled by `entry_pressure_gain`); an OFFLINE reset (`discharge()` on
  every completed sleep cycle); and a refractory floor bounding fire rate. Its own docstring cites
  Borbely Process-S -- the same anchor MECH-354 cites (Borbely et al. 2016, J Sleep Res).
- **NOT absorbed -- the narrowed residual, which is MECH-354's real remaining content:** (1) the
  INTEGRAND is waking PREDICTION ERROR (MEL), not EFFORT -- so the built accumulator is a
  learning-demand drive, not a cost drive, and MECH-354's distinctive antecedent ("accumulates from your
  own successful effort") is untested; (2) it is ONE-bound, not two -- there is no lower recovery bound
  and no hysteresis, only a discharge-to-zero; (3) it emits SLEEP ENTRY, not an in-task STOP, so nothing
  reaches MECH-342 or ARC-078; (4) the entire FAST within-task variant is absent.
- **Reverse-deps needing repointing if governance accepts any absorption:** none in `claims.yaml` --
  `grep MECH-354` returns no other claim's `depends_on`. MECH-354's OWN `depends_on` (SD-012, SD-048,
  MECH-342, ARC-078, SD-017, SD-011) is unaffected. So the absorption is cheap: it narrows MECH-354's
  text, it does not re-point a graph.
- **Recommended framing:** do NOT retire MECH-354. Narrow its slow leg to the single testable residual
  "**the Process-S entry-pressure accumulator's integrand should be EFFORT, not prediction error**" --
  which is a small, well-posed, buildable comparison on an EXISTING mechanism (swap the integrand behind
  a flag, compare entry timing under a graded effort axis at fixed MEL) -- and keep the FAST two-bound
  in-task accumulator as MECH-354's own unbuilt content. Expect PARTIAL absorption, not supersession.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-354 is registered `candidate` with
`v3_pending: true` and reads as ordinary pending-experiment work, but nothing has been built, nothing is
queued, and it has no `substrate_queue` entry, while a mechanism implementing a substantial part of its
SLOW leg (`SD-SLEEP-ENTRY-PRESSURE`) landed 2026-08-26 with no cross-reference in either direction.
Governance should decide (i) whether to register the fast accumulator as a substrate-queue build, and
(ii) whether to accept the partial absorption above and narrow the slow leg to the integrand question.
Leaving it as-is means a future session re-derives a fatigue accumulator without noticing that a
Process-S accumulator with an offline discharge already exists in `ree_core/sleep/`.

---

### SD-083 -- consolidation.offline_policy_consolidation_window: an OFFLINE, trace-selective ...

**Recommended disposition:** **(a) testable now -- and legs (i)-(iii) are ALREADY ANSWERED CONFIRMING by
banked, non-degenerate telemetry in V3-EXQ-836d and V3-EXQ-836e.** Only leg (iv) (trace selectivity,
per-parameter-group Fisher mass) lacks a readout, and that is a manifest addition or a reanalysis of
recorded state, NOT a new experiment. Governance's real work on this claim is evidence ROUTING and a
`depends_on` repoint, not a run.

**Extracted from:** the claim's own title and `implementation_note`, which state four checkable
properties (interval-accumulated capture `c(N)=capture_max*(1-exp(-N/tau))`; novelty gating; trace
selectivity via Fisher of the policy log-likelihood; and the orthogonality assertion "BUILDS PROTECTION
without retraining, so post_bc is invariant to the interval"). Turned into an instrument-validity
falsifier and checked against the per-arm telemetry actually recorded in 836d/836e.

**Currency check:** verified -- and this claim's registry state is the most stale in the group:
- `implementation_note` says "**NOT YET VALIDATED by experiment**: V3-EXQ-836b (INTERVAL) and
  V3-EXQ-836c (NOVELTY) exercise it". Both ran 2026-07-29; the noise-scaled redesigns 836d (novelty) and
  836e (interval) ran 2026-08-01. All four are `non_degenerate: true`, all four declare
  `"substrate": "SD-083 offline policy-consolidation window (ree-v3 42ab95f688)"`, and 836e's per-arm
  gate is `all_green: true` with zero red or structurally-vacuous arms.
- `status: candidate_substrate_landed`, `live_status.as_of: 2026-07-29`, `evidence: []`, and no entry in
  `claim_evidence.v1.json` -- because all four runs carry `claim_ids: ["MECH-476"]` only.
- **The consumer claim is RETIRED.** MECH-476 is `status: retired`, `superseded_by: [MECH-459,
  MECH-460]`, verdict 2026-08-01 "WITHDRAWN per the claim's own pre-registered falsifier". SD-083 thus
  `depends_on` a retired claim.
- The cognifold PORT into the SD-017 sleep loop that SD-083's `implementation_note` registers as a
  follow-on is gated on "836b and/or 836c score SUPPORTED" (`sleep_substrate_plan.md`, 2026-07-29). All
  four arms scored `weakens`. **That trigger can never fire, and no sleep GAP should be opened for it.**

**epistemic_category (proposed):** `standard`. (Not `substrate_ceiling` -- nothing downstream absorbs
its signal; not `substrate_conditional` -- it is built, exercised four times, and its own asserted
properties are directly measured.)

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: the window must actually run and its knob must be demonstrably live and
> demonstrably OFF in the control -- `use_offline_consolidation=True` on ON arms;
> `offline_ewc_installed=True` on every ON arm and `False` on the N=0 / OFF arm;
> `offline_n_fisher_states > 0`; and `mean_offline_ewc_penalty_recent > 0` on ON arms and exactly `0.0`
> on OFF. All four hold in V3-EXQ-836e: `window_n0` installed 0/10 seeds, penalty 0.0, capture 0.0;
> `window_n150 / n400 / n900` installed 10/10 each, penalty 0.246 / 0.316 / 0.346,
> `offline_n_fisher_states` 256 in every ON arm.
>
> CONFIRMING (SD-083's four asserted properties, each stated with the measured value that already
> answers it):
> (i) INTERVAL ACCUMULATION -- `offline_capture_resource` follows `c(N) = capture_max * (1 - exp(-N/tau))`:
> strictly increasing and saturating in `window_steps`, with `offline_effective_ewc_coef = capture *
> offline_ewc_max_coef`. MEASURED (836e, `offline_ewc_max_coef = 100.0`): capture
> 0.0 / 0.5276 / 0.8647 / 0.9889 and eff_coef 0.0 / 52.76 / 86.47 / 98.89 at N = 0 / 150 / 400 / 900.
> **CONFIRMED.**
> (ii) DOSE-INTERVAL ORTHOGONALITY -- the claim's own "BUILDS PROTECTION without retraining, so post_bc
> is invariant to the interval and the INTERVAL axis is orthogonal to the DOSE axis". MEASURED (836e):
> `post_bc_foraging_competence = 9.53` in ALL FOUR interval arms including N=0, identical to the
> reported precision. **CONFIRMED**, and this is the strongest single result -- it is the property that
> makes the interval axis interpretable at all.
> (iii) NOVELTY GATING (Moncada 2007) -- the paired/unpaired contrast must move
> `offline_novelty_factor` and hence `offline_effective_ewc_coef`, with capture, Fisher mass and post_bc
> matched. MEASURED (836d): paired novelty 1.0 -> eff_coef 77.69; unpaired novelty 0.05 -> eff_coef
> 3.88; `offline_capture_resource` 0.7769 and `offline_fisher_mass` 28.33 and `post_bc` 4.61 IDENTICAL
> across both arms. **CONFIRMED** -- the gate moves exactly one factor and nothing else.
> (iv) TRACE SELECTIVITY -- the Fisher is computed on the POLICY log-likelihood, so value-head
> parameters must receive ~0 weight (this is the property that distinguishes SD-083 from the ONLINE
> GLOBAL MECH-475 KL anchor, and it is the claim's stated distinctive content). Assert directly:
> per-parameter-GROUP Fisher mass, policy head vs value head, with the value-head share below (say) 1%
> of total. **NOT YET MEASURED** -- 836b/c/d/e report only a scalar `offline_fisher_mass`. This is the
> one open leg, and it is a manifest field, not an experiment.
> (v) RNG NEUTRALITY -- snapshot/restore around the window must leave post-window RNG state identical to
> the OFF arm. Covered at the unit level by
> `ree-v3/tests/contracts/test_sd083_offline_consolidation.py` (12/12) but never asserted in a run
> manifest; worth promoting to a manifest gate.
>
> FALSIFYING: `offline_capture_resource` non-monotone in `window_steps`, or flat, or not saturating
> (the c(N) form is wrong); OR `post_bc` moving with the interval (the window is RETRAINING rather than
> building protection, and the interval/dose axes are NOT orthogonal, which would invalidate every
> interval-arm reading built on this instrument); OR the novelty gate leaving `offline_effective_ewc_coef`
> unchanged between paired and unpaired (there is no novelty gating, only an unconditional anchor); OR
> value-head Fisher mass comparable to policy-head Fisher mass (the anchor is GLOBAL, not
> trace-selective, and SD-083's asserted distinction from MECH-475 collapses -- this is the sharpest
> available falsifier and the only one still open).
>
> POTENCY -- STATED SEPARATELY BECAUSE IT IS NOT SD-083's OWN CLAIM, BUT IS MANDATORY FOR ANY CONSUMER
> USING THIS INSTRUMENT: 836d/836e show the penalty is LIVE but not EFFICACIOUS. `retained_fraction` is
> invariant to a penalty whose coefficient varies ~14x (836e: 0.712 / 0.707 / 0.860 / 0.723 across
> eff_coef 0 / 52.8 / 86.5 / 98.9; leave-one-out stable across 10 folds, verdict `weakened` in all 10),
> and in 836d the WEAKER-penalty unpaired arm retained MORE than the paired arm (0.950 vs 0.834) --
> the wrong direction. Any future experiment consuming this window MUST carry a POTENCY precondition:
> demonstrate that the applied penalty CONSTRAINS the parameter update (e.g. post-refinement
> parameter-space distance from theta* falls measurably as eff_coef rises), because without it a null on
> the consumer claim cannot distinguish "no consolidation process" from "the anchor was too weak to
> matter". This distinction is not settled by anything on record.

**Proposal sketch (a):**
- **title:** "SD-083 instrument-validity readout: per-parameter-group Fisher mass (policy vs value head)
  and window RNG-neutrality, emitted from the existing `consolidate_offline_window` path"
- **related_claims:** SD-083 (primary), MECH-459, MECH-460 (the live successors of MECH-476), MECH-475
  (the online-global contrast this claim asserts it differs from), MECH-441
- **acceptance_checks:** (1) manifest emits per-parameter-group Fisher mass with value-head share
  reported; (2) manifest emits RNG-state equality against the OFF arm; (3) `claim_ids` names SD-083 with
  an explicit direction; (4) the four already-confirmed properties (i)-(iii) are re-emitted in the same
  manifest so the whole instrument-validity claim is banked in ONE artifact rather than reconstructed
  from four MECH-476-tagged runs; (5) a POTENCY readout (parameter-space distance from theta* as a
  function of eff_coef) so the potency gap is measured rather than inferred.
- **Cost note:** this is a reanalysis / instrumentation pass on an existing testbed path, not a new
  lineage. It should NOT be sized like the 836 runs.

**depends_on additions (if any):** **REPOINT, do not add.** `depends_on: [MECH-476, MECH-475, MECH-441,
SD-017]` currently names a RETIRED claim. Repoint `MECH-476 -> MECH-459, MECH-460` (per MECH-476's own
`superseded_by`), and either drop the `SD-017` edge or re-label it in `notes` as a PROSPECTIVE PORT edge
whose trigger is now unreachable -- as written it makes SD-083 look like live sleep-substrate work,
which it is not, and which the sleep plan explicitly warns against ("do not open a sleep GAP for it
pre-emptively").

**GOVERNANCE FLAG (two, kept separate):**

1. `evidence_discrepancy` -- SD-083 has `evidence: []` and no `claim_evidence.v1.json` entry, while FOUR
   non-degenerate runs (V3-EXQ-836b, 836c, 836d, 836e) declare SD-083 as their substrate, exercise its
   every asserted property, and record telemetry that CONFIRMS three of the four (capture curve
   0.0/0.5276/0.8647/0.9889; post_bc identical at 9.53 across all interval arms including N=0; novelty
   gate 1.0 -> eff_coef 77.69 vs 0.05 -> 3.88 with everything else matched). Its `implementation_note`
   still reads "NOT YET VALIDATED by experiment". The runs carry `claim_ids: ["MECH-476"]` only, so
   nothing routed. This is a routing gap, not a promotion request -- digestion does not promote -- but
   it is the clearest case in the group of banked evidence that never reached its claim.

2. `stale_note` -- SD-083's stated purpose is DISCHARGED and its onward gate is UNREACHABLE. It exists
   "to unblock MECH-476's two blocked_substrate falsifier arms"; both arms ran, both plus their
   redesigns scored `weakens`, and MECH-476 is now `status: retired` (superseded by MECH-459/MECH-460).
   The registered cognifold PORT into the SD-017 sleep loop is gated on "836b and/or 836c score
   SUPPORTED" (`sleep_substrate_plan.md`, 2026-07-29), which can never happen. Governance should (a)
   move SD-083 off `candidate_substrate_landed` to whatever status fits a validated instrument whose
   consumer retired, (b) repoint `depends_on`, and (c) record in the sleep plan that the SD-083 port
   trigger is dead so a later sleep session does not go looking for it. **Do NOT excrete SD-083** -- it
   is a landed, contract-tested, four-times-exercised instrument in the same `mech457` testbed where
   MECH-476's successors MECH-459/MECH-460 live, so it may still be consumed; only its framing is stale.

---

<!-- G3 appended 2026-09-04T21:18:57Z -->
## G3 -- control-plane commitment modulation cluster  (agent report)

### Group preamble

**Why these are together (restated, then my own view).** The grouping was made on namespace
(`control_plane.*`) plus title overlap on interrupt / release / independent-proposal / variability.
That is right about the namespace and misleading about the mechanism. The five partition into two
sub-clusters that the substrate itself already separates, in as many words:

- **Sub-cluster A -- the COMMIT gate** (the inequality `running_variance < effective_threshold`,
  ARC-016 / MECH-090): MECH-104 (fast surprise impulse on the *numerator*), MECH-106 (slow valence
  bias on the *denominator*), MECH-250 (periodic hard *release* bypassing the inequality),
  MECH-234 (whether more than one proposal can hold the effector at once).
- **Sub-cluster B -- the SELECTION softmax temperature** (what E3 does *given* it is choosing):
  SD-105 alone.

`/Users/dgolden/REE_Working/ree-v3/ree_core/regulators/phasic_surprise_burst.py` lines 9-21 draws
exactly this line for the MECH-104/SD-069 pair: *"RELATIONSHIP TO MECH-104 (important -- do not
conflate) ... THIS module routes the same surprise event to the E3 SELECTION softmax temperature
instead ... Same biological substrate, same source signal, different consumer."* The same reading
applies to MECH-250 vs SD-105.

**(i) same-claim / merge candidates.**
- **MECH-104 vs MECH-106: NOT the same claim, and no merge.** They act on opposite sides of one
  inequality at different timescales (MECH-104 = fast prediction-error impulse on `running_variance`;
  MECH-106 = slow outcome-valence EMA on `commit_threshold`). Because they move the same inequality,
  they are *mutually confounded in measurement* -- see (iv) -- but they are distinct mechanisms.
  MECH-106 `depends_on: MECH-104`; that dependency is real and I recommend keeping it (MECH-106's own
  notes position it explicitly as "distinct from MECH-104 (volatility interrupt, fast)").
- **MECH-250 -> MECH-108: STRONG PARTIAL merge pressure, pointing at an already-BUILT mechanism
  outside the group.** Full proposal under MECH-250 below. Headline: MECH-108's BreathOscillator is
  built (`ree_core/heartbeat/clock.py`), automatically wired (`agent.py:7287` -> `agent.py:9256`),
  and MECH-250's biological grounding is *already inside MECH-108's own code comment*
  (`clock.py:28`: "Biological basis: exhalation-phase respiratory coupling"). Expect PARTIAL
  absorption with a genuinely non-empty residual (WINDOW vs BOUNDARY; SOFTEN vs HARD-RELEASE).
- **MECH-234: not a merge candidate.** It is a lit-derived *design ruling on MECH-090*, not a
  parallel mechanism; its ruling has already been applied (its own notes: "Layer 3 ... is not
  warranted").
- **SD-105 vs MECH-313: no merge.** SD-105's own title positions it as the *state-dependent*
  complement of MECH-313's *state-independent* constant lift on the SAME channel; both knobs exist
  and are independently toggleable (`use_noise_floor`, `use_selection_entropy_floor`, both default
  False). But they must never be armed together without an arm pinning one -- SD-105's own
  `implementation_note` says it is applied *after* MECH-313, so MECH-313's readout
  (`noise_floor_temp`) deliberately reports the PRE-multiplier value.

**(ii) contradictions / undercut premises.**
1. **MECH-234 does NOT contradict the single-commitment assumption the others rest on -- it
   RATIFIES it for V3, and in doing so makes itself unfalsifiable here.** `ree_core/environment/`
   contains exactly one environment (`causal_grid_world.py`); its `action_dim` (line 1529) is a
   single discrete channel of 5 (6 with the consummatory act). MECH-234's *same-effector* leg
   ("winner-takes-all, not independent parallel expression") is therefore TRUE BY CONSTRUCTION in
   V3, and its *cross-effector* leg has no substrate to run on. So it neither threatens nor supports
   the other four.
2. **MECH-106 collides in SIGN with SD-011 (`status: stable`) on the very same variable.**
   `e3_selector.select()` composes `effective_threshold` as base -> `(1 - MECH-108 sweep)` ->
   `(1 + SD-011 urgency)` -> SD-093/MECH-426 (`predictors/e3_selector.py:3599-3625`). SD-011, as
   *fixed on 2026-08-26*, RAISES `effective_threshold` under accumulated threat -- i.e. harm makes
   commitment MORE permissive ("D2 avoidance escape response"). MECH-106 asserts the opposite: harm
   raises the biological threshold = *lowers* the variance-space threshold = commitment HARDER (and
   its own driver implements exactly that, `v3_exq_231a...py:261-269`). Both are latent by default
   (`urgency_weight = 0.0`; MECH-106 unbuilt), so there is no live conflict today -- but the moment
   MECH-106 is landed in the substrate it lands on the same multiplicative chain as a `stable`
   claim with the opposite sign under harm. Flagged.
3. **SD-105's own premise is undercut by a same-day BLOCKING red-team verdict that the claim block
   does not mention.** See the SD-105 entry and GOVERNANCE FLAG 5.

**(iii) shared falsifier.** Yes -- and it is a PRECONDITION rather than a test. All four
commit-gate claims are assertions about one inequality, and every one of them is vacuous unless
both sides of that inequality have live dynamic range in the run. State it once here; each of
MECH-104 / MECH-106 / MECH-250 cross-references it rather than re-deriving it.

> **THE COMMIT-GATE DYNAMIC-RANGE PRECONDITION (shared, G3).**
> `commitment_threshold = 0.40` in *variance space* (`ree_core/utils/config.py:1022`), and
> `variance_commit_threshold()` is the identity (`e3_selector.py:265`). The measured un-inflated
> operating point of `running_variance` is **0.005420** (V3-EXQ-794, recorded verbatim in
> `config.py:1058`) -- i.e. **~74x below the threshold**. The default agent is therefore
> *permanently committed*, which is precisely the degeneracy MECH-104's own `functional_restatement`
> predicts ("world_forward training drives running_variance to near-zero, permanently locking the
> agent in committed state"). Consequently any run adjudicating MECH-104 / MECH-106 / MECH-250 MUST
> report, from its CONTROL arm: (a) the realised `running_variance` range and its distance to
> `effective_threshold`; (b) the realised **committed-fraction, which must be strictly between 0
> and 1** -- at 1.0 no de-commitment can be observed, at 0.0 there is no commitment to break;
> (c) whether the SD-076 floor is binding. On (c), note the floor is *conditional*:
> `_apply_wci_rv_floor()` runs only inside the `use_waking_confidence_inflation` branch
> (`e3_selector.py:809-833`), and that flag defaults False (`config.py:1046`). When it IS armed, the
> floor is `waking_confidence_rv_floor = 0.01` absolute (`relative_frac` defaults 0.0, so the
> absolute path is the live one) and V3-EXQ-794 measured `rv_final` EXACTLY 0.010000 on all four
> arms -- a saturation signature, not a null. Either way the gap to 0.40 is 40x-74x.

**(iv) cross-cutting finding -- the committed-fraction is a shared confound that crosses the
sub-cluster boundary, so SD-105 is coupled to the other four despite the different consumer.**
`self.last_precommit_probs = probs.detach()` is written *inside* `e3_selector.select()`
(`e3_selector.py:3590`) -- and that is the distribution SD-105's controller integrates (its module
docstring: "the PREVIOUS waking tick's E3 pre-commit selection distribution
(`agent.e3.last_precommit_probs`)"). So anything that changes *how often the agent is uncommitted*
-- MECH-104's spike, MECH-106's bias, MECH-250's release, MECH-108's sweep -- changes the population
of ticks over which realised selection entropy is measured. Two consequences, both operational:

- **A null on SD-105's headroom restoration is uninterpretable unless the commit duty cycle is
  pinned or reported.** SD-105's entropy EMA is not a pure measure of policy confidence; it is
  confounded with the commit duty cycle. MECH-108 is *already on by default in every
  experiment-built config* (see Currency finding 5), injecting an uncommitted window every 50
  steps into exactly that trace.
- **Symmetrically, a de-commitment result on 104/106/250 measured on an SD-105-armed agent is
  uninterpretable**, because the selection temperature was being moved by a controller reading the
  very duty cycle under test.

**Pin one; never arm both live.** This is structurally the same defect the V3-EXQ-963b red team
found *within* the selection channel (finding F1: a closed-loop set-point controller sitting on the
DV it regulates). The group-level extension is that the loop also closes *through the commit gate*,
not only within selection -- which is new, and is not recorded anywhere I could find.

**Currency findings (verified this pass).**

1. **MECH-104's `status_note` is STALE.** It stops at EXQ-365 (2026-04-14). `claim_evidence.v1.json`
   shows two later non-excluded PASSes: `v3_exq_126...` re-run (2026-04-21T20:23:36Z) and
   **`v3_exq_623_mech104_volatility_interrupt_discriminative_pair` (2026-06-01T15:20:50Z, PASS)** --
   and 623 is the *important* one, being the first run to add the behavioural de-commitment gates
   (C6/C7) that the claim's own title asserts. Current index: `exp_conf 0.77`, 11 experimental
   entries, quadrant `confirmed_established`, `fail_runs 2` (both excluded: `superseded` /
   `non_contributory`).
2. **MECH-104's Route-2 is STILL NOT in the substrate, and every Route-2 result is
   driver-injected.** No `surprise_coeff`, no rv-directed `surprise_threshold`, no gated
   `_running_variance +=` anywhere under `ree_core/`. The impulse is poked in from the driver with
   an experimenter-chosen magnitude in every case: `v3_exq_061...py:~171`
   (`agent.e3._running_variance = float(...) + spike_magnitude`), `v3_exq_062b...py:347`
   (`agent.e3._running_variance += spike_magnitude`), and `v3_exq_623...py` docstring
   (`running_variance += SPIKE_MAGNITUDE * (surprise - SURPRISE_THRESHOLD)`). The substrate says so
   itself: `regulators/phasic_surprise_burst.py:32` -- *"the signal experiments already poke to fake
   MECH-104"*. Meanwhile EXQ-204, the one run that measured the **endogenous** spike, recorded
   `harm_spike_rv ~1.6-1.9e-6` -- roughly **five orders of magnitude** below the ~0.39 excursion
   needed to cross a 0.40 threshold. The claim's own `notes` do say Route (2) is "for later V3
   phases", so this is not a false statement in the block; it is a currency fact that changes how
   the `active` status should be read.
3. **MECH-106 has NO substrate implementation at all.** Zero hits for `MECH-106` and zero for
   `valence_bias` anywhere under `ree_core/`. The live `effective_threshold` chain
   (`e3_selector.py:3599-3625`) carries a MECH-108 sweep term, an SD-011 urgency term and an
   SD-093/MECH-426 term -- and no valence term. EXQ-231a's `_effective_threshold_vb()`
   (`v3_exq_231a...py:261`) is a **driver-local function**. The claim's `notes` sentence
   "V3 implementation: valence_bias updated at each E3 tick via a slow EMA on outcome valence
   signal" is a *plan written in the present tense*; it has not landed. MECH-106 is `provisional`
   on exactly one non-excluded experimental entry (`exp_conf 0.575`, quadrant `plausible_unproven`).
4. **SD-105's registered validation experiment was NOT queued, and its own substrate_queue entry
   says otherwise.** `evidence/planning/substrate_queue.json`
   (`sd_phasic_burst_decay_and_warmup_headroom.validation_experiment`) reads *"V3-EXQ-963b ...
   queued by campaign-c2c-20260904"*. It was not: ree-v3 commit **`d2104f8`** is titled
   *"V3-EXQ-963b driver: BLOCKING red-team verdict recorded, NOT queued"*; the live queue snapshot
   (ree-v3 `99817b6`, today) holds only V3-EXQ-1002 / V3-EXQ-983a / V3-EXQ-993a; and
   `git log -S"963b" -- experiment_queue.json` returns nothing. The driver exists and is lint-clean
   but is deliberately unqueued.
5. **MECH-108's `epistemic_category: substrate_conditional` looks stale, and it matters because
   MECH-250 depends on it.** The BreathOscillator is built (`heartbeat/clock.py`, `sweep_active`),
   automatically wired (`agent.py:7287` computes `sweep_reduction`, passed at `agent.py:9256`), and
   `REEConfig.from_dims()` defaults `breath_period = 50` (`config.py:8169`, assigned at
   `config.py:9791`) against the dataclass default of 0 (`config.py:3148`). Since every experiment
   builds its config through `from_dims`, **MECH-108 is ON by default in practice**, not merely
   buildable. It nonetheless carries **zero evidence rows**. The likely reason is arithmetic and is
   the key input to MECH-250 below: the sweep multiplies the threshold by `(1 - 0.25)`, i.e.
   0.40 -> 0.30, against an rv operating point of ~0.0054 -- still ~55x away, so **MECH-108's
   softening cannot produce a single uncommitted step at the current operating point.**
6. **MECH-234, MECH-250 and SD-105 each have zero evidence rows** in `claim_evidence.v1.json`
   (consistent with `candidate`). MECH-104: 11 experimental + 5 literature. MECH-106: 1 non-excluded
   experimental + 5 literature.
7. **None of the five is on the live front.** `docs/CURRENT_FRONT.md` (generated 2026-09-04T14:17Z):
   "The live front is the observation -> z_world -> E1/E2-rollout interface, **not the selector**:
   39 of 43 remaining v3 nodes chain to it." This should temper how much new compute the group
   attracts -- it argues for one well-targeted MECH-104 run and deferral/merge elsewhere.
8. **SD-105's block is substantively complete but has one gap and one questionable field.** Present:
   id/title/claim_type/subject/polarity/status/live_status/epistemic_category/implementation_phase/
   v3_pending/version_relevance/claim_level/registered_utc/depends_on/related_claims/source/
   functional_restatement/implementation_note. Its `source` design doc
   (`docs/architecture/sd_105_selection_entropy_headroom_floor.md`, 164 lines) exists. Missing:
   `location` (all four siblings in this group carry one), and no `notes`. The questionable field is
   `epistemic_category: standard` -- see the SD-105 entry. The design doc is *also* stale: line 151
   still names V3-EXQ-963b as the validation and it contains no mention of the freeze/share problem.

---

### MECH-104 -- Unexpected harm events spike commitment uncertainty (LC-NE volatility interrupt), enabling de-commitment.

**Recommended disposition:** **(a) testable now** -- the *endogenous* half of the claim is
substrate-live and default-on, and the one question no run has ever asked (does the UN-INJECTED
surprise spike actually de-commit?) is answerable on today's substrate with V3-EXQ-623's design
minus its driver injection.

**Extracted from:** V3-EXQ-623's pre-registered criteria (C1-C5 signal-magnitude gates, C6
behavioural de-commitment ratio >= 2.0x) fused with V3-EXQ-204's endogenous spike measurement
(`harm_spike_rv ~1.6-1.9e-6`, and its C1-C4 as recorded in the claim's own `status_note`). These
are the two halves of MECH-104's title that have never been run in the same arm. Not drafted fresh.

**Currency check:** `status_note` stops at EXQ-365 but two later PASSes exist, 623 being decisive
(`claim_evidence.v1.json`, `latest_run_id = v3_exq_623_..._20260601T152050Z_v3`). Route-2 is absent
from `ree_core/` (no `surprise_coeff`; grep of the whole tree); every Route-2 run injects from the
driver (`v3_exq_061...py:~171`, `v3_exq_062b...py:347`, `v3_exq_623...py` docstring), which
`regulators/phasic_surprise_burst.py:32` states outright. The SD-076 rv floor
(`config.py:1053`, gated on `use_waking_confidence_inflation`, default False at `config.py:1046`)
landed 2026-07-22 -- *after* MECH-104 went active -- and is now a load-bearing precondition of every
rv readout. V3-EXQ-623 additionally ran with `use_mech090_readiness_conjunction=False` and
`use_commit_readiness_gate=False`, so the evidence is at a readiness-gates-OFF configuration.

**epistemic_category (proposed):** `standard` (keep / set explicitly). The endogenous EMA path is
built and default-on and nothing downstream absorbs its signal -- the signal is simply small, which
is a measurable fact rather than a ceiling. **If the run below falsifies the behavioural leg while
replicating the selectivity leg, THAT is the moment to re-tag `substrate_ceiling`** (built,
repeatedly exercised, causal signal cannot reach the outcome metric) and route to substrate work on
the rv-to-threshold gap.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it. Specific to this run, the CONTROL (gate-ON,
> no-injection) arm must report and satisfy: (a) realised `running_variance` range and its distance
> to `effective_threshold` (base 0.40, `config.py:1022`); (b) realised committed-fraction strictly
> between 0 and 1 -- a run at 1.0 cannot observe a de-commitment; (c) `n_unexpected_harm_events >= 10`
> occurring *in committed state* (V3-EXQ-623 C5); (d) the SD-076 floor's binding fraction --
> `running_variance` must not sit at `waking_confidence_rv_floor` for more than 10% of ticks, which
> is the exact clamp V3-EXQ-794 hit (`rv_final` EXACTLY 0.010000 on all four arms); and (e)
> **`breath_period = 0` in BOTH arms**, because `from_dims` otherwise arms MECH-108's sweep by
> default and a sweep-driven uncommitted window would be misread as a surprise-driven one. And,
> load-bearing: **no line of the driver may write `agent.e3._running_variance` in the ON arm** --
> the entire question is whether the endogenous impulse suffices.
>
> **CONFIRMING.** On a matched-seed pair over >= 3 seeds sharing trained weights and episode
> sequence -- ENDOGENOUS-ON vs ABLATED (`_ema_alpha = 0.0`, variance frozen; the V3-EXQ-204
> ablation) -- the ON arm shows BOTH legs *in the same arm*: (i) SELECTIVITY: endogenous
> `delta_var_unexpected` exceeds `delta_var_expected` by more than 3 SD of the per-seed delta AND by
> an absolute floor of 1e-4, in >= 2 of 3 seeds; and (ii) SUFFICIENCY: committed -> uncommitted
> transitions attributable to those events (V3-EXQ-623's 20-tick POST_SPIKE_WINDOW attribution)
> occur at >= 2.0x the ABLATED arm's rate, with the ABLATED rate reported and non-degenerate, in
> >= 2 of 3 seeds. Leg (ii) in the absence of any injection is what has never been shown.
>
> **FALSIFYING.** Leg (i) replicates and leg (ii) does not: the endogenous `delta_var_unexpected` is
> real and selective but stays far below the rv-to-threshold gap, so committed -> uncommitted
> transition rates are statistically indistinguishable between ON and ABLATED. V3-EXQ-204's own
> endogenous magnitude (`harm_spike_rv ~1.6-1.9e-6` against a ~0.39 gap) *predicts exactly this
> outcome*, so it must be treated as the live alternative hypothesis, not the surprise. This
> refutes the "enabling de-commitment" half of the title while leaving "spikes commitment
> uncertainty" standing, and is grounds to demote MECH-104 from `active` and to re-tag it
> `substrate_ceiling`. A second, distinct falsifying pattern: the ABLATED arm shows the *same*
> transition rate, which means the observed transitions were never surprise-driven at all (most
> likely MECH-108's sweep, or the readiness gates) -- which is why precondition (e) is mandatory.

**Proposal sketch (a):**
- **title:** `V3-EXQ-<next> -- MECH-104 endogenous volatility interrupt: does the UN-INJECTED surprise spike de-commit? (supersedes V3-EXQ-623's behavioural leg, which injected)`
- **related_claims:** `MECH-104`, `ARC-016`, `MECH-090`, `SD-076`, `MECH-108` (as a pinned-off confound)
- **acceptance_checks:** C1-C2 selectivity as above; C3 ABLATED flat (`delta_var_unexpected < 1e-6`);
  C4 cross-condition discriminative delta; C5 `n_unexpected_harm >= 10` in committed state;
  **C6 de-commitment ratio >= 2.0x with the ABLATED denominator reported**; C7 committed-fraction in
  (0,1) in every arm; C8 `breath_period == 0` asserted at runtime in both arms; C9 no write to
  `_running_variance` outside `update_running_variance()` (assert by source lint, as V3-EXQ-623's
  own driver could not). Declare a `dv_headroom` precondition **denominated on the same statistic
  each criterion routes on** -- the V3-EXQ-963b F3 lesson (max_abs read 1.55x headroom where the
  4-of-5-seed statistic read a 2.3x shortfall).

**depends_on additions:** `SD-076` -- the waking-confidence rv floor is now a precondition of every
MECH-104 readout and postdates the claim's promotion.

**GOVERNANCE FLAG:** `stale_note` -- MECH-104's `status_note` stops at EXQ-365 (2026-04-14) and omits
the two later non-excluded PASSes, including V3-EXQ-623 (2026-06-01), which is the strongest evidence
on file and the only run to test the behavioural half of the title.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- MECH-104's `active` status rests on a conjunction
*across* runs that no single run establishes: endogenous SELECTIVITY (V3-EXQ-204) plus
driver-INJECTED SUFFICIENCY (V3-EXQ-061 / 062b / 623). The only endogenous magnitude ever measured
(`harm_spike_rv ~1.6-1.9e-6`) is ~5 orders of magnitude below the ~0.39 rv-to-threshold gap, and
`regulators/phasic_surprise_burst.py:32` describes the injection path as experiments that "poke to
fake MECH-104". This does not make the claim wrong; it makes `active` a stronger reading than the
evidence supports until the run above is done.

---

### MECH-106 -- Commitment threshold is asymmetrically modulated by outcome valence: positive outcomes lower it, negative outcomes raise it.

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`**, blocking substrate
= the valence-bias term on `effective_threshold`, which has never existed in `ree_core/`; the sole
supporting run emulated it inside its own driver, and that emulation is *symmetric*, so the
ASYMMETRY the claim is named for has not in fact been tested.

**Extracted from:** the claim's own `functional_restatement`
(`commit_threshold_effective = commit_threshold_base x (1 + valence_bias)`) and V3-EXQ-231a's five
pre-registered criteria (C1 `da_divergence > 0.20`, C2 `threshold_asymmetry > 1.20`,
C3 `latency_ratio_vb > 2.0`, C4 `latency_ratio_nb in [0.5, 2.5]`, C5 `asymmetry_delta > 1.0`), read
against that driver's actual implementation at `v3_exq_231a...py:147-152, 261-269, 546-557`.

**Currency check:** **No substrate implementation exists.** Zero hits for `MECH-106` and zero for
`valence_bias` in `ree_core/` (whole-tree grep). The live `effective_threshold` composition
(`e3_selector.py:3599-3625`) is base -> MECH-108 sweep -> SD-011 urgency -> SD-093/MECH-426; there is
no valence term. `_effective_threshold_vb()` at `v3_exq_231a...py:261` is driver-local. The claim's
`notes` line "V3 implementation: valence_bias updated at each E3 tick via a slow EMA" is an unlanded
plan in the present tense. Index: `exp_conf 0.575`, `genuine_exp_count 1`, quadrant
`plausible_unproven`, `fail_runs 0` (the two EXQ-231 FAILs are `scoring_excluded: superseded`).

**Additionally, and this is the substantive finding: V3-EXQ-231a's C2 is not independent of its C1.**
The driver sets `BIAS_WEIGHT = 1.2` and
`effective_threshold = base * (1 + 1.2 * (da - 0.5))` (`v3_exq_231a...py:152, 269`) -- a **symmetric
linear map in `da` about 0.5**. C2's metric is
`threshold_asymmetry = threshold_pos_vb / threshold_neg_vb` (line 547), which under that map is a
deterministic function of C1's `da_divergence = da_pos - da_neg`. Working the recorded numbers:
`da_divergence = 0.73-0.78` gives, e.g. at `da_pos ~= 0.87 / da_neg ~= 0.11`,
`(1 + 1.2 x 0.37) / (1 + 1.2 x -0.39) = 1.444 / 0.532 = 2.71` -- which is exactly the reported
`threshold_asymmetry = 2.7-2.8`. So C2 could not have failed once C1 passed. More importantly, a
symmetric linear modulation **cannot distinguish "asymmetric valence modulation" (Frank 2005's
asymmetric D1/D2 dynamic range, which is MECH-106's actual assertion) from "any monotone valence
modulation"**. The asymmetry half of the title is untested.

**epistemic_category (proposed):** `substrate_conditional` (set explicitly). Per REE_assembly
CLAUDE.md's sharpened discriminator: the mechanism the claim asserts has *never been exercised in the
substrate* -- the code does not exist -- and the one banked positive result comes from a driver
emulation whose functional form does not match the claim. That is `substrate_conditional`, not
`substrate_ceiling` (nothing downstream is absorbing a signal; there is no signal in the substrate).

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it -- and note MECH-106 needs it *twice over*, because both
> the base threshold and the valence-modulated threshold must sit where `running_variance` can
> actually cross them. Specific to this claim: (a) the run must exhibit a **differentiated valence
> history** -- `da_pos - da_neg > 0.20` measured, which is the precise failure that made the original
> V3-EXQ-231 a design flaw rather than a claim failure ("PERSISTENT and REACTIVE conditions produced
> identical commit values"); (b) latency-to-commit must be finite and unsaturated in BOTH the
> positive-history and negative-history conditions -- an episode-length-censored latency in the
> negative condition measures the episode budget, not the threshold; (c) the modulation must be
> implemented **asymmetrically**, i.e. with independent gains for the positive and negative
> directions (`w_pos != w_neg` as free parameters), because a symmetric linear map makes the
> asymmetry criterion an arithmetic consequence of the divergence criterion (see V3-EXQ-231a above)
> and therefore vacuous; (d) MECH-104's impulse and SD-011's urgency term must be pinned OFF
> (`urgency_weight = 0.0`, no rv injection) -- they move the same inequality (G3 preamble (iv)).
>
> **CONFIRMING.** With independent positive/negative gains and a matched-seed VALENCE_BIAS vs NO_BIAS
> ablation over >= 5 seeds: (i) the **direction** leg -- mean latency-to-commit is longer after a
> negative-outcome history than after a positive one in the VALENCE_BIAS arm, by more than 3 SD of
> the per-seed latency delta and by an absolute floor of 5 ticks, in >= 4 of 5 seeds, while the
> NO_BIAS arm shows a latency ratio inside [0.5, 2.5] (V3-EXQ-231a's C4, retained as the
> no-manipulation control); and (ii) the **asymmetry** leg, which is the claim's actual content --
> the fitted `|w_neg| / |w_pos|` is bounded away from 1.0 (>= 1.5, or <= 0.67) with a
> per-seed-bootstrap CI excluding 1.0, in >= 4 of 5 seeds. Leg (ii) must be measured, not assumed:
> it is what separates MECH-106 from the weaker claim "outcome valence modulates the commit
> threshold at all".
>
> **FALSIFYING.** Either (i) fails -- valence history does not shift commitment latency once
> MECH-104 and SD-011 are pinned off, which would say the EXQ-231a result was carried by the
> driver's hand-set `BIAS_WEIGHT` rather than by any property of outcome valence -- or (i) passes
> and (ii) fails, i.e. `|w_neg| / |w_pos|` is statistically indistinguishable from 1.0. The second
> is the more likely and the more informative: it would refute MECH-106 *as written* (asymmetric)
> while supporting a narrower successor ("outcome valence modulates the commit threshold
> monotonically"), and would be grounds to demote from `provisional` and re-title. A third pattern:
> the seed-42 anomaly recorded in `evidence_quality_note` ("near-zero divergence, no commitments")
> recurs on more than 1 of 5 seeds -- that is precondition (a) failing, not a result, and the run
> must be re-designed rather than adjudicated.

**Proposal sketch:** none -- this is disposition (c), not (a). The run above is only writable once
the valence-bias term exists in `e3_selector`'s `effective_threshold` chain **with independent
positive/negative gains**. That is a small, well-specified substrate build (one EMA + one
two-gain multiplier at `e3_selector.py:3599`, alongside the existing MECH-108 and SD-011 terms) and
is the correct thing to route to `/implement-substrate` -- but it MUST be designed against the
SD-011 sign collision below, not landed beside it silently.

**depends_on additions:** none. (`MECH-104`, `MECH-090`, `ARC-016`, `MECH-105` are all correct and
live. `MECH-104` is `active`; per the G3 brief's question, MECH-106 inherits a **live but
narrower-than-advertised** precondition -- MECH-104's endogenous selectivity is real and
substrate-live, its de-commitment sufficiency is driver-injected only. So the precondition is not
dead, but MECH-106 should not be read as inheriting "de-commitment demonstrably works".)

**GOVERNANCE FLAG:** `evidence_discrepancy` -- MECH-106 is `provisional` on a single non-excluded
run (V3-EXQ-231a) in which (1) the mechanism was implemented **in the driver, not the substrate**
(no `valence_bias` anywhere in `ree_core/`), and (2) criterion C2 (`threshold_asymmetry > 1.20`) is
an arithmetic consequence of criterion C1 (`da_divergence > 0.20`) under that driver's own
symmetric linear map `base * (1 + 1.2 * (da - 0.5))` -- reproduced numerically above -- so the
"5/5 criteria" count over-states the independent evidence, and the **asymmetry** the claim is named
for was never tested.

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-106 and SD-011 (`status: stable`) make
**opposite-sign** predictions about how harm modulates `effective_threshold`, on the same
multiplicative chain in `e3_selector.select()` (`e3_selector.py:3599-3625`). SD-011's block was
sign-flipped on 2026-08-26 to RAISE the threshold under accumulated threat (commit *more* readily,
"D2 avoidance escape response"); MECH-106 asserts harm makes commitment *harder*. Both are latent by
default (`urgency_weight = 0.0`; MECH-106 unbuilt), so there is no live defect -- but this must be
adjudicated **before** any MECH-106 substrate build lands, or the two will silently cancel.

---

### MECH-234 -- DMS (goal-directed) and DLS (habitual) corticostriatal circuits can produce simultaneous parallel motor outputs only when targeting anatomically distinct motor effector pools...

**Recommended disposition:** **(c) substrate-blocked -- `substrate_conditional`**, reframed onto the
REE leg (cross-effector parallel expression), which is blocked on a multi-effector environment that
does not exist; the out-of-domain leg (the DMS/DLS anatomy) is already discharged by the two reviews
the claim itself cites, and the claim's *design ruling* has already been applied.

This is a **FUSED claim** and I am following the brief's instruction to reframe to the REE leg and
name the other. The two legs:
- **Out-of-domain leg (dominant in the title):** "DMS/DLS produce simultaneous parallel outputs only
  across anatomically distinct effector pools; within a pool, BG winner-takes-all." This is
  neuroanatomy. It is resolved, by Redgrave et al. (2010) `10.1038/nrn2915` and Balleine &
  O'Doherty (2010) `10.1038/npp.2009.131`, both already cited in the block. No REE substrate at any
  level bears on it. It should not be carried as an open mechanism_hypothesis.
- **REE leg (the reframe):** "in a substrate whose outputs share one effector pool, an independent
  parallel habitual channel (Layer 3) is not warranted; MECH-090 BetaGate's same-effector
  suppression is the correct model." This is a **design ruling on MECH-090** and it has already
  fired -- the block's own `notes` say Layer 3 "is not warranted" and names Layers 1+2 as the
  correct implementation.

**Extracted from:** the claim's own `notes` ("REE DESIGN IMPLICATION" paragraph) and its
`literature_evidence`. No `experimental_test` field exists; nothing drafted fresh.

**Currency check:** `ree_core/environment/` contains exactly one environment,
`causal_grid_world.py`. Its action space is a single discrete channel: `action_dim` (line 1529) is 5,
growing to 6 when the consummatory-act flag is on (lines 544, 2341-2344). There is no second
effector pool and no multi-effector environment anywhere in the tree. Zero evidence rows in
`claim_evidence.v1.json`. Zero reverse-dependencies in `claims.yaml` (checked by structural scan of
`depends_on` / `related_claims` / `supersedes` / `blocks` / `conflicts_with`). `depends_on: MECH-090`
(`active`) and `ARC-021` (`provisional`) are both live. **Answering the G3 brief's question
directly: MECH-234 does NOT contradict the single-commitment assumption the other four rest on -- it
is the claim that RATIFIES it for V3, and its same-effector leg is true by construction here.**

**epistemic_category (proposed):** `substrate_conditional` (set explicitly), with the out-of-domain
leg named in the claim text. Rationale for choosing `substrate_conditional` over `out_of_domain`:
the residual REE question *would* be helped by a substrate (a multi-effector environment), which is
the discriminator the brief's (c2) reserves `out_of_domain` for the absence of. Governance may
alternatively prefer to reclassify `claim_type: literature_synthesis` and close the REE leg as an
applied design ruling -- I flag that as the live alternative rather than deciding it here.

**Draft `what_would_answer`:**

> **NON-DEGENERACY PRECONDITION.** The test requires an environment with **>= 2 anatomically
> distinct effector pools** -- two independently-commandable action channels whose commands are not
> mutually exclusive within a step. `ree_core/environment/causal_grid_world.py` has exactly one
> (`action_dim` 5-6, a single discrete choice, `causal_grid_world.py:1529, 2341-2344`), so on the
> current substrate the same-effector leg is TRUE BY CONSTRUCTION and the cross-effector leg is
> UNTESTABLE -- there is no non-degenerate run available and any "confirmation" would be vacuous.
> Additionally: a habitual channel distinct from the E3 deliberative channel must be separately
> observable (E1-direct or a policy-chunking output per `ree_core/policy/policy_chunking.py`,
> ARC-071), so that "both computed" can be distinguished from "one was expressed".
>
> **CONFIRMING (conditional on a multi-effector substrate landing).** With two channels A and B, and
> a committed E3 trajectory addressing channel A: (i) CROSS-DOMAIN -- the habitual output on channel
> B is expressed at a rate statistically indistinguishable from its uncommitted baseline (a
> ratio within [0.85, 1.15] with a bootstrap CI excluding 0.5), i.e. commitment does not suppress the
> other pool; AND (ii) SAME-DOMAIN -- the habitual output on channel A is suppressed relative to its
> uncommitted baseline by more than 3 SD of the per-seed suppression delta and by an absolute floor
> of 50% expression loss, in >= 2 of 3 seeds. The claim's content is the CONJUNCTION and the
> DISSOCIATION between (i) and (ii); either alone is a weaker claim.
>
> **FALSIFYING.** Either (i) fails -- commitment suppresses the *other* effector pool too, which
> would mean REE's commitment is a global gate rather than a per-effector one and would invalidate
> the "Layer 3 applies in multi-effector environments" half of the ruling -- or (ii) fails, i.e. the
> habitual channel is expressed on the committed effector concurrently with the deliberative one,
> which would refute the winner-takes-all model MECH-090's BetaGate encodes and reopen the Layer 3
> design question the claim closed. **For the out-of-domain leg, a counterexample looks like:** a
> peer-reviewed report of *simultaneous, independently-expressed* DMS- and DLS-driven motor output
> within a single effector pool in an intact animal (i.e. not sequential alternation and not
> cross-pool), which would contradict Balleine & O'Doherty (2010)'s qualification and require the
> title's "only when" to be weakened.

**Proposal sketch (only for a/d):** n/a.

**depends_on additions:** none. (`MECH-090` active, `ARC-021` provisional; both correct.)

**GOVERNANCE FLAG:** `contested_disposition` -- MECH-234 has sat at `candidate` since 2026-04-15 with
zero evidence rows and zero reverse-deps while its operative content (a design ruling: do not build
Layer 3) was applied long ago. It is either (a) a `literature_synthesis` whose REE consequence has
been discharged, or (b) a `substrate_conditional` mechanism awaiting a multi-effector environment
that is not on any roadmap I could find. Leaving it as an undifferentiated `candidate`
mechanism_hypothesis costs governance a recurring adjudication with no possible next step.

---

### MECH-250 -- The end of exhalation provides a hard, periodic release signal for committed motor programs via respiratory-motor coupling...

**Recommended disposition:** **(g) merge with sibling -- PROPOSE ONLY: partial absorption into
MECH-108 (already BUILT and default-on, outside the group), with a narrowed but genuinely non-empty
residual.** MECH-250 must not be superseded outright: its residual is the only breath-timed
mechanism that can actually fire at the substrate's current operating point.

**Merge proposal, in the required form.**
- **Surviving id:** `MECH-108` (BreathOscillator). Built at `ree_core/heartbeat/clock.py`
  (`sweep_active`, `_breath_phase_step`, `_sweep_amplitude`, `_sweep_duration`), automatically wired
  at `agent.py:7287` (`sweep_reduction = self.clock.sweep_amplitude if self.clock.sweep_active else
  0.0`) and consumed at `agent.py:9256` -> `e3_selector.py:3600-3601`.
- **Absorbed id:** `MECH-250`, **partially**.
- **What text moves:** MECH-250's respiratory-motor-coupling biology (diaphragm and accessory-muscle
  relaxation at end-expiration; the cross-species observation -- dogs timing initiation to a sharp
  outbreath, human vocalisation on expiration, skilled striking actions clustering at exhale-end)
  should move into MECH-108's `notes` as its biological grounding. **MECH-108's code already carries
  a one-line version of it** (`clock.py:28`: "Biological basis: exhalation-phase respiratory coupling
  cyclically modulates..."), so the claims registry is currently *behind its own substrate* on this
  point -- the merge closes that gap rather than opening a new one.
- **What must NOT be absorbed (the residual, and it is real):** two orthogonal distinctions the
  claim itself draws and that the substrate genuinely does not implement.
  1. **WINDOW vs BOUNDARY.** MECH-108 asserts a sweep *window* (`sweep_duration = 5` of every
     `breath_period = 50` steps). MECH-250 asserts a *phase boundary* event at exhale-end. The
     boundary is derivable from `clock._breath_phase_step` but is not exposed as an event, and
     `EXHALE` / `receive_respiratory_phase` appear nowhere in `ree_core/`.
  2. **SOFTEN vs HARD-RELEASE, and this is the load-bearing half.** MECH-108 multiplies the
     threshold by `(1 - sweep_amplitude)` = `(1 - 0.25)`, i.e. **0.40 -> 0.30**. Against the measured
     un-inflated `running_variance` operating point of **0.005420** (V3-EXQ-794, quoted at
     `config.py:1058`) that is still ~55x away -- **so MECH-108's softening cannot produce a single
     uncommitted step at the current operating point.** This is almost certainly why MECH-108 has
     zero evidence rows despite being on by default. MECH-250 instead asserts an unconditional
     `beta_gate.release()` -- and `BetaGate.release()` exists (`ree_core/heartbeat/beta_gate.py:178`,
     with ten call sites in `agent.py`). **A hard release is therefore the only breath-timed
     mechanism that can fire at all on this substrate**, which makes MECH-250's residual more
     valuable after the merge, not less.
- **Reverse-deps needing repointing:** **none.** Structural scan of `claims.yaml` finds zero
  `depends_on` / `related_claims` / `supersedes` / `blocks` / `conflicts_with` references to
  MECH-250. (Note the *forward* chain MECH-250 -> MECH-108 -> MECH-104 exists and is unaffected.)

**Extracted from:** the claim's own `notes` -- specifically its explicit MECH-108 contrast ("not a
threshold-softening effect but a positive release trigger: it actively drives beta_gate.release()")
and its implementation hint ("extend BetaGate with `receive_respiratory_phase(phase) -> release at
EXHALE_END`, driven by the MultiRateClock breath cycle state"). Not drafted fresh.

**Currency check:** `beta_gate.release()` exists (`heartbeat/beta_gate.py:178`). The MultiRateClock
tracks a breath cycle (`clock.py:83-97`) but exposes only the boolean `sweep_active` (line 108) --
**no phase-boundary event, no `receive_respiratory_phase`, no `EXHALE` token anywhere in
`ree_core/`** (whole-tree grep). So MECH-250's implementation hint is accurate and unbuilt.
Meanwhile its dependency MECH-108 is *further along than the registry says*: built, auto-wired, and
ON by default in every experiment-built config because `REEConfig.from_dims()` defaults
`breath_period = 50` (`config.py:8169`, assigned `config.py:9791`) against a dataclass default of 0
(`config.py:3148`) -- yet MECH-108 carries `epistemic_category: substrate_conditional` and zero
evidence rows. MECH-250's other dependencies: `ARC-028` `candidate`, `MECH-091` `candidate`,
`MECH-090` `active`. Zero evidence rows for MECH-250 itself.

**epistemic_category (proposed):** `substrate_conditional` (set explicitly) for the residual after
absorption. The positive release trigger has never been exercised because the code does not exist;
blocking substrate = a phase-boundary event on `MultiRateClock` plus
`BetaGate.receive_respiratory_phase()`. This is a small, well-specified build.

**Draft `what_would_answer`** (written for the residual, i.e. after the MECH-108 absorption -- the
question is *hard release at a boundary*, not *periodic uncommitted windows*, which is MECH-108's):

> **NON-DEGENERACY PRECONDITION.** See the group's shared COMMIT-GATE DYNAMIC-RANGE PRECONDITION
> (G3 preamble (iii)); do not re-derive it. Specific to this claim, and decisive: the run must
> establish that **MECH-108's existing threshold softening is INERT at the run's own operating
> point** -- report `effective_threshold` under sweep (`0.40 x (1 - sweep_amplitude)`) against the
> realised `running_variance` distribution, and confirm the softened threshold is not crossed. If
> the sweep alone *does* produce uncommitted steps in this configuration, MECH-250's residual is not
> separable from MECH-108 in that run and the run cannot adjudicate it -- re-derive the operating
> point first. Additionally: (a) the committed-fraction in the release-OFF control arm must be
> strictly between 0 and 1, and specifically **high** (> 0.8) -- a hard release is only observable
> against a background of sustained commitment; (b) the breath cycle must be running
> (`breath_period > 0`) and the exhale-end boundary must be counted, with `n_boundaries >= 20` per
> episode-block; (c) MECH-104's surprise impulse must be pinned off (no rv injection,
> `_ema_alpha` at its default) so that de-commitments cannot be attributed to two mechanisms at
> once (G3 preamble (iv)).
>
> **CONFIRMING.** With a `receive_respiratory_phase(EXHALE_END) -> beta_gate.release()` build, on a
> matched-seed RELEASE-ON vs RELEASE-OFF pair (both with `breath_period = 50`, so MECH-108's sweep is
> identical in both arms and cancels): (i) **PHASE-LOCKING** -- committed -> uncommitted transitions
> in the ON arm cluster at the exhale-end boundary, with a circular-phase concentration over the
> breath cycle whose Rayleigh test rejects uniformity at p < 0.01 in >= 2 of 3 seeds; and
> (ii) **CAUSAL CONTRIBUTION** -- the ON arm's transition rate exceeds the OFF arm's by more than
> 3 SD of the per-seed rate delta and by an absolute floor of 1 transition per 5 breath cycles.
> Leg (i) is what distinguishes MECH-250 from any generic periodic de-commitment, and (ii) is what
> distinguishes it from MECH-108's already-present sweep.
>
> **FALSIFYING.** (ii) holds but (i) fails: transitions increase but are uniformly distributed over
> the breath cycle, meaning the mechanism is a periodic release *rate* rather than a
> *phase-locked boundary* event -- that refutes MECH-250 as written and collapses the residual back
> into MECH-108's window model, i.e. it makes the full absorption correct after all. Alternatively,
> (i) and (ii) both hold but the OFF arm shows the same transition rate once `breath_period = 0` is
> also tested as a third arm -- meaning the transitions were produced by the sweep, not the release.
> A third pattern, and the cheapest to hit: the OFF arm's committed-fraction is already < 0.8 in
> the control, so there was never sustained commitment for a release to break -- that is the
> precondition failing, and is a re-design signal, not a result.

**Proposal sketch (only for a/d):** n/a -- disposition is (g), and the run above is only writable
after the (small) substrate build. If governance prefers, route
`MultiRateClock` phase-boundary event + `BetaGate.receive_respiratory_phase()` to
`/implement-substrate` as a single entry, since it is fully specified by the claim's own hint.

**depends_on additions:** none needed; `MECH-108`, `ARC-028`, `MECH-091`, `MECH-090` are all present
and correct.

**GOVERNANCE FLAG:** `stale_note` (concerns MECH-108, surfaced via MECH-250's dependency) --
MECH-108 carries `epistemic_category: substrate_conditional` while its BreathOscillator is built
(`heartbeat/clock.py`), auto-wired (`agent.py:7287` -> `9256` -> `e3_selector.py:3600`), and ON by
default in every experiment-built config (`REEConfig.from_dims` defaults `breath_period = 50`,
`config.py:8169/9791`, against a dataclass default of 0 at `config.py:3148`). It nonetheless has zero
evidence rows -- most likely because its 25% threshold softening (0.40 -> 0.30) is arithmetically
inert against an rv operating point of ~0.0054. Either the category is stale, or MECH-108 is a
*built-but-inert* mechanism, which is a different and more interesting finding. Worth one
adjudication.

---

### SD-105 -- Selection-entropy headroom floor: a TONIC behavioural-variability set-point on the E3 selection softmax temperature (one-sided integral controller in log-temperature)

**Recommended disposition:** **(f) defer with a durable `digestion_note`** -- the claim was
registered today and is well-formed, but its own registered validation route was **killed the same
day** by a BLOCKING red-team verdict that neither the claim block nor its design doc records, and
the named fix requires a substrate capability SD-105 does not have. What must be resolved first is
named precisely below. (Secondary reading, if governance prefers a category to a defer:
`substrate_conditional` on the freeze/share API.)

**Extracted from:** the claim's own `functional_restatement` and `implementation_note`; the module
docstring at `ree-v3/ree_core/regulators/selection_entropy_floor.py` (which specifies the controller
and its `get_state()` reporting surface, including `headroom_met`, `saturated`,
`n_ticks_saturated`); the design doc
`REE_assembly/docs/architecture/sd_105_selection_entropy_headroom_floor.md`; and -- decisively --
the STEP 4.5 RED-TEAM VERDICT block at
`ree-v3/experiments/v3_exq_963b_mech063ii_tonic_phasic_dissociation_retest.py:544-640`.

**Currency check -- the block is complete but two of its statements are already false.**
- *Complete:* the block carries id/title/claim_type/subject/polarity/status/live_status/
  epistemic_category/implementation_phase/v3_pending/version_relevance/claim_level/registered_utc/
  depends_on (SD-074, MECH-313)/related_claims (SD-104, SD-069, MECH-063)/source/
  functional_restatement/implementation_note. Its design doc exists (164 lines). **Missing:**
  `location` (all four siblings in G3 carry one) and `notes`. One reverse-dep: SD-104
  `related_claims`.
- *Built and default-off, as claimed:* `ree_core/regulators/selection_entropy_floor.py` exists;
  `use_selection_entropy_floor: bool = False` with `_target 0.15`, `_gain 0.5`,
  `_max_temperature_ratio 8.0`, `_ema_decay 0.2`, `_deadband 0.05` (`config.py:4430-4446`, wired
  through `from_dims` at `config.py:7359-7364, 8793-8794`); application site at `agent.py:1225`.
  Contracts B1-B10 exist. Zero evidence rows. Substrate_queue entry
  `sd_phasic_burst_decay_and_warmup_headroom` is `implemented_pending_validation` /
  `status_phase: validation_owed`, both legs built.
- **FALSE STATEMENT 1 -- "validation is V3-EXQ-963b" (in `functional_restatement`), and
  substrate_queue's `validation_experiment: "... queued by campaign-c2c-20260904"`.** V3-EXQ-963b
  was **not queued**. ree-v3 commit `d2104f8` is titled *"V3-EXQ-963b driver: BLOCKING red-team
  verdict recorded, NOT queued"*; the live queue snapshot (ree-v3 `99817b6`, 2026-09-04) contains
  only V3-EXQ-1002 / 983a / 993a; `git log -S"963b" -- experiment_queue.json` returns nothing.
- **FALSE STATEMENT 2 (implicit) -- that arming SD-105 in a difference-of-arms design is sound.**
  Red-team finding **F1, "CONFIRMED / NOT FIXED (the blocking core)"**: *"SD-105 is a closed-loop
  SET-POINT controller on S_sustained_entropy -- the exact DV C1's dS_tonic contrast reads... A
  set-point controller applies a DIFFERENT lift per arm precisely because arms start at different
  entropies, so it COMPRESSES the contrast rather than cancelling it."* Verified against
  V3-EXQ-963a's own per-arm data: at `SEF_TARGET = 0.12` the controller would lift some arms and
  hold others on 4 of 5 seeds, and *"on seeds 23/29/37 it lifts exactly the TONIC-OFF arms and holds
  the TONIC-ON arms -- differentially compressing dS_tonic in the direction that destroys C1."* The
  verdict also notes SD-105's R5 gate *"passes by construction (the controller drives T0P0 toward
  0.12 > E_SAT_LOW) -- a gate certifying its own subject."* The named fix (successor requirement
  (a)): converge the controller ONCE and apply a **single FROZEN, SHARED multiplier** uniformly to
  all arms -- and *"SD-105 has no freeze/share API today, so this is a substrate or driver-harness
  build, not a config change."*
- The design doc is stale in the same way: line 151 still names V3-EXQ-963b as the validation, and
  the doc contains no mention of freeze/share or of F1.

**epistemic_category (proposed):** **`substrate_conditional`** (change from the currently-registered
`standard`). Rationale against the CLAUDE.md discriminator: the mechanism is *coded* but has been
**exercised zero times** (no evidence rows, no queued run), and the only validation design put
forward has been shown to be structurally unable to discriminate; the upstream capability it now
depends on -- a converge-once / freeze / share-multiplier mode -- is *planned but not built*. That
is `substrate_conditional`, not `substrate_ceiling` (nothing downstream is absorbing SD-105's
signal; SD-105 is itself the thing that would absorb the *consumer's* signal). Governance may
reasonably prefer to leave `standard` and rely on the defer note; I flag the disagreement rather
than assume it.

**Note on what IS already discharged.** SD-105 splits cleanly into two legs and only one is in
doubt. The **arithmetic/design leg** -- one-sidedness (multiplier never < 1.0), the reporting cap
(`saturated` surfaced rather than hidden), tonic placement after MECH-313 and before the SD-069
phasic delta, and EMA/integrator survival across `reset()` -- is a proof obligation already
discharged by contracts B1-B10 in
`ree-v3/tests/contracts/test_sd104_sd105_burst_decay_and_entropy_headroom.py`. Only the **empirical
leg** (that the floor restores usable dynamic range *without distorting the contrast a consumer
reads*) is open, and F1 is a direct argument that as a live closed loop it does distort it.

**Draft `what_would_answer`** (written for the FROZEN-multiplier form, which is the only form that
can be validated; the live closed-loop form is what F1 rules out):

> **NON-DEGENERACY PRECONDITION.** (a) The controller must have something to do: the **un-armed**
> baseline realised normalized selection entropy on the warmed agent must sit **at or below the R5
> saturation floor** -- V3-EXQ-963a measured 0.0195-0.153 against V3-EXQ-779a's 0.152-0.610 on the
> same design -- because if the baseline already clears the band, an entropy floor is inert and the
> run measures nothing. (b) The multiplier must be **FROZEN AND SHARED**: converged once (e.g. on
> the T0P0 baseline during warmup) and then applied as a single constant to every arm in the read
> phase. A LIVE closed loop is disqualified by construction in any difference-of-arms design whose
> DV is realised selection entropy -- see the V3-EXQ-963b F1 verdict at
> `v3_exq_963b...py:556-580`; do not re-derive that argument, and do not accept "armed identically
> in all arms, so it cancels" (that reasoning was explicitly withdrawn by the session that wrote
> it). (c) `saturated` must be reported per arm and must be **False** -- a saturated controller has
> stopped integrating and the cell is uninformative by SD-105's own reporting contract. (d) The
> **committed-fraction must be pinned and reported per arm** (G3 preamble (iv)): SD-105 integrates
> `e3.last_precommit_probs`, which is written inside `select()`, so the entropy EMA is confounded
> with the commit duty cycle -- MECH-108's sweep is on by default and MECH-104/MECH-250 would move
> it further. (e) `use_noise_floor` (MECH-313) must be pinned in a known state, since it is the
> state-independent lift on the same channel.
>
> **CONFIRMING.** With a frozen, shared multiplier `m >= 1.0` applied uniformly: (i) **HEADROOM
> RESTORED** -- the T0P0 baseline entropy moves from below `E_SAT_LOW` (0.02) to inside the
> 0.02-0.98 band on >= 4 of 5 seeds, with `saturated = False` throughout; AND (ii) **CONTRAST
> PRESERVED, which is the load-bearing half** -- the tonic contrast `dS_tonic` measured under the
> frozen multiplier is statistically indistinguishable from the same contrast measured with the
> multiplier off, on a per-seed paired comparison (paired difference CI containing 0, and
> |mean paired difference| below 0.25 x the multiplier-off `|dS_tonic|`). Leg (ii) is exactly what
> the live closed loop fails and what a frozen multiplier is claimed to fix; a run reporting only
> (i) has certified its own subject (the R5-passes-by-construction defect F1 names).
>
> **FALSIFYING.** (i) holds and (ii) fails -- the frozen multiplier lifts every arm off the floor
> but still compresses `dS_tonic` beyond the band above. That would mean the compression is not an
> artifact of the *closed loop* but of *raising the temperature at all*, i.e. entropy headroom and
> contrast fidelity are not jointly achievable on this channel, and SD-105's central assertion
> (that the warmup branch of the autopsy's fork is the right one, and re-deriving R5's band is
> wrong) is refuted -- the autopsy's *second* branch would then be the only one left. Second
> falsifying pattern: (i) fails because reaching the target requires a multiplier beyond
> `selection_entropy_floor_max_temperature_ratio` (8.0), i.e. `saturated = True` -- the floor is
> unreachable on a warmed agent, and SD-105 is inert where it is needed most. Third: the frozen
> multiplier restores baseline entropy but the consumer's own criterion (MECH-063 (ii) C1) still
> cannot discriminate for the *independent* reasons F2/F5/F6 name (additive-in-temperature phasic
> delta shrinking against a lifted baseline; per-arm warm caches making `dS_phasic` a
> weights-difference; `R_transient` with no lever-off control) -- in which case SD-105 is vindicated
> and the *consumer's* design is the problem, and that must be recorded as such rather than charged
> back to SD-105.

**Proposal sketch (only for a/d):** n/a -- disposition is (f). What must be resolved first, verbatim
for the `digestion_note`:

> DEFERRED 2026-09-04 (thought-digestion G3). SD-105's registered validation V3-EXQ-963b was NOT
> queued: ree-v3 `d2104f8` records a BLOCKING Step-4.5 red-team verdict whose core finding (F1) is
> that SD-105, as a LIVE closed-loop set-point controller, sits on the exact DV the consumer's
> criterion reads and differentially compresses it -- verified against V3-EXQ-963a per-arm data
> (on seeds 23/29/37 it lifts the TONIC-OFF arms and holds the TONIC-ON arms). Both outcomes of the
> R6 guard are unproductive (R6 fails -> requeue; R6 passes -> SD-105 was inert) and R5 passes by
> construction. RESOLVE FIRST, in order: (1) build the converge-once / FREEZE / SHARE-multiplier
> mode named in that verdict's successor requirement (a) -- SD-105 has no such API today, so this is
> a substrate or driver-harness build, not a config change; (2) re-point
> `substrate_queue.sd_phasic_burst_decay_and_warmup_headroom.validation_experiment` and this claim's
> `functional_restatement` off V3-EXQ-963b onto the successor; (3) update
> `docs/architecture/sd_105_selection_entropy_headroom_floor.md` (line 151 still names 963b and the
> doc has no freeze/share section). Until (1) lands, SD-105 has no runnable validation and its
> `implemented_pending_validation` reading should not be read as "one run away".

**depends_on additions:** none required. `SD-074` and `MECH-313` are both correct and were verified
resolved before the build (substrate_queue `depends_on_resolved_note`, 2026-09-04). Consider adding
`MECH-108` to `related_claims` -- MECH-108's sweep is on by default and perturbs the commit duty
cycle that SD-105's entropy EMA integrates (G3 preamble (iv)); that coupling is currently recorded
nowhere.

**GOVERNANCE FLAG:** `contested_disposition` -- SD-105 was registered 2026-09-04 asserting the
autopsy's "warmup must leave headroom" branch and naming V3-EXQ-963b as its validation. On the same
day, ree-v3 `d2104f8` recorded a BLOCKING red-team verdict whose core finding (F1, "CONFIRMED / NOT
FIXED") is that SD-105 cannot be validated as a live closed loop in a difference-of-arms design whose
DV is the quantity it regulates, and requires a freeze/share API SD-105 does not have. Neither the
claim block, its `functional_restatement`, its `implementation_note`, nor its design doc records
this. The claim is not thereby wrong -- but "IMPLEMENTED ... validation is V3-EXQ-963b" currently
reads as one run from resolution when it is one substrate build plus a re-designed run away.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json`,
`sd_phasic_burst_decay_and_warmup_headroom.validation_experiment`, states V3-EXQ-963b was "queued by
campaign-c2c-20260904". It was not (ree-v3 `d2104f8`; the live queue snapshot `99817b6` holds only
V3-EXQ-1002 / 983a / 993a; `git log -S963b` on the queue file is empty). The entry sits at
`status_phase: validation_owed` with no owner for the owed validation.

---

<!-- G5 appended 2026-09-04T21:18:57Z -->
## G5 -- earned authority / shared epistemic state / rule_state closure  (agent report)

### Group preamble

- **Why these are together (restate, then my own view):** the brief grouped these on ARC-121
  `depends_on` SD-034 (6.00) and on ARC-120 <-> ARC-121 sharing an architectural namespace plus a
  claimed common source, the 2026-08-27 developmental-integration intake (4.25). **The second half of
  that rationale is wrong and should not be carried forward** (see Currency findings 1). The grouping
  nevertheless holds for a better reason that the similarity metric could not see: **all three are
  UMBRELLA/FRAMING claims sitting on top of already-built machinery, each of which has already had its
  sharp, testable content decomposed out into named children** -- ARC-120 -> ARC-130/ARC-131,
  SD-034 -> MECH-445/MECH-446, ARC-121 -> MECH-482/MECH-483. That shared shape, not the subject
  matter, is what makes them one digestion problem: the standing risk for all three is drafting a
  falsifier that silently re-tests a child's question, and the correct output for each is a falsifier
  fenced to the residual the children do NOT own.

- **(i) same-claim / merge candidates:** **No merge inside the group.** ARC-120 and ARC-121 are not
  two readings of one commitment: different `subject` namespaces
  (`architecture.competence_before_authority_framing` vs
  `architecture.epistemic_state_centrality_framing`), disjoint `depends_on` sets except MECH-094, and
  different falsification corpora (ARC-120's is the registry of accepted authority-granting
  mechanisms; ARC-121's is the set of belief/uncertainty containers in `ree_core/`). ARC-121 does NOT
  name a substrate ARC-120 presupposes -- ARC-120's authority gates are predicates over eligibility,
  mode and provenance, none of which requires a unified epistemic-state object; ARC-120 would survive
  intact in an architecture where every mechanism kept private belief state.
  **Merge pressure exists, but it points OUTSIDE the group in all three cases, and in all three cases
  the registry has already adjudicated it as non-supersession:** ARC-130 (`depends_on: ARC-120`,
  "base 5-stage sequence this refines/extends -- NOT superseded, ARC-120 remains sole owner of its own
  sequence"); ARC-128 (`depends_on: SD-034`, "DISTINCT FROM SD-034: SD-034 is a single IMPLEMENTED
  instance"); MECH-482/483 (`depends_on` of ARC-121, its local instances). **One PARTIAL absorption is
  worth proposing (g), and only one:** ARC-120's title carries a five-stage ladder
  ("existence -> representation -> competence -> authority -> behavioural influence") whose first four
  stages are reproduced verbatim inside ARC-130's longer, better-evidenced ladder
  ("existence, representation, endogenous recruitment, local operation, competitive authority,
  committed throughput, ecological consequence, retention/generalisation"), and ARC-130 has a
  2026-08-26 `evidence_quality_note` adjudicating its ladder CONFIRMED-SUPPORTS while ARC-120 has
  `exp_count 0`. Proposal: **narrow ARC-120's title to its ORDERING assertion** ("authority is earned
  through demonstrated competence, never granted merely because a computation exists") and have the
  ladder itself cross-reference ARC-130 rather than restate it. Absorbed text: the parenthetical
  stage list. Surviving id: ARC-120 (it is the `depends_on` target of both ARC-130 and ARC-131 and
  cannot be retired). Reverse-deps needing no repointing: ARC-130, ARC-131, ARC-135
  (`related_claims`), GOV-CAPCONTRACT-1 (`related_claims`). This is a narrowing, not a merge; I am
  proposing it, not applying it.

- **(ii) contradictions / undercut premises:** **Yes -- one sharp, and it is the group's best finding.**
  ARC-121 asserts that REE's mechanisms *increasingly converge* on a SHARED epistemic-state object,
  and it names **MECH-482 (`epistemic_deficit`) as its first dependency, i.e. as an instance of that
  convergence.** In `ree_core/` today, `epistemic_deficit` is referenced in exactly **4 files** --
  its own module `ree_core/policy/epistemic_deficit.py`, `ree_core/policy/__init__.py`,
  `ree_core/utils/config.py` (declaration only), and `ree_core/agent.py`, where it is wired as a
  **single-consumer source for one knob** (`curiosity_learning_progress_source == "epistemic_deficit"`,
  agent.py:1815-1920). Harm/ethics evaluation, replay, planning and the closure operator -- the exact
  consumers ARC-121's own title enumerates -- do not read it. Compare `hypothesis_tag` (MECH-094,
  ARC-121's fourth dependency): 24 files, 11 subpackages. **ARC-121's own dependency set therefore
  contains both its cleanest confirming instance and its cleanest counterexample**, and the
  counterexample is the more recently worked one (its substrate entry
  `sd_epistemic_deficit_multitarget_readiness` was added 2026-08-30 and is still
  `implemented_pending_validation`). This is not fatal -- one private container falsifies the
  convergence TREND, not the framing -- but it must be in the claim's falsifier text rather than
  discovered again by the next session.
  A second, weaker tension, worth recording because it is ARC-120's first live test case rather than a
  problem: SD-034's `functional_restatement` calls mode-conditioning a "critical falsifiability
  constraint," while the closure operator's newest firing route (`habenula_tick`, ARC-108 JOB-2,
  2026-06-22) deliberately does NOT gate on operating mode ("the abort does NOT gate on
  mode-conditioning -- a worse-than-expected outcome aborts content-wise regardless of operating
  mode", closure_operator.py:546-548). It is still gated on `hypothesis_tag is False` (MECH-094) and
  `beta_gate.is_elevated`, so **ARC-120 survives its most recent test case** -- but SD-034's
  mode-conditioning clause has an unrecorded carve-out.

- **(iii) shared falsifier:** Yes, one, and it runs from SD-034 to ARC-121, not the other way.
  ARC-121's confirming metric -- how many distinct `ree_core/` subpackages read a given epistemic
  container -- is measured on objects SD-034 and MECH-094 own (`rule_state`, `hypothesis_tag`).
  ARC-121's draft below therefore **quotes the census rather than re-deriving a separate notion of
  "shared"**, and any future revision of what counts as a shared epistemic object should be made once,
  in ARC-121, and cross-referenced by the others. In the other direction there is **no** shared
  falsifier between SD-034 and ARC-120: SD-034's residual question is an ablation (is closure
  necessary?), ARC-120's is a registry audit (is any accepted authority ungated?), and running one
  tells you nothing about the other.

- **(iv) cross-cutting finding:** **All three claims' residual falsifiers are ADJUDICATION or AUDIT
  obligations, not new experiments -- with exactly one exception, and identifying that exception is
  the point of this pass.** ARC-120's is a registry/design-review predicate plus a cross-tag of
  evidence that already exists (ARC-130's 2026-08-26 note names the runs and explicitly assigns them
  to ARC-120's rung); ARC-121's is a static code census, decidable today with no run at all; SD-034's
  retained core (five-part token firing, No-Go install, residue discharge) is already discharged by
  V3-EXQ-460d (`n_closures >= 1`, `nogo_installed >= 1`) and V3-EXQ-466e (PASS/supports). **The one
  genuinely un-run question in the group is SD-034's OWN primary falsifier -- the over-specification
  ablation ("can MECH-090/260/094 tuning alone produce the closure signature?") -- which no child owns
  and which has never been run in five months and thirteen SD-034-lineage experiments.** Every one of
  those thirteen tested whether closure has DE-COMMIT AUTHORITY; none tested whether closure is
  NECESSARY. The mutual-confound corollary: a null on MECH-445/446 (de-commit coupling/magnitude) is
  NOT a null on SD-034, and the registry already enforces this correctly -- all of 460h/460i/460j/460k
  /460l/715/717 are tagged to MECH-445/446 and none to SD-034. Do not let a future session read the
  460-lineage FAIL history as SD-034 evidence.

- **Currency findings (stale notes, landed blockers, unreviewed results):**
  1. **The grouping rationale's source attribution is wrong.** ARC-120 and ARC-121 were both registered
     **2026-08-06** with `source: docs/thoughts/2026-08-06_scientific_evolution_of_ree.md` (the
     historical-archaeology intake, Observations 4 and 3 respectively). The 2026-08-27
     developmental-integration intake
     (`evidence/planning/thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md`)
     merely **cross-references ARC-120** in its novelty table ("already owned") and lists it under
     `related_claims` for GOV-CAPCONTRACT-1 and ARC-135; **ARC-121 does not appear in that document at
     all** (grep: zero hits). Reading that doc for "their shared source" yields nothing about ARC-121.
  2. **ARC-120 has an unrecorded literature pull.** `evidence/literature/targeted_review_arc_120/`,
     5 entries dated **2026-09-02** (daw2005 uncertainty arbitration 0.74; lee2014 reliability
     arbitration 0.78; haruno2001 responsibility-gated control 0.72; luna2015 protracted control
     maturation 0.62; blumberg2013 twitch-bootstrapped authority, `mixed` 0.66). `lit_conf 0.852`,
     `overall_confidence 0.852`, `exp_conf 0.0`, quadrant `plausible_unproven`. The claim's `notes`
     still read as though no evidence pull had been attempted.
  3. **ARC-121's literature pull is still landing -- four entries are dated TODAY (2026-09-04).**
     9 entries total; `lit_conf 0.746`. **Two are `weakens`**: bach2012 (uncertainty encoded in
     distinct neural systems, 0.72 -- described in its own summary as "the clearest direct
     counter-evidence in the pull") and namburi2015 (dissociable BLA->NAc / BLA->CeM circuits with a
     causal double dissociation, 0.65). Seven support. Neither the pull nor its two weakens entries is
     reflected in ARC-121's block. Note the scope problem this creates -- see GOVERNANCE FLAG 5.
  4. **SD-034: V3-EXQ-466e is absent from claims.yaml.** `grep -c 466e claims.yaml` = 0.
     `v3_exq_466e_sd034_satisficing_residue_discharge_behavioural_20260625T030205Z_v3` ran
     **2026-06-25**, **status PASS**, `evidence_direction_per_claim: {SD-034: supports}`,
     `scoring_excluded: None` -- it is the **only genuine, non-excluded experimental entry SD-034 has**
     (`genuine_exp_count 1`, `pass_runs 1`, `fail_runs 0`, `exp_conf 0.616`, `overall 0.766`). It is
     already marked reviewed in `review_tracker.json`. Meanwhile SD-034's `live_status.evidence` still
     points at `failure_autopsy_V3-EXQ-466d_2026-06-24` (`non_contributory`) -- the SUPERSEDED
     predecessor -- with `as_of: 2026-07-11`. The block's most recent governance note is 2026-06-19.
  5. **The 460h re-queue named in SD-034's 2026-06-19 claim-synthesis note has long since run, and so
     have four successors.** 460h (2026-06-20), 460i (06-21), 460j (06-21), 460k (06-22), 460l
     (06-22), plus V3-EXQ-715 (07-06), 715a (07-06) and 717 (07-07). **Every one is tagged to
     MECH-445/MECH-446** (460l additionally MECH-090/342/ARC-108); **none to SD-034** -- the
     decomposition held exactly as designed. Outcomes: 460h/i/j/k/l all `non_contributory`;
     `substrate_queue.json` `f_dominance_conversion_ceiling` records
     "460h_460i_RAN_substrate_not_ready__readiness_still_unmet__PROMOTES_NOTHING"; 460k FAILed
     `closure_exclusive_eval_armed_hold 0/3`; V3-EXQ-717 is a `weakens` on MECH-445. All reviewed;
     `pending_review.md` shows **0 pending** as of 2026-09-04T18:57:45Z.
  6. **SD-034's `implementation_note` is stale in two ways.**
     `ree-v3/ree_core/governance/closure_operator.py` is now **816 LOC**, not the "616 LOC" recorded;
     and the note describes **two** completion entry points (automatic `tick()`, explicit
     `emit_closure`) while the code has **three** -- a **habenula negative-RPE abort**
     (`habenula_tick` / `ClosureOperatorConfig.habenula_abort_enabled` /
     `habenula_delta_threshold` / counter `_n_habenula_aborts`, exposed in `get_state()` as
     `n_habenula_aborts`) added by **ARC-108 JOB-2 on 2026-06-22**, which fires the SAME five-part
     `_fire`. `grep -c habenula_abort claims.yaml` = **0** -- this third caller of SD-034's operator is
     recorded nowhere in the registry.
  7. **SD-034's `pending_retest_after_substrate: true` is probably stale.** The retest it names is the
     non-cap-pinned de-commit DV, which was decomposed to MECH-445/446 on 2026-06-19 and has since had
     its own eight-run history. The umbrella inherited the flag from before the decomposition.
  8. **The 2026-06-13 `demote_to_candidate` deferral is still open and is now decidable.** Its own text
     says "re-evaluate the `conflict_ratio` post-rebuild before any provisional->candidate move."
     Post-rebuild (index generated 2026-09-04T14:48:23Z): `fail_runs 0`, `pass_runs 1`,
     `genuine_exp_count 1` -- every historical weakens is excluded as
     `stale_substrate` / `non_contributory` / `superseded`. The deferral should be formally closed as
     no-longer-applicable rather than left standing.
  9. **ARC-120 has zero experimental entries despite evidence at its rung existing and being named.**
     ARC-130's 2026-08-26 `evidence_quality_note` (chip-20260826-arc130-authority-throughput-evidence-tagging)
     explicitly withholds MECH-314/MECH-320 (`failure_autopsy_604a-624a-630_2026-06-03`) and MECH-341
     (V3-EXQ-614d) from itself on the ground that they "instantiate a DIFFERENT, EARLIER rung failure
     -- local operation without competitive authority ... which is the transition this claim's own
     notes explicitly assign to ARC-120," and says they were "left untagged on that basis, not
     overlooked." They were never tagged to ARC-120 either.
  10. **ARC-128 checked, as instructed: registered 2026-08-25, `depends_on: SD-034`,
      `epistemic_category: substrate_conditional`, `implementation_phase: v4`, DO-NOT-BUILD-in-V3, and
      NOT present in `claim_evidence.v1.json`. Its central factual assertion about SD-034 is
      CODE-CONFIRMED**: `ClosureEvent.reason` carries only
      `"auto-stable" | "explicit" | "skipped:<cause>"` (closure_operator.py:209), so SD-034 genuinely
      does not distinguish suspension from disengagement from interruption. ARC-128 is a legitimate
      V4 generalisation, not a duplicate, and no merge is indicated in either direction.
  11. **`substrate_queue.json` (177 entries) has NO entry for ARC-120, ARC-121, ARC-128 or MECH-511**
      -- consistent with ARC-120's own "introduces no new mechanism" and with ARC-128/MECH-511's
      explicit V4 parks. **MECH-511 checked as instructed**: it is `substrate_conditional` / v4 /
      "DO NOT build in V3 and DO NOT queue a V3 experiment", and it is a per-event *learning*
      eligibility gate, **not** a competence-gated *write-authority* build for ARC-120; the 2026-08-27
      intake lists it only as an `related_claims` neighbour. The two SD-034-relevant substrate entries
      are `commitment-closure-control-plane` (still `amend_implemented_pending_validation`) and
      `SD-034` itself (`implemented`).
  12. **Master switch is default-OFF and bit-identical OFF**: `use_closure_operator: bool = False`
      (config.py:5876), with `use_closure_env_completion_hook: False` and
      `closure_decommit_hold_ticks: 0`. `agent.py:2277-2284` enforces
      `use_closure_operator=True requires use_lateral_pfc_analog=True`. Per project memory
      `reference_claim_status_vs_default_off_flag`, SD-034's `provisional` status does not imply the
      knob is on in any production profile -- it is not.

---

### SD-034 -- Closure operator over committed rule_state: on satisfaction of a committed rule_state's...

**Recommended disposition:** **(a) testable now** -- the umbrella's OWN primary falsifier (is closure
emergent from MECH-090/260/094 tuning?) has never been run in thirteen lineage experiments, and it is
cheaply runnable today because the operator is BUILT, reaches `n_closures >= 1` on the 603n substrate,
has one PASSing non-degenerate DV (466e), and is bit-identical OFF -- so the ablation arm is free.

**Extracted from:** the claim's own `functional_restatement`, "Falsifiable (primary)" and
"Falsifiable (secondary)" clauses, verbatim in substance; the non-degeneracy gate is lifted from the
2026-06-12 amend's own retest gate ("n_closures>=1 reachable + nogo_installed>=1 on >=2/3 seeds");
the DV and its demonstrated non-vacuity come from V3-EXQ-466e. Nothing here is invented from a blank
page.

**Currency check:** `ree-v3/ree_core/governance/closure_operator.py` read (816 LOC; `use_closure_operator`
default False at `utils/config.py:5876`; three firing routes; `get_state()` exposes `n_ticks`,
`n_closures`, `n_habenula_aborts`, `stable_tick_count`, `active_pe_cap`, `last_event`);
`agent.py:2277-2284, 10189-10210` (lateral-PFC precondition, `notify_env_completion` hook);
`evidence/experiments/claim_evidence.v1.json` (2026-09-04T14:48:23Z: SD-034 exp=1 lit=9,
`exp_conf 0.616`, `pass_runs 1`, `fail_runs 0`, latest run 466e);
`v3_exq_466e_.../manifest.json` (PASS, `{SD-034: supports}`, 2026-06-25T03:02:05Z);
manifests for 460h/460i/460j/460k/460l/715/717 (all `evidence_direction_per_claim` on MECH-445/446,
none on SD-034); `review_tracker.json` (466e, 466d, 460h, 717 all reviewed); `pending_review.md`
(0 pending, 2026-09-04T18:57:45Z); `substrate_queue.json` (`SD-034` = `implemented`,
`commitment-closure-control-plane` = `amend_implemented_pending_validation`);
`docs/architecture/persistent_process_termination_taxonomy.md` sections 1-2a (ARC-128 comparison);
`closure_status.md` line 72 (`commitment_closure:GAP-4-battery`, in_progress, "466e RAN + PASSED");
`cross_plan_root_cause_synthesis_20260902.md` lines 122/138 (the 460 lineage's `substrate_not_ready`
self-routes share the observation->z_world->E1/E2 interface root; the GAP-4 battery's *b behavioural
cohort members will hit that gate, the non-behavioural members will not).

**epistemic_category (proposed):** `standard` -- **unchanged, and deliberately so.** SD-034 is
`design_decision`, its mechanism is BUILT and has been EXERCISED non-degenerately (466e), and the
residual question is a straight ablation on existing substrate. It is therefore neither
`substrate_conditional` (the code exists and has run) nor `substrate_ceiling` (the ON arm's DV is not
absorbed downstream -- 466e PASSed it). The `substrate_ceiling` reading applies to the DE-COMMIT
face, which is MECH-445/446's, not this umbrella's. No `live_status.reading` marker on SD-034
proposes either substrate category.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION -- two-sided, because this test has a tuned control arm that can be
> made vacuous as easily as the treatment arm. (ON side) `use_closure_operator=True` with
> `use_lateral_pfc_analog=True` (enforced, agent.py:2277), on the 603n foraging-competent substrate,
> and the closure path must demonstrably fire: `n_closures >= 1` AND `nogo_installed >= 1` on >= 2/3
> seeds -- this is the exact gate the 2026-06-12 amend pre-registered, and the exact defect
> V3-EXQ-460c hit (`n_closures = 0` despite env `sequence_completions` of 2/5/6). The residue-discharge
> DV must be non-flat, i.e. reproduce V3-EXQ-466e's demonstrated separation, not sit at floor.
> (OFF-tuned side) the control arm must be a real search and not a token one: at least 3 distinct
> settings each of the MECH-090 beta commit/release thresholds, the MECH-260 action-history depth, and
> the MECH-094 mode-gating predicate, with the BEST-performing member reported as the control, not the
> mean. If `n_closures = 0` in ON, or the tuned sweep collapses to a single point, the run self-routes
> `substrate_not_ready_requeue` and MUST NOT be scored in either direction. Report `n_ticks`,
> `n_closures`, `n_habenula_aborts` and the `skipped:<cause>` histogram from `ClosureOperator.get_state()`
> for every arm, so a null is attributable to a named skip cause rather than to "closure did nothing".
>
> CONFIRMING: three arms -- ON, OFF-baseline, OFF-tuned. SD-034 is supported if the ON arm reproduces
> the five-part token JOINTLY -- (a) MECH-090 beta release surviving `closure_decommit_hold_ticks`,
> (b) targeted MECH-260 No-Go on the just-completed action class, (c) within-domain residue attenuation
> with the 1e-6 floor asserted intact (the "residue cannot be erased" invariant), (d) a `closure_event`
> reaching SD-032a, (e) MECH-268 dACC pe rebaseline -- while the OFF-tuned arm reproduces at most ONE
> of the five; and if the ON-vs-OFF-tuned gap on the 466e residue-discharge DV exceeds
> max(1.5 x the pooled SD of the per-seed ON-minus-OFF-tuned delta, an absolute floor of 10% of the
> OFF-baseline within-domain residue mass) on >= 2/3 seeds. Scoring the five components SEPARATELY is
> load-bearing: a scalar composite would let a large residue effect mask the absence of the No-Go
> pulse, which is precisely the failure the 2026-06-12 amend was built to fix.
>
> FALSIFYING: the OFF-tuned arm reproduces >= 4 of the 5 components AND its residue-discharge DV lands
> within 1 SD of ON on >= 2/3 seeds. Then closure is emergent from the existing MECH-090/MECH-260/
> MECH-094 substrate and SD-034 is over-specification -- this is the claim's own primary falsifier,
> unchanged. SECONDARY (also the claim's own, and it routes elsewhere rather than weakening SD-034):
> if ON resolves verified-but-not-released but introduces PREMATURE disengagement -- beta released
> before the terminal step on a fraction of multi-step episodes exceeding OFF-baseline by more than
> the same margin -- then the SD-033a completion-condition detector or the mode-conditioning logic is
> wrong, not the operator; that outcome self-routes to the detector and MUST NOT be recorded as a
> weakens on SD-034.
>
> SCOPE FENCE (mandatory, and the reason this draft is fenced rather than broad): the closure->beta
> COUPLING face and the de-commit MAGNITUDE face are NOT in scope. They were decomposed out to
> MECH-445 and MECH-446 on 2026-06-19 (user-approved, spec
> `evidence/planning/claim_synthesis_SD-034-closure_2026-06-19.md`) and have since accumulated eight
> further runs of their own (460h/i/j/k/l, 715, 715a, 717). A null on either is NOT a null on SD-034,
> and no de-commit DV may be scored against this claim.

**Proposal sketch (a):**
- **title:** `V3-EXQ-466f -- SD-034 closure-operator NECESSITY ablation: three-arm ON / OFF-baseline /
  OFF-tuned(MECH-090 + MECH-260 + MECH-094 sweep) scored componentwise on the five-part done token`
- **related_claims:** SD-034 (primary, direction expected `supports` or `weakens`); MECH-090,
  MECH-260, MECH-094 (co-tagged -- the tuned arm is a direct test of THEIR sufficiency, so if
  OFF-tuned reproduces the signature they gain a `supports` while SD-034 takes the `weakens`);
  MECH-268, SD-032a (co-tagged, `non_contributory` expected -- they are components (d)/(e), not the
  question). **Explicitly NOT tagged:** MECH-445, MECH-446 (scope fence).
- **acceptance_checks:**
  1. ON arm gate: `n_closures >= 1` AND `nogo_installed >= 1` on >= 2/3 seeds, else
     `substrate_not_ready_requeue` and no scoring.
  2. OFF-tuned arm carries >= 3 settings per knob (9 configurations minimum); the best member is
     reported as the control and the full sweep is in the manifest.
  3. All five token components scored and reported separately; no scalar composite in the verdict.
  4. Residue floor invariant asserted: no field weight below 1e-6 in any arm.
  5. Bit-identical-OFF check: `use_closure_operator=False` reproduces OFF-baseline exactly (the
     existing contract in `test_sd034_decommit_hold_and_env_hook.py` covers the shape).
  6. `get_state()` telemetry (`n_ticks`, `n_closures`, `n_habenula_aborts`, `skipped:<cause>`
     histogram) emitted per arm per seed.
  7. `habenula_abort_enabled=False` in ALL arms -- the ARC-108 JOB-2 route is a third caller with
     different (deliberately un-mode-gated) semantics and would confound the necessity question.
  8. >= 3 seeds; per-seed deltas reported so the SD-scaled gate is computable rather than asserted.
- **Priority note:** per `cross_plan_root_cause_synthesis_20260902.md` line 138, GAP-4-battery's
  *behavioural* cohort members will hit the observation->z_world->E1/E2 interface gate; this ablation
  is a **non-behavioural** member of that battery (it scores the token's own components, not an
  ecological outcome), so it does NOT chain to that binding constraint and is runnable now. That
  distinction is the reason this is disposition (a) and not (c).

**depends_on additions (if any):** **ARC-108** -- if governance accepts the habenula abort as a
legitimate third caller of SD-034's `_fire`, it belongs in SD-034's dependency/cross-reference set;
today the coupling exists only in `ree-v3/CLAUDE.md` and in code. Recorded as a proposal, not applied.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- **V3-EXQ-466e (PASS, `{SD-034: supports}`,
2026-06-25T03:02:05Z, reviewed, `scoring_excluded: None`) is the ONLY genuine scoring experimental
entry SD-034 has and it appears nowhere in `claims.yaml`.** SD-034's `live_status.evidence` still
cites the superseded `failure_autopsy_V3-EXQ-466d_2026-06-24` (`non_contributory`) at
`as_of: 2026-07-11`, and the block's most recent governance note is 2026-06-19. The index already
reflects 466e (`exp_conf 0.616`, `overall 0.766`, `fail_runs 0`); the claim text does not. A session
reading only the block would conclude SD-034's evidence record is uniformly negative, which is the
opposite of the current state.

**GOVERNANCE FLAG:** `stale_note` -- SD-034's `implementation_note` records "616 LOC" and two
completion entry points; `closure_operator.py` is 816 LOC with **three** firing routes, the third being
the ARC-108 JOB-2 habenula negative-RPE abort (`habenula_tick`, `habenula_abort_enabled`,
`habenula_delta_threshold`, `_n_habenula_aborts`, added 2026-06-22, firing the same five-part `_fire`).
`grep -c habenula_abort claims.yaml` = 0. Additionally, that route **deliberately does not gate on
operating mode**, which is an unrecorded carve-out from SD-034's `functional_restatement`
mode-conditioning clause ("critical falsifiability constraint per SD-034 spec", also restated in the
module docstring). Either the clause needs a stated exception or the route needs a justification in
SD-034's block.

**GOVERNANCE FLAG:** `stale_note` -- two flags on this claim are now decidable and should be closed
rather than left standing: (i) `pending_retest_after_substrate: true`, whose named retest (the
non-cap-pinned de-commit DV) was decomposed to MECH-445/446 on 2026-06-19 and has since run eight
times under those ids; (ii) the 2026-06-13 `demote_to_candidate` recommendation, recorded as DEFERRED
pending a post-rebuild `conflict_ratio` re-evaluation -- post-rebuild is now available
(2026-09-04T14:48:23Z: `fail_runs 0`, `pass_runs 1`, all historical weakens excluded as
`stale_substrate`/`non_contributory`/`superseded`), so the deferral is resolved and the demotion is
not indicated.

---

### ARC-120 -- Behavioural/write authority in REE is (and should remain) EARNED through demonstrated...

**Recommended disposition:** **(b) derivational** -- its falsification condition is a standing
design-review predicate over the registry of ACCEPTED authority-granting mechanisms, discharged by
audit and by adjudicating evidence that already exists, never by a new experiment; the claim's own
notes say it "introduces no new mechanism" and is "falsified in the design sense." **Sequencing
condition on the category flip:** apply the evidence cross-tag flagged below FIRST and hold
`epistemic_category` at `standard` until it lands, because `derivational` suppresses promote/demote
and would freeze the one adjudication route ARC-120 has.

**Extracted from:** the claim's own `notes` -- "falsified in the design sense by any future accepted
mechanism that grants behavioural or write authority WITHOUT a competence-like gate" -- turned into a
decidable audit with a named corpus and a named non-degeneracy floor; plus ARC-130's 2026-08-26
`evidence_quality_note`, which supplies the confirming-side experimental instances by name and
explicitly assigns them to this claim's rung. The four gate TYPES in the CONFIRMING clause are
ARC-120's own `depends_on` set read as a taxonomy, not a fresh invention.

**Currency check:** live block re-read at `claims.yaml:81928-81971` (status `candidate`,
`epistemic_category: standard`, deps ARC-107 / SD-032b / MECH-261 / MECH-094 after the 2026-08-10 edge
correction that removed MECH-368 and INV-039); `claim_evidence.v1.json` (exp=0, lit=5,
`lit_conf 0.852`, `overall 0.852`, `pass_runs 0`, quadrant `plausible_unproven`, latest entry
`2026-09-02_arc_120_uncertainty_arbitration_daw2005`); `evidence/literature/targeted_review_arc_120/`
(5 entry dirs, all 2026-09-02, no SYNTHESIS.md yet); ARC-130 block (`claims.yaml:89891+`,
`depends_on: ARC-120`, "NOT superseded, ARC-120 remains sole owner of its own sequence", plus its
`evidence_quality_note`'s "CHECKED AND DELIBERATELY NOT TAGGED" paragraph); ARC-131 block
(`depends_on: ARC-120`, extends it "in the composition direction");
`thought_intake_2026-08-27_developmental_integration_and_readiness_programme.md` lines 65/68/82/190/234
(ARC-120 cited as already-owning the competence-to-authority bridge and the research-philosophy
principles; the capture's own recommendation is "test whether existing machinery suffices before
proposing a controller -- that is a workstream, not a claim"); `substrate_queue.json` -- **no ARC-120
entry, nothing to build**, consistent with the claim's own text; MECH-511 read in full and confirmed
NOT to be an earned-authority build (v4, `substrate_conditional`, explicit DO-NOT-BUILD-in-V3, and a
LEARNING-eligibility gate rather than a write-authority gate); `closure_operator.py:546-548, 559-586`
for the habenula test case below.

**epistemic_category (proposed):** `derivational` **once the cross-tag lands; `standard` until then.**
Rationale for not proposing `substrate_coherence` (the value `architectural_commitment` would
otherwise infer): `substrate_coherence` is for design choices that ARE the substrate, whereas ARC-120
is a *predicate over* substrate choices and is genuinely refutable by a single counterexample -- the
audit has a real fail state, which `substrate_coherence` would obscure. Rationale for not leaving it
`standard` permanently: `standard` demands `exp_conf` for promotion, and ARC-120 will never generate
its own experiment; leaving it there guarantees perpetual `lit_only` / `low_exp` flags. Note this is
the OPPOSITE recommendation to ARC-130, which correctly stays `standard` because its distinctive
post-authority clause does have its own runnable content.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: this is an audit, and an audit over an empty or trivial corpus is the
> characteristic vacuity here. The corpus is every mechanism that ACTUALLY GRANTS AUTHORITY -- i.e.
> whose effect is to admit a signal to a committed-selection surface, a memory/representation write
> path, or a consolidation-rate control -- that was ACCEPTED (registered `active`/`stable`/
> `provisional`, code present in `ree_core/`, reachable on a production path, not default-off-and-
> never-enabled) since ARC-120's registration on 2026-08-06. **At least 5 such mechanisms must be in
> the corpus**; with 0-2 the correct output is "insufficient corpus", never "confirmed". Each must be
> classified gated/ungated by READING ITS ADMISSION PREDICATE IN CODE, not by reading its claim prose
> -- a claim whose text promises a gate that the code does not implement counts as UNGATED, and that
> asymmetry is the whole point of running the audit against `ree_core/` rather than against
> `claims.yaml`.
>
> CONFIRMING: every mechanism in the corpus conditions its authority grant on at least one
> competence-like predicate -- per-event eligibility (ARC-107), a learnable rather than fixed store
> (SD-032b), operating-mode write gating (MECH-261), real-vs-simulated provenance tagging (MECH-094),
> or a demonstrable equivalent. WORKED CONFIRMING INSTANCE, already in the record and usable as the
> audit's first row: the ARC-108 JOB-2 habenula de-commit (`ClosureOperator.habenula_tick`, ree-v3,
> 2026-06-22) grants a genuinely NEW behavioural authority -- abort a live commitment on a
> worse-than-expected outcome -- and gates it on `hypothesis_tag is False` (MECH-094, so a replay/DMN
> outcome cannot abort a waking commitment) AND `beta_gate.is_elevated` (nothing to de-commit
> otherwise). That is a competence-like gate, so **ARC-120 survives its most recent test case**, and
> it survives it in the informative direction: the gate was added for a reason internal to the
> mechanism, not to satisfy this claim. On the experimental side, ARC-120's rung is discharged by the
> authority-ABSENT findings ARC-130's 2026-08-26 note explicitly assigns to it -- MECH-314/MECH-320
> score-bias terms "dominated by the primary harm/goal score term, so they never change argmax"
> (`failure_autopsy_604a-624a-630_2026-06-03`), and MECH-341 firing "but leaving committed-class
> entropy invariant" (V3-EXQ-614d). These are instances of authority correctly NOT granted to a
> mechanism that had not earned it.
>
> FALSIFYING: one accepted, production-reachable mechanism whose authority-admission predicate reads
> ONLY on signal presence or magnitude -- no eligibility, mode, learnability or provenance condition --
> and whose acceptance was not flagged as a deliberate exception. One clean instance falsifies the
> normative half ("should remain"); a second instance PLUS a governance decision declining to add a
> gate falsifies the descriptive half ("is"). NEAR-MISS SHAPE TO REJECT, so the audit does not
> manufacture a false positive: an ungated INTERNAL scalar that cannot reach a committed surface is
> NOT a counterexample here -- it fails at competitive authority or committed throughput, which are
> ARC-130's rungs, not this claim's. The discriminator is whether the ungated signal demonstrably
> reaches a committed action, a durable write, or a consolidation rate.
>
> PROOF/AUDIT OBLIGATION (the artifact this claim resolves into, in place of an experiment): a dated
> table of the post-2026-08-06 authority-granting mechanisms, each with its admission predicate quoted
> from `ree_core/` and classified against the four gate types above, re-run at each governance cycle
> that accepts a new authority-granting mechanism. ARC-120 closes as resolved-by-derivation when that
> table has been maintained across a meaningful corpus with no ungated row; it is refuted the first
> time a row is ungated and stays ungated by decision.

**Proposal sketch (only for a/d):** not applicable -- this is (b). The deliverable is the audit table
above, not a queue entry. Explicitly do NOT queue an experiment for ARC-120: the claim's own text says
it "introduces no new mechanism" and has "nothing to build," and `substrate_queue.json` correctly
holds no entry for it.

**depends_on additions (if any):** none. **ARC-130 and ARC-131 already depend on ARC-120** (not the
reverse) and that direction is correct and should not be inverted -- ARC-120 is the base sequence, and
both extenders explicitly refuse to supersede it. See the (i) preamble for the narrowing proposal
(absorb the ladder parenthetical into ARC-130's, keep the ordering assertion here).

**GOVERNANCE FLAG:** `promotion_review` -- **ARC-120 carries `exp_count 0` while pre-existing,
CONFIRMED evidence at its own rung sits untagged, by an explicit decision recorded in a sibling
claim.** ARC-130's 2026-08-26 `evidence_quality_note` (chip-20260826-arc130-authority-throughput-
evidence-tagging) withholds `failure_autopsy_604a-624a-630_2026-06-03` (MECH-314/320) and V3-EXQ-614d
(MECH-341) from ARC-130 on the ground that they instantiate "local operation without competitive
authority ... the transition this claim's own notes explicitly assign to ARC-120," and says they were
"left untagged on that basis, not overlooked" -- but no corresponding tag to ARC-120 was ever made.
Recommend a cross-tag pass mirroring chip-20260826 exactly (set `diagnostic_evidence_adjudicated: true`
on ARC-120 with an `evidence_quality_note` naming those runs), since both are `claim_ids: []`
diagnostic-purpose findings that will otherwise never reach the index. This is adjudication of
existing evidence, not promotion.

**GOVERNANCE FLAG:** `stale_note` -- ARC-120 acquired a 5-entry literature pull on **2026-09-02**
(`evidence/literature/targeted_review_arc_120/`, `lit_conf 0.852`, one `mixed`: blumberg2013
twitch-bootstrapped authority) with no SYNTHESIS.md and no reflection in the claim's `notes`, which
still read as though the claim had never been evidenced. Per project memory `feedback_lit_exp_decoupled`
the literature is not co-equal with experiment, so this must not by itself move status -- but the pull
should be summarised into the block, and blumberg2013 in particular (authority bootstrapped from
pre-competence spontaneous twitching) is the nearest thing in the record to a biological counterexample
to a strict competence-before-authority ordering and deserves an explicit disposition rather than
silence.

---

### ARC-121 -- REE's mechanisms increasingly converge on maintaining and consuming a SHARED epistemic...

**Recommended disposition:** **(b) derivational** -- ARC-121's own stated falsifier is about REE's
substrate-development trajectory, which is decidable TODAY by a static census of `ree_core/` with no
experiment and no substrate work; and running that census already surfaces a live counterexample
inside the claim's own dependency set, which is a stronger and cheaper result than any experiment
would have produced.

**Extracted from:** the claim's own `notes` -- "Falsified in the design sense if REE's future substrate
development keeps adding local, mechanism-private belief/uncertainty representations rather than
converging toward anything approximating one shared epistemic-state object" -- operationalised into a
counting rule with a stated exclusion list, plus the measured baseline below. The "shared" predicate is
NOT re-derived here: it is defined once, in this claim, on the objects SD-034 and MECH-094 own, and the
group's other drafts point at it rather than restating it (preamble (iii)).

**Currency check:** live block re-read at `claims.yaml:81972-82013`; `claim_evidence.v1.json`
(exp=0, lit=9, `lit_conf 0.746`, `pass_runs 0`, quadrant `plausible_unproven`, latest entry
`2026-09-04_arc_121_vmpfc_lesion_moral_judgment_koenigs2007` at 14:28Z **today**);
`evidence/literature/targeted_review_arc_121/` -- 9 entry dirs, 5 dated 2026-09-02 and 4 dated
2026-09-04, including two `weakens` whose summaries I read in full (bach2012, namburi2015).
**Code census run against `/Users/dgolden/REE_Working/ree-v3/ree_core/`:** `hypothesis_tag` -> 24
files across `amygdala/`, `pfc/`, `sleep/`, `hippocampal/`, `residue/`, `predictors/`, `governance/`,
`latent/`, `cingulate/`, `regulators/`, `policy/` (11 subpackages); `rule_state` -> 10 files across
`pfc/`, `predictors/`, `cingulate/`, `regulators/`, `policy/`, `governance/`, `environment/`
(7 subpackages); `epistemic_deficit` -> **4 files** (`policy/epistemic_deficit.py`,
`policy/__init__.py`, `utils/config.py`, `agent.py`), with `agent.py:1815-1920` wiring it solely as
`curiosity_learning_progress_source == "epistemic_deficit"`. `E2WorldUncertaintyHead`
(`predictors/e2_world_uncertainty.py`) and `EpistemicDeficitAccumulator` are the only two
uncertainty/belief container classes in the tree by class-name search. Dependency blocks read:
MECH-482 (`substrate_conditional`, `candidate`, `pending_retest_after_substrate: true`, 2026-08-30
autopsy of V3-EXQ-964 found C2 "STRUCTURALLY UNSATISFIABLE" because `reset()` clears all persistent
targets every episode); MECH-483 (`substrate_conditional`, already carries a
`what_would_answer` -- used as the house-structure exemplar for this pass; no `orient_survey` /
`survey_regime` symbol exists in `ree_core/`, so it is genuinely unbuilt); SD-034 (see above);
MECH-094 (the shared object, 24 files). `substrate_queue.json`: no ARC-121 entry;
`sd_epistemic_deficit_multitarget_readiness` added 2026-08-30T07:25Z,
`implemented_pending_validation`. **ARC-121 is not mentioned anywhere in the 2026-08-27 intake.**

**epistemic_category (proposed):** `derivational`. The question is settled by working through the
architecture as built, not by experiment, and there is no substrate to wait for -- so neither
`substrate_conditional` (MECH-482 IS built and exercised; MECH-483 is not, but ARC-121 does not depend
on MECH-483 being built to be assessable) nor `substrate_ceiling` (nothing downstream is absorbing a
signal; the claim is about code topology). `derivational` also correctly suppresses `narrow_open_question`,
which would be meaningless for a convergence-trend framing.

**Draft `what_would_answer`:**

> NON-DEGENERACY PRECONDITION: the census must run over epistemic CONTAINERS -- a class or persistent
> agent attribute that holds belief / uncertainty / possibility / commitment state and is instantiated
> on a production path in `ree_core/` -- not over every module that mentions a keyword. The sharing
> measure for a container is the number of DISTINCT top-level `ree_core/` subpackages that READ it,
> excluding (i) its own defining module, (ii) that package's `__init__.py`, and (iii)
> `ree_core/utils/config.py`, which carries declarations only and would otherwise make every container
> look one-subpackage-shared. A census in which every container scores identically -- all shared or all
> private -- is uninformative about CONVERGENCE (which is a claim about a trend, not a state) and must
> be reported as uninformative rather than as a verdict; convergence requires at least two containers
> at different sharing levels and a defensible ordering by date of addition.
>
> CONFIRMING: newly added epistemic containers are read across >= 3 distinct subpackages -- they JOIN
> the existing shared objects rather than adding private ones -- and the shared:private ratio is
> non-decreasing across successive substrate additions. MEASURED BASELINE, ree-v3 `ree_core/` as of
> 2026-09-04, which any future census should be diffed against rather than re-derived:
> `hypothesis_tag` (MECH-094) = 24 files / 11 subpackages, spanning amygdala, PFC, sleep, hippocampal,
> residue, predictors, governance, latent, cingulate, regulators and policy -- strongly shared, and
> exactly the cross-mechanism consumption pattern ARC-121's title asserts (prediction, replay,
> harm/ethics evaluation, planning and learning all read it); `rule_state` (SD-033a / SD-034) = 10
> files / 7 subpackages -- shared, and read by both the closure operator and E3 selection, i.e.
> commitment really is a first-class object several mechanisms consume rather than one module's local
> variable. Those two are the claim's genuine confirming core and they are strong.
>
> FALSIFYING: newly added epistemic containers are confined to their own defining module plus the
> agent constructor -- private, single-consumer, with no cross-mechanism read path. **THIS PATTERN IS
> ALREADY PRESENT, and the instance sits inside ARC-121's OWN `depends_on` set.** `epistemic_deficit`
> (MECH-482, `ree_core/policy/epistemic_deficit.py`, substrate entry SD-102) is referenced in exactly
> 4 files -- its own module, `policy/__init__.py`, `utils/config.py` (declaration), and `agent.py`,
> where it is instantiated only when `curiosity_learning_progress_source == "epistemic_deficit"` and
> consumed as a single-purpose curiosity/learning-progress source (agent.py:1815-1920). It is NOT read
> by harm/ethics evaluation, replay, planning, or the closure operator -- the precise consumers
> ARC-121's title enumerates -- and its substrate was still being actively extended on 2026-08-30
> (`sd_epistemic_deficit_multitarget_readiness`, `implemented_pending_validation`) without acquiring a
> shared read path. So REE's most actively-developed belief/uncertainty addition is mechanism-private,
> which is the falsifying pattern the claim itself specifies. CALIBRATION, so this is not over-read:
> ONE private container falsifies the convergence TREND, not the framing -- the correct response is to
> amend ARC-121 from "increasingly converge" to "converge on some, not all, epistemic constituents",
> or to route `epistemic_deficit` into a shared read path and re-census. ARC-121 is falsified OUTRIGHT
> only if a SECOND post-registration epistemic container is added with no shared read path and no
> accepted plan to give it one -- at that point private-by-default is the architecture's actual
> practice and the framing is describing an aspiration rather than a trend.

**Proposal sketch (only for a/d):** not applicable -- (b). Deliverable is the dated census table
(container, defining module, reading subpackages, date added, shared/private), regenerable in one
`grep` pass, with the 2026-09-04 baseline above as row zero. Do NOT queue an experiment: the claim's
own notes already say it is "not directly falsifiable by a single experiment," and the reason is not
that it is hard to test but that it is not an experimental question at all.

**depends_on additions (if any):** none to ARC-121 itself. **Proposed cross-reference in the OTHER
direction (propose only):** MECH-482's block should record that its single-consumer wiring is
ARC-121's live counterexample, so that the next session extending SD-102 knows a second REE-level
claim is watching that wiring. Deliberately NOT proposing that ARC-121 depend on MECH-511, MECH-512 or
Q-079 -- the claim's own notes already fence Q-079's DLIF and SD-062's claims-index graph as "adjacent
and orthogonal, not merged," and that fence is correct and should be preserved.

**GOVERNANCE FLAG:** `contested_disposition` -- **ARC-121 is a FUSED claim and its literature pull is
scoring the wrong leg.** Its title and its stated falsifier are both about **REE's own architecture**
("REE's mechanisms increasingly converge...", falsified by "REE's future substrate development"),
which is a code-auditable, derivational question. The 9-entry pull (2026-09-02 and 2026-09-04, latest
14:28Z today) instead adjudicates a **biological-plausibility** leg -- whether the BRAIN uses one
shared epistemic-state object -- and produces two `weakens` on that basis: bach2012 (uncertainty
encoded in distinct neural systems; its own summary calls it "the clearest direct counter-evidence in
the pull") and namburi2015 (causal double dissociation between BLA->NAc and BLA->CeM valence circuits).
Both summaries are careful and explicitly flag the gap -- namburi2015's own limitations section notes
the dissociation is at an INPUT stage upstream of the vmPFC "common currency" hub the supporting
entries address, and bach2012's notes that "anatomically distinct encodings do not entail functionally
private state." So the entries are sound; the ROUTING is not. Recommend: (i) split the biological leg
out explicitly (either a `related_claims` pointer to the valuation/common-currency literature question
or a narrow sibling registration), (ii) re-scope the existing 9 entries as bearing on that leg, and
(iii) score ARC-121 itself on the code census. Left as-is, ARC-121 will accumulate biology `weakens`
against a claim about a Python package -- and per project memory `feedback_lit_exp_decoupled`, that
literature must not be treated as load-bearing for a REE-architecture assertion in any case.

**GOVERNANCE FLAG:** `evidence_discrepancy` -- ARC-121 declares MECH-482 as a dependency and as an
instance of epistemic-state convergence, while the code shows `epistemic_deficit` is a 4-file,
single-consumer, mechanism-private container with no read path from harm evaluation, replay, planning
or closure. The claim's premise and its own dependency's implementation disagree. Not urgent and not a
demotion trigger (both are `candidate`), but it should be recorded on both blocks rather than
rediscovered: it is the concrete content of ARC-121's falsifier, and MECH-482's next substrate pass is
where it would cheaply be fixed.

---

### Cross-group note for the orchestrator (not a claim disposition)

The campaign brief attributed ARC-120 and ARC-121 to the **2026-08-27 developmental-integration
intake**. Both were registered **2026-08-06** from
`docs/thoughts/2026-08-06_scientific_evolution_of_ree.md` (Observations 4 and 3). The 2026-08-27
document cross-references ARC-120 four times as "already owned" and **never mentions ARC-121**. If any
other group's brief, or any tracked review file, carries the same attribution, it should be corrected
there too -- **`stale_note`**.

---

<!-- G6 appended 2026-09-04T21:18:57Z -->
## G6 -- committed-action diversity through selection  (agent report)

### Group preamble

- **Why these are together (restated, then my view).** The task framing was: MECH-442 `depends_on`
  both MECH-341 and MECH-294; 442 asserts diversity SURVIVES the commit, 341 asserts E3 scoring
  PRESERVES class diversity upstream, and 294 was assumed to "supply the per-cycle binding that makes
  *class* well-defined". **Two of those three premises do not survive contact with the substrate,**
  and the corrections are the main product of this pass:

  1. **MECH-294 does NOT define "class".** "Trajectory class" is defined in exactly one place --
     `ree-v3/ree_core/predictors/e3_score_diversity.py::E3ScoreDiversity._first_action_classes`
     (line 143): `int(first_step.argmax().item())`, i.e. the argmax of the candidate's *first action
     step*, over `action_dim == 5`. It has no dependence on theta-packet binding whatsoever.
     MECH-294's contribution to this pipeline is a **modulatory channel source**
     (`modulatory_channel_route_source="coherence"`, per-candidate co-binding coherence with a
     cross-candidate RANGE), which feeds the same selection authority MECH-442 would restrict. So
     294 relates to 442 as *one candidate content-source for the within-eligible-set bias*, not as
     the class-definer. MECH-442's `depends_on: MECH-294` comment ("selection-authority/binding
     substrate the archive must route around F with") is right about the *channel* and wrong if read
     as depending on 294's joint-binding **content** clause -- see the `depends_on` note under
     MECH-442.
  2. **MECH-442's mechanism is already largely BUILT, under MECH-341.** MECH-341 Option 2,
     `E3ScoreDiversity.stratified_select` (e3_score_diversity.py:240-330), is, verbatim from its own
     docstring: *partition candidates by first-action class -> per class pick the argmin-score
     candidate as class representative -> sample across class representatives with
     `softmax(-best_in_class_score / T)`*. That is a behavioural-descriptor partition, a **per-niche
     F-best elite**, and a **coverage-aware commit rule** -- MECH-442's stated mechanism, with the
     descriptor pinned to first-action class. It runs on BOTH the committed and uncommitted selection
     paths since the 2026-05-28 retune, and it carries the unit-range authority normalisation
     (2026-06-03). MECH-442's `notes` never mention this module; they cite only `e3_selector.select`
     top-k / modulatory-authority. **MECH-442's "not yet built" premise is materially stale.**

- **(i) same-claim / merge candidates.** **MECH-341 and MECH-442 are NOT the same claim** -- they are
  separated by an explicit, ratified scope boundary and by different readouts:
  MECH-341's 2026-06-14 ratification carries the EXPLICIT CAVEAT that it asserts scoring-layer
  **preservation** and *"does NOT assert that the preserved diversity reaches the COMMITTED action"*;
  MECH-442's DV is exactly committed-action-class entropy. So they are complementary layers, and the
  brief's second horn is the right one: **442 is the downstream test whose non-degeneracy
  precondition is 341 holding.**
  BUT there is real, **partial** merge pressure pointing at MECH-341's already-built
  `stratified_select` (in-group) and at MECH-448's built `f_demotion` eligibility envelope
  (out-of-group, `e3_selector.py:3757-3765`, which takes precedence over `top_k`). Between them they
  already instantiate: descriptor partition + per-niche elite + coverage-aware commit
  (`stratified_select`), and eligible-set restriction upstream of the argmax with F removed from the
  final arbitration (`f_demotion` / `top_k`). **Proposed PARTIAL absorption with a narrowed
  residual** (details in the MECH-442 entry): MECH-442's surviving, genuinely-unbuilt residual is
  only *(a)* descriptors OTHER than first-action class (committed-action class,
  `e2.world_forward` strategy signature) and *(b)* placing the niche partition at the **eligible-set
  restriction** stage of `select()` (composed with `f_demotion`/`top_k`) rather than at the
  score-composition stage. No full merge; no id retired.
  MECH-294 is not a merge candidate with either.

- **(ii) contradictions / undercut premises.** One live undercut, and it runs 294 -> 442.
  MECH-442's dependency on MECH-294 is stated as needing the binding substrate "to route around F
  with". V3-EXQ-840b (2026-08-01) returned `weakens` on 294's joint clause. If that weakens stands,
  it does **not** undercut 442 -- what 442 needs is the *routing channel* (which demonstrably works:
  `route_range_per_arm_mean` JOINT 0.069 / ALT 0.057 / OFF+SHUF 0.0, `route_active_frac` 1.0), not
  the joint-vs-alternation content claim. So the dependency should be read/annotated as channel-only.
  No contradiction between 341 and 442; no contradiction between 341 and 294.
  Second, weaker tension: MECH-442's own load-bearing lit weakens (Ponzi 2007, `weakens`, conf 0.66)
  says the BG gate is a WTA that collapses to one action -- 442 already accommodates this by placing
  the archive upstream of the argmax, so this is a scoping constraint rather than a contradiction,
  and it is the same constraint `f_demotion`/`top_k` already satisfy.

- **(iii) shared falsifier.** **YES, and it already exists and must NOT be re-derived: ARC-065's
  `what_would_answer` "ARMED-CONVERSION" non-degeneracy precondition** (live in claims.yaml; already
  written to be cross-referenced by MECH-440/441, MECH-442's cluster siblings). Restated only for
  navigation, not for copying:
  - **(P1)** `support_preserving_min_first_action_classes = action_dim` (5), asserted from the
    MEASURED `mean_distinct_first_action_classes >= 0.9 * action_dim` (>= 4.5) **in every arm**. At
    the shipped default of 2 the pool realises ~2-3 classes of 5, so committed-class entropy is
    capped **identically in every arm** -- an arm-invariant ceiling no diversity lever can move.
  - **(P2)** `use_modulatory_selection_authority = True` with measured
    `authority_rel_deviation_mean > 0.05` in every arm carrying a modulatory lever.
  - Third leg: ARC-062 gated-policy heads + learned context discriminator ON in every arm.
  - Evidence that both are load-bearing and neither substitutes: V3-EXQ-949 (2026-08-25, 5 seeds)
    measured yoked committed-action divergence **0.000 with P1 alone, 0.000 with P2 alone, 0.3675
    with both**, at a measured pool diversity of 4.856 vs the 4.5 floor.
  - ARC-065's text is explicit: **"A null with either clamp in place is VACUOUS and must self-route
    `substrate_not_ready_requeue`, never `weakens`."**

  All three G6 claims read out on the *same statistic family* -- a distribution over first-action /
  committed-action classes at the E3 commit (entropy, or TV between arms) -- so this one precondition
  block is the correct shared text for all three, and each entry below points at it rather than
  restating it.

  **Second shared item (the pseudo-replication answer the brief asked for).** The de-duplication the
  memory `reference-hold-weighted-e3-readout-form2` warns about is already solved by a shared helper:
  `ree-v3/experiments/_lib/fresh_select.py` (`FreshSelectProbe` / `FreshSelectCounter`). It clears the
  E3 select diagnostics before every `select_action`, so a **latched (held) tick contributes NO row**,
  and emits `n_fresh_select` / `n_latched` / `fresh_select_yield` / `replication_factor` per cell.
  The established denominator floor is `nominal window ticks / beta_rate_max_steps=20` (the MECH-093
  worst-case cadence) -- V3-EXQ-840b used floor 180, measured 400. **Any falsifier in this group must
  state its candidate/selection counts on the fresh-select denominator and record
  `replication_factor`;** the raw per-tick count is ~9x pseudo-replicated (840b's own precondition
  text says so).

- **(iv) cross-cutting finding (the mutual confound).** **Every negative result currently on file for
  this group was measured under P1 at its default of 2 -- so a null on any one of them is
  uninterpretable until P1 is lifted.** Concretely: V3-EXQ-840b (MECH-294's only genuine experimental
  entry, and the sole basis for `exp_conf 0.249` and the `substrate_ceiling -> standard` category
  graduation) ran with `support_preserving_min_first_action_classes=2` (driver line 485) and measured
  `worst_diversity_joint = 2.0022` against its own local floor of 1.0 -- i.e. **2.0 of 5 classes**,
  versus ARC-065's ratified 4.5. MECH-341's three supporting runs (569d / 614a / 660) were all
  measured under the same clamp, which additionally means `stratified_select` was operating at its
  bare minimum (`min_classes_for_stratification = 2` against a pool realising exactly ~2 classes) --
  a preservation claim tested where there is almost nothing to preserve. And MECH-442, if built and
  tested today, would inherit the identical ceiling.
  Second cross-cutting item: **SD-105** (selection-entropy headroom floor, registered 2026-09-04,
  being digested elsewhere -- NOT digested here) is a **direct confound for any test in this group**:
  it is a one-sided integral controller that raises the E3 selection softmax temperature until
  realised normalised selection entropy sits at a floor. That *manufactures* the DV all three claims
  read out on. Any MECH-341/294/442 falisifier must either run SD-105 OFF, or hold it as a matched
  constant across arms **and record the controller's realised log-temperature per arm**; a
  floor-pinned readout also compresses the headroom an archive lift would have to move into (SD-105's
  own text makes exactly this argument about the R5 headroom gate).

- **Currency findings (verified this pass).**
  1. **`substrate_queue.json` -> `sd_id: MECH-341`** still reads
     `status: amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true`. That string
     predates 614e, 660, 660a/660b and the 2026-06-14 ratification. **Stale.**
     (`closure_status.md` line 59 is *correct* and current: `behavioral_diversity_isolation:GAP-B`
     -- "MECH-341 STRAND CLOSED 2026-06-14 (ratified provisional, commit 80f4fcf250)".)
  2. **`substrate_queue.json` -> `sd_id: mech294_coherence_magnitude_strengthening`** is still
     `ready: false` with a status string describing the **V3-EXQ-840** diagnosis. Its own
     `diagnosis_correction` (2026-07-31) concluded *"No ree_core substrate change is warranted...
     there is nothing to strengthen"*, and V3-EXQ-840b then ran and resolved the line on 2026-08-01.
     The entry has never been closed out, and its `recommended_next_step` (reconcile the confirmed
     autopsy artifact `failure_autopsy_batch-687a-...-2026-07-30.json`, whose "sub-floor
     cross-candidate range" claim does not match 840's own `per_arm_gate` data) appears unactioned.
     **Stale + an open reconcile.**
  3. **MECH-341 `status_note` cites `exp_conf 0.871 > 0.62` at the 2026-06-14 ratification.** The
     live index (`claim_evidence.v1.json`, generated 2026-09-04T14:48Z) now reads
     **`experimental_confidence 0.683`**, 3 supports : 0 weakens, `evidence_quadrant
     confirmed_established`, latest run V3-EXQ-660 (2026-06-10). Still clears the 0.62 gate, so the
     ratification stands, but the quoted figure is stale by ~0.19.
  4. **MECH-442's "not yet built" premise is stale** -- see preamble (2) and the MECH-442 entry.
  5. **The conversion-ceiling campaign has moved off the selection face.**
     `conversion_ceiling_campaign_plan.md` (7 nodes, 0% closed, all `assembling`): `:P-comp` RAN
     non_contributory; `:P2-rootC` RAN TERMINAL (715/715a/717 all FAIL, "selection-face lift RULED
     OUT, delta -63"); `:P4-learned-gating` **EXHAUSTED / retired**; `:FULLSTACK` RAN TERMINAL
     (V3-EXQ-714 readiness abort); `:CAMPAIGN` "converged on competence gate"
     (724 -> 732 -> 732a -> 737/738); `:GENERATION` (the missing 6th face, MECH-458) **blocked on
     upstream INV-088 z_world differentiation**. MECH-442 is **not** a face in that plan. This is
     directly consistent with [memory] `project_v3_binding_constraint_observation_interface`.
  6. **`claims.json` shows MECH-294 `awaiting: modulatory-bias-selection-authority`** -- that
     substrate is `implemented / ready: true` in `substrate_queue.json` and was consumed by 840b.
     Minor derived-field staleness; low priority.

---

### MECH-294 -- Theta-burst packet contains multi-content joint binding: each ~125 ms theta cycle binds a {goal_latent, action_proposal, risk_estimate, state_summary} tuple

**Recommended disposition:** **(a) testable now** -- the V3 leg has a validated driver and a landed
substrate lift (P1 raised to `action_dim`, proven necessary by V3-EXQ-947/949) that makes a
*non-vacuous* re-measurement of the exact 840b criteria buildable today; the current `weakens` was
measured under the clamp ARC-065's ratified precondition declares vacuous.

**Extracted from:** the claim's own `functional_restatement` "Falsifiable (primary)" / "Falsifiable
(secondary)" clauses, plus V3-EXQ-840b's pre-registered outcome map
(`evidence_direction_note`) and its `interpretation.preconditions` block -- turned into house
structure, not designed fresh. The non-degeneracy half is cross-referenced to ARC-065, not
re-derived.

**Currency check (what was verified, and where).**
- `ceiling_routing_note`'s "RESOLVED 2026-08-01 ... clean weakens, all readiness green" is
  **accurate as far as it goes**: `v3_exq_840b_..._20260801T120516Z_v3.json` shows
  `non_degenerate: true`, all 12 preconditions met, 10 seeds (42-51),
  `route_range_per_arm_mean` JOINT 0.06924 / ALT 0.057463 / OFF 0.0 / SHUF 0.0,
  C1 mean TV 0.087 with 3/10 seeds >= the 0.1 floor (7 required), C2 mean TV 0.1928 with 7/10.
- **But two things in that same manifest were not carried into the claim text.** (a) The driver's
  pass rule is a *conjunction*: `c1_pass = (seeds_above_floor >= 7) AND (mean_tv > baseline_tv)`
  (driver line 968-969), where `baseline_tv = _cross_seed_baseline_tv()` is documented in the driver
  as *"Mean pairwise within-arm cross-seed TV (**the noise band C1/C2 must exceed**)"*. Measured
  `cross_seed_baseline_tv = 0.7669`; `exceeds_baseline` is **false for BOTH C1 and C2**. So the
  claim's "C2 ... moot given C1" is imprecise -- **C2 independently failed its own baseline
  conjunct**, i.e. even the maximal JOINT-vs-SHUFFLED manipulation did not clear the design's own
  noise band, and the run therefore never demonstrated that *any* contrast in the design could
  produce a PASS. (b) The run used `support_preserving_min_first_action_classes=2` (driver line 485)
  and measured `worst_diversity_* = 2.0022` of `action_dim=5` -- ARC-065's P1 clamp at its default.
- `substrate_queue.json::mech294_coherence_magnitude_strengthening` is stale (`ready: false`,
  V3-EXQ-840-era status string) and its `recommended_next_step` reconcile of the 2026-07-30 batch
  autopsy is unactioned. Its `diagnosis_correction` conclusion ("no substrate change warranted") is
  sound and was borne out by 840b.
- Substrate confirmed present and default-OFF: `use_multi_content_theta_packet` (config.py:3306,
  `False`), `theta_packet_compose_per_candidate_coherence` (config.py:3340, `False`); module
  `ree_core/latent/multi_content_theta_packet.py`. Claim status `active`-adjacent but knobs
  default-off, per [memory] `reference-claim-status-vs-default-off-flag` -- so any arm must assert
  the knobs from measured per-arm quantities, not from the config, which 840b correctly did.

**epistemic_category (proposed):** `standard` -- **no change** (the 2026-08-01 graduation was the
right call on the information then available; the vacuity finding is raised as a governance flag for
adjudication, not applied unilaterally here). If governance accepts the flag, the correct move is to
re-adjudicate the 840b *entry* to `non_contributory / substrate_not_ready_requeue` and restore
`pending_retest_after_substrate: true`, **not** to move the category back to `substrate_ceiling` --
the ceiling this category once named (upstream range not routed) is genuinely resolved.

**Draft `what_would_answer`:**

> **SCOPE.** This claim is FUSED. Its PRIMARY falsifier is out-of-substrate for V3: joint
> multi-content decoding on hippocampal+amygdala+BG+ACC theta-resolved population recordings,
> showing whether semantically-distinct streams (goal vs risk vs state) are simultaneously decodable
> within one theta cycle, versus Kay et al. 2020's cross-cycle alternation. No such analysis is
> published; that leg resolves by literature/collaboration, not by REE (`evidence_quality_note` and
> `ceiling_routing_note` both already say so). What follows is the **REE leg only** -- the
> substrate-side joint-vs-alternation discriminator the 2026-04-26 governance hold named as
> route (a).
>
> **NON-DEGENERACY PRECONDITION.** Four conditions, all asserted from MEASURED per-arm quantities,
> never from config.
> (1) **The armed-conversion block: see ARC-065's own `what_would_answer` (P1 + P2 + the ARC-062
> gated-policy leg) -- do not re-derive it here.** P1 is the one V3-EXQ-840b did not have:
> `support_preserving_min_first_action_classes` must equal `action_dim`, with measured
> `mean_distinct_first_action_classes >= 0.9 * action_dim` (>= 4.5 of 5) **in every arm**. 840b ran
> at 2 and measured 2.0022, i.e. the committed-action distribution was capped at ~2 realised classes
> identically in all four arms, which bounds any between-arm TV by construction. A null measured
> under that clamp self-routes `substrate_not_ready_requeue`, never `weakens`.
> (2) **The 840b readiness block, retained verbatim in kind:** `joint_route_range_supra_floor`
> (JOINT routed per-candidate coherence cross-candidate RANGE > 0.01 on the 7th-largest per-seed
> value -- the SAME-STATISTIC safeguard against the V3-EXQ-661 rescale-invisible scalar null),
> `routed_range_bounded` (< 1e6, the 643a explosion ceiling),
> `adequate_committed_window_sample` (worst-cell `n_p1_ticks_past_window` >= 200 -- the precondition
> V3-EXQ-840 actually failed, per the corrected diagnosis in
> `substrate_queue.json::mech294_coherence_magnitude_strengthening.diagnosis_correction`).
> (3) **De-duplication, mandatory and explicit:** committed-action counts must be accumulated on the
> **fresh-select denominator** via `experiments/_lib/fresh_select.py` (diagnostics cleared before
> every `select_action`, so a latched/held tick contributes no row), with
> `adequate_fresh_selection_sample` >= `nominal_window_ticks / beta_rate_max_steps(20)` on the
> `MIN_SEEDS_FOR_PASS`-th largest per-seed value, and `n_latched` / `replication_factor` reported
> per cell. Raw per-tick accumulation is ~9x pseudo-replicated and voids the readout
> ([memory] `reference-hold-weighted-e3-readout-form2`).
> (4) **An instrument positive control on the DV itself, which 840b lacked.** A yoked
> same-arm-vs-same-arm control must diverge on 0 ticks (V3-EXQ-949's
> `paired_control_is_bit_identical`), AND at least one arm contrast in the design must be shown
> capable of exceeding `cross_seed_baseline_tv` -- otherwise the pre-registered pass rule
> (`mean_tv > baseline_tv`, driver line 968) is unsatisfiable by construction and a FAIL is a
> `measurement_test_design_defect`, not a claim verdict. In 840b `cross_seed_baseline_tv = 0.7669`
> and the largest observed contrast was 0.1928, so no arm cleared it.
> **SD-105 (selection-entropy headroom floor) must be OFF, or matched-constant across all arms with
> its realised log-temperature recorded per arm** -- an entropy controller acting on the E3 softmax
> directly manufactures this DV.
>
> **CONFIRMING.** On a pool with `mean_distinct_first_action_classes >= 4.5` and routed coherence
> supra-floor and mode-distinct (JOINT > ALT > SHUF ~ 0), the committed-action-class distribution
> under JOINT differs from ALTERNATION by mean paired TV **> max(0.1, cross_seed_baseline_tv)** on
> **>= 7/10 seeds** (C1), AND JOINT differs from SHUFFLED on the same bar (C2). Both must hold: C1
> alone with C2 failing is `multi_content_present_joint_not_isolated` -> `mixed`, and does NOT
> promote the joint clause. Effect-size gate scaled per [memory]
> `feedback_effect_size_pass_gate_margin`: the absolute floor 0.1 is retained as a floor, and the
> `cross_seed_baseline_tv` conjunct supplies the SD-of-the-delta half -- do NOT drop the baseline
> conjunct to make the test pass.
>
> **FALSIFYING.** With every precondition above met -- including P1 at >= 4.5 classes and a
> demonstrated capacity for some contrast to exceed the baseline -- JOINT remains
> indistinguishable from ALTERNATION on the committed-action distribution (C1 fail). That is the
> Kay-2020 parsimonious outcome: the joint-packet clause is over-specified at the
> behavioural-committed-action level this substrate can measure. It weakens the *joint* clause only;
> it does not touch MECH-089's theta-gamma multiplexing substrate, on which MECH-294 depends and
> which is separately lit-anchored (Lisman & Jensen 2013, Colgin 2009, Igarashi 2014).
> A **second** independent falsifying route, if the committed readout stays resolution-limited:
> per the claim's own "Falsifiable (secondary)", manipulate V_s anchor-eligibility so packet
> components differ in temporal vintage, and show that downstream consumers (E3 commit gate, dACC
> adaptive control) respond **no differently** to the component-typed packet than to a
> homogeneous-latent null on a readout upstream of the committed argmax (e.g. the routed
> cross-candidate range distribution, or the rank-order of the eligible set) -- a readout not
> subject to the class-count ceiling.

**Proposal sketch (for (a)):**
- **title:** `V3-EXQ-840c -- MECH-294 theta-packet joint-binding committed-action falsifier, ARMED-CONVERSION re-measurement (supersedes V3-EXQ-840b)`
- **related_claims:** `MECH-294` (primary), `ARC-065` (precondition owner), `MECH-089`, `MECH-269b`,
  `MECH-341` (the class definition the DV is built on)
- **acceptance_checks:**
  - R1 `support_preserving_min_first_action_classes = action_dim`; measured
    `mean_distinct_first_action_classes >= 4.5` in **all four** arms (ARC-065 P1).
  - R2 `use_modulatory_selection_authority = True`; measured `authority_rel_deviation_mean > 0.05`
    in all packet-ON arms (ARC-065 P2).
  - R3 the four 840b readiness preconditions unchanged (`routed_range_bounded`,
    `joint_route_range_supra_floor` 0.01, `candidate_first_action_diversity_supra_floor` -- floor
    RAISED from 1.0 to 4.5, `adequate_committed_window_sample` 200).
  - R4 fresh-select denominator + `n_latched` / `replication_factor` recorded per cell;
    `adequate_fresh_selection_sample >= 180`.
  - R5 yoked same-arm instrument control diverges on 0 ticks.
  - C1 JOINT vs ALT mean paired TV `> max(0.1, cross_seed_baseline_tv)` on >= 7/10 seeds.
  - C2 JOINT vs SHUF, same bar.
  - Outcome map unchanged from 840b (`joint_binding_behaviourally_load_bearing` -> supports;
    `multi_content_present_joint_not_isolated` -> mixed; `joint_indistinguishable_from_alternation`
    -> weakens; **any** readiness red -> `substrate_not_ready_requeue` / non_degenerate=false).
  - SD-105 OFF (or matched-constant with realised log-temperature recorded per arm).
  - Reuse the 840b driver and its OFF-arm fingerprint where eligible; the P1 change alters the arm
    fingerprint, so a fresh OFF-arm mint is expected -- emit it with
    `include_driver_script_in_hash=False` per the standing arm-reuse rule.
- **Sequencing note:** this is a *substrate-lift retest*, not a re-derive. 840b is one run and the
  re-run changes a clamp ARC-065's ratified precondition names as decisive; no re-derive brake
  applies. If governance prefers not to spend cloud time here (MECH-294 blocks no closure node),
  the honest fallback is disposition (f) with a `digestion_note` recording the P1 vacuity so the
  `weakens` is not read as stronger than it is.

**depends_on additions (if any):** none required. Optional annotation: MECH-294's own
`depends_on` is complete; it is MECH-442's inbound edge that needs the channel-vs-content
clarification (see MECH-442).

**GOVERNANCE FLAG:** `evidence_discrepancy` -- **V3-EXQ-840b, MECH-294's sole genuine experimental
entry (the `weakens` behind `exp_conf 0.249` and the 2026-08-01 `substrate_ceiling -> standard`
graduation), was measured under ARC-065's P1 clamp at its default of 2** (driver line 485;
`worst_diversity_* = 2.0022` of `action_dim=5`, vs ARC-065's required >= 4.5), and its own
pre-registered `mean_tv > cross_seed_baseline_tv` conjunct was **false for both C1 and C2**
(`cross_seed_baseline_tv = 0.7669`; largest contrast 0.1928). ARC-065's ratified
`what_would_answer` states that a null under either clamp "is VACUOUS and must self-route
`substrate_not_ready_requeue`, never `weakens`". The clamp's decisiveness was established by
V3-EXQ-947/949 (2026-08-25), i.e. **after** the 2026-08-01 autopsy -- so this is a
landed-result-vs-earlier-adjudication conflict, not an error by that autopsy. Requested adjudication:
(i) re-classify the 840b entry `weakens -> non_contributory / substrate_not_ready_requeue` on BOTH
the flat and the nested `runs/**/manifest.json` (per [memory]
`reference-indexer-reads-runs-pack-not-flat` -- the indexer scores the nested pack, and MECH-341's
own 660a incident is the precedent for this exact half-applied-reclassification bug), and restore
`pending_retest_after_substrate: true`; or (ii) retain the `weakens` with an explicit recorded
caveat. Either way the `standard` category should stay -- the original ceiling is genuinely resolved.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json` entry
`mech294_coherence_magnitude_strengthening` still carries `ready: false` and a V3-EXQ-840-era status
string, though its own `diagnosis_correction` (2026-07-31, session `confident-morse-af47a8`)
concluded no substrate change is warranted and V3-EXQ-840b then closed the line on 2026-08-01. Its
`recommended_next_step` -- reconcile the confirmed autopsy artifact
`failure_autopsy_batch-687a-707c-840-748a-833-842-810b-673-614-798afail_2026-07-30.json`, whose
"sub-floor cross-candidate range" finding contradicts the run's own `per_arm_gate` data
(measured 0.063841 vs floor 0.01, ~6x headroom) -- appears unactioned. Close the entry and reconcile
the autopsy.

---

### MECH-341 -- e3_scoring_preserves_trajectory_class_diversity. E3 score aggregation over CEM-supplied candidates must preserve trajectory-class diversity

**Recommended disposition:** **(a) testable now** -- the claim is ratified `provisional` at a scope
that was only ever measured with the candidate pool clamped to ~2 of 5 first-action classes, which is
the degenerate boundary of its own mechanism (`min_classes_for_stratification = 2`); the now-validated
raised-P1 substrate makes a genuinely non-degenerate test of the preservation assertion buildable
today, and it can fail.

**Extracted from:** the claim's `notes` ("Falsifier sequence: Phase P2 diagnostic... P3 substrate
work + B_only / ablate_B arms"), the `implementation_note`'s V3-EXQ-611/611b/611c acceptance
criteria (C1 `stratified_fired > 0`; C2 `entropy_bonus_max_abs >= 0.7 * scale`; C3
`selected_classes >= 2` with `frac_pre_ge2 >= 0.5`), the 2026-06-14 ratification's EXPLICIT CAVEAT
(scope = preservation, NOT committed-action conversion), and the 660b autopsy's retirement of the
graded-in-K falsifier as over-specifying a *preservation* claim. Nothing designed from a blank page;
the one genuinely new element is the raised-P1 arm, which comes from ARC-065 / V3-EXQ-947/949.

**Currency check (what was verified, and where).**
- **Substrate present and default-OFF, verified in code:** `use_e3_score_diversity` master
  (`ree_core/utils/config.py:4758`, `False`); module
  `ree_core/predictors/e3_score_diversity.py`; `apply_entropy_bonus` (line 165) and
  `stratified_select` (line 240) both present; `_first_action_classes` (line 143) is the sole
  definition of "trajectory class" = `int(first_step.argmax().item())`. `stratified_select` is
  consulted on BOTH the committed and uncommitted selection paths (2026-05-28 retune) and carries the
  2026-06-03 unit-range authority normalisation (`use_selection_authority` +
  `authority_min_range_floor`). Verified: the claim text is faithful to the code.
- **Evidence index (current):** `claim_evidence.v1.json` @2026-09-04T14:48Z --
  `experimental_confidence 0.683`, `genuine_exp_count 3`, **3 supports : 0 weakens**,
  `evidence_quadrant confirmed_established`, `pass_runs 3`, latest run
  `v3_exq_660_mech341_within_class_representative_diversity_20260610T044109Z_v3`. Status
  `provisional`, `v3_pending: false`, `pending_retest_after_substrate: false` -- all consistent with
  the 2026-06-14 ratification. **The `status_note`'s quoted `exp_conf 0.871` is stale (now 0.683);
  the ratification still clears the 0.62 gate, so no consequence beyond the number.**
- **Closure obligation: none open.** `closure_status.md` line 59 --
  `behavioral_diversity_isolation:GAP-B` records "MECH-341 STRAND CLOSED 2026-06-14 (ratified
  provisional, commit 80f4fcf250)".
- **Stale substrate_queue entry:** `sd_id: MECH-341` still reads
  `amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true` -- five months and four
  runs out of date. Flagged below.
- **The un-noticed clamp.** All three supporting runs (569d 2026-05-31, 614a 2026-05-30, 660
  2026-06-10) predate V3-EXQ-947/949 (2026-08-25) and were measured with
  `support_preserving_min_first_action_classes` at the shipped default of 2. Since
  `min_classes_for_stratification = 2`, the mechanism was tested at exactly the boundary where it
  first engages -- with a 2-class partition of a K-candidate pool, each "niche" is large, which is
  precisely the regime where the *within-class* representative lever (660's PASS,
  `within_class_rep_cond_entropy 4.862` vs legacy 4.781, a thin +0.08 nats against a 0.05 threshold)
  has the most room, and the *across-class* preservation assertion has almost none.

**epistemic_category (proposed):** `standard` -- **no change**. The claim has 3 clean supports, no
open ceiling, and its `pending_retest_after_substrate` is correctly `false` (the committed-action
conversion is explicitly NOT a MECH-341 retest, per the ratification note and the inline comment at
claims.yaml:64964). The proposed run below is a *strengthening/robustness* test of an already-
provisional claim, not a ceiling retest.

**Draft `what_would_answer`:**

> **SCOPE, ratified 2026-06-14 and load-bearing for reading this falsifier.** MECH-341 asserts
> **scoring-layer PRESERVATION** -- that E3 score aggregation does not collapse an upstream-diverse
> candidate pool onto a single deterministic ranking. It does **NOT** assert that the preserved
> diversity reaches the COMMITTED action; that conversion is the shared E3 selection-authority
> ceiling tracked on `behavioral_diversity_isolation:GAP-A` / MECH-439 F-dominance, and is MECH-442's
> territory, not this claim's. A flat committed-action-class entropy is therefore **not** evidence
> against MECH-341 (614e and 660 both showed byte-identical committed-class entropy while MECH-341
> passed). Two falsifier shapes are additionally RETIRED and must not be resurrected:
> (a) **graded-in-K dose-response** -- retired by confirmed `failure_autopsy_V3-EXQ-660b_2026-06-11`
> because a graded response over-specifies a binary preserve-or-collapse claim (three convergent
> iterations 660 / 660a / 660b; no 660c); (b) **in-isolation clearance via the
> `entropy_bias_scale` lever** -- V3-EXQ-616 proved mathematically that a uniform additive bias
> cannot move a single-class CEM proposer output (bit-identical across scales 1/2/4/8), so the
> B_only arm's structural bound sits at the *proposer* layer (SP-CEM presence), not the score-layer
> knob. MECH-341 is a preserver, never an in-isolation generator.
>
> **NON-DEGENERACY PRECONDITION.**
> (1) **There must be something to preserve, and this is the condition every run to date missed.**
> Measured `mean_distinct_first_action_classes` in the PRE-scoring candidate pool must be
> `>= 0.9 * action_dim` (>= 4.5 of 5), i.e. `support_preserving_min_first_action_classes` raised to
> `action_dim` -- **see ARC-065's own `what_would_answer` (P1) for the full statement and the
> V3-EXQ-949 evidence; do not re-derive it here.** At the shipped default of 2 the pool realises
> ~2-3 classes and `min_classes_for_stratification = 2` is only just satisfied, so a "preservation"
> verdict is measured at the mechanism's degenerate boundary.
> (2) The substrate must be OPERATIVE and measured as such, not assumed from config
> (`use_e3_score_diversity` and both sub-flags default `False`): `n_stratified_fired > 0` on every
> ON arm and every seed (the V3-EXQ-611 C1 criterion -- 611's ARM_2 recorded
> `n_stratified_fired = 0` across all seeds and that FAIL was a wiring artefact, not a claim result),
> and `entropy_bonus_max_abs` non-trivial relative to the observed `mean_top2_class_gap` (the 611c
> C2 lesson: `lambda = 0.05` produced a 0.045 bonus against gaps of 0.27-1.96 and was inert; the
> defaults are now `lambda = 0.5`, `bias_scale = 1.0`).
> (3) **De-duplication:** the pre/post class counts and the within-class representative entropy must
> be accumulated on the **fresh-select denominator** (`experiments/_lib/fresh_select.py` -- select
> diagnostics cleared before every `select_action`, latched ticks contribute no row), with
> `n_fresh_select`, `n_latched` and `replication_factor` reported per cell. A held/latched E3 decision
> re-counted per tick inflates every class count by the hold factor (~9x) and is the standing
> hold-weighted readout hazard.
> (4) SD-105 (selection-entropy headroom floor) OFF or matched-constant with realised log-temperature
> recorded per arm.
>
> **CONFIRMING.** On a pool with measured `mean_distinct_first_action_classes >= 4.5`: the number of
> distinct first-action classes SURVIVING the E3 scoring step (post-score, pre-commit) is
> strict-above the same quantity with `use_e3_score_diversity = False`, on >= 2/3 seeds; and the
> established within-class-representative readout `H(rep_signature | committed_class)` (the 660
> corrected readout mandated by the 614e autopsy's Learning #2 -- **not** committed-class entropy)
> remains strict-above legacy-argmin by a margin exceeding both an absolute floor and the
> cross-seed SD of the delta. The already-established instance at the clamped pool is 660:
> 4.862 vs 4.781 nats, +0.081 against a 0.05 threshold -- **note this margin is thin and its
> SD-scaled robustness was never established**, which is part of what the raised-P1 arm would test.
>
> **FALSIFYING.** Two distinct routes, either sufficient.
> (i) **Collapse at a genuinely diverse pool:** with `mean_distinct_first_action_classes >= 4.5`
> upstream and the substrate measured operative, the post-scoring distinct-class count does NOT
> exceed the `use_e3_score_diversity = False` control (the diverse pool is collapsed by scoring
> regardless of the preserver) -- MECH-341's preservation assertion fails exactly where it should
> bite hardest. (ii) **Boundary artefact:** the 660 within-class-representative lift does not
> replicate at the raised pool -- at ~4.9 classes the niches are small (often singletons, where
> `stratified_select`'s own code short-circuits to argmin: `len(class_idxs) < 2`), so a +0.08 nats
> effect that vanishes when niches shrink would indicate the ratified result was an artefact of the
> 2-class clamp rather than a property of the preserver. Either outcome is a genuine weakening and
> would put the 2026-06-14 ratification back in front of governance.

**Proposal sketch (for (a)):**
- **title:** `V3-EXQ-660c -- MECH-341 scoring-layer class-diversity preservation at an ARMED (raised-P1) candidate pool`
  (note: the retired "660c" label was for the *graded-in-K* successor, which stays retired; if the
  collision is judged confusing, mint a fresh number rather than a letter -- flagging it here rather
  than deciding it, per the EXQ versioning policy's "when in doubt, new number".)
- **related_claims:** `MECH-341` (primary), `ARC-065` (precondition owner + parent pathway),
  `MECH-442` (consumer of the preserved diversity -- reads the same class statistic downstream),
  `INV-076`, `MECH-257`
- **acceptance_checks:**
  - R1 measured `mean_distinct_first_action_classes >= 4.5` (of 5) in **every** arm, pre-scoring.
  - R2 `n_stratified_fired > 0` on every ON arm and seed; `entropy_bonus_max_abs` recorded against
    the measured `mean_top2_class_gap`.
  - R3 fresh-select denominator; `n_latched` / `replication_factor` per cell.
  - R4 `use_e3_score_diversity = False` control arm, bit-identical baseline asserted from the
    substrate hash.
  - C1 post-scoring distinct-class count strict-above the OFF control on >= 2/3 seeds.
  - C2 `H(rep_signature | committed_class)` lift over legacy-argmin exceeding
    `max(absolute_floor, k * SD(delta))` -- i.e. re-run 660's C2 with an SD-scaled gate rather than
    the bare 0.05 that the original cleared by 0.031.
  - Negative control (declare explicitly, so a null is interpretable): committed-CLASS entropy is
    expected to stay flat -- it is the EXPECTED negative control per the 660 interpretation grid,
    NOT a gate, and must not be read as a MECH-341 failure.
  - Arms: 2x2 over {P1 clamp 2, P1 clamp `action_dim`} x {`use_e3_score_diversity` OFF, ON} so the
    clamp's own contribution is dissociated from the preserver's.
- **Value if it PASSES:** converts MECH-341's supports from "stack-only / single-pathway"
  (`narrow_supports_flag`, recorded 2026-06-11 and still standing) to a result established at a
  non-degenerate pool, which is the outstanding condition on any future promotion above
  `provisional`.

**depends_on additions (if any):** consider adding **`ARC-065` is already present**; no new edges
needed. Worth recording in the claim text (not as an edge): the raised-P1 dependency is on
`support_preserving_min_first_action_classes`, i.e. on SP-CEM / ARC-065 GAP-A, which the claim
already depends on.

**GOVERNANCE FLAG:** `stale_note` -- `evidence/planning/substrate_queue.json` entry `sd_id: MECH-341`
still reads `status: amend_validated_v3_exq_614c_614d_zero_committed_authority`, `ready: true`,
describing a state superseded by V3-EXQ-614e (2026-06-07), V3-EXQ-660 (2026-06-10), the 660a/660b
reclassifications (2026-06-11) and the 2026-06-14 ratification that closed
`behavioral_diversity_isolation:GAP-B` for this claim. Update or close the entry. Separately,
MECH-341's own `status_note` quotes `exp_conf 0.871` where the live index now reads 0.683 -- the
ratification still stands (gate 0.62) but the figure should be corrected or dated when the note is
next touched.

---

### MECH-442 -- Committed-action diversity survives the selection/commit step via a behavioral-descriptor eligible-set ARCHIVE (Quality-Diversity / MAP-Elites analog)

**Recommended disposition:** **(f) defer, with a durable `digestion_note`** -- the claim's mechanism
is substantially already built (under MECH-341 and MECH-448, unnoticed by its 2026-06-18
registration), its genuine residual is a descriptor generalisation whose test is currently
unmeasurable for the same P1 reason as the rest of the group, and the whole conversion-ceiling
campaign has RUN TERMINAL on the selection face and re-routed upstream to generation/competence. It
has fan-in 0 and blocks no closure node. **What must be resolved first, specifically:** (1) ARC-065's
P1+P2 armed-conversion clamps lifted and held in every arm; (2) the `:GENERATION` face
(MECH-458 / ARC-065 rarity-seeking) unblocked from INV-088 z_world differentiation; (3) governance
adjudication of the partial-absorption proposal below, which determines whether there is a distinct
claim left to test at all.

**Extracted from:** the claim's own `notes` FALSIFIER clause (verbatim: *"if a
behavioral-descriptor-indexed committed-selection archive does NOT lift committed-action-class
entropy strict-above BOTH collapsed-proposer and matched-noise on >=2/3 seeds BEYOND the
descriptor-free top-k shortlist (V3-EXQ-569i), OR lifts it only by selecting F-dominated/unsafe
actions past the per-niche-elite bound..."*) and its pre-registered 2x2 discriminator. Turned into
house structure, with the non-degeneracy half cross-referenced (not re-derived) to ARC-065 and the
comparator set corrected for what has been built since 2026-06-18.

**Currency check (what was verified, and where).**
- **`substrate_conditional` is correct as a category, but the "not yet built" premise is
  materially stale.** `MECH-341::E3ScoreDiversity.stratified_select`
  (`ree-v3/ree_core/predictors/e3_score_diversity.py:240-330`) is, by its own docstring,
  *"1. Partition candidates by first-action class. 2. Per class, pick the argmin-score candidate as
  class representative. 3. Sample across class representatives with
  `softmax(-best_in_class_score / stratified_temperature)`."* That is a behavioural-descriptor
  partition, a per-niche F-best elite, and a coverage-aware commit rule -- MECH-442's mechanism, with
  the descriptor pinned to first-action class. It runs on the committed path and is validated
  (V3-EXQ-611c C1/C3, 614d/614e C3 readiness, 660 PASS). MECH-442's notes never mention this module.
- **The eligible-set half is also built, and by more than top-k.** `e3_selector.py:3751-3765`:
  MECH-448 / ARC-107 `shortlist_mode == "f_demotion"` builds a rank-preserving divisive-normalisation
  **F-eligibility envelope** (F decides eligibility only; F is then REMOVED from the within-eligible
  argmin), and it **takes precedence over** `margin` / `top_k`. `top_k` itself has since gained a
  conflict-graded k (`modulatory_shortlist_conflict_graded`, `k = clamp(round(k_max -
  (k_max-1)*gap_norm), 1, K)`). MECH-448 is `candidate` with a `what_would_answer` already drafted;
  MECH-449 is `provisional` / `shown`. So MECH-442's stated comparator ("BEYOND the descriptor-free
  top-k shortlist, V3-EXQ-569i") is **out of date**: the route of record is now the MECH-448
  demotion + MECH-449 Go/No-Go stack.
- **The campaign has moved off this face.** `evidence/planning/conversion_ceiling_campaign_plan.md`
  (7 nodes, 0% closed): `:P-comp` RAN non_contributory (699, precondition_unmet, "no build owed");
  `:P2-rootC` RAN TERMINAL (715/715a/717 all FAIL -- *"selection-face lift RULED OUT, delta -63"*);
  `:P4-learned-gating` **EXHAUSTED / retired**; `:FULLSTACK` RAN TERMINAL (V3-EXQ-714 readiness
  abort, C2 never scored); `:CAMPAIGN` *"converged on competence gate"* (724 -> 732 -> 732a ->
  737/738); `:GENERATION` (MECH-458) **blocked on upstream INV-088**. MECH-442 is not a face.
  `substrate_queue.json::f_dominance_conversion_ceiling` records
  `selection_face_conversion_ceiling_LIFTED_on_GAP_A_foraging_substrate__CONVERSION_ROUTE_OF_RECORD`
  via MECH-448/449 (V3-EXQ-689g PASS, promoted provisional 2026-06-22) -- **four days after MECH-442
  was registered**, with `GAP_A_lift_generalisation_NOT_yet_demonstrated` and `PROMOTES_NOTHING`.
- **Evidence:** `claim_evidence.v1.json` -- `genuine_exp_count 0`, `exp_conf 0.0`, 5 literature
  entries (4 supports / 1 weakens = Ponzi 2007, conf 0.66), `lit_conf 0.756`,
  `evidence_quadrant plausible_unproven`. Fan-in **0** (nothing depends on MECH-442). No manifest
  under `evidence/experiments/` references MECH-442 outside derived indexes.
- **No archive code exists:** grep for `map_elites` / `behavioral_descriptor` / `behavioural_descriptor`
  / `niche` across `ree-v3/ree_core/` and `ree-v3/experiments/_lib/` returns nothing relevant (the
  only `niche` hits are ecological niches in `causal_grid_world.py`). So the *descriptor-general*
  archive genuinely does not exist -- which is what keeps `substrate_conditional` correct.
- `ceiling_decision: deferred` / `ceiling_routing_note` ("DO NOT build in V3 until routed by
  experiment") is **still accurate and should be retained**.

**epistemic_category (proposed):** `substrate_conditional` -- **no change.** The descriptor-general
archive has never been built or exercised, so `substrate_ceiling` (built AND exercised, downstream
mechanism absorbs the signal) does not apply; the existing `live_status.reading:
candidate/substrate_conditional` marker was checked and is correct.

**Draft `what_would_answer`:**

> **PRECEDENCE NOTE (read before designing any run).** Three things already instantiate parts of
> this claim, and a falsifier that ignores them tests nothing new:
> (a) **`MECH-341::stratified_select`** is already a descriptor-indexed per-niche-elite archive with
> a coverage-aware commit rule, for `descriptor = first-action class`;
> (b) **`MECH-448` `f_demotion`** (e3_selector.py:3757) is already an eligible-set restriction
> upstream of the argmax with F removed from the within-eligible arbitration -- and it takes
> precedence over `top_k`;
> (c) **`MECH-449`** Go/No-Go constitution is the validated partner (V3-EXQ-689g PASS).
> The comparator in this claim's registered FALSIFIER ("BEYOND the descriptor-free top-k shortlist,
> V3-EXQ-569i") is therefore **superseded**: the baseline arm must be the MECH-448 demotion +
> MECH-449 stack (the conversion route of record), not 569i top-k. **MECH-442's remaining testable
> residual is exactly two things:** (i) a descriptor OTHER than first-action class -- specifically
> the `e2.world_forward` strategy signature or the realised committed-action class -- and (ii) niche
> partitioning placed at the **eligible-set restriction** stage of `E3TrajectorySelector.select`
> (composed with `f_demotion`), rather than at MECH-341's score-composition stage.
>
> **NON-DEGENERACY PRECONDITION.** **See ARC-065's own `what_would_answer` ARMED-CONVERSION block
> (P1 + P2 + the ARC-062 gated-policy leg) -- MECH-440 and MECH-441 already cross-reference that
> text and this claim does the same; do not re-derive it.** Two additions specific to this claim:
> (3) **The descriptor must be non-degenerate independently of the class ceiling.** The realised
> number of occupied NICHES per tick, on the proposed descriptor, must be measured `>= 3` and must
> exceed the number of first-action classes -- otherwise the "generalised" descriptor is a relabelling
> of MECH-341's existing partition and the arm is a duplicate of a built mechanism, not a test of a
> new one. Report niche-occupancy histograms per arm.
> (4) **De-duplication is mandatory and must be stated in the driver**: committed-action counts and
> niche-occupancy counts on the **fresh-select denominator**
> (`ree-v3/experiments/_lib/fresh_select.py` -- diagnostics cleared before every `select_action`, so
> a latched tick contributes no row), with `n_fresh_select >= nominal_window_ticks /
> beta_rate_max_steps(20)`, and `n_latched` / `replication_factor` emitted per cell. Without this the
> "committed-action-class entropy" DV is inflated ~9x by held decisions and every arm difference is
> an artefact of differing hold durations -- a real hazard here because a coverage-aware commit rule
> *changes hold duration by design*.
> (5) **SD-105 (selection-entropy headroom floor) must be OFF, or matched-constant across arms with
> its realised log-temperature recorded per arm.** SD-105 is a one-sided integral controller that
> raises the E3 selection temperature until realised normalised selection entropy hits a floor --
> i.e. it directly manufactures this claim's DV, and if it is pinning the floor it also compresses
> the headroom an archive lift would have to move into. A MECH-442 result measured with SD-105 live
> and unrecorded is uninterpretable in either direction.
>
> **CONFIRMING.** On an armed pool (>= 4.5 of 5 first-action classes, authority ON, gated policy ON),
> in the pre-registered **2x2 (F-de-collapse) x (behavioural-descriptor archive vs the MECH-448/449
> route of record)** ablation under the C+D composite: the descriptor-archive arm lifts
> committed-action-class entropy **strict-above** BOTH the collapsed-proposer control AND the
> matched-noise control on **>= 2/3 seeds**, AND strict-above the MECH-448/449 baseline arm by a
> margin exceeding both an absolute floor and the cross-seed SD of the delta, **WITHOUT** a
> per-niche F-quality regression: no committed action may exceed the per-niche-elite F bound, and no
> harmful action class may be globally disinhibited (the Ponzi-2007 safety constraint that motivates
> keeping the archive upstream of the argmax; the same safety guard MECH-448's own
> `what_would_answer` states).
>
> **FALSIFYING.** Either (i) the descriptor archive does NOT lift committed-action-class entropy
> beyond the MECH-448/449 baseline on >= 2/3 seeds with all preconditions met -- the behavioural
> descriptor earns no keep over F-rank eligibility restriction, and the fix is rebalancing F's E3
> variance share directly (MECH-439); or (ii) it lifts entropy only by admitting candidates past the
> per-niche-elite F bound or by disinhibiting a harmful class -- a quality/safety regression, which
> under Ponzi 2007 is the predicted failure of putting niching too close to the commit. Note the
> asymmetry deliberately: a NULL here is only informative once ARC-065's P1 is lifted; under the
> default clamp a null self-routes `substrate_not_ready_requeue`.

**Proposal sketch:** *not applicable* -- disposition is (f), no experiment proposed. The design above
is recorded so it is ready to queue if and when the deferral conditions clear. If governance instead
wants to act now, the cheapest informative step is **not** a build: it is the **partial-absorption
adjudication** below, which may show there is no distinct claim left to build.

**Proposed `digestion_note` (durable, for the claim block):**
> Digested 2026-09-04 (`/thought-digestion v3-closure`, G6). DEFERRED, not orphaned; category stays
> `substrate_conditional`; `ceiling_decision: deferred` and the "DO NOT build in V3 until routed by
> experiment" note both stand. Three specific conditions must resolve before this is queueable:
> (1) ARC-065's ARMED-CONVERSION P1 (`support_preserving_min_first_action_classes = action_dim`,
> measured >= 0.9*action_dim per arm) and P2 (`use_modulatory_selection_authority`, measured
> `authority_rel_deviation_mean > 0.05`) both held in every arm -- V3-EXQ-949 (2026-08-25) measured
> yoked committed divergence 0.000 / 0.000 / 0.3675 for P1-only / P2-only / both;
> (2) the `conversion_ceiling_campaign:GENERATION` face (MECH-458) unblocked from INV-088 z_world
> differentiation -- every other face of that campaign has RUN TERMINAL and the selection-face lift
> is recorded RULED OUT (`:P2-rootC`, delta -63);
> (3) governance adjudication of the partial-absorption finding: MECH-341's built
> `E3ScoreDiversity.stratified_select` already implements descriptor-partition + per-niche F-best
> elite + coverage-aware commit for `descriptor = first-action class`, and MECH-448's built
> `f_demotion` envelope already implements eligible-set restriction upstream of the argmax with F
> removed from within-eligible arbitration. The residual unbuilt content of MECH-442 is (a) a
> descriptor other than first-action class (`e2.world_forward` strategy signature / committed-action
> class) and (b) niche partitioning at the eligible-set stage rather than the score-composition
> stage. The registered comparator "beyond the descriptor-free top-k shortlist (V3-EXQ-569i)" is
> superseded by the MECH-448/449 conversion route of record (V3-EXQ-689g PASS, 2026-06-22).

**depends_on additions (if any):**
- **Add `MECH-448`** (and optionally `MECH-449`) -- the F-eligibility-demotion envelope is now the
  baseline this claim must beat, and is the built instance of "eligible-set restriction upstream of
  the argmax". Its absence from `depends_on` is why the stale top-k comparator survived.
- **Annotate `MECH-294`** (do not remove): the dependency is on the *modulatory channel routing*
  (`modulatory_channel_route_source`, cross-candidate route range -- demonstrably functional:
  JOINT 0.069 / ALT 0.057 / OFF+SHUF 0.0 in V3-EXQ-840b), **not** on MECH-294's joint-binding
  content clause, which V3-EXQ-840b returned `weakens` on. As written, the edge comment invites the
  wrong inference.
- No change to `MECH-341` / `MECH-439` / `ARC-065` / `ARC-062` edges.

**GOVERNANCE FLAG:** `contested_disposition` -- **PARTIAL-ABSORPTION PROPOSAL (proposal only; no id
retired, nothing deleted).**
- **Survivors:** `MECH-341` (in-group) and `MECH-448` (out-of-group, already BUILT). **Absorbed
  (partially):** `MECH-442`.
- **What text moves:** MECH-442's mechanism description -- "partitions the eligible candidate set by
  a behavioral descriptor ... and retains the F-best candidate WITHIN each behavioral niche, then
  commits by a coverage-aware rule" -- is already realised by
  `E3ScoreDiversity.stratified_select` (partition by first-action class -> argmin within class ->
  softmax across class representatives, with unit-range authority normalisation), and its
  "eligible-set restriction UPSTREAM of the winner-take-all commit, F unchanged at the argmax" half
  is already realised by MECH-448's `f_demotion` envelope. MECH-442's Cully/Mouret/Pugh literature
  anchors and the Ponzi-2007 upstream-placement constraint should be **copied** (not moved) onto
  MECH-341's and MECH-448's blocks as external-analog grounding, since they are the strongest
  available theoretical justification for machinery those claims already own.
- **Narrowed residual retained under MECH-442** (this is a partial absorption, not supersession):
  *"committed-action diversity is better preserved by a niche partition on a descriptor OTHER than
  first-action class -- specifically the `e2.world_forward` strategy signature or the realised
  committed-action class -- and by placing that partition at the eligible-set restriction stage of
  `E3TrajectorySelector.select` (composed with `f_demotion`) rather than at MECH-341's
  score-composition stage."* Title and notes to be narrowed accordingly.
- **Reverse-deps needing repointing: NONE** -- MECH-442 has **fan-in 0** (verified against the full
  registry: no claim lists it in `depends_on`). This is a clean absorption with no downstream
  breakage, which is unusual and is the main reason it is worth doing rather than leaving the
  overlap latent.
- **Why raise it rather than act:** MECH-442 is a convergence-intake claim (CDQ-003 /
  CPKT-QUALITY-DIVERSITY-20260618) whose value is partly as a record that the external QD/MAP-Elites
  frame was evaluated against REE. Narrowing it preserves that record while removing the false
  implication that its mechanism is unbuilt. Digestion proposes; governance decides.

**GOVERNANCE FLAG:** `stale_note` -- MECH-442's `notes` assert *"substrate_conditional on a
behavioral-descriptor eligible-set archive beyond top-k not yet built"* and name V3-EXQ-569i top-k as
the comparator. Both were true on 2026-06-18 and are not true now: (a) a descriptor-indexed
per-niche-elite archive with a coverage-aware commit rule IS built (`stratified_select`, under
MECH-341, validated through V3-EXQ-660); (b) the conversion route of record is MECH-448 demotion +
MECH-449 Go/No-Go (V3-EXQ-689g PASS, 2026-06-22, four days after registration), not 569i top-k; and
(c) `top_k` itself has since gained conflict-graded width. The claim's `ceiling_routing_note` and
`ceiling_decision: deferred` remain correct and should be kept.

> **Orchestrator correction (2026-09-04T21:18:57Z):** the G5 dispatch prompt said ARC-120/ARC-121 were registered from the 2026-08-27 developmental-integration intake; the G5 agent verified they were registered 2026-08-06 from `docs/thoughts/2026-08-06_scientific_evolution_of_ree.md`. The grouping edge (same namespace + title overlap) stands; the source attribution in the prompt was wrong.
