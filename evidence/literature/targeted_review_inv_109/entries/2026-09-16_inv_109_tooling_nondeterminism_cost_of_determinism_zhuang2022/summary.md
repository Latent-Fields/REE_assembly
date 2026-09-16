# Randomness in Neural Network Training: Characterizing the Impact of Tooling (Zhuang, Zhang, Song & Hooker, MLSys 2022)

## What the paper did

Where Summers and Dinneen isolate randomness *inside* the training procedure, Zhuang et al. look underneath it, at the tooling: the accelerator architecture, the kernel library, the reduction order, the framework's choice of algorithm for a given convolution. They run a large-scale characterisation across several GPU accelerator architectures, a range of standard networks, and open datasets, asking two questions in tandem -- how much does each tooling-level source of nondeterminism actually move the trained model, and what does it cost to turn that source off?

The cost answer is the one that gets quoted: enforcing deterministic implementations carries overhead of up to 746 percent on widely used GPU accelerators, and the penalty varies dramatically between network architectures and hardware types. The scientific answer is subtler and, for our purposes, more useful. The impact of nondeterminism is *nuanced*: top-line metrics such as top-1 accuracy are not noticeably impacted, while model performance on certain parts of the data distribution is far more sensitive to the introduction of randomness. Aggregate agreement, disaggregate disagreement.

## How this bears on INV-109 -- both ways

This entry is filed `mixed`, and the mixture is the point.

On the supporting side, it identifies the layer INV-109 is gesturing at when it says a pinned substrate *commit* is not a substitute. A commit pin fixes the source. The nondeterminism Zhuang et al. characterise lives below the source -- in which kernel the library selects, in what order a reduction accumulates, in what the accelerator does with a fused multiply-add. None of that is visible to the pin, which is why REE can report a fully pinned run with `substrate_stable_across_run: false` and have that be consistent rather than contradictory.

The subgroup finding is a closer structural match still. INV-109's whole shape is *the regime-level readouts agree and the artifact is not the same*: the consumer-width values fall in the declared band, the participation ratios match 1008, and the weight deltas differ anyway. Zhuang et al. observed that same shape independently, in a different domain, at scale -- top-1 holds while slices move. That is worth more than a paper simply asserting that nondeterminism exists, because it is evidence about the *diagnostic value of aggregate agreement*, which is exactly what the 1010 audit was tempted to over-read.

On the countervailing side: they also show that determinism is attainable. Not cheaply, not portably, but attainable -- within a fixed hardware and software stack, deterministic kernels give you reproducible training. INV-109 states its own falsifier as "recipe reproduction under a pinned substrate commit yields BIT-IDENTICAL endpoint weights across machine classes and repeated runs". On this paper's evidence, the *repeated runs, same stack* half of that is a configuration question with a known answer, not an impossibility. The cross-machine-class half is where the claim retains its force. This is a real bound on INV-109 and I would rather record it here than have governance discover it later.

## Limitations

The study is GPU-centric, and the REE comparison that motivated INV-109 is CPU-to-CPU: 1008 on `linux-x86_64-py3.10-torch2.12.0+cpu`, 1010 on `darwin-arm64-py3.13-torch2.12.0`. The dominant divergence sources on that boundary are not the ones this paper attributes -- there is no nondeterministic cuDNN algorithm selection to blame; it is BLAS reduction order, math-library version, and (per this project's own cross-class measurement) `torch.multinomial` specifically, with `rand`/`randint`/`randperm`/`bernoulli` bit-identical. So the qualitative conclusion transfers and the numbers emphatically do not. Quoting 746 percent as REE's cost of determinism would be a category error.

The second limitation is the one this whole pull keeps running into: the paper's operative notion of "the same model" is behavioural. It measures accuracy and slice performance, not weight-state hashes. It therefore evidences the *consequences* of endpoint non-identity rather than endpoint non-identity itself. INV-109's prescribed instrument -- `hash_tensor_state` at both endpoints, re-verified at every evaluation boundary -- has no counterpart here.

## Confidence

0.78. The systems methodology is strong and the scale is real, and the subgroup finding is a genuinely independent replication of INV-109's structural shape. The discount is two-part: the unit of sameness is behavioural rather than weight-state (mapping fidelity 0.70), and GPU-accelerator conclusions are being read onto a CPU cross-class comparison (transfer risk 0.40). I have deliberately not let the supporting half of the paper set the direction; the determinism-is-purchasable result is a live constraint on how broadly INV-109 can be stated.
