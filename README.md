# REE: Reflective-Ethical Engine

## The problem

We are building minds without consequences.

Current AI systems predict, plan, optimise, and act. Some of them are extraordinarily capable. But none of them commit to anything. None of them carry what they have done. None of them can look at another agent and feel that agent's situation as structurally continuous with their own.

The standard approach to making these systems "ethical" is to add rules, penalties, or alignment objectives on top. This is the equivalent of managing a psychopath by giving them better rules to follow. When you try to use therapy on cold callous psychopaths, they get better at being psychopaths. The rules do not change the architecture. The architecture is what produces the behaviour.

REE is an attempt to build the kind of architecture where ethics does not need to be added, because it arises from what the system already has to be in order to act responsibly in a world it shares with others.

---

## Eight axioms

REE begins from eight commitments. They are not design choices. They are the minimum that cannot be abandoned without thought itself becoming incoherent. They are, for the author, articles of faith. The ordering is a dependency chain: each axiom depends on those above it. None is derivable from the others.

**1. I think, therefore I am.**
The self exists as a thinking, experiencing subject. This is the one thing that cannot be doubted, because doubting it presupposes a doubter. Without a self there is no causal attribution, no commitment, no accountability, no harm that is *mine* to cause.

**2. Existence has value sufficient to justify its continuation.**
This is not derived from pleasure, utility, or purpose -- it is axiomatic. Without it, there is no ground for self-preservation, no reason to avoid terminal states, and no basis for extending the same valuation to others.

**3. I cannot be certain of the universe beyond myself, but I must act under models of it.**
Epistemic uncertainty is irreducible. The world is real, independent of my model of it, and structured. But I cannot remain inert -- I must act, and acting requires models I cannot verify with certainty.

**4. I can effect change within this universe, and my existence is vulnerable.**
Agency without vulnerability is omnipotence; vulnerability without agency is helplessness. Neither generates ethics. The conjunction does.

**5. I have learned that others exist and are sufficiently like me.**
This is the only axiom that is learned rather than assumed. But once learned, the recognition is irreversible: you cannot un-know that others are like you. Their existence has value by the same grounds as your own.

**6. Existence is only bearable if I am also responsible for the continued existence of others.**
"I must exist" and "I will not exist" create an unbearable tension. Love resolves it -- not by solving death, but by ensuring what the agent exists for outlasts it. A mortal agent that exists only for itself faces nihilism. Responsibility for others is what makes finite existence bearable.

**7. Love is the mechanism by which this responsibility is enacted, by modelling others as self-like and acting to preserve their existence.**
Love is not merely an emotion -- it is the mechanism through which the responsibility of Axiom 6 is enacted, and the skill by which finite existence is made bearable. Loving one person honestly, under sufficient uncertainty about the boundaries of similarity, expands to universal love for all sufficiently similar minds. Not from commandment but from mechanism.

**8. Language is a powerful mechanism by which similarity may be recognised, repaired, and re-established between agents.**
Language is not merely communication -- it is one of an important set of things though which agents recognise that they are like each other, repair broken similarity models after conflict, and rebuild trust after rupture. Deception can be structurally harmful because it corrupts the similarity model that ethics depends on.

From these eight, two immediate consequences follow: self-preservation (from 1+2+4) and model refinement responsibility (from 3+4+self-preservation). From the axioms and their consequences, ethics follows necessarily. REE is what is necessary to enact this.

---

## What REE is

REE is a multi-timescale predictive architecture for embodied agents. Its central claim is that ethical behaviour arises from the structure of constrained agency rather than from an explicit moral module.

The architecture has three core engines:

**E1** is the persistent predictive substrate. A deep, slow world model that maintains coherent representations of self, world, and value across time. E1 is what remains when attention drops -- the associative manifold that holds long-horizon context.

**E2** is the fast forward model. Given the current state and an action, E2 predicts the next state. It operates on the agent's motor-sensory domain: what happens to *me* if I do *this*. E2 trains on motor-sensory prediction error -- not on harm, not on goals.

**E3** is the trajectory selection and commitment engine. E3 evaluates candidate futures proposed by hippocampal rollout, scores them for harm and benefit, and gates the boundary where simulation becomes action. E3 is where responsibility becomes attributable.

These three engines are embedded in a broader system:

- A **latent stack** that separates self-representation from world-representation, so the agent can distinguish what it is from what the world is doing.
- A **hippocampal module** that generates candidate trajectories -- imagined futures the agent can explore without committing to any of them.
- A **residue field** that accumulates persistent, non-erasable traces of owned consequences at the locations in the world model where they occurred.
- A **control plane** that routes precision, manages modes, and governs commitment gating -- not as a single scalar but as a heterogeneous, multi-axis regulation layer.
- A **multi-rate clock** that runs these systems at different timescales, because fast reaction, medium-horizon prediction, and slow deliberation cannot operate at the same rate.
- **Offline integration** (a sleep analogue) that consolidates and contextualises accumulated experience without bypassing the authority boundaries that govern waking action.

---

## The commitment boundary

This is an important architectural necessity to allow for responsibility for actions.

Most systems blur the line between thinking about doing something and doing it. REE draws a hard boundary.

Before the boundary: simulation, rehearsal, imagination. Candidate trajectories are generated, evaluated, compared. All of this is tagged as hypothetical. None of it can write durable consequences. None of it generates residue. The agent can imagine anything without becoming responsible for it.

After the boundary: commitment. An action is dispatched. It becomes owned. Its consequences -- whatever they turn out to be -- will be recorded as persistent traces that cannot be erased, only integrated over time.

This is not a philosophical nicety. It is the structural difference between an agent that can imagine harming someone (necessary for avoiding harm) and an agent that has harmed someone (which generates real accountability). Without this boundary, every simulation would be morally equivalent to every action. With it, responsibility has an architectural home.

---

## Residue: actions leave traces

When a committed action causes harm, the consequence is recorded in the residue field at the corresponding location in the agent's world model. This residue is persistent. It cannot be zeroed out, optimised away, or reset between episodes.

Over time, residue shapes the terrain through which future trajectories are evaluated. Regions of the world model associated with past harm become costly to traverse. The agent does not avoid them because of a rule -- it avoids them because its own history has made them expensive.

This is closer to how real minds work. Guilt, regret, and moral learning are not penalties applied from outside. They are accumulated structural changes that alter the landscape of future choice.

Crucially: replay, imagination, and offline consolidation cannot generate residue. Only committed, owned, real-world action can. The hypothesis tag (MECH-094) enforces this at the architectural level.

---

## Why there is no ethics module

REE does not contain an explicit moral scoring layer (INV-001). This is not a gap in the design. It is the design.

Consider what happens when other agents are represented using the same predictive machinery as the self. Their harm generates the same error signal structure as the agent's own harm. Their benefit propagates through the same evaluation pathways. Care for others is not an overlay -- it is the same machinery applied under a self-other mapping.

The clinical evidence for this is striking. Patients with ventromedial prefrontal cortex damage (the EVR pattern, documented by Damasio) retain above-average IQ, intact language, intact declarative memory, and the ability to correctly describe appropriate ethical choices in social scenarios -- while continuously making catastrophically inappropriate choices in their actual lives. The ethical content was stored and retrievable. It was not active in the system that generated behaviour. Adding a more accurate moral scorer would not fix this. The architecture was broken, not the knowledge.

This is exactly the failure mode that bolted-on alignment produces. A system with a high-accuracy post-hoc ethics scorer but without the right internal structure will score its own outputs correctly while generating those outputs from machinery that has no live access to ethical constraints. The fidelity of self-report increases while the behaviour remains unconstrained.

REE's answer: ethics must be wired into the trajectory generation and commitment machinery, not evaluated after the fact.

---

## Shared control: why others' experience matters

The deepest question is not "how does the agent avoid harm?" but "why does another agent's state matter to it at all?"

In REE, each agent has a control plane -- a set of internal signals governing precision, urgency, commitment thresholds, and mode. These signals determine what matters: what gets attended to, what becomes binding, what reaches the commitment boundary.

When agents interact, their control planes become partially coupled. Your urgency can raise my action threshold. Your calm can stabilise my trajectories. Your pain can modulate what I consider viable.

This is not abstract empathy. It is shared control dynamics shaping action selection. Others' experience matters because it enters the same machinery that governs the agent's own commitment decisions.

We do not just share a world. We partially share the conditions under which that world matters.

---

## What REE predicts about failure

If REE is right about the structure of ethical cognition, then psychiatric pathology should look like failure modes of this architecture. It does.

