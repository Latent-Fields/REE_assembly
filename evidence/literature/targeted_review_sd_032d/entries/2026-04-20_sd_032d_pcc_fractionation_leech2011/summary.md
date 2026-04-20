# Fractionating the DMN: ventral vs dorsal PCC (Leech, Kamourieh, Beckmann & Sharp 2011)

## What the paper did

Leech and colleagues used fMRI during a working-memory task (0-back versus 2-back) to examine whether the posterior cingulate cortex -- canonically a single DMN node that deactivates when attention turns outward -- is in fact functionally homogeneous. They applied dual-regression functional connectivity analysis to extract subregion-specific coupling with the default mode network and with the cognitive control network as task difficulty rose. A standard subtraction analysis within PCC reproduced the familiar global deactivation with increasing load. The dual-regression analysis did not.

## Key findings relevant to SD-032d

Ventral and dorsal PCC dissociated. Ventral PCC showed reduced integration with the DMN and weakened anticorrelation with the CCN as task demand increased -- consistent with ventral PCC doing the classically described "DMN" job of internally-directed cognition that has to be suppressed under task load. Dorsal PCC behaved oppositely. Its DMN integration increased, and its anticorrelation with CCN strengthened, as the task got harder. At rest, dorsal PCC was already showing mixed affiliation -- functional connectivity with both DMN and attention networks. The authors interpret dorsal PCC as a region that sits at the interface between the two large-scale networks and modulates their interaction, rather than being wholly internal to either.

## How this translates to REE

SD-032d posits a PCC-analog whose job is not to perform cognitive control itself (that is SD-032b/dACC) but to modulate the metastability of the coordinator -- to bias how readily the SD-032a salience network flips between operating modes. Leech 2011 is direct support for that role: dorsal PCC is not a controller, it is a modulator of how two controllers (DMN and CCN, roughly internal and external task networks) interact, and that modulation is load-dependent.

The ree-v3 implementation compresses ventral and dorsal PCC into a single stability scalar `pcc_stability` in [0, 1] that feeds MECH-259's switch threshold. That compression is defensible under the minimum-sufficient principle: the coordinator needs one scalar to bias the threshold, not a full subregional decomposition. But the paper's finding that dorsal PCC tracks task load is a reminder that the current PCCAnalog inputs -- success EMA, drive_level, steps-since-offline -- do not include a cognitive-demand signal. If V3-EXQ-447 shows that the stability scalar responds only to fatigue and offline recency but not to task-demand-linked signals, that would flag a gap relative to Leech 2011.

## Limitations and caveats

This is human fMRI in healthy young adults on a working-memory task. The inferred "modulation" is a functional-connectivity dissociation, not a causal demonstration. The Leech team does not show that perturbing dorsal PCC changes the DMN/CCN balance; they show the subregion's connectivity profile is load-dependent. The REE translation -- that this corresponds to a stability scalar fed into a coordinator's switch threshold -- is a further computational inference the paper does not make. Ventral/dorsal fractionation does not by itself license the one-scalar compression; the compression is a ree-v3 design choice that has to be defended on its own terms (it is, in the SD-032d spec, because MECH-259 reads only one such scalar).

## Confidence reasoning

Strong source (J Neurosci, dual-regression is well-validated). Mapping fidelity is moderate -- the paper supports the architectural role (PCC-analog modulates between-network balance) but does not directly license the specific computational form (scalar-to-threshold). Transfer risk is low because the underlying dissociation is a robust fMRI finding replicated in later work, including the companion Leech 2012 paper also registered in this pull. Confidence 0.78 -- solid support for the SD-032d architectural claim, with an explicit caveat that dorsal PCC's demand-sensitivity is not currently captured in PCCAnalog's arithmetic.
