# Sleep-Associated Behavioural Transition Investigation (V3-EXQ-906 Lineage)

Second follow-on from the completed 906/Fishtank organism-level reviews and the
developmental-ecology correction
(`developmental_ecology_curiosity_foraging_correction_2026-08-10.md`). This document investigates a
specific human visual observation: an apparently abrupt pre/post-sleep transition from
ballistic/drifting movement to complex, environmentally contingent multi-step navigation. No new
experiment is queued or run. This is a re-read of already-collected episode logs plus a design
document, in the same category as the prior sessions' bout-level analysis and the developmental-
ecology reanalysis.

---

## 0. Duplication check

- `TASK_CHIPS.json`: no open chip mentions `sleep`+`ablation`, `consolidation`+`richness`, or
  `blocked_agency`/`MECH-353` together. The only open sleep-adjacent chip is
  `chip-20260810-fishtank-developmental-ecology` (already twice-amended by this session), whose
  item 3 ("sleep decoupling") is the correct home for this document's prospective design — amended
  again below (Section 9), not duplicated.
- `sleep_substrate_plan.md` GAP-1/GAP-2: a different thread entirely (SWS/REM *write*-diversity
  metrics, gated on `arc_062_rule_apprehension:GAP-B`) — not about organism-level trajectory
  reorganisation. Cross-referenced, not engaged with further; this document's question is
  orthogonal to that gate.
- `organism_lifespan_development_review_906_lineage_2026-08-10.md` Section 4 and
  `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 6 already did real work
  on this exact question (V3-EXQ-909's DV gap; a retrospective 906b/906c boundary comparison on
  harm rate / mode entropy / benefit rate). This document does not repeat either — it (a) grounds
  the `assert` classifier precisely (neither prior review did), (b) extends the existing boundary
  comparison with the richer trajectory-organisation measures the task specifically asks for
  (turning, tortuosity, straight-runs, hazard-conditioned turning, acquisition chaining), (c) adds
  full-episode-grain analysis alongside the existing 100-step-window analysis, and (d) applies
  GOV-FAILLOC-1 explicitly to the reconciliation, none of which the prior two reviews did.

---

## 1. What `assert` actually means — code-grounded, not name-inferred

`classify_mode()` (`ree-v3/experiments/_lib/baselines/affective_fishtank.py:144`), used verbatim
from V3-EXQ-664, applies affect precedence `freeze > assert > shelter > avoid > approach > explore
> neutral`. `assert` fires when `z_block_assert > ASSERT_THRESH` (0.10), **before** the shelter/
avoid/approach checks are even evaluated — so a step inside the reef, or one showing high harm,
would still classify as `assert` if `z_block_assert` clears the threshold first.

`z_block` is **`MECH-353`, "blocked-agency / control-failure affect stream"** — an internal REE
affect signal, not an observer-side or residual/default classification. Per its own module
docstring (`ree_core/affect/blocked_agency.py`): it rises when **an intended action repeatedly
fails to produce its forward-model-predicted outcome, the mismatch is attributed to an EXTERNAL
constraint (not the agent's own motor error), AND the goal/capacity-belief are RETAINED** — "the
energised 'assert / restore' pole," biologically anchored to the RAGE circuit /
frustrative-non-reward literature (Davis & Montag 2019; Papini 2024), explicitly distinct from
harm (needs noxious contact; `z_block` needs none), suffering (opposite pole of the same
controllability axis — capacity-belief COLLAPSED, not retained), and residue (an action *taken* at
a cost, vs `z_block`'s action *prevented*).

**`use_blocked_agency=True` is explicitly set in the Fishtank driver's `_make_config()`**
(`v3_exq_906b_full_stack_observational_fishtank.py:396`, confirmed by direct grep, not assumed) —
this is the real MECH-353 signal, not a disabled-default fallback. Its concrete antecedent in this
ecology is partly identifiable in code: `scheduled_action_block_enabled=True` fires with
`prob=0.4` every `interval=10` steps (confirmed in both runs' `env_config`) and, on firing,
**cancels the agent's chosen move outright — the agent stays put, with no damage and no layout
change, "a pure external constraint"** (`causal_grid_world.py:2230-2236`, the exact per-tick
mechanism the module docstring's "external, not motor-error" gate is built to detect). `z_block`
also accumulates via an EMA and decays via a leak rate on success — so a step classified `assert`
does not require an active block on that exact tick, only that the accumulated signal is still
above threshold from recent ones.

**Correction to a likely implicit equation: `assert` mode does NOT mean sustained straight/
ballistic movement — the data shows the opposite.** Computed `assert_static_frac` (fraction of
`assert`-labelled steps where position did not change from the previous step) across every
100-step window in both runs where `assert` steps existed: 0.65–0.96, i.e. **the large majority of
`assert`-classified steps involve the agent NOT moving.** This is exactly what the mechanism
predicts — a repeatedly-thwarted action attempt is definitionally *not* producing net displacement
— and is the opposite of "long, relatively straight travel." **Do not read the human's
`assert`-adjacent recollection as literally "assert = ballistic drifting."** Section 2 below
re-examines what the actually-ballistic-looking stretches of trajectory are classified as instead.

---

## 2. Reconsidering the pre-sleep behaviour with the corrected `assert` reading

`sleep_cycle_fired_before_this_segment` (a real per-episode log field, not inferred) confirms both
906b and 906c's one real sleep firing occurred **before episode 7** — consistent with, and now
directly verified rather than only cited from, the prior reviews' Section 6/4.

**`assert_rate` in the segment immediately preceding the real sleep firing is close to zero in
both runs, not elevated.** Full-episode `assert_rate`: 906b ep6 (pre-sleep) = 0.002; 906c ep6
(pre-sleep) = 0.0. By contrast, `assert_rate` is substantial in *other*, non-sleep-adjacent
episodes of the same runs — 906b ep3 = 0.598; 906c ep1/ep4/ep5 = 0.49/0.69/0.67. **The episode
immediately preceding sleep is not the run's most `assert`-heavy episode in either run — if
anything it is among the least.** This is a direct, code-grounded correction to any reading that
specifically ties elevated blocked-agency/`assert` to the pre-sleep period.

**What the trajectory immediately preceding the boundary actually looked like (qualitative,
step-by-step, both runs — full table in Section 8):**

- **906b, last 12 steps of ep6**: a genuinely straight, monotonic run — `pos` moves
  `(10,7)->(10,6)->(10,5)->(10,4)->(10,3)->(10,2)`, six consecutive steps in one direction — **while
  classified `shelter`, not `assert`** (the reef-patch geometry plus elevated harm outrank `assert`
  in the precedence order at this point), with `harm_event=True` for 5 of those steps as the agent
  moves directly toward, and briefly onto, a hazard cell (nearest-hazard distance falls to 0), then
  reverses for two steps. **This is the closest thing in either boundary window to the human's
  "long, relatively straight travel" description — and it is `shelter`-classified, not
  `assert`-classified, and it ends in repeated harm, not calm drifting.**
- **906c, last 12 steps of ep6**: the opposite pattern — the agent's position goes fully **static**
  at `(1,1)` for the last 8 of 12 steps (mode oscillating `neutral`/`explore`, one
  `action_blocked=True` event), consistent with the corrected `assert`/blocked-agency reading
  (though this particular stretch classifies `neutral`/`explore`, not `assert`, since `z_block`
  did not clear threshold here) but **not at all consistent with ballistic travel** — this is the
  agent stuck in what is very plausibly a grid corner.

**Honest synthesis**: the pre-sleep window shows genuinely different shapes in the two runs (one
straight-and-harmful, one stuck-and-static), neither of which is well-described as calm ballistic
drifting, and neither of which is `assert`-dominated. The human's recollection of "substantial
`assert`" pre-sleep may describe a *different* stretch of the same long viewing session (not
necessarily the 12–100 steps immediately abutting this specific logged firing), may describe a
different run than the two analysed here, or may reflect a generically real pattern (elevated
`assert` **is** substantial in several episodes of both runs, 0.29–0.69) that the visual impression
associated with "before sleep" without it specifically clustering there in this data. All three are
live possibilities; this document does not adjudicate between them further — see Section 9's
inspectability-artefact recommendation for how a future session could.

---

## 3. Extended boundary reanalysis: local-window vs full-episode, richer measures

Reused the exact retrospective design from `reef_ecology_strategy_affective_occupancy_review_
2026-08-10.md` Section 6 (sleep boundary ep6->ep7 vs the other 6 non-sleep boundaries in the same
run, matched 100-step windows) as a sanity check, then extended it with turning-angle entropy,
straight-run length, tortuosity, action-repeat-rate, `action_blocked` rate, hazard-conditioned
turning, and resource-acquisition counts — none of which the prior retrospective test computed.
Script: `sleep_boundary_trajectory_reanalysis.py` (one-off, not committed, same category as prior
ad hoc analysis scripts).

**Sanity check — reproduces the prior review's numbers exactly** (906b sleep boundary: harm
0.15->0.00, mode entropy 0.0->1.64, benefit 0.30->0.51, all matching Section 6 to the reported
precision), confirming the extension is built on the same data and methodology, not a divergent
re-derivation.

### 3a. Local 100-step window at the sleep boundary: a real shift, still not sleep-specific

| measure | 906b pre->post | 906c pre->post | matched/exceeded by a non-sleep boundary in the same run? |
|---|---|---|---|
| mode entropy | 0.0 -> 1.64 | 0.24 -> 1.67 | **yes** — 906b ep0->1: 0.0 -> 1.99 (larger jump, no sleep) |
| turning entropy | 0.88 -> 1.24 | 0.92 -> 1.15 | **yes** — 906b ep1->2: 0.63 -> 1.17 (comparable, no sleep) |
| mean straight-run length | 3.0 -> 2.78 (shorter) | 2.0 -> 3.16 (longer) | mixed direction across runs — not a consistent signature either way |
| tortuosity | 7.0 -> 6.25 (slightly less tortuous) | n/a (pre net-displacement ~0) -> 10.0 | 906b's other boundaries range 2.6–12.0 pre and post; no outlier |
| hazard-conditioned turning (near vs far) | pre 0.90 vs 1.05 (near < far); post: too few near-hazard turns to compare | pre: too few near-hazard samples; **post 0.88 vs 0.57 (near > far)** | this one 906c post-window value is the one genuinely structured-complexity-consistent signal found (Section 3c) |
| resource acquisitions in window | 0 -> 0 | 0 -> 0 | no window-local acquisition change at the boundary itself in either run |

**Read**: the local-window shift is real (entropy and turning both rise, harm falls, benefit rises)
but is the same magnitude as, or smaller than, shifts seen at several boundaries with no sleep
event at all — extending, with a richer measure set, exactly the conclusion the prior review
already reached from coarser measures (generic segment-reset effect, not distinguishably
sleep-specific).

### 3b. Full-episode grain: no clean "more organised/more successful" post-sleep episode

| | 906b ep6 (pre) | 906b ep7 (post) | 906c ep6 (pre) | 906c ep7 (post) |
|---|---|---|---|---|
| assert_rate | 0.002 | 0.0 | 0.0 | 0.0 |
| mode entropy | 0.757 | 1.187 | 1.776 | **2.134** |
| turning entropy | 0.885 | 0.838 (lower) | 1.113 | 1.155 |
| mean straight-run | 5.1 | 4.71 (shorter) | 3.56 | 3.37 (shorter) |
| tortuosity | 26.3 | 22.0 (less tortuous) | 11.1 | **36.3 (much more tortuous)** |
| resource acquisitions | 1 | **0** | **4** | 2 (fewer) |

**This is a genuinely mixed, honest result, stated plainly rather than forced toward the hoped-for
direction**: 906b's post-sleep episode has **zero** resource acquisitions across its full 500 steps
(fewer than its immediate predecessor) and slightly *lower* turning entropy and shorter straight
runs than the pre-sleep episode — the opposite of "more organised and more successful." 906c's
post-sleep episode is more tortuous (consistent with more complex navigation) but acquires *fewer*
resources than its predecessor (2 vs 4). **Neither run shows the full package the human described
(complex navigation AND repeated successful acquisition) at the full-episode grain.** This does not
retract the local-window finding (3a) or the qualitative texture (Section 2, Section 8) — it means
whatever local shift exists at the boundary does not propagate into a cleaner whole-episode
signature, which is itself informative: **the n=1-firing, environment-reset-confounded design
cannot currently distinguish a genuine but localised consolidation effect from ordinary
episode-to-episode variability**, which is exactly the discriminating design gap Section 9
addresses.

### 3c. The one structured-complexity-consistent signal found, reported without overclaiming it

906c's post-sleep 100-step window shows mean turning angle **0.88 rad when within 3 cells of a
hazard vs 0.57 rad when farther** — turning *more* near a hazard than away from one, the specific
"structured adaptive complexity" signature the task asks to distinguish from mere entropy increase
(hazard-conditioned turning, not turning per se). **This is a single run, a single window, and the
pre-sleep comparison value is unavailable (too few near-hazard turning samples in that window to
compute a rate at all)** — it cannot be compared against its own pre-sleep baseline, let alone
ruled out as coincidence via a non-sleep-boundary control the way Section 3a's other measures were.
Recorded as a genuinely observed, non-fabricated data point, explicitly not treated as confirming
evidence.

---

## 4. Reconciling with V3-EXQ-909: did it test the same phenomenon?

**No — established precisely, not assumed.** Re-confirming and extending
`organism_lifespan_development_review_906_lineage_2026-08-10.md` Section 4's finding: V3-EXQ-909's
pre-registered pass rule is `sws_slot_diversity > 0.01 OR replay_diversity_index > 0.01`, both
**internal sleep-mechanism diversity metrics** (mean pairwise cosine distance between replayed
memory slots; distinct regions replayed / draws-per-cycle) — not behavioural measures of any kind.
The only before/after field in its data, `post_sleep_z_goal_before`/`_after`, checks that the
goal-latent vector survives the sleep pass numerically intact (bit-identical in every sampled
record) — an internal-state retention check, not a behavioural comparison.

**Direct comparison, stated explicitly per the task's instruction:**

| What V3-EXQ-909 measured | What changed visually in the Fishtank (the human observation) |
|---|---|
| Diversity of which memory slots got replayed (`sws_slot_diversity`) | Diversity/organisation of the agent's *movement trajectory* |
| Diversity of which spatial regions got replayed (`replay_diversity_index`) | Whether movement responds to hazard *geometry* (turning near threats) |
| Whether the goal-latent vector is bit-identical before/after sleep | Whether *behaviour* differs before/after sleep |
| Waking mode-entropy of the segment *preceding* a firing | Nothing about the segment *following* a firing — 909 logs no such field at all |

**There is no overlap.** 909 cannot speak to the human's observation in either direction — it is
not a null result on the right DV, it is a result on a *different* DV entirely. Per GOV-FAILLOC-1,
this is squarely **MEASURES**, and more specifically a sharper case than "the measure was too
coarse": **the measure was never aimed at this phenomenon at all.**

**One partial exception, precisely characterised rather than ignored**: 909 did log
`waking_mode_entropy_bits_prior_segment` per firing (45 firings, 3 seeds) and did compute
`r(waking mode-entropy, sws_slot_diversity) = 0.393` — a genuine, if weak, attempt at exactly the
richness-covariation question Section 5 below asks about, for the *sleep-mechanism-diversity* side
of the chain (not the behavioural-reorganisation side). The prior review already judged this
correlation inconclusive because both variables sit near their measurement floor
(`sws_slot_diversity` mean 2.3e-04; `replay_diversity_index` exactly 0.02 with zero variance on
every one of 45 firings) — restated here, not re-litigated: **909 partially anticipated the
richness question for one link of the chain, got a floor-dominated non-answer, and never asked it
for the behavioural link at all.**

---

## 5. Sleep as history-dependent: classifying existing runs by experiential richness

Per the task's framing, "does sleep improve REE" is underspecified — the well-formed question is
whether sleep *consolidates a particular preceding history* into altered subsequent behaviour.
Classifying the sleep-relevant runs on record by what preceded the firing(s):

- **906b's one firing (before ep7)**: preceded by 6 full episodes (~3400 steps) of rich, varied
  ecological experience — hazard encounters, resource excursions (established: 64 excursions
  across the run), harm events, a mix of modes. **Rich.**
- **906c's one firing (before ep7)**: same — 6 episodes, ~3400 steps, 67 excursions. **Rich.**
- **V3-EXQ-909's 45 firings across 3 seeds**: preceded by segments of the *same* Fishtank
  substrate (per the organism review, 909 reuses the 906b/906c-tier ecology) — so also
  ecologically rich in principle, **but the richness was not held constant or varied as an
  independent variable**; it was measured post hoc (`waking_mode_entropy_bits_prior_segment`) and
  correlated against sleep-mechanism diversity only, never against post-sleep *behaviour* (Section
  4). **Rich but uncontrolled, and only weakly interrogated.**

**Do those sleep effects covary with richness?** Not testably, from existing data, for the
behavioural question — because the one measure that would show it (post-sleep behavioural
reorganisation) was never logged for any of these runs. For the internal-diversity question, the
one correlation available (`r=0.393`) is floor-dominated and inconclusive (Section 4). **This
document does not classify any existing run as "impoverished" — every sleep-adjacent run on record
happens to follow rich waking experience** (the Fishtank's minimum is already a multi-hundred-step,
multi-hazard, multi-resource segment) — so the specific comparison the task raises (does a rich
history produce a detectable effect where an impoverished one does not) **cannot be run from
existing data at all; there is no impoverished-history sleep firing on record to contrast against.**
This is itself the finding: the richness-dependence hypothesis is *untested*, not weakly supported
or refuted, because the contrast case does not exist yet.

Per the task's own explicit instruction, **this is not used to invalidate 909's null-ish result** —
909's finding (near-degenerate replay diversity, `sws_slot_diversity`/`replay_diversity_index` both
near floor) stands on its own terms as a finding about the *mechanism's internal diversity*,
unaffected by the fact that its preceding-richness question was never connected to a behavioural
outcome.

---

## 6. The confound, restated precisely, plus what persists vs resets

Reconfirming, not re-deriving, `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md`
Section 6 and `organism_lifespan_development_review_906_lineage_2026-08-10.md` Section 1: **sleep
and environment/segment reset are confounded in the existing data — the correct statement is that a
sleep-associated boundary in a rich trajectory was followed by an apparent transition, not that
sleep caused it.**

What persists across this boundary vs what resets (from `ree_core/agent.py` `reset()` and
`causal_grid_world.py` `reset()`, code-cited in the organism review's own Section 1, restated here
for this document's self-containedness): **persists** — trained weights, the residue field's
accumulated identity, theta-buffer contents, memory/hippocampal state. **Resets** — hazard/resource
layout (freshly randomised), agent spawn position. **This is the mechanism behind the specific,
sharp point raised in Section 7 below**: even a perfectly-functioning consolidation pass has
nothing useful to express about *spatial* structure, because the spatial structure it might have
consolidated is destroyed at the same tick.

---

## 7. GOV-FAILLOC-1 applied to the whole causal chain

curiosity -> exploration -> ecological experience -> memory/trace formation -> sleep/replay/
consolidation -> altered prediction/search policy -> increased ecological competence, localised
against what this and the prior reviews actually established:

| Link | Status | Localisation |
|---|---|---|
| Was meaningful experience generated? | **Yes, confirmed** | Neither — 906b/906c genuinely produced rich, varied experience (established, prior reviews) |
| Was it encoded (available for replay)? | Partially confirmed | Mechanism — residue field / hippocampal RBF density accumulate continuously (architectural fact); content of what specifically got encoded before this firing is not separately verified |
| Was it available to replay? | **Yes mechanically, but degenerate in practice** | **Mechanism — `replay_diversity_index` is exactly 0.02 (1 unique region / 50 draws) on every one of 45 firings, zero variance.** Already diagnosed as a likely structural bug, not this document's finding (organism review Section 12d) |
| Did replay occur? | Yes | Neither — firings are logged events, undisputed |
| Did relevant internal state change? | **Unverified beyond one field** | Measures — only goal-latent bit-identity is checked; no other internal-state pre/post comparison logged |
| Was learned information retained after waking? | **Not logged** | Measures — no field exists for this |
| Did the post-sleep environment provide an opportunity to express it? | **No, structurally** | **Environment — the same boundary that fires sleep re-randomises the hazard/resource layout, so any consolidated *spatial* knowledge is invalidated at the exact moment it would need to be expressed** (Section 6) |
| Did the behavioural measure capture expression? | **No** | **Measures — V3-EXQ-909 never logged post-sleep behaviour at all (Section 4); this document's own retrospective reanalysis (Section 3) is the first attempt, and remains n=1-firing-per-run and reset-confounded** |

**Net read, stated at the same level of caution the organism review used for its own table**: no
single link is cleanly "REE failed." The chain has at least one confirmed mechanism-layer defect
(replay diversity collapse) and at least two measurement-layer gaps (no post-sleep behavioural
logging anywhere; no internal-state-change logging beyond one field) and one environment-layer
self-defeat (reset destroys exactly the content sleep would consolidate). **A null or ambiguous
final behavioural effect, if one is eventually measured cleanly, would currently be
unattributable to any single link — this table is what "instrument enough of the chain to
localise failure" (the task's own instruction) currently looks like given what exists.**

---

## 8. Trajectory appendix — representative sequences (inspectability, not just scalars)

Per the task's instruction to retain visual/trajectory inspectability rather than reduce
immediately to scalars. Full 12-step-before/12-step-after tables at the sleep boundary, both runs
(`t`, `pos`, `action`, `mode`, `transition_type`, `harm_event`, nearest-hazard distance,
nearest-resource distance, `action_blocked`):

**906b, last 12 steps of ep6 (pre)**: a monotonic straight run `(10,7)->(10,6)->(10,5)->(10,4)->
(10,3)->(10,2)`, six steps in one direction, classified `shelter` throughout (not `assert`), with
`harm_event=True` on 5 of 6 as the agent moves directly onto a hazard cell (nearest-hazard distance
reaches 0), then two steps reversing away.

**906b, first 12 steps of ep7 (post)**: short movement into the reef (`reef_entry` at t=2), then
five consecutive ticks static at `(9,4)` (mode `shelter`), one genuine `action_blocked` event at
t=10, `benefit_approach` transition-type throughout — settling behaviour, not the complex
multi-directional navigation the human described, in this specific 12-step window.

**906c, last 12 steps of ep6 (pre)**: position goes static at `(1,1)` for 8 of 12 steps
(`neutral`/`explore` modes, one `action_blocked`) — stuck, not ballistic.

**906c, first 12 steps of ep7 (post)**: the one window in this appendix that does visually match
the human's description — `hazard_approach` harm events at t=0,2,3,4,5 with the agent jinking
`(5,7)->(5,6)->(5,5)->(4,5)->(4,5)->(5,5)`, i.e. down, then left, then back right, consistent with
reactive hazard avoidance, before settling into a straighter run toward the reef
(`(6,5)->(7,5)->(8,5)->(9,5)->(10,5)`) and a `reef_entry` at t=8.

**Honest summary of the appendix**: one of four windows (906c post) visually resembles the human's
description closely; the other three do not, in either direction (906b pre is straight but
harmful/`shelter`-labelled, not calm drifting; 906b post is static/settling, not complex; 906c pre
is stuck, not ballistic). **This is not strong support for a clean, general ballistic-to-structured
transition at this specific logged boundary** — it is one partially-matching window, three
non-matching ones, and a real, non-fabricated data point that should inform (not decide) how much
weight the single-firing retrospective design can bear.

**On building a dedicated inspectability tool**: the organism review already proposed a
"top-N surprise-peak inspectability tool" as an unbuilt successor
(Section 10 item 5, that document). A sleep-boundary trajectory browser (extract N steps either
side of every `sleep_cycle_fired_before_this_segment` event across a run, render position/mode/
hazard/resource context) is a natural sibling of that same unbuilt tool, not a separate one — noted
in Section 9's follow-on rather than built here, to avoid building two overlapping small tools
where one general one would serve both.

---

## 9. Durable-task correction: amending the existing chip, not duplicating

`chip-20260810-fishtank-developmental-ecology` (already amended once this session for the
food-perceptibility correction) is amended again via `chip_ledger.py amend-prompt`, extending its
existing item 3 ("sleep decoupling") with:

1. An explicit **sleep-vs-matched-no-sleep ablation arm** (rich waking experience + sleep vs
   matched rich waking experience + a matched wake interval with no sleep firing) — the minimum
   design that actually separates sleep from ordinary elapsed time, which item 3's original wording
   (decouple sleep from segment-boundary reset) does not by itself provide.
2. A pointer to this document's Section 6 finding that **environment continuity across the sleep
   boundary (item 2 of the same chip) is not only needed for within-life-development testing but
   is a *prerequisite* for any sleep-consolidation test to be interpretable at all** — the same
   fix serves both purposes, stated explicitly so a future implementer does not treat them as
   separate asks.
3. A pointer to Section 4's developmental-ecology connection (below) as the strongest version of
   the consolidation test, to be layered on once the probabilistic-cue mechanism
   (`developmental_ecology_curiosity_foraging_correction_2026-08-10.md` Section 4) exists.

The original (twice-prior) wording is preserved in the chip's `prompt_history`, per the ledger's
own convention — not deleted.

**The human observation is recorded here as the durable, hypothesis-generating record, explicitly
distinguished from machine-confirmed quantitative evidence**: *the original Fishtank contained a
visually striking sleep-associated transition from relatively ballistic/drifting behaviour to
apparently structured, environmentally contingent multi-step navigation involving hazard avoidance
and repeated resource acquisition. Sleep causality is unresolved because the transition was
confounded with an environment/segment reset, and existing sleep assays (V3-EXQ-909) do not measure
this specific form of behavioural reorganisation. This session's own extended reanalysis (Section
3) found a real but non-sleep-specific local-window shift, no clean full-episode-level
improvement, and one non-dismissed but unreplicated structured-complexity signal (hazard-
conditioned turning, 906c post-sleep only) — the phenomenon is neither confirmed nor closed.*

---

## 10. Connection to the probabilistic developmental ecology

Cross-referencing, not restating, `developmental_ecology_curiosity_foraging_correction_2026-08-10.md`
Section 4. That mechanism (a perceptible habitat cue shifting resource-prior probability without
guaranteeing food) is a substantially stronger consolidation test than generic post-sleep movement
statistics, for a reason this document's Section 6 makes concrete: it gives sleep **specific,
identifiable content to consolidate** (a context-to-resource-probability association) whose
post-sleep expression can be measured directly (preferential search in the previously-productive
context, reduced surprise on repeat encounters, improved abandonment of unproductive search) —
each of which is a *specific* prediction, unlike "does behaviour look more organised," which
Section 3 already showed is not a clean or consistent measure even with a richer feature set. This
is recorded as the target test for once both the ablation design (Section 9) and the probabilistic
cue mechanism land — not proposed as a near-term build in its own right, per the same
avoid-over-implementation instruction that governed the developmental-ecology document.

---

## 11. Sleep-state architecture — kept separate, per the task's instruction

Cross-referencing `reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 6's own
final paragraph: REE continued locomoting during the one sleep cycle that fired in each run — there
is no sensory-gating/motor-inhibition state during sleep in the current substrate, so every
"before/after sleep" comparison in this document means before/after an *offline consolidation
event*, not before/after a genuine sleep *state*. This document's findings (Sections 3–8) are about
consolidation efficacy and are silent on whether sleep-state implementation (gating, paralysis,
autobiographical-vs-offline memory treatment) is complete — the two questions are independent, and
a future finding on one should not be read as resolving the other.

