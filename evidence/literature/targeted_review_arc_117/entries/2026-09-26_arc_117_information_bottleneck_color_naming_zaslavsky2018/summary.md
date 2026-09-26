# Zaslavsky, Kemp, Regier & Tishby (2018) -- Efficient compression in color naming and its evolution

**What they did.** They framed a language's colour vocabulary as an information bottleneck. The speaker has a colour in mind and encodes it as a word, and the listener reconstructs a belief about the colour from the word. A good lexicon trades off *complexity* (how many distinctions it keeps) against *accuracy*, meaning how closely the listener's reconstruction matches what the speaker meant. They then asked where real languages fall on that trade-off.

**What they found.** Colour-naming systems across the World Color Survey languages lie close to the optimal frontier. A single trade-off parameter captures much of the variation between languages. The optimal systems also show the untidy features real languages have: soft boundaries, and large regions named inconsistently.

**What it means for ARC-117.** The accuracy term here is the receiver's residual uncertainty about the sender's intended meaning. So this is evidence, at a whole-language scale, that the thing a communication code is optimised for is the receiver's reconstruction, just as ARC-117 says of individual messages. It is not merely the sender's compression of what struck them.

**Two important qualifications.** First, level. This paper is about which words a language *makes available*, shaped over generations. It is not about which one a speaker *chooses* now. ARC-117 is a per-message claim, and the paper cannot test it directly. Second, the wording. The IB solution does not minimise receiver uncertainty. It trades uncertainty off against cost, and happily leaves large regions of colour space ambiguous. ARC-117 would be better stated as "selection trades receiver-uncertainty reduction against channel cost". Its own falsifier already implies this with its "matched channel budget".

**Confidence.** 0.5. Strong source and the right objective, but at one remove from the claim's level.
