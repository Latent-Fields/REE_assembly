# Thought-digestion staging -- 2026-09-22 -- action-conditioned world model / arousal-gated commitment

**What this is.** Draft `what_would_answer` text produced in the SAME session as the Stage 2 intake
`evidence/planning/thought_intake_2026-09-22_action_conditioned_world_model_and_arousal_gated_commitment.md`,
staged here for the user's review per `/thought-digestion` (draft-only mode). APPLIED to `claims.yaml` 2026-09-22 after the user's approval (session thought-digest-mech580-apply-20260922); disposition (c) substrate_conditional retained. Kept as the record of what was proposed.

**How to use.** Read the draft below; on approval, the applying session copies it verbatim into the
claim's `what_would_answer`, sets `epistemic_category` per the disposition, and checkpoint-commits.
On edits, edit here first so the record of what was proposed survives.

Session: `thought-ingest-acwm-arousal-commit-20260922`.

## Governance flags surfaced (read first)

1. **CommitReadiness gate armed and still inert (MECH-090 substrate; measured 2026-09-18, IGW-20260918-245).**
   `use_commit_readiness_gate=True` with `_readiness` pinned to 0.0 below `commit_readiness_floor=0.05`
   produced 0 action divergences on a 150-tick CONTROL diff. MECH-042's 2026-09-22 runnability audit
   records it as "EXISTING NODE, MISSING EDGE" but no substrate_queue row names the repair. Raised as a
   governance flag by this session (see intake Next steps). Not a digestion disposition.
2. **`MECH465-COMMIT-GATE-HEADROOM` `ready:false` is stale** (its own 2026-09-22 runnability audit note:
   ARC-029 variance-tracking commit bar landed ree-v3 2026-09-18). Already recorded inside that row;
   noted here only because MECH-580's precondition P4 leans on that lever.

## Wave 1 -- MECH-580 (new this pass; the only claim registered by the intake)

**Group context.** Solo by construction (freshly registered). Read-only context members: MECH-463
(argmax-invariance of scalar affect routes), MECH-465 (WHETHER face needs boundary regime), MECH-448 /
ARC-107 (eligibility envelope, `f_eligibility_envelope_floor` a fixed global 0.30), MECH-313 (LC-NE
tonic noise floor), MECH-093 / MECH-005 (WHEN face), ARC-002 (action-conditioned E2).

