# Place field assembly distribution encodes preferred locations (Mamad et al., 2017, PLoS Biology)

## What the paper did

Mamad and colleagues recorded CA1 place cells in rats learning a reward-driven place preference, and combined that with optogenetic manipulation of ventral tegmental area dopaminergic neurons. The question was whether the hippocampal map merely reports where the animal is, or whether it also stores what the animal has learned about the value of being there.

## Key findings relevant to the claim

Place fields clustered toward rewarded locations, and -- this is the part that carries the argument -- the degree of clustering correlated with the animal's behavioural navigation preference. The stronger the preference, the more the map had reorganised around it. The optogenetic arm then converted the correlation into a mechanism: VTA dopaminergic activity directed the experience-dependent redistribution of fields. The authors' own conclusion is unambiguous, and it is the direct negation of MECH-143 as written: hippocampal neurons are not merely mapping a static environment, they also store the concurrent context reward value.

## How this translates to REE

If the dorsal map's field *distribution* is shaped by value, then the residue-field terrain R(x,t) that ARC-007's trajectory proposal module reads is not a value-neutral substrate handed to it from somewhere else. Value has already been written into the geometry, and written by an identifiable teaching signal.

It is worth being precise about what this does and does not break. ARC-007's letter survives: the proposer can still compute no *new* value at plan time, because the value is already baked into the terrain it navigates. What takes damage is the framing -- the picture of a value-free map plus a pure navigator. The more defensible picture is a value-shaped map plus a navigator that does no further value work. That is a meaningfully different architecture, and it relocates the question from "does the proposer compute value?" to "when and how does value get written into the terrain?", which the V3 substrate currently has no mechanism for at all.

## Limitations and caveats

The critical caveat, and the one easiest to lose: this manipulation varies where reward *is*, not what a fixed goal is *worth*. Duvelle et al.'s value-at-constant-location null and this result are not in contradiction -- a map can be insensitive to the value of a fixed goal while still being reorganised by learning where goals are. Anyone citing this as a straight refutation of MECH-143 has skipped a step. I have held mapping_fidelity at 0.55 to mark exactly that gap.

Beyond that: rat tetrode data, no analogue of a planning module is tested, and the dopaminergic write mechanism has no counterpart in the V3 substrate, so the causal half of the paper is currently unactionable for us even though it is the strongest half scientifically.

## Confidence reasoning

0.60. Source quality is high (0.80) -- peer-reviewed, causal, well-powered. Mapping fidelity is the limiting term (0.55) for the reason above. Direction is **weakens** rather than mixed: unlike Masala et al., this paper offers nothing that supports the value-free reading, and its authors state the opposing conclusion outright.
