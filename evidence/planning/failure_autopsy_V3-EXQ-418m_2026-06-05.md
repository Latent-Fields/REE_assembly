# Failure Autopsy -- V3-EXQ-418m (SD-016 Path 3 feedforward cue->slot tagger)

- **Generated (UTC):** 2026-06-05T18:00:39Z
- **Scope:** single
- **Status:** confirmed (user-reviewed at interactive gate)
- **Run:** `v3_exq_418m_sd016_cue_slot_tagger_20260605T165833Z_v3`
- **Queue id:** V3-EXQ-418m
- **Purpose:** diagnostic -- `claim_ids = []` (weights no claim)
- **Outcome:** FAIL
- **Routing (user-confirmed):** implement-substrate (action=amend SD-016) + queue-experiment (z_world cross-context separation probe). Hippocampal-indexed retrieval = design note + gated future branch.

---

## 1. Facts (no interpretation)

2-arm ablation, 3 seeds [42,43,44], both arms `sd016_enabled=True`, `writepath_mode="off"`,
`temperature_learnable=False`. Training schedule matched to V3-EXQ-418i (P0=20, P1=40,
STEPS=150, LAMBDA_TERRAIN=0.1, LAMBDA_CUE_ACTION=0.5, lr=1e-4). Only inter-arm difference is
the `sd016_cue_slot_tagger` flag. Selection entropy read uniformly from the active selection
mechanism in each arm (`_last_cue_slot_weights`).

| Criterion | Rule | Result | Seeds |
|---|---|---|---|
| **C1** (primary) | A1_ON sel_entropy_mean < 2.5 | **FAIL** | 0/3 |
| **C1b** | A1_ON sel_context_divergence > 0.1 | **FAIL** | 0/3 |
| **C2** (control) | A0_OFF sel_entropy_mean > 2.65 | **PASS** | 3/3 |

Uniform reference `ln(16) = 2.772588722239781`.

| Metric | A0_OFF | A1_ON |
|---|---|---|
| sel_entropy_mean (mean / min / max) | 2.77259 / 2.77259 / 2.77259 | **2.75357** / 2.73188 / 2.76575 |
| sel_context_divergence (mean / min) | 2.47e-05 / 2.07e-05 | **0.00213** / 0.00066 |
| action_bias_per_channel_std (mean) | 0.00327 | 0.00297 |
| action_bias_div (mean) | 0.01168 | **0.00987** |

**Which criterion failed:** the *discrimination* criteria (C1 saddle-break, C1b context-dependence).
The *negative control* (C2) passes perfectly. **"Negative control passes, every discrimination
criterion fails" is the substrate-ceiling fingerprint.**

Read precisely:
- **OFF reproduced the saddle exactly:** entropy == ln(16) to 6 d.p. -> the legacy q.k slot-selection
  is pinned at the uniform saddle, as 418i found. Ablation is clean.
- **ON moved entropy only 0.019 below ln(16)** (needed 0.27). A random-init MLP produces non-uniform
  *but fixed* logits, so the softmax isn't perfectly flat -> a hair off the *static* saddle.
- **ON context divergence stayed ~0.0021** (needed 0.1) -> the tagger's selection barely varies across
  contexts. This is the load-bearing number.
- `action_bias_div` did not improve (ON < OFF). Correctly non-gating: full propagation is the
  SD-055 / cue_action_proj concern, recorded as context only.

---

## 2. Decisive reconciliation against the parked SD-016 lineage

SD-016 was **parked 2026-04-28** in `substrate_queue.json`
(`implementation_status: parked_pending_env_entropy_precondition`). The parking diagnosis, from
**V3-EXQ-418f / 418g / 418h**, localized the bottleneck *one level upstream of the attention path*:

- **418f probe:** queries near-constant across inputs because **z_world itself is near-constant**:
  pairwise `cos(z_world) ~ 0.998` across the batch; `q_norm.std/mean = 1.2%`; slot 4 wins all 64 samples.
- **418g 4-arm:** even with *perfectly orthogonal* slots (slot_diversity 1.000) and *delta-peaky*
  attention (attn_entropy 0.000), `action_class_entropy` stayed at `1.105e-10` **identically across all
  four arms** -- because the cue-indexing query does not vary across contexts.
- Conclusion at parking: "the current CausalGridWorldV2 configs do not generate enough cross-context
  z_world entropy for any retrieval substrate to do work." Validation precondition set: cross-context
  `cos(z_world) < 0.95`. **V3-EXQ-418h tested it and FAILed** (env does not clear the gate).

**Path 3 changed the selection MECHANISM (q.k -> feedforward MLP) but not the selection INPUT (still
z_world).** 418m's two numbers are exactly what the parking diagnosis predicts:

- *Entropy moved a hair (cosmetic):* off the **static** saddle in the trivial "non-uniform fixed logits"
  sense -- not the meaningful "context-selective" sense.
- *Context divergence ~0 (load-bearing):* the tagger's input barely changes across contexts, so its
  output barely changes. The C1b instrument is what exposes this; C1 alone (entropy) would have been
  ambiguous.

**A selection mechanism over z_world -- q.k, MLP, VQ-VAE codebook, or hippocampal index -- cannot be
context-selective until z_world separates across contexts.** 418m re-confirms the parking; it does not
overturn it.

---

## 3. Core question: are we asking a frontal cue selector to do hippocampal event retrieval?

**Partly yes -- but 418m does not demonstrate it, and asserting it now would over-read the result.**
Two distinct issues are tangled, and 418m cannot discriminate them because the z_world-collapse
confound sits **upstream of both** the q.k path and the tagger path (both consume z_world):

| | Issue | Proven by 418m? |
|---|---|---|
| (1) | **Input impoverishment** -- z_world carries no cross-context variance (env + encoder). The proximate, *sufficient* cause of this FAIL. | **Yes** -- re-confirms the parked precondition. |
| (2) | **Wrong abstraction level** -- selecting among 16 undifferentiated slots via a frontal feedforward tagger, vs retrieving hippocampal event/state/outcome nodes with relational indexing + pattern completion. | **No** -- confound masks it; cannot tell "semantically arbitrary slots" from "arbitrary because the query is constant." |

**User-confirmed classification: ambiguous between input-impoverishment and wrong-abstraction-level,
with impoverishment dominant and sufficient.**

The biological refinement is recorded as load-bearing (Section 4) but does **not** drive a build now.

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | `claim_ids=[]`; SD-016 (vmPFC somatic-marker cue retrieval, Bechara IGT) unchallenged. The test could not let SD-016 express itself -- the upstream z_world-separation precondition was unmet. |
| Biological reference | **partial / mislevelled** | SD-016 maps to vmPFC/OFC loading affective/safety/residue/goal-pull content into navigable state. But relational/event **indexing** + pattern completion over state/action/outcome traces is **hippocampal** (MECH-044 hippocampal relational binding+comparison; ARC-006/ARC-007; MECH-267 mode-conditioned hippocampal proposals). Current impl collapses index + load into one frontal MLP. This is a *level-of-abstraction* divergence, NOT a formal-definition import error (so not the SD-003 failure mode). lit_status: partial (vmPFC grounding present in SD-016 functional_restatement; MECH-044 hippocampal-relational lit exists from the 2026-06-04 object-files pull, but no `targeted_review` linking hippocampal event-indexing to SD-016 cue retrieval). |
| Prerequisites / dependency | **missing (dominant)** | z_world cross-context separation precondition unmet; parked since 2026-04-28; 418h confirmed unmet. |
| Implementation completeness | **complete** | tagger wired; bit-identical OFF verified (OFF entropy == ln(16) exactly). Not a stub, not the locus. |
| Environment adequacy | **too sparse (dominant)** | CausalGridWorldV2 (size 8, 1-5 hazards, no SD-023 landmarks engaged) does not generate cross-context z_world variance. |
| Measurement adequacy | **adequate / improved** | C1b context-divergence is the correct new instrument -- it distinguishes "static off-saddle" from "context-selective." C1 (entropy) alone would have been misleading. |
| Integration adequacy | isolated (by design) | retrieval->action_bias gated on SD-055 / cue_action_proj; correctly excluded from the pass gate. Not the failure locus. |
| Scale / capacity | adequate | the feedforward tagger is not capacity-limited; the deficit is input variance, not model size. |

**Recommended `epistemic_category`: `substrate_ceiling`** (encoder/env too coarse to carry cross-context
z_world at the granularity SD-016 retrieval requires), with a flagged, *not-yet-discriminable* secondary
hypothesis (abstraction level / hippocampal indexing).

---

## 5. Is the entropy movement worth a sweep? No.

2.7726 -> 2.7536 is **cosmetic**. A temperature / learning-rate / duration sweep would sharpen *fixed*
logits -- pushing C1 entropy down while making **C1b worse** (sharper fixed selection = even less context
dependence). Because the autopsy can *explain* why a purely local tagger cannot become selective without a
varying input (its input, z_world, is near-constant -- 418f cosine 0.998), a Path-3 training-strength
sweep is **contraindicated**, not merely deferred (satisfies the rule: do not default to a tagger sweep
unless the autopsy can explain why a local tagger should become selective without higher-level targets --
here it explains the opposite).

---

## 6. What evidence would distinguish "undertrained Path 3" from "wrong abstraction level"

Clear the z_world confound **first**. Under demonstrated cross-context z_world separation
(`cos(z_world) < 0.95`, e.g. SD-023 landmarks ON):

- If the feedforward tagger **becomes context-selective** (C1b passes) -> it was input/training; the slot
  abstraction was adequate. Hippocampal route not needed.
- If selection **varies but is semantically arbitrary** (divergence > 0 but does not track
  safe-vs-dangerous) -> *that* is the wrong-abstraction signature, and the hippocampal event/outcome-grounded
  route is justified.

This is why the smallest next step is the z_world-separation probe, not more tagger work.

---

## 7. Routing (user-confirmed)

1. **implement-substrate (action = amend SD-016).** Append the 418m failure_record to the existing
   parked `SD-016` substrate_queue entry; reaffirm `parked_pending_env_entropy_precondition`; keep
   `priority: 5`, `ready: false`, `status` unchanged. Add a **hippocampal-indexing design note** to the
   entry's `implementation_note_update` (gated future branch -- see below).
2. **queue-experiment (smallest next experiment).** A z_world cross-context separation probe:
   SD-023 landmarks ON vs OFF, safe-vs-dangerous z_world batches, pairwise-cosine separation metric;
   gate = absolute cross-context `cos(z_world) < 0.95` in at least one env config. Diagnostic,
   `claim_ids=[]`. This is a refresh/scoping of the parked V3-EXQ-418h gate (which FAILed) to determine
   whether *any* existing env config (landmarks ON) clears the precondition before further SD-016 work.
   If it clears -> the discriminator in Section 6 becomes runnable; if not -> SD-016 retrieval work stays
   parked pending broader env-enrichment scope (a larger, V4-adjacent decision -- not taken here).

**Hippocampal-indexed cue/context retrieval = design note + gated future branch** (user-confirmed). Keep
SD-016 as the cue-facing interface; record the idea that its selectable units may need to correspond to
hippocampal event/state/outcome nodes (relational index + pattern completion) rather than undifferentiated
memory slots. Cross-ref MECH-044 / ARC-006 / ARC-007 / MECH-267. **Gate to revisit:**
(a) z_world cross-context separation demonstrated, AND (b) under separated z_world, slot-level selection
proven semantically arbitrary (Section 6 second branch). Do **not** build it now.

---

## 8. Claim impact

**None.** 418m weights no claim (`claim_ids=[]`). SD-016 stays `implemented` (design_decision); the
substrate_queue entry stays `parked_pending_env_entropy_precondition`. **No demotion, no confidence change.**
This is explicitly **not** a falsification of SD-016 (vmPFC cue-context retrieval is a real biological
mechanism; the failure is translation/input, not the claim) and **not** evidence against cue/action
architecture globally. `narrow_supports_flag = false` (no supports to narrow). `pending_retest_after_substrate
= true` (retest gated on z_world separation).

No `evidence_quality_note` change is *required* on any claim (claim_ids=[]). For the audit trail, governance
may optionally append to SD-016's note: *"V3-EXQ-418m (2026-06-05, diagnostic, claim_ids=[]): SD-016 Path 3
feedforward cue->slot tagger reproduced the ln(16) OFF saddle (C2 3/3) but did not break it ON (C1 0/3,
entropy 2.7536 vs 2.5; C1b context-divergence 0.0021 vs 0.1). Re-confirms the parked
env-entropy precondition: a new selection mechanism over the same near-constant z_world (418f cosine 0.998)
cannot be context-selective. Routing: amend SD-016 substrate_queue + queue z_world separation probe;
hippocampal-indexed retrieval logged as a gated design note. No status/confidence change."*

---

## 9. Containment -- what must NOT be built from this autopsy

- NOT a Path-3 training-strength / learning-rate / temperature / duration sweep (Section 5).
- NOT a stronger slot-selectivity aux loss or contrastive safe-vs-dangerous objective yet (same input confound).
- NOT a return to Path 2 VQ-VAE / codebook (also consumes z_world -> same failure).
- NOT a hippocampal-indexed retrieval substrate yet (premature; gated -- Section 7).
- NOT interoceptive need-gating; NOT orienting/surveying; NOT safe-gradient following; NOT activating
  CandidateRuleField as a fix.
- 418m is **not** behavioural evidence -- retrieval-selectivity substrate readiness only.
- Do NOT conflate SD-016 retrieval selectivity with V3-EXQ-640a cue-to-action **authority**.

**Distinction ladder preserved** (418m sits at rung 2 and fails it for an upstream-input reason):
cue fires -> **cue retrieves context selectively** -> cue pulls z_goal -> cue biases E2/E3 action
generation/evaluation -> behaviour changes.
