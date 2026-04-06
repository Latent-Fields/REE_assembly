# Differential replay of reward and punishment paths predicts approach and avoidance

**McFadyen, Liu & Dolan, 2023, Nature Neuroscience**

## What the paper does

McFadyen et al. used MEG to track rapid sequential replay in human participants during approach-avoidance decisions. Participants learned the layout of environments containing paths leading to reward or punishment, then chose whether to enter. The MEG methodology captures state-to-state transitions within 20-90ms — the neural signature of compressed sequential replay — allowing trial-by-trial tracking of what the hippocampus is replaying as participants deliberate.

## Key findings relevant to MECH-205

The central finding is that replay is valence-asymmetric: replay of rewarding paths was boosted relative to aversive paths before avoidance decisions, and attenuated before approach decisions. The hippocampus replays harm-relevant content more heavily when preparing to avoid, and benefit-relevant content more heavily when preparing to approach. Critically, this was not just correlational: a trial-by-trial bias toward replaying punishing paths predicted irrational decisions to approach riskier environments — as though the system was generating threat-weighted evidence, and a bias in that evidence generation led to biased decisions.

The anxiety dimension is notable: the effect was stronger in participants with higher trait anxiety, suggesting that the valence asymmetry in replay is itself modulated by individual differences in harm-weighting.

## Mapping to MECH-205's contrastive causal structure

MECH-205 claims that the contrastive replay structure is directionally asymmetric by valence: harm surprises generate contrastive variations asking "what would I have had to do differently to avoid this?" writing to the avoidance/residue map, while goal surprises generate variations asking "what lucky features should I exploit?" writing to the approach map. McFadyen et al. provide direct empirical support for this asymmetry: the hippocampus does in fact treat harm-relevant and reward-relevant replay differently, and this difference in replay content has downstream effects on approach vs avoidance behaviour.

The anxiety finding adds a further layer: if individual differences in harm-salience modulate the valence asymmetry in replay, then MECH-205's residue field (which weights harm traces by salience) would predict exactly this — individuals with a chronically upweighted harm signal would show exaggerated harm-path replay, consistent with the anxious replay bias observed here.

## Limitations

The study measures forward planning replay (awake, before decisions), not offline sleep consolidation replay. MECH-205 primarily targets the offline contrastive replay during sleep; the present study shows the valence asymmetry exists in waking planning replay, but whether the same asymmetry holds in sleep replay is an open question. The study also does not test the contrastive pairing structure within a single replay event — it measures relative replay frequency of valence-differentiated paths, not structured anchor-vs-variation comparison.

## Confidence reasoning

Nature Neuroscience, well-powered human MEG with trial-level precision. Mapping fidelity high for the valence-asymmetry aspect, lower for the offline consolidation and contrastive structure aspects. Overall confidence 0.80.
