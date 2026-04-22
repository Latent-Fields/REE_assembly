# Homeostatic Override / Imminent-Death Drive Amplification Literature Pull

> Paste this into a new Claude Code session as your opening message.
> Created: 2026-04-22
> Origin: V3-EXQ-471 fishtank visualization showed a catatonic-locked agent whose
> energy depleted to zero with no homeostatic override. SD-036 (GABAergic decay)
> resolves the harm-stream lock but does not address the missing override authority
> that should let hunger override threat under survival demand.

## Prompt

/lit-pull Homeostatic-need brain circuits and how they amplify or override other
drive systems under imminent-death conditions -- specifically the question of how
hunger / energy depletion / dehydration acquires authority to override threat-driven
avoidance behaviour. The architectural question: in V3 we have separate streams for
threat (z_harm), goal (z_goal), drive (energy/homeostatic), and an arbitration
mechanism (mode selection via SD-032a SalienceCoordinator). When a hazard event
locks the agent into avoid mode and energy then runs to zero, no mechanism currently
reverses the lock -- avoid still wins arbitration even when starvation is imminent.
Subjectively, hunger does not just compete with threat; it sharpens or amplifies
multiple drives simultaneously (the dread stream may itself intensify, the
fast-interrupt becomes more sensitive, goal pursuit becomes more compulsive). This
suggests a broadcast neuromodulator that gain-modulates several streams from one
homeostatic source, rather than a competing scalar.

Target claims to inform / extend:
- **SD-012** (drive-modulated goal seeding -- currently has no override authority over
  z_harm-driven avoid mode)
- **SD-036** (GABAergic cross-stream decay regulator, registered 2026-04-22 -- the
  decay layer is one half of the catatonia rescue; this lit-pull addresses the other
  half: what reverses the mode lock when survival demands it)
- **MECH-279** (PAG GABAergic freeze-gate -- freeze exit may be normal-route via
  decay or override-route via homeostatic emergency)
- **SD-032a** (SalienceCoordinator -- target for whatever mechanism provides override
  authority)
- Possible new SD/MECH for the override mechanism itself

Specific neurobiological systems to cover:

1. **Lateral hypothalamus (LH)** -- the canonical hunger/feeding circuit. Specifically:
   - LH GABAergic and glutamatergic projections to VTA, PAG, and PFC
   - How LH activity overrides defensive behaviour in foraging-under-threat paradigms
   - Burnett et al 2019 (LH circuits and feeding); Sternson lab work on AgRP/POMC

2. **Orexin / hypocretin (LHA)** -- broadcast arousal/motivation neuromodulator
   strongly implicated in the kind of multi-stream gain modulation the
   architectural question requires:
   - Orexin projections to VTA, LC, raphe, BLA, PFC, PAG
   - Berthoud, Saper, Sakurai work on orexin as a homeostasis-arousal coupler
   - How orexin loss (narcolepsy) produces specific failures in motivated behaviour
     under metabolic challenge -- the human knockout

3. **Lateral parabrachial nucleus (LPB)** and the brainstem sensory-aversive coupling:
   - How interoceptive distress signals (hunger, thirst, hypoxia, hypoglycaemia) are
     routed through LPB to higher centres
   - LPB CGRP neurons and threat-vs-need integration (Palmiter lab)

4. **Ventromedial hypothalamus (VMH)** and defensive-vs-feeding switching:
   - VMH SF1 neurons in defensive behaviour and how they interact with LH feeding
     circuits
   - Lin et al, Anderson lab work on VMH switching

5. **Insula and interoceptive amplification under metabolic stress:**
   - How insular processing of interoceptive signals scales with deprivation level
   - Craig 2009 + extensions; whether this maps onto SD-032c (AIC-analog) gain
     modulation under drive

6. **The clinical and ethological literature on starvation overriding fear:**
   - Foraging-under-predation models (Lima & Dill 1990 and successors)
   - Clinical: anorexia nervosa as a *failure* of this override (drive does not
     acquire override authority -- explanatory question for the architecture)
   - Clinical: hyperphagic conditions (Prader-Willi, hypothalamic damage) as
     pathological excess of override
   - The phenomenology of severe hypoglycaemia / hypoxia: which streams *intensify*
     vs which *suppress*

## Architectural questions the lit-pull should help answer

1. **Single broadcast vs multi-target competition.** Does a single homeostatic
   neuromodulator (orexin is the leading candidate) gain-modulate multiple streams
   simultaneously, or is the override mediated by point-to-point projections that
   each carry their own copy of the homeostatic signal? The former predicts a
   regulator-layer architecture (parallel to SD-036's GABA layer); the latter
   predicts per-target wiring without a regulator.

2. **Threshold vs continuous.** Does override authority appear gradually as drive
   accumulates, or does it cross a threshold and snap on? The latter would be
   architecturally cleaner and matches the clinical phenomenology of "I just
   couldn't keep refusing food / stop drinking water." The former matches the
   neuroeconomics literature on graded value.

3. **Symmetry across drives.** Is the override mechanism the same for hunger,
   thirst, hypoxia, sleep deprivation, etc., or does each homeostatic system have
   its own override pathway? Architectural parsimony favours shared; neurobiological
   evidence may favour partly distinct (e.g. CO2-sensing for hypoxia is anatomically
   separable from glucose-sensing for hunger).

4. **Does the override AMPLIFY z_harm or REPLACE its arbitration weight?** The user
   observation suggests amplification -- hunger sharpens dread, not replaces it.
   This would predict that under starvation the agent becomes *more* threat-sensitive,
   not less, but also *more* willing to act despite threat (because both signals are
   amplified and the action threshold is the difference). This is a substantively
   different architecture from "drive overrides threat" and the lit-pull should be
   alert to which model the biology supports.

5. **What is the bridge to z_goal seeding (SD-012)?** Currently SD-012 requires
   benefit_exposure > 0 to seed z_goal. Under override, does drive directly seed
   z_goal (skipping benefit_exposure), or does override force the agent into
   exploratory action that *creates* benefit_exposure, which then seeds z_goal via
   the normal pathway?

## Output structure

Standard targeted_review_*/ format. Suggested directory:
`evidence/literature/targeted_review_homeostatic_override/`

Per-paper records as usual. After the pull, write a short synthesis note flagging:
- Which architectural question(s) each paper addresses
- Which of the five questions above remain underdetermined and need additional pulls
- Whether the evidence supports registering a new SD/MECH cluster for the override
  mechanism (and if so, draft proposed claim text)

Estimated scope: ~10-15 papers, single session.

## Notes for the agent doing the pull

- The user is a consultant psychiatrist who deals clinically with both ends of the
  override-failure spectrum (anorexia nervosa = override-deficient; hyperphagia =
  override-excessive). Use precise clinical terminology.
- The architectural reading explicitly *expects* the override to be a broadcast
  neuromodulator -- be alert to evidence that contradicts this expectation, not just
  evidence that supports it.
- Connect to existing REE memory entries on homeostasis and drive: SD-012 (drive
  seeding), MECH-186/187/188 (serotonergic regulatory layer for the goal pipeline),
  SD-036 (GABAergic decay regulator). The hypothesised override layer is candidate
  third regulatory layer alongside 5-HT and GABA, plausibly orexin-mediated.
- The exemplar that motivated this pull is V3-EXQ-471 (fishtank visualization,
  2026-04-21 to 2026-04-22). Worth re-reading the trace summary in
  `psychiatric_failure_modes.md` "Catatonia, Subtype II" before starting.
