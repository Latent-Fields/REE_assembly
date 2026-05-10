# MECH-318 Absorption Check

**Date:** 2026-05-10
**Status:** complete
**Verdict:** **(B) Partially absorbed — empirical retirement-vs-promotion verdict deferred to V3-EXQ-543c successor on multi-rule-context substrate.**
**Authoring context:** GAP-I row of `arc_062_rule_apprehension_plan.md`. Provisional-registration flag on MECH-318 (`registration_provisional_pending_meta_rl_absorption_check`) commissioned this check. Sibling absorption checks for MECH-316 / MECH-317 are out of scope for this pass.

---

## Question

Does the existing `ree-v3` substrate already implement meta-RL recurrent rule-state representation (Wang et al. 2018; Duan et al. 2016 RL^2)? Or does MECH-318 require a new substrate?

The provisional registration anticipates two empirical outcomes:

> "If V3-EXQ-543c (or a follow-on) demonstrates that the existing z_self / z_world latent recurrent state already supports the rule-state abstraction MECH-318 names, this claim should be retired (its function is absorbed into the existing latent stack). If V3-EXQ-543c shows that the latent stack is insufficient and a dedicated substrate is needed, MECH-318 promotes to active." — `claims.yaml` MECH-318 evidence_quality_note

This memo is the **architectural absorption check** that determines what an empirical follow-on test even looks like. It identifies which existing substrates partially serve the function and where the remaining gap is.

---

## Wang 2018 / Duan 2016 specification

The five load-bearing properties of meta-RL recurrent task-state representation:

| # | Property | What the literature requires |
|---|---|---|
| W1 | Recurrent network topology | LSTM (or GRU) hidden state evolves across time within a sequence. |
| W2 | Trained across many task instances | Many-task training distribution; weights shaped by gradient descent over the task family, not by hand. |
| W3 | Hidden state encodes task identity / rule-context | The recurrent state, by the end of a task instance, has converged to a representation that distinguishes the current task from sibling tasks in the training family. Not just immediate sensory state. |
| W4 | Within-episode policy adaptation downstream of the recurrent state | The recurrent state biases action selection so the policy adapts to the inferred rule without weight updates inside the episode. |
| W5 | Cross-episode hidden-state continuity (RL^2-specific) | Hidden state is carried forward across episodes within a task instance, so the agent accumulates evidence about the rule across multiple episodes. (Wang 2018's "outer-loop" and Duan 2016's defining design.) |

W3 + W5 are the load-bearing functional properties. W1 and W2 are *necessary mechanism*; W4 is the *coupling-to-policy* property. The biology anchor for the same role is OFC cognitive-map encoding of task state (Wilson, Takahashi, Schoenbaum & Niv 2014; Schuck et al. 2016) -- a discrete-symbolic alternative to the continuous-recurrent meta-RL framing. The architectural choice between continuous-recurrent and discrete-symbolic instantiation is genuinely open at the literature level; per the ARC-064 lit-pull synthesis (`evidence/literature/targeted_review_arc_064_bottom_up_rule_discovery/synthesis.md` line 135) "Whether MECH-318 needs a NEW substrate or can be implemented as a structured readout of existing latent-stack representations is a substrate-design call, not literature-decidable."

---

## Candidate 1 — E1 LSTM (`ree-v3/ree_core/predictors/e1_deep.py`)

`E1DeepPredictor.transition_rnn` is an `nn.LSTM` over `[z_self, z_world]` input. `ContextMemory` adds a slot-attention buffer.

