# Failure Autopsy: V3-EXQ-603t (MECH-357)

**Generated:** 2026-08-13T05:24:45Z
**Scope:** single
**Status:** confirmed
**Dry-run check:** clean (`check_dry_run_citations.py` — 0 dry cited, 5 clean across the full 4-target batch this session)

## 1. Facts

- **Run:** `v3_exq_603t_instrumental_avoidance_scheduled_external_hazard_20260811T173724Z_v3`, queue_id V3-EXQ-603t, claim_ids `["MECH-357"]`.
- **Outcome:** FAIL, `evidence_direction: non_contributory`. `interpretation.label`/`readiness_route`: `pressure_insufficient_lesion_ceiling_requeue`. Not a dry run; recording provenance clean (`validate_recording.py`: 0 always-core gaps).
- **Substrate:** SD-058/MECH-357 driven under an SD-029 `scheduled_external_hazard` field (interval=20, prob=0.9, adjacent_only=True), ambient `env_drift` reverted to defaults, SD-059/MECH-358 escape-affordance bridge and harm-pathway-training fix both ON for all arms. Machine `ree-worker-3`, elapsed ~11.3h, seeds [42,43,44].
- **Readiness preconditions (5 total):** R1 (freeze commits on LESION), R2 (gate engages+suppresses on INTACT), R3 (stage-0 goal formation) all met. **R4 (discriminative headroom below — LESION must fail its own negative control) NOT met**: `G_H_LESION_frac = 1.0` (full ceiling), worse (less conflict) than 603s's exact tie of 0.6667. R5 (survivability above) met.
- Since R4 failed, primary criteria (`G_H_INTACT_clears_2of3`, `G_H_INTACT_beats_LESION`) were never validly evaluated — `evidence_direction = non_contributory` by construction, not a claim falsification. **Directional anomaly noted but not load-bearing:** ARM_INTACT (0.333) actually scored *worse* than ARM_LESION (1.0), the opposite of the hypothesized direction.
- **New finding this autopsy characterized:** the learned `avoidance_efficacy` eligibility trace underflows to numerically zero (1e-89 to 1e-127) in every arm/seed — consistent with 603h/603r/603s. Traced to `infralimbic_avoidance_gate.py`: a ~90-100:1 decay:credit tick ratio against `leak_rate=0.02` (vs `learn_rate=0.05` on far fewer credit ticks), so `(1-leak)^n_decay` underflows well before Stage-H ends. Suppression has been governed by the annealing `scaffold_floor` alone, never learned efficacy, in every run to date.

## 2. Lineage

603h (2026-06, first engagement but tied 0/3=0/3, two confounds found: no directed-escape credit, harm-pathway untrained) → 603r (2026-08-09, both fixes combined, LESION reaches ceiling — a third confound: harm-pathway fix alone eliminates conflict) → 603s (2026-08-10, mobile-predator `env_drift` pressure — exact tie 0.6667/0.6667, routed to `/implement-substrate` scoped to agent-directed pursuit or event-suddenness) → **603t (this run)** — SD-029 scheduled discrete-adjacency hazard, the scoping-recommended fix — LESION regresses to full ceiling, *worse* than 603s's tie.

## 3. Claim-layer mapping — MECH-357

Infralimbic-PFC-analog freeze-suppression + instrumental-avoidance gate (action-bias, freeze-suppression override of MECH-279 PAG, eligibility-trace avoidance-efficacy learner). `status: candidate`, `epistemic_category: standard`, `implementation_phase: v3`, `pending_retest_after_substrate: true`. `depends_on`: SD-058, MECH-279, SD-035, SD-011 — all confirmed IMPLEMENTED. The claim has **not** been tested under conditions where it could express itself for the fourth consecutive time — every attempt has been caught by a readiness/non-degeneracy guard before the primary criteria could be meaningfully evaluated.

## 4. Biological-reference triage

