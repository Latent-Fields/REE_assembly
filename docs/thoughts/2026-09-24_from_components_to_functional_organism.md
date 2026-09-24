Status: processed
Intake: evidence/planning/thought_intake_2026-09-24_from_components_to_functional_organism.md
Claims registered: MECH-586 (2026-09-24, chip-20260924-mech586-register) -- intake sec 6
Orchestrator execution prompt: evidence/planning/orchestrator_execution_prompt_2026-09-24_functional_organism_path.md

# From components that work to an organism that works

An evidence-graded path for the Reflective-Ethical Engine (REE)

**Date:** 24 September 2026
**Status:** thought document and proposed validation map; not a claim promotion, build authorisation, experiment commission, or change to version scope.
**Evidence freeze:** REE_assembly at d3b73c9ec92064ab836f134134a08fd549c17942; ree-v3 at 4fc6f3d0f33f2746e4586f349b82af6ab94a3936. The latest assembly commit in this snapshot is dated 06:08:57 Coordinated Universal Time on 24 September.
**Authorship:** the quoted seeds below are Daniel's words. The analysis, proposed tests and synthesis are assistant-authored at his request; they should not be treated as his verbatim formulations or as ratified architecture.
**Capture route:** pasted into a Claude Code session by the user on 2026-09-24 with the instruction that, after ingestion and digestion, an execution prompt for a `/metaworker-orchestrate` session should be produced from it. Text below is verbatim.

## 1. The question behind the thought

> "It always tastes very close to working. But it really feels close now"

> "And what are the pieces needed to get it working? Do we know them now for sure?"

> "Could you look into this more to create a thought document which maps the path to functional organism"

The answer after a fresh repository inspection is: we have a better map of the necessary functions and several actual failures, but not a proven sufficient set of repairs. Some links previously described as missing already exist. Some plausible fixes have failed. Several encouraging new results demonstrate influence on selection, not improved behaviour.

The useful target is therefore not "install the remaining modules." It is to establish a reproducible closed learning loop:

> The organism detects a consequential distinction, predicts what its own alternatives would change, selects and executes accordingly, experiences the outcome, and uses that experience to improve later choices without losing earlier competence.

This is a functional description, not a claim about consciousness, sentience, general intelligence or the eventual success of REE's ethical architecture. A single-agent world cannot demonstrate care for other agents.

The working hypothesis is that a substantial part of the remaining difficulty lies in decision-useful information surviving each handoff. That is stronger than saying "the parts are disconnected," but weaker -- and more defensible -- than saying "one new legibility layer will make everything work."

## 2. What the fresh inspection changes

The earlier conversational account needs four corrections.

1. **A native world-forward route to selection exists.** The driver for V3-EXQ-1081 traces the hippocampal proposer through `rollout_with_world()` and `world_forward()` into the world-state sequences scored by the trajectory-selection system (E3). A direct search inside the selector had missed this indirect route. The remaining question is useful content and reliable behavioural benefit, not whether any connection exists. [R6]
2. **Action blindness is configuration- and assay-dependent.** V3-EXQ-1082 uses a live, reset-on-termination battery and alpha_world=0.9. Its baseline reads actions on all three seeds; adding the tested separation-margin loss reduces that read. We cannot now say that the world model simply lacks action conditioning, nor recommend the margin loss as an established repair. [R5]
3. **The harm probe has not resolved the cause.** V3-EXQ-1077 removes the active-error pattern with converged training but returns an ambiguous comparison with persistence on all three eligible seeds. It neither proves a representation ceiling nor proves that another prediction-error source will solve the problem. [R4]
4. **The top three ready items are not the complete organism recipe.** Harm-forward diagnosis, candidate effort and held-rule transfer are valuable work packages. They do not establish encoder adequacy, goal grounding, useful multi-step prediction, execution, retention, ecological transfer or integrated compatibility by themselves. [R2, R9, R10]