---

## 12. What this document did not resolve

- Which of the three explanations for the human's `assert`-adjacent recollection (Section 2) is
  correct — a different stretch of viewing, a different run, or a real-but-not-boundary-clustered
  pattern. Not decidable from the two logged firings alone.
- Whether the one structured-complexity signal (Section 3c, 906c post-sleep hazard-conditioned
  turning) is real or noise — n=1, no pre-sleep comparison value available.
- The concrete parameterisation of the sleep-vs-no-sleep ablation design — left to the amended
  chip, per the task's own instruction not to over-implement in a first pass.
- Whether a dedicated sleep-boundary trajectory browser should be built as its own tool or merged
  with the already-proposed surprise-peak browser — flagged (Section 8), not decided.

---

## 13. Addendum (2026-08-11): E3 commitment-gate mechanistic candidate + V3-EXQ-913 reanalysis

Second follow-on, from a fresh user visual observation independently describing the same
transition, refined mid-session to specifically **action-sequence coherence** (reversal
frequency, run length, directional persistence) rather than spatial path smoothness (grids
cannot be spatially smooth). This section does not repeat the duplication check above — it
re-confirms this document, `reef_ecology_...review`, and `V3-EXQ-909` are still the complete
prior-art set (re-checked via `git log --grep`, `TASK_CHIPS.json`, `claims.yaml`) — and adds
code-grounded mechanistic analysis plus a genuine extension of already-collected data that was
sitting unread for this purpose.

