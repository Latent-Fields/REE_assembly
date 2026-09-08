# Friston et al. (2012) -- Dopamine, affordance and active inference

**Claim tested:** MECH-002 (Precision control analogues shape cognitive regimes)
**Direction:** supports | **Confidence:** 0.72

## What the paper did

This is a simulation paper with an argument attached, and the argument is the important part. The
standard story about phasic dopamine is that it reports reward prediction error -- a scalar teaching
signal. Friston and colleagues propose something structurally different: that dopamine encodes the
*precision*, or salience, of the cues that engender action. Not how good an outcome was, but how much
to trust the representations that are currently proposing what to do. They build a hierarchical
generative model performing sequential movements under active inference, vary that precision term,
and show that a range of behavioural phenomena -- including Parkinsonian slowing -- fall out of a
single synaptic-level parameter.

No dopamine is measured anywhere in this paper. It is worth saying that plainly at the outset,
because it bounds what the entry can do for the claim.

## Findings relevant to MECH-002

MECH-002 makes two moves that this paper supports. The first is the specific assignment: the
dopamine-like regime "increases precision at action and policy depths" and "promotes temporal
collapse of a selected trajectory". Friston et al.'s "precision of cues that engender action" is
close to a restatement of that. High precision on action-relevant representations is exactly what
makes one affordance stop competing and start being executed -- which is what REE means by
trajectory locking. A trajectory that is merely one hypothesis among several has not collapsed; a
trajectory the system is committed to has.

The second move is more structural, and it is the one I think this paper actually carries. MECH-002
opens by insisting that "precision control does not merely tune learning rates" -- that it "induces
qualitatively distinct cognitive regimes". That is a strong claim and it needs external support,
because the obvious deflationary reading of any gain parameter is that it makes learning faster or
slower. What this paper demonstrates, within one model, is that varying a single precision parameter
moves the system between behavioural repertoires that a clinician would describe as different
*conditions* rather than different settings. That is the shape of evidence MECH-002 needs, even
though it is produced in silico.

## How this translates to REE, and where it strains

Two boundaries, and the second is the one that should be held in view.

The first is the ordinary simulation caveat. What is shown is that a precision account *can*
generate the phenomena, not that dopamine *does* implement precision. For an architectural claim
this is a weaker problem than it looks -- REE is not making a neuroscientific assertion about
mammalian dopamine, it is borrowing a control-theoretic shape -- but it does mean the entry cannot
be cited as evidence about the biology.

The second is sharper. The dopamine-as-precision reading is a minority position relative to
dopamine-as-reward-prediction-error, which has decades of direct electrophysiology behind it.
MECH-002 adopts the precision reading as a *premise*. That is a legitimate thing for a mechanism
hypothesis to do, but it means the claim is resting on a contested interpretation rather than
settled ground, and it should not be presented otherwise. If the RPE account turns out to be the
primary role, MECH-002's dopamine-like regime is mis-named -- the commitment function would still
need to exist in the architecture, but it would need a different biological analogue, and the
neuromodulatory framing would be doing less work than it appears to.

There is also a directional gap worth recording. The pathology this paper reproduces is bradykinesia
-- motor slowing under *reduced* action precision. MECH-002 asserts the opposite arm: over-commitment,
mania, compulsivity under *excessive* precision. Nothing here evidences that arm. The claim's
high-precision pathology is currently supported by clinical plausibility rather than by anything in
this directory.

## Confidence reasoning

Source quality 0.80 -- PLoS Computational Biology, heavily cited, an author list that is central to
this literature, but simulation-only. Mapping fidelity 0.85 -- the phrase "precision of cues that
engender action" maps onto MECH-002's dopamine regime about as directly as cross-framework mappings
get, and the one-parameter/many-regimes structure matches the claim's headline. Transfer risk 0.35,
notably higher than the Yu and Dayan entry, because the transfer is doubly indirect: simulation to
substrate, and a contested interpretation of dopamine to an architectural premise.

Aggregate 0.72. Solid support for the shape of MECH-002's dopamine regime; not support for the claim
that this is what dopamine is.
