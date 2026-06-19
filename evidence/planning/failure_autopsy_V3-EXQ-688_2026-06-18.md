# Failure Autopsy -- V3-EXQ-688 (MECH-044 hippocampal relational binding diagnostic)

- **Generated (UTC):** 2026-06-19T13:48:04Z
- **Scope:** single
- **Status:** confirmed (user-adjudicated 2026-06-19)
- **Target:** MECH-044 (`entities.hippocampal_relational_binding`, provisional, mechanism_hypothesis)
- **Runs (3 seeds, all identical early-exit):**
  - `v3_exq_688_mech044_hippocampal_relational_binding_20260618T061915Z_v3`
  - `..._20260618T061935Z_v3`
  - `..._20260618T062812Z_v3` (ree-cloud-1)
- **Outcome:** FAIL / `non_contributory`; self-route `substrate_not_ready_requeue`; flagged `precondition_unmet` by the 2026-06-18T08:04Z governance adjudication gate (blocks any governance action on MECH-044 until adjudicated).
- **Routing (confirmed):** `/queue-experiment` -> corrected successor **V3-EXQ-688a** (full fix + non-vacuity guards). NOT substrate enrichment. MECH-044 stays **provisional** (NOT weakened).

---

## 1. Facts (no interpretation)

All three seeds bailed at the P0 readiness gate (`experiments/_metrics.p0_readiness_gate` -> `P0NotReady`) and wrote the early-exit manifest from `run_experiment()` (script lines 334-354). No experiment body (P1 arms / C1-C3 criteria) ran. Recorded preconditions, identical across seeds (z_world value varies trivially seed to seed):

| Precondition (gate) | measured | threshold | direction | met |
|---|---|---|---|---|
| `z_world_discriminable` (G0) | ~0.137-0.142 | 0.10 | lower | **True** |
| `V_s_responsive` (G1) | **0.0** | 0.05 | lower | **False** |
| `boundary_events_fire` (G2) | **0.0** | 1.0 | lower | **False** |

Two of three readiness gates failed -> `P0NotReady` -> early exit. The manifests contain only `interpretation.{label, preconditions}` -- no `metrics`, no `arm_results`, no `criteria_non_degenerate`.

**Which criterion failed:** a *readiness/precondition* gate, not an absolute or discrimination criterion. The claim was never put under test.

## 2. Script + config reconstruction (`ree-v3/experiments/v3_exq_688_mech044_hippocampal_relational_binding.py`)

Pre-registered design (docstring): 3 arms x 3 seeds (INTACT / ABLATION_OFF / ABLATION_NO_ANCHORS); relational-change vs absolute-change trials; key metric `relational_sensitivity` = (boundary events on relation change - baseline) / boundary events on absolute change; criteria C1 relational_sensitivity_INTACT >= 0.5, C2 INTACT > OFF + 0.3, C3 anchor_reset_count > 0. Readiness gates G0/G1/G2 measured BEFORE the experiment on `_build_agent(use_hippocampal=True, use_anchor_sets=True)`.

**Agent config (`_build_agent`, lines 117-129):**
```python
cfg = REEConfig.from_dims(
    ..., use_hippocampal=use_hippocampal,
    use_anchor_sets=use_anchor_sets if use_hippocampal else False,
    use_event_segmenter=True if use_anchor_sets else False,
)
```
The call arms `use_hippocampal`, `use_anchor_sets`, `use_event_segmenter`. It does **NOT** pass `use_per_stream_vs=True`.

## 3. Root cause -- each failed precondition

### G1 `V_s_responsive` is a VACUOUS precondition (code-confirmed)

The probe (`_p0_readiness_checks`, lines 287-303) reads, before and after a forced large observation shift:
```python
vs_initial = agent.hippocampal.per_stream_vs.get("z_world", 1.0)
...                              # 10x random shift x10 ticks
vs_after   = agent.hippocampal.per_stream_vs.get("z_world", 1.0)
vs_change  = abs(vs_initial - vs_after)
```
`HippocampalModule.per_stream_vs` is the MECH-269 Phase-1 observable. It is populated **only** when `config.use_per_stream_vs=True`:
- `from_dims` (`ree_core/utils/config.py:4026, :4939`): `use_per_stream_vs` defaults **False**; `_build_agent` never overrides it.
- `update_per_stream_vs` (`ree_core/hippocampal/module.py:1871`): `if not getattr(self.config, "use_per_stream_vs", False): return` -- a no-op; `self.per_stream_vs` stays `{}` (initialised empty at `module.py:141`).

