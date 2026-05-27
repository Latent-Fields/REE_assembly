# Failure autopsy: V3-EXQ-543l (ARC-062 GAP-B escalated falsifier)

| field | value |
|---|---|
| run_id | `v3_exq_543l_arc062_mode_separation_gap_b_falsifier_20260526T023059Z_v3` |
| queue_id | V3-EXQ-543l |
| hostname | ree-cloud-2 |
| purpose | evidence -- GAP-B escalated post-543k retest |
| supersedes | V3-EXQ-543k |
| supersedes_chain | V3-EXQ-543k -> V3-EXQ-543i -> V3-EXQ-543h -> V3-EXQ-543g |
| claim_ids | ARC-062, MECH-309, INV-074, MECH-334 |
| outcome | FAIL |
| interpretation_branch | `e_collapse_survives_structure_MECH309_strong_ARC063_required` |
| `basin_stable` | true |
| epistemic_category (recommended) | substrate_ceiling |
| status | confirmed (user 2026-05-27T05:23:02Z) |

## 1. Facts reconstruction (no interpretation)

### What the experiment tested

GAP-B escalated falsifier: MODE_SEPARATION_FLOOR raised 0.25 -> **0.5** and P1_W_DEVIATION_AUX_WEIGHT raised 0.1 -> **0.3** on the gated arms. Inherits the 12-arm 2x2x2 x diff_on/off grid + K_IDENTICAL_RUNS=3 basin gate + outcome-coupled REINFORCE P1 loss byte-for-byte from V3-EXQ-543k. The escalated floor adds 2x non-cancellable mode contrast at w~0.5; the escalated aux puts 3x stronger pressure on the discriminator to move w off 0.5 during outcome-coupled REINFORCE. Everything else (env config = SD-054 bipartite layout; supersession-chain logic; acceptance criteria; manifest shape) is inherited from 543k.

PASS rule: `basin_stable AND diff_on_escape AND diff_off_reproduced_collapse AND c2c3_on_pass`.

### What the manifest reports

| Metric | Value |
|---|---|
| `diff_primary_pass` | false |
| `diff_on_escape` | **false** (all 4 diff-ON gated arms 3/3 inert: ARM_8, ARM_9, ARM_10, ARM_11) |
| `diff_off_reproduced_collapse` | true (all 4 diff-OFF gated arms 3/3 inert: ARM_2, ARM_3, ARM_6, ARM_7) |
| `c2c3_on_pass` | false |
| `c2_on_pass` | false |
| `c3_on_pass` | false |
| `c3_on_relative_delta_hardened` | 0.198 (threshold 0.50) |
| `repro_543g_signature` | true |
| `D2_xtal_pass` | false |
| `D2_xtal_delta_arm7_minus_arm6` | 0.008 (threshold 0.10; essentially zero -- crystallization did not rescue) |
| `D1_dacc_alone_pass` | false (delta = -0.091) |
| `D2_off_dacc_adds_to_gated_pass` | false (delta = -0.132) |
| `D3_gated_adds_to_dacc_pass` | false (delta = -0.138) |
| `D4_replication_543c_pass` | false |
| `C4_cross_seed_variation_pass` | true (the only passing criterion) |
| `basin_stable` | true |
| `legacy_pass_rule_met` | false |
| `overall_pass` | **false** |
| `interpretation_branch` | `e_collapse_survives_structure_MECH309_strong_ARC063_required` |
| `ARM_0_baseline mean_reef_fraction` | **0.650** (single-head E3 -- substrate carries diversity when ungated) |
| `ARM_1_dacc_only mean_reef_fraction` | 0.558 |
| `ARM_2_gated_only mean_reef_fraction` | 0.552 (3/3 inert) |
| `ARM_8_gated_only_diff mean_reef_fraction` | 0.472 (3/3 inert) |
| `ARM_9_both_diff mean_reef_fraction` | 0.334 (3/3 inert) |

Per-claim direction overlay already on manifest: ARC-062=weakens, MECH-309=supports, INV-074=non_contributory, MECH-334=non_contributory.

### Expected vs observed

The 543k autopsy (`failure_autopsy_V3-EXQ-543k_2026-05-21.json`) explicitly pre-registered the anticipated branch for a real GAP-B run that landed branch-e: "mode_separation_floor + P1 w-deviation aux did not escape MECH-309 collapse" with exactly this per-claim split. The 543l manifest matches the prediction exactly even after the 2x floor escalation and 3x aux escalation.

### Failed criterion type

