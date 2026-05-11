# Schulz & Gershman 2019 — Algorithmic architecture of exploration in the human brain

**Citation.** Schulz E, Gershman SJ. (2019). The algorithmic architecture of exploration in the human brain. *Current Opinion in Neurobiology* 55:7-14. [DOI](https://doi.org/10.1016/j.conb.2018.11.003). PMID 30529148.

## What the paper does

This is a synthesis review of the human-exploration literature through late 2018. It pulls together the evidence that humans use both random and uncertainty-directed strategies — the behavioural evidence (Wilson 2014, Gershman 2018), the neural-system mappings (Daw 2006 for frontopolar directed; the Aston-Jones & Cohen adaptive-gain account for LC-NE random), the causal manipulations (Zajkowski 2017 TMS, Warren 2017 atomoxetine), and the developmental trajectories (a separate line of work showing that random exploration peaks in adolescence while directed exploration is stable across adulthood).

The synthesis argument is: random and uncertainty-directed exploration are not just two readings of one underlying mechanism; they are mechanistically distinct, neurally dissociable, pharmacologically separable, and developmentally distinct. The review also touches on more recent work on structure-aware exploration (people exploit correlations between options) but the primary thesis is the dual-system architecture.

## Relevance to Q-043

Schulz & Gershman 2019 functions as the load-bearing synthesis for Q-043's R1: do the two mechanisms exist? The cumulative human-evidence answer is yes, and this review packages the case in a single citable artifact. For REE governance, citing the review is shorthand for citing the cluster of primary work that the review aggregates.

For the V3 parametric-sweep design, the most useful take-home is the developmental angle. Random exploration peaks in adolescence and falls in adulthood; directed exploration is stable. This suggests that the two mechanisms have different time constants for learning the appropriate calibration — if REE's MECH-313 weight needs to be re-tuned faster than MECH-314 weight (because the optimal noise floor depends on substrate stability, which changes during training), the sweep should consider whether to test calibrations as fixed scalars or as schedules over training epochs.

## Caveats

Reviews are not primary evidence. Schulz & Gershman 2019's confidence should be lower than that of the primary papers it synthesises, otherwise this lit-pull would double-count. I weight the review at 0.76 explicitly to keep its contribution to the aggregate lit_conf modest — its independent value is in the framing and cross-paper synthesis, not in adding new empirical content.

The review does not commit to a calibration verdict — it endorses the dual-system architecture but leaves the relative-weight question open. For Q-043 this is appropriate because the calibration question is substrate-specific and the human literature does not have a direct analog of SD-054. The review is informative about the existence premise but does not pre-resolve the calibration verdict.

I also note that the developmental angle does not map cleanly to REE. The agent does not have life-stages; it has training epochs. Translating "random exploration peaks in adolescence" into a prediction about MECH-313 weight scheduling is speculative and probably premature.

## Confidence reasoning

I assign 0.76. Source quality (0.80) and mapping fidelity (0.80) are both high — the review is in a strong venue and the synthesis claim maps directly onto Q-043's R1. Transfer risk (0.30) is moderate. The deliberate down-weighting from a hypothetical "review of strong primary work = 0.85+" to 0.76 reflects double-counting risk: the primary papers in this lit-pull already carry the synthesis's load. Future readers should give more weight to the primary entries (Daw 2006, Wilson 2014, Zajkowski 2017, Warren 2017, Gershman 2018) than to this review when judging whether Q-043's R1 is settled.
