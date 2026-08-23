# Reinforcement learning and episodic memory: an integrative framework (Gershman & Daw, 2017)

**Claim tested:** Q-095 — does explicit coordinated episodic organisation add capability
beyond REE's existing trajectory-generation account?
**Direction: supports**, confidence 0.70. This entry's contribution is that it states the
capability hypothesis in the currency Q-095 asks for, and tells you which regimes to look in.

## What the paper argues

Gershman and Daw open with an observation about the field rather than about the brain: RL
theory made its progress on simple tasks, and the simplicity of those tasks hides properties
that dominate real learning. State spaces are high-dimensional, continuous and partially
observable. Data are therefore sparse — precisely the same situation may never be encountered
twice. And rewards depend on long-term consequences in ways that break the assumptions making
RL tractable.

They then note a second problem that looks unrelated and argue that it is not. Theories of RL
have leaned almost entirely on procedural and semantic memory: knowledge about action values
or world models, extracted gradually across many experiences. That leaves out episodic memory
— traces of individual events — entirely.

Their proposal is that the second gap explains the first. Endowing an RL system with episodic
memory buys three things: efficient approximation of value functions over complex state
spaces, learning from very little data, and bridging long-term dependencies between actions
and rewards.

## Why this is the right currency for Q-095

Q-095's `what_would_answer` is explicit that the comparison must be scored on downstream
generalisation and discrimination rather than on any internal representational statistic. That
constraint is easy to state and easy to quietly violate, because internal statistics are so
much cheaper to measure — and the whole MECH-495 lineage exists partly because a
representational statistic (the `slot_cosine_sim` family) turned out to have been both
computed wrongly and pointed at the wrong quantity.

This review supplies three candidate dependent variables that are unambiguously behavioural:
sample efficiency, performance under partial observability, and long-horizon credit
assignment. None of them can be gamed by a representation that merely looks better organised.

It also identifies the regime in which to look, which is the more practically useful
contribution and the one most likely to be forgotten. The advantage episodic memory confers is
not universal — it is concentrated where data are sparse, state is high-dimensional or
partially observable, and reward is delayed. A Q-095 test run in a dense-data, low-dimensional,
short-horizon environment can return a clean null for regime reasons that have nothing to do
with the question, and reading that null as resolving toward reinterpretation would be a
straightforward error. Related: the effect this literature predicts lives in the *learning
curve*, not its endpoint, so scoring an arm on asymptotic performance alone will miss it.

## The scope gap, which is the reason confidence is 0.70

This is the part to be careful about, because the paper is easy to over-claim.

Gershman and Daw argue for episodic memory as an *instance-based retrieval store* — remember
specific past experiences, use them to evaluate current options. Q-095 asks about something
considerably larger: whether binding, segmentation, separation, completion, indexing and
remapping constitute one coordinated organising principle. The review supports the weaker
proposition and is silent on the stronger one. Having an episodic store earns its keep; that
tells you nothing about whether the six capabilities are one thing.

And there is a sharper version of the problem, which cuts against counting this entry too
heavily. If REE's existing trajectory-generation account *already* retrieves individual past
experiences — and it plausibly does — then this paper's capability argument is already
discharged by the architecture REE has. In that case it supports nothing whatever about the
additional coordinated principle, and counting it as support for Q-095's ADDS-CAPABILITY horn
would be double-counting an advantage REE has already banked. The two must be scored
separately: does an episodic store help (probably, per this review), and does *coordinating*
the six capabilities help beyond that (unaddressed here).

It is also a review rather than primary work, so its evidential weight properly belongs to the
literature it aggregates. `mapping_fidelity` is set at 0.62 to record the scope gap, which is
the dominant limitation rather than source quality.
