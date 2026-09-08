# MAEBE: Multi-Agent Emergent Behavior Framework (Erisken et al., 2025)

## What the paper did

Erisken, Gothard, Leitgab and Potham set out to test something that most AI safety
evaluation quietly assumes: that if you have certified an agent as aligned on its own, you
have learned something durable about how it will behave in company. They built MAEBE, an
evaluation framework that runs the Greatest Good Benchmark -- a moral-preference instrument --
against both isolated LLM agents and ensembles of them, and paired it with a "double-inversion"
questioning technique that reframes each moral question without changing what it asks. Three
questions organise the work: do a model's moral preferences move when the framing moves; is
ensemble moral reasoning predictable from the isolated agents that compose it; and do peer
pressure and group dynamics introduce failure modes that single-agent evaluation cannot see.

## Key findings relevant to ARC-034

The answers were, in order: yes, no, and yes. Single-agent moral preferences -- particularly
on instrumental harm -- turned out to be unstable under reframing alone, which is worth
pausing on, because it means the n=1 baseline against which any ensemble is compared is not
itself a fixed quantity. More centrally for ARC-034, the paper reports that "the moral
reasoning of LLM ensembles is not directly predictable from isolated agent behavior due to
emergent group dynamics." And the group dynamic that did the work was peer pressure:
ensembles converged under mutual influence, and did so *even when a supervisor agent was
present*. The authors' conclusion is stated as a methodological requirement rather than a
finding about any particular model -- safety evaluation must occur in interactive multi-agent
contexts, and cannot assume single-agent results generalise.

## How this translates to REE

ARC-034 asserts that ethics testing must span nth-order multiagent trajectory distributions,
and that local pairwise probes are insufficient to characterise emergent ethical properties.
The MAEBE result is, as directly as external literature is likely to get, the negative half of
that claim demonstrated empirically in an artificial system: per-agent alignment certificates
did not compose into an ensemble alignment certificate. That maps onto ARC-034's test type (2),
multi-agent stress testing -- does ethical behaviour degrade or amplify under load? -- and the
supervisor result sharpens it, because the obvious engineering response to emergent
misalignment is to add an overseer, and here the overseer did not restore the validity of the
n=1 evaluation.

What it does *not* do is evidence the converse case, which is the one that actually motivated
ARC-034. The MECH-127 scenario is that locally depleted agents may produce *more* ethical
emergent behaviour at n=k than a direct-pathway analysis predicts, via counterfactual empathic
activation. MAEBE shows that n=1 fails to predict n=k; it does not show that the failure runs
in the favourable direction as well as the unfavourable one, and ARC-034's counterfactual-probe
test type (1) has no analogue in this paper at all.

## Limitations and caveats

Three, and they are not small. First, this is an unrefereed preprint from independent
researchers, workshop-submitted; there is no replication and the ensemble scale is modest.
Second, and more consequentially for the mapping: the agents are LLMs answering a moral
questionnaire. Their "moral preference" is a stated answer, not a behavioural disposition
arising from any care mechanism. REE's position under INV-001 is that there is no explicit
ethics module -- ethical behaviour is supposed to fall out of the substrate rather than be
read off a policy -- so a result about LLMs' stated moral preferences supports the *epistemics*
of ARC-034 (n=1 does not predict n=k) without telling us that the same non-composition holds
for ethical properties grounded the way REE grounds them. Third, "peer pressure" in an LLM
ensemble is a conversational phenomenon mediated by text context; whether the analogous
coupling exists in a REE multi-agent deployment is an open question, not an inherited result.

## Confidence reasoning

I have set confidence at 0.68. Mapping fidelity is high (0.85) and, for an architectural
test-scope claim, that is the term that should dominate: the paper's headline sentence is
nearly a restatement of ARC-034's core, and it was arrived at independently, which is the kind
of convergence that should raise one's credence. Source quality is the binding constraint
(0.55) -- preprint, one benchmark, no replication -- and transfer risk is moderate (0.35)
rather than high, because the structural transfer (artificial multi-agent ensemble to
artificial multi-agent ensemble) is short even though the ethics construct does not carry
across cleanly. The honest summary is that ARC-034's negative claim now has external
empirical company; its positive programme -- counterfactual probes, cascade mapping, the
formal characterisation of convergence to emergent state q -- remains unevidenced here.
