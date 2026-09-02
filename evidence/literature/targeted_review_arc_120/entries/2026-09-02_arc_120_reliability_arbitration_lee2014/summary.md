# Neural computations underlying arbitration between model-based and model-free learning

Lee, Shimojo & O'Doherty (2014), *Neuron* 81(3):687-699. PMID 24507199, PMC3968946. doi:10.1016/j.neuron.2013.11.028.

## What the paper did

Daw et al. (2005, also in this directory) proposed that behavioural control is allocated between the model-based and model-free systems by their relative uncertainty. Lee and colleagues went looking for the arbitrator itself. Healthy adults performed a two-stage Markov decision task in which state-transition uncertainty and reward stochasticity were manipulated so that the two learning systems' predictions would be differentially reliable at different points in the session. They fitted a computational arbitration model that carries an explicit per-system reliability estimate, and regressed those signals against BOLD.

Three findings matter here. First, inferior lateral prefrontal cortex and frontopolar cortex encode the reliability signals of both systems. Second, the same regions encode the *output of a comparison* between those reliabilities -- not just how good each system is, but which is currently better. Third, and this is the finding I keep coming back to, functional connectivity from these regions to model-free valuation areas is *negatively* modulated by the degree of model-based control. The arbitrator appears to act by turning the losing system's valuation signal down.

## Why this bears on ARC-120

ARC-120 says authority is earned through demonstrated competence and never granted merely because a computation exists. Lee et al. supply the missing mechanistic middle for that assertion. It is one thing to say, normatively, that authority should track accuracy; it is another to find that the brain maintains an explicit reliability variable per module, an explicit comparison between them, and a pathway by which the comparison suppresses the loser.

That third element is the part I would not have predicted from the claim as written, and it sharpens ARC-120 rather than merely confirming it. The naive reading of "authority is earned" is permissive: the competent module gets to act, the incompetent one just does not. What Lee et al. see is stricter and more interesting -- the incompetent module is *actively withheld*. Its computation continues; its influence on valuation is attenuated. That is a design distinction with teeth for REE. A gate implemented purely as an enabling condition on the competent path (MECH-094-style tagging that only the writer consults) is a weaker architecture than one that also attenuates the untrusted path's contribution to valuation. Worth carrying into whatever the next ARC-120 instance turns out to be.

## Limits of the mapping

The authority at stake is action selection, over trials, in a value-learning task. ARC-120 also covers write authority -- what enters memory, what gets committed -- and this paper says nothing about that. "Reliability" here is a running estimate of prediction-error variance, which is a momentary competence, not the accrued developmental competence ARC-120's existence -> representation -> competence -> authority sequence describes; the same gap noted in the Daw entry applies.

Two more caveats worth stating plainly. The connectivity finding is a psychophysiological-interaction-style result: it establishes that frontopolar-to-valuation coupling covaries with arbitration state, not that the frontopolar signal *causes* the suppression. And as with every entry in this directory, no external paper can address ARC-120's second half -- whether REE's four existing gates are instances of one principle or four unrelated gates. That is an internal architectural question. Literature can only make the general principle credible.

## Confidence

0.78, the highest in this pull. Source quality 0.80 (Neuron, well-powered design, model comparison done properly, but fMRI is indirect and the key connectivity result is correlational). Mapping fidelity 0.78 -- higher than Daw 2005 because the explicit reliability representation and the active-suppression finding are precisely the two features ARC-120 needs, and because they are measured rather than posited. Transfer risk 0.32: human decision-making to a computational substrate, with the additional caveat that a BOLD-level modulation may not have a clean algorithmic counterpart.
