# Failure Autopsy: V3-EXQ-875 (MECH-471 local-update competence-interference test)

Generated: 2026-08-03T16:48:16Z
Scope: single
Status: confirmed (interactive gate completed)

## 1. Facts

- **Run**: `v3_exq_875_mech471_competence_provenance_20260803T120202Z_v3`, queue_id `V3-EXQ-875`,
  claim `MECH-471`, `experiment_purpose: evidence`, machine `ree-worker-3`,
  `elapsed_seconds: 73643.66` (~20.5h wall-clock).
- **dry_run gate (Step 2a)**: checked via `scripts/check_dry_run_citations.py` -- 1 clean, 0 dry.
  Manifest top-level `dry_run: false`. This is a real run, not a smoke.
- **Outcome**: `FAIL`, `evidence_direction: unknown` (as recorded pre-autopsy),
  self-routed `interpretation_label: substrate_not_ready_requeue`.
- **Design** (EXP-0399): a shared REINFORCE agent acquires two survival competences under
  different hazard geometries (env A "corner", env B "banded"), then Phase 2 applies a
  targeted REINFORCE update to competence B only at increasing `strength`, and Phase 3
  re-measures competence A (unrelated) for degradation. `interference_delta_survival` is the
  load-bearing DV; polarity is deliberate -- FAIL (A degrades) SUPPORTS MECH-471, PASS WEAKENS
  it.
- **Failed criterion**: NON-DEGENERACY (an absolute/precondition criterion, not a
  discrimination criterion). `readiness.acquisition_ok: false` --
  `a_baseline_worst_seed=19.667` and `b_baseline_worst_seed=15.5`, both far below
  `survival_floor_ticks=90.0` (60% of the 150-step episode). `targeted_moved: false` --
  the Phase-2 perturbation moved competence B by exactly `0.0` at the worst seed, even at the
  highest strength (150). No competence was actually installed to interfere with; the
  driver's own non-degeneracy guard correctly declined to report a discrimination verdict.
  `non_degenerate: false`, `degeneracy_reason: "a_baseline_survival_horizon: floor-pinned
  (max=87.4167<=floor=90)"`.

### Root cause -- independently verified against the driver source, not taken on trust

`experiments/v3_exq_875_mech471_competence_provenance.py` calls
`experiments._lib.allon_training._train_all_on_agent(...)` three times (lines 270, 279, 288 --
competence-A acquisition, competence-B acquisition, Phase-2 targeted update). **None of the
three calls pass `zworld_p0_episodes`**, which defaults to `0` in the shared helper
(`allon_training.py:291`). This is the exact SD-070 defect already documented in
`ree-v3/CLAUDE.md` ("SD-070 ADOPTION in the `_train_all_on_agent` driver family"): with no P0a
z_world-encoder warmup, `split_encoder.world_encoder` is never stepped and `z_world` stays a
frozen random projection, silently, with no error. This is the identical defect that caused
V3-EXQ-728's original "3/3 seeds failed" result, fixed there by exactly this remedy
(`zworld_p0_episodes=60`).

I confirmed this by reading `allon_training.py`'s signature (`zworld_p0_episodes: int = 0`)
and every one of 875's three call sites directly -- the omission is unambiguous, not inferred
from the requeue note alone.

### Already corrected

A prior session (before this autopsy was invoked) diagnosed the same root cause and queued
**V3-EXQ-875a** (`supersedes: V3-EXQ-875`, correct alphabetic-suffix convention -- same
scientific question, implementation fix only): adds `ZWORLD_P0_EPISODES=60` to competence-A
acquisition, and aligns `P0_WARMUP_EPISODES`/`P1_ACQUIRE_EPISODES`/`STEPS_PER_EPISODE`/
`EVAL_EPISODES` to V3-EXQ-728's validated post-fix recipe (200/90/200/20, vs 875's
120/50/150/12) rather than guessing a partial bump. Validated via a throwaway probe before
queuing (`latent_stack_weight_delta`: 4/4 world_encoder tensors moved,
`zworld_encoder_trained=True`). Design (seeds, strength levels, dose-response, acceptance
criteria, polarity) is unchanged -- only training-readiness instrumentation was broken.
Status: `pending`, not yet run. Cost flagged honestly in the queue note (~55h estimated
single-worker commitment, claim explicitly not on the V3 critical path).

