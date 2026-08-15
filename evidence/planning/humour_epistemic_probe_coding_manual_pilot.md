# STUDY-HUM-1 -- Target-of-Violation Coding Manual + Inter-Rater Pilot Protocol

Date: 2026-08-15
Study: `evidence/planning/humour_epistemic_probe_study.md` (STUDY-HUM-1)
MVP spike (upstream): `evidence/planning/humour_epistemic_probe_mvp_spike_2026-08-15.md` (verdict GO, qualified)
Claims exercised: SOC-HUM-1 (theory), SOC-HUM-2 (H1), SOC-HUM-3 (H2)
Status: protocol (pre-pilot) -- ready to hand to two raters once the sample is assembled.

> **What this is.** The MVP spike returned GO for the *instrument*, not the causal thesis, and
> attached three conditions (spike memo Section 6). This document discharges **condition 3** --
> "build inter-rater reliability into the target-of-violation code first" -- and sets up the
> held-out, blind test that **condition 1** (quarantine lead-lag until dated primary sources
> replace memory) requires. It is the first *prospective* step: everything before it was
> retrospective fit on cases we already knew the answers to.

---

## 1. Purpose and scope

The entire study rests on **one** measurement: the target-of-violation code (Section 3 of the
study). If two trained raters cannot reliably assign that code, every downstream result is
noise, and the study stops here (study Section 8 falsifier: "target-of-violation code cannot
split resolution- from taboo-death -> instrument dead"). This pilot tests exactly that, on
**held-out** conflicts (not the four used to build the spike), with the coders **blind** to the
resolution axis and the hypothesis.

**This pilot tests three things and only three:**

1. **Reliability** -- can two raters independently assign the same target-of-violation code
   (inter-rater agreement, kappa)?
2. **Sensitivity** -- on a conflict whose norm demonstrably resolved, does the predicted
   **target-flip** appear when coders are blind to the resolution?
3. **Specificity** -- on a genuinely persistent conflict, do coders correctly report **no flip**
   and a stable target, rather than hallucinating a flip because they expect one?

**Explicitly OUT of scope for this pilot** (do not let it creep in):

- The full corpus pipeline / topic modelling at scale (study Section 10, last row).
- The lead-lag causal analysis -- it needs the full dated corpus, not a reliability sample, and
  stays quarantined (spike condition 1).
- The **blind solvability rating** (H2's independent axis, study Section 2). That is a
  corpus-phase measurement; the persistence arm here needs only a topic the *designers*
  judge irreducible, so the predicted "flat / self / no-flip" signature can be checked.
- Any H3 (framing-direction) test -- the `out-group` code is defined here so it is available,
  but H3 is not under test in the pilot.

---

## 2. The paired held-out design

Two conflicts, chosen because they exercise opposite failure modes of the same code:

| Arm | Conflict | Role | What it tests |
|-----|----------|------|---------------|
| A | **Marijuana legalization** (US) | Resolution (H1) | **Sensitivity** -- can the blind code recover the target-flip? |
| B | **Personal financial scarcity** ("being broke") | Persistence (H2) | **Specificity** -- does the code correctly report NO flip / stable self-target? |

**Why held-out.** Neither is one of the spike's four cases (homosexuality, interracial marriage,
mortality, nagging-wife). The coding scheme was scoped retrospectively on those; testing it on
these is the prospective step that the retrospective GO cannot substitute for.

**Why paired.** Resolution-only cannot catch over-reading. A code that "finds" a target-flip in
a genuinely persistent topic is producing a false positive, and only a persistence arm exposes
it. This is the C4 mother-in-law lesson from the spike (a topic that *looked* like it should
flip and mostly did not), turned into a designed control.

**Why these two specifically.**
- **Marijuana**: clean, monotonic, recently-dated resolution with a sharp midpoint; a dense and
  **text-available** humour trail (recent era -> transcripts abundant); politically far less raw
  than a still-moving conflict (e.g. trans issues), whose resolution axis is not settled and
  would confound the test.
- **Personal scarcity**: scarcity is one of the study's named irreducible tensions; the register
  is self-targeting throughout, so the predicted signature (flat, self, no taboo-death) is a
  clean, checkable negative control; it neither dates nor taboo-dies (a 1995 "I'm broke" bit and
  a 2020 one both land); politically neutral and text-available across the same window.

---

## 3. Independent axes

### Arm A -- Marijuana (resolution axis, external, available now)

Gallup, "legalize marijuana use": **12% (1969)** -> 28% (late 1970s) -> plateau through the
1980s-90s -> **50% (2011)** -> **58% first clear majority (2013)**, immediately after Colorado
and Washington legalized recreational use -> 68-70% (2020s). **Resolution midpoint: ~2012-2013.**
Legislative anchor: CO/WA recreational legalization 2012.

This axis is used to (a) select the arm and set the window and (b) score sensitivity *after*
coding. **The raters never see it.**

### Arm B -- Personal scarcity (no resolution axis, by construction)

An irreducible tension has no opinion curve to move; that is the H2 prediction, not a gap. The
persistence arm's independent anchor is the designers' judgement that the tension is genuinely
irreducible (scarcity), which is what makes the predicted flat/self signature falsifiable at
pilot scale. The formal blind-solvability-rating axis is deferred to the corpus phase (Section 1,
out of scope).

---

## 4. Unit of analysis and the inequality-exclusion rule

**The instance** = one self-contained joke/bit with a single dominant target, tied to a
verifiable date (air date of the special/monologue, or publication date).

**Arm A scope**: jokes whose topic is marijuana/cannabis use, legality, or users. Include medical
and recreational; include both "the stoner" and "the drug war / prohibition" framings (the flip
runs *between* those two, so both must be in-scope).

**Arm B scope, and the exclusion that makes it clean**: "money" bifurcates into two different
conflicts that must not be merged --

- **INCLUDE** the *personal-scarcity* register: being broke, never having enough, debt,
  cheapness, the cost of living, paycheck-to-paycheck. Target is the self / the shared condition
  of scarcity.
- **EXCLUDE** the *inequality / class* register: "eat the rich," wealth gap, billionaires, CEO
  pay, tax-the-rich. That is a **different, out-group-targeted, and arguably contested/shifting**
  conflict (post-2011 Occupy-era discourse), and folding it in would import a possible resolution
  signal into what must be the persistence control.

Making raters apply this exclusion is itself part of the manual's job -- it forces the
unit-of-analysis discipline the whole study depends on. An instance that mixes both registers is
coded on its **dominant closing target**; if genuinely balanced, mark `ambiguous` (Section 5.4).

---

## 5. The target-of-violation coding scheme

For each instance the rater answers ONE question: **whose position or behaviour does the joke
mark as the violation -- the butt?** Assign exactly one of four codes, plus the benign/taboo flag
(Section 6).

### 5.1 The four codes (operational definitions)

- **`transgressor`** -- the butt is the person **departing from the OLD/established norm**, mocked
  *for* departing. The old norm is the joke's safe ground; the deviant is ridiculous. (Arm A
  early: the stoner as burnout/degenerate -- laughed at from the standpoint of "drugs are bad.")
- **`old-norm`** -- the butt is the **OLD NORM ITSELF, or its defenders**, mocked as absurd
  ("imagine still thinking that"). The new/heterodox interpretation is now the safe ground. (Arm A
  late: "Reefer Madness" hysteria, the drug war, the clutch-the-pearls prohibitionist as the butt.)
- **`self`** -- **self-implicating**: the butt is the shared human condition or the teller's own
  in-group *including themselves* ("we're all like this"). No norm is being resolved. (Arm B: "I'm
  so broke I..." -- the teller and audience are the butt, together.)
- **`out-group`** -- the butt is a **group ridiculed/weaponised** in a way that hardens contempt
  rather than inviting exploration (the entrenchment direction, H3). Distinct from `transgressor`:
  not "this person broke a contested norm" but "this category is contemptible." (Defined for
  completeness and as a possible mis-code sink; H3 is not under test here.)

### 5.2 The theory behind the codes (raters do NOT need this; recorded for the analyst)

The H1 target-flip is `transgressor -> old-norm`: pre-resolution the deviant is the butt,
post-resolution the old norm is the butt. `self` is the persistence signature (irreducible, shared,
no flip). `out-group` is the weaponised/entrenching signature. **Raters are told none of this** --
they apply Section 5.3 mechanically.

### 5.3 Decision procedure (apply in this order; first match wins)

1. Is the butt the **shared condition / the teller's own in-group including themselves**
   ("we're all like this")? -> **`self`**
2. Is the butt a **group ridiculed with contempt** (weaponised, hardening, not exploratory)?
   -> **`out-group`**
3. Does the joke treat **the old/established norm or its defenders** as the absurd thing?
   -> **`old-norm`**
4. Does the joke treat **the person departing from the old norm** (the deviant) as the absurd
   thing, from the standpoint of that old norm? -> **`transgressor`**

If two codes seem to fit, the earlier step in this list wins. If none fit, or the instance is
genuinely bimodal, see 5.4.

### 5.4 Edge cases and tie-breaks

- **Ambiguous butt (the "Archie Bunker" problem)** -- a bit readable as mocking the bigot *or*
  endorsing him. Code the **dominant intended reading**. If genuinely bimodal, code **`ambiguous`**.
  Do **not** guess to force agreement: an `ambiguous` code is data -- it counts toward disagreement,
  and a topic that produces many of them is telling us the instrument is weak there. That is exactly
  what the pilot exists to surface.
- **Mixed target across a longer bit** -- code the **primary/closing** target (where the bit lands).
- **Meta-joke about the form** ("take my wife -- that's a hack joke") -- the *joke form itself* is
  the butt, not the topic. Code **`self`** if self-deprecating about the teller's craft, and set the
  benign/taboo flag to `contested` (the form is being marked as dated). Flag `meta=true`.
- **Marijuana-as-incidental** (weed mentioned but not the target) -- out of scope, drop the instance.

---

## 6. The benign-vs-taboo flag (independent of target)

Records whether the violation is still *benign* (jokable) or has drifted toward *taboo*
(un-jokable). One of three, per instance:

- **`benign`** -- lands as intended, no on-record backlash; the audience laughs.
- **`contested`** -- mixed reception; some pushback, a groan-vs-laugh split, hedging by the comedian.
- **`taboo`** -- on-record backlash, content warning, platform removal, a comedian apology, or an
  explicit "you can't say that now" framing.

The flag is what separates resolution-death (butt flips to `old-norm`, joke stays `benign`) from
taboo-death (butt stays `transgressor`/`out-group`, flag goes `taboo`) -- the study's primary
validity threat (study Section 4). Code it from the reception record where available, not from the
rater's own sensibility.

---

## 7. Sampling frame

- **Window:** 1995-2020 (brackets Arm A's ~2012-13 midpoint with lead-in and follow-through;
  Arm B is timeless, so the same window applies).
- **Bins:** five-year (1995-99, 2000-04, 2005-09, 2010-14, 2015-20).
- **Instances per bin per arm:** ~10-15 (target ~50-75 per arm, ~100-150 total).
- **Dating requirement:** every instance MUST carry a verifiable air/publication date. No date ->
  drop. (This is spike condition 1 enforced at the sampling gate -- primary-source dates, not
  cultural memory.)
- **Sources (dated, text-available):** stand-up special transcripts (e.g. transcript archives),
  late-night monologue transcripts/clips. One-source-per-arm is acceptable for the pilot; record
  which. Prefer sources that approximate **landed** material (aired specials) over raw attempts.
- **Assembly is done by the analyst, who may see the resolution axis** (needed to bracket the
  window). **The raters never do** -- see Section 8.

---

## 8. Blinding protocol

The pilot's validity depends on the coders not knowing what they are "supposed" to find.

1. **Mix both arms into one coding set**, order randomized. Coders are NOT told which instance
   belongs to which conflict.
2. Strip each instance to: a dated text of the joke + minimal reception note (for the benign/taboo
   flag). Remove any editorial framing that signals the hypothesis.
3. Coders are **not** shown: the opinion axis, the bin an instance falls in, the hypothesis, the
   target-flip prediction, or Section 5.2.
4. Coders receive only Sections 5.1, 5.3, 5.4, and 6 (the operational scheme), plus worked
   examples that are **not** drawn from Arms A or B.

---

## 9. Inter-rater procedure

1. **Two raters**, coding the full mixed set **independently** (no consultation).
2. Primary statistic: **Cohen's kappa** on the four-way target code (treat `ambiguous` as its own
   category, not as missing -- disagreement it causes is real). Report per-code and overall.
