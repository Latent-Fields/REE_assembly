# Failure Autopsy: V3-EXQ-866a's G0 foraging-competence failure (deep dive)

**Chip:** `chip-20260808-g0-foraging-competence-autopsy`, routed from `chip-20260808-scaffolded-c6-misdiagnosis-routing` (user-authorized 2026-08-08, option A), itself from IGW-20260808-200 / `chip-20260808-igw200-scaffolded-curriculum-hazard-rebalance`'s diagnosis (`scaffolded_curriculum_hazard_rebalance_diagnosis_staged_2026-08-08.md`).

**Status:** confirmed (user-gated via `AskUserQuestion`, 2026-08-08).

**Not a first look.** V3-EXQ-866a's G0 failure was already autopsied once (`failure_autopsy_V3-EXQ-866a_2026-08-03`, confirmed, routed to a substrate-regression diagnostic). That diagnostic (V3-EXQ-866b) has since run and reported no regression. This is the follow-on diagnosis the landed 866b redesign obligates (per `[[feedback_reautopsy_full_attention_despite_fix]]`) — a full four-layer treatment of G0 specifically, now that the "substrate regression" hypothesis is closed and today's separate C6-misdiagnosis session has isolated G0 as the real primary blocker (not C6, which was a measurement bug in 866a's own driver — see sibling chip `chip-20260808-v3exq866c-c6-run-p2-fix`, out of scope here).

## 1. What was already done (dedup check per the chip's own stop-check)

| Run | Date | Finding | Routing |
|---|---|---|---|
| V3-EXQ-866 (lightweight harness) | 2026-08-02 | G0 FAIL, `substrate_not_ready_requeue` | escalate to scaffolded_sd054_onboarding curriculum |
| V3-EXQ-866a (scaffolded curriculum, THIS run) | 2026-08-03 | G0 FAIL again, `substrate_ceiling` (confirmed autopsy) | substrate-regression diagnostic (re-run 603q fresh) |
| V3-EXQ-866b (603q re-run) | 2026-08-07 | PASS -- 603q's own script reproduces its own cited baseline; `non_contributory/standard` | no substrate drift; a recording-provenance timing gap chipped as infra-tooling, not grounds to distrust the run |
| C6-misdiagnosis diagnosis (staged doc) | 2026-08-08 | z_goal is preserved through the curriculum (probed directly, enters P2 at ~0.52); the "0.12" C6 reading is a driver-side measurement bug (unconditional `update_z_goal` vs the scheduler's contact-gated `run_p2`) | C6 fix routed separately (866c); **G0 identified as the real primary blocker and routed to its own diagnosis (this autopsy)** |
| MECH-307 `from_dims()` wiring fix | 2026-08-07 (`d63f13b7`) | MECH-307's master flag was unreachable through the factory constructor for 84 drivers incl. 603q/866a/866b -- all three ran with it silently OFF despite requesting it on | V3-EXQ-899 queued 2026-08-08T10:15Z, in-harness FULL_M307_ON vs OFF vs RANDOM A/B on 866a's exact config -- **not yet run** |

No prior artifact performs the specific four-layer diagnosis this chip asks for (a dedicated look at why G0 fails, cross-referenced against the broader competence-floor literature in this repo). `granularity_debt_cluster.py INV-034` / `Q-021` show exactly 2 tagging targets (V3-EXQ-866, V3-EXQ-866a), both already read; no third target exists yet.

## 2. Facts reconstruction

Manifest: `v3_exq_866a_inv034_q021_goal_maintenance_agency_onboarded_20260803T075813Z_v3.json`. Real run (`dry_run` unset/false, `substrate_hash` present, `elapsed_seconds` populated, `substrate_commit.commit=312ad5b0...`, predates the MECH-307 fix by 4 days).

Pre-registered gates (script docstring, lines 114-138): `G0 non-degeneracy: resource_visit_rate_FULL >= resource_visit_rate_RANDOM + 0.05 on >= 2/3 seeds`, checked first; G0 failing self-routes to `non_contributory`, explicitly "never a false weakens of INV-034/Q-021."

**G0, per seed:** `resource_visit_rate_FULL` 0.00208 / 0.00246 / 0.00539 vs `resource_visit_rate_RANDOM` 0.0103 (pooled). Fails the +0.05 margin on 0/3 seeds -- not close.

**Stage-H (a separate, earlier curriculum leg, `HAZARD_STAGE_SURVIVAL_GATE_STEPS=75`):** `hazard_median_last_window` 5.5 / 4.0 / 5.0 -- **identical per-seed values in FULL and AVOIDANCE_ONLY** (e.g. seed 42: 5.5 in both arms). `hazard_survival_gate_passed=false` on all 3 seeds, both arms. The script's own docstring states FULL and AVOIDANCE_ONLY share "the SAME harm-avoidance / NoGo channel ... all unchanged" -- this identity is the confirmation that the goal/wanting-pathway additions in FULL (z_goal, MECH-295, MECH-307, SD-057) are **not** implicated in the Stage-H survival failure; it is a property of the shared base harm-avoidance mechanism as instantiated in this curriculum.

**P1 (later stage, post Stage-H):** `p1_survival_gate_passed=true`, `p1_median_last_window=200.0` on all seeds, both arms. Survival is fine one stage later.

**P2 (measurement window):** `survival_rate` ~0.68 for FULL/AVOIDANCE_ONLY (RANDOM 0.0). Not catastrophic.

**Policy entropy at P2 -- new signature, not remarked on in the 2026-08-03 autopsy despite being in the manifest:** `policy_entropy_mean_FULL` = -9.98e-10, `policy_entropy_fresh_select_mean_FULL` = -9.64e-10 -- essentially zero (floating-point noise around a true zero), identically for AVOIDANCE_ONLY. `policy_entropy_mean_RANDOM` = 1.603 (near `ln(5)`, consistent with near-uniform selection over ~5 actions). This holds even restricted to `fresh_select` events (n_fresh_select in the hundreds, n_held in the thousands -- so this is not an artifact of commitment-holding inflating the "held" count; genuinely fresh decisions are also collapsed). **Both trained arms have converged to a near-deterministic single-action policy at P2.**

`n_resource_events` 8/9/26 out of 3846/3653/4826 total_steps -- foraging happens, but far below chance.

## 3. Prior autopsy dedup / methodological note on the Stage-H comparison

Both the 2026-08-03 autopsy and today's diagnosis doc cite "~7x below 603q's cited `base_mean_survival=37.725`" as the headline shortfall. Checking this against 603q's own manifest (`v3_exq_603q_sd059_mech358_escape_affordance_bridge_evidence_20260617T042830Z_v3.json`): its `stage_plan` names five stages -- `nursery_forced_feed`, `guided_low_conflict`, `easy_foraging`, `guarded_hazard`, `mature_test` -- and `base_mean_survival` is the `mature_test` (stage 4, `run_p2`) figure. No stage in that manifest is named "Stage-H." 866a's own source comments (`# --- Stage-H regime (603q's amend-validated anchor) ---`) assert this correspondence was deliberately checked against 603q's source, not just its manifest's human-summarized `stage_plan` field, so this is **not** presented as a confirmed mismatch -- but it was never independently re-verified by either prior autopsy, and 866b's regression check (which confirmed 603q's *script* doesn't drift) does not by itself confirm 866a's Stage-H gate is measuring the same referent 603q's cited figure measured. Recorded as an open methodological uncertainty, not resolved here.

What is not uncertain: the P1 survival gate (an unambiguous same-driver, same-scale comparison) passes cleanly (200/200), so whatever Stage-H's own early-curriculum reading means, it is not evidence that this agent cannot survive hazards at all.

## 4. Claim-layer map

INV-034 (invariant, `candidate`, `v3_pending`) + Q-021 (`open_question`) -- "goal maintenance is necessary for ethical agency" / the ARC-030 drive-absence vs self-incoherence-gated-suppression discrimination. G0 is a pre-registered **non-degeneracy precondition**, not a test of the claim -- by the driver's own design, G0 failing routes to `non_contributory` and is stated explicitly to never weaken INV-034/Q-021. This autopsy does not change that: the claim mechanism (z_goal-mediated approach vs NoGo-only avoidance) has still not been fairly exercised, because the FULL arm never clears the foraging floor needed to distinguish "goal maintenance restores approach" (C4) from "nothing forages here."

**claims.yaml currency note:** the current INV-034/Q-021 `evidence_quality_note`'s most recent (2026-08-08) entry attributes the residual gap to "z_goal decays to a P2 mean of 0.12" -- today's separate C6 diagnosis found this is a measurement artifact, not a real curriculum effect. That correction belongs to the sibling C6 chip/governance, not duplicated here, but flagged so it is not left stale in this artifact's own routing note.

## 5. Biological-reference triage

Unchanged primary reference: D1/D2 Go/NoGo basal ganglia pathways evaluating shared proposals (Bariselli 2018, PMID 29481617); wanting (prospective) vs liking (reactive) dissociation (Barch & Dowd 2010, PMID 20868638). Still not fairly exercised (same conclusion as 2026-08-03) -- G0 gates before this mechanism is engaged.

**New cross-reference, this autopsy's primary finding:** the observed phenotype -- survives fine one stage later (P1: 200/200), but the P2 trained policy has collapsed to near-zero entropy and forages below random -- is not a novel signature in this codebase. It matches, closely and specifically, the already-registered **approach-before-avoidance ontogenetic-ordering** candidate root (`[[project_ontogenetic_ordering_approach_before_avoidance]]`, itself grounded in Debiec & Sullivan 2016 PMID reviewed doi:10.1016/j.nlm.2016.10.015, Opendak 2025, Clements 2022, Brunelli 2007, Muller 2018 -- altricial-mammal active-avoidance systems are ontogenetically quiescent early; appetitive approach is bootstrapped first) and the MECH-457 competence-floor cluster's own confirmed instances:

- **V3-EXQ-728**: "all-ON substrate SURVIVES but won't FORAGE (foraging normalized -0.016, below random-walk floor)" -- the phenotype of an agent that "grew up threat-first."
- **V3-EXQ-769** (`failure_autopsy_V3-EXQ-769_2026-07-17`, MECH-457's 6th non_contributory autopsy, re-derive brake FIRED there): "avoidance learned WITHOUT approach" -- every ON arm survives the full 200 steps, avoids contamination, forages ~0. Explicitly reframed from `substrate_ceiling` to `competence_implementation_gap` (missing-dependency) rather than mandating a blind capacity/redesign fix, and routed to a GOV-FANOUT-1 discrimination portfolio: H1 drive-schedule (don't anneal the appetitive drive / approach-first ordering), H2 reward-coupling (metabolic forage-to-survive environment), H3 credit-horizon (dense-shaped forage oracle) -- each with a declared null, in flight.
- **V3-EXQ-677/798** (MECH-180, `[[project_mech180_competence_collapse_is_hazard_death]]`): a related but mechanistically distinct instance (death by hazard transit, not avoidance-without-approach) of the same umbrella MECH-457 floor -- explicitly "already OWNED and BLOCKED -- do not mint a new EXQ or substrate entry."

866a's own signature is closer to the 728/769 shape (survives, doesn't forage, near-zero P2 policy entropy) than to the 677/798 shape (dies early). The Stage-H-specific death reading (§3) may be a separate, earlier-curriculum-immaturity effect, or may share root cause with 677/798 -- this autopsy does not have grounds to discriminate that and does not attempt to.

**User confirmed (AskUserQuestion, 2026-08-08):** this is read as the same underlying competence-floor phenomenon playing out on the scaffolded_sd054_onboarding curriculum / INV-034-Q-021 claim pair, not a structurally distinct new ceiling.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | G0 non-degeneracy precondition unmet a 3rd time (866/866a original/this deep-dive); INV-034/Q-021's own mechanism still not fairly exercised. Not evidence against the claim by design. |
| Biological reference | clear, but not the one previously cited alone | D1/D2 Go/NoGo (Bariselli 2018) + wanting/liking (Barch & Dowd 2010) remain the claim's own reference, untested. The *failure phenotype* itself matches a second, independently-grounded reference: ontogenetic approach-before-avoidance ordering (Debiec & Sullivan 2016 et al.), already load-bearing for the MECH-457 cluster. |
| Developmental / dependency prerequisites | missing/immature, cross-claim | Same missing dependency the MECH-457 GOV-FANOUT-1 portfolio is actively discriminating (drive-schedule ordering / reward-coupling / credit-horizon) — not yet resolved anywhere in this codebase, INV-034/Q-021 included. |
| Implementation completeness | new finding this autopsy | Policy entropy ≈0 at P2 for both trained arms (§2) — a genuine collapsed/near-deterministic policy, not previously flagged for this run. Consistent with, not previously connected to, the "avoidance learned without approach" signature. |
| Environment adequacy | handled correctly | P2 hazard-food-attraction guard (0.3) was already calibrated against the class default's degenerate behaviour during pre-queue verification (866a's own docstring §"P2 MEASUREMENT GUARD") — not implicated here. |
| Measurement adequacy | partially uncertain | This run's own numbers are commit-verified and trustworthy at face value. The cross-run comparison to 603q's cited Stage-H figure carries an unresolved methodological uncertainty (§3) not previously surfaced. |
| Integration adequacy | untested, in flight | MECH-307 confirmed OFF for this run (bug, fixed 2026-08-07 after this run executed); V3-EXQ-899 tests the corrected wiring in-harness on this exact FULL config — queued, not yet run. |
| Scale / capacity | adequate on paper | Curriculum budgets match the cited reference (confirmed line-by-line in the 2026-08-03 autopsy, unchanged). |

## 7. Learning extracted

1. G0's failure on 866a is very likely the same underlying competence-floor phenomenon already under active, brake-fired investigation as MECH-457 (specifically the approach-before-avoidance ontogenetic-ordering line: V3-EXQ-728/769), not a ceiling specific to scaffolded_sd054_onboarding. User-confirmed.
2. Policy entropy collapse to ~0 at P2, identical in FULL and AVOIDANCE_ONLY, is a real signature in this run's own manifest not previously surfaced — it strengthens rather than merely echoes the MECH-457-cluster read (both arms have converged on a near-deterministic action, consistent with an avoidance-dominant / non-exploratory basin rather than a partial or noisy foraging deficit).
3. The Stage-H-specific survival gate fails identically in both arms (ruling out the goal/wanting-pathway additions as its cause) but the cross-run comparison anchoring the "~7x shortfall" framing rests on a methodologically uncertain correspondence to 603q's own differently-named stages — flagged, not resolved.
4. There is a genuinely new, not-yet-tried, already-queued angle specific to this harness (MECH-307 wiring fix, V3-EXQ-899) that must be allowed to resolve or fail to resolve before this is treated as confirmed-hard.
5. Reframing the epistemic category from `substrate_ceiling` (which would fire the re-derive brake at 2 hits and mandate an immediate fresh redesign) to `competence_implementation_gap` (missing-dependency, matching V3-EXQ-769's own precedent) keeps both live paths — MECH-307/899 and the MECH-457 H1/H2/H3 portfolio — open rather than forcing a premature standalone build for INV-034/Q-021 specifically. User-confirmed.
6. claims.yaml's current governance note attributes part of the residual gap to a z_goal/C6 effect that today's separate diagnosis found to be a measurement artifact, not real — worth correcting when the sibling C6 chip or the next governance cycle touches this claim, not duplicated here.

## 8. Routing (user-confirmed, AskUserQuestion 2026-08-08)

- **No new build.** Do not queue a fresh substrate redesign for INV-034/Q-021's G0 gate now — that would risk duplicating both the in-flight MECH-307 diagnostic (899) and the already-active, brake-fired MECH-457 GOV-FANOUT-1 portfolio, without first checking whether either explains this instance.
- **Await V3-EXQ-899.** Its FULL_M307_ON vs FULL_M307_OFF vs RANDOM in-harness A/B (using this exact 866a FULL config) is the immediate decisive next test and is already queued.
- **Cross-reference to MECH-457.** This finding should be linked to the MECH-457 competence-floor cluster (candidate for `/claim-synthesis` or, at minimum, an explicit cross-reference in the evidence_quality_note) so that whichever upstream fix eventually resolves MECH-457's H1/H2/H3 portfolio is also tested against scaffolded_sd054_onboarding's Stage-H/P2 measurement once available.
- `pending_retest_after_substrate = true`, gated on EITHER V3-EXQ-899 landing OR the MECH-457 H1/H2/H3 portfolio resolving.
- `recommended_epistemic_category = competence_implementation_gap` (not a 2nd `substrate_ceiling` hit — re-derive brake does NOT fire; count for INV-034/Q-021 stays at 1).
- `recommended_evidence_direction = non_contributory` (unchanged — still explicitly not evidence against INV-034/Q-021).

Step 9b (hypothesis-space ledger): skipped. No `fanout_recommendation` emitted (the discrimination portfolio this connects to, MECH-457's H1/H2/H3, is already registered and owned elsewhere — not re-registered here to avoid a duplicate/competing pre-registration), and INV-034/Q-021 has no existing pre-registered question in the ledger to resolve (confirmed unchanged from the 2026-08-03 autopsy's own check).