Closest mammalian mechanism: infralimbic-PFC → central-amygdala/PAG freeze-suppression circuit underlying active avoidance (Moscarello & LeDoux 2013/2020; Diehl et al. 2018 PL-BLA inhibitory circuit; Ho et al. 2025 IL-PV freeze-suppression). Three dated lit entries exist (`targeted_review_connectome_mech_357`, 2026-08-09) — a faithful biological translation, not a formal-definition import. The confound history (603h→603r→603s→603t) reads like successive removal of literature-named preconditions for active-avoidance acquisition; the newly-characterized eligibility-trace defect has a real biological analog (extinction/forgetting dominating acquisition — a recognizable failure mode in real avoidance-learning experiments, not an REE-specific artifact).

## 5. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | unclear | R4 failed; primary comparison invalid under the driver's own guard |
| Biological reference | clear | 3 lit entries, specific circuitry |
| Prerequisites | present | All 4 depends_on IMPLEMENTED |
| Implementation completeness | partial | Gate structurally engages, but eligibility trace never functions as designed |
| Environment adequacy | too sparse / wrong pressures | 4th distinct config-only design, still fails, and regressed vs 603s |
| Measurement adequacy | adequate | Guard performed exactly as designed; recording clean |
| Integration adequacy | coupled but unstable | No run has isolated any single component's marginal contribution |
| Scale/capacity | adequate | Not implicated |

**Failure-location (GOV-FAILLOC-1):** MIXED — MECHANISM FAILED (implementation partial: eligibility-trace defect) + ENVIRONMENT FAILED (pressure design still insufficient); MEASURES adequate. REE FAILED not established (requires all three independently adequate).

## 6. Re-derive brake & granularity-debt checks

- **Re-derive brake:** 0 prior confirmed `substrate_ceiling` hits for MECH-357 (603r/603s both used non-ceiling categories). Does **not** fire.
- **Granularity-debt:** 2 prior targets (603r, 603s), both `claim_alignment: unclear` — neither reads `weakened`. Does **not** fire (measurement/implementation debt, not granularity debt).

## 7. Recommended epistemic_category

`standard` (unchanged). The remaining path (wiring the already-built `hazard_agent_pursuit` primitive) is `complicated (buildable)`, not irreducibly substrate-blocked, so `substrate_ceiling`/`substrate_conditional` would overstate the case.

## 8. Learning extracted

- Config-only Stage-H hazard-pressure levers (static field, mobile-predator drift, scheduled discrete adjacency) are exhausted across three structurally distinct designs.
- The learned `avoidance_efficacy` eligibility trace has never functioned as designed in any run to date — a separate, newly-characterized implementation defect independent of the environment-pressure question.
- The already-built `hazard_agent_pursuit` primitive on `CausalGridWorldV2` is the one remaining candidate pressure mechanism and is buildable now.

## 9. Routing — CONFIRMED

**`/implement-substrate`, amend** (user confirmed the recommended option at the Step 8 gate, 2026-08-13). Amend the existing `mech357-freeze-incompatible-pressure-mechanism` substrate_queue entry (already partially updated by an unrelated 2026-08-12 session naming this exact next step — this autopsy formalizes it) to wire `hazard_agent_pursuit` (`causal_grid_world.py:517-535,1108,4980-5010`) into `scaffolded_sd054_onboarding.py`'s Stage-H `_build_env` (~line 1780-1800), mirroring how `scheduled_external_hazard`/`env_drift` are already threaded. **Separately** flag the eligibility-trace `leak_rate`/`learn_rate` imbalance as a probable second, independent substrate defect — do not fold silently into the pressure-mechanism fix.

Draft `evidence_quality_note`: see JSON companion `failure_autopsy_V3-EXQ-603t_2026-08-13.json`.

## 10. Governance apply checklist

- [ ] Append `evidence_quality_note` to MECH-357 in `claims.yaml` (text in JSON companion)
- [ ] `epistemic_category` unchanged (`standard`)
- [ ] Amend `substrate_queue.json` SD entry `mech357-freeze-incompatible-pressure-mechanism` per `recommended_substrate_queue_entry`
- [ ] Consider a second, separate substrate_queue line item for the eligibility-trace leak:learn defect
