# Pessoa 2008 — On the relationship between emotion and cognition

**Claim grounded:** ARC-088 (emotion-as-anti-collapse architecture; affect as native, not bolt-on, control)
**Direction:** supports · **Confidence:** 0.60
**Source:** Pessoa L. *Nat Rev Neurosci* 9(2):148–58 (2008). According to PubMed; [DOI 10.1038/nrn2317](https://doi.org/10.1038/nrn2317).

## What the paper argues

Pessoa challenges the then-prevalent modular view of the brain as carved into "affective" regions (the amygdala as the emotion centre) and "cognitive" regions (lateral prefrontal cortex as the reasoning centre). He argues this segregation is untenable: complex cognitive-emotional behaviours arise from *dynamic coalitions of networks*, none of which is properly described as specifically affective or cognitive. Central to these interactions are high-connectivity **hubs** that regulate the flow and integration of information across regions. Emotion, on this view, is not a downstream evaluator bolted onto a cognitive core — it is woven into the same networks that produce behaviour.

## Why it grounds ARC-088

ARC-088's load-bearing architectural thesis is that emotion-like systems must be **native** control machinery — gates, biases, interrupts, salience shifts, persistence regulators, release conditions, credit-assignment signals — and that an *optimise-then-bolt-on-safety* design *fails* because these evaluators arrive too late if added afterward. The "603 lineage" worked example in the claim makes the same point empirically: the agent could form goals and feel threat but did not learn directed escape until the affective-learning bridge was made native to selection. Pessoa is the canonical neuroscience grounding for the "native, not bolt-on" half of ARC-088: the brain does not separate evaluation from computation into a wrapper-and-core; affect is integrated into the behaviour-producing networks. For a substrate_coherence architectural commitment, that is exactly the kind of conceptual anchor the biology-before-formal-definitions rule asks for.

## Limitations and the mapping caveat

Two honest boundaries. First, Pessoa grounds the *integration / native-control* thesis but **not** ARC-088's distinctive *functional* claim — that the collective effect of partially-independent affective evaluators is to prevent behaviour collapsing onto the currently dominant gradient (anti-collapse / structured behavioural diversity). That function is unevidenced by a general integration review and remains the genuinely-novel part of ARC-088. Second, there is a mild *tension*: Pessoa emphasises integration and shared hubs, whereas ARC-088's load-bearing rule is to *preserve distinct affective streams* (distinct learning targets and gating conditions, merging to one value scalar forbidden). These reconcile — ARC-088 explicitly allows distinct streams to share *interfaces/consumers* while keeping learning targets distinct — but Pessoa does not draw that distinction, so the paper supports the "native" axis more cleanly than the "partially-independent" axis.

## Confidence reasoning

Source quality is high (Nat Rev Neurosci, foundational). Mapping_fidelity is 0.60 — strong for the native-not-bolt-on thesis, weaker for the specific anti-collapse function. ARC-088 is an `architectural_commitment` with `epistemic_category: substrate_coherence`, so promotion/demotion is already suppressed and no experiment can confirm it; literature grounding is conceptual by nature and confidence is capped accordingly. Net 0.60. Literature confidence only; experimental confidence stays 0; ARC-088 status and gating are unchanged and nothing promotes.
