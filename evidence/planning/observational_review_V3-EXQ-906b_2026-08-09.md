# Observational Review: V3-EXQ-906b -- Full-Stack Observational Fishtank

**Generated:** 2026-08-09T17:17Z
**Type:** organism-level observational review (NOT a failure autopsy -- 906b is a PASS diagnostic
showcase, `claim_ids=[]`, `evidence_direction=non_contributory`; nothing here weights governance)
**Run:** `v3_exq_906b_full_stack_observational_fishtank_20260809T163034Z_v3` (machine `ree-cloud-4`,
substrate `ree-v3 240ae31537`, 897s, seed 0)
**Sources read:** manifest + `_episode_log.json` (3909 eval steps / 8 segments), the 906b driver,
`_read_affect` (v3_exq_664), `ree_core/policy/tonic_vigor.py`, `ree_core/regulators/mech295_liking_bridge.py`,
`ree_core/residue/field.py` (VALENCE_* indices), `ree_core/pag/freeze_gate.py`,
`ree_core/sleep/phase_manager.py`, `update_z_goal` (agent.py), `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md`,
`sleep_substrate_plan.md`, `experiment_queue.json`, `substrate_queue.json`.

---

## 0. Verdict on the central interpretation

> *906b appears to establish a survivable, behaviourally diverse REE whose basic food-seeking and
> harm-avoidance competencies are present but imperfect. The Fishtank has now moved from proving REE
> can stay alive long enough to observe toward exposing organism-level integration and competency
> questions: appetitive coherence, sleep-state integration, defensive-response availability, and
> meaningful temporal coupling between internal state and behaviour.*

**Supported, with two sharpenings that the telemetry forces:**

1. **Survivable + behaviourally diverse: CONFIRMED.** Segments now run 413--500 steps (mean 488.6 vs
   906's ~14.9), 6/8 to the step cap. Six behavioural modes are active (shelter 1463, neutral 774,
   assert 738, approach 643, avoid 169, explore 122 steps) with per-segment action entropy ~1.9--2.1.
   This is genuine *behavioural* diversity. **But it is diversity-in-place, not diversity-in-space**:
   the agent visits only 18--39 of 144 cells per segment (12.5--27%) and physically moves on only
   ~20--32% of steps (95--158 of 500). The provisional "pure behavioural diversity exists" reading
   holds at the affective-mode/action level; spatial exploration is narrow.

2. **The headline organism-level finding is DECOUPLING, not incompetence.** The affect channels vary
   substantially but are **temporally decoupled** from both environmental events and subsequent
   behaviour (Section 4). "Channels are alive" and "channels organise behaviour" are separable, and
   906b shows the first without the second. This is the most important novel result and the correct
   next frontier -- ahead of, and partly upstream of, "increase competency."

---

## 1. Behavioural diversity (MEASURES: valid; REE: diversity present)

| metric | value |
|---|---|
| modes active (steps) | shelter 1463, neutral 774, assert 738, approach 643, avoid 169, explore 122, freeze 0 |
| action entropy / segment | 1.88 -- 2.10 bits |
| unique cells / segment | 18 -- 39 of 144 (12.5% -- 27.1%) |
| steps with movement / segment | 95 -- 158 of ~500 (~20% -- 32%) |

Diversity is real and multi-modal; the qualitative "clearly behaviourally diverse" observation is
corroborated. The nuance to carry forward: the dominant mode is `shelter` (in-reef + elevated harm),
and the agent is spatially sedentary. Diversity of internal mode does not yet translate to diversity
of spatial trajectory.

---

## 2. Competency: food-seeking and harm-avoidance

### 2a. Harm-avoidance -- GENUINE, imperfect (REE: competent-ish; ENVIRONMENT + MECHANISM: working)

- Mean Manhattan distance to nearest hazard across all steps = **3.52**; on harm-taking steps = **1.02**.
- Only **13.0%** of steps take harm (278 of 3909); 45.6% of steps are within distance <=2 of a hazard.
- Segment endings: 6/8 step-cap, only 2/8 health-depleted.

Read: the agent keeps a real standoff distance and takes damage essentially only when adjacent
(dist~1) -- exactly the "close-range harm, smell-before-harm" ecology 906b's radius fix engineered.
This is **present but imperfect** harm-avoidance competency, consistent with the user's observation.
The 906b proximity-radius fix (env layer) is doing its job.

### 2b. Food-seeking -- WEAK, and mis-attributed by the coarse signal (REE + MECHANISM + ENVIRONMENT, mixed)

The positive-signal picture looks healthy at first (1516 steps with positive `harm_signal`, sum
+42.6; 1384 `benefit_approach` transitions) **but is not discrete-resource acquisition**:

- Mean distance to the nearest mapped resource is **6.23 across all steps and 6.02 on benefit steps**
  -- i.e. the agent is *no closer to a resource when it receives benefit than at baseline*.
- Only **11** actual `resource` (consummatory) transitions occurred in 3909 steps.
- `resource_respawn_on_consume=False`; `reef_enabled=True` (3 patches); `shelter` is the dominant mode.

Read: the benefit REE receives is overwhelmingly the **ambient proximity-benefit / reef field**, not
navigation-to-and-consumption-of the 5 discrete resources. So "moderately capable of finding food"
is better stated as **"exploiting a diffuse benefit gradient (reef/proximity) without organising
behaviour around discrete resource localisation."** This is *not* purely a REE failure: the benefit
field is diffuse by construction (`proximity_benefit_scale=0.03` shares the tightened
`proximity_approach_threshold`), and with non-respawning resources the consummatory target is sparse.
The appetitive->consummatory sequence the user wants inspectable is barely exercised in this ecology.

---

## 3. Appetitive system inspection (wanting / vigor / liking)

The user's three observations each resolve to a *different* failure location.

### 3a. Wanting (`z_goal`) rises little -- WEAK/SPARSE COUPLING, not a dead channel (MECHANISM)

`z_goal` = `goal_state.goal_norm()`. Distribution over 3909 steps: min 0, **p50 = 0.000**, mean
0.024, p95 0.179, **max 0.476**. So wanting is at floor for >50% of steps and occasionally rises to
~0.48. `update_z_goal` seeds `z_goal` on **consummatory benefit contact** (gated, then decays); with
only ~11 real consumption events and a diffuse benefit field, the wanting channel is seeded rarely and
decays between seeds. **The channel works** (stage-0 peak was 0.481; it does rise) but is starved of
the discrete-contact events that drive it. Classification: weak/sparse coupling driven by the ecology
(Section 2b), not a broken mechanism. The user's "wanting rose very little despite food-seeking" is
**confirmed and explained**: the "food-seeking" is proximity-gradient exploitation, which does not
seed wanting.

### 3b. Vigor flat at 0.0 -- KNOWN MECHANISM issue, NOT telemetry (MECHANISM; already tracked)

Decisive: per-step `vigor` is **exactly 0.0 on all 3909 steps (0 nulls)**, so
`_last_control_vector["shared"]["tonic_vigor_v_t"]` *is* being populated -- this is a real zero, not a
missing key. `TonicVigor.compute_score_bias` sets
`v_t = max(v_t_floor=0, max(0, v_raw) * gate_e * gate_d * gate_p)`, where `v_raw` is a slow EWMA of
`-score` (E3 lower-is-better). If realised E3 scores keep `v_raw <= 0`, then `max(0, v_raw)=0` and
`v_t` is pinned at 0 regardless of gates. This is exactly the **"sign/scale failure on v_raw"** the
`TonicVigorConfig.v_t_floor` field was added to diagnose (V3-EXQ-563 family:
`563_action_bias_actuator_test`, `563b_candidate_support_repair`, `563c_stratified_cem_bias_calibration`).
**Not novel and not a visualisation problem** -- flat-zero vigor is the expected output of the known
`v_raw` sign issue under this stack. Reference, do not re-register.

