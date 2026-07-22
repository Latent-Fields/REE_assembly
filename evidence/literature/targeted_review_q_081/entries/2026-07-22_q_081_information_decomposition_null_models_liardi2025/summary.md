# Null models for comparing information decomposition across complex systems (Liardi et al., 2025) -- Q-081, INV-091

## What the paper did

Partial Information Decomposition splits the information a set of sources carries about a target
into redundant, unique and synergistic parts. It has become the standard tool for asking whether a
system is integrated, and Liardi and colleagues point out that people have been reading its output
wrong.

The problem is that atom values depend on how much total information is flowing, not only on how it
is organised. Their demonstration is clean: take two systems with identical source-target
structure, change only the noise level, and the decomposition flips from synergy-dominated to
redundancy-dominated. Nothing about the organisation changed. The obvious repair -- divide by total
mutual information -- fails, because synergy, redundancy and unique information each scale
differently with noise, so normalisation by TMI presumes a linearity that is not there.

Their fix is NuMIT: rather than comparing raw atoms, compare a system's atoms against an ensemble
of randomly generated systems constrained to have the *same* total mutual information, and report
each atom as its quantile in that null distribution. For Gaussian systems the ensemble is generated
by tuning a noise parameter to match the observed TMI while randomising covariances; for VAR models
by rescaling the spectral radius. Validated against synthetic systems where the ground truth is
known; applied to 48 subjects under LSD, ketamine and psilocybin, where an increase in synergy
turns out to be visible only after normalisation. Agreement between three different PID definitions
(MMI, CCS, DEP) rises from roughly rho 0.4 to above 0.7 once normalised. MATLAB implementation
released.

## Why this belongs in the Q-081 directory

Q-081's directory already holds Lancaster et al. 2018 on surrogate construction. That entry governs
one half of the null problem: how to build a surrogate that preserves each stream's own temporal
structure while destroying only the cross-stream relation. This paper governs a different half, and
for INV-091 it is the more dangerous one.

INV-091's falsifier is an **ablation series** -- remove event broadcasts, remove mode conditioning,
remove commitment landmarks, remove residue feedback, force lockstep, randomise rates, collapse the
harm streams -- required to produce a *non-monotonic* relation between cross-stream similarity and
function. That design compares a statistic across arms. And every one of those ablations changes
how much information is flowing through the system. If the statistic is from the PID family, this
paper says the comparison is invalid before it starts: an arm with more noise will read as more
redundant than an arm with less, with the organisation untouched.

The failure mode is worse than a null result, because it is a *positive* one. An unnormalised
ablation series across seven arms with seven different total-information levels could produce a
beautifully non-monotonic curve that is nothing but TMI varying across arms -- INV-091 apparently
confirmed by an artefact, in a cluster where every claim currently sits at exp_conf 0.0 and a first
positive result would carry disproportionate weight. That is exactly the kind of outcome the
cluster's existing entries (Hancock's necessary-but-not-sufficient warning, Vidaurre's
scheduler-null problem) were written to forestall, arriving by a route none of them cover.

Four things follow for the prospective run, if it uses a PID-family statistic:

1. Fix and **name** the PID definition in advance. The three definitions disagreed at rho ~0.4 on
   raw atoms; leaving the choice implicit makes the result unreproducible.
2. Report atoms as **NuMIT quantiles**, not raw values.
3. Report **total mutual information per arm** alongside every atom, so a reader can see whether it
   moved and by how much.
4. Treat any non-monotonicity that **disappears under normalisation** as refuted, not as noise.

## Limitations, and why this is a correction rather than a solution

Two caveats, and the second is the one that keeps this from being the last word on nulls.

The validation is on linear-Gaussian and VAR(1) systems. The authors state directly that non-linear
relationships are essential and not addressed here, and that extending to VAR(p) for p > 1 is
computationally intensive. REE's streams are nonlinear, and non-stationary across training. The
normalisation's calibration in our regime is assumed, not shown.

More fundamentally, the nulls preserve total mutual information *and nothing else* -- all structure
is randomised. The authors concede that whether such ensembles resemble real systems is open, and
that "biologically meaningful null models remain unknown". So NuMIT removes one specific,
demonstrated confound. It does not supply a REE-plausible null. Pairing it with the
constrained-realisation surrogates from the Lancaster entry is doing two different jobs -- one
controls what the surrogate preserves within streams, the other controls the comparability of the
decomposition across arms -- and neither substitutes for the other.

The neuroimaging application is human pharmacological data, so GOV-ANALOGY-1 applies to that
portion. But the load-bearing content is a mathematical result about how an estimator behaves,
which is substrate-independent and is what search 10 was looking for.

## Confidence reasoning

0.72. Strong source, released code, validated against synthetic ground truth where the right answer
is known, and a confound that lands squarely on the specific falsifier INV-091 already commits to.
The main reason it is not higher is that REE has not yet chosen a PID-family statistic -- if the
prospective run uses a different family (DSA, transition matrices, event-locked alignment) this
entry constrains it only by analogy, though the general lesson that a cross-arm statistic must be
calibrated against arm-specific information throughput survives the change of family.

Direction is `supports` in the methodological sense: it strengthens what INV-091's falsifier would
have to look like to be believable. It says nothing about whether the band exists.

lit_conf only. exp_conf on Q-081, MECH-466, INV-091 and ARC-112 remains 0.0 -- nothing in cluster A
has been run, and the telemetry audit gating it is still the precondition.
