# Failure Autopsy: V3-EXQ-598 (SD-033a)

- Session: failure-autopsy-V3-EXQ-598-20260529T165713Z
- Generated UTC: 2026-05-29T16:57:13Z
- Scope: single (cluster-absorb to V3-EXQ-591 substrate-uniform family)
- Status: confirmed (user judgment 2026-05-29)
- Target: `v3_exq_598_gap1_sd033a_bias_head_trainable_ablation_20260521T070715Z_v3`
- Queue ID: V3-EXQ-598
- Claim IDs: [SD-033a]
- Manifest outcome: FAIL
- Manifest evidence_direction: non_contributory (governance-applied 2026-05-21)
- Manifest epistemic_category: substrate_ceiling

## 1. Facts reconstruction (no interpretation)

V3-EXQ-598 was queued as a Phase-1 GAP-1 probe under sd033_governance_plan.md:
SD-033a bias-head trainable ablation on the ARC-062 + SD-054 bipartite stack
(post-SP-CEM defaults, differential heads + mode_separation_floor from the
543i/543k substrate line). 2-arm design, 3 seeds. Single varied factor:
`lateral_pfc_train_rule_bias_head` (frozen-zero vs trainable). Ran
2026-05-21 on ree-cloud-2 (elapsed 1346.6 s, 22.4 min). Scientific gate
declared `gates_on_exq=V3-EXQ-543k`.

Pre-registered acceptance:

| Criterion | Rule | Result |
|---|---|---|
| C1_frozen_silent       | ARM_0 p1_mean_abs_lpfc_bias < 1e-4 all seeds | PASS (0.0/0.0/0.0) |
| C2_trainable_nonzero   | ARM_1 p1_mean_abs_lpfc_bias >= 0.002 on >=2/3 seeds | PASS (0.10 / 0.052 / 0.034 -- 3/3) |
| C3_trainable_not_monomodal | ARM_1 p2_reef_visit_fraction in (0.20, 0.80) on >=2/3 seeds | FAIL (0.096 / 0.029 / 0.000 -- 0/3) |
| overall PASS | C1 AND C2 AND C3 | FAIL |

ARM_0 reef_visit_fraction (frozen baseline): 0.0964 / 0.0598 / 0.0000.
ARM_1 reef_visit_fraction (trainable):       0.0964 / 0.0289 / 0.0000.
The two arms are equivalent on the behavioural metric -- the ARM_1 head
movement (~0.05-0.10) does not translate into reef-side exploration.

Failed-criterion shape: **discrimination criterion FAILs while absolute /
substrate-readiness criteria PASS** -- the substrate-ceiling fingerprint
already named by the 2026-05-27 V3-EXQ-591 autopsy.

Manifest already carries an evidence_direction_note from the 2026-05-21
governance pass: "premature GAP-1 probe (gates_on 543k). C1/C2 pass
(frozen silent, trainable nonzero) but C3 fail -- trainable bias moves
yet P2 reef remains monomodal (0.0 on 2/3 seeds). Substrate_ceiling /
ordering: bias-head trainability alone does not break collapse before
GAP-B resolved." This autopsy formalises that determination and surfaces
the cluster shape.

## 2. Claim-layer mapping

SD-033a (`pfc.lateral_pfc_analog_rule_goal`, claims.yaml line 20010) is a
`claim_type: design_decision`, status `candidate`,
`implementation_phase: v3`, `v3_pending: true`. It asserts that the
mid-lateral PFC analog substrate must satisfy four functional signatures:

> (i) represent rules abstracted over the specific stimulus space;
> (ii) persist rule-selective activity across simulated time steps
>      without external drive;
> (iii) project bias signals into E3's trajectory-selection machinery;
> (iv) accept writes under MECH-261 gating (external_task /
>      internal_planning license, internal_replay suppress).

