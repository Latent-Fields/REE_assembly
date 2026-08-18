# Summary: Matsumoto & Hikosaka (2009) — "Two types of dopamine neuron distinctly convey positive and negative motivational signals"

**Entry ID:** 2026-08-18_mech054_two_dopamine_channels_matsumoto2009
**Claim tested:** MECH-054 (signed harm/benefit prediction-error precision channels remain distinct)
**Evidence direction:** supports | **Confidence:** 0.76

---

> **PROVENANCE NOTE.** This entry replaces `evidence/literature/neuro_pe_habenula_da/entries/2026-02-13_habenula_da_signed_pe_review`, deleted 2026-08-16 (governance cycle, GFLAG-0031) because that record's source block was an unfilled template placeholder (authors "Example Author A"/"Example Author B", doi `10.0000/example-doi`) asserting `supports` at confidence 0.74 for MECH-053/MECH-054 with nothing behind it. Governance left a real habenula/dopamine signed-PE review as a genuine `/lit-pull` gap rather than inventing a replacement inline. Routed to chip `chip-20260816-lit-provenance-quarantine`. By the time this chip ran, a separate, unrelated 2026-08-17 `/lit-pull` session (`REE_assembly` `8b5bf3b8bc`) had already added five strong MECH-053 entries (including two other Matsumoto & Hikosaka lateral-habenula papers), substantially closing the MECH-053 side of the gap. MECH-054 still had only one literature entry (the 2007 Matsumoto & Hikosaka lateral-habenula paper). This entry adds the strongest remaining directly-relevant paper for MECH-054's specific "distinct signed channels" framing.

---

## What the paper did

Matsumoto and Hikosaka recorded from single dopamine neurons in the substantia nigra pars compacta (SNc) and ventral tegmental area (VTA) of rhesus macaques performing a Pavlovian conditioning task in which visual cues predicted either a liquid reward or an aversive airpuff to the face. This design lets the authors ask a question the standard "dopamine = reward prediction error" framework does not directly test: do all dopamine neurons encode signed value (excited by good news, inhibited by bad news), or do some encode unsigned motivational salience (excited by *any* motivationally significant event, good or bad)?

## Key findings relevant to MECH-054

The population split into two functionally and anatomically distinct groups. A minority of neurons were "value-coding": excited by reward-predicting cues and inhibited by airpuff-predicting cues -- a signed response, consistent with the classical reward-prediction-error account. A larger group were "salience-coding": excited by *both* reward-predicting and airpuff-predicting cues, an unsigned response that tracked motivational significance rather than valence. Critically, these two response types were not randomly intermixed -- value-coding neurons were located more ventromedially (including VTA), salience-coding neurons more dorsolaterally (SNc), and a parallel anatomical split was seen for responses to the unconditioned outcomes themselves.

## Translation to REE

MECH-054 claims that signed harm and benefit prediction-error precision channels remain computationally distinct rather than being collapsed into a single blended valence signal downstream. This paper is direct primate electrophysiological evidence that the dopaminergic output stage itself already implements (at least) two separable channels -- one that preserves sign (value-coding) and one that does not (salience-coding) -- and that this separation has an anatomical substrate rather than being a purely post-hoc statistical decomposition. That a signed channel exists as an anatomically identifiable population, separate from an unsigned salience channel, supports MECH-054's structural claim that sign is not discarded or averaged away by the time these signals reach downstream valuation and control circuits.

## Limitations and caveats

Two things temper how far this evidence reaches. First, the signed (value-coding) population is the *minority* of recorded neurons here -- most dopamine neurons in this dataset are salience-coding. So this paper supports "a signed channel exists and is anatomically separable," not "dopamine output is predominantly signed" -- MECH-054 does not require the stronger claim, but the distinction matters for how this entry should be read. Second, MECH-054 is about signed *precision* channels -- i.e., not just sign but also reliability/weighting -- and this paper tests sign, not precision-weighting; the "precision" half of the claim is untested by this source. The task stimuli (liquid reward, airpuff) are simple unconditioned Pavlovian outcomes, a narrower and lower-level construct than REE's graded, contextual harm/benefit residue fields, so there is a real transfer step from "airpuff-predicting cue" to "harm terrain."

## Confidence reasoning

Source quality is high: Nature, primate single-unit recording with anatomical localisation of every recorded neuron, from the same research programme (Matsumoto & Hikosaka) whose lateral-habenula work already anchors this corpus's MECH-053 coverage, giving this entry a coherent mechanistic neighbourhood rather than sitting in isolation. Mapping fidelity is moderate: strong for the "separable signed vs unsigned channels exist" component of MECH-054, weaker for the "precision" (reliability-weighting) component, which the paper does not address. Transfer risk is moderate: simple Pavlovian appetitive/aversive outcomes versus REE's graded residue-field valence structure. Aggregate confidence 0.76 -- solid, genuinely relevant primate evidence for the channel-separability half of MECH-054, correctly scoped rather than over-claimed, and a real replacement for the deleted placeholder rather than a manufactured one.
