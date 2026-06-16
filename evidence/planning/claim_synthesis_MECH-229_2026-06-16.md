# Claim Synthesis — MECH-229 (wanting/liking) decomposition PROPOSAL

- **Generated:** 2026-06-16T19:58Z
- **Skill:** `/claim-synthesis` (proposal-first; nothing lands in claims.yaml without per-child user approval)
- **Routed by:** `failure_autopsy_V3-EXQ-514q_2026-06-16.md` §8 (confirmed) — secondary route alongside the already-queued V3-EXQ-514r disambiguator.
- **Entry point:** direct nomination (MECH-229).
- **Status:** PROPOSAL — awaiting per-child approval.

## 0. One-line

MECH-229 bundles an **established** behavioral dissociation (a: wanting ≠ liking, object-bound) with a **substrate-blocked** drive-coupling leg (b: wanting is drive-state-modulated). Propose splitting (b) out into a distinct, immediately-testable, lit-grounded child claim (MECH-436), retaining MECH-229 as the narrowed umbrella for (a). This is **not** a demotion of MECH-229.

## 1. The cluster (Step 1–2)

Direct nomination MECH-229. The FAIL/`non_contributory` cluster on the 514 lineage (`bears_on: MECH-229`), all with a `/failure-autopsy` artifact:

| Autopsy | Run | Signature | Self-route / verdict |
|---|---|---|---|
| 514l (06-03) | foraging-competence prerequisite; C6 dissoc 0.0 (no reward-contact history) | substrate_ceiling | `non_contributory` / implement-substrate |
| 514m (06-11) | disabled VALENCE write paths → C_WL=0.0 vacuous (channel never written) | degenerate / test-design | `non_contributory` / queue-experiment |
| 514p (06-15) | raw-fraction criterion confounded by (N−1)/N categorical baseline | measurement / test-design | `non_contributory` / queue-experiment |
| 514q (06-16) | sub-threshold in-run drive magnitude (~0.006); criterion now fixed; delta=0.0 exact | substrate_ceiling | `non_contributory` / queue-experiment + **claim-synthesis** |

Alongside the cluster, **514o (06-15) PASSed at 0.80** — `mean_object_bound_wl_dissoc_fraction = 0.80` on the SD-049 multi-resource substrate — the genuine non-degenerate support for leg (a).

## 2. Discrimination gate (Step 3 — the load-bearing filter)

**Honest reading first.** Taken *individually*, each of the four FAILs falls into a Step-3 EXCLUDE class — 514l/514q are substrate-ceiling, 514m is degenerate (vacuous criterion), 514p is measurement/test-design. A naïve per-run application of the gate would STOP. That is the correct refusal for a cluster that is *only* test-design/substrate churn around a single mechanism.

**Why this cluster nonetheless PROCEEDS to decomposition** — three independent grounds, none of which is "manufacture a claim from a measurement bug" (the failure mode the gate guards against):

1. **The cluster's PASS/FAIL splits cleanly along a sub-mechanism boundary.** Every genuine *support* (514o, object-bound fraction 0.80; 514q `object_bound` 0.70 consistent) lands on leg (a); every FAIL/churn lands on the *drive-coupling* leg (b). When a claim's successes and failures partition along an internal boundary, that boundary **is** the granularity-debt line. The claim text names only "wanting ≠ liking"; it never separately asserts the *drive-state modulation* of wanting that legs (b) is failing to express.

2. **The 514 / wanting≠liking chain is the skill's own canonical granularity-debt exemplar.** SKILL.md (lines 18–22) cites *“MECH-229 ‘wanting != liking’ (the 514 chain) decomposed into the SD-057 object-binding layer”* as the paradigm case of real, load-bearing granularity debt. This is the **next** decomposition in that recognized chain — now separating the drive-coupling leg, exactly as the prior round separated object-binding.

3. **The anti-proliferation rail is satisfied: the proposed child is immediately testable, not a believed-tail inflation.** The (b) child carries a concrete `what_would_answer` (the drive-dependence delta with an effect-size gate) **and its first falsifier is already queued** — V3-EXQ-514r (overshoot + OFF control + recalibrated argmax-relevant readiness). We are separating an *established* leg from an *unmade-but-testable* leg, not minting an untestable claim from an instrumentation artefact.

**Gate verdict: PROCEED** (one child). The decomposition protects the established (a) from (b)'s substrate churn and gives (b) a named, falsifiable identity.

## 3. Common thread (Step 4)

