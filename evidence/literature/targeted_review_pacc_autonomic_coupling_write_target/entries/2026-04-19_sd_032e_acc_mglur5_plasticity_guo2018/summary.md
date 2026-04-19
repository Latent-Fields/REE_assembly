# Guo et al 2018 — ACC LTP in chronic pain, mGluR5 mechanism

## What the paper did

Guo and colleagues used adult male rats with peripheral nerve injury to establish a chronic pain phenotype, then recorded from ACC synapses both in slice and in vivo over a 7-14 day window. They found that sustained C-fibre (slow, unmyelinated, affective-pain-carrying) input drove long-term potentiation at ACC synapses, mediated by metabotropic glutamate receptor 5 (mGluR5) signalling. Pharmacologically blocking mGluR5 both prevented the LTP and reversed the behavioural sensitisation phenotype. The plasticity had a distinct timecourse: it required days of sustained input to saturate and days of nociceptive quiescence to return toward baseline.

## Key findings relevant to SD-032e

This paper provides the cleanest cellular-mechanism anchor for SD-032e's core architectural move. The REE proposal — sustained z_harm_a produces a slow-timescale shift in a downstream variable — is an abstraction over exactly this kind of synaptic-plasticity process. The EMA operator SD-032e uses is a high-level way to say "accumulate the slow input into a persistent gain/bias state." The biology shows the accumulation is real, operates on days-timescale, and is reversible if the input abates.

Three findings matter specifically. First, the timescale is *days* in rodent ACC, not minutes or hours. SD-032e's EMA rate needs to reflect this — a decay constant corresponding to thousands or tens of thousands of timesteps, not hundreds. Second, the write target in the biology is *local ACC synaptic efficacy*, not a remote variable that ACC writes into. This refines the architectural mapping. Third, the plasticity has an explicit decay path when input abates, which bears on the offline-normalisation question.

## Translation to REE

The cellular mechanism supports a slight revision to SD-032e's architecture. Rather than having pACC-analog write directly into drive_level, a more biologically faithful mapping would have pACC-analog accumulate its own internal gain state (a slow EMA of z_harm_a), and have *that gain state* modulate pACC's downstream output — which in turn influences SD-012's drive_level via the existing pathway. This is one more layer of indirection than the current SD-032e spec, and for a first implementation it may not be worth the complexity. But the SD doc should note that the direct-write framing compresses two biological steps (ACC plasticity, then ACC-modulated downstream influence) and is a simplification.

On the offline-decay question: Guo 2018 is consistent with (but does not directly test) a sleep-normalisation hypothesis. The plasticity is reversible given nociceptive quiescence, and there is a separate literature on sleep-pain bidirectional coupling that I did not pull for this review. The cleanest decision for SD-032e is the one already in the plan: default `pacc_offline_decay=0.0` and flag that any non-zero value instantiates a distinct sleep-recalibration claim that must be registered separately with its own literature (separate from MECH-092 SWR replay, separate from INV-049 offline-necessity).

## Limitations and caveats

Rodent-to-agent transfer is always non-trivial. The mGluR5 mechanism is specific to mammalian glutamatergic signalling and does not constrain how an abstract agent implements the analogous slow-gain accumulation. The study is male-only, as much of the ACC chronic-pain literature has been historically; female-specific circuitry differences have been reported elsewhere and are not addressed here.

## Confidence reasoning

Confidence is 0.68. Source quality is good (Cerebral Cortex, well-replicated chronic-pain paradigm, mechanistic pharmacology). Mapping fidelity is moderate-good: the cellular mechanism maps cleanly onto an EMA abstraction and constrains the timescale usefully, though it refines the write-target framing SD-032e currently uses. Transfer risk is moderate. This paper is the most useful of the four for setting SD-032e's config defaults — specifically, for choosing a slow decay constant and for framing the offline-decay question as a separate claim.
