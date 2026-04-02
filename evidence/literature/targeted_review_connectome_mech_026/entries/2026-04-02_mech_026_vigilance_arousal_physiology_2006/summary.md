# Oken et al. (2006) — Vigilance, Alertness, or Sustained Attention: Physiological Basis and Measurement

## What the paper does

Oken, Salinsky, and Elsas review the physiological substrates of vigilance and arousal, drawing together EEG, autonomic, and neuromodulatory evidence. They establish that vigilance depends on ascending reticular activating system projections through the thalamus to cortex, critically modulated by the locus coeruleus-norepinephrine (LC-NE) system. A central finding: arousal (internal cortical activation state) and behavioral output (motor activity) are dissociable. An organism can be highly aroused — cortex activated, norepinephrine elevated, thalamocortical loops engaged — while producing minimal or no motor output. This is the physiological definition of vigilance.

## Relevance to MECH-026

MECH-026 claims ready vigilance primes restraint under high sensitivity without action. Oken et al. provide the physiological foundation: the brain has dedicated circuitry for maintaining high arousal while suppressing behavioral output. This is not passive — it requires active maintenance by the ascending arousal systems. The LC-NE system sets the arousal level; the thalamocortical loops sustain cortical sensitivity; and prefrontal inhibitory circuits suppress premature motor responses.

For REE, the key translation: ready vigilance is a real, metabolically costly, actively maintained neural state. It is not "the absence of action" — it is a specific configuration that the brain deliberately enters and sustains. REE's computational analogue (high precision weights + suppressed action selection) captures the functional profile but misses the active maintenance cost.

## The arousal modulation question

The LC-NE inverted-U curve is particularly relevant. At intermediate norepinephrine levels, the system is optimally vigilant — sensitive but not reactive. Too low, and signals are missed. Too high, and the system becomes hypervigilant, responding to noise. This has a direct implication for REE: the precision parameter in ready vigilance mode cannot simply be "set to maximum." There is an optimal sensitivity level, and exceeding it produces false alarms rather than better monitoring.

This connects to a broader question about whether REE needs an arousal-like state variable separate from the precision weights. Biological vigilance is modulated by a global neuromodulatory signal (norepinephrine) that affects all cortical processing simultaneously. REE's current architecture uses channel-specific precision weights (w_harm, w_goal via MECH-152). Whether vigilance needs a global arousal parameter in addition to these channel-specific weights is an open design question.

## Mapping caveats

The review is grounded in clinical neurophysiology — EEG signatures, pupil diameter, heart rate variability. REE has no physiological substrate, so the rich measurement tradition described here has no computational analogue. More fundamentally, biological vigilance has metabolic costs (it is tiring to maintain) and temporal dynamics (the vigilance decrement). REE's computational precision parameter has no fatigue and no cost. Whether this difference matters depends on whether the cost of vigilance is informationally relevant or merely a biological constraint.

## Confidence reasoning

Solid review in a respected clinical journal. The arousal-behavior dissociation finding directly supports MECH-026's core claim. Confidence moderated by the large gap between physiological measurement (EEG, autonomic) and computational architecture (precision weights), and by the unitary arousal treatment versus REE's potentially channel-specific sensitivity.
