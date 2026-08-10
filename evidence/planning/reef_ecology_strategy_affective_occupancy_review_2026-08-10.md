# Reef Ecology Strategy, Affective Occupancy & Surprise Review: V3-EXQ-906 Lineage

**Generated:** 2026-08-10T06:15Z
**Type:** organism-level observational review, direct continuation of
`organism_lifespan_development_review_906_lineage_2026-08-10.md` (do not repeat that analysis; this
extends it with 10 new lines of inquiry raised by human visual inspection). All findings below are
retrospective analysis of already-collected 906b/906c episode logs unless explicitly marked as a
successor proposal. `claim_ids=[]` throughout; non-scoring.
**New analysis this session:** ground-truth `in_reef`-based excursion analysis (distinct from the
mode-classifier bouts used previously); reef design-history recovery; a working surprise-peak browser
(top-8 peaks, full context); familiar-event surprise decline (raw and baseline-relative); retrospective
sleep pre/post comparison against non-sleep-boundary controls; accumulator-drift check on excite/dread/
surprise. Duplication-checked first (Section 0 below) — none of this existed.

---

## 0. Duplication check (done before any new analysis or proposal)

None of the ten lines of inquiry below had prior art as a claim, tool, or completed analysis:
**shelter-centred risk/reward framing** (not found — only the generic mode-diversity framing existed);
**ecological competence reframing** (not found); **lifetime affective-occupancy measurement** (not
found as a measurement, though a formal valence/relief/safety/soothing taxonomy already exists,
distributed across `ree_core/residue/field.py`, `docs/architecture/affect_primitives.md`, and the
`z_beta` arousal control-plane docs — see Section 3); **surprise-peak inspection tool** (confirmed still
unbuilt as of this morning's review); **developmental-ecology redesign proposal** (not found — only the
narrower layout-continuity fix from the prior review); **welfare-instrumentation-as-hygiene** (not
found as measurement, though `SENT-2`/`SENT-4` already establish the *policy* of capping negative-valence
exposure, `v4`-binding — see Section 9). One important piece of prior art WAS found and materially
changes Section 1: the reef ecology's design history (SD-054, `MECH-309`, `V3-EXQ-522`).

---

## 1. The reef ecology hypothesis — recovered design history, then tested against ground truth

### 1a. What was actually pre-registered, and what was not

The reef/shelter mechanic (`SD-054`, introduced `ree-v3` commit `3d8c8999`, 2026-05-04) was explicitly
designed around a two-attractor, prey-fish analogy **three months before the 906 lineage existed**:

> `docs/architecture/sd_054_reef_enrichment_substrate.md` (2026-05-08): "The biological analog is
> coral-reef refugia: in marine systems, predator-free patches with distinct microhabitat structure
> force fish into context-dependent strategy selection (shelter-seeking near the reef vs. foraging in
> open water)."

This is genuinely the user's "prey-fish-like" intuition, pre-registered. **But the quantitative target
was a *balanced*, *actively switching* dual strategy, not a shelter-dominant one.** `V3-EXQ-522`
(2026-05-05) pre-registered three numeric acceptance criteria for a trained policy: **C1**
`reef_visit_fraction >= 0.05`, **C2** `foraging_fraction >= 0.15` (foraging must *persist*, not be
crowded out), **C3** `zone_transitions_per_ep >= 1.0` (active switching, not settling into one zone).

**Crucially, the design record itself had already downgraded its own expectation before 906 existed.**
The same architecture doc, updated as of 2026-07-10 (after several intermediate trained-policy retests,
before any fishtank observational run): "The trained agent does not adopt a discriminative reef-vs-forage
policy. It stays monomodal under gradient descent... every SD-029 retest on SD-054 substrate has returned
`non_contributory`... The trained policy does not adopt the discriminative reef-vs-forage regime." This
already-diagnosed failure mode has a name and a registered `candidate` claim: **`MECH-309`** —
"Monomodal policy collapse is the equilibrium of a parametric-policy agent without a rule-apprehension
layer... without a non-Bayesian rule-creator that proposes discriminative policy modes ('near-hazard ->
reef regime; else -> forage regime'), the trainer collapses to the smoothest single regime good-enough
across the whole state space." (`claims.yaml`, `candidate`, gated on `ARC-062`.)

**No document, before or since, predicted *which* single mode a collapse would favour.** The specific
shelter/`assert`-dominant phenotype the human observer watched was not itself a pre-906 prediction — only
the general tendency to collapse toward *some* single regime was anticipated, via `MECH-309`.

### 1b. Excursion analysis against ground truth (`in_reef`, not the `mode` classifier)

The prior review's bout analysis used the post-hoc `mode` classifier. Here, "shelter" is instead
operationalised directly from the substrate's own ground-truth `in_reef` flag, and an **excursion** =
a maximal contiguous run of `in_reef=False` steps.

**A. Shelter is genuinely protective — replicated across both runs:**

| | 906b | 906c |
|---|---|---|
| fraction of life `in_reef` | 0.41 | 0.27 |
| harm-event rate while `in_reef` | 0.039 | 0.053 |
| harm-event rate while NOT `in_reef` | 0.094 | 0.085 |
| exposure/shelter harm-rate ratio | **2.43x** | **1.61x** |

Both runs show meaningfully elevated harm while outside the reef. This is a real, replicated,
quantitative signature that shelter functions as protection — not merely a label.

**B. Excursion inventory — replicated:** 64 excursions (906b) / 67 (906c), mean duration 36-41 steps,
73-83% yield some benefit signal, ~48% involve some harm, ~9-11% end censored (segment cut off before
returning). Both runs comfortably exceed `V3-EXQ-522`'s own **C3** bar (`zone_transitions_per_ep >= 1.0`)
by roughly 7-8x (≈8 excursions/episode), and **C1**/**C2** by an even larger margin (`in_reef` 0.27-0.41
vs C1's 0.05 floor; not-`in_reef` 0.59-0.73 vs C2's 0.15 floor). **906b/906c cannot formally score against
`V3-EXQ-522`** (diagnostic showcase, `claim_ids=[]`, all-ON not the scored trained-policy arm that
`V3-EXQ-522` targets) — but the raw statistics would comfortably clear every one of `V3-EXQ-522`'s
numeric bars, on a substrate where the design record's own most recent status (2026-07-10) said every
prior SD-029 retest had failed to reach a discriminative regime at all. This is worth flagging as a
genuinely positive, quantitative observation for a future *properly scored* retest to test formally
(Section 8) — not asserted as a pass here.

**C. Successful/harmed excursions are longer and deeper — replicated, but largely tautological, not
strategic:** benefit-yielding excursions are far longer and deeper than non-benefit ones (906b: 42.5 vs
4.6 steps; 906c: 53.2 vs 8.1 steps), and so are harmed ones vs clean ones (906b: 53.3 vs 19.8 steps;
906c: 61.6 vs 22.4 steps). **This pattern is largely definitional, not evidence of deliberate
depth-modulation**: the benefit field is diffuse and continuous (established in the prior review), so
any excursion that simply lasts longer has more opportunity to register *some* benefit or *some* harm
along the way, independent of any strategic choice. Read alone, B and C support "REE leaves shelter,
sometimes profitably, sometimes at cost" — not yet "REE strategically modulates how far/long it goes."

**D. Opportunity-triggered exit — a structural finding the environment itself makes untestable as
posed, plus a weak residual signal:** the minimum possible gap between the reef boundary and any
resource is **4-5 cells in every episode of both runs**, while the agent's sensory window is
radius-2 (established in the prior review). **By construction, no resource can ever be within sensing
range while the agent is standing inside the reef** — so a literal "REE senses a nearby resource and
decides to leave" mechanism cannot be exercised by this ecology's current geometry at all; this is an
**ENVIRONMENT-layer** finding, not evidence about REE's decision-making. A softer test — correlating
continuous nearest-resource distance (even beyond sensory range, which the diffuse ambient benefit field
could in principle still respond to) against leave-shelter probability — finds a weak effect in the
predicted direction (r=-0.13 in 906b, r=-0.16 in 906c: closer resource associated with modestly higher
leave-probability) but the effect is **not monotonic across distance quintiles** in either run, and
should be read as, at most, a marginal signature riding on the diffuse ambient-gradient exploitation
already established, not a clean opportunity-detection policy.

**E. Threat-triggered return — weak and, on the crudest test, backwards; a distance-controlled retest
sharpens it to "weak and inconsistent," not "adaptive."** A naive test (does REE return to shelter within
5 steps of being near a hazard or just harmed?) shows the **opposite** of the hypothesised direction in
both runs: P(retreat|threatened) 0.047 (906b) / 0.052 (906c) vs P(retreat|safe) 0.169 / 0.145 — a genuine,
replicated, counter-intuitive result. But this crude test is confounded by absolute distance from the reef
(a threatened agent deep in an excursion cannot mechanically reach the reef within a fixed 5-step window
regardless of intent, while a "safe" agent is more likely already near the boundary). A distance-controlled
version (does distance-to-reef trend down over the next 3 steps, bucketed by current distance) is more
informative but still not a clean win: in the closest bucket (`dist_now` 0-3), threatened steps trend
toward the reef (906b: -0.297, 906c: -0.034) while safe steps trend *away* (906b: +0.099, 906c: +0.189) —
the one bucket where the predicted direction shows up — but at greater distances the two conditions
converge or lose separation (906b `dist_now` 7-10: threatened -0.108 vs safe -0.142, direction reversed).
**Net read: a modest, distance-dependent, inconsistent signature — present at close range in both runs,
absent or reversed farther out. Not the clean "threat-sensitive homing" behaviour the strong hypothesis
would need.**

### 1c. Verdict on the central question: did REE independently converge on the predicted reef strategy?

**Partially, and specifically not in the way originally intended.** Per GOV-FAILLOC-1, this is a genuinely
mixed result, not chargeable cleanly to REE:

- **REE-candidate, supported:** shelter use is real and genuinely protective (1a A); excursion *frequency*
  comfortably clears every one of `V3-EXQ-522`'s own pre-registered numeric bars.
- **MECHANISM, already-tracked, re-observed in a new context:** the coarse phenotype (heavy time in one
  or two dominant zones, with real but largely reactive/undirected switching) is more consistent with the
  *already-diagnosed* `MECH-309` monomodal-collapse-without-a-rule-apprehender than with a genuinely
  discriminative, context-triggered policy. What is new here is *which* pole the collapse favours (the
  safety pole) and that it is not a *pure* collapse (real excursions do occur, unlike a 0%/100% split) —
  but the underlying mechanism gap `MECH-309` names (no rule-creator proposing "near-hazard -> reef;
  else -> forage" as a discriminative regime) is unchanged and pre-dates this observation.
  **Cross-reference `MECH-309` when recording this; do not register it as a fresh finding.**
- **ENVIRONMENT, novel:** the reef-resource spatial geometry (min gap 4-5 cells, beyond sensory radius 2)
  structurally forecloses a clean opportunity-triggered-exit mechanism from ever being testable in the
  current ecology (Section 8 successor).
- **Not established either way:** genuine threat-triggered return (weak, distance-dependent, inconsistent
  across runs).

**The correct short formulation:** REE's shelter use functions as real protection and its switching
frequency exceeds the ecology's own pre-registered activity bar, but the *contingency* that would make
this a genuinely adaptive risk/reward strategy — leaving because an opportunity is sensed, returning
because a threat is sensed — is weak, inconsistent across seeds, and in one crude test actively backwards.
This is closer to "real ecological structure being exploited passively/diffusely" than to "REE learned
the reef's intended discriminative strategy." Distinguishing **behavioural impoverishment** from
**adaptive shelter-centred foraging** the way the brief asked: it is neither — it is closer to a third
category, **passive exploitation of a genuinely protective zone without demonstrated contingent
control**, which is exactly what `MECH-309`'s "monomodal collapse without a rule-apprehender" would
predict happens to *any* two-attractor context if you don't build the discriminative layer.

---

## 2. Ecological competence, reframed — and where scalar measures undervalue it

Reframing competence against the ecological objective the brief specifies — *obtain sufficient resources
while minimising dangerous exposure and remaining alive* — rather than against exploration/approach/
movement maximisation, changes the reading of several already-established facts:

- **Survivability (prior review):** 906b/906c/911 show 75-100% step-cap censoring — under this framing,
  that is not "REE trivially avoids ending" so much as "the organism satisfies the minimal ecological
  bar (stay alive) so completely that this measure saturates," which is a *different* claim from
  "REE is behaviourally impoverished."
- **Harm/shelter tradeoff (Section 1b-A):** a 1.6-2.4x lower harm rate while sheltering, with genuine
  time spent both sheltering and foraging, is closer to what "minimise dangerous exposure while
  acquiring sufficient resources" would look like than a pure explore-maximiser or a pure hider would
  produce (either extreme would score *worse* on this specific objective, not better).
- **Where generic scalar measures likely undervalue this:** the prior review's Section 4 correlations
  (dread->harm, z_goal->approach, near-zero) test whether internal state predicts the *next single
  action* — a maximisation-flavoured question ("is REE optimising moment-to-moment"). They do not test
  whether the *aggregate outcome* (harm rate, survival, resource sufficiency) is good relative to the
  ecological problem. Both readings can be true simultaneously: moment-to-moment internal-state coupling
  can be weak (confirmed, Section 4 of the prior review; re-confirmed at bout level, Section 6 of the
  prior review) while the *aggregate* behavioural statistics (Section 1b here) are still consistent with
  a reasonably-adapted outcome. **This is a MEASURES-layer point, not a retraction of the coupling
  finding**: the coupling finding is about mechanism (does an internal state variable drive the next
  action), and is unaffected by this section; what changes is only whether "REE is weakly competent" is
  the right gloss on the *aggregate* result, when a survive-and-manage-exposure objective is used instead
  of an implicit maximise-everything one.
- **Caveat, stated plainly:** none of Section 1's tests found REE *actively balancing* resource gain
  against exposure risk in a directed way (the excursion-depth/harm/benefit relationships in 1b-C are
  confounded with duration, and the threat-return test in 1b-E is weak/inconsistent) — so "REE balances
  resource gain against exposure risk" should be read as **not established**, distinct from "REE's
  aggregate outcome happens to look reasonably balanced," which the harm/shelter ratio does support.

---

## 3. Proto-valence / affective occupancy — conservative, and one genuinely new measurement finding

### 3a. The existing taxonomy already distinguishes what the brief asks to distinguish

Before presenting new analysis: a formal valence/arousal/relief/safety/wanting taxonomy already exists in
this codebase, distributed across three sources rather than unified in one document, and should be cited
rather than re-invented:

- `ree_core/residue/field.py`: six residue valence-vector components — `WANTING`(0), `LIKING`(1),
  `HARM_DISCRIMINATIVE`(2), `SURPRISE`(3, unsigned), `POSITIVE_SURPRISE`/excite(4),
  `NEGATIVE_SURPRISE`/dread(5).
- `docs/architecture/affect_primitives.md`: **relief** (`MECH-302`, registered V3) — "event-locked,
  phasic, value-coding reinforcement... at the offset of an aversive event... tags 'this reduced
  suffering.'" **Safety** (`MECH-303` contextual / `MECH-304` cue-specific, registered V3) — "a learned
  prospective predictor that threat is absent... licenses commitment-release and approach... future /
  tonic / inhibitory," explicitly distinguished from mere low harm and from wanting. **Soothing**
  (`MECH-355`, V4-social candidate) — present-tense down-regulation of an ongoing stress response.
- **Arousal** appears as a distinct control-plane signal (`z_beta`, gating attentional/theta-buffer
  gain), not folded into the valence register.

**None of relief (`MECH-302`), safety (`MECH-303`/`MECH-304`), or arousal (`z_beta`) are surfaced in the
Fishtank driver's telemetry** — the same "computed but never read out" pattern already found for
`residue_wanting` and `liking` before 906c partially fixed it. This is a genuine, concrete, low-cost
follow-on (surface `z_beta`, and the relief/safety channels if their compute paths are reachable from this
config, alongside the wanting/liking/surprise work already landed) that would let a future pass test
these already-registered constructs directly instead of approximating them.

### 3b. New finding: the unclamped-accumulator defect extends to `dread`, not only `excite`/`liking`

`SD-RESIDUE-VALENCE-BOUND` was previously established for `excite` (906a autopsy) and extended to
`liking` (this morning's review, since it shares the identical `RBFLayer.update_valence()` unclamped `+=`
write path). **Direct per-episode inspection shows `dread` shares the same signature — a novel finding,
robustly replicated across both runs:**

| episode | 906b mean excite | 906b mean dread | 906c mean excite | 906c mean dread |
|---|---|---|---|---|
| 0 | 1.35 | 0.049 | 0.09 | 0.020 |
| 1 | 4.93 | 0.345 | 0.85 | 0.052 |
| 2 | 8.40 | 0.724 | 2.35 | 0.160 |
| 3 | 15.25 | 1.250 | 2.75 | 0.225 |
| 4 | 13.02 | 0.888 | 5.22 | 0.435 |
| 5 | 21.08 | 1.680 | 7.33 | 0.612 |
| 6 | 18.62 | 1.156 | 8.03 | 0.759 |
| 7 | 29.58 | 2.011 | 10.16 | 1.085 |

Both channels rise roughly monotonically across the run's 8 episodes, in both seeds — a ~20x rise for
excite and a ~40x rise for dread in 906b; a ~110x rise for excite and a ~55x rise for dread in 906c.
`r(excite, within-episode step index)` is +0.21 (906b) / +0.15 (906c) — a real, modest, time-drift
correlation — while `r(excite, harm_signal)` is +0.02 / -0.01 — essentially zero. **This is a shared
plumbing defect across (at least) excite, dread, and liking, not an excite-specific issue** — the
recommendation to extend `SD-RESIDUE-VALENCE-BOUND`'s scope should name `dread` explicitly, since the
existing manifests currently only caveat `excite` (and, per this morning's review, `liking`).

### 3c. Directly testing the user's memory: are apparently-positive spikes during negative events explained by contamination?

**Yes, substantially — and the mechanism is now identified rather than merely suspected.** At harm-event
steps, both excite (1.20-1.43x baseline) and dread (1.31-1.48x baseline) are elevated together, in both
runs; the fraction of steps with *both* channels simultaneously above their own within-run 75th
percentile (21.7-24.5%) is roughly 3-4x what independence would predict (6.25%) — because both channels
are driven substantially by the same shared, non-decaying, revisit-count-linked accumulation (3b), so
whenever one is elevated (late in an episode, or in a heavily-revisited region), the other tends to be
elevated too, **independent of the momentary event's actual valence.** An event-triggered average around
harm events does show a small, real, event-locked bump-and-decay shape in *both* channels over a ~9-step
window (too short for the slow across-episode drift to explain it alone) — so there is likely a genuine,
small, event-locked component riding on top of the much larger accumulator-driven baseline. **Given both
components are present and entangled, the specific vivid case the user recalled (a nominally negative
event with an apparently positive-looking co-spike) is best explained by the shared accumulator drift
plus an entangled small phasic co-response, not by REE genuinely evaluating a harmful event as good.**

### 3d. Testing the proposed near-term formulation

> *"REE's observable behaviour does not appear chronically distress-like, but current positive-valence
> channel defects prevent determination of whether its overall proto-affective balance is genuinely
> positive."*

**Verified, with dread now added to the defect list.** Nothing in this session's data shows REE spending
a dominant fraction of its life in a state that would read as chronic distress by any of the available
proxies (dread's absolute magnitude stays well below excite's throughout both runs; harm-event rate is
3.9-9.4% of steps; shelter — the lower-harm zone — is occupied 27-41% of the time). But the accumulator
defect now demonstrably contaminates the negative-valence channel too, not only the positive one, so
**the formulation should be widened**: current channel defects prevent determination of the overall
proto-affective balance in *either* direction, not only the positive one. The safest defensible statement
given this session's evidence is closer to: *REE's observable behaviour does not appear chronically
distress-like by any currently-available proxy, and the channels that would need to be trustworthy to say
more (excite, dread, liking) are all contaminated by the same shared measurement defect in a way that
prevents a genuine hedonic-balance estimate in either direction.*

### 3e. What repaired telemetry would need, concretely

Beyond the already-scoped `SD-RESIDUE-VALENCE-BOUND` fix (clamp/decay the accumulator across all six
valence indices, not only excite): (1) surface `z_beta` (arousal) and the relief/safety channels
(`MECH-302`/`303`/`304`) per 3a; (2) log a per-step or per-write **baseline-relative** value alongside the
raw accumulated one for every valence index (Section 5 below shows this materially changes conclusions,
not only for surprise); (3) an explicit offset/relief detector (harm-stream derivative, per `MECH-302`'s
own definition) rather than inferring relief informally from a raw-channel decay curve.

---

## 4. Surprise event browser — built and run this session (previously proposed, unbuilt)

Top-8 `residue_surprise` peaks extracted per run, with ~7-step surrounding context (position, `in_reef`,
mode, nearby hazards/resources, injected-event flags, transitions, dread/excite/z_goal, subsequent
movement). Full per-peak detail is in the session's working notes; the pattern across both runs' top
peaks is decisive and consistent:

- **In 906b, 5 of the top 8 surprise peaks occur exactly around `reef_entry`/`reef_exit` transitions**
  (in_reef=True, mode=shelter, with `reef_entry`/`reef_exit` in the surrounding transition window) — the
  single most surprising *class* of moment in this agent's recorded life is crossing the reef boundary,
  not any hazard or injected event.
- **3 of the top 8 (906b) form one tight cluster (ep4, t=210-212) around a genuine resource-consumption
  run** — `transition_type='resource'` fires three times in a 3-step window, with elevated surprise
  (0.41-0.48), high excite (27-29), and, notably, elevated dread (1.9-1.9) *simultaneously* — a concrete,
  named instance of the co-activation pattern discussed in 3c, occurring at what is by any reasonable
  standard a genuinely significant appetitive event.
- **Zero of the top-8 peaks in either run correspond to `limb_damage_injected`, `external_hazard_injected`,
  or `world_rule_shift_occurred`** (all `False` on every one of the top-8 in both runs). This is a
  decisive, concrete confirmation — via direct inspection rather than inference — of exactly the
  distinction the user's brief raised: **the experimenter-labelled "important" injected events are not
  among REE's most surprising moments; ordinary context transitions (reef boundary crossings) and
  genuine appetitive events are.** This directly corroborates and sharpens `V3-EXQ-910`'s already-
  established finding (near-zero trigger alignment on those same injected event types) — 910 showed the
  candidate trigger doesn't fire reliably on those events; this browser shows *why*, empirically: those
  events simply are not where REE's own largest prediction-error spikes occur.

This answers the user's stated question directly: **what actually surprises REE, in this substrate, is
predominantly boundary-crossing (reef entry/exit) and genuine resource acquisition — not the
experimenter's injected hazard/damage/rule-shift events.**

---

## 5. Familiar-event surprise decline — inconsistent on raw values, more consistent once a local baseline is subtracted

Tested four recurring event classes (reef entry, reef exit, first-hazard-approach-per-encounter, blocked
action) by comparing the first half vs second half of each event class's occurrences within one
continuous run.

**On raw `residue_surprise` values, the two runs disagree:** 906b shows a clean decline for all four
event classes (reef_entry 0.033ratio decline to 0.011, i.e. ratio late/early **0.33**; reef_exit **0.48**;
action_blocked **0.66**; hazard_proximity **0.81**). 906c shows flat-to-*increasing* for the same four
(reef_entry **1.14**; reef_exit **1.03**; action_blocked **1.31**; hazard_proximity **1.68**). Read alone,
this looks like a non-replication.

**But `residue_surprise` shares the same write mechanism as excite/dread/liking (Section 3b), so a raw
early-vs-late comparison is exactly the kind of test the accumulator defect would corrupt** — and per the
prior review's own Section 11b design note, the theoretically correct test was already specified as a
*derivative against a rolling baseline*, not an absolute-value comparison. Recomputing each event's
surprise value **relative to a trailing 50-step rolling mean** (removing the local drift) resolves most of
the disagreement:

| event class | 906b raw delta | 906b baseline-relative delta | 906c raw delta | 906c baseline-relative delta |
|---|---|---|---|---|
| reef_entry | ratio 0.33 (decline) | **-0.022** (decline) | ratio 1.14 (flat/rise) | **-0.001** (weak decline) |
| reef_exit | ratio 0.48 (decline) | **-0.011** (decline) | ratio 1.03 (flat) | **-0.005** (decline) |
| action_blocked | ratio 0.66 (decline) | **-0.008** (decline) | ratio 1.31 (rise) | **~0.000** (flat) |
| hazard_proximity | ratio 0.81 (decline) | **-0.006** (decline) | ratio 1.68 (rise) | **+0.002** (weak rise) |

Once the local accumulator drift is subtracted, **3 of 4 event classes decline in both runs (reef_entry,
reef_exit, action_blocked in 906b clearly; reef_entry/reef_exit weakly but consistently in 906c)**, with
only `hazard_proximity` staying ambiguous (small, opposite-signed, near-zero deltas in each run).
**Reef-boundary crossing is the strongest and most consistent signal: a recurring, predictable context
transition becomes measurably less surprising with repeated exposure within the same continuous life, in
both available runs, once the accumulator-drift confound is controlled for.** This is genuine, if modest,
evidence for the selective-decline signature the brief asked about — distinct from global habituation,
since the *relative-to-local-baseline* measure is specifically designed not to register overall signal
flattening. The methodological lesson is worth stating plainly: **raw-value early-vs-late comparisons on
any of the six valence-vector channels are not currently trustworthy without a baseline-relative
correction**, and this is a second, independent illustration of that (after 3b/3c) — not a new caveat
invented for this section alone.

---

## 6. Sleep pre/post — a retrospective test IS possible from 906b/906c's own data (unlike V3-EXQ-909), and it does not support a sleep-specific effect

The prior review established `V3-EXQ-909` contains no pre/post-sleep behavioural comparison at all. But
906b and 906c each had **one real sleep-cycle firing** during their own eval, with real waking behaviour
recorded both before and after it — a retrospective test is possible using data already on disk, comparing
the sleep boundary against the run's other (non-sleep) segment boundaries as a control group for the
generic environment-reset effect (established in the prior review: `env.reset()` fires at every boundary
regardless of cause).

**906b (sleep before ep7):** last 100 steps of ep6 (pre) -> first 100 steps of ep7 (post): harm rate
0.15->0.00, mode entropy 0.0 (completely degenerate — a single mode for the entire tail) -> 1.64, benefit
rate 0.30->0.51. Taken alone, this matches the human observer's impression of more organised, less
harmful, more successful behaviour after sleep.

**But this pattern is not distinguishable from the generic reset effect.** Across the other 6 (non-sleep)
boundaries in the same run: entropy rises from a similarly-degenerate 0.0 tail at the **ep0->ep1**
boundary to **1.99** — a *larger* jump than the sleep boundary's, with no sleep cycle involved at all.
Harm rate decreases post-boundary at 4 of the 6 non-sleep boundaries too (plausibly explained by the
906b/906c "safe spawn" fix itself, which guarantees no segment starts already inside a harm zone —
an environment-engineering reason for low harm right after *any* reset, sleep or not).

**906c (sleep before ep7) replicates this exact pattern:** entropy 0.24 (pre) -> 1.67 (post) at the sleep
boundary, but **4 of the 6 non-sleep boundaries in 906c show pre-entropy of exactly 0.0** (segments that
happened to end in a single degenerate mode) followed by post-entropy in the 1.4-1.97 range — the same
"degenerate tail -> diverse fresh start" shape, with no sleep cycle involved, at multiple non-sleep
boundaries.

**Verdict: the retrospective test that the prior review could not run for 909 was run here for 906b and
906c's own real sleep firings, and it finds the apparent post-sleep refinement is not distinguishable from
the generic segment-boundary reset effect** (fresh spawn position, fresh hazard/resource layout, freedom
from whatever long single-mode bout the agent had settled into by the end of the prior segment). With
only one real sleep firing per run, this cannot rule out a genuine sleep-specific contribution entirely —
but it does mean the human-visible "looks better after sleep" impression has a fully sufficient
non-sleep explanation already present in the same data, and should not be read as evidence for
sleep-dependent refinement without a design that decouples sleep firing from segment-boundary reset
(Section 8).

**The separate, already-established architectural gap stands unchanged**: REE continued locomoting during
the one sleep cycle that fired (prior review, Section 5) — there is no sensory-gating/motor-inhibition
state during sleep in the current substrate, so "before/after sleep" here means before/after an *offline
consolidation event*, not before/after a genuine sleep *state*.

---

## 7. "Day-1 vs day-2" analogy — which mechanisms plausibly need more than ~4,000 lived steps, stated without excusing anything

Used only as an experimental analogy, per the brief's own caveat. Given the prior review's finding that
one continuous run currently spans at most ~4,000 steps across 8 segments, and Section 5/3 above show that
even the clearest developmental signal found this session (reef-entry surprise decline) is modest in
magnitude and needs a baseline-relative correction to see clearly at all: mechanisms that plausibly
require substantially more accumulated, varied experience than this budget provides include
**differentiated memory** consolidation effects (Section 6 — one sleep firing per run is not enough to
characterise a mechanism that may need many firings to show a signature), **calibrated surprise**
specifically (Section 5's signal is present but small; more encounters per event class would sharpen it),
and **sophisticated avoidance** (`MECH-357`'s eligibility-trace avoidance learner is a training-time
mechanism whose within-life signature, if any, was not tested this session — a concrete, cheap follow-on:
confirm whether it is active in the fishtank config before treating its absence as a finding). This is
offered as *context* for why several null/weak findings in this and the prior review may be under-powered
by lived experience, not as a reason to discount them — the accumulator-drift and reef/`MECH-309` findings
in this session, for instance, are not experience-budget-limited; they are measurement-defect and
already-diagnosed-mechanism findings respectively, and more lived time would not resolve them.

---

## 8. Environment design as a first-class scientific problem — two concrete, evidenced requirements added to the prior review's proposal

The prior review already proposed a layout-continuity fix (segment boundaries currently re-randomise the
hazard/resource layout, confounding within-life development analysis). This session adds two further,
specifically evidenced requirements for a developmental-ecology redesign, rather than restating that
proposal:

1. ~~**Resource/reef spatial reachability.** Section 1b-D found the reef-to-nearest-resource gap
   (4-5 cells) exceeds the agent's sensory radius (2) in every episode of both runs — no version of
   an opportunity-triggered leave-shelter policy can be exercised, tested, or learned under the
   current geometry. A developmental ecology aimed at testing risk/reward contingency needs at
   least some resources reachable from within (or at the edge of) sensory range of the shelter
   zone.**~~
   **[CORRECTED 2026-08-10, see `developmental_ecology_curiosity_foraging_correction_2026-08-10.md`
   Section 1 — left visible rather than deleted, per this repository's supersession convention.]**
   The empirical finding above (the gap exceeds sensory radius) is correct and stands. The
   inference drawn from it — that this forecloses a testable strategy and that the fix is to make
   food sensible from the reef — does not: REE's curiosity/exploration machinery is specifically
   intended to license leaving shelter without a currently sensed target, so
   "sense food from the reef -> leave" is not the only, or the most developmentally interesting,
   pipeline available. The corrected requirement is that resources be **discoverable through the
   exploratory repertoire without requiring pre-departure perception**, plus a perceptible habitat
   cue that probabilistically (not deterministically) predicts elevated resource likelihood — see
   the correction document Sections 1c/4 for the full requirement and design principle.
2. **Decoupling sleep firing from segment-boundary reset.** Section 6's retrospective test was
   confounded specifically because the one sleep firing available coincided with a segment boundary that
   also triggered a full environment reset. A design that lets sleep fire mid-segment (not only at
   boundaries), or that holds environment/layout constant across a boundary a sleep cycle happens to
   coincide with, would let a future retrospective (or prospective) test isolate the sleep-specific
   contribution the way this session's test could not.

Both are additive to, not a duplicate of, the prior review's layout-continuity proposal — reuse rather
than re-propose that one when this is written up as a queued successor.

---

## 9. Long-life welfare instrumentation as experimental hygiene

No inference of consciousness, sentience, or suffering is made or implied by this section. The relevant
existing governance rule is **`SENT-2`** (`governance.welfare.welfare_budget`, `candidate`,
`binds_at_version: v4`): "experiment-level limits on sustained negative-valence exposure, inescapability,
helplessness-like conditions, repeated adverse replay, and persistence of distress-like accumulators...
apply... even while the system is judged non-sentient — to build the habit before moral-patient ambiguity
increases." `SENT-2` establishes the *policy* (cap exposure) but not an *instrumentation* (measure and
report occupancy). **Recommendation, framed as informing/operationalising `SENT-2` rather than a new
governance rule:** if a future successor gives REE a substantially longer or richer continuous life
(Section 8), add lifetime affective-occupancy reporting (fraction of steps above/below simple
within-run percentile thresholds on dread, harm-event rate, `in_reef` fraction) as a standard reported
statistic alongside the scientific metrics — conservative experimental/ethical hygiene, exactly as `SENT-2`
already anticipates, not a claim that REE has welfare in a biological or phenomenal sense. This should be
raised at `/governance` alongside `SENT-2`/`SENT-4`'s eventual v4 binding, not built now.

---

## 10. Overall synthesis, tested rather than assumed

The candidate synthesis offered in the brief is **partially supported, with the specific overreach
identified and removed**:

- **Supported:** the 906 lineage shows an integrated, inspectable agent whose coarse behaviour includes
  genuine, replicated, protective shelter use (Section 1b-A) and switching frequency that comfortably
  clears the ecology's own pre-registered activity bars (Section 1b-B). REE's aggregate outcome — survive,
  spend meaningfully less time exposed than sheltering, acquire some resources — is closer to what an
  ecologically-framed competence measure would call adequate than a pure exploration/movement-maximising
  measure suggests (Section 2).
- **Not supported, and should not be asserted:** "REE independently converged on the predicted reef
  strategy" in the strong sense (opportunity-triggered exit, threat-triggered return). The opportunity
  test is structurally foreclosed by the environment's own geometry; the threat-return test is weak,
  distance-dependent, and inconsistent across seeds. The coarse phenotype is better explained by the
  *already-diagnosed* `MECH-309` (monomodal collapse without a rule-apprehension layer) landing on the
  safety pole of the two designed attractors than by genuine discriminative context-sensitivity — this
  should be recorded as a corroboration of `MECH-309` in a new context, not a fresh discovery.
- **Also supported, newly:** the affective picture is not evidence of chronic distress by any available
  proxy, but the channel defect that already blocked a positive-valence reading (`excite`) now
  demonstrably blocks a negative-valence reading too (`dread`) — the "cannot yet determine overall
  balance" formulation should be widened accordingly (Section 3d).
- **Also supported, newly:** what actually surprises REE is measurably different from what the
  experimenters inject as "important" (Section 4), and there is a real, if modest and previously
  invisible-without-baseline-correction, familiar-event surprise decline for the ecology's most common
  recurring transition (Section 5).
- **Also tested and found unsupported:** the "sleep produces visible refinement" impression, when tested
  retrospectively against a proper non-sleep-boundary control group using the only real sleep-firing data
  this lineage has produced, is not distinguishable from the generic segment-reset effect (Section 6).

No item above is chargeable cleanly to "REE FAILED." The strongest REE-adjacent finding (reef strategy
convergence) resolves mostly to an already-tracked mechanism gap (`MECH-309`); the strongest measurement
finding (accumulator contamination) now covers three channels instead of one; the strongest environment
finding (resource/reef unreachability) is a concrete, fixable geometry fact, not a REE competence
question.
