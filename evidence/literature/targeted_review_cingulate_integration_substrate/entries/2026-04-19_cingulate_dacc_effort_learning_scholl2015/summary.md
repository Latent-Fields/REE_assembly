# Scholl, Kolling, Nelissen, Wittmann, Harmer, Rushworth 2015 — The Good, the Bad, and the Irrelevant: Neural Mechanisms of Learning Real and Hypothetical Rewards and Effort

**Source:** *Journal of Neuroscience*, [10.1523/JNEUROSCI.0396-15.2015](https://doi.org/10.1523/JNEUROSCI.0396-15.2015). Via PubMed (PMID 26269633).

## What the paper does

The Rushworth lab uses human fMRI with a two-option learning task in which participants learn reward and effort values simultaneously. A critical design feature: rewards on each trial are stochastically "real" (delivered) or "hypothetical" (shown but not delivered), while effort is always real. The real/hypothetical distinction is informationally irrelevant for long-term learning -- participants should integrate all outcomes equally. But humans show an irrational bias toward choices that recently produced real rewards.

The paper dissociates which brain regions track rational learning signals vs which track the irrational bias. dACC and lateral anterior PFC track the rational effort-learning signal and actively suppress the bias; vmPFC and amygdala track reward learning but also carry the irrational recent-real-reward bias.

## Key findings relevant to the claim

- **dACC tracks effort-learning signals** -- specifically, the prediction error on expected effort expenditure, integrated over trials. This is dissociable from reward-learning signals tracked by vmPFC.
- **dACC and lateral anterior PFC jointly *suppress* the recency bias.** Participants who rely more on these regions show more rational long-term learning; those who rely more on vmPFC/amygdala show more monostrategy and more bias to recent real outcomes.
- **Credit assignment for costly actions is a dACC function**, distinct from value-tracking for rewards. This fits the broader Rushworth-lab account of dACC as the credit-assignment hub for effortful/costly decisions.
- **The bias-suppression is an active process.** It is not just that dACC codes effort; it is that dACC plus lateral PFC *counteract* the bias that would otherwise emerge from amygdala/vmPFC. Remove dACC and behaviour reverts to chasing recent-salient reward.

## How this maps onto REE (the translation)

Two architectural implications for the cingulate substrate:

1. **The dACC-analog needs a distinct pathway for cost credit assignment.** Rewards feed a vmPFC-analog; costs (effort, z_harm_a, z_harm_s) feed the dACC-analog. These must not collapse. In ree-v3 right now, trajectory cost is a single sum with reward and harm mixed; this is the failure mode Scholl's dissociation warns against. A cleaner architecture is: separate reward-value and cost-value accumulators, integrated at a downstream decision module.

2. **The dACC-analog should act as a bias suppressor for monostrategy.** This is a new role the pull surfaces that wasn't in the original Options A/B/C -- it's a distinct claim. The mechanism: dACC writes a counter-bias that favours exploration away from recently-rewarded choices when long-term value information demands it. In ree-v3, this connects directly to the monostrategy failure seen in fishtank_viz ("fish swimming same route") and to the goal-seeding problem that SD-012 / EXQ-085 couldn't solve.

The second implication deserves its own claim in the new SD cluster -- something like "dACC-analog bias-suppression against recency bias." It is not the z_harm_a consumer question, but it is a separate function the cingulate substrate should subserve, and the evidence is Rushworth-lab-strong.

## Limitations and caveats

Scholl's effort is physical/cognitive effort (button-holds, task-switching), not pain-driven harm. The bridge to affective-pain credit assignment rests on Shackman's meta-analytic finding that dACC co-localizes for pain, affect, and control -- if you accept that convergence, the inference holds. If you are sceptical of the pain-effort functional identity, this transfer is more speculative.

The real-vs-hypothetical design is a specific experimental manipulation; the "recency bias" Scholl documents may be specific to paradigms that mix informational signals. Whether a similar bias-suppression function operates during harm/avoidance learning is inferred, not measured. A direct test in ree-v3 would require a paradigm where affective pain and informational value diverge and checking that a dACC-analog suppresses the salience-based bias.

Transfer risk: effort is not the same as harm, and a two-arm bandit is not the same as trajectory-based action selection in a grid world. Moderate transfer penalty applies.

## Confidence reasoning

0.78. Rushworth-lab work is high-quality and the effort/reward dissociation is well-established in the broader literature. Source quality is strong. Mapping fidelity is moderate for the "dACC handles cost credit assignment" claim (direct) but weaker for the "dACC suppresses monostrategy bias" claim as applied to ree-v3 specifically (the paradigm is different). Transfer risk is moderate-to-high because of the effort-vs-harm and task-design gaps. Still, the bias-suppression finding is worth including because it identifies a cingulate role that the other papers in this pull do not, and it connects directly to an observed ree-v3 failure mode (monostrategy).
