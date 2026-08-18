# MECH-151 affordance-set-size instrumentation -- DESIGN BLOCKED at `/queue-experiment` Step 2.5c

**Status: AWAITING USER REVIEW. Nothing in this file has been written to claims.yaml, substrate_queue.json, experiment_queue.json, or any other registry.**

- **Written:** 2026-08-18T03:12:46Z
- **Session:** `metaworker-chip-20260816-queueexp-mech151-affordance-set-instrumentation-v2` (headless metaworker chip)
- **Chip:** `chip-20260816-queueexp-mech151-affordance-set-instrumentation-v2`
- **Outcome:** **No experiment was queued. No script was written.** Step 2.5c of `/queue-experiment` fired a hard stop, and independently the chip's proposed design was found to rest on two factual errors and one structural impossibility.

This file exists because the chip asked for an experiment and none was produced. Everything below is the reason, plus the corrected design a successor should use once the blocker clears.

---

## 1. The mandated stop: Step 2.5c substrate-path overlap, `severity: corrupting`

`/queue-experiment` Step 2.5c requires that no **open** `substrate_queue.json` entry with `severity: corrupting` overlaps the `ree_core` modules the proposed driver would exercise. One does, squarely:

| field | value |
|---|---|
| `sd_id` | `contextmemory-write-path-addressing-degeneracy` |
| `title` | ContextMemory.write() hard-argmin addressing has a deterministic single-slot fixed point under a low-variance query stream -- give the WRITE path the non-degenerate selection the READ path already has |
| `severity` | **corrupting** |
| `status` | `pending_implementation` (`status_phase: build_owed`, `ready: true`, `depends_on_unresolved: []`) |
| `priority` | 1 |
| `substrate_paths` | `ree_core/predictors/e1_deep.py` |
| `added_utc` | 2026-08-16T19:11:21Z, by `/governance` (`cranky-driscoll-126a36`) from `failure_autopsy_436f-603u-precondition-blocked-cluster_2026-08-16` |

The overlap is not incidental -- it is the *source* of the signal under test. MECH-151's pathway is
`z_world -> ContextMemory retrieval -> cue_context -> cue_action_proj -> action_bias`
(`e1_deep.py::extract_cue_context`). The defect's failure record measured **`n_occupied_slots = 1 of 16` in both arms on 3/5 seeds despite 2,837-4,903 `ContextMemory.write()` calls per arm**. With one occupied slot, `cue_context` is effectively constant no matter which slot the read path selects, because there is only one distinct slot content to retrieve.

Two consequences make this fatal rather than merely degrading:

1. **The cue-indexed half of MECH-151's input is inert.** `action_bias = cue_action_proj(cat([cue_context, z_world]))`. With `cue_context` pinned, *all* surviving variation in `action_bias` comes from the raw `z_world` half -- the EXQ-449a concatenation workaround, added precisely because `cue_context` had collapsed under uniform attention. A run would therefore report a live, varying, well-formed `action_bias` that is **not cue-indexed at all**, which is the exact claim MECH-151 makes.
2. **The corrupting config is the config this experiment would have to use.** The failure record is `v3_exq_436f_..._sd016_armed_retest`, run with the **full SD-016 production combination armed and confirmed engaged** (`sd016_arming_engaged`, pooled applied ctxdiv loss 25,796.28 against a 1e-9 floor) -- the same `cue_slot_tagger=True` / `gumbel` / `ctxdiv_weight=0.5` combination that MECH-151's current `live_status` rests on. The entry notes the read-path fix "changes write-path occupancy by ZERO seeds."

The entry's own `severity_rationale` describes the resulting artefact: *"Nothing errors, the readout is well-formed, and the resulting null looks like a genuine finding. That is the definition of `corrupting` -- evidence that LOOKS valid but is not -- and it has now produced exactly that artefact twice (436e, 436f)."*

