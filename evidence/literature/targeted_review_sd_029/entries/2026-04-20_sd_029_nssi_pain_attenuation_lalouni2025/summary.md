# Lalouni et al. (2025): Attenuation of Self-Induced Pain in Women With Nonsuicidal Self-Injury and Healthy Controls

*European Journal of Pain* 2025. DOI: 10.1002/ejp.70057

## What the paper did

Lalouni and colleagues ran a larger replication and extension of their 2020 Pain paper, comparing self-induced versus experimenter-induced pressure-pain thresholds in women with nonsuicidal self-injury (NSSI) against healthy female controls. The main question was whether the sensory-attenuation phenomenon is preserved, exaggerated, or blunted in a clinical population known to engage in deliberate self-injury.

## Key findings

Self-induced pressure-pain thresholds were significantly higher than experimenter-induced thresholds in both groups. The mean between-condition difference was approximately 164.8 kPa, consistent in magnitude with Lalouni 2020. The NSSI group had roughly 106.7 kPa higher thresholds overall than controls. When prevalence of >=10% attenuation was computed per participant, 95% of NSSI participants met the criterion versus 78% of controls (p=0.022). Sensory attenuation correlated modestly with conditioned pain modulation across subjects (Kendall tau = 0.17, p = 0.025), suggesting partial substrate overlap between the efference-copy-driven forward-model comparator and descending pain-modulatory pathways.

## Mapping to SD-029

The primary value for SD-029 is replication. Lalouni 2020 established the nociceptive-stream attenuation effect in 40 healthy adults; this paper confirms it in a larger, clinically heterogeneous sample. The prevalence finding is especially useful for SD-029 C2 calibration. Twenty-two percent of healthy controls did not show >=10% attenuation -- the biological comparator mechanism is population-typical but not universal. A V3 experiment that insists on perfect or near-universal attenuation across seeds would be out of step with the biological baseline. The C2 criterion should be framed in terms of a population-level effect (most agent-caused events attenuated relative to externally-caused) rather than a per-event cancellation threshold.

The conditioned-pain-modulation correlation is interesting but secondary. It hints that E2_harm_s in the REE architecture might share substrate with a general descending-pain-modulation module rather than being an isolated forward model. This is architectural rather than claim-level -- SD-029 itself doesn't take a position on the internal wiring of E2_harm_s, so the correlation is suggestive but not decision-relevant.

## Caveats

Two. First, the clinical framing is not directly relevant to SD-029 in V3. The V3 agent is not meant to model psychiatric individual differences; it is meant to detect self-caused versus externally-caused harm in a gridworld. Read this paper for replication evidence and the population-variance signal, not the NSSI interpretation. Second, the between-group difference (NSSI > controls in attenuation) is in the opposite direction of what a simple "broken comparator -> clinical pain dysfunction" model would predict. This is hypothesis-generating at best for the clinical literature and largely tangential to the V3 implementation.

## Confidence reasoning

Source quality is moderate-high: peer-reviewed European Journal of Pain, larger sample than Lalouni 2020, but the analysis is more exploratory with multiple group contrasts. Mapping fidelity is good for the core attenuation result but weaker for the clinical extensions. Transfer risk is similar to Lalouni 2020 -- static algometer paradigm, not V3 agent dynamics. Aggregate 0.72, slightly below Lalouni 2020. This is a supporting-replication paper rather than a primary-evidence paper.
