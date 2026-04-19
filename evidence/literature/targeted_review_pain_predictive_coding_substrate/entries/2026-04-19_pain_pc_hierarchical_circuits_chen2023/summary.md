# Chen 2023 -- Hierarchical predictive coding in distributed pain circuits

**Citation.** Chen ZS. Hierarchical predictive coding in distributed pain circuits. Frontiers in Neural Circuits 2023; 17: 1073537. [DOI](https://doi.org/10.3389/fncir.2023.1073537). (According to PubMed.)

**What they did.** Theoretical review proposing an updated hierarchical predictive coding framework for pain perception. Draws on human and animal data showing that pain processing is distributed across cingulate and insular sub-regions with distinct functional roles.

**Key argument.** The cingulate-insula network is neither fully decentralised nor single-site. It is hierarchical: bottom-up nociceptive inputs meet top-down expectation signals at multiple levels, with active inference as the integration scheme. Traveling-wave oscillations are proposed as the coordinating mechanism between levels. Sub-regions of cingulate and insula contribute different functional signals but are bound into a coherent forecast by the network hierarchy.

**What this does for the REE question.** Gives the architectural precedent for our SD-032 cluster (already distributed, hub-and-network) and for treating E2_harm_a and E2_harm_s as two heads within a shared hierarchical predictor rather than two fully independent modules. The paper does not adjudicate the specific sharing question empirically, but the framework strongly favours the shared-trunk interpretation: if the whole pain network is computing under one hierarchical generative model, you do not have two independent forward models floating around unbound.

**Limitations.** Theoretical review; no new data. Heavily weighted toward active-inference formalism, which is a specific choice that not all authors in this literature endorse.

**Confidence reasoning.** Moderate. Useful for the synthesis because it explicitly states the hierarchical-distributed architecture that REE has already committed to. Not decisive because it is not empirical.
