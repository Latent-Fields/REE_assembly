# Curriculum Learning for RL Domains (Narvekar et al., JMLR 2020)

## What the paper did

Narvekar, Peng, Leonetti, Sinapov, Taylor, and Stone produced a comprehensive survey and framework for curriculum learning in RL, covering 17 years of the literature. Their framework classifies curriculum approaches along four axes: who designs the curriculum (human expert vs automatic generator), what varies across curriculum tasks (difficulty, task type, reward structure, environment parameters), when tasks are introduced (fixed schedule, performance-triggered, or adaptive online), and how transfer occurs between tasks (policy initialisation, reward shaping, state abstraction). The survey identifies three main paradigms: teacher-student curricula (an external teacher selects tasks based on student performance), self-paced curricula (the learner modulates its own task selection), and task-generation curricula (new tasks are created rather than selected from a fixed pool).

## Key findings

The most important finding for REE's diversity problem is the distinction between difficulty-based curricula and diversity-based curricula. A curriculum that only sequences tasks by difficulty (easy-to-hard) does not prevent monostrategy if all tasks require the same strategy. A diversity-based curriculum explicitly sequences tasks by behavioral type -- which strategy must be used -- to ensure the agent develops a repertoire before gradient pressure consolidates a single dominant mode. The survey also identifies a consistent finding in the curriculum literature: adaptive curricula outperform fixed schedules, because the optimal task sequence depends on the agent's current competence state, which changes during training.

## Translation to REE

For REE's V_s monostrategy problem, the curriculum axis that matters is task type (which attractor/goal-mode is primary), not task difficulty. A curriculum that graduates from "easy foraging" to "hard foraging" will still produce a foraging monostrategy. What is needed is a curriculum that sequences experiences by which behavioral mode is being developed: first establish basic safety-seeking competence, then establish basic foraging competence, then introduce environments requiring context-sensitive switching between them. The survey's framework directly supports the behavioral_diversity_acceptance_criteria.md Rung ladder structure: Rung 0-1 establishes mode competence, Rung 2-3 tests mode selection and switching, Rung 4 tests ethical mode prioritisation. The curriculum should be adaptive, not fixed: mode transitions should be triggered by competence plateaus on the current mode, not by episode count.

## Limitations and caveats

This is a survey paper. It provides taxonomy and principles, not experimental evidence for specific curriculum designs. The survey does not cover the quality-diversity literature (MAP-Elites, DIAYN) in depth -- these approaches are covered separately in this literature pull. The automatic curriculum generation section notes that source task selection (which tasks to include and in what order) is largely unsolved, and most successful examples require domain-specific knowledge to design the curriculum. REE will need domain expertise to specify the initial curriculum tasks before any adaptive mechanism can take over.

## Confidence

0.72. JMLR comprehensive survey; solid organisational contribution. Mapping fidelity moderate because this is a taxonomy, not an empirical study. The framework is directly applicable to REE's curriculum design choices, but specific parameters (task ordering, transition criteria) require empirical investigation.
