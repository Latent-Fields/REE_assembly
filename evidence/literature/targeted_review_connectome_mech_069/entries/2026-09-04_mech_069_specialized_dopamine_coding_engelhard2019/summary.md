# Engelhard, Finkelstein, Cox et al. (2019) -- "Specialized coding of sensory, motor and cognitive variables in VTA dopamine neurons"

## What the paper did

Engelhard and colleagues asked the question this literature gap most needs answered directly: is the population of midbrain dopamine neurons a homogeneous broadcaster of one scalar reward-prediction-error (RPE) signal, or does it carry genuinely differentiated information? Rather than argue the point, they measured it -- two-photon calcium imaging through an implanted lens recorded activity from over 300 individual VTA dopamine neurons in mice navigating a complex virtual-reality decision task that required tracking position, velocity, upcoming choices, and reward outcomes simultaneously.

## Key findings relevant to MECH-069

The population is not uniform. Dopamine neurons encoded an array of sensory, motor, and cognitive variables beyond reward itself, and this encoding was not randomly distributed across the population -- it clustered functionally, such that identifiable subpopulations preferentially carried information about particular variable classes. Critically, these functional clusters were also *spatially* organized within VTA, and this spatial organization aligned with known projection topography (which downstream striatal/cortical target a given dopamine neuron's axon reaches). That is a structural, anatomically-grounded form of channel separation, not merely a statistical curiosity in a population-average signal.

## Translation to REE

MECH-069's strong claim is that REE's E1 (sensory-prediction error), E2 (motor-sensory error on z_gamma), and E3 (harm/goal error) are incommensurable and must be kept as structurally distinct learning channels. Engelhard et al. do not test that three-way partition directly -- their task had no aversive/harm dimension at all, so E3 is simply untested here -- but they do establish the necessary precondition: the brain's actual dopaminergic teaching-signal machinery is capable of, and in this case demonstrably does, depart from the textbook single-scalar-RPE model in favor of functionally specialized, anatomically-organized subchannels. This is exactly the kind of measurement (not argument) the EXT-003 pull's caveat asked for.

## Limitations and caveats

Two limits keep this from being direct confirmation. First, most individual neurons here are multiplexed -- they carry weighted mixtures of several variables rather than pure single-error-type signals, so "specialization" is a population/clustering phenomenon, not a clean per-neuron trichotomy the way MECH-069's three-loop architecture would want. Second, and more importantly for REE's specific claim, this paradigm is reward-only: there is no punishment or harm-avoidance condition, so the paper is silent on whether a harm/goal-error channel (E3) is dissociable from the sensory/motor variables it does measure.

## Confidence reasoning

High source quality (Nature, large single-unit sample, sophisticated task design) earns this a strong evidentiary weight for the general proposition that dopaminergic teaching signals are structured and heterogeneous rather than one broadcast signal differentially read out. Mapping fidelity to REE's specific E1/E2/E3 cut is only moderate given the multiplexing and the missing harm dimension, which is why this is tagged `mixed` rather than a clean `supports` -- it moves the needle toward MECH-069 without confirming its exact shape.
