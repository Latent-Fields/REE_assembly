# Harm deforms the map only if the harm is remembered

Blair and colleagues imaged CA1 place cells with a head-mounted miniscope in fourteen freely behaving
rats. The animals first learned a path preference for food reward, and then received mild footshock on
the preferred path, so that the aversive event was localised to a known stretch of the animal's own
established route. The design's real move is the scopolamine arm: some rats received the anticholinergic
before the shock, which leaves the shock fully perceived but blocks its encoding into memory. The
question then becomes whether the map reorganises because a shock *happened* or because a shock was
*retained*.

The answer is the retained one. Place cells remapped significantly more following remembered than
following forgotten shocks, and the degree of remapping tracked memory formation rather than the
sensory event. A control condition inserting a neutral barrier — a change in the path's affordances
without aversive content — produced significantly less remapping than shock did.

I find this the single most useful entry in this pull, because it does not merely show that harm
history changes a cognitive map; it shows the change is gated on commitment to memory. REE has already
made that gating an architectural commitment rather than an empirical hope: `ResidueField.accumulate`
carries the MECH-094 hypothesis-tag refusal, so simulated or replayed content is not permitted to
deform the residue geometry. The scopolamine arm is the biological version of that refusal, obtained
pharmacologically rather than by tagging. A shock the animal cannot encode is, as far as the map is
concerned, a shock that did not happen. That is the structure MECH-023's third CONFIRMING criterion
asks for — hypothesis-tagged harm must not produce the divergence — arriving from an independent
direction.

Two things this does not establish, and they matter for how the REE experiment is designed. First, the
remapping is representational; the paper reports it alongside behaviour but does not show that the map
change *causes* the subsequent avoidance. A REE run that produced residue-driven rank divergence with
no downstream behavioural consequence would be in the same evidential position, and should be reported
as such rather than as a clean confirmation. Second, and more practically: the neutral-barrier control
produced *less* remapping, not *no* remapping. Changing what a state affords perturbs the map on its
own. The MECH-023 design's B fork — a harm-free path of equal length — therefore needs to be matched on
affordance change and not merely on path length, or the identical-history noise baseline is being
estimated against the wrong null and criterion (i) will look easier to pass than it is.

The honest limit on the scopolamine dissociation is that it separates remembered from forgotten, not
harm from non-harm. Systemic anticholinergic blockade impairs encoding broadly; it does not isolate a
harm-specific accumulation channel. So the paper licenses "the map deforms only for events that are
committed to memory" and not "there is a dedicated pathway by which harm in particular accumulates".
REE asserts the stronger version. That gap is the reason mapping fidelity is 0.78 rather than higher.

Confidence 0.8. Good preparation, adequate n, a within-subject design and a genuinely informative
pharmacological control, published in eLife. The transfer risk is the usual rodent-spatial-to-latent-space
one, mitigated by the fact that REE's residue field is explicitly an analogue of this system rather than
a coincidental resemblance.
