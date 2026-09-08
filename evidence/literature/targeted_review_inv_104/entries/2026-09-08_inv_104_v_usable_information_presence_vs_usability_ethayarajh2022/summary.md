# Understanding Dataset Difficulty with V-Usable Information (Ethayarajh, Choi & Swayamdipta, ICML 2022)

## Why a dataset-difficulty paper is in an INV-104 pull

INV-104 asserts that five classes of distinction must be *preserved, or left recoverable through the
dynamics*, across every compression step on the observation -> z_world -> E1/E2 path. That
disjunction is doing real work, and it is the part most likely to be measured badly. The claim's own
falsifier text says so in as many words: T1 alone is not the test, because V3-EXQ-978 found the
class-1 field linearly decodable at r2 0.710 (sense path) / 0.858 (encoder path) while V3-EXQ-948
found a downstream reader on that same latent sitting at 0.5 resources/episode against a 1.0
competence floor. Present and usable came apart on this exact class.

This paper is the formal statement of why that is not an anomaly but the expected case. Building on
Xu et al.'s predictive V-information, Ethayarajh and colleagues make explicit that "how much
information X carries about Y" is not well-posed until you name the family V of functions permitted
to do the extracting. Fix V, and you get V-usable information -- and with it the pointwise version,
PVI, per instance. Change V, and the quantity changes. A quantity that is high for an unbounded
extractor can be zero, or negative, for a bounded one.

## What follows for the falsifier

Three things, and they are all about measurement discipline rather than about the substance of the
preservation contract.

First, it retrospectively vindicates the decision to make R_k rather than probe r2 the verdict
statistic. A ridge or logistic probe *is* a choice of V -- a very small one. Reporting its r2 and
calling the class "preserved" is reporting V-usable information for a family nobody downstream
belongs to.

Second, it constrains how the arms must be built. R_k is
`(acc_compressed - acc_untrained_projection) / (acc_raw_input - acc_untrained_projection)`, and that
ratio is only interpretable if the adapter family is *identical* across all three arms. NDP-4
already requires the same-capacity floor arm; this paper explains why that requirement is load-bearing
rather than tidy-mindedness. Vary the adapter capacity between arms and R_k stops being a statement
about the compression at all.

Third -- and this is the uncomfortable one -- V-information can be negative. A representation can
make a bounded extractor *worse* than the label prior, if its geometry is adversarial to that
extractor family. So a sub-floor R_k does not license the conclusion "the class was destroyed". It
is equally consistent with MECH-517's H-C route: the information is there and the geometry is
wrong. INV-104's conditional-interpretation clause already anticipates this for H-B (consumer never
learned the mapping); the V-information framing says the same caution applies to H-C, and that the
discrimination has to come from somewhere other than R_k's magnitude.

## Where I have not let this reach

This is an NLP paper about annotation artefacts in text benchmarks. Nothing in its empirical results
transfers to an embodied agent's world-model compression, and I have not tried to make it. What
transfers is a definitional point that happens to be domain-general, plus the negative-information
caution. More importantly, the paper is completely silent on INV-104's actual content: it gives a
principled way to ask whether a distinction is usable, and says nothing whatsoever about which
distinctions an organism must keep. That is the whole substantive burden of INV-104 and this paper
does not touch it.

## Confidence

0.62, and the decomposition is where the honesty lives: source_quality 0.88, mapping_fidelity 0.55.
This is excellent evidence for a premise of the falsifier's design and weak evidence for the claim
itself. Recording it as "supports" with a high confidence would misrepresent what it supports.
