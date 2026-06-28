---
title: "SD-v4-loop-segregation: Parallel Segregated Cortico-BG-Thalamic Loops (V3, reappointed from V4 2026-06-24)"
nav_exclude: true
---

# SD-v4-loop-segregation: Parallel Segregated Cortico-BG-Thalamic Loops (V3, reappointed from V4 2026-06-24)

**Substrate / queue id:** `v4_loop_segregation`
**Owning claim:** ARC-110 (this is ARC-110's build design-of-record, NOT a new claim)
**Subject:** `selection.parallel_segregated_loops`
**Status:** IMPLEMENTED 2026-06-27; finer-channel plumbing DEFECT fixed 2026-06-28; **C2 RELEASE (per-named-channel range-preserving routing) LANDED 2026-06-28** -- the limbic loop now carries per-candidate range so C2 (limbic load-bearing) is testable. Validation re-queued as V3-EXQ-707b (supersedes 707/707a). See "VALIDATION + DEFECT 2026-06-28" and "C2 RELEASE LANDED 2026-06-28" below. PROMOTES NOTHING.
**Generation:** V3 — REAPPOINTED V4->V3 2026-06-24 (user-directed; recouped onto the V3 critical path because it attacks the V3 closure blocker MECH-439). Filename / substrate id `v4_loop_segregation` retained for cross-ref stability; the substrate is V3-generation.
**Gate:** V3-EXQ-704 (MECH-451 finer-channel-granularity pre-emption falsifier). Build proceeds only if 704 fails to convert non-motor influence to committed action on the single arena; a 704 PASS means the ceiling was representational compression and this loop build is PRE-EMPTED.
**Registered:** 2026-06-24
**Depends on (built, V3-frozen):** ARC-107, MECH-448, MECH-449, ARC-108, MECH-450
**Couples:** ARC-109 (D1/D2 split, reappointed V3 2026-06-24), MECH-451 (intermediate finer-channel falsifier, V3 — the GATE), MECH-452 (loop-local eligibility traces, reappointed V3 2026-06-24), ARC-111 (context-conditioned weights, already V3)
**Unblocks:** MECH-439, ARC-108, MECH-450, ARC-110
**Escalation source:** `evidence/planning/failure_autopsy_V3-EXQ-700b_2026-06-24.{md,json}` (user-adjudicated 2026-06-24, CONCURRENT with the V3-EXQ-700c null-redesign)

> **Scope discipline (updated 2026-06-24 for the V3 reappointment).** This document now
> specifies a **V3 substrate**, but the build is **deferred and GATED on V3-EXQ-704**
> (MECH-451). As of this writing it has NOT modified `ree-v3/ree_core/` and has NOT queued
> its validation experiment. When the gate clears (704 fails to convert), the build proceeds
> via `/implement-substrate` behind a no-op-default flag (ARC-106 G2 reuse-the-mechanism,
> parallel buffers, byte-identical OFF) and its validation is a **V3 experiment**
> (`architecture_epoch: ree_hybrid_guardrails_v1`, `run_id` ending `_v3`). If 704 PASSes the
> loop build is **pre-empted** and this doc is retired-as-superseded. The concurrent
> V3-EXQ-700c null-redesign (the autopsy's prong B) is a SEPARATE `/queue-experiment` track,
> not part of this substrate.

---

## IMPLEMENTED 2026-06-27 (full scope)

**Gate cleared.** V3-EXQ-704b (MECH-451 finer-channel falsifier) ran the finer channels
correctly (magnitude-match ratio 1.0; channels dissociated 0.0087 + learned 0.00135) and they
did NOT convert (`matched_noise_control_verified_lifting 0/2`). Per the pre-registered fork
this is the **positive-evidence-FOR-ARC-110** outcome (representational compression is NOT the
binding constraint), so the gate OPENS rather than pre-empts. Corroborated by V3-EXQ-706b (first
fully-valid double-gated MECH-314 test, curiosity 0.967 < F-only 1.029 < valid null 1.019).
Cluster autopsy: `evidence/planning/failure_autopsy_704b-706b-conversion-ceiling_2026-06-27.{md,json}`.

> **CORRECTION 2026-06-28 (V3-EXQ-707 autopsy):** the claim above that 704b "ran the finer
> channels correctly" is WRONG. A plumbing defect (see below) meant the NAMED cortical
> channels (ofc/dacc/lpfc/vigour/liking) never reached the selector -- the "channels
> dissociated 0.0087" figure was over the lumped residual/mech341/route 3-way split, NOT the
> named decomposition. 704b's finer-channel leg therefore did not exercise MECH-451's
> hypothesis, and the gate it "cleared" rests (for the MECH-451 leg) on an untested mechanism.
> The curiosity leg (706/706b, MECH-314) is UNAFFECTED -- curiosity rides `residual`, which
> always reached the selector. The escalation to a loop build is not retracted (the curiosity
> leg stands), but the MECH-451 pre-emption test must be RE-RUN post-fix.

## VALIDATION + DEFECT 2026-06-28 (V3-EXQ-707)

V3-EXQ-707 (first ARC-110 validation) returned **non_contributory / substrate_not_ready_requeue**
(PROMOTES NOTHING). `ARM_DROP_LIMBIC` was **byte-identical to `A1_LOOPS` on all 6 seeds**, making
the C2 (limbic loop load-bearing) criterion untestable. Code autopsy found three stacked defects:

1. **DEFECT (FIXED 2026-06-28).** `ree-v3/ree_core/agent.py` built its per-head finer-channel
   dict (`score_bias_channels`) gated on the TOP-LEVEL `self.config.use_finer_channel_gating`,
   which is **never set anywhere in `ree_core`** (always False), while the `e3.select()` consumer
   and the selector both read `config.e3.use_finer_channel_gating`. Net: `score_bias_channels`
   was **always None** reaching the selector -> the MECH-451 named decomposition
   (ofc/dacc/lpfc/vigour/liking/gated_policy) never reached the loop arbitration; only the lumped
   `residual`/`mech341`/`route` did, all mapped to the **default (associative)** loop. The limbic
   loop was **empty in every arm** (its nonzero `pref_range` was a settling-on-zeros artefact), so
   the DROP-LIMBIC ablation (which only remaps ofc/liking/vigour) was a no-op. **Fixed** to read
   `config.e3.use_finer_channel_gating`. Regression guard:
   `ree-v3/tests/test_arc110_loop_segregation.py`.
2. The 707 driver did not enable the limbic-loop input modules
   (`use_ofc_analog` / `use_mech295_liking_bridge` / `use_tonic_vigor`).
3. **DEEPER BLOCKER (the C2 release gate).** Even with Defect 1 fixed AND the modules enabled, the
   named cortical bias heads emit **per-candidate-FLAT output**: the OFC head's INPUT carries real
   per-candidate range (mean 0.028) but its OUTPUT range is **exactly 0.0** (dacc/lpfc/vigour
   likewise; only gated_policy ~7e-4). Under per-loop zscore a flat channel is inert, so the limbic
   loop carries no per-candidate competition and ablating it is a no-op **regardless of module
   enablement** (verified: modules-on `DROP` still == `A1` byte-identical). This is the MECH-191
   phasic-externalisation gap -- the only channels carrying per-candidate range (and thus driving
   the apparent A1>A0 loop dynamics) are the lumped residual/mech341/route (the GAP-A
   `project_channel_range`-routed path), all in the associative loop.

**Consequence.** 707's apparent C1 (loop conversion) dynamics did NOT exercise the cortical
motor/associative/limbic decomposition; the whole validation must be re-run after the release
condition. **C2 is documented ABLATION-INERT / SUBSTRATE-BLOCKED** (not a silent fail;
`load_bearing` stays false so it never gated the ARC-110 verdict).

**RELEASE CONDITION (C2 testable).** Feed per-NAMED-channel range-preserving routed
representations (the `project_channel_range` / GAP-A path that already keeps `route` phasic) into
the segregated loops so the limbic channels carry per-candidate signal -- a substrate build, not a
config flip. Then re-run a 707 successor with the limbic modules enabled and assert the per-tick
committed index differs DROP-on vs DROP-off.

## C2 RELEASE LANDED 2026-06-28 (per-named-channel routing)

The release condition above is **BUILT** (via `/implement-substrate`, behind a no-op-default
flag, byte-identical OFF). New `E3Config` flag **`use_named_channel_routing`**: when on (with
loop segregation + finer-channel gating), each named channel's loop-arbitration term is sourced
from its per-candidate REPRESENTATION routed through the parameter-free, range-preserving
`project_channel_range` projection (the SAME GAP-A path that keeps the lumped `route` channel
phasic) INSTEAD of its flattened bias-head scalar.

| Piece | Flag (E3Config) | Where |
|---|---|---|
| Per-named-channel range-preserving routing into the segregated loops | `use_named_channel_routing` | `agent.select_action` captures each named channel's per-candidate representation (ofc/lpfc -> world-summaries [K,D]; liking -> goal-proximity [K]; vigour -> first-action one-hots [K,A]; dacc -> payoff/effort [K,2]; gated_policy -> summaries [K,D]) -> `project_channel_range` -> `score_bias_channel_routed` kwarg -> `e3_selector.select` builds a `loop_term_override` -> `_segregated_loop_arbitrate` substitutes the routed term for the flat scalar in the **loop accumulation only** |

**Surgical scope.** The override changes ONLY the segregated-loop arbitration's view of the named
channels. The `_lcg_terms` eligibility traces, the authority/shortlist `_modulatory_accum`
recompose, and the F/score commit path are **all unchanged** -- so OFF is bit-identical and ON
leaves the safety envelope (MECH-448/449) and the learned-gating machinery untouched. New
diagnostics `loop_named_channel_routed_ranges` / `loop_limbic_routed_max_range` expose the
per-named-channel routed per-candidate range for the C2 non-degeneracy gate. **Selection-only**
(writes nothing to memory; MECH-094 not engaged). Regression guard:
`ree-v3/tests/test_arc110_loop_segregation.py` (`TestNamedChannelRoutingC2Release` proves
limbic-loop range > 0 + `DROP_LIMBIC != A1` once the routed terms carry range;
`TestRoutedRepsReachSelectorThroughAgent` guards the agent.py capture+route plumbing).

**Validation:** V3-EXQ-707b (`v3_exq_707b_arc110_loop_segregation_c2_release`, supersedes 707a)
enables `use_named_channel_routing` + the limbic input modules on the loop arms and adds a
per-NAMED-channel non-degeneracy precondition (`named_channel_routing_live`: a limbic channel's
routed per-candidate range must clear a substantive floor on a strict-majority of divergent seeds)
evaluated BEFORE C2 is scored -- so the vacuous DROP==A1 self-routes
`substrate_not_ready_requeue`, never a false weakens. PROMOTES NOTHING.

**Built (user chose full scope 2026-06-27):** all four pieces, all behind no-op-default flags,
byte-identical OFF (ARC-106 G2 reuse-the-mechanism, parallel buffers).

| Piece | Flag (E3Config) | Where |
|---|---|---|
| **S1** N>=3 segregated loops (motor / associative / limbic), within-loop competition first, Haber ascending-spiral cross-loop arbitration after, per-loop zscore normalisation (strips F's magnitude advantage) | `use_loop_segregation` | `e3_selector._segregated_loop_arbitrate` (replaces the single-arena within-eligible argmin) |
| **S2** in-layer same-layer committed-class null (magnitude-matched random structure injected at the non-motor loop accumulators -- the layer the loops settle on) | `loop_segregation_noise_on` / `loop_segregation_noise_alpha` | `e3_selector._loop_inlayer_null` |
| **ARC-109** D1/D2 opponent populations with asymmetric DA gain (per loop; dissociates approach-avoidance conflict from indifference) | `use_d1_d2_population_split` / `d1_da_gain` / `d2_da_gain` | `e3_selector._d1_d2_split` |
| **MECH-452** loop-local eligibility traces (credit only the loop whose within-loop winner matched the commit) | `use_loop_local_eligibility_traces` | `e3_selector` eligibility-recording site |

**Safety unchanged.** All loop arbitration runs STRICTLY within the F + MECH-449 Go/No-Go
eligible set, so a non-motor loop can FLIP the within-eligible winner but can NEVER re-admit a
suppressed candidate -- the orthogonal-to-F safety guarantee is inherited from the envelope.

**Non-degeneracy guard (live).** Diagnostics `loop_committed_neq_motor_winner` +
`loop_cross_loop_winner_disagreement` + per-loop `loop_*_pref_range` record whether a non-motor
loop actually flipped the commit / loops disagreed. A "segregated" loop pinned to the motor
winner is a vacuous split -> the validation self-routes `substrate_not_ready_requeue`.

**Phased training: N/A** -- reuses the already-trained valuation heads (no new encoder); all
learned objects (w_chan / W_lat / D1/D2 gains / loop traces) ride the existing ARC-108 LOCAL
three-factor update (not autograd). **MECH-094:** all learning writes inherit the existing
`simulation_mode=False` waking gate; the in-layer null is selection-only (writes nothing to
memory). **Promotes nothing** -- candidate/substrate_conditional claims unchanged pending the
validation run.

---

## Problem

The committed-action-diversity **conversion ceiling** (MECH-439) is the standing V3
bottleneck: the primary harm/goal score **F monopolises ~88-89% of E3 committed-selection
variance** (V3-EXQ-571: 0.886 baseline, 0.894 with the full diversity stack). Modulatory,
within-class, and rule-bias channels cannot convert per-candidate diversity into
*committed*-action diversity while F dominates a single shared selection arena.

The basal-ganglia eligibility constitution (ARC-107) was built to attack this. Its
arithmetic envelope (MECH-448 rank-preserving F->eligibility demotion + MECH-449 Go/No-Go
opponency) lifted the *selection-face* ceiling on the GAP-A foraging substrate. The
**learned-gating** layer was then added: ARC-108 (signed-dopaminergic-RPE learned per-channel
weights `w_chan`) and MECH-450 (a bounded recurrent settling step with learned lateral
inhibition `W_lat`). Both are BUILT and engaged in V3.

The V3-EXQ-700 lineage tested whether learned gating + settling **converts** committed-action
diversity where the arithmetic envelope plateaus. It hit **two binding constraints that a
single foraging arena cannot remove** (700b autopsy, four-layer diagnosis):

1. **Measurement (ROOT).** The matched-noise null perturbs **policy softmax temperature**
   (MECH-313 noise floor), which is **decoupled** from the committed-class-entropy DV by the
   very F-bounded eligibility constitution under test (MECH-448/449 + top-k shortlist +
   Go/No-Go). Temperature and committed-class diversity do not co-vary, so the null is
   **structurally inert** (`noise_verified_lifting=False`; 0/3 divergent-seed lift at
   `NOISE_FLOOR_ALPHA=2.0`, *worse* than 1/3 at 1.0). `NOISE_FLOOR_ALPHA` is the wrong knob,
   and on a single arena it is **un-fixable by tuning** -- a 700c at alpha=3.0 is near-certain
   to fail identically. A valid committed-class null must perturb at the **same layer the
   settling acts on** (the eligibility/settling field), not policy temperature.

2. **Environment (binding constraint).** Biological BG action selection runs over **multiple
   parallel cortico-BG-thalamic loops** (loop segregation; Alexander/DeLong/Strick). A single
   foraging arena collapses every channel into ONE F-dominated competition, so
   **loop-segregated committed diversity is unreachable** -- there is no per-loop degree of
   freedom for the limbic "is this worth committing to" computation to express a value
   different from the motor loop's F-winner.

The settling **signal**, by contrast, is real and **strengthening** across the lineage
(700 seed-42-only +0.25 over A0 -> 700b a2 +0.037 / a3 +0.051 / c3u +0.123 over A0, a
majority of divergent seeds passing C1). A strengthening signal blocked by one broken
instrument on a substrate that structurally cannot host the instrument is the **opposite** of
"circling the same ceiling": it is the escalation argument for the V4 loop-segregation
substrate.

### Failure record (defines acceptance criteria)

| run | NOISE_FLOOR_ALPHA | noise lifts / divergent | settling lift over A0 | reading |
|---|---|---|---|---|
| V3-EXQ-700 | 1.0 | 1/3 | seed-42 only (+0.25, beat noise) | 1 clean seed |
| V3-EXQ-700a | 1.0 | 0/3 | unscoreable (pool collapsed) | -- |
| V3-EXQ-700b | 2.0 | **0/3** | a2 +0.037 / a3 +0.051 / c3u +0.123 | majority of divergent (C1 pass) above an UNVERIFIED null |

Re-derive brake FIRED at 700b (MECH-439 5th / ARC-108 3rd / MECH-450 2nd non_contributory),
REFUSING the naive same-lever alpha-bump requeue. The user-adjudicated V4 escalation proceeds
regardless, so the brake's anti-delay intent is honoured.

**Acceptance target (from the autopsy `failure_record_entry`):** a substrate on which
(a) a **same-layer (eligibility/settling-field) committed-class null verify-lifts above A0 on
a strict majority of divergent seeds** (so the settling-vs-null conversion comparison becomes
valid), and (b) **loop-segregated committed conversion** is achievable -- at least one
non-motor loop converts a previously-F-dominated control function to committed action via a
per-loop ablation the collapsed arena cannot produce.

---

## Solution

Build the V4 full BG-thalamo-cortical loop substrate: replace the single collapsed E3
selection arena with **N parallel segregated cortico-BG-thalamic loops**, plus an
**in-layer committed-class null** that perturbs the layer the settling acts on.

### S1. Segregated loop channels

At minimum three functionally-distinct loops, mirroring the Alexander/DeLong/Strick
parallel-loop organisation (translation target is **functional**, not anatomical mimicry --
ARC-106):

| Loop | Function | V3 collapse it de-collapses |
|---|---|---|
| **Motor** | sensorimotor action selection (the locus where F legitimately dominates) | the F-dominated argmin over the whole candidate set |
| **Associative / cognitive-set** | rule / set-shifting / lateral-PFC rule-evidence | dACC/lPFC bias folded in as an additive `score_bias` term |
| **Limbic / motivational** | "is this worth committing to" value (ventral striatum / OFC) | OFC devaluation folded in as an additive bias, drowned by F |

Each loop owns its **own** eligibility mask + Go/No-Go gate (MECH-449) + recurrent settling
step (MECH-450), running **within-loop competition first**, with cross-loop arbitration
**after** -- rather than collapsing all channels into one shared arena where the dACC/lPFC/OFC
analogs feed in only as additive biases. F can then dominate **only** the motor loop; it
cannot drown the limbic loop's distinct value computation (the ARC-110 s.D
artefact-of-collapse hypothesis).

### S2. In-layer (same-layer) committed-class null

The 700-lineage null is mis-layered. The V4 null is a **magnitude-matched random-structure
perturbation injected at the eligibility/settling-field layer** (the `_modulatory_accum` /
`W_lat` settling field that MECH-450 acts on), gated cleanly behind a `noise_on` switch so
non-noise arms stay byte-identical. Because it perturbs the **same layer** the settling
operates on -- not policy softmax temperature -- it can actually move the committed-class DV,
so `noise_verified_lifting` becomes a meaningful non-vacuity precondition. This is the
substrate-level fix for the measurement ROOT; the V3-EXQ-700c null-redesign prototypes the
same idea on the single arena as a cheap parallel bet.

### S3. Cross-loop arbitration + dopamine spiral coupling (ARC-108 / MECH-452)

Cross-loop arbitration after within-loop competition needs an integration medium. ARC-110's
`depends_on` names **Haber's ascending striato-nigro-striatal dopamine spiral** (limbic ->
associative -> motor) as the coupler: ARC-108 supplies the spiral, ARC-110 supplies the loops
it couples -- co-requisite, not independent. **MECH-452** (loop-local eligibility traces under
a globally-broadcast dopamine signal) is the V4 credit-assignment piece: even with one shared
`delta_t`, the credit traces deciding WHICH loop/channel the signal updates must remain LOCAL
and loop-specific, else a smeared trace makes learned gating appear ineffective even when the
rule is correct.

### S4. D1/D2 population split (ARC-109)

The Go/No-Go scoring SIGN (MECH-449) should de-collapse into two opponent populations with
asymmetric DA gain (D1-LTP / D2-LTD) so high-Go+high-No-Go conflict is dissociable from
low-Go+low-No-Go indifference -- the population substrate the loop-specific CSTC disorder axis
needs (ARC-106 EARNS).

### Sequencing — the cheap V3 rung comes first (MECH-451)

ARC-110's full per-loop build is the expensive bet. **MECH-451** (intermediate
finer-channel-granularity falsifier) is the **cheap V3-tractable rung BEFORE** it: expose the
compressed E3 `score_bias` blend as >=3 separately-learnable finer channels (OFC-devaluation /
dACC-conflict / lateral-PFC rule-evidence / vigour / liking) to the ARC-108 `w_chan` learner,
keeping ONE shared arena. If finer channels convert non-motor influence to committed action,
the conversion ceiling is **representational compression** and the V4 loop build is
pre-empted. If they move their weights but produce no committed-conversion lift, that is
**positive evidence FOR ARC-110** -- compression is not the binding constraint and full
per-loop competition is implicated. MECH-451 should be exhausted (via `/queue-experiment` +
`/implement-substrate` of the finer-channel slice) before committing the V4 loop build.