> Every non-(a) failure in the cluster circles the same unnamed question: **does the homeostatic drive *state* modulate wanting (target and/or intensity), dissociably from liking?** MECH-229 asserts that wanting and liking are dissociable *signals*; it does not separately assert that wanting is **drive-state-modulated** — the incentive-salience core that 514m/514p/514q were all (in different broken ways) trying to measure and 514q finally isolated as substrate-blocked (in-run per-axis drive spread ~0.006 ≪ the argmax-moving regime).

## 4. Lit grounding (Step 5 — mandatory, already pulled this session)

`targeted_review_connectome_mech_347` (written 2026-06-16, same session as the autopsy):

- **Berridge 2006** (*Psychopharmacology*; conf 0.74, supports) — the canonical incentive-salience review. Wanting is cue-triggered and **“integrates Pavlovian information *with physiological state signals*.”** Explicitly flags that REE's `cue_pull` uses a fixed gain *“rather than a dopamine-analog state signal … the no-gate premise is faithful, but the magnitude control is a simplification.”** → directly names the (b) gap: drive-state amplitude modulation is the biologically load-bearing, under-implemented part.
- **Smith, Berridge & Aldridge 2011** (*PNAS*; conf 0.76, supports — highest in batch) — direct neural dissociation: dopamine stimulation amplified **only** the incentive-salience (“wanting”) component, leaving hedonic “liking” and learned prediction untouched. Wanting can be moved dissociably from value.
- **DiFeliceantonio & Berridge 2016** (*Eur J Neurosci*; conf 0.72, supports) — limbic activation **dynamically amplifies** cue attraction in a **competitive** way (one cue a stronger “motivational magnet” at the expense of another); flexible (cue followed to a new location). The behavioral face of drive/state-modulated wanting.

**Verdict:** biology is clear and not a formal import — incentive salience *is* drive/state-modulated cue attraction, dissociable from liking. The (b) child is grounded. (The same lit grounds MECH-347, the `cue_recall_wanting` implementation whose amplitude is `base_value·(1+κ·per_axis_drive)` — the κ·drive term the child claim is the behavioral validation of.)

## 5. Decomposition proposal (Step 6)

### MECH-229 — fate: **narrowed-and-retained as the umbrella for leg (a)**
- Keeps its title/subject as the **behavioral wanting ≠ liking object-bound dissociation** (established by 514o PASS 0.80; 514q object_bound 0.70 consistent).
- Status **unchanged this cycle** (`provisional`, `epistemic_category: standard`), per the confirmed autopsy §8. `narrow_supports_flag: true` and `pending_retest_after_substrate: true` stay (the remaining MECH-229 support is the single 514o object-bound pathway).
- The **drive-coupling leg is moved out** to MECH-436. A `decomposition` note records that the drive-state-modulation content is now carried by MECH-436 and is `pending_retest_after_substrate` with **V3-EXQ-514r as the owning falsifier**.
- **Leg (a) is NOT weakened.** No status/category/scoring change to the established dissociation.

### MECH-436 (next free at registration time) — **candidate child**

| Field | Value |
|---|---|
| `id` | MECH-436 (verify max at write time) |
| `claim_type` | `mechanism_hypothesis` |
| `subject` | `drive.wanting_drive_state_modulation` |
| `polarity` | asserts |
| `status` | `candidate` |
| `epistemic_category` | `substrate_ceiling` (V3-tractable in principle; V3 P2 foraging produces near-flat per-axis drive ~0.006 — too coarse to express drive-coupling; enrichment path = SD-049-PHASE-2 differential-depletion/κ-scaling amend, with a pre-registered V4-1 multi-agent-ecology dependency) |
| `implementation_phase` | v3 |
| `split_from` | MECH-229 |
| `depends_on` | MECH-229, SD-049, MECH-347, MECH-346 |
| `pending_retest_after_substrate` | true |

**Claim (one line):** Wanting is **drive-state-modulated** — the homeostatic drive state shifts the wanting target and/or intensity (incentive salience amplitude `∝ base_value·(1+κ·per_axis_drive)`), dissociably from liking; on a substrate with differential per-axis depletion the most-wanted object tracks the currently-most-depleted drive axis even when the liking (consummatory) target does not.

**`what_would_answer` (draft — testable):** A drive-dependence delta `mean(WL_drive − WL_nodrive) ≥ max(k·pstdev(delta), FLOOR)` where the in-run per-axis drive spread is in the argmax-moving regime (asserted by a recalibrated readiness gate, not merely spread > 1e-3) and an overshoot positive control flips `most_wanted` while an OFF/bank-disabled control floors at wanting==liking. **First falsifier already queued: V3-EXQ-514r** — overshoot flips `most_wanted` ⇒ drive *can* carve at adequate magnitude (514q FAIL is env/magnitude artefact, substrate_ceiling, → SD-049-PHASE-2 enrichment, **not** a weakens); overshoot does **not** flip even at large drive ⇒ genuine MECH-436 weakens.

