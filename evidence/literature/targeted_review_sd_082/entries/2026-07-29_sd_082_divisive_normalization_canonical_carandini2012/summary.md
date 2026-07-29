# Normalisation as the canonical way to survive a common drive (Carandini & Heeger 2012)

Carandini and Heeger's review makes a simple structural argument: normalisation -- dividing a
neuron's response by a pooled factor summarising the activity of its neighbours -- shows up in so
many places that it is best understood as a canonical computation rather than a local trick. It was
developed for contrast responses in V1 and has since been invoked for odour representation,
attentional modulation, value encoding, and multisensory integration, across species from
invertebrates to mammals.

Why this bears on SD-082: normalisation is the brain's answer to exactly the problem SD-082
identifies. When a population receives a strong shared input, the individual responses run toward
their ceiling and the *differences* between them -- which is where the information lives -- get
crushed. Normalisation discounts the pooled component so the relative pattern survives, and it does
so in a way that also keeps responses inside their dynamic range. One operation, both jobs.

That is a satisfying match to the two changes SD-082 makes, and it is worth noticing that the match
covers the second change as well as the first. The hard clamp in the original SD-033a head does not
merely destroy the differential signal by railing every candidate to the same value; its flat region
also zeroes the REINFORCE gradient, so the head cannot learn its way out. Divisive gain control
bounds responses without ever having a flat region -- the bound is asymptotic, not a wall. The
scaled-tanh replacement is the same idea in a different algebra: same magnitude bound, gradient
preserved.

Here is the caveat, and it is the load-bearing one for this entry. The canonical computation is
*divisive*. SD-082 implements *subtractive* mean removal, then bounds separately. Those are not
interchangeable. Division rescales gain and preserves ratios between candidates; subtraction
preserves absolute differences and leaves the scale alone. Under the SD-008 cone -- large shared
magnitude, small residual differences -- both would rescue the signal, which is why the design
instinct is sound. But if the informative structure in REE's candidate summaries turns out to be
multiplicative in the common magnitude rather than additive on top of it, subtraction is the wrong
operator, and the symptom would be a bias head whose behaviour depends on the overall scale of
z_world. That is cheap to check and worth checking. A review also contributes synthesis rather than
a new measurement, which is a second reason not to lean on it too hard.

Direction supports, confidence 0.58. Good biological warrant for the shape of the fix; not evidence
for the particular form of it.