### 13a. Mechanistic candidates, checked against what's actually enabled in the Fishtank driver

Four candidates traced through `ree_core/` and cross-checked against `use_*` flags in the
`v3_exq_906b`/`909`/`913`/`916` driver family (none of this document's prior sections did this
code-level check):

- **E3 commitment-gate persistence — the strongest candidate, and genuinely new to this
  thread.** `E3Selector` commits to a pre-planned action sequence when
  `commit_variance < effective_threshold` (`e3_selector.py:3149-3210`); once committed, the
  agent walks `_committed_step_idx` through that sequence **without re-running CEM/softmax
  selection each tick** (`agent.py:6059-6072`). Lower commit-variance -> commits more readily
  and persists longer -> more ticks executed open-loop from one plan -> directly matches
  "longer coherent action runs, fewer local re-decisions." **Not yet confirmed as sleep-linked
  in these runs**: its one identified sleep-modulated input,
  `E3Selector.recalibrate_precision_to` (called only when `use_rem_precision_recalibration=True`,
  default `False`), is confirmed **off** in every `v3_exq_9*`/fishtank driver (grepped). If a
  real effect exists in the data below, it is not running through this designed pathway.
- **Policy chunking (ARC-071/MECH-323/324, sleep-only carve-out MECH-322)** — biologically
  grounded (Albouy 2013 cited in-module) and `use_policy_chunking=True` IS enabled in the
  Fishtank driver, but the flag that lets a crystallised chunk actually influence action
  selection, `use_chunk_proposal_injection`, is confirmed **off** everywhere in the
  906/909/913/916 family (only set in dedicated ARC-071 diagnostic scripts) and the module's own
  docstring states the path is bit-identical to OFF when disabled. **Ruled out** as the operative
  mechanism in the observed runs, though it remains a real, ready-made candidate for a future
  run that explicitly enables injection.
- **SHY normalisation (MECH-120)**, active in the driver, does the *opposite* of a naive
  "sharpens toward the dominant strategy" story: `E1Deep.shy_normalise` shrinks every
  context-memory slot toward the population mean (homogenises, does not sharpen). Its effect on
  trajectory coherence, if any, would be indirect (more consistent shared representations
  feeding E3 scoring) and is currently unmeasured.
- **Noise floor / softmax temperature (MECH-313)** — confirmed **structurally untouched by
  sleep anywhere in the code** (no sleep code path writes to it). This matters for the
  hypothesis below: whatever effect exists cannot be "sleep globally lowered exploration,"
  because there is no mechanism for that in this substrate.
- **Replay content-selection (MECH-285/273)** is confirmed **outcome-agnostic** — staleness-
  weighted or uniform-random sampling, no reward/success term anywhere in either module. This
  weakens any framing of "sleep preferentially consolidates SUCCESSFUL behavioural structure"
  specifically; the mechanism as implemented does not select for good outcomes.

### 13b. V3-EXQ-913 already contains a real sleep-vs-no-sleep ablation, previously unread this way

`chip-20260810-fishtank-developmental-ecology`'s third amendment (Section 9 above) proposed a
sleep-vs-matched-no-sleep ablation arm. **It was already built and run**: V3-EXQ-913
(`ree-v3` `7786455`, ran 2026-08-10T21:32Z, `PASS` as a diagnostic-readiness check,
`claim_ids=[]`, `evidence_direction: non_contributory` — never scored as a hypothesis test).
Its `sleep_ablation_comparison` block logged 5 matched (same seed, same segment index,
hazard/resource layout held constant via `env.reset_to()`) 100-step `WITH_SLEEP` vs `NO_SLEEP`
windows across 2 seeds, already computing turning-angle entropy, tortuosity, and straight-run
length — almost exactly this document's Section 3 metric set. One pair (seed1, seg19) is
degenerate (`NO_SLEEP` side `path_length=0`) and excluded throughout.

**This session extended that data with the action-*label*-level metrics the refined
observation specifically asks for** (reversal rate, action-run length, repeat rate — distinct
from the existing spatial turning/tortuosity, which conflate a 90-degree turn with a full
reversal), plus a proper significance test and a confound check neither this document's
Section 3 nor V3-EXQ-913's own manifest performed. Full method: parsed the 62MB episode log
directly (`v3_exq_913_developmental_ecology_fishtank_20260810T213204Z_episode_log.json`), same
5 matched pairs, same 100-step windows.

**Action encoding note (methodologically important):** `world_rule_shift_enabled=True` (250-tick
interval) periodically permutes the live action-ID -> spatial-direction map. Reversal/run-length
computed on the canonical action-ID inverse pairing (0<->1, 2<->3; action 4=stay has no inverse)
therefore measures **policy-output-sequence structure**, not necessarily literal spatial
backtracking, for windows that straddle a rule-shift. This distinction did not exist anywhere in
this document's prior sections.

| delta (with_sleep minus no_sleep) | seed0/seg1 | seed0/seg11 | seed0/seg21 | seed1/seg9 | sign pattern (n=4 usable) | exact 2-sided sign-test p |
|---|---|---|---|---|---|---|
| `turning_entropy_delta` (existing) | -0.378 | -0.430 | -0.442 | +0.469 | 3 neg, 1 pos | 0.625 |
| `tortuosity_delta` (existing) | -0.881 | -8.0 | -4.025 | 0.0 (tie) | 3 neg, 1 tie (n=3) | 0.25 |
| `mean_run_length_delta` (new) | +10.417 | +4.808 | +5.238 | -85.714 | 3 pos, 1 neg | 0.625 |
| `reversal_rate_delta` (new) | -0.040 | 0.0 (tie) | 0.0 (tie) | 0.0 (tie) | 1 neg, 3 ties (n=1) | 1.0 (uninformative) |

**Stated as plainly as the rest of this document's honest-mixed-result convention: n=4 (or
fewer after ties) cannot reach conventional significance under a sign test even when every
available sign agrees — the best case here (`tortuosity_delta`, unanimous 3/3 after excluding a
tie) is p=0.25. This is a hard sample-size ceiling, not evidence against an effect, and must not
be read as either.** `reversal_rate` sits at a floor (2-6 reversals per 99 transitions across
all 10 windows) and is uninformative at this n — a floor-effect finding in its own right, not a
disconfirmation.

**New, previously unflagged confound, found while extracting spawn positions for the confound
check this reanalysis added:** in **all 5 matched pairs**, the agent's spawn position differs
between the `with_sleep` and `no_sleep` arms at the same segment index (Manhattan distances
5-11 cells on a 12x12 board). `env.reset_to()`'s `layout_continuity_confirmed: true` guarantees
hazard/resource layout continuity only — spawn point is independently re-rolled per arm's own
RNG stream each segment (`v3_exq_913_developmental_ecology_fishtank.py:351-355`, safe-spawn
retry loop). **This is a real, unaddressed confound**: a different starting position (different
distance to nearest hazard/resource/boundary) can by itself change turning and run-length
statistics independent of any sleep effect, and it affects every one of the 5 comparisons in
this data. A separate data-quality note: `seed1/no_sleep/seg9`'s window is near-degenerate (the
agent moves 3 ticks then sits motionless at one cell for the remaining 96, still emitting a
constant action label) — not the manifest's already-excluded `path_length=0` pair, but similarly
artifact-prone and worth reading its row with that caveat.