### 3c. Liking not visualised -- MEASUREMENT/TELEMETRY GAP, signal EXISTS (MEASURES; fixable)

`_read_affect` (v3_exq_664, the shared telemetry reader) emits `z_harm_*`, `drive`, `z_goal`, `vigor`,
`override`, `z_block`, `excite`, `dread` -- **there is no `liking` key at all.** But the liking signal
*does* exist in the substrate: `ResidueField` valence is a 6-vector
`[WANTING(0), LIKING(1), HARM_DISCRIMINATIVE(2), SURPRISE(3), POSITIVE_SURPRISE(4), NEGATIVE_SURPRISE(5)]`,
and `_read_affect` already calls `evaluate_valence(z_world)` -- it just reads indices 4/5 (excite/dread)
and never index 1 (liking) or index 0 (residue-wanting). The MECH-295 liking bridge is enabled and
`update_liking()` / anticipatory-write paths populate `VALENCE_LIKING`. So liking was never absent --
it was never *surfaced*. This is a clean telemetry+viz fix (Section 7 + 8).

### 3d. Excite is inflated and cannot be trusted as an appetitive readout (MEASURES; already routed)

`excite` mean = **14.0**, max **42.7** (vs dread mean 1.0, max 2.8). Per the 906a autopsy, this is the
**SD-RESIDUE-VALENCE-BOUND** finding: `RBFLayer.update_valence()` is an unclamped `+=` with no decay,
fired every step MECH-307 split-surprise crosses threshold, so a long-lived agent revisiting the same
regions drives POSITIVE_SURPRISE unboundedly. **excite here is largely a monotonic accumulation
artifact, not a clean anticipatory-positive-valence readout** -- which contaminates any excite-based
coupling (Section 4). Already routed by the 906a autopsy as a `recommended_substrate_queue_entry`
pending `/governance` ratification; referenced here, not re-registered.

---

## 4. Temporal coupling: the central novel finding (MEASURES vary, coupling absent)

Contemporaneous and lagged Pearson correlations over all 8 segments (per-segment, so no boundary
artefacts):

| coupling tested | r | interpretation |
|---|---|---|
| dread(t) -> any harm in t+1..t+3 | **0.065** | dread does NOT anticipate harm (base harm rate 0.13) |
| z_goal(t) -> approach mode at t+1 | **0.064** | wanting does NOT precede approach |
| z_goal(t) -> any benefit in t+1..t+3 | **-0.036** | wanting does NOT predict resource acquisition |
| dread <-> z_harm_a (contemporaneous) | **0.032** | dread not tracking harm-affect even in-step |
| excite <-> benefit signal (contemporaneous) | **0.029** | excitement does NOT track appetitive events |

**Every affect->behaviour and affect->event coupling is essentially zero, while the channels
themselves are non-degenerate (they vary).** This is the sharp organism-level result: 906b has
"alive" affect telemetry that does **not** predict subsequent action or track environmental events.
The user's precise question -- *do internal-state transitions predict subsequent action rather than
merely producing non-zero telemetry?* -- answers **no, in this run.**

**This null is partly explained, not purely a REE failure, and the discrimination matters:**
- The `excite<->benefit` null is **uninterpretable** as stated -- excite is contaminated by the
  unbounded accumulator (3d). MEASURES-limited.
- The `z_goal->approach/benefit` nulls are **coupling-starved**: wanting is at floor >50% of the time
  (3a), so it has little signal to be predictive with. MECHANISM/ENVIRONMENT-limited.
- The `dread->harm` null (dread is *not* accumulator-inflated; max 2.8) is the cleanest and most
  concerning: dread varies but does not anticipate the adjacency-harm it should. This is the strongest
  candidate for a genuine **defensive-anticipation coupling gap** -- but it needs the confound-free
  re-measure in Section 6 before it is charged to REE.

---

## 5. Sleep integration (ENVIRONMENT/ARCHITECTURE gap -- confirmed, novel-to-record)

The user observed a sleep cycle near the end with REE still swimming around. **Confirmed and explained
architecturally:**

- Sleep fired once, at the boundary **before segment ep7** (`sleep_cycle_fired_before_this_segment=True`).
- ep7 then ran a normal 500-step waking segment (237 benefit, 13 harm, 132 moves, action entropy 1.98)
  -- **behaviourally indistinguishable from waking segments.**
- Code-confirmed: `SleepPhaseManager.notify_episode_end()` fires `_run_cycle()` as an **offline
  between-episode consolidation event**. A `grep` for motor-inhibition / sensory-gating / atonia /
  behavioural-quiescence across `ree_core/` returns **only PAG-freeze hits, nothing in `ree_core/sleep/`**.
  The only onset-side gate is `use_mech286_sleep_onset_gate` (orexin wake-stability), which decides
  *whether* a cycle fires, not what the organism does *during* one.

**There is no in-life "asleep" state.** Sleep is purely a consolidation pass between segments; the
organism never enters a state that gates perception or action. This is exactly why REE "keeps swimming":
architecturally there is nothing to make it stop.

### Recommended architectural requirement (for `/governance` ratification, NOT self-applied here)

**REQ-SLEEP-STATE-GATING (new).** Sleep should become a *coordinated state-dependent* condition, not
merely an internal update event. Minimum components to specify:
- **motor inhibition / behavioural quiescence** so ordinary exploratory action does not continue during sleep;
- **sensory gating / reduction** during sleep;
- an explicit statement of **which internal processes remain active** (offline E1/E2 updating /
  consolidation where architecturally intended -- the existing `_run_cycle` work is the natural
  in-state occupant);
- coupling to the existing `sleep_onset_gate` / `phase_manager` rather than a new parallel path.

**REQ-SLEEP-MEMORY-DISTINCTION (new, DEPENDENCY-GATED -- do NOT build now).** Once
autobiographical/episodic memory exists, REE should **not** encode ordinary external experience during
sleep as consciously-experienced episodic content. Preserve the distinction between offline
updating/consolidation and autobiographical experience: retain the *fact/state-transition* that sleep
occurred, plus appropriately salient awakenings/internal events, without constructing a normal waking
episodic stream for the sleeping interval. **Blocked-until:** an autobiographical/episodic memory
substrate exists (none does today -- do not pre-implement; record as a standing dependency so the
episodic-memory build inherits it).

*Relationship to existing plan:* `sleep_substrate_plan.md` GAP-2 (SD-017 retest cohort) is
upstream-blocked on the **behavioural-diversity substrate** (`arc_062_rule_apprehension:GAP-B`) --
that is about sleep *refining* waking diversity. The state-gating requirement above is **orthogonal and
new**: it is about sleep changing the organism's *behavioural state while asleep*, which no existing
node covers.

---

## 6. Freeze: zero fires is a CONFIG artifact, not REE and not incapacity (MEASURES/config)