So both `.get("z_world", 1.0)` reads return the **literal default 1.0**, and `vs_change = |1.0 - 1.0| = 0.0` **by construction, independent of any substrate behaviour**. G1 can never pass in this config. The 0.0 is an instrumentation null, not a measurement that the MECH-269 V_s signal is unresponsive. (Identical statistic-level pattern to V3-EXQ-642's `z_block` identically-0-on-untrained-encoder.)

### G2 `boundary_events_fire` is under-stimulated (strong inference)

The MECH-288 EventSegmenter **is** armed (`use_event_segmenter=True` for ARM_INTACT; `drain_boundary_events` is callable). The probe (lines 306-321) feeds 100 ticks of plain `torch.randn(1, WORLD_OBS_DIM)` -- i.i.d. white noise -- and counts boundary events. The segmenter fires on *structured/sustained* transitions: the fast PE-threshold detector needs a sustained z-scored departure >= 0.65 with `min_segment_length` suppressing re-fires (contract C2: "silent on constant baseline, fires on 10x sustained spike"); the slow BOCPD keys on `z_goal`, which is inactive (no goal seeding). Uncorrelated noise on an **untrained** encoder produces no sustained structured boundary -> 0 events over 100 ticks. The probe stimulus is mis-designed: it should drive the segmenter with the experiment's own structured relational/absolute manipulation (or a sustained step change), not white noise.

## 4. Adjudication -- the self-route is a MISLABEL

`substrate_not_ready_requeue` asserts the MECH-269 V_s / MECH-288 boundary substrate is too coarse to support the test. That is false. The substrate was **never armed** (G1: `use_per_stream_vs` off) and **never properly stimulated** (G2: white noise vs structured transitions). This is the **V3-EXQ-642 class**: a self-route generated on an un-armed / untrained / un-stimulated substrate, masquerading as a substrate-readiness verdict. It is the `precondition_unmet` case the diagnostic-adjudication gate exists to catch -- the branch's assumption ("the substrate's V_s/boundary machinery is live and was exercised") was itself unmet, so the label mislabels the cause.

**Therefore:** NOT `substrate_ceiling`. The `non_contributory` direction stands (the run yields no evidence about MECH-044), but it carries no negative weight against the claim.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact / untested | The run never reached the C1-C3 relational-sensitivity body; the claim could not express itself. |
| Biological reference | partial | MECH-044 is biologically grounded (Olsen et al. 2012: hippocampus does online relational work in the perception-action loop). BUT the ARC-006/MECH-044/MECH-045 cluster carries a recorded *no-biology-lit-pull-at-registration* flag (claims.yaml:37558). Not the failure cause here, but a standing gap. |
| Dependency / prerequisites | missing | `use_per_stream_vs` (MECH-269 Phase 1) was not armed -- the precondition probe's dependency was absent. |
| Implementation completeness | partial (harness) | The MECH-269 / MECH-288 substrate is IMPLEMENTED and available in V3; the *experiment harness* failed to arm/stimulate it. Not a substrate gap. |
| Environment adequacy | n/a | Synthetic `_create_entity_observations`; the run never reached env-trial code. |
| Measurement adequacy | misleading | G1 reads a constant default (vacuous); G2 stimulus (white noise) cannot elicit the signal it gates on. |
| Integration adequacy | n/a | Body never ran. |
| Scale / capacity | likely insufficient (deeper) | Even with G1/G2 fixed, the agent is **untrained** and obs are **synthetic**; a random encoder yields near-trivial z_world, so the C1-C3 body risks a second vacuous result (the SD-031 / MECH-353 / V3-EXQ-642 "dimensionality is necessary, not sufficient" lesson). |

**Recommended `epistemic_category`:** leave MECH-044 at its inferred `standard` (do NOT set `substrate_ceiling`). The recommendation is harness re-issue, not substrate enrichment.

## 6. Learning extracted

1. **G1 was an instrumentation null.** A readiness gate that reads `per_stream_vs.get(..., 1.0)` while `use_per_stream_vs` is off can only ever report 0.0 change -- it tests the harness config, not the substrate. Any diagnostic whose precondition reads a flag-gated observable must arm that flag (or assert it armed) or it self-routes vacuously.
2. **G2 stimulus did not match the gated signal.** Probing a structured-transition detector with i.i.d. noise guarantees a null. Readiness probes must use the same class of stimulus the experiment body uses.
3. **The self-route was untrustworthy by construction.** Both failing preconditions were guaranteed-fail artifacts of the config, so `substrate_not_ready_requeue` carried no information about MECH-269/MECH-288 readiness -- the adjudication gate correctly held it.
4. **Deeper (carry to 688a):** an untrained agent + synthetic obs cannot fairly test relational binding even past the readiness gate; the successor needs a non-vacuity prerequisite on the C1-C3 body (e.g. trained/discriminative encoder + a verified boundary-event existence proof on the structured manipulation) so a random-encoder run self-routes honestly rather than producing a spurious PASS/FAIL.

## 7. Repair pathway (confirmed routing)

**Route: `/queue-experiment` -> V3-EXQ-688a (new letter; bug-fix to the same scientific question, MECH-044).** Full fix + non-vacuity guards (user-confirmed):

1. **Arm `use_per_stream_vs=True`** in `_build_agent` (and `per_stream_vs_streams` covering `z_world`) so G1 measures the real MECH-269 V_s signal rather than the constant default.
2. **Redesign G2** to drive the MECH-288 segmenter with the structured relational/absolute manipulation (or a sustained step change), not white noise -- so a true boundary-event count is observable.
3. **Add non-vacuity prerequisites** that fail loudly (or honestly self-route) when the substrate is un-armed or the encoder is untrained/non-discriminative: e.g. assert `per_stream_vs` is non-empty post-arm; require a boundary-event existence proof on the structured stimulus; gate the C1-C3 body on a discriminative-z_world check (guard against the random-encoder trivial-signal regime).
4. **Consider a trained/warmed encoder** (or document why an untrained module is the intended test surface) so the relational-sensitivity body is not run on noise.

**Secondary (not selected as primary):** the MECH-044 cluster's recorded no-biology-lit-pull gap (claims.yaml:37558) remains open; a `targeted_review` `/lit-pull` for hippocampal relational binding would let the claim be fairly weighted under the biology-before-formal-definitions rule. Flagged for a future pass, not blocking 688a.

**Do NOT** re-run under the same EXQ id (runner skips completed ids); use 688a. **Do NOT** edit claims.yaml / the manifest / the queue from this autopsy -- governance applies.

## 8. Governance hand-off (recommended writes; governance applies)

- MECH-044: **no status change** (stays `provisional`); **no weaken**. The 3 `non_contributory` entries carry no confidence/conflict weight (never-tested precondition_unmet).
- Recommended `evidence_quality_note` text for MECH-044 (governance to write):
  > V3-EXQ-688 (3 seeds, 2026-06-18) FAIL/non_contributory was a `precondition_unmet` vacuous self-route, NOT a substrate-readiness verdict: G1 `V_s_responsive` read `per_stream_vs.get("z_world",1.0)` while the harness left `use_per_stream_vs=False`, forcing vs_change=0.0 by construction; G2 `boundary_events_fire` fed the MECH-288 segmenter i.i.d. white noise (no structured transition) -> 0 events. MECH-269/MECH-288 substrate is implemented and available; the experiment harness simply did not arm/stimulate it. MECH-044 was never put under test. Routed to V3-EXQ-688a (arm use_per_stream_vs, structured-stimulus G2, non-vacuity + discriminative-encoder guards). NOT substrate_ceiling.
- No `substrate_queue` entry recommended (no substrate gap; the fix is harness-side).
- Optional follow-on: `/lit-pull targeted_review_<mech-044 relational binding>` (cluster no-biology-lit-pull flag).

## 9. Granularity-debt check

First `/failure-autopsy` on MECH-044 (grep of `evidence/planning/failure_autopsy_*` for 688 / mech-044 returned none). No recurrence -> no `/claim-synthesis` trigger. One autopsy is a diagnosis, not a pattern.
