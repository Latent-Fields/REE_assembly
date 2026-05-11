# Kennerley et al. 2006 — Optimal decision making and the anterior cingulate cortex

According to PubMed, [DOI 10.1038/nn1724](https://doi.org/10.1038/nn1724), PMID 16783368.

## What the paper did

Macaques received ACC lesions or sham controls and were tested on two tasks: a reinforcement-guided two-choice task with probabilistic outcomes, and a dynamic foraging task with shifting reward rates. The behavioural analysis decomposed performance into within-trial responses (error-detection, post-error correction) and across-trial integration (sustaining rewarded responses, risk-payoff integration).

## Key findings relevant to Q-045

ACC lesions produced a striking dissociation. The lesioned monkeys could STILL detect that a particular choice had just been wrong and could STILL adjust their next-trial response accordingly. What they could NOT do was sustain rewarded responses across trials, or integrate risk and payoff in dynamic foraging. The deficit was specifically in the integration of ACTION-OUTCOME HISTORY into voluntary choice — a within-substrate dissociation that argues ACC's role is value-from-history, not error-detection or value-from-stimulus.

## How this translates to REE

For Q-045 this paper supplies the CAUSAL leg of the dACC substrate-distinctness argument. Scholl 2015 (also in this pull) is correlational fMRI; Kennerley is lesion-causal. Together they say: dACC is causally necessary for action-outcome history integration (Kennerley), and one specific aspect of that integration is content-selective suppression of irrelevant recent rewards (Scholl). MECH-260 sits at the intersection. The architectural argument for Q-045 is that MECH-260's substrate (dACC) is doing something computationally specific that an LC-NE noise-floor primitive (MECH-313) cannot reproduce: it integrates a temporally-extended action-outcome history and selectively gates which past trials propagate to current value.

The 4-arm ablation registered against Q-045 should reproduce Kennerley's pattern in the 260-OFF arms: preserved within-trial sensitivity (the agent can still detect a particular harm and avoid it on the next trial) but impaired across-trial value-history learning (the agent fails to sustain a successful policy over a longer window, or fails to integrate accumulated risk into ongoing choice). If the 260-OFF arms instead show preserved across-trial learning, MECH-260's V3 implementation is under-specified — it has captured the anti-recency face of ACC's role but not the broader history-integration substrate that anti-recency sits inside.

This connects to the SD-054 reef-foraging substrate design: the substrate must support measurement of across-trial integration on the foraging dynamics, not just within-trial responses to immediate outcomes. If SD-054 as currently designed only generates short-horizon outcomes (a single decision tick has its consequence within that tick), the 4-arm ablation will not have the temporal-horizon needed to dissociate MECH-260 from MECH-313 in the Kennerley sense. This is a substrate-readiness diagnostic that should run BEFORE the 4-arm ablation, not after.

## Limitations and caveats

Macaque-to-REE is a two-hop transfer (species + abstraction level). The mapping to MECH-260 specifically is partial: Kennerley shows ACC is necessary for action-outcome history integration in general, which is broader than 'anti-recency suppression of irrelevant rewards'. Scholl 2015 supplies the narrower content-selectivity. Kennerley's task did not include an irrelevant-reward condition; it used dynamic foraging and probabilistic reinforcement. The mapping is to the ACC's role as the SUBSTRATE that supports history-integration — MECH-260 as anti-recency sits inside this broader substrate, but does not exhaust it. MECH-260's V3 implementation should be evaluated against both anchors.

## Confidence reasoning

Confidence 0.81. Source quality high (Nature Neuroscience, causal lesion, multi-task with explicit within-vs-across-trial decomposition). Mapping fidelity strong on the substrate-distinctness argument that Q-045 needs (ACC does specific history-integration work, not noise) and moderate on the specific MECH-260 primitive (anti-recency is one face of ACC history-integration, not the whole role). Transfer risk moderate (macaque-to-REE, lesion-to-substrate-ablation — both are well-trodden mappings). Provides the CAUSAL leg complementing Scholl 2015's correlational fMRI.
