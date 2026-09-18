---
title: "MECH-268 f_sat: functional form, or gradedness?"
nav_exclude: true
status: provisional
status_asof: 2026-09-18
status_claim: MECH-268
---

# MECH-268 f_sat: does the claim assert the functional form, or gradedness?

**Claim ID:** MECH-268 (dacc.conflict_saturation)
**Investigated:** 2026-09-18, session `cranky-wiles-c85265`, user-commissioned via the
Orchestrator (`orchestrate-20260918-gc`)
**Status:** INVESTIGATION. Proposes; applies nothing. No `ree_core` code was changed.
**Depends on:** SD-032b (dACC adaptive control), MECH-258 (the pe signal), SD-034 (closure)
**Referent fix:** LANDED 2026-09-18, `ree-v3` `9cba6c7` + docstring self-correction `f7e0aa2`
(lever `dacc_saturation_thread_current_class`, default False); both verified ancestors of
`origin/main`. It does **not** change any conclusion here -- see "The one genuine form defect".
**Answers:** `chip-20260917-mech268-closure-cadence-dose` (open, unclaimed, waiting on this)
**See also:** [`sd_032_cingulate_integration_substrate.md`](sd_032_cingulate_integration_substrate.md)

## The question

MECH-268 is implemented as

```
n_rec  = count(outcome_class in last dacc_saturation_window outcomes)   # W = 8
excess = max(0, n_rec - dacc_saturation_grace)                          # G = 2
f_sat  = 1.0 / (1.0 + dacc_saturation_strength * excess)                # s = 0.3
pe     = pe_capped * f_sat
```

Two arithmetic consequences drive everything downstream. `excess` is an integer in
`[0, W-G]`, so **at most 7 values of f_sat are reachable** for a given `(s, W, G)`; and the
minimum is `1/(1 + s*(W-G))` -- **0.357 at s=0.3, 0.25 at s=0.5** -- so the reachable range
is `[floor, 1]`, not `(0, 1]`.

Three consecutive MECH-268 experiment designs were refused in two days, each for a reason
traceable to that structure rather than to any user decision. The question the user posed is
therefore whether MECH-268 asserts **this functional form** (in which case the form is fine
and the three designs were simply specified outside its reachable set) or **gradedness as a
functional property** (in which case ~7 rungs over a floored range is a substrate ceiling).

The user's framing is explicit and is the one this document answers: decide it **functionally
-- from what REE needs f_sat for -- not by exegesis of the claim text.**

## Verdict

**FORM -- the reciprocal-with-grace form is not what is wrong, and the three refused designs
were genuinely mis-specified.** But the finding that actually matters is a third thing that
neither branch of the question anticipated, and it is what the design constraint below is
built from:

> **f_sat is currently inert at BOTH of its live consumers, for two reasons that have nothing
> to do with f_sat's functional form, and that no change to that form would repair.**
> At the Shenhav EVC consumer the inertness is *structural and exact*: `candidate_effort` is
> constant across candidates by construction, so the entire control-demand term -- the only
> part of `mode_ev` that `pe` touches -- is a uniform shift, hence argmin-invariant.
> At the SD-032a mode register the inertness is a *calibration* mismatch between `pe`'s
> operating scale and the register's critical value.

So gradedness is not a substrate ceiling, because **no live consumer can resolve any number of
levels at present.** Adding rungs to a signal nothing reads changes nothing. And equally, the
form is not vindicated: it is simply not the binding constraint, and "the form is right" must
not be read as "MECH-268 is working."

One genuine, biology-grounded defect *in the form itself* did surface, is independent of the
in-flight referent fix, and is recorded in Line 2 below: **f_sat reads an unordered COUNT, and
the biology it cites is about a RUN.**

## Line 1 -- what consumes sat_factor, and what does it need

`sat_factor` has exactly two live consumers. Both were traced in the tree and measured on a
live agent.

### Consumer A -- Shenhav EVC -> `DACCtoE3Adapter` -> E3 selection

The chain (`ree-v3/ree_core/cingulate/dacc.py`, `ree_core/agent.py`):

```
pe            = pe_capped * f_sat                                  # dacc.py:_affective_pe
control_req   = pe * dacc_effort_cost                              # dacc.py:397
mode_ev       = candidate_payoffs - control_req * candidate_effort # dacc.py:398
bias          = dacc_weight * drive_gain * (-mode_ev + ...)        # DACCtoE3Adapter.forward
score         = <E3 score> + bias                                  # lower is better
```

