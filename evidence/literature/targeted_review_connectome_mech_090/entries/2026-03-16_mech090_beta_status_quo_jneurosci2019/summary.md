# Literature Summary: 2026-03-16_mech090_beta_status_quo_jneurosci2019

## Claims Tested

- `MECH-090`

## Source

- Helfrich R, Knight RT (2019). *Beta Oscillations in Working Memory, Executive Control of Movement and Thought, and Sensorimotor Function*. Journal of Neuroscience.
- DOI: `10.1523/JNEUROSCI.1163-19.2019`
- URL: `https://www.jneurosci.org/content/39/42/8231`

## Source Wording

Beta band oscillations (~13-30 Hz) in the subthalamic nucleus (STN) and basal ganglia encode a "maintain current state / status quo" signal that opposes action initiation and cognitive updating. Elevated prefrontal beta during working memory delay periods prevents interference; beta drops at task completion. The hyperdirect pathway (cortex → STN, bypassing striatum) propagates high-beta synchrony to enforce rapid braking under urgency. Enhanced beta in the STN is pathologically amplified in Parkinson's disease, where motor slowing results from excessive status-quo gating.

## REE Translation

MECH-090 (beta-gated policy output): Beta elevation during a committed action sequence holds E3's current policy state from propagating to action selection — the E3 model continues updating internally (heartbeat continues) but the output is blocked. At sequence completion or unexpected salient event: beta drops → E3 state propagates. The hyperdirect cortex → STN pathway is the fast interrupt substrate: it can force early beta drop for mid-sequence emergency braking without waiting for completion. This explains why the ATTRIBUTION_BLIND condition in MECH-057a performed comparably to COMPLETION_GATED — continuous updating without beta gate is closer to the correct architecture than episodic gating.

## Caveat

Most direct STN beta evidence is from Parkinson's disease populations where beta is pathologically amplified; whether the same gating principle operates in healthy agentic action sequences is inferred rather than directly tested. PFC delay-period beta (more relevant to E3) is better evidenced in healthy populations, but the specific internal-update vs output-propagation distinction is not always explicitly tested in the reviewed literature.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
