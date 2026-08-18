# The offload dividend may be lookup: overlap explains much of RETRO's gain

Norlund, Doostmohammadi, Johansson and Kuhlmann went back to the RETRO result and asked the
uncomfortable question: when a retrieval-enhanced model beats a much larger non-retrieval one,
what is actually doing the work? The suggestion in the original literature was that the gain
reflects non-trivial generalisation arising from the *combination* of model weights and
retrieved context. Their finding is that the gains largely originate from overlapping tokens
between the retrieval database and the test data — that is, considerably less non-trivial
generalisation than had been assumed. They also note something with wider reach: even limited
token overlap can markedly reduce test-time loss, which makes generalisation in
retrieval-augmented models genuinely hard to evaluate at all.

This is the adversarial reading of the best supporting entry in this pull, and it should be
read against it directly. Q-093's confirming direction depends on a specific mechanism: that
persistent acquired structure *persists and is reused*, so competence does not have to be
reconstructed in context each time. If, in the flagship demonstration of memory offload, much
of the measured benefit turns out to be surface overlap between the store and the test set,
then the RAG literature is a weaker warrant for that mechanism than it first appears. This is
the memory-augmented analogue of evaluating on the training set, and it is exactly the failure
mode a system with large persistent stores is most exposed to.

The practical consequence for Q-093 is a design requirement rather than a verdict. Any REE
efficiency dividend has to be demonstrated on evaluation content that is not already resident
in z_world, episodic memory or the semantic structures — and the residual overlap has to be
*measured*, not assumed away. The paper's second finding makes this harder than it sounds: if
even limited overlap moves the loss substantially, an overlap control cannot be a binary
contamination check. It has to be graded, and a REE result reported without a graded overlap
measure is uninterpretable in this respect.

The honest limitation is that the paper identifies a confound Q-093 must control without
supplying the instrument to control it. "Token overlap" has a crisp operational definition in
text retrieval. REE's persistent state is a learned latent field plus episodic and semantic
structures, and no equivalent overlap metric exists for it. Constructing one is unbuilt work,
and it is now a visible precondition on any valid test of this claim. I have set confidence at
0.60: the reproduction is at smaller scale than the system it critiques and reports a
contribution analysis rather than a clean causal decomposition, so it establishes that overlap
explains much of the gain without pinning down how much would survive without it. That is
enough to weaken, not enough to refute.
