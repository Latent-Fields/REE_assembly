# Red-team -- claim_synthesis MECH-157 and MECH-039 design-option proposals (2026-09-25)

- **Date:** 2026-09-25T07:49Z
- **Reviewer:** adversarial red-team subagent (read-only; this file is the only write)
- **Targets:** `claim_synthesis_MECH-157_20260925.md`, `claim_synthesis_MECH-039_20260925.md`
- **Code measured:** ree-v3 `main` @ `2ce89ce` (same sha the docs cite)
- **Method:** every Section-1 premise re-measured against live code; the recommendation tested against the claim's registered `what_would_answer`; ownership checked against claims.yaml; missing options looked for in the substrate.

Verdicts: **MECH-157: CONTESTED. MECH-039: CONTESTED.** Both recommendations survive in spirit; each has a specific defect that would produce a vacuous or mis-attributed first run if built exactly as written.

---

## A. MECH-157 (Option A recommended) -- CONTESTED

### A1. Premises

| # | Doc claim | Re-measured | Holds? |
|---|---|---|---|
| P1 | `alpha_world` is the observation-vs-prior blend; `prec_world` is only a magnitude gain | `stack.py:1584` `z_world = alpha_world*z_world + (1-alpha_world)*prev_state.z_world`. `stack.py:1022-1027` `prec_world = sigmoid(world_precision_logit)` (an **input-independent learned parameter**, `stack.py:947`) then `z_world = z_world * prec_world`. | **Yes**, with one sharpening: the "prior" in the EMA is the agent's own previous smoothed `z_world`, i.e. temporal smoothing, not a generative prior. `prec_world` is not merely a magnitude gain, it is a *constant per-dimension* gain -- it cannot be "precision of sensory data" under any reading, which strengthens P2. |
| P2 | `compute_prediction_error` has zero callers | `/usr/bin/grep -rn compute_prediction_error --include='*.py' ree_core experiments tests coordinator` -> only the def at `stack.py:1716`. No reader of `state.precision["world"]` outside `stack.py`. | **Yes.** |
| P3 | Waking `hippocampal.replay()` output is discarded | `agent.py:11640` assigns `replay_trajs`; the only other mention is the sibling assignment at `:11633`. Never read. **But** the offline paths DO consume it: `agent.py:13858` `forward_trajs` is scored (`_score_trajectory`, MECH-365 routing) and `:13946` `extra` feeds `terrain_scores`; `module.py:3258` `diverse_replay` re-consumes `replay()`. | **Partly.** True for the quiescent-E3 waking path only. The doc's Consequence ("a replay-rate knob ... gives a degenerate consumer on the waking path") is correct as scoped, but the `offline_consolidation` row of the claim's own table -- the Replay mode -- has a live consumer. The doc does not say so. |
| P4 | Falsifier excludes write gating as the DV locus | `claims.yaml:22256` "Consumer / boundary: The precision-application path on the shared E1 substrate ... not write gating or CEM noise". | **Yes as DV locus** -- but overstated as exclusion: the same falsifier's Manipulation lists "MECH-261 write gating" among the consumers to ablate one at a time. Option C is excluded as the DV, not from the design. |
| P5 | Mode dimension not live | `config.py:3043` `mode_conditioning_enabled=False`; `:4465` `use_salience_coordinator=False`; the 2026-09-18 zero-delta measurement is in the falsifier text. | **Yes.** |
| P6 | No Mixed mode | `salience_coordinator.py:75-80`. | **Yes.** |
| P7 | Rollout consumer exists | `module.py:2001,2027` gate on `mode_conditioning_enabled`. | **Yes.** |

**Premise the doc did not state and needed to (P8):** the shipped `alpha_world` default is **0.3** (`stack.py:1539` fallback; `config.py:23-53` warns on every `from_dims()` call that omits it; SD-008 `stable` requires >= 0.9). At default the sensory:prior ratio in *external_task* is already 0.3:0.7 -- the claim's "External = high sensory" row is violated before any mode term exists.

### A2. Recommendation -- the defects

