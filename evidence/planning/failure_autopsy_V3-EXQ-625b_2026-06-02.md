# Failure Autopsy — V3-EXQ-625b (SD-037 axis-b Phase 1b)

**Target.** V3-EXQ-625b — `v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3`
**Scope.** Single-target autopsy (not a cluster).
**Status.** Confirmed (interactive Step 8 gate completed 2026-06-02; user confirmed all three recommended routings).
**Generated UTC.** 2026-06-02T05:50:36Z
**Author.** failure-autopsy skill, REE_Working session `failure-autopsy-v3-exq-625b-20260602T055036Z`.

---

## 1. Scope and routing

- Diagnostic experiment, `claim_ids=[]`, `experiment_purpose=diagnostic`. Per Phase-3 governance, no claim is directly weighted by this manifest.
- Supersedes V3-EXQ-625 (config defect: affective-stream off on the gap4 path; 625b enables it via the 2026-06-01 `/diagnose-errors` fix).
- Predecessor V3-EXQ-620 was axis-(a) Phase 1; V3-EXQ-625b is axis-(b) Phase 1b under the SD-037 axis-(b) sustained-threat curriculum plan (REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md, 2026-06-01).
- Outcome: FAIL on plan-doc §3.4 acceptance gate (C1 + C2 PASS, C3 FAIL).

---

## 2. Facts — manifest reconstruction (no interpretation)

### 2.1 Configuration

- Seeds: 42, 7, 19 (matches plan-doc §3.1).
- Warmup: 50 episodes. Eval: 10 episodes. Steps per episode: 200.
- Substrate flags (per plan-doc §3.1): `use_pag_freeze_gate=True`, `use_gabaergic_decay=True`, `use_salience_coordinator=True`, `use_lateral_pfc_analog=True`, `use_amygdala_analog=True`, `use_bla_analog=True`, `use_cea_analog=True`, `use_dacc=True`, `gap4_operating=True`. Broadcast OFF (all four MECH-281 cascade gains 0.0).
- `affective_harm_stream_enabled: true` (the 2026-06-01 /diagnose-errors fix that distinguishes 625b from 625).
- Env-overlay delta vs V3-EXQ-620: `scheduled_external_hazard_enabled=True`, `interval=20`, `prob=0.7`, `adjacent_only=True`, `hazard_harm=0.2`, `proximity_harm_scale=0.2`. All other ENV_FISHTANK_KWARGS defaults preserved.

### 2.2 Acceptance gate result (plan-doc §3.4)

| Criterion | Required | Achieved | Verdict |
|---|---|---|---|
| C1 curriculum_firing (external_hazard_event_count > 0) | 3/3 seeds | 3/3 (42 → 10, 7 → 45, 19 → 6) | **PASS** |
| C2 z_harm_a non-zero (zero_fraction < 1.0) | ≥2/3 seeds | 3/3 (all zero_fraction = 0.0) | **PASS** |
| C3 sustained window (≥1 run of ≥10 consecutive ticks with z_harm_a > 0.4) | ≥2/3 seeds | 1/3 (seed 7 only) | **FAIL** |

Overall: `acceptance_pass: false`.

### 2.3 Per-seed pattern — the load-bearing observation

| Seed | total_eval_steps | action_counts | z_harm_a_norm mean (min..max) | z_harm_a_norm p99 | sustained_runs | external_hazard_events |
|---|---|---|---|---|---|---|
| 42 | 312 | {3: 281, 2: 20, 1: 10, 0: 1} | 0.323 (0.313..0.339) | 0.335 | 0 | 10 |
| 7 | 1413 | {0: 1409, 1: 4} | 0.435 (0.431..0.457) | 0.447 | 1 (length 1413) | 45 |
| 19 | 191 | {1: 7, 0: 172, 3: 7, 2: 5} | 0.335 (0.329..0.355) | 0.351 | 0 | 6 |

Three seeds, three monomorphic action distributions, three different attractors. Seeds 42 and 19 stay structurally below the 0.4 threshold (p99 0.335 / 0.351 — never crosses). Seed 7 stays structurally above (p10 0.432 — never falls below).

### 2.4 Side observations

- `dacc_pe` mean = 0.0 across all three seeds (zero_fraction = 1.0 universally). Structural instrumentation gap, predates 625b — same dead-channel signature noted on the V3-EXQ-620 predecessor manifest.
- `pag_sustained_product` zero_fraction: seed 42 = 1.0, seed 7 = 0.16, seed 19 = 1.0. Non-zero only in seed 7, where it's a direct consequence of seed 7's continuously-above-threshold z_harm_a.
- `cea_low_freq_magnitude` non-zero across all seeds (mean 0.07–0.09, well below the 0.5 CeA `fast_route_threshold`).
- `bla_pe_magnitude` non-zero across all seeds (mean 0.30–0.43); BLA PE channel alive.

