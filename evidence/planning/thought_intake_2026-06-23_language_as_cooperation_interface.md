# Thought Intake — Language as a cooperation interface over nonverbal cognition

**Date of thought:** 2026-06-23
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-06-23_language_as_cooperation_interface.md`
**Session:** `confident-pare-9273f1` (orphaned-thought intake pass, 2026-07-21)
**Source:** the user's own hypothesis about the function of language, reported directly. **No external literature.** One of three siblings split out of the superseded parent `2026-06-23_language_as_cooperation_interface_to_nonverbal_cognition.md` (do not intake the parent; the other two siblings are intaken in this same pass, and the split produced no fourth sibling).
**Status:** structured intake written; candidate claims **NOT yet registered** (concurrent sessions held the `docs/claims/claims.yaml` claim at intake time). Registration deferred.
**Promotes/demotes:** nothing.

## Authorship note

The **Core hypothesis** below is the user's, quoted verbatim, and it is a single dense sentence carrying three separable propositions. The handle/index formalism, the sufficient-statistic framing, the bidirectional adaptor diagram, and the update-policy pipeline are assistant formalisation developed in dialogue — claim-generative material, not canon.

## The hypothesis (verbatim)

> This has fed my hypothesis for how language is in my mind primarily a descriptor of internal processes for reducing cognitive burden of cooperation which happens to correspond well to the external world as internal processes are often modelling the world.

Three propositions are braided here and are separated below: language **describes internal processes**; its function is **reducing the cognitive burden of cooperation**; and its correspondence to the world is **inherited via the world model** rather than direct.

## Overlap handled first — do not duplicate the 2026-07-14 intake

The 2026-07-14 rule-apprehension intake (`thought_intake_2026-07-14_rule_apprehension_organisational_principle.md`) already carries **candidate claim 3: language as interface, not substrate** — including the LLM counterexample (*reasoning-like behaviour from language alone does not establish language as the native substrate*) and its testable compensation leg (*a system with a weakened non-linguistic reasoning stage should show greater reliance on linguistic scaffolding*). It also carries the MIT logic/language dissociation as its external anchor.

**That claim is owned there. This intake does not re-propose it.** The interface-not-substrate proposition is common ground between the two thoughts; register it **once**, at the 2026-07-14 intake, and cross-reference from here. What this thought adds beyond it is the *function* (cooperation cost), the *reference mechanism* (inherited via the world model), and the *input policy* (propose, don't install) — all three of which the 2026-07-14 intake does not touch.

**Correction to that intake, recorded here:** its Routing note says *"there is an existing unprocessed thought on private speech and externalised DMN that should be pulled in the same pass."* That is stale. `docs/thoughts/2026-06-08_play_private_speech_externalised_dmn.md` is **`Status: processed`**, reaped into ARC-090, MECH-380-384 and Q-068 on 2026-06-09, with a home doc at `docs/architecture/externalised_dmn_play_private_speech.md`. The private-speech territory is registered, not open.

## Already owned — cross-reference, do NOT re-assert

This is one of the most heavily pre-claimed areas in the registry. Nearly every section of the raw thought has an owner:

| Element in the thought | Existing claim(s) |
|---|---|
| Language emerges as functional self-representation, not a bolt-on | **INV-003** |
| Language is a symbolic mediation and **coordination** layer | **ARC-009** |
| Language is a high-bandwidth **externalisation of pre-existing functional states**; the bootstrap requires functional states as referents | **ARC-048** |
| Language cannot override embodied harm sensing | **INV-007**; language-input instance **ARC-104**; inference-level instance **ARC-103** |
| Bootstrap enabling-condition contract (what must pre-exist) | **ARC-099** |
| Language bootstraps from a grounded social ecology, not from grammar | **ARC-101** |
| Grammar/LLMs are **mined** for candidate primitives, not imported | **ARC-100** |
| **Language can feed back into cognition — instantiating or corrupting internal structures** | **MECH-424** (explicitly bidirectional: good language repairs, poor language degrades) |
| Incoming affect from language must enter as a distribution, not a point belief | **INV-085** |
| A LanguageAffectAdaptor parsing affect from language into the shared world model | **MECH-373**; **MECH-418** (one evidence source among several) |
| Private speech; internalisation ladder; distancing operator; labels as top-down control | **ARC-090**, **MECH-380**, **MECH-381**, **MECH-382**, **MECH-383**, **Q-068** — *the whole "internalisation and private speech" section of the raw thought* |
| Language acquisition tracks play-mode maturation | **MECH-308** |
| Predicate-argument-event bridge; frame inventory; aspect as event-arc map; compositional generalisation | **MECH-415**, **MECH-416**, **MECH-417**, **MECH-422**, **MECH-419** |
| Two abstraction levels not to be conflated (substrate vs symbolic) | **ARC-102** |
| Signal legibility as prerequisite for coordination; signals as causal externalisations | **MECH-192**, **MECH-191**, **INV-057** |
| Minimal signalling channel requirements; trust and deception | **MECH-014**, **MECH-015**, **MECH-010**-**013** |
| Explanation may be reconstruction, not causal transcript | **MECH-094**, **MECH-256**; and the introspection sibling intake's candidate 3 |
| Claims index as a typed graph over distributed evidential support | **SD-062** |
| Causal attribution gap: language describes causation without a causal-signature mechanism | **EXT-005** |

**Bluntly: the raw thought's "internalisation and private speech" section, its "language can feed back into cognition" section, and its "candidate architectural formulation" are all already registered.** Do not re-register any of them.

## Genuinely new — three things

### N1. Cooperation-cost minimisation as the *function*, with a sufficient-statistic formulation

ARC-009 says language *is* a coordination layer. ARC-101 says it *bootstraps from* a social ecology. Neither says **what it is for** in a way that predicts anything.

The thought's formulation does: the function is minimising the cost of inferring another agent's internal state, and the message should approximate a **task-relevant sufficient statistic** for the receiver — *"transmission of task-relevant sufficient statistics rather than complete mind-state replication."*

That is sharper than a coordination layer because it predicts **what gets said**, not merely that saying happens: the features selected for transmission should be those that most reduce the *receiver's* uncertainty about the sender's state, which is a different and testable objective from sender-side salience. Nothing in the registry states a message-selection objective at all.

### N2. Worldly reference is inherited via the world model, not direct — and one mechanism should cover non-present referents

The thought's most distinctive proposition, and it is genuinely absent:

```
world -> internal dynamical model -> language describing/indexing model states
```

Language corresponds to the world **because the internal processes it describes are themselves modelling the world**. ARC-048 says language externalises functional states; it does not say this is *why* reference works, and it does not draw the corollary.

The corollary is the falsifiable part: if reference is mediated by the model rather than by the world, then referring to **imagined, counterfactual, fictional, abstract or impossible** states requires **no separate mechanism** — those are simply model states that are stable or reconstructable. A registry that needed a distinct "imagination-reference" pathway would falsify the claim. This makes an otherwise philosophical proposition into an architectural prediction with a clear negative signature.

### N3. Incoming language proposes candidate states; it never installs beliefs

Partially covered and importantly incomplete. **INV-085** requires affect recovered from language to enter as a distribution. **ARC-104** forbids linguistic input overriding the harm/ethics stream. Both are *content-specific* guards.

The general **update policy** — utterance -> candidate internal states -> evaluation against context, source reliability, causal compatibility, existing world-model structure, memory, uncertainty, current goals, and the speaker model -> possible update — is not registered for arbitrary content. Given MECH-424 explicitly allows language to *instantiate* structures not acquired sensorimotorically, the absence of a general propose-and-evaluate gate is a real hole with a safety consequence: MECH-424's corruption branch is exactly what an install-on-assert policy would maximise.

### Also new, at discipline level

**Claims-as-handles.** The claim text is a compact linguistic handle into distributed evidence, dependencies, conflicts and experiments — the same principle one level up. SD-062 registers the graph but not this reading. Keep it as a note, and label it an **analogy**: per the 2026-07-14 intake's standing guard, REE:Assembly parallels must never be used as evidence that REE operates the same way.

## Explicitly NOT proposed

- **Not** re-proposing "language is an interface, not the substrate" — owned by the 2026-07-14 intake's candidate 3. Cross-reference only.
- **Not** re-registering private speech, the internalisation ladder, distancing, or labels-as-control (ARC-090, MECH-380-383, Q-068).
- **Not** re-registering language's feedback into cognition (MECH-424) or its harm-override prohibition (INV-007, ARC-103, ARC-104).
- **Not** proposing any V3 language scope expansion. There is no language stream in V3 and there should not be one for this.
- **Not** proposing language as an internal data format. The raw thought's "preserve a nonlinguistic core" section is a restatement of INV-003/ARC-048/ARC-102 and adds nothing registrable.
- **Not** claiming cooperation-cost reduction is language's *sole* function — the raw thought's own counterposition list rejects that, and the candidate below is scoped to a design objective, not an evolutionary account.

## Candidate claims (for registration at digestion)

1. **Message selection minimises the receiver's residual uncertainty: an utterance approximates a task-relevant sufficient statistic for the receiver, not a compression of the sender's salience.** *Candidate, architectural / `substrate_conditional` (V5/V6).* *Falsifier / PASS-FAIL shape:* two signalling policies in a multi-agent coordination task — features selected by **predicted uncertainty-reduction in the receiver** vs features selected by **sender-side salience**, under a matched channel budget. PASS = the receiver-objective arm achieves lower coordination cost by a margin scaled on the SD of the delta plus an absolute floor. FAIL = indistinguishable, which would say the receiver model is doing no work and language selection can be sender-local. *Non-degeneracy precondition:* the receiver's uncertainty must be **live** — non-zero cross-arm and cross-seed variance in the receiver's posterior entropy over the sender's relevant state. A task where the receiver already knows the sender's state (entropy floored at zero) or can never know it (entropy pinned at maximum) discriminates nothing between the policies, and the run self-routes `substrate_not_ready`. Additionally the channel budget must bind — an unconstrained channel makes selection moot. *Substrate status:* blocked in V3; nearest live substrate is **MECH-192** z_beta leakage, which is affective and non-propositional and would not test this. *Cross-ref:* ARC-009, ARC-101, ARC-099, MECH-014, MECH-192, INV-057, MECH-191, and the 2026-07-14 candidate 3.

2. **Worldly reference is inherited through the world model, and the same mechanism covers non-present referents.** *Candidate, architectural / `substrate_conditional`.* Language refers reliably to the world because it indexes internal states that model the world; therefore reference to imagined, counterfactual, fictional and abstract states requires no additional mechanism. *Falsifier / PASS-FAIL shape:* the negative signature is the test. A system that refers correctly to present referents should extend to non-present ones **without an added pathway**, given only that the corresponding model states are stable or reconstructable. FAIL = non-present reference requires a distinct mechanism, or degrades in a way not explained by the stability of the underlying model state. PASS additionally requires that reference quality **track model-state stability** rather than referent presence — that is the discriminating measurement. *Non-degeneracy precondition:* present-referent reference must first clear a floor with non-zero cross-seed variance; and the model states standing in for non-present referents must be independently shown to be reconstructable (a stability measure above floor). If either is at floor there is nothing to extend and the run self-routes `substrate_not_ready`. *Cross-ref:* ARC-048, INV-003, ARC-102, MECH-416, MECH-419, EXT-005.

3. **Language-input update policy: an utterance proposes candidate model states which are evaluated before any update; it never installs a belief.** *Candidate, architectural — generalises INV-085 from affect to arbitrary content and generalises ARC-104 from the harm stream to all content.* Evaluation criteria: context, source reliability, causal compatibility with existing world-model structure, memory, uncertainty, current goals, speaker model. *Falsifier / PASS-FAIL shape:* inject an assertion that contradicts available world evidence, under a source-reliability manipulation. PASS = the resulting belief tracks the **evidence** and the **source reliability** rather than the assertion — specifically, a low-reliability contradicting assertion leaves belief substantially unchanged while a high-reliability one shifts it, and neither overwrites contradicting direct evidence. FAIL = belief tracks assertion irrespective of reliability or contradicting evidence. *Non-degeneracy precondition:* the contradicting-evidence manipulation must **move belief in the no-language control** — non-zero cross-arm variance — otherwise the test cannot distinguish "language was correctly refused" from "nothing moves belief at all", and it self-routes `substrate_not_ready`. Likewise the source-reliability manipulation must be represented at all; if the speaker model is absent the reliability leg is untestable. *Cross-ref:* INV-085, ARC-104, ARC-103, INV-007, MECH-424 (its corruption branch is what this guards), MECH-373, MECH-418.

4. **(Discipline note, not a claim) Claims-as-handles.** The claim text is a handle into distributed support, the same principle one level up. Record in the digestion discipline notes, **explicitly labelled an analogy**, per the 2026-07-14 standing guard. Do not register; SD-062 owns the structure.

## Routing

- **Everything registrable here is substrate-blocked.** V3 has no language stream, no propositional input channel, and no speaker model. The honest routing is: **register scoped to V5/V6, design nothing, queue nothing.** Any EXQ id arising from this intake would be a mistake.
- **Candidate 3 is the one to register first** despite being blocked, because it is a **safety-shaped constraint on a mechanism that is already registered as capable of corruption** (MECH-424). A constraint registered before the capability is built is worth more than one registered after.
- **Candidate 1's dependency is the sharp one:** it needs a receiver model, a bound channel, and a coordination task with live receiver uncertainty. Note this is not merely "V5 work" — it is a specific substrate requirement that should be recorded against ARC-099's enabling-condition contract, which is where the bootstrap preconditions already live. `complex (probe-gated)` at the point it becomes buildable; not now.
- **Candidate 2 is `complex (probe-gated)`** and its probe is unusually cheap when the time comes: measure whether reference quality tracks model-state stability or referent presence. Record the probe design now so it is not re-derived.
- **"What makes an internal basin stable enough to acquire a linguistic handle?"** is `complex (probe-gated)` — and it is the *precondition* question for candidates 1 and 2 both. It is the right first spike whenever this line reopens.
- **"Does language retrieve a pre-existing attractor, create a new one, or both?"** is answered-in-principle by **MECH-424** (both). Do not re-open it as a question; it is a registered claim awaiting a substrate.
- **`/lit-pull`:** one pull, scoped to **cooperation-cost and informational-value accounts of language** (Gricean pragmatics, rational speech-act / listener-modelling, signalling under channel constraints) — this is the load-bearing leg for candidate 1 and a mature literature. **Merge it with the 2026-07-14 intake's pull** on language-as-scaffold rather than running two. Do **not** re-pull on private speech: that territory is registered (ARC-090/MECH-380-384) and the 2026-07-14 note pointing at it is stale, as corrected above.

## Next steps

1. Register candidates 1-3 as `substrate_conditional` (V5/V6), 3 first. **Deferred from this session** — `claims.yaml` was held by concurrent sessions at intake time.
2. Mark the raw thought `Status: processed` only once registration lands. It currently remains `unprocessed`, correctly.
3. Do **not** mark the superseded parent `2026-06-23_language_as_cooperation_interface_to_nonverbal_cognition.md` processed — it is `Status: superseded` and its three children carry its content.
4. Fix the stale private-speech note in `thought_intake_2026-07-14_rule_apprehension_organisational_principle.md` Routing, or rely on the correction recorded above.
5. Record candidate 1's substrate requirement against ARC-099's enabling-condition contract.
6. Read alongside its two split siblings, `thought_intake_2026-06-23_cross_system_resonance_and_inference_calibration.md` and `thought_intake_2026-06-23_introspection_as_architectural_evidence_for_ree.md`.
