# Reward and navigation history in hippocampal replay (Bhattarai et al., 2019, PNAS)

## What the paper did

Bhattarai, Lee and Jung trained rats on a spatial sequence memory task and asked how awake hippocampal replay -- both forward and reverse -- is modulated by reward and by navigation history, two factors that are ordinarily confounded and that this design separates.

## Key findings relevant to the claim

Reward enhanced both replay types, but differently. It increased the *rate* of reverse replays, and it increased the *fidelity* of forward replays -- not only for the trajectory just travelled but for other alternative trajectories heading toward a rewarding location. Forward replays also reactivated upcoming rewarded trajectories more faithfully than already-rewarded ones. The authors' interpretation is stated plainly: forward and reverse replays may jointly construct a map of potential navigation trajectories and their associated values -- in their words, a value map.

## How this translates to REE

This paper cuts across MECH-143 rather than along it, and that is precisely why it earns an entry. MECH-143 is a claim about place-field geometry. This is a measurement of replay content. Both can be true at once: fields stable under value change, replay weighted by value. Nothing here contradicts Duvelle et al.

But I do not think that is a comfortable result for us, and it would be a mistake to file it as "not applicable". ARC-007's trajectory proposal module is functionally far closer to forward replay than to the static place map -- proposing candidate future trajectories is what forward replay *does*. So a value signal in forward replay lands squarely on the component ARC-007 most wants to keep free of value computation. The claim as worded survives; the architectural constraint the claim was registered to support does not obviously survive with it.

The useful consequence is a sharpening: MECH-143's no-new-value-computation constraint is defensible if stated at the level of place-field geometry, and false if stated at the level of dorsal hippocampal output. Those are not the same claim, and the current wording does not distinguish them.

## Limitations and caveats

The load-bearing step is entirely ours. Identifying ARC-007's proposal module with hippocampal forward replay is an architectural analogy, not an empirical finding, and if that analogy is rejected this paper says very little about MECH-143 in either direction. I have raised transfer_risk to 0.40 to mark that, and held mapping_fidelity at 0.50 because the paper measures a variable adjacent to the one the claim names.

Additionally: rat data, awake replay only, appetitive task only. There is no aversive condition, so nothing here constrains the negative half of R(x,t) -- which is where MECH-144 and MECH-073 do their work.

## Confidence reasoning

0.52, sitting deliberately just above the weak/moderate boundary. Source quality is genuinely high (0.80); the discount is all in the mapping. Direction is **mixed**: the paper is consistent with MECH-143's literal content while undermining the architectural inference drawn from it, and collapsing that into either *supports* or *weakens* would misreport it to governance.
