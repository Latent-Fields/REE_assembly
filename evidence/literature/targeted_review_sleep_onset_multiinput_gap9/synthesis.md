# Sleep onset as multi-input convergence -- synthesis against `sleep_substrate:GAP-9`

> Created: 2026-08-14
> Chip: `chip-20260812-sleep-onset-multiinput-litsynth`
> Type: **CONSOLIDATION-synthesis**, not a from-scratch pull. Most of the
> circadian / homeostatic / adenosine / local-SWA grounding already exists in
> this repo and is cited here rather than re-derived. Seven new entries were
> added only for the two topics confirmed absent from the corpus (see
> "Absence check" below).
> Primary consumer: **`chip-20260813-sleep-gap9-trigger-build`** (open) -- the
> chip that has to pick a trigger design. This document is the input to that
> decision, and Section 6 is written as its brief.

---

## 0. Scope and question

`sleep_substrate:GAP-9` (registered 2026-08-12) establishes that REE's sleep
trigger is **boundary-only** and therefore structurally unreachable inside a
true single-continuous life, and names three candidate mechanical fixes:

- **(a)** a step-count / time-based within-life trigger
- **(b)** a fatigue / prediction-error-burden trigger reusing GAP-5b's
  `SD-MEL-CONSUMER` accumulator
- **(c)** an experimenter-inserted "virtual boundary" at a configured step
  interval

The choice is registered as an open **architectural decision**, not an
empirical unknown. This synthesis asks three things of the biology:

1. Does the literature support a single global "sleep drive" scalar, or
   several converging / competing accumulated-need processes?
2. Which of (a)/(b)/(c) is best grounded -- and does a combination beat a
   single winner?
3. Should sleep *permission* be gated on safety / predicted future harm,
   as a thing distinct from cadence and timing?

---

## 1. Absence check (what was genuinely missing)

Confirmed by grep over `evidence/literature/` before any new search:

| Topic | Corpus state before this pull |
|---|---|
| Circadian + homeostatic two-process | **present** -- `targeted_review_inv_050/` (Borbely 1982) |
| Process S / adenosine accumulator | **present** -- `targeted_review_fatigue_vs_helplessness_dissociation/` (Borbely 2016) |
| Two-bound leaky stop-and-recover accumulator | **present** -- same dir (Meyniel 2013) |
| Local use-dependent SWA (learning -> local sleep intensity) | **present** -- `targeted_review_connectome_mech_180/` (Huber 2004), `targeted_review_inv_050/` (Rasch 2013) |
| Arousal / orexin kinetics | **present** -- `targeted_review_sd_037_orexin_kinetics/` |
| Predation-risk allocation (for **foraging**) | **present** -- `targeted_review_arc_062_refuge_forage_ecology/` (Lima & Bednekoff 1999) |
| **Local sleep as a distributed regulatory unit** (vs one global scalar) | **ABSENT** -- added here (Krueger 2008, Vyazovskiy 2011) |
| **Safety / predation gating of sleep permission** | **ABSENT** -- added here (Lima 2005, Rattenborg 1999, Loftus 2022, Tamaki 2016) |
| **Sleep onset as a bistable switch with an external stabiliser** | **ABSENT** -- added here (Saper 2010) |

The Lima & Bednekoff 1999 risk-allocation entry already in the corpus is
load-bearing for Section 5 and is **re-used, not re-pulled** -- it was
originally pulled for ARC-062 foraging allocation, and this synthesis is the
first artifact to transfer it to sleep.

Adjacency check: `chip-20260812-mech303-sourcing-mode-reconciliation` (done)
and `chip-20260812-mech303-threshold-sourcing` (open) own the MECH-303 safety-
signal-sourcing question. Section 5.2 below deliberately **does not** re-do
that work; it identifies a *second consumer* of the same signal that those
chips do not cover, and hands it to them.

---

## 2. Verdict 1 -- sleep drive is NOT one global scalar

The chip asked this not to be assumed. The literature is clear, and the answer
is **no**: sleep onset is driven by several inputs that are not
inter-substitutable, and they are not even all the same *logical type*. Three
types, at least four inputs:

### Type A -- accumulated need (integrates over time, additive)

- **Process S / adenosine** (Borbely 1982; Borbely 2016, both in corpus). A
  genuine scalar accumulator with an exponential offline discharge. This is
  the one input that a single global scalar *does* describe correctly.
- **Learning demand / MEL** (INV-050's third drive; Walker 2004, Rasch 2013,
  Huber 2004, all in corpus). Empirically separable from time-awake: Huber's
  visuomotor-adaptation subjects showed SWA elevation localised to the trained
  cortex, absent in a movement-matched no-learning control, with the magnitude
  predicting overnight gain.
- Critically, **Type A is not one variable, and its second member is not even
  scalar**. Huber's effect is *topographic*. Krueger 2008 (new) takes this to
  its conclusion: sleep is "a fundamental property of neuronal networks and is
  dependent on prior activity in each network", with whole-organism sleep an
  **emergent property of local units synchronising**, not a global set-point
  imposed top-down. Vyazovskiy 2011 (new) supplies the decisive observation:
  in sleep-deprived but behaviourally awake rats, *local* cortical populations
  go offline independently of the global state, and those local off-periods
  predict performance errors. Local units can be asleep while the organism is
  awake.

### Type B -- permissive gate / clock (does not accumulate; multiplicative)

- **Process C, circadian** (Borbely 1982). This is the input most often
  mis-described as a drive. It is a *gate*: a phase-locked window that does
  not integrate prior wake and is not discharged by sleep. Borbely's whole
  contribution was that C and S are different objects that must be composed.
- **Saper 2010** (new) supplies the mechanism: sleep-wake is a **flip-flop
  switch** built from mutual inhibition (VLPO vs the monoaminergic groups),
  which is sharply bistable but intrinsically *unstable*, and is held in place
  by orexin acting from **outside** the switch. Saper's own framing names
  three regulators of switching -- "homeostatic, circadian, and **allostatic**"
  -- which is exactly the three-type decomposition this section is arguing for,
  stated in the source literature.

### Type C -- allostatic / ecological override (context-dependent; can beat Type A)

- **Loftus 2022** (new) is the decisive empirical entry, and it is the single
  most important new source in this pull. Wild olive baboons, accelerometry +
  GPS: they **sacrificed sleep in less-familiar locations and when near more
  group-mates, regardless of how long they had slept the prior night or how
  much they had exerted themselves the preceding day**, and did **not**
  compensate with more intense sleep afterwards. That is a direct empirical
  refutation of a pure additive-drive-plus-threshold model in the ecological
  setting REE is trying to simulate: the accumulated need was measured, was
  present, and did not win.
- **Lima 2005** (new), the canonical review: the predatory environment is a
  determinant of sleep *architecture and timing*, and animals in risky
  environments spend less time in the most vulnerable sleep states. Risk
  reorganises sleep; it does not simply suppress it.
- **Rattenborg 1999** (new): mallards at the edge of a group raised
  unihemispheric slow-wave sleep from **12.4% to 31.8%**, and directed the
  open eye away from the group centre **86.2%** of the time. The risk response
  is *graded and steerable*, not a binary permit.
- **Tamaki 2016** (new): the human first-night effect is one hemisphere's
  default-mode network staying vigilant in a novel environment, with faster
  arousal to deviant stimuli on that side, gone by night two.

### The conclusion that matters for REE

**Do not build one global `sleep_drive` scalar and threshold it.** The
literature supports:

1. an accumulated-need family that is *spatially distributed*, whose global
   value is emergent rather than primitive (Krueger, Huber, Vyazovskiy);
2. a permissive gate/clock that is a **different object** from the need
   signal and must be composed with it, not summed into it (Borbely, Saper);
3. an allostatic risk term that can **override** (1) outright (Loftus), and
   whose expression is *graded and partial* rather than a veto (Rattenborg,
   Tamaki, Lima).

Types A and B compose multiplicatively (a gate times a drive). Type C is not a
third addend either -- it modulates *how much and how deeply*, and in the
limit it wins.

