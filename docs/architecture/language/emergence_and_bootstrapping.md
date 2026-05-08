---
nav_exclude: true
---

# Emergence And Bootstrapping

**Claim Type:** mechanism_hypothesis  
**Scope:** Language emergence and bootstrapping  
**Depends On:** ARC-009, ARC-010  
**Status:** candidate  
**Claim ID:** MECH-010
<a id="mech-010"></a>

---

Source: `docs/processed/legacy_tree/architecture/language/emergence_and_bootstrapping.md`

> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

# Emergence & Bootstrapping

REE predicts that language-like signalling emerges when:
- agents have private internal state (interoception/homeostasis),
- must model others under partial observability,
- benefit from coordination,
- plan over longer horizons,
- and operate under compute/attention limits.

Joint attention is the immediate precursor: once agents detect each other as `OTHER_SELFLIKE`, WORLD predictions improve
by conditioning on what the other is attending to. That creates **simulation overhead**, which pressures the system to
externalise predictive state.

Language therefore emerges as a **compression and coordination layer**, not a new reasoning engine.

### Bootstrapping sequence (human-analogous but implementation-agnostic)
1. Affective signalling (low-bandwidth, high-salience): distress, aversion, approach cues
2. Attentional biases: agent/face-like feature attention; gaze-following analogues
3. Proto-symbols: repeated signals tied to stable contexts ("danger", "stop", "help")
4. Symbolic compression: compositional messages that condition priors and plans
5. Normative layer: shared expectations transmitted socially (still constrained by embodied harm)

### Minimal requirement
REE does not require pre-defined grammar or symbols—only a channel for exporting internal summaries that can update others' priors.

Minimal nudges for bootstrapping:
- external symbol production (cheap, repeatable, perceivable outputs),
- attention coupling to those symbols,
- commitment tagging for some patterns,
- fast correction tokens ("no", "wait", "stop").

Dual-stream nudge (functional analog):
- a **dorsal sequence→motor channel** for fast sensorimotor mapping, paired with a **ventral meaning** channel for
  semantic grounding (distributed rather than a single tract; see `arcuate_fasciculus.md`).

---

## Basic Expression Catalog (the bootstrap primitives)

The "affective signalling" of step 1 above is not an undifferentiated cloud. In any social vertebrate
— and conspicuously in dogs, primates, and human infants — a small inventory of stereotyped basic
expressions does most of the bootstrapping work. Each entry in this inventory carries a specific
learning-signal role; together they form the substrate that proto-symbols (step 3) attach to.

| Expression | Channel content | Learning-signal role |
|---|---|---|
| **Play pose / play bow** | "what follows is play frame" | Bilateral signal that opens a `play_mode` episode (INV-059, ARC-049). Tags the next sequence as authorized-synthetic so partners can join without misreading aggression as real. Direct precursor to the brackets-as-frame logic of language. |
| **Head tilt toward speaker** | "active uncertainty / attempted decoding" | Externalises a high-precision attempt to parse an under-specified social signal. The tilt itself is informative to the speaker — it is a feedback channel that says *the message did not fully land*, which is the minimal ingredient for repair-pressure on the speaker. |
| **Laughter** | breath-expiration coupled to "expiring thoughts" | A temporal coupling between the release of a held cognitive frame (a prediction that just resolved with low harm) and a perceptible motor signal (vocalised expiration). Reads to the listener as *insight occurred and it was safe* — simultaneously a social-safety marker and a salience marker for the content that just resolved. The breath coupling is what makes it broadcast-cheap and contagious. |
| **Mutual gaze / gaze-following** | "joint attention frame" | The immediate precursor flagged in §1 above. Establishes that two agents share a referent, which is the precondition for any proto-symbol to acquire stable meaning. |
| **Distress vocalisation / whimper** | sustained negative valence broadcast | The minimal channel for SD-011 affective harm to escape the body. Works because partners can detect and respond before the harm is observable from outside. The "stop / help" correction tokens of the minimal-signalling channel descend from this. |
| **Approach cue (orient + reduce distance)** | "I am committing to social engagement" | A commitment marker (in the MECH-061 sense) that opens a turn-taking window. The closing of distance is itself a commitment — once it lands, withdrawal is informative. |
| **Vocal mimicry / matched cadence** | "I am modelling you and you can model me" | The earliest two-way prediction-coupling primitive. Reciprocal matching produces a shared timing structure that later carries phonological content. |
| **Pointing / referential gesture** | "this thing, in shared frame" | Decouples *referent* from *predicate*. The first move toward compositional structure: a single signal that indexes a slot rather than carrying full content. |

