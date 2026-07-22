# Q-081 — Structure-Destroying (Landmark-Removal) Arm: Design Record

**Status:** BUILT (2026-07-22). NOT YET RUNNABLE — see §7.
**Gates:** `Q-081` (non-degeneracy guard, STRUCTURE-DESTROYING ARM paragraph), `MECH-466`
**Code:** `ree-v3/experiments/_lib/q081_landmark_removal.py`
**Validation:** `ree-v3/tests/contracts/test_q081_landmark_removal.py` (35 tests, all passing)
**Companion:** `q081_surrogate_null_design.md` — the *analysis*-side control. Neither substitutes
for the other.

---

## 1. What this arm is, in one paragraph

Q-081's guard requires two controls, and says explicitly that they are not substitutes. The
surrogate destroys cross-stream alignment **in the analysis**; this arm destroys the event /
commitment landmark structure **in the system**, while leaving intact (a) the streams, (b) the
configured update rates (SD-006: E1/E2/E3 at 1/3/10), and (c) the environmental input
statistics. A cross-stream statistic that survives this arm was measuring the clock. That is the
sharpest available discriminator between Outcome A (shared organisation) and Outcome B (wired
gates / configured rates only). The worked analogue is the scrambled-story control in Chang,
Nastase & Hasson 2022 (PNAS), which preserved low-level input statistics, destroyed nested event
structure, and made the cross-area lag gradient vanish — thereby excluding the intrinsic-rate
explanation.

## 2. Where it intervenes — and why no `ree_core` change was needed

This was the first finding, and it substantially reduced the blast radius of the work.

`REEAgent.sense()` calls `hippocampal.event_segmenter.step(...)` once per waking tick and binds
the result to a **single local `events` list**, which is then the sole input to all three live
consumer paths (`ree-v3/ree_core/agent.py` ~4249–4367):

```
events = self.hippocampal.event_segmenter.step(...)
  -> self.hippocampal._boundary_event_queue.extend(events)              # MECH-288
  -> self.hippocampal.invalidation_trigger.step(boundary_events=events) # MECH-287
     -> broadcasts -> apply_invalidation_broadcasts_to_regions()
        (drops per-region V_s entries, marks anchors inactive)
  -> self.hippocampal.tick_anchor_set(events=anchor_events)             # MECH-269
     -> anchor_set.consume_boundary_events()
        -> write_anchor(scale, segment_id_new, stream_mixture, z_world)
```

Because that local list is a single choke point, **wrapping `event_segmenter.step` is sufficient
and complete**. The arm therefore lives at the experiment layer, following the established
precedent (`consolidation_lesion_harness.py`, the V3-EXQ-702 injected-content pattern): no
`ree_core` change, no new `REEConfig` knob (and so none of the three-site plumbing hazard), no
backward-compatibility surface, and the lever is removed entirely by `detach()`.

The third consumer is what gives the arm **behavioural reach**: `write_anchor` binds
`segment_id_new` to the `z_world` present **at emission time**. Re-emitting a landmark at a
decorrelated tick binds the anchor to a different world state — the alignment is destroyed in the
system, not merely relabelled. Anchors feed V_s, V_s feeds `vs_rollout_gate`, and the gate feeds
E3 selection.

## 3. Behavioural reach is flag-conditional — asserted, not assumed

If `use_invalidation_trigger`, `use_anchor_sets`, `use_per_region_vs` and
`use_staleness_accumulator` are all False, boundary events are queued and drained with **no
consumer**. The arm is then behaviourally inert: it trivially "preserves input statistics"
because there is no path by which it could change them, and it tests only statistics computed on
the boundary stream itself — which is not what Q-081 asks.

That is the same defect class as an inert arm knob (`inert_arm_knob.py`): a conjunctive claim
silently loses a conjunct and the run still passes. `assert_behavioural_reach()` makes it a
**precondition** that raises, in the spirit of MECH-466's boundary-rate non-degeneracy guard. An
arm that cannot act is not a control.