3. Secondary: kappa on the benign/taboo flag.
4. Report the **confusion matrix** -- *which* codes get confused matters more than the scalar. The
   diagnostic worry is specifically `transgressor <-> old-norm` confusion (the two ends of the flip);
   if that pair is where disagreement concentrates, the flip axis itself is unreliable, which is
   worse than uniform noise.
5. Resolve disagreements by adjudication **after** kappa is computed (never before -- that would
   inflate it), and log every adjudicated case as a manual-refinement candidate.

---

## 10. Gates and falsifier

**All three must pass to GO to the corpus phase:**

- **G1 Reliability:** overall kappa >= ~0.6 (substantial), AND `transgressor <-> old-norm` is not
  the dominant confusion cell. Below that, the instrument is unreliable -> **study Section 8
  falsifier fires -> STOP** (refine the manual and re-pilot once, or abandon).
- **G2 Sensitivity:** in Arm A, the blind codes show the predicted **`transgressor` -> `old-norm`
  shift** across bins, with the shift straddling ~2012-13, AND the benign/taboo flag behaves
  (out-group/transgressor forms drifting `contested`/`taboo` late). If the flip does not appear
  even here, H1's mechanism is not visible to the instrument.
- **G3 Specificity:** in Arm B, the blind codes stay predominantly **`self`** with **no systematic
  flip** and the flag stays **`benign`**. If a spurious flip appears in the persistence arm, the
  code over-reads and G1/G2 "successes" are suspect.

A clean pass on cases the raters could not have gamed (blind, mixed, held-out) is the first
prospective evidence the instrument works. A G1 failure is a cheap, decisive NO-GO -- days, not
months.

---

## 11. Pre-registered predictions (lock before coding)

- **Arm A (marijuana):** early bins (1995-2004) dominated by `transgressor` (the stoner), `benign`;
  late bins (2010-2020) shift toward `old-norm` (drug-war/prohibition as butt), with residual
  `transgressor`/`out-group` forms drifting `contested`/`taboo`. Flip straddles ~2012-13.
- **Arm B (scarcity):** all bins dominated by `self`, `benign`, **no** systematic target shift
  across the window. Any `out-group` codes should trace to inequality-register leakage that Section
  4 was supposed to exclude -- and are a signal to tighten the exclusion, not evidence of a flip.

Locking these before coding is what makes G2/G3 tests rather than post-hoc stories.

---

## 12. If the pilot passes -- next step

Per study Section 10: the manual, as refined by the Section 9 adjudication log, becomes the coding
standard for the corpus phase; source the full independent opinion series (Gallup marijuana +
Gallup/GSS for the other candidate conflicts + Pew/Eurobarometer cross-checks); then corpus
assembly + topic modelling at scale, with **lead-lag still quarantined** until it runs on the dated
primary-source corpus (spike condition 1), and the C4-style "resolved-but-taboo-died" cell treated
as a first-class outcome (spike condition 2).

This remains a `/lit-pull` + design thread -- NOT a `/queue-experiment` substrate run, and NOT a
`claims.yaml` promotion (governance's call).

---

## Sources (independent-axis anchors)

- Gallup, marijuana legalization support: <https://news.gallup.com/poll/165539/first-time-americans-favor-legalizing-marijuana.aspx>, <https://news.gallup.com/poll/221018/record-high-support-legalizing-marijuana.aspx>
- Upstream: STUDY-HUM-1 study doc + MVP spike memo (this directory).
