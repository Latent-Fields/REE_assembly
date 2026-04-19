# Seymour 2019 — Pain: A Precision Signal for Reinforcement Learning and Control

**Source:** *Neuron*, [10.1016/j.neuron.2019.01.055](https://doi.org/10.1016/j.neuron.2019.01.055). Via PubMed (PMID 30897355).

## What the paper does

Seymour -- long the lead computational researcher on pain -- reframes pain away from "aversive scalar" and toward "precision-weighted control signal in a Bayesian active-inference / reinforcement-learning framework". The paper argues that the behavioural response to nociception is not a simple function of pain magnitude, but depends on how much precision (inverse-variance weighting) the organism assigns to the pain prediction error. High-precision pain drives large, committed behavioural adjustment; low-precision pain is down-weighted or absorbed. This framework integrates affective/sensory dual streams (Price, Craig), ACC integration (Shackman), and ACC-striatal value coupling (Baliki) into a coherent computational model.

## Key findings relevant to the claim

- **Pain as control signal, not just valence.** The primary function of pain in decision making is to drive policy updates, not to produce a hedonic score. This reframing matters: "how aversive is this?" is secondary to "how much should this reshape my behaviour?"
- **Precision weighting.** The behavioural impact of a pain signal is modulated by its precision -- expected, predictable, controllable pain has lower precision (lower impact on policy); unexpected, uncontrollable pain has higher precision (large impact).
- **Active-inference framing.** Pain is treated as a prediction error against an internal pain model. Minimizing expected pain prediction error is a control objective -- the agent plans actions that reduce anticipated pain-surprise, not that minimize a scalar pain cost.
- **Integration with cingulate/insular substrate.** Seymour ties this directly to the anatomy: AIC generates pain prediction errors from interoception, ACC/aMCC integrates them with other control demands, striatum stores and updates the action-value target.
- **Clinical relevance.** Chronic pain, placebo, and psychiatric-pain comorbidities all fit naturally as precision/predictability disturbances rather than magnitude disturbances.

## How this maps onto REE (the translation)

This paper gives the *computational form* the cingulate substrate should implement. The implications for ree-v3 are tight:

1. **z_harm_a should not enter action selection as a raw magnitude.** It should enter as a precision-weighted prediction error against an internal pain model. This is exactly what SD-020 (harm_surprise_PE, currently provisional) aims to compute. Seymour's framework elevates SD-020 from "useful refinement" to "prerequisite for the cingulate substrate to work biologically."

2. **Precision weighting is the 'adaptive control' function Shackman 2011 proposed.** Shackman said dACC integrates affect with control demand to produce adjustment magnitude. Seymour specifies what that integration computes: precision-weighted prediction error on the pain forward model. The two papers together give the dACC-analog a complete specification: inputs = (z_harm_a PE, precision estimate, control demand); output = policy update magnitude.

3. **Requires a pain forward model.** To compute prediction error, ree-v3 needs an E2-analog for affective pain -- an E2_harm_a module that forecasts expected z_harm_a given the current trajectory. This is architecturally parallel to the E2_harm_s proposed in ARC-033 for SD-003 counterfactual redesign. A clean design would unify them: E2_harm_s (sensory pain forecast) + E2_harm_a (affective pain forecast) computed on the same substrate but reading different input channels.

4. **Binds Options A/B/C into one framework.** In Seymour's terms:
   - Option B (forward-rollout affective cost) is *prerequisite*: there is no precision-weighted PE without a forward model. Must be built first.
   - Option A (dACC integration into action value) is what the cingulate substrate computes *given* Option B's forward model.
   - Option C (AIC urgency-interrupt) is what happens when precision exceeds an interrupt threshold -- it's the escape hatch from the smooth RL update into network switching, as described in Craig/Menon. It fires when the current trajectory is being invalidated faster than smooth updates can keep up.

   So all three are real, in a specific sequence: forward model -> precision-weighted PE -> RL update if below threshold OR network switch if above.

## Limitations and caveats

Seymour's framework is prescriptive. Adopting it commits ree-v3 to implementing a pain forward model, a precision estimate, and a joint prediction-error + control-demand integration -- substantial downstream substrate work that goes beyond the original "wire up z_harm_a" framing. The framing is clean but expensive, and there is a legitimate minimal-implementation path that just gets z_harm_a into some consumer without full precision weighting. The cost-benefit of the full framework depends on whether ree-v3 can afford the forward-model substrate now or whether a simpler bridge is needed first.

The framework is also theoretical rather than empirical in this review -- Seymour cites empirical support but the review itself synthesises and proposes rather than demonstrating new findings. Empirical tests of the precision-weighted framing in human decision making exist (Seymour's own lab has run them) but are not this paper's main contribution.

Transfer risk: moderate. The computational framing is already in ree-v3's native vocabulary (prediction errors, precision, forward models, active inference), so translation is direct. The main risk is over-commitment -- adopting the full Bayesian framing may impose structure that is harder to validate than it is to write.

## Confidence reasoning

0.82. This is the computational-framing capstone of the pull. High source quality (Neuron review by the field's lead Bayesian-pain researcher). High mapping fidelity because the framework speaks ree-v3's vocabulary directly. The discount is for transfer risk (adopting the framework commits us to expensive downstream work) and for the fact that the framework's empirical support is distributed across many studies rather than concentrated in this single paper. Still, as a scoping input for the new SD cluster, this paper is close to essential.
