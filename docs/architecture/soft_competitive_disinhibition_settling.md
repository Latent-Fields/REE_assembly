---
title: "Disinhibitory soft-competitive settling -- MECH-140 x MECH-450 (V3)"
nav_exclude: true
---

# Disinhibitory soft-competitive settling -- MECH-140 x MECH-450

**Substrate id:** `disinhibitory_soft_competitive_settling`
**Owning claims:** MECH-140 (tri-loop arbitration uses SOFT-COMPETITIVE DISINHIBITION -- losers
down-weighted, not silenced -- rather than winner-take-all) x MECH-450 (a minimal RECURRENT SETTLING
step -- a few rounds of mutual/lateral inhibition over the eligible set before commit, replacing the
one-shot pallidal-readout argmin). This is the IMPLEMENTATION of their coupling; it is NOT a new claim.
**Subject:** `selection.disinhibitory_soft_competitive_settling`
**Status:** IMPLEMENTED 2026-07-02. PROMOTES NOTHING. Behind a no-op-default flag, byte-identical OFF
(and an exact no-op at the default gain 0.0 even when the flag is on). MECH-140 + MECH-450 stay
`candidate` until a falsifier converts them.
**Generation:** V3 (attacks the V3 closure blocker MECH-439; `run_id` ends `_v3`,
`architecture_epoch: ree_hybrid_guardrails_v1`).
**Depends on (built, V3-frozen):** MECH-448/449 + ARC-107 (the F-bounded Go/No-Go eligible set the
settling runs within). Composes with -- does not require -- MECH-450 `W_lat`
(`use_learned_settling_step`), ARC-110 (`use_loop_segregation`), and the learned cross-loop
arbitration (`use_learned_cross_loop_arbitration`, V3-EXQ-709).
**Config flag:** `E3Config.use_soft_competitive_settling` (default `False`) + `soft_competitive_settling_gain`
(default `0.0` = exact no-op even when on) + `_rounds` (3) / `_temperature` (1.0) / `_cross_class` (0.25).
**Regression guard:** `ree-v3/tests/contracts/test_soft_competitive_settling.py`.

---

## Problem

