# Mileykovskiy, Kiyashchenko, & Siegel 2005 — behavioural correlates of identified orexin neurons

## What the paper did

Mileykovskiy and colleagues recorded single-unit activity from juxtacellularly labelled, identified hypocretin/orexin neurons in freely-moving rats across the full sleep-wake cycle. Cell identification through juxtacellular labelling is the methodological strength here: previous extracellular recordings in the lateral hypothalamus were necessarily mixed-population, while these recordings are confirmed orexin-cell readings. Behavioural state was classified by EEG/EMG and video, allowing firing-rate comparisons across quiet waking, grooming, eating, exploration, REM sleep, and slow-wave sleep.

## Key findings relevant to MECH-280

Two firing-rate observations matter for MECH-280's parameter anchoring. First, the active/quiet ratio: orexin neurons show roughly a five-fold firing-rate increase from quiet waking to active behaviours, with maximal firing during exploration. This is the biological referent for MECH-280's recruitment_threshold sitting in the middle of the dynamic range — a quiet-waking equivalent input produces near-zero override, an active-waking equivalent input saturates. Second, the temporal kinetics: sensory-evoked activation is transient (sub-second to seconds), but firing remains elevated across whole episodes of active waking lasting tens of seconds to minutes, with moderate sustained activity through grooming and eating. The episode-scale carry-over is the kinetic profile MECH-280's sustained_threat_window (12 steps) and EMA decay (half-life ≈ 14 steps) are built to capture.

The picture from these recordings is one of integration across behavioural episode rather than per-event response: the firing rate during a foraging bout reflects the bout's sustained demand, not the moment-by-moment sensory transients within it. That kinetic profile is exactly what an integration-window-plus-EMA-decay implementation produces.

## How this translates to REE

The recordings give MECH-280 two of its four scalar parameters direct biological anchors. sustained_threat_window in the 8–25-step band is consistent with episodes of tens of seconds to a couple of minutes when one REE step ≈ 1–3 s of real time. decay_rate ≈ 0.05 (half-life ≈ 14 steps) is consistent with the multi-second to minute-scale carry-over of orexin elevation after stimulus offset. The five-fold active/quiet ratio anchors the recruitment_threshold ≈ 0.5 midpoint. None of these parameters are pinned to single digits by the recordings, but the bands they live in are biological rather than arbitrary.

## Limitations and caveats

The recordings are in rat under standard sleep-wake-active behavioural state monitoring. The threat / metabolic-demand contingencies MECH-280 cares about — sustained predator presence under rising hunger — are not the explicit experimental contrast. The mapping from active-waking firing to override_signal recruitment under sustained drive plus threat is therefore one inferential step removed. The papers that close that loop (de Araujo Salgado 2023, Marino 2020) are the behavioural-arbitration anchors; this paper provides the kinetic envelope within which the arbitration plays out.

## Confidence reasoning

I am giving this 0.78. Source quality is high (0.85, Neuron-tier primary recording with cell-identification controls). Mapping fidelity is 0.74 — the experimental contrast is sleep-wake-active rather than threat-foraging arbitration, so the kinetic anchors transfer well but the recruitment-under-threat-and-drive specificity has to be inferred. Transfer risk is standard at 0.32. The aggregate sits in the supports band, level with the Marino 2020 anchor: this paper grounds MECH-280's kinetic parameters, Marino grounds its existence-of-an-LH-override-channel claim, and de Araujo Salgado 2023 grounds its behavioural-arbitration prediction. Together the three give MECH-280 a defensible biological foundation; alpha_override remains the parameter least constrained by primary data.
