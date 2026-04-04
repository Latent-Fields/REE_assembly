# Hierarchical predictive coding in distributed pain circuits

**Chen ZS (2023) — Frontiers in Neural Circuits — DOI: 10.3389/fncir.2023.1073537**

---

## What the study did

This mini-review synthesizes evidence from human neuroimaging and animal electrophysiology studies to propose a hierarchical predictive coding framework for distributed pain circuits. The review identifies the cingulate cortex and insula cortex as the two major hubs integrating information from sensory afferents and spinothalamic inputs. It proposes active inference as the generalized computational algorithm, with hierarchically organized traveling waves of neural oscillations providing the implementation mechanism for bottom-up and top-down information flow across the distributed pain network.

## Key findings

The review consolidates the functional dissociation between insula subregions: the anterior insula cortex (AIC) responds as a modality-unspecific aversive surprise signal (unsigned intensity prediction errors), while the dorsal posterior insula cortex (PIC) encodes modality-specific signed intensity prediction errors -- that is, directional departures from expected stimulus intensity. This is subtly different from the simpler view that posterior insula merely encodes raw intensity: it encodes the signed discrepancy between predicted and received intensity, which still maintains it as the sensory-discriminative stream but makes it part of the predictive hierarchy rather than a passive relay.

The review also proposes that different subregions of cingulate and insula cortices have distinct projections and functional roles, supporting the idea that the pain network is not a monolithic system but a set of computationally specialized modules. Importantly, the review notes that whether the distributed network is completely decentralized or requires networkwide coordination remains an open question -- intellectual honesty that is worth preserving in how these results are applied.

## Translation to REE and ARC-033

ARC-033 asserts that SD-003 requires a dedicated forward model E2_harm_s for the sensory-discriminative harm stream, separate from E2.world_forward. This review provides the theoretical framework that makes that architectural choice principled rather than arbitrary.

In hierarchical predictive coding, every level of the processing hierarchy requires a generative (forward) model predicting activity at the level below. For the pain system, the dorsal posterior insula (z_harm_s's biological correspondent) sits within a hierarchy that requires its activity to be predictable from higher-level states. E2_harm_s is exactly this: the model that predicts how z_harm_s evolves given the agent's action, allowing SD-003 to compute the counterfactual harm state z_harm_s_cf. The AIC prediction-error signal (E3's reading of the harm stream) and the dorsal PIC intensity signal (E2_harm_s's prediction target) map onto the architectural roles that the review describes for these regions.

The review also supports the architectural independence claim: the insula-cingulate pain hierarchy is anatomically and computationally distinct from the sensorimotor forward model hierarchies in the cerebellum and motor cortex. This independently motivates ARC-033's claim that E2_harm_s cannot be a component of E2.world_forward -- they operate in different substrates with different projections.

## Limitations and caveats

This is a theoretical review with no novel empirical data. The active inference framing carries theoretical commitments that REE does not fully adopt -- in particular, the free energy minimization objective and precision-weighted prediction error computation differ from how REE trains E2_harm_s (loss-minimization on harm-delta prediction). The traveling-wave implementation mechanism proposed for biological predictive coding has no direct equivalent in an ANN substrate; if the hierarchical structure is critically substrate-dependent, the transfer is limited.

The dorsal PIC as signed intensity prediction error (rather than raw intensity) is also worth noting: if z_harm_s corresponds to dorsal PIC rather than a purely intensity-encoding signal, then E2_harm_s is predicting a channel that already incorporates some expectation-comparison. This is architecturally fine for ARC-033, but it means the forward model is predicting a slightly richer signal than pure proximity. The EXQ-166e harm-delta architecture (predicting the change in harm_obs rather than absolute harm_obs) is actually consistent with this interpretation.

## Confidence reasoning

Confidence is 0.65 -- the appropriate level for a theoretical review in the correct domain. The framework alignment is strong, the failure signatures are real (decentralization uncertainty, substrate dependence), and the paper's value is in providing theoretical context rather than empirical confirmation. It functions well as a framework paper alongside the Geuter 2017 and Song 2021 empirical entries.