**Build already chipped -- do not duplicate.** `chip-20260816-implsub-contextmemory-writepath-degeneracy` (status `open`, no `TASK_CLAIMS` holder, so registered but not yet in flight) routes this to `/implement-substrate`. Its own TLDR already anticipates this stop: *"Blocks SD-017/ARC-045/MECH-166 **and a MECH-151 experiment**."* No IGW ledger/assignment entry exists for it.

*Gate-hygiene note:* this entry's `status` is `pending_implementation`, which is **not** swallowed by Step 2.5c's `CLOSED` substring test, so the gate fired correctly here. That is worth stating because the sibling chip `chip-20260816-step25c-inert-corrupting-stamp` records that `implemented_pending_validation` entries *are* wrongly swallowed by that same test. This stop is not one of the inert cases.

---

## 2. Correction to the chip's premise: the V3-EXQ-640a "NULL" was the pathway being OFF, not a floor reading

The chip states that `failure_autopsy_V3-EXQ-640a_2026-06-06` found `mean_cue_action_bias_norm` NULL in all 6 cells "under DEFAULT settings" and read this as a dead-gradient defect, and then reasons that a correctly-functioning *relative* bias would also read at floor if the affordance set were single-option.

**No bias norm was ever measured in 640a.** Read directly from the manifest
`v3_exq_640a_scaffold_cue_authority_gain_sweep_20260606T013614Z_v3.json`, every cell carries:

```
sum_cue_action_bias_norm   = 0.0
n_cue_action_bias_present  = 0      <-- the load-bearing number
mean_cue_action_bias_norm  = None   ( = _safe_div(0.0, 0) )
```

`n_cue_action_bias_present` increments only when `agent._cue_action_bias is not None`. It is zero in **every cell**, so the tensor was `None` on every read. The mechanism: `agent.py` sets `_cue_action_bias` only under `if hasattr(self.e1, 'world_query_proj')`, and `world_query_proj` is created only when `sd016_enabled=True`. The 640a driver never sets `sd016_enabled` -- the string `sd016` appears nowhere in the driver and nowhere in the manifest.

The harness comment at the measurement site says so outright
(`experiments/scaffolded_sd054_onboarding.py`, `post_cue_diag` init):
> *"SD-016 cue_action_proj bias norm (agent._cue_action_bias); **usually 0 in the 638a config (SD-016 off)** -- captured for completeness so a future SD-016-on arm is comparable."*

So there are **three** candidate readings of an absent/floor bias norm, not two, and 640a is the first:

- **R0 -- pathway not enabled.** What 640a actually was. A measurement artefact; says nothing about MECH-151.
- **R1 -- enabled but ungrounded.** The separately-documented dead-gradient issue (`ree-v3/CLAUDE.md` SD-016: `cue_action_proj` receives exactly 0.0 gradient through the non-differentiable CEM argmax; EXQ-449 C1 PASS). Note this predicts `action_bias_divergence ~= 0`, i.e. the bias does not *vary* with context -- it does **not** predict a zero *norm*, since a randomly-initialised `Linear` emits a non-zero vector.
- **R2 -- enabled, alive, but competition-conditioned**, so at floor where the affordance set is single-option. The chip's hypothesis.

Any successor **must** carry R0 as an explicit readiness precondition (`n_cue_action_bias_present > 0`), which 640a lacked. The 640a autopsy itself attributed the NULL to R1; the manifest shows it was R0. Both readings agree the run says nothing about MECH-151, so no downstream conclusion changes -- but the distinction matters for what a successor has to control.

---

## 3. The structural finding: R2 is impossible by construction, and the chip's literal DV is a pre-determined identity

This is the most consequential item in this file, and it stands independently of the Step 2.5c blocker. Each link was verified in source.

### 3a. `action_bias` cannot be competition-conditioned

`action_bias` is computed **once per E1 tick, from `z_world` alone**, before any candidate exists:

```python
# e1_deep.py::extract_cue_context
action_bias = self.cue_action_proj(torch.cat([cue_context, z_world], dim=-1))
```