---

## Architecture Context

This substrate sits in the basal-ganglia missing-piece cluster registered 2026-06-22 from
`evidence/planning/basal_ganglia_assembly_map_2026-06-22.md` (assembly-map A.2 / A.5):

- **ARC-107** (BG selector constitution, V3) -- the umbrella the segregated loops are the
  loop-STRUCTURE for; V3 collapses all loops into one shared commitment interface (s6b).
- **ARC-108** (unified dopamine substrate, V3-built) -- the learned `w_chan` + signed RPE; the
  dopamine spiral that integrates the loops.
- **MECH-450** (recurrent settling step, V3-built) -- the within-loop settling competition each
  segregated loop runs.
- **ARC-109** (D1/D2 split, V4) -- the population substrate the asymmetric DA gain acts on.
- **MECH-451** (intermediate finer-channel falsifier, V3) -- the cheap rung that can pre-empt
  this build.
- **MECH-452** (loop-local eligibility traces, V4) -- the credit-assignment piece for
  multi-loop learning under one dopamine signal.
- **ARC-021 / MECH-069** -- the LEARNING-channel half of segregation (three incommensurable
  error signals); ARC-110 owns the SELECTION-STRUCTURE half. Distinct but co-justifying.
- **MECH-062** -- the asserted-but-collapsed tri-loop gating; ARC-110 owns the missing
  selection-structure segregation MECH-062 names.

