# SD-034: Governance Closure Operator

**Claim ID:** SD-034
**Subject:** governance.closure_operator
**Status:** IMPLEMENTED 2026-04-20 (validated 2026-04-21; design doc backfilled 2026-04-27)
**Registered:** 2026-04-20
**Depends on:** SD-033 (governance cluster), SD-033a (lateral PFC analog rule_state), MECH-090 (BetaGate commitment latch), MECH-260 (dACC action-class No-Go), MECH-094 (hypothesis tag write gate), SD-032a (SalienceCoordinator), SD-032b (dACC analog)
**Blocks:** EXP-0156 / V3-EXQ-460 (verified-but-not-released), EXP-0157 / V3-EXQ-461 (delayed-reward persistence), EXP-0162 / V3-EXQ-466 (satisficing / residue discharge), EXP-0164 / V3-EXQ-468 (commitment vs contradiction). All landing-diagnostic variants PASSed 2026-04-21.

## Problem

REE-V3 has the substrate for Go (basal-ganglia-like gate, SD-032a operating-mode register), Hold (MECH-090 BetaGate bistable commitment latch), and No-Go (MECH-260 dACC action-class suppression). What is missing is the operator that turns evaluation **off** on successful completion. Without it, a committed rule_state that has been satisfied keeps being evaluated, keeps consuming mode budget, keeps generating residue, and the agent cannot disengage. The 2026-04-20 GAP MEMO and the OCD thought set identify this as the load-bearing missing piece in the governance layer — verified-but-not-released, delayed-reward-persistence, and satisficing failures all trace back to the absence of a closure operator.

## Solution

Implemented as `ree_core/governance/closure_operator.py` (`ClosureOperator`, `ClosureOperatorConfig`, `ClosureEvent`). On detection of rule-completion, the operator emits a five-part coordinated "done" token:

1. **Beta release** — calls `MECH-090 beta_gate.release()` to drop the commitment latch.
2. **No-Go injection** — calls `MECH-260 dacc.inject_nogo(action_class, count)` to bias the just-completed action class toward suppression on the next cycle. Uses the same FIFO mechanism as execution-recorded suppression but is semantically distinct (closure-driven rather than execution-recorded).
3. **Residue discharge** — calls `ResidueField.discharge_domain(z_world, factor, radius)` for rule-domain multiplicative decay on RBF weights. A hard 1e-6 floor preserves the "residue cannot be erased" invariant; valence_vecs are not modified so 4-component valence is preserved (replay prioritisation remains faithful).
4. **Salience signal** — calls `SalienceCoordinator.update_signal("closure_event", value)`, which re-biases mode affinity toward `internal_planning` via registered affinity_weights (default `internal_planning=0.5`).
5. **dACC PE reset** — calls `dacc.reset_episode_pe()` and optionally installs a `dacc_pe_cap` (MECH-268 saturation/reset coupling).

### Completion detection

Two paths.

**Tick path** (default): the operator checks at every `select_action()` whether
- `||rule_state(t) - rule_state(t-1)|| < closure_rule_delta_threshold` for `closure_stable_ticks` consecutive ticks
- AND `beta_gate_elevated == True`
- AND `current_mode in allowed_closure_modes`
- AND `sd_033a write_gate >= closure_min_sd033a_gate`
- AND `||rule_state|| > 0` (guard against firing on an unset rule_state).

**Explicit path**: `emit_closure(action_class, z_world, bypass_mode_conditioning=False)`. The experiment hook for controlled ablations.

### Mode conditioning as falsifiability predicate

Mode conditioning generalises MECH-094's hypothesis-tag write gate to the closure operation. Closure firing is blocked in `internal_replay` and `offline_consolidation` modes via `allowed_closure_modes` and via the `sd_033a` gate floor (`write_gate("sd_033a") = 0.05` in internal_replay). The architectural commitment is testable: if MECH-090 + MECH-260 + MECH-094 tuning *without* closure produces the same behavioural signature as closure-with-MECH-094-restriction in follow-up behavioural variants, SD-034 is over-specification. The mode-conditioning predicate is the falsification handle.

### ResidueField.discharge_domain API (added in same pass)

Multiplicative decay + sign-aware 1e-6 floor + radius-scoped in-domain selection via squared-distance comparison against `(radius * bandwidth)^2`. `valence_vecs` are NOT modified — the 4-component valence is preserved so replay prioritisation remains faithful.

### DACCAdaptiveControl extensions

- `dacc_pe_cap` config field (absolute cap on precision-weighted PE after closure).
- `inject_nogo(action_class, count)` method.
- `reset_episode_pe()` method (distinct from full `reset()` — preserves `_action_history` where the just-injected No-Go lives).

### Agent wiring

`REEAgent.__init__` instantiates `closure_operator` when `use_closure_operator=True` (requires `use_lateral_pfc_analog=True` and `use_dacc=True`; salience coordinator optional). `select_action()` calls `closure_operator.tick()` after action emission with current `z_world`, `argmax(action_class)`, `operating_mode`, and `sd_033a` gate. `reset()` calls `closure_operator.reset()`. `register_on_coordinator()` wires `closure_event` into `salience.config.affinity_weights` at init.

### Config surface

- `REEConfig.use_closure_operator` (bool, default False) — master switch
- `closure_rule_delta_threshold` (default 0.001)
- `closure_stable_ticks` (default 3)
- `closure_require_beta_elevated` (default True)
- `closure_min_sd033a_gate` (default 0.5)
- `closure_nogo_injection_count` (default 3)
- `closure_residue_discharge_factor` (default 0.5)
- `closure_residue_discharge_radius` (default 1.5)
- `closure_signal_value` (default 1.0)
- `closure_reset_pe_ema` (default True)
- `closure_pe_cap_after` (default None)
- `closure_signal_affinity_internal_planning` (default 0.5)

