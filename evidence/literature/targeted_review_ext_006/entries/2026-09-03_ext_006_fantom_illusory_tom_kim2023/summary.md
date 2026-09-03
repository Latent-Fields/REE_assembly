# Kim et al. (2023) -- FANToM: Stress-testing Machine Theory of Mind in Interactions

## What the paper did

The authors begin from an observation about the shape of the existing evidence rather than about
its verdict: theory-of-mind benchmarks for language models are built from passive narratives. A
finished story is presented, one belief question is asked, and the model answers. Whatever else
that measures, it does not measure the thing the phrase "theory of mind" is normally meant to pick
out in social life, which is holding a model of what several other people currently know while the
situation keeps changing under you.

FANToM is built to remove that shortcut. It comprises 256 multiparty conversations containing about
10,000 questions, constructed around information asymmetry: characters join and leave the
discussion, so at any point different participants have had access to different subsets of what was
said. Six question types are asked about the same underlying facts -- belief as free response and
as multiple choice, information access as a list and as yes/no, answerability as a list and as
yes/no -- and this redundancy is the paper's methodological core, because question types that
demand identical underlying reasoning ought to be answered alike by any system that actually has
the reasoning. A human baseline was measured rather than assumed. On the all-question aggregate for
short conversations, humans reach 87.5%; GPT-4-0613 with chain-of-thought reaches 26.6%, ChatGPT
3.7%, and Mistral Instruct 0.1%. Chain-of-thought and fine-tuning do not close the gap.

## How this maps onto EXT-006

EXT-006 makes two assertions that most of this literature runs together: that there is no running
structural model of another agent's latent state, and that what stands in its place is pattern
completion over text. FANToM is the one paper found in this pull that separates them and finds for
both.

The first is addressed by the design. When characters enter and leave, each character's accessible
information is a state variable that has to be carried forward and updated turn by turn, and the
answer to a belief question is a function of that variable at the current moment. The collapse from
87.5% to 26.6% is a collapse specifically on maintaining state across an interaction, not on
extracting a belief from a static narrative -- the models are much better at the latter, as the
older benchmarks show. The second is addressed by the question-type dissociation. Models score
substantially higher on multiple-choice belief questions than on the free-response version and on
the information-access questions that the belief attribution logically presupposes. A system reading
an answer off a maintained belief state would score alike across formats, because all three queries
read the same variable. A system doing completion over surface form does better where the surface
supplies candidates to discriminate among. The authors put it plainly: "some instances of successful
LLM ToM reasoning in FANToM should be interpreted as illusory."

For REE the relevance is to ARC-010. Kappa coupling is defined over a continuously maintained model
of the other, because a penalty term that is meant to make another agent's predicted degradation
bear on this agent's trajectory selection has to be recomputed as the other's situation evolves.
What FANToM shows is that in the systems EXT-006 is about, the object that would have to be
recomputed does not persist across turns and is not queryable in a format-invariant way. That is not
a claim about REE's own implementation working; it is the reason REE builds the other-model
explicitly rather than expecting it to emerge from a language prior.

## Limitations and caveats

The models are 2023-generation, which is the generation-transfer risk running through every LLM
entry in this pull and is not dismissible -- Strachan et al. (2024), also in this pull, is the
counterweight. The all-question aggregate is a strict conjunctive score requiring every question
about a conversation to be answered correctly, so 26.6% must not be quoted beside a per-item
accuracy from another benchmark; the two numbers do not mean the same thing, and the human 87.5% is
the only fair comparator for it. The "illusory ToM" conclusion is an inference from a dissociation
across question formats rather than a measurement of what is represented internally. It is a strong
inference and the redundant-question design is the right way to license it, but what it establishes
is that the belief answers are not underwritten by the reasoning they presuppose, not what
representation is in fact present.

The fourth limitation is the one that recurs across this whole review, and it is worth stating
rather than leaving implicit. FANToM is a language benchmark. It can speak to whether a
model of the other is maintained; it cannot speak to whether such a model, once maintained, couples
into action selection as a penalty in the same residue field that governs the agent's own
trajectory. That second half of EXT-006 has no literature bearing on it in either direction, because
the paradigm has no selection process to couple into. It is properly experimental work, and this
pull should not be read as having addressed it.

## Confidence

0.82, the highest in this pull. Source quality 0.85 (peer-reviewed at EMNLP, purpose-built
benchmark at scale, measured human baseline, and -- importantly, given how much benchmark
contamination distorts this literature -- a key inference that rests on a within-paper dissociation
rather than on an absolute score). Mapping fidelity 0.85: the interactive information-asymmetric
design targets EXT-006's "running structural model" phrase more directly than anything else found,
and the format dissociation targets its "pattern completion" phrase; held below 0.9 because the
paper reasons about behaviour and question format throughout, never about internal representation.
Transfer risk 0.30, entirely model generation.
