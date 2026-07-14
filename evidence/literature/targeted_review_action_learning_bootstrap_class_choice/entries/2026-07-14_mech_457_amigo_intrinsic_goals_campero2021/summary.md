# Learning with AMIGo: Adversarially Motivated Intrinsic Goals

**Class surveyed:** CURRICULUM / GOAL-GENERATION | **Evidence direction:** supports | **Confidence:** 0.8

**Source:** Andres Campero, Roberta Raileanu, Heinrich Kuttler et al. (2021). *Learning with AMIGo: Adversarially Motivated Intrinsic Goals.* ICLR 2021 (arXiv:2006.12122)

AMIGo pairs a goal-generating 'teacher' network with a goal-conditioned 'student' policy. The teacher is trained by a constructively-adversarial objective -- rewarded for proposing goals the student reaches in more than t* steps but penalised for goals never reached, with t* slowly increased -- so proposed goals sit at the moving frontier of the student's competence. This manufactures a dense, self-paced curriculum with no external reward and no expert.

The result that matters: on hard procedurally-generated MiniGrid tasks (KeyCorridor, ObstructedMaze) where sparse RL and count-based / RND-style intrinsic bonuses stay at floor, AMIGo solves them. This is the cleanest published case of an unsupervised, self-generated teaching signal reaching competence a plain novelty bonus cannot -- the closest analogue to REE's question 'what is the unsupervised route to what BC (32.72) achieved?'. BC injects the teaching signal from outside; the curriculum class generates the equivalent internally.

Critically for the duplication question, the goal-frontier signal is *competence-directed*, not density-directed: RND rewards state unfamiliarity (saturates once visited), AMIGo rewards reaching newly-achievable targets (adapts as the student improves). It composes with rather than duplicates REE's curiosity substrate -- curiosity says 'go somewhere new', the frontier says 'master something just-out-of-reach'.

Buildability is moderate: a small goal-proposer network plus conditioning the existing actor-critic on a goal embedding -- a training-regime change plus one lightweight add-on, no new world-model or memory. The main precondition/risk is that useful forage competence must be expressible as a reachable parameterized goal. Confidence 0.80.
