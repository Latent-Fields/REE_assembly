# Eichenbaum 2017 -- On the Integration of Space, Time, and Memory

DOI: [10.1016/j.neuron.2017.06.036](https://doi.org/10.1016/j.neuron.2017.06.036) -- Neuron (PubMed 28858612)

## What the paper did

A theoretical review by Eichenbaum on how spatial and temporal information are jointly represented in hippocampus. He synthesises the place-cell, time-cell, grid-cell, and event-cell literatures and argues for a generalised hippocampal mechanism: not a dedicated spatial map nor a dedicated temporal map, but a multiplexed network that organises memories along whatever dimensions are relevant to the current task.

## Findings relevant to V_s foundation

The central architectural claim is that CA1 carries independent multiplexed representations of multiple dimensions -- space, time, sequence position, abstract relations -- with mixed selectivity at the single-cell level. This is the strongest available statement that hippocampal coding is fundamentally multi-dimensional rather than reducible to a single privileged variable like place. Different memories engage different dimension mixtures, and the same physical place can be represented differently depending on which dimensions are task-relevant.

For the V_s foundation, this carries the strongest implication for the per-stream vs integrated V_s question. The Eichenbaum frame is consistent with V_s being meaningful per dimension/stream because the underlying hippocampal code is mixed-selectivity over multiple dimensions -- a per-stream V_s readout would correspond to projecting the hippocampal mixed code onto each dimension separately. But the readout itself is integrated at the cell level (mixed selectivity); per-stream V_s in the substrate is an in-silico projection of the integrated representation, not a per-stream computation that biology performs explicitly.

## Translation to REE / MECH-269 / per-stream V_s

For the per-stream V_s architectural choice, this paper argues nuance. Biology does multi-dimensional integrated coding at the cell level; per-stream V_s in the substrate is a projection of that integrated code, not a biology-faithful per-stream computation. So per-stream V_s is best characterised as a computational convenience that exposes information already present in the integrated representation, not as a deviation from biology -- as long as the architecture document is honest that biology computes mixed selectivity and the per-stream readout is a projection.

For MECH-269 anchors, the multi-dimensional code reinforces the (place, context) framing from Wood and Frank: an anchor key is fundamentally multi-dimensional, with place as one component and other task-relevant dimensions as others. The substrate plan should treat the per-stream vector as the disambiguator, with the integrated mixed representation as the underlying biology.

For granularity, Eichenbaum is explicit that the relevant scale depends on what the task organises memories along. Place-cell-field grain is right for spatial tasks; time-cell-grain is right for temporal sequences; event-segment grain is right when context boundaries are the organising structure. The substrate's commitment to environmentally-grounded chunks (grid cell or action-object) is one defensible choice but not the only biologically valid one -- a more general substrate would let granularity emerge from the task structure rather than fix it architecturally.

## Limitations and caveats

Theoretical review, not new data. The mixed-selectivity claim is well-supported by primary literature but the specific multiplexing mechanism is debated. The granularity-emerges-from-task framing is principled but may make the substrate harder to specify -- biology gets it for free, in-silico we have to choose. The paper does not address dual-trace coexistence directly, only that multiple dimensions can be mixed in a single cell.

## Confidence reasoning

Source quality very high (Neuron, Eichenbaum, well-cited). Mapping fidelity is high for the per-stream V_s architectural reading -- the paper directly supports the mixed-selectivity-with-projection-readout interpretation. Transfer risk is moderate because the granularity-emerges-from-task position complicates the substrate's fixed-granularity commitment.