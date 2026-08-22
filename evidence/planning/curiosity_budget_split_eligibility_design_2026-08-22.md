**Status: DESIGN PASS -- AWAITING USER RATIFICATION. No code, no config, no claims.yaml
status/flag edits were made by this session. This document proposes; it does not build.**

# Curiosity budget split: does a constitutional-eligibility layer beat a shared clamp + static weights?

Session: `serene-yalow-3dd4b0`. Chip: `chip-20260822-curiosity-budget-split-eligibility`.
Baseline under review: section 4 of
`evidence/planning/mech314bc_percandidate_extension_staged_2026-08-08.md` (NOT RATIFIED
2026-08-22).
Work-graph classification on entry: `complex (probe-gated)`. On exit: see section 11 --
partially converted to `complicated (buildable)`, with one named probe remaining.

---

## 0. The question, and the user's objection

ARC-065 GAP-A gave MECH-314b (uncertainty) and MECH-314c (learning-progress) a per-candidate
read, joining MECH-314a (novelty). All three now contribute to the same argmin-relevant
deviation term inside one shared `+/-curiosity_bias_scale` budget in
`StructuredCuriosity.compute_score_bias`. How is that budget allocated among them?

Section 4's staged resolution: one shared deviation clamp; relative allocation governed by the
static per-flavour weights (Q-043/Q-044); per-sub-flavour clamps rejected.

The user declined to ratify, verbatim:

> "this is exactly where the constitutional eligibility and more complex biology similar basal
> ganglia set up might have a better answer than a single test. perhaps more consideration as
> to how this could be robustly done is needed"

This document tests that objection against the substrate. **The objection is substantially
correct, and more sharply so than the phrasing suggests**: section 4's rationale point 3 is not
merely under-ambitious, it is **refuted by measurement**. Details in section 2b.

---

## 1. What the baseline actually is, in code

`ree-v3/ree_core/policy/structured_curiosity.py:compute_score_bias`, verified this session:

```
total = 0
if novelty:      total -= w_nov * novelty_vec          # [K], per-candidate
if uncertainty:  total -= w_unc * uncertainty_vec      # [K] (Phase 2) or scalar*ones (Phase 1)
if lp:           total -= w_lp  * lp_vec               # [K] (Phase 2) or scalar*ones (Phase 1)

raw_offset    = total.mean()                  # argmin-INERT
raw_deviation = total - raw_offset            # argmin-RELEVANT
deviation = clamp(raw_deviation, -bias_scale, +bias_scale)   # ONE shared clamp
offset    = clamp(raw_offset,    -bias_scale, +bias_scale)
total = deviation + offset
```

Defaults: `curiosity_novelty_weight = curiosity_uncertainty_weight =
curiosity_learning_progress_weight = 0.05`; `curiosity_bias_scale = 0.1`.

The clamp is applied elementwise to the **summed** deviation. This matters for section 2a.

---

## 2. Which of section 4's four rationale points survive contact with the substrate

### 2a. Point 1 (the budget is a channel property, not a sub-flavour property) -- SURVIVES

Correct and load-bearing. The clamp bounds curiosity against the rest of the score-bias chain
(dACC / lateral_pfc / ofc / mech295). That is a statement about curiosity-as-a-channel. No
candidate design below disturbs it: **every design keeps exactly one shared clamp, unchanged,
at the same place in the pipeline.**

### 2b. Point 2 (per-flavour rails sum to 3x the rail) -- SURVIVES, and generalises into a hard design constraint

This is section 4's strongest argument and it is correct as written. Three independent box
constraints `|dev_f| <= rail` imply only `|sum_f dev_f| <= 3*rail`. A design that bounds each
flavour separately does not bound the channel, which re-opens exactly the domination the clamp
exists to prevent.

**Promoted here to a binding constraint on every candidate: C1 -- the total argmin-relevant
influence must remain bounded by a single shared rail. A design that does not satisfy C1 is not
a candidate.** Both designs below satisfy C1, and they satisfy it the same way: they change
*what is summed*, never *how the sum is bounded*. Normalisation and gating happen strictly
**upstream** of the single existing clamp, which is left byte-for-byte alone.

The general point section 4 was reaching for, stated precisely: **independent per-channel box
constraints cannot bound a sum; coupled constraints can.** A simplex allocation
(`gains >= 0, sum(gains) <= 1`) or a shared post-sum rail are both coupled. Per-flavour rails
are not. This is why "per-flavour clamps" is the wrong shape and "per-flavour normalisation
under one rail" is not the same proposal wearing a hat.

### 2c. Point 3 (within-budget domination is a WEIGHT-calibration question, Q-043/Q-044) -- DOES NOT SURVIVE

Three independent findings, all verifiable from source or registry, each sufficient on its own.

**(i) The three signals are on mutually incommensurable scales, so equal weights are not equal
allocation.** Verified in source this session:

| flavour | signal | units | scale |
|---|---|---|---|
| 314a novelty | `min_dists / mean_norm` (`structured_curiosity.py`) | **dimensionless ratio** | explicitly scale-normalised, O(1) |
| 314b uncertainty (Phase 2) | `predictive_variance` = `(std**2).mean(-1)` (`e2_world_uncertainty.py:516`) | **squared z_world units** | unbounded positive |
| 314b uncertainty (Phase 1) | `e3._running_variance` | squared PE units | unbounded positive |
| 314c learning progress | EMA of `abs(PE_t - PE_{t-K})` | PE-difference units | unbounded positive |

314a is *already* normalised, and the code says why, verbatim: *"Normalise by the
candidate-pool mean norm to keep magnitudes comparable across world_dim choices and to avoid
swamping the bias_scale clamp."* **The module has already accepted this principle -- for
exactly this reason -- and applies it to one flavour of three.** Designs B and C below are not
a foreign import from the BG literature; they are the uniform application of a rule this module
already follows.

With all three weights defaulting to `0.05` against quantities in a dimensionless ratio, a
squared-z variance, and a PE first-difference, the realised allocation is set by the accident of
each signal's natural scale. That is not a calibration state; it is an uncalibrat**able** one.

*Worked, with the module's own defaults (`w = 0.05` each, `bias_scale = 0.1`, K=32).* Take a
314b variance with a raw span of ~4e3 against a 314a novelty ratio with a raw span of ~5e-2 --
a scale gap the table above makes unremarkable. The summed pre-clamp deviation span is then
~198, against a rail that permits a post-clamp span of 0.2. Every candidate but one is pinned
at the rail: `last_clamp_saturated_frac` sits at its `(K-1)/K` ceiling and 314a's ordering is
annihilated. **That is the exact failure the 2026-07-21 clamp-ordering fix was made to prevent,
recurring one layer down** -- reached last time through uniformity, reached this time through
scale. That fix bounded the *mechanism* by which a flavour could flatten the ranking; it did
not bound the *magnitudes*, because at the time only 314a had a per-candidate span at all.

**(ii) 314b's scale is NON-STATIONARY, and shrinks precisely as the mechanism starts working.**
`predictive_variance` is a variance. Training the SD-063 head *reduces* it -- that is what
training a variance head does. So under Design A the 314b/314a allocation ratio drifts by
orders of magnitude across training with nobody touching a knob, and drifts *downward* exactly
as 314b's signal becomes trustworthy. **A static weight cannot govern a non-stationary
allocation.** This is the technical core of the user's objection and it is not a matter of
taste.

**(iii) Q-043 -- the question point 3 defers to -- is itself blocked, by a measurement of the
very authority point 3 assumes.** From `claims.yaml`, Q-043 `what_would_answer`, HARD
PRECONDITION, *"the decisive blocker, confirmed twice"*: V3-EXQ-605 found the curiosity
dimension fully degenerate (`curiosity_scale` 1x/5x/10x byte-identical per-cell entropy) and
V3-EXQ-667 found 4/5 seeds byte-identical across full 8x joint scaling -- **"the knobs have
ZERO authority"**.

Point 3 therefore routes the allocation question to a question that is blocked on the premise
point 3 asserts. *Honest caveat, stated because it is the strongest counter:* those
measurements (2026-06-11) **predate** the 2026-07-21 clamp-ordering fix that restored 314a's
argmin-relevant path, so they are not a current reading. But the correct conclusion from that
is not "point 3 stands" -- it is that **the weights have never been demonstrated to govern
allocation, and the only direct evidence on record says they did not.** Point 3 assumes what
has been measured false and not since re-measured.

### 2d. Point 4 (the residual hazard is caught by the readiness gate) -- SURVIVES ONLY AS OBSERVATION, NOT AS PREVENTION

Point 4 is honest about what it does: `last_clamp_saturated_frac` and the per-flavour
`*_dev_range` diagnostics let an experimenter *see* a wide-span 314b compressing 314a's
ordering inside the shared clamp. Nobody disputes that it is observable.

The user's objection is that observing is not governing, and it lands. Two consequences:

- The gate fires **out of band** (at experiment readiness, once, by human assertion) against a
  hazard that is **in band** (per decision, every tick, and -- per (ii) above -- drifting
  across training). A readiness assertion made at t=0 does not bind at t=100k.
- **The readiness gate is already a degenerate eligibility layer.** Its
  `*_dev_range > 0` test is precisely a validity predicate: *does this flavour carry
  argmin-relevant span right now?* Section 4 computes exactly the right quantity and then
  writes it to a diagnostic instead of routing it into the allocation. So the gap between
  section 4 and the user's proposal is smaller than either framing suggests: it is the gap
  between an offline binary assertion and an online graded signal, over a quantity that is
  **already computed inside `compute_score_bias` on every call**.

That last observation is what makes Design B small.

---

## 3. Is this the same KIND of problem as commitment eligibility?

The chip asks this directly. The answer is **partially, and the difference is the design's main
fork.**

**Where the analogy holds.** ARC-107 / MECH-448's principle is exactly on point, and it is the
user's phrase "constitutional eligibility" in the codebase's own words: *"The required
architecture is **constitutional, not parametric**... a signal's STRENGTH must be necessary but
not sufficient -- it also needs LAWFUL ACCESS to committed action"*; *"F decides who is
ELIGIBLE to compete, not who wins."* Transposed one layer down: **a curiosity sub-flavour's
raw magnitude should not purchase allocation.** Section 4 is the parametric answer (weights and
a rail). ARC-107 was registered because the parametric answer failed at this seam across five
mechanistically distinct channels (CRF 654g, OFC 485h, SD-037 625e, dACC 445h, modulatory
569g). The user is applying an established finding of this codebase one layer down, not
importing an intuition.

**Where the analogy breaks, and it matters.** BG eligibility arbitrates **competitors for a
single output**, where winner-take-most is the right shape. The three curiosity sub-flavours
are better read as **three noisy estimators of one latent quantity** -- expected information
gain. Novelty estimates it by state-space coverage; uncertainty by predictive variance;
learning progress by realised error reduction. Under that reading the principled combination is
**precision-weighted fusion**, not competition, and a winner-take-all eligibility gate would be
actively wrong -- it would throw away two of three estimates of the same thing.

**This fork is exactly Q-044**, which is open: *"Are 314a, 314b, 314c three distinct substrates
with independent contributions, or three different readings of one mechanism?"* Q-044 has its
own HARD PRECONDITION and is not resolvable today.

**The load-bearing consequence, and the reason a recommendation is possible at all:
commensuration is correct under BOTH readings of Q-044.**

- If they are three readings of one mechanism -> normalisation is **commensuration before
  fusion**. Required.
- If they are three distinct substrates -> normalisation is **stripping a magnitude advantage
  before competition**. Required, and it is literally ARC-110's named conversion mechanism.

So the *normalisation* layer is Q-044-agnostic and can be designed now. The *learned
arbitration* layer (Design D) is not -- it needs to know what it is arbitrating between. This
is the cleanest line through the problem and it drives the recommendation in section 12.

