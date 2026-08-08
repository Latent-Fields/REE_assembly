# Failure Autopsy: V3-EXQ-901 (INV-051, MEL dose-rigidity sweep)

**Generated:** 2026-08-08T16:39:36Z
**Scope:** single
**Status:** confirmed (Step 8 interactive gate: user confirmed `/queue-experiment` redesign, 901a)

## 1. Facts

Run: `v3_exq_901_inv051_mel_dose_rigidity_sweep_20260808T152754Z_v3` (queue V3-EXQ-901, `experiment_purpose: evidence`, machine `ree-cloud-4`, elapsed ~2.7h, seeds `[42,123,456]`). `dry_run` confirmed false. `validate_recording.py`: OK, 0 always-core gaps (`substrate_hash`, `config`, `seeds`, `machine_class`, `elapsed_seconds` all present) — **not a recording gap**.

Note on naming: in REE, "MEL" = **Model Error Load** (aggregate daily prediction-error accumulation), not melatonin. This run's own name invites the mix-up; the correct biological anchors are synaptic-homeostasis / cognitive-arousal-and-insomnia literature, not chronobiology.

Manifest self-route: `interpretation.label: substrate_not_ready_requeue`. Four readiness preconditions gate the run before the U-shape criterion (C1) is evaluated:

| Precondition | measured | threshold | met |
|---|---|---|---|
| R1 world_forward_converged_frozen_probe | 1.0 | 0.667 | true |
| R2 mel_dose_sweep_gradient_present | 1.0 | 0.667 | true |
| R3 sleep_opportunity_uniform_across_dose | 1.0 | 0.667 | true |
| **R4 rigidity_fresh_selection_sample_adequate** | **0.0** | 0.667 | **false** |

R1-R3 all pass at 100% (world model trained, MEL dose genuinely graded, sleep opportunity structurally uniform). Only R4 fails, on all 3 seeds. R4 requires >=15 fresh (non-held/non-latched) `e3_tick` action selections per ON-arm/seed cell. Per-cell fresh-select counts: seed 42 mostly clears (11,18,16,19,16,20 -- only one cell at 11 misses); seed 123 collapses everywhere (13,7,5,**1**,3,4 -- one cell has a single fresh selection, producing a degenerate rigidity_index=1.0); seed 456 intermediate (13,11,9,17,15,17). Because R4 requires every cell to clear, one bad cell per seed poisons that seed's readiness. `criteria_non_degenerate.C1_measured_mel_gradient_present=false` and `C1_rigidity_spread_nonzero=false` are downstream of `readiness_ok=False` (the script sets `c1_gradient_present = readiness_ok and bool(ready_seeds)`), not independent findings -- C1 was never meaningfully scored, not "tested and found flat."

**Dead z_goal stream — confirmed present, confirmed NOT load-bearing.** `z_goal_stream: {ticks_total: 48576, writer_calls: 0, active_frac: 0.0, writer_defect: true, goal_state_present: true}`, matching the `pending_review.md` flag. But the driver source explicitly declares:

```
DEAD_Z_GOAL_STREAM_EXEMPT = (
    "inherited verbatim from V3-EXQ-845/718a/798a for architecture parity; "
    "wiring update_z_goal would activate the E3 goal term, E1 conditioning, "
    "and the SD-024 benefit-attractor producer, confounding the rigidity "
    "readout this experiment routes on. Knob is arm-symmetric."
)
```

