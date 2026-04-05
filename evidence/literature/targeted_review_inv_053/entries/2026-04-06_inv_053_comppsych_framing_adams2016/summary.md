# Adams, Huys & Roiser (2016) -- Computational Psychiatry Towards a Mathematically Informed Understanding

## What the Paper Did

Adams, Huys, and Roiser wrote what functions as the programmatic manifesto of the computational
psychiatry approach -- a review article situating the field and demonstrating its method on two
worked examples: depression and schizophrenia. For depression, they identify two candidate
computational mechanisms. The first is helplessness as a Bayesian prior: if an agent holds a
strong prior belief that its actions do not influence outcomes, Q-value computation will be
distorted before any learning has occurred. The second is the failure to inhibit mental
exploration of aversive events, drawing directly on Dayan and Huys (2008)'s pruning model.
Both mechanisms produce depressive phenomenology through distorted reward valuation. For
schizophrenia, they invoke predictive coding and abnormal precision weighting. The paper is
authoritative and highly cited as the reference statement of the field.

## Key Findings and Their Relevance

What this paper establishes is the conceptual framework of the entire Huys/Dayan/Adams lineage:
depression is fundamentally a problem of reward learning and value computation. The failure is
in how the agent evaluates the world -- either via prior beliefs about agency (helplessness)
or via runaway aversive search (pruning failure). Both accounts share a structural assumption:
the agent is capable of generating motivational states and is failing in how it computes or
constrains their expression. Agency, drive, and approach orientation are implicitly assumed
as background capabilities that may be distorted but are present.

## REE Mapping and the Terrain/Seeding Distinction

INV-053 asks a prior question: what if the substrate generating motivational states is itself
collapsed? The Adams/Huys/Roiser framework does not have a computational slot for this failure.
In their architecture, a motivational state is the product of Q-value computation weighted
by precision and prior beliefs -- there is no separable substrate whose absence would prevent
motivation from being generated at all. REE's architecture disaggregates this: benefit terrain
(VALENCE_WANTING) is a separate computational layer from value computation, and z_goal seeding
is a further separable mechanism. Either can fail while the Q-value computation machinery
remains intact and correctly calibrated.

The clinical significance of this distinction is real. The helplessness and pruning accounts
describe a patient who is cognitively active -- thinking, evaluating, ruminative, responsive
to new information albeit with distorted priors. INV-053 describes a different phenomenological
profile: the patient who is not engaged, not ruminative, not evaluating, but simply absent from
the motivational space. This maps more closely to severe melancholic depression with prominent
psychomotor retardation, avolition, and the clinical impression of "switched off" rather than
"switched wrong." These are not competing accounts of the same patient profile; they are
accounts of different patient profiles, which is exactly what the field needs.

## Limitations and Caveats

The paper's framework is genuinely powerful for the profiles it addresses, and the mechanisms
it identifies (helplessness priors, pruning failure) are well-supported empirically. The
limitation is scope, not validity: the framework operates at one architectural layer and does
not need to consider layers upstream of value computation. REE's claim is that those upstream
layers exist, are separable, and fail in characteristic ways. This is an extension of the
framework, not a correction of it. The REE paper should be careful to position INV-053 as
adding a layer to the Adams/Huys/Roiser framework, not as contradicting it -- the failure
modes can co-occur and may characterise different patient profiles or different phases of the
same illness.

## Confidence Reasoning

Source quality is very high. Mapping fidelity is modest because the paper establishes the
contrast class rather than evidencing INV-053 directly. The absence of terrain/seeding
concepts in the paper is informative: it confirms that this is a genuinely novel architectural
level, not a relabelling of existing constructs. Confidence 0.55 reflects the paper's role
as essential background for positioning INV-053, without contributing direct evidence for
the specific attractor/terrain/seeding claim.
