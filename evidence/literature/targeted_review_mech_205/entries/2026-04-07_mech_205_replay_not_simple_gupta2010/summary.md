# Hippocampal Replay Is Not a Simple Function of Experience

**Gupta, van der Meer, Touretzky & Redish, 2010, Neuron**

## What the paper does

Gupta et al. recorded hippocampal place cells in rats navigating a multiple-T maze and analysed SWR-associated replay sequences during rest periods. The critical question: does replay merely recapitulate experienced trajectories, or can it construct novel ones?

## Key findings relevant to MECH-205

The headline result is that rats replayed shortcut trajectories they had never actually traversed. These shortcuts were composed by combining a forward replay segment from one experienced trajectory with a backward replay segment from another, creating a spatially coherent but never-experienced path. The probability of these shortcuts arising from chance alignment of independent forward and reverse replays was extremely low -- these are genuine novel constructions.

This is the most direct empirical evidence for MECH-205's claim that hippocampal replay is *generative*. The hippocampus is not simply re-presenting cached episodes; it is recombining elements to construct counterfactual trajectories. In REE terms, this is E2 running counterfactual rollouts during offline phases -- "what if I had gone this way instead?"

## Mapping to REE

The shortcut sequences map onto MECH-205's counterfactual variations: the hippocampus generates nearby trajectories around experienced episodes, expanding the training set for the forward models beyond what was directly experienced. This is precisely the mechanism by which offline replay could train SD-003 attribution capacity -- by generating counterfactual action sequences and comparing their predicted outcomes.

The limitation is that Gupta et al. do not test whether surprise drives the generation of these novel sequences. The shortcuts may be generated because of spatial proximity and trajectory overlap, not because the original experience was surprising. MECH-205 claims both surprise-gating AND generative variation; this paper provides strong evidence for the latter but is silent on the former.

## Limitations

Rodent spatial navigation only. The generative sequences observed are spatial shortcuts -- a specific type of recombination driven by the spatial structure of the maze. Whether the same generative mechanism operates for non-spatial, affect-laden episodes (e.g., surprising harm events, which are central to MECH-205's connection to the residue field) is unknown.

## Confidence reasoning

Landmark paper in the replay literature; strong electrophysiology with rigorous statistical controls for chance alignment. High mapping fidelity for the generative aspect; silent on the surprise-gating aspect. Overall confidence 0.78.