`total_freeze_fires = 0` across 3909 eval steps with 278 harm-taking steps. **Airtight cause:** the
906b driver deliberately sets `agent.pag_freeze_gate.config.duration_input_threshold = 1e9` for the
eval ("disable the MOTOR override only ... the all-ON agent's chronic z_harm_a would otherwise
freeze-lock every step"). In `freeze_gate.py` the freeze duration counter only increments when
`z_harm_a > duration_input_threshold`; with the threshold at 1e9 and `z_harm_a` max ~few, the counter
**never** increments, so `freeze_commit = z_harm_a * duration(=0) > theta_freeze` is never true and
`freeze_active` can **never** become True.

So freeze was **incapable of activating under the observational configuration, by design** -- NOT
"available but never selected," and NOT a substrate incapacity. **Consequence:** whether REE would
*appropriately* select freeze (vs the chronic-saturation freeze-lock the relaxation was papering over)
is **untested by this run.** That is a real open question, addressed in Section 7's successor proposal,
not a failure to charge to REE.

---

## 7. Four-layer failure-location summary

| Observation | REE FAILED | MECHANISM FAILED | MEASURES FAILED | ENVIRONMENT FAILED | Net classification |
|---|---|---|---|---|---|
| Behavioural diversity exists | -- | -- | -- | -- | REE: diversity present (in-mode, not in-space) |
| Food-seeking weak | partial | partial (wanting seeding sparse) | partial (coarse benefit signal conflates reef/proximity with consumption) | partial (diffuse benefit field, non-respawn) | **MIXED** -- not chargeable to REE alone |
| Harm-avoidance imperfect | slight | -- | -- | -- (env fix working) | REE: competent-imperfect |
| Wanting rises little | -- | yes (sparse contact seeding) | -- | yes (few consummatory events) | MECHANISM+ENVIRONMENT |
| Vigor flat 0.0 | -- | **yes** (known v_raw sign/scale, V3-EXQ-563) | no (real zero, not missing key) | -- | MECHANISM (already tracked) |
| Liking not shown | -- | -- | **yes** (never surfaced; signal exists) | -- | MEASURES (fixable) |
| Excite huge/decoupled | -- | yes (unbounded accumulator) | yes (channel contaminated) | -- | MECHANISM+MEASURES (already routed: SD-RESIDUE-VALENCE-BOUND) |
| Affect->behaviour decoupled | **candidate** | candidate | partly (excite contaminated) | partly (wanting-starved) | **MIXED/UNCERTAIN -- needs confound-free re-measure** |
| Sleep = continued swimming | -- | -- | -- | **yes** (no in-life sleep state exists) | ARCHITECTURE gap (new requirement) |
| Freeze 0 fires | -- | -- | **yes** (config disabled it) | -- | MEASURES/config artifact |

No observation is cleanly and solely "REE FAILED." The strongest REE-candidate (affect->behaviour
decoupling) is exactly the one most confounded by known measurement defects, which is why the
successor below prioritises removing those confounds before charging REE.

---

## 8. Already-tracked vs novel (dedup)

**Already tracked -- reference, do NOT re-register:**
- Survivability radius fix -- done (906b itself).
- `SD-RESIDUE-VALENCE-BOUND` (excite inflation) -- routed by 906a autopsy, pending `/governance`.
- Vigor `v_raw` sign/scale -- V3-EXQ-563 family + `TonicVigorConfig.v_t_floor` diagnostic.
- SD-017 sleep *refinement* retest cohort -- `sleep_substrate_plan.md` GAP-2 (blocked on GAP-B diversity substrate).

**Genuinely novel (recorded here):**
1. Affect->behaviour temporal decoupling as a first-class organism-level result (Section 4).
2. Food signal != discrete-resource acquisition (proximity/reef exploitation) (Section 2b).
3. Sleep has no in-life behavioural-state gating -> REQ-SLEEP-STATE-GATING (Section 5).
4. Autobiographical-memory-vs-consolidation distinction -> REQ-SLEEP-MEMORY-DISTINCTION (dependency-gated).
5. Liking present in substrate but never surfaced to telemetry/viz (Sections 3c, 9).

**Queue state:** `experiment_queue.json` has 1 unrelated item (V3-EXQ-324d). No 906c / successor is
queued -- no duplication risk.

---

## 9. Proposed successors (for `/queue-experiment`; NOT queued here -- mandatory-skill-path)

1. **V3-EXQ-906c -- appetitive-sequence + coupling instrumentation.** Same ecology, but (a) emit
   `liking` (VALENCE_LIKING) and residue-`wanting` (VALENCE_WANTING) per step from `_read_affect` so
   the full sequence food-perception -> approach -> consumption -> liking -> wanting -> next-behaviour
   is inspectable; (b) add affect->behaviour lagged-coupling metrics as first-class manifest fields
   (the Section 4 correlations, computed in-run); (c) hold excite interpretation pending
   SD-RESIDUE-VALENCE-BOUND, or run *after* it lands so excite is trustworthy. This is the direct
   enabler for the viz work in Section 10.
2. **V3-EXQ-906d -- defensive-availability probe.** Re-enable the PAG freeze motor override
   (`duration_input_threshold` at its real value) under a *calmed* harm regime (so chronic z_harm_a
   does not freeze-lock), to test whether freeze is *appropriately* selected around adjacency-harm
   -- the question Section 6 shows 906b cannot answer. Pair with the `dread->harm` coupling metric.
3. **Ecology enrichment for food-seeking (design note, lower priority).** If discrete-resource
   acquisition is the competency of interest, the diffuse-benefit-field confound (Section 2b) must be
   reduced (e.g. `resource_respawn_on_consume=True` and/or a sharper resource-vs-ambient benefit
   contrast) so that "food-seeking" measures navigation-to-resource rather than gradient-sitting.

These are proposals; authoring goes through `/queue-experiment`. Follow-on chip recorded.

---

## 10. Visualisation change made this session (`fishtank_viz.html`)

- Added a **liking** bar to the Affect panel's Drive & wanting group, auto-scaled and **graceful**
  (hidden when the `liking` field is absent, e.g. for 906b's own log, which predates the 906c
  telemetry emission). This makes the appetitive sequence inspectable as soon as 906c emits liking.
- Made the bipolar valence meter scale excite and dread on **independent** maxima so the inflated
  excite (Section 3d) no longer visually crushes dread to zero width.
- Wanting continues to auto-scale to its own per-episode max (already the case), which is the correct
  way to make its small but real variation visible.

These are visualisation-only (REE_assembly); no experiment code or queue entry is touched here.

---

## 11. Follow-up (2026-08-09T17:34Z user steer): diversity harvest + the freeze/orienting gap

Two user observations on the review above, each investigated against code/claims before acting.

### 11a. "This trace shows plenty of diversity -- harvest any claims." Two DIFFERENT quantities are being conflated, and the harvest is a convergence, not an unblock.

The word "diversity" names two unrelated things here, and the distinction is load-bearing:

- **906b behavioural diversity = a MEASURE, observer-applied, non-converting.** The "6 modes" are not a substrate control state -- `mode` is produced by `_classify_mode(z_harm_norm, world_change_norm, harm_signal, in_reef, freeze, z_block_assert)` (v3_exq_664), a post-hoc classifier with fixed precedence `freeze>assert>shelter>avoid>approach>explore>neutral` over thresholded telemetry. So "mode diversity" largely re-expresses affect-channel + position variation through a bucketer. It is real *behavioural-repertoire/exploration* variety, but it is exactly the kind that Section 4 showed does **not** convert into committed, state-appropriate action.

- **The sleep GAP-2 blocker's "diversity" = committed-class-entropy under a TRAINED policy.** `sleep_substrate:GAP-2` is `depends_on: arc_062_rule_apprehension:GAP-B`, whose closure gate is a **C2 committed-class-entropy lift** -- does a rule-creator's differentiated `rule_state` move *which action class the trained CEM/GatedPolicy commits to*. The whole 654->654j / 569i / 689a / MECH-448-449 lineage established the blocker is the **MECH-439 F-dominance conversion ceiling**: "the matured+active+differentiated rule_state reaches committed action but cannot move the F-dominated committed argmax." And `reconcile_2026_07_09` (failure_autopsy_V3-EXQ-719a) reframed it as a **behavioural-COMPETENCE / training-regime ceiling** ("first direct competence measurement of the integrated all-ON agent: forages 0.065/0.0/0.455 resources/ep, below the 1.0 floor on 0/3 seeds; diffuse state-blind commitment, NOT literal monomodal collapse").

So the fishtank's mode diversity does **not** unblock sleep GAP-2: sleep-refinement needs *converting* diversity to refine, and the fishtank shows the *non-converting* kind. Increasing repertoire diversity further is not the lever.

**But there IS a genuine harvest, and it is a convergence the review above missed:** the Section-4 temporal-decoupling finding is the **same phenomenon as the MECH-439 conversion ceiling / 719a competence-wall, observed at the organism level, in a fresh substrate (the all-ON fishtank) via a fresh instrument (affect->behaviour coupling).** Two independent corroborations, not restatements:
- **Competence**: 719a measured the all-ON agent foraging 0.065/0.0/0.455 resources/ep (below the 1.0 floor); 906b independently reproduces exactly that shape (11 consummatory events / 3909 steps; food-seeking is diffuse-gradient sitting, not committed acquisition -- Section 2b).
- **Conversion/decoupling**: 719a's "diffuse state-blind commitment" (internal state present, does not steer the committed argmax) is precisely 906b's "affect channels vary but do not predict subsequent action" (Section 4, all couplings ~0).

This is worth recording as a **corroborating behavioural channel** for the MECH-439 F-dominance / competence-wall lineage (which already counts CRF/OFC/dACC/temperature channels) -- but 906b is single-seed, all-ON, `claim_ids=[]`, so it **cannot score** MECH-439/ARC-062/MECH-309; it is observational corroboration + a sharpening of where to push, for `/governance` to weigh, not a scoring move made here.

**One `complex (probe-gated)` empirical discrimination the fishtank newly makes cheap** (nobody has run it -- the fishtank showcase is new): the two sleep-refinement experiments that returned bit-identical waking-vs-sleep metrics (V3-EXQ-418l / 436a) ran on the *collapsed monomodal trained-policy* substrate whose "waking phase produces no behavioural variation for sleep to refine" (GAP-2 `upstream_block_reason`). The **fishtank all-ON substrate does have visible waking behavioural variation.** So: *does the sleep-refinement DV (slot/mode diversity) register a non-null waking->sleep difference on the fishtank substrate?* Expected answer given the above is **no** (the variation is the non-converting kind), which would *confirm* the block is about conversion not repertoire -- but it is untested, and either result is informative. This is a candidate targeted probe, not an unblock claim.

### 11b. "Give the fish a fright, freeze, reorient, then approach/withdraw." Correct, and the chain is essentially UNBUILT -- `complicated (buildable)`, and it is the substrate answer to Section 4's decoupling.

Investigated against the substrate:
- **Freeze is suffering-driven, not threat-anticipation-driven.** `pag/freeze_gate.py`: `freeze_commit = (z_harm_a * duration_above_threshold) > theta_freeze`, i.e. freeze fires on *accumulated harm/suffering* sustained over ticks -- it responds to harm being *experienced*, not to *noticing approaching danger*. (This is also why disabling it via `duration_input_threshold=1e9` in 906b was necessary -- Section 6.)
- **There is no orienting / startle / reorienting mechanism at all.** A tree-wide grep for `orient|reorient|startle|fright` across `ree-v3/ree_core/` returns nothing (one incidental `broadcast_override.py` string). The approach/avoid/freeze "modes" are the post-hoc classifier of 11a, not a substrate detect->orient->decide chain.
- **Consequence:** the fright->freeze->reorient->approach/withdraw chain the user describes is genuinely absent. Building it is exactly the mechanism that would create the coupling Section 4 found missing: dread does not anticipate harm (r=0.065) precisely because no anticipatory-threat -> defensive-response pathway is wired.

**Proposed substrate design (for `/implement-substrate`; candidate new mechanism -- defensive orienting response):**
1. **The "fright" is EPISTEMIC, not nociceptive (user, 2026-08-09T17:40Z -- corrects an earlier draft of this step).** Freeze must fire on *a signal that suffering COULD accrue -- anything sudden, unexpected, that REE does not yet know what it is* -- NOT on accrued harm (`z_harm_a`, the current gate) and NOT on nociceptive proximity to a *known* hazard. The right substrate input already exists and is not the harm channel: **`VALENCE_SURPRISE` (residue index 3), defined in `residue/field.py` as "prediction error magnitude (novelty / unexpectedness)"** -- the UNSIGNED surprise, deliberately distinct from `VALENCE_POSITIVE_SURPRISE`/`VALENCE_NEGATIVE_SURPRISE` (indices 4/5 = excite/dread, which are already *valenced* as good/bad). The trigger is a **phasic spike in unsigned surprise with the stimulus not-yet-identified** (high prediction error + low recognition confidence) -- i.e. pre-valence: before REE knows whether the unexpected thing is threat, resource, or nothing. This is the Sokolov orienting-reflex shape (freeze-to-the-unexpected), and it is precautionary precisely because the unknown *could* be harmful. NOTE two telemetry facts: `_read_affect` surfaces indices 4/5 but NOT index 3, so this exact signal is computed every step and never surfaced (same gap as liking, Section 3c); and the phasic/onset character matters -- it is the sudden *rise* in surprise, not a standing surprise level, so the trigger is a positive derivative / novelty-onset detector on index 3, gated by low identification confidence.
2. **Phasic freeze (orienting arrest) -- held until epistemic sufficiency, not a timer.** Distinct from the chronic `z_harm_a` suffering-lock: locomotor halt on the surprise-onset, *not* gated on accumulated suffering. Duration is open-ended while the unknown remains unidentified -- this is not a fixed short pulse that auto-expires.
3. **Orienting reflex = the pathway BACK TO PLANNED ACTION (user, 2026-08-09T17:43Z -- elevates this from "missing bridge" to load-bearing).** Currently nonexistent. Because the trigger is pre-valence ("does not know what it is"), freeze buys time to *turn toward and attend to* the unexpected stimulus so the surprise RESOLVES into an identification -- unsigned surprise (index 3) collapses as the stimulus becomes recognised, and signed valence (excite index 4 / dread index 5) is what it collapses INTO. That resolution is what makes the freeze-override (step 4) possible, and override is what returns control to ordinary action selection / planned behaviour. **Without orienting, freeze has no epistemic exit -- the organism cannot get back to planned action.** So orienting is not an optional attentional flourish on top of freeze; it is the mechanism that closes the surprise loop. This is why the user flagged "we may need to push more on implementation" of reorienting -- it is the critical piece of the full chain, not a secondary polish.
4. **Freeze override = "knows enough to decide action" (user, 2026-08-09T17:42Z).** The freeze is *released* (overridden) when identification confidence crosses a sufficiency threshold -- i.e. when REE has figured out enough about the unexpected stimulus that an action decision is warranted -- NOT when a clock expires and NOT when suffering drops. Release and action selection are the same moment: override unlocks the committed action that the now-resolved valence supports.
5. **Action decision (approach / withdraw / resume) -- driven by the RESOLVED valence, gated by the override.** Once override fires (step 4), the now-assigned valence decides: dread (index 5) -> withdraw, excite (index 4) -> approach, neither -> resume prior behaviour. Full pipeline: **surprise/novelty -> freeze -> orient/identify -> (knows enough) override releases freeze -> valence-gated approach|withdraw|resume**. The known-hazard proximity signal (`z_harm_s` / hazard-field gradient) is NOT the freeze trigger; it is at most one input to the *post-identification* withdraw decision. (Distinct from the existing orexin `override` channel -- that is a different mechanism; this is freeze-release on epistemic sufficiency.)

This is substantial (a new ree_core pathway + likely a new MECH claim), not a knob change. It should be built via `/implement-substrate`, then its coupling validated -- which also subsumes the review's proposed **V3-EXQ-906d** (defensive-availability probe): 906d tested whether the *existing* suffering-driven freeze is appropriately selected; the real answer is that the *anticipatory* defensive chain does not exist yet and needs building first.

### 11e. Post-orient action menu: fight / flight / freeze / fawn -- and recruit ≠ fawn (user, 2026-08-09T17:46Z; RECORD for later)

After fright -> fast interrupt -> orient, humans sometimes branch into the familiar defensive set **fight / flight / freeze / fawn**. Step 5 above only named approach / withdraw / resume -- a solo-organism subset. The fuller post-identification menu, for when social substrate exists:

| Branch | Function | REE mapping (provisional) |
|--------|----------|---------------------------|
| **Freeze (hold)** | buy time while unknown / still insufficiently identified | steps 2-4 (phasic freeze until epistemic sufficiency) |
| **Flight** | withdraw from identified threat | dread -> withdraw (step 5) |
| **Fight** | approach-as-defense / confront | not yet in the 11b chain; later defensive-approach under resolved threat |
| **Fawn** | *appease the threat source* (submit, placate, stay attached to aggressor to reduce harm) | closer to loveability/repair failure modes (punishment-avoidance appeasement) than to calling for help; see loveability plans |
| **Recruit / distress call** | *seek others* -- fast broadcast that something is wrong and allies/caregivers should come | **NOT fawn** |

**Scream / cry / distress vocalization is usually recruit, not fawn.** Fawn targets the threat; recruit targets conspecifics. Ethology: infant distress cry, alarm call. Psychology: closer to attachment proximity-seeking / tend-and-befriend than to the "fawn" slot in the 4F list. REE already has a functional hypothesis in `docs/architecture/social.md` (affective expression as safety mechanism: extreme expression can **trigger assistance, e.g. distress calls**) -- not built, not anatomical.

**Status:** record-only architectural note for later. The current fishtank has no "other," so recruit is gated on multi-agent / social partners. Do **not** fold recruit into the first `/implement-substrate` defensive-orienting increment (11d), and do **not** mis-label it as fawn when social defense is eventually designed. Keep **recruit** and **fawn** as distinct branches of the post-orient menu.

### 11c. Routing (proposed; skill-gated -- not executed here)
- **Harvest (11a):** record the decoupling<->conversion/competence-ceiling convergence against the MECH-439 / competence-wall lineage via `/governance` (observational corroboration, not a scoring move); it does not touch the sleep block.
- **Probe (11a):** optional `/queue-experiment` -- run the sleep-refinement DV on the fishtank substrate to settle repertoire-vs-conversion empirically.
- **Build (11b):** `/implement-substrate` the surprise->freeze->reorient->epistemic-override->approach/withdraw defensive-orienting pathway (+ candidate MECH registration), which supersedes the 906d probe proposal.
- **Later (11e):** when social partners exist, design post-orient **recruit / distress-call** as distinct from **fawn**; do not start that in the 11b increment.

### 11d. Build directive + status (user, 2026-08-09T17:40Z)
**RECORD-ONLY this session -- the build is NOT started here; it is to be picked up in a dedicated `/implement-substrate` session.** User steer on ambition when it is: **build the FULL chain (surprise/novelty fright -> phasic freeze held until identified -> orienting reflex -> epistemic-sufficiency freeze-override -> valence-gated approach/withdraw / return to planned action) "as ambitiously as is possible given what we know" -- do NOT scope down to a minimal fright+withdraw increment, and do NOT treat orienting as optional.** Orienting is load-bearing: it is how freeze ends and planned action resumes. So the dedicated session should treat all five components of 11b as the first increment (with orienting as a first-class sub-build, not a deferred follow-on), register the candidate defensive-orienting MECH, and validate against the Section-4 coupling nulls (the pass criterion is that the built chain moves surprise-onset->freeze and post-identification dread->withdraw / excite->approach couplings off ~0 -- i.e. it converts unresolved novelty into arrest, then resolved valence into state-appropriate action and return to planned behaviour; the organism-level counterpart to lifting the MECH-439 conversion ceiling). The harvest (11a/11c) and the sleep-substrate probe remain available but are not blockers on the build.

---

## 12. Continued data-mining of the raw 906b episode log (2026-08-09T17:55Z follow-on, user-directed)

Deeper pass over the per-step episode log (`..._episode_log.json`, 3909 steps / 8 segments) using fields
logged but not yet inspected in Sections 1-6: `is_committed`, `residue_surprise`, `residue_write_fired`,
`beta_elevated`, `action_blocked`, `limb_damage_injected`, `external_hazard_injected`,
`world_rule_shift_occurred`, `transition_type`, raw `action`. All findings below read data already
collected by the 906b run -- no new experiment.

### 12a. `is_committed` = 0/3909 -- a direct, already-logged corroboration of the non-committed reading, sharper than the 11a mode-diversity proxy

`is_committed` (`e3_selector.get_commitment_state()`, consumed at `agent.py:11351`) reflects the CORE
trajectory-latch commitment mechanism: `committed = running_variance < commit_threshold`
(`e3_selector.py:15`, `3143`-`3149`), True whenever `_committed_trajectory` (or the closure-exclusive
`_closure_committed_trajectory`) is non-None for that tick. This is read from the main `select(...)` path,
not a niche or off-by-default lever, and it is **never True across all 3909 steps of this run**.

This is a cheaper and more direct organism-level signal than 11a's mode-diversity harvest: `mode` is a
post-hoc classifier over telemetry (`_classify_mode`), whereas `is_committed` is the substrate's own
commitment flag, read from the exact mechanism the MECH-439/GAP-B lineage names (`committed_now` /
`_committed_trajectory`). A clean 0/3909 on the all-ON fishtank is a second, independent corroboration of
"diffuse, non-committed selection," obtained from data already collected.

**Caveat, same as 11a:** single-seed, all-ON, `claim_ids=[]` -- observational, non-scoring. This pass also
does not have `running_variance` / `commit_threshold` themselves in the per-step log, so it cannot
distinguish "structurally far from the commit threshold" from "chronically just short of it" -- that needs
a telemetry addition (13d) or a targeted probe, not a re-read of what's already logged.

### 12b. `residue_surprise` (VALENCE_SURPRISE, unsigned) -- distribution, plus a real, small, INCIDENTAL startle-like coupling that already exists with no orienting mechanism built

Full-run distribution (3909 steps): min 0.0, p50 0.0 (floor >50% of the time, same shape as `z_goal`),
p90 0.040, p95 0.084, p99 0.233, max 0.478, mean 0.014. This gives a first empirical anchor for calibrating
the "phasic spike" onset threshold the 11b design needs (11b step 1) instead of picking one blind.

Using the p90 cutoff (>=0.040) as a naive spike proxy and testing the exact coupling 11b's build is meant
to create -- **surprise-spike(t) -> behaviour-change(t+1), within-episode only (no cross-boundary lag)**:

| | P(mode change @ t+1) | P(moved @ t+1) |
|---|---|---|
| surprise-spike @ t (n=391) | 15.4% | **44.3%** |
| no spike @ t (n=3510) | 11.1% | 24.0% |

Movement-onset is elevated ~1.85x following a surprise spike (44.3% vs 24.0%); mode-change ~1.4x (15.4% vs
11.1%). **Novel-to-record: an incidental startle-like coupling already exists in the substrate without any
purpose-built orienting mechanism** -- `residue_surprise` genuinely drives *something* downstream, but
diffusely (not a clean binary freeze-then-resolve), which is exactly the gap the 11b design closes. This
also gives 11b's validation step a concrete pre-registered baseline to beat: the built chain should push
this well past 44%/15% toward a sharp, deterministic surprise->arrest->resolve->act signature, not merely
reproduce the incidental correlation already present.

`residue_write_fired` correlates r=0.54 with `residue_surprise` contemporaneously (mean surprise 0.054 when
a write fires vs 0.0 when it doesn't; fire-rate 1005/3909 = 25.7%) -- confirms the write-gate is a
surprise-triggered mechanism, a sanity check rather than a new finding.

`residue_surprise` anti-correlates weakly with both `dread` (r=-0.12) and `excite` (r=-0.12)
contemporaneously -- consistent with (not proof of) the 11b framing that unsigned surprise is highest
*before* a stimulus is identified and falls as it resolves into signed valence. Worth re-testing once a
future run emits `residue_surprise` alongside a per-step identification-confidence proxy, which does not
currently exist in telemetry.

### 12c. Rare-event and blocked-action bookkeeping (scope note, not a new finding)

`transition_type` tally across 3909 steps: `benefit_approach` 1384, `none` 1934, `hazard_approach` 258,
`action_blocked` 152, `reef_entry`/`reef_exit` 56/56, `resource` 11, `env_caused_hazard` 21,
`world_rule_shift` 14, `external_hazard` 8, `limb_damage` 15. `beta_elevated` is True on 100% of steps
(3909/3909) -- flagged for a future pass (chronically saturated by the all-ON config, or the expected tonic
state? not investigated here). Stress-injection events (`limb_damage_injected` 28/3909 = 0.7%,
`external_hazard_injected` 31/3909 = 0.8%, `world_rule_shift_occurred` 15/3909 = 0.4%) are rare but
non-zero -- this eval config does exercise the rare-event/perturbation paths at least a little, not a null
config. `action_blocked` fires on 3.9% of steps (152/3909), matching the `transition_type='action_blocked'`
count exactly (consistency check, no discrepancy found).

### 12d. The one sleep cycle that fired: `sws_slot_diversity`~0, zero replay draws -- a concrete, n=1 preview consistent with 11a's "expected null" prediction

`ep7.sleep_cycle_detail` (the only sleep-firing episode in this run, before segment ep7 -- Section 5):
`sws_n_writes=5.0`, but `replay_diversity_index=-1.0` -- the phase-manager's own sentinel for **zero SWS
replay draws this cycle** (`phase_manager.py:517-530`: `-1.0` when `_n_draws==0`), despite 5 writes having
occurred. `sws_slot_diversity=0.0021` (effectively zero). `post_sleep_z_goal_before` =
`post_sleep_z_goal_after` = 1.81e-8 (both at floor; `post_sleep_z_goal_retention=1.0` only because both
sides are ~0 -- nothing was there to retain, consistent with 3a's z_goal-at-floor finding).
`rem_wanting_spread_n_steps=0.0`, `rem_n_reverse=0.0` -- REM's wanting-spread mechanism did nothing this
cycle. `rem_n_rollouts=10.0` did run (`rem_mean_harm_terrain=25.2`, `rem_terrain_variance=93.2` -- REM
terrain rollouts happened and varied); it is specifically the SWS replay-diversity and REM wanting-spread
channels that read empty.

**This is a concrete, already-collected preview consistent with 11a's "expected null" for track C** (does
the sleep-refinement DV register a non-null waking->sleep difference on this substrate?): on this one
firing, it does not -- writes happened but nothing was drawn/replayed, and the wanting channel had nothing
to spread because it was already at floor going in. **Caveat: n=1** -- a single sleep cycle in a
single-seed run is not a substitute for track C's proper probe (which should test across multiple
firings/seeds and report `sws_slot_diversity` / `replay_diversity_index` as first-class metrics, which this
ad-hoc read confirms are already computed and logged per-cycle, just not yet surfaced in a manifest summary
-- another small telemetry candidate for 13d). Recorded as informative context for track C, not as
resolving it.

### 12e. Directional environmental organisation -- movement direction is UNCORRELATED with the nearest resource/hazard even in the modes classified as steering toward/away from them (2026-08-09T18:06Z, answering the original brief's unaddressed "does behaviour become appropriately organised around environmental information?")

The original review brief asked this explicitly and it was not directly tested in Sections 1-11: not "does the agent end up closer to a resource" (Section 2b: no) but **does the agent's per-step movement DIRECTION point toward/away from the nearest mapped resource/hazard**, using `hazards`/`resources` (the driver's `current_hazards`/`current_resources`, ground-truth positions, confirmed at `v3_exq_906b_full_stack_observational_fishtank.py:661-663`) against `pos(t+1)-pos(t)`, restricted to steps that actually moved:

| mode (at step t) | tested alignment | n | mean cosine | frac aligned (cos>0) | frac opposed (cos<0) |
|---|---|---|---|---|---|
| `approach` | move-vector . vector-to-nearest-resource | 291 | **0.019** | 44.3% | 41.9% |
| `avoid` | move-vector . vector-away-from-nearest-hazard | 64 | **-0.053** | 39.1% | 42.2% |
| `neutral` (control) | move-vector . vector-to-nearest-resource | 43 | 0.180 | 44.2% | 18.6% |
| `neutral` (control) | move-vector . vector-away-from-nearest-hazard | 42 | -0.308 | 14.3% | 52.4% |

**Both classified modes are essentially uncorrelated with the nearest-entity direction they are named for** -- `approach` mean cosine 0.019 (chance is 0), `avoid` mean cosine -0.053 (chance is 0; the sign is even backwards from "away"). This directly answers the brief's question: **no, movement is not organised around the nearest discrete resource/hazard's position**, consistent with (and sharper than) Section 2b's distance-based finding -- `approach`/`avoid` as classified by `_classify_mode` track affect-channel thresholds (`z_harm_norm`, `world_change_norm`, `harm_signal`, `in_reef`), not literal navigation toward/away from a specific mapped entity. This is consistent with the ambient/reef-proximity-field explanation already established in 2b/3a: the diffuse field that drives behaviour has no privileged direction toward any one discrete resource, so "approach" in the classifier's sense need not point at anything in particular.

