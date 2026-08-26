# MECH-521 derivational probe: is "graceful then discrete" actually derivable?

**Date:** 2026-08-26 · **Session:** `insights-7fd98a` · **Status:** FINDING -- desk derivation, no REE substrate touched, nothing registered.
**Owed by:** MECH-521's `what_would_answer`, which names this as the DERIVATIONAL PRECONDITION
owed *before* any substrate work: "the discriminating signature is ASSERTED, NOT DERIVED.
Pattern formation gives domain COUNT and SIZE as functions of the control parameter; the
mapping from domain size to per-item representational FIDELITY is unargued."
**Probe:** `mech521_settling_derivation_probe.py`, `_v2.py`, `_v3.py` (session scratch; 1-D ring,
N=240, Mexican-hat kernel, no REE imports).

---

## Verdict: the signature is **NOT** derivable from coupling-vs-lateral-inhibition alone. It requires a THIRD ingredient MECH-521 does not name -- a SHARED BUDGET.

MECH-521 predicts, as the thing that makes it a "third answer" to Q-077's slot-vs-resource
fork: *capacity degrades gracefully (resource-like) up to a point and then loses a whole
domain (slot-like).* Both halves must co-occur, or it is not a hybrid and adds nothing to
either horn.

**What settling alone gives (no shared budget):**

| M items | peaks | retain% | pos_err | peak amplitude |
|---|---|---|---|---|
| 2 | 1.8 | 88% | 0.75 | **1.000** |
| 8 | 5.0 | 62% | 3.30 | **1.000** |
| 16 | 6.2 | 39% | 2.89 | **1.000** |
| 28 | 6.8 | 24% | 6.68 | **1.000** |

Capacity is real -- peak count saturates (~6-7) and the saturation point **moves with the
coupling/inhibition ratio** (measured in v2: strong-inhibition caps ~8, mid ~12, weak ~14-18).
**MECH-521's leg 2 -- that capacity and occupancy are distinct regulators -- is DERIVED.**

But per-item fidelity is **pinned at 1.000 at every load**. There is no graceful phase at all.
v2, run without jitter, made this starker still: positional error stayed at *exactly* 0.00 up
to capacity and then jumped to 8-13 in one step. **Settling alone yields "perfect until a
cliff" -- the pure SLOT horn, not a hybrid.**

**Why, and it is obvious once seen:** nothing is shared. Each item gets its own input bump of
equal amplitude, so there is no quantity for additional items to dilute. A graceful phase is
not merely absent, it is *structurally impossible* in that model.

**What a shared budget adds (divisive normalisation, fixed total drive):**

| M items | peaks | peak amplitude |
|---|---|---|
| 2 | 1.8 | 0.996 |
| 4 | 3.5 | 0.945 |
| 8 | 4.5 | 0.881 |
| 12 | 4.2 | 0.879 |
| 16 | 5.2 | 0.811 |
| 20 | 6.0 | 0.758 |
| 28 | 6.2 | **0.719** |

Now fidelity declines **smoothly and monotonically** (0.996 -> 0.719) while peak count still
saturates (~6) and retention still drops discretely. **Both halves of the signature co-occur --
but only with the shared budget switched on.**

## What this changes for MECH-521

1. **The claim as registered is under-specified.** It attributes the signature to "a
   coupling-versus-lateral-inhibition settling competition, bounded above by an independently-set
   CAPACITY". That is two ingredients; the derivation needs **three**. Without the third the
   claim predicts the slot horn, which Q-077 already contains, and the "third answer" framing
   collapses.
2. **The missing ingredient is nameable and already in REE.** Divisive normalisation is exactly
   the form MECH-448's rank-preserving F->eligibility envelope uses, and `_loop_normalize`
   (`e3_selector.py`) is a live normalisation site. So this is a concrete substrate hook, not a
   new import -- which makes the amendment cheap rather than damaging.
3. **It sharpens the falsifier.** MECH-521's `what_would_answer` currently runs a 2x2 of
   carrier-ratio x coupling. On this derivation the **shared-budget term is a third factor and
   the load-bearing one**: with it off, the graceful phase should vanish while capacity survives.
   That is a cleaner and cheaper discriminator than the 2x2, and it is a *prediction* the toy
   makes rather than a reconciliation.
4. **Leg 2 survives intact and is now derived** -- capacity and occupancy really are separable,
   and the capacity bound really does move with the control parameter.

## Honest limits

- **One toy, one kernel family, one normalisation form.** A 1-D ring with a Mexican-hat kernel
  is the standard minimal model, not a proof about REE's actual dynamics.
- **Retention percentages are depressed by a measurement artifact, not by the mechanism.**
  v3 jitters item positions (deliberately, to kill a ring resonance -- v2's evenly-spaced items
  are commensurate with the inhibition wavelength at some M, which produced a spurious
  non-monotone recovery at M=18). Jitter lets items land inside one excitatory width of each
  other, which caps retention independently of capacity. **The DV that carries the finding is
  peak amplitude, not retention.**
- **The v1 run had a rotation bug** in item-to-domain matching (retained=0 with domains present
  at low load); v2/v3 replace segment bookkeeping with rotation-free local-maximum detection.
  Recorded because the v1 numbers are in the session scratch and should not be reused.
- This says nothing about whether REE's perceptual grain behaves this way -- MECH-521's P0-P2
  substrate preconditions are all still unmet (no endogenous unit count, no shared fidelity
  budget, capacity is a hard `max_tokens` constant). It says only what the *proposed mechanism*
  does and does not predict.

## Recommendation (not applied -- for the user / `/governance`)

Amend MECH-521 to name the shared budget as a required third ingredient, and re-point its
falsifier at the shared-budget term as the primary factor. Do **not** retire the claim: leg 2
is derived, and the missing ingredient is both identifiable and already present in the
substrate. The "third answer to Q-077" framing is what needs the caveat -- it holds *only
under a shared budget*, which is arguably just Bays & Husain's resource horn supplying the
graded half, with settling supplying the discrete half.
