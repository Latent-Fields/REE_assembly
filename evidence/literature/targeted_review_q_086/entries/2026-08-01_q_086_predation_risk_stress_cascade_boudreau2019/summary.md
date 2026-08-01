# Boudreau et al. (2019) -- Experimental increase in predation risk causes a cascading stress response in free-ranging snowshoe hares

**What the paper did.** The authors ran a genuine field experiment (not a
correlational study) manipulating predation risk in free-ranging snowshoe hares
over two consecutive summers, simulating natural predator chases with a model
predator. Hares were monitored intensively by radio-telemetry, and a suite of
physiological assays tracked stress hormones (plasma cortisol, cortisol-binding
capacity), immune markers (neutrophil:lymphocyte ratio), and metabolic indices
(glucose), alongside two independent whole-organism condition indices.

**Key findings.** Risk-augmented hares showed a robust, graded physiological
stress cascade relative to controls: 25.8% higher free plasma cortisol, 15.9%
lower cortisol-binding capacity, a greater neutrophil:lymphocyte skew, and a 10.4%
increase in glucose -- a clean demonstration that manipulated predation-risk
intensity produces a measurable, scaling physiological stress response in a wild,
chronic-exposure setting. But despite this physiological shift, neither condition
index differed between risk-augmented and control hares across the study period.
The authors attribute this to compensatory foraging and/or metabolic adjustment
that buffered the animals' overall state even as their internal stress physiology
moved.

**How this maps to Q-086.** Of the sources pulled for this claim, this is the
closest real-world analogue to REE's actual manipulation: predation-risk intensity
manipulated in a chronic, ecological setting, with a physiological readout
measured for response. Its headline finding directly weakens any strong prior
that "ecological tracking" is an implausible or merely hopeful reading of z_harm_a
saturation -- a physiological signal genuinely CAN and DOES scale with
predation-risk manipulation in the wild. That is disconfirming evidence against a
pure calibration-pathology story taken as the default explanation. But the more
interesting result for Q-086 is the dissociation the paper reports: the
physiological signal rose while whole-organism condition did not. That is direct
evidence that a rising internal stress/affective readout is not automatically the
same claim as the organism's true fitness-relevant state degrading in step. Q-086
implicitly treats "does the affective signal track hazard density" and "is the
organism's true suffering/degradation state tracking hazard density" as one
question; this paper shows they can and do dissociate in a real system, via
compensation. For REE, that suggests z_harm_a's saturation could be neither pure
calibration pathology nor pure faithful chronic-suffering tracking, but a third
regime: a physiological/affective signal correctly rising with the manipulation
while the agent's downstream functional state is buffered by some other
mechanism (in REE's case, plausibly policy adaptation rather than metabolic
compensation). This is why the entry is scored "mixed" rather than a clean
support for either side of Q-086's framing.

**Limitations and caveats.** This is one species over two field seasons, comparing
a risk-augmented group to controls rather than tracing a graded dose-response
curve across multiple discrete hazard-intensity levels the way REE's num_hazards
manipulation does. The physiological measures are endocrine and immune (cortisol,
cortisol-binding capacity, neutrophil:lymphocyte ratio, glucose), not neural or
representational -- so this speaks to whether ecological tracking of hazard
intensity is physiologically plausible in principle, not to whether REE's specific
z_harm_a/z_harm_s two-tier architecture implements it correctly or where the
saturation actually originates. The domain transfer from wild mammal predation
physiology to an RL agent's internal scalar harm signal is substantial and should
be weighted accordingly.

**Confidence reasoning.** Source quality is high: this is a genuine field
experiment with intensive telemetry monitoring and direct manipulation of the
variable of interest, published in a strong ecology journal (Oecologia).  Mapping
fidelity is moderate: the ecological logic (a physiological signal tracking
manipulated risk in a wild, chronic setting) is the closest available real-world
analogue to REE's environment manipulation, but the readout modality differs
substantially from REE's internal scalar signal. Transfer risk is moderate given
the wild-mammal-to-artificial-agent gap. Net confidence 0.60, direction "mixed":
it is genuine disconfirming evidence against dismissing ecological tracking as
implausible, while simultaneously complicating the naive version of that reading
by showing physiological signal and organism-level state can dissociate under
compensation.