| Property | Verdict | Evidence |
|---|---|---|
| W1 recurrent topology | **YES** | `nn.LSTM(input_size=total_dim, hidden_size=hidden_dim, num_layers=num_layers)` at `e1_deep.py:123-129`. |
| W2 trained across tasks | **NO** | Trained on sensory prediction error within whatever single task is running; no multi-task training distribution exists in V3 (SD-054 single-context). |
| W3 hidden state encodes task identity | **NO** | E1's hidden state encodes an unrolled prediction of `[z_self, z_world]` over `prediction_horizon=20`. Its loss is reconstruction of next-step latent, not rule-context discrimination. There is no objective shaping it toward a task-id representation. |
| W4 biases action selection | **INDIRECT** | E1 produces an associative `prior` (`generate_prior`) consumed by `HippocampalModule` for trajectory proposal conditioning, and `extract_cue_context` projects through `cue_terrain_proj` / `cue_action_proj` into E2/E3 -- but the path is sensory-cue-driven, not rule-state-driven. |
| W5 cross-episode hidden-state continuity | **NO** | `reset_hidden_state()` is called every episode (`e1_deep.py:220-222`). E1 is *deliberately* episode-bounded. This is the load-bearing failure: the central RL^2 property is absent. |

**Subtotal:** topology yes; functional role no. E1 is a slow-world-model, not a rule-state encoder. Repurposing the LSTM for MECH-318 would require giving up the per-episode reset (architectural conflict with the existing world-prediction objective) AND adding a multi-task training signal AND adding a cross-episode hidden-state carry mechanism. This is not absorption -- it would be a parallel substrate that happens to share the LSTM topology pattern.

---

## Candidate 2 — SD-033a LateralPFCAnalog `rule_state` buffer (`ree-v3/ree_core/pfc/lateral_pfc_analog.py`)

`LateralPFCAnalog` holds a `rule_state` buffer with gate-modulated EMA update; `MECH-261` write-gate registry conditions the update on operating mode; `MECH-262` registered as the rule-selective-persistence claim this substrate instantiates.

| Property | Verdict | Evidence |
|---|---|---|
| W1 recurrent topology | **PARTIAL** | "Recurrence" is a gate-modulated EMA, not an LSTM/GRU. `rule_state <- (1 - eta*gate) * rule_state + eta*gate * source` at `lateral_pfc_analog.py:236`. Update sources are `delta_proj(z_delta)` and `world_proj(z_world)`. The DESIGN ALTERNATIVES block (`lateral_pfc_analog.py:24-72`) explicitly documents this as Choice A3 with a queued lit-pull on whether biology is recurrent-spiking-persistence (Mansouri 2020) or synaptic-hold (STP) -- the EMA is a known approximation. |
| W2 trained across tasks | **NO** | Bias head is currently frozen-random with last-Linear weights and bias zeroed at init (`lateral_pfc_analog.py:177-180`); phased-training protocol explicitly *deferred* (Choice A2). The `delta_proj` / `world_proj` projections are also frozen-random. No actual rule-policy mapping is learned in V3 today. |
| W3 hidden state encodes task identity | **PARTIAL (substrate-ready, function-empty)** | Conceptually `rule_state` IS the task-state encoding the substrate names. But because the projections are frozen-random, what `rule_state` actually contains is a random projection of `z_delta` + pooled `z_world` -- nothing rule-shaped has been trained into it. The mode-gating works (gate-near-0 distractor resistance) so the *persistence* signature is there; the *content-is-rule-state* signature is not. |
| W4 biases action selection | **YES, structurally** | `compute_bias()` returns per-candidate score_bias clamped to [-bias_scale, +bias_scale]; composed additively into `dacc_score_bias` before E3.select(). The downstream coupling exists. Initial output is exactly zero by design (zeroed last Linear) so behaviour is bit-identical to OFF until training pressure is applied. |
| W5 cross-episode hidden-state continuity | **NO** | `reset()` zeros `rule_state` on episode boundary via `REEAgent.reset()`. The substrate docstring explicitly says "Cross-episode carry-over is NOT implemented (V3 simplification; V4 extension if required)" (`agent.py:select_action` block; mirrored in `claims.yaml` SD-033a entry). |

**Subtotal:** SD-033a is the closest match to a "rule-state representation that biases action selection" function. It covers W4 (coupling) and partially W1 (recurrence-as-EMA) and W3 (substrate-ready). It misses W2 entirely (frozen head), W5 entirely (per-episode reset), and the W3 content function is empty until phased training lands.

