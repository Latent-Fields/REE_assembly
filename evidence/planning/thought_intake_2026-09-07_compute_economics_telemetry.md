# Thought intake -- Compute as an evolving substrate: lightweight economics telemetry

**Date processed:** 2026-09-08
**Raw thought:** `docs/thoughts/2026-09-07_compute_as_an_evolving_substrate_lightweight_economics_telemetry_for_ree.md` (318 lines)
**Session:** thought-ingestion-20260908

## Outcome: NO NEW CLAIMS REGISTERED -- and that is the correct result

This is an **infrastructure/tooling proposal**, not a hypothesis about REE cognition. There is nothing
claim-shaped in it: it asserts nothing about representation, commitment, prediction, regulation or any
other object the claims registry tracks. Per the ingestion skill's own guidance, a pure tooling proposal
with nothing claim-shaped in it is a complete ingestion pass with an empty candidate-claims section, and
forcing a claim into existence to avoid that would be worse than leaving it out.

## 1. Verbatim core proposal

> The useful question is not: *How much are the models costing today?* It is: **What computational
> resources is REE consuming, what value are they producing, which of those resources could be
> substituted, and at what point does owning compute become preferable to renting it?**

And the implementation principle:

> **Measure once at the execution chokepoints; derive everything else later.**

## 2. What already exists (the extraction result)

The thought refers to "an earlier coordinator display [that] contained pricing information ...
subsequently displaced". That machinery is still live and was located this pass:

- **`REE_assembly/serve.py` ~L5334-5480** -- a ccusage-style reader that walks
  `~/.claude/projects/**/*.jsonl`, identifies the model per assistant turn, and prices it against a
  hardcoded `_CLAUDE_PRICING` table (per-1M input/output, with cache-write 1.25x/2x and cache-read 0.1x
  multipliers; unknown models default to opus tier). `_claude_price_for()` is the accessor.

**What that covers:** commercial Claude Code token spend, one workload class, derived live from
transcripts.

**What it does NOT cover, i.e. the actual gap the thought identifies:**

- no append-only ledger -- cost is recomputed from transcripts each time, so history is only as durable
  as the transcript files;
- resource quantities are not recorded independently of price, so the thought's central point (record
  GPU-hours/tokens/CPU-hours and apply a *separate* pricing table, so falling hardware prices do not
  invalidate history) is unimplemented;
- no GPU-hours, CPU-hours, peak accelerator/system memory, or storage/IO burden;
- no workload-class dimension (governance / coding / literature / experiment / training / inference /
  analysis);
- no linkage from a cost record to an experiment/run/task identifier;
- no substitutability layer at all (`local_substitutable`, `substitution_candidate`,
  `quality_constraint`, `repeatability`) -- and the thought is emphatic that **cost incurred and cost
  actually substitutable are different quantities**, since EUR 1,000 of frontier reasoning is not
  equivalent to EUR 1,000 of GPU rental if no local model can do the work acceptably;
- no queue-delay / experiment-deferred-for-cost measures, which is where the thought locates the
  *scientific* (not monetary) value of ownership;
- no ownership/crossover model, and no recognition that there are **several** crossovers rather than one.

**Related known dead-end, recorded so it is not re-attempted:** [memory]
`reference_explorer_usage_panel_plan_limit_deadend` -- plan-limit percentage is not exposed by the API.
That constrains what a usage panel can show; it does not affect the resource-ledger proposal, which is
about locally observable quantities.

## 3. Key formulations (verbatim)

- "Compute accounting should be almost entirely observational, automatically collected at existing execution chokepoints, and cheap enough that it **never becomes a reason not to run an experiment**."
- "This separates **what REE required** from **what that requirement currently costs to satisfy**."
- "The word **substitutable** is essential. The accounting system should not claim that an API call could have been local merely because a local model exists."
- "Ownership has scientific value if it converts scarce scheduled computation into an abundant laboratory instrument."
- "sunk-cost pressure encouraging experiments suited to owned hardware rather than experiments scientifically worth doing" -- listed by the thought itself as an ownership *risk*.
- "**Waiting has option value.**"
- "One day the graph may cross: **cost of thinking about the organism** versus **cost of letting the organism think.**"

## 4. Affected existing claims

None. Nothing in `claims.yaml` was read as owning or conflicting with this
(`grep -icE "compute.{0,12}(ledger|econom)|ownership crossover"` -> 0).

The thought does restate an existing Wave 4 planning finding -- that **adjudication rather than numerical
compute is presently the principal bound on scientific throughput** -- as motivation. That finding is
already recorded in the Wave 4 planning material and is not re-registered here.

## 5. Candidate claims -- REGISTERED this pass

**None.** See the outcome statement above.

If any part of this ever becomes claim-shaped, the likeliest candidate is not the ledger but the
*prediction* the ledger would test: that REE's computational centre of gravity migrates from "machines
thinking about REE" to "machines running REE" over development. That is currently a project-trajectory
expectation rather than an assertion about the organism, and it would be premature to register it before
the ledger exists to measure it.

## 6. Next steps

1. **Implementation is chipped, not queued** -- this is engineering work, not experiment work, so it
   does not touch `experiment_queue.json`.
2. **Build order follows the thought's own principle:** instrument the existing chokepoints (experiment
   manifests already carry run identity and elapsed time; cloud runners know machine type and duration;
   the serve.py reader already knows model identity and token counts) and emit append-only records.
   Do **not** create a per-experiment form.
3. **Keep pricing out of the ledger.** Resource quantities in the records; a separate pricing/config
   file applied at analysis time. This is the single design decision most likely to be lost in
   implementation and most expensive to retrofit.
4. **Substitutability must be measured, not asserted.** The thought proposes occasional "compute
   substitution assays" -- can this class of coordinator task be done by a smaller model without
   materially degrading the result? Until such an assay runs, `local_substitutable` should stay
   `unknown` rather than being guessed.
5. **No purchase decision is implied or recommended by this pass.** The thought explicitly declines to
   select hardware and proposes a conservative multi-condition trigger instead.
