# Self-Attribution Per Reafferent Stream

**Registered:** 2026-04-18
**Status:** Active roadmap document. Supersedes the narrow SD-003 counterfactual architecture.

---

## Summary

Self-attribution in REE is implemented by a **single-pass forward-model comparator**
applied independently to each reafferent latent stream. One general mechanism
(MECH-256) over three stream-specific substrate instantiations (SD-029 active,
SD-030 / SD-031 V4-deferred). The same forward model per stream is read in two
modes (MECH-257): retrospective comparator (attribution) and prospective
rollout-scoring (evaluation), arbitrated by a controller signal.

This structure is a deliberate restructuring of the retired two-pass
counterfactual architecture (SD-003, 28 FAILs), grounded in a three-pull
literature synthesis (2026-04-18, 14 entries across comparator / evaluator /
mode-distinction).

---

## Claim Topology

| Claim    | Scope                                                    | Status    | Phase | Doc |
|----------|----------------------------------------------------------|-----------|-------|-----|
| MECH-256 | General comparator mechanism, stream-agnostic            | candidate | V3    | this doc |
| MECH-257 | Dual-function (comparator vs evaluator), gated readout   | candidate | V3    | this doc |
| SD-029   | z_harm_s comparator (active V3 implementation)           | candidate | V3    | [arc_033_e2_harm_s_forward_model.md](arc_033_e2_harm_s_forward_model.md) |
| SD-030   | z_self comparator (motor-proprioceptive)                 | candidate | V4    | [sd_030_e2_self_forward_model.md](sd_030_e2_self_forward_model.md) |
| SD-031   | z_world comparator (causal footprint)                    | candidate | V4    | [sd_031_e2_world_forward_model.md](sd_031_e2_world_forward_model.md) |

SD-003 is superseded by MECH-256 + SD-029 as of 2026-04-18.

---

## The General Mechanism (MECH-256)

For any reafferent latent stream `z_x` with an efference-copy-driven forward
model `E2_x`:

```
predicted_z_x = E2_x(z_x_{t-1}, a_actual)
residual_z_x  = z_x_observed - predicted_z_x
causal_sig    = f(residual_z_x, context)
```

**One forward pass.** No counterfactual branch. No `E2(a_cf)` call. The
forward prediction on the actually-taken action is the reference; the
residual **is** the agency signal.

Self-caused events produce attenuated residuals (the prediction succeeds);
externally-caused events produce large residuals (the prediction fails).
Shergill 2003 measures this attenuation at roughly 50% on the force-matching
task -- partial, not binary.

---

## Per-Stream Substrates

The computational mechanism is uniform across streams; the substrates are
stream-specific, matching the anatomical organisation of biological agency
attribution:

| Stream     | Substrate         | Biology                                                                          |
|------------|-------------------|----------------------------------------------------------------------------------|
| z_harm_s   | E2_harm_s         | ACC / insula (nociceptive self-vs-other attribution); descending pain modulation |
| z_self     | E2_self (V4)      | Cerebellum (Wolpert/Miall/Ito); S1/S2 cancellation (Blakemore tickle)            |
| z_world    | E2_world (V4)     | Parietal outcome prediction; colliculus / MD-thalamus corollary discharge        |

Other biological streams (oculomotor, vocal, electrosensory) share the same
computational template but are not part of the current REE agent's
sensorimotor envelope.

---

## Dual-Function Reading (MECH-257)

Each `E2_x` is a single substrate read in two modes:

**Mode 1 — Retrospective comparator (attribution, post-action):**
```
residual = z_x_observed - E2_x(z_x_{t-1}, a_actual)
```

**Mode 2 — Prospective rollout-scoring (evaluation, pre-action):**
```
for each candidate action a_i:
    predicted_trajectory = E2_x-rollout(z_x_t, a_i, horizon=k)
    value(a_i) = f(predicted_trajectory)
```

Same learned weights. A controller signal arbitrates mode. V3 candidate for
the gating signal: commitment boundary / MECH-094 hypothesis tag. V4
candidates: dACC EVC (Shenhav 2013/2016) or heartbeat-phase gating (ARC-023).

Biological precedent is strongest in the hippocampus: Diba & Buzsaki 2007
and Dragoi & Tonegawa 2011 show one CA1 population expressing forward
(preplay) and reverse (replay) sequences within a single session, phase-
governed. Mattar & Daw 2018 gives a single prioritized-memory-access
algorithm that produces both forward planning and reverse credit assignment
traversals over a shared forward model.

---

