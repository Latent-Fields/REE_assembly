# Thought Intake: Direction-Blind Reactive Ambitendency (catatonia route III)

- **Date processed:** 2026-09-06
- **Raw thought:** `docs/thoughts/2026-09-06_direction_blind_reactive_ambitendency.md`
- **Session:** thought-ingestion-ambitendency-20260906 (same session that raised GFLAG-0131 and added the viewer arm badge)
- **Stage:** 2 (structured intake). **REGISTERED:** MECH-535, MECH-536.

## Verbatim core proposal

> looking at the behaviours I would wonder if the ambitendency seen has anything to do with the catatonic ambitendency which in my mind shows there is something malfunctioning which may include contracts with basal ganglia systems

Worked in conversation to: the V3-EXQ-978 two-cell oscillation IS ambitendency in the clinical sense (one step toward food, one step away, repeated), and stupor (boundary-press) arises from the same frozen policy under other start cells. But the generative mechanism is a direction-blind state representation read by a memoryless reactive actor, not a malfunctioning commitment gate and not a harm-stream lock. The basal-ganglia contract enters as a PREDICTION: a commitment latch abolishes the sign without restoring competence, so persistence is protective against representational degradation rather than necessary for competence.

## Evidence provenance (observational, not scored)

V3-EXQ-978 episode-log companion, seed 42, 12 episodes (6 `field_loss_off`, 6 `field_loss_on`), each an independent frozen-policy rollout on a fresh env. Per-step counts checked directly from the log:

| Pattern | Episodes | Detail |
|---|---|---|
| Two-cell approach/withdraw limit cycle | 10 / 12 | resource_field_max alternates high/low across the pair; 9-11 immediate reversals per episode; health_depleted at step 11-23 via the contamination rule (num_hazards = 0) |
| Boundary-press fixed point | 2 / 12 | same action every step against the wall; 198/200 stationary; survives 200 steps, eats nothing (one incidental consumption on the approach run) |
| Straight-run transients before the cycle | ON arm | up to 7 cells; the single in-cycle consumption is on such a run; directional-head argmax constant (cell 6) on every ON step |

Correction to GFLAG-0131's summary: it reads "9 of 12" cycling and "3" wall-press; the per-episode count is 10 and 2. The mechanism claim and the follow-on it names are unchanged.

## What's new vs. existing REE docs/claims (novelty table)

| Thread in the thought | Existing REE coverage | Verdict |
|---|---|---|
| Catatonia as inability to commit (gate frozen at max threshold) | MECH-202 direction B (`psychiatric.commitment_gate_failure`); psychiatric_failure_modes.md commit-gate paralysis table | Already owned, and explicitly NOT this case: the 978 reader has no gate in the loop. Cross-ref + distinguish. |
| Catatonia as harm-stream lock upstream of an intact gate (EXQ-471 exemplar) | SD-036 subtype II; MECH-279 PAG freeze gate | Already owned, and NOT this case: hazard-free rung, no harm stream in the eval loop, no mode manager. Cross-ref + distinguish. |
| One undertrained mechanism, several failure signatures; failure taxonomy indexed on two axes | INV-061; ARC-086 | Already owned as the organising stance; this intake adds one row (a representational-axis route to the catatonia phenotype). Cross-ref. |
| z_world differentiation bounds what a downstream reader can do | INV-088 (`world_goal_evaluator_bounded_by_z_world_differentiation`); 978 autopsy (decodable != usable, H-B/H-C) | Already owned as the bound; this intake names the BEHAVIOURAL signature of the bound (ambitendency / stupor), which nothing registers. Adjacent, register narrowly. |
| Commitment with hysteresis / switching costs; asymmetric enter/exit thresholds | MECH-047; MECH-266; ARC-107 root C (post-commit latch, commit-entry decisiveness) | Already owned as MECHANISMS. What is new is the FUNCTIONAL claim about them: persistence is protective against representational degradation, not necessary for competence, with a specific dissociating prediction. Adjacent, register narrowly. |
| Ambitendency (approach/withdraw limit cycle) as a named failure signature; its lethality by repetition | Nothing. `grep -i ambitend|two-cycle|limit cycle` over claims.yaml and psychiatric_failure_modes.md: 0 hits. | Genuinely new -> MECH-535. |
| Latch converts ambitendency to perseveration without competence (gating vs representational deficit discriminator) | Nothing registers this prediction. The 978 autopsy's oracle-adapter discriminator (H-B/H-C) tests the READOUT axis with a supervised adapter; this is a different, cheaper discriminator on the ACTION-PERSISTENCE axis. | Genuinely new -> MECH-536. |
| Stochastic eval breaks the cycle (noise as de facto commitment perturbation) | GFLAG-0131 (raised 2026-09-04, evidence_discrepancy on INV-088 / MECH-457) | Already routed to governance; not a claim. Cross-ref in notes. |