**Discrimination.** Negative-control / sanity (`diff_off_reproduced_collapse`) PASSES; every discrimination criterion (`diff_on_escape`, `c2c3_on_pass`, `D2_xtal`, `D1`/`D2_off`/`D3`/`D4`) FAILS. Canonical substrate-ceiling fingerprint repeated across the entire 543g..543l lineage.

## 2. Claim-layer mapping

### ARC-062 -- architectural commitment, weak-reading rule-apprehension slot
- claim_text: gated-policy architecture in which at least two policy heads share encoder features but receive different gating from a learned context discriminator
- status: candidate; epistemic_category: substrate_ceiling; v3_pending: true; pending_retest_after_substrate: true; narrow_supports_flag: true
- Test-bed appropriateness: **the claim could express itself.** Differential-head substrate landed 2026-05-17; one-hot head input augmentation landed 2026-05-17; mode_separation_floor escalated to 0.5; P1 w-deviation aux escalated to 0.3; Phase-3 crystallization landed 2026-05-17. Every architectural lever Phase-1 weak-reading is supposed to use IS in the run.
- Result: **weakens** (single contributory FAIL against a claim that previously had zero contributory PASS evidence in the trained-policy substrate).

### MECH-309 -- mechanism_hypothesis, monomodal-collapse-as-equilibrium
- claim_text: "monomodal policy collapse is the equilibrium of a parametric-policy agent without a rule-apprehension layer"
- status: candidate; v3_pending: true; epistemic_category: substrate_ceiling; pending_retest_after_substrate: true
- MECH-309's pre-registered falsifying condition (in `functional_restatement`): "if ARM_1 also produces monomodal behaviour matching ARM_0, MECH-309's diagnosis is wrong". The 543l ARM_1 / ARM_2 / ARM_3 / ARM_8 / ARM_9 / ARM_10 / ARM_11 all collapse despite differential heads + escalated floor + escalated aux + crystallization. This is the STRONG-reading positive evidence MECH-309 predicts when no rule-creator is wired.
- Result: **supports** (first contributory trained-policy support entry). Single-pathway support; remains v3_pending pending V3-EXQ-598b corroboration.

### INV-074 -- universal invariant, plasticity crystallization necessity
- claim_text: "any model-building agent whose internal scoring is dominated by a high-variance predictive pathway will converge to monostrategy under Hebbian-equivalent learning unless a time-bounded plasticity asymmetry allows competing diversity circuits to establish competitive weight before winner-take-all dynamics close off the option space"
- status: candidate; lit_conf: 0.82; epistemic_category: substrate_ceiling; pending_retest_after_substrate: true
- Test-bed appropriateness: **NO.** The crystallization closure (MECH-333/MECH-334 implementation) fires at CRYSTALLIZE_P1_OPEN_FRACTION=0.5 of P1 -- but at that point the gated heads have not differentiated (the policy was inert from step 0). The PNN/Lynx1/NgR1-analog lock mechanism froze a head pair that had nothing to lock. The lock fired but the diversity-circuit-must-establish-competitive-weight-during-the-open-window precondition was never met.
- Result: **non_contributory** (missing prerequisite -- functional differentiated GatedPolicy = MECH-333 + INV-074, not claim pressure).

### MECH-334 -- mechanism_hypothesis, critical period closure / crystallization
- claim_text: PNN/Lynx1/NgR1 three-brake closure mechanism that reduces plasticity for crystallized diversity distribution
- status: candidate; lit_conf: 0.78; v3_pending: true; epistemic_category: substrate_ceiling; pending_retest_after_substrate: true
- Test-bed appropriateness: **NO.** Same prerequisite gap as INV-074. The closure ran (crystallize_at_phase3=True on ARM_4..ARM_7 + ARM_10..ARM_11 = the xtal arms); the closure machinery worked; but it closed an already-collapsed policy. EWC residue write-protect + plasticity-injection expansion both fired; both are bit-identical to closing on noise.
- Result: **non_contributory**.

## 3. Biological-reference triage

**Closest mechanism**: PFC rule-cells / mixed-selectivity / corticostriatal action gating. Specifically:
- Miller & Cohen 2001 (Annu Rev Neurosci): PFC rule-as-top-down-bias foundational
- Rigotti et al. 2013 (Nature): mixed-selectivity
- Bongard & Nieder 2010 (PNAS): PFC rule-coding units abstract over instances
- Mitchell et al. 2016 (J Neurosci): macaque MD network with insular cluster (distributed rule-context modulation)
- Erez & Duncan 2015: MD adaptive coding
- Capkova/Mansouri/Buckley 2025 (eNeuro): frontal lesion rule-value-learning dissociation

