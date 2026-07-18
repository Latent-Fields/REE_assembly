# Failure autopsy — V3-EXQ-778c (SD-068 null-content control)

**Generated:** 2026-07-18T08:33:58Z
**Scope:** single (with an explicit supersession of V3-EXQ-778b)
**Status:** confirmed (user-adjudicated at the Step 8 gate, 2026-07-18)
**Target run_id:** `v3_exq_sd068_null_content_control_diagnostic_20260718T072318Z_v3`
**Superseded run_id:** `v3_exq_sd068_null_content_control_diagnostic_20260718T065939Z_v3` (V3-EXQ-778b, n=2)
**Claims tagged:** SD-068 (subject), MECH-168 / INV-047 / MECH-169 (context only)
**Purpose:** diagnostic (instrument-validity control; does not weight governance confidence)

---

## 1. Why this is an autopsy and not a `/governance` clear

V3-EXQ-778c ran to completion and returned `outcome: FAIL` with `evidence_direction: weakens`
on SD-068. Its load-bearing criterion C1 failed on **0 of 8 seeds**. It is not a crash
(no traceback, full manifest, `dry_run: false`, `elapsed_seconds` 809.4), so
`/diagnose-errors` does not apply.

It is also **not** a broken run. The readiness precondition
(`injected_arm_sigma_slope_supra_floor`, measured 0.0665 vs threshold 1e-06) was **met**,
C2 (`ratio_interpretable_all_phases`) **passed**, and `criteria_non_degenerate` is `true`
on all three criteria. The instrument did exactly what it was built to do and returned an
informative negative about the instrument it was auditing.

The experiment script pre-registered this reading (`v3_exq_sd068_null_content_control_diagnostic.py`
lines 90–92):

> A FAIL here is an INFORMATIVE outcome, not a broken run: it scopes SD-068's
> non-vacuity honestly (the contract would then have to be carried by the REM
> passthrough-vs-generative contrast alone) rather than withdrawing the claim.

That pre-registration is honoured below.

## 2. Facts — reconstruction, no interpretation

### 2a. Supersession (not a pair)

`778c` carries `supersedes: "V3-EXQ-778b"` in-manifest. It is the powered successor:

