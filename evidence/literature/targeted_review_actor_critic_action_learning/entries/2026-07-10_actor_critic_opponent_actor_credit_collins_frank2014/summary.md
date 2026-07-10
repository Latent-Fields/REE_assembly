# Collins & Frank (2014) — Opponent actor learning (OpAL)

*According to PubMed. [DOI: 10.1037/a0037015](https://doi.org/10.1037/a0037015). Psychological Review 121(3):337-66.*

## What the paper did

OpAL takes the classical actor-critic and opens up the actor. Where the standard model has a single actor storing action values, Collins & Frank split it into a **dual opponent-actor system**: two striatal populations mapping onto the D1/direct/"Go" pathway and the D2/indirect/"NoGo" pathway, which come to specialize respectively in discriminating *positive* and *negative* action values. Dopamine sets the gain on each channel, and — this is the paper's punchline — that single move lets one framework capture effects the standard actor-critic cannot hold together: dopamine's influence on learning, on effort/choice-incentive, and on motor-skill acquisition, *and their interactions*, across probabilistic RL, effort-based choice, and skill-learning studies.

## Why it matters for the translation gap

Schultz gives REE the teaching signal, O'Doherty gives the actor-critic split across substrates, and OpAL fills in the *credit-assignment internals* of the dorsal-striatal actor the V3-EXQ-724 autopsy pointed to. I read two imports here, and the ranking matters more than either import alone:

1. **Load-bearing:** OpAL is built *on* the actor-critic scaffold. An actor is a first-class learner with its own value-baseline critic — reinforcing, from the computational-modeling side, that biological action learning is not a bias term riding on a prediction model. This is the same thesis as the neuro anchors, now stated in an algorithm that has been fit quantitatively to behaviour.

2. **Second-order:** the actor itself can be an *opponent pair* (Go/NoGo, direct/indirect), so positive and negative action-value credit are assigned on separable channels rather than a single signed value.

The governance-relevant recommendation falls straight out of that ranking. The owed `f_dominance_conversion_ceiling` build should be a **single actor + critic first** — which is exactly what V3-EXQ-737 tests — and should treat the opponent-actor split as a *later* enrichment, reached for only if single-actor credit assignment proves insufficient. This is not timidity; it is the explicit lesson of the cognitive-architecture graveyard doc (WS-8): structure ahead of capability is how Soar and ACT-R ossified. OpAL is the right paper to know about *before* building, precisely so the D1/D2 elaboration is a deliberate later choice rather than a default.

## Limitations and honest caveats

The opponent-actor machinery is more architecture than REE's minimal build needs, and importing it prematurely would re-instantiate the over-elaboration anti-pattern. OpAL is also a model *of dopamine's behavioural and pharmacological signatures* — it explains probabilistic-RL and effort-choice data — not a demonstration that an artificial agent *needs* opponent actors to forage. So it motivates the internal structure of the actor; it does not prove REE requires that structure to clear the competence floor. Finally, OpAL leans on dopamine as a **shared gain term** across both actor channels — a single modulator — which sits in some tension with REE's incommensurable-channels commitment (ARC-021/MECH-069) if imported literally rather than as role.

## Confidence

**0.74, supports.** High source quality (Psychological Review, the canonical striatal-RL modeling lab). I hold mapping fidelity at 0.68 and transfer risk at 0.40 deliberately: the actor-critic backbone imports cleanly and directly supports the "action is a first-class learner" thesis, but the opponent-actor refinement is beyond the minimal owed build and could mislead toward premature elaboration if treated as the target rather than an option. Its real value to this pull is scoping — it tells us how far the dorsal-striatal actor *can* be developed, so the first build can honestly stop short of it.