## 4. The hard constraint: preserving environmental input statistics

This is the part the task brief correctly identifies as hard, and it is why the module *reports*
rather than merely intervenes.

**Chang had it easy in one respect: the stimulus was exogenous**, so scrambling could not change
what the subject received. REE is a **closed loop**. Any intervention with behavioural reach —
and per §3 an intervention *without* behavioural reach is vacuous — propagates to action, and
therefore to what the agent encounters. **Input statistics cannot be preserved by fiat in a
closed loop, and claiming otherwise would be exactly the confound the arm exists to exclude.**

So preservation is established at two levels, and the second is a measurement, not a guarantee.

### Level 1 — by construction, at the intervention site

The emitted boundary train is a **permutation of a donor train**, so these are preserved
**exactly**, not in distribution:

| Quantity | Why it matters |
|---|---|
| boundary **count** | a changed count changes the invalidation drive, not the alignment |
| inter-event-interval **multiset** | burstiness is real structure; losing it would be the fresh-only-shuffle error the surrogate module already supersedes |
| **posterior** multiset | `broadcast_strength = posterior * gain` — this multiset *is* the drive |
| **scale mix** (fast/slow counts) | a slow fire resets `inner` and suppresses a same-tick fast fire; the mix is structural |

`preservation_report()` audits each per episode and sets `preserved_by_construction=False` if any
fails. Nothing downstream can distinguish the arm from the intact arm by the marginal statistics
of the landmark signal itself — only by its timing relative to system state.

### Level 2 — by measurement, downstream

`input_statistics_divergence()` compares scrambled against intact on the quantities that define
*what the agent encountered*: per-channel observation marginals (standardised on the intact arm's
SD), state-visitation distribution (Jensen–Shannon), action distribution (JS), harm and reward
event rates, and mean episode length.

Thresholds are **pre-registered in the module** (`DEFAULT_INPUT_STAT_THRESHOLDS`) so the verdict
cannot be tuned after seeing the result. They are deliberately loose — the check is for a *gross*
shift ("the agent went somewhere else entirely"), not bit-equality, which a closed loop cannot
deliver and which would make every honest run look confounded.

On breach, `input_statistics_preserved=False` and the arm is **CONFOUNDED**: "the statistic
vanished" and "the agent was somewhere else" are not separable. Such a run must not be reported
as a null result; it self-routes, exactly as a boundary-rate floor/ceiling pin self-routes
`substrate_not_ready` under MECH-466. **A Level-2 failure can be legitimate** — it is a finding
about coupling strength, not a harness bug, and must be reported rather than tuned away.

Two vacuity guards on the verdict itself, both pinned by contract: an **unmeasured** metric is
listed in `not_measured` and never counted as cleared; and a comparison with **no** metrics at
all returns `input_statistics_preserved=False` with "cannot be asserted", not a pass.

## 5. The lever: yoked permutation of the donor train

Three candidate levers were evaluated. The brief asked for a choice with justification, not an
assumption.

**REJECTED as primary — suppress boundary emission.** Removes the landmark structure but also
removes the drive: broadcast count goes to zero, confounding "landmarks misaligned" with "less
invalidation drive". It is a *lesion*, and Chang's control was explicitly not a lesion. Retained
as an out-of-family reference arm, flagged `is_lesion=True`, and contract-pinned as never the
primary.

**REJECTED as primary — online rate-matched resampling.** Emitting with probability *p* = running
boundary rate preserves the mean rate but imposes geometric inter-event intervals. Hierarchical
segmentation is bursty by construction (a slow fire suppresses a same-tick fast fire), so the IEI
distribution would not be preserved — and a statistic could then die from the loss of burstiness
rather than the loss of alignment. Same error class as the fresh-only shuffle.

