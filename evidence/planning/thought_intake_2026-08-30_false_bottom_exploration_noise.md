# Thought Intake: False bottoms, attractor escape, and what exploration noise is for

- **Date processed:** 2026-09-01
- **Raw thought:** `docs/thoughts/2026-08-30_false_bottom_exploration_noise.md`
- **Session:** planning-metabolise-20260901

## Verbatim core proposal

MECH-440's noisy-selection mechanism may be testing the wrong conception of exploration. The motivating intuition is not "when several immediate actions have similar scores, add noise" but "when you cannot figure something out, you start trying random stuff." Injected variation exists to escape a **false bottom** — an attractor that is locally stable and appears low-energy but is a dead end. The trigger should be **confidence without successful resolution** (persistent failure despite settling), not uncertainty/near-ties; the perturbation may need to occur ABOVE the immediate action level (trajectories, strategies, retrieved attractors, dominant-attractor precision/authority); the loop is triggered-annealing-shaped: stuckness → inject variation → escape attractor → search → settle → reduce exploration. V3-EXQ-959's clean weakening of the near-tie/self-annealing formulation STANDS (per the raw file's own processing note); the proposal re-scopes the ecological function, it does not explain away the negative.

## Key formulations

> "Noise should help the creature get out of a false bottom."
> Reframe: away from "uncertain therefore random," toward "settled but unresolved therefore reopen the search space."

## What's new vs. existing REE docs/claims

| Thread | Existing coverage | Verdict |
|---|---|---|
| Low-level noise floor + self-annealing | **MECH-440** (state-conditioned self-annealing weight noise; weakens stands post-959), **MECH-313** (tonic floor, non-propagating per V3-EXQ-687) | Already-owned; explicitly distinguished-from |
| The stuckness trigger (confidence-without-resolution) | **MECH-482** epistemic_deficit accumulator — "persistent, target-bound … unresolved, consequential, potentially-resolvable model inadequacy," rises with unresolved importance x uncertainty x resolvability x persistence — is nearly the exact trigger quantity, and its substrate LANDED 2026-08-29 (ree-v3 b69a1b8, SD-102) | Already-owned trigger SUBSTRATE — the new claim consumes it rather than duplicating it |
| Sleep-phase annealing | Astrocyte sleep-annealing Q-claim (anneal/reset R(x,t)) | Adjacent-but-distinct (offline field anneal vs online triggered escape) |
| Stuckness-triggered, above-action-level attractor-escape exploration as a distinct mechanism | Nothing — no claim ties a stuckness signal to progressively broader perturbation with post-resolution decay | **Genuinely new — registered below** |
| False-bottom test ecology (delayed-return trap, blocked-path detour, rule-change, sparse-reward, loop basin) | No existing ecology creates a genuine false bottom | New experimental requirement; carried in the claim's notes for the eventual falsifier design |

## Affected existing claims

MECH-440 untouched (weakens stands; its routed lit-pull chip-20260830-mech440-targeted-lit-pull should ALSO read this intake — the lit target should include triggered/annealing-style exploration, not only NoisyNet-family parametric noise). MECH-482, MECH-313, MECH-314b/c cross-referenced via depends_on.

## Candidate claims — REGISTERED this pass

- **MECH-527** — stuckness-triggered attractor-escape exploration: a triggered, organism-level annealing analogue, gated on confidence-without-resolution (natural substrate: MECH-482's epistemic_deficit), perturbing above the immediate-action level with escalating breadth, decaying after successful resolution.

## Next steps

1. Feed this intake to the MECH-440 targeted lit-pull (chip-20260830-mech440-targeted-lit-pull) before it runs — one lit-pull can serve both claims.
2. A false-bottom ecology experiment is plausibly V3-tractable NOW (MECH-482 substrate landed; gridworld traps buildable), but routing is /governance's call — flagged, not decided here.