**Overall read on the extended data, stated at the same calibration as this document's existing
findings**: weakly-consistent-but-underpowered, now with one new corroborating metric
(`mean_run_length`, 3/4 pairs favouring `with_sleep`, same direction as the existing
turning/tortuosity numbers) and one newly-uninformative metric (`reversal_rate`, floor effect),
plus a genuine new confound (unmatched spawn position) that was not checked before and tempers
how much weight the whole `sleep_ablation_comparison` block can currently bear. This is
hypothesis-generating, not confirmatory — consistent with, and not overturning, this document's
existing Section 3/12 conclusions.

### 13c. Refined hypothesis

> Any post-sleep increase in action-sequence coherence in this substrate is more likely to arise
> from increased persistence of E3's commitment gate (lower commit-variance -> longer open-loop
> execution of an already-planned action sequence, reducing per-tick re-scoring) than from a
> "smoothing" of movement per se, a global reduction in stochasticity (structurally excluded --
> sleep never touches the noise floor), or preferential consolidation of specifically
> *successful* behavioural structure (replay sampling is confirmed outcome-agnostic). The
> commit-gate mechanism's only known sleep-linked trigger is disabled in the Fishtank driver, so
> if the V3-EXQ-913 signal above is real, it is running through an unflagged, currently
> unmeasured route -- the single most important open question, not yet the "consolidation of
> successful structure" story the original visual impression suggested.

**Terminology**: prefer **"action-run coherence"** (behavioural-measurement level) and
**"commitment-gate persistence"** (mechanistic-claim level) over "smoothness" (spatial, already
corrected away by the user) or "strategy" (implies interpretation ahead of measurement, per the
Stage-1/Stage-2 discipline in `thought_intake_2026-08-11_behavioural_diversity_umpire.md`).

### 13d. Forward plan (not performed this session; see chip spawns in Housekeeping)

1. **Fix the spawn-position confound** before trusting any future version of this comparison --
   match spawn position across arms at each segment index, not only hazard/resource layout.
2. **Instrument the mechanistic variable directly**: log `E3Selector._running_variance` /
   commit-gate engagement rate per matched window, so a coherence effect (if confirmed) can be
   tied to the commit-gate hypothesis rather than left as a correlation between behaviour and
   an unidentified cause.
3. **Scale seeds** (2 -> at least 5-8) -- the sign-test ceiling in 13b is a sample-size problem,
   not a methodology problem.
4. **Transfer test**: once 1-3 produce a real, well-powered signal, rerun the same ablation in a
   structurally different ecology to distinguish route memorisation from general reorganisation
   from noise (three-way outcome, per the user's own framing).
5. **Blinded umpire**: apply the exact cross-environment discriminability methodology from
   `thought_intake_2026-08-11_behavioural_diversity_umpire.md` to this pre/post-sleep case --
   held-out classifier over the full feature vector (turning entropy, tortuosity, run length,
   reversal rate), tested against a permutation null AND a matched-schedule no-firing control,
   feature-importance inspection only after Stage-1 discriminability passes.

---

## Decision log

- 2026-08-10: Grounded the `assert` classifier (MECH-353 blocked-agency, `scheduled_action_block`
  antecedent) and found it is predominantly a STATIC, not ballistic, signature — a correction to a
  likely implicit reading, not a retraction of the human's observation. Extended the existing
  906b/906c sleep-boundary retrospective test with trajectory-organisation measures (turning,
  tortuosity, straight-runs, hazard-conditioned turning, acquisition chaining) at both local-window
  and full-episode grain; found a real but non-sleep-specific local shift, no clean full-episode
  improvement, and one unreplicated structured-complexity signal. Established precisely that
  V3-EXQ-909 tested a different phenomenon (sleep-mechanism internal diversity) than the one the
  human observed (behavioural trajectory reorganisation), with zero overlap. Applied GOV-FAILLOC-1
  to localise the whole curiosity->consolidation->competence chain. Amended
  `chip-20260810-fishtank-developmental-ecology` a third time (sleep-vs-no-sleep ablation arm).
  Motivated by direct user follow-on request. (session: angry-heisenberg-e8fec7, worktree)
- 2026-08-11: Second follow-on (fresh, independent user observation, refined mid-session to
  action-sequence coherence specifically). Added the E3 commitment-gate persistence mechanistic
  candidate (new to this thread); code-confirmed policy-chunking-injection and MECH-204
  precision-recalibration/broadcast are BOTH disabled in the Fishtank driver family (rules two
  plausible mechanisms out); confirmed noise-floor/temperature structurally untouched by sleep
  and replay content-selection outcome-agnostic. Extended V3-EXQ-913's existing (never
  hypothesis-scored) `sleep_ablation_comparison` data with action-label reversal-rate/run-length
  metrics and a sign test (best case p=0.25, n=4 hard ceiling, not significant); found a genuine
  new confound (spawn position unmatched across arms in all 5 pairs) that was not previously
  checked. Net: hypothesis-generating, not confirmatory. Refined hypothesis + terminology
  recommendation in 13c. Forward plan (13d) chipped, not performed here: fix spawn-position
  match + instrument commit-variance + scale seeds (`/queue-experiment`); ground the
  commit-gate-persistence mechanism biologically (`/lit-pull`, distinct from chunking's existing
  lit-pull); scope a shared, reusable behavioural-trajectory-metrics library/experiment pattern
  (currently reinvented ad hoc across this document, the reef review, and V3-EXQ-913's own
  analysis script) as a separate research/design chip, per direct user request.
  (session: jovial-shannon-35d300, worktree)
