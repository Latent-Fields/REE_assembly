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
1. **Anticipatory threat detection (the "fright").** The post-906b sensory window now sees harm-onset before contact (the engineered smell-before-harm gap: harm onset inside radius-2, `proximity_n_threshold=0.4`/`hazard_field_decay=2.5`). Wire a *phasic* startle signal from a sharp positive gradient in perceived proximity-to-hazard (`z_harm_s` sensory / hazard-field gradient in-window) -- the anticipatory signal that dread *should* carry.
2. **Phasic freeze (orienting arrest).** A brief, threat-triggered freeze distinct from the chronic `z_harm_a` suffering-lock -- short-duration locomotor halt on the startle, not gated on accumulated suffering.
3. **Reorienting.** An attentional/heading turn toward the detected threat (currently nonexistent). This is the "push more on implementation" the user names -- orienting is the missing bridge.
4. **Action decision (approach vs withdraw).** Post-orient, select defensive withdraw vs appetitive approach from valence sign x threat proximity, bridging orienting into the existing approach/avoid behaviour.

This is substantial (a new ree_core pathway + likely a new MECH claim), not a knob change. It should be built via `/implement-substrate`, then its coupling validated -- which also subsumes the review's proposed **V3-EXQ-906d** (defensive-availability probe): 906d tested whether the *existing* suffering-driven freeze is appropriately selected; the real answer is that the *anticipatory* defensive chain does not exist yet and needs building first.

### 11c. Routing (proposed; skill-gated -- not executed here)
- **Harvest (11a):** record the decoupling<->conversion/competence-ceiling convergence against the MECH-439 / competence-wall lineage via `/governance` (observational corroboration, not a scoring move); it does not touch the sleep block.
- **Probe (11a):** optional `/queue-experiment` -- run the sleep-refinement DV on the fishtank substrate to settle repertoire-vs-conversion empirically.
- **Build (11b):** `/implement-substrate` the fright->freeze->reorient->approach/withdraw defensive-orienting pathway (+ candidate MECH registration), which supersedes the 906d probe proposal.

### 11d. Build directive + status (user, 2026-08-09T17:40Z)
**RECORD-ONLY this session -- the build is NOT started here; it is to be picked up in a dedicated `/implement-substrate` session.** User steer on ambition when it is: **build the FULL chain (fright -> phasic freeze -> reorienting turn -> valence-gated approach/withdraw arbitration) "as ambitiously as is possible given what we know" -- do NOT scope down to a minimal fright+withdraw increment.** So the dedicated session should treat all four components of 11b as the first increment, register the candidate defensive-orienting MECH, and validate against the Section-4 coupling nulls (the pass criterion is that the built chain moves dread->avoidance / threat-proximity->withdraw coupling off ~0, i.e. it converts anticipatory threat state into state-appropriate action -- the organism-level counterpart to lifting the MECH-439 conversion ceiling). The harvest (11a/11c) and the sleep-substrate probe remain available but are not blockers on the build.
