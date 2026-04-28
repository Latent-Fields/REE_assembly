# Botvinick, Niv & Barto 2009 — Hierarchically organized behaviour and its neural foundations

According to PubMed: Botvinick, Niv & Barto. *Cognition* 113(3):262-280 (2009). [DOI 10.1016/j.cognition.2008.08.011](https://doi.org/10.1016/j.cognition.2008.08.011). PMID 18926527.

## What the paper did

The paper integrates the formal *options* framework from hierarchical reinforcement learning (Sutton, Precup & Singh 1999) with neuroscience evidence about the functional architecture of prefrontal cortex. The core formal idea: actions in classical RL are atomic, but real behaviour is divisible into discrete tasks, which contain subtask sequences, which are built from simple actions. Hierarchical RL extends the formalism by allowing the agent to aggregate actions into *reusable subroutines* — options. An option is formally a triple: an initiation set (states where the option can start), an internal policy (what to do while running), and a termination function (when the option ends).

The neural reading the authors propose is that components of hierarchical RL map onto known PFC functional architecture. Dorsolateral PFC supports the active maintenance of subtask context. Orbital PFC contributes outcome-evaluation that gates option selection. Anterior cingulate may participate in cost-of-control evaluation that arbitrates flat-vs-hierarchical action selection. The framework is partly inferential — they argue components "might map onto" rather than demonstrating dissociations directly — but subsequent fMRI work (Ribas-Fernandes 2011, Boorman 2009) has provided more direct neural support.

The single most architecturally important open question they flag: **how does an agent identify new option subroutines from experience?** This is the same question an REE option library would face — how would the substrate populate its option dictionary?

## Why this matters for REE's decomposition question

This paper grounds the **option / hierarchical-RL level** of the biological action representation hierarchy. The level sits above flat goal-directed planning (Daw 2005, separate entry) and below abstract goal representation (the ARC-035 / SD-033b territory). Options are temporally extended, reusable, named action subroutines whose internal logic is hidden from the higher-level controller.

For REE V3 the architectural mapping is interesting. The action_object_decoder in HippocampalModule is functionally similar to an option in that it produces a multi-step action sequence from a compact representation. But it is a *continuous* decoder over a fixed `action_object_dim` — not a discrete library of named, recallable options each with explicit initiation and termination conditions. The architectural difference matters because:

- An option library can be queried by *initiation match*: "what options can I start from this state?"
- An option library can be selected by *expected outcome*: "which option's termination state cosine-matches my current goal?"
- An option library can be composed: "run option A until it terminates, then option B, etc."
- A continuous decoder can do none of these directly without re-rolling through E2 + CEM.

For MECH-293 ghost-goal probes specifically, an option library would couple naturally. Ghost probes currently seed CEM from anchor `z_world` snapshots. With an option library, probes could additionally select *which option* to invoke at the seed state — preferring options whose initiation set matches the seed and whose termination state cosine-matches the current `z_goal`. This is a strictly richer probe-seeding strategy.

## What it does NOT settle

REE's grid-world has 4 atomic actions and episodes of 200-500 steps. The option / hierarchical-RL framework is biologically and computationally significant when actions are temporally extended at much longer scales — "walk to the kitchen" as a 50-step subroutine, "complete the foraging route" as a 200-step subroutine. At V3 granularity, the option level provides limited additional capacity over the existing CEM proposer; CEM with horizon 30 is already operating at temporally-extended scales relative to single actions.

The option substrate becomes architecturally load-bearing when REE moves to richer environments. Tools (multi-step preparation sequences before use), social coordination (multi-step protocols with another agent), or hierarchical task structure (sub-goals nested within larger goals) all require options that the current SD-004 action-object framework doesn't naturally express.

The framework leaves open *how* options are identified from experience. Botvinick et al. flag this as an important open question. For an REE option library, this is the same question — how would the dictionary populate? Sleep-driven extraction (per the type-prototype lit-pull) is one candidate; bottleneck states (states the agent passes through frequently on the way to many goals) are another, supported by computational work.

The neural mapping is partly inferential. The paper argues components "might map onto" PFC structures rather than demonstrating dissociations directly. Subsequent fMRI work has tightened this, but the original framework paper is the anchor, not the empirical close.

## Confidence reasoning

I sit this at 0.83. Source quality 0.88 — *Cognition*, foundational integrative review, options framework is widely adopted in computational neuroscience and cognitive modelling. Mapping fidelity 0.78 because the option level is a genuine missing slot in REE V3's decomposition between primitive actions and goal-directed planning, with a clear architectural shape. Transfer risk 0.40 because V3's gridworld and short episodes don't strongly need temporally extended actions; the option level becomes more architecturally meaningful in V4 environments with richer task structure.
