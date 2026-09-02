# Zhu (2026) -- Hourglass reasoning: stage isolation as the active ingredient in rule induction

If the Capkova lesion study is the best biological match to ARC-113, this preprint is the best
*mechanical* one, because it does not merely observe stage separation -- it builds it, removes it,
and measures the cost. Hourglass decomposes few-shot rule induction in a frozen LLM into an
Induction module (compressing support examples into a schema), a Deduction module (deriving a rule
and discarding the transient scaffold), an Implementer, and an error-driven Refiner. The design
constraint is the interesting part: only the compressed pair (schema, rule) may cross a stage
boundary. Everything else is walled off.

The results are substantial where they are positive. On ARC-AGI-2 with GPT-5.5, best-of-5 accuracy
rose from 62.8% to 76.8%; on ChipBench Verilog synthesis, pass@1 nearly doubled from 31.1% to 57.8%.
But the number that matters for ARC-113 is not in the headline table, it is in the ablations. The
author reports that a variant retaining structured intermediate representations while *removing* the
enforced context isolation -- Struct-SR -- collapsed accuracy below even the unstructured baseline.
Naming the stages was not enough. Only the topology of information flow produced the gain. This is
as close to a direct test of "the stages must not collapse into a single reasoning module" as the
current literature offers, and it comes with a named failure mode for the collapsed case: when raw
examples, current artifacts, and error feedback share one undifferentiated context, the system
"abandons its earlier rule and patches the code directly", anchoring on instance-specific
perceptual detail instead of the abstract regularity. That is a characteristic signature, not a
generic decrement.

A second ablation speaks to the *ordered* half of the claim, which I had not expected to find
evidence for at all. Weakening the initial induction cost 20.5 percentage points, and the downstream
Refiner could not recover it. An ordered pipeline inherits a hard dependency on the quality of its
early stages -- refinement cannot repair apprehension. If that generalises, it predicts something
specific for the REE ablation: short-circuiting an *early* stage should produce a deeper and less
recoverable failure than short-circuiting a late one, which is itself a dissociation worth
instrumenting.

Now the caveats, which are heavy enough that I have held confidence to 0.68 despite the highest
mapping fidelity in this pull. The stages are prompt-level roles imposed on a frozen model. Nothing
is trained. The isolation is soft -- context partitioning, not architecture -- and the author states
plainly that this offers no formal guarantee the stages did not silently recombine inside the model.
REE's stages are substrate components with their own learning dynamics, so this is an existence
proof that stage collapse carries a measurable cost in *some* inductive system, not evidence about
REE's substrate. The four Hourglass stages also cover only the middle of ARC-113's cycle: there is
no analog of experience, behavioural interaction, or long-term integration.

And the method is not uniformly good. On BBEH-Linguini with GPT-5.5 the staged architecture was
*worse* than the monolithic baseline, pass@1 falling from 58.3% to 46.5%. I have recorded this as a
failure signature rather than smoothing it over, because it is the honest boundary of the result:
enforced stage separation is not free and is not universally beneficial. Source quality is the
weakest link -- single author, not peer reviewed, two proprietary model families, a public ARC-AGI-2
evaluation set with unquantified pretraining exposure, and pass@5 estimates the author admits are
optimistically biased by early stopping. I would not want ARC-113 to rest on this paper alone. As
one leg of a triangulation with the lesion and fMRI work, it earns its place, mainly because it is
the only source that performs the collapse manipulation rather than inferring it.
