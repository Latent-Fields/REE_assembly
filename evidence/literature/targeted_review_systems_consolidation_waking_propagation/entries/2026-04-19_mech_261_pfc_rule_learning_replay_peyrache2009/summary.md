# Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009) -- Replay of rule-learning related neural patterns in PFC during sleep

## What the paper does

Peyrache and colleagues recorded ensemble activity from rat medial prefrontal
cortex during and after a cross-modal rule-shift task. The behavioural design
required the rat to switch between two strategies (e.g., visual vs tactile
cue-based rule), with the rule-shift providing a clean learning event. The
authors then analysed PFC ensemble activity during post-learning slow-wave
sleep using explained-variance methods that can detect whether a pattern
present during waking behaviour re-emerges during sleep above chance. The
central finding: PFC patterns associated with response selection during rule
learning replay prominently during subsequent slow-wave sleep, and the replay
occurs in transient highly synchronised bouts that are largely coincident with
hippocampal sharp-wave-ripple complexes. The coupling to hippocampal SWRs
provides the first clean demonstration that the hippocampal-cortical dialogue
framework extends to prefrontal, rule-representation-level cortex -- not just
sensory or spatial cortex.

## Relevance to MECH-261

The other three empirical entries in this pull (Carr 2011, Rothschild 2017,
Tambini 2019) establish (a) that awake SWRs support both consolidation and
retrieval, (b) that hippocampal replay causally propagates forward into
sensory cortex, and (c) that awake reactivation biases subsequent cognition
in humans. What they do not individually establish is that this propagation
reaches cortex specifically carrying action-relevant representations. Peyrache
and colleagues close that gap. The cortical region whose patterns replay under
hippocampal SWR coupling is medial PFC, the rodent homologue of the cortex most
implicated in rule representation, action policy, and meta-control.

For MECH-261, this matters because the claim is not just that replay happens
and propagates forward, but that replay propagates to substrates that will
subsequently be read by action selection in external_task mode. The V3 design
consequence is that internal_replay and offline_consolidation modes should be
implemented as write-enabled to a PFC-analog substrate -- perhaps the
rule-level or meta-policy layer, above the moment-to-moment trajectory proposal
buffer -- and not only to cortical-sensory buffers.

## Caveats and mapping risks

The paper is sleep-only. The bridge to waking internal_replay is inferred from
the Carr 2011 review and subsequent awake-SWR work, not from this paper directly.
The rule-level ensemble patterns that replay are cognitive control signatures
rather than motor action commands; the translation to action-selection bias in
REE terms requires the additional step of assuming that rule-representation
changes eventually propagate to action-value estimates. This step is standard
in cognitive neuroscience but is one inference removed from the direct finding.

A secondary caveat is methodological: the explained-variance analysis detects
statistical similarity between waking and sleep ensemble patterns but does not
directly demonstrate that the sleep replay causally alters subsequent waking
behaviour. Later work in the Battaglia and Peyrache groups has addressed this
with optogenetic disruption paradigms; those are downstream of this paper and
broadly support the causal interpretation, but this specific paper leaves the
causal arrow as inference from temporal coupling.

## Confidence reasoning

Source quality is high (Nature Neuroscience, Battaglia lab, rigorous EV/REV
methodology that has become standard). Mapping fidelity is high for the claim
that cortical action-relevant representations (not just sensory) participate
in SWR-coupled replay. Transfer risk is moderate: sleep-to-waking and
rule-representation-to-action-selection are both standard but require adjacent
literature to complete. Aggregate confidence 0.75.