**Dependencies of the reference mechanism in real brains**:
1. A non-Bayesian routing consumer that translates the context discriminator's output into a structural training signal on the rule-bearing pathway (biologically: cortico-striatal gating, MD thalamus, PFC-BG loop). REE analog: GAP-C (discriminator -> SD-033a LateralPFCAnalog.update source vector).
2. A trainable rule-bias head receiving downstream gradient (biologically: PFC unit plasticity under MD-gated activity). REE analog: GAP-D (lateral_pfc.rule_bias_head in P1 optimizer).
3. Per-head precision contrast that does not cancel at w~0.5 (biologically: differential PFC unit tuning). REE analog: GAP-B mode_separation_floor + P1 w-deviation aux.

**Is REE's translation faithful or a formal-definition import?** Faithful translation. The weak-reading two-head architecture is a low-dimensional approximation of high-dimensional mixed-selectivity (Pull A R2 caveat, expected to break at multi-strategy scaling -- Phase 4 / GAP-E). Not a formal-definition import. The floor/aux/differential-heads are implementation choices that respect biology; they do not import a non-biological formalism that biology refutes.

**Does the failure resemble missing-dependency in real brains?** **Yes.** A PFC unit with mixed-selectivity input but no MD-gated routing consumer and no downstream gradient on the rule-bearing weights would also fail to differentiate. The 543l result IS the missing-dependency signature: dependencies 1 and 2 (GAP-C + GAP-D) are substrate-landed but their behavioural training validation (V3-EXQ-598b) has not run.

**Lit-pull status**: discharged. `evidence/literature/targeted_review_arc_062_rule_apprehension/` (Pull A, 8 entries, 2026-05-09) + `evidence/literature/targeted_review_arc_062_refuge_forage_ecology/` (Pull B, 6 entries, 2026-05-09). lit_conf 0.78-0.82, supports-direction. Pre-registered acceptance defaults (R1 multi-stream input / R2 N=2 heads at Phase 1 / R3 score_bias-level routing / R4 tolerance-window acceptance) all derived from this synthesis. No additional lit-pull commissioned by this autopsy.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakens ARC-062 / supports MECH-309 / non_contributory INV-074 + MECH-334 | claim test bed appropriate for ARC-062 + MECH-309; missing-prerequisite for INV-074 + MECH-334 |
| Biological reference | clear, well-anchored | Pull A + Pull B discharged; not divergence |
| Prerequisites | partial | GAP-C + GAP-D substrate-landed 2026-05-17 but behavioural validation V3-EXQ-598b not yet run |
| Implementation | complete for tested factors | floor=0.5, aux=0.3, differential heads, crystallization, one-hot head input all wired and exercised; 12-arm grid evaluated |
| Environment | adequate | SD-054 reef + bipartite layout; ARM_0 baseline mean_reef_fraction=0.650 confirms substrate carries diversity when ungated |
| Measurement | adequate | K=3 basin gate, basin_stable=true, all acceptance thresholds clearly defined and triggered |
| Integration | isolated | shared-return outcome-coupled REINFORCE has no routing consumer at the gated heads -- GAP-C/D not in loop |
| Scale | adequate | 60 P1 ep x 200 step/ep x 3 seeds x 12 arms; matches 543k design |

**Dominant diagnosis**: **substrate_ceiling** (integration layer + prerequisites layer). The substrate has the wiring the claim asserts; what is missing is the training-signal routing that lets the discriminator output reach the rule-bearing pathway. Same epistemic_category already stamped on all four claims from prior 543h/i/k autopsies; confirmed for 543l.

## 5. Cluster pattern

Five iterations along the floor/aux/structure axis, share one shape:

| Experiment | Substrate change | Negative-control / sanity | Discrimination | Reading |
|---|---|---|---|---|
| V3-EXQ-543g | option-2 one-hot head input + outcome-coupled REINFORCE P1 | host-A active / cloud-3+4 inert (cross-machine bistability) | 1/3 minority-basin "weakens ARC-062" on host-A only | non_contributory (artifact) |
| V3-EXQ-543h | crystallize_at_phase3 landing | no repro (branch-c) | n/a -- substrate drift | non_contributory |
| V3-EXQ-543i | use_differential_heads landing | byte-identical runs landed opposite basins | basin-nondeterministic | non_contributory |
| V3-EXQ-543k | mode_separation_floor=0.25 + P1 w-deviation aux=0.1 | basin stability not met | mode_separation_score=0.483 below floor=0.5 | FAIL/mixed |
| **V3-EXQ-543l** | **floor=0.5 + aux=0.3 (this autopsy)** | **diff_off_reproduced_collapse=true** | **all diff-ON 3/3 inert; D2_xtal=0.008** | **FAIL branch-e** |

