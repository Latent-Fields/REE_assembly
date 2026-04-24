---
nav_exclude: true
---

# Waking-Phase V_s Invalidation: Runtime Trigger + Local Accumulator

**Claim cluster:** MECH-287 (broadcast invalidation trigger, NEW), MECH-284 (V_s residual
accumulator, REFINED operational definition), MECH-269 (anchor selection + dual-trace
reset criteria, REFINED)
**Status:** candidate, v3_pending
**Phase status (substrate):** Phase 1 (per-stream V_s) IMPLEMENTED; Phase 2 (event
segmenter MECH-288, anchor sets, per-region V_s, invalidation trigger MECH-287)
IMPLEMENTED; Phase 3 online arm (MECH-284 staleness accumulator + MECH-269 hysteresis
consumer) IMPLEMENTED 2026-04-24; Phase 3 offline arm (MECH-285 sleep-priority
readout) DEFERRED.
**Registered:** 2026-04-22
**Origin exemplar:** V3-EXQ-475 (re-run of V3-EXQ-471 with SD-036 GABA decay enabled)
showed 5-6 PAG freeze releases per seed but ~12 re-commits per release, with all 1000/1000
eval steps in freeze. SD-036 decay and MECH-279 freeze exit are firing correctly; the
endogenous driver of re-commit is the hippocampal proposer pulling avoid-flavoured
trajectories from the original anchor. There is no waking-phase signal that downweights
the anchor as evidence accumulates that it no longer fits.
**Lit-pulls:**
- `evidence/literature/targeted_review_waking_v_s_invalidation/` (12 papers +
  SYNTHESIS.md, 2026-04-22) — origin pull, drove MECH-287 registration.
- `evidence/literature/targeted_review_v_s_foundation/` (12 papers + SYNTHESIS.md,
  2026-04-22) — foundation pull commissioned for Phase 2 substrate work; covers
  schema-region granularity (verdict 1), multi-map coexistence and dual-trace
  modes (verdict 2), per-stream V_s as projection-readout of mixed-selectivity
  integrated code (verdict 3), splitter-cell anchor types (verdict 4), and the
  upstream anchor-side comparator stage of the MECH-287 trigger (verdict 5).
- Cross-references: `targeted_review_connectome_mech_269/` (replay content),
  `targeted_review_homeostatic_override/` (LC/orexin coupling).
**Depends on:** SD-005, ARC-007, ARC-018, MECH-089, MECH-094, MECH-269, MECH-272,
MECH-285, SD-010, SD-011

---

## Problem

The V_s bidirectional cluster registered 2026-04-22 (MECH-283 forward recognition gate,
MECH-284 residual schema-staleness accumulator, MECH-285 sleep replay priority) closes the
*offline* arm: residuals accumulated across waking get integrated and acted on during
sleep. The runtime arm is incomplete. MECH-284 specifies that staleness accumulates and
is "read-only during waking; consumed during sleep by MECH-285." This works for the slow
schema-revision regime but cannot rescue an agent that is *currently* trapped in an avoid
mode driven by a stale anchor.

V3-EXQ-475 made this concrete. Decay returns z_harm_a below the freeze exit threshold;
the freeze gate releases (5-6 times across the 1000-step eval). But the hippocampal
proposer keeps drawing trajectories from the original avoid-anchor; those trajectories
re-stoke z_harm_a; freeze re-commits within ~80 steps. The lock is not in the harm
stream itself (decay works) and not in the freeze gate (exits work). The lock is in the
*proposer's choice of anchor*, which has no waking-phase mechanism for invalidation.

The biological expectation is that anchor invalidation happens during waking too --
otherwise an agent could not correct a stale schema across a single afternoon, and
clinical phenomenology would not include experiences like "I just realised the threat
is gone" in real time. The architectural commitment MECH-287 + the refinements to
MECH-284 and MECH-269 make is that:

1. **Waking-phase invalidation is a two-circuit system.** A *trigger* event signals
   single-instance schema-fit violations broadly; a *local accumulator* integrates these
   over a per-schema window and emits a downweight on the affected anchor's V_s.
2. **The two circuits are substrate-distinct.** The biology supports separating them
   (LC/DA for the broadcast trigger; OFC for the local accumulator), and the failure modes
   dissociate clinically.
3. **Reset is dual-trace.** When V_s drops below the anchor-reset threshold, the
   predecessor anchor is *marked inactive*, not erased. The new anchor is added; routing
   (MECH-272) decides which is operative under what state.