### Recording / provenance note (investigated, confirmed benign -- not a confound)

The manifest flags `substrate_stable_across_run: false`: the process-snapshot substrate hash
differs between the `strength=0` cells (`e001d2aa...`, `substrate_n_files=179`, resolved
2026-08-02T16:31:04Z) and the `strength=25/50/150` cells (`b1fa9593...`,
`substrate_n_files=181`, resolved 2026-08-02T20:39:17Z) -- a ~4h drift during this run's
~20.5h wall-clock. I traced this: six `ree_core`-touching commits landed on `ree-v3` `main`
in that window (SD-092 primitive + call-site wiring, SD-093 effort/persistence modulation,
MECH-203 tiebreak, plus two experiment-only commits) -- accounting for the +2 file count.
Every one of the substrate-touching commits adds a new **default-off** config flag
(`use_hierarchical_goal_credit`, `use_progress_velocity_effort_modulation`, both default
`False`, bit-identical off) to code paths this experiment's config never enables. This is
confirmed genuinely benign, not asserted: the manifest's own internal determinism check shows
`a_baseline` is bit-identical across all four `strength` arms for each seed (e.g. seed 42:
19.666667 at strength 0/25/50/150 identically), exactly as the driver's design requires if
Phase 1 is unaffected by the mid-run substrate churn. Recorded here as a provenance
observation, not as a confound requiring re-run.

## 2. Claim-layer mapping (MECH-471)

`claims.yaml`: `status: candidate`, `epistemic_category: standard`, `implementation_phase: v3`,
registered 2026-07-22, `depends_on: [MECH-392, INV-080, MECH-401, MECH-083, MECH-261,
ARC-092]` (consolidation-path machinery MECH-471 generalises FROM -- the driver's own docstring
correctly notes these are NOT needed for this behavioural probe; testable now on existing
substrate). No prior `evidence_quality_note`, no prior autopsy (first FAIL cycle for this
claim -- confirmed via `granularity_debt_cluster.py MECH-471`: 0 tagging targets).

**Did the test let the claim express itself?** No. The precondition (an above-floor,
cross-seed-variant competence to interfere with) was never met, so this run produced no
information about whether local competence updates interfere with unrelated competences on
this substrate. This is a harness-configuration gap, not a claim-layer problem, and not a
substrate ceiling -- the substrate itself (z_world encoder, SD-070) is proven functional by
V3-EXQ-728's fix.

## 3. Biological-reference triage

MECH-471 asserts that behavioural-competence updates need the same
bounded/provenanced/rollback-capable discipline already built for memory consolidation
(MECH-392/INV-080/MECH-401), grounded in the same biology as retrograde-interference /
motor-skill-consolidation literature (Brashers-Krug, Shadmehr & Bizzi 1996; Krakauer, Ghez &
Ghilardi 2005; Walker, Brakefield, Hobson & Stickgold 2003).

**This literature is already on file** -- pulled 2026-07-29 under
`targeted_review_mech_457_consolidation` for the closely-related sibling claim **MECH-476**
("competence retention dissociable from acquisition... consolidation is properly defined as
resistance to retrograde interference [Krakauer 2005]"). MECH-476 tested this using the
Krakauer A->B->A design directly (BC-install foraging competence, then unconstrained-RL
erosion, varying install DOSE and A->B offline INTERVAL, plus a Moncada & Viola 2007
novelty-tagging arm) and was **retired 2026-08-01**: all three falsifier arms
(V3-EXQ-836a dose, 836d novelty-tagging, 836e interval) found retained-fraction **invariant**
to every manipulated variable -- REE's existing protection pathways (distributional critic
V3-EXQ-788, KL anchor V3-EXQ-792) are plain regularizers, not a dose/time-sensitive
consolidation PROCESS.