There is also a freshness issue. The workset generated at 04:59:23 reports 260 items, 33 ready, zero workset items in flight, and two pending reviews. The later pending-review document generated at 06:04:23 reports seven items, including six diagnostics without confirmed autopsies and one error manifest. "Zero in flight" is a workset field, not evidence that the whole experimental system has no live work. The workset itself names live experiments. No new execution should be based on the older count alone. [R1]

### The evidence that matters most

| Finding in the inspected snapshot | What it supports | What it does not establish |
|---|---|---|
| The confirmed encoder-transfer analysis records a preservation coefficient of determination (R²) improvement of **0.1184**, but consumer action agreement improves only **0.0081** after 3.3 times the training steps. The question was re-posed as `sd106_objective_consumer_transfer`. | Improving the existing preservation objective is not translating proportionately into this consumer's task. | That all useful information is absent; that every consumer is broken; or that task-aware supervision is already a proven repair. [R2] |
| The confirmed `V3-EXQ-1062a` autopsy finds the harm-forward head worse than persistence in **six of six cells**. | The absolute R² readiness gate was inadequate for this slow-changing latent; the residual cannot be assumed to represent world surprise cleanly. | That harm is useless, that the broader mechanism is falsified, or that this is definitely a representational limit. The magnitude of negative skill is denominator-sensitive. [R3] |
| `V3-EXQ-1077`: three seeds reproduce the defect and converge; all three then return `cannot_determine`. | Completed instrumentation and a narrower, still unresolved causal question. | A reason to repeat the same training probe, or a clean win for either undertraining or a ceiling explanation. Diagnostic adjudication remains pending. [R4] |
| `V3-EXQ-1082`: baseline action-read statistic **0.341 / 0.216 / 0.227**; baseline skill against identity **0.349 / 0.219 / 0.215**, at the stated operating point. All tested margin arms lower the action-read statistic. | Candidate action information is readable under this configuration; "force predictions farther apart" is not equivalent to learning their consequences correctly. | A universal operating-point recommendation, closed-loop competence, or a formally adjudicated conclusion. [R5] |
| `V3-EXQ-1081`: after a forced sleep cycle, the head swap changes top-preferred first-action classes through the rollout route; that route passes its criterion on two of three seeds. Norm-matched random perturbations also change rankings. | A real route through which a sleep-sized head change can affect selection. | That sleep made choices better, or that endogenous sleep entry works. The curiosity-only route is undetermined because its route-specific positive control fails; the overall diagnostic still needs adjudication. [R6] |
| `V3-EXQ-1012c` reports `commensurate_at_eligibility_both_regimes`. | An existing channel-normalisation operator has a promising local validation result at the eligibility boundary. | Justification to build a duplicate scaler, or evidence that the resulting decisions improve viability. Diagnostic adjudication is pending. [R7] |
| Candidate effort is computed from `c.actions.shape[1]`, the common physical horizon in the registered defect. | A uniform effort term cannot discriminate candidates in that pool. | That predicted harm and effort are interchangeable quantities. [R8] |
| The `SD-033` audit identifies no driver for held-rule transfer to novel stimuli; its readout machinery already exists. | A specific untested functional signature. | That the whole prefrontal cortex cluster is absent or needs rebuilding. [R9] |

The evidence domains are the repository's existing D0-D7: instrument validity, local mechanism validity, local causal consequence, closed-loop behavioural consequence, ecological generalisation, developmental validity, integrated compatibility/simplification, and adaptive recovery. These are separate dimensions, not a scalar ladder. This thought generates no new experimental evidence. The new ranking-reach observation is, at most, provisional evidence of local causal consequence -- not organism-level benefit. [R10]

## 3. Define "working" before searching for the last piece

Three milestones should remain distinct.

**A. A minimally competent closed-loop agent.** In a declared small-world task, the agent learns something consequential, uses it to pursue goals and avoid hazards, and outperforms matched simple controls through its own executed actions. One convincing result earns competence in that task -- not robustness or general intelligence.