**Is this N independent bugs or one structural property?**

**One structural property.** The 543g cross-machine bistability + 543i basin nondeterminism + 543k subthreshold + 543l basin-stable collapse-at-escalated-thresholds together rule out "tuning noise on a working substrate". Every implementation-side intervention (differential heads, escalated floor, escalated aux, crystallization, one-hot head input) was tested and none changed the cluster shape. The shape is: outcome-coupled REINFORCE on shared-return gated heads collapses to inert monomodal equilibrium; MECH-333 differential structure + GAP-B floor/aux do not supply the missing context-routing training signal that GAP-C (discriminator -> SD-033a rule_state) and GAP-D (trainable rule_bias_head in P1 optimizer) wire.

**Two live readings**:
1. **substrate-enrichment via GAP-C/D first (user-confirmed reading)**: the missing routing consumer is the structural gap; GAP-C/D substrate landed 2026-05-17 supplies it; V3-EXQ-598b is the empirical test. Cluster reads non_contributory-pending-routing-validation until 598b lands.
2. **test-design ceiling (parked alternative)**: REINFORCE on shared return is structurally insufficient regardless of arm; gradient flows only through the selected first-step action's REINFORCE update; the discriminator's gradient signal is gated by the selected action's outcome only, not by a per-head contrast. Cluster reads as positive evidence that ARC-062 weak-reading is dead and ARC-063 V4 distributed CandidateRule field is required.

**Discriminating experiment**: V3-EXQ-598b. Substrate-enrichment reading predicts contributory PASS (routing consumer rescues differentiation). Test-design-ceiling reading predicts FAIL/weakens at GAP-C/D level (REINFORCE on shared return cannot route regardless of consumer).

## 6. Learning extracted

1. **Floor/aux escalation does not break collapse.** 2x stronger floor + 3x stronger aux did not change the cluster shape -- confirming the 543k autopsy's anticipated branch-e prediction. The GAP-B floor + aux are necessary but not sufficient.
2. **Differential heads + crystallization + escalated floor + escalated aux are ALL necessary AND NONE sufficient.** Each individually landed substrate is exercised in 543l; none unblocks the cluster shape.
3. **MECH-309's prediction is sharper than initially registered.** Collapse survives every implementation-side intervention that does not introduce a non-Bayesian routing consumer. This is positive evidence for MECH-309's strong-reading scope (parametric-policy gradient descent does not invent the discriminative split). First contributory trained-policy support for MECH-309 in the registry.
4. **The 543g/543i/543k/543l shape is one structural property.** Cross-machine bistability + basin nondeterminism + escalated-thresholds collapse together form a single coherent failure shape; treating them as N independent tuning bugs would have missed the substrate-ceiling reading.
5. **INV-074 / MECH-334 cannot be evaluated against this lineage until ARC-062 produces a differentiated gated policy.** Every closure-arm result is non_contributory because the lock fires on heads that never differentiated.
6. **The user-confirmed routing is substrate-enrichment first.** V3-EXQ-598b is the gating experiment. Do NOT commission further floor/aux ablations (notional V3-EXQ-543m) until 598b lands.

## 7. Repair pathway

| Diagnosis | Routing |
|---|---|
| Substrate-enrichment reading + missing-routing-consumer prerequisites | **Governance-stamp** + **retest via V3-EXQ-598b** (substrate-landed GAP-C/D; validation EXQ queued 2026-05-24) |
| User confirmed (2026-05-27T05:23:02Z): per-claim 4-split, governance-stamp-then-retest, substrate-enrichment first | applied |
| Further floor/aux ablations | **deferred** until V3-EXQ-598b lands |
| ARC-063 V4 lit-pull / design | **deferred** until V3-EXQ-598b lands and clarifies which reading wins |
| ARC-062 demotion | **rejected** -- pending_retest_after_substrate maintained |

## 8. Draft `evidence_quality_note` text governance should append (per claim)

Note: the 543l manifest already records the correct per-claim split (ARC-062=weakens, MECH-309=supports, INV-074=non_contributory, MECH-334=non_contributory). Governance does NOT need to override `evidence_direction_per_claim`; it just appends a quality-note paragraph and preserves the flags.

### ARC-062 + MECH-309 + INV-074 + MECH-334 (single shared paragraph)

