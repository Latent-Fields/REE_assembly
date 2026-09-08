# Choi et al. 2019 -- an agent that works out which pixels are itself

Train a small attention model to do nothing but guess which action was taken between two frames, and it learns to look at the character. Nobody told it where the agent was. The controllable part of the world falls out of the task of predicting one's own action, which is a plausible artificial cousin of the cricket's corollary discharge: the system learns which changes are its own. Give that discovered variable to an exploration bonus and Montezuma's Revenge, the standing embarrassment of sparse-reward RL at the time, becomes tractable without demonstrations.

Why this entry rather than a dozen others from the artificial-agents literature: it is the only one this pull found that meets both of GOV-CONTRACT-1's tests for that domain. The variable emerges without being specified, and the agent lacking it fails in the way MECH-545 predicts for an agency lesion, poor action learning. Most of the rest of the domain, including the object-slot, provenance-buffer and uncertainty-ensemble results recorded in the synthesis, shows ablation of a hand-installed bias, which is the weaker half of the test.

The confound is honest and structural. Controllability here is defined relative to a discrete action set, that is, relative to a body. So the embodied reading, that the variable recurs because agents have effectors, is not ruled out by a result that requires effectors to state it. And the emergent-communication literature (Chaabouni et al. 2020; Lipinski et al. 2023) warns that task pressure alone does not reliably force a separately encoded relation into a channel, so emergence in one architecture is not evidence that any unified system must carry it.

Confidence 0.6. Motivation only.
