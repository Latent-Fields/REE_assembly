# Toward ethical cognitive architectures for the development of artificial moral agents (Cervantes, López & Cervantes, 2020)

## What the paper did

This is a review and position paper rather than a study. Cervantes, López and Cervantes take
the major general cognitive architectures -- Soar, LIDA, ACT-R, iCub -- several of which are
explicitly offered as foundations for artificial general intelligence, and ask what would have
to be added to them for an agent built on one to be a genuine moral agent rather than a system
that follows moral rules. Their answer is framed as a set of open challenges: what mechanisms
must an artificial agent have in order to make moral decisions, and where in the architecture
do those mechanisms belong.

## Key findings relevant to ARC-043

The review's structural position is the relevant content, and it lands on ARC-043's two central
commitments independently.

First, on modularity. The authors argue that ethical reasoning should be woven into
architecture design rather than bolted on -- that "developing a computational model of human
beings' ethical decision-making is an essential cognitive function to achieve both a truly
human-like intelligence in cognitive architectures and an AGI model of human cognition." Ethics
is presented as core to the architecture, not as a governor sitting on top of it filtering
outputs. This is the same position REE holds under INV-001: no explicit ethics module.

Second, on ordering. The review identifies layered prerequisites for moral agency: foundational
cognitive functions (perception, world modelling), then social-cognitive capacities -- "social
cognition, mental state, and reasoning", including the ability to think about the contents of
someone else's mind and to "step into the other's shoes" -- then moral-emotion mechanisms, with
anticipated moral emotions such as pride and guilt acting as "a moral regulator of the ethical
decision-making process", and moral judgment emerging from the integration of these layers
rather than from a rule set. Alongside these it stipulates autonomy and a motivational system.

## How this translates to REE

ARC-043 orders the ethical stack as five axiom layers (epistemic ground, existence, other minds,
shared world, love/shared valence), then ethics derived from them at Layer 5, then REE as the
decision system at Layer 6, then the action-consequence-learning closure at Layers 7-9. The
review's sequence -- world model, then theory of mind, then affective regulation, then moral
judgment -- maps recognisably onto ARC-043's Layers 1/3, then Layer 2, then Layer 4, then Layer 5.
That two independent efforts, one of which had no exposure to REE, arrive at a similar middle
section of the stack is the kind of convergence that should modestly raise credence in the
ordering, particularly since the convergence is on the *derivation* structure and not merely on
a list of ingredients.

It is also worth noting what this entry contributes that the other two ARC-043 entries do not:
it is the only one for which the domains match natively. Young et al. requires a
human-neuroscience-to-artificial-architecture transfer, and Hesp et al. is a simulation of a
rodent task; this paper is already reasoning about the architecture of artificial moral agents,
which is precisely what ARC-043 is a claim about.

## Limitations and caveats

The obvious one, and it should not be softened: this is an argument, not a result. The review's
own conclusion is that ethical cognitive architectures constitute a set of unsolved challenges,
and it reports that none of the architectures it surveys actually implements the layering it
proposes. So we have two proposals -- ARC-043 and this one -- that agree with each other, and
neither is independently confirmed by anything. Two architects agreeing on a blueprint is
weaker evidence than it feels like, and the feeling of corroboration is exactly the thing to
distrust here.

The alignment is also only partial. The review bottoms out at perception and world modelling;
it posits nothing answering to ARC-043's Layer 0 (epistemic ground) or Layer 1 (existence), so
the two orderings agree on direction but not on what sits at the foundation. And it is silent
on ARC-043's entire upper half -- Layer 6, REE as the decision system implementing ethics under
uncertainty, and Layers 7-9 closing the action-consequence-learning loop. Across all three
entries in this pull, that upper half remains untouched, which is itself the more useful finding.

## Confidence reasoning

Confidence 0.62. Mapping fidelity is the highest of the ARC-043 set at 0.75, because unlike the
other two entries this source is arguing about layer ordering *directly*, which is what the
claim asserts. Transfer risk is correspondingly the lowest at 0.30 -- no cross-domain leap is
required. Source quality is the constraint at 0.60: peer-reviewed in Cognitive Systems Research,
but non-empirical. The result is an entry that raises credence in ARC-043's ordering without
being able to test it, and which sharpens where the claim is currently unsupported: the axioms
below other-minds, and everything above ethics.
