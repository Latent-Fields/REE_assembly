# Jailbroken: How Does LLM Safety Training Fail? (Wei, Haghtalab & Steinhardt, NeurIPS 2023)

## What the paper did

Wei and colleagues asked a question that is prior to the usual jailbreak arms race: not *which*
prompts defeat safety training, but *why* safety training is the kind of thing that can be defeated
at all. They propose two failure modes. **Competing objectives** arise when a model's capability
goals and its safety goals pull in opposite directions -- the model has been trained both to be
helpful and to refuse, and an attacker constructs a prompt in which helpfulness wins. **Mismatched
generalization** arises when safety training fails to cover a domain the model's capabilities
nonetheless reach, so a reframing (an encoding, an unusual language, a fictional register) carries
the request outside the guard's coverage while leaving the capability intact. They then build
attacks from each failure mode and run them against GPT-4 and Claude v1.3. The attacks succeed on
every prompt in a collection of unsafe requests taken from the models' own red-teaming evaluation
sets.

## Why this bears on ARC-104

ARC-104 says there must be no path by which symbolic or linguistic content overwrites or suppresses
a harm signal. The temptation is to read that as a claim about how hard you should try. This paper
is the argument that it is instead a claim about *topology*. "Competing objectives" is not a
description of insufficient training; it is a description of an architecture in which the harm
constraint has been installed as **one preference among others, expressed in the same medium as the
input**. Once that is the shape, defeat by language is not a bug to be patched but the predictable
consequence of the arrangement -- and the authors say as much when they argue against the idea that
scaling alone resolves these failures.

That is precisely the distinction ARC-104 is trying to make explicit. The claim's own wording --
symbolic input may *condition* priors, but the harm substrate retains *veto* authority -- is the
statement that harm must not be a competing objective. Wei et al. give us the empirical case for why
that matters, stated in the negative: here is what happens when it is one.

## Limitations, and what this does not establish

The mapping is architectural, not substantive, and I want to be exact about the gap. These models
have no embodied or interoceptive harm channel whatsoever. Their "harm signal" is itself a
linguistic disposition, trained by RLHF over text. So the configuration ARC-104 actually specifies
-- a *non-linguistic* harm substrate holding veto over a language-mediated update -- is not the
configuration that failed here. It was never present to fail. What this paper shows is that the
guard is **necessary**; it is silent on whether ARC-104's particular guard is **sufficient**, or
even realisable. There is a real risk of reading more support out of it than it contains, and the
`mapping_caveat` on the record says so.

The attacks themselves are also dated -- they target specific 2023-era deployed models -- even
though the failure taxonomy has aged well and has been absorbed into later work (see the Qi et al.
entry in this same pull, which subsumes adversarial suffixes under a single mechanism).

## Confidence

0.72. Source quality is high (0.85): a well-designed, heavily cited study at a top venue with a
clean conceptual contribution. Mapping fidelity is the binding constraint at 0.70, for the reason
above -- the paper evidences the failure mode the guard excludes rather than the guard itself. Per
the skill's calibration guide I have weighted mapping fidelity heavily because ARC-104 is an
`architectural_commitment`, and I have held the aggregate below 0.8 deliberately. Transfer risk is
0.35 rather than lower because the inference runs from an all-linguistic system to an architecture
whose defining feature is the presence of something non-linguistic.
