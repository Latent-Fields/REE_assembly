# Krueger et al. 2008 -- Sleep as a fundamental property of neuronal assemblies

According to PubMed: Krueger JM, Rector DM, Roy S, Van Dongen HPA, Belenky G, Panksepp J. *Nature Reviews Neuroscience* 2008;9(12):910-919. [DOI 10.1038/nrn2521](https://doi.org/10.1038/nrn2521) (PMID 18985047).

## What the paper argues

A review and formal proposal arguing against the classical picture of sleep as a state imposed top-down by a central controller. The authors marshal the local-sleep-regulatory-substance literature (ATP, cytokines, adenosine released as a function of local neuronal activity) and present a mathematical model in which individual cortical columns switch between wake-like and sleep-like states as a function of their own recent use, coupling to one another humorally and electrically.

## Core claim

Sleep "seems to be a fundamental property of neuronal networks and is dependent on prior activity in each network." Whole-organism sleep is an **emergent property** of many local units synchronising -- not a global set-point that the units obey.

## Why this matters for GAP-9

This is the strongest single source behind the synthesis's Verdict 1, and it reframes GAP-9's question rather than just answering it. "What global signal should trigger sleep?" presupposes a central controller that the biology does not appear to have. The honest V3 position that follows is not that REE's single MEL scalar is wrong, but that it is a **coarse stand-in for an emergent aggregate**, adopted for tractability with the divergence recorded.

The review also constrains the *direction* of any future refinement, which is its most actionable content. If REE ever builds per-region sleep need, Krueger says to **aggregate upward from per-region demand**, not to subdivide a global budget downward. Those two implementations look similar on a whiteboard and behave very differently: a subdivided fixed budget caps how much offline effort any single high-demand region can receive, which is the opposite of the use-dependent behaviour Huber 2004 (in corpus) measured.

Alongside Vyazovskiy 2011 (its empirical companion in this pull), it also supplies the mechanistic reason partial sleep is possible at all -- which is what makes the graded risk responses in Rattenborg 1999 and Tamaki 2016 coherent rather than exotic.

## Where the paper's coverage ends

This is a theoretical framework, and the local/emergent account remains contested against centrally-controlled models; the review is advocacy for a position, not a settled consensus. It specifies no parameter anchors -- how many units, what coupling strength, what aggregation function -- so it constrains architecture direction only. It is also silent on the allostatic/safety axis entirely: nothing here bears on whether risk should gate sleep, which is a separate input handled by the Lima 2005 and Loftus 2022 entries in this pull.

## Confidence reasoning

Source quality 0.90 -- *Nature Reviews Neuroscience*, heavily cited, authored by the originators of the local-sleep account including Panksepp. Mapping fidelity 0.85, good because the paper's claim is architectural and GAP-9's open item is explicitly an architectural decision rather than an empirical unknown. Transfer risk 0.25 -- the account is contested, and REE has no columnar substrate to instantiate it. Confidence 0.85.

## Failure signatures for the cluster

1. **Top-down subdivision instead of bottom-up aggregation.** If REE later builds per-region sleep need by allocating shares of a fixed global budget rather than aggregating per-region demand upward, Krueger predicts saturation: regions with genuinely high demand cannot exceed their share, so consolidation flattens. Diagnostic: check whether summed per-region offline effort is constant across arms with different demand profiles -- a constant sum is the signature of the wrong construction.
