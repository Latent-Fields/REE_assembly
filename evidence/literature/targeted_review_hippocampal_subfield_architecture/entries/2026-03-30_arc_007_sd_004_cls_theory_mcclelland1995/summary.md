# Summary: McClelland, McNaughton & O'Reilly (1995) — Complementary Learning Systems

**Entry:** 2026-03-30_arc_007_sd_004_cls_theory_mcclelland1995
**Claims tested:** ARC-007, SD-004
**Evidence direction:** supports | **Confidence:** 0.82

---

The McClelland, McNaughton and O'Reilly (1995) paper is the theoretical bedrock for REE's entire hippocampal architecture. The argument it makes is not about a specific mechanism but about a structural necessity: any learning system that must both acquire new experiences rapidly and retain structured knowledge across many experiences *must* have two components. A single network learning new episodes rapidly will undergo catastrophic interference — the weight changes required to store the new episode will overwrite existing structured representations. The only solution is a fast-binding store (hippocampus) that acquires episodes one-shot, combined with a slow-integrating store (neocortex) that accumulates knowledge through gradual, interleaved replay of hippocampal memories.

This argument is powerful because it does not depend on any particular empirical detail. It follows from the mathematics of gradient-descent learning in connectionist systems. The empirical evidence assembled in support — HM's anterograde amnesia, the time-limited retrograde gradient, the preserved semantic memory in hippocampal patients — is compelling but secondary. The argument would stand even if we only had the mathematical analysis. For REE, this means the separation of HippocampalModule from E1 is not a design choice but a computational necessity: an agent that needs to learn new harm trajectories rapidly without corrupting E1's slow-built world model *must* have something like a hippocampal fast-binding store.

The implications for ARC-007 are direct. Hippocampal storage of paths through residue-field terrain is the specific instance of fast binding that REE requires: each harm-involving trajectory is an episode that must be stored rapidly (the agent cannot wait for interleaved gradient descent to encode it) and later replayed to update E3's harm terrain model (the neocortical equivalent). ARC-007's claim that hippocampal systems store and replay paths is simply the REE-specific instantiation of CLS theory.

The SD-004 connection is less direct but important. CLS theory says the hippocampus stores *episodes* — specific indexed instances. SD-004 says the REE hippocampus stores action-object representations as the backbone of its map. These are consistent: the choice of action-objects as the indexed format is a downstream design decision about *what kind* of episode gets stored. CLS theory is silent on this format question, but it licenses the general claim that hippocampal storage is episode-indexed rather than feature-averaged. The action-object format is the REE answer to: what is the right episode type for a planning agent operating in harm terrain?

The main caveat is that subsequent work (Tse et al. 2007) has shown neocortical learning can be rapid for schema-consistent information. This weakens the hard boundary between fast (hippocampal) and slow (neocortical) learning, and has implications for REE: E1 may be able to rapidly encode certain harm patterns if they are consistent with its existing world model. The REE architecture currently treats E1 as purely slow; this may need refinement.

Confidence is 0.82: foundational, domain-general, high mapping fidelity to the architectural separation REE requires. The main caveat is the schema-consistent rapid neocortical learning finding.
