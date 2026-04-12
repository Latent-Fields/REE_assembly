---
nav_exclude: true
---

# SD-004 + SD-005 Encoder Co-Design Specification

**Status:** Active design — SD-004 and SD-005 structurally implemented; SD-007 (reafference
correction) required for functional separation.
**Date:** 2026-03-18 (updated from 2026-03-14 original; incorporates V3 EXQ-001–012 findings)
**Supersedes:** `2026-03-14_self_world_latent_split_sd003_limitation.md` (design sketch)

---

## 1. Problem Statement

V2 used a unified latent `z_gamma` for all sensory channels. This conflates two structurally
distinct kinds of information:

- **Self-directed effects**: body position, energy, proprioceptive state — immediate, fully
  action-determined, carry no moral weight per se
- **World-directed effects**: environmental changes caused by agent action — contamination,
  object state modification, harm events — carry moral weight and drive residue accumulation

Without separation, the SD-003 attribution pipeline (`world_delta = ||E2(z, a_actual) -
E2(z, a_cf)||`) is uninformative: `z_gamma` encodes egocentric perspective and body-state
simultaneously, so both `z_actual` and `z_cf` encode essentially the same current view
(dominated by perspective shift from locomotion), and E2 correctly learns the identity
shortcut: `E2(z_gamma, a_actual) ≈ E2(z_gamma, a_cf)`.

**Evidence of identity shortcut (V3 EXQ-002–012):**
- E2 world loss: ~0.0003–0.0005, invariant to environment perturbation
- calibration_gap: 0.0007 (threshold: 0.05), indistinguishable from random
- Root cause confirmed by EXQ-013: body_selectivity_margin = −0.137 (z_world MORE
  sensitive to body movement than z_self — structurally backwards)

---

## 2. SD-005 — Self/World Latent Split

### Design

Split `z_gamma` into two architecturally separate streams:

| Channel | Dimension | Domain | Update Authority | Temporal Grain |
|---------|-----------|--------|-----------------|----------------|
| `z_self` | `self_dim=32` | Proprioceptive + interoceptive | E2 (motor-sensory) | High frequency |
| `z_world` | `world_dim=32` | Exteroceptive world-state | E3 + Hippocampal | Lower, replayed |

**Observation routing (SD-005 encoder):**
- `body_obs` (dim=10): position, health, energy, footprint → z_self encoder (dorsal head)
- `world_obs` (dim=54): local view, contamination view → z_world encoder (ventral head)

**Module read/write contract:**
- E1: reads `z_self + z_world` (associative prior; read-only during inference)
- E2: writes `z_self_next` via `predict_next_self(z_self, a)`. Motor-sensory domain.
- E3 complex: writes z_world updates via harm/goal error
- HippocampalModule: reads `z_world` via action objects (SD-004); navigates O
- ResidueField: accumulates `world_delta = ||z_world_actual - z_world_cf||`
  (NOT `z_gamma_delta`; MECH-094 hypothesis_tag gate applies)

### Status and Limitation

SD-005 is structurally implemented (V3 split encoder, EXQ-001 PASS). However, EXQ-001 used
aggregate correlation metrics; event-conditional analysis (EXQ-013) shows functional
entanglement persists:

- `body_selectivity_margin = −0.137`: z_world is MORE selective to body events than z_self
- Cause: `world_obs` (exteroceptive) still receives egocentric view shifts from locomotion
- Structural separation ≠ functional separation until SD-007 is applied

**SD-005 depends on SD-007 for functional correctness.**

---

## 3. SD-007 — Perspective-Corrected World Latent (Reafference Correction)

### Why it is required

When the agent moves, the egocentric `world_obs` changes because the view shifts — not because
world content changed. The ventral encoder learns that `z_world` captures current egocentric
neighbourhood, not stable world features. This is reafferent signal (perspective shift caused by
self-motion) confounded with exafferent signal (genuine world change).

**Consequence for SD-003:** `E2_world(z_world, a_actual) ≈ E2_world(z_world, a_cf)` because
both actions are evaluated from the same current egocentric z_world. E2 cannot learn any
action-conditional structure (identity shortcut); E2 world loss → 0 trivially.

**Biological grounding:** Area MSTd (Gu et al. 2008, *Nature Neuroscience* 11:1201–1210):
- **Congruent neurons**: visual and vestibular heading preferences aligned → fire when visual
  motion is consistent with self-motion (reafference). Interpretation: world stable, I moved.
- **Incongruent neurons**: preferences opposed → fire when visual motion does NOT match expected
  self-motion (exafference). Interpretation: world changed beyond my movement prediction.

This reafference/exafference decomposition occurs in extrastriate cortex (early visual processing)
before hippocampal or prefrontal circuits. The efference copy arrives via SLF I/II/III (Rolls et
al. 2023, premotor → PPC pathway).

### Architecture: ReafferencePredictor

Placement: inside `LatentStack.encode()`, after the ventral encoder produces `z_world_raw`,
before temporal EMA is applied.

```
obs_t → SplitEncoder → z_world_raw (raw egocentric world encoding)
                     → z_self (proprioceptive)

E2_self(z_self_{t-1}, a_{t-1}) → z_self_predicted_t   [efference copy]

ReafferencePredictor(z_world_raw_{t-1}, a_{t-1}) → Δz_world_loco  [expected perspective shift]

z_world_corrected = z_world_raw - Δz_world_loco

EMA: z_world ← α_world · z_world_corrected + (1-α_world) · z_world_prev
```

**MECH-101 — Input must be z_world_raw_{t-1} (NOT z_self_{t-1}):** In a local-view
environment, the perspective shift Δz_world_raw from locomotion includes the content of
newly-revealed cells as they enter the field of view. This content is unknowable from body
state (z_self encodes position/health/energy only) but is fully available in z_world_raw_{t-1}
(which encodes what was visible at the previous position). V3-EXQ-027 confirmed this
empirically: R²=0.027 with (z_self, a) inputs versus the target Δz_world_raw, because
cell content variation dominates the delta and is inaccessible from z_self.

Biological grounding: MSTd receives full visual optic flow (scene content-dependent) + vestibular
+ efference copy — NOT body state + efference copy. The optic flow carries scene content;
z_self is equivalent to vestibular + body proprioception only.

**Training signal:** Trained exclusively on empty-space steps (`transition_type == "none"`)
where the only source of z_world change is the perspective shift from locomotion. This gives
clean, uncontaminated targets for fitting the expected reafference component.

```
target_Δz_world = z_world_raw_t - z_world_raw_{t-1}   (on empty-space steps only)
L_reaf = ||ReafferencePredictor(z_world_raw_{t-1}, a_{t-1}) - target_Δz_world||²
```

`z_world_raw_{t-1}` is available as `LatentState.z_world_raw` (stored every step in encode()).

Trained either as a learned MLP (online gradient, adds parameters) or via lstsq fit
(offline, zero additional parameters; EXQ-021 validates this approach).

**Updated z_world semantics post-SD-007:**
- `z_world_corrected ≈ 0` on empty-space steps (perspective shift cancelled)
- `z_world_corrected ≠ 0` on world-event steps (contamination, hazard entry: genuine changes)
- `body_selectivity_margin > 0` now achievable (world stream is now insensitive to body motion)

### Evidence Targets (EXQ-016, EXQ-021)

- EXQ-016 (bug-affected): R²_test = 0.118 (insufficient; root causes: alpha=0.3 EMA + C3 metric bug)
- EXQ-027 (MECH-101 fix, z_self → z_world_raw_prev inputs): Expected R²_test > 0.20
- EXQ-021 (lstsq, bug-fixed): Expected R²_test > 0.25; calibration_gap > 0.05

### Implementation Contract

When `LatentStackConfig.reafference_action_dim > 0`:
- `LatentStack.encode()` accepts `prev_action: Optional[torch.Tensor]`
- When `prev_action` is not None and `prev_state` is available:
  - Retrieve `z_world_raw_prev = prev_state.z_world_raw` (falls back to `prev_state.z_world`)
  - Apply `z_world_corrected = z_world_raw - ReafferencePredictor(z_world_raw_prev, a_prev)`
  - Store `z_world_raw` in `LatentState` for diagnostic use