---

## Foundation lit-pull integration (2026-04-22 Phase 2)

The `targeted_review_v_s_foundation/` SYNTHESIS (12 papers; place-cell remapping,
attractor dynamics, splitter/trajectory cells, schema cells / event boundaries,
multi-trace / pattern separation, comparator / HC-VTA loop, subicular routing)
constrains four substrate decisions in addition to the MECH-287 dual-component
refinement (verdict 5, integrated into Section 1 below).

**Verdict 1 — schema-region granularity (NOT place-cell-field).** The substrate
defaults the V_s region unit to schema / event-segment / action-object scale, with
multi-scale support where the task demands finer resolution. Eichenbaum 2017
establishes that hippocampal coding is multi-dimensional mixed-selectivity at the
cell level with the relevant organisation scale emerging from task structure;
Tse 2007 schemas operate at integrated event/context level; Sols/DuBrow/Davachi
2017 shows event boundaries (not place transitions) drive reinstatement and
consolidation priority. Substrate implication: `attribution_weight(r,
source_streams)` operates over schema regions, not place fields. The accumulator
`staleness[r]` is keyed on schema-region IDs. Place-cell-field-scale resolution
should be available as an option but is not the default unit. Region granularity
itself is also a tunable lever in scaling experiments — see project memory
`project_intelligence_scaling_levers.md`.

**Verdict 2 — dual-trace anchor preservation supports both hard-switching AND
soft re-weighting.** Wills 2005 (attractor morphing, bistable winner-take-all
ensemble switching) gives the hard-switch mechanism; Colgin 2008 (rate remapping)
and Frank 2000 / Wood 2000 (trajectory-cell rate modulation) give the
soft-re-weighting mechanism. Substrate implication: MECH-269 dual-trace must
support BOTH a hard anchor switch (Wills attractor flip) and a soft mixture
re-weighting (Colgin-style graded mixture). MECH-272 routing then treats the
choice between these regimes as a function of V_s magnitude and input ambiguity
rather than committing architecturally to one mode. Section 3 below
(`mark_inactive(a)` + `seek_new_anchor`) describes the hard-switch path; the
soft-re-weighting path is added as a separate routing-level operation that
adjusts mixture weights over the active anchor set without marking any anchor
inactive.

**Verdict 3 — per-stream V_s is a projection-readout of an integrated
mixed-selectivity code, NOT a biological per-stream computation.** Eichenbaum
2017: hippocampal CA1 carries multiplexed independent representations of
multiple dimensions with mixed selectivity at the single-cell level — biology
computes a single integrated mixed code; per-stream readout is downstream
extraction. Vinogradova 2001 grounds the principle that biology computes mismatch
between functionally distinct streams (the principle is biological; the specific
five-stream count z_world / z_self / z_harm_s / z_harm_a / z_goal is an
engineering choice). Yonelinas 2019 contextual-binding theory shows the
integrated code degrades into something more per-stream-like under capacity
constraints, giving the substrate plan a recoverable-fallback grounding.
Substrate implication: register per-stream V_s as a *projection-readout* in the
substrate documentation and naming (`v_s_per_stream_readout`, not
`v_s_per_stream_compute`). This validates the Phase 1 deviation from the
original plan that wired V_s uniformly via an identity proxy at
`HippocampalModule` scope rather than per-stream forward predictors —
architecturally that is the more biology-faithful choice, since the integrated
code lives at the hippocampal scope and per-stream readouts are extracted from
it. Per-stream forward predictors should NOT be added in Phase 2.

**Verdict 4 — splitter-cell support for both pure-place and stream-conditioned
anchors.** Wood 2000 (~one-third pure-place, ~one-third context-dependent
firing on shared stem in continuous-alternation) and Frank 2000 (W-maze
trajectory-cell encoding) establish that anchor encoding conditional on a
stream-mixture / trajectory / context signal is biologically standard, not
exotic. Substrate implication: MECH-269 anchor type catalogue includes BOTH
pure-place anchors (V_s reset on the location signal alone) and stream-mixture-
conditioned anchors (V_s reset conditional on a trajectory / context / intent
signal). The exact ratio is task-dependent and is NOT hard-coded; both types
must be supported and the mix emerges from training.

---

## Mechanism

### 1. MECH-287 (NEW): Dual-component invalidation trigger

A per-step broadcast signal that fires whenever a schema-fit violation is registered
above threshold. Computationally:

```
trigger(t) = { norm(z_pred(t-1) - z_obs(t)) > theta_trigger      OR
               value_PE(t) < -theta_value                          OR
               external_surprise_signal(t) > theta_surprise }
```

When `trigger(t)` fires, an event is emitted on a global trigger bus carrying:

- `t` (time index)
- `magnitude` (which gate fired and by how much)
- `source_streams` (which streams contributed -- z_world, z_harm, z_goal, etc.)
- `current_anchor_set` (which anchor regions were active when the violation occurred)

The trigger event is the *thing the accumulator integrates*. It is not itself an
update -- it is a labelled event broadcast widely so that all downstream accumulators
that care about this region can consume it.

**Biological substrate — DUAL-COMPONENT coupled-stage architecture** (per
`targeted_review_v_s_foundation/` SYNTHESIS verdict 5; supersedes the broadcast-only
framing in the original 2026-04-22 design):

The trigger is not a single broadcast event but the downstream stage of a two-stage
loop. Treating broadcast and comparator as alternative trigger sources misses the
loop architecture biology actually uses.

*Upstream anchor-side comparator stage:*
- CA1/CA3 mismatch comparator (Vinogradova 2001) — hippocampus computes
  match/mismatch between two functionally distinct input streams; output gates
  both intra-hippocampal output and subcortical arousal modulation.
