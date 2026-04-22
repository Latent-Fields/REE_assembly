# Stalnaker, Cooch & Schoenbaum 2015 -- What the Orbitofrontal Cortex Does Not Do

According to PubMed ([DOI](https://doi.org/10.1038/nn.3982)).

## What the paper does

Stalnaker, Cooch, and Schoenbaum -- the last of whom co-authored Wilson2014 -- wrote this critical review essentially as a corrective to OFC's expanding empire. The OFC literature has grown from one paper a month in 1987 to fifty a month at the time of writing, and the authors argue that this expansion has been driven less by new evidence than by the field's habit of attributing whatever new cognitive function is fashionable to whichever brain area is being recorded. The paper systematically walks through claims about OFC's role in inhibition, reversal learning, conflict monitoring, emotion regulation, and value comparison, and shows that for most of these the supporting data are thinner than the prevailing consensus implies, that competing brain regions perform the function equally well, or that contradictory findings have been quietly ignored. What the authors *do* defend, narrowly, is OFC's role in model-based valuation that depends on inferred state information -- the construct from Wilson2014.

## Why it matters for V_s invalidation

This is the boundary-condition paper for our OFC-as-V_s-substrate mapping. Wilson2014 argued that OFC labels the current task state and that this label gates downstream RL. Stalnaker2015 says: yes, but do not extend that beyond the inferred-state role. That constraint matters for MECH-284. If V_s is generic schema validity, OFC is the wrong substrate -- many other regions track many other kinds of schema. If V_s is specifically the inferred-state label that gates downstream value learning, OFC is the right substrate. Our architecture must commit to one of these readings before the OFC mapping can be defended seriously.

The architectural implication is non-trivial. MECH-284 should accumulate violations relevant to the inferred-state representation -- not violations of every prediction the agent makes. A violation of E1's sensory prediction does not necessarily belong in MECH-284's accumulator; only a violation that bears on whether the currently labelled state is the right state does. This narrows MECH-284 considerably. It also suggests that V_s as a single scalar may be the wrong abstraction -- the brain probably maintains separate validity signals for separate kinds of schema (sensory model, regional dynamics, social context, body schema), each tied to a different substrate.

## What the paper does not do

It is a critique, not a new empirical result. It does not generate new evidence for V_s; it sharpens what the V_s = OFC claim must defend. Treat it as a constraint paper, weight it lower than Wilson2014, but include it in the synthesis because the constraint is load-bearing.

## Clinical resonance

The clinical reading inherits the constraint. Bechara-Damasio gambling-task patients show OFC-specific deficits in updating *inferred* outcome contingencies, not in updating any kind of expectation. That is consistent with the Stalnaker reading. It also predicts that catatonia subtype II's anchor lock-in -- if OFC-mediated -- should specifically affect inferred-state updating, not raw sensory updating. That distinction would be testable.

## Confidence reasoning

Source quality high (Nat Neurosci, senior authors who co-authored the positive paper they are constraining). Mapping fidelity moderate (0.60) because the paper's value is in narrowing not supporting. Direction is mixed because it narrows Wilson2014. Aggregate 0.65.
