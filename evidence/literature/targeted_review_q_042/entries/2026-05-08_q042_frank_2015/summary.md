# Frank, Gagne, Nyhus, Masters, Wiecki, Cavanagh & Badre 2015 — fMRI and EEG predictors of dynamic decision parameters during human reinforcement learning

**Source:** Frank MJ, Gagne C, Nyhus E, Masters S, Wiecki TV, Cavanagh JF, Badre D. *Journal of Neuroscience* 35(2):485-494 (2015). [DOI](https://doi.org/10.1523/JNEUROSCI.2036-14.2015). PMID 25589744, PMCID PMC4293405. According to PubMed.

## What the paper did

Frank and colleagues asked whether the dynamics of reinforcement learning and the dynamics of decision making -- two literatures that had typically been treated separately -- could be unified at the trial level. They modelled human choice behaviour in an RL task with a drift-diffusion model (DDM) in which the trial-by-trial reward values, learned via standard RL update rules, are then sequentially sampled at the next decision until the cumulative value signal crosses a threshold. The threshold itself was modelled as varying trial by trial. They collected simultaneous fMRI and EEG and found that the trial-specific threshold value was well predicted by STN BOLD activity and by mediofrontal (pre-SMA) theta in EEG. When choices differed subtly in reward values, increased pre-SMA theta and STN BOLD coincided with raised thresholds, allowing more evidence accumulation before commit. The threshold modulation was time-locked to the decision phase -- not to outcome.

## Why it matters for Q-042

This paper is the cleanest empirical answer to Q-042's timing question. The decision threshold -- the biological analogue of REE's BG commit gate -- is updated WITHIN a single decision cycle, BEFORE outcome arrival, via a pre-SMA->STN communication channel. The update is dynamic, conflict-sensitive, and lives entirely in the action-selection phase. This is precisely what Option B in Q-042 proposes: hoist the precision update upstream so that the BG commit gate has live, current threshold information at action time, regardless of whether outcome integration has happened.

The structural correspondence to REE's recent failure mode is striking. The EXQ-514d / 530 / 536 cluster failed because _running_variance pinned at precision_init=0.5 -- the update never fired because the experiment scripts never called agent.update_residue(). Biologically, this corresponds to a brain whose pre-SMA never communicates with STN, and whose decision threshold therefore never updates from its prior. Frank et al.'s threshold modulation is exactly the pre-commit gain modulation REE wants. If REE's analogue lives only at outcome time, the equivalent biological mechanism is unavailable.

## Mapping to REE

The architectural pattern transfers; the substrate analogy is approximate. DDM threshold (how much evidence to accumulate before commit) and ARC-016 precision (how much to weight a given prediction error) are not identical computational roles. They are, however, both pre-commit gain controls that determine how decisively the agent acts on its current beliefs, and both are updated trial-by-trial in biology by a signal that fires at action selection. So the architectural recommendation transfers: REE should compute and broadcast a current precision signal AT action-selection time, even if the canonical statistical update of the running variance happens later.

The dual-update reading Q-042's notes already favours fits the data well. Frank et al.'s threshold lives at action selection time but is updated trial-by-trial based on accumulated outcome history -- so behind the scenes, the underlying statistics are also being incorporated post-outcome. Biology runs both arms.

## Caveats

The simultaneous fMRI+EEG-DDM methodology is technically demanding and the specific BOLD-theta-threshold coupling reported here has been refined by later studies but not always replicated at the strength of the original report. The sample is moderate (~25 subjects), typical for fMRI but small for the strong DDM parameter inference being made. The DDM threshold is one specific model parameter; alternative race-model parameterisations would attribute the same data to different computational variables. None of these caveats undermine the timing claim relevant to Q-042 -- that whatever the parameter is called, it updates at action selection time -- but they do mean the substrate identification (STN + pre-SMA + theta) should be treated as the canonical case, not the only one.

## Confidence reasoning

0.80 supports for Q-042. Source quality high (0.85, J Neurosci, methodologically demanding). Mapping fidelity high (0.78) -- the paper directly tests the timing question and finds Option B's answer. Transfer risk low-moderate (0.25) -- the pre-SMA->STN architectural pattern transfers cleanly to REE's E3->BG commit gate analogue. This is the strongest single piece of evidence in this lit-pull for Option B over Option A.