### 2.5 Which criterion failed

C3 (discrimination criterion). C1 and C2 (absolute / negative-control criteria) pass cleanly. The substrate-ceiling fingerprint "absolute / negative-control passes, discrimination fails" applies — but the discrimination failure is one architectural layer downstream of the affective-stream layer the curriculum was designed to engage (see §5).

---

## 3. Claim-layer mapping

`claim_ids=[]`. No claim is directly weighted.

The plan-doc carries SD-037 / MECH-280 / MECH-281 as ultimate downstream targets via the chip sequence Phase 2 (recalibration block) → Phase 3 (verification diagnostic) → Phase 4 (V3-EXQ-483f). 625b is Phase 1b — two phases upstream of any claim-weighting measurement. The FAIL therefore does not alter the SD-037 substrate_ceiling diagnosis from the 2026-05-31 V3-EXQ-483e autopsy. Tag accuracy verified: `claim_ids=[]` is correct given the diagnostic scope (not inherited from a predecessor that should have carried tags).

---

## 4. Biological-reference triage

### 4.1 Closest mammalian / human / connectome reference

PAG sustained-threat integration: Bandler & Shipley 1994 (columnar PAG organization), McNaughton & Corr 2004 (BIS sustained-threat axis), Carter 2009 (LH→PAG orexin projection — the SD-037 anchor). Surrounding systems the reference depends on in real brains: hippocampal place-/episode-level orienting, amygdalo-cortical valuation, BLA / CeA arousal cascade, motor cortex / striatal action selection capable of expressing dynamic behavioural sequences (orient → vigilance → freeze/escape → return → re-engage).

### 4.2 Biological translation vs formal-definition import

Not a formal-definition import. The plan-doc's design is biology-anchored. Divergence is at the **measurement-design layer**, not the mechanism layer.

The C3 acceptance criterion ("≥1 run of ≥10 consecutive ticks with z_harm_a > 0.4") is too crude. It cannot distinguish:
- **Biological intent**: PAG sees dynamic threat crossings — z_harm_a rises across the 0.4 duration_input_threshold, the duration integrator accumulates, behaviour transitions, z_harm_a falls back, the cycle repeats.
- **Literal-pass under catatonic lock**: z_harm_a is pinned continuously above 0.4 for the entire eval window because the agent has frozen in a monomorphic action loop that holds it in a high-threat configuration. The "sustained run" criterion is satisfied trivially because the entire eval is one run.

Seed 7 demonstrates the latter: 1413 consecutive ticks of action 0, z_harm_a min 0.431 / max 0.457, one "sustained run" of length 1413 — counts as 1/3 toward C3 but is biologically degenerate. Seeds 42 and 19 demonstrate a different pathology: monomorphic action lock that holds z_harm_a below 0.4 throughout, producing 0 sustained runs.

### 4.3 Lit-pull status

`evidence/literature/targeted_review_orexin_kinetics/` already covers the SD-037 mechanism layer (synthesis.md, 7 entries, lit_conf 0.789, supports-direction). No new lit-pull commission. The plan-doc's biological grounding is sound; what failed is the measurement criterion's faithfulness to the dynamic-sequence biology.

### 4.4 Missing-dependency signature?

Yes — the failure resembles what would happen biologically if a known dependency of the reference mechanism were absent: **behavioural-diversity generation**. In intact mammals, sustained threat produces dynamic action sequences because the behavioural repertoire is diverse and competitive (PFC + striatal + cortical loops generating multiple candidate actions, with one winning the gating contest per moment). In 625b, all three seeds collapse to one repeated action. The downstream pathology then becomes "PAG never sees dynamic z_harm_a crossings because the agent never behaviourally transitions" — exactly what we observe.

This is the same monostrategy / behavioural-diversity gap that ARC-065 (SP-CEM main-path), SD-056 (action-conditional contrastive E2), MECH-341 (E3 score diversity preservation), and scaffolded_sd054_onboarding (Phase 0/1/2 onboarding curriculum) are already addressing. V3-EXQ-625b is **corroborating evidence on an existing substrate gap**, not a novel substrate need.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a | diagnostic, claim_ids=[] |
| Biological reference | partial | PAG sustained-threat literature solid; C3 criterion drifts from dynamic-sequence biology by treating "always above" as equivalent to "dynamic crossings" |
| Prerequisites | **missing — behavioural diversity** | ARC-065 + SD-056 + MECH-341 + scaffolded_sd054_onboarding behavioural-diversity substrate not yet validated as effective under this env config; monostrategy collapse persists |
| Implementation | complete (curriculum + affective stream); collapse downstream | env curriculum fires per C1; affective stream lights up per C2; policy collapses monomorphically — same behavioural-diversity hole substrate_queue is already tracking |
| Environment | adequate at hazard layer | seed 7 proves env CAN sustain z_harm_a above 0.4 — env is not the bottleneck |
| Measurement | **inadequate at C3** | C3 cannot distinguish PAG dynamic engagement (biological intent) from catatonic-lock literal-pass (seed 7) |
| Integration | broken at policy layer | upstream env signal lands, downstream policy collapses |
| Scale | adequate | budget and magnitudes appropriate |

