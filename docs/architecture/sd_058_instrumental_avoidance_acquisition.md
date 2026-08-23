---
title: "SD-058: defensive_action.instrumental_avoidance_acquisition"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 16
status: candidate/v3_pending
status_asof: 2026-07-10
status_claim: SD-058
---

# SD-058: defensive_action.instrumental_avoidance_acquisition

**Claim ID:** SD-058 (architecture) + MECH-357 (mechanism)
**Subject:** `defensive_action.instrumental_avoidance_acquisition`
**Status:** IMPLEMENTED 2026-06-07 (substrate; v3_pending until the Stage-H validation EXQ PASSes)
**Registered:** 2026-06-07
**Depends on:** SD-035 (amygdala BLA/CeA analogue), MECH-279 (PAG freeze-gate), SD-011 (z_harm_a affective stream)
**Blocks:** `scaffolded_sd054_onboarding` Stage-H / P1 survival leg (goal_pipeline GAP-2);
transitively ARC-060, MECH-320, ARC-068, SD-054-readiness (all `pending_retest_after_substrate`)

> **Validation attempt 6 (2026-08-14): agent-directed hazard pursuit.** The Stage-H
> validation has failed to discriminate 5 times (603h/603k/603r static; 603s
> mobile-predator drift -> exact tie `G_H_INTACT=G_H_LESION=0.6667`; 603t SD-029
> scheduled adjacency -> LESION ceiling 1.0), each because the pressure mechanism left
> hazard motion agent-INDEPENDENT or one-shot, so no sustained Pavlovian-instrumental
> conflict formed. The 6th and final pressure candidate -- **agent-directed hazard
> pursuit** (`hazard_agent_pursuit`, built into the env by ree-v3 `39b5ca8`) -- was
> threaded into Stage-H onboarding on 2026-08-14 (session `intelligent-elgamal-222d2b`,
> `/implement-substrate`) and validation **V3-EXQ-603u** queued (603s + directedness:
> `hazard_agent_pursuit=0.9`). SD-058 stays `v3_pending` until 603u PASSes. Design +
> data-flow: [`../../evidence/planning/mech357_agent_pursuit_build_2026-08-14.md`](../../evidence/planning/mech357_agent_pursuit_build_2026-08-14.md).
> Separately, the MECH-357 avoidance-efficacy eligibility-trace leak:learn imbalance is
> tracked as its own `substrate_queue` item
> (`mech357-avoidance-efficacy-eligibility-trace-imbalance`); it does not confound the
> Stage-H window (the protective-scaffold floor covers it).

---

## Problem

The `scaffolded_sd054_onboarding` substrate-readiness probe **V3-EXQ-603g** (2026-06-07)
showed that goal **FORMATION** works (G0 stage-0 positive control 3/3; z_goal lights on
forced feed) but the **P1 survival / hazard-avoidance LEARNING leg does not train** even when
isolated as a dedicated Stage-H (G1 survival 0/3; G_H isolated-hazard 0/3 at budget;
median episode length 12.5/38.0/28.5 vs gate 75). The user adjudicated this as a **deeper
survival / aversion-learning substrate gap, not a budget/curriculum tweak**
(`failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07`).

A targeted biology lit-pull was commissioned BEFORE any further curriculum-budget iteration
(avoiding the SD-003-style "philosophy-right / mechanism-wrong, iterate the caveat" trap; see
`memory/feedback_biology_before_formal_definitions.md`). Its verdict
(`evidence/literature/targeted_review_hazard_avoidance_learning/SYNTHESIS.md`, 5 entries:
SD-035 x3 + MECH-279 + SD-054) is that the fix is **structural, not budgetary**:

- **REE already has the Pavlovian / defensive side.** SD-035 (amygdala salience: BLA encoding +
  CeA mode-prior / fast-prime) + MECH-279 (CeA->vlPAG freeze gate) give REE the defensive
  *reaction* (Tovote et al. 2016 Nature confirms MECH-279 is response EXECUTION, not learning).
- **What is MISSING is the instrumental-acquisition side.** Moscarello & LeDoux 2013
  (J Neurosci; the load-bearing **MIXED** entry) shows active avoidance learning is the
  **resolution of a Pavlovian-instrumental conflict**: the freezing reaction and the
  instrumental avoidance action are mutually exclusive, and learning to avoid **requires the
  infralimbic prefrontal cortex (ilPFC) to suppress central-amygdala-driven freezing** (ilPFC
  lesion -> more freezing, less avoidance; CeA lesion -> the opposite).
