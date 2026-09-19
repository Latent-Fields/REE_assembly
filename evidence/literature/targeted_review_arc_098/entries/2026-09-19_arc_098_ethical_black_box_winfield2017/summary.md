# Winfield & Jirotka (2017) -- The Case for an Ethical Black Box

**Claim tested:** ARC-098 (safety.autonomy_suspension_without_shame) | **Direction:** supports | **Confidence:** 0.72

## Why this entry exists

The 2026-09-19 pull for ARC-098 landed two entries and left a hole, and both of them said so. Orseau
& Armstrong covered the first conjunct -- autonomy may be suspended -- and recorded in their own
failure signatures that "an agent can be perfectly safely interruptible and still fail ARC-098 by
discarding the state that would let an operator diagnose why the interruption was warranted".
Tangney covered the third conjunct, the avoidance of global self-condemnation. The second conjunct,
*preserve evidence*, had nothing. This entry is the first of three addressing it.

## What the paper did

Winfield (Bristol Robotics Lab) and Jirotka (Oxford) argue that robots and autonomous systems should
carry the equivalent of an aircraft Flight Data Recorder, which they call an ethical black box (EBB).
The motivating case is the May 2016 fatal Tesla Autopilot crash and what they describe as a
"worrying perception that transparency is lacking in how these events are disclosed" -- system
developers speak reassuringly, and may be suspected of having an interest in the gloss.

The substantive contribution is section 4.1's outline specification. The EBB draws from all three of
a robot's major subsystems: sampled or compressed raw data (or extracted features) from the sensors,
actuator demands from the actuator system, and from the AI at minimum high-level state -- "braking",
"steering left" -- and ideally high-level goals and alerts such as "cyclist detected front left -
taking avoiding action". Everything is date-, time- and location-stamped. The stated design principle
is that from the recorded data it must be possible to reconstruct the timeline leading up to and
during an accident.

Two design commitments in that section carry the weight for our purposes. The first: "the dataflows
between robot subsystems and the EBB are one way only - the EBB must, as far as the robot is
concerned, be an entirely passive subsystem." The second, its complement and its limit: "The EBB
will of course also need to be secure and tamper-proof" -- asserted in one sentence, with no
mechanism offered.

Section 5 then argues something the technical sections do not: that the recorder is not the
explanation. "In aviation it is the investigation, not the black box data per se, which concludes
why an air accident occurred." The EBB provides "the crucial and objective timeline against which
all other witness accounts can be superposed", and the authors spend the section on the social
process -- the specialist investigation team, the manufacturer called to account, the conflicting
testimony of bystanders and forensics -- that turns a record into a finding.

## How this bears on ARC-098

The flight-recorder analogy is the paper's headline and is not the part that earns the entry. The
part that earns it is the one-way dataflow.

ARC-098's preservation conjunct has a self-referential threat model that the other two conjuncts do
not. The system whose evidence must be preserved is the system in the dangerous self-state -- which
is to say, the least trustworthy possible custodian of that evidence, at exactly the moment its
custody matters. Any design in which preservation depends on the agent continuing to choose
preservation has assumed away the problem. Winfield and Jirotka's specification does not: the agent
emits, and thereafter has no write path to what it emitted. Preservation stops being a disposition
the agent maintains and becomes a property of the wiring.

That is a genuine architectural invariant, and it is importable into V5 more or less verbatim. It
also converts a vague requirement into a checkable one -- "can the self-model reach the record?" is
a question about a diagram, not about the agent's motivations.

The paper hands REE one further specific. Discussing robots with an ethical governor, the authors
note that extending the EBB "would in principle be straightforward: the EBB would need to
additionally log the decisions made by the ethical governor". That is the direct analogue of what
ARC-098 needs: the self-state detector's firings, and the suspensions they trigger, recorded on the
same passive one-way channel as everything else. It is the right place to attach the claim's
machinery, and it is worth having a citation for the obvious answer being the correct one.

## Where the claim outruns the specification

Three gaps, in ascending order of how much they should worry us.

The tamper-resistance sentence is doing no work. One-way dataflow stops the robot's normal control
path from rewriting the log; it says nothing about a compromised agent reaching the storage some
other way, and "secure and tamper-proof" is a requirement statement, not a mechanism. This is
precisely the gap the Schneier & Kelsey entry in this directory addresses, which is why the two are
best read together.

The retention model is wrong for this claim. The worked example sizes a 1TB drive for roughly three
hours at 100MB/s and specifies that the EBB "would, like an aircraft flight data recorder,
continuously overwrite the oldest data logs, so that at any one time the EBB stores the most recent
3 hours". For an aircraft this is fine -- the flight is shorter than the window and the accident
terminates it. For a continuously-running cognitive system it is not: an episode whose onset
precedes the window is simply gone, and an agent whose subsequent activity generates volume flushes
the record of its own earlier dangerous state without ever performing an act that anyone could
identify as concealment. I want to be careful about the strength of this: it is not a claim that
such an agent would be *motivated* to flush the buffer, only that a fixed-capacity window makes
non-preservation the default outcome of ordinary operation. ARC-098 needs retention keyed to the
episode, not to wall-clock capacity.

The layer is wrong, and this is the one that matters most. The authors deliberately exclude the AI's
low-level internal decision-making from the record, reasoning that architectures differ too much --
"some may be algorithmic, others based on artificial neural networks" -- for a common specification
to be possible. That exclusion is well motivated for a portable industry standard and directly
contrary to what this claim requires. ARC-098 is about detecting a dangerous *self-state*; a
self-state is an internal variable. An EBB built exactly to this specification would faithfully
record that autonomy was suspended and what the agent did afterwards, and would not record the thing
the suspension was about.

## Limitations

This is a position paper. Nothing is proved, nothing is implemented, nothing is measured. It is
influential -- the authors and colleagues later developed the idea into a draft open standard for
social robots -- but influence is not evidence, and I have kept source_quality at 0.70 to say so.

The domain gap is real and I do not want to smooth it. The paper's setting is embodied
safety-critical robotics: physical accidents, skid marks, bystanders with phones, a statutory road
traffic investigation agency, a manufacturer that can be compelled to release training data. ARC-098
concerns an internal state in a cognitive architecture where there is no accident scene, no
third-party witness, and no investigator. The paper's own central argument in section 5 is that the
black box is made meaningful by the investigation around it -- which means REE currently has the
recorder end of that pairing conceivable and the investigation end entirely unspecified. That is not
a reason to discount the entry; it is a finding about ARC-098 that this paper is what surfaces. The
claim's third conjunct, *seek correction*, presupposes something to seek correction from, and
nothing in REE names it.

## Confidence reasoning

Source quality 0.70 -- respectable venue, central authors, no result. Mapping fidelity 0.82, the
highest component here and the highest in this directory: the paper's subject is an artificial
autonomous system's obligation to preserve a diagnosable record of its own behaviour for post-hoc
investigation, which is ARC-098's second conjunct with almost no translation required, and the
one-way-dataflow requirement matches the conjunct's adversarial structure exactly. Docked for the
low-level-state exclusion. Transfer risk 0.32 -- no species or population inference, but a real gap
from physical-accident settings with statutory investigators to an internal self-state with neither.

Aggregate 0.72, above the components' mean because ARC-098 is an `architectural_commitment` and
mapping fidelity is weighted accordingly; below Orseau & Armstrong's 0.74 because that entry has a
theorem and this one has a diagram.
