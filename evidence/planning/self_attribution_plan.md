---
closure_plan:
  id: self_attribution
  title: "Self-Attribution Comparator Loop"
  registered: 2026-05-08
  scope_claims: [SD-013, SD-029, SD-030, SD-031, ARC-033, ARC-058, MECH-256, MECH-257, MECH-258, MECH-260]
  nodes:
    - id: "self_attribution:GAP-1"
      title: "ARC-033 vs ARC-058 path arbitration (forensic 445h read)"
      phase: 1
      status: blocked
      severity: high
      owner_exq: V3-EXQ-445h
      unblocks_claims: [ARC-033, ARC-058, MECH-258, MECH-260]
      depends_on: []
      blocking_external: ["sleep_substrate:GAP-1 Phase 1 PASS", "MECH-269 V_s monostrategy landing", "MECH-307 conjunction architecture"]
      resume_condition: "Same upstream substrate gates as GAP-2. 2026-05-11 forensic read of EXQ-445h surfaced that (a) EXQ-445h dropped the ON_SHARED arm (CONDITIONS=[OFF, ON_INDEPENDENT] only); (b) the earlier three-arm EXQ-445 and EXQ-445b runs that did include ON_SHARED produced bit-identical metrics between ON_INDEPENDENT and ON_SHARED (harm_a_forward_r2 and mean_score_bias_abs floating-point-identical per seed across both arms) under action_class_entropy=0.0 monostrategy. The architectural arbitration is unmeasurable for the same V_s monostrategy reason as GAP-2 -- both forward models converge to predicting a near-degenerate z_harm_a signal. GAP-1 is not a separate gap from GAP-2."
      last_updated: 2026-05-11
    - id: "self_attribution:GAP-2"
      title: "SD-029 / MECH-256 retest under full substrate stack"
      phase: 2
      status: blocked
      severity: high
      owner_exq: TBD
      unblocks_claims: [SD-029, MECH-256, ARC-033, SD-013]
      depends_on: ["sleep_substrate:GAP-1", "goal_pipeline:GAP-1"]
      blocking_external: ["MECH-269 V_s monostrategy landing (satisfier path identified 2026-05-16: ARC-065 SP-CEM, V3-EXQ-567 PASS)"]
      last_updated: 2026-05-16
      resume_condition: "Monostrategy gate now has a concrete satisfier: V3-EXQ-567 PASS (supports ARC-065) -- SP-CEM lifts natural action entropy 0.012->0.497, producing the policy diversity needed for balanced agent-vs-env event distributions (the SD-029 C2/C3 measurement requirement). Retest unblockable once SP-CEM lands in the main agent action path; re-issue SD-029 / MECH-256 retest via /queue-experiment then. See 2026-05-16 decision-log entry."
    - id: "self_attribution:GAP-3"
      title: "MECH-257 dual-function 3-arm ablation re-queue"
      phase: 3
      status: blocked
      severity: medium
      owner_exq: TBD
      unblocks_claims: [MECH-257, MECH-094]
      depends_on: ["self_attribution:GAP-1", "self_attribution:GAP-2"]
      last_updated: 2026-05-08
    - id: "self_attribution:GAP-4"
      title: "Nociceptive-comparator lit-pull (PAG/RVM/ACC)"
      phase: 4
      status: open
      severity: medium
      owner_exq: null
      unblocks_claims: [MECH-256, SD-029]
      depends_on: []
      last_updated: 2026-05-08
    - id: "self_attribution:GAP-5"
      title: "SD-030/SD-031 z_self / z_world materialisation (V4)"
      phase: 5
      status: deferred
      severity: low
      owner_exq: null
      unblocks_claims: [SD-030, SD-031]
      depends_on: []
      last_updated: 2026-05-08
---
# Self-Attribution Comparator Loop Plan

**Registered:** 2026-05-08
**Status:** active
**Scope:** the self-attribution comparator pipeline -- the layer that
turns reafferent latent streams into an agency signal. Covers SD-003
(superseded predecessor), MECH-256 (general single-pass forward-model
comparator, stream-agnostic), SD-029 (concrete z_harm_s instantiation),
MECH-257 (dual-function single-substrate E2: comparator vs evaluator,
controller-gated), SD-013 (interventional training for E2_harm_s),
ARC-033 (independent-per-stream E2_harm_s), ARC-058 (shared
HarmForwardTrunk + per-stream HarmForwardHead, COMPETING with ARC-033),
MECH-258 (precision-weighted pain PE, E2_harm_a forward), MECH-260 (dACC
bias suppression, shared with the dACC bundle), and the V4-deferred
per-stream successors SD-030 (z_self motor-proprioceptive) + SD-031
(z_world causal-footprint).

