# Lima, Rattenborg, Lesku & Amlaner 2005 -- Sleeping under the risk of predation

Lima SL, Rattenborg NC, Lesku JA, Amlaner CJ. *Animal Behaviour* 2005;70(4):723-736. [DOI 10.1016/j.anbehav.2005.01.008](https://doi.org/10.1016/j.anbehav.2005.01.008). (Not indexed in PubMed; citation verified against the publisher record and the authors' institutional listing.)

## What the paper argues

The canonical review of the sleep-and-predation literature, by the four authors who established the field. It evaluates and largely rejects the older idea that sleep exists *to serve* an antipredator function (keeping animals immobile and hidden), and replaces it with the inverse framing: sleep imposes an unavoidable **vulnerability**, and understanding how animals manage that vulnerability illuminates both the function and the architecture of sleep.

## Core claim

The predatory environment is a determinant of sleep **architecture and timing**. Species in riskier environments spend less time in the most vulnerable sleep states. Critically, sleep need is **traded off against survival rather than abolished**: antipredator pressure *reorganises the expression* of sleep -- which states, how deep, when, where -- rather than suppressing it.

## Why this matters for GAP-9

It answers the chip's third question affirmatively and, more usefully, constrains the *shape* of the answer.

**Affirmative:** safety is a legitimate and biologically necessary input to sleep onset, distinct from accumulated need and from timing. That ratifies MECH-286's existence as a permission object with its own flag and call site, separate from the K/MEL cadence machinery -- an architectural separation REE already has and which this synthesis endorses rather than proposes.

**Constraining:** the trade-off framing is an argument against MECH-286's current **boolean AND** form. Real animals under risk do not refuse sleep; they reallocate it. In REE terms the natural home for a threat term is therefore the existing continuous duration/depth lever (`MELConsumer.scale_steps`, which already scales `sws_consolidation_steps` and `rem_attribution_steps`) rather than -- or in addition to -- a permit flag. This is the cheap recommendation: the lever exists, and a threat multiplier on it degrades to current behaviour at 1.0.

Read together with the corpus's existing Lima & Bednekoff 1999 risk-allocation entry (`targeted_review_arc_062_refuge_forage_ecology/`, pulled originally for foraging), the pair gives the strongest form of the argument: under *chronic* high risk, antipredator effort drops because the animal must feed sometime -- transferred to sleep, a hard boolean gate would starve sleep exactly in the worlds where the agent spends its life in danger.

## Where the paper's coverage ends

A comparative and field review across birds and mammals, so it establishes patterns rather than mechanism, and its quantitative content is species-specific and not a source of REE parameter anchors. More importantly for transfer: half of what the paper is about is differential vulnerability across sleep **states** (REM being more vulnerable than NREM -- atonia, raised arousal thresholds), and REE has no analogue of this. Its SWS and REM analogues are not differentially vulnerable in any embodied sense; the agent is equally unresponsive in both. So the architecture-reallocation half of the finding transfers only weakly, while the timing-and-duration half transfers well. The synthesis relies on the latter.

## Confidence reasoning

Source quality 0.95 -- the canonical review in a leading behavioural journal, by the field's founding authors, broad rather than single-species. Mapping fidelity 0.82, reduced because REE lacks the differential-vulnerability structure that a substantial part of the paper addresses. Transfer risk 0.25 -- the general trade-off logic is species-general and transfers cleanly; the state-architecture specifics do not. Confidence 0.90.

## Failure signatures for the cluster

1. **Sleep starvation under chronic risk.** If a safety term is added to REE sleep onset as a hard boolean AND, and a run in a persistently hazardous environment shows sleep never firing, Lima 2005 (with Lima & Bednekoff 1999) says this is a modelling error rather than a correctly-modelled trade-off. Diagnostic: plot sleep-cycle count against hazard density; a floor pinned at zero for high density is the signature, and it will be easy to misread as a broken trigger.

2. **Invariant sleep expression across risk regimes.** Conversely, if sleep duration and timing are completely unaffected by hazard exposure once a permit is granted, the allostatic input is not reaching the expression machinery at all -- the gate is binary-only and the reorganisation half of the finding is unimplemented.
