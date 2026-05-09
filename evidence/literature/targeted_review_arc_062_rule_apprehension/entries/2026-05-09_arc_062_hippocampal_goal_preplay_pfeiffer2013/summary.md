# Pfeiffer & Foster 2013 — Hippocampal place-cell sequences depict future paths to remembered goals

According to PubMed: Pfeiffer & Foster 2013, *Nature* 497(7447):74–9. [DOI 10.1038/nature12112](https://doi.org/10.1038/nature12112) (PMID 23594744, PMC3990408).

## What the paper shows

Multi-electrode recordings from rat hippocampal CA1 during goal-directed navigation in an open arena. Before initiating each trajectory, the hippocampus generated brief place-cell sequences depicting *spatial trajectories from the rat's current location toward a known goal location*. These sequences predicted the rat's immediate future behaviour. Critically, the prediction held even when the specific combination of start and goal locations was novel — the rat had never run that exact trajectory before — so the mechanism is generative-from-cognitive-map, not retrieval of a remembered episode. The authors propose hippocampal sequence events as a goal-directed, trajectory-finding mechanism: they identify important places and relevant behavioural paths at specific times when memory retrieval is required.

## Why this matters for R3 (where does rule context modulate action selection?)

R3 has three candidate sites in the REE substrate:
- (i) score-aggregation level (BG-side gate on candidate scoring)
- (ii) trajectory-proposal level (hippocampal preplay biasing which futures get generated)
- (iii) score_bias level (PFC top-down per-candidate additive bias)

Pfeiffer & Foster establish (ii) as a real biological mechanism. Goal-biased forward sequence generation is the rodent-CA1 analog of REE's `HippocampalModule.propose_trajectories()` with goal-conditioned CEM seeding. The biology is unambiguous: the hippocampus does *not* propose value-flat trajectories that downstream regions then weight; it proposes *goal-biased* trajectories from the start. Rule-context-biased trajectories (the natural extension under MECH-309 / ARC-062 logic) would route discriminator output to seed the proposal distribution upstream of E3 scoring.

## Why ARC-063 has this baked in and ARC-062 does not

ARC-063 strong reading commits explicitly: "Hippocampal rollout generation is biased by active CandidateRule objects: rules embed in the rollout landscape itself, becoming 'psychologically real' by shaping which futures are easy to imagine rather than by being verbally endorsed." That is Pfeiffer & Foster's mechanism elevated from spatial goals to abstract rules. ARC-062 weak reading defers this — it commits to gated policy heads at the score-aggregation / score_bias level, not at the proposal level. Pfeiffer & Foster's evidence supports the architectural choice that ARC-063 is right *eventually*, but does not arbitrate whether ARC-062's score-aggregation-level commitment is sufficient for V3-scope.

## Mapping caveat

Pfeiffer & Foster establish goal-biased forward sequences. They do *not* directly test rule-context-biased sequences ("reef-context vs forage-context preplay"). The transfer from spatial-goal preplay to context-rule-biased preplay is real biologically (the underlying mechanism is goal-conditioned generative sequence-rollout from the cognitive map; rules embed in the goal-conditioning) but adds a step. The R3 site-(ii) reading is therefore an extrapolation backed by a strong analog rather than a direct test.

## Cross-link

This paper was previously pulled for the MECH-307 cluster (`evidence/literature/targeted_review_excitement_5th_valence_channel/entries/2026-05-09_mech307_hippocampal_preplay_to_goal_pfeiffer2013/`) with a Gap-4 anticipatory-affect mapping. The current entry is re-tagged for ARC-062 / MECH-309 / ARC-063 with a different REE-translation: there it was the consumer-side hippocampal preplay-to-goal substrate; here it is the architectural site-selection question for the rule-apprehension layer. Same source, distinct mappings.

## Confidence reasoning

Source quality high — *Nature*, foundational for the goal-biased preplay literature, methodologically clean (open arena novel start-goal combinations rule out episode-retrieval explanation). Mapping fidelity reduced because the paper supports R3 site (ii) as legitimate but does not arbitrate it as primary — and the ARC-062 weak-reading architectural commitment is to a different site (iii). Transfer risk moderate: rodent CA1 to REE `HippocampalModule` generalises well, but rule-context-biased preplay is an extrapolation from spatial-goal-biased preplay. Confidence 0.82 reflects strong evidence for R3-(ii) as a real site, with the architectural-commitment-mismatch caveat captured in `failure_signatures`.

## Failure signature for the cluster

If ARC-062 weak reading at the score_bias level (option iii) FAILs the SD-054 monomodal-collapse falsifier, Pfeiffer & Foster's mechanism is the natural alternative to try next: route the discriminator output to bias the hippocampal CEM seed distribution (trajectory-proposal level, option ii) rather than to per-candidate score_bias. If both options fail, the diagnosis routes upward to ARC-063 strong reading and the V4 distributed CandidateRule field.
