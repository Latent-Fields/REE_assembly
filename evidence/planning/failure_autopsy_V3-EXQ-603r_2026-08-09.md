# Failure Autopsy — V3-EXQ-603r (MECH-357 instrumental avoidance, combined-fix retest)

**Generated:** 2026-08-09T05:43:28Z
**Scope:** single
**Status:** confirmed (interactive gate run 2026-08-09 — user confirmed reclassifying the filed `weakens` to `measurement_test_design_defect`)

## 1. Headline finding: the re-derive brake does NOT fire, despite an 18-letter lineage

Ran the Step 7 R1-R3 counting recipe over every confirmed `failure_autopsy_*.json` for MECH-357: **zero prior runs anywhere in the corpus ever claim-tagged MECH-357.** Hand-verified against every confirmed 603-lineage autopsy file's `targets[].claim_ids`:

| Autopsy | run_id(s) | claim_ids tagged |
|---|---|---|
| 603_2026-05-23 | 603_q045 | Q-045, MECH-313, MECH-260 |
| 603d_2026-06-01 | 603d | Q-045, MECH-313, MECH-260 |
| 603e-626a-622_2026-06-03 | 603e/626a/622 | Q-045,MECH-313,MECH-260 / [] / [] |
| 603f_2026-06-07 | 603f | [] |
| 603g-624c-651a_2026-06-07 | 603g/651a/624c | [] / ARC-060 / MECH-320,ARC-068 |
| 603h_2026-06-08 | 603h | [] |
| 603i_2026-06-08 | 603i | [] |
| 603l_2026-06-10 | 603l | SD-059, MECH-358 |
| 603m_2026-06-10 | 603m | [] |
| 603p_2026-06-15 | 603p | [] |
| 866b_2026-08-07 (603q check) | 866b | SD-059, MECH-358 |

**603r is the first and only run in the entire lineage whose targets tag MECH-357.** The other 17 letters were a substrate-construction program (SD-054 curriculum scaffolding -> Stage-H hazard decomposition -> harm-pathway training -> escape-affordance bridge SD-059/MECH-358) building the dependencies MECH-357 needed, not repeated ceiling hits against MECH-357 itself. Even stamping this target `substrate_ceiling` would make it hit #1, not hit #2. **The brake structurally cannot fire on this evidence.** `granularity_debt_cluster.py MECH-357` independently confirms: 0 tagging targets, trigger does not fire.

## 2. Facts

Manifest `v3_exq_603r_instrumental_avoidance_combined_fix_retest_20260808T230931Z_v3`, predecessor `V3-EXQ-603h`, `claim_ids: ['MECH-357']`. Literal Moscarello & LeDoux lesion-vs-intact design, 2 arms x 3 seeds (42/43/44, same as 603h). Both arms now carry BOTH previously-diagnosed fixes identically: `harm_pathway_fix` (603k/603q) and `escape_bridge_fix` (SD-059/MECH-358, 603j/603q).

Readiness (all three preconditions met — a real discrimination test, not a precondition failure):
- `pavlovian_freeze_reaction_present_on_lesion`: 1.0
- `ilpfc_gate_engages_and_suppresses_freeze_on_intact`: 1.0
- `stage0_forced_feed_lights_zgoal_on_intact`: 0.667

Load-bearing criteria: `G_H_INTACT_clears_2of3` PASS (INTACT survival medians all 200). `G_H_INTACT_beats_LESION` **FAIL** — because **LESION now also survives at ceiling** (medians 200/103/200, all clearing the 75-step gate).

**The decisive fact**: hazard config is byte-identical to 603h (`HAZARD_STAGE_NUM_HAZARDS`, `HAZARD_STAGE_PROXIMITY_HARM`, `HAZARD_STAGE_SURVIVAL_GATE_STEPS` all confirmed identical between the two driver scripts), where LESION medians were 27.5/16.5/19.0 (all failing). What changed is that both arms now carry the harm-pathway-training fix — and that fix alone appears sufficient to let the *reactive/passive* PAG freeze-release cycle (MECH-279, no instrumental component) survive the Stage-H hazard field, because accurate proximity-correlated harm signal makes simple freeze-when-close/release-when-safe timing adequate.

MECH-357's own `avoidance_efficacy` eligibility-trace credit event is still essentially inert (n_credit ~490-633 vs n_decay ~30746-35504, ~1-2% ratio) — the identical signature 603h already found and left unresolved.

**Failed criterion: discrimination**, mirror-image of 603h's failure shape: 603h failed because both arms flatlined near the floor (uninformative from below); 603r fails because both arms saturate at the ceiling (uninformative from above). Neither existing non-degeneracy flag tests for discriminative headroom.

Dry-run check: clean.

## 3. Claim-layer mapping

MECH-357 (`candidate/v3_pending`, `depends_on: [SD-058, MECH-279, SD-035, SD-011]`). This run tested MECH-357 under conditions where its own comparator arm (LESION) no longer isolates the claimed mechanism — the harm-pathway fix, applied to both arms for sound isolation reasons, unexpectedly rescues LESION's passive survival too. That is a test-design property, not a property of MECH-357. Freeze-suppression engagement is still confirmed (readiness 1.0).

## 4. Biological-reference triage