> V3-EXQ-543l (valid manifest, escalated GAP-B at floor=0.5 / aux=0.3) FAIL branch-e: mode_separation_floor + P1 w-deviation aux did not escape MECH-309 monomodal collapse. All four diff-ON gated arms 3/3 inert (diff_on_escape=false); all four diff-OFF gated arms 3/3 inert (diff_off_reproduced_collapse=true, valid sanity); D2_xtal_delta_arm7_minus_arm6=0.008 (crystallization did not rescue the gated-only arm); repro_543g_signature=true. Extends the failure_autopsy_V3-EXQ-543i / 543k substrate_ceiling cluster reading. ARC-062=weakens (narrow_supports_flag retained -- this is one contributory FAIL against a claim with zero contributory PASS evidence; cluster shape is one structural property not five independent bugs). MECH-309=supports (first contributory trained-policy support; collapse survives differential structure + crystallization + escalated floor + escalated aux, which is what MECH-309's strong reading predicts when no rule-creator is wired). INV-074=non_contributory (crystallization fired on head pair that never differentiated before closure; the PNN/Lynx1/NgR1-analog lock mechanism was never exercised -- missing prerequisite, not claim pressure). MECH-334=non_contributory (same prerequisite gap; closure froze an already-collapsed policy). Do NOT demote ARC-062 -- pending_retest_after_substrate through V3-EXQ-598b (GAP-C: discriminator -> SD-033a rule_state routing; GAP-D: trainable rule_bias_head in P1 optimizer; both substrate-landed 2026-05-17). epistemic_category=substrate_ceiling. failure_autopsy_V3-EXQ-543l_2026-05-27.

## 9. Retest sequence

1. **V3-EXQ-598b** -- GAP-C/D behavioural validation (supersedes V3-EXQ-598/598a; gates_on=V3-EXQ-543l; queued 2026-05-24). **Contributory PASS** closes GAP-B and unblocks downstream items (V3-EXQ-606b for ARC-064 GAP-I; commitment_closure GAP-1 SD-033a behavioural arms).
2. **V3-EXQ-598b non_contributory** -> `/diagnose-errors` session on what 598b measured vs what GAP-C/D supplies; surface the substrate-enrichment vs test-design-ceiling fork explicitly.
3. **V3-EXQ-598b FAIL/weakens** -> escalate to ARC-063 V4 lit-pull + design session; treat the 543 lineage as test-design-ceiling evidence.
4. **Further floor/aux ablations (notional V3-EXQ-543m) DEFERRED** -- do not commission until 598b lands.

## 10. User-confirmed decisions

| Question | Decision (recorded 2026-05-27T05:23:02Z) |
|---|---|
| Per-claim direction overlay | Confirm 4-claim split: ARC-062=weakens, MECH-309=supports, INV-074=non_contributory, MECH-334=non_contributory |
| Post-autopsy routing | Governance-stamp + retest via V3-EXQ-598b |
| Cluster reading | Substrate-enrichment first |

## 11. Preceding autopsies in this lineage

- `failure_autopsy_EXQ-543e_2026-05-17.{md,json}`
- `failure_autopsy_EXQ-543f_2026-05-17.{md,json}`
- `failure_autopsy_V3-EXQ-543h_2026-05-18.{md,json}`
- `failure_autopsy_543i_2026-05-19.{md,json}`
- `failure_autopsy_V3-EXQ-543i_2026-05-19.{md,json}`
- `failure_autopsy_V3-EXQ-543k_2026-05-21.{md,json}`
- **`failure_autopsy_V3-EXQ-543l_2026-05-27.{md,json}` (this autopsy)**

## 12. Plan-of-record cross-references

- `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` (GAP-B owner_exq=V3-EXQ-543l; GAP-C/D owner_exq=V3-EXQ-598; substrate_note "Substrate DONE 2026-05-17. Validation V3-EXQ-598b queued 2026-05-24 ... gated on V3-EXQ-543l contributory PASS")
- `REE_assembly/evidence/planning/behavioral_diversity_isolation_plan.md` (downstream consumer)
- `REE_assembly/docs/architecture/rule_apprehension_layer.md` (ARC-062 / ARC-063 / MECH-309 architectural framing)
- `REE_assembly/docs/architecture/critical_period_crystallization.md` (INV-074 / MECH-333 / MECH-334 framing)
- `REE_assembly/docs/claims/claims.yaml` (ARC-062, MECH-309, INV-074, MECH-334 -- all already carry epistemic_category=substrate_ceiling + pending_retest_after_substrate; governance to append this autopsy paragraph)
- `REE_assembly/evidence/planning/substrate_queue.json` (ARC-062 failure_record extension)
