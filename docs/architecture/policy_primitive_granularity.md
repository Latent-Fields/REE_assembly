# Policy Primitive Granularity — Architectural Family

**Status:** family slot registered 2026-05-10 (ARC-069 parent + ARC-070 + ARC-071 candidate / pending_design).
**Family principle:** the unit of policy that the rule-apprehension and diversity-generation layers operate on is itself a dynamic representation — primitives can decompose into finer ones (ARC-070, on prediction failure) or compose into coarser ones (ARC-071, on repeated grounding).

---

## What this family fixes

REE today treats hippocampal rollout primitives as flat-grain. ARC-007 (strict) commits to value-flat hippocampal proposals, instantiated currently as CEM-sampled action sequences at single-timestep grain. Both downstream layers — ARC-062 rule apprehension and ARC-065 behavioural diversity generation — read these flat sequences. There is no machinery for the unit being chained to rescale.

The user's observation, via the rollout chaining work:

> "When looking at chaining behaviours together for hippocampal rollout we are working on there being behavioural diversity to chain together but when imagining a chain presumably the imagined chains may need splitting up into more chained behaviours or sometimes a number of chained behaviours together being realised to better be represented by a single behaviour (or rather than behaviour I suppose we should be thinking as policy or apprehended rule)."

This identifies two inverse architectural moves missing from the substrate:

| Direction | Trigger | Timescale | Phenomenology |
|-----------|---------|-----------|---------------|
| **Decomposition (ARC-070)** | Prediction failure on a chunk (low MECH-269 V_s on chunk's region; or E2 disagreement; or completion-signal failure) | Fast, simulation-side | "I planned 'go to the kitchen' but now I need to plan the steps." |
| **Composition (ARC-071)** | Repetition + outcome consistency on a sub-sequence | Slow, execution-side | "Making coffee was once seventeen motor acts; after a thousand repetitions it's one unit." |

Both are operations on the same underlying object — the policy-primitive representation that ARC-007 emits, ARC-062 reads, and ARC-065 perturbs. ARC-069 names the parent commitment ("primitives are dynamic"); ARC-070 and ARC-071 name the inverse operations.

---

## The three slots

### ARC-069 — parent commitment (primitives are dynamic)

The architectural commitment, separate from any specific mechanism. Reads: *the unit-of-policy that the rule-apprehension layer (ARC-062) and the diversity-generation layer (ARC-065) operate on is itself dynamic, not a fixed primitive.* This is registered before mechanism work because the commitment cuts across multiple subsystems and constrains their joint design.

Without ARC-069, ARC-007 hippocampal proposals are flat-grain forever; ARC-062 must apprehend rules at whatever grain the proposer happens to emit; ARC-065 perturbs only at that grain. With ARC-069, the proposer emits at variable grain; ARC-062 sees rules at the appropriate scale for the current task; ARC-065 perturbs at the grain that actually adds diversity.

### ARC-070 — decomposition on prediction failure (zoom in)

When an imagined chunk fails to ground at the resolution required for execution, the rollout representation re-segments the chunk into finer primitives. Trigger candidates:

- **MECH-269 V_s drop on the chunk's region** — cleanest existing-substrate hook; if V_s on the region is low, chunked primitives over that region can't be reliably predicted.
- **E2 forward-model disagreement** — chunk-grain prediction disagrees with stepwise primitive-grain prediction.
- **Hippocampal completion-signal failure** (MECH-105 / ARC-028) — expected completion doesn't arrive on schedule.
- **Mid-execution prediction error** — chunk fired, agent is N steps in, next predicted state has diverged. Decompose the remainder.

Likely a combination — lit-pull will arbitrate.

Biology anchors (post-2026-05-10 lit-pull verdicts integrated; see `evidence/literature/targeted_review_arc_070_decomposition/synthesis.md`):

- **Zacks et al. 2007 (Psychol Bull)** — event segmentation theory; PE is the canonical boundary trigger; framework is substrate-agnostic about whether the predictive stream is observed or imagined. R1 + R2 (theoretical) + R5 anchor. lit_conf 0.84.
- **Schacter, Addis & Buckner 2008 (Ann NY Acad Sci)** — constructive episodic simulation; the same core network (medial PFC, hippocampus, retrosplenial / posterior cingulate, inferior parietal lobule) supports both remembering past and imagining future events. R2 LOAD-BEARING empirical anchor — added to the primary cluster from the lit-pull. lit_conf 0.82.
- **Badre & D'Esposito 2009 (Nat Rev Neurosci)** — rostro-caudal prefrontal hierarchy; multi-level action abstraction. R3 empirical anchor. lit_conf 0.78.
- **Pfeiffer & Foster 2013 (Nature)** — hippocampal forward path sweeps elaborate trajectories with cue-dependent dynamics; the imagination-side rollout substrate exists and is online during navigation. R1 substrate + R3 + R4 substrate anchor. lit_conf 0.78.
- **Koechlin & Summerfield 2007 (Trends Cogn Sci)** — cascaded cognitive control; theoretical scaffold for multi-level decomposition. R3 theoretical + R5 hybrid anchor. lit_conf 0.74.
- **Schapiro et al. 2017 (Phil Trans Roy Soc B)** — CLS within hippocampus; trisynaptic pattern-separation as candidate V_s substrate; dual pathways support multi-grain representation. R1 substrate + R2 pathway grounding + R3 multi-grain anchor. lit_conf 0.74.
- **McGovern & Barto 2001 (ICML)** — bottleneck-state subgoal discovery; **foil**, not primary. R5 verdict distinguishes bottleneck-state framing (statistical) from PE-driven framing (biological); ARC-070 commits to PE-driven primary. lit_conf 0.62 (mixed direction).

### ARC-071 — composition via repeated grounding (zoom out)

Sequences of primitives repeatedly executed together with consistent outcomes are accumulated into a single primitive. The chunked unit is added to the candidate pool; downstream layers operate on it atomically. The pre-existing primitive sequence remains available, so ARC-070 can decompose the chunk back if it later fails to predict.

ARC-071 names the **transition mechanism that MECH-163 dual systems presupposes but does not specify**. MECH-163 names the presence of a habit system and a planned system; ARC-071 is the machinery that pumps content from planned-into-habitual.

Trigger candidates:
- **Repetition count + outcome consistency** — the canonical Graybiel pattern.
- **Reward-rate-conditioned chunking** — Sakai 2003 motor sequence learning.
- **V_s-conditioned chunking** — chunks form preferentially over sequences that produce reliable predictions (V_s-positive analog of ARC-070's V_s-negative trigger).
- **Free-energy minimisation** — chunks form because they reduce expected free energy.

Biology anchors:
- **Graybiel 1998 (Annu Rev Neurosci)** + **Graybiel 2008** — striatal chunking foundational references.
- **Sakai et al. 2003 (Curr Opin Neurobiol)** — chunking in motor sequence learning across pre-SMA / cerebellum / striatum.
- **Wymbs et al. 2012 (Neuron)** — motor chunk formation.
- **Sutton et al. 1999 (Artificial Intelligence)** — options framework, cleanest formal analog.
- **Botvinick 2009 (Trends Cogn Sci)** — hierarchical organisation of behaviour.
- **Yin & Knowlton 2006 (Nat Rev Neurosci)** — DLS (habit / chunked) vs DMS (goal-directed / unchunked) division.
- **Smith & Graybiel 2013 (Neuron)** — chunk dynamics: form, dissolve, reform across timescales.

---

## How the three relate to existing REE substrate

**ARC-007 strict** (hippocampal proposals are value-flat): preserved. The regranularisation operates on the *shape* of proposals, not on their value. ARC-007's no-internal-value-head invariant is intact.

**ARC-062 rule apprehension** (gated policy heads + context discriminator): reads policy primitives. With ARC-069 instantiated, the rules being apprehended are over potentially-chunked primitives. Open question deferred to child-MECH design: rule identification across grains.

**ARC-065 behavioural diversity generation**: perturbs primitives. Composition reduces local diversity (chunked sub-elements lose independent perturbability) but increases abstraction; decomposition increases local diversity but raises combinatorial cost.

**MECH-269 V_s** (per-stream / per-region verisimilitude): the most plausible trigger signal for ARC-070 decomposition, and a candidate condition (V_s-positive) for ARC-071 composition. ARC-070 becomes the **second major V_s consumer** after MECH-269b symmetric-V_s-gating.

**MECH-288 event segmenter** (substrate-side two-level hierarchical detector reading latent + PE streams): **ARC-070 is a bidirectional consumer of the same substrate, not a parallel module** (lit-pull R2 verdict 2026-05-10, LOAD-BEARING, conf 0.74). MECH-288's API consumes `latent_dict` + `pe_dict` — substrate-agnostic about whether those latents originate in observation or in simulation. ARC-070 adds the policy-side consumer that reads MECH-288 boundary pulses on the rollout / imagination stream and re-segments the proposal trajectory at finer grain. Same detector, two input streams (observation, rollout), two downstream effects (MECH-269 anchor-set update on observation; decomposition pulse on rollout). The "imagination-side analog" framing from the original registration is superseded by the bidirectional-substrate framing. Falsifiable: lesioning MECH-288 should impair BOTH observation-side anchor partition AND imagination-side decomposition; the bidirectional hypothesis predicts no dissociation. See `evidence/literature/targeted_review_arc_070_decomposition/synthesis.md` for the constructive-episodic-simulation grounding (Schacter 2008 core network).

**MECH-292 / MECH-293 ghost-goal bank + waking probes**: anchors are point-keys. ARC-069 + ARC-071 add structure-bearing primitives that anchors can seed. The SD-039 goal_payload extends naturally to chunks — a chunked primitive with a stable goal-payload is an accumulated "recipe" the agent has formed.

**MECH-163 dual systems** (planned vs habitual): ARC-071 is the transition mechanism. Habit chunks are the *output* of ARC-071; planned-system trajectories are the *input*. Without ARC-071 the dual systems are static configurations; with ARC-071 the division of labour shifts continuously with experience.

**MECH-094 hypothesis_tag**: ARC-070 fires during simulation (must respect MECH-094 — decomposition during waking action does not write residue). ARC-071 fires from real executed sequences (`hypothesis_tag=False`) by default, with one explicit narrow exception: **MECH-322** (registered 2026-05-11 to resolve the ARC-071 lit-pull R6 governance escalation) permits ARC-071 chunking from replayed (`hypothesis_tag=True`) sequences during designated SD-017 sleep phase IF (a) the replayed sequence carries a value-tag from prior real-executed episodes meeting a high-positive threshold, (b) the replay occurs in sleep mode (not waking DMN), (c) the formed chunk carries a `replay_origin=True` audit flag and faces accelerated dissolution if not corroborated by real waking execution within N episodes (suggested default 50–100). MECH-094 strict gating remains the default for all other write paths; MECH-322 is a parallel narrow path with audit trail. Waking DMN (where MECH-292 / MECH-293 ghost-goal probes operate) remains MECH-094-strict — the carve-out is sleep-only. The carve-out matches the Albouy 2013 hippocampal-striatal sleep-replay coupling found in the ARC-071 lit-pull R6 evidence.

---

## How the three slots compose at runtime

```
Hippocampal rollout produces a candidate trajectory.
                         |
                         v
Trajectory consists of a sequence of *primitives*. Each primitive is
EITHER a single-action unit OR a chunk (ARC-071-formed, ARC-070-decomposable).
                         |
                         v
For each primitive in the trajectory, evaluate predictability:
  - chunk grain: V_s on chunk region (MECH-269) + chunk outcome confidence
  - if V_s is below threshold, decompose chunk into sub-elements (ARC-070)
                         |
                         v
ARC-062 apprehends rules over the (possibly-decomposed) trajectory.
ARC-065 generates diversity at the appropriate grain.
                         |
                         v
On commit + execution, accumulate (sub-sequence, outcome) pairs.
                         |
                         v
ARC-071 composition accumulator: for repeated (sub-sequence -> outcome)
patterns with low outcome variance, form a new chunked primitive and add it
to the candidate pool. (Original primitives remain; chunks are additive.)
```

ARC-070 sits in the **rollout** path (simulation-side, fast); ARC-071 sits in the **post-execution** path (real-grounding-side, slow). They operate on the same representational object but at different stages and timescales.

---

## Falsifiable family-level prediction

Run an REE agent for many episodes on a task with a structurally repeating sub-sequence (e.g. SD-054 reef + a repeating forage-loop):

- **Without ARC-071**: every rollout in episode 1000 still proposes at single-action grain. Rollout deliberation cost stays flat. Behavioural latency on the repeating sub-sequence does not drop.
- **With ARC-071 active**: the repeating sub-sequence compresses into a chunked primitive. Rollout deliberation cost on it drops measurably. Behavioural latency drops (faster commit, less deliberation).

Then introduce a region of high V_s drop in the middle of a chunked primitive's region:

- **Without ARC-070**: agent commits to the chunk, executes it blind, pays prediction-failure cost at execution.
- **With ARC-070 active**: agent re-decomposes during rollout; refines the proposal at finer grain over the low-V_s region; either finds a finer-grain plan that grounds, or fails-to-plan and aborts (both PASS — the prediction is the decomposition fires, not that the alternative succeeds).

---

## What this commits REE to

A representational shape for policy primitives that has not previously been registered: **variable-grain, dynamically restructured by both prediction failure (decompose) and repetition with consistency (compose)**. Every existing slot in REE that touches the rollout or rule-apprehension paths has been written assuming flat-grain primitives; ARC-069 commits to relaxing that assumption.

The biggest downstream consequence is for ARC-062 / ARC-065. Rules apprehended at one grain may not apply at another; diversity generated at one grain may not produce useful candidates at another. The grain question is now part of the rule and diversity design space — not a parameter we set, but a state-conditioned variable. This is bigger than it looks; the lit-pulls and child-MECH phases will need to address grain-invariant rule apprehension explicitly.

---

## What this is NOT

- **Not a hierarchical-RL options re-implementation.** Sutton 1999 is the analog, not the spec. Biology distributes the substrate (hippocampal / prefrontal / striatal) in a way that doesn't cleanly map to the options framework's value-side machinery.
- **Not a representation-compression slot at the encoder layer.** Chunks are over policy primitives, not over latent observations. SD-009 z_world contrastive supervision and SD-018 z_world resource proximity are encoder-side; ARC-069 family is policy-side.
- **Not a goal hierarchy.** Chunks are over policy primitives. Goal hierarchies are a separate architectural concern (cf. SD-015 z_resource and z_goal_snapshot in MECH-292/293). The two interact (goals drive which chunks form) but are not the same slot.
- **Not a feedback loop on V_s itself.** ARC-070 reads V_s; the V_s update path remains MECH-269 substrate.

---

## Open Q-claims worth registering at child-MECH time

1. **Grain-invariant rule apprehension**: how does ARC-062 handle rules learned at one grain that need to apply at another? Hierarchical rules are likely apprehended at multiple grains in parallel (Botvinick 2009); the design will need to address this.
2. **Chunks-of-chunks recursion**: depth of recursion permitted. Biology supports deep hierarchy; computational cost / catastrophic-rigidity tradeoffs are open.
3. **Decomposition triggered by outcome inconsistency**: when an existing chunk's outcome variance rises above threshold, does the chunk decompose (ARC-070), or simply become un-selectable from the proposal pool? Different behavioural signatures; lit not decisive.
4. **Diversity generation across grains**: should ARC-065 operate on chunked or unchunked representations? Likely both at different timescales — separate Q-claim.

---

## Pathology cross-references (speculative, pending lit-pull)

These cross-link to `psychiatric_failure_modes.md` after lit-pulls land:

- **Obsessive-compulsive disorder** as ARC-071 weakened: chunks fail to form, every routine action is re-planned at primitive grain, over-deliberation signature.
- **Autism / insistence-on-sameness** as ARC-070 weakened on chunked primitives: chunks form normally but cannot be re-decomposed when context demands different grain, producing rigidity.
- **Skill / motor-learning impairments**: chunking machinery itself impaired; sequences never compress; deliberation budget exhausted.

These are pre-registration cross-references — speculative until biology lit-pulls land and child-MECH mechanism shape is fixed.

---

## Child MECH/SD design — what's needed before phasing

Two independent lit-pulls anticipated:

1. **`targeted_review_arc_070_decomposition/`** — **LANDED 2026-05-10.** 7 entries; aggregate lit_conf 0.88 (indexer-computed); 6 supports + 1 mixed. Five verdicts settled: R1 V_s-drop on chunk's region as primary trigger (PE-driven); **R2 LOAD-BEARING — SHARED SUBSTRATE: ARC-070 is a bidirectional consumer of MECH-288, not a parallel module**; R3 multi-level recursive decomposition with depth cap 3-4; R4 both pre-commit and mid-execution phases via same mechanism with MECH-094 hypothesis_tag-conditional downstream effects; R5 PE-driven primary, McGovern-Barto bottleneck-state framing as optional consolidation-phase secondary. See `evidence/literature/targeted_review_arc_070_decomposition/synthesis.md`.
2. **`targeted_review_arc_071_composition/`** — **LANDED 2026-05-10** (sibling parallel pull). 9 entries; aggregate lit_conf 0.848. R3 confirmed ARC-071 IS the missing transition mechanism MECH-163 dual_goal_directed_systems presupposes (MECH-163 depends_on +ARC-071 committed 2026-05-10). R6 SAFETY-CRITICAL: biology does NOT cleanly gate chunking write path against replay/imagined sequences — **RESOLVED 2026-05-11 via MECH-322** sleep-replay value-conditioned carve-out (narrow exception path, audit trail, accelerated dissolution on uncorroborated replay-origin chunks). Child-MECH design unblocked.

The two children share the parent commitment but no execution path — they're decoupled within the cluster, similar to how ARC-066 / ARC-067 / ARC-068 are decoupled within the non-deficit-action-drives family.

### Child-MECH design — ARC-070 side (REGISTERED 2026-05-10)

With R2 settled, ARC-070's first child mechanism is registered as **MECH-321 `policy.decomposition_via_event_segmenter`** (`candidate / v3_pending`):

- **Subject:** `policy.decomposition_via_event_segmenter`. Policy-side consumer of MECH-288 boundary pulses on the rollout / imagination input stream.
- **depends_on:** ARC-070 (parent), MECH-288 (substrate), MECH-269 (V_s primitive trigger source), MECH-094 (hypothesis_tag gating).
- **Trigger (R1):** V_s drop on chunk's region (read out of MECH-288 + MECH-269). MECH-288 produces the boundary; MECH-321 consumes the boundary at the policy-primitive layer and triggers re-segmentation.
- **Output:** re-segmented rollout proposal stream at finer grain.
- **Depth control (R3):** recursive multi-level decomposition with depth cap 3-4.
- **Phase handling (R4):** pre-commitment fires during simulation under hypothesis_tag=True with no residue write; mid-execution decomposition fires under hypothesis_tag=False with residue write enabled and observation-side consumer chain operating normally.
- **Optional secondary (R5):** bottleneck-aware consolidation-phase analysis; may integrate with ARC-071 chunk-formation pipeline once the ARC-071 R6 governance decision lands.

Substrate-readiness prerequisite: MECH-288 substrate (`event_segmenter.py`) must land first WITH the input_stream label extension (per MECH-288 2026-05-10 ARC-070 bidirectional-consumer commitment in its notes). MECH-321 cannot be substrate-implemented before MECH-288. Phase-1 placement is a thin policy-side module subscribing to a MECH-288 BoundaryEvent queue filtered to `input_stream=rollout`, wired at the hippocampal-rollout candidate-generation layer prior to E3 trajectory selection.

Discriminative-pair validation experiment specified in MECH-321 functional_restatement (ARM_0 baseline / ARM_1 V_s-drop primary / ARM_2 bottleneck-state primary); deferred until substrate lands.

### Child-MECH design — ARC-071 side (FORMATION OPERATOR REGISTERED 2026-05-11; maintenance operator pending)

With R6 resolved via MECH-322 (sleep-replay carve-out), ARC-071's child-MECH design is unblocked. The lit-pull's R2 verdict (phase-dependent multi-substrate with formation in striatum/DLS and maintenance in IL/vmPFC) maps onto **two child-MECHs**, mirroring Smith & Graybiel 2013's "dual operator view":

**MECH-323 `policy.composition.chunk_accumulator_formation` (REGISTERED 2026-05-11)** — the striatum/DLS-analog formation operator.

- **Subject:** `policy.composition.chunk_accumulator_formation`. Builds chunk candidates from sequences of policy primitives repeatedly executed together with consistent outcomes.
- **depends_on:** ARC-071 (parent), MECH-094 (default strict gate), MECH-322 (sleep-replay carve-out path), SD-014 (valence vector), SD-039 (anchor goal-payload), MECH-269 (V_s positive secondary).
- **Trigger conditions (joint AND):** (1) repetition count ≥ R_min over sliding window W; (2) outcome-variance below F_low formation threshold (hysteresis with MECH-324's F_high dissolution threshold); (3) evaluative gate — accumulated outcome mean must be positive (Graybiel 2008 framing). Secondary preference: V_s-positive (the symmetric inverse of MECH-321's V_s-negative trigger).
- **Chunked-primitive object fields:** `sequence`, `initiation_set`, `termination_condition`, `value_tag`, `replay_origin`, `formation_timestamp`, `depth`. The initiation_set + termination_condition fields satisfy the Sutton 1999 options-structure requirement that R4 surfaced.
- **Suggested parameter defaults (child-MECH validation refines):** R_min = 20 reps; W = 100 trials; F_low = 0.15 (on 0–1 normalised outcome-variance); evaluative threshold = baseline + 0.05; recursion depth cap = 3.
- **Two write paths:** default MECH-094-strict (real-executed sequences, replay_origin=False); MECH-322 sleep-replay carve-out (high-value-tagged sleep replays, replay_origin=True, dissolution-deadline accounting).
- **What MECH-323 preserves:** ARC-007 strict value-flat proposals (value_tag is metadata, not a value head); MECH-094 strict on the default path; SD-039 anchor payload semantics; MECH-269 substrate.
- **First validation experiment:** substrate-readiness diagnostic measuring whether the accumulator fires at all on a structurally repeating sub-sequence task with default parameters. Behavioural-latency / rollout-cost measurements follow once the accumulator-only diagnostic passes.

**MECH-324 `policy.composition.chunk_maintenance` (PENDING — separate registration pass)** — the IL/vmPFC-analog maintenance operator. Causally required for chunk crystallisation per Smith & Graybiel 2013 optogenetic disruption. Will define: chunk persistence under continued real-execution corroboration; chunk dissolution when variance rises above F_high (slower timescale than formation, per R5); accelerated dissolution for MECH-322 replay-origin chunks not corroborated within N episodes; cross-link to MECH-163 habit-maintenance side and INV-037 / INV-038 (vmPFC-analog substrate hooks).

**Frontoparietal early-phase parsing (Wymbs 2012 R2 partial-mapping):** not a separate ARC-071 child-MECH. It bleeds into ARC-070 / MECH-321 territory (segmentation, not concatenation); cross-linked to MECH-321 rather than registered here.

---

## See also

- `claims.yaml` — ARC-069 / ARC-070 / ARC-071 entries (full functional_restatement and notes per claim)
- `non_deficit_action_drives.md` — companion architectural family registered the same day (2026-05-10) from user phenomenology
- `MECH-269` — V_s primitive (most plausible ARC-070 trigger signal)
- `MECH-288` — event segmenter (observation-side analog of ARC-070)
- `MECH-163` — dual systems (ARC-071 names the transition mechanism)
- `MECH-292` / `MECH-293` — ghost-goal bank + probes (chunks may seed anchors)
- `ARC-007` (strict) — hippocampal proposals; ARC-069 family preserves value-flat property
- `ARC-062` — rule apprehension (operates over primitives at variable grain)
- `ARC-065` — behavioural diversity generation (perturbs primitives at variable grain)
- `MECH-094` — hypothesis tag (composition is execution-side, decomposition is simulation-side; both must respect the gate)
