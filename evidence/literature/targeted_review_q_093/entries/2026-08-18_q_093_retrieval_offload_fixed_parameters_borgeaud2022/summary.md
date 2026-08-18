# RETRO: a fixed-size predictor that rides a growing store

Borgeaud and colleagues took an autoregressive transformer and, instead of asking it to
memorise the world in its weights, gave it a retrieval mechanism: at each chunk of input, the
model looks up similar chunks from an external corpus and conditions on what it finds. The
corpus reached two trillion tokens. The headline result is that a 7.5B-parameter RETRO model
reaches performance comparable to GPT-3 and Jurassic-1 on the Pile while using roughly 25x
fewer parameters, and — the part that matters more for us — that performance keeps improving
as the retrieval database is scaled up *with the model held fixed*.

That second fact is the reason this paper opens the Q-093 file. Q-093 asks whether REE's
organising machinery — E1, E2, E3, commitment, replay, residue, goal maintenance — can stay
roughly fixed in cost while the richness of what it organises grows. RETRO is the clearest
published demonstration that a system *can* be cut at such a seam and that the store side can
carry the growth. It is also, quietly, well-behaved on the methodological point Q-093 is most
insistent about: the comparison against GPT-3 is made at approximately matched competence on
a shared evaluation, not at unmatched competence, which is exactly the non-degeneracy
precondition the claim's `what_would_answer` demands before any efficiency comparison is
allowed to mean anything.

So why is the confidence only 0.62? Two boundaries, and I want to be blunt about both rather
than let the parameter-count headline do work it cannot do. The first is functional: RETRO's
fixed-size component is a next-token predictor. REE's fixed-size component is supposed to be a
*controller* — something that commits, replays, maintains goals across interruption, and
carries residue. The seam is topologically analogous and functionally quite different, and a
result about predictors staying small does not entail a result about controllers staying
small. The second is arithmetic: 25x fewer *parameters* is not 25x less *lifetime cost*. A
two-trillion-token index has a storage footprint and a per-query approximate-nearest-neighbour
cost, and neither appears in the headline. Q-093 defines its denominator as total lifetime
cost precisely so that this kind of accounting cannot be skipped. Read honestly, RETRO
evidences that the seam can exist and can pay; it does not evidence that the lifetime-cost
verdict goes REE's way.

There is a third caveat that is easy to miss and probably the most important for us. RETRO's
database is *static* — indexed once, never rewritten. REE's representational spaces are
learned and continually revised, so REE's analogue of "grow the database" also grows the cost
of maintaining, consolidating and re-indexing it. That term has no counterpart in this paper
at all, and it is the term where REE's replay and consolidation machinery would show up on the
wrong side of the ledger. This entry should be read alongside the Norlund et al. entry in this
same directory, which argues that even the gain RETRO does report may be substantially
lookup rather than structural reuse.
