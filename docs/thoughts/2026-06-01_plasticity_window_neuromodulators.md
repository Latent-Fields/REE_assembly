Status: processed

Processed in:
- (processed directly into canonical form -- this file IS the canonical framing paragraph for the plasticity-window OPENING side; deliberately unregistered per its own Status header)
- `evidence/planning/thought_intake_2026-05-21_gated_plasticity.md` + `evidence/planning/thought_intake_2026-05-04_smoothened_da_ach.md` (the plasticity-governance cluster that cites this as the ACh/PV/BDNF opening-side sibling)
- `evidence/planning/goal_pipeline_developmental_window_diagnostic_memo_2026-06-01.md`; memory `project_plasticity_window_neuromodulators`

<!-- incorporated-but-unmarked PARTIAL (sweep marker-fixup 2026-06-05); see audit in WORKSPACE_STATE.md -->

---

# Plasticity-window neuromodulators (ACh / PV-interneuron / BDNF / state-dependent gain)

**Date:** 2026-06-01
**Status:** thoughts / framing note — NOT a substrate-design memo, NOT a claim registration, NOT a closure-plan entry
**Author session:** developmental-window-followup-20260601T081500Z (originated as a side-flag during failure-autopsy V3-EXQ-622 follow-up)
**Disposition:** long-horizon V4-or-late-V3 substrate territory; do not scope into V3 unless explicitly commissioned

---

## What this is

A framing note capturing the gap between what REE currently has for plasticity-window regulation and what the biological reference mechanism actually provides. Spilling the observation into the repo so future sessions touching ACh / critical-period-closure / state-dependent learning-rate / nucleus-basalis-analog can start from a substantive paragraph rather than re-deriving the framing.

Not a plan. Not a claim. Not a substrate design.

---

## The asymmetry

REE has built the **closure side** of developmental plasticity windows:

- **INV-074** plasticity-injection crystallization (architectural commitment)
- **MECH-333** Phase-3 trainable-substrate freeze
- **MECH-334** EWC residue write-protect (Kirkpatrick et al. 2017 anchor)
- Implemented 2026-05-17 in `ree-v3/ree_core/policy/gated_policy.py` (`GatedPolicy.crystallize()` + `.expansion_parameters()`) and `ree-v3/ree_core/residue/field.py` (`ResidueField.snapshot_ewc_anchor()` + `.ewc_penalty()`). Wired through `InfantCurriculumScheduler.on_phase3_entry` fire-once hook.
- ARC-075 names "infant curriculum plasticity magnitude asymmetry" — the broader architectural framing.
- The 2026-05-17 design doc `REE_assembly/docs/architecture/critical_period_crystallization.md` covers the Nikishin 2023 / Kirkpatrick 2017 synthesis.

REE does NOT have the **opening side**:

- No basal-forebrain-analog (nucleus basalis of Meynert) gating cortical encoder learning rates.
- No state-conditional plasticity scalar (sleep stage, attention, novelty, arousal as plasticity *gain multipliers* — distinct from the *content* signals MECH-313 LC-NE tonic, MECH-104 phasic, MECH-203 5-HT carry).
- No trophic / BDNF-analog modulating window duration.
- No PV-interneuron / GABA-maturation analog gating window closure timing as a function of inhibitory tone.

What we have that is adjacent but NOT this:

| Existing substrate | What it does | What it doesn't do |
|---|---|---|
| MECH-203/204 SerotoninModule (tonic 5-HT, SR-1/SR-2/SR-3) | State regulation, sleep mode, REM zero-point capture | Doesn't multiply a learning rate; doesn't gate plasticity at encoder / E1 / E2 / residue layers |
| MECH-313 LC-NE tonic noise floor | Softmax temperature lift on E3 selection | Doesn't gate plasticity; gates choice noise |
| MECH-104 phasic LC-NE / volatility interrupt | De-commitment signal under sustained PE | Content-side, not plasticity-side |
| SD-037 broadcast override (orexin) | Drive + sustained-threat recruited; gain on goal seeding + PAG exit threshold | Doesn't gate plasticity; gates affective broadcast |
| MECH-279 PAG freeze gate | Committed motor freeze under sustained z_harm_a | Behavioural gate, not plasticity gate |
| MECH-260 dACC anti-recency | State-dependent score-bias against recently-executed action classes | Within-cortex inhibition, not basal-forebrain plasticity gate |
| MECH-090 R-c readiness conjunction | Commit entry predicate (within-tick decisiveness + across-tick motor readiness) | Behavioural gate, not plasticity gate |

