# Arousal that sets the learning rate: pillar three confirmed, prohibition two strained

Nassar and colleagues put human subjects in a predictive-inference task where a noisy process
occasionally changes its underlying state, so that rational behaviour requires continuously
assessing two things: how unstable the process is, and how reliable recent data are as evidence
about its current state. They then asked what pupil diameter -- with luminance effects removed --
tracks. The answer was both quantities. Brief pupil changes reflected assessed instability;
baseline diameter reflected the reliability of recent data and individual differences in
expectations about how often the world changes. Crucially, the two metrics together predicted how
much influence new data had on subsequent inference. And then they went further than correlation:
a task- and luminance-independent manipulation of pupil diameter predictably altered that
influence.

Read against MECH-005's third pillar, this is close to a direct confirmation. The claim holds that
nu modulates how much post-commit error propagates upward -- high nu and errors drive theta-level
restructuring, low nu and they are damped and treated as noise. Nassar shows an arousal signal
doing exactly that gating in humans, and shows it with a manipulation rather than an observation.
Of everything in this pull, this is the closest thing to causal evidence that a noradrenergic-proxy
signal sets how strongly incoming error reshapes the model.

Read against the claim's prohibitions, the same finding is the sharpest challenge in the pull. The
quantity being set here is the weight on new evidence in belief updating. In predictive-processing
vocabulary that is a precision term. MECH-005 says nu does not update precision registers, and the
design rationale is emphatic: "any architecture where stress or surprise directly rewrites
confidence is already collapsed." Nassar reports approximately that architecture running in healthy
humans, and running well -- adaptively, normatively, rationally. The baseline finding compounds it:
if tonic arousal encodes an expectation about the rate of environmental instability, then nu
carries a belief about the world, not merely an allocation of urgency.

I have filed this as mixed, and I want to be clear that this is not indecision. The pillar it
supports and the prohibition it strains are the same result described at two levels. An
implementation cannot take the support and discard the challenge, because they are the same
mechanism. What REE has to decide is whether the fragmentation of precision from path authority is
an architectural commitment worth defending against this evidence, or a distinction that dissolves
on contact with it. That is a governance question, not a literature question, and it should be put
to MECH-005 explicitly rather than left implicit.

Two limits keep confidence at 0.63. The task has no commitment structure -- subjects predict, they
do not act irreversibly -- so "post-commit" in REE's sense is not instantiated at all, and the
privileged status of after-action error remains untested. And pupil is a multi-determined proxy:
acetylcholine, superior colliculus and effort all contribute, the manipulation moved pupil rather
than LC firing, and a dissociation between pupil and direct LC recording would reopen rather than
resolve the precision conflict.
