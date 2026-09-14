# Lit/Exp Decoupling (Option E) -- phase history

**Status: closed.** The three-phase migration described below completed on
2026-05-01; `REE_assembly/CLAUDE.md` "Lit/Exp Decoupling (Option E)" carries
only the two-line current-state pointer to this file. Moved out of CLAUDE.md
2026-09-14 (WI-B2 Item B, `claude_code_prompt_audit_20260914.md` row 3b/1) --
the phase narrative had been sitting in present-tense prose describing a
cutover that finished four months earlier, with no reader-facing reason to
re-derive it from CLAUDE.md on every read.

## Phase history

- **Phase 1 (2026-04-29):** shadow-only -- added decoupled fields and a
  sibling recommendations report. No production behavior changed.
- **Phase 2 (2026-04-29 .. 2026-05-01):** discrepancy reckoning -- the
  shadow report exposed 15 implementation-cohort claims with zero
  experimental backing. Categorised them along existing claim_type lines:
  6 substrate_coherence (correctly suppressed), 5 answer_state (correctly
  exempt), 4 standard-gating that needed experiments. All 4 standard-gating
  claims (MECH-094, SD-017, SD-035, MECH-062) had discriminative-pair
  experiments queued and PASSed; all are now `confirmed_established`.
- **Phase 3 (2026-05-01):** cutover landed. Production gates now drive on
  `experimental_confidence`. Diff against the pre-cutover snapshot:
  +2 actionable demotion recommendations surfaced (MECH-095, MECH-102 --
  both `mechanism_hypothesis` whose lit_conf was masking insufficient
  exp_conf under the legacy blend), 0 prior recommendations lost.

See `REE_assembly/CLAUDE.md` "Lit/Exp Decoupling (Option E)" for the current
regime (the 2D quadrant table, what Phase 3 changed, what is preserved) and
`memory/feedback_lit_exp_decoupled.md` for the methodology rule (never
re-tune the lit/exp blend coefficients -- the blend itself was the bug) and
the failed B-strict / B-softened / C-balanced staging variants.
