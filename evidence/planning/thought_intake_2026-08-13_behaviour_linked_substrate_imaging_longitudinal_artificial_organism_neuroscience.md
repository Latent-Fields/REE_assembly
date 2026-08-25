# Thought intake — behaviour-linked substrate imaging and longitudinal artificial-organism neuroscience

**Date:** 2026-08-25T20:50:35Z
**Raw thought:** `docs/thoughts/2026-08-13_behaviour_linked_substrate_imaging_longitudinal_artificial_organism_neuroscience.md`
**Session:** loop-ti-behav-imaging-k80npe (`/thought-ingestion`, non-interactive, single-thought pass)

## Verbatim prompt

The raw thought's originating line: "I wonder about applying some brain scan like behavioural
analysis. We could look at what activity in r e substrate is associated with what behaviour.
Extending temporally and associative."

Unpacked, the proposal is: build a synchronised, timeline-shared visualisation of Fishtank
behaviour and internal REE substrate activity (a "brain map" for REE, with intensity/colour/
pulsing/size/connection-change/background-drift channels tied to explicitly documented recorded
variables — never to what the architecture is "supposed" to do); use it first for **event-related**
analysis (align substrate state around behavioural events — reef departure, food approach, harm,
sleep, goal abandonment, etc.); extend the alignment window across many **temporal offsets**
(`substrate(t-1)`, `t-10`, `t-100`, `t-1000` -> `behaviour(t)`), not only the immediate surround;
treat **distributed multivariate substrate-state patterns**, not single variables, as the unit of
analysis, including representational-similarity-style comparisons across behaviour/location/goal/
history/age/outcome; run this **longitudinally across a whole REE lifetime** to see whether
internal-behavioural signatures stabilise, shift, or diverge with development; and move from
correlation to **causation** using checkpoint branch-and-replay (perturb a candidate mechanism,
restore a checkpoint, replay the environment, compare a matched unperturbed sibling branch) —
summarised by the thought as **observe -> associate -> hypothesise -> intervene -> replay ->
adjudicate**. A second explicit thread: human parallel *visual* processing is proposed as a
high-bandwidth **hypothesis-generation** instrument (not evidence) precisely because it can absorb
far more simultaneous signal than serial logs/plots/summaries — with an explicit **apophenia
safeguard** (documented variable mappings, raw data authoritative, visual read is observation/
hypothesis only, quantify before believing, confirm on held-out lifetimes, require intervention
for causal claims).

