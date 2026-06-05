Status: processed

Processed in:
- `evidence/planning/thought_intake_2026-06-01_protofeelings_audit_register.md` (intake; 17-signal proto-affective audit register extending affect_primitives.md; P0 V3-gaps = curiosity/fatigue/safety/boundary; guilt-shame side cross-links musings_on_V4)

---

# REE Thought Intake: Proto-feelings and implementation timing

## Title

Proto-feelings as control signals: candidate list, threshold status, and implementation timing

## Type

Architecture audit / implementation-priority scaffold / affective control-layer planning

## Core claim

Reflective Ethical Engine already contains several proto-feelings as drive-weighted control signals.

These are not “emotions” in the ordinary human-labelled sense. They are control signals that influence salience, affordance ranking, persistence, commitment probability, policy arbitration, and post-action learning.

The next architectural task is not to add a general emotion module.

The task is to determine:

1. which proto-feelings are already represented,
2. which are missing or under-specified,
3. which are required for minimum viable REE control,
4. which are required only for mammalian/human-like completeness,
5. when each should be implemented, deferred, or left as theory.

---

## Definitions

### Proto-feeling

A proto-feeling is:

> a drive-weighted control signal that changes perception, salience, action selection, persistence, commitment, or learning.

It may be conscious in humans, but does not need to be conscious in REE.

It may correspond to a named human feeling, but does not need to.

### Threshold A: Minimum viable REE control

A proto-feeling belongs at this threshold if its absence causes basic action-arbitration failure.

Examples:

- quiescence
- harm-blindness
- compulsive approach
- monostrategy lock-in
- inability to explore
- inability to stop
- inability to recover
- inability to commit
- inability to learn from consequence
- inability to repair after harm
- inability to detect blocked agency or coercion

### Threshold B: Mammalian/human-like affective completeness

A proto-feeling belongs at this threshold if its absence does not necessarily break minimum control, but prevents mammalian-like or human-like affective cognition.

Examples:

- no attachment
- no grief
- no shame
- no guilt
- no social repair
- no comfort/soothing
- no social safety
- no disgust/contamination
- no playfulness
- no embodied fatigue
- no therapy-like symbolic emotional processing

---

## Implementation timing categories

### Now / V3-relevant

Implement or explicitly audit soon because the signal may affect current REE bottlenecks.

Criteria:

- affects current experiments,
- affects monostrategy, quiescence, commitment, safety, or learning,
- can be proxied in single-agent V3,
- does not require full multi-agent social substrate.

### Late V3 / conditional pull-forward

Track now and implement if current failures point toward it.

Criteria:

- plausible relevance to V3,
- but implementation may be costly or premature,
- should be pulled forward only if experiments show a matching failure signature.

### V4 / multi-agent developmental

Important, but needs caregiver, peer, social, attachment, or multi-agent substrate.

Criteria:

- requires social signalling,
- requires co-regulation,
- requires another agent,
- requires long developmental history,
- cannot be meaningfully tested in V3 except as a proxy.

### Theory / long-range

Keep conceptually visible but do not implement unless the REE target expands.

Criteria:

- not necessary for safety/corrigibility,
- not necessary for current mammalian-social target,
- high risk of anthropomorphic overbuild.

---

# Candidate proto-feelings

## 1. Wanting / approach / SEEKING

### Function

Approach pressure toward benefit, resources, goals, and affordances.

### Current REE status

Strongly represented.

Likely substrates:

- z_goal
- VALENCE_WANTING
- drive_level
- drive_floor
- drive trace / anticipatory wanting
- benefit exposure
- goal seeding

### Threshold A

Required.

Without wanting, REE risks quiescence: harm avoidance remains, but no sufficient approach drive exists to commit.

### Threshold B

Required.

Mammalian cognition requires sustained approach, curiosity, seeking, and anticipatory motivation.

### Implementation timing

Already V3-core.

Continue refining rather than adding as new module.

### Failure if absent

- quiescence
- anhedonia-like wanting failure
- benefit encountered but not pursued
- planning system has no motivational terrain

---

## 2. Liking / consummatory benefit

### Function

Positive evaluation of received benefit. Distinct from wanting.

### Current REE status

Moderate to strong.

Likely substrates:

- benefit evaluation
- VALENCE_LIKING
- liking bridge concepts
- consummatory resource signal

