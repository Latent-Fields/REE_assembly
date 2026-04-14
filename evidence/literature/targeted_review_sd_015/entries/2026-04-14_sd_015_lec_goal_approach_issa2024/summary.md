# Lateral entorhinal cortex subpopulations represent experiential epochs surrounding reward
**Issa, Radvansky, Xuan & Dombeck (2024) | Nature Neuroscience | doi:10.1038/s41593-023-01557-4**

## What the paper did

Issa and colleagues used two-photon calcium imaging with a microprism preparation to record from LEC, MEC, and CA1 neurons simultaneously in head-fixed mice navigating a 1D virtual reality linear track. The core manipulation was to move the reward location mid-session, allowing the authors to dissociate neurons encoding absolute spatial position (which would maintain their firing location) from neurons encoding reward-relative or goal-relative position (which would shift with the reward). They then used optogenetic inhibition of LEC during learning of the new reward location to test whether LEC is causally necessary for flexible goal-directed navigation.

## Key findings relevant to SD-015

The LEC contained three functionally distinct populations: pre-reward cells that ramped up during goal approach, reward-consumption-active (RCA) cells that fired transiently at reward delivery, and post-reward cells that activated after consumption. Critically, when the reward location moved, approximately half of these cells immediately shifted their firing to be reward-relative at the new location -- they tracked the goal, not the map. MEC cells, by contrast, maintained their absolute spatial position coding. LEC inhibition selectively impaired learning of the new reward location (measured by the animal's behavioural slowing and licking selectivity), without affecting performance at the already-learned location.

The authors interpret LEC as providing reward-centric "what" information to complement MEC's spatial "where" information. This is the biological instantiation of the argument SD-015 is making: you cannot navigate flexibly to a goal by relying only on the spatial map, because the map encodes "where the resource was" not "what kind of resource to seek." The LEC goal-approach population encodes the latter -- it fires in anticipation of reward regardless of where in the environment that reward currently sits.

## The REE translation

For CausalGridWorld, resources respawn at random locations each episode. An agent that relies on z_world to represent "this is where food was" will fail when food respawns elsewhere -- the location is uninformative about resource type. An agent with a dedicated z_resource encoder that responds to object-type features (the food's visual signature) independent of its spatial coordinates can approach correctly regardless of respawn location. The LEC pre-reward population is the neural analogue: it provides a goal-type signal that shifts immediately when the goal relocates, rather than being anchored to the spatial map.

The hippocampal module then receives both z_resource (goal-type signal, LEC-like) and z_world (spatial context, MEC-like), binding them into the episodic object-place representation needed for efficient navigation. This is exactly the architecture SD-015 proposes.

## Limitations and caveats

The study uses a single reward type in a one-dimensional environment. LEC "goal-approach" cells in this context encode reward approach generally -- there is no test of whether LEC distinguishes between multiple distinct goal types (food vs. water vs. novel object). SD-015's z_resource encoder must perform this multi-type discrimination, which is a stronger requirement than the current study tests. It remains an open question whether distinct LEC subpopulations encode different reward types, or whether object-type discrimination is achieved at an earlier stage (IT cortex, perirhinal cortex) before the signal reaches LEC. The 1D virtual track also limits generalization to the 2D navigation problem in CausalGridWorld.

## Confidence reasoning

Source quality is high: simultaneous multi-region imaging, large cell counts, clean within-session reward relocation control, and causal optogenetics. The directional support for SD-015 is solid -- reward-relative rather than position-relative LEC coding is directly observed, and LEC is shown necessary for flexible goal updating. Confidence is 0.76 rather than higher because the single-reward-type design leaves the multi-category discrimination question open, and the 1D-to-2D transfer carries some risk.
