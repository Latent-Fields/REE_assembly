# Norman & Shallice 1986 -- The Supervisory Attentional System and contention scheduling

## What the paper did

Norman and Shallice published the foundational theoretical chapter that introduced the dual-mechanism architecture underpinning four decades of executive-function neuroscience. They argued that action selection requires two complementary control systems:

1. **Contention scheduling** -- a lower-level competitive activation process among action schemas, handling routine and overlearned behaviour. Schemas compete via lateral inhibition; the winner gates motor output.
2. **The Supervisory Attentional System (SAS)** -- a higher-level mechanism that overrides contention scheduling for novel, dangerous, or non-routine situations. The SAS biases schema activation based on willed/conscious goals; without the SAS, behaviour is captured by whatever environmental triggers most strongly activate routine schemas.

The two mechanisms are dissociable: frontal-lobe damage selectively impairs the SAS while leaving contention scheduling intact, producing the characteristic *utilisation behaviour* and *capture errors* of frontal patients. Posterior / basal-ganglia damage selectively impairs contention scheduling, producing apraxia and sequencing errors.

## Key findings relevant to the rule-apprehension vocabulary question

The Norman-Shallice 1986 dual-mechanism architecture is a near-direct functional analog of REE's ARC-062 + MECH-312 split. The translation is:

| Norman-Shallice 1986 | REE 2026 working term |
|---|---|
| Contention scheduling | MECH-312 arbitration |
| Action schema | Option / rule with context |
| Schema activation | Policy fragment activation |
| Lateral inhibition between schemas | Soft competition between options |
| Supervisory Attentional System | ARC-062 gated_policy + discriminator |
| SAS biasing schemas based on goals | Discriminator detecting non-routine context, gated_policy overriding routine |
| Frontal-lobe / SAS dissociation | (Falsifiable prediction for ARC-062-OFF arm) |

For Pull 4, the implications are sharp. ARC-062 has been described in REE-internal language as "top-down rule application via gated_policy + discriminator". The Norman-Shallice 1986 framing makes this much more precise: ARC-062 is a *Supervisory Attentional System* that overrides routine contention scheduling when the discriminator detects a non-routine context. That is a more functionally crisp claim than "top-down rule application", and it comes with 40 years of patient-data anchoring (frontal-lobe lesion syndromes) and an explicit dissociation prediction (lesion ARC-062 should produce utilisation-behaviour / capture-error patterns, not just degraded performance).

## How the findings translate to REE

Three concrete implications for cluster registration:

1. **R2 inheritable result**: the dual-mechanism dissociation gives REE a falsifiable prediction. A V3 substrate-validation experiment ablating ARC-062 (the SAS analog) should produce capture-error / context-perseveration patterns, not generalised performance degradation. If it produces the latter, the SAS-mapping is wrong.

2. **R4 renaming candidate**: ARC-062 could be renamed "supervisory attentional override" rather than "top-down rule application". The new name lands in 40 years of cognitive-neuroscience vocabulary and is more functionally precise.

3. **R3 genuine REE divergence**: Norman-Shallice 1986 says nothing about *simulation-mode write-gating*, dual-stream affective modulation, or V_s invalidation. Those remain candidate KEEP-AS-IS divergences.

## Limitations and caveats

The SAS as originally proposed is a single unified system. Modern executive-function accounts (Stuss 2011, Diamond 2013, Miyake & Friedman 2012) decompose it into multiple sub-components: working-memory maintenance, inhibition / response-suppression, set-shifting, error-monitoring, planning. Adopting SAS vocabulary commits REE to a coarse-grained reading; the modern multi-component decomposition is more empirically supported but less unified.

Also: the original 1986 paper is theoretical / book-chapter rather than empirical. The empirical anchoring comes from the broader Shallice frontal-lobe-patient programme. Inheritance is concept-level, not algorithm-level -- pairing with Cooper-Shallice 2000 (computational simulation) is the natural completion of the citation.

## Confidence reasoning

Scored 0.74. Source quality solid (foundational reference, 5000+ citations). Mapping_fidelity high (0.78) for the dual-mechanism architecture. Transfer_risk moderate (0.40) due to modern decomposition of SAS and the absence of direct algorithmic specification in the original paper. The paper feeds R2 (vocabulary inheritance: SAS, contention scheduling), R4 (rename ARC-062 to "supervisory attentional override"), and R3 (REE divergences are MECH-094 + dual streams + V_s, not the SAS layer).
