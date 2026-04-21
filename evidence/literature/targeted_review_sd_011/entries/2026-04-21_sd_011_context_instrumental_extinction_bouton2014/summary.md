# Bouton & Todd (2014) — A fundamental role for context in instrumental learning and extinction

## What the paper does

Bouton and Todd review roughly two decades of experimental work — most of it from Bouton's own lab — on how physical context modulates instrumental (operant) learning and extinction in rats. They establish that extinction of a lever-press response in context B does not erase the original A-context learning; instead, the animal learns a context-specific inhibitory relation, and the original response renews when the animal is placed back in A (ABA renewal), in a novel context C (ABC renewal), or even in the extinction context after a delay (AAB renewal). They also show that context modulates instrumental behaviour before extinction — a plain context switch after acquisition causes a response decrement — which they argue supports direct context-response associations and sometimes a hierarchical context/(response-reinforcer) representation.

## Key findings relevant to SD-011 context-stability

This is the closest available proxy for the canonical Bouton 2004 "context-and-state" paper. The central result for SD-011 is: learned affective/motivational relations are not context-free. If I train an animal that context A is dangerous (punished) and extinguish in B, the danger representation does not generalise cleanly — it renews when I put the animal back in A. Whatever cortical stream encodes the motivational consequences of harm, its behavioural expression is gated by context-response associations.

Mapped onto SD-011: z_harm_a's role as a motivational/urgency signal consumed by E3 is precisely the kind of learned affective relation that Bouton's framework predicts should be context-bound. The behavioural meaning of "this context is dangerous" is a context-response inhibitory binding, not a context-free scalar. z_harm_s's role is different — it is a forward-predictable mapping from action to proximity (a physical regularity), and should therefore be much less context-bound.

So the context-stability question gets a split answer. The architectural dual-stream (z_harm_s + z_harm_a) is not what is at stake in Bouton's work. What is at stake is whether the downstream consumers of z_harm_a must implement context-specific learning. Bouton says yes, unambiguously. For SD-011 this is a calibration signal for how E3 uses z_harm_a rather than a challenge to the dual-stream architecture itself.

## How this translates to REE

The translation is a design constraint on E3's consumption of z_harm_a: harm-avoidance behaviour should be encoded as context-response bindings rather than as context-free valuations. In V3 implementation terms, if ARC-016 harm-variance gating modulates E3's behavioural output based on sustained threat, the modulation weights themselves should be context-gated — a fresh context should not inherit full avoidance strength from a previously-learned dangerous context. This is testable: after training avoidance in one gridworld configuration, changing the context should produce partial renewal on return, not clean generalisation.

z_harm_s as a physical-regularity representation should be more context-stable by construction. The E2_harm_s forward model predicts z_harm_s from action; as long as physical stimulus-proximity regularities hold across contexts (the harm source is still in the same spatial position relative to the agent), z_harm_s's encoding should transfer. This is compatible with SD-003 counterfactual attribution relying on E2_harm_s — if the forward model were context-bound, counterfactual attribution would fail under context shift.

## Limitations and caveats

The mapping from operant conditioning with distinct physical chambers to REE's dual-stream nociceptive architecture is inferential. Bouton's paradigm uses explicit context manipulations (chamber changes with distinct wall patterns, odours, tactile surfaces) while REE's context shifts are typically environment perturbations. Whether these are analogous enough that Bouton's framework transfers is not obvious. The paper also does not directly measure any nociceptive stream — the mapping is at the level of "learned affective relations are context-bound," which the paper establishes robustly for operant behaviour generally.

## Confidence reasoning

I put this at 0.60 — solid but not high. The general principle (affective/motivational learning is context-specific) is well-established across species and paradigms, so it transfers in its general form. But the specific mapping to z_harm_a consumers in E3 is inferential and requires several interpretive steps. The paper's contribution to SD-011 is a design constraint on the downstream consumer, not a direct validation or refutation of the dual-stream architecture. Honest reading: Bouton's framework is compatible with SD-011, licenses a sharper implementation of E3's z_harm_a consumption, and provides a failure prediction (absence of renewal effects in V3 avoidance tasks would weaken the claim).
