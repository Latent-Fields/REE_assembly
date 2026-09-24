# REPORT -- targeted_review_boundary_contracts_information_bottleneck (ARC-144, GOV-CONTRACT-3)

No prior literature entries existed for either claim (grep empty). timestamp_utc = 2026-09-24T11:24:42Z for all.

## Entries

- 2026-09-24_arc_144_information_bottleneck_relevance_variable_tishby1999 -- supports, 0.45 -- relevance is defined only relative to a consumer variable Y, so there is no Y-free "what must pass"; motivational/definitional, not evidence about real interfaces.
- 2026-09-24_arc_144_decoder_side_information_rate_distortion_wyner1976 -- supports, 0.50 -- the minimum rate at a tolerated distortion depends on the decoder's side information: the closest formal counterpart of I_AB ("needs, minus can reconstruct locally") and of the {I_AB, distortion, receiver capability} entry. Theorem with unbounded decoders.
- 2026-09-24_gov_contract_3_usable_information_computational_constraints_xu2020 -- supports, 0.60 -- V-information (bounded decoder family) formalises "operational, not information-theoretic" reducibility; it can be created by computation (violates DPI). Also tags ARC-144.
- 2026-09-24_gov_contract_3_mdl_probing_decoder_complexity_voita2020 -- supports, 0.50 -- MDL probing charges for decoder effort, closing the "powerful decoder" loophole the relocation checklist names; method template, a different domain (NLP probes).
- 2026-09-24_gov_contract_3_information_bottleneck_deep_learning_critique_saxe2019 -- weakens, 0.55 -- the IB compression phase is activation- and estimator-dependent and not causal for generalisation; undercuts citing IB as evidence that modules DO compress to task-relevant payloads, and warns that MI cost terms can be estimator artefacts. Also tags ARC-144.

## Anchors the claims named

Both claims name only literatures, not specific papers ("information-bottleneck, rate-distortion and MDL ... a /lit-pull is owed BEFORE any is cited as support").
- Information bottleneck (Tishby, Pereira & Bialek, Allerton 1999, pp. 368-377; arXiv physics/0004057): verified by WebSearch hits. No DOI given.
- Rate-distortion: represented by Wyner & Ziv 1976 (IEEE Trans Inf Theory 22(1):1-10, doi 10.1109/TIT.1976.1055508) as the receiver-dependent variant. Verified by WebSearch hits.
- MDL: Grunwald, "A tutorial introduction to the minimum description length principle" (arXiv math/0406077, 2004; extended from the MIT Press 2005 collection) was verified by WebSearch but not written as an entry. It is only a general anchor. Voita & Titov 2020 is the operational application and is cited in its place.
- Saxe et al. critique: verified. The journal version is J Stat Mech 2019, 124020, doi 10.1088/1742-5468/ab3985 (ICLR 2018 conference version).

## Which support "boundary-indexed, not one universal header", and which are only motivational

- **Only motivational:** Tishby et al. (IB). It shows the right compression is relative to the consumer's task. It does not show that real interfaces differ, or how much they overlap.
- **Formal support for the form of the contract entry:** Wyner-Ziv. The required rate is indexed by the receiver's side information and the tolerated distortion, per link. It is still a theorem, with unbounded decoders.
- **Supports GOV-CONTRACT-3's operational standard, not ARC-144's boundary indexing directly:** Xu et al. and Voita & Titov.
- **None of these bear on ARC-144's actual falsifiable content,** the size of the SHARED CORE across heterogeneous boundaries. I found no literature measuring obligation overlap across many interfaces. That remains purely empirical.

## Implications for the claim TEXT (suggested; not applied)

1. GOV-CONTRACT-3 notes say the IB/RD/MDL literatures are "the obvious anchors" for contract cost. Suggest amending: plain IB and RD use Shannon information with ideal decoders, which is exactly the information-theoretic reducibility the rule calls inadmissible. The better-matched anchors are usable/V-information (Xu et al. 2020) and MDL with the decoder's cost counted (two-part/online codes; Voita & Titov 2020). Citing plain IB as support for the rule would be self-contradictory.
2. GOV-CONTRACT-3 requirement (1), "fixed assumptions about precision and decoder power": V-information makes clear the verdict is a function of the decoder family V. Suggest the rule require V (the receiver's decoder class) to be declared BEFORE a merge is scored, so V cannot be chosen after the fact.
3. GOV-CONTRACT-3 falsifying branch ("cost terms not estimable"): Saxe et al. show MI estimates in deterministic networks can be estimator artefacts. This makes that branch a live risk. Prefer bounded-decoder or code-length measures over raw MI.
4. ARC-144: I_AB's "cannot cheaply reconstruct locally" is a resource-bounded version of Wyner-Ziv side information (and of the Shannon-vs-V_B gap). Citing Wyner-Ziv for the form is fair, with the caveat that it is resource-unbounded. Do not cite IB as evidence that trained modules compress to receiver-relevant payloads (Saxe et al.).

## Could not verify / limits

Egress policy blocked arxiv.org, semanticscholar (API and site), dblp, openreview, ieeexplore and princeton.edu for both WebFetch and curl. All bibliographic fields therefore come from WebSearch result summaries of the publisher/index pages, not from the pages themselves. Consequences:
- No DOI for Tishby 1999 (none exists for the Allerton paper) or Xu 2020 (ICLR). A url was used instead.
- Page and volume fields for Wyner-Ziv and Voita-Titov come from search summaries. A spot-check on a machine with IEEE/ACL access is advisable before merge.
- I could not read full texts, so content claims rest on abstracts as rendered in search results plus standard knowledge of these results.
