# Literature Summary: 2026-04-04_mech060_forward_model_simulation_wolpert1998

## Claims Tested

- `MECH-060`

## Source

- Wolpert DM, Miall RC, Kawato M (1998), *Internal models in the cerebellum*. Trends in Cognitive Sciences 2(9): 338-347.
- DOI: 10.1016/S1364-6613(98)01221-2
- URL: https://pubmed.ncbi.nlm.nih.gov/21227230/

## Mapping to REE

MECH-060's pre-commit simulation channel requires a computational substrate that generates expected harm from candidate actions before those actions execute -- a forward model operating on efference copy rather than on realized sensory feedback. Wolpert, Miall and Kawato (1998) provide the theoretical framework that makes this biologically coherent.

The key distinction in their framework is between forward internal models (which take a motor command as input and predict the resulting sensory state) and inverse models (which invert this mapping to generate commands). The forward model operates on an efference copy of the intended motor command: the cerebellum receives the motor command, generates a predicted sensory consequence, and this prediction is used to cancel the expected reafference before actual sensory feedback arrives. This temporal advance -- prediction before execution, error correction after feedback -- is structurally isomorphic to REE's pre-commit/post-commit channel separation.

In REE's architecture, E2 plays the role of the forward model: it operates on the intended action (efference copy) and the current latent state to generate predicted harm across a rollout horizon, before env.step() commits the action. The actual harm returned by env.step() is the realized error, the cerebellar equivalent of true sensory feedback correcting the forward model's prediction. The write-locus boundary in MECH-060 -- where only post-commit harm updates the durable residue field -- corresponds to the functional separation between reafference cancellation (ephemeral, pre-motor) and adaptive updating (persistent, post-movement).

The cerebellum's anatomical isolation from structures responsible for durable memory consolidation -- with the cerebellar prediction loop operating on a timescale of tens of milliseconds and not writing to cortical long-term stores -- is a biological instance of the write-boundary enforcement MECH-060 requires. Pre-motor predictions are used but not consolidated; post-movement errors drive adaptation.

## Caveats and Mapping Limits

- The paper addresses motor control, not harm attribution or moral responsibility. The conceptual mapping to REE's ethical accountability framing is inferential.
- The cerebellum/cortex distinction provides a neural analogy for the write boundary, but the analogy does not transfer cleanly to agent learning systems.
- This is a foundational theoretical review, not an experiment testing the consequence of contaminating the two channels.

## Direction and Confidence

- `evidence_direction`: `supports`
- `confidence`: `0.75`
- Rationale: canonical theoretical grounding for the simulation-vs-realized-outcome channel distinction, with clear cerebellar substrate; does not test write-boundary enforcement or contamination consequences in any REE-relevant sense.