The V3 selection readout commits by a **hard one-shot argmin** over the F + MECH-448/449 within-eligible
field. A hard argmin over an F-dominated score structurally returns the F-winner -- the MECH-439
conversion ceiling (F monopolises ~88-89% of committed-selection variance, V3-EXQ-571). The
already-built learned settling (`W_lat`, MECH-450's *learned* half) is a **no-op at init**: it only
bites after dopaminergic learning, so it cannot supply an at-init attractor-flip, and the whole
700/704/706/707 lineage confirmed that no *learned* selection-face lever converts committed-action
diversity on the single arena.

The missing piece the two claims name is **structural, not learned**: MECH-140 asserts arbitration is
*soft-competitive disinhibition* (losers reduced, not silenced) rather than winner-take-all, and
MECH-450 asserts a *minimal recurrent settling step* (a few rounds of lateral inhibition) that can
*flip* the selected attractor where the one-shot argmin cannot. A 2026-07-02 `/lit-pull` attached
fresh external evidence that this is the right primitive:

- **Gallo Aquino / Kim / Rungratsameetaweemana (PLOS Biology 2026, DOI 10.1371/journal.pbio.3003831)** --
  a biologically-constrained E/I RNN + causal mouse-V1 silencing showing **inhibition-on-inhibition is
  the top-down context channel**, and ablating it **collapses task-switching while single-task
  processing survives**. This hands us a ready-made ablation falsifier (below).
- **Keller et al (Neuron 2020, DOI 10.1016/j.neuron.2020.11.013)** -- VIP->SOM cortical disinhibition
  necessary+sufficient for contextual modulation (MECH-140's disinhibition, graded and load-bearing).
- **Lee & Sabatini (Nature 2021)** + **Morita (Behav Brain Res 2016)** -- indirect-pathway *competitive
  disinhibition* (not hard suppression) and the striatal-WTA-vs-cortical-soft-max complementarity
  MECH-140 is built on.
- **Wang 2002 / Rolls 2021** recurrent-attractor + striatal-WTA models -- the bounded recurrent
  settling MECH-450 abstracts.

Post-attach `lit_confidence`: MECH-140 **0.695** (first grounding), MECH-450 **0.837**.

### Failure record (defines acceptance criteria)

| run | conversion DV | reading |
|---|---|---|
| V3-EXQ-707b | committed-class entropy A1_LOOPS **0.838** ~ A0 0.914 (below) | segregation alone, static arbitration, does not convert |
| V3-EXQ-700d | magnitude-matched same-layer null could not verify-lift committed-class entropy (3rd failed valid-null) | the single arena furnishes no valid committed-class null |

**Acceptance target** (for the SEPARATE validation falsifier, queued after this build lands): with the
soft-competitive settling ON (gain > 0), the settling **actually moves the readout** (round_delta > 0 and
the committed winner can flip vs the one-shot argmin) AND committed-action-class entropy lifts above the
one-shot argmin on a strict majority of divergent seeds, on the 569i top-k + MECH-448 demotion conversion
stack, **with no harmful-class disinhibition** (safety) and **not via added stochasticity**
(noise-as-diversity guard).

---

## Solution

A new method `_soft_competitive_settle(field, candidates, eligible_idx)` in `e3_selector.py`. It runs a
few rounds of soft-competitive lateral inhibition over the within-eligible field (COST units, lower ==
better) BEFORE the commit, then returns the settled field to the existing argmin.

### Forward (per round, R rounds)

```
x       = -field                          # activation (higher = better)
for r in range(R):
    support = softmax(x / T)              # graded competitive support, ALL > 0 -> never silenced
    inhib   = gain * (K @ support)        # lateral inhibition received from competitors
    x       = x - inhib                   # disinhibit the winner, reduce (not silence) the losers
return -x                                 # back to COST units for the existing argmin
```

`K` is the **parameter-free class-surround kernel**: `K_ij = 1.0` when candidates `i` and `j` share a
first-action class, `cross_class` (< 1, default 0.25) across classes, `0` on the diagonal (no
self-inhibition). The first-action class is the `argmax` of each candidate's first action -- the SAME
discretisation `W_lat` uses. Because `K` encodes candidate-vs-candidate **structure** (not merely each
competitor's own activation), the settling can **reorder**: a candidate crowded by same-class rivals
accrues more lateral inhibition than an isolated slightly-worse one and can lose to it. A purely uniform
(all-to-all) proportional inhibition would be a monotone, rank-preserving sharpen and could never change
the committed argmin -- behaviourally inert against the F-dominance ceiling; the structured surround is
what gives the settling teeth. `support` is a softmax, so every candidate keeps strictly-positive
activation across all rounds -- **graded, never zeroed** (MECH-140, not winner-take-all).

### Where it composes (two sites, both flag-gated, both bit-identical OFF)

- **Single arena:** transforms `_modulatory_accum[eligible_idx]` after the (learned) `W_lat` settling
  block and before the within-eligible commit argmin.
- **Segregated loops (ARC-110):** transforms the arbitrated cross-loop `final` field after the cross-loop
  combine + explore term and before commit -- so it settles the arbitrated field; it does **not**
  reimplement the cross-loop combine. Its flag is orthogonal to `use_learned_cross_loop_arbitration`
  and default-OFF, so V3-EXQ-709's arms are byte-identical (no collision).

This is a **within-eligible / within-loop** transform: the learned `W_lat` shapes within-loop
competition (learned, no-op at init), the learned `M_cross` shapes across-loop authority (learned), and
this parameter-free step supplies the **always-on graded soft-competition floor** beneath both.

### No-op / bit-identity

`use_soft_competitive_settling=False` -> the block is skipped -> bit-identical. `gain == 0.0` (the
default even when the flag is on) -> `inhib == 0` -> exact no-op (byte-identical at flag-off / at-default,
mirroring `noisy_selection_sigma_init=0.0`). A positive gain must be set to activate. `n < 2` eligible ->
skipped. Waking-only (no settling on a simulation/replay tick, MECH-094). No learned parameters, no
autograd (operates on a detached copy).

### Safety (unchanged)

The settling transforms ONLY the eligible subset, so a No-Go / F-excluded candidate is never touched and
never selectable however the field moves (**no global disinhibition**); the argmin over the returned
field always yields >= 1 survivor. The orthogonal-to-F safety guarantee is inherited from the MECH-448/449
envelope regardless of the settling dynamics.

---

## Biological Grounding (ARC-106)

**Grounding ladder.**

- **L0 (phenomenon).** Action selection is a *competition* that leaves losing options attenuated but
  monitoring-capable, resolved by *recurrent* settling rather than a single feed-forward comparison; the
  competition is shaped by *disinhibition* (removing inhibition from the winner) not hard gating.
- **L1 (systems function).** Soft-competitive disinhibition (indirect-pathway inter-collicular
  competition, Lee & Sabatini 2021; cortical VIP->SOM disinhibition, Keller 2020) + bounded recurrent
  attractor settling (Wang 2002; Rolls 2021) + surround inhibition between competing motor programs
  (Mink 1996). The claim is FUNCTIONAL (a graded, recurrent, structure-sensitive competition that can
  reorder and never silences), not anatomical mimicry.
- **L2 (REE realisation).** A few rounds of softmax-support lateral inhibition over the within-eligible
  field with a fixed first-action-class surround kernel; graded (softmax support > 0), reordering
  (structured kernel), safe (within the eligible set), waking-only.
- **L3 (parameters).** `gain` (inhibition strength), `rounds` (recurrence depth), `temperature`
  (support sharpness), `cross_class` (surround selectivity). All no-op at their `gain 0.0` default.

**Load-bearing-vs-decorative ablation test (ARC-106 cargo-cult guard).** The settling is load-bearing iff
its removal (the flag OFF / gain 0) changes the pre-registered conversion metric. Concretely: on the
conversion-ceiling substrate, the ON arm must lift committed-action-class entropy above the OFF arm AND
the settled winner must be able to differ from the one-shot argmin (round_delta > 0 with a flipped
committed index on a divergent pool). If committed-class entropy and the committed index are unchanged
when the settling is ablated, the step is **decorative** and the claims are WEAKENED (route back). The
PLOS-Biology ablation falsifier is the sharper form of this test (below).

**Divergence ledger (logged, not silent):**

| # | Divergence from biology | Why acceptable (function over homology) |
|---|---|---|
| SCS-1 | **Locus.** The strongest lit evidence (Gallo Aquino/Rungratsameetaweemana 2026; Keller 2020) is **CORTICAL** VIP/SST inhibition-on-inhibition; REE applies the primitive at the **BG within-eligible selection** locus (the tri-loop arbitration MECH-140 names). | ARC-106 G1 function-not-homology: the transferable content is "disinhibition is a real, graded, load-bearing, recurrent-settling top-down control primitive," which is locus-general. The lit caveat is explicit: the cortical papers do NOT validate a BG/pallidal locus, and are silent on the striatal specifics -- that grounding comes from the BG-specific sources (Lee & Sabatini 2021 indirect pathway; Morita 2016 striatal WTA; Mink 1996 surround). This is the honest lit gap. |
| SCS-2 | **Kernel is FIXED, biology's is learned + similarity-graded.** REE's surround kernel is a fixed first-action-class co-membership (1.0 within, `cross_class` across); biology's lateral weights are plastic and graded by representational similarity. | That plasticity is precisely `W_lat`'s job (MECH-450's learned half, `use_learned_settling_step`). This substrate is the **always-on structural floor** beneath the learned inhibition; the two compose. A learned or continuous-similarity kernel is a documented follow-on (would break bit-identical-at-default). |
| SCS-3 | **Discrete first-action class**, not a continuous action-space similarity metric. | Honest simplification; matches the existing `W_lat` discretisation, keeps the kernel parameter-free and the settling cheap. A cosine-similarity kernel is a future refinement. |
| SCS-4 | **Bounded rounds (R~3), no convergence guarantee** to a fixed point. | Deliberate: the "minimal" recurrent step (MECH-450 is explicitly the V3-bounded version; the full thalamo-cortico-basal settling loop is the V4 bet). Bounded rounds keep it a cheap, safe, one-tick transform. |

**Psychiatric-failure-mode mapping (ARC-106 EARNS -- required column).** The settling dynamics, once a
controllable axis, model both poles of the arbitration disorder space (consistent with MECH-450's
`psychiatric_failure_mode` field):

- **Too few / too-weak rounds (gain -> 0, R -> 1)** = collapse back to the one-shot argmin: no settling
  to flip the attractor, the F-winner always wins regardless of context -> **cognitive inflexibility /
  perseveration on the dominant option**, and (when the modulatory blend is unresolved) the
  indecision / blend-output **avolition / abulia** pole. This is exactly the PLOS-Biology
  inhibition-on-inhibition-ablation signature: task-switching collapses while single-task processing
  survives.
- **Runaway recurrent gain (gain, R too high)** = a locked attractor that new evidence cannot flip ->
  **perseveration / catatonic-fixity / obsessional-loop** pole.
- **Loss of the graded floor (hard-WTA instead of soft-competitive)** = losing options silenced rather
  than attenuated, so no monitoring signal survives from the unchosen option -> the impulsive /
  context-blind over-commitment pole MECH-140 exists to prevent (the "WTA imposed across loops causes
  coupling collapse" failure).

---

## The PLOS-Biology ablation falsifier (ready-made)

The Rungratsameetaweemana 2026 result is a pre-registered ablation design REE can run directly: matched
arms where the **inhibition-on-inhibition (lateral-inhibition) edge is INTACT vs ABLATED**
(`use_soft_competitive_settling` ON with gain > 0 vs the same stack with the settling removed), with the
**pre-registered prediction that ablation collapses task-context / switching behaviour while single-task
performance survives** (the mouse-V1 silencing signature). A DECORATIVE settling step would leave both
task-switching and single-task performance unchanged when ablated; a LOAD-BEARING one selectively
degrades switching. `claim_ids = [MECH-140, MECH-450]` (+ MECH-439 if run on the conversion-ceiling
substrate). `EXPERIMENT_PURPOSE = evidence`. PROMOTES NOTHING until it runs.

---

## ML/AI Engineering Notes (Layer 7 -- counsel, not authority)

- **Recurrent soft-WTA / normalisation dynamics.** The softmax-support lateral-inhibition update is a
  standard bounded soft-competition; the REE adaptation is that (a) the kernel is a fixed structural
  surround (not learned attention weights), (b) it operates strictly within a safety envelope, and (c)
  it is a detached, no-autograd, no-parameter transform. Do NOT import an attention block or a learned
  gating net -- the structure is the point, and the learned counterpart already exists (`W_lat`).
- **Rank-preserving trap.** A uniform, similarity-blind proportional inhibition is a monotone sharpen
  and cannot reorder -- it would be behaviourally inert against the very ceiling this exists to break.
  The class-surround kernel is the minimal structure that restores reordering; this was the decisive
  design fork (2026-07-02, user-confirmed class-surround).
- **Numerical stability.** `temperature >= 1e-6` guard; `gain == 0` short-circuits to an exact no-op;
  softmax keeps support bounded in (0,1); bounded R keeps the field finite. No learning-rate to tune
  (parameter-free).

---

## MECH-094

Selection-only, waking-only. The settling runs on the waking committed-selection path; a simulation /
replay tick is skipped (`not simulation_mode`). Nothing is written to memory by this mechanism and there
are no learned parameters, so the `hypothesis_tag` requirement does not engage at this layer.

---

## Claim handling (no new child)

This build mints **no new claim**. It is the coupled implementation of two already-registered candidates
(MECH-140 x MECH-450); it annotates their `implementation_note`s and records the coupling via their
existing `depends_on` / `related_claims`. Both stay `candidate` -- the validation + ablation falsifiers
(queued separately, new EXQ, `claim_ids = [MECH-140, MECH-450]`) test them; a passing run does not
auto-promote.

## Related Claims

MECH-140 (soft-competitive disinhibition), MECH-450 (minimal recurrent settling), MECH-439
(conversion-ceiling umbrella), MECH-448 / MECH-449 (F-bounded Go/No-Go eligible set), ARC-107 (BG
selector constitution), ARC-108 / ARC-110 + `learned_cross_loop_arbitration` (the learned settling /
loops it composes with), ARC-106 (biology grounding). See
`learned_cross_loop_arbitration.md`, `sd_v4_loop_segregation.md`, and the 2026-07-02 lit entries
`evidence/literature/targeted_review_connectome_mech_140/` + `.../targeted_review_connectome_mech_450/`.
