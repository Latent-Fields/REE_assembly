# Compute as an Evolving Substrate: Lightweight Economics Telemetry for REE

Status: processed
Intake: evidence/planning/thought_intake_2026-09-07_compute_economics_telemetry.md
Claims registered: none -- infrastructure/tooling proposal, nothing claim-shaped

## Thought

The computational needs of the Reflective–Ethical Engine (REE) project are unlikely to remain of the same kind throughout development.

At present, substantial cost is associated with the machinery surrounding REE: commercial frontier models reading repositories, coordinating work, generating and reviewing code, managing claims, interpreting experiments, and adjudicating evidence. The current Wave 4 planning work reinforces this distinction: it identifies inter-governance activity as a major token sink and, more importantly, concludes that adjudication rather than numerical compute is presently the principal bound on scientific throughput. 

That situation need not persist.

As REE matures, the computational centre of gravity may move from **machines thinking about REE** toward **machines running REE**.

Long developmental trajectories, larger environments, multiple organisms, ablation studies, parameter searches, repeated seeds, counterfactual rollouts, sleep/waking comparisons, population studies and increasingly detailed internal measurement could create a large, persistent computational workload. This is fundamentally different from buying access to frontier reasoning.

The correct infrastructure strategy therefore cannot be decided once. It should emerge from measurement.

## The old pricing readout was pointing at something useful

An earlier coordinator display contained pricing information. That information was subsequently displaced as the coordinator readout evolved.

Rather than simply restoring a price counter, its underlying idea should be resurrected in a broader form.

The useful question is not:

> How much are the models costing today?

It is:

> What computational resources is REE consuming, what value are they producing, which of those resources could be substituted, and at what point does owning compute become preferable to renting it?

This requires only lightweight accounting.

The objective is **not** to construct another governance subsystem. Compute accounting should be almost entirely observational, automatically collected at existing execution chokepoints, and cheap enough that it never becomes a reason not to run an experiment.

## A lightweight compute ledger

Each substantial computational activity could emit a small append-only record.

A minimal record might contain:

- timestamp
- repository / subsystem
- workload class
  - governance
  - coding
  - literature/research
  - experiment
  - training
  - inference
  - analysis
- experiment/run/task identifier where applicable
- provider/backend
- model or hardware type
- wall-clock duration
- input/output/cached tokens where available
- Graphics Processing Unit (GPU) hours where applicable
- Central Processing Unit (CPU) hours where useful
- peak accelerator memory where readily measurable
- peak system memory where readily measurable
- direct monetary cost
- estimated electricity use for owned compute
- success/failure/aborted state

Most of these should be harvested automatically rather than supplied by an agent.

A second, deliberately smaller layer could record economic interpretation:

- `local_substitutable`: yes / no / unknown
- `substitution_candidate`: model or hardware class, if known
- `quality_constraint`: whether frontier capability was materially necessary
- `repeatability`: one-off / intermittent / recurrent / continuous

The distinction between **cost incurred** and **cost actually substitutable** is particularly important.

€1,000 spent on frontier reasoning is not equivalent to €1,000 of GPU rental if no local model can perform the same work acceptably.

## Record resources, not merely money

Prices change rapidly. Historical resource consumption is more durable.

Therefore the ledger should preferentially record quantities such as:

- tokens
- GPU-hours
- CPU-hours
- memory requirement
- elapsed time
- storage/input-output burden

and separately apply a pricing table.

If an H100 GPU-hour falls from €4 to €2, historical experiments do not need to be rewritten. Their resource consumption remains valid and the economic model can simply be recalculated using new prices.

Likewise, the cost of electricity, commercial model tokens, cloud accelerators and candidate workstations can change independently.

This separates:

**what REE required**

from

**what that requirement currently costs to satisfy.**

That distinction could become extremely valuable over years of development.

## The coordinator display can then become a readout, not the database

The old pricing area could return in a more useful guise as perhaps a **COMPUTE / ECONOMICS** panel.

It need not be large.

For example:

**Last 30 days**
- commercial model spend
- cloud compute spend
- local compute estimate
- GPU-hours
- frontier tokens
- percentage judged locally substitutable

**Workload mix**
- assembly/governance
- scientific experimentation
- training
- analysis

**Ownership signal**
- annualised substitutable spend
- estimated local-machine utilisation
- candidate workstation break-even
- confidence: low / medium / high

The interesting number eventually becomes something like:

> **OWNERSHIP CROSSOVER: not reached**

or later:

> **OWNERSHIP CROSSOVER: plausible — projected 19-month payback**

That is considerably more informative than displaying today's token price.

## A dynamic ownership model

For a candidate machine:

\[
C_{\text{owned}}
=
C_{\text{capital amortisation}}
+
C_{\text{electricity}}
+
C_{\text{maintenance}}
+
C_{\text{obsolescence}}
\]