**Cluster evidence it explains:** 514m, 514p, 514q (all circling drive-coupling expressibility/measurement); 514l's no-contact-history ceiling is the upstream prerequisite. Leaves 514o (object-bound dissociation) cleanly with MECH-229(a).

**Lit grounding:** `targeted_review_connectome_mech_347` (Berridge 2006 state-modulated amplitude; Smith 2011 dissociable wanting; DiFeliceantonio 2016 competitive drive-amplified cue magnet).

**Architecture-doc stub:** add to `docs/architecture/approach_avoidance_symmetry.md` under the MECH-112/MECH-229 section — "MECH-436: drive-state modulation of wanting (incentive-salience amplitude), split from MECH-229 2026-06-16; owning falsifier V3-EXQ-514r; substrate_ceiling pending SD-049-PHASE-2 differential depletion."

## 6. What this proposal does NOT do

- Does **not** weaken or demote MECH-229 or its established (a) dissociation.
- Does **not** build the SD-049-PHASE-2 substrate amend (contingent on V3-EXQ-514r resolving to substrate_ceiling — the overshoot-flips branch; left for a post-514r `/implement-substrate` session).
- Does **not** mark anything `shown` (MECH-436 lands `candidate`; only `/governance` on exp_conf promotes; only `/queue-experiment` tests; 514r is already queued).

## 7. Registration plan (on per-child approval only — Step 7)

1. Re-read claims.yaml insertion region (concurrency: a parallel `claim-synthesis-ARC-065` session may also touch claims.yaml).
2. Register MECH-436 (`candidate`, fields above, `what_would_answer` + `depends_on` + arch-doc stub). Confirm max id at write time.
3. Add the `decomposition` note to MECH-229 (drive-coupling leg → MECH-436; 514r owning falsifier). No status/category/scoring change to MECH-229.
4. `python scripts/build_claims_json.py` (validator + claims.json regen; confirm MECH-436 appears, stance tally moves).
5. Rebuild index (`build_experiment_indexes.py`).
6. **Derive-only reconcile** only if MECH-229's status/`v3_pending` changes — it does **not** this cycle, so no `record_decision.py` / closure-node prose edit is required for MECH-229. MECH-436 is a new `candidate` (no prior decision-log/closure-node state to reconcile).
7. Pathspec-limited commit (`-- docs/claims/claims.yaml docs/assets/data/claims.json docs/architecture/approach_avoidance_symmetry.md evidence/planning/claim_synthesis_MECH-229_2026-06-16.md`), `git show --stat HEAD`, push `HEAD:master`.

## 8. OUTCOME (2026-06-16) — APPROVED + REGISTERED

User approved per-child with one amendment: child tagged **`epistemic_category: substrate_conditional`** (not `substrate_ceiling`) — the response is to **wait for the upstream substrate** (planned-but-not-built SD-049-PHASE-2 differential-depletion / κ-scaling amend + the pre-registered V4-1 multi-agent-ecology dependency), not to enrich the current V3 env. Both categories suppress promote/demote and fire conflict alerts; neither fires `narrow_open_question` — same indexer dispatch.

Registered:
- **MECH-436** `drive.wanting_drive_state_modulation` — `candidate`, `substrate_conditional`, `implementation_phase: v3`, `v3_pending: true`, `split_from: MECH-229`, `pending_retest_after_substrate: true`, `depends_on: [MECH-229, SD-049, MECH-347, MECH-346]`, `what_would_answer` = drive-dependence delta with effect-size gate + owning falsifier V3-EXQ-514r. Location `docs/architecture/sd_057_object_bound_incentive_salience.md`. Stance: `believed` (exp_conf 0).
- **MECH-229** — RETAINED as the narrowed umbrella for leg (a). Added `related_claims: [MECH-436]` + a dated decomposition entry atop `evidence_quality_note`. **No** status / `epistemic_category` / `narrow_supports_flag` / `pending_retest_after_substrate` change — so **no derive-only reconcile** (record_decision.py / closure-node prose) required. Leg (a) NOT weakened.
- Architecture-doc stub added to `sd_057_object_bound_incentive_salience.md`.

`build_claims_json.py` → 818 claims (+1), MECH-436 present, no validator warning on it. Indexer rebuilt clean (1338 runs). The SD-049-PHASE-2 substrate amend is NOT built (contingent on 514r; left for a post-514r `/implement-substrate` session).
