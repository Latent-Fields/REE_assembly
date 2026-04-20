# Targeted review: SD-032d (PCC-analog attention partition / metastability)

**Date:** 2026-04-20
**Claim:** SD-032d -- Posterior cingulate analog in the cingulate integration substrate; emits `pcc_stability` in [0, 1] modulating MECH-259 switch threshold in the SD-032a salience coordinator.
**Scope:** Complements the parent `targeted_review_cingulate_integration_substrate/` (which contains the Leech & Sharp 2013/2014 "Arousal, Balance, Breadth" review and broader salience-network coverage). This pull targets PCC specifics beyond the overview review.

## Entries

| Entry | Year | Direction | Confidence | Role |
|---|---|---|---|---|
| Leech, Kamourieh, Beckmann & Sharp 2011 (Fractionating the DMN) | 2011 | supports | 0.78 | Ventral/dorsal PCC dissociate under cognitive load; dorsal PCC modulates DMN/CCN balance -- direct support for PCC-analog as a network-level modulator. |
| Leech, Braga & Sharp 2012 (Echoes of the brain within PCC) | 2012 | supports | 0.75 | PCC subregions echo multiple networks; posterior hub framing supports SD-032d's multi-input, integrative architecture. |
| Hayden, Smith & Platt 2009 (Macaque CGp default-mode electrophysiology) | 2009 | supports | 0.80 | Single-unit evidence that PCC firing tracks task engagement and predicts errors -- primate grounding for the success-EMA input to PCCAnalog. |
| Zaky et al 2024 (Mind-blanks during visuomotor tracking) | 2024 | mixed | 0.62 | Short attentional lapses (mind-blanks) do NOT produce PCC activity increase; refines PCC role to sustained engagement tracking rather than fast lapse detection. Justifies slow-timescale PCCAnalog design. |

Aggregate literature_confidence (simple mean): **0.74**.
Aggregate with direction weighting (supports counted +1, mixed counted +0.5 for SD-032d's design): 3 x supports + 1 x mixed = structurally supportive with one flagged nuance.

## Key findings for SD-032d

1. **PCC is a network-level modulator, not a within-network controller.** Leech 2011 and 2012 together establish the architectural framing: dorsal PCC sits at the interface between DMN and cognitive-control networks, with connectivity that modulates *between* networks rather than *within* either. SD-032d's design choice -- PCCAnalog emits a stability scalar biasing the SD-032a coordinator's switch threshold rather than itself performing control -- is consistent with this biology.

2. **PCC activity tracks task engagement on a slow timescale.** Hayden 2009 provides the primate single-unit grounding: CGp firing is suppressed during engagement and elevated during disengagement and cued rest, and predicts upcoming errors. The ree-v3 success-outcome EMA (updated via `agent.note_task_outcome`) plus offline-recency counter are the computational analogues.

3. **Short attentional lapses are NOT PCC-mediated.** Zaky 2024 establishes that brief involuntary mind-blanks do not produce PCC activity increase; the signal instead appears in dACC/SMA. This is a useful boundary condition: it justifies the slow-timescale PCCAnalog design (stability should track sustained engagement, not brief recoveries) and flags that any future need to model brief recovery dynamics belongs in SD-032b (dACC-analog), not SD-032d.

4. **The scalar-output compression is an explicit simplification.** Leech 2011 and 2012 both emphasise PCC heterogeneity (ventral/dorsal, multiple network echoes). ree-v3's PCCAnalog compresses this to one scalar because MECH-259 reads only one stability input. If V3-EXQ-447 shows coordinator behaviour sensitive to stability composition (e.g. fatigue-driven versus recency-driven), the architecture may need to be split.

## V3-EXQ-447 validation predictions

The current V3-EXQ-447 design tests PCCAnalog monotonicity against inputs. Given this pull, the minimum adequacy criteria are:

- `pcc_stability` responds monotonically to success-EMA manipulation (Hayden 2009 engagement-tracking signature).
- `pcc_stability` responds monotonically to drive_level manipulation (Leech 2013 arousal-state dependence).
- `pcc_stability` responds monotonically to offline-recency manipulation (Leech 2013 arousal, Zaky 2024 sustained-disengagement framing).
- Ablating PCCAnalog produces over-committed task behaviour (SD-032d spec + Leech 2011 dorsal-PCC-modulates-balance implication).

Stretch validation (not in current V3-EXQ-447):

- PCCAnalog's stability scalar should drop immediately prior to task errors (Hayden 2009 predicts CGp firing rises just before errors; ree-v3 inverse mapping is stability drops).
- PCCAnalog should not respond to brief (~1-2 step) attentional failures -- those belong to dACC-analog recovery dynamics (Zaky 2024).

## Gaps and flagged issues

1. **Task-demand signal absent from PCCAnalog inputs.** Leech 2011 dorsal PCC tracks task difficulty. PCCAnalog reads success-outcome, drive_level, offline-recency -- not cognitive-demand directly. A high-difficulty sustained task should produce a specific stability signature the current architecture cannot distinguish from a moderate-difficulty task at similar success rate.
2. **Multi-network echo compression.** Leech 2012 posits PCC as multi-network hub. Scalar output loses this. Future refinement candidate if coordinator behaviour needs differentiated stability channels.
3. **Recovery-of-responsiveness dynamics.** Zaky 2024 locates these in dACC/SMA. SD-032b owns dACC-analog; this is a cross-cluster flag for the SD-032 cluster rather than an SD-032d-specific gap.

## References (DOIs)

- Leech R, Kamourieh S, Beckmann CF, Sharp DJ (2011). Fractionating the default mode network. *J Neurosci* 31(9): 3217-24. [10.1523/JNEUROSCI.5626-10.2011](https://doi.org/10.1523/JNEUROSCI.5626-10.2011)
- Leech R, Braga R, Sharp DJ (2012). Echoes of the brain within the posterior cingulate cortex. *J Neurosci* 32(1): 215-22. [10.1523/JNEUROSCI.3689-11.2012](https://doi.org/10.1523/JNEUROSCI.3689-11.2012)
- Hayden BY, Smith DV, Platt ML (2009). Electrophysiological correlates of default-mode processing in macaque posterior cingulate cortex. *PNAS* 106(14): 5948-53. [10.1073/pnas.0812035106](https://doi.org/10.1073/pnas.0812035106)
- Zaky MH, Shoorangiz R, Poudel GR, Yang L, Innes CRH, Jones RD (2024). Conscious but not thinking -- Mind-blanks during visuomotor tracking. *Human Brain Mapping* 45(11): e26781. [10.1002/hbm.26781](https://doi.org/10.1002/hbm.26781)

Parent review (for broader cingulate-cluster context, already registered 2026-04-19): `targeted_review_cingulate_integration_substrate/` (9 entries including Leech & Sharp 2013 Brain review, Menon & Uddin 2010, Shackman 2011, Craig 2009, Baliki 2010, Seymour 2019, Vogt 2005, Scholl/Kolling 2015, Price 2000).

According to PubMed, all four entries here are sourced from PubMed-indexed publications with DOIs as listed above.