**Literature bearing on the falsifier (verified this pass, intake section 4).** Eldar et al. 2013 and
Jepma & Nieuwenhuis 2011 support the breadth mechanism; de Gee et al. 2017/2020 show arousal ALSO
acts on a per-candidate bias term in brains, so the third FALSIFYING clause below (committed candidate
changes WITH score reordering) is not merely a MECH-463 re-route -- it is the REE signature of a
de Gee-type route and should be reported as such. Steinemann et al. 2018: read the evidence path
(P1's cross-candidate spread) in every arousal arm, since one control demand co-recruits both faces.
Thura & Cisek 2017 locate BG authority on WHETHER; the DV here (admitted-set size) is locus-agnostic.

**Recommended disposition: (c) substrate-blocked, `epistemic_category: substrate_conditional`,
V3-native.** The envelope, the arousal scalar (urgency / z_beta) and the sampled-commit levers all
exist, but the COUPLING (arousal -> envelope floor or dn_sigma) does not -- a small, three-site
`REEConfig` knob per `/implement-substrate` -- and the endogenous-arousal arm is degenerate until
`mech005-endogenous-arousal-dynamic-range` lands (exogenous arousal per MECH-463's protocol is the
runnable arm). `/governance` decides whether to commission the coupling build; nothing is queued here.

### Draft `what_would_answer` (MECH-580)

```
NON-DEGENERACY PRECONDITION:
(P1) Candidate futures are ACTION-DISCRIMINABLE: cross-candidate F-score spread sits above the
float32 ULP floor (the V3-EXQ-643 non-vacuity gate, as MECH-463 requires) AND E2 world-forward
pairwise divergence across the K candidates tracks their action differences (ARC-002 weak form).
Without P1 a breadth change admits or excludes nothing that differs, and the run is vacuous.
(P2) The eligibility envelope is LIVE: use_f_eligibility_demotion is ON and excluded_count varies
across ticks (not the V3-EXQ-654h admitted-all twin, excluded_count == 0).
(P3) The arousal manipulation has DYNAMIC RANGE within the run: arousal is set EXOGENOUSLY, i.i.d.
over a pre-registered decile range at each tick (MECH-463's protocol), because endogenous ||z_beta||
spans 0.91% of its mean (substrate_queue mech005-endogenous-arousal-dynamic-range) and an
endogenous-arousal arm is degenerate until that row lands.
(P4) A SAMPLED commit pick is armed (use_gap_scaled_commit_temperature or
use_precision_scaled_commit_temperature), because under a pure argmin a breadth change can only
matter on the ticks where it excludes the incumbent; the deterministic-argmin arm is reported but
is not the verdict arm.
Degenerate if any of P1-P4 fails; a null under unmet preconditions is not evidence against.

CONFIRMING: K_eligible (admitted-set size per tick) falls monotonically with arousal decile with the
bottom-versus-top gap above the pre-registered effect-size floor (scaled on the seed SD of the
delta plus an absolute floor of 2 candidates); committed-class entropy rises at low arousal and
falls at high arousal; the committed candidate's F-rank changes with arousal ONLY through
admitted-set membership -- the rank-preserving fraction within the admitted set stays ~1.0 (as
V3-EXQ-689d) and the full-K score ORDER is invariant across arousal arms (MECH-463's
argmax-invariance retained, not contradicted).

FALSIFYING: with P1-P4 met, K_eligible is flat across arousal deciles (breadth is not the route),
OR committed-class entropy does not move with K_eligible (breadth moves but does not convert to a
different committed candidate), OR the committed candidate changes with arousal WHILE the full-K
score order also changes (arousal is reordering, which refutes MECH-463's argmax-invariance instead
and re-routes to that claim rather than to this one).

Manipulation: couple the envelope to the arousal scalar with a pre-registered MONOTONE map
(f_eligibility_envelope_floor rising with arousal, and/or f_eligibility_dn_sigma narrowing), versus
a fixed-floor control at matched seeds; arousal set exogenously across deciles per P3.
Control: fixed envelope floor (stock 0.30) at every arousal decile; an arousal-OFF arm; a
deterministic-argmin arm (P4 off) reported alongside.
Required event: waking E3 selection over the K=32 CEM candidate pool with the BG eligibility
constitution ON (use_f_eligibility_demotion) on a substrate where candidate scores are
discriminable -- the GAP-A foraging substrate on which V3-EXQ-689d measured 0.371 -> 0.938.
DV: K_eligible per tick by arousal decile; committed-class entropy per decile; rank-preserving
fraction within the admitted set; full-K score-order invariance across arms; realised commit rate
(to confirm the WHETHER face did not move -- a moving commit rate is a confound to be reported,
not a result).
BOUNDARY: this claim is about the WHICH-SET face only. A result that the commit RATE moves with
arousal belongs to MECH-465; a result that E3 CADENCE moves belongs to MECH-093/MECH-005.
```

**Why substrate_conditional and not standard.** The coupling map is unbuilt (zero evidence banked
either way) -- that is the `substrate_conditional` definition, not a `substrate_ceiling` (a built,
exercised mechanism absorbed downstream). If the coupling is built and P1-P4 met and the result is a
null, the category flips to `standard` on that run.

**Cross-reference, do not re-derive.** P3 quotes `mech005-endogenous-arousal-dynamic-range`'s
finding verbatim; P1 reuses MECH-463's own non-vacuity gate; the rank-preserving-fraction readout is
V3-EXQ-689d's instrument.
