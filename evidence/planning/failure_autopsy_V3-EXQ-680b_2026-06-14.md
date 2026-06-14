# Failure Autopsy -- V3-EXQ-680b (MECH-423 cross-model super-additivity, hardened margin)

- **Generated (UTC):** 2026-06-14T22:27:22Z
- **Scope:** single
- **Target run:** `v3_exq_680b_mech423_superadditivity_ablation_20260614T201913Z_v3`
- **Queue id:** V3-EXQ-680b | **purpose:** evidence | **claim_ids:** [MECH-423]
- **Outcome adjudicated:** FAIL / `interpretation.label = additive_below_margin` / `evidence_direction = inconclusive`
- **Failed criterion:** discrimination (`superadditivity_margin_pair`: 0/3 seeds clear margin)
- **Status:** confirmed (user-accepted 2026-06-14)
- **Routing:** `/queue-experiment` -> V3-EXQ-680c (implementation + measurement fix; same scientific question)
- **Supersession lineage:** 680 (encoder-not-in-optimizer bugfix) -> 680a (false PASS, level-scaled margin) -> **680b** (hardened delta-scaled + floored margin; correctly flips 680a's false PASS to inconclusive on identical data).

## 1. Facts (no interpretation)

`integration_score = world_R2 + affordance_R2` (held-out), per arm per seed. R1/R2/R3
readiness all met (`all_preconditions_met = true`); `non_degenerate = true`.

| seed | ISOLATED | PAIR | delta_pair | PAIR world_R2 / afford_R2 | PAIR R1 min_grad_norm |
|---|---|---|---|---|---|
| 42  | 0.207 | 1.774  | **+1.567** | 0.874 / 0.900 | 5.27 |
| 123 | 0.262 | 1.498  | **+1.236** | 0.711 / 0.787 | 3.12 |
| 456 | 0.137 | **-1.050** | **-1.187** | **-1.428** / 0.378 | **46.30** |

- mean delta_pair **+0.5386 > 0**; across-seed delta SD **1.2275**.
- margin = `max(2.0 * pstdev(delta_pair), 0.02)` = **2.455**; `n_seeds_pass = 0`; `super_additive = false`.
- Verdict branch hit: `mean_delta_pair > 0` AND `n_seeds_pass < MIN_SEEDS_PASS` -> `additive_below_margin / inconclusive` (NOT the `mean <= 0` weakens branch).
- Exploratory TRIPLE (proxy object head, NOT ARC-080; tags nothing): seed 123 diverged to world_R2 **-149.05**, grad norm **2.0e11**, R2 `converged = false` (`final_rel_delta 0.907`, 10 iters). Seed 456 TRIPLE world_R2 -1.168.
- Identical delta_pair to 680a (same data); the ONLY change is the hardened margin. 680b
  cleanly confirms the hardened gate flips 680a's false PASS to a correct inconclusive.

## 2. Claim-layer mapping

MECH-423 (`mechanism_hypothesis`, status candidate, implementation_phase v3, epistemic_category
standard): "cross-model integration is SUPER-ADDITIVE -- integrated E1 world-model + E2
affordance-model over a shared latent beats a param/compute-matched bag of isolated modules."
`depends_on`: ARC-004/001/002, MECH-081/033, ARC-080. `what_would_answer` = exactly this 3-arm
ablation with the R1/R2/R3 readiness precondition.

**Did the test let the claim express itself?** Yes -- on the 2 numerically stable seeds the
integrated arm beat the isolated baseline by **+1.57 / +1.24** combined-R2 units (a large,
clean super-additive delta). The claim is **intact**: the inconclusive verdict reflects an
underpowered/contaminated margin (one divergent seed), not an absence of the asserted effect.
`claim_ids = [MECH-423]` is accurate (not inherited stale; this is the registered EXP-0380
load-bearing arm). MECH-423 stays candidate, exp_conf 0; **not weakened.**

## 3. Biological-reference triage

- **Closest mechanism:** multisensory integration / inverse effectiveness -- cortical and
  superior-colliculus multisensory neurons whose bimodal response *exceeds the sum* of the
  unimodal responses; shared-representation MTL (Caruana 1997). This is a genuine existence
  proof for the **class** of super-additivity.
- **is_formal_import:** partial. The mechanism is grounded in both biology (multisensory
  enhancement) and an ML prior (shared-rep MTL); it is not a pure formal-definition import of
  the SD-003 kind. Biology lit-pull already commissioned and present:
  `targeted_review_mech_423_integration_prerequisites` (2026-06-12). **No new `/lit-pull`
  arises.**
- **Does the failure match a missing-dependency signature?** No. It matches a numerical-
  instability signature (one seed's world head diverged), not the biological "missing
  dependency" pattern. The biology supports the mechanism; the substrate exhibits it on stable
  seeds.

## 4. The -1.19 (seed 456) adjudication -- instability artifact, NOT weakens

Three independent reasons the -1.187 seed is a training-instability artifact rather than a
negative-transfer *weakens* signal:

1. **Dissociated head behaviour.** On seed 456 the **world head collapsed** (world_R2 -1.428)
   while the **affordance head IMPROVED** (0.123 -> 0.378). Structured gradient-conflict
   negative transfer would degrade *both* coupled streams; one stream diverging while the
   other improves is the signature of a single unstable optimisation run, not bidirectional
   conflict.
2. **Numerical-divergence fingerprint + unbounded-below metric.** Seed 456's R1 gradient norm
   (46.3) is ~10-15x the stable seeds (3.1-5.3); `world_R2` is unbounded below, so a single
   divergent seed produces a large negative number that **dominates `delta_SD`** and inflates
   the margin (2.455) out of reach. The exploratory TRIPLE arm removes all doubt that the
   co-training is numerically unstable on a subset of seeds: seed 123 reached grad norm
   **2.0e11** -> world_R2 **-149**, with the inference loop failing to converge.
3. **The design's own weakens gate was not entered.** The script routes `weakens` only when
   `mean delta_pair <= 0` (a whole-distribution call); the mean is **+0.539 > 0**, so by its
   pre-registration this is NOT the weakens regime. It is `additive_below_margin / inconclusive`.

### Load-bearing measurement defect discovered (drives the 680c redesign)

The manifest reports `mean_pairwise_cosine = 0.0` for **all** pair arms / all seeds. This is a
**structural artifact, not a measurement**: in 680b the R1 probe wires
`world: world_head(z[:, :self_dim])` and `self: self_head(z[:, self_dim:])` -- the two heads
read **disjoint halves** of the probe latent, so their gradients w.r.t. `z_shared` have
non-overlapping support and the pairwise cosine is mathematically pinned at exactly 0.0 every
seed (cf. 679's readiness diagnostic, which measured cosine 0.12-0.26 on a differently-wired
probe). Consequence: the R1 **"net-negative cosine = negative-transfer" guard is inert** in
680b -- it physically cannot fire. We therefore rule out negative transfer on the evidence in
(1)-(3) above, NOT on the cosine check. (R1's *other* sub-check, `min_grad_norm > floor`, is
genuinely met at 3-46, so coupling is real and the readiness gate is not wholly vacuous; only
its cosine sub-check is inert.)

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **intact** | 2/3 seeds express strong super-additivity (+1.57/+1.24); inconclusive = underpowered margin, not absent effect. MECH-423 not weakened. |
| Biological reference | **clear** | multisensory super-additivity / inverse effectiveness; lit-pull present (2026-06-12). |
| Prerequisites | **present** (caveat) | R1 min_grad / R2 / R3 met; readiness gate cleared. Caveat: R1 cosine sub-check structurally inert (disjoint-slice probe). |
| Implementation | **partial** | world-head co-training diverges on a subset of seeds (grad 46 -> -1.4 R2 in pair; grad 2e11 -> -149 in triple); no grad clipping / unbounded score. |
| Environment | adequate | grid 6 / 4 hazards / 3 resources. |
| Measurement | **under-instrumented / misleading** | `world_R2` unbounded below lets one divergent seed dominate `delta_SD` -> margin un-passable; cosine negative-transfer guard inert. |
| Integration | **coupled but unstable** | interleaved consolidation touches both heads (R3 clean), but co-training is numerically unstable on some seeds. |
| Scale | **likely insufficient** | n=3 with 1 unstable seed is underpowered for a 2-of-3 margin test. |

`recommended_epistemic_category`: **standard** (NOT substrate_ceiling -- the substrate produces
+1.5 super-additive deltas when training is stable; the defect is the experiment's training
regime + metric, not ree_core).

## 6. Learning extracted

1. **The -1.19 seed is a numerical-instability artifact**, not a negative-transfer weakens:
   world head diverged while affordance head improved; grad-norm spike; mean delta positive;
   the weakens gate (mean <= 0) was not entered.
2. **`world_R2` unbounded-below + no grad clipping is a margin-poisoning measurement defect**:
   a single divergent seed dominates the across-seed delta SD and renders the hardened margin
   un-passable even when 2/3 seeds are strongly super-additive.
3. **The R1 cosine negative-transfer guard is inert as wired** (disjoint-slice probe -> cosine
   identically 0.0). Genuine negative transfer could not be detected by this run; the guard
   must probe gradient alignment on the *shared encoder parameters* (overlapping support) to be
   able to fire.
4. **The hardened margin works as intended**: it correctly flips 680a's false PASS to a correct
   inconclusive on identical data, and is strictly tighter (margin can only rise) so it cannot
   manufacture a false PASS. (Confirms the effect-size PASS-gate memory: SD-of-delta + absolute
   floor.)
5. n=3 is underpowered for a 2-of-3 reliability margin once instability is in play.

## 7. Repair pathway (user-confirmed)

**Routing: `/queue-experiment` -> V3-EXQ-680c** (same scientific question; alphabetic suffix =
implementation/measurement fix, not a new hypothesis). Redesign spec:

- **(a) Numerical stability of the co-training:** add gradient clipping on the world/affordance
  heads (and the proxy head in the exploratory triple) and/or lower the head LR, so a seed does
  not diverge to world_R2 << 0. Verify no arm/seed produces `R2 converged = false`.
- **(b) Bound the score against single-seed domination:** clamp/winsorize the per-seed
  `integration_score` at a sensible floor (e.g. clip world_R2 / affordance_R2 at a lower bound,
  or winsorise the delta distribution) so one divergent seed cannot dominate `delta_SD` and
  inflate the margin. Keep the hardened `max(2*SD(delta), FLOOR)` margin basis.
- **(c) Make the negative-transfer guard real:** re-wire the R1 cosine probe to measure
  per-module gradient alignment on the **shared encoder parameters** (where both heads'
  gradients genuinely overlap), not on disjoint latent slices, so `cosine < 0` can actually
  fire and route `substrate_not_ready` in a true negative-transfer regime.
- **(d) Power:** n >= 5 seeds.

This redesign goes through `/queue-experiment` (code review + smoke test) -- it touches scoring
logic and the readiness probe wiring, which is exactly the copy-and-modify risk that skill
guards. NOT `/implement-substrate` (no ree_core gap), NOT `/lit-pull` (biology lit present),
NOT a demotion (claim intact).

## 8. Governance hand-off (recommended writes -- governance applies, this skill does not)

- `evidence_direction`: **inconclusive** (confirm the self-route; keep as-is).
- Recommended `evidence_quality_note` text (governance to write on the 680b manifest /
  MECH-423 evidence ledger):
  > "V3-EXQ-680b additive_below_margin (mean delta_pair +0.539 > 0, 0/3 seeds clear hardened
  > margin 2.455). Autopsy 2026-06-14: the single -1.19 seed (456) is a numerical-instability
  > artifact (world head diverged to R2 -1.43 with grad norm 46x stable seeds; affordance head
  > IMPROVED on the same seed; exploratory triple seed 123 grad 2e11 -> R2 -149) NOT a
  > negative-transfer weakens -- the weakens gate (mean delta <= 0) was not entered and the R1
  > cosine negative-transfer guard is structurally inert (disjoint-slice probe). MECH-423 NOT
  > weakened; 2/3 seeds show clean super-additivity (+1.57/+1.24). Margin poisoned by
  > unbounded-below world_R2. pending_retest_after V3-EXQ-680c (grad-clip + bounded score +
  > real cosine probe + n>=5)."
- `recommended_epistemic_category`: standard.
- `recommended_substrate_queue_entry.action`: **none** (no substrate gap).
- `pending_retest_after_substrate`: false (retest is via experiment redesign 680c, not
  substrate).
- `narrow_supports_flag`: false (this is an inconclusive, not a substrate-limitation
  reclassification of a supports; no illusory-conflict-resolution risk).

## 9. Recurrence note (granularity-debt check)

Prior planning autopsy on this target: `failure_autopsy_V3-EXQ-679_2026-06-14` -- but that was a
**clean diagnostic gate-clear** (`claim_ids = []`, tags/weighs nothing), not a claim-weighing
FAIL. 680b is the **first** evidence-FAIL circling MECH-423. This is therefore **not** a
granularity-debt recurrence (no pattern of distinct FAIL signatures across separate autopsies).
Re-evaluate only if 680c also returns inconclusive/mixed -- that would be the first genuine
recurrence and the point to consider `/claim-synthesis`.