### 5.1 Recommended `epistemic_category`

**substrate_ceiling.** Not at the affective-stream layer (axis (b) DID lift z_harm_a — seed 7 is proof). Ceiling is one layer downstream of where the SD-037 axis-(b) plan-doc was looking: the behavioural-diversity substrate cluster. This autopsy is corroborating evidence on the existing substrate gap, NOT a novel substrate need.

(Note: this recommendation applies to the **autopsy artifact's epistemic framing**, not to any claim's `epistemic_category` field — the manifest carries `claim_ids=[]` so no claim is reclassified.)

### 5.2 Why plan-doc §5 routings do NOT fit

The plan-doc §5 fallbacks all assume the env is failing to sustain threat:
- §5.1 (z_harm_a pinned at zero despite curriculum firing) — falsified: zero_fraction = 0 in all three seeds.
- §5.2 (z_harm_a lifts but no sustained runs) — partially applicable to seeds 42/19, but seed 7's 1413-step sustained run falsifies the "env can't sustain" reading.
- §5.4 (env-kwarg surface exhausted → axis (c) sustained-threat scheduler) — falsified: the env DOES sustain (seed 7).

A heavier env curriculum will not fix this. The seed-7 result proves the env is fully capable; a sharper scheduler that forced even more sustained windows would only deepen the lock signature without resolving it.

---

## 6. Cluster pattern

Not a multi-target cluster autopsy. The single-target FAIL is informative on its own.

However, V3-EXQ-625b's failure shape **adds an axis to an existing cross-claim pattern**: monostrategy collapse under sustained external threat. The existing corpus characterizes monostrategy under OFF-baseline (V3-EXQ-543/590a/591/598/603/610 substrate-uniform z_goal-zero family, V3-EXQ-483 catatonic-lock chain). 625b shows the lock holds under sustained-threat env too. The behavioural-diversity substrate (ARC-065 / SD-056 / MECH-341 / scaffolded_sd054_onboarding) must therefore deliver diversity under **both** quiescent and sustained-threat env conditions to clear the cluster.

---

## 7. Learning extracted

1. **The 625b env config is sufficient at the affective-stream layer.** Plan-doc §1.2 sensitivity rationale is empirically validated by seed 7 (mean z_harm_a = 0.435 sustained 1413 ticks).
2. **The C3 acceptance criterion is too crude.** It cannot distinguish biological PAG dynamic engagement from catatonic-lock literal pass. A redesigned criterion needs explicit dynamic-crossings detection — e.g. require ≥1 below→above AND ≥1 above→below transition per seed, OR cap "sustained run" length so frozen full-eval runs are ineligible, OR require sustained-run density as a fraction of eval-window length below a threshold.
3. **Monostrategy collapse persists under sustained threat.** Three seeds, three lock attractors (action 3 only / action 0 only / action 0 dominant). Eval-length divergence 191 / 312 / 1413 confirms different attractors per seed, not stochastic exploration. Same shape as the broader behavioural-diversity cluster the substrate_queue is already chasing — adds the sustained-threat axis.
4. **`dacc_pe` = 0 is a structural instrumentation gap** independent of axis (b). Same dead-channel signature on V3-EXQ-620 predecessor. Surface separately to next governance cycle as informational observation; not load-bearing for the C3 FAIL.

---

## 8. Routing — confirmed at the Step 8 interactive gate

User-confirmed routing (2026-06-02T05:50:36Z, AskUserQuestion):

1. **Implement-substrate AMEND on behavioural-diversity cluster** (primary routing).
2. Evidence_direction kept at `non_contributory` (the runner-set value is correct).
3. SD-037 status unchanged — substrate_ceiling diagnosis at the consumer-input-threshold layer stands; 625b is upstream of the SD-037 gating layer.

### 8.1 Substrate_queue AMEND target

**Target SD ID:** `scaffolded_sd054_onboarding` (status: `amend_pending`).

Rationale: This entry is already the active behavioural-diversity / goal-pipeline training-regime substrate work; the V3-EXQ-603d autopsy yesterday (2026-06-01) routed an amend here, leaving `amend_pending` for the next implementation step. 625b's monostrategy-under-sustained-threat finding adds a failure record alongside the 603d failure record. Same substrate, additional axis of evidence.

Alternative target considered: `ARC-065` (`phase_1_implemented`) or `MECH-341` (`amend_implemented_pending_validation`). Both are behavioural-diversity layer but lack an active `amend_pending` slot to attach a failure_record to. `scaffolded_sd054_onboarding` is the live amend node.