- **Avoidance is developmentally / gradually acquired under a protective scaffold.**
  Debiec & Sullivan 2017 + Thompson, Sullivan & Wilson 2008: avoidance is not an init-time
  capacity; it is gated by substrate maturation and a protective scaffold during acquisition
  (maternal HPA / CORT buffering). Turchetta et al. 2020 (NeurIPS) is the ML mirror: hazardous
  tasks become learnable under an external instructor / reset curriculum that protects during
  acquisition and is withdrawn.

A freeze-and-salience substrate with no reaction-suppression / instrumental layer is the
**ilPFC-lesion animal: it freezes instead of learning to avoid** -- precisely the 603g G_H 0/3
signature. The closest REE substrate (SD-035 / MECH-279) exists but is wired only as a salience
stage + a freeze gate, **not as a curriculum avoidance-LEARNING driver**.

---

## Solution

Two coordinated additions, both behind a single master switch (`use_instrumental_avoidance`),
all defaults no-op (bit-identical OFF). The mechanism is registered as **MECH-357**; the
architectural commitment (that REE's defensive system needs an instrumental-acquisition side,
not only a defensive-reaction side) is **SD-058**.

### (a) Instrumental-avoidance ACTION pathway

Under retained threat, the gate emits a per-candidate E3 score-bias that **penalises passivity
(the no-op / freeze class) and mildly favours directed action**, proportional to a learned
avoidance-efficacy and to the current threat level. It does NOT compute the escape direction --
E3's existing harm-forward evaluation already scores low-harm trajectories favourably; the gate's
job (per Moscarello & LeDoux) is to **release the instrumental action by suppressing the competing
freeze**, letting the existing harm gradient pick the escape among the directed candidates. This
is the missing step from *reaction* to *learned avoidance*.

### (b) ilPFC-analog freeze-SUPPRESSION gate over the MECH-279 output

A scalar `freeze_suppression` in [0, 1] reads the threat (z_harm_a) and the learned/scaffolded
avoidance-efficacy and, when above a threshold, **overrides the MECH-279 freeze no-op** so the
agent takes its selected (instrumental-avoidance) action instead of freezing. This is the direct
analogue of ilPFC top-down inhibition of CeA-driven freezing. The suppression is consulted ONLY
at the MECH-279 application site, so it is inert when `use_pag_freeze_gate=False` (the gate's
action-pathway half (a) still operates, since freezing is also expressible as a passive no-op
choice the bias penalises).

### Avoidance-efficacy learning (the acquisition; eligibility trace)

The load-bearing "acquisition" piece. The gate maintains a scalar `avoidance_efficacy` in [0, 1]
(EMA / eligibility trace), starting low (`initial_efficacy`, default 0.0 = the freeze-default of an
ilPFC-naive animal). Each tick, post-action:

```
delta = z_harm_a_prev_norm - z_harm_a_now_norm        # > 0 = harm dropped after the action
if last_action_was_directed and z_harm_a_prev_norm > threat_floor:
    if delta > efficacy_reward_floor:                 # directed action avoided harm
        avoidance_efficacy += learn_rate * (1 - avoidance_efficacy)   # credit
    else:                                             # acted but harm did not drop
        avoidance_efficacy -= leak_rate * avoidance_efficacy
elif z_harm_a_prev_norm > threat_floor:               # froze (no-op) under threat
    avoidance_efficacy -= leak_rate * avoidance_efficacy             # freezing is not credited
```

So the agent **gradually discovers that directed action avoids harm**, and the gate's authority
(both the action-bias gain and the freeze-suppression) rises with that discovery -- the
developmental / gradual acquisition Debiec & Sullivan 2017 and Thompson 2008 describe.

### Protective-scaffold anneal (the curriculum; secondary)

The maternal-buffering / Turchetta reset-curriculum analogue. The effective efficacy consumed by
both consumers is `max(avoidance_efficacy, scaffold_floor)`. The curriculum sets a non-zero
`scaffold_floor` early in acquisition (an external instructor *shows* the agent that avoidance
works -- it takes directed actions and survives long enough to generate the experience that
trains the predictive substrate) and **anneals the floor down** as competence (the measured
`avoidance_efficacy`) grows, so the agent takes over. This is the **secondary** curriculum change;
**budget escalation is explicitly NOT the primary fix** (`ready` stays false until the structural
mechanism is validated).

### Module surface

