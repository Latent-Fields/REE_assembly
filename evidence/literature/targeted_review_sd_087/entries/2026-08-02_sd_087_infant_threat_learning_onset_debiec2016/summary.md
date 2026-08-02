# The neurobiology of safety and threat learning in infancy (Debiec & Sullivan, Neurobiol Learn Mem 2016)

## What the paper did

This is a review from the group that established the infant threat-learning sensitive period, synthesising roughly two decades of work on the infant rat. The core finding is that the aversive teaching signal is not present from birth. In early life the threat system is essentially quiescent and learning is biased toward *attachment* -- pups form preferences to caregiver-associated cues, and will do so even when the associated stimulus is painful (tail pinch, moderate shock). This is not a deficit; it is a design that keeps a dependent animal oriented toward the parent it cannot survive without.

At roughly the midway point to independence, pups gain access to the adult-like, amygdala-dependent threat system and begin showing responses to natural dangers such as predator odour. What makes this more than a maturation timetable is the gating. Between about postnatal day 10 and 15 pups can switch *between* the infant and adult-like systems, and which one is engaged is controlled by maternal presence and stress-hormone levels: alone, the pup learns fear; with the mother, it learns attachment. The mother can suppress the pup's corticosterone response and with it amygdala activation. Only near weaning does access to the attachment system close and the amygdala-dependent threat system become the sole route. The companion primary work (Thompson, Sullivan & Wilson 2008; Moriceau, Roth & Sullivan 2010) shows the synaptic correlate -- tetanic stimulation induces long-term plasticity in basolateral amygdala pathways in post-sensitive-period pups but not in sensitive-period pups, and GABA-A blockade reverts post-sensitive slices to the immature pattern.

## Why this matters for SD-087, in both directions

I have scored this entry `mixed`, and the reason is that it genuinely reads both ways.

**Supporting branch (a).** Biology does not run the aversive teaching signal from the start. It has a defined onset, and the valuation an animal forms *before* that onset is formed under a different teaching regime entirely -- attachment rather than threat. That is structurally the situation SD-087 describes: a default-trained REE agent (`harm_surprise_pe_enabled=False`) fits `z_harm_a` against the EMA accumulated-harm target, which is a different teaching regime from the one SD-020's validation was performed under. Under REE's brain-like-construction principle, the existence of a real onset window in the biology is the most naturalistic support available for the idea that *when* the harm teaching signal arrives is a design variable rather than an implementation detail.

**Cutting against a strict irreversibility reading.** The rodent switch is gated and, within the juvenile window, reversible in both directions. Maternal presence can reinstate attachment learning at PN10-15 in an animal that has already acquired access to the threat system. So the biology shows an onset *without* showing that a late-arriving signal cannot take. If anything it shows the opposite: the system is built to be switched. That is a direct constraint on how far the V3-EXQ-856 null can be read as evidence of a closed window, and it is the reason this entry is not scored `supports`.

## Limitations

This is the highest-transfer-risk entry in the pull and should not carry mechanistic weight alone. The mapping is an analogy between a biological maturational window and a configuration flag. REE has no corticosterone, no caregiver, and no maturational clock; the correspondence rests entirely on curriculum position standing in for developmental stage, and that substitution is unvalidated. It also interacts awkwardly with the raw-warmup curriculum-scope condition SD-087 inherits from SD-086, which is itself unresolved -- so the one REE-side variable that would carry the analogy is the variable already flagged as uncertain.

There is a further asymmetry worth naming. The onset in the rodent is driven by an exogenous clock (amygdala maturation, the end of the stress hyporesponsive period). An artificial agent has no exogenous clock, so "the signal must arrive at the right time" may have no REE-side referent at all -- the timing in REE is a free parameter set by whoever writes the curriculum, not a fact about the organism. And this is a review; it aggregates rather than testing the specific proposition that a teaching signal introduced late fails to reshape an already-trained valuation.

## Confidence reasoning

Source quality 0.78 -- authoritative authors and a well-established literature, but a review rather than primary empirical work, so capped below the primary papers here. Mapping fidelity 0.50 and transfer risk 0.55, both reflecting the rodent-infant-to-artificial-agent leap.

Aggregate 0.52, close to the component mean with no upward adjustment, because the supporting and disconfirming readings genuinely offset each other. Direction `mixed`. The right use of this entry is as construction guidance under the brain-like-construction principle -- it says the onset of a harm teaching signal is a real design variable that biology takes seriously -- and not as evidence about what V3-EXQ-856 measured.
