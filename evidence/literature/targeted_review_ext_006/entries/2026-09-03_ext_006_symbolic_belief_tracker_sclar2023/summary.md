# Sclar et al. (2023) -- Minding Language Models' (Lack of) Theory of Mind

## What the paper did

The other entries in this pull establish EXT-006's absence claim by its consequences: brittleness
under perturbation, dependence on question format, failure to persist across conversational turns.
This paper takes the opposite route. It supplies the thing EXT-006 says is missing and reports what
happens.

SymbolicToM is a decoding-time algorithm that sits outside the language model and maintains an
explicit graphical representation of each character's beliefs, each character's estimate of the
other characters' beliefs, and higher orders of the same. The network's weights, training data and
prompt are untouched; only the belief structure is added. On the ToMi benchmark, GPT-3-Davinci gains
38 absolute points, reaching 92% averaged across question types. On second-order false-belief
questions -- what A believes B believes -- GPT-3.5 gains 78 absolute points. The authors also test
out-of-distribution robustness by varying story structure, and there the divergence is stark: on one
variant, GPT-3.5 with SymbolicToM reaches 100% while a supervised baseline that had been fitted to
the benchmark drops to 65%. Their framing of the motivation is direct -- models "still lack basic
theory of mind capabilities out-of-the-box", and they posit that "simply scaling up models will not
imbue them with theory of mind due to the inherently symbolic and implicit nature of the phenomenon."

## How this maps onto EXT-006

An absence claim is awkward to evidence. You can show the consequences of the absence, which is what
Ullman and FANToM do, but consequences are always compatible with the alternative reading that the
mechanism is present and merely weak. What Sclar et al. contribute is closer to a controlled
manipulation. Everything except the belief representation is held fixed -- same parameters, same
semantic knowledge, same decoding -- and an explicit per-character belief state is added. If the
deficit had been a knowledge deficit, adding a bookkeeping structure would do nothing, because the
structure supplies no facts about the world. The gain of 38 to 78 absolute points therefore locates
the deficit where EXT-006 puts it: in the maintained structural representation, not in what the
model knows.

The second-order result sharpens this usefully. The largest gains are on recursive attributions,
which is where pattern completion has the least surface regularity to exploit and where a structural
model has the most to offer, because a graph that already holds A's model of B answers the question
by lookup. That gradient -- small gains on first-order, very large gains on second-order -- is what
one would predict if the underlying competence were completion over story shape.

For REE this is the closest thing in the accessible literature to a positive argument for the
architectural commitment in ARC-010. REE does not treat the other-model as something that will
emerge from sufficient exposure; it builds it. The moral here is that this is the right call, and
that the difference it makes on the recursive cases is not marginal. I want to be careful about how
far that carries, though, and the next section is mostly about that.

## Limitations and caveats

The first caveat is the one that matters most and it cuts directly against a naive reading.
SymbolicToM is a symbolic scaffold outside the network, built by a separate algorithm that parses
the story into a graph. What the paper demonstrates is that an explicit structural other-model is
sufficient to repair the behaviour. It does not demonstrate that the network could host such a
model, nor that a learned internal representation would do the same work. REE's other-model is
meant to be internal and learned, so this is an argument by analogy about what kind of object is
required, not evidence about whether REE's version functions.

Second, the authors report -- to their credit, since it undercuts their own numbers -- that ToMi
contains spurious patterns, and that in their human study physical commonsense makes human answers
depend on which nouns are used and disagree with ToMi's own labels. Every headline figure here rests
on that benchmark. The direction of the effect is not in doubt but the point estimates are doing
less work than they appear to.

Third, the tracked object is propositional belief about object location in generated reading-
comprehension narratives. ARC-010 needs something rather different: a latent state of another agent
whose predicted degradation enters the residue field as a penalty on trajectory selection. Beliefs
about where a cat is are not that, and the gap between the two should not be smoothed over by the
shared word "model". Fourth, the base models are GPT-3-Davinci and GPT-3.5 -- 2023 systems, with the
same generation-transfer risk that qualifies every LLM entry in this pull.

## Confidence

0.76. Source quality 0.82 (ACL main conference; an unusually clean intervention in which the belief
structure is the only thing that varies; and honest reporting of a flaw in the benchmark their own
results depend on -- held below 0.85 precisely because that flaw is real). Mapping fidelity 0.72:
the structural moral transfers to ARC-010's design commitment, but the object tracked is
propositional rather than latent-affective, which is a genuine gap rather than a formality. Transfer
risk 0.30, covering model generation; the scaffold-versus-internal distinction is handled as a
caveat rather than discounted numerically, because it is a boundary on what the entry may be cited
for rather than a probability that the finding fails to hold.
