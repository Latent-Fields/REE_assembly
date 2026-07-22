# Lee, Shimojo & O'Doherty 2014 — reliability-based arbitration between model-based and model-free control

**Claims:** MECH-477 (primary), MECH-163 (secondary)
**Direction:** supports · **confidence 0.82**

## What the paper did

Twenty-odd healthy adults performed a two-step Markov decision task while being scanned, with two manipulations crossed: how predictable the state transitions were, and how reliable the outcomes were. The authors fit a computational arbitrator to each subject's choices and then asked where in the brain its internal quantities were represented. The arbitrator maintains a reliability estimate for each of the two learning systems and converts the pair into a single probability, P(MB), that the model-based system holds control on this trial. Action selection is then a softmax over a value signal formed by weighting the two systems' values by that probability.

The critical result is that inferior lateral prefrontal cortex and frontopolar cortex encode *both* the reliability signals and the output of the comparison between them. That is a different and much stronger finding than "two systems exist" — it says there is a third thing, a comparator, with its own neural signature.

## Why this is the entry MECH-477 was missing

MECH-477 was registered on exactly this distinction: MECH-163 conflated architecture (two pathways exist) with dynamics (control shifts between them). Daw, Niv & Dayan 2005 — already on file at confidence 0.79 — supplies the normative argument that a rational agent *ought* to arbitrate by relative uncertainty. What it cannot supply is evidence that a brain actually instantiates a separable arbitration element rather than, say, letting the two pathways compete at the value stage by whoever shouts loudest. Lee 2014 is that evidence.

Three details bear directly on how SD-081 should be built, and each is a decision the normative account leaves open.

**What signal the arbitrator reads.** Not uncertainty in state-action value, which is what Daw 2005 proposed. Model-based reliability is computed here as a variance-to-mean ratio over the state prediction error — an inverse index of dispersion, essentially the probability that SPE is currently zero. Model-free reliability uses cruder machinery: a Pearce-Hall-style running average of the *unsigned* reward prediction error. These are not the same quantity, they are not computed by the same estimator, and the model that fits behaviour best is the asymmetric one. A REE arbitrator that computes both arms' confidence with one shared estimator is making a substantive departure, not a simplification.

**The timescale.** Trial-by-trial. The authors were explicit that they needed the state-transition probabilities to move fast enough for tonic shifts in P(MB) to be detectable at fMRI frequencies, which tells us the underlying quantity is faster still. This is the fast allocation mechanism, and it is the reason MECH-477 is properly distinct from ARC-071's slow repetition-driven transfer.

**Graded, not discrete.** Control "is not implemented in an all or nothing fashion." P(MB) is a continuous weight, governed by a two-state transition rule the authors borrow from biophysics, and it carries a bias term favouring the habit system on the grounds that habits cost less effort. That bias is not decoration — an unbiased arbitrator over-recruits the deliberative arm.

There is a fourth finding I find the most interesting and the most awkward. The arbitration appears to work by *suppression*: connectivity between the arbitrator regions and model-free valuation areas is negatively modulated by the degree of model-based control, and the authors looked for the reciprocal effect and did not find it. So this is not a symmetric competition in which two bidders are scaled against each other. It is a mechanism that reaches down and turns the habit pathway off when planning is going well, and otherwise leaves it running. If that is right, then the natural REE implementation is an attenuation gate on the habit pathway rather than a softmax mixture over two value streams — and those two designs will not behave identically under MECH-477's falsifier, because only the first predicts that the OFF arm's flat response is a habit pathway that was never attenuated.

## Limitations, honestly

The localisation is correlational. BOLD covariation with a model-derived regressor tells us the quantity is represented somewhere in that voxel's input; the psychophysiological interaction tells us coupling changes with P(MB). Neither is a causal test, and no lesion or stimulation data are offered. MECH-477's falsifier is a causal contrast — arbitrator OFF versus ON — so the paper motivates the build without underwriting the result.

The pathway identities also transfer imperfectly. The model-based system here is tree search over a two-step graph the subject has learned explicitly. REE's goal-directed pathway is hippocampal replay-based planning. The *arbitration logic* transfers well; the claim that REE's planner can compute an SPE-dispersion reliability signal at all is an assumption the build will have to discharge, and it is precisely what MECH-477's mandatory manipulation check should be watching — the arbitration weight must be shown to vary with measured uncertainty, or the run scores nothing.

I have set mapping fidelity at 0.78 rather than higher for that reason. The confidence of 0.82 reflects a strong empirical anchor for the existence and signal-type of an arbitrator, discounted for the correlational design and the pathway mismatch. Per standing discipline this is `lit_conf` only and is not blended with any experimental confidence; MECH-477's `exp_conf` remains unset, with V3-EXQ-786a standing as the measured OFF arm and no ON arm yet run.
