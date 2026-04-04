# Jadhav et al. 2012 — Awake Hippocampal SWRs Are Causally Required for Spatial Memory

**Source:** Jadhav SP, Kemere C, German PW, Frank LM. "Awake hippocampal sharp-wave ripples support spatial memory." *Science* 336(6087):1454-8, 2012. DOI: [10.1126/science.1217230](https://doi.org/10.1126/science.1217230)

**Claims evidenced:** MECH-092, MECH-121

---

## What the paper did

The Frank laboratory implemented a closed-loop system to detect and interrupt awake hippocampal sharp-wave ripples (SWRs) in real time as rats learned a spatial alternation task on a W-maze. Each time a SWR was detected during inter-trajectory pauses, a brief electrical stimulation was delivered to CA1, disrupting the SWR event. A sham stimulation control group received equivalent stimulation uncoupled from SWR events. This causal design allowed the researchers to test whether awake SWRs are necessary for memory-guided decision making, beyond their correlational relationship to replay activity.

## Key findings relevant to REE

SWR interruption produced a persistent learning deficit throughout training -- not just during the early consolidation window. The deficit was specific to the SWR-dependent memory function: place field activity (the spatial map itself) was not impaired by SWR interruption, and post-experience sleep SWR reactivation was also intact. The learning failure was therefore not due to disrupted encoding of the spatial environment but to disrupted use of the encoded map to guide choices.

This is a critical distinction: the map forms but cannot be accessed for decision-making. The hippocampus stores spatial information; awake SWRs are the retrieval mechanism that makes that information available to guide ongoing behaviour.

## Translation to REE

MECH-092 posits that quiescent E3 heartbeat cycles trigger SWR-equivalent replay for viability map consolidation. The Jadhav result establishes the causal necessity of this mechanism: it is not merely that hippocampal replay correlates with good memory performance; disrupting replay specifically prevents memory-guided decision making. For REE, this means that the quiescent replay during inter-episode pauses is a required function of the HippocampalModule, not an optional background process. An agent lacking MECH-092 would accumulate a viability map in E3 but fail to make that map available to guide action selection -- accumulating terrain representations that never become operational.

MECH-121 (NREM SWR replay for episodic-to-semantic transfer) is supported more indirectly: the paper establishes that hippocampal SWR function is causally necessary for memory, which is the prerequisite for any claim about what sleep-phase SWRs specifically accomplish. If awake SWRs can be disrupted to produce learning failure, then sleep-phase SWR content should similarly matter for what gets consolidated into E1's world model.

The finding that place field activity is preserved despite SWR interruption is architecturally important for REE: z_world encoding (E1/E3 terrain representation) and viability map access (hippocampal SWR-gated retrieval) are dissociable. Disrupting MECH-092 would not corrupt the latent world model -- it would prevent its operational deployment for planning.

## Limitations and caveats

The interruption is nonselective -- all SWRs are disrupted regardless of their content. Whether specific trajectory replays are necessary (e.g., forward vs reverse, goal-directed vs exploratory) cannot be assessed from this paradigm. The Jadhav paper also confounds awake and sleep-phase SWR functions slightly: by disrupting only awake SWRs, it leaves sleep SWRs intact, showing that awake SWRs have an independent function. This means the paper supports MECH-092 specifically (awake quiescent replay), not the full MECH-121 sleep-phase pipeline.

## Confidence reasoning

Confidence 0.87 -- high for MECH-092 specifically, moderate for MECH-121 indirectly. Exceptional source quality (Science, causal closed-loop design). The mapping to MECH-092 is direct; MECH-121 requires an additional inferential step from awake SWR necessity to sleep-phase SWR consolidation.