| | 778b | 778c |
|---|---|---|
| seeds | `{42, 7}` | `{42, 7, 123, 2024, 99, 7777, 314, 1000}` (778a's set) |
| `need_seeds` | 2 | 8 |
| `n_seeds_pass` | 0 | 0 |
| outcome / direction | FAIL / weakens | FAIL / weakens |
| `elapsed_seconds` | 215.9 | 809.4 |
| `substrate_hash` | `ab931f62…` | `4de2a96e…` |

The seed set is a strict superset and the **injected-arm slopes on the two shared seeds are
bit-identical** across the two runs (seed 42: sws `2.269717072399339`, nrem
`0.09671970039873905`, rem `0.1386070204874681`). The differing `substrate_hash` reflects
the driver-script change (n=2 → n=8 seed list + distribution stats), not a substrate
change to the measured path. 778c therefore strictly dominates; 778b should be marked
`evidence_direction: "superseded"` and must not double-count.

The script records why n=2 was wrong (lines 127–140): 778b was authored on the belief that
778 had found a seed-stable order, which the manifests refute; and the rem leg's null ratio
is genuinely seed-variable because its clamp saturation is itself a random draw. 778b's
rem verdict flipped across its 2 seeds (`confound_verdict_stable: false`), which is exactly
the under-powering 778c corrects.

### 2b. Which criterion failed

C1 is the **discrimination** criterion (`null_slope_ratio <= 0.25 on all 3 phases`), and it
is the only load-bearing one. C2 (readiness / positive control) passed. This is *not* the
"negative control passes, discrimination fails" substrate-ceiling fingerprint — the
discrimination that failed is about the **instrument**, not the substrate.

### 2c. Per-phase result (n=8)

| phase | mean null_slope_ratio | sd | 95% CI | seeds confounded | verdict stable | reading |
|---|---|---|---|---|---|---|
| `nrem` | 0.1445 | 0.00090 | [0.1438, 0.1451] | 0/8 | yes | **content-contingent** — clean |
| `sws`  | 1.0000 | 2.7e-08 | [0.99999997, 1.00000001] | 8/8 | yes | **fully confounded** — content-free |
| `rem`  | 1911.6 | 3306.1 | [-379, 4203] | 3/8 | **no** | **degenerate / uninterpretable** |

**`sws` is the decisive finding.** The null arm's sigma-slope is numerically identical to
the injected arm's to eight decimal places on 8/8 seeds. The integrity payload shows why
this is structural rather than statistical: at every sigma the injected arm has
`signal_power` 5585.7 and the null arm `signal_power` 0.0, while `noise_power` is **the
same in both arms** (384.18, 1536.73, 6146.91, 24587.64). `denoising_snr_db =
10*log10(signal_power / noise_power)` therefore has a sigma-slope driven **entirely** by
`log(noise_power)`; the content term is a constant offset that differentiates away. The
SWS readout carries zero content information by construction.

**`rem` is degenerate in both directions.** Per-seed null ratios are either exactly `0.0`
(5/8 seeds — the null arm's `calibration_error` pins at the constant 998.5009992509989 on
every sigma, `target_clamped: 1.0`, so the slope is exactly zero) or off-scale 1801–9143
(3/8 seeds — the null arm's precision reference collapses onto the 1e-3 positivity floor,
so `1/1e-3 = 1000` dominates). The manifest's own `rem_off_scale_note` says to read a large
value as "this leg is structurally content-free", never as a calibrated N-fold sensitivity.
The 5 "unconfounded" seeds are unconfounded only *by degeneracy* — a zero slope from a
saturated constant is not evidence of content-contingency. `ceiling_inside_ci95: true`
confirms the verdict is unresolved at this n. C3 fails here.

### 2d. Recording provenance

The always-core is present: `recording_schema: rec/v1`, top-level `substrate_hash`,
`machine` (`ree-worker-1`) / `machine_class` (`linux-x86_64-py3.10`), `elapsed_seconds`,
full `config`, explicit `seeds` list, plus per-cell `arm_fingerprint`. **No recording
debt.** This is a measurement finding, not a recording finding — the readout was computed
and durably written; it is the readout's *definition* that is blind.

## 3. Claim-layer mapping — which layer may this FAIL touch?

| Claim | Role here | May this run move it? |
|---|---|---|
| **SD-068** | the harness whose non-vacuity is audited | **Yes** — this is a direct instrument-validity test of SD-068's own contract |
| MECH-168 | staged failure under diffuse damage | **No** — context tag only; the run tests the instrument, not the claim |
| INV-047 | staged clinical decline | **No** — same |
| MECH-169 | glymphatic/attribution complementarity | **No** — same |
| MECH-121 | NREM slot-filling (held) | deliberately **not tagged**; hold respected |

The `claim_ids` tagging is accurate and was re-evaluated by the author rather than
inherited (script lines 62–70 state the rationale explicitly, including the MECH-121
omission). No EXQ-048/MECH-057b-style mis-tag risk here.

So the per-claim `evidence_direction` in the manifest is correct as emitted: `weakens` on
SD-068, `unknown` on the other three. **This run does not weaken MECH-168 / INV-047 /
MECH-169.** What it does is invalidate a *prior annotation* that was banked onto them — see
§6.

## 4. Biological-reference triage

- **Closest reference mechanism:** targeted memory reactivation (TMR) during sleep — cueing
  a consolidating trace with a sensory cue paired at encoding.
- **Methodological precedent:** Bar et al. 2020, *Curr Biol*, DOI 10.1016/j.cub.2020.01.091.
  The lit entry exists: `evidence/literature/targeted_review_sd_068/entries/2026-07-18_sd_068_local_tmr_injected_content_bar2020/`.
  **`lit_status: present`** — this is *not* a formal-definition import with no biology, so
  the SD-003 failure mode does not apply.
- **Is the null control faithful to the precedent?** Yes, and this is the load-bearing
  point. What made Bar et al. convincing is precisely that unilateral olfactory stimulation
  during sleep produced no memory and no oscillatory effect when learning had occurred
  *without* the contextual odour — the perturbation alone does nothing; it acts only on
  injected content. 778c is the direct analog, and it holds the delivered perturbation
  numerically identical across arms (`diffuse_perturb(rms_ref=...)`) so the null arm is
  "same odour, no prior pairing" rather than "weaker odour".
- **Does the failure resemble a biological missing-dependency signature?** No — and that is
  what makes the diagnosis clean. This is not a case of "the mechanism needs a prerequisite
  we haven't built". The SWS *substrate operation* (`shy_normalise` + `run_sws_schema_pass`)
  is present and running; it is the **measurement wrapped around it** that fails to
  reference the injected content. The biology is not implicated at all.

**Verdict: translation is fine at the mechanism layer; the failure is entirely at the
measurement layer.** SD-068's design principle (inject known content, perturb at scope,
read out at scope) is biologically well-grounded and survives; one of its three
instantiations does not implement that principle.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **weakened (scoped)** | SD-068's 3-phase non-vacuity contract is refuted on 2 of 3 phases; the principle and the nrem instantiation stand |
| Biological reference | **clear** | TMR / Bar et al. 2020; lit entry present; null-control design is faithful to the precedent |
| Developmental / dependency prerequisites | **present** | MECH-120/121/123 phase ops all present and firing; nothing upstream is missing |
| Implementation completeness | **partial** | `sws_denoising_snr` has the *symbol* of a denoising-quality readout but not its functional role — it is a noise-power statistic |
| Environment adequacy | **adequate** | offline/injected-content design; no environment pressure required |
| Measurement adequacy | **misleading** | the dominant layer. `denoising_snr_db` differentiates its content term away; the rem calibration readout saturates at both rails |
| Integration adequacy | **coupled** | arms share substrate, warm-up and RNG streams; injected arm verified bit-identical to the pre-778b harness |
| Scale / capacity | **adequate** | n=8 resolves sws and nrem decisively; only the rem leg remains under-powered, and by degeneracy rather than n |