**B. An integrated functional organism.** The same functioning configuration retains competence through learning and sleep, handles predeclared changes in its environment, and does not require a different hand-tuned bundle for every successful demonstration. Its component contributions remain causally inspectable. Recovery is demonstrated where the substrate actually supports it.

**C. Strict version-three closure.** This remains the registered project commitment, not a new definition invented here. The version-three (V3) closure dashboard reports 72.3% weighted progress, 34 remaining nodes, and 11 assembly-frontier nodes excluded from the percentage. That is plan accounting, not "72.3% intelligent" or a completion-time estimate. Relative to the Sunday 19 July 2026 strict green-board benchmark, this snapshot does not establish closure. It makes some of the remaining scientific questions more precise. [R16]

A can be demonstrated before every item in C closes. B may expose additional interactions after A succeeds. Conversely, a greener administrative board does not independently establish either A or B.

## 4. The functional pieces and the evidence each must earn

The table is a dependency map, not a demand for eight new modules. Most rows already have substantial code, claims or experiments. They must be tested on a named configuration; a default-off implementation is neither absent nor automatically part of the functioning organism.

| Required function | Existing owners or surfaces | Next evidence needed | Interpretation of a valid null |
|---|---|---|---|
| **1. Consequential state and goal representation** | Observation-to-`z_world` encoder; `SD-106`; `MECH-567/568`; existing goal and resource paths | Held-out, task-relevant distinctions usable by actual bounded consumers, with other grounding capabilities preserved | Localise information loss, target mismatch, capacity or learning interference; do not buy more of the already-tested preservation budget |
| **2. Useful action-conditioned futures** | Deep predictive system (E1), fast forward predictor (E2), hippocampal proposer; `SD-PP-B5/B10`; `V3-EXQ-1082` | Actual-versus-swapped-action discrimination, appropriate baselines, and correct consequence contrasts at the horizon used for choice | Separate wrong operating point, wrong target, exposure and rollout drift; mere output spread is insufficient |
| **3. Consumer-specific access to those futures** | Existing proposer rollouts; candidate summaries; `SD-082`; mutual-legibility programme | Correctly paired content changes the intended consumer more usefully than mismatched, zeroed or distribution-matched controls | Distinguish absent content from bad indexing, unreadable coordinates, saturation or the wrong consumer |
| **4. Consequence-sensitive comparison** | E3 harm/benefit/goal/residue channels; existing commensurability operator; dorsal anterior cingulate cortex analogue; candidate-effort item | Meaningful candidate differences survive scaling and eligibility; harm, effort and goal trade-offs have the expected signs | Find uniform terms, duplicate costs, domination, timing errors or invalid semantics before adding another valuation module |
| **5. Commitment and effective action** | Selector, eligibility gates, commitment latch, motor execution; existing commitment-control claims | Changed evidence changes an executed first action when warranted, and the action improves an outcome | Locate where ranking, eligibility, latching, sampling or execution erased the effect |
| **6. Outcome learning and calibrated revision** | Waking updates; prediction errors; precision-provenance machinery; `SD-PP-1..4`; `SD-PP-B9/B11` | Reliable contradiction updates the relevant relation; noisy contradiction does not dominate; confidence predicts error on held-out experience | Revisit reliability estimation, attribution, plasticity and data support; confidence alone must not immunise a wrong model |
| **7. Retention and compatibility** | Memory, replay, sleep, write gates, shared-latent consumers; existing integration/deletion doctrine | New competence survives a sleep/learning cycle without unacceptable loss elsewhere; remove redundant compensations where possible | Diagnose interference or a missing developmental dependency; do not call all non-improvement a need for more replay |
| **8. Transfer and bounded recovery** | Existing ecological harnesses and organism-validation doctrine; `Q-108` as a later design seed | Competence survives held-out world changes; where permitted, the organism detects and recovers from mismatch without a supplied failure label | Retain the limited task-specific claim; expand the explanation if several repairs interact or the hypothesis partition misses the outcome |

