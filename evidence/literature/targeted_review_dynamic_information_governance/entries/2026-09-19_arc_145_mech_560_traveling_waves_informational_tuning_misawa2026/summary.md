# Misawa et al. 2026 -- traveling waves, informational tuning, and the selectivity/volume dissociation

This is the trigger paper for the whole 2026-09-10 dynamic-information-governance family, and until now it
had never been fetched: ARC-145's notes record it as reached via a Popular Mechanics article and marked
`LITERATURE ANCHOR, UNVERIFIED`. It is verified here. The citation is exact -- *iScience* 29(8):116728,
doi 10.1016/j.isci.2026.116728, PMID 42472099, PMC13380430, authors Misawa, Chinen, Kawabata, Kaiju, Suzuki
and Komura -- and the paper says what the claim notes say it says.

What the authors did: they built a 116-channel ultra-thin sheet ECoG array covering almost the entire right
hemisphere and recorded visual-evoked potentials to LED stimulation of the left eye, in 45 sessions from 10
head-fixed rats, awake and under isoflurane. Note the species, because no REE document currently records it:
this is rat, not primate. Traveling waves were extracted by generalised-phase analysis, clustered into
motifs, and their relation to directed information flow quantified by transfer entropy normalised against
pairwise mutual information. Awake cortex showed more stable evoked waves, a richer repertoire of widespread
motifs, and transfer entropy more sharply tuned to the direction of wave propagation. The authors name the
last of these *informational tuning* and propose it as a general framework for the geometry relating neural
and informational flows.

The finding that actually matters for REE is in the supplement rather than the abstract, and it is the one
MECH-560's notes lean on hardest: **overall transfer-entropy magnitude was significantly higher under
anaesthesia than during wakefulness** (Fig. S7A), which the authors explicitly invoke to rule out the
possibility that awake selectivity is a by-product of greater transfer. That is precisely the shape MECH-560
asserts -- organisation of directed influence dissociating from the amount transferred -- and it is a
stronger result than the abstract alone would support. It also vindicates the tension MECH-560's notes flag
with MECH-227 (anaesthesia as global D_V collapse): in this preparation, anaesthesia did not reduce total
transfer, it increased it. A session that had verified only the abstract would have missed this and might
reasonably have concluded the claim note over-read its source. It does not.

How far does this carry? Not far, and deliberately so. Per `feedback_lit_exp_decoupled`, a paper that
resembles REE raises no claim's confidence, and nothing here is evidence about an REE engine. Three specific
limits are worth stating rather than leaving implicit. First, there is no task: the animal views a flash, so
ARC-145's third property -- that a routing state grants the sender causal privilege over a receiver *at that
moment*, with respect to some decision -- is not tested against any decision at all. Second, the selectivity
measure is a property of electrode-pair information flow, not of behavioural competence, so MECH-560's
behavioural half (integrated behaviour degrading in proportion to lost selectivity at matched traffic) gets
no support here beyond plausibility. Third, for MECH-561 the paper is close to silent: a traveling wave is a
phase gradient and can be read as a moving window of receiver availability, which is suggestive, but nothing
in this study indexes a communication subspace by an endogenous cyclic coordinate. I have tagged MECH-561
because the wave-as-moving-read-window reading is the claim's own stated motivation, not because the paper
tests it.

Confidence 0.55. Source quality is good but not outstanding -- a novel preparation from a single lab with no
replication, in a journal that is respectable rather than top-tier. The binding constraint is mapping
fidelity: the honest translation is "the dissociation MECH-560 posits is a real, measurable phenomenon in at
least one biological system", which is worth having and is much less than support for the claim. MECH-560's
existing instruction stands and this entry does not discharge it: `informational tuning` must not be treated
as equivalent to RF(t) or TI(t) without an explicit methodological mapping, which nobody has yet written.
