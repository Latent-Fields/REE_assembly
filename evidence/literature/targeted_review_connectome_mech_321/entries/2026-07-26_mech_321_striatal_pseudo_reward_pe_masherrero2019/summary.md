# Striatal pseudo-reward prediction errors bias choice (Mas-Herrero et al. 2019)

**Claim tested:** MECH-321 (policy_decomposition_via_event_segmenter)
**Direction:** mixed · **Confidence:** 0.60

## What the paper does

Hierarchical reinforcement learning buys tractability by decomposing complex action sets into subgoals, and it pays for that decomposition with *pseudo-rewards* — internally generated reinforcement signals attached to subgoal attainment, which allow actions leading to a subgoal to be reinforced before the final goal is reached. The pseudo-reward prediction error (PRPE) is the credit-assignment currency of the decomposition.

Mas-Herrero and colleagues asked whether that currency is free. They built a decision-making paradigm that dissociates ordinary reward prediction errors from PRPEs, and ran it as an fMRI study (n=20) plus a separate behavioural study (n=19). Two results. Behaviourally, participants developed a preference for the most pseudo-rewarding option **even though it did not lead to more monetary reward**. Neurally, the size of that preference was predicted by individual differences in the relative striatal sensitivity to PRPEs versus real RPEs. Pseudo-rewards, in short, generate genuine learning signals in the striatum, and those signals distort choice in the absence of any advantage.

## Why this matters for MECH-321

The entire ARC-070 parent literature set is about how decomposition *helps* — Zacks on segmentation, Schapiro on complementary learning systems, Badre & D'Esposito on rostro-caudal hierarchy, McGovern & Barto on subgoal discovery. That is a one-sided evidence base for a mechanism REE is about to build, and it is the kind of one-sidedness that produces a substrate whose failure modes are discovered experimentally rather than anticipated.

This paper supplies the missing side. It says: if you decompose, and if decomposition entails assigning credit at subgoal grain, the agent acquires a taste for subgoals as such. It will prefer trajectories dense in subgoal completions over trajectories that actually pay. That is a specific, measurable, pre-registrable prediction about a MECH-321-equipped agent, and it is far more useful to have it written down before the substrate lands than after.

I want to flag one structural aspect of the failure mode, because it bears on the depth cap. The bias scaled with how strongly the striatum weighted PRPEs relative to RPEs — it is not a fixed offset you calibrate away once. In REE terms, an operator that fires more readily (a lower V_s threshold, or a deeper permitted recursion) generates more subgoals, hence more subgoal-grain credit, hence more subgoal-seeking. The depth cap of 3–4 that MECH-321 inherits from Badre & D'Esposito and Koechlin & Summerfield bounds recursion *depth*, but does not obviously bound this feedback path, since a shallow decomposition applied often produces plenty of subgoals. That is worth a look at design-refinement time.

## Where the mapping breaks

The honest caveat is substantial and I would not want this entry read without it. **MECH-321 as registered does not mint pseudo-rewards.** Its trigger is a V_s drop or boundary fire on the chunk's region; its output is a re-segmented rollout proposal stream. Segmentation and credit assignment are separable, and the paper's finding bites only if decomposition also moves credit to subgoal grain. Whether it does is precisely one of the implementation choices still open at substrate-landing time. If MECH-321 lands as pure segmentation with credit assignment held at the terminal objective, this failure mode does not arise and this entry becomes near-irrelevant to the claim. That conditionality is the reason mapping fidelity sits at 0.65 rather than higher, and it should be recorded as a design question the substrate work has to answer explicitly rather than by default.

Two smaller reservations. The paradigm delivers *explicit* pseudo-reward feedback; it is possible the bias is a response to salient externally-marked subgoal completion rather than to internally generated segmentation, in which case the transfer to REE's implicit boundary pulses is weaker than it looks. And the neural half of the result is an individual-differences correlation at n=20, which is not a sample size at which I would want to lean hard on a brain–behaviour correlation. The behavioural preference effect, replicated in a second sample, is the sturdier finding.

## Confidence reasoning

I have set this at 0.60 and marked it **mixed** rather than supports or weakens, which is the honest reading: it confirms that the subgoal-grain machinery MECH-321 presupposes is real and consequential in brains, while showing that its consequences include a maladaptive one. Source quality (0.72) is helped by the behavioural replication and held down by the fMRI sample. Mapping fidelity (0.65) is capped by the segmentation-versus-credit gap described above. Transfer risk (0.40) reflects that human monetary decision-making and REE rollout decomposition share an abstraction rather than a mechanism.

The most valuable thing in this entry is not the confidence number — it is the three failure signatures. They are the falsifiers to instrument when MECH-321's substrate is built.
