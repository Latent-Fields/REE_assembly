# Associative and spatial learning deficits in HuD-overexpressing mice (Bolognani et al., 2006)

## Why this paper opens the gate

The 2026-05-21 gated_plasticity intake would not let seven candidates be registered until someone
went and looked at two things in the biology. The first was HuD/ELAVL4 -- whether a developmental
plasticity operator is genuinely reused in the adult brain, and on what terms. This is the paper
that answers it, and it answers in a more interesting direction than the intake anticipated.

HuD is a neuron-specific RNA-binding protein that stabilises short-lived mRNAs. It does this during
brain development, during nerve regeneration, and in synaptic plasticity -- the same operator,
across epochs, which is exactly the "developmental reuse" shape the intake was reaching for.
Bolognani and colleagues took two independent transgenic lines overexpressing HuD in adult forebrain
neurons under the alphaCaMKII promoter, and ran them through contextual and cued fear conditioning
and the Morris water maze.

The mice were worse. Acquisition and retention of both cued and contextual fear were impaired, and
they could not remember where the hidden platform was. There were no motor or sensory abnormalities,
so this is a cognitive deficit rather than an inability to perform. The authors' conclusion is the
sentence the intake needed: post-transcriptional stabilisation "may have to be restricted temporally
and spatially for proper acquisition and storage of memories".

## What it settles, precisely

It settles that the *permission structure* is the load-bearing part of the design, not a safety
wrapper around it. The staged candidate `plasticity.developmental_reuse_stricter_permissions` says
an operator carried over from development must be gated more tightly in the adult than it was
developmentally. Here is a case where removing that restriction does not produce a system that
learns too eagerly or too broadly; it produces a system that learns worse on every endpoint tested.
For REE that reframes the gate from an optimisation to a correctness condition.

It also does real work for INV-056. Selective neoteny says social, goal-representation and
epistemic-ethical substrates should retain elevated plasticity into adulthood while procedural and
motor substrates harden. This paper is a reminder that "retain elevated plasticity" cannot be
implemented as "leave the developmental operator running". The retained thing has to be the
*capacity* under a gate, not the ungated operator.

## What it does not settle, and I want this on the record

The manipulation is constitutive and lifelong. That leaves a live alternative explanation the design
cannot exclude: the transgene may have mis-wired the brain during development, and the adult deficit
is a developmental scar rather than a failure of adult permissions. An inducible, adult-onset version
of the same experiment would separate these. Until one exists, the entry supports the claim's shape
without pinning its mechanism.

It is also purely gain-of-function. Nothing here shows that gated adult reuse *helps*. The staged
candidate has two limbs -- that the operator is reused, and that reuse needs stricter permissions --
and this paper supports only the second.

One detail deserves more attention than it usually gets. The authors note HuD is itself increased
after learning. So the substrate rises with learning and impairs learning when raised constitutively.
That is a non-monotonic dose-response, and none of the seven staged candidates currently model it:
they are all written as permissions, which is to say binary gates. If the biology is a gain with an
optimum, a binary gate is the wrong abstraction and the candidates would need rewording before
registration. I would rather flag that now than have it surface after the claims are in the registry.

## Confidence

0.74, direction mixed (supports INV-056 and INV-074, mixed on MECH-083). Good study, close mapping,
discounted for the constitutive-versus-conditional confound and for the gain-of-function-only design.