`f_sat` is a **scalar**. The only per-candidate quantity it gates is `candidate_effort`.
And `candidate_effort` is (`agent.py:7537`):

```python
effort = torch.tensor([float(c.actions.shape[1]) for c in candidates], ...)
```

`c.actions` is `[batch, horizon, action_dim]`, so **`candidate_effort` is the physical rollout
horizon** -- a generator configuration parameter, identical for every candidate in a set. This
is not incidental: MECH-267's mode-conditioned look-ahead-depth mechanism scales the *scoring
window* and its docstring states explicitly that it "does not change the physical rollout
length (`config.horizon` stays fixed)". There is no code path that emits candidates of
differing `actions.shape[1]` into one `select_action` call.

Measured on a live agent (`REEConfig.from_dims(use_dacc=True, use_affective_harm_stream=True,
use_salience_coordinator=True, use_lateral_pfc_analog=True, dacc_saturation_enabled=True)`,
`CausalGridWorldV2` 8x8 / 8 hazards, 120 ticks, `dacc_weight` at both 0.0 and 1.0):

| quantity | measured |
|---|---|
| candidates per tick (K) | 32 |
| distinct `candidate_effort` values within a tick | **1** (30.0), on 120/120 ticks |
| ticks with `candidate_effort` spread > 0 | **0 / 120** |
| `f_sat` values actually visited | all 7 (0.3571 ... 1.0) |
| `n_rec` values visited | 0 ... 8 |
| **ticks where the E3 argmin changes across all 7 reachable f_sat values** | **0 / 120** |

The zero in the last row is not a null result to be chased with a bigger sample. With
`candidate_effort` constant at `H`:

- `control_req * candidate_effort` is the constant vector `control_req * H` -> a **uniform
  shift** on every candidate's score -> **argmin-invariant**, exactly;
- `harm_interaction = payoff_c * (-effort_c)` where `effort_c = effort - effort.mean()`,
  so the Croxson interaction term is **identically the zero vector**;
- `foraging_value` is a scalar and enters uniformly -> argmin-invariant;
- `suppression` (MECH-260) is per-candidate but has no `pe` dependence.

