# Lai, Huang & Gershman 2025 -- chunking as a resource-rational compression of policy

This paper asks why chunking happens at all, which is a question ARC-069 has so far answered by
gesturing at combinatorial cost. Lai and colleagues build a model in which chunking falls out of
optimising a trade-off between reward and *conditional policy complexity*: when the environment has
temporal structure that action selection can exploit, binding actions together compresses the policy
and reduces the memory needed to encode it. They then confirm the model's predictions behaviourally
-- chunking lowers conditional policy complexity and reaction times, chunking increases as working
memory load rises, and chunking in turn frees working memory for other information.

The useful thing this does for us is supply a *trigger* for the composition leg, and it is not the
trigger ARC-071 currently proposes. ARC-071 says composition fires on repetition count plus outcome
consistency. Lai et al. suggest the variable actually doing the work is compressibility under a
binding resource constraint, and that repetition is only a proxy for it. Those come apart in cases
we should care about: a sub-sequence can be repeated many times with consistent outcomes and still
be worthless to compress if the environment offers no temporal structure for selection to exploit,
and conversely a rarely-visited but highly predictable sub-sequence is exactly what compression
theory says to chunk first. If that is right, the accumulator design implied by ARC-071 would chunk
the wrong things -- and it would do so quietly, since a repetition-triggered accumulator always has
something to fire on.

There is a currency problem I do not want to paper over. The constraint Lai et al. optimise against
is a capacity limit on policy *storage* -- working memory. ARC-069's motivating cost is the
combinatorial expense of *searching* at fine grain during rollout. These are not the same quantity,
and they can diverge: a policy that is cheap to store may still be expensive to search over, and
compressing on a storage criterion could compress precisely the sequences whose rollout cost was
never the problem. Whether the two coincide in REE's substrate is an empirical question nobody has
asked, and it should probably be asked before an ARC-071 mechanism is built on a compression
rationale.

The paper is also silent on decomposition, and the silence is not neutral. A pure policy-compression
account predicts chunks *persist* for as long as the environment stays compressible; it supplies no
pressure that would re-decompose a chunk when its predicted outcome fails to ground. ARC-070 needs
some other principle. That the cleanest normative account of composition has nothing to say about
decomposition is itself mild support for ARC-069's two-slots-not-one structure, arriving from the
computational side to meet Jin et al. arriving from the neural side.

Confidence 0.72. Source quality 0.82 -- Cognition, a clean theory-plus-confirmation structure, but
a 2025 paper with no independent replication yet. Mapping fidelity 0.72, held there by the cost-
currency mismatch rather than by anything wrong with the paper. Transfer risk is comparatively low
at 0.30, since this is already a computational account of an agent-shaped problem.
