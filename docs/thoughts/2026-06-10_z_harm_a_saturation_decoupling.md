# Thought Intake: z_harm_a (affective suffering stream) saturates high and decouples from current safety

## Working title

**The affective harm stream (z_harm_a / SD-011) reads as chronic saturated suffering — magnitude without functional range, decoupled from (even inverted vs) instantaneous safety**

## Status

Status: processed

Processed in:
- registered 2026-08-01 (REE_assembly origin/master 58ab5d11db) by session cool-sutherland-623d3f, from the intake `evidence/planning/thought_intake_2026-06-10_z_harm_a_saturation_decoupling.md` written 2026-07-21 by confident-pare-9273f1.
- Candidate 1 -> **SD-086** (z_harm_a functional readout must be a calibrated scalar, not the latent norm).
- Candidate 2 -> **SD-087** (SD-020's stable reading is flag-on-scoped, not default-trained agents), plus a `default_off_scope_note` annotation on **SD-020**.
- Candidate 3 -> **Q-086** (environment-confound control: ecological vs representational saturation).
- Candidate 4 -> `readout_precondition_note` annotations on **SD-050** and **MECH-302** (registered as a precondition, not an independent claim, per the intake).
- Candidate 5 -> scope tag (raw-warmup / curriculum-conditional) carried on SD-086/SD-087/Q-086, not a standalone claim.
The two confound/flag experiments (SD-087 OFF-vs-ON, Q-086 gentler-environment) are queue-experiment follow-on, to run via /queue-experiment.

Trigger: surfaced by the V3-EXQ-664 affective fishtank showcase (2026-06-10). Watching the replay, the "suffering" channel reads pegged-high essentially all the time. Quantifying it exposed something more specific than "high": the affective stream is saturated AND mis-signed relative to safety. This is the embodied-visualisation value-add (cf. `feedback_whimsy_visualization` — the viz surfaced a representational pathology faster than the scalar metrics did).

## The observation (data)

From the V3-EXQ-664 episode log (`evidence/experiments/v3_exq_664_affective_fishtank_showcase/...112808Z_episode_log.json`), the agent runs the 524 reef stack + the affective register (SD-010/011/019a/021, MECH-279/307/320/353, SD-037). Pooling all 378 eval steps across 3 seeds:

- **z_harm_a (affective / C-fibre suffering, SD-011):** mean **6.49**, range 4.42-7.42, std 1.03, CoV ~16%. Within any single episode the range is tiny (e.g. seed-0 episode: 7.18-7.42) -> it sits at a high, near-flat saturated baseline. (The fishtank bar pegged at 100% until the viz was switched to within-episode min-max scaling on 2026-06-10; the numeric value still reads ~7.4.)
- **By behavioural mode** (this is the striking part): `shelter` (safe reef) = **7.25**, `avoid` = 6.26, `freeze` = 5.79. Suffering is **highest when the agent is sheltering / safest**.
- **By harm event:** on steps where harm actually landed, z_harm_a mean = **5.97**; on non-harm steps = **6.76**. Suffering is *slightly lower* on the steps where harm occurs.
- **Contrast with the faster tiers (which behave correctly):** sensory z_harm_s mean 0.42, CoV **41.5%**, low baseline, tracks threat; unpleasantness z_harm_un mean 0.76, CoV 18.6%, intermediate.

So the three-tier cascade is doing its *timescale* job (fast tier tracks, slow tier integrates), but the slow affective tier is (a) saturated near a ceiling, (b) magnitude-dominated (its norm carries a large near-constant component, so the absolute level is not a faithful "suffering level"), and (c) functionally decoupled from — even inverted against — current safety.

## Interpretation (two stacked effects)

1. **Faithful chronic-stress component.** z_harm_a is an EMA accumulator of harm history (SD-011 second source: `harm_history`; C-fibre analog). In the relentlessly punishing reef env (`num_hazards=4`, `hazard_food_attraction=0.7`, proximity harm) it integrates harm and never decays enough to recover, so "chronic high suffering" is partly real and is plausibly *why* the agent keeps fleeing to the reef (it shelters because accumulated affective load is high, not because instantaneous threat is) — that is also why `shelter` shows the highest z_harm_a: shelter happens *after* a rough patch, when the accumulator is high.

2. **Calibration / representation pathology.** The readout is the **norm** of the trained z_harm_a latent, which is dominated by a large near-constant encoder component, so most of the 6.5 is offset, not signal. The functional part is small and mis-signed. This is the same **magnitude-without-dynamic-range** shape flagged by `project_candidate_differentiated_affective_gradients` / V3-EXQ-643 ("the modulatory signal had magnitude but zero cross-candidate range") — here it is zero (or inverted) *cross-state* range rather than cross-candidate.

The net: as currently encoded + read, z_harm_a is a poor "suffering" scalar. It cannot carve behaviour by suffering level because the level barely moves and points the wrong way w.r.t. safety.

## Candidate directions (not yet claims — for intake adjudication)

- **Decay / recovery window.** The accumulator never recovers in a chronic-threat env. Does z_harm_a need a faster decay, an active relief-driven reset (cf. MECH-302 SufferingDerivativeComparator / SD-050, which already fires on suffering descent), or a homeostatic set-point it relaxes toward during shelter? The relief comparator exists but z_harm_a clearly is not being pulled down by it here.
- **Readout != raw norm.** A faithful suffering scalar may need a trained / calibrated affective *valuation* (a learned scalar head off z_harm_a) rather than the latent norm — the norm conflates a large constant offset with the small functional signal. Parallel to how benefit/harm are read via trained eval heads, not latent norms.
- **Dynamic-range / safety-coupling.** The inversion vs safety (highest in shelter, lower on harm) suggests z_harm_a is not coupled to the safety-prediction substrate (MECH-303/304 / SD-051/052) or to descending modulation (SD-021, which only gates z_harm_s, not z_harm_a). Should the affective stream be modulated by conditioned/contextual safety so it can relax when safe?
- **Env confound to rule out.** Re-check on a gentler env (lower hazard density / `hazard_food_attraction`) to separate "faithful chronic suffering in a brutal env" from "saturated regardless of env". If z_harm_a still pegs high in a benign env, it is calibration, not ecology.

## Scope caveat (material)

This finding is from a **non-curriculum** agent. V3-EXQ-664 trains only a ~50-episode
524-style warmup (E1 prediction + E2.world_forward MSE + E3.harm_eval_head + encoder aux
losses: SD-018 resource-proximity, SD-011 harm-accum). It does **not** run the
`scaffolded_sd054_onboarding` curriculum, and crucially does **not** enable
`scaffold_train_harm_pathway` (the 603i/603k harm-pathway co-training that trains the
z_harm_a affective encoder + E3 harm-eval + z_world on the hazard-proximity / accumulated-harm
labels). So:

- The flat z_goal / wanting channel is **expected** here — the scaffolded onboarding is what
  seeds and matures z_goal; this agent never received it (goal-pipeline gap, not a viz issue).
- The z_harm_a saturation / safety-decoupling reported above is a property of the **raw-warmup**
  encoder. Under harm-pathway training the z_harm_a affective stream is co-trained on
  accumulated-harm with the encoder, which could change the saturation magnitude and the
  safety-coupling. **Re-check under the curriculum + harm-pathway training before treating the
  saturation/inversion as a substrate property of the developmentally-trained agent.** A
  curriculum-trained affective showcase variant is the right vehicle for that comparison.

## Cross-references (depends_on candidates for intake)

- SD-011 (dual nociceptive streams; z_harm_a is the affective/accumulator stream) — the substrate under examination.
- SD-019a / z_harm_un (middle tier; behaves correctly) and SD-010 / z_harm_s (fast tier; tracks) — the contrast that localises the issue to the slow tier.
- SD-021 (descending modulation gates z_harm_s only; z_harm_a explicitly persists) — relevant to whether z_harm_a *should* be relaxable.
- MECH-302 / SD-050 (suffering-derivative comparator — relief on z_harm_a descent) and MECH-303/304 / SD-051/052 (safety prediction) — candidate couplings that would let suffering recover when safe.
- V3-EXQ-643 / `project_candidate_differentiated_affective_gradients` (magnitude-without-range affect pathology) — the same shape, cross-state here.
- ARC-016 (precision / variance gating) — z_harm_a feeds E3 commit gating as motivational urgency; a saturated z_harm_a means that urgency signal is near-constant.

## Provenance

Fishtank viz (`fishtank_viz.html` v2026-06-10.2) now renders the nociceptive-cascade bars min-max-scaled within the episode so the small dynamics are visible while the numeric value reports the absolute (saturated) level — the change that made this finding legible at a glance.
