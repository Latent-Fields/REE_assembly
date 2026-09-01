# GOV-V4CUT-1 — V4 Prerequisite Cut (first derivation)

- **Generated:** 2026-09-01T04:55:40Z
- **Session:** c2-v4cut-20260901 (campaign plan C2, `docs/plans/campaign_plan_20260901.md`)
- **Chip:** chip-20260901-v4-prerequisite-cut-derivation
- **Posture:** AUDIT REPORT — a derived projection over existing claims/plans (GOV-V4CUT-1's
  own registration requirement, same posture as GOV-CEIL-1/GOV-APPLY-1). This document is
  NEVER a second hand-maintained registry: every verdict below cites the registry/plan
  artifact it was derived from, goes stale the moment those move, and is superseded by
  re-running the derivation. Nothing here was applied to `claims.yaml`; proposed
  dispositions were routed as `governance_flag.py raise --flag-type contested_disposition`
  entries (Section 3) for `/governance` + user adjudication.

## Inputs

- `docs/claims/claims.yaml` — GOV-V4CUT-1 entry (the eight-category frame) + the live registry.
- `docs/assets/data/claims.json` — derived `assembly_state` (1077 claims; 252 `gated_v3`).
- `evidence/planning/closure_status.md` (2026-08-30T15:51Z) — "Remaining work to close v3"
  (34 nodes) + "Assembly frontier" (10 nodes) ONLY. Deferred/Done/V4-V5 sections not swept.
- `docs/architecture/v4_spec.md` (Phase A draft, 2026-05-02) — the five V4 primitives and the
  spec's own V3 prerequisites section.
- `evidence/planning/thought_intake_2026-08-31_replay_rebucketing_decision_relevance.md` —
  first pull-forward candidates.
- Cross-check target: `docs/plans/campaign_plan_20260901.md` Section 2 (the first-order read
  this audit supersedes).

**Method note (per the task's constraint):** the cut was NOT inferred from `phase:` labels.
Each verdict asks what V4's five primitives (V4-0 object permanence, V4-1 multi-agent,
V4-2 self-model, V4-3 long-horizon, V4-4 action repertoire) *structurally assume*, and
whether a V3 failure there would surface inside V4 behaviour as an uninterpretable artifact.
Historical placement in the work graph (which plan a node lives in, what phase label a claim
carries) was treated as evidence about provenance, not about architectural dependence — and
Section 2.3/3 documents several places where the two disagree.

---

## 1. The transitive prerequisite set

The smallest set of V3 capabilities whose truth or functional adequacy V4 actually assumes,
with qualification state and the evidence behind each verdict. Qualification vocabulary
(GOV-V4CUT-1): **robust** = robustly demonstrated; **localised** = causally localised
sufficiently for inheritance; **bounded** = bounded-and-instrumented (known failure mode
detectable and distinguishable from V4-specific effects); **BLOCKING** =
unresolved-and-blocking.

**Set size: 11 capabilities.** 4 qualified (robust/bounded), 3 partially qualified, 4 BLOCKING.

