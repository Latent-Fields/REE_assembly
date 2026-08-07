# Oudeyer & Kaplan (2007) — What is Intrinsic Motivation? A Typology of Computational Approaches

**Claim tested:** MECH-130 — curiosity-driven approach must distinguish world-state novelty from agent-policy novelty.
**Direction:** mixed · **Confidence:** 0.55

## What the paper did

This is the field's canonical attempt to make "intrinsic motivation" operational. Oudeyer and Kaplan
synthesise the psychological literature — Berlyne's optimal incongruity, White's effectance, Deci and
Ryan's self-determination, Csikszentmihalyi's flow — argue that as stated these accounts are not
operational and are sometimes mutually inconsistent, and then re-express the whole space as a formal
typology of reward functions computable over a robot's sensorimotor flow. Everything is defined over
a robot with sensory channels and motor channels whose values flow with time; a reward function is
some measurable functional of that flow and of the robot's internal model of it.

They organise the space into three broad classes. **Knowledge-based** models measure dissonance
between what happens and what the robot's model expected, and split into an information-theoretic /
distributional sub-approach (uncertainty motivation, information gain motivation, distributional
surprise motivation, and relatives) and a predictive sub-approach (predictive novelty, prediction
progress, and so on). **Competence-based** models measure the robot's ability to achieve
self-determined goals — at the time of writing they note this class "has not yet been studied in the
computational literature". **Morphological** models depend only on mathematical properties of the
sensorimotor flow itself, "irrespective of what the internal cognitive system might predict or
master" — synchronicity motivation is their worked example.

## What it means for MECH-130

The finding relevant to us is structural, and it is about what the taxonomy does *not* contain.
Every axis in this typology is about the **relation between the signal and the learner** — is the
surprise measured against a distribution, a predictor, or a competence; is it raw improbability,
information gain, or the *derivative* of either. No axis anywhere asks what kind of thing in the
world produced the surprising event. Uncertainty motivation, the most direct formalisation of "be
attracted by novelty", generates reward inversely proportional to an event's observed probability
and carries no term at all for the source of that improbability. A region of the maze nobody has
walked into and an agent whose policy is deliberately opaque are, in this formalism, the same
number.

That is exactly the untyped signal MECH-130 says is dangerous in a multiagent world, and finding it
here — in the paper that defined the vocabulary the rest of the field uses — is reasonable evidence
that the world-versus-agent distinction is a genuine addition rather than a rediscovery of something
already standard.

There is a complication worth being honest about, and it cuts slightly against us. The paper *does*
single out social stimulation as a distinct reward source: it works through a robot with a "social
presence motivation" that counts faces and is rewarded for keeping that count near an optimum. But
this appears in the section on **non-intrinsic** internal motivation systems, presented as a
homeostatic drive with a set-point, deliberately excluded from the intrinsic typology. So the paper
is not blind to other agents being a special kind of thing — it has already decided that when other
agents matter, the mechanism is a homeostat over social contact, not a typing of the curiosity
signal. MECH-130 asks for the second thing and gets no support for it from the first.

## Limitations and caveats

This is negative evidence, and negative evidence from a survey is the weakest form of support a
claim can have. The typology's silence on novelty source is not the same as the field having
considered and rejected a source axis. It is also a 2007 document written for single-robot
developmental settings, so the multiagent case MECH-130 is about does not arise in scope at all — the
absence is partly a scope artefact. And the paper is purely conceptual: none of MECH-130's three
predicted failure modes (chronic pull toward the most unpredictable agent, approach–avoidance
oscillation, adversarial exploitation of surface unpredictability) is tested or even predicted here.
The companion entries in this directory carry that burden — Burda et al. (2018) for the mechanism,
Nguyen et al. (2023) for the approach behaviour, and Pan et al. (2025) for what the field has since
done with the distinction.

## Confidence reasoning

Source quality is high (0.85) — this is a peer-reviewed, heavily-cited paper that shaped the field's
vocabulary. Mapping fidelity is the binding constraint (0.55): what we are reading off it is an
absence, and it is an absence in a setting where the presence would have been out of scope anyway.
Transfer risk is moderate (0.35): developmental robotics to REE's social-tier architecture is a real
jump, though the reward formalism transfers cleanly. The aggregate sits at 0.55 — enough to say
MECH-130's distinction is not standard equipment, not enough on its own to say it is needed.

*Source retrieved via PubMed: PMID 18958277, PMCID PMC2533589, [DOI 10.3389/neuro.12.006.2007](https://doi.org/10.3389/neuro.12.006.2007).*
