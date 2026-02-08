> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

# Minimal Signalling Channel (Pre-language)

Before full language, REE benefits from a minimal signalling interface that can externalise:
- harm/degradation alerts
- intent/commitment markers
- uncertainty/confidence markers
- "stop/avoid" priors (trajectory warnings)

### Interface sketch
Inputs: internal summaries (z_theta/z_delta slices, residue flags, confidence)
Outputs: discrete or continuous signals that other agents can condition on

### Design constraints
- Signals are integrated via trust-weighting (reliability inference)
- Signals cannot mask embodied harm channels in the receiving agent
- Signals should be cheap relative to full other-model inference