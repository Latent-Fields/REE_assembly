# Targeted review: MECH-295 (liking-stream as necessary intermediate between drive amplification and approach-cue selection)

**Claim:** MECH-295 (candidate, depends on SD-012, SD-015, SD-016) -- drive modulation (SD-012, e.g. hunger raising drive_level) does not produce approach behaviour by itself. It must propagate through liking-stream activation (the appetitive valence stream; biological analog: NAc shell hedonic hot spot, ventral pallidum, mu-opioid signalling, OFC pleasure coding) which supplies the cue-side pull for approach action selection. Without the liking-stream link, drive-amplified goal seeding produces a passive goal latent without behavioural consequence -- the EXQ-483 signature (override fires, PAG releases up, but approach_commit = 0.0 across all arms).

**Pulled:** 2026-04-26. 6 entries.

## Entries in this directory

| Entry | Paper | Year | Tag | Direction | Confidence | Key contribution |
|---|---|---|---|---|---|---|
| `2026-04-26_mech_295_mu_opioid_hedonic_hotspot_pecina2005` | Pecina & Berridge, J Neurosci | 2005 | b | supports | 0.78 | Anatomical hedonic hotspot in NAc shell; outside hotspot, mu-opioid increases intake without increasing liking. Substrate-level evidence for a discrete liking generator. |
| `2026-04-26_mech_295_vp_hedonic_coding_smith2011` | Smith Berridge Aldridge, PNAS | 2011 | a | supports | 0.82 | VP single-unit recording: drive change (sodium depletion) does NOT directly rewire cue-evoked motivational firing; palatability code recodes first, then cue firing follows. Drive -> liking -> wanting. |
| `2026-04-26_mech_295_hotspot_mapping_castro2014` | Castro & Berridge, Phys Behav | 2014 | b | supports | 0.74 | Decade of hotspot mapping consolidated: NAc shell + posterior VP hotspots are anatomically discrete from wanting territory. |
| `2026-04-26_mech_295_hyperdopa_wanting_not_liking_pecina2003` | Pecina Cagniard Berridge Aldridge, J Neurosci | 2003 | c | mixed | 0.70 | DAT-knockdown mice: more wanting, unchanged liking. Wanting/liking dissociation background. Supports weak reading; weakens naive strong reading. |
| `2026-04-26_mech_295_pleasure_systems_review_berridge2015` | Berridge & Kringelbach, Neuron | 2015 | a | supports | 0.76 | Architectural articulation of liking as a necessary input to motivated approach, not a passive readout. Most explicit theoretical statement of MECH-295's principle. |
| `2026-04-26_mech_295_incentive_learning_dickinson1994` | Dickinson & Balleine, Animal Learn Behav | 1994 | a | supports | 0.80 | Foundational behavioural demonstration: drive-state shifts do not directly rewire action selection; they must route through experienced hedonic value of the outcome. Pre-Berridge vocabulary for the same architectural principle. |

## Tag breakdown

- (a) direct support for liking-required-for-drive-to-approach: 3 entries (Smith 2011, Berridge & Kringelbach 2015, Dickinson & Balleine 1994). Mean confidence 0.79.
- (b) liking encoding only (substrate evidence without necessity link): 2 entries (Pecina 2005, Castro 2014). Mean confidence 0.76.
- (c) wanting/liking dissociation background: 1 entry (Pecina 2003). Confidence 0.70.
- (d) experimental gap: see below.

## Aggregate direction

5 supports, 1 mixed, 0 weakens. Mean confidence across all 6 entries: 0.77.

## Existing related entries elsewhere in the corpus

The corpus already contains substantial Berridge-related lit, tagged to other claims. Most relevant cross-references:

- `targeted_review_connectome_mech_117/entries/2026-03-29_mech_117_wanting_liking_dopamine_berridge1998` -- the foundational Berridge & Robinson 1998 paper, tagged to MECH-117 (wanting/liking dissociation as REE benefit_eval_head vs z_goal_latent).
- `targeted_review_connectome_arc_036/entries/2026-03-29_arc_036_hedonic_hotspot_opioid_berridge2009` -- Berridge 2009 hotspot review tagged to ARC-036.
- `targeted_review_connectome_mech_112/entries/2026-03-29_mech_112_wanting_liking_addiction_berridge2016` -- Berridge 2016 addiction review tagged to MECH-112.
- `targeted_review_sd_014/entries/2026-04-17_sd_014_wanting_liking_neural_dissociation_smith2011` -- Smith 2011 already tagged to SD-014. The MECH-295 entry here uses the same paper from a different mapping angle (necessity link rather than dissociation per se); Daniel may want to add MECH-295 to that entry's claim_ids_tested at the next governance sweep, OR keep this as the cross-referenced primary entry. I recommend keeping both because the mapping framings differ.
- `targeted_review_ghost_goal_search/entries/2026-04-26_ghost_goal_wanting_liking_berridge1998` -- Berridge 1998 tagged to ghost-goal context.

