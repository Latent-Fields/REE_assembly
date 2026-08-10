# Synthesis: Is Competence-via-Long-Life-Experience-and-Practice (Plus Value-Gated Sleep) Actually Tested?

**Generated:** 2026-08-10T15:46:40Z
**Type:** cross-cutting synthesis, direct continuation of the 2026-08-10 `/governance` fishtank-lineage
cycle. Prompted by a direct user question after that cycle closed: has REE actually tested the
hypothesis that competence is achieved through long life (as the time-budget for accumulating
experience and practice) plus practice itself, refined by recurrent sleep cycles following valuable
experience -- and does REE need inference/rule-creation mechanisms before competence is achievable
at all?
**Scope:** claim-free synthesis connecting existing findings; proposes nothing new to build, only
clarifies what is and is not tested and why. No new experiment queued here.

---

## 0. Duplication check

Searched `evidence/planning/*.md` for "practice", "long life", "lifelong", "value-gated sleep" --
no prior document poses this exact integrated question. The pieces it connects are individually
well-documented (competence_floor / conversion_ceiling_root hypothesis-space entries, MECH-357,
MECH-309, MECH-322, the 906-lineage organism review) but nowhere previously assembled into one
answer to "is this specific causal chain tested."

---

## 1. The critical architectural fact the four fishtank documents never state explicitly

**The 906-lineage "life" is post-training evaluation on a FROZEN policy.** Read directly,
`experiments/v3_exq_906b_full_stack_observational_fishtank.py:775-781`:

```python
diag = _run_curriculum(agent, scheduler, device, seed, total_eps)   # TRAINING -- policy updates here
...
ree = _observational_run(agent, eval_env, eval_eps, eval_steps, seed)  # EVAL -- torch.no_grad()
```

`_observational_run()` -- the function that produces every episode log, every segment, every
"life" the two organism-level reviews and this session's autopsies analyzed -- runs entirely under
`torch.no_grad()`. Curriculum training (Stage-0/0b/P0/Stage-H/P1 + harm-pathway co-training)
happens **once, before** the observed life begins, and produces the frozen policy weights the
observed segments then execute against. **No gradient update, and therefore no weight-based
learning, occurs during any of the segments the organism review's Section 7 within-lifetime
development test, or this session's autopsies, examined.**

This is a load-bearing fact for the user's question. Their hypothesized chain -- long life as a
time-budget, filled with experience and practice, refined by sleep -- implicitly assumes something
changes about the agent's competence *during* the observed life. In a frozen-policy eval, the
*policy* cannot be that something. Section 7's within-life "improvement" pattern (declining harm,
rising benefit across 906b's 8 segments), even setting aside its own confound (Section 2 below),
could never be attributed to synaptic/weight learning under this design -- it would have to come
from somewhere else.

## 2. What CAN change within a frozen-policy life, and what already exists to test it

Not everything is frozen. `agent.py` `reset()` (per the organism review's own Section 1, re-verified
this session) explicitly PERSISTS across non-zero episode boundaries: the residue field's
accumulated valence state, the hippocampal exploration/memory buffer, theta-buffer/z_self/z_world
continuity, sleep-machinery cadence state, dACC/salience/coalition state. These are non-parametric --
they update via plain arithmetic (EMAs, buffer appends, accumulator increments), not backprop, so
they run fine under `torch.no_grad()`.

**MECH-357's `avoidance_efficacy` is the most direct existing instance of this class, and it is
explicitly designed to be exactly what the user is describing.** Read directly,
`ree_core/pfc/infralimbic_avoidance_gate.py`:

```python
self._avoidance_efficacy += lr * (1.0 - self._avoidance_efficacy)   # credited: directed action under threat reduced z_harm_a
self._avoidance_efficacy -= leak * self._avoidance_efficacy          # decayed: freeze / failed avoidance
```

