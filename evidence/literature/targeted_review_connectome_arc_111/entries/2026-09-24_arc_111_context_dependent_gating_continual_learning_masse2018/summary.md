# Masse, Grant & Freedman 2018 -- context-dependent gating against catastrophic forgetting

**What they did.** Networks trained on one task after another usually forget the earlier ones, because new learning overwrites the weights that mattered. Masse and colleagues added a context signal that switches on a sparse, mostly non-overlapping subset of hidden units for each task. Each task's learning then lands mostly on its own units' weights. Combined with synaptic stabilisation, this let feedforward and recurrent networks, trained by supervised or reinforcement learning, keep performing across many tasks learned in sequence.

**Why it matters for ARC-111.** The 2026-09-21 falsifier-runnability audit found the core problem with ARC-111: its named first instance, ARC-108's w_chan, is one global, context-free buffer, so cross-context weight variance is zero by construction. The falsifier's precondition can never be met. This paper shows a cheap, biologically motivated way to build the missing object. A context-indexed mask selects a per-context effective weight set, and local learning then gives each context its own learned weights. It also shows why the weight form matters: with shared weights, context-dependent learning interferes, and that is where the benefit comes from.

**The caveat, again about the boundary.** The gate is a 0/1 multiplier on hidden units, which is formally a gain. Like Salinas & Sejnowski, this suggests the line between gain and weight is really about where the multiplier sits, on an output or on a hidden basis. That doesn't hurt the claim's behavioural requirement. It does mean the claim's wording, which contrasts "a gain" with "the weights themselves," should be rewritten in terms of what the conditioning acts on.

**Confidence.** 0.60.
