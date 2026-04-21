# Roozendaal & McGaugh (2011) "Memory Modulation" — supplement to MECH-074

## Why this paper, and what question it answers for us

McGaugh's 2004 *Annual Review* already sits in this directory as the canonical statement that the basolateral amygdala (BLA) gates consolidation in downstream memory systems. That paper is strong on mechanism and weak on numbers. What the `BLAAnalog` module needs, before it can be wired to `HippocampalModule`, is the shape of the gain curve and the duration of the window in which the gain applies. The 2011 Roozendaal & McGaugh review in *Behavioral Neuroscience* (125(6):797-824; doi:10.1037/a0026187) is the closest thing the field has to a consolidated numerical synthesis, drawn from roughly three decades of rodent post-training pharmacology from the same lab. It is the supplementary source that pays for itself.

## What the paper actually reports

Two quantitative regularities matter for us. The first is the post-training window. Intra-BLA infusions of norepinephrine (0.3-1.0 ug) or clenbuterol administered shortly after training reliably enhance 24-hour retention; the same infusions given before retention testing, or given at delays that push them outside the immediate post-training period, do not. Roozendaal and McGaugh treat this as their central argument that BLA modulation acts on consolidation rather than acquisition or retrieval. The window is not crisp; it is read off from experiments that manipulate the post-training delay, and the functional edge is at tens of minutes, not hours.

The second is the shape of the dose-response curve. The paper is explicit that dopaminergic D1 modulation of working memory follows an inverted-U. For glucocorticoids the text describes a biphasic pattern -- enhancement at moderate doses (around 1 mg/kg corticosterone systemically), impairment at high doses -- and for intra-BLA adrenergic drugs the same shape appears: propranolol impairs dose-dependently (0.1, 0.3, 1.0 ug), NE enhances in a bounded range, and above that range the effects flatten or reverse. The honest gloss is that the literature is more consistent about the *shape* of the curve than about any single numerical peak. An interpolation across the clenbuterol, NE, and corticosterone studies puts the peak enhancement roughly in the 2-3x range above unmodulated baseline retention scores, with clear degradation beyond that.

## Where the translation strains

I want to be direct about the caveat. Rodent posttraining pharmacology measures a behavioral retention score at 24 hours; we are proposing to set a scalar multiplier on a latent write operation in a simulated agent running at 100ms per step. The mapping is structural, not quantitative -- a bounded post-event window with an inverted-U gain curve -- and the specific numerical defaults below are seeds for ablation, not imported constants. If our V3 experiments show that a 3x peak or a 10-minute window fits the data better, that is the experiment working as intended. What we are borrowing from Roozendaal & McGaugh is the *form* of the rule: gain rises with arousal up to a point, then falls; gain is active for a bounded window after the triggering event; outside emotionally arousing regimes the system reverts to flat baseline.

## Quantitative defaults for BLAAnalog config

Given 1 simulation step ~= 100 ms, and taking ||z_harm_a|| to be normalized to [0, 1] by the module's internal normalization:

- `encoding_gain_max`: **2.5x** (peak multiplier on HippocampalModule write strength at mid-arousal)
- `arousal_threshold`: **||z_harm_a|| >= 0.4** (below this, gain = 1.0; neutral episodes are not amplified)
- `arousal_peak`: **||z_harm_a|| ~= 0.7** (location of inverted-U peak; above this, gain decays back toward 1.0 and can drop below it at saturation)
- `post_event_window_steps`: **1.8e4 steps (~30 minutes simulated)** (gain is active within this window after the triggering arousal event; outside it, gain = 1.0)
- `window_decay`: exponential with half-life **~3.6e3 steps (~6 minutes)** inside the window, so that the late tail approaches baseline smoothly rather than cliff-dropping

These numbers should be treated as the starting envelope for V3 ablation sweeps, not as facts. Their justification is that the shape matches Roozendaal & McGaugh (2011) and the magnitude stays within the range that rodent pharmacology tolerates without flipping sign.
