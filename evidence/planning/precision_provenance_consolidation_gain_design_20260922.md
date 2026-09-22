# Preregistration: precision-provenance-conditioned consolidation gain (V3-EXQ-1073)

**Status:** PRE-REGISTERED DESIGN, constants PROVISIONAL until the Freeze Record (section 15) is
appended. Nothing in sections 1-14 may change after section 15 is written except by a dated
amendment that names what changed and why, before any full-run DV is read.
**Session:** `compassionate-pike-fe9174`, 2026-09-22. **Queue slot:** V3-EXQ-1073 (reserved).
**Intake:** `thought_intake_2026-09-22_behavioral_precision_provenance_and_sleep_plasticity_gain.md`.
**Substrate it runs on:** SD-PP-1..4 (`docs/architecture/precision_provenance_substrate_spec.md`);
necessities register `precision_provenance_substrate_necessities_20260922.md`.
**Claims tagged:** MECH-572 (lead). `experiment_purpose = "diagnostic"` (mechanism probe: the
producers are new substrate and two of their quantities are named proxies; see section 14 for the
evidence level).

---

## 1. Causal question

Does preserving behaviourally grounded epistemic provenance from waking experience, and using it
ONLY to regulate later sleep-time plasticity gain, improve consolidation compared with the
existing fixed-gain mechanism, without creating a self-sealing protection for confidently wrong
representations?

Not asked: "can sleep be made less destructive" (a smaller lr does that; ARM D-global is that).

## 2. Three precision quantities (kept distinct, each with a named producer)

| quantity | producer | read when | proxy limitations |
|---|---|---|---|
| historical model precision `pi_hist` | SD-PP-2 `precision_at()` | at the waking test, BEFORE the outcome | EMA source is global/state-blind; SD-063 source per-state but total-spread minus noise |
| evidence precision `pi_e` (z units) | SD-PP-1 `evidence_precision_z` | at the outcome | frame-difference MAD statistic; kappa measured on motion, applied to noise (conservative) |
| current model precision `pi_cur` | SD-PP-2 `current_read()` | at sleep entry | same producer as `pi_hist`, later time |

Historical precision is provenance, not protection: it enters the gain rule ONLY through the
surprise reopen factor `r_i >= 1` (section 5). Any implementation in which high `pi_hist` reduces
learning is invalid for the main hypothesis (SD-PP-4 test 3 pins this).

## 3. Metadata packet (SD-PP-3, schema 1) -- the minimum that distinguishes the three

`pred_at_test`, `pe`, `pi_hist` (+ `v_tot_hist`, `v_ale_hist`, `precision_source`),
`evidence_variance_z`, `evidence_precision_z`, `sigma_obs`, `kappa`, `evidence_ready`,
`surprise = pi_hist * max(pe - noise_gain * evidence_variance_z, 0)`, `buffer_index`, `tick`,
`provenance="real"`, `has_prev`. No field is computed from any later tick (SD-PP-3 test 3).
Not stored: behavioural success/failure (no producer; registered B1), timestamp beyond `tick`.

## 4. The consolidation path under test (unchanged content, order, count)

`SleepLoopManager.force_cycle -> CrossModuleConsolidator.consolidate({"e1","e2","e2_world"})`,
fresh Adam per module, 8 steps, base lr 1e-3, batch 16, `compute_e2_world_loss` drawing
`torch.randperm` batches. The manipulation touches ONLY the `e2_world` module's per-row loss
weights and per-step lr. The `randperm` draw is identical across arms at a given (seed,
condition, cycle) because no arm consumes extra RNG (pinned by the A/B bit-identity gate).

## 5. Gain rule (SD-PP-4, exact; constants provisional until section 15)

