# Failure Autopsy: V3-EXQ-850 (MECH-204 x SD-076 H1 discrimination probe -- diagnostic adjudication)

Generated: 2026-08-01T10:37:54Z
Status: confirmed (interactive gate completed with user)
Scope: single, diagnostic self-route flagged `precondition_unmet`

## Time-sensitive note for governance

The hypothesis space this run resolves a leg of carries an **EVB-0454 decision deadline of 2026-08-03T20:50:36Z** for SD-076 (recorded in V3-EXQ-794a's autopsy, `hypothesis_space_ledger_pending`, never previously applied to the live registry -- applied by this autopsy, see Step 9b below). That deadline is just over 2 days from this autopsy. H1 (this run) is now resolved; H2 (exposure-budget probe, V3-EXQ-853, per queue_id) has not yet run; H3 requires a `/lit-pull` commission that has not been started. Flagging this timing risk explicitly, per 794a's own `observation_bottleneck` note.

## 1. Facts

- **run_id**: `v3_exq_850_mech204_sd076_h1_f1_damping_probe_20260801T000749Z_v3`
- **queue_id**: V3-EXQ-850
- **claim_ids**: MECH-204, SD-076 (`bears_on`, `experiment_purpose: diagnostic` -- excluded from governance confidence/conflict scoring by design)
- **fanout_source**: `failure_autopsy_V3-EXQ-794a_2026-07-31.json`, hypothesis `H1-f1-recalibration-damping`
- Not a dry run (confirmed via `check_dry_run_citations.py`).

### The question
794a's full behavioural loop reached only ~half the overconfidence-reduction (rv_final) the SD-076 headroom repair's own isolated validation smoke demonstrated is achievable at the identical error scale. 794a's autopsy raised 3 rival hypotheses (H1 F1-damping / H2 insufficient exposure / H3 wrong mechanism form). This run tests H1: does F1/REM precision recalibration (ON in every arm of 794a by design necessity) partially counteract SD-076's drift, damping the observable effect relative to the F1-never-engaged smoke?

### Design
Re-runs 794a's two INFL-only cells (ARM_INFL_LO asymmetry=0.6, ARM_INFL_HI asymmetry=0.8) with EXACTLY ONE change: `use_rem_precision_recalibration=False` instead of True. Compares against two PRE-REGISTERED reference constants (not derived from this run's own statistics): `REF_794A_RV_FINAL` (F1 ON, same arms: LO=0.003998, HI=0.003870) and `SMOKE_RV_FINAL` (F1 never engaged: LO=0.002538, HI=0.002103).

### Readiness: FAILED on `dose_levels_separated` (both arms)
- `f1_recalib_disabled_confirmed_fired` / `_move`: MET (0.0 in both arms) -- the F1 ablation genuinely took effect, confirmed at the code level (WRITEBACK block gated on `use_rem_precision_recalibration`, writes nothing when False).
- `rv_live`: MET (both arms) -- rv is not dead/degenerate.
- `dose_levels_separated` ("THE 794 GATE, re-checked under F1-off"): measured `|rv_final(LO) - rv_final(HI)| = 3.21e-05` vs threshold `1e-04`. **NOT MET.** The two asymmetry doses (0.6 vs 0.8) produce essentially identical rv even with F1 disabled -- the same saturation signature 794a itself apparently showed.

Self-route: `substrate_not_ready_requeue` (evidence_direction `inconclusive`, per-claim both `unknown`). This is exactly the `precondition_unmet` self-route flagged by the indexer for adjudication.

### C1/C2 (computed but gated behind the failed precondition)
| Criterion | measured | notes |
|---|---|---|
| C1_LO_h1_f1_damping_confirmed (load-bearing) | gap_closed_frac=0.233, rv_final=0.003658 | FAIL -- did not reach smoke's range |
| C2_HI_h1_f1_damping_confirmed (load-bearing) | gap_closed_frac=0.138, rv_final=0.003626 | FAIL -- did not reach smoke's range |
| C_MONO_dose_response_direction (non-load-bearing, diagnostic only) | lo=0.003658 > hi=0.003626 | direction consistent |