### The dependencies are not one long queue

Representation and prediction quality constrain whether candidate costs have meaningful content. Consumer access and channel authority constrain whether that content can influence selection. Execution then determines whether a ranking difference becomes a world difference.

But instrument validity, candidate indexing, operating-mode occupancy and commitment timing can be inspected independently. A broken "when to commit" gate is not automatically explained by a world-model deficit. The existing commitment thought explicitly separates when, whether, and which candidates are eligible. [R14]

Likewise, the harm-prediction-error question and the world-action-readability question are related failure patterns, not the same experiment or the same proven cause. Solving one must not silently close the other.

## 5. Three distinctions that prevent an attractive but wrong repair

### 5.1 Difference, correctness and usefulness are different properties

A model can produce different predictions for different actions and still rank their consequences incorrectly. It can predict the next latent well by copying the current latent while missing the small difference that matters for action. It can improve an external readout without improving its installed consumer.

Each candidate therefore needs three questions answered:

1. Do the predicted futures actually differ under different actions?
2. Do those differences correspond to outcomes the actions really produce?
3. Does the organism use the relevant difference to make a better choice?

The latest margin-loss result makes this distinction immediately practical. It does not show that action-conditioned modelling is a bad idea; it shows why forcing separation is not a sufficient training objective. [R5]

### 5.2 Harm level, expected harm, surprise, uncertainty and effort are not one scalar

Harm level describes present/recent adverse state. Expected harm concerns a candidate future. Prediction error is the discrepancy between a forecast and what occurred. Predictor reliability concerns how much trust that forecasting process has earned. Effort concerns the resources or control required by an action or policy.

The B9 experiment concerns a harm-latent predictor and the meaning of its residual. It does not, by itself, validate a prospective harm-cost readout. An ensemble-disagreement signal might improve an uncertainty or surprise estimate without supplying either expected harm or effort.

The candidate-effort item currently points toward harm-forward rollout cost. Before implementation, establish what "effort" means in the test and whether that cost is already charged elsewhere. Otherwise a nonconstant replacement can fix argmin invariance while double-counting harm or testing the wrong construct. If the registered harm-forward design is retained, its competence dependency remains; an alternative effort definition requires an explicit design decision, not a silent substitution. [R8]

### 5.3 Uncertain danger must not automatically become cheap danger

The earlier shorthand that an unreliable harm forecast should simply "count less" is incomplete. Lower confidence in a hazard model does not establish safety. A suitable controller may investigate, shorten its trusted planning horizon, preserve alternatives, or apply conservative bounds.

Separate authority to update a belief, confidence in a prediction, and the cost of a possible adverse outcome. The current precision-provenance implementation already distinguishes historical and current confidence, but its global fallback and noise-subtraction assumptions are explicit limitations. They should not be described as fully calibrated, candidate-specific reliability. [R11]

## 6. The smallest convincing end-to-end demonstration

The following is a proposed assay family, not an allocated experiment identifier and not permission to bypass readiness gates.

### Initial task: one consequential choice

Use an existing, scope-compatible small world with two feasible routes to a resource. One route is locally attractive but has a delayed adverse consequence; the other trades a measurable cost against that consequence. The future distinction must be learnable from the permitted observation/history, and the planning horizon must contain it. If the environment cannot independently vary effort and harm, do not label this an effort experiment.

Begin with the competence and delayed-consequence slice. Add a held-rule transfer slice only after its own mode-occupancy and readout prerequisites pass. Do not demand that a first end-to-end test simultaneously validate every mechanism.

### Preflight: prove the event can be tested

