# Literature Summary: 2026-03-22_mech030_predictive_coding_rem_hobson2012

## Claims Tested

- `MECH-030`

## Source

- Hobson JA, Friston KJ (2012). *Waking and dreaming consciousness: Neurobiological and functional considerations*.
  Progress in Neurobiology.
- DOI: `10.1016/j.pneurobio.2012.05.003`
- URL: `https://www.sciencedirect.com/science/article/pii/S0301008212000919`
- **Note on source confidence**: Hobson and Friston co-authored multiple pieces during 2012-2014. The DOI listed
  is the best candidate for this specific synthesis, but readers should verify article content directly.

## Source Wording

Hobson and Friston apply the free energy principle (active inference) to the neurobiology of waking and dreaming.
Their central argument: waking consciousness is a tightly constrained inference process -- sensory prediction errors
drive rapid updates to beliefs, with precision tightly regulated by aminergic neuromodulators (noradrenaline, serotonin)
that amplify sensory input. REM sleep inverts this arrangement: aminergic suppression reduces precision assigned to
sensory channels, effectively lifting the constraint that waking sensory input imposes on the generative model.

In this unconstrained state, the generative model can explore and revise its hyperparameters -- especially the precision
priors that determine how strongly each source of prediction error is weighted. Dreams, on this account, are the
experiential correlate of this unconstrained prior exploration: the model generates predictions that are not anchored
to actual sensory input, allowing it to test and update the structural parameters of the generative model in ways that
online sensory-driven inference cannot achieve.

REM thus serves as the complement to NREM systems consolidation: NREM transfers specific episodic content; REM updates
the structural parameters (priors, precision weights) that determine how future episodes are processed.

## REE Translation

MECH-030 claims that the offline sleep mode recalibrates mode boundaries. The mode boundaries in REE are precisely
the precision-weighted prior parameters that determine when the system transitions between deliberative, committed,
and evaluative regimes. Hobson & Friston's REM account provides the biological precedent for an offline phase
dedicated to recalibrating exactly these structural parameters:

1. **Aminergic suppression = commit signal suppression.** During REM, the neuromodulatory systems that amplify
   sensory prediction error and drive online action are suppressed. This is the biological analog of the commit
   boundary protection required by ARC-020: no new irreversible actions can be committed while the system is in
   the offline recalibration phase.

2. **Unconstrained prior exploration = mode boundary recalibration.** The lifted sensory constraint during REM
   allows the generative model to adjust its hyperparameters. In REE terms, this is the mechanism by which
   alpha_k precision priors and mode transition thresholds can be updated without the risk of those updates
   being immediately expressed as action commitments.

3. **Complementarity with NREM.** The SHY + systems consolidation literature (TRK-01, TRK-02) covers the
   episodic content layer; Hobson & Friston cover the structural parameter layer. MECH-030 requires both:
   episodic replay (trajectory and residue integration) and structural recalibration (precision priors,
   mode boundaries).

## Caveat

MECH-030 is explicitly V4 scope -- not implemented in V1, V2, or V3 REE substrates. This entry is
architectural motivation only.

The Hobson-Friston account is theoretical synthesis, not primary data. The specific claim that REM updates
precision hyperparameters is inferred from the active inference framework applied to known REM neurophysiology;
it is not a directly measured result. The predictive coding interpretation of REM remains debated, and alternative
accounts (e.g., threat simulation, memory integration without hyperparameter update) are also supported. REE
architectural decisions about mode boundary recalibration should treat this as one framework among several, not
a settled mechanistic account.

The "unconstrained prior exploration" function has no direct computational analog in current REE substrates.
Specifying what this means in the REE implementation (e.g., what parameters are updated, by what gradient signal,
with what selectivity) is a V4 design question that remains open.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.74`
