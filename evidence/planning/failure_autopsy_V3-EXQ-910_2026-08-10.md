# Failure Autopsy: V3-EXQ-910 (MECH-489 defensive-orienting validation)

**Generated:** 2026-08-10T14:21:33Z
**Scope:** single
**Status:** confirmed
**Target:** V3-EXQ-910 (FAIL, `experiment_purpose: diagnostic`, `claim_ids: [MECH-489]`)

Written as part of `/governance`'s Step 1.5 inline autopsy pass. Primary source:
`organism_lifespan_development_review_906_lineage_2026-08-10.md` Section 3, which correctly
identified the trigger-alignment failure and the 100%-withdraw lockup but explicitly left open
*which* trigger implementation was built ("The manifest contains no record of which trigger
implementation was actually used... flagged as follow-on... needs the actual
`defensive_orienting.py` trigger-condition code cross-referenced against the run"). **This
autopsy reads that source and corrects the review's own speculation.**

**Dry-run gate:** clean (`check_dry_run_citations.py`, 0 hits).
**Recording provenance:** `recording_schema: rec/v1`, `substrate_hash`, `machine`/`machine_class`,
`elapsed_seconds` (14313.4s), `seeds: [0,1]` all present.

## Facts

2-arm ablation (`orienting_off`/`orienting_on`), seeds [0,1]. `event_trigger_alignment`:
`limb_damage_injected` n=76/n_aligned=2 (2.6%), `external_hazard_injected` n=65/n_aligned=1
(1.5%), `world_rule_shift_occurred` n=30/n_aligned=0 (0.0%). `decision_alignment`: 206 logged
overrides, decision_counts `{approach: 0, withdraw: 206, resume: 0}`. ON-arm unconditional
movement collapses 15x vs OFF (0.013 vs 0.200) and vs the 12b baseline (0.24).

## Corrected finding: the built trigger IS the recommended onset-detector design

Read directly, `ree_core/pag/defensive_orienting.py` (module docstring, lines 16-34):

> "Trigger (resolves observational_review_V3-EXQ-906b Section 12h's finding that a naive
> `residue_surprise > p90` design under-fires...): a positive-derivative / onset detector over
> TWO already-phasic substrate channels, not one absolute threshold —
> `trigger(t) = (residue_surprise(t) - surprise_baseline(t) > onset_delta_surprise) OR
> (z_harm_s_norm(t) - harm_s_baseline(t) > onset_delta_harm_s)`, baselines are slow EMAs, updated
> ONLY while NOT orienting."

This is **exactly** the derivative/onset-detector design the prior review recommended, not the
naive absolute-threshold design it speculated was likely built. The near-zero alignment is
**not** a "the prior warning wasn't carried into the build" defect — the build correctly
implemented the recommended design and still fails to align with the specific ground-truth
event set. This is a more interesting and more precise finding than the speculation it replaces.

## New finding: a decision-layer scale mismatch structurally biases every override toward withdraw

Read directly, `ree_core/agent.py:8008-8022` (Component 4/5, the override→action-decision step):

```python
if _do_out.override_fired and self._current_latent is not None:
    _do_zw = self._current_latent.z_world
    _do_benefit = float(self.residue_field.evaluate_benefit(_do_zw).mean().item())
    _do_harm_val = _do_harm_s_norm   # = z_harm_s.detach().norm().item()
    _do_eps = float(getattr(self.config, "orienting_decision_epsilon", 0.01))
    if _do_benefit > _do_harm_val + _do_eps:
        self._orienting_decision = "approach"
    elif _do_harm_val > _do_benefit + _do_eps:
        self._orienting_decision = "withdraw"
    else:
        self._orienting_decision = "resume"
```

`_do_harm_val` is an **L2 vector norm** — by construction non-negative, and non-zero whenever
`z_harm_s` carries any signal at all, regardless of the sign or magnitude of the triggering
event's actual valence. `_do_benefit` is `evaluate_benefit(z_world)` — an RBF-kernel "attraction
value... higher = closer to a previously-beneficial region" (`ree_core/residue/field.py:661-670`),
which reads near-zero unless the agent is standing very close to a region it has previously
found beneficial (confirmed elsewhere: both fishtank reviews independently characterize the
benefit field as diffuse and modest in magnitude). **Comparing a structurally non-negative norm
against a near-zero-unless-close-to-resource attraction value means `_do_harm_val` wins the
comparison almost unconditionally** — independent of whether the specific triggering stimulus
was actually good, bad, or neutral. This is a **units/scale mismatch**, not a threshold-tuning
slip: no choice of `orienting_decision_epsilon` fixes a comparison between two quantities on
different, non-commensurable scales.

This single bug is sufficient on its own to explain the observed 0/0/206 approach/resume/withdraw
split, independent of whether the trigger fired on a "correct" event.

## Claim-layer map

