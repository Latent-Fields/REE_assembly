# Interpreting V3-EXQ-700 failure: loop decomposition, granularity, and residual missing pieces

Status: processed
Processed in:
- `docs/claims/claims.yaml` (thought-intake REAP: MECH-451, MECH-452, MECH-453 (V3-EXQ-700 failure interpretation / loop decomposition). This file is cited in those claims' `sources`.)



## Digestion record (2026-06-23)

This doc is a forward-interpretation aid for **V3-EXQ-700** (the ARC-108 JOB-1 learned-gating
selection 2x2 falsifier, queued 2026-06-22, not yet run). Most of its candidate claims were
**already reaped into the registry the same day** (the assembly-map intake-reap):

- Separate motor / cognitive / motivational loops -> **ARC-110** (its falsifier *is* V3-EXQ-700).
- Context-conditioned weights -> **ARC-111**.
- D1/D2 population split -> **ARC-109**.
- Recurrent settling step -> **MECH-450**; F-dominance ceiling -> **MECH-439**; unified dopamine
  substrate -> **ARC-108**.
- Candidate-generation bottleneck -> already covered by GAP-A / ARC-065 / MECH-313.
- The inference rule ("a preconditions-met failure shifts uncertainty toward ARC-110/ARC-111, not
  away from ARC-108") -> already encoded in `ARC-110.what_would_answer` + `ARC-108.depends_on`
  (the ARC-110 sequencing fork). The **result-interpretation matrix** below remains the durable
  decision aid for when V3-EXQ-700 returns.

Three genuinely-new residue ideas were **registered this pass** (user-approved):

- **MECH-451** -- intermediate channel-granularity falsifier (expose finer score_bias channels to
  the learner BEFORE the full ARC-110 loop build). V3-tractable; proposal **EXP-0391** minted.
- **MECH-452** -- loop-local eligibility traces under a globally-broadcast dopamine signal (V4).
- **MECH-453** -- cholinergic TAN-pause plasticity-window gating of selector credit (V4).

All three stay `candidate` / `substrate_conditional`; PROMOTES NOTHING.

## Source thought

> What do you think is missing? Or do you think much of the 40% chance this round doesn’t succeed is absorbed by the likely three loop decomposition needed?

## Context

V3-EXQ-700 tests whether learned dopamine-gated channel weights (`w_chan`) and learned recurrent lateral inhibition (`W_lat`) can overcome the MECH-439 F-dominance ceiling inside the current collapsed E3 selector arena. ARC-110 already records the possibility that motor, associative/cognitive, and limbic/motivational cortico-basal-ganglia-thalamic loops need to be represented as distinct competitions rather than as bias channels summed into one global selector. ARC-111 separately records the possibility that learned weights must be context-conditioned rather than globally fixed.

The question is how to interpret a preconditions-met failure of V3-EXQ-700. Such a failure would not necessarily mean that dopamine-gated learning is the wrong principle. It may mean that the principle has been inserted at the wrong representational granularity.

## Working interpretation

A substantial share of the current failure probability is plausibly absorbed by the collapsed-loop design, but not all of it.

A rough causal attribution is:

```text
P(this round fails) ≈ 0.35–0.45

of that failure mass:

~50–65%  collapsed loops / coarse channel aggregation
~15–25%  context-independent weights and credit assignment
~10–20%  learning-signal or eligibility-trace mismatch
~5–15%   assay, curriculum, or non-vacuity problems
```

These categories overlap and should not be treated as a clean additive statistical model.

## Main candidate missing piece: separate loops

The current system asks one shared selector arena to perform several distinct functions at once:

- motivational valuation;
- cognitive or rule-based control;
- motor/action execution;
- conflict monitoring;
- persistence and release.

In the current implementation, dACC-, lateral-PFC-, OFC-, liking-, curiosity-, vigour-, and route-related influences enter one arena as biases. A single learned weight vector is therefore asked both to determine what is motivationally important and to determine which action should execute.

A more faithful decomposition would allow:

```text
within-loop competition
→ loop-specific winner or state
→ cross-loop arbitration / coordination
→ action commitment
```

This could prevent motivational, cognitive, and motor signals from contaminating one another inside a single F-dominated competition.

If V3-EXQ-700 shows that learning is active but behavioural conversion remains absent, the leading interpretation should become:

```text
shared_arena_interference
+ missing_within-loop_competition
+ missing_cross-loop_arbitration
```

This would justify pulling ARC-110 forward rather than weakening ARC-108 by default.

## Closely related: channel compression

The current `score_bias` channel compresses several distinct control functions before the learning rule sees them. The learner may therefore be unable to discover separately that:

- OFC devaluation matters in one state;
- dACC conflict matters in another;
- lateral-PFC rule evidence should dominate in a specific phase;
- motivational value should alter persistence rather than motor choice;
- motor vigour should alter execution without changing valuation.

An intermediate architecture between one global selector and full anatomical loop decomposition may be:

```text
one_global_weight_vector
→ finer_exposed_channels
→ loop-specific_weight_vectors
```

This may be enough to test whether the key failure is representational compression before implementing the complete loop architecture.

## Context-conditioned weights

A fixed global weight is only appropriate if a channel has the same relevance across all states. In REE, the appropriate influence of harm, benefit, novelty, rule evidence, urgency, and social value likely depends on:

- current goal;
- threat state;
- uncertainty;
- deliberation versus execution;
- behavioural phase;
- remembered context;
- recent success, frustration, or devaluation.

A global learned weight may average across incompatible contexts:

```text
useful_in_context_A
+ harmful_in_context_B
→ average_weight_near_zero
```

This could make dopamine-gated learning appear ineffective even when the underlying rule is correct. A preconditions-met failure with strong weight movement but poor behavioural lift should therefore increase the priority of ARC-111.

## Other missing pieces not fully explained by loop decomposition

### D1/D2 population split

Go and No-Go are still represented largely as scoring directions rather than as separate populations with opposite dopamine sensitivity. The current asymmetric update may be sufficient for V3, but may not generate the required opponent dynamics under negative reward-prediction error, reversal, or changing motivational state.

### Local eligibility traces and credit assignment

The same signed reward-prediction error currently drives both channel-weight and lateral-settling updates. The teaching signal may be shared globally, but the credit traces probably need to remain local and loop-specific:

```text
shared dopamine signal
× separate local eligibility traces
× loop-specific active synapses
```

A failure could therefore arise because the learning principle is right but the eligibility trace is too broad or temporally smeared.

### Reward target and temporal contrast

`R_t = benefit_eval - harm_eval` is coherent, but the trained heads may not yet expose the exact consequence needed for selector learning. Reward may be delayed, sparse, or insufficiently differentiated across candidate classes.

A negative result could therefore mean:

```text
no useful teaching contrast
```

rather than:

```text
dopamine-gated gating is wrong
```

### Plasticity-window gating

A cholinergic TAN-pause-like mechanism is absent. Dopamine should probably not update every recently active selector component continuously. A narrower plasticity window may be needed to prevent credit smearing.

### Candidate-generation limits

Perfect selection cannot choose an option that is not represented distinctly enough. If candidate trajectories are highly correlated, or their summaries do not expose the relevant behavioural distinction, learned gating may move while conversion remains impossible. This would place the bottleneck upstream of basal-ganglia selection.

## Result interpretation matrix

| V3-EXQ-700 result | Leading interpretation |
|---|---|
| `w_chan` and `W_lat` change, but no behavioural lift | Collapsed-loop interference, coarse channels, or missing context conditioning |
| Signed and unsigned reward-prediction error perform similarly | Direction is not load-bearing here, or the assay lacks positive/negative teaching contrast |
| Signed beats unsigned, but still no conversion | Learning is real; representation or loop structure is limiting |
| `w_chan` helps, settling does not | Learned reweighting is primary; recurrent settling is unnecessary or poorly represented |
| Settling helps, `w_chan` does not | One-shot selection was the bottleneck; fixed channel mixture may be adequate |
| Combined arm performs worse than either alone | Strong evidence for interference inside the shared arena |
| Learned variables do not move meaningfully | Teaching signal, traces, reward contrast, or implementation non-vacuity problem |
| Weights move strongly but collapse onto one channel | Missing context conditioning, regularisation, or homeostatic control |
| Training improves but reversal fails | Fixed weights or slow traces; ARC-111 becomes more likely |

## Candidate inference rule

> If V3-EXQ-700 fails despite demonstrably active, direction-sensitive learning, then most remaining uncertainty should shift toward ARC-110 and ARC-111 rather than away from ARC-108.

The loop-decomposition hypothesis is not an after-the-fact rescue. It is already a registered architectural fork with a predicted symptom: learned gating inside one collapsed arena may remain unable to overcome F-dominance.

The current uncertainty is better represented as:

```text
10–15%  learning rule or teaching signal itself insufficient
20–25%  correct learning principle, wrong granularity or loop architecture
5–10%   experiment or developmental substrate fails to expose it
```

## Candidate claims / implications for later adjudication

- Distinct motor, cognitive/associative, and motivational loops may be required for learned gating to become behaviourally effective.
- Learned channel weights may need to be context-conditioned rather than globally fixed.
- Separate loop-local eligibility traces may be required even when dopamine is globally broadcast.
- Strong parameter movement without behavioural conversion should count as evidence against representational granularity, not automatically against the learning rule.
- A combined learned-weight plus learned-settling arm performing worse than either arm alone would be positive evidence for shared-arena interference.
- Finer channel exposure may provide an intermediate falsifier before full three-loop decomposition.

## Open questions

- What exact non-vacuity evidence is required before interpreting failure as architectural rather than implementation-level?
- Should finer channel separation be tested before full ARC-110 loop decomposition?
- What context variables should condition ARC-111 weights?
- Should eligibility traces be separate by loop, by channel, by action class, or by synapse-like connection?
- How should cross-loop arbitration occur without recreating a second collapsed global arena?
- Which reversal or context-switch assay would best distinguish fixed weights from context-conditioned weights?

## Possible affected components

- ARC-108 unified dopamine substrate
- ARC-110 parallel segregated loops
- ARC-111 context-conditioned weights
- MECH-439 F-dominance / conversion ceiling
- MECH-450 learned recurrent settling
- E3 selector channel representation
- reward-prediction-error and eligibility-trace design
- candidate generation and candidate-summary representation
- V3/V4 sequencing decision
