# Anticipatory affect: conjunction architecture (MECH-307) vs SD-014 6-channel amendment

**Created:** 2026-05-08
**Type:** architecture proposal + comparative analysis
**Status:** MECH-307 registered as candidate / v3_pending; SD-014 amendment proposed but not yet applied to registry pending MECH-307 experimental outcome.
**Anchors:** `evidence/literature/targeted_review_excitement_5th_valence_channel/` (9 entries, lit_conf 0.77); `evidence/literature/wanting_liking_sleep_consolidation_synthesis.md`; `mech188_vs_mech295_dual_path.md`.

## The architectural question

The 2026-05-08 lit-pull on excitement-as-distinct-affect established that anticipatory
positive arousal at reward cues (NAcc-anticipation in Knutson 2001a et seq.) is neurally
dissociable from VALENCE_WANTING (directional motivation), VALENCE_LIKING (consummatory
hedonic), and z_beta arousal (timing modulation). The lit-pull's naive verdict was
**REGISTER VALENCE_EXCITEMENT** as a 5th channel in SD-014's residue valence vector.

On code-level inspection, a more parsimonious answer emerged: excitement *should* fall out
of the existing 4 channels as a derived conjunction-state, but currently does not, because
of four specific wiring gaps. Fixing the wiring is more biologically faithful than adding
a new channel — biology does not have a "VALENCE_EXCITEMENT neuron type"; the excitement
signal measured in NAcc fMRI is the anatomical convergence of DA RPE + hippocampal
preplay + ANS arousal at one structure.

This document records both proposals, their relationship, and the empirical test that
adjudicates between them.

## The four wiring gaps (MECH-307 first-line proposal)

### Gap 1: VALENCE_SURPRISE is unsigned magnitude

