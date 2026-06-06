# Failure Autopsy — V3-EXQ-647 (modulatory_authority_reuse_split)

- **Generated (UTC):** 2026-06-06T20:08:29Z
- **Session:** failure-autopsy-V3-EXQ-647-20260606T2002Z
- **Scope:** single
- **Status:** confirmed (user accepted verdict "as stated" + routing 2026-06-06)
- **Target run:** `v3_exq_647_modulatory_authority_reuse_split_20260606T195410Z_v3`
- **Queue id:** V3-EXQ-647 (machine `ree-cloud-4`)
- **Experiment purpose:** diagnostic · **claim_ids:** [] · **evidence_direction:** non_contributory (stays — no governance weight)
- **Self-route label being adjudicated:** `authority_active_no_behaviour_change`

---

## 0. One-paragraph verdict

V3-EXQ-647 is the **post-float32-fix** clean look at the modulatory-bias-selection-authority
substrate (the arm-reuse system-test reconstruction of 643a on cloud-4). The arm-reuse
machinery itself worked correctly; the FAIL is purely the 643a **scientific verdict**.
Readiness, C0, C1, and C3 all PASS — the authority is now **alive and dose-responsive**
(active 0.97, scale_factor 3.28→18.0 across gains 0.5→0.8), a genuine advance over the
643 autopsy where the gate was numerically dead. **C2 (rank-change over OFF) fails.** The
script self-routes to *"authority too weak — sweep gain higher,"* but the within-run C3
evidence **refutes** that remedy: gain was already swept 5.5× in scale_factor with **zero**
change in selection-change rate. The authority is **gain<1 gap-relative by design** (its
intended safety property), so it only flips **near-ties**, whose frequency is an
environment property, not a gain knob — and the C2 rank-change metric is **confounded** by
a high, seed-variable OFF baseline (legacy bias channels the authority replaces). This is a
**measurement / test-design limitation**, not an authority falsification. The mechanism is
biologically faithful (conflict/gap-gated neuromodulatory biasing of BG selection). The
blocker has **moved** from "gate dead" (643) to "C2 cannot measure a gain<1 authority" (647).

---

## 1. Facts (reconstruction — no interpretation)

### 1.1 The arm-reuse system worked; the FAIL is the science
- ARM_A (`authority_off_baseline`) was **reused** from the V3-EXQ-646 mint by explicit cite
  (3 cells, `reused_from_run_id` + `reused_fingerprint` provenance stamped; machine_class
  `linux-x86_64-py3.10`). The automated fingerprint consumer **correctly refused** all 3
  seeds (`fingerprint_not_in_index`, expected — documents the Phase-1 script_path-coupling
  gap); the explicit cite performed the reuse.
- ARM_B (gain 0.5) and ARM_C (gain 0.8) run **fresh** on cloud-4 via 643a's own
  `_run_seed_arm`. Arms differ **only** in `use_modulatory_selection_authority` and
  `modulatory_authority_gain`.
- → The reuse is sound by construction; nothing in the FAIL implicates the reuse path.

### 1.2 Verdict ladder
| Gate | Result | Evidence |
|---|---|---|
| readiness | **MET** | P-RANGE 0.2238 ≫ floor 1e-4; P-BOUNDED 1.0 ≥ 0.9 |
| C0 curiosity non-degeneracy | **PASS** | score_bias_abs_mean > 1e-4, both ON arms, 3/3 |
| C1 authority active (load-bearing) | **PASS** | B active 0.969 / scale 3.28; C active 0.970 / scale 18.0; OFF silent 0.0 |
| C2 authority changes selection + behaviour | **FAIL** | see below |
| C3 dose-response (informative) | **PASS** | c_scale 18.0 > b_scale 3.28; c_rank 0.350 ≥ b_rank 0.320 |

### 1.3 C2 decomposition (the failed gate)
C2 requires, on ≥2/3 seeds per ON arm, BOTH a rank-change AND a behavioural-change vs ARM_A.
- **behavioural-change** (visited_cells / episode_len rel-Δ > 0.05 vs OFF): B **2/3**, C **3/3** → would pass.
- **rank-change** (`bias_changed_selection_frac` ON − OFF > 0.05): B **1/3**, C **1/3** → **FAILS**, and this is what sinks C2.

`bias_changed_selection_frac` = fraction of P1 select ticks where
`selected_candidate_rank_before_bias > 0` (the bias channel(s) changed which candidate was
selected vs raw pre-bias scores). Per-seed:

| seed | ARM_A (OFF) | ARM_B | B−A | ARM_C | C−A |
|---|---|---|---|---|---|
| 42 | 0.073 | 0.339 | **+0.266** | 0.290 | **+0.217** |
| 43 | 0.331 | 0.151 | −0.180 | 0.293 | −0.038 |
| 44 | 0.608 | 0.469 | −0.139 | 0.466 | −0.146 |
| mean | 0.337 | 0.320 | | 0.350 | |

Only seed 42 clears +0.05 for either ON arm → 1/3 each.