```
ree_core/pfc/infralimbic_avoidance_gate.py
    InstrumentalAvoidanceGate
    InstrumentalAvoidanceGateConfig
    InstrumentalAvoidanceGateOutput
```

Pure-arithmetic regulator (no `nn.Module`, no trained parameters, no gradient flow), mirroring the
SD-035 CeA/BLA, MECH-279 PAG, MECH-313 NoiseFloor, MECH-320 TonicVigor pattern. Lives in
`ree_core/pfc/` alongside `lateral_pfc_analog.py` (dorsolateral) and `ofc_analog.py` --
infralimbic is the third PFC subdivision analogue.

### Config surface

| Flag | Type | Default | Role |
|---|---|---|---|
| `use_instrumental_avoidance` | bool | `False` | Master switch. Default OFF = bit-identical. |
| `avoidance_learn_rate` | float | `0.05` | efficacy credit EMA rate on successful avoidance |
| `avoidance_leak_rate` | float | `0.02` | efficacy decay on freeze / failed-avoidance under threat |
| `avoidance_initial_efficacy` | float | `0.0` | freeze-default for the ilPFC-naive agent |
| `avoidance_scaffold_floor` | float | `0.0` | protective-scaffold floor (curriculum sets >0; anneals) |
| `avoidance_threat_floor` | float | `0.1` | z_harm_a norm below which there is no threat to avoid |
| `avoidance_threat_ref` | float | `0.5` | z_harm_a norm mapping to full threat_scale=1.0 |
| `avoidance_efficacy_reward_floor` | float | `1e-4` | min harm-drop counted as a successful avoidance |
| `avoidance_action_bias_gain` | float | `0.1` | gain on the directed-action / anti-passivity bias |
| `avoidance_bias_scale` | float | `0.1` | clamp on |bias| (mirrors lateral_pfc / curiosity / vigor) |
| `avoidance_suppression_threshold` | float | `0.5` | effective-efficacy*threat above which freeze is suppressed |
| `avoidance_noop_class` | int | `0` | the passive/no-op action class (matches MECH-279 / MECH-320) |

All wired through `REEConfig.from_dims` (mirrors MECH-313 / MECH-314 / MECH-320, NOT the env-only
SD-049 pattern -- this is a policy-layer regulator on the agent).

### Curriculum surface (Stage-H driver)

`scaffolded_sd054_onboarding.py` `run_hazard_avoidance` gains an optional protective-scaffold
anneal: when the agent carries an `InstrumentalAvoidanceGate` and the scaffold flag is set, the
scheduler sets `avoidance_scaffold_floor` to a high value early in Stage-H and anneals it down
linearly across the Stage-H window (knobs `scaffold_avoidance_scaffold_floor_start` /
`_end` / master `scaffold_avoidance_driver_enabled`). The gate is the avoidance-LEARNING driver:
it bootstraps the agent into taking directed avoidance actions so it (1) survives long enough to
clear the G_H survival gate and (2) generates the experience that trains E1/E2/E3 to avoid
autonomously. Budget escalation is held as the explicitly-secondary lever.

---

## Data flow

```
sense():
  encode() -> z_harm_a  (SD-011; requires use_affective_harm_stream=True)
    -> SD-035 BLA/CeA tick (defensive reaction; existing)
    -> [NEW] InstrumentalAvoidanceGate.update(z_harm_a_norm, last_action_was_directed)
             # eligibility-trace efficacy learning; one-tick lag on the outcome read

select_action():
  ... dacc / lateral_pfc / ofc / mech295 / MECH-314 curiosity / MECH-320 vigor score_bias chain ...
    -> [NEW] avoidance_bias[K] = gate.compute_action_bias(z_harm_a_norm, action_classes, noop_class)
             # +penalise no-op / -favour directed, scaled by effective_efficacy * threat_scale
    -> composed additively into dacc_score_bias (after MECH-320, before e3.select)
  e3.select(score_bias=...)
  ... MECH-279 PAG freeze block ...
    -> [NEW] if freeze_active AND gate.freeze_suppression(z_harm_a_norm) >= suppression_threshold:
             SKIP the no-op override   # ilPFC suppresses CeA-driven freezing
  -> record whether the emitted action is directed (for next-tick gate.update)
```

`z_harm_a_prev` is cached in the gate; the outcome (did harm drop after the action?) is read on the
next tick -- a one-tick lag, biologically plausible (the avoidance outcome is the just-experienced
threat change). The gate reads SD-035's affective stream (z_harm_a) as the threat signal and sits
over the MECH-279 freeze output as the thing it suppresses -- so SD-035 / MECH-279 ARE wired as the
avoidance-learning driver, the precise gap the lit verdict names.

