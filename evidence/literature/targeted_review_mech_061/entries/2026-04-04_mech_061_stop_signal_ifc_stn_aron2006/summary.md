# Summary: Aron & Poldrack (2006) — IFC-STN Circuit for Commitment Enforcement

**Source:** Aron AR, Poldrack RA. Cortical and Subcortical Contributions to Stop Signal Response Inhibition: Role of the Subthalamic Nucleus. *Journal of Neuroscience*, 26(9), 2424-2433.

## The Question They Were Asking

When a motor command has been issued but circumstances change, how does the brain cancel it? And where in the cortico-subcortical circuit does this cancellation happen? Aron and Poldrack used the Stop Signal Task — in which participants respond to Go stimuli and occasionally receive a Stop signal to cancel their response — combined with fMRI to identify the neural circuitry of response inhibition. Their specific hypothesis was that the subthalamic nucleus (STN), positioned to broadcast broadly across basal ganglia output nuclei, might play a key role in suppressing an already-initiated response, via a hyperdirect pathway from cortex.

## What They Found

Going activated the expected direct pathway nodes: frontal motor areas, striatum, globus pallidus, and motor cortex. Stopping selectively activated right inferior frontal cortex (IFC) and the subthalamic nucleus (STN). The proposed mechanism is that right IFC rapidly recruits STN via a hyperdirect cortico-subthalamic projection; STN then applies broad excitation to the globus pallidus, which suppresses thalamocortical output, reducing activation in motor cortex and canceling the response. The critical architecture is the competition between two pathways: the go (direct striatal) pathway, which releases the motor plan, and the stop (hyperdirect IFC-STN) pathway, which suppresses it. Whether the action is committed or cancelled depends on which pathway wins the race.

## Why This Matters for MECH-061

The IFC-STN circuit is the neural enforcement mechanism for the commit boundary. MECH-061 posits a boundary that, when crossed, is irreversible -- and this paper provides the mechanistic account of how that irreversibility is implemented. Before the boundary: both the go pathway and the stop pathway are active; the stop pathway can still win the race and cancel the action. After the boundary: the go pathway has established irreversible dominance; STN-mediated suppression can no longer overcome the motor command that is already in execution. The commit boundary in MECH-061 is, at the neural circuit level, precisely the moment when the go pathway's activation exceeds the stop pathway's cancellation capacity. After that point, the reclassification MECH-061 describes follows structurally: the agent is now in the domain of realized outcomes rather than revisable predictions.

What the Aron & Poldrack architecture adds is specificity about the circuitry involved in commitment enforcement, which complements the other entries in this review. Schultze-Kraft et al. locate the boundary temporally; Thura & Cisek characterize its cortical signature; Michelet et al. demonstrate its effect on error routing. Aron & Poldrack explain why it is hard: the go pathway and stop pathway are in direct competition, and past a certain activation level, the go pathway's momentum cannot be reversed. This is not a design choice of the architect but a consequence of the basal ganglia's circuit topology.

## Honest Uncertainty

The paper addresses response inhibition under external Stop signals, not internally generated commitment. MECH-061's boundary arises from the agent's own deliberation reaching a conclusion, not from an external interruption signal. The circuits may overlap but the triggering mechanism is different: IFC-STN is recruited reactively in response to a perceived need to stop, whereas the commit boundary in REE is generated proactively by the planning system. Whether the same STN suppression pathway mediates both is plausible but not shown.

The fMRI temporal resolution is also a genuine limitation here. Response inhibition unfolds in hundreds of milliseconds; the 1-2 second TR of typical BOLD imaging blurs the temporal dynamics that would be needed to characterize the race between go and stop pathways in detail. The Aron & Poldrack paper tells us which regions are involved more than it tells us the precise temporal dynamics of the race — and it is the temporal dynamics that matter for understanding exactly where the point of no return falls.
