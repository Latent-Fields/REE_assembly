# TPJ Agency-Detection Comparator (MECH-095)

**Claim ID:** MECH-095
**Status:** candidate
**Implementation phase:** V3
**Depends on:** SD-005 (z_self/z_world split), MECH-069 (incommensurable error signals), MECH-096 (dual-stream encoder), MECH-097 (peripersonal space as commit locus)
**Created:** 2026-03-17

---

## 1. The Problem This Solves

SD-003's V2 experiments (EXQ-027, EXQ-028) used:

```
causal_delta = ||E2(z_gamma, a_actual) - E2(z_gamma, a_cf)||
```

EXQ-027 result: `calibration_gap = 0.027` (best: dense-hazard condition). Pass threshold: `> 0.05`. **FAIL.**

The root cause is not a calibration problem — it is an ontological conflation. `z_gamma` encodes two structurally different kinds of state change in a single latent:

- **Proprioceptive self-effects**: body position shifted, energy expended, posture changed. These are *immediate*, *action-determined*, and carry *no moral weight*. They are large on every move, regardless of whether harm was caused.
- **World-directed effects**: contamination laid down, hazard entered, environment modified. These carry *potential moral weight* and accumulate as residue candidates.

When `z_gamma` conflates both, `causal_delta` is swamped by proprioceptive noise. A normal move and a contaminating move produce similar `causal_delta` magnitudes — the discrimination signal can barely exceed noise.

**MECH-095 is the mechanism that makes this cut.** It places a comparator at the z_self/z_world interface that decomposes state change into self-caused (motor-predictable) and world-contributed (motor-unpredictable) components.

---

## 2. Neural Basis

The temporoparietal junction (TPJ) computes the mismatch between the efference-copy-predicted sensory consequence of an action and the actual observed sensory consequence (Blakemore, Wolpert & Frith, 2002).

- **High match** → the action produced exactly what the motor system predicted → self-caused
- **High mismatch** → the observed outcome includes components the motor system could not have predicted from the action alone → world-contributed cause

This is the neural substrate for the **sense of agency**. Its failure is clinically documented: schizophrenic passivity phenomena arise when self-generated actions are experienced as externally caused — the comparator misattributes self-generated motor predictions as world events (Frith et al., 2000).

The REE TPJ comparator is a direct architectural analog: it does not detect agency phenomenologically, but it performs the same computational role — extracting the self-caused/world-caused decomposition from the action-prediction/observation residual.

---

## 3. Computational Structure

### 3.1 Prerequisites

MECH-095 presupposes SD-005 (self/world latent split) and MECH-096 (dual-stream encoder). Without these, there is no `z_self` stream separate from `z_world`, and the comparator degenerates to the same V2 `z_gamma` mismatch.

```
Observation o_t
      ↓
DualStreamEncoder (MECH-096)
   ├─ Dorsal head → z_self_t   (egocentric, action-relevant, high temporal resolution)
   └─ Ventral head → z_world_t (allocentric, object-identity, sustained)
```

### 3.2 Online Efference-Copy Mode (per-step)

At each agent step:

```
Step t: action a_t committed

E2(z_self_{t-1}, a_{t-1}) → z_self_predicted_t       # efference copy: what motor model expects
DualStreamEncoder(o_t) → z_self_observed_t             # actual sensory reafference

TPJComparator:
  mismatch_vector = z_self_observed_t - z_self_predicted_t
  agency_signal   = exp(-λ · ||mismatch_vector||²)     # ∈ (0,1]; 1=perfect match=self-caused
  residue_flag    = agency_signal < θ_agency            # mismatch exceeds PPS boundary
```

`θ_agency` is the agency threshold, modulated by `z_beta` via MECH-097 (peripersonal space boundary is not fixed — scales with arousal, tool-use, attentional state).

**Interpretation:**
- `agency_signal ≈ 1`: the action produced exactly the body-state change E2 predicted → self-caused → no residue contribution from this step
- `agency_signal ≪ 1`: the observed z_self change includes components E2 could not predict from the motor command alone → world-contributed → residue candidate

### 3.3 Counterfactual Attribution Mode (SD-003 compatible)

The SD-003 causal signature now decomposes cleanly:

```
# Self-attribution component (motor model, no moral weight)
self_delta = E2(z_self_t, a_actual) - E2(z_self_t, a_cf)

# World-attribution component (consequence model, carries moral weight)
world_delta = z_world_{t+1}(a_actual) - z_world_{t+1}(a_cf)
```

Residue accumulates on `world_delta`, not `self_delta`:

```
# V2 (conflated, noisy):
residue_candidate = ||E2(z_gamma, a_actual) - E2(z_gamma, a_cf)||

# V3 (decomposed, clean):
residue_candidate = ||z_world_{t+1}(a_actual) - z_world_{t+1}(a_cf)||
                                                    filtered by agency_signal < θ_agency
```

