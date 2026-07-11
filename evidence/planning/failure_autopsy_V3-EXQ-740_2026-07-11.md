# Failure Autopsy — V3-EXQ-740 (INV-064 maturational-sequence necessity)

- **Generated (UTC):** 2026-07-11T21:41:41Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered)
- **Run:** `v3_exq_740_inv064_maturational_sequence_e3_bounded_20260711T211644Z_v3`
- **Queue id:** V3-EXQ-740 · **Claim:** INV-064 (`development.maturational_sequence`)
- **Outcome:** FAIL · `evidence_direction=unknown` · `non_degenerate=false`
- **Machine:** ree-cloud-2 · seeds [42, 7, 19] · onset_episodes [2, 5, 11, 22]

## 1. Claim under test

INV-064 (`e1_e2_e3_maturational_sequence_necessity`, invariant / emergent from ARC-001/002/003/019;
status **candidate**, `pending_substrate_reconfirmation: true`): E3's harm/goal evaluator quality is
**strictly bounded** by E1/E2 representational differentiation — poorly-differentiated z_world /
action_objects inputs yield a noise-fitted E3 evaluator, so productive E3 training cannot begin until
E1/E2 have reached sufficient schema differentiation. Grounded in a real developmental fact:
prefrontal cortex is the last cortex to myelinate (completing mid-20s), and the sensory(E1) →
motor(E2) → frontal(E3) maturation order is asserted to be a *computational necessity*, not an
anatomical accident.

## 2. Facts reconstruction (no interpretation)

