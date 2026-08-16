# Wilson, Takahashi, Schoenbaum & Niv 2014 -- OFC as a cognitive map of task space

## What the paper argues

That OFC's job is to say *where you are* in a task -- to compute a label for the current state, one that
folds in information the senses do not currently supply (what happened earlier, what is being held in
working memory) -- and to make that label available to reinforcement-learning machinery elsewhere in the
brain. The authors show the framework accounts for the classic OFC findings (reversal learning, delayed
alternation, extinction, devaluation) and for the more recent result that OFC lesions distort dopaminergic
firing in VTA, which is a satisfying test because it is a consequence in a structure OFC merely talks to.

## Why I pulled it for MECH-151

MECH-151 does not stand alone. It consumes a cue-indexed context vector from E1 that MECH-150 posits, and
it assumes that vector is *exported* -- projected onward to shape machinery that is not E1. If that
assumption has no biological analogue, MECH-151 is an engineering convenience dressed as a modelled
mechanism.

This paper is the cleanest statement I know that the assumption is sound. The theory's whole architecture
is compute-here, consume-there: OFC labels the state, and the label is used for learning *elsewhere*. The
VTA lesion result is what makes that more than a manner of speaking.

There is a second thing worth taking from it. Wilson et al. insist the state label must include
unobservable components -- and they insist on it because that is where the OFC-lesion phenomenology lives.
A context vector computed from the current observation alone would be a strictly weaker object. MECH-151
specifies its bias source as cue-specific and z_world-indexed, which is on the right side of that line,
but it is worth noting the requirement is not decorative: it is the part of the theory that does the
explanatory work.

## The honest limitation

The consumer, in this paper, is the reinforcement-learning system -- prediction errors, valuation. It is
not the action-specification stage. MECH-151's actual novelty is that the context vector reaches into the
affordance manifold and reweights it *before search*, and Wilson et al. say nothing about that. So what I
am banking here is the premise, not the claim.

I have tagged the entry to MECH-150 as well as MECH-151 for that reason. The state-abstraction content
belongs to MECH-150; pretending it is all MECH-151 evidence would quietly inflate the wrong claim's
literature confidence, and MECH-151 is a claim whose experimental record is thin enough that it does not
need help of that sort.

## Confidence

0.60. The paper is excellent and I have no quarrel with its source quality. The number is set by mapping
fidelity: strong evidence for the scaffolding MECH-151 rests on, weak evidence for MECH-151 itself.