The candidate set enters nowhere. It is then cached (`agent._cue_action_bias`) and passed down into the CEM loop, where `E2.action_object()` adds **the same vector** to every candidate, at every horizon step:

```python
# e2_fast.py::action_object
o_t = self.action_object_head(torch.cat([z_world, action], dim=-1))
if action_bias is not None:
    o_t = o_t + action_bias
```

`||action_bias||` is therefore **arithmetically independent of affordance-set size**. Conditioning it on affordance-set size can only ever expose the indirect correlation that `z_world` itself carries with the agent's situation. The chip's three predicted outcomes collapse:

| chip's predicted outcome | verdict |
|---|---|
| Dead-gradient defect -> floor in BOTH bins | possible (this is R1/R0) |
| Working **relative** bias -> non-zero in multi-option, floor in single-option | **structurally impossible** |
| Working **additive** bias -> non-zero in BOTH | **structurally guaranteed** given any non-degenerate projection |

So the chip's literal design -- bias norm conditioned on affordance-set-size bin -- is a **DV-symmetry-invariant readout**: the manipulation is invisible to the DV by arithmetic, at every seed, on every substrate. This is exactly the class `/queue-experiment` documents from `failure_autopsy_V3-EXQ-604c_2026-07-20` (broadcast scalar vs. an argmax-derived DV). Run as written it would have produced a confident, well-formed, entirely pre-determined "supports the additive form" result.

**MECH-151's stated form is not merely nominally unconditional -- it is structurally incapable of being anything else.** The divergence from Pastor-Bernier & Cisek 2011 that the literature entry flags is therefore real, and it is a property of the design, not something an experiment needs to discover.

### 3b. The bias has zero within-pass ranking authority

Tracing where `o_t` goes:

- `o_t` is accumulated into `Trajectory.action_objects` (`e2_fast.py::rollout_with_world`).
- The world-state transition does **not** read `o_t`: `z_world = self.world_forward(z_world, action)` uses `(z_world, action)` directly.
- `HippocampalModule._score_trajectory` scores `trajectory.get_world_state_sequence()` (residue terrain, plus optional wanting / curiosity / mode terms), falling back to `states` (z_self). **It never reads `action_objects`.**
- `ree_core/predictors/e3_selector.py` contains **zero** references to `action_object`, `action_bias`, or `.trajectory`.
- The only other consumers of `Trajectory.action_objects` are pure storage copies: `record_exploration_trajectory`, `reverse_replay`, and the backward-credit-sweep buffer.

Therefore `action_bias` does not affect candidate scores or E3 selection within a scoring pass.

### 3c. Its entire behavioural authority is a translation of the proposal mean

The one live path is the CEM refit. In both branches the candidate weights are score-derived and hence bias-independent, while the bias is the same constant on every candidate:

- **legacy (default):** `ao_mean = mean_{i in elites}(ao_base_i + b) = ao_mean_base + b`
- **differentiable (`use_differentiable_cem=True`):** `ao_mean = Σ_i w_i (ao_base_i + b) = ao_mean_base + b`, since `w = softmax(-score/T)` sums to 1 and `score` does not read `ao`.

`ao_std` is **unchanged** in both -- standard deviation is translation-invariant. The shifted `ao_mean` seeds the next CEM iteration (`num_cem_iterations = 3` by default), whose samples are decoded by the linear `action_object_decoder` (so the actions shift by `W_dec · b`), rolled out, and *then* scored. That is a real but wholly indirect authority path.

**Summary:** `action_bias`'s complete causal contribution is a rigid translation of the proposal distribution's mean in action-object space, identical regardless of how many candidates exist or how diverse they are.

### 3d. A candidate answer to the open EXP-0155 diagnostic

`ree-v3/CLAUDE.md` (SD-016) records that EXQ-449's C2 arm successfully trained `cue_action_proj` (grad ~0.013, delta ~0.21) yet `action_bias_divergence` stayed at exactly 0.0, concluding *"something downstream of cue_action_proj zeroes the signal before it reaches E3.select"* -- and queues **EXP-0155** to instrument the forward path and find the blocker before any EXQ-418b successor is written.

