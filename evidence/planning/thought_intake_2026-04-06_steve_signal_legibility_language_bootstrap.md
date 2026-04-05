# Thought Intake: Steve the Dog -- Signal Legibility, Language Bootstrap, and Self-Strengthening Coordination

**Date:** 2026-04-06
**Session type:** Design conversation (Claude Code)
**Raw thought file:** `docs/thoughts/2026-04-06_steve_signal_legibility_language_bootstrap.md`
**Extends:** `evidence/planning/thought_intake_2026-04-05_steve_dog_emotional_mirroring.md` (Steve #1)
**Output:** Claims MECH-191, MECH-192, MECH-193, ARC-048, INV-057 registered in claims.yaml (2026-04-06). Lit search completed (2026-04-06). Vignettes page extended and ree-paper updated (2026-04-06).

---

## Prompt

Daniel's observation (verbatim):

> Steve the dog also automatically emits a whining when wanting a lot. Externalisation of different basic functions of his cognition is an important part of co-ordination as he needs a signal to pick up from others that match self model states. We should be able to map many of these. His huff of breathing out when he is abandoning plans, his yelp when hurt, his little face which notes him to be a little person, his tail wag, his play pose and more. These stereotypes signals most likely match very specific aspects of function in his mind and the externalisation of them allows for the fast empathy system to produce coordination. The reward just by seeing his face and licks from him or petting him that reaffirms. All of these signals allow for the fast empathy system to produce coordination. Humans likely have many more and mapping them will be important. Understanding the pathways that are associated with this and comparing the functional motif of large language models as well as the human specific brain pathways that exist should help with the language bootstrap phase of REE development

---

## What's New vs. Existing REE Docs

| Topic | Status |
|-------|--------|
| Empathy coupling via OTHER_SELFLIKE (MECH-031) | Already covered |
| z_beta leakage from other-model (MECH-183) | Already covered (Steve #1) |
| Cross-modal harm signal (MECH-182) | Already covered (Steve #1) -- but only for ONE signal (bark timbre) |
| Language emergence as functional self-representation (INV-003) | Already covered -- but no pre-linguistic-to-linguistic bridge described |
| **Stereotyped signals as causal externalizations of specific functional states (whine=wanting, huff=plan abandonment, yelp=nociception, etc.)** | **NEW -- extends MECH-182's single-signal observation to a general principle** |
| **Signal legibility as prerequisite for fast empathy coordination** | **NEW -- without legible signals, MECH-183 leakage cannot produce coordination** |
| **Social reward signals reinforce empathic coupling (oxytocin-gaze loop, affiliative touch)** | **NEW -- the coordination loop is self-strengthening** |
| **Language as high-bandwidth version of pre-linguistic functional-state externalization** | **NEW -- connects INV-003 to the pre-linguistic signal repertoire; defines the language bootstrap prerequisite** |
| **Cross-species legibility as evidence of functional specificity** | **NEW -- invariant-level claim: legibility without convention implies causal generation** |

---

## Key Formulations

### 1. The legibility condition

For z_beta leakage to produce coordination, the perceived signal must map onto a corresponding internal state. Stereotyped signals satisfy this because they are causal products of the states they communicate.

### 2. Signal catalog

| Signal | Functional state | REE component |
|--------|-----------------|---------------|
| Whine | Wanting/desire | z_goal activation without satisfaction |
| Huff | Plan abandonment | E3 trajectory discard |
| Yelp | Nociception | z_harm activation |
| Facial expression | Attachment/recognition | OTHER_SELFLIKE model activation |
| Tail wag | Positive arousal | z_beta positive valence |
| Play bow | Mode invitation | Mode manager state transition request |
| Licks/petting (received) | Social reward | Coupling reinforcement |

### 3. The language bootstrap

Language adds bandwidth and resolution to a channel that already exists. The prerequisite is that functional states exist as referents. Pre-linguistic: yelp -> "I hurt." Linguistic: "My leg hurts when I walk on wet grass." Same referent architecture, higher resolution.

### 4. The self-strengthening loop

coordination -> affiliative exchange -> stronger coupling -> more sensitive state-matching -> better coordination.

---

## Affected Existing Claims

| Claim ID | Title (short) | Relation |
|----------|---------------|----------|
| MECH-182 | Vocalization timbre as harm signal | MECH-191 generalizes from one signal to the full repertoire |
| MECH-183 | z_beta leakage | MECH-192 identifies the legibility prerequisite for MECH-183 to produce coordination |
| INV-003 | Language as functional self-representation | ARC-048 provides the pre-linguistic bridge |
| INV-005 | Harm via mirror modelling | MECH-191/192 specify how the mirror modelling signal is transmitted |
| INV-029 | Love as long-horizon care-investment | MECH-193 explains how the coupling strengthens over time |
| MECH-031 | Empathy coupling via control-plane knobs | MECH-192 is additive -- legibility is upstream of coupling |

No conflicts with existing claims identified. All five new claims are additive -- they describe
specific pathways and structural requirements not covered by existing claims.

---

## Candidate Claims (registered 2026-04-06 in claims.yaml)

### MECH-191: Stereotyped behavioral signals are causal externalizations of specific internal functional states

> Stereotyped signals (whine=wanting, huff=plan-abandonment, yelp=nociception, tail-wag=positive-
> arousal, play-bow=mode-invitation) are causally generated by internal functional states. Because
> the signal is a causal product (not a convention), any observer with a corresponding internal
> state can map it. Extends MECH-182 from one signal to the full repertoire.

- **Type:** mechanism_hypothesis
- **Subject:** social.signal_legibility
- **Polarity:** asserts
- **Status:** candidate
- **Related:** MECH-182, MECH-183

### MECH-192: Signal legibility is prerequisite for fast empathy coordination

> z_beta leakage can only produce functional state-matching if the perceived signal maps onto a
> corresponding internal state in the observer. Stereotyped behavioral signals (MECH-191) meet
> this requirement because they are produced by the same functional states they communicate.
> Explains why fast empathy works cross-species without shared language.

- **Type:** mechanism_hypothesis
- **Subject:** social.legibility_empathy_prerequisite
- **Polarity:** asserts
- **Status:** candidate
- **Related:** MECH-183, MECH-191

### MECH-193: Social reward signals reinforce empathic coupling strength

> Affiliative signals (petting, licks, facial expressions) activate reward pathways that strengthen
> coupling between self-model and attributed other-model. The coordination loop is self-reinforcing:
> successful coordination -> affiliative exchange -> stronger coupling -> more sensitive state-
> matching -> better coordination. Oxytocin-gaze loop and C-tactile afferents provide the neural
> substrate.

- **Type:** mechanism_hypothesis
- **Subject:** social.reward_coupling_reinforcement
- **Polarity:** asserts
- **Status:** candidate
- **Related:** MECH-183, MECH-192, INV-029

### ARC-048: Language as high-bandwidth externalization of pre-existing functional states

> Pre-linguistic Steve says "I hurt" (yelp); linguistic Daniel says "my leg hurts when I walk on
> wet grass." Same referent architecture, higher resolution. Language adds bandwidth and precision
> to a channel that already exists. The language bootstrap phase requires functional states
> (harm, wanting, reward, mode) to pre-exist as referents.

- **Type:** architecture_hypothesis
- **Subject:** language.externalization_channel
- **Polarity:** asserts
- **Status:** candidate
- **Related:** INV-003, MECH-191, MECH-192

### INV-057: Cross-species signal legibility evidences functional specificity

> If stereotyped behavioral signals were socially conventional, cross-species reading would require
> separate learning for each species. That dog-human emotional communication works largely
> automatically evidences shared functional architecture. The cross-species legibility is formal
> evidence that signals are causally generated by their referent states.

- **Type:** invariant
- **Subject:** social.cross_species_legibility_evidence
- **Polarity:** asserts
- **Status:** candidate
- **Related:** MECH-191

---

## Literature Search (2026-04-06)

Targeted review: `evidence/literature/targeted_review_social_signal_legibility/` (10 entries, Wave 1).

### MECH-191: Stereotyped signals as causal externalizations

**Novelty verdict: PARTIAL**

Causal production via source-filter mechanisms well-established; discrete functional-state-to-signal
mapping and "cross-architectural legibility" framing novel.

Key papers:
- **Briefer 2012:** Vocal expression of emotions in mammals -- source-filter theory of vocal production
  connecting acoustic parameters to affective states.
- **Brudzynski 2007:** Ultrasonic calls of rats as indicator signals of negative or positive states --
  demonstrates that distinct call types are generated by distinct affective states via separable
  neural substrates.

### MECH-192: Legibility prerequisite for fast empathy

**Novelty verdict: PARTIAL**

Cross-species emotion recognition in dogs well-documented; framing legibility as prerequisite
specifically for z_beta leakage coordination is novel.

Key papers:
- **Albuquerque et al. 2016:** Dogs recognize dog and human emotions -- multimodal (face + voice)
  cross-species emotion recognition without training; demonstrates automatic legibility.
- **Silva et al. 2011:** Canis empathicus -- dogs show empathic-like responses to human emotional
  displays across modalities.

### MECH-193: Social reward reinforces coupling

**Novelty verdict: PARTIAL**

Oxytocin-gaze loop and C-tactile touch reward established; connecting to empathic coupling
strength specifically is novel.

Key papers:
- **Nagasawa et al. 2015 (Science):** Oxytocin-gaze positive loop -- mutual gaze between dog and
  owner increases oxytocin in both species; the loop is self-reinforcing.
- **Walker et al. 2017:** C-tactile afferents -- unmyelinated low-threshold mechanoreceptors that
  specifically encode pleasant/affiliative touch, providing reward signal for social contact.

### ARC-048: Language as high-bandwidth externalization

**Novelty verdict: PARTIAL**

Language evolution from emotional vocalization classical; REE-specific framing as bandwidth increase
over pre-existing functional-state channel is novel.

Key papers:
- **Filippi 2016:** Emotional prosody as language precursor -- connects pre-linguistic emotional
  vocalization to language evolution through prosodic continuity.
- **Fournier 2026:** Cross-species vocal emotion -- evidence for conserved emotional encoding
  in vocal signals across phylogenetically distant species.

### INV-057: Cross-species legibility = functional specificity

**Novelty verdict: PARTIAL**

Darwin/Ekman universality classical; using legibility as formal evidence for functional specificity
rather than convention is novel argumentative move.

Key papers:
- **Molnar et al. 2010:** Blind perceivers can identify emotional valence from dog barks --
  demonstrates that legibility does not require visual convention learning; acoustic information
  alone is sufficient.
- **Ekman 2009:** Darwin's contributions to our understanding of emotional expressions --
  reviews the universality thesis and cross-cultural evidence for innate emotional expression.

---

## Paper Angle

This vignette is primarily relevant to:

1. **Future social/ethics extension paper** (not paper 1) -- signal legibility and the
   self-strengthening coupling loop are core mechanisms for social agency.
2. **Future language paper** -- ARC-048 connects INV-003 to concrete pre-linguistic substrate;
   defines what the language bootstrap requires (functional states as referents).

The LLM functional motif comparison angle (comparing human brain-specific pathways with LLM
architectural motifs) may be a separate paper opportunity. Daniel's prompt specifically mentions
"comparing the functional motif of large language models as well as the human specific brain
pathways" -- this is a distinct research program from the pre-linguistic signal mapping and
should be scoped separately.

---

## Next Steps

1. ~~Register MECH-191, MECH-192, MECH-193, ARC-048, INV-057 in `docs/claims/claims.yaml`~~ DONE 2026-04-06
2. ~~Literature search (Wave 1)~~ DONE 2026-04-06 -- targeted_review_social_signal_legibility/ (10 entries)
3. ~~Vignettes page extended and ree-paper updated~~ DONE 2026-04-06 (per output header)
4. Architecture stubs -- social.md should gain stubs for MECH-191/192/193 and ARC-048 when
   social extension work begins in earnest (not in this session -- scope discipline)
5. Language bootstrap design doc -- ARC-048 warrants a dedicated architecture doc mapping
   pre-linguistic signals to functional motifs (future work)
6. LLM functional motif comparison -- separate research program; flag for future scoping
