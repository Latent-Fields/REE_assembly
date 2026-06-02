# Disposition memo: the "EXQ-085 / MECH-071 dead chain"

**Date:** 2026-06-02
**Author:** analysis session (EXQ-085 / MECH-071 dead-chain disposition)
**Status:** RECOMMENDATION ONLY — flagged for user decision. No `claims.yaml` edit made.
**Trigger:** `insights_report.md` Experiment Health flagged EXQ-085 as the longest dead
chain (14 lettered FAIL iterations, no PASS, no successor) and recommended (line 144)
"shelve MECH-071."

---

## TL;DR

The "EXQ-085 / MECH-071 dead chain" is a **misnomer on two counts**, and the
insights-report recommendation to shelve MECH-071 is based on a letter-suffix
heuristic that does not match the evidence:

1. **MECH-071 is not the claim that failed.** MECH-071's core assertion — the E3
   `harm_eval` calibration-gradient asymmetry, measured by criterion **C3** — **PASSED
   in every iteration of the 085 chain** (cal_gap 0.03–0.26, threshold 0.03) and is
   independently validated by EXQ-026 (cal_gap 0.037) and EXQ-029 (cal_gap 0.239).
   MECH-071 is already `provisional`. The recurring FAIL is criterion **C2**
   (goal-directed-navigation `benefit_ratio`), which tests a *different* mechanism
   (goal-state latent steering navigation toward resources), not harm calibration.

2. **The chain is not abandoned — it migrated to fresh EXQ lineages under the correct
   claims.** The C2 navigation question moved off the 085 letters at 085h (2026-03-30)
   onto SD-015, then onto fresh numbers (EXQ-185, EXQ-182a, EXQ-322, EXQ-514) and is
   **active today** as the goal-stream-repair ladder **V3-EXQ-622 / 626 / 626a**
   (626a `claimed` on ree-cloud-1, 2026-06-01). The insights-report "no successor"
   detection is a letter-suffix heuristic blind to continuation under new numbers.

**This is therefore neither a substrate ceiling for MECH-071 (which passed) nor a
simple bug.** It is (a) a claim-tagging mis-attribution against MECH-071, plus (b) a
genuinely hard goal-navigation problem that is being worked under the correct claims
(SD-015 / MECH-112 / ARC-030 → 626 ladder).

---

## What MECH-071 actually claims

`claims.yaml` MECH-071 (`status: provisional`, `claim_type: mechanism_hypothesis`,
`subject: e3.harm_eval_calibration_gradient_asymmetry`, no explicit `epistemic_category`
→ inferred `standard`):

> E2/E3 harm prediction is better calibrated for agent-caused vs environment-caused
> transitions; E3 learns a *graded* danger model — `harm_eval` rises continuously with
> hazard proximity (approach → contact), not only at contact.

That gradient is operationalised as **criterion C3** in the 085 scripts
(`calibration_gap_goal_present`). It is the only criterion in the chain that maps to
MECH-071. The other criteria (C1 z_goal_norm, C2 benefit_ratio, C4 prox_r2/rfm_loss)
test the goal-navigation apparatus.

---

## The 085 chain, decomposed

The 14 iterations are **not one experiment** — the chain forks. Claim tags by iteration
(from the manifests):

| Iterations | claim_ids tagged | What is under test |
|---|---|---|
| 085, 085c, 085d, 085e | MECH-071, INV-034 | goal-seeding + (C3) calibration |
| 085f, 085g | MECH-071, MECH-112, MECH-117, SD-012 | goal-wired navigation + (C3) calibration |
| 085h, 085i, 085j, 085k, 085l, 085n, 085o | **SD-015**, SD-012, MECH-112 | z_resource encoder (NOT MECH-071) |
| 085m | **ARC-030**, MECH-112, SD-015 | benefit-eval E3 (NOT MECH-071) |

Only **6 of the 14** iterations (085–085g) carry MECH-071 at all; the last 8 dropped
MECH-071 entirely and re-tagged to SD-015 / ARC-030. The insights heuristic counts all
14 against MECH-071.

### C3 (MECH-071) passed throughout; C2 (navigation) is what fails

| Run | C3 cal_gap (MECH-071) | C2 benefit_ratio (navigation) | Verdict |
|---|---|---|---|
| EXQ-026 (baseline) | 0.037 PASS | n/a | **PASS 5/5** |
| EXQ-029 (proxy fields) | 0.239 PASS | n/a | **PASS** |
| 085–085d | C3 PASS where measured | z_goal never seeded (<0.1) | non_contributory (already reclassified) |
| 085e | 0.166 PASS | 1.00 FAIL | FAIL 3/4 |
| 085f | 0.030 PASS | 0.28 FAIL | FAIL 3/4 |
| 085g | 0.218 PASS | 0.37 FAIL | FAIL 3/4 |
| 085o | 0.263 PASS | 0.11 FAIL | FAIL 3/4 |

In every scored iteration C1/C3/C4 PASS and **only C2 fails**. The goal-guided agent
navigates *worse* than random (ratio < 1.0), so MECH-124's V4 over-salience risk is not
triggered (goal_vs_harm_ratio ~2.3 throughout, well above the 0.3 risk floor).