**D1 (load-bearing). Option A's DV is analytically entailed by its manipulation.** The doc says the registered DV "becomes computable without new recorders" as `alpha_eff/(1-alpha_eff)`. But `alpha_eff = alpha_world * sum_m operating_mode[m] * mode_alpha_world_scale[m]` is a deterministic function of the config dict and the mode vector. "Precision routing profiles differ systematically by mode" then holds by construction for any non-constant dict -- the CONFIRMING leg of the falsifier is vacuous on that DV. This is the exact shape MECH-025's precondition names ("the scored DV must not be a monotone function of the [manipulation] itself") and the MECH-449 937b failure (C1 "only reachable value is 1.0"). The falsifier's non-vacuous content is the OTHER half of its DV sentence -- "mode differences producing measurable downstream consequences" -- which the doc mentions only as a risk ("must show it is mode-locked"). The honest DV under Option A is the SD-008 `event_selectivity_margin` of `z_world`, keyed by coordinator mode (a readout V3-EXQ-023/040 already implement), plus the orthogonality control; `alpha_eff` is a manipulation check, not the DV.
- Confirmer: `sed -n 1584p /Users/dgolden/REE_Working/ree-v3/ree_core/latent/stack.py` -- the only mode-dependent term in the proposed build is the coefficient; nothing else on that line can move with mode.

**D2. Multiplicative scale on the shipped default silently violates SD-008 in external_task.** The doc says "`external_task` stays at >= 0.9 to keep SD-008". With `alpha_world=0.3` at default and a *scale* dict, external_task at scale 1.0 gives 0.3; reaching 0.9 needs scale 3.0 and a clamp, and "bit-identical when OFF" then means bit-identical to a substrate that is already below the SD-008 floor. The knob must be a per-mode **absolute alpha** (or the run must pin `alpha_world=0.9` and the doc must say so), and the external_task cell must be reported per SD-008's own precondition ("SD-008 alpha_world pinned and reported at 0.9", `claims.yaml:14741`).
- Confirmer: `/usr/bin/grep -n 'alpha_world' /Users/dgolden/REE_Working/ree-v3/ree_core/latent/stack.py | head -3` and `sed -n 42,53p /Users/dgolden/REE_Working/ree-v3/ree_core/utils/config.py`.

**D3. "Hippocampal drive = 1 - alpha_eff" is a relabel, not a narrowing.** `(1-alpha_world) * prev_state.z_world` is the agent's *own previous smoothed state*. No hippocampal content, no E1 generative prediction, no rollout enters `z_world` on this path (grep for any hippocampal/anchor/recall write into `z_world` in `agent.py` returns nothing; the only internally-generated additive term into `z_world` is the hierarchical `world_topdown(z_beta)` at `stack.py:1017`). So under Option A, "Internal mode" = `z_world` frozen near its last value -- perceptual decoupling, yes (the Baird/Villena-Gonzalez phenotype), but NOT "generative imagination on the same E1 substrate", which is the claim's stated content (`modes_of_cognition.md#mech-157`: "the same deep world model supports both perceptual coupling (External) and generative imagination (Internal)"). The doc's own Section 2 concedes "no path at all by which hippocampal content drives the shared z_world" and then defines the missing quantity as the complement of the one that exists. Kremin & Hasselmo 2007 does not license this: their reciprocal balance is afferent input vs **recurrent retrieval** -- two content sources -- not observation vs its own EMA. The proposed note-level narrowing therefore collapses a claim dimension. If the user accepts Option A, the narrowing must be worded as what it is ("hippocampal drive is NOT operationalised; the Internal row is tested only on its sensory-decoupling half") rather than as an equivalence -- and the `claim_ids` accuracy rule then argues the first run tags MECH-157's sensory-gain half only.
- Confirmer: `sed -n 1584p stack.py`; `/usr/bin/grep -n "hippocamp\|anchor\|replay" ree_core/latent/stack.py | /usr/bin/grep -i "z_world ="` returns nothing.

**D4. SD-008 conflict is real but bounded.** SD-008 (`stable`) says event suppression below 0.9 is a defect. Option A makes it the intended phenotype in internal/replay modes. Not a contradiction *if* the narrowing states that SD-008's floor is scoped to the external_task regime -- but that is a second claim-text touch (SD-008 note), which the doc does not list among the owed governance actions. Add it.

**Is a non-recommended option better?** No. B is worse for the reasons given (P2 magnitude confound; goal-retrieval gain is an action-axis channel). C tests MECH-261/ARC-038. D is honest but unbounded. The right call is **A as amended** (D1-D3) or the omitted **Option E** below.

### A3. Ownership

