# Non-Deficit Action Drives — Architectural Family

**Status:** family slot registered 2026-05-10 (ARC-066 + ARC-067 + ARC-068 candidate / pending_design).
**Family principle:** behaviour comes from surplus capacity AND from deficits, not from deficits alone.

---

## What this family fixes

REE today has three sources of behavioural pressure:

| Source | Substrate | Goes to zero when... |
|--------|-----------|----------------------|
| Threats | z_harm (SD-010 / SD-011) | safe |
| Specific wants | z_goal seeded from depletion (SD-012 / SD-015) | well-fed |
| Novelty / uncertainty / learning-progress | MECH-314 curiosity sub-flavours | familiar |

A well-fed, safe REE agent in a familiar environment with no specific z_goal therefore has **no gradient to act**. Standing still pays no cost; no candidate trajectory has a positive bias; the only thing that prevents argmax-on-noise is MECH-313's tonic noise floor (which spreads the distribution but doesn't add a directional bias toward action over no-op).

Biology has a different equilibrium. A healthy energetic person in the same situation reports a felt push to deploy capacity — restlessness when bored, drive to act when fresh, the felt cost of "wasting time". This phenomenology was the registration trigger (user, 2026-05-10):

> "I observe a drive in me to do something while I have energy rather than nothing / imagination and other non-behavioural work. In REE it seems that the agent is happy doing nothing."

The three claims register the architectural slots needed to close this gap. Each is a genuinely distinct architectural shape; they compose at E3 score-aggregation but do different work and have different lit anchors.

---

## The three slots

### ARC-066 — tonic vigor coupling (positive-side, score-additive)

Capacity-keyed action bias. The vigor scalar is a slow EWMA over the realised E3-score-receipt stream (long-run average reward rate, per Niv 2007 formalism), gated downward when internal-state proxies (energy reserve, drive integrator, recent prediction error) are unfavourable. The scalar biases E3 score selection toward action over no-op trajectories. **Independent of any specific target.**

Biology anchor cluster (post lit-pull 2026-05-10, R1+R3+R4 verdicts; see [synthesis](../../evidence/literature/targeted_review_arc_066_tonic_vigor/synthesis.md)):
- **Niv et al. 2007 (Psychopharmacology)** — vigor-of-action set by tonic dopamine tracking average reward rate. Formalism anchor for R3 (additive opportunity-cost form) and R4 (slow EWMA scalar).
- **Salamone & Correa 2012 (Neuron)** — mesolimbic DA encodes the activational dimension of motivation, dissociable from hedonic / consummatory aspects. Substrate identity for the DA-vigor account.
- **Beierholm et al. 2013 (Neuropsychopharmacology)** — human pharmacological causal test: L-DOPA strengthens the avg-reward-rate-vigor coupling vs placebo; citalopram does not. Specificity-to-DA evidence.
- **Walton et al. 2003 (J Neurosci)** — ACC effort-cost lesion in rats; BOUNDARY anchor for the ACC effort-cost machinery (which is closer to SD-032b dACC adaptive control / ARC-068 territory than to ARC-066).
- **Depue & Collins 1999 (Behav Brain Sci)** — BAS as an independent personality dimension; low BAS = anhedonic inertia, high BAS = drive-to-act. Abstract-level commitment that the function is real and target-free.

#### What ARC-066 is NOT (lit-pull R2 verdict)

The slot was originally registered with Aston-Jones & Cohen 2005 (LC-NE adaptive gain) as a primary anchor, with the gloss "LC-NE tonic mode biases toward exploitation/action -- directional action bias, not noise on choice". The lit-pull R2 verdict **rejects** this attribution:

- **Aston-Jones & Cohen 2005 (Annu Rev Neurosci)** — theoretical anchor for the dual-mode LC-NE framework. Consistent with EITHER a noise-mediated reading or a direction-mediated reading at the conceptual level.
- **Kane et al. 2017 (Cogn Affect Behav Neurosci)** — the disambiguation. DREADD-mediated chemogenetic stimulation of LC tonic activity in rats, by the original Aston-Jones / Cohen authorship group, with formal model comparison: the resulting earlier patch-leaving was best explained by an INCREASE IN DECISION NOISE rather than a SYSTEMATIC BIAS. The LC-NE tonic effect is one mechanism (noise), not two.

The implication: LC-NE tonic mode is **fully covered by MECH-313** (stochastic noise floor / softmax temperature lift). There is no remaining LC-NE function for ARC-066 to claim. The ARC-066 substrate attribution is therefore **mesolimbic DA-vigor (Niv / Salamone / Beierholm) + BAS abstract level (Depue & Collins)**, NOT LC-NE.

