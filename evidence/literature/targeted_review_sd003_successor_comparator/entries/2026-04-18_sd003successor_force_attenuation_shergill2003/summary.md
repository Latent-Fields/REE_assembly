# Shergill, Bays, Frith & Wolpert (2003) -- Two Eyes for an Eye: The Neuroscience of Force Escalation

## What the paper did

Shergill and colleagues designed a force-matching task to quantify how much the brain attenuates its own self-generated sensations. Pairs of participants had their left index fingers resting in moulded supports attached via a torque motor to a lightweight lever. A target force was delivered to the left finger, and the participant had to reproduce that force either directly (pressing on the lever with their right index finger, so the reproduction was self-generated) or indirectly (adjusting a joystick that controlled the torque motor, so the reproduction was externally generated). The paradigm is elegant because the physics of the two reproduction routes are identical; only the self-generated nature differs.

## Key findings relevant to an SD-003 successor

In the direct condition, participants systematically over-produced force. To match a target, they had to press harder than the target dictated, because their own pressing felt weaker than it was. In the indirect (joystick) condition, reproduction was close to accurate. The attenuation is quantified: the direct condition showed an intercept increase of about 0.53 N and a slope increase of about 49% relative to indirect. Translated: when you generate a force yourself, you feel it as roughly half its true magnitude.

The authors interpret this as direct behavioural evidence for a forward-model / comparator mechanism. The motor command to press generates an efference copy, which predicts the expected reafferent force sensation, which is then subtracted from the actual sensation. The residual is what the subject feels. In the joystick condition, there is no efference copy for the right hand's force output on the left finger (the output is mediated by a motor, not by the right hand), so no subtraction occurs, and perception is accurate.

## Translation to ARC-033 and the SD-003 successor

This paper speaks to the comparator-residual half of the single-pass architecture. It says: when E2_harm_s produces a z_harm_s_pred and the observed z_harm_s matches, the observed signal should be suppressed in perception. When the observed z_harm_s does not match (externally generated), it should pass through at full magnitude. The magnitude of attenuation in Shergill 2003 -- roughly 50% -- sets an experimental target: a validation experiment for the REE successor should show an analogous magnitude asymmetry between self-caused and environment-caused harm changes of identical physical intensity.

Concretely, an EXQ that tests the SD-003 successor could measure the distribution of z_harm_s_obs - z_harm_s_pred residuals under two conditions: agent-caused harm proximity change (where E2_harm_s should predict accurately, so residual small) versus environment-caused (where E2_harm_s should not predict, so residual large). The Shergill paradigm says we should expect a clean separation.

## Limitations and caveats

The obvious caveat is modality. Shergill 2003 uses innocuous tactile force, not harm. The authors assume the forward model is modality-general, and Wolpert's broader programme supports this, but nothing in this paper directly shows that nociceptive signals are cancelled by the same mechanism. A second caveat is timing: the attenuation in the force-matching task is concurrent (it operates during the reproduction movement). REE may need the comparator output on a longer timescale, to gate residue accumulation across episodes. Shergill 2003 does not speak to this.

A third, more subtle issue: the paper measures perceptual attenuation, not agency attribution. The two are related but distinct. Agency attribution is the categorical decision that I did this. Attenuation is the analog reduction in felt intensity. REE needs both halves, and this paper only supplies the analog half. The agency-attribution half comes from Frith 2000 and Haggard 2017.

## Confidence reasoning

Source quality is very high (Science, clean paradigm, strong internal control via the joystick indirect condition, short but tightly argued). Mapping fidelity is moderate-high because the magnitude of attenuation is a quantitative target REE can aim at, but the channel differs (force sensation vs harm proximity). Transfer risk is moderate-low because the forward model is assumed modality-general and the broader Wolpert literature supports this. Overall confidence 0.78.

Based on article retrieved via PubMed search. DOI: https://doi.org/10.1126/science.1085327
