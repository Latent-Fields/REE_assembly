# Common Functional Brain States Encode both Perceived Emotion and the Psychophysiological Response to Affective Stimuli

**Bush, Privratsky, Gardner, Zielinski & Kilts (2018) — Scientific Reports**
DOI: [10.1038/s41598-018-33621-6](https://doi.org/10.1038/s41598-018-33621-6)
*Based on articles retrieved from PubMed*

## What the paper did

Bush and colleagues applied multivariate pattern analysis (MVPA) to fMRI data collected while participants passively viewed images from the International Affective Picture System (IAPS) -- a well-validated battery spanning a range of valence and arousal combinations. The key question was whether whole-brain functional states could predict not just the categorical emotional content of images but the continuous valence and arousal dimensions that characterise them, including the individual's own psychophysiological response (skin conductance). A secondary analysis used geometric methods to ask whether the neural encodings of valence and arousal were independent or overlapping in brain state space.

## Key findings

Brain states significantly predicted normative valence scores, normative arousal scores, and individual skin conductance responses -- all above chance. The brain state's predictive effect size was more than three times that of skin conductance alone for valence/arousal prediction, suggesting that neural patterns carry richer affective information than peripheral physiology. The geometric analysis of the regression parameters -- the neuroanatomical signature of each dimension's encoding -- found that valence and arousal loadings were orthogonal in the space of brain voxels. This directly confirms the circumplex model's core structural claim: valence and arousal are not just conceptually distinct but neurally non-overlapping in their encoding patterns.

## REE translation

Q-017 asks for the minimal orthogonal control-axis subset that preserves observed regime separations in REE's control plane. Bush et al. provide the strongest available fMRI evidence that valence and arousal are genuinely orthogonal neural dimensions -- they cannot be reduced to a single composite axis without losing information about the other. For REE, this supports treating mu/kappa (harm/benefit valence) and precision/arousal as two independent axes in the control plane, neither reducible to the other. The MVPA approach is also methodologically instructive for REE: the regime separations that Q-017 cares about are not just behavioural categories but geometrically distinct regions in latent state space. If REE's control axes are truly minimal and orthogonal, they should be recoverable from agent state representations using a similar MVPA approach.

## Limitations

Passive viewing of static IAPS images is a very constrained emotional context. Real decisions in REE involve dynamic, multi-step interactions where valence and arousal co-vary in ways that static images do not capture. The orthogonality result applies to the neural encoding space of a passive viewer -- there is no reason to assume it holds in the action-generation state space of an active agent under threat or commitment pressure. The study also tests only two axes; REE posits additional control dimensions (commitment state, goal salience, precision weighting) whose independence from valence and arousal is not tested here. Finally, n=19 is a modest sample for a geometric claim about neural encoding structure.

## Confidence reasoning

I rate this 0.72. The finding is directly relevant: it is the clearest available fMRI evidence that the core circumplex axes are orthogonally encoded. The geometric analysis is a genuine contribution beyond correlational claims. The confidence penalty comes from the passive/static context, the small sample, and the restricted scope -- showing that two axes are orthogonal does not tell us whether the full set of REE control axes is minimal.

## Considered for MECH-142, not tagged (2026-08-10)

MECH-142 ("Valence-arousal axis orthogonality in the control plane is not a static geometric property but requires active cholinergic maintenance during learning; without it, axes drift toward correlation under repeated co-activation") cites this paper in its `notes` field as part of the orthogonality evidence it was built from. On review, `claim_ids_tested` was deliberately left as `["Q-017"]` rather than extended to include MECH-142: this study is a single-session passive-viewing paradigm with no learning manipulation and no cholinergic measure, so it can show that valence and arousal are orthogonal in one snapshot, but it cannot speak to whether that orthogonality is actively maintained over time or would drift under repeated co-activation without a gating mechanism -- the actual content of MECH-142's hypothesis. It supports MECH-142's background premise (orthogonality exists to be maintained) and MECH-063's orthogonal-axes commitment, but not MECH-142's mechanism claim itself. See the Gonzalez-Redondo et al. (2025) entry in this same directory, which was extended to MECH-142 on 2026-08-10 because it directly tests a gated-vs-ungated contrast.
