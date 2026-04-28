# Jacobson, Hoyer, de Lecea (2022) -- Hypocretins as a translational integrator hub

## What the paper does

This is a major review in the *Journal of Internal Medicine* by three established figures in
the orexin/hypocretin literature, including de Lecea (one of the original co-discoverers of
hypocretin). It synthesises about twenty years of mechanistic and translational work since
the original 1998 reports, and frames the Hcrt system as a non-redundant arousal regulator
whose architectural signature is the *combination* of two features: it sits at a convergence
point for diverse internal-state inputs (circadian, metabolic, emotional valence, stress,
reward), and it projects broadly via excitatory peptide release to many downstream
arousal-relevant nuclei. The translational arc covers narcolepsy (Hcrt cell loss, the
pathognomonic lesion), insomnia (where the dual orexin receptor antagonists suvorexant,
lemborexant, and daridorexant are now licensed), and provisional applications in addiction
and neurodegeneration.

## Findings relevant to SD-037

The architectural-level claim in SD-037 is that the V3 control stack needs a third
regulatory layer alongside 5-HT (MECH-186/187/188, goal-pipeline gain) and GABA (SD-036,
cross-stream decay) -- specifically a small, broadly-projecting gain modulator that
integrates internal homeostatic state and threat context to produce an override_signal,
which then reweights z_harm at downstream commit gates and gates the SD-012
drive->z_goal seeding bridge.

Jacobson et al.'s description of the Hcrt system is, to a first approximation, the
canonical biological instance of exactly this architecture. They write that "the Hcrt
system is a hub that integrates diverse inputs modulating arousal (e.g., circadian
rhythms, metabolic status, positive and negative emotions) and conveys this information
to multiple output regions." This is essentially the SD-037 functional restatement. They
emphasise that the system is non-redundant -- which maps to SD-037's claim that GABAergic
decay alone (SD-036) is architecturally insufficient to break harm-stream lock-in under
sustained threat -- and that its lesion produces narcolepsy with cataplexy, which maps to
SD-037's predicted "lost override" phenotype: z_harm and drive_level continue to compute
normally but fail to integrate into coordinated behaviour.

## REE translation and mapping caveats

The translation to REE is direct at the architectural level but requires care at the
mechanism level. SD-037 commits to *reweighting* of z_harm at commit gates rather than
*silencing* it. Jacobson et al. describe Hcrt as a gain modulator on downstream targets,
which is consistent with reweighting but does not uniquely entail it -- one could read
their description as compatible with replacement rather than reweighting. The strongest
claim that survives the translation is the architectural one: the V3 control stack
benefits from an integrator-and-broadcaster layer whose lesion produces a
decoupling-rather-than-silencing phenotype, and biology has independently converged on
this design.

A second caveat: Hcrt biology has two receptor types (OX1R, OX2R) with partly dissociable
downstream effects. SD-037 currently commits to a unitary scalar override_signal; if V3
experiments expose phenotypes that require dissociable arms (e.g., one for
narcolepsy/cataplexy, one for hyperphagia/PWS), this would push toward a low-dimensional
override vector rather than a scalar.

## Confidence reasoning

I am setting confidence to 0.82. Source quality is very high (J Intern Med review by
domain leaders, peer-reviewed, well-cited). Mapping fidelity is high because the
integrator-hub-with-widespread-projections framing is explicit in the paper, not something
I am importing from outside. Transfer risk is moderate-low: the architectural-level claim
is well established across rodent and human work, and the paper itself is the synthesis.
I am holding back from 0.9 because the paper is narrative and does not separately test
the SD-037-specific commitment that the override REWEIGHTS rather than REPLACES downstream
harm signals -- that is a refinement that requires paired electrophysiology or
optogenetic-and-imaging data, not synthesis-level evidence.

The honest reading: this paper is the strongest available biological cover for the SD-037
architectural commitment, and the V3 design's appeal to an orexin-analog as the third
regulatory layer is licensed by it. But it does not constrain the parameters or the
specific reweighting mathematics; that work is the role of the existing parameter-anchoring
lit-pull (Mileykovskiy 2005, Lee 2005, Karnani 2020, Johnson 2012) and of the V3-EXQ-483
factorial validation series.