- When `prev_action` is None (first step, or SD-007 disabled): `z_world_corrected = z_world_raw`
- `REEAgent.sense()` accepts optional `prev_action` parameter and passes it to `encode()`
- **Training data contract**: reaf_data tuples must be `(z_world_raw_prev, a, Δz_world_raw)`,
  NOT `(z_self_prev, a, Δz_world_raw)`. See MECH-101.

---

## 4. SD-004 — Action Objects

### Design

E2 produces compressed world-effect representations `o_t` encoding the world-directed
consequence of taking action `a_t` from `z_world_t`:

```
o_t = E2.action_object(z_world_t, a_t)    [action_object_dim=16 << world_dim=32]
```

HippocampalModule navigates in action-object space **O** (not raw `z_world`). This provides:
1. **Planning horizon extension**: action-object space is lower-dimensional and semantically
   grounded in world-effects. CEM in O is more tractable than in raw z_world.
2. **Q-020 (ARC-007 strict)**: hippocampal proposals are value-flat (no independent value
   head). Terrain sensitivity arises from navigating residue-shaped z_world, not valuation.

### Status

SD-004 PASSED (EXQ-003): TERRAIN harm_rate 0.0010 vs RANDOM 0.0896; survival 193.6 vs 32.7
steps. Action-object space navigation effective at ~6× improvement.

### SD-004 + SD-005 co-design

After SD-007 is applied:
- `z_world_corrected` is the correct input to `E2.action_object(z_world, a)` — action objects
  should encode genuine world-effects, not perspective shifts
- `E2.world_forward(z_world_corrected, a)` should produce action-conditional divergence at
  hazard positions (no longer dominated by the identity shortcut)
- HippocampalModule terrain map navigates `z_world_corrected` space; residue field also
  operates on `z_world_corrected`

---

## 5. SD-009 — Event Contrastive Supervision (MECH-100)

### Why reconstruction loss is insufficient

Standard reconstruction and E1-prediction losses are invariant to harm-relevance:
- An empty-cell step and a contamination-cell step produce similar E1 reconstruction loss
- The encoder has no gradient signal to distinguish event types in z_world

An explicit event-type cross-entropy auxiliary loss forces z_world to represent
hazard-vs-empty distinctions as a separable signal.

### Architecture: Event Classifier Head

Added to `SplitEncoder` as optional (when `LatentStackConfig.use_event_classifier = True`):

```python
event_classifier = nn.Linear(world_dim, 3)    # [none, env_caused_hazard, agent_caused_hazard]
```

Training: `L_event = CrossEntropy(event_classifier(z_world), event_label)` with
`lambda_event` mixing weight (tuned by EXQ-020).

Event labels are provided by CausalGridWorld `info['transition_type']` at each step:
- 0 = none (empty step)
- 1 = env_caused_hazard
- 2 = agent_caused_hazard

**Status:** Pending validation (EXQ-020 tests contrastive alone; EXQ-022 combines with lstsq).
Expected FAIL on C1 in isolation (insufficient without reafference correction), but meaningful
accuracy improvement in C2 event classification.

---

## 6. MECH-099 — Three-Stream Encoder Architecture

Updated from MECH-096 (dual-stream) based on Haak & Beckmann (2018, HCP resting-state n=470):

| Stream | Biological Pathway | REE Mapping | Head |
|--------|-------------------|-------------|------|
| Dorsal | IPS/occipitoparietal | Body/action, egocentric | `body_encoder` → z_self |
| Ventral | VO/PHC | Object identity, world content | `world_encoder` → z_world |
| Lateral (third) | MT→MST/FST→posterior STS | Dynamic motion, agency, harm-salient | `lateral_head` → z_harm |

The lateral head (`harm_dim > 0` in config) bypasses E2_world and feeds E3's harm evaluation
directly — a faster channel for harm-salient sensory events. Currently disabled by default.

