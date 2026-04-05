# Thought Intake: Steve the Dog -- Vocalization Timbre, z_beta Leakage, and Other-Directed Harm Avoidance

**Date:** 2026-04-05
**Session type:** Design conversation (Claude Code)
**Raw thought file:** `docs/thoughts/2026-04-05_steve_dog_emotional_mirroring.md`
**Output:** Claims MECH-182, MECH-183, MECH-184, MECH-185 registered in claims.yaml (2026-04-06). Lit search completed (2026-04-06). Architecture stubs noted. Vignettes page and ree-paper addition created (2026-04-06).

---

## Prompt

Daniel's observation (verbatim):

> Observing my wonderfully social and good dog Steve. I have come to believe he has all the cognitive
> machinery for ethical behaviour that humans have and is a little person with a self model. Now he
> would have learned that harms exist and with his attribution stream working would have picked out
> approach gradients for harm. He would have noticed that surprise is often on approach to harm.
> Surprise increases adrenaline and increases muscle tone which leads to a very particular timbre
> change in his barks. So he knows that in his self model this timbre change is often indicative of
> an approach to harm gradient. So he is concerned by this timbre change. Feeling it is part of what
> we know as the emotion of trepidation, fear. He also has attributed similar models to others as his
> self model. He hears the same timbre change in the voice of my husband. Because emotional states
> plotted for others directly leak into the same places that self emotions are when he hears the timbre
> change in my husband he is instantly fearful and trepidation about the circumstance is active and
> he plots harm gradients to avoid for my husband and rollouts from his hippocampus aim to enable
> escape from harm for my husband by his actions. I understand that we now know that this manifestation
> of love is scalable (I may be wrong) but nevertheless it shows why he is such a good boy. As a pack
> animal the emotional sharing is strong and he uses his understanding to the best of his ability to
> share attention, goals, and harm avoidance with his loved ones.

Daniel's addition:

> the surprise approach linkage which creates curiosity is helpfully doubled since surprise regarding
> hearing the signal and the leaked surprise fast empathy means Steve really wants to approach the
> distressed loved one

---

## What's New vs. Existing REE Docs

| Topic | Status |
|-------|--------|
| Harm via mirror modelling (INV-005) | Already covered |
| Love as long-horizon care-investment (INV-029) | Already covered |
| Empathy coupling via OTHER_SELFLIKE and control-plane knobs (MECH-031) | Already covered |
| OTHER_SELFLIKE high-recall bias (MECH-032) | Already covered |
| Counterfactual other-cost-aversion as motivational surrogate (MECH-127) | Already covered |
| **Acoustic/vocal timbre as learned cross-modal harm-approach signal (self-experience learning, cross-agent generalization)** | **NEW -- MECH-031 covers realized empathy coupling, not acoustic harm signal learning** |
| **Direct z_beta leakage (other-agent affective state activates self z_beta directly, not as inference)** | **NEW -- PAM functional description exists, computational implementation as z_beta leakage is novel** |
| **Other-directed hippocampal rollouts (planning architecture unchanged, harm-gradient source swapped to other-agent)** | **NEW -- mechanistic grounding of INV-029 not previously specified** |
| **Surprise-doubled approach gradient (prediction error approach + z_beta leakage approach converging on distressed other)** | **NEW -- explains approach-toward vs avoidance-for-other distinction not covered anywhere** |

---

## Key Formulations

### MECH-182: Vocalization timbre as learned cross-modal harm-approach signal

> Physiological arousal during harm-approach (surprise -> adrenaline -> muscle tone) produces
> characteristic acoustic changes in an agent's own vocalizations. The harm attribution stream
> learns this cross-modal correlation: timbre change is a reliable predictor of harm approach.
> Generalization: when the same acoustic feature appears in another agent's vocalizations, the
> harm-approach signal fires via the attributed other-model, generating trepidation/fear.

Structural steps:
1. Agent approaches harm gradient -> surprise activates -> adrenaline -> muscle tone changes
2. Muscle tone change alters vocalization timbre (cross-modal acoustic effect)
3. Attribution stream registers co-occurrence: timbre-change predicts harm proximity
4. Self-model registers timbre-change as harm-approach signal (emotion of trepidation)
5. Attribution assigns similar self-models to other agents (pack/social salience)
6. Other agent vocalizes with same timbre change -> attributed other-model fires harm-approach signal
7. Own trepidation activates as if self were approaching harm -> protective behavioral cascade

Key distinction from MECH-031: MECH-031 describes general empathy coupling via control-plane
modulation. MECH-182 describes the specific acoustic learning mechanism by which one sensory
modality (vocalization timbre) becomes a cross-agent harm signal via embodied self-experience.
The generalization from own-vocalization-experience to other-vocalization is the novel step.