## Key formulations (verbatim, load-bearing)

> Ambitendency = intact actor + direction-blind state + no persistence. A representational route, not a gating one.

> The latch converts ambitendency into perseveration without competence.

> Commitment is not necessary given a good representation. What it buys is robustness to a degraded one.

> The 978 reader has no BG contract to malfunction; what it shows is what an actor looks like without one.

## Affected existing claims

Cross-referenced via `depends_on` only: MECH-202, SD-036, MECH-279, INV-088, MECH-457, ARC-086 (from MECH-535); MECH-535, ARC-107, MECH-047, MECH-266, MECH-457 (from MECH-536). No status, confidence, evidence record, or wording changed on any existing claim. psychiatric_failure_modes.md gains a Subtype III section and two table rows; the existing Subtype I/II text is untouched.

## Candidate claims -- REGISTERED this pass

- **MECH-535** (`psychiatric.catatonia_direction_blind_reactive_ambitendency`, mechanism_hypothesis, candidate, standard, v3). Direction-blind reactive ambitendency: a memoryless reactive actor over a representation carrying goal proximity but not goal direction yields, from one frozen policy, a two-cell approach/withdraw limit cycle (ambitendency) or a boundary-press fixed point (stupor) by initial condition. Third generative route to the catatonic phenotype, distinct from MECH-202B and SD-036 subtype II; needs no gate to malfunction.
- **MECH-536** (`selection.commitment_persistence_robustness_contract`, mechanism_hypothesis, candidate, standard, v3). BG-like action persistence is protective against representational degradation, not necessary for competence. Predicted dissociating signature: adding a latch to a direction-blind actor abolishes the limit cycle and produces perseveration with no rise in resources per episode.

Both carry `epistemic_category: standard` rather than `substrate_conditional` because the phenomenon is already observed on existing V3 substrate and the falsifier runs on that substrate; `implementation_phase: v3` mirrors SD-036 / MECH-279, the sibling catatonia entries grounded in a V3 fishtank exemplar. No `what_would_answer` drafted here (that is `/thought-digestion`'s job).

## Next steps (not done here)

- **Routing decision, /governance:** the MECH-536 falsifier is an eval-time action-persistence wrapper (persist the chosen action for k >= 2 steps, or a Schmitt-style switch cost) on the SAME frozen OFF-arm policy, scored on resources/episode AND cycle incidence. It is cheap and V3-ready; whether it runs as a letter of 978, folds into chip-20260903-exq978-oracle-adapter-discriminator's pre-registration (GFLAG-0131 already asks that chip to pre-register a stochastic or contamination-off eval), or waits, is a governance call. Not queued from this intake.
- **Literature pull before hardening MECH-535:** ambitendency mechanism accounts (Northoff's top-down OFC/mPFC-motor model; GABA-A and NMDA-R routes; Moskowitz tonic-immobility framing). Question to answer: has a goal-in-valence-but-not-direction route been proposed clinically? The lorazepam analogy in the raw thought is an analogy, not evidence (feedback_lit_exp_decoupled).
- **Left unregistered pending a closer check:** whether the contamination-rule lethality (the pattern kills by its own repetition) deserves its own entry as an "autotoxic persistence" signature, or is adequately carried by ARC-086's axis index. Flagged, not minted.
