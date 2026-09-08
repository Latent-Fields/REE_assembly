# TMS to RTPJ reduces the role of beliefs in moral judgment (Young, Camprodon, Hauser, Pascual-Leone & Saxe, 2010)

## What the paper did

Young and colleagues asked whether the right temporoparietal junction -- the region most
reliably implicated in reasoning about other people's mental states -- is *necessary* for
moral judgment, rather than merely active during it. The distinction matters: fMRI can tell
you that a region participates, but only a causal intervention can tell you that the
downstream function depends on it. They used transcranial magnetic stimulation to disrupt
RTPJ activity in two experiments: offline (1 Hz for 25 minutes, before the task, n=8) and
online (10 Hz for 500 ms, concurrent with the judgment question, n=12). The RTPJ target was
localised per participant by fMRI; the control site sat 5 cm posterior on the axial plane.

Participants judged moral vignettes in a 2x2 design crossing the actor's *belief* (negative or
neutral) with the *outcome* (negative or neutral), yielding four cells: intentional harm
(bad belief, bad outcome), attempted harm (bad belief, neutral outcome), accidental harm
(neutral belief, bad outcome), and non-harm. The attempted-harm and accidental-harm cells are
where belief and outcome dissociate, so they are the diagnostic conditions: an observer who
cannot use mental states must fall back on outcomes.

## Key findings relevant to ARC-043

That is what happened. In both experiments, RTPJ stimulation caused participants to rely less
on the actor's mental states. The effect was clearest for attempted harms -- an actor who
intended harm but failed -- which participants judged as *more* morally permissible after RTPJ
TMS than after control-site TMS (experiment 1: t(59)=2.28, p=0.03; experiment 2: t(81)=2.11,
p=0.038; combined t(87)=3.6, p=0.001). The accidental-harm cell shifted in the predicted
direction (toward more forbidden) but did not reach independent significance in item analyses,
though the belief-by-TMS interaction was robust across both experiments (F(1,12)=7.6, p=0.017).

The shape of the deficit is the interesting part. Moral judgment was not abolished; it
*regressed* to outcome-based evaluation. Degrade the capacity to represent what was in the
other agent's mind, and what remains is a judgment about what happened.

## How this translates to REE

ARC-043 commits to an ordering: Layers 0-4 are the axioms (epistemic ground, existence, other
minds, shared world, love/shared valence), Layer 5 is ethics *derived from* those axioms, Layer 6
is REE as the decision system implementing ethics under uncertainty, Layers 7-9 close the
action-consequence-learning loop. This paper bears on exactly one edge of that graph: other
minds (Layer 2) sitting beneath ethics (Layer 5). And it bears on it causally, which is what an
ordering claim needs -- correlational co-activation would be compatible with the reverse
dependency or with a common cause. Here the manipulation is upstream and the degradation is
downstream, in the direction ARC-043 predicts.

The regression-to-outcome pattern is a further small confirmation of the layer picture, because
it is what you would expect if ethics is *computed over* mental-state representations rather
than being an independent module that merely consults them. Remove the input and the
computation does not fail; it produces the answer it can produce from what remains.

## Limitations and caveats

I want to be careful not to let one edge stand in for the whole stack. ARC-043 asserts a
nine-layer ordering and this paper licenses a single dependency within it. It says nothing
about the epistemic ground, existence, shared world or shared-valence layers, nothing about
their relative order, and nothing about Layers 6-9 -- the decision system and the
action-consequence-learning closure, which is arguably the more contentious half of the claim.

There is also a category question that no amount of neuroscience settles. ARC-043 is an
*architectural commitment* about how REE is organised. Showing that the human brain implements
moral judgment atop mental-state inference establishes that this is one workable architecture,
not that it is the necessary one. REE's brain-like-construction principle is what licenses
treating biological organisation as design evidence at all, and that principle is a stance, not
a finding.

Two narrower caveats: n=20 across both experiments is small even for a within-subject TMS
design, and the accidental-harm arm did not independently reach significance, so the causal
conclusion leans on attempted harm. And because a virtual lesion degrades rather than abolishes,
what is evidenced is a graded dependency -- moral judgment gets worse without other-minds
inference -- not the strict layer dependency that "Layer 5 is derived from Layers 0-4" might be
read to assert.

## Confidence reasoning

Confidence 0.70. Source quality 0.82: PNAS, causal intervention, replicated across two
stimulation protocols within the paper, individually fMRI-localised targets and a real control
site -- discounted for the small sample and the one arm that fell short. Mapping fidelity 0.70,
capped hard by the one-edge-of-nine problem. Transfer risk 0.35, which is the ordinary
human-neuroscience-to-artificial-architecture leap REE takes as a matter of policy rather than
an unusual stretch. The net position: ARC-043's Layer 2 -> Layer 5 edge has genuine causal
support; the rest of the stack ordering remains, as far as this pull found, unevidenced.
