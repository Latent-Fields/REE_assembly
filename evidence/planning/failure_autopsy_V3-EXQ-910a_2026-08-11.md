# Failure Autopsy: V3-EXQ-910a (MECH-489 defensive-orienting decision retest)

**Generated:** 2026-08-11T05:19:03Z
**Scope:** single
**Status:** confirmed
**Target:** V3-EXQ-910a (FAIL, `experiment_purpose: diagnostic`, `claim_ids: [MECH-489]`, supersedes V3-EXQ-910)
**Predecessor:** V3-EXQ-910 (`failure_autopsy_V3-EXQ-910_2026-08-10.md`)

Requested explicitly against the older orienting architecture already registered in
`claims.yaml` (MECH-395, MECH-482, MECH-483) — not begun from the assumption that these should
have been bundled into MECH-489. Applies GOV-FAILLOC-1.

**Dry-run gate:** clean (`check_dry_run_citations.py`, 0 hits on both 910 and 910a).
**Recording provenance:** both manifests carry `recording_schema: rec/v1`, `substrate_hash`,
`machine`/`machine_class`, `elapsed_seconds`, `seeds: [0,1]`.

## Facts (verified directly against the manifests, not copied from prior prose)

| | V3-EXQ-910 | V3-EXQ-910a |
|---|---|---|
| `n_overrides` (`decision_alignment.n_overrides`) | 42 | **21** |
| `decision_counts` | approach=0, withdraw=**206**, resume=0 | approach=0, withdraw=**206**, resume=0 |
| `event_trigger_alignment.limb_damage_injected` | n=76, aligned=2 (2.6%) | n=72, aligned=0 (**0.0%**) |
| `event_trigger_alignment.external_hazard_injected` | n=65, aligned=1 (1.5%) | n=58, aligned=0 (**0.0%**) |
| `event_trigger_alignment.world_rule_shift_occurred` | n=30, aligned=0 (0.0%) | n=29, aligned=0 (0.0%) |
| `on_arm_coupling.p_moved_given_spike` (baseline 0.443) | 0.28 | **0.090** |
| `on_arm_coupling.p_modechange_given_spike` (baseline 0.154) | 0.14 | **0.090** |
| `criteria_non_degenerate.C_decision_alignment_non_degenerate` | n/a (criterion (c) added in 910a) | `true` (⚠️ this flag only checks `n_overrides>0`, NOT actual category spread — see below) |
| substrate_hash | `d366c3b4...` | `d65dce58...` (post-fix commit `ad8bd4aa3c`) |

**The prior autopsy's own headline number is wrong, and it propagated.** `failure_autopsy_V3-EXQ-910_2026-08-10.md`, the SD-ORIENTING-DECISION-SCALE commit message, its architecture doc, and `substrate_queue.json`'s `failure_record` all say "206/206 logged overrides" / "206 logged overrides." **The manifest's own `n_overrides` field says 42, not 206.** `decision_counts` (sum=206) and `n_overrides` (=42) are two different measurements computed in the same loop over the same step list (`_decision_alignment()` in both driver scripts) — see "Decisive new finding" below for why they diverge and why the divergence itself is a problem. This correction is recorded here; the existing artifacts are not silently rewritten (see Governance hygiene).

## Critical conceptual audit: `identification_confidence`

Read directly from `ree_core/pag/defensive_orienting.py:299-309` (the ONLY place this variable is computed):

```python
current_excess = max(surprise_delta, harm_s_delta, 0.0)
residual = min(1.0, current_excess / self._peak_excess)
gain = confidence_rise_rate * (1.0 - residual)      # rises as the SAME triggering signal decays
gain += confidence_floor_rise                        # 0.0 by default
self._identification_confidence += gain              # clamped [0,1]
```