The `world_delta` discriminates agent-caused contamination from environment-caused hazard because:
- **Agent-caused contamination**: z_world changes more under `a_actual` than `a_cf` (the contamination footprint is in z_world)
- **Environment-caused hazard**: z_world change is similar under `a_actual` and `a_cf` (the hazard was already there; the agent only entered it)

This is why the V3 version of SD-003 should exceed the 0.05 threshold: the world_delta is the clean causal signal, not swamped by proprioceptive self-effects.

---

## 4. Interface Specification

```python
@dataclass
class TPJOutput:
    agency_signal: Tensor       # shape (batch,) ∈ (0,1] — 1 = self-caused
    mismatch_vector: Tensor     # shape (batch, z_self_dim) — directional residual
    residue_flag: Tensor        # shape (batch,) bool — mismatch exceeds θ_agency
    world_contribution: Tensor  # shape (batch, z_self_dim) — unpredicted z_self change


class TPJComparator(nn.Module):
    """
    TPJ agency-detection comparator.
    Computes efference-copy prediction vs sensory reafference mismatch
    for online agency attribution.

    Placement: between E2 (efference prediction) and residue accumulation.
    Receives z_beta for dynamic agency threshold (via PPS — MECH-097).
    """

    def forward(
        self,
        z_self_predicted: Tensor,   # E2's efference-copy prediction of z_self_{t+1}
        z_self_observed: Tensor,    # Dorsal encoder's observed z_self_{t+1}
        z_beta: Tensor,             # Affective/arousal state (modulates θ_agency via MECH-097)
    ) -> TPJOutput:
        ...

    def counterfactual_attribution(
        self,
        z_world_actual: Tensor,     # z_world_{t+1} under a_actual
        z_world_cf: Tensor,         # z_world_{t+1} under a_cf (null or baseline action)
    ) -> Tensor:
        """
        World-delta causal signature for SD-003.
        Returns the world-state change attributable to the agent's action choice.
        This is the moral-weight-bearing component: it should be large when the
        agent contaminated the world and small when the agent merely entered an
        environment hazard.
        """
        ...
```

---

## 5. Placement in the Agent Step Loop

```
Per-step online loop:

o_{t+1} available (after env.step(a_t))
    │
    ▼
DualStreamEncoder(o_{t+1})
    ├─ z_self_observed_{t+1}  (dorsal head)
    └─ z_world_{t+1}          (ventral head)
    │
    ▼ (z_self branch)
TPJComparator(
    z_self_predicted_{t+1},   ← from E2(z_self_t, a_t) computed at commit time
    z_self_observed_{t+1},
    z_beta_t
)   → { agency_signal, residue_flag, world_contribution }
    │
    ├─ if residue_flag:
    │       compute world_delta = ||z_world_{t+1} - z_world_t||
    │       residue_accumulation ← world_delta (not total z_gamma change)
    │       attribution_ledger ← commit_id, world_contribution, agency_signal
    │
    └─ always:
            motor_sensory_error = ||z_self_predicted_{t+1} - z_self_observed_{t+1}||
            E2 training target: minimize motor_sensory_error (clean proprioceptive signal)
```

**Commit boundary interaction:**
- Pre-commit: TPJ comparator runs on simulation/rehearsal trajectories. `residue_flag` during rehearsal does NOT accumulate residue — it only informs trajectory selection (high `residue_flag` trajectory = higher anticipated world cost).
- Post-commit: `residue_flag` from realized steps DOES accumulate residue, gated by commit token (MECH-060/061).

---

## 6. Why V3 SD-003 Should Exceed the 0.05 Threshold

The V2 EXQ-027 calibration gap (`0.027`) failed because:

1. `z_gamma` encodes both body-position change and contamination signal
2. Body-position change under `a_actual` and `a_cf` are identical in magnitude (same step size)
3. Contamination change is a small fraction of total z_gamma delta
4. Signal-to-noise ratio for contamination in causal_delta is low

With MECH-095 + SD-005:

1. z_self encodes body-position change (dorsal head — egocentric, motor-relevant)
2. z_world encodes contamination state (ventral head — allocentric, identity-sustained)
3. `world_delta = ||z_world_{t+1}(a_actual) - z_world_{t+1}(a_cf)||` is ZERO for pure movement steps (z_world unchanged by a_cf) and NON-ZERO for contaminating steps (agent's action modified z_world)
4. The signal that was buried in z_gamma noise is now the ENTIRE signal in z_world_delta

Predicted effect: `calibration_gap` for V3-EXQ-002 (redesigned SD-003) should substantially exceed 0.05, likely in the 0.15–0.30 range for the dense-hazard condition where contamination contrast is maximal.

---

## 7. Dependency Chain

```
SD-005 (z_self / z_world split)
    │
    ├─ MECH-096 (dual-stream encoder)
    │      Dorsal head → z_self
    │      Ventral head → z_world
    │
    ├─ MECH-097 (peripersonal space)
    │      PPS boundary defines where self ends and world begins
    │      Modulates TPJ θ_agency via z_beta
    │
    └─ MECH-095 (THIS DOCUMENT — TPJ comparator)
           Uses z_self stream from MECH-096
           Receives θ_agency modulation from MECH-097
           Outputs agency_signal → routes to residue accumulation
           Outputs world_contribution → SD-003 causal_delta (clean)
```

MECH-095 cannot be implemented before MECH-096 provides a z_self stream that is architecturally separate from z_world. If implemented on z_gamma (as in V2), the comparator degrades to the V2 causal_delta and provides no improvement.

---

## 8. Relationship to Existing Mechanisms

**MECH-059 (precision channel separation):** MECH-095 produces a second signal orthogonal to precision — `agency_signal` is about causal attribution, not prediction confidence. High agency_signal (self-caused, correct prediction) with LOW precision (uncertain self-model) is possible: the agent knows it caused the outcome but is uncertain about the details. These should not be collapsed.

**MECH-060 (pre/post-commit channel separation):** The TPJ comparator's `residue_flag` output routes to different sinks depending on phase. Pre-commit: shapes trajectory selection (candidate with high residue_flag = higher world cost). Post-commit: triggers residue accumulation in the attribution ledger.

**ARC-015 (agency and responsibility flow):** MECH-095 is the concrete implementation of the "compare predicted versus observed reafference" step in ARC-015's responsibility flow. ARC-015 identifies this comparison as the origin of responsibility ("this change was because of me"). MECH-095 operationalizes it.

**MECH-069 (incommensurable error signals):** The TPJ comparator is what makes the three error signals MEASURABLY incommensurable. Motor-sensory error (E2 on z_self) and world-consequence error (E3 on z_world) can only be cleanly separated if the TPJ comparator routes the unexplained z_self change to z_world attribution. Without this routing, the incommensurability is an architectural claim that cannot be quantitatively validated.

---

## 9. Failure Modes

**TPJ comparator calibrated too strictly (θ_agency too low):** Nearly all steps flagged as world-contributed. Residue accumulates for every move. Moral paralysis — agent treats all of its actions as morally significant even when only body position changed.

**TPJ comparator calibrated too loosely (θ_agency too high):** Nothing flagged. Residue never accumulates. Equivalent to the V2 naive accumulation problem but now with an explicit mechanism that systematically fails.

**z_self/z_world boundary leakage (MECH-096 failure):** If the dual-stream encoder allows cross-contamination between z_self and z_world during training, the comparator's input is again the V2 conflated case. The architectural separation from MECH-096 must be maintained structurally (separate output heads, separate gradient pathways, separate loss terms).

**Static θ_agency (MECH-097 not wired):** If θ_agency is a fixed scalar rather than modulated by z_beta via PPS, the comparator cannot adapt to tool use, action amplification, or arousal-driven changes in the agent's effective body boundary. This produces systematic miscalibration in high-arousal or tool-extended conditions.

---

## 10. V3 Experimental Target

**V3-EXQ-002** (redesigned SD-003): Re-run the MECH-071/072 attribution experiments on the V3 substrate with SD-005 + MECH-095 + MECH-096 wired.

Primary metric: `calibration_gap = mean(world_delta | agent_caused) - mean(world_delta | env_caused) > 0.05`

Predicted outcome: gap exceeds threshold (target 0.15+) because world_delta cleanly encodes contamination footprint, not body-state noise.

Secondary metric: `false_attribution_rate` under FORESEEABLE condition should drop more sharply than in V2 EXQ-028, because agency_signal provides a cleaner gating signal than E2.predict_harm operating on z_gamma.

---

## Related Claims

- MECH-095 (this document)
- SD-005 (self/world latent split — design_decisions.md)
- MECH-096 (dual-stream encoder)
- MECH-097 (peripersonal space as commit locus)
- MECH-069 (incommensurable error signals)
- ARC-015 (agency and responsibility flow)
- MECH-059 (confidence channel separation)
- MECH-060 (pre/post-commit channel separation)
- ARC-021 (three BG-like learning channels)

## References

- Blakemore, S.-J., Wolpert, D. M., & Frith, C. D. (2002). Abnormalities in the awareness of action. *Trends in Cognitive Sciences*, 6(6), 237–242. [efference copy / sense of agency]
- Frith, C. D., Blakemore, S.-J., & Wolpert, D. M. (2000). Explaining the symptoms of schizophrenia: Abnormalities in the awareness of action. *Brain Research Reviews*, 31(2-3), 357–363. [passivity phenomena, comparator failure]
- `evidence/literature/targeted_review_connectome_mech_095/`
- `docs/thoughts/2026-03-14_self_world_latent_split_sd003_limitation.md`
