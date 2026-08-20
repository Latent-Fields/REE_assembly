# Natural selective attention: orienting and emotion

Bradley (2009), *Psychophysiology* 46(1):1-11. DOI 10.1111/j.1469-8986.2008.00702.x. PMID 18778317. PMC3645482.

## What the paper does

This is a review, not a primary study, and I am including it for a specific, narrow purpose: SD-099's own design doc explicitly invokes "the Sokolov orienting-reflex shape" as part of its organism-level grounding, but nowhere states what that shape's actual TIME COURSE is. Bradley's review is a standard, well-cited synthesis of exactly that lineage -- the human psychophysiological orienting response as multiple dissociable components (an early cardiac-deceleration/perceptual-enhancement component, a later electrodermal action-readiness component, a still-later cortical late-positive-potential significance-detection component) rather than a single unitary reflex, each habituating at its own rate across repeated presentations.

## Why this bears on SD-099's persistence-window question

The pull's Q1b asked for a second, unit-free route to the same design decision: how does the post-decision bias persistence compare to the duration of the ORIENTING EPISODE ITSELF? This review is the grounding for that comparison's denominator. Classical psychophysiology places the orienting response's own components on a multi-second time course -- cardiac deceleration typically unfolds and peaks across several seconds post-onset, with later attentional and cortical components later still. That is the same order of magnitude as the post-decision freezing durations reported in the Shang 2018 and Vale 2017 entries in this directory (hundreds of milliseconds to tens of seconds), not two orders of magnitude smaller.

This matters for interpreting Option C specifically. If the orienting EPISODE that precedes SD-099's decision itself takes on the order of seconds to unfold and resolve (per this literature), then a post-decision bias window of 60-125ms -- Option C -- would be shorter than the very episode it is meant to follow from, which is an odd shape for a "persistence" quantity to take. Option A's 625ms-1.25s is, by contrast, comfortably within the same order of magnitude as the orienting episode's own components. I want to be careful not to overstate this: SD-099's PAG-analog gate is a much more abstract, faster-cycling mechanism than a human cardiac orienting response, and nothing here licenses treating the numbers as interchangeable. But as a plausibility check on relative ORDER OF MAGNITUDE, a bias window shorter than the eliciting episode itself is a design smell worth naming explicitly.

## Limitations

This is human autonomic and electrocortical psychophysiology -- heart rate, skin conductance, EEG -- not rodent behavior and not a behavioral action-selection bias. It says nothing directly about SD-099's approach/withdraw/resume decision or about how long a resolved decision biases subsequent choices; it only grounds the duration of the preceding orienting episode (Q1b's denominator), leaving Q1 itself to the other entries in this directory. And it is a review synthesizing a large prior literature rather than a single new measurement, so its numbers should be read as an established consensus range rather than a precise point estimate with its own error bars.

## Confidence

0.55. Source quality 0.72 -- an established, well-cited review in a core psychophysiology venue, synthesizing a mature literature. Mapping fidelity 0.50 -- directly useful for Q1b, silent on Q1, and physiological rather than behavioral. Transfer risk 0.40 -- human-to-agent and physiology-to-behavior gaps, partially offset by this being the exact theoretical lineage SD-099's own documentation already cites.
