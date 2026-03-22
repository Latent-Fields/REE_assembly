# Literature Summary: 2026-03-22_mech089_canolty_knight_cfc_2010

## Claims Tested

- `MECH-089`

## Source

- Canolty RT, Knight RT (2010). *The functional role of cross-frequency coupling*. Trends in Cognitive Sciences.
- DOI: `10.1016/j.tics.2010.09.001`
- URL: `https://www.sciencedirect.com/science/article/pii/S1364661310001890`

## Source Wording

Theta-phase to gamma-amplitude coupling (theta-gamma PAC) is a robust phenomenon across human hippocampus, entorhinal cortex, and prefrontal cortex, observed during memory encoding, working memory maintenance, and attentional tasks. The mechanism: the phase of a slow oscillation (theta, ~4-8 Hz) modulates the amplitude of fast oscillations (gamma, ~30-100 Hz), such that gamma bursts preferentially occur at specific theta phases. This allows a slow hierarchical system to read out the activity of a fast local circuit in batches aligned to the theta frame. CFC is proposed as a general neural mechanism for hierarchical integration across circuits operating at incompatible timescales.

## REE Translation

MECH-089 (theta-gamma CFC as ThetaBuffer substrate): Canolty & Knight provide the most direct mechanistic account of how CFC enables inter-level information transfer. In REE terms, E1 generates fast prediction-error signals at the gamma-equivalent rate; theta-gamma CFC packages these into theta-phase-aligned summaries that E3 can sample at its slower deliberation rate. The ThetaBuffer is the computational instantiation of this biological packaging mechanism. Importantly, this review covers human prefrontal CFC as well as hippocampal CFC, extending the Lisman & Jensen rodent spatial result to the planning-hierarchy domain most directly relevant to REE.

## Caveat

The review establishes that CFC is a communication mechanism across timescales but does not directly demonstrate that downstream slow-oscillation systems are functionally blind to fast-oscillation content outside of theta windows. The strong MECH-089 claim that "E3 never sees raw E1" is architecturally motivated by CFC but not directly proven by it — this distinction would require lesion-equivalent evidence or targeted decoupling experiments not present in the reviewed literature. The specific theta rate (~4-8 Hz) is substantially faster than some conceptions of E3 deliberation; rate calibration is needed in V3 design.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.84`
