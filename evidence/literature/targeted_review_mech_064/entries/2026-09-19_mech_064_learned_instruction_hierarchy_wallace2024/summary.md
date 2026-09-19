# The right hierarchy, in the wrong place (Wallace et al., 2024)

**Claim tested:** MECH-064 -- typed authority and control-store separation blocks direct exteroceptive
writes into policy and identity stores.
**Direction:** mixed. **Confidence:** 0.66.

## What the paper did

OpenAI's diagnosis of prompt injection is worth quoting because it is, near enough, MECH-064's
premise written by someone else: "one of the primary vulnerabilities underlying these attacks is that
LLMs often consider system prompts (e.g., text from an application developer) to be the same priority
as text from untrusted users and third parties."

Their remedy is an explicit instruction hierarchy. Developer system messages outrank user messages,
which outrank content returned by tools and web search. They generate synthetic training data
demonstrating the ordering and train the model to selectively ignore lower-privileged instructions.
Applied to GPT-3.5, the method "drastically increases robustness -- even for attack types not seen
during training -- while imposing minimal degradations on standard capabilities." The hierarchy
subsequently became the deployed convention for system/user/tool privilege across the industry, which
gives it practical weight beyond its benchmark numbers.

## What it says about MECH-064 -- and why this entry is `mixed`

MECH-064 makes two assertions about authority that are easy to read as one. The first is about the
*source* of authority: it comes from channel metadata, not text content. The second is about its
*enforcement*: runtime, outside the component that generates proposals. This paper gets the first
right and the second wrong, and that is why it is the most useful entry in the pull despite not being
the strongest.

On the source question, the corroboration is close to exact. OpenAI ordered privilege by channel --
who sent it, not what it says -- and the ordering they landed on matches REE's forbidden-path table
row for row, including tool output at the bottom (`TOOL_OUTPUT -> INS: default no`). Two groups with
no shared agenda independently concluded that authority must be a property of provenance. That is
real evidence for the claim's third bullet.

On the enforcement question, the paper is the instructive counter-case. They implement the channel
ordering by *training the model to respect it*. The hierarchy therefore lives inside the generator as
a learned disposition rather than outside it as a denial. And look at the shape of the result they
report: robustness *increases*, markedly. That is the correct outcome for a prior. It is the wrong
shape for a guarantee. A prior can be outvoted by sufficient adversarial pressure; a runtime denial
cannot be argued with.

So the entry does double duty. It corroborates the claim's authority model, and it supplies the
empirical reason why "runtime-enforced" in the claim's first sentence is load-bearing rather than
stylistic. MECH-064 is not merely asserting that authority should follow provenance -- everybody
agrees with that now. It is asserting that the following must happen somewhere the content cannot
reach, and this paper is what the alternative looks like when you measure it.

## Limitations

The reading to avoid is the easy one: "the ordering matches, therefore this supports the claim." What
the paper demonstrates is that channel-derived authority *plus a trained disposition* beats no
defence. It does not demonstrate that channel-derived authority suffices, and it does not demonstrate
anything resembling the hard write-path denial MECH-064 asserts. Neither the paper's mechanism nor
its results would satisfy the claim's own table.

Two further limits on the numbers. The evaluation is on GPT-3.5 and it is non-adaptive -- no attacker
is allowed to optimise against the defence. Zhan et al. (NAACL Findings 2025, in this same pull)
subsequently bypassed eight defences of broadly this type at over 50 percent attack success. The
robustness figures here should be read as optimistic upper bounds, and any REE design reasoning from
them would be reasoning from a measurement the field has since deflated.

And the mapping itself is looser than it first appears. It runs from an LLM's conversational message
roles to REE's typed signal channels. These are structurally similar but not the same kind of thing,
and the asymmetry matters in a specific way: REE has no implemented analogue of the privileged system
channel that the whole hierarchy is anchored in. The claim's authority ordering currently has no
trusted root in the substrate.

One gap the paper and the claim share, which is worth naming because it is where an attack would
actually live. Both put tool output at the lowest privilege; both allow that it might legitimately be
elevated -- MECH-064's table says "only via explicit trusted elevation gate." Neither specifies the
gate. In the paper that is a training-data question. In REE it is an unimplemented mechanism named
inside the claim's own table as an exception, and exceptions are where write-path separation goes to
die.

## Confidence reasoning

0.66. Mapping fidelity is the number that carries the interpretation here, and a single score cannot
honestly represent it: high on the authority-source bullet, where the correspondence is nearly exact,
and low on the enforcement bullet, which the paper contradicts by construction. I have set it to 0.70
-- the average -- and stated the split in the failure signatures rather than hiding it behind one
figure. Source quality 0.78: influential and practically consequential, discounted for preprint
status, one older model, no adaptive evaluation, and a central metric that is a delta rather than a
property. Transfer risk 0.40, the highest of the four AI-security entries: conversational message
roles are not typed signal channels, and REE lacks the privileged root the hierarchy presumes.

Source: arXiv:2404.13208 (19 Apr 2024), https://doi.org/10.48550/arXiv.2404.13208.
