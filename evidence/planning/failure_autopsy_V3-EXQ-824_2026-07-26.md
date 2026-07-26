# Failure Autopsy: V3-EXQ-824 (Q-081 shared-organisation landmark-removal)

Generated: `2026-07-26T18:16:27Z`
Scope: single
Session: `optimistic-ellis-4357c6`

## 1. Facts reconstruction

**Manifest**: `v3_exq_824_q081_shared_organisation_landmark_removal_20260726T165630Z_v3`
(`REE_assembly/evidence/experiments/v3_exq_824_q081_shared_organisation_landmark_removal_20260726T165630Z_v3.json`).
`outcome: FAIL`, `evidence_direction: weakens` (as recorded — disputed below), `non_degenerate: true`.

Self-route: `interpretation.label = "wired_gates_only_landmark_invariant"` — "Outcome B: RV(z_world,
operating_mode) delta (ON-minus-REMOVED) mean=0.0000 did not clear the effective floor 0.0300 across
5 valid seeds. Whatever cross-stream coupling exists survives landmark removal — it was measuring the
clock, not landmark-dependent organisation."

All four `preconditions[]` report `met: true`, including `landmark_arm_behavioural_reach`
(measured 1.0 vs threshold 1.0 — "the boundary stream has at least one live consumer"). The single
load-bearing criterion `C_ablation_delta_clears_effect_size_floor` failed: `measured=0.0`,
`threshold=0.03` (`effective_floor = max(1.5*sd_delta, 0.03)`, and `sd_delta=0.0`).

**The measured quantity is not merely "below floor" — it is bit-identical.** `delta_summary` records
`rv_on_all_seeds` and `rv_removed_all_seeds` as literally the same Python floats at every seed
(`0.21475614340838226`, `0.17546435578839678`, `0.10284282041100536`, `0.04482955468581675`,
`0.13379026090355503` — verified `on == rem` at full float64 precision for all 5 seeds, not rounded
agreement). `sd_delta = 0.0` exactly. This is a stronger and qualitatively different signal than "no
detectable effect": a real stochastic manipulation applied to two independently-simulated arms
(different `arm_fingerprint` per arm, confirmed different `preservation_removed.mean_true_emitted_alignment`
vs `preservation_on` at the boundary-stream level, e.g. seed 0: 0.95 vs 0.71) cannot by chance produce
an exactly-equal downstream statistic across 5 seeds unless that statistic's computation never actually
depended on the manipulated variable.

**Script**: `ree-v3/experiments/v3_exq_824_q081_shared_organisation_landmark_removal.py`. `PRIMARY_PAIR
= ("z_world", "operating_mode")`. Per-seed: `agent_p0` warmed up once, then deep-copied into two arms
(`agent_on`, `agent_rm`), each stepped through a fresh but seed-identical env with a `LandmarkScrambler`
attached (`mode="off"` for ON, `mode="iei_permute"` for REMOVED — a yoked permutation of the ON arm's
own boundary train). `analyze_arm_trace()` computes `rv_primary` from each arm's own
`StreamTraceRecorder` output.

**Queue entry**: `V3-EXQ-824`, `ree-v3/experiment_queue.json`. `experiment_purpose: evidence`. No
`supersedes`. First real run of the landmark-removal arm named in Q-081's own design notes
(`evidence/planning/q081_landmark_removal_arm_design.md`, built 2026-07-22).

**Expected vs observed**: expected either RV(ON) - RV(REMOVED) ≥ 0.03 (Outcome A, landmark-dependent
organisation) or a small/zero delta with the two arms otherwise showing independent stochastic
variation (Outcome B, genuinely landmark-invariant). Observed: exact numerical identity, which is
neither — it is the signature of the manipulation never reaching the measured pair's computation.
**Failed criterion**: discrimination criterion (`C_ablation_delta_clears_effect_size_floor`), but the
underlying defect is in a *precondition* (`landmark_arm_behavioural_reach`) that should not have
passed.

## 2. Source-level root cause

`behavioural_reach.consumers` for this run: `{use_invalidation_trigger: true, use_anchor_sets: false,
use_per_region_vs: false, use_staleness_accumulator: false}`, `live_consumers: ["use_invalidation_trigger"]`.

`assert_behavioural_reach()` (`ree-v3/experiments/_lib/q081_landmark_removal.py:857-897`) defines
`has_behavioural_reach = segmenter_on and live`, where `live` is non-empty if **any one** of the four
consumer flags is set. This treats `use_invalidation_trigger` alone as sufficient "reach."

Traced in `ree_core/`:

- `ree_core/hippocampal/module.py:215-225`: MECH-287 (`use_invalidation_trigger`) subscribes to
  MECH-288 `BoundaryEvent`s and re-emits them as `BroadcastEvent`s into `self._broadcast_event_queue`.
  The module's own comment: *"The broadcast queue is drained by downstream MECH-269 anchor-reset (T3)
  / MECH-284 staleness accumulator consumers."*
- `ree_core/agent.py:4479-4488`: `tick_anchor_set()` — the MECH-269 consumer that actually installs/
  remaps anchors and (via `write_anchor`) touches `z_world` — is gated on `use_anchor_sets`, **not**
  `use_invalidation_trigger`. Off in this run.
- `ree_core/agent.py:4501-4514`: `apply_invalidation_broadcasts_to_regions()`, the other real reader of
  `_broadcast_event_queue`, is gated on `use_per_region_vs`. Also off in this run.
- `ree_core/agent.py:4323-4338`: the **only** other place `drain_broadcast_events()` is called is a
  tick-boundary bounding flush, run explicitly *because* — per the code's own comment — "Phase 3
  consumers... will call drain_boundary_events()/drain_broadcast_events() in select_action() once they
  are implemented. Until Phase 3 lands nothing in select_action() drains the queues" — i.e. this flush
  exists only to bound unconsumed queue growth, not to apply any effect.

So with only `use_invalidation_trigger=True`, MECH-287 fires, the broadcast queue fills, and is then
discarded by the bounding flush every tick. **No code path in this configuration reads the queue for
any purpose that could influence agent state, `z_world`, or `operating_mode`.** The landmark
manipulation (which measurably altered the boundary stream itself — `preservation_removed` shows
`mean_true_emitted_alignment` dropping from ~0.95 (ON) to ~0.71 (REMOVED) at seed 0) had zero causal
path to the measured pair. Bit-identical `rv_primary` is exactly the expected outcome of that, not
evidence of Outcome B.

**Confirmed already known and already fixed in a sibling script.** `ree-v3/experiments/
v3_exq_827_inv091_cross_stream_similarity_band.py:216-231` (`_build_cfg`), docstring verbatim:

> "Shared INTACT-rate config for all three arms. `use_anchor_sets=True` gives the landmark scrambler
> real reach into z_world via MECH-269 `write_anchor` (`assert_behavioural_reach` is satisfied by
> `use_invalidation_trigger` alone, but the anchor path is the one that actually touches z_world, which
> is what this experiment measures)."

827's author identified precisely this defect and worked around it locally by setting
`cfg.hippocampal.use_anchor_sets = True` after the shared `q081_profile_kwargs()` (which does not
include `use_anchor_sets`) is applied. 824's script relies on `q081_profile_kwargs()` alone
(`"q081_flags": {k: True for k in q081_profile_kwargs() if k != "use_sleep_loop"}`) and never sets
`use_anchor_sets`. Per `WORKSPACE_STATE.md` (2026-07-26T15:27Z entry), 824 and 827 were drafted
concurrently and collided on the same queue-ID before being separated — the fix landed in one sibling
and not the other, i.e. this is a documented instance of a known-bug fix failing to propagate across
independently-authored siblings of the same experiment family, not a bug nobody had seen before.

`v3_exq_814_mech288_input_stream_isolation_diagnostic` (the third user of
`assert_behavioural_reach`/`q081_landmark_removal`, already run 2026-07-24,
`evidence_direction: non_contributory`, unrelated finding) does not measure the (z_world,
operating_mode) RV pair and is not implicated by this specific defect — checked, not investigated
further.

## 3. Claim-layer map

**Q-081** (`open_question`, `status: candidate`, `epistemic_category: standard`,
`implementation_phase: v3`). Asks whether REE's multi-rate execution produces genuinely SHARED
cross-stream organisation (Outcome A) versus organisation trivially implied by configured rates and
wired gates (Outcome B) — this run is the first live test of the structure-destroying (landmark-removal)
arm the claim's own notes specify as mandatory alongside the surrogate-null control.
`depends_on`: SD-006, ARC-023, ARC-025, MECH-288, MECH-321, MECH-091.

**Did the experiment test the claim under conditions where it could express itself?** No. The claim's
own design notes (`claims.yaml` Q-081, "STRUCTURE-DESTROYING ARM BUILT 2026-07-22") explicitly name
the landmark-removal arm as wrapping "the single choke point feeding all three live consumers (MECH-288
boundary queue, MECH-287 broadcast trigger, MECH-269 anchor install)" — the design record correctly
anticipated that MECH-269 (anchor install) mattered. The *script* did not follow through: it enabled
only the MECH-287 broadcast trigger, which (per §2) has no causal reach to the measured pair on its
own. This is a test-design implementation gap, not a fair test of Q-081 Outcome A vs B.

## 4. Biological-reference triage

Q-081 is a methodological/architectural claim about whether REE's heterogeneous-timescale streams
exhibit genuinely shared organisation, grounded in real cross-timescale-coordination literature already
cited in the claim (Shared spatial/temporal principles govern connectome dynamics across timescales,
PNAS 2026; Lancaster et al. 2018 on surrogate construction; Chang, Nastase & Hasson 2022 on the
scrambled-story structure-destroying control that the landmark-removal arm is explicitly modelled on).
The experimental design (surrogate null + structure-destroying arm) is well-grounded and not a
formal-definition import needing a fresh lit-pull — the defect here is REE-internal (a precondition
check too permissive for its own wiring), not a biology/architecture mismatch.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear (not weakened) | Design anticipated the right consumer (MECH-269); script didn't wire it. Q-081 not fairly tested. |
| Biological reference | clear | Scrambled-control precedent (Chang/Nastase/Hasson) correctly instantiated at the design-doc level. |
| Developmental / dependency prerequisites | present | MECH-269, MECH-284, MECH-287, MECH-288 all `status: implemented` in `substrate_queue.json` — no new substrate needed. |
| Implementation completeness | partial | MECH-287 fires (symbol of the mechanism); nothing in this config reads its output (no functional role reaching the DV). |
| Environment adequacy | adequate | Not the limiting factor. |
| Measurement adequacy | misleading | `assert_behavioural_reach()`'s "any one flag" definition of `live` does not imply reach to the specific measured pair; passed on a technicality. |
| Integration adequacy | isolated | MECH-287 broadcast queue populated but undrained by anything else in this config — confirmed by source trace, not inferred. |
| Scale / capacity | adequate | Not implicated. |

Dominant diagnosis: **precondition_unmet**, mislabeled by the self-route as a substantive Outcome-B
finding (`wired_gates_only_landmark_invariant`). This is the same shape as the canonical V3-EXQ-642
incident this skill exists to catch: the self-route is a hypothesis, not a verdict, and here it is
wrong — the precondition test that gated it is the actual defect.

## 6. Learning extracted

- Existing dependency **strengthened, not weakened**: nothing here bears on whether Q-081's Outcome A
  or B is true. The finding is entirely about test-design validity.
- **Measurement gap** in a shared library precondition check (`assert_behavioural_reach`,
  `experiments/_lib/q081_landmark_removal.py`): "at least one live consumer flag" is not equivalent to
  "the enabled consumer reaches the measured pair." For the (z_world, operating_mode) primary pair
  specifically, only `use_anchor_sets` and/or `use_per_region_vs` provide real reach;
  `use_invalidation_trigger` alone does not (confirmed by source trace of every consumer of
  `_broadcast_event_queue`).
