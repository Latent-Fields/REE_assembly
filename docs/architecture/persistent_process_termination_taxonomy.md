---
title: "Persistent-Process Termination Taxonomy"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 25
status: candidate
status_asof: 2026-08-25
status_claim: ARC-128
---

# Persistent-Process Termination Taxonomy

**Claim IDs:** ARC-128 (generality), MECH-497 (self-referential stopping failure), MECH-498 (progress-gated disengagement)
**Origin:** thought-intake [thought_intake_2026-08-12_persistence_must_earn_continuation.md](../../evidence/planning/thought_intake_2026-08-12_persistence_must_earn_continuation.md), from raw thought `docs/thoughts/2026-08-12_persistence_must_earn_continuation.md`
**Status:** candidate / substrate_conditional / implementation_phase v4. Promote/demote-suppressed. Not a V3 build target.

> This is a **control-plane compass doc**, not a V3 implementation target. All three claims
> registered here are `substrate_conditional` / `implementation_phase: v4` -- they generalize
> and extend already-built V3 machinery (SD-034, MECH-343/SD-061, MECH-080, MECH-434) rather
> than proposing new V3 substrate. Do not build a general termination-taxonomy substrate or
> queue a V3 experiment from this doc without an explicit version-routing decision.

---

## 1. What already exists (do not duplicate)

REE already has a working instance of "turn evaluation off on success," built specifically for
committed `rule_state`:

- **SD-034 (IMPLEMENTED 2026-04-20)** -- the governance `ClosureOperator`: on rule completion,
  emits a five-part "done" token (beta release via MECH-090, No-Go injection via MECH-260,
  residue discharge, salience re-bias, dACC PE reset). Born from the same root the new thought
  reaches independently: per `sd_034_governance_closure_operator.md`, "The 2026-04-20 GAP MEMO
  and the OCD thought set identify this as the load-bearing missing piece in the governance
  layer."
- **MECH-343 / SD-061 (difficulty-gated proposal entropy)** -- the *opposite-direction* response
  to a stalled process: when goal progress stalls but goal salience is preserved, REE should
  widen proposal-generation entropy (more candidates, higher sampling temperature) rather than
  give up.
- **MECH-080** -- rollout-truncation set-points as a psychiatric individual-differences
  substrate; explicitly names OCD as abnormally deep BG/ACh attractor lock-in.
- **MECH-434 (epistemic commitment timing)** -- WHEN to stop gathering evidence and commit,
  balancing pragmatic vs. epistemic value, inverted-U between epistemic-freezing and
  anti-epistemic-panic. This is close to the thought's sections 2/3/7/20 ("sure enough must be
  dynamic") but scoped to the inference layer's evidence-gathering decision specifically.
- **Q-080** -- the effort-dissociation environment (Charnov MVT / optimal foraging), already
  built (landed 2026-07-09); the substrate a marginal-value-style continuation rule would test
  against, if/when this cluster is routed to V3.

None of the above is re-asserted below. The claims here name the gap that remains once all four
are accounted for.

## 2. The gap: three distinct novel threads

### 2a. Generality (ARC-128)

SD-034's closure token is a *single instance*, wired specifically to committed `rule_state` via
the BetaGate/dACC pair. The thought's claim is that the same structural requirement --
terminate, and record *why* -- recurs across every other persistent-process family REE already
has an activation/drive for (information-seeking, planning, memory retrieval, threat
monitoring, exploration, ethical counterfactual generation), and that REE currently has no
shared taxonomy for those terminations beyond the rule_state-specific instance. The taxonomy
proposed (completion / satiety / closure / disengagement / suspension / switching /
interruption / reopening) is richer than SD-034's binary "done token fires or it doesn't": SD-034
covers *completion* and *closure*; it does not by itself distinguish *suspension* (resumable)
from *disengagement* (abandoned) from *interruption* (externally invalidated), and preserving
that distinction is exactly what the archival-ethics thought
(`2026-08-14_preserving_the_possibility_of_future_reconstruction.md`) later assumes when it
asks that "termination should preserve **why** termination occurred."

### 2b. Self-referential stopping failure (MECH-497)

A distinct failure mechanism from MECH-080's attractor-lock-in account of OCD: a persistent
process can degrade the very confidence/evidence variable that gates its own stopping condition
-- the repeated-checking literature's finding that repeated verification reduces subjective
recollective confidence while leaving objective accuracy largely intact. This is a
self-referential-measurement failure (the act of checking corrupts the stopping signal), not a
BG/ACh gate-dynamics failure (MECH-080's deep locked rollout basin). The two may co-occur in a
real OCD-like failure but are mechanistically separate, and a substrate fix for one would not by
itself fix the other.

### 2c. Progress-gated disengagement (MECH-498)

The disengagement-direction complement to MECH-343/SD-061. MECH-343 widens the candidate search
when a goal-directed process stalls (with goal salience preserved) -- it is a "try harder"
response. Nothing in the current registry covers the case where widening *also* fails to
restore progress: this claim proposes that continuation of any persistent process should be
gated jointly on marginal expected return relative to alternatives (MVT framing, cf. Q-080) and
on the *observed rate* of progress -- not only the current absolute uncertainty/value level --
so that a process whose marginal progress has collapsed increasingly loses justification for
further resource allocation even while absolute uncertainty remains high.

## 3. Explicitly out of scope here

- The multi-agent strategic-cost-of-delay thread (thought section 6: another mind can make
  waiting costly independent of information value) is flagged in the intake as needing a closer
  check against REE's existing multi-agent/adversarial-evidence claims before it can be judged
  genuinely new; it is not registered as its own claim in this pass.
- The sleep/termination-behaviour speculation (thought section 17) is explicitly hypothesis-
  generating on a single anecdotal Fishtank observation and is not claim-worthy yet.

## 4. Literature to mine before any of this hardens

Per the raw thought: biological satiation/meal-termination circuitry, optimal foraging /
Marginal Value Theorem, bounded rationality and satisficing, rational metareasoning, evidence
accumulation / speed-accuracy trade-offs / collapsing bounds, basal-ganglia commitment threshold
and veto mechanisms, ACC control allocation and persistence/switching, goal disengagement and
re-engagement, hierarchical-RL options/termination functions, multi-agent decision timing, and
the OCD repeated-checking/confidence literature specifically (distinct from the attractor-
lock-in literature already used for MECH-080).
