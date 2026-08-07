# Discovery of Options via Meta-Learned Subgoals (Veeriah et al. 2021, NeurIPS)

Most of hierarchical reinforcement learning's "options" literature assumes the useful subgoals are
already known, or hand-engineered, and the interesting problem is just choosing among them. Veeriah
and colleagues (a DeepMind team including David Silver and Satinder Singh) instead ask where those
subgoals should come from in the first place. Their answer is a manager-worker split: a manager
policy chooses, per task, between primitive actions and a set of task-independent "options," each of
which is defined by its own learned reward function and termination condition -- in effect, a learned
subgoal. Rather than hand-specifying what makes a good subgoal, the option's reward and termination
functions are themselves parameters, optimized end-to-end via meta-gradients so that having this
option around actually helps the manager do better across many training tasks. The headline result is
transfer: options discovered this way generalize usefully to held-out tasks the system never trained
on, letting a freshly initialized manager learn faster than one with only primitive actions.

This is relevant to the intake's candidate topology for a specific reason: it is evidence that
subgoal DISCOVERY, not just subgoal CREDIT once a hierarchy is already declared, is a tractable
machine learning problem with a real credit-assignment mechanism behind it. REE's existing MECH-427/
428 machinery already handles cross-level credit for a given parent/subgoal relation -- subgoal
attainment can reinforce or bootstrap the parent. What this paper adds, at least as a proof of
concept from an unrelated field, is that the SAME kind of credit signal (does having this subgoal
make the higher-level policy better off) can also be turned around to originate candidate subgoals
in the first place, rather than only crediting subgoals someone already wrote down. That is one
version of what the intake calls "downward discovery" -- a new state turning out to be a necessary
subgoal -- happening through an optimization process instead of a moment of noticing.

The gap between what this paper shows and what the intake's candidate claim needs is real and worth
stating precisely. The manager-worker split here is a fixed two-level hierarchy; it has nothing to
say about lateral relations (an orthogonal possibility worth retaining for later, per the intake's
Section 1c) or about a possibility being revealed as SUPERORDINATE to the current goal, both of which
the intake explicitly wants a general topology to hold alongside parent/subgoal. And discovery in
this paper happens slowly, across many training episodes and tasks, via meta-gradient descent -- not
as a fast, within-episode event triggered by something the agent notices while pursuing an unrelated
goal, which is the scenario the intake's Section 1 quotation actually describes. So this paper
supports the general PRINCIPLE that subgoal structure need not be fully hand-given, without
supporting the specific mechanism (fast, in-episode, surprise-triggered structural revision) the
intake's key formulation depends on.

Confidence: 0.58, the lowest of the "supports" entries. Source quality is good (NeurIPS, credible
lineage of prior options-framework work, genuine held-out-task generalization results). Mapping
fidelity is moderate-low: real support for "discovery, not just credit, is tractable," but no purchase
on multi-relation-typing, laterality, or fast online discovery -- exactly the parts of the candidate
claim that remain open after this pull.