- **Propagation-prevention finding**: the fix already exists, independently discovered and applied in
  sibling script `v3_exq_827_inv091_cross_stream_similarity_band.py` (`use_anchor_sets = True`,
  documented in its own docstring), but did not propagate to `v3_exq_824` because the two scripts were
  authored concurrently and collided on a queue ID before being separated (`WORKSPACE_STATE.md`
  2026-07-26T15:27Z). Fixing the shared library's precondition check — rather than relying on each new
  script's author to independently rediscover 827's docstring — is the correct place to stop this
  recurring for any future Q-081-family script.

## 7. Repair pathway

**Node classification**: `complicated (buildable)` for the redesign (the fix is a named, already-proven
change — enable `use_anchor_sets`, mirroring 827 — with no open question); the underlying MECH-269/284/287/288
substrate is already `implemented`, so this is **not** `/implement-substrate` work.

**Routing: `/queue-experiment`**, same-question redesign (V3-EXQ-824a, alphabetic suffix — the
scientific question, Outcome A vs B, is unchanged; only the implementation was wrong). Scope for the
redesign:

1. Set `cfg.hippocampal.use_anchor_sets = True` after `q081_profile_kwargs()` in `_build_cfg` /
   equivalent, mirroring `v3_exq_827_inv091_cross_stream_similarity_band.py:230` — the proven fix.
2. **Tighten `assert_behavioural_reach()`** in `experiments/_lib/q081_landmark_removal.py` so `live`
   for the purposes of "reach to (z_world, operating_mode)" requires `use_anchor_sets` and/or
   `use_per_region_vs` specifically, not `use_invalidation_trigger` alone — or at minimum, warn/require
   an explicit opt-in when only the broadcast-trigger-alone configuration is used, so this cannot pass
   silently for a future Q-081-family script the way it did here. This is the propagation-stopping fix;
   scope it into the same redesign work so it lands with test coverage (the existing 35-contract suite
   in `tests/contracts/test_q081_landmark_removal.py`) rather than as an unreviewed drive-by edit.
3. Re-run with the fixed config; verify the ON/REMOVED `rv_primary` values are NOT bit-identical before
   trusting any Outcome A/B verdict (a cheap smoke-level check that would have caught this immediately).

**Recommended `evidence_quality_note` for Q-081** (governance to write, not this skill):

> V3-EXQ-824 (2026-07-26) self-routed `wired_gates_only_landmark_invariant` (Outcome B) but is
> `non_contributory`, not `weakens`: the ON/REMOVED arms' RV(z_world, operating_mode) statistics were
> bit-identical at all 5 seeds because the run's only enabled consumer flag (`use_invalidation_trigger`)
> has no causal reach to z_world/operating_mode in this codebase (confirmed by source trace,
> `failure_autopsy_V3-EXQ-824_2026-07-26`) — the landmark manipulation never reached the measured pair.
> Sibling script V3-EXQ-827 already carries the fix (`use_anchor_sets=True`). Superseded by V3-EXQ-824a
> pending a corrected re-run with real behavioural reach.

## 8. Interactive gate

User confirmed (chat, 2026-07-26): "we need to proceed to ensure we correct all this and stop it
propagating" — endorsing the diagnosis and instructing that the fix (library precondition tightening +
824a redesign) be pursued as active follow-on work rather than left as a passive recommendation. Per
the project's mandatory skill path for experiment scripts (`CLAUDE.md` "Experiment Scripts"), the actual
script/library edit is chipped to `/queue-experiment` (code review + smoke test required), not
performed inline in this autopsy.

## 9. Routing summary

- `evidence_direction`: `weakens` -> `non_contributory` (recommended; governance applies)
- `epistemic_category`: `measurement_test_design_defect`
- `recommended_substrate_queue_entry.action`: `none` (no substrate build needed)
- Routing: `/queue-experiment` (V3-EXQ-824a redesign + `assert_behavioural_reach` library fix) — chipped
  as a follow-on session per the mandatory skill path.
- Re-derive brake: does not apply (`epistemic_category` is not `substrate_ceiling`).
- Step 9b (hypothesis ledger): evaluated, skipped — no `fanout_recommendation` (single target, not a
  discrimination between live hypotheses), and none of the 12 existing `hypothesis_space_registry.v1.json`
  questions tag Q-081.
