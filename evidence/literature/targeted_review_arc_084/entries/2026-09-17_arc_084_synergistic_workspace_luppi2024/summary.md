# A synergistic workspace for human consciousness revealed by Integrated Information Decomposition (Luppi et al., 2024)

## What the paper did

Luppi and colleagues applied Integrated Information Decomposition to fMRI from 100 individuals,
adding 15 volunteers under anaesthesia and patients with disorders of consciousness as a validation
arm. The decomposition separates the information two regions share into *redundant* components
(either region alone carries it) and *synergistic* components (only the two together carry it). On
this basis they identify gateway regions, corresponding to the default mode network, and broadcaster
regions, corresponding to the executive control network. Loss of consciousness coincided with a
breakdown of information integration within this synergistic workspace, particularly in the gateways.

## The part that supports ARC-084, and a part I did not expect

ARC-084's first commitment is that inter-field coupling is *typed* -- that an edge has a kind, not
just a weight. This paper is a strong demonstration that a typed account is both constructible and
empirically productive: synergistic and redundant couplings are distinguishable, they are not
recoverable from a single connectivity scalar, and they dissociate under a manipulation as dramatic
as anaesthesia. That is a real result, and it makes the typed-edge formalism considerably more
respectable than a purely theoretical proposal would be.

The unexpected contribution is the gateway/broadcaster distinction. ARC-084's edge specification
includes a `write_authority` field, and gated-decoupling as a coupling mode whose function is to
isolate simulation, offline integration or unsafe candidates from release authority. Across this
whole pull, nothing else evidences that field at all. Here there is at least a structural analogue: a
broadcaster holds release authority over information into the wider network that a gateway does not.
Whether that analogy survives contact with a real V4 design I cannot say, but it is the only
empirical purchase on write_authority I found, and it is worth recording for that reason alone.

## Why I have set mapping fidelity low on purpose

ARC-084's own notes cite Luppi in its CAUTIONS -- competition is not synaptic inhibition, a
competitive edge is not intrinsically harmful, competition is not reward subtraction. The claim is
already alert to the risk of borrowing this literature carelessly. I want to state the specific form
that risk takes here, because it is easy to miss and would be expensive to discover later.

Synergy and redundancy are not cooperation and competition. They are orthogonal axes. Two regions can
be redundant while cooperating, or synergistic while competing; the decomposition says how
information is distributed between them, not whether one is suppressing the other. A V4
operationalisation that reached for Integrated Information Decomposition as its measure of ARC-084's
coupling modes would be measuring a genuinely different thing while believing it had tested the
claim. That would produce a clean-looking result on the wrong question -- the worst outcome available.

So this entry supports "edges have types". It does not support "the types are cooperative,
competitive and gated-decoupling", and it should not be counted toward the latter.

## A quieter observation that cuts against the claim

The entire decomposition is non-negative. Nothing in this framework requires a competitive mode, and
the framework nevertheless explains a great deal -- including a clinical dissociation. That is at
least weak evidence that a rich typed-edge account of brain coupling can be built without any signed
component whatsoever. ARC-084 insists that sign is first-class and generative. The most developed
typed-coupling framework in contemporary neuroscience gets by without it. That is not a refutation,
but it does mean the burden of showing that sign adds something sits squarely with the claim, and
this literature does not lift it.

## Confidence

0.50 -- the lowest in this pull, and low for a reason that has nothing to do with the quality of the
work, which is high. The paper is strong evidence for a neighbouring proposition and only indirect
evidence for this one. Recording that distinction accurately matters more here than the number does.
