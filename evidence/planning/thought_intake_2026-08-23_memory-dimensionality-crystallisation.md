# Thought intake -- memory dimensionality crystallisation, environment-conditional target

Raw thought file: `docs/thoughts/2026-08-23_memory-dimensionality-crystallisation.md`
Date: 2026-08-23
Session: `bold-chaum-7e245c` (arose in conversation during the `/governance` cycle of
2026-08-22, out of GFLAG-0047)
Status: REGISTERED -- MECH-496, INV-101 registered in `claims.yaml`; MECH-495 amended;
EXP-0588 minted in `manual_proposals.v1.json`.

## Verbatim prompt

> and it would seem to me that there would need to be a period where the dimensionality
> and general bucket overview of the system would have to be possible to be changed with
> this diminishing perhaps to crystialise as the environment that the system finds its in
> more clearly stable? THe general ree system may need vastly different systems in
> diffewrent universes and set ups right?

## What's new vs. existing REE docs

| Element | Already in REE? | Where | Verdict |
|---|---|---|---|
| Open -> diminish -> crystallise plasticity schedule | **YES**, extensively | INV-074, MECH-333, MECH-334, ARC-076, MECH-335, MECH-484 | Not new -- but scoped **entirely to the scoring / policy plane** (behavioural diversity vs winner-take-all capture) |
| That schedule applied to **representational structure / dimensionality** | **NO** | -- | **NEW** -> MECH-496 |
| Crystallisation **target** set by the environment, not the architecture | **NO** | registry search returned 1 hit (MECH-442), unrelated | **NEW** -> INV-101 |
| Differentiation is the wrong *objective* for memory organisation | YES | MECH-495 (registered 2026-08-20) | Existing -- these claims *strengthen* it from a different direction |
| Memory bucket count as an adaptive quantity | **NO** | `ContextMemory(num_slots=16)` is a fixed constructor arg | **NEW** (substrate gap) |

## Key formulations

**1. Ill-definedness, not just mis-targeting.** MECH-495 argues differentiation is the
wrong *target*. Under variable dimensionality it is worse than wrong -- it is **not
well-defined**, because separation can always be increased by adding buckets. The
objective degenerates into "use more slots", which is a statement about capacity rather
than organisation.

**2. The metric presupposes its own outcome.** `sws_slot_diversity` computed over 16 slots
measures spread across a dimensionality that was never chosen on evidence. Relational
appropriateness survives variable dimensionality precisely because it is an *agreement*
measure against ground-truth latent structure -- indifferent to how many slots achieved
the agreement.

**3. Wrong in both directions.** A single hand-set dimensionality is over-provisioned in a
simple world (spurious **splitting**) and under-provisioned in a rich one (forced
**merging**).

**4. MECH-495's 2x2 doubles as a dimensionality detector.** Its two off-diagonal cells --
different-appearance/same-context and similar-appearance/different-context -- are exactly
the splitting and merging failures in (3). A second, independent use for a test already
designed, and the cheapest route to evidence short of building a self-sizing memory.

**5. A missing *when*.** MECH-495 says what to measure and in which cell, but not at what
developmental moment. A system whose structure is still plastic reads as poor relational
agreement on any static snapshot -- an artifact of timing, not evidence against the
objective. This became MECH-495 precondition (iv).

## Substrate state at intake

`ree-v3/ree_core/predictors/e1_deep.py:36`:

```python
class ContextMemory(nn.Module):
    def __init__(self, latent_dim, memory_dim=128, num_slots=16, ...)
```

Fixed-size `nn.Module` buffer. No growth, no allocation policy, no environment
conditioning. `sws_slot_diversity` (= 1 - slot_cosine_sim) is emitted by **29** experiment
drivers -- note the count, since GFLAG-0047's own text names 6 sleep-pass drivers, which is
the sleep-pass subset rather than the full blast radius.

## Affected existing claims

- **MECH-495** -- AMENDED. Precondition (iv) DEVELOPMENTAL TIMING appended to
  `what_would_answer`. Not a change to the claim's content.
