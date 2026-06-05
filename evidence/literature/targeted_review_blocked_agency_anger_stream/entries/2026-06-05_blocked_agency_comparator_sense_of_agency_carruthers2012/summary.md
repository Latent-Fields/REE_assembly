# The comparator model: REE already has the blocked-agency detector (Carruthers 2012)

**Source:** Carruthers, G. (2012). The case for the comparator model as an explanation of the sense of agency and its breakdowns. *Consciousness and Cognition*, 21(1):30–45. DOI [10.1016/j.concog.2010.08.005](https://doi.org/10.1016/j.concog.2010.08.005) (PMID 20833565).

## What the paper does

A theoretical paper defending the Frith-lineage *comparator model* of the sense of agency against the multifactorial-weighting model of Synofzik and colleagues. On the comparator account, a forward model generates an efference copy of each motor command and predicts its sensory consequences; a comparator then matches that prediction against the actual sensory feedback. The sense of agency "arises when and only when the comparator detects that the predicted sensory feedback is identical to the actual sensory feedback." When prediction and reality mismatch, agency is absent or is attributed to an external agent — which is how the model explains breakdowns such as delusions of alien control in schizophrenia. Carruthers' specific contribution is to rebut the common objection that *actual* sensory consequences are not needed to elicit agency, and to show the comparator can account for both healthy and delusional self-attribution performance.

## Findings relevant to the candidate stream

The point for REE is that the **detection mechanism for blocked agency already exists in the substrate**. A blocked-agency event is, formally, a comparator mismatch on the *action-outcome* channel: the agent issued an action, predicted an effect, and the realised effect repeatedly failed to match. That is the same computation the comparator model describes for the sense of agency and its loss. So the candidate stream does not require a new sensor — it requires an *affective readout* layered on the existing comparator. The paper also flags the two things the bare comparator does **not** supply: (1) an attribution step (was the mismatch caused by an external constraint, or by my own motor error?), and (2) a gating context (is my goal/capacity still live?). Both are needed before a mismatch becomes a *blocked-agency affect* rather than a neutral prediction error.

## How it maps to REE

REE already instantiates a comparator in SD-029: `residual = z_harm_s_observed − E2_harm_s(z_harm_s_{t-1}, a_actual)` for harm-channel agency attribution. The same machinery, applied to the *action-outcome / goal channel*, is the detector for blocked agency: intended effect predicted by the forward model (E2), realised effect diverges, integrated over a window, attributed to external constraint, gated on retained z_goal/wanting. This is why the verdict can place the V3 proxy as *low-cost*: SD-029 is the sensor, MECH-112/z_goal supplies the expectation, and the new work is the readout + attribution + capacity gate, not a new substrate. I co-tag SD-029 because the paper genuinely supports the comparator's role in agency detection, which is SD-029's mechanism.

## Limitations and confidence

This is a single-author theoretical paper whose empirical anchor is alien-control delusion, not environmentally-blocked action, and the comparator model is actively contested (Synofzik et al.'s multifactorial weighting is a live rival in which agency is sometimes inferred from intention/context rather than realised-outcome comparison). So the comparator-mismatch should be treated as the *necessary* detection primitive for blocked agency, not as a complete account of agency in REE. I score 0.66: moderate source quality, good mapping fidelity to SD-029 (the load-bearing claim), moderate transfer risk given the contested model and the delusion-rather-than-blocking empirical base.
