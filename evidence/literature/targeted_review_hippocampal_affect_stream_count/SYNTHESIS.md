# Synthesis: Hippocampal Map-Tagged Affect Streams — Count and Mechanism

**Date:** 2026-05-08
**Question:** How many functionally distinct affective/valence channels show evidence of (a) distinct remapping (global or rate remapping triggered by the affective context) vs (b) modulated firing without remapping in the hippocampus? Does SD-011's dual-nociceptive split generalize to an N-affect-stream map-tagging claim?
**Scope:** Rodent + bat (no primate hippocampal single-unit data with affect dissection found in this pull); CA1 emphasis with vCA1 noted where relevant.
**Entries:** 9 papers across 4 channels.

---

## Per-channel evidence table

| Channel | Remapping evidence | Modulated firing / dedicated population | Substrate | Strength | Key citations |
|---|---|---|---|---|---|
| **Reward / goal** | Rate remapping near goal under LC drive (Kaufman 2020); partial remapping during reward-aversion task (Ormond 2023) | Dedicated reward-cell population stable across remapping (Gauthier & Tank 2018); conjunctive place-reward continuum incl. within-session transitions (Xiao 2020); place ensemble itself is **value-free** (Duvelle 2019, negative result) | Dorsal CA1, subiculum; LC noradrenergic write-channel | **Strong (0.80 mean)** | Gauthier 2018, Duvelle 2019, Kaufman 2020, Xiao 2020 |
| **Fear / acute aversive** | Global/partial remapping after fear conditioning (Moita 2004); long-term stabilization across days (Wang 2012); partial remapping in mixed reward-aversion task with replay enrichment (Ormond 2023) | Not the headline finding for fear — remapping is the dominant signature | Dorsal CA1; converges across shock and predator-odor paradigms | **Strong (0.81 mean)** | Moita 2004, Wang 2012, Ormond 2023 |
| **Anxiety / sustained threat** | Not the headline mechanism — the encoding is by modulated firing, not place-field reorganization | Dedicated anxiety-cell population in **vCA1** projecting specifically to LHA (not BA); causally required for avoidance (Jimenez 2018) | **Ventral CA1**, projection-target-defined | **Moderate (0.82, single paper)** | Jimenez 2018 |
| **Social / conspecific position** | Not directly tested as remapping; coding is at the cell-class level | Dedicated social-place-cell population in dorsal CA1 of bat (Omer 2018); joint and shared receptive fields for self/other in rat CA1 (Danjo 2018) | Dorsal CA1; cross-species (bat + rat) | **Moderate-strong (0.80 mean)** | Omer 2018, Danjo 2018 |
| **Disgust / visceral** | No direct hippocampal place-cell literature found in this pull | — | — | **Absent** (gap) | None |
| **Sensory-discriminative vs affective-motivational nociception (SD-011 split)** | Not directly tested at the hippocampal level — fear-conditioning literature bundles the two | — | — | **Untested at this resolution** (gap) | None |

---

## Direct answer: how many channels?

**Four channels with hippocampal map-tagging evidence**, by a relaxed criterion (dedicated population OR clear remapping OR projection-defined modulated firing):

1. **Reward / goal** — strongest evidence; both dedicated population (Gauthier & Tank) and rate-remapping mechanism (Kaufman/LC).
2. **Fear / acute aversive** — strongest remapping evidence; persists across days; recruited preferentially into replay.
3. **Anxiety / sustained threat** — dedicated population, but **modulated firing** in vCA1, not place-field remapping. Defined by projection target (LHA).
4. **Social / conspecific position** — dedicated population across bat and rat; some cells abstract over agent identity.

**Two gaps:**
- **Disgust / visceral / interoceptive aversive** — no direct hippocampal place-cell literature surfaced. This is itself a finding: either disgust is not map-tagged at all, or it is and nobody has run the right experiment. Likely the latter, given that interoceptive aversive signals reach the hippocampus via insular and entorhinal projections.
- **The SD-011 sensory/affective nociceptive split itself** — not directly tested. Fear-conditioning literature bundles A-delta and C-fibre signals. A clean test would dissociate proximity/intensity coding from accumulated-deviation coding at the place-cell level. As far as this lit-pull found, no such experiment exists.

---

## Distinct remapping vs modulated firing — the architectural distinction

The user's specific request was to distinguish (a) *distinct remapping* from (b) *modulated firing only*. The evidence splits cleanly:

| | Remapping (global or rate) | Modulated firing only |
|---|---|---|
| **Reward** | Yes (rate remapping under LC; goal-zone overrepresentation) | Yes (dedicated cells are not 'remapping' — they are a stable, identity-preserving subpopulation that *itself* contradicts random remapping) |
| **Fear** | Yes (Moita 2004 global/partial; Wang 2012 long-term) | Less the headline; firing-rate effects exist but the structural remapping is dominant |
| **Anxiety** | No clean remapping evidence | **Dominant mechanism** — vCA1 cells show state-dependent firing-rate modulation in anxiogenic environments |
| **Social** | Not framed as remapping; the social channel is detected by cell-class identity, not by spatial reorganization | Dominant — social-place-cells are characterized by what they fire for, not by how their fields move |

