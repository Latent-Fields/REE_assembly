# Failure autopsy: V3-EXQ-956 (ContextMemory gumbel_learned write-address validation) — 2026-08-29

**Run:** `v3_exq_956_contextmemory_write_gumbel_learned_validation_20260829T014524Z_v3` · FAIL · diagnostic · claim_ids [] · seeds [42,7,13,100,200] · ree-cloud-2 · self-route `gumbel_learned_occupancy_only_content_discrimination_not_confirmed`
**Status:** confirmed (interactive gate 2026-08-29; session autopsy-batch-20260829)
**Dry-run check:** clean.

## Facts

First run ever with `contextmemory_write_addressing_loss_weight > 0` under real training (w=0.5, 100 ep × 150 steps = 15,000 steps, the 907-proven schedule) — the validation the corrupting substrate entry's THIRD-mechanism note said was owed. The driver's `_e1_tick` wiring fix is load-bearing: without it `compute_prediction_loss()` returned exactly 0.0 every step and the tagger stayed byte-frozen (verified empirically pre-landing). Mechanical controls clean 5/5 both ways (untrained tagger byte-frozen; trained moved 1.14–1.37). P0 writepath met (min 1432 writes vs 200). C1 occupancy 5/5 both gumbel arms (16/16 slots — Gumbel-noise-driven, training-independent, as pre-registered). LEGACY reproduced the known 3-seed single-slot lock (7/13/100 — the 436e/436f/943 operating point).

**The single load-bearing failure is the discrimination criterion C2**: mean eval-mode 2-cluster probe Jaccard trained **0.667** vs required ≤ untrained 0.400 − 0.25 = **0.15**. Headroom gate met (0.400 ≥ 0.25), precondition_unmet=false, non-degenerate. Training also concentrated training-time writes (entropy 3.97 → 2.67–3.24; self-repeat 0.06 → 0.35–0.51; arm-matched anneal — identical per-seed write counts, and the untrained arm's 3.97 shows annealing alone does not concentrate).

**Strength calibration (red-team, adopted):** the required −0.25 move is *clearly absent* (no trained seed at Jaccard 0; min trained 1/3) — that half is noise-proof. The *wrong-direction* +0.267 point estimate is **suggestive, not established** (exact paired sign-flip / permutation p ≈ 0.24–0.28 on 5 bimodal per-seed Jaccards; the corroborating 40-episode pre-check, 0.4→0.9, is non-independent). Cheap confirmer if it ever matters: +10 seeds × 2 gumbel arms ≈ 26 min cloud, and/or probe_clusters > 2.

## Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | n/a | deliberately claim-free (SD-017/ARC-045/MECH-166 unblocked only on validation) |
| Biological reference | partial | pattern separation (DG-CA3) is content-driven; a diversity penalty on the addressing policy is a formal import |
| Prerequisites | present | gradient path genuinely wired for the first time |
| Implementation | complete | substrate clean at 3e193452; controls prove the wiring |
| Environment | adequate | real-agent latents, context switching, contract-test probe instrument |
| Measurement | adequate | one caveat: C2 is a 5-seed mean of a bimodal quantity (coarse) — but the required move is clearly absent regardless |
| Integration | coupled | training-time occupancy + eval probe + loss on the same live ContextMemory |
| Scale | adequate at the tested operating point | w=0.5 is the only value ever measured for this loss |

**Failure-location (GOV-FAILLOC-1): MECHANISM FAILED** — implementation complete, measurement adequate, environment adequate; the tested mechanism (pairwise-diversity write-addressing loss producing content-conditioned selection) failed to produce content discrimination. Second loss *design* to fail (first: MoE importance loss, content-blind Jaccard 1.000, replaced pre-landing). Not chargeable to REE as a whole.

## Disposition (user-confirmed)

- Self-route label **accurate**; direction non_contributory (claim-free, scoring-excluded); category `standard`.
- **Substrate entry amend** (`contextmemory-write-path-addressing-degeneracy`, severity corrupting): append the 956 failure record (resolved: open); entry **stays `implemented_pending_validation`** — consistent with the 2026-08-26 human decision. None of BIAS / REFRACTORY / gumbel_learned@w=0.5 has demonstrated content-conditioned write selection.
- **Fan-out portfolio (GOV-FANOUT-1 shape), registered as a NEW hypothesis-space question** (`contextmemory_write_content_discrimination`; no existing qid covers the write-path question):
  - **H1 loss-objective-mismatch** (axis: algorithm) — diversity loss references no content; a content-referencing (contrastive) objective required. Direct precedent: V3-EXQ-907's read-path result at the same schedule. Probe on both real-agent latents and the synthetic stream (avoids conflation with H4).
  - **H2 operating-point** (axis: process) — not eliminated by this run; first leg = the cheap 10-seed sweep (also settles the wrong-direction question), then weights {0.1, 2.0, 8.0}.
  - **H3 task-pressure-required** (axis: drive) — couple the SD-016 read-path loss through write selection.
  - **H4 input-distribution** (axis: representation, red-team addition) — train-time z_world under-differentiation (SD-008 ~0.98-cosine cone) may leave no usable content structure; un-instrumented in this manifest.
- Probes routed via `/queue-experiment` after governance ratifies; **nothing spawned by this session** (2026-07-30 rule).

**Re-derive brake: does not fire** (no claims tagged; no ceiling reads). **Granularity trigger: n/a** (claim-free).

**7b:** 0 fires (claim-keyed checks structurally inapplicable — claim-free target). **7c:** CONFIRMED core + routing; wrong-direction sub-claim CONTESTED and adopted (recalibrated); H4 added per red-team; hygiene noted (driver docstring 100-vs-200-episode inconsistency; pre-check per-seed list vs stated mean).

## Learning extracted

1. "The tagger trains" ≠ "the tagger learns the right thing": substantial parameter movement + write concentration with no discrimination gain — a diversity-shaped auxiliary loss does not purchase content conditioning.
2. The `_e1_tick` wiring find generalises: any driver in this family that never calls `act()`/`act_with_split_obs()` silently trains **nothing** through `compute_prediction_loss()`; the byte-frozen/moved control pair should be standard for auxiliary-loss validations.
3. Two independent loss designs have now failed — recurrence points first at the objective family (H1), though H2/H4 are not eliminated.