**Counter-intuitive nuance, flagged rather than smoothed over:** the `neutral`-mode control shows STRONGER hazard-avoidance alignment (-0.308, 52.4% opposed) than `avoid` mode itself (-0.053, 42.2% opposed) -- ordinary unclassified movement happens to point away from the nearest hazard more reliably than movement during steps the classifier labels `avoid`. Caveat: small n (42 vs 64), single-seed -- this is suggestive, not decisive, but it is consistent with `avoid` mode often being a stationary defensive posture (elevated harm/shelter-adjacent telemetry) rather than active directional fleeing, which would explain why its own movement (on the minority of `avoid` steps that move at all) is no more oriented than chance.

**Failure-location:** MIXED, same shape as 2b/4 -- not chargeable to REE alone. The classifier (MEASURES) names modes after a directional concept the underlying telemetry thresholds don't test; the diffuse benefit/hazard field (ENVIRONMENT) gives no discrete direction to organise around; and the substrate's own selection (MECHANISM, `is_committed`=0/3909 per 12a) is not steering toward any single latched target. This strengthens the case for track A (13-A): a defensive-orienting mechanism keyed to a specific identified stimulus (not a diffuse field) is exactly the kind of directed target the current substrate lacks.

### 12f. Cross-episode trajectory diversity -- genuine, not a fixed home base (answering the original brief's "trajectory diversity" ask)

Per-episode unique-cell counts (Section 1) show within-episode diversity; this checks the complementary question -- does the SAME region get revisited every episode, or does trajectory vary across episodes? Per-episode visited-cell sets, all 8 episodes:

- Per-episode unique cells: 39, 28, 30, 30, 24, 23, 35, 18 (of 144).
- Pairwise Jaccard overlap across all C(8,2)=28 episode pairs: mean **0.197**, range 0.000-0.516 -- episodes overlap only modestly on average, and some pairs share almost nothing.
- Union of cells visited across all 8 episodes: **97/144 = 67.4%** of the grid -- far broader than any single episode's 12.5-27.1%.
- Cells visited in literally every one of the 8 episodes (a fixed "home base" signature): **0**.

**Genuine cross-episode trajectory diversity, not a repeated favourite corner.** Collectively the agent covers two-thirds of the grid over 8 episodes with no single cell common to all of them, even though each individual episode is spatially narrow (Section 1). Read together with 12e: the agent explores broadly and variably across episodes, but within any one episode/step its direction of travel is not organised around the nearest discrete resource/hazard -- diversity-in-aggregate coexists with the absence of local directional organisation.

### 12g. "Does harm respond and decay appropriately?" -- YES for the normalised channel, NO for the accumulated one, and the split explains Section 6's freeze finding (2026-08-09T18:1xZ, answering another unaddressed brief item)