- **MECH-249** (`candidate`): "Acetylcholine/noradrenaline balance implements ... hippocampal write profiles as a continuous neuromodulatory state variable" -- cites Hasselmo explicitly. The doc's Option-A narrowing ("one reciprocal balance ... following Kremin & Hasselmo") is MECH-249's thesis restated on the E1 read side. Not a contradiction, but the narrowing should cite MECH-249 as the owner of the neuromodulator-balance reading, and MECH-249's own precondition ("mode identity must be measured independently rather than assigned from the same two inputs") is exactly D1.
- **MECH-245** (`candidate`, hallucination = top-down dominance): its Manipulation is "substitute the agent's own predicted z_world for the encoder's observed z_world at the perception boundary". That is the genuine sensory-vs-internal blend on `z_world` -- and it is owned there. Option E below borrows it; the doc should say so.
- **INV-067** (`candidate`, verisimilitude = precision-weighted ascending vs descending correspondence): adjacent, definitional; no conflict.
- **SD-008** (`stable`): see D4.
- **ARC-038**: owns the `hc_viability` consumer build (its precondition: "A consumer must exist that ingests replayed trajectories into the viability map ... routed through a gate target that MECH-261 actually reads"). Doc correctly defers Option C there.

### A4. Missing option

**Option E -- mode-scaled blend of `z_world` toward E1/E2's own predicted `z_world` (the SELF-1/DR-13 pattern, world side).** The substrate already implements exactly this shape for `z_self`: `stack.py:1561-1567` blends the recurrent `z_self` toward `self_e1_anchor` (`agent.py:5568`, sourced from `_e1_predicted_next_z_self`, `agent.py:6732`) with weight `self_recurrence_e1_coupling` (`config.py:200-201`, default OFF). `E2WorldForward` produces `z_world_pred` (`e2_world.py:12-13,255`). A `world_e1_coupling` scaled per mode (external ~0, internal/replay high) makes `1-alpha_eff` genuinely *internally generated content on the shared E1 state* -- the claim's actual assertion -- with the same cost as Option A (one dict, one blend, one diagnostic) and no invented hippocampus->E1 edge (the generative source is the world model the claim names, not the hippocampus). It also gives a non-entailed DV: the divergence between `z_world` and the encoder's instantaneous estimate under fixed mode weights depends on the *trained model*, not on the config. Caveat: this is MECH-245's manipulation used as a mode-conditioned regime rather than a failure mode, so the first run must tag carefully. Recommend adding E to the table; A-vs-E is the real decision.

### A5. Hygiene (move nothing)

- "inside `LatentStack.sense`" -- there is no `sense`; the method is `encode` (`stack.py:1351`). `encode` takes no `operating_mode`; the build needs a new kwarg threaded from `agent.py:5586`.
- `stack.py:946-947` -> `:947`; `:1019-1026` -> `:1022-1027`; `salience_coordinator.py:234-240` -> `:235-240`.
- Section 3 lit entries are not ingested (doc says so); fine, but "Based on articles retrieved from PubMed" should be tagged design-grounding-only per the doc's own Section 3 last line.

---

## B. MECH-039 (Option 1 recommended) -- CONTESTED

### B1. Premises

| # | Doc claim | Re-measured | Holds? |
|---|---|---|---|
| P1 | `get_readiness()` public, live-called | `commit_readiness.py:324` public; `agent.py:7588` calls it inside the MECH-342 maintenance-release block (`:7557` guard `self.maintenance_release is not None and self.beta_gate.is_elevated`). `use_commit_readiness=False` (`config.py:5840`). | **Yes.** Note the live call is reached only under `use_maintenance_release` AND beta elevated; when `commit_readiness` is None the axis is inert. The "safe flag set" doc task the doc names is real. |
| P2a | PAGFreezeGate, default OFF | `freeze_gate.py:381` `is_active`; `config.py:7110` `use_pag_freeze_gate=False`. Consumer: `agent.py:11013-11030` replaces the action with a no-op. | **Yes.** |
| P2b | Habenula abort, default OFF, a commit-abort | `config.py:6533` `use_habenula_decommit=False`; `closure_operator.py:191` `habenula_abort_enabled=False`; `habenula_tick` (`:505`) fires `_fire` (beta release + No-Go + residue discharge) only when `use_closure_operator` AND beta elevated AND `delta_t < threshold`; `agent.py:11741-11756` tears down the committed trajectory. | **Yes** -- it is a **post-commit abort**, fires only while committed. MECH-053's 2026-09-21 disposition (R6) explicitly classes this path as "a wrong-boundary substitute for the pre-commit veto claim". For MECH-039 the post-commit interrupt is arguably the *right* boundary (an interrupt of the current regime), but the doc should say it is choosing the boundary MECH-053 rejected, and why. |
| P2c | MECH-449 safety No-Go, default OFF, "fail-open guard never overrides it" | `config.py:2225` `use_gng_endogenous_safety=False`; needs `use_go_nogo_constitution` too (`agent.py:10460`). **The override claim is false in the case that matters:** `e3_selector.py:2437-2446` -- when every eligible candidate is No-Go'd, `pool = safe_pool if safe_pool.numel() > 0 else all_idx` selects the strongest-F candidate **even if it is safety-vetoed**. | **Partly false.** In the all-catastrophic regime (the emergency condition Option 1's hazard-onset manipulation is designed to elicit) the veto is overridden and the agent commits anyway. |
| P3 | No emergency mode; adding one is circular | `salience_coordinator.py:75-80`. | **Yes**, but see D6. |
| P4 | Arousal assemblable from `e3.volatility_estimate` + `clock.e3_steps_per_tick` | `e3_selector.py:1031`; carried. | Not re-measured by the doc; accepted. |
| P5 | 3/6 channels live | Carried from 2026-09-02. | Not re-measured; accepted. |