**Code:** [`agent.py:3075-3077`](../../../ree-v3/ree_core/agent.py#L3075-L3077):

```python
pe_mag = float(pe_val.detach())                            # magnitude only
self._pe_ema = (1 - self._pe_ema_alpha) * self._pe_ema + self._pe_ema_alpha * pe_mag
surprise = max(0.0, pe_mag - self._pe_ema)                 # max(0, ...) -- non-negative
```

A positive PE (good thing happened unexpectedly — the dopamine RPE that underlies excitement
in biology) and a negative PE (bad thing happened unexpectedly — the habenula signature of
dread) are written identically to VALENCE_SURPRISE. The sign is discarded at the write site.
There is no way for any downstream consumer to distinguish "joy at unexpected reward" from
"panic at unexpected harm" by reading the residue field.

**Fix:** Either (a) store signed PE in VALENCE_SURPRISE (negative for negative PE, positive
for positive PE), with consumers reading sign or magnitude as needed; or (b) split into
VALENCE_POSITIVE_SURPRISE and VALENCE_NEGATIVE_SURPRISE as separate channels.

Option (a) is cheaper (~5 lines, one field semantics change behind a config flag
`config.surprise_signed`) and preserves backward compatibility (consumers reading magnitude
get the same behaviour as today via `abs()`). Option (b) is cleaner but more disruptive.
Recommend (a) as default; (b) only if a downstream consumer needs the channel-level
separation.

### Gap 2: MECH-216 schema readout writes only to VALENCE_WANTING

**Code:** [`agent.py:3753-3757`](../../../ree-v3/ree_core/agent.py#L3753-L3757):

```python
self.residue_field.update_valence(
    z_world, component=VALENCE_WANTING,
    value=wanting_value, hypothesis_tag=False,
)
```

When `schema_salience` fires above threshold, the schema readout produces a single write —
to VALENCE_WANTING only. Biology's NAcc-anticipation signal at reward cues drives, *jointly*:
(i) wanting amplification (already done), (ii) sympathetic activation through ANS pathways
(z_beta arousal should rise — currently absent), and (iii) partial anticipatory hedonic
activation (a VALENCE_LIKING write before contact — currently absent). MECH-216 currently
implements only (i).

**Fix:** When `schema_salience >= threshold` AND `use_mech307_conjunction=True`, write all
three jointly:

```python
# proposed
gain = self.config.schema_wanting_gain
sal_val = float(self._schema_salience.squeeze())
drive_lvl = drive_level
predicted_z_world = self._z_world_predicted  # from gap 4 fix; fallback to current z_world
target_z = predicted_z_world if predicted_z_world is not None else z_world

# Gap 2 (i): VALENCE_WANTING (existing)
self.residue_field.update_valence(target_z, VALENCE_WANTING,
                                   sal_val * gain * max(drive_lvl, 0.1))
# Gap 2 (ii): partial anticipatory VALENCE_LIKING
self.residue_field.update_valence(target_z, VALENCE_LIKING,
                                   sal_val * self.config.mech307_anticipatory_liking_gain * drive_lvl)
# Gap 2 (iii) -- subsumes Gap 3: z_beta arousal pulse
self.latent_stack.tick_z_beta_pulse(sal_val * self.config.mech307_z_beta_schema_gain)
```

The `tick_z_beta_pulse` method does not yet exist; would need to be added to LatentStack.

### Gap 3: z_beta has no input path from cue prediction

**Code analysis:** z_beta is encoded from sensory observation in LatentStack. It is read by
MECH-093 to modulate E3 heartbeat rate. There is *no* path from MECH-216 schema readout to
z_beta amplitude. So when the schema head says "imminent positive event" (the upstream
signature of excitement), the arousal axis does not elevate.

**Fix:** Subsumed into Gap 2. The `tick_z_beta_pulse` method increments z_beta arousal
amplitude by a small amount proportional to schema_salience. This wires the cue → ANS path
that biology has anatomically.

### Gap 4: MECH-216 writes at the agent's current z_world, not at the predicted-imminent location

**Code:** [`agent.py:3754`](../../../ree-v3/ree_core/agent.py#L3754) writes to
`self._current_latent.z_world`. The residue field is marked at "wherever the agent is now,"
not at "where the agent predicts the goal will be." Biology's hippocampal place-cell preplay +
NAcc-anticipation marks the *predicted* goal location.

**Fix:** Use E1's forward prediction (already computed in `_e1_tick`) to identify the
predicted z_world, write at that location instead. Falls back to current z_world when
prediction is not available.

## What "excitement" looks like under the conjunction reading

Under all four fixes, the residue field at a predicted-imminent-reward location carries:

- VALENCE_WANTING amplitude high (anticipatory wanting via MECH-216)
- VALENCE_LIKING amplitude high (anticipatory hedonic via Gap 2 fix)
- VALENCE_POSITIVE_SURPRISE amplitude high (signed PE from a cue that exceeded prediction; Gap 1 fix)
- z_beta arousal elevated globally (Gap 3 fix)

A consumer that needs to detect excitement reads the joint state at a location:

```python
def is_excitement_state_at(z_loc, residue_field, z_beta_arousal, threshold=0.6):
    v = residue_field.evaluate_valence(z_loc)
    return (
        v[VALENCE_WANTING] > threshold
        and v[VALENCE_LIKING] > threshold * 0.5  # anticipatory liking is partial
        and v[VALENCE_SURPRISE] > 0  # signed -- positive PE only
        and z_beta_arousal > threshold
    )
```

Functional consumers that benefit:

- **MECH-205 surprise-gated replay write**: priority weighted by conjunction detection.
  Adcock 2006 prediction: locations with high anticipatory-conjunction at encoding receive
  >= 1.5x replay frequency vs uniform-priority baseline.
- **MECH-292 ranked ghost-goal bank**: `ghost_priority += w_conj * is_excitement_state(r)`.
- **MECH-279 PAG freeze gate**: VALENCE_NEGATIVE_SURPRISE + VALENCE_HARM_DISCRIMINATIVE +
  z_beta high → dread state → stronger freeze probability.

## Why MECH-307 is first-line and SD-014 6-channel is fallback

**MECH-307 advantages:**

1. *Biological fidelity*: excitement is composed of multiple signals at convergence, not a
   primitive neuron type. The conjunction architecture matches biology's actual organisation.
2. *Cost*: ~40 lines of code, all backward-compatible behind `use_mech307_conjunction=False`.
3. *Diagnostic value*: fixing Gap 1 (signed PE) likely also fixes the EXQ-141 curiosity
   drive failure (MECH-111), because that test depended on an upstream signed-novelty signal
   that the substrate cannot currently produce. One fix unblocks two tests.
4. *Parsimony*: avoids growing the residue field's `valence_vecs` buffer from `[K, 4]` to
   `[K, 6]`.

**SD-014 6-channel amendment advantages:**

1. *Direct write site*: a consumer that needs excitement reads `v[VALENCE_EXCITEMENT]` once,
   not a four-channel joint condition. Less dispersed, less error-prone if many consumers need
   the signal.
2. *Easier to ablate*: setting `valence_excitement_enabled=False` cleanly disables the
   anticipatory-positive-arousal writes; the conjunction architecture is harder to ablate
   cleanly because each gap-fix is a separate flag.
3. *Phenomenologically transparent*: the channel name maps to the construct name. Easier to
   communicate in claim text.

## SD-014 amendment proposal text (FALLBACK -- not yet applied to registry)

Should the MECH-307 conjunction-fix experiment fail or produce unreliable conjunction
detection at consumer sites, this is the proposed registry amendment to SD-014:

```
SD-014 (proposed amendment 2026-05-XX, FALLBACK pending MECH-307 experimental outcome)

Status change: provisional (current) -> provisional (amended; quadrant unchanged
pending experimental validation of the 6-channel architecture).

V is extended from 4-component to 6-component:
  V = [VALENCE_WANTING, VALENCE_LIKING, VALENCE_HARM_DISCRIMINATIVE,
       VALENCE_SURPRISE, VALENCE_EXCITEMENT, VALENCE_DREAD]

VALENCE_EXCITEMENT (index 4, new): high-arousal-positive anticipatory affect.
  Write site: cue-stage anticipatory write by MECH-216 schema readout when
    schema_salience >= threshold AND drive_level >= threshold AND prediction_certainty
    >= threshold. Write magnitude proportional to (schema_salience x drive x certainty).
  Update rule: e <- (1-alpha_e) * e + alpha_e * (excitement_value)
  Decay: very slow (alpha_e ~ 0.005 to match VALENCE_WANTING decay timescale).
  Hypothesis_tag gating: writes only when hypothesis_tag=False (waking).

VALENCE_DREAD (index 5, new): high-arousal-negative anticipatory affect.
  Symmetric to VALENCE_EXCITEMENT. Write site: when MECH-216 schema readout predicts
    imminent harm (predicted z_harm_a > threshold) with low controllability prediction.
    Cross-link to MECH-305 controllability-weighted affective load.
  Drives MECH-279 PAG freeze gate as one input among several.

Functional consumers:
  - MECH-205 surprise-gated replay write: priority bonus on locations with high
    VALENCE_EXCITEMENT (per Adcock 2006 prediction).
  - MECH-292 ghost_priority: ghost_priority += w_e * VALENCE_EXCITEMENT(r) -
    w_d * VALENCE_DREAD(r).
  - MECH-279 PAG freeze gate: VALENCE_DREAD as input alongside z_harm_a, override_signal.

Backward compatibility: valence_excitement_enabled / valence_dread_enabled config flags,
  default True (the channels exist but are written only when the gating conditions fire).
  Bit-identical when both flags are False (channels exist as zero-valued buffer slots).

Lit anchors: Knutson 2001a [DOI](https://doi.org/10.1523/JNEUROSCI.21-16-j0002.2001),
  Knutson 2001b [DOI](https://doi.org/10.1097/00001756-200112040-00016),
  Adcock 2006 [DOI](https://doi.org/10.1016/j.neuron.2006.03.036),
  Berns 2006 [DOI](https://doi.org/10.1126/science.1123721),
  Posner 2009 [DOI](https://doi.org/10.1002/hbm.20553),
  Bromberg-Martin 2010 [DOI](https://doi.org/10.1016/j.neuron.2010.11.022),
  Bromberg-Martin 2010b [DOI](https://doi.org/10.1016/j.neuron.2010.06.016),
  Knutson 2008 [DOI](https://doi.org/10.1016/j.biopsych.2007.07.023),
  Johnson 2019 [DOI](https://doi.org/10.1016/j.nicl.2019.102018).
```

## Discriminative experiment (queued but not registered)

`v3_exq_XXX_anticipatory_affect_arch_ablation`: 4 arms × 3 seeds, ~3-4h on Mac.

- ARM_0_off: current substrate (all 4 wiring gaps unfixed, baseline)
- ARM_1_signed_pe: Gap 1 fix only (Gaps 2-4 unfixed)
- ARM_2_full_conjunction: All 4 fixes (MECH-307 first-line architecture)
- ARM_3_5channel: SD-014 6-channel amendment (VALENCE_EXCITEMENT + VALENCE_DREAD added
  as discrete channels written by MECH-216, all 4 wiring gaps unfixed)

Acceptance:
- C1: conjunction-state detection rate at predicted-reward locations:
  ARM_2 >= 0.7, ARM_0 < 0.2 (test that the fixes work).
- C2: Adcock 2006 prediction: sleep-replay frequency at conjunction-state /
  uniform-priority baseline >= 1.5x in ARM_2.
- C3: ARM_2 vs ARM_3 head-to-head: probe accuracy on subsequent identity
  discrimination (analog of EXQ-538 SD-049 Phase 2) is comparable, but ARM_2 uses
  fewer net residue-field writes (parsimony measure).

PASS = C1 AND C2 AND C3 → MECH-307 conjunction-fix is the right architecture; SD-014
amendment can be retired as fallback.

PARTIAL PASS (C1 + C2 only, ARM_3 outperforms on C3) → SD-014 amendment is the better
architecture; apply registry amendment.

FAIL on C1 → wiring fixes don't compose into a detectable conjunction state; investigate
whether the issue is at the read site (consumer detection) or the write site (gap-fix
implementation incorrect). Diagnostic before any architectural commitment.

## Sequencing

1. **EXQ-537** (SD-029 single-pass comparator) lands first to clear the currently-running
   commit-chain diagnostic queue.
2. **EXQ-141b** (MECH-111 retest on corrected commit-chain substrate) lands to clear the
   curiosity-drive question with the same fixes applied.
3. **EXQ-XXX** (this experiment, MECH-307 4-arm + SD-014-amendment alternative arm)
   lands to adjudicate between the two architectures.
4. Apply the winning architecture to claims.yaml + ree-v3 implementation.

## Open considerations

- The MECH-307 conjunction architecture moves complexity to the consumer side (each
  consumer does a 4-channel joint read). If the V3 registry grows to many consumers of
  excitement / dread states (MECH-205, MECH-292, MECH-279, future MECH-3XX), the
  bookkeeping cost grows linearly with consumer count. SD-014 amendment writes once,
  reads once at each consumer. The right balance depends on how many consumers eventually
  need the signal.

- The signed VALENCE_SURPRISE fix (Gap 1) has implications beyond excitement: any consumer
  that currently reads VALENCE_SURPRISE assumes magnitude semantics. Auditing existing
  consumers is part of the implementation cost. Identified consumers as of 2026-05-08:
  MECH-205 surprise-gated replay (reads magnitude OK), MECH-094 hypothesis tag write gate
  (does not consume VALENCE_SURPRISE directly). No urgent breakage expected, but this
  audit should land before flipping `surprise_signed=True` as default.

- The Gap 4 fix (write at predicted z_world) requires E1 to expose its forward prediction
  via a stable accessor. Currently E1's prediction is internal; would need a new method
  `e1.get_z_world_prediction()` returning a `[batch, world_dim]` tensor or None.

## See also

- `evidence/literature/targeted_review_excitement_5th_valence_channel/SYNTHESIS.md` — the
  9-entry lit-pull that triggered this proposal
- `mech188_vs_mech295_dual_path.md` — companion architecture note from the same dialogue
- `sustained_drive_anticipatory_wanting.md` — adjacent SD-012 amendment scope (Berridge
  wanting persistence; same anticipatory-wanting cluster)
- claims.yaml — MECH-307 entry (registered 2026-05-08), SD-014 entry (amendment proposal
  in evidence_quality_note pending experimental validation)
