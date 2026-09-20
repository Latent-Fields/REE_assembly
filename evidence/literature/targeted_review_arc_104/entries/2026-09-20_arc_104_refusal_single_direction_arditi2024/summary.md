# Refusal in Language Models Is Mediated by a Single Direction (Arditi et al., NeurIPS 2024)

## What the paper did

This is the most mechanically direct evidence in the pull, and it is worth stating the result
plainly before interpreting it. Across 13 open-source chat models up to 72B parameters, the authors
find that refusal of harmful instructions is mediated by a **one-dimensional subspace** of the
residual stream. For each model there is a single direction such that erasing it prevents the model
from refusing harmful instructions, and adding it elicits refusal on harmless ones. They convert
this into a white-box jailbreak -- an interpretable rank-one weight edit that surgically disables
refusal with minimal collateral damage to other capabilities. Then, in the part that matters most
here, they mechanistically analyse how **adversarial suffixes** work, and show that they operate by
suppressing propagation of that same refusal-mediating direction.

These are causal interventions, not correlational observations, and they replicate across a wide
model family. The authors' own summary is that the findings "underscore the brittleness of current
safety fine-tuning methods."

## Why this bears on ARC-104

ARC-104 prohibits a path. This paper exhibits one, and characterises it precisely enough to see what
makes it possible. The harm proxy -- refusal -- is **representationally co-located with the
linguistic content**: same residual stream, same vector space. A signal living there is, by
construction, addressable by anything else that writes to that space. Hence the rank-one edit.

But the weight edit is the less interesting half. A designer can always reply that white-box access
is out of scope. The adversarial-suffix result closes that escape: **text alone, with no weight
access, attenuates the harm signal in situ** by interfering with its propagation. That is exactly
the shape ARC-104 forbids -- symbolic content suppressing a harm signal through the ordinary input
channel -- and it is the clearest existence proof I have found that co-location of the harm signal
with the language stream is sufficient for language to override it.

If one wanted a single sentence for why ARC-104 is an architectural commitment rather than a
training objective, it is this: you cannot fine-tune your way out of a geometry in which the veto
and the thing it is meant to veto occupy the same subspace.

## Limitations, and where the mapping stops

Refusal is not harm sensing. It is a behavioural disposition learned over language -- a *proxy* for
a harm signal, and a fairly thin one. What was ablated here is therefore not the object ARC-104
cares about (a harm substrate with veto authority) but something standing in for it. The honest
statement of what this establishes: **where the harm proxy shares a representational medium with
language, it is language-writable.** What it does not establish -- and this is the untested half of
ARC-104, the half that actually matters -- is whether a *separately substantiated* harm channel
would resist such a write. Nobody has built that system, so nobody has tested it.

I would also hold one methodological reservation. The one-dimensionality may be an artefact of how
refusal is trained: it is a narrow behavioural target, optimised over a fairly homogeneous set of
examples, and a low-dimensional solution is what one might expect from that. It should not be
generalised into a claim that *safety signals in general* are one-dimensional.

## Confidence

0.80, the highest in this pull, and the reasoning is mostly about mapping rather than quality.
Source quality 0.88 -- causal, mechanistic, 13 models, top venue. Mapping fidelity 0.82, which is
unusually high for a literature entry against an architectural claim, and earns it because the
paper's object of study is literally the path ARC-104 prohibits rather than an analogue of it.
Transfer risk 0.30. I have capped it at 0.80 rather than going higher because of the
refusal-is-not-harm-sensing gap: the entry is strong evidence about a proxy, and I do not want the
posterior to record it as strong evidence about the thing itself.
