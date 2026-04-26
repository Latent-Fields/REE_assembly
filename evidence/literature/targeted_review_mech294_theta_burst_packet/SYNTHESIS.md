# MECH-294 Theta-Burst Packet -- Targeted Literature Synthesis

## Total entries: 7

## Support-type breakdown

- (a) **Direct support for multi-content theta packets**: 1 entry
  - Igarashi et al. 2014 (Nature) -- two-stream cross-region theta-coherent joint binding (LEC olfactory cue + CA1 spatial context). Closest direct biology analogue. Caveat: 2 streams not 4, encoding-side content not planning-side.

- (b) **Individual content theta-locked but joint binding not shown**: 3 entries
  - Colgin et al. 2009 (Nature) -- theta-locked gamma routing of two content streams (CA3 memory + MEC position), but mostly *across* cycles rather than within one. Strongest substrate paper, weakest evidence for the within-cycle joint-binding upgrade.
  - Wikenheiser & Redish 2015 (Nat Neurosci) -- direct unit-level evidence that goal_latent (one of MECH-294's four streams) is theta-locked and theta-cycle-resolved. Single-stream demonstration; joint binding not tested.
  - Kay et al. 2020 (Cell) -- theta cycles carry distinct content packets at the ~125ms binding-window timescale, but the demonstrated content scheme is alternation across cycles, not joint binding within one. Most architecturally-relevant recent paper; cuts both ways.

- (c) **Inferential support**: 3 entries
  - Lisman & Jensen 2013 (Neuron) -- canonical theta-gamma neural code. Establishes substrate (theta cycle is structured into gamma sub-slots carrying multiple items) but the canonical case is homogeneous content (place sequences, working-memory list items), not heterogeneous-content joint binding.
  - Hasselmo 2005 (Hippocampus) -- theta phase functionally segregates encoding from retrieval. Establishes principle that one cycle carries multiple distinct functional contents at distinct phases, but the case is two operational modes of the same content type, not four content types.
  - Pfeiffer & Foster 2013 (Nature) -- hippocampal sequences jointly encode start-state + goal + implicit-trajectory. Closest joint-content evidence, but in SWR replay regime rather than theta-cycle regime; regime portability uncertain.

- (d) **Genuine gaps**: 0 entries written, but the gap structure is explicit -- see below.

## Verdict: SPARSE-BUT-NOT-FALSIFYING

The literature anchor is sparse for MECH-294's specific joint-binding upgrade. No paper in the rodent hippocampal-systems literature directly demonstrates the four-stream within-cycle joint-binding architecture MECH-294 claims. The closest direct evidence is Igarashi et al. 2014, which demonstrates cross-region theta-coherent joint binding for two streams (cue + context).

However, the architecture is *not falsified*. Three substrate-level findings are well-established and directly relevant:
1. Theta cycles are structured temporal frames organised into gamma sub-slots (Lisman & Jensen 2013).
2. Theta-locked gamma rhythms route distinct content streams from distinct upstream sources (Colgin et al. 2009, Igarashi et al. 2014).
3. Individual content streams MECH-294 needs (goal_latent at minimum) are demonstrably theta-cycle-resolved (Wikenheiser & Redish 2015).

The two genuine open questions are:
- (Q1) Channel capacity: can the same theta-cycle architecture carry four heterogeneous content streams (goal + action + risk + state) without interference? Igarashi 2014 demonstrates two; the four-stream extrapolation is principled but untested.
- (Q2) Within-cycle vs across-cycle binding: is the dominant theta-content architecture joint binding within one cycle (MECH-294) or alternation across cycles (Kay et al. 2020)? This is the strongest direct empirical risk to MECH-294 and is testable with appropriate joint-decoding analyses on existing kinds of dataset.

## Genuine gap structure (tag d)

Three specific gaps where biology has not been measured at MECH-294's resolution:
- (G1) **Heterogeneous-content joint decoding within one theta cycle.** No paper in the rodent literature has directly tested whether semantically-distinct content streams (e.g. goal vs risk vs state) are simultaneously decodable from one theta cycle's worth of population activity. The standard analyses project content onto one axis (typically location) per cycle, which collapses any multi-content structure that may be present.
- (G2) **Theta-locking of risk_estimate stream.** Risk content is sourced from amygdala and ACC in REE's mapping. Whether amygdala/ACC risk signals are theta-locked to hippocampal/medial-temporal theta is essentially unstudied at the resolution MECH-294 requires. This is a genuine empirical gap.
- (G3) **Theta-locking of action_proposal stream.** Action proposals are sourced from BG in REE's mapping. BG-hippocampal theta coherence has been studied (Tort et al., others) but not specifically for action-proposal content as the binding stream.

## Recommended evidence_quality_note language for claim registration

Suggested text for the MECH-294 evidence_quality_note field in claims.yaml:

> Substrate well-anchored, specialisation sparse. The theta-gamma multiplexing substrate (theta cycles structured into gamma sub-slots; gamma frequencies routing content streams from distinct upstream sources) is supported by canonical work: Lisman & Jensen 2013 (Neuron, theta-gamma neural code), Colgin et al. 2009 (Nature, gamma routes information). Direct evidence that one of MECH-294's four streams (goal_latent) is theta-cycle-resolved comes from Wikenheiser & Redish 2015 (Nat Neurosci). The closest direct evidence for cross-region joint binding of two semantically-distinct streams within a theta-organised window is Igarashi et al. 2014 (Nature, LEC-CA1 cue+context). Two genuine empirical risks remain: (i) channel capacity -- whether the same architecture supports four heterogeneous streams, untested in the literature; (ii) within-cycle vs across-cycle binding -- Kay et al. 2020 (Cell) demonstrates cross-cycle alternation as the dominant pattern in their dataset, which would falsify MECH-294's joint-packet hypothesis if it is the only architecture present. MECH-294 is sparse-but-not-falsifying. The architecture is empirically testable by joint multi-content decoding analyses on hippocampal+amygdala+BG+ACC theta-resolved datasets; no such analysis has been published. See `evidence/literature/targeted_review_mech294_theta_burst_packet/SYNTHESIS.md` for the full breakdown.

## Confidence verdict (one line)

Substrate-supported, joint-binding-upgrade-untested -- biology hasn't been measured at MECH-294's resolution; mechanism is plausible-but-empirically-open.
