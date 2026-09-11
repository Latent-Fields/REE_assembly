# ARC-059 skip-ordering ablation: readiness verdict

- **Written:** 2026-09-11T12:34:46Z
- **Session:** confident-panini-0cdba7 (chip `chip-20260911-arc059-ablation-readiness`)
- **Question:** have the preconditions gating ARC-059's PRIMARY skip-ordering ablation cleared?
- **Refs at time of writing:** ree-v3 `1bbcf19`, REE_assembly `4fabbfac1f`
- **This is a readiness verdict, not an experiment.** Nothing was queued.

## Headline

**NOT READY overall — but the blocker has moved, and the claim's own text now names the wrong one.**

| Gate | Verdict | One-line basis |
|---|---|---|
| (a) P0 world-forward comparator convergence | **READY** | V3-EXQ-703a PASS 2026-08-08: per-seed R2 0.557 / 0.188 / 0.628, 2/3 clear the 0.20 floor |
| (b) cf_margin achievable contrast band | **READY** | same run: cf_margin recalibrated 0.30 -> 0.15, **3/3** seeds straddle backed/correlational |
| (c) V3 hand-wires the action space | **NOT READY** | `action_dim: int = 4` still a fixed config field; no action-space-discovery code exists |
| (d) *not asked, but load-bearing* | **NOT READY** | stage 2 itself (MECH-278) was relabeled `implementation_phase: v4`, `phase_locked: true` |

**The chip's premise is stale in the user's favour and against it at once.** V3-EXQ-703a —
described in the chip and in ARC-059's own `what_would_answer` as "has not been run" — **was
queued and run on 2026-08-08, PASSed, and is already marked reviewed.** It cleared both of the
MECH-276 feedstock preconditions, i.e. the claim's entire gate (2). But gate (1) is untouched, and
a third obstruction that the claim's two-gate framing does not name has appeared since.

So: **do not queue V3-EXQ-703a — it exists.** And do not read its PASS as unblocking the ablation.

---

## (a) P0 world-forward comparator convergence — READY

**Evidence:** `evidence/experiments/v3_exq_703a_mech276_scientist_attribution_readiness_20260808T191524Z_v3.json`
(run_id `v3_exq_703a_mech276_scientist_attribution_readiness_20260808T191524Z_v3`, outcome **PASS**,
`interpretation.label = mech276_feedstock_readiness_confirmed`, `supersedes: v3_exq_703_...`).
Queued in ree-v3 `d508e91`; snapshot `3b5a7ad`.

| | V3-EXQ-703 (2026-06-23) | V3-EXQ-703a (2026-08-08) |
|---|---|---|
| `world_forward_r2` per seed | -0.688 / -0.057 / +0.581 | **0.5569 / 0.1881 / 0.6276** |
| seeds clearing 0.20 | 1 / 3 | **2 / 3** (`R1_n_pass: 2`, `R1_met: true`) |
| gate-relevant measure | — | `R1_nth_largest_r2 = 0.5569` vs `threshold 0.20` |

**What fixed it:** the P0 objective was made reconstruction-primary (`W_CONTRAST_AUX = 0.1`) with a
real budget (`n_p0_transitions: 1000`, `n_p0_train_steps: 2000`) and the gate moved from run-level
to per-seed. The precondition record states it explicitly: *"P0-trained E2WorldForward
(reconstruction-primary, W_CONTRAST_AUX=0.1) on real action-conditional env transitions"*.

**On the shared-confound question the chip asked.** ARC-059's text says this is *"the same
untrained-P0-world-forward confound as V3-EXQ-701/642, not a missing MECH-276 mechanism."* That
reading holds, and the fix genuinely came from the shared lineage rather than being a MECH-276
-specific patch: the 701 lineage worked the same problem in sequence — 701a `converged_p0`
(2026-06-23), 701b `frozen_probe`, 701c `recononly` (2026-06-29) — and **701c's reconstruction-only
P0 reports `summary.r2_ok: true`**. 703a then adopted that same recon-primary recipe. The three
701 FAILs are not P0-convergence failures: 701a/701b self-route `substrate_not_ready_requeue`, and
701c FAILs on `mel_not_modulated_by_novelty` — a downstream INV-050 question, with its comparator
converged. The 642 lineage likewise ran on to a PASS (642c `validated_clear_v3_pending`, 2026-09-04).

**Caveat, stated because the gate hides it.** Seed 7 lands at **0.1881**, just under the 0.20 floor.
The criterion is ">= 2/3 seeds", so this is a legitimate pass — but it is a 2-of-3 pass with the
third seed a hair short, not a clean sweep. Any future arm that needs all three seeds converged
should re-measure rather than inherit this verdict.

## (b) cf_margin achievable contrast band — READY

**Evidence:** same manifest.

| | V3-EXQ-703 | V3-EXQ-703a |
|---|---|---|
| `cf_margin` | 0.30 (above the whole distribution) | **0.15** (inside it) |
| seeds straddling backed/correlational | 0 / 3 | **3 / 3** (`R2_straddle_per_seed`: 42 T, 7 T, 123 T) |
| `R2_n_ready` (straddle **and** R1-pass) | — | 2, `threshold 2.0`, `R2_met: true` |

The band is not merely non-empty, it is comfortably two-sided. Per-arm, seed 42 gives
`n_counterfactual_backed = 203` against `n_correlational_skipped = 37`; seed 7 gives 43 against 197
— the margin partitions the contrast distribution in *both* directions across seeds, which is
exactly what "achievable contrast band" asks for. Measured `mech276_mean_cf_contrast` 0.166 (seed 42)
and 0.127 (seed 7) bracket the 0.15 margin.

The load-bearing criterion also cleared non-degenerately:
`posterior_discrimination_cf_vs_correlational` passed on 2/2 ready seeds,
`posterior_deltas_ready` first value 0.00203 against the 1e-3 floor, and
`criteria_non_degenerate` records both `discrimination_feedstock_differs` and
`discrimination_aggregator_updated` true.

**Answer to the question as posed** ("*could* it be recalibrated so seeds actually straddle") —
stronger than asked: it already *has* been, and it did.

**One operational note, not a blocker.** The MECH-276 mechanism
(`ree-v3/ree_core/attribution/scientist_attribution_buffer.py`, landed `34afa82` 2026-06-23) is
still default-OFF: `use_scientist_attribution: bool = False` (`ree_core/utils/config.py:5694`). Any
run consuming this feedstock must set the flag ON; 703a did.

## (c) Action space still hand-wired — NOT READY

**Unchanged since MECH-277's own direct search of 2026-08-08. Re-verified against ree-v3 `1bbcf19`:**

- `ree_core/utils/config.py:449`, `:873`, `:2488` — `action_dim: int = 4`, a plain config field.
- `config.py:8404 / :8434 / :8452` — `from_dims` wires `config.e1.action_dim`,
  `config.e2.action_dim` and `config.hippocampal.action_dim` from one caller-supplied argument.
  Specification flows *inward from the experimenter*; nothing flows back.
- `ree_core/environment/causal_grid_world.py:113-115` — `ACTIONS` is a 5-entry class-level literal
  (four moves + no-op). The code comments that the map stays "the canonical 5-move map" and (`:830`)
  that "the class-level ACTIONS dict is never mutated".
- `causal_grid_world.py:1529-1535` — `action_dim` is
  `len(self.ACTIONS) + (1 if self.consummatory_act_enabled else 0)`: a **config flag**, not a
  learning process.
- **No motor-babbling / action-space-discovery code exists** anywhere in `ree_core/` or
  `experiments/`. Every `babbling` hit is the curriculum's "Phase 0", and
  `experiments/infant_curriculum.py:241-245` shows what Phase 0 actually sets —
  `novelty_bonus_weight: 0.5`, `residue_scale_factor: 0.0`,
  `offline_integration_frequency: 10`. Exploration *incentives*. It never touches `action_dim` or
  any action-space structure. MECH-277's note already says this; it is still true.

**The closest thing that landed since, and why it does not count.** MECH-457's consummatory-act
build (substrate_queue, BUILT 2026-07-25) genuinely grows the action space 5 -> 6 by appending a
distinct `CONSUME` action, and actor heads re-key automatically. But it grows it *behind the env
kwarg `consummatory_act_enabled`* — the experimenter decides the agent has a new action, and the
agent discovers nothing. If anything this is the cleanest available demonstration that V3's action
space is an experimenter-set constant: the one mechanism in the tree that changes `action_dim` does
so from a config flag.

**Consequence for the ablation, restated from ARC-059's own precondition.** A literal "withhold
stage 1" manipulation on this substrate can only truncate a phase's episode count while the action
space stays fully specified underneath. That is precisely the degenerate manipulation the claim
pre-registered as *not* a verdict either way.

## (d) Not asked, but it now gates the same ablation — NOT READY

The chip asked three questions framed by ARC-059's June wording. A fourth obstruction has arrived
since, from governance rather than from substrate, and it bears on the same PRIMARY ablation:

