# Adams, Stephan, Brown, Frith & Friston 2013 -- The computational anatomy of psychosis

## What the paper did

Adams and colleagues unified a heterogeneous set of psychotic symptoms -- hallucinosis, delusions, sensory-attenuation deficits, abnormal smooth-pursuit eye movements, catatonia -- as expressions of a single computational pathology: aberrant encoding of precision. Within the predictive-coding framework, precision is the inverse variance attached to prediction errors and prior beliefs, biologically encoded by post-synaptic gain and modulated by NMDA-receptor function and dopaminergic neuromodulation. When precision is mis-set, behaviours that depend on revising priors in light of incoming evidence fail in characteristic ways. The paper ran simulations of perceptual synthesis, smooth pursuit, and agency attribution under the precision-pathology assumption and reproduced features of the corresponding psychopathologies.

## Key findings relevant to MECH-269b

Adams et al. supply the failure-mode prediction that grounds MECH-269b architectural-prediction half. MECH-269b parent claim warns that without V_s gating on E1 / E2 rollouts, downstream consumers receive stale-but-confident-looking prediction errors which suppress behavioural revision and produce wired-but-inert failure modes. This is exactly the clinical phenotype Adams et al. describe under aberrant precision: precision is mis-set, prediction errors are computed but mis-weighted, and the system fails to revise its beliefs even when contradicting evidence accumulates. The architectural claim that precision is the relevant gating signal is therefore corroborated indirectly: the predictive-coding framework failure modes are observed clinically and look like MECH-269b predicted failure modes.

This is tag (c) inferential support plus tag (d) failure-mode evidence -- the support is at the framework level rather than from direct measurement.

## How the findings translate to REE

REE wired-but-inert hypothesis -- that V_s gating is necessary on E1 / E2 because without it the cortical consumers are mis-weighted in characteristic ways -- inherits the Adams et al. clinical-correspondence argument. The same logic that explains psychosis as aberrant precision predicts that an REE substrate without V_s gating on cortical rollouts will exhibit psychosis-analog behaviours: confident-but-stale predictions, over-strong sensory priors leading to perceptual confabulation, failures of behavioural revision in the face of accumulating contrary evidence.

## Limitations and caveats

Three caveats. First, the paper does not directly measure per-stream precision in psychosis -- the support is framework-level, predicting that mis-set precision produces specific failure modes. Second, the symmetric-application question (does the same precision parameter that mis-fires in psychosis also mis-fire in hippocampal anchor selection?) is not engaged. Hippocampus appears briefly in the context of pattern completion but the symmetric-V_s claim is not addressed. Third, clinical mapping is heterogeneous: the precision-weighting account competes with dopamine-signal-to-noise and aberrant-salience accounts, and not all psychotic patients fit the precision profile.

## Confidence reasoning

Confidence 0.66 -- supports MECH-269b at the framework level and supplies the failure-mode prediction that matches MECH-269b wired-but-inert warning. Source quality good (peer-reviewed clinical-computational synthesis with senior authorship). Mapping fidelity moderate because the support is indirect -- a failure-mode prediction backing an architectural claim. Transfer risk noticeable because clinical psychosis is heterogeneous and the precision account is one of several competing frameworks. The supportive force is in the structural correspondence between MECH-269b failure prediction and the clinical phenotype Adams et al. describe.