- Reset on termination; exclude dead-agent rows and episode-crossing transitions where inappropriate. Record failed opportunities rather than silently replacing them.
- Freeze configuration, enabled flags, training exposure, seeds, task family and model/checkpoint identities. Distinguish the creature's configuration from the apparatus used to examine it.
- Verify at least two meaningful candidate alternatives and real post-action summaries; report empty buffers, constant readouts and fresh-selection counts explicitly.
- Demonstrate that the environment offers a real trade-off and that an evaluator-only positive control can detect it. Privileged environment state must never leak into the organism's inference or action policy.
- Predeclare the primary behavioural endpoint, practical effect-size threshold, uncertainty estimate, exclusion policy and decision rule. Treat episodes/seeds -- not correlated ticks alone -- as replication units.

### Controls and causal trace

Compare a frozen incumbent against the minimally changed candidate at matched training and evaluation budgets. Add a mechanism-specific lesion and a mismatched-content control. Where relevant, include a simple reactive/myopic control and a complexity-matched alternative; the point is to test the proposed contribution, not handicap the comparator.

Keep two instruments separate:

**A paired diagnostic** holds the experience stream constant and tests the internal handoff. It logs candidate identity, predicted consequence, uncertainty source, per-channel score, eligibility, preferred first-action class and action returned. A self-yoked unchanged control must reproduce the original result.

**An autonomous closed-loop evaluation** lets each arm execute its own choices and experience its own subsequent world. It tests resources obtained, avoidable harm, task completion and viability. A yoked trace alone cannot establish the benefit of actions that its comparison arm never executes.

For the forward-model slice, record both absolute outcome error and error relative to persistence; evaluate action contrasts and the deployed multi-step horizon. Latent scale and temporal smoothing must remain controlled. A changed baseline must not masquerade as improved predictive competence.

### Acceptance and failure interpretation

The first functional claim is earned only if the intact system improves the preregistered behavioural endpoint without violating harm/viability limits, and targeted disruption removes the predicted advantage while controls remain valid.

| Observed pattern | What to conclude next |
|---|---|
| Probe improves, native prediction/selection does not | The handoff remains unproven; inspect the actual consumer rather than declaring competence |
| Prediction and ranking change, executed actions do not | Inspect eligibility, commitment, sampling and the motor path |
| Actions change but outcomes do not improve | The information, objective, horizon or trade-off may be wrong; changing behaviour alone is not success |
| Outcome improves without the claimed internal mediator | Record a behavioural gain but reject or narrow that mechanism explanation |
| Intact and simpler/mismatched controls perform equally | Prefer the simpler explanation unless a distinct, preregistered phenotype separates them |
| The entire loop works in one task | Bank a scoped closed-loop result; then test retention, integration and ecological transfer |

A subsequent slice changes one unannounced environmental relation while keeping it observable. Recovery should be read against frozen-update and irrelevant-update controls, followed by retention and a second held-out perturbation. This is the intended direction toward a functional organism -- not an assertion that the present substrate can already perform it. The general adaptive-recovery question Q-108 remains version-four, substrate-conditional; its nearest V3-expressible slice must be routed through governance before commissioning. [R10, R12]

## 7. Concrete next sequence, with no duplicate work

### First: adjudicate the evidence already obtained

Resolve the current review list before allocating new work. It now includes V3-EXQ-1077, 1078, 1012c, 1081, 1080, 1082, plus the 1066 error. Diagnostic self-labels are not governance verdicts. In particular, 1078 has a vacuity flag and 1081 has a route-specific unmet precondition; do not award broad evidence credit from their overall PASS labels. Diagnose 1066 through the error workflow; any justified rerun gets a new letter. [R1]

Reconcile source records after those decisions. The world-forward-consumer entry still says there is no native route, while 1081 documents the indirect proposer route. The generated current-front page still contains older "queued/running" and re-pose-pending text despite the confirmed 23 September re-pose. Update the owners and then regenerate, not the generated headline by hand. This document does not perform those mutations. [R2, R6, R17]

### Second: stabilise one meaningful forward-model baseline

Adjudicate 1082 and reuse its evidence. Do not repeat 1079 or 1082 merely to prove that the alpha operating point and live-battery distinction matter. Do not carry the margin loss forward as if it had succeeded.