**MECH-278 — stage 2, the thing the ablation manipulates — was relabeled
`implementation_phase: v4`, `v3_pending: false`, `phase_locked: true`** (GFLAG-0105 resolution;
claims.yaml as of today). The stated grounds: `object_representation_v4_plan.md:47` records
MECH-278's object definition as *"currently BYPASSED in V3 (z_world engineered pre-split)"*, and
`:142-143` names the developmental-ordering layer explicitly with *"MECH-278's object definition
bypassed in V3"*. MECH-274 (stage 3) is likewise `v4` / `phase_locked`.

So the PRIMARY ablation — "give stage-2 training before stage-1" — has no stage-2 manipulandum in
V3 either. Even a substrate that discovered its action space tomorrow (clearing (c)) would still be
forming object-schemas against an engineered `z_world`, not via interventional action. There is no
`z_world` ablation path in `ree_core/` (searched; nothing).

ARC-059 itself remains `implementation_phase: v3`, `v3_pending: true` while both of the stages its
ablation contrasts are V4-locked. That tension is already on governance's docket — GFLAG-0113's
resolution note records a **NEEDS-DECISION, narrowed to MECH-274**: either split ARC-059 into a
v3-only stages-1-2 claim and a v4 stages-1-3 claim, or retype the `ARC-059 -> MECH-274` edge
(recommendation: the latter). That decision, whichever way it goes, is upstream of this ablation
ever being constructible.

---

## What would have to change

Using the work-graph debt vocabulary:

- **Gate (c)** is `complicated (buildable)`, not `complex (probe-gated)`. Nobody needs to run a
  diagnostic to learn what to do — MECH-277's own note already specifies it: *"a V4 substrate that
  genuinely discovers its action space, or a purpose-built V3 developmental sub-experiment that
  replaces the fixed action_dim config with an online discovery process."* It is buildable with
  known rules; it is simply large, unscoped, and — per that same note — **not on the V3 roadmap**.
  The honest status is execution backlog nobody has costed, not discovery debt.
- **Gate (d)** is a governance decision, not a build: whether ARC-059's v3-testable content is the
  stages-1-2 ordering alone. GFLAG-0113 already owns it.
- **Gates (a) and (b)** need nothing. They are closed by a run that already exists.

**Recommended framing for whoever picks this up:** the interesting question is no longer "is the
MECH-276 feedstock ready" (it is) but "is there a stages-1-2-only ablation worth constructing at
all, given that stage 2's V3 form is an engineered `z_world`". That is the question the September
literature pull made load-bearing, and it is a `/claim-synthesis` or `/governance` question before
it is a `/queue-experiment` one.

## Cross-reference: the 2026-09-11 literature pull

The pull (REE_assembly `127a49fa61`, `evidence/literature/targeted_review_arc_059/`) is net-negative
and its own entries anticipate this verdict. Jacquey et al. 2019 (`supports`) is an architectural
review, and its summary states plainly that counting it as confirmation *"would be double-counting
a commitment rather than testing it"*. Klein-Radukic & Zmyj 2020 (`weakens`, longitudinal N=113
null) and Surian & Caldi 2010 (`weakens`, agent-before-featural individuation at 10 months) are the
empirical entries, and both weaken the claim.

Two design warnings in those entries survive into any future ablation and should be carried forward:

1. **Klein-Radukic & Zmyj** — if the ablation reads stage-1 competence off a coarse proxy and the
   downstream effect off another coarse proxy, the two can fail to correlate even where the
   mechanism is present. A null would then be uninformative rather than falsifying.
2. **Surian & Caldi** — if stage 2 is object-schema formation *via experimental action*, then the
   dynamic cues that mark out agents are already inside stage 2. An ablation withholding stage 2 to
   probe stage 3 would be withholding the very representation it means to probe. As that summary
   puts it, the arm could come back null "for reasons that have nothing to do with the ordering
   being wrong — namely that the agent cue was never actually withheld."

## Staleness found (routed, not fixed here)

ARC-059's `what_would_answer` carries `Evidence status (2026-08-07)` and asserts *"The recommended
re-queue (converged P0 + recalibrated cf_margin, tentatively V3-EXQ-703a) has not been run as of
this draft."* That became false **one day later**. MECH-276's `what_would_answer` similarly still
reads *"Chip already spawned ... to queue the corrected re-run"* as pending. Nothing walks
`what_would_answer`, so neither self-corrected. Routed via `governance_flag.py raise` (see below).

Also noted, not acted on: V3-EXQ-703a carries `claim_ids: []`, so its PASS reaches no claim through
`claim_evidence.v1.json` — ARC-059, MECH-276, MECH-277 and MECH-278 are all absent from that file.
That is normal for a readiness diagnostic and is not a defect; it is recorded here because it
explains why the claim text could go stale while a PASS sat in the evidence tree.