**Of the four terms `DACCtoE3Adapter` emits, the only per-candidate-discriminative ones are
the payoff part of `-mode_ev` (which is E3's own previous score fed back) and MECH-260
suppression. Nothing that depends on `pe` can influence E3 selection.** Therefore *no*
functional form for f_sat -- reciprocal, exponential, continuous, 7-level or 7000-level --
can change a single selection through this consumer. The defect is in the **effort proxy**,
not in f_sat.

A second, separable observation from the same probe: `dacc_weight` defaults to **0.0** even
under `use_dacc=True`, so `DACCtoE3Adapter` emits the zero vector unless an experiment sets it
(experiments that want a live dACC use 0.5 or 1.0). V3-EXQ-729 -- MECH-268's ecological
falsifier -- does **not** set it. Its live-loop demonstration therefore ran with this consumer
disconnected twice over. That does not retract 729's live-wiring result, which was about
`record_outcome` call counts, but it does bound what that run can be cited for.

### Consumer B -- SD-032a salience coordinator / the mode register

This is the consumer MECH-268's own `functional_restatement` names: saturation exists so that
"the mode register [can] relax even without an explicit closure event". `pe` reaches it as
`dacc_pe` (`salience_coordinator.py:426`) on two paths:

- **affinity:** `affinity_weights["dacc_pe"] = {"internal_planning": 1.0, "internal_replay": 0.5}`,
  added raw to the mode logits, against `external_task_bias = 1.0`;
- **salience:** `salience_weights["dacc_pe"] = 1.0`, summed into `salience_aggregate`, compared
  against `enter_threshold = switch_threshold (1.0) * (1 + stability_scaling * pcc_stability)`.

Both are **absolute-threshold** reads of a scalar, not comparisons across candidates. What
matters is therefore whether f_sat can move `pe` **across a critical value of order 1.0**, and
`f_sat <= 1` means it can only ever push `pe` **down**.

Measured, same live agent, 160 ticks, sweeping all 7 reachable f_sat at strengths 0.3 / 0.5 /
1.0 / 3.0 / 10.0 and recomputing the register's arithmetic exactly:

| quantity | measured |
|---|---|
| `pe_unsaturated` | min 0.271, median 0.975, max 0.990 |
| mode-register critical value for `pe` | `external_task_bias + drive` = **1.0** (drive measured 0.0) |
| `aic_salience` (the other salience input) | 0.0 -- SD-032c not landed |
| mode occupancy | `external_task` 160/160 |
| ticks where `argmax(operating_mode)` changes across the reachable set | **0 / 160**, at every strength |
| ticks where `mode_switch_trigger` changes | **0 / 160**, at every strength |

`pe` never reaches the critical value, so the register is already on the side f_sat would push
it toward; attenuating further only widens the margin. Note the sweep was extended to
strength 10.0 (floor 0.0164) -- **the result is zero at every strength**, so this is a
statement about the operating point, not about the floor.

The opposite regime is documented in the substrate itself. The `affinity_input_cap` comment
(`salience_coordinator.py:276-288`, the 2026-08-12 MECH-266 occupancy fix) records
`dacc_pe ~16-17` through eval on the V3-EXQ-464d/467d substrate -- "two orders of magnitude
above the [0,1]-bounded engagement signal" -- with `operating_mode` collapsing to one-hot
`internal_planning`. That is the rumination signature MECH-268 exists to prevent, observed;
and the fix shipped for it was a **clamp** (`affinity_input_cap`), not saturation. At
`pe ~16`, f_sat's floor of 0.357 yields 5.7 -- still 5.7x above the critical value. At s=0.5
it yields 4.0. f_sat cannot act there either.

So in both regimes for which numbers exist, what decides whether f_sat can do anything is the
**ratio of `pe`'s operating scale to a critical value of order 1.0** -- a calibration property
of `pe` and of `external_task_bias`/`switch_threshold`, not a property of f_sat's granularity.
In neither regime would a finer or continuous f_sat change a single outcome. This is the same
units-mismatch class already documented for `dacc_goal_readout_normalize` and for
`affinity_input_cap`; it is not new to MECH-268, and MECH-268 should not be made to carry it.

### What Line 1 settles

A **multiplicative attenuator cannot own a threshold-relative property.** Consumer B needs
`pe` to land on a particular side of an absolute critical value; f_sat has no knowledge of
that value, and its floor is set by `(s, W, G)` alone. This is the structural reason the
"gradedness" branch of the question does not resolve the situation: the consumer's requirement
is about **where the range sits relative to a threshold**, and gradedness is about **how
finely the range is sampled**. Those are different properties, and only the first is binding.

## Line 2 -- biology

The MECH-268 lit-pull (2026-04-27, eight entries in
`evidence/literature/targeted_review_connectome_mech_268/`) is complete and directly on point;
no new pull is needed. It does not speak with one voice, and the disagreement is informative.

- **Behrens 2007** (ACC volatility-adaptive learning rate): the modulation is a **graded**
  learning-rate adapter, not a binary cap. The entry's explicit implementation recommendation
  is "graded learning-rate adapter rather than a binary habituation cap". This is the single
  source behind the claim's registered distinguishing property.
- **Quilodran, Rothe & Procyk 2008** (macaque ACC, exploration -> exploitation): the cleanest
  direct evidence. Outcome signals are "specific to the first reward" and **disappear** in
  subsequent exploitation trials. Two things follow. First, the empirical dynamic is
  **near-complete silencing after ~1 repetition**, which is steeper and deeper than a
  reciprocal decaying to a 0.357 floor after a grace of 2. Second, and more important, the
  signal **does not die -- it transfers forward to the predictive cue**. Total signal weight
  is conserved and relocated. A multiplicative attenuator implements neither silencing nor
  transfer.
- **Bryden 2011** (rat ACC attention-for-learning): ACC error is **gain-modulated by an
  external attention variable** (Pearce-Hall), not self-saturated by its own outcome history.
  The entry states the failure signature outright: if that is the better account, "MECH-268 is
  framed incorrectly."

So the biology supports *some* history-dependent modulation strongly and across three
modalities, supports **gradedness over a binary cap** (Behrens), and simultaneously indicates
that the reachable range should approach **silence**, not a floor at 0.357 (Quilodran). The
reciprocal-with-grace shape -- "a few free repetitions, then diminishing returns" -- is a
recognisable adaptation curve and is defensible as a V3 approximation. It is not the shape any
of the three papers actually measured.

### The one genuine form defect: `n_rec` is a relabeling-symmetric, order-blind COUNT

`n_rec` is `sum(1 for o in recent if o == cls)` over the last `W` outcomes, where `cls` is
**whichever class is current**. Two defects follow, and they are the same defect:

**(a) It is symmetric under relabeling the classes, so there is no monotone dose in outcome
mixture.** "Count of the current class's own recurrences" cannot distinguish an all-harm stream
from an all-clear one -- both are maximal recurrence of *their* class. So `E[f_sat]` is
necessarily symmetric about a 50/50 mixture, and minimal (most attenuated) at the *extremes*,
maximal (least attenuated) in the *middle*. This is a **property of the functional form, not of
the referent**: it holds for `history[-1]` (the pre-fix fallback) and for the threaded current
class (`9cba6c7`) alike, because both are "whichever class is current". Measured, 20,000
samples per point, `W=8, s=0.3, G=2`:

| base rate p | 0.0 | 0.25 | 0.5 | 0.75 | 1.0 |
|---|---|---|---|---|---|
| `E[f_sat]` | 0.357 | 0.545 | **0.602** | 0.544 | 0.357 |

This is the arithmetic non-monotonicity that killed the first of the three designs, and the
**referent fix does not repair it** -- a point independently established by the session that
landed that fix, and confirmed here. A monotone dose would require a *fixed* referent class
(measured, same conditions: 1.000 -> 0.907 -> 0.661 -> 0.469 -> 0.357, monotone), which is a
**different statistic from the one MECH-268 specifies** and is not what landed.

**(b) It is blind to order, so it cannot express the biology it cites.** Quilodran's saturation
is a property of a **run** (consecutive repetition within an exploitation period); Behrens' is a
property of **volatility** (how often the contingency changes). Neither is a frequency over a
window, and a count cannot distinguish them.

Verified arithmetically (`W=8, s=0.3, G=2`). Each of these streams is 4-of-8, so both classes
have count 4 and the table reads identically under **either** live referent:

| stream (oldest -> newest) | `n_rec` | longest run | `f_sat` |
|---|---|---|---|
| `1 1 1 1 0 0 0 0` (stable run) | 4 | 4 | **0.6250** |
| `1 1 0 0 1 1 0 0` (clustered)  | 4 | 2 | **0.6250** |
| `1 0 1 0 1 0 1 0` (maximal volatility) | 4 | 1 | **0.6250** |

All **70** distinct 4-of-8 streams yield exactly one f_sat value, 0.6250, while the longest
run spans 1 through 4 across them. A maximally volatile alternation is attenuated **exactly as
hard** as a stable run of the same base rate.

That is a direct contradiction of Behrens 2007 -- the very entry the claim's gradedness
property rests on -- which says volatility should **raise** the signal, not leave it
untouched. It is also the wrong dynamic for the rumination story: an agent alternating between
two outcomes is not stuck, and should not have its conflict signal attenuated as though it
were.

**This defect is in the form, is biology-grounded rather than experiment-driven, and is
untouched by the referent fix** -- which changes *which class* is counted and not *that a
relabeling-symmetric, order-blind count is what is read*. It is the one respect in which this
investigation finds the functional form itself wanting, and (a) and (b) are one defect wearing
two faces: both follow from `n_rec` being a count of the current class over an unordered
window.

## Line 3 -- the closure-cadence coupling

`ClosureOperator._fire()` calls `dacc.reset_outcome_history()`
(`closure_operator.py:727-730`; `reset_outcome_history` defaults `True` at `:155`), which
clears the FIFO. Closure cadence therefore drives `n_rec` directly: a trained agent's `n_rec`
sweeps 0..8 repeatedly even when every recorded class is identical, which is why measured
interior occupancy was 0.911-0.946 at every harm threshold tested
(`REE_assembly` `e64d57908f3`) and why the measurements have pointed at closure cadence three
times.

**Does the form need to be graded to carry that coupling?** No -- and the framing slightly
misreads what the coupling is. A closure reset does not *modulate* f_sat; it **re-enters** it
at `n_rec = 0`, i.e. at `f_sat = 1.0`. Closure cadence sets the **residence time** in the
saturated part of the range, not the depth of saturation. Gradedness is what makes the sweep
*observable* at the f_sat level (an on/off cap would show the same residence time as a binary
series), but the consumer-side finding above applies unchanged: the sweep is observable in the
diagnostic and consequential nowhere.

**In production, closure cadence is not merely *a* source of variation -- it is very nearly the
only one.** The outcome class is near-constant live: measured `z_harm_a` norms 0.354-0.890 never
cross the 0.05 default `contextual_safety_harm_threshold`, matching the independently measured
`harm_class_fraction` of 0.946-1.000 with the threshold lever inert. So the recurrence signal is
driven by the FIFO being *cleared* on rule completion, not by graded class-recurrence.

That sharpens the answer to the chip's question. **If the variation the consumer sees comes from
cadence rather than from graded class-recurrence, then gradedness of the FORM is carrying almost
none of the load in production** -- the shape of the decay between rungs matters far less than
how often the ladder is re-entered at the top. This is a second, independent reason the
"gradedness is the claim" branch does not resolve the situation.

Two guards for whoever reads this next:

- **Do not bank "f_sat pins at its floor live."** That was reported and then **withdrawn as a
  fixture artifact**: `use_closure_operator` defaults False, so a fixture that builds no
  `ClosureOperator` never calls `reset_outcome_history()` and the FIFO simply fills. With
  closure ON the FIFO clears, `n_rec` re-ramps and sweeps 0..8.
- **The Line 1 consumer results do not depend on which mechanism generates the variation.**
  Both sweeps enumerate the *reachable set* by construction -- all 7 values of f_sat at each
  captured tick -- rather than relying on the values a particular run happened to visit. A
  different generating mechanism changes which rungs are *occupied*; it cannot change the fact
  that no rung moves the consumer.

So closure cadence does supply real, rich variation in f_sat. It does not supply variation in
anything f_sat drives.

## The design constraint (the FORM branch's deliverable)

Any future MECH-268 experiment must satisfy all four:

1. **The DV must be `sat_factor` itself, or `pe`, and not a behavioural downstream** -- until
   one of the two consumer defects in Line 1 is fixed. There is no behavioural DV that
   `sat_factor` can move. A design that asserts one is unrunnable, and this is the common root
   of all three refusals.
2. **Any criterion on f_sat levels must live in `[1/(1+s*(W-G)), 1]` over at most `W-G+1`
   distinct values**, and must state `(s, W, G)` alongside, because both the rung set and the
   floor are functions of all three. A criterion phrased on the "interior of (0,1)" is
   satisfied by the floor itself and is therefore vacuous. The same rigidity is how
   V3-EXQ-1051's replacement gate came to entail the criterion it protected (GFLAG-0330): its
   arms were a *strength* ladder (0 / 0.15 / 0.3 / 0.5), every arm of a seed sharing one
   trained snapshot and one pinned eval env, so the adjacent-arm gap is minimised at
   `excess = 1` -- per-observation minima 0.1304 / 0.1003 / 0.1026 -- and an
   `interior_occupancy >= 0.5` gate therefore *guarantees* every gap >= 0.0502 while C1 asked
   only for >= 0.03. C1's failure region lay strictly inside the region the gate already
   declared red.
3. **An occupancy gate and a gap criterion on the same rung ladder are not independent.** Pick
   one, or gate on something outside the ladder.
4. **Harm density / outcome mixture is NOT a valid dose variable, under either referent.**
   `E[f_sat]` is symmetric-unimodal in it (Line 2a), which is a property of the form and was
   not repaired by `9cba6c7`. Do not re-propose it. This is settled, not open.
5. **Set `use_closure_operator=True` explicitly, and assert it fired.** It defaults False. A
   fixture without it never calls `reset_outcome_history()`, so the FIFO fills and pins -- which
   has already produced one reported-then-withdrawn finding (Line 3). Any MECH-268 design whose
   variation is supposed to come from cadence must assert a non-zero closure count in-run, not
   assume it.

## Claim-level recommendation (propose only -- `claims.yaml` is governance's)

**Narrow MECH-268's text; do not open a substrate_queue ceiling entry against f_sat.**

1. **`functional_restatement` / `implementation_note`: say that the reciprocal-with-grace shape
   is an implementation choice, not the assertion.** The claim's own title already asserts a
   *property* ("caps and habituates ... does not grow unboundedly"), and the functional
   restatement already says "`f_sat` caps pe growth and introduces habituation" without
   committing to an algebraic form. Make that explicit so a future session cannot read the
   reciprocal as load-bearing, and record the reachable-set facts (<= `W-G+1` values; floor
   `1/(1+s(W-G))`) next to it, since they are what three designs tripped over.
2. **Add a scope line: MECH-268 is currently a claim about the SIGNAL, not about BEHAVIOUR.**
   The evidence bar should say so. The 2026-09-16 governance narrowing already went most of
   this way for V3-EXQ-729; Line 1 supplies the mechanism that makes it a permanent scope
   statement rather than a per-run caveat.
3. **Record the count-vs-run defect as a known limitation with a named failure signature**
   (Line 2). It is real, it is biology-grounded, and it should not be rediscovered.
4. **Two substrate_queue entries are owed -- against the CONSUMERS, not against f_sat:**
   - `candidate_effort` carries no cross-candidate information (`c.actions.shape[1]`, constant
     by construction), which makes the entire Shenhav EVC effort term argmin-invariant and
     `harm_interaction` identically zero. This is **complicated (buildable)** -- a real effort
     proxy (harm-forward rollout cost, already named as the intended refinement in the
     `agent.py:7536` comment) is a known build, and its blast radius is SD-032b as a whole, not
     MECH-268.
   - `dacc_pe`'s operating scale is uncalibrated against the mode register's critical value
     (~`external_task_bias`), measured at both ~0.99 and ~16-17 in different configurations.
     This is **complex (probe-gated)**: a spike is needed to establish what `pe`'s intended
     operating range *is* before anyone picks a normalisation, and until then it is a
     `puzzle (known rules)` -- the missing fact is a calibration target, not a reframing.

None of the four is a change to f_sat.

## Verdict on `chip-20260917-mech268-closure-cadence-dose`

**Yes -- it should proceed, and it is now the only viable dose variable of the three that have
been tried. It must be re-scoped to a signal-level DV.** No sequencing constraint remains: the
referent fix has landed (`9cba6c7`), and this design does not depend on it either way.

The chip's core measurement -- that closure cadence, not harm density, is what drives f_sat
variation in the live loop -- is correct, and is confirmed independently here (Line 3). Closure
cadence is not merely a better dose than harm density; it is the one that is left. Harm density
is arithmetically ruled out under both referents (Line 2a, design constraint 4), and the
strength ladder is ruled out by GFLAG-0330's entailment. Cadence is directly manipulable
(`reset_outcome_history`, the closure-firing predicate, the refractory window,
`closure_operator.py:~157`), it produces the wide `n_rec` sweep already measured, and it is
referent-independent.

**Its dose variable should be closure INTER-FIRE INTERVAL** -- the refractory window, swept to
give mean inter-closure intervals that straddle `W = 8` ticks (e.g. ~2, ~8, ~24) -- **and its
DV should be the distribution of `sat_factor` across the reachable rung set, pre-registered as
a distributional contrast (e.g. mean rung index, or occupancy of the bottom two rungs), not as
a gap criterion and not as an interior-occupancy gate** (design constraints 2 and 3). Expected
direction is unambiguous and falsifiable: long intervals let `n_rec` reach the window length
and concentrate mass at the floor; short intervals re-enter at `f_sat = 1.0` before the grace
is exhausted and concentrate mass at the ceiling. That would be the first ecological
gradedness evidence MECH-268 has -- which is exactly the bar the 2026-09-16 governance
narrowing left open.

**What it must not do is carry a behavioural DV.** Line 1 shows there is no behavioural
quantity `sat_factor` can move today, so a behavioural arm would produce a fourth refusal for
the fourth different-looking reason. If the design is written that way, refuse it again.

## Work-graph routing

| item | class | why |
|---|---|---|
| MECH-268 claim-text narrowing | `complicated (buildable)` | governance edit; content specified above |
| count-vs-run defect in f_sat | `complicated (buildable)` | a run-length or volatility statistic is a known build; deliberately NOT proposed here (see the scope note below) |
| `candidate_effort` proxy | `complicated (buildable)` | the intended refinement is already named in-tree |
| `dacc_pe` calibration vs mode register | `complex (probe-gated)` -> `puzzle (known rules)` | needs a spike to fix the operating-range target; then a known fix |
| closure-cadence dose experiment | `complicated (buildable)` | re-scope as above and queue via `/queue-experiment` |
| which dACC channel saturates (pe / surprise / commitment) | `mystery (known data)` | the lit-pull's own residual; Quilodran's transfer finding suggests the framing, not the data, is what is missing |

**Scope note, stated because it is the specific error the last two days of red-team refusals
have been preventing:** the count-vs-run defect is recorded above as a limitation and routed as
buildable, but **this document does not recommend changing f_sat now.** A form change would be
premature while both of f_sat's consumers are inert -- there would be no way to tell whether it
helped. Fix the consumers first; then the form question becomes measurable, and the count-vs-run
finding is waiting for whoever asks it.

## Method

Read-only throughout; `ree_core` unmodified. Three probes, all on a live `REEAgent` built with
V3-EXQ-729's configuration in `CausalGridWorldV2` (8x8, 8 hazards):

1. **Consumer A sweep** -- 120 ticks at `dacc_weight` 0.0 and 1.0; captured per-tick
   `candidate_effort`, `mode_ev`, `pe_unsaturated`, `control_required`, the applied dACC bias
   and `e3.last_scores`; recomputed the E3 argmin at all 7 reachable f_sat values.
2. **Consumer B sweep** -- 160 ticks; captured the salience coordinator's full input-signal
   dict per tick; recomputed `operating_mode`, `salience_aggregate` and `mode_switch_trigger`
   at all 7 reachable f_sat values, for `dacc_saturation_strength` in
   {0.3, 0.5, 1.0, 3.0, 10.0}.
3. **Order-sensitivity and mixture-response** -- exhaustive enumeration of all 2^8 outcome
   streams against a reimplementation of `_saturation_factor`'s arithmetic, plus 20,000-sample
   Monte Carlo of `E[f_sat]` vs base rate under both the current-class referent (live) and a
   hypothetical fixed-class referent (for contrast only -- it is not what `9cba6c7` installs).

The three probe scripts are short and self-contained; they are not landed in `ree-v3`
(this investigation is read-only on the substrate) and are reproducible from the specification
above. Probes 1 and 2 build the agent exactly as `_build_agent` in
`experiments/v3_exq_729_mech268_dacc_saturation_liveloop.py` does, adding only `dacc_weight`.

**Limitations, stated rather than papered over.**
(a) Probes 1 and 2 ran on an **untrained** agent. A P0-warmup (budget 120, V3-EXQ-729's value)
replication of probe 2 was started and is **NOT reported here** -- it did not finish inside this
session's budget. It is **owed**, and it is the one check that could qualify Consumer B's
result, because `pe`'s operating scale is what training moves. Re-run:
`/opt/local/bin/python3 scratch/ree_fsat_trained.py` per the reproduction note below. Consumer
B's conclusion should be read as established for the untrained regime and *indicative* for the
trained one -- with the caveat that the trained regime documented in-tree (`dacc_pe ~16-17`)
sits even further from the critical value, i.e. training moved `pe` the wrong way for f_sat to
act.
(b) Consumer A's conclusion does **not** depend on training: it follows from
`candidate_effort` being the rollout horizon, which is a structural property of the generator.
(c) The `pe ~16-17` figure for the opposite calibration regime is quoted from the
`salience_coordinator.py` source comment (V3-EXQ-464d/467d substrate), not re-measured here.
(d) No conclusion here is conditional on the outcome-class referent. `9cba6c7` landed while
this investigation was running; symmetric-unimodality is a property of the form and survives it
(Line 2a), and the order-insensitivity table is referent-invariant by construction.
(e) `pe` reaches `salience_aggregate` twice in the live config -- directly
(`salience_weights["dacc_pe"] = 1.0`) and through `dacc_foraging = max(0, pe - pe_ema)` at
weight 0.5. Probe 2 re-scales only the direct path and holds the recorded `dacc_foraging`
fixed, which *understates* how far saturation pushes `salience_aggregate` down. Since the
measured effect was already zero in the direction that matters, correcting it would not change
the conclusion; it would strengthen it.
