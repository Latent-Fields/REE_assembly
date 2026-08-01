# Failure Autopsy: V3-EXQ-844 (MECH-321 R4 mid-execution task-outcome effect)

Generated: 2026-08-01T10:37:54Z
Status: confirmed (interactive gate completed with user, including a follow-up mechanistic investigation)
Scope: single

## 1. Facts

- **run_id**: `v3_exq_844_mech321_r4_midexec_task_effect_20260801T013315Z_v3`
- **claim_ids**: MECH-321. **bears_on**: MECH-321, SD-084, ARC-070, ARC-071.
- **reuse_baseline_from**: `v3_exq_839_sd084_midexec_reachability_20260729T220727Z_v3`
- **evidence_direction**: weakens (self-routed), label `midexec_decomposition_does_not_reduce_harm`
- Not a dry run (confirmed via `check_dry_run_citations.py`). `non_degenerate: true`.
- This is the EVIDENCE successor to V3-EXQ-839 (confirmed `failure_autopsy_V3-EXQ-839_2026-07-30`), which validated the R4 mid-execution abort hook is REACHABLE (415 evaluations ON, 0 OFF) but explicitly adjudicated reachability only, deferring the TASK-OUTCOME question to a successor. 839's autopsy recommended this successor; per CLAUDE.md's chip-routing rule, it was chipped by governance once ratified (2026-07-30 GOV-DIAG-1 recurrence note), not self-chipped by 839's own autopsy session.

### The question
MECH-321's R4 functional_restatement: mid-execution decomposition reads V_s on a committed macro's REMAINING content while it is executing; if V_s has dropped (or a MECH-288 boundary fires), the remainder is decomposed and the commit latch released rather than blindly finishing a now-unreliable plan. Reachability is closed (839). Open: does aborting a stale macro reduce execution-time forward-prediction error / harm relative to letting it run to completion?

### Design
Reuses the SD-084 lineage's ARM_HANDLE_OFF/ON exactly (same env, schedule, substrate stack, both seed tiers -- `use_persistent_committed_program_handle` is the only manipulation, unchanged from 839). What's new is the DV: 839's own manifest carries no per-tick forward-PE/harm field (only a whole-run mean), and this driver's own analysis of 839's data showed why a whole-run mean is the WRONG statistic -- the manipulation can only affect ticks from the first-divergence-tick onward (839's own `first_divergence_tick` values: 101, 64, 78 out of 720 ticks/cell), so a whole-run mean is diluted by up to ~85% arm-identical ticks. This run computes a PAIRED, POST-DIVERGENCE-WINDOW, fresh-selection-restricted statistic instead.

### Readiness: all green (both arms)
- `multi_action_commits_present`: MET (139, both arms) -- multi-action programs genuinely committed.
- `decomposition_precommit_live`: MET (1724, both arms) -- decomposition machinery genuinely running.
- `off_forward_pe_varies` / `off_forward_pe_bounded`: MET -- OFF-arm positive control confirms the DV is not a degenerate constant.
- `midexec_decomposition_occurs` (ARM_HANDLE_ON only): confirmed occurring (scoped out for OFF, correctly -- not meaningful there).

### Criteria
| Criterion | load-bearing | measured | threshold | passed |
|---|---|---|---|---|
| C1_TASK_OUTCOME_IMPROVES (harm, windowed, fresh-selection-restricted) | YES | -0.003262 | >0.0 (needs improvement) | **FAIL** |
| C2_FORWARD_PE_CORROBORATES (mechanistic corroboration, same window) | no | 0.000247 | >0.0 | **PASS** |

