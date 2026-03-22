# Literature Summary: 2026-03-22_mech047_dfc_switching_vidaurre2017

## Claims Tested

- `MECH-047`

## Source

- Vidaurre D, Smith SM, Woolrich MW (2017). *Brain network dynamics are hierarchically organized in time*. PNAS.
- DOI: `10.1073/pnas.1705120114`
- URL: `https://www.pnas.org/doi/10.1073/pnas.1705120114`

## Source Wording

Using a hidden Markov model (HMM) applied to resting-state fMRI from 1003 HCP participants, the authors identify 12 recurrent transient brain states with characteristic dwell times ranging from approximately 100 ms to several seconds. Transitions between states are governed by a non-uniform transition probability matrix: certain state pairs interconvert readily (high transition probability, effectively a fast switching corridor), while others show very low transition probability, constituting what the authors term a "switching barrier." The temporal structure is hierarchical: faster micro-state fluctuations occur within longer-lasting macro-state epochs, and the spectral content of each level differs systematically. The authors argue this hierarchical organisation reflects the multi-timescale architecture of brain networks and is not reducible to a flat set of equiprobable transitions.

## REE Translation

MECH-047 (mode-commitment hysteresis): The non-uniform transition probability matrix from Vidaurre et al. provides direct empirical grounding for the REE mode-transition gate. State pairs with low transition probability are the empirical analog of mode pairs with high switching cost in MECH-047. Specifically, the asymmetry in transition probabilities (some modes are rarely entered from certain source modes) supports the hysteresis account: once in a mode, the system's history biases it to remain there. The hierarchical temporal nesting maps naturally to REE's two levels of dynamics -- within-mode processing (E1/E2-rate fluctuations, fast micro-states) vs. control-plane mode changes (E3-rate macro-state transitions). The dwell-time distributions provide a quantitative prior for calibrating the hysteresis time constant in the MECH-047 implementation.

## Caveat

The 12 HMM states are derived from resting-state data and are not labelled by cognitive function. The three REE modes (doing, ready-vigilance, default-mode) are task-defined categories and cannot be read off directly from HMM state labels. The mapping from specific HMM states to REE modes requires additional functional localisation (e.g., task-fMRI state decoding) that this paper does not provide. The paper also does not manipulate or measure arousal, so the LC-NE gating component of MECH-047 is not addressed here -- that support comes from TRK-LC (Aston-Jones & Cohen 2005).

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.74`
