# Treadway & Zald (2011) -- Reconsidering Anhedonia in Depression

## What the Paper Did

Treadway and Zald made the argument that anhedonia -- one of the two cardinal symptoms of major
depression alongside low mood -- has been systematically underspecified in both research and
clinical practice. The conventional operationalisation conflates two computationally and
neurobiologically distinct phenomena: consummatory pleasure (the hedonic experience of reward
when it occurs) and motivational drive (the prospective orientation toward reward that generates
approach behaviour). The preclinical literature, they argue, is unambiguous: dopamine is
primarily involved in the motivational, not the hedonic, component. Opioid systems mediate
hedonic experience. These are doubly dissociable. In depressed patients, the dominant deficit
is motivational: reduced willingness to invest effort for outcomes, impaired effort-cost-benefit
analysis, reduced goal-directed approach -- with consummatory pleasure that may be largely
intact when the patient is actually confronted with a reward. The paper introduces the term
"decisional anhedonia" to capture the downstream effects of this motivational collapse on
reward-seeking behaviour.

## Key Findings

The paper's core empirical claims are: (1) dopamine depletion in animals and humans impairs
effort allocation for reward without abolishing hedonic experience; (2) depressed patients
show disproportionate reductions in willingness to exert physical and cognitive effort for
rewards relative to controls; (3) this effort-based deficit is the most sensitive assay for
detecting motivational anhedonia and distinguishing it from hedonic anhedonia; (4) the neural
substrate is distinct -- OFC/striatum for hedonic coding, anterior cingulate/prefrontal cortex
for effort and cost-benefit computation. The clinical implication is that anhedonia-targeted
therapies must address motivational systems, not merely pleasure systems, and that current
rating scales (which ask about experienced pleasure) are systematically insensitive to the
motivational deficit.

## REE Mapping

This paper provides the behavioural-science grounding for INV-053 at exactly the right
conceptual level. REE's architectural distinction between z_goal (wanting, prospective approach
gradient) and benefit_eval_head (liking, hedonic calibration signal at receipt) is a
computational instantiation of Treadway and Zald's neurobiological distinction. The INV-053
attractor state -- VALENCE_WANTING collapsed, z_goal absent, HABIT/PLANNED equivalent -- is
the computational model of decisional anhedonia. The patient who can still experience pleasure
when placed directly at a reward but will not invest effort to seek reward is the clinical
face of z_goal seeding failure with intact benefit_eval_head function.

The paper also illuminates why the Huys/Dayan Q-value lineage describes a different patient
profile. A patient with a helplessness prior or pruning failure is still generating approach
drives and evaluating them poorly. A patient with motivational anhedonia has stopped generating
the approach drives. Treadway and Zald's wanting/liking distinction is the clinical key to
separating these two types of computational failure.

## Limitations and Caveats

The paper does not provide a computational model of how motivational collapse occurs -- it
identifies the phenomenon and its neural substrates but does not specify the mechanism.
REE fills this gap: benefit_exposure below the SD-012 seeding threshold prevents z_goal
formation, which collapses VALENCE_WANTING terrain. The paper also focuses on the acute
motivational deficit rather than the chronicity and self-maintenance that INV-053 specifically
claims (closed negative feedback loop via INV-054). That claim requires additional grounding
in the effort-allocation and behavioural-activation literature.

The dopamine framing in the paper is a specific neurobiological claim that REE does not
depend on: REE's mechanism (benefit_exposure threshold, z_goal seeding, terrain dynamics)
is substrate-independent, with serotonin as one possible tonic regulator (MECH-186/187/188).
The mapping from paper to claim does not require accepting dopamine as the sole or primary
mechanism.

## Confidence Reasoning

Strong source quality, high mapping fidelity for the wanting/liking dissociation and
decisional anhedonia concepts. Transfer risk is low because the behavioural signature maps
directly to REE's architecture. Confidence 0.72 reflects the paper's role as direct empirical
grounding for the wanting/liking dissociation that underlies INV-053, discounted for the
absence of a computational mechanism and for the paper's focus on the acute deficit rather
than chronicity.