This is a first-class, sanctioned opt-out recognized by `validate_experiments.py`'s static lint. The rigidity DV reads `select_action`'s live output on a fixed probe battery via E3 tick counting -- it never reads `current_z_goal`/`GoalState.is_active()`. Since z_goal is off identically in every arm, its inertness cannot bias the cross-arm comparison. **This is architecturally distinct from the V3-EXQ-626/830 canonical writer-omission defect** (a hand-rolled loop that should have called `update_z_goal` and didn't) -- it is an intentional, arm-symmetric, criteria-independent inert knob.

## 2. Claim-layer mapping

INV-051 (`docs/claims/claims.yaml`): "There exists an optimal range of daily Model Error Load (MEL): insufficient MEL produces progressive model rigidity; excessive MEL produces overload insomnia and incomplete update." `claim_type: invariant`, `invariant_type: emergent`, `emergent_from: [SD-017]`, `status: candidate`, `epistemic_category: substrate_conditional`, `depends_on: [INV-050, INV-049, SD-017, MECH-181]`.

Sibling claim INV-050 (circadian/homeostatic/MEL three-drive sleep regulation) is currently under governance HOLD (GFLAG-0002, 2026-08-07) pending independent evidence beyond the 845/861/861a pseudo-replicated seed set. Not a blocker for V3-EXQ-901, which was purpose-built as the first >=3-level graded MEL-dose sweep with a pre-registered rigidity DV (prior runs only tested a high-vs-low contrast scoring consolidation *amount*, not rigidity/U-shape).

Not tested fairly -- the manifest's own self-route (`substrate_not_ready_requeue`) is correct on independent inspection: the readiness gate that would let C1 evaluate the U-shape never cleared.

## 3. Biological-reference triage

Already lit-pulled (`evidence/literature/targeted_review_inv_051/`, 2026-04-06, `lit_status: present`):

- **Tononi & Cirelli 2006 (Synaptic Homeostasis Hypothesis)** -- waking = net synaptic potentiation proportional to learning/PE load; SWA renormalizes it, scaled to prior waking load. Maps onto the under-stimulation pole (low MEL -> weak SWA drive -> entrenchment).
- **Harvey 2002 (cognitive model of insomnia)** -- pre-sleep cognitive arousal prevents cortical quiescence despite adequate sleep opportunity. Maps onto the overload pole, with a noted specificity gap (Harvey's mechanism is secondary sleep-anxiety, not primary MEL-overflow).

Not a formal-definition import -- MEL is grounded via SHY's "potentiation proportional to learning load" framing, not an ungrounded formal construct. No `/lit-pull` commission warranted; the one real biology gap (MECH-178 noradrenergic/hyperarousal, no NA/cortisol substrate) is already correctly scoped out of INV-051's own falsifier.

The FAIL is not biology-shaped -- it is an instrumentation sample-size shortfall in the rigidity readout, orthogonal to the biological mechanism under test.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (untested) | Never reached the C1 U-shape test; readiness gate blocked evaluation. |
| Biological reference | clear | SHY + Harvey cognitive-insomnia, both lit-pulled and mapped; MECH-178 NA gap correctly scoped out. |
| Prerequisites | present | SD-017 stable; MEL producer/consumer built+validated (798a); depends_on satisfied. |
| Implementation completeness | complete (mechanism) / partial (instrumentation) | MEL producer/consumer/sleep-loop pipeline complete (R1-R3 pass 100%); E3-fresh-selection tally under-provisioned. |
| Environment | adequate | 5-level graded world_rule_shift ladder validated (798a); gradient genuinely present, sleep opportunity uniform. |
| Measurement | **under-instrumented — root cause** | R4 (>=15 fresh selections/cell) fails all 3 seeds; several cells rest on 1-5 fresh selections (one cell n=1, degenerate rigidity_index=1.0). PROBE_EPISODES already doubled (3->6) this session, still insufficient, unevenly (2%-16% of executed ticks). |
| Integration | coupled, working | R1-R3 all clearing shows the pipeline integrates correctly; defect isolated to the probe-battery sampling step. |
| Scale/capacity | likely insufficient | Probe budget needs enlarging, or a design guaranteeing N fresh selections directly rather than sampling-until-budget-exhausted. |

**Recording-debt vs measurement-debt: this is measurement-debt, not recording-debt.** The fresh e3_tick selections genuinely did not occur in sufficient number at run time -- nothing was computed-but-discarded. The fix is a probe-budget/design change, not a re-run with better bookkeeping.

## 5. Recommended epistemic_category / evidence_direction / evidence_quality_note

`epistemic_category: precondition_unmet` (not `substrate_ceiling`, not a recording gap -- the canonical shape the skill's own key rules cite, V3-EXQ-642: a readiness precondition, not the claim's own criterion, is what failed, and the script's own self-route already correctly names it). `evidence_direction: non_contributory` (confirms manifest's own value).

> V3-EXQ-901 FAIL is non-contributory to INV-051. Readiness precondition R4 (rigidity_fresh_selection_sample_adequate -- >=15 fresh e3_tick selections per ON-arm/seed) failed on 0/3 seeds; several cells rest on as few as 1-5 fresh selections, so the primary rigidity DV cannot be trusted and C1 was never meaningfully scored. R1-R3 (world-model convergence, MEL-dose gradient, sleep-opportunity uniformity) all cleared at 100%, so this is a probe-budget/measurement-design shortfall in the driver, not a substrate limitation. This manifest also carries pending_review.md's "Dead z_goal stream" flag (writer_calls=0, active_frac=0.0) -- confirmed, by autopsy read of the driver source (DEAD_Z_GOAL_STREAM_EXEMPT), to be an intentional, arm-symmetric, criteria-independent inertness (rigidity_index is read from select_action's live probe-battery output, never gated on z_goal/GoalState), not a writer-call omission bug. It does not affect this adjudication and should be marked reviewed/exempt rather than left open. INV-051 remains candidate/substrate_conditional, still untested for its core U-shape prediction. Route: /queue-experiment same-question redesign (V3-EXQ-901a) with a materially enlarged or redesigned probe-sampling budget sufficient to clear R4 on >=2/3 seeds.

## 6. Recommended routing — CONFIRMED /queue-experiment redesign (901a)

Not a recording gap (recording complete) and not `/implement-substrate` (no substrate defect -- R1-R3 all pass, mechanism works). This is the "measurement/environment/test-design gap" row -> `/queue-experiment`, same-question alphabetic-suffix re-run.

Concrete redesign direction for the successor session:
- Materially enlarge `PROBE_EPISODES` (6 was already 2x the original 3; seed-123's shortfall (fresh-selects as low as 1) suggests another 2-4x, or a seed-adaptive/until-N-fresh sampling loop rather than a fixed episode count).
- Consider whether `e3_tick` cadence can be safely tightened during the probe only (not training) to raise fresh-selection rate without confounding what's measured.
- Investigate why fresh-select yield is so seed/arm-dependent (2%-16% of executed ticks) -- may indicate hold-latching interacts with policy confidence/entropy in a way worth understanding before re-running blind (worth a look, not a blocker).

No `recommended_substrate_queue_entry` -- driver-side, not substrate-side (`action: none`). `severity`/`substrate_paths` left unset -- this defect hasn't corrupted any *other* experiment's evidence (R4 is new to this driver, correctly self-detected before a bad conclusion was drawn).

**Re-derive brake:** N/A -- first-ever autopsy target for INV-051 (0 tagging targets). **fanout_recommendation:** N/A -- single readiness-gate FAIL, not a discrimination among live hypotheses.

## 7. Learning extracted

- The R4 sample-size floor (added this session, following the hold-weighted-E3-readout pseudo-replication fix) is working exactly as designed -- it caught a genuine under-powered readout before a spurious C1 result could be reported (seed-123 arm-3, n=1 fresh selection, rigidity_index=1.0, is the sharpest illustration).
- "MEL" in REE = Model Error Load, not melatonin -- worth flagging given the run's own name.
- A deliberately-inert z_goal stream is a legitimate, first-class design pattern (`DEAD_Z_GOAL_STREAM_EXEMPT`); the mechanical `pending_review.md` flag correctly cannot distinguish it from a genuine writer-omission defect -- that distinction is exactly this autopsy step's job, confirmed here.
- Probe-budget sizing against a fresh-selection floor is a nontrivial design problem -- doubling episode count was a reasonable first correction but insufficient, and the shortfall is unevenly distributed across seeds/arms, so a flat episode-count increase may not be the most efficient fix; an adaptive "sample until N fresh selections" loop would directly target the actual constraint.

## 8. Systemic vs one-off

The defect *class* (E3 hold-weighted pseudo-replication -- counting held/latched action repeats as independent samples) is systemic and already being actively addressed elsewhere in the corpus (MECH-321/MECH-448 lineage: v3_exq_689i, 816b, 816d, 820 already carry similar fresh-selection floors). This specific FAIL -- the probe budget being too small to clear the floor -- appears local to V3-EXQ-901's own design; no other current INV-05x/MEL-lineage experiment uses this rigidity-DV + E3-fresh-tick-gated combination. Worth a light check when 901a's redesign lands: if the fresh-select-yield variance pattern recurs, it may point to something more general about hold-latching behaviour worth documenting for the other four E3-fresh-tick-gated drivers -- speculative, not confirmed here.
