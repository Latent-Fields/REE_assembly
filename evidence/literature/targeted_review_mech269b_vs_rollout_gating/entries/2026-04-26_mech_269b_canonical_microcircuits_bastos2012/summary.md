# Bastos, Usrey, Adams, Mangun, Fries & Friston 2012 -- Canonical microcircuits for predictive coding

## What the paper did

Bastos and colleagues wrote a foundational *Neuron* review reconciling the established notion of a canonical six-layer cortical microcircuit with the contemporary view of cortex as a hierarchical Bayesian inference engine. They mapped specific neuronal populations (superficial pyramidal cells, deep pyramidal cells, spiny stellates, classes of interneurons) onto specific computational roles required by predictive-coding theory: superficial pyramidals as prediction-error reporters, deep pyramidals as prediction generators, modulatory inhibition as a substrate for the precision (gain) on prediction-error signals. The result is an architectural blueprint in which prediction-error signals ascend the cortical hierarchy multiplied by a precision factor that is itself encoded in post-synaptic gain and modulated by neuromodulators.

## Key findings relevant to MECH-269b

For MECH-269b the central finding is that the cortical column has a built-in mechanism for gating prediction-error contribution by a precision signal. In MECH-269b's language this is exactly the architectural primitive needed on the E1 and E2 side -- a per-circuit gain factor that determines whether a given prediction-error stream is strongly forwarded or muted. Bastos et al. argue this is encoded biologically by NMDA-receptor function, classical neuromodulator release, and the intrinsic balance of excitation and inhibition within the column. The mechanism is general -- it applies to any cortical region implementing predictive coding -- which means E1 (sensory predictor) and E2 (transition model), both being cortical-analog modules in REE, inherit the same primitive.

Crucially, the paper supplies tag (c) inferential support for MECH-269b. It does not measure per-stream precision specifically, but it establishes that the cortex is wired to host stream-specific precision modulation if streams correspond to anatomically separable circuits. The MECH-269b assumption that V_s is per-stream rather than per-region is consistent with their framework.

## How the findings translate to REE

The translation is straightforward at the architectural level. REE inherits the canonical-microcircuit substrate as the implementation of MECH-269b's cortex-side gating. The V_s signal acts as the precision parameter that the cortical column already knows how to consume. For the per-stream specialisation, REE assumes that z_world, z_self, z_harm_s, z_harm_a, z_goal correspond to anatomically separable cortical territories (visual cortex, somatosensory cortex, anterior insula / dACC, etc.), each of which can carry its own precision signal. Bastos et al. supply the local primitive; REE specialises it across the inter-territory level.

## Limitations and caveats

Two caveats. First, the paper argues at the column level and does not directly demonstrate per-stream precision modulation -- the assumption that distinct content-streams (visual prediction error vs interoceptive prediction error vs proprioceptive prediction error) can each have their own gain factor is consistent with the framework but is not itself measured. Second, and more important for MECH-269b, the paper makes no claim about hippocampal proposer dynamics. The symmetric-application question -- does the same V_s signal that gates hippocampal anchor selection also gate cortical forward-prediction contribution? -- is not addressed at all here. This is genuinely a gap, not a contradiction. The cortex side is supported; the symmetric application is silent.

## Confidence reasoning

Confidence 0.72 -- supports MECH-269b at the architectural level. Source quality very high (peer-reviewed, top-tier neuroscience journal, senior authors). Mapping fidelity moderate because the paper supplies the architectural primitive but not the per-stream or symmetric-application specialisations MECH-269b requires. Transfer risk modest because the canonical-microcircuit account is broadly applied across cortical regions, including those that would house E1 and E2.