### Backward compatibility

`use_closure_operator=False` by default → `agent.closure_operator is None`; every integration site is a no-op. Existing experiments unaffected. Bit-identical with `closure_signal_affinity_internal_planning=0.0` and the master switch off.

## Architecture Context

SD-034 is the first substrate landed in the SD-033 governance cluster (see `evidence/planning/sd033_governance_plan.md`). It is also the first consumer of the MECH-261 write-gate registry's mode-conditioning predicate. Subsequent substrates in the cluster — MECH-266 (asymmetric mode hysteresis), MECH-267 (mode-conditioned hippocampal proposals), MECH-268 (dACC conflict saturation) — are independent extensions of existing modules; SD-034 is the only one that is a new module / new operator.

The five-part signal collocates several biologically-observed end-of-sequence signatures: OFC sequence-completion cells (Rich & Shapiro 2009; Schuck 2016), task-set disengagement (Collins & Frank 2014), and the post-completion No-Go refractory period (Mayr & Keele 2000). The collocation hypothesis is the architectural commitment: V3 treats them as one operator, EXP-0156 and EXP-0162 probe whether they should remain co-located or split.

## Biological Grounding

- **Rich & Shapiro 2009** — rat PFC strategy-switch neurons; transient activity at strategy completion ([DOI 10.1523/JNEUROSCI.4732-08.2009](https://doi.org/10.1523/JNEUROSCI.4732-08.2009)).
- **Schuck 2016** — human OFC encodes task-stage / state-space position; supports a "where in the sequence am I?" detector that closure can read from ([DOI 10.1016/j.neuron.2016.08.019](https://doi.org/10.1016/j.neuron.2016.08.019)).
- **Collins & Frank 2014 (OPAL)** — D1/D2 striatal opponent dynamics produce task-set disengagement under DA modulation ([DOI 10.1037/a0037015](https://doi.org/10.1037/a0037015)).
- **Mayr & Keele 2000** — backward inhibition: post-completion refractory period on re-entry to the just-abandoned task set, six replicating experiments ([DOI 10.1037/0096-3445.129.1.4](https://doi.org/10.1037/0096-3445.129.1.4)).
- **Smith & Graybiel 2013** — dual-operator action-bracketing in striatum + infralimbic cortex; flags closure substrate may be multi-region rather than OFC/ACC-only ([DOI 10.1016/j.neuron.2013.05.038](https://doi.org/10.1016/j.neuron.2013.05.038)).

The 2026-04-27 SD-034 lit-pull (`evidence/literature/targeted_review_sd_034/`) recommends:
1. Implement No-Go as graded score_bias decay rather than hard refractory gate. **The V3 implementation matches**: MECH-260's FIFO action-class history produces a graded recency-bias suppression rather than a binary block.
2. Closure-detection signal can fire from multiple substrates (not OFC/ACC only). **The V3 implementation is consistent**: the substrate commitment is the rule-state-delta-stability detector, not anatomical localisation. The architectural choice is substrate-agnostic.
3. Post a transient negative bias to the just-completed rule via SD-033a's per-candidate projection. **The V3 implementation differs slightly**: closure does not modify SD-033a's bias weights directly; the negative bias is delivered through MECH-260 action-class suppression. The downstream effect is similar (next-cycle bias against the just-completed action class) but the substrate is different (action-class FIFO rather than rule-bias projection). For V4 reconsideration: routing the post-completion bias through SD-033a's existing per-candidate bias projection would unify the bias channels.

## What This SD Enables

Validation experiments queued + run + PASSed 2026-04-21:
- **V3-EXQ-460** (EXP-0156 verified-but-not-released): substrate-landing diagnostic, 6 sub-tests covering backward compat, wiring, beta release, No-Go, pe reset, mode conditioning. **PASS** on smoke.
- **V3-EXQ-466** (EXP-0162 satisficing / residue discharge): residue-discharge landing diagnostic, 5 sub-tests covering near attenuation, far spared, invariant preserved, closure→discharge end-to-end, distant-z spares. **PASS** on smoke.
- **V3-EXQ-468** (EXP-0164 commitment vs contradiction): coupled SD-034 + MECH-268 PE-saturation diagnostic. **PASS** on smoke.

Behavioural variants with full E3 task loop + tolerance-band completion env are deferred. Both variants depend on phased rule_state training (not yet on the V3 roadmap) and on a CausalGridWorldV2 task-loop env extension that has not been authored.

## Related Claims

- **MECH-260** — dACC action-class suppression. Closure inject_nogo extends the existing FIFO mechanism with a closure-driven entry point.
- **MECH-261** — write-gate registry. Closure consumes the mode-conditioning predicate to gate firing in internal_replay / offline_consolidation modes.
- **MECH-262** — rule-bias projection from SD-033a. Closure reads SD-033a write_gate as a precondition.
- **MECH-094** — hypothesis tag / categorical write gate. Closure mode-conditioning generalises this to the closure operation.
- **MECH-268** — dACC PE saturation. Closure couples to MECH-268 via `closure_reset_pe_ema` and the optional `dacc_pe_cap` install.

## Anchor Documents

- Anchor doc: `REE_assembly/evidence/planning/sd033_governance_plan.md`
- Source thought file: `docs/thoughts/2026-04-20_ocd4.md`
- Lit-pull review: `evidence/literature/targeted_review_sd_034/` (6 entries, 2026-04-21 + 2026-04-27)
- Implementation notes (full): `ree-v3/CLAUDE.md` lines 1476-1555