**The actual F1-off vs F1-on vs smoke comparison** (the between-run test H1 is really about):
| | LO (asym=0.6) | HI (asym=0.8) |
|---|---|---|
| F1 ON (794a reference) | 0.003998 | 0.003870 |
| **F1 OFF (this run)** | **0.003658** | **0.003626** |
| Smoke (F1 never engaged) | 0.002538 | 0.002103 |

F1-off sits measurably below F1-on in BOTH arms -- in H1's predicted direction -- but closes only 14-23% of the gap to the smoke floor, far short of the driver's own confirmation bar.

## 2. Adjudication of the self-route

**The precondition IS genuinely unmet, and I concur with `substrate_not_ready_requeue` on its own terms.** `dose_levels_separated` fails by a wide margin (3.21e-05 vs a 1e-04 floor) -- this is not a borderline call. The driver's own docstring names this "THE 794 GATE, re-checked under F1-off," implying 794a's own design already treated dose-separation as a load-bearing readiness signal, and it fails identically here.

**However, two things should not be lost by a bare "requeue" label:**

1. **A real, directionally-consistent partial signal exists underneath the failed gate.** F1-off values sit measurably below F1-on reference values in both arms, in exactly the direction H1 predicts. This does not confirm H1 (the driver's own C1/C2 gap-closure criteria both explicitly fail -- only 14-23% of the gap closes, nowhere near the smoke floor) -- but it is not nothing either. It argues H1 explains SOME of 794a's shortfall, shifting weight toward H2/H3 explaining the rest, exactly as 794a's own docstring anticipated for a "not fully confirmed" H1 outcome.

2. **The `dose_levels_separated` precondition may be testing an orthogonal question to what H1 actually needs.** H1's decisive test is a BETWEEN-RUN comparison (this run's F1-off rv vs 794a's F1-on rv vs the smoke's F1-never-engaged rv) against pre-registered constants -- it does not intrinsically require the WITHIN-run asymmetry dose axis to differentiate. `dose_levels_separated` answers "does asymmetry level differentiate rv at all" -- a question this probe inherited wholesale from 794a's own C1 design (which tests dose-response, a different claim) rather than one H1's design specifically needs. Gating the informative between-run F1-comparison entirely behind a within-run dose-separation check that is orthogonal to it is arguably too strict for this specific probe's design.

## 3. Biological-reference triage

MECH-204 (broadcast correction / F1 precision recalibration) and SD-076 (asymmetric-EMA waking-confidence inflation) are both mechanism-level claims about metacognitive precision regulation. The underlying biological question -- does an offline recalibration process partially counteract waking-induced confidence drift before it's measured -- has a plausible mammalian analog (sleep-dependent recalibration of perceptual/metacognitive confidence; consistent with general sleep-homeostasis literature), though no specific citation is pinned to H1 itself in 794a's docstring. This diagnostic run does not itself carry claim weight (excluded from governance confidence/conflict scoring by `experiment_purpose: diagnostic`), so a full biological-reference table is not the load-bearing part of this adjudication -- the discrimination-portfolio mechanics are.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (diagnostic, no claim weight) | Correctly excluded from scoring; this run's job is discrimination among rival hypotheses, not claim evidence. |
| Biological reference | partial | Plausible sleep-recalibration analog; not the load-bearing layer for a diagnostic. |
| Developnetal / dependency prerequisites | present | SD-076 headroom repair (452f99e367), MECH-204 F1 precision recalibration, sws/rem sleep loop machinery all landed and confirmed engaging (manipulation check passes cleanly). |
| Implementation completeness | complete | The F1 ablation is confirmed to take effect at the code level, not just via a config flag assertion. |
| Environment adequacy | **inadequate for the dose axis specifically** | The asymmetry range (0.6-0.8) does not differentiate rv under F1-off, mirroring 794a's own apparent saturation -- the SAME dose range may simply be too narrow/high to discriminate on this axis. |
| Measurement adequacy | **gate mis-scoped for this probe's design** | `dose_levels_separated`, borrowed wholesale from 794a's dose-response design, blocks a between-run F1-on/off comparison that does not itself depend on within-run dose separation. |
| Integration adequacy | coupled, working | F1/SD-076/sleep-loop interaction is real and measurable (the partial signal exists). |
| Scale / capacity | unclear | Not testable given the gate failure; would need a redesign that decouples the two questions to assess. |

