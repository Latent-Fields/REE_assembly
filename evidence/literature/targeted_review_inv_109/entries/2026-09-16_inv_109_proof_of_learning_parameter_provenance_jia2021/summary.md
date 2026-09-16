# Proof-of-Learning: Definitions and Practice (Jia, Yaghini, Choquette-Choo, Dullerud, Thudi, Chandrasekaran & Papernot, IEEE S&P 2021)

## What the paper did

This is a security paper, and it begins from what is, almost word for word, INV-109's premise: "once the model's final parameters are released, there is currently no mechanism for the entity which trained the model to prove that these parameters were indeed the result of this optimization procedure." The authors want a *proof of learning* -- a certificate that a given set of weights is the product of a given training run, defensible against an adversary who would rather manufacture the certificate than do the work.

The obvious design is to let the verifier re-run the recipe and check whether it arrives at the claimed weights. The paper's central engineering finding is that this does not work, and the sentence in which they say so is the reason this entry exists: "reproducing weights trained step by step leads to a negligible reproduction error. However, attempting to reproduce an entire sequence leads to a large error due to the linear increase in entropy over the T steps" -- and crucially, this happens "even when using the exact same batching strategy, architecture, initial parameters, and training setup, due to the irreproducible noise arising from the hardware and low-level libraries."

So the protocol they actually build persists state. The prover "reveals to the verifier some of the intermediate weights achieved during training as its PoL", releasing "the values of the weights (or model updates) at periodic intervals". The verifier then loads a recorded checkpoint into its own model, performs k updates to reach `W'_{t+k}`, and compares against the claimed `W_{t+k}`, tolerating `d2(W'_{t+k}, W_{t+k}) <= delta` -- where delta "should be calibrated before verification starts, as it depends on hardware, model architecture, dataset, checkpointing interval, and the learning hyperparameters."

## How this bears on INV-109

INV-109 says: any claim naming a specific earlier endpoint requires that endpoint's weights and observations to have been **persisted and loaded, not re-derived**. Jia et al. arrived at that requirement independently, under adversarial pressure, and with a budget to do otherwise if anything else had worked. That is the value of this entry. The other papers in this pull establish that reproductions diverge; this one establishes that a serious attempt to *certify artifact identity from a recipe* concluded it was not possible and built persistence machinery instead.

Their reproduction-error structure also supplies the quantitative shape the REE case was missing. Error over one step is negligible; error over a trajectory grows with its length. That is why the 1010 lineage's re-run of 60 P0a + 200 P0 + 90 P1 episodes cannot be expected to land on 1008's weights however faithfully the recipe is followed -- and why "we pinned the substrate commit" does not help, since the pin does not shorten the trajectory or remove the low-level library noise the entropy accumulates from. Their slack parameter, explicitly hardware-dependent, is the same machine-class sensitivity the 1008-against-1010 pair exhibits (`linux-x86_64-py3.10-torch2.12.0+cpu` at substrate hash `875d3044` against `darwin-arm64-py3.13-torch2.12.0` at `1fdd6171`).

## Where it does not support INV-109, and this matters

INV-109 prescribes a discriminator that is "mechanical and cheap: a recorded state hash at both endpoints, re-verified at every evaluation boundary, with a mismatch aborting rather than warning." Jia et al. do not do that. They tolerate a calibrated distance, and they are explicit that the tolerance must be calibrated per hardware and per architecture -- which is to say, they considered an exact-equality check and did not adopt it. So this paper ratifies INV-109's **diagnosis** almost literally while adopting a strictly weaker **remedy**. An entry citing it as external support for hash-and-abort would be over-reading it, and I have recorded that as a failure signature rather than quietly absorbing it into the confidence score.

There is a defence available to INV-109 here, and it should be stated as a defence rather than smuggled in as a finding. PoL must verify a *trajectory* against a recomputation, which unavoidably involves recomputed floats and therefore a tolerance. INV-109's REE application needs only to compare *stored* endpoint hashes against each other -- no recomputation, so no tolerance needed. The two designs differ because the tasks differ, not because one is stricter about the same thing. But that argument is mine, not the paper's, and governance should treat it that way.

## Limitations and provenance notes

Setting is adversarial security on supervised vision benchmarks, not scientific measurement of a learned representation; the threat model is a lying prover, whereas INV-109's failure mode is an honest session inheriting an unmeasured sentence. The technical fact is the same, but the appropriate tolerance may not be.

Metadata: the IEEE DOI for the proceedings version was not resolved during this pull, so the `doi` key is omitted rather than set to `null` (which in this corpus would assert "checked, none exists"). The arXiv identifier `2103.05633` and the proceedings pages 1039-1056 are recorded and are sufficient to locate the paper. Quotations above are from the arXiv HTML v1; the PDF did not render to extractable text via the fetch path used.

## Confidence

0.86, the highest in this pull, on mapping fidelity rather than venue alone. The paper's design constraint *is* the claim, which is a rarer and stronger form of corroboration than a result that merely happens to be consistent with it. The discount is the remedy gap (slack parameter versus exact hash) and the adversarial-versus-scientific setting.
