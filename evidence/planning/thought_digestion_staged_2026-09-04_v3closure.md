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
