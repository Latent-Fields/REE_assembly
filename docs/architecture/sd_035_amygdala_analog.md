---
nav_exclude: true
---

# SD-035: Amygdala Analogue — BLA + CeA Salience Stage

**Claim ID:** SD-035 (substrate) + MECH-046 (CeA mode prior) + MECH-074 parent + MECH-074a-d (split children)
**Subject:** `amygdala.analog_substrate`
**Status:** candidate, v3_pending — NOT YET IMPLEMENTED
**Registered:** 2026-04-21
**Depends on:** SD-011, SD-032a, ARC-005, ARC-007, MECH-039
**Paired with:** SD-032 (cingulate integration) — SD-035 is the missing upstream stage that feeds SD-032a

---

## Problem

ree-v3 produces `z_harm_a` via `AffectiveHarmEncoder` ([ree-v3/ree_core/latent/stack.py:168](../../../ree-v3/ree_core/latent/stack.py)) and consumes it downstream in the cingulate cluster (SD-032a–e). The partial urgency interrupt at [ree-v3/ree_core/agent.py:869-886](../../../ree-v3/ree_core/agent.py) gives us a CeA-like fast pulse, and AICAnalog (SD-032c) gives us cortical urgency. But the explicit amygdala claims — MECH-046 (fast salience classification writes a mode prior) and MECH-074 (amygdala as read/write head for valenced hippocampal map) — have **no dedicated substrate**.

Before SD-035, MECH-046/074 were promised-but-unimplemented. The cingulate is downstream; it consumes what the amygdala writes. Without an upstream amygdala stage:

- There is no BLA-style **encoding-gain multiplier** on hippocampal writes under arousal.
- There is no **content-selective retrieval bias** on hippocampal readout — only a scalar-gain approximation would fit downstream, which is the named failure signature LaBar & Cabeza 2006 rule out.
- There is no **remap signal** emitted on harm-PE spikes; MECH-073's valenced map cannot reorganise under threat prediction violation.
- The fast subcortical priming channel (MECH-074c) is conflated with the cortical urgency interrupt, obscuring both.
- The CeA mode-prior write (MECH-046) has nothing that produces it; SalienceCoordinator has an unfilled peer slot.

The lit-pull (`evidence/literature/targeted_review_amygdala_analog/synthesis.md`, 8 entries across `targeted_review_connectome_mech_046` and `targeted_review_connectome_mech_074`) resolves the architecture:

- **BLA and CeA are biologically distinct subdivisions with distinct jobs.** Collapsing them is the same error as collapsing the cingulate into a single hub. The correct form is two peer modules.
- **Retrieval bias must be content-selective (per-trace weight vector), not scalar.** Scalar is a named failure signature — it cannot reproduce the central/peripheral dissociation that is the hallmark of amygdala-lesion studies (LaBar & Cabeza 2006).
- **Remap requires predictor attribution, not broadcast.** The contextual-vs-auditory dissociation in Moita 2004 (Z = -1.36 vs -0.34, p = 0.02) rules out a broadcast architecture.
- **Fast subcortical route is real (~75 ms) but bounded** (Méndez-Bértolo 2016 + Pessoa & Adolphs 2010). CeA biases a coordinator that also takes cortical input — never unilateral, always overridable.

---

## BLA / CeA split rationale

| Module | Biological analogue | Inputs | Outputs | Owns |
|---|---|---|---|---|
| BLAAnalog | Basolateral amygdala | `z_harm_a`, `z_harm_a_pred`, `hippocampal_context` | `encoding_gain` (scalar), `retrieval_bias` (per-trace weight vector), `remap_signal` (per-code binary + strength) | MECH-074a, MECH-074b, MECH-074d |
| CeAAnalog | Central amygdala | `z_harm_a`, `cue_features=None`, `escapability_hint=None` | `mode_prior` (vector over operating modes; pre-softmax additive log-odds), `fast_prime` (scalar action/candidate prior) | MECH-046, MECH-074c |

**Why two modules, not one:**

1. **Distinct latencies.** CeA fires within 1–2 sim steps (~75 ms biological); BLA operates on slower encoding/retrieval windows (minutes to days). A single tick function would have to gate both behaviours on different time constants — clearer as two modules.
2. **Distinct targets.** CeA writes to SalienceCoordinator (and indirectly to candidate generation via fast_prime). BLA writes to HippocampalModule (encoding strength, retrieval weights, remap). Collapsing them forces a crossbar that does not exist biologically and invites contamination.
3. **Distinct failure modes.** Falsification signatures for MECH-074a (encoding gain) and MECH-074d (remap) test BLA arithmetic. Falsification for MECH-046 and MECH-074c test CeA arithmetic. Splitting preserves the ability to ablate each subdivision independently in EXQs.
4. **Mirrors SD-032's pattern.** SD-032 split cingulate into five subdivisions (a–e) each as its own module. SD-035 follows the same discipline at smaller scale: two subdivisions, two modules.