Closest reference: Moscarello & LeDoux 2013 (`evidence/literature/targeted_review_hazard_avoidance_learning/`, conf 0.78, load-bearing): active avoidance = resolving a Pavlovian-instrumental **conflict**; the paradigm's discriminative power over "just react passively" comes specifically from a task structure where passive Pavlovian defense *cannot* succeed. REE's Stage-H hazard field, as currently configured, does not enforce that conflict — once the harm signal is accurate, passive freeze/release timing is apparently adequate to survive this particular field (static hazards, no pursuit, no freeze-incompatible pressure). This is a newly surfaced dependency (a task-demand requirement), not a repeat of the two previously-diagnosed and now-resolved confounds (603h's "no directed escape," 603p's "harm landscape not discriminative"). Not a formal-definition import — no fresh `/lit-pull` is warranted; the existing review already covers the mechanism.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (weakened only if the confound is ignored) | freeze-suppression still confirmed engaging; survival-benefit comparison is confounded |
| Biological reference | partial | matches Moscarello & LeDoux's paradigm structurally, but REE's hazard field lacks the freeze-incompatible task demand their paradigm depends on for discriminative power |
| Dependency prerequisites | present | SD-058, MECH-279, SD-011, SD-035, harm-pathway training, escape bridge all present and engaging |
| Implementation completeness | partial | freeze-suppression complete; `avoidance_efficacy` eligibility-trace credit mechanism still essentially non-functional, same signature as 603h |
| Environment adequacy | too lenient (ceiling effect) — the dominant finding | harm-pathway fix, correctly applied to isolate the gate, unexpectedly makes the environment survivable via passive timing alone |
| Measurement adequacy | under-instrumented for this failure mode | no existing check for discriminative headroom between arms |
| Integration adequacy | coupled but confounded | the two independently-validated fixes integrate correctly with each other and the gate; their joint effect on LESION was not anticipated by the pre-registration |
| Scale/capacity | not implicated | both arms reaching ceiling argues against a capacity/budget explanation |

The driver's own pre-registration reasoned that ARM_LESION should "still be expected to freeze under threat per 603h's own PAG-forces-override finding" — that reasoning addressed whether LESION could take instrumental action, not whether accurate harm signal alone would make passive freeze/release timing survival-sufficient without any instrumental action at all. A legitimate design decision that exposed a new confound, not a flawed execution.

## 6. Learning extracted

1. New dependency discovered: the Stage-H hazard field needs a freeze-incompatible pressure (pursuit, escalating threat, or a freeze-cost such as starvation) to force the Pavlovian-instrumental conflict that gives active-avoidance paradigms their discriminative power.
2. Existing gap re-confirmed unresolved: MECH-357's own `avoidance_efficacy` credit event remains essentially inert, now masked by two independently functioning fixes.
3. The comparator arm (LESION) needs re-validation as a negative control under any harder configuration before a future letter is trusted.

## 7. Routing (confirmed)

**Reclassified per user confirmation**: `epistemic_category: measurement_test_design_defect` (was filed `weakens`), `evidence_direction: non_contributory`. Routing: `/queue-experiment`, alphabetic suffix (603s) — same question (MECH-357), redesigned environment: add a freeze-incompatible pressure to Stage-H (moving/pursuing hazard, or a freeze-cost, or extended episode budget with escalating density); re-validate LESION-as-negative-control first (a short readiness precondition) before spending budget on the full INTACT arm; re-instrument `avoidance_efficacy` credit-event diagnostics per-episode.

**Explicitly NOT `/implement-substrate`** — nothing here is a missing build; MECH-357, SD-059/MECH-358, and the harm-pathway fix are all present, wired, and functioning as designed. **Explicitly NOT a governance demotion** — MECH-357 has not been tested fairly against the highest bar; biology explains why the confound arose, arguing for fixing the test, not demoting the claim.

`recommended_substrate_queue_entry.action: none` — the `escape-affordance-bridge` entry (status IMPLEMENTED) is unaffected by this finding; its `ready_blocked_by` note is stale (still describes 603l as in-flight, predates 603q/866b/this run) — a housekeeping item for governance's next pass, not a build owed from this autopsy.

**Step 9b**: no existing hypothesis-space qid names MECH-357; no `fanout_recommendation` emitted. Registration deferred.

## 8. Evidence quality note (for governance to apply)

> V3-EXQ-603r (claim-tagged MECH-357 combined-fix rerun of 603h's own lesion-vs-intact design, first claim-tagged test of MECH-357 in the 603 lineage) FAILED the discrimination criterion (G_H_INTACT_beats_LESION) while clearing the absolute criterion (G_H_INTACT_clears_2/3, all readiness preconditions met at 1.0). Both the harm-pathway-training fix (603k) and the escape-affordance-bridge fix (SD-059/MECH-358, 603j/603q) were applied identically to both arms to isolate the ilPFC gate as the sole variable, following 603h's own diagnosis. Unexpectedly, ARM_LESION (no gate at all) ALSO reached survival ceiling (median 200/103/200 vs 603h's 27.5/16.5/19.0 under byte-identical hazard config) -- the harm-pathway fix alone makes passive PAG freeze/release timing survival-adequate in this hazard field, eliminating the Pavlovian-instrumental conflict Moscarello & LeDoux's paradigm depends on for discriminative power. This is a third, newly-surfaced test-design confound (distinct from 603h's "no directed escape" and 603p's "harm landscape not discriminative," both now resolved), not a mechanism failure: MECH-357's freeze-suppression still engages cleanly (readiness 1.0), though its own avoidance_efficacy eligibility-trace credit event remains essentially inert (n_credit ~1-2% of n_decay, unchanged from 603h). NOT demoting MECH-357; reclassified epistemic_category to measurement_test_design_defect (was filed weakens). Routed to /queue-experiment (603s), adding a freeze-incompatible pressure to Stage-H, with LESION-as-negative-control re-validated first. SD-058/MECH-357/SD-059/MECH-358 stay candidate/v3_pending, mechanism unweakened. Re-derive brake does not fire: this is the FIRST claim-tagged MECH-357 test across the whole 18-letter 603 lineage (verified R1-R3 over the full confirmed-autopsy corpus) -- the letter count reflects a substrate-construction program, not repeated same-claim ceiling hits.
