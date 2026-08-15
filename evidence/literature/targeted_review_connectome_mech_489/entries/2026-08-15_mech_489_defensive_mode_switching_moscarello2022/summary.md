# The central nucleus of the amygdala and the construction of defensive modes across the threat-imminence continuum

Moscarello & Penzo (2022), *Nature Neuroscience* 25(8):999-1008. DOI 10.1038/s41593-022-01130-5. PMID 35915178.

## What the paper argues

This is a perspective rather than a primary report, and its value is in the organising proposal. The authors argue that the varied defensive behaviours seen in rodent laboratory paradigms -- freezing, avoidance, flight, risk assessment -- are not a grab-bag of separate reflexes but a set of discrete *modes*, arranged along a continuum of threat imminence and constructed by the central nucleus of the amygdala. The mechanism they propose for moving between them is mutually inhibitory circuitry operating a winner-takes-all strategy: modes compete, one wins, and transitions between defensive responses are transitions in which circuit element currently has the upper hand.

Two things follow that are worth holding onto. Defensive action selection is *selection* -- discrete, competitive, mutually exclusive -- rather than a continuous blend. And which mode wins is organised by imminence, learned through association with experience, rather than by the raw intensity of the eliciting stimulus.

## Why this bears on MECH-489

MECH-489's Components 4 and 5 take a post-arrest decision and resolve it into one of approach, withdraw or resume, by comparing a harm channel against a benefit channel. Two features of the claim get support here.

First, the shape of the decision. A substrate that resolves to one of a small set of mutually exclusive behavioural modes is architecturally in the right family. This is not a trivial endorsement -- one could imagine defensive responding as a graded intensity dial, and REE's design instead commits to discrete outcomes. The biology, on this account, does the same thing, and does it by mutual inhibition.

Second, the boundary against MECH-279. MECH-489 is registered as a phasic arrest triggered by something unexpected being noticed; MECH-279 is a chronic freeze responding to accumulated suffering. `claims.yaml` distinguishes them explicitly, and the V3-EXQ-910a autopsy examined that boundary and concluded it was scientifically sound and should not be redrawn. This paper is independent support for that judgement: states at different points on the imminence continuum are built by different circuit configurations, which is exactly what two separate mechanism claims would predict. It is reassuring when a boundary drawn on internal-consistency grounds turns out to also be the boundary the biology draws.

There is also a more pointed observation available. If defensive mode selection is winner-takes-all competition, then a decision layer that resolves to the *same* mode on every override event is not exhibiting selection at all -- it is exhibiting a competition with a structurally biased input. That is precisely what the V3-EXQ-910 autopsy diagnosed as a code-level scale-mismatch bug producing a 0/0/206 approach/resume/withdraw split. I note the convergence but want to be careful with it: the autopsy established that finding from the code, on experimental evidence, and it stands on its own. This paper does not add weight to it. What it adds is a reason to think the fix matters architecturally rather than cosmetically -- degenerate winner-takes-all output is a signature the biology says should not occur.

## Limitations

The organising variable does not transfer, and this is the main caveat. The biology arranges defensive modes by *threat imminence* -- how near the threat is in space and time -- learned associatively over experience. MECH-489 gates on an instantaneous onset derivative and then compares harm against benefit at the current location. REE has no imminence representation at all. So what transfers is the competitive-selection architecture; the variable that drives the competition does not, and anyone reading this entry as "REE's harm-versus-benefit comparison is biologically validated" would be over-reading it substantially.

It is also a review. The winner-takes-all proposal is the authors' synthesis of a literature rather than a single decisive experiment, and it inherits whatever remains unsettled in that literature. And it is rodent throughout.

## Confidence

0.70. Source quality 0.90 -- Nature Neuroscience, established investigators, a large and reasonably convergent underlying literature. Mapping fidelity 0.62, held down by the imminence mismatch. Transfer risk 0.35, which is lower than the rodent-to-agent gap might suggest, on the grounds that a computational strategy like mutual inhibition transfers across substrates more readily than anatomy does -- that is a judgement call and I would not defend it strongly.