---

## 3. Code findings established this session (verified, not cited)

These were checked against `ree-v3` at `origin/main` and are load-bearing for
Sections 4 and 5. They are stated here because two of them materially change
how expensive GAP-9's candidate designs are.

**F1. The MEL accumulator is already per-step.**
`MELConsumer.note_step_pe()` (`ree_core/sleep/mel_consumer.py:111`) is called
once per **waking step** from `REEAgent.update_residue`
(`ree_core/agent.py:9696`). The accumulated learning-demand signal therefore
already exists at every step of a continuous life.

**F2. The decision site, not the signal, is boundary-bound.**
`MELConsumer.entry_permitted()` has exactly **one** call site in the entire
repo -- `ree_core/sleep/phase_manager.py:191`, inside `notify_episode_end()`.
So GAP-9 is a **call-site gap, not a signal gap**. This is the single most
useful finding in this document for the build chip: the expensive part of
design (b) (a per-step fatigue/PE accumulator) is *already built and already
running*; what is missing is a per-step evaluation.

**F3. `entry_permitted()` already implements the composition of (a) and (b).**
Its body is `crossed or at_ceiling` -- fire when accumulated MEL crosses
`mel_entry_threshold`, **or** when the K counter hits its ceiling, the latter
documented in-source as a "safety backstop so sleep is never starved
indefinitely". The composed design recommended in Section 4 is therefore not a
new mechanism; it is the existing function with `episodes_since_sleep`
re-based onto steps.

**F4. A safety-gated sleep-permission architecture already exists in code,
default-off.** `evaluate_sleep_onset_permit()`
(`ree_core/sleep/sleep_onset_gate.py`, MECH-286, `use_mech286_sleep_onset_gate`
default `False`) implements a three-condition AND:
`override < theta_sleep_permit` AND `max staleness > theta_sleep_recruit` AND
`z_harm_a.norm() < threat_tonic_threshold`. It is evaluated inside
`_run_cycle()`, so it applies to `force_cycle()` as well as to
`notify_episode_end()`.

**F5. MECH-286's threat term reads the same signal MECH-303 was shown not to
be able to discriminate safety with.** MECH-286's `threat_ok` is
`z_harm_a.norm()`; `docs/architecture/mech_303_contextual_safety_terrain.md`
line 52 gives MECH-303's monitored quantity as `harm_norm = z_harm_a.norm()`,
the same expression. V3-EXQ-917 measured chance-level (coin-flip)
discrimination between safe and unsafe places at every threshold tested, and
`chip-20260812-mech303-sourcing-mode-reconciliation` confirmed the cause is
SD-022's intentional `damage_sourced` re-sourcing decoupling the signal from
place context. See Section 5.2.

---

## 4. Verdict 2 -- weighing GAP-9's three candidate designs

### 4.0 First, (c) is not a design candidate -- it is the control condition

Design (c), an experimenter-inserted virtual boundary, has **no biological
referent at all**. There is no organism in which an experimenter inserts the
sleep trigger; that is a description of an *instrument*, not a mechanism. It
also already exists: `force_cycle()` is exactly this, and
`chip-20260812-causal-sleep-deprivation-matched-arm-design` (open) is already
built around using it.

This is a reclassification, not a rejection. (c) is the **right tool for the
causal experiment** -- it is how you ask "does a sleep cycle at this point in
this life change anything", holding everything else fixed -- and it is the
wrong thing to call an emergent trigger. Choosing (c) as *the* GAP-9 fix would
leave the substrate with no autonomous within-life trigger while appearing to
close the gap. Recommend: keep (c), name it as instrumentation, and do not
count it as closing GAP-9.

One caveat the build chip must not miss, from F4: because the MECH-286 gate
sits inside `_run_cycle()`, a `force_cycle()`-driven virtual boundary is
**still subject to it** when that flag is on. A matched-arm causal design that
enables MECH-286 can therefore have its injected cycles silently refused.

### 4.1 (a) step-count / time-based -- well grounded, but as Process C, not as need

