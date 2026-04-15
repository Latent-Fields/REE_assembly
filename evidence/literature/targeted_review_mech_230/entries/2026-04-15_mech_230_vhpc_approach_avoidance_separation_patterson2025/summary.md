# MECH-230 Literature Entry: Patterson et al. 2025

**Entry ID:** 2026-04-15_mech_230_vhpc_approach_avoidance_separation_patterson2025
**Claim:** MECH-230 -- z_goal as structured positive attractor distinct from harm avoidance
**DOI:** https://doi.org/10.1371/journal.pbio.3002722

---

## What the paper did

Patterson and colleagues (2025) investigated the circuit mechanisms underlying approach-avoidance conflict (AAC) -- the situation where an agent faces simultaneous signals of reward and punishment and must decide whether to approach or avoid. Prior work had implicated the ventral hippocampus (vHPC) as a key node in AAC arbitration, but the specific output pathway had not been causally dissected. They used pathway-specific chemogenetics in male and female Long-Evans rats to inhibit the vCA1-to-nucleus accumbens (NAc) shell projection while animals underwent an AAC test presenting concurrent positive and negative valence cues. Additional assays controlled for pure avoidance, anxiety, and social preference to isolate the specific contribution of this pathway.

## Key findings relevant to MECH-230

The central finding is a double dissociation: inhibiting the vCA1-NAc shell circuit increased avoidance bias and decision latency specifically during motivational conflict, but had no effect on pure avoidance or on anxiety-like behavior. This means the pathway is not a general fear/avoidance circuit but specifically encodes the *approach bias* during conflict -- the signal that tips the balance toward approach when both reward and punishment are simultaneously present. A secondary finding was that the same pathway was required for approach to social novelty, suggesting it encodes approach motivation more broadly, not only in contexts of explicit conflict.

## REE translation

MECH-230 requires that z_goal (the positive approach attractor) is distinct from z_harm (avoidance signal) within E3's latent space, and that this distinction enables navigation toward goals even in the presence of harm signals. Patterson et al. provide circuit evidence that this separation is biologically real: the hippocampus outputs approach-biasing information through a dedicated pathway (vCA1-NAc shell) that is dissociable from avoidance circuits. In REE terms, the vCA1-NAc shell pathway is the biological analogue of z_goal's downstream influence on action selection -- a positive approach signal that competes with z_harm rather than being subsumed by it.

The motivational conflict finding is particularly relevant to REE's experimental context. The EXQ-085 series failed to produce z_goal_norm > 0.1, suggesting that without SD-012 drive, z_goal collapses toward zero and cannot compete against z_harm. Patterson et al.'s observation that vCA1-NAc inhibition defaults the animal to avoidance in conflict conditions provides a behavioral prediction for what REE should look like when z_goal fails: not random behavior, but avoidance bias, because z_harm without a competing z_goal produces asymmetric behavior.

## Limitations and caveats

The paper demonstrates a *pathway-level* separation -- approach is channeled through vCA1-NAc shell, avoidance through other circuits. This is circuit-level evidence for the separation MECH-230 requires, but it does not directly show that z_goal and z_harm occupy geometrically distinct sub-spaces within hippocampal internal representations. The separation may be entirely at the output projection level, with internal hippocampal encoding remaining valence-agnostic.

A further caveat is the motivational source. This study uses conditioned approach and avoidance signals (learned cue-outcome associations) plus innate anxiety/social preference. MECH-230's goal representation is seeded by homeostatic drive (SD-012), a different motivational architecture. Whether drive-seeded goals produce the same vCA1-NAc pathway engagement as externally conditioned reward cues is an open question.

## Confidence reasoning

Confidence is set at 0.58 (mixed). The paper provides real and relevant evidence that approach and avoidance are separated at the hippocampal output level, which is necessary but not sufficient for MECH-230. It supports the distinctness requirement indirectly but cannot confirm the latent sub-space geometry the claim specifically requires. The mixed direction reflects that the paper simultaneously supports the approach/avoidance separation component of MECH-230 while being agnostic about (and therefore not confirming) the positive attractor structure in the internal representational space. Combined with Naude et al. 2024 and Muhle-Karbe et al. 2023, this paper completes the evidential picture: structured goal attractor (Naude), compressed goal geometry in hippocampus/OFC (Muhle-Karbe), and circuit-level approach/avoidance separation at hippocampal output (Patterson).
