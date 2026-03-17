# Literature Summary: 2026-03-17_mech095_abnormalities_awareness_action_blakemore2002

## Claims Tested

- `MECH-095`

## Source

- Blakemore SJ, Wolpert DM, Frith CD (2002). *Abnormalities in the awareness of action*. Trends in Cognitive Sciences, 6(6), 237–242.
- DOI: `10.1016/s1364-6613(02)01907-1`
- URL: `https://pubmed.ncbi.nlm.nih.gov/12039604/`

## Source Wording

The sense of agency is produced by a forward-model comparator: an efference copy of the motor command is used to predict the expected sensory consequences; if the predicted sensory outcome matches the actual sensory feedback, the movement is experienced as self-caused. When prediction and outcome diverge, the cause is attributed externally. The temporoparietal junction (TPJ) is the critical neural substrate for this comparison. Pathological failure — as in schizophrenic passivity phenomena and delusions of control — results from disruption of this comparator, causing self-generated actions to be experienced as externally caused. The tickling asymmetry (self-tickling is less ticklish) is the normal behavioural signature: the forward model cancels predicted self-contact, attenuating its salience.

## REE Translation

**MECH-095 (TPJ agency-detection comparator)**: The biological mechanism is a forward-model prediction vs sensory outcome comparator at the self/world interface. In REE terms: E2's z_self_{t+1} prediction (derived from efference copy of action a_t) must be compared against observed z_self_{t+1} after execution. Match → self-caused state change, no residue. Mismatch → world-contributed cause, residue candidate scaled by divergence. This is the missing layer in SD-005's z_self/z_world split: separating the streams is necessary but not sufficient — the comparator mechanism is required to generate the attribution signal that SD-003 needs.

**SD-003 (counterfactual attribution)**: The causal_delta `||E2(z, a_actual) - E2(z, a_cf)||` is an approximation of this comparator operating in the counterfactual mode (comparing two forward-model predictions rather than prediction vs observation). MECH-095 grounds why this approximation fails in V2: without z_self/z_world separation, the delta includes proprioceptive self-effects (body moved differently under a_actual vs a_cf) that are not moral-residue-relevant, swamping the world-directed causal signature.

## Caveat

Blakemore et al. address the phenomenological sense of agency, not moral responsibility attribution directly. The mapping from agency-detection comparator to residue-accumulation trigger is a REE design choice — the biology supports the mechanism but not the specific moral-weighting application. TPJ localization is well-evidenced; the latent-space comparator implementation is REE-specific.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.78`
