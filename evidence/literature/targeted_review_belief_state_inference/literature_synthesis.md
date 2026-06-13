# Literature Synthesis: Belief-State Inference Layer -- Biology Grounding + Failure-Mode Register

**Date:** 2026-06-13
**Grounding node:** `inference_belief_state_v4:INF-7` (the inference failure-mode register + biology grounding that gates blocked INF-3/INF-4/INF-5/INF-6).
**Primary claims:** Q-070 (failure-mode register open question), ARC-091 (inference / belief-state affordance layer umbrella). Sub-mechanism touches: MECH-385 (belief-state hypothesis set), MECH-388 (epistemic action pressure), INV-078 (inferred-trajectory provenance).
**Discipline:** biology-before-formal-definitions. This pull raises **literature_confidence only**; experimental_confidence stays 0 for every claim. **It promotes nothing** -- all targeted claims are `substrate_conditional` / `implementation_phase: v4` and gated by the V3 closure %.

---

## Why this pull exists

The inference layer is the user-named integrative function that turns partial evidence into a *set* of state hypotheses and inferred affordances under uncertainty -- the step that lets the creature, smelling danger, *infer* the cave exit rather than only avoid the smell (V3-EXQ-603k ARM_HARM_ON_NAV passes; ARM_HARM_ON_MIDLINE struggles). Project rule (`feedback_biology_before_formal_definitions`; canonical failures SD-003 / SD-010) requires the biology be grounded *before* the belief-state substrate is built. INF-7 is that grounding node, and it doubles as the diagnostic-design source for the eventual V4 safety-route-inference experiment family.

---

## Strand grounding (L1..L5)

| Strand | Anchor paper | Direction / conf | What it grounds |
|---|---|---|---|
| **L1** hippocampal-prefrontal replay | Pfeiffer & Foster 2013 (Nature) | supports 0.78 | Hippocampal output is a *prospective hypothesis generator*, not only retrieval: pre-navigation sequences depict future paths to remembered goals. Backs ARC-007/ARC-018 as the candidate-trajectory source. |
| **L2** cognitive maps / relational inference | Whittington et al. 2020, TEM (Cell) | supports 0.76 | The hippocampal-entorhinal map is a *general relational* structure that factorises and generalises -- "state as navigable relational situation"; grounds the map over/under-generalisation failure axis. |
| **L3** pattern-completion vs preplay safety | Kay et al. 2020 (Cell) | supports 0.80 | The substrate holds *multiple competing futures in constant sub-second alternation* and refuses to collapse early. Highest-fidelity mapping: MECH-385 belief-set + INV-078 hypothesis-not-commitment. |
| **L4** POMDP belief state | Kaelbling, Littman & Cassandra 1998 (Artif. Intell.) | supports 0.70 | Formal proof that under hidden state the policy must map a *belief* (not the observation) to action. The "why" behind MECH-385; REE's top-k set is a tractable non-Bayesian approximation. |
| **L4** latent world models | Hafner et al. 2023, DreamerV3 (arXiv) | supports 0.65 | ML existence-proof that action under partial information needs *latent prediction + imagined rollout*. Also a counter-example on reward-collapse / provenance (REE separates streams). |
| **L5** active inference / epistemic value | Friston et al. 2015 (Cognitive Neuroscience) | supports 0.70 | Policy value decomposes into pragmatic + *epistemic* value; information-gathering actions are selectable when not immediately rewarding. Backbone of MECH-388. |

The five strands triangulate the same conclusion from three directions -- rodent electrophysiology (L1, L3), a unifying neuro-computational model (L2), and normative AI theory (L4, L5): **action under partial observability must be selected from an inferred, multi-hypothesis, provenance-tagged belief state, and may legitimately serve uncertainty reduction.** That is ARC-091 stated in someone else's vocabulary, and it is well-supported. What none of these papers supply is REE's *specific* solution (bounded top-k, stream-separated, heuristic precision) -- so the grounding is at the level of problem and principle, not mechanism identity.

---

## Failure-mode register -> existing MECH-126 state-abstraction taxonomy

The task's load-bearing instruction: map the inference-specific failure modes onto the **existing** state-abstraction failure taxonomy (MECH-126: `state_abstraction.failure_modes_psychiatric_analogs` -- context loss, uncertainty collapse, valence mis-tagging, overmerge, oversplit, threat-spreading), **rather than inventing a parallel one**. The clinical inference literature (Sterzer 2018; Ross 2015) is the bridge that makes the reduction defensible. The strong reading -- which Q-070 holds open as a question, not an assertion -- is that the new modes are largely re-descriptions of the same state-abstraction failures *under partial observability*.

