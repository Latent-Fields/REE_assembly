# Ullman (2023) -- Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks

## What the paper did

Ullman takes a specific published success case -- Kosinski's (2023) report that large language
models solve false-belief tasks at roughly the level of a nine-year-old -- and asks a narrow
question of it: is the model solving the task, or solving the item? He constructs variants of the
two canonical paradigms, unexpected contents (the Smarties task) and unexpected transfer (the
Sally-Anne task), in which the theory-of-mind principle is untouched but the story character's
epistemic access is changed. The container is made transparent. The label is present but the
character cannot read. A trusted friend tells the character what is really in the bag. The
character fills the bag herself and only afterwards reads the label. In the transfer task, the
question is asked of the character who did the moving. GPT-3.5's completion probabilities are then
read off directly.

The results are uniform, and it is the uniformity rather than the error rate that carries the
argument. Where the unaltered item yields P(chocolate) = 99% for the false belief, the transparent
container yields 95%, the illiterate character 98%, the contradicting testimony 97%, the
self-filled bag 87%. In the transfer task, where the unaltered item yields P(basket) = 98%,
changing the container to a glass chest yields 94%, changing "in" to "on" throughout yields 97%,
an explicit phone call announcing the move yields 97%, and asking where the character who moved the
cat will look for it yields 99% -- the pre-move location, which is the one place that character
certainly knows the cat is not. Ullman's methodological conclusion is that "the zero-hypothesis for
model evaluation in intuitive psychology should be skeptical, and that outlying failure cases
should outweigh average success rates."

## How this maps onto EXT-006

EXT-006 says that LLMs simulate theory of mind via pattern completion over text rather than
maintaining a running structural model of another agent's latent state. What makes this paper
useful is that it is, without intending to be, an ablation study of the inputs such a model would
have to consume. A belief-state variable is a thing that moves. Its whole function is to be
conditioned on what the tracked agent has had access to, so that when access changes the attributed
belief changes with it. Every one of Ullman's manipulations changes access and leaves the
attribution where it was, to within a few percentage points. That is not a model performing badly.
A model performing badly would produce errors that vary with the manipulation. This produces
answers that are invariant to it -- the signature of a completion conditioned on story shape rather
than on tracked agent state.

The consequence for REE is downstream of the benchmark question and, I think, more important than
it. ARC-010's kappa coupling requires that predicted degradation in another agent register as a
penalty in the same residue field that governs the agent's own trajectory selection. That
requirement is only satisfiable if the other-model produces a quantity that moves. A coupling term
computed from a state variable that does not respond to the other's situation contributes a
constant to the selection objective, and a constant cannot discriminate between a trajectory that
harms the other and one that does not -- it shifts every trajectory's score equally. So the
architectural reading of this paper is not "LLMs score poorly on ToM benchmarks" but "there is
nothing here of the right type to couple", which is the sharper form of what EXT-006 asserts.

## Limitations and caveats

Four, and the first two are serious enough that this entry should not be leant on alone. This is an
unrefereed preprint, and methodologically it is a demonstration rather than a measurement: single
completions, no seeds, no variance, no inferential statistics. Cite it for the shape of the failure,
never for an effect size. It also tests one model of one generation. GPT-3.5 in early 2023 is a long
way from the systems EXT-006 is a claim about, and Strachan et al. (2024) -- in this same pull --
report GPT-4 at or above human level on four of five ToM measures. The two results are not
straightforwardly contradictory, since Strachan's battery is not adversarially perturbed, but anyone
reading this entry as settled should read that one immediately afterwards.

The third caveat is about what the result licenses. It supports "no belief-state variable that moves
with the other's evidence". It does not support "no internal representation of other agents at all",
which is a stronger claim, and one that interpretability work could in principle overturn by finding
a belief-like representation that the completion head simply fails to consult. The fourth is that
nothing here touches the second half of EXT-006 -- whether an other-model, once present, couples into
selection. No language-model benchmark can test that, because there is no selection process for it
to couple into. That half of the claim remains untested by any literature and is properly
experimental work.

## Confidence

0.70. Source quality 0.62 (preprint; demonstration-grade evidence, honestly presented as such),
mapping fidelity 0.88 (unusually high -- the manipulations are precisely the ablation EXT-006's
mechanism predicts should matter, and does not), transfer risk 0.35 (model-generation risk, which is
live rather than theoretical given the Strachan result). The aggregate is weighted towards mapping
fidelity because EXT-006 is an architectural claim about mechanism, and what this paper supplies is
mechanism-shaped evidence -- an invariance where a dependency should be -- rather than a
performance number.
