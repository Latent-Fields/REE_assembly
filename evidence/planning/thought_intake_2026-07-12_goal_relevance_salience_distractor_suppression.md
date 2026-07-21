# Thought Intake — Goal relevance, salience, and distractor suppression

**Date of thought:** 2026-07-12
**Intake written:** 2026-07-21
**Raw thought file:** `docs/thoughts/2026-07-12_goal_relevance_salience_and_distractor_suppression.md`
**Session:** `sad-newton-00451d` (thought-intake ingestion, 2026-07-21)
**Source:** report on brainstem neurons controlling attention by suppressing competing distractors
**Status:** structured intake written; candidate claims NOT yet registered (concurrent session held the `claims.yaml` claim).
**Promotes/demotes:** nothing.

## Authorship note

The raw thought is the user's, including its own repository-grounded correction (the paper does not introduce distractor suppression to REE — REE already has it, distributed). This intake adds the claim-level cross-reference, isolates what is genuinely unowned, and routes.

## Already owned — cross-reference, do NOT re-assert

This lands squarely on ground the 2026-06-04 attention analysis already mapped: **REE-v3 attention is distributed precision-selection control, not a missing module** (`docs/thoughts/2026-06-04_attention_distributed_precision_selection.md`). The raw thought reaches the same conclusion independently, which is a useful convergence but not new registrable content.

| Element in the thought | Existing claim(s) |
|---|---|
| Rule-state protection / persistence through distractors | **SD-033a** (lateral-PFC analog), **MECH-262** (rule-selective, distractor-resistant persistence) |
| Mode-conditioned write gating | **MECH-261** (generalises MECH-094) |
| Salience-network switching / mode control | **MECH-259**, **SD-032a** |
| Precision / top-down template routing | **ARC-005**, **MECH-251** (`z_goal` precision template via `dan_feedback`) |
| E3 boundary top-k latent selection (attentional bottleneck) | **MECH-254** |
| Goal-directed template compilation | **MECH-255** |
| Object-bound incentive salience + cue-driven capture | **SD-057**, **MECH-347** |
| Task-set / rule apprehension | **ARC-062**, **ARC-063** |
| Distractor-resistance already TESTED | **V3-EXQ-484** (salience-coordinator gating protects rule state from replay drift) |
| WM decay under distractor/horizon/effort load | the Q-080 effort-dissociation line (already has a non-degeneracy precondition on bare-goal load) |

The goal-relevance-vs-salience distinction the thought draws is **already architecturally instantiated** (`z_goal` / `z_resource` / predictive wanting / affordance bias on one side; salience coordinator / operating mode / dACC / urgency interrupt / mode hysteresis on the other). Do not register it as a new claim; it is a good glossary entry.

**Standing containment rule (carried over from the 2026-06-04 analysis, still in force): do NOT add a generic attention module, and do not expand the V3 green-board closure path.** A new attention substrate is justified only if an experiment exposes a *specific* failure. The material below is written to respect that.

## Genuinely new — three things

### N1. The three-way distractor-failure taxonomy, and the observation that REE's evidence covers only one leg

The sharp contribution. Three distinct failures:

1. **Sensory capture** — the distractor enters or dominates the active representation.
2. **Rule corruption** — the distractor overwrites or destabilises the active goal/rule/task context.
3. **Behavioural capture** — the rule survives intact, but the distractor still controls action selection.

REE's distractor evidence (V3-EXQ-484, MECH-262) is **rule corruption only**. Legs 1 and 3 are untested. Leg 3 is the one that matters most for the containment rule above, because it is precisely the failure that *rule-state protection cannot catch by construction* — an intact rule that fails to steer action is invisible to a rule-drift metric.

This is a coverage gap in the existing claim set, not a new mechanism. It is the cheapest genuinely-new thing here.

### N2. Pre-selection suppression as a distinct architectural level

> Does REE suppress distractors before selection, or mainly preserve higher-level state after distraction occurs?

REE's mechanisms are predominantly *post-entry*: write gating, persistence, conflict handling, mode hysteresis. The brainstem/superior-colliculus result points at suppression of competing **orienting or target-selection signals before they acquire behavioural control**. Whether REE needs an explicit pre-selection substrate, or whether existing precision-weighted cue routing plus MECH-254's top-k bottleneck already suffices, is an open architectural question — and per the containment rule, the default answer is "sufficient until a specific failure says otherwise."

Note the honest framing: this is `complex (probe-gated)`. The probe is N1 leg 3 (behavioural capture). Only a behavioural-capture failure that survives ablation of the existing mechanisms would justify a pre-selection substrate.

### N3. Distractor suppression is an **ethical** control problem, not only a performance problem

The strongest and least-anticipated move in the thought:

> In REE, weak or unexpected signals may carry morally relevant information.

