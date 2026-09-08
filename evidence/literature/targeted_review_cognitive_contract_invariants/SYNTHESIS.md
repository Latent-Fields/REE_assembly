# Targeted lit-pull synthesis: the five MECH-545 contract-invariant candidates across GOV-CONTRACT-1's five external domains

**Pulled** 2026-09-08 (13 entries in `entries/`, 60+ verified sources cited below).
**Target claims** ARC-142 (the cognitive contract), MECH-545 (contract-lesion assays), MECH-546 (grammar inherits the contract; typology and emergent-communication cells only). GOV-CONTRACT-1 is the RULE this pull is run under, not a claim it evidences.
**Chip** `chip-20260908-cognitive-contract-litpull`; session `peaceful-kare-a6a78f`.
**Source thought** `docs/thoughts/2026-09-08_deriving_the_cognitive_contract.md` sections 7-9; intake `evidence/planning/thought_intake_2026-09-08_deriving_the_cognitive_contract.md` section 8 item 1.
**Companion pull** `targeted_review_inv_104/` (INV-104 is the first instantiated contract; Pezzulo et al. 2026 there is the developmental source cited in GOV-CONTRACT-1's held-out record).

## Read this first: what this document is and is not

1. **Literature resembling REE is motivation, never support.** Per `feedback_lit_exp_decoupled`, nothing here raises any claim's confidence or status. ARC-142, MECH-545 and MECH-546 remain `candidate`; GOV-CONTRACT-1 remains warn-only. Experimental evidence is load-bearing; this is the map of where the external literature stands so that the REE-internal test (domain 6) can be designed against it.
2. **Domain 6 (REE-internal necessity) is deliberately NOT assessed.** That is experiment evidence, owned by MECH-545's assays, not by a literature pull.
3. **The twelve-field ledger (`evidence/planning/cognitive_contract_invariant_ledger.v1.json`) is not built** and its chip (`chip-20260908-cognitive-contract-ledger`) had not landed at pull time (not present in `TASK_CHIPS.json`, no ledger file). Section 4 below gives one ledger-shaped block per candidate, field names matching GOV-CONTRACT-1's record shape, so they can be pasted into the ledger's records when it exists. The `ree` and `lesion_prediction` fields are left as pointers, not filled.
4. **Verdict grading.** Every one of the 25 cells returned a nominal "supports" from its domain search. That is not informative on its own, so each cell is graded here against the DOMAIN's own admissibility criterion in GOV-CONTRACT-1:
   - **S** -- supports, criterion met (typology: recurrent AND obligatorily encoded OR preserved when its carrier is absent; developmental: present pre-linguistically; neuroscience: modality/subsystem-independent representation OR a known retaining translation mechanism; comparative: present in a lineage with a substantially different ecology; artificial agents: discovered WITHOUT being specified).
   - **s** -- weak or partial support, criterion only half met (typology: areal/cultural-leaning or category-internally incoherent; comparative: close-relative proxy only; artificial agents: ablation of a hand-installed bias with no emergence).
   - **A** -- absent; **C** -- contradicts. (No cell landed in A or C outright; the C-flavoured findings are inside cells and listed in section 3.)
   - **Quorum** counts **S only**. The count including **s** is shown in parentheses. A candidate at >= 2 S is "quorum-eligible pending REE-internal test"; 0-1 S is "held uncertain".
5. **Cross-linguistic universality alone is inadmissible** (GOV-CONTRACT-1). The typology column never contributes standing on its own; it is admitted as an inverse probe and counts as at most one domain in a quorum.

---

## 1. The 5 x 5 verdict matrix

| candidate | 1 typology | 2 developmental | 3 neuroscience | 4 comparative | 5 artificial agents | quorum (S) | status |
|---|---|---|---|---|---|---|---|
| IDENTITY | S | S | S | S | s | **4** (5) | quorum-eligible pending REE-internal test |
| TEMPORAL RELATION | S | S | S | S | S | **5** (5) | quorum-eligible pending REE-internal test |
| REALITY STATUS | s | S | S | s | s | **2** (5) | quorum-eligible pending REE-internal test -- at the threshold; see section 3 |
| AGENCY / CONTROLLABILITY | S | S | S | S | S | **5** (5) | quorum-eligible pending REE-internal test |
| CONFIDENCE / PRECISION | s | S | S | S | s | **3** (5) | quorum-eligible pending REE-internal test -- as a FLAG; the WEIGHT reading is held uncertain |

**No candidate is held uncertain at the whole-candidate level.** Two are held uncertain at the sub-relation level: REALITY STATUS as a single four-way provenance relation (the domains support only a coarse actual / not-actual marker and split the rest), and CONFIDENCE as precision-weighting (only decision confidence as a flag is developmentally early). Both splits are the pull's most useful output for MECH-545, because a lesion assay that does not name which sub-relation it deletes is uninterpretable.

**Standing caution on the matrix shape.** Twenty-five supports is what one would also get from a search that finds what it looks for. Three things argue that it is not only that: every cell carries a verified dissent (section 3); the grading demotes five cells to partial; and the two candidates the source thought itself flagged as most likely composite (reality status, confidence) are the two the literature splits. The pull was conducted by five independent agents, one per domain, each instructed to record negative findings as first-class; none had access to the others' results.

---

## 2. Per-cell evidence (1-3 verified sources per cell; full citations in section 6)

Each line: verdict grade -- key result -- **classification reading** (ARCH = supports the architectural reading; EMB = embodied / ecological alternative live; CULT = human-linguistic / cultural alternative live).

### IDENTITY (same entity across a boundary; persistence of an individual)
- **Typology S.** Same-entity information is grammaticalised by at least three structurally unlike devices reinvented in unrelated stocks: definite articles (Dryer, WALS 37: 422/620 languages mark definiteness, 198 do not), switch-reference (Roberts 2017: 40+ Papuan families plus independent American families, a dedicated slot whose only content is "same subject or not"), obviation, and 3rd-person anaphors grammaticalised from demonstratives (Heine & Kuteva 2002). **ARCH-leaning: something must carry the relation; CULT live: discourse-disambiguation explains switch-reference equally well; no single device is universal.**
- **Developmental S.** Numerical identity across occlusion computed at 10-12 months from spatiotemporal information before kind information (Xu & Carey 1996); feature channels enter the identity decision at different ages (Wilcox 1999); 14-month-olds infer identity from non-visible causal properties (Cacchione et al. 2013). **ARCH: a separable computation with its own timetable; EMB for the FORMAT: the earliest inputs are body-in-space.**
- **Neuroscience S.** Human MTL neurons fire for the same individual across picture, spoken name and written name; invariance rises along the MTL hierarchy (Quian Quiroga et al. 2009; review Quian Quiroga 2012). **ARCH for the format (modality-invariant); CULT for the content (cell tuning is acquired).**
- **Comparative S.** Cross-modal individual recognition in horses (Proops et al. 2009); mirror self-recognition in magpies (Prior et al. 2008) and, contested, cleaner wrasse (Kohda et al. 2019; dissent Vonk 2020). **ARCH: mammal, bird, teleost; EMB live: all are social species for whom conspecific identity is an ecological problem.**
- **Artificial agents s.** PLATO fails intuitive-physics VoE without an object-level carrier (Piloto et al. 2022); Loci-Looped acquires object permanence from observation alone (Traub et al. 2023); slot attention (Locatello et al. 2020). **Ablation met; emergence only partly met (object structure is supplied in PLATO and slot attention). ARCH-leaning with the task-structure alternative live.**

### TEMPORAL RELATION (before / after / now; present vs anticipated; causal order)
- **Typology S.** Grammatical tense is absent in ~40% of 222 languages and clusters areally (Dahl & Velupillai, WALS 66) -- tense itself is CULT -- yet a tenseless language still obligatorily recovers temporal reference from aspect, adverbials and discourse (Tonhauser 2011), and TAM grams are repeatedly reinvented from lexical sources across 25 phyla (Bybee, Perkins & Pagliuca 1994). **ARCH: the relation survives deletion of its dedicated carrier (a preservation-under-lesion result, the only one of its kind in this domain); also a translatable-around observation for MECH-545.**
- **Developmental S.** Newborns hours old prefer causal launching order (Mascalzoni et al. 2013). Arbitrary order becomes reliable only ~28 months with verbal help (Bauer et al. 1998); at 9 months order is bound to the specific materials (Lukowski et al. 2009). **ARCH for causal order; CULT for arbitrary order-as-content.**
- **Neuroscience S.** Hippocampal time cells tile empty delays and retime (MacDonald et al. 2011); lateral entorhinal population state encodes elapsed time seconds-to-hours, absent in MEC and CA1-CA3 (Tsao et al. 2018). Dissent: rate after-effects do not transfer across vision, audition, touch (Motala et al. 2018). **ARCH at the episodic level; EMB / modality-specific at the sensory-timing level.**
- **Comparative S.** What-where-when in scrub jays (Clayton & Dickinson 1998), future planning without current motivation (Raby et al. 2007), and what-where-when preserved with age in cuttlefish, an animal with no hippocampus (Schnell et al. 2021). Dissent: Suddendorf & Corballis 2007 (trace-strength could do it without a represented relation). **ARCH: corvid and cephalopod; translatable-around argument live.**
- **Artificial agents S.** Elapsed time emerges unspecified as trajectory position in RNNs and stays decodable when multiplexed with non-temporal content (Bi & Zhou 2020). Temporal reference in emergent communication does NOT arise from loss/task pressure and needs an architectural change (Lipinski et al. 2023). **ARCH: emergence met; the Lipinski result argues against the CULT reading specifically.**

### REALITY STATUS (observed / remembered / imagined / counterfactual)
- **Typology s.** Evidentiality grammaticalised in 237/418 languages but almost absent from Africa and, per de Haan (WALS 77/78), "more of an areal feature than a genetic feature"; "irrealis" is not a coherent single category (Bybee 1998) and its rehabilitation splits it into possible vs counterfactual (von Prince, Krajinovic & Krifka 2022). **CULT-leaning; the relation looks like a FAMILY, not one invariant.**
- **Developmental S.** 15-month-olds track pretend-episode consistency without confusing it with the real cups (Onishi, Baillargeon & Leslie 2007). Reliable fantasy/reality assignment is protracted and knowledge-dependent (Woolley & Ghossainy 2013) and degrades under emotion (Carrick & Quas 2006). **ARCH for a coarse actual / not-actual marker; the four-way distinction is late.**
- **Neuroscience S.** Paracingulate sulcus morphology predicts hallucination in schizophrenia REGARDLESS of sensory modality (Garrison et al. 2015; review Simons, Garrison & Johnson 2017). Dissent: reality judgements are a threshold on a graded signal that perception and imagery SHARE; vivid imagery is judged real (Dijkstra & Fleming 2023). **ARCH: a subsystem-independent DECISION; but the mechanism is reconstruction from a shared signal, not a protected tag.**
- **Comparative s.** Source-of-encounter memory in rats, abolished by CA3 inactivation (Crystal et al. 2013; review Crystal 2016; dissociation Smith et al. 2017). Searches for imagined-vs-perceived discrimination or DRM-analogue false memory in any non-human species returned zero records. **Provenance is separably lesionable in a close relative; the observed-vs-imagined contrast the candidate names is effectively ABSENT in this domain.**
- **Artificial agents s.** Untagged model-generated transitions collapse model-based RL; separating real and imagined buffers and bounding imagination depth is the fix (Janner et al. 2019 MBPO; Buckman et al. 2018 STEVE). No case found of an agent inventing an observed / imagined marker unprompted. **Ablation met, emergence not met.**

### AGENCY / CONTROLLABILITY (self-caused vs external; actor; controllability)
- **Typology S.** Morphological causative in 287/310 languages (Song, WALS 111); semantic (agent / patient) alignment emerges and decays independently in unrelated stocks (Donohue & Wichmann 2008). Over half of 190 languages give core arguments no case distinction (Comrie, WALS 98) -- the relation is always recoverable, the vehicle highly variable. **ARCH-leaning; EMB live: near-universality is what a shared action problem predicts too.**
- **Developmental S.** 12-month-olds attribute goal-directed agency to a 2-D circle with no body from efficient action-to-goal structure (Gergely et al. 1995); actor identity travels with the goal at 13 months (Buresh & Woodward 2007); bidirectional action-effect binding by 9 months (Verschoor et al. 2010); self / other discrimination of contingent specular images at 4 months (Rochat & Striano 2002). **ARCH: body-independent attribution is the decisive datum.**
- **Neuroscience S.** Corollary discharge is a distinction-retaining translation mechanism recurring across phyla (Crapse & Sommer 2008); cerebellar forward-model cancellation of self-produced sensation (Blakemore, Wolpert & Frith 1998); controllability as a separately localised mPFC signal (Maier & Seligman 2016; Amat et al. 2005). Dissent: the agency signal is effector-specific and can enhance rather than suppress (Reznik et al. 2014). **ARCH for the relation; EMB for the implementation.**
- **Comparative S.** A single identified corollary-discharge interneuron in the singing cricket (Poulet & Hedwig 2006); learned negative image of self-generated electrosensory reafference in mormyrid fish (Bell et al. 1997, 1993); deliberate self-agency discrimination in chimpanzees (Kaneko & Tomonaga 2011). **ARCH: insect, fish, primate, three unrelated modalities -- the least embodiment-confounded cell in the pull.**
- **Artificial agents S.** The controllable part of the observation is discovered by predicting one's own action, and lacking it collapses sparse-reward exploration (Choi et al. 2019) -- the only cell in this domain where BOTH admissibility tests are met; controllability as the organising variable for representation learning (Thomas et al. 2017). **ARCH; EMB live: "controllable" is defined relative to an action set.**

### CONFIDENCE / PRECISION (reliability travelling with content)
- **Typology s.** An epistemic meaning domain is cross-linguistically coherent but comprises two subdomains, certainty and information source, that cluster into fused systems (Boye 2012); mirativity as a grammaticalised prediction-error marker (DeLancey 1997) is contested as a category (Aikhenvald 2012). **Certainty is usually FUSED with evidentiality; CULT live: hedging to a hearer is an audience-design pressure with no analogue inside one mind.**
- **Developmental S.** Non-verbal metacognitive sensitivity with an adult-homologous ERN at 12-18 months (Goupil & Kouider 2016); selective help-seeking at 20 months (Goupil, Romand-Monnier & Kouider 2016). Dissent: reliability-weighted visual-haptic integration absent until ~8 years (Gori et al. 2008). **ARCH for confidence-as-FLAG; the WEIGHT is late and calibration-dependent.**
- **Neuroscience S.** Confidence compared across vision and audition as precisely as within a task (de Gardelle, Le Corre & Mamassian 2016); LIP neurons carrying the decision also carry certainty (Kiani & Shadlen 2009). Qualification: domain-general AND domain-specific confidence representations coexist in PFC (Morales, Lau & Fleming 2018). **ARCH: a common currency across a modality boundary, partly reconstructed.**
- **Comparative S.** Chosen-vs-forced opt-out signature in rhesus (Hampton 2001), rats (Foote & Crystal 2007) and honeybees (Perry & Barron 2013). Dissents: first-order associative reading (Carruthers 2008; contra Smith, Couchman & Beran 2014); pigeons repeatedly fail. **ARCH: insect; translatable-around argument live; the species dissociation is itself dissenting.**
- **Artificial agents s.** Factorial ablation PE > P > DE > D: aleatoric and epistemic uncertainty are separately necessary for model-based control (Chua et al. 2018 PETS); per-example uncertainty weighting of imagined rollouts (Buckman et al. 2018). Emergent-communication agents modulate effort by difficulty but no explicit confidence value in the channel was verified (Evtimova et al. 2018). **Ablation met, emergence not met.**

---

## 3. Negative and dissenting findings (first-class, per GOV-CONTRACT-1)

These are the results most likely to be dropped in practice, so they are listed before the classification.

1. **None of the five has a universal obligatory grammatical encoding.** 32% of 620 languages have no article; ~40% of 222 no grammatical past; 43% of 418 no grammatical evidential; 52% of 190 no agent / patient case distinction. The relations are not read off morphology. (Typology, all candidates.)
2. **Reality-status marking is diffused culture on the typological evidence.** Evidentiality is areal, not genetic (de Haan); tenselessness is areal too. (Typology, REALITY STATUS, TEMPORAL.)
3. **REALITY STATUS is probably not one relation.** Typology splits possible from counterfactual (von Prince et al. 2022) and rejects a unitary irrealis (Bybee 1998); development shows an early pretend / actual marker but a late four-way distinction; neuroscience shows a subsystem-independent decision over a subsystem-shared graded signal (Dijkstra & Fleming 2023); comparative work has only source-of-encounter provenance in rodents and nothing on imagined-vs-observed. The MECH-545 lesion "observed, remembered, simulated and counterfactual states indistinct across the boundary" may be deleting two or three relations at once.
4. **CONFIDENCE and REALITY STATUS are frequently fused** in the morphology (Boye's two subdomains in one epistemic system; the DeLancey / Aikhenvald mirativity dispute). This argues against treating them as two separately preserved invariants in the lesion list without an explicit dissociation control.
5. **CONFIDENCE splits into flag and weight.** Decision confidence is early (12-20 months); precision-weighted integration across a modality boundary is late (~8 years, Gori et al. 2008). Only the flag has developmental precedence.
6. **Translatable-around arguments exist for three candidates and must be preserved.** Temporal reference is recovered without tense (Tonhauser 2011); animal what-where-when could be trace strength (Suddendorf & Corballis 2007); animal opt-out could be first-order (Carruthers 2008); reality status in adults is reconstructed from signal strength (Dijkstra & Fleming 2023). Each is exactly the possibility GOV-CONTRACT-1 says to keep: the relation may be recoverable at the receiver without ever being marked in transit. MECH-545's within-boundary control is what separates a lost tag from a degraded signal.
7. **The artificial-agents domain is mostly ablation, not emergence.** For IDENTITY, REALITY STATUS and CONFIDENCE every strong result ablates a hand-installed inductive bias. Only TEMPORAL (Bi & Zhou 2020) and AGENCY (Choi et al. 2019) show the variable arising unspecified. Emergence is the test that matters for architectural standing; this domain meets it twice in five.
8. **Marked structure in a channel is not forced by need.** Emergent languages generalise without being compositional and compositionality is selected by transmission ease (Chaabouni et al. 2020; Kirby, Cornish & Smith 2008). So a distinction being marked in any language, natural or emergent, defaults to CULT. Temporal reference in emergent communication needed an architectural intervention, not task pressure (Lipinski et al. 2023). This is direction-(b) evidence for MECH-546 and a standing caution against the inference "agents invent it, therefore it is required".
9. **Sensory-level timing is modality-specific** (Motala et al. 2018) and the **agency signal is effector-specific** (Reznik et al. 2014); **confidence has domain-specific PFC representations alongside domain-general ones** (Morales, Lau & Fleming 2018). Where a relation is architectural, its implementation is local -- consistent with ARC-142's "engines may encode an invariant differently", and also with the embodied reading of the mechanism.
10. **Species dissociations are dissenting evidence.** Pigeons fail uncertainty monitoring where monkeys, dolphins, rats and bees pass; the wrasse identity result is contested. A required invariant should not dissociate cleanly by species.

---

## 4. Ledger-shaped records (paste-ready for `cognitive_contract_invariant_ledger.v1.json` when it exists)

Field names follow GOV-CONTRACT-1's twelve-field record. `ree` and `lesion_prediction` are pointers only: `ree` is domain 6 (not assessed here); `lesion_prediction` is MECH-545's pre-registered signature, unchanged.

### identity
- **candidate:** identity
- **definition:** whether two representations (across engines or across time) concern the same entity; persistence of an individual across transformations
- **linguistic:** S -- switch-reference, definiteness, obviation, anaphora reinvented in unrelated stocks (Roberts 2017; Dryer WALS 37; Heine & Kuteva 2002); no single universal device
- **developmental:** S -- numerical identity at 10-12 months, pre-sortal-language (Xu & Carey 1996; Wilcox 1999; Cacchione et al. 2013)
- **neural:** S -- modality-invariant identity cells in human MTL (Quian Quiroga et al. 2009, 2012)
- **comparative:** S -- cross-modal individual recognition in horses; mirror self-recognition in magpies, contested in wrasse (Proops et al. 2009; Prior et al. 2008; Kohda et al. 2019 / Vonk 2020)
- **artificial_agent:** s -- necessity by ablation (Piloto et al. 2022), partial emergence (Traub et al. 2023); object structure usually supplied
- **ree:** not assessed (domain 6; MECH-545 identity lesion; content-level owner ARC-080)
- **lesion_prediction:** MECH-545 -- broken persistence, duplicated selves / objects, incoherent credit assignment, unstable memory integration
- **alternative_explanation:** social ecology (conspecific recognition is a shared problem for every positive species); discourse disambiguation (typology); early identity inputs are spatiotemporal / embodied; object-level physics may just need object-level slots (task structure)
- **classification:** architectural (provisional) -- relation; format of early inputs embodied
- **confidence:** moderate-high; quorum 4 of 5 external domains (5 with partial)

### temporal_relation
- **candidate:** temporal relation
- **definition:** before / after / now between represented states; present vs anticipated; cause-before-effect order
- **linguistic:** S -- relation obligatorily recovered in tenseless languages (Tonhauser 2011); tense itself areal, absent in ~40% (Dahl & Velupillai WALS 66); TAM grams reinvented across 25 phyla (Bybee, Perkins & Pagliuca 1994)
- **developmental:** S -- causal launching order preferred hours after birth (Mascalzoni et al. 2013); arbitrary order late and language-assisted (Bauer et al. 1998; Lukowski et al. 2009)
- **neural:** S -- hippocampal time cells (MacDonald et al. 2011), LEC elapsed-time code (Tsao et al. 2018); sensory timing modality-specific (Motala et al. 2018)
- **comparative:** S -- what-where-when in scrub jays and cuttlefish, future planning in jays (Clayton & Dickinson 1998; Schnell et al. 2021; Raby et al. 2007); trace-strength dissent (Suddendorf & Corballis 2007)
- **artificial_agent:** S -- elapsed time emerges unspecified in RNNs (Bi & Zhou 2020); temporal reference in emergent communication needs architecture, not pressure (Lipinski et al. 2023)
- **ree:** not assessed (domain 6; content-level owners INV-035, INV-104 class 3, MECH-539)
- **lesion_prediction:** MECH-545 -- cause / effect inversion, present vs anticipated confusion, memory / prediction contamination
- **alternative_explanation:** tense and arbitrary sequence memory are cultural; sensory-level timing is embodied and modality-local; behavioural what-where-when could be a decaying trace without a represented relation
- **classification:** architectural (provisional) for causal / episodic order; cultural for tense and arbitrary order-as-content; embodied at the sensory-timing level
- **confidence:** high among the five; quorum 5 of 5, and the only candidate with a preservation-under-lesion result in the typology domain

### reality_status
- **candidate:** reality status
- **definition:** whether a represented state is observed, remembered, imagined / simulated, or counterfactual
- **linguistic:** s -- evidentiality in 237/418 languages but areal (de Haan WALS 77/78); irrealis not one category (Bybee 1998), splits possible vs counterfactual (von Prince et al. 2022)
- **developmental:** S -- pretend / real bookkeeping at 15 months (Onishi et al. 2007); four-way distinction late and emotion-sensitive (Woolley & Ghossainy 2013; Carrick & Quas 2006)
- **neural:** S -- paracingulate sulcus predicts hallucination modality-independently (Garrison et al. 2015; Simons et al. 2017); decision is a threshold on a shared graded signal (Dijkstra & Fleming 2023)
- **comparative:** s -- rodent source-of-encounter memory only (Crystal et al. 2013, 2016); imagined-vs-observed untested in any non-human species
- **artificial_agent:** s -- untagged imagined data collapses model-based RL (Janner et al. 2019; Buckman et al. 2018); the tag never emerges
- **ree:** not assessed (domain 6; content-level owners MECH-094, MECH-365, MECH-271, ARC-092, MECH-430; the V3-buildable cousin flagged on MECH-545)
- **lesion_prediction:** MECH-545 -- confabulation-like commitment to imagined states, impaired counterfactual learning, psychosis-like representational error
- **alternative_explanation:** cultural diffusion of evidential marking; reconstruction from signal strength rather than a preserved tag; the candidate is a family (actual / possible / counterfactual; source vs actuality) rather than one relation
- **classification:** uncertain, architectural-leaning for a coarse actual / not-actual marker; the four-way relation as stated is unsupported as a single invariant
- **confidence:** low-moderate; quorum 2 of 5 (5 with partial) -- at the threshold, and the two S cells (developmental, neuroscience) each carry a dissent that reshapes the candidate

### agency_controllability
- **candidate:** agency / controllability
- **definition:** self-caused vs externally caused; who the actor is; whether the outcome is controllable
- **linguistic:** S -- morphological causative in 287/310 languages (Song WALS 111); semantic alignment reinvented independently (Donohue & Wichmann 2008); vehicle variable (Comrie WALS 98; Siewierska WALS 100)
- **developmental:** S -- goal attribution to a bodiless agent at 12 months (Gergely et al. 1995); actor bound to goal at 13 months (Buresh & Woodward 2007); action-effect binding by 9 months (Verschoor et al. 2010); self / other specular discrimination at 4 months (Rochat & Striano 2002)
- **neural:** S -- corollary discharge as a retaining translation mechanism across phyla (Crapse & Sommer 2008); cerebellar cancellation (Blakemore et al. 1998); controllability as an mPFC signal (Maier & Seligman 2016; Amat et al. 2005); effector-specific implementation (Reznik et al. 2014)
- **comparative:** S -- single corollary-discharge interneuron in cricket (Poulet & Hedwig 2006); electrosensory negative image in mormyrids (Bell et al. 1997, 1993); self-agency in chimpanzees (Kaneko & Tomonaga 2011)
- **artificial_agent:** S -- controllable factor discovered from own-action prediction, with collapse without it (Choi et al. 2019); controllability as organising variable (Thomas et al. 2017)
- **ree:** not assessed (domain 6; content-level owner MECH-256 and the reafference lineage)
- **lesion_prediction:** MECH-545 -- poor action learning, internal / external attribution errors, failed intentional planning
- **alternative_explanation:** every mind with effectors faces the same problem (embodied); implementation is per-effector and per-modality; "controllable" is defined relative to an action set
- **classification:** architectural (provisional; the strongest case of the five) for the coarse self-caused / not primitive; derived structure (intention, responsibility, social attribution) not assessed
- **confidence:** high among the five; quorum 5 of 5, with the least embodiment-confounded evidence (insect, electric fish, bodiless 2-D agent)

### confidence_precision
- **candidate:** confidence / precision
- **definition:** reliability / uncertainty attached to a representation, travelling with the content across the boundary
- **linguistic:** s -- epistemic domain coherent but fused with information source (Boye 2012); mirativity contested (DeLancey 1997; Aikhenvald 2012)
- **developmental:** S -- non-verbal decision confidence with ERN at 12-18 months, help-seeking at 20 months (Goupil & Kouider 2016; Goupil et al. 2016); reliability-weighted integration absent until ~8 years (Gori et al. 2008)
- **neural:** S -- common currency across vision and audition (de Gardelle et al. 2016); certainty co-represented in LIP (Kiani & Shadlen 2009); domain-general plus domain-specific PFC confidence (Morales et al. 2018)
- **comparative:** S -- opt-out signature in rhesus, rats, honeybees (Hampton 2001; Foote & Crystal 2007; Perry & Barron 2013); first-order dissent (Carruthers 2008); pigeons fail
- **artificial_agent:** s -- aleatoric and epistemic uncertainty separately necessary by factorial ablation (Chua et al. 2018); per-example weighting (Buckman et al. 2018); no emergence; no verified explicit confidence in an emergent channel (Evtimova et al. 2018)
- **ree:** not assessed (domain 6; content-level owner the precision / MECH-123 lineage)
- **lesion_prediction:** MECH-545 -- overcommitment, under-reaction to reliable predictions, failed precision-sensitive integration
- **alternative_explanation:** first-order associative account of opt-out; audience-design hedging (typology); precision-weighting is a late calibration achievement, not a given; confidence fused with source
- **classification:** split -- confidence-as-FLAG architectural (provisional); confidence-as-WEIGHT uncertain, embodied / calibration-dependent
- **confidence:** moderate; quorum 3 of 5 (5 with partial), all three S cells qualified

---

## 5. What this pull implies for the claims (routing notes, not dispositions)

- **MECH-545.** Two of the five pre-registered lesions are under-specified against the literature. The REALITY-STATUS lesion should say whether it deletes actual / not-actual, source, or counterfactual status (or all three, as a compound). The CONFIDENCE lesion should say whether it deletes the flag or the weight. The within-boundary control (MECH-537's encoded-but-not-exposed confound, INV-105 rung 2 vs 3) is not optional for any candidate, because four translatable-around arguments now exist. Routing: `/governance` Step 2b, as a note on the claim, not a status change.
- **ARC-142.** The developmental clause ("coarse primitives precede derived structure") is corroborated in outline for agency (self-caused / not at 4-9 months before goal attribution at 12) and for confidence (flag before weight) and reality status (pretend / actual before the four-way distinction). That is a reading, not evidence. Nothing here bears on the contract / translation / schema LAYERING, which is REE-internal.
- **MECH-546.** Direction (b) of its two-way test has three verified instances (tense, evidentiality, compositionality-by-transmission-ease classify as cultural); direction (a) has one suggestive instance (temporal reference needs architecture, not pressure, to enter a channel). The claim's own note said a lit-pull was owed before any citation is used as support; it has now been done and the balance is a weakening result for the mechanism as stated (Chaabouni entry). Routing: `/governance` may wish to record `evidence_direction: mixed` at the next cycle; not applied here.
- **GOV-CONTRACT-1.** The rule worked as designed on this corpus: it demoted five cells that a plain search returned as supports, and it split two candidates. Held-out record: this pull was NOT written from the rule's motivating cases and gives a different answer from a plain universality count on every row of the typology column. That is one non-degenerate case for GOV-HELDOUT-1 on GOV-CONTRACT-1's wording, recorded here for the next governance cycle to count.
- **The ledger chip.** When `chip-20260908-cognitive-contract-ledger` lands, section 4 is the paste source. Per-candidate `ree` fields stay empty until MECH-545 runs.

---

## 6. Verified sources by domain (identifiers resolved in-session; unverified classics are listed in the per-domain agent reports and were not counted)

**Domain 1 -- typology.** Dryer 2013 WALS ch. 37 (wals.info/chapter/37); Roberts 2017 doi:10.1017/9781316135716.017; Heine & Kuteva 2002 doi:10.1017/CBO9780511613463; Dahl & Velupillai 2013 WALS ch. 66; Tonhauser 2011 doi:10.1007/s10988-011-9097-2; Bybee, Perkins & Pagliuca 1994 ISBN 9780226086651; de Haan 2013 WALS ch. 77, 78; Bybee 1998 Anthropological Linguistics 40:257-271; von Prince, Krajinovic & Krifka 2022 doi:10.1353/lan.2022.0009; Song 2013 WALS ch. 111; Comrie 2013 WALS ch. 98; Siewierska 2013 WALS ch. 100; Donohue & Wichmann 2008 doi:10.1093/acprof:oso/9780199238385.001.0001; Boye 2012 doi:10.1515/9783110219036; DeLancey 1997 doi:10.1515/lity.1997.1.1.33; Aikhenvald 2012 doi:10.1515/lity-2012-0017; Lazard 1999 doi:10.1515/lity.1999.3.1.91.

**Domain 2 -- developmental.** Xu & Carey 1996 PMID 8635312; Wilcox 1999 PMID 10553669; Cacchione, Schaub & Rakoczy 2013 PMID 22906060; Mascalzoni et al. 2013 PMID 23587033; Bauer et al. 1998 PMID 9640427; Lukowski, Wiebe & Bauer 2009 PMID 19328556; Saxe & Carey 2006 PMID 16905110; Onishi, Baillargeon & Leslie 2007 PMID 17107649; Woolley & Ghossainy 2013 PMID 23496765; Carrick & Quas 2006 PMID 17087560; Gergely et al. 1995 PMID 7554793; Buresh & Woodward 2007 PMID 16930577; Verschoor et al. 2010 PMID 21738512; Rochat & Striano 2002 PMID 14717242; Goupil & Kouider 2016 PMID 27773566; Goupil, Romand-Monnier & Kouider 2016 PMID 26951655; Gori et al. 2008 PMID 18450446.

**Domain 3 -- neuroscience.** Quian Quiroga et al. 2009 PMID 19631538; Quian Quiroga 2012 PMID 22760181; MacDonald et al. 2011 PMID 21867888; Tsao et al. 2018 PMID 30158699; Motala et al. 2018 PMID 29343859; Garrison et al. 2015 PMID 26573408; Simons, Garrison & Johnson 2017 PMID 28462815; Dijkstra & Fleming 2023 PMID 36959279; Crapse & Sommer 2008 PMID 18641666; Blakemore, Wolpert & Frith 1998 PMID 10196573; Maier & Seligman 2016 PMID 27337390; Reznik et al. 2014 PMID 24898564; de Gardelle, Le Corre & Mamassian 2016 PMID 26808061; Kiani & Shadlen 2009 PMID 19423820; Morales, Lau & Fleming 2018 PMID 29519851.

**Domain 4 -- comparative.** Proops, McComb & Reby 2009 PMID 19075246; Prior, Schwarz & Guenturkuen 2008 PMID 18715117; Kohda et al. 2019 PMID 30730878; Vonk 2020 PMID 31209801; Clayton & Dickinson 1998 PMID 9751053; Schnell et al. 2021 PMID 34403629; Raby et al. 2007 PMID 17314979; Suddendorf & Corballis 2007 PMID 17963565, 2010 PMID 19962409; Crystal et al. 2013 PMID 23394830; Crystal 2016 PMID 26609644; Smith et al. 2017 PMID 27908748; Poulet & Hedwig 2006 PMID 16439660; Bell et al. 1997 PMID 9153391, 1993 PMID 8506312; Kaneko & Tomonaga 2011 PMID 21543355; Amat et al. 2005 PMID 15696163; Hampton 2001 PMID 11274360; Perry & Barron 2013 PMID 24191024; Foote & Crystal 2007 PMID 17346969; Carruthers 2008 doi:10.1111/j.1468-0017.2007.00329.x; Smith, Couchman & Beran 2014 PMID 23957740.

**Domain 5 -- artificial agents.** Piloto et al. 2022 PMID 35817932; Traub et al. 2023 arXiv:2310.10372; Locatello et al. 2020 arXiv:2006.15055; Bi & Zhou 2020 PMID 32341153; Lipinski et al. 2023 arXiv:2310.06555; Janner et al. 2019 arXiv:1906.08253; Buckman et al. 2018 arXiv:1807.01675; Choi et al. 2019 arXiv:1811.01483; Thomas et al. 2017 arXiv:1708.01289; Chua et al. 2018 arXiv:1805.12114; Evtimova et al. 2018 arXiv:1705.10369; Chaabouni et al. 2020 arXiv:2004.09124; Kirby, Cornish & Smith 2008 doi:10.1073/pnas.0707835105.

**Method.** Five parallel search agents, one per domain, each blind to the others, each required to resolve every cited identifier in-session (NCBI E-utilities, Crossref, arXiv, WALS chapter pages, Semantic Scholar) and to list unverifiable classics separately and uncounted. Empty PubMed queries were simplified once then routed to web search, never retried. Grading in section 1 and the classification in section 4 are this session's, applied after the five reports were read together.
