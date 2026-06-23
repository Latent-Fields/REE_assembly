---
title: "Commit/release-DURATION lever: graded natural-commit-occupancy release"
parent: "Executive & PFC Control"
grandparent: Architecture
nav_order: 4
---

# Commit/release-DURATION lever: graded natural-commit-occupancy release

**Status:** IMPLEMENTED 2026-06-20 (substrate; PROMOTES NOTHING)
**Subject:** control_plane.natural_commit_occupancy_release
**Substrate-queue rung:** `f_dominance_conversion_ceiling` -> rung 6 (commit/release-DURATION face)
**Cluster claims (candidate):** SD-034 (closure operator / done-token release), MECH-090 (commitment-gated routing latch), MECH-342 (commit-maintenance-release on degraded readiness), MECH-445 (closure->beta coupling), MECH-446 (de-commit-authority magnitude)
**Grounding:** ARC-106 brain-like construction; BG-3 biology grounding (`evidence/literature/targeted_review_commit_release_duration_latch/SYNTHESIS.md`, divergence **D1**)

## Role

This is the **commit/release-DURATION** lever of the F-dominance front -- **PARALLEL to**, not an escalation of, the selection-face levers (MECH-439 conflict-graded width / commit-temperature; MECH-448 rank-preserving F->eligibility demotion). Those act at E3 **selection**; this acts on how long a committed action is **held**.

It is **NOT blocked on GAP-I / V3-EXQ-689c** (a dead-end selection-face parametric retest). Per the 460h governance note (`behavioral_diversity_isolation:GAP-I` `governance_2026_06_20`), the commit/release-duration face is its own lever, separate from the selection-face levers (k / commit-T).

## Problem (V3-EXQ-460h)

On strong (F-decisive) seeds the bistable beta latch elevates once and then **holds for ~2400-2600 steps**, because nothing releases it: a decisive F-gap means "good options," so MECH-342 maintenance-release (which fires on *degraded* readiness) is silent, and no closure fires so SD-034 is silent. That monolithic natural-commit occupancy **swamps** the SD-034 closure de-commit, leaving the de-commit certifiers disjoint across seeds:

| seed | OFF committed_steps | closure commit_intent |
|------|---------------------|-----------------------|
| 42 (strong) | 2414 | 0 |
| 43 (strong) | 2609 | 0 |
| 44 (weak)   | 0    | 375 |

MECH-445 (commit-intent) and MECH-446 (de-commit occupancy drop) never co-occur on the same seed -- the **460h disjoint-certifier problem**. The de-commit is measurable only where the natural commit is *weak*.

This lever makes the F-driven natural commit **less monolithic** so weak-natural-commit becomes the norm across seeds, dissolving the 460h problem (MECH-445 commit-intent fires broadly AND MECH-446 de-commit becomes occupancy-attributable on the same seeds).

## Biological constraint -- BG-3 SYNTHESIS divergence D1 (load-bearing)

Biology does **not** set commitment DURATION with a separate fixed refractory clock. It times the hold with a **graded BG/pallidal urgency** signal that rises over the held epoch (Thura, Cabana, Feghaly & Cisek 2022, *PLoS Biol* [10.1371/journal.pbio.3001861]) and/or makes maintenance **co-extensive with the executing action** (Jin, Tecuapetla & Costa 2014, *Nat Neurosci* [10.1038/nn.3632]). REE's existing committed-run-scaled beta-gate refractory is the "tuned, not bio-sourced" divergence D1 names.

**Therefore the lever is a GRADED release, never another fixed refractory constant.**

## Solution

A pure-arithmetic regulator `ree_core/policy/natural_commit_urgency.py`
(`NaturalCommitUrgencyRelease` + `NaturalCommitUrgencyReleaseConfig`), sibling to
`commit_maintenance_release.py` (MECH-342). It **reuses** `BetaGate.committed_run_length`
(the MECH-090 commit-gate machinery) rather than maintaining its own latch
(ARC-106 guardrail G2: reuse-before-duplicate -- **no parallel latch module**).

Two D1-faithful release modes, both togglable under one master flag (so the
sequenced 460i-successor falsifier can discriminate which lifts):

### (1) URGENCY mode (Thura/Cisek)

Each maintenance tick the latch is held by a *natural* commit:

