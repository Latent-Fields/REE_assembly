# Karlsson & Frank (2009) — Awake Remote Replay: The Quiescent Reactivation Substrate for MECH-092

**Claims tested:** MECH-092, ARC-007
**Evidence direction:** supports | **Confidence:** 0.82

---

## What the paper did

Karlsson and Frank recorded from CA1 tetrode arrays in rats navigating a two-environment paradigm: a familiar track and a remote track the rat had visited earlier in the day. The key question was whether hippocampal SWR-associated replay during awake quiescence is restricted to the current environment, or whether it can access stored representations from spatially remote, recently-experienced environments.

The answer was unambiguous. During brief pauses in waking behavior — the awake quiescent states associated with sharp-wave ripples — CA1 ensembles replayed sequential place cell activity from both the current environment and from remote environments visited earlier in the session. Remote replay was as frequent as local replay, and critically, it was stronger after periods of recent movement than after extended quiescence. This last detail matters: remote replay is not simply background noise during rest; it is triggered by the transition into quiescence following active navigation.

## Key findings for MECH-092

MECH-092 claims that quiescent E3 heartbeat cycles trigger hippocampal SWR-equivalent replay for viability map consolidation — specifically, that the replay is not restricted to what the agent is currently doing, but accesses the broader stored trajectory library. Karlsson & Frank provide the canonical empirical support:

1. **SWR replay during awake quiescence accesses remote stored trajectories** — not just the currently active context. The viability map can be replayed from stored locations outside the current state, which is precisely what MECH-092 requires for consolidation functions that compare and integrate trajectories across time and context.

2. **Quiescent replay is triggered by the offset of movement** — suggesting that the hippocampus uses the brief rest periods that naturally occur during navigation (and in REE, after commitment events) to initiate replay. This is consistent with MECH-092's specification that quiescent E3 heartbeat cycles, which occur at commitment boundaries and during post-action rest, serve as the consolidation trigger.

3. **Remote replay is structured and sequential** — it is not random noise but coherent sequential reactivation. This confirms that what is being replayed is trajectory information, not just place cell activation, consistent with ARC-007's specification that hippocampus stores and replays path traces.

## REE translation: the remote access property

For REE's multi-session learning, the remote access property is critical. An agent that can only consolidate the current context's trajectories during rest would have severely limited integration across episodes. The Karlsson finding establishes that the quiescent replay mechanism reaches into the trajectory library — it can consolidate spatially distant trajectories that were experienced earlier in the session. In REE terms: a quiescent heartbeat cycle at position A can replay trajectory segments from position B, permitting integration of viability map information that was encoded at different times and locations. This supports the architecture of MECH-092 where rest-triggered replay performs offline integration across the full viability map, not just local updates.

The finding that remote replay is most robust after recent movement also matches REE's design: the completion of an active navigation episode (commitment + execution) is the natural trigger for the quiescent cycle that initiates consolidation.

## Limitations

Rodent spatial paradigm; "remote" means spatially remote environments, not abstractly or semantically remote trajectories. The mapping to REE's abstract viability map (which operates in z_world action-consequence space rather than physical space) requires inference about what the non-spatial analogue of the CA1 sequential replay would look like. The paper does not directly test whether remote replay drives consolidation of the remote-environment representation (only that it occurs); the functional consequence for long-term memory requires integration with Wilson & McNaughton (1994) and subsequent consolidation literature. MECH-094 (the hypothesis tag that prevents replay from producing residue) is not addressed here.
