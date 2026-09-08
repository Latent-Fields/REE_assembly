# Receiver-conditioned translation and recurrent interface stability

**Date:** 2026-09-08  
**Status:** child thought / falsifiable interface hypothesis  
**Parent:** `2026-09-07_mutual_legibility_communication_subspaces.md`  
**Companion:** `2026-09-07_mutual_legibility_implementation_assays.md`  
**Trigger:** XKV (`Dual-Cache Latent Space Communication between Heterogeneous Language Models`, Liu et al., 2026) and the independent public `kvloom` implementation

## Why this deserves a separate note

The mutual-legibility thought initially framed translation largely as a map from a sender representation into a receiver-compatible form:

`sender state -> bridge -> receiver-readable state`

XKV suggests a more relational formulation. Its translator reads **both** the sharer's and receiver's key-value caches, constructs a compact joint memory, and writes a gated residual back into the receiver's native cache geometry. Translation is therefore not merely a function of the sender representation. It is conditioned by the receiver's current representational state and by the receiver position being updated.

A better abstraction is:

`translated content = T(sender state, receiver state, receiver position/context)`

This is potentially important for REE because the meaning of a useful interface may depend on what the consumer already knows, expects, is attending to, or is trying to predict.

The independent `kvloom` implementation adds a second observation that is especially relevant to recurrent cognitive systems: a translator that works well for a single handoff can become unstable when repeatedly applied to its own previously modified receiver state. In the released checkpoints, naïve repeated application rapidly degraded performance, while recomputing against the original clean receiver cache preserved the first-turn advantage.

That creates a separate property that the existing mutual-legibility framework did not make explicit enough:

> **An interface can be statically useful yet recurrently unstable.**

REE operates through repeated state updates, so this distinction may be load-bearing.

---

## 1. Receiver-conditioned translation

### 1.1 Why a fixed bridge may be insufficient

A fixed map `T(A)` assumes that the same sender state should always be rendered into the same receiver-facing message.

But a receiver may already contain some of the relevant information, may currently be operating in a different context or mode, or may require different aspects of the sender state at different moments. A useful translation may therefore need to depend on both systems:

`T(A, B)`

rather than only on `A`.

This is not equivalent to giving the bridge unrestricted cognitive authority. The important constraint is that receiver-conditioning should determine **what part of already-present sender information is exposed and how it is expressed**, rather than allowing the bridge to solve the task independently.

### 1.2 Relation to communication subspaces

The communication-subspace framing already suggests that only selected sender dimensions are visible to a consumer. Receiver-conditioned translation sharpens this:

> the relevant communication subspace itself may be conditional on the receiver's current state.

The sender may support several potential read surfaces. Which one should be active may depend on:

- receiver mode;
- current goal or task-loop context;
- uncertainty;
- action/candidate under evaluation;
- retrieved episodic context;
- temporal phase;
- current predicted state.

Thus mutual legibility may be **context-indexed** rather than represented by one globally fixed cross-system alignment.

### 1.3 REE interfaces where this could matter

Candidate examples include:

- `z_world -> E1`: E1 may need different world-state distinctions depending on the current predictive trajectory;
- `z_world -> E2`: fast action-conditioned prediction may require a different read surface from E1;
- `E1 <-> E2`: translation may depend on the candidate action/horizon being evaluated;
- hippocampal retrieval -> consumer: what is useful from an episode depends partly on the consumer's present query/state;
- ContextMemory -> downstream reader: retrieved content may need to be expressed relative to current context rather than injected as a fixed latent message;
- sleep/replay interfaces: offline communication may use a different receiver-conditioned geometry from waking operation.

None of these implications currently justify adding a receiver-conditioned bridge to REE. They justify a diagnostic comparison between fixed and receiver-conditioned interface models.

---

## 2. Recurrent interface stability

### 2.1 Single-step success is not enough

The `kvloom` implementation reports that its single-turn XKV translators reproduce the broad performance ordering of the original paper, but repeated naïve application onto an already modified receiver cache causes rapid collapse. Recomputing the residual against the original clean receiver cache avoids that deterioration.

This means a translator can satisfy:

`one-step utility > 0`

while failing:

`repeated closed-loop stability`.

For REE this is particularly important because most interfaces are traversed repeatedly over trajectories, episodes, or recurrent prediction loops.

### 2.2 Possible failure mechanism

A bridge trained on receiver states drawn from the native receiver distribution may output a modified receiver state that lies slightly off that distribution. If the next bridge application treats this modified state as ordinary input, the error can compound:

`B_0 -> T(A_0, B_0) = B_1'`

`B_1' -> T(A_1, B_1') = B_2'`

and so on.

Even a small per-step off-manifold displacement can accumulate until the receiver is operating in a state regime the bridge was never trained to handle.

A second possibility is semantic double-counting: information already injected during one step is not recognised as already present, so the bridge repeatedly amplifies the same evidence.

These mechanisms should be distinguished experimentally.

### 2.3 New interface property: recurrence stability

The mutual-legibility framework should therefore add another criterion:

**recurrently stable** — repeated use of the interface preserves receiver state validity, information calibration, and functional behaviour over the timescale on which the actual system will use it.

The full ladder becomes:

`encoded -> decodable -> natively accessible -> bridgeable -> pairing-specific -> causally used -> behaviourally useful -> recurrently stable`

For dynamical systems, recurrence stability may need to be assessed before behavioural usefulness is considered architecturally meaningful.

---

## 3. Clean-base versus cumulative translation

The `kvloom` result suggests a useful experimental distinction.

### Cumulative translation

Each new translation operates on the receiver state produced by the previous translation.

Advantages:

- fully recurrent;
- allows previous translated content to shape future interface behaviour.

Risks:

- compounding off-manifold drift;
- duplicated evidence;
- escalating gain;
- self-generated interface artefacts becoming new input evidence.

### Clean-base translation

Each translation is computed relative to an unmodified or separately maintained native receiver state, with the translated residual treated as a temporary overlay.

Advantages:

- prevents recursive contamination;
- preserves a native receiver reference frame;
- makes causal attribution cleaner.

Risks:

- may prevent genuinely useful integration of prior transmitted information;
- requires an explicit distinction between native state and interface-conditioned overlay;
- could become architecturally artificial if retained permanently.

For REE, this resembles the broader distinction between **state** and **modulatory/contextual overlay**. It may be safer to test translated information first as an overlay or gated read surface rather than as an irreversible rewrite of the receiver's core latent state.

---

## 4. A falsifiable REE assay

A receiver-conditioning / recurrence assay should keep both endpoint systems frozen and compare, at matched capacity where possible:

1. fixed sender-only bridge `T(A)`;
2. receiver-conditioned bridge `T(A, B)`;
3. receiver-conditioned bridge with receiver-state permutation;
4. cumulative repeated application;
5. clean-base / temporary-overlay application;
6. zero and moment-matched random controls;
7. correct-vs-mismatched sender-state controls.

Measure:

- one-step consumer performance;
- multi-step performance curve;
- receiver-manifold distance/drift;
- task-information calibration;
- bridge output norm/gain over time;
- whether previously transmitted content is re-injected redundantly;
- dynamic compatibility with native receiver transitions;
- correct-pair specificity.

### Key interpretations

- `T(A,B) > T(A)` on held-out data, with receiver-permutation destroying the gain: evidence that receiver conditioning is genuinely useful;
- `T(A,B) > T(A)` but receiver permutation has little effect: additional capacity rather than meaningful conditioning may explain the result;
- one-step rescue with cumulative collapse but clean-base stability: recurrent interface instability;
- cumulative stability with correct-pair specificity: stronger evidence that a recurrent bridge is functionally coherent;
- both fixed and conditioned bridges fail while richer source information succeeds: upstream representation deficiency remains more likely.

---

## 5. Relationship to E1/E2 and sleep

This thought may matter particularly for E1/E2 because both are recurrent predictive systems.

A bridge that appears successful under isolated snapshots could still corrupt rollout trajectories if repeatedly applied. Therefore any proposed E1/E2 interface repair should be tested over the same horizons used to judge predictive competence.

It also sharpens the sleep hypothesis. Offline interface recalibration should not merely make states more mutually legible at one instant. It should improve or preserve **closed-loop stability** when waking dynamics resume.

A sleep-induced interface change that improves a static probe but destabilises the next waking trajectory would be a failure, not consolidation.

This suggests a future sleep metric:

> change in multi-step interface stability and correct-pair-specific communication after offline consolidation.

Again, this is a REE hypothesis, not an established biological claim.

---

## 6. Architectural caution

Receiver-conditioned translation is powerful enough to become dangerous as an explanation.

A high-capacity `T(A,B)` can in principle compute an arbitrary joint function of sender and receiver and thereby become a new hidden cognitive module. The evidence burden should therefore be stricter than for a simple linear bridge.

Any later architectural consideration should require:

- frozen endpoints during diagnosis;
- explicit parameter/capacity reporting;
- sender-only matched-capacity baseline;
- receiver-state permutation control;
- correct/mismatched sender control;
- off-manifold and recurrence-stability checks;
- held-out environments/tasks;
- demonstration that the bridge exposes/aligns existing content rather than learning the task independently.

The default interpretation should remain diagnostic until these tests are passed.

---

## 7. Evidence-status update

XKV itself strengthens the heterogeneous-bridge evidence because it operates across frozen models that may differ in family, depth, key-value geometry and tokenizer.

The public `kvloom` implementation is particularly valuable because it is independent of the original authors and reproduces the broad ordering across a substantial grid of released translators. However, the current checkpoints are exploratory: single seed, limited validation examples, short training runs, and no confidence intervals. This upgrades the evidence from author-only demonstration toward **early independent replication**, not settled replication.

The repeated-application collapse appears in the independent implementation rather than the original XKV paper and should therefore be tracked separately as an emerging finding requiring replication.

---

## Working principle

> **Mutual legibility may be relational rather than fixed: what a sender should expose can depend on the receiver's current state. But an interface that is useful once is not necessarily safe to use repeatedly. In a recurrent cognitive system, translation must be both content-specific and dynamically self-consistent over time.**

This extends the parent mutual-legibility thought without changing its central claim. It adds two testable dimensions that should be incorporated into future interface assays: **receiver conditioning** and **recurrent stability**.
