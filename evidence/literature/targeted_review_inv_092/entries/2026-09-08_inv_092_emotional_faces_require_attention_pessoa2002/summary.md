# Pessoa et al. (2002) -- Neural processing of emotional faces requires attention

**Claim tested:** INV-092 | **Direction:** supports | **Confidence:** 0.70

## What the paper did

Twenty-one healthy adults were scanned with fMRI while viewing fearful, happy and neutral faces. The authors first localised regions responding differentially to emotional versus neutral expressions, then measured those same responses while attention was consumed by a competing peripheral bar-orientation task demanding enough that subjects reached only 64% accuracy. The prevailing view at the time held that emotional stimuli activate the brain automatically, largely immune from attentional control -- the amygdala in particular being the canonical privileged fast route.

Every region responding differentially to emotional faces, amygdala included, did so *only* when attentional resources were available. Under high load, unattended-face responses showed no significant difference from zero. The authors conclude that facial-expression processing is under top-down control.

## Why this matters for INV-092

INV-092's notes name four things an adequate suppressor must distinguish, and flag the fourth -- another agent's state becoming newly relevant -- as the hardest. This paper is the reason it is hard, and it is the sharpest evidence in this pull for why the invariant needs to exist as a stated constraint rather than an assumed property.

A facial expression is the canonical other-agent state signal. The amygdala is the canonical privileged channel for it. Both were silenced by nothing more exotic than a demanding concurrent task. The suppression was not the product of a badly designed mechanism, an adversarial input, or a safety-relevant design error; it was an ordinary competing task doing exactly what competing tasks do.

The design implication is blunt. A tempting REE shortcut is to tag harm and other-agent inputs "high priority" and treat permeability as thereby secured. Priority is a weight. Suppression scales weights. Nothing about being weighted highly makes a signal exempt from a mechanism whose entire function is to attenuate weights on non-goal inputs. If the biological system with a dedicated subcortical route for exactly this signal class can have that route closed by a bar-orientation task, an engineered suppressor should be assumed to close it unless measurement says otherwise.

It also tells the falsifier where to look. The expectation this sets is that the other-agent leg breaks at a *lower* suppression setting than the one at which goal completion reaches its optimum. If so, a sweep that instruments a single generic "harm interrupt rate" will find the failure late or not at all -- the other-agent channel has to be injected and scored separately from the nociceptive-analogue channel.

## Limitations and caveats

The dependent measure is a differential BOLD response, not an interrupt or a behavioural override. A suppressed differential response does not prove the signal could not have interrupted had the situation demanded it; INV-092 constrains interruptibility, and this paper measures representation. The load manipulation is perceptual and spatial, which is not the goal-commitment suppression REE would implement.

Most importantly, this result sits inside a live dispute and should not be presented as settled. Vuilleumier and colleagues report amygdala responses to fearful faces that survive comparable attentional manipulations, and Pessoa's own 2005 *Current Opinion in Neurobiology* review treats the extent of attention-independent emotional processing as an open question. The authors of this paper themselves note that their finding shows attention is *necessary* for differential emotional processing under these conditions, not that involuntary threat responses never occur under lighter competing demand. The defensible reading for REE is therefore: the other-agent channel *can* be closed by load, to an uncertain degree that varies with conditions -- which is itself sufficient to establish that permeability must be measured per suppression setting rather than assumed.

## Confidence reasoning

Source quality 0.85: PNAS, Ungerleider lab, adequately powered for its era, heavily cited. Mapping fidelity 0.65, capped by the gap between a differential BOLD response and an interrupt. Transfer risk 0.50: what transfers is a direction -- a strong enough competing task can close the other-agent channel -- not a parameter, and REE's suppressor is not a perceptual-load manipulation. Aggregate 0.70 rather than higher, principally because the finding's replication status is genuinely mixed and an entry that overstates it would mislead a future governance read in the direction of false alarm rather than false comfort, which is the less costly error but still an error.
