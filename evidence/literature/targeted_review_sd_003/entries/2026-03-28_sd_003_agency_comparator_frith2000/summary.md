# Frith, Blakemore & Wolpert (2000) — Summary for SD-003

**Source**: Frith, C.D., Blakemore, S.J., & Wolpert, D.M. (2000). Abnormalities in the awareness and control of action. *Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences*, 355(1404), 1771-1788. DOI: [10.1098/rstb.2000.0734](https://doi.org/10.1098/rstb.2000.0734)

## What the Paper Did

This is a canonical theoretical review from the Wolpert-Frith group synthesising the forward model account of motor awareness and agency. The paper proposes a framework in which the motor system maintains two kinds of internal representations: (1) the current and predicted state of the limbs and body, derived from both sensory signals and efference copies of motor commands; and (2) the intended state, representing the movement the agent planned to make. These representations are served by distinct neural substrates -- parietal cortex for current/predicted state, prefrontal and premotor cortex for intended action. The paper uses this framework to interpret a range of neuropsychiatric phenomena: phantom limbs, anosognosia, utilisation behaviour, and -- most relevantly for SD-003 -- delusions of control.

## Key Findings Relevant to SD-003

The core mechanistic claim is that the sense of agency depends on a forward model comparator. The motor system issues an efference copy of the motor command to a forward model that predicts the expected sensory consequence of the action. A comparator checks this prediction against actual sensory feedback. When predicted and actual match, the sensory event is classified as self-caused. When they diverge, the event is classified as externally caused. This is the computational basis of self-attribution.

The clinical validation is particularly important: patients with schizophrenia who experience delusions of control (passivity phenomena, made movements) report that their own actions feel alien or externally caused. The paper interprets this as a failure of the forward model comparator -- the efference copy is not correctly generating a prediction, so self-produced movements are not recognised as self-caused. This constitutes a natural experiment: disrupting the forward model comparator disrupts self-attribution in exactly the direction SD-003 would predict.

The paper also identifies anosognosia (denial of paralysis) as the complementary failure: patients retain motor command streams but have lost sensory feedback, and experience illusory movement based on motor command streams alone. This suggests the forward model can generate a self-attribution signal even in the absence of sensory feedback -- relevant to SD-003 in low-observation environments.

## Translation to REE / SD-003

SD-003 formalises the Frith-Blakemore-Wolpert framework as a computable operation in the harm-stream latent space: causal_sig = E2_harm_s(z_t, a_actual) - E2_harm_s(z_t, a_cf). E2_harm_s is the REE forward model -- the efference copy maps onto the action input, and the forward model outputs a prediction of the harm-stream consequence. The key innovation SD-003 adds beyond the single-pass comparator described here is the two-pass counterfactual: rather than comparing predicted against observed, SD-003 compares two forward model outputs (actual action and counterfactual action) to isolate what specifically the agent's action caused, independent of what the environment would have produced anyway.

The clinical failure signatures (delusions of control, anosognosia) are the human-level instantiation of what SD-003 is designed to prevent: systematic misattribution of self-caused harm-stream changes to external causes (or vice versa), which would corrupt the agent's causal record and prevent accurate self-evaluation.

## Limitations and Caveats

The paper directly evidences the single-pass comparator (E2(a_actual) - observed), not SD-003's two-pass counterfactual difference. The extension from single-pass to two-pass is theoretically motivated but not empirically grounded in this paper specifically. The biological mechanisms described (parietal-prefrontal circuitry, corollary discharge pathways) abstract over levels of detail not yet instantiated in REE V3. The paper's concern is with bodily movement and motor control; SD-003 operates in a harm-stream latent space whose relationship to proprioceptive/motor signals is indirect.

## Confidence Reasoning

Confidence 0.72. The source quality is very high (Phil Trans Roy Soc B, canonical review, widely cited) and the theoretical claim is exactly the computational principle SD-003 builds on. The moderate confidence reflects the single-pass vs two-pass gap and the domain transfer from motor awareness to harm-stream causal attribution.