Event-triggered average (steps -2..+12 around every `harm_event=True` step, within-episode, 278 events) for
the two distinct harm channels logged per step:

| channel | t-2 | t+0 (event) | t+1 (peak) | t+6 | t+12 | shape |
|---|---|---|---|---|---|---|
| `z_harm_norm` / `z_harm_s` (identical distributions) | 0.2240 | 0.2297 | **0.2302 (peak)** | 0.2162 | 0.2072 | clean phasic rise-then-decay |
| `z_harm_a` | 2.4599 | 2.4794 | 2.4863 | 2.5056 | 2.5406 (still rising) | flat/chronically elevated, no event-locked transient |

**`z_harm_norm` (= `z_harm_s`, confirmed identical min/p10/p50/p90/max across the full 3909-step
distribution -- likely the same signal under two field names) genuinely rises around a harm event, peaks
1 step later, and decays smoothly over the next ~10+ steps back toward baseline -- a textbook appropriate
phasic harm response.** This directly answers the original brief's "does harm respond and decay
appropriately?" with **yes**, for this channel.

**`z_harm_a` shows no such structure in the same window** -- it drifts slowly upward throughout (2.46 ->
2.54) with no visible peak-and-decay tied to individual events, consistent with its full-run distribution
being chronically mid-to-high (p10=0.44, p50=2.88, p90=4.17, mean=2.51) rather than resting near a floor
between events. This is not a new defect -- **it corroborates, from independent data, the mechanism Section
6 already inferred**: the 906b driver disables the freeze *duration* threshold specifically because "the
all-ON agent's chronic z_harm_a would otherwise freeze-lock every step" (Section 6). The event-triggered
curve shows directly why: `z_harm_a` does not return to a low resting level between harm events at this
hazard density (45.6% of steps within Manhattan distance <=2 of a hazard, Section 2a), so it has no clean
phasic profile to gate a duration-based freeze trigger on.

**Consequence for 13-A:** freeze/vigor (Section 3b) both read from `z_harm_a`, the chronic/non-phasic
channel, while `z_harm_norm` -- sitting right next to it in the same telemetry -- shows the clean phasic
shape a trigger mechanism would actually want. The 11b design already avoids this by keying the new
defensive-orienting trigger to `residue_surprise` (index 3) rather than any `z_harm_*` channel (Section
11b step 1); this finding is corroborating evidence that channel choice was the right call, not a reason to
revisit it.

### 12h. Ground-truth injected-event response -- `residue_surprise` does NOT reliably fire on the paradigm cases it is meant to catch; the 12b threshold under-catches them. FLAG FOR TRACK A BEFORE BUILDING (2026-08-09T18:1xZ)

12b calibrated a candidate surprise-spike threshold (p90=0.040) from the OVERALL step distribution. This
checks it against the one thing that matters more than the overall distribution: does `residue_surprise`
actually respond to the three kinds of ground-truth "sudden, unexpected, could-be-harmful" event the
environment genuinely injects (`limb_damage_injected`, `external_hazard_injected`,
`world_rule_shift_occurred`) -- exactly the paradigm cases 11b's design describes. Event-triggered
averages (window t-1..t+4, within-episode):

| event | n | `residue_surprise` @t+0 | vs global mean (0.0139) | mode-change rate @t+0/t+1 | vs global (0.115) |
|---|---|---|---|---|---|
| `limb_damage_injected` | 28 | 0.0054 | **below baseline** | 0.214 / 0.071 | ~1.9x / ~0.6x |
| `external_hazard_injected` | 31 | 0.0239 | ~1.7x, but still **below the 0.040 p90 threshold** | 0.258 / 0.290 | ~2.2x / ~2.5x |
| `world_rule_shift_occurred` | 15 | 0.0072 | below baseline | 0.000 / 0.077 | 0x / ~0.7x (delayed rise by t+3) |

**`residue_surprise` does not spike on `limb_damage_injected` or `world_rule_shift_occurred` at all, and its
average response to `external_hazard_injected` (0.024) sits BELOW the p90=0.040 threshold 12b proposed as a
candidate spike cutoff.** A trigger built to fire on `residue_surprise > p90` would therefore likely MISS
the majority of `external_hazard_injected` events and essentially all `limb_damage_injected` /
`world_rule_shift_occurred` events -- exactly the events the defensive-orienting mechanism exists to catch.

**This is not simply "nothing happens" -- other channels DO respond, just not the one 11b proposes to key
off:**
- `mode` changes at an elevated rate right at `limb_damage_injected` (21.4% vs 11.5% baseline, ~1.9x) and
  for two steps around `external_hazard_injected` (25.8%/29.0% vs 11.5%, ~2.2-2.5x) -- a real behavioural
  response exists, it is just not visible in `residue_surprise`.
- `dread`/`excite` show modest, mostly-delayed rises for `external_hazard_injected` (+9%/+9% by t+1) and
  `world_rule_shift_occurred` (+21%/+23% by t+1) -- i.e. valence does shift, on a slower timescale than a
  single-step spike.
- `z_harm_a` does not spike either (consistent with 12g: it is the chronic, non-phasic channel).

**Reading, per the four-layer framework:** MEASURES/design-choice issue, not a REE failure -- the substrate
clearly registers SOMETHING (mode-change, delayed dread/excite) around at least 2 of 3 injected event types,
but the specific channel (`residue_surprise`) and threshold (statistical p90 of the overall distribution)
proposed in 11b/12b as the trigger for the defensive-orienting chain would under-fire on the very events it
is meant to catch. Small-n caveat throughout (15-31 events, single seed) -- this is a real risk signal, not
a definitive refutation of the surprise-based design.

**Action for track A (13-A), stated explicitly rather than left implicit:** before committing to
`residue_surprise > p90(0.040)` as the trigger condition, the `/implement-substrate` session should
re-derive the threshold (or reconsider the trigger channel/combination) against ground-truth injected events
specifically, not only the overall step distribution -- e.g. lower the threshold, use a per-episode-relative
spike (derivative against a rolling baseline, as 11b step 1 already specifies -- "positive derivative /
novelty-onset detector", which this analysis did not implement; a same-step absolute-value spike test may be
systematically less sensitive than the derivative-based onset detector the design actually calls for) or
combine `residue_surprise` with the `mode`-change signal, which responds more reliably. This changes the
build's calibration step, not its architecture -- steps 2-5 of 11b (freeze, orienting, override,
action-decision) are unaffected.

### 12i. Remaining channel profiling (brief; nothing else load-bearing found)

- **`footprint_at_cell`** (per-cell visit counter, `causal_grid_world.py:2623`/`3151`): median 11, p90 33,
  max 77 across 3909 steps -- cells that get visited get REVISITED many times, reinforcing the
  diversity-in-place-not-space reading (Section 1, 12f): the agent doesn't merely stay in a small area, it
  returns to the same handful of cells repeatedly.
- **`override`** (orexin wake-stability channel, continuous 0-1, not boolean): cold-starts near 0 at the
  very first step of the whole run (`ep0` step 0 = 0.031), rises to a ~0.69-0.76 plateau within episode 0,
  and STAYS at that plateau for the remaining 7 episodes (each episode starts near where the previous one
  ended) -- no visible decline toward a sleep-permissive low value before the one sleep cycle that fires
  (`ep7` starts at 0.729, unremarkable relative to `ep1`-`ep6`). So whatever drives the single sleep onset
  in this run, it is not a visible slow decline in `override` -- consistent with Section 5's finding that
  `use_mech286_sleep_onset_gate` decides *whether* a cycle fires from state not captured by this channel
  alone.
