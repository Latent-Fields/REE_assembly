# Dayan & Huys (2008) -- Serotonin, Inhibition, and Negative Mood

## What the Paper Did

Dayan and Huys constructed a computational model in which serotonin acts as a pruning signal
in a decision tree of emotionally valenced thoughts. The model's core idea is that behavioural
and cognitive inhibition -- the capacity to suppress low- or negatively-valued mental trajectories
-- depends on serotonergic tone. When serotonin drops (psychiatrically or experimentally), the
pruning fails: the agent continues mentally exploring aversive branches it would normally terminate.
This generates unexpectedly large negative prediction errors across many time steps, producing a
generalised aversive shift in the agent's reinforcement statistics. The result is a computational
account of sustained negative mood: not a single bad event, but a cascade of ruminated aversive
predictions. The model is elegant in that it explains why serotonin reuptake inhibitors are
antidepressant even though serotonin's primary associations in the learning literature are with
aversive rather than appetitive signals.

## Key Findings and Their Relevance

The paper establishes three things relevant to INV-053. First, it shows that depression can
emerge from a failure of a control signal -- not from aberrant learning of values per se, but
from failure to apply those values as gating criteria. Second, it demonstrates that this failure
has an attractor-like quality: once pruning fails, the cascade of negative prediction errors
self-reinforces. Third, it locates the mechanism at the level of action-sequence evaluation --
the Q-value and inhibitory layer of decision-making. This is the canonical Huys/Dayan lineage
account: depression as failure in value-weighted inhibition of mental search.

## REE Mapping and Architectural Distinction

INV-053 occupies a different architectural layer. The Dayan/Huys account presupposes that the
agent is actively exploring decision trees -- evaluating branches, computing expected values,
and applying inhibitory signals. INV-053 describes the state that obtains when the agent has
stopped entering that process at all. When VALENCE_WANTING terrain is collapsed and z_goal is
absent, there is no approach-goal to generate the decision tree in the first place. The agent
is not failing to prune bad branches; it is not generating branches. This is an earlier, more
upstream failure. The Dayan/Huys model would describe a patient still cognitively active but
ruminative; INV-053 would describe a patient with motivational collapse and psychomotor
retardation -- the state where there is nothing to inhibit because there is nothing being
initiated. These need not be mutually exclusive clinical presentations, but they are
computationally distinct failure modes.

The mapping_caveat in the record.json is therefore load-bearing for the paper: REE's contribution
is to identify terrain/seeding collapse as a distinct, earlier failure mode not captured in the
Huys/Dayan lineage. This entry establishes what INV-053 is arguing against, which is exactly
what is needed to locate the claim's novelty.

## Limitations and Caveats

The model is highly simplified -- chains of affectively valenced "thoughts" rather than a
structured world model or benefit terrain. The serotonin-as-pruning hypothesis, while influential,
has been contested: there are alternative computational interpretations of serotonin's role
(patience, temporal discounting, uncertainty). The paper's contribution is primarily theoretical.
It does not provide behavioural or neuroimaging predictions that directly distinguish its account
from INV-053's. That is precisely why the architectural distinction must be made explicitly in
the REE paper: these mechanisms operate at different levels and neither is derivable from the
other.

## Confidence Reasoning

High source quality (PLoS Computational Biology, Dayan and Huys are two of the most rigorous
theorists in the field). Moderate mapping fidelity because the mechanism is at a different layer.
This entry functions primarily as a contrast case -- it establishes the Q-value lineage against
which INV-053 makes its novel claim -- rather than as direct support or evidence for INV-053.
Confidence 0.62 reflects: strong relevance for positioning, weak direct evidential contribution
to the specific attractor/terrain/seeding claim.