| # | Capability V4 assumes | Assumed by | State | Evidence pointer |
|---|---|---|---|---|
| P1 | Non-degenerate committed-action selection (F-dominance bounded, diversity floor real) | V4-1 (any social readout), V4-4 | **BLOCKING** → convertible to *bounded* | MECH-439 (~88-89% variance monopoly) measured with a since-repaired instrument; re-audit is chip-20260830-mech439-571b-monopoly-audit (C1 item 1, unexecuted). Ceiling lifted V3-EXQ-689d PASS (behavioral_diversity GAP-I); conversion-ceiling campaign 0%, 7 nodes assembling |
| P2 | Multi-step planning recruitment (habit/planned arbitration; full-horizon read exists and is recruited) | V4-1 explicitly (v4_spec "full completion gate"), V4-3 | **partial** | MECH-477 arbitration SUPPORTED (V3-EXQ-811a PASS 2026-07-24); MECH-163 leg 1 WEAKENED (V3-EXQ-786b, recruitment-on-novelty failed without arbitrator); MECH-478 long-horizon leg unresolved (awaiting_substrate); MECH-479 prosocial leg is structurally a V4 test, not a V3 prerequisite — see Section 3 F6 |
| P3 | Self-attribution (self/world-caused sensory-change discrimination) | V4-0 (MECH-278's own precondition), V4-1 (other-agent modelling presupposes self/other separation) | **BLOCKING** | ARC-033 stable, but the operative comparator claims (MECH-256, SD-031) are unadjudicated and self_attribution GAP-1/2 are blocked on the same substrate gates (closure_status rows, forensic 445h read); GAP-6 discriminative validation blocked |
| P4 | Trained representational compression sites + non-collapsing readout interfaces | V4-0 (entity slots bind into z_world/E1 schemas — v4_spec implementation surface), all V4 measurement | **BLOCKING** | MECH-523 (designated compression sites systematically UNTRAINED), SD-080 (E2.action_object_head receives zero gradient from every training path), MECH-518 (one-tensor-two-masters variance contention), MECH-516 (argmax collapse at incentive-to-goal interface), MECH-517 (interface-before-representation ordering); SD-070/SD-056 are the named remediation recipes |
| P5 | Sleep/consolidation write path that writes CONTENT (not only calibration) | V4-0 (sleep-aggregation schema stabilisation is v4_spec's own open design question), V4-3 | **bounded, pending H1-H4** | SD-017 stable/shown; sleep_substrate 91% done; the open piece is sleep_substrate:GAP-2 (SD-017 retest cohort, upstream_blocked) gated on the write-content H1-H4 portfolio (chip-20260830-ctxmem-write-content-h1h4-portfolio, unexecuted); SD-068 lesion harness exists as the detection instrument |
| P6 | Commitment / closure / mode governance | V4-3 (lifetime identity is commitment-scaffolded), V4-4 (withdrawal-analog = committed disengagement) | **robust** (residue = characterisation) | MECH-090 active/shown; MECH-449 provisional/shown; commitment_closure plan 79% done; open nodes are OCD-battery completeness (GAP-4/GAP-4-battery — classified characterisation, Section 2.1) and one buildable trigger wiring (GAP-7) |
| P7 | Goal pipeline (wanting / liking / drive cascade) | all five primitives | **robust** | goal_pipeline plan 100% done; SD-012 provisional/mature (v4_spec first-paper gate satisfied 2026-05-02) |
| P8 | Epistemic-deficit / orienting drive (aimed investigation) | V4-0 (MECH-276 scientist-agent, MECH-277 action-space discovery presuppose an epistemic drive to aim intervention) | **BLOCKING** (build in flight) | MECH-482 accumulator substrate landed (campaign plan §1); ORNT-2 open on MECH-482's own non-degeneracy precondition; C3 item 1 (sd_epistemic_deficit_multitarget_readiness, IGW-225) is the staged unblock; MECH-489 chain autopsied (V3-EXQ-910b confirmed-autopsied) |
| P9 | Defensive/coping action repertoire beyond freeze (instrumental avoidance, escape-affordance, recovery) | V4-4 (coping channels are the point of the richer repertoire; MECH-102's framing needs them) | **partial** | MECH-357 node partial (mech357_avoidance_efficacy:BUILD, Stage-H wiring unfinished); SD-058/SD-059 registered, substrate partially landed; MECH-353/354/356 affect streams registered |
| P10 | Calibrated scalar harm/affect readout | V4-1 (other-agent z_harm_a/welfare modelling inherits any miscalibration), ethics cohort (Q-028/029) | **bounded** | Calibration-debt programme WP-A done (memory: project_calibration_debt); SD-086/SD-087 register the residual defect precisely (norm-vs-scalar confound; flag-on scoping); Q-086 is the environment-confound control |
| P11 | Interpretability & provenance harness (epoch tagging, diversity umpire, staleness lints, MECH-517 discipline) | the cutover itself — V4 evidence must be distinguishable from inherited-V3 artifact | **robust** (inheritance must be made explicit) | architecture_epoch machinery handles a V4 epoch (v4_spec migration item 4); Q-092 umpire + repaired MECH-439 instrument exist; the cutover condition is that these instruments are *carried into* the V4 harness, not merely exist in V3 (Section 4.2) |

**What is deliberately NOT in the set** (the campaign plan's first-order read includes some
of these — disagreements detailed in 2.3): rule apprehension (ARC-062 family), the global
workspace access gate (GATE-B/SD-064), the OCD battery, goal-hierarchy enrichment, the
ghost-goal/topology refinements, all fine-grain biology-fidelity hypotheses. V4's five
primitives assume none of them; each is inherited *capability* whose validation is desirable
but whose absence does not make V4 behaviour uninterpretable.

---

## 2. Classification into the eight GOV-V4CUT-1 categories

### 2.1 The 34 remaining + 10 assembling closure nodes

Categories: **IP** = inherited_prerequisite, **VAL** = validation_of_inherited_capability,
**CHAR** = v3_only_characterisation, **HARN** = v3_harness_or_calibration, **DIAG** =
diagnostic_debt, **SUP** = superseded_or_reposed_by_v4, **V4L** = v4_or_later_architecture,
**ORPH** = orphan_or_dependency_defect.

**Remaining (34):**

| node | category | rationale (one line) |
|---|---|---|
| orienting:ORNT-1 | IP | orienting/surveying mode is P8; V4-0 scientist-agent aims interventions with it |
| orienting:ORNT-2 | IP | the P8 accumulator's own non-degeneracy validation; gates everything in the cluster |
| orienting:ORNT-3 | VAL | third behavioural regime = validation of the P8 capability once ORNT-2 lands |
| orienting:ORNT-4 | CHAR | explanatory question about a V3 phenomenon (cold-start floor); not assumed by V4 |
| orienting:ORNT-6 | VAL | MECH-489 defensive-orienting chain validation (910b autopsied); defensive repertoire completeness |
| self_attribution:GAP-1 | IP | ARC-033-vs-ARC-058 path adjudication IS the causal localisation P3 needs |
| self_attribution:GAP-2 | IP | SD-029/MECH-256 retest under full stack = P3 qualification |
| self_attribution:GAP-3 | VAL | 3-arm ablation refines an already-localised capability |
| self_attribution:GAP-6 | VAL | SD-031 discriminative validation; P3 secondary leg |
| sd_037_axis_b:P2 | HARN | deterministic threshold recalibration (plan's own framing) |
| sd_037_axis_b:P3 | HARN | verification diagnostic for the recalibration |
| sd_037_axis_b:P4 | HARN | terminal validation of a calibration campaign; not a capability V4 assumes |
| arc_062:GAP-B | VAL | MECH-309 behavioural falsifier; rule apprehension is inherited capability, not a V4 assumption (see 2.3) |
| arc_062:GAP-H | VAL | ARC-065 diversity-generation residue leg |
| arc_062:GAP-I | VAL | bottom-up rule discovery, blocked on GAP-B; same family verdict |
| arc_062:GAP-I-absorption | VAL | absorption checks; bookkeeping-grade validation |
| arc_062:GAP-J | CHAR | precision-gating family characterisation, low sev |
| arc_062:GAP-K | VAL | MECH-319 write-gating evidence largely satisfied (V3-EXQ-628) |
| behavioral_diversity:GAP-B | IP | E3 scoring collapse (MECH-341) is a P1 face |
| behavioral_diversity:GAP-C | IP | tonic noise floor (MECH-313) is the P1 diversity-floor face |
| behavioral_diversity:GAP-G | HARN | MECH-314 Goldilocks weight calibration |
| behavioral_diversity:GAP-I | IP | MECH-439 F-dominance — the P1 root; highest-leverage single node in the cut |
| global_workspace:A | CHAR | does REE have a J-space — a characterisation question about V3; V4 does not assume workspace |
| global_workspace:B | CHAR | ablation-cliff shape; same verdict |
| global_workspace:GATE-B | CHAR* | *conditional: becomes IP only if the top-k access gate is adopted into the default V4 constitution (see 2.3, disagreement 1) |
| global_workspace:MECH-191 | HARN | cross-architecture legibility of a readout = methodology |
| policy_decomposition:REPOSE | SUP | autopsy-confirmed non-contributory on the saturated V3 regime; the trigger question is better posed where chunks actually fail to ground — candidate V4 re-pose (Section 4.3) |
| commitment_closure:GAP-4 | CHAR | OCD-battery completeness = clinical-fidelity characterisation; the commitment CAPABILITY (P6) is already qualified (see 2.3, disagreement 2) |
| commitment_closure:GAP-4-battery | CHAR | same verdict, behavioural cohort leg |
| commitment_closure:GAP-7 | IP | MECH-091 salient-event resync: 2 of 3 triggers unwired, buildable now; V4's event-driven ecology leans on phase-reset harder than V3 |
| mech357:BUILD | IP | instrumental-avoidance wiring completes P9's coping repertoire |
| sleep_substrate:GAP-2 | IP | SD-017 retest cohort = P5's write-content qualification |
| infant_substrate:GAP-13 | HARN | novelty-bonus Goldilocks sweep = calibration |
| infant_substrate:GAP-14 | CHAR | curriculum-vs-flat comparison; V3 characterisation (NB: evidence bearing on the ARC-136-vs-ARC-019 tension) |

**Assembling (10):**

| node | category | rationale |
|---|---|---|
| conversion_ceiling:CAMPAIGN | IP | umbrella of the P1 qualification programme |
| conversion_ceiling:FULLSTACK | IP | the co-armed full-stack test IS P1's qualification event |
| conversion_ceiling:GENERATION | IP | MECH-458 sixth face; blocked_on_upstream |
| conversion_ceiling:P-comp | IP | selection-face composition (ran_non_contributory — carries diagnostic residue) |
| conversion_ceiling:P2-rootC | IP | de-commit authority face (MECH-445/446) |
| conversion_ceiling:P3-ofc | IP | valuation face, built — nearest-to-ready P1 face |
| conversion_ceiling:P4-learned-gating | IP | ARC-108/MECH-450 learned-gating face |
| behavioral_diversity:GAP-K | IP | same ARC-108/MECH-450 stack seen from the diversity plan |
| commitment_closure:GAP-8 | VAL | SD-033b behavioural validation (built) — validation of the qualified P6 |
| sd_037_axis_b:P1b | HARN | substrate-readiness diagnostic for a calibration campaign |

**Closure-node tally (44):** IP 18 · VAL 10 · CHAR 8 · HARN 7 · SUP 1 · DIAG 0 · V4L 0 · ORPH 0.

### 2.2 The 252 gated_v3 claims, by coherent cluster

`gated_v3` = `v3_pending` manual hold, or `implementation_phase: v3` without mature status
(`scripts/build_claims_json.py:resolve_assembly_state`). Clusters below are exhaustive and
disjoint — coverage was machine-checked against the derived set (252/252 assigned, 0
duplicates; method in the Appendix). Exemplars are named; ids are listed so the projection
is reproducible, but this list is a *projection*, not a registry.

**Tally (252):** inherited_prerequisite **68** · validation_of_inherited_capability **64** ·
v3_only_characterisation **41** · v3_harness_or_calibration **38** (of which 20 are
process/governance/out-of-domain claims the eight-category frame does not really apply to —
see the last cluster) · v4_or_later_architecture **33** · superseded_or_reposed_by_v4 **6** ·
diagnostic_debt **1** · orphan_or_dependency_defect **1**.

**inherited_prerequisite (68):**

- *Selection / diversity / conversion-ceiling* (18) — the P1 programme. Exemplars MECH-439
  (F-dominance root), MECH-448 (rank-preserving demotion), MECH-457/459/460/461 (competence
  floor family), MECH-463/464/465 (arousal/opponent-gain composition), MECH-313 (noise
  floor), SD-061, MECH-440, MECH-445/446, ARC-107, ARC-088, MECH-140, MECH-458.
- *Planning recruitment / dual-system* (11) — the P2 programme. Exemplars MECH-163
  (narrowed core), MECH-477 (supported), SD-081, MECH-057b, ARC-028, MECH-105, MECH-135,
  MECH-236/237, MECH-125, SD-084.
- *Representation-training debt* (7) — the P4 cluster: MECH-523, SD-080, MECH-518,
  MECH-516, MECH-517, SD-070, SD-056. **Absent from the campaign plan's first-order read
  entirely; this audit's strongest addition** (finding 1, Section 2.3).
- *Self-attribution core* (4) — P3: MECH-256, SD-031, MECH-098, MECH-221.
- *Sleep write-path content* (6) — P5: MECH-120, SD-071, SD-083, MECH-283, MECH-285, Q-055.
- *Defence / coping channels* (9) — P9: MECH-353/354/356/357/358, SD-058/059, MECH-489,
  SD-099.
- *Incentive / object binding* (7) — MECH-344/345/346/347/348, MECH-436, SD-057. Classified
  IP because this stack is the V3 seed of V4-0 entity slots (per-object identity binding
  already half-exists on the wanting side) — see flag F4.
- *Object-identity minimal pillars* (3) — ARC-080/081/082. The registry already gates these
  v3 while v4_spec claims V4-0 as the object-permanence primitive; the minimal token-identity
  form is a genuine V3 prerequisite, the full slot architecture is V4-0 (flag F4).
- *Ethics floor invariants* (2) — INV-092 (suppression permeability), INV-093 (harm-sensitivity
  floor under skill optimisation): constitution-level constraints whose load INCREASES under
  V4's heavier learning; qualify (or bound) before richer optimisation inherits them.
- *Salient-event resync* (1) — MECH-091 (= commitment_closure:GAP-7, buildable now).

**validation_of_inherited_capability (64):** E1 goal/context conditioning (7: MECH-116,
MECH-128, MECH-150/151/153, MECH-160, MECH-162); self-attribution secondary (3: MECH-072,
MECH-115, MECH-136); sleep/consolidation secondary (8: MECH-286, MECH-289/290/291, SD-038,
MECH-208, MECH-213, MECH-490); verisimilitude anchor gating (2: MECH-269/269b);
hippocampal retrieval pathways (3: ARC-032, MECH-325, MECH-326); ARC-063 candidate-rule
faces (9: MECH-349..352, SD-078, SD-082, MECH-317, ARC-113, MECH-314b); control-plane/PFC
subdivisions (14: SD-032d, SD-033/033c/033d, SD-036, MECH-251, MECH-258, MECH-260, MECH-265,
MECH-480, MECH-161, SD-069, SD-075, MECH-342); harm-stream structure (9: ARC-052, ARC-058,
MECH-219/220, SD-019a/b, MECH-167, MECH-305, MECH-332); safety-prediction substrate (3:
SD-051/052, SD-065); hippocampal valence nodes (1: SD-014); drive legacy formulations (3:
MECH-111/112/113 — largely absorbed by the done goal pipeline, pending absorption
adjudication); ethics cue sufficiency (1: INV-040); learning meta-selection (1: MECH-474).

**v3_only_characterisation (41):** goal-hierarchy enrichment (8: ARC-051, ARC-060,
MECH-426/427/428, SD-092, MECH-455, SD-077 — several better *posed* in V4-3, Section 4.3);
ghost-goal/topology refinements (7: MECH-292/293, MECH-339/340, MECH-468/469/470);
vigor/idle-aversion (6: ARC-066/067/068, MECH-320, MECH-330/331); pathology/phenomenology
(7: MECH-222, MECH-118, MECH-307, MECH-467, INV-062, MECH-209, MECH-180); open design
questions (10: Q-040/041/042, Q-056, Q-081, Q-094/095, MECH-466, MECH-494/495);
developmental v3-curriculum-scoped (2: ARC-042, ARC-075); integration band (1: INV-091).

**v3_harness_or_calibration (38):** calibration debt (7: SD-086/087, Q-086, SD-066/067,
Q-043, Q-054); probe/env harness (8: SD-068, SD-074, SD-023, SD-054, SD-048, SD-055,
SD-076, Q-092); learning-integrity discipline (3: MECH-384, MECH-471/472 — methodology V4
inherits wholesale); **process/governance/out-of-domain (20)**: GOV-ANALOGY-1, GOV-HELDOUT-1,
GOV-META-1, GOV-METAB-1, GOV-PRESERVE-1, GOV-REJECT-1, GOV-STRAT-1, GOV-UMPIRE-1,
GOV-V4CUT-1 itself, SENT-17, SOC-HUM-1..4, and the meta-architecture framings ARC-106,
ARC-112, ARC-120/121, ARC-130/131. The eight-category frame is about organism capabilities;
these are programme-process or societal claims that advance by practice outcomes, not
experiments, and carry no cutover force (SENT-17 excepted — it is a constraint ON the
migration; carried into the dossier, Section 4.5).

**v4_or_later_architecture (33):** social/V4-flagged strays currently gated v3 (8:
MECH-276, MECH-278, ARC-031, MECH-129, MECH-130, ARC-083, ARC-077, MECH-308 — the first
three are listed by v4_spec itself as V4-0/V4-2 cohort members, flag F5); biology-fidelity
fine grain awaiting an organ-analog substrate no generation yet plans (19: MECH-074/074b/074d,
MECH-099, MECH-107/109/110, MECH-186/187/188, MECH-203/204, MECH-206, MECH-239, MECH-270,
MECH-282, MECH-294, ARC-037, ARC-038); unbuilt architecture commitments richer than V3's
frame (2: ARC-053 TCL, ARC-054 D_V); developmental lifetime/critical-period (4: ARC-076,
MECH-335/336, INV-041 — these need V4-3 persistent identity to be testable at all).

**superseded_or_reposed_by_v4 (6):** the decomposition/composition cluster — ARC-070,
MECH-321/322/323/324, Q-085. The V3-EXQ-938 autopsy found the V3 regime saturated
(non-contributory); grain/chunking questions are better posed where chunks fail to ground,
which V3's environment does not produce (Section 4.3). Note the adjacency to the ARC-134
grain family: if F1's minimal-grain split is accepted, the *perceptual* half pulls forward
while this *policy* half re-poses in V4 — the two halves of "grain" get opposite verdicts,
deliberately.

**diagnostic_debt (1):** MECH-492 — a registered defect finding (MECH-286's sleep-permission
threat conjunct is an uncalibrated, undeclared-source consumer), not a capability claim.

**orphan_or_dependency_defect (1):** MECH-274 — title literally opens "V4-reserved." while
its labels gate it v3; pure bookkeeping defect (flag F5).

### 2.3 Cross-check against the campaign plan's Section 2 first-order read

Agreements (stated so the disagreements are legible): orienting/epistemic-deficit,
self-attribution GAP-1/2, F-dominance root, sleep write-path CONTENT — all confirmed as
inherited prerequisites; sd_037_axis_b as calibration, infant GAP-13/14 and the J-lens
experiments as non-blocking — confirmed.

**Disagreements (the deliverable the task asked for):**

1. **global_workspace:GATE-B — plan says inherited prerequisite; this audit says
   v3_only_characterisation (conditional).** V4's five primitives nowhere assume a
   capacity-limited workspace access channel; SD-027/MECH-254 describe an optional gate
   (`use_boundary_access_gate`) probing whether REE *has* workspace-like access dynamics.
   That is a characterisation question about V3. It converts to inherited_prerequisite only
   under an explicit design decision to adopt the gate into V4's default constitution — a
   decision nobody has taken. Building GATE-B is still worthwhile (experiments A/B want it);
   it just does not gate the cutover.
2. **Commitment machinery — plan lists commitment_closure GAP-4/7/8 wholesale as inherited
   prerequisites; this audit splits them.** The commitment CAPABILITY (P6) is already
   qualified (MECH-090 active/shown; MECH-449 provisional/shown; plan 79% done). GAP-4 and
   GAP-4-battery are OCD-battery completeness — psychiatric-fidelity characterisation of V3,
   valuable and publishable, but a V4 built on an organism without a completed OCD battery
   is not thereby uninterpretable. Only GAP-7 (MECH-091 trigger wiring, a build) stays IP.
3. **Rule apprehension (arc_062 GAP-B and dependents) — plan says inherited prerequisite;
   this audit says validation_of_inherited_capability, non-blocking.** V4-0..V4-4
   structurally assume none of the rule machinery; the richer rule *sources* the programme
   cares about (ARC-077 social scaffolding) are themselves V4-bound. A V3 rule-apprehension
   failure would surface in V4 as absent rule-following — detectable, attributable, not
   masquerading. GAP-B remains load-bearing *within V3's own closure definition*; the cut
   distinguishes "V3 closure wants it" from "V4 assumes it", which is exactly the
   conflation GOV-V4CUT-1 exists to remove.
4. **The representation-training debt cluster (MECH-523, SD-080, MECH-518, MECH-516,
   MECH-517, SD-070, SD-056) is missing from the plan's first-order read altogether** — and
   this audit ranks it among the top two blockers (P4). V4-0's entity slots bind into
   exactly the sites MECH-523 shows are untrained and SD-080 shows receive zero gradient;
   MECH-517 states the general principle that representation improvements are undetectable
   through collapsing interfaces. Building V4-0 on this foundation is the canonical
   "inherited defect masquerading as novel phenomenon" scenario.
5. **policy_decomposition:REPOSE — plan lists it under harness/characterisation
   non-blockers; this audit classifies superseded_or_reposed_by_v4** (with its whole
   mechanism family), on the strength of the V3-EXQ-938 autopsy's regime-saturation finding.
   A V3 re-pose is possible but pays the environment-enrichment cost for one question; the
   V4 ecology produces grounding failures natively.

---

## 3. Pull-forward adjudications (claim-split proposals — PROPOSED, not applied)

Frame: GOV-V4CUT-1's registration note — "prefer claim SPLITS (minimal v3 prerequisite vs
richer v4 mechanism) over wholesale relabelling." Every proposal below was raised as a
`contested_disposition` governance flag; nothing was edited in `claims.yaml`. Adjudications
AGAINST pull-forward are recorded here too (they need no flag — no change is proposed).

**F1 — ARC-134 + MECH-521 (endogenous perceptual grain): SPLIT, minimal P0 forward.**
Proposal: a minimal v3 claim asserting only that a merge/split operator over the existing
EntityObservation boundary must exist and be *corrigible by consequence evidence* — fixed
capacity, no dynamic per-population regulation, no settling competition. The richer
mechanism (MECH-521's occupancy-as-order-parameter settling dynamics, MECH-522 ephaptic
specialisation) stays v4_v5. Grounds: MECH-529's intake names P0 grain as the substrate
floor of the rebucketing loop; ARC-134's own notes concede the perceptual cell is genuinely
empty in V3; and the scalar-dial-vs-per-population caution in ARC-134's notes is exactly
respected by pulling forward only the operator's existence, not its regulation.

**F2 — MECH-507 (compression/decompression bridge): SPLIT, minimal decompression head
forward.** Proposal: a minimal v3 claim that at least ONE designated compression site gets
an explicit *trained* decompression/readout stage. Grounds: this is the same repair the P4
training-debt cluster already needs (SD-080's zero-gradient head, MECH-518's dual-role
contention, MECH-517's interface principle) — the minimal MECH-507 form is not new V4
machinery, it is the principled statement of the P4 remediation. The full reciprocal-bridge
reframing stays v4_v5.

**F3 — MECH-529 (replay-driven rebucketing): SPLIT, two plumbing contracts forward.**
Proposal: pull forward (a) an index-continuity contract — consolidation/re-indexing must
preserve episodic addressability (already implicitly assumed by V3 sleep machinery; testable
against the existing SD-017/SD-068 harness), and (b) typed insufficiency signals as
plumbing — E3/commitment outcomes emit typed error signals, never category labels
(non-oracularity is enforceable in V3 today). The full split/merge/reweight loop stays v4
(its substrate floor is F1's P0 operator).

**F4 — ARC-080/081/082/083 (object-identity pillars) vs v4_spec V4-0: SPLIT the ownership.**
The registry gates ARC-080/081/082 v3 while v4_spec claims object/entity permanence as V4-0
— double ownership with contradictory version placement. Proposal: minimal v3 form = a
token-bound identity representation over the object kinds V3 already has (resources,
hazards, landmarks), building on the MECH-344/345 per-object binding stack that half-exists
on the wanting side; the full pillar architecture (occlusion-surviving slots, affordance
bundles, ARC-083 others-as-slots) is V4-0. ARC-083 additionally moves v4 outright
(others-as-slots presupposes V4-1).

**F5 — Label conflicts: MECH-274, MECH-276, MECH-278, ARC-031.** MECH-274's title opens
"V4-reserved." yet it is gated_v3; MECH-276/MECH-278 are v4_spec V4-0 cohort members and
ARC-031 a v4_spec V4-2 cohort member, all currently gated_v3. Proposal: re-label to their
v4_spec placement (or split per F1-F4 pattern where a genuine v3 seed exists — MECH-278's
precondition clause is P3, already owned by self_attribution).

**F6 — The v4_spec entry gate itself (MECH-163 + MECH-478 + MECH-479): RE-DERIVE.**
v4_spec's "full completion gate: MECH-163 validated" is unsatisfiable as written: MECH-163
was narrowed 2026-07-22 to leg (1), leg (1) was then WEAKENED by V3-EXQ-786b, legs (2)/(3)
were split out to MECH-478/479, and MECH-479 (prosocial planning) structurally requires
V4-1 to test — the gate as written contains its own deadlock. Proposal: restate the V3-side
planning gate as {MECH-477 arbitration (already SUPPORTED, V3-EXQ-811a) + MECH-478
long-horizon leg}, and move MECH-479 to V4-phase validation. This is the P2 row of
Section 1 made actionable.

**Adjudicated AGAINST pull-forward (no flag; recorded for the audit trail):**
- **MECH-512** (momentary compression depth): no knob exists at any timescale
  (`e1_deep.py`), and its own notes require MECH-496's allocation policy to land first.
  Nothing in the prerequisite set assumes momentary depth control. Stays v4_v5.
- **MECH-508** (attractor-as-generative-disposition): representational redefinition whose
  dissociation experiment requires MECH-512 as an independent variable; no v3-minimal form
  exists that is distinct from existing precision instrumentation. Stays v4_v5.
- **Sleep/replay re-indexing beyond F3(a)**: the full re-indexing mechanism is the v4 loop;
  only the continuity CONTRACT pulls forward.

---

## 4. Cutover-review dossier

### 4.1 Which V3 failures could still make V4 behaviour uninterpretable?

Ranked by (probability of being real) x (masquerade potential inside V4):

1. **Untrained compression sites / collapsing interfaces (P4).** V4-0 binds entity slots
   into representational sites that MECH-523/SD-080 show are untrained. Failure mode: entity
   "permanence" scores reflect harness artifacts of a degenerate O-space; representation
   improvements invisible (MECH-517). *Masquerade potential: maximal* — this is the exact
   class GOV-V4CUT-1's registration warns about ("inherited V3 defects masquerading as novel
   phenomena").
2. **F-dominance monopoly unbounded (P1).** If committed-selection variance is still
   monopolised, every V4-1 social readout collapses to near-deterministic policy — and reads
   as "agents do not socially differentiate", a fake V4 discovery. The 571b re-audit is the
   single cheapest uncertainty reduction in the entire cut.
3. **Self-attribution unresolved (P3).** Other-agent modelling without a validated
   self/other comparator produces misattribution dynamics (MECH-222's psychosis analog) that
   would read as social phenomena.
4. **Sleep writes calibration, not content (P5).** V4-0's schema stabilisation premise
   fails silently; object schemas never consolidate and the failure attributes to V4-0's
   new machinery rather than the inherited write path.
5. **Epistemic drive absent/degenerate (P8).** V4-0's scientist-agent stages degrade to
   undirected flailing; "action-space discovery" results become noise studies.
6. **Miscalibrated harm scalar (P10).** The V4 ethics cohort (Q-028/029, MECH-102) inherits
   a norm-vs-scalar confound; welfare conclusions become artifacts. Cheap to fix in V3
   (SD-086/087 are precise).

### 4.2 Are those detectable in V4 if they occur?

| Failure | Detectable in V4? | Condition |
|---|---|---|
| P4 interface collapse | **Poorly** — the defect suppresses its own evidence (MECH-517) | Must be fixed or bounded IN V3; minimum bound = land SD-070/SD-080-style training on the sites V4-0 binds to, plus a collapse lint in the V4 harness |
| P1 monopoly | Yes, IF the repaired MECH-439 instrument + Q-092 umpire are ported into the V4 harness | Make instrument inheritance an explicit cutover condition — P11 |
| P3 misattribution | Partially (comparator telemetry exists) | GAP-1/2 adjudication, or ship V4 with the comparator instrumented and a declared bound |
| P5 content-free consolidation | Yes — SD-068's lesion harness generalises | Port SD-068 to the V4-0 harness; H1-H4 portfolio remains the V3-side answer |
| P8 degenerate epistemic drive | Yes (behavioural; accumulator telemetry) | C3 build 1 + ORNT-2 validation |
| P10 harm miscalibration | Yes (calibration probes are substrate-independent) | Run the SD-086/087 recalibration before any V4 ethics claim |

The asymmetry in row 1 is the dossier's sharpest conclusion: **P4 is the one blocker that
cannot be deferred to V4-side detection.** Everything else can in principle cross the
boundary bounded-and-instrumented; P4 crosses only as an embedded artifact generator.

### 4.3 Which remaining V3 questions are better posed in V4's richer ecology?

- **Prosocial planning (MECH-479)** — structurally V4-1; posing it in V3 is impossible, not
  merely awkward (F6).
- **Policy decomposition/composition (ARC-070, MECH-321..324, Q-085)** — V3's regime is
  measured-saturated (V3-EXQ-938 autopsy); V4 produces chunk-grounding failures natively.
- **Goal-hierarchy enrichment (ARC-051/060, MECH-426/427/428, SD-092)** — subgoal credit
  and hierarchy earn their keep over multi-episode horizons; V4-3's lifetime boundary is the
  natural test bed.
- **Coping-channel differentiation (MECH-102 framing, parts of P9's richer repertoire)** —
  negotiation/withdrawal/cooperation only exist as channels in a multi-agent ecology.
- **Agent-typed novelty (MECH-130), relational harm (MECH-129)** — need an "other" to type
  against.
- **Developmental critical-period claims (ARC-076, MECH-335/336, INV-041)** — need V4-3
  persistent identity for a critical period to be a fact about an individual.
- Conversely, questions that should NOT be deferred: everything in Section 4.1 (deferral is
  how they become uninterpretable), and the calibration items (cheap now, confounded later).

### 4.4 Is V3 still exposing foundational defects, or mostly calibration/characterisation?

Both, in a measurable ratio. Recent months still produced genuine foundational-defect
discoveries — MECH-518 (dual-role tensor contention), SD-080 (zero-gradient head), MECH-523
(untrained compression sites), MECH-492 (undeclared-source consumer) are all 2026-07/08
registrations, and they are DEFECTS, not calibration. That argues the cutover window is
**not yet open**: the organism is still yielding structural surprises at a rate that would
contaminate V4. But the composition of the remaining work has visibly shifted: of the 44
live closure nodes, 15 (34%) are characterisation/harness; of the 252 gated claims, 118
(47%) are characterisation/harness/process and another 39 (15%) belong to V4-or-later or
re-pose buckets — i.e. **most of the nominal "remaining V3 work" does not gate V4.** The
blocking core is small and enumerable: the four BLOCKING capabilities (P1, P3, P4, P8) plus
the P2/P5 partial legs. That is the window's near edge.

### 4.5 Cutover conditions this audit proposes for the eventual review

1. P1: 571b audit landed; conversion-ceiling FULLSTACK verdict in hand (either direction —
   a bounded negative is inheritable; an unbounded unknown is not).
2. P2: F6's re-derived gate — MECH-478 resolved or explicitly bounded; MECH-477 stands.
3. P3: GAP-1/2 adjudicated, or comparator shipped instrumented-with-declared-bound.
4. P4: designated compression sites trained (SD-070/SD-056-class recipes applied to the
   sites V4-0 binds), + interface-collapse lint in the V4 harness. **Non-deferrable.**
5. P5: H1-H4 write-content verdict in hand; SD-068 harness ported.
6. P8: epistemic-deficit build landed + ORNT-2 non-degeneracy shown.
7. P10: SD-086/087 recalibration applied.
8. P11: repaired diversity instrument + umpire + epoch tagging carried into the V4 harness
   as a checklist item, not an assumption.
9. SENT-17 honoured across every mechanism substitution the migration performs (the one
   governance claim with direct cutover force).
10. After qualification, per GOV-V4CUT-1: V3 continues as validated simple reference
   organism (v3-only characterisation continues WITHOUT gating V4), V4 becomes the active
   development organism — two states at once, legitimately.

---

## Appendix — method and reproducibility

- gated_v3 population: `docs/assets/data/claims.json` filtered on
  `assembly_state == "gated_v3"` (252 of 1077 as of this run; derivation semantics in
  `scripts/build_claims_json.py`).
- Closure nodes: the two named sections of `closure_status.md` (2026-08-30T15:51Z snapshot),
  verbatim — 34 + 10 rows.
- Cluster assignment was validated programmatically: 252/252 covered, 0 duplicate
  assignments, 0 non-gated ids. The assignment dict is small enough to re-derive from
  Section 2.2's id lists; deliberately NOT committed as a data file (audit posture — this
  report is the projection's record, the registry stays the single source of truth).
- Known sensitivity: cluster→category is judgement at cluster grain; individual claims near
  cluster boundaries (e.g. MECH-260 dACC bias suppression, sitting between control-plane
  validation and the P1 diversity stack; Q-056 between characterisation and P1) would move
  one bucket without changing any Section 1 or Section 4 conclusion.
- Supersedes: the first-order read in `docs/plans/campaign_plan_20260901.md` Section 2 (that
  document says so itself). Superseded by: any re-run of this derivation after governance
  acts on the Section 3 flags.
