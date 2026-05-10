# Cooper & Shallice 2000 -- Contention Scheduling and the Control of Routine Activities

## What the paper did

Cooper and Shallice formalised the contention-scheduling theory originally proposed by Norman and Shallice (1986) into a computational simulation. The model represents routine action as a hierarchically-organised network of *action schemas*: each schema has an activation level, initiation conditions (perceptual triggers), and termination conditions (goal completion). Schemas compete for execution via lateral inhibition; the winner gates motor output. They demonstrate that the model produces realistic action sequences in everyday tasks (preparing coffee, packing a lunchbox) and that selectively lesioning activation pathways reproduces the characteristic sequencing errors of action-disorganisation syndrome (ADS) patients with frontal-lobe damage.

## Key findings relevant to the rule-apprehension vocabulary question

This paper anchors the *parallel ancestor lineage* to the AI options framework. Both traditions converged on essentially the same primitives in different vocabulary:

| AI options vocabulary | Cooper-Shallice schema vocabulary |
|---|---|
| Option | Action schema |
| Initiation set / context | Schema initiation conditions |
| Intra-option policy | Schema body / sub-schemas |
| Termination function | Schema termination conditions |
| Policy-over-options | Lateral inhibition / contention scheduling |
| Hierarchical option structure | Schema hierarchy |
| (no clean analog) | Supervisory Attentional System (SAS) |

For Pull 4's vocabulary-mapping question this matters: the schema tradition has been doing approximately what REE's rule-apprehension cluster has been doing, for *fifty years* (Norman-Shallice 1986 builds on Bartlett 1932). The vocabulary inheritance is rich: schema, schema-activation, lateral inhibition, contention scheduling, supervisory attentional system. ARC-062's gated_policy + discriminator is, in this vocabulary, the SAS overriding routine contention scheduling for novel contexts -- which is a more precise functional decomposition than REE has yet articulated.

## How the findings translate to REE

The translation gives REE a vocabulary upgrade and a candidate functional split:

1. **MECH-312 (dual-channel rule arbitration) = contention scheduling** between competing rule-options. The Cooper-Shallice lateral-inhibition mechanism is a directly transferable implementation candidate.
2. **ARC-062 (top-down rule application via gated_policy + discriminator) = Supervisory Attentional System overriding contention scheduling** for non-routine contexts. The discriminator is the SAS's "is this routine?" classifier; the gated_policy is the SAS's override output.
3. **ARC-064 (bottom-up rule discovery) = schema acquisition / schema-network learning**, which the schema tradition has its own (less computationally developed) literature on.

The implication for cluster registration: the schema vocabulary is more anatomically-grounded (PFC-SAS = ARC-062 is a sharper claim than "context-conditioned policy") but algorithmically less developed (no option-critic-equivalent gradient). The right move is to use schema vocabulary for *describing function* and options vocabulary for *prescribing implementation* -- a hybrid that explicitly bridges the two traditions.

## Limitations and caveats

The Cooper-Shallice model is *descriptive*. It reproduces patient lesion patterns in simulation, but does not have the algorithmic / convergence-theorem apparatus of options/HRL. So inheriting from this line gives REE *concepts* (schema, lateral inhibition, SAS) but does not give REE off-the-shelf *algorithms* in the way Bacon 2017 or Eysenbach 2018 do.

The schema tradition has also fragmented since 2000. There has been no mass continuation of the Cooper-Shallice model in the way option-critic and DIAYN extended Sutton-Precup-Singh. Adopting schema vocabulary commits REE to a relatively static body of work, while options/HRL vocabulary commits REE to an actively-developing one.

The deeper caveat: the schema and options traditions were *never explicitly merged*, despite addressing essentially the same architectural slot. There is no foundational paper that says "schema = option". Adopting the equivalence is something REE would be doing largely on its own initiative.

## Confidence reasoning

Scored 0.72. Source quality is solid (Cog Neuropsychology, well-cited, frontal-lobe-patient data anchors). Mapping_fidelity is high (0.78) for concept-level translation. Transfer_risk is moderate (0.40) because the model is descriptive and the schema-options identification is REE's own bridge work. Direction is "mixed" because while the concept-level inheritance supports the options-vocabulary mapping, the schema tradition adds the SAS / supervisory-attention layer that pure options/HRL canon does not include -- this is a genuine vocabulary upgrade for ARC-062. The paper feeds R2 (vocabulary inheritance) and R4 (HYBRID renaming recommendation: schema vocabulary for function, options vocabulary for implementation).
