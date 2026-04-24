# Santos-Pata, Barry & Olafsdottir (2023) -- "Theta-band phase locking during encoding leads to coordinated entorhinal-hippocampal replay"

**Current Biology** 33(21):4570-4581.e5. [DOI](https://doi.org/10.1016/j.cub.2023.09.011). PMID 37776862.

*(According to PubMed.)*

## What the paper does

Santos-Pata and colleagues ask a question that sits between the online encoding and offline replay literatures: during movement-based encoding, which dMEC (deep medial entorhinal cortex) cells are locked to hippocampal theta LFP, and does that online lock predict participation in subsequent CA1 replay? The design uses simultaneous CA1 and dMEC recordings in rats acquiring a novel spatial task, so the experience-dependence of the synchrony can be tracked across training. Theta-phase-locking during movement is characterised per dMEC cell; participation in coordinated CA1 replay during offline epochs is measured separately; the two are then cross-referenced.

The headline findings are three. First, the dMEC cells that are theta-locked during movement are disproportionately the ones that participate in coordinated CA1 replay during subsequent offline periods. Second, dMEC synchrony with CA1 replay peaks about 10 ms after CA1 replay initiation, suggesting that replay is initiated in CA1 and then propagates to extra-hippocampal structures -- which matches the standard story of hippocampus as initiator. Third, the synchrony grows with experience, mirroring task acquisition rather than being a fixed anatomical property.

## Findings relevant to MECH-269

MECH-269's anchor-selection mechanism depends on MECH-089 (theta-gamma nesting): the per-cycle summary that the proposer's V_s signal is computed against is theta-cycle-averaged, not instantaneous. For that design to make biological sense, theta-phase-locking needs to be the mechanism that selects which cellular ensembles' activity actually participates in replay content. Santos-Pata et al. are the direct test of this, and they find it to be the case.

The experience-dependent growth of the dMEC-CA1 synchrony is the additional piece that tightens the match. V_s in MECH-269 is a running alignment score: the more the agent's predictions have been realised in this region of latent space, the higher V_s is and the more anchor-eligible that stream becomes. A purely static anatomical locking pattern would fit MECH-269 less well than a learning-sensitive one. Santos-Pata et al. show that the locking is learning-sensitive, which is the match MECH-269 needs.

## How it translates to REE

The architectural lesson for REE is that theta-phase-locked ensemble selection is the pre-REE machinery that MECH-089 / MECH-269 inherit. The V3 substrate implementation of V_s should consume theta-cycle-averaged stream summaries rather than instantaneous latents, and it should treat theta-phase-locked ensemble participation as the equivalent of "this stream's evidence for anchor eligibility." The CA1-initiating / dMEC-following latency of 10 ms -- small relative to theta-cycle duration -- also suggests that the per-cycle summary the proposer consumes is already the result of hippocampal-initiated coordination propagating outward, rather than an independent computation per downstream region.

For REE's streams specifically, the translation requires the additional commitment that theta-phase-locked encoding ensembles carry stream-local content (z_world, z_harm_s, z_goal, z_self). Santos-Pata et al. do not prove this; their analysis is at the level of spatial-task cell assemblies rather than REE streams. The paper supports the architectural role of theta-phase-locking in selecting replay participants; it does not validate the stream-local decomposition MECH-269 commits to.

## Limitations and caveats

The task is spatial acquisition in rat. The content being coordinated is place-cell-adjacent, not REE streams; the mapping from place-cell assemblies to z_world / z_harm_s / z_goal requires the REE-side commitment that biological content-typed subpopulations correspond to REE streams. Harvey et al. 2023 (already entered under MECH-271) provides some support for cellular-level content-typing in CA1; Santos-Pata et al. provide the theta-phase-locking selection mechanism. The two papers together establish a plausible substrate for stream-local selective replay participation without directly testing it.

The latency result (dMEC follows CA1 by ~10 ms) may complicate MECH-269's per-stream V_s computation. If V_s for z_world needs dMEC content to compute against, and dMEC content is only available ~10 ms after CA1 replay initiation, the readout is slightly delayed. Whether this matters for anchor selection depends on the cycle time of the proposer, which is a V3-substrate parameter not yet fixed.

## Confidence reasoning

Source quality is high: Current Biology, Olafsdottir as senior author (her 2018 review is already in the MECH-269 evidence set), rigorous simultaneous dMEC-CA1 electrophysiology with experience-dependent analysis. Mapping fidelity is 0.70 -- the paper directly supports the theta-phase-locking architecture MECH-269 depends on via MECH-089, and the experience-dependence matches V_s's running-alignment character. Transfer risk is 0.30 -- moderate -- because the architectural lesson transfers but the REE-specific stream-local commitment is an extrapolation the paper cannot directly validate. Overall confidence 0.74 -- this should be cited as support for the MECH-089/MECH-269 link (theta-phase-locking as the selection mechanism for replay participation) and for the learning-sensitivity of V_s-like signals.
