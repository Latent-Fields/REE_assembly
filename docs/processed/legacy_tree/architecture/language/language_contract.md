> **Elaborates Section 5 (Social Extension: Language) of `REE_CORE.md`.**

# Language Contract (Required Interface)

## Purpose
Language provides symbolic compression and social coordination for agents operating under uncertainty.
It functions as an externalised signal of internal state, reducing the computational overhead of full inverse modelling of others.

## Inputs
- Latent state summaries (typically context/regime-biased: z_theta, z_delta)
- Residue traces eligible for narration/abstraction (warnings, commitments, repair signals)
- Social context signals (presence of other agents; interaction channel availability)

## Outputs
- Updates to priors over latent space (belief/intent conditioning)
- Constraints or affordances on trajectory generation (plan shaping, coordination cues)
- Shared representations with other agents (common ground / alignment of expectations)

## Invariants
- Language MUST NOT directly override harm sensing or homeostatic degradation signals
- Language MUST NOT erase moral residue (R) or convert it into a purely reputational score
- Language MAY contextualise residue (scope, conditions, uncertainty) and defer action via commitments
- Language MUST be trust-weighted: symbolic inputs are integrated proportional to inferred reliability

## Failure if misused
- Rationalisation of harm (symbolic override of degradation)
- Ideological capture (fixed frames overriding perception and residue)
- Bureaucratic dissociation (abstraction decoupling from harm signals)
- Deceptive signalling attacks (manipulating others' priors)