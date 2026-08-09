---
nav_exclude: true
---

# Thought Intake: Control Plane as a Stopping Signal (STN-Hyperdirect Analogy)

**Raw thought file:** `docs/thoughts/2026-08-09_control_plane_as_stopping_signal_gated_on_f_dominance.md`
**Session:** mel-dose-sweep-inv-051-6b93d7, 2026-08-09
**Status:** processed, claim registered (MECH-488)

---

## Verbatim prompt

> "I have noticed that the ree_assembly machinery has a coordination plane which
> is somewhat similar to the control plane in ree. I noticed that the
> coordination plane's biggest task if often stopping other work elsewhere. I
> wonder how much of the control plane should be used to signal downregulating
> or pausing other parts of ree. An interesting functional parallel which may
> lead to progress with ree. what do you think?"

Follow-up direction across the session: ground the parallel in the actual REE
substrate code and in the neuroscience/computational literature (not just
prose analogy), then check whether the coupling it implies had already been
considered anywhere in the existing planning docs, before writing anything up.

---

## What's New vs. Existing REE Docs (novelty table)

| Existing doc/claim | What it already covers | What this thought adds |
|---|---|---|
| `control_plane_signal_map.md` (MECH-004) | Signal classes S1-S5, knobs K1-K10, functional wiring table | No signal class represents *within-selection contestedness* (a decision-gap/conflict measure). S3 (aversive) and S5 (reality-coherence) are the only "conflict-like" signals reaching K10, and neither is selection-internal. |
| MECH-449/MECH-450 (`e3_selector.py` Go/No-Go + lateral inhibition) | Tonic per-candidate suppression, Mink 1996-style surround inhibition | Correctly identified as mechanism (a) in the BG literature (tonic inhibition + selective disinhibition) -- not new, but the intake is the first place this is explicitly distinguished from mechanism (b) below and cross-referenced to the STN literature. |
| MECH-279/MECH-280 (PAG freeze-gate, K10 hard veto) | A global, harm-threshold-triggered freeze -- functionally mechanism (b) | Confirms MECH-004 already functionally maps PAG to K10, but nothing previously named this as the REE analog of the STN hyperdirect "global stop" circuit, or noted it has exactly one trigger input (harm) with no conflict-based second trigger. |
| SD-037 axis (a)/(b) recalibration plans (`sd_037_axis_a_consumer_input_recalibration_plan.md`, `sd_037_axis_b_sustained_threat_curriculum_plan.md`) | Two routes to get PAG (and BLA/CeA/dACC) to engage ecologically, both by manipulating the SAME z_harm_a-derived input harder | Checked directly (grep): neither plan ever considered a second, independent trigger input for the gate. This is a genuine, confirmed absence, not an interpretation. |
| MECH-439 F-dominance conversion-ceiling cluster (`claim_synthesis_MECH-439_*.md`, `docs/roadmap.md`) | The project's own-acknowledged "live root choke": candidate-pool collapse suppressing behavioural diversity across multiple channels | **New finding, not previously connected**: V3-EXQ-689 (MECH-439's own falsifier) independently confirmed `gap_norm` -- the exact signal this thought's proposed mechanism needs -- is ALSO degenerate (`gap_spread_seeds=0`), and the confirmed autopsy attributes this to F-dominance directly. This ties MECH-439 to the K10/PAG engagement problem (previously tracked separately under SD-037/MECH-280) through a shared mechanism nobody had named: both the STN-analog's would-be input and its would-be receiving gate are casualties of the same root cause. |

**Net assessment:** the coordination-plane analogy itself was a fresh observation with no prior doc; once investigated, it resolved to a real, literature-grounded, and (before this intake) genuinely unclaimed design gap in MECH-004's signal taxonomy -- but one that is currently untestable, for a documented reason connecting two previously-separate blocked threads (SD-037/MECH-280 and MECH-439).

---

## Key formulations

1. **Two distinct BG-literature mechanisms, not one**: (a) tonic inhibition +
   selective disinhibition (Mink 1996; Redgrave, Prescott & Gurney 1999) vs.
   (b) STN hyperdirect-pathway global brake (Aron & Poldrack 2006; Frank 2006
   "Hold your horses"; Wiecki & Frank 2013 combines both in one architecture).
   REE's coordination plane (conflict-triggered, binary, network-wide stop)
   maps onto (b), not (a).
2. **REE already has one of each mechanism, unintegrated**: MECH-449/450
   (mechanism a) and MECH-279 (mechanism b, PAG freeze-gate = K10).
3. **The specific missing wire**: `gap_norm` (computed in
   `_gap_scaled_commit_pick`, `ree-v3/ree_core/predictors/e3_selector.py`) is a
   selection-conflict measure that never leaves E3 -- it is not an S1-S5 signal
   class in MECH-004's taxonomy, and it feeds no control-plane knob.
4. **Confirmed (not hypothesized) shared-root-cause coupling**: both the would-be
   sending signal (`gap_norm`, V3-EXQ-689: `gap_spread_seeds=0`) and the
   would-be receiving mechanism (PAG/K10, MECH-280: `pag_release_count_end=0`
   across 12/12 runs) are independently dead under the MECH-439 F-dominance
   regime, and the project's own confirmed autopsy states the `gap_norm`
   collapse "is itself a manifestation of the F-dominance MECH-439 asserts."
5. **Consequence**: this is a prediction to check once MECH-439 clears
   (do `gap_norm` spread and PAG engagement recover together, confirming the
   shared-cause reading?), not a build to start now.

---

## Affected existing claims

- **MECH-004** (control plane signal map) -- gains a documented gap (no S6
  signal class) and a named candidate claim addressing it (MECH-488). No
  change to MECH-004's own status; its architecture doc gained a new section.
- **MECH-449 / MECH-450** (Go/No-Go + lateral inhibition) -- unaffected in
  status; cited as the mechanism-(a) sibling MECH-488 is explicitly
  complementary to, not a replacement for.
- **MECH-279 / MECH-280** (PAG freeze-gate) -- unaffected in status
  (`substrate_ceiling`/`pending_retest_after_substrate` stands); MECH-488
  depends_on both and inherits their gating.
- **MECH-439** (F-dominance conversion ceiling) -- unaffected in status; this
  intake adds a new *downstream* claim (MECH-488) gated on it, and documents a
  connection between MECH-439 and the previously-separately-tracked SD-037/
  MECH-280 PAG-engagement problem that had not been made explicit before.
- **SD-037** -- unaffected; its axis (a)/(b) plans were read, not amended
  (out of scope for this intake; the finding is that neither considered a
  second trigger, not a proposal to rewrite either plan).

No existing claim's evidence, status, or confidence was altered by this
intake -- purely additive.

---

## Candidate claims

**REGISTERED** (per the thought-intake discipline -- genuinely-new ideas are
registered in the same pass, not left as future-registration prose):

- **MECH-488** -- "A selection-conflict signal (E3's per-candidate decision-gap,
  gap_norm) should feed the control plane as a distinct S6 class, driving K5
  control-allocation escalation and K10 hard-veto threshold as a fast,
  conflict-triggered brake." `status: candidate`,
  `epistemic_category: substrate_conditional`, `implementation_phase: v3`,
  `depends_on: [MECH-004, MECH-449, MECH-279, MECH-280, MECH-439]`,
  `location: docs/architecture/control_plane_signal_map.md#mech-488`.
  Carries an explicit `what_would_answer` with a two-part non-degeneracy
  precondition (MECH-439 clears AND both `gap_norm` spread and PAG engagement
  independently recover) before any experiment against it is meaningful.
  **DO NOT BUILD IN V3 until that precondition holds** -- stated in both the
  claim's `notes` and the architecture doc section.

No other genuinely-new candidate claims were identified in this thought; the
rest of the thought's content (the two-mechanism literature distinction, what
REE already has) is exposition supporting MECH-488, not separate claims.

---

## Next steps

1. **No action required now.** MECH-488 is correctly parked behind MECH-439;
   the right next step is passive -- when MECH-439's falsifier ladder produces
   a PASS (candidate diversity reaching committed action), re-check `gap_norm`
   spread and PAG engagement together as a matter of course, since this claim
   predicts they move together.
2. **Do not queue an experiment against MECH-488** until the `what_would_answer`
   non-degeneracy precondition is independently confirmed (see claim text).
   A run attempted before then would self-route `substrate_not_ready_requeue`,
   same failure shape as V3-EXQ-689 and V3-EXQ-620.
3. **When MECH-439 next reports a status change** (governance cycle or
   `/failure-autopsy` on its current falsifier lineage), a governance session
   should check whether MECH-488's precondition (a)/(b) newly hold, and if so
   route MECH-488 toward `/queue-experiment` -- this is standard MECH-439
   downstream-unblock housekeeping, not a new process.
4. No lit-pull needed -- the citations backing MECH-488 (Mink 1996; Redgrave,
   Prescott & Gurney 1999; Aron & Poldrack 2006; Frank 2006; Wiecki & Frank
   2013) were retrieved and verified via PubMed during this session, not
   assumed from background knowledge.
