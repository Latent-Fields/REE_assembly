# Summary: Botvinick et al. (2019) — Reinforcement Learning, Fast and Slow

**Entry:** 2026-03-30_arc_018_mech_033_rl_fast_slow_botvinick2019
**Claims tested:** ARC-018, MECH-033, ARC-007
**Evidence direction:** supports | **Confidence:** 0.80

---

Botvinick and colleagues' 2019 Trends in Cognitive Sciences paper is best understood as the DeepMind synthesis of everything the field had learned about fast and slow learning in AI systems, written through the lens of neuroscience. It brings together three threads: classical CLS theory (McClelland 1995, Kumaran 2016), episodic RL (Lengyel & Dayan 2008), and meta-RL (Wang et al. 2018). The result is a unified framework that is directly applicable to REE's hybrid architecture.

The fast/slow distinction maps cleanly onto REE. Slow learning corresponds to E1 (LSTM world model, trained via gradient descent over many episodes) and E3's harm terrain prior (accumulated over the full training history). Fast learning corresponds to HippocampalModule: specific harm trajectories bound in one or a few exposures, available for immediate retrieval. The paper argues that these systems are not alternatives — they are complementary in the strict CLS sense: each does something the other cannot. Slow learning discovers structure; fast learning captures specifics. REE's architecture implements both.

The episodic RL thread extends Lengyel & Dayan in a way that matters for ARC-007 and ARC-018. Botvinick et al. note that episodic RL does not merely retrieve stored outcomes — it can combine stored episodes in novel ways to support generalization. A stored episode of "turn left near the red marker" and another of "red markers co-occur with hazards" can be combined to produce "avoid left turns near red markers" even if this specific combination was never experienced. This is the hippocampal generalization that Kumaran 2016 described; Botvinick et al. show it can be implemented in practice in deep RL systems. For ARC-007, this means the hippocampal path memory is not a static lookup but a generative store — it can propose novel safe trajectories by compositing fragments of stored safe paths.

The meta-RL thread is more speculative for REE but worth noting. The meta-RL agent (implemented as an LSTM trained across diverse tasks) develops an internal RL algorithm in its recurrent activations. Applied to REE: E3's LSTM, trained across multiple harm configurations, could develop an internal bias toward harm-avoidant behavior that operates faster than the explicit terrain-prior updates. This would make E3 simultaneously a slow-trained explicit terrain reasoner (what the current V3 implementation implements) and a fast-adapting implicit harm avoider (what meta-RL would add). The meta-RL benefit requires diverse task training — which is not guaranteed in REE's current setup.

The paper's honest admission about limits is worth flagging for governance: it notes that the combination of episodic RL and meta-RL creates a system that is "extremely efficient" early in learning but has not been shown to achieve human-level sample efficiency in complex domains. REE's comparable challenge is whether the HippocampalModule provides meaningful planning efficiency gains over E3 acting alone in the CausalGridWorld environment — a question that ARC-018's experiments (EXQ-172 FAIL at low E2 fidelity) are directly probing.

Confidence is 0.80: modern, directly applicable, well-grounded, with a real caveat around meta-RL applicability to REE's training regime.
