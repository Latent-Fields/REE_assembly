# Attention is Turing-Complete (Pérez, Barceló & Marinkovic, 2021) — the requirement IMPL-027 drops

## The gap this entry is about

IMPL-027's section 2 is introduced as showing how "REE's derived structures address each CNC
requirement." The claim's `notes` field in claims.yaml puts it more strongly: "REE addresses all four
from first principles."

It addresses three. The subsections are Behavior Consistency (2.1), Long-Horizon Stability (2.2),
Universal Programmability (2.3), and Machine-Native Semantics (2.4). Three of those are CNC
requirements. "Long-Horizon Stability" is not — it is a REE-introduced category. And requirement 1,
Turing completeness, appears in the section 1 table, is never answered, and gets no row in the
section 5 translation table either.

The count being right (four subsections, four requirements) is probably why the substitution went
unnoticed. It is the kind of drift that happens when a source list and an answer list are drafted at
different sittings.

## What the paper establishes

Pérez, Barceló and Marinkovic prove that the Transformer with hard attention is Turing complete,
"exclusively based on their capacity to compute and access internal dense representations of the
data," and identify minimal architectural elements sufficient for the result. It is a formal
computability argument in JMLR, with no trained-model component.

## Why this cuts both ways for IMPL-027

The obvious reading is that the missing row is a defect, and it is: a comparison document that
enumerates four requirements and answers three has an accuracy problem, and the claim's notes assert
a coverage the document does not deliver. That should be fixed, and there is a second-order problem
behind it — REE has no registered formal expressiveness or computability result anywhere in the claim
graph. So there is currently nothing that *could* fill the requirement-1 row. The omission is not a
drafting slip that a paragraph would repair; it marks an absence in the underlying claim set.

The less obvious reading is that the omission may be the right call, and IMPL-027 would be stronger
for saying so explicitly rather than staying silent. If hard-attention Transformers are already Turing
complete, then expressive universality is not what separates a Completely Neural Computer from a
current video model. The NC prototypes score around 4% on arithmetic while being built from an
architecture class that is, in principle, universal. Universality was never the binding constraint.
What binds is whether execution stays consistent, whether routines install and persist, whether
semantics are structural rather than surface — which is to say, requirements 2, 3 and 4. The three
IMPL-027 actually answers.

So the constructive fix is not to invent a REE answer to requirement 1. It is to say, in one honest
paragraph: requirement 1 is not architecturally discriminating, here is why, and REE therefore makes
no claim about it. That converts a silent gap into a stated position, and it is a better position
than the one the notes field currently asserts.

## Limitations, stated plainly

I want to be careful not to over-read a formal result, because this is precisely the literature where
that happens most.

Turing completeness of an architecture *class* says nothing about whether any trained instance
executes anything reliably. The proof and the 4% arithmetic accuracy are entirely compatible. Nothing
here means requirement 1 is "solved" in any sense the NC authors would accept.

I also did not verify from the full text which idealisation assumptions the proof rests on. The
standard caveats in this literature are arbitrary-precision internal representations and unbounded
computation steps, and if those are load-bearing here — as I would expect — the practical force of the
result is weaker than the headline. I am flagging this rather than asserting it, because I read the
abstract and the venue metadata, not the proofs.

And the comparison is asymmetric in a way worth naming: REE has no formal expressiveness result of its
own to set against this one. I am using a Transformer result to argue about where a gap in a REE
document sits, not to compare two programmes on equal formal footing.

## Confidence reasoning

0.62, direction `weakens`. Source quality 0.85 — peer-reviewed, strong venue, well-cited. Mapping
fidelity 0.60, because the paper is about Transformers and has nothing to say about REE, NC, or this
claim; the argument connecting it to IMPL-027's missing row is mine. Transfer risk 0.50, the highest
in this pull and deliberately so: the distance between an idealised universality proof and any claim
about real systems is exactly where this result is most often abused, and the narrow use I am making
of it — locating a coverage gap and arguing the gap is defensible — is about as much weight as it will
bear.
