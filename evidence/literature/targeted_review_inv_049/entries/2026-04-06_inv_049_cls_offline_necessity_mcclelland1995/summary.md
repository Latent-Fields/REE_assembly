# McClelland, McNaughton & O'Reilly (1995) — Complementary Learning Systems

**Claim tested:** INV-049 — offline update phases are a general computational necessity for model-building agents, not a biological contingency.

## The Problem They Set Out to Explain

McClelland, McNaughton, and O'Reilly opened with a puzzle that should interest anyone building learning systems: connectionist networks trained sequentially on successive tasks suffer catastrophic interference -- new learning does not merely displace old knowledge gradually, it erases it almost completely. The problem is structural. Distributed representations share weights across tasks; gradient updates to accommodate new inputs shift those weights in ways that obliterate old patterns. If you want to know why brains have hippocampi, this paper is where to start.

## The Computational Argument

The core theorem, though the authors did not formalize it as such, is this: any system that (a) learns by updating shared distributed parameters and (b) encounters novel inputs sequentially will suffer catastrophic interference unless it interleaves training across old and new examples. Pure online learning -- updating only on what is currently in front of the system -- is provably self-defeating over time for such systems. The solution is interleaved learning: mixing old episodes back into the training stream alongside new ones. This requires, at minimum, a mechanism for storing episodes separately from the main parameter store, and a process for replaying them.

## The Biological Mapping

McClelland et al. proposed that the mammalian brain implements this solution architecturally. The hippocampus acts as a fast, sparse, pattern-separated memory that can encode new episodes without immediately updating the slowly-learning neocortex. During sleep (and rest), hippocampal replay drives neocortical consolidation through interleaved experience, allowing the neocortex to gradually integrate new knowledge without catastrophic disruption of existing representations. Sleep is, on this view, the computational mechanism by which the brain runs its offline update phase -- not because biology found a convenient window, but because the mathematics demands it.

## Relevance to INV-049

This paper directly grounds INV-049's claim of general computational necessity. INV-049 asserts that any agent building a world model from experience cannot safely update that model while using it for online navigation, and must therefore have periodic offline phases of model reorganisation. McClelland et al. provide the formal basis for the first half of this claim: sequential online updating of a distributed model is self-defeating. The biological framing adds texture but is not required for the abstract argument. The honest caveat is scope: the catastrophic interference proof is sharpest for gradient-descent systems with distributed representations. Whether it extends with equal force to all possible model-building architectures -- Bayesian updaters, symbolic planners, hybrid systems -- is not addressed here. INV-049 claims universality; this paper establishes the claim for the class of architectures REE actually uses.

## Notes on Confidence

The mapping fidelity is high. The source quality is essentially maximal -- this is one of the most-cited theoretical papers in cognitive neuroscience, and its core computational argument has been independently confirmed many times over in the continual learning literature. The mild discount on confidence is for the universality claim in INV-049: the paper does not purport to cover all learning architectures, and neither should we claim it does.