**Recommended `epistemic_category`: `measurement_gap`.**
Explicitly **not** `substrate_ceiling` — the substrate is present and firing; the metric is
blind. Explicitly **not** a recording gap — the readout was recorded, its definition is
wrong.

## 6. Learning extracted

1. **The SWS leg of the SD-068 staging order has never measured content fidelity.**
   `denoising_snr_db` is a pure noise-power statistic. Any conclusion resting on
   `sws_tolerance` is a conclusion about noise sensitivity.

2. **This retro-explains a tell that was already visible in the SD-068 doc.** Leg 1 reports
   `sws` tolerance std ~9e-9 against nrem 0.0014 and rem 0.396, and a suspiciously tight
   95% CI of [0.422, 0.425] on the NREM-before-SWS difference. That tightness was read as
   robustness; it is in fact the signature of a near-deterministic analytic metric. **A
   variance three-to-five orders of magnitude below its siblings is an instrument-validity
   flag, not a strength-of-effect signal.** This is the generalisable methodological lesson.

3. **The doc's Leg 1 headline is retracted.** "`nrem` fails before `sws` — ROBUST, 8/8,
   sign-test p = 0.0078" compares a content-contingent readout against a content-free one.
   The comparison is not evidence of staging. (User-adjudicated at the Step 8 gate.)

4. **Leg 2 (REM generative gain 0.149, 8/8 attenuating) is NOT overturned by C1** — it is a
   different readout (`rem_generative_fidelity`) with its own internal clean-vs-corrupt
   control. But see §7 H3: the null arm's `rem_generative_gain` (~0.182/0.184/0.188/0.209
   on seed 42) is close to the injected arm's (~0.165/0.166/0.172/0.190) with
   `rem_gen_content_scale: 0.0`. This is **outside the scored C1 criteria** and is recorded
   as an open question, not a verdict. If it replicates, it does not touch "the transfer
   function attenuates" but it does undercut the doc's specific gloss that *"the correction
   needs an intact seed"* (sd_068 doc line 221).

5. **The null control is the highest-value instrument this harness has.** It cost ~13.5
   minutes of cloud compute and invalidated a headline result banked the previous day. The
   generalisable rule: **an injected-content harness should ship its zero-content null arm
   in the same cycle as its first scored run**, not one day later.

6. **Second-order:** the harness's own CONFOUND REGISTER worked exactly as designed —
   confounded phases were reported and flagged, never silently dropped. That design choice
   is what made this finding legible rather than invisible.

## 7. Repair pathway