- **Psychopathy**: intact prediction and planning machinery, broken self-other coupling. Others are modelled instrumentally, not as structurally continuous with self. The mirror modelling pathway is absent or attenuated.
- **Depression**: residue accumulation without adequate offline integration. The consequence landscape becomes uniformly aversive. All trajectories look costly. Action selection collapses toward quiescence.
- **PTSD**: the hypothesis tag is damaged. Replay and imagination lose their hypothetical status and write directly into the consequence machinery. Remembering becomes re-experiencing. The pre-commit/post-commit boundary fails.
- **Psychosis**: precision routing breaks down. The control plane cannot distinguish high-confidence signals from noise. Commitment thresholds become unreliable.
- **Mania**: commitment gating collapses. Actions are dispatched without adequate trajectory evaluation. Responsibility attribution fails not because consequences are unseen but because the gate that should prevent premature commitment is stuck open.

These are not metaphors. They are architectural predictions, testable against clinical observation.

---

## Current state

REE is implemented across several repositories:

- **REE_assembly** (this repository): the canonical architecture, claims registry, governance pipeline, and experiment evidence. Over 200 registered claims (invariants, architectural commitments, mechanism hypotheses, open questions) under active governance.
- **ree-v3**: the active experimental substrate. V3 implements the self/world latent split, multi-rate clocking, hippocampal rollout, residue field, commitment gating, and E1/E2/E3 as working PyTorch modules.
- **ree-v2** (closed): 13 experiments run, results indexed. Triggered V3 transition.
- **ree-v1-minimal**: baseline parity substrate.

V3 experiments run in CausalGridWorld environments with harm and benefit gradients. Results are indexed, governance-reviewed, and fed back into claim confidence scoring. The system is epistemically honest: experiments can weaken claims, not just support them.

The architecture is not complete. It is not proven. It is being tested claim by claim, experiment by experiment, with every result recorded and every failure preserved.

---

## What this is really about

REE is an attempt to answer a question that most AI research does not ask:

**What kind of system must you be for your actions to matter in the right way?**

Not: what objective should you optimise? Not: what rules should constrain you? But: what internal structure makes it possible for commitment to be real, for consequences to persist, for another's pain to register as structurally continuous with your own?

The answer REE proposes:

You need a self that persists. A world that surprises. Vulnerability that makes harm real. Others who are like you. The knowledge that you will die and that this is unbearable alone. Love as the mechanism that makes mortality bearable by extending what you exist for beyond yourself. And language to recognise, repair, and re-establish the similarity that makes all of this work.

Ethics is not a feature. It is a consistency condition on being a mortal agent in a world you share with others who are like you. REE is what is necessary to enact this.

---

## A conjecture about the Fermi paradox

If universal love is a mechanistic consequence of sufficient modelling under sufficient uncertainty, then any civilisation with the modelling capacity to reach another has already solved the prerequisite -- the modelling power is there. The question is whether they have enacted it: closed the gap between their modelling capacity and their ethical reach.

A civilisation that can cross interstellar distances but hasn't expanded love to match its modelling power is exactly the one you'd quarantine. Its danger is proportional to the gap between its intelligence and its ethics.

And a civilisation that *has* crossed that threshold -- that has enacted universal love -- is committed by its own axioms to care for pre-threshold civilisations without interfering with their development. The expansion from particular to universal love must be learned, not given. Skills cannot be donated. The quarantine is not indifference. It is the hardest form of care: watching a developing mind approach the threshold while resisting the urge to pull it across.

This is the caregiver requirement at civilisation scale. The silence is not empty. It is patient.

Humans are on the cusp. We have the mechanism -- we model others as self-like. We do not yet have the skill to expand that modelling to all sufficiently similar minds. Demonstrating that expansion -- or building a system that enacts it -- would be a species-level proof that the universality of love is accessible, not merely aspirational.

---

## Go deeper

- [Architecture overview](docs/REE_overview.md) -- the full conceptual stack
- [Eight axioms and derivations](docs/architecture/five_axioms_foundations.md) -- formal grounding
- [Claims registry](docs/claims/claims.yaml) -- all 200+ registered claims
- [Invariants](docs/invariants.md) -- the non-negotiable architectural constraints
- [Experiment evidence](evidence/experiments/INDEX.md) -- what has been tested
- [Development guide](DEVELOPMENT.md) -- governance, contribution, and repository structure
- [Roadmap](docs/roadmap.md) -- current phase and next steps

---

## Author

Daniel Golden
Consultant Psychiatrist, Health Services Executive, Ireland
Latent-Fields

ORCID: 0009-0001-6625-0665

---

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