| INF-7 inference failure mode | Reduces to (MECH-126 axis) | Lit anchor | Note |
|---|---|---|---|
| failure-to-infer-hidden-danger | context loss + uncertainty collapse | Kaelbling 1998 | Acting on observation not belief; the POMDP-quantified cost of a memoryless/observation-reactive policy. |
| failure-to-infer-hidden-safety | context loss (+ avoidant over-narrowing) | Kaelbling 1998 | Same root; manifests as helplessness / narrow safe zone rather than harm exposure. |
| overconfident-wrong-hypothesis | overmerge + uncertainty collapse | Sterzer 2018 | Over-weighted prior -> false inference held with high confidence (delusion topology). |
| premature-collapse (hypothesis collapses too early) | uncertainty collapse | Ross 2015 (**mixed**); Kay 2020 (healthy contrast) | JTC bias is real but modest/confounded -> the mode is graded, not a crisp lesion. |
| hypothesis-proliferation / apophenia / paranoia | valence mis-tagging + threat-spreading | Sterzer 2018 | Aberrant salience assigns meaning/threat to noise; the over-many-hypotheses tail. |
| cue-hijack (weak cue displaces stronger evidence) | valence mis-tagging (precision pathology) | Sterzer 2018 | Mis-weighted precision lets a weak cue dominate; SD-057 cue-recall is where REE would over/under-weight. |
| rule-overreach (rule applied outside its context) | overmerge | (ARC-062/063 boundary) | Candidate rule transferred past its licit context = merging distinct rule-contexts; rule-apprehension boundary problem. |
| map-overgeneralisation | overmerge | Whittington 2020 | Wrong route transferred from a superficially-similar state; structurally-distinct states collapsed. |
| map-oversplitting | oversplit | Whittington 2020 | Failure to transfer a safe route across structurally-equivalent states. |
| epistemic-freezing (gather forever, never commit) | (over-exploration; the dual of uncertainty collapse) | Friston 2015 | Over-weighting epistemic value; the commitment side, ties to BetaGate / commitment timing. |
| anti-epistemic-panic (commit too fast under threat) | uncertainty collapse | Friston 2015; Ross 2015 | Weighting only pragmatic value under threat; sample too little -> over-hasty commitment. |

**Net reading for Q-070.** Nine of the eleven inference failure modes reduce cleanly to one or two existing MECH-126 axes; the two epistemic-balance modes (epistemic-freezing, anti-epistemic-panic) are best described as a *commitment-timing* dimension MECH-126 does not name explicitly, sitting on the uncertainty-collapse axis but adding an over-exploration pole. So the answer to Q-070's "do they reduce to the existing taxonomy?" is **mostly yes, with one genuinely-new axis (epistemic commitment timing)**. That residual is the candidate for a proposal-first completion-set claim (below). This is a *proposed* reading surfaced for the user, not a registered finding.

---

## Completion-set harvest (PROPOSAL-FIRST -- not auto-registered)

Per the intake-must-reap rule, the pull surfaces one genuinely-new candidate the existing register does not own. **It is surfaced here for the user, not registered.**

1. **Proposed: an epistemic-commitment-timing axis on the failure register.** The two modes epistemic-freezing / anti-epistemic-panic do not reduce to a single MECH-126 axis -- they form an over-explore vs over-commit *timing* dimension (grounded in Friston 2015 pragmatic-vs-epistemic balance and Ross 2015's graded JTC effect), naturally owned at the BetaGate / commitment-timing seam rather than the state-abstraction taxonomy. Could be registered as either (a) an explicit sub-axis note on Q-070's register, or (b) a small candidate MECH wiring the inference layer's epistemic balance to the existing commitment machinery (MECH-061 commit / MECH-090 beta). **Recommend (a)** -- keep it inside Q-070 until the V4 belief-state substrate exists; minting a MECH now would be a substrate_conditional claim with no testable home.

No other net-new claim is warranted: the remaining ten modes are re-descriptions of MECH-126 axes (no new claim), and the L1..L5 biology grounds already-registered claims (ARC-091 / MECH-385 / MECH-388 / INV-078).

---

## What this pull deliberately does NOT do

- **Promotes nothing.** exp_conf stays 0 on every claim; the V3 closure % is untouched (these are `generation: v4`).
- **Queues no experiment.** Q-070 is `epistemic_category: substrate_conditional` set explicitly so `narrow_open_question` does not fire -- the right response is to ground via literature and design the V4 substrate, not to run a V3 experiment.
- **Does not weaken SD-059 / MECH-358 or the harm pathway.** The 603k midline interpretation rule holds: midline failure where ARM_HARM_ON_NAV passes is *progress* (harm valuation supported; safety-route inference not yet built / not yet developmentally fair), not harm-pathway falsification.
- **Registers no new claim.** The epistemic-commitment-timing axis is proposal-first.
