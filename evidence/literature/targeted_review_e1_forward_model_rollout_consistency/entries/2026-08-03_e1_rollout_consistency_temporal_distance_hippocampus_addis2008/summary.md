# Addis & Schacter 2008 -- Temporal distance modulates hippocampal engagement

**Claim(s):** MECH-135 | **Direction:** supports | **Confidence:** 0.60

*According to PubMed* (PMID 18157862), [DOI: 10.1002/hipo.20405](https://doi.org/10.1002/hipo.20405).

## What the paper did

Participants were cued to construct a past or future event, pressed a button once it was in mind, then elaborated it and rated it, all during event-related fMRI. The analysis that matters here is the parametric modulation: temporal distance and amount of detail entered as covariates, with medial temporal lobe and frontopolar cortex as the focus.

Two results. On **detail**: left posterior hippocampus tracked the amount of detail in both past and future events, while left anterior hippocampus responded differentially to detail in *future* events -- which the authors read as recombination of details into a novel future event. On **temporal distance**: bilateral hippocampal activity correlated significantly with the increasing *remoteness* of future events. Their interpretation is that remote future events include increasingly disparate details, and integrating those into a coherent simulation demands intensive relational processing.

## Why this is the more architecturally useful of the two biology entries

The Hassabis lesion study is the more famous paper and establishes that the simulation system is separable from perception. This one says something I find more directly actionable: **simulating further ahead is not the same operation run for longer.** Hippocampal recruitment *scales with depth*. Biology adds machinery as the horizon extends.

Now look at what E1 does. `predict_long_horizon` is a plain Python loop -- `for _ in range(horizon)`, LSTM step, project, feed the prediction back as the next input. Thirty iterations of one map, with no term, no module, and no objective whose contribution grows with depth, trained throughout at `horizon=1`. That is precisely the architecture the biological result argues against. Depth is treated as free iteration when in tissue it is the thing that costs most.

What makes me weight this despite unremarkable source-quality numbers is that it converges on the ML side's recommendation from a completely independent direction. Four ML papers say, in different vocabularies, *train at the horizon you plan at*. This says biology *builds* at the horizon it plans at. Two literatures with nothing methodological in common landing on the same architectural commitment is worth more than either alone.

It also weakly discriminates among the candidates. Approaches that add depth-scaled structure -- TD-MPC's H-step unroll, Asadi's sequence-conditioned model -- sit closer to the biological arrangement than approaches that leave the composition unchanged and only regularise it.

## Limitations

The step from increased BOLD signal to "more computational work is required at depth" is an interpretation and not the only one available. Remote future events may recruit more hippocampus because they are more novel, more schematic, less constrained by retrieved detail, or harder in ways that have nothing to do with integrative load. The authors' reading is plausible and it is the reading REE leans on, but it is inference from a parametric correlation in a modest sample, not a demonstration of computational necessity.

The scales are also frankly incommensurable. Biological temporal distance here spans days to years of subjective time; REE's rollout depth is thirty substrate ticks in a grid world. The mapping is an analogy of architectural principle, nothing more, and I would not let it carry any quantitative weight.

And it motivates depth-aware structure *in general*. It does not pick a fix, and should not be cited as though it did.

## Confidence reasoning

Source quality 0.68 -- Hippocampus 2008 from Schacter's group, well-cited within the constructive-episodic-simulation literature, but a modest-sample parametric fMRI study from before large-sample norms, and BOLD-to-computation inference is soft. Mapping fidelity 0.62: the architectural principle transfers well and lands on exactly the axis V3-EXQ-108b failed on -- horizon depth, which the sibling E2 review does not cover at all -- while the quantitative scales do not transfer. Transfer risk 0.45.

Aggregate 0.60, direction **supports**. The clearest biological statement available that composing a one-step model with itself is not how a working simulator reaches a long horizon.
