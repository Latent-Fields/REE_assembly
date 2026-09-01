# Rohde & Plaut (1999) -- Language acquisition in the absence of explicit negative evidence: how important is starting small?

**Claim tested:** ARC-019 | **Direction:** weakens | **Confidence:** 0.62

## What the paper did

Rohde and Plaut set out to reproduce and extend Elman (1993). They trained simple recurrent
networks on pseudo-natural grammars of varying English-likeness -- systematically varying the
proportion of complex constructions, the degree of semantic constraint on which nouns take which
verbs, and network capacity -- under both staged ("starting small", via simplified input or
limited initial memory) and unstaged regimes. Their sweep was materially broader than the original.

The finding: none of their simulations showed an advantage to starting small. In most, the staged
regime performed *worse* than full-complexity training from the outset, and the deficit widened as
the language was made more English-like -- i.e. as semantic constraints between verbs and their
arguments were strengthened, which is what makes natural language learnable in the first place.
Their reading is that Elman's positive result was contingent on the particular capacity and
schedule settings he happened to use, and that neither maturational constraint nor innate
linguistic mechanisms are needed to account for acquisition without negative evidence.

## Why this bears on ARC-019

This is the strongest directly-adversarial evidence in this pull. ARC-019's FALSIFYING branch
describes a world in which "the explicit stage/gate structure is not doing useful work beyond what
unstructured training achieves anyway -- the curriculum may still be a convenient scaffold ... but
'staged development with explicit gates' would not be architecturally load-bearing". Rohde and
Plaut report that world, in the one domain where the staged-development claim was most firmly
established.

The detail that should worry us most is the *interaction*: the harm from staging increased with
task realism. If that generalises, a REE staged-vs-flat comparison run on a simple early
environment could favour the staged arm and then invert as the environment is enriched -- meaning
an early positive V3 result on the infant curriculum would be the least reliable kind of support
for ARC-019, not the most.

## The honest limit on this

I do not think this refutes ARC-019 as stated, and it would be over-reading to file it that way.
What Rohde and Plaut manipulate is the *complexity of the input distribution* in supervised
sequence prediction. What REE gates is *phase advance in an embodied agent with a reward, a policy,
and a competence floor*, where the argued benefit is not representational bootstrapping but
avoiding the expenditure of a finite episode budget on sub-tasks the agent cannot yet master. Those
are different mechanisms that happen to share a name. A network can always keep training on hard
sentences it is failing at; an agent that cannot reach a goal state generates no useful gradient at
all. That asymmetry is not represented anywhere in this paper.

So: this is a genuine and well-executed weakening of the *general* proposition that staging helps,
and it should lower our prior on ARC-019 substantially. It is not a substitute for running REE's
own matched-budget comparison, and it does not tell us what that comparison will show.

## Confidence reasoning

`source_quality` 0.80 -- broader and more systematic than the study it targets, same journal,
authors with no stake in a negative outcome, and it has stood for twenty-five years as the standard
counterweight. `mapping_fidelity` 0.60 and `transfer_risk` 0.55 are set identically to the Elman
entry on purpose: the two papers share a domain and a manipulation, and scoring the negative result
on easier terms than the positive one would be a way of importing a conclusion through the
calibration. Aggregate 0.62, above Elman's 0.45 purely on source quality, since a careful
failure-to-replicate carries more information about a general architectural commitment than the
single positive finding it targets.
