# Synthesis: SD-032e pACC-Autonomic Coupling — Write Target and Timescale Scoping

**Scope:** scoping review for SD-032e implementation. Four literature entries drawn from Baliki 2012 (chronic pain corticostriatal connectivity), Mayberg 2005 (sgACC DBS for depression), Gianaros/Critchley 2011 (cingulate-brainstem autonomic coupling), Guo 2018 (ACC mGluR5 plasticity in chronic pain). The review addresses three questions raised during SD-032e planning before implementation.

---

## Question 1 — Does pACC/sgACC write primarily to a slow homeostatic baseline (drive_level), a valence setpoint (affect-signed state), or fast autonomic effectors directly?

**All three pathways exist biologically. They are not alternative theories; they are coexisting output channels of pACC/sgACC.**

- *Fast autonomic-effector route:* Gianaros 2011 is the clearest evidence — pgACC/sgACC to PAG to medullary autonomic nuclei to heart, on sub-second to seconds timescale. This route is real and clinically important (baroreflex, heart rate variability, depression-linked autonomic dysregulation). REE currently has no fast-autonomic analogue; implementing this route would require a new precision-like or arousal-like variable and a PAG-analogue module. **Out of scope for SD-032e.**

- *Valence setpoint route:* Mayberg 2005 is the strongest anchor — sgACC tonic activity biases mood across a valenced baseline, and suppressing sgACC reverses depression. This implies the pACC/sgACC write target is valence-signed. REE's current drive_level (SD-012) is unsigned (1 − energy), so a literal Mayberg mapping onto drive_level is a shape mismatch.

- *Slow homeostatic baseline route:* Baliki 2012 shows that sustained nociceptive exposure reorganises corticostriatal connectivity on a months-timescale, licensing the general architectural move SD-032e makes. But the Baliki drift localises to mPFC-NAc reward-valuation circuitry, not to an interoceptive homeostatic baseline.

**Recommendation for SD-032e:** write into `drive_level` as a first-pass simplification, with the SD doc explicitly noting three things: (a) this compresses pACC's valence-setpoint role onto REE's nearest unsigned scalar; (b) the fast-effector route is known biology that SD-032e does not cover and that a future SD-032f could; (c) a biologically tighter long-term target would be a valence-signed setpoint variable distinct from drive_level, and adding one would be a natural step if SD-032e's validation experiment shows the unsigned mapping is too coarse. Do NOT cite Mayberg as direct support for writing into drive_level; cite it for the architectural move (write-into-setpoint) with the mapping caveat stated.

---

## Question 2 — Is a slow-EMA write-back from sustained z_harm_a into a drive_level-analog biologically licensed, or a simplification the literature flags?

**Both. It is biologically licensed as an architectural move; it is a simplification at the mapping level that the literature does flag.**

Licensed: Guo 2018 provides the cellular mechanism — sustained C-fibre (affective-pain) input drives mGluR5-dependent LTP at ACC synapses over 7-14 days, and the plasticity produces persistent behavioural sensitisation that reverses when the input abates and mGluR5 is blocked. A slow-EMA abstraction of sustained z_harm_a is a reasonable high-level stand-in for this process. Baliki 2012 provides the macroscopic evidence that such slow drift is real and clinically significant in humans.

Flagged as simplification: the biology shows the plasticity accumulates *inside pACC* (as local synaptic efficacy), and pACC then modulates downstream targets through its output connections. SD-032e as currently scoped compresses two biological steps into one by writing directly from z_harm_a into drive_level. A more faithful mapping would have pACC-analog accumulate an internal gain state, and that internal state would modulate pACC's downstream output, which in turn would influence drive_level via the existing SD-012 path. Whether to implement the indirect version is an engineering trade: one more layer of indirection for cleaner biological mapping.

