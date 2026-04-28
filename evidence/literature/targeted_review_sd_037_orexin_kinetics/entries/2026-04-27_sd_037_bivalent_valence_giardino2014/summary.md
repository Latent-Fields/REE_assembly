# Giardino & de Lecea (2014) -- Hypocretin neuromodulation across stress and reward

## What the paper does

This is a short, well-cited Current Opinion in Neurobiology review by de Lecea and a
postdoc working in his lab. The argument is structurally simple: hypocretin/orexin is a
peptide neuromodulator with one source population (lateral hypothalamus) and projections
across hypothalamic, extended amygdala, brainstem, and mesolimbic targets, and it
modulates dysregulated states at both ends of the valence axis -- chronic stress and
hyperarousal on one side, compulsive drug-seeking on the other. The paper is short enough
that it does not introduce new data; rather, it integrates the empirical work in 2012-2014
into a coherent neuromodulatory account.

## Findings relevant to SD-037

The SD-037 architecture commits to an override_signal computed from two inputs:
drive_level (a positive-valence-adjacent signal: hunger, metabolic demand) and
sustained-threat context (a negative-valence signal: rolling z_harm window). The output
of the integrator can swing toward threat-active coping (raising the PAG freeze-gate
threshold via MECH-280) or toward drive-driven goal seeding (gating the SD-012
drive->z_goal bridge). The key architectural commitment is that *one* integrator outputs
authority across *both* valence-axis directions. Without this bivalence, SD-037 collapses
into either a threat-gating module (overlapping with SD-036 GABAergic decay) or a
drive-gating module (overlapping with the homeostatic AgRP/NPY literature).

Giardino & de Lecea make exactly the bivalent claim explicit: Hcrt operates across both
"negative and positive emotional valence" via "divergent behavioural domains." This
licenses the SD-037 architectural commitment to a single integrator with bivalent output,
which is the feature that makes it a third regulatory layer rather than a duplicate of
SD-036 or of MECH-186/187/188.

## REE translation and mapping caveats

The most important caveat is that the review covers *dysregulated* states -- chronic
stress, addiction -- rather than normal-range integration of drive and threat. SD-037's
typical operating regime is the latter (an animal under sustained but moderate hunger and
moderate threat, choosing whether to forage). Whether the same bivalent integrator story
holds in normal physiology is licensed by the wider Hcrt literature (Mileykovskiy 2005,
Lee 2005, Karnani 2020 are all in normal-state animals) but not directly by this paper.

A second caveat is dimensional. SD-037 commits to a unitary scalar override_signal.
Giardino & de Lecea describe Hcrt's stress-axis and reward-axis modulation as
mechanistically distinct (different downstream targets, partly different receptor
contributions). If the V3-EXQ-483 series surfaces phenotype-level dissociations, this
would be evidence that the scalar simplification needs to be relaxed.

## Confidence reasoning

I am setting confidence to 0.74. Source quality is moderate-high -- Curr Opin Neurobiol
is a respected review venue, and de Lecea's authorship adds weight, but the format is
short and integrative rather than primary. Mapping fidelity is high at the architectural
level: the bivalence claim is explicit. Transfer risk is moderate -- the data
underpinning the review are largely rodent and pathological-state, and translation to
REE's normal-state architecture requires the additional support from the empirical
parameter-anchoring papers in the same review series.

The honest reading: this paper provides the bivalence-at-architectural-level support for
SD-037 that distinguishes it from SD-036 and from the 5-HT goal-pipeline gain layer. It
is a useful but not load-bearing entry; the load-bearing entries for SD-037 are the
empirical electrophysiology and microinjection papers (Mileykovskiy 2005, Castro 2016,
Marino 2020, Johnson 2012).
