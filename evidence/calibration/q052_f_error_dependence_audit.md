# Q-052 — Diversity-Signal Forward-Model-Error Dependence Audit (ICM Self-Defeat Check)

- **Audit date:** 2026-05-17T18:17:37Z
- **Auditor session:** q052-f-error-dependence-audit-2026-05-17T181123Z
- **Code state:** ree-v3 `ree_core/` @ working tree 2026-05-17; REE_assembly @ 6fd9210120
- **Claim:** Q-052 (registered 2026-05-17, claims.yaml commit 3bd35da308) — diagnostic branch
- **Diagnostic source:** Pathak et al. 2017 (ICM, arXiv:1705.05363), cited in Q-052 `literature_anchors`
- **Status:** CANONICAL. The V3-EXQ-543h task and any Q-052 governance review should consume this note rather than re-deriving the classification.

---

## Question

For each diversity-contributing signal, is the signal's *magnitude* computed as (or proportional to)
a function of forward-model prediction error / surprise / E2-rollout error, such that it shrinks
toward zero as F's prediction accuracy improves over training (the ICM self-defeat failure mode)?

`F` here = the predictive model whose error is accumulated in
`E3TrajectorySelector._running_variance` — an EMA of prediction-error-squared:

```
ree_core/predictors/e3_selector.py:228-234
  def update_running_variance(self, prediction_error):
      error_var = prediction_error.pow(2).mean().item()
      self._running_variance = (1 - self._ema_alpha) * self._running_variance
                              + self._ema_alpha * error_var
  # initial value: config.precision_init = 0.5  (e3_selector.py:172; config.py:311)
```

`_running_variance` *is* F's prediction-error magnitude (smoothed). Any signal whose magnitude is
proportional to `_running_variance` (or to its time-derivative) decays to F's irreducible PE floor
as F consolidates — the textbook ICM/Schmidhuber self-defeat.

---

## Per-signal classification

