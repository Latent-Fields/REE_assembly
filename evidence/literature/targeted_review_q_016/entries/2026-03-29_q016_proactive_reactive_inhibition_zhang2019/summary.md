# Common Neural Network for Different Functions: An Investigation of Proactive and Reactive Inhibition

**Zhang & Iwaki (2019) — Frontiers in Behavioral Neuroscience**
DOI: [10.3389/fnbeh.2019.00124](https://doi.org/10.3389/fnbeh.2019.00124)
*Based on articles retrieved from PubMed*

## What the paper did

Zhang and Iwaki asked whether preparing in advance to inhibit an action (proactive inhibition) recruits the same circuits as cancelling an action already in progress (reactive inhibition). Using the stop-signal paradigm in healthy human adults with fMRI data, they compared 70 dynamic causal models to identify which pathways were specifically recruited by each inhibitory mode, and whether the fronto-basal ganglia network that supports both types of inhibition had distinguishable modulatory architectures.

## Key findings

Both proactive and reactive inhibition engaged the core network: inferior frontal gyrus (IFG), supplementary motor area (SMA), subthalamic nucleus (STN), and primary motor cortex (M1). But proactive inhibition additionally recruited a longer pathway: DLPFC to caudate to IFG to SMA, with the DCM analysis specifically confirming that caudate-to-IFG connectivity was modulated by proactive inhibition only. Reactive inhibition relied on the shorter, faster hyperdirect pathway (IFG-SMA-STN-M1). The authors characterise this as a two-pathway architecture: a slower deliberative pathway for planned suppression and a fast emergency pathway for in-flight cancellation.

## REE translation

For Q-016, this two-pathway finding is directly relevant to what the tri-loop arbitration policy must do. REE's conflict between loops is not always a reactive emergency -- often E3's planning horizon anticipates a potential conflict (the agent knows it is approaching a high-risk situation) before the motor loop has committed. The proactive pathway maps onto E3's pre-commit simulation: E3 can instruct the gate-priority system in advance, via the DLPFC-caudate channel, to depress the motor loop's go-probability even before the sensorium loop signals danger. The reactive pathway maps onto REE's post-commit suppression mechanism: once committed, only the fast hyperdirect channel is fast enough to cancel. An arbitration policy that only has one speed (all reactive, or all proactive) will either fail to cancel fast enough in emergencies, or will over-suppress by treating every commit as a proactive suppression problem. The policy needs both pathways, and the gate-conflict decision must include a timeliness assessment -- is this conflict detected early enough to use the proactive channel, or must it be routed to the hyperdirect emergency path?

## Limitations

The stop-signal paradigm constrains the proactive manipulation to a single motor response in a simple two-choice context. REE's tri-loop conflict involves three loops with incommensurable error signals (MECH-069), which the stop-signal paradigm does not capture. DCM connectivity is a model-comparison technique with multiple assumptions about the generating model; the specific pathways identified may depend on the model space chosen rather than reflecting ground truth anatomy. The study does not examine what happens when proactive suppression fails -- the failure mode most relevant to coupling collapse.

## Confidence reasoning

I rate this 0.66. The two-pathway distinction (proactive long-path vs. reactive hyperdirect) is a clean and well-supported finding that maps directly onto REE's need for a multi-timescale arbitration policy. The confidence penalty comes from the simplicity of the paradigm, the model-dependence of DCM results, and the absence of data on failure modes and coupling collapse.
