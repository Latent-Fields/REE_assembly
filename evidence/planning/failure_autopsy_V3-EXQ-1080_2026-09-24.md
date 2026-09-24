# Failure autopsy (diagnostic PASS) -- V3-EXQ-1080 contamination-footgun prevalence probe

- Run: `v3_exq_1080_contamination_truncation_prevalence_probe_20260924T000105Z_v3` (ree-cloud-2, substrate `5cac673346`, clean, elapsed 7537 s)
- Purpose: `diagnostic`, claim-free (`claim_ids: []`), source flag GFLAG-0304 option B
- Outcome: PASS (6/9 criteria; the 3 non-passing criteria are non-load-bearing prevalence readouts, see section 2)
- Self-route: `contamination_truncation_present_verdicts_robust_no_reruns_owed`
- Status: **awaiting_human_confirmation** (staging mode; drafted by a subagent of `/governance` session governance-20260924-workset; generated 2026-09-24T06:02:36Z)
- **CONFIRMED 2026-09-24T07:29:21Z** at the /governance interactive gate (session governance-20260924). Confirmed as drafted. No re-run owed for the 7 direct claims; family/uncovered claims stay undecided. Recommendation-ledger: rec-20260924-002ff612. Hypothesis ledger applied (Step 9b).
- Bears on: `GFLAG-0304`, `sd094_contamination_footgun_exposure`

## 0. Premises re-measured (brief audit)

| Premise in the brief | Re-measured | Result |
|---|---|---|
| V3-EXQ-1080 is a diagnostic PASS with no claim tags | manifest `status: PASS`, `experiment_purpose: diagnostic`, `claim_ids_tested: []` | holds |
| Self-route is `..._verdicts_robust_no_reruns_owed` | `interpretation.label` | holds |
| Queued under GFLAG-0304 option B | driver `SOURCE_FLAG = "GFLAG-0304"`; flag resolution note names the chipped probe | holds |
| "decide whether this result lets governance resolve GFLAG-0304" | `governance_flags.v1.json`: GFLAG-0304 `status: resolved`, `resolved_at: 2026-09-23T19:38:21Z` (options A+B, REE_assembly `4cf047ba8f`) | **STALE** -- the flag is already resolved. What is outstanding is the deferred decision its resolution note names: "Per-claim re-runs are decided after it reads out." Section 8 gives that decision. |
| The run is real, not a smoke | `check_dry_run_citations.py` over the run and the 4 historical target run_ids: 0 dry, 5 clean; `--family v3_exq_1080`: 0 dry / 1 real | holds |
| Always-core recording present | `validate_recording.py`: OK, 0 gaps | holds (one cosmetic mismatch, section 6) |

## 1. Facts (no interpretation)

**Design.** Four historical exposed runs were re-executed through their own driver loops, at their original full-scale configuration, on the current substrate, twice each: ARM_STOCK (as written) and ARM_OPTOUT (every env built with `hazard_free_contamination_gate=True`, which zeroes `contamination_spread` only where `num_hazards == 0`). A class-level wrap of `CausalGridWorld.__init__/step/reset` logs each hazard-free episode's length, done-cause and contaminated-cell contacts. Load-bearing criterion C_PREV: no determinable target's own verdict tuple (outcome, evidence_direction, per-claim directions, interpretation label) differs between arms. Readiness: positive control met and >= 3 determinable targets.

**Positive control** (random walker, 669c nursery geometry, 20 x 100 steps): stock death fraction 1.00 (floor 0.5), gated 0.00 (ceiling 0.0), 20/20 episodes each arm. Met.

**Per target** (all numbers read from `probe_cells` in the flat manifest):

