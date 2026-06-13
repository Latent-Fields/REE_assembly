# Failure Autopsy — V3-EXQ-669a (MECH-329 wanting-before-liking goal seeding)

- **Generated (UTC):** 2026-06-13T09:48:09Z
- **Scope:** single
- **Status:** confirmed
- **Run:** `v3_exq_669a_mech329_wanting_first_goal_seeding_20260613T074454Z_v3`
- **Queue id:** V3-EXQ-669a (supersedes the ERROR run `v3_exq_669_...`, an `env.to()` numpy-env crash fixed by a `/diagnose-errors` session)
- **Outcome:** FAIL · self-classified `evidence_direction: challenges` / `evidence_class: negative_evidence` (non-standard → routed to autopsy, not an inline stamp)
- **Claims tagged:** MECH-329 (mechanism_hypothesis, candidate, conf 0.0), MECH-189 (mechanism_hypothesis, candidate, conf 0.0)
- **Machine:** ree-cloud-2

---

## 1. Facts — reconstruction (no interpretation)

The script (`ree-v3/experiments/v3_exq_669a_mech329_wanting_first_goal_seeding.py`) runs a 4-phase
`InfantCurriculumScheduler` (Phase 0–3) for three matched-seed conditions, with the MECH-189
`SuperOrdinalGoalMemory` substrate enabled (`use_super_ordinal_goal_anchors=True`,
`super_ordinal_salience_threshold=0.3`, `super_ordinal_complexity_threshold=0.2`), writes frozen
at the Phase-2 child→adult transition:

- **A wanting_first** — z_goal enabled Phase 0–1, benefit_eval delayed to Phase 2
- **B liking_first** — benefit_eval enabled Phase 0–1, z_goal delayed to Phase 2
- **C both_delayed** — neither enabled until Phase 2 (the **positive / substrate-sanity control**)

Per-condition results (verbatim from the manifest `results` block):

| condition | total_steps | benefit_contacts | harm_events | anchor_count | total_writes | total_seeds | p01_writes | p01_mean_complexity |
|---|---|---|---|---|---|---|---|---|
| wanting_first | 54277 | **1244** | **4953** | **0** | **0** | 0 | **0** | 0.000 |
| liking_first  | 54277 | **1244** | **4953** | **0** | **0** | 0 | **0** | 0.000 |
| both_delayed  | 54277 | **1244** | **4953** | **0** | **0** | 0 | **0** | 0.000 |

Criteria: `c1_wanting_more_anchors=false`, `c2_wanting_more_writes=false`,
`c3_wanting_higher_complexity=false`, **`c4_delayed_sanity=false`** (the positive control yielded 0 anchors).

**Two load-bearing facts:**

1. **Every discriminative metric is pinned at 0 in every arm — including the positive/sanity control.**
   anchor_count = total_writes = p01_writes = 0, p01_mean_complexity = 0.000, across all three conditions.
   `total_writes=0` means the MECH-189 salience write gate **never fired once** in 3 × 54277 steps. The
   harness (`experiments/_harness.StepHarness`) *does* make the canonical
   `agent.update_z_goal(benefit_exposure=…, drive_level=…)` call each tick, so the write hook was reached;
   the salience conjunction (`benefit_exposure·(1+drive_weight·effective_drive) ≥ 0.3` AND complexity ≥ 0.2)
   simply never cleared at ecological contact magnitudes.

2. **The arms are behaviourally identical.** `benefit_contacts=1244` and `harm_events=4953` are *byte-identical*
   across wanting_first, liking_first, and both_delayed. The wanting/liking phase-gating manipulation produced
   **zero** behavioural divergence — the three conditions are one trajectory.

**Which criterion failed:** the negative-control / absolute criterion (`c4_delayed_sanity`) *and* every
discrimination criterion (c1/c2/c3). This is the substrate-ceiling fingerprint in its most extreme form:
*the positive control itself is on the floor*, so there is no measurement baseline against which an ordering
effect could ever express.

## 2. Claim-layer mapping

- **MECH-329** (the tagged target): *the wanting system seeds z_goal anchors via accidental benefit contacts
  **before** the liking system is calibrated.* This is an **ORDERING** claim — it predicts a *difference in the
  timing/quantity/complexity of super-ordinal writes between a wanting-first and a liking-first developmental
  schedule.* Testing an ordering requires that writes occur **in at least one arm**. With `total_writes=0`
  everywhere, the experiment measured the ordering of an empty set. The claim could not express itself.
- **MECH-189** (the substrate MECH-329 depends on): *high-salience child-phase contacts under high contextual
  complexity are written to persistent ContextMemory as super-ordinal anchors.* The substrate landed 2026-06-09;
  its own validation **V3-EXQ-588c used a forced-feed Stage-0 write** precisely to bypass the ecological
  z_goal-seeding ceiling. 669a re-introduced the ecological harness, so the salience gate was starved.

Did the experiment test either claim under conditions where it could express itself? **No.** An ordering claim
and a write-formation claim are both untestable when no write ever fires in any arm — and the manifest's own
`c4` sanity control confirms that floor.

**`claim_ids` accuracy:** the tags (MECH-329, MECH-189) are correct for *what the script intends* to test, but
because the substrate produced zero discriminative signal, the run weighs against neither claim. No tag drift
(distinct from the EXQ-048/MECH-057b inheritance failure mode).

## 3. Biological-reference triage

- **MECH-329** — closest reference is Berridge incentive-salience / mesolimbic-dopamine *wanting* preceding
  hedonic *liking* calibration in development (Berridge & Robinson; Zhang et al. wanting = r·κ(drive)). This is a
  **faithful biological translation**, not a formal-definition import. The mechanism has a robust existence proof.
- **MECH-189** — childhood goal-hierarchy formation; reference = developmental acquisition of super-ordinal goals
  under a protected early window (the claim's own `depends_on` names INV-041 childhood-prerequisite,
  INV-037/038 stored-vs-active, SD-016 cue-indexed ContextMemory).
- **Does the failure resemble a missing dependency of the reference mechanism?** Yes — directly. In biology,
  incentive-salience goal seeding presupposes a developmental stage in which the infant reliably *makes benefit
  contact* (a nursery / caregiver-feeding period). The REE analogue of that prerequisite is the
  `scaffolded_sd054_onboarding` Stage-0 forced-feed nursery. 669a ran the *ecological* `InfantCurriculumScheduler`,
  which hits the documented **goal_pipeline:GAP-2 foraging-competence / benefit-contact ceiling** — the agent never
  reaches self-sustaining contact, so z_goal stays `< 0.1` and the salience gate is never cleared. The FAIL is a
  **discovered (already-known) prerequisite**, i.e. *positive evidence for the dependency*, not a falsification of
  the seeding mechanism.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | intact | ordering/formation claims untested; no expression conditions met |
| Biological reference | clear | wanting-before-liking + childhood goal formation both have strong existence proofs; not formal imports |
| Developmental / dependency prerequisites | **missing** | the Stage-0 nursery (forced-feed z_goal) that MECH-189's own validation V3-EXQ-588c required is absent from this harness |
| Implementation completeness | complete | MECH-189 SuperOrdinalGoalMemory + write hook landed 2026-06-09; StepHarness calls update_z_goal — substrate is wired, just unfed |
| Environment adequacy | **wrong harness / too sparse** | ecological InfantCurriculum hits goal_pipeline:GAP-2; not the scaffolded nursery |
| Measurement adequacy | **misleading (vacuous)** | discriminative metric pinned at 0 in every arm incl. positive control → degenerate by construction |
| Integration adequacy | isolated | wanting/liking gating has no behavioural authority while z_goal never seeds (identical benefit_contacts) |
| Scale / capacity | adequate | 54277 steps/arm is ample; not a budget issue |

**Recommended `epistemic_category`: `substrate_ceiling`** (V3-tractable in principle; the existing ecological
substrate is too coarse to seed z_goal, so the claim cannot be measured on it). Equivalent degeneracy class to
V3-EXQ-642 (`z_block≡0`), V3-EXQ-514m (`C_WL≡0`).

## 5. Learning extracted

1. **Discovered/confirmed dependency (positive-negative):** MECH-329/MECH-189 cannot be evaluated on the ecological
   InfantCurriculum harness while goal_pipeline:GAP-2 is open. The FAIL *supports* the developmental-nursery
   prerequisite the claims' own design names.
2. **Degenerate-by-construction:** the manifest's `c4_delayed_sanity=false` is the tell — the positive control is
   itself on the floor, so this is not evidence about wanting-vs-liking ordering; it is the absence of any seeding.