`surprise_delta`/`harm_s_delta` are the same two scalars (`residue_surprise`, `z_harm_s` norm) that
drove the trigger, measured against their own EMA baseline, **frozen at its pre-trigger value for
the whole episode** (so this genuinely tracks decay of the raw signal, not baseline creep — the
module's own docstring is accurate about this part). `_peak_excess` is the excess recorded AT THE
MOMENT of triggering.

Determined by inspecting the actual equations and state transitions, this variable has **zero**
causal dependence on: additional sensory sampling, active observation, uncertainty reduction,
target localisation, model improvement, cue identification, hippocampal information acquisition,
MECH-482 epistemic deficit, MECH-483 orient/survey behaviour, MECH-395 cue-specific orienting, or
any quantity constituting actual epistemic resolution. The formula reads exactly two scalars, both
already used to fire the trigger.

**Counterfactual test (as requested):**
- *Hold epistemic content constant, let the phasic channel decay* → `identification_confidence`
  **will** rise and **will** release the gate — nothing else feeds `gain`. Confirmed structurally:
  the formula has no term for anything except `current_excess`/`peak_excess`.
- *Provide strong resolving information while keeping the trigger channel elevated* → confidence
  **cannot** rise (`residual` stays near 1.0, `gain` stays near 0). There is no input channel for
  "resolving information" to enter through at all — the module reads only two scalars.

**Verdict: `identification_confidence` is scientifically a habituation/decay-tracker — "has the
perturbation subsided" confidence — not an identification, recognition, or epistemic-sufficiency
variable in any information-theoretic or cognitive sense.** It is genuinely NOT a fixed-timer
either (MECH-489's own falsifying signature #3, "identification-confidence resolves on a fixed
schedule regardless of whether the triggering signal has genuinely decayed," is literally
FALSE — the dynamics are decay-coupled, not clock-driven). The claim's own pre-registration posed
a binary (fixed-timer vs epistemically-driven) that misses the actual truth: **decay-coupled but
non-epistemic**, a third category. This is not a naming quibble — "the freeze is a disguised
timer" and "the freeze is a disguised timer, not a fixed one" are different findings, and only the
second is what the code actually shows.

**Does trigger → arrest → confidence → override contain a genuine orient/investigate/resolve
operation between arrest and release? No — stated plainly, verified two ways:**

1. **Motor**: `ree_core/agent.py:9049-9063` forces the emitted action to a no-op one-hot vector
   whenever `orienting_active` is True (composed via OR with `PAGFreezeGate`'s own freeze). The
   agent physically cannot move toward, scan, or reorient toward the trigger location while
   arrested — freeze *prevents* the very investigation the design brief's language implies.
2. **Informational**: the only new state written during arrest is the decay-timer above (no
   sensory-sampling change, no hippocampal read, no belief update). Component 3's location capture
   (`_orienting_trigger_z_world`, `agent.py:8105-8108`) is a **passive one-shot snapshot at the
   trigger tick**, never refined or updated during the arrest — not active localisation.

The one thing that IS real during arrest: sensory encoding is not halted (the normal
per-tick `_current_latent` computation continues regardless of orienting state) — but that is the
baseline pipeline running as it always does, not a new or enhanced information-gathering operation
triggered BY orienting.

## Distinguishing the four orienting concepts

| | MECH-489 (phasic arrest) | MECH-482 (epistemic deficit) | MECH-483 (orient/survey) | MECH-395 (cue-specific orient) |
|---|---|---|---|---|
| Timescale | phasic, single-episode, resets on release | persistent, target-bound accumulator | diffuse regime, driven by MECH-482 | per-cue episode |
| Trigger | sudden onset (positive-derivative surprise/harm) | unresolved importance × uncertainty × resolvability × persistence | accumulated epistemic_deficit | a present, already-identified cue with low directional confidence |
| What it does | freeze, then release on signal decay | accumulates/decays with resolution | widens behavioural sampling, gathers info | samples gradients to resolve ONE vector |
| Built in V3? | Yes (2026-08-09) | No — DO NOT build (gated on GAP-A) | No — DO NOT build (gated on GAP-A) | No — DO NOT build (v3_pending) |

`claims.yaml`'s own `depends_on` comments on MECH-489, and SD-099's "Related Claims" section,
already draw this distinction explicitly and correctly — MECH-489's trigger signal
(`residue_surprise`, computed every step) does not depend on MECH-482's unbuilt GAP-A substrate,
so "DO NOT build in V3" does not extend to it. **This boundary is scientifically sound and I am
not recommending it be redrawn.**

**What IS true, one level up from the formal claim boundary:** the *originating design brief*
(`observational_review_V3-EXQ-906b_2026-08-09.md` §11b step 3) that motivated MECH-489/SD-099
explicitly calls for the orienting component to "**turn toward and attend to** the unexpected
stimulus so the surprise **resolves into an identification**" — active, investigative language,
and states plainly "**without orienting, freeze has no epistemic exit**... orienting is not an
optional attentional flourish on top of freeze; it is the mechanism that closes the surprise
loop." SD-099's own architecture doc repeats this framing ("orienting reflex... the 'attend to
the stimulus until it resolves' dynamic"). What got built, per the code trace above, is a passive
decay-timer wearing that name. **This is not a code-level dependency on MECH-395/482/483 — it is
a naming/narrative gap between MECH-489's own design brief and its own implementation**, filled
by borrowing vocabulary ("identification," "attend," "orient") that MECH-395/482/483 are the
claims meant to eventually formalize, without implementing the operations those words denote.

**Candidate architecture, tested against the registered claims and existing wiring:**

```
unexpected event
 -> MECH-489 phasic defensive arrest                      [BUILT, real]
 -> unresolved uncertainty sustains MECH-482 epistemic deficit   [NOT built — MECH-489 does not feed this]
 -> MECH-483 orient/survey gathers information             [NOT built — MECH-489 performs no such gathering]
 -> if a cue is identified, MECH-395 cue-specific orientation    [NOT built — no handoff exists]
 -> epistemic deficit decreases / identification grounded  [NOT built]
 -> approach / withdraw / resume                            [BUILT, but see Leg 5 below]
```

This candidate sequence is **consistent with how the claims are registered** (SD-099's doc calls
MECH-489 "upstream of" MECH-395: "its own resolution is what would hand off to something
MECH-395-shaped, not the same mechanism") but **the handoff itself does not exist in code.**
MECH-489 currently short-circuits straight from arrest to a decay-timer to action-decision,
without ever routing through anything MECH-482/483/395-shaped. That is architecturally
legitimate (MECH-489 was never claimed to build that handoff — see boundary discussion above) but
it means the "full chain" narrative in §11b/SD-099 currently describes a THREE-mechanism
composition (MECH-489 → MECH-483/482 → MECH-395) of which only the first link is built, and the
first link's own internal "orient/identify" sub-step does not do what its name says.

## Leg-by-leg re-evaluation

**Leg 1 — event detection.** FAILS, 0/0/0% alignment on all three ground-truth event types in
910a (worse than 910's already-poor 2.6/1.5/0%). This **reconfirms** the already-established
finding from `failure_autopsy_V3-EXQ-910_2026-08-10.md` — not new information. That autopsy
correctly traced this to channel *composition*, independently corroborated by
`reef_ecology_strategy_affective_occupancy_review_2026-08-10.md`'s surprise-peak browser (this
substrate's `residue_surprise` peaks concentrate on reef-boundary crossings and resource events,
not hazard events). Investigated per the brief's checklist: the trigger design IS the recommended
onset-detector (verified directly against `defensive_orienting.py`'s code, not assumed); the
action-decision problem does not explain this — Leg 1 is upstream of and independent of the
decision layer entirely.

**Leg 2 — phasic arrest.** Works as specified. Action is genuinely forced to no-op
(`agent.py:9049-9063`) while `orienting_active`.

**Leg 3 — information acquisition.** Does not exist. No sensory-sampling change, no active
localisation, no belief update occurs during arrest (code-verified above). Freeze itself prevents
locomotion toward the trigger, so even incidental "moving closer for a better look" is impossible.

**Leg 4 — epistemic satiation vs. signal decay.** Release is driven by decay of the SAME
triggering channel (code-verified above, counterfactuals confirm no epistemic content can
influence it). This is a genuine, decisive finding: whatever "identification_confidence" is, it
is not identification.

**Leg 5 — stimulus-grounded action.** The decision has real inputs: a captured location
(`_orienting_trigger_z_world`), and (post-fix) z-scored harm-vs-benefit channels read at the
CURRENT z_world. So it is not ungrounded in the sense of "has no idea what triggered it." What
IS broken is the **measurement** of its output — see next section — so no conclusion about
whether the decision is *correctly* valence-gated can currently be drawn either way.

## Decisive new finding: `decision_counts` cannot support criterion (c) in either direction

Traced in `ree_core/agent.py:8117-8189` (unchanged by SD-ORIENTING-DECISION-SCALE except the
comparison arithmetic itself): on an override tick, `_orienting_decision` is set once and
`_orienting_decision_ticks_remaining` is set to `orienting_post_override_bias_ticks` (**5**,
config default, confirmed unchanged by the fix via `git show 357c14f`). The persistence window
is *supposed* to decrement each subsequent tick and reset the decision to `None` after 5 ticks —
but this decrement/reset **only executes when `all(c.world_states for c in candidates)` holds**
(`agent.py:8165`; the code's own comment: "degrades gracefully... when world_states are not
tracked"). Confirmed `world_states` IS populated in the normal path
(`hippocampal.propose_trajectories` → `E2FastPredictor.rollout_with_world`), so the gate is not
trivially always-open — but its reliability across every subsequent tick (including ticks where
MECH-090 trajectory-stepping may return a held/committed action without regenerating candidates)
was not directly verifiable from the aggregated manifest alone.

The per-step log (`v3_exq_906b_full_stack_observational_fishtank.py:708`,
`"orienting_decision": getattr(agent, "_orienting_decision", None)`) reads whatever
`_orienting_decision` currently is, EVERY tick, regardless of whether the decrement executed.
Consequence: **`decision_counts` is not "how N override events resolved" — it is "how many
step-ticks the decision variable happened to sit at a given value,"** bounded above, under the
documented 5-tick window, by `n_overrides × 5`.

For 910a: `21 × 5 = 105` theoretical maximum. **Observed `decision_counts` sum is 206 — roughly
double the theoretical maximum**, and byte-identical to 910's total (42 overrides, same 206)
despite half the override count and a different substrate hash (`d65dce58...` vs `d366c3b4...`,
reflecting the fix's own code change). This is not consistent with the persistence window working
as designed. **I could not fully pin the exact failure mode** — no per-step episode logs were
saved for either run (only the aggregated manifest/metrics/summary triad exists under
`evidence/experiments/v3_exq_910{,a}_.../runs/`), so the reset-condition's actual tick-by-tick
behaviour cannot be directly inspected post-hoc. What IS established: the two counters are
structurally decoupled from each other in a way inconsistent with the documented 5-tick model,
which means **`decision_counts`, as currently logged, cannot be trusted as a faithful readout of
the decision layer's behaviour** — independent of whether the SD-ORIENTING-DECISION-SCALE fix
itself works correctly.

**What DOES survive this measurement defect, because it doesn't depend on window duration:** the
discrete classification made AT the override tick itself is real (it's set once, synchronously,
in the same `if _do_out.override_fired:` block that increments `n_overrides`). Across 63 pooled
override events in 910+910a combined, **not one** resolves to "approach" or "resume" — a
persistence-window-independent finding. Whether this reflects (a) a residual scale issue in the
fix, (b) the environment's override-triggering events genuinely being threat-dominated even when
they aren't among the three injected fields, or (c) something else, **cannot currently be
determined** — criterion (c) as implemented cannot discriminate these, because its own
denominator (206) is not "how many overrides" at all.

## Hypothesis elimination (H1–H7)

- **H1 (trigger calibration/timing failure):** Partially true but not new — already explained by
  the prior autopsy's independent MEASURES corroboration (channel *composition*, not calibration
  or timing per se). Investigated per the brief: previous-tick surprise caching, onset-delta
  calibration, and OR-combination behaviour are all as designed; the under-fire is explained by
  what this substrate's surprise channel actually responds to, not a wiring defect.
- **H2 (implementation-semantic failure — `identification_confidence` doesn't measure epistemic
  identification):** **CONFIRMED**, code-verified above (Critical conceptual audit).
- **H3 (missing compositional substrate — needs MECH-482/483/395 machinery):** **NOT established
  as a code-level requirement** — the claim boundary correctly does not depend on that unbuilt
  substrate. Survives only in the narrower "naming/narrative debt" form described above.
- **H4 (action-grounding failure — no stimulus-specific representation for
  approach/withdraw/resume):** **NOT supported.** The decision has a captured location and reads
  real per-tick channels (harm norm, benefit value, both now z-scored against running baselines).
  What fails is not grounding but measurement (H5).
- **H5 (measurement-granularity/test-design failure):** **CONFIRMED and central** — `decision_counts`
  is structurally decoupled from `n_overrides` in a way inconsistent with the documented
  persistence-window model; criterion (c) as currently computed cannot support a conclusion in
  either direction.
- **H6 (environment/event invalidity):** **NOT supported.** Events are real, well-powered (72/58/29
  pooled, all clear the n≥3 readiness floor by a wide margin).
- **H7 (MECH-489 itself is simply wrong, even after removing adjacent-system requirements):**
  **CANNOT BE REACHED.** Per GOV-FAILLOC-1, REE-FAILED requires Implementation, Measurement, AND
  Environment to each independently read adequate/complete. Measurement fails outright (H5,
  confirmed); Implementation is partial (Leg 1 channel-composition gap, confirmed). H7 is not
  eliminated but is not established either — it remains open pending a working measurement.

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | weakened (partial, re-confirming + newly explicit) | Leg 1 re-confirms 910's falsification (not new); Leg 3/4's "no resolution operation exists" is a newly explicit finding against the architecture doc's own framing, not against the formal claim boundary |
| Biological reference | partial | Sokolov orienting-reflex anchor remains sound for arrest/release-on-decay; the *narrative* framing of Component 3 ("orient/identify," "attend to") overclaims relative to a pure habituation timer — a real but narrower biological analog (startle habituation, not active orienting/investigation) |
| Prerequisites | present | all pooled-event-count and override-count readiness preconditions cleared with margin (72/58/29 events, 21 overrides ≥5 floor) |
| Implementation | partial | trigger correctly implements the recommended two-channel onset design (re-confirmed); the "orienting reflex" component implements less than its own design brief (§11b step 3) specifies; decision-layer arithmetic fix landed correctly per `git show 357c14f`, but its measurement (below) is broken |
| Environment | adequate | not implicated; events are real and well-powered |
| Measurement | **broken** | `decision_counts` is structurally decoupled from `n_overrides` (206 observed vs. 105 theoretical max for 910a's 21 overrides); criterion (c) cannot support a conclusion either way; this is newly identified in THIS autopsy, not present in the prior one |
| Integration | partially coupled | trigger, arrest, and decision-arithmetic all fire and read real channels; the intended orient/resolve step between arrest and release does not exist as a distinct operation |
| Scale | adequate | n=72/58/29 events, n=21 overrides — sample size is not the limiting factor |

**Failure-location (GOV-FAILLOC-1):** MECHANISM (Leg 1 channel composition, re-confirmed
established; Leg 3/4 "no resolution operation" newly established from direct code read) +
MEASURES (decision_counts structural defect, newly established) + ENVIRONMENT not implicated.
**Net: MIXED.** REE-FAILED is not reached (Measurement fails outright, so the three-way adequacy
precondition is not met). Not chargeable to REE alone, and specifically not chargeable to
MECH-489's *claim boundary* (which is sound) — chargeable to (a) a real gap between MECH-489's
own design brief and its own implementation, and (b) a genuine, previously-unidentified
measurement defect in the decision-layer telemetry.

## Scientific disposition

**What does V3-EXQ-910a genuinely tell us about MECH-489?** MIXED — confirmed with the user at
the interactive gate. Leg 1's falsification re-confirms (not extends) the standing finding from
V3-EXQ-910. The newly explicit finding here is that MECH-489's "orienting reflex" component,
which the SD-099 architecture doc frames as active attending/identification, is code-verified to
implement pure signal-decay with no epistemic content — a genuine finding against the *doc's own
narrative*, though not against the formal claim boundary (which never actually pre-registered
"identification" as a falsifiable property distinct from decay). Criterion (c)'s FAIL is **not
usable as evidence in either direction** — the measurement it depends on (`decision_counts`) is
broken independent of whether the SD-ORIENTING-DECISION-SCALE fix achieved its goal.

**What does it tell us about MECH-482/483/395?** Nothing directly — none were active or tested.
This boundary is stated explicitly: absence of MECH-482/483/395 machinery is not evidence against
those claims, and MECH-489's own claim registration correctly does not depend on their
not-yet-built substrate (GAP-A). The finding here concerns MECH-489's *narrative framing*
borrowing vocabulary from that adjacent territory, not any test of the adjacent claims themselves.

**Is MECH-489's claim boundary still scientifically coherent?** **Yes — retain it as a phasic
defensive-arrest primitive, with its "identification"/"orient" interpretation for Component 3
corrected to "signal-decay release."** Confirmed with the user: no claim rewrite recommended.
Recommend instead a governance note on SD-099's architecture doc (not an immediate edit — user
confirmed governance-note-only) flagging that "attend to the stimulus," "orient/identify," and
"the stimulus becomes recognised" overclaim relative to what Component 3 actually computes, so a
future reader (or a future claim built on top of this one) does not inherit the same over-read.

## Governance and evidence hygiene

- Engineering completion (the z-scoring fix landed and is smoke-tested per `git show 357c14f`) ≠
  mechanism validation (criterion (c) cannot currently validate or falsify it — the measurement is
  broken).
- MECH-489's failure on Leg 1/criterion (c) ≠ failure of MECH-482/483/395 — none were tested, and
  their absence does not exonerate or implicate them.
- `identification_confidence`'s name is not evidence of an implemented cognitive function — code-
  verified to be a decay-timer.
- **Correcting existing artifacts:** the prior autopsy's "206/206 logged overrides" phrasing (and
  its propagation into the SD-ORIENTING-DECISION-SCALE commit message, architecture doc, and
  `substrate_queue.json`'s `failure_record`) is factually imprecise (`n_overrides=42`, not 206) —
  recorded here per the normal correction procedure, NOT silently rewritten in place. The
  `substrate_queue.json` entry's `failure_record` gets a NEW item (this autopsy's finding),
  leaving the existing item's text untouched per the standing convention (see
  `recommended_substrate_queue_entry` below).

## Failure-location summary (GOV-FAILLOC-1) — repeated for the JSON schema

`failure_location: {mechanism: established, measures: established, environment: not_established,
ree: false, net_classification: "MIXED"}`.

## `recommended_substrate_queue_entry`

**Action: amend.** `target_sd_id: SD-ORIENTING-DECISION-SCALE`.

The existing entry's `status` ("implemented_pending_validation") and `validation_experiment`
("PENDING -- 910a re-queue... not yet queued") are now STALE — 910a has run and FAILED. Update:

```json
"status": "implemented_pending_validation",
"validation_experiment": "V3-EXQ-910a ran and FAILED, but criterion (c) — the fix's own acceptance
  test — cannot be trusted: decision_counts (206) is ~2x the theoretical max under n_overrides=21
  and orienting_post_override_bias_ticks=5, decoupled from n_overrides in a way inconsistent with
  the documented persistence-window model. A NEW, SEPARATE decision-logging defect (not the
  scale-mismatch this SD fixed) must be resolved before this SD's own validation can be trusted
  in either direction. See failure_autopsy_V3-EXQ-910a_2026-08-11.md."
```

**Severity: `degrading`, not `corrupting`** — this defect does not invalidate Leg 1's independent
trigger-alignment finding (unaffected by decision_counts) or the arithmetic fix's own smoke-tested
correctness; it invalidates only the decision-layer *behavioural telemetry* (criterion (c) and any
future decision_alignment readout).

**`substrate_paths`:** `["ree_core/agent.py::select_action"]` (the persistence-decrement/reset
block, `agent.py:8160-8189`) — same function as the original fix, different sub-block.

```json
"failure_record_entry": {
  "run_id": "v3_exq_910a_mech489_defensive_orienting_decision_retest_20260810T213616Z_v3",
  "experiment_type": "v3_exq_910a_mech489_defensive_orienting_decision_retest",
  "metric": "decision_counts sum (206) exceeds the theoretical max (n_overrides=21 x orienting_post_override_bias_ticks=5 = 105) by ~2x, and is byte-identical to V3-EXQ-910's total (42 overrides, also 206) -- the per-step orienting_decision log field is decoupled from the intended N-tick persistence window in a way not fully diagnosable from the aggregated manifest alone (no per-step episode log was retained for either run)",
  "target": "decision_counts sum should be bounded by n_overrides x orienting_post_override_bias_ticks under normal (world_states-tracked) operation, and should NOT reproduce a prior run's total exactly when n_overrides differs substantially",
  "resolved": "open"
}
```

**No `resolves_prior_failure_record`** — the existing item ("decision_alignment across 206 logged
overrides...") describes the ORIGINAL scale-mismatch bug (resolved by the landed fix) but itself
carries the same "206 logged overrides" imprecision this autopsy corrects; it is left as-is
(historical record of what motivated the fix) rather than edited, per the standing convention of
not silently rewriting prior artifacts. This autopsy's NEW item is the currently-open one.

## Successor design (confirmed with user)

**NOT another omnibus re-run.** The smallest discriminating next step, confirmed with the user:

1. **Fix the decision-logging defect first** (`complicated (buildable)` — the bug and the fix
   shape are both narrow and specified by this autopsy: either make the persistence-decrement
   unconditional on `world_states` for LOGGING purposes specifically (leave the score-bias
   application itself gated as before), or — simpler — log the decision classification only at
   the override tick itself (`orienting_override_fired==True`), which is unambiguous and does not
   depend on the ticks_remaining machinery at all for measurement purposes. Route via
   `/implement-substrate`, `substrate_queue.json` amend above.
2. **Re-measure** decision_alignment. Because the fix is a pure logging/counting change, not a
   behavioural change, this does NOT require a fresh experiment run — the existing 910a episode
   trace (if still reconstructible from raw logs) or a cheap re-run under the corrected logging
   would suffice. **Do not queue a fresh discriminating experiment now** — confirmed with the
   user: wait to see whether the corrected measurement resolves the ambiguity before committing
   to a new EXQ.
3. **Only if the corrected measurement STILL shows 100% withdraw** with well-powered override
   counts, investigate a residual scale-mismatch in the z-scoring fix itself (e.g., the benefit
   channel's MAD staying pinned near the `scale_floor` most of the time, given the benefit field
   is near-zero except close to accumulated centers, could still asymmetrically inflate or deflate
   one channel's z-score relative to the other — this was NOT verified either way in this autopsy
   and is a candidate, not a finding).

Governance note (not an immediate edit, confirmed with user): `docs/architecture/sd_099_defensive_orienting_response.md`
Component 3's language ("orienting reflex... the 'attend to the stimulus until it resolves'
dynamic") should eventually be revised to describe what is actually computed (decay of the
triggering channel's own excess-over-baseline) rather than active attending/identification, so a
future reader does not inherit the over-read this autopsy found. Left to `/governance` to action
in its own cycle, not self-applied here.

## Growth-restriction / Step 9b

Checked: no existing `qid` in `hypothesis_space_registry.v1.json` references MECH-489, MECH-395,
MECH-482, MECH-483, or SD-099 (grep confirmed 2026-08-11). This is a single-target adjudication
against MECH-489's own pre-registered falsifying signature, not a discrimination among multiple
live rival hypotheses — no `fanout_recommendation`. Per Step 9b's applicability rule ("adjudicates
a leg" with a `recommended_evidence_direction`), this target does carry one (`mixed`), but absent
any existing hypothesis-space question for this claim family and absent a fan-out, there is
nothing to pre-register or resolve against. Skip cleanly, consistent with the prior autopsy's own
check.

## Re-derive brake / granularity-debt check

**Re-derive brake:** does not fire. Under the R1–R3 counting convention (RUN-level, latest
adjudication wins, `substrate_ceiling`-only), V3-EXQ-910's `recommended_epistemic_category` is
`standard`, not `substrate_ceiling` — 0 ceiling hits for MECH-489, threshold (2) not reached
regardless of this autopsy's own category (also `standard` — see below).

**Granularity-debt recurrence:** checked via `scripts/granularity_debt_cluster.py MECH-489` —
1 prior target (V3-EXQ-910, `weakened`) before this one. This autopsy adds a SECOND `weakened`(-ish,
`mixed`) target, but the underlying failure SIGNATURES are: (a) Leg 1 — a **re-confirmation** of
910's own finding, not a structurally new signature; (b) the measurement-defect finding — a
NEW signature, but one that argues for **fixing an instrument**, not for **splitting the claim**.
Per the standing rule ("a cluster in which NO target reads `weakened` [for a structurally
different reason] is measurement or implementation debt, not granularity debt"), this does NOT
fire the `/claim-synthesis` trigger — the claim boundary itself is not the problem; a decision-
layer logging bug is. Recorded here so the next autopsy circling MECH-489 (if any) can see this
was checked and correctly did not fire.

## Routing (confirmed at interactive gate, 2026-08-11)

**`/implement-substrate`** (SD-ORIENTING-DECISION-SCALE amend, decision-logging defect,
severity=degrading) — fix the decision_counts logging defect. **Do NOT queue a fresh
discriminating experiment now** — re-measure against the corrected logging first; only escalate
to a new EXQ if the corrected measurement still shows the degenerate split. **Governance note**
(not an immediate doc edit) recommended for SD-099's Component-3 language. Not spawned as a chip
from this artifact (per the skill's Step 8 rule) — `/governance` records and chips the build
separately, after its own Step 2b/4/6a ratification.
