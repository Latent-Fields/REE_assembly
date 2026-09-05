# Failure autopsy -- V3-EXQ-993a (ARC-021, MECH-069)

**Generated:** 2026-09-05T02:38:25Z - **Scope:** single - **Status:** `confirmed`
**Confirmed:** 2026-09-05T09:34:00Z by `governance-20260905 (user gate, inline route A)`
(Drafted headless in staging mode on behalf of governance session `governance-20260905`. The Step 7c
cross-model red-team and the Step 8 human gate have both now run -- see **section 8b**, which records
what they changed. The hypothesis-space registry block in section 14 remains
**draft-for-governance**: the main session writes the registry, this artifact does not.)
**Machine-readable:** `failure_autopsy_V3-EXQ-993a_2026-09-05.json`
**Re-adjudication of:** `failure_autopsy_ext-claim-probe-cluster_2026-09-03` (target V3-EXQ-993), read in full.

---

## 0. The one-line verdict

The merged-channel ablation ARC-021 has been asking for since March finally ran with a working
readout, cleared every gate including the new DV-headroom ones, and **found nothing**. Merging the
three learning channels did not degrade harm calibration -- it was indistinguishable in DENSE and
nominally *better* in SPARSE. That is ARC-021's own pre-registered falsifying
signature, so the driver's combination rule emitted `weakens` -- and **governance records `mixed`
instead**. Three reasons, all raised by the Step 7c cross-model red-team and ratified at the Step 8
gate: computed correctly (t(3), not z), the run's own 95% interval does **not** exclude the -0.15
degradation it pre-registered, in *either* condition, and joint power there is ~12%; only **one of
ARC-021's two falsifier DVs** was read; and the three things merged were experiment-local surrogate
heads over a frozen latent, not the E1/E2/E3 modules ARC-021 names by file. So the run is
**informative** -- it rules out a *large* merged degradation on a working readout, which nothing in
this family could do before -- and it is not a falsification.

---

## 1. Facts -- no interpretation

**Run:** `v3_exq_993a_arc021_merged_channel_action_conditioned_harm_20260904T212334Z_v3`
**Queue:** V3-EXQ-993a (priority 45, `machine_affinity: any`, backlog EVB-1248), `supersedes` V3-EXQ-993.
**Purpose:** `evidence`. **Outcome:** FAIL. **Label:** `merged_channel_hypothesis_not_supported`.
**Machine:** `ree-cloud-4`, `linux-x86_64-py3.10-torch2.12.0+cpu`, elapsed 83.5 s.
**Claims tagged:** ARC-021, MECH-069. **EXT-003 deliberately dropped** (see section 7).

**Dry-run gate (Step 2a):** `check_dry_run_citations.py` -> `0 dry cited, 0 dry in named families,
0 ambiguous, 1 clean, 0 unknown`. Top-level `dry_run` absent/falsy on the manifest.
`dry_run_checked: true`, `excluded_dry_run_ids: []`. No dry manifest is cited anywhere below.

**Recording provenance:** `validate_recording.py` -> **OK, zero always-core gaps**. `recording_schema
rec/v1`, top-level `substrate_hash 7cd0378...`, `substrate_stable_across_run: true`, `machine` /
`machine_class`, `elapsed_seconds`, full `config`, explicit `seeds [101,202,303,404]`, and a per-cell
`arm_fingerprint` on all 16 cells. `substrate_commit` records `dirty: true, dirty_count: 1` on an
unrelated path (`experiments/_lib/baselines/arc019_curriculum_gating.py`) -- noted, immaterial.

**One recording defect the schema check cannot see (red-team H1).** `validate_recording.py`'s "OK" is
true of the **schema** and false of one **value**: `metrics.worst_harm_action_sensitivity` records
**8.0**, which is the *coverage count*, not the sensitivity. The driver reads
`preconditions[0]["measured"]` positionally (line 1336) and the design red-team's F6 later inserted
`control_arm_coverage_complete` at index 0. The true value, **0.11382**, is at
`interpretation.preconditions[1].measured`. **No verdict is affected** -- every gate and both
criteria read `interpretation.preconditions` directly, not `metrics` -- but any consumer reading that
field gets 8.0. Recorded in the JSON under `recording_defects`; one-line fix (index by `name`, not
position) for any lettered successor.

### 1a. What the script measures and how it decides

Two hazard densities (DENSE 15 hazards, SPARSE 4) x two arms x four seeds = 16 cells.

- **ARM_SEPARATED (control):** three independent heads (sensory-reconstruction, action-conditioned
  forward, action-conditioned harm), three independent Adam instances, three independent losses,
  three disjoint parameter sets, three separate backward passes. Verified at source.
- **ARM_MERGED:** one shared 2-layer trunk consuming `(z_world, action_onehot)`; all three heads read
  its hidden representation; ONE Adam over trunk+heads; ONE summed loss backpropagated jointly.

Depth-, width- and clip-matched (design red-team F5), so **parameter sharing and loss summation are
the only differences** -- which is exactly ARC-021's content.

DV: `calibration_gap = mean(causal_sig | near_hazard) - mean(causal_sig | safe)`, where
`causal_sig = harm_logit(z_t, a_actual) - harm_logit(z_t, a_cf)` read **pre-sigmoid**, with the
counterfactual restricted to movement actions (F8).

Criteria, per condition, paired per seed: `mean(MERGED - SEPARATED) <= -0.15` **AND** all four seeds
`<= 0`. PASS iff both conditions fire; `mixed` if one; **`weakens` if neither**.

### 1b. Expected vs observed

| | DENSE | SPARSE |
|---|---|---|
| SEPARATED mean gap | 0.45438 | 0.39862 |
| MERGED mean gap | 0.44801 | 0.51061 |
| **mean paired diff** | **-0.00637** | **+0.11199** |
| per-seed diffs (101/202/303/404) | -0.0147 / -0.1784 / +0.0736 / +0.0941 | +0.3521 / -0.0153 / +0.1105 / +0.0006 |
| seeds with MERGED <= SEPARATED | 2 of 4 | 1 of 4 |
| criterion | **FAIL** (margin and sign-consistency) | **FAIL** (margin and sign-consistency) |
| non-degenerate | true | true |

Expected under ARC-021: MERGED at least 0.15 *below* SEPARATED in both conditions, every seed.
Observed: essentially zero in DENSE, and the *wrong sign* in SPARSE.

**Which criterion failed: the DISCRIMINATION criteria, and only those.** Every readiness, absolute
and non-degeneracy gate passed:

| gate | measured | threshold | headroom |
|---|---|---|---|
| `control_arm_coverage_complete` | 8 | 8 intended | complete |
| `harm_head_action_sensitivity_present` (worst control cell) | 0.11382 | 0.05 | 2.3x |
| `p1_harm_events_observed_per_condition` (min across conditions) | 1616 | 10 | 161.6x |
| **H1** `dv_headroom_margin_room_below_control` (floor_headroom) | 0.22857 | 0.15 | 1.52x |
| **H2** `dv_headroom_control_signal_floor_reachable` (max_abs) | 0.71546 | 0.40 | 1.79x |
| non-degeneracy: mean SEPARATED vs `SEPARATED_SIGNAL_FLOOR` 0.20 | 0.4544 / 0.3986 | 0.20 | 2.3x / 2.0x |

All eight SEPARATED cells are positive (0.2286 to 0.7155). **This is the inverse of the
substrate-ceiling fingerprint.** The usual tell is "absolute/negative-control gates pass,
discrimination fails because the DV had no room". Here headroom was *measured, over the control arm,
before a single MERGED cell was trained* -- and the discrimination failed anyway.

> **What that headroom does and does not certify (red-team F4).** H1 declares `dv_bounds: [0.0, 1.0]`
> and computes `floor_headroom = min(control) - 0.0`. But `calibration_gap` is a difference of mean
> logit differences and is **unbounded below** -- the driver says so itself (lines 203-205), and
> negative components appear in this run's own cells. That is conservative for a *refusal* gate, but
> as evidence that "MERGED had room to degrade" it is vacuous: on an unbounded-below DV there is
> always room to fall by 0.15. What H1 actually establishes is that the **control** arm's signal sits
> at least MARGIN above zero. The question a null needs answered is **power**, not headroom -- see
> section 4.