The closest existing concept is the `InfantCurriculumScheduler` (`ree-v3/experiments/infant_curriculum.py`) Phase 0 → 1 → 2 → 3 transition with `on_phase3_entry` firing crystallization — but those transitions are **scheduler-driven**, not **state-gated by a neuromodulatory scalar**. The 622 staged curriculum we just analysed (S0 → S1 → S2 → S3) is the same shape: explicit phase boundaries set by episode count, not by an arousal / attention / novelty state that opens and closes plasticity gates as it does in mammalian cortex.

---

## Biological vocabulary worth bringing in eventually

Anchors for whoever picks this up:

- **Hensch 2005** *Critical period plasticity in local cortical circuits.* PV-interneuron / GABA-mediated critical-period closure. The classic reference for window onset/offset as a function of inhibitory maturation.
- **Bear & Singer 1986** *Modulation of visual cortical plasticity by acetylcholine and noradrenaline.* The original demonstration that combined ACh + NE depletion abolishes visual cortex plasticity even in animals at peak critical-period age. The single most direct evidence for ACh as a plasticity-gain modulator.
- **Froemke 2015** *Plasticity of cortical excitatory-inhibitory balance.* A1 receptive-field plasticity gated by nucleus basalis stimulation. Closest to "pair ACh with stimulus, get encoder remapping".
- **Kilgard & Merzenich 1998** *Cortical map reorganization enabled by nucleus basalis activity.* Same paradigm; broader cortex.
- **Sale et al. 2007** *Environmental enrichment in adulthood promotes amblyopia recovery through a reduction of intracortical inhibition.* Critical-period reopening via GABA reduction — analog of "turn off the crystallization" in REE terms.
- **Lehmann & Lowel 2008** *Age-dependent ocular dominance plasticity in adult mice.* The non-binary picture: windows don't close fully, they shift in gain.
- **Trachtenberg 2015** *Competition, inhibition, and critical periods of cortical plasticity.* The modern synthesis.

REE's own existing lit-pull anchors that touch adjacent territory:

- `evidence/literature/targeted_review_arc_075_infant_curriculum_plasticity_asymmetry/` (if it exists; check before citing)
- `evidence/literature/targeted_review_mech_204_rem_precision_recalibration/` (REM zero-point capture is a state-gated recalibration, related but distinct)
- The `evidence/literature/targeted_review_orexin_kinetics/` synthesis for SD-037 — orexin as an arousal-gain hub

The biological observation that motivates the framing: ACh is essentially a **per-stimulus gating signal** for which inputs the cortex should incorporate into its long-term representations. Without it (e.g. nucleus basalis lesion), animals can still perceive and respond, but their cortical representations don't update — they keep operating on the representations they had before the lesion. This is direct evidence for the architectural commitment that "plasticity ≠ activity; plasticity is a separately-gated process".

---

## What a V3 / V4 substrate cluster would look like (sketch only)

If this is ever commissioned, the natural shape is:

- **ARC-XXX** *Plasticity-window neuromodulator gating.* Architectural commitment that cortical encoder learning rates and residue-field write rates are multiplicatively gated by a state-conditional plasticity scalar, distinct from the content signals carried by LC-NE / 5-HT / orexin. State variables that drive the scalar: attention focus, novelty / surprise, arousal, developmental phase, sleep state.
- **MECH-XXX-Ach** *ACh-analog basal-forebrain plasticity gain.* Scalar in `[0, 1]` multiplying encoder learning rates and residue write magnitudes. Driven by: novelty (MECH-205 surprise EMA), attention focus (SD-032a salience coordinator current_mode), arousal (drive_level + sustained z_harm_a). Per Bear & Singer 1986 the natural pair is ACh + NE; the LC-NE pair lives at MECH-313 (tonic) + MECH-104 (phasic), so a Bear-pair instantiation might compose ACh-gate × LC-NE-gate multiplicatively.
- **MECH-XXX-PV** *PV-interneuron inhibitory maturation as window-closure clock.* Time-since-cell-onset accumulator that monotonically lowers the ceiling on plasticity gain. Hensch 2005 anchor. The biological-faithful form of the existing MECH-333 / MECH-334 closure mechanism (currently a binary phase transition).
- **MECH-XXX-BDNF** *Trophic-window-duration scalar.* Lower-priority; the duration knob on top of the gain knob.
- **Q-XXX** *Does plasticity-gain modulate identically across encoder / residue / hippocampal / E2-forward layers?* Open question on layer-specific vs unified gating. Biology says layer-specific (visual vs auditory vs somatosensory critical periods have very different timings); REE would have to decide between one global ACh scalar vs per-substrate scalars.

The V3 vs V4 boundary: a single ACh-scalar gate with a hand-tuned BDNF-duration knob is V3-tractable if scoped to ONE substrate (e.g. just the residue field, or just the LatentStack encoders). A full ACh × PV × BDNF cluster with layer-specific gain and developmental dynamics is V4 — that's where the social systems sit and where the substrate budget grows.

---

## How the current goal-pipeline diagnostic relates

The V3-EXQ-630-ish (chip spawned) 4-arm dissociation has an ARM_D that tests "writer-freeze across the transition." That arm is the **V3-conservative approximation** of what a real ACh-gated plasticity window would do: instead of an ACh scalar dropping `mech295` and `mech307` write gain to zero during the transition, the scheduler manually sets the master flags to False. If ARM_D PASSes, the conclusion is **NOT** "REE needs a full ACh / plasticity-window system." The conclusion is "scheduler-driven flag toggling at the transition is sufficient for the V3 goal-pipeline question." The ACh-system substrate work is a *separate*, *later* claim about how the toggling would be made state-conditional rather than scheduler-driven.

Do not collapse the two. Do not let an ARM_D PASS authorise V4-scope substrate work in V3.

---

## Tracking

This note is the canonical paragraph. When this cluster is eventually picked up, the substrate-design memo can cite this paragraph as the framing. Until then:

- No claim registered in `claims.yaml`.
- No entry in `substrate_queue.json`.
- No closure-map node touched.
- No /lit-pull commissioned (the references above are starting points if a lit-pull is later commissioned; do not pull pre-emptively).
- Project memory entry at `~/.claude/projects/-Users-dgolden-REE-Working/memory/project_plasticity_window_neuromodulators.md` so future sessions touching ACh / critical-period / nucleus-basalis topics surface this framing automatically.

If a future session is tempted to grow this into a substrate cluster, the gate to clear first is: **is there a concrete V3 problem this would unblock, and is the V3-conservative form (scheduler-driven flag toggles, like ARM_D above) demonstrably insufficient for it?** If yes, /lit-pull on Hensch + Bear & Singer + Froemke + Kilgard + Sale before any substrate-design memo.

---

*Author session: developmental-window-followup-20260601T081500Z. References: [INV-074 plasticity-injection crystallization design doc](../architecture/critical_period_crystallization.md), [goal_pipeline_developmental_window_diagnostic_memo_2026-06-01.md](../../evidence/planning/goal_pipeline_developmental_window_diagnostic_memo_2026-06-01.md), [failure_autopsy_V3-EXQ-622_2026-06-01.md](../../evidence/planning/failure_autopsy_V3-EXQ-622_2026-06-01.md).*
