# Active avoidance learning requires prefrontal suppression of amygdala-mediated defensive reactions (Moscarello & LeDoux, 2013)

**Claim tested:** SD-035 (amygdala analogue as avoidance-learning driver) -- with a missing-mechanism warning
**Direction:** mixed | **Confidence:** 0.78

## Why this is the decision-relevant entry

Of the five papers in this review, this is the one that most directly explains *why the V3-EXQ-603g survival/hazard-avoidance Stage-H would not train* (G_H 0/3), and therefore the one that most shapes what the substrate fix should be. The developmental papers say avoidance learning is gated by substrate maturation; Tovote says the freeze output exists as a distinct circuit; this paper says the thing in between -- the step from "having a defensive reaction" to "having learned to avoid" -- is itself a hard, separately-implemented computation.

## What the paper did and found

Moscarello & LeDoux studied signaled active avoidance (AA) in rats -- the animal learns to perform an action during a warning cue to prevent shock -- using pretraining excitotoxic lesions of the infralimbic prefrontal cortex (ilPFC) and the central amygdala (CeA). Their framing is that AA "involves pavlovian and instrumental components, which produce competing behavioral responses that must be reconciled," and that "early trials of AA training are characterized by a conflict between mutually exclusive responses to the CS": the Pavlovian freezing reaction and the instrumental avoidance action cannot both happen, so one must give way.

The lesion results give a double dissociation. Removing the suppressor (ilPFC) made freezing worse and avoidance harder: ilPFC lesions produced "a main effect for lesion (F(1,14) = 14.78, p = 0.002), indicating that ilPFC lesion increased conditioned freezing across sessions," with correspondingly reduced avoidance. Removing the freeze source (CeA) did the opposite, with "a lesion x session interaction (F(4,48) = 6.19, p < 0.001)," reduced freezing and facilitated avoidance. The authors conclude that "AA learning recruits ilPFC to inhibit CeA-mediated defense behaviors, leading to a robust suppression of freezing."

## How this translates to REE -- and why the direction is *mixed*

REE currently has two of the three pieces this circuit needs. SD-035 supplies the amygdala salience stage; MECH-279 supplies the CeA->PAG freeze gate. What REE does **not** have is the third piece: a prefrontal-analog that *inhibits the freeze reaction so an instrumental avoidance action can be acquired and consolidated*. Map the lesion conditions onto the substrate and the failure becomes legible: a REE agent with a freeze gate but no reaction-suppression layer is the ilPFC-lesion animal -- it freezes instead of learning to avoid. That is the 603g G_H 0/3 signature, restated as a circuit prediction.

So I marked this entry **mixed** rather than supports. It supports the broad design intent (wire the amygdala as an avoidance-learning driver) but it simultaneously falsifies the *sufficiency* of the current wiring: extending curriculum budget on an SD-035+MECH-279 freeze-and-salience substrate will not produce avoidance learning, because the limiting computation is the resolution of a Pavlovian-instrumental conflict, not the accumulation of more conditioning episodes. The implied fix is structural -- add an instrumental-avoidance action pathway and an ilPFC-analog suppression gate over the freeze output -- which is exactly the kind of "deeper substrate mechanism" the user's adjudication called for, and which this review exists to license before any further curriculum iteration.

## Limitations and confidence reasoning

Confidence 0.78. It is a strong primary causal study from the LeDoux lab with a clean lesion double-dissociation and reported statistics, and the Pavlovian-instrumental-conflict account is well-replicated. It sits below the Tovote entry because it is paradigm-specific (two-way shuttle AA, not survival-under-hazard foraging) and because the key REE implication is the *absence* of a component rather than confirmation of a present one -- which is inherently a more inferential mapping. The honest framing for governance: this paper is the strongest evidence that the fix is a new suppression/instrumental layer (a candidate SD/MECH), and it should be weighted as a design prescription, not as confirmation that SD-035 alone resolves the leg.
