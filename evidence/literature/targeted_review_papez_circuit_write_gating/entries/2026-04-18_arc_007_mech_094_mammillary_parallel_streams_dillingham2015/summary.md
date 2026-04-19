# Dillingham et al. 2015 — How do mammillary body inputs contribute to anterior thalamic function?

**PubMed:** 25107491 | **DOI:** [10.1016/j.neubiorev.2014.07.025](https://doi.org/10.1016/j.neubiorev.2014.07.025) | **Venue:** Neuroscience and Biobehavioral Reviews, 54, 108-119.

*Source: PubMed.*

## What the paper does

A review that reframes mammillary body function. The pre-2015 consensus
treated the mammillary bodies as a passive hippocampal relay — a node on
the fornix that forwarded hippocampal output to the anterior thalamus.
Dillingham et al. marshal lesion, electrophysiology, and tracer evidence
to show that this is wrong on two counts. First, the mammillary bodies
receive substantial non-hippocampal input from the ventral and dorsal
tegmental nuclei of Gudden. Second, the medial and lateral mammillary
bodies carry distinct information streams — the medial body (fed by
VTN-Gudden) supports memory via the anterior medial thalamic nucleus,
while the lateral body (fed by DTN-Gudden) generates head-direction
signals via the anterior dorsal thalamic nucleus. These two parallel
streams converge on the anterior thalamus but remain functionally
segregated.

## Findings relevant to REE

This matters for ARC-007 and MECH-094 together. The write-gating
hypothesis requires that different action modes — habitual, planned,
simulated, sleep — can route through different Papez sub-pathways.
That architectural requirement is vacuous if the Papez circuit is a
single serial loop from hippocampus through one relay station to
anterior thalamus and back. It becomes concrete if the relay itself
is dual-channel, which is exactly what Dillingham et al. establish.

The two-stream structure gives REE a candidate mapping: z_world-domain
hippocampal proposals (ARC-007 trajectory proposal) route through the
medial-mammillary / AM-thalamus channel; egocentric / head-direction
signals route through the lateral-mammillary / AD-thalamus channel.
The two channels can be gated independently. The hypothesis_tag
(MECH-094) — if it lives in this circuit at all — can therefore act
on specific channels rather than the whole loop.

## Mapping and translation to REE

The translation is architectural, not functional. The paper establishes
that the anatomical substrate for channel-specific write gating exists
and is not a serial bottleneck. It does not identify any projection
that carries a write-gating signal. The failure mode is the usual one
for connectome data: structure without direction-of-information-flow.

There is also a specific falsification signature. The two-stream model
predicts a double dissociation: selective VTN-Gudden lesion should
impair memory write but spare head-direction; selective DTN-Gudden
lesion should do the opposite. The review cites converging evidence
for both arms of this dissociation in rodent lesion studies.

## Caveats and limitations

Rodent anatomy. The mammillary bodies have well-established human
homology, but the Gudden tegmental nuclei are less well-characterised
in humans — the critical upstream inputs are not as anatomically
settled in primates as they are in rats. Transfer risk is moderate,
not low. The review is a secondary source; primary evidence comes
from lesion and tracer studies in rats.

The two-stream architecture is necessary for mode-specific gating but
not sufficient to prove it. The gate-bearing projection — the
anatomical address of MECH-094's hypothesis tag — remains unidentified.

## Confidence reasoning

0.8. High source quality (rigorous review synthesising lesion,
electrophysiology, and tracer evidence). High mapping fidelity because
the two-stream architectural claim translates directly into the REE
requirement for channel-specific write gating. Moderate transfer risk
because rodent-to-human mapping for Gudden tegmental nuclei is less
settled than for the mammillary bodies themselves. The entry
substantively strengthens the anatomical substrate for MECH-094
beyond what Kamali 2023's tractography provides, because it adds
functional differentiation to the structural connectivity.

## Related REE claims

- ARC-007: multi-node hippocampal trajectory proposal; parallel stream
  architecture is the structural substrate for routing different
  trajectory types through different Papez sub-pathways.
- MECH-094: hypothesis-tag write gate; two-stream Papez architecture
  permits channel-specific gating, the structural prerequisite for
  mode-specific write profiles.
