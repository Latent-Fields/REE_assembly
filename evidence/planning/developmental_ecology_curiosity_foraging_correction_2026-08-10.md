# Developmental-Ecology Correction: Food Perceptibility, Curiosity-Discovery Reanalysis, and Probabilistic Resource Priors (V3-EXQ-906 Lineage)

Direct continuation of `organism_lifespan_development_review_906_lineage_2026-08-10.md` and
`reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` (session `relaxed-shtern-75392b`,
2026-08-10). This document does three things: (1) corrects a specific overreach in the prior
review's environment-design requirement, (2) reanalyses the already-collected 906b/906c excursion
data against a different causal question than the prior reviews asked, and (3) proposes a
probabilistic-ecology design principle for the successor already chipped
(`chip-20260810-fishtank-developmental-ecology`), which this document amends rather than
duplicates.

No new experiment is queued or run here. No substrate is changed. This is a re-read of
already-collected episode logs (same category as the prior reviews' bout-level analysis and
surprise-peak browser) plus a design-document correction.

---

## 0. Duplication check (done before any new analysis or proposal)

- Searched `TASK_CHIPS.json` for `developmental ecology`, `resource reachab`, `probabilistic
  forag`, `curiosity`, `906`, `reef` -> found the exact three open chips this document engages
  with (`chip-20260810-fishtank-developmental-ecology`, `-uncensored-survival`,
  `-affect-telemetry`), all spawned 2026-08-10T06:4x by `relaxed-shtern-75392b`, all still `open`
  and unclaimed at the time of writing.
- Searched `claims.yaml` for `MECH-309`, `SD-025`, `MECH-314`, `SD-054`, `V3-EXQ-522` -> all exist
  and are cross-referenced below (Section 4), not re-registered.
- Searched `evidence/planning/*.md` for `sensory radius`, `sensory window`,
  `reef-to-nearest-resource`, `opportunity-triggered` -> the only two planning documents using
  this framing are the two reviews this document continues from; both are addressed directly
  (Section 1).
- Grepped `ree_core/` for curiosity/novelty machinery before assuming any needed to be built
  (Section 3) -- confirmed it already exists and is partially active in this exact ecology.
