# Affect-stream differentiation: RELIEF vs SAFETY vs SOOTHING -- Lit-Pull Verdict

**Date:** 2026-06-05
**Question (a):** Are relief, safety, and soothing mechanistically dissociable (distinct circuits, valence-timing, computational role)?
**Question (b):** For SAFETY and SOOTHING each, should REE register a distinct affect-primitive stream, fold into the existing Relief row, or defer -- and at what V3/V4 scope?
**Feeds:** `docs/architecture/affect_primitives.md` "Extension Register: Beyond Harm" decision.
**Failure mode guarded:** SD-011 / SD-003 "philosophy-right, mechanism-wrong" -- collapsing distinct biological systems into one REE primitive (`feedback_biology_before_formal_definitions`).
**Relationship to prior work:** This pull EXTENDS, and does not duplicate, the 2026-05-03 `targeted_review_relief_completion_mechanism` verdict (which first split relief-completion from safety-cue prediction and seeded MECH-302/303/304). It adds (i) newer, stronger anchors for each pole, and (ii) the entirely new SOOTHING/COMFORT dimension that the prior pull did not cover.

---

## Headline

**(a) YES -- all three are strongly dissociable.** They differ on every axis: distinct circuits, distinct valence-timing (offset-phasic / prospective-tonic / present-regulatory), and distinct computational roles (reinforcement teaching signal / learned inhibitory predictor / autonomic state-gain modulator). None is identical to "Relief". Confidence **0.82**.

**(b1) SAFETY -> register-as-distinct-stream. ALREADY DONE in claims.yaml (MECH-303 + MECH-304); this pull CONFIRMS it is biology-correct.** The remaining action is a *documentation* fix: the `affect_primitives.md` Extension Register still lists only a single V4-deferred "Relief" row and does not reflect that safety is a separately-registered, V3-phase, two-system cluster distinct from relief. Recommend updating the register to add SAFETY rows pointing at MECH-303/304 (doc-sync, not a new claim). Scope: **V3** (already `implementation_phase: v3`; off the current critical path, do not add to it now).

**(b2) SOOTHING/COMFORT -> register-as-distinct-category, but DEFER substrate to V4-social.** This is the genuine unregistered gap. It must NOT be folded into Relief (MECH-302) or Safety (MECH-303/304) -- different circuit, time-reference, and computational role. Recommend adding a distinct SOOTHING row to the Extension Register scoped **V4-social (primary)** with an optional **V3-minimal non-social autonomic-recovery hook** noted but not built. No claim registered in this session (per task scope).

---

## The three-way differentiation table

| Axis | RELIEF | SAFETY | SOOTHING / COMFORT |
|---|---|---|---|
| **Definition** | Appetitive signal at the **offset** of an aversive event; a positive reinforcer | A **learned prospective predictor** that threat is **absent** (active inhibitory learning / conditioned inhibition), NOT mere low harm | **Down-regulation of the ongoing stress response**, often via a conspecific (social buffering) |
| **Time reference** | Past (event-locked to aversive termination) | Future (prediction over a horizon) | Present (modulates the active trajectory) |
| **Valence-timing** | Phasic, retrospective-at-offset, **appetitive** | Tonic/contextual, prospective, **permissive/inhibitory** (suppresses fear; "absence of negative") | State-modulatory, present-tense, **calming** (reduces arousal/drive) |
| **Core circuit** | NAc / VTA, value-coding dopamine; **D1 + NMDA coincidence** | Prefrontal-hippocampal-thalamic: mPFC IL/PL, vHipp-PL, **nucleus reuniens -> BLA**; IL-CeA output | Oxytocinergic + parasympathetic/HPA + prefrontal regulation |
| **Computational role** | **Reinforcement teaching signal** (tags "this reduced suffering") | **Learned predictor / gate** (licenses commitment-release + approach) | **State-gain / recovery modulator** (reduces magnitude + persistence of the active stress state) |
| **Lit anchors (this pull)** | Bergado Acosta 2017 | Corches 2019 (contextual/PL-IL), Silva 2021 (reuniens->BLA active transmission) | Hostinar 2014 (review), Heinrichs 2003 (human oxytocin x support) |
| **Lit anchors (prior pull)** | Andreatta 2012, Navratilova 2012, Brombergmartin 2010 | Kreutzmann 2020, Meyer 2019 | -- (not covered) |
| **REE mapping** | **MECH-302** (reuses reward/goal pipeline; reads SD-011 suffering derivative) | **MECH-303** (contextual passive) + **MECH-304** (cue-specific conditioned inhibition) | **PROPOSED, unregistered**: state-gain modulator on MECH-219 (suffering accumulator) decay + SD-012 / SD-032e drive-autonomic layer |
| **Registry status** | Registered candidate (v3) | Registered candidates (v3) | **Not registered** |
| **Scope** | V3 | V3 | **V4-social** (+ optional V3-minimal autonomic-recovery hook) |

