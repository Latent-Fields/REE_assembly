# Lukitsch (2025): An integral forward model of agency experience in thought and action

*Frontiers in Psychology* 16, 1524904. DOI: 10.3389/fpsyg.2025.1524904

## What the paper did

Lukitsch offered a recent theoretical synthesis of the agency-attribution literature, arguing against compartmentalised dual-pathway comparator models (the tradition descending from Frith's original formulation and developed by Synofzik, Vosgerau, and Newen into a two-step account). His alternative, "integral forward modelling" (IFM), treats the forward model as a unified mechanism in which predictions simultaneously function as motor commands and as predicted outcomes -- what he calls a "pushmi-pullyu" representation. Agency experience, on this view, is not the output of a separate comparator branch; it emerges from the temporally extended structure of prediction-error minimisation within the same loop that drives action and perception.

## Key theoretical claims

Two are directly relevant to SD-029. First, Lukitsch rejects architectures in which agency is computed by a dedicated, modularised comparator that runs alongside the main action-perception loop. He argues such "auxiliary forward modelling" (AFM) accounts import an unnecessary complication and that the unified active-inference-style architecture is both more parsimonious and more biologically plausible. This is theoretical support for SD-029's decision to abandon SD-003's dual-branch (factual vs counterfactual) comparator. Second, Lukitsch argues that the sense of agency is realised through the temporal structure of prediction-error minimisation: "SoA is realized through the temporal structure of prediction error minimization." Prospective (protentional) and retrospective agency signals are temporally integrated rather than sequentially computed.

## Mapping to SD-029

The first claim is straightforward support for SD-029's architectural direction. If biology implements agency through a unified forward model rather than a dual-branch comparator, then SD-029's choice to drop the counterfactual (cf_gap) branch in favour of a single-pass residual is the biologically correct simplification, not a pragmatic compromise. Lukitsch adds a philosophical warrant that Brown 2013 provides in active-inference terms.

The second claim introduces a caveat that the other papers in this pull do not surface. If agency experience emerges from temporally integrated error cancellation, rather than from any single step's residual, then SD-029's C2 and C3 criteria -- which evaluate the residual either on average or conditioned on specific approach-to-harm events -- may be operating at the wrong temporal scale. An event-conditioned window (C3) is already better than a step-averaged one, but Lukitsch's framing suggests that the residual's integrated time course over a trajectory, not its peak or mean, may be the biologically meaningful signal. This is worth flagging as a design consideration for V3-EXQ-433a reanalysis: compute the residual's integral or cumulative structure over the approach trajectory, not just its per-step or mean values.

## Caveats

Important ones. First, this is a philosophy-of-mind theoretical review in a frontiers-tier journal, not a primary empirical study or even a well-established computational model. The "integral forward model" framing is a useful conceptual redescription but does not yield quantitative predictions about what temporal window is correct, what the residual should look like, or what signatures to expect in data. Second, Lukitsch's argument is largely negative: it rejects competing accounts but does not provide a detailed positive implementation. For SD-029 this means the paper reinforces the architectural direction but does not help validate the specific V3 implementation.

## Confidence reasoning

Source quality is moderate. Frontiers in Psychology is peer-reviewed but with a more permissive editorial standard than top journals in the field; the paper is also very recent with no citation or replication track record yet. Mapping fidelity is moderate -- the single-mechanism forward-model argument maps well onto SD-029, but the temporal-integration argument adds structural complications the current SD-029 does not address. Transfer risk is low because the argument is framework-general. Aggregate 0.55, evidence_direction mixed rather than supports: the paper supports the architectural direction but suggests the current per-step or short-window C2/C3 readouts may be under-calibrated relative to the temporally integrated signal biology likely uses.