- Checked `TASK_CLAIMS.json` for active claims on the files this document touches -- a directory-
  scope governance-pause claim (`queue-depth-low-ops-aac785`, `REE_assembly/evidence/`) overlaps;
  per CLAUDE.md this is a NOTE not an arbitration (scope claims aren't arbitrated), and that
  session's task is `claims.yaml` disposition of the 906-lineage reviews, not this document's
  planning-correction work -- different task, `--allow-overlap`'d on this session's own claim.

---

## 1. Correction: resources do not need to be perceptible from the reef

### 1a. The overreach, quoted exactly

`reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 8, item 1, currently
reads:

> "**Resource/reef spatial reachability.** Section 1b-D found the reef-to-nearest-resource gap
> (4-5 cells) exceeds the agent's sensory radius (2) in every episode of both runs — no version of
> an opportunity-triggered leave-shelter policy can be exercised, tested, or learned under the
> current geometry. A developmental ecology aimed at testing risk/reward contingency needs at
> least some resources reachable from within (or at the edge of) sensory range of the shelter
> zone."

The same framing was carried into `chip-20260810-fishtank-developmental-ecology`'s item 2 ("Place
at least one resource within (or at the edge of) the agent's sensory radius of the reef boundary,
so a leave-shelter-for-a-sensed-opportunity policy becomes exercisable and testable").

**The underlying empirical claim in Section 1b-D is correct and is not being retracted**: the
reef-to-nearest-resource gap genuinely does exceed sensory radius 2 in essentially every episode
(re-confirmed below, Section 2a, on both the Chebyshev and Manhattan metric — 91-97% of
departures have no resource within radius 2 of the agent's position). What is wrong is the
inference drawn from it: that this forecloses a testable opportunity-triggered leave-shelter
mechanism, and that the fix is to make food directly sense-able from the reef.

### 1b. Why the inference is wrong

REE's substrate includes curiosity/exploration machinery specifically intended to license
behaviour in the absence of an immediately perceptible extrinsic reward (Section 3 below
establishes exactly which mechanisms, and which of them are actually active in this ecology). A
"sense food -> leave reef -> approach food" pipeline is only one of several ways an
opportunity-triggered strategy could be exercised. A richer, developmentally more interesting
pipeline is:

```
safe base -> curiosity-driven exploration -> encounter/discovery -> appetitive engagement
  -> outcome -> memory/learning -> altered future exploration
```

Under this pipeline, the reef-to-resource gap exceeding sensory radius is not a design failure —
it is close to the point. If food were directly sensible from the reef, "opportunity-triggered
exit" would collapse into simple cue-following (leave when you see food, don't when you don't),
which is a *simpler*, less developmentally interesting problem than the one the reef ecology was
apparently trying to pose. The gap is what makes curiosity-driven discovery a *necessary*
component of any successful foraging strategy rather than an optional embellishment on top of
direct perception.

### 1c. The corrected requirement

Replacing Section 8 item 1's requirement:

> **Resources must be discoverable through the exploratory behavioural repertoire available to
> REE, without requiring them to be directly perceptible before exploration begins.** The
> geometry does not need to change to satisfy this — Section 2 below finds the *current* geometry
> already satisfies a weak form of it (resources are found during a substantial minority of
> excursions). What the ecology is currently missing is not sensory reachability but **learnable
> intermediate structure**: a perceptible environmental/contextual cue, sensible at greater range
> than an individual resource, that shifts the *prior probability* of finding food in a given
> region without guaranteeing it or revealing exact location (Section 4). That is a different and
> more specific gap than "food must be closer," and is additive to, not a replacement for, the
> layout-continuity and sleep-decoupling requirements already in Section 8.

This document does not silently rewrite the original Section 8 text (the evidentiary-integrity
convention this repository already uses for superseded findings — see `claims.yaml`
`evidence_direction: superseded` and the EXQ-lettering supersession policy). Section 8 item 1 in
the source document has been annotated in place with a pointer to this correction; the original
reasoning is left legible rather than deleted, consistent with how a superseded manifest is
handled elsewhere in this repository.

---

## 2. Reanalysis of 906b/906c excursions: the curiosity-discovery causal question

The prior reviews asked "did REE leave shelter *because* it sensed food?" and answered no (by
construction, since food is never within sensory range while sheltered). This section asks a
different question of the same already-collected data: **did REE leave shelter without a
currently sensed extrinsic target, explore, subsequently discover a resource, and change
behaviour appropriately?**

### 2a. Method

Re-read both 906b's and 906c's full episode logs directly (`v3_exq_906b_..._episode_log.json`,
`v3_exq_906c_..._episode_log.json` — 1 seed x 8 segments x ~500 steps each, the same ground-truth
`in_reef`/`resources`/`hazards` fields the prior reviews used). An excursion is a maximal
contiguous run of `in_reef=False`, matching the prior reviews' own definition (64 excursions in
906b, 67 in 906c — reused unchanged). For each excursion, computed, purely from logged
ground-truth positions (no new instrumentation, no model changes):

1. **Departure** — first step of the excursion, and whether *any* resource is within sensory
   radius 2 of the agent's position at that exact step (both Chebyshev and Manhattan distance
   checked; results agree to within a handful of excursions).
2. **Sensory state at departure** — nearest-resource distance at the departure step.
3. **Curiosity/exploration-related internal state at departure** — the existing `mode` classifier
   value, `residue_surprise`, `excite`/`dread`, and `drive` at the departure step. **Caveat, stated
   per the task's own instruction not to force categories telemetry cannot discriminate**: neither
   SD-025's hippocampal novelty signal (`density x (1 - familiarity)`) nor MECH-314's structured
   curiosity bonus is logged per-step anywhere in the episode record — both are internal to
   trajectory/candidate scoring and leave no direct telemetry trace. `mode`/`residue_surprise` are
   therefore used as *proxies*, not as direct readouts of the curiosity mechanism, and are labelled
   as such throughout.
4. **Trajectory before first resource perception** — the step-by-step nearest-resource-distance
   trace from departure to the first step (if any) where that distance falls to <=2.
5. **First resource/opportunity detection** — the step index (relative to departure) at which
   distance first reaches <=2, if it ever does within that excursion.
6. **Transition into approach/appetitive behaviour** — whether `transition_type` reads
   `benefit_approach` at or after the first-perception step.
7. **Acquisition or failure** — whether the `resources` list shrinks (a genuine pickup;
   `resource_respawn_on_consume=False` and `toroidal=False` in both runs, so a count decrease is
   an unambiguous consumption event, not respawn noise) at or after the first-perception step.
8. **Return / continued exploration** — whether the excursion ends by returning to `in_reef=True`
   or is censored by the episode boundary (reused from the prior review's inventory, not
   recomputed).

Script: `excursion_stage_reanalysis.py` (run locally against the two local episode logs; not
committed — a one-off reanalysis script in the same category as the prior sessions' ad hoc
bout-analysis and surprise-peak-browser code, not a reusable library component).

### 2b. Results

| | 906b (n=64 excursions) | 906c (n=67 excursions) |
|---|---|---|
| Resource within radius 2 **at the departure step itself** | 6 (9.4%) | 2 (3.0%) |
| Resource comes within radius 2 **at some point** during the excursion | 27 (42.2%) | 31 (46.3%) |
| Excursion **ends in an acquisition** (resource count drops) | 8 (12.5%) | 11 (16.4%) |
| Of excursions that perceive a resource: subsequently show `benefit_approach` | 27/27 (100%) | 30/31 (96.8%) |
| Of excursions that perceive a resource: subsequently acquire | 8/27 (29.6%) | 11/31 (35.5%) |
| Steps from departure to first perception (mean / median, of those that ever perceive) | 1.7 / 2.0 | 8.7 / 3.0 |
| Departure `mode` distribution | approach 53, assert 9, avoid 1, explore 1 | approach 50, assert 11, avoid 2, explore 3, neutral 1 |

**Finding 1 — departure is almost never accompanied by a directly sensed target, confirming (not
retracting) the prior structural finding, with a small honest exception.** 91-97% of departures
have no resource within sensory range at the moment of leaving. The 3-9% that do are a real,
small minority — worth noting rather than rounding to zero, but they do not change the headline
picture: **the overwhelming majority of excursions are not literal "I see food, I go get it"**
events, exactly as the prior review established, and exactly consistent with the developmental
sequence this document proposes (exploration precedes discovery, not the reverse).

**Finding 2 — a substantial minority, not a majority, of excursions ever bring the agent within
sensing range of a resource at all (42-46%).** More than half of all excursions never perceive a
resource. This is itself informative and was not measured by the prior reviews (which measured
"yields some benefit signal," 73-83%, via the diffuse ambient-benefit field, not literal
within-radius resource perception — a different and much more permissive criterion). Read
together: the diffuse benefit field lets an excursion register partial credit without ever coming
close enough to a discrete resource, while literal discovery-then-approach-then-acquire is a
narrower, less frequent event chain.

**Finding 3 — once a resource is perceived, appetitive engagement is essentially automatic
(97-100% show `benefit_approach`), but perception -> acquisition succeeds only 30-36% of the
time.** The gate that matters for outcome is not "does REE respond appropriately once it notices
food" (it does, almost always) but "does REE come close enough to notice in the first place" and
"does the subsequent approach actually close the distance before the resource is lost/episode
ends/a hazard interrupts." This reframes where any future competence measure should focus: not on
the approach step (already near-ceiling), but on discovery and completion.

**Finding 4 — once perception fires, the agent is usually already close (median 2-3 steps to
first perception), which argues against a picture of long random wandering ending in accidental
contact, for the *subset* of excursions that do perceive a resource.** This is consistent with
directed movement (via the diffuse ambient benefit-gradient the prior review already established,
or SD-025's novelty-biased trajectory scoring, or both) getting the agent into the vicinity before
literal within-radius sensing takes over — not with a slow, undirected diffusion process. The
906c tail (max 82 steps, and a genuine early-vs-late split — mean 21.1 in segments 0-3 vs 3.6 in
segments 4-7) shows the opposite pattern also occurs for a subset. **The early/late split is
reported descriptively, not as a learning finding**: it is confounded by exactly the same
per-segment layout re-randomization the organism review's Section 7 already identified and flagged
as blocking any within-life development claim — a future successor needs the layout-continuity fix
(already in Section 8 item 2, unchanged by this document) before this specific number can be
attributed to learning rather than to which segment happened to spawn resources closer to the
reef.

**Finding 5 — departure `mode` is overwhelmingly `approach`, almost never `explore` (1/64, 3/67).**
This is the honest, slightly deflationary half of this reanalysis, stated per the task's own
instruction not to retrospectively declare behaviour adaptive because it resembles the hoped-for
description: **the existing coarse `mode` classifier's `explore` label essentially never coincides
with the moment of leaving shelter.** This does not mean curiosity machinery had no causal role
(SD-025's novelty bias operates as a continuous trajectory-scoring term, not a discrete mode, so it
would not necessarily surface as an `explore`-labelled departure — Section 3 below), but it does
mean the classifier-visible evidence for "REE explores its way out of the reef" is weak.
**Classified honestly, per excursion type, without forcing a clean split**: departures are best
described as **diffuse-gradient-guided approach with a curiosity-biased trajectory-selection
component that is not separately observable in current telemetry**, not as classifier-labelled
"exploration," and not as literal cue-following (Finding 1 rules that out directly). A
genuinely clean discrimination between "curiosity-driven discovery," "learned search," and "random
wandering with accidental contact" is **not achievable with current telemetry** — this document
does not force it, per the task's own explicit instruction — and would need per-step logging of
the SD-025 novelty term and the MECH-314 score-bias (currently internal, uncomputed-to-log) to
resolve. This is recorded as an instrumentation gap (Section 6) rather than answered by proxy.

### 2c. What this reanalysis does and does not establish

- **Does establish**: departure is not literal direct-cue-following (Finding 1); a substantial
  minority of excursions genuinely discover a resource through movement that started without a
  sensed target (Finding 2); discovery reliably triggers appetitive engagement (Finding 3);
  discovery-to-acquisition, not approach, is the binding constraint on outcome (Finding 3).
- **Does not establish**: that discovery is driven by *curiosity specifically* as opposed to
  diffuse-gradient exploitation, nor that search behaviour improves with experience (Finding 4's
  early/late split is confounded exactly as the organism review already flagged for a different
  measure). Both require instrumentation this ecology does not currently have (Section 6).

---

## 3. Mechanistic grounding: what curiosity machinery is actually active in this ecology

Checked directly against `ree-v3/experiments/v3_exq_906b_full_stack_observational_fishtank.py`'s
`_make_config()` (line ~433-434) and `ree_core/utils/config.py`'s defaults, rather than assumed:

- **SD-025 (hippocampal curiosity drive, `claims.yaml` `candidate`)** — `cfg.hippocampal.
  curiosity_weight = 0.05` (`CURIOSITY_WEIGHT`, line 250). **Active in this exact ecology.**
  Biases CEM trajectory scoring toward regions of higher representational density with lower
  familiarity (`novelty(z) = density(z) x (1 - familiarity(z))`), continuous and weight-independent
  of the resource RBF, decaying via an EMA as a region is revisited (`ree_core/hippocampal/
  curiosity.py`). This is the most plausible mechanistic driver of Finding 4 (fast approach once
  in the vicinity) and Finding 2 (a meaningful fraction of excursions reach a resource at all) —
  it operates as a continuous trajectory-scoring bias, not a discrete behavioural mode, which is
  exactly why it would not surface as `mode=="explore"` (Finding 5).
- **MECH-314 (structured_curiosity_bonus, `claims.yaml` `candidate_substrate_landed`)** —
  `use_structured_curiosity` defaults `False` and is **not set anywhere in the Fishtank driver's
  config** — confirmed absent from `_make_config()` by direct grep, not assumed from the default.
  **Not active in this ecology.** This mechanism (frontopolar/striatal per-candidate novelty and
  uncertainty score-bias at the E3 action-selection step, distinct from SD-025's trajectory-level
  bias) exists, is validated on a different substrate (`V3-EXQ-604c` PASS, GAP-A), and would be a
  natural additional lever for a future successor that wants a *discrete*, more classifier-visible
  exploration signature — but turning it on is a substrate-configuration change, not something
  this document recommends doing without a specific falsifiable question attached (per CLAUDE.md's
  "avoid unnecessary complexity in the first implementation").
- **MECH-309 (monomodal collapse without a rule-apprehension layer, `claims.yaml` `candidate`,
  `v3_pending`, gated on ARC-062/063/077)** — already established by both prior reviews as the
  best-fitting mechanism for the coarse shelter-dominant phenotype. Unaffected by this document;
  cross-referenced, not re-diagnosed. Directly relevant here because a genuinely discriminative
  "sensed-opportunity -> leave; sensed-threat -> return" *policy* (as opposed to the diffuse
  gradient-following this reanalysis found) is exactly what MECH-309 predicts will not emerge
  without a rule-apprehension layer, regardless of how the ecology's resource geometry is
  arranged. **This is a load-bearing caveat for the successor design in Section 4**: making
  discovery *possible* (this document's correction) does not by itself make discovery
  *discriminative/strategic* (MECH-309's gap) — the two are complementary requirements, not
  substitutes for each other.

---

## 4. Design principle: probabilistic developmental ecology

Per the task's instruction not to hard-code a specific implementation if existing abstractions
support something better, and not to over-implement in a first pass, this section states the
**principle**, checks it against what the substrate already supports, and leaves the concrete
parameterization to the successor design (already chipped, Section 7).

### 4a. The three-tier hierarchy

```
reef/shelter        = safe base (existing; harm-rate ratio 1.6-2.4x, established, unchanged)
foraging habitat/context = a perceptible environmental cue correlated with elevated resource
                            probability, sensible at a range comparable to or greater than the
                            reef-to-resource gap -- NOT a guarantee of food
individual resource  = perceptible only once REE is close enough (current radius-2 sensing,
                        unchanged)
```

### 4b. Avoid deterministic cue -> reward mapping

A habitat cue that deterministically predicts food collapses the problem back into simple
cue-following at one remove (leave when the cue is visible instead of when the food is visible —
same shape, larger radius). The cue must change the *prior* probability of encountering food in
that region — presence, exact location, quantity, discovery time, exposure cost, and hazard risk
should all remain uncertain within the cue's footprint. Concretely, the environment's existing
resource field mechanics (each run currently has `num_resources=5` placed independently of any
habitat marker) would need a **region-conditioned resource-placement prior** rather than a fixed
uniform placement — a probability-of-spawn gradient tied to a new perceptible terrain/substrate
feature, not a new deterministic zone type. This is additive to the existing reef/open-water
bipartite layout (`reef_bipartite_layout`), not a replacement for it.

### 4c. What already exists vs what would need building

- The diffuse ambient benefit/hazard proximity fields (`proximity_benefit_scale`,
  `_compute_proximity_fields()`) already give the agent a *continuous* gradient signal beyond
  literal per-cell perception — this is architecturally close to "a perceptible cue correlated
  with resource probability," but it currently tracks the *actual* resource positions each
  episode, not a *stable habitat feature* independent of where resources happen to spawn that
  segment. The gap is specifically that the cue and the resource placement are the same variable
  today (the field *is* a smoothed copy of the resource positions), rather than two correlated but
  distinct variables (a stable terrain feature, and a resource-placement process that is
  *conditioned on* that feature but not identical to it).
- No existing config knob separates "where resources are likely" from "where resources are."
  Building this is scoped to the developmental-ecology successor (Section 7), not to this
  document.

---

## 5. Candidate longitudinal competence measures (for a future successor, not built here)

Restating the task's own list against what this ecology's current telemetry could and could not
support, to avoid proposing a measure that cannot be operationalized:

- **Already computable from current telemetry, reusable as-is on any successor carrying the same
  fields**: search time / steps allocated before first perception (Section 2, this document);
  discoveries per unit exploration (Finding 2's ratio); path efficiency before first perception
  (Section 2b); revisit probability following previous success (would need a stable per-region
  identity across segments, which requires the layout-continuity fix already in Section 8 item 2).
- **Needs the probabilistic-cue mechanism (Section 4) to be meaningful at all**: probability of
  entering high-resource-prior vs matched low-resource-prior regions (there is currently only one
  region kind); calibration between expected resource value and exposure risk (there is currently
  no varying "expected value" signal distinct from the resource field itself).
- **Needs new per-step instrumentation regardless of ecology changes**: any direct measurement of
  whether search policy reflects the latent resource distribution *before* individual resources
  enter sensory range requires logging the SD-025/MECH-314 internal scoring terms (Section 2b/3),
  not just positions and modes.
- **The early-vs-late / same-persistent-agent comparison** the task asks for is already the
  organism review's Section 7 within-lifetime test — cross-referenced, not restated; still blocked
  by the same per-segment layout-randomization confound, which the already-chipped successor
  (Section 7 below) is designed to remove.

---

## 6. Exploration-quality evaluation criteria and the specific instrumentation gap

The task asks that exploration itself be evaluated (state-space expansion, preference for
uncertain/novel states, avoidance of pathological loops, discoveries generated, efficiency gains
with experience, retained stochasticity) rather than assumed adaptive because it looks
exploration-shaped. **This document explicitly declines to score 906b/906c against these criteria
retrospectively**, for the same reason Finding 5 above stopped short of calling the departure
behaviour "curiosity-driven": none of SD-025's novelty term, MECH-314's score-bias, or a
state-visitation count is logged per-step in the existing episode record, so none of
state-space-expansion, novelty-preference, or loop-avoidance can be measured directly from current
data — only inferred indirectly through position traces, which is a much weaker instrument than
the internal signal itself. **This is recorded as a concrete instrumentation requirement for the
next successor** (surface SD-025's per-tick novelty term and, if `use_structured_curiosity` is
ever turned on, MECH-314's score-bias, into the shared telemetry reader — the same pattern already
used for `residue_surprise`/wanting/liking, chip `chip-20260809-906b-surprise-telemetry`), not
attempted here by proxy.

---

## 7. Ecological trade-offs — explicitly deferred, not implemented

Per the task's own instruction ("avoid unnecessary complexity in the first implementation...
establish the minimum ecology capable of distinguishing naive exploration from learned
probabilistic foraging first"), the multi-context ecology (high-risk/high-yield vs low-risk/
low-yield regions, time-varying productivity, a region that degrades, a novel region introduced
later in life) is **not proposed as a first build**. It is recorded here as a validated future
direction, contingent on the single-context probabilistic-cue mechanism (Section 4) landing and
showing a genuine prior-learning signature first. Building multiple contexts before establishing
that the agent can learn even one probabilistic association would make any negative result
uninterpretable (is the failure the multi-context complexity, or the base mechanism?) — the same
reasoning the organism review already applied when it deferred every proposal to a single
successor per confound rather than bundling unrelated fixes.

---

## 8. Reef's role as safe base — reconsidered, not re-targeted

The task asks not to reduce the reef hypothesis to a fixed 50/50 occupancy target and to recover
the original design rationale. **This was already done by the review this document continues
from** (`reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 1a): the actual
pre-registered bars (`V3-EXQ-522`) are `reef_visit_fraction >= 0.05`, `foraging_fraction >= 0.15`,
`zone_transitions_per_ep >= 1.0` — a floor on both sides plus active switching, not a 50/50 target
at all. Cross-referenced, not restated. What this document adds is only the reframing of *why* the
current shelter-dominant phenotype is not disqualifying under an ecological-objective framing
(harm-minimization while remaining alive, not movement-maximization) — already covered by that
same review's Section 2, also cross-referenced rather than repeated here.

---

## 9. Surprise and sleep/memory linkage — cross-reference, not new

Both are already substantively covered by the two prior reviews and are not re-derived here:
selective surprise/habituation (baseline-relative surprise decline on familiar reef-boundary
events, `reef_ecology...` Section 5) and the sleep/segment-boundary confound (`reef_ecology...`
Section 6, `organism_lifespan...` Section 4, both already flagged and already routed into Section
8 item 2 of the successor requirement, unchanged by this document). The task's specific framing —
that a probabilistic ecology gives sleep something meaningful to consolidate (context ->
exploration -> discovery, repeated, then tested pre/post sleep for altered context preference) — is
a genuinely new angle not previously stated, and is recorded as a **future** measure contingent on
both the probabilistic-cue mechanism (Section 4) and the sleep/segment decoupling (already chipped)
landing first; not actionable before either exists.

---

## 10. Welfare instrumentation — cross-reference, not new

Already covered by `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 9
(operationalising `SENT-2`, not a new governance rule, deliberately not built now). This document
adds one line: **a probabilistic-risk ecology (Section 4) that varies exposure cost and hazard
risk by region is exactly the kind of "deliberately introduces uncertainty, resource scarcity and
risk" design the task flags as needing recorded aversive-exposure accounting** — so when Section 4
is eventually built, Section 9's recommendation (lifetime affective-occupancy reporting alongside
scientific metrics) should be applied to it specifically, not only to the base ecology. No new
claim, no new build, no inference of welfare status.

---

## 11. Durable-task corrections made

**`chip-20260810-fishtank-developmental-ecology` amended** (not duplicated) via `chip_ledger.py
amend-prompt`: item 2 of "the three findings this chip must address" and the corresponding
suggested-approach bullet are corrected from "place at least one resource within sensory radius of
the reef" to "ensure resources are discoverable through the exploratory repertoire, and add a
perceptible habitat/context cue that probabilistically (not deterministically) predicts elevated
resource likelihood in a region, per this document's Section 4." The chip's other two findings
(layout continuity, sleep decoupling) are unchanged. The amendment is recorded in the chip's
`prompt_history` per the ledger's own convention; the original (now-superseded) wording is not
deleted from that history.

**`chip-20260810-fishtank-uncensored-survival` and `chip-20260810-fishtank-affect-telemetry`** —
read in full; neither references the food-perceptibility framing; left unchanged.

---

## 12. Eight-item durable-representation checklist (per the task's explicit request)

| Item | Status | Where |
|---|---|---|
| Probabilistic developmental ecology | **Not previously represented — this document is the first.** | Section 4, this doc |
| Curiosity-driven foraging analysis | **Not previously attempted as a distinct analysis — this document is the first.** | Section 2, this doc |
| Continuous-life semantics | Already tracked, code-verified | `organism_lifespan...` Section 1 |
| Longitudinal competence measures | Already tracked, partially blocked by a named confound | `organism_lifespan...` Section 7; extended Section 5, this doc |
| Selective surprise/habituation analysis | Already tracked | `reef_ecology...` Section 5 |
| Sleep separated from segment resets | Already tracked, already chipped | `reef_ecology...` Section 6/8 item 2; `chip-20260810-fishtank-developmental-ecology` |
| Corrected affect/valence instrumentation | Already tracked (SD-RESIDUE-VALENCE-BOUND, extended to `dread`) | `reef_ecology...` Section 3b |
| Conservative long-life welfare instrumentation | Already tracked, operationalising SENT-2 | `reef_ecology...` Section 9; extended Section 10, this doc |

---

## 13. What this document did not resolve

- Whether SD-025's continuous novelty bias is *actually* the mechanism behind Finding 4 (fast
  post-departure approach), as opposed to the diffuse ambient benefit-field gradient the prior
  review already established, or some mixture — both are plausible from available telemetry and
  cannot be separated without the instrumentation gap named in Section 6 being closed first.
- Whether MECH-314's structured curiosity bonus, if enabled, would produce a more classifier-
  visible `explore`-mode departure signature than SD-025 alone currently does — not tested, would
  require a substrate-configuration change out of scope for a reanalysis document.
- The concrete parameterization of the probabilistic habitat-cue mechanism (Section 4) — left to
  the amended successor chip, per the task's own instruction not to over-implement in a first
  pass.

---

## Decision log

- 2026-08-10: Corrected `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 8
  item 1 in place (annotated, not deleted) and amended `chip-20260810-fishtank-developmental-
  ecology` to remove the "resources must be sensorially reachable from reef" requirement, replacing
  it with a discoverability-via-exploration requirement plus a probabilistic habitat-cue
  mechanism. Motivated by direct user correction, not a self-identified error. (session:
  angry-heisenberg-e8fec7, worktree)