```
decisiveness_scale = 1 + gap_entry_sensitivity * gap_norm_at_entry
urgency += urgency_rate * decisiveness_scale
fire when urgency >= release_bound
```

`gap_norm_at_entry` in [0, 1] is the normalised top-F decisiveness captured at
commit entry (1 = a decisive F-gap = the kind of commit that monopolises the
latch). The **gap-scaling is the load-bearing piece**: an F-decisive natural
commit accrues release-urgency *faster*, so the strongest-F holds -- exactly the
ones that swamp the de-commit -- are shortened most. This attacks the
F-dominance directly in the duration domain and **folds in the "gap-scaled
commit-entry threshold" impl_hint candidate** (commit-entry decisiveness sets
the release rate).

`gap_entry_sensitivity = 0` reduces the urgency to a flat fixed-rate timeout --
the contrasted **"another fixed refractory" control** the D1 falsifier compares
the gap-scaled lever against.

### (2) ACTION-EXTENT mode (Jin)

Release the natural commit when the committed trajectory's executed action
sequence **completes** (the agent has stepped through all of
`trajectory.actions` rather than repeating the last action indefinitely).
Renders the "maintenance co-extensive with the executing action" biology + the
"natural-commit run-length cap" impl_hint candidate as a **behaviourally-grounded
cap** (the trajectory horizon), NOT a tuned constant. Fires regardless of
urgency when the sequence is complete.

## Divergence ledger (ARC-106)

| REE mechanism | Biological reference | Divergence | Load-bearing? | Falsifier |
|---|---|---|---|---|
| Graded urgency-scaled release of the natural-commit latch, rate scaled by entry decisiveness | Graded BG/pallidal urgency timing the hold (Thura 2022); maintenance co-extensive with the action (Jin 2014) | Replaces the "tuned, not bio-sourced" committed-run-scaled refractory (D1) with a graded urgency / behaviour-extent release | **YES (resolves D1)** | The graded lever changes committed-epoch length and lifts the de-commit DV where the fixed refractory does not (the 460i-successor). `gap_entry_sensitivity=0` is the flat-refractory control; if the gap-scaled rate does not beat it, the grading is decorative. |

## Distinct from siblings (not a duplicate)

- **MECH-342** maintenance-release fires on *degraded* readiness (poor options) and is therefore **silent on the healthy-but-prolonged decisive commit** that actually monopolises the latch -- exactly why strong seeds hold ~2400 steps. This fires on a healthy, prolonged natural commit (the duration-urgency face MECH-342 does not cover).
- **SD-034 Leg-B committed-run-scaled refractory (MECH-446)** holds the latch *down post-closure* (how long to keep it released). This shortens the natural commit's occupancy *up* (how long it stays elevated). It does not install a refractory; it releases.
- **MECH-091** urgency-interrupt fires on z_harm threat. This is a *duration* urgency with no harm-stream input.
- **ARC-028/MECH-105** completion releases on a *high* completion signal (good plan). This releases on held-duration urgency or executed-sequence completion regardless of plan quality.

## Psychiatric failure-mode column (ARC-106 required)

| Break | Disorder analog |
|-------|-----------------|
| Urgency too weak / sensitivity 0 / bound too high (under-release) | rigidity / perseveration / catatonic over-maintenance (the current F-monopoly: holds ~2400 steps) |
| Urgency too strong / bound too low (over-release) | distractibility / disorganisation; commitment cannot be sustained against noise |

*Honesty guardrail (ARC-106): these state what each break resembles, not that the lever is the disorder mechanism.*

## Config (REEConfig + from_dims, all no-op default -> bit-identical OFF)

| Param | Default | Purpose |
|-------|---------|---------|
| `use_natural_commit_urgency_release` | False | master switch |
| `natural_commit_release_urgency_mode` | True | enable the Thura/Cisek urgency mode (consulted only when master on) |
| `natural_commit_release_action_extent_mode` | True | enable the Jin action-extent mode (consulted only when master on) |
| `natural_commit_urgency_rate` | 0.01 | per-tick base urgency increment |
| `natural_commit_urgency_release_bound` | 1.0 | urgency-mode release threshold |
| `natural_commit_urgency_cap` | 1.5 | hard clamp on urgency (>= bound) |
| `natural_commit_gap_entry_sensitivity` | 1.0 | **load-bearing** gap-scaling; 0.0 = flat control |
| `natural_commit_urgency_onset_ticks` | 0 | grace ticks before urgency accrues |