A fixed-interval within-life trigger is a real biological object: it is
**Process C**, the circadian pacemaker. It is phase/time-driven, does not
integrate prior activity, and is not discharged by sleeping. So (a) is not
"the atheoretical cheap option" -- it is a faithful implementation of one of
the two processes in the canonical model.

What it is *not* is a need signal. A pure step-count trigger implements the
gate half of Borbely and omits the homeostatic half entirely: sleep would fire
on a metronome regardless of whether anything had been learned or any error
accumulated. Every consumer GAP-9 exists to unblock (MECH-204 recalibration,
the Phase B-E aggregation cluster, GAP-5b duration scaling) is a
*consolidation* consumer whose demand is exactly the thing a metronome ignores.

**Grounding: strong, for what it is. As a sole trigger: incomplete.**

### 4.2 (b) MEL / fatigue accumulator -- best grounded as the need signal, but currently unfirable alone

(b) is Process S / INV-050's third drive, and it is the best-grounded of the
three as a *need* signal: Borbely 2016 for the homeostatic accumulator shape,
Meyniel 2013 (in corpus) for the two-bound leaky-accumulator computational
form, Huber 2004 and Rasch 2013 for learning-demand specifically calibrating
offline resources. Per F1/F2 it is also far closer to built than the GAP-9
registration implies.

It has one decisive practical problem, and it comes from this repo's own
evidence rather than from the biology. GAP-5b's `completed_note` records that
V3-EXQ-718a **validated the consumer and failed the ecological producer link**:
measured waking MEL was noise-level (~1e-5, scrambled with respect to novelty
level) because CausalGridWorldV2 converges too completely
(`conv_rel_drop ~0.98`) to sustain learning load. The re-derive brake has
fired and the ecological demonstration is re-parked.

Consequence: **a MEL-threshold trigger in the current test-bed would never
fire.** Design (b) adopted alone does not close GAP-9 in the environments REE
actually runs; it converts a structurally-unreachable trigger into an
empirically-unreachable one, which is harder to notice.

**Grounding: strongest of the three. As a sole trigger, in the current
environment: non-firing.**

### 4.3 The recommendation: (a) + (b) composed, which is what the code already does

The literature does not choose between a clock and an accumulator. Borbely's
1982 contribution *was* the composition -- neither C nor S alone reproduces
the sleep-timing data. Saper 2010 restates it at the circuit level, adding
that the switch needs an external stabiliser to keep the composition from
chattering.

So the answer to the chip's "does any combination make more sense than a
single winner" is **yes, and it is the only combination the source literature
actually endorses**:

> **Primary trigger = accumulated need (b), with a step-based ceiling (a) as a
> backstop that guarantees sleep is never starved.**

Three things make this the cheap recommendation rather than the ambitious one:

1. It is **already the shape of `entry_permitted()`** (F3): `crossed or
   at_ceiling`, with the ceiling already documented as an anti-starvation
   backstop. No new control logic is required.
2. The accumulator already runs per-step (F1), so the need signal needs no new
   plumbing.
3. It is **robust to the 718a producer failure**: when MEL is noise-level, the
   step ceiling carries firing and the substrate degrades gracefully to
   design (a); when a non-converging environment is eventually built, the same
   code starts firing on demand with no change. Design (b) alone has no such
   floor, and design (a) alone has no path to demand-sensitivity.

**Minimal diff for `chip-20260813-sleep-gap9-trigger-build`:**

- Add a per-**step** evaluation site for `entry_permitted()` on the waking
  path, alongside the existing `note_step_pe()` call
  (`ree_core/agent.py:9696` is the natural anchor -- the signal is already
  there).
- Re-base the ceiling from `episodes_since_sleep` / `cycle_every_k_episodes`
  onto a step counter / `steps_between_sleep_ceiling`. `entry_permitted()`'s
  signature is already `(counter, ceiling)` and needs no change.
- Keep `notify_episode_end()` exactly as-is, so multi-episode drivers stay
  bit-identical.