---

## Subdivisions

### BLAAnalog — MECH-074a/b/d

Non-trainable arithmetic. File: `ree-v3/ree_core/amygdala/bla.py` (NEW).

**Interface:**
```python
BLAAnalog.tick(
    z_harm_a: Tensor,
    z_harm_a_pred: Tensor,
    hippocampal_context: HippocampalContext,
) -> BLAOutput
# BLAOutput fields:
#   encoding_gain: float              (MECH-074a)
#   retrieval_bias: Tensor[num_traces]   (MECH-074b; per-trace weights, NOT scalar)
#   remap_signal: Tensor[num_codes]   (MECH-074d; per-code binary with strength)
```

**Encoding gain (MECH-074a).** Inverted-U over arousal magnitude with exponential decay post-event. Defaults from Roozendaal & McGaugh 2011:

- `encoding_gain_max = 2.5` at `||z_harm_a|| ~ 0.7`
- `encoding_gain_floor = 1.0` below `||z_harm_a|| = 0.4`
- post-event window: 18000 sim steps (~30 min biological)
- half-life: 3600 sim steps (~6 min biological)

Multiplies HippocampalModule write strength at encoding time.

**Retrieval bias (MECH-074b).** Per-trace weight vector `w_i = 1 + alpha * arousal_tag_i`, with `alpha in [0.3, 1.0]`. Requires HippocampalModule to carry a per-trace `arousal_tag` field populated at encoding time. Non-transient: BLA contribution grows with trace age (amygdala-MTL connectivity increases from 20 min to 1 week, LaBar & Cabeza 2006).

**Remap signal (MECH-074d).** Fires when `||z_harm_a - z_harm_a_pred||` exceeds ~1 SD of the running harm-PE distribution **AND** a predictor-attribution head flags at least one candidate latent code. Both conditions required. Binary per-code shape; partial (~1/3) remap amplitude (Moita 2004).

### CeAAnalog — MECH-046, MECH-074c

Non-trainable arithmetic. File: `ree-v3/ree_core/amygdala/cea.py` (NEW).

**Interface:**
```python
CeAAnalog.tick(
    z_harm_a: Tensor,
    cue_features: Optional[Tensor] = None,
    escapability_hint: Optional[Tensor] = None,  # Q-036 placeholder (no-op)
) -> CeAOutput
# CeAOutput fields:
#   mode_prior: Tensor[num_modes]   (MECH-046; pre-softmax additive log-odds)
#   fast_prime: float               (MECH-074c; scalar candidate-prior pulse)
```

**Mode prior (MECH-046).** Pre-softmax additive log-odds bias on SalienceCoordinator's harm-related mode channels. Gated on `||LowFreq(z_harm_a)||_1 > theta_cea_fast`. Emits within 1–2 sim steps (~75 ms, Méndez-Bértolo 2016) of threshold crossing. Cortical AIC/dACC discriminate at ~5–10 sim steps (~400 ms); fast:slow ratio ~5:1.

**Fast prime (MECH-074c).** Distinct from `mode_prior`: a scalar pulse biasing candidate generation directly (short subcortical route, not a cortical mode write). Magnitude ceiling `|fast_prime| <= max cortical AIC/dACC log-odds adjustment`. If cortical confirmation is absent within 5–10 sim steps, `fast_prime` decays with `tau_decay in [3, 5]` sim steps toward baseline.

