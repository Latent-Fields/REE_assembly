# Failure Autopsy — V3-EXQ-543e (arc_062_rule_apprehension:GAP-B)

**Date:** 2026-05-17T06:09:58Z
**Experiment:** `v3_exq_543e_arc062_spcem_falsifier`
**Run:** `v3_exq_543e_arc062_spcem_falsifier_20260517T010202Z_v3`
**Outcome:** FAIL — `evidence_direction: non_contributory`,
`per_claim {ARC-062: weakens, MECH-309: non_contributory}` (pre-registered
`_compute_per_claim_direction` grid; **NOT force-mapped**)
**Run quality:** real run, `dry_run=False`, `exit_reason: ok`,
`actual_secs=4760.7` — clean completion, scientific FAIL, not a crash.
**Type:** non-claim-weighing autopsy (analysis/handoff only).

---

## One-line verdict

**H3 confirmed — confound-free substrate-level finding, not an artifact.**
SP-CEM + stratified elites delivered genuinely first-action-diverse,
non-degenerate candidates to the probe; the persistent inert-gating
cleanly isolates the ARC-062 `GatedPolicy` head's **z_world-only input**
as the architectural bottleneck. Routes to the pre-registered **option 2:
augment the head input with the first-action one-hot** (`/implement-substrate`),
then re-issue the falsifier as V3-EXQ-543f.

---

## What FAILed

| Arm | reef_fraction | Note |
|---|---|---|
| ARM_0 baseline | 0.6918 | |
| ARM_1 dacc_only | 0.6918 | D1 delta exactly 0.0 (dACC anti-recency: zero behavioural change) |
| ARM_2 gated_only | 0.5600 | `p1_inert_gating_detected=True` all 3 seeds |
| ARM_3 both | 0.5600 | D2 delta exactly 0.0; D3 = -0.1317 (gated *reduced* reef use) |

`probe_gate_arm2_failed=True`, `probe_gate_arm3_failed=True`;
`n_inert_gating_seeds_arm2=3`, `n_inert_gating_seeds_arm3=3`. Same
inert-gating signature as 543b (TV exact-zero) / 543c (TV ~1e-7) / 543d.

---

## Hypotheses discriminated

A direct diagnostic harness replicated 543e's exact ARM_2 (gated ON,
dacc OFF) P0 stepping path — `sense -> record_transition -> sense ->
clock.advance -> generate_trajectories -> select_action -> env.step` —
and instrumented `agent.hippocampal.get_last_propose_diagnostics()` plus
the pairwise L2 spread of the exact tensor the probe uses
(`candidate_features = cat([c.world_states[1] for c in candidates[:8]])`).

### H1 — SP-CEM not engaging at probe time / candidates collapsed: **FALSE**

- `candidate_unique_first_action_classes`: **mean 4.95** (min 4, max 5)
- `candidate_first_action_entropy`: **mean 1.26**
- `n_candidates per propose`: 32 (full population)
- `support_preserving_active steps = 0 / 22`

`support_preserving_active=0` is the **expected** signature when
stratified-elites already deliver diversity without needing the injection
path — V3-EXQ-567's own notes record exactly this ("stratified elites
achieve diversity WITHOUT triggering the injection path, so
support_preserving_active stays 0 when stratified works well"). The
candidate population is genuinely diverse (≈5 unique first-action
classes). SP-CEM is engaging via the stratified path.

### H2 — Probe-feature construction masking variance (543b Cause-1 repeat): **FALSE**

- `world_states[0]` pairwise meanL2 = **0.0 exact** (the 543b Cause-1
  quantity — confirms the world_states[1] fix is correctly in place; the
  script is NOT reading the identical pre-action z_world)
- `world_states[1]` pairwise meanL2 ≈ **0.013** (range 0.008–0.016)
  — ~1000x larger than 543b's ~1.2e-5. The probe's `candidate_features`
  are non-degenerate and distinguishable across the K candidates.

The 2026-05-11 candidate-distinguishability confound is **definitively
eliminated**: the features the probe reads genuinely differ per candidate.

### H3 — Genuine substrate finding: **CONFIRMED**

The discriminating signal is strong in **action space** but washed out
by the time it reaches the head's **z_world input space**:

| Quantity | Value |
|---|---|
| Candidate first-action classes (unique) | **4.95** |
| `world_states[1]` vector norm per candidate | 0.6705 |
| Cross-candidate per-dim std | 0.001473 |
| **Cross-candidate variation / signal magnitude** | **0.0022 (0.22%)** |

SP-CEM/stratified produces ≈5 distinct first-action classes, but E2's
world-forward model compresses that categorical diversity to **0.22% of
the z_world signal magnitude** in `world_states[1]`. The ARC-062
`GatedPolicy` head reads z_world-derived features (R1 multi-stream
`z_world, z_self, z_harm_a`) — it does **not** see the first action. The
candidate-distinguishing information exists upstream but is ~450x below
the signal it is embedded in by the time the head can read it. The head
therefore cannot produce context-conditional behavioural divergence, and
the probe correctly detects inert-gating.

Additional structural finding (not the primary bottleneck): only
**~9–10% of steps** generate fresh candidates via an E3 tick; the rest
return the MECH-057a/MECH-090 cached `_committed_candidates`. This is
expected heartbeat-gating behaviour and does not change the verdict (the
cached set is itself stratified-diverse), but it is logged for the
re-issue design.

---

## Why this is contributory evidence, not a wasted run

543e is the **first run in the 543 lineage where the substrate
confound is provably absent**. 543b/c/d were `non_contributory` because
the collapsed CEM left `world_states[1]` at ~1e-5 (the heads had nothing
to discriminate). Here `world_states[1]` ≈ 0.013 and first-action classes
≈ 4.95 — the substrate delivers diversity. With that confound removed,
the persistent inert-gating is a **clean, confound-free isolation of the
ARC-062 head's z_world-only input as the architectural bottleneck**. The
script's pre-registered grid maps the probe-gate short-circuit to
`non_contributory` (a conservative pre-registration authored when the
substrate confound was still suspected); the underlying finding is in
fact the substrate-level result the MECH-309 / ARC-062 narrative
predicts: the gated-policy substrate as currently wired (z_world-only
head input) is insufficient.

**The `non_contributory` direction is left as-is and NOT force-mapped.**
The contributory weight of this run is captured by this autopsy and the
plan-doc routing, not by re-labelling the manifest.

---

## Routing recommendation

**Pre-registered option 2 (script header "Possible outcomes" + 2026-05-11
decision-log): augment the ARC-062 `GatedPolicy` head input with the
first-action one-hot — `/implement-substrate`.** This diagnosis supplies
direct quantitative justification: the discriminating signal (first-action
class, 4.95 unique) is strong and available but is compressed to 0.22%
relative magnitude in the z_world the head currently reads. Feeding the
first-action one-hot directly to the head restores the categorical signal
to the head's input space.

Then re-issue the falsifier on the augmented head as **V3-EXQ-543f** via
`/queue-experiment` (canonical 543d 2x2 factorial + SP-CEM substrate
unchanged; only the head input contract changes). supersedes V3-EXQ-543e.

GAP-B status: `in-progress` → remains `in-progress`, blocked on the
option-2 substrate change. GAP-C / GAP-D stay `open`, correctly sequenced
after a contributory falsifier PASS.

**Not recommended:** ARC-062 substrate-rationale retirement. The substrate
is not redundant — it is under-fed. The diagnosis shows the mechanism is
sound but the head's input contract is the gap, which is precisely what
option 2 fixes.

---

## Handoff notes

- `review_tracker.json` NOT modified here (diagnose-errors responsibility
  boundary). V3-EXQ-543e is a completed FAIL now diagnosed/discussed —
  flag for the next governance/review pass to add the run_id to
  `reviewed_run_ids`.
- `claims.yaml` NOT modified. GAP-B unblocks/promotes nothing until a
  contributory falsifier PASS.
- The V3-EXQ-543e manifest `evidence_direction` is left
  `non_contributory` (not superseded yet — supersession is set when
  V3-EXQ-543f is queued, per the EXQ versioning policy).
- Diagnostic harness: `/tmp/diag_543e_spcem.py` (throwaway; not committed).

---

# Addendum (session B, 2026-05-17T06:54:38Z) — dACC root cause + 543d cluster

> Independent second-session autopsy. **Complementary, not contradictory.**
> Session A above root-caused the *gated-policy* axis (ARC-062 z_world-only
> head under-fed despite genuinely diverse SP-CEM candidates). This
> addendum root-causes the *other* factorial axis — the **exact-zero
> D1/D2** that A recorded as a fact ("dACC anti-recency: zero behavioural
> change") but did not explain. Both findings are true and independent:
> the 2x2 had BOTH a dead dACC axis (config bug) AND an under-fed ARC-062
> head (substrate). Routing decisions below are user-confirmed via the
> interactive gate.

## A1. Root cause of the exact-zero D1/D2 (decisive, in adapter code)

`DACCtoE3Adapter.forward()` — `ree-v3/ree_core/cingulate/dacc.py:482-484`:

```python
weight = self.config.dacc_weight * float(bundle.get("drive_gain", 1.0))
if weight == 0.0:
    return torch.zeros_like(mode_ev)   # returns BEFORE the suppression term (line 491)
```

V3-EXQ-543e sets only `dacc_suppression_weight=0.5` and **leaves
`dacc_weight=0.0`** (script docstring lines 66-69 treat it as a peer
"other channel"). But `dacc_weight` is the adapter's **master gain**.
With it 0.0 the adapter returns the zero vector *before* the
`dacc_suppression_weight * suppression` term (line 491) ever executes.
`DACCConfig` docstring: *"All weights default to zero so the module is
no-op."* Adapter docstring: activation requires *"dacc_weight > 0
(combined with at least one sub-weight > 0)."*

`use_dacc=True` instantiates the module, `agent.py:3489-3492` fills the
FIFO via `record_action`, and `agent.sense(...obs_harm_a...)` populates
`z_harm_a` (so the `z_harm_a is not None` gate at agent.py:2683 passes).
The history and bundle are live — only the adapter's master gain is zero,
so its E3 score_bias is identically zero every step. Hence ARM_0≡ARM_1
and ARM_2≡ARM_3 **byte-identical across all 3 seeds** (D1=D2=0.0 exactly).
The MECH-260 anti-recency axis was never live. "dACC produced zero
behavioural change" is a configuration artifact, NOT a MECH-260 signal —
it must not be read as evidence MECH-260 is ineffective.

## A2. Cluster finding (load-bearing) — 543d carries the identical bug

`grep` confirms V3-EXQ-543d has the same config pattern (same docstring
lines 65-66; `dacc_suppression_weight=DACC_SUPPRESSION_WEIGHT`, no
`dacc_weight`). 543d's verdict was attributed *solely* to the collapsed-CEM
substrate; in fact its dACC axis was also inert for this independent
reason. **Structural property (one bug, not two):** across two
structurally-different CEM substrates (collapsed-CEM 543d, SP-CEM 543e),
the MECH-260 second axis of the 543d-lineage falsifier has **never been
live**. The "2x2 factorial" has only ever been a confounded 1x2. The
543d→543e supersession rationale ("543d invalid *only* because
collapsed-CEM") is incomplete.

## A3. Reconciled epistemic category

This run is **dual-natured**:
- **dACC axis → `configuration_error`** (harness misconfiguration;
  `dacc_weight=0.0` master-gate). NOT substrate, NOT claim pressure.
- **ARC-062 gated axis → substrate under-fed** (session A's H3:
  z_world-only head input; genuine substrate question).

Session A's `non_contributory` (overall) is correct and not force-mapped.
The manifest's **per-claim `ARC-062: weakens` is the wrong layer
attribution** — the gated-only contrast ran inside a degenerate factorial
(dead dACC axis) with the gating probe inert in 3/3 seeds; that is a
harness/translation gap, not soft evidence against ARC-062.

## A4. Routing refinements (user-confirmed; extend, do not replace, §"Routing recommendation")

1. **Confirmed dual routing.** Session A's `/implement-substrate` option-2
   (augment ARC-062 head input with first-action one-hot) **stands** and
   matches the user's decision. **Addition:** the re-issued **V3-EXQ-543f**
   must *also* set `dacc_weight>0` (e.g. 1.0) alongside
   `dacc_suppression_weight=0.5`, AND carry a pre-flight non-degeneracy
   assertion (dACC-on arm != dACC-off arm by epsilon) — otherwise the
   MECH-260 axis stays dead even after the head augmentation, and 543f
   would *again* be a confounded 1x2. Also correct the script docstring's
   mischaracterisation of `dacc_weight` as a peer channel.
2. **Recommend governance reclassify** the manifest per-claim direction
   **ARC-062 `weakens` → `non_contributory`** (keeps ARC-062
   candidate/v3_pending; no conflict-ratio movement; non_contributory is
   inactive in scoring — no illusory conflict resolution).
3. **Retrospective caveat on V3-EXQ-543d** (governance to note): its
   recorded `ARC-062=weakens / MECH-309=non_contributory` was invalid for
   the `dacc_weight=0` reason in addition to the collapsed-CEM reason.
   Supersession (543e supersedes 543d) already implies inactive; add the
   explicit note so the reason is not mis-recorded as substrate-only.
4. `pending_retest_after_substrate`: the ARC-062 option-2 substrate change
   is real (session A); the dACC fix is config-only. **543f needs BOTH**
   landed before it is a valid test of the 2x2.

## A5. Biological-reference triage (dACC axis)

Not a biology case. MECH-260 (dACC recency/monostrategy suppression —
Scholl & Klein-Flugge 2018) has a working existence proof and the adapter
behaves exactly as its own contract documents. Pure configuration error.
**No /lit-pull indicated** for the dACC axis.

## A6. Concurrency note

Two `/failure-autopsy` sessions ran on V3-EXQ-543e independently. Session
A committed first (`481d4eef0b`). Session B (this addendum,
TASK_CLAIMS `failure-autopsy-exq543e-20260517T060331Z`) appended rather
than overwrote, per user direction. No claims.yaml / manifest /
review_tracker / substrate_queue edits by either session — governance
applies the recommendations.
