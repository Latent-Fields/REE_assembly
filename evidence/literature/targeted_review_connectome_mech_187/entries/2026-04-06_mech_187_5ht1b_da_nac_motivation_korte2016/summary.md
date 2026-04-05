# Korte et al. (2016) -- 5-HT1A/1B Agonism, DA in NAc, and the Paradox of Reward Motivation

**Entry:** 2026-04-06_mech_187_5ht1b_da_nac_motivation_korte2016
**Claim:** MECH-187 (Incentive Salience Gain Regulation by Serotonin)
**Source:** Korte SM et al. "The 5-HT1A/1B-receptor agonist eltoprazine increases both catecholamine release in the prefrontal cortex and dopamine release in the nucleus accumbens and decreases motivation for reward and 'waiting' impulsivity, but increases 'stopping' impulsivity." Eur J Pharmacol. 2016;794:257-269. DOI: 10.1016/j.ejphar.2016.11.024. PMID: 27866999.

---

## What the paper did

Korte et al. conducted a multi-assay pharmacological study in rats using eltoprazine, a 5-HT1A/1B receptor agonist. They combined in vivo microdialysis (measuring extracellular dopamine, norepinephrine, and serotonin simultaneously in mPFC, OFC, and NAc) with intracranial self-stimulation (ICSS) for brain reward threshold measurement, delay-aversion task for waiting impulsivity, and stop-signal task for stopping impulsivity. The logic was to characterize the full profile of 5-HT1A/1B agonism across the motivational-inhibitory spectrum, with particular interest in whether eltoprazine's efficacy for impulse control disorders might be linked to its monoaminergic effects.

## Key findings

The microdialysis results are the most directly relevant to MECH-187. Eltoprazine increased DA release in NAc by approximately 30-50% above baseline (reading from the figures), while simultaneously decreasing 5-HT release in mPFC and NAc. It also elevated DA and NE in both mPFC and OFC. Crucially, despite the NAc DA increase, brain stimulation reward became less effective: ICSS reward thresholds were elevated, meaning rats required stronger brain stimulation to maintain the same behavioral output. This is the paradox: more DA in NAc, but reduced motivation for reward.

On the behavioral side: eltoprazine decreased waiting impulsivity (impulsive choice in delay-aversion task) but increased stopping impulsivity (stop-signal task). This dissociation confirms that the 5-HT1A/1B system has different effects on different forms of behavioral control, which aligns with Cools et al. (2008)'s dual-function account.

## REE mapping to MECH-187 and the gain paradox

MECH-187 formalizes serotonin as a gain on the benefit_exposure -> z_goal transduction. Korte et al.'s result raises a refinement: the gain relationship is not simply about DA release amplitude in NAc. When 5-HT1A/1B receptors are activated (mimicking elevated serotonergic tone), DA in NAc goes up, yet wanting (as measured by ICSS threshold) goes down. This is initially paradoxical but resolves if we consider that 5-HT receptor activation at the NAc modulates the transduction efficiency of DA signal into motivational output -- not merely the DA concentration. Mechanistically, 5-HT1B receptors are expressed on DA terminals in NAc and on postsynaptic MSNs; activation could alter DA re-uptake, phasic vs. tonic DA signal ratio, or downstream MSN responsivity to DA.

For MECH-187 in the REE architecture: the gain parameter is best interpreted as the transduction efficiency (how much z_goal change per unit of benefit_exposure-triggered DA signal), rather than the DA release amplitude itself. This is an important refinement. In EXP-0099 design terms, the gain multiplier acts on the benefit -> z_goal computation, not on the benefit terrain signal amplitude. The direction of the effect under elevated serotonergic tone (eltoprazine) is reduced motivation -- consistent with MECH-187 predicting that gain suppression (low effective 5-HT signaling -> low NAc 5-HT tone) produces elevated wanting. The proposed x0.2 reduction in EXP-0099 corresponds to high-5-HT-tone suppression of transduction gain, and x5 elevation corresponds to low-5-HT-tone disinhibition.

## Quantitative constraints for EXP-0099

This is the paper most relevant to calibrating EXP-0099 gain multipliers. Key quantitative observations:

- NAc DA increased approximately 30-50% above baseline under eltoprazine (reading from Fig. 1 in paper), while ICSS threshold was elevated by approximately 15-25%.
- This suggests the gain suppression under elevated 5-HT tone is modest in magnitude in the NAc DA -> reward motivation direction (not a 5-fold suppression).
- The proposed x0.2 gain reduction (implying an 80% suppression of transduction) may be too strong given this data.
- Conversely, the x5 elevation under low 5-HT-tone is speculative -- the paper does not test a 5-HT-depleted condition. The natural comparison would be tryptophan-depleted animals.
- A more empirically grounded estimate might be: high-5-HT-tone suppresses transduction gain by 20-40% (not 80%), and low-5-HT-tone elevates it by 50-150% (not 500%). But this requires formal dose-response curves that this study does not provide.

These quantitative caveats should be incorporated into the EXP-0099 parameter sweep: the proposed extreme values (x0.2, x5) represent theoretical upper bounds on gain modulation range; the empirically supported range is likely narrower.

## Limitations and caveats

The paradoxical direction (more NAc DA, less wanting) under eltoprazine requires caution. The concurrent NE elevation in PFC is a confound -- elevated PFC NE could independently suppress ICSS-seeking via top-down inhibition. The 5-HT1A component of eltoprazine (autoreceptor stimulation in DRN) would reduce 5-HT release downstream, complicating interpretation: the NAc DA increase may be mediated partly by DRN autoreceptor-mediated 5-HT reduction rather than direct NAc 5-HT1B receptor activation. This means the paper reports a mixed pharmacological effect, not a clean dissection of 5-HT gain on NAc DA. Transfer risk to an endogenous gain-modulation interpretation is moderate.

## Confidence reasoning

This is the most mechanistically direct paper for MECH-187 among the four, providing in vivo circuit-level measurements (microdialysis) at the target circuit (NAc DA) combined with a direct motivational assay (ICSS). The paradoxical direction is interpretively tractable and refines rather than refutes MECH-187's gain formulation. Confidence 0.72 reflects good mechanistic grounding tempered by the pharmacological complexity and the modest sample size typical of microdialysis rodent studies.
