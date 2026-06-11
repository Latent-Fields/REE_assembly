# Mongillo, Barak & Tsodyks (2008) — Synaptic theory of working memory

**Claim:** ARC-063 (CandidateRule field with tolerance-gated availability). **Direction:** supports (fork-B mechanism; the directly implementable one). **Confidence:** 0.78.

## What the paper did

Mongillo and colleagues built a spiking recurrent-network model of neocortex equipped with short-term synaptic plasticity (Tsodyks–Markram facilitation) and showed that working memory can be sustained **without persistent spiking**. The mechanism: when a population fires, presynaptic residual calcium accumulates and transiently raises release probability on the recently-active recurrent synapses. This leaves a *memory trace in the synaptic weights* that persists for roughly a second after the neurons fall silent. Because calcium kinetics are slow, the trace needs only occasional, sparse, low-rate spikes to refresh — making the mechanism metabolically cheap and robust to distraction — and it is read back out when the network is next probed. With stronger facilitation the same model produces spontaneous reactivation *bursts* rather than tonic firing. This is the decisive mechanistic model for fork B, and crucially it is the most directly *implementable* one for a software substrate.

## Why it is the implementation anchor for the CRF fix

The CRF's maintenance bug is precise: `availability` is an activity-dependent EMA that decays every tick (`mature_availability_decay`) and is only refreshed on match, so a differentiated rule that matches sparsely erodes toward the retire floor between matches. Mongillo describes *exactly* the primitive that fixes this. The maintenance substrate should be a **synaptic-trace-like availability** that:

1. **persists across context-absent ticks without the rule firing** — the trace lives in the "synapse," not in ongoing activity;
2. **decays on a long, deliberately-set horizon** rather than per-tick — slow, like calcium kinetics, so the gap between sparse matches is survivable;
3. **is refreshed by sparse matches** rather than requiring continuous activity — Mongillo's "occasional refresh at a low rate" *is* the CRF's sparse-match regime.

The fit is close to one-to-one: a differentiated rule that matches rarely is precisely the case synaptic facilitation was conceived to handle. The model also supplies the optional bridge to fork A — strong facilitation yields reactivation bursts — which is how the engaged rule can transiently "fire" (Funahashi/Compte) on top of a silently-maintained pool.

## The one thing not to import

The biological time constant is ~1 s, set by calcium kinetics. The CRF must keep a rule available across roughly 2000–3900 ticks — far longer than the biological window. So the transferable content is the **mechanism class** (silent, slowly-decaying, sparsely-refreshable, activity-decoupled maintenance), not the numeric constant. The CRF's maintenance horizon is a free design parameter to be set so a differentiated rule survives its typical inter-match gap; biology motivates the *form* of the term, not its value. The paper itself flags the complementary risk: facilitation is capacity- and interference-limited, so maintenance is not free and unbounded. The CRF's differentiated, pinned-distinct directions are the favourable (low-interference) case, but the term should still degrade gracefully under load rather than holding everything forever.

## Confidence reasoning

Foundational high-impact model (Science) — strong source quality. Mapping fidelity is high (0.80) because the mechanism is a near-exact fit to the availability-maintenance primitive the CRF needs. Transfer risk is low-moderate; the only genuine hazard is naively importing the ~1 s constant, which the caveat isolates. Together with Stokes (2015) and Lundqvist (2018), this paper moves the fork verdict decisively toward B for the *pool*, while leaving fork A as the mechanism for the *engaged* rule.