### Threshold A

Required.

REE needs to distinguish actual benefit from mere approach pressure.

### Threshold B

Required.

Mammalian affect requires consummatory positive states, not just seeking.

### Implementation timing

Already V3-relevant.

Maintain strict separation from wanting.

### Failure if absent

- approach without consummatory calibration
- no distinction between pursuit and satisfaction
- compulsive seeking risk
- poor learning from achieved benefit

---

## 3. Threat / fear / avoidance

### Function

Avoidance pressure in response to harm, danger, predicted injury, or adverse consequence.

### Current REE status

Strong.

Likely substrates:

- z_harm_a
- z_harm_s
- harm history
- aversive arousal
- harm-gated commitment
- residue updates after harm

### Threshold A

Required.

Without threat/avoidance, REE becomes harm-blind.

### Threshold B

Required.

Mammalian cognition requires threat sensitivity and defensive modulation.

### Implementation timing

Already V3-core.

Continue refining distinction between sensory harm and affective-motivational harm.

### Failure if absent

- harm-blindness
- reckless commitment
- inability to learn avoidance
- unsafe exploration
- no fear-like interruption of plans

---

## 4. Residue / regret / consequence trace

### Function

Persistent path-dependent trace of harm, value mismatch, or ethical consequence.

### Current REE status

Strong.

Likely substrates:

- residue field
- moral residue
- value mismatch routing
- path-dependent consequence memory

### Threshold A

Required.

Without residue, REE cannot learn ethically from consequences over time.

### Threshold B

Required.

Mammalian/human-like cognition requires consequence memory, regret, guilt-adjacent repair, and continuity of responsibility.

### Implementation timing

Already V3-core.

Potential future expansion should distinguish:

- consequence trace,
- regret,
- guilt,
- repair drive,
- shame.

### Failure if absent

- no ethical path memory
- repeated harm without cumulative learning
- consequence-free action selection
- no basis for repair

---

## 5. Commitment pressure / urgency-to-act

### Function

Collapse from candidate futures into one intended trajectory.

### Current REE status

Strong.

Likely substrates:

- E3 trajectory selection
- BetaGate
- commitment readiness
- precision increase
- post-commit learning relevance

### Threshold A

Required.

Without commitment, REE can simulate but not act.

### Threshold B

Required.

Mammalian action requires action commitment, not only deliberation.

### Implementation timing

Already V3-core.

Continue work on readiness, false commitment, degenerate commitment, and release.

### Failure if absent

- endless deliberation
- unstable action
- no intended trajectory
- no diagnostic post-action error
- no clear agency boundary

---

## 6. Curiosity / novelty / exploratory interest

### Function

Approach toward uncertainty, novelty, learnable structure, or prediction-error-rich regions.

### Current REE status

Partial.

Likely substrates:

- novelty-driven exploration
- play substrate
- prediction-error locus targeting
- learning progress motivation
- behavioural diversity mechanisms

### Threshold A

Probably required.

Without curiosity or novelty drive, REE risks sparse-reward brittleness, monostrategy, and failure to discover affordances.

### Threshold B

Required.

Mammalian development uses exploratory play and curiosity heavily.

### Implementation timing

Now / V3-relevant.

This should be one of the first proto-feelings audited for implementation because it directly connects to current monostrategy and developmental bottlenecks.

### Possible minimal implementation

A curiosity signal could bias action selection toward:

- high prediction error,
- high learning progress,
- under-sampled state regions,
- affordance uncertainty,
- safe novelty.

### Failure if absent

- monostrategy lock-in
- brittle learning
- poor affordance discovery
- overdependence on external reward
- underdeveloped play/childhood curriculum

---

## 7. Playfulness / safe synthetic action

### Function

Low-risk exploration of action, commitment, social framing, counterfactuals, and rules.

### Current REE status

Conceptually strong but implementation-limited.

Likely substrates:

- play frame tag
- hypothesis tag
- synthetic goal/harm signals
- pretend play
- games-with-rules
- frame maintenance
- caregiver/peer co-regulation

### Threshold A

Probably required developmentally.

A minimal REE may not need full play, but safe synthetic exploration may be necessary for robust development without catastrophic harm.

### Threshold B

Required.

Mammalian/human-like development requires play for learning, sociality, affect regulation, and frame distinction.