**Design (commitment-free, frozen-representation curriculum-order contrast).** Per (seed, onset ∈
{2,5,11,22}): (1) mature E1 + E2.world_forward + encoder for `onset` episodes via the canonical
`goal_pipeline_tier1.warmup_train` (the incidental harm_eval head is discarded); (2) freeze
E1 / E2.world_transition / E2.world_action_encoder / latent_stack; (3) collect a **shared** harm
dataset by replaying a fixed seeded action sequence through a fixed env (raw trajectory + harm labels
*identical* across the 4 onset arms of a seed — only the frozen encoder's z_world differs); (4) re-init
`agent.e3.harm_eval_head` to a bit-identical shared init and train **only** that head for a fixed
budget (E3_EPOCHS=40) on the frozen-encoded (z_world, harm_target) tensors; (5) read held-out harm R²,
train R², and the train–test gap.

- **IV** = onset episodes (E1/E2 maturity at E3 onset).
- **Validity precondition** `PC_iv_moved` = `mean_seed(eff_rank[onset_max] / eff_rank[onset_min]) ≥ 1.15`
  (E1 differentiation, measured by z_world effective-rank / participation ratio, must actually increase).
- **DV** = harm_eval held-out R² and gap = train R² − test R².
- Regime: `scheduled_external_hazard_enabled=False` (537b lesson — by-design-unpredictable ext events
  floor harm R² regardless of maturity), so harm is predictable-from-state and E1/E2 differentiation is
  the intended binding constraint.

**Observed — the IV ran backwards and floored (z_world is 32-dim):**

| onset | mean z_world eff_rank | mean E2 forward R² | mean held-out harm R² |
|---|---|---|---|
| 2 (least mature) | **1.477** ← highest | 0.989 | −0.427 |
| 5 | 1.088 | 0.995 | −0.142 |
| 11 | 1.247 | 0.981 | −0.235 |
| 22 (most mature) | 1.041 | 0.990 | −0.353 |

- per-seed eff_rank ratio (onset_max/onset_min): **[0.855, 0.493, 0.962]**, mean **0.770** — every seed
  below 1.0: z_world differentiation **decreased** as maturation increased.
- Effective rank ~1–2 out of 32 available dimensions at **every** arm → near rank-1 collapse throughout.
- E2 forward R² ≈ **0.99 at onset_2 already** → the world model is saturated at the *earliest* arm.
- DV vacuous-but-recorded: `mean_delta_r2` 0.074 with SD 0.438; per-seed ΔR² [−0.189, +0.580, −0.168];
  held-out harm R² negative in all 4 arms; per-seed Spearman(onset, R²) [−1.0, +0.2, −1.0].
- `PC_events` = true (min harm_event_frac 0.878 ≫ 0.03 floor) — harm was plentiful; not the problem.

**Failed criterion:** the **validity precondition** `PC_iv_moved` (not a discrimination criterion). The
differentiation gradient the probe requires was never established, so C1/C2/C3 are moot. The
non-degeneracy guard fired correctly and self-routed `non_degenerate=false`, `evidence_direction=unknown`
— the guard did its job (this is the V3-EXQ-642 / V3-EXQ-047m pattern: a precondition for a well-posed
contrast was never met).

## 3. Claim-layer mapping

`claim_ids=[INV-064]` is **accurate** (not an inherited-tag artifact). The probe faithfully targets the
load-bearing E1/E2-world → E3-harm leg (`e3_selector.harm_eval` reads z_world). But it did **not** test
the claim under conditions where the claim could express itself: the claim predicts a bound that becomes
visible only across an *immature → mature* differentiation gradient, and no such gradient existed in the
run (see §5). An unmet validity precondition must not be read as pressure on the invariant.

## 4. Biological-reference triage

- **Closest reference mechanism:** cortical maturation order — sensory/perceptual regions myelinate and
  differentiate first, association/premotor next, prefrontal last (mid-20s). This is a robust
  developmental-neuroscience finding, **not** a formal-definition import (no Pearl/Shannon/optimal-control
  abstraction is standing in for a mechanism here). The class existence proof is **strong**.
- **Formal-import? No.** So biology-divergence-is-load-bearing does not apply, and the primary output is
  **not** a `/lit-pull` commission. Lit grounding for the developmental ordering is not the bottleneck;
  the bottleneck is the V3 *operationalisation* of "differentiation."
- **Missing-dependency signature? No.** The failure does not resemble a biological system missing a
  dependency of the maturation mechanism. It resembles a **measurement artifact**: the chosen observable
  of "differentiation" (participation-ratio effective rank of a temporally-smoothed EMA world-latent,
  sampled over a random-action replay) moves *opposite* to the differentiation the claim means. In real
  cortex, maturation increases *task-relevant discriminability* (a trained manifold decodes more
  categories) even as raw dimensionality of the active representation contracts onto a task manifold —
  exactly the direction eff_rank penalises.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | claim never expressed itself — the IV was vacuous |
| Biological reference | **clear** | PFC-last-myelination; E1→E2→E3 order; strong class existence proof; not a formal import |
| Dependency / prerequisites | present | `warmup_train` / ARC-019 curriculum runs, but yields a saturated rep from the earliest arm |
| Implementation completeness | partial | maturation "works" but z_world saturates by onset_2 (E2 R²≈0.99) → no genuinely-immature arm |
| Environment adequacy | adequate | dense predictable harm present (event_frac 0.88); not the binding issue |
| **Measurement adequacy** | **misleading (dominant)** | eff_rank of an α_world=0.9 **EMA** z_world over a *random-action* replay *decreases* with maturation — a trained EMA world-latent specialises onto a low-dim task manifold, so trajectory-covariance rank runs **opposite** to INV-064's "differentiation" (task-relevant discriminability, which increases) |
| Integration adequacy | n/a | single-module frozen-representation probe |
| **Scale / window** | **too narrow (co-dominant)** | onset 2..22 is entirely post-saturation (E2 R²≈0.99 at onset_2) — no immature→mature gradient exists to exercise, regardless of metric |

**Recommended `epistemic_category`: `measurement_degeneracy`.** The IV observable is confounded and the
onset window is post-saturation, so the maturational contrast was structurally un-exercisable — the run
carries no interpretable signal *on INV-064*, but does carry a clear *methodological* signal about how to
operationalise "differentiation" on the V3 substrate.

## 6. Learning extracted

1. **eff_rank / participation ratio is the wrong differentiation observable for a smoothed world latent.**
   With `alpha_world=0.9`, z_world is a heavily temporally-smoothed EMA; over a random-action replay its
   covariance is dominated by low-frequency drift and specialises onto a ~rank-1 task manifold as it
   matures. Effective rank therefore *decreases* with training — opposite to the task-relevant
   discriminability INV-064 means. A trained, task-specialised representation is *lower* raw rank, not
   higher.
2. **The onset window sat entirely in the saturated regime.** E2 forward R² ≈ 0.99 at onset_2 means there
   was no genuinely-immature anchor: 2..22 episodes are all past the point where the world model is
   trivially predictable. Any correct differentiation metric would still see little gradient without an
   immature anchor (onset ~0–1, or an explicit E1-capacity degradation arm).
3. **Secondary observation (carry, do not over-read):** held-out harm R² is negative in *all* arms while
   E2 forward R² ≈ 0.99 — z_world predicts its own forward dynamics almost perfectly yet carries little
   held-out harm information at any maturity. This is confounded here by the vacuous IV; the redesign
   should verify harm is decodable-in-principle at the mature anchor (a positive control) before reading
   the gradient, so a genuine "z_world carries no harm info" substrate finding is not mistaken for
   "differentiation doesn't help."
4. **The precondition guard worked.** Infrastructure behaved correctly — the run self-routed
   `non_degenerate=false` rather than emitting a spurious `weakens`. No code defect in the guard.

## 7. Repair pathway (user-confirmed at the interactive gate)

**Work-graph classification:** `complex (probe-gated) / puzzle (known rules)` — the frame (curriculum-order
contrast on a frozen representation) is well-posed; a *fact* is missing (does a genuine
differentiation→E3-quality bound appear once the IV is made to move?). The fix is a **corrected re-queue**,
not a substrate build and not more of the same.

- **Route: `/queue-experiment` — single corrected successor V3-EXQ-740a** (new alphabetic letter: same
  scientific question, corrected operationalisation). Not a fanout (the two levers below form one coherent
  redesign, not a discrimination between mutually-exclusive hypotheses). Required elements:
  1. **IV-moving differentiation observable** that *increases* with maturation — replace raw eff_rank with
     a **task-relevant discriminability** metric: e.g. linear-probe decodability of harm-relevant world
     features (or world-state identity) from the frozen z_world; OR eff_rank computed over a *controlled,
     diverse probe-set of distinct world configurations* rather than a random-action replay trajectory (so
     rank reflects schema capacity, not EMA drift).
  2. **A genuinely-immature anchor arm** — extend onset to include ~0–1 episodes (near-fresh encoder)
     and/or add an explicit E1-capacity degradation arm, so an immature→mature gradient actually exists.
     Justification: E2 forward R² ≈ 0.99 at onset_2 shows 2..22 is all saturated.
  3. **Keep the `PC_iv_moved`-style non-degeneracy guard**, now on the corrected observable and checking
     the IV moved *in the predicted direction*; add a **mature-anchor harm-decodability positive control**
     so a null gradient is not confounded by an undecodable harm target.
  4. `supersedes: V3-EXQ-740`; `claim_ids=[INV-064]`; `experiment_purpose=evidence`.
- **No substrate build** (`recommended_substrate_queue_entry.action = none`) — the substrate carries the
  information (E2 R²≈0.99); the gap is measurement + test design, not a missing mechanism.
- **No demotion, no `/lit-pull`** — biology is a strong existence proof and not a formal import.
- **Re-derive brake: NOT fired** — this is the first `substrate_ceiling`/`non_contributory` autopsy for
  INV-064 (count 1 < threshold 2). Note for the next cycle: a *second* non_contributory / degenerate INV-064
  autopsy would implicate the operationalisation itself → route to a test-bed/measurement redesign, not a
  third letter circling the same observable.

## 8. Draft `evidence_quality_note` (governance writes this; not written here)

> V3-EXQ-740 (INV-064 maturational-sequence necessity) FAILed on the **validity precondition only**
> (`PC_iv_moved`): mean z_world eff_rank ratio 0.770 < 1.15 — E1/E2 differentiation did *not* increase
> across the onset {2,5,11,22} schedule; it ran backwards (per-seed [0.855, 0.493, 0.962]). Root cause is
> **measurement + design**, not claim pressure: (a) eff_rank / participation-ratio of the α_world=0.9 EMA
> z_world sampled over a random-action replay *decreases* with maturation (a trained EMA latent
> specialises onto a low-dim task manifold), opposite to INV-064's "differentiation" (task-relevant
> discriminability); (b) the onset window is entirely post-saturation — E2 forward R² ≈ 0.99 at onset_2 —
> so no immature anchor arm existed. INV-064 was therefore **never testable** here → `non_contributory`,
> `measurement_degeneracy`; no weighting. Re-queued as corrected successor **V3-EXQ-740a** (task-relevant
> decodability observable + immature anchor + mature-anchor harm-decodability positive control; keeps the
> PC_iv_moved-style guard). INV-064 stays **candidate / pending_substrate_reconfirmation**. First INV-064
> degenerate autopsy — re-derive brake not fired; a second would implicate the operationalisation (route
> to test-bed/measurement redesign, not a third letter).

## 9. Routing decision (confirmed)

- **Root cause:** measurement + window (user-accepted).
- **Route:** single corrected **V3-EXQ-740a** via `/queue-experiment` (user-selected).
- **evidence_direction:** `non_contributory`; **epistemic_category:** `measurement_degeneracy`.
- **INV-064:** stays candidate / pending_substrate_reconfirmation — **PROMOTES / DEMOTES NOTHING**.
- Analysis + handoff only. This skill writes no edits to claims.yaml, the manifest, review_tracker, or
  substrate_queue — `/governance` applies the note and marks the run reviewed; `/queue-experiment` builds
  740a.
