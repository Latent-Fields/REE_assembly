# Thought-digestion drafts: harm-to-threat causal credit (MECH-598, MECH-599, Q-113)

**Date:** 2026-09-26
**Session:** thought-ingest-harm-to-threat-20260926 (interactive; the user reviews before anything is applied)
**Source intake:** `thought_intake_2026-09-26_harm_to_threat_causal_attention_and_credit.md` section 10
**Mode:** grouped. The three claims form one group: same `source_thought`, and `MECH-599 depends_on MECH-598`,
with Q-113 relating to both. The drafts were written by the orchestrating session, which ran the overlap audit
itself, rather than by a dispatched agent.

## Group preamble

- **Shared precondition.** All three need the same non-degeneracy precondition: `z_world` must carry
  **discriminable identity for two co-present candidate cues**. MECH-074d already failed on that property
  (V3-EXQ-894/894a/894b/894c, blocked on MECH-153). Q-113 holds the canonical wording (P1 below).
  MECH-598 and MECH-599 point to it instead of re-deriving it.
- **Ordering.** Q-113 is the gate. MECH-598 and MECH-599 are only worth building if Q-113 comes back with
  answer (3) "new mechanism". Answers (1), (2) and (4) each make them unnecessary for V3.
- **Merges or contradictions:** none. MECH-599 is the threat-side mirror of MECH-304. The two are sisters and
  do not duplicate each other.
- **Near-term consequence for the campaign.** V3-EXQ-1109 ran 2026-09-26T16:19Z and returned FAIL
  (diagnostic). F0 was INDETERMINATE: `z_harm_a` hazard-distance R^2 was 0.139 against encoder fidelity
  0.992, and freeze was active in 100% of ticks. The run is not yet autopsied, and it is not yet in
  `review_tracker.json`. The coupled-loop campaign parks the MECH-280 LH-PAG override build until 1109
  "resolves the freeze input". The SEMANTIC half of that question (injury is not threat) is already owned
  by SD-011 / SD-020 / MECH-258. The near-term re-wire (feed freeze from `z_harm_s` proximity or E3
  predicted harm instead of raw `z_harm_a`) needs NONE of the three claims below. Adjudicating that is
  `/failure-autopsy` work on 1109, not digestion.

## Recommended dispositions

| Claim | Disposition | Category | Proposal |
|---|---|---|---|
| Q-113 | (c) substrate-blocked | `substrate_conditional` (unchanged) | none. Its first step is a representation probe, owed after MECH-153 / the `z_world` differentiation work |
| MECH-598 | (c) substrate-blocked | `substrate_conditional` (unchanged) | none |
| MECH-599 | (c) substrate-blocked | `substrate_conditional` (unchanged) | none |

## Q-113 draft `what_would_answer`

```
DIGESTED 2026-09-26 (thought-ingest-harm-to-threat-20260926). DISPOSITION: (c) substrate-blocked,
substrate_conditional -- the environment needs a two-cue harm contingency that CausalGridWorld does not have
(SD-065 added a Pavlovian SAFETY CS channel; there is no threat-CS twin), and source-specific credit is
presumptively gated on z_world cue identity (MECH-153). First step is a probe, not an experiment.

NON-DEGENERACY PRECONDITIONS (a null under any unmet one is not evidence for any of the four answers):
  P1. CUE IDENTITY IN z_world (the shared precondition MECH-598 / MECH-599 point at). Two co-present
      candidate cues A (harm-predictive) and B (neutral) must be linearly decodable from frozen z_world
      on held-out ticks above a pre-registered bar (balanced accuracy >= 0.80, and above an
      untrained-projection control of the same input, cf. V3-EXQ-1002). If P1 fails the answer is (4)
      REPRESENTATION-GATED and the run stops there.
  P2. A GENUINE CONTINGENCY WITH HEADROOM. Only A causes damage; B co-occurs with A on a pre-registered
      fraction of harm events AND appears alone without harm; a pre-contact avoidance action is available
      so anticipatory avoidance is measurable; no hazard identity or proximity oracle reaches the agent.
  P3. A LIVE ADVERSE EVENT. The trigger is a phasic event (z_harm_s onset / harm-PE / negative delta in
      valued self-state), counted per event; persistent ||z_harm_a|| magnitude does not count (V3-EXQ-1109).
  P4. EDGE TRACE RECORDED. For each edge (adverse event -> orienting -> candidate eligibility/attribution
      -> durable write -> prospective prediction -> pre-harm behaviour) the run records producer,
      consumer, default flag state, and whether the edge fired, so a null names its failing edge.

MANIPULATION: the existing stack with SD-099 (DefensiveOrientingGate) and MECH-074d (BLAAttributionHead)
ON versus OFF, crossed with an injury-vs-threat consumer arm (freeze/orienting release reading z_harm_s or
E3 predicted harm instead of raw z_harm_a). Matched seeds (>= 5), identical contingency schedule.
Controls: B-only exposure; contingency reversal phase (A becomes safe, B harmful).

DV: (i) pre-contact avoidance of A vs B (source specificity = avoid(A) - avoid(B)), measured on trials
BEFORE any new damage in that trial; (ii) predicted harm from E3 / residue at first sight of A vs B;
(iii) reversal: trials-to-criterion after the swap; (iv) per-edge firing from P4.

ANSWER MAPPING:
  (1) INTEGRATION -- every edge fires in isolation (P4) but specificity > 0 only when SD-099 and MECH-074d
      are both ON and wired to a prospective consumer.
  (2) SEMANTIC SPLIT -- specificity and reversal appear ONLY in the injury-vs-threat consumer arm.
  (3) NEW MECHANISM -- P1-P3 green, all edges fire, and specificity stays ~0 in every arm (A and B are
      credited alike, or neither becomes a pre-harm predictor): the stack lacks selective credit ->
      MECH-598 / MECH-599 become the build candidates.
  (4) REPRESENTATION-GATED -- P1 fails.
FALSIFYING the premise of the question: the unmodified current stack (flags at defaults) already shows
specificity > 0 on >= 4/5 seeds and reverses; then Q-113 closes "already closed" and MECH-598 / MECH-599
lose their V3 motivation.
```