**The architectural point:** these are not cute behavioural details. Each one is a discrete *learning
signal carrier* with a specific job. The proto-symbol stage of step 3 above is not "agents start
emitting arbitrary sounds and one happens to stick"; it is "agents already have an inventory of
broadcast-cheap social channels, and proto-symbols accrete onto those channels as conditional
modifiers." Distress vocalisation acquires "danger-shaped" variants. Approach cue acquires "approach
*and*" qualifiers. Pointing acquires which-thing modulators. The basic expression is the
load-bearing primitive; the proto-symbol is the modifier.

This sharpens the bootstrap claim: language does not emerge from undifferentiated affective noise.
It emerges as a system of conditional modifiers attached to a small inventory of discrete,
behaviourally-stereotyped social channels.

---

## Language as a Specialised Game Type in Play Mode

Play mode (`play_mode.md`, INV-058 / MECH-194 / ARC-049) is the architectural substrate that
permits *real learning under synthetic stakes*. The play frame opens with a bilateral signal,
suspends real-world residue, and lets gradient flow through E3/E2/E1 as if the synthetic signals
were real. This is exactly the substrate language acquisition needs.

The hypothesis: **language is a specialised game type running inside `play_mode`**, where the
game-specific synthetic signals are *symbolic-content goals and conversational-violation harms*.

What this buys, mapped to the play_mode architecture:

| Play_mode element | Language-game instantiation |
|---|---|
| Bilateral frame-opening signal (INV-059) | The basic expression catalog above — play-pose, mutual gaze, approach cue, vocal mimicry. These open the language game just as they open any other play. |
| Synthetic z_goal (MECH-194) | The act of producing or comprehending an utterance is the goal; the homeostatic state is bracketed for the duration. |
| Synthetic z_harm | Conversational violations (mis-reference, prediction-failure on what the partner meant, repair-failure) generate harm signals that drive learning *inside the language game* without corresponding to real-world damage. The head-tilt-as-uncertainty signal is the listener's local harm-equivalent: "this did not parse." |
| Frame-closing signal | Conversational closings (drop in mutual gaze, turn-end prosody, "ok" / "right" tokens) close the language game just as physical play has its own closings. |
| Strategy / calibration dissociation (MECH-195) | What transfers out of language play: phonological competence, prediction-of-other-speaker structure, compositional habits. What stays inside the play frame: the specific synthetic-harm calibration of "this utterance was wrong" — which is why language learning generalises without language-game errors leaking into real-world harm budgets. |

**The architectural payoff:** if language is a specialised play game, REE does not need a separate
"language acquisition module" with its own learning rules. It needs (a) the basic expression
catalog wired into play-mode frame opening, (b) play-mode itself, and (c) a path by which
proto-symbols accrete onto basic expressions as conditional modifiers. The rest follows from
play-mode's existing capacity to convert synthetic stakes into real gradient updates.

This also predicts a developmental signature: language acquisition should track the maturation of
play-mode itself, not the maturation of any putative language-specific substrate. Loss-of-language
in adults under stress / fatigue / aphasia should track loss-of-play-mode-availability rather than
selective damage to a language module — except where the dorsal sequence→motor or ventral meaning
pathways are themselves lesioned (cf. `arcuate_fasciculus.md`).

---

## What this changes for MECH-010

The original MECH-010 was abstract — "affective signalling, attentional biases, proto-symbols,
symbolic compression, normative layer." The expansion does not change the five-step sequence but
specifies:

1. **Step 1 (affective signalling)** is enumerated by the basic expression catalog. Each entry is a
   testable bootstrap primitive with a specific learning-signal role.
2. **Step 3 (proto-symbols)** is reframed: proto-symbols are conditional modifiers attached to
   basic-expression channels, not arbitrary signals competing for behavioural relevance from
   scratch.
3. **The substrate that runs steps 1–5** is `play_mode` itself, not a parallel language-acquisition
   substrate. Language is a specialised play-game instantiation.

Open questions this surfaces:
- *How does the basic expression catalog get installed?* In humans and dogs, much of it is innate
  (or near-innate). REE may need either a small library of innate basic-expression slots or an
  earlier developmental phase in which they are scaffolded by simpler social interaction.
- *What is the minimum number of catalog entries to bootstrap a working language game?* The
  literature suggests not many — joint attention + distress + approach + mimicry may be enough.
  Worth a falsifiable scoping experiment under appropriate substrate.
- *Does this picture predict that artificial systems trained without play_mode-like episodes will
  fail to acquire language compositionally?* It predicts they should fail to acquire **socially
  grounded** language compositionally — pattern-matching imitation may still work, but the
  conversational-violation-as-synthetic-harm pathway will be absent.

---

## Cross-Species Naturalistic Observation: the Negation Primitive