This plan is the durable resume-point for self-attribution work across
sessions. When work pauses to handle adjacent paths (e.g. sleep
substrate, MECH-307 conjunction architecture, V_s monostrategy), the
deviation is logged in the [Decision log](#decision-log) below with a
resume condition.

---

## One-line framing

> SD-003 cost 28 FAILs over six months. The successor layer (MECH-256
> single-pass comparator with SD-029 as the V3 instantiation) is
> wired end-to-end on z_harm_s, but every empirical attempt to
> distinguish self-caused from externally-caused harm has been
> reclassified non_contributory because the policy is monomodal and
> the substrate-level architectural choice (per-stream vs shared
> trunk) has not been arbitrated.

The comparator scaffolding is in place: ARC-033 forward model passes
C1 (forward_r2 ~0.998, EXQ-330a / EXQ-166e), interventional training
(SD-013) is implemented and supported by EXQ-353, the env-level
balanced-hazard curriculum (SD-029 implementation_note) shipped
2026-04-21, and the dACC bundle (MECH-258 + MECH-260) consumes the
comparator output.

What is missing:

1. The **architectural arbitration** between ARC-033 (independent per-
   stream forward models) and ARC-058 (shared HarmForwardTrunk +
   per-stream heads). V3-EXQ-445 was designed as the three-arm
   ablation for this; its result interpretation is Phase 1 below.
2. **Single-pass comparator validation on z_harm_s under balanced events**
   (SD-029 / MECH-256 C2 + C3). Five consecutive runs (EXQ-433 / 433a /
   433b / 470 / 433d / 433f / 537 / 537a / 523b) reclassified
   non_contributory under V_s monostrategy. Gated on MECH-269 V_s landing
   AND on MECH-204 sleep-substrate Phase 1 (per substrate_queue
   unblocks_claims).
3. **MECH-257 dual-function controller gating** (one E2_x substrate read
   in two modes, comparator vs evaluator, arbitrated by a controller
   signal). EXQ-452 reclassified non_contributory under the same V_s
   substrate gap. Phase 3 below.

The gap is not "more design"; the gap is the architectural arbitration
(Phase 1) and the substrate readiness (Phase 2 + Phase 3) that the
plans of record for sleep and goal pipeline are jointly unblocking.

---

## Source artefacts

Provenance for every gap and decision in this plan:

| Artefact | Role |
|---|---|
| 2026-04-18 SD-003 supersession decision (claims.yaml SD-003 supersession_note) | Closes the two-pass counterfactual era; opens the single-pass comparator era; promotes MECH-256 + SD-029 |
| 2026-04-18 three-pull literature synthesis | Frith 2000 + Shergill 2003 + Blakemore 1998 + Haggard 2017 (single-pass comparator); Mattar & Daw 2018 + Diba & Buzsaki 2007 + Dragoi & Tonegawa 2011 + Kay 2020 + Pezzulo 2014 + Shenhav 2013/2016 (dual-function single-substrate evaluator); Horing & Buchel 2022 (shared-trunk AIC unsigned aversive PE) |
| [docs/architecture/self_attribution_per_stream.md](../../docs/architecture/self_attribution_per_stream.md) | Per-stream topology: SD-029 (V3 z_harm_s), SD-030 (V4 z_self), SD-031 (V4 z_world); MECH-256 stream-agnostic mechanism; MECH-257 dual-function gating |
| [docs/architecture/sd_013_e2_harm_s_interventional_training.md](../../docs/architecture/sd_013_e2_harm_s_interventional_training.md) | Interventional training spec for E2_harm_s |
| [docs/architecture/sd_032_cingulate_integration_substrate.md](../../docs/architecture/sd_032_cingulate_integration_substrate.md) | dACC bundle consumer of MECH-258 precision-weighted PE; MECH-260 bias-suppression spec |
| ree-v3 V3-EXQ-445 / 445a / 445b / 445c / 445h scripts | Three-arm ablation: dACC-OFF vs dACC-ON-independent (ARC-033) vs dACC-ON-shared-trunk (ARC-058) |
| EXQ-433 / 433a / 433b / 470 / 433d / 433f / 537 / 537a / 523b governance reads (SD-029 evidence_quality_note) | Five consecutive non_contributory under V_s monostrategy; substrate-ceiling pattern |
| EXQ-452 governance read (MECH-257 evidence_quality_note) | Dual-function gated-readout cannot resolve under monomodal policy |
| substrate_queue.json MECH-204 entry unblocks_claims `[Q-041, Q-042, INV-049, SD-029, MECH-256, MECH-111, SD-049]` | Sleep-substrate Phase 1 is the upstream gate for SD-029 / MECH-256 retest |

---

## Existing substrate (do not duplicate)

Wired and behaving correctly:

| Component | Location | Status |
|---|---|---|
| ARC-033 E2_harm_s forward model | `ree-v3/ree_core/predictors/e2_harm_s.py` (`E2HarmSForward`) | C1 forward_r2 ~0.998 confirmed (EXQ-330a, EXQ-166e PASS 6/6) |
| SD-013 interventional training for E2_harm_s | `ree-v3/ree_core/predictors/e2_harm_s.py` `compute_interventional_loss` | EXQ-353 PASS supports; provisional |
| MECH-258 E2_harm_a forward model + precision-weighting | `ree-v3/ree_core/predictors/e2_harm_a.py` (`E2HarmAForward`); `ree_core/cingulate/dacc.py` PE bundle | EXQ-445h C1 wins 2/3 seeds; first clean supports |
| MECH-260 dACC bias-suppression FIFO | `ree-v3/ree_core/cingulate/dacc.py` `record_action`/`forward` suppression channel | EXQ-445h C3 wins 3/3 seeds |
| ARC-058 shared HarmForwardTrunk + HarmForwardHead | `ree-v3/ree_core/latent/stack.py` (`HarmForwardTrunk`, `HarmForwardHead`); E2_harm_a/E2_harm_s constructor switch via `shared_trunk` | scaffolded; arbitration via V3-EXQ-445 three-arm ablation pending |
| SD-029 balanced-hazard curriculum | ree-v3 CausalGridWorldV2 `scheduled_external_hazard_*` knobs (2026-04-21); info-dict `external_hazard_event_count` | env substrate landed; behavioural test blocked by V_s monostrategy |
| Comparator residual readout | `ree-v3/ree_core/agent.py` self-attribution path consuming E2_harm_s reafferent residual | end-to-end wired; awaits balanced events |

---

## Gap inventory

Five gaps, ordered by leverage. Each is the basis for one row of the
[Status table](#status-table) below.

| Gap | Subject | Severity | Unblocks |
|---|---|---|---|
| **GAP-1** | ARC-033 vs ARC-058 architectural arbitration unresolved (independent-per-stream vs shared-trunk + heads); only V3-EXQ-445h has produced a clean partial read | load-bearing | ARC-033 retire-or-confirm; ARC-058 retire-or-promote; MECH-257 single-substrate philosophy |
| **GAP-2** | SD-029 single-pass C2/C3 unmeasurable while policy is monomodal (5 consecutive non_contributory: EXQ-433/433a/433b/470/433d/433f/537/537a/523b) | high | MECH-256 empirical promotion; SD-029 candidate -> provisional; INV-049/Q-041/Q-042 confidence on the comparator side |
| **GAP-3** | MECH-257 dual-function controller-gated readout untestable under monomodal policy (EXQ-452 non_contributory) | high | MECH-257 falsification one way or the other; arbitrates "two substrates per stream" parameter doubling |
| **GAP-4** | Q1: nociceptive-transfer caveat -- comparator literature evidences mechanism on sensorimotor / tactile / force streams; extension to nociceptive streams plausible (PAG/RVM descending modulation shares efference-copy structure) but not directly demonstrated; main mapping risk | medium | architectural confidence in MECH-256 generalisation across reafferent streams |
| **GAP-5** | SD-030 (z_self) + SD-031 (z_world) are V4-deferred placeholders; per-stream topology is not testable until z_self / z_world become first-class latents with their own forward models | low (V4 deferred) | per-stream topology completeness; not in V3 scope |

---

## Sequenced plan

Five phases. Each phase is small, verifiable, and unblocks at least one
downstream claim. Phases are ordered by what each unblocks. Where work
depends on adjacent non-self-attribution paths (sleep substrate Phase 1,
goal pipeline dACC bundle, V_s monostrategy fix), that is called out
inline and tracked as the upstream gate in the
[Status table](#status-table).

### Phase 1: V3-EXQ-445 three-arm ablation result interpretation (GAP-1)

**Status (2026-05-11): blocked on same substrate gates as Phase 2.**
Forensic read of EXQ-445h surfaced that the arbitration data does not
exist in any 445-iteration, and the bit-identical pattern in the
iterations that did include ON_SHARED is the same V_s monostrategy
substrate ceiling that has been reclassifying the SD-029 cohort
non_contributory. See [Decision log -- 2026-05-11](#2026-05-11-gap-1-monostrategy-inversion)
below.

ARC-033 and ARC-058 are registered as competing architectural
commitments. V3-EXQ-445 was designed as the three-arm ablation that
arbitrates them: dACC-OFF (baseline) vs dACC-ON-independent (ARC-033
path) vs dACC-ON-shared-trunk (ARC-058 path).

**Two findings invert the original Phase 1 plan:**

1. EXQ-445h is two-arm only -- `CONDITIONS = ["OFF", "ON_INDEPENDENT"]`
   ([v3_exq_445h_sd032b_dacc_reef.py:83](../../../ree-v3/experiments/v3_exq_445h_sd032b_dacc_reef.py)).
   The ARC-058 arm was silently dropped after EXQ-445b. EXQ-445a/c/d/f/g/h
   all run `use_shared_harm_trunk=False` hard-coded. The "latest in the
   series" that the plan keyed on has no shared-trunk data.
2. The earlier three-arm runs (EXQ-445 + EXQ-445b two timestamps) show
   floating-point-identical metrics between ON_INDEPENDENT and ON_SHARED
   per seed:
   - seed=42: harm_a_forward_r2=0.9371525719237495,
     mean_score_bias_abs=3374526.2593920277 (both arms)
   - seed=7:  harm_a_forward_r2=0.918056702809114,
     mean_score_bias_abs=954306.9917550903 (both arms)
   - seed=13: harm_a_forward_r2=0.8406720867479271,
     mean_score_bias_abs=86130.61802364363 (both arms)

   The two architectures (ARC-033 path uses `ResidualHarmForward`;
   ARC-058 path uses `HarmForwardTrunk + HarmForwardHead`) are genuinely
   different module trees with different parameter counts. The only way
   to produce floating-point-identical training metrics is for the
   architectural distinction to not actually exercise -- which under
   `action_class_entropy=0.0` across every seed in every condition is
   exactly what monostrategy predicts: trajectories are deterministic
   given seed alone, both forward models consume the same near-degenerate
   z_harm_a stream, and both trivially fit it. The original EXQ-445
   pass-criteria `c4_arc033_vs_arc058_diagnostic` actually recorded
   `mean_r2_independent == mean_r2_shared == 0.8986271204935968` exactly;
   the "winner_suggested_by_forward_r2: ARC-058_shared" tag was
   meaningless because the test was non-discriminative.

GAP-1 is therefore not a separate gap from GAP-2. The architectural
arbitration requires balanced agent-vs-env event distributions for the
two architectures to produce different forward_r2 readouts. Under V_s
monostrategy that distribution does not exist, and the bit-identicality
is the substrate-ceiling signature.

**Revised Phase 1 deliverables (post-2026-05-11):**

1. **Reclassify EXQ-445 + EXQ-445b ARC-033/ARC-058 entries**:
   evidence_direction_per_claim for ARC-033 and ARC-058 -> non_contributory
   with evidence_quality_note pointing at action_class_entropy=0.0 +
   bit-identical-across-arms signature. MECH-258 / MECH-260 / SD-032b
   reads are kept as recorded (those criteria are about within-arm
   behaviour, not cross-arm arbitration) but inherit the same
   substrate-ceiling caveat -- they reflect what an untrained-policy
   monostrategy run can fit, not what the dACC bundle does when the
   policy actually exercises both event classes.
2. **Resume condition (same as GAP-2)**: when sleep_substrate_plan Phase 1
   PASSes AND MECH-269 V_s lands AND MECH-307 conjunction architecture
   lands, queue a fresh three-arm ablation (NOT a 445-letter iteration --
   the 445h template is two-arm) on the full substrate stack. Acceptance
   criteria identical to Phase 2 (balanced events; C2 partial attenuation;
   C3 SNR) PLUS the cross-arm comparator: shared-trunk forward_r2 must
   differ from independent-per-stream forward_r2 by more than the
   per-seed run-to-run noise floor to be discriminative.
3. **Caveat (preserved from original plan)**: SD-032b does_not_support
   running may stem from substrate gaps not yet inventoried
   (previous-valence-on-unexpected, MECH-307 conjunction architecture,
   sleep substrate). Per the 2026-05-08 governance note in MECH-260
   evidence_quality_note: do NOT advance toward demote until the
   candidate-gap inventory broadens.

Phase 1 originally claimed to be **not gated** on Phase 2 / Phase 3
substrate work because it read a result that had already been collected.
The 2026-05-11 finding inverts that: the result that was collected does
not actually contain arbitration data, and the substrate gaps that block
Phase 2 also block Phase 1.

Acceptance (updated): ARC-033 + ARC-058 entries in claims.yaml +
substrate_queue retain their candidate status with evidence_quality_note
recording the substrate-ceiling finding. The architectural verdict is
deferred to the same resume window as Phase 2.

### Phase 2: MECH-256 single-pass comparator validation under balanced events (GAP-2)

The C2 + C3 measurements that SD-029 + MECH-256 need (residual
attenuation on self-caused vs externally-caused harm + approach-event
SNR) cannot be made while the policy is monomodal. EXQ-433 / 433a /
433b / 470 / 433d / 433f / 537 / 537a / 523b form a five-instance
substrate-ceiling pattern: in each, the C0 trials-sufficient gate fails
because the agent runs in either "exploit only" or "avoid only" mode
and produces near-zero counts on the opposite class. EXQ-433f
(2026-05-08 diagnose-errors) added a fifth confirmation that even
SD-050 reef enrichment (`reef_enabled=True`, `n_reef_patches=3`,
`hazard_food_attraction=0.7`) does not break monostrategy at 8x8 scale.

**Upstream gates** (from substrate_queue MECH-204 unblocks_claims +
governance 2026-04-22 hold):

- **MECH-204 sleep-substrate Phase 1** (precision recalibration consumer
  in [sleep_substrate_plan.md](sleep_substrate_plan.md) Phase 1).
  Sleep_substrate_plan Phase 4 (MECH-273 real replay-derived training
  targets) writes back to E2_harm_s using SD-003 / SD-029 causal_sig as
  evidence -- the self-attribution loop is the **consumer** of the sleep
  loop's writeback. The relationship is bidirectional: sleep needs SD-029
  to train its writeback target, and SD-029 needs sleep recalibration to
  break the V_s monostrategy that makes its events unbalanced.
- **MECH-269 V_s landing** (waking-side V_s invalidation runtime
  Phase 1-3 already landed 2026-04-22 -- 2026-04-24; what is missing is
  the V_s-driven action selection coupling that produces balanced
  agent-vs-environment event distributions).
- **MECH-307 anticipatory-affect conjunction architecture** (added to
  substrate_queue priority=1 2026-05-08; gates the goal-pipeline
  commit-chain that, when fixed, may break monostrategy upstream of V_s).

Deliverables:

1. **Resume condition.** When sleep_substrate_plan Phase 1 PASS landed
   (post-REM `_running_variance` measurably moved toward zero-point
   reference in ON arm) AND MECH-269 V_s landed AND MECH-307 conjunction
   architecture lands, re-queue an SD-029 / MECH-256 retest with the
   full substrate stack on (`use_per_stream_vs=True`,
   `use_anchor_sets=True`, `use_sd039_anchor_payload=True`,
   `use_sleep_loop=True`, sleep recalibration ON,
   `scheduled_external_hazard_enabled=True`).
2. **Acceptance per retest:** C0 trials-sufficient gate PASS on >=3/4
   seeds (>=20 agent_caused_hazard trials AND >=20 env_caused_hazard
   trials per seed); C1 forward_r2 >= 0.9; C2 residual partially
   attenuated for self-caused vs externally-caused (Shergill partial-
   attenuation pattern, **not binary**); C3 approach-event SNR >
   threshold.
3. **Diagnostic non_contributory bookkeeping.** When a retest still
   produces monostrategy events, the verdict is `non_contributory` per
   the governance pattern, not `weakens`. Distinguishes substrate-
   ceiling from mechanism-falsification.

Phase 2 is gated on three upstream substrates landing. The plan-doc
records the gate explicitly so a future session does not re-queue an
SD-029 retest before sleep / V_s / MECH-307 close.

### Phase 3: MECH-257 dual-function controller-gated readout (GAP-3)

MECH-257 claims that E2_harm_s (and E2_harm_a, and any E2_x) is a
single substrate read in two modes -- retrospective comparator
(attribution) and prospective rollout-scoring (evaluation) -- arbitrated
by a controller signal (V3 candidate: commitment boundary state /
hypothesis tag MECH-094; V4 candidate: dACC EVC signal following
Shenhav 2013/2016, or heartbeat-phase gating per ARC-023). The
falsifiable branch: if a single substrate cannot support both modes
(training for evaluator degrades comparator performance or vice versa),
MECH-257 is refuted and the architecture must split into two substrates
per stream, doubling parameter count.

EXQ-452 (governance 2026-04-22) was reclassified non_contributory: dual-
function gated-readout test cannot resolve under V_s monostrategy because
both reads operate over the same locked policy and mode-specific
performance differences cannot manifest.

**Upstream gates:** Phase 2 PASS (need balanced events for both modes
to be exercised) + Phase 1 verdict (need to know whether E2_x is one
substrate or two before testing single-substrate vs split-substrate).

Deliverables:

1. **Re-queue MECH-257 dual-function ablation** after Phase 2 PASS.
   Three arms: (a) comparator-only training, (b) evaluator-only training,
   (c) joint training. Measure mode-specific performance under each
   training regime.
2. **Acceptance:** if joint training produces comparable per-mode
   performance to mode-split baselines, MECH-257 supports (single
   substrate sufficient). If joint training degrades performance >X%
   on either mode, MECH-257 weakens (split required).
3. **Controller signal selection.** V3 default: hypothesis tag MECH-094
   gates which mode is active. Phase 3b (deferred): if V4 controller
   candidates (dACC EVC, heartbeat-phase gating) become available,
   re-test the controller arbitration.

### Phase 4: nociceptive-transfer arbitration (GAP-4) -- Q1

Open question Q1 (registered in this plan): can the comparator
mechanism, evidenced biologically on sensorimotor / tactile / force /
oculomotor / electrosensory streams, generalise to a nociceptive
stream? Plausible (descending pain modulation in PAG/RVM shares the
efference-copy structure; ACC/insula pain self-vs-other attribution
in Frith 2000 and the descending pain modulation literature) but not
directly demonstrated in the four canonical comparator papers
(Frith 2000, Shergill 2003, Blakemore 1998, Haggard 2017). This is
the main mapping risk for SD-029 specifically.

Deliverables:

1. **Targeted lit-pull** on nociceptive comparator / efference-copy
   evidence. Anchor papers: Fields 2004 (PAG/RVM descending
   modulation), Wager 2013 (anticipatory pain modulation), Seymour
   2019 (pain as precision-weighted control signal), descending pain
   modulation reviews 2020-2025. Open question: does the nociceptive
   stream have a comparator-class circuit, or does it use a different
   mechanism (e.g. precision gating without efference-copy
   cancellation)?
2. **Architectural read.** If lit converges on comparator-class
   nociceptive circuit, MECH-256 generalisation to z_harm_s is
   confirmed and SD-029 inherits MECH-256's lit_conf. If lit
   diverges (precision-only, no efference cancellation), SD-029 needs
   its own design doc separate from MECH-256 and the comparator
   metaphor on z_harm_s is over-specified.

Phase 4 is **not gated** on substrate work -- it is a literature pull
that can land in parallel with Phase 1 / Phase 2.

### Phase 5: SD-030 + SD-031 V4 placeholder maintenance (GAP-5)

SD-030 (z_self motor-proprioceptive comparator) and SD-031 (z_world
causal-footprint comparator) are V4-deferred. No V3 evidence expected.
Phase 5 is **passive** -- the plan-doc tracks them for completeness so
that V4 work resumes from a known state.

Deliverables (V4 only): when z_self and z_world become first-class
latents with their own forward models, instantiate MECH-256 on each
and run per-stream C1/C2/C3 acceptance. Until then, SD-030 / SD-031
remain candidate / V4-deferred in claims.yaml.

GAP-5 is intentionally NOT in the V3 scope of this plan.

---

## Status table

The resume primitive. Updated every session that touches self-
attribution work. See [Resume ritual](#resume-ritual) below.

| Gap | Phase | Status | Blocking on | Next action | Owner-EXQ | Last updated |
|---|---|---|---|---|---|---|
| GAP-1 | 1 | blocked | sleep_substrate Phase 1 PASS + MECH-269 V_s landing + MECH-307 conjunction architecture (same gates as GAP-2) | After upstream gates close, queue a fresh three-arm ablation (NOT 445h -- that script is two-arm) that exercises ARC-033 vs ARC-058 under balanced events. Forensic read 2026-05-11 surfaced substrate-ceiling, not arbitration data -- see Decision log | TBD (post-substrate-gates) | 2026-05-11 |
| GAP-2 | 2 | blocked | sleep_substrate_plan Phase 1 PASS + MECH-269 V_s landing + MECH-307 conjunction architecture | After all three upstream gates close, re-queue SD-029 / MECH-256 retest with full substrate stack | TBD (post-substrate-gates) | 2026-05-08 |
| GAP-3 | 3 | blocked | Phase 2 PASS + Phase 1 verdict | After Phase 2 PASS, re-queue MECH-257 dual-function 3-arm ablation | re-queue of EXQ-452 (TBD) | 2026-05-08 |
| GAP-4 | 4 | open | nothing | Schedule nociceptive-comparator lit-pull (PAG/RVM descending modulation, ACC pain attribution) | n/a (lit-pull) | 2026-05-08 |
| GAP-5 | 5 | deferred V4 | z_self / z_world materialisation in V4 | none in V3 | n/a | 2026-05-08 |

Status values: `open`, `in-progress`, `blocked`, `paused`, `done`, `deferred`.
A `paused` row carries a resume condition in the [Decision log](#decision-log).

---

## Cross-references

| Plan node | substrate_queue.json sd_id | claims.yaml claim | Design doc |
|---|---|---|---|
| GAP-1 / Phase 1 | (new design_doc set on MECH-256, MECH-257, MECH-258, ARC-058, SD-029) | ARC-033, ARC-058, MECH-258, MECH-260 | self_attribution_per_stream.md, sd_032_cingulate_integration_substrate.md |
| GAP-2 / Phase 2 | SD-029 (priority=1, status=implemented), MECH-256 (new), MECH-204 (priority=1; **sleep upstream gate**) | SD-029, MECH-256, ARC-033, SD-013 | self_attribution_per_stream.md |
| GAP-3 / Phase 3 | MECH-257 (new) | MECH-257, MECH-094 | self_attribution_per_stream.md, control_plane_heartbeat.md |
| GAP-4 / Phase 4 | n/a (lit-pull only) | MECH-256, SD-029 | self_attribution_per_stream.md |
| GAP-5 / Phase 5 | SD-030 (priority=3, V4), SD-031 (priority=3, V4) | SD-030, SD-031 | sd_030_e2_self_forward_model.md, sd_031_e2_world_forward_model.md |

### Cross-plan boundaries

This plan **consumes** writeback from
[sleep_substrate_plan.md](sleep_substrate_plan.md): Phase 4 of the sleep
plan (MECH-273 real replay-derived training targets) constructs training
tuples `(z_harm_s, a, posterior-corrected residual)` from the cycle's
routed events; the `self`-domain posterior uses **SD-003 / SD-029
causal_sig as evidence**. The self-attribution comparator output is what
makes MECH-273 informative on the self domain. Without a working
comparator (this plan's Phase 1 + Phase 2), MECH-273 writes synthetic
batches and its empirical promotion is impossible.

This plan **provides input to** the goal pipeline (cross-link to
`goal_pipeline_plan.md` -- not yet written; expected sibling plan-of-
record). The dACC bundle (MECH-258 precision-weighted PE channel +
MECH-260 bias suppression channel) consumes the comparator output as
its `pe` field; the comparator's quality bounds the goal pipeline's
commit quality. When the comparator residual is uninformative (Phase 2
blocked), `dACC.pe` is dominated by raw forward-model loss rather than
agency signal, and the goal pipeline's commit-chain decisions are
correspondingly noisy.

The SD-029 single-pass comparator + Q-041 unified threshold supervisor
are gated on MECH-204 (sleep_substrate_plan Phase 1) per substrate_queue
unblocks_claims -- this is reflected explicitly in the
[Status table](#status-table) GAP-2 row.

---

## Decision log

Append-only. Every architectural choice + every deviation pause / resume.

### 2026-05-16 - Closure-map reconciliation: SD-029 / MECH-256 retest monostrategy gate has a validated substrate fix (ARC-065 SP-CEM)

Staleness pass (status tables 5-8 days behind runner, now V3-EXQ-581).

GAP-2 (SD-029 / MECH-256 retest) carries
`blocking_external: ["MECH-269 V_s monostrategy landing"]`; GAP-1 and
GAP-3 inherit the same gate (GAP-1 resume_condition: "Same upstream
substrate gates as GAP-2"). Reconciled evidence:
- V3-EXQ-550 FAIL (supports MECH-269): confirms the monostrategy
  reading at no-training depth -- a monomodal policy cannot generate the
  balanced agent-vs-env event distributions the SD-029 C2/C3 metrics
  need.
- V3-EXQ-567 PASS (supports ARC-065): support-preserving CEM lifts
  natural action entropy 0.012 -> 0.497 and candidate support
  1.007 -> 2.810 -- the validated mechanism that produces the policy
  diversity the retest requires.

The "MECH-269 V_s monostrategy landing" blocking_external now has a
concrete satisfier path (ARC-065 SP-CEM, V3-EXQ-567). GAP-1/2/3 stay
`blocked` (retest not yet run) but are unblockable once SP-CEM lands in
the main agent path; GAP-2 blocking_external + last_updated updated
accordingly.

### 2026-05-11 - GAP-1 monostrategy inversion {#2026-05-11-gap-1-monostrategy-inversion}

Phase 1 forensic read of V3-EXQ-445h, performed today, surfaced that the
arbitration data the plan keyed on does not exist. Two findings:

1. **EXQ-445h is two-arm only.** Script line 83 of
   [v3_exq_445h_sd032b_dacc_reef.py](../../../ree-v3/experiments/v3_exq_445h_sd032b_dacc_reef.py)
   sets `CONDITIONS = ["OFF", "ON_INDEPENDENT"]`. The ON_SHARED arm was
   silently dropped after the EXQ-445b iteration; EXQ-445a/c/d/f/g/h all
   run `use_shared_harm_trunk=False` hard-coded. The 2026-05-08 plan-
   registration step referred to "EXQ-445h forensic read" because the
   manifest's c1_mech258 / c2_sd032b / c3_mech260 grid reads as if it had
   the data; the underlying script does not.
2. **EXQ-445 and EXQ-445b (which retained the three-arm shape) show
   floating-point-identical metrics across ON_INDEPENDENT and ON_SHARED**
   per seed (harm_a_forward_r2 and mean_score_bias_abs both bit-identical
   across the two architectural arms, varying only across seeds). Under
   `action_class_entropy=0.0` in every condition for every seed, the
   policy is monomodal -- the trajectory through the env is deterministic
   given seed alone, so both forward-model architectures consume the same
   z_harm_a stream and trivially fit a near-degenerate target. The
   architectural distinction between `ResidualHarmForward` (ARC-033) and
   `HarmForwardTrunk + HarmForwardHead` (ARC-058) is unmeasurable because
   the input distribution does not exercise it. The EXQ-445
   `c4_arc033_vs_arc058_diagnostic` field even records this:
   `mean_r2_independent == mean_r2_shared == 0.8986271204935968` exactly;
   the "winner_suggested_by_forward_r2: ARC-058_shared" tag is
   meaningless because the test is non-discriminative.

Conclusion: **GAP-1 is the same V_s monostrategy substrate ceiling that
blocks GAP-2.** The 9 non_contributory reclassifications already logged
for SD-029 (EXQ-433 / 433a / 433b / 470 / 433d / 433f / 537 / 537a /
523b) are the same blocker -- EXQ-445 and EXQ-445b just didn't get
reclassified the same way at original-review time because c1_mech258
PASSed at the same trivial-fit signature.

Actions taken this session:
- GAP-1 status `open` -> `blocked` with same upstream gates as GAP-2
  (sleep_substrate Phase 1 PASS + MECH-269 V_s landing + MECH-307
  conjunction architecture).
- EXQ-445 and EXQ-445b (two timestamped runs) manifests updated:
  evidence_direction_per_claim for ARC-033 and ARC-058 -> non_contributory
  with evidence_quality_note pointing at the bit-identicality +
  action_class_entropy=0.0 signature. MECH-258 / MECH-260 / SD-032b reads
  preserved (within-arm criteria) but inherit the substrate-ceiling
  caveat.
- Phase 1 narrative section updated to record the inversion. The "not
  gated on Phase 2/3" claim is removed; the revised acceptance is to
  queue a fresh three-arm ablation (NOT a 445-letter iteration) post-
  substrate-gates with both balanced-events acceptance AND a cross-arm
  discriminability floor.
- No new EXQ queued. Queueing EXQ-445i would burn a runner session on
  the same blocker.

### 2026-05-08 - Plan registered

Plan created in conversation with user. SD-003 supersession history
(2026-04-18) treated as background context; this plan covers the
successor layer (MECH-256 + SD-029 + MECH-257) and its competing
architectural commitments (ARC-033 vs ARC-058). Five gaps surfaced and
sequenced into five phases. Cross-plan boundaries with
sleep_substrate_plan (consumer of writeback) and goal_pipeline_plan
(provider of dACC PE input) made explicit.

### 2026-04-18 - SD-003 superseded by MECH-256 + SD-029

Recorded in claims.yaml SD-003 supersession_note. Reasons: (1) 28 FAILs
across V2+V3 iterations on the two-pass counterfactual architecture
since z_world -> z_harm_s stream migration; (2) biological precedent
gap -- Frith 2000, Shergill 2003, Blakemore 1998 evidence single-pass
comparator (`residual = observed - E2(prev_state, a_actual)`), not
two-pass counterfactual; (3) three-pull lit synthesis 2026-04-18
converged on single-pass comparator with one E2 substrate read in two
modes (MECH-257). Existing evidence chain (EXQ-030b/115/166a/195/353/431)
remains in the historical record; new V3 evidence accrues to SD-029.
ARC-033 forward model component carried forward unchanged.

### 2026-04-19 - ARC-058 registered as competing claim against ARC-033

Horing & Buchel 2022 (J Neurosci) "modality-general neural code for
aversive stimulus representation in the anterior insula" is the
biological grounding: anterior insula encodes unsigned aversive PE
shared across pain, loud noise, and other aversive modalities; dorsal
posterior insula carries modality-specific signed PE. ARC-058 holds
that a SHARED HarmForwardTrunk encodes the unsigned modality-
independent substrate while stream-specific HarmForwardHeads produce
signed per-modality readouts; ARC-033 holds independent per-stream
forward models. Falsifiable via V3-EXQ-445 three-arm ablation. MECH-257
(single-substrate dual-function) is the sibling philosophical claim.

### 2026-04-22 - SD-029 retest cohort reclassified non_contributory under V_s monostrategy

EXQ-433/433a/433b/470 reclassified non_contributory (governance
2026-04-22). Substrate gap is V_s monostrategy: monomodal policy cannot
generate balanced agent-vs-env event distributions for C2/C3
measurement. Hold candidate pending MECH-269 V_s landing.

### 2026-04-27 - EXQ-433d adds fourth confirmation

V3-EXQ-433d FAIL (2026-04-27): 4-seed run with EXQ-479 calibrated
curriculum. agent_caused_hazard=0/0/0/0 in all 4 seeds. Same monomodal
phenotype. Reclassified non_contributory.

### 2026-05-08 - EXQ-433f adds fifth confirmation; SD-050 reef enrichment does not break monostrategy

V3-EXQ-433f (2026-05-08 diagnose-errors): C0 trials-sufficient gate
FAILed in 3/4 seeds (agent_caused_trials 15/7/20/3 vs target 20). SD-050
reef enrichment (`reef_enabled=True`, `n_reef_patches=3`,
`hazard_food_attraction=0.7`) intended to break monostrategy on 8x8
grid but did not produce balanced events at this scale. Hold remains
gated on MECH-269 / MECH-269b V_s landing; reef-substrate tweaks are
not the unblock.

### 2026-05-08 - Sleep substrate identified as upstream gate

Per 2026-05-08 governance and substrate_queue MECH-204 entry's
unblocks_claims, the sleep loop is the load-bearing upstream substrate
for SD-029 / MECH-256 retest. The relationship is bidirectional: sleep's
MECH-273 writeback consumes SD-029 causal_sig, and SD-029 retest
requires sleep recalibration to break the V_s monostrategy. This plan
records the gate; sleep_substrate_plan Phase 1 is the trigger.

---

## Open questions

Numbered for reference from future sessions.

- **Q1 (Phase 4)**: Does the comparator mechanism generalise to
  nociceptive streams? Comparator literature evidences mechanism on
  sensorimotor / tactile / force / oculomotor / electrosensory streams.
  Extension to nociceptive plausible (PAG/RVM descending modulation
  shares efference-copy structure; ACC/insula pain self-vs-other
  attribution) but not directly demonstrated in the four canonical
  comparator papers (Frith 2000, Shergill 2003, Blakemore 1998,
  Haggard 2017). Default proposed: schedule a targeted lit-pull on
  nociceptive comparator / descending pain modulation
  (anchor papers: Fields 2004, Wager 2013, Seymour 2019, plus
  2020-2025 reviews). Resolves to either "MECH-256 generalises ->
  SD-029 inherits lit_conf" or "MECH-256 + nociceptive needs separate
  design doc -> SD-029 has its own architectural commitment".
- **Q2 (Phase 1)**: For the ARC-033 vs ARC-058 verdict, what
  forward_r2 degradation threshold should trigger ARC-058 retirement?
  Default proposed: degradation > 5% on z_harm_s forward_r2 in the
  shared-trunk path vs the independent-per-stream path is sufficient
  to weaken ARC-058. Less than 5% with a usable shared-PE signal
  weakens ARC-033 in favour of parameter parsimony.
- **Q3 (Phase 3)**: For MECH-257 controller signal selection in V3,
  is the hypothesis tag (MECH-094) sufficient, or does the controller
  need additional state (commitment boundary, heartbeat phase from
  ARC-023, dACC EVC at V4)? Default proposed: V3 uses MECH-094 only;
  V4 layered controllers added in a follow-up plan-doc when ARC-023
  + Shenhav-EVC substrates become available.
- **Q4 (Phase 2)**: When SD-029 retest finally produces balanced
  events, is the partial-attenuation pattern (Shergill 2003) the
  correct C2 acceptance, or should C2 require near-binary
  discrimination? Default proposed: partial attenuation is the
  biologically grounded acceptance per Shergill 2003 (~50% partial,
  not binary); a binary requirement would over-specify the comparator.

---

## Resume ritual

When picking up self-attribution work after a deviation:

1. Read this plan document first.
2. Read the [Status table](#status-table) and identify the row that
   was `paused` or `in-progress`.
3. If `blocked`, check whether the upstream gate has fired:
   - GAP-2 / Phase 2: read [sleep_substrate_plan.md](sleep_substrate_plan.md)
     status table for Phase 1 PASS + check substrate_queue.json
     MECH-269 / MECH-307 entries.
   - GAP-3 / Phase 3: check Phase 2 status here AND Phase 1 verdict.
4. If `in-progress`, find the most recent decision-log entry for that
   phase and continue from the last concrete action.
5. Update the row's `Last updated` field and `Status` if it changes.
6. Append a new decision-log entry for any architectural choice made
   during the resumed session.

Sessions that do NOT touch self-attribution work do not need to read
this document. Sessions that DO touch SD-003 / SD-029 / MECH-256 /
MECH-257 / SD-013 / ARC-033 / ARC-058 / MECH-258 / MECH-260 / SD-030 /
SD-031 read this document before any code or experiment edit.

The plan-doc is the agent's working memory across sessions. TodoWrite
entries die with the session; WORKSPACE_STATE.md is recent-work, not
strategic; substrate_queue.json is granular but does not capture phase
ordering or decision rationale. This document is the single source of
truth for self-attribution strategy.

---

## See also

- [docs/architecture/self_attribution_per_stream.md](../../docs/architecture/self_attribution_per_stream.md)
- [docs/architecture/sd_013_e2_harm_s_interventional_training.md](../../docs/architecture/sd_013_e2_harm_s_interventional_training.md)
- [docs/architecture/sd_032_cingulate_integration_substrate.md](../../docs/architecture/sd_032_cingulate_integration_substrate.md)
- [docs/architecture/sd_003_experiment_design.md](../../docs/architecture/sd_003_experiment_design.md) (historical / superseded)
- [evidence/planning/sleep_substrate_plan.md](./sleep_substrate_plan.md) Phase 4 cross-boundary
- [evidence/planning/sd033_governance_plan.md](./sd033_governance_plan.md) plan-doc precedent
- [evidence/planning/substrate_queue.json](./substrate_queue.json) MECH-204 priority=1 (sleep gate); SD-029 priority=1; MECH-307 priority=1
- evidence/planning/goal_pipeline_plan.md (sibling plan-of-record; consumes comparator output via dACC bundle; not yet written at registration time)
- evidence/planning/commitment_closure_plan.md (sibling plan-of-record; in-progress in parallel session)