### Implementation timing

Late V3 / V4 split.

V3 can implement single-agent proxy play.

Full play is V4 because real play requires frame signalling, caregiver/peer monitoring, and social repair.

### Possible minimal implementation

V3 proxy:

- synthetic goal episodes,
- synthetic harm bounded below catastrophic levels,
- explicit frame-open/frame-close,
- commitment gate blocked from treating play content as real commitment,
- transfer test from play-trained strategy to real episode.

### Failure if absent

- real harm required for learning
- poor counterfactual handling
- frame confusion
- brittle ethical agency
- no safe rehearsal of commitment
- no developmental route to social play

---

## 8. Fatigue / overload / stop-recover

### Function

A pressure to stop, rest, downshift, consolidate, or reduce load when continuing action becomes unsafe or inefficient.

### Current REE status

Partial.

Likely substrates:

- homeostasis
- energy
- sleep/offline mode
- overload concepts may be implicit rather than explicit

### Threshold A

Required.

A system that can approach and avoid but cannot stop or recover may overcommit, degrade, or fail to consolidate.

### Threshold B

Required.

Embodied mammalian affect includes fatigue, tiredness, overwhelm, satiety, and recovery needs.

### Implementation timing

Now / V3-relevant.

This may be a minimum control-layer requirement, especially for preventing over-persistence and supporting sleep/offline integration.

### Possible minimal implementation

A stop-recover proto-feeling could be based on:

- cumulative prediction error,
- action entropy,
- resource depletion,
- recent harm load,
- failed-commit streak,
- high uncertainty with low benefit,
- need for replay/offline consolidation.

### Failure if absent

- overcommitment
- brittle persistence
- no recovery mode
- no graceful downshift
- poor sleep/offline timing
- pathological “keep trying” loops

---

## 9. Safety / soothing / comfort

### Function

Positive safe-enough state that permits exploration, attachment, play, sleep, repair, and updating.

### Current REE status

Weak or implicit.

Likely current proxy:

- low harm
- stable context
- low uncertainty
- successful recovery
- caregiver protection in future V4

### Threshold A

Probably required.

Low harm is not the same as safety. REE may need a positive safety signal to permit exploration, learning, and down-regulation.

### Threshold B

Required.

Mammalian affect requires comfort, soothing, co-regulation, and felt safety.

### Implementation timing

P1 / late V3 candidate.

Single-agent V3 may implement “safe-enough” as a control state. Full soothing/co-regulation is V4.

### Possible minimal implementation

Safety signal could increase when:

- harm low,
- prediction error bounded,
- goal not urgent,
- resource state adequate,
- no recent boundary violation,
- stable context,
- safe caregiver/anchor present in V4.

Effects:

- lower threat precision,
- increase exploration/play allowance,
- permit sleep/offline replay,
- allow memory reconsolidation/update.

### Failure if absent

- system only knows danger versus no danger
- poor rest
- poor therapy-like updating
- poor play entry
- poor attachment development
- chronic vigilance attractors

---

## 10. Anger / boundary violation / blocked agency

### Function

Signal that agency, boundary, fairness, autonomy, or expected constraint has been violated or blocked.

### Current REE status

Underdeveloped.

Possible current proxies:

- harm
- residue
- constraint violation
- failed goal pursuit
- blocked action
- coercion-like context may not yet be explicit

### Threshold A

Probably required.

This may be necessary for anti-coercion, anti-domination, blocked-agency detection, and defence against exploitation.

### Threshold B

Required.

Mammalian and human social cognition require anger/rage-like boundary defence and response to violation.

### Implementation timing

P1 / conditional V3 pull-forward.

Should be audited soon. Implementation may be V3-proxy if framed as blocked-agency or boundary-violation rather than full anger.

### Possible minimal implementation

Boundary-violation signal could fire when:

- intended action repeatedly blocked by external agent or constraint,
- consent/capacity boundary violated,
- resource access unfairly prevented,
- harm imposed by another agent,
- predicted safe affordance becomes coercive,
- rule frame breached.

Effects:

- increase salience of blocker,
- raise policy priority for boundary restoration,
- trigger repair/assertion/withdrawal candidates,
- mark residue if unresolved.

### Failure if absent

- learned helplessness
- excessive compliance
- poor coercion detection
- no injustice signal
- failure to defend self/others
- boundary collapse