**ADOPTED — yoked permutation (`mode="iei_permute"`, the pre-registered `PRIMARY_MODE`).** The
intact arm runs first and banks its boundary train per `(seed, episode_index)`. The scrambled arm
replays a permutation of *that exact train*, with `(interval, payload)` pairs permuted **jointly
as units** — precisely the paragraph-scramble of the analogue: same segments, same durations,
same content, scrambled order and therefore scrambled alignment.

A useful property falls out and is contract-pinned: because the permuted intervals are a
rearrangement of the same multiset, their cumulative sum **ends exactly at the donor's last
boundary tick**, so no event can fall off the end of the episode and the count is preserved
*exactly* rather than approximately. (This is why `intervals()` measures the first interval from
`t=0` — it makes the interval list a complete reparameterisation of the time list, so
`cumsum(intervals) == times`.)

Matching is seed-for-seed and episode-for-episode, which makes the guarantee **auditable rather
than distributional**. This is a yoked-control design in the behavioural-neuroscience sense and
inherits that design's known caveat: after the first behavioural divergence, the donor train is
no longer "what this agent would have produced". That is accepted deliberately — an
exactly-matched landmark signal is worth more here than a counterfactually-faithful one, because
the question is precisely whether alignment mattered.

**ADOPTED as the conservative secondary — `mode="circular_shift"`.** A rigid circular shift
destroys landmark-to-stream alignment while preserving the landmark train's *own* internal
structure (autocorrelation, burstiness, interval sequence) up to a single wrap interval. Running
it alongside the primary **dissociates two things the primary destroys together**: alignment with
the rest of the system, versus the internal organisation of the landmark train. A statistic that
dies under `iei_permute` but survives `circular_shift` was reading landmark-train structure, not
cross-stream alignment. Worth the extra arm.

**ADOPTED as the donor-free fallback — `mode="jitter"`.** Causal, needs no donor, preserves the
count exactly (pending events flush on the final tick), but smears the IEI multiset — and the
preservation report says so rather than hiding it.

## 6. Interpretation rules (carried from the claim, restated because they are easy to lose)

- Do **not** report a surrogate-cleared statistic as evidence for Outcome A on its own. Clearing
  the null is necessary and nowhere near sufficient; wired coordination clears it correctly.
- A statistic that **survives** this arm is evidence about the **clock** — Outcome B — not
  evidence for the claim.
- Cross-stream **lag** remains a control quantity that must be present and must not explain the
  result. It is not promoted by this arm.
- This arm plus the surrogate is still not the **ablation series**, which remains the only full
  A-vs-B discriminator.

## 7. What this does NOT deliver, and what remains

The arm is **built and contract-validated but not yet runnable**, for one reason: the per-step
multi-stream trace recorder (`experiments/_lib/stream_recorder.py`, `trace_store.py`,
`q081_profile.py`, session `suspicious-williamson-73da0d`) **has not landed on `ree-v3` `origin/main`**
as of 2026-07-22T18:07Z. Without it there is nothing recording the cross-stream traces the arm
is a control for, so no experiment script or queue entry was written — writing one against an
unlanded recorder would pin an API that may still change.

| Piece | State | Owner |
|---|---|---|
| Retrospective telemetry audit | DONE (`4fb39223a9`) | closed |
| Constrained-realisation surrogate + null validation | DONE (`47ee07d`) | closed |
| Per-step multi-stream recorder | **IN FLIGHT — not on `origin/main`** | session `suspicious-williamson-73da0d` |
| **Structure-destroying (landmark-removal) arm** | **DONE — this record** | this session |
| Prospective recording run (script + queue entry) | NOT STARTED — blocked on the recorder; must go through `/queue-experiment` | unowned |
| Ablation series (the only A-vs-B discriminator) | NOT STARTED | unowned |

Work-graph classification: the run is `complicated (buildable)` once the recorder lands — it is
execution backlog, not discovery debt. Nothing here is `complex (probe-gated)`.

The module is usable independently of the recorder: it consumes only the agent's hippocampal
surface and returns plain dicts, so a driver can attach it as soon as there is something to
record.
