# Berridge & Robinson (2016) -- Liking, wanting, and the incentive-sensitization theory of addiction

**Claim tested:** ARC-095 (affect.open_extensible_stream_taxonomy) | **Direction:** supports | **Confidence:** 0.80

## What the paper did

Berridge and Robinson's invited American Psychologist review consolidates roughly two decades of
work establishing that reward is not one thing. Incentive salience -- "wanting" -- is mesolimbic
dopamine-dependent, sensitizable, persistent, and can be driven without any accompanying pleasure.
Hedonic impact -- "liking" -- is mediated by a comparatively fragile and anatomically restricted set
of opioid and endocannabinoid hotspots, and does not sensitize with repeated drug exposure. The two
are doubly dissociable: you can manipulate one and leave the other intact.

Applied to addiction, this yields the incentive-sensitization account: repeated drug exposure
sensitizes the wanting system while liking stays flat or declines, producing compulsive pursuit of a
reward the agent no longer enjoys. Whatever one makes of that clinical theory -- and it is contested
-- the underlying dissociation is among the better-replicated findings in affective neuroscience.

## Why this is the strongest entry in the ARC-095 pull

The Lindquist meta-analysis argues that a frozen taxonomy is unsupported. This paper does something
more useful for a design commitment: it shows the actual cost of freezing, by documenting a worked
instance of the exact operation ARC-095 reserves. The field had a single handle called "reward". It
looked primitive. It was not: it had to become two, and the two behave so differently that keeping
them merged makes an entire class of pathology *inexpressible*.

That last point is the one I would carry into the V5 design. A REE register that had frozen "reward"
as a single handle would not merely have been imprecise about incentive-sensitization -- it would
have been unable to represent it at all, because the pathology just is a growing divergence between
wanting and liking. A schema with one handle for both has no vocabulary for the gap. You cannot
detect a failure your representation cannot express, which means the freeze does not simply degrade
resolution; it creates a permanent blind spot whose existence is invisible from inside the scheme.

And the correction took twenty years to arrive. That is the argument for keeping split/merge
available rather than for getting the carve right up front: the corrective evidence arrives long
after the ontology has to be committed. The same reasoning turns back on ARC-095's own list.
Liking and wanting appear there correctly separated -- REE has the benefit of hindsight. But
"suffering", "threat" and "frustration" are exactly the sort of coarse folk groupings that the
liking/wanting history suggests may themselves fracture once a substrate generates real data.

There is also an implementation-level lesson worth recording: the split mattered because the two
components have different *dynamics* -- different neurochemistry, different sensitization
behaviour, different time courses. So the split/merge permission ARC-095 reserves has to extend to
the machinery that updates each handle, not merely to the label attached to it. A register that
lets you rename a handle but not re-plumb its update rule has not really preserved the operation.

## Limitations

The dissociation is established primarily in rodents, via taste-reactivity paradigms and targeted
dopamine and opioid manipulations. Human evidence is more indirect, and the translation of "wanting"
to human craving remains contested, as does incentive-sensitization as a complete account of
addiction. This is also a review rather than a primary report.

The more important caveat is about what a single precedent can prove. This paper shows that *one*
historical taxonomy needed splitting. That supports keeping the operation available. It does not
establish how often splits are needed, when a register is mature enough to close, or that REE's
particular handles will fracture the same way. Leaning on one vivid case to justify permanent
extensibility is an availability argument unless it is paired with an account of what openness
itself costs -- and neither this paper nor ARC-098's sibling claim supplies that. If I were
stress-testing ARC-095, that is where I would press: the claim asserts a benefit of openness and is
silent on its price.

## Confidence reasoning

Mapping fidelity is unusually high for an architectural claim (0.84) because the paper *instantiates*
the operation ARC-095 reserves rather than merely bearing on it thematically, and I have weighted it
accordingly. Source quality is strong (0.88) but capped below a primary report -- review format, and
a contested surrounding framework even though the core dissociation is not contested. Transfer risk
is moderate-low (0.28): rodent-to-human is the paper's own weak seam, but the architectural lesson
that handles fracture under evidence transfers independently of whether incentive-sensitization is
the right theory of addiction. Aggregate 0.80.
