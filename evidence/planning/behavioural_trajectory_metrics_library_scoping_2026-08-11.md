# Shared Behavioural-Trajectory-Metrics Library: Scoping Proposal

**Generated:** 2026-08-11T20:28Z
**Type:** research/design scoping only, per explicit user instruction ("we may need to design a
whole new experiment type and research how to make experiments which use behavioural data" --
treat as exploratory; produce a recommendation and tradeoffs; **do not implement without a
follow-up go-ahead**). No code was written, no file under `ree-v3/experiments/_lib/` was
modified, and no experiment was queued for this chip. `claim_ids=[]`; this document proposes,
it does not register or resolve any claim.
**Chip:** `chip-20260811-trajectory-metrics-library-scoping`, spawned from
`sleep_transition_investigation_906_lineage_2026-08-10.md`'s 2026-08-11 decision-log entry.

---

## 0. Duplication check (done before drafting the proposal)

- `TASK_CHIPS.json`: no other open or resolved chip mentions a trajectory-metrics library,
  `trajectory_metrics.py`, or a shared behavioural-analysis module (grepped
  `trajectory.metric|trajectory_lib|behavioural.trajectory`; the only hit is this chip's own
  entry).
- `claims.yaml`: `trajectory library` hits exist, but every one refers to **`MECH-325`**, REE's
  proposed internal hippocampal/PFC replay-trajectory library (a substrate memory-retrieval
  mechanism, biologically anchored, gated V4) -- a completely different object from what this
  document proposes. **Disambiguation, stated explicitly so the two are never conflated**:
  `MECH-325` is REE's own candidate internal memory structure; this proposal is external
  offline **analysis tooling** an experimenter runs against already-logged episode data, with no
  causal role in REE's behaviour. Same generate/measure distinction the
  `thought_intake_2026-08-11_behavioural_diversity_umpire.md` novelty table already drew between
  `ARC-062`'s discriminator and the "umpire" (Section 3 below).
- `evidence/planning/`: no existing file matches `trajectory` in its name; no prior scoping
  proposal for this exists.
- `git log --all --grep` (both repos): no prior commit references a `trajectory_metric` module.

**Conclusion: no prior art for the proposal itself.** Sections 1-2 below establish the prior art
this proposal is *responding to* (the repeated ad hoc reinventions), which is the reason the
chip exists.

---

## 1. What each of the three-plus-one prior threads actually computed

Read in full, not summarised from memory, per the chip's own instruction. Metric definitions
below are extracted from the source documents/code, not re-derived.

### 1a. `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` -- ecological/excursion statistics

Ground-truth-`in_reef`-based **excursion** analysis (a maximal contiguous run of `in_reef=False`
steps), computed ad hoc for that review only:
- excursion count, mean duration, mean "depth" (undefined precisely in the doc beyond duration)
- benefit/harm yield per excursion (categorical: yields benefit / involves harm / censored)
- harm-event rate conditioned on `in_reef` vs not
- zone-transition rate per episode
- distance-to-nearest-resource vs leave-shelter-probability correlation (opportunity-triggered
  exit test)
- distance-to-reef trend over the next 3 steps, bucketed by current distance, conditioned on
  threatened/safe (threat-triggered-return test)

This is a **domain-specific (reef/shelter) ecological feature family** -- it does not generalise
to an arbitrary environment without a notion of "protective zone." No shared code; computed
directly against the raw episode log in that session.

### 1b. `sleep_transition_investigation_906_lineage_2026-08-10.md` Section 3 -- spatial trajectory-organisation statistics

Reused the reef review's boundary-comparison *design* (sleep boundary vs matched 100-step
windows at other boundaries) but extended the *feature set* with genuinely general,
environment-agnostic trajectory-organisation measures, via a one-off, uncommitted script
(`sleep_boundary_trajectory_reanalysis.py`, explicitly stated as "one-off, not committed"):
turning-angle entropy, mean/max straight-run length, tortuosity, action-repeat-rate,
`action_blocked` rate, hazard-conditioned turning, resource-acquisition counts.

