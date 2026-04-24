# MECH-285 Sleep-Replay Seed-Distribution Lit-Pull -- Synthesis

> Created: 2026-04-24
> Scope: 10 entries addressing MECH-285's narrow-vs-broad seed-coverage
> decision, priority shape, timing of inactive-trace replay, salience
> interaction, and dual-trace replay-content.
> Sibling pulls that this synthesis draws on but does not duplicate:
> `targeted_review_connectome_mech_269/`, `targeted_review_v_s_foundation/`,
> `targeted_review_waking_v_s_invalidation/`,
> `targeted_review_connectome_mech_270/`,
> `targeted_review_connectome_mech_271/`,
> `targeted_review_connectome_arc_028/`,
> `targeted_review_sleep_phase_mechanisms/`.

## Verdicts

### 1. Seed-coverage: BROAD (with qualifications)

The most load-bearing finding comes from Gillespie et al. 2021: awake
replay content is enriched for previously-rewarded locations *and* for
places not recently visited, and is decoupled from subsequent choice.
Karlsson & Frank 2009 independently show that remote-environment replay
is as common as local replay during waking pauses -- the seed pool
demonstrably includes representations the animal is not currently in.
Olafsdottir 2015 extends this to unvisited space: seeds can include
anchors the animal has only seen, provided a motivational gating signal
flags them.

Wu & Foster 2014 constrains this: the broad pool is not uniform over
all place cells. Seeds respect experienced topology, with the ripple
substructure mirroring the maze graph. So the broad reading is not
"sample uniformly over the anchor set"; it is "sample over the
experience-structured graph, with weighting".

**Implication for MECH-285:** The narrow (active-anchor-only)
implementation is not biologically faithful. The `AnchorSet`'s
dual-trace preservation must reach the sleep-replay consumer -- inactive
anchors need to remain in the seed pool. The architectural commitment
is to persist a region-to-seed map across `AnchorSet.mark_inactive`,
and to keep MECH-284 staleness accumulating on inactive regions (or
mirror it on a separate inactive-trace channel) so the sleep consumer
can rank them.

### 2. Priority shape: STALENESS-PROPORTIONAL (not threshold-gated)

Michon et al. 2019 show that post-learning replay-event count
correlates with reward magnitude in a graded fashion -- a continuous
relationship, not a step. Closed-loop ripple disruption causally ties
this graded scaling to SWR scheduling itself. Mattar & Daw 2018 give
the normative backing: EVB is smooth in both gain and need terms, and
a threshold-gated implementation leaves utility on the table. Mattar
& Daw specifically predict that staleness-proportional priority is
what an optimal system should do if it is tracking gain.

**Implication for MECH-285:** The default sampler topology is a
softmax / power-weighted distribution over accumulated staleness, not
a categorical "stale-enough-to-replay" flag. The MECH-284 staleness
accumulator's continuous integrate-and-decay output is directly usable
as the priority input; no thresholding step is needed in the sleep
consumer.

### 3. Timing: FIRST-BOUT for broad coverage, possibly delayed for integration

Karlsson & Frank 2009 is the cleanest timing evidence: remote replay
is present during brief waking pauses immediately after motion -- no
long delay required for inactive traces to become replay-eligible.
Combined with Olafsdottir 2015 (preplay of just-seen unvisited space)
and Diba & Buzsaki 2007 (forward and reverse sequences both present
immediately pre-/post-run), the substrate supports first-bout seeding
of broad content.

The one hesitation comes from Schlichting, Mumford & Preston 2015:
representational integration is more likely for *established* memories
than for simultaneously-encoded pairs. This is fMRI, not replay, and
the translation is indirect -- but it hints that while broad seeding
may be first-bout, full schema integration of a newly-invalidated
trace may benefit from a delay (at least one night for the winning
trace to consolidate, subsequent nights for the loser to integrate).

**Implication for MECH-285:** The seed-pool broadening happens on
the first post-invalidation sleep bout -- no temporal gate needed on
the sampling stage itself. However, the downstream MECH-275 / MECH-273
consumers (which integrate replay content into schema / self-model
revisions) may implicitly have a delay: the first bout's inactive-trace
replay may primarily reinforce the new winning trace, and it may take
subsequent bouts for substantive integration of the losing trace to
register. This is a consumer-side property, not a MECH-285 sampler
property. MECH-285 itself can be stateless on timing.

### 4. Salience interaction: DISSOCIABLE ARMS, composed at the sampler

Joo & Frank 2018 synthesise the multi-mode SWR framing: different SWR
types correspond to different cognitive functions, distinguishable by
content and physiology. Retrieval-SWRs (awake decision support) and
consolidation-SWRs (offline schema update) plausibly recruit different
priority signals. McNamara et al. 2014 establish the salience arm
causally: DA activation during encoding biases later SWR reactivation.
Michon et al. 2019 show reward scales replay count.

Gillespie et al. 2021's co-presence of past-reward enrichment *and*
not-recently-visited enrichment within the same replay population is
the closest direct evidence that multiple priority signals are both
active. Under the Joo & Frank multi-mode framing, these signals
likely sit in distinct SWR subpopulations (salience preferentially in
retrieval-SWRs, staleness preferentially in consolidation-SWRs),
converging at the sampler level but dissociable in principle.

**Implication for MECH-285:** The two priority signals (dopamine
salience tag and V_s staleness) are separate write paths on the same
replay-selection stage. They do not need to be arbitrated by an
explicit composition function -- they target different SWR
subpopulations. The MECH-285 implementation should be a staleness-only
modulator on the consolidation-SWR arm, allowing the salience arm
(MECH-074b / McNamara 2014 substrate) to operate independently on
retrieval-SWRs. In conditions where both signals happen to target the
same content, the effective priority is their sum; in dissociable
conditions (low-arousal high-novelty) the two arms produce different
replay content. This is the MECH-285-consistent reading and aligns
with the claim's falsifiability section.

### 5. Dual-trace at replay-content level: SUPPORTED

Karlsson & Frank 2009's remote-environment replay is the strongest
positive evidence that inactive traces (representations of
non-current environments) remain SWR-eligible. The broader MECH-269
/ MECH-270 dual-trace literature (already pulled in sibling reviews)
shows the behavioural dual-trace of Bouton 2004 has hippocampal
neural substrates. Gillespie 2021's not-recently-visited enrichment
is compatible with replay of genuinely remote/stale traces alongside
active ones.

Diba & Buzsaki 2007's forward/reverse duality adds nuance: even
within a single trace, the seed distribution has internal mode
structure. Dual-trace preservation at the replay level may interact
with mode selection in ways not yet characterised.

**Implication for MECH-285:** The Bouton dual-trace reaches the
sleep-replay stage. MECH-285 can trust that `AnchorSet` inactive
traces will generate SWR content, and the MECH-284 staleness
accumulator's continued integration on inactive regions is a
well-motivated design choice. The broad-coverage reading is the
biologically faithful one.

## Implementation recommendation

**BROAD-UNBOUNDED**, staleness-proportional, stateless-on-timing,
dissociable from salience, consumer-scoped.

Concretely for the MECH-285 module:

1. **Seed pool**: all anchors in the AnchorSet whose dual-trace is
   preserved, regardless of current active/inactive flag. No time-since-
   invalidation filter on the pool itself.
2. **Priority function**: softmax over MECH-284 accumulated staleness
   (continuous-weighted), with MECH-284 configured to continue
   accumulating on inactive regions (mirror channel acceptable).
3. **Temporal gating**: none at the sampler stage. Seed distribution
   is a stateless readout of current staleness snapshot at each
   sleep-phase sampling call.
4. **Salience arm**: separate -- MECH-285 modifies only the
   consolidation-SWR priority, not the retrieval-SWR or salience-driven
   replay paths. MECH-074b / DA-tag handling stays where it is.
5. **Mode-awareness**: deferred as a V4 refinement. Diba & Buzsaki's
   forward/reverse factorisation is a real biological feature but is
   not needed for the first MECH-285 implementation; a single scalar
   priority per anchor suffices for the initial sleep-phase sampler.

One-line rationale: Gillespie 2021's co-enrichment of past-rewarded
and not-recently-visited replay content is direct evidence that broad
seed coverage with a staleness-like priority is what the biology does;
Mattar & Daw 2018's EVB framing is the normative rationale; Joo &
Frank 2018's multi-mode SWR synthesis is the scoping constraint that
lets MECH-285 live as a consumer-specific arm without arbitrating
against salience.

## Open question flagged back to v_s_invalidation_runtime.md Q4

The MECH-285 coupling magnitude remains unsettled by this pull. The
literature establishes the *shape* (broad, proportional,
consumer-scoped) but gives no direct range for how strongly V_s
staleness should modulate replay priority in rodent empirical terms.
Mattar & Daw's EVB framework implies a model-specific answer (scale
by gain relative to prior variance), and Michon 2019's reward-magnitude
correlation gives a rough empirical calibration point for the
salience-arm coupling magnitude -- but neither translates directly to
a MECH-285 default coefficient. A V3 EXQ sweep over coupling magnitudes
on the sleep consumer, with action-class entropy as outcome, remains
the cleanest way to settle the in-silico default.

## Clinical mapping (Daniel's interest)

Three clinical phenotypes map cleanly onto MECH-285 dysfunction:

1. **PTSD intrusive replay**: consistent with MECH-094 hypothesis-tag
   loss combined with intact MECH-285 staleness priority. Traumatic
   memory carries extreme epistemic staleness (schema cannot easily
   absorb it) and extreme salience, so both arms drive toward it; the
   missing hypothesis tag means replay outputs are written to
   commitment-relevant consumers (waking intrusions). Treatment target:
   restore tagging function, not suppress replay.
2. **Depressive rumination**: narrow-coverage high-salience loop.
   MECH-285 staleness priority is attenuated (novelty-blind) or
   overridden by dominant salience signal on a small set of
   high-negative-affect anchors; the seed pool collapses around the
   rumination content. Treatment target: broaden the seed pool
   (behavioural activation, novelty exposure) to restore MECH-285
   staleness coverage.
3. **Novelty-blindness in schizophrenia**: MECH-284 comparator
   hypoactivity upstream of MECH-285. Schema-staleness never
   accumulates because the comparator that should write residuals is
   underactive, so MECH-285 sees a flat priority landscape and
   consolidation-SWR content becomes either random or salience-only.
   Testable via resting-state replay paradigms in first-episode
   patients.

These clinical mappings are architectural conjectures, not literature-
supported claims -- flagged as directions for future lit-pulls rather
than verdicts from this one.

## Papers pulled in this review

| # | First author | Year | Venue | Verdict contribution |
|---|--------------|------|-------|----------------------|
| 1 | Olafsdottir  | 2015 | eLife | Broad seed coverage (salience-gated) |
| 2 | Wu & Foster  | 2014 | J Neurosci | Seeds experience-structured |
| 3 | Gillespie    | 2021 | Neuron | Broad + staleness-like priority (closest direct test) |
| 4 | Karlsson & Frank | 2009 | Nat Neurosci | Broad coverage, remote-environment |
| 5 | Schlichting  | 2015 | Nat Commun | Integration timing (weak) |
| 6 | Diba & Buzsaki | 2007 | Nat Neurosci | Forward/reverse mode structure |
| 7 | Michon       | 2019 | Curr Biol | Proportional priority (strongest) |
| 8 | Mattar & Daw | 2018 | Nat Neurosci | Normative EVB backbone |
| 9 | McNamara     | 2014 | Nat Neurosci | Salience arm causal substrate |
| 10 | Joo & Frank | 2018 | Nat Rev Neurosci | Multi-mode SWR scoping constraint |

## Papers NOT pulled (already in sibling reviews)

- Pfeiffer & Foster 2013 -- `targeted_review_connectome_mech_269/`
- Olafsdottir et al. 2018 review -- `targeted_review_connectome_mech_269/`
- Foster 2006 reverse replay -- `targeted_review_connectome_arc_028/`
- Gupta et al. 2010 generative replay -- `targeted_review_connectome_arc_028/`
- Carr et al. 2011 awake replay review -- `targeted_review_connectome_arc_028/`
- Tse et al. 2007 schemas -- `targeted_review_v_s_foundation/`
- Bouton 2004 extinction -- `targeted_review_waking_v_s_invalidation/`
- Tambini & Davachi 2013, 2019 -- cited in SD-032a register, not re-pulled
- Diekelmann 2010 NREM replay -- `targeted_review_sleep_phase_mechanisms/`
- Tang et al. 2017 awake-vs-sleep SWR -- `targeted_review_connectome_mech_269/`
