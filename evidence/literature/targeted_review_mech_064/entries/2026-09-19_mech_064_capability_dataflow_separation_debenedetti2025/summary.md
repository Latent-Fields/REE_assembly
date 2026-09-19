# CaMeL: control/data-flow separation and capabilities as a built defence (Debenedetti et al., 2025)

**Claim tested:** MECH-064 -- typed authority and control-store separation blocks direct exteroceptive
writes into policy and identity stores.
**Direction:** supports. **Confidence:** 0.82.

## What the paper did

The authors start from a premise worth stating plainly, because MECH-064 rests on the same one: a
language model cannot reliably tell an instruction from a datum, and no amount of training makes it
reliable enough to be a security boundary. If that is true, then the defence cannot live inside the
model. It has to live in the system around the model.

CaMeL is their construction. A *privileged* LLM sees only the trusted user query and never touches
untrusted content; from that query alone it emits a program that fixes the control flow and the data
flow. A *quarantined* LLM is then allowed to read untrusted content -- tool outputs, retrieved
documents, email bodies -- but it has no tool access and cannot emit control flow. A purpose-built
Python interpreter runs the program, propagating capability metadata alongside every value, and
evaluates security policies at each tool call. The consequence they emphasise is structural rather
than statistical: because the control and data flow were extracted from the trusted query *before*
any untrusted data was read, untrusted data "can never impact the program flow". On AgentDojo the
system solves 77 percent of tasks with provable security, against 84 percent for an undefended agent.

## What it says about MECH-064

The interesting thing here is not that the paper agrees with the claim. It is that a group with no
knowledge of REE, solving a narrower engineering problem, arrived at three of MECH-064's four
bullets independently and in the same order.

MECH-064 says external channels emit only `OBS` and `INS`. CaMeL says the component that reads
untrusted content may produce parsed values and nothing else -- no tool calls, no control flow. Same
restriction, different vocabulary.

MECH-064 says authority labels come from channel metadata, not text content. CaMeL attaches
capabilities to values according to provenance, and no string inside a value can forge one. This is
the bullet I would have expected to be the most contestable, and it is the one the paper is most
explicit about: the label is a property of where the data came from, full stop.

MECH-064 says verification runs outside proposal generation prior to commitment. CaMeL's policy check
fires in the interpreter at the tool-call boundary, structurally outside the LLM that proposed the
call. Again the same shape.

So the entry does two things for the claim. It moves MECH-064 from "plausible design stance" to
"design stance with a working implementation and a measured cost", and it hands REE a concrete
falsifiable specification: taint-carrying values, a policy evaluated at the store-write boundary, and
a proposal generator that never holds write authority. That is a testable thing, which is more than
the claim had before.

## Limitations, and the one that actually bites

The gentle limitation is the domain gap. CaMeL is software around a language model; REE's `POL`, `ID`
and `CAPS` are persistent self-model state in a cognitive control plane. The mapping is an argument
by structural analogy, and tight analogies are still analogies.

The limitation that actually bites is scope, and it is worth being uncomfortable about. CaMeL secures
the transformation of *one* trusted query into *one* program. Its capabilities protect values inside
a single interpreter run. MECH-064 is pointed somewhere harder: at writes into stores that persist
across episodes and accumulate. Nothing in this paper licenses the step from "per-episode capability
discipline holds" to "the policy store is durably uncorrupted". Ask the question the paper cannot
answer -- was a write that legitimately entered `ID` last week authorised, and would a thousand
individually-policy-compliant sessions leave `POL` where it started? -- and you are outside its
results entirely. Stored and cross-session injection is an open problem in this literature, and it is
an open hole in the claim.

Two smaller things worth recording rather than waving past. The provable-security guarantee is
provable *relative to a supplied policy*; the interpreter enforces what it is given and cannot tell
you the policy admits an attack. REE's equivalent -- the allowed/forbidden path table in
`control_plane_signal_map.md` -- is currently prose, not a checked artifact, which means the claim is
presently asserting a guarantee it has no mechanism to hold itself to. And the seven-point utility
gap is a real price for forbidding untrusted data from touching control flow. MECH-064 asserts the
separation is necessary and nowhere prices it. If REE pays something comparable in task competence,
that lands directly on the conversion-ceiling work, and it should be measured rather than assumed
away.

One asymmetry deserves flagging because it is a deliberate divergence rather than an oversight.
CaMeL's strength comes from making the bad path *impossible* -- untrusted data cannot express control
flow, so there is nothing to verify. MECH-064's `E3 proposal -> commit` row is *conditional*: it
routes through a verifier plus veto clearance rather than a structural denial. That is REE choosing
the harder and less provable side of the trade, presumably because a cognitive architecture cannot
forbid its own proposals the way an interpreter can forbid a syntax. Fine -- but the paper's
guarantee does not transfer across that choice, and the claim should not borrow its confidence.

## Confidence reasoning

0.82, driven by mapping fidelity (0.85) rather than by source quality alone. The paper's own design
decisions *are* the claim's bullets, so the translation needs little interpretive work -- that is
unusual and it is what earns the high number. Source quality 0.85: strong author group, released
code, evaluation against an established harness, discounted for preprint status and for the
policy-relative sense of "provable". Transfer risk 0.30, and the composition is worth noting: almost
none of that risk is domain transfer, since we are already in artificial-agent territory. It is
nearly all scope -- the persistent-store question MECH-064 exists to answer is the one the paper
does not touch.

Source: arXiv:2503.18813 (v2, 24 Jun 2025), https://doi.org/10.48550/arXiv.2503.18813.
Implementation: https://github.com/google-research/camel-prompt-injection.
