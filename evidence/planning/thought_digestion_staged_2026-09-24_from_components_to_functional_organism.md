# Thought-digestion staging -- 2026-09-24 -- from components that work to an organism that works

**What this is.** Draft `what_would_answer` text and a disposition produced in the SAME session as the
Stage 2 intake `evidence/planning/thought_intake_2026-09-24_from_components_to_functional_organism.md`.
It is staged here for review per `/thought-digestion` (draft-only mode). **Nothing here is applied.**
The one claim it digests (provisional MECH-586) is itself STAGED, not registered, because
`governance-20260924-workset` owns `claims.yaml` (intake header).

**How to use.** The session that registers MECH-586:
1. Copies the draft below verbatim into the claim's `what_would_answer`.
2. Keeps `epistemic_category: substrate_conditional`.
3. Checkpoint-commits.

To change the draft, edit it here first so the record of what was proposed survives.

Session: `thought-organism-path-20260924`.

## Governance flags surfaced (read first)

1. **GFLAG-0447 (raised by this session, REE_assembly `bc7edc2465`).** The ready build
   `sd032b-candidate-effort-proxy` (IGW-222, user-HELD until the 2026-09-25T18:00Z re-raise) names a
   harm-forward rollout cost as its effort producer. That double-counts harm (MECH-354), pre-empts
   Q-080, and depends on a harm-forward head that loses to persistence in 6/6 cells (V3-EXQ-1062a).
   This is a design gate, not a digestion disposition.
2. **GFLAG-0437 (pre-existing, from the V3-EXQ-1081 draft autopsy).** SD-PP-B1's "no native route to
   E3" premise is false. Not a digestion disposition.
3. **CURRENT_FRONT source text trails the confirmed 2026-09-23 re-pose.** It still says V3-EXQ-1010 is
   "queued and running" and that the re-pose is routed "until it happens". The fix belongs in the source,
   followed by a regen. Listed in the intake's Next steps.

## Wave 1 -- MECH-586 (provisional id; the only claim the intake recommends)

**Group context.** Solo. Read-only context members:
- **ARC-052:** half (A) E3 weighting by exp(-log_sigma) is unbuilt; half (B) precision estimation passed on V3-EXQ-977.
- **MECH-485:** magnitude + confidence fan out to three consumers; low confidence routes to orient/survey.
- **MECH-510:** prediction vs error precision.
- **MECH-454:** own-option preservation, not harm.
- **MECH-388:** information-gathering pressure.
- **Q-027:** irreversibility under uncertainty.
- **SD-PP-B11:** harm-reliability module, registration-only.

**Draft `what_would_answer`:**

```
NON-DEGENERACY PRECONDITIONS (a null under any unmet one is uninterpretable, not evidence against):
  P1. A harm-forward forecast exists that beats persistence on held-out opportunities (skill > 0 vs
      the persistence baseline, the gate V3-EXQ-1062a introduced). V3-EXQ-1062a found 6/6 cells
      WORSE than persistence and V3-EXQ-1077 returned cannot_determine -- P1 is currently UNMET.
  P2. A per-candidate or per-stream confidence for that forecast varies across opportunities above a
      permutation null (ARC-052 half B's V3-EXQ-977 standard), AND is not merely a relabelled harm
      LEVEL (decorrelated from z_harm_a magnitude -- the SD-PP-B9 registered null).
  P3. Hazard forecasts in the test world are genuinely uncertain in a way the organism can reduce by
      acting (investigate / wait / sample), and avoidable harm is a scored outcome.

CONFIRMING: At matched reward, matched exposure and matched training budget, an arm that routes low
harm-forecast confidence to redirect consumers (MECH-485 orient/survey, shortened trusted horizon,
alternative preservation) while leaving the expected-harm COST weight in E3 ranking undiscounted
incurs LESS realised avoidable harm than an arm that discounts expected harm by the same confidence
(ARC-052 half-A form, exp(-log_sigma) on the cost term), and the difference disappears when the
forecast is made uninformative (mismatched-content control). Autonomous closed-loop evaluation (each
arm executes its own choices, GOV-JURIS-1 D3), not a yoked trace.

FALSIFYING: With P1-P3 met, discount-by-confidence produces no more realised avoidable harm than
redirect-without-discount, OR the redirect arm's harm advantage is bought entirely by starving reward
(no harm benefit at matched reward). Either outcome says the asymmetry is unnecessary and ARC-052's
half-A form is safe as written.

SUBSTRATE / INSTRUMENT REQUIREMENT: Neither harm encoder emits (mu, log_sigma) (ARC-052 disposition
note), E3 has only the single ARC-016 running-variance precision term, and MECH-485's three-consumer
fan-out is substrate_conditional. There is no producer and no consumer today.
```

**Recommended disposition: (c) substrate-blocked, `epistemic_category: substrate_conditional`.**
Two things are missing: a better-than-persistence harm forecast (P1, UNMET) and a per-stream harm
confidence that reaches E3. The claim has **design value NOW** and should not wait for testability. It
is the boundary that must be read BEFORE ARC-052's half A or SD-PP-B11 is built. `/governance` decides:
- V3 vs V4 routing;
- whether to also write the asymmetry as a boundary note directly on ARC-052 and SD-PP-B11.

**Do NOT queue an experiment. Do NOT build.**

## Not digested this pass (by design)

The thought's other threads (intake section 5, T1-T4 and T6-T10) are owned by existing claims. A
digestion pass over them would re-litigate settled `what_would_answer` text without new evidence. The
evidence that bears on them arrives through `/governance` confirming the six 2026-09-24 draft
autopsies, and that belongs to `/governance`, not to digestion.