The minimum-sufficient-catalog question (open question 2 below) asked what additional
basic-expression entries would be needed for compositional bootstrapping beyond the eight
already enumerated. The strongest theoretical prediction was a *negation primitive* — without
active negation, compositional generalisation collapses (you can mark "this" but not "not
this," "X" but not "X is not Y").

A naturalistic observation in a non-language-acquiring social vertebrate (Steve, a domestic
dog) sharpens the prediction substantially. Steve displays three architecturally distinct
negation primitives:

1. **Directional / demonstrative negation** — pulls the lead the opposite way, *clearly enough
   for signal but not trying to actually go that way*. The action is performed rather than
   enacted: he produces the literal-direction-action precisely because he expects it to be read
   as signal. Cognitively this requires modelling the partner's interpretation and trusting
   them to read performance-not-literal.
2. **Play-frame negation (comic offer-and-withdraw)** — offers a toy then withdraws it
   demonstratively to mean "the negative is the intention." The negation is *only legible
   because play_mode is open*. Outside the play frame, snatching back an offered thing reads as
   defection or possessiveness; inside the frame, it reads as comedic negation precisely
   because play_mode's synthetic-stakes authorisation lets the partner interpret the action as
   performance.
3. **Attentional negation (pointed gaze-aversion)** — when withholding a toy and the partner
   seeks it, Steve plants his gaze pointedly elsewhere and holds his position. This is *very
   different from ignoring*: it is an active not-looking that requires Steve to model that the
   partner expects shared attention and to actively decline it. Structurally it is the inverse
   of the joint-attention frame-opening primitive — refusal at the frame-management layer
   rather than the content layer.

**The architectural sharpening.** All three primitives are *demonstrative rather than literal*
— they live in a meta-layer that requires the partner to interpret the action as performance.
That meta-layer is precisely the play_mode authorisation structure (MECH-194 / ARC-049):
actions whose literal consequences are bracketed and whose interpretation lives in the
play-frame-adjacent meta-layer. The negation primitive is therefore not "head shake or
turn-away as a token"; it is **any action that means its-own-opposite-as-signal under
play-frame authorisation**.

The cross-species evidence reinforces MECH-308's central claim. Negation in a vertebrate that
does not acquire compositional language nonetheless recruits the play_mode substrate the
language-game would later run on — exactly the pattern predicted if play_mode is the
phylogenetically-prior substrate that hosts the bootstrap primitives. The same cognitive
machinery (model partner's interpretation; produce action-as-signal; trust partner to read
performance) is in place, awaiting the conditional-modifier layer (proto-symbols) that humans
add on top.

This also makes a falsifiable cross-species prediction testable in principle: vertebrates
without a robust play_mode substrate (i.e. species whose play repertoire is narrow or absent)
should fail to display demonstrative negation primitives, even if they display literal
withdrawal or aggression. Conversely, vertebrates with rich play repertoires (corvids,
cetaceans, canids, primates) should display the demonstrative-negation pattern that Steve
shows.

The pre-linguistic infant analogue: the head-shake at 9–12 months is famously *demonstrative*
— performed as signal before negation has propositional content (Spitz 1957 and the
developmental literature on the second of "the three organisers"). The same demonstrative
character is what the catalog entry should specify; head-shake-as-token is a culturally-shaped
instantiation of the deeper primitive.

---

## Open Questions

- Innate vs scaffolded acquisition of the basic expression catalog (above).
- Minimum sufficient catalog for compositional bootstrapping (above).
- Predicted failure modes for systems trained without `play_mode` substrate (above).

## Related Claims (IDs)

- MECH-010 (this claim — language emergence and bootstrapping; the basic-expression-catalog and play-as-language-substrate sections above refine its steps 1 and 3)
- **MECH-308 (companion claim — language acquisition tracks play_mode maturation; registered 2026-05-08; the play-as-language-game framing above is its primary architectural anchor)**
- INV-058 (play structurally necessary)
- INV-059 (bilateral play-frame signal)
- MECH-194 (synthetic signal substitution under play)
- MECH-195 (strategy / calibration dissociation)
- ARC-049 (play frame tag)
- ARC-009 (language as coordination layer; parent claim)
- ARC-010 (social cognition; OTHER_SELFLIKE detection)
- MECH-014 (minimal signalling channel; pre-language interface)

## References / Source Fragments

- `docs/processed/legacy_tree/architecture/language/emergence_and_bootstrapping.md`
- `docs/architecture/play_mode.md` (play_mode substrate that this doc now treats as the language-game host)
- `docs/architecture/language/minimal_signalling_channel.md` (the minimal pre-language interface)
- `docs/architecture/language/language_and_learning.md`
- `docs/architecture/arcuate_fasciculus.md` (dorsal sequence→motor channel)
