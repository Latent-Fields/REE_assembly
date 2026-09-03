# What would it take to *know*? (Richens & Everitt, ICLR 2024 oral) — EXT-005

**Source:** Richens J, Everitt T. *Robust Agents Learn Causal World Models*. ICLR 2024 (oral). arXiv:2402.10877.

## What the paper does

The paper settles a question that had been assumed rather than answered: must an agent learn a causal model in order to generalise, or would some other inductive bias do? The answer is a theorem. **Any agent capable of satisfying a regret bound under a large set of distributional shifts must have learned an approximate causal model of the data-generating process**, and for optimal agents that approximate model converges to the true one.

No experiments, no models tested. A proof.

## Why this entry is `mixed`, and why that is the honest label

It cuts both ways, and forcing it into a direction would misrepresent it.

**It weakens EXT-005** by closing off the inference the claim implicitly leans on. "It was trained on text, therefore it has no causal model" is not valid reasoning, and this theorem is why: causal-model possession is *entailed by behaviour*, not read off training provenance. If a system is robust under shift, it has one, whatever its training looked like and whatever anybody intended. The theorem also rejects the binary — "approximate" is graded, and intermediate systems hold partial causal structure — so a claim asserting *total* absence is asking for more than the formalism will supply.

**It strengthens EXT-005** by handing it the criterion it currently lacks. If causal models are diagnosable by robustness under distributional shift, then in-distribution benchmark accuracy is exactly the wrong instrument — which retrospectively explains the tension in the rest of this pull. Kıcıman's 97% is in-distribution and therefore, by this theorem's standard, uninformative about mechanism. Jin's finetuned models, which succeed in-distribution and collapse once variable names and phrasings are perturbed, are the theorem's negative case in textbook form: no robustness under shift, so by the contrapositive, no causal model. The two results stop contradicting each other the moment you apply the right test.

## What this is actually worth to REE

More than either of the other readings, and this is the most useful thing the pull produced.

EXT-005 is currently stated as a claim about the **absence of an internal mechanism**. That is the hardest kind of claim to evidence, the easiest to over-state, and the shape of claim that tends to sit at `candidate` indefinitely because nothing can move it. Richens and Everitt convert it into a claim about **generalisation under shift**, which is measurable.

And the same conversion applies to REE's own side of the ledger, which is where it earns its keep. If SD-029's comparator and ARC-037's routing constitute a genuine causal attribution mechanism rather than a correlational shortcut that happens to work in training, then an agent carrying them should **hold its attribution accuracy under shifts of the environment's causal structure that leave the surface statistics intact** — and an ablated arm without the comparator should not. That is a falsifier, it is stated in the paper's own currency, and it is a runnable V3 experiment rather than a philosophical position. Worth noting for whoever picks up the substrate side of this cluster.

The companion result from the same group is worth flagging alongside: *Discovering agents* (Kenton, Kumar, Farquhar, Richens, MacDermott & Everitt, *Artificial Intelligence* 322:103963, 2023) derives a causal discovery algorithm for identifying agents, and its Algorithm 1 takes **interventional distributions** as input — it cannot run on observational data. Two results from the same lab, pointing the same way: causal structure about agency requires interventions, and interventions are the one thing a corpus does not contain.

## Limitations

Three, and the first is substantial enough to cap the confidence.

The theorem is about an **agent facing a decision problem with a regret bound**. An LLM answering causal questions about vignettes is not straightforwardly that — it is not optimising regret over the environment it describes. Applying the theorem to LLMs requires a bridging argument the paper does not make, and this entry is where that bridge gets built rather than imported. It must not be cited as directly establishing anything about LLM internals.

Second, "approximate causal model" is graded. The result licenses claims about partial causal structure and declines the binary that EXT-005's phrasing assumes. It does not adjudicate the claim so much as tell the claim to be stated differently.

Third, the theorem is about causal models of *the world*. EXT-005's specific target is the agent-caused / world-caused distinction over the agent's **own** actions. An agent's own action is of course a variable in its causal model, but the paper does not single that variable out or treat self-attribution as a distinct competence — which, given SD-029, MECH-095 and ARC-037 all turn on precisely that distinction, is the gap the whole cluster sits in.

## Confidence

0.70. Source quality 0.92, the highest in the pull — an ICLR oral, a proved theorem rather than a benchmark, from a group whose companion result on agent discovery points the same way. Transfer risk 0.20, also the lowest: mathematics has no species step. Mapping fidelity 0.60 is what holds the aggregate at 0.70 despite that source quality, for the first limitation: the theorem's subject is regret-bounded agents and world models, and the route to EXT-005 runs through an argument this entry supplies itself.
