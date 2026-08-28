Status: processed

Intake: evidence/planning/thought_intake_2026-08-07_responsibility_counterfactual_memory.md
Registered: MECH-485 (threshold-gated predicted-harm/confidence pipeline), Q-090 (leg-3 admission-criterion open question), INV-012 Leg 3 (retrospective retention + counterfactual evaluation + self-attribution -- added once the concurrent digestion session that owned INV-012 closed), MECH-487 (provenance-tagged retention buffer for rejected/uncommitted E3 candidates -- registered later the same day, 2026-08-07T19:47Z, once the dedicated lit-pull it was originally gated on landed: evidence/literature/targeted_review_uncommitted_candidate_retention/, 5 entries)

## The thought (user's own reasoning, session 2026-08-07, captured near-verbatim)

Prompted mid-session during `/thought-digestion` while correcting `INV-012`
("Responsibility arises through commitment, not prediction alone"). The
session had just added a "Leg 0" precondition to INV-012 -- that genuine
responsibility requires E3 to be selecting among differentiated candidate
futures at the moment of choice, not making a near-deterministic pick that
gets labeled "commitment" after the fact (this precondition is currently
unmet -- see MECH-439 F-dominance conversion-ceiling, `ceiling_decision:
exhausted`).

The user's line of reasoning, in the order it was raised:

1. "responsibility also depends on remembering the path unchosen within
   one's own personal memory / narrative"

2. "and being able to work out when harm could have been avoided and
   benefits / goals could have otherwise been achieved"

3. "all of that is needed to be able to say 'my choice was the reason for
   this', all probably linked with sense of self systems"

4. "and the whole personal or individual responsibility related systems
   would be a rich source of possible learning, one whereby imagined things
   can end up leaving a trace"

5. "a very important line to be able to walk -- as if the wrong things get
   pulled in you would get potentially positive feedbacks leading to hard
   learned delusions I would imagine"

6. "highlighting the importance of metacognitive systems again"

## Reading of the argument

Choosing among genuinely differentiated futures (Leg 0) is necessary but not
sufficient for responsibility. A further, distinct requirement is retrospective:
the agent must be able to (a) retain that an alternative existed and roughly
what it was, (b) evaluate counterfactually whether that alternative would have
avoided the harm actually incurred, or better achieved the goal actually
pursued, and (c) attribute the resulting outcome to *its own* choice
specifically, as opposed to circumstance -- and (c) is explicitly tied to
sense-of-self machinery, not just to a bare causal-attribution computation.

Point 4 reframes this as an opportunity, not just a requirement: if imagined/
counterfactual alternatives *could* leave some trace, that trace is a rich
learning signal -- essentially, learning from paths not taken, not only from
paths taken.

Point 5 is the load-bearing caution, and it's stated as a prediction about
failure mode, not just a vague worry: if the wrong kind of content gets
admitted into that learning loop -- i.e. imagined content treated with the
weight of real experience -- the system would get a *positive* feedback
signal reinforcing a belief that was never actually tested against reality.
Repeated, that is a plausible computational account of a hard-learned
delusion: not a one-off hallucination, but a confabulation that has been
reinforced into stability by its own imagined "confirmations."

Point 6 identifies why (5) is dangerous specifically as a *metacognitive*
failure: distinguishing "this happened" from "this was imagined, and I am
only using it to evaluate a counterfactual" is a second-order epistemic
judgment about the source and status of one's own mental content, not a
first-order judgment about the world.

## Architectural grounding found this session (read-only research, not applied)

Dispatched a research agent mid-session to check what currently exists.
Findings, for whoever picks this up next:

- **No mechanism retains rejected E3 candidates beyond the current tick, in
  any form.** `e3_selector.select()` scores every candidate but only the
  winner survives; the closest partial exception (`SD-033e`/`MECH-264`,
  frontopolar counterfactual-value tracking) reduces the best-unchosen
  alternative to a bare scalar (`cfv_now`), overwritten every tick, consumed
  once for a live switch-decision pressure term. Nothing about *which*
  alternative existed, or its content, survives past the tick it was
  computed on.