Determine whether the readable baseline remains useful at the actual deployed horizon and through the actual consumer. Reuse valid recorded material where it answers the question. The SD-PP-B10 encoder proposals remain registration-only; the new result is a reason to reassess their premise before commissioning construction, not blanket authority to implement them. [R5, R8, R13]

The separate encoder-to-consumer problem remains owned by `sd106_objective_consumer_transfer` and MECH-567/568. A task-aligned auxiliary target is a candidate test, not an established fix. Preserve the required grounding-head co-measurement and distinguish supervised diagnostic scaffolding from non-oracular learned competence. Do not reopen the closed extra-preservation-training branch or repeat the already-adjudicated whitening comparison as if it were untested. That negative was specific to the tested transformation against its standardised baseline, not every possible coordinate change. [R2, R18]

### Third: choose the next B9 discrimination after its ambiguous result is adjudicated

Record the persistence-relative gate and convergence probe as already completed. A source/readout comparison remains a reasonable next discriminator: residual-head error versus ensemble disagreement or an innovation-based statistic on the same recorded opportunities, with exposure matched.

Preserve the registered null concerning failure to separate the alternative from harm level, but do not mistake decorrelation from harm level for calibrated epistemic information. Add an independently scored outcome/learning-usefulness check to any subsequent claim of functional value. Ensemble agreement can also be wrong; innovation variance can contain noise.

If the alternatives remain uninformative, the representation/update-rate and exposure-coupling explanations remain available. A null does not uniquely choose between them. Retain an explicit outside-the-partition explanation if no proposed leg accounts for the pattern. No production harm-reliability module is authorised by this thought; SD-PP-B11 remains registration-only. [R3, R4, R8]

### Fourth: obtain one useful choice before multiplying downstream tests

Use the existing candidate-summary and channel-normalisation machinery where valid; adjudicate 1012c rather than rebuilding its operator. Test one actual consequence-sensitive route with the paired diagnostic plus autonomous outcome evaluation above.

Then implement candidate effort only when its semantics and producer are defensible, preserving default-off compatibility. Require within-tick candidate spread, correct trade-off behaviour and an attributable outcome -- not merely different score magnitudes.

The lateral prefrontal cortex held-rule experiment can be prepared independently, but may run only once its competence, mode-occupancy and candidate-readout prerequisites are met. Reuse the existing trained-head and post-action-summary infrastructure. Compare rule-enabled, E3-alone and frozen-head arms; score novel-stimulus transfer, not another copy of the distractor-resistance result. A pass would credit the lateral rule-transfer function, not the entire subdivision architecture. [R7-R9]

### Fifth: retain, transfer, simplify

Once a scoped closed-loop improvement exists, test it after learning/sleep, across a frozen ecological change, and in the assembled bundle. Remove one repair at a time or replace it with a simpler mechanism at matched budget. A repair made redundant by an upstream fix should be removable.

Developmental necessity requires comparisons at matched final capacity and training budgets; success after a mature-agent patch is not evidence that its developmental history was adequate. These are already part of the organism-validation doctrine, not new requirements invented here. [R10]

### Explicit do-not-repeat list

- V3-EXQ-1077: already ran; ambiguous, not missing.
- V3-EXQ-1079/1082: operating-point probe and live-battery revalidation already ran. Reuse/adjudicate before any successor.
- V3-EXQ-1080: records a contamination/truncation scoping result with a "no reruns owed" self-route; adjudicate it rather than launching blanket repeats.
- V3-EXQ-1062b as another same-claim dose, schedule or window rescue: refused by the confirmed autopsy.
- MECH-018 / EXP-0755 and MECH-154 / EXP-0361: blocked on named substrate, not new ready experiments.
- SD-ZWORLD-SENSE-PATH-PARITY: do not restore the withdrawn build; the original gap did not reproduce.
- sd105_frozen_shared_entropy_floor_multiplier: registration-only.
- Generic SD-081 confirmation: first examine the existing V3-EXQ-811a evidence and exact claim scope; zero evidence credited to the design identifier does not mean nothing relevant ran.
- The new affordance bridge ARC-149, arousal eligibility-breadth claim MECH-580, and general recovery question Q-108: registered later-version proposals, not implicit additions to the immediate V3 build list. [R3, R8, R12, R15]