ARC-062 Phase 1 (`gated_policy.py`, landed 2026-05-09 per V3-EXQ-542 5/5 PASS) is materially relevant here: it provides a multi-stream `(z_world, z_self, z_harm_a)` context discriminator -> sigmoid w in [0,1] -> two-head softmax bias -> `dacc_score_bias`. The discriminator IS a per-tick mini-rule-context classifier on the same multi-stream input Wang 2018 / Miller & Cohen 2001 names. The critical structural difference: ARC-062 is *per-tick stateless* (no recurrence), which by construction excludes W1 + W3 + W5. But it covers W4 with an actual training signal (the discriminator + heads will be trained in Phase 2 V3-EXQ-543b on the SD-054 reef-vs-forage falsifier).

The combined SD-033a + ARC-062 + ARC-062-Phase-3 picture is closer to absorption than SD-033a alone:
- ARC-062 discriminator: covers W3 (encodes rule-context discrimination from multi-stream input) on a per-tick basis, with training pressure.
- SD-033a `rule_state`: covers W1 / W3 (substrate-ready buffer) + W4 (downstream bias coupling).
- The closure between the two arms is the explicit GAP-C work in `arc_062_rule_apprehension_plan.md`: "Wire discriminator output into LateralPFCAnalog.update() source vector." Phase 3 wires the ARC-062 discriminator INTO the SD-033a update path -- and that wiring is precisely the move that gives SD-033a's `rule_state` a content-is-rule-state W3 function.

W5 (cross-episode continuity) remains uncovered by the combined picture. Both substrates reset on episode boundary.

---

## Candidate 3 — MECH-269 anchor sets + per-region V_s (`ree-v3/ree_core/hippocampal/anchor_set.py`)

`AnchorSet` keys discrete region records by `(scale, segment_id, stream_mixture)` with dual-trace preservation; `MECH-288` event segmenter emits boundary events; `MECH-284` staleness accumulator integrates region-level evidence over time. SD-039 anchor goal-snapshot payload preserves motivational state on each anchor.

| Property | Verdict | Evidence |
|---|---|---|
| W1 recurrent topology | **NO (different paradigm)** | Anchor sets are a discrete symbolic store, not a recurrent network. State evolution is via segment-id increment + EMA per-anchor V_s + staleness integration. Closer to Schuck 2016 / Wilson 2014 OFC discrete-state cognitive-map biology than to Wang 2018 LSTM-style recurrent meta-RL. |
| W2 trained | **NO** | Pure arithmetic; no learned parameters. By design (substrate-coherence claim type). |
| W3 encodes task identity | **PARTIAL (in the discrete-symbolic interpretation)** | `(scale, segment_id)` IS a discrete task-state label; the event segmenter produces boundaries on regime change (BOCPD on z_goal, PE-threshold on z_world / z_self). Under the Wilson 2014 / Schuck 2016 reading, this IS the OFC cognitive-map analog. Under the Wang 2018 reading, it is not -- the encoding is symbolic / discrete, not continuous-recurrent. |
| W4 biases action selection | **YES, indirectly** | Via MECH-269b VsRolloutGate (gates E1/E2 cortical rollouts on regional V_s) and MECH-292 / MECH-293 ranked ghost-goal probes (anchors bias trajectory proposal); also via SD-039 payload feeding the bank ranker. Path is observation-routing-driven, not rule-policy-driven. |
| W5 cross-episode hidden-state continuity | **NO** | `reset()` clears active and inactive anchors on episode boundary. |

**Subtotal:** MECH-269 covers Wilson/Schuck OFC discrete-state-label biology. Not a recurrent-meta-RL substrate. Architecturally adjacent rather than competing with SD-033a + ARC-062.