The V3-EXQ-598 experiment ran the implemented LateralPFCAnalog substrate
on a `gated_policy_use_differential_heads + mode_separation_floor`
configuration with `use_lateral_pfc_analog=True,
lateral_pfc_use_discriminator_source=True,
lateral_pfc_discriminator_pool_weight=0.3`. C1 and C2 directly evidence
signatures (ii) persistence and (iii) bias projection -- ARM_0
frozen-zeroed head produces silent bias by construction; ARM_1 trainable
head moves under E3 REINFORCE pressure flowing through the bias additively
into `dacc_score_bias` (see SD-033a GAP-D entry in ree-v3/CLAUDE.md
2026-05-17). Signature (iv) is exercised by the salience-coordinator
write_gate path but not specifically measured by this experiment.
Signature (i) is structural; not tested at this fidelity.

C3 is the behavioural prediction: a meaningful rule bias should drive the
agent into reef-side states with probability in the (0.20, 0.80)
monostrategy-breaking band. **This C3 prediction is not a pure SD-033a
prediction.** It depends jointly on:

- SD-033a bias-head trainability (the variable under test);
- ARC-062 mode-conditioned policy producing per-candidate first-action
  diversity (the upstream rule-creator/discriminator stage MECH-309
  diagnoses);
- The trained policy inhabiting reef-side states often enough for the
  bias to express itself.

Under the monomodal-policy collapse pattern (MECH-309 strong reading) the
agent's CEM candidates collapse to a single first-action class, the
bipartite reef layout never gets exercised, and reef_visit_fraction
remains pinned near 0 regardless of bias-head trainability. The
experiment **did not test SD-033a under conditions where the claim could
express itself**.

This is the canonical "test ran in a regime where the substrate cannot
express itself" pattern (cf. EXQ-048/048b claim_ids inheritance incident
documented in REE_assembly/CLAUDE.md).

## 3. Biological-reference triage

SD-033a is faithfully translated, not a formal-definition import.

Closest mammalian reference mechanism: mid-lateral prefrontal cortex
rule / goal representation -- Miller & Cohen 2001 (rule-as-top-down-bias,
Annu Rev Neurosci); Mansouri et al 2020 (stimulus-abstracted rule
neurons, Nat Rev Neurosci); Badre & Nee 2018 (caudal-rostral abstraction
gradient, Trends Cogn Sci). Pull A SYNTHESIS for the
`targeted_review_pfc_subdivision_architecture` lit-pull captured
lit_conf ~ 0.80 across the cluster (Miller & Cohen 2001 + Mansouri 2020 +
Badre & Nee 2018 + Rigotti 2013 + Mitchell 2016 + Bongard & Nieder 2010 +
Erez & Duncan 2015).

Dependencies of the biological reference mechanism that the failure
might be signalling:

- BG / striatal action-selection delivering per-candidate diversity into
  the PFC bias chain (this is the dependency the failure DOES signal --
  the upstream ARC-062 / SD-056 / MECH-341 cluster).
- Sensory cortex delivering distinguishable z_world per candidate (the
  SD-056 substrate fix landed 2026-05-29 addresses this).
- Hippocampal completion signal to release commitment (orthogonal here).

The failure resembles "a known dependency of the reference mechanism is
absent." Specifically, the BG-level action-selection diversity precursor
that downstream PFC rule representations bias is what's missing -- not
PFC rule-representation function itself. This is **positive evidence for
the dependency claim** (MECH-309 / ARC-062 / ARC-065 / SD-056), not
falsification of SD-033a.

