# The ARC-004 bridge premise propagates: MECH-520 and MECH-522 both rest on "depth IS timescale"

**Date:** 2026-08-28 · **Session:** `elated-nobel-914234` (continuation of `insights-7fd98a`)
**Status:** FINDING -- registry + source inspection. Nothing registered, no claim status changed, no substrate change.
**Upstream:** [`arc004_wiring_topology_probe_20260828.md`](arc004_wiring_topology_probe_20260828.md) (GFLAG-0088, GFLAG-0089).
**Concerns:** MECH-520, MECH-522, MECH-521, ARC-134 -- all `candidate`, all `v4`, all `v3_pending`. **Nothing is broken now**; what is broken is a *precondition* each of them will need when it is built.

---

## 1. The bridge

Sections 9.4 and 10.7 of the originating synthesis argue for ephaptic coupling
*specifically* -- rather than any generic gate -- with this step:

> a neuromodulatory scalar must be TOLD which level to act on -- the depth index
> is external to the signal -- whereas a field has a coherence LENGTH and a
> characteristic FREQUENCY, and **in a system where depth is timescale
> (ARC-004)** both are natively scale-indexed.

That sentence is registered verbatim in **MECH-522**'s `what_would_answer`. The
same bridge appears in **MECH-520**'s title: *"Requiring the higher-order latents
to remain PREDICTIVE across the **ARC-004 temporal spread**"*, and again in its
notes as *"a predictive obligation **across timescales**"*.

The upstream finding is that as built there is no temporal spread: the
beta/theta/delta cascade is within-tick and the only temporal operator is three
**parallel** EMAs sharing one hardcoded constant, unchanged since ree-v3's first
commit. Measured on the real stack, 10 seeds: `mean(delta - beta) = +0.102`
against a `0.8*SD` bar of `0.354`, monotone ordering on 4 of 10 seeds.

## 2. What that does to each claim

**MECH-520 -- the whole mechanism.** Its content is that a predictive obligation
*across horizons* supplies a constraint a pure value objective lacks:
"cross-horizon prediction demands retained state structure that value alone does
not". As built the three depths span no horizons, so the obligation would be the
same obligation three times and could not supply differential structure. This is
not a small-print issue: cross-horizon spread is the entire source of the
anti-collapse constraint. MECH-520 is not *refuted* -- it is **not
implementable in V3 as formulated**, which is a different and more repairable
thing.

**MECH-522 -- one of its two legs.** The claim offers two field properties:
coherence **length** (spatial extent) and characteristic **frequency** (depth
index). The frequency leg is the one that runs through ARC-004 and is currently
void; the **coherence-length leg is untouched** and does not depend on
depth-is-timescale at all. So MECH-522 loses half of its why-ephaptic-specifically
argument rather than all of it -- and the surviving half is the one that speaks
to MECH-521's coupling-constant role, which is MECH-522's actual subject.

**Registry hygiene:** MECH-522's argument names ARC-004 explicitly and its
`depends_on` is `[MECH-521, MECH-228, MECH-270, MECH-499, MECH-500, MECH-456,
ARC-134]` -- **ARC-004 is not declared**. An undeclared dependency of exactly the
kind that makes this propagation invisible to any dependency walk.

**What is NOT affected: the cheap path stays open.** The synthesis's S9.9d
ordering -- state the perceptual analogue of ARC-069 (done: ARC-134), then probe
whether arbitrating MECH-288's already-two-scale segmenter changes anything, and
only then ask whether field coherence is the right arbiter -- uses no frequency
bridge anywhere. It is unaffected and remains the non-exotic first move.

## 3. The consequence for ordering, which is the useful part

The serial-smoothing build identified upstream was justified there as "the
minimum that makes ARC-004 testable". It is worth more than that: it is a
**shared prerequisite for two v4 claims' preconditions**. One small, flag-gated,
bit-identical-when-OFF substrate item in `LatentStack.encode` restores the
temporal spread that MECH-520's mechanism needs and that MECH-522's frequency
leg indexes. That materially raises its value, and it is the kind of dependency
that is easy to miss because both consumers are `v4` and neither is blocked
today.

Stated in the debt vocabulary: MECH-520 and MECH-522's frequency leg are not
`complex (probe-gated)` on the ephaptic science -- they are
`complicated (buildable)` behind one V3 substrate item, and only *then*
probe-gated.

## 4. Separately: MECH-521's "third ingredient" -- right form, wrong population

The MECH-521 derivational toy
([`mech521_settling_signature_derivation_20260826.md`](mech521_settling_signature_derivation_20260826.md))
established that "graceful then discrete" needs a **shared budget** (divisive
normalisation) as a third ingredient, and noted the good news that this "is
already in REE -- divisive normalisation is exactly MECH-448's
eligibility-envelope form".

**Checked in source. The form is right; the wiring is not.**

- **MECH-448 is a genuine divisive normalisation, implemented and validated.**
  `ree_core/predictors/e3_selector.py:1576` --
  `merit[i] = clamp(max(F) - F[i], 0)`, `pooled = sigma + merit.sum()`,
  `elig[i] = merit[i] / pooled`. A shared pooled denominator across the competing
  field, exactly the shape the toy needs. Its docstring also already carries two
  traps a re-instantiation would otherwise rediscover: a fraction-of-max floor
  cancels the pooled term and degenerates to the margin shortlist, and a fixed
  absolute floor mis-fires per channel (654h all-admit no-op, 485i bespoke
  per-seed floor) which is why the adaptive mean-relative floor exists.
- **But it acts over E3 action CANDIDATES**, not perceptual slots.
- A second shared-budget normalisation exists over a slot bank --
  `ree_core/amygdala/attribution_head.py:314`, `torch.softmax(scores, dim=-1)`
  over `n_slots` -- but those are `ContextMemory` slots (MECH-166, offline
  context) read for harm attribution, not an online perceptual occupancy.
- **Nothing normalises over an online perceptual slot population, because that
  population does not exist.** ARC-134 says so in its own text: REE "has made
  this commitment for policy (ARC-069/070/071) and for context slots offline
  (MECH-166) but **never for online perception, where the unit remains fixed**."

So the correction is narrow and useful in both directions. The toy's third
ingredient does not have to be invented -- there are two working reference
implementations in-tree, one of which has already paid for its own failure modes.
What is missing is the **population** it would act on, and that gap is already
owned by ARC-134 rather than being new. MECH-521's `depends_on` already lists
ARC-134, so the registry ordering is correct; what was inaccurate was only the
"already in REE" framing, which reads as less work than it is.

## 5. Limits

- Registry-and-source inspection only. No measurement here beyond the upstream
  probe, and no claim status changed.
- The reading of MECH-520 as "not implementable as formulated" is an argument
  from its stated mechanism, not a run. If governance reads its cross-horizon
  language as aspirational rather than load-bearing, the conclusion weakens
  accordingly -- but then the claim needs re-wording either way.
- MECH-522's two legs are separated here on the basis of its registered text.
  Whether its author intends them as jointly or severally sufficient is a
  question for the claim owner.
- Whether a perceptual slot population *should* exist online is ARC-134's
  question and is deliberately not argued here.