Two bookkeeping notes on the table (red-team H2, H3). Of the five precondition entries, **three carry
`kind: readiness` and two carry `kind: dv_headroom`** -- they are not all readiness-kind. And the two
`dv_headroom` entries carry **no `met` key**, unlike the three readiness entries; the indexer
recomputes `met` from `(measured, threshold, direction)` per the entry's own `implementation_note`, so
nothing breaks, but "all five passed" above is read off that **recomputation**, not off the manifest.

---

## 2. Claim layer

### ARC-021 -- "Three BG-like cortico-striatal loops require distinct learning channels"

`architectural_commitment`, status **provisional**, `epistemic_category: standard`,
`pending_retest_after_substrate: true`, `depends_on [ARC-004]`, `coupled_with [MECH-033, MECH-069, Q-019]`.

Its `evidence_quality_note` is unusually candid about its own provenance: the 2026-03 promotion
reasoned *one hop* from SD-003's V3-EXQ-007/008/009/010 series, all four of which are formally FAIL
against their own >0.05 bar (gaps -0.0151, -0.0066, -0.0184, +0.0267). The note's own summary is
"channel separation trends correctly, and does not obviously hurt" -- **not** "separation is
required" -- and it states outright: *"the load-bearing test has never been run... that needs the
merged-channel ablation specified in what_would_answer."*

**V3-EXQ-993a is that test.** And its `what_would_answer` pre-states the falsifying signature
verbatim: *"if a merged/shared-channel condition (single trunk, single optimizer, one loss combining
sensory + motor-sensory + harm/goal error) produces calibration_gap ... statistically
indistinguishable from -- or better than -- the separated-channel baseline, across the same
near-hazard/safe probe design and both dense- and sparse-hazard conditions, that falsifies the
REQUIRED part of ARC-021."*

The run produced that pattern in both conditions, on the probe design named -- **on one of the two
DVs the signature names.** The falsifying text requires `calibration_gap` **AND** attribution accuracy
to be indistinguishable-or-better; this driver reads `calibration_gap` only (there is no
attribution-accuracy readout anywhere in it). And "statistically indistinguishable" is not what a
threshold-plus-sign-consistency criterion tests: at this run's power, "indistinguishable" means
"underpowered", which is not what the falsifier text intended. Both points are red-team F2(b), and
together with the corrected interval in section 4 they are why the recorded direction is `mixed`
rather than `weakens`.

Its non-degeneracy precondition -- *"requires the three error channels to be genuinely separately
optimized **in the substrate under test**"*, a sentence that then names `E1DeepPredictor` / E2 /
`E3TrajectorySelector` by module path -- is satisfied by the SEPARATED arm **in the surrogate's sense,
not in the substrate the sentence names** (red-team F2(c) / H4). The *topological* reading is met and
verified at source (three disjoint parameter sets, three optimizers, three backward passes); the
modules separately optimized are experiment-local heads. Reading the precondition as discharged here
is a substitution of substrate, and it is recorded as one rather than waved through.

### MECH-069 -- "Sensory prediction error, motor-sensory error, and harm/goal error are incommensurable and cannot be collapsed"

`mechanism_hypothesis`, status **stable**, `epistemic_category: standard`,
`pending_retest_after_substrate: true`, `depends_on [MECH-033, ARC-018]`.

The MERGED arm literally collapses the three, and harm calibration did not degrade -- so the run is
on-target for the *collapse-degrades-harm-calibration* consequence. It is **not** on-target for
MECH-069's scale / covariance / temporal content (`v3_exq_005_mech069_error_scale.py`'s question,
never run to a manifest). The driver pre-registered this narrowing itself: *"this run tests the
collapse-degrades-E3 consequence, not MECH-069's scale/temporal content ... so it cannot on its own
demote a stable claim."*

### claim_ids accuracy

Both tags are earned. Neither is inherited without re-evaluation -- the driver re-derived the tag
list from scratch and *removed* one (EXT-003, section 7). No peripheral co-tag applies, so no
`recommended_epistemic_category_per_claim` re-attribution is needed on those grounds (both are
stamped `standard` for the ordinary reason).

### Out-of-domain trap check

