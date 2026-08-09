# Lee & Jung (2017) — Separation or binding? A critique of the DG-as-pattern-separator theory

**Source:** Neuroscience and Biobehavioral Reviews 75:183–194. DOI [10.1016/j.neubiorev.2017.01.049](https://doi.org/10.1016/j.neubiorev.2017.01.049). PMID 28174077. Retrieved via PubMed.

**Claim:** SD-016 (selection mechanism leg — bears on the portfolio's root framing).
**Direction:** weakens. **Confidence:** 0.61.

## What the paper argues

Lee and Jung take the popular theory — that the dentate gyrus exists to orthogonalise overlapping
input patterns into non-overlapping ones — and argue that it is not as well supported as its
ubiquity suggests. Their review concludes that "the theoretical support and empirical evidence for
this theory are not strong." In its place they advance an older alternative: that the DG's job is to
**bind together different types of incoming sensory information**, and that binding better captures
its contribution to memory encoding than separation does.

Two strands of their critique matter most here. The first is a conflation argument: "pattern
separation" in the behavioural literature means an animal discriminating between similar contexts,
while in the computational literature it means orthogonalising overlapping input vectors. These are
different claims and the field routinely slides between them, treating behavioural discrimination
deficits as evidence for a computational orthogonalisation function. The second is that a large share
of the causal evidence comes from adult-neurogenesis manipulations, which alter excitability, network
sparsity and mood-related behaviour well beyond any separation-specific role — so the causal
attribution is looser than the confident vocabulary implies.

## Why I included it, and what it does to the SD-016 case

This entry is here because a literature pull commissioned to ground a mechanism the autopsy already
favoured would be worth very little if it only found agreement. This is the strongest available
statement of the dissenting position, and it lands close to home.

The uncomfortable observation is this. The GOV-FANOUT-1 H3 leg proposes hard/competitive selection
*because* the biological reference is pattern separation. If the DG is better described as a
conjunctive binding stage, the correct import is close to the opposite — a mechanism that *combines*
`z_world` with other input streams into a conjunctive code, rather than one that sparsifies and
orthogonalises.

And SD-016's own claim text arguably describes binding rather than separation. Its
`functional_restatement` says the point is to associate an exteroceptive context cue with
hazard-relevant content, so that E2 affordance and E3 terrain precision can be modulated *before*
harm contact — the vmPFC somatic-marker analogue. Read that carefully and nothing in it requires
orthogonalisation. It requires a reliable *conjunction*. That is a genuine tension between the claim's
stated purpose and the fix the portfolio is about to build for it, and I would rather it were on the
record before three experiments run than discovered afterwards.

The practical output, though, is an **instrumentation** change rather than a redirection, and I want
to be clear about why. Binding is not operationalised in this paper to the point where it yields an
implementable REE mechanism; the critique is much better developed than the alternative. So the
useful move is to make the H3 leg capable of *detecting* the binding critique's signature rather than
to act on it pre-emptively:

> **Instrument downstream function alongside C1/C1b in the H3 leg.** If the binding account is right,
> sparsifying the retrieval will discard the conjunctive combination that the downstream consumers
> need — so we should expect low entropy (C1 passes), moving context-divergence (C1b passes), *and
> degraded* `terrain_loss` / downstream performance. That combination is a specific, falsifiable
> signature. Without a downstream measure it would be reported as an unambiguous partial win.

That costs essentially nothing to add and converts a philosophical objection into a discriminating
measurement, which is the only form in which this critique can actually earn its keep in the
portfolio.

It also compounds a warning the Cayco-Gajic & Silver entry raises from a different direction. That
paper says decorrelation is neither necessary nor sufficient for separation; this one says the
computational and behavioural senses of separation are conflated. Both converge on the same practical
point: **SD-016's C1/C1b instruments measure representational properties, and the claim's actual
purpose is behavioural.** V3-EXQ-418g is the precedent nobody should have to rediscover — slot
diversity forced to 1.000, attention entropy to 0.000, and downstream action-class entropy flat at
1.1e-10 across all four arms. Representational success with zero functional consequence has already
happened once on this exact claim.

## Limitations — and why this is 0.61 and not higher

I have deliberately not given this entry parity with the direct measurements in this directory, and
the reasons are worth stating so a later reader does not over-weight it:

- **It is a minority position argued in a review, with no new data.** It is a reading of the
  literature, set against papers like Neunuebel & Knierim (2014) that report direct simultaneous
  recordings.
- **It predates the strongest evidence against it in this pull.** Espinoza et al. (2018) came a year
  later and materially strengthens the WTA/separation architecture case — the DG's lateral:recurrent
  inhibition ratio of 9.25, an order of magnitude away from every other measured circuit, is exactly
  the kind of specialisation that is hard to explain if separation is not a real function. Lee and
  Jung were not arguing against that.
- **The alternative is under-specified.** "Binding" does not come with a circuit mechanism the way
  WTA does. That asymmetry is real and is the reason this entry produces an instrument recommendation
  rather than a design one.
- **Part of the dispute is orthogonal to what SD-016 can test.** The separation-versus-binding
  argument is framed around a complete memory system with encoding and retrieval phases; SD-016's
  lineage has only retrieval selection under test, with no encoding phase in the experiment. Some of
  the disagreement simply cannot be adjudicated by anything in this portfolio.

My reading, on balance: the H3 leg remains well motivated and should proceed. But the portfolio should
carry the knowledge that its biological reference is **contested rather than settled**, and it should
instrument for the specific failure this critique predicts. The V3-EXQ-898 autopsy characterised REE's
tagger as a "formal-definition import" of pattern separation. This paper raises the sharper
possibility that the definition being imported may itself not be securely grounded in the biology it
is borrowed from — which is a different and more interesting problem than getting the import wrong.