Compare this with:

\[
C_{\text{external}}
=
C_{\text{substitutable API}}
+
C_{\text{substitutable cloud compute}}
\]

The word **substitutable** is essential.

The accounting system should not claim that an application programming interface (API) call could have been local merely because a local model exists. Substitution should eventually be empirically demonstrated on REE workloads.

This suggests that REE could occasionally run **compute substitution assays**:

> Can this class of coordinator task be performed by model X instead of the current frontier model without materially degrading the result?

The answer then becomes part of the economic dataset.

Commercial model progress itself can therefore reduce the value of owning inference hardware in one part of the project while increasing the value of ownership elsewhere.

## There are several crossovers, not one

The system should avoid producing a single simplistic “buy a workstation” number.

There may be separate crossover points for:

1. **REE_assembly inference**
2. **routine coding and administration**
3. **REE experimental inference**
4. **REE training**
5. **large experimental sweeps**
6. **persistent organism operation**
7. **rare high-compute experiments**

Some may never favour ownership.

For example, commercial frontier cognition might remain best purchased externally while recurrent REE experiments become overwhelmingly cheaper locally.

Conversely, enormous but infrequent experiments may remain ideal cloud workloads even after REE owns substantial hardware.

The probable mature infrastructure is therefore hybrid rather than purely local or purely cloud.

## Queueing and scientific latency matter too

Pure monetary accounting misses an important benefit of owned compute.

Suppose an experiment costs only €20 in the cloud, but starting it involves provisioning hardware, transferring data, configuring environments and deciding whether its value justifies the expense.

A local machine sitting beside the development environment changes behaviour.

Experiments can become:

> “Run it.”

rather than:

> “Is this worth renting a machine for?”

That reduction in friction may increase experimentation itself.

The ledger should therefore eventually capture at least crude measures of:

- queue delay
- time from experiment-ready to experiment-start
- failures caused by unavailable resources
- experiments deferred for cost or capacity reasons

Ownership has scientific value if it converts scarce scheduled computation into an abundant laboratory instrument.

## Conversely, ownership creates risks

A purchase can also lock REE into assumptions that turn out to be wrong.

Relevant risks include:

- accelerator architecture becoming obsolete
- insufficient accelerator memory
- software ecosystem incompatibility
- poor utilisation
- rapidly falling cloud prices
- rapid improvement in commercial models
- REE becoming CPU- rather than GPU-bound
- REE becoming memory-bandwidth-bound rather than compute-bound
- distributed experiments proving more valuable than one very large machine
- hardware failures
- heat, noise and electrical requirements
- sunk-cost pressure encouraging experiments suited to owned hardware rather than experiments scientifically worth doing

The telemetry should therefore make **delay** measurable too.

Waiting has option value.

## Suggested purchase trigger

Rather than selecting a particular workstation today, REE could eventually define a conservative purchasing rule.

For example, investigate ownership seriously when all of the following become true:

- projected workload fits a known hardware class;
- the workload has remained substantial for several months;
- a meaningful proportion of external spend is demonstrably substitutable;
- utilisation would be high enough to avoid largely idle capital;
- expected payback is comfortably within the useful hardware lifetime;
- local execution provides meaningful scientific-throughput benefits;
- the proposed hardware has been tested using actual REE workloads before purchase.

This turns a future €10,000, €30,000 or €150,000 decision from speculation into an evidence-backed infrastructure decision.

## Implementation principle

The important constraint is:

> **Measure once at the execution chokepoints; derive everything else later.**

There should not be a new form for every experiment.

Experiment manifests already know much of what is required. Model wrappers know token counts and model identity. Cloud runners know machine type and duration. Local runners can obtain hardware and elapsed-time information.

These events can feed an append-only lightweight ledger, perhaps with a small pricing/configuration file applied during analysis.

The coordinator then merely reads the resulting summary.

If the coordinator interface changes again, the economic history survives.

## Broader implication

REE is unusual in that its infrastructure requirements may themselves trace the developmental progression of the project.

Early REE may spend most of its resources on external intelligence required to construct and understand the organism.

Later REE may spend increasingly large resources on the organism's own development, experience and experimental replication.

A compute ledger could make that transition visible.

One day the graph may cross:

**cost of thinking about the organism**

versus

**cost of letting the organism think.**

That crossover would itself be an interesting milestone in the development of REE.

## Suggested action

Introduce lightweight compute accounting now, while the workload is still modest.

Do not optimise infrastructure around it yet.

Record enough information that future decisions about local workstations, cloud accelerators and commercial models can be reconstructed empirically.

Resurrect the former pricing display only as a view over this deeper dataset.

The immediate goal is therefore not to decide what computer REE needs.

It is to ensure that, when REE eventually tells us what computer it needs, we have been listening.
