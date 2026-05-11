# targeted_review_mech_316_cross_episode_regularity -- Index

Targeted literature review for **MECH-316**: the cross-episode regularity-extraction substrate of ARC-064 bottom-up rule discovery. Adjudicates which implementation flavour the substrate-design pass should commit to among the four candidates Pull 1 surfaced: (a) Bayesian latent-cause inference, (b) successor-representation, (c) attention-modulated RL, (d) explicit structure-learning over discrete structural forms.

| Entry | Source | Year | Direction | Confidence | Implementation flavour |
|-------|--------|------|-----------|-----------|------------------------|
| 2026-05-11_mech_316_latent_structure_learning_gershman_niv_2010 | Gershman & Niv, *Curr Opin Neurobiol* | 2010 | supports | 0.80 | Bayesian latent-cause (framework anchor) |
| 2026-05-11_mech_316_context_causal_structure_gershman_2017 | Gershman, *Psychon Bull Rev* | 2017 | supports | 0.76 | Bayesian latent-cause (operationalisation extension) |
| 2026-05-11_mech_316_hippocampus_preserves_order_davachi_dubrow_2015 | Davachi & DuBrow, *Trends Cogn Sci* | 2015 | supports | 0.74 | empirical substrate anchor (hippocampal) |
| 2026-05-11_mech_316_rl_multidimensional_attention_niv_2015 | Niv et al., *J Neurosci* | 2015 | supports | 0.82 | attention-modulated RL (foundational anchor) |
| 2026-05-11_mech_316_discovery_structural_form_kemp_tenenbaum_2008 | Kemp & Tenenbaum, *PNAS* | 2008 | mixed | 0.62 | structure-learning (boundary-case anchor) |

Note: Pull 1 (ARC-064 bottom-up rule discovery, 2026-05-10) already anchored the successor-representation flavour with Stachenfeld et al. 2017 and Momennejad et al. 2017, and anchored the hippocampal CLS-monosynaptic substrate role with Schapiro et al. 2017. Pull 2 does not re-cite those entries -- the Pull-1 synthesis already covers them; Pull 2 is the implementation-flavour adjudication that Pull 1's R2 verdict deferred.

See `synthesis.md` for R-verdicts on R1 (which implementation flavour is the architectural target), R2 (does MECH-316 need explicit inference machinery or does an SR / attention substrate suffice), R3 (the Davachi-DuBrow empirical-signature anchor), and R4 (what experimental design distinguishes the flavours on REE's behavioural-trajectory-record substrate).
