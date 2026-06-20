# Bogacz & Gurney (2007) — The basal ganglia and cortex implement optimal decision making between alternative actions

**Source:** Bogacz, R., Gurney, K. (2007). *Neural Computation* 19(2):442-477. [DOI 10.1162/neco.2007.19.2.442](https://doi.org/10.1162/neco.2007.19.2.442) · PMID 17206871. (According to PubMed.)

**Claim under test:** MECH-439 — and specifically the *optimality* framing of the cortico-STN threshold (the Bogacz seed line of the "Bogacz & Cohen" threshold-adaptation pairing).

## What the paper did

Bogacz and Gurney show analytically that the cortico-basal-ganglia loop is wired exactly as it would need to be to implement the **multihypothesis sequential probability ratio test (MSPRT)** — the asymptotically optimal statistical procedure for deciding among N alternatives with the fewest samples for a given error rate. In their mapping, cortical channels integrate evidence for each alternative; the **STN computes a normalization term** by pooling activity across *all* competing channels; and the basal-ganglia output nucleus gates the option whose *normalized* evidence first crosses threshold. The key structural claim is that the decision is made on a **likelihood ratio** — each option's evidence evaluated *against the whole competing field* — not on any option's raw magnitude. They validate predicted firing properties against existing physiology and show the implementation is parametrically robust and outperforms rival neural decision schemes.

## Why it is mixed for MECH-439 (and why that is the useful part)

This paper is the single most load-bearing entry in the pull, and it is genuinely two-directional.

**It supports the problem framing.** MECH-439 says F monopolises ~88-89% of E3 committed-selection variance, so the committed argmax cannot reflect the modulatory field. Read through MSPRT, that is *precisely a normalization failure*: REE commits on F's raw dominance rather than on F evaluated as a likelihood ratio against the competing field. The strongest normative theory of basal-ganglia decision making says the whole point of the STN is to arbitrate one channel against the *whole* field — exactly the operation whose absence the cluster autopsy diagnosed. So the diagnosis ("the F-monopoly is the bottleneck; the missing dependency is the field-normalizing STN term") is not REE-parochial; it is what the optimal-decision theory predicts a missing STN normalization would look like.

**It weakens the specific fix.** The biologically-optimal STN operation is a **continuous, global normalization** across all alternatives on every step. REE's `k=f(F-gap)` is neither continuous nor global — it widens a discrete shortlist *only when the top-F gap is small*. Where F dominates the global sum (the very F-monopoly regime MECH-439 targets), a purely local near-ties widening cannot recover the optimal likelihood-ratio computation: the dominant channel stays dominant after the widening, because the widening does nothing to F's scale relative to the field. The MSPRT account therefore predicts that the top-k lever is a *coarse approximation* that will cap committed entropy below the proposer ceiling — the cluster autopsy's pessimistic **Reading-2** — and that the *principled* lever is direct, rank-preserving F→eligibility demotion (a renormalization of F against the field), not a shortlist truncation.

This is the divergence the user asked to be treated as load-bearing rather than as a caveat. The strongest biological theory of BG decision making points **past** the proposed fix toward the alternative lever the autopsy already named as Reading-2. That does not falsify MECH-439 — it sharpens the planning fork: the optimal mechanism is a normalization, and `k=f(F-gap)` is a local stand-in for it.

## How this should read against the 689a result

689a's pre-registered falsifier — does the committed-entropy lift correlate with the per-tick F-gap? — is exactly the test of whether the local approximation is adequate. A lift that correlates with F-gap says the near-ties truncation captures enough of the normalization to matter on this substrate (the optimistic Reading-1). A lift that does *not* correlate, or no lift, corroborates the MSPRT reading that only a continuous global renormalization (direct F-variance rebalancing) will do. Bogacz & Gurney gives that fork a normative spine: it tells us *which* of the two readings is the biologically-optimal end-state, so a 689a FAIL is triaged toward F-renormalization rather than logged as a bare null.

## Confidence

I assign **mixed, confidence 0.6**. Source quality is high — the canonical normative theory of BG decision making, analytically derived and physiology-validated. Mapping fidelity is moderate: the optimality/normalization *framework* maps tightly onto the F-monopoly diagnosis, but the specific optimal *operation* (continuous global normalization) diverges from the proposed discrete top-k. Transfer risk is moderate: a normative model transfers cleanly in principle, but its optimality guarantees assume a likelihood-ratio formulation REE's E3 selector does not yet implement — so the "optimal lever" it endorses (F-renormalization) is a *different build* than 689a, and that difference is the point.