An adequate suppressor must distinguish four things that all present as "input competing with the current goal":

- irrelevant distraction (suppress),
- legitimate interruption (allow),
- urgent harm signal (must override),
- another agent's state becoming newly relevant (must override, and is the hardest).

This makes over-suppression a **safety failure mode**, not merely a rigidity cost — a well-tuned distractor suppressor that improves benchmark scores by silencing weak signals is exactly the thing that would silence a weak harm cue. It connects the attention line to the ethics perimeter and to the harm-stream priority machinery, and it supplies the correct acceptance shape for any future suppression mechanism: **PASS requires improved goal completion under distractor load AND preserved interruptibility by harm/other-agent signals.** A single-axis attention score cannot express that, which is why the thought insists the measurement panel not be collapsed.

## Candidate claims (for registration at digestion)

1. **Distractor resistance has three dissociable failure modes; REE's evidence covers only rule corruption.** *Candidate, diagnostic/coverage.* Sensory capture, rule corruption and behavioural capture are dissociable, and a system can pass rule-corruption tests while failing behavioural capture. *Falsifier:* a distractor battery instrumented for all three separately — sensory-capture rate (distractor present in active representation), rule-state drift, wrong-target selection rate with rule verified intact. PASS for dissociability requires at least one condition where rule drift is at floor while wrong-target selection is elevated. *Non-degeneracy guard:* the distractor must actually be registered by the system (non-zero sensory-capture rate in at least one arm) — a distractor the agent never encodes tests nothing, and an all-floor battery self-routes `substrate_not_ready`. *Type:* diagnostic over existing substrate. *Cross-ref:* MECH-262, SD-033a, MECH-261, V3-EXQ-484, MECH-254.

2. **Suppression must be selectively permeable to harm and other-agent signals (ethical interruptibility).** *Candidate, INV/SENT-flavoured.* Any distractor-suppression mechanism must preserve the ability of sufficiently important weak evidence to interrupt an established rule or commitment; suppression strength that improves goal completion by silencing weak harm cues is a failure, not a success. *Falsifier:* paired measurement — goal completion under distractor load AND interrupt latency/rate for an injected weak harm or other-agent-urgency signal, across a suppression-strength sweep. FAIL if the suppression setting that maximises completion also measurably degrades harm interruptibility. *Non-degeneracy guard:* the harm-interrupt channel must be demonstrably live at zero suppression (baseline interrupt rate well above floor). *Type:* invariant / governance-adjacent constraint on a future mechanism. *Cross-ref:* the harm-stream priority claims (SD-010, SD-011, ARC-027), urgency interruption, ethics perimeter (SENT-*/GOV-*), EXT-009.

3. **(Deferred, probe-gated) Pre-selection suppression requires an explicit substrate.** *Candidate — register only as a `substrate_conditional` open question, explicitly gated on candidate claim 1 leg 3.* Do NOT register as an assertion and do NOT build. *Cross-ref:* MECH-254, ARC-005, MECH-251, SD-057/MECH-347.

**Explicitly not proposed:** a general attention architecture, a named distractor-suppression module, or any change to the V3 critical path. The thought says so itself; the containment rule says so independently.

## Routing

- **Benchmark family, not a subsystem.** The noisy-environment benchmark (distractor classes: physically salient irrelevant cues, same-type object distractors, false affordances, misleading reward-proximal cues, competing orienting targets, repeated interruption cues, and — importantly — distractors introduced *before commitment*, *during commitment*, and *during replay/planning*) is the durable artifact here. It answers the thought's own open question 7 ("which existing REE claim should own this benchmark family?"): **MECH-262 owns rule corruption; legs 1 and 3 need a new owner**, and candidate claim 1 is that owner.
- **Sequencing.** Candidate claim 1 is queueable now in principle, but the pre-commit/during-commit/during-replay distractor timing conditions are the interesting ones and depend on stable commitment behaviour. Check against the standing constraint that the substrate cannot sustain multi-step commitment before designing the during-commitment arm.
- **Literature:** the five targeted questions form a `/lit-pull` brief. The load-bearing one is *brainstem / superior-colliculus competition — at what stage does suppression occur* (sensory representation vs orienting command vs target competition vs motor output), because it determines whether N2 is even a distinct level or a re-description of MECH-254's bottleneck.
- **Ethics cross-link:** candidate claim 2 should be visible from the ethics perimeter plan, not filed only under attention.

## Next steps

1. Register candidate claims 1–2 (and 3 as a gated open question) in `claims.yaml`. **Deferred from this session.**
2. Mark the raw thought `Status: processed` once (1) lands.
3. `/lit-pull` on the suppression-stage question.
4. Scope the three-leg distractor battery against existing telemetry before queuing anything.
