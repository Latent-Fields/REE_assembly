# Forschack et al. (2022) -- Target facilitation without distractor suppression in two-stimulus search displays

## What the paper did

The signal suppression hypothesis holds that salient distractors are proactively suppressed below baseline before they can capture attention -- a genuinely pre-selection inhibitory process. Testing it requires a baseline that is neither target nor distractor, and this study supplies one: task-irrelevant filler stimuli in a third colour. Participants viewed randomised two-item displays -- target plus distractor, or a filler pair -- embedded in an ongoing stream of flickering grey circles. Attention was indexed two ways at once, by steady-state visual evoked potentials driven by the flicker and by perturbations of endogenous alpha.

## Key findings relevant to Q-082

Both measures converged against early proactive suppression. Salient distractors were not pushed below the filler baseline. What the data showed instead was initial capture by every colour-change stimulus -- targets, distractors and fillers alike -- followed by a later narrowing of attention onto the target. That is target facilitation, not distractor suppression.

## How this translates to Q-082

Q-082 asks whether REE needs an explicit pre-selection suppression substrate or whether precision-weighted cue routing plus the MECH-254 top-k boundary bottleneck already suffices. This entry is evidence for the second horn, and it is the reason I did not let the Mysore & Knudsen entry stand as the directory's verdict. The human electrophysiological case for a dedicated proactive suppression signal is weaker than its prominence suggests, and the pattern that survives -- everything competes, then the target is upweighted -- is close to what a precision-weighted competition with a capacity bottleneck would produce without any suppression machinery at all.

Read alongside the McPeek entry, a coherent alternative picture emerges: suppression is not a separate stage but the shadow cast by facilitation within a competitive map, and its residue at commitment time is what actually matters behaviourally.

## Limitations and confidence

This is a null result and I want to hold it at its true weight rather than let it do more work than it can. A two-item display is close to the minimum competition a search task can pose; suppression may simply not be recruited until competition is stronger, and appear at larger set sizes. Absence of an SSVEP or alpha signature is also not absence of suppression -- both are coarse population measures relative to the single-unit competition that McPeek and Mysore & Knudsen resolve. The van Moorselaar entry in this directory bears on the same dispute from the opposite direction, showing that the distractor positivity usually cited *for* suppression is partly attributable to target upweighting, which is convergent with this null but does not remove the possibility that some suppression is real.

There is one forward-looking implication worth recording. If suppression is what appears when competition gets strong, then the question for REE is a scaling question: does the top-k boundary bottleneck hold up as the number of competing candidates grows, or does it degrade in a way that a suppression substrate would have prevented? That is a sharper framing of Q-082's second horn than the claim currently carries.

None of this licenses building anything. Q-082 is registered as a gated open question behind MECH-467 leg 3, with explicit do-not-build and do-not-queue instructions, and this entry is grounding for the question rather than progress toward closing it.

Confidence 0.69.

*Retrieved via PubMed. [DOI](https://doi.org/10.1093/cercor/bhab450)*