## Data flow

```
commit entry (bistable elevate site, agent.py): result.committed (natural)
  -> note_commit_entry(gap_norm)  [arm + reset urgency; gap_norm from result.scores]
each subsequent committed tick (the MECH-342 release region):
  -> tick(committed_run_length=beta_gate.committed_run_length,
          action_sequence_complete=_committed_step_idx >= horizon)
  -> fire -> beta_gate.release(); _committed_step_idx=0;
             _committed_anchor_keys=None; e3._committed_trajectory=None
agent.reset() -> regulator.reset()  (per-episode)
```

A purely closure-coupled elevation (`result.committed` False) does **not** arm
the lever -- its occupancy is governed by the SD-034 closure machinery.

## Diagnostics (`get_state()`)

`ncur_last_occupancy_at_release` (latch-occupancy length at the last release),
`ncur_n_urgency_releases` / `ncur_n_action_extent_releases` / `ncur_n_releases_total`
(release-event counts), `urgency` / `last_decisiveness_scale` (graded-release
magnitude), `gap_norm_at_entry`, `natural_commit_armed`, `ncur_n_simulation_skips`.

## MECH-094

`tick(simulation_mode=True)` is a no-op (a replay / DMN tick must not abort a
committed motor program). Matches the SD-035 / MECH-279 / MECH-313 / MECH-320 /
MECH-342 pattern.

## Backward compatibility

`use_natural_commit_urgency_release=False` by default -> `agent.natural_commit_urgency`
is None; the arm site and release block are skipped -> bit-identical. No
`e3_selector.py` change (clean separation from the selection-face MECH-448), no
`beta_gate.py` change (reuses the existing `committed_run_length`), no
`claims.yaml` change (PROMOTES NOTHING).

## Phased training

N/A (pure-arithmetic regulator; no learned parameters; no gradient flow).

## What this enables

The sequenced **460i-successor falsifier** (the de-commit retest on this lever,
MECH-445/446) becomes runnable on a regime where weak-natural-commit is the norm
across seeds, so MECH-445 commit-intent and MECH-446 de-commit occupancy drop can
co-occur on the same seeds. **The falsifier is the sequenced next step; it is NOT
queued by this build.**

## Validation

Substrate-readiness contract suite `tests/contracts/test_natural_commit_urgency.py`
(OFF bit-identical / gap-scaled rate load-bearing / action-extent / unarmed
no-op / MECH-094 / config validation / agent release wiring + bounded occupancy /
ON-inert == OFF / arm-site / release-only safety). The 460i-successor behavioural
falsifier is sequenced next.

---

## AMEND: natural-commit LATCH-HOLD (establish the sustained-hold OFF baseline) (2026-06-21)

**Status:** IMPLEMENTED 2026-06-21 (substrate; PROMOTES NOTHING). Routed by the
confirmed `failure_autopsy_V3-EXQ-460i_2026-06-21` (user-adjudicated; Option B
"make the OFF baseline actually sustain"). Pairs with the V3-EXQ-460j gate-3
sustained-hold redesign (the experiment side).

### Why
V3-EXQ-460i self-routed `substrate_not_ready_requeue` at readiness gate 3
(`lever_did_not_shorten_occupancy`): the rung-6 release was correctly **armed**
(`lever_present=true`; `_clone_arm` set the modes + gap-sensitivity) and its
arm-site `note_commit_entry` was reached on NATURAL `result.committed` commits, but
it fired **zero** releases because **the 460h sustained ~2400-step monolithic
natural-commit hold did not reproduce**. The active SD-034 de-commit control-plane
(closure->beta coupling re-toggle, the Leg-B committed-run-scaled refractory, etc.)
fragmented the beta latch to ~1-tick blips **even with the release OFF**
(`ARM_LEVER_OFF` total_beta_elevated ~= beta_release_events, 415/405 seed 43), so
there was **no sustained occupancy to shorten** and the urgency accumulator
(reset per fresh entry, ~0.01-0.02/tick) could not reach `release_bound` over ~1
tick. The release lever is sound; the **regime** was missing.

