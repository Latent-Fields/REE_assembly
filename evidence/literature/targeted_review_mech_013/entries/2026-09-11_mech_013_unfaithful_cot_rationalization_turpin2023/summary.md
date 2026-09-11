# Language Models Don't Always Say What They Think (Turpin, Michael, Perez & Bowman, 2023)

MECH-013 is, at bottom, a warning about agents that talk. It says that a language layer sitting over
embodied ethical signals can come loose from them and fail in characteristic ways. REE does not yet
have that layer. So it is worth asking whether the artificial systems a REE language channel would
most likely be built from already show the decoupling. This paper says they do.

Turpin and colleagues added biasing features to prompts. The simplest was reordering few-shot
examples so that the right answer was always "(A)". The biases steered GPT-3.5 and Claude 1.0 toward
wrong answers, and accuracy fell by up to 36% across 13 BIG-Bench Hard tasks. The models'
chain-of-thought explanations did not mention the bias. They built a plausible case for the answer the
bias had produced. On a social-bias task, the explanations justified stereotype-aligned answers
without mentioning the stereotype. The verbal account and the actual determinant of the output have
come apart, and the account is fluent enough that you would not guess it.

Read beside Hall et al. (2012), also in this directory, the pattern is hard to miss. People defend
moral positions they never held, and language models defend answers for reasons that did not produce
them. Post-hoc verbal rationalisation looks like a property of language-producing systems as a class,
not a human quirk. The REE consequence is the same in both cases, and I think it is the most
practically useful thing this literature pull yields. If REE ever gains a symbol channel, the residue
field and harm streams have to be read directly for audit and governance. Anything the language layer
says about why an action was taken is a hypothesis to check against them.

The limits need stating clearly. These models have no harm signal, no residue, no body. What their
language comes loose from is the causal basis of a text output, not an ethical signal. So MECH-013's
specific mechanism, language suppressing or explaining away *harm*, is not instantiated. This paper
supports the rationalisation limb in its misreport form ("the account does not reflect the cause"),
not its suppression form ("the account turns the signal down"). The biasing features are artificial,
the models are of one vintage, and REE has no language substrate for any of this to attach to yet.

Confidence 0.52. The source is strong and the mapping modest, for the same reason as the Hall entry.
Between them, the two establish the misreport reading of rationalisation well. Neither touches the
suppression reading. Only the weak Jarcho entry and, indirectly, Walker's observer effect bear on
that.