**MECH-489** (candidate, `mechanism_hypothesis`, `v3_pending: false`, depends_on SD-099/MECH-279/
MECH-395/MECH-482/MECH-483/MECH-205). The claim is a **compound, five-component chain**: "freeze-
arrest → orient/identify → epistemic-sufficiency-override → valence-gated approach/withdraw/
resume." Its own pre-registered `what_would_answer` names three FALSIFYING signatures, one of
which this run's trigger-alignment data matches closely: *"the trigger still under-fires on the
ground-truth event set despite the two-channel redesign (channel choice was still wrong, not
just calibration)."* Its CONFIRMING signature required alignment plus ON-arm coupling numbers
moving well past OFF-arm incidental baselines toward "a sharp, deterministic signature" — the
opposite happened: ON-arm's `p_moved_given_spike` (0.28) and `p_modechange_given_spike` (0.14) sit
at or below both the OFF-arm legacy proxy (0.296/0.283) and the 12b baseline (0.443/0.154), not
above them.

**Did the experiment test the claim fairly?** Split by sub-component:
- **Trigger/identification** (Components 1-3): fairly tested. Sample-size preconditions cleared
  (76/65/30 pooled events, all far above the n≥3 floor), the recommended design was built
  correctly, and it still under-fires — this legitimately hits the claim's own pre-registered
  falsifying signature #1.
- **Valence-gated decision** (Components 4-5): **not** fairly tested. The scale-mismatch bug
  means the observed 100%-withdraw pattern cannot distinguish "the mechanism does not genuinely
  valence-gate" from "the mechanism's arithmetic has a units bug that always resolves to
  withdraw regardless of input." This sub-component's test is confounded by an implementation
  gap, not informative about the claim.

## Biological reference