Section 3b is a concrete candidate for that blocker: **the scoring and selection path never reads `action_objects` at all**, so there is no forward route from `o_t` to `E3.select`, and (equally) no gradient route back -- which is why SD-055's differentiable CEM restores a gradient to the *action sequence* (EXQ-568 `grad_max=372`) without producing behavioural divergence. This is offered as a hypothesis with its evidence, not a closure: EXP-0155 remains open and should adjudicate it.

---

## 4. Corrected design for the successor (do not queue until the blocker clears)

Preserved so the chip's intent is not lost. **Prerequisite:** `contextmemory-write-path-addressing-degeneracy` implemented and validated, i.e. `n_occupied_slots >= 2` on >= 3/5 seeds.

**Primary DV -- non-invariant, and the one that answers the question.** Not the bias norm, but the bias's *selection authority*: a paired ON/OFF ablation of `action_bias` at matched state (same seed, same `z_world`, same RNG reset), measuring whether the committed action / action-object changes. Condition that on affordance-set-size bin. This DV is genuinely non-invariant: whether a rigid translation of the proposal mean changes the eventual commitment does depend on how the candidate set is distributed, because `world_forward` and the residue terrain are non-linear.

**Operationalising affordance-set size.** Measure it, do not assume it -- at the current `z_world`, compute the **unbiased** `o_t(a) = E2.action_object(z_world, a)` for each primitive action `a` and report both a continuous spread (mean pairwise L2) and a pre-registered-tolerance distinct-cluster count. A corridor or wall-adjacent cell, where blocked moves produce near-identical world-effects, is the natural single-option regime; an open cell is the multi-option regime.

**Retain the bias norm as instrumentation, not as a gate.** Record `mean_cue_action_bias_norm` and `n_cue_action_bias_present` per affordance-set bin as the chip asked, but declare in the manifest that this readout is structurally invariant under the conditioning variable (section 3a) and therefore **diagnostic only** -- never a load-bearing criterion. Its real job is the R0 control that 640a lacked.

**Mandatory readiness preconditions.**
- `n_cue_action_bias_present > 0` (R0 -- the pathway is actually enabled).
- `n_occupied_slots >= 2` (the section-1 blocker is genuinely cleared for *this* run, not merely marked implemented).
- A non-degeneracy check that both affordance-set bins are populated above a pre-registered sample floor.
- Per `/queue-experiment`, the readiness statistic must be the *same* statistic the load-bearing criterion routes on -- an authority-gated criterion needs an authority-based readiness check on a positive control, not a bias-magnitude proxy.

**Devaluation sub-question (Gourley 2013).** The chip flags it as optional. It should stay out of this design: section 3c shows the bias is a fixed translation of the proposal mean with no outcome-model dependence anywhere in its path, so the devaluation test's answer is already largely determined by the architecture. It is better posed as a design question about MECH-151's form than as an experiment.

---

## 5. What a reader should do with this

1. **Route `contextmemory-write-path-addressing-degeneracy` to `/implement-substrate`** via the existing `chip-20260816-implsub-contextmemory-writepath-degeneracy`. It is `ready: true`, priority 1, no design doc owed, and blocks SD-017 / ARC-045 / MECH-166 in addition to this work.
2. **Consider whether MECH-151's `live_status` should be qualified.** It currently reads *"supports -- narrow context-conditioning mechanism confirmed on 2/3 seeds"* on the strength of V3-EXQ-922, under the same SD-016 production config that 436f later showed runs against a 1-of-16 slot bank. Section 3a additionally shows the claim's own stated form cannot be competition-conditioned. This is flagged for governance, **not** adjudicated here.
3. **Note section 3d against EXP-0155** as a candidate resolution to be tested, not as a closure.
4. Nothing here has been applied to any registry.
