# Cayco-Gajic & Silver (2019) — Re-evaluating circuit mechanisms underlying pattern separation

**Source:** Neuron 101(4):584–602. DOI [10.1016/j.neuron.2019.01.044](https://doi.org/10.1016/j.neuron.2019.01.044). PMID 30790539 / PMC7028396. Retrieved via PubMed.

**Claim:** SD-016 (selection mechanism leg — bears on both H2 and H3).
**Direction:** mixed. **Confidence:** 0.74.

## What the paper argues

This is a synthesis review with a thesis, and the thesis is a correction. Cayco-Gajic and Silver take
three circuits that are all conventionally described as pattern separators — the cerebellar granule
layer, the insect mushroom body, and the dentate gyrus — and argue that recent findings "have
questioned long-held ideas" about how any of them actually do it.

Their reframing is that the right common currency is the **dimensionality of the space available for
population codes**. What these circuits share is not lateral inhibition or sparse firing but *sparse,
divergent connectivity that expands the input into a much larger population*, and thereby into a
higher-dimensional representation where previously overlapping patterns become linearly separable.
Sparse activity levels and lateral inhibition are, in this account, modulators of that expansion
rather than the mechanism itself. They also make a point about what the computation is *for*: the
pay-off is facilitating associative learning in the presence of trial-to-trial variability, not
decorrelation as an end in itself. And they emphasise that the three circuits use genuinely
*different* strategies — the shared label conceals real mechanistic divergence.

## Why this matters for SD-016 — and why it changes a recommendation

I included this entry as the counterweight on the other four, and it turned out to earn its place by
changing a design recommendation rather than merely adding caution. It is worth stating the
uncomfortable part plainly.

The paper **agrees** with this pull's central thesis: pattern separation is produced by structural
circuit properties, not by a downstream objective demanding it. That is the V3-EXQ-898 autopsy's
diagnosis and it survives.

But it **reassigns which structure carries the load** — from competition to expansion. And SD-016's
retrieval path runs the wrong way. `extract_cue_context` maps a 32-dimensional `z_world` onto **16
slots**. That is a dimensionality *contraction*. Every circuit in this review is strongly *expansive*
— the dentate gyrus has roughly tenfold more granule cells than its entorhinal input, and the
cerebellar granule layer is more extreme still.

If Cayco-Gajic and Silver are right, then applying a competitive operator to 16 slots is applying it
to a representation that has already been squeezed below the dimensionality at which separation is
achievable. H3 might then improve the entropy metric without touching the actual problem.

I do **not** read this as a reason to stand H3 down. The operator change is cheap, it is well
motivated by Espinoza's connectivity measurements, and the portfolio is explicitly a discrimination
exercise — a null on H3 is informative. But it does argue for a concrete addition to how H2 is
scoped: **slot count / expansion should be a first-class variable in the H2 leg**, not just "what
should a structured retrieval unit look like." A slot-count ladder — 16 / 64 / 256 with matched
sparsity — is cheap, directly motivated by this paper, and is an arm the portfolio does not currently
contain. Given that the portfolio's §5 adversarial audit already worried about scale/capacity
coverage and resolved it via matched-budget baselines on the *training* side, this is the same worry
reappearing on the *representational* side, where it has not been addressed.

There is a second, subtler warning here that lands squarely on SD-016's instruments. The authors
argue decorrelation is neither necessary nor sufficient for pattern separation. SD-016's C1b
context-divergence measure is close to a decorrelation metric. So a design could move C1b — pass the
acceptance criterion — without improving the associative-learning function that separation exists to
serve. SD-016's own leg B (downstream behavioural exploitation) is already known to be gated and
untested, and V3-EXQ-418g is the cautionary precedent: it *forced* slot diversity to 1.000 and
attention entropy to 0.000, and downstream action-class entropy stayed flat at 1.1e-10 across all
four arms. Representational success with zero functional consequence has already happened once on
this claim. This paper explains why that is the expected failure mode rather than a surprise.

## Limitations

Two honest discounts, both of which I have priced in.

First, this is synthesis and argument, not new measurement. The expansion thesis is strongest for the
cerebellar granule layer, where the anatomy is most extreme; the dentate gyrus is the case the authors
treat most tentatively. Anyone citing this against the Espinoza connectivity data should notice that
Espinoza is a direct measurement and this is an interpretive frame — they are not the same kind of
evidence, and where they pull in different directions the measurement should generally win on the
narrow question it addresses (does the DG have WTA-compatible wiring? yes, clearly).

Second, and this one blunts the naive fix: **"dimensionality" here is a property of the population
code, not of the unit count.** It is how many independent directions the activity actually spans.
Raising SD-016's slot count from 16 to 256 would not produce expansion if the slots stay correlated —
and given that the entire observed pathology is slots behaving identically, correlated slots is the
default expectation, not a remote risk. So the ladder arm above has to be instrumented on the
*effective dimensionality of the selection distributions*, not on slot count. That is a real
instrument-design task, and flagging it is probably this entry's most practically useful contribution
after the expansion observation itself.

Third, their functional criterion — associative learning under trial-to-trial variability — is
something SD-016 does not currently measure at all. Importing their framing honestly means adding an
instrument, not just an arm. I would not gate H2 on building that instrument, but it belongs in the
claim's `what_would_answer` the next time it is revised.
