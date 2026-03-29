# Stephan et al. (2016) -- Allostatic self-efficacy: a metacognitive theory of dyshomeostasis-induced fatigue and depression

**Claim tested:** Q-021 (does pure harm-avoidance training produce behavioral flatness?)

## What the paper did

Stephan and colleagues developed a hierarchical Bayesian framework connecting interoceptive inference, allostatic regulation, and psychopathology. Their key move is to treat homeostatic regulation as a problem of Bayesian inference over bodily states, and then to add a metacognitive layer: the brain does not just regulate homeostasis, it also maintains beliefs about how well it is doing at regulating homeostasis (allostatic self-efficacy). When chronic dyshomeostasis causes repeated prediction errors that cannot be corrected by standard allostatic responses, the metacognitive layer updates toward low self-efficacy: the belief that regulatory actions will fail. Under low self-efficacy, the agent reduces effortful approach behaviors -- why expend effort if you believe it will not restore homeostasis? The resulting behavioral profile is fatigue and depression: withdrawal from goal pursuit, reduced initiation, quiescent policy.

## Key findings relevant to Q-021

The mechanism described is a clinical analog of Q-021's Pathway A (drive absence route to behavioral flatness). The paper predicts that behavioral flatness (fatigue, depression, reduced initiation) emerges from drive system failure -- specifically from a failure of the belief that approach actions will successfully reduce drive. In REE's terms, this corresponds to an agent that has no positive signal telling it that actions can bring it closer to a goal state. The self-efficacy failure produces the same behavioral signature as absent goal representation: the agent stops initiating, stops exploring, converges on the minimum-action policy.

The positive feedback loop is also architecturally important: behavioral avoidance prevents disconfirming evidence (approach actions that would show the agent it can reduce drive), which maintains or worsens the low-self-efficacy belief, which further reduces approach. This is a stable attractor -- behavioral flatness is not transient but self-maintaining. For Q-021, this predicts that pure harm-avoidance training does not merely produce flat behavior during training, but locks in a stable quiescent attractor that persists even if the architecture is subsequently changed.

## REE translation

Q-021 asks whether training with only harm-avoidance signals produces behavioral flatness. Stephan et al. provide the clinical model of how this happens biologically: when the drive/approach system fails to generate updating signals (equivalent to no approach signal in training), the agent's metacognitive model of its own efficacy degrades, and the resulting behavioral policy converges on non-action. In REE, the pure harm-avoidance training regime is analogous to a regime where benefit_eval_head produces no signal (or is weighted to zero) -- the agent never learns that approach actions reduce drive or move toward goals. The optimal policy under pure harm avoidance is the minimum-action policy (quiescence minimises harm exposure). Stephan et al. show that in biological systems, this policy is not just locally optimal -- it becomes a stable attractor via the self-efficacy feedback loop.

The paper is also relevant to Q-021's two-pathway analysis. Pathway A (drive absence) is the direct analog of the Stephan framework: absent drive signal produces behavioral flatness. Pathway B (D_eff/MECH-113) may also have a Stephan analog: high D_eff (self-model incoherence) could be interpreted as equivalent to low allostatic self-efficacy -- the agent's model of its own capacity to act effectively is disrupted, causing commitment suppression even when drive is present.

## Limitations and caveats

Stephan et al. 2016 is a theoretical framework paper, not an experimental study. The Bayesian framing is not native to REE's gradient descent training, and the self-efficacy mechanism (a metacognitive belief layer) has no direct architectural analog in current REE. The clinical subjects (depressed and fatigued patients) may differ from a trained agent in ways that matter: human fatigue involves neuroimmune, endocrine, and motivational systems that interact in complex ways not present in REE. The framework also blurs together homeostatic failure (the drive signal is disrupted) and belief failure (the agent believes it cannot restore homeostasis), which are architecturally distinct in REE.

## Confidence reasoning

Confidence is 0.73. The framework provides a compelling clinical narrative for how behavioral flatness emerges from drive system failure, which maps to Q-021's Pathway A. The theoretical framing is compatible with Q-021's predictions but requires substantial translation from the active inference framework to REE's training regime question. Confidence is moderate because the paper is theoretical, the mechanism differs from REE's training regime, and the connection requires conceptual bridging.
