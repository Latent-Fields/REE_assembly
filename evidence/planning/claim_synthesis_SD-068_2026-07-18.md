# Claim synthesis — SD-068 (consolidation-pipeline lesion harness)

- **Generated (UTC):** 2026-07-18T18:19:23Z
- **Session:** `gracious-bassi-721580` (SD-068 claim-synthesis decomposition)
- **Trigger:** `granularity_debt_trigger` (`fires: true`, `n: 2`) in
  `evidence/planning/failure_autopsy_SD-068-rem-fanout-cluster_2026-07-18.json`
  (REE_assembly `master` `deda5e17ed`), `handoff_status: recommended_not_yet_run`.
- **Status:** **APPROVED, REGISTRATION DEFERRED.** All four children approved by the user at
  the Step-7 gate on 2026-07-18, together with the umbrella-and-amend-title fate for SD-068.
  Registration into `claims.yaml` is **deliberately held** pending the concurrent
  duplicate-key dedup pass (§6.1) and is carried by a follow-on chip. Nothing in
  `claims.yaml` has been edited by this session.
- **Verdict:** the cluster **CLEARS** the granularity-debt bar. Decompose. This is **not**
  a demotion recommendation — SD-068 is coarse, not wrong.

---

## 1. Cluster assembled

All runs bearing on SD-068, in order:

| Run | Phase under test | Outcome | Failure signature |
|-----|------------------|---------|-------------------|
| V3-EXQ-778b (n=2) | all three | superseded by 778c | — |
| V3-EXQ-778c (n=8) | all three | FAIL / weakens | `sws` content-free **by algebraic cancellation** in a log-ratio; `rem` degenerate at both clamp rails; `nrem` **content-contingent (works)** |
| V3-EXQ-778d (n=8) | rem | FAIL (control rehabilitated) | readiness-anchor **specification defect** — one-rail predicate against a two-rail degeneracy, unmeetable by construction |
| V3-EXQ-778e (n=8) | rem | FAIL / weakens | de-clamped readout **still content-free** on every non-degenerate seed (0.999 / 0.998 / 0.326 vs a 0.25 ceiling) |
| V3-EXQ-778f (n=8) | rem (generative gain) | PASS / weakens | `rem_generative_gain` **flat in content scale** (delta −0.0097 vs a 0.05 bar, residual trend sign-inverted) |
| V3-EXQ-778g (n=8) | sws (rebuilt) | PASS / supports | none — rebuilt `_sws_pattern_completion` clears C1 at 0.1495, 8/8 |

Autopsy artifacts read: `failure_autopsy_V3-EXQ-778c_2026-07-18.{md,json}`,
`failure_autopsy_SD-068-rem-fanout-cluster_2026-07-18.json`,
`failure_autopsy_V3-EXQ-778g_2026-07-18.*`. Architecture doc:
`docs/architecture/sd_068_consolidation_lesion_harness.md` (incl. the ~361-369 partial
re-widening block and the NARROW-SUPPORTS caution).

**Registry state note.** The SD-068 `evidence_quality_note` in `claims.yaml` currently
carries the 778c narrowing and the 778g partial re-widening, but **not** the REM cluster's
`recommended_evidence_quality_note_SD_068`. The governance session that owed the REM writes
(`reverent-chatterjee-5f187e`, landed `1ded9267a2`) applied them to the three run manifests,
`review_tracker.json` and the architecture doc — **not** to `claims.yaml`. That note is
still owed and is *independent of this proposal*; it should land whether or not the
decomposition is approved.

---

## 2. Discrimination gate (skill Step 3) — the load-bearing filter

Classifying each signature. **Two of the four are excluded**, and saying so is the point of
the gate: a forced decomposition on those alone would manufacture a claim from a
measurement bug.

**EXCLUDED — test-design debt (fix/retire the test, not the claim):**

- **778c `sws` algebraic cancellation.** `denoising_snr_db = 10*log10(signal/noise)` with
  `noise_power` identical across arms at every sigma → the content term differentiates
  away. A badly chosen readout *formula*, and it was correctly handled **as** test-design
  debt: the readout was rebuilt (`_sws_pattern_completion`) and re-validated by 778g at the
  *same* C1 ceiling that excluded it. Signature resolved; contributes nothing to a
  granularity signal.