Canonical V4 anchors: `v4_spec.md`, `v4_planning_index.md`. This doc should reference them,
not redefine V4 scope.

---

## What This Substrate Enables

- **ARC-110** -- the loop-segregation architectural claim this builds; its pull-forward fork
  (V3-EXQ-700 preconditions-met-no-lift) resolved toward escalation at the 700b autopsy.
- **MECH-439** -- a valid test of whether the conversion ceiling is partly an ARTEFACT of the
  single-arena collapse (F bounded to the motor loop) vs an intrinsic property.
- **ARC-108 / MECH-450** -- a substrate on which learned gating + settling can be tested
  against a **valid in-layer null** and across **segregated loops**, the two conditions the
  single arena structurally denied.
- **ARC-109 / MECH-452** -- the coupled D1/D2 and loop-local-trace pieces, buildable once the
  loops exist.
- The **loop-specific CSTC disorder axis** (loop-localised OCD / motor-loop akinesia /
  avolition-vs-bradykinesia dissociation) -- the ARC-106 psychiatric-failure-mode EARNS target
  that a single collapsed arena cannot model.

---

## Biological Grounding (ARC-106)

Functional translation of the Alexander/DeLong/Strick parallel cortico-BG-thalamic loop
organisation -- segregated motor, associative/cognitive, and limbic/motivational circuits,
each a closed cortex -> striatum -> pallidum/SNr -> thalamus -> cortex loop, integrated by
Haber's ascending dopamine spiral. **Not anatomical mimicry**: each loop analogue carries an
ARC-106 divergence-ledger row + a per-loop ablation falsifier; a loop that, ablated, leaves a
pre-registered conversion metric unchanged is DECORATIVE and dropped (load-bearing-vs-decorative
test). The grounding is already partly present in MECH-335's staggered ventral->dorsal
developmental windows (limbic/value loop opens earliest), which presuppose the parallel-loop
structure.

