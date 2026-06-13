# Sleep-dependent memory triage: the offline write-weight the store must honour

**Stickgold & Walker (2013), *Nature Neuroscience* 16(2):139-145. [DOI](https://doi.org/10.1038/nn.3303)** (PMID 23354387).
Claims grounded: **MECH-361** (offline write-weight), **MECH-252 / MECH-253** (sleep cross-link). Direction: **mixed**. *According to PubMed.*

## What the paper does

Stickgold and Walker's thesis is that the sleeping brain is not a passive archive. It performs **memory triage**: most of what is encoded in a day is forgotten, and of what is retained, the brain *chooses among operations* — integrate the memory into existing networks, distil overarching rules from it (generalisation), or simply stabilise it verbatim. The decisive framing for REE is that retention and the choice of operation are **selective and tagged** — biased by signals of future relevance, emotional salience, and explicit instruction. Sleep "knows which information to preserve" because that information was flagged as mattering.

## Why it grounds the cluster

This is the cross-link the ABM-9 readiness gate names ("SWS/REM content-vs-weights split, co-constitutive of honest replay-based learning"). Two grounding roles:

- **MECH-361 (offline write-weight).** MECH-361 says affect is a write-weight: high-gradient episodes are preferentially written. Stickgold and Walker supply the offline half of that — consolidation is *selective and salience-biased*, not uniform. What survives the night is what was tagged as relevant or emotionally significant. That is "affect/salience scales durable write" at the systems-consolidation timescale, complementing the McGaugh BLA mechanism at the cellular timescale.
- **MECH-252 / MECH-253 (distinct consolidation operations).** The review establishes that consolidation is not one thing — integration vs rule-distillation vs verbatim stabilisation are genuinely different operations applied to retained memories. MECH-252 (SWS consolidates goal-value content) and MECH-253 (REM consolidates template-performance into projection *weights*) presuppose exactly this: that the store undergoes *different* offline write operations, and the unified ARC-085 store must honour them rather than treating replay as uniform.

## Where the mapping strains (why `mixed`, not `supports`)

The honest gap is specificity. Stickgold and Walker argue for selective, operation-differentiated, salience-biased consolidation *in general*. They do **not** deliver MECH-252/253's particular dissociation — that **SWS** consolidates *stored content* while **REM** consolidates *projection weights*. That is a stage-specific *and* target-specific claim (which sleep stage, acting on which kind of representation), and this review does not pin operations to stages that cleanly, nor introduce a content-vs-weights axis at all. So it grounds the *premise* MECH-252/253 share (consolidation is plural and operation-typed) while leaving their *specific split* still owed direct, stage-resolved evidence. For MECH-361 the limit is parallel: "salience biases what is retained" is supported; "a graded affective *gradient* is the quantitative write-weight" is not — the mechanism that sets and reads the retention tag is left open.

That is why both the direction is `mixed` and the claim set is tagged conservatively to the premise-level claims (MECH-361, MECH-252, MECH-253) rather than asserting the dissociation is evidenced. The finer SWS-content/REM-weights test belongs to the sleep_substrate track, and a future stage-resolved pull (or a V4 experiment) is what would actually discriminate MECH-252 from MECH-253.

## Confidence

0.62, `mixed`. High source quality. The binding constraint is mapping fidelity: a real, directionally-clear grounding of the *shared premise* (selective, operation-differentiated, salience-weighted offline consolidation) and underdetermination of the *specific stage/target split*. Raises literature_confidence on the cross-link claims only; promotes nothing.
