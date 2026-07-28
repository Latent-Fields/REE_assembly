# Inactivation of the infralimbic prefrontal cortex reinstates goal-directed responding in overtrained rats (Coutureau & Killcross, Behav Brain Res 2003)

## What the paper did

Rats were given extended instrumental training on a lever-press for food -- enough training that responding had gone habitual, in the technical sense of no longer tracking the value of the outcome. Bilateral cannulae were then implanted over infralimbic cortex. After reminder training, animals received either muscimol (temporarily silencing infralimbic cortex) or vehicle, and were tested for goal sensitivity by specific-satiety devaluation of the instrumental outcome followed by an extinction test.

The vehicle-infused animals behaved as overtrained animals do: they kept pressing regardless of whether the outcome had been devalued. The muscimol animals showed *selective sensitivity to devaluation* -- they pressed less for the devalued outcome. Silencing infralimbic cortex had, in the authors' words, produced "a reinstatement of goal-directed responding".

## Findings relevant to MECH-324

The value of this paper for us is convergence. Smith et al. 2012 established the same functional role for infralimbic cortex using optogenetics in a T-maze; this is a different method (pharmacological inactivation), a different task (single-lever instrumental responding), a different assay (specific-satiety devaluation rather than run-pattern analysis), and a different laboratory, arriving at the same place. For a claim with `v3_pending: True` and no experimental evidence at all, the strength of the biological warrant matters, and independent convergence is worth more than a second paper from the same group.

The specific finding that bears on MECH-324's 2026-07-27 correction is what the goal-directed system looked like when it came back. It came back *intact*. Extended overtraining had not degraded the action-outcome representation -- it had merely stopped it being expressed, and the moment infralimbic cortex was silenced it was immediately and selectively usable. That is the retention property viewed from the other side: Smith et al. showed the suppressed *habit* survives, and this shows the suppressed *alternative* survives too. Nothing in habitisation destroys anything.

## How this translates to REE

MECH-324's maintenance operator gates whether a formed chunk crystallises and becomes selectable, with the underlying primitives always available. When maintenance is off -- the registered ARM_2 -- chunks form but never become selectable, and behaviour should fall back on the primitives. That is the substrate shape of what these two papers jointly describe.

But I want to flag a divergence rather than let the mapping read cleaner than it is. Coutureau and Killcross do not conclude that infralimbic cortex *enables the habit*. They conclude that "the development of habitual responding reflects the active inhibition of goal-directed responses that are mediated by action-outcome associations." On their account, IL suppresses the goal-directed system, and silencing IL releases it. MECH-324 implements something different: the chunk's own selectability is gated, and the primitives are never inhibited, merely out-competed.

These two architectures produce the same behaviour under the manipulations tested here -- habit when IL is intact, goal-directed when it is not -- which is why the phenomenon transfers. They are not the same mechanism, and they will come apart under any manipulation that dissociates release-from-inhibition from loss-of-chunk-selectability. Whether REE's version is wrong or merely different is not something this paper can settle, and I would not want a governance reader to take the entry as endorsing the implementation at that level of detail. It endorses the phenomenon.

There is a further consequence for the open MECH-321 question the claim's own notes raise -- how dissolution should interact with decomposition on the same chunk. This paper argues the constituent action-outcome representations remain fully available and undamaged throughout habitisation. That is an argument for the conservative default already chosen (decomposition is single-execution-only, the chunk stays CRYSTALLISED), and against the aggressive alternative where every decomposition incident triggers DISSOLVING.

## Limitations and caveats

Muscimol inactivation is spatially and temporally coarse next to the optogenetic result, and the test comparison is between-subjects rather than within-animal reversible, so the case for causal specificity rests more on the 2012 PNAS paper than on this one. The behavioural object is also much simpler: a single lever press is a long way from a multi-step policy chunk, and the granularity jump is the main transfer risk.

And, as with the other entry in this folder, nothing here touches MECH-324's asymmetric hysteresis band or `f_reacq`. Those remain uncalibrated engineering defaults, and the literature on file does not constrain them.

One methodological point worth carrying into experiment design. What made this result legible was the devaluation probe -- without it, the muscimol and vehicle animals' raw press rates would not have told the story. REE currently has no analog. A validation experiment that measures only chunk selection frequency cannot distinguish "the chunk dissolved" from "the chunk simply was not selected on these trials". Some outcome-sensitivity probe is the discriminating measure, and it is not yet registered.

## Confidence reasoning

0.76, a little under the Smith et al. entry. Source quality is solid rather than exceptional -- specialist journal, coarser manipulation, between-subjects test. Its contribution is convergent validity, which is exactly what a `v3_pending` claim with zero experimental evidence most needs. Mapping fidelity is held at 0.72 by the active-inhibition divergence, which I think is a genuine architectural difference and not a matter of phrasing.
