# Rattenborg, Lima & Amlaner 1999 -- Half-awake to the risk of predation

According to PubMed: Rattenborg NC, Lima SL, Amlaner CJ. *Nature* 1999;397(6718):397-398. [DOI 10.1038/17037](https://doi.org/10.1038/17037) (PMID 29667967).

## What the paper did

Recorded EEG and eye state in mallard ducks sleeping in a row of four, comparing birds at the **edge** of the group (exposed on one flank) with birds at the **centre** (flanked by conspecifics on both sides) -- a clean within-species manipulation of perceived predation risk that holds the environment otherwise constant.

## Core finding

Edge birds increased unihemispheric slow-wave sleep from **12.4% to 31.8%** of sleep time relative to centre birds. During unihemispheric sleep they directed the **open eye away from the group centre 86.2%** of the time -- i.e. toward the exposed flank, where a predator would come from. Birds detected approaching predators during unihemispheric sleep. The authors identify this as the first demonstration of an animal behaviourally controlling sleep and wakefulness *simultaneously in different brain regions*.

## Why this matters for GAP-9

This is the decisive source behind the synthesis's recommendation that a safety term be **graded rather than boolean**, and it is decisive because of the numbers rather than the phenomenon. The risk response here is not permit-or-refuse: it is a continuous reallocation of *how much of the system sleeps* (12.4% -> 31.8%, a shift not a switch), plus **directional steering** of the retained vigilance channel toward the threat. The bird did not sleep less; it slept differently.

It is also the point where two otherwise separate threads in this pull meet. Partial sleep under threat is only mechanically natural if sleep state is regionally decomposable -- which is exactly what Krueger 2008 and Vyazovskiy 2011 (sibling entries) establish. So the local-sleep thread is not merely an interesting divergence to note; it is the substrate that makes graded safety responses possible in the first place. REE, having whole-agent sleep, cannot do this, and the duration/depth factor is its available approximation -- which the synthesis names as an approximation rather than an equivalent.

## Where the paper's coverage ends

REE has no hemispheric or regional decomposition of its sleep state, and no sensory vigilance channel that could remain open during a sleep cycle -- during SWS/REM passes the agent is simply not stepping the environment. So the *mechanism* is not implementable in V3 at all. What transfers is the **shape of the risk response**: graded, partial, retaining a watch. The 12.4%/31.8% figures are mallard-specific under one particular group geometry and are emphatically not parameter anchors for a REE threat term. The paper is also short (a Nature brief communication) with a modest sample, and the effect has since been elaborated by the same group's later comparative work rather than replicated at scale in mallards.

## Confidence reasoning

Source quality 0.95 -- landmark *Nature* paper, clean quantitative behavioural contrast with a directional control (eye orientation) that rules out incidental asymmetry. Mapping fidelity 0.80: the response-shape finding transfers well, the mechanism not at all. Transfer risk 0.30, elevated for that reason -- there is a real hazard of over-reading this entry as licensing a partial-sleep build REE cannot support. Confidence 0.90.

## Failure signatures for the cluster

1. **Bimodal sleep across a risk gradient.** If REE implements the safety term as an all-or-nothing permit, sleep across a hazard gradient will be bimodal -- full cycles or none. Rattenborg predicts the biological response is monotone-graded in risk. Diagnostic: sleep duration or depth as a function of threat magnitude should be continuous and monotone; a step function is the signature of a boolean-only implementation.

2. **Undirected vigilance.** A weaker signature, recorded for completeness: the biological response is *steered* toward the threat, not merely reduced in depth. REE has no analogue today, but if a partial-sleep capability is ever built and its retained channel is threat-agnostic, that is a departure from the finding rather than a simplification of it.