This is a substrate-attribution reframe; the architectural function ARC-066 names is unchanged.

Distinct from existing slots:
- SD-012 drive: rises *as energy falls*. ARC-066 is the inverse — rises *as capacity rises*.
- MECH-313 noise floor: orthogonal axis (entropy on choice, not direction toward action). Lit-pull R2 verdict establishes that LC-NE tonic mode is fully covered by MECH-313.
- MECH-216 predictive wanting: target-conditioned. ARC-066 is target-free.

### ARC-067 — idle aversion / boredom (negative-side, valence accumulator)

Sustained low-engagement is itself negatively valenced. A slow accumulator over an engagement-rate scalar (commit transitions per episode, novel-observation count, E3 deliberation depth, residue-write rate — exact composition TBD at child-MECH design time) integrates negative pressure when engagement falls below a threshold. The aversive recruits the same downstream as actual harm via a z_harm-like channel, so engagement-poverty competes for action-selection priority on the same axis as discomfort.

Biology anchor cluster:
- **Eastwood et al. 2012 (Perspect Psychol Sci)** "The Unengaged Mind" — boredom as functional state of failed engagement.
- **van Tilburg & Igou 2017** — boredom as functional emotion that prompts pursuit of meaningful activity.
- **Westgate & Wilson 2018 (Psychol Rev)** — meaning-and-attentional-component (MAC) model: boredom as engagement / opportunity misalignment.
- **Bench & Lench 2013** — boredom proneness as predictor of risk-taking and stimulation-seeking.
- **Csikszentmihalyi 1990** — flow as engagement-arousal match; boredom as one corner of the skill/challenge mismatch space.
- **Ulrich-Lai & Herman 2009 (Nat Rev Neurosci)** — chronic stress of low-control / understimulation regimes (HPA axis).

Distinct from MECH-314 curiosity: curiosity rewards positive novelty / learning progress; boredom punishes their absence. The two are not inverse — you can be in genuinely novel territory and still bored if no engagement opportunity exists; conversely you can be in familiar territory and not bored if engagement is rich.

Likely two timescales (probably separate child claims): **acute restlessness** (~minutes / tens of episodes) and **chronic anhedonic flatness** (~episodes / sessions).

### ARC-068 — opportunity cost no-op penalty (negative-side, score-additive)

Trajectories that consume time without progress pay a cost in E3 scoring proportional to a tonic expected-reward-rate scalar. Composes with ARC-066: the same capacity scalar that biases toward action ALSO inflates the cost of passivity, so the two work on opposite ends of the score axis.

Biology anchor cluster:
- **Niv et al. 2007 (PNAS)** — average reward rate as discount on rest. Resting trades guaranteed-zero now for continued-zero later, against a positive expected baseline.
- **Kurzban et al. 2013 (Behav Brain Sci)** — effort and opportunity cost as the felt motivation to disengage when better alternatives become available.
- **Kolling et al. 2015 (Curr Opin Neurobiol)** — dACC foraging-value: switch FROM current option when value falls below environmental average.
- **Salamone et al. 2003 (Behav Brain Res)** — DA-depleted animals accept low-effort low-reward over high-effort high-reward; cost computed against opportunity baseline.
- **Constantino & Daw 2015** — foraging behaviour modelled with opportunity-cost discounting predicts patch-leaving better than fixed-discount RL.

Cleanest existing substrate boundary to disambiguate: **SD-032b dACC adaptive control** carries a foraging_value (Kolling 2015 framing) that biases mode-switch when current option falls below environmental average. ARC-068 is similar but cleaner — biases the SCORE of any passive trajectory regardless of mode. They compose at different architectural levels (mode-switch vs trajectory-score) and aren't redundant.

---

## How the three compose

ARC-066 and ARC-068 work at the **E3 score** layer. ARC-067 works at the **z_harm valence** layer.

```
E3 score(trajectory) =
    expected_harm_cost
  - expected_benefit
  + dacc_score_bias              [SD-032b]
  + lateral_pfc_bias             [SD-033a]
  + ofc_bias                     [SD-033b]
  + mech295_liking_bias          [MECH-295]
  + curiosity_bonus              [MECH-314]
  + gated_policy_bias            [ARC-062 / GatedPolicy]
  + noise_floor_temperature_lift [MECH-313]   # at softmax stage
  - vigor_action_bias            [ARC-066, NEW: directional toward action]
  + opportunity_cost_no_op       [ARC-068, NEW: cost on passive trajectories]

z_harm_a aggregate also sums:
  + boredom_aversive             [ARC-067, NEW: engagement-rate accumulator]
```

ARC-066 and ARC-068 are mathematical complements. Some child MECH designs may collapse them into a single signed scalar (capacity-keyed pressure that adds to action scores AND subtracts from passive scores). The slot-level registration keeps them separate so the design space stays open; the child MECH chooses the parameterisation.

ARC-067 is on a different layer because boredom *feels* aversive — it recruits the same affective channel as physical discomfort. Routing through z_harm_a (affective stream, SD-011) gives that phenomenology automatically: chronic boredom should produce z_harm_a-like consequences (descending modulation, AIC urgency, downstream ARC-058 affective-PE substrate consumption).

---

## What this commits REE to

A category not previously in the substrate: **behaviour from surplus**. Every existing behavioural source is keyed to a deficit (threat, depletion, novelty-as-information-gap). The non_deficit_action_drives family asserts that biological behaviour also comes from the *complement* condition — high capacity, low engagement, accumulating opportunity cost — and that REE needs explicit architectural slots for this.

Falsifiable family-level prediction: an REE agent with all current drives + curiosity + override + sleep + dACC + closure operator ON, in a familiar safe environment with full energy, no specific z_goal, and no novel inputs, will be **behaviourally inert** — action density at MECH-313 noise floor only. With the three non_deficit_action_drives slots instantiated, action density should rise monotonically with the capacity scalar, and the agent should exhibit exploratory action even with all deficit-side drives at zero.

This is testable on SD-054 (reef substrate) or any environment that can hold the agent in the well-fed-safe-familiar regime for a long episode horizon.

---

## What this is NOT

- **Not a depression / anhedonia model.** ARC-067 ablation is the model of clinical anhedonia / abulia / catatonic flatness; the substrate-present case is the healthy baseline. Future cross-reference to `psychiatric_failure_modes.md` appropriate.
- **Not a re-implementation of MECH-313 LC-NE noise.** ARC-066 and MECH-313 share an LC-NE biological substrate but instantiate different LC-NE functions (directional action bias vs noise floor). Both can hold simultaneously.
- **Not a vigor-of-execution timing parameter.** ARC-066 names the WHETHER-to-act axis. The HOW-FAST-to-act axis (Niv 2007 also covers this) is a candidate future MECH/Q-claim, not part of the current slot registration.

---

## Child MECH/SD design — what's needed before phasing

All three slots require **lit-pulls** before child MECH/SD design. The biology anchors above are sufficient to motivate slot registration but not to fix mechanism shape. Per project rule (`feedback_biology_before_formal_definitions`), formal-concept claims need a biology lit-pull *before* registration; for ARCs at the slot level the requirement is lighter, but child MECH design requires the full pull.

Three independent lit-pulls likely:

1. **`targeted_review_arc_066_tonic_vigor/`** — average reward rate, LC-NE tonic direction, DA effort-vigor, BAS tonic level. Disambiguate Niv 2007 average-reward-rate (slow integrator over reward history) from Aston-Jones LC-NE tonic (state-conditioned arousal mode) from Salamone DA effort-vigor (action-cost computation). The three are convergent in phenomenology but mechanistically distinct.
2. **`targeted_review_arc_067_boredom/`** — Eastwood / Westgate / van Tilburg engagement-failure literature; flow / arousal mismatch; clinical anhedonia / abulia substrate; HPA / glucocorticoid response to chronic understimulation. Pick implementation shape: (a) functional-emotion engagement-search trigger, (b) attentional-failure account, (c) opportunity-cost-felt overlap with ARC-068.
3. **`targeted_review_arc_068_opportunity_cost/`** — Niv 2007 average-reward-rate-as-rest-discount, Kurzban 2013 felt-cost-of-staying, Constantino & Daw 2015 opportunity-cost discounting, Salamone 2003 DA-depletion effort selection. Critical disambiguation: the boundary between ARC-068 and SD-032b dACC foraging. Pick a cleanly discriminative implementation.

After each lit-pull, child MECH design can proceed independently. The three slots are loosely coupled — no slot blocks any other — but their child mechanisms will likely be wired in the same agent block (REEAgent.select_action E3 score-aggregation chain) and will need contract-level testing for non-interaction in the OFF state.

---

## Child mechanisms registered to date

All three family lit-pulls complete (2026-05-10). Child MECH design executed 2026-05-16.

### ARC-066 child mechanisms
- **MECH-320** (registered 2026-05-10) — `tonic_vigor_coupling_score_bias`. Child mechanism for ARC-066 AND ARC-068 (collapsed implementation, see below). Adds an additive vigor bias on E3 action-trajectory scoring (positive addend on action candidates, negative addend on no-op candidates via w_passive term), where v_t is a slow EWMA over the realised E3-score-receipt stream gated by secondary internal-state modulators (energy / drive / PE). Substrate: mesolimbic DA-vigor (Niv 2007 formalism, Salamone & Correa 2012 substrate identity, Beierholm 2013 human causal test). R3 falsifiable secondary alternative (multiplicative gain) discriminable from primary via parametric sweep on a pre-existing action preference. Substrate landed 2026-05-10 in `ree-v3/ree_core/policy/tonic_vigor.py`.

### ARC-067 child mechanisms
- **MECH-330** (registered 2026-05-16) — `idle_aversion_acute_restlessness_accumulator`. First child mechanism for ARC-067, acute timescale (~minutes / tens of episodes). Three-input executive engagement-rate estimator (commit transitions, E3 deliberation depth, residue-write rate) -> slow accumulator with threshold -> writes negative valence to z_harm_a affective stream (SD-011 routing per Danckert 2018 AIC-deactivation and Wilson 2014 Science self-shock exchangeability). MAC meaning-component secondary channel reuses existing z_goal substrate (SD-012 / MECH-308). One-way cross-talk: seeds MECH-331 on sustained non-discharge.
- **MECH-331** (registered 2026-05-16) — `idle_aversion_chronic_anhedonic_flatness_substrate`. Second child mechanism for ARC-067, chronic timescale (~sessions / episode-blocks). Slow frontostriatal effort-allocation integrator seeded by sustained MECH-330 activation; scales DOWN z_harm_a write amplitude from MECH-330 via gain gate (gain_floor > 0). Implements the apathy archetype (preserved capacity, preserved hedonic experience, impaired effort-to-act mobilisation). HPA-axis substrate context (Ulrich-Lai & Herman 2009). Introduces across-episode persistent state; infrastructure deferred to substrate-landing time.

### ARC-068 child mechanisms
- **MECH-320 w_passive term** — ARC-068 collapses into MECH-320 per ARC-068 lit-pull R3 verdict (2026-05-16). Niv 2007's derivation is symmetric: the same average-reward-rate scalar produces (a) positive bias on action vigor (ARC-066 = MECH-320 positive addend) and (b) additive cost on time-spent-passive (ARC-068 = MECH-320 w_passive term). No separate MECH registered for ARC-068; ARC-068 slot-level registration preserved to allow future re-splitting if psychiatric failure-mode dissociations (anhedonia vs mania) motivate separate scalars.

## See also

- `claims.yaml` — ARC-066 / ARC-067 / ARC-068 / MECH-320 / MECH-330 / MECH-331 entries (full functional_restatement and notes).
- `evidence/literature/targeted_review_arc_066_tonic_vigor/synthesis.md` — ARC-066 lit-pull (R1-R4 verdicts, lit_conf 0.789).
- `evidence/literature/targeted_review_arc_067_boredom/synthesis.md` — ARC-067 lit-pull (R1-R5 verdicts, lit_conf 0.72-0.76).
- `evidence/literature/targeted_review_arc_068_opportunity_cost/synthesis.md` — ARC-068 lit-pull (R1-R4 verdicts, lit_conf 0.78-0.82).
- `MECH-313` — LC-NE tonic noise floor (ARC-065 child). Per ARC-066 R2 verdict, MECH-313 fully covers the LC-NE substrate; MECH-320 is mesolimbic-DA-attributed, NOT LC-NE.
- `MECH-216` — predictive wanting (target-conditioned; ARC-066 is target-free).
- `SD-012` — homeostatic drive (deficit-keyed; ARC-066 is capacity-keyed inverse).
- `SD-032b` — dACC adaptive control / foraging_value (closest existing relative to ARC-068; boundary is kernel timescale: ARC-068 uses long-window historical EMA, SD-032b uses current-environmental scalar per Kolling 2016).
- `SD-037` — broadcast override / orexin (deficit-recruited; ARC-066 is surplus-recruited; opposite corners of state space).
- `SD-011` — affective harm stream (z_harm_a routing for MECH-330 boredom aversive).