Sokolov orienting-reflex (the module's own stated anchor) is a real, well-grounded biological
target for the trigger/identification chain — a phasic, novelty/deviation-driven arrest-and-orient
response is well established. The specific channel choice (unsigned prediction-error surprise +
sensory-discriminative harm norm) is a reasonable translation of "unexpected, not-yet-identified
onset." The MEASURES finding below (residue_surprise's own composition in this ecology) refines
rather than contradicts the biological translation: the channel type is right, but this
substrate's specific implementation of it is dominated by a different event class than the one
the validation targets.

## Corroborating MEASURES finding (independent, from the sibling reef-ecology review)

`reef_ecology_strategy_affective_occupancy_review_2026-08-10.md` Section 4 (the surprise-peak
browser, built and run independently of this trigger-alignment question) found: **zero of the
top-8 `residue_surprise` peaks in either 906b or 906c correspond to `limb_damage_injected`,
`external_hazard_injected`, or `world_rule_shift_occurred`** — the largest surprise spikes are
predominantly reef-boundary crossings and genuine resource-consumption events. This independently
corroborates, from a different run and a different analysis, exactly why a correctly-built onset
detector over `residue_surprise` would under-fire on the specific injected-event types 910
targets: the channel is real and mechanistically sound, but **in this ecology its largest signal
is not concentrated on hazard-type events at all.** This sharpens MECH-489's own falsifying
disjunct from "channel choice was wrong" to the more precise "the chosen channel's own
composition in this substrate does not concentrate on the target event class."

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (trigger sub-component only) | falsifying signature #1 hit fairly; decision sub-component confounded, not informative |
| Biological reference | partial | Sokolov orienting-reflex anchor is sound; channel-type translation is reasonable; this substrate's surprise-channel composition doesn't concentrate on the target events |
| Prerequisites | present | all pooled-event-count preconditions cleared with margin |
| Implementation | partial | trigger correctly implements the recommended design; decision layer (Component 4/5) has a real scale-mismatch bug |
| Environment | adequate | not implicated |
| Measurement | misleading (partial) | residue_surprise's own peak composition (corroborated independently) means "surprise" as measured is not equivalent to "surprise about the experimenter's injected events" |
| Integration | partially coupled | trigger and override fire; the override's downstream decision arithmetic is broken |
| Scale | adequate | n=76/65/30 events, n=206 overrides -- sample size is not the limiting factor |

**Failure-location (GOV-FAILLOC-1):** MECHANISM (decision-layer scale-mismatch bug, established)
+ MEASURES (residue_surprise composition doesn't concentrate on target events, established,
corroborated independently) + partial biological-reference nuance (channel type right, this
ecology's channel composition wrong for the specific target). Net: **MIXED — trigger-alignment
sub-claim fairly falsified per the claim's own pre-registered signature, refined by the MEASURES
finding; valence-gating sub-claim confounded by a MECHANISM implementation bug and not fairly
tested. Not chargeable to REE alone, and specifically NOT the "calibration miss" the prior
review speculated.**

## Learning extracted

1. The derivative/onset-detector trigger design the prior review recommended was built exactly
   as specified — the near-zero alignment is not attributable to ignoring that recommendation.
2. A real, identifiable code bug (comparing a non-negative norm against a near-zero-unless-close
   attraction value) in the decision layer (`ree_core/agent.py:8008-8022`) structurally biases
   every override toward withdraw, independent of the triggering event's actual valence — this
   fully explains the 0/0/206 approach/resume/withdraw split without needing to invoke the
   trigger-alignment question at all.
3. MECH-489's own pre-registered falsifying signature #1 is hit by the trigger-alignment data,
   refined by an independent corroborating MEASURES finding (the reef review's surprise-peak
   browser): this substrate's `residue_surprise` channel does not concentrate on hazard-type
   events, so a correctly-designed onset detector built on it will still under-fire on them.
4. MECH-489 bundles two testable sub-mechanisms (trigger/identification, valence-gated decision)
   that this single run resolves in opposite directions — a candidate case for future
   granularity-debt tracking if a second autopsy on this claim recurs with a similarly split
   fate (not fired here: this is the first autopsy on MECH-489, 0 prior hits, granularity-debt
   cluster and re-derive brake both checked and confirmed not to fire).

## Repair pathway

- **Decision-layer scale mismatch** → `complicated (buildable)` → `/implement-substrate`. Fix:
  normalize/rescale the harm-norm and benefit-value onto commensurable units before comparing
  (e.g., z-score each against its own running distribution, or compare signed valence rather
  than a magnitude-vs-value comparison) — this is a well-posed, single-file fix with no open
  question about what "correct" looks like.
- **Trigger-alignment finding** → the falsifying signature already stands on MECH-489's own
  pre-registered terms; no further build is owed for this specific finding, but a future re-test
  of the valence-gating sub-component should happen only AFTER the decision-layer fix lands
  (re-testing the confounded sub-component on the same broken arithmetic would repeat the same
  uninformative result).

## `recommended_substrate_queue_entry`

**Action: create.** `sd_id_suggested: SD-ORIENTING-DECISION-SCALE`. `severity: corrupting` —
this bug corrupts every future defensive-orienting override decision, not only this run's (any
experiment relying on the mechanism's approach/withdraw/resume output while
`use_defensive_orienting=True` inherits the same structural withdraw-bias). `substrate_paths:
["ree_core/agent.py::select_action"]` (the Component 4/5 block at lines 8008-8022).

```json
"failure_record_entry": {
  "run_id": "v3_exq_910_mech489_defensive_orienting_validation_20260810T004433Z_v3",
  "experiment_type": "v3_exq_910_mech489_defensive_orienting_validation",
  "metric": "decision_alignment across 206 logged overrides: approach=0, withdraw=206, resume=0 -- a norm-vs-attraction-value scale mismatch structurally biases every comparison toward withdraw",
  "target": "a properly-scaled comparison should yield a non-degenerate mix of approach/withdraw/resume tracking actual event valence, not a 100%-one-sided split",
  "resolved": "open"
}
```

## Recommended `evidence_direction` and `evidence_quality_note`

**Recommend `mixed`** (revising the manifest's current `weakens`) — confirmed at the interactive
gate. Draft note for MECH-489:

> 2026-08-10 (failure_autopsy_V3-EXQ-910_2026-08-10, confirmed): V3-EXQ-910 evidence is MIXED,
> not a clean weakens. The trigger/identification sub-component (Components 1-3) fairly hits the
> claim's own pre-registered falsifying signature #1 (near-zero alignment on ground-truth
> injected events: 2.6%/1.5%/0.0%, despite the recommended derivative/onset-detector design being
> built correctly -- verified by reading ree_core/pag/defensive_orienting.py directly), refined
> by an independent MEASURES corroboration (this ecology's residue_surprise peaks are dominated
> by reef-boundary crossings and resource events, not hazard-type events). The valence-gated
> decision sub-component (Components 4-5) is NOT fairly tested: a real code bug in
> ree_core/agent.py (comparing a structurally non-negative harm norm against a near-zero-unless-
> close-to-resource benefit attraction value) structurally biases every override toward withdraw
> independent of actual event valence, fully explaining the observed 0/0/206 approach/resume/
> withdraw split on its own. pending_retest_after_substrate=true for the decision sub-component
> only, once SD-ORIENTING-DECISION-SCALE lands; the trigger-alignment falsification stands and
> does not need re-testing.

Set `pending_retest_after_substrate: true` on MECH-489.

## Growth-restriction / Step 9b

Not applicable — this is a validation test against a single pre-registered claim (confirming vs
falsifying signature), not a discrimination among multiple live rival hypotheses; no
`fanout_recommendation`. Checked: no existing `qid` in `hypothesis_space_registry.v1.json`
references MECH-489. Skip cleanly.

## Re-derive brake / granularity-debt check

Both checked directly against the confirmed-autopsy corpus: **0 prior hits** for MECH-489 (first
autopsy on this claim) — re-derive brake does not fire (threshold requires ≥2), granularity-debt
recurrence cluster does not fire (requires a second autopsy circling the same claim).

## Routing (confirmed at interactive gate)

**implement-substrate** — SD-ORIENTING-DECISION-SCALE (decision-layer scale-mismatch fix,
severity=corrupting). Recommend a **910a re-queue after the fix lands**, scoped to re-test
valence-gating only — the trigger-alignment falsifier already stands on its own pre-registered
terms and does not need re-testing. Not spawned from this artifact (per the skill's Step 8 rule);
governance records the recommendation and chips the build separately.