**Why three streams is architecturally required (MECH-069):** The three streams run on distinct
white-matter tracts (SLF I/II/III dorsal; ventral occipitotemporal; lateral STS pathway).
Incommensurability of error signals (MECH-069) is partly explained by physically distinct
hardware. Collapsing dorsal, ventral, and lateral into one trunk violates the biological
architecture.

---

## 7. MECH-095 — TPJ Agency-Detection Comparator

Biological basis: temporoparietal junction (TPJ) computes efference-copy-predicted sensory
consequence vs actual observed sensory consequence (Blakemore, Wolpert & Frith, 2002).

### Dependency on SD-007

Without SD-007, E2_self's motor prediction is trained on z_self that still includes residual
perspective-shift confound → mismatch signal is noisy and non-diagnostic.

With SD-007:
- `z_self` encodes genuine body-state changes (perspective shift removed from world stream)
- E2_self is trained on clean proprioceptive targets
- `mismatch = ||z_self_observed - E2_self(z_self_{t-1}, a_{t-1})||` is diagnostic of
  unexpected body-state changes (unexpected hazard entries, environmental collisions)

### EXQ-011 Failure Analysis

EXQ-011: `harm_safe_gap = 0.00470` (threshold 0.005) — marginal fail. Root cause: E2_self
trained on z_self that is partially confounded. After SD-007:
- z_self should be cleaner (perspective-shift in world stream only)
- E2_self mismatch signal should improve
- Predicted harm_safe_gap > 0.01 (well above threshold)

---

## 8. Updated SD-003 Attribution Pipeline (V3 Full)

The V2 pipeline (`E2.predict_harm(z_gamma, a)`) is deprecated. The V3 pipeline:

```
# Step 1: encode with reafference correction
z_self_t, z_world_corrected_t = LatentStack.encode(obs_t, prev_state, prev_action)

# Step 2: E2_world forward (perspective-corrected)
z_world_actual_{t+1} = E2_world(z_world_corrected_t, a_actual)
z_world_cf_{t+1}     = E2_world(z_world_corrected_t, a_cf)

# Step 3: E3 harm evaluation (harm/goal domain)
harm_actual = E3.harm_eval(z_world_actual_{t+1})
harm_cf     = E3.harm_eval(z_world_cf_{t+1})

# Step 4: causal signature
causal_sig = harm_actual - harm_cf     # > 0 at agent-caused harm; ≈ 0 at env-caused
world_delta = ||z_world_actual_{t+1} - z_world_cf_{t+1}||
```

**Why V3 pipeline should exceed calibration_gap > 0.05 (previously 0.0007):**

1. `z_world_corrected` now varies with world content (contamination, hazards) not perspective
2. `E2_world(z_world_corrected, a_actual)` vs `E2_world(z_world_corrected, a_cf)` now diverge
   at hazard positions because z_world_corrected encodes whether current cell is contaminated
3. E3.harm_eval(z_world) trained on genuine harm/goal error (not motor-sensory)
4. Identity shortcut is broken: `z_world_corrected_actual ≠ z_world_corrected_cf` at harm sites

Predicted calibration_gap after full SD-007 integration: **0.15–0.30** (tpj_agency_comparator.md).

---

## 9. MECH-071 V3 Redesign

**V2 MECH-071:** `calibration_gap = E2.predict_harm(z_gamma, a)` discrimination

**V3 redesign:** `calibration_gap = E3.harm_eval(z_world_corrected)` discrimination

The V3 claim: at harm events, `E3.harm_eval(z_world_corrected)` is higher before agent-caused
transitions than before env-caused transitions, because:
- Before agent_caused: contamination_view in world_obs is HIGH (agent placed it)
  → z_world_corrected encodes elevated contamination → E3.harm_eval → higher
- Before env_caused: contamination_view is LOW (env placed hazard, not contamination_view)
  → z_world_corrected reflects hazard indirectly → E3.harm_eval → lower

This is testable WITHOUT E2_world forward pass (direct z_world evaluation at the step
where harm occurs). PASS criterion: calibration_gap > 0.05 (trained), < 0.10 (random).