### 8.2 Failure-record entry (for governance to write to substrate_queue.json)

```json
{
  "run_id": "v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3",
  "experiment_type": "v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat",
  "metric": "C3 sustained-window 1/3 FAIL via monostrategy collapse: three seeds → three monomorphic action attractors (seed 42 action 3 only, seed 7 action 0 only for 1409/1413 steps, seed 19 action 0 dominant). z_harm_a structurally locked below 0.4 in seeds 42/19 and continuously above 0.4 in seed 7. Eval-length divergence 191/312/1413 confirms policy-attractor collapse, not stochastic variation. Env curriculum proven sufficient at affective-stream layer (seed 7); behavioural-diversity layer is the load-bearing gap.",
  "target": "Behavioural-diversity substrate must deliver dynamic action sequences under sustained-threat env config so PAG duration integrator sees genuine z_harm_a crossings (≥1 below→above AND ≥1 above→below transition per seed) rather than monomorphic action lock at a single threat-level attractor."
}
```

### 8.3 Recommended companion action — sharpen C3 criterion

Independent of the substrate amend, the SD-037 axis-(b) Phase 1b script should be redesigned with a sharper C3 criterion before any subsequent re-run. Suggested form:
- C3a: ≥1 above→below transition per seed (i.e. excludes seed-7-style continuously-elevated frozen pass).
- C3b: ≥1 sustained run of ≥10 ticks per seed (the original C3).
- Joint: C3 PASS = C3a AND C3b on ≥2/3 seeds.

This is a /queue-experiment redesign, not part of this autopsy. Recommend governance schedule it after the behavioural-diversity substrate amend lands and `scaffolded_sd054_onboarding` re-validates downstream behavioural diversity.

### 8.4 What governance writes

- **substrate_queue.json:** append the failure_record_entry in §8.2 to the existing `scaffolded_sd054_onboarding` entry's `failure_records` (alongside the 603d record from yesterday's autopsy).
- **claims.yaml:** no edits. claim_ids=[] on the manifest; SD-037 / MECH-280 / MECH-281 status unchanged.
- **review_tracker.json:** mark V3-EXQ-625b reviewed (next /governance cycle).
- **manifest:** no `evidence_quality_note` or `evidence_direction_note` edit needed beyond the runner's existing `non_contributory` value. (Optional: a one-line `evidence_direction_note` pointing at this autopsy artifact would be helpful but is not load-bearing.)

### 8.5 Recommended `evidence_quality_note` text (for an optional manifest annotation — NOT to be written by this autopsy)

> [2026-06-02 failure-autopsy V3-EXQ-625b]: FAIL on plan-doc §3.4 C3 (sustained-window, 1/3). C1 + C2 PASS. Substrate-ceiling at one layer downstream of the affective-stream curriculum: behavioural-diversity collapse to monomorphic action attractors persists under sustained-threat env (three seeds, three locks; eval-length divergence 191/312/1413). Seed 7 frozen on action 0 for 1409/1413 steps produces a literal-pass C3 that is biologically degenerate. Routed to scaffolded_sd054_onboarding substrate_queue amend as corroborating failure record alongside V3-EXQ-603d. SD-037 / MECH-280 / MECH-281 status unchanged (this FAIL is upstream of their gating layer). Companion follow-on: redesign C3 to distinguish dynamic crossings from continuous-elevation lock. Artifact: evidence/planning/failure_autopsy_V3-EXQ-625b_2026-06-02.{md,json}.

---

## 9. Cross-references

- Manifest: `REE_assembly/evidence/experiments/v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat_20260601T181233Z_v3.json`
- Script: `ree-v3/experiments/v3_exq_625b_sd037_axis_b_phase1b_consumer_input_distributions_sustained_threat.py`
- Plan-of-record: `REE_assembly/evidence/planning/sd_037_axis_b_sustained_threat_curriculum_plan.md` (2026-06-01)
- Predecessor autopsy chain: V3-EXQ-483d (2026-05-30), V3-EXQ-483e (2026-05-31) — SD-037 substrate_ceiling lineage.
- Diagnose-errors session that produced 625b (and 620b): TASK_CLAIMS `diagnose-errors-v3-exq-625-20260601T174337Z` (2026-06-01).
- Sibling autopsy in flight: V3-EXQ-592f (TASK_CLAIMS `failure-autopsy-v3-exq-592f-20260602T055130Z`) — MECH-090 R-c release authority; orthogonal target, no collision.
- Substrate-queue target: `REE_assembly/evidence/planning/substrate_queue.json` → `scaffolded_sd054_onboarding` (status `amend_pending`).
- Sibling failure-record entry: V3-EXQ-603d on `scaffolded_sd054_onboarding` (2026-06-01).
