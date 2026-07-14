# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

**Class surveyed:** OPTIONS / SKILLS | **Evidence direction:** supports | **Confidence:** 0.62

**Source:** Richard S. Sutton, Doina Precup, Satinder Singh (1999). *Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning.* Artificial Intelligence 112(1-2):181-211 DOI: 10.1016/S0004-3702(99)00052-1

Sutton, Precup & Singh's options framework defines an option as a triple -- initiation set, intra-option policy, and termination condition -- a closed-loop temporally-extended sub-behaviour the agent can invoke like a primitive action. Planning and learning then occur over a semi-MDP whose actions are options, so value backups jump across multiple timesteps and the policy composes reusable sub-behaviours rather than primitive moves.

This is the theoretical warrant that temporal abstraction is a distinct capability from flat control: options change decision granularity, enabling faster credit assignment and structured exploration (an option carries the agent across many gridworld cells in one decision). It is orthogonal to and composable with a novelty bonus -- RND changes what states get visited, options change the timescale of decision and credit assignment.

The honest limit: the framework is silent on where good options come from, and its demonstrations use hand-specified options. So it supports the *class* but the floor->competent benefit depends on either hand-designed options (cheap, buildable) or learned option discovery (Paper DIAYN, heavyweight). For a small forage-gridworld, a few structurally-obvious hand-specified options with explicit termination is the cheap discriminating probe.

Confidence 0.62: strong framework-level support, but not itself a floor->competent datapoint on this substrate. Its practical value is as the lightweight entry point (hand-specified options + termination bracketing) that tests the temporal-abstraction hypothesis before committing to DIAYN-class discovery machinery.
