# Voigt et al. 2018 - Hard Decisions Shape the Neural Coding of Preferences

[DOI](https://doi.org/10.1523/JNEUROSCI.1681-18.2018) | PMID 30530856 | J Neurosci, 2018 | According to PubMed.

## What the paper did

Voigt and colleagues ran an fMRI study with concurrent eye-tracking on healthy adults, using a paradigm in which participants made hard binary choices between equally valued food items. The headline question was when and where in the brain preference changes are computed — at the moment of decision, or only afterward through dissonance reduction. The headline answer is: online, during the decision itself, predicted by activity in left dorsolateral prefrontal cortex and precuneus, with eye-fixation patterns also predicting the magnitude of upcoming value change.

The architecturally-relevant finding is the second one. Voigt's group probed memory for the choices in a follow-up phase. They found that the preference adjustments became behaviourally relevant — that is, actually showed up in subsequent valuation — only for choices that were remembered. And the act of remembering was associated with hippocampus activity.

Phrased as a dissociation: same hard choice, same dlPFC engagement, same evidence of online preference update during the decision — but no behavioural consequence in the next valuation phase unless the hippocampus retained the record of having made that particular choice. If the choice was forgotten, the lock did not engage.

## Why this matters for the commit-boundary belief lock proposal

This is the strongest empirical match in the pull for the architectural prediction the brief makes. The proposed commit-boundary belief lock mechanism rests on the claim that revision cost depends on the durable record of the commit — if the agent's hippocampal-mediated record of having committed is intact, the belief is locked; if the record is degraded or lost, the lock dissolves and the belief reverts to standard revisability.

Voigt's design isolates exactly that dependency. The decision happens. The dlPFC computes a value update. The agent leaves the scanner. Hours or days later, the preference change is detectable only for choices the hippocampus retained. The hippocampus is doing exactly the work the brief assigns to the commit-record substrate (INV-021 territory).

This is also the cleanest available reply to a possible alternative: that the dissonance / preference-change effect is purely an online artefact of the decision-making process and does not actually leave a durable trace. Voigt's data refute this: the trace IS durable, conditional on memory of the commit. Without the commit record, the trace evaporates. With it, the trace persists into the subsequent valuation. That conditional dependency is the architectural signature.

The proposed two-mechanism framing in the brief (commit-boundary belief lock + attribution-rigidity setpoint) maps neatly onto Voigt's results. The dlPFC is doing the value-update / conflict-resolution work that engages at commit (the commit-boundary mechanism); the hippocampus is doing the record-keeping that determines whether the update propagates to durable belief (the attribution-rigidity setpoint, in its biological substrate). Set the hippocampal record-keeping high and the mechanism produces lock; set it low and the mechanism dissolves.

## Limits and caveats

The paradigm tests preference change over food items, not propositional belief revision under counter-evidence. The "remembered vs not" contrast is between low-stakes forgetting and low-stakes recall, not between high-stakes acted-upon beliefs and high-stakes unacted-upon beliefs. The transfer to clinical delusion-resistance scenarios is one inferential step — plausible if the underlying machinery generalises, but not directly demonstrated.

A subtler issue: the paper does not explicitly frame its result as testing the dependence of belief lock on commit-record retention. The authors interpret the result as showing that preferences are dynamic, with adjustment dependent on memory of having made the choice. The architectural framing the brief imposes (memory of the commit IS the substrate of the lock) is a re-reading of their data, defensible but not what they say.

## Confidence reasoning

Confidence at 0.88 — the highest of any entry in the pull. Source quality is high (J Neurosci; fMRI + eye-tracking + behaviour + memory probe is a well-designed combination). Mapping fidelity is unusually high because the experimental dissociation Voigt isolates IS the architectural prediction the brief makes — the conditional dependence of downstream representational shift on commit-record retention. Transfer risk is moderate because the paradigm is low-stakes consumer preferences rather than high-stakes propositional beliefs, but the underlying value-update + record-keeping circuitry is plausibly the same.

This entry, together with Tandetnik 2021 (frontal lesion patients fail to show the effect even with intact memory), forms the Stream 5 pair. Voigt isolates the necessity of the hippocampal commit-record substrate; Tandetnik isolates the necessity of the frontal-lobe executive substrate. Both substrate conditions are required for the proposed mechanism to operate.
