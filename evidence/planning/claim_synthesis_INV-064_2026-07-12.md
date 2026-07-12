# Claim-Synthesis Proposal — INV-064 (e1_e2_e3_maturational_sequence_necessity)

- **Generated (UTC):** 2026-07-12T11:20Z
- **Trigger:** 2nd INV-064 degeneracy, routed from `failure_autopsy_V3-EXQ-740a_2026-07-12` (user selected `/claim-synthesis` at the autopsy interactive gate).
- **Cluster:** `V3-EXQ-740` (IV ran backwards) + `V3-EXQ-740a` (harm DV undecodable from z_world). Both `non_degenerate=false`, `non_contributory`, `measurement_degeneracy`.
- **Verdict:** DECOMPOSE — INV-064 becomes an **umbrella**, retained at `candidate / pending_substrate_reconfirmation`, over **two stream-specific child bounds**.
- **Promotes / demotes NOTHING.** No substrate build owed. Children land as `candidate`.

---

## 1. Discrimination gate — why this is granularity debt, not the MECH-341 STOP pattern

Two `non_degenerate=false` runs *look*, on a naive read, like the MECH-341 `660/660a/660b`
test-design-debt STOP case (iterated degeneracies → retire the falsifier, do not decompose).
That read is wrong here, and the difference is structural — it is the **mirror image**:

| | MECH-341 660-lineage (STOP) | INV-064 740-cluster (PROCEED) |
|---|---|---|
| Direction of mismatch | test asked a **finer** axis than the claim asserts (granularity **over-reach in the test**) | claim is **coarser** than the substrate (granularity **debt in the claim**) |
| Substrate streams | one well-posed stream, mis-measured | **two** separately-encoded, separately-maturing streams the claim lumps as one |
| Correct fix | retire/repair the falsifier; no new claim | split the claim to match the substrate's stream structure |

INV-064 asserts a **single** bound — "E3's harm/goal evaluator quality is strictly bounded by
E1/E2 representational differentiation" — over inputs its canonical text names as **"z_world from
E1 and action_objects from E2."** But SD-010 (verified in `ree-v3/ree_core/predictors/e3_selector.py`
+ `ree_core/latent/stack.py`) deliberately splits E3 evaluation into **two streams with two
encoders and two maturation trajectories**:

- **goal/world-feature evaluation** reads **z_world** (E1 encoder) — `harm_eval(z_world)` /
  `benefit_eval` / goal scoring (`harm_eval_head`, `e3_selector.py:593`).
- **nociceptive harm evaluation** reads **z_harm = HarmEncoder(harm_obs)** — `harm_eval_z_harm`
  (`e3_selector.py:660`), where `HarmEncoder` (`stack.py:119`) is instantiated **outside** the
  z_world encoder and is **exempt from reafference correction** (introduced to resolve the
  EXQ-027b over-correction paradox: the ReafferencePredictor was subtracting hazard when harm was
  fused into z_world).

The two degeneracies are **not** two independent measurement bugs on one well-posed claim. They
are the probe colliding with the **unnamed stream-split**:

- **740** mis-measured **z_world** differentiation (eff_rank of a smoothed EMA latent ran backwards).
- **740a** measured **harm on z_world** — but SD-010 routes harm through **z_harm**; 740a's
  degeneracy **is the discovery** that the claim names the wrong stream for its harm leg. The
  dispositive contrast: from the *same* frozen z_world, harm **world-features** decode fine and
  **rise** with maturation (`world_feat_decode_r2` 0.048 → 0.245), while realized **scalar harm**
  does not (`harm_decode_r2` 0.034, flat) — z_world is not harm-blind, the harm *stream* is elsewhere.

A test tweak cannot fix this, because the claim's *scope* spans two scientifically distinct bounds
on two different trajectories. **This clears the granularity-debt bar** (Step 3): ≥2 distinct,
genuine, substrate-ready failure signatures circling one claim, whose common thread is a mechanism
the broad claim does not name.

**Anti-proliferation rail satisfied.** Both children come out **immediately testable with distinct,
substrate-ready observables** — neither is a plausible-sounding formal import:

