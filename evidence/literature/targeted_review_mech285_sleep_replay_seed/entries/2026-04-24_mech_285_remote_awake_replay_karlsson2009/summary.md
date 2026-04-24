# Karlsson & Frank 2009 -- awake replay reaches remote environments

## What the paper did

Rats were trained across multiple spatial environments. The authors recorded CA1 place cells and asked whether awake replay events during brief behavioural pauses were exclusively drawn from the animal's current environment, or whether they also depicted trajectories through environments the animal was not currently in.

## Key findings relevant to MECH-285

Remote (non-current) replay was as frequent as local (current) replay. The seed pool for awake SWR content includes stored representations from environments outside current sensory context. A secondary finding: remote replay was more robust during pauses that followed recent motion than during extended quiescence, suggesting a movement-triggered or arousal-coupled component to the broadening.

## Translation to REE

For MECH-285 this is one of the strongest single pieces of evidence that the seed distribution is structurally broad. The architectural commitment would be to persist a region-to-seed map across `AnchorSet.mark_inactive`: inactive anchors must remain in the pool for sampling, because the biology clearly samples from them. A strict narrow-reading implementation, in which only currently-active anchors can seed replay, would fail to reproduce the basic Karlsson & Frank phenomenology.

The caveat is worth sitting with. Karlsson & Frank find that remote replay is *more* robust during active pauses and *less* robust during extended quiescence. This is the opposite of what a naive sleep-regime reading would predict -- a sustained offline state with broad staleness-weighted sampling. One resolution: remote replay in awake pauses may serve decision-support / retrieval functions (cf. Gillespie 2021, Joo & Frank 2018), while sleep remote replay serves consolidation / schema-revision. Both exist, but the balance between them may shift with state. MECH-285's commitment is to the sleep-regime function specifically; Karlsson & Frank provide strong evidence that the *substrate* for broad seeding exists, without pinning down the priority weights during deep sleep.

## Limitations and caveats

The paper studies waking behaviour, not sleep. Its "remote replay is more robust during recent-motion pauses" finding complicates a direct MECH-285 mapping -- the broadening mechanism seems tied to arousal/motor-coupling rather than to pure offline schema work. Interpreting this for sleep replay requires assuming that the sleep regime inherits the broad-pool substrate, which is a reasonable but not directly tested assumption.

## Confidence reasoning

A canonical, well-replicated foundational result. Source quality high. Mapping fidelity high for the broad-vs-narrow seed-coverage question. Transfer risk is moderate; the awake-vs-sleep gap is the main hazard. Aggregate confidence 0.78.
