# Balaban-Feld et al. 2019 — State-dependent foraging among social fish in a risky environment

According to PubMed: Balaban-Feld, Mitchell, Kotler, Vijayan, Tov Elem & Abramsky 2019, *Oecologia* 190(1):37–45. [DOI 10.1007/s00442-019-04395-z](https://doi.org/10.1007/s00442-019-04395-z) (PMID 30929073).

## What the paper does

Behavioural ecology experiment with goldfish (*Carassius auratus*) in mixed-condition groups facing a little egret (*Egretta garzetta*) predator. Each group contained equal numbers of underfed and well-fed individuals; both conditions experienced the same predator and the same artificial pool with a refuge area and open foraging zone. The authors measured refuge-emergence behaviour, foraging participation, food consumption, and mortality across conditions.

## What the data show

Three quantitative findings:

1. **Underfed fish exhibited higher levels of risky behaviour** — they participated in more foraging outings and emerged from the refuge in frontal group positions, compared to well-fed individuals from the same groups.
2. **Underfed fish consumed more food** as a result of the riskier strategy.
3. **Underfed fish did not experience higher mortality** — the egret predator preferentially attacked groups of three or more fish and often captured fish in the chaotic period *following* a failed initial strike, rather than the first fish to emerge from refuge. The risk of being-first-to-emerge turned out to be lower than naive optimal-foraging models would predict, because predator targeting was group-density-dependent rather than first-emerge-dependent.

The architectural takeaway: refuge-vs-forage allocation under active predator threat is *state-dependent* (a function of internal energy / drive), not state-invariant. Within a single hazard regime, allocation varies with internal state across individuals.

## Why this matters for R4 (Phase 2 calibration target)

This is the closest direct empirical anchor in the pull to SD-054's reef-vs-forage substrate. Same animal class (fish), same architectural motif (refuge area + open forage zone + active predator), and quantitative behavioural data on the dependent variable that the Phase 2 falsifier needs to calibrate.

Three convergent implications for ARC-062 and the Phase 2 falsifier:

1. **The discriminator must read agent internal state** (drive_level / z_self / z_harm_a). This confirms Pull A's R1 verdict — the multi-stream default rather than the single-stream `z_world` only fallback. ARC-062 weak reading with `z_world` only is predicted to *fail* the state-dependence test on SD-054 because it cannot route the energy-vs-safety trade-off through any internal-state channel.

2. **Within-arm variation across seeds is the predicted signature**, not single-ratio convergence. Real fish in matched conditions allocate differently as a function of internal state; ARM_1 of the Phase 2 falsifier should similarly show within-arm spread that tracks `drive_level`. If all seeds converge to the same ratio, the discriminator is collapsing across what should be state-distinguished policies.

3. **For R4 numerical calibration**: the paper provides specific quantitative spread (% emergence frequency, % foraging participation differential between underfed and well-fed). Best biology-anchored target the pull surfaces is the *spread* of allocation across internal-state conditions, not a single mean. The Phase 2 acceptance threshold should specify a state-modulation slope, not a fixed allocation ratio.

## Why this matters for MECH-309

MECH-309 says trainers cannot invent rules. The state-dependent rule "forage more when underfed, refuge more when sated" is a real biological rule that the goldfish exhibit. For ARC-062 to reproduce it, the gated-policy + discriminator must develop policy heads that *differ* in their state-dependence — not just in their context-dependence. The Capkova/Mansouri 2025 PFC lesion dissociation (Pull A entry) showed three distinct sub-functions in the rule-apprehension layer; one of them (OFC-rule-value-updating) is the rule-value-by-state coupling that Balaban-Feld's data exhibits. ARC-062 weak reading addresses only the rule-maintenance leg; if its Phase 2 falsifier reproduces the density-dependence (Lima-Bednekoff signature) but fails the state-dependence (Balaban-Feld signature), the diagnosis routes to the OFC-analog substrate as the next-thing-to-wire.

## Mapping caveat

Goldfish-and-egret in artificial mesocosms is one specific instantiation. Coral reef fish facing reef-resident predators (e.g. moray eels, groupers, sharks) operate in a different regime: continuous predator presence rather than intermittent strikes; structural complexity of reef refugia varies along multiple axes (interstitial vs canopy refuge); different prey-predator size ratios. The state-dependence *shape* (energy-low → forage-more) is robust across taxa per the broader risk-allocation literature; the specific numerical ratio is system-specific. SD-054's persistent food-attracted-hazard regime is closer in temporal pattern to coral-reef ecology than to goldfish-egret mesocosm; the paper's quantitative ratios should be treated as illustrative rather than directly transferable. Sample size n=12 paired groups is moderate; replication across reef-fish species would tighten calibration.

## Confidence reasoning

Source quality 0.83 — solid *Oecologia* paper, peer-reviewed, methodologically clean experimental design with active predator. Mapping fidelity 0.85 — highest among entries in this pull because the system (fish + refuge + predator + state-dependent allocation) maps directly to SD-054. Transfer risk 0.25 — goldfish-egret to coral-reef-fish is a real but small step within behavioural ecology; the state-dependence shape generalises. Confidence 0.81 reflects: strongest direct anchor for R4 fish-refuge calibration with the species-specific-numerical-ratio caveat captured in mapping_caveat.

## Failure signatures for the cluster

1. **State-invariant allocation**: if ARC-062 weak reading on SD-054 produces refuge-use that is invariant across agent `drive_level` / energy, Balaban-Feld predicts this is a failure of state-dependent gating. The discriminator is not reading interoceptive signals — direct R1 confirmation needed for the multi-stream default. Diagnostic: vary starting `drive_level` across seeds in ARM_1 of Phase 2 falsifier; PASS = monotone refuge-vs-state relationship; FAIL = invariant allocation.

2. **Within-arm convergence**: if ARC-062 produces no within-arm variation in refuge-use across seeds (all seeds converge to the same ratio despite varied internal state), the discriminator is collapsing across what should be state-distinguished policies. Diagnostic indicator that the gated policy has not internalised state-dependence even if it has internalised context-dependence.
