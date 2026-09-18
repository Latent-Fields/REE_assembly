# Taylor et al. (2022) -- Structural connections between the noradrenergic and cholinergic system shape the dynamics of functional brain networks

*NeuroImage 260:119455 -- doi:10.1016/j.neuroimage.2022.119455 -- PMID 35809888*

## The part of the claim this entry is for

MECH-039 carries a precondition before either of its signatures can be read at all. The named control channels must be independently measurable and show non-zero cross-condition variance, because -- in the claim's own words -- "a run where all channels move in lockstep cannot discriminate 'stable region in a continuous space' from 'discrete module'." That precondition is the part of the claim most likely to be violated silently in a REE run, and nothing else in this pull addresses it head-on. This paper does.

## What it found

The authors estimated white-matter connectivity between the two neuromodulatory hubs REE models most directly -- the locus coeruleus and the nucleus basalis of Meynert -- and related that structural measure to resting-state functional dynamics across individuals. Two results. First, a significant positive relationship between LC-nbM white-matter strength and the extent of network-level integration following BOLD peaks in LC *relative to* nbM activity. Second, individuals with denser interconnecting streamlines showed "a heightened ability to shift to novel brain states". The framing is that "the underlying static features of the neuromodulatory hubs can impose some constraints on the dynamic features of the brain", and that the two systems should be understood as anatomically interconnected rather than studied in isolation.

## Reading it for and against

*For* non-degeneracy: the two channels are separately identifiable and produce dissociable dynamic signatures. The integration measure keys on their *relative* timing, which only means anything if they are not the same quantity. Taken with Munn et al. 2021 -- where LC and BNM bursts move the energy landscape in opposite directions -- there is a reasonable case that the biological analogues of REE's arousal and precision channels are genuinely two things.

*Against*, or at least complicating: the paper's headline is that they are **coupled**, structurally and consequentially, and that the *degree* of coupling is what predicts flexibility. So the picture is neither independence nor redundancy but partial coupling. That is exactly the regime where MECH-039's precondition degrades gracefully and quietly rather than failing loudly. A fully lockstep run would be obvious. A run with cross-channel correlation at 0.7 would not be, and it would leave the joint channel space at materially lower effective dimensionality than the channel count -- which is enough to blur the distinction the claim is trying to draw, without anything in the output looking wrong. The operational consequence: any experiment reporting a MECH-039 verdict should report a measured cross-channel variance and correlation structure alongside it, as a precondition check rather than an afterthought.

## The asymmetry that limits how much this licenses

There is a structural problem with transferring this to REE, and it cuts against the claim rather than for it. REE's control plane exposes its channels as separately writable scalars. They are independent *by construction*. So the substrate cannot really fail the non-degeneracy precondition the way biology might -- it can only fail it by accident of a particular policy driving them together. That makes a REE confirmation of MECH-039 a weaker result than it would be in a system where the channels were emergent and had to earn their separability. This is worth stating explicitly in any experiment that cites this entry: the biology says these channels are interactive components, REE has decided to model them as independent axes, and a confirmation obtained in the easier setting should not be read back onto the harder one.

## Method cautions

Tractography between the LC and the nbM asks diffusion MRI to resolve a pathway between two structures each at or below its effective resolution, in a region dense with crossing fibres -- conditions under which false-positive streamlines are well documented. A spurious streamline count correlated with head motion, age or overall white-matter integrity would reproduce this individual-differences result with no underlying connection. The design is also purely correlational: nothing is manipulated, so "structure constrains dynamics" is an interpretation of a cross-sectional association, and the same third factor could drive both sides of it. And the transfer is from a between-subject correlation to a within-run dynamical property; the paper gives no evidence that this coupling structure holds moment to moment within an individual, which is the timescale MECH-039 actually concerns.

Confidence 0.55, direction `mixed`. Source quality 0.72 -- established lab, careful analysis, but a hard measurement with known failure modes and no manipulation. Mapping fidelity 0.60: it speaks directly to channel separability, which is what the precondition needs, but via structural connectivity and individual differences rather than by measuring channel values over time. Transfer risk 0.45, covering both the cross-sectional-to-within-run gap and the by-construction asymmetry above.