**Premise the doc missed (P6): there are more than three veto-shaped producers, and the two omitted ones are the only ones that actually FORCE a coordinator transition.** (i) **SD-035 CeA fast route** (`use_cea_analog=True` by default, `config.py:6968`; needs `use_amygdala_analog`, default False, `:6962`): `cea_fast_prime` is registered on the coordinator's `salience_weights` at 0.5 (`agent.py:2576`) and `cea_mode_prior` writes a mode prior (`agent.py:2491`, MECH-046) -- its registered falsifier is literally "time-to-mode-switch on threat-cue onset". (ii) **SD-037 broadcast override** (`use_broadcast_override=False`, `config.py:7183`): `override_signal` is an `affinity_weights` input to the coordinator (`agent.py:2785`) and feeds the freeze gate (`agent.py:10980`). These are the substrate's existing "fast interrupt channel that can force a transition even when the rest of the control state reflects a prior regime" (`control_plane.md#mech-039`). The doc's "which of three" framing is under-counted.

### B2. Recommendation -- the defects

**D5 (load-bearing). None of Option 1's three constituents can force a multi-channel transition, so the composite cannot test the claim's distinctive prediction, and the doc's "yes (onsets)" cell is unsupported.** Freeze replaces the action (one channel: readiness/motor gating). Habenula abort releases beta (one channel: commitment). MECH-449 prunes the candidate set inside E3 select (no channel; and see P2c, it is overridden in the all-unsafe case). None touches the coordinator, precision routing, or arousal. Any "multi-channel jump at veto onset" observed under Option 1 will be the *hazard* driving arousal (volatility), freeze, and safety No-Go in parallel from the same `z_harm_a` -- i.e. the lockstep degeneracy MECH-039's precondition names ("a run where all channels move in lockstep cannot discriminate"). The doc levels a circularity charge at Option 2 and does not notice that Option 1 has a common-cause version of the same problem. The constituent that dissociates is the habenula abort (driven by signed RPE `delta_t`, not harm level) -- which is also the one whose own claim (MECH-053) says it is the wrong boundary for a veto.
- Confirmer: `sed -n 2437,2446p ree_core/predictors/e3_selector.py` (override); `/usr/bin/grep -n "salience\|coordinator\|operating_mode" ree_core/pag/freeze_gate.py` returns nothing (freeze has no path into the coordinator).

**D6. The circularity argument against Option 2 is sound but not specific to Option 2.** The "replay/learning scheduling" channel is already label-derived for the four existing modes (MECH-261 write gates and MECH-267 rollout are functions of `current_mode`). So whichever option runs with `use_salience_coordinator=True`, that channel is partly the label. Option 1 is only non-circular if the coordinator is OFF (default) or its derived channels are excluded from the clustering. The doc should state that constraint; otherwise "Circularity risk: none" for Option 1 is wrong.

