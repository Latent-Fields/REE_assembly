# Sutton, Precup & Singh 1999 -- Options as the canonical temporal-abstraction primitive

## What the paper did

Sutton, Precup and Singh proposed a formal extension of the standard MDP/RL framework to handle temporally abstract actions, which they called *options*. An option is a triple `(I, pi, beta)`: an initiation set `I` of states from which the option can start, an intra-option policy `pi` that maps state to action while the option is running, and a stochastic termination condition `beta(s)` that gives the probability of stopping in each state. Primitive actions are the limiting case (single-step options that always terminate). They show that an MDP augmented with options becomes a semi-Markov decision process (SMDP), prove that standard SMDP Q-learning and value iteration extend to options with the usual convergence guarantees, and develop *intra-option learning* that lets the agent learn about an option from any trajectory consistent with that option's policy -- without needing to fully execute it.

## Key findings relevant to the rule-apprehension vocabulary question

This is the load-bearing paper for the working hypothesis behind Pull 4. What we have been calling, in REE-internal language, "rule apprehension" -- gated context-conditioned policies (ARC-062), bottom-up extraction of behavioural patterns (ARC-064), behavioural-pattern-compression (MECH-317) -- is, in computer-science / RL vocabulary, an *option*. The option triple maps cleanly:

- **Initiation set `I`** corresponds to the discriminator side of ARC-062 / the "context where this rule applies" of bottom-up rule discovery.
- **Intra-option policy `pi`** is the policy fragment that implements the rule's behavioural content.
- **Termination condition `beta`** is what tells the agent when the rule no longer applies / the chunked sequence ends.

Twenty-six years of follow-on work (Stolle & Precup 2002 option-discovery, Bacon, Harb & Precup 2017 option-critic, Eysenbach et al. 2018 DIAYN, Solway et al. 2014 optimal hierarchies, Botvinick, Niv & Barto 2009 neural HRL) sits on top of this paper. If REE adopts options vocabulary, all of that lands on the desk for free.

## How the findings translate to REE

The translation is mostly direct, with one design caveat:

- ARC-062 ("top-down rule application") -> *option selection over a set of context-conditioned options*. The gated_policy + discriminator is a learned gating mechanism over options.
- ARC-064 ("bottom-up rule discovery") -> *option discovery from trajectory data*. The proposed sub-MECHs MECH-316 (cross-episode-regularity-extraction) and MECH-317 (behavioural-pattern-compression) line up with two complementary option-discovery pathways: statistical-regularity extraction (Stachenfeld 2017 successor-representation) and chunking by repetition (Smith & Graybiel 2013 striatal action-chunking, Bacon 2017 option-critic).
- MECH-318 ("rule-state-abstraction-substrate") -> *option-conditioned state abstraction*. OFC-as-cognitive-map (Wilson 2014, Schuck 2016, Niv 2019) hosts the labels that make options identifiable.

The caveat: options assume MDP/SMDP structure and a state-conditioned termination function `beta(s)`. REE's substrate is continuous-state with competition-mediated termination; the option formalism is right *conceptually* but the implementation likely uses a soft / salience-driven termination rather than a hard beta. That mismatch is implementation work, not a refutation of the mapping.

## Limitations and caveats

The Sutton-Precup-Singh framework is silent on *how* options are discovered. That is the part of ARC-064 / MECH-317 we most need, and it is left to the follow-on literature. Also, options as originally formulated assume a given reward signal; some of REE's bottom-up rule discovery is partially reward-agnostic (a behavioural pattern can be extracted from trajectory regularity without being valuable yet), which connects more naturally to Eysenbach 2018's DIAYN line than to vanilla options. So the inheritance is partial: the *formalism* and the *value-learning theorems* transfer, the *discovery algorithms* need to be picked up from later papers.

## Confidence reasoning

I scored this 0.88. Source quality is at-ceiling -- this is the foundational AI-journal paper, 6000+ citations, no replication concerns. The mapping_fidelity is high (0.85) because the option-triple concept genuinely covers what REE's rule-apprehension cluster has been pointing at, and there is a clean correspondence for each of the proposed sub-MECHs. Transfer risk is moderate (0.30) because the discrete-MDP / hard-termination assumptions don't transfer literally and option-discovery has to be picked up from successor papers. The verdict the paper feeds: ARC-062, ARC-064 and MECH-317 should probably be re-named or hybrid-named onto options vocabulary; the genuinely new REE contribution lives elsewhere (Pull 4 R3).
