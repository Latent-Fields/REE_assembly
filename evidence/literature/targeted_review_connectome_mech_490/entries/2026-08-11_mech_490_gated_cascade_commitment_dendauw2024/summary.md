# Dendauw et al. (2024) — the gated cascade diffusion model (architecture grounding, non-sleep)

This paper is included for a different reason than the other three entries in this pull. Where
those speak to whether *sleep* modulates sequence-execution fluency, this one speaks to whether
the *commit-gate architecture itself* — the thing MECH-490 proposes sleep might modulate — is a
real, independently discovered feature of human decision-making, rather than a REE-specific
design choice with no biological analogue. Dendauw and colleagues extend the standard
drift-diffusion model of decision-making with a motor-level gate: accumulated evidence is
smoothed into a motor-preparation signal that is held back from triggering muscle activation
until it crosses a threshold, at which point the system commits and executes. They validate this
against joint reaction-time and EMG dynamics across four separate decision domains (motion
perception, numerical comparison, recognition memory, lexical decision), and the model fits
better than competing diffusion-model variants across all four.

The structural parallel to E3Selector is close: accumulate a decision variable, smooth it,
gate it against a threshold, commit, then execute without further re-accumulation for that
action — which is exactly `commit_variance < effective_threshold` followed by walking
`_committed_step_idx` through a plan without re-running CEM/softmax. That parallel is worth
having on record: it means REE's commit-gate is not an ad hoc computational convenience but an
instance of a mechanism independently found in human decision-motor coupling.

What this paper cannot do is speak to MECH-490's actual claim, which is about *sleep*. There is
no sleep, consolidation, offline-processing, or even time-of-day content anywhere in it — every
task is tested within a single session. It is marked `evidence_direction: unknown` rather than
`supports` for exactly that reason: it grounds a precondition of the claim (the gate architecture
is real) without touching the causal claim itself (sleep changes the gate's persistence). It also
tests single discrete responses, not multi-tick open-loop execution of an extended sequence, so
even the architectural analogy is structural rather than a direct empirical match. Read this
entry as "the gate concept is not made up," not as "sleep evidence" — conflating the two would
overstate what the paper shows.
