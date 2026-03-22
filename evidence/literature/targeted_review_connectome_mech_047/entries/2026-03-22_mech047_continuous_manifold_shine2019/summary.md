# Literature Summary: 2026-03-22_mech047_continuous_manifold_shine2019

## Claims Tested

- `MECH-047`

## Source

- Shine JM, Bissett PG, Bell PT, Koyejo O, Balsters JH, Gorgolewski KJ, Moodie CA, Poldrack RA (2019). *Human cognition involves the dynamic integration of neural activity and neuromodulatory systems*. Nature Neuroscience.
- DOI: `10.1038/s41593-018-0312-0`
- URL: `https://www.nature.com/articles/s41593-018-0312-0`

## Source Wording

Using 7T task-fMRI during a cognitive flexibility paradigm, the authors apply PCA to whole-brain connectivity matrices and find that transitions between task conditions trace smooth, low-dimensional trajectories through a 2-3 dimensional manifold rather than jumping between discrete, separable states. The first manifold dimension correlates strongly with task demand and with pupil-linked arousal (a non-invasive proxy for LC-NE activity). The authors argue that the apparent discreteness of cognitive states (task-on / task-off) is an artifact of coarse labelling: the underlying neural dynamics are continuous, with arousal serving as a continuous modulator of position along the integration-segregation axis. Transitions between conditions produce traversals of this manifold at rates that depend on the magnitude of the arousal shift, but there is no evidence of a sharp switching threshold or hysteretic barrier.

## REE Translation

MECH-047 (mode-commitment hysteresis with discrete mode gates): Shine et al. constitute the primary challenge to MECH-047 in this literature set. The discrete three-mode model assumes that doing, ready-vigilance, and default-mode are separable attractor states with a well-defined gate between them. If neural dynamics are instead continuous manifold traversals, then: (1) there may be no sharp moment of mode entry at which hysteresis kicks in; (2) the switching cost may be better modelled as a continuous function of arousal-manifold position rather than a binary threshold crossing; (3) the three mode labels may not correspond to separable attractors but to regions of a continuum.

The partial support comes from the finding that LC-NE (pupillometry proxy) predicts manifold position and modulates transition rate. This is consistent with MECH-047's arousal-gating claim: LC-NE does gate transitions, even if the transition is not discrete. The challenge is therefore at the level of architectural framing (discrete vs. continuous) rather than a falsification of arousal gating. A continuous-manifold reformulation of MECH-047 -- in which hysteresis is implemented as position-dependent switching probability along the arousal manifold -- would be fully consistent with Shine et al. and would retain the core phenomenology of mode commitment.

## Caveat

The cognitive flexibility paradigm (task switching between conditions) is not an analogue of the REE three-mode cycle. REE default-mode (planning/simulation) is a distinctly internal, stimulus-independent state that Shine et al.'s task did not include; the manifold may show sharper structure when default-mode DMN is included. Manifold dimensionality reduction (PCA) can obscure discrete attractors if the between-attractor variance is small relative to within-attractor variance; the continuous appearance could be an artifact of compression. The pupillometry LC-NE proxy is indirect and has known confounds (task-evoked pupil dilation, luminance). These caveats limit the strength of the challenge: the evidence weakens the discrete-gate architecture but does not falsify hysteresis as a functional property.

## Direction and Confidence

- `evidence_direction`: `mixed`
- `confidence`: `0.71`