### Why C2 fails — the diagnosis is complete

- **085–085d:** random-walk warmup without homeostatic drive never seeds z_goal
  (z_goal_norm < 0.1). Mechanism never instantiated → already marked
  `non_contributory` for MECH-071 (thought doc
  `docs/thoughts/2026-03-24_mech071_goal_latent_non_contributory_evidence.md`; SD-012
  homeostatic drive registered as the fix).
- **085f/085g:** wiring fixed and z_goal seeds (norm 0.23–0.40), but
  `goal_resource_r ≈ 0.07` — z_world at contact encodes the whole scene, not the
  resource; features are not position-invariant across respawns. → SD-015 registered
  (dedicated z_resource encoder).
- **085h–085o (SD-015):** the encoder *learns* a position-invariant resource
  representation (085l prox_r2 0.91, r_enc 0.87) yet navigation still fails
  (benefit_ratio 0.42 → 0.11). Sorting the receptive field to remove position kills the
  usable signal.
- **EXQ-182a oracle ceiling PASS (11.14x):** a handcrafted perfect goal cue drives
  navigation far past threshold — **proving the action-selection mechanism is sound**.
  The bottleneck is z_goal *learning quality* + **multi-step planning horizon**:
  EXQ-185 showed 1-step greedy lookahead creates local traps on a 10×10 grid.

The 085-era blocker for the planning-horizon half was **SD-004** (hippocampal
multi-step planning), which at the time was unbuilt. **SD-004 is now `implemented`**, and
the live 626 ladder probes goal-stream formation under the developmental-window /
object-binding framing (`goal_stream_repair_diagnostic_ladder_2026-06-01.md`,
`failure_autopsy_V3-EXQ-626_2026-06-01.md`).

---

## Recommended disposition (for user decision)

**1. MECH-071 — leave `provisional`. Do NOT demote or reclassify.**
The 085 chain provides **zero weakening evidence** against MECH-071; its calibration
gradient (C3) passed in every iteration and is independently validated by EXQ-026/029.
Shelving MECH-071 (insights line 144) would discard a validated claim on the strength of
a navigation failure it does not own.

**2. Tidy the evidence record (optional, low-risk).**
Mark the MECH-071 evidence entries on **085e / 085f / 085g** `non_contributory` *for
MECH-071* — matching the treatment already applied to 085–085d — since these test C2
goal-navigation, not the C3 calibration gradient. This is a CLAIM_IDS-Accuracy-Rule
correction: it removes the false "MECH-071 has 14 FAILs" signal that the index and the
insights heuristic both read. (The C3 PASSes could alternatively be kept as `supports`
for MECH-071, but `non_contributory` is cleaner given the runs were designed around C2.)
Rebuild the index after any such edit.

**3. The 085-letter chain — close as MIGRATED / SUPERSEDED, not "stalled."**
Its scientific question (goal-directed navigation) is not dead; it lives under
SD-015 → ARC-030 → the active **V3-EXQ-622 / 626 / 626a** goal-stream ladder. **No new
085 letter and no new EXQ are warranted for MECH-071** — the calibration claim is
settled. The goal-navigation question already has a correctly-numbered live successor.

**4. The genuine substrate story belongs to SD-015 / MECH-112 / ARC-030, not MECH-071.**
That cohort is `substrate_conditional` in character (gated on z_goal formation quality +
multi-step planning), with SD-004 now implemented and the 626 ladder actively probing
it. No reclassification is requested here — flag only that *if* governance wants to mark
the goal-navigation cohort, `substrate_conditional` (depends on the planned object-bound
incentive-salience substrate per the 626 autopsy) fits better than `substrate_ceiling`,
because the oracle PASS shows the mechanism is reachable once the upstream signal exists.

**5. insights_report.md heuristic — annotate, don't trust blindly.**
Lines 17 / 33 / 144 conflate (a) letter-suffix count with claim attribution and (b)
absence of a same-letter successor with abandonment. Recommend the Experiment Health
detector cross-reference claim continuity (the 085 question continues under SD-015 → 626)
and per-criterion outcomes (C3 vs C2) before labelling a chain "dead" or recommending a
claim be shelved.

---

## Evidence pointers

- Manifests: `evidence/experiments/v3_exq_085*/` (085 … 085o)
- MECH-071 claim + full evidence_quality_note: `docs/claims/claims.yaml` (MECH-071)
- SD-015 claim + continuation trail (EXQ-185 / 182a / 322 / 514): `docs/claims/claims.yaml` (SD-015)
- Non-contributory rationale: `docs/thoughts/2026-03-24_mech071_goal_latent_non_contributory_evidence.md`
- Live successor lineage: `ree-v3/experiment_queue.json` (V3-EXQ-626a),
  `failure_autopsy_V3-EXQ-626_2026-06-01.md`,
  `goal_stream_repair_diagnostic_ladder_2026-06-01.md`
- Flag source: `insights_report.md` (Experiment Health, lines 17 / 33 / 144)
