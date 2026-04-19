# Craig 2009 — How do you feel—now? The anterior insula and human awareness

**Source:** *Nature Reviews Neuroscience*, [10.1038/nrn2555](https://doi.org/10.1038/nrn2555). Via PubMed (PMID 19096369).

## What the paper does

Craig synthesises his long-running research programme on interoception into an account of the anterior insula (AIC) as the brain's hub for integrating bodily-state signals with emotional and cognitive content. The paper argues AIC constructs a unified "global emotional moment" by pooling visceral, autonomic, nociceptive, proprioceptive, and affective streams, and that this integration is a prerequisite for subjective feeling and for the kind of urgency that drives rapid behavioural change.

## Key findings relevant to the claim

- **AIC receives interoceptive input via the lamina-I / spinothalamic / VMpo pathway.** This is anatomically separate from the lateral-thalamic sensory-discriminative route. AIC is downstream of affective-motivational pain (z_harm_a's real substrate target), not sensory-discriminative pain.
- **AIC integrates interoception with emotional and cognitive signals.** It is *not* just an affective-pain module; it is the node where affective pain meets everything else that constitutes current bodily state.
- **AIC has direct efferents to autonomic control regions** (brainstem nuclei, hypothalamus) and to motor/premotor cortex. This is the structural basis for urgency-interrupt: AIC can directly drive state change in autonomic and motor systems when salient interoceptive events demand it.
- **AIC-ACC salience network.** Craig (with Menon/Uddin providing the fuller network account) describes AIC and dACC as co-active during salient events of all modalities -- pain, surprise, error, uncertainty. This salience network *switches* between large-scale brain networks (DMN vs task-positive) when the global state demands reallocation of attention and control.

## How this maps onto REE (the translation)

This paper is the direct biological basis for **Option C** in the z_harm_a consumer question, and it clarifies why Option C is not the same computation as Options A or B. The AIC's role is urgency-interrupt: when affective pain (or any salient interoceptive event) exceeds threshold, the AIC triggers network-state switching -- it does not incrementally add cost to ongoing action evaluation.

Key architectural implications for the new cingulate substrate:
1. The urgency-interrupt path should be gated on interoceptive *baseline*, not affective-pain magnitude alone. The same z_harm_a should trigger interrupt for a depleted agent and be absorbed for a well-resourced one. This means ree-v3 needs an interoceptive state vector (drive_level, fatigue, metabolic estimate) that modulates the AIC-analog's threshold. SD-012 (homeostatic drive) is the corresponding substrate and is already on the queue.
2. The interrupt should **phase-reset E3** (this is exactly MECH-091), not just modulate commit threshold. ree-v3's current `urgency_weight` stub is too weak -- it nudges threshold but does not force state reset. Connecting z_harm_a into MECH-091's trigger conditions is the cleanest wiring.
3. The interrupt should **trigger network switching**, not just module-internal changes. In ree-v3 terms, a salient affective-pain event should suspend trajectory evaluation and kick the agent into a replay / orientation mode (adjacent to MECH-092 micro-quiescence replay). This is a coupling that doesn't yet exist.

Critically, Craig's framing shows Option C is *not* the z_harm_a consumer in the action-selection sense -- it is a parallel consumer that operates on the commitment/attention control surface rather than the action-value surface. ree-v3 needs both the ACC-analog (action-value consumer, Options A/B) and the AIC-analog (urgency-interrupt consumer, Option C), with interoceptive gating binding them.

## Limitations and caveats

Craig's framework is strongly phenomenological -- "global emotional moment" and "material me" are consciousness constructs, and the paper sometimes treats AIC as causally responsible for awareness itself. For the substrate work, we should extract only the mechanistic claims (AIC-as-hub, direct autonomic efferents, salience-network structure) and leave the phenomenology aside. We are not trying to give ree-v3 subjective feelings; we are trying to give it a working urgency-interrupt pathway.

Craig also treats AIC as hierarchically above ACC. Later work (Menon & Uddin 2010) reframes them as peer nodes in a salience network, which is the more useful framing for ree-v3. I'm rating this paper on the mechanistic content and setting aside the hierarchical claim.

Transfer risk: the clinical/phenomenological framing of "feeling" does not translate directly to an embodied agent's control architecture. The mechanism (interoceptive + affective integration -> autonomic/motor interrupt) translates cleanly; the phenomenology does not and should not.

## Confidence reasoning

0.80. Source quality is high (canonical AIC review, widely cited). Mapping fidelity is strong for the urgency-interrupt role and for the interoceptive-gating requirement, weaker for action-selection details (which belong to ACC/aMCC work). Transfer risk is moderate -- the mechanistic claims translate cleanly but the phenomenological framing does not, and some specifics (AIC-ACC hierarchy) have been superseded.
