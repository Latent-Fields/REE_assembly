# Aton et al. (2013) — Visual experience and subsequent sleep induce sequential plastic changes in inhibitory and excitatory cortical neurons

*According to PubMed. Proc Natl Acad Sci U S A 110(8):3101-6. [DOI](https://doi.org/10.1073/pnas.1208093110) · PMID 23300282 · PMC3581875. (Note: the claims.yaml anchor cited page 3059; the verified citation is 110(8):3101-6.)*

## What the paper did

Aton and colleagues recorded continuously from cat visual cortex — fast-spiking interneurons and putative principal neurons — straight through a period of waking monocular deprivation and the sleep that followed. They saw a two-act structure. In waking, deprivation depressed the fast-spiking interneurons and shifted their ocular bias: the *instruction*. But the ocular-dominance shift in the principal neurons did not appear then. It appeared only after subsequent non-REM sleep, during which principal-neuron firing rose and became phase-locked to slow-wave and spindle oscillations: the *execution*. The size of the final shift was proportional both to the waking interneuron changes and to the sleep-associated principal-neuron changes. Two gates, in order: waking instructs, sleep crystallizes.

## Why it matters for MECH-334 and INV-074

This is the entry that earns two claim tags, and it earns them honestly. For MECH-334, it supplies the *execution timing*: crystallization is sleep-gated. That is not a decorative detail — MECH-334 already declares dependencies on MECH-120 (sleep SWY downscaling) and MECH-165 (replay diversity), and Aton et al. are the in-vivo demonstration that the consolidation actually happens during the sleep phase, not during the waking experience that instructs it. For INV-074, the paper supplies the *ordering constraint*: corrupted waking dynamics prevent sleep from crystallizing the right representation. In other words, MECH-334 cannot rescue a diversity distribution that was never competitively established during the MECH-333 open window. That makes the two claims jointly falsifiable — a property worth having, because it means a single well-designed experiment can speak to both.

## Limitations and the honest caveat

The phenomenon is ocular-dominance plasticity in cat visual cortex; REE's analogue is an offline consolidation phase locking in a diversity distribution. What transfers is the abstract two-step sequence — competitive instruction in the active phase, crystallization in a subsequent offline phase — not fast-spiking-interneuron physiology or cortical spindle oscillations. I have logged the two consequential constraints as failure signatures because they are prescriptive, not descriptive: (1) if REE attempts to crystallize the diversity distribution during the active phase with no subsequent consolidation step, it is not implementing this biology and MECH-334 would be mis-built; (2) if the open-window instruction is wrong, no amount of closure machinery saves it — which couples MECH-334's success to INV-074's necessity condition and is exactly the kind of coupling governance should want made explicit.

## Confidence

0.82, `supports`. Source quality is high (PNAS; Frank lab; careful continuous in-vivo recording). Mapping fidelity is good for the temporal-ordering structure that the REE sleep dependencies need, discounted by the cat-visual-cortex-to-REE-consolidation abstraction. Its real value in this folder is not redundancy with the molecular-lock papers but the missing piece they do not address: *when* crystallization happens, and *what must already be true* for it to work.