- **778d readiness-anchor predicate.** The autopsy itself types this
  `specification_defect` / `readiness_anchor_predicate_narrower_than_anchored_degeneracy`,
  with `recommended_substrate_queue_entry.action: none` and a ledger-hygiene re-run routed
  as V3-EXQ-778h. Pure instrument specification error. Excluded.

**EXCLUDED — substrate-not-ready:** none. 778d self-routed `substrate_not_ready_requeue`
and that label was **REJECTED** at adjudication ("a specification defect in the readiness
anchor, not a substrate-readiness fact"). `prerequisites: present` on every leg. Nothing in
this cluster is substrate-blocked.

**EXCLUDED — vacuous criterion:** none survives as vacuous. `criteria_non_degenerate` is
true throughout; every leg carried a **passing positive control**; the single degeneracy
flag (778d C1) traces entirely to the excluded specification defect and the control was
rehabilitated on the corrected both-rails predicate against **bit-identical floats across
three independent runs**.

**SURVIVING — genuine, non-degenerate, substrate-ready:**

1. **778e** — de-clamping changed the *scale* (9143 → ~1.0) but not the *pattern*; the same
   5 seeds saturate, and on every non-degenerate seed the ratio is above the 0.25 ceiling.
   The degeneracy is **not** a units artifact. The REM precision quantity does not track
   content.
2. **778f** — a clean non-degenerate PASS as shipped: `rem_generative_gain` attenuates 8/8
   at *every* content scale including zero. The attenuation is real; it is **content-free**.

**Is that a single clean falsification rather than granularity debt?** This is the honest
close call, and the answer turns on scope. Read narrowly, 778e and 778f converge on one
finding (*the REM leg is content-free*) — which alone would route to governance, not here.
But the granularity signal is not internal to the REM leg; it is the **heterogeneity of
fates across the phases that SD-068 binds into one contract**:

- `nrem` — content-contingent natively, works as first built (0.1445, 0/8 confounded);
- `sws` — broke, and was **repairable** by reformulating the readout (0.1495, 8/8);
- `rem` — broke differently, and is **not repairable as conceived** (two independent legs,
  two design axes, no substrate-queue entry proposed by any of them);
- **staging order** — untestable in principle while any ranked leg lacks an interpretable
  readout, and unsupported after four runs.

Four parts, four different epistemic fates, **one claim**. The registry symptom is visible
directly: SD-068's `evidence_quality_note` has been narrowed, partially re-widened, and
re-narrowed *within a single day*, and now runs to ~110 lines of scope-surgery — including
an explicit self-correction of a phrase that a prior amendment had made stale. That churn
is the cost of a single scope-carrier standing in for four separable ones.

**GATE VERDICT: PROCEED.** ≥2 distinct, genuine, non-degenerate, substrate-ready
signatures, and the decomposition is *evidence-discharging rather than tail-inflating* —
three of the four proposed children carry already-collected, already-adjudicated evidence.

---

## 3. The common thread (skill Step 4)

> **SD-068 assumes "per-phase output-quality readout" names one kind of thing, instantiable
> three times. It does not. Content fidelity is scorable only where the phase's output is a
> FIRST-ORDER content-bearing quantity (NREM transfer, SWS retrieval margin); the REM phase's
> output is PRECISION — a second-order quantity over representations — which is content-free
> by type, not by construction defect, and whose damage is therefore only readable through a
> DOWNSTREAM behavioural consequence.**

This explains both surviving signatures at once, and explains why de-clamping (778e) could
not help: there was no content signal to recover. It also explains the SWS repair's shape —
what fixed `sws` was moving from a *power-ratio* to a *retrieval-margin* formulation, i.e.
making it a first-order content measure. The claim's own `functional_restatement` already
half-notices the substrate fact ("the three phases operate on DISJOINT state") but draws no
consequence for readout *type*.

---

## 4. Literature grounding (skill Step 5) — commissioned and returned

Full pull run this session. Per-question verdicts:

- **Q1 — how REM vs SWS/NREM benefit is measured. SUPPORTS (strongly).** The field already
  has this asymmetry. SWS/NREM benefit is operationalised as first-order content fidelity
  (recall accuracy, TMR cueing deltas; Cairney et al. 2014, 2016). REM benefit is
  characteristically measured through *integrative/downstream* outcomes — unitisation,
  assimilation into remote networks, rule/schema abstraction (Walker & Stickgold 2010,
  *Nat Rev Neurosci*); Brodt et al. 2023 (*Neuron*) assign content-transfer machinery to
  SWS and give REM a balancing/renormalisation role. The field measures REM behaviourally
  because it has not found a content-fidelity quantity REM moves.
- **Q2 — does REM do precision recalibration rather than content restoration? MIXED.**
  Theory-level support is strong: Hobson, Hong & Friston 2014 (dreaming refines the
  generative model by minimising *complexity*, with accuracy explicitly **not** entrained
  in dreaming); Hopkins 2016 (free energy = complexity − accuracy; REM reduces complexity,
  resembling Bayesian model selection). Best empirical proxy: van der Helm et al. 2011,
  *Curr Biol* — REM depotentiates amygdala reactivity while the memory content is retained
  (the cleanest biological instance of "REM adjusts weighting on a representation, not the
  representation"). Renormalisation frame: Tononi & Cirelli 2014 (SHY). **Flag:** "precision"
  in the strict Bayesian sense is applied to REM *theoretically*; no located paper measures
  a REM-specific precision parameter empirically. This is a **defensible formal import with
  partial biological warrant**, and the child claim below must say so.
- **Q3 — are second-order quantities non-measurable by content-fidelity scoring?
  SUPPORTS**, as an established methodological principle from metacognition rather than
  sleep. Maniscalco & Lau 2012: naive confidence-based type-2 measures are confounded by
  type-1 sensitivity and bias; a dedicated estimator (meta-d′) is required. Mazancieux
  et al. 2020: metacognitive efficiency correlates across domains *even where first-order
  performance does not*. **A raw precision quantity tracking noise rather than content is
  the expected signature of an unnormalised type-2 measure** — i.e. our 778e result is what
  the methodology literature predicts, not an anomaly.
- **Q4 — ordering of phase vulnerability under diffuse insult. MIXED / regime-conditional.**
  Dissociable phase vulnerabilities are well attested (Ohayon et al. 2004 meta-analysis;
  Sharon et al. 2025 slow-wave synchrony in prodromal AD; Cho et al. 2025), but the ordering
  **inverts with insult duration** in the rebound-priority designs (Rechtschaffen et al.
  1999: short TSD gives both SWA and REM rebound; chronic TSD gives large REM rebound with
  *no* high-amplitude NREM rebound). **There is no single canonical degradation sequence.**
  A staging-order claim must therefore be stated *conditional on insult regime* — which
  SD-068's current formulation does not do, and which is an independent reason to separate
  it from the instrument claims.

Nothing in the pull contradicts the decomposition. The one flagged import (Q2) is confined
to the naming of REM's operation, not to the type-fact that drives the decomposition.

---

## 5. Proposed decomposition

### Fate of SD-068 — **UMBRELLA, narrowed** (not superseded, not demoted)

SD-068 is retained and narrowed to what it actually established and what actually worked:
the **harness design decision** — a uniform RMS-scaled Gaussian per-phase diffuse-damage
knob plus injected-content scoring at the experiment layer, zero `ree_core` change. Its
per-phase instrument assertions and its staging-order non-vacuity carrier move to the
children below. Requires a **title amendment**, since the current title names the staging
order as a non-vacuity carrier — the specific binding that holds the per-phase results
hostage.

### Child A — `MECH-462` *(provisional id; re-check max at registration)*

- **claim_type:** `mechanism` · **subject:** `sleep.consolidation_readout_order`
- **Claim:** Consolidation-phase damage is content-scorable only where the phase's output is
  a first-order content-bearing quantity (NREM inter-store transfer; SWS retrieval margin).
  A phase whose output is a second-order quantity over representations — REM precision /
  confidence recalibration — is content-free by type, and its damage is readable only
  through a downstream behavioural discrimination consequence, never through a statistic
  computed on the precision quantity itself.
- **`what_would_answer`:** Build a meta-d′-analogue downstream readout for the REM phase
  (does the agent's post-REM confidence separate its own correct from incorrect retrievals?)
  and run it on the *same cells* as V3-EXQ-778e. Child A is **supported** if the downstream
  readout is content-contingent (`null_slope_ratio <= 0.25`, `ceiling_inside_ci95` false,
  ≥6/8 seeds) while the direct precision readout on those same cells remains above 0.25.
  **Refuted** if the downstream readout is *also* content-free (the phase carries no
  recoverable damage signal at all), or if a direct precision-quantity readout can be made
  content-contingent (the type-fact is false and this was construction defect after all).
- **`depends_on`:** SD-068, MECH-123, MECH-204
- **`epistemic_category`:** `measurement_gap`
- **Lit grounding:** Q1 (Walker & Stickgold 2010; Brodt et al. 2023) + Q3 (Maniscalco & Lau
  2012; Mazancieux et al. 2020). Register with the Q2 formal-import flag explicit.
- **Explains:** 778c `rem` both-rail degeneracy, 778e de-clamped content-freeness, 778f
  generative-gain content-freeness — all three as one type fact rather than three bugs.

### Child B — `SD-071` *(provisional)*

- **claim_type:** `design_decision` · **subject:** `sleep.first_order_phase_readouts`
- **Claim:** The NREM slot-filling and SWS pattern-completion legs of the harness are
  validated content-contingent instruments: injected-content transfer fidelity (`nrem`) and
  cosine retrieval margin against injected prototypes probed with the unscaled base (`sws`).
- **`what_would_answer`:** Already largely discharged — `nrem` `null_slope_ratio` 0.1445,
  CI [0.1438, 0.1451], 0/8 confounded (778c); `sws` 0.1495, sd 0.0218, CI [0.1344, 0.1646],
  `ceiling_inside_ci95` false, 8/8, plus the C3 content-scale ladder at spread 0.1108 >
  0.01 floor (778g). Remaining condition for promotion: one **non-diagnostic** run tagging
  the claim, since both supporting runs are `experiment_purpose: diagnostic` and do not
  weight governance confidence.
- **`depends_on`:** SD-068, MECH-120, MECH-121
- **`epistemic_category`:** `measurement_validated`
- **Purpose:** lets two already-earned instrument-validity results settle as their own claim
  instead of being repeatedly re-scoped inside SD-068's note.

### Child C — `SD-072` *(provisional)*

- **claim_type:** `design_decision` · **subject:** `sleep.rem_downstream_damage_readout`
- **Claim:** The REM leg's damage readout must be replaced by a downstream behavioural
  discrimination measure (a meta-d′-analogue over post-REM retrieval confidence). The direct
  `calibration_error` readout and the `rem_generative_gain` contrast are retired as
  functional-damage instruments — the former content-free after de-clamping, the latter flat
  in content scale.
- **`what_would_answer`:** the same instrument-validity gate applied to the replacement:
  `null_slope_ratio_rem_downstream <= 0.25` with `ceiling_inside_ci95` false at n=8, plus a
  pre-registered content-scale ladder (as 778g C3). Refuted if the replacement fails the
  same C1 ceiling that retired its predecessor — **symmetry of criterion is required**, per
  the 778g re-admission precedent.
- **`depends_on`:** SD-068, MECH-462 *(Child A)*, MECH-123
- **`epistemic_category`:** `substrate_conditional`
- **Note:** this is the build child. It is the concrete substrate consequence of Child A and
  the only proposed child that asks for new implementation.

### Child D — `SD-073` *(provisional)*

- **claim_type:** `design_decision` · **subject:** `sleep.consolidation_staging_order`
- **Claim:** The reverse-dependency **staging order** — that under uniform diffuse damage the
  three phases fail in dependency order rather than uniformly — is a distinct, separately
  testable cross-phase ranking claim, **conditional on the insult regime**, and is
  establishable only once all three phases carry validated content-contingent instruments.
- **`what_would_answer`:** re-run `run_staged_sweep` with all three validated instruments
  (SD-071 `nrem`+`sws` plus SD-072's REM replacement), at a **declared insult regime**
  (acute single-sweep vs chronic repeated-sweep — the lit requires this be stated, since the
  biological ordering inverts with insult duration). Supported if the damage-tolerance rank
  order matches the reverse-dependency prediction on ≥6/8 seeds within a declared regime;
  refuted if the order is unstable across seeds or inverts within one regime. Explicitly
  **not** answerable by any run in which a ranked leg lacks an interpretable readout.
- **`depends_on`:** SD-068, SD-071, SD-072, MECH-168, INV-047, MECH-169
- **`epistemic_category`:** `substrate_conditional`
- **Purpose — the main structural payoff.** The staging order is currently named in SD-068's
  *title* as a non-vacuity carrier, so per-phase instrument results cannot settle while it is
  unsupported, and it cannot be established while any leg lacks a readout. Separating it
  converts that deadlock into an ordinary `depends_on` edge. The existing prose gate ("staging
  order is a CROSS-phase ranking and cannot be supported while one of the three ranked legs
  has no interpretable readout") becomes structural rather than a paragraph that each
  amendment has to restate.

### What does NOT change

- No status, confidence, promotion or demotion change on SD-068, MECH-168, INV-047 or
  MECH-169. All supporting runs are `experiment_purpose: diagnostic`.
- The **MECH-121 hold** (`hold_pending_v3_substrate`) stays RESPECTED; no child tags it.
- The `rem_generative_gain` **attenuation finding stands** (0.149, 8/8 attenuating). Only the
  "correction needs an intact seed" gloss is retracted, and that retraction has already
  landed via the governance session.
- `hypothesis_space_registry.v1.json` is **not touched** (GOV-FROZEN-1: `/failure-autopsy`
  Step 9b is its single producer).

---

## 6. Open items for the approval gate

1. **Concurrency conflict on `claims.yaml`.** Session `jovial-joliot-9f904b` holds an active
   claim on `REE_assembly/docs/claims/claims.yaml` (claimed 2026-07-18T18:12:26Z, "adjudicate
   and merge 25 claims carrying duplicate top-level keys"). Registration must not race that
   dedup pass. Recommend registering **after** it lands, and re-reading the insertion region
   immediately before editing.
2. **Id allocation.** `SD-071` / `MECH-462` are the next free ids as of
   2026-07-18T18:19Z (max `SD-070`, `MECH-461`). Re-check max + recent `git log` at write time.
3. **Owed independently of this proposal:** the REM cluster's
   `recommended_evidence_quality_note_SD_068` still needs to reach SD-068's
   `evidence_quality_note` in `claims.yaml`. Not this skill's write.

---

## 7. Approval record (skill Step 7)

Interactive gate, 2026-07-18, session `gracious-bassi-721580`.

| Item | Decision |
|------|----------|
| Child A — `MECH-462` readout-type mechanism | **APPROVED** |
| Child B — `SD-071` first-order instruments validated | **APPROVED** |
| Child C — `SD-072` REM downstream discrimination readout | **APPROVED** |
| Child D — `SD-073` staging order separated | **APPROVED** |
| SD-068 fate | **Umbrella + AMEND TITLE** — narrow to the harness design decision; strike the staging-order non-vacuity carrier from the title |
| Registration timing | **DEFERRED** — wait for the `jovial-joliot-9f904b` duplicate-key dedup pass to land before touching `claims.yaml` |

**Registration checklist for the follow-on session** (nothing below has been done):

1. Confirm `jovial-joliot-9f904b` is closed and its dedup landed on `origin/master`.
2. Take a `TASK_CLAIMS` claim covering `docs/claims/claims.yaml`,
   `docs/assets/data/claims.json`, and this file.
3. Re-check max ids (`SD-*`, `MECH-*`) in the file **and** recent `git log` — the
   provisional ids here were free at 2026-07-18T18:19Z only.
4. Register all four children as `status: candidate`, each with `what_would_answer`,
   `depends_on`, `epistemic_category` and a `location` architecture-doc stub, per §5.
   Re-read the insertion region immediately before editing.
5. Amend the SD-068 title (strike staging order as a non-vacuity carrier) and wire the
   umbrella `depends_on` relationships.
6. `python scripts/build_claims_json.py` — confirm the four children appear and the stance
   tally moved.
7. Commit via `scripts/ree_commit.py`, verify with `git show --stat HEAD`, push `HEAD:master`.

No status, confidence, promotion or demotion change is authorised by this approval — all
supporting runs are `experiment_purpose: diagnostic`. The MECH-121 hold stays RESPECTED.
