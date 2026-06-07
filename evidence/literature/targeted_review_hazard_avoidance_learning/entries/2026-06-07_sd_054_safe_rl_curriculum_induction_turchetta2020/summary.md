# Safe Reinforcement Learning via Curriculum Induction (Turchetta et al., NeurIPS 2020)

**Claim tested:** SD-054 (scaffolded onboarding curriculum design)
**Direction:** supports | **Confidence:** 0.62

## What the paper did

This is the ML-side leg of the review: the question of what makes hazard-avoidance *learnable as a staged competency* versus failing to train at all. Turchetta and colleagues address safety-critical RL, where "the agent needs to behave safely not only after but also while learning." Their criticism of prior safe-RL is that it leans on priors and smoothness assumptions that do not hold in realistic hazardous domains. Their alternative is explicitly modelled on human teaching: an automatic instructor (a "monitor") that holds a library of reset controllers and activates one whenever the agent starts behaving dangerously, preventing damage during exploration. Crucially, the instructor itself learns -- from watching the agent's progress -- a policy over which reset controller to deploy when. That learned intervention policy *is* the curriculum, and it is optimised for the agent's final reward. They demonstrate the framework inducing curricula for safe and efficient learning in two environments.

## How this translates to REE

The mapping is to the `scaffolded_sd054_onboarding` curriculum design rather than to a biological mechanism. The V3-EXQ-603g probe expected an isolated hazard-avoidance stage to train within budget and it did not. This paper is the ML statement of why that shape recurs: in hazardous domains, an agent left to learn unscaffolded tends not to acquire safe behaviour, because the very mistakes it needs to learn from are the ones that end the episode (or, in REE's case, end survival before competence forms). The fix that works in the ML literature is an external scaffold that intervenes during acquisition and is gradually withdrawn -- which is structurally the same move as the maternal-buffering scaffold in the developmental-biology entries (Debiec & Sullivan 2017). Both supply *protection during acquisition*. For REE this supports redesigning the onboarding as a staged, teacher/reset-scaffolded avoidance curriculum, with the protective intervention annealed as competence grows, rather than as a single unscaffolded survival stage with a larger episode budget.

## Why the confidence is deliberately the lowest in the review

Confidence is 0.62 -- by design the lowest of the five entries. This is a methods analogue, not biological evidence, and not evidence for any REE assertion-claim. The project's biology-before-formal-definitions principle is explicit that a formal/ML construct must not, on its own, drive a substrate mechanism decision; the canonical failures (SD-003, SD-010/011) came from getting the philosophy or the formalism right while the mechanism was wrong. So the role of this paper is bounded: it shows the curriculum *shape* is feasible and constrains the engineering, while the SD-035/MECH-279 biology entries carry the mechanism question. It also sits in the lit channel only -- under the lit/exp decoupling policy it is a parallel sanity-check signal, not a contributor to experimental confidence.

## Limitations and confidence reasoning

The venue is strong (NeurIPS 2020), but the environments are driving-like and gridworld tasks, not REE's foraging-under-hazard substrate, and the reset-controller abstraction may not have a clean REE homologue (REE has no obvious "reset to safe state" operator mid-episode). Mapping fidelity is therefore moderate (0.55) and transfer risk elevated (0.45). The defensible takeaway for the substrate_queue verdict is narrow and specific: *the curriculum-scaffold reading is feasible and is corroborated independently on the ML side*, which is exactly the kind of cross-domain convergence (developmental biology + RL practice) that strengthens confidence in the "staged, scaffolded acquisition" design without licensing any particular mechanism by itself.