### The fix (no-op default; bit-identical OFF)
A **latch-HOLD** SEPARATE from (and independent of) the release lever -- so it arms
in the `ARM_LEVER_OFF` baseline too. A fresh NATURAL commit (`result.committed`)
**arms** the hold; while armed AND the committed trajectory persists, the beta
latch is **RE-ASSERTED each tick** (kept elevated against the de-commit churn) so
the natural-commit occupancy **sustains by construction** -- the sustained
reference the rung-6 release shortens and the gate-3 sustained-hold proxy certifies.

The hold **YIELDS to (disarms on) the three PRINCIPLED releases** so it never papers
over them:
- **SD-034 closure de-commit** -- `beta_gate.refractory_remaining > 0` (the latch is
  being held DOWN by the closure); the hold does not fight it, preserving the
  MECH-446 within-arm occupancy-drop DV.
- **MECH-091 genuine-threat urgency interrupt** -- safety; **never** overridden.
- **the rung-6 NaturalCommitUrgencyRelease's own duration release** -- this IS the
  lever shortening the held natural commit (the whole point); the hold disarms so
  the occupancy stays shortened.
It also disarms when the committed trajectory ends or the optional
`natural_commit_latch_hold_max_ticks` safety cap is reached.

Arm/release/coupling semantics are otherwise unchanged: with the hold keeping beta
elevated, `note_commit_entry` fires once (the bistable elevate block is skipped
while already elevated), so the rung-6 urgency accumulates monotonically over the
held duration and fires -- exactly the behaviour 460i lacked.

### Config (REEConfig + from_dims, no-op default)
- `use_natural_commit_latch_hold` (bool, default `False`) -- master, INDEPENDENT of
  `use_natural_commit_urgency_release`. `ARM_LEVER_OFF` baseline = hold ON + release
  OFF -> sustained reference; `ARM_GAP_SCALED` = hold ON + graded urgency ON ->
  sustained then shortened.
- `natural_commit_latch_hold_max_ticks` (int, default `0` = unbounded) -- safety cap
  on re-assert ticks per natural-commit run.

### Data flow
`select_action` arm-site (the bistable natural-commit elevate, `result.committed`):
`_ncl_hold_active = True`. End-of-tick re-assertion (after all release sites, before
the between-tick branch; runs every tick): if armed AND committed trajectory persists
AND `refractory_remaining == 0` AND no MECH-091 / rung-6 release fired this tick AND
under the max-ticks cap -> `beta_gate.elevate()` (keep elevated); else disarm.

### Backward compatibility
`use_natural_commit_latch_hold=False` by default -> `_ncl_hold_active` stays False,
no arm, no re-assert; the per-tick principled-release flags are no-op bool writes.
Bit-identical OFF. Contracts: `tests/contracts/test_natural_commit_latch_hold.py`
(C1 defaults + master-off no-op / C2 arm-site / C3 re-assert-against-churn
load-bearing [hold ON sustains where hold OFF drops] / C4 yield to closure
refractory / C5 yield when the commit ends / C6 max-ticks cap / C7 bit-identical
OFF).

### Validation
The **V3-EXQ-460j** successor (NEW letter; supersedes V3-EXQ-460i) arms the hold in
ALL arms and redesigns gate 3 to a **sustained-hold proxy** (longest consecutive
beta-elevated run + mean per-commit hold length `total_beta_elevated/max(1,
beta_release_events)`) above a floor on `>=2/3` OFF-arm guard seeds, AND requires
`ncur_n_releases_total>0` with a `>= LEVER_OCC_DROP_FRAC` occupancy drop vs OFF on
`ARM_GAP_SCALED`, BEFORE the CO_OCCURRENCE DV is scored. MECH-446/445 stay
candidate / v3_pending / pending_retest_after_substrate until it scores a
contributory result.

---

## Closure-exclusive de-commit eval mode (rung-6 BUILD, 2026-06-22)

