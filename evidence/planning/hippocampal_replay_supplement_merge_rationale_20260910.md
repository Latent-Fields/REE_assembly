# Merge rationale: 2026-09-09 hippocampal replay interface-maintenance supplement

**Inputs.** LOCAL = `853e336bbb:docs/thoughts/2026-09-09_hippocampal_replay_interface_maintenance_supplement.md` (262 lines, unlanded, discarded after this merge). ORIGIN = `origin/master:` same path (226 lines). Written six minutes apart by two sessions that did not know about each other. Below I call them **pass A** (local) and **pass B** (origin), which is how the merged document names them.

---

## 1. Conceptual differences

### 1.1 They do not actually disagree about what a completed causal chain is

This is the first thing to say plainly, because the framing in the merge request implies a rivalry that does not exist on inspection. Pass A's six links and pass B's six gates map onto each other almost one-to-one:

| Pass A link | Pass B gate |
|---|---|
| 1 established mapping / 2 relevant change | 1 measured change |
| 3 preserved local content | 2 local preservation |
| 4 lost receiver use | 3 access loss |
| 5 selective repair (correct vs shuffled, matched marginals) | 4 pair-specific maintenance + 5 causal restoration |
| 6 consolidation exclusion | 6 rival exclusion |

Both insist the chain must close inside one design and both explicitly reject an additive proof assembled from separate preparations. Where they differ is sharpness of exclusion language, and pass B is sharper in exactly one place worth keeping: it names what does *not* count as a representational change — "neuron turnover, registration noise, behavior, or a coordinate rotation that preserves the receiver-potent subspace." That last clause pre-empts the stable-subspace rival at the definition stage rather than leaving it to the rivals section. I took pass B's gate list as the spine and folded pass A's "established mapping before drift" requirement in.

Pass A has one conceptual asset here that pass B lacks entirely: the **four-way taxonomy of confounded outcomes** — local consolidation / retrieval triggering and completion / stable routing / interface repair, with the observation that all four produce the same observable of restored downstream performance after upstream change. That is the single best paragraph in either document. It is why the gates exist, and neither the rivals section nor the assay design is properly motivated without it. Retained verbatim in spirit as §2's closing block.

### 1.2 Gate 0 vs staged contrasts: not a live methodological dispute

The premise that pass A uses "staged minimal contrasts" *instead of* Gate 0 is wrong. **Pass A also has a Gate 0**, called "Gate 0—validate the failure as interface-specific," with four probes: no drift, relevant invertible drift, unused-coordinate drift, known inverse adapter. Pass B's Gate 0 has three probes plus an oracle-inverse requirement. Two sessions independently converged on the same methodological commitment. That convergence is itself worth noting — it is the one place the parallel-authorship accident produces evidence rather than duplication.

Given they converged, the question becomes which execution is better, and it is **pass B's, on three specific points**:

1. Pass B states the two benign cases it must reject *by name* (invariant-subspace drift; global task loss) before listing probes. Pass A lists probes and lets the reader infer what they rule out.
2. Pass B gives the **failure directions as diagnoses**, not just as pass conditions: "if the oracle cannot restore use, the lesion is not an interface lesion"; "if null-space drift degrades use, the subspace identification is invalid." Pass A only states the proceed condition. The difference matters, because a failed Gate 0 in pass B's version tells you which part of your instrument is broken, and in pass A's version it just stops you.
3. Pass B adds the **ordering constraint**: sender-only drift is the first identification case; receiver-only and joint drift are generalization tests, because joint drift leaves the locus of repair underdetermined. Pass A does not order the drift conditions at all, which is a real hole — its §3.2 separately notes that joint sender/receiver drift breaks Rule–O'Leary's long-horizon guarantee, but it never draws the design consequence.

So: **pass B's Gate 0 supersedes pass A's, and pass A's Gate 0 is dropped.** But this is a supersession within a shared commitment, not one framing defeating another.

Pass A's staging keeps two things pass B's does not, and both are retained inside pass B's Gate 0:

- The **two-interface requirement** — one interface drifted and repairable, a second stable or affected only in unused coordinates — which is inherited from the parent assay B spec and is the only structural control that makes a nonspecific arousal/plasticity effect *visible* rather than merely argued against. Losing this would silently weaken assay B relative to what the parent document already committed to.
- The **staging rationale**: don't buy a pairing × timing factorial before either instrument works independently. Pass B also defers timing to stage two but does not say why in cost terms.

### 1.3 Where they genuinely disagree: how strong Káli–Dayan is

This is the only real substantive conflict, and it is a flat contradiction in the bottom lines.

- **Pass A:** "The strongest direct result is computational: Káli and Dayan explicitly model an intact hippocampal trace becoming inaccessible ... then restore access by replay-driven reassociation." Pass A's audit says the correspondence-update mechanism "is genuine interface reassociation in the model. It is not merely another label for strengthening the stored hippocampal trace."
- **Pass B:** the same paper contains *two* maintenance operations; **either one rescues episodic recall, combining them yields no clear extra benefit, and for semantic memory ordinary cortical learning on replay is the more important of the two.**

Pass B is right and pass A is wrong-by-omission. Pass A's claim (that the refresh operation is *distinct from* trace strengthening) is true and survives; but pass A never reports that the rehearsal operation rescues equally well, and its bottom line therefore promotes Káli–Dayan to "strongest direct result" when the model actually declines to award unique necessity to interface repair — inside its own simulation, with no biology involved. That is the most consequential single difference between the documents, because pass A's version of the bottom line makes the campaign's interface-maintenance interpretation look better supported than it is.

**Resolved wholly in pass B's direction.** Pass A's "strongest direct result is computational" sentence is deleted and replaced with pass B's adjudication. Pass A's mechanical description of *why* refresh is genuine reassociation is kept, because it is compatible and it explains what the operation does.

### 1.4 Different self-descriptions of epistemic status

Pass B: "design-generative, not evidential." Pass A: "the literature motivates assay B; it does not provide biological closure for R4's interface-maintenance interpretation." These are the same claim; pass B's phrase is more portable and pass A's names the specific claim (R4) at stake. Both kept, in that order.

---

## 2. Material content unique to each

### 2.1 Káli–Dayan: pass A more complete on construction, pass B more complete on adjudication

**Pass A only:** three lower feature areas + MTNC; 100 binary units per area; reciprocal all-to-all symmetric weights; Boltzmann machine reducing to an RBM because within-area connections are unsimulated; **cue threshold = bitwise Hamming distance 20**; **cleanup threshold = Hamming distance 5**; the ~**90% replay / 10% new experience** ratio in the transfer simulations versus balanced replay in the correspondence-maintenance comparison; and an explicit assumed-versus-shown list.

**Pass B only:** the recall criterion (clamp two feature areas, complete the third); "local cleanup memories are hard-coded"; contrastive-divergence-like learning; **the two-operation decomposition and the finding that either rescues**; the semantic-memory asymmetry.

Neither is complete alone. The merged §3.1 is the union, ordered so that pass B's adjudication is the punchline rather than a caveat. Pass A's Hamming thresholds and the 90/10 ratio are quantitative facts that a reader needs to evaluate the model's fragility and would have been lost.

### 2.2 Rule–O'Leary: pass B is better and brings a paper pass A missed entirely

**Pass A only:** 100 encoding units; OU-like gradual drift vs abrupt one-feature-at-a-time resampling; **plasticity applied after each 5 of 100 features change**; eventual preferred-tuning shift after extensive drift; **continuous symmetries permit an unanchored global rotation**; large infrequent drift and decoder/recurrent drift reduce stability; joint sender+receiver drift voids the long-horizon guarantee.

**Pass B only:** the authors describe the Hebbian–homeostatic coupling as an **ansatz requiring physiological confirmation** (a source-honesty flag that materially weakens the rival's biological standing and belongs in the text); response normalization as an intermediate variant; the origin and long-term updating of the recurrent internal model are left open; and **Micou & O'Leary 2026** — a whole paper absent from pass A, showing heavy-tailed sparse tuning jumps make unsupervised readout correction *easier*, and raising the **code-drift versus world-change ambiguity**.

That ambiguity is the deepest conceptual item in either document and pass A does not have it in any form. It generates pass B's debt #8 and is the reason a "successful repair" is not self-certifying: a self-healing readout can correct a truthful update away, and an experimenter scoring restored performance cannot tell. Retained as a named rival class (§5.6) and a debt, not just a footnote.

**Verdict on the request's question:** pass B's Rule–O'Leary treatment is more complete; pass A's Káli–Dayan treatment is more complete on mechanics and less complete on judgment. Neither version dominates on both.

### 2.3 Evidence matrix: near-disjoint coverage, union is the whole point

Shared rows (10): Káli–Dayan, Rule–O'Leary, Rule 2020, Gallego 2020, Gonzalez 2026, Ji–Wilson 2007, Rothschild 2017, Maingret 2016, Gridchyn 2020, Kovács 2016.

**Pass A only (14):** Harvey 2023, Nitzan 2020, Takigawa 2026, Okyere 2026, Lansink 2009, Barnes–Wilson 2014, Bendor–Wilson 2012, de Sousa 2019, Cowansage 2014, Tanaka 2014, van de Ven 2016, Roux 2017, Cho 2025, Thompson 2026.

**Pass B only (9):** Micou–O'Leary 2026, Ólafsdóttir 2016, Berners-Lee 2021, Geva-Sagiv 2023, Clawson 2021, Deceuninck–Kloosterman 2024, Widloski–Foster 2025, Keinath 2022, Peters 2026.

Each version has load-bearing rows the other simply lacks. All 33 retained. The ones I would defend hardest:

*From pass B:*
- **Widloski–Foster 2025.** ~25% of replays lack ripples, and ripple timing depends on decoded replayed location. This invalidates the intervention target of every ripple-triggered design in the matrix, including two of pass A's own nulls. Pass A has no measurement-validity item at all. Promoted from a matrix row to a named design constraint (§6.5), because it changes what arms D/E can even be implemented as.
- **Berners-Lee 2021.** The best existing content → identified receiver → later behaviour adjacency. Its absence from pass A is a straight coverage hole in the row of the argument pass A cares most about.
- **Peters 2026.** Coordinated *orthogonal* drift across areas preserving cross-area geometry is the strongest form of the stable-scaffold rival — it removes the interface problem with no maintenance mechanism at all. Pass A's §5.1 argues this rival from Gallego/Rule/Gonzalez, none of which shows coordination across areas.
- **Deceuninck–Kloosterman 2024.** A behavioural causal null; pass A has only Kovács's map-stability null.

*From pass A:*
- **Barnes–Wilson 2014.** Imposed matched vs mismatched-novel vs delayed replay patterns: the closest thing in the biological literature to assay B's arm E, manipulating pattern identity × state × timing. Pass B's debt list asks someone to "develop a within-context permutation" without noting that a precedent exists in another pathway. Keeping this is the difference between an unprecedented design and a design with a known analogue.
- **Cowansage 2014 + de Sousa 2019 + Tanaka 2014.** Pass B carries the completion/rehearsal rival on Clawson alone. Pass A's three make it much harder to dismiss: a cortical trace can drive behaviour with the hippocampus off (Cowansage), local ensemble reactivation alone produces systems-consolidation-like change (de Sousa), and cortical reinstatement can be causally broken at retrieval (Tanaka). This rival class needs to be strong, because it is arm G.
- **Nitzan 2020.** The only causal interareal transmission demonstration in either matrix — fills the "causal influence, no repair" cell that otherwise sits empty.
- **Thompson 2026.** Procedural replay survives hippocampal lesion. A scope limit on replay authority that neither the rivals nor the debts would otherwise carry.
- **Roux 2017.** Behaviour intact despite local representational damage — the inverse dissociation, and a warning that behavioural stability is weak evidence of representational stability.
- **Takigawa 2026.** Physically lateralizing two competing traces to opposite V1 hemispheres is a design idea as much as an observation.

### 2.4 Assay design: pass B's arms, pass A's guardrails

**Pass B only:** the formal endpoint `U = performance(message available) − performance(message ablated or counterfactually replaced)`, with `x_t`, `D_s`, `A_t` notation; the lettered arm table; the estimand `D > max(E, F, G)`; the explicit warning that `D > B` alone is uninterpretable; the instruction to sweep maintenance interval against drift rate (without which the local rival is handicapped and the comparison is rigged); the requirement of symmetric local adaptation under joint drift; "regressing out unequal local recall after the fact is insufficient because consolidation may already have altered which items remain available."

**Pass A only:** the frozen-before-maintenance list; drift-in-unused-coordinates as a *negative instrument control* and inverse adapter as *positive control* (pass B has the oracle but not the negative-control framing); equivalence tests rather than nonsignificance; held-out episodes + recombined relations + a second receiver query; frozen evaluation endpoints with adaptive probes reported separately; report subspace overlap and transfer separately; **continue drift after one-step rescue — transient remapping followed by collapse is not maintenance**; and the **permitted-outcome-language table**.

Two things here deserve calling out.

**The arm sets are not the same set, and merging them improved the design.** Pass A's arm 5 is "ordinary full-example rehearsal/co-exposure as a matched-data upper bound" — *online paired* experience, testing whether offline scheduling adds anything. Pass B's arm G is "receiver-local ordinary rehearsal/completion" — a *local* rival with no sender message. These are different rivals answering different questions, and each session had only one. The merged design has both, as G (local completion) and H (paired co-exposure), giving eight arms. Correspondingly I **rejected pass A's decision to combine self-healing and cortical completion into a single comparator** ("This comparator deliberately instantiates the joint Rule–O'Leary plus cortical-completion rival"). A combined arm cannot say which local mechanism won, and if it beats correct pairs you learn nothing about which rival to pursue. Pass B separates F and G; that is the better call.

**The outcome-language table has no counterpart in pass B and is worth more than its length.** It preregisters what each result pattern licenses you to say, which is the only durable protection against post-hoc reinterpretation of an ambiguous rescue. I kept it and rewrote every row against the merged eight-arm lettering, and added three rows the merge made available: `C` failing to restore `U` (the drift model is invalid, not the hypothesis), Gate 0 failing, and rescue-then-collapse.

### 2.5 Citations and search reporting

Pass B has a real footnoted Sources section with 19 full bibliographic entries; pass A has inline DOI links and no titles or author lists. Pass B's is correct scholarly practice and I adopted it for the whole merged matrix.

**This has an honest cost.** For the 14 pass-A-only studies I have DOIs, venues, and surnames but no recorded titles. I did **not** reconstruct titles from memory — in a document that will replace the canonical copy, a plausibly-wrong title is worse than a missing one. Those footnotes carry author, year, venue where stated, and DOI, marked "[Title not recorded in the source pass.]", with a note in the Sources preamble. Completing them is logged as a documentation debt.

Search streams: pass B's per-stream table with an explicit stopping result per stream is the better structure; pass A's numbered list carries the actual query strings, which is what makes the search reproducible. Merged into pass B's table with pass A's query strings folded into the query-families column, plus three streams pass B did not report (imposed/cued replay pairing, TMR nulls, domain scope of replay authority).

---

## 3. Retention decision

**They are complementary, and the merge carries both — but not symmetrically, and not as a diplomatic split.** Pass B wins every head-to-head where they conflict; pass A supplies most of the material neither the conflicts nor the framing touch.

Concretely: **pass B owns the frame** (gates, Gate 0, the Káli–Dayan adjudication, the endpoint definition, the arm lettering and estimand, sourcing). **Pass A owns the guardrails and roughly half the evidence** (the four-way taxonomy, the model construction parameters, the enumerated rival classes, the measurement rules, the outcome-language table, the causal-interareal / imposed-pairing / cortical-completion / domain-scope rows). If forced to keep only one document I would keep pass B — its bottom line is not overstated and pass A's is. But the cost would be real and I would not pay it voluntarily: dropping pass A loses Barnes–Wilson, the completion rival's biological teeth, the outcome-language table, the durability requirement, and the two-interface control.

### Things I dropped, and why — challenge these first

1. **Pass A's Gate 0 (§6.3, four contrasts).** Superseded by pass B's, which names the benign cases, gives failure diagnoses, and orders sender-only first. Pass A's negative-instrument-control and positive-control framing was carried across; only the structure was dropped.
2. **Pass A's bottom-line claim that Káli–Dayan is "the strongest direct result."** Contradicted by pass B's reading of the same paper. This is the one deletion that changes the document's conclusion, and it changes it in the more conservative direction.
3. **Pass A's combined self-healing + completion comparator (§6.2).** Replaced by separate arms F and G. Rationale in §2.4 above.
4. **Pass A's separate "Matrix adjudication" and pass B's "Why the biological chain remains open."** Merged into one §4.1 rather than kept as two passes over the same ground. Pass B's three-family diagnosis became the frame; pass A's per-study "nearest pieces" list became the detail under it. Nothing substantive lost; one layer of duplication removed.
5. **Pass A's numbered search-stream list as a structure.** Query strings all survive inside the merged table; the list format does not.
6. **Pass A's access-code scheme (`FT`/`AP`/`AR`/`PP`).** Standardized to pass B's (`FT`/`AM`/`ABS`/`PRE`). Where the two passes disagreed about access to the same study — Ji–Wilson, Rothschild, Gridchyn, Rule 2020 — **I recorded the stronger claim**, on the reasoning that if one pass inspected full text then full text was inspected. This is the one merge decision I am least comfortable with, because the codes are per-pass session facts and I am asserting a union I did not personally verify. Marked in the access key. Flag it if the codes are meant to be audit trail rather than bibliographic status.
7. **Titles for the 14 pass-A-only sources.** Not dropped so much as never present; deliberately not reconstructed. See §2.5.

### Too close to call

- **Numbered vs unnumbered headings.** I went with pass A's numbering. The merged document is 375 lines, longer than either input, and the rationale and any future review need stable cross-references (§6.3, §4.1). Purely a legibility judgment; reverse it freely, it touches no content.
- **Whether §5's enumerated rival classes and §4.1's three-family diagnosis are redundant.** They cut the same material differently — §5 is "what the assay must beat," §4.1 is "why the existing evidence fails." I kept both and made sure neither restates the other's sentences, but a reader who thinks the document is too long should look here first.
- **Debt-list length.** Merging 12 + 10 debts deduplicated to 15, which is a lot. I could not find two I was confident were the same debt rather than two aspects of one.
- **Pass A's §3.3 ("the models are competitors, not confirmations").** Short, unique to pass A, and arguably implied by the audits that precede it. I kept it because it names pair identity, endpoint competence, timescale ratio, and receiver-scaffold stability as *the* decisive experimental variables, which is the hinge between §3 and §6. But it is the most cuttable section in the merged document.