- **MECH-334** -- named as `depends_on` for MECH-496. It currently reads
  `epistemic_category: substrate_ceiling`, `ceiling_decision: deferred`, so the full form
  of MECH-496 inherits that park. This is why EXP-0588 is scoped to need neither.
- **INV-074 / MECH-333 / ARC-076 / MECH-335 / MECH-484** -- `related_claims` only. Not
  duplicated: they are the scoring-plane statement of the same schedule.
- **SD-017 / ARC-045 / MECH-166** -- `related_claims`. The V3-EXQ-436 lineage is the
  corpus the probe re-runs, and all three are also named in GFLAG-0047.
- **INV-044** -- not wired, but worth recording: its entire experimental evidence base
  (both V3-EXQ-429 runs) was withdrawn on 2026-08-22 because its PASS gate was the raw
  whole-bank `sws_slot_diversity` and an empty 16-slot bank clears the threshold at
  P=1.0000. That was the *correctness* failure. If MECH-496/INV-101 hold, the same metric
  family is additionally **mis-targeted and ill-defined** wherever else it gates a
  criterion.

## Candidate claims -- REGISTERED

| ID | Type | Category | Summary |
|---|---|---|---|
| **MECH-496** | `mechanism_hypothesis` | `substrate_conditional` | Representational dimensionality is an outcome of a plasticity schedule, not an a-priori constant |
| **INV-101** | `invariant` / `universal` | `substrate_conditional` | The crystallisation target is environment-conditional, not an architectural constant |

Both `candidate`, `implementation_phase: v3`. Category and phase reasoning is recorded in
each claim's own `notes` and is explicitly flagged as revisable by governance:
`substrate_conditional` (not `substrate_ceiling`) because no allocation policy exists, so
nothing has ever been exercised and no evidence is banked either way; `v3` following the
phase-label-follows-dependency rule from MECH-334.

## Proposal minted

**EXP-0588** (`manual_proposals.v1.json`, `status: proposed`) -- the num_slots sweep probe.
Deliberately scoped below the claims it serves: it re-runs a slice of the V3-EXQ-436
lineage across num_slots 4/8/16/32 with matched seeds, and **cannot confirm or falsify
either claim**. It answers one prior question -- is the incumbent 16 load-bearing or inert?
A NULL result (DV flat across num_slots) is a fully informative PASS of the probe, not a
failure of the claims.

## Next steps

1. `/governance` to review the two registrations at its next cycle -- in particular the
   `implementation_phase: v3` and `substrate_conditional` calls, both flagged as revisable.
2. `/queue-experiment` for EXP-0588 when it is picked up. **It must not be widened into
   the self-sizing-memory build** -- that sits on MECH-334's deferred ceiling, and the
   probe's whole value is that it needs neither MECH-334 nor any new substrate.
3. GFLAG-0047 remains **OPEN** and is not resolved by any of this. These claims sharpen
   the fork (they add an argument for the relational-topology side, from dimensionality
   rather than from generalisation-and-linking) but do not settle it. Note the flag's own
   stated gating point has since closed: `chip-20260819-queueexp-contextmemory-writesel-validation`
   resolved `done` on 2026-08-20 and queued V3-EXQ-943, which ran, PASSed as a
   substrate-readiness diagnostic (`claim_ids: []`) and was reviewed on 2026-08-21 -- but
   its DVs were occupancy/determinism-family, which is the *precondition* MECH-495 itself
   mandates rather than a test of the objective. **The fork needs a new gating point.**
4. No lit pull owed at registration. If one is wanted, the relevant literature is
   developmental critical periods in representational (not policy) learning, and
   nonparametric / structure-learning approaches to latent-cause count.

## Honest counter-argument (carried from the raw thought)

A self-sizing memory is a large V4/V5-shaped build on top of an already-parked ceiling, and
REE has 23 parked ceiling claims. There is a real risk these two claims join that pile. The
mitigation is EXP-0588: a spike that needs no new substrate and whose null result is
decision-relevant. If the probe comes back STABLE, the honest reading is that this thought
is correct in principle and not yet load-bearing in practice -- and both claims should wait.