- **`drive`, `z_self_norm`, `z_world_norm`, `z_block`**: all within sensible bounded ranges, nothing
  anomalous (`drive` p50=0.327, `z_self_norm` p50=0.632, `z_world_norm` p50=1.350, `z_block` at floor
  >50% of the time then rising to 0.80-0.94 in the top decile, consistent with gating the 738-step `assert`
  mode in `_classify_mode`).

### 12j. Pre-existing candidate claims in adjacent territory -- MECH-395/482/483, discovered at `/session-land` Phase 5a re-verification, distinct from track A but requiring explicit reconciliation (2026-08-09T18:4xZ)

`claims.yaml` already carries a mature cluster of candidate claims registered 2026-08-05 (from a
`docs/thoughts/2026-08-05_epistemic_deficit_and_orienting.md` thought intake) that were not surfaced by any
earlier pass of this review, because the original grep in Sections 11b/13-A checked the `ree_core/` CODE
tree (genuinely empty) and a narrow claims.yaml grep, not a full read of the surrounding claim cluster:

- **MECH-482** (`epistemic_deficit`): a persistent, target-bound accumulator ("rises with unresolved
  importance x uncertainty x expected_resolvability x persistence"), explicitly defined **in contrast to**
  "raw novelty (MECH-314a)... **transient prediction error**... learning-progress (MECH-314c)". `status:
  candidate`, `v3_pending: true`, **"DO NOT build in V3"** -- gated on GAP-A (`substrate_queue.json`,
  priority 1, unclaimed: extending per-candidate uncertainty tracking to MECH-314b/314c, currently a global
  scalar), which is not yet built.
- **MECH-483** (`orient/survey`): "a third primitive behavioural regime (alongside approach and avoid)... a
  temporary, diffuse reduction in commitment... driven by accumulated epistemic_deficit (MECH-482) rather
  than a specific cue." Also `candidate`/`v3_pending`/**"DO NOT build in V3"**, same GAP-A gate.
- **MECH-395** (`pre-approach orienting/surveying mode`): a cue-triggered, need-gated active-sensing state
  entered when a cue/need IS present but directional confidence is too low -- narrower and different again
  (resolves a specific vector for an already-identified cue, not a diffuse survey).

**Track A's proposed mechanism is genuinely distinct, not a duplicate -- the two claims' own definitions
draw the line.** MECH-482 is explicitly defined AGAINST "transient prediction error"; track A's trigger
(11b step 1, corroborated 12b/12h) is a **phasic spike in `residue_surprise`** -- exactly a transient,
per-step prediction-error-magnitude signal, the opposite end of the timescale from MECH-482's slow,
persistent, target-bound accumulator. Track A's signal (`residue_surprise`, residue index 3) is *also
already computed every step* (confirmed directly in the 906b episode log throughout this review) --
it does **not** depend on GAP-A's not-yet-built target-bound uncertainty substrate, so the "DO NOT build in
V3" gate on MECH-482/483 does not extend to it. This is the same phasic-vs-chronic distinction 12g already
established empirically for the harm channel (`z_harm_norm` phasic vs `z_harm_a` chronic) -- now recognised
as a general pattern in this substrate's telemetry, not a one-off.

**But the naming space is now crowded (three "orienting"-adjacent mechanisms), and this needs explicit
handling, not silent registration.** Risk: a cold `/implement-substrate` session registering a new
"defensive orienting" MECH without reading this cluster could (a) pick a confusingly similar name/subject,
(b) fail to cross-reference MECH-395/482/483 the way each of THEM cross-references the others (their own
convention -- see their `depends_on` lists and "Distinct from MECH-XXX..." notes), or (c) worse, have its
STOP-CHECK's `grep -iE "defensive.orient|orienting" claims.yaml` match these entries and incorrectly
conclude "a MECH already registered, STOP" and abort on a false positive. **Chip A's prompt has been revised
(v3) to name this cluster explicitly, explain why it is not a block, and require the new MECH to
cross-reference MECH-395/482/483 by the existing convention rather than register in isolation.**

---

## 13. Tracked follow-on tasks (recorded 2026-08-09T17:55Z, user-directed: "all of the above must be done")

All four tracks below were reviewed with the user and confirmed as required -- recorded here as the single
reference list rather than split across TASK_CLAIMS/chips prematurely. Each is scoped to its own dedicated
skill session per repo convention; none is started or claimed by this data-mining session.

**A. Build the defensive-orienting chain (`/implement-substrate`).** Full scope in Section 11b/11d:
surprise-onset -> phasic freeze (held until epistemic sufficiency) -> orienting reflex (return path to
planned action) -> freeze-override (identification-confidence sufficiency) -> valence-gated
approach/withdraw/resume. Register candidate MECH. Validate against the Section 4 coupling nulls (target:
post-build, the surprise->behaviour couplings measured in 12b should move well past their current near-zero
/ diffuse-44% baselines toward a sharp, deterministic signature). 12b's p90/p95/p99 spike thresholds and the
44.3%/15.4% incidental-coupling baseline are usable inputs for this build's design and its pre/post
validation. 12e adds direct corroboration: movement direction during `approach`/`avoid` mode is essentially
uncorrelated with the nearest resource/hazard (mean cosine 0.019 / -0.053) -- there is currently no
mechanism that latches onto and steers toward a specific identified stimulus, which is exactly the gap this
build closes. **CALIBRATION RISK, read 12h before setting the trigger threshold**: `residue_surprise` does
not reliably spike on the ground-truth injected events (`limb_damage_injected`, `world_rule_shift_occurred`)
and its average response to `external_hazard_injected` (0.024) sits below the p90=0.040 threshold 12b
proposed -- a naive absolute-value-spike trigger at that threshold would likely under-fire on the paradigm
cases. 11b step 1 already specifies a positive-derivative/novelty-onset detector rather than an absolute
threshold; re-derive/validate the actual trigger condition against these ground-truth events specifically
(12h), not only the overall distribution, before finalising it. Largest scope of the four; user-ratified "as
ambitious as possible," orienting is load-bearing (not deferrable).

**B. `/governance` harvest.** Record the Section 4 affect->behaviour decoupling as an independent,
fresh-substrate corroboration of the MECH-439 F-dominance / 719a competence-wall lineage (11a) -- now
strengthened by 12a's direct `is_committed`=0/3909 reading, a sharper instrument than the mode-diversity
proxy alone. Non-scoring (`claim_ids=[]`, single-seed, all-ON) -- observational corroboration only, for
governance to weigh.

**C. `/queue-experiment` -- sleep-refinement DV on the fishtank substrate.** Tests whether the
sleep-refinement DV (slot/mode diversity) registers a non-null waking->sleep difference on this
repertoire-diverse-but-non-converting substrate, discriminating "sleep GAP-2 is blocked on repertoire" vs
"blocked on conversion" (11a). Expected null given 12a/12b; 12d's n=1 ad-hoc read of this run's one firing
(`sws_slot_diversity`~0, `replay_diversity_index`=-1.0 sentinel for zero draws) previews that expectation
but does not resolve it -- a proper probe across multiple firings/seeds is still needed.

**D. Telemetry/viz follow-on.** Surface `VALENCE_SURPRISE` (residue index 3, i.e. `residue_surprise`) and
`VALENCE_LIKING` (index 1) in `_read_affect` / `fishtank_viz.html` -- liking bar already landed (Section
10); surprise is not yet surfaced (3c, 11b step 1 note). Smallest scope; substantially de-risks A by making
the freeze-trigger signal visually inspectable during the build. Also candidate: log `running_variance` /
`commit_threshold` per-step (currently absent -- see 12a caveat) so a future pass can distinguish
"structurally uncommitted" from "chronically near-threshold."