---

## 11. Disgust / contamination / corruption

### Function

Avoidance of contamination, corruption, impurity, infection, spoiled resources, or boundary-polluting contact.

### Current REE status

Likely missing.

Possible current proxies:

- harm
- threat
- residue
- obsessive-compulsive disorder contamination concepts if present elsewhere

### Threshold A

Context-dependent.

Required if REE must handle contaminated affordances, corruption, pathogen-like risk, spoiled resources, polluted information, or obsessive-compulsive disorder-like contamination states.

### Threshold B

Required.

Mammalian/human-like affective completeness requires disgust and contamination avoidance.

### Implementation timing

P1 if contamination/corruption is in scope; otherwise V4.

### Possible minimal implementation

Contamination signal could differ from harm:

- harm = immediate damage,
- contamination = contact-based spreading risk or latent corruption.

It could mark objects, locations, memories, or agents as contaminated after contact with a contaminant source.

Effects:

- avoidance,
- cleaning/repair candidate generation,
- reduced trust in contaminated affordance,
- spread along contact graph,
- decay or repair after decontamination.

### Failure if absent

- treats spoiled or contaminated benefit as safe
- no boundary-pollution reasoning
- no corruption detection
- weak obsessive-compulsive disorder contamination modelling
- inability to distinguish harm from impurity/contact risk

---

## 12. Care / attachment

### Function

Approach, protection, and value-preservation directed toward another agent or toward self-as-care-worthy.

### Current REE status

Conceptual / V4-heavy.

Likely related substrates:

- loveability internalisation
- caregiver modelling
- shared valence
- social architecture
- repair after harm
- care weights

### Threshold A

Not required for minimal single-agent V3.

May become required for multi-agent ethical REE.

### Threshold B

Required.

Mammalian/human-like cognition requires attachment, caregiving, and internalised care.

### Implementation timing

V4.

Do not force into V3 except as a placeholder or simple proxy.

### Possible minimal implementation

V4 care signal could:

- assign protective value to another agent,
- maintain concern across absence,
- generate repair after harm,
- support self-care via internalised loveability,
- alter action scoring when another agent is vulnerable.

### Failure if absent

- cold ethics
- no attachment
- no caregiving
- no loveability internalisation
- repair becomes abstract rather than motivated
- social agents treated as objects or constraints only

---

## 13. Separation distress / grief

### Function

Distress and reorganisation after loss of attachment, expected presence, role, home, future, or valued relation.

### Current REE status

Underdeveloped.

Possible current proxies:

- residue
- loss of benefit
- absent goal
- attachment not yet implemented

### Threshold A

Not required for minimal V3.

Could become required for stable long-horizon multi-agent agents.

### Threshold B

Required.

Mammalian/human-like affective cognition requires loss, mourning, and adaptation to absence.

### Implementation timing

V4 / theory until attachment substrate exists.

### Possible minimal implementation

Requires prior attachment/care representation.

Grief signal could fire when:

- valued agent/resource permanently absent,
- predicted reunion fails,
- role/future collapses,
- repair impossible,
- attachment goal cannot be satisfied.

Effects:

- search,
- protest,
- withdrawal,
- memory reconsolidation,
- value reorganisation,
- new goal formation after loss.

### Failure if absent

- no mourning
- no model of loss
- brittle attachment
- no therapy-like grief processing
- no distinction between temporary absence and irreversible loss

---

## 14. Shame / social self-threat

### Function

Signal that the self is negatively evaluated, exposed, devalued, or misaligned with social norms.

### Current REE status

Likely missing or implicit.

Possible current proxies:

- residue
- failed social prediction
- repair after harm
- self-model conflict

### Threshold A

Not required for minimal V3.

May be required for advanced social corrigibility.

### Threshold B

Required.

Human-like social cognition requires shame/status/self-threat handling, though it must be carefully distinguished from guilt and repair.

### Implementation timing

V4.

Avoid early implementation unless social substrate and repair pathways exist; otherwise it risks creating pathological self-punishment analogues.

### Possible minimal implementation

Shame-like signal should require:

- self-model,
- social evaluator model,
- norm model,
- exposure/publicness or imagined social judgement,
- repair/soothing off-ramp.

Effects:

- social withdrawal,
- concealment,
- norm update,
- repair attempt,
- status recalibration.

### Failure if absent

- poor norm internalisation
- no social self-threat
- no embarrassment/shame-like learning
- weak social repair
- poor modelling of human therapy material

### Risk if implemented too early

- global self-condemnation
- pathological inhibition
- shame without repair
- social compliance collapse

---

## 15. Guilt / repair urge

### Function

Action-focused distress after causing harm, motivating repair.

### Current REE status

Partial via residue, but repair urge may be under-specified.

### Threshold A

Probably required for mature ethical REE.

Maybe not required for toy V3.

### Threshold B

Required.

Human-like social and moral cognition requires guilt-like repair motivation.

### Implementation timing

Late V3 / V4.

Could be pulled forward if residue exists but does not generate repair behaviour.

### Possible minimal implementation

Guilt-like signal should be distinct from shame:

- guilt = “my action caused harm; repair the harm”
- shame = “I am bad/exposed/devalued”

Minimal guilt proxy:

- harm caused by committed action,
- attribution to self trajectory,
- repair affordance exists,
- repair candidate receives salience boost.

### Failure if absent

- residue without repair
- ethical learning stays punitive or avoidant
- no apology/restitution behaviour
- repeated harm without restoration

---

## 16. Boredom / under-stimulation

### Function

Signal that current state lacks learning progress, novelty, meaningful goal movement, or sufficient salience.

### Current REE status

Partial.

Possible overlap:

- curiosity
- novelty
- learning progress
- exploration pressure

### Threshold A

Possibly required.

May be needed to escape low-value loops and promote exploration.

### Threshold B

Required.

Mammalian/human-like cognition includes boredom as a driver away from stagnation.

### Implementation timing

V3-relevant if monostrategy or repetitive low-progress behaviour persists.

### Possible minimal implementation

Boredom signal could rise when:

- prediction error low,
- learning progress low,
- goal progress low,
- no meaningful novelty,
- repeated state-action loop,
- safety adequate.

Effects:

- increase exploration temperature,
- widen candidate generation,
- seek novelty,
- trigger play mode.

### Failure if absent

- repetitive loops
- no exploration after local competence
- failure to seek richer affordances
- stagnation despite safety

---

## 17. Lust / mating drive

### Function

Reproductive/sexual motivational system.

### Current REE status

Absent.

### Threshold A

Not required.

### Threshold B

Optional.

Only required if the target is full mammalian repertoire, not REE safety/corrigibility.

### Implementation timing

Theory / out of scope.

### Failure if absent

None for current REE.

### Risk if implemented

High anthropomorphic and safety complexity for low architectural value.

---

# Implementation priority summary

## P0: Now / V3-relevant

These may affect current REE bottlenecks.

1. Curiosity / novelty / exploratory interest
2. Fatigue / overload / stop-recover
3. Safety / soothing / comfort as positive safe-enough state
4. Boundary violation / blocked agency, at least as an audit category

## P1: Conditional V3 pull-forward

Implement if matching failure signatures appear.

1. Disgust / contamination / corruption
2. Boredom / under-stimulation
3. Guilt / repair urge, if residue does not generate repair behaviour
4. Boundary violation, if coercion or blocked-agency failures appear

## P2: V4 / multi-agent developmental

Track now, implement with social substrate.

1. Care / attachment
2. Separation distress / grief
3. Shame / status / social self-threat
4. Full play with peer/caregiver frame maintenance
5. Social soothing / co-regulation

## P3: Theory / out of scope

1. Lust / mating drive
2. Any full named-emotion taxonomy implemented as labels rather than control signals

---

# Recommended next step

Do not implement a general emotion module.

Instead create a proto-affective audit register with one row per candidate control signal.

Each row should include:

- name,
- control function,
- current REE substrate,
- Threshold A status,
- Threshold B status,
- pathology if absent,
- pathology if overactive,
- V3/V4/theory timing,
- smallest testable proxy,
- literature anchors,
- claim IDs if already represented,
- open implementation questions.

---

# Short form

REE already has proto-feelings.

The missing work is not emotional decoration.

The missing work is a staged proto-affective control audit:

> What signals must exist for safe action arbitration now, and what signals must eventually exist for mammalian/human-like social affect?

Implementation should follow failure signatures, not human emotion names.