| Signal | F-dependent? | File:line (magnitude computation) | Expression | Reasoning |
|---|---|---|---|---|
| **MECH-313** noise floor | **NO** (F-independent, safe) | `ree_core/policy/noise_floor.py:192-193` | `lifted = baseline_T + noise_floor_alpha`; `effective = max(lifted, min_temperature)` | Pure constant temperature lift. `alpha`, `min_temperature` are fixed config scalars. No PE / `_running_variance` / model-confidence input. State-independent by design. Does not decay as F improves. The `baseline_T` passed in (agent.py:3293) is irrelevant to F; the `max(., min_temperature)` floor is the load-bearing term and is constant. |
| **MECH-314a** curiosity-novelty | **NO** w.r.t. F (separate coverage caveat) | `ree_core/policy/structured_curiosity.py:419-426`, applied `:331` | `novelty = min_dists / mean_norm`; `total -= curiosity_novelty_weight * novelty` (`min_dists` = candidate first-step z_world distance to nearest **active ResidueField RBF center**) | Magnitude is a spatial coverage / recency-of-encounter distance, **not** forward-model PE. Independent of F's prediction accuracy. CAVEAT: it *does* decay as the residue field saturates over a well-covered map — but that is novelty/coverage exhaustion, a distinct failure mode, **not** the Q-052 ICM/F-error self-defeat. |
| **MECH-314b** curiosity-uncertainty | **YES — self-defeating (ICM)** | signal read `ree_core/policy/structured_curiosity.py:441-444`; applied `:347` | `bias_b = -curiosity_uncertainty_weight * e3._running_variance` (broadcast over K) | The bonus magnitude is **directly proportional to F's prediction error** (`_running_variance` = EMA of PE²). As F consolidates, PE→floor, `_running_variance`→floor, bonus→~0. Exact Pathak-2017 ICM signature: the exploration bonus collapses precisely in well-predicted regions. |
| **MECH-314c** curiosity-learning-progress | **YES — self-defeating (Schmidhuber/ICM)** | feed `ree_core/agent.py:3337` (`pe_scalar = e3._running_variance`); LP `ree_core/policy/structured_curiosity.py:477,483`; applied `:365` | `bias_c = -curiosity_learning_progress_weight * EMA(|rv_t - rv_{t-K}|)` where `rv = e3._running_variance` | Explicitly the Schmidhuber-1991 / Pathak-2017 first-difference-of-PE learning-progress signal (module docstring cites Pathak 2017 directly). Fed scalar is `_running_variance` (PE-MSE). As F consolidates, PE→low **and flat** → first-difference→0 → LP-EMA→0 → bonus→0. Self-defeating by construction. |
| **MECH-320** tonic vigor | **NO** (F-independent; F-coupling is *protective/inverse*) | core EWMA `ree_core/policy/tonic_vigor.py:308-309`; fed `ree_core/agent.py:3350-3356`; PE gate `tonic_vigor.py:475-493`; `recent_pe` src `agent.py:3232` | `v_raw = (1-α)·v_raw + α·(−selected_E3_score)`; `bias = ∓w·v_t`, `v_t = max(v_t_floor, max(0,v_raw)·g_e·g_d·g_pe)` | Load-bearing signal is a slow EWMA over the realised E3 trajectory **reward/cost** (harm/goal/residue), **not** PE. Does not shrink as F improves. Its only F-coupling is `gate_pe`, which *suppresses* vigor when PE is **high**; as F improves PE drops → `gate_pe`→1.0 → vigor is **released** (rises). F-improvement *increases* this signal — opposite of self-defeat. (Orthogonal pre-existing sign/scale bug zeros `v_raw`; that is not F-dependence and is tracked separately.) |
| **MECH-260** dACC anti-recency | **NO** (F-independent, safe) | `ree_core/cingulate/dacc.py:267-277`; adapter `dacc.py:491-492` | `suppression[i] = count(class_i ∈ last N actions) / len(history)`; `bias += dacc_suppression_weight · suppression` | Pure function of the recent chosen-action-class FIFO. No PE / `_running_variance` / model-confidence input. State-dependent on action history, fully independent of F's prediction error. NOTE: the sibling dACC `foraging_value` (`dacc.py:384`, `max(0, pe − pe_baseline)` against the E2_harm_a forward model) **is** F-dependent — but it is an exploration-pressure scalar that raises all candidates uniformly (not an inter-candidate diversity signal; DACCtoE3Adapter docstring) and is off by default (`dacc_foraging_weight=0`). Not the Q-052 diversity term. |
| **MECH-295** liking bridge | **NO** (F-independent) | `ree_core/regulators/mech295_liking_bridge.py:270-273` (cue), `:223` (write), `:375` (MECH-307) | `bias = -liking_to_approach_cue_gain · drive_level · goal_proximity` | Magnitude is `drive_level · goal_proximity` — no PE / `_running_variance`. MECH-307 Path B (`:367-375`) gates on a `VALENCE_SURPRISE > 0` *conjunction* but the magnitude is `gain · drive_level` (binary-gated, not PE-scaled) and `use_mech307_conjunction_read` defaults False. F-independent. |

---

## Verdict — does Q-052's ICM self-defeat flag fire?

**The flag FIRES, but component-specifically — not for the whole stack.**

- **F-DEPENDENT (self-defeating):** MECH-314b (uncertainty) and MECH-314c (learning-progress).
  Both are wired off `e3._running_variance` (the PE-MSE EMA). Their bonus magnitude is, respectively,
  proportional to F's prediction error and to its first difference. Both collapse toward zero as F
  consolidates. This is exactly the Pathak-2017 ICM / Schmidhuber-1991 failure the Q-052 diagnostic
  flag anticipates.
- **F-INDEPENDENT (safe / durable):** MECH-313 (constant temperature lift), MECH-314a (residue-coverage
  novelty), MECH-320 (reward-rate EWMA; F-coupling is inverse/protective), MECH-260 (action-history
  FIFO), MECH-295 (drive·proximity). None decay as F improves.

So the diversity stack is a **mixture**: its curiosity sub-channels are structurally self-defeating;
its noise-floor / coverage / vigor / anti-recency channels are not.

---

## Implication for EXQ-573 interpretation

EXQ-573 (10×/5×/1× static bias-scale sweep on MECH-313/314/320, ±combined) must be read
**per component, not in aggregate**:

1. **Lift attributable to MECH-313** (constant, F-independent): durable. Static scaling is the
   correct, non-self-defeating fix for this channel. This is the cleanest magnitude lever (A).
2. **Lift attributable to MECH-314b/c** (F-dependent): **transient**. A 5-10× scale multiplies a
   signal that is itself decaying to zero — it delays, not prevents, collapse. If EXQ-573 shows an
   early-training entropy lift sourced from curiosity-uncertainty/LP, expect it to **regress as F
   keeps consolidating**. A short EXQ-573 run can therefore *over-estimate* the durable benefit of
   the curiosity channels.
3. **Lift attributable to MECH-314a / MECH-320** (F-independent): durable for F-decay purposes
   (314a still subject to its own separate coverage-exhaustion; MECH-320 still blocked by its
   pre-existing `v_raw` sign/scale bug, independent of this audit).

Caveat — current dominant blocker is upstream of F-dependence: V3-EXQ-573's observed result was
*bit-identical across all 10 arms* (developmental warm-start failure: signals at/near zero at cold
start, `_running_variance=precision_init=0.5` decaying immediately; per WORKSPACE_STATE
2026-05-16T11:38Z, DEV-NEED-029). F-error-dependence is the **next** failure that bites *after*
warm-start is fixed — specifically for 314b/c. Once warm-start (DEV-NEED-029) is established, the
predicted signatures are: 314b/c → transient-then-regress (confirms structural B for those channels);
313 / 314a / 320 / 260 → durable lift if scaled (confirms magnitude A for those channels).

---

## Implication for Q-052 resolution and MECH-333/334 prioritization

Q-052 does **not** resolve cleanly to (B) STRUCTURAL *regardless* of EXQ-573. The correct reading:

- The magnitude fix (A) **is viable** — but specifically through the **F-independent** channels,
  most cleanly **MECH-313** (a pure constant entropy floor that scaling fixes durably), with
  MECH-314a and a sign-fixed MECH-320 as secondary durable levers.
- The structural fix (B) — the **MECH-333/334 critical-period crystallization** mechanism — is
  **necessary only insofar as the architecture relies on the F-dependent curiosity sub-channels
  (MECH-314b/c) for behavioural diversity.** Those two channels cannot be rescued by static scaling;
  for them, (B) is required, or they must be re-grounded on an F-independent novelty signal
  (e.g. routed through residue-coverage like 314a rather than `_running_variance`).

**Recommendation to governance / V3-EXQ-543h:**
1. Treat MECH-313 as the primary durable diversity lever; calibrate its scale via EXQ-573 with
   confidence that the lift will not self-defeat.
2. Flag MECH-314b/c as ICM-self-defeating: do not interpret any EXQ-573 curiosity-sourced lift as
   durable without a long-horizon (post-F-consolidation) check. MECH-333/334 prioritization is
   justified **for the curiosity channels specifically**, not as a blanket conclusion for the whole
   ARC-065 stack.
3. Consider an architectural option distinct from MECH-333/334 for the curiosity channels:
   re-ground MECH-314b/c magnitude on an F-independent quantity (coverage / state-visitation
   novelty, as 314a already does) so the bonus does not vanish with F consolidation. This would
   make (A) viable for curiosity too and reduce the load on (B).

---

## One-paragraph summary

The Q-052 ICM self-defeat flag **fires for MECH-314b (uncertainty) and MECH-314c
(learning-progress)** — both compute their bonus magnitude directly from `e3._running_variance`
(the forward-model PE-MSE EMA) or its first difference, so both collapse to zero as F consolidates,
exactly the Pathak-2017 failure mode. It does **not** fire for MECH-313 (constant temperature lift),
MECH-314a (residue-coverage novelty), MECH-320 (reward-rate EWMA; its only F-coupling is inverse and
protective), MECH-260 (action-history FIFO), or MECH-295 (drive·proximity) — these are F-independent
and durable. Consequently Q-052 is **mixed**, not uniformly structural: the magnitude fix (A,
EXQ-573 static scaling) is durable for the F-independent channels (MECH-313 is the cleanest lever),
while the MECH-333/334 structural critical-period mechanism (B) is needed specifically for the
F-dependent curiosity sub-channels — or those channels should be re-grounded on an F-independent
novelty signal.