| Target (direct claims) | DV unit | STOCK DV units died | OPTOUT DV units died | STOCK contaminated contacts | Verdict STOCK == OPTOUT | STOCK == historical manifest | Class |
|---|---|---|---|---|---|---|---|
| 669c (MECH-329, MECH-189) | hazard-free episode | 39/126 = 0.310 | 0/126 | 123 | yes: FAIL / mixed / MECH-329 weakens, MECH-189 supports / `wanting_before_liking_ordering_not_demonstrated` | yes (outcome, direction, per-claim, label) | truncated_verdict_robust |
| 939a (MECH-303) | SAFE DV walk (P1 exposure + P2 test) | 24/24 = 1.000 contain >= 1 health_depleted segment (96 deaths; walks continue, no window loss) | 0/24 | 1800 (all phases) | yes: PASS / supports / `mech303_proximity_gated_accumulation_lowers_background_vigilance` | yes | truncated_verdict_robust (driver class name; the exposure is harm intrusion, not truncation) |
| 904 (ARC-070) | hazard-free episode (24 steps) | 0/320 | 0/320 | 0 | yes: PASS / supports / `arc070_decomposition_operation_confirmed` | yes | clean |
| 888 (MECH-074, 074a, 074b) | neutral-context episode | 140/240 = 0.583 | 0/240 | 456 | yes: PASS / supports / all three per-claim supports / `mech074_readwrite_head_two_route_separability_supports` | yes | truncated_verdict_robust |

Manipulation checks (all met): OPTOUT hazard-free `contamination_spread` = 0.0 and contacts = 0 in every target; hazarded envs (888 threat context, 939a HAZARD arms) left at stock spread 0.5 in both arms; every target recorded exactly its intended DV-unit count in both arms (126 / 24 / 320 / 240); `post_done_steps` = 0 everywhere. Neither arm's verdict is degenerate for any target, so all 4 are determinable.

**Sub-threshold movement** (from `target_metrics`, where captured):
- 669c: `frac_c3_p01_complexity` 0.333 (STOCK) -> 0.000 (OPTOUT); `c3_pass` 0 in both (needs 2 of 3 seeds); wean-phase writes 567 -> 600 on seed 44. Gating made MECH-329's failing criterion *worse*, not better.
- 888: c1-c3 met on 3/3 seeds in both arms (2 needed); `aor_z_mean` ARM_FULL 0.434 -> 0.470, TAG_OFF 0.256 -> 0.296, GAIN_FLAT 0.115 -> 0.135, OFF ~0 in both. Effect ordering preserved, magnitudes slightly larger when gated.
- 904: every counter bit-identical across arms (e.g. boundary fires 180/180, decomposed 180/240).
- 939a: `target_metrics` is `{}` in both arms -- the adapter reads `man["metrics"]` or `man["readout"]`, and 939a's manifest carries neither (its DV gaps live in `criteria[].gap` and `per_seed_release_rate`). The seed-5 stdout tails show identical release rates for B/C/D, but B and C are pinned at 0 by construction and C/D run in HAZARD contexts the gate does not touch, so that identity is not evidence. Arm A, the only SAFE arm the verdict actually tests, is not in the tail, and the DV gaps were not captured. **Window-length check (red-team F1):** every 939a SAFE DV walk ran its full length in both arms (exposure `steps_total` 2880 = 12 x 240, test 1176 = 12 x 98, in STOCK and OPTOUT alike). 939a's 'death' is harm intrusion plus a layout reset inside a continuing walk. It is not a lost window, as the driver's own docstring pre-registers.

**Recomputation.** 669c 39/126 = 0.3095; 888 140/240 = 0.5833; 939a 24/24 = 1.0 -- match `metrics.json`. The verdict tuples were compared field by field from `stock_verdict` / `optout_verdict`; all four identical.

## 2. Which criteria failed

None load-bearing. The three non-passing criteria are `669c/939a/888::stock_dv_death_frac_below_material` (threshold < 0.10). They are prevalence readouts, pre-registered as non-load-bearing, and "failing" them is exactly what routes the label to `truncation_present` rather than `prevalence_low`. C_PREV passed with measured 0 verdict-sensitive targets out of 4 determinable.

## 3. Claim-layer mapping

Claim-free: the run scores no claim and its `evidence_direction: non_contributory` is correct and should stay. It audits the evidence base of 7 direct claims (MECH-329, MECH-189, MECH-303, MECH-074, MECH-074a, MECH-074b, ARC-070) and names 3 family claims (MECH-074d, SD-077, SD-079) plus 3 uncovered (MECH-106, INV-054, MECH-427) -- together the 13 indexer-scored claims of GFLAG-0304. The flag's other 13 claims (>= 50% of non-superseded entries only: ARC-060, DEV-NEED-003, INV-043, MECH-026, MECH-162, MECH-217, MECH-236, MECH-294, MECH-467, MECH-537, Q-080, Q-086, SD-106) are outside this probe's scope entirely and were not annotated under option A either.