## What's new vs. existing REE docs/claims

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| A synchronised behaviour+substrate observability *instrument* (dual-panel Fishtank + substrate map, shared timeline, documented visual-channel mappings) | No claim proposes this. `Fishtank` exists as the behavioural environment/showcase (`failure_autopsy_V3-EXQ-916-916a-917-920-fishtank-cluster`, `V3-EXQ-664` affective showcase) but has no internal-state-visualisation counterpart in the registry. `feedback_whimsy_visualization` (project memory) records that the *existing* embodied Fishtank visual read already surfaced the z_harm_a saturation finding before scalar metrics did (claims.yaml line ~79482 notes on the reaped z_harm_a-readout candidate) — real informal precedent that the instrument class works, but not itself a registered architectural/tooling claim. | **Genuinely new** -> register (`GOV-SUBIMG-1`) |
| Explicit "never animate what the architecture is *supposed* to be doing" discipline (visual property <-> recorded variable/transformation, documented and mechanical) | Not covered by any existing claim as a standing rule for a visualisation instrument specifically; the closest structural relative is the general triangulation principle in `GOV-INTRO-1` ("[a hypothesis-generation source] never validates alone") and `GOV-BEHADJ-1`'s discovery-vs-confirmation separation. | Folded into `GOV-SUBIMG-1` as the instrument's own governing discipline, citing the two existing principles rather than re-deriving a third one. |
| Human visual parallel processing as high-bandwidth hypothesis generation; division of labour (visual detection -> quantitative reproducibility test -> causal intervention) | **Already owned.** `GOV-BEHADJ-1` ("umpire, not ruler") already requires discovery-oriented analysis run *alongside* pre-specified hypothesis-directed measures, with strict separation of discovery from confirmation, for organism-level behavioural interpretation — and its own lit-pull note (claims.yaml ~82869) explicitly names "the researcher's own first unblinded visual read of a Fishtank trajectory" as the real contamination point, citing Lit et al. 2011's Clever-Hans replication. `GOV-INTRO-1` is the general triangulation rule this specialises for a different origin class (introspection there, visual pattern-noticing here). | **Already-owned** -> cross-reference only, no new claim. |
| Apophenia risk / epistemic safeguard on the visualisation itself | **Already owned**, same two claims as above. `GOV-BEHADJ-1`'s lit-pull already establishes that blinding-at-scoring-time is *necessary but demonstrably insufficient* (the contamination happens at the researcher's real-time read, before any blind scoring step), which is a stronger and better-evidenced version of the raw thought's own six-point safeguard list. | **Already-owned** -> cross-reference only; the safeguard belongs to `GOV-BEHADJ-1`/`GOV-INTRO-1`'s existing discipline, extended (not re-invented) to cover substrate-visual reads, not only behavioural-trajectory reads. |
| Event-related alignment of substrate activity around discrete behavioural events (across event types, across repeated occurrences, across organisms) | No existing claim proposes this as a general *method*. Many individual mechanism claims describe specific substrate responses to specific events (e.g. harm-onset dACC/PAG dynamics, sleep-onset consolidation triggers), but none proposes the general event-related-analysis technique itself, applicable across arbitrary event types. | **Genuinely new** -> register (part of `GOV-SUBIMG-2`) |
| Sweeping the analysis across a temporal-offset ladder (`t-1` … `t-1000`+), not only the immediate surround | No existing claim. Residue/consolidation claims (e.g. `INV-099` residue continuity, `MECH-204` sleep-linked precision recalibration) assert that consequences *persist* over time, but none proposes the temporal-offset-sweep *method* for detecting how far back a predictive association extends. | **Genuinely new** -> register (part of `GOV-SUBIMG-2`) |
| Distributed / multivariate substrate-state pattern analysis (representational-similarity-style), without pre-imposed behavioural labels | `representational-similarity` appears twice in the registry (claims.yaml ~20518, ~83733) but only as a suggested *confirming-signature test* for other, narrower claims (e.g. MECH-495's environment-conditional memory-dimensionality claim) — never as a standing general analysis method in its own right. | **Genuinely new** as a general method -> register (part of `GOV-SUBIMG-2`) |
| Longitudinal artificial-organism neuroscience across development (signature stability, emergent associations, individual developmental-history effects) | The `development.*` subject area has many claims about developmental *stages and mechanisms* (e.g. curriculum, maturation), and `ARC-...` "preservation for future reconstruction" (claims.yaml ~83299) is about preserving developmental history at *end of life* — orthogonal, not the same proposal. No claim proposes tracking internal-behavioural *signature stability* longitudinally as an analysis method. | **Genuinely new** -> register (part of `GOV-SUBIMG-2`) |
| Causation via checkpoint branch-and-replay (branch a checkpoint at a developmental age, perturb, compare to a matched unperturbed sibling) | The **substrate precondition is already explicitly flagged as unmet**, in `ARC-124`'s own `what_would_answer`: "V3 checkpoints exist but nothing forks a running agent, so there is no branch to reason about." `ARC-124`/`ARC-125`/`SD-095`/`SD-096` cover the **ethics and governance** of branching (successor standing, commitment inheritance, provenance ledger) *once forking exists* — none of them treats branching as an **experimental technique** for causal confirmation. | **Adjacent-but-distinct** -> register narrowly (part of `GOV-SUBIMG-2`), explicitly citing `ARC-124`'s substrate precondition and distinguishing from the ethics claims. |
| The `observe -> associate -> hypothesise -> intervene -> replay -> adjudicate` pipeline | Structurally parallel to `MECH-276` ("the scientist-agent principle": the agent itself generates hypotheses, acts to produce informative contrast, observes outcomes, computes counterfactual-backed attribution) — but `MECH-276` is about the **agent's own** internal scientist-like behaviour toward *its* environment. This thought's pipeline is the **external human researcher's** method for studying the agent. Different subject entirely, same abstract shape. | **Adjacent-but-distinct** -> cited in `GOV-SUBIMG-2` notes as a structural parallel, not a duplicate. |

## Key formulations

- "I wonder about applying some brain scan like behavioural analysis. We could look at what
  activity in r e substrate is associated with what behaviour. Extending temporally and
  associative."
- "A bit like my brain map visualisation pulsing and colour changing."
- "The display should never animate according to what the architecture is *supposed* to be doing."
- "`substrate(t-1) -> behaviour(t)`" / "`substrate(t-100) -> behaviour(t)`" / "`substrate(t-1000)
  -> behaviour(t)`"
- "observe -> associate -> hypothesise -> intervene -> replay -> adjudicate"
- "And my visual processing as a human means the bandwidth for my participation in assessment is
  significantly increased."
- "human visual processing detects candidate structure -> quantitative analysis tests whether it
  is reproducible -> controlled intervention tests whether the relationship is causal."
- "The visualisation itself creates a substantial risk of apophenia. Complex pulsing maps will
  almost inevitably appear meaningful to a human observer."
- "REE is increasingly becoming sufficiently integrated that observing only its components or only
  its external behaviour may leave important structure invisible. The opportunity is to observe
  both simultaneously."

## Affected existing claims

Cross-referenced, none amended, none had status/confidence/evidence touched:

- `GOV-BEHADJ-1` (behavioural-adjudication methodology, "umpire not ruler") — the discipline both
  new claims extend from behavioural-only adjudication to substrate-linked adjudication. Its own
  lit-pull note is cited directly as the stronger, already-evidenced version of the raw thought's
  apophenia safeguard.
- `GOV-INTRO-1` (introspection triangulation: generates hypotheses, never validates alone) — cited
  as the general epistemic-triangulation principle this thought's "visual detection is hypothesis-
  generation, not evidence" claim specialises for a different origin class.
- `ARC-124` (successor branches from copying a running REE) — cited for its own stated substrate
  precondition ("nothing forks a running agent"), which the new claim's causal-confirmation arm
  inherits directly, and distinguished from (ethics/governance of branching vs. branching as an
  experimental technique).
- `ARC-125`, `SD-095`, `SD-096` — the sibling continuity/branching-ethics claims, cited in
  `GOV-SUBIMG-2`'s notes as the adjacent-but-distinct cluster this does not duplicate or extend.
- `MECH-276` (scientist-agent principle) — cited as a structural parallel (agent-internal
  hypothesis-testing vs. external-researcher hypothesis-testing), not a duplicate.

## Candidate claims — REGISTERED this pass

### GOV-SUBIMG-1

**Title:** REE Assembly should build a synchronised, mechanically-derived behaviour+substrate
observability instrument — a Fishtank behavioural panel and a substrate-activity map sharing one
navigable timeline, with every visual property (intensity, colour, pulsing, size/halo, connection
change, slow background drift) tied to an explicitly documented recorded variable or
transformation and never to what the architecture is "supposed" to be doing — so that a
researcher's high-bandwidth parallel visual processing can generate candidate structure that
`GOV-BEHADJ-1`'s discovery-oriented methodology and `GOV-INTRO-1`'s triangulation rule then
require to be quantified and causally tested before being treated as a finding.

`claim_type: governance_rule`, `subject: governance.epistemics.substrate_behaviour_observability_instrument`,
`status: candidate`, `epistemic_category: governance_rule`, `claim_level: governance`,
`binds_at_version: v3` (buildable incrementally against existing V3 Fishtank + telemetry data;
no new agent substrate required — it is an observability tool, not an agent mechanism),
`blocks_v3_green_board: false`. `depends_on` / `related_claims`: `GOV-BEHADJ-1`, `GOV-INTRO-1`.

### GOV-SUBIMG-2

**Title:** Once REE substrate activity is observable (`GOV-SUBIMG-1`), Assembly should apply a
behaviour-linked substrate-association methodology that aligns internal state to behavioural
events (event-related analysis across event types, repeated occurrences, and organisms), extends
the alignment window across many temporal offsets from `t-1` to `t-1000`+ steps rather than only
the immediate surround, treats distributed multivariate substrate-state patterns — not single
variables — as the primary unit of analysis (representational-similarity-style comparison across
current behaviour, location, goal, recent history, developmental age, and subsequent behaviour),
tracks how internal-behavioural signatures change across a long individual REE lifetime
(longitudinal artificial-organism analysis), and moves from association to causal claims only via
checkpoint branch-and-replay intervention against a matched unperturbed sibling branch — following
the same discovery-then-confirmation discipline `GOV-BEHADJ-1` already requires for purely
behavioural adjudication.

`claim_type: governance_rule`, `subject: governance.epistemics.longitudinal_substrate_behaviour_causal_methodology`,
`status: candidate`, `epistemic_category: governance_rule`, `claim_level: governance`,
`binds_at_version: v4` (the correlational/associative sub-pieces — event-related alignment,
temporal-offset sweep, distributed-pattern comparison, longitudinal-within-lifetime tracking — are
cheaply testable as an offline analysis harness against existing V3 Fishtank + telemetry data
*today*; only the causal branch-and-replay confirmation arm is gated behind the fork/checkpoint-
branch capability `ARC-124` already flags as unbuilt in V3. This split is noted explicitly for a
`/governance` routing decision rather than decided unilaterally here — see notes),
`blocks_v3_green_board: false`. `depends_on` / `related_claims`: `GOV-SUBIMG-1`, `GOV-BEHADJ-1`,
`ARC-124`, `ARC-125`, `SD-095`, `SD-096`, `MECH-276`.

Both entries are written into `docs/claims/claims.yaml` in this same pass (see commit).

## Next steps

- **Version-routing split for `GOV-SUBIMG-2`** (flagged above, not decided unilaterally): a
  `/governance` cycle should confirm whether the associative/correlational sub-pieces can be
  scoped out and started against V3 data now, independent of the causal branch-and-replay arm
  which needs the checkpoint-fork capability `ARC-124` already names as missing.
  MECH-499's registration the same day (see claims.yaml tail) confirms concurrent sessions are
  actively touching the registry; no conflict found on re-read immediately before this write.
- **Literature pull, not yet done**: the raw thought makes no literature claim of its own (unlike
  many other recent intakes) — it is a from-scratch methodological proposal modelled on
  behavioural/systems neuroscience conventions (event-related potentials/fMRI, representational
  similarity analysis, longitudinal cohort designs) named only informally. A `/lit-pull` pass
  anchoring "event-related substrate-behaviour alignment" and "representational similarity
  analysis" against the actual neuroscience literature (Kriegeskorte RSA, event-related fMRI/ERP
  methodology) would strengthen `GOV-SUBIMG-2` before any hardening past `candidate`.
  `feedback_lit_exp_decoupled` applies: a literature match would corroborate the *methodology's
  soundness*, not strengthen any REE claim's confidence.
  **Correction to `GOV-BEHADJ-1` precedent**: that claim's own lit-pull note doubles as prior
  evidence directly relevant to `GOV-SUBIMG-1`'s apophenia safeguard (the Lit et al. 2011 finding)
  — cite it rather than commissioning a duplicate pull on the same point.
- **Do not build in V3** beyond what is already licensed: `GOV-SUBIMG-1`'s instrument is scoped
  as buildable-now tooling (no agent-substrate change), but no experiment should be queued from
  either claim without an explicit `/governance` routing decision, per this skill's standing
  discipline (Step 6/9).
- **Thread deliberately left unregistered**: the raw thought's own framing of the instrument as
  eventually forming a "longitudinal behavioural systems neuroscience of an artificial organism"
  research programme is aspirational framing, not a separable claim — it is the *combined* effect
  of `GOV-SUBIMG-1` + `GOV-SUBIMG-2` working together over many long-lived REEs, not a third
  proposition.