## V3 Implementation Target (SD-029)

**PASS criteria (event-conditioned, not mean-over-all-steps):**

- **C1:** `forward_r2(E2_harm_s) >= 0.9` on the reafferent z_harm_s stream.
- **C2:** Residual magnitude partially attenuated for self-caused vs
  externally-caused harm events (Shergill partial-attenuation pattern,
  not a binary gate).
- **C3:** Residual signal-to-noise above threshold on **approach-to-harm
  events specifically**. Event-conditioned, not mean over all steps --
  this was the lesson from EXQ-431, where mean cf_gap was uninformative
  because agent-caused hazard events were sample-starved (counts 1 / 156 / 2
  across seeds 42 / 7 / 13).

**Training requirement (SD-013):** E2_harm_s must see counterfactual
perturbations during training to learn `P(z_harm_s | do(a))` rather than the
correlational `P(z_harm_s | z_t, a)`. Pure observational training produces a
biased causal signal in confounded states.

---

## Why SD-003 Was Superseded

Three accumulating reasons led to the supersession decision:

1. **Empirical:** 28 FAILs accumulated across V2+V3 iterations with no PASS
   on the two-pass counterfactual architecture since the z_world → z_harm_s
   stream migration. EXQ-030b's original PASS was on the (now-retired)
   z_world pipeline.

2. **Biological:** The three-pull 2026-04-18 synthesis (Frith 2000,
   Shergill 2003, Blakemore 1998, Haggard 2017) directly evidences a
   single-pass comparator; the two-pass counterfactual extension has no
   direct biological precedent. The earlier evidence_quality_note on SD-003
   had already flagged this as a caveat; the supersession accepts the
   caveat as load-bearing.

3. **Architectural:** Mean-cf-gap metrics drowned the rare high-signal
   approach-to-harm states; the single-pass comparator's signal structure
   is event-shaped rather than mean-shaped, which aligns with the
   event-density controls that EXQ-431 showed were required.

The ARC-033 E2_harm_s substrate is carried forward unchanged; it is the
concrete forward model SD-029 runs on. SD-003's evidence chain (EXQ-030b,
115, 166a, 195, 353, 431) remains in the historical record but does not
accrue to SD-029 without re-analysis.

---

## First Test for SD-029

Event-conditioned reanalysis of EXQ-330a traces against approach-to-harm
events. If the existing traces include sufficient reafference + action data,
no new run is required; the analysis is a manifest post-processor. If the
sample density is insufficient, a short re-run with event-density controls
(guaranteed minimum agent-caused-hazard events per seed) is queued.

## Curriculum Substrate (2026-04-21)

The balanced-hazard-event curriculum required for C3/C4 is now implemented as
an opt-in env augmentation in `CausalGridWorldV2`:
`scheduled_external_hazard_enabled=True` with `_interval`, `_prob`,
`_adjacent_only` sub-knobs. Disabled by default so all legacy experiments run
unchanged. See `ree-v3/CLAUDE.md` section "SD-029: Balanced Hazard-Event
Curriculum (2026-04-21)" for the full data flow. The first validation experiment
is V3-EXQ-470.

**Status: SD-029 substrate IMPLEMENTED 2026-04-21** -- the forward model
(ARC-033) and interventional training (SD-013) were already in place; the
curriculum gap was the last substrate blocker. Remaining work is experimental
(validate C3/C4 under the new curriculum).

---

## Open Questions

1. **Dual-function falsifiability test:** does training E2_x jointly for
   comparator + evaluator degrade mode-specific performance relative to
   mode-split baselines? Requires an ablation experiment not yet queued.
2. **Nociceptive transfer:** the canonical comparator literature is on
   sensorimotor/tactile/force streams. Extension to nociceptive streams is
   plausible (PAG/RVM descending modulation shares the efference-copy
   structure) but not directly demonstrated. This is the main mapping risk
   for SD-029.
3. **Arbitrator identity:** what biological substrate houses the controller
   signal that gates comparator vs evaluator mode? dACC (Shenhav EVC) and
   heartbeat phase (ARC-023) are the two V3/V4 candidates.

---

## References

Full literature entries:
- `evidence/literature/targeted_review_sd003_successor_comparator/entries/` (4)
- `evidence/literature/targeted_review_sd003_successor_evaluator/entries/` (5)
- `evidence/literature/targeted_review_e2_dual_function_mode_distinction/entries/` (5)

Legacy architecture (retained for diff):
- `docs/architecture/sd_003_experiment_design.md` -- the retired two-pass design.
