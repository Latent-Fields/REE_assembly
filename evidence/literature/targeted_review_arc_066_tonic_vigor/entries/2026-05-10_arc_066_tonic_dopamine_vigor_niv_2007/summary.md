# Niv, Daw, Joel & Dayan 2007 -- Tonic dopamine and opportunity costs

**Citation:** Niv Y, Daw ND, Joel D, Dayan P. Tonic dopamine: opportunity costs and the control of response vigor. *Psychopharmacology (Berl)*. 2007;191(3):507-520. PMID: 17031711. DOI: 10.1007/s00213-006-0502-4.

## What the paper does

Niv et al. start from the observation that the dominant computational story about dopamine -- phasic burst as a TD prediction error driving discrete action selection -- leaves the role of *tonic* DA underspecified. They derive an account in which the long-run average rate of reward functions as an opportunity cost on time spent passive, and is reported by tonic levels of DA. The mathematical claim is clean: in an average-cost RL formulation, the optimal response latency varies inversely with the reward rate history. Higher average reward implies higher cost-of-delay implies faster responding, regardless of the specific reward currently being pursued. The paper gathers free-operant pharmacology evidence (DA depletion / pharmacological manipulation effects on lever-press rate, latency, and willingness to expend effort) and shows the data fit the opportunity-cost framework.

## Why this matters for ARC-066

The architectural commitment ARC-066 registers is precisely the architectural slot Niv et al. mathematically motivate. The user-observed phenomenology -- "I observe a drive in me to do something while I have energy rather than nothing" -- maps onto Niv's opportunity-cost mechanism in a way the rest of the deficit-keyed REE substrate does not: the long-run average reward rate gives a *target-free* gradient toward action that is positive in well-fed-safe-familiar regimes (because reward history is rich) and tapers in degraded regimes (because reward history is poor). This is the architectural shape the family doc names as the missing substrate.

The R1 verdict (substrate attribution) and R3 verdict (implementation shape) both lean heavily on this paper. For R1, Niv's derivation gives the cleanest theoretical account of mesolimbic DA as the substrate, separating it from phasic-prediction-error functions which are not the ARC-066 territory. For R3, the opportunity-cost form is naturally additive: vigor = +(average_reward_rate * time_in_action) is equivalent to a passive-trajectory penalty = -(average_reward_rate * time_passive), so the child MECH can be implemented as either an additive bonus on action-trajectory E3 scores or an additive cost on no-op-trajectory scores. This is the cleanest implementation alternative and the one the synthesis will recommend.

## Caveats

The biggest scope mismatch is WHETHER-vs-HOW-FAST. Niv et al. formalise the timing axis (response latency given that responding is happening), not the act-vs-not-act selection axis. ARC-066 is registered specifically for the latter. The mathematical transfer is clean -- the same scalar that biases response rate also biases the score gap between action and no-op trajectories -- but the empirical evidence in Niv 2007 directly tests the timing readout, not the act-vs-not-act selection. This is why the entry confidence is 0.83 rather than higher. The companion Beierholm 2013 paper provides the human pharmacological complement that strengthens the causal interpretation but inherits the same readout-scope limitation.

A second caveat: the paper's "vigor scalar" is a long-run history average, not an internal capacity scalar. The ARC-066 functional_restatement currently says "high energy AND low recent prediction error AND low drive" -- an internal-state composition. Niv 2007 attributes the scalar to *environmental* reward history. The two are correlated in normal conditions but mathematically distinct. The R4 verdict will recommend revising the slot's pre-registered scalar composition toward Niv's reward-history account, with internal-state proxies as secondary modulators. This is an architectural reframe for the slot, not for this paper's evidence per se.

## Confidence reasoning

Source quality is high (foundational paper, heavily cited, principled mathematical derivation, integrates broad pharmacology literature). Mapping fidelity is strong on the substrate and form, weakened by the scope mismatch on readout (timing vs selection). Transfer risk is moderate: the theoretical framework transfers cleanly to REE's E3 scoring chain, but the empirical anchoring is in rodent free-operant tasks with simpler action spaces than REE's episodic environments. Aggregate 0.83 -- highest of the seven-paper ARC-066 cohort, reflecting Niv 2007's load-bearing role across R1, R3, and R4.

According to PubMed, this paper appears under the cited PMID with the DOI listed above; the project briefing's PNAS attribution is corrected to Psychopharmacology (Berl).