No `self.training` gate, no `.eval()`/`.train()` check -- a plain Python float update, confirmed to
run during the frozen-policy eval. The module's own docstring (line 169) states outright:
"avoidance_efficacy -- developmental acquisition persists across episodes." **This is REE's actual
built candidate mechanism for the user's hypothesis**: practice (repeated directed action under
threat) building competence (better avoidance) across a lived episode, entirely without weight
updates -- a form of within-life, memory-based skill acquisition rather than gradient-based
learning.

**It has never had a fair test.** Confirmed across V3-EXQ-603h (2026-06-07), 603k (2026-06-09,
diagnostic-level PASS only), 603r (2026-08-09), 603s (2026-08-10, this session): every combined-fix
attempt to isolate whether the gate *causes* better survival has been blocked by a different
environment-design confound each time (escape-affordance bridge missing; harm-pathway untrained;
harm-pathway-fix-alone rescuing the LESION arm; mobile-predator drift still not forcing genuine
discrimination). The mechanism engages (avoidance_efficacy has reached 0.633 in at least one run)
but whether that engagement *matters for survival* -- the actual test of "does practice build
competence" -- remains, after four attempts, undetermined by design defect, not by evidence against
the mechanism.

## 3. Sleep specifically after valuable experience -- the weakest-tested link

The user's hypothesis names sleep cycles *following valuable experience and practice* specifically,
not sleep generically. Two things exist in this space, neither the integrated test:

- **V3-EXQ-909** (this session's autopsy) tests sleep-mechanism *internal* diversity
  (`sws_slot_diversity`, `replay_diversity_index`) -- a different DV entirely from behavioural
  consolidation, with zero conceptual overlap (per `sleep_transition_investigation_906_lineage_2026-08-10.md`
  Section 4, read this session). It says nothing about whether sleep after valuable experience
  improves subsequent competence.
- **MECH-322** (`sleep_replay_value_conditioned_chunking_consolidation`, ARC-071's carve-out) is the
  one existing mechanism that is explicitly value-gated: it permits chunk formation from replayed
  sequences during sleep *only if* the replayed sequence carries a value-tag from prior
  real-executed episodes, with accelerated dissolution if not corroborated by real waking execution.
  This is architecturally the closest existing instantiation of "recurrent sleep cycles after
  valuable experience" -- but it is scoped to forming a reusable *action-sequence chunk*, not to
  general competence improvement, and its own evidence base is thin: one supporting run
  (V3-EXQ-873a, 2026-08-07), `v3_pending` still `true` ("single-run supports does not alone clear a
  v3_pending gate").

The already-chipped `chip-20260810-fishtank-developmental-ecology` (item 3, amended twice this
session) adds a sleep-vs-no-sleep ablation, but it tests generic behavioural reorganisation after
*any* sleep firing, not consolidation specifically gated on the value of what preceded it. It is the
right next step for the *sleep-vs-elapsed-time* confound, but it does not by itself test the
value-gating half of the user's hypothesis.

## 4. Direct answer to the user's question

**No, the integrated hypothesis -- long life as time-budget, filled with (MECH-357-style) practice,
consolidated by sleep specifically following valuable experience, producing measurable competence
-- has not been tested as a whole.** Every piece is in one of three states:

| Piece | Status |
|---|---|
| Long life as time-budget for experience | Real (up to ~4000 steps/life), but the within-life development test that would show its payoff (organism review Section 7) is confounded by per-segment environment re-randomisation |
| Practice building competence (MECH-357) | A genuine, already-built, non-gradient mechanism exists and is architecturally exactly right for this -- but has never had a fair test across 4 attempts (design-defect blocked, not evidence against) |
| Sleep after valuable experience -> competence | Almost entirely untested. The one value-gated sleep mechanism (MECH-322) tests chunk formation, not general competence, on a single supporting run |
| Competence measured as a trajectory over the life | No existing fishtank run reports this; `competence_floor`'s own `observation_bottleneck` (a DIFFERENT question, about retention of BC-installed competence) already states the general requirement: "a competence TRAJECTORY DV, not terminal" -- the same instrumentation gap applies here |

## 5. The user's second question: are inference mechanisms required before competence is achievable?

**This is not a speculative worry -- it is REE's best-evidenced finding in exactly this territory,
independent of anything this session did.** Two existing, heavily-tested claims say, in effect, yes:

- **MECH-309** (candidate, `substrate_ceiling`, 20+ confirmed ceiling-hit autopsies across the
  ARC-062/MECH-309 family, most recently corroborated this session by the 906b/906c/911 cluster):
  "Bayesian update and gradient descent revise weights over a hypothesis space they do not invent;
  without a non-Bayesian rule-creator that proposes discriminative policy modes... the trainer
  collapses to the smoothest single regime good-enough across the whole state space." This is
  exactly the user's worry, stated as REE's own working hypothesis and repeatedly corroborated: a
  parametric policy trained by gradient descent, however much experience it accumulates, does not
  *invent* new discriminative strategies on its own.
- **`conversion_ceiling_root`'s `H-f-dominance`** (alive, one of four live candidate roots for why
  a discriminative signal that DOES exist and DOES reach committed action still fails to diversify
  behaviour): even when the "right" modulatory signal is present, the trained action-value head's
  own argmax dominates the decision, so the signal is computed but not acted on. A second,
  independent line pointing the same direction as MECH-309.

Neither of these is about experience quantity -- both are about a structural property of
gradient-descent-trained selection. More lived time, more practice repetitions, or more sleep
cycles would not by themselves resolve either finding; both explicitly name the missing ingredient
as an inference/rule-creation layer, not a data quantity.

## 6. What would actually be needed to test the user's hypothesis cleanly, and why it is not built yet

An integrated test needs, at minimum: (a) layout continuity across segments (removes the
environment-luck confound -- already the first item of `chip-20260810-fishtank-developmental-ecology`,
not yet landed); (b) a MECH-357 pressure design that genuinely forces the LESION arm to fail its own
negative control (the open question `chip-20260810-mech357-pressure-scoping`, spawned this session,
was built to scope -- not yet landed); (c) a competence-trajectory DV logged per segment across the
life (not built anywhere yet); (d) ideally, extending MECH-322's value-gating principle from chunk
formation to a general post-sleep competence readout (not built, and MECH-322 itself is still thin
on evidence).

**Building this now would be premature** -- per this repo's own standing principle (the
developmental-ecology correction document's Section 7, and the organism review's own practice of
deferring every proposal to a single successor per confound rather than bundling): (a) and (b) are
independent prerequisites, neither landed, and a combined test run before either lands would be
uninterpretable on failure (is it the environment confound, the pressure design, or a genuine
absence of practice-driven competence?). This synthesis is recorded so the connection is not lost,
not to justify building ahead of its prerequisites.

## 7. What this document does NOT resolve

- Whether MECH-357's avoidance_efficacy, once fairly testable, will actually demonstrate a
  practice-competence link, or will itself hit the same F-dominance/rule-apprehension ceiling
  MECH-309/`conversion_ceiling_root` already describe for gradient-trained selection. Given
  avoidance_efficacy feeds into a score_bias (not the trained action-value head directly), it may
  be architecturally positioned to escape F-dominance -- but this is not established, only
  plausible.
- Whether extending MECH-322's value-gating to a general competence readout is the right design, or
  whether a simpler mechanism suffices -- not scoped here.
- The concrete instrumentation for a competence-trajectory DV -- left for whichever future session
  picks this up once (a) and (b) land.

## 8. Follow-on

Recorded as a target integrated test, contingent on `chip-20260810-fishtank-developmental-ecology`
item 1 (layout continuity) and `chip-20260810-mech357-pressure-scoping`'s eventual build both
landing -- not proposed as a near-term build. A new chip
(`chip-20260810-lifelong-practice-competence-synthesis`) is spawned as a standing reminder to connect
the two once both land, rather than being silently lost between two independently-tracked chips.
