# Targeted review — competence bootstrap without a demonstrator

**Claim under review:** CDQ-007
**Pulled:** 2026-07-18T07:07:52Z
**Sources:** 8 (7 PubMed-indexed with DOIs, 1 older behavioural study via Consensus)
**Status:** INFORMING ONLY — this review does not adjudicate the CDQ-007 discrimination and does not recommend a build.

This pull is the mandatory biology precondition under the `biology_before_formal_definitions`
invariant: instantiate the biological story before importing the formal/engineering solution.
The research question was posed as biology, not engineering — *how do animals bootstrap competent
goal-directed action without a demonstrator?* — and the entries below were selected to give
even-handed coverage of both open legs, including the sources that cut against each.

---

## Entries

| Entry | Source | Class | Direction | Conf. |
|---|---|---|---|---|
| `..._locomotor_primitives_dominici2011` | Dominici et al. 2011, *Science* | multi-muscle EMG, comparative | supports | 0.82 |
| `..._self_generated_movement_cpg_zeng2021` | Zeng et al. 2021, *Curr Biol* | embryonic imaging + deprivation | mixed | 0.70 |
| `..._innate_investigatory_drive_ahmadlou2021` | Ahmadlou et al. 2021, *Science* | optogenetic circuit dissection | supports | 0.78 |
| `..._seeking_information_drive_kesner2022` | Kesner, Calva & Ikemoto 2022, *Prog Neurobiol* | theoretical review | supports | 0.62 |
| `..._dopamine_necessity_feeding_szczypka2001` | Szczypka et al. 2001, *Neuron* | genetic necessity + rescue | supports | 0.75 |
| `..._untutored_sequence_selforganization_mackevicius2023` | Mackevicius et al. 2023, *eLife* | calcium imaging, delayed tutoring | mixed | 0.80 |
| `..._ghost_control_emulation_veit2023` | Veit et al. 2023, *Anim Cogn* | behavioural, ghost control | weakens | 0.72 |
| `..._untutored_song_abnormal_volman1995` | Volman et al. 1995, *J Comp Psychol* | behavioural, isolate rearing | supports | 0.55 |

---

## 1. Innate motor primitives, CPGs, and species-typical fixed action patterns

The clearest finding in this literature is that **development refines a pre-specified action basis;
it does not construct one.** Dominici et al. factorised multi-muscle EMG across human neonates,
toddlers, preschoolers and adults and found the two neonatal patterns of lumbosacral motoneuron
activation *retained* into adulthood, augmented by two new patterns first appearing in toddlers —
against the standing assumption that primitive control is suppressed and replaced. The same
primitives appear in rat, cat, macaque and guineafowl, which is a strong argument that the basis
set is ancestral rather than learned.

This is the level at which the precocial/altricial contrast is most instructive, and it is worth
saying what it does and does not license. Precocial species express near-complete locomotor and
feeding repertoires within hours of hatching, altricial species take weeks — but Dominici's result
suggests the difference is one of *maturational schedule over a shared basis*, not one of
"precocial species have primitives and altricial species learn theirs". No source in this pull
supports the latter reading.

The important qualification comes from Zeng et al., who show the innate seed circuit is **not
sufficient on its own**. Drosophila embryos deprived of proprioceptive feedback fail to develop
functional locomotor CPGs. An identified pioneer premotor circuit autonomously generates rhythmic
plateau potentials, those drive muscle contraction, the contraction produces proprioceptive
feedback, and *that feedback* is required for the gap-junctional coupling that assembles the mature
CPG. So the biological bootstrap is demonstrator-free but **not experience-free**: an innate
activity generator supplies its own curriculum through a closed loop.

**What this section establishes:** the action *alphabet* is innate and refined. It establishes
nothing about where goal-direction comes from — innate primitives supply what an agent *can do*,
not what it is *for*.

## 2. Innate, non-extinguishing approach drives

Three entries bear here, and they separate cleanly into what is well established and what is not.

**Well established — the drive exists as a separable substrate.** Ahmadlou et al. identify
inhibitory medial zona incerta neurons as *essential for the decision to investigate* an object or
conspecific, receiving prelimbic drive and instigating investigative action by inhibiting the
periaqueductal gray. This is action *initiation* toward salient stimuli, causally dissected, with
no learned reward association required. Kesner et al. review the broader architecture and make the
claim explicit: exploratory behaviour occurs in the absence of clear goal or reward, is regulated
by an innate drive, and is implemented by supramammillary→hippocampal (cognitive) and
supramammillary→medial-septal→VTA (vigour) pathways — with phasic dopamine reframed as signalling
potentially-important stimuli rather than rewards. Biology keeps the drive channel and the
prediction-error critic architecturally distinct.

**Well established — the drive is necessary for expression.** Szczypka et al. is the necessity
result CDQ-007 asked for. Dopamine-deficient mice perceive food, possess the motor apparatus, and
retain hedonic reactivity (preference returns immediately on regional dopamine restoration) — and
they starve. Regional rescue dissociates the components: caudate putamen restores feeding and
nest-building, accumbens restores exploration. An animal that can see, can move and can value, but
does not go, is exactly the profile the REE converter presents.

**NOT established — that the drive is non-extinguishing.** This is the load-bearing property for
the H-approach-primitive leg and no source in this pull measures it. Ahmadlou et al. do not test
extinction under sustained non-reward; non-extinction is inferred from reward-independence, which
is weaker. Worse, Kesner et al.'s proposed currency is *environment prediction error* — an
error-driven quantity that **quiesces as the world-model improves**. On that account a
well-modelled environment would silence the drive, which is close to the opposite of what a
cold-start requires. The biology supports a *separable, reward-independent, necessary* drive
channel. It does not yet support a *non-extinguishing* one.

**NOT established — that the drive is sufficient to acquire competence.** Szczypka is
loss-of-function in an animal that already has the repertoire: necessity-for-*expression*, not
necessity-for-*acquisition*. The REE question is an acquisition question, and this gap is not
closed by any source here.

## 3. Observational / social learning, and whether an early prior is outgrown

Mackevicius et al. is the most informative entry in the pull because it runs both legs inside one
experiment. Delaying tutor exposure in juvenile zebra finches and imaging HVC shows (a) neural
sequences emerge **without any tutoring**, so tutor experience is not necessary for sequence
formation; (b) after tutor exposure, those pre-existing sequences become **tightly associated with
newly learned syllables** — the demonstrator-derived content binds onto the self-organized
scaffold; and (c) only half the delayed birds learned, and the failures were exactly those whose
pre-tutoring sequences were most **crystallized** around their own untutored song.

Volman et al. supply the behavioural endpoint the imaging does not: untutored zebra finches sing
*structured but abnormal* song. Innate machinery gets the learner to structured; the demonstrator
closes the gap to species-typical. They also report that untutored siblings copy *each other* as
much as tutored birds copy adults — which makes "no demonstrator" nearly unrealisable in a social
species, since any peer is a partial demonstrator.

Veit et al. is the counterweight. Pigs given a conspecific demonstrator, a human demonstrator, a
**ghost control** (self-moving objects, no agent), or a ghost-plus-bystander all solved a two-step
foraging apparatus equally well, and all beat non-observers. The conclusion is emulation: the
animals learned about the *apparatus*, not the *actions*. What a demonstration transmits, at least
in an affordance-dominated task, is **task structure, not policy** — and a non-social channel can
carry it.

**On transience — the biology inverts the expected worry.** CDQ-007 asked whether an early
demonstrator-derived prior is later outgrown. Mackevicius suggests the pressing risk runs the other
way: it is the *self-generated, untutored* structure that hardens and locks the learner out of
later demonstrator-derived improvement. The demonstrator-derived prior in that system is not a
crutch to be shed; it is an input with a *closing window*. This is a framing correction, not an
answer, and it rests on a maturational clock a REE converter does not have.

---

## Bearing on the H-bc-prior vs H-approach-primitive discrimination

**This section informs the discrimination. It does not adjudicate it, and it does not recommend a
build.** The REE converter's failure — invariant across four eliminated axes, readiness met on
every leg, every treatment arm at the ~0–1 foraging floor, with behavioural cloning (32.72) the
sole floor-clearing existence proof — is not resolved by anything below. What follows is the
evidence-direction ledger only.

### H-approach-primitive (innate, non-extinguishing, demonstrator-free approach drive)

**Evidence FOR:**
- **The drive exists as a distinct, genetically specified substrate.** Ahmadlou et al. give a
  causally dissected circuit (ZIm) whose function is converting stimulus presence into engagement,
  independent of learned reward value (conf. 0.78).
- **It is architecturally separate from the reward critic.** Kesner et al. place seeking on
  supramammillary→septal→VTA circuitry distinct from RPE machinery, with phasic DA reframed as
  salience rather than reward (conf. 0.62). If REE's converter is missing a channel rather than
  mistuning one, biology has that channel.
- **It is necessary for goal-directed action in an otherwise-intact agent.** Szczypka et al.:
  perception intact, motor intact, hedonics intact, and the animal still starves (conf. 0.75).
  This is the closest biological analog of "readiness met on every leg, foraging at floor".
- **Demonstrator-free bootstrap is a real phenomenon.** Zeng et al. (self-generated movement
  builds the CPG, conf. 0.70) and Mackevicius et al. (sequences self-organize with no tutor,
  conf. 0.80) are both existence proofs that competence machinery can assemble with zero
  conspecific input.
- **The action basis is innate everywhere it has been looked at.** Dominici et al., across four
  developmental stages and five species (conf. 0.82). "Learner with no action prior fails" is the
  biological default outcome, not an anomaly.

**Evidence AGAINST:**
- **Non-extinction is unmeasured, and the best-specified account points the other way.** Kesner et
  al.'s environment-prediction-error currency *quiesces* as the world-model improves. No source
  here tests a drive that survives sustained non-reward. This is the single sharpest objection in
  the pull, and it lands on the property the leg most needs.
- **An innate generator alone is insufficient.** Zeng et al.: deprived of the feedback its own
  activity produces, the innate seed circuit fails to mature. "Add a drive" is underspecified
  unless one also names what the drive's output trains.
- **Necessity ≠ acquisition.** Szczypka is a knockout in an animal that already possesses the
  repertoire — necessity-for-expression, not for cold-start acquisition. The gap is unbridged.
- **Innate primitives are the alphabet, not the objective.** Dominici demonstrates an innate motor
  basis and says nothing about goal-direction. An agent with primitives and no goal-composition
  still forages at floor.
- **Self-organized structure can become a barrier.** Mackevicius: the birds that failed to learn
  were those whose *untutored* sequences had crystallized.

**Left open:** whether any biological approach drive is genuinely non-extinguishing under sustained
non-reward; whether such a drive is sufficient (not merely necessary) to *acquire* competence from
a cold start; what a drive's output would have to train in REE for the Zeng-style closed loop to
have an analog.

### H-bc-prior (competence-directed behavioural-prior / imitation seed)

**Evidence FOR:**
- **Demonstrator-free bootstrap reaches structured, not species-typical.** Volman et al.:
  untutored finches sing — abnormally (conf. 0.55). The innate route has a ceiling the demonstrator
  lifts.
- **A demonstrator-derived prior binds onto innate scaffolding and produces the competent form.**
  Mackevicius et al.: post-tutor, pre-existing sequences become tightly associated with newly
  learned syllables (conf. 0.80). This is close to the mechanistic picture a BC seed would need.
- **Observers beat non-observers, robustly.** Veit et al.: every observer condition outperformed
  non-observers on both engagement and success (conf. 0.72). An external informational prior was
  required; the pigs given nothing did worse.
- **Social species manufacture demonstrators.** Volman et al.: untutored siblings copy each other
  as much as tutored birds copy adults — suggesting the demand for an external behavioural prior is
  real enough that learners will source one from whatever is available.

**Evidence AGAINST:**
- **The demonstrator need not be an agent, and need not supply a policy.** Veit et al.'s ghost
  control matched a live conspecific. What transferred was *affordance/task-structure* information,
  not actions (conf. 0.72). If BC's 32.72 works because it transmits structure, a non-imitative
  structural channel could substitute — and the imitative reading of the leg is then wrong.
- **The scaffold does not require a demonstrator.** Mackevicius: sequences form fully without
  tutoring. Whatever the demonstrator contributes, it is not the sequencing machinery.
- **Untutored is degraded, not floored.** Volman et al.'s isolate birds still sing structured
  song. The biological demonstrator-deprivation failure mode is a *ceiling* deficit, not the
  near-zero *floor* REE observes — so the analogy supports "a prior raises the ceiling" much better
  than "a prior is required to leave the floor". This is a substantive mismatch between the
  biological evidence and the REE phenomenon it is being brought to bear on.
- **The prior has a closing window rather than being permanent.** Mackevicius: only half the
  delayed birds learned. A demonstrator-derived prior is usable only while the substrate is
  plastic.

**Left open:** whether a structural/affordance prior (ghost-control-equivalent) would suffice in a
temporally extended foraging task where action selection, not affordance discovery, is the
difficulty; whether the biological ceiling-deficit failure mode has any bearing on a floor-level
failure; whether the "outgrown" question is even well-posed given that biology's version of the
risk is the *opposite* one (premature crystallization of self-generated structure).

### What the biology does not settle

No source in this pull runs the decisive comparison. Nothing here contrasts *drive-only* against
*prior-only* in the same organism on the same task from a genuine cold start. The two legs appear
in biology as **complementary stages in sequence** (innate scaffold + drive, then demonstrator-
derived content bound onto it while plastic), not as competing alternatives — which is itself
informative about the framing, but is not a verdict on which is load-bearing for the REE converter,
and must not be read as one.

Three specific transfer risks apply across the whole pull and should travel with any downstream
use: (1) the biological failure mode under demonstrator deprivation is *degraded competence*, not
*floor-level failure*; (2) every demonstrator-necessity result comes from systems with maturational
clocks and critical periods that REE has no analog for; (3) the necessity evidence for approach
drive is expression-necessity in already-competent animals, not acquisition-necessity in naive
ones.
