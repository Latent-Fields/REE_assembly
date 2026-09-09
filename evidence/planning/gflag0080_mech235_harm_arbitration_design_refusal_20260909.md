# GFLAG-0080 / MECH-235 -- the "re-run 811a with z_harm_a logged" design is decided by construction; REFUSED at design

- **Status:** design refusal record. **No experiment was queued.** No flag was resolved (GFLAG-0080 stays `open`; resolution is `/governance`'s call).
- **Written (UTC):** 2026-09-09T00:24Z by session `confident-panini-0cdba7` (Mac `DLAPTOP`, umbrella worktree; claims `confident-panini-0cdba7`, `-records`).
- **Campaign:** wave-6 S6 item 2 (`science_wave_campaign_plan_20260908b.md` section 3 S6), chip `chip-20260901-gflag0080-mech235-arbitration-rerun`.
- **Claim:** MECH-235 (`candidate`) -- "vmPFC arbitration continuously weights model-based (E3) vs model-free (E1) contributions ... unexpected threat (urgency signal) shifts weighting toward model-free."
- **Flag:** GFLAG-0080 (`contested_disposition`, raised 2026-08-28 by `thought-digestion-v3closure-20260828`; narrowed by `governance_flag_triage_20260901.md`: the graded weight EXISTS -- SD-081/MECH-477 `_arbitrate_dual_system`, validated by V3-EXQ-811a PASS 2026-07-24 -- but arbitrates DEPTH under UNCERTAINTY, a different independent variable from MECH-235's urgency/commitment).
- **Chip's ask:** queue a lettered re-run of V3-EXQ-811a with `z_harm_a` logged per tick, "powered to detect whether w moves with z_harm_a over and above the relative-uncertainty relationship 811a already measured", and -- its own escape clause -- "if you cannot [separate a genuine harm contribution from that near-deterministic existing relationship], say so and report the design as blocked rather than queueing something uninterpretable." This record takes the escape clause, on the source.

---

## 1. Sequencing gate (GFLAG-0072) -- satisfied, and not applicable to this DV

The chip was held behind `chip-20260901-gflag0072-class-entropy-ceiling` (the committed-class-entropy ceiling that makes ARC-065-lineage nulls uninterpretable). That chip resolved `done` 2026-09-01: the ceiling is real but ALREADY REMEDIATED for the lineage that needed it (V3-EXQ-955 at `class_floor 5`, governance-ratified 2026-08-29), while the default of 2 still stands at ~276 call sites for ARC-065/439/441.

For THIS design it is **not applicable**: the DV is the continuous arbitration weight `w` in (0, 1) and its relation to a continuous harm signal, not committed-class entropy. No `support_preserving_min_first_action_classes` floor caps `w`. The interpretability basis of a null here is therefore not the class-entropy ceiling -- it is the construction argument in section 2, which is worse: the null is not merely uninterpretable, it is guaranteed.

## 2. The finding: `w` has no harm input, so "does harm move w over and above relative uncertainty" is FALSE by construction

Read from `ree-v3/ree_core/predictors/e3_selector.py` at HEAD (2026-09-09), `_arbitrate_dual_system` (def at :1623):

```
u_h   = max(0, habit_uncertainty)                 # :1758  caller-supplied (agent.py :9372-9388)
u_p   = max(0, self._running_variance)            # :1759  E3's own z_world PE-MSE EMA
u_h_n = u_h / (u_h + EMA(u_h) + eps)              # :1770  normalised against own EMA baseline
u_p_n = u_p / (u_p + EMA(u_p) + eps)              # :1771
w     = sigmoid(gain * (u_h_n - u_p_n) + bias)    # :1775  gain=4.0, bias=0.0 defaults
```

`w` is a closed-form function of exactly two inputs. Where they come from:

- `habit_uncertainty` (`ree_core/agent.py` :9372-9388): `1 - familiarity_tracker.query(z_world)` (preferred) or `e3._novelty_ema` (fallback). Neither reads `z_harm_a`, `z_harm_s`, `harm_bridge`, or any harm quantity.
- `_running_variance` (`e3_selector.py` :4410-4416, `update()`): `prediction_error = actual_z_world - predicted_world`, i.e. the E3-side **z_world** one-step prediction error of the selected trajectory, EMA-smoothed. Not a harm prediction error.

`z_harm_a` IS passed into `_arbitrate_dual_system` (`select()` :3122-3135 forwards `z_harm_a`, `harm_bridge`, `harm_forward_model`, `z_harm_s_current` as `**score_kwargs`) -- but only to `score_trajectory(...)` at :1725-1736, which produces the HABIT score vector that gets blended. Harm shapes the two score vectors `z_h` / `z_p`; it does not touch `w`.

Consequences for the proposed design:

1. **The partial correlation of `w` with `z_harm_a` given `(u_h_n, u_p_n)` is identically zero** -- not small, not noisy: zero, because `w` is a deterministic function of those two numbers (811a measured `rho_w_vs_relative_uncertainty = 1.0` for exactly this reason). The chip's stated readout, "w moves with z_harm_a OVER AND ABOVE the relative-uncertainty relationship", cannot be anything but null.
2. **The only route by which harm can co-vary with `w` is indirect**: a harmful transition may also be a z_world-surprising one, raising `_running_variance`, raising `u_p_n`, LOWERING `w` -- i.e. shifting control toward the myopic/habit read. That is MECH-235's predicted DIRECTION ("unexpected threat shifts weighting toward model-free"), but it is mediated by generic surprise, and a design matching harm-surprising against equally-surprising harmless transitions on `|z_world PE|` would find zero difference, again by construction.
3. **Logging `z_harm_a` therefore cannot test MECH-235's mechanism** ("harm prediction error moves the arbitration") because the substrate has no such coupling to detect. A run would return the guaranteed null, cost cloud compute (811a: 38,452 s), and -- via the flag's disposition -- read as evidence AGAINST MECH-235 when it is evidence of nothing.

This is the `criterion_exceeds_achievable_range` class in its purest form: the DV cannot move in response to the manipulation by arithmetic, at every seed, on every substrate. Per `/queue-experiment` Step 3 DV-symmetry rule, an arm whose manipulation is invisible to its DV by construction is scoped OUT, never queued as `mixed`.

## 3. What WOULD test MECH-235's harm leg -- a build, not a run

Work-graph classification (`work_graph_debt_vocabulary.md`): **`complicated (buildable)`**, route `/implement-substrate`, NOT `/queue-experiment`. The named build: give the arbitrator a harm-prediction-error input. Two candidate shapes, either of which converts the question into a falsifiable ON/OFF:

- **(a) Augment `u_planned`** with a harm-PE component (e.g. `u_p := u_p + lambda_h * harm_pe_ema`, where `harm_pe` is the E3 `harm_eval`/`harm_forward_model` one-step error on the executed transition), default `lambda_h = 0.0` for bit-identity. Falsifier: ON vs OFF on a harm-surprise-controlled environment; readout `w` conditioned on harm-surprising vs matched harmless-surprising transitions; MECH-235 predicts `w` drops MORE on harm-surprising transitions under ON only.
- **(b) A `z_harm_a`-driven bias term** on the sigmoid (`bias := bias - kappa * z_harm_a_norm`), default `kappa = 0.0`. Same falsifier; a cruder coupling (tonic, not PE-based) and less faithful to the Dolan & Dayan mechanism the claim cites.

Either way the substrate change is small (one config knob, one line in `_arbitrate_dual_system`, one contract pinning bit-identity at the default), and the experiment that follows is a genuine new letter off 811 with a criterion that CAN fail. Recorded here as the owed follow-on; NOT written to `substrate_queue.json` by this session (chip scope: queue-experiment only; governance owns the disposition via GFLAG-0080).

## 4. Interaction with the standing flag

GFLAG-0080's surviving content after the 2026-09-01 triage was: "SD-081 arbitrates DEPTH under UNCERTAINTY, whereas MECH-235 claims arbitration on URGENCY and commitment. Different independent variables." This record confirms that reading from the source and sharpens it: the URGENCY/harm independent variable has **no path into `w` at all**. The claim's own text names the MECH-091 urgency interrupt (`E3Config.urgency_interrupt_threshold`, a hard binary) as "the substrate implementation of this arbitration shift" -- so on the current substrate MECH-235's harm leg is implemented only as the binary switch the claim says the arbitration is NOT. That is the contested disposition, restated with the line numbers. Recommended governance action: keep MECH-235 `candidate`, mark the harm/urgency leg `substrate_conditional` on build (a)/(b) above, and close GFLAG-0080 against this record + `governance_flag_triage_20260901.md`.

## 5. STOP-CHECK trail

- `task_claim.py check --resources ree-v3/experiments` at 2026-09-09T00:09Z: whole-file overlap with IGW-233 (INV-095) and W6-S5b, opened `--allow-overlap` (different experiments; queue appends are serialised by `ree_commit.py`).
- GFLAG-0080 `status: open` in `governance_flags.v1.json` at 2026-09-09T00:15Z (checked; not resolved by this session).
- 811a manifest re-read: `claim_ids [MECH-477, MECH-163]`, `outcome PASS`, arbitration stats recorded per condition (familiar/novel) -- no `z_harm_a` series, as the chip states.
- Chip `chip-20260901-gflag0080-mech235-arbitration-rerun`: claimed 2026-09-09T00:16Z, resolved `done` (refusal) with this record as the note.