- Child (i) already has **first positive evidence** (`world_feat_decode_r2` rose 0.048 → 0.245 in
  740a — "first valid demonstration that E1/E2 task-relevant differentiation increases with
  maturation on the V3 substrate").
- Child (ii) has a clearly-specified z_harm observable the **re-derive brake explicitly permits**
  (the brake refuses only a *same-observable* z_world 740b; a z_harm-decodability probe is a
  different observable).

**Not the other three exclude-classes:** not test-design debt (the fix is not "repair one test" —
the claim spans two streams); not clean single falsification (the claim is not wrong, it is
under-differentiated — its world leg is partly *supported*); not substrate-not-ready (both streams
+ both evaluators already exist in V3; **no build owed**).

---

## 2. Common thread (Step 4)

> INV-064 asserts one "E1/E2 differentiation → E3 evaluator quality" bound, but the substrate
> implements E3 evaluation as **two separately-encoded, separately-maturing streams** (z_world for
> goal/world-feature evaluation; z_harm for nociception), so the single bound is really **two bounds
> on two different maturation trajectories** — and the claim never names the split.

---

## 3. Lit grounding (Step 5)

The developmental-**ordering** biology (PFC last to myelinate) is a strong existence proof and was
*not* the bottleneck — no full `/lit-pull` for it. The **new** content the decomposition introduces
is that the **harm/nociceptive evaluator matures on a distinct trajectory** from the world/goal
evaluator. That is grounded:

- **Separate anatomical pathway.** Nociception reaches operculo-insular / mid-cingulate cortex via
  parallel **spino-thalamic and spino-parabrachial** projections, temporally and anatomically
  distinct from the later fronto-parietal exteroceptive activity — Bastuji et al. 2016, *Hum Brain
  Mapp* [1]. (Matches the `HarmEncoder` docstring's stated basis.)
- **Distinct developmental maturation of the nociceptive projection.** The MD→ACC nociceptive
  projection undergoes its own **silent-synapse → AMPAR-stabilised maturation** process (GluN2B-
  enriched nascent synapses maturing/unsilencing) — Wang et al. 2020, *Pain* [2]. The harm stream
  has a maturation trajectory of its own, mechanistically separate from exteroceptive-cortex
  differentiation.
- **Different timetables (the load-bearing point).** The **dual-systems / maturational-imbalance**
  model: the socioemotional/affective (value/harm) system and the cognitive-control (goal) system
  "**develop along different timetables**" — Casey et al. 2011 [3a]; Strang et al. 2013 [3b]. This
  is the biological warrant for **two** stream-specific bounds rather than one; INV-064's own `notes`
  ("adolescent risk-taking persists well past sensory-motor competence") already gesture at exactly
  this dissociation.

No lit finding undermines child (i) (the z_world goal-eval bound). The lit **supports the split.**

---

## 4. Proposed decomposition

### INV-064 — fate: **umbrella (narrowed-and-retained)**
Stays `candidate / pending_substrate_reconfirmation`. Its "E3 evaluator bounded by E1/E2
differentiation" clause is now understood as realised through the two stream-specific child bounds
below. **No edit to its `status`, `evidence_direction`, or `evidence_quality_note`** (governance
consumes the 740a note separately). Add only a `decomposition_note` wiring the children.

---

### Child (i) — proposed **INV-088** (next free at write time)
- **title:** `world_goal_evaluator_bounded_by_z_world_differentiation`
- **claim_type:** invariant · **invariant_type:** emergent · **emergent_from:** [ARC-001, ARC-003, ARC-019]
- **subject:** `development.maturational_sequence`
- **status:** candidate · `pending_substrate_reconfirmation: true` (inherits provisional ARC-019)
- **claim (one line):** E3's goal / world-feature evaluation quality (`harm_eval(z_world)`,
  `benefit_eval`, goal scoring) is strictly bounded by **z_world (E1) representational
  differentiation**; productive training of the z_world-reading evaluators cannot precede sufficient
  E1 schema differentiation.
- **what_would_answer:** A frozen-representation curriculum-order contrast (onset including a
  genuinely immature anchor ~0) where (a) world-feature decodability from frozen z_world
  (`world_feat_decode_r2`, predictive z_world[t]→harm_obs[t+1]) rises monotonically with E1/E2
  maturation — **already established by 740a, 0.048 → 0.245, `PC_iv_moved` passed** — AND (b) the
  held-out quality of a z_world-reading E3 evaluator (re-init head, fixed budget, frozen z_world)
  improves monotonically with that rising decodability. The remaining test is the **DV coupling**
  (evaluator quality tracks z_world differentiation); the IV leg is done.
- **depends_on:** [INV-064, ARC-001, ARC-003, ARC-019]
- **grounded by:** PFC-last-myelination existence proof (parent); dual-systems cognitive-control
  leg [3a][3b].
- **epistemic_category:** testable-now (NOT `substrate_ceiling` — substrate ready, partial positive
  evidence in hand).
- **Motivating evidence:** 740a IV leg (the *supported* half of the cluster).

---

### Child (ii) — proposed **INV-089** (next free at write time)
- **title:** `harm_evaluator_bounded_by_z_harm_differentiation`
- **claim_type:** invariant · **invariant_type:** emergent · **emergent_from:** [ARC-003, ARC-019, ARC-027]
  (ARC-027 = nociceptive separation / SD-010 stream)
- **subject:** `development.maturational_sequence`
- **status:** candidate · `pending_substrate_reconfirmation: true`
- **claim (one line):** E3's **nociceptive** harm-evaluation quality (`harm_eval_z_harm`) is strictly
  bounded by **z_harm = HarmEncoder(harm_obs) representational differentiation** — a maturation
  trajectory **distinct** from z_world's (HarmEncoder is a separate encoder, exempt from reafference
  correction). Productive harm-evaluator training cannot precede sufficient z_harm differentiation.