Node classification (`docs/architecture/work_graph_debt_vocabulary.md`):

- **SWS readout → `complicated (buildable)`.** A named build with no open question:
  replace `sws_denoising_snr` with a readout scored against the injected content, exactly
  as `rem_terrain_variance` → `rem_generative_fidelity` was replaced (ree-v3 `main`
  `da873a1`). Route: **`/implement-substrate`** on
  `ree-v3/experiments/_lib/consolidation_lesion_harness.py`. Experiment-layer only, zero
  `ree_core` change — so **no `substrate_queue.json` entry** (`action: "none"`), matching
  the `festive-neumann-b7b7b4` / `infallible-panini-0ba871` precedent for this same harness.
  The build must keep the backward-compatible key contract and re-validate via a new
  diagnostic letter.

- **REM leg → `complex (probe-gated) / puzzle (known rules)`, ≥2 live hypotheses →
  GOV-FANOUT-1 portfolio.** Do not power-bump the braked design; fan out on distinct axes:

| # | Hypothesis | Axis | Probe sketch | Declared null |
|---|---|---|---|---|
| H1 | The rem null degeneracy is an artifact of the `step=1.0` full-adoption measurement choice driving `calibration_error` into its clamp rails | measurement | re-run the rem leg over a `step` ladder (e.g. 0.1/0.25/0.5/1.0); read whether the null arm leaves the 998.5 constant and the 1e-3 floor | if the null arm stays railed at every `step`, H1 is refuted |
| H2 | The rem calibration readout is genuinely content-independent (like `sws`), and the clamping is incidental | representation | score the rem leg against the injected precision target directly rather than via `running_variance_after`; compare null vs injected slope in common units | if a de-clamped readout yields null_slope_ratio <= 0.25, H2 is refuted |
| H3 | `rem_generative_gain` is a content-free property of the rollout transfer function, not evidence that "correction needs an intact seed" | observation | contrast generative gain at `rem_gen_content_scale` in {0.0, 0.5, 1.0} across seeds; test whether gain varies with content scale at all | if gain scales monotonically with content scale, H3 is refuted and the doc's gloss stands |

  These three are pre-registered into the frozen ledger at Step 9b **before** their
  adjudicating runs exist.

- **Re-derive brake:** does **not** fire. This is the first autopsy on SD-068 (registered
  2026-07-17), and its recommended direction is `weakens` with category `measurement_gap` —
  neither `substrate_ceiling` nor `non_contributory` — so it does not count toward the
  threshold. No same-claim re-queue is refused.

- **Granularity-debt recurrence:** no prior `failure_autopsy_*` doc targets SD-068. First
  autopsy on this target; no `/claim-synthesis` trigger.

## 8. Recommended governance writes — exact text (this skill does NOT apply them)

### 8a. Mark the superseded predecessor

On `v3_exq_sd068_null_content_control_diagnostic_20260718T065939Z_v3.json` (V3-EXQ-778b):

- `evidence_direction: "superseded"`
- `evidence_direction_note`:
  > Superseded by V3-EXQ-778c (`...20260718T072318Z_v3`), which re-ran the identical
  > null-content control at the full 8-seed V3-EXQ-778a set. 778b ran at n=2 and left the
  > rem leg unresolved (per-seed null ratios [4348.47, 0.0], `confound_verdict_stable:
  > false`); its sws (1.0000) and nrem (0.1449) legs are reproduced bit-identically in
  > 778c. Same conclusion, strictly dominated evidence — does not count separately toward
  > SD-068 confidence.

### 8b. SD-068 — narrow, do not demote (user-adjudicated)

`evidence_quality_note` to append on **SD-068**:

> V3-EXQ-778c (diagnostic, n=8, 2026-07-18) ran the pre-registered zero-injected-content
> null control and FAILED the load-bearing C1 on 0/8 seeds. Per phase: `nrem`
> null_slope_ratio 0.1445 (95% CI [0.1438, 0.1451], 0/8 confounded) is cleanly
> content-contingent; `sws` is 1.0000 (sd 2.7e-8, 8/8 confounded) — `denoising_snr_db` is
> a pure noise-power statistic whose content term differentiates away, so it has never
> measured content fidelity; `rem` is degenerate at both rails (exactly 0.0 on 5/8 from a
> saturated `calibration_error` constant, off-scale 1801-9143 on 3/8 from the 1e-3
> precision floor) and is UNINTERPRETABLE at this n (`ceiling_inside_ci95: true`).
> Readiness precondition met and C2 passed, so this is an informative negative about the
> instrument, not a broken run. Per the script's own pre-registration (lines 90-92),
> SD-068's non-vacuity contract is hereby NARROWED rather than withdrawn: it is carried by
> the `nrem` injected-content leg and the REM passthrough-vs-generative contrast, and NOT
> by the `sws` leg. Routing: /implement-substrate to replace `sws_denoising_snr` with a
> content-scored readout (same pattern as `rem_terrain_variance` -> `rem_generative_fidelity`,
> ree-v3 main da873a1). No status or confidence change; diagnostic evidence does not weight
> governance confidence. See failure_autopsy_V3-EXQ-778c_2026-07-18.

### 8c. MECH-168 / INV-047 — amend the annotation banked on 2026-07-17

The 2026-07-17 fold (REE_assembly `c95b2f4a0f`, session `focused-kare-62d137`) banked the
SD-068 staging finding onto these claims. Append to the existing `evidence_quality_note`
on **MECH-168** and **INV-047**:

> AMENDED 2026-07-18 by V3-EXQ-778c (SD-068 null-content control, n=8). The
> "NREM-before-SWS adjacency ROBUST (8/8, sign-test p = 0.0078, 95% CI [0.422, 0.425])"
> half of the 2026-07-17 V3-EXQ-778a staging fold is RETRACTED as evidence of staging: the
> `sws` pole of that adjacency is a content-free readout (null_slope_ratio 1.0000 on 8/8
> seeds, sd 2.7e-8), so the comparison is between a content-contingent readout (`nrem`) and
> a noise statistic (`sws`). The tightness of that CI is the signature of a
> near-deterministic analytic metric, not strength of effect — `sws` tolerance std ~9e-9 vs
> `nrem` 0.0014 and `rem` 0.396. The REM-fails-first half was already CONTESTED /
> underpowered and is unchanged. The 2026-07-17 Leg 2 finding (REM generative gain 0.149,
> 8/8 attenuating) is a different readout and is NOT overturned, though see
> failure_autopsy_V3-EXQ-778c_2026-07-18 H3 for an open question on its content-dependence.
> No confidence change: V3-EXQ-778c tags these claims as CONTEXT only and its per-claim
> evidence_direction is `unknown`. This amends an annotation, not the claims themselves.

### 8d. MECH-169 — amend the fold-note

Append the same retraction, scoped to MECH-169's V3-testable staging half:

> AMENDED 2026-07-18 by V3-EXQ-778c: the SD-068 fold-note's staging-order support is
> narrowed to the `nrem` leg. The `sws` leg is content-free (null_slope_ratio 1.0000, 8/8)
> and the `rem` leg is uninterpretable at n=8; only the `nrem` leg is confirmed
> content-contingent. The glymphatic half remains out of V3 scope. No confidence change.
> See failure_autopsy_V3-EXQ-778c_2026-07-18.

### 8e. SD-068 architecture doc

`docs/architecture/sd_068_consolidation_lesion_harness.md`:
- Leg 1: retract the "ROBUST" wording per §6.3; keep the numbers, add the null-control
  reading and the variance-as-instrument-flag lesson.
- Add a "Null-content control (V3-EXQ-778c)" subsection under Diagnostic results.
- Amend the `sws_denoising_snr` bullet in **Solution** to record that it is content-free
  pending the rebuild.
- Flag line 221's "the correction needs an intact seed" gloss as an open question (H3).

## 9. Routing summary

| Item | Route | Owner |
|---|---|---|
| SWS content-scored readout rebuild | `/implement-substrate` (harness `_lib`, no substrate_queue entry) | next session |
| REM leg H1/H2/H3 portfolio | `/queue-experiment` fan-out after pre-registration | next session |
| 778b supersession + claim annotations | `/governance` (applied this session per user instruction) | this session |
| SD-068 doc amendment | this session | this session |

**Not routed:** no claim demotion, no `/lit-pull` (lit entry present), no
`/claim-synthesis` (first autopsy on target), no re-derive brake, no same-claim re-queue
refusal.
