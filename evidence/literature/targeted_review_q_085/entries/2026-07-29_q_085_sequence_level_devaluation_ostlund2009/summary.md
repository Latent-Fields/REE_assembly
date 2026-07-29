# The unit of representation is the unit of control (Ostlund, Winterbauer & Balleine 2009)

This is the closest thing in the animal literature to a direct test of Q-085's premise, and it
arrives with a cleaner dissociation than I expected to find. Rats were trained on a bidirectional
heterogeneous chain task in which the *order* of two lever presses determined which reward they got
-- so the ordered pair, not either press alone, was the thing that predicted the outcome. Half the
animals had excitotoxic lesions of dorsomedial prefrontal cortex; half were shams. Both groups
learned the task. The question was what they had learned.

Devaluation answered it. Sham rats withheld the *whole sequence* whose associated outcome had been
devalued, and did the same under contingency degradation. The lesioned rats did not reorganise at
that level at all: they suppressed only the terminal response of the offending sequence, leaving the
more distal one intact -- the signature of an animal that represents the two presses as separate
behavioural units rather than as a chunk. So the grain at which the animal represented the action
was the grain at which outcome-value information could express itself. That is exactly the coupling
Q-085 says MECH-323 leaves unowned: MECH-323 registers chunk size as a formation parameter, while
the property it actually sets lives on the consumer side, in the beta gate and the release set.

But the result cuts in a direction Q-085's RESOLVED-YES criterion does not currently anticipate, and
this is the most useful thing in the entry. Chunking did not make the sham rats outcome-insensitive.
It made them sensitive *at the sequence boundary*. Given a choice point before each sequence, they
declined to start the one they no longer wanted. What the chunk removed was the ability to adjust
*within* the sequence -- and in this task nothing ever asked them to.

Translate that into the V3 design and it becomes a pre-registration item. Q-085 scores RESOLVED-YES
if post-devaluation persistence rises monotonically with realised mean committed-chunk length. That
will hold only to the extent the value change becomes knowable *after* the beta gate commits. If the
SD-033b devaluation is fully knowable at chunk onset, a long macro is no more insensitive than a
short one, because the agent simply never commits to it -- and the experiment returns a flat
dose-response while the hypothesis is perfectly true. This is a different confound from the
interruption confound already registered (longer macros meeting more release opportunities and so
reading as *less* insensitive); the two push opposite ways and both need logging. Concretely: record
the tick at which the devaluation signal first becomes available to the agent relative to each
chunk's commit tick, and report persistence conditioned on chunks committed *before* that tick.

Limits, stated plainly. Sequences were two presses long, so there is no length axis here whatsoever
-- this study cannot speak to monotonicity, only to chunk-versus-no-chunk. The manipulation is a
lesion that removes the capacity to chunk, not a parameter that tunes grain. And it is a rat with an
intact dual-system architecture, whereas ree_core contains no model-free machinery at all, so the
dmPFC lesion has no counterpart in the substrate. One further detail worth carrying: when
sequence-level representation was lost, control did not vanish or spread evenly -- it collapsed onto
the response nearest the outcome. Element-wise credit assignment is not the neutral fallback.

Direction mixed, confidence 0.72.