- **what_would_answer:** A frozen-representation contrast over **HarmEncoder (z_harm)** maturation:
  decode realized `harm_target` from **frozen z_harm** across HarmEncoder onset, verify
  **z_harm-harm-decodability RISES with z_harm maturation** (the positive control that harm is
  decodable-in-principle from **the stream E3 actually uses**), then show `harm_eval_z_harm` held-out
  quality is bounded by z_harm differentiation. Trajectory reported **separately** from child (i)
  (distinct encoder). **Explicitly NOT a z_world decode** — the re-derive brake refuses a
  same-observable 740b; this probes z_harm, a different observable.
- **depends_on:** [INV-064, SD-010, ARC-003, ARC-019, ARC-027]
- **grounded by:** separate spino-thalamic/parabrachial → insula/ACC pathway [1]; distinct
  nociceptive-projection synaptic maturation [2]; dual-systems affective leg / different timetables
  [3a][3b].
- **epistemic_category:** testable-now (substrate ready: `harm_eval_z_harm` + `HarmEncoder` exist).
- **Motivating evidence:** 740a harm leg (the *mis-streamed, never-validly-exercised* half — the
  measurement collision that revealed the split).

---

## 5. Supersession / narrowing

- **INV-064:** narrowed-and-retained as umbrella; unchanged status/evidence. Gains children INV-088,
  INV-089 as reverse-deps + a `decomposition_note`.
- **No existing claim is superseded or demoted.** The children are *finer* than INV-064, not
  replacements; INV-064's ordering-necessity content (E1→E2→E3) is untouched.
- **Downstream:** MECH-214 (`depends_on: [INV-064, ...]`) and MECH-215 (`depends_on: [INV-064, ...]`)
  continue to depend on the **umbrella** — no rewiring needed (they rest on the maturational-sequence
  necessity as a whole, not on a single stream leg).

---

## 6. References

- [1] Bastuji et al. 2016, *Human Brain Mapping* — Pain networks: spatiotemporal analysis nociception→conscious perception. https://consensus.app/papers/details/72e6b2106fbd5fa78907e811e7085012/
- [2] Wang et al. 2020, *Pain* — Neuropathic pain generates silent synapses in thalamic (MD)→ACC projection. https://consensus.app/papers/details/7b220fca2a605afca663ff087a2f526c/
- [3a] Casey et al. 2011, *J Res Adolesc* — Braking and Accelerating of the Adolescent Brain (maturational-imbalance). https://consensus.app/papers/details/dbf4881d4e8d5a6183ebc4481dcfcd7a/
- [3b] Strang et al. 2013, *Front Hum Neurosci* — The value of the dual systems model of adolescent risk-taking ("different timetables"). https://consensus.app/papers/details/baa3a3ef891d5dedb15f75cf67bce307/

---

## 7. Post-approval registration plan (Step 7 — NOT executed until per-child approval)

1. `TASK_CLAIMS` claim covering `docs/claims/claims.yaml`, `docs/assets/data/claims.json`, this doc.
2. Re-read INV-064 insertion region + re-check max INV id at write time (currently INV-087 → children
   INV-088/089; verify no concurrent addition via `git log`).
3. Register approved children (candidate, each with `what_would_answer` + `depends_on` +
   architecture-doc stub); add INV-064 `decomposition_note` wiring the umbrella.
4. `python scripts/build_claims_json.py` (validator + regen; confirm children appear, stance tally moved).
5. Pathspec commit `-- docs/claims/claims.yaml docs/assets/data/claims.json evidence/planning/claim_synthesis_INV-064_2026-07-12.md`; `git show --stat HEAD`; push `HEAD:master`.
6. Hand off: children ready for `/queue-experiment` (child ii's z_harm test is the re-posed successor
   to 740a; child i's DV-coupling test extends the already-validated 740a IV leg).
