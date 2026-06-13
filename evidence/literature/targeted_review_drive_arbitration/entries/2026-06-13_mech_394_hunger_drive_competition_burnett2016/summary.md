# Hunger-Driven Motivational State Competition (Burnett et al. 2016)

**Claim(s):** MECH-394 (multidrive arbitration policy), SD-060 (non-terminal drive register)
**Direction:** supports · **Confidence:** 0.80
**Source:** Burnett, Li, Webber, Tsaousidou, Xue, Bruning & Krashes (2016), *Neuron*. According to PubMed, [DOI: 10.1016/j.neuron.2016.08.032](https://doi.org/10.1016/j.neuron.2016.08.032).

## What the paper did

Burnett and colleagues asked a question that ethology has posed for decades but rarely answered at the circuit level: when an animal is bombarded by competing internal demands -- it is hungry *and* thirsty *and* frightened *and* there is a conspecific to investigate -- how does the nervous system decide what to do? Using hypothalamic Agouti-related-peptide (AgRP) arcuate (ARC) neurons as an entry point, they ran a battery of behavioural assays pitting hunger against thirst, anxiety-related behaviour, innate fear, and social interaction, and combined this with real-time fibre-photometry recording of ARC activity and optogenetic manipulation. The design lets them read off both the *behavioural* outcome of competition and the *neural* correlate of the integration that produces it.

## Key findings relevant to the claim

The headline result is that hunger does not sit at a fixed rung of a static ladder. Instead, the hungry state *increases its capacity to suppress* rival motivational systems -- and crucially it does so "often only when food is accessible." The dominance of one drive over another is conditional on the affordance structure of the environment, not a hard-wired ranking. At the neural level, ARC neurons showed time-locked responses not only to food presentation but also to conspecific investigation, which the authors take as evidence that "even at the level of ARC neurons, choices are remarkably flexible computations, integrating internal state, external factors, and anticipated yield."

That triplet -- internal state, external factors, anticipated yield -- is, almost word for word, the orchestration variable set MECH-394 names (context, per-axis satiation, inter-drive competition, developmental phase). The paper is the cleanest available biological existence proof that drive arbitration (a) is real, (b) operates by the *winning* drive actively suppressing the others rather than by a passive max-pick, and (c) is graded by satiation level and gated by context. It also incidentally grounds SD-060: thirst, fear, anxiety, and social interest are handled here as first-class competing drives in their own right, not as terms folded into a single energy scalar.

## How it translates to REE

For MECH-394 the translation is direct. REE's claim is that behaviour under multiple active drives is selected by a soft-competitive orchestration over context/satiation/competition/developmental-phase rather than a fixed priority or single-axis winner. Burnett et al. supply the wet-lab version of exactly that: a competition whose outcome flips with context (food accessibility) and with the depth of the driving need. The arcuate integration of state + external factors + anticipated yield is the biological instance of the contextual arbitration REE wants to build. For SD-060 it confirms that the brain does treat non-energy needs (thirst, fear, sociality) as distinct axes that can win or lose the competition -- the register REE proposes is biologically warranted, not a tidy abstraction.

## Limitations and caveats

Two honest boundaries. First, the data establish hunger-*dominates*-others, not a symmetric N-way arbitration: we see hunger suppressing thirst/fear/sociality, but the reciprocal geometry (does extreme fear suppress hunger, and by how much?) is left open, so the full competition surface MECH-394 generalises to is under-constrained by this single paper. Second, and this is the more useful caveat for design: the context-gating finding is a *warning* against the naive implementation. A drive register that arbitrates by static weights -- "hunger always beats thirst" -- would mispredict the very phenomenon Burnett documents, because hunger only wins decisively when food is reachable. Whatever MECH-394 becomes, its arbitration must read the environment's affordance state, not just the internal drive vector. The mapping is functional rather than mechanistic: REE has no arcuate/AgRP analogue, so this evidences the *computation* MECH-394 posits, not its substrate.

## Confidence reasoning

Source quality is high (Neuron; converging photometry, optogenetics, and a behavioural battery from the Krashes lab). Mapping fidelity is high because the orchestration-over-context-and-satiation language is almost identical to MECH-394's, but I hold it below 0.8 because the paper shows the hunger-dominant regime rather than a complete arbitration policy and REE has no homologous substrate. Transfer risk is moderate (mouse appetitive/defensive behaviour to a gridworld drive register) but the principle under test -- contextual, satiation-graded competition -- is the kind of thing that should be substrate-general. Net 0.80, and per the lit/exp decoupling this raises MECH-394's and SD-060's *literature* confidence only; both remain substrate_conditional V4 claims with exp_conf = 0 and are promoted by nothing here.