## 4. Biological-reference triage

Not a mechanism test, so there is no mechanism to triage. The instrument question is ecological: a hazard-free nursery in which the agent's own traffic poisons cells (SD-094) is a self-generated hazard with no analogue in the ecological setting these claims describe. The gate removes that artefact while leaving deliberately hazarded contexts intact, which is the right intervention.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim-free) | audits the evidence base of 7 direct claims; tests none |
| Biological reference | n/a | instrument/ecology question, not a mechanism translation |
| Developmental / dependency prerequisites | present | positive control met at both rails; all 4 targets determinable, none degenerate |
| Implementation completeness | complete | class-level instrument covered every env (census counts match the targets' env constructors); the gate bound where intended and nowhere else |
| Environment adequacy | adequate | targets ran at their original full-scale configuration; STOCK reproduced every historical verdict tuple in full (outcome, direction, per-claim directions, label) |
| Measurement adequacy | adequate for the categorical question, partial for margins | C_PREV can fail: a change in any of 4 fields for any of 4 targets flips it. 3 of 4 targets had a large exposure contrast between arms (669c and 888 truncation at 31% and 58%; 939a harm intrusion in 24/24 SAFE walks; 0% gated), so the robustness is tested, not assumed. Two limits: 904 had zero exposure (0 contacts), so it is cleared by absence of exposure, not by a sensitivity test; 939a's margins were not captured (recording gap, section 6), so its robustness is categorical only |
| Integration adequacy | coupled (with one exposure-free target) | the hazard-free env feeds each exposed target's DV: 669c's whole nursery is hazard-free; 888's neutral context moved `aor_z`; 939a's SAFE arms carry its accumulation DVs. For 904 the gate was coupled but not exercised: 24-step episodes do not accumulate the four entries needed to contaminate a cell (0 contacts) |
| Scale / capacity | adequate for the 4 targets; not for the corpus | n = 4 purposive targets of 92 exposed runs (60 chip-scored); 3 PASS/supports + 1 FAIL/mixed. 0 of 3 exposed targets verdict-sensitive puts no useful upper bound on corpus-wide sensitivity, and negative-verdict exposed runs (where a truncated window is most plausibly what produced the FAIL) are under-sampled |

**Failure-location summary (GOV-FAILLOC-1).** Nothing failed: this is a diagnostic PASS, and no "REE failed" reading is made. MECHANISM (instrument) established; MEASURES established for the categorical verdict question and partial for margins; ENVIRONMENT established. Net: the self-route label holds for its stated scope.

**Is "verdicts robust, no re-runs owed" vacuous?** No, within its scope, for three reasons.
1. The criterion can fail. It compares four fields of each target's own verdict; the red-team fixes (F1, F7) made a label-only change and a one-arm-degenerate change count as sensitive.
2. The manipulation actually separated the arms. OPTOUT removed every contamination death and contact, while in STOCK 31% (669c) and 58% (888) of DV episodes died and all 24 of 939a's SAFE walks carried contamination deaths. A verdict insensitive to that contrast is a real finding.
3. The comparison is anchored to history. STOCK reproduced each historical verdict tuple in full, so the robustness transfers to the runs the claims actually cite. The driver checks outcome and direction only; this autopsy checked the label and per-claim directions against the historical manifests as well.

Where it is thinner than the label reads:
- 904 / ARC-070 is "clean", not "robust": it was never exposed.
- 939a / MECH-303's robustness is categorical only, and coarse by construction (red-team A2). Historically B = C = 0 on every seed (pinned), A = 0.71-0.79 and D = 0.70-0.82 against a DV_MARGIN of 0.34. The verdict therefore flips only if arm A's release rate more than halves. The test is real (A ran in the exposed SAFE context), but it is a wide instrument.
- 904's arms did differ in observation: stock deposits 0.5 per entry into `contamination_view`, while the gate zeroes it. Its counters were bit-identical because they are driven by the injected `region_vs` IV, so it is insensitive by construction and not merely unexposed.
- The label clears direct claims only, which the driver already states.

## 6. Learning extracted

1. **Contamination exposure is prevalent, not rare, on today's substrate.** The standing claim notes (GFLAG-0304 option A, 2026-09-23) say truncation was "confirmed in only 1 of 92 exposed runs (V3-EXQ-940)". That premise is now stale. Two of four re-run targets had material window truncation (669c 31% of episodes, 888 58%; window loss 10% and 36%). A third, 939a, had a different exposure: 96 contamination deaths across its 24 full-length SAFE walks, i.e. harm intrusion into the 'safe' context without window loss. That is arguably more relevant to a contextual-safety claim than truncation would be. 904's 24-step episodes were not exposed. Qualifier (red-team A5): these rates are for the CONFIGURATION on the current substrate (`ce6577a3`), not the historical exposure. For example, 669c's worst-seed write count is 550 historically, 395 in STOCK today and 600 gated. The prevalence of exposure and its verdict-sensitivity are separate questions, and this run separates them: high prevalence, zero verdict-sensitivity in the sample.
2. **Verdict-robust is not effect-neutral.** 669c's failing C3 went from 1/3 to 0/3 seeds under gating. 888's effect sizes grew slightly. The footgun perturbs magnitudes, and in this sample it happened not to cross a verdict threshold.
3a. **Arm fingerprints do not see the gate (red-team H3).** The gate is injected by the class-level wrap, not through any `config_slice`, so STOCK and OPTOUT cells emit identical arm fingerprints. That is harmless while arm reuse is emit-only, but it would become a false cache hit if arm reuse ever consumed these manifests. A successor probe should put the gate in the config slice.
3. **Recording gap (minor).** The 939a adapter captured no metrics because it read keys that 939a's manifest does not emit. Any re-use of this probe pattern should read `criteria[].gap` / `per_seed_release_rate` for 939a-style drivers (Experimental Recording Standard, section 3c family payload).
4. **Cosmetic provenance mismatch.** The manifest's top-level `seeds: [0]` is a placeholder. The real seeds are each target's own (669c 42-44; 939a 0-5; 904 11/23/47/71; 888 42/43/45) and are recorded only implicitly in the driver code. Not decision-relevant.
5. **Sampling asymmetry for any extension.** The corpus's exposed negative-verdict runs (INV-054 278/435 does_not_support/non_contributory with 300-episode phases; the MECH-314 family; SD-049 514b weakens) are where a truncated window could itself have generated the verdict. INV-054 is the highest-risk uncovered claim: long episodes and a negative verdict.

## 7. Repair pathway and routing

Node class: `complex (probe-gated) / puzzle (known rules)`, resolved for the 7 direct claims. The fact was missing and this run supplied it. For the uncovered and family claims the node stays `complex (probe-gated)`.

- **Primary action: governance annotation, no experiment.** For the 7 direct claims, the deferred per-claim decision is **no re-run owed**. Governance appends a dated readout paragraph (draft text below) to each claim's `evidence_quality_note`, next to the 2026-09-23 contamination-exposure paragraph.
- **Family claims (MECH-074d, SD-077, SD-079): caveat stands, no re-run decided.** Transfer is by constructor, not by measurement. 894* add a P0 warmup that 888 lacks; 807/823 run 32-step episodes against 904's 24.
- **Uncovered (MECH-106, INV-054, MECH-427): still undecided.**
- **Optional follow-on (routing `queue-experiment`, governance's call):** a same-pattern extension probe. It would cover INV-054 (V3-EXQ-278/435) first, because it is the highest risk, then MECH-427 (883) and MECH-106 (231a). It could add one 894* target and one 807/823 target to close the family caveats. It should also read 939a-style `criteria[].gap` margins. It should be a new EXQ number, since the question differs (different targets). Report only. Per the skill, governance chips it once it ratifies this disposition.

Re-derive brake: n/a (claim-free, no ceiling reading). Granularity-debt trigger: does not fire (no claim_ids). Step 7b pre-routing checks: 0 fires; C1/C2/C3/C5/C7 inapplicable (claim-free, no sibling prose at check time, no arm x seed result array). Step 7c carries the load.

**Draft `evidence_quality_note` paragraph for MECH-329, MECH-189, MECH-303, MECH-074, MECH-074a, MECH-074b** (append; do not replace):

> [2026-09-24 governance, GFLAG-0304 option-B readout, V3-EXQ-1080 (`v3_exq_1080_contamination_truncation_prevalence_probe_20260924T000105Z_v3`), autopsy failure_autopsy_V3-EXQ-1080_2026-09-24] CONTAMINATION RE-MEASURED -- NO RE-RUN OWED. The exposed run behind this claim (<669c | 939a | 888>) was re-run on the current substrate at full scale with and without the hazard-free contamination gate. Contamination exposure was real and material: <669c: 31% of hazard-free episodes ended health_depleted (window loss 10%) | 888: 58% of neutral-context episodes ended health_depleted (window loss 36%) | 939a: no window loss, but all 24 SAFE DV walks contained contamination deaths (96 in total; harm intrusion into the safe context, walks continued)> without the gate, 0% with it. The run's full verdict (outcome, direction, per-claim directions, label) was identical in both arms and reproduced the historical manifest. The 2026-09-23 exposure caveat is therefore discharged for this claim's verdict. Magnitudes did move (<669c: failing C3 fell 1/3 -> 0/3 seeds under gating | 939a: margins not recorded | 888: aor_z effects slightly larger under gating>). No status/confidence/direction change.

**Draft paragraph for ARC-070:**

> [2026-09-24 governance, GFLAG-0304 option-B readout, V3-EXQ-1080, autopsy failure_autopsy_V3-EXQ-1080_2026-09-24] CONTAMINATION RE-MEASURED -- NOT EXPOSED IN PRACTICE, NO RE-RUN OWED. V3-EXQ-904 re-run at full scale (4 seeds x 4 arms x 20 x 24-step episodes) recorded zero contaminated-cell contacts and zero health_depleted episodes, and every decomposition counter was bit-identical with and without the gate. 24-step episodes do not accumulate enough entries to contaminate a cell. This clears ARC-070 by absence of exposure, not by a sensitivity test; it does NOT transfer to SD-079's 32-step 807/823 runs. No status/confidence/direction change.

**Draft paragraph for MECH-074d, SD-077, SD-079** (if governance wants the family state recorded):

> [2026-09-24 governance, GFLAG-0304 option-B readout, V3-EXQ-1080] Family claim: the representative target sharing this claim's env constructor (<888 | 669c | 904>) was verdict-robust under gating, but the transfer is by constructor, not measurement (<894* add a P0 warmup | 1040 differs in schedule | 807/823 run 32-step episodes>). The 2026-09-23 exposure caveat STANDS; no re-run decided.

Also correct the stale premise in the 11 claims' 2026-09-23 paragraphs. They say "actual contamination-driven truncation is confirmed in only 1 of 92 exposed runs". V3-EXQ-1080 confirms material truncation in 2 more on today's substrate (669c, 888) and contamination harm intrusion without window loss in a third (939a). The right form is a dated addendum, not an in-place rewrite.

## 8. GFLAG-0304 and other flags

- **GFLAG-0304 cannot be "resolved" by this result, because it is already `resolved` (2026-09-23T19:38:21Z).** Its resolution note defers one thing: "Per-claim re-runs are decided after it reads out." This autopsy supplies that decision:
  - no re-run owed: MECH-329, MECH-189, MECH-303, MECH-074, MECH-074a, MECH-074b (verdict-robust under measured truncation), and ARC-070 (not exposed);
  - caveat stands, undecided: MECH-074d, SD-077, SD-079;
  - not covered, undecided: MECH-106, INV-054, MECH-427.
  Governance applies it as claims.yaml note edits. It does not change the flag's status. Suggested addendum text, if governance keeps a trail on the flag or in the walk record: "V3-EXQ-1080 read out 2026-09-24 (PASS, `contamination_truncation_present_verdicts_robust_no_reruns_owed`; autopsy failure_autopsy_V3-EXQ-1080_2026-09-24): window truncation material in 2/4 targets (669c 31%, 888 58%), harm intrusion without window loss in 939a (96 deaths across 24 full-length SAFE walks), 904 unexposed; 0/4 verdict-sensitive; no per-claim re-runs owed for the 7 direct claims; family (MECH-074d, SD-077, SD-079) and uncovered (MECH-106, INV-054, MECH-427) remain undecided; the flag's 13 non-indexer-scored claims were outside the probe."
- No other open flag references the contamination footgun, V3-EXQ-1080 or V3-EXQ-940. A search of `governance_flags.v1.json` found only resolved GFLAG-0131, 0257 and 0276, which are unrelated SD-094 confound adjudications.

## 9. Red-team verdict (Step 7c)

Run on **Fable** (the drafting session is Opus), a cross-model pass. The reasoning was withheld, and the pass recomputed from the manifest cells (dv_death_frac, window loss and the verdict-tuple equality all match). Findings are in the scratchpad file `redteam_1080.md`.

**Verdict: CONTESTED (narrow). The recommendation survives; one assertion was wrong and is now corrected.**
- **F1 (accepted, applied):** 939a was NOT truncated. Exposure `steps_total` 2880 and test `steps_total` 1176 are the same in both arms, so every SAFE walk ran its full length. Its exposure is harm intrusion plus a layout reset inside a continuing walk. Every 'truncation in 3/4' statement (lesson 1, the MECH-303 addendum, the stale-premise correction, the GFLAG-0304 trail text) now reads 2/4 truncation + 939a harm intrusion. The fix changes no recommendation. Cheap confirmer: `jq '.probe_cells[1].per_arm[].episodes.hf_by_phase'` on the flat manifest.
- A2 (accepted as a qualification): 939a's verdict is coarse by construction, because only arm A can flip it and it would have to fall from ~0.75 below 0.34. Added to section 5.
- A3 (clean): no cross-arm leakage. Global accumulators are recording-only; 939a's HAZARD cells reproduced bit-identically across arms, which is positive evidence that the per-cell RNG reset works.
- A4 (accepted): the gate also zeroes the `contamination_view` observation. 904 is therefore insensitive by construction, not merely unexposed. Added to section 5.
- A5 (accepted): full-tuple reproduction was established by this autopsy's own read of the historical manifests, not by the run. Prevalence figures describe the configuration on today's substrate. Qualifier added to lesson 1.
- A6 (clean): 669c and 888 are genuine sensitivity tests. The DVs are coupled to the hazard-free env, sub-threshold metrics moved in the predicted direction, and the verdicts held.
- Hygiene H1 (B's 0.00 identity is by construction) was applied. H3 (identical arm fingerprints) was added as lesson 3a. H2 (pooled `enabled_default_off_flags`) is noted here only. H4 is already lesson 4. H5 was fixed by the lesson-1 rewrite.
- Optional confirmer the red-team named: re-run only the 939a adapter with the metrics fix, both arms, ~22 min on ree-cloud-2. It would turn 939a's categorical robustness into a measured margin. It is not required for the disposition, and could be folded into the optional extension probe.

## 10. Recommended disposition for the walk

- Keep `evidence_direction: non_contributory` and set no claim direction, since the run is claim-free. `recommended_epistemic_category: standard` (claim-free, no suppression asserted).
- Mark the run reviewed in `review_tracker.json`. The review action is: accept the self-route as holding for its stated scope, with the two qualifications recorded (904 not exposed; 939a categorical only).
- Apply the claims.yaml note paragraphs in section 7 to the 7 direct claims, plus the optional family paragraphs.
- Decide whether to chip the optional extension probe. It is report-only here, and governance chips it after ratification.
- `recommended_diagnostic_evidence_adjudicated` is deliberately NOT set on any claim. That flag marks an adjudicated-and-expected zero experimental count, and these claims are not zero-evidence; the run is an audit of their existing entries, not a diagnostic entry for them.
- Step 9b: nothing to register. No hypothesis-space question covers contamination prevalence, the run opens no rival set, and it emits no `fanout_recommendation`. Recorded as `hypothesis_space_ledger_pending: {action: none}` in the JSON.