`failure_autopsy_V3-EXQ-460j` (user-adjudicated "Park + amend, name the substrate")
established that the latch-hold above NEVER armed on the full closure-coupling
substrate: it arms only on a decisive natural commit (`result.committed`), which
does not form there (`ncl_hold_reassert_total=0`, `max_consecutive_beta_run=1`,
`sd034_n_closure_commit_intent=0`). So **natural-commit and the SD-034 closure
de-commit were NON-DISSOCIABLE** -- there was no sustained natural-commit occupancy
for the de-commit to act on, and no fair test of MECH-445 (commit-intent) / MECH-446
(occupancy-drop) was reachable. A plain yield-clause patch (a "460k") was REFUSED as
targeting the wrong cause (the release/yield logic); the actual cause is the **arm
source** of the occupancy.

### The lever (`closure_exclusive_decommit_eval`, no-op default)
When on, the eval makes beta elevation **closure-exclusive** and re-points the
latch-hold's arm source onto the closure plane:

- **Closure-exclusive elevation** (`agent.py` bistable elevate block): the fragile
  F-driven `result.committed` path is SUPPRESSED from `_commit_for_beta`, which is
  driven ONLY by `_closure_commit_active` (the closure->beta coupling). So the beta
  occupancy is provably closure-formed, not contaminated by a stray natural commit.
- **Closure-coupled hold-arm**: the natural-commit latch-hold ARMS on
  `_closure_commit_active` (a closure-plane commitment forming) in addition to
  `result.committed`, guarded by `beta_gate.refractory_remaining == 0` so it does NOT
  re-arm while an SD-034 closure de-commit is actively holding beta down (the hold
  yields to the de-commit, preserving the MECH-446 occupancy-drop DV). A
  `_ncl_hold_closure_armed_count` readout certifies the eval-mode arm path fired.

The existing re-assertion + yield-on-refractory machinery is UNCHANGED: a closure
commitment forms -> the hold arms + sustains a beta occupancy -> the SD-034 closure
FIRES -> `beta_gate.release()` + refractory -> the hold yields -> the occupancy
drops -> the refractory expires -> the next closure commit re-arms. This dissociates
**occupancy formation** (closure-coupled latch-hold, reliable on all seeds) from
**closure de-commit** (the SD-034 refractory), making MECH-445 commit-intent and
MECH-446 occupancy-drop co-measurable on the same seed -- dissolving the 460h
disjoint-certifier problem.

### Why this is not the refused 460k
460k was a yield-clause narrowing (the release side, which the 460j autopsy proved is
not the blocker). This BUILD changes the ARM SOURCE of the occupancy (the 460j root
cause: "the latch-hold never armed"). It reuses `BetaGate.committed_run_length` and
the existing hold/re-assertion/yield -- no parallel latch module (ARC-106 G2).

### Preconditions + backward compatibility
`closure_exclusive_decommit_eval=True` requires `use_closure_commit_beta_coupling=True`
AND `use_natural_commit_latch_hold=True` (loud `ValueError` at `REEAgent.__init__`).
Default False -> `_commit_for_beta` is the legacy `result.committed OR
_closure_commit_active`, the hold arms only on `result.committed` -> bit-identical.
Contracts: `tests/contracts/test_closure_exclusive_decommit_eval.py` (C1 config
defaults / C2 preconditions raise / C3 closure-coupled-commit arms the hold under
eval [LOAD-BEARING] + legacy does not / C4 natural-commit suppressed under eval / C5
yield to the closure refractory preserved / C6 bit-identical OFF). preflight 8/8;
sibling closure/latch/beta-gate contracts 31/31; the V3-EXQ-460j dry-run reproduces
its eval-OFF baseline signature (`off_occ~4`, `reassert=0`, `sustained_hold=False`);
activation: eval ON arms+re-asserts (`closure_armed=1`, `reassert=8`) where eval OFF
stays 0 (the 460j signature).

### Validation
A 460-lineage successor (NEW letter; supersedes V3-EXQ-460j; queued separately via
`/queue-experiment` AFTER this build lands) runs in the closure-exclusive de-commit
eval mode and gates on: (a) the ARM_LEVER_OFF baseline sustains a natural-commit
occupancy on `>=2/3` seeds, THEN (b) the rung-6 release demonstrably shortens it AND
MECH-445 commit-intent + MECH-446 occupancy-drop co-occur on the same seeds.
MECH-445 / MECH-446 stay candidate / standard / v3_pending /
pending_retest_after_substrate until that successor scores. PROMOTES NOTHING.
