# De Preter & Heinricher (2024): The 'In's and Out's' of Descending Pain Modulation from the Rostral Ventromedial Medulla

*Trends in Neurosciences* 47(6), 447-460. DOI: 10.1016/j.tins.2024.04.006  
*(Cross-filed from targeted_review_connectome_mech_256; different mapping emphasis for SD-021)*

## What the paper did

De Preter and Heinricher (Oregon Health & Science University) reviewed the current understanding of the rostral ventromedial medulla (RVM) as the key output node of the descending pain-modulatory circuit. The RVM receives input from the periaqueductal gray (PAG) -- which in turn receives cortical projections from ACC/pgACC and prefrontal cortex encoding motivational state -- as well as ascending nociceptive signals from the spinal cord. Two functionally defined cell classes control dorsal horn pain transmission: OFF-cells (disinhibited in analgesic/committed states, antinociceptive) and ON-cells (activated in hyperalgesic states, pronociceptive). The review summarises input circuitry, molecular cell-type identification challenges, and the role of each population in persistent pain states.

## Key findings relevant to SD-021

This paper directly characterises the biological circuit that SD-021 posits as its substrate. SD-021 states that when E3 is committed to a trajectory through expected harm, z_harm_s PE precision is reduced via a descending modulatory pathway. The De Preter & Heinricher review identifies this as the pgACC -> PAG -> RVM cascade: when the agent is motivationally committed to traversing harm (ACC/pgACC activates PAG), RVM OFF-cells fire and ON-cells are suppressed, reducing dorsal horn nociceptive transmission.

Two features of the circuit are particularly important for SD-021's implementation. First, the modulation is graded and context-sensitive, not binary -- supporting the SD-021 specification of a graded attenuation factor (0 < alpha_descending < 1) rather than a hard switch. Second, the system involves both opioid and endocannabinoid pathways (consistent with the Hohmann 2005 implementation constraint already in this corpus): the harm_s_gain function should not be modelled as a single mu-opioid mechanism.

## Mapping to SD-021 and MECH-332

For SD-021, this paper provides the mechanistic substrate description that the earlier lit entries (Tracey & Mantyh 2007, Crawford 2021, Petrovic 2002) approached through imaging and pharmacology. The Heinricher lab's electrophysiology directly characterises the ON/OFF cell firing dynamics that implement SD-021's gain control.

For MECH-332 (registered 2026-05-17), this paper establishes the key dissociation insight: the PAG/RVM implements SD-021's commitment-gated precision suppression via behavioral-state gating (motivational/emotional ACC input), which is mechanistically distinct from the efference-copy comparator of MECH-256 (motor command -> spinal/cortical forward-model subtraction). The two pathways have different anatomical substrates, different trigger conditions, and different temporal granularities. See the companion entry in targeted_review_connectome_mech_256 for the MECH-256-facing mapping (where the same paper's evidence direction is mixed rather than supports, because from MECH-256's perspective the finding constrains WHERE the efference-copy mechanism is implemented, not WHETHER it exists).

## Caveats

The molecular identification challenge highlighted by the authors -- functional ON/OFF classes are not yet cleanly alignable with molecular markers -- introduces uncertainty into the implementation model. SD-021's current binary committed/uncommitted gate may be an oversimplification of a more graded, cell-type-heterogeneous system. The paper's primary evidence is rodent, with human imaging corroboration limited to BOLD correlates.

## Confidence reasoning

Source quality is high (Heinricher lab canonical authority, *Trends in Neurosciences*). Mapping fidelity is stronger here (0.80) than in the MECH-256 cross-file entry (0.65) because the paper's core message -- PAG/RVM implements motivational-state-gated nociceptive gain control -- maps directly onto SD-021's substrate claim. Transfer risk is low. Aggregate 0.82.
