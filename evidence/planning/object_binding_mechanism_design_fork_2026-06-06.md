# Object-Binding Mechanism — the design fork: coherence/synchrony vs competitive slot-attention

**Type:** design memo / thought-intake (planning — NOT a claim, NOT a substrate spec)
**Date:** 2026-06-06
**Parent thread:** [`object_representation_thread_2026-06-04.md`](object_representation_thread_2026-06-04.md) (ARC-080 umbrella + ARC-081/082/083 pillars)
**Trigger:** The 2026-06-06 object-files lit-pull delta surfaced **two distinct candidate binding mechanisms** in the literature record — coherence/synchrony (Fries 2015 CTC; Singer & Gray 1995; von der Malsburg 1999) and competitive slot-attention (Locatello 2020; Kipf SAVi 2022). User question: *"How will we decide between those two kinds? It feels like the brain does both and somehow gains an advantage in representational capacity."*

**Status:** SYNTHESIS + a falsifiable decision procedure for the next session that touches the bound-representation substrate. No claim registered, no substrate code, no experiment queued. V4-leaning / off the V3-closure (GAP-7) critical path — same parking as the rest of the object thread.

---

## 1. They are not competitors — they bind different things

The cleaner framing is a **division of labour**, not a fork. Three orthogonal jobs:

| Job | Mechanism | What it is | Strength | Weakness |
|---|---|---|---|---|
| **Addressing** | **Slots / indexes** (Locatello slot-attention; Pylyshyn FINSTs; SAVi) | A small set of persistent, exchangeable pointers — "object #3, whatever it currently is." Survives time + occlusion. Fixed capacity K. | Stable, readable/writable, compositional, factored | Rigid; says nothing about relations *between* slots; single-frame slot-attention has no persistence on its own |
| **Binding** | **Synchrony / coherence** (Fries CTC; Singer&Gray; von der Malsburg) | "Which features belong to the pointed-at object *right now*," and "which objects are relationally grouped this moment." Carried by relative timing; computed on the fly. | Flexible, relational, supports novel groupings; combinatorially cheap | Transient — cannot hold identity across a perceptual gap (you can't synchronize with an occluded, unperceived object) |
| **Capacity / ordering** | **Theta-gamma multiplexing** (Lisman & Jensen 2013; Lisman & Idiart 1995) | Several gamma cycles nest in one theta cycle; each carries a bound item; phase encodes order/relation. | Multiplies simultaneous-item capacity; encodes ordinal/relational structure | Bounded (~7+/-2 items); needs items to multiplex over (i.e. presupposes slots/binding) |

So: **slots answer *which object*; synchrony answers *which features cohere into it and how objects relate*; theta-gamma phase answers *how many and in what order*.** A pure-slot system is a filing cabinet with no dynamic regrouping; a pure-synchrony system binds beautifully but has no stable address to write to or read from. The user's "the brain does both" is this division stated mechanistically — and the capacity advantage is real and named: **effective capacity ~ (slots) x (phase bins)**, not just (slots). That is the formal version of "gains an advantage in representational capacity."

## 2. This reframes the V3-EXQ-641a null

641a (coherence-ablation non-reducibility, fair contrast-matched control) found a coherence term over `world_states`<->`states` **functionally redundant** with the integrated prediction error E. The autopsy read this as "the bound-representation prerequisite is absent."

In the §1 frame this becomes precise: **641a failed because there was nothing slot-like for coherence to bind.** Synchrony presupposes addressable things to be coherent *about*. REE built the synchrony/routing layer FIRST — the entire heartbeat control plane (MECH-089 theta-gamma packaging, MECH-090/093 beta gating + heartbeat frequency, MECH-091 phase-reset, MECH-094 hypothesis-tag write gate, MECH-270 ephaptic) — and never built the slots. A coherence read over streams that carry no token structure has nothing for phase to organize, so it is redundant with E by construction. **REE built the two layers in the wrong order.**

Corollary: REE already *owns the synchrony half* (the heartbeat) and the theta-gamma capacity primitive (MECH-089). The **missing** piece is the slot/addressing layer — exactly the parked `bound multi-stream representation` substrate (generalise `z_object`/`z_resource` from a type-tag store to a token-keyed object-file). The thread memo's "type vs token vs anchor" fork is the slot-design fork.

## 3. The decision procedure — you don't choose, you sequence and test

Because synchrony presupposes slots, the answer to "which one" is "build slots first, then measure whether synchrony adds non-reducible value over slots." Concretely:

1. **Build the slot layer** (token-keyed object-file; instance-level `z_object`). This is the parked `bound multi-stream representation` substrate (status `pending_implementation`). Design fork to resolve first: **type vs token vs anchor** as the unit (the thread memo §2.2 gap).
2. **Re-run the 641a non-reducibility test over slots.** Acceptance: does a coherence/phase term change *which* trajectory/binding is selected **beyond** what slot-identity + E already explain, under the same fair contrast-matched control?
   - **YES -> BOTH are needed.** Synchrony adds relational/temporal binding on top of slot addressing; register the coherence factor (the candidate Q `entities/selection.coherence_nonreducibility`, currently NOT registered).
   - **STILL redundant -> slots alone suffice at this scale;** synchrony is decorative for REE's task (at least in this environment). Close the coherence-nonreducibility intake as structural-analogy-no-mechanism.
3. **Capacity test for the multiplexing claim.** Build an environment that demands holding N > K objects, or relational binding *between* objects, and check whether the phase/heartbeat layer extends capacity past K slots (the Lisman-Jensen prediction). This is the direct empirical version of "both gives an advantage."

The pieces line up REE-shaped: **slots + a forward model that predicts them = SAVi** (Kipf 2022), and **REE's E2 is already that forward model**. The heartbeat is the routing/gating layer on top. So "both" is not exotic for REE — it is slots feeding E2, gated by the existing synchrony machinery. SAVi also supplies the persistence half (slots tracked across video frames) that vanilla slot-attention lacks — i.e. it is a candidate substrate for ARC-080 Pillar 1 (object permanence).

## 4. Honest caveats (do not over-commit)

- **Brain-does-both does not oblige a minimal mind to.** REE methodology: brain is an existence proof for the *class*, then test whether REE *needs* it. "Both" is a hypothesis with a clean falsification path (steps 2-3), not a foregone architecture.
- **Environment adequacy.** It is entirely possible slots alone suffice at gridworld scale and synchrony only earns its keep in richer, more relational environments — the same environment-adequacy worry 641a raised. The capacity test (step 3) must construct genuine binding pressure or it will under-detect the synchrony advantage.
- **Binding-by-synchrony is itself contested** (Shadlen & Movshon 1999 and successors: synchrony may accompany rather than constitute binding). So even a YES at step 2 should be read as "a coherence factor helps here," not "synchrony is THE binding code."
- **Two different bets, not one.** Coherence/synchrony and competitive slot-attention are distinct binding mechanisms; the literature record now holds both. The slot layer (step 1) is mechanism-agnostic about *how* features get assigned to a slot — competition (slot-attention) and coherence (synchrony) are two candidate assignment rules, and they could coexist (competition allocates the slot; coherence binds features into it and relates slots).

## 5. What stays off the V3 critical path

Everything here. No slot substrate, no coherence-factor registration, no SD-016/permanence work bundled into GAP-7. The L9 wanting!=liking retest (`scaffolded_sd054_onboarding` / V3-EXQ-603f) is untouched. The only V3-era-safe actions are this memo and the grounding lit-pull (Lisman&Jensen, SAVi, von der Malsburg — landed 2026-06-06 into `targeted_review_object_files_feature_binding`).

## Appendix — claim / file index

- Synchrony layer (BUILT): MECH-089 (theta-gamma nesting), MECH-090/093 (beta gate / heartbeat freq), MECH-091 (phase reset), MECH-094 (hypothesis-tag write gate), MECH-270 (ephaptic). `docs/architecture/control_plane_heartbeat.md`.
- Slot layer (MISSING): parked `bound multi-stream representation` substrate (`substrate_queue.json`, `pending_implementation`); generalise `z_object` (`ree-v3/ree_core/goal.py` IncentiveTokenBank, `latent/stack.py` ResourceEncoder). Candidate Q `entities/selection.coherence_nonreducibility` (NOT registered).
- Object umbrella: ARC-080 + ARC-081/082/083; `docs/architecture/arc_080_object_representation_primitive.md`.
- Diagnostic that triggered this: `failure_autopsy_V3-EXQ-641a_2026-06-06.{md,json}`.
- Literature: `targeted_review_object_files_feature_binding/` (Fries 2015, Singer&Gray 1995, Locatello 2020, Lisman&Jensen 2013, Kipf SAVi 2022, von der Malsburg 1999) + `targeted_review_object_permanence/`.
