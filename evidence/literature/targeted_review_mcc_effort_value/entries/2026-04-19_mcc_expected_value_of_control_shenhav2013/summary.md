# Shenhav, Botvinick & Cohen 2013 — The expected value of control: an integrative theory of ACC function

**Source:** *Neuron* 79(2):217-240, [10.1016/j.neuron.2013.07.007](https://doi.org/10.1016/j.neuron.2013.07.007). Via PubMed (PMID 23889930).

## What the paper does

Shenhav, Botvinick and Cohen respond to the long-running puzzle of dACC — that it seems to be involved in everything: conflict monitoring, error detection, value computation, reward prediction error, effort integration, surprise — by proposing that dACC computes a single quantity, the *expected value of control* (EVC), and that the diversity of findings reflects the diversity of *inputs* to that computation rather than a diversity of functions. EVC has three components: the expected payoff from a controlled process, the amount of control required to achieve that payoff, and the cost of cognitive effort. dACC uses EVC to decide whether to allocate control, where to allocate it, and how much. The paper re-interprets a large body of prior dACC findings under this framework and lays out testable predictions.

## Key findings relevant to the claim

- **Three-component decomposition of dACC output.** EVC = expected payoff − expected control requirement × effort cost. This is the paper's central computational claim.
- **Unified account of heterogeneous findings.** Conflict-monitoring signals, error-related negativity, reward prediction error, effort-integration signals — all are EVC inputs, not separate functions.
- **Dynamic allocation.** dACC does not simply evaluate options; it allocates control to processes. This makes dACC a *meta-controller* rather than a value comparator.
- **Effort cost is explicitly modelled.** Unlike foraging-value frameworks, EVC treats cognitive effort as a scarce resource with an explicit cost term that must be paid by any controlled process.

## How this maps onto REE (the translation)

EVC gives us the cleanest computational specification we have seen for what SD-032b (dACC/aMCC-analog) actually outputs. For each candidate operating mode *M* (external-task, internal-planning, internal-replay, offline-consolidation), the dACC-analog should compute:

```
EV_net(M) = expected_payoff(M) - control_required(M) * effort_cost
```

where:
- `expected_payoff(M)` is the benefit of being in mode M given current z_world and z_harm signals (this is the Kolling 2012 environment-value contribution).
- `control_required(M)` is the policy-reshaping cost of entering mode M from the current mode — high for disruptive transitions (e.g., task → replay), low for already-primed transitions.
- `effort_cost` is the scarcity of cognitive resources, which ree-v3 can tie to SD-012 homeostatic drive (energy budget).

The salience-network coordinator (SD-032a) then selects `argmax_M EV_net(M)`; the mode-switch trigger (MECH-259) fires when a non-current mode's EV exceeds the current mode's EV by some threshold. This is a richer substrate than the simple urgency-weight / z_harm_a wiring we originally considered — it explicitly models the cost of switching, not just the urgency to switch.

For MECH-260 (dACC bias suppression against monostrategy), EVC makes a sharp prediction: the suppression of a dominant-but-suboptimal strategy should scale with `control_required(alternative_mode)` — it costs more to suppress a strong habit, and dACC-analog activity should reflect that cost. A monostrategy fish-swimming-same-route agent (cf. the whimsy visualization entry) would show exactly this pathology: its `control_required` for mode-switching is chronically high because no alternative mode has been rehearsed.

## Limitations and caveats

EVC is a *normative* theory; it specifies what the computation is without specifying how it is implemented. ree-v3 must make design choices for all three terms that EVC does not constrain (how to represent "amount of control required", how to discount effort cost dynamically). The paper also does not resolve the Kolling vs Shenhav debate about whether foraging value and EVC are the same thing or distinct — that debate is continued in the 2016 follow-up (separate entry).

EVC competes with alternative accounts (foraging-value, error-likelihood, surprise-minimisation). All are partially correct; EVC is the most computationally concrete but is not the settled consensus. There are also critics who argue that the "control cost" term is under-specified and effectively treated as a fitted parameter, which weakens the explanatory force.

For ree-v3 specifically, EVC is a useful vocabulary but we should treat the specific three-term decomposition as a hypothesis. A minimum-viable SD-032b can be built against EVC's structure with the explicit knowledge that we may later need to replace one or more of its terms with different primitives (e.g., Kolling-style environment-average-value as a better representation of `expected_payoff`).

## Confidence reasoning

0.84. Influential, highly-cited Neuron review; the three-term decomposition is the single cleanest computational spec for dACC we have available. High mapping fidelity because EVC's three terms have direct ree-v3 analogues. Low transfer risk because EVC is already a computational theory rather than a species-specific physiological claim. The discount is because EVC is one of several competing frameworks and its empirical validation is largely re-interpretation of prior findings, not prospective prediction. Still the strongest candidate to anchor the SD-032b design specification.
