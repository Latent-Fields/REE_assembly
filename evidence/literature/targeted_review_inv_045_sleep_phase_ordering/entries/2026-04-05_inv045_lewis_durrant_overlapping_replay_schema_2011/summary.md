# Lewis & Durrant 2011 -- Overlapping memory replay during sleep builds cognitive schemata

**Evidence direction: mixed**

## What the paper claims

Sleep consolidation drives schema formation through the overlapping replay of related memories. When two memories share elements (e.g., two episodes that both involve a specific object or location), Hebbian learning during NREM replay strengthens their shared components and allows a more abstract, generalised representation to form in neocortex. During subsequent REM sleep, this cortical abstraction is replayed alongside older cortical knowledge, enabling the new schema to be integrated into existing long-term knowledge structures. Repeated NREM-REM cycles progressively increase the level of abstraction.

## Does it make the full derivation argument?

No -- but this is the closest paper found to making the ordering constraint explicit. The functional dependency is described: REM integration requires that NREM-derived abstract cortical representations already exist. If REM ran first, the cortical targets for integration would not yet contain the Hebbian-abstracted schema from overlapping replay -- there would be nothing new to integrate. This is a functional ordering dependency, not merely a description of what each phase does. However, Lewis and Durrant do not frame this as a derivation from first principles. They do not state: "REM-before-NREM would fail because...". The implication is there; the proof is not.

## Relevance to INV-045

The most directly relevant paper found. Lewis and Durrant's account maps onto INV-045 Phases 2-3: Phase 2 (NREM schema replay with diversity) creates the Hebbian abstraction that is Phase 3's input (ThetaBuffer / spindle coordination transfers these cortical patterns into the hippocampal attribution map). The functional dependency between NREM-first and REM-second is implicit in the model: REM integration cannot add new schema to the existing knowledge structure if the new schema hasn't been formed yet (Phase 2 is a prerequisite for Phase 3/4). The paper also independently supports MECH-165 (replay diversity): it is the overlapping replay of multiple related episodes, not repetition of the dominant episode, that drives schema formation. This is the Hebbian diversity argument.

## Key gap for INV-045

The paper makes the ordering dependency implicit but never derives it. No papers have built on Lewis and Durrant to formalise the dependency as a computational proof: "REM-before-NREM would produce qualitatively different (incorrect) behaviour because [reason]." This formalisation step is what INV-045 claims to provide from an engineering-necessity perspective, and the biological literature has not done it.