```
K_i    = pi_e_i / (pi_e_i + pi_cur)                                     write authority (Kalman form)
m_i    = sqrt( max(pe_i - NOISE_GAIN * ev_var_i, 0) / V_REF )            epistemic innovation magnitude
r_i    = min( R_MAX, 1 + BETA * max(0, ln(surprise_i)) )                 reopen factor (historical precision enters only here)
gain_i = clip( G_MAX * K_i * m_i * r_i, G_MIN, G_MAX )
loss   = sum_i gain_i * l_i / sum_i gain_i ;   lr_step = lr * mean_i gain_i
NOISE_GAIN = 2.0   V_REF = 1e-2   BETA = 0.5   R_MAX = 3.0   G_MIN = 0.02   G_MAX = 2.0
SD-PP-1/2: obs_ema_alpha 0.2, kappa_ema_alpha 0.05, sigma_floor 0.005, pe_ema_alpha 0.05, v_floor 1e-6, v_init 1e-2, source sd063_or_ema
```
Justifications: `K` is the Bayesian posterior weight of evidence against belief; `m` restores the
innovation magnitude a fresh Adam discards (MECH-572); `V_REF` is the fresh-base residual scale
from the LANDED V3-EXQ-1063 manifest (2.8e-3..1.2e-2), not from this run; `NOISE_GAIN=2` from the
near-identity head (MECH-573). No constant is set from any post-sleep readout of this run.
Provisional means: the pre-run non-degeneracy probe (section 9) may reveal a constant that makes
a channel degenerate (e.g. `V_REF` so large every `m_i` floors); such a change is recorded in
section 15 with the probe statistic that motivated it, BEFORE any DV is read.

## 6. Arms (all fork from the identical pre-sleep state per seed x condition)

| arm | metadata recorded | gain | purpose |
|---|---|---|---|
| A `ARM_A_BASELINE` | no | fresh Adam, fixed lr | current behaviour; reproduces MECH-572 phenotype in condition 1 |
| B `ARM_B_STORE_ONLY` | yes | as A | storage neutrality |
| C `ARM_C_PROVENANCE` | yes | rule, mode `provenance` | treatment |
| C0 `ARM_C_NOHIST` | yes | mode `provenance_nohist` (`r_i=1`) | is historical precision load-bearing (intake F1)? |
| Dg `ARM_D_GLOBAL` | yes | mode `global`, `global_scale = c_seed` | matched-budget rival: "any lr reduction works" |
| Dr `ARM_D_RESIDUAL` | yes | mode `residual_only`, `global_scale = c_seed` | matched-budget rival: current residual only (no evidence/historical precision; intake F2) |