Divergence from biology at the SD-033a layer: none.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | C1 + C2 PASS evidence signatures (ii) + (iii) of SD-033a. C3 falls outside what SD-033a alone can deliver. |
| Biological reference | clear | Miller & Cohen 2001 + Mansouri 2020 + Badre & Nee 2018; lit_conf 0.80; faithful translation. |
| Prerequisites | missing | ARC-062 GAP-B (mode-conditioned policy, V3-EXQ-543k contributory PASS) not landed at run time; sd033_governance_plan explicitly gates SD-033a EXQs on it. Goal-pipeline default-config substrate gap from 591 autopsy is the same structural blocker. |
| Implementation | complete | script + queue + scientific gate + run all proper; LateralPFCAnalog substrate operates as specified (proved by C1 + C2). |
| Environment | inadequate-for-discrimination | reef enrichment present (reef_enabled=True, bipartite=True, reef_bipartite_axis=horizontal, reef_bipartite_agent_band_radius=1) but monomodal-policy collapse prevents the agent inhabiting reef-half states; C3 is unmeasurable in this regime. |
| Measurement | misleading-for-this-claim | C3 reef-visit-fraction in (0.20, 0.80) is a downstream-integration metric -- under monomodal policy it ALWAYS fails regardless of bias-head trainability. Not a clean SD-033a probe. Any SD-033a successor needs a metric that exercises the bias head independent of policy class-diversity (e.g., direct rule_state cosine probes on held-out rule-context pairs). |
| Integration | isolated | SD-033a and downstream policy chain (ARC-062 + ARC-065 + SD-056) not jointly evaluable until monomodal collapse is broken. |
| Scale | adequate | 3 seeds, P0=30 / P1=50 / P2=16 episodes x 100 steps; consistent with substrate-readiness budgets. |

**Recommended `epistemic_category`: substrate_ceiling** (already in
manifest, confirmed).

## 5. Cluster pattern (cluster-absorb to substrate-uniform family)

V3-EXQ-598 fits the substrate-uniform family the 2026-05-27 V3-EXQ-591
autopsy named.

| Experiment | Claim | Negative-control / absolute | Discrimination criteria | Read |
|---|---|---|---|---|
| V3-EXQ-540a/b/c/e | MECH-307, MECH-295 | bridge instantiates and wires | conj_fire_rate=0 across all arms | default config values sat above achievable substrate ceiling pre-540 recalibration |
| V3-EXQ-603 / 603b | Q-045, MECH-313, MECH-260 | scripts complete; substrates landed | 2/3 seeds died at 350-475 steps; effective N=1 | training-regime measurement_gap; phased P0/P1 needed (V3-EXQ-603c routed 2026-05-27, FAIL) |
| V3-EXQ-590a | MECH-314 (Goldilocks novelty) | wiring intact | per-candidate signal=0 across all 5 weight arms x 3 seeds | MECH-314a per-candidate signal structurally zero under E2 z_world per-candidate collapse (V3-EXQ-571 root-cause) |
| V3-EXQ-591 | ARC-046 (infant curriculum) | C3 residue_coverage saturates to 1.0 trivially | 6/7 criteria fail every arm | z_goal collapses ~1e-7; curriculum scheduler stuck in Phase 0 |
| **V3-EXQ-598 (this)** | **SD-033a** | **C1 frozen_silent + C2 trainable_nonzero PASS (substrate operates as specified)** | **C3 reef_visit in (0.20, 0.80) fails all 3 seeds in both arms** | **monomodal-policy collapse prevents reef-side exploration regardless of bias-head trainability** |
| V3-EXQ-598b (sibling, 2026-05-27) | SD-033a + MECH-262 | C1 + C2 PASS | C3 reef-visit fraction equivalent across arms | governance-applied 2026-05-29 morning: MECH-262=non_contributory + substrate_ceiling + pending_retest_after_substrate; SD-033a retained as supports |
| V3-EXQ-490g cohort (in flight) | SD-037 / MECH-280 / MECH-281 / Q-045 / MECH-313 / MECH-260 | substrate-readiness PASS | approach_commit / behavioural diversity = 0 | parallel cluster autopsy under sibling session, same family |

This is **one structural property across structurally-different claims**, not N independent bugs. The substrate-uniform reading favoured by the 591 autopsy holds: the V3 substrate at default config under random-policy training does not produce non-trivial z_goal / behavioural diversity / action-class differentiation. Different experiments measure different downstream consumers; all hit the same upstream blocker.

The competing reading (test_design_ceiling: each experiment chose a poor metric independently) is rejected by the convergent shape across 6+ structurally-different claims with 6+ different downstream consumers. Coincidental independent metric errors at that breadth are implausible.

## 6. Learning extracted