---

## Evidence by pole

### RELIEF (the existing Relief row; MECH-302)

- **[Bergado Acosta et al. 2017](https://doi.org/10.1016/j.neuropharm.2016.11.022)** (Neuropharmacology 114:58-66, PMID 27894877): relief-learning *acquisition* requires coincident dopamine D1 + NMDA activation in the nucleus accumbens -- the same value-coding reward coincidence that mediates reward learning. Pins relief to reward substrate at the receptor level. **supports MECH-302**, conf 0.82.
- Converges with prior-pull anchors: Andreatta 2012 (ventral-striatum/amygdala double dissociation), Navratilova 2012 (VTA-DA / NAc-DA at pain offset).
- **Verdict for relief:** the existing Relief row + MECH-302 are well-grounded. Relief is an **event-locked, phasic, value-coding reinforcement** signal. This is the reference pole; safety and soothing are NOT this.

### SAFETY (MECH-303 contextual passive + MECH-304 cue-specific; already registered)

- **[Corches et al. 2019](https://doi.org/10.1016/j.bbr.2018.11.042)** (Behav Brain Res 360:169-184, PMID 30502356): prelimbic mPFC codes context-danger; differential conditioning recruits additional PL+IL ensembles for inhibition of generalized fear. Safety is an *active prefrontal representation*, not low-harm. **supports MECH-303**, conf 0.74.
- **[Silva et al. 2021](https://doi.org/10.1038/s41593-021-00856-y)** (Nat Neurosci 24(7):964-974, PMID 34017129): nucleus reuniens -> BLA registers and *transmits* safety signals that causally drive remote fear extinction (rises before freezing cessation; inhibition impairs, activation facilitates). Causal, bidirectional anchor for *active* safety transmission. **supports MECH-304**, conf 0.80.
- Converges with prior-pull anchors: Kreutzmann 2020 (IL required for safety *expression*), Meyer 2019 (vHipp-PL conditioned inhibition).
- **Verdict for safety:** dissociable from relief on circuit (prefrontal-hippocampal-thalamic vs NAc/VTA), valence-timing (prospective-tonic vs offset-phasic), and computational role (predictor/gate vs reinforcement). The relief-vs-safety split is biology-correct and ALREADY in the registry (MECH-302 vs MECH-303/304). **register-as-distinct = already satisfied.**
- **Anatomical flag (enrichment, not contradiction):** Silva implicates a midline-**thalamic** relay (reuniens) and a **time-since-encoding** dependence (remote > recent) absent from MECH-303/304's stated cortico-striatal / IL-CeA / vHipp-PL anatomy. A future revision of MECH-303/304 should consider adding the thalamic node.

### SOOTHING / COMFORT (proposed, unregistered)

- **[Hostinar, Sullivan & Gunnar 2014](https://doi.org/10.1037/a0032671)** (Psychol Bull 140(1):256-282, PMID 23607429): social buffering = dampened HPA-axis stress response in the presence/assistance of a conspecific; mediated by oxytocinergic systems + prefrontal networks; shaped by early attachment. **supports the differentiation** (no registered claim), conf 0.78.
- **[Heinrichs et al. 2003](https://doi.org/10.1016/S0006-3223(03)00465-7)** (Biol Psychiatry 54(12):1389-1398, PMID 14675803): oxytocin x social support suppress cortisol and subjective anxiety to acute psychosocial stress; strongest at the interaction. Causal human anchor for socially-gated, oxytocin-mediated down-regulation of the *ongoing* stress state. **supports the differentiation** (no registered claim), conf 0.76.
- **Verdict for soothing:** dissociable from BOTH. It acts on the *present* stress trajectory (vs relief's past-offset, safety's future-prediction); its substrate is oxytocin/parasympathetic/HPA (vs NAc/VTA, vs cortico-amygdalar); its computational role is a state-gain/recovery modulator (vs reinforcer, vs predictor). It is socially gated -- the canonical trigger is a conspecific, which REE V3 cannot represent. **register-as-distinct-category, V4-social scope; do not fold into Relief or Safety.**

---

## Mapping to existing REE substrate (required)

- **SD-011 (dual nociceptive harm streams):** the *input* substrate. All three affect computations *read/modulate* the harm streams; none *is* a harm stream. Relief = derivative/offset of the suffering stream; Safety = prediction that the harm stream stays low; Soothing = down-regulation of the ongoing suffering/drive state. The same read-not-be discipline SD-011 already enforces for relief applies to safety and soothing.
- **MECH-112 (structured latent goal representation; the appetitive/"wanting" axis):** relief shares the reward *machinery* (NAc/VTA) but with opposite-polarity input (aversive offset, MECH-302). Safety is NOT wanting (it is inhibitory prediction). Soothing is NOT liking (it is autonomic state down-regulation). **Do not conflate safety or soothing with MECH-112** -- that would be a second instance of the philosophy-right/mechanism-wrong failure.
- **Existing Relief row (affect_primitives.md, V4-deferred):** under-specified relative to the registry. The MECH-302/303/304 cluster already splits relief from safety; the Extension Register table has not caught up. Recommended doc-sync: replace the single "Relief" row with (i) a Relief row -> MECH-302, (ii) a Safety row -> MECH-303/304, (iii) a new Soothing/Comfort row -> proposed/unregistered, V4-social.
- **Soothing's proposed home:** MECH-219 (suffering accumulator) decay/gain + SD-012 (homeostatic drive) + SD-032e (pACC autonomic coupling). A soothing input would *lower the gain / speed the recovery* of the active aversive trajectory -- mechanistically a modulator on these, not a new harm/reward channel.

---

## Recommendations (for the affect_primitives.md Extension Register decision; NOT executed this session)

1. **SAFETY -- doc-sync only (no new claim).** Update the Extension Register to add SAFETY rows pointing at the already-registered MECH-303 (contextual passive) and MECH-304 (cue-specific conditioned inhibition), and stop implying relief is the only beyond-harm row. Optionally flag the Silva-2021 thalamic-relay + remote-vs-recent enrichment on MECH-303/304. Scope V3; off the current critical path.
2. **SOOTHING -- add a distinct Extension Register row; register a candidate claim later.** Scope V4-social (primary). Note an optional V3-minimal non-social autonomic-recovery hook (parasympathetic down-regulation of ongoing arousal acting on MECH-219 decay / SD-012 drive) but do NOT build it on the V3 critical path. When registered, it must depend on MECH-219 + SD-012 + SD-032e and be explicitly NOT-MECH-302/303/304 and NOT-MECH-112.
3. **RELIEF -- no change beyond the row-split in (1).** MECH-302 is well-grounded.
4. **Cross-link** this verdict to the proto-feelings audit register (`thought_intake_2026-06-01_protofeelings_audit_register.md`), which flagged "safety/soothing as a positive safe-enough state" as a P0 gap -- this pull resolves it into two distinct items (safety = already registered; soothing = V4-social gap).

## What this pull does NOT settle

- The exact REE *update rule* for soothing (gain reduction vs decay acceleration vs setpoint shift on MECH-219/SD-012) -- needs a design pass, not more lit.
- Whether MECH-303 (passive contextual) and MECH-304 (cue-specific) should absorb the reuniens thalamic relay or whether it warrants a third safety sub-mechanism.
- Whether a non-social V3 self-soothing core is worth building at all, or whether soothing is purely V4-social. (Recommend deferring this decision until V4-social scoping.)

## Confidence components

- **Cross-species + cross-method convergence:** high. Relief (rat pharmacology + rodent/human imaging from prior pull); safety (mouse ensembles + causal optogenetics + cited human imaging); soothing (rodent + human, review + controlled experiment).
- **Dissociation strength:** high. Three anatomically separate systems with three distinct time-references and computational roles; double dissociations available for relief-vs-fear and safety-vs-threat.
- **REE-mapping fidelity:** high for relief + safety (registered claims with matching substrate); moderate-low for soothing (no V3 other-model, no HPA axis -- V4-bound, analogical mapping).
- **Net:** 0.82 in the differentiation verdict; the safety conclusion (already-registered, biology-correct) is the most secure, the soothing conclusion (distinct system, V4-social) is well-supported but its REE implementation is the least settled.
