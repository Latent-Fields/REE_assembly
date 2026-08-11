# Bottary, Sonni, Wright & Spencer (2016) — chunk concatenation and nREM2/spindles

Bottary and colleagues re-analysed an existing motor-sequence-learning dataset (young vs older
adults, a pegboard sequence learned by massed practice, tested before and after a night of
sleep or an equivalent waking interval) at a finer grain than the usual whole-sequence
speed/accuracy score. They separated "chunk formation" — the sub-sequences of fast,
low-variability keypresses that emerge during initial practice, present in both age groups —
from "chunk concatenation": the specific speeding of the *slowest* transitions, the ones
sitting between chunks, which is what makes an already-learned sequence run as one continuous
motion rather than several short bursts separated by hesitations. Young adults showed
sleep-dependent concatenation, correlated with sigma-band (spindle) power during nREM2. Older
adults did not — sleep protected their existing performance from daytime interference, but did
not actively speed the between-chunk transitions the way it did in young adults, and this
group difference tracked reduced nREM2 spindle activity with age.

For MECH-490 this is the closest thing in the literature to the exact distinction the claim
needs. REE's E3 commitment-gate hypothesis is explicitly *not* about forming new action chunks
(that is ARC-071's territory, already grounded in the striatal-chunking literature cited in
`policy_chunking.py`) — it is about whether an *already-planned* sequence gets executed with
fewer per-tick re-decisions once committed. Bottary et al. give real behavioural evidence that
this is a separable process from chunk formation, with its own separable sleep-stage signature.
And that signature is nREM2/spindles, not REM — which bears directly on the claim's `depends_on`
question about MECH-204: if a coherence-persistence effect like MECH-490's is real and follows
this biological precedent, MECH-204's REM-phase precision-recalibration route is probably the
wrong substrate to eventually re-enable for it. A spindle/SWS-linked route, which the Fishtank
substrate does not currently model at all, would be the biologically closer candidate.

The mapping is not free of risk. Bottary et al. measure transition *speed* at fixed accuracy in
a rote, externally-imposed, once-learned sequence; E3Selector's commit-gate operates on an
agent's own online-generated action plan in a continuously changing environment, and "faster
transition between two already-known chunks" is not the same variable as "lower commit-variance,
fewer re-scoring events." Treating the two as instances of the same underlying phenomenon —
reduced within-run internal interruption — is a translation REE is making, not a claim the paper
makes about REE. The design is also correlational (EEG power correlated with behavioural change
within a sleep-vs-wake groups comparison), not a causal spindle-suppression manipulation, so the
sigma-power-drives-concatenation link itself carries the usual correlational caveats. Held at
0.72: solid direct precedent for the formation-vs-fluency distinction and for the
stage-specificity question, moderate risk on how cleanly it maps onto the specific commit-gate
variable REE proposes.
