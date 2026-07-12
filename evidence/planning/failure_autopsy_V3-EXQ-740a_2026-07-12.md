# Failure Autopsy — V3-EXQ-740a (INV-064 maturational-sequence necessity, 2nd degeneracy)

- **Generated (UTC):** 2026-07-12T10:53:14Z
- **Scope:** single
- **Status:** confirmed (interactive gate answered)
- **Run:** `v3_exq_740a_inv064_maturational_sequence_e3_bounded_20260711T233512Z_v3`
- **Queue id:** V3-EXQ-740a · **supersedes** V3-EXQ-740 · **Claim:** INV-064 (`development.maturational_sequence`)
- **Outcome:** FAIL · `evidence_direction=unknown` (self-report) · `non_degenerate=false`
- **Machine:** ree-cloud-2 · seeds [42, 7, 19] · onset_episodes [0, 1, 4, 12, 30]
- **Predecessor autopsy:** `failure_autopsy_V3-EXQ-740_2026-07-11` (non_contributory / measurement_degeneracy, IV ran backwards)

## 1. Claim under test

INV-064 (`e1_e2_e3_maturational_sequence_necessity`, invariant / emergent from ARC-001/002/003/019;
status **candidate**, `pending_substrate_reconfirmation: true`): E3's harm/goal evaluator quality is
**strictly bounded** by E1/E2 representational differentiation — poorly-differentiated inputs yield a
noise-fitted E3 evaluator, so productive E3 training cannot begin until E1/E2 have reached sufficient
schema differentiation. Grounded in PFC-last-myelination developmental biology (strong, non-formal
existence proof — unchanged from the 740 triage). The canonical claim text names E3's primary inputs
explicitly: **"z_world from E1 and action_objects from E2."**

## 2. Facts reconstruction (no interpretation)

740a is the corrected successor to 740, carrying the four autopsy-mandated fixes. Design is unchanged
in shape (commitment-free, frozen-representation curriculum-order contrast; per (seed, onset): mature
E1+E2+encoder for `onset` episodes, freeze, collect a **shared** fixed-trajectory harm dataset, re-init
`e3.harm_eval_head` to a bit-identical init, train only that head for a fixed budget, read out held-out
harm R²). The fixes:

- **FIX 1 (IV):** replace the eff_rank that ran backwards with `world_feat_decode_r2` = held-out ridge R²
  of z_world[t] → harm_obs[t+1] (predictive, JL-safe, expected to **increase** with maturation).
