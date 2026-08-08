# INV-051 MEL dose-sweep — deferred to V3-EXQ-901; independent design caveat

**Status: FYI for governance / the eventual V3-EXQ-901 autopsy. Not a queue action.**

- **Chip:** `chip-20260808-inv051-mel-dose-sweep`.
- **Generated:** 2026-08-08T12:46Z; **corrected 2026-08-08T13:0xZ** after discovering the chip was double-dispatched.
- **Outcome: DEFERRED, not queued.** This chip was dispatched to two sessions at once. Sibling session **`mel-dose-sweep-inv-051-6b93d7`** (same chip_ref) won the race and already did the full `/queue-experiment` work: it queued **V3-EXQ-901** (`ree-v3` origin/main `751bb5ef40…`) — a 6-arm `world_rule_shift` MEL-dose ladder (under-stimulation → mid → **overload**, plus a matched **consumer-OFF control**) with a pre-registered rigidity DV (E3 post-training policy entropy on a fixed novel probe) — smoke-passed, `validate_experiments --strict` clean, and minted proposal **EXP-0587/EVB-0596** (`manual_proposals.v1.json`, `claim_id: INV-051`). See its WORKSPACE_STATE entry (2026-08-08T12:46:54Z). **This (duplicate) session did NOT re-queue anything** — per the concurrency-arbitration rule (earliest claimant wins; 6b93d7's claim opened first, in this session's own start-of-session git log).

## Correction to this note's original conclusion

The first draft of this file concluded the falsifier was **"not queueable"** because the inverted-U's **upper (overload) limb has no substrate** — reasoning that the consumer models homeostatic compensation (`factor = clamp(1 + gain·(mel/ref − 1), 0.5, 3.0)`; more MEL → more sleep) and that ecological HIGH reaches only duration factor **~1.27**, so the clamp never binds and "MEL exceeding clearance capacity" is unreachable. **That conclusion was wrong, and is retracted.** The ~1.27 figure came from the *averaged* factor in the differently-purposed MECH-180 runs (V3-EXQ-845/861/861a), not from a direct probe. 6b93d7 ran the one-tick readiness probe this note did not: with `world_rule_shift depth=3, interval=10`, `mel_duration_factor` **reaches FACTOR_MAX = 3.0** — the saturation the overload arm leans on IS empirically reachable, and depth grades the re-permutation rate (19/20 vs 13/20 distinct action-maps at depth 3 vs 2). So the experiment is buildable and was correctly queued.

## Residual independent caveat (genuinely useful; weigh at V3-EXQ-901's autopsy, do not treat as a blocker)

One design risk survives the correction and is worth pre-registering as an interpretation note, because it is exactly the kind of thing the eventual autopsy should check:

- **Reaching `factor_max` is the consumer's *maximal compensation*, not decompensation.** In this substrate more MEL buys *more* offline processing (up to 3×), which tends to *complete* update, not leave it incomplete. For the overload arm to raise rigidity via INV-051's stated mechanism ("incomplete update accumulates"), the depth-3 re-permutation rate must exceed what even the 3×-saturated offline duration can clear — i.e. genuine demand-over-capacity, not merely a saturated factor. Whether that holds is the empirical question V3-EXQ-901 answers; it is **not** settled by the factor hitting the clamp.
- **Also note the operative signal is MEAN per-step MEL** (the consumer reads mean e3 PE over the wake period, EMA α=0.1), so a momentary force-cycle factor of 3.0 in the readiness probe is not the same as a *sustained* above-clamp mean over a full run. Check the run's sustained per-arm mean MEL and per-arm factor, not just peaks.
- **The genuine decompensation mechanism INV-051 names — sleep capacity *falling* as MEL rises (hyperarousal; high NA/cortisol, MECH-178) — has no substrate** (no NA/arousal plane in `ree_core`; MECH-178 substrate-blocked). V3-EXQ-901's overload arm therefore tests the "demand exceeds a *fixed* offline ceiling" reading, not the "capacity actively collapses" reading. A PASS supports the fixed-ceiling half; it says nothing about the hyperarousal half. V3-EXQ-901's consumer-OFF control is the right lever to check the effect is MEL-driven rather than a construction artifact.

**Interpretation guidance for the autopsy:** if the overload arm shows rigidity **monotone-descending** across the ladder (rather than rising at the top), read it as *"the substrate could not instantiate genuine over-capacity overload"* (the risk above), **not** automatically as an INV-051 falsification — the two are distinguishable via the sustained per-arm mean MEL vs the 3× offline clearance and the consumer-OFF control.

## Corroborating state (unchanged)

- INV-050 sibling governance **GFLAG-0002** (user-confirmed HOLD 2026-08-07): promotion re-gated on genuinely independent evidence (new seeds and/or held-out environment and/or consumer-absent control) because 845/861/861a are pseudo-replication (one config × seeds 42/123/456). V3-EXQ-901's consumer-OFF control partly addresses this; confirm its seed set is not merely a superset of 42/123/456.
- Prior gated proposal `EXP-0376` (`experiment_proposals.v1.json`, `blocked_substrate`) predates the 2026-08-01 producer validation and is now superseded by EXP-0587/V3-EXQ-901.

---

*Author: headless metaworker session `metaworker-chip-20260808-inv051-mel-dose-sweep` (the duplicate; deferred to 6b93d7). Committed under its own TASK_CLAIMS entry.*
