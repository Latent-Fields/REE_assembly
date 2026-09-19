# A critical time window for dopamine actions on the structural plasticity of dendritic spines (Yagishita et al., 2014)

## What the paper did

Yagishita and colleagues asked how a synapse knows that it was the one responsible. Behaviour is reinforced by rewards arriving within roughly a second or two of the action, but the molecular basis of that narrow timing had not been identified. They used two-photon glutamate uncaging at single dendritic spines of striatal medium spiny neurons together with independent optogenetic stimulation of dopaminergic afferents, which let them impose an arbitrary interval between the two signals rather than observing whatever interval the animal happened to produce.

Spine enlargement -- a structural, persistent change, not a transient conductance shift -- occurred only when dopamine arrived 0.3 to 2 seconds *after* the glutamatergic input. Outside that window, nothing durable happened. They then traced the window to its cause: rapid cAMP regulation in thin distal dendrites, where high phosphodiesterase activity means protein kinase A is activated only if dopamine follows glutamate closely enough. The contingency detector is a local biochemical timer.

## Why this is the right paper for MECH-066

The Kaufman null-space entry in this pull establishes that shared representations can be separated at a *transient* output boundary. Its honest weakness, which I priced explicitly, is that it says nothing about persistence -- and MECH-066's whole force is about *durable* write boundaries. This paper is what closes that gap.

The dissociation here is double and clean. Glutamatergic activity happens whether or not it will be consolidated: representation is unrestricted. And that activity, fully present and fully tuned, produces no structural change at all without the coincident reinforcement signal: activity is not sufficient for persistence. The reference system genuinely does hold the representation open and gate the durable write, which is the shape MECH-066 asserts.

It also puts a mechanism under MECH-060's existing experimental result. EVB-0043 (EXQ-005, PASS) ablated write-locus separation in `ree-v1-minimal` by letting pre-commit `sim_error` leak into the persistent residue field, and measured a 46-fold inflation of `total_residue` (8520 versus 186) with harm ordering preserved in the clean condition. That is an architectural demonstration that *something* must gate the durable write. Yagishita shows what the biological version of that gate is made of, and that it operates at the level of the individual synapse rather than as a single checkpoint.

## The limitation that matters, stated plainly

The gate demonstrated here is **temporal, not typed**, and I do not think this can be glossed. Dopamine-gated spine enlargement is a coincidence detector. It asks *when* the input arrived, never *where it came from*. A self-generated, pre-commit simulation that happened to fall inside the 0.3-2 second window would be consolidated exactly as readily as genuine reafference -- the mechanism has no channel-identity information to condition on.

MECH-066 asserts something stronger: separation by channel *type* at the write boundary. On the evidence here, biology may achieve most of its practical separation by the cheaper route -- simulated activity is usually not temporally adjacent to a commit, so it is usually not eligible -- rather than by typing the channels at all. That is a materially different architecture from REE's, where `update_residue` accepts only post-commit harm by construction and the typing is explicit in code. The paper therefore supports MECH-066's *requirement* while leaving its *mechanism* clause unevidenced, and this is the first failure signature I recorded: a REE variant that gated durable writes on temporal proximity to the commit rather than on channel identity would reproduce precisely the CONT_RESIDUE contamination.

The second limitation is levels of description. This is single-spine biochemistry in mouse striatal slices under optical uncaging, and the identified mechanism -- phosphodiesterase-restricted PKA activation in thin distal dendrites -- has no counterpart anywhere in REE. The inference from here to a claim about error-channel routing crosses several levels, which is where the `transfer_risk` of 0.45 comes from.

## Confidence

0.7. Source quality is very high: Science, with the contingency *manipulated* rather than observed, which is exactly the control that makes the timing claim causal. Mapping fidelity is the constraint at 0.6, entirely because of the timing-versus-typing gap. The aggregate sits below the mean of a naive reading of the components because for an architectural claim like MECH-066 I weight mapping fidelity heavily, and the thing this paper does not show -- source-typed exclusion -- is the specific thing MECH-066 asserts over and above MECH-060.
