# Pessoa & Adolphs 2010 — From a "low road" to "many roads"

Where Méndez-Bértolo 2016 provides the millisecond-resolution affirmative evidence, Pessoa & Adolphs 2010 is the prior review that sets the boundary conditions on what the fast route can and cannot be. It is not an anti-low-road polemic, though it is sometimes read that way — it is a careful synthesis arguing that the strong form of the classical low-road claim (a privileged, fast, pre-cortical route that drives amygdala responses to unseen threat stimuli, often without cortical involvement) is poorly supported in primates on anatomical and single-unit grounds. The pulvinar-amygdala projection they review is sparse and not obviously fast; single-unit amygdala responses in macaque are latency-wise not dramatically shorter than cortical responses; and lesion/fMRI evidence for pure subcortical processing is weaker than early reports suggested.

Their alternative is "many roads": the amygdala receives biologically-relevant information through multiple cortical and subcortical streams, and its role is less of a privileged detector and more of a coordinator of cortical evaluation. This is the framing we actually want in REE. It tells us that MECH-046 (CeA mode_prior) and MECH-074c (fast_prime) must exist, but must not dominate. The CeA analogue should bias the SalienceCoordinator; it should not be wired so that a single CeA spike commits the agent to a defensive action irrespective of downstream cortical evidence.

Reading this paper alongside Méndez-Bértolo 2016 gives us the bracket. Méndez-Bértolo shows the fast route is real and has a ~75 ms latency advantage for a narrow stimulus class (low-spatial-frequency fearful faces via magnocellular inputs). Pessoa & Adolphs remind us that outside that narrow class, the route is weak, and the amygdala's functional role is coordinative rather than executive. In REE terms: build the fast route, calibrate its bias magnitude to be meaningful but overridable, and ensure cortical (AIC/dACC) analogues can outvote CeA once they finish integrating. The many-roads framing is a direct match for REE's multi-gate SalienceCoordinator.

One implementation consequence: if we build CeA as a unilateral actor — its output directly gates motor pathways — we will reproduce exactly the architecture Pessoa & Adolphs argue against. The correct design, consistent with both papers, is that CeA biases a coordinator that also takes cortical inputs, and CeA bias decays if not confirmed by cortical signals within a bounded window.

## Quantitative defaults for CeAAnalog config

- **Override window**: cortical (AIC/dACC) analogues must be able to override CeA `fast_prime` within ~5-10 sim steps (~300-400 ms biological). After this window, if cortical confirmation is absent, `fast_prime` decays toward baseline.
- **Bias magnitude ceiling**: `|fast_prime_max|` ≤ max cortical AIC/dACC log-odds adjustment — not dominant.
- **Decay time constant**: ~3-5 sim steps (~150-250 ms) if unconfirmed.
- **No direct motor gating**: CeA writes only to SalienceCoordinator.
- **Gating placement**: pre-softmax additive log-odds bias on harm channel.