The MECH-295 directory takes the architectural-bridge framing (drive -> liking -> approach as a NECESSITY chain) which none of the existing entries directly carry. It is appropriate to have a dedicated MECH-295 directory rather than retrofit existing entries, given the distinct interpretive framing.

## Strongest support

Smith, Berridge & Aldridge 2011 (PNAS) is the strongest single piece of direct evidence. Single-cell VP recording shows that drive change (sodium depletion) does NOT directly rewire the cue-evoked motivational firing -- the palatability code at receipt has to be re-encoded first, and the cue-firing follows on subsequent trials. This is the cleanest mechanistic version of MECH-295's necessity claim that exists in the literature. Dickinson & Balleine 1994 is the cleanest behavioural version: drive-state shifts do not directly rewire instrumental responding without intervening outcome experience.

## Weakest gaps

The cleanest direct test of MECH-295's necessity claim does not exist in the literature in a single paper. That experiment is: (i) lesion or pharmacologically silence the NAc shell rostrodorsal hedonic hotspot OR mu-opioid antagonist in the hotspot, (ii) impose a drive manipulation (food deprivation), (iii) test cue-driven approach to a learned food-associated cue, (iv) prediction: drive-amplified approach should collapse. The fragments of this experiment exist across the Berridge corpus, but the integrated test is not delivered. This is tag (d) -- experimental gap. The available evidence supports the architecture but does not arbitrate strong necessity vs weaker bridge-but-not-strict-necessity readings.

The DAT-knockdown finding (Pecina 2003, tag c, mixed) is also a structural caution: it shows that wanting can be amplified without amplifying liking. The naive strong reading of MECH-295 ("elevated approach requires elevated liking") is incompatible with this. The precise reading ("liking-stream activation is the necessary BRIDGE; baseline liking is sufficient -- only the LINK must be intact") is compatible. The literature does not arbitrate which reading is correct; MECH-295 should specify.

## Recommended evidence_quality_note

> MECH-295 has strong literature support for its architectural premise (a separable liking-stream substrate exists) and its general principle (drive-state changes route through experienced hedonic value before reaching action selection). The strongest direct evidence is Smith Berridge Aldridge 2011 (VP single-unit; drive change recodes palatability before cue firing) and Dickinson & Balleine 1994 (instrumental devaluation requires outcome re-experience). The strong-necessity reading (no liking activation => no approach) versus the weak-bridge reading (baseline liking sufficient if bridge intact) is NOT arbitrated by the existing literature; the DAT-knockdown finding (Pecina 2003) is compatible only with the weak reading. The cleanest direct test of MECH-295 (mu-opioid antagonist in NAc shell hotspot + hunger + cue-approach) is an experimental gap. EXQ-483's failure signature is consistent with a broken liking-bridge wiring; Daniel should specify in the claim text whether MECH-295 commits to strong necessity (level-coupled) or weak necessity (link-required-but-baseline-sufficient).

## Confidence verdict

Aggregate literature confidence: 0.77 (mean of 6 entries). The claim is well-grounded in substrate evidence (b), well-grounded in mechanistic correlation evidence (a, Smith 2011 + Dickinson & Balleine 1994), and has clear architectural articulation in the Berridge & Kringelbach 2015 review. The remaining ambiguity is interpretive (strong vs weak necessity) rather than substrate-level, and resolving it requires the symmetric blockade experiment that does not yet exist.

For governance purposes: MECH-295 should NOT be promoted to active on literature alone, but the literature is strong enough to support a candidate -> provisional move IF V3 evidence (e.g. an EXQ-483 follow-up that wires the liking-stream and shows approach_commit recovers) becomes available. The literature's biggest contribution is showing that the alternative architectures (drive directly produces approach; liking is a passive readout) are weakly supported in biology.
