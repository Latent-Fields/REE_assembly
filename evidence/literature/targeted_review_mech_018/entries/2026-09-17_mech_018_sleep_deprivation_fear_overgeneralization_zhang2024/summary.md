# Sleep deprivation increases the generalization of perceptual and concept-based fear

## What the paper did

Zhang and colleagues built a fear-conditioning paradigm that separates two ways a threat memory can
spread. Perceptual cues were colours (navy blue and olive green, as P+ and P-); conceptual cues were
semantic categories (animals and furniture, as C+ and C-). After acquisition at 21:00, participants
either slept normally or underwent one night of total sleep deprivation, and were tested at 07:00 on
four novel generalised combinations: C+P+, C+P-, C-P+, C-P-. Shock-expectancy ratings, skin
conductance and functional near-infrared spectroscopy were recorded throughout. The deprived group
showed higher shock expectancy -- most clearly for P+ and C- -- along with increased oxygenated
haemoglobin in dorsolateral prefrontal cortex and increased triangular inferior frontal gyrus
activation during the generalisation test. The authors read this as a model of the
over-generalisation seen in anxiety and fear-related disorders.

## Why this bears on MECH-018

MECH-018's second readout is the one that carries the claim's clinical meaning: sleep is supposed to
stop a harm signal spreading to contexts that merely resemble the one where harm occurred. REE names
the failure mode directly -- spurious guilt. This paper is the human contrapositive. Take sleep away,
and the fear spreads.

What makes it a better fit than most of this literature is the factorisation. REE's residue field
over-generalises geometrically: RBF kernels centred on harm locations overlap neighbouring
non-harm locations in z_world, and the specificity ratio measures how badly. But a well-built agent
should also be able to generalise along learned structure rather than raw proximity -- that is what
context-tying means. Zhang et al. separate exactly those two axes and find sleep deprivation
degrading both. That is the right shape: sleep is not merely narrowing the kernel, it is maintaining
a distinction between "near in feature space" and "belongs to the same threat context".

## The limitation that governance should weight most

Deprivation designs answer a different question from the one MECH-018 asks. Removing sleep shows
that sleep is NECESSARY for specificity to be maintained. It does not show that any operation
running inside a sleep cycle PRODUCES that specificity. The distinction is not pedantic here,
because MECH-018's own SUBSTRATE note says plainly that `ResidueField.integrate` exists but is not
called from `SleepLoopManager._run_cycle`, and that the live question is whether wiring the call
site delivers anything. A purely passive account -- that waking updates keep smearing the field, and
sleep helps only by being an interval in which no smearing happens -- predicts the identical human
result. That passive account is the null MECH-018 has to beat, and this paper cannot beat it for us.

It follows that the REE experiment must not be designed as sleep-versus-no-sleep alone. MECH-018 has
already got this right by requiring a NAIVE-DECAY comparator alongside the no-sleep arm. This entry
is a reminder of why that second arm is not optional bookkeeping: without it, a passing result is
uninterpretable in precisely the way this otherwise-good human study is.

## Further caveats

fNIRS is a coarse modality with shallow cortical penetration and cannot see the amygdala or
hippocampus, so the neural half of the result constrains little. The effects concentrated on P+ and
C- rather than spreading uniformly across the four generalised categories, which a clean
over-generalisation account does not obviously predict and the authors do not fully explain. And the
direction reported here is not uncontested: Davidson et al. (2016, PMID 26359128), whose entry sits
alongside this one in this directory, used a within-modality generalisation gradient across a nap
and found no sleep-versus-wake difference at all.

## Confidence

0.55. On the claim's crux readout and in the claim's favour, with a paradigm whose structure maps
unusually well onto REE's geometry -- but built on a deprivation logic that cannot distinguish the
active operation MECH-018 asserts from the passive interval it would have to beat, and contradicted
by at least one competent null in the same directory.
