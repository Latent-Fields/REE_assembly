# Neunuebel & Knierim (2014) -- CA3 completes coherent representations from degraded input

Neunuebel and Knierim recorded simultaneously from dentate gyrus and CA3 in behaving rats while
placing local and global spatial reference frames in conflict, and showed something the field had
long predicted but not directly measured: CA3's population output was closer to the originally stored
representation than its own dentate gyrus input was. The input had been severely disrupted -- that is
the dentate gyrus doing pattern separation -- and CA3 nonetheless produced a coherent response, which
is pattern completion. Two complementary operations, measured in the same animals at the same time,
with the degradation of the input quantified rather than assumed.

Of the four entries in this pull, this is the only one that speaks to INV-040's mechanism rather than
its behavioural signature, and that is why it carries the highest confidence. Strip INV-040 of its
domain vocabulary and what remains is a claim about content-addressable retrieval: a partial cue
indexes a stored association, and the retrieved content configures downstream weighting. In REE that
is E1's ContextMemory query, keyed on `z_world` alone rather than on full state, feeding
`cue_terrain_proj` and thence E3's terrain weighting. Neunuebel and Knierim establish that the
retrieval operation INV-040 leans on is real and quantitatively demonstrable. That is what makes "the
full accumulation of z_harm_a is not required" architecturally coherent rather than merely
convenient -- there is a known circuit that does exactly this.

The finding that should change how INV-040 is tested, though, is the other half of the paper.
Completion is only cue-*specific* to the extent that the stored patterns were separated first. That
is not an incidental framing choice; it is the design of the experiment, which turns on CA3
completing while its dentate gyrus input is disrupted. A memory bank whose stored entries are
mutually near-identical will return the same output whatever the cue, and any downstream weighting
computed from it will be cue-invariant by construction.

This is not hypothetical for REE, and the convergence is worth flagging to governance explicitly. The
sibling experimental proposal for this same claim, EXP-0682, was gated `blocked_substrate` earlier on
2026-09-07 after the ContextMemory bank was measured near rank-1 under the online write path
(written-slot pairwise cosine 0.9993 in V3-EXQ-436g), compressing the w_harm range by 31x to 1600x
while slot *selection* remained healthy. That is precisely the failure this literature predicts:
completion machinery operating over an unseparated store, retrieving undifferentiated content despite
correctly discriminating the cue. The blocked experiment and this paper are describing the same
thing from opposite ends, which is a good sign for both. It also means the release condition on
EXP-0682 -- restore measurable pairwise separation among written slots -- is not merely a numerical
hygiene target; it is the biologically motivated precondition without which INV-040 is not testable
at all.

Confidence 0.68, held below 0.8 for one honest reason: the retrieved content here is a spatial
reference frame in a rat on a familiar track. Nothing in this paper concerns harm, valence, or
precision weighting, and I am not claiming the same circuit configures defensive terrain. The mapping
is at the level of the computation, not the content. One further boundary belongs on the record:
CA3's completion has a threshold in cue fraction, so "a minimal cue is sufficient" holds only above
that threshold, and INV-040 must not be read as asserting sufficiency for arbitrarily impoverished
cues.