Neither claim is a clinical or out-of-domain claim, and neither's decisive-test description names a
test class this run cannot instantiate -- ARC-021's names *this* test. `governance-reclassify
(out_of_domain)` does not apply, and would be actively harmful (it sits in `_UNTESTABLE_EPISTEMIC`).

---

## 3. Biological-reference triage

**Closest reference:** parallel segregated cortico-basal-ganglia-thalamic loops (Alexander/DeLong),
with channel-specific dopaminergic teaching signals; cerebellar forward internal models as the
motor-sensory channel; PAG-to-dopamine nociceptive gating as the harm channel.

**Formal-definition import?** No. ARC-021/MECH-069 are biological translations, not imports of
Pearl/Shannon/optimal-control machinery. The SD-003 counterfactual *shape* the DV uses is a formal
construct, but it is the same shape used across the V3-EXQ-007-010 series and is not the locus here.

**Literature status: PRESENT, and no `/lit-pull` is owed.**

- `targeted_review_connectome_arc_021` (2026-03-29): Haber 2003 corticostriatal spirals,
  Hazy 2007 BG loops and learning, O'Reilly & Frank 2006 three BG loops.
- `targeted_review_connectome_mech_069` (2026-09-04, campaign C4, 5 entries).
- `targeted_review_reafference_streams`: Haak & Beckmann 2018 (three white-matter streams).

**The C4 pull is directly load-bearing here, and it splits.** The open question in the biology is
whether the three error signals are separately **computed** or merely separately **gated**:

| entry | direction | conf | bearing |
|---|---|---|---|
| Engel 2024 -- heterogeneous striatal dopamine (NAc-core / DMS / DLS) | supports | 0.78 | territories are not uniform readouts of one broadcast signal |
| Groessl 2018 -- PAG-to-dopamine fear gate | supports | 0.72 | a distinct harm channel exists |
| Engelhard 2019 -- specialized sensory/motor/cognitive coding in VTA DA neurons | mixed | 0.68 | functionally clustered, but within one population |
| Wolpert 1998 -- cerebellar forward internal models | supports | 0.66 | a separate forward-model channel |
| **Schultz 1998 -- global RPE counterweight** | **weakens** | 0.60 | DA neurons *"fail to discriminate between different rewards"*; specificity is added downstream |

**This matters for the adjudication.** Schultz's position -- one global teaching signal,
differentiated at the readout -- is *precisely* what this run's null is consistent with. So the FAIL
does **not** contradict the biological existence proof for parallel loops; it bears on whether
separate *computation at the source* is required, which is contested in the biology itself. That is
the honest reading, and it is why this run is genuinely **informative** rather than a
translation failure -- but it is also a reason the direction is `mixed`: a null that the biology's own
minority position predicts, at a power that could not have detected the majority position's effect,
does not discriminate between them.

**Missing-dependency signature?** No. The failure does not resemble what would happen biologically
if a known dependency of the reference mechanism were absent -- there is no prerequisite here that
is missing and would restore the effect. (The one candidate, an unfrozen encoder so the merge can
reach representation learning, is not a *missing dependency* but an untested configuration, and is
routed as H2/H1 legs below.)

---

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | For the NECESSITY half of ARC-021 and MECH-069's collapse-degrades-calibration consequence, at this scale. The claim's own falsifying signature was produced on the probe design it names, in both required conditions -- but on **one of its two DVs**, at a power that could not have detected the predicted effect (joint ~12% at -0.15), with the corrected interval **not** excluding -0.15, and on a surrogate rather than the substrate the precondition names. Moved from `weakened` at the Step 8 gate (red-team F1/F2). |
| Biological reference | **clear** (and internally contested) | Parallel loops are well evidenced; whether the error signals are separately *computed* is exactly what the 2026-09-04 C4 pull splits on. The null sits with Schultz 1998 against Engel/Engelhard/Groessl/Wolpert. |
| Developmental / dependency prerequisites | **present** | ARC-021's stated non-degeneracy precondition is satisfied by the SEPARATED arm, verified at source. `depends_on` ARC-004 / MECH-033 / ARC-018 are not implicated. |
| Implementation completeness | **partial** | *The load-bearing qualifier.* See below. |
| Environment adequacy | **adequate** | CausalGridWorldV2 12x12 / 3x3 view at BOTH hazard densities, as ARC-021's falsifying text requires. 1616 / 1878 harm events. Near-hazard and safe probe populations well populated and geometrically distinct in both (DENSE 683-698 vs 49-84; SPARSE 203-219 vs 583-638). The environment contains the pressure. |
| Measurement adequacy | **adequate** | The strongest measurement posture this family has had. See below. |
| Integration adequacy | **isolated** | Deliberately: no `ree_core.agent`/`REEAgent`, no E1/E2/E3 predictor module, no latent stack, no sleep loop. Same property as the implementation row. |
| Scale / capacity | **adequate** for the effects it was powered for | 4 seeds x 2 conditions x 2 arms; 80 P0 + 80 P1 episodes x 120 steps; 15 probe resets. See the power note below. |

**Why implementation is `partial` -- three specific things.** The ablation is a faithful *topology*
analogue, but it is instantiated in an experiment-local three-head surrogate over a 32-dim
`z_world`, not in the `E1DeepPredictor` / `E2WorldForward` / `E2HarmSForward` / `E3TrajectorySelector`
modules ARC-021's `what_would_answer` names **by file**:

1. **There is no E3 selection role at all.** Behaviour is a uniform-random policy; the harm channel
   is a supervised BCE classifier. "Harm/goal error" is instantiated as label prediction, not as a
   valuation channel with authority over commitment.
2. **The encoder is FROZEN during P1** (heads train on `.detach()`ed `z_world`). The merge can
   contaminate only a downstream 2-layer trunk; it cannot corrupt the *latent itself*, which is
   where cross-stream contamination would bite hardest biologically.
3. **The three losses are summed with equal weight** -- an arbitrary commensuration the claim does
   not specify.

**Why measurement is `adequate`.** The readout was rebuilt after the predecessor's sigmoid-compression
defect (action-conditioned pre-sigmoid logit, trained on the distribution it is read on). The control
arm went from max |gap| **0.00152 -> 0.71546 (~470x)**, positive in 8 of 8 cells.
`SEPARATED_SIGNAL_FLOOR` was **raised** 0.02 -> 0.20 and still cleared in both conditions. Bars were
sized against a *measured* paired null (24 cells, 3 head-init draws; mean +0.0216, sd 0.1659, sign
not consistent across draw pairs, i.e. centred on zero).

**The residual measurement debt -- stated not papered over, and CORRECTED at Step 7c (F1).** The
driver's own F9: `MARGIN = 0.15` with n=4 necessarily absorbs any sub-margin degradation. The draft of
this artifact then wrote a bound computed with a **z**-multiplier on n=4, which was wrong. An n=4
paired mean needs **t(3) = 3.182**, not 1.96:

| | mean diff | sd | drafted (z) 95% CI | **correct t(3) 95% CI** |
|---|---|---|---|---|
| DENSE | -0.00637 | 0.1240 | [-0.128, +0.115] | **[-0.204, +0.191]** |
| SPARSE | +0.11199 | 0.1696 | [-0.054, +0.278] | **[-0.158, +0.382]** |

So the run excludes a merged-degradation of roughly **0.20 or larger in DENSE** and **0.16 or larger
in SPARSE** -- and **does not exclude the pre-registered -0.15 in either condition.** The drafted
intervals and the "0.13+ / 0.05+ excluded" clause are **withdrawn**, here and in the storable note in
section 13. Measurement stays `adequate` -- the instrument works -- but *adequate instrumentation is
not adequate power*, and the draft conflated the two.

**Power note -- and it does not let the claim off, but it does not let the FAIL off either.** Against
the measured per-cell null sd 0.1659, the full criterion (mean <= -0.15 AND all four seeds <= 0) has
roughly **35% power per condition** at a *true* effect of exactly -0.15 (red-team F1, Monte Carlo,
200k draws). The draft's "roughly 40%" was both imprecise and, more importantly, **per-condition** --
and the pre-registered PASS requires **both** conditions, so **joint power at -0.15 is about 12%**
(0.353^2). At -0.30 it is about **85% per condition and 73% jointly**.

Stated plainly: **this design returns a FAIL roughly 88% of the time when ARC-021 is exactly right at
the effect size the run itself pre-registered.** The observed point estimates *are* null-to-reversed
(DENSE -0.0064, SPARSE +0.1120) and that is worth recording -- but at this power that cannot be used
as a premise that the result is more than an unmet bar. The draft's "**null-to-reversed estimate**,
not merely an unmet bar" licence for `weakens` is **withdrawn**.

**And the one place the result must not be over-read.** SPARSE's apparent *advantage* for merging is
carried by a single seed: dropping seed 101 (+0.3521) leaves a mean of +0.0319. The defensible
statement is "indistinguishable, possibly better", **not** "merging helps".

---

## 5. Failure location (GOV-FAILLOC-1)

| Bucket | Reads from | Verdict |
|---|---|---|
| MECHANISM FAILED | Implementation completeness (`partial`) | **partial** -- not established |
| MEASURES FAILED | Measurement adequacy (`adequate`) | **established** |
| ENVIRONMENT FAILED | Environment adequacy (`adequate`) | **established** |
| REE FAILED | all three | **false** |

**Net: MIXED, MECHANISM-partial -- not chargeable to REE alone, and specifically not REE FAILED.**

Measurement and environment each read *independently adequate* here, which is rare in this corpus and
is why the run is **informative** rather than `non_contributory`: the readout was rebuilt and verified
*before* the arms were compared, the control arm carried real signal in 8 of 8 cells (~470x over the
predecessor), and both hazard densities were present.

**That is not, however, a licence for `weakens`, and the draft's two licensing premises are withdrawn
at the gate.** (i) *"The DV had measured room to move"* -- red-team F4: H1's `dv_bounds [0.0, 1.0]`
declaration is false for an unbounded-below DV, so the headroom gates certify the **control** arm's
signal, not the merged arm's room to degrade. (ii) *"a null-to-reversed estimate"* -- red-team F1: the
corrected t(3) intervals do not exclude the predicted -0.15 in either condition, and joint power there
is ~12%. Adequate **instrumentation** is not adequate **power**. Claim alignment therefore reads
`unclear` and the recorded direction is `mixed`; the net stays **MIXED, MECHANISM-partial**.

What is only partial is the mechanism's *translation*. So the correct organism-level statement is
**not** "REE's three-loop separation is unnecessary" but:

> A faithful topology analogue of the separation, tested where it was supposed to bite **at a power
> that could only have caught a large effect**, did not bite -- and the untested residue is the real
> stack **and the second falsifier DV**, not the instrument.

---

## 6. Work-graph classification and routing

**Node: `complex (probe-gated) / puzzle (known rules)`.** The frame is well posed -- we know exactly
what to merge, exactly what to measure, and the readout now works. What is missing is a **fact**:
does the null survive on the real E1/E2/E3 stack, with a live selection role and an unfrozen encoder?
That is a spike, not a build (so not `complicated (buildable)`); we do not already have the data, so
it is not `mystery (known data)`; and the residual is a named untested configuration, not noise, so
it is not `aleatoric (irreducible)`.

**Routing: `/queue-experiment`, NEW EXQ NUMBER -- not a lettered iteration of 993.** The scientific
question changes. 993/993a asked "does merging three surrogate channels degrade harm calibration?"
and that is now answered (no, at this scale, with the bounds above). The next question is "does that
null survive on the ree_core E1/E2/E3 stack?" -- a different mechanism under test.

### GOV-FANOUT-1: this is a discrimination, so fan out

Three live hypotheses, three different design axes, each with a declared null:

| | Hypothesis | Axis | Probe | Null |
|---|---|---|---|---|
| **H1** | Separation genuinely is NOT required; the null is the truth | drive | Same two arms with the **encoder unfrozen** and jointly optimised in P1, so a collapsed objective can corrupt the latent itself | both mean paired diffs still > -0.15, no sign consistency |
| **H2** | The surrogate is too shallow to express the contamination; the null is a translation artefact | representation | Ablate the **actual ree_core stack** (E1/E2/E3 under one optimizer over `agent.parameters()`) inside a live `REEAgent` loop, scoring calibration_gap **and** attribution accuracy **and** a selection-level harm-avoidance readout. Six mandatory repairs first -- see section 8 | no degradation beyond a margin the design can actually detect, in either condition |
| **H3** | The degradation is real but SUB-MARGIN and this design cannot resolve it (the driver's own F9) | measurement | >= 16 seeds and/or paired variance reduction (shared P0, common random numbers), pre-registering a **0.05** effect stated as a CI on the paired mean | the 95% CI excludes -0.05 in both conditions |

**H2 is the highest-value leg -- it is the test ARC-021 names by file -- and it should NOT be
authored from scratch.** See section 8 for the existing driver it starts from and the **six** repairs
that are mandatory before it runs. One of those repairs (the detach/undetach encoder gradient) is what
keeps H1 and H2 **separable at all**: as the existing driver stands, it varies both in a single arm.

### What is NOT owed

- **No `/lit-pull`.** Both claims carry current targeted reviews; MECH-069's landed 2026-09-04.
- **No `/implement-substrate` build.** The substrate amend below records a *resolution* and
  validation evidence, not a gap.
- **No `/claim-synthesis` handoff.** See section 9.
- **No demotion.** ARC-021 stays `provisional`; MECH-069 stays `stable`. One scoped, underpowered
  surrogate-topology run does not demote a stable claim, and the driver pre-registered that constraint.
- **A MANIFEST OVERRIDE *is* owed.** The flat manifest and the run-pack manifest both carry
  `evidence_direction: weakens` and `evidence_direction_per_claim: weakens/weakens`, and the indexer
  has already scored that. Recording `mixed` in `claims.yaml` alone would leave the scored direction
  disagreeing with the confirmed adjudication -- see the apply checklist in section 13 and
  `recommended_manifest_write` in the JSON.

---

## 7. The EXT-003 drop -- recorded view for governance ratification

**Endorse the drop.**

EXT-003 asserts an **exploitation** failure mode: scalar reward conflates incommensurable error
signals, *so an agent exploits the conflation*. V3-EXQ-993a has no reward, no policy optimisation and
no agent maximising anything -- behaviour is uniform-random and all three channels are supervised
prediction targets. Nothing in the design can hack anything, in either direction.

Tagging it would let a claim-scoring consumer read "reward hacking tested" off a design with no
reward, which is the exact failure `REE_assembly/CLAUDE.md`'s claim_ids-accuracy rule 3 warns about
("err toward fewer tags"). The drop costs EXT-003 nothing: V3-EXQ-993 tagged it and was adjudicated
`non_contributory`, so no evidence entry is lost.

**Counter-argument considered and rejected.** The MERGED arm *does* instantiate the mechanism half of
EXT-003's rider (one scalar objective summed over three error terms), so a partial/mixed tag could be
argued. Rejected: EXT-003's polarity asserts the *exploit*, and a design in which nothing can exploit
anything cannot bear on it either way. Under-tagging here **protects** the 2026-09-03 user ruling
that EXT-003 waits on experimental evidence -- the right response is a probe that actually
instantiates a reward and an optimisation loop, not a tag on a supervised prediction study.

**Bears-on note governance should carry anyway.** EXT-003's `ree_mechanism` field cites MECH-069 and
ARC-021 as the reason REE resists reward hacking ("REE maintains three distinct BG-like loops with
separate learning channels that cannot be mutually satisfied by a single exploit"). That rider
**inherits** whatever ARC-021/MECH-069 lose here, without any evidence tag on EXT-003 itself.

---

## 8. Mechanical pre-routing checks (Step 7b) -- 1 fire, ACTED ON

`scripts/autopsy_pre_routing_checks.py --json` -> `fire_count: 1`.

> **C1** -- *routing recommends queue-experiment for ['ARC-021','MECH-069'], but driver(s) for that
> claim are already on disk, have NEVER scored a run (nor has any same-question sibling), and are not
> mentioned anywhere in this artifact:* **`v3_spark_arc021_three_loop_scale`**

**Disposition: acted on, and it changed a recommendation.** Read at source,
`ree-v3/experiments/v3_spark_arc021_three_loop_scale.py` imports `ree_core.agent.REEAgent` and
implements SEPARATE (three independent optimizers) vs MERGED (**one optimizer over
`agent.parameters()`, combined loss E1+E2+E3**) at `REEConfig.large()` world_dim=128, scoring
`e3_discrim` *and* `harm_rate`. That is materially the **H2 leg** -- the ablation on the real
E1/E2/E3 stack in a live agent loop, the one thing 993a did not do and the thing ARC-021 names by
file. It has never produced a manifest.

So the H2 probe is rewritten to **start from this driver rather than author a fourth** -- with **six
mandatory repairs**. Items 1-2 came from the Step 7b read; items 3-6 were added by the Step 7c
red-team (F3), which read the file at source and found a confound that would have wrecked the leg:

1. Its C1 bar `e3_discrim_separate > e3_discrim_merged + 0.02` is **unmeasured** -- the same defect
   class 993 died of. Re-derive it from a measured control arm.
2. It carries **no `dv_headroom` precondition**. Add H1/H2 gates of the
   `dv-dynamic-range-precondition-class` kind over its control arm before the MERGED arm trains --
   and declare `dv_bounds` **honestly** for whichever DV is chosen (an unbounded-below DV must not be
   declared `[0, 1]`; that false declaration is this autopsy's own red-team F4).
3. **Pair the arms on seed.** It runs `_run_condition("SEPARATE", args.seed, ...)` then
   `_run_condition("MERGED", args.seed + 1, ...)` (lines 318-320), so the arms differ in env seed
   **and** agent init -- the unpaired-arm defect class the 993 design red-team fixed by pairing.
4. **Break the encoder-gradient confound -- this is the load-bearing one.**
   `_train_step_separate` computes the harm loss on `latent.z_world.detach()` (line 108) while
   `_train_step_merged` uses the **undetached** `latent.z_world` ("allow contamination gradient",
   lines 126-128). So as written, MERGED differs from SEPARATE in **two** things at once: optimizer
   topology **and** whether the harm gradient reaches the encoder. Those are precisely **H1**
   (encoder-level merge) and **H2** (real-stack merge) above -- run as-is, the driver would **alias
   the two legs in one arm**, the exact verdict-aliasing GOV-FANOUT-1 forbids. Fix: make the encoder
   gradient a **separate factor** (2x2: topology x detach/undetach) or make it **symmetric** across
   arms, and state in the queue entry which manipulation the leg isolates.
5. **Multi-seed with a measured paired null.** It is single-seed (default 42), with no
   sign-consistency rule and no measured null, so repair 1's bar has nothing to be sized against.
   Given this autopsy's own power arithmetic (joint ~12% at -0.15 on n=4), the successor must
   pre-register an effect its seed count can actually **detect**, not inherit 993a's -0.15/n=4.
6. **Runner/indexer-compatible manifest.** Its output is an ad-hoc JSON -- no `claim_ids`, no
   `evidence_direction`, no recording-standard fields, no `--dry-run`, no `_experiment_lib` -- written
   to `REE_assembly/evidence/experiments/<type>/`. Rebuild it through `experiments/_lib`
   (`manifest_core.stamp_recording_core(...)`) or nothing it produces will be scored.

Also recommended: add the 993a `calibration_gap` readout alongside `e3_discrim` (and read ARC-021's
second falsifier DV, attribution accuracy), since `e3_discrim` is a discrimination statistic rather
than the SD-003 causal signature `what_would_answer` names.

**Runnability against the current `agent.py` is UNVERIFIED, and this artifact says so rather than
implying otherwise.** Every agent method the spark calls resolves *by name*
(`compute_prediction_loss`, `generate_trajectories`, `select_action`, `record_transition`,
`update_residue`, `sense`, `reset`; the `e1`/`e2`/`e3`/`latent_stack` attributes; `REEConfig.large`;
the `CausalGridWorldV2` kwargs) -- but **signatures were not checked and the file has never
executed**. A smoke run against current `agent.py` is the *first* step of this leg.

**This does not contradict the 993a driver's own C1 verdict.** That verdict ruled the spark not a
substitute *for 993a's question*, on exactly reason 3 plus the unmeasured bar -- and it was right.
What changed is that the same file is the right *starting point* for the different, downstream
question this autopsy routes.

C2, C3 and C6 did not fire; C5 was reported inapplicable on the pre-`.md` draft run and re-checked
clean afterwards. Both claim ids resolve, so the quiet on C2/C3 is a real quiet, not a blind one.

**Step 7c (adversarial red-team) was not run on the staged draft** -- excluded by the dispatching
session's staging scope. It has since been run, cross-model, and its findings are folded throughout
this artifact; see **section 8b**. Note separately that the *driver* carries its own cross-model
(fable) red-team pass from design time (CONTESTED, 10 findings, 7 fixed, 2 resolved by measurement, 1
recorded) -- that pass attacked the DESIGN, not this ADJUDICATION, and did not substitute for 7c.

---

## 8b. Red-team and gate

**Step 7c: cross-model adversarial pass (model `fable-5.1`) -- verdict `CONTESTED`.** Four defects
(F1-F4), three findings verified sound (F5-F7), seven hygiene items (H1-H7). All four defects and
four hygiene items are folded into both files; the machine-readable record is the top-level
`red_team` block in the JSON.

| # | Finding | What it moved |
|---|---|---|
| **F1** | The effect-size bound in the storable note used a **z**-multiplier on n=4, and the power figure was per-condition, not whole-run | Bound replaced with the t(3) intervals **[-0.204, +0.191]** DENSE / **[-0.158, +0.382]** SPARSE, which **do not exclude -0.15**; power restated as ~35% per condition and **~12% jointly** at -0.15 (~85% / ~73% at -0.30). The "null-to-reversed estimate, not merely an unmet bar" premise is **withdrawn** as a licence for `weakens`. |
| **F2** | `weakens` is the corpus-minority reading for the `{implementation: partial, measurement: adequate}` cell (123 `non_contributory` / 18 `weakens` / 10 `mixed`) and the draft neither cited nor justified the departure; two literal gaps against ARC-021's own falsifier text went unmentioned (second DV never read; the precondition names the substrate) | **Direction weakens -> `mixed` on both claims** (user gate). `claim_alignment` **weakened -> unclear**. The note now carries the corrected bound, the one-DV-of-two gap, the surrogate-vs-named-substrate substitution, and an explicit statement that this **departs from the direction the pre-registered combination rule emitted**. |
| **F3** | The H2 leg's "start from the spark driver" carried an unlisted confound that would **alias H1 and H2 in one arm**, and listed 2 of at least 6 mandatory repairs | Repair list section 8 rewritten to **six** items -- seed pairing, the detach/undetach encoder-gradient factor, multi-seed with a measured paired null, and an `_experiment_lib` manifest -- plus an explicit statement that runnability against current `agent.py` is **unverified**. |
| **F4** | H1's `dv_bounds: [0, 1]` declaration is **false** for an unbounded-below DV, so the headroom gates certify the **control** arm's signal, not the merged arm's room to degrade | "The DV had measured room to move" removed as a licence for the direction (sections 1b, 5). The substrate amend's validation record now reads **"PASS-path, first of six queued validations; refusal path never fired in production; dv_bounds declaration defect noted"**, and `validation_owed` should **not** be discharged on it (section 12). |
| **F5** | Clearing `pending_retest_after_substrate` on both claims -- **verified sound** | Kept unchanged. |
| **F6** | The substrate amend resolving the 993 `failure_record` item -- **verified sound** | Kept, with the F4 caveat attached. |
| **F7** | The EXT-003 drop -- **verified sound** | Kept unchanged (section 7). |
| **H1** | Manifest recording defect: `metrics.worst_harm_action_sensitivity` = 8.0 is the coverage count | Recorded in section 1 and in the JSON's `recording_defects`; no verdict affected. |
| **H2, H3** | "all five gates" is read off the indexer's recomputation; 3 are `kind: readiness`, 2 are `kind: dv_headroom` | Corrected in section 1b. |
| **H4** | "satisfied by the SEPARATED arm" | Qualified to "in the surrogate's sense, not in the substrate the sentence names" (section 2). |

H5 (the `standard` category call is right, but its confidence is tempered by F4), H6 (**every**
checked absolute holds -- 8/8 control cells positive, ~470x, H1 1.52x, H2 1.79x, the 2-of-4 and
1-of-4 sign counts, drop-seed-101 +0.0319, sds 0.124 / 0.170, worst control sensitivity 0.1138, harm
events 1616 / 1878, floor 0.20 cleared at 0.4544 / 0.3986) and H7 do not move the verdict.

**What the red-team did NOT contest, and what therefore stands unchanged:** the arms, the cells, the
sign counts, the gate ratios, the control coverage, the ~470x lift, the EXT-003 drop, the resolution
of the 993 `failure_record` item, and clearing the retest flag.

**Step 8: human gate (2026-09-05).** Decisions, binding:

1. `evidence_direction` -> **`mixed`** for **both** ARC-021 and MECH-069, on the four grounds in the
   note (corrected interval; joint power ~12% at -0.15; one falsifier DV of two; surrogate rather than
   the named substrate). The run is informative -- **not** `non_contributory` -- but it is not a clean
   falsification.
2. `pending_retest_after_substrate` **clears on both** (unchanged from the draft; GFLAG-0137).
3. `epistemic_category` stays **`standard`** on both (unchanged).
4. Because the manifest's own combination rule wrote `weakens` and the indexer has scored it,
   **governance must override the manifest on both copies** -- see the apply checklist in section 13.

---

## 9. Granularity-debt recurrence trigger -- does NOT fire

Read with `REE_assembly/scripts/granularity_debt_cluster.py` (targets whose own `claim_ids` name the
claim -- not a grep of the planning directory).

**ARC-021: 3 tagging targets, alignment distribution `other=1, unclear=1, untested=1`. NO target
reads `weakened`. Trigger does not fire.**

| artifact | run | direction / category | alignment |
|---|---|---|---|
| `failure_autopsy_ext-claim-probe-cluster_2026-09-03` | `v3_exq_993_...` | non_contributory / standard | untested |
| `failure_autopsy_grandfathered-misc2-ninethread-cluster_2026-08-08` | `v3_exq_004_arc021_incommensurability_...` | mixed / measurement_gap | unclear |
| `failure_autopsy_grandfathered-r6-closure-sweep_2026-08-08` | `20260316T232412Z_v3_exq_004_...` | mixed / measurement_gap | other |

The reader's own rule applies: a cluster in which no target reads `weakened` is measurement or
implementation debt, not granularity debt. The one free-text `other` was read by hand -- it says
"already-diagnosed elsewhere" and is the **same run** as the misc2 target (v3_exq_004,
double-counted across two 2026-08-08 grandfathered sweeps). No buried weakened reading.

> Note (amended at the Step 8 gate): the draft expected this autopsy to add ARC-021's **first**
> `weakened` target. It does **not** -- `claim_alignment` was moved to **`unclear`** (section 4), so
> ARC-021's distribution stays `other=1, unclear=2, untested=1` with **still no `weakened` target**,
> and the trigger's count-side condition remains unmet on the next pass too. Re-evaluate on the next
> ARC-021 autopsy -- and it will still need structurally *different* signatures, not merely a first
> weakened reading.

**MECH-069: 8 tagging targets, alignment distribution `other=3, unclear=2, weakened=2, untested=1`.
Count-side condition met; trigger still does NOT fire, on structural grounds.**

Both prior `weakened` targets circle the **same signature** as this run -- collapse/merge the error
channels and the harm-attribution readout fails to degrade:

- `v3_exq_035_mech069_optimizer_merge_...` is literally an optimizer merge (and its target was already
  `weakened_resolved_by_supersession`);
- `v3_exq_047b_sd005_sd010_joint_...` is the unified-vs-split latent -- the representation-level form
  of the same merge.

That is **one recurring question tested at three fidelities**, i.e. a fidelity ladder, not several
finer mechanisms hiding inside a coarse claim. Routing to `/claim-synthesis` would inflate the
believed tail on what is measurement/fidelity debt. If a fourth `weakened` MECH-069 target appears
with a *structurally different* signature -- a scale/covariance failure rather than a merge failure --
re-evaluate then.

---

## 10. Re-derive brake -- does NOT fire

Re-derived under the binding R1-R3 convention with the SKILL.md Step 7 recipe verbatim, run from
`/Users/dgolden/REE_Working` over every confirmed `failure_autopsy_*.json`:

| claim | counting hits | threshold | fires |
|---|---|---|---|
| ARC-021 | **0** | 2 | no |
| MECH-069 | **0** | 2 | no |

R1 (unit = run) and R2 (latest adjudication supersedes) are satisfied trivially -- each claim's only
recent target is the 993 one in the 2026-09-03 cluster. **R3 excludes it:** that target's per-claim
category is `standard`, not `substrate_ceiling`, so the predicate short-circuits at clause 1 before
the direction fallback is reached. The grandfathered 2026-08-08 targets carry
`measurement_gap`/`standard` with mixed directions and likewise do not count. **This autopsy adds no
hit either** -- category `standard`, direction `mixed` (moved from `weakens` at the Step 8 gate),
neither of which is a counting reading; the brake is unaffected by the change, since it counts
`substrate_ceiling` categories first and `weakens` was never the operative clause here.

`supersedes_autopsy`: `failure_autopsy_ext-claim-probe-cluster_2026-09-03`.
**No re-queue is refused.** The section-6 portfolio is permitted and recommended.

---

## 11. What this re-adjudication moves in the superseded artifact

Read `failure_autopsy_ext-claim-probe-cluster_2026-09-03` end to end (routing, failure-location,
learning) plus the 993a driver docstring, per the re-adjudication rule.

1. **Its central diagnosis is CORROBORATED, not overturned.** It localised 993's flatness to the
   driver-local harm head's sigmoid compression and prescribed reading the pre-sigmoid logit. Doing
   that -- plus the training-target repair the 993a driver measured independently -- raised the
   control arm ~470x. **The prescribed fix worked.**
2. **Its learning item 6 is vindicated:** "declining to lower a floor the data missed by 13x was the
   correct call". The floor was *raised* 0.02 -> 0.20 and still cleared in both conditions.
3. **Its `pending_retest_after_substrate: true` on ARC-021 and MECH-069 is DISCHARGED.** The stated
   condition was "once the readout is fixed"; it is fixed and the retest has run and cleared every
   precondition. See GFLAG-0137, raised precisely because the IGW routine keeps re-spawning "Retest
   after substrate: ARC-021" against a condition already met.
4. **Its substrate entry's 993 failure_record item is RESOLVED** (section 12).
5. **Its EXT-003 disposition is UNCHANGED** (`standard`, `non_contributory`, status stays candidate).
   EXT-003 is untagged here and only inherits the section-7 bears-on note.

---

## 12. Substrate queue -- `amend` to record a RESOLUTION, not a gap

**No new substrate gap was found and no new failure record is minted.**

`dv-dynamic-range-precondition-class` currently reads `status: implemented_pending_validation`,
`status_phase: validation_owed`, `severity: degrading`, paths
`[validate_experiments.py, experiments/_metrics.py::p0_readiness_gate]`.

**V3-EXQ-993a is its first production USE, and only a PARTIAL validation.** The `dv_headroom`
precondition kind ran over the control arm *before any MERGED cell trained*, measured H1 1.52x and H2
1.79x, and correctly let the run proceed to a verdict rather than self-routing
`substrate_not_ready_requeue`. **Record the validation verbatim as:**

> PASS-path, first of six queued validations; refusal path never fired in production; `dv_bounds`
> declaration defect noted.

The defect (red-team F4): H1 declared `dv_bounds: [0.0, 1.0]` for `calibration_gap`, which is a
difference of mean logit differences and is **unbounded below** -- and the precondition class did not
catch the false declaration. **Governance should therefore NOT discharge `validation_owed` on this
single PASS-path use:** the entry's own `implementation_note` names six queued validations, and the
refusal path (`substrate_not_ready_requeue`) is still unexercised in production.

**`resolves_prior_failure_record`:** the item for
`v3_exq_993_ext003_arc021_merged_channel_ablation_20260903T053340Z_v3` -> **`resolved`**. Its stated
target was *"a control-arm signal at or above the registered 0.02 floor, established BEFORE the
ablation arm is run"*. 993a establishes exactly that, through this entry's own machinery, against a
floor raised to 0.20. The other open item on the entry (`v3_exq_999_mech161_...`) is untouched. The item's target **is**
met and closing it is justified (red-team F6, verified sound) -- with the F4 caveat above attached to
the accompanying validation.

`severity` and `substrate_paths` are **unchanged** -- this occurrence is a success of the gate, not a
failure of it, so nothing about the classification moves.

---

## 13. Confirmed `evidence_quality_note` for governance (apply via `/governance`, not from here)

> V3-EXQ-993a (2026-09-04, supersedes V3-EXQ-993) is the merged-channel ablation ARC-021's
> what_would_answer has named as 'the missing test' since 2026-03. It is the FIRST run in this
> family with a working readout: the action-conditioned PRE-SIGMOID harm logit, trained on the
> distribution it is read on, lifted the SEPARATED control arm's max |calibration_gap| from
> 0.00152 (993, 13.1x below its own 0.02 floor) to 0.71546, positive in 8 of 8 control cells, with
> SEPARATED_SIGNAL_FLOOR raised 0.02 -> 0.20 and still cleared in both conditions (DENSE 0.4544,
> SPARSE 0.3986). Every readiness gate passed, including the two dv_headroom gates minted by the
> 2026-09-03 cluster autopsy's substrate entry dv-dynamic-range-precondition-class (H1
> floor_headroom 0.22857 vs MARGIN 0.15 = 1.52x; H2 max_abs 0.71546 vs 0.40 = 1.79x), both
> evaluated over the control arm BEFORE any MERGED cell trained. RESULT: merging the three
> channels into one shared trunk under one optimizer and one summed loss did NOT degrade harm
> calibration AT THE PRE-REGISTERED BAR. DENSE mean paired diff -0.0064 (merged 0.44801 vs
> separated 0.45438; per-seed -0.0147 / -0.1784 / +0.0736 / +0.0941, 2 of 4 negative); SPARSE
> +0.1120 in the OPPOSITE direction (merged 0.51061 vs separated 0.39862; per-seed +0.3521 /
> -0.0153 / +0.1105 / +0.0006, 1 of 4 negative). Both criteria required mean <= -0.15 AND all 4
> seeds <= 0; both failed on both clauses, so the driver's pre-registered combination rule emitted
> `weakens`. GOVERNANCE RECORDS `mixed`, NOT `weakens`, AND THIS IS A DELIBERATE DEPARTURE FROM
> THE PRE-REGISTERED RULE (user gate, 2026-09-05, after a cross-model Step 7c red-team returned
> CONTESTED). Four grounds, in order of weight. (1) EFFECT SIZE, CORRECTED. The bound originally
> drafted into this note ([-0.128, +0.115] DENSE / [-0.054, +0.278] SPARSE) was computed with a
> z-multiplier on n=4 paired diffs and is WITHDRAWN. The correct t(3) 95 percent intervals are
> [-0.204, +0.191] (DENSE, mean -0.0064, sd 0.1240) and [-0.158, +0.382] (SPARSE, mean +0.1120, sd
> 0.1696), which do NOT exclude the pre-registered -0.15 in EITHER condition. What the run
> excludes is a merged degradation of roughly 0.20+ (DENSE) / 0.16+ (SPARSE), and nothing smaller.
> Power at a true -0.15 is about 35 percent per condition and about 12 percent JOINTLY (the PASS
> requires both), i.e. this design returns FAIL roughly 88 percent of the time when ARC-021 is
> exactly right at its own pre-registered effect; at -0.30, power is about 85 percent per
> condition and about 73 percent jointly. (2) ONE FALSIFIER DV OF TWO. ARC-021's falsifying
> signature names calibration_gap AND attribution accuracy; this driver reads calibration_gap
> only, so the signature was met on half of what it specifies. (3) PRECONDITION SUBSTRATE. The
> non-degeneracy precondition requires the three channels to be separately optimized IN THE
> SUBSTRATE UNDER TEST and names E1DeepPredictor / E2*Forward / E3TrajectorySelector by file; the
> SEPARATED arm satisfies it only in the SURROGATE's sense (experiment-local
> sensory-reconstruction / forward-prediction / action-conditioned harm heads over a frozen 32-dim
> z_world), with no E3 selection role and a uniform-random policy, so the merge could contaminate
> only a downstream 2-layer trunk and never the latent itself. (4) HEADROOM IS NOT POWER. H1's
> `dv_bounds: [0.0, 1.0]` declaration is false for a DV that is a difference of mean logit
> differences and is unbounded below, so the headroom gates certify the CONTROL arm's signal
> rather than the MERGED arm's room to degrade; 'the DV had measured room to move' is withdrawn as
> a licence for a direction. WHAT `mixed` MEANS HERE, precisely: the run is INFORMATIVE and is
> emphatically NOT non_contributory -- it is the first working-readout instance of the claim's own
> named ablation, its control arm carries real signal in 8 of 8 cells, and it does rule out a
> LARGE merged degradation in a faithful topology analogue. It does not exclude the effect ARC-021
> predicts, and it did not test the substrate the claim names. IT DOES NOT BEAR ON: the
> descriptive claim that REE currently instantiates three separately-optimized channels (true, and
> verified in this run's control arm); MECH-069's scale / covariance / temporal incommensurability
> content (v3_exq_005's question, untouched here); or the biological existence proof for parallel
> cortico-striatal loops. TWO FURTHER BOUNDS, recorded rather than argued away: SPARSE's apparent
> ADVANTAGE for merging is carried by one seed -- dropping seed 101 (+0.3521) leaves mean +0.0319,
> so the defensible statement is 'indistinguishable at this power, possibly better', not 'merging
> helps'; and BIOLOGY -- the null direction is compatible with error signals being separately
> GATED rather than separately COMPUTED (Schultz 1998, a deliberate counterweight in the
> 2026-09-04 C4 pull), against which Engel 2024 / Engelhard 2019 / Groessl 2018 / Wolpert 1998
> argue for genuine channel specificity, so the biology is contested in exactly the direction this
> run points. MANIFEST OVERRIDE OWED: the flat manifest and the run-pack manifest BOTH carry
> evidence_direction `weakens` and evidence_direction_per_claim weakens/weakens, and the indexer
> has already scored that, so governance must write `mixed` onto BOTH copies together with an
> evidence_direction_note citing this artifact -- see `recommended_manifest_write`. A claims.yaml
> note alone would leave the scored direction disagreeing with the adjudication. STATUS: ARC-021
> stays `provisional` and MECH-069 stays `stable` -- one scoped, underpowered surrogate run does
> not move either, and the driver itself pre-registered that this run 'tests the
> collapse-degrades-E3 consequence, not MECH-069's scale/temporal content, so it cannot on its own
> demote a stable claim'. PENDING RETEST: the retest owed by the 2026-09-03 cluster autopsy
> (`pending_retest_after_substrate: true`, condition 'once the readout is fixed') HAS NOW RUN and
> cleared its preconditions, so the flag should be cleared on BOTH claims -- see GFLAG-0137,
> raised precisely because the IGW routine keeps re-spawning 'Retest after substrate: ARC-021'
> against a discharged condition. The remaining substrate-fidelity question (does this null
> survive on the real E1/E2/E3 stack, with a live selection role and an unfrozen encoder) is
> routed as a NEW experiment, not as an unresolved retest flag.

### Per-claim apply checklist

| claim | direction | category | status | other |
|---|---|---|---|---|
| **ARC-021** | **`weakens` -> `mixed`** (departs from the pre-registered rule -- see the note) | `standard` (already stored -- no move) | stays `provisional` | **`pending_retest_after_substrate: true -> false`**; write the note above |
| **MECH-069** | **`weakens` -> `mixed`**, narrowed in the note | `standard` (already stored -- no move) | stays `stable` | **`pending_retest_after_substrate: true -> false`**; write the note above |
| EXT-003 | not adjudicated (untagged) | unchanged | unchanged | carry the section-7 bears-on note only |

### MANIFEST OVERRIDE -- also owed, and it is not optional

The manifest's **own** pre-registered combination rule wrote `weakens`: the flat manifest and the
run-pack manifest each carry `evidence_direction: "weakens"` and
`evidence_direction_per_claim: {ARC-021: weakens, MECH-069: weakens}`, and
`build_experiment_indexes.py` has **already scored** that. So a `claims.yaml` note alone would leave
the scored direction disagreeing with this confirmed adjudication. Governance must write, on **both**
copies (`write_both_copies: true`), and rebuild the index afterwards:

| field | value |
|---|---|
| `evidence_direction` | `mixed` |
| `evidence_direction_per_claim` | `{"ARC-021": "mixed", "MECH-069": "mixed"}` |
| `evidence_direction_note` | the override paragraph in the JSON's `recommended_manifest_write` (cites this artifact and the t-interval correction) |

- flat: `evidence/experiments/v3_exq_993a_arc021_merged_channel_action_conditioned_harm_20260904T212334Z_v3.json`
- pack: `evidence/experiments/v3_exq_993a_arc021_merged_channel_action_conditioned_harm/runs/v3_exq_993a_arc021_merged_channel_action_conditioned_harm_20260904T212334Z_v3/manifest.json`

`recommended_diagnostic_evidence_adjudicated` is deliberately **not** set: `experiment_purpose` is
`evidence`, and that flag exists to mark an adjudicated-and-expected zero on a diagnostic, not to
paper over an evidence result.

---

## 14. Hypothesis-space ledger (Step 9b) -- DRAFTED ONLY, not written

Searched `hypothesis_space_registry.v1.json` (50 questions): **zero occurrences** of ARC-021,
MECH-069 or EXT-003 in the whole serialised file. The four literal `993` substring matches are
unrelated numeric fragments in other qids' text. **No existing registry question has a leg this run
adjudicates**, and no existing qid's theme covers it (the nearest neighbours,
`sd005-zself-zworld-asymmetry` and `e3_fdominance_causal_discrimination`, are about latent-split
asymmetry and E3 variance dominance respectively, not channel-topology necessity).

**Growth-restriction check:** not applicable -- no existing qid is being grown. (The only qid
carrying a non-empty `growth_restriction` is `competence_floor`, closed to further fan-out and
unrelated.)

**Recommendation: open a NEW question** `arc021_channel_separation_necessity` with **four legs, all
`alive`.** The full draft block is in the JSON under
`hypothesis_space_ledger_pending.draft_new_question`. **Still not written here** -- this block stays
**draft-for-governance** even though the artifact is confirmed; the main `/governance` session writes
the registry.

**Leg 1 (`H-surrogate-trunk-merge-degrades`) stays `alive`, amended at the Step 8 gate.** The draft had
it `falsified_at_this_scale`; that state, its `resolved_utc`, and its z-interval bound were all
consequences of the same z-vs-t error (red-team F1) and are **withdrawn**. The corrected reading:

- `evidence_direction: mixed`, `met_elimination_bar: false`, `control_passed: true`,
  `non_degenerate: true`, `resolving_runs: [v3_exq_993a_..._20260904T212334Z_v3]`.
- **Basis.** Both pre-registered criteria failed on both clauses, with H1/H2 cleared and 8/8 control
  cells positive -- but the correct t(3) intervals **[-0.204, +0.191]** (DENSE) and
  **[-0.158, +0.382]** (SPARSE) do **not** exclude this leg's own `>= 0.15` degradation in either
  condition, and joint power at -0.15 is ~12%. **The bar is not met, so the leg is not eliminated and
  not falsified.** What the run *does* establish is an **upper bound** -- roughly 0.20+ (DENSE) /
  0.16+ (SPARSE) is excluded, in this surrogate, on a working readout. Two further limits on how far
  the leg was even tested: only one of ARC-021's two falsifier DVs was read, and the arm satisfies the
  non-degeneracy precondition only in the surrogate's sense.

The three fan-out legs (`H-encoder-level-merge-degrades`, `H-real-stack-merge-degrades`,
`H-submargin-degradation-exists`) are pre-registered `alive` as drafted; `H-real-stack-merge-degrades`
now carries the section-8 repair conditions, **including repair 4** -- without it, that leg and
`H-encoder-level-merge-degrades` would be aliased in a single arm.

**Flag when applying:** leg 1 is retro-registered and adjudicated-against by the *same* artifact, so it
must not be counted as a live pre-registration in the Dimension 3/4 denominator; and
`initial_frozen_count` must be set to **4**, with `initial_frozen_count_at_registration` set to the
same value and never moved thereafter (invariant 1).

---

## 15. Learning extracted

1. **A prescribed readout repair worked, and the size is worth recording.** Reading the harm signal
   as an action-conditioned **pre-sigmoid** logit trained on the distribution it is read on, rather
   than a post-transition sigmoid, moved the control arm's max |calibration_gap| from 0.00152 to
   0.71546 (~470x) and made 8 of 8 control cells positive.
2. **The deeper defect the redesign found is a TRAINING-TARGET defect, and it generalises.**
   `causal_grid_world.py:2745` writes `grid[new_x,new_y] = 'agent'` on every committed move, so a
   head trained `h(z_t1) -> harm_label` is taught that post-harm states look *safe* (measured
   `harm_discrim_logit` 0.042 and -0.029 in DENSE). Any future driver labelling a transition outcome
   on the POST-transition observation in this environment inherits the same erasure.
3. **The dv_headroom precondition class RAN as designed on its first production use -- but validates
   less than the draft claimed.** It measured the control arm's room before the ablation arm trained
   (H1 1.52x, H2 1.79x) and let the run reach a verdict. Red-team F4 bounds it: H1 declared
   `dv_bounds: [0.0, 1.0]` for a DV that is **unbounded below**, and the class did not catch the false
   declaration. On such a DV, `floor_headroom = min(control) - lower_bound` certifies the **control**
   arm's signal, not the ablation arm's room to degrade -- so the gate must never be cited as evidence
   that a null "had somewhere to fall". PASS-path evidence only; the refusal path is still
   unexercised.
4. **RAISING a non-degeneracy floor is the correct response to a repaired instrument, not lowering
   it.** 0.02 -> 0.20 (10x), cleared in both conditions with room to spare.
5. **A precondition-cleared FAIL in the falsifying direction is not automatically a falsification,
   and TWO independent questions have to be answered before treating it as one.** (i) *Is the
   mechanism under test the claim's own mechanism, or a surrogate for it?* Here the topology was
   faithful but the modules merged were experiment-local heads over a frozen latent -- and only one of
   the falsifier's two DVs was read. (ii) *Could the design have DETECTED the predicted effect?* Here
   it could not reliably: joint power at the pre-registered -0.15 is ~12%, so FAIL is the modal
   outcome even when the claim is exactly right. The draft called this run "clean, well-powered" -- it
   was clean; it was **not** well-powered at its own pre-registered effect, and that adjective was
   doing load-bearing work in the direction argument until the red-team removed it.
6. **Pre-registering a margin buys a false-positive guarantee and pays for it in a stated blind
   spot.** Recording per-seed diffs in `interpretation.condition_detail` is what keeps it visible --
   and it is what let this autopsy report that SPARSE's apparent merged advantage is carried by one
   seed, rather than repeating the label.
7. **When a claim's `what_would_answer` names modules BY FILE, check which fidelity actually ran**
   before treating the falsifying signature as met.
8. **A Step 7b C1 fire is worth reading as "someone may already have built your NEXT experiment",**
   not only as "you may be duplicating this one" -- that is precisely what happened here. The
   corollary the red-team supplied: **read the surfaced driver at source before recommending it.** Two
   of the six repairs it needs (unpaired arms, and a detach/undetach asymmetry that would alias two
   fan-out legs in one arm) are invisible from the file's docstring and shape alone.
9. **An n=4 paired mean needs t(3) = 3.182, not 1.96 -- and the difference is not cosmetic when the
   number lands in a STORABLE field.** The draft's z-intervals understated each half-width by ~38% and
   converted an interval that **includes** the pre-registered -0.15 into one that appeared to exclude
   it, inside an `evidence_quality_note` governance copies verbatim into `claims.yaml`. Two standing
   lessons: recompute effect-size bounds with the small-sample multiplier before writing them into a
   storable field, and **always state the power at the pre-registered effect alongside the interval**
   -- that is what stops "not detected" being read as "excluded".
10. **A positional read of a preconditions list is fragile against later insertions, and it fails
    silently.** The driver computes `worst_harm_sensitivity = preconditions[0]["measured"]` (line
    1336); the *design* red-team's F6 later inserted `control_arm_coverage_complete` at the head of
    that list, so `metrics.worst_harm_action_sensitivity` records **8.0** -- the coverage count --
    instead of the true 0.11382. `validate_recording.py` reports OK because the **schema** is intact:
    a schema check cannot see a wrong **value** in a right **field**. Index preconditions by `name`.
11. **A cross-model Step 7c pass changed this adjudication's recorded direction, its stored
    effect-size bound, its `claim_alignment` cell and its fan-out repair list** -- none of which the
    authoring pass had flagged as uncertain. The two defects that mattered most (a z-interval on n=4,
    and a positional list read) were **arithmetic/mechanical**, not interpretive: exactly the class a
    second reader catches cheaply and an author re-reading their own prose does not.

---

## 16. Open doubts -- RESOLVED at the Step 8 gate (2026-09-05)

All five were put to the user after the Step 7c red-team. Recorded here with their dispositions rather
than deleted.

1. **Was `weakens` too strong?** -- **RESOLVED: yes, on both claims.** Recorded direction is `mixed`.
   The draft's own premise ("a null-to-reversed estimate, not merely an unmet bar") did not survive
   the corrected interval: with joint power ~12% at -0.15 and a t(3) interval that includes it, the
   estimate cannot carry that weight. Two further grounds the draft had not stated: one falsifier DV
   of two was read, and the precondition names a substrate the surrogate does not instantiate.
2. **Was the surrogate-vs-real-stack gap enough to move the direction?** -- **RESOLVED: it is one of
   three grounds, and `non_contributory` is still wrong.** The run is informative: first working
   readout in the family, 8/8 control cells positive, and a genuine upper bound on the effect.
   `mixed` is the reading that carries both facts at once; `non_contributory` would say the run taught
   us nothing, which is false.
3. **Clearing `pending_retest_after_substrate` on both claims** -- **RESOLVED: clear both.** The
   *stated condition* ("once the readout is fixed") is met, the readout and the harness lint entry are
   both built, the retest ran, and GFLAG-0137 asks for exactly this. Red-team F5 independently
   verified the clear as sound. The residual substrate-fidelity question belongs in a new queued
   experiment, not in a stale flag.
4. **Step 7c red-team** -- **RESOLVED: run, cross-model, verdict CONTESTED; see section 8b.** The
   Step 8 gate is this section.
5. **The substrate `amend` records a resolution rather than a gap** -- **RESOLVED, with one
   narrowing.** Close the 993 `failure_record` item (red-team F6: target met). Do **not** discharge
   `validation_owed` on it: the validation is PASS-path only, the first of six queued, and it rides on
   a `dv_bounds` declaration that is false for this DV (F4). See section 12.

**One thing the gate did NOT settle, and it is worth naming.** The red-team's corpus count for this
four-layer cell (`implementation: partial`, `measurement: adequate`) is `non_contributory` 123 /
`weakens` 18 / `mixed` 10. `mixed` is a minority reading too. It is chosen here because the run is
*genuinely* informative in a way most of that 123 are not -- but the corpus shape is a standing
invitation to ask whether this cell is being read consistently across the family.