## 5. Cluster pattern

N/A -- single target, one leg of a 3-hypothesis discrimination portfolio (see Step 9b below for the other two legs' status).

## 6. Learning extracted

1. **The precondition_unmet self-route is correct on its own terms** -- `dose_levels_separated` genuinely fails, and the driver's own C1/C2 criteria (gap-closure vs the smoke) both correctly fail to confirm H1.
2. **A real, small, directionally-consistent F1-damping signal exists** underneath the failed gate -- F1-off measurably reduces rv below the F1-on reference in both arms, closing 14-23% of the gap to the smoke floor. Not sufficient to confirm H1, but rules out "F1 has zero effect."
3. **The readiness gate conflates two different questions**: whether asymmetry-dose differentiates rv (inherited from 794a's design) vs whether F1-on/off differentiates rv (what H1's between-run comparison actually needs). A redesign that separates these would let H1's decisive comparison be read cleanly even if the dose axis stays saturated.
4. **H1 is neither confirmed nor eliminated** -- it stays in the live hypothesis space (see Step 9b), with weight partially shifted toward H2/H3 per 794a's own pre-registered reading of a "not fully confirmed" H1 result.

## 7. Recommended routing

**Recommended `epistemic_category`**: `measurement_test_design_defect` (the dose-separation gate, not the substrate, is what's blocking a clean read).

**Recommended `evidence_direction`**: `inconclusive` (concur with self-route) at the run level; the H1 hypothesis-space resolution (Step 9b) captures the nuance the flat label cannot.

**Recommended `evidence_quality_note`** (draft text for governance; this is a diagnostic, so this note is informational for the MECH-204/SD-076 hypothesis-space campaign, not a claim-weight change):
> V3-EXQ-850 (confirmed failure_autopsy_V3-EXQ-850_2026-08-01, GOV-FANOUT-1 H1 leg of failure_autopsy_V3-EXQ-794a_2026-07-31's 3-hypothesis portfolio): precondition_unmet correctly flagged and correctly self-routed (dose_levels_separated fails by a wide margin -- LO/HI asymmetry doses produce near-identical rv even with F1 disabled, mirroring 794a's own apparent saturation). A real partial signal survives underneath: F1-off rv sits measurably below the F1-on reference in both arms, in H1's predicted direction, closing 14-23% of the full-loop-vs-smoke gap -- not sufficient to confirm H1 (the driver's own gap-closure criteria both fail), but rules out zero effect. H1 stays alive in the hypothesis space, weight partially shifted toward H2/H3. Recommend a requeue that decouples the dose-separation readiness check (which answers a different question than H1's between-run F1-comparison needs) from H1's actual decisive test. Time-sensitive: EVB-0454's SD-076 decision deadline is 2026-08-03T20:50:36Z; H2 (V3-EXQ-853) has not yet run and H3 needs a /lit-pull commission not yet started.

**routing**: `queue-experiment` -- redesign that separates the dose-separation question from the F1-on/off comparison (e.g. drop `dose_levels_separated` as a hard gate for an F1-focused single-dose design, or widen the asymmetry range if within-run dose differentiation is still wanted for other reasons).

User-confirmed at the interactive gate (2026-08-01): "Concur + recommend gate redesign."