- **Counterfactual-attribution machinery exists but serves a different
  purpose.** `SD-003`/`MECH-276` (scientist-agent counterfactual-backed
  attribution) compute a causal-attribution signal ("did my action cause
  this outcome") for training, not for narrative recall of what could have
  happened instead.
- **The one place "regret" appears at all in the registry is `Q-028`**,
  proposing an unbuilt `MECH-402` (context-sensitive self/other comparator +
  moral residue, citing Williams 1965's "agent-regret") -- but scoped
  narrowly to a single self-vs-other axiom-conflict trade-off, V5-gated on a
  multi-agent substrate that doesn't exist, and not connected anywhere to
  E3's `select()`.
- **`MECH-292`/`MECH-293`** (ghost-goal bank) is memory for abandoned *goal
  locations*, not for rejected *action-trajectory candidates* at a specific
  decision point -- a different axis.
- **`ARC-085`** (autobiographical event-token substrate) is the one place
  that *could* eventually host this, but is V4/V5, unbuilt, and its current
  field schema (`committed_vs_imagined`, i.e. the MECH-094 provenance tag)
  does not include anything for "sibling alternatives considered and
  rejected here."
- **`MECH-094`** (this session's `INV-011` audit) is the existing, confirmed
  safety boundary directly relevant to point 5: it is deliberately strict --
  imagined/simulated content produces zero belief update in real-experience
  channels (residue, valence, hippocampal writes), specifically to prevent
  the confabulation failure mode the user is describing. The one bounded
  exception REE already has (`MECH-322`, the sleep-only ARC-071 chunking
  carve-out) is gated on prior *real*-episode value-tag, fires only in a
  designated offline phase, and carries an audit flag with accelerated
  dissolution if never corroborated by real execution -- i.e. REE already
  has a working template for "let a narrow, bounded exception through the
  imagination/reality gate, under audit," not an open door. Any future
  mechanism implementing points 1-4 above would need to be shaped the same
  way: bounded, audited, provisional-until-corroborated -- not a general
  relaxation of MECH-094.
- **`INV-033`** ("REE agents require second-order epistemic access to their
  own [epistemic states]") is the existing claim closest to point 6, and has
  not yet been digested this session (no `what_would_answer` yet).

## Possible affected components

- `INV-012` (responsibility through commitment) -- this is the direct
  extension point; adds a third requirement beyond the two already staged
  this session (Leg 0: differentiated choice; Leg 1: distinguishable
  write-mechanism).
- `SD-033e` / `MECH-264` (frontopolar counterfactual value) -- nearest
  existing mechanism; would need extension from a transient scalar to
  something retained and content-addressable if this is ever built.
- `SD-003` / `MECH-276` (counterfactual self-attribution) -- causal-
  attribution half of point 3 already has machinery; narrative-retention
  half does not.
- `Q-028` / `MECH-402` (moral residue, agent-regret) -- currently the only
  place "regret" is named; narrowly scoped, would need generalizing beyond
  the self/other axiom-conflict case to cover this.
- `ARC-085` (autobiographical event tokens) -- candidate eventual host
  substrate; V4/V5, unbuilt, schema would need a field for
  rejected-alternative content.
- `MECH-094` / `MECH-322` (imagination/reality write-gate + its one bounded
  exception) -- the safety-boundary precedent point 5 is worried about;
  whatever gets built here should follow MECH-322's shape, not loosen
  MECH-094 generally.
- `INV-033` (second-order epistemic access) -- point 6's connection; not yet
  digested, likely the natural home for the metacognitive framing.
- E3 (`ree_core/predictors/e3_selector.py`) -- would need a retention hook
  at `select()` if this is ever built (currently discards losing candidates
  outright).

## Addendum (same session, later): the "two memory types" framing

While reviewing wave 11 of `/thought-digestion` (specifically INV-021's drafted
falsifier, which lists "uncommitted exploratory evaluation leaving a lasting
trace" as a candidate write-pathway exception to check), the user restated the
above in a sharper, more general form:

> "Ree needs to remember what it does through committed action but also what
> it has thought but not committed to. Earlier work referenced this."

This is not quite the same question as points 1-6 above (which are about
responsibility specifically -- retaining WHICH alternative existed, evaluating
it counterfactually, attributing outcomes to self). It's one level more basic:
does REE have **two distinct memory types** at all -- (a) memory of what it
did (committed, real-consequence, already exists: hippocampal/residue writes
gated by MECH-094), and (b) memory of what it considered and did not do
(currently: nothing retains this past the tick it was computed on, per the
architectural-grounding findings above). Responsibility (points 1-6) is one
consumer of memory type (b) if it existed; it is not the only possible reason
to want it.

**"Earlier work referenced this" -- confirmed, this is
`[[feedback_imagination_learning_constraints]]`** (memory file
`project_imagination_learning_constraints.md`, surfaced 2026-05-10, session
`73bd79e3-6c91-4ba8-af2b-56b430db003d`). That memory's LICIT taxonomy already
names the adjacent category directly: "Counterfactual exploration -- explore
'what if' branches to surface implicit preferences without committing.
Plausibly licit but the surfaced preferences are *priors for future waking
testing*, not knowledge claims themselves." That entry answers the WHETHER
question (is retaining/using uncommitted-thought content licit at all, and
under what constraint) but stops short of specifying a MECHANISM -- it was
written as a candidate ARC/MECH/Q registration shape, explicitly "do NOT
register without dedicated lit-pull," and nothing has been registered since.

**Three independent surfacing points now on record for the same gap, none yet
converted into a registered claim:**
1. `project_imagination_learning_constraints.md` (2026-05-10) -- the
   LICIT/FORBIDDEN learning-from-imagination taxonomy; names "counterfactual
   exploration -> priors for future waking testing" as licit in principle.
2. This file's own "Architectural grounding" section (2026-08-07, earlier
   this session) -- confirms no mechanism retains rejected E3 candidates past
   the current tick; SD-033e/MECH-264 reduces to a transient scalar; ARC-085
   is the nearest eventual host substrate but is V4/V5, unbuilt, and its
   schema has no field for "sibling alternatives considered and rejected."
3. INV-021's `what_would_answer` Leg 1 (2026-08-07, wave 11, this session) --
   lists "uncommitted exploratory evaluation leaving a lasting trace" as a
   candidate exception to the claim that all durable updates occur at
   ARC-003 commit boundaries. If REE ever builds mechanism (b), INV-021
   itself would need to be re-evaluated: a durable trace of an uncommitted
   thought would be a counter-example to INV-021's exclusivity claim as
   currently stated, UNLESS such traces are explicitly typed as a distinct,
   non-responsibility-bearing update class (i.e. "durable but not
   commit-boundary-gated AND not responsibility-bearing" is a coherent third
   category INV-021 does not currently name).

**Confabulation-risk framing (points 4-6 above) applies here with equal
force, and MECH-322 is still the right template**, not a general relaxation:
whatever mechanism (b) looks like, it needs the same bounded/audited/
provisional-until-corroborated shape MECH-322 already demonstrates for the
one exception REE currently allows through the MECH-094 write gate.

## Addendum 2 (same session, later still): prospective use -- interrupting before harm, not just remembering after

The addendum above ("two memory types") separated *committed* memory from
*considered-but-not-committed* memory. The user's next point is about a third,
distinct use of the same underlying machinery -- not retrospective (attributing
responsibility after the fact) and not passive retention, but **prospective,
in-the-moment correction**:

> "When committed to a path and the predicted future brings high chance of harm
> (or indeed success) -- or a recently branched choice space does the same --
> this gives opportunity for fixing an error before it leads to harm or
> rerouting a course to get to goal. It does not need to await actual harm or
> goal to be comparing imagined futures."

Reading: this names two distinct trigger conditions for the same intervention:

1. **Already committed, mid-execution** -- ongoing forward prediction along the
   currently-committed trajectory crosses a harm (or success) threshold. This is
   a live re-evaluation of a path already locked in, not a pre-commit
   comparison among candidates.
2. **A newly branched choice space** -- a fresh decision point has just opened
   (new options exist that didn't before), and the same high-predicted-harm /
   high-predicted-success signal applies there too, independent of (1).

Both cases license the same action: **correct or reroute now**, using the
predicted (imagined) future as the trigger -- explicitly *not* gated on waiting
for the harm or the goal to actually materialize. The comparison is between
imagined futures, evaluated prospectively, not a comparison run only after an
outcome is known.

**"The fast interrupt may be of particular importance here" (user, flagged
explicitly).** This points at existing, already-registered architecture rather
than something new to invent from scratch:

- **`MECH-090`** (BetaGate) -- its own notes already describe exactly this
  shape: "Hyperdirect pathway (cortex->STN->GPi) provides fast interrupt for
  urgent stop-change without waiting for completion." I.e. REE already has a
  registered claim that action-selection updates need not wait for the
  currently-committed sequence to finish -- an urgent stop-change signal can
  break beta-gated suppression and let E3's (continuously-updating) internal
  model state propagate to actual action selection mid-sequence. This is case
  (1) above, nearly verbatim.
- **`MECH-141`** (tri-loop dual-timescale arbitration) -- makes explicit that
  this is architecturally a SEPARATE, faster pathway from ordinary evaluation,
  not a special mode of it: a slow proactive prefrontal-caudate pathway
  (seconds-scale, pre-sets gate bias ahead of time) plus a fast reactive
  hyperdirect STN pathway (milliseconds-scale, fires on an unexpected/urgent
  signal after commitment). MECH-141's own text warns that collapsing the two
  into one arbitration signal "loses the fast-interrupt capability" -- i.e. the
  speed is not incidental, it is the point: a slow deliberative re-evaluation
  loop cannot substitute for this pathway, because by the time it would fire
  the harm window may already have closed.
- **What neither MECH-090 nor MECH-141 currently specifies is the TRIGGER
  content**: both are about the existence and speed of the interrupt channel,
  not about what predicted-future comparison feeds it. The user's point here is
  that the trigger itself should be a live comparison of *imagined* forward
  trajectories against a harm/success threshold -- which is E2/E3 forward-
  prediction territory (`ree_core/predictors/e3_selector.py`, the same
  machinery discussed in the "Architectural grounding" section above for
  case (2), branch-point re-evaluation) feeding into the MECH-090/MECH-141
  interrupt pathway for case (1), mid-sequence re-evaluation. Whether that
  connection (predicted-harm/success magnitude -> hyperdirect interrupt
  threshold) already exists anywhere in the current substrate, or is itself the
  gap, was not checked this session -- flagged as a next step below rather than
  asserted either way.
- **Same confabulation caution as Addendum 1 applies, arguably more sharply
  here**: if the "predicted future" feeding the fast interrupt is itself
  poorly calibrated (a bad forward rollout, an unreliable E2 prediction), a
  fast, hard-to-veto interrupt pathway acting on it is a *more* dangerous
  failure mode than a slow deliberative one would be, precisely because its
  whole design point is to act before there is time for correction. Any future
  wiring of predicted-harm/success into MECH-090/MECH-141 would need its own
  non-degeneracy/calibration guard, analogous to MECH-094's role for the
  imagination/reality write gate discussed above -- not the same mechanism, but
  the same category of caution.

This addendum's relationship to Addendum 1 ("two memory types"): both are about
imagined/uncommitted content doing real work rather than being discarded --
Addendum 1 is about *retention* of rejected alternatives for later narrative/
responsibility use; this addendum is about *live* use of forward-predicted
futures to trigger a real-time interrupt. They may share representational
substrate (E2/E3 forward rollouts) but are functionally distinct consumers.

## Addendum 3 (same session, later still): what the comparison is actually against

Continuing directly from Addendum 2. The user's next point specifies what the
"imagined futures vs. harm potential" comparison implied there is actually made
*against*:

> "Implied is an ongoing comparison of imagined futures with harm potentials,
> which may need to compare to previous harms in some way and also comparing
> to goals, we may have some of this in the ghost goal and cue system."

Reading: Addendum 2 left the trigger content unspecified -- "predicted harm/
success magnitude" was named but not grounded in anything that produces that
magnitude. This point supplies two candidate grounding sources, both flagged
as *possibly already partially present* rather than asserted as complete:

1. **Comparison against previous harms** -- the closest existing claim is
   `MECH-131` (vmPFC-analog residue activation): residue (stored curvature
   over L-space, `ARC-013`) encodes past aversive experience, and MECH-131's
   specific requirement is that this stored history be *activated as an
   anticipatory forward-biasing signal at trajectory-evaluation time* --
   weighting E3 away from harm-associated trajectories *before* candidate
   generation, not only after. Its own biological grounding (Budhani 2006
   reversal learning; Bechara 1996 Iowa Gambling Task anticipatory SCR) is
   precisely about the failure mode of having the harm history stored but not
   activated into the live evaluation -- which is the gap Addendum 2 was
   circling without naming.
2. **Comparison against goals, via the ghost-goal / cue system** -- `MECH-292`/
   `MECH-293` (ghost-goal bank + waking probe search) plus their substrate
   `SD-039` (dual-trace anchor goal-snapshot payload) are, per their own
   2026-05-19 "retrieval-cue reframe," explicitly a **content-addressed cued-
   recall system**: z_goal/context acts as a cue, the SD-039 payload (goal
   snapshot + wanting/arousal payload, populated from `bla_output.arousal_tag`
   among other fields) is the stored trace, and `goal_match` is the cue-to-
   trace match score. This is architecturally close to what an "ongoing
   comparison" needs -- a live cue continuously matched against stored traces
   -- though its current scope is retrieving *stale/inactive anchors* whose
   goal-payload still matches a live goal, not evaluating *forward-predicted*
   trajectories against a harm/success threshold. Whether the same cue-
   matching machinery generalizes to case (1)/(2) in Addendum 2, or is a
   parallel system that would need its own wiring, is unresolved here.

Neither of these is confirmed to already do what Addendum 2 needs -- MECH-131
is candidate/unbuilt in this form, and SD-039's own `what_would_answer` (read
this session) records its retrieval/query level as *still open*, blocked on a
measured non-degeneracy precondition (z_goal cue collapse across goal-epochs,
V3-EXQ-889, 2026-08-03) that has not been resolved as of this writing. So the
honest state is: REE has two separate, partially-built pieces (anticipatory
harm-residue activation; goal-cued content-addressable retrieval) that
*could* compose into what Addendum 2 is describing, not a single mechanism
that already does it.

## Addendum 4 (same session, later still): the missing third option -- when the prediction itself is uncertain

> "Gosh. It also ties into the need more info systems that are not at all
> implemented I think."

Confirmed: **`MECH-482`** (epistemic_deficit: a persistent, target-bound
accumulator for unresolved, consequential, potentially-resolvable model
inadequacy) and **`MECH-483`** (orient/survey: a third primitive behavioural
regime, alongside approach and avoid, that widens sampling and gathers
information before committing, driven by MECH-482 rather than a specific cue)
are both `candidate/v3_pending/substrate_conditional`, registered 2026-08-05
from `docs/thoughts/2026-08-05_epistemic_deficit_and_orienting.md` -- genuinely
not built. `Q-089` (whether this explains the cold-start competence split) sits
on top of both, also unbuilt.

Why this connects here rather than being a separate topic: Addendum 2's own
confabulation caution left a gap -- "if the predicted future feeding the fast
interrupt is itself poorly calibrated... a fast, hard-to-veto interrupt
pathway acting on it is a *more* dangerous failure mode." That caution named
the danger but not the resolution. MECH-482/MECH-483 are the resolution
*shape*, even though unbuilt: they describe exactly the missing third option
between "trust the prediction, interrupt/reroute now" (Addendum 2/3, high
confidence) and "trust the prediction, do nothing" (ignore a genuinely
uncertain read) -- namely, when predicted harm/success is *uncertain* rather
than confidently high, the licensed response is neither of those, but a
distinct orient/survey regime: reduce commitment, widen sampling, gather
resolving information, THEN re-evaluate. This turns the earlier three
sub-threads into a single triage structure by predicted-harm confidence:

- **high-confidence high predicted harm/success** -> MECH-090/MECH-141/MECH-138
  fast-interrupt or cancel-window pathway (Addendum 2)
- **low-confidence / high epistemic_deficit** -> MECH-483 orient/survey, gated
  by MECH-482 (this addendum) -- gather information before committing to
  either interrupt or continuation
- **resolved / low predicted harm** -> continue the committed path unchanged

All three legs of that triage are either unbuilt (MECH-482/483) or have an
unspecified trigger-content connection to forward prediction (MECH-090/141,
per Addendum 2's own open next-step). So the honest state, updated: this isn't
one missing connection, it's a whole missing decision layer sitting on top of
E2/E3 forward prediction, with REE currently holding scattered, individually
unbuilt pieces (fast interrupt, cancel-window, epistemic-deficit accumulator,
orient/survey regime, harm-residue activation, goal-cue retrieval) that would
need to compose into it.

## Addendum 5 (same session, later still): confirmed synthesis -- one signal, threshold-gated into three consumers

The user confirmed the synthesis question my prior assessment (of this file,
same session) raised: that the fast-interrupt pathway (Addendum 2) and the
retained-alternative memory (Addendum 1) may be **the same predicted-harm
signal read at two different regimes**, not two unrelated systems that happen
to share substrate.

> "And yes, the two predicted harm of your point 1 is very relevant."

Stated explicitly, combining with Addendum 4's triage: this is **one
continuous signal** -- a predicted-harm/success magnitude plus a confidence/
epistemic_deficit term, both produced from the same E2/E3 forward-prediction
substrate discussed throughout this file -- with (at least) **three distinct
threshold-gated consumers**, not three separate mechanisms that happen to
overlap:

1. **High confidence, magnitude above the fast-interrupt threshold** ->
   MECH-090/MECH-141/MECH-138 fire in real time: interrupt or reroute the
   committed path, or veto before execution lock-in. (Addendum 2)
2. **Confidence too low to trust the magnitude at all (high epistemic_deficit)**
   -> MECH-482/MECH-483 fire instead: orient/survey, gather resolving
   information, defer the interrupt-vs-continue decision until confidence
   rises. (Addendum 4)
3. **Confidence adequate, magnitude below the interrupt threshold (or the
   interrupt pathway didn't fire in time / wasn't wired up / was a genuinely
   close call)** -> this is not a null outcome. It is precisely the
   near-miss case the ORIGINAL thought (points 1-6, Addendum 1) needs
   retained: an alternative that was seriously enough weighted to be worth
   remembering, evaluating counterfactually after the fact, and using for
   responsibility attribution and learning -- even though it didn't cross the
   bar for real-time action.

This reframes the file's own apparent two-thread structure (prospective
correction vs. retrospective responsibility, which Addendum 2 described as
"functionally distinct consumers" of shared substrate) into a single
threshold-gated pipeline instead: the SAME predicted-harm evaluation feeds
real-time correction at the top of the distribution, information-seeking at
the low-confidence end, and retrospective memory/responsibility at whatever
doesn't get consumed by the other two. Under this reading, Addendum 1's
"nothing retains rejected E3 candidates past the current tick" finding is not
just a gap in memory -- it is specifically the gap in leg 3 of this pipeline:
the predicted-harm signal is computed (E3 `select()` scores every candidate)
but whatever doesn't trigger legs 1 or 2 is simply discarded rather than
routed to retention. **This is likely the single most important structural
claim in the whole file for a Stage 2 intake to state as its central
proposal**, rather than as one of several loosely related findings.

One open question this raises rather than resolves: whether "worth retaining"
(leg 3's admission criterion) is the same magnitude range as "not quite worth
interrupting," or a separately-tuned threshold -- i.e. whether legs 1-3
partition the same scale at two cut-points, or leg 3 has its own independent
relevance criterion (e.g. gated by goal-match per Addendum 3's ghost-goal/cue
reading, rather than by harm-magnitude proximity to the interrupt threshold
alone). Not decided here.

**User's follow-up: this question may need to be resolved empirically, not
stipulated architecturally.** I.e. rather than a design choice made once at
build time, whether legs 1-3 share one cut-scale or leg 3 has an independent
criterion is itself something a behavioral test could distinguish -- the two
readings make different predictions. A same-scale reading predicts retained
alternatives cluster just below whatever the interrupt threshold turns out to
be; an independent-criterion reading predicts retained alternatives are better
explained by goal-relevance/match than by proximity to the interrupt cutoff,
and would show cases of low-harm-magnitude-but-high-goal-match alternatives
retained (or the reverse: high-magnitude-but-goal-irrelevant alternatives NOT
retained) that the same-scale reading would not produce. This is exactly the
kind of question the `/thought-digestion` `what_would_answer` step is for
(not attempted here, per the user's earlier instruction to keep this session
to direct capture) -- worth stating explicitly in the Stage 2 intake as a
question with its own falsification condition, rather than a parameter to be
picked by judgment.

## Next steps (not done in this session)

- Per Addendum 5 (user-confirmed synthesis): the Stage 2 intake's central
  proposal should likely be framed as the single threshold-gated pipeline --
  one predicted-harm/confidence signal off E2/E3 forward prediction, three
  consumers by regime (fast-interrupt / orient-survey / retain-for-
  responsibility) -- rather than as a set of loosely related findings. The
  open leg-3-admission-criterion question at the end of Addendum 5 (shared
  cut-point vs. independent relevance criterion) should be posed explicitly
  as a FALSIFIABLE question with its own `what_would_answer` (per the user's
  follow-up: this is empirically resolvable, not a parameter to stipulate by
  judgment) rather than something the claim registration decides by fiat.
- Structured Stage 2 intake (`evidence/planning/thought_intake_2026-08-07_
  responsibility_counterfactual_memory.md`) if/when this gets picked up for
  real design work -- novelty table against `INV-012`/`SD-033e`/`Q-028`/
  `ARC-085`, and a considered claim-registration proposal (likely a new
  claim depending on `INV-012`, rather than folding into it, given how much
  distinct content this is).
- Per the addendum above, the Stage 2 intake should ALSO reconcile against
  `project_imagination_learning_constraints.md`'s pending candidate
  registration (`ARC-XXX imagination_learning_constraint_principle` and its
  Q-XXX/MECH-XXX children, "do NOT register without dedicated lit-pull") --
  three independent sessions have now surfaced the same underlying gap
  (uncommitted-thought retention) from three different angles (learning-
  licitness, responsibility, INV-021's write-pathway exclusivity check)
  without any of them converting it into a registered claim. That
  convergence itself is worth naming explicitly in the Stage 2 intake as
  evidence this is ripe, not merely recurring noise.
- Whoever picks this up should re-verify the architectural grounding above
  against current `ree-v3` state before relying on it -- it reflects a
  single research pass on 2026-08-07, not a full audit.
- Per Addendum 2: check whether current REE substrate ever wires a
  predicted-harm/success magnitude from E2/E3 forward rollouts into the
  `MECH-090`/`MECH-141` hyperdirect (STN->GPi) fast-interrupt pathway, or
  whether that connection is itself the gap. Neither claim currently names a
  trigger source; both currently describe an urgent/unexpected-signal
  interrupt, not a continuously-compared-imagined-future one.
- Per Addendum 4: also pull in `MECH-138` (cancel-window-open flag, dFMC/
  pre-SMA to premotor veto pathway, vetoes *before* execution lock-in) as a
  third relevant timescale alongside MECH-090/MECH-141 -- not yet cross-
  referenced in Addendum 2/4's fast-interrupt discussion. And when this
  reaches Stage 2, cross-reference `docs/thoughts/2026-08-05_epistemic_deficit
  _and_orienting.md` / `MECH-482`/`MECH-483`/`Q-089` directly rather than only
  from this file, since the triage-structure synthesis in Addendum 4 is new
  content not present in either source on its own.