**The architectural reading:** the hippocampus uses *different mechanisms for different channels.* Acute fear and reward-translocation drive map reorganization (remapping). Sustained-state channels (anxiety) and identity channels (social, dedicated reward cells) operate by population-level modulated firing without spatial reorganization. This is not a uniform N-channel architecture — it is a heterogeneous one in which the channel type and the substrate co-vary.

---

## SD-011 generalization verdict

**Does SD-011 generalize?** Partially — and the partiality is informative.

**Yes, in the sense that:** the hippocampus reserves dedicated/projection-specific cells or remapping populations for at least four behaviourally-privileged channels (reward, fear, anxiety, social), not just for raw spatial coding. SD-011's intuition that affect channels deserve their own architectural slots is supported.

**But not in the sense of "N parallel z_harm-style streams":** the four channels do not share a common architectural template. Reward and fear do remapping in dorsal CA1; anxiety does modulated firing in vCA1 with projection-target specificity; social does dedicated-cell encoding in dorsal CA1 with cross-agent shared receptive fields. Whatever the generalization is, it cannot be "all affect channels do what z_harm_s and z_harm_a do."

**A more honest restatement of the generalization:**

> The hippocampal map admits multiple privileged channels, where each channel is realized by *the architectural mechanism best suited to its temporal and behavioural profile.* Acute, episodic affect (fear, reward translocation) gets place-field remapping. Sustained states (anxiety) get modulated firing in projection-defined ventral populations. Identity-stable channels (reward identity across environments, conspecific position) get dedicated populations with stable receptive fields. The SD-011 architecture (z_harm_s + z_harm_a) is consistent with this picture but is not the only template.

---

## Implications for V3 / V4

1. **The "affect channel" framing may be too narrow.** Social/conspecific position is privileged but is not affective. The right framing may be "behaviourally privileged channels" — affect is one important subset but not the defining feature.

2. **Heterogeneous mechanisms argue for heterogeneous V3/V4 substrate.** If we want anxiety, social, reward, and harm channels in V3/V4, we should not implement them all the same way:
   - **Acute affective events** (harm spike, reward delivery) → trigger remapping-style updates to z_world (consistent with current SD-011 design for harm).
   - **Sustained states** (anxiety, sustained drive — SD-053 family) → modulated firing analogue, i.e. a state-modulator that biases the existing channels rather than reorganizing them.
   - **Identity-stable channels** (reward locus, conspecific identity) → dedicated subpopulation analogue, i.e. cells/units that preserve their function across substrate-wide reorganization. Harm and reward should both have these.
   - **Projection-target specificity** (vCA1->LHA vs vCA1->BA) → in V3/V4 terms, channels should be defined not just by source identity but by which downstream module (E3-tactical vs E3-strategic vs default-mode) reads them. This dimension is largely unexploited in the current architecture.

3. **The SD-011 sensory/affective nociceptive split is novel territory.** No existing hippocampal literature directly tests the dual-stream architecture at the place-cell level. This is an experimental gap that REE could address with a discriminative paradigm — separately manipulating proximity/intensity (sensory) vs accumulated deviation (affective) and asking whether they drive distinct CA1 remappings or distinct dedicated cells. That would be a high-value V3 experiment.

4. **Disgust/interoceptive aversive is unscored.** Worth a follow-up lit-pull or a literature gap memo. Given REE's interest in homeostatic drive (SD-012) and harm-stream architecture (SD-011), interoceptive aversive signals from insular projections are a likely candidate for a fifth channel.

---

## Recommendations

- **No new claim registration needed from this pull.** The findings refine and motivate but don't directly support or weaken existing claims to a degree that would change governance status. SD-011 is already provisional with strong evidence; this generalization question is upstream of registration.
- **Architecture memo (low-priority, propose):** consider drafting `docs/architecture/hippocampal_map_tagged_channels.md` summarizing the heterogeneous-mechanism picture and listing the four channels + projection-target dimension as a design space for V4. This is cheap and would consolidate the lit-pull into a usable design reference. Confirm with user before writing.
- **Experimental gap (flag):** the SD-011 sensory/affective nociceptive split has no direct hippocampal-level test in the literature. A discriminative experiment in V3 — under appropriate substrate — would be a genuinely novel contribution rather than a replication. Park this for the substrate-queue audit.
- **Lit-pull gap (flag):** disgust/interoceptive-aversive hippocampal coding. If an interoceptive-aversive channel matters for V4 (likely yes, given SD-012's homeostatic-drive scope), this gap should be filled. Tag for a future targeted_review.

---

## Aggregate confidence and quadrant

- **Channels with strong support:** reward (4 entries, mean 0.75), fear (3 entries, mean 0.81)
- **Channels with moderate support:** anxiety (1 entry, 0.82), social (2 entries, mean 0.80)
- **Channels with no direct evidence:** disgust, SD-011-style sensory/affective harm split

**Overall lit-pull confidence in the SD-011 generalization (interpreted as "multiple affect/behaviourally-privileged channels have hippocampal map representation"):** **0.80** — high, but with the architectural caveat that the channels are not homogeneous in their mechanism. The naive "N parallel streams" reading does not survive the literature; a refined "heterogeneous N channels with channel-appropriate mechanisms" reading is well supported.
