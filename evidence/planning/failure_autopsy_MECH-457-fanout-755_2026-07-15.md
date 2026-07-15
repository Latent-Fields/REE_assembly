# Failure Autopsy — MECH-457 GOV-FANOUT-1 H-mode leg (V3-EXQ-755), four-axis portfolio close

- **Generated:** 2026-07-15T13:47:18Z
- **Scope:** cluster (continuation / four-single-axis close)
- **Status:** confirmed
- **Cluster slug:** `MECH-457-fanout-755`
- **Fans out from:** `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15.json`
- **Arc:** 734-737 (conversion-ceiling / competence gap) → `sd_actor_critic_action_learning` built → 742 (all arms sub-floor; actor on frozen z_world < random → "deeper than action-learning") → 747/748/749 (H-rep + reward-density REFUTED; cause = RL exploration/credit bootstrap) → 751 (RND clears floor 5.22 unsupervised; ICM fails) + lit-pull (novelty class rejected as *the build*; 4 composable classes named) → 752/753/754 (credit / return / curriculum, all FAIL sub-floor; cold-start adopted; brake fires; route = build `mech457_competence_bootstrap_explorer`) → **755 (this autopsy): the 4th and final single-axis leg — H-mode/policy-control — FAIL.**
- **Recording:** `validate_recording` OK — `substrate_hash` present (`dd3db615…`), seeds [42,43,44], `rec/v1`. **No recording gap.**
- **User decisions (2026-07-15, Step 8 gate):** (1) **Fold into the pending build** — route `implement-substrate`, amend `mech457_competence_bootstrap_explorer` with 755's failure record (sharpening its capacity half); brake refuses any same-claim re-test. (2) **Close now, note 756 in-flight** — write the four-single-axis portfolio close; do not block the build on the 756 additivity pair.

---

## Where this sits

The 752-753-754 autopsy adopted the **cold-start / success-dependence** reading, fired the re-derive brake (2nd non_contributory MECH-457 autopsy), and routed to a single build — a competent unsupervised explorer composing the landed ARC-065/MECH-314 curiosity substrate as a success-independent bootstrap drive — while explicitly sanctioning **H-mode as the one remaining distinct axis to run in parallel, not gating the build**, with a pre-registered null: *"H-mode arm ≤ RND 5.22 plateau on a strict majority of seeds."*

**755 came back exactly at that null.** This closes the four single-axis discrimination legs. The H-credit × H-return additivity **pair cell (V3-EXQ-756) was still running on ree-cloud-3** at autopsy time.

---

## Facts — the H-mode leg

**Mechanism (treatment):** a critic-utility-gated explore/exploit mode scalar `m_t = sigmoid(k·(utility − baseline))` (Aston-Jones & Cohen 2005; Daw 2006) annealing the rollout-entropy temperature and the RND intrinsic coefficient toward greedy exploitation as utility rises — a meta-controller *over* exploration. **Comparator:** the SAME-RUN fixed-coefficient RND arm (intrinsic_coef 1.0, no anneal). The treatment is the **gate**, not more novelty.

Shared controls (env solvable, floor real, all readiness met):

| Control | foraging_competence @D3 (per seed) |
|---|---|
| `greedy_oracle` (global-info ceiling) | 57.0 / 57.3 / 57.3 |
| `local_view_greedy` (5×5 observability ceiling, fair denominator) | 45.75 / 49.7 / 48.7 (mean 48.05) |
| `random_walk` (near-floor lower bound) | 1.05 / 0.9 / 0.85 |
| `sparse_zw` (742 sparse reproduction) | 0.15 / 0.25 / 0.30 |

Load-bearing arms (per-seed foraging_competence @D3):

| Arm | z_world (seeds 42/43/44) | mean | raw (seeds 42/43/44) | mean |
|---|---|---|---|---|
| `rnd_fixed` (comparator) | 5.85 / 1.2 / 0.85 | **2.633** | 0.2 / 0.6 / 1.4 | **0.733** |
| `rnd_mode` (treatment gate) | 3.65 / 4.45 / 0.7 | **2.933** | 0.2 / 0.2 / 0.7 | **0.367** |
| mode gain (mode − fixed) | | **+0.30** | | **−0.367** |

- **Load-bearing criterion `C_hmode_beats_fixed_rnd_by_margin` = FAIL.** Consolidation margin = 1.0 res/ep; z_world gain +0.30 (below margin), raw gain −0.367 (mode *worse*). `any_rep_mode_gain = false`.
- The gate **did** act: `per_arm_intrinsic_reward_recent` mode_zw 0.0466 > fixed_zw 0.0254 — the anneal shifted behaviour; it just produced no competence lift.
- **Readiness MET; non-degenerate = true.** The env is solvable from the local view (48.05 ≫ 1.0 floor).

**Which criterion failed:** the **discrimination** criterion (mode beats fixed by margin) — not a readiness or absolute criterion (those all passed). This is the substrate-ceiling fingerprint: readiness/negative-control passes, discrimination fails.

**How 755 differs in shape from 752-754:** those three sat *sub-floor* (their mechanism arms ≈ sparse baseline, below 1.0). Here the RND arms **clear the floor** (2.633, 2.933) — but the arbitration **gate** adds nothing on top of raw fixed novelty. Same structural conclusion, reached from a different angle.

---

## Cluster read — the four-axis portfolio, convergent

| Leg | Class / axis | Result | Shape |
|---|---|---|---|
| **752** H-credit | prioritized backward credit sweep | FAIL | sub-floor (~0.2–0.45) — nothing to sweep from ~0 success |
| **753** H-return | Go-Explore archive + return | FAIL | sub-floor — no interesting states reached to archive |
| **754** H-curriculum | AMIGo goal-frontier | FAIL | sub-floor — trivial achievable frontier from ~0 competence |
| **755** H-mode | critic-utility explore/exploit gate | FAIL | **clears floor via RND, but gate adds no gain** over fixed RND |
| — 751 H-optim | unsupervised RND explorer | **PASS** | the sole floor-clear (5.22, ≈11% of the 48 ceiling) |
| — 756 pair | H-credit × H-return additivity | *running* | in flight on ree-cloud-3 at autopsy time |

**Not N independent nulls — one structural property with two joined halves:**

1. **Cold-start / success-dependence (752-754).** Backward credit needs a successful trajectory to propagate from; Go-Explore needs interesting states to archive; AMIGo needs an achievable frontier that carries gradient. All three amplify signal *derived from prior task success*, so they cannot bootstrap from ~0. Only the two **success-independent** classes in the arc — RND novelty (751, 5.22) and BC imitation (748, 32.72) — break the floor.
2. **Capacity / conversion (755).** Even a *competent arbitration controller* over a success-independent drive cannot squeeze more competence from a low-capacity explorer. The ceiling is the explorer's **capacity to convert coverage into competence** — RND reaches only ~11% of the local-view ceiling — not the way exploration is *scheduled*.

Both halves point at the **same single build**: `mech457_competence_bootstrap_explorer` must compose ARC-065/MECH-314 curiosity as a success-independent bootstrap drive **and** carry adequate policy capacity / training budget to reach floor→*competent*. 755's contribution is to sharpen the **second half** and to rule out the tempting "we just need better explore/exploit arbitration" alternative.

Biology-resonant: LC-NE explore/exploit gain arbitration (Aston-Jones & Cohen 2005; Daw 2006) *modulates* an already-competent policy's exploration — it sits downstream of, and cannot manufacture, the competence a low-capacity learner never had. A discovered dependency-ordering, not a falsification.

---

## Claim-layer mapping

- **MECH-457** (mechanism_hypothesis; candidate; v3_pending; depends_on SD-056, MECH-229) — "the action-LEARNING machinery that converts drive into learned control." 755 does not test the claim's truth; it discriminates *which* lever the machinery still lacks. It **refutes the policy-control/arbitration axis as that lever** and **strengthens the capacity half** of the bootstrap dependency. Necessity intact; one more sufficiency candidate refuted. MECH-457 stays **candidate / v3_pending**.
- **INV-088** (invariant; emergent; candidate) — not carried on 755, but the strategy-diversity readout it needs remains starved for a matched-competent policy (same block as 750/754). Retest is `pending_retest_after_substrate` on the same build. Stays **candidate / pending_substrate_reconfirmation**.

`experiment_purpose: diagnostic` → **excluded from governance confidence/conflict scoring.** This autopsy records the discrimination + build sharpening, not weighted evidence. **PROMOTES / DEMOTES NOTHING.**

---

## Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **strengthened (dependency)** | refutes the arbitration axis as the missing lever; strengthens the "explorer capacity to convert coverage→competence" half; does not falsify MECH-457 |
| Biological reference | **clear** | LC-NE explore/exploit gain arbitration modulates a competent policy; it sits downstream of competence and cannot bootstrap it |
| Prerequisites / dependencies | **missing (buildable)** | success-independent dense drive (752-754 half) + adequate policy capacity/budget (this half) |
| Implementation completeness | complete (portfolio-gated) | ModeGate active (intrinsic-reward anneal shifted); mode arm deterministic + supra-floor; the gate simply produced no lift |
| Environment adequacy | **adequate** | oracle 57.2, local-view 48.05, RND supra-floor; the 1.0 floor is genuine |
| Measurement adequacy | **adequate** | per-seed competence both reps; RND/BC/ceiling bands pre-registered; correct same-run comparator |
| Integration adequacy | isolated-per-axis | H-mode run alone; additivity (756) still in flight |
| Scale / capacity | **insufficient at the current explorer** | build target: floor→*competent*, not merely off-floor |

**Recording-debt vs measurement-debt:** neither. Manifest recording-complete, metric correct. The gap is a **buildable substrate**, not a blind spot.

---

## Re-derive brake (MOVE-3) — FIRES (3rd)

- Prior `non_contributory`/convergent failure-autopsy docs tagging **MECH-457**: **2** (`failure_autopsy_MECH-457-fanout-751-750_2026-07-14` target 750; `failure_autopsy_MECH-457-fanout-752-753-754_2026-07-15`).
- This autopsy records 755 as **non_contributory to claim confidence** (diagnostic; PROMOTES/DEMOTES NOTHING) and convergent-on-substrate → the **3rd** such reading (threshold = 2). **Brake fires.**
- **Consequence:** route to **`implement-substrate`** on `mech457_competence_bootstrap_explorer`; **REFUSE** a same-claim mode-gate retune or any further single-axis bolt-on leg circling the same competence floor. The post-build retest of the composed explorer, and any genuinely-distinct-mechanism new-EXQ question, are **not** refused.
- **Portfolio is exhausted at the single-axis level** — the one remaining cell (756 additivity pair) is already running; **no fresh fan-out is owed.**

---

## Routing

| Target | Outcome | Verdict | Routing |
|---|---|---|---|
| V3-EXQ-755 (H-mode) | diagnostic FAIL | non_contributory to confidence; refutes arbitration axis; strengthens capacity half of the bootstrap dependency | **implement-substrate** (amend `mech457_competence_bootstrap_explorer`) |

**Recommended substrate_queue action: `amend`** target `mech457_competence_bootstrap_explorer` (the entry the 752-753-754 autopsy recommends governance `create`). Append 755's failure record; if governance has not yet created the entry, create it per the 752-753-754 autopsy first, then append. The amend note adds the **capacity/budget requirement**: the composed explorer must reach floor→*competent*, not merely off-floor. Priority 1. No duplicate `create`.

---

## Draft `evidence_quality_note` for governance (verbatim in JSON)

**MECH-457 (755):** "2026-07-15 (GOV-FANOUT-1 discrimination portfolio V3-EXQ-755, H-mode/policy-control axis; diagnostic, claim_ids=[MECH-457]; consumed via /governance from failure_autopsy_MECH-457-fanout-755_2026-07-15). A critic-utility-gated explore/exploit mode scalar yields NO consolidation gain over a SAME-RUN fixed-coefficient RND arm (z_world +0.30 < 1.0 margin; raw −0.37; any_rep_mode_gain=false) while every readiness precondition holds (oracle 57.2, local-view 48.05). Distinct from 752/753/754 (sub-floor): the RND arms DO clear the floor but the arbitration gate adds nothing → the policy-control axis is REFUTED as the missing lever, and the residual is explorer CAPACITY to convert coverage→competence (RND ≈11% of the 48 ceiling), not exploration scheduling. CLOSES the four single-axis legs (752/753/754/755 all FAIL; only 751 RND cleared the floor) and STRENGTHENS the 'adequate policy capacity/training budget' half of the pending mech457_competence_bootstrap_explorer build. Does NOT falsify MECH-457 (necessity intact). Diagnostic — excluded from scoring; PROMOTES/DEMOTES NOTHING. Re-derive brake FIRES (3rd non_contributory/convergent MECH-457 autopsy): route = implement-substrate (fold this record into mech457_competence_bootstrap_explorer); same-claim mode-gate retune / further bolt-on leg REFUSED. MECH-457 stays candidate/v3_pending. The H-credit×H-return additivity pair V3-EXQ-756 was still running on ree-cloud-3 at autopsy time."
