# Lundqvist, Herman & Miller (2018) — Working Memory: Delay Activity, Yes! Persistent Activity? Maybe Not

**Claim:** ARC-063 (CandidateRule field with tolerance-gated availability). **Direction:** supports (the explicit fork adjudication, toward B with sparse reactivation). **Confidence:** 0.75.

## What the paper argues

This perspective is the head-on adjudication of the persistent-firing-versus-activity-silent debate — the exact fork the V3-EXQ-666 autopsy posed. Lundqvist, Herman and Miller concede the uncontroversial half ("The question is not whether delay activity is a WM mechanism. It clearly is.") and then attack the contested half: the evidence for *continuous* persistent spiking is largely an **artifact of averaging** spikes across time and across trials. On single trials, delay activity is "more sparse than persistent" — it "often occurs in sparse transient bursts" (gamma bursts, from the authors' own LFP work, Lundqvist et al. 2016, Neuron). Between bursts, the memory does not vanish; it is carried by short-term synaptic plasticity: "spikes leave an 'impression' in the networks that maintains WM information between spiking," and "memories are carried by temporary changes in synaptic weights, 'impressions' left in the network" during the quiescent periods. Delay activity, yes; *persistent* activity, maybe not.

## Why this closes the fork for the CRF

Read against V3-EXQ-666 the mapping is almost literal. The CRF's `crf_frac_active` is `_n_active_steps / _step` — the fraction of ticks on which some matched rule clears threshold. That is an **averaged-activity readout**, and this paper's central warning is that averaged activity *hides* sparse-but-maintained coding. A differentiated rule in ARM_2 matches sparsely, so it reads ~0.016 active fraction — yet, if maintenance is synaptic, it is fully available the whole time. The collapse the autopsy found is the precise failure Lundqvist et al. predict for any activity-based maintenance metric.

The verdict the paper supports is not naive fork A ("keep every available rule firing" — biologically false and, as Compte/Wang show, infeasible at pool scale) and not a pure binary fork B either. It is the **synthesis**: a persistent *synaptic* store (the "impression") that survives silence, refreshed and read out by *sparse* bursty reactivation when the context recurs. For the CRF this licenses both prescriptions already converging from Stokes and Mongillo:

1. **Maintain availability as an activity-decoupled trace** that persists across context-absent ticks and decays only on a long horizon — the "impression left in the network."
2. **Do not measure maintenance by per-tick firing.** Replace/supplement `crf_frac_active` with a maintained-pool readout (fraction of differentiated rules whose availability would clear threshold on context recurrence). The current metric is the averaged-activity artifact this paper exists to warn against.

## Caveat

This is a perspective built on re-interpreting existing data, not a new experiment, and the burst-coding account remains actively contested — it was published back-to-back with a strong-persistent-activity rebuttal (Constantinidis et al. 2018, "Persistent Spiking Activity Underlies Working Memory," same issue). So the CRF should adopt the *form* (activity-silent maintenance plus sparse reactivation) without asserting the biological debate is fully settled. Fortunately the substrate recommendation is robust to that uncertainty: even the persistent-activity camp agrees a maintained item need not be *selected/read-out* every moment, and the CRF's engaged-rule sustained term (fork A) and silent-pool trace (fork B) are complementary, not mutually exclusive.

## Confidence reasoning

High mapping fidelity (0.82): the paper's core diagnosis (averaging hides sparse-but-maintained coding) is a direct description of the `crf_frac_active` readout failure. Source quality is strong-for-a-perspective but it argues from reinterpretation and the burst account is contested, so it sits below the primary-data ceiling. Transfer risk is low-moderate.
