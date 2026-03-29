# Summary: Wolpert, Miall & Kawato (1998) — Internal Models in the Cerebellum

**Entry ID:** 2026-03-29_mech_135_mosaic_parallel_forward_models_wolpert1998
**Claim tested:** MECH-135 (planning.e1_e2_parallel_rollout)

---

## What the paper did

Wolpert, Miall, and Kawato wrote a synthetic theoretical review in *Trends in Cognitive Sciences* (1998) proposing that the cerebellum contains internal models of the motor apparatus. The paper distinguishes two types: inverse models, which compute the motor command needed to achieve a desired trajectory, and forward models, which predict the sensory consequences of a given motor command. The central contribution is a computational architecture -- later formalized as MOSAIC (Modular Selection and Identification for Control) -- in which *multiple* paired forward and inverse models operate in parallel. Each forward model predicts the state given the current action, and responsibility estimates based on prediction error gate each model's contribution to the final output. The biological grounding draws on the ocular following response and arm movement adaptation data to argue that the cerebellum is a plausible anatomical substrate for both types of model.

## Key findings

The MOSAIC architecture requires that all forward models run simultaneously during action generation and evaluation. No single model has priority; rather, the ensemble contributes proportionally to its current prediction accuracy. This is a structural argument for parallelism: the cerebellar forward models do not take turns. A second key claim is that forward models overcome the feedback delay problem -- because sensory feedback arrives too slowly to correct fast movements, a forward model running ahead of sensory reality provides a prediction of current state that allows real-time error correction. This time-delay bypass argument is central: it implies that the forward model (E2 in REE terms) must be temporally coupled to the evolving state of the system rather than being a one-shot pre-computation.

## REE translation

The MOSAIC parallel forward model architecture maps directly onto the claim in MECH-135 that E2 must run *alongside* E1 rather than sequentially. In the REE framing, E2 (cerebellar-like, z_self latent) is the fast forward predictor, and E1 (cortical, z_world latent) is the slower world model. Wolpert et al.'s argument that forward models must run in parallel to supply timely state predictions is a biological precedent for the architectural choice MECH-135 defends. The responsibility-gating mechanism also suggests a candidate basis for how E2 output could modulate trajectory selection: modules with lower prediction error (more confident E2 rollouts) would contribute more to the final trajectory estimate.

## Limitations and caveats

The gap between what MOSAIC demonstrates and what MECH-135 requires is worth stating plainly. MOSAIC's forward models all operate within a fixed context -- the cortical world-state is an input to the responsibility estimators, not a variable being jointly updated. MECH-135 claims that z_world (E1's representation) *co-evolves* during the E2 rollout -- that the two latents are mutually updating, not that one is frozen while the other runs. MOSAIC does not address this stronger coupling. Additionally, the paper is firmly in the motor domain; the extension to cognitive planning and trajectory evaluation over longer time horizons is not demonstrated here (though it is speculated about in the companion Wolpert & Kawato 1998 Neural Networks paper). These are not reasons to discount the paper as evidence, but they mark the precise inferential step that MECH-135 requires beyond what MOSAIC provides.

## Confidence reasoning

This is a landmark theoretical paper with strong citation history and solid biological anchoring in motor data. The parallel architecture claim is well-established. The confidence of 0.72 reflects the strength of the parallel structure evidence relative to the gap on co-evolution. A reader who found the co-evolution claim already plausible on other grounds would treat this paper as strong corroborating support; a skeptic of co-evolution would note that MOSAIC is compatible with a fixed-context architecture and therefore does not compel the MECH-135 interpretation.
