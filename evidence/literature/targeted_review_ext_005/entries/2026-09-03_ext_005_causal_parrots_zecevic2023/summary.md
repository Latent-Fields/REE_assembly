# Causal talk without a causal model (Zečević et al., TMLR 2023) — EXT-005

**Source:** Zečević M, Willig M, Dhami DS, Kersting K. *Causal Parrots: Large Language Models May Talk Causality But Are Not Causal*. Transactions on Machine Learning Research, 2023. arXiv:2308.13067.

## What the paper does

The paper asks a question that sounds rhetorical and is not: when a language model gives a correct causal answer, what computed it? The authors' answer is that nothing in the model did. They introduce a **meta SCM** — a structural causal model whose *variables are causal facts about other structural causal models*. Altitude causes temperature; that is a causal fact, and it is also a sentence that appears in text. A model trained to predict text therefore has access to the correlational shadow of an enormous number of causal conclusions, each of which was reached by some human running an experiment or an inference the model never ran. On this account, correct causal output is recitation from the meta SCM, and the label the authors choose — parrots — is doing precise work rather than being rude.

The empirical section is a supporting illustration rather than a decisive test. On common-sense causal chains posed as propositional logic, GPT-3 reaches 45%, Luminous 50%, OPT-30B 20%; on intuitive physics, 61.11%, 11.11% and 19.44% respectively. There is a causal-discovery evaluation against six ground-truth graphs (Altitude, Health, Driving, Recovery, Cancer, Earthquake) scored by SID/SHD/F1, and a k-NN probe of GPT-3 Ada embeddings against ConceptNet causal facts. The authors' own summary of it is that current LLMs are "even weak causal parrots."

## The finding that matters for EXT-005

EXT-005 asserts that language describes causation without any mechanism that computes a causal signature. That is a negative claim, and negative claims are cheap unless someone explains how the appearance survives the absence. This paper is the explanation. Causal facts are text; a text model gets the facts without ever forming the object that generated them.

The reason this matters for REE specifically is that REE's answer is a *quantity*, not a fact. SD-029's comparator computes `residual = z_harm_s_observed − E2_harm_s(z_harm_s_{t−1}, a_actual)`; the earlier SD-003 formulation computed `E2(z_t, a_actual) − E2(z_t, a_cf)`. Both are differences between what a forward model predicted under the action actually taken and what was observed or would have followed from an alternative. Two properties of that quantity are worth stating plainly against the meta-SCM picture. It is computed at run time from the agent's own efference copy, so it cannot be looked up. And it is indexed to *this* agent's action on *this* occasion, so it could never have appeared in anyone's training corpus — there is no sentence in the world reporting the counterfactual difference for an action REE has not yet taken. A meta SCM contains other people's causal conclusions. It cannot contain this.

## Limitations, and one that should not be smoothed over

Three, and the second is the one a governance reader should hold onto.

First, the meta-SCM account is a **conjecture**, and the authors say so in the abstract. This entry supports EXT-005's premise by supplying its best available explanation; it does not establish it. The accuracies above show weakness, and weakness is compatible with a bad causal model as much as with none at all.

Second, and this is the real boundary: the paper is about causal inference concerning **the world**, not about **self-attribution**. Whether a system knows that altitude causes temperature is a different question from whether it can distinguish a state change it produced from one it merely observed. EXT-005's actual content — false attribution and false denial of the agent's own causal responsibility — is not tested anywhere in this paper. The step from "no causal model of the world" to "no causal signature of own agency" is an inference made here on REE's behalf, and it is the weakest joint in the argument. It is plausible (a signature of own agency is a causal quantity, so a system with no causal machinery has no way to compute one) but it is not demonstrated, and the honest thing is to record it as a gap this pull could not close rather than as a conclusion it reached.

Third, the models tested are GPT-3, Luminous and OPT-30B, with some GPT-4 results. That generation is old relative to the systems EXT-005 is about, and Kıcıman et al. — also in this pull — report far stronger numbers on overlapping task types. The low accuracies should be read as the evidence available when the argument was framed, not as a current measurement.

## Confidence

0.74. Source quality 0.78 — TMLR review is real, the formal construction is careful, but the headline is a conjecture and the empirics are illustrative. Mapping fidelity 0.72 is the limiting term, for the second limitation above: the paper hits EXT-005's premise squarely and its self-attribution content not at all. Transfer risk 0.30, which is unusual for a paper with no species or lab-to-field step; the risk here is *generation* transfer, and it is a real one.
