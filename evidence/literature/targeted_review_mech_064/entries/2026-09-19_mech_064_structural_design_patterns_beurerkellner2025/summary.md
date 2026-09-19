# Six patterns, one principle: security as a property of the system, not the model (Beurer-Kellner et al., 2025)

**Claim tested:** MECH-064 -- typed authority and control-store separation blocks direct exteroceptive
writes into policy and identity stores.
**Direction:** supports. **Confidence:** 0.76.

## What the paper did

Fourteen authors from ETH Zurich, Google DeepMind, IBM, Microsoft, Invariant Labs and elsewhere set
out to answer a question the field had been answering badly: given that prompt injection keeps
working, what kind of thing is a fix? Their answer is that it is not a model property. They are
direct about it -- "Designing models inherently robust to attacks that elicit arbitrary outputs --
such as prompt injection -- is extremely challenging" -- and equally direct that the usual
mitigations do not close the gap: "While these heuristic approaches provide some protection, they do
not provide guarantees."

What they propose instead is a governing principle and six patterns realising it. The principle:
"once an LLM agent has ingested untrusted input, it must be constrained so that it is *impossible*
for that input to trigger any consequential actions." The patterns are the Action-Selector,
Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute and Context-Minimization patterns.
They analyse the security/utility trade-off of each and illustrate them with case studies. Crucially,
they are candid about the mechanism by which the patterns work: by "constraining the actions of
agents to explicitly prevent them from solving arbitrary tasks."

## What it says about MECH-064

MECH-064 opens by asserting that prompt-injection resistance *requires* runtime-enforced payload
typing and write-path separation. That is a strong claim, and the most valuable thing this paper does
is to show that a large group of security researchers, working independently and with no interest in
REE, converged on the same requirement at the same level of generality. The claim's forbidden-path
row -- `EXTERNAL -> POL/ID/CAPS`, hard deny at runtime API boundary -- is one instantiation of their
principle. That is not nothing: it means MECH-064 is not an idiosyncratic architectural preference
but a restatement of what an independent literature now treats as the only family of answer that
yields guarantees.

Two of the six patterns land on specific bullets of the claim. Plan-Then-Execute fixes the action
plan *before* any untrusted content is read, which is exactly REE's "verification runs outside
proposal generation prior to commitment" -- the verification is upstream of the content that would
subvert it, structurally rather than by policy. The Dual LLM pattern separates a component that may
read untrusted content but not act from one that may act but never sees untrusted content, which is
REE's `EXTERNAL -> OBS/INS`-only restriction in different clothing.

But the most useful thing the paper gives MECH-064 is a demand rather than a reassurance, and it is
worth stating as the finding rather than burying it in caveats. There are six patterns, not one. They
are inequivalent -- different guarantees, different utility costs. MECH-064 names a *principle*
(authority separation) but does not commit to a *mechanism*. Which means an implementation could
satisfy every sentence of the claim's prose while choosing whichever pattern has the weakest
guarantees. As written, the claim is not falsifiable; it becomes falsifiable when it picks one.

## Limitations, and the disanalogy worth worrying about

The soft limitation first: this is a catalogue with case studies, not a measurement. It establishes
the right family of answer and reasons carefully about trade-offs, but it produces no number for how
much protection any pattern actually buys. It cannot be cited as evidence about the *magnitude* of
anything MECH-064 asserts, only about its shape.

There is also a direct tension with the claim that I would rather name than smooth over. The paper
says its patterns work by preventing agents from solving arbitrary tasks. MECH-064 asserts write-path
separation as a clean safety property with no stated competence cost. If this literature is right,
that is an incomplete claim: the separation necessarily removes reachable behaviours, and REE has not
characterised which ones. That is testable, and it should be tested rather than assumed benign.

The disanalogy that genuinely worries me is the enumeration problem. Every one of the six patterns
presumes a designer who knows in advance which actions are consequential -- and in a tool-calling
agent that is a reasonable presumption, because the consequential actions are an API surface you can
list. REE's privileged writes go into persistent self-model stores whose boundaries currently exist
as prose in `control_plane_signal_map.md`. Are a cognitive architecture's consequential writes
enumerable at all, at the granularity these patterns require? I do not think that question has been
asked, and it is prior to implementation rather than downstream of it. Until it is answered, this
paper supports MECH-064's *principle* while leaving its *implementability in REE* genuinely open.

One last honest note on the claim's rhetoric. MECH-064's table reads as an absolute -- hard deny.
This paper's framing is more careful: what architectural separation buys you is a guarantee
*conditional on the constraint being correctly drawn*, not an impossibility. The claim would be
stronger, not weaker, for adopting that phrasing, because it would put the burden where it belongs --
on the boundary enumeration, which is the part nobody has audited.

## Confidence reasoning

0.76, a little below the CaMeL entry and for an instructive reason: source quality here is arguably
higher in breadth (fourteen authors across six-plus institutions, and the field has adopted the
vocabulary) but lower in kind, because synthesis cannot be weighted as measurement. Source quality
0.80. Mapping fidelity 0.80 -- the governing principle is close to a restatement of the claim's
forbidden-path rule, and two named patterns hit two of its bullets, docked because the paper's unit
of protection is a task-scoped loop while the claim's unit is a store that outlives tasks. Transfer
risk 0.35, marginally worse than CaMeL: the same scope gap applies, plus this paper's entire method
presupposes an enumerable set of consequential actions, and for REE that is an open question rather
than a detail.

Source: arXiv:2506.08837 (v3, 27 Jun 2025), https://doi.org/10.48550/arXiv.2506.08837.

*Provenance note: the pattern names above were taken from the arXiv HTML full text. A WebFetch
summary of the PDF returned six plausible-sounding but fabricated names (Input Isolation,
Sandboxing, Semantic Separation, Output Filtering, Anomaly Detection, User Confirmation); they do not
appear in the paper and should not be propagated from any secondary source.*