`c_seed` = mean of ARM C's realised per-row gains pooled over ALL conditions, cycles and steps for
that seed (computed from C's gain diagnostics, never from any DV). D arms run after C for the
seed. Budget equivalence is therefore exact in total and deliberately NOT per condition: the
rival hypothesis is a single global reduction.

## 7. Conditions (each a separate waking regime; seed-paired across arms)

| cond | base | P1 waking | retention battery | correction battery | epistemic regime (hist, ev, cur) |
|---|---|---|---|---|---|
| 1 `COND_CONVERGED_CLEAN` | P0 3600 steps converged | clean, rule R0 | R0 clean | -- | high, high, high -- avoid destructive displacement |
| 2 `COND_UNDERFIT` | P0 0 train steps (V3-EXQ-1063 FRESH regime) | clean, R0 | R0 clean | -- | low, high, low -- keep learning |
| 3 `COND_CONFIDENTLY_WRONG` | converged | rule R1 = R0 with action map inverted (swap 0<->1, 2<->3), reliable | R0 clean ("letting go") | R1 clean | high, high, cur drops -- must reopen |
| 4 `COND_NOISY_CONTRADICTION` | converged | R0 + additive obs noise sigma 0.12 on world_state (798a/1071 hook) | R0 clean | -- | high, LOW, cur epi high -- must not learn the noise |

Batteries are captured once per seed before P0 with the (never-trained) encoder, from held-out
env instances (seed+9973; R1 battery from the same instance with the same permutation applied),
fixed random action policy, pure read (V3-EXQ-1063 `_sample_probe_battery` form). Conditions 3
and 4 are the "large but reliable" vs "large but unreliable" pair; their waking PE distributions
are recorded and reported (matching is approximate; sigma 0.12 is 798a's MEL-match to its HIGH
shift arm).

Factorial mapping (hist x ev x cur): the four conditions realise (H,H,H), (L,H,L), (H,H,L->drop),
(H,L,H). This is a reduced matched subset, chosen because the full 2x2x2 would require
manipulating evidence precision inside the converged-clean regime, which the same noise hook
provides only as condition 4. The three quantities are still separately identified: `ev` by
cond 4 vs 3, `cur` by cond 1 vs 2, `hist` by ARM C vs C0 within cond 3.

## 8. Readouts (per seed x condition x arm x cycle)

Mechanistic: per-step gain (mean/min/max/sd, `n_missing`), per-step lr scale, grad norm,
`world_head_max_abs_delta`, displacement / pre-sleep residual ratio, packet distributions
(`pi_hist`, `pi_e`, `pe`, `surprise`), `pi_cur` at sleep entry, replay batch count/order hash,
optimiser: fresh Adam (asserted), `adam_step_bound = n_steps * lr`.
Representation: pre/post battery MSE on every battery above; `identity_predictor_mse` and skill
`1 - MSE/MSE_identity` (MECH-573); retention = `post/pre - 1` on the retention battery;
correction = `(pre - post)/pre` on the R1 battery (cond 3); let-go = `post/pre - 1` on R0 in cond 3.
Organism-level: NONE AVAILABLE (section 14).

## 9. Pre-run gates (STOP conditions; smoke + liveness probe, before section 15)

G1 liveness: at a pinned seed, `world_head_max_abs_delta` strictly increasing over `global_scale`
in (0.1, 0.5, 1.0, 2.0) (SD-PP-4 test 10, and re-measured in the driver's `--liveness` mode).
G2 A/B neutrality: world buffers and world-head parameters BITWISE identical between A and B after
cycle 1 (tolerance 0); replay batch draws identical across all six arms (hash).
G3 evidence channel varies: `evidence_precision_z` in cond 4 < 0.25 x cond 1 (per seed), and does
NOT differ between cond 1 and cond 3 by more than 2x (evidence precision must not alias the
rule shift).
G4 historical precision varies: within-run SD of `pi_hist` over packets > 0 in every condition,
and cond 3 early-post-shift packets carry `surprise` > 10 while cond 1 packets sit at median < 3.
G5 current precision varies: `pi_cur` cond 1 > 10 x `pi_cur` cond 2.
G6 consolidator displaces: `world_head_max_abs_delta` > 0 in ARM A of every condition.
G7 readouts have variance: across-sleep MSE delta in ARM A has non-zero SD across seeds and is
not pinned at 0 in any cell; no arm's post-sleep MSE saturates at floor (< 1e-8) or explodes (nan).
G8 readability (MECH-573): converged-base skill vs identity predictor > 0 on >= 2/3 seeds; if not
met the retention contrasts in conds 1/3/4 are recorded `non_degenerate=False` and the run
continues for cond 2 and the mechanistic readouts only.
G9 PE separation (B5): mean waking PE in cond 3 > 2 x converged residual on >= 2/3 seeds; else
cond 3 is `non_degenerate=False`.
Any of G1-G6 failing -> outcome FAIL, label `substrate_not_ready_requeue`, no DV read.

## 10. Seeds, pairing, statistics

Seeds (42, 123, 456) -- V3-EXQ-1063's set, fixed here. Every arm of a (seed, condition) starts
from the identical pre-sleep state (same P0 cache, same waking RNG); D arms too. Report per-seed
paired deltas for every contrast, mean, SD, and a t-based 95% CI (n=3, flagged low-power); a
"2/3 seeds" sign count is the pre-registered decision rule, the CI is descriptive.
Exclusions (pre-registered): a cell with a non-finite parameter after sleep is excluded and named;
no other exclusion. All seeds reported.

## 11. Primary contrasts and thresholds

Let `ret(arm)` = retention-battery `post/pre - 1` (0 = unchanged, +1 = doubled error),
`corr(arm)` = R1-battery `(pre - post)/pre`, MARGIN = 0.02 x pre-MSE-equivalent, i.e. 2% relative.
- **P1 A vs B (equivalence):** bitwise identical (G2); readout tolerance 0.
- **P2 B vs C, cond 1 (protection):** `ret(C) < ret(B) - MARGIN` on >= 2/3 seeds AND `ret(C) < 0.10`
  on >= 2/3 seeds (post-sleep error rise at most 10% of residual; MECH-572 phenotype is >= 100%).
- **P3 B vs C, cond 2 (still learns):** `ret(C) <= ret(B) + MARGIN` on >= 2/3 seeds (C not worse
  than baseline learning on the underfit base).
- **P4 anti-self-sealing, cond 3:** `corr(C) >= corr(B) - MARGIN` on >= 2/3 seeds AND `corr(C) > 0`
  on >= 2/3 seeds. Failure of either = self-sealing (Result 3) regardless of P2.
- **P5 evidence precision, cond 4:** `ret(C) < ret(Dr) - MARGIN` on >= 2/3 seeds (C ignores the
  noise; residual-only learns it).
- **P6 C vs Dg (beyond generic reduction):** C beats Dg on P2 AND P4 simultaneously on >= 2/3 seeds
  (`ret(C) < ret(Dg) - MARGIN` in cond 1 and `corr(C) > corr(Dg) + MARGIN` in cond 3). Dg is expected
  to pass P2 (small lr protects) and fail P4 (small lr under-corrects) -- that split is the whole
  point of the matched budget.
- **P7 C vs C0 (historical precision load-bearing, F1):** `corr(C) > corr(C0) + MARGIN` in cond 3 on
  >= 2/3 seeds; a null here is a RESULT (historical precision not shown to add information).
MARGIN is an absolute floor; where per-seed SDs of the paired deltas exceed it, the SD-scaled
margin (1 SD) is reported alongside and the decision uses the larger.

## 12. Interpretation matrix (pre-registered)

| result | pattern | interpretation | governance recommendation |
|---|---|---|---|
| R1 | P2, P3, P4, P6 pass | provenance contributes information beyond generic gain reduction | supports precision-provenance mechanism (mechanistic level only, section 14); do NOT promote |
| R2 | P2/P4 pass but P6 fails (C ~ Dg) | MECH-572 is an optimiser/gain-scheduling defect; provenance not shown to add value | generic gain correction sufficient; prefer the simpler mechanism |
| R3 | P2 pass, P4 fail | self-sealing precision dynamics | self-sealing failure; analyse whether `pi_hist` acted as authority (check `r_i` and `K_i` traces); no threshold rescue |
| R4 | internal readouts pass, no behavioural endpoint | mechanistic/local success only | requires organism-level follow-up (B1) -- this is the CEILING of this run by construction |
| R5 | G1 or G6 fail | gain manipulation inert / consolidator does not displace | instrument/substrate non-diagnostic; not evidence against the hypothesis |
| R6 | G3/G4/G5 fail | a precision channel does not survive the waking-to-replay path at this operating point | substrate non-diagnostic; route to the B-rows |
| R7 | P5 fails (C learns noise like Dr) | evidence precision adds nothing beyond raw error (intake F2) | weakens the evidence-precision component only |
| mixed | any other | report the pattern; no rescue | mixed/inconclusive |

## 13. Red-team (adversarial design review, disposed before freeze)

1. *Can C win merely because its mean lr is smaller?* -- Dg has the SAME total budget; P6 requires
   C to beat Dg on protection AND correction, which a uniform reduction cannot do.
2. *Can C appear stable by freezing all learning?* -- P3 (cond 2) and P4 (`corr(C) > 0`) both fail
   under freezing; G_MIN = 0.02 keeps a floor.
3. *Is prediction precision independent from residual?* -- Not fully: the EMA source is 1/EMA(PE).
   Independence is obtained in TIME (pi_hist is read before the outcome; pi_cur at sleep entry)
   and through the SD-063 per-state source when ready. Cond 3's early-post-shift packets are the
   case where pi_hist and pe decouple (high, high); G4 checks it exists.
4. *Is evidence precision genuinely manipulated or a renamed outcome magnitude?* -- SD-PP-1 never
   reads the model or the outcome; G3 requires it NOT to move under the rule shift (cond 3) while
   it does under noise (cond 4).
5. *Can future information leak into the packet?* -- SD-PP-2 `precision_at` before
   `observe_outcome`, enforced inside `ReplayProvenanceRecorder.record` and tested (SD-PP-3 test 3).
6. *Is the confidently-wrong case genuinely high-confidence before contradiction?* -- G4 (surprise
   > 10 on early post-shift packets) is the measured check; the base is the SAME converged head as
   cond 1 (G5/G8).
7. *Does ARM D represent the rival adequately?* -- two D arms: uniform reduction (Dg) and
   current-residual scheduling (Dr), both budget-matched.
8. *Does the optimiser make nominal gain differences ineffective?* -- G1 liveness on displacement,
   plus the per-step lr scaling is the mechanism precisely because per-row weights alone would be
   normalised by Adam.
9. *Are replay selection and gain coupled?* -- same `randperm` stream; batch hash asserted equal
   across arms (G2).
10. *Can the behavioural endpoint move independently of the internal metric?* -- there is no
    behavioural endpoint in this run (section 14); the claim is capped accordingly.
11. *Is any criterion guaranteed by construction?* -- P1 (A=B) is guaranteed IF the recorder is
    RNG-free; that is what it tests. G6 is guaranteed on a fresh base; it is a readiness check,
    not a result.
12. *Oracle information?* -- the rule-shift permutation and the noise sigma are never read by the
    organism; the batteries are instrument-side.
13. *Null from saturation / dead channels / unread metadata / absent consumer?* -- G3-G7 and the
    `n_missing` diagnostic (must be 0 for rows with `has_prev`) cover each.
14. *Encoder dynamic range (B5)* -- G8/G9 mark cond 3 and the retention contrasts non-degenerate
    rather than letting a compressed signal read as a null.

## 14. Evidence level statement

No default-on consumer of `e2.world_forward` exists in E3 (register B1), so this run cannot
produce an organism-level endpoint. Its ceiling is Result 4: mechanistic/local. It is registered
`experiment_purpose="diagnostic"` and its manifest will carry `evidence_direction:
non_contributory` with the pattern in `interpretation.label`; governance may cite the
mechanistic pattern but must not promote MECH-572 or register a new claim from it. The
organism-level follow-up is a separate chip on B1.

## 15. Freeze record

(to be appended after the smoke / liveness / non-degeneracy probes, before the full run; must
list every constant with its final value, every gate's measured value, and any constant changed
since section 5 with the probe statistic that motivated it)

---

## 15. Freeze record (appended 2026-09-22, session `compassionate-pike-fe9174`, BEFORE the full run)

**Substrate:** SD-PP-1..4 landed on ree-v3 `main` (commit named in the queue entry); remote suite 6493 passed
+ the flag-registry fix; 45 new contract tests + 7 integration contracts green. Driver
`experiments/v3_exq_1073_mech572_precision_provenance_gain.py`, validator `--strict` clean, red-team
(Step 4.5) CONTESTED with 8 findings, all applied (below).

**Probe artefacts (waking-channel statistics, seed 42, full P0 3600 + full 180-step calibration, one
cycle; the run's own `--probe` mode reproduces them):**

| cond | ev_var median | sigma_obs | kappa | pi_hist sd | surprise median | frac>10 | pe_mean | pi_cur | skill |
|---|---|---|---|---|---|---|---|---|---|
| converged clean | 3.53e-9 | 0.005 (floor) | 1.41e-4 | 1.84e5 | 0.68 | 0.006 | 4.53e-6 | 6.22e5 | -0.071 |
| underfit | 1.16e-8 | 0.005 | 4.63e-4 | 7.2 | 1.02 | 0 | 7.61e-3 | 134 | -540 |
| confidently wrong | 5.28e-9 | 0.005 | 2.11e-4 | 3.65e4 | 0.79 | 0.006 | 1.11e-5 | 1.84e5 | -0.071 |
| noisy contradiction | 1.59e-6 | 0.119 | 1.08e-4 | 2.75e5 | 0.49 | 0.006 | 6.96e-6 | 7.11e5 | -0.071 |

ARM C realised gain per condition (k / m / r means, step scale): converged 0.997 / 0.022 / 1.06 ->
**0.038**; underfit 1.0 / 0.86 / 1.01 -> **1.78**; confidently wrong 0.999 / 0.031 / 1.02 -> **0.072**;
noisy 0.440 / 0.015 / 1.12 -> **0.027**. The four regimes separate ~67x, and the Kalman term is the
factor that discounts the noisy condition (k 0.44 vs ~1.0 elsewhere).

Attainability ladder (global scale -> displacement -> retention_r0, seed 42): 0.02 -> 1.6e-4 -> 0.078;
0.05 -> 4.0e-4 -> 0.47; 0.1 -> 8.0e-4 -> 1.80; 0.5 -> 4.0e-3 -> 22.1; 1.0 -> 8.0e-3 -> 19.8; 2.0 ->
1.6e-2 -> 18.8. Displacement is exactly linear in the scale (G1 live); retention is NON-monotone above
scale 0.5.

**Gate outcomes at full budget (seed 42):** G3 leg 1 0.0022 (< 0.25) pass; G3 leg 2 sigma_obs equal at
the floor pass; G3b 0.579 (<= 2.0) pass; G4 pass; G4b FAIL (early surprise frac 0.033 vs >= 0.5);
G5 4628x pass; G8 FAIL (skill -0.071); G9 FAIL (pe ratio 0.74 vs > 2.0).

**Pre-freeze amendments, each motivated by a probe statistic, none by a post-sleep DV of the full
run** (the seed-42 probe did print cycle-1 retention values; no threshold or constant was changed in
response to them, and the two changes below to P2 are motivated by the LANDED V3-EXQ-1063 numbers and
the ladder, which reads a global-scale arm, not ARM C):

1. **Calibration window (A1).** Every arm cell starts from the cached P0 head with NO estimator
   history, so `pi_hist` began at exactly `1/v_init = 100` in every condition (probe). A 180-step clean
   calibration window (env seed+2, never used by any condition) now runs once per base and its
   estimator state (SD-PP-1/2 `get_state`) is restored identically into every arm. Effect: converged
   `v_tot` 5.1e-6 vs underfit 7.9e-3 at P1 entry; G5 moved from 3.7x (cold) to 4628x.
2. **G3 statistic (A2).** The original leg averaged `evidence_precision_z` (a 1/x quantity dominated by
   cold-start frames: 0.66 ratio); it now uses the packet MEDIAN of `evidence_variance_z` (0.0022).
   Threshold unchanged (0.25).
3. **G3 leg 2 rescoped (A2'/F2).** The kappa-ratio leg (|log2| <= 1) tested kappa invariance between
   two CLEAN regimes, and kappa is measured on motion (SD-PP-1 limitation; register B7). It is now the
   non-routing marker G3b with threshold 2.0 (a 2x kappa shift moves K by ~1%), and the verdict-routing
   leg 2 is the direct assertion the old leg meant: sigma_obs medians of cond 1 and cond 3 equal, AT the
   floor. Measured: G3b 0.579 at full budget (3.795 at a 30-step calibration).
4. **G4 split (A3).** G4 keeps the `pi_hist`-varies leg as verdict-routing; the surprise leg is now G4b,
   non-routing, marking P4/P7 (and P6's correction leg) `non_degenerate=False` when unmet. Reason: the
   converged head is near copy-the-input (skill -0.071, MECH-573) and barely reads the action, so
   inverting the action map is not a contradiction (inverted-rule battery MSE 1.13e-5 vs original
   1.49e-5). This is substrate necessity **B5**, measured; G9 fails for the same reason. Condition 3
   and ARM C-nohist stay in the run so that the finding is recorded on three seeds.
5. **P2 restated (F1).** The absolute ceiling `ret(C) < 0.10` was scaled against "MECH-572 rise ~100%";
   the landed V3-EXQ-1063 seed-42 rise is ~480% over three cycles, and the ladder shows `ret < 0.10`
   needs a budget below ~0.022 while ARM C's realised converged gain is 0.038. The load-bearing P2 leg
   is now `ret(C) < ret(B) - margin` (protection relative to baseline); the absolute bar is reported as
   the non-routing P2b ("MECH-572 rise within 10% of residual"). No gain constant changed.
6. **ARM D-residual redesigned (batch 4).** As built, `residual_only` inherited the pooled global
   budget `c_seed` (~0.48, dominated by the underfit condition's 1.78), so it could not reallocate
   budget across conditions and was a weak rival. It now schedules from the CURRENT per-row residual:
   `g_i = clip(G_MAX * sqrt(pe_cur_i / V_REF), G_MIN, G_MAX)`, no stored packet, no precision term
   (i.e. C's magnitude factor with K = 1, r = 1 and the current rather than stored innovation). ARM
   D-global is unchanged and is the matched-TOTAL-budget rival; its per-condition budget skew (Dg ~12x
   C's gain in cond 1, ~7x in cond 3) is recorded in the manifest and P6 must be read against it.
7. **Preconditions tightened (F3):** packets-per-buffer-entry >= 0.99; gain rows with provenance
   >= 0.9. **Consumer-liveness marker (F4):** G1b, ARM C's realised step scale must differ from 1.0
   (0.976 at seed 42). **Pairing (F5):** encoder-parameter hash asserted against the base build; action
   buffer and post-cycle RNG hashes added to G2. **Budget ratios (F6)** recorded per condition.
   **`--probe` mode (F7)** is the freeze artefact. **Docs (F8):** R3 requires P2 pass AND P4 fail;
   R7 reachable only when R1/R2/R3 do not fire; `precision_source` is `"ema"` on every packet (SD-063
   head off in every arm), so `pi_hist` is global and state-blind.

**Frozen constants:** NOISE_GAIN 2.0, V_REF 1e-2, BETA 0.5, R_MAX 3.0, G_MIN 0.02, G_MAX 2.0,
obs_ema_alpha 0.2, kappa_ema_alpha 0.05, sigma_floor 0.005, pe_ema_alpha 0.05, v_floor 1e-6, v_init 1e-2,
source sd063_or_ema (resolves to ema), CALIB_STEPS 180, seeds (42, 123, 456), N_CYCLES 2, MARGIN 0.02,
G3 0.25, G3b 2.0, G4b 0.5 / 3.0, G5 10, G9 2.0, LIVENESS_SCALES (0.02, 0.05, 0.1, 0.5, 1.0, 2.0).

**Expected disposition, stated before the run:** P1 passes (by construction, that is its job); P3 is
the one contrast expected both readable and informative; P2 (relative) likely passes; P2b likely fails;
P4/P6-correction/P7 will be marked non-degenerate on every seed where G4b/G9 fail (B5); P2/P5/P6 are
marked non-degenerate on seeds where the converged base fails MECH-573's skill > 0 (1063: seed 123
+0.227, seeds 42/456 negative). The citable yield is therefore: A/B neutrality, the factor-by-factor
mechanism readout (k/m/r per condition), the attainability curve, P3, and a three-seed instrument
record that condition 3 is unposeable on this head. Ceiling remains Result 4 (mechanistic/local).