**Selectivity constraint.** CeA must fire on harm-affective valence, not generic arousal. Named failure: if CeA fires on arousing non-threat stimuli (e.g., arousing scenes in Méndez-Bértolo's calibration), `fast_prime` is a generic salience detector, not a CeA analogue.

---

## Config surface

Lives in `ree-v3/ree_core/utils/config.py`. Master switch `REEConfig.use_amygdala_analog=False` gates both modules (defaults make them no-ops — backward-compat requirement).

```python
@dataclass
class BLAConfig:
    enabled: bool = False                          # master switch
    encoding_gain_max: float = 2.5                 # Roozendaal 2011
    encoding_gain_arousal_threshold: float = 0.4
    encoding_gain_arousal_peak: float = 0.7
    encoding_gain_window_steps: int = 18000
    encoding_gain_half_life_steps: int = 3600
    retrieval_bias_alpha: float = 0.6              # midpoint of 0.3-1.0
    retrieval_bias_compensation: float = 0.0       # start at 0; enable 0.1-0.3 later
    retrieval_tag_at_encoding: bool = True         # required per LaBar 2006
    remap_pe_sigma_threshold: float = 1.0          # units of running PE stdev
    remap_code_fraction: float = 0.33              # Moita 2004
    remap_requires_attribution: bool = True        # Moita 2004 attribution gate

@dataclass
class CeAConfig:
    enabled: bool = False                          # master switch
    fast_route_threshold: float = 0.5              # theta_cea_fast on LowFreq(z_harm_a)
    fast_route_input_is_lowfreq: bool = True       # Mendez-Bertolo 2016
    mode_prior_log_odds_max: float = 0.8           # bounded below AIC/dACC ceiling
    fast_prime_decay_tau_steps: int = 4            # 3-5 range
    fast_prime_override_window_steps: int = 8      # 5-10 range; after, decays
    pre_softmax_additive: bool = True              # NOT post-softmax multiplicative
```

---

## Data flow

```
  AffectiveHarmEncoder ──► z_harm_a ──┬──► BLAAnalog.tick ──► BLAOutput
  (ree_core/latent/stack.py)          │                        │
                                      │                        ├─► encoding_gain  ───► HippocampalModule write
                                      │                        ├─► retrieval_bias ───► E3.select candidate reweighting
                                      │                        └─► remap_signal   ───► HippocampalModule update hook
                                      │
                                      └──► CeAAnalog.tick ──► CeAOutput
                                                               │
                                                               ├─► mode_prior     ───► SalienceCoordinator (pre-softmax additive)
                                                               └─► fast_prime     ───► candidate generation bias
```

- `agent.sense()` ticks BLAAnalog and CeAAnalog after `z_harm_a` is produced; outputs are attached to `LatentState`.
- `SalienceCoordinator.tick` accepts `mode_prior` from CeA and adds to pre-softmax logits (reuses existing API; mirror SD-032c AICAnalog wiring).
- `HippocampalModule` write path multiplies write strength by BLA `encoding_gain`; accepts `remap_signal` on its existing update hook.
- `E3.select` accepts BLA `retrieval_bias` to reweight hippocampal candidate proposals.
- Urgency interrupt at [agent.py:869-886](../../../ree-v3/ree_core/agent.py) stays inline this pass (deliberate; migration into `CeAAnalog.fast_prime` is a second pass once MECH-074c is validated).

---

## Biological grounding

Full evidence records at `evidence/literature/targeted_review_amygdala_analog/synthesis.md`. Load-bearing papers:

| Role | Paper | Confidence | Claim |
|---|---|---|---|
| BLA encoding gain | Roozendaal & McGaugh 2011 | 0.82 | MECH-074a |
| BLA retrieval bias | LaBar & Cabeza 2006 | 0.72 | MECH-074b |
| BLA remap / reconsolidation | Nader, Schafe & LeDoux 2000 | 0.80 | MECH-074d |
| BLA remap / place-cell dissociation | Moita et al 2004 | 0.78 | MECH-074d (attribution gate) |
| CeA fast route (latency) | Méndez-Bértolo et al 2016 | 0.88 | MECH-046, MECH-074c |
| CeA fast route (bounds) | Pessoa & Adolphs 2010 | 0.72 | MECH-046, MECH-074c |
| BLA canonical (pre-existing) | McGaugh 2004 | 0.82 | MECH-074 parent |
| BLA retrieval canonical (pre-existing) | Dolcos et al 2004 | — | MECH-074b |

The biology-before-formal-definitions rule (MEMORY `feedback_biology_before_formal_definitions.md`) was applied: SD-035 and MECH-074a-d were registered only after the lit-pull extracted quantitative defaults. Config values are seeded from that synthesis, not chosen a priori.

---

## Falsification signatures

### Per sub-claim

**MECH-074a (encoding gain):** Falsified if EXQ-B shows threat-context recall does not improve under BLA-modulated gain relative to gain=1, OR if neutral recall is harmed by gain>1. The inverted-U and 30-min window are the specific parametric commitments; a flat or monotone gain surface also falsifies.

**MECH-074b (retrieval bias):** Falsified if central/gist threat-associated items are NOT retrieved preferentially over peripheral/neutral items under BLA retrieval-bias ON, or if a uniform retrieval boost across all traces reproduces the same behaviour (collapses to scalar form).

**MECH-074c (CeA fast prime):** Falsified if fast_prime emits later than ~2 sim steps, OR if it fails to decay under cortical non-confirmation within the override window, OR if it fires on arousing-but-neutral stimuli (selectivity fail — indicates a generic salience detector, not a CeA analogue).

**MECH-074d (remap with attribution):** Falsified if remap_signal fires on sub-threshold PE, OR if it perturbs untagged codes uniformly (attribution gate broken), OR if remap amplitude is wholesale (closer to 100% than 33%).

**MECH-046 (CeA mode prior):** Falsified by EXQ-A if CeA-ON does not beat CeA-OFF on mode-switch latency, OR if the zeroed-prior control does not match CeA-OFF (which would show the effect runs through some pathway other than the mode prior).

### Cross-cutting (SD-035 substrate)

**Backward-compat signature:** With `use_amygdala_analog=False`, one existing EXQ (e.g. baseline CausalGridWorld run) MUST produce bit-identical metrics to the pre-SD-035 codebase. Any drift falsifies the no-op guarantee.

**Dominance signature:** CeA `fast_prime` and `mode_prior` magnitudes must stay ≤ cortical AIC/dACC ceilings. If any EXQ shows CeA outputs dominating cortical inputs (i.e., SalienceCoordinator switching modes regardless of cortical state when CeA fires), the magnitude ceilings are miscalibrated — Pessoa & Adolphs 2010 "many roads" framing is violated.

**Selectivity signature:** A calibration run on arousing-but-neutral stimuli (analogue of Méndez-Bértolo's non-face arousing scenes) must show CeA NOT firing. If it does, CeA is a generic arousal detector.

---

## Implementation plan

1. **Configs** — `BLAConfig`, `CeAConfig`, `use_amygdala_analog` master switch in `ree-v3/ree_core/utils/config.py`.
2. **Modules** — `ree-v3/ree_core/amygdala/bla.py` and `ree-v3/ree_core/amygdala/cea.py`.
3. **LatentState extension** — add optional `bla_out`, `cea_out` fields in `ree_core/latent/stack.py`; tick both in `agent.sense()` after `z_harm_a`.
4. **Wiring** — SalienceCoordinator accepts `mode_prior`; HippocampalModule accepts `encoding_gain` and `remap_signal`; E3.select accepts `retrieval_bias`; HippocampalModule grows a per-trace `arousal_tag` field (MECH-074b requirement — flagged as a broader change).
5. **Backward-compat smoke** — replay one existing EXQ with flag OFF; confirm bit-identical metrics.
6. **Activation smoke** — with flag ON and lit-pull defaults, confirm CeA `mode_prior` shifts under threat cue, BLA `encoding_gain > 1` during threat, BLA `remap_signal` fires on synthetic PE spike.
7. **CLAUDE.md entry** in `ree-v3/CLAUDE.md` (mirror SD-032c format).
8. **Experiments** — queue EXQ-A (CeA mode-prior ablation, 3 arms) and EXQ-B (BLA encoding + remap, 2 arms). MECH-074b retrieval-bias and MECH-074c fast-prime get follow-up EXQs once A/B pass.

---

## Q-036 escapability follow-up

CeAAnalog carries an `escapability_hint: Optional[Tensor] = None` parameter as a **no-op placeholder**. The parameter is accepted by `tick()` but the initial non-trainable arithmetic does not consume it. This is deliberate: when MECH-219 / Q-036 (escapability signal) lands, it can be wired in without a module-interface refactor.

Rationale for placeholder rather than full integration:
- Q-036 is not a blocker for MECH-046 / MECH-074a-d. Blocking SD-035 on it would stall the amygdala work indefinitely.
- The parametric form of escapability's contribution to CeA priming is not yet resolved (would it gate `fast_prime` amplitude? shift `mode_prior` away from defensive modes? both?). Better to defer than to guess.
- Adding the parameter now, as a no-op, costs nothing and prevents a breaking change later.

Follow-up trigger: when Q-036 is promoted to a mechanism claim with a proposed parametric form, a follow-up EXQ (TBD) will add the escapability pathway and measure behavioural differences under controllable vs uncontrollable threat.

---

## Open risks / follow-ups

1. **Per-trace arousal_tag in HippocampalModule.** MECH-074b requires HippocampalModule to carry a per-trace `arousal_tag` field that BLAAnalog writes at encoding and reads at retrieval. This is a broader wiring change than a simple multiplier. If HippocampalModule does not currently carry such a field, adding it is a sub-task of Step 4.

2. **Predictor-attribution head.** MECH-074d requires a predictor-identification step before emitting `remap_signal`. Initial pass approximates by picking codes whose contribution to the harm-PE exceeds a threshold; a learnable attribution head is a deliberate second pass.

3. **Cortical-ceiling calibration.** CeA `fast_prime` magnitude ceiling must stay ≤ max AIC/dACC log-odds adjustment. Read the current AIC ceiling from `SalienceCoordinatorConfig` and set `mode_prior_log_odds_max` accordingly; do not guess.

4. **SD-032b dACC FAIL.** `v3_exq_445` shows the affective PE path is currently underperforming. EXQ-A/B acceptance criteria must be calibrated against this — don't expect the mode-prior ablation to produce clean signals if upstream PE is broken. Flagged as a prerequisite risk, not a blocker.

5. **Learnable fear-conditioning head.** The initial pass is non-trainable arithmetic. A learnable fear-conditioning head (threat-cue → `z_harm_a` amplification with experience) is explicitly a second pass.