- **FIX 2 (window):** onset now `{0, 1, 4, 12, 30}` — onset_0 is a fresh (untrained) encoder, a genuine
  immature anchor (740's `{2,5,11,22}` was entirely post-saturation).
- **FIX 3 (positive control):** `harm_decode_r2` = held-out ridge R² of z_world[t] → harm_target[t],
  gated at onset_max (`PC_harm_decodable ≥ 0.05`) — verify harm is decodable-in-principle before reading
  the gradient.
- **FIX 4 (guard):** `PC_iv_moved` now checks the corrected observable moved in the **predicted
  direction** (mean predictive-decode delta ≥ 0.03 AND > 0).

**Observed — the IV fix worked; the positive control failed:**

| onset | world_feat_decode_r2 (IV) | harm_decode_r2 (pos. ctrl) | mean E2 fwd R² | mean held-out harm R² (DV) |
|---|---|---|---|---|
| 0 (fresh) | 0.048 | 0.006 | 0.041 | −1.582 |
| 1 | 0.119 | 0.007 | 0.950 | −0.201 |
| 4 | 0.176 | 0.013 | 0.980 | −0.219 |
| 12 | 0.212 | 0.027 | 0.992 | −0.251 |
| 30 (mature) | **0.245** | **0.034** | 0.974 | −0.761 |

- **`PC_iv_moved` = true** — mean predictive-decode delta 0.197 ≫ 0.03; rises monotonically across all
  five arms. Task-relevant differentiation genuinely **increased** with maturation. Both of 740's flaws
  (backwards IV, saturated window) are gone: onset_0 is a real immature anchor (eff_rank 6.4–8.3, E2 fwd
  ≈ 0), and the IV moves in the predicted direction.
- **`PC_harm_decodable` = false** — mean mature-anchor `harm_decode_r2` **0.034 < 0.05**. Realized scalar
  harm is **not linearly decodable from z_world even at maturity**. It rises slightly (0.006 → 0.034) but
  never clears the floor.
- **`PC_events` = true** (min harm_event_frac 0.878 ≫ 0.03) — harm was plentiful; not the problem.
- The DV (held-out harm R²) is **negative in all arms**, consistent with a target the input stream does
  not carry.

**Failed criterion:** the **validity precondition** `PC_harm_decodable` (a positive control, not a
discrimination criterion). The run self-routed `non_degenerate=false` / `evidence_direction=unknown`
correctly — the guard did its job.

## 3. Claim-layer mapping

`claim_ids=[INV-064]` is **accurate** (not an inherited-tag artifact). But the probe splits into two legs
that fared oppositely:

- **IV leg (E1/E2 differentiation):** now validly exercised — differentiation rises. This is **first-time
  positive evidence for the IV half** of INV-064 on the V3 substrate.
- **DV / harm leg (E3 harm-eval quality bounded by that differentiation):** **never validly exercised** —
  the E3 harm_eval head reads z_world, and its target is undecodable from z_world, so the trained MLP was
  fitting a target that is not a function of its input. A null/negative DV gradient here carries no
  information about the *bound* INV-064 asserts.

## 4. Biological-reference triage

- **Closest reference mechanism** (unchanged from 740): cortical maturation order (PFC last to myelinate).
  Strong, **non-formal-import** class existence proof. Biology-divergence-is-load-bearing does not apply;
  primary output is **not** a `/lit-pull` commission.
- **Missing-dependency signature? Partially — but it is a claim/probe issue, not a biological gap.** The
  substrate has a dedicated nociceptive stream (SD-010): `harm_eval_z_harm(z_harm)` where
  `z_harm = HarmEncoder(harm_obs)` is instantiated **outside** the z_world encoder and is exempt from
  reafference correction — introduced precisely because fusing hazard into z_world caused the EXQ-027b
  over-correction paradox (ReafferencePredictor subtracting hazard when it was fused into z_world). So in
  the V3 architecture, **harm is deliberately routed through z_harm, not z_world.** Decoding realized harm
  from z_world (as both the 740a positive control and its `harm_eval_head` do) reads the stream the
  architecture specifically does not use for harm.

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **split** | IV/world leg now expresses (differentiation rises); harm leg never validly exercised — its DV target is undecodable from the probed stream |
| Biological reference | **clear** | PFC-last-myelination; strong class existence proof; not a formal import (unchanged from 740) |
| Dependency / prerequisites | present | warmup curriculum runs; **immature anchor is now genuinely immature** (onset_0 eff_rank 6.4–8.3, E2 fwd ≈ 0) — FIX 2 worked |
| Implementation completeness | **partial / mis-targeted** | probe + 740a `harm_eval_head` read **z_world**; SD-010 routes harm through a **dedicated z_harm stream** (`harm_eval_z_harm`). Harm-from-z_world decodes the wrong stream |
| Environment adequacy | adequate | dense predictable harm (event_frac 0.88); not the binding issue |
| **Measurement adequacy** | **misleading (dominant)** | positive control decodes **realized scalar harm** = f(world-state, **body/z_self**, **random action**) from **z_world alone** — structurally under-determined (body + random-action variance are noise w.r.t. z_world) AND wrong-stream (SD-010). Contrast: harm-**world-features** (harm_obs) decode fine from the same z_world (0.245) and **rise** with maturation |
| Integration adequacy | n/a | single-module frozen-representation probe |
| **Scale / window** | **adequate now** | onset 0..30 spans immature→mature — FIX 2 resolved 740's post-saturation window |

**Recommended `epistemic_category`: `measurement_degeneracy`** (specifically: wrong-stream + under-
determined-target operationalisation of the harm DV). The IV half is now valid; the harm DV was
structurally un-exercisable, so the run carries **no interpretable signal on INV-064's bound**, but does
carry a clear *methodological* signal about which stream and target form the harm leg must use.

## 6. Adjudication — is harm-undecodable a substrate signal, or a mis-posed observable?

**Mis-posed observable, confounded — NOT a clean substrate signal.** The contrast is dispositive: same
frozen z_world, same ridge machinery — harm-relevant **world features** decode at 0.245 and rise, while
realized **scalar harm** decodes at 0.034 flat. z_world is not harm-blind; the target *form and stream*
were mis-chosen. Two independent probe-side confounds, neither a substrate ceiling:

1. **Wrong stream (SD-010):** harm lives in z_harm by architectural design, not z_world.
2. **Under-determined target:** realized post-random-action scalar harm depends on body/z_self + the
   random action, neither in z_world.

So INV-064's maturational-necessity claim **is** testable with a decodable task-relevant observable. But
the run surfaced a genuine, load-bearing **claim↔substrate mismatch**: the canonical claim names z_world
as E3's harm input, while SD-010 routes harm through a dedicated z_harm stream with its own evaluator.
That mismatch — not "harm is absent from the substrate" — is the real finding.

## 7. Recurrence, re-derive brake, and repair pathway

**Work-graph classification:** `complex (probe-gated) / mystery (known data)` — we already have the data;
the frame (decode-realized-scalar-harm-from-z_world-alone) is wrong. Do **not** gather more of the same
observable.

**Re-derive brake — FIRED (2nd non_contributory INV-064 degeneracy, threshold 2).** Prior:
`failure_autopsy_V3-EXQ-740_2026-07-11` (non_contributory). This autopsy is the 2nd. Per MOVE-3 the brake
fires; its **refusal half is load-bearing and correct**: *no same-observable 740b* (re-decoding scalar
harm from z_world is exactly the loop the brake exists to stop). **Deviation from the brake's default
route:** the default `implement-substrate` **does not apply** — there is no substrate build owed. The IV's
rising `world_feat_decode_r2` (0.245) proves z_world carries the information, and the z_harm stream +
`harm_eval_z_harm` already exist. The 740 autopsy pre-registered this exact contingency: *"a SECOND
non_contributory / degenerate INV-064 result would implicate the OPERATIONALISATION itself → route to a
test-bed / measurement redesign, NOT a third lettered iteration."*

**Granularity-debt recurrence trigger — FIRES.** This is the 2nd `failure_autopsy_*` on INV-064, with a
**different failure signature each time** (740: IV backwards; 740a: DV undecodable). Combined with the
z_world-vs-z_harm mismatch, the recurrence is the granularity-debt signal: INV-064 may conflate two
distinct claims —

- a **world/goal-evaluator** maturational bound on **z_world** differentiation (the leg the IV now
  validly exercises), and
- a **harm-evaluator** maturational bound on **z_harm** differentiation (a different maturation
  trajectory: `HarmEncoder`, not the z_world encoder).

**Route (user-selected at the interactive gate): `/claim-synthesis` FIRST.** Resolve the claim scope —
which stream the harm-leg bound is even about — proposal-first and lit-grounded, **before** any further
experiment. The decomposition then determines the correct re-posed observable (z_harm-decodability with a
z_harm maturation trajectory, and/or the already-working world-feature-decodability for the world/goal
leg). This is the mystery(known-data) response: reframe, do not re-run the same observable.

- **No substrate build** (`recommended_substrate_queue_entry.action = none`) — the substrate carries the
  information and the z_harm evaluator already exists.
- **No demotion, no `/lit-pull`** — biology is a strong existence proof, not a formal import; and the harm
  leg was never validly tested, so there is no fair-test failure to demote on.
- **No same-observable re-queue** — the brake refuses a 740b decoding scalar harm from z_world.

## 8. Learning extracted

1. **The 740 IV fix worked.** `world_feat_decode_r2` (predictive z_world → next-step harm world-features)
   rises monotonically 0.048 → 0.245 across onset {0,1,4,12,30}; `PC_iv_moved` passes with a genuine
   immature anchor. This is the **first valid demonstration that E1/E2 task-relevant differentiation
   increases with maturation** on the V3 substrate — the IV half of INV-064.
2. **The harm leg reads the wrong stream.** Both the 740a positive control and the substrate's
   `harm_eval(z_world)` decode harm from z_world; SD-010 deliberately routes harm through a dedicated
   `z_harm = HarmEncoder(harm_obs)` stream (`harm_eval_z_harm`), exempt from reafference correction. Any
   INV-064 harm-leg test must exercise the stream E3 actually uses for harm.
3. **Realized post-random-action scalar harm is a structurally under-determined DV for a z_world probe.**
   harm_target = f(world-state, body/z_self, action); z_world carries only the world-state part. The
   decodable, rising `world_feat_decode_r2` (harm world-features) is the existence proof that the *form*,
   not the substrate, was the problem.
4. **Recurrence with differing signatures is the granularity signal.** 740 (IV backwards) and 740a (DV
   undecodable) are two different measurement failures circling one claim — the tell that INV-064 is
   probably two claims (world/goal-eval bound on z_world vs harm-eval bound on z_harm), which is why the
   route is `/claim-synthesis` before a third experiment.
5. **The positive-control guard worked.** 740a self-routed `non_degenerate=false` on the failed positive
   control rather than emitting a spurious `weakens` on a confounded DV. No guard defect — the FIX-3
   control the 740 redesign added is exactly what caught this.

## 9. Draft `evidence_quality_note` (governance writes this; not written here)

> 2026-07-12 (V3-EXQ-740a, corrected successor to V3-EXQ-740; consumed from
> failure_autopsy_V3-EXQ-740a_2026-07-12, confirmed): 2nd INV-064 degeneracy. The 740 IV fix SUCCEEDED —
> the corrected task-relevant differentiation observable (world_feat_decode_r2, predictive z_world →
> harm_obs[t+1]) rises monotonically 0.048 → 0.245 across onset {0,1,4,12,30} with a genuine immature
> anchor; PC_iv_moved passes (mean delta 0.197). This is the first valid demonstration that E1/E2
> task-relevant differentiation increases with maturation. But the run FAILed DEGENERATE on the NEW
> mature-anchor harm-decodability positive control (PC_harm_decodable): mean linear harm decode R2 0.034 <
> 0.05 — realized scalar harm is not decodable from z_world even at maturity. Root cause is measurement,
> NOT claim pressure and NOT a substrate ceiling: (a) SD-010 deliberately routes harm through a dedicated
> z_harm = HarmEncoder(harm_obs) stream (harm_eval_z_harm), outside the z_world encoder — the probe (and
> the 740a harm_eval_head) read z_world, the wrong stream; (b) realized post-random-action scalar harm =
> f(world-state, body/z_self, action), structurally under-determined from z_world alone. The contrast is
> dispositive: harm WORLD-FEATURES decode fine from the same z_world (0.245, rising) while realized scalar
> harm does not (0.034, flat). evidence_direction non_contributory / epistemic_category
> measurement_degeneracy; NOT weighted. Re-derive brake FIRED (2nd non_contributory INV-064 autopsy) —
> REFUSE a same-observable 740b; NO implement-substrate (substrate carries the info; z_harm evaluator
> exists). Route: /claim-synthesis FIRST — the different-signature recurrence (740 IV-backwards; 740a
> DV-undecodable) plus the z_world-vs-z_harm mismatch is granularity debt: INV-064 likely conflates a
> world/goal-evaluator maturational bound on z_world (IV now validly demonstrated) with a harm-evaluator
> maturational bound on z_harm. Resolve claim scope proposal-first before any re-posed experiment. INV-064
> stays candidate / pending_substrate_reconfirmation; PROMOTES/DEMOTES NOTHING.

## 10. Routing decision (confirmed at interactive gate)

- **Root cause:** measurement (wrong-stream + under-determined harm DV target); the IV/differentiation leg
  is now valid.
- **Adjudication:** harm-undecodable-from-z_world is a **mis-posed observable, confounded** — NOT a clean
  substrate signal (world-feature decodability rises to 0.245 from the same z_world). The load-bearing
  finding is the claim↔substrate mismatch (claim names z_world; SD-010 routes harm via z_harm).
- **Route (user-selected):** `/claim-synthesis` FIRST — decompose/resolve the z_world-vs-z_harm scope of
  INV-064's maturational bound before any further experiment. Re-derive brake FIRED (refuse same-observable
  740b); `implement-substrate` deviation justified (no build owed).
- **evidence_direction:** `non_contributory`; **epistemic_category:** `measurement_degeneracy`.
- **INV-064:** stays candidate / pending_substrate_reconfirmation — **PROMOTES / DEMOTES NOTHING**.
- Analysis + handoff only. This skill writes no edits to claims.yaml, the manifest, review_tracker, or
  substrate_queue — `/governance` applies the note and marks the run reviewed; `/claim-synthesis` owns the
  decomposition.
