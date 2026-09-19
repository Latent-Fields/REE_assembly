# Eight defences, all broken -- and what the broken set has in common (Zhan et al., 2025)

**Claim tested:** MECH-064 -- typed authority and control-store separation blocks direct exteroceptive
writes into policy and identity stores.
**Direction:** supports (by elimination). **Confidence:** 0.74.

## What the paper did

The authors' complaint is methodological before it is empirical: defences against indirect prompt
injection "remain questionable due to insufficient testing against adaptive attacks." A defence
evaluated against fixed attacks tells you it survived those attacks, which is not what anyone wants
to know.

So they let the attacker optimise. Eight defences, in three categories the paper names itself.
Detection-based: a fine-tuned DeBERTaV3 detector, an LLM-based detector, and perplexity filtering
("identifying adversarial inputs lacking coherent meaning"). Input-level: instructional prevention
("explicitly instructing the model to be wary of IPI attacks"), data prompt isolation (which
"introduces delimiters around the tool response"), sandwich prevention ("attaching an additional user
instruction following the tool response"), and paraphrasing. Model-level: adversarial finetuning.

They "bypass all of them using adaptive attacks, consistently achieving an attack success rate of over
50%."

## What it says about MECH-064

MECH-064's third bullet is as much a prohibition as a design: authority labels come from channel
metadata, *not* text content. Prohibitions are awkward to support directly -- you cannot measure the
absence of a bad idea -- so the natural evidence is a demonstration of what happens to the thing being
prohibited. That is what this paper supplies, and with unusual tidiness.

Sort the eight broken defences by what they actually rely on. Three infer trustworthiness by
inspecting content. Four manipulate the text stream to mark, warn about, or neutralise the untrusted
region. One trains the disposition into the model. Every single one derives authority from content, or
from a learned prior over content. All of them fall over at above 50 percent attack success once an
attacker is allowed to push.

Now notice what is *not* in the set. No capability propagation. No control/data-flow extraction. No
runtime denial at a store-write boundary. Nothing, that is, resembling MECH-064's actual mechanism.
The paper has emptied out the family the claim rules out a priori while leaving the claim's own family
alone.

Two specific hits are worth pulling out because they bear on how a REE implementation could go wrong.

*Delimiter defences fail.* Data prompt isolation and sandwich prevention are both broken. This matters
more than the bare result suggests, because delimiters are the cheap and tempting way to implement
"typed payloads": mark the untrusted region inside the text, instruct the model to respect the mark.
That *is* type separation -- but type separation located in the content stream, where the content can
reach it. If a REE implementation of MECH-064 ends up tagging payload types inside a serialised prompt,
it will not have implemented the claim. It will have implemented one of the eight broken defences. The
claim's separation is only meaningful when enforced in a channel the content cannot address.

*Adversarial finetuning fails.* This closes a loop with the Wallace et al. entry in this pull. Training
the model to respect an authority ordering is the other obvious route to MECH-064's authority model,
and it is empirically in the broken set. The claim's insistence on *runtime* rather than *learned*
enforcement therefore now rests on measurement, not only on architectural preference. That is a real
upgrade in the claim's evidential position, and it is the most concrete thing this pull establishes.

## Limitations, including the one aimed at REE

The support here is by elimination, and elimination is only as good as the exhaustiveness of the
alternatives. The honest statement of the limitation: MECH-064's mechanism survives this paper by
*absence*, not by *resistance*. Nobody attacked it. Absence of testing must not be written down as
robustness, and later work has in fact broken structural separation defences in multi-agent settings,
so there is no basis for thinking the claim's family is immune.

The sharper discomfort is that the paper's methodological verdict lands on REE as much as on the
defences it breaks. Its whole point is that defences look strong until somebody optimises against
them. MECH-064 has had no adversarial evaluation of any kind -- its confidence rests entirely on
architectural argument, which is precisely the epistemic position the paper is warning about. By the
paper's own standard the claim is *unevaluated*, not robust. The tempting reading -- "the rivals
failed and ours would not" -- inverts the finding. The defensible reading is narrower: the
content-derived-authority route is closed, which raises the prior on the metadata-derived route
without having tested it.

Which suggests the obvious owed work, and I would rather state it than leave it implied: MECH-064's
falsifier is an adaptive-attack evaluation against a REE implementation of the write-path denial, not
a further architectural argument. This paper is the template for what that evaluation would have to
look like.

## Confidence reasoning

0.74. Source quality 0.82, the highest in this pull and the only peer-reviewed venue among the
AI-security entries -- released code, one methodology, eight targets, a uniform and decisive result.
Mapping fidelity 0.70: the paper never mentions anything like REE's mechanism, so the mapping is an
inference from the *composition* of the tested set to a conclusion about its untested complement. That
is a sound prior-shifting argument and it is not a measurement of anything the claim asserts, and the
score reflects the difference. Transfer risk 0.30: no species or clinical inference, shared
artificial-agent domain, but the elimination structure carries its own risk -- the untested family may
fail for reasons this paper was never positioned to surface.

Source: Findings of the ACL: NAACL 2025; arXiv:2503.00061 (v2, 4 Mar 2025),
https://doi.org/10.48550/arXiv.2503.00061. Code: https://github.com/uiuc-kang-lab/AdaptiveAttackAgent.