## 8. What is genuinely new here, and what is already owned

| Formulation | Relationship to existing work |
|---|---|
| Information must reach the real consumer | Already owned by mutual legibility, causal reach and the organism-validation doctrine; no new omnibus "legibility module" claim warranted |
| Representation must preserve action consequences relevant to choice | Already covered by world-model, objective-transfer and affordance thoughts; this document connects their tests |
| Sleep should preserve provenance and calibrate future learning | Already developed in the 22 September precision-provenance thought and `SD-PP-1..4`; not a new sleep proposal |
| Distinguish reach from benefit on the now-demonstrated world-forward route | A current evidence synthesis that changes the next decision; does not introduce a new mechanism |
| Separate the three ready items from the full organism path | The principal planning contribution of this document |
| Pair internal causal tracing with autonomous outcome evaluation on one configuration | A concrete assay proposal implementing existing evidence-domain discipline |
| Keep effort, harm prediction and epistemic reliability distinct at the integration boundary | An explicit design safeguard prompted by the present workset; route to existing owners before considering a new claim |

The September mutual-legibility thoughts already warned that channel dependence is not content dependence and that a bridge can become an extra computing system rather than an explanation. The affordance thought explicitly says it is design-generative, not an instruction to modify V3. This document preserves those limits. [R14]

## 9. Literature anchors: useful constraints, not validation of REE

These are focused primary-source checks, not an exhaustive literature review. The source abstracts establish the narrow contributions described here; the REE implications are design inferences.

**Grimm and colleagues (2020), value equivalence.** Their model-based reinforcement-learning formulation defines equivalence relative to policies and value functions, motivating models useful for planning rather than faithful reconstruction of everything. REE inference: ask whether the representation preserves consequential choices. This does not licence discarding information required by other consumers of a shared latent. [L1]

**Janner and colleagues (2019), model usage.** Their analysis and experiments motivate short model-generated rollouts branched from real experience to balance model utility against error. REE inference: validate the horizon the organism actually uses and consider bounded model trust. The result does not select an optimal horizon for REE or justify abandoning its multi-step planning commitment. [L2]

**Pathak, Gandhi and Gupta (2019), ensemble disagreement.** They use disagreement among dynamics models as a self-supervised exploration signal, including stochastic domains. REE inference: disagreement is a credible rival to raw residual error for a bounded diagnostic. It is not automatically a calibrated harm-reliability estimate, a prospective harm forecast, or an effort cost. [L3]

**Keramati and Gutkin (2014), homeostatic reinforcement learning.** Their normative model links reward seeking to physiological regulation under its stated assumptions and describes anticipatory responses to homeostatic challenges. REE inference: a functional-organism evaluation should include maintained viability and consequences, not only action diversity or score movement. It does not prove that REE's particular affective architecture is necessary. [L4]

## 10. What would change this map?

The path is deliberately revisable.

- If readable, accurate candidate consequences reach selection but behaviour remains poor, the dominant bottleneck may be the objective, action repertoire, commitment regime or ecology -- not communication.
- If a simple direct policy matches the complete preregistered phenotype at matched capacity and budget, a proposed intermediary has not earned its complexity. Do not protect it by moving the test afterward.
- If the repairs work separately but not jointly, integration or learning interference becomes the next question.
- If success requires privileged labels at deployment, manually supplied failure identity, or continual experimenter retuning, record a scaffolded demonstration rather than autonomous competence.
- If multiple causes coexist, abandon the assumption of one last missing piece. Expand or re-pose the hypothesis partition before another rescue experiment.
- If a competence loss can be removed by deleting a subsystem, that is positive progress, not a defeat for the programme.