---

## Backward compatibility

With `use_instrumental_avoidance=False` (default), `agent.instrumental_avoidance` is `None`; the
`sense()` update call, the `select_action` bias composition, and the MECH-279 suppression check are
all skipped -> bit-identical to the pre-SD-058 agent. The Stage-H curriculum anneal is gated by
`scaffold_avoidance_driver_enabled` (default False) AND requires the agent to carry the gate, so
existing experiments and the default scaffold are unaffected.

---

## Phased training

**N/A.** The gate is a pure-arithmetic regulator with no learned parameters and no gradient flow
(matching SD-035 / MECH-279 / MECH-313 / MECH-320). The "learning" is the eligibility-trace
efficacy EMA, not an encoder head -> no P0/P1/P2 latent-target phasing, no head-collapse risk. The
Stage-H scaffold IS phased training at the curriculum level (it is an additional goal-frozen
E1/E2/E3 warm-up phase); the gate shapes which actions the agent takes within it.

## MECH-094

**N/A / call-site scoped.** Both gate methods accept `simulation_mode` and are no-ops when True
(replay / DMN content must not credit avoidance-efficacy or suppress freeze on imagined outcomes),
matching the SD-035 / MECH-279 / MECH-313 / MECH-320 / MECH-353 pattern. The gate is invoked only
on the waking `sense()` / `select_action()` paths.

## Evidence-staleness (Step 8.5)

NOT triggered. `use_instrumental_avoidance` is a no-op-default flag; every existing experiment uses
the default (gate disabled), so no dependent claim's measured mechanism changes. KEEP all evidence.

---

## What this SD enables

- The `scaffolded_sd054_onboarding` Stage-H / P1 survival leg can train (the 603g G_H 0/3 blocker).
- Transitively unblocks the goal_pipeline GAP-2 retest cohort and the
  `pending_retest_after_substrate` claims gated on it: **ARC-060, MECH-320, ARC-068,
  SD-054-readiness**.

## What this SD is NOT promising

- A passing Stage-H survival readout does not by itself promote any downstream claim; it removes the
  survival-competence confound so those claims can be fairly retested.
- The gate does not invent the escape direction (ARC-007-strict-compatible): E3's existing harm
  evaluation supplies the direction; the gate only resolves the freeze-vs-act conflict.