3. **Harness mismatch is the actionable defect:** 669a imports `InfantCurriculumScheduler`, **not**
   `scaffolded_sd054_onboarding` — yet that nursery is `ready: true` in `substrate_queue.json` (flipped
   2026-06-11, V3-EXQ-603n PASS) and its forced-feed Stage-0 is the only validated z_goal-seeding path above the
   GAP-2 ceiling. The retest must run on it with a non-vacuity gate.

## 6. Recurrence / granularity-debt check

This is the **second** autopsy touching MECH-189 (prior: `failure_autopsy_V3-EXQ-588_2026-05-19`). The recurrence
trigger asks whether the two carry *different* failure signatures (→ granularity debt → `/claim-synthesis`).
They do **not**: 588 = the super-ordinal write path *did not exist yet*; 669a = the path now exists but is
*starved by the same upstream GAP-2 z_goal-seeding ceiling*. Both are the **one** structural property (z_goal never
seeds ecologically), at successive build stages — not a coarse claim hiding several finer mechanisms. **No
`/claim-synthesis` recommendation.** MECH-189/MECH-329 are correctly scoped; they are blocked, not coarse.

## 7. Routing

| Field | Value |
|---|---|
| recommended_evidence_direction | `non_contributory` |
| recommended_epistemic_category | `substrate_ceiling` |
| pending_retest_after_substrate | **true** |
| narrow_supports_flag | false |
| routing | **`/queue-experiment`** (re-issue on the ready nursery harness; substrate itself needs no new work) |
| substrate_queue action | **none** (`scaffolded_sd054_onboarding` already `ready: true`; the gap is the *experiment's harness choice*, not a missing substrate) |
| demotion | **none** (both claims already candidate / confidence 0.0 — nothing to demote; no falsification) |

**Retest spec (new EXQ letter — same scientific question, harness fix):** re-issue the wanting-first vs
liking-first vs both_delayed ordering test on the **`scaffolded_sd054_onboarding`** curriculum (Stage-0 forced-feed
nursery → wean), so super-ordinal writes actually fire, with a **pre-registered non-vacuity readiness gate**: the
`both_delayed` positive control must produce `anchor_count ≥ 1` (and `total_writes ≥ 1`) **before** C1/C2/C3
ordering criteria are scored — otherwise self-route `substrate_not_ready_requeue` rather than emitting a FAIL.
This is the exact same readiness discipline V3-EXQ-588c used for the MECH-189 substrate validation.

**Draft `evidence_quality_note` (for governance to write — do not write here):**
> V3-EXQ-669a (MECH-329 wanting-before-liking ordering; MECH-189 super-ordinal write) reclassified
> non_contributory + substrate_ceiling + pending_retest_after_substrate. The run is degenerate by construction:
> anchor_count = total_writes = p01_writes = 0 and p01_mean_complexity = 0.000 in **all three arms including the
> both_delayed positive/sanity control (c4=false)**, with byte-identical benefit_contacts (1244) and harm_events
> (4953) across arms — the discriminative metric is pinned at 0, so the ordering claim was measured over an empty
> set. Root cause = goal_pipeline:GAP-2 (the ecological InfantCurriculum harness never reaches self-sustaining
> benefit contact, z_goal_norm < 0.1, the MECH-189 salience write gate never fires). NOT a falsification of
> MECH-329 or MECH-189; both stay candidate / confidence 0.0. Retest owed on the `scaffolded_sd054_onboarding`
> nursery harness (ready: true 2026-06-11) with a both_delayed anchor_count ≥ 1 non-vacuity readiness gate.

## 8. Cross-references

- `goal_pipeline_plan.md` **GAP-2** — the foraging-competence / benefit-contact ceiling that is the root cause;
  the same blocker that left the V3-EXQ-514 lineage non_contributory.
- `failure_autopsy_V3-EXQ-588_2026-05-19` — prior MECH-189 autopsy (substrate-unbuilt stage of the same blocker).
- `failure_autopsy_V3-EXQ-514m_2026-06-11` / V3-EXQ-642 — sibling vacuous-criterion (`C_WL≡0` / `z_block≡0`)
  degenerate-run precedents.
- `substrate_queue.json` `scaffolded_sd054_onboarding` (ready: true, readiness_flip_2026_06_11) — the retest target.
- ree-v3/CLAUDE.md `MECH-189` substrate entry + `scaffolded_sd054_onboarding` amend chain — V3-EXQ-588c forced-feed
  precedent.
