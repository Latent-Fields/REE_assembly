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

- [x] **MVP spike (Section 9) -- DONE 2026-08-15. Verdict: GO (qualified).** Full memo:
      `evidence/planning/humour_epistemic_probe_mvp_spike_2026-08-15.md`. Four cases:
      C1 homosexuality/SSM + C2 interracial-marriage (resolution/H1), C3 mortality
      (persistence/H2), C4 nagging-wife jokes (adversarial). **Gate met on both arms:**
      (i) the target-of-violation code separates resolution- from taboo-death non-trivially
      (C1 anti-gay + C2 overt-racist forms taboo-died while old-norm forms rose; C4 the code
      correctly reads taboo-death and *dissents* from the naive "vanished->resolved"
      inference); (ii) humour target-flip relates to the independent opinion axis and
      *leads* it in the two clean cases (C1 ~5-12y, C2 ~20y). **Two carried caveats:**
      the lead-lag reading is contaminated by analyst hindsight and must be re-run on dated
      primary sources (memo condition 1); and C4 is a partial counterexample to H1's strong
      form -- a norm resolved (~1985, GSS FEFAM) with only a weak/late flip, so "resolution
      is preceded by a target-flip" is *sufficient-signal*, not *necessary-precursor* (memo
      condition 2). GO is for the **instrument**, not the causal thesis (untestable by hand).
- [~] **NEXT (GO path): target-of-violation coding manual + inter-rater reliability check
      FIRST** -- **PROTOCOL WRITTEN 2026-08-15:**
      `evidence/planning/humour_epistemic_probe_coding_manual_pilot.md`. Paired held-out,
      blind design: Arm A marijuana legalization (resolution/H1, Gallup midpoint ~2012-13)
      tests **sensitivity** (does the blind code recover the target-flip?); Arm B personal
      financial scarcity (persistence/H2) tests **specificity** (does it correctly report
      NO flip?). Operational definitions for the four target codes + benign/taboo flag,
      the inequality-exclusion unit-of-analysis rule, sampling frame (1995-2020, 5-yr bins,
      ~100-150 dated instances), full blinding protocol, and three GO gates (kappa >=~0.6
      with no dominant transgressor<->old-norm confusion; Arm A flip recovered; Arm B stays
      flat/self). **Remaining to run:** assemble the dated sample from primary sources, hand
      to two raters, compute kappa. Awaiting user's go-ahead to execute.
- [ ] Source the independent opinion series (Gallup SSM + Gallup interracial-marriage +
      GSS FEFAM already anchored in the spike memo; add Pew acceptance-of-homosexuality,
      Eurobarometer cross-checks).
- [~] **SECOND PILOT PROMOTED 2026-08-15: Ireland, the referendum lead-lag natural experiment.**
      Protocol: `evidence/planning/humour_epistemic_probe_ireland_referendum_pilot.md`. Runs
      AFTER the US coding-manual pilot passes. Tests transportability of the instrument, the
      **lead-lag crux** against discrete dated referendums (SSM 2015-05-22 62% Yes; Repeal 2018-
      05-25 66% Yes), and the SOC-HUM-5 medium sub-question. See Section 11.
- [ ] Source the independent opinion series (Gallup SSM + Gallup interracial-marriage +
      GSS FEFAM already anchored in the spike memo; add Pew acceptance-of-homosexuality,
      Eurobarometer + Irish referendum record cross-checks).
- [ ] Only then: corpus assembly + topic modelling at scale -- with lead-lag **quarantined**
      until it runs on dated primary sources, and the C4 "opinion-resolved-but-humour-taboo-died"
      cell treated as a first-class outcome, not noise.

---

## 11. Cross-cultural scope and the medium-externalization sub-question (candidate SOC-HUM-5)

Sections 1-10 are implicitly **American**, because the humour axis needs canonical, dated,
broadcast humour media, and the US industrialised that. This raises a genuine subquestion of the
original idea -- registered here as **candidate SOC-HUM-5** (to be registered in `claims.yaml` via
the thought-intake / governance route, NOT by a design session):

> **SOC-HUM-5 (candidate).** The humour-as-epistemic-probe mechanism (SOC-HUM-1) is
> substrate-universal, but its *observable trace* is externalised through culture-specific media of
> differing recordability. Therefore (a) recorded-humour **volume** is confounded with medium and is
> **not** cross-culturally comparable; and (b) only the within-culture **target-flip structure** and
> its **timing** relative to that culture's own resolution axis is comparable.
> *Null:* the flip-structure, where measurable, does not transport across cultures in a way tied to
> the mechanism rather than to recordability.

**Why this matters and is not merely a data-availability caveat:** the medium bias is confounded
with the very thing measured. A culture that resolves norms through dense *oral, small-world*
humour would register as having *less* humour activity purely because less is recorded -- when the
mechanism may be *more* active there. So the deliverable is never a global volume comparison; it is
a within-culture claim ("within each culture with an adequate corpus and a clean resolution axis,
the flip appears and leads/lags consistently"), compared across cultures on **structure only**.

**Four tiers of applicability:**

- **American** -- calibration case, both axes dense (specials/late-night + Gallup/GSS). The US pilot.
- **European** -- good resolution axis (Eurobarometer, ESS, referendums); humour axis nationally
  siloed by language (UK broadcast satire; German *Kabarett*, explicitly societal-critique; French
  cartoon/cabaret). Per-country corpora, compared on structure.
- **Irish** -- the paradox and the **sharpest** case: oral/small-world humour (thin recorded layer)
  BUT the world's cleanest resolution axis (discrete dated referendums) flipping a **shared** old
  norm (the Catholic Church). **Promoted to an actual second pilot** -- see
  `humour_epistemic_probe_ireland_referendum_pilot.md`. Dave Allen (1970s) and *Father Ted*
  (1995-98) already sit in the recorded trail as Church-as-butt deep-lead anchors, decades before
  the 2015/2018 votes.
- **Worldwide** -- the honest ceiling: the *mechanism* may be universal, *this measurement* is not
  culture-neutral. "Worldwide" means medium-appropriate proxies per culture, never a global volume
  comparison.

The upside: the medium bias becomes a **testable sub-hypothesis**, not just a limitation -- and
Ireland's referendum axis is the single sharpest place to test whether the flip *leads a discrete
resolution event*, which the US poll-drift cases can only blur.

---

## 12. The normative payoff, and its exact dependency on the evidence (candidates SOC-HUM-6, SOC-HUM-7)

Two further candidate claims, and the reason the study's *normative* conclusion -- that
entertainers carry a societal responsibility as epistemic infrastructure -- is **earned by
degrees, never asserted**. (Both are candidates to register via the thought-intake / governance
route; SOC-HUM-7 routes through the ethics perimeter, not `claims.yaml` alone.)

**Candidate SOC-HUM-6 (observational -- the probe-vs-safety-valve dissociation).** Not all
tension-humour does epistemic work. A long-standing rival theory -- the **safety-valve** function
-- holds that humour discharges tension *without* reframing, dissipating the pressure to engage and
thereby *preserving* the status quo ("putting it back on the shelf"). Three fates, all producing
laughter: **probe/unblock** (reframes, opens the node -- target-flip / self, benign-violation held);
**safety-valve/deflect** (releases the steam, closes the node); **entrench/weaponise** (out-group,
forecloses). SOC-HUM-6 sharpens H1: it is **probe-mode** humour specifically, not humour *volume*,
that leads resolution; safety-valve humour is null or negatively associated. Testable **now** in the
corpus being built, via the same coding scheme. *Null:* probe-mode and safety-valve humour relate
equally (or not at all) to resolution -- in which case the mechanism as stated is wrong.

**Candidate SOC-HUM-7 (interventional -- cultivating the fili).** In a small, high-connectivity
country with unresolved high-tension conflicts, deliberately training satirists/poets/comedians in
the **probe mode** -- recovering the institutional role the *fili* historically held in Gaelic
Ireland -- increases the rate/quality of societal epistemic engagement with those issues.
**Ethically bounded: the aim is PROCESS, not OUTCOME** -- restoring the capacity to *examine* a
too-charged issue (the societal analog of the therapeutic stance: make the unbearable thinkable
*without* dictating the conclusion), never pushing a verdict. Downstream of observational validation;
routes through the **ethics perimeter** (SENT-/GOV- governance rules). *Null:* trained-cohort output
shows no shift toward probe-mode, or the shift produces no downstream engagement effect.

**The dependency ladder -- the responsibility claim is calibrated to the evidence, never unconditional:**
- Flip only **lags** resolution -> entertainers are **barometers** (honest mirrors); "drivers" is false.
- Probe-mode makes issues safe to examine and the flip **leads** (H1-lead + SOC-HUM-6) -> **enablers**;
  "decision-helpers" is *earned*, because the mode chosen causally shapes whether exploration happens.
- That effect is large **and trainable** (SOC-HUM-7) -> **drivers**, and the full vanguard claim is licensed.

**Even the null results carry a (different) responsibility.** If the safety-valve theory wins
(SOC-HUM-6 null/reversed), the duty *inverts*: **not** to be the pressure-release valve that lets a
society feel it has engaged while avoiding. The only branch where responsibility fully collapses is
pure lagging narration -- and even there, "be an honest mirror" survives.

**Posture: research hypothesis, not program.** The normative claim is earned by degrees as each
hypothesis lands; it is not asserted and then acted on by recruiting practitioners. The spike-first,
blind-coding, lead-lag-quarantined discipline this thread has kept is exactly what would let the
eventual normative conclusion -- *if* earned -- stand up rather than read as advocacy. "Newspapers
may be dead but entertainment is not": if comedy is epistemic machinery and the print fourth-estate
is collapsing, comedy may be the *surviving* channel -- which raises the stakes of cultivating it
well, but only once the mechanism is shown to be real. The dependency ladder above is expressed
structurally in the seed repo's claims matrix as a **claim graph** (SOC-HUM-7 `depends_on`
SOC-HUM-1/2/6), so "earned by degrees" is a gated promotion, not a slogan.

---

This is a `/lit-pull` + design thread, not a `/queue-experiment` substrate run -- it does
not belong in `ree-v3/experiment_queue.json`.