**This exact feature computation was then independently reimplemented a second time**, in
`ree-v3/experiments/v3_exq_913_developmental_ecology_fishtank.py:387-472`
(`_trajectory_organization_stats()`), whose own docstring says explicitly: "computed here
directly from logged positions (that document's own script was not committed and is
reimplemented from its Section 3 method description, not copied)." The committed version's exact
definitions (verified by reading the code, not inferred):

| metric | definition (from `_trajectory_organization_stats`) |
|---|---|
| `turning_angle_mean` / `turning_angle_entropy_bits` | absolute angular difference (radians) between consecutive non-null headings (`atan2(dy,dx)` on integer position deltas); entropy is Shannon entropy in bits over an 8-bin histogram of turning angles in `[0, pi]` |
| `mean_straight_run_length` / `max_straight_run_length` | consecutive steps sharing the same heading (`abs(h - run_heading) < 1e-6`) |
| `tortuosity` | `path_length / net_displacement`, both Manhattan (`sum(abs(dx)+abs(dy))` vs `abs(dx_total)+abs(dy_total)`); `None` when `net_displacement == 0` |
| `turning_near_hazard_mean` / `turning_far_hazard_mean` | mean turning angle conditioned on whether the step's Manhattan distance to the nearest hazard is `<= HAZARD_NEAR_RADIUS` |

This is a **spatial-geometry feature family**, computed purely from `pos` sequences plus a
hazard-position list -- genuinely environment-agnostic, requiring only `{pos, (optional)
hazard/resource positions}` per step.

### 1c. This session's own 2026-08-11 addendum (Section 13b of the same document) -- action-label-sequence statistics

A **third, distinct feature family**, added specifically because spatial turning/tortuosity
"conflate a 90-degree turn with a full reversal" and grids cannot be spatially smooth: reversal
rate and action-run length computed on the **action-ID sequence itself** (canonical inverse
pairing 0<->1, 2<->3; action 4=stay has no inverse), not on positions. Computed via a throwaway
script parsing the raw episode log directly for this session only; never committed.

**The methodologically important finding from this thread, which any shared module MUST
encode as a documented policy, not an afterthought:** `world_rule_shift_enabled=True`
periodically permutes the live action-ID -> spatial-direction map. A reversal/run-length
statistic computed on action IDs therefore measures **policy-output-sequence structure**
(does REE keep re-selecting the same abstract action), which is **not the same thing** as
spatial backtracking once a window straddles a rule-shift boundary. The two spatial-family
metrics above (1b) and this action-label family are **not interchangeable**, and no existing
document or script computes both from the same window with an explicit note on which
question each answers.

### 1d. `thought_intake_2026-08-11_behavioural_diversity_umpire.md` -- a different layer entirely: discriminability testing, not descriptive metrics

Distinct from 1a-1c in kind, not just content. This proposes an **evaluation methodology**
(Section 3 below), not a feature-computation function: given *some* trajectory-segment feature
vector (which could be built from 1a/1b/1c's outputs), fit a held-out classifier across two
conditions/environments, test accuracy against a permutation null AND a matched-control policy,
and check orthogonal-perturbation selectivity, with a strict measurement/interpretation
two-stage separation. It explicitly reuses `MECH-191`'s classifier-as-discriminator experiment
pattern (`v3_exq_686_mech191_signal_state_discriminability.py`) as its intended code starting
point, and explicitly reuses the reef review's already-computed excursion statistics as its
intended feature source rather than reinventing features.

**Conclusion of Section 1**: three genuinely different, only-partially-overlapping feature
families (ecological/excursion, spatial-geometry, action-label-sequence) have each been computed
ad hoc at least once, with one of the three (spatial-geometry) already independently
reimplemented a second time from a natural-language method description rather than shared code
-- a real definitional-drift risk, not merely a duplicated-effort one (see Section 4c). A fourth,
architecturally distinct concern (cross-condition discriminability testing) has been proposed
but not built, and explicitly depends on feature vectors from families like these as its input.

---

## 2. Existing shared infrastructure -- confirmed gap, with one adjacent (not overlapping) tool

Surveyed `ree-v3/experiments/_lib/` (48 files) and `_lib/baselines/` (25 files) directly, not by
assumption:

- **No file matches** `tortuosity|turning_angle|reversal_rate|straight_run|trajectory_metric`
  anywhere in `_lib/`. The gap the chip describes is real and confirmed, not assumed.
- **One genuinely adjacent tool already exists and should not be duplicated**:
  `_lib/event_window_browser.py` (built 2026-08-10, consolidating the same reef-review and
  sleep-investigation threads' *window-selection/rendering* code, exactly the surprise-peak and
  sleep-boundary browsers both documents proposed). Its own docstring states its purpose
  precisely: "This module builds one reusable tool covering both, so future reviews do not repeat
  either script ad hoc a third time" -- i.e. it is **the direct precedent for doing exactly what
  this chip is scoping**, one layer up (event selection + trajectory rendering, not metric
  computation). Confirmed by reading its function list
  (`select_surprise_peaks`, `select_sleep_boundaries`, `render_event`, `build_report`): it
  extracts and displays a window of raw step dicts; it does not compute turning angle,
  tortuosity, or any scalar/vector trajectory statistic over that window. **A trajectory-metrics
  module and `event_window_browser.py` are complementary, not competing**: the browser answers
  "which window, and what did it look like raw"; a metrics module would answer "what does this
  window's shape quantify to." A natural integration point (not proposed as required scope, see
  Section 6) would be for `render_event()` to optionally attach a metrics module's output for the
  rendered window.