**The dissociation**: aborting a stale macro DOES measurably lower forward-prediction error post-abort (C2, mechanistic corroboration passes) -- confirming the mechanism engages and does what it is architecturally designed to do informationally. But this does NOT translate into reduced task harm (C1, the claim's actual load-bearing prediction, fails, with the point estimate trending slightly the wrong way).

## 2. Follow-up mechanistic investigation (why does C2 pass while C1 fails?)

The user asked, mid-autopsy, whether this dissociation might be explained by REE's threat/fear proto-emotion machinery biasing (or failing to bias) the post-abort redecomposition toward defensive/lower-harm paths. Investigated directly against the substrate code (not speculated):

1. **MECH-288** (the boundary detector that can trigger MECH-321's abort, alongside a V_s drop) is PURE predictive-surprise / goal-shift detection (`ree_core/hippocampal/event_segmenter.py`) -- fast-scale PE z-score over z_world+z_self, slow-scale BOCPD change-point on z_goal. Zero contact with `z_harm_a`/`z_harm_s`.
2. **REE does have a genuinely fear/threat-triggered mid-execution abort** -- but it is a DIFFERENT, parallel mechanism: MECH-091 ("urgency interrupt," `agent.py:5342-5399`), which reads `z_harm_a`/`z_harm_un` against an urgency threshold and is architecturally distinct from MECH-321 (both are independently enumerated among the five principled mid-execution commit-releases). MECH-091 did not fire in this run -- MECH-321's trigger is unrelated to hazard proximity.
3. **The redecomposition step itself (`_apply_policy_decomposition`, `hippocampal/module.py:896-983`; `PolicyDecomposition.evaluate()`/`decompose_sequence()`, `policy/policy_decomposition.py:471-747`) reads only z_self/z_world/z_goal/event_segmenter -- no `z_harm_a`, no threat_scale, anywhere in the file.**
4. **More fundamentally: this step performs NO ranked selection among candidate re-tilings at all.** It is a binary decompose/keep test per candidate on structural grounds, and ALL surviving leaf tiles are additively recombined (`return kept + decomposed_out`). There is no choice being made here to bias with any signal, harm or otherwise.
5. A real, adjacent motivational channel does exist (SD-039's `AnchorGoalPayload`, carrying `wanting_strength` and a BLA-sourced `arousal_tag`, feeding `GhostGoalBank.rank()` for MECH-293's ghost-anchor revisitation) -- architecturally closer to "bias which path gets chosen" than the raw amygdala pathway. But it is REWARD-valence (wanting), not harm-valence; a `VALENCE_HARM_DISCRIMINATIVE` residue-field channel exists elsewhere in the substrate but is never captured into `AnchorGoalPayload`; and this channel is not wired into `_apply_policy_decomposition` at all.

**Conclusion**: the user's hypothesis is coherent and points at a real, specific, previously-unrecorded gap -- but more precisely than "fear biases choice." Neither a harm-valence signal NOR a selection mechanism to apply one exists at this specific junction. This is not "the signal exists but isn't wired in" (a simple wiring fix); it is that the redecomposition step has no selection step of any kind to bias. This directly and cleanly explains the C1/C2 dissociation: C2 passes because aborting mechanically reduces PE regardless of what replaces the stale macro; C1 fails because nothing in the replacement step selects FOR lower harm.

No existing `substrate_queue.json` entry or claims.yaml claim covers "hazard-aware policy-decomposition retiling" (checked directly).

## 3. Claim-layer map

**MECH-321** (`policy_decomposition_via_event_segmenter`, candidate, v3_pending, `epistemic_category` currently unset). depends_on: ARC-070, MECH-288, MECH-269, MECH-094. `bears_on` chain carries a 6-hit GOV-DIAG-1 recurrence note (2026-07-30) that explicitly distinguishes THIS run's axis (mid-execution task-outcome, reached via 839's clean reachability result) from the REFUSED 816e same-question env-harshening re-pose (a different, PRE-COMMIT/R1 axis, saturated at the forward-PE discrimination floor across 4 letters). This run is not a repeat of a braked pattern.

## 4. Biological-reference triage

Closest mammalian reference for MECH-321 itself: recognizing a plan has become unreliable mid-execution and abandoning/replanning rather than perseverating (a general cognitive-control / plan-monitoring literature, not specifically cited in this driver's docstring). C2's positive result (lower PE post-abort) is exactly what this predicts.

For the C1 gap specifically: real defensive/threat-appraisal systems (amygdala-driven, PAG-mediated flight/freeze circuits) DO bias which alternative path an animal takes when a plan is interrupted by new threat-relevant information -- not just THAT it replans, but toward WHICH replan. REE has the analogous pieces (BLA/CeA amygdala SD-035, infralimbic avoidance gate MECH-357/SD-058, hippocampal motivational payload SD-039) but, per the investigation above, they are not connected to this specific redecomposition junction. This is a genuine `biology before formal definitions`-style gap: REE has each component of a threat-modulated replanning circuit but has not yet joined them at the point where MECH-321 makes its replacement selection -- more precisely, it has not yet BUILT a selection step there at all.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (for the harm-outcome prediction specifically) | The claim's task-outcome prediction was tested fairly (readiness all green, windowed statistic fixes 839's own identified whole-run-mean dilution problem) and did not hold. The mechanistic prediction (abort reduces PE) DID hold. |
| Biological reference | clear for the mechanism, gap identified for the outcome | Plan-monitoring/replanning literature supports C2's finding; threat-modulated path-selection literature (amygdala/PAG defensive circuits) is the relevant biology for WHY C1 might fail, and REE has the component pieces but not the junction. |
| Developmental / dependency prerequisites | present | ARC-070/MECH-288/MECH-269/MECH-094 all landed; SD-084's persistent handle (validated 839) made this reachable. |
| Implementation completeness | **specifically absent**: no harm-valence signal AND no ranked-selection step exists in `_apply_policy_decomposition` | This is the precise, code-verified root of the C1 failure -- not ambiguous. |
| Environment adequacy | adequate | Same SD-084-lineage env as 839, already validated to produce genuine mid-execution divergence. |
| Measurement adequacy | **now adequate** (this run's own contribution) | The paired, post-divergence-window, fresh-selection-restricted statistic specifically fixes the whole-run-mean dilution problem 839's own data flagged; this is a genuinely well-powered, correctly-scoped C1 test. |
| Integration adequacy | isolated -- the two systems (threat appraisal, policy decomposition) exist but are not coupled at this junction | Precisely the gap. |
| Scale / capacity | not applicable to this finding | Not a scale issue. |

## 6. Cluster pattern

N/A -- single target.

## 7. Learning extracted

1. **A genuine, well-powered, mechanistically-interpretable dissociation**: the mid-execution abort mechanism works exactly as designed informationally (lower PE post-abort, C2 passes) but this does not translate to lower harm (C1, load-bearing, fails) -- because nothing in the redecomposition step selects among candidate re-tilings for lower harm. This is NOT ambiguous or unexplained; it is structurally guaranteed by the current implementation, which performs no ranked selection of any kind at this step.
2. **REE's fear/threat proto-emotion machinery (BLA/CeA, MECH-357/SD-058) exists and biases action choice elsewhere** (E3 candidate scoring, MECH-091's separate urgency-interrupt abort) but is not connected to MECH-321's redecomposition. MECH-288 (MECH-321's own trigger) is purely predictive-surprise-based, unrelated to hazard proximity.
3. **The hippocampal motivational payload (SD-039 `AnchorGoalPayload`) is architecturally the more natural coupling point** for "which path gets chosen" than the raw amygdala signal, but it currently carries only reward-valence (`wanting_strength`), not harm-valence -- `VALENCE_HARM_DISCRIMINATIVE` exists as a residue-field channel elsewhere but is never captured into it. And it is not wired into `_apply_policy_decomposition` regardless.
4. This is a well-localized, buildable substrate gap (not a probe-gated unknown) once specified: extend `AnchorGoalPayload`/`build_goal_payload` with a signed harm-valence field sourced from `z_harm_a`/BLA `threat_scale`, AND build an actual scoring/selection step in `_apply_policy_decomposition` to use it (currently there is no selection step of any kind to extend).