**D7. Option 1's cost/risk rows understate.** Option 1 includes the MECH-449 producer, so it inherits the "heavy flag stack" (`use_go_nogo_constitution`, F-eligibility demotion, live modulatory accumulator, K>=2, 200-sample warmup at `agent.py:4716`) the doc lists only as an Option 3 risk, PLUS `use_pag_freeze_gate` PLUS `use_closure_operator`+`use_habenula_decommit`. Further, the MECH-449 producer has **never run**: V3-EXQ-1090 is still queued (`experiment_queue.json:11`), and its landing commit `da9221c` records "red-team CONTESTED -> F2 partly fixed". Its non-degeneracy is unmeasured (MECH-449's own precondition: at shipped defaults the No-Go signal was analytically entailed, 937b). Option 1 "small build" is a small *accessor* on top of the largest un-smoked flag combination in the table.

**Is a non-recommended option better?** As written, no -- but the omitted option is (B4). Between the written four, Option 3 is *more* honest than Option 1 about what it can test ("weakly (pruning, not interrupt)"), and Option 1 should carry the same "weakly" until D5 is addressed.

### B3. Ownership

- The proposed MECH-039 note ("named modes are hypothesised channel-space regions identified by eliciting condition, not SalienceCoordinator enum entries") does not contradict SD-032a/MECH-261 (soft vector) and is consistent with ARC-016 (`stable`). No conflict.
- Using the habenula abort as a MECH-039 veto constituent sits on the boundary MECH-053's disposition rejected (R6, `claims.yaml` MECH-053 SUBSTRATE block: "Pre-commit readiness/veto boundary required by MECH-053, distinct from ARC-108 post-commit release"). Not a contradiction for MECH-039, but the two claims would then read the same producer at opposite boundaries; the note should say which one MECH-039 tests.
- MECH-040's falsifier already names `override_signal/freeze-gate` as the veto-side footprint and SD-069/softmax temperature as the volatility-side; Option 1's arousal proxy (`volatility_estimate`) and veto composite therefore overlap MECH-040's own DV pair. Tag both or neither, per the claim_ids accuracy rule.

### B4. Missing option

**Option 5 -- V-E: SD-035 CeA fast-prime / SD-037 override_signal as the veto channel (read-only), emergency as condition-elicited (E-A).** These are the existing producers with a live path INTO the coordinator (`agent.py:2576,2785`), so a veto onset can actually force the mode-switch the claim predicts, and MECH-046's registered DV (time-to-mode-switch on threat onset, CeA-ON vs OFF) is the exact "fast forced transition" readout. Tick-level scalars exist today (`cea_fast_prime` amplitude with decay `config.py:2559-2561`; `override_signal` per tick). Cost: zero build beyond a recorder; flag stack `use_amygdala_analog` (+ default-on `use_cea_analog`), and optionally `use_broadcast_override`. Circularity: the CeA prior is an INPUT to the coordinator, not its label, so the channel is not label-derived. Residual risk: `use_salience_coordinator` must be ON for the forcing to be observable, which re-enters D6 for the replay channel -- exclude that channel from the cluster or run with MECH-261 gates ablated. This option dominates Option 1 on the claim's distinctive prediction and should be the recommendation, with Option 1's three producers recorded as *additional* read-only constituents.

### B5. Hygiene

- EXP-0781 is MECH-037 (confirmed); the doc's correction of the source chip stands.
- `agent.py:7588` correct at `2ce89ce`; `commit_readiness.py:324/366`, `closure_operator.py:191`, `freeze_gate.py:381`, `da9221c` all resolve.
- P5 carried from `8dff6ab6a0` is not re-measured; the doc says so. Acceptable but should be re-run before any queue, since the 2026-09-24 landing added producers on the same day.

---

## C. Summary table

| Doc | Verdict | Load-bearing defect | Cheapest fix |
|---|---|---|---|
| MECH-157 | CONTESTED | D1: `alpha_eff` DV is entailed by the manipulation; D3: `1-alpha_eff` is previous-state weight, not hippocampal drive | Re-state DV as mode-keyed SD-008 event-selectivity margin + orthogonality control; word the narrowing as "hippocampal drive not operationalised"; add Option E (world-side E1-anchor blend) to the table; fix D2 (absolute per-mode alpha, pin 0.9) |
| MECH-039 | CONTESTED | D5: none of the three constituents forces a transition; MECH-449 veto is overridden in the all-unsafe case (`e3_selector.py:2437-2446`); D7: Option 1 inherits the whole un-smoked flag stack | Add Option 5 (CeA fast-prime / SD-037 override as veto, the only producers wired into the coordinator); mark Option 1's veto-exception cell "weakly" until a forcing constituent is included; exclude label-derived channels from the cluster (D6) |