### 1.4 The decisive within-run datum
Gain 0.5→0.8 raised `modulatory_authority_scale_factor_mean` **3.28 → 18.0 (5.5×)** while
`bias_changed_selection_frac` stayed **flat** (0.320 → 0.350, within seed noise).
**Dose-response on magnitude: present. Dose-response on selection-change: absent.**

---

## 2. Adjudicating the self-route

The script's interpretation grid maps "readiness + C1 hold, C2 fails" to:
> *"Authority fires + rescales but does NOT change selection/behaviour. Authority too weak
> at these gains OR no near-ties in this env. **Sweep gain higher.** NOT a substrate bug."*

**The "sweep gain higher" branch is refuted by §1.4.** Gain was already swept (0.5→0.8),
producing a 5.5× scale-factor increase with no change in selection-change rate. This is the
expected behaviour of a **gain<1 gap-relative** authority: the substrate rescales the
modulatory contribution so `range(mod) = gain · raw_score_range`, then adds it to the raw
scores. With gain<1 the modulation is **subdominant** to the primary harm/goal gap by
construction (the substrate's deliberate safety property — *"competitive in near-ties but
subdominant when the primary gap exceeds gain·range"*). So selection only flips on
**near-ties**, and the **frequency of near-ties is fixed by the environment / primary-score
geometry**, not by the gain. Raising gain raises the magnitude of a perturbation that still
can't beat a clear primary winner. The correct sub-branch is therefore **"no near-ties /
criterion confounded,"** not "too weak — sweep higher."

**The C2 rank-change metric is additionally confounded.** ARM_A (authority OFF) already has
a **high, wildly seed-variable** `bias_changed_selection_frac` (0.073 / 0.331 / 0.608)
because the OFF arm still runs the other bias channels / the legacy
`normalize_score_bias_to_e3_range` path. When the authority is ON it **replaces** that
legacy normalization. So C2 compares *authority-driven* selection-change against
*legacy-normalization-driven* selection-change — both ≈ 0.33 — and demands the authority
**add** >0.05 on top of a saturated, noisy baseline on 2/3 seeds. A gain<1 authority cannot
reliably clear that bar regardless of whether it "works."

---

## 3. Claim-layer mapping

`claim_ids = []` — diagnostic / substrate-readiness. No claim is weighted by this run, so
there is **no falsification surface and no demotion**. The substrate under test is
`modulatory-bias-selection-authority` (substrate_queue, status
`implemented_pending_validation`, `ready=false`), whose downstream `unblocks_claims` include
MECH-314/314a/b/c, Q-044, MECH-320, ARC-068, MECH-341, MECH-295, SD-057, MECH-346/347. **None
of those retests are cleared by this run** — they stay gated.

---

## 4. Biological-reference triage

- **Closest mechanism:** neuromodulatory / limbic biasing of basal-ganglia (E3/BG) action
  selection — DA/5-HT/NE and affective channels tipping the committed choice.
- **Faithful translation, not a formal import.** In real brains this biasing is
  **conflict/gap-gated**: Frank's conflict-graded STN decision threshold (the same
  literature ARC-063 / MECH-351 already cite) means modulation tips **near-ties** and does
  **not** override a clear value winner. The REE behaviour (gain<1 only flips near-ties;
  more gain ≠ more flips) is the **expected** signature of that gating, not a defect.
- **Missing-dependency reading:** if the agent forages monostrategically with a clear
  primary winner most ticks, near-ties are rare → a correctly-functioning gap-gated
  authority *should* rarely change selection. Near-tie frequency is itself downstream of
  behavioural diversity / env richness — consistent with the substrate's existing
  `depends_on_unresolved = scaffolded_sd054_onboarding (GAP-2 foraging competence)`.

→ Biological reference verdict: **clear**. The mechanism is not falsified; the test could
not let "carves behaviour" express itself.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | n/a (claim_ids=[]) | No governance weight; mechanism NOT falsified |
| Biological reference | **clear** | Conflict/gap-gated BG biasing; gain<1 near-tie-only is faithful (Frank STN threshold) |
| Prerequisites / dependency | partial | Near-tie frequency downstream of GAP-2 monostrategy (already listed dep) |
| Implementation completeness | **complete** | Post-float32-fix gate fires + dose-responds; OFF silent; readiness met |
| Environment adequacy | **questionable** | Does the env present enough near-tie decision points for a gain<1 authority to act? Criterion can't tell us |
| Measurement adequacy | **under/mis-instrumented (dominant)** | C2 rank-change confounds authority-vs-legacy + asks gain<1 to beat a saturated, seed-variable OFF baseline |
| Integration | not implicated | — |
| Scale / capacity | not implicated | — |

**Dominant diagnosis layer:** measurement / test-design (C2 confound), with a coupled
environment-adequacy sub-question (near-tie frequency).

**Recommended epistemic_category:** `measurement_artifact` (test-design ceiling — the C2
criterion cannot measure a gain<1 gap-relative authority against a legacy-channel-saturated
baseline). NOT `substrate_ceiling`.

---

## 6. Learning extracted

1. **The float32 fix worked** — C1 is alive (active 0.97, scale dose-response). The 643
   blocker ("gate numerically dead") is **resolved**; the blocker has moved to the C2
   criterion. This is real forward progress to record on the substrate.
2. **"Sweep gain higher" is the wrong remedy for a gain<1 gap-relative authority.** The
   within-run C3 dose-response (5.5× scale, flat selection-change) is the proof. Future
   modulatory-authority validations should not list gain-sweep as the C2 remedy.
3. **`bias_changed_selection_frac` is a confounded discrimination metric** when other bias
   channels are active in the OFF arm. A clean test must attribute selection-change to the
   **authority specifically** (with-authority vs without-authority argmin on the *same*
   tick's raw scores) and measure it on **near-tie ticks** (gap < gain·range — the regime
   the authority is designed to act in).
4. **Reuse held across a non-trivial scientific run** — the 646 OFF baseline drove a full
   643a verdict on cloud-4 cell-for-cell. Arm-reuse is validated for this experiment family.

---

## 7. Repair pathway (user-confirmed 2026-06-06)

### 7.1 PRIMARY — `/queue-experiment` V3-EXQ-643b (corrected C2, baseline-reuse on cloud-4)
Same scientific question (does the modulatory authority carve committed selection?) →
**lettered successor**. **Instrumentation-only** correction so the **646 ARM_A baseline
stays byte-reusable** (user constraint: *"queue a modified 643b if it can use the baseline
again for ree-cloud-4"*):

- **Do NOT change the ARM_A config** — keep `use_modulatory_selection_authority=False` at the
  exact 643a/646 settings so the V3-EXQ-646 mint cells remain reuse-eligible (machine_class
  `linux-x86_64`, same seeds 42/43/44, same env/schedule). 643b explicit-cites the latest
  `v3_exq_646_*_v3.json` ARM_A, identical to 647.
- **Replace the C2 rank-change metric** with an **authority-attributable** measure computed
  per tick in the ON arms only: on each select tick, compute the argmin under
  `raw_scores + authority_mod` vs the argmin under `raw_scores` alone (no other bias
  channel) → `authority_flipped_selection` boolean. This isolates the authority from the
  legacy channels the channel-agnostic `bias_changed_selection_frac` lumps together, so it
  does **not** require turning the legacy channels off in ARM_A (preserving reuse).
- **Restrict the readiness/denominator to near-tie ticks** (`raw_score_gap < gain · range`)
  — the regime a gain<1 authority is designed to act in — and report the authority-flip rate
  *within* that population, plus the near-tie frequency itself (so a low flip rate caused by
  near-tie scarcity is distinguishable from authority impotence on genuine ties).
- **Drop "sweep gain higher"** from the interpretation grid; replace with the near-tie-
  frequency / env-adequacy branch.
- Machine affinity `ree-cloud-4`; experiment_purpose diagnostic; claim_ids=[].
- (Goes through the `/queue-experiment` skill per the mandatory-skill-path rule — this
  autopsy session does not write the script.)

### 7.2 RECOMMENDED — `substrate_queue` status amend (governance applies; action=amend)
No substrate code change. Record on the `modulatory_bias_selection_authority` entry:
- Append a 647 record: **C1 now PASSES** post-float32-fix (active 0.97, scale dose-response
  3.28→18.0); the prior dead-gate failure_records (604a / 643) are superseded as the active
  blocker.
- The active blocker has **moved to test-design** (C2 cannot measure a gain<1 gap-relative
  authority against a legacy-saturated baseline) — corrected re-validation = V3-EXQ-643b.
- Keep `ready=false` and `pending_retest_after_substrate=true`; the MECH-314/320/341 retests
  stay gated until 643b clears an authority-attributable, near-tie-scoped selection-change.
- `next_step` → V3-EXQ-643b.

### 7.3 evidence_direction
Stays **non_contributory** (diagnostic, claim_ids=[]). No change.

---

## 8. Cross-reference
- Predecessor autopsy: `failure_autopsy_V3-EXQ-643_2026-06-06.{md,json}` (gate-dead / float32
  cancellation — the layer this run shows is resolved).
- Substrate: `modulatory-bias-selection-authority` (substrate_queue; CLAUDE.md
  2026-06-03 landing + 2026-06-06 float32 amend).
- Comparison target **V3-EXQ-643a** (Mac full run) is still queued/claimed (priority 315);
  it shares 647's evaluator and will likely reproduce the same C2 FAIL — 643b's corrected
  criterion is intended to supersede the C2 design for both.
- Design doc: `docs/architecture/modulatory_bias_selection_authority.md`.
- Related thread: candidate-differentiated affective gradients / per-candidate modulatory
  variance (the recurring 604a/624a/614d/643 scoring-layer pattern; 647 is the first run to
  clear the gate and isolate the *selection-authority* axis as the remaining question).
