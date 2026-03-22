# Literature Summary: 2026-03-22_mech090_engel_fries_beta_status_quo_2010

## Claims Tested

- `MECH-090`

## Source

- Engel AK, Fries P (2010). *Beta-band oscillations -- signalling the status quo?*. Current Opinion in Neurobiology.
- DOI: `10.1016/j.conb.2010.02.014`
- URL: `https://www.sciencedirect.com/science/article/pii/S0959438810000389`

## Source Wording

Beta oscillations (~13-30 Hz) actively signal "the status quo" — a top-down maintenance signal that keeps the current sensorimotor or cognitive state in force against disruptive change. This framing distinguishes beta from a simple idle rhythm: beta is elevated when the system is in a committed state and must resist updating, and suppressed when the system needs to initiate change or respond to new input. Beta desynchronization precedes voluntary movement; beta resynchronization follows movement completion, marking the re-establishment of the maintained state. The same maintenance logic applies in cognitive control: elevated beta during delay periods preserves the task-relevant representation against interference.

## REE Translation

MECH-090 (beta-gated policy output during committed sequences): Engel & Fries's status-quo framing directly supports the committed-sequence interpretation in MECH-090. Elevated beta during an ongoing action sequence is an active signal maintaining the current committed plan, preventing E3 from propagating an updated policy prematurely. The sequence-completion resynchronization maps to the post-completion beta-drop in MECH-090, which releases the gate on E3 output propagation. This review provides the conceptual foundation distinguishing MECH-090's committed-maintenance role from the idle/default-rhythm interpretation that would undermine the claim.

## Caveat

The review does not directly test the internal-model-update vs output-propagation distinction that is specific to MECH-090 — it establishes that beta gates *change* in general, not specifically whether it blocks output while allowing internal computation to continue. Circuit-level corroboration from Helfrich & Knight (2019, this review series) is needed for the propagation-gating specificity. Also, the status-quo framing has been debated since 2010; alternative accounts (e.g., beta as predictive coding signal) partially challenge but do not refute the maintenance interpretation.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.80`