1. **SD-033a substrate operates as specified.** ARM_0 frozen-zeroed head produces silent ARM_0 (signature ii confirmed); ARM_1 trainable head produces meaningful magnitude movement ~0.05-0.10 (signature iii confirmed). Both are positive evidence for SD-033a at the substrate-readiness layer.

2. **C3 reef-visit-fraction is a downstream-integration metric, not a clean SD-033a probe.** Any future SD-033a-specific behavioural validation needs a metric that exercises the bias head independent of policy class-diversity. Candidate replacements: direct rule_state cosine probes on held-out rule-context pairs; representational-similarity analysis on rule_state across distractor events (Mansouri 2020 transfer-to-novel-stimuli signature); rule-selective persistence measurement across forced internal_replay events (signature ii of SD-033a directly).

3. **Scientific-gate semantic is too permissive.** `_require_scientific_gate(V3-EXQ-543k)` is a manifest-existence check on a PASS outcome, not a check on whether 543k landed a *contributory* PASS (evidence_direction in supports). Governance correctly judged 598 premature even though the gate allowed it through. A stricter gate (require outcome=PASS AND evidence_direction=supports) would have caught this. V3-EXQ-598b adopted `gate_semantic=permissive_manifest_exists_outcome_pass_or_fail` deliberately to avoid this trap.

4. **5th member of the substrate-uniform family.** Convergent shape across ARC-046 / MECH-307 / Q-045 / MECH-314 / SD-033a (plus the 490g cohort in flight) strongly supports the substrate_enrichment reading over test_design_ceiling. Planning decision favoured by 591 autopsy holds: treat substrate fix as the unblocker for all family members.

5. **Failure as positive evidence for dependency.** The C3 FAIL signature resembles the biological consequence of absent BG-level action-selection diversity precursor -- this is positive evidence for the MECH-309 / ARC-062 / ARC-065 dependency claim, not falsification of SD-033a. SD-056 (E2 action-conditional divergence preservation, landed 2026-05-29) is the architecturally-faithful substrate fix at the predictor layer; V3-EXQ-569a is the behavioural falsifier in flight.

## 7. Repair pathway and routing