**Key difference from V2:** This uses z_world (world content) not z_gamma (body + world mixed).
The discriminating signal lives in the contamination channel of world_obs → z_world_corrected,
which was invisible in V2 because z_gamma averaged it with body-state noise.

---

## 10. Dependency Chain and Experiment Ordering

```
SD-005 (z_self/z_world split) [structural — PASS EXQ-001]
    │
    ├─ SD-008 (alpha_world >= 0.9) [EXQ-023 RUNNING]
    │       Prerequisite: event responses visible (alpha=0.3 suppresses to 30%)
    │
    ├─ SD-007 (reafference correction) [EXQ-021 pending]
    │       Prerequisite: world stream functionally distinct from perspective shift
    │       Requires: prev_action available in LatentStack.encode()
    │       Validates via: EXQ-021 (lstsq, expected R² > 0.25)
    │
    ├─ SD-009 (event contrastive supervision) [EXQ-020 pending]
    │       Prerequisite: SD-008 (events visible before classification)
    │       Can run in parallel with SD-007
    │
    └─ SD-004 (action objects) [PASS EXQ-003]
            Post-SD-007: action_object() should use z_world_corrected

After SD-007 + SD-008:
    ├─ MECH-071 V3 redesign [EXQ-026 — new]
    │       E3.harm_eval(z_world_corrected) calibration gap
    ├─ MECH-095 V3 redesign [EXQ-028 — after EXQ-011 FAIL analysis]
    │       TPJ proxy with clean z_self
    └─ SD-003 V3 full pipeline [EXQ-027 — new]
            calibration_gap target: 0.15–0.30
```

---

## 11. Alpha-World Requirement (SD-008)

Separate from SD-007 but required for event visibility:

```python
# LatentStack.encode() temporal EMA:
z_world = alpha_world * z_world_corrected + (1 - alpha_world) * prev_z_world
```

With `alpha_world = 0.3` (default for backward compat):
- z_world is a ~3-step weighted average (0.3 × current + 0.21 × t-1 + 0.147 × t-2 ...)
- Harm events (single-step, discrete): suppressed to ~30% of true magnitude
- E2_world loss → 0 because z_world barely moves between steps

With `alpha_world = 0.9`:
- z_world = 0.9 × current + 0.09 × prev: nearly pure current-step encoding
- Harm events fully visible in z_world
- MECH-089 theta buffer handles temporal integration at higher level

**Config:** `LatentStackConfig.alpha_world` (default 0.3 for backward compat).
All V3 experiments should set `alpha_world=0.9` or `alpha_world=1.0`.
Change the default in config ONLY after EXQ-023 confirms 0.9 is universally better.

---

## 12. Open Questions

- **Q-020 (resolved):** ARC-007 STRICT — HippocampalModule generates value-flat proposals.
  Terrain sensitivity from residue-shaped z_world, not separate value head.
- **Q: lstsq vs MLP for ReafferencePredictor?** EXQ-021 (lstsq) vs EXQ-016 (MLP, failed).
  Recommended: start with lstsq (zero extra parameters; EXQ-021 expected PASS).
- **Q: lateral head training signal?** EXQ-015 (three-stream lateral) pending.
  Concern: lateral head bypasses E2 but still needs a training loss.
- **Q: SD-008 + SD-007 interaction?** EXQ-023 (alpha=0.9 alone) must PASS before
  combining with SD-007 to isolate effects.

---

## 13. Success Criteria for V3 Encoder Co-Design

The encoder co-design is successful when:

1. `body_selectivity_margin > 0` (z_self more correlated with body events than z_world is)
2. `world_selectivity_margin > 0.05` (z_world more correlated with world events than z_self is)
3. Reafference R² > 0.25 on empty-space steps (SD-007 predictor effective)
4. `calibration_gap(E3.harm_eval(z_world)) > 0.05` (MECH-071 V3)
5. SD-003 `calibration_gap > 0.15` (full pipeline with reafference)

Criteria 1+2 validate functional separation. Criteria 3 validates reafference. Criteria 4+5
validate the full attribution pipeline.