- Gate on a new default-`False` flag per the codebase's OR-only convention
  (GAP-3's `use_sleep_aggregation_cluster` precedent), so the default path is
  byte-identical.
- Report `mel_n_steps_accumulated` and which arm of the OR fired
  (need-crossing vs ceiling) as diagnostics -- without that, a run in which
  the ceiling silently carried 100% of firings is indistinguishable from a
  working demand-sensitive trigger. **This is the 718a failure mode
  re-appearing one level up, and it is the single easiest thing to get wrong.**

**What this recommendation deliberately does not do:** it does not make the
accumulated-need signal *local/topographic*, which Section 2 says the biology
supports (Krueger, Huber, Vyazovskiy). One global MEL scalar is a real
simplification against the literature. It is the right V3 simplification --
REE has no per-region sleep-need substrate and building one is a much larger
piece of work -- but it should be recorded as a known divergence rather than
quietly adopted. See Section 7.

---

## 5. Verdict 3 -- should sleep permission be gated on safety?

### 5.1 Yes, and the separation is already correct in code

The chip asks whether "safe enough to sleep" should be a thing distinct from
cadence and timing. The literature answer is unambiguous: **yes, and it is a
different logical type, not another addend** (Section 2, Type C). Saper 2010
names allostatic regulation of the switch alongside homeostatic and circadian;
Loftus 2022 shows the allostatic term overriding the homeostatic one outright
in the wild.

REE's substrate has already made this separation structurally (F4): MECH-286
is a *permission* object with its own flag and its own call site, distinct
from the K/MEL *cadence* objects. That is the right architecture and this
synthesis **ratifies** it rather than proposing anything new. The two open
questions are what the gate reads, and what shape its output should be.

### 5.2 The gate currently reads a signal shown to carry no place-safety information

This is the one genuinely new, falsifiable finding in this pull, and it is a
cross-thread one -- it is visible only from the sleep side and the safety side
together, which is why neither thread's own chips surfaced it.

Per F5: MECH-286's `threat_ok` term is `z_harm_a.norm() <
threat_tonic_threshold`. MECH-303 monitors the same expression, and V3-EXQ-917
measured its safe-vs-unsafe place discrimination at **chance level at every
threshold tested**, with `chip-20260812-mech303-sourcing-mode-reconciliation`
confirming the cause as SD-022's intentional `damage_sourced` re-sourcing
(a design decision, not a wiring bug) decoupling the signal from place context.

So if `use_mech286_sleep_onset_gate` were switched on today, its safety term
would be gating sleep permission on a signal known to be uninformative about
whether the agent is anywhere safe. It would behave as a near-constant offset
or as noise -- and, being ANDed, a near-constant offset in the wrong direction
silently converts the gate into either an always-permit or an always-refuse.

**This is not a duplicate of `chip-20260812-mech303-threshold-sourcing`**
(open), which is building a dedicated proximity signal for the MECH-303 gate.
It is the observation that **MECH-286 is a second, unnoticed consumer of the
same defective sourcing**, and should be re-pointed at whatever signal that
chip lands. Handing it over rather than duplicating it is the correct division
here.

Cheap falsifier, requiring no new instrumentation: `evaluate_sleep_onset_permit()`
already emits `mech286_z_harm_a_norm` and `mech286_threat_ok`, and
`v3_exq_891_mech286_sleep_onset_conjunction_signature.py` already evaluates the
gate per-cell. Correlate `mech286_threat_ok` against ground-truth local hazard
density across cells. Prediction: **no better than chance**, matching V3-EXQ-917.

### 5.3 The gate should be graded, not boolean -- and REE already has the lever

The literature is consistent and, on this point, unanimous across four
independent sources: the response to risk is **partial and graded**, never a
veto.

- **Rattenborg 1999**: 12.4% -> 31.8% unihemispheric sleep at the group edge.
  The bird did not stop sleeping; it changed *how* it slept and kept a
  vigilance channel open.
- **Tamaki 2016**: one hemisphere stays vigilant in a novel environment. Again
  partial sleep plus a retained watch, not suppression.
- **Loftus 2022**: baboons in unfamiliar locations slept **less**, not zero,
  and did not compensate.
- **Lima 2005**: risk reorganises sleep architecture and timing; risky-
  environment species spend less time in the *most vulnerable* states.

And the decisive argument against a hard AND-gate comes from the corpus's own
Lima & Bednekoff 1999 risk-allocation entry, transferred from foraging to
sleep for the first time here. Its prediction (2) is that under **chronic**
high risk, antipredator effort *drops*, because the animal must feed sometime.
Transferred: **a hard boolean safety gate starves sleep exactly in the worlds
where the agent spends its life in danger** -- and by the same token a run in a
persistently hazardous environment would show sleep never firing, which reads
as a broken trigger rather than as a modelled trade-off. Real animals
reallocate; they do not abstain.

Recommendation, and it is cheap because the lever exists: **route the safety
term into the sleep-cycle DURATION factor, not (only) into a boolean permit.**
`MELConsumer.scale_steps()` already scales `sws_consolidation_steps` and
`rem_attribution_steps` by a clamped continuous factor. A threat term
multiplying that factor gives "sleep, but more briefly and less deeply, under
risk" -- which is what all four sources describe -- with no new mechanism, and
degrades to the current behaviour at factor 1.0.

If a boolean permit is retained at all, it should be the *outer* backstop
(catastrophic threat only, threshold set high), with the graded term doing the
ordinary work. That is Saper's architecture: a sharp bistable switch, plus a
continuous stabiliser acting from outside it.

### 5.4 Current harm vs predicted future harm

The organism-review Section 8 question -- should "safe enough to sleep" depend
on **predicted future** harm rather than current harm level -- gets a clear
directional answer and an honest cost estimate.

**The literature says predicted.** Lima & Bednekoff's risk allocation is
inherently predictive: deciding to abstain *now* is only rational against an
expectation of a future low-risk window, which is why the load-bearing variable
is the *contrast between windows* rather than the current level. Loftus 2022's
baboons responded to **location unfamiliarity** -- an expectation about
unobserved risk, not a measurement of present harm; nothing was attacking them.
Tamaki 2016's first-night effect is the same thing in humans and disappears by
night two, i.e. it tracks a *predictive* state that updates with experience,
not a current-harm reading. And the anticipatory-sleep-banking literature shows
sleep being taken in advance of *predicted* future opportunity loss.

Current harm is in fact close to the **worst** available proxy: an agent that
is being harmed right now is, definitionally, not in a state where the decision
"should I sleep" is live. The interesting cases -- the ones all four ecological
sources are about -- are precisely those where current harm is **zero** and the
question is whether it is *about to stop being* zero.

**But the honest cost:** REE has no forward risk model wired to this. Building
one is squarely the MECH-303 / SD-051 / SD-065 / SD-066 safety-abstraction
thread, not a GAP-9 sub-task, and GAP-9's build chip should not be made to wait
on it. Recommended sequencing:

1. **Now (GAP-9 build chip):** land the trigger per Section 4.3. Do **not**
   enable MECH-286 as part of it -- per 5.2 its safety term is currently
   uninformative, and enabling it would confound the first true-single-life
   sleep run with a defective gate.
2. **Next (cheap, no new substrate):** re-shape the MECH-286 threat term from
   boolean-AND to a graded duration multiplier per 5.3.
3. **Then (blocked on the MECH-303 thread):** re-point the threat term at
   whichever place-safety signal `chip-20260812-mech303-threshold-sourcing`
   lands, and only then move from current to predicted harm.

Steps 1 and 2 are `complicated (buildable)`. Step 3 is genuinely gated on
another thread's output, and should be recorded as such rather than attempted
here.

---

## 6. Brief for `chip-20260813-sleep-gap9-trigger-build`

Condensed, so the build chip does not have to re-read this document:

1. **Choose (a)+(b) composed, not one of the three.** Primary = MEL/need
   crossing; backstop = step-count ceiling. This is the only shape the source
   literature endorses (Borbely two-process; Saper switch-plus-stabiliser).
2. **It is smaller than the GAP-9 registration implies.** The accumulator is
   already per-step (F1) and `entry_permitted()` already implements
   `crossed or at_ceiling` (F3). The gap is a **call site**, not a signal.
3. **Re-base the ceiling from episodes to steps**; leave `notify_episode_end()`
   untouched so multi-episode drivers stay bit-identical; new default-`False`
   flag per the GAP-3 convention.
4. **Emit which arm of the OR fired.** Without it, a run where the ceiling
   carried every firing looks identical to a working demand-sensitive trigger
   -- this is V3-EXQ-718a's failure mode re-appearing one level up.
5. **Expect the ceiling to carry firing in CausalGridWorldV2.** Per GAP-5b,
   measured MEL there is noise-level. That is not a bug in the trigger and
   should not be diagnosed as one.
6. **Do not enable `use_mech286_sleep_onset_gate` in the validation run.** Its
   threat term currently reads a signal with chance-level place-safety
   discrimination (Section 5.2); enabling it would confound the first
   true-single-life sleep result.
7. **Do not count design (c) as closing GAP-9.** It is instrumentation
   (`force_cycle()`, already used by
   `chip-20260812-causal-sleep-deprivation-matched-arm-design`), and note that
   MECH-286, if on, gates `force_cycle()` too (F4).

---

## 7. Known divergences from the biology, recorded deliberately

Stated so they are adopted knowingly rather than by omission:

1. **One global MEL scalar, where the biology is topographic.** Krueger 2008,
   Huber 2004 and Vyazovskiy 2011 all describe sleep need as a property of
   *local* units, with the global state emergent. REE has no per-region
   sleep-need substrate. Recommended as the correct V3 simplification, flagged
   as a V4 target. Note this is not merely cosmetic: local sleep need is what
   makes *partial* sleep (Section 5.3) mechanically natural, so the global-
   scalar simplification and the graded-safety recommendation pull against each
   other -- the duration lever is the V3 stand-in for a mechanism the biology
   implements spatially.
2. **No circadian phase.** Design (a)'s step ceiling is an interval, not a
   phase-locked oscillator; it has no notion of a time-of-day-appropriate
   window. Acceptable -- REE has no day/night environment -- but it means (a)
   is a weaker Process C than the label suggests.
3. **Current-harm safety term, where the biology is predictive** (Section 5.4).
   Sequenced, not solved.
4. **No unihemispheric / partial-sleep capability.** Rattenborg 1999 and
   Tamaki 2016 both describe the risk response as *keeping part of the system
   awake*. REE's sleep is whole-agent. The duration/depth lever is the nearest
   available approximation.

---

## 8. Proposed candidate claim -- NOT REGISTERED

**Status: PROPOSED ONLY. Nothing in this section has been written to
`claims.yaml`.**

A genuinely new falsifiable statement did emerge (Section 5.2), so per the
chip's instruction a candidate registration is warranted. It was **not**
written, because `task_claim.py open` returned an **exit-3 arbitration verdict
on `REE_assembly/docs/claims/claims.yaml`**: the owning session is
`igw-auto-igw-217-substrate-ready-sd-queue-seed-en-20260813T183630Z`
(claimed 2026-08-13T18:36:30Z, not stale at the time of this work). Per
CLAUDE.md the non-owner stops. This section is the handover.

> **Candidate: MECH-286's sleep-permission threat term is sourced from a
> place-safety-uninformative signal.**
>
> *Statement:* MECH-286's third gate condition (`z_harm_a.norm() <
> threat_tonic_threshold`) reads the same quantity MECH-303 monitors, which
> V3-EXQ-917 measured at chance-level discrimination between safe and unsafe
> places. Therefore, with `use_mech286_sleep_onset_gate` enabled, the
> `threat_ok` term does not gate on safety: it behaves as a near-constant
> offset or as noise, and because it is ANDed, converts the gate into an
> effective always-permit or always-refuse rather than a safety gate.
>
> *Falsifier:* correlate `mech286_threat_ok` (already emitted) against
> ground-truth local hazard density across cells, using the existing per-cell
> evaluation harness in
> `ree-v3/experiments/v3_exq_891_mech286_sleep_onset_conjunction_signature.py`.
> The claim is **refuted** if `threat_ok` discriminates hazardous from
> non-hazardous cells above chance; **supported** if it does not, or if it is
> invariant across the hazard gradient.
>
> *Relations:* `depends_on` MECH-303 sourcing; second consumer of the defect
> that `chip-20260812-mech303-threshold-sourcing` is addressing;
> `bears_on` MECH-286, MECH-303, SD-022, `sleep_substrate:GAP-5`.
>
> *Type:* substrate-defect / consumer-sourcing, not a mechanism hypothesis.

A second, weaker candidate is **not** proposed, deliberately: "sleep permission
should be graded rather than boolean" (Section 5.3) is design-informing and
well-grounded, but it states a preference rather than a falsifiable prediction
about REE's behaviour, and forcing it into claim shape would misrepresent it.

---

## 9. Entries added by this pull

| Entry | Source | Year | Direction | Confidence | Role |
|---|---|---|---|---|---|
| `2026-08-14_gap9_local_sleep_awake_vyazovskiy2011` | Vyazovskiy et al., *Nature* | 2011 | supports | 0.88 | Local units sleep independently of global state |
| `2026-08-14_gap9_neuronal_assembly_sleep_krueger2008` | Krueger et al., *Nat Rev Neurosci* | 2008 | supports | 0.85 | Global sleep emergent from local units |
| `2026-08-14_gap9_predation_risk_sleep_lima2005` | Lima, Rattenborg, Lesku & Amlaner, *Anim Behav* | 2005 | supports | 0.90 | Risk shapes sleep architecture + timing |
| `2026-08-14_gap9_unihemispheric_predation_rattenborg1999` | Rattenborg, Lima & Amlaner, *Nature* | 1999 | supports | 0.90 | Graded, steerable, partial sleep under risk |
| `2026-08-14_gap9_ecological_override_homeostasis_loftus2022` | Loftus, Harel, Nunez & Crofoot, *eLife* | 2022 | supports | 0.92 | Ecological pressure overrides homeostatic drive |
| `2026-08-14_gap9_first_night_effect_nightwatch_tamaki2016` | Tamaki, Bang, Watanabe & Sasaki, *Curr Biol* | 2016 | supports | 0.87 | Novel-environment vigilance; local + predictive |
| `2026-08-14_gap9_sleep_state_switching_saper2010` | Saper, Fuller, Pedersen, Lu & Scammell, *Neuron* | 2010 | supports | 0.90 | Bistable switch + external stabiliser; allostatic |

Re-used from the existing corpus without re-pulling: Borbely 1982, Walker 2004,
Rasch 2013 (`targeted_review_inv_050/`); Borbely 2016, Meyniel 2013
(`targeted_review_fatigue_vs_helplessness_dissociation/`); Huber 2004
(`targeted_review_connectome_mech_180/`); Lima & Bednekoff 1999
(`targeted_review_arc_062_refuge_forage_ecology/`); the SD-037 orexin parameter
anchors (`targeted_review_sd_037_orexin_kinetics/`).

---

## 10. One-line verdict

Sleep onset is **not** one global scalar: it is an accumulated need (spatially
distributed in biology, one scalar in REE), composed with a permissive
gate/clock, and overridable by an allostatic risk term whose expression is
**graded and partial rather than a veto**. GAP-9 should therefore adopt
**(a)+(b) composed** -- MEL need with a step-count backstop, which is already
the shape of `entry_permitted()` and is a call-site change rather than a new
mechanism -- treat **(c) as instrumentation, not a trigger**, and keep sleep
*permission* separate from cadence, as the substrate already does; but the
existing MECH-286 permission gate should be left **off** for the first
true-single-life run, because its threat term reads a signal already measured
at chance-level place-safety discrimination, and should later be re-shaped from
a boolean AND into a graded duration multiplier and re-pointed at a properly
sourced safety signal.