**Primary routing: implement-substrate `amend` on ARC-046** (goal-pipeline / training-regime substrate-prereq #2 from V3-EXQ-591 autopsy). Append V3-EXQ-598 `failure_record_entry` to the existing ARC-046 substrate_queue entry. NO new substrate_queue entry. Same substrate target the V3-EXQ-490g cohort autopsy is converging on; the 5th + 6th cluster member share the substrate-enrichment routing.

**Secondary routing follow-on note** (per user judgment 2026-05-29): leave free-text note in SD-033a evidence_quality_note that any future successor needs a redesigned metric (not just a re-run on enriched substrate). C3 reef-visit-fraction is the load-bearing metric problem; substrate enrichment alone will not produce a clean SD-033a probe -- the metric itself needs to be replaced. Candidate redesigns listed in Learning #2.

**No new EXQ to queue at this autopsy.** Behavioural retest of SD-033a deferred until: (a) ARC-062 GAP-B contributory PASS (in flight via V3-EXQ-569a SD-056 falsifier queued 2026-05-29), AND (b) goal-pipeline default-config produces non-trivial behavioural diversity (substrate-prereq #2). At that point a successor (call it V3-EXQ-598c) with a redesigned metric becomes scientifically meaningful.

**No `/lit-pull` commission.** SD-033a lit anchorage (Miller & Cohen 2001 + Mansouri 2020 + Badre & Nee 2018) at lit_conf 0.80 is adequate. The biology-vs-mechanism divergence layer is not load-bearing here.

**No `/diagnose-errors`.** The experiment ran to completion; this is FAIL not ERROR.

**No governance-demotion.** Tested-fairly threshold not cleared: the experiment did not test SD-033a under conditions where the claim could express itself. C1 + C2 PASS provide positive substrate-readiness evidence; C3 FAIL is non-contributory.

### Recommended SD-033a flag changes (governance-applied)

Per user judgment 2026-05-29 (all three flags):

- **evidence_quality_note append** (draft text in section 8 below; SD-033a currently has only "Registered pre-implementation. See SD-033 parent." with no V3-EXQ-598 mention).
- **pending_retest_after_substrate=true** (currently only set on MECH-262 from this morning's governance round; SD-033a not yet flagged).
- **narrow_supports_flag=true** (C1 + C2 are positive substrate-readiness evidence for SD-033a but single-pathway -- no env diversity, no rule-context diversity probe; should not on its own promote SD-033a).

## 8. Draft `evidence_quality_note` (governance to apply to SD-033a)

> 2026-05-29 (V3-EXQ-598 failure_autopsy): SD-033a substrate operates as
> specified -- C1 frozen_silent PASS (ARM_0 mean |score_bias|=0.0 all
> 3 seeds) + C2 trainable_nonzero PASS (ARM_1 mean |score_bias|
> 0.10/0.052/0.034 clear 0.002 floor) directly evidence signatures
> (ii) persistence and (iii) bias projection into E3. Narrow-supports:
> positive evidence is single-pathway (reef + bipartite env, monomodal
> policy regime); should not on its own promote SD-033a.
>
> C3 trainable_not_monomodal FAIL (ARM_1 reef_visit_fraction
> 0.096/0.029/0.000 across 3 seeds; ARM_0 equivalent 0.096/0.060/0.000)
> was a downstream-integration FAIL, not an SD-033a substrate FAIL:
> C3 reef-visit-band metric depends jointly on SD-033a bias-head
> trainability AND ARC-062 mode-conditioned policy producing
> per-candidate first-action diversity AND reef-side states being
> inhabited; monomodal-policy collapse (MECH-309 family) prevents the
> agent inhabiting reef-side states regardless of bias-head
> trainability.
>
> Convergent shape with V3-EXQ-591 autopsy substrate-uniform family
> (540a/b/c/e + 603/603b + 590a + 591 + 598b sibling + V3-EXQ-490g
> cohort in flight) -- one structural property (V3 substrate at default
> config under random-policy training does not produce non-trivial
> behavioural diversity) across 6+ structurally-different claims.
> evidence_direction non_contributory + epistemic_category=substrate_
> ceiling correctly applied by 2026-05-21 governance.
>
> Retest gated on (a) ARC-062 GAP-B contributory PASS (in flight via
> V3-EXQ-569a SD-056 falsifier queued 2026-05-29) and (b) goal-pipeline
> / training-regime substrate enrichment producing non-trivial
> behavioural diversity in default config. Any successor SHOULD ALSO
> redesign the SD-033a behavioural metric -- C3 reef-visit-fraction is
> a downstream-integration metric, not a clean SD-033a probe.
> Candidate replacements: direct rule_state cosine probes on held-out
> rule-context pairs (Mansouri 2020 transfer signature); rule-selective
> persistence measurement across forced internal_replay events
> (signature ii direct test). pending_retest_after_substrate=true.
> Autopsy: evidence/planning/failure_autopsy_V3-EXQ-598_2026-05-29.md.

## 9. Routing summary (one line per recipient)

- governance: append draft `evidence_quality_note` (section 8) to SD-033a in claims.yaml; set `pending_retest_after_substrate: true` and `narrow_supports_flag: true` on SD-033a; SD-033a status remains `candidate` v3_pending; rebuild claims.json.
- substrate_queue (governance writes): append `failure_record_entry` to existing ARC-046 entry (no new SD entry) per the JSON below.
- queue-experiment: NO new EXQ this autopsy; successor V3-EXQ-598c deferred until (a) V3-EXQ-569a contributory PASS + (b) goal-pipeline substrate enrichment validated. Successor must also redesign the SD-033a behavioural metric.
- closure_drift: no plan-doc gap-row updates required this pass. sd033_governance_plan.md already records the gate-on relationship to V3-EXQ-543k; GAP-1 EXQ-authoring stays "gated on V3-EXQ-543k / GAP-B" per the plan.
