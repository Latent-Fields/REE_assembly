# STUDY-HUM-1 -- Humour as a Societal Epistemic Probe

Status: design (pre-pilot)
Registered: 2026-08-14
Raw thought: `docs/thoughts/2026-08-14_humour_societal_epistemic_probe.md`
Claims: SOC-HUM-1 (theory), SOC-HUM-2/3/4 (hypotheses H1/H2/H3)
Depends on: MECH-110 (individual-level laughter mechanism)

> **Scope flag.** This is an *adjacent-to-REE* research thread. Its test domain is
> societal humour corpora + independent public-opinion series -- NOT the V3 experiment
> substrate. The claims are registered `epistemic_category: out_of_domain` so governance
> does not wait for a V3 run. The connection to REE is conceptual and reciprocal: the
> mechanism (de-committed probe re-opening a gridlocked node) is the REE commitment /
> spike-before-commit pattern at societal scale, and the "blocked node in the claim
> index" is the working analogy for a gridlocked societal norm-conflict.

---

## 1. Core claim under test (SOC-HUM-1)

In domains of implied threat, comic treatment of a contested norm acts as a
**low-commitment, deniable probe**, and the *time-trajectory* of that humour tracks the
epistemic state of the underlying conflict. A joke floats a heterodox interpretation
without committing anyone to it ("I'm only joking"), so it evades the defensive
counter-opposition that a bald assertion triggers; laughter is the assay readout of
whether the reframe is societally viable yet.

This is **one** of humour's functions, not a theory of humour. Humour separately does
affiliation, status negotiation, play/rehearsal, and cognitive reward. Null results here
say nothing about those. Scoping it narrowly is deliberate -- over-broad theories of
humour are the ones that die; an isolable mechanism can be tested.

Theoretical anchors (independent, pre-existing): **benign-violation** (McGraw & Warren --
funny requires a simultaneous violation and safety) and **relief theory** (tension
discharged by reframing). The novel addition is the **societal-gridlock** frame: humour
re-opens a "blocked node" that direct assertion only entrenches.

---

## 2. Hypotheses (each with its null)

- **H1 -- Dating tracks resolution (SOC-HUM-2).** A conflict's comedic prevalence rises
  while contested, then declines after the norm resolves -- and the decline is preceded
  by a **target-flip**: the butt shifts from the *transgressor* to the *old norm itself*.
  *H0: prevalence decline is independent of the (independently measured) resolution.*

- **H2 -- Persistence tracks irreducibility (SOC-HUM-3).** Topics with flat,
  non-declining curves across the whole time-base map preferentially onto **genuinely
  irreducible** human tensions (mortality, scarcity, the sexes, power, hypocrisy) rather
  than merely-hard-but-solvable ones. *H0: persistent topics are unrelated to a blind
  solvability rating.*

- **H3 -- Direction predictor (SOC-HUM-4).** Self-implicating framing ("we're all like
  this") co-occurs with / precedes resolution; out-group-weaponised framing co-occurs
  with entrenchment (non-resolution or polarization). *H0: framing direction is unrelated
  to resolution outcome.*

---

## 3. Measurement backbone -- TWO independent axes (the part that makes it science)

The whole design stands or falls on having a resolution signal that does **not** come
from the humour itself. Otherwise it is circular (use jokes to define resolution, then
"discover" that jokes track resolution).

1. **Humour axis** (from the corpus), per conflict-topic per time-bin:
   - *Prevalence* as SHARE-of-corpus, never raw count (the industry grew; normalise).
   - *Target-of-violation* code: {transgressor, old-norm, out-group, self}.
   - *Benign-vs-taboo* flag: content warnings, backlash, platform removal, "can't joke
     about that any more" markers.
2. **Resolution axis** (external, non-humour), for the SAME conflicts over the SAME years:
   longitudinal opinion series (GSS, Gallup, Eurobarometer, Pew), legislation/court dates,
   norm surveys.

The test is whether the SHAPE of the humour curve predicts/tracks the independent
attitude curve. No external axis -> not a study.

---

## 4. Primary validity threat -- resolution-death vs taboo-death

Disappearance from humour is **two-valued with the same signature**:
- **Resolution-death:** the norm shifted, the violation is now trivial, the joke is boring.
- **Taboo-death:** the violation stopped being *benign* -- now genuinely offensive, so
  un-jokable.

Opposite epistemic states, identical "topic went away" observable. The
**target-of-violation code is the primary instrument** that separates them:
resolution-death flips the butt onto the old norm; taboo-death just stops or triggers
backlash. **If that code cannot reliably distinguish the two, H1 is untestable and the
instrument has failed -- stop.**

Secondary confound: **context-decay** -- topical/referential jokes die because the shared
reference decayed, not because anything resolved. Control by restricting to evergreen
STRUCTURAL conflicts, or by modelling reference half-life separately.

Other threats: comedian/broadcast **selection bias** (what got recorded); **survivorship**
of recordings; changing **industry size** over time (handled by share-normalisation).
Free partial control: material only survives to a recorded special if it landed in clubs,
so a specials corpus approximates **landed probes**, not mere attempts.

---

## 5. The finding that would make it matter -- lead vs lag

With both axes in hand, the **lead-lag direction** is the crux:
- Humour decline **lags** the attitude shift -> humour *marks* resolution (society settled,
  then stopped joking).
- Target-flip **leads** the attitude midpoint -> humour may *drive* resolution (the joking
  did the work).

Observational corpora cannot prove causation, but a consistent *lead* is the strongest
available signal that humour does epistemic WORK rather than merely narrating it. That is
the thesis, made empirical. State up front that a lead is suggestive, not dispositive.

---

## 6. Which functions this instrument sees

Topic/conflict data is well-targeted at the epistemic-unblocking function and relatively
**blind** to the other four (affiliation, status, play, reward live in delivery, timing,
and the comedian-audience relationship, not in topic). This is a feature: the instrument
isolates the function under test instead of smearing across all five.

---

## 7. Corpora (usable time-bases)

- **Stand-up specials** -- dense, recent; already club-filtered to landed material.
- **Late-night monologues** -- fine time-resolution; tests the fast/ephemeral end.
- **Century-scale base** -- *Punch* (1841-2002), *New Yorker* cartoon archives -- lets
  resolution be observed over the long horizon where norms actually move.

---

## 8. Pre-registered falsifiers

- Prevalence decline unrelated to the independent attitude series -> **H1 dead**.
- Persistent topics randomly distributed over blind-rated solvability -> **H2 dead**.
- Target-of-violation code cannot split resolution- from taboo-death -> **instrument
  dead**, stop before scaling.
- Framing direction (self vs out-group) unrelated to resolution outcome -> **H3 dead**.

---

## 9. MVP spike BEFORE any pipeline (the study takes its own medicine)

Do not build the corpus pipeline first. Run the cheap diagnostic:

1. Pick **3-5 conflicts with well-documented attitude shifts** where independent opinion
   data already exists.
2. Assemble a modest transcript sample spanning each shift.
3. Hand-code target-of-violation over time.
4. Eyeball whether humour-curve shape + target-flip relate to the attitude curve, and
   whether the target-flip leads or lags.

If the pilot shows nothing on cases hand-picked *to* show it, the theory is probably wrong
and the cost was days, not months. This is the REE `complex (probe-gated)` ->
cheap-diagnostic-first discipline applied reflexively to the study itself.

---

## 10. Status / next steps

- [ ] MVP spike (Section 9) -- 3-5 hand-picked conflicts, hand-coded. **Gate: do not scale
      unless the pilot separates resolution- from taboo-death AND shows any curve relation.**
- [ ] If pilot passes: specify the target-of-violation coding manual + inter-rater check.
- [ ] Source the independent opinion series for the candidate conflicts (GSS/Gallup/Pew).
- [ ] Only then: corpus assembly + topic modelling at scale.

This is a `/lit-pull` + design thread, not a `/queue-experiment` substrate run -- it does
not belong in `ree-v3/experiment_queue.json`.