This does not resolve MECH-471 -- the design axis differs (MECH-471 tests cross-*environment*
interference via a targeted-dose REINFORCE perturbation on two structurally distinct
competences; MECH-476 tested within-task BC-install-then-RL-erosion) -- but it is directly
relevant prior evidence for judging what "supports MECH-471" would mean, and for whether
MECH-471 and the MECH-459/460/475/476 cluster are probing meaningfully separate ground before
committing ~55h of compute to 875a. **User-confirmed disposition (interactive gate,
2026-08-03): note this adjacency in the record and move on -- no `/claim-synthesis` escalation
now.** Surfaced here so a future reader (governance, or whoever reviews 875a's eventual
result) has it in view.

Lit status for MECH-471 itself: **absent** (no dedicated `targeted_review_mech_471*` entry
exists) -- the adjacent MECH-476 pull substantially covers the same biological ground, so no
new `/lit-pull` commission is recommended at this time; flag for a future MECH-471-specific
pull only if 875a's result makes the biological framing load-bearing.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | Test never reached a state where MECH-471 could express itself -- no verdict possible either way |
| Biological reference | clear, adjacent ground already tested | Krakauer 2005 / Walker 2003 retrograde-interference paradigm on file via MECH-476 (sibling, same lit base, just retired) |
| Prerequisites | present but not enabled | SD-070 z_world encoder warmup exists and works (proven by V3-EXQ-728's fix) -- simply omitted from this driver's 3 call sites |
| Implementation completeness | harness bug (driver-level, not substrate) | Substrate itself is fine; an opt-in flag defaulting to 0 was never wired in |
| Environment adequacy | adequate | Env config (hazard geometry, reef placement) not implicated |
| Measurement adequacy | adequate -- guard worked as designed | Non-degeneracy check correctly caught the degenerate acquisition state rather than emitting a false discrimination verdict |
| Integration adequacy | n/a | Single-agent, single-substrate test; no cross-module integration question raised |
| Scale / capacity | contributing factor, already corrected | Training budget (120/50/150/12) also below 728's validated recipe (200/90/200/20); aligned in 875a |

Recording provenance: complete (`ree-v3/validate_recording.py` reports 0 always-core gaps).
This is not a recording gap -- the readout needed to adjudicate (readiness/degeneracy fields)
was present and is exactly what correctly triggered the self-route.

## 5. Learning extracted

- The SD-070 z_world-warmup omission is a **recurring driver-configuration defect class**
  across the `_train_all_on_agent` driver family (now confirmed twice: V3-EXQ-728 originally,
  V3-EXQ-875 here) -- the opt-in default-`0` design makes it silent and easy to omit. Worth a
  standing lint (a `dry_run_unreachable_criterion`-style static check flagging a
  `_train_all_on_agent` call site with no `zworld_p0_episodes` in a driver whose acceptance
  criteria depend on z_world-derived representations) rather than relying on each new driver
  author remembering the CLAUDE.md note. **Not fixed in this session** (out of this autopsy's
  scope; flagged as follow-on below).
- The non-degeneracy guard in this driver worked exactly as intended: it declined to report a
  discrimination verdict on a degenerate acquisition rather than silently returning a
  misleading PASS or FAIL on MECH-471. This is a positive validation of the guard design, not
  a finding against the claim or the substrate.
- MECH-471 and the MECH-457/459/460/475/476 cluster are adjacent but not (yet demonstrated to
  be) redundant; the adjacency is worth having in view before 875a's result is read, and
  worth a `/claim-synthesis` look if 875a itself returns an ambiguous or contested reading.

## 6. Repair pathway / routing (user-confirmed)

- **Routing: `queue-experiment`** -- already executed as V3-EXQ-875a before this autopsy ran;
  this autopsy ratifies that correction rather than proposing a new one. No changes requested.
- **`recommended_substrate_queue_entry.action: none`** -- no substrate gap. The SD-070 z_world
  encoder substrate already exists and functions correctly (proven by 728); this was purely a
  driver-configuration omission, now fixed in 875a.
- **Re-derive brake**: inert. First `substrate_ceiling`/`non_contributory`-class autopsy for
  MECH-471 (count = 0 prior; this autopsy does not even read as `substrate_ceiling` --
  `precondition_unmet`/`non_contributory` per R3 would not count toward that brake regardless).
  No refusal of a same-claim re-queue is warranted or issued -- 875a is exactly the same-claim,
  same-design, instrumentation-only re-run the brake would permit.
- **Granularity-debt trigger**: does not fire. 0 tagging targets in the recurrence cluster
  (first autopsy for this claim); no `weakened` reading exists to found a recurrence pattern
  on.
- **Fan-out**: not applicable. This is a single, non-discriminating precondition failure with
  one clear, already-identified, already-fixed root cause -- not a discrimination bottleneck
  between live rival hypotheses.

## 7. Draft `evidence_quality_note` (for `/governance` to apply, NOT written by this skill)

> [2026-08-03 failure-autopsy, V3-EXQ-875, confirmed]: FAIL self-routed
> `substrate_not_ready_requeue` -- correctly. Root cause verified against driver source: all
> three `_train_all_on_agent` calls in `v3_exq_875_mech471_competence_provenance.py` omit
> `zworld_p0_episodes` (defaults to 0), the exact SD-070 defect documented in `ree-v3/CLAUDE.md`
> and previously responsible for V3-EXQ-728's original failed seeds. No competence was
> installed above floor (`a_baseline_worst_seed=19.67`, `b_baseline_worst_seed=15.5` vs
> `floor=90.0`) and the targeted perturbation moved nothing (`targeted_moved=false`) -- the
> run yields no information about MECH-471 either way. Non-contributory /
> precondition_unmet, not evidence toward or against the claim. Corrected re-run already
> queued and validated pre-run: V3-EXQ-875a (`supersedes: V3-EXQ-875`), zworld_p0 warmup added,
> training budget aligned to V3-EXQ-728's validated recipe. Note for whoever reads 875a's
> result: sibling claim MECH-476 (same Krakauer 2005 / Walker 2003 lit base, retired
> 2026-08-01) found REE's existing competence-protection pathways are plain regularizers, not
> a dose/interval-sensitive consolidation process -- relevant adjacent context, not
> dispositive for MECH-471's distinct cross-environment design. Stays candidate;
> `v3_pending` not applicable (was not set). No substrate_queue action -- this was a driver
> configuration gap, not a substrate gap.

## 8. Dry-run / recording checks (per skill Step 2a / Step 2)

- `dry_run_checked: true`, `excluded_dry_run_ids: []` (target itself is clean, not dry).
- `ree-v3/validate_recording.py`: 0 always-core gaps, 0 thin-pack drops, 0 schema warnings.

## 9. Frozen hypothesis-space ledger (Step 9b)

**Skipped, deliberately.** This target has `recommended_evidence_direction` set
(`non_contributory`), which technically meets condition (ii) of Step 9b's trigger, but it is
exactly the skill's own named skip example: "a lone non-fan-out FAIL that discriminates
nothing and opens no rival set." No `fanout_recommendation` was emitted, no existing question
in `hypothesis_space_registry.v1.json` covers MECH-471 or this design (checked: 0 matches by
claim id or title/short_title substring "interference"), and the run itself resolved nothing
(precondition_unmet -> per the Step 9b state-mapping table, would stay `alive` even if
registered). Registering a brand-new question solely to record "1 uninformative run, still
alive" was judged not worth the denominator overhead for a first-cycle precondition failure;
skipping cleanly per the skill's own guidance.

## 10. Session notes

- Coordination-plane pause claim (`failure-autopsy-10b982-pause`) **failed arbitration** (exit
  3): three sessions already hold earlier active claims naming
  `REE_assembly/docs/claims/claims.yaml`, `evidence/planning/substrate_queue.json`, and
  `ree-v3/experiment_queue.json` (`epic-mirzakhani-4928b5` SD-091 wiring;
  `metaworker-chip-20260803-848b-arc005-ladder`; `metaworker-chip-20260803-873a-mech322-fraction-gate`).
  Per CLAUDE.md arbitration rule, this session is not the owner and did not proceed with the
  pause claim (nothing was written, so nothing to reverse). This autopsy does not touch any of
  the contended files, so the lack of a pause does not affect its own correctness -- noted here
  for completeness per the skill's handover convention.