- The corpus-scan-sharing precedent (`ree-v3/tests/contracts/conftest.py`, built 2026-07-28) was
  read as requested, as a pattern reference. It solves a different problem (avoid re-parsing the
  same corpus N times across N *test* functions in one pytest session) via a session-scoped
  fixture and an explicit rejected-alternative writeup (a full in-memory cache was measured and
  rejected on memory grounds). The transferable lesson is procedural, not structural: **when the
  same computation is independently reinvented 2+ times, the fix is one shared, tested function
  with the exact-count/exact-value pins that prove coverage didn't silently narrow** -- not a
  specific code shape to copy. This proposal follows that lesson (Section 4) without copying the
  fixture-and-cache mechanics, which don't apply here (trajectory metrics are computed once per
  experiment run, not once per test-suite session).
- `_lib/arm_fingerprint.py` and the baseline-factoring convention (`_lib/baselines/*.py`, per
  `CLAUDE.md`'s "mint arms as you go" rule) were read for the shared-infrastructure *pattern*,
  not for direct reuse -- they solve reuse of trained-arm *outputs* (fingerprinted OFF-arm
  rollouts), not reuse of *analysis code* applied after the fact. Not directly applicable here.
- The `/queue-experiment` skill's acceptance-check / non-degeneracy-precondition pattern
  (`_lib/precondition_gate.py`, `PreconditionSpec`, `applies_to`, `structural_max`/`structural_min`,
  `aggregate_arm_gates`) is real, load-bearing shared infrastructure for a different concern
  (whether a scored experiment's arms are non-degenerate before a claim-relevant PASS/FAIL is
  trusted) -- discussed in Section 5 as the integration point a future "trajectory experiment
  pattern" would need to plug into, not duplicate.

---

## 3. Proposed design: what a shared module should and should not contain

### 3a. Scope: a feature-computation library, explicitly NOT a statistical-test harness

**Recommendation: keep these as two separate modules at two separate abstraction layers**, not
one combined library. Justification, not just assertion:

- Sections 1a-1c (metrics) are **pure functions of a step sequence**: given positions/actions/
  hazard-positions, return scalars or small vectors. They have no notion of "condition,"
  "environment," "held-out split," or "null distribution."
- Section 1d (the umpire) is a **statistical procedure** that consumes feature vectors from many
  episodes across two-or-more conditions and returns a discriminability verdict with a
  permutation test, a matched control, and a selectivity check. It has no opinion about which
  features feed it.
- Conflating them would mean every future descriptive-metric addition (e.g. a fourth feature
  family for a different environment) forces a change to, or at minimum a re-read of, the
  statistical-test code, and vice versa -- exactly the coupling `event_window_browser.py`
  deliberately avoided by staying a pure window-selection tool rather than also computing
  metrics. `MECH-191`'s existing classifier-experiment code is the natural implementation seed
  for the *second* module, when and if `Q-092` (the umpire claim) is queued -- it should
  **consume** whatever feature vector a metrics module produces, not be extended to compute
  features itself.

### 3b. Proposed shape of `experiments/_lib/trajectory_metrics.py` (metrics module only)

A pure-function module over a standard step-record shape already used consistently across the
906-lineage drivers and `event_window_browser.py`'s own documented input contract: a list of
per-step dicts each carrying at minimum `pos: [int, int]` and `action: int`, with optional
`hazards`/`resources` lists of `[x, y]` cells (only needed for hazard-conditioned metrics).
No new data format -- this is the shape three independent scripts have already converged on
without coordinating.

Proposed function groups, one per already-established feature family (Section 1), each
independently callable so a caller uses only what it needs:

1. **Spatial-geometry family** (from 1b, i.e. `_trajectory_organization_stats`'s function body
   moved verbatim into the shared module, not rewritten): turning-angle mean/entropy,
   straight-run length, tortuosity, hazard-conditioned turning. This is the one family with an
   existing, tested, committed implementation (`v3_exq_913`'s function) -- the mechanical,
   lowest-risk piece of this proposal, since it is a pure extraction with no design decisions
   left open.
2. **Action-label-sequence family** (from 1c, newly formalised -- this session's version was
   never committed, only described in prose): reversal rate, action-run length, repeat rate,
   computed on the action-ID sequence with the canonical inverse-pairing table as an explicit,
   named, overridable parameter (not hardcoded), so a different environment's action space can
   supply its own inverse-pairing (or declare none).
3. **Explicit dual-reporting policy for the world-rule-shift caveat (1c)**: the module MUST
   accept an optional `rule_shift_boundaries: List[int]` (step indices where the action->direction
   map changed) and, when supplied, tag any window straddling a boundary in its output
   (`spans_rule_shift: bool`), rather than silently computing a number whose interpretation
   (spatial vs policy-output structure) depends on information the caller may not have
   surfaced. When `rule_shift_boundaries` is not supplied, the module should compute the
   action-label family only and be silent about spatial interpretation, since it cannot know
   whether the mapping was stable -- **failing informative, not failing silent**, is the
   concrete design requirement the chip asked for.
4. **Ecological/excursion family (1a) is explicitly NOT proposed for inclusion.** It is
   domain-specific to reef/shelter-style protective-zone environments (it needs an `in_reef`-
   equivalent ground-truth flag that most environments will not have) and is a different
   abstraction: an *episode-level* summary built from many *transitions*, not a *window-level*
   trajectory-shape statistic. Recommend it stay a per-experiment concern (as it already is,
   e.g. reused inside the reef review's own script), documented here only so a future reader
   does not wonder why it was omitted.

### 3c. Non-degeneracy preconditions specific to trajectory data

Two concrete degenerate-window failure modes were **found empirically, in this exact prior-art
set**, not hypothesised: (a) `tortuosity`'s `net_displacement == 0` division-by-zero guard
already exists in the committed `_trajectory_organization_stats` code (returns `None`); (b) this
session's Section 13b found a near-degenerate window (`seed1/no_sleep/seg9`: agent moves 3 ticks
then sits motionless for the remaining 96) that was *not* caught by any existing check and had
to be manually flagged as artifact-prone in the writeup. A shared module should expose a
`degeneracy_flags` field per window (e.g. `static_frac > 0.9`, `n_turning_samples < floor`,
`net_displacement == 0`) using the same floor/ceiling/interval vocabulary
`precondition_gate.py` already establishes (Section 5), rather than each caller inventing its
own ad hoc threshold the way this session did.

---

## 4. Whether a standard "behavioural-trajectory experiment" PATTERN is warranted

Distinguishing, as the chip's task asked, the **metrics library** (Section 3, recommended now)
from a **standardised experiment pattern** analogous to `/queue-experiment`'s scalar-channel
acceptance-check convention (a materially larger commitment: a documented convention for
held-out/matched-pair design, trajectory-specific preconditions wired into
`precondition_gate.py`, and a place for the umpire methodology to plug in).

### 4a. What a pattern would need, concretely, drawn from what already went wrong

- **Matched-pair design must check nuisance variables beyond the one being held constant.**
  V3-EXQ-913's own `sleep_ablation_comparison` held hazard/resource layout constant across arms
  (`env.reset_to()`, `layout_continuity_confirmed: true`) but left **spawn position independently
  re-rolled per arm** -- a confound found only by this session's own re-analysis, in all 5 matched
  pairs, after the experiment had already run and been marked `non_contributory`. A documented
  pattern would need an explicit checklist of "what must be matched across arms in a trajectory
  comparison" (layout, spawn position, and -- per the world-rule-shift finding above -- rule-shift
  phase), not left to each script's author to think of.
- **Sample-size ceilings bite harder for trajectory comparisons than scalar ones.** The same
  V3-EXQ-913 reanalysis hit a hard sign-test ceiling (best case p=0.25 at n=3-4 usable pairs)
  even with every available sign agreeing -- because a trajectory comparison needs *matched
  segments*, which are a scarcer resource than scalar samples. A pattern's documented convention
  should set expectations (minimum matched-pair count for a formally testable result) rather than
  let a well-designed but underpowered comparison get reported as null.
- **The umpire methodology (1d) is the natural statistical-test layer for this pattern**, once
  Q-092 (already registered, `status: open`, not yet queued per its own explicit "do not queue
  yet" precondition) produces a first result. It should not be re-derived; this pattern would
  cite it rather than duplicate its held-out/permutation/matched-control design.

### 4b. Integration point with the existing acceptance-check machinery

If a trajectory experiment is ever formally scored (i.e. moves from "retrospective ad hoc
review" to a `/queue-experiment`-authored, `claim_ids`-bearing run), it should reuse
`precondition_gate.py`'s existing `PreconditionSpec`/`applies_to`/`aggregate_arm_gates` machinery
for the degeneracy flags in Section 3c, rather than inventing a parallel gate system --
exactly the rule already stated in the `/queue-experiment` skill for every other precondition
type ("Use `experiments/_lib/precondition_gate.py` rather than hand-rolling this ... the drift is
why the rule did not propagate"). This is a design constraint to state now (so a future builder
doesn't hand-roll a fourth gate system) but not something to build in this scoping pass.

### 4c. Cost/benefit, stated for and against, per the chip's explicit instruction to be fair

**For building the metrics module (Section 3) now:**
- Three independent computations of overlapping metrics in the space of two weeks, one of which
  (spatial-geometry) was **already reimplemented from a prose description rather than shared
  code** -- a real, already-manifested definitional-drift risk (a future fourth reimplementation
  could silently diverge from `_trajectory_organization_stats`'s exact tie-breaking on
  `abs(h - run_heading) < 1e-6` or its 8-bin/`[0,pi]` entropy histogram choice, producing numbers
  that look comparable but aren't).
- The extraction cost for the spatial-geometry family specifically is close to zero: the code
  already exists, is committed, and is not proposed to change -- only to move and be imported
  from two places instead of one.
- A fourth, structurally different consumer (the umpire, Section 1d) already names this exact
  library as its intended feature source ("reuse, do not reinvent... build the trajectory-segment
  feature vector from that existing instrumentation"), so the "will a second/third use case
  actually materialise" bar the chip asked to check honestly is **already cleared** by
  already-written proposals, not merely hypothesised.

**Against, stated fairly rather than dismissed:**
- Every one of the three metric-computation reinventions so far was a **retrospective, ad hoc,
  uncommitted analysis script** run inside a single research session, not a committed, queued,
  `claim_ids`-bearing experiment (V3-EXQ-913's `_trajectory_organization_stats` is the one
  exception, and even there the *ablation comparison it fed* self-routed `non_contributory`,
  never reaching a scored claim). It is possible the genuine, recurring need is for an
  **analyst's toolbox function**, not production experiment infrastructure -- and over-engineering
  toward the `/queue-experiment`-pattern shape (Section 4a/4b) ahead of a real committed consumer
  risks building governance/precondition scaffolding nobody uses, the same over-abstraction risk
  `event_window_browser.py`'s own docstring implicitly avoided by staying a thin, two-mode tool.
- The three feature families (1a-1c) are genuinely different enough (ecological/excursion vs.
  spatial-geometry vs. action-label-sequence) that a single module risks becoming a grab-bag with
  poor cohesion if built too eagerly, before it's clear which combinations future callers
  actually want together.
- No experiment has yet been *formally scored* using any of these metrics, so the
  precondition-gate integration (4b) would currently be designed against a zero-instance
  distribution of real usage patterns -- exactly the kind of premature-generalisation risk
  `CLAUDE.md`'s "Narrow Edits Only" and held-out-check disciplines warn about for standing
  infrastructure.

---

## 5. Recommendation

**Build the metrics module (Section 3b), scoped narrowly, as a follow-on chip. Do NOT build the
standardised experiment pattern (Section 4) yet.**

Concretely, if a follow-up go-ahead is given:

1. Extract `_trajectory_organization_stats` from `v3_exq_913_developmental_ecology_fishtank.py`
   into `experiments/_lib/trajectory_metrics.py` **verbatim in behaviour** (same function body,
   same defaults, same `HAZARD_NEAR_RADIUS` constant made an explicit parameter with the same
   default), with a regression test asserting bit-identical output on a fixture before and after
   the move -- this is the zero-design-risk, mechanical half of the proposal.
2. Add the action-label-sequence family (reversal rate, run length, repeat rate) as new
   functions in the same module, formalising this session's uncommitted script, with the
   `rule_shift_boundaries`/`spans_rule_shift` dual-reporting policy from Section 3b(3) as a
   first-class parameter, not an afterthought -- this is new code, but small and already
   fully specified by this session's own prose description (Section 1c).
3. Add the `degeneracy_flags` output (Section 3c) using existing found failure modes as the
   test fixtures (the `net_displacement==0` case already handled; the near-static-window case
   from `seed1/no_sleep/seg9` as a new one), reusing `precondition_gate.py`'s floor/ceiling
   vocabulary for the flag names so a later formal-pattern integration (Section 4b) doesn't
   need to rename anything.
4. Do **not** build the standardised experiment pattern, the `precondition_gate.py` wiring, or
   any change to `event_window_browser.py` in this same pass -- reassess once either (a) a
   second experiment is committed and queued that consumes this module for a scored claim, or
   (b) `Q-092`'s umpire experiment is actually queued and needs a feature source, whichever
   comes first. Building the pattern ahead of either would be exactly the premature-abstraction
   risk Section 4c's "against" case names.
5. When (4)'s trigger condition is met, revisit whether `event_window_browser.py` should gain an
   optional "attach metrics for this window" mode (Section 2) -- explicitly deferred, not
   decided, here.

This recommendation resolves the chip's central question (worth building vs. not) as **worth
building the narrow half now, not the broad half yet** -- distinguishing a low-risk, already-
proven-needed extraction from a higher-risk, not-yet-needed pattern, rather than a single
yes/no verdict across both.

---

## 6. What this document did not resolve (explicitly out of scope for this scoping pass)

- The exact function signatures / module-level API for `trajectory_metrics.py` -- left to the
  implementer at build time, per this being a design *scoping* document, not an implementation
  plan.
- Whether `event_window_browser.py` should eventually import the metrics module -- flagged
  (Section 2, Section 5 item 5) as a future integration point, not decided now.
- Whether the ecological/excursion family (1a) should ever be generalised beyond reef/shelter
  environments -- explicitly recommended against inclusion in the first build (Section 3b item 4),
  revisit only if a second protective-zone-style environment is built.
- Any code, test, or experiment queue entry -- none written, per the chip's explicit instruction.

---

## Decision log

- 2026-08-11: Scoping/research chip (not build) completed. Read all three prior-art threads plus
  the umpire thought-intake in full; extracted three genuinely-distinct trajectory feature
  families (ecological/excursion, spatial-geometry, action-label-sequence) and one
  architecturally-separate discriminability-testing layer (the umpire). Confirmed via direct
  code/file survey that no shared trajectory-metrics infrastructure exists in
  `ree-v3/experiments/_lib/`, but that one adjacent tool (`event_window_browser.py`) already
  exists as the direct precedent for consolidating exactly this kind of repeated ad hoc script.
  Recommendation: build a narrow, low-risk `trajectory_metrics.py` extraction+formalisation now
  (metrics module only); defer the broader `/queue-experiment`-style acceptance-check pattern
  until a real committed/scored consumer exists. Awaiting human go-ahead before any build work
  begins. (session: sd-016-h3-algorithm-3370cd, worktree,
  [chip_ref: chip-20260811-trajectory-metrics-library-scoping])
