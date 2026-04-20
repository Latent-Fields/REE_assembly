# Goulden et al 2014 -- DCM replication of salience-network switching

## What the paper did

An independent methodological replication of Sridharan, Levitin & Menon 2008. Where Sridharan used Granger causality on BOLD time series to establish that the salience network drives CEN/DMN transitions, Goulden used a different causal-inference approach: dynamic causal modelling (DCM) applied to network time courses extracted by spatial independent component analysis (ICA) of resting-state fMRI. The question was whether the Sridharan finding -- salience network as causal switcher -- would hold when analysed with a Bayesian model-comparison framework rather than Granger.

The study applied DCM to two independent resting-state datasets. Across both, the winning model specified the salience network (AIC + dACC nodes) as the driver of bidirectional transitions between DMN and CEN. The authors report that the result is repeatable across datasets, which matters because DCM is sensitive to model-space specification and individual-dataset idiosyncrasies.

## Why this matters for SD-032a

Methodological replication is what separates a robust architectural principle from a Granger-causality artefact. BOLD-based Granger has well-known sensitivity to haemodynamic-response variability that can produce spurious directionality. DCM uses a generative Bayesian model with an explicit neural-to-BOLD forward step, so it is less vulnerable to that specific failure mode. When two different causal-inference methods agree on the same directionality -- salience drives CEN/DMN switching -- the architectural claim is considerably harder to dismiss.

For SD-032a, this is supporting (not primary) evidence. The primary architectural license comes from Sridharan 2008; Goulden 2014's value is reducing the prior probability that the salience-coordinator framing is a methodological artefact. It directly reinforces the ree-v3 design choice to have a SalienceCoordinator that reads aggregated signals and emits mode-switch triggers, rather than distributing that function across the subdivisions.

## Limitations and caveats

Two limitations matter for REE. First, the study is resting-state only. It says nothing about whether the coordinator role scales or modulates with task demand. ree-v3 operates primarily in task-engaged regimes (external_task mode is the default attractor per SD-032a's implementation), so the transferability from resting-state dynamics to active-agent dynamics carries a non-trivial assumption. Second, DCM shows *which* network drives the switches, not *what aggregation rule* the driver uses. Goulden's evidence is compatible with many possible internal computations for the salience network, including ree-v3's softmax-over-affinity-logits, but also a winner-take-all rule, a threshold-only rule, or a graded proportional rule. The implementation choice is not constrained by this paper.

There is also the usual caveat that canonical-network labels from ICA are themselves model-dependent. "The" CEN or "the" DMN is an operational definition based on consistent ICA decomposition; small changes to preprocessing can shift the boundaries. The architectural finding survives these shifts in practice, but a principled reader should treat "salience network drives switching" as a robust pattern rather than a tight biological prediction.

## Confidence reasoning

I assigned 0.78 rather than a higher value because the paper is primarily a methodological replication, not a new empirical finding. It strengthens the Sridharan 2008 mapping but does not add new architectural constraints; I do not want to double-count its evidential weight. Source quality is 0.80 (NeuroImage, Bayesian model comparison, two independent datasets). Mapping fidelity is 0.75 -- same limitations as Sridharan. Transfer risk 0.30 because resting-state generalisation to task-engaged regimes adds a layer of extrapolation.

Read together, Sridharan 2008 and Goulden 2014 license the architectural framing of a salience-network coordinator as causally upstream of mode switching, with two different causal-inference methods agreeing. That is a reasonable biological scaffold for SD-032a. What neither paper tells us is whether ree-v3's specific four-mode vector, softmax rule, or hysteresis threshold are the right implementation choices -- those remain in scope for V3-EXQ-446.