The architecturally interesting fact is that REE has both arms of the rule-state-encoding biology already substrate-landed: MECH-269 for the discrete OFC-cognitive-map arm; SD-033a + ARC-062 for the continuous lateral-PFC-recurrent-rule-bias arm. MECH-318's question collapses to *which arm carries the meta-RL-style function* -- an empirical question on multi-rule-context substrate that doesn't exist yet.

---

## Verdict (B) — Partially absorbed

The five Wang 2018 properties map across the existing substrate cluster as:

| Property | Absorbed by | Notes |
|---|---|---|
| W1 recurrent topology | E1 LSTM (topology only); SD-033a EMA (recurrence-as-EMA approximation) | E1 is dedicated to world-prediction; the recurrence is reused only at the topology level. SD-033a is the architectural recurrence-substitute commitment for the rule-state slot. |
| W2 trained across tasks | **NOT ABSORBED** | No multi-task training distribution exists in V3 (SD-054 is single-context). Closing this is a *training methodology + environment* gap, not a substrate gap. |
| W3 encodes task identity | ARC-062 discriminator (per-tick) + SD-033a `rule_state` (buffered, content-empty until Phase 3 wiring) | Phase 3 GAP-C wires the discriminator into the rule_state update path; that closure gives SD-033a's buffer a content-is-rule-state function. |
| W4 biases action selection | SD-033a `compute_bias()` -> dacc_score_bias additive composition; ARC-062 gated_policy heads -> dacc_score_bias additive composition | Both are wired; ARC-062 will train; SD-033a head training is deferred (Choice A2). |
| W5 cross-episode hidden-state continuity | **NOT ABSORBED** | All three candidate substrates reset per-episode. RL^2's defining property is absent. |

**Two real gaps remain after the absorption check:**

1. **W2 + the multi-rule-context substrate** -- no training distribution exists to shape any of the substrates into a genuine rule-state encoder. This is the SD-054 single-context blocker the claim entry already names. Multi-rule-context substrate (e.g. SD-054 extended with two reef configurations requiring different foraging strategies) is the prerequisite for *any* MECH-318 validation experiment, regardless of whether the verdict is retire-or-promote.

2. **W5 cross-episode continuity** -- not in any V3 substrate. Adding it to SD-033a (the most plausible host) would conflict with the existing `reset()` semantics that anchor the rest of the agent's per-episode state machine. This may be V4 work; the claim entry already notes "Cross-episode carry-over is NOT implemented (V3 simplification; V4 extension if required)" on SD-033a. Wang 2018-style RL^2 may simply be V4-scope; the V3 question reduces to W1+W3+W4 within-episode coverage.

**Within-V3-scope reduced question:** *given W2 requires a multi-rule-context substrate that doesn't exist, and W5 may be V4-scope, does the within-episode portion of MECH-318 (W1 + W3 + W4) absorb into the SD-033a + ARC-062 + ARC-062-Phase-3 cluster?*

The within-V3 answer is **substantially yes** -- once Phase 3 GAP-C wires the ARC-062 discriminator into the SD-033a `rule_state` update path, the combined substrate provides a recurrent (EMA) rule-state buffer whose content is shaped by a multi-stream context discriminator and that biases action selection downstream. That is an in-scope V3 instantiation of the within-episode part of Wang 2018. The cross-episode RL^2 part is V4-deferred along with ARC-063 strong-reading.

**Therefore:** verdict (B) Partially absorbed. SD-033a + ARC-062 (with Phase 3 wiring closure) is the substrate that bears MECH-318's claim weight in V3. No new V3 substrate is commissioned by this absorption check. The empirical retirement-vs-promotion verdict (claim status `candidate -> superseded` vs `candidate -> active`) is deferred until:

- ARC-062 Phase 2 (V3-EXQ-543b) lands a PASS verdict on the monomodal-collapse falsifier on SD-054.
- ARC-062 Phase 3 (GAP-C) wires the discriminator into SD-033a `rule_state`.
- A multi-rule-context substrate is built (SD-054 extension to >=2 reef configurations OR equivalent) so V3-EXQ-543c-successor can falsify the within-episode adaptation signature MECH-318 names.

If post-Phase-3 the SD-033a + ARC-062 cluster produces the within-episode rule-state-adaptation behavioural signature, MECH-318 retires as `superseded` with `superseded_by: SD-033a + ARC-062 (cluster)`. If the cluster fails to produce the signature on the multi-rule-context substrate, MECH-318 promotes to `candidate -> active` and motivates a dedicated substrate landing.

---

## Forward-link from this memo to the substrates that bear the claim weight

Until the V3-EXQ-543c-successor verdict lands, MECH-318's within-episode functional weight is borne by:

- **SD-033a LateralPFCAnalog `rule_state` buffer** -- `ree-v3/ree_core/pfc/lateral_pfc_analog.py`. Provides W1 (EMA recurrence) + W3 substrate-readiness + W4 downstream bias. Design doc: `REE_assembly/docs/architecture/sd_033a_lateral_pfc_analog.md`.
- **ARC-062 Phase 1 GatedPolicy + context discriminator** -- `ree-v3/ree_core/policy/gated_policy.py`. Provides W3 per-tick rule-context discrimination on multi-stream input + W4 downstream bias via score-aggregation gradient. V3-EXQ-542 5/5 PASS 2026-05-09. Plan-of-record GAP-A done.
- **ARC-062 Phase 3 GAP-C wiring** (currently `open`, blocked on Phase 2 GAP-B PASS via V3-EXQ-543b) -- closes the loop between the discriminator and the rule_state buffer; this is the wiring that gives SD-033a's buffer a content-is-rule-state W3 function and unlocks the within-episode portion of MECH-318. Plan-of-record: `arc_062_rule_apprehension_plan.md` Phase 3 section.

The W2 multi-task-training and W5 cross-episode-continuity gaps remain on MECH-318 specifically and are NOT absorbed; they are the legitimate residual scope of the claim if the empirical verdict turns out to require a dedicated substrate. These map to V4 / ARC-063 strong reading and to environment work (multi-rule-context substrate) respectively.

---

## What this memo does NOT do

- Does NOT retire MECH-318. Empirical verdict deferred to V3-EXQ-543c-successor on multi-rule-context substrate.
- Does NOT commission new V3 substrate work. The combined SD-033a + ARC-062 + Phase-3-wiring substrate is sufficient for the within-V3 portion of the claim.
- Does NOT close GAP-I in the plan-of-record. GAP-I status moves from `registered` to `absorption_check_done` (the architectural absorption check); the empirical retirement-vs-promotion gate moves to a new V3-EXQ-543c-successor row pending Phase 2 + Phase 3 closure.
- Does NOT extend to MECH-316 or MECH-317. Sibling absorption checks for the cross-episode regularity extraction substrate (Schapiro 2017 CLS) and behavioural pattern compression substrate (Smith & Graybiel option-critic) are separately scoped tasks; this memo flags them as still-open but does not open them.

---

## Cross-references

- Claim: `REE_assembly/docs/claims/claims.yaml` MECH-318.
- Lit-pull synthesis: `REE_assembly/evidence/literature/targeted_review_arc_064_bottom_up_rule_discovery/synthesis.md` (R2 verdict; Q-XXX-2 open question on absorption).
- Plan-of-record: `REE_assembly/evidence/planning/arc_062_rule_apprehension_plan.md` GAP-I row + this-session decision-log entry.
- Substrate that bears the W4 + partial-W3 weight: `REE_assembly/docs/architecture/sd_033a_lateral_pfc_analog.md`.
- Substrate that bears the W3 per-tick discrimination weight: ARC-062 Phase 1 -- gated_policy.py module + plan-of-record Phase 1 entry.
- Sibling unbuilt substrates: MECH-316 (`cross_episode_regularity_extraction`), MECH-317 (`behavioural_pattern_compression`), MECH-319 (`simulation_mode_rule_write_gating`). All separately scoped.