- Subicular routing (O'Mara 2009) — anatomical hub through which hippocampal
  mismatch reaches NAc-VP-VTA. The trigger flows through this pathway; it does
  not bypass it.
- HC-VTA loop wiring (Lisman & Grace 2005) — hippocampal mismatch propagates
  via subiculum-NAc-VP to VTA, which back-projects dopamine to enhance
  hippocampal LTP. This loop is what couples the upstream comparator to the
  downstream broadcast.
- Event-boundary reinstatement support (Sols/DuBrow/Davachi 2017) — event
  boundaries behave like local mismatch signals at the schema/event-segment
  scale, consistent with the comparator firing on schema-region boundaries
  rather than arbitrary single-step latent deltas.

*Downstream broadcast stage* (parallel, partially redundant):
- Locus coeruleus phasic burst (Aston-Jones & Cohen 2005; Sara & Bouret 2012)
- DA generalised PE (Schultz 1997; Gardner, Schoenbaum & Gershman 2018) —
  value-PE arm
- Lateral habenula negative-RPE (Matsumoto & Hikosaka 2007; Bromberg-Martin
  & Hikosaka 2011) — value_PE < -theta_value arm

*Dissociation inside MECH-287:* comparator-loss = silent trigger (CA1/CA3 lesion
analog: no upstream signal to broadcast); broadcast-loss = silent invalidation
(LC lesion analog: comparator fires but no global gain modulation downstream);
both intact = full trigger event. This dissociation is testable separately from
the trigger-vs-accumulator (MECH-287 vs MECH-284) factorial.

### 2. MECH-284 REFINED: Local schema-staleness accumulator

The MECH-284 entry currently says staleness is "read-only during waking; consumed during
sleep by MECH-285." This is correct for the schema-revision read-out, but the accumulator
*itself* must update during waking — that is the only opportunity to integrate trigger
events into a per-region signal. The clarification is:

```
For each schema region r in active_anchor_set(t):
    if trigger(t):
        staleness[r] += attribution_weight(r, source_streams) * magnitude
    staleness[r] *= leak_factor   # slow decay so stale regions clear
```

`attribution_weight(r, source_streams)` is the schema-specific credit assignment step:
which schema regions plausibly contributed to the broadcast event. Biologically this is
the cortical control over LC (ACC/OFC -> LC) — the broadcast trigger is undifferentiated;
the local accumulator does the credit assignment.

The accumulator is read by *two* downstream consumers:

1. **MECH-285** (offline / sleep): the staleness map biases replay priority during sleep
   consolidation. This is the existing read-out.
2. **MECH-269 anchor-reset gate** (online / waking): when `staleness[r]` exceeds
   `theta_reset(r)`, the anchor on region r is marked inactive and a new anchor is sought
   for the current latent slice. This is the new read-out specified here.

The two read-outs share the same accumulator state but operate on different timescales —
sleep consumes the integrated map across many anchors; the online reset consumes a single
anchor's staleness against its own threshold.

**Biological substrate:** OFC representational drift (Wilson et al 2014; Stalnaker et al
2015) is the best candidate for the local accumulator state. The OFC-as-cognitive-map-of-
task-space framing maps directly onto V_s as per-region schema validity; OFC labelling
integrates evidence over trials and reorganises when the underlying state is judged to
have changed. Hippocampal DG / alEC pattern separation (Yassa & Stark 2011; Reagh et al
2018) provides upstream interference-detection signals that feed the accumulator.

### 3. MECH-269 REFINED: Anchor-reset criteria with dual-trace preservation

MECH-269 currently specifies anchor *selection* by V_s gating. It does not specify what
happens when V_s drops below threshold for an active anchor. The refinement:

```
For each active anchor a on region r:
    V_s_anchor(a, t) = V_s(r, t) - staleness[r]
    if V_s_anchor(a, t) < theta_reset(r) for k consecutive steps:
        mark_inactive(a)
        seek_new_anchor(latent_slice(t))
```

**Dual-trace requirement (Bouton 2004).** `mark_inactive(a)` must NOT erase the anchor.
Extinction is new learning, not unlearning; the avoid-anchor and a new safety-anchor must
coexist in the hippocampal anchor set, with **MECH-272 (state-gated routing) deciding
which is operative under what state**. This makes MECH-272 a load-bearing part of the
fix, not just an ancillary mechanism. State-gated routing has to handle anchor mixtures
in waking under the same logic it uses for waking-anchor vs sleep-probe routing.

**`k consecutive steps` requirement.** A single trigger event should not collapse an
anchor — the anchor would oscillate. Requiring `k` consecutive steps below threshold
gives the architecture a hysteresis property analogous to MECH-266 asymmetric mode
hysteresis. Initial value `k = 5` (substrate-tunable).

**Why threshold not graded.** The accumulator is graded; the reset is threshold. Mixing
the two avoids a discrete reset on every staleness perturbation while keeping the graded
accumulator informative for offline replay priority.

---

## Why these three mechanisms together rather than expanding MECH-284 alone

The minimal-change alternative would be: keep MECH-284 alone, expand its functional
restatement to include the trigger event implicitly, expand MECH-269 to include anchor
reset by reading MECH-284 output. This is cheaper to register but gives up two things:

1. **Failure-mode dissociation.** LC hypoactivity (under-trigger), DA dysfunction
   (under-value-trigger), LHb hyperactivity (over-trigger), OFC lesion (accumulator
   broken), alEC hypoactivity (input pathway broken) are biologically distinguishable
   failures that produce distinguishable phenotypes (perseveration, anhedonia, learned
   helplessness, reversal-learning failure, mnemonic discrimination loss). A single
   MECH-284 covering both the trigger and the accumulator collapses this distinction.

2. **Substrate-readiness story.** A trigger-event MECH can be implemented in ree-v3 as a
   per-step signal in the agent loop (similar to how prediction-error signals are
   already wired). The accumulator MECH-284 needs a longer-timescale state machine.
   Separating them lets each be implemented and tested independently.

The cost of registering MECH-287 separately is a single new claim entry. The benefit
is an architecture that maps cleanly onto biology and onto the experiments that would
falsify each component.

---

## Predicted observables (V3 scope)

A V3 experiment validating MECH-287 + refined MECH-284 + refined MECH-269 would measure:

1. **EXQ-475 freeze re-commit resolution.** Re-running V3-EXQ-475 with the runtime
   invalidation circuit enabled (default `theta_trigger`, `theta_reset`, `k=5`) should
   produce: trigger events fire on each freeze release as the agent observes that
   no harm follows; `staleness[r]` accumulates over ~3-5 trigger events; anchor reset
   fires; new anchor selected (probably nearer to current safe location); freeze
   re-commit rate falls dramatically. Predicted: 1-2 freeze episodes total instead of
   20+, eval ends with the agent exploring rather than locked.

2. **Trigger-vs-accumulator dissociation.** Lesion the accumulator only (set
   `attribution_weight` to zero, so trigger events fire but never accumulate) — agent
   should look like vanilla EXQ-475 (releases occur, re-commits dominate). Lesion the
   trigger only (set `theta_trigger` very high, accumulator can never integrate) — agent
   should look the same. Lesion both — same. Lesion neither — resolution. The four-arm
   factorial is the falsifiable architectural prediction.

3. **Dual-trace preservation.** After the agent escapes the avoid-mode, present the
   original threat cue again. The avoid-anchor should still be retrievable (response
   latency, anchor-set inspection) — i.e. extinction does not erase. If MECH-272 routing
   is intact, the agent should respond to the cue again rather than ignoring it.

4. **Sleep replay priority coupling (Q4 from SYNTHESIS).** A waking session with high
   trigger-event load should produce higher MECH-285 replay priority on the affected
   regions than a session with low trigger-event load, even when the offline schema
   inputs are matched. This is the architectural coupling that the lit-pull identified
   as underdetermined; the V3 experiment can test it directly.

Candidate experiment names (not yet queued):
- `v3_exq_NNN_mech287_runtime_invalidation_unlocks_exq475.py` (single-condition: full
  circuit on/off, replicate EXQ-475 conditions; default candidate for V3-EXQ-476)
- `v3_exq_NNN_trigger_vs_accumulator_dissociation.py` (four-arm factorial)
- `v3_exq_NNN_dual_trace_post_extinction_retrieval.py` (extinction + re-cue)
- `v3_exq_NNN_waking_load_to_sleep_priority.py` (Q4 coupling)

Substrate hooks required:
- `ree_core/regulators/invalidation_trigger.py` — new module hosting MECH-287; emits
  trigger events on a queue consumed by the accumulator.
- `ree_core/hippocampal/staleness_accumulator.py` — new module hosting MECH-284 runtime
  state; subscribes to the trigger queue, applies attribution_weight, maintains the
  per-region staleness map; exposes both the sleep read-out (existing MECH-285
  consumer) and the online reset read-out (new MECH-269 consumer).
- `ree_core/hippocampal/module.py` — extend HippocampalModule with anchor-reset gate
  reading the staleness accumulator; preserve old anchors via dual-trace inactive flag.
- `ree_core/cingulate/salience_coordinator.py` — extend MECH-272 routing to handle
  anchor mixtures (active + inactive coexist; routing decides which is operative).

---

## Open design questions

1. **Trigger substrate canonical choice.** LC vs DA vs LHb. The current architecture
   commits only to "broadcast event exists." For substrate implementation, the simplest
   first pass treats trigger as a single computed signal combining the three; future
   refinement could split them. Lit-pull candidate (deferred): Chandler 2014 / Schwarz
   2015 LC modular projections to test schema-targeting.

2. **`attribution_weight` parametrisation.** The simplest first pass weights all regions
   in `active_anchor_set` equally. A more biological version weights by which streams
   contributed (z_harm vs z_goal). A more learned version uses an attribution head that
   trains during sleep on hindsight residuals. Open whether to specify in the substrate
   first pass.

3. **`theta_reset(r)` source.** Per-region threshold or single global. Per-region is
   architecturally cleaner (different schema regions have different normal staleness
   levels) but requires per-region threshold initialisation. Default first pass: single
   global threshold.

4. **MECH-285 coupling magnitude (the SYNTHESIS Q4).** Whether the runtime accumulator
   feeds sleep replay priority *quantitatively* (priority proportional to integrated
   waking staleness) or *qualitatively* (priority depends only on whether staleness
   exceeded the runtime reset threshold). The empirical literature does not discriminate;
   defer to a V3 experiment.

5. **Interaction with MECH-094 hypothesis tag.** Anchor-reset events should probably
   be tagged with MECH-094's hypothesis tag so that the new anchor's first proposals
   are routed as probes (per MECH-269 probe channel) until the new anchor's V_s
   accumulates sufficient anchor-eligibility evidence. Open whether this happens
   automatically or needs explicit specification.

6. **Failure mode to surface as diagnostic.** If `theta_trigger` is set too low, every
   small surprise fires the trigger and the accumulator saturates immediately, producing
   anchor-reset chaos. Architecturally this matches the clinical observation of high-
   anxiety states with "everything seems wrong." Worth surfacing as a diagnostic counter
   (mean trigger fire rate; mean anchor reset interval) rather than relying on the
   parameter sweep to catch it.

---

## Status log

- **2026-04-22** — Design doc written. MECH-287 reserved. Discussion origin: V3-EXQ-475
  evidence (5-6 freeze releases, ~12 re-commits per release, 1000/1000 freeze active)
  shows that SD-036 decay + MECH-279 freeze exit are insufficient without an upstream
  anchor invalidation signal. Lit-pull on waking-phase online V_s invalidation
  (`targeted_review_waking_v_s_invalidation/`, 12 papers) converged on a two-circuit
  architecture: LC/DA broadcast trigger + OFC local accumulator. Recommendation is to
  register MECH-287 separately rather than expand MECH-284, because failure modes
  dissociate clinically and substrate readiness differs. MECH-269 refined with
  dual-trace anchor-reset criteria (Bouton 2004); MECH-272 promoted to load-bearing
  status for the fix because routing has to maintain anchor mixtures.
- Registration in `claims.yaml` follows in same session.
- **2026-04-22 (Phase 2 update)** — `targeted_review_v_s_foundation/` SYNTHESIS
  integrated. Five verdicts incorporated: (1) schema/event-segment as default
  V_s region granularity (NOT place-cell-field), with multi-scale support; (2)
  MECH-269 dual-trace must support both hard-switching (Wills 2005) and soft
  re-weighting (Colgin 2008) modes; (3) per-stream V_s reframed as
  projection-readout of integrated mixed-selectivity code (Eichenbaum 2017),
  validating the Phase 1 identity-proxy decision and ruling out per-stream
  forward predictors as a Phase 2 task; (4) anchor type catalogue supports both
  pure-place and stream-mixture-conditioned anchors (Wood 2000, Frank 2000) with
  ratio emergent from task; (5) MECH-287 trigger refined to dual-component
  coupled-stage architecture — upstream anchor-side CA1/CA3 mismatch comparator
  (Vinogradova 2001) routed via subiculum (O'Mara 2009) into the HC-VTA loop
  (Lisman & Grace 2005) coupled to the downstream broadcast (LC / DA / LHb).
  MECH-287 entry in `claims.yaml` updated with dual-component title, extended
  functional_restatement, and notes cross-reference to both lit-pulls. Region
  granularity also flagged as a tunable scaling lever per project memory
  `project_intelligence_scaling_levers.md` (Daniel's 2026-04-22 aside on
  granularity / latent dim / network depth / sensory granularity coupling).
- **2026-04-24 (Phase 3 online arm IMPLEMENTED)** — MECH-284 staleness accumulator
  landed in ree-v3 as `ree_core/hippocampal/staleness_accumulator.py`, wired into
  `HippocampalModule.tick_anchor_set` between `consume_boundary_events` (Phase 2(ii))
  and `tick_hysteresis`. Integration drains the broadcast event queue (MECH-287
  events) with `attribution_weight` credit over the active anchor set; `tick_leak`
  applies EMA decay `leak_factor=0.995` per call. Region key is `(scale,
  segment_id)` — matches `per_region_vs` partition; `stream_mixture` dropped
  because the accumulator indexes on the event-segment partition the Phase 2
  per-region aggregation already uses. Two new `HippocampalConfig` flags, both
  default False: `use_staleness_accumulator` (instantiates the accumulator for
  diagnostic read-out without changing hysteresis behaviour) and
  `use_mech284_hysteresis` (additionally swaps MECH-269 `AnchorSet.tick_hysteresis`
  from the Phase 2 internal proxy `(tick − last_accessed) * staleness_rate` to
  the MECH-284 accumulator lookup). Both threaded through `REEConfig.from_dims`.
  Attribution modes: `"equal"` (baseline, default) and `"stream_overlap"` (cosine
  similarity between broadcast `source_sources` and anchor's stream mixture).
  Dual-trace `mark_inactive` (NOT erase) preserved from Phase 2 — Phase 3 only
  changes how the hysteresis threshold is evaluated, not the extinction
  semantics. MECH-094 respected via call-site scoping: the accumulator is only
  touched during waking via `HippocampalModule.tick_anchor_set`, which is the
  realised-observation path; simulated/probe content goes through different
  write-gates and does not enter the broadcast queue. Backward-compat gate:
  91/91 preflight + contract regression PASS with flags OFF (bit-identical
  behaviour vs Phase 2). Activation smoke (`/tmp/smoke_mech284.py`) covers three
  ARMs: ARM0 backward-compat (accumulator None when flag OFF); ARM1
  integrate+leak (two-region equal-credit integration gives 0.4975 each after
  one broadcast and one leak tick, matching 0.5 × 0.995 exactly); ARM2
  hysteresis swap (with staleness forced high, MECH-269 `tick_hysteresis` fires
  `mark_inactive` at k=3 under the MECH-284 lookup). V3-EXQ-478 queued as the
  Phase 3 diagnostic validation (2 seeds × 2 arms OFF vs ON; metrics:
  freeze_recommit_count, anchor_reset_count, mean_staleness_peak, action_class_
  entropy). Phase 3 offline arm (MECH-285 sleep-priority readout) explicitly
  deferred — the infrastructure (per-region accumulator, `snapshot()`,
  `get_stats()`) is in place but the sleep-phase consumer is not yet wired.
