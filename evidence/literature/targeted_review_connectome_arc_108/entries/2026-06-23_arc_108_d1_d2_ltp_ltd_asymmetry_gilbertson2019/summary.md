# Maladaptive striatal plasticity and abnormal reward-learning in cervical dystonia

According to PubMed. Source: Gilbertson, Humphries & Steele (2019), *European Journal of Neuroscience* 50(7):3191-3204. [DOI](https://doi.org/10.1111/ejn.14414)

## What the paper did

Forty patients with cervical dystonia and forty matched controls performed a reward-gain and loss-avoidance reversal-learning task. The authors then fitted each participant's behaviour to a computational model of the basal ganglia that builds in *receptor-specific* corticostriatal learning rules -- separate long-term-potentiation and long-term-depression terms for the D1 (direct-pathway) and D2 (indirect-pathway) populations. They ran a model comparison across four hypothesised abnormalities (increased or decreased D1:LTP/LTD, increased or decreased D2:LTP/LTD) to see which best reproduced the patients' behaviour. The answer: a model with *decreased D2:LTP/LTD* -- excessive D2 corticostriatal depotentiation -- best explained the data. Patients were selectively impaired in the post-reversal phase, and, strikingly, individual reward-reversal learning rates correlated with the severity of the patient's motor symptoms.

## Why it speaks to ARC-108

ARC-108 does not just propose that the gating weights be learned by a dopaminergic teaching signal; it specifically commits to the D1-LTP / D2-LTD asymmetry as part of the rule. This paper is empirical evidence that those two receptor branches are real, separable, individually parameterisable, and behaviourally consequential. The model could only fit the patients by letting D1 and D2 LTP/LTD vary independently -- a single symmetric learning rule would have had no way to localise the deficit to the D2 depotentiation branch. That is exactly the degree of freedom ARC-108 wants to install in the E3 selector's gating layer, and the design choice is vindicated here by the fact that it carries diagnostic information.

Just as important for our purposes is the second half of ARC-108's requirement: every architectural commitment under ARC-106 must name a psychiatric failure mode, and breakage must map to a disorder. This paper delivers a worked instance of that logic from the other direction -- it takes a clinical population, derives the receptor-specific plasticity abnormality that explains their behaviour, and shows the learning-rate parameter tracks symptom severity. The grammar is precisely the one ARC-108 adopts: derange a specific branch of the D1/D2 LTP-LTD rule and a graded behavioural pathology follows.

## The caveat I want on the record

The syndrome here is cervical dystonia, a movement disorder, not any of the dopaminergic-RPE psychopathologies ARC-108 names (addiction, the aberrant-salience positive symptoms of schizophrenia, anhedonic blunted-RPE depression, the impulse-control/dyskinesia spectrum). So the mechanistic mapping is strong -- separable D1/D2 LTP-LTD branches whose asymmetry is load-bearing -- but the syndrome-level mapping to ARC-108's specific failure-mode list is by analogy of mechanism, not by matching the disorder. I would not cite this as evidence about addiction or schizophrenia; I cite it as evidence that the *form* of rule ARC-108 commits to is one that real striatal plasticity instantiates and whose imbalance is clinically real.

## Confidence

I put this at 0.70. Human behaviour fitted to a mechanistically explicit model is good empirical grounding (source quality 0.78), and the mapping onto ARC-108's D1/D2 asymmetry is faithful (0.72). I hold it back with an elevated transfer risk (0.40) because the off-target syndrome means the psychiatric-failure-mode support is suggestive rather than direct.
