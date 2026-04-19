# Vogt 2005 — Pain and emotion interactions in subregions of the cingulate gyrus

**Source:** *Nature Reviews Neuroscience*, [10.1038/nrn1704](https://doi.org/10.1038/nrn1704). Via PubMed (PMID 15995724).

## What the paper does

Vogt provides the canonical anatomical and functional parcellation of the cingulate gyrus. Using cytoarchitecture, receptor-binding profiles, macaque tract-tracing, and converging human lesion/fMRI evidence, he argues the cingulate is four distinct regions, not one: ACC (perigenual pACC + subgenual sgACC), MCC (anterior aMCC + posterior pMCC), PCC, and RSC. Each subregion has a distinct role in pain processing and in the broader emotion/action/memory integration.

## Key findings relevant to the claim

- **pACC / sgACC**: drives autonomic and endocrine responses to pain; handles pain affect and the coupling between affective pain and visceral/hormonal output. Clinical damage -> emotional blunting, apathy, altered pain experience.
- **aMCC (anterior midcingulate)**: effort-value, action-outcome evaluation, conflict monitoring, credit assignment for costly actions. The region most engaged during decisions about whether a painful or effortful action is worth its expected reward. Receives pain input *and* input from reward and cognitive-control streams.
- **pMCC (posterior midcingulate)**: motor preparation and enactment -- Vogt describes this region as the motor pole of the cingulate, tightly coupled to premotor/supplementary motor areas.
- **PCC**: memory/attention/orientation, strongly implicated in the default mode network, handles autobiographical and contextual retrieval. Task-deactivated during external-attention demands; elevated during internal-generated cognition.
- **RSC**: spatial and contextual memory; tightly coupled to hippocampus.

Pain activates all four regions but in different ways: pACC for affect and autonomic coupling; aMCC for evaluating whether to avoid/tolerate; pMCC for motor enactment of escape; PCC for contextual/retrieval-related aspects (what does this pain mean in this context, have I been here before).

## How this maps onto REE (the translation)

This is the scoping paper for the new cingulate-substrate SD cluster. The architectural implication is that the missing substrate is not one module but four separable computations:

| Vogt region | Function | ree-v3 gap |
|---|---|---|
| pACC / sgACC | Affective pain -> autonomic/valence | z_harm_a produced but not wired to valence/drive update |
| aMCC | Effort-value, action-outcome evaluation, conflict | No integration node; trajectory cost sums z_harm_s only |
| pMCC | Motor gating on effortful/painful actions | MECH-090 beta propagation gate (partial; broken in SD-021) |
| PCC | Offline retrieval / DMN / context | INV-049 sleep (partial), MECH-092 micro-quiescence replay (partial) |

The z_harm_a consumer question (Options A/B/C) maps specifically onto the aMCC role: integrating affective pain with effort/reward to produce an action-value bias. Meanwhile the *urgency-interrupt* function (Option C in the original framing) is more an AIC-pACC function -- autonomic urgency that phase-resets the motor loop. This is why the Explore investigation found the two roles scattered across ree-v3 (lambda_ethical scaling, urgency_weight commit-threshold modulation): they correspond to *different cingulate subdivisions* doing *different jobs*, and ree-v3 has gestures at each without the integration substrate that binds them.

Critically: Options A, B, C are not competing. They are different subdivisions' jobs. A working cingulate substrate needs all three, partitioned cleanly.

## Limitations and caveats

Vogt's parcellation is anatomical, not computational. In a unified latent architecture like ree-v3 we can in principle compute all four cingulate functions in one shared module if the input signals are separable -- the four regions are convenient labels for computations, not a mandate for four separate torch modules. Over-fitting to the anatomy would be a mistake.

The review also doesn't speak to the computational *form* of each region's operation. We get "aMCC does effort-value" but not "aMCC computes expected-value-minus-cost at decision time and writes the result to striatal DA targets." For that, the Rushworth lab papers (Scholl/Kolling 2015) are needed.

Transfer risk is moderate: macaque cytoarchitecture -> human functional imaging -> embodied-agent computation is a three-step transfer, and each step loses fidelity. The *existence* of separable cingulate computations is robust; the specific anatomical boundaries are less directly load-bearing for ree-v3.

## Confidence reasoning

0.85. Vogt is canonical; the anatomical claims have held up; and the paper gives the exact scoping the new SD cluster needs. Mapping fidelity is high for the architectural-partitioning question but only moderate for specific wiring decisions, because the paper does not speak in the computational language ree-v3 requires. Low-to-moderate transfer risk because the core claim -- "cingulate is not a unitary substrate" -- is robust across species and methods.