- This is Stage-A (single-agent) avoidance acquisition only. Social / observational avoidance
  (learning to avoid from another agent's harm) is V4.

---

## Biological grounding

| Entry | Role |
|---|---|
| Moscarello & LeDoux 2013 (J Neurosci) | **Load-bearing.** Active avoidance = resolving a Pavlovian-instrumental conflict; learning REQUIRES ilPFC to suppress CeA-driven freezing. ilPFC lesion -> more freezing, less avoidance; CeA lesion -> opposite. Grounds (a) the instrumental-action pathway and (b) the ilPFC freeze-suppression gate. |
| Tovote et al. 2016 (Nature) | CeA->vlPAG disinhibition produces freezing; freeze and flight are distinct competing outputs. Confirms MECH-279 is response EXECUTION, not learning -> the acquisition layer must be added on top, not inside MECH-279. |
| Debiec & Sullivan 2017 (Neurobiol Learn Mem) | Avoidance learning is developmentally / gradually acquired, gated by amygdala maturation + parental HPA/CORT buffering. Grounds the eligibility-trace gradual acquisition + the protective-scaffold anneal. |
| Thompson, Sullivan & Wilson 2008 (Brain Res) | Inducible BLA plasticity (GABAergic-gated) appears exactly when avoidance learning becomes possible -- substrate-readiness, not budget. Grounds treating this as a structural readiness gate. |
| Turchetta et al. 2020 (NeurIPS) | ML mirror: hazardous tasks become learnable under an external instructor / reset curriculum that protects during acquisition and is withdrawn. Grounds the protective-scaffold-floor anneal shape (methods-only). |

Literature synthesis: `evidence/literature/targeted_review_hazard_avoidance_learning/SYNTHESIS.md`.

## Related claims

- **SD-035** (amygdala BLA/CeA analogue) -- the defensive-reaction salience side this builds the
  acquisition side onto.
- **MECH-279** (PAG freeze-gate) -- the freeze output the ilPFC gate suppresses.
- **SD-011** (z_harm_a affective stream) -- the threat signal the gate reads.
- **MECH-320** (tonic vigor) / **MECH-314** (structured curiosity) -- sibling policy-layer
  score-bias regulators composed in the same chain.
- **MECH-090** (commit-entry) / **MECH-091** (urgency interrupt) -- orthogonal control-state gates;
  unaffected.
- **MECH-353** (blocked-agency / z_block) -- the assert pole on a *blocked* intended action;
  distinct (z_block fires on a blocked action under retained capacity; SD-058 fires under threat to
  resolve freeze-vs-avoid). Sibling pure-arithmetic affect/defensive regulator.

Plan-of-record: `evidence/planning/sd_054_scaffolded_onboarding_substrate_design.md`,
`evidence/planning/failure_autopsy_V3-EXQ-603g-624c-651a_2026-06-07.md`,
`evidence/planning/substrate_queue.json` (`scaffolded_sd054_onboarding`).

---

## Implementation grounding corrections (2026-06-07)

Three corrections surfaced during implementation (the substrate is unchanged; these
sharpen the framing and the validation):

1. **Distinct from the reflexive escape-from-freeze levers (NOT a duplicate).**
   REE already has two reflexive escape mechanisms over the PAG freeze: **SD-037**
   `override_signal` (orexin) raises the PAG **exit threshold** on drive+sustained-threat
   (`agent.py` PAG block), and **MECH-281** lowers the **MECH-091 urgency-interrupt**
   threshold. Both are **reflexive** threat/arousal-driven escape -- they fire as a
   function of instantaneous state, not of anything learned. The ilPFC gate
   (MECH-357) is categorically different: its freeze-suppression and action-bias scale
   with a **LEARNED avoidance-efficacy** (the eligibility trace), bootstrapped by the
   protective-scaffold floor. It is the *acquisition* of an instrumental avoidance
   action by suppressing the Pavlovian reaction (Moscarello & LeDoux 2013), not a
   reflex. This is recorded as `distinct_from: [SD-037, MECH-281, MECH-091]` on SD-058
   and MECH-357 in `claims.yaml`.

2. **The load-bearing prerequisite: the harm stream was never fed.** The legacy
   `scaffolded_sd054_onboarding._train_episode` / `_eval_episode` call
   `agent.sense(obs_body, obs_world)` with **no harm args**, so `z_harm_a` (and
   `z_harm_s`) are **None across the entire curriculum**. Every harm-driven substrate
   -- MECH-279 PAG freeze, SD-035 amygdala, AND this gate -- keys on `z_harm_a` and is
   therefore **inert** in the failing curriculum: the agent navigates the hazard band
   with no threat signal at all. The fix is a new flag `scaffold_feed_harm_stream`
   (default False, bit-identical OFF) + helper `_sense_with_optional_harm` that feeds
   `harm_obs` + `harm_obs_a` into `sense()`. With it on, `z_harm_a_norm` measures
   ~0.34 in Stage-H -- enough for the gate to engage and (with tuned thresholds) for
   PAG to freeze. This is the wiring that gives the agent a threat signal to learn
   avoidance from; without it the whole defensive/acquisition stack does nothing.

3. **The validation enables PAG so the freeze-suppression is the literal,
   load-bearing mechanism.** `use_pag_freeze_gate` defaults False and the scaffold
   does not set it, so half (b) (freeze-suppression over the MECH-279 override) is
   otherwise unexercised. V3-EXQ-603h is therefore a literal Moscarello & LeDoux
   **ilPFC-lesion vs intact** design: BOTH arms have PAG (tuned to `z_harm_a` ~0.34 --
   `pag_duration_input_threshold` 0.2 < 0.34 so the duration counter accumulates,
   `pag_theta_freeze` 0.8) + the fed harm stream; the only difference is the ilPFC gate.
   ARM_LESION (PAG, no gate) freezes and cannot acquire avoidance; ARM_INTACT (PAG +
   gate + protective-scaffold driver) suppresses the freeze and acquires instrumental
   avoidance. The scaffold floor resolves the freeze->never-act->never-learn
   chicken-and-egg: it bootstraps suppression from the start so the agent acts, accrues
   avoidance experience, and the learned efficacy sustains the suppression as the floor
   anneals. A probe confirms the full chain engages once the harm stream is fed (PAG
   freezes; the gate suppresses `n_freeze_suppressed>0` and learns efficacy 0 -> ~0.6).
   Non-vacuity preconditions on 603h: PAG must freeze on the lesion arm AND the gate
   must engage+suppress on the intact arm, else `substrate_not_ready_requeue`.
