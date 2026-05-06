# Gurney, Prescott, Redgrave 2001 (Part I) — A computational model of action selection in the basal ganglia: a new functional anatomy

## What the paper does

The 2001 GPR model is the computational instantiation of the Redgrave 1999 thesis. Where the 1999 paper argued that the BG are a unified selection device, the 2001 model shows you can actually build one out of biologically plausible BG primitives. The model encodes each candidate action as a scalar salience and recasts action selection as signal selection — pick the highest-salience signal and pass it through. The selection circuit is an off-centre / on-surround feedforward network: each candidate inhibits its neighbours and excites its own output, producing winner-take-all dynamics on the GPi/SNr stage.

The model's most provocative architectural move, for Q-019 purposes, is that it decomposes BG anatomy into two pathways — selection and control — and explicitly contrasts this with the prevailing direct/indirect partitioning. Selection performs the actual signal arbitration. Control regulates the selection pathway, synergising with dopaminergic gain modulation to keep the selector working under varying input conditions. Neither pathway carries any notion of three loops or three independent gates. The whole computation is one selection circuit with one regulatory circuit.

## Why this matters for Q-019

Q-019 frames the architectural question as three loops or one gate. The GPR model's alternative decomposition — selection plus control — is technically a third option, but its computational story is the unified-selection story. The same selection circuit handles whatever inputs cortex routes to it, regardless of whether those inputs are limbic, associative, or motor in origin. The topographic specialisation that Alexander 1990 and Haber 2008 see in the input layer is, in the GPR view, peripheral to the actual arbitration mechanism.

The Humphries & Gurney 2021 retrospective (PMID 34272969) is useful context here: twenty years of follow-up work in the Sheffield / Nottingham labs has shown the GPR model is productive — descendant models continue to perform action selection competently without invoking three loops, and have been extended to tasks that would seem to require multi-domain arbitration. That track record is not proof that the brain does selection this way, but it does establish that the unified-selection view is computationally sufficient for a wide class of behaviours that the three-loop view also claims to explain.

## Limitations and caveats

The principal caveat is the obvious one: this is a computational model, not a measurement. GPR demonstrates feasibility, not biological reality. It is entirely possible that the BG have evolved a three-gate architecture even though a one-gate architecture would compute equally well. Selection pressure does not always produce the most parsimonious computation.

There is also a subtler caveat. GPR's selection / control decomposition is not exactly the same as Q-019's option (A) — it is a third architectural framing that happens to share option (A)'s commitment to a single arbitration circuit. Citing GPR against Q-019 option (B) requires the reader to accept that GPR's alternative decomposition is incompatible with strict three-loop functional segregation. That's correct, I think, but it's worth being explicit about: GPR doesn't directly say "three loops is wrong" — it says "here is a different decomposition that works without invoking three loops."

The Boraud 2000 single-unit follow-up (PMID 10712496) provides empirical anchoring for the unified-selection signature at the GPi output stage in MPTP-treated monkeys. So the GPR architecture is not pure theory — it has empirical correlates at the output stage. But the input-layer topography that motivates the three-loop view is also empirical, and GPR doesn't deny it. The argument is about what the topographically-organised inputs are doing — feeding three independent gates, or feeding one gate via parallel channels.

## Confidence reasoning

I'm assigning 0.7. Source quality is good (Biological Cybernetics, foundational paper, productive lineage). Mapping fidelity is moderate — GPR's decomposition is not exactly Q-019 option (A) but is incompatible with option (B). Transfer risk is moderate because computational sufficiency is not biological necessity. The entry's evidential weight against three-gate architecture is real but indirect: it shows the unified-selection alternative is buildable and has been productive, not that the brain actually implements selection this way.

According to PubMed, Gurney K, Prescott TJ, Redgrave P (2001), Biological Cybernetics 84(6):401-410. [DOI: 10.1007/PL00007984](https://doi.org/10.1007/PL00007984). For the twenty-year retrospective and lineage discussion: Humphries MD, Gurney K (2021), Biological Cybernetics 115(4):323-329. [DOI: 10.1007/s00422-021-00887-5](https://doi.org/10.1007/s00422-021-00887-5).
