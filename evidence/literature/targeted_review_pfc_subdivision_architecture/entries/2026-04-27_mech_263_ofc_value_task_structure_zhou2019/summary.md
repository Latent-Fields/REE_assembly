# Zhou, Gardner, Stalnaker, Ramus, Wikenheiser, Niv & Schoenbaum (2019) -- Multiplexed but Dissociable Value and Task Structure in OFC

## What the paper did

The authors recorded single-unit ensembles from rat OFC during an odour sequence task that they explicitly designed to dissociate value from task structure. The task had 24 unique "positions" defined by sensory information, reward likelihood, or both -- analogous to a spatial maze but constructed in odour space. The motivating question was whether OFC encodes expected value, a value-agnostic cognitive map of the task, or both. The authors framed the longstanding value-vs-cognitive-map debate as a false dichotomy, hypothesising that the two representations might co-exist on a continuum determined by task complexity and experience.

## Key findings relevant to MECH-263

OFC ensembles encoded the structure of the odour-sequence task: distinct positions in the sequence were distinguishable in the neural code, including positions that differed only in their structural role rather than in their immediate sensory features or expected reward. Multiplexed with this value-invariant representation, a representation of expected value at each location was also present. Critically, the two codes were dissociable -- they occupied separable axes in the population activity, not a fused mixture. The authors explicitly conclude that "the value and task structure co-existed as dissociable components of the neural code in OFC."

## How this maps to REE

This is the strongest available neural evidence for MECH-263's central architectural commitment. MECH-263 states that SD-033b carries "two complementary framings, treated as co-present rather than as alternatives" -- a structured cognitive map and specific-outcome predictions, with value signals "riding on top of this structured representation rather than being stored in it directly." The Zhou paper provides direct neural support for exactly this layered, multiplexed architecture. For ree-v3, this gives a clean justification for E2's representational design: a structured task-state representation as the primary substrate, with value as a separable signal that conditions on it. The paper also pre-empts a likely objection -- that an integrated value-only signal would suffice -- by showing the two are dissociable in real neural ensembles.

## Limitations and caveats

The paper does not address the mOFC vs lOFC subdivision in fine detail. MECH-263 distinguishes SD-033b (OFC, structured outcomes + cognitive map) from SD-033c (vmPFC, scalar value). Zhou 2019 finds value as a separable axis within OFC ensemble activity, but does not establish whether that scalar component is anatomically distinct from the structured component or whether it reflects vmPFC inputs. The Lopatina/Sadacca lOFC vs mOFC dissociation work (PMID 28541078) is needed to settle the subdivision question. The species transfer is the usual rat-to-REE chain.

## Confidence reasoning

I have set this at 0.86. Source quality is high (Current Biology, Niv-Schoenbaum collaboration, 24-state task is among the richest in this literature). Mapping fidelity is exceptionally high -- the paper's core conceptual claim is essentially identical to MECH-263's core conceptual claim, which is unusual for transfer literature. Transfer risk is moderate. The reason it is not 0.9+ is that the paper does not directly test the mOFC/lOFC subdivision MECH-263 inherits from SD-033, and the n is again small relative to human studies.

## Citation

According to PubMed, DOI: [10.1016/j.cub.2019.01.048](https://doi.org/10.1016/j.cub.2019.01.048). PMID 30827919.