---

## 4. The prior art is already built, in this repo, one layer up

ARC-110 (parallel segregated cortico-BG-thalamic loops) was **built 2026-06-27** behind
`REEConfig.use_loop_segregation`. `ree-v3/ree_core/predictors/e3_selector.py` contains the
whole stack, and every piece transposes:

| ARC-110 component (built) | What it does | Transposed to the curiosity layer |
|---|---|---|
| `_loop_normalize(pref, mode)` -- `zscore` \| `range` \| `none` | *"Normalise a loop's within-eligible preference so F's raw magnitude carries no cross-loop advantage (the ARC-110 conversion mechanism)"* | per-flavour commensuration (Design B) |
| flat loop -> `zeros` (`std < 1e-9`) | a loop with no spread contributes nothing | **per-decision validity gate, already implemented** |
| static gains `m_a`, `g_a`, `g_l` | fixed cross-loop combine | per-flavour allocation gains |
| `W_cross = I + M_cross`, learned, `M_cross==0` -> bit-identical | dopamine-gated learned arbitration | learned allocation (Design D) |
| `_parity_forward_gain` / ascending-parity controller | bounds a channel's effective weight at a parity ceiling | bounded allocation without per-flavour rails |
| `_loop_inlayer_null(accum, alpha)` | magnitude-matched random-structure perturbation **in the same layer**, so `noise_verified_lifting` is a meaningful non-vacuity precondition | **the non-vacuity control for all falsifiers below** |

Two things follow. First, "use eligibility" is **not** gated on building an eligibility layer
from scratch -- the chip's worry that ARC-008 and MECH-062 are both partly-unbuilt is correct
about *those two claims* but is answered by ARC-110, which is the claim that actually owns
selection-structure segregation (MECH-062's own `status_note` routes it there explicitly, and
ARC-110's notes say *"do NOT chip a duplicate experiment"*). Second, the codebase's
no-op-default discipline (`M_cross == 0` -> bit-identical) is the template for shipping any of
this safely.

**The honest warning that comes with the prior art.** ARC-110's own validation, V3-EXQ-707c
(2026-07-25), reads *"the F-dominance conversion ceiling is INTRINSIC, not a
single-arena-collapse artefact"* -- i.e. this exact normalise-then-arbitrate stack, one layer
up, **did not lift the ceiling it was built to lift.** Any expected effect size here must be
sized against that. The counter-argument, which is real but must not be overstated: at the loop
layer the stack was trying to make a *lower-valued* channel win against a higher-valued one --
a value question. Here it is making *incommensurably-scaled estimators* comparable -- a units
question, which normalisation actually does solve. Different failure mode, same machinery. That
distinction is a reason for cautious optimism, not for confidence.

---

## 5. Constraints every candidate must satisfy

Derived from section 2, and used as the comparison axes in section 9.

- **C1 (from point 2).** Total argmin-relevant influence bounded by ONE shared rail. No
  per-flavour rails.
- **C2 (from point 1).** The clamp stays a whole-channel authority knob; `curiosity_bias_scale`
  keeps its current meaning.
- **C3 (from point 3).** Allocation must be invariant to each signal's arbitrary units and
  robust to a signal's scale drifting non-stationarily across training.
- **C4 (from point 4).** The domination hazard must be addressed per-decision, in band -- not
  only observed at readiness.
- **C5 (vacuous-channel class: 604a / 624a / 614d / 640a).** The design must be
  *distinguishable* from static weights by a pre-registered measurement, with a
  magnitude-matched in-layer null establishing that the layer has authority at all.
- **C6 (codebase discipline).** Bit-identical OFF by default.

---

## 6. Design A -- baseline (section 4, restated honestly)

One shared clamp; static per-flavour weights; observe-at-readiness.

- C1 **PASS** -- one rail on the summed deviation.
- C2 **PASS** -- by construction.
- C3 **FAIL** -- section 2c(i)/(ii). Equal weights across a dimensionless ratio, a squared-z
  variance and a PE first-difference are not equal allocation, and 314b's scale shrinks as its
  head trains.
- C4 **FAIL** -- observation, not prevention; fires once, out of band.
- C5 n/a -- it *is* the baseline.
- C6 **PASS** -- it is the shipped state.

**Not withdrawn, and genuinely defensible on two counts:** it is the only design with zero new
machinery, and if the span-disparity probe in section 11 returns "no disparity", A is exactly
right and everything below is over-engineering. That is a real possible outcome and it is why
section 12 does not recommend building today.

---

## 7. Design B -- commensurate allocation (RECOMMENDED design of record)

**The one-line statement.** Normalise each flavour's contribution to a common span *before*
summing; allocate with gains on the simplex; leave the single shared clamp exactly as it is.

```
nov_c = w_nov * novelty_vec                       # unchanged
unc_c = w_unc * uncertainty_vec                   # unchanged
lp_c  = w_lp  * lp_vec                            # unchanged

# NEW, and the ONLY new step:
nov_n = flavour_normalize(nov_c, mode)            # range -> span exactly 1; flat -> zeros
unc_n = flavour_normalize(unc_c, mode)
lp_n  = flavour_normalize(lp_c,  mode)

total = -(g_nov*nov_n + g_unc*unc_n + g_lp*lp_n)  # gains >= 0, sum(gains) <= 1
# ... then the EXISTING offset/deviation split and the EXISTING single clamp, untouched.
```

`flavour_normalize` is `_loop_normalize` transposed (section 4), including its
`spread < eps -> zeros` branch.

**How it answers the four rationale points.**

1. *(Point 1)* Untouched. One clamp, same place, same meaning.
2. *(Point 2)* **Structurally avoided rather than argued around.** There are no per-flavour
   rails. Normalisation is a *rescale*, not a bound; the bound is still the single post-sum
   clamp, so the total is bounded exactly as today. With `sum(gains) <= 1` and each normalised
   span `<= 1` under `range` mode, the pre-clamp deviation span is bounded by `sum(gains)` --
   a quantity the baseline leaves **unbounded**, since the raw signals are unbounded. The
   post-clamp bound is *identical* in both designs (same rail, same place); what B adds is a
   bound where A has none. Point 2 is the reason this design normalises instead of clamping
   per flavour, and point 2 survives intact.
3. *(Point 3)* Answered at the root: after normalisation the gains are **dimensionless shares**,
   so allocation is finally expressible. This is the first configuration in which "calibrate
   the weights" is a coherent instruction, which makes B a **prerequisite for Q-043**, not a
   competitor to it.
4. *(Point 4)* The residual hazard is **removed by construction**, per decision, in band: a
   wide-span 314b cannot compress 314a's ordering because no flavour carries a magnitude
   advantage into the sum. The `*_dev_range` diagnostics survive unchanged as the observation
   layer (report both raw and normalised spans, so the disparity stays visible rather than
   being silently absorbed).

**V3-tractable NOW: yes, entirely. No new substrate, no new signal, no training.** Sizing:
one `flavour_normalize` helper (~20 lines, transposable from `_loop_normalize`), one config
enum `curiosity_flavour_normalize: {"none","range","zscore"}` default `"none"`, three gain
floats defaulting to reproduce today's behaviour, the call-site change above, and contracts.
Every input it needs is already computed inside `compute_score_bias`.

**Recommend `range` over `zscore`** for this layer, departing from ARC-110's default: `range`
maps each flavour to a span of exactly 1, so the gains *are* the allocation and
`sum(gains) <= 1` is a literal budget statement. `zscore` leaves the span dependent on K and on
distributional shape, which reintroduces a weaker version of the commensurability problem.

**The real hazard in this design, stated plainly.** Normalisation is division by spread, so a
*nearly*-flat flavour has its numerical noise amplified into a full-span signal -- a **dead
channel normalised up into a loud one**, which is the vacuous-channel failure class running in
reverse and would be worse than the disease. `_loop_normalize`'s absolute `< 1e-9` guard is not
adequate here, because these signals have no common scale for an absolute threshold to mean
anything (that is the whole problem). The guard must be **relative** -- spread measured against
the flavour's own magnitude or against a noise floor. Getting that threshold right is where
Design C earns its keep.

**Behavioural note, not a defect but must not be glossed:** turning normalisation ON is
bit-identical OFF (C6) but is *not* behaviour-preserving when enabled -- with today's equal
default weights it would newly produce genuinely equal allocation. That is the point of the
change, and it makes the ON path a scored-run decision, not a silent default flip.

---

## 8. Design C -- two-tier constitutional eligibility (validity gate, then commensurate competition)

Design B with the implicit `spread -> zeros` branch promoted to an **explicit, first-class,
per-decision eligibility predicate**, which is the direct reading of the user's "constitutional
eligibility":

```
eligible_f = (spread_f > relative_floor_f) AND (source_f is live) AND (precondition_f holds)
gains      = normalize_to_simplex(base_gains * eligible_f)   # ineligible -> 0, others share out
```

Tier 1 (**eligibility**) is binary and is about *validity*: does this estimator carry meaning
right now? Tier 2 (**allocation**) is graded and runs only among the eligible.

Per-flavour predicates that are already available or nearly so:
- **314a**: `_last_candidate_spread > 0` -- the Q-044 hard precondition (E2 world-forward
  compressing K candidates to identical z_world) is *exactly* an eligibility failure, and today
  it is invisible to the allocation.
- **314b**: head instantiated **and trained** (the SD-063 keystone) **and**
  `uncertainty_dev_range` above a relative floor. The "untrained head is near-uniform" hazard
  that section 6 of the staged doc warns about becomes a *mechanised* refusal rather than a
  human instruction not to enable a flag.
- **314c**: no live source until MECH-482 -> permanently ineligible today, correctly and
  automatically, rather than by a guard hardcoded to `None` in `agent.py`.

**How it answers the four points:** identical to B on points 1, 2, 3 (same single clamp, same
simplex, same commensuration). It goes strictly further on point 4: the readiness gate is
promoted from an offline human assertion into an online mechanism, so an estimator that
*becomes* invalid mid-run (a head whose variance collapses, a candidate pool that degenerates)
is dropped at that decision rather than at the next experiment review.

**V3-tractable NOW: mostly.** The gate machinery is small and needs no new substrate. What it
needs that does not exist is the **relative validity floor** -- the threshold below which a
spread is noise rather than signal. That number is not derivable from first principles here; it
has to be measured per flavour. **This is the honest gate on C, and it is the same measurement
the section 11 probe produces.**

**What C does NOT need:** ARC-008's tau/rho/phi three-axis system or MECH-062's tri-loop
gating, both of which are unbuilt. This design deliberately does not depend on either. Anyone
extending it should note that ARC-008's `digestion_note` currently asks for a
split/reclassification decision *before* it is treated as one falsifiable claim -- it is not a
foundation to build on today.

---

## 9. Comparison

| | A (baseline) | B (commensurate) | C (eligibility + commensurate) | D (learned) |
|---|---|---|---|---|
| C1 total bounded | PASS | PASS | PASS | PASS |
| C2 clamp semantics | PASS | PASS | PASS | PASS |
| C3 unit-invariant / drift-robust | **FAIL** | PASS | PASS | PASS |
| C4 in-band, per-decision | **FAIL** | PASS | PASS (explicit) | PASS |
| C5 distinguishable from A | n/a | yes (sec 10) | yes (sec 10) | yes |
| C6 bit-identical OFF | PASS | PASS | PASS | PASS |
| new substrate needed | none | **none** | none + one measured floor | learning signal + Q-044 |
| gated on Q-044 | no | **no** | no | **yes** |
| build size | zero | small | small + a measurement | large |

**Design D -- learned allocation** (the `W_cross = I + M_cross` analog: gains learned by a
three-factor dopamine-gated update on post-commit outcome). Included for completeness and
**not recommended now**. It is the most biologically faithful and the most fully "constitutional",
and the machinery exists one layer up. But it is gated on Q-044 (section 3: you cannot learn an
allocation without knowing whether you are fusing estimators or arbitrating competitors), it
needs a credit-assignment signal for "did this flavour's recommendation reduce error", which is
itself MECH-482-shaped, and V3-EXQ-707c is direct evidence that the learned-arbitration stack
one layer up did not deliver its expected lift. Sizing it honestly: a substrate build of the
same order as ARC-110's, behind at least two unresolved questions. Revisit after B/C and Q-044.

---

## 10. Falsifiers and readiness signatures

Per C5, each design needs a pre-registered measurement distinguishing it from A, and a
non-vacuity control. The 604a / 624a / 614d / 640a class is the thing to beat: **a mechanism
that cannot be distinguished from static weights is not an improvement.**

**Shared non-vacuity precondition (reuse, do not reinvent).** Adopt the ARC-110 S2 in-layer
null: perturb a flavour's contribution with a magnitude-matched random-structure vector **in
the same layer** and confirm the committed DV moves (`noise_verified_lifting`). If a
magnitude-matched null cannot move the committed action, the curiosity layer has no authority
and **no result from any design in this document is informative**. Given V3-EXQ-605/667's
measured zero-authority finding (section 2c(iii)), this precondition is not a formality -- it is
the most likely place the whole programme stops, and it should be checked first and cheaply.

**Design B vs A -- discriminating condition.** B and A differ *only* when the flavours' raw
deviation spans are unequal; at equal spans normalisation is a no-op. So:

- *Readiness signature:* measured span disparity
  `D = max_f(dev_range_f) / min_f(dev_range_f)` over live flavours, `D >> 1`. If `D ~ 1`, B is
  vacuous by construction and must not be scored -- **this is the guard that stops B joining the
  604a class.**
- *Pre-registered prediction:* define **selection attribution** = the fraction of decisions on
  which the committed candidate equals the argmin of the widest-span flavour taken alone. Under
  A with large `D`, attribution should be near 1 (one flavour is effectively deciding). Under B
  it should fall materially toward a blended/chance level.
- *FALSIFIED if:* with `D >> 1` measured, A and B produce the same committed-action sequence.
  That would mean either the shared clamp already equalises the flavours, or the argmin is
  dominated by the non-curiosity chain regardless -- **the ARC-107 F-dominance ceiling
  reasserting itself, which given V3-EXQ-707c is the single most likely null and should be
  named as such in advance.**

**Design C vs B -- discriminating condition.** C differs from B only when a flavour's validity
*changes state* during a run.

- *Readiness signature:* at least one flavour crosses its validity floor mid-run (e.g. 314b's
  `uncertainty_dev_range` rising above the floor as the SD-063 head trains, or 314a's
  `_last_candidate_spread` collapsing when the candidate pool degenerates). Count the crossings;
  **zero crossings means C is indistinguishable from B on that run and must not be scored
  against it.**
- *Pre-registered prediction:* C's committed-action sequence diverges from B's exactly at and
  after the crossing ticks, and C's post-crossing behaviour tracks the newly-valid estimator.
- *FALSIFIED if:* crossings occur and the sequences do not diverge -- the gate is decorative.

---

## 11. What remains `complex (probe-gated)`

One probe, and it is deliberately cheap. **Do not choose between A, B and C without it.**

**PROBE: the span-disparity and authority probe.**

For each decision on an existing curiosity-on run, record the three per-flavour contribution
vectors (the `*_contrib` tensors already computed in `compute_score_bias`; today only their
scalar ranges are retained). Then, entirely offline from those recordings:

1. compute the span disparity `D` -- **does the problem exist?**
2. recompute the argmin under per-flavour normalisation and count the decisions on which the
   committed candidate would change -- **would fixing it matter?**
3. run the magnitude-matched in-layer null -- **does this layer have authority at all?**

This needs no new substrate and no new experiment arm; it is instrumentation plus offline
arithmetic on recorded vectors.

Outcomes, all three of which are decisive:
- `D ~ 1` **or** ~0% selection changes -> **the budget-split question is moot at the current
  substrate; Design A is correct and B/C are over-engineering.** Ratify section 4 as written.
- `D >> 1` with a material fraction of selection changes -> **B converts to
  `complicated (buildable)`** and should be built.
- The in-layer null cannot move the committed DV -> **the question is not a budget-split
  question at all**; it is downstream of the ARC-107 authority ceiling, and the correct route is
  ARC-107 / MECH-448, not this seam. Re-classifies the whole node.

**Sequencing, and why this does not block anything.** The probe is only *meaningful* once
314b's per-candidate source is live, because until then 314b contributes a pure uniform offset
with `dev_range == 0` and the disparity is undefined. That source is exactly what
`chip-20260822-sd063-head-training-keystone` builds, and that chip already produces
`last_uncertainty_dev_range` as part of its own readiness gate. **The measurement this decision
needs is a by-product of a build that is already authorised and already running.** So the
correct sequencing is: keystone lands -> probe reads its diagnostics -> this decision resolves.
No duplicated work, and nothing here blocks that chip.

---

## 12. Recommendation

**Do not ratify section 4 as written. Adopt Design B's constraint set (C1-C6) as the design of
record. Do not build yet -- sequence the build behind the SD-063 keystone, which produces the
measurement that decides whether to build at all.**

Reasoning, compressed:

1. Section 4's points 1 and 2 are correct and are preserved unchanged by every alternative.
   **Point 2 in particular is not worked around -- it is the reason B normalises instead of
   clamping per flavour.**
2. Section 4's point 3 is refuted by measurement, not by preference: incommensurable units, a
   non-stationary 314b scale that drifts as the head trains, and a Q-043 precondition recording
   that the weights had zero measured authority. This is the substantive part of the user's
   objection and it is correct.
3. Section 4's point 4 is honest but is observation, not governance -- and the quantity it
   observes is already computed in-band on every call, which makes the fix small.
4. The mechanism is not exotic and is not gated on the two partly-unbuilt anchors the chip
   named (ARC-008, MECH-062). It is **already built one layer up** as ARC-110, transposes
   component-for-component, and is the uniform application of a normalisation rule 314a already
   follows for the reason the code itself states.
5. It is nonetheless **not yet demonstrated to be needed**, and one honest cheap probe can
   dissolve the question entirely. Building before that probe would be exactly the
   substrate-first error this codebase keeps autopsying.

**The disagreement, surfaced rather than smoothed.** Section 4's author was right that a
budget is a channel property and right that per-flavour rails are the wrong shape; the staged
doc's strongest argument survives this review intact and is load-bearing in the replacement.
Where it erred was in treating the leftover as a calibration problem, when the signals are not
on a common scale and one of them does not hold still. And there is a real argument *against*
this recommendation that should be weighed: **V3-EXQ-707c is direct evidence that this exact
normalise-then-arbitrate machinery, one layer up, did not deliver its expected lift.** The
counter is that the failure mode differs (a value question there, a units question here), but
that is a reason for cautious optimism, not confidence. Expected effect size should be set low,
and the section 11 probe is what keeps a low-expected-effect build from being spent
speculatively.

---

## 13. Scope -- what this document deliberately did not do

- **No code.** Nothing in `ree-v3` was modified.
- **No config.** No new knobs; the ones named in section 7 are proposals.
- **No claims.yaml edits.** No `status`, `v3_pending`, `pending_retest_after_substrate`,
  confidence or `implementation_note` change on MECH-314a/b/c, Q-043, Q-044, ARC-008,
  MECH-062, ARC-110, MECH-448 or MECH-482.
- **Section 4 left intact.** Its resolution text is unedited and remains the baseline; this
  document is referenced from it, not substituted into it.
- **No duplication of `chip-20260822-sd063-head-training-keystone`**, which is independent,
  authorised, and is the correct next build regardless of how this decision resolves.