The decisive near-term observation would be modest but substantial: a previously learned consequence makes the organism choose better in an untrained situation; a targeted intervention removes that advantage; and the advantage survives a relevant learning or sleep cycle. Ecological generality and autonomous recovery would still require their own evidence.

We know how to make the next successes more meaningful. We do not yet know that they exhaust the remaining problems. That is the defensible technical content of "close."

## Sources and provenance

Repository links are pinned to the inspected commits. The diagnostic records are cited as recorded results, with pending adjudication stated above. No experiments were run, claim statuses changed, or work items queued while producing this document.

- R1 -- Live workset and review mismatch: workset; pending review.
- R2 -- Encoder transfer and resolved re-pose: confirmed 23 September re-pose; objective-transfer mechanisms. The latter retains historical framing; the confirmed re-pose and current registry take precedence.
- R3 -- Harm-forward failure and refusal: V3-EXQ-1062a autopsy.
- R4 -- Converged harm-head ambiguity: V3-EXQ-1077 record.
- R5 -- Live-battery world-forward revalidation: V3-EXQ-1082 record; driver.
- R6 -- Native route and sleep-sized ranking reach: V3-EXQ-1081 driver, including premise correction and yoked design; record.
- R7 -- Existing channel operator: substrate record; V3-EXQ-1012c result.
- R8 -- Candidate effort and build boundaries: agent code; substrate queue, especially sd032b-candidate-effort-proxy, SD-PP-B1/B5/B9/B10/B11, parity and entropy-floor records.
- R9 -- Rule-transfer gap and existing repair: claim registry, SD-033; SD-082 post-action-summary amendment.
- R10 -- Organism-level jurisdiction and validation: architecture anchor; detailed doctrine.
- R11 -- Precision already built, with limitations: world-forward epistemic precision; provenance-conditioned consolidation.
- R12 -- Version and ownership boundaries: current claim registry, especially ARC-149, MECH-580, Q-108, MECH-163/478/479. Current claim-specific scope supersedes older broad module summaries.
- R13 -- Operating-point and dead-agent-battery correction: confirmed V3-EXQ-1079 autopsy.
- R14 -- Prior thoughts: mutual-legibility implications, 7 September; affordance and valuation, 18 September; action-conditioned modelling and commitment, 22 September; behavioural precision provenance, 22 September.
- R15 -- Blocked and previously tested work: experiment proposals; claim registry, MECH-163 and V3-EXQ-811a history; V3-EXQ-1080 record.
- R16 -- Closure accounting: 24 September closure dashboard.
- R17 -- Generated front, with stale source text: CURRENT_FRONT.
- R18 -- Scope of the whitening negative: confirmed V3-EXQ-1065 autopsy.
- L1: Grimm, C., Barreto, A., Singh, S. P., and Silver, D. (2020). The Value Equivalence Principle for Model-Based Reinforcement Learning. Advances in Neural Information Processing Systems 33.
- L2: Janner, M., Fu, J., Zhang, M., and Levine, S. (2019). When to Trust Your Model: Model-Based Policy Optimization. Advances in Neural Information Processing Systems 32.
- L3: Pathak, D., Gandhi, D., and Gupta, A. (2019). Self-Supervised Exploration via Disagreement. Proceedings of Machine Learning Research 97, 5062-5071.
- L4: Keramati, M., and Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. eLife 3:e04811. https://doi.org/10.7554/eLife.04811.

## Possible affected components

Observation and latent encoding; E1/E2 forward modelling; hippocampal proposal, retrieval and replay; candidate summaries; E3 scoring and eligibility; harm, benefit, goal and effort readouts; commitment and motor execution; precision provenance and plasticity; sleep and retention; developmental and ecological validation; evidence interpretation and workset freshness.
