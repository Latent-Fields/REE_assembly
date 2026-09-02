# Kane et al. (2022) -- Rat anterior cingulate cortex continuously signals decision variables in a patch foraging task

*Entry for ARC-073: play-to-real transition is triggered by competence saturation or drive pressure, not by scheduled duration.*

## What the paper did

Rats performed a patch-foraging task while ACC was recorded. The authors built a leaky-accumulator model grounded in the marginal value theorem, generating estimates of the decision variables within and across trials, and tested the model's predictions against the recorded activity. Model-predicted dynamics matched ACC activity closely. They then went further than the correlational study allows: they pharmacologically inactivated ACC and asked what happened to the decision.

Two findings, pulling in different directions. First, the rats followed MVT -- they left a patch when its reward rate depleted toward the average rate across patches -- replicating the behavioural rule in a second species and confirming that the depletion-threshold decision is not a primate curiosity. Second, ACC inactivation profoundly changed foraging decisions and response times, and yet the rats *still followed the MVT decision rule*. The authors conclude that ACC encodes foraging-related variables for reasons unrelated to patch-leaving decisions.

## Why this matters for ARC-073, in both directions

The supporting half is straightforward and worth stating plainly: the "leave when the marginal rate of return decays to threshold" rule is robust, species-general, and survives a strong causal perturbation of the region that appeared to compute it. If REE builds play-episode close on a saturation test rather than a duration, it is building on a rule that biology keeps re-implementing. That is real support for ARC-073's positive clause.

The weakening half is more interesting and, I think, more useful. ARC-073's implementation note says: monitor a rolling LP estimate during play; close the episode when LP drops below `play_lp_saturation_threshold`. That is a single-signal, single-locus story. This paper is a worked example of exactly that story failing in a system where it looked overwhelmingly true. The accumulator model fit the ACC signal beautifully. Remove the ACC and the behaviour changes -- but the *rule* does not. The signal that best tracked the decision variable was not the thing making the decision.

I want to be careful about what this does and does not do to the claim. ARC-073 makes no anatomical commitment; it is a claim about a criterion, not about where the criterion lives. So this is not a contradiction. What it is, is a warning about validation. If REE instruments play-mode exit by watching one LP estimator and then runs a diagnostic that perturbs that estimator, it may find behaviour largely unchanged and conclude the criterion is wrong, when what it has actually discovered is that its estimator is a correlate. The inference "this variable tracks the transition, therefore this variable triggers the transition" is the one this paper breaks, and it is the inference an REE experiment on ARC-073 is most likely to make by default.

## Limitations

Rodent foraging to synthetic-goal play is a long transfer, and the same exogenous-versus-endogenous depletion problem noted in the Hayden entry applies here unchanged. The inactivation is pharmacological and therefore coarse -- it is not evidence that no cortical region computes the decision, only that this one, at this grain, is not necessary for the rule. And the causal half of the result speaks to methodology rather than to ARC-073's content, which is why I have recorded the entry as `mixed` rather than `weakens`: the behavioural half genuinely supports the claim's positive clause.

## Confidence

0.58. The design is strong -- model, recording, and causal manipulation in one paper -- and the venue is solid. The number is depressed because the entry is doing double duty across two clauses of the claim and neither half maps cleanly onto play. It is here mostly to stop the Hayden entry from being read as more settled than it is.
