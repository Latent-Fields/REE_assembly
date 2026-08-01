# Failure Autopsy: V3-EXQ-851 (ARC-062/MECH-309, GOV-FANOUT-1 Leg P-A, lateral-PFC route erratum fix)

**Generated:** 2026-08-01T12:54:47Z
**Run:** `v3_exq_851_arc062_pa_lateral_pfc_route_source_gapfanout_20260801T110851Z_v3`
**Queue ID:** V3-EXQ-851
**Claim IDs:** MECH-309, ARC-062
**Status:** confirmed

## 1. Facts

**Design.** Matched-stack identical to V3-EXQ-654j (SP-CEM, GAP-A e2_world_forward candidate summaries, MECH-448 rank-preserving F→eligibility demotion, MECH-449 active Go/No-Go opponency, CRF/LateralPFCAnalog rule-apprehension stack), same seeds (42/43/44). The **one change**: `modulatory_channel_route_source` from `'cand_world_summary'` (654j) to `'lateral_pfc'` — correcting a design-doc erratum that had originally specified `'gated_policy'` (which routes an unrelated module and has no connection to the rule-apprehension channel this leg is meant to test).

**Outcome:** FAIL. Self-route: `substrate_not_ready_requeue`. `elapsed_seconds: 27623` (~7.67 hours).

**Preconditions (8 total, 5 pass / 3 fail):**
| Precondition | Measured | Threshold | Met |
|---|---|---|---|
| committed_class_axis_exercisable | 3.0 | 2.0 | ✅ |
| gapa_consumed_summary_divergence | 2.0 | 2.0 | ✅ |
| gapa_consumed_summary_bounded | 0.163 | <1e6 | ✅ |
| arm_on_rule_field_differentiated_and_matured | 3.0 | 2.0 | ✅ |
| propagation_non_vacuity_arm_on_bias_differs | 3.0 | 2.0 | ✅ |
| **mech448_demotion_lever_live_and_excluding** | **0.0** | 2.0 | ❌ |
| **mech449_active_nogo_live_and_suppressing** | **0.0** | 2.0 | ❌ |
| **lateral_pfc_route_range_supra_floor_and_sample_adequate (NEW, C1g)** | **0.0** | 2.0 | ❌ |

## 2. The key comparison — same seeds, 654j vs 851

| Precondition | V3-EXQ-654j (seeds 42/43/44) | V3-EXQ-851 (same seeds) |
|---|---|---|
| mech448_demotion_lever | **17.76** (robustly live) | **0.0** (dead) |
| mech449_active_nogo | **1.549** (robustly live) | **0.0** (dead) |

Verified by direct manifest comparison. Both drivers set `USE_F_ELIGIBILITY_DEMOTION=True` and `USE_GO_NOGO_CONSTITUTION=True` — the flags are not the difference. The only design change is the route-source value.

## 3. Why "substrate not ready" is the wrong read

Same seeds → same random draws, same environment layout, same warmup trajectory up to the point where the manipulated channel diverges. A precondition flipping from robustly-live to completely dead under *identical* seeds is a **deterministic** result, not a stochastic power/noise problem. Requeuing with new seeds risks reproducing the identical dead outcome if the cause is the route-source change (as the evidence strongly suggests) rather than seed luck.

## 4. What the manifest's own note gets wrong

The manifest's `evidence_direction_note` states: *"H1 (selection-authority coupling gap) is REFUTED as the ceiling... C1-holds-C2-fail self-routes conversion_ceiling_persists_despite_active_nogo."* That is the **C1-holds** branch's conclusion — it does not describe *this* run, which hit **C1-fails** (three preconditions dead, including the brand-new erratum-fix check). This autopsy does not endorse the "H1 refuted" language as applying to this run's actual outcome; the note appears to be describing the driver's general outcome-map rather than this specific result.

## 5. Code trace (partial — root cause not yet fully identified)

`ree_core/agent.py`'s `modulatory_channel_route_source == 'lateral_pfc'` branch identity-routes `_bdc_lpfc` into `channel_route_bias`, which is passed to `E3.select()` via `_e3_select_kwargs`. MECH-448/449 are gated by their own independent flags (`use_f_eligibility_demotion`, `use_go_nogo_constitution`) and read from `_dacc_last_bundle`/candidate scoring elsewhere — the code paths look structurally independent. This means the causal mechanism connecting the route-source change to MECH-448/449's collapse is **not yet identified from a static code read alone**. A near-zero-range injected channel (per the failing C1g check — the lateral_pfc route itself shows sub-floor range) could still be destabilizing downstream candidate scoring/selection dynamics in a way not visible without running a controlled comparison.

## 6. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | 3 preconditions failed, no H1 verdict possible |
| Biological reference | not load-bearing | diagnostic, matches 654j's own convention |
| Prerequisites | **partially present** | candidate-generation dynamics fine; MECH-448/449 dead |
| Implementation | route branch correctly wired, flags correctly set | yet mechanisms didn't engage — deeper interaction, not a config bug |
| Environment | same seeds as 654j | rules out seed variance |
| Measurement | new C1g check also failed | erratum-fix route itself under-differentiated |
| Integration | sole causal candidate: route-source change | mechanism not yet identified |
| Scale | not assessed | diagnosis is prior to scale questions |

## 7. Learning extracted

1. A precondition flipping from robustly-live to completely dead under identical seeds is a strong deterministic signal — treat differently from a marginal/noisy near-miss.
2. Self-route embedded prose can describe the wrong outcome branch — always check which precondition branch actually fired before accepting a manifest's own narrative.
3. A structurally-independent-looking code path is not sufficient evidence of no causal interaction — a near-zero-range injected signal can still destabilize downstream dynamics in ways invisible to a static read.
4. A ~7.7-hour full design is too expensive to blindly re-run; a cheap targeted ablation should isolate the cause first.

## 8. Routing (user-confirmed)

**Evidence direction: `non_contributory`** (confirmed — no verdict possible on H1 from this run).

**Routing: `/queue-experiment`** — a **targeted diagnostic** (not a blind requeue of the same ~7.7-hour design) comparing `modulatory_channel_route_source='lateral_pfc'` vs `'none'` at the same seeds (42/43/44), tracking MECH-448/449 engagement directly, to confirm or rule out `channel_route_bias` itself as the causal factor before spending more compute on the full falsifier design. User explicitly confirmed: do not accept the self-route at face value and requeue as-is.

Re-derive brake: 0 prior `substrate_ceiling` autopsies for ARC-062/MECH-309 in this category — does not fire (this reading is `measurement_test_design_defect`, not `substrate_ceiling`).
