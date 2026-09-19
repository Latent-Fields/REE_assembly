# Steel, Angeli and Robertson 2026 -- shared indexing coordinate between globally distinct networks

MECH-555's notes carry this as `EXTERNAL MOTIVATION, NOT INDEPENDENTLY VERIFIED IN THIS PASS`, taken from the
source thought's reference list. It is verified here, and a small bibliographic wrinkle is worth recording
because it will otherwise trip a future session.

The citation resolves, exactly as stated: DOI 10.7554/eLife.110234 is an eLife reviewed preprint by Steel
(Adam), Angeli (Peter A) and Robertson (Caroline E), issued 2026-09-08 -- matching the "revised 2026-09-08"
in the claim note to the day. The wrinkle is that PubMed does not index the eLife version; it indexes the
bioRxiv original (PMID 39386717, PMC11463438, doi 10.1101/2024.09.25.615084), and Crossref records the eLife
DOI as `is-version-of` that preprint. I have put the eLife DOI in `source.doi` because that is what the claim
cites, and the bioRxiv PMID/PMC alongside it because that is where the abstract is actually readable. Both
point at one paper. Separately, and this is the real trap: the same three authors published *Positive and
Negative Retinotopic Codes in the Human Hippocampus* (J Neurosci 2026, PMID 42538298) two weeks earlier. It
is a different paper and must not be conflated with this one.

The result matches the claim note almost word for word. Using densely sampled 7T fMRI with individualised
resting-state parcellations and voxel-wise population-receptive-field mapping, the authors find that although
spontaneous Default Network and dorsal-attention activity is uncorrelated *at the network level*, coupling
*across* the networks is organised by the latent visual-field preferences of individual voxels: voxels
sharing visual-field preferences couple more strongly than those with divergent preferences. Retinotopic
coding turns out to be intrinsic to the DN and persists even during elevated top-down drive from DN to dATN.

Why this is the right motivation for MECH-555 and not more than that. The claim asserts that two systems can
each contain a task distinction, expose it through a healthy communication subspace, and still fail to
communicate because they index that distinction against incompatible relational coordinates -- so reference
frame is a third interface factor beside content and subspace. What this paper supplies is the existence
proof for the positive case: globally distinct systems whose interaction *is* organised by a shared indexing
coordinate. What it does not supply is the failure case, and that is the one MECH-555 actually needs. Nobody
here permutes the frame while holding content and receiver state fixed; the evidence is correlational resting-
state structure. MECH-555's own discriminator -- a frame permutation at fixed receiver state -- remains unrun,
and the assay that would run it is owned by `hippocampal_campaign_assay_specifications_20260910.md` assay A,
not by this entry.

One further caution the abstract makes plain and a casual reading would lose: the retinotopically specific
interactions are *bivalent*. DN voxels with negative (suppressive) visual response amplitudes are
anticorrelated with matched dATN voxels, while positive-amplitude ones are positively correlated. "Shared
frame means coupling" is therefore too simple; shared frame means *structured* interaction whose sign depends
on response polarity. Confidence 0.52, discounted for preprint status and the small-N dense-sampling design.
MECH-555's own three cautions are adopted verbatim into the mapping caveat and are not softened here:
retinotopy is not to be copied, no universal coordinate vocabulary is prescribed, and a shared index across
consumers is not evidence for a global workspace.