## MECH-598 draft `what_would_answer`

```
DIGESTED 2026-09-26 (thought-ingest-harm-to-threat-20260926). DISPOSITION: (c) substrate-blocked,
substrate_conditional -- no per-candidate associability state exists in ree_core. Build is gated on Q-113
returning answer (3); do not build before.

NON-DEGENERACY PRECONDITIONS: Q-113's P1 (cue identity in z_world), P2 (A/B contingency with headroom)
and P3 (phasic adverse event, not persistent z_harm_a) -- see Q-113's own what_would_answer, do not
re-derive. Additionally:
  P5. MATCHED TOTAL GAIN. The broadcast-control arm applies the SAME summed learning-rate increase per
      adverse event as the selective arm, spread uniformly over all codes in the eligibility window
      (the MECH-074a / MECH-398 analogue). Without this match any advantage is "learn harder", not
      "learn about the cause".
  P6. ASSOCIABILITY IS LIVE. The per-candidate associability trace must vary across candidates (logged
      per event); a flat trace makes the selective arm identical to the broadcast arm.

CONFIRMING (>= 4/5 fresh seeds, matched schedule): the selective-associability arm beats the matched
broadcast arm on (i) source specificity avoid(A) - avoid(B) before damage, reached in fewer harmful
encounters, AND (ii) reversal: after the A/B swap, associability for B rises and B acquires threat value
faster than in the broadcast arm (the Pearce-Hall signature -- surprise re-opens learning about the cue).
The immediate nocifensive response to actual damage is the same across arms (sparing check).

FALSIFYING (any one, with P1-P6 green):
  - the broadcast arm matches the selective arm on specificity AND sample efficiency;
  - the selective arm is not faster at reversal than an arm with associability frozen at its
    pre-reversal values (no persistent associability effect -- only a one-shot boost, which is MECH-431 /
    MECH-074b territory);
  - the selective arm over-generalises (avoid(B) rises with avoid(A)).
If specificity is achieved but reversal is not faster, NARROW the claim to a retrospective selective
boost and drop the persistent-associability half.
```

## MECH-599 draft `what_would_answer`

```
DIGESTED 2026-09-26 (thought-ingest-harm-to-threat-20260926). DISPOSITION: (c) substrate-blocked,
substrate_conditional -- no ConditionedThreat store and no threat-CS environment channel exist. Build is
gated on Q-113 returning answer (2) or (3); the natural V3 build is a mirror of SD-051
(ConditionedSafetyStore) plus an SD-065-style threat-CS channel.

NON-DEGENERACY PRECONDITIONS: Q-113's P1-P3 (see its what_would_answer, do not re-derive). Additionally:
  P7. INJURY AND THREAT DISSOCIABLE IN THE SCHEDULE. The run includes a threat-removed-but-injured phase:
      damage is delivered, then cue A is removed while z_harm_a stays elevated, plus a cue-A-present,
      uninjured phase. Without both cells the store's output and accumulated injury are confounded.
  P8. STORE LIVE. The store's prototype for A is written (non-zero) and its match score at A differs from
      its match score at B before the scoring window.

CONFIRMING (>= 4/5 fresh seeds): with the store ON and defensive consumers reading its output:
  (i) on the uninjured cue-A-present cell, freeze/withdraw probability and E3 predicted harm rise BEFORE
      any new damage, and do not rise at B;
  (ii) on the threat-removed-but-injured cell, acute freeze/escape falls toward baseline while z_harm_a
      stays high -- the consumer tracks predicted threat, not injury;
  (iii) extinction: repeated A-without-harm lowers the store's match-driven threat output. A MECH-304-style
      safety cue presented with A additionally releases the avoidance commitment, which checks that the
      sister systems interoperate.
Store-OFF arm (consumers on raw z_harm_a, current MECH-279 wiring) is the control.

FALSIFYING (any one, P1-P3 / P7-P8 green):
  - the store-OFF arm already shows (i) and (ii) at matched seeds (the existing contextual route --
    residue / E3 harm_eval -- suffices, so the cue-specific store is redundant in V3);
  - store ON fails (i) (the store learns but does not reach behaviour: a consumption failure, which
    re-routes to the consumer contract rather than the store);
  - store ON shows (i) at B as strongly as at A (no cue specificity).
```