## 8. Recommended routing

**Recommended `epistemic_category`**: `competence_implementation_gap` (a specific, identified, buildable absence -- not `substrate_ceiling`, not a measurement gap; the measurement here is exemplary).

**Recommended `evidence_direction`**: `weakens` (concur with self-route) for MECH-321's harm-outcome prediction specifically, with the mechanistic (PE-reduction) half explicitly noted as supported.

**Recommended `evidence_quality_note`** (draft text for governance):
> V3-EXQ-844 (confirmed failure_autopsy_V3-EXQ-844_2026-08-01, evidence successor to V3-EXQ-839's reachability validation): MECH-321's mid-execution abort mechanism engages correctly and reduces forward-prediction-error post-abort (C2, non-load-bearing mechanistic corroboration, PASSES) -- but does not reduce actual task harm (C1, load-bearing, FAILS; -0.0033, wrong direction), using a paired post-divergence-window statistic specifically built to fix the whole-run-mean dilution problem 839's own data flagged. Code-verified root cause: `_apply_policy_decomposition` (ree_core/hippocampal/module.py:896-983) and `PolicyDecomposition.evaluate()`/`decompose_sequence()` (ree_core/policy/policy_decomposition.py:471-747) read only z_self/z_world/z_goal -- no harm-valence signal (`z_harm_a`) reaches this step, AND the step performs no ranked selection among candidate re-tilings at all (a binary decompose/keep test per candidate; all surviving tiles are additively recombined). MECH-288 (MECH-321's own trigger) is pure predictive-surprise, unrelated to hazard proximity; the substrate's actual fear/threat pathway (BLA/CeA, MECH-357/SD-058) biases action selection elsewhere (E3 scoring, the separate MECH-091 urgency-interrupt abort) but is not connected here. weakens (harm-outcome prediction specifically); the mechanistic (PE-reduction) prediction is supported. v3_pending STAYS. Route: /implement-substrate -- a harm-valence-weighted selection step in the redecomposition path (extend AnchorGoalPayload with a signed harm-valence field sourced from z_harm_a/BLA threat_scale; build an actual scoring step in _apply_policy_decomposition, which currently has none). Design phase needs a /lit-pull commission first (threat-modulated defensive path-selection literature -- e.g. Fanselow's predatory-imminence-continuum framing of graded defensive behavior selection -- to ground HOW harm-valence should shape tile selection, per the biology-before-formal-definitions convention) before implementation specifics are fixed.

**recommended_substrate_queue_entry**:
- `action`: `create` (no existing entry covers hazard-aware policy-decomposition retiling; verified against `substrate_queue.json`).
- `sd_id_suggested`: `SD-hazard-aware-policy-decomposition` (governance may rename).
- `title`: Harm-valence-weighted selection in mid-execution policy redecomposition.
- `implementation_hint`: Extend SD-039's `AnchorGoalPayload`/`build_goal_payload` with a signed harm-valence field sourced from `z_harm_a`/BLA `threat_scale` (a `VALENCE_HARM_DISCRIMINATIVE` residue-field channel already exists elsewhere but is not captured here). Build an actual ranked-selection step in `_apply_policy_decomposition` (`ree_core/hippocampal/module.py:896-983`) -- currently absent; all surviving tiles are additively recombined with no choice among them. **Prerequisite**: commission a targeted `/lit-pull` on threat-modulated defensive path-selection (e.g. Fanselow's predatory-imminence continuum, or comparable graded-defensive-response literature) before fixing the exact functional form, per biology-before-formal-definitions.
- `unblocks_claims`: [MECH-321]
- `depends_on_unresolved`: [] (all component pieces -- SD-035, MECH-357/SD-058, SD-039 -- already landed as candidate substrate)
- `priority_suggested`: 2 (one fresh, well-localized failure record; does not yet block ≥3 claims)
- `failure_record_entry`: `{run_id: v3_exq_844_..., experiment_type: v3_exq_844_mech321_r4_midexec_task_effect, metric: "C1_TASK_OUTCOME_IMPROVES measured -0.003262 vs threshold >0.0", target: "load-bearing harm-reduction criterion, currently structurally unreachable -- no selection step exists to bias"}`

**routing**: `implement-substrate` (with a `/lit-pull` prerequisite named in the implementation_hint, per user instruction -- design phase needs literature grounding "as ever").

User-confirmed at the interactive gate (2026-08-01), after a follow-up mechanistic investigation: implementation-completeness gap routing with a `recommended_substrate_queue_entry`, noting a `/lit-pull` will be needed for the design phase.
