# V3-EXQ-970a -- ContextMemory write-content H1 on the redesigned MI instrument (supersedes V3-EXQ-970)

**Status:** PASS  **Label:** training_raises_content_conditioning_content_reference_not_required_a_h1pass_divfail_b_h1pass_divpass

| unit | readout | mean UNTRAINED | mean arm | mean diff | p | gate | pass |
|---|---|---|---|---|---|---|---|
| A::H1_CONTRASTIVE | heldout_real_nmi_excess | 0.018 | 0.312 | 0.294 | 0.0039 | True | True |
| A::DIVERSITY_956 | heldout_real_nmi_excess | 0.018 | 0.011 | -0.007 | 0.5117 | True | False |
| B::H1_CONTRASTIVE | synthetic_fresh_nmi_excess | 0.067 | 0.259 | 0.192 | 0.0039 | True | True |
| B::DIVERSITY_956 | synthetic_fresh_nmi_excess | 0.067 | 0.310 | 0.244 | 0.0039 | True | True |

refractory k=2 reference: A -0.018, B 0.026

margin 0.1, alpha_corrected 0.0125
