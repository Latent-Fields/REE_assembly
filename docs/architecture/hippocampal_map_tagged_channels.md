# Hippocampal Map-Tagged Channels — Heterogeneous Affect Encoding in the REE Architecture

**Status:** design reference (V4 scope; informs V3 SD-011 generalization)
**Created:** 2026-05-08
**Source pull:** [`evidence/literature/targeted_review_hippocampal_affect_stream_count/`](../../evidence/literature/targeted_review_hippocampal_affect_stream_count/)
**Related claims:** SD-011, SD-012, SD-014, ARC-007, MECH-216, MECH-285, INV-049

---

## 1. Why this document exists

The 2026-05-08 lit-pull was triggered by a generative question: *if SD-011's dual nociceptive split (z_harm_s + z_harm_a) is real, how many other affect streams have the same kind of privileged hippocampal-map representation, and is the architectural mechanism uniform?* The literature answer, across 10 papers in 4 channels, is **partial generalization with heterogeneous mechanisms**. This doc records the resulting picture so it does not need to be re-derived from primary sources whenever V3/V4 design touches an affect channel.

The naive reading — "N parallel z_harm-style streams" — does not survive the literature. The supported reading is **heterogeneous N channels with channel-appropriate mechanisms**, where the mechanism varies systematically with the channel's temporal and behavioural profile.

---

## 2. The four channels

| Channel | Substrate | Mechanism | Strength | Canonical citations |
|---|---|---|---|---|
| **Reward / goal** | Dorsal CA1, subiculum; LC noradrenergic write | Mixed: dedicated identity-stable population *and* rate remapping under neuromodulator drive | Strong | Gauthier & Tank 2018 ([DOI](https://doi.org/10.1016/j.neuron.2018.06.008)); Kaufman et al. 2020 ([DOI](https://doi.org/10.1016/j.neuron.2019.12.029)); Duvelle et al. 2019 ([DOI](https://doi.org/10.1523/JNEUROSCI.1578-18.2018)); Xiao et al. 2020 ([DOI](https://doi.org/10.1007/s00422-020-00830-0)) |
| **Fear / acute aversive** | Dorsal CA1 | Global / partial place-field remapping; long-term stabilization; replay enrichment | Strong | Moita et al. 2004 ([DOI](https://doi.org/10.1523/JNEUROSCI.5492-03.2004)); Wang et al. 2012 ([DOI](https://doi.org/10.1523/JNEUROSCI.0480-12.2012)); Ormond et al. 2023 ([DOI](https://doi.org/10.1523/JNEUROSCI.1450-22.2022)) |
| **Anxiety / sustained threat** | **Ventral CA1**, projection-target-defined (vCA1->LHA) | Modulated firing in a dedicated subpopulation; *no* place-field remapping | Moderate (single paper) | Jimenez et al. 2018 ([DOI](https://doi.org/10.1016/j.neuron.2018.01.016)) |
| **Social / conspecific position** | Dorsal CA1; cross-species (bat + rat) | Dedicated population with stable receptive fields; subset shows shared self/other receptive fields | Moderate-strong | Omer et al. 2018 ([DOI](https://doi.org/10.1126/science.aao3474)); Danjo et al. 2018 ([DOI](https://doi.org/10.1126/science.aao3898)) |

**Two unfilled cells in the table:**
- *Disgust / interoceptive aversive* — no direct hippocampal place-cell literature surfaced. Plausible 5th channel via insular projections; flagged for a future targeted_review.
- *SD-011 sensory/affective nociceptive split itself* — no hippocampal-level experiment dissociates A-delta-style proximity coding from C-fibre-style accumulated-deviation coding at the place-cell level. This is novel territory REE could occupy with a dedicated V3 experiment under appropriate substrate.

---

## 3. The three mechanism classes

Across the four supported channels, three distinct architectural mechanisms appear:

### M1 — Place-field remapping (global or partial)

The place ensemble *itself* reorganizes when the affective context changes. Cells alter their preferred firing locations, and the new representation can stabilize over days (Wang 2012). Cells that remap are preferentially recruited into sharp-wave ripple replay (Ormond 2023), which is the mechanism by which the new representation propagates to neocortex.

- *Best fit for:* acute, episodic affect (fear conditioning, reward-locus translocation).
- *REE analogue:* updates to z_world that reorganize the residue/place encoding when an affective event reaches the hippocampal write-channel. SD-011's z_harm_s is the closest current implementation.

### M2 — Modulated firing in projection-defined dedicated populations

Cells with stable spatial properties show firing-rate modulation under a specific affective state, *and* the cells carrying that modulation are anatomically defined by their projection target. Anxiety cells in vCA1 fire more in anxiogenic environments without changing their place fields, and they are enriched in the LHA-projecting (not BA-projecting) subset (Jimenez 2018).

- *Best fit for:* sustained states (anxiety, sustained drive, mood) that bias behaviour without requiring per-event map reorganization.
- *REE analogue:* a state-modulator architectural slot that biases existing channels rather than reorganizing them. SD-014's valence vector and z_beta come closest in current REE; a true M2 slot would have explicit projection-target binding to a downstream module (analogue of LHA's role in driving avoidance behaviour).

### M3 — Dedicated identity-stable populations

A small, specialized cell population fires for a specific channel-relevant content across environments where the surrounding place ensemble remaps randomly. The reward cells of Gauthier & Tank 2018 and the social place cells of Omer/Danjo 2018 are the canonical instances. These cells are not "place cells with affect modulation" — their identity is preserved across global remapping.

- *Best fit for:* identity-stable channel content that needs to be tracked across context shifts (reward identity, conspecific position).
- *REE analogue:* a per-channel cell-class slot whose activations survive substrate-wide reorganization. No current REE component implements this directly; the closest is the persistence of z_harm streams across z_world remappings, but the REE implementation is at the latent-vector level, not the cell-population level.

### Cross-class observations

- **A single channel can use more than one mechanism.** Reward uses both M3 (dedicated cells) and M1 (rate remapping under LC). Fear primarily uses M1 but the replay-enrichment finding (Ormond) is functionally an M3-adjacent stability signal.
- **Channels segregate by anatomical substrate.** Reward, fear, social → dorsal CA1. Anxiety → ventral CA1. Projection target (LHA vs BA) further splits ventral channels. The hippocampus is not a single map but a stack of partially-segregated maps.
- **Conjunctive cells exist** (Xiao 2020). Channels are not strictly orthogonal populations — there is a continuum from pure place to pure channel-specific with hybrids and within-session migrations between modes.

---

## 4. Implications for the SD-011 generalization

SD-011 currently splits the harm stream into z_harm_s (sensory-discriminative, A-delta analogue) and z_harm_a (affective-motivational, C-fibre analogue). The literature supports this kind of split *in principle* — multiple affect channels do get privileged map representation. But the mechanism cannot be assumed uniform across channels.

For each REE affect/behaviourally-privileged channel, the architectural choice is now explicit:

| REE channel | Suggested primary mechanism | Justification |
|---|---|---|
| z_harm_s (sensory harm proximity/intensity) | **M1** (remapping-style write to z_world) | Acute, location-bound, episodic — matches the fear-conditioning and reward-translocation pattern |
| z_harm_a (affective-motivational harm accumulation) | **M2** (state-modulator) | Sustained, non-localized, biases behaviour without needing per-event map reorganization — matches the anxiety pattern |
| z_goal / appetitive (SD-012 homeostatic drive) | **M1 + M3** (remapping at goal-zone *and* dedicated identity-stable subpopulation) | Reward channel uses both in the literature; goal locus reorganizes under LC drive but identity persists across environments |
| z_social (V4 candidate, currently absent) | **M3** (dedicated identity-stable) | Conspecific position is the canonical M3 case; if REE adds a social channel in V4, the natural form is a dedicated subpopulation analogue |
| Sustained drive / arousal (SD-014 z_beta family) | **M2** | Already a state-modulator; the literature anxiety case validates this design |

**The headline architectural commitment:** REE should not assume a single template ("every affect channel is implemented like z_harm"). The channel's *temporal profile* (acute vs sustained), *content stability* (event-bound vs identity-stable), and *behavioural role* (avoidance vs approach vs tracking) jointly determine which mechanism is appropriate. The hippocampal literature gives us a three-mechanism toolkit; we should pick per channel.

---

## 5. The projection-target dimension (currently unexploited)

Jimenez 2018's vCA1->LHA-vs-vCA1->BA dissociation is the most important architectural finding in this lit-pull that *is not yet reflected* in REE. In biology, a single cell population (vCA1 anxiety cells) carries different functional identities depending on which downstream module receives its output:

- vCA1->LHA = anxiety/avoidance drive
- vCA1->BA = contextual fear memory

Same source neurons; different downstream consumers; functionally distinct channels.

In REE terms, this means an affect channel is defined not just by *what writes it* (the source-side identity, e.g. z_harm_s vs z_harm_a) but also by *which module reads it* (the projection-side identity, e.g. tactical E3 vs strategic E3 vs default-mode replay). The current SD-011 architecture is source-side only — z_harm_s and z_harm_a have distinct identities at the encoder, but their downstream consumers are not architecturally segregated.

For V4, this argues for a two-axis channel taxonomy:

| | Tactical-E3 read | Strategic-E3 read | Default-mode / sleep read |
|---|---|---|---|
| z_harm_s | acute avoidance | route planning | consolidation of harm-locus memory |
| z_harm_a | sustained drive bias | long-horizon mood-conditioned planning | mood-state replay |
| z_goal | approach selection | route planning | reward-place consolidation |
| z_social (V4) | conspecific tracking | social plan modeling | social-context replay |

Each cell of this matrix is a candidate read-site that could in principle be wired separately. Most current REE implementations collapse the row (one channel, one read) — V4 should consider exploding the matrix where the projection-side dimension is functionally meaningful.

---

## 6. What this changes for V3 and V4

**V3 (current):**
- No immediate claim-registry edits required. SD-011 stands; the generalization is informational.
- One high-value experimental gap: the SD-011 sensory/affective dissociation has no direct hippocampal-level test in the literature. A discriminative experiment under appropriate substrate (V_s monostrategy cleared, MECH-269 substrate landed) would be a genuine novel contribution. Park for the substrate-queue audit.

**V4 (planning):**
- Adopt the three-mechanism toolkit (M1 remapping / M2 state-modulator / M3 dedicated identity-stable) as the default vocabulary for any new affect or behaviourally-privileged channel.
- Add the projection-target dimension to the channel taxonomy. Channels are not just defined by source identity; they need a downstream-consumer specification.
- Treat the disgust / interoceptive aversive gap as a known unknown. If V4 wants to model homeostatic harm-from-within (organ damage, illness, satiation-violation), this is the channel to formalize and the lit-pull to do.
- The social channel is a clean V4 candidate. If added, M3 (dedicated identity-stable) is the literature-warranted form, with the option of shared self/other receptive fields (Danjo 2018) as a primitive for multi-agent simulation.

---

## 7. Open questions

1. **Do M1 and M3 share substrate or are they distinct populations?** Xiao 2020's continuum reading suggests shared substrate with continuous variation in channel-specificity. If so, REE should not enforce strict population segregation.
2. **Is the M2 (modulated firing) class scalable to >1 sustained-state channel?** The vCA1 literature has anxiety cells; whether parallel sustained-state channels (mood, sustained drive, sustained arousal) coexist via separate projection targets is largely unstudied.
3. **What is the developmental/learning order in which these channels acquire their map-tagging?** The persistence finding (Wang 2012) shows fear-tagging stabilizes long-term, but how it interacts with the existing reward-tag and social-tag is not addressed in any single paper. For REE, this matters for SD-017 sleep-aggregation and consolidation order.
4. **Does the SD-011 sensory/affective split exist at the cell-population level or only at the latent-vector level in REE?** This is the experimental question we could ask first.

---

## 8. References (full DOI)

Primary lit-pull entries:
- Gauthier & Tank 2018 — [DOI 10.1016/j.neuron.2018.06.008](https://doi.org/10.1016/j.neuron.2018.06.008)
- Duvelle et al. 2019 — [DOI 10.1523/JNEUROSCI.1578-18.2018](https://doi.org/10.1523/JNEUROSCI.1578-18.2018)
- Kaufman et al. 2020 — [DOI 10.1016/j.neuron.2019.12.029](https://doi.org/10.1016/j.neuron.2019.12.029)
- Xiao et al. 2020 — [DOI 10.1007/s00422-020-00830-0](https://doi.org/10.1007/s00422-020-00830-0)
- Moita et al. 2004 — [DOI 10.1523/JNEUROSCI.5492-03.2004](https://doi.org/10.1523/JNEUROSCI.5492-03.2004)
- Wang et al. 2012 — [DOI 10.1523/JNEUROSCI.0480-12.2012](https://doi.org/10.1523/JNEUROSCI.0480-12.2012)
- Ormond et al. 2023 — [DOI 10.1523/JNEUROSCI.1450-22.2022](https://doi.org/10.1523/JNEUROSCI.1450-22.2022)
- Jimenez et al. 2018 — [DOI 10.1016/j.neuron.2018.01.016](https://doi.org/10.1016/j.neuron.2018.01.016)
- Omer et al. 2018 — [DOI 10.1126/science.aao3474](https://doi.org/10.1126/science.aao3474)
- Danjo et al. 2018 — [DOI 10.1126/science.aao3898](https://doi.org/10.1126/science.aao3898)

REE cross-references:
- SD-011 (dual nociceptive streams) — [`docs/claims/claims.yaml`](../claims/claims.yaml)
- SD-012 (homeostatic drive) — [`docs/claims/claims.yaml`](../claims/claims.yaml)
- SD-014 (valence vector) — [`docs/architecture/anticipatory_affect_conjunction_vs_dual_channel.md`](anticipatory_affect_conjunction_vs_dual_channel.md)
- Lit-pull synthesis — [`evidence/literature/targeted_review_hippocampal_affect_stream_count/SYNTHESIS.md`](../../evidence/literature/targeted_review_hippocampal_affect_stream_count/SYNTHESIS.md)
