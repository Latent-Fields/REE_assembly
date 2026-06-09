# Neonatal critical-period sensitization: the failure mode ARC-046 is designed to prevent

**Claim:** ARC-046 — "The infant stage requires a hazard protection mechanism that permits sensorially salient harm exposure without catastrophic residue saturation."

**Source:** Hohmann AG, Neely MH, Piña J, Nackley AG (2005), *The Journal of Pain* 6(12):798-808. According to PubMed, [DOI 10.1016/j.jpain.2005.07.009](https://doi.org/10.1016/j.jpain.2005.07.009), PMID 16326368. Direction: **mixed** (confidence 0.70).

## What the paper did

Rats received unilateral intraplantar complete Freund's adjuvant (CFA), producing chronic hind-paw inflammation, on **postnatal day 0 (P0)** or **postnatal day 14 (P14)**, with saline and untreated controls. In adulthood the animals were challenged with intradermal capsaicin, and both behavioral sensitization (thermal/mechanical hyperalgesia, allodynia) and neuronal activation (dorsal-horn Fos protein) were measured. The P0-CFA animals showed elevated capsaicin-evoked hyperalgesia and allodynia and increased Fos in the superficial and neck regions of the dorsal horn as adults. The **P14-CFA animals did not** — the same inflammatory insult, delivered two weeks later, left adult pain processing essentially normal. The authors conclude that chronic inflammation within a critical developmental period permanently alters adult pain sensitivity through lasting central sensitization.

## Why this is mixed evidence for ARC-046

The paper cuts both ways, which is exactly why I have logged it as `mixed` rather than `supports`.

**It supports the protective half of ARC-046.** ARC-046 posits a failure mode — "catastrophic residue saturation" — in which unmitigated harm load during infancy produces "a permanently damaged substrate that cannot support childhood training." This study is a concrete biological instance of that failure mode. An early harm insult, delivered when protection is absent, does not merely teach the animal where harm lives; it permanently raises the gain of the entire nociceptive system into adulthood. That is precisely the durable, maladaptive set-point ARC-046 says infancy must be shielded from, and it is the empirical justification for `residue_scale_factor ~0.1` and reduced `hazard_magnitude`. It also confirms that a **developmental window** is real and sharply bounded (P0 damages, P14 does not), which grounds ARC-046's design that protection is "progressively removed as the agent transitions through childhood to adulthood."

**It pressures the optimistic half of ARC-046.** The claim's short form is that infant harm exposure can be "educative ... but not permanently damaging." This paper shows that whether an identical insult is benign or permanently damaging is decided by *timing alone*. There is no dose of early nociceptive input that is automatically safe; safety is a property of *when* relative to the critical window, not of the harm being "infant-scaled." So the protection mechanism ARC-046 requires is not optional polish — without correctly-timed attenuation, salient harm exposure in the sensitive window is catastrophic by default. The educative-without-damage outcome is achievable, but only because the protection is doing real work.

## Limitations

This is spinal/peripheral nociceptive sensitization in the rat, not a global "residue field," and the damaging outcome measured here is *hyperalgesia* (raised gain) rather than *saturation* (exhausted plasticity). Those are related failure modes but not identical, so the mapping fidelity is moderate (0.62). The critical-period boundaries are specific to the developing rat dorsal horn; transposing them onto REE's infancy→childhood curriculum schedule is qualitative. I have kept overall confidence at 0.70 and flagged the species/level transfer in `transfer_risk`.

## Why included

Together with the SHRP review (Suchecki 2018), this paper completes the biological case for ARC-046 from the opposite direction. Suchecki shows the *mechanism* — an actively regulated developmental clamp on harm-load. Hohmann shows the *stakes* — what happens when that clamp is absent or mistimed: permanent sensitization, the catastrophic residue saturation ARC-046 exists to prevent.
