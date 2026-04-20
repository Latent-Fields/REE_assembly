# Echoes of the brain within PCC (Leech, Braga & Sharp 2012)

## What the paper did

Leech and colleagues followed up their 2011 ventral/dorsal fractionation of PCC with a multivariate fMRI analysis designed to test whether PCC subregions echo multiple large-scale networks simultaneously. They combined GLM analysis of an attentionally demanding task with independent component analysis of resting-state PCC activity, then compared PCC subregion-level signatures against whole-brain functional networks identified independently.

## Key findings relevant to SD-032d

Within PCC, separable-but-overlapping subregions produced distinct connectivity signatures. A predominantly ventral PCC subregion coupled strongly with the rest of the DMN. Two subregions in dorsal PCC coupled with frontoparietal control networks. During the attentional task, these subregions modulated differently -- the dorsal subregions showed the load-dependent coupling with control networks that Leech 2011 had already documented. The authors frame PCC not as a homogeneous DMN node but as a cortical hub whose subregions each reflect activity from different large-scale systems, positioning PCC to integrate information across functionally distinct networks.

## How this translates to REE

SD-032d treats the PCC-analog as a network-level modulator rather than a within-network controller. Leech 2012 is direct support for that architectural framing. The paper's central claim -- PCC as a posterior hub whose subregions echo multiple networks -- matches the ree-v3 design in structure if not in output granularity. PCCAnalog currently reads multiple input streams (task-success EMA, drive_level via SD-012, steps-since-offline-phase) and integrates them into a single stability scalar fed to the SD-032a coordinator. The multi-input structure is Leech-compatible; the scalar output is a compression.

Two consequences for V3 experiments. First, the PCCAnalog design is correctly posterior-hub-shaped in topology -- it sits between multiple substrate signals and emits one modulator. Second, if V3-EXQ-447 shows the coordinator's behaviour is sensitive to the *composition* of the stability signal in a way pcc_stability's scalar output cannot represent (for example, if fatigue-driven stability and offline-recency-driven stability produce different downstream effects), Leech 2012 would predict a split into multiple output channels corresponding to the paper's multiple subregional signatures.

## Limitations and caveats

Leech 2012's core finding is *heterogeneity*. ree-v3 compresses that heterogeneity to one scalar on the reasonable grounds that the downstream consumer (MECH-259 threshold) reads only one scalar. But the paper does not license that compression -- in fact it predicts compressing multi-network PCC to one scalar loses information. This is an acknowledged simplification in the SD-032d spec. The empirical test in V3-EXQ-447 should probe whether PCCAnalog's scalar output is sufficient or whether differentiated stability channels are needed. The paper is human fMRI, so direct causal interpretation of PCC subregions as modulators of other networks is inferential, not demonstrated.

## Confidence reasoning

Source quality is strong (J Neurosci, replicated follow-up to Leech 2011). Mapping fidelity is moderate: the hub role is well supported, but the scalar compression is not licensed by the paper and the paper arguably predicts it is too coarse. Transfer risk is low -- PCC as multi-network hub is a widely replicated finding in subsequent connectivity literature. Confidence 0.75 -- supports the architectural premise of SD-032d while flagging an explicit tension with the scalar-output design choice.