**Recommendation:** proceed with the direct-write EMA as designed, but note in the SD-032e spec that this is a two-step compression. Keep the EMA decay constant slow enough to reflect the days-timescale biology — if a REE episode is ~1000 steps, the decay constant should correspond to multi-episode accumulation (e.g. `pacc_drive_ema=0.995` or slower), not within-episode saturation. The current plan was `0.99`; that is at the fast end of biological plausibility and should be verified by the validation experiment showing meaningful drift only after sustained exposure.

---

## Question 3 — Is offline/sleep normalisation of accumulated drift a distinct claim with its own literature, or a default behaviour SD-032e should include?

**Distinct claim. SD-032e should default `pacc_offline_decay=0.0` and flag that any non-zero value instantiates a separate sleep-recalibration claim requiring its own registration.**

The current lit-pull did not sample the sleep-pain-recalibration literature directly. Guo 2018 shows the ACC plasticity is reversible given nociceptive quiescence but does not isolate a sleep-specific mechanism. The broader sleep-pain bidirectional literature (sleep deprivation increases pain sensitivity; restorative sleep reduces chronic-pain plasticity) exists but is not part of the evidence in this review.

REE already has claims in the offline/sleep space that would risk conflation if SD-032e silently implements offline decay:
- **MECH-092** — hippocampal SWR-equivalent replay during micro-quiescent E3 heartbeat cycles.
- **INV-049** — the general law that offline phases are a mathematical necessity for model-building agents (the "sleep necessity" invariant).
- **MECH-094** — hypothesis-tag gate for write-safety during simulation/DMN.

A pACC offline decay mechanism would be a *fourth*, distinct offline-phase function: homeostatic normalisation of accumulated affective-pain drift. Rolling it in as a default of SD-032e would both conflate it with the existing offline claims and preclude proper registration with its own literature, its own falsification signatures, and its own prerequisite checks.

**Recommendation:** default `pacc_offline_decay=0.0` in SD-032e. Document in the SD-032e spec and in ree-v3/CLAUDE.md that non-zero values instantiate a separate sleep-recalibration claim (provisionally MECH-TBD). That claim, if pursued, would need its own lit-pull covering sleep-pain bidirectional dynamics and its own validation experiment. SD-032e remains scoped to the accumulation-without-offline-normalisation case; offline normalisation is a follow-up claim, not an implementation default.

---

## Architectural recommendation summary

1. **Write target:** `drive_level` (SD-012) as first-pass proxy. Valence-signed setpoint is the biologically tighter target; document the shape mismatch in SD-032e spec. Do not cite Mayberg 2005 as direct validation of the drive_level mapping.

2. **Timescale:** slow EMA over sustained z_harm_a, with decay constant set for multi-episode accumulation (~0.995 or slower), not within-episode saturation. Validation experiment must confirm drift magnitude scales with sustained exposure duration, not peak intensity.

3. **Offline decay:** default zero. Non-zero values require a separate registered claim with its own literature and validation. SD-032e does not model sleep normalisation.

4. **Direct-write simplification:** explicitly noted as compressing two biological steps (ACC internal plasticity → ACC-modulated downstream influence) into one. Acceptable for first substrate; may be revisited if validation experiment shows the compression produces wrong-shape drift dynamics.

5. **Scope exclusion:** fast-effector route (Gianaros 2011, ACC-PAG-medulla-heart on seconds timescale) is real biology SD-032e does not address. Flag as future work (notional SD-032f) contingent on REE gaining fast-autonomic variables.

---

## Falsification signatures (consolidated)

SD-032e is falsified if any of the following hold in its validation experiment:

1. Sustained z_harm_a exposure produces no measurable drift in drive_level.
2. Drift saturates within a single episode (timescale mismatch with Guo 2018 biology).
3. Drift occurs but is unrelated to z_harm_a magnitude — i.e. any prolonged simulation produces the same drift regardless of affective-pain content.
4. Drift occurs but has no downstream behavioural consequence in SD-032c's salience gating or in action selection — a write with no read is not a setpoint.
