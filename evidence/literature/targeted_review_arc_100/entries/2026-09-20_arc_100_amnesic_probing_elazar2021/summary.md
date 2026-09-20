# Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals (Elazar, Ravfogel, Jacovi & Goldberg, TACL 2021)

## What the paper did

By 2020 the probing literature had become large and slightly complacent. The standard move was: train a small classifier to predict some linguistic property -- part of speech, dependency label, named-entity type -- from a frozen neural representation; if the classifier does well, conclude that the model "encodes" that property; imply, usually without saying so, that the model therefore uses it.

Elazar and colleagues break the implication. Their argument is that probing results cannot license behavioural conclusions at all, because decodability and use are simply different things. They then do the constructive work: *Amnesic Probing* assesses a property's importance by removing it from the representation -- by iterative nullspace projection -- and measuring what happens to the model's actual behaviour downstream. Not "can I find part-of-speech in BERT?" but "if I take part-of-speech out, does BERT's masked-language-modelling behaviour change?"

The headline empirical finding is the one that matters: conventional probing performance is *not correlated* with task importance. Properties that probe well can be causally inert. The paper ends with an explicit call for increased scrutiny of claims drawing behavioural or causal conclusions from probing results.

## Why this is the load-bearing entry for ARC-100

ARC-100 has two kinds of content. There is the prohibition -- no imported transformer block, no LLM as authority -- which is architectural, and which a project either violates or does not. And there is the *grounding criterion*: a mined cut counts as grounded only if it changes perception, attention, action, memory, rule-availability or coordination. The criterion is the part that ordinary work can violate quietly, week by week, without anyone noticing.

GRAM-2 makes this concrete and makes the risk visible. The grammar-to-substrate mapping table has a column headed *grounded-or-merely-named*. That column is the honesty mechanism of the entire mining method, and it is exactly the column that is easy to fill in wrongly under mild pressure -- because the cheapest available evidence for "grounded" is a decodability result, and a decodability result is available for almost anything.

Elazar et al. show that this cheap evidence is invalid, and they show it empirically rather than by argument. Then they supply the method the criterion actually needs: ablate, and measure the behavioural consequence. Note the shape of ARC-100's criterion -- it is a *disjunctive list of behavioural consequences* (perception, attention, action, memory, rule-availability, coordination). That is not merely compatible with the amnesic-probing protocol; it is the same idea in a different vocabulary. Whoever wrote the criterion was reaching for this method without naming it.

The practical upshot is that "grounded-or-merely-named" stops being a judgement call and becomes a measurement with a published protocol. A GRAM-2 row is grounded if removing the candidate primitive from the relevant substrate changes at least one of the six named behaviours, and not otherwise.

Worth recording that the error runs both ways. The paper's converse point is that a property can be causally important while being hard to decode -- so a *low* probe score is not evidence that a mined cut is absent. A mapping table scored by probes alone will make errors in both directions, which is worse than making them in one.

## Limitations, including one the paper itself inherits

The substrate is a pretrained transformer and the properties are linguistic annotations. REE's substrate is a different object, and -- this is the more important mismatch -- the cuts GRAM-2 contemplates are not properties one decodes from a frozen representation. Noun-to-object-token, verb-to-action-affordance, aspect-to-event-closure: these are architectural commitments about what a module computes, not latent variables waiting to be probed. So what transfers here is methodological, not empirical. ARC-100 inherits the *discipline* -- require a causal intervention, distrust decodability -- and none of the specific results.

And the method has its own ceiling, which I would rather state than let a future reader discover. Removal is by linear projection, and subsequent work has established that this neither guarantees the target property has been fully removed nor guarantees that nothing else was removed alongside it. So an ablation verdict is bounded. A GRAM-2 row scored this way is honestly described as "grounded, to the precision of the ablation" rather than simply grounded -- which is a weaker statement than the table's binary column currently permits, and possibly an argument for a third value in that column.

## Confidence

0.82, `supports` -- the highest in this pull, and the only entry where source quality (0.85) and mapping fidelity (0.84) are both above 0.80. TACL, released code, widely adopted, and the method has been *refined* by later work rather than overturned, which is the right kind of afterlife for a methodological paper. Mapping fidelity is high because ARC-100's grounding criterion and this paper's central thesis are the same proposition stated twice. Transfer risk 0.30 reflects honestly that what crosses over is a method and a caution rather than a finding.
