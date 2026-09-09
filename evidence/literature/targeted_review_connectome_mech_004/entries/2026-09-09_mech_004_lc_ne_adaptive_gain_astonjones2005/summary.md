# Aston-Jones & Cohen (2005), "An integrative theory of locus coeruleus-norepinephrine function: adaptive gain and optimal performance"

**Claim tested:** MECH-004 (control-plane signal-to-knob wiring map)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

Aston-Jones and Cohen assemble two decades of locus coeruleus recording -- much of it their own,
in behaving macaques and rodents performing vigilance and signal-detection tasks -- into a single
functional account. The organising observation is that LC has two modes rather than a single
activity level, and that the modes are distinguished by *timescale structure*, not by which cells
fire. In phasic mode, tonic firing sits at a moderate level and task-relevant decision outcomes
elicit brief bursts; target neurons get a transient gain boost, and the animal performs the
current task well. In tonic mode, baseline firing rises, the phasic bursts disappear, performance
on the current task degrades, and behaviour becomes distractible -- the animal samples
alternatives. They propose that this is adaptive: LC implements a gain parameter, and switching
modes is how the system trades exploitation against exploration. The switch itself is driven from
outside, by anterior cingulate and orbitofrontal assessment of how well the current task is paying.

## What it says about MECH-004

Three things, of decreasing comfort.

The first is a straightforward endorsement of the tonic/phasic decomposition inside S4. The map
splits its safety signal into a tonic baseline component ("whether core viability is within
bounds") and a phasic volatility component ("how rapidly safety is changing"), and routes them to
different knobs -- baseline to K7, volatility to K8. Adaptive gain theory is a worked instance of
precisely that architecture, in a real nucleus, where the two signals are distinguished by
timescale rather than by carrying different content. That is a non-obvious design choice and it
is good to find it independently instantiated.

The second is that the map's tier assignment is right. MECH-004 sorts its modulators into
stream-specific precision planes, loop-specific planes, and global modulators, and puts the
NE-like axis in the global tier. LC's projections are famously diffuse, and its gain change is
correspondingly non-selective. Placing it globally is a fact about the anatomy, not a
convenience.

The third is the most useful and the most double-edged. The map asserts a route from S4 through
K7 to K4 -- arousal baseline shaping exploration pressure -- without saying how one becomes the
other. Adaptive gain theory supplies the mechanism, and the mechanism is that they are not really
two things. They are two readings of one underlying regime setting. That explains the route, and
in doing so it undercuts the framing.

## Limitations and caveats

MECH-004 presents ten knobs as a list of meta-parameters, and lists K4, K7 and K8 among them
without specifying any coupling between them. Adaptive gain theory is a one-variable account:
move LC mode and arousal baseline, exploration pressure and interrupt bias all move together, in
a fixed relationship. A control plane built literally to the map can therefore be commanded into
states this account says are not reachable -- high arousal baseline together with low exploration
pressure and intact phasic responsiveness, say -- and nothing in the map would flag it. If one is
going to cite this paper in support of K4/K7/K8, the honest form of the citation is that it
supports the *couplings* and mildly embarrasses the *enumeration*.

Two smaller cautions. Tonic-mode "exploration" is, in the data, distractibility and degraded
performance; the map's language of exploration as adaptive widening of search imports an
optimism the phenomenon does not carry. And the utility signal driving mode switching comes from
ACC and OFC evaluating *task payoff*. Nothing here evaluates provenance, authority or identity
continuity, so this paper offers no support at all for S5, the reality-coherence channel that is
MECH-004's most distinctive and least evidenced component. A related gap: because LC gain is
global, it cannot be the mechanism that implements the stream-specific precision planes
(Pi_ext, Pi_int, Pi_prop, Pi_noc) the map also requires. Something else has to, and the map does
not say what.

## Confidence reasoning

0.72. Source quality 0.85 -- canonical, heavily replicated, in a serious review venue, grounded
in the authors' own primate work, discounted only because it is synthesis-plus-modelling rather
than new measurement. Mapping fidelity 0.65, the second-lowest in this pull, because the paper
supports and corrects the claim in the same breath: the phenomena map cleanly onto three named
knobs while the paper's one-variable structure argues those knobs are not independent. Transfer
risk 0.35 for the animal-to-artificial-agent step on what is in part an anatomical claim about a
particular nucleus.