### MECH-183: z_beta leakage -- direct affective activation from other-model

> When an agent's other-model is sufficiently coupled (via attribution stream + OTHER_SELFLIKE
> tagging), the other agent's affective state activations propagate directly into self z_beta
> processing -- not as inference about the other but as direct activation. This is the
> computational implementation of INV-005 (harm via mirror modelling): emotional states
> plotted for others "directly leak into the same places that self emotions are."

Structural steps:
1. OTHER_SELFLIKE tagging marks agent-B model as sufficiently self-like
2. Attribution stream maintains running z_beta estimate for agent-B
3. Acoustic harm-approach signal fires (MECH-182) in attributed B-model
4. B's z_beta (fear, trepidation) activates in the attributed model
5. Via leakage gate (gated by attribution stream coupling strength): B's z_beta directly
   activates own z_beta processing -- bypassing inference
6. Agent experiences own z_beta activation as fear/trepidation about B's circumstance
7. This activation drives protective behavioral cascade (MECH-184)

Key distinction from MECH-031: MECH-031 describes modulation (how empathy adjusts existing
behavior via control-plane knobs). MECH-183 describes direct activation -- the other's state
arrives in self z_beta not as a parameter change but as an affective signal. This is additive
to modulation, not the same mechanism.

Relationship to PAM (Perception-Action Model): Preston & de Waal's PAM describes the functional
pattern (shared representations activated by perception of other's state). MECH-183 is the
specific computational implementation: z_beta leakage gated by attribution stream + OTHER_SELFLIKE
coupling. The gating mechanism is novel.

### MECH-184: Other-directed hippocampal harm avoidance

> When z_beta leakage causes harm-gradient activation to be other-referenced, hippocampal
> rollout proposals target harm avoidance for the other agent. The planning architecture is
> structurally identical to self-preservation; only the harm-gradient source has changed.
> This is the mechanistic grounding of INV-029 (love as long-horizon care-investment):
> love is architecturally the same as self-preservation, with the harm-gradient source
> pointing at the coupled other-agent.

Structural steps:
1. z_beta leakage activates harm-gradient for other-agent's circumstance (MECH-183)
2. Hippocampal rollout engine receives harm-gradient -- reads it as harm-to-avoid
3. Rollout proposals generate candidate trajectories for harm avoidance
4. Trajectories target escape/protection for the other agent (harm source is other-referenced)
5. Commitment gating evaluates proposals against cost and achievability
6. Behavioral output: approach distressed other + protective action sequence

Key distinction from MECH-127 (counterfactual other-cost-aversion): MECH-127 is motivational
bypass -- other-cost-aversion substitutes for a degraded direct pathway. MECH-184 is direct
gradient substitution: the harm gradient itself becomes other-referenced, running through the
same hippocampal planning machinery without any bypass. Both are additive contributions.

Note: this mechanism requires the planning architecture to be sufficiently general to accept
harm-gradient inputs regardless of their source (self vs other). This is an architectural
commitment that V3 implementation must verify.

### MECH-185: Surprise-doubled approach gradient toward distressed other

> When harm-signal timbre is heard from a coupled other-agent, two simultaneous approach
> gradients converge on the distressed other:
> (1) Observer's own prediction error from unexpected acoustic signal -> curiosity approach
>     gradient (standard surprise -> approach for novel/unexpected stimuli)
> (2) z_beta leakage carries the other's surprise/distress as direct affective activation ->
>     second curiosity/approach gradient from the leaked surprise
> Both converge on approaching the distressed loved one. This explains why empathic animals
> are pulled TOWARD the distressed other rather than only avoiding harm for them from a distance.

Structural steps:
1. Coupled other-agent vocalizes with harm-timbre signal (unexpected to observer)
2. Observer's prediction error activates: unexpected acoustic input -> surprise
3. Surprise -> approach gradient (curiosity drives toward novel/unexpected)
4. Simultaneously: z_beta leakage carries other-agent's own surprise/fear
5. Leaked surprise activates second approach gradient in observer's own z_beta
6. Two approach gradients superpose: observer is doubly drawn toward distressed other
7. Combined approach motivation drives protective contact (not flight/distance)

Key insight: this explains the distinction between approach-toward vs avoidance-for-other.
Self-preservation from harm generates avoidance (flee own harm). Other-directed harm avoidance
alone (MECH-184) could in principle generate protective action from a distance. The doubled
approach gradient from MECH-185 explains why pack/social animals physically approach and
attempt contact with distressed conspecifics -- the curiosity and leaked distress together
make proximity adaptive, not just harm-avoidance action.

---

## Affected Existing Claims

| Claim ID | Title (short) | Relation |
|----------|---------------|----------|
| INV-005 | Harm via mirror modelling | MECH-183 is the specific computational mechanism; MECH-182 is the sensory trigger |
| INV-029 | Love as long-horizon care-investment | MECH-184 is the mechanistic grounding -- love = self-preservation with other-referenced harm gradient |
| MECH-031 | Empathy coupling via control-plane knobs | MECH-182/183 are additive -- acoustic learning + leakage are distinct from modulation |
| MECH-032 | OTHER_SELFLIKE high-recall bias | Precondition for MECH-183/184 -- high-recall bias ensures coupling is established for pack members |
| MECH-127 | Counterfactual other-cost-aversion | MECH-184 is additive -- direct gradient substitution, not motivational bypass |
| INV-034 | Goal maintenance necessary for ethical agency | MECH-185 shows goal maintenance can be other-referenced and amplified by shared surprise |

No conflicts with existing claims identified. All four new mechanisms are additive -- they
describe specific pathways and implementations not covered by existing claims.

---

## Candidate Claims (registered 2026-04-06 in claims.yaml)

### MECH-182: Vocalization timbre as learned cross-modal harm-approach signal, generalizing to other-agent vocalizations

> Physiological arousal (surprise -> adrenaline -> muscle tone) causes acoustic changes in own
> vocalizations correlated with harm approach. This cross-modal association is learned from
> self-experience by the harm attribution stream, then generalizes: the same acoustic feature
> in another agent's vocalizations activates the harm-approach signal via the attributed
> other-model.

- **Type:** mechanism_hypothesis
- **Subject:** social.vocalization_harm_signal
- **Polarity:** asserts
- **Status:** candidate
- **Related:** INV-005, MECH-031, MECH-032

### MECH-183: z_beta leakage -- attributed other-model affective state activates self z_beta directly, not via inference

> When an agent's other-model is sufficiently coupled via attribution stream + OTHER_SELFLIKE
> tagging, the other agent's affective state activations leak directly into self z_beta
> processing -- not as inference about the other but as direct activation. This is the
> specific computational implementation of INV-005 (harm via mirror modelling).

- **Type:** mechanism_hypothesis
- **Subject:** social.zbeta_leakage
- **Polarity:** asserts
- **Status:** candidate
- **Related:** INV-005, MECH-031, MECH-032

### MECH-184: Other-directed hippocampal harm avoidance -- planning architecture identical to self-preservation with harm-gradient source swapped to coupled other-agent

> When z_beta leakage causes harm-gradient activation to be other-referenced, hippocampal
> rollout proposals target harm avoidance for the other agent. The planning architecture is
> structurally identical to self-preservation; only the harm-gradient source has changed.
> This is the mechanistic grounding of INV-029 (love as long-horizon care-investment).

- **Type:** mechanism_hypothesis
- **Subject:** social.other_directed_harm_avoidance
- **Polarity:** asserts
- **Status:** candidate
- **Related:** INV-029, MECH-183, MECH-031, MECH-127

### MECH-185: Surprise-doubled approach gradient toward distressed other -- prediction error approach and z_beta leakage approach converge simultaneously

> When harm-signal timbre is heard from a coupled other-agent, two simultaneous approach
> gradients converge on the distressed other: (1) observer's own prediction error from
> unexpected acoustic signal -> curiosity approach gradient; (2) z_beta leakage carries the
> other's surprise/distress as direct affective activation -> second curiosity approach gradient.
> Both converge on approaching the distressed loved one.

- **Type:** mechanism_hypothesis
- **Subject:** social.empathic_curiosity_approach_doubling
- **Polarity:** asserts
- **Status:** candidate
- **Related:** MECH-183, MECH-184, INV-029

---

## Literature Search (2026-04-06)

Targeted review: `evidence/literature/targeted_review_social_emotional_mirroring/` (10 entries, Wave 1).

### MECH-182: Vocalization timbre as cross-modal harm signal

**Novelty verdict: PARTIAL**

Acoustic substrate documented:
- **Andics et al. 2014 (Current Biology):** Dogs and humans share voice-sensitive cortical regions
  processing emotional valence from vocalizations -- including f0 (fundamental frequency, the main
  carrier of timbre change) in conserved auditory regions. Establishes that dogs process
  conspecific and heterospecific vocalizations with affective content using homologous neural
  machinery.
- **Balint et al. 2022 (NeuroImage):** Multimodal vocal emotion processing in dogs; confirms
  cross-species generalization of the acoustic-affective substrate.

What is not in the literature: the specific novel component -- learning the harm-signal
correlation from own-vocalization experience during physiological arousal (self-model grounding)
and generalizing cross-agent. The acoustic substrate is documented; the learning mechanism and
cross-agent generalization via attributed self-model is novel.

### MECH-183: z_beta leakage

**Novelty verdict: PARTIAL**

PAM functional description well-established:
- **Preston & de Waal 2002 (Behavioral and Brain Sciences):** Perception-Action Model -- shared
  representations between self and other; perceiving another's emotional state activates the
  observer's own corresponding representations. Foundational PAM paper.
- **de Waal & Preston 2017 (Nature Reviews Neuroscience):** Autonomic synchrony evidence --
  physiological coupling between conspecifics (heart rate, skin conductance) during social
  interaction. Shows direct (not inferential) affective coupling in mammals.
- **Lamm, Decety & Singer 2011 (NeuroImage):** 32-study meta-analysis of shared neural substrate
  for pain/empathy -- insula and mACC consistently activated for both self-pain and observed-pain.
  Confirms shared substrate mechanism.

What is not in the literature: the specific computational implementation as z_beta leakage
gated by attribution stream + OTHER_SELFLIKE tagging. PAM describes the functional outcome;
the gating mechanism is novel.

### MECH-184: Other-directed hippocampal harm avoidance

**Novelty verdict: CONFIRMED**

Anatomical substrate identified:
- **Amft et al. 2014 (Brain Structure and Function):** Social-affective default mode network
  (DMN) includes hippocampus and vmPFC -- identifies the anatomical basis for social-affective
  planning. Consistent with hippocampal involvement in other-directed planning.
- **Kesner et al. 2022 (Progress in Neurobiology):** Supramammillary-hippocampal-dopamine seeking
  circuit -- hippocampus engages in motivated trajectory planning; dopamine modulates seeking
  behavior. Anatomical substrate supports, but does not describe, other-directed rollout reuse.

What is not in the literature: no paper describes hippocampal planning being reused with
harm-gradient source swapped to another agent. Amft and Kesner provide anatomical substrate
only. The computational claim -- same architecture, swapped gradient source -- is novel.

### MECH-185: Surprise-doubled approach gradient

**Novelty verdict: CONFIRMED**

Behavioral evidence for approach toward distressed others:
- **Sato et al. 2015 (Animal Cognition):** Rats help distressed cagemates -- demonstrates
  prosocial approach behavior in rodents; interpreted as empathy-driven helping.
- **Ben-Ami Bartal et al. 2016 (Frontiers in Psychology):** Anxiolytic specifically impairs
  helping -- pharmacological dissection showing that anxiolytic (reduces anxiety/surprise) blocks
  approach and helping, while the distress is maintained. Consistent with surprise/arousal as
  necessary component of approach motivation.
- **Yu et al. 2024 (Behavioural Processes):** Multimodal emotional contagion in social mammals --
  behavioral evidence for cross-modal affective transfer.

What is not in the literature: the dual converging gradient account. Behavioral evidence for
approach exists; single-mechanism explanations (empathic distress, contagion, or curiosity
alone) are offered. The specific prediction that two independent gradients (own prediction error
+ leaked z_beta surprise) converge simultaneously on approaching the distressed other -- and
that this explains approach-toward vs avoidance-for-other -- is not described.

---

## Paper Angle

This vignette is primarily relevant to the **social/ethics extension paper** (NOT paper 1 per
`first_paper_brief.md`). The Steve observation is the most accessible biological illustration
of INV-029 and the mechanism by which love emerges architecturally from harm avoidance +
z_beta coupling.

Core contribution for the social paper:
- The Steve vignette shows all four mechanisms operating in a real social mammal, grounded in
  known neuroscience (conserved auditory regions, PAM, DMN/hippocampus anatomy)
- MECH-184 provides the first mechanistic grounding of INV-029: love is not a distinct
  architectural module but self-preservation with an other-referenced harm gradient
- MECH-185 provides a novel dual-gradient account of approach-toward behavior in empathic
  animals -- testable as a prediction (anxiolytics should impair approach but not protective
  action from distance; the Bartal 2016 finding is consistent)
- The vocalization-timbre pathway (MECH-182) grounds the mechanism in embodied self-experience,
  not abstract inference -- this is the REE signature: no explicit emotion module, learning
  from co-occurrence in the self-model

**Paper angle: strong for social extension.** Steve as a worked example could serve as the
opening vignette -- concrete, familiar, non-human (avoids anthropocentric objections), and
illustrates all four mechanisms in one coherent narrative.

---

## Next Steps

1. ~~Register MECH-182, MECH-183, MECH-184, MECH-185 in `docs/claims/claims.yaml`~~ DONE 2026-04-06
2. ~~Literature search (Wave 1)~~ DONE 2026-04-06 -- targeted_review_social_emotional_mirroring/ (10 entries)
3. Architecture stubs -- social.md should gain stubs for MECH-182/183/184/185 when social
   extension work begins in earnest (not in this session -- scope discipline)
4. Flag for social/ethics extension paper planning when that paper is active
5. Vignettes page and ree-paper addition -- DONE 2026-04-06 (per output header)
