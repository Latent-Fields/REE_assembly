# How Language Model Hallucinations Can Snowball (Zhang, Press, Merrill, Liu & Smith, 2023)

**Claim tested:** EXT-002 -- *Hallucination: no persistent error residue accumulates to shape future outputs.*
**Direction:** supports | **Confidence:** 0.78

## What the paper does

The authors construct three question-answering datasets -- primality judgements, US senator search, and graph connectivity -- chosen so that ChatGPT and GPT-4 frequently give a wrong answer and then, when asked to justify it, produce an explanation containing at least one further false claim. The design's pivot is what happens next: they take those downstream false claims out of the conversation and present them to the same model in isolation. ChatGPT identifies 67% of its own mistakes this way; GPT-4 identifies 87%. The authors name the pattern *hallucination snowballing*: an early error is over-committed to, and generates further errors the model would not otherwise have made.

## Why this is the strongest entry in the EXT-002 set

Most evidence for EXT-002 is evidence of an absence, and absence arguments are weak when a simpler explanation is available. Here the simpler explanation is explicitly killed. If the model produced the downstream falsehoods because it did not know better, the out-of-context detection rate should be near chance. It is 67% and 87%. So the information required to penalise the earlier commitment is present inside the model at the moment it is doing the opposite. What is missing is not knowledge; it is any pathway by which a committed error becomes a standing cost on the continuation.

That is precisely the shape EXT-002 asserts. And it is worth noting that the paper shows something slightly stronger than the claim's wording. EXT-002 says errors leave no trace that *penalises* future outputs. Snowballing shows that the trace exists and has the wrong sign: the earlier error does shape what comes next, as context to be made consistent with, so it is amplified rather than damped. A transformer conditions on its own prior tokens as evidence; it has no channel that marks them as *costly*. In the REE contrast the claim draws, phi(z) accumulates E1 prediction error and pushes trajectory selection away from the region that produced it (ARC-005, INV-006, INV-008) -- a negative-feedback term. Autoregressive self-conditioning is the positive-feedback term with the same input.

## Limitations

Two boundaries I want stated plainly. First, everything here happens inside a single context window. The paper establishes that no error-penalising signal operates over the generation horizon; it does not measure anything about persistence across episodes. The cross-episode reading of EXT-002 is *trivially* true for a stateless API model, and this paper is not what evidences it -- it evidences the more interesting within-trajectory version. A governance reader should not let this entry stand in for cross-episode evidence.

Second, ChatGPT and GPT-4 as accessed in 2023 are deployed products with undisclosed post-training, and possibly retrieval or safety scaffolding in the path. The result characterises those systems, not a bare transformer decoder. It happens that both readings serve EXT-002 -- if anything the deployed-system version is the more relevant one, since the claim is about what LLMs actually do -- but the inference is to the product, not to the architecture, and the architectural attribution in EXT-002's notes rests on the mechanism argument rather than on this measurement.

I also could not verify a refereed venue for this paper via arXiv, OpenAlex, Crossref or DBLP on 2026-09-03, so it is recorded as a preprint and `source_quality` discounted accordingly. The datasets are small and purpose-built, which is appropriate for a dissociation but limits the generality of the rates themselves.

## Confidence reasoning

`mapping_fidelity` at 0.88 is the highest in this pull, because the experiment isolates the exact variable the claim is about and controls for the main confound. `transfer_risk` is 0.20 -- same domain, same artefact class, no species or task transfer to discount. `source_quality` at 0.75 carries the preprint status and the small constructed datasets. The aggregate of 0.78 weights mapping fidelity heavily, which is the right emphasis for a claim about architecture; I stopped short of 0.8 because the within-window scope is a real restriction on what the entry can be cited for.