**Non-degeneracy guard (from ARC-110 `what_would_answer`):** the per-loop channels must carry
live cross-loop variance. A "segregated" loop pinned to the motor loop's winner is a vacuous
split and self-routes `substrate_not_ready_requeue`.

---

## ML/AI Engineering Notes (Layer 7)

- **Mixture-of-experts / modular RL routing** is the closest ML parallel for parallel
  competing channels with a learned arbiter. Use it for the engineering hazard it flags --
  **router collapse / dead experts**: a naive learned cross-loop arbiter tends to route all
  commitment through one loop (here: the motor/F loop), exactly the pathology the substrate
  exists to avoid. Mitigation: the non-degeneracy guard (live cross-loop variance) is a
  load-bearing acceptance gate, and the within-loop-first / arbitrate-after ordering keeps each
  loop's competition alive independent of the arbiter. Do NOT import MoE *architecture*
  (top-k gating networks at scale) -- the REE loops are 3 functionally-specified circuits, not
  learned anonymous experts.
- **Lateral-inhibition settling / Hopfield-style attractor dynamics** (MECH-450, already
  built): bound the recurrent rounds (R~3) and keep `W_lat` a local-plasticity buffer, never an
  autograd target -- the V3 build already does this; the V4 multi-loop version multiplies it
  per loop, so watch total settling cost.
- **Eligibility traces** (MECH-452): standard RL eligibility-trace theory is the engineering
  source for keeping credit loop-local; the REE adaptation is that the trace is per-loop and
  the teaching signal (`delta_t`) is a single shared dopamine broadcast, so the trace -- not the
  signal -- carries the locality.
- The biological grounding (Alexander/DeLong/Strick, Haber) is the architectural authority;
  the ML parallels above are engineering counsel only.

---

## MECH-094

Not applicable at the architectural level. Any V4 experiment built against this substrate that
writes simulation/replay content to memory during non-waking states must carry
`hypothesis_tag=True` (MECH-094), and the learned-gating writes inherit the V3 waking-only gate
(`w_chan` / `W_lat` are not updated on simulation ticks).

---

## Related Claims

ARC-110 (owner), MECH-439, ARC-107, ARC-108, ARC-109, MECH-448, MECH-449, MECH-450, MECH-451,
MECH-452, ARC-111, ARC-021, MECH-069, MECH-062, Q-016, Q-078, ARC-106.
