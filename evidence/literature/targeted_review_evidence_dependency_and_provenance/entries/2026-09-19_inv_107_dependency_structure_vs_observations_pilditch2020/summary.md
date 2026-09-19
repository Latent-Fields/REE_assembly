# Pilditch, Hahn, Fenton and Lagnado 2020 -- why INV-107 is negative-only

This was the load-bearing verification of the pass. INV-107's notes state that the invariant's negative-only
form "was arrived at by CORRECTION, not by caution", and that this paper is what forced the correction --
while simultaneously recording it as `NOT INDEPENDENTLY VERIFIED by this pass`, taken second-hand from
`provenance_judgment_class_literature_tranche.md` section 3.3. If the paper did not say what the notes say it
says, INV-107's form would be wrong. It says it.

The citation is exact: *Cognition* 204:104343, doi 10.1016/j.cognition.2020.104343, PMID 32599310, authors
Pilditch, Hahn, Fenton and Lagnado. The abstract states the thesis in almost the words INV-107's notes use:
dependencies between experts, group members or evidence "have traditionally been seen as a form of
redundancy", and "this conception of dependence conflates the structure of a dependency network, and the
observations across this network". By disentangling the two, the authors show by mathematical proof and
worked examples "that there are cases where dependencies yield an informational advantage over independence"
-- specifically, when a structural dependency exists but the observations across it are partial or
contradicting, those observations support the hypothesis *more* than they would absent the dependency.

The consequence for REE is precise and worth restating, because it is the kind of thing that erodes into its
opposite over a few sessions of paraphrase. The intuitive rule -- a hypothesis must not cite its own
descendants as independent witnesses -- reads naturally as an instruction to discount, and from there to
collapse a lineage to one vote. That reading is provably wrong. Dependency structure is information, and
collapsing it throws that information away; the correct response is to *represent* dependency and condition
on it, which is what INV-107 actually requires and what MECH-553's compressed causal genealogy is proposed to
supply. The negative form is therefore not timidity about a strong claim; it is the strongest form that
survives the proof.

The operational consequence is a scoring requirement, and it is the part most likely to be lost. Any
successor experiment must score over-discounting as a failure, not only under-discounting. A scoring set
assembled entirely from redundant-dependence cases makes "discount everything dependent" the winning strategy
and will report a false winner -- a system that has learned nothing about dependency structure will top the
leaderboard. INV-107's notes already say this; the paper is what makes it more than a stylistic preference.
The P6 rung of the provenance ladder, where explicit genealogy is compared against lineage-free dependency
estimation, is the place this bites hardest.

Confidence 0.72, the highest in this pass, and the reasoning is worth being explicit about since it inverts
the usual pattern. This is a formal result rather than an empirical effect, so it carries no replication risk
and does not decay; mapping fidelity is unusually high because INV-107's form was derived from this exact
distinction rather than merely decorated with it. What holds it below 0.8 is that no formal result can
establish that REE *needs* the invariant -- it constrains the invariant's form, which is a different and
narrower service. The paper's third finding, that lay reasoners endorse the underpinning assumptions while
failing to apply them, is recorded as a failure signature rather than leaned on: it is a warning that human
intuition is not a safe oracle for calibrating a dependency-aware combiner.
