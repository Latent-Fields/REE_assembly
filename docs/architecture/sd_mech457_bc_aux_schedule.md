---
title: "Substrate: mech457_bc_aux_schedule"
parent: "Goals, Drives & Motivation"
grandparent: Architecture
nav_order: 28
---

# Substrate: mech457_bc_aux_schedule

**Substrate id:** `mech457_bc_aux_schedule` (composition primitive; no SD-NNN number -- lives in `experiments/_lib/**`, not `ree_core`)
**Subject:** `action_learning.bc_auxiliary_persistence_schedule`
**Status:** IMPLEMENTED (2026-07-18)
**Registered:** 2026-07-18
**Depends on:** `mech457_competence_bootstrap_explorer` (IMPLEMENTED 2026-07-16), H-bc-prior BC-auxiliary hook (`bc_demo` / `bc_aux_coef`, landed 2026-07-18 with V3-EXQ-780)
**Blocks (unblocks on validation):** hypothesis `H-retention-auxiliary-decay` (question `competence_floor`, `hypothesis_space_registry.v1.json`); MECH-457 (candidate / v3_pending), INV-088 (candidate / pending_substrate_reconfirmation)
**Design doc:** `evidence/planning/mech457_retention_portfolio_2026-07-18.md`

## Problem

The MECH-457 retention portfolio reframes the competence question from "which mechanism
produces competence" to "why is produced competence not RETAINED". The reframe is licensed by
V3-EXQ-780's raw_view arm, which took the BC seed 3/3 at `post_bc_foraging_competence = 20.933`
and then scored a terminal null -- a *successful* manipulation that decayed, mis-scored as a
failed one because the interpretation grid enumerated only a ~0 null.

`H-retention-auxiliary-decay` asks whether the installed prior is being actively out-competed by
the RL objective, by sweeping the persistence of the imitation auxiliary (constant / annealed /
off) and reading a competence **half-life**. Its declared null: *half-life is invariant to the
auxiliary schedule -> the prior is not being out-competed by the RL objective.*

That sweep cannot be expressed against the live substrate. `bc_aux_coef` is a constant float
(`experiments/_lib/mech457_explorer_classes.py:537`, declared
`experiments/_lib/mech457_bootstrap_explorer.py:148`), read once per episode at
`mech457_explorer_classes.py:702` where `loss = loss + float(bc_aux_coef) * bc_loss`. There is no
way to vary it over training, so only the *constant* and *off* cells of a three-cell sweep are
reachable; the annealed cell -- the one that actually discriminates the hypothesis -- is not.

This is the **cheapest** of the four retention gaps, and the scheduling pattern it needs already
exists beside it in the same function.

## Solution

Mirror the proven `(ep, n_episodes) -> float` callable pattern already used for the intrinsic
coefficient and rollout entropy.

**`experiments/_lib/mech457_explorer_classes.py` (`train_a2c`):**

1. New keyword `bc_aux_schedule: Optional[Callable[[int, int], float]] = None`, declared beside
   `coef_schedule` / `entropy_schedule` (`:534-535`).
2. Per-episode effective coefficient, computed in the same block that derives `beta_eff` /
   `coef_eff` (`:615-622`):
   `bc_coef_eff = float(bc_aux_schedule(ep, n_episodes)) if bc_aux_schedule is not None else bc_aux_coef`
3. The auxiliary guard and loss term (`:702`, `:708`) read `bc_coef_eff` rather than the constant.
4. `bc_aux_coef_first` and `bc_aux_coef_last` added to the returned guard dict, so the manifest can
   verify the schedule actually moved rather than assuming it did. (Both endpoints, not just the
   final value: an annealed arm whose schedule silently stayed flat is otherwise indistinguishable
   from a constant arm.)

**`experiments/_lib/mech457_bootstrap_explorer.py` (`BootstrapExplorerConfig` /
`train_bootstrap_explorer`):**

5. Two new config fields -- `bc_aux_coef_end: Optional[float] = None` and
   `bc_aux_anneal_fraction: float = 0.0` -- declared in `as_slice()`.
6. `train_bootstrap_explorer` builds the schedule with the **existing** `linear_anneal`.
7. The `bc_demo`-required precondition extends to `max(start, end) > 0`, and is **moved ahead of
   module construction**. A ramp-UP cell (start `0.0` -> end `>0`) slips past a start-only check;
   and a misconfigured arm should fail on its config rather than partway through allocation. (Found
   during smoke testing: the check previously sat after the `RNDModule` construction, so a config
   error surfaced as an unrelated `AttributeError`.)

### Two design choices that are load-bearing, not stylistic

**(a) The effective value must drive the GUARD, not just the loss weight.** The existing guard is
`if bc_demo is not None and bc_aux_coef > 0.0 and bc_logits:`. An annealed cell passes
`bc_aux_coef = 0.0` with a nonzero schedule; a guard still reading the constant would suppress the
auxiliary entirely and silently produce an *off* arm labelled *annealed* -- a degenerate arm read
as a scientific verdict.

**(b) The BC schedule uses `linear_anneal`, NOT the shared `warm_then_anneal`.** The latter is
parameterised by `warm_start_fraction`, which is shared with the intrinsic-coefficient and entropy
schedules. Routing BC decay through it would couple the auxiliary's persistence to the exploration
anneal, confounding the leg's single intervention. For the same reason `bc_aux_schedule` is
deliberately **not** placed under the `mode_gate` mutual-exclusion branch (`:551-555`): that
exclusion exists because a developmental anneal and a critic-utility gate are competing answers to
the same question about *exploration* scheduling. BC persistence is orthogonal to both.

### Anti-alias constraint (carried from the portfolio's anti-alias audit)

This leg owns the `bc_aux_coef` axis. `mech457_policy_kl_anchor` (`H-retention-consolidation`)
MUST NOT be operationalised through the BC auxiliary -- anchoring via `bc_aux_coef` would anchor to
the *demonstrator* rather than to the installed policy snapshot, aliasing the two legs directly.
The four legs partition the retention pathway into what the baseline **knows** (critic), how far
the policy may **move** (consolidation), how long the prior is **held** (this leg), and whether the
drive **terminates correctly** (consummation binding).

## Backward compatibility

All new parameters are no-op defaults: `bc_aux_schedule=None`, `bc_aux_coef_end=None`,
`bc_aux_anneal_fraction=0.0`. With defaults, `bc_coef_eff == bc_aux_coef` and every pre-existing
caller (765 / 769 / 770 / 771 / 772 / 780 / 781) is byte-identical. No existing default changes.

**Fingerprint note:** this edits `experiments/_lib/**`, which is bound into `substrate_hash`, so
pre-change baseline arm fingerprints are correctly refused for reuse. That is the mechanism working
as designed, not a regression. `as_slice()` gains two declared keys for the same reason -- config
slices must declare what they can vary.

## Phased training

Not applicable. This adds no encoder head and trains no new module on latent targets; it reweights
an existing cross-entropy term against a fixed demonstrator. The P0->P1->P2 phasing requirement
does not attach.

## MECH-094

Not applicable. No simulation, replay, or non-waking-state memory write is introduced. (The
pre-existing prioritized credit-replay in the same function replays *stored on-policy transitions*
for credit assignment, not generated content, and is untouched by this build.)

## What this substrate enables

`H-retention-auxiliary-decay` becomes buildable: BC-install to the raw_view ~20.9 point, then RL
refinement under three auxiliary-persistence cells (constant / annealed / off) at matched seeds,
measuring the post-installation competence **trajectory** and reading a half-life.

Per the portfolio's mandatory design constraints, any eventual script must (1) sample competence on
a fixed post-install schedule rather than terminally, (2) enumerate a "manipulation succeeded and
then decayed" branch in its interpretation grid and route on declared covariates rather than only
the terminal criterion, and (3) treat install verification as a precondition -- an arm whose BC
install did not take must self-route `substrate_not_ready_requeue`, never a retention verdict.

**Nothing is queued on this build alone.** Per GOV-FANOUT-1 and the portfolio's routing section,
no leg is queued until at least TWO of the four retention builds are buildable -- adjudicating a
leg in isolation is how a confident-but-wrong elimination enters the frozen ledger, and the
780/781/782 cluster is the validating instance.

## Validation status (as built, 2026-07-18)

Six contracts appended to `ree-v3/tests/contracts/test_mech457_bootstrap_explorer.py` (C12-C17;
17 pass in that file). Full `ree-v3` suite: **1649 passed, 0 failures** -- backward compatibility
confirmed rather than asserted.

The two load-bearing checks:

- **C14** trains the same seed twice and asserts a schedule returning `c` is **bit-identical** to
  passing the float `c` (weight-vector delta exactly `0.0`). This is the guard regression: it fails
  if the auxiliary's `if` reads the constant instead of the effective coefficient.
- An end-to-end three-cell run confirms the cells produce **distinct policies** -- weight deltas
  `||constant - off|| = 0.039`, `||annealed - off|| = 0.030`, `||annealed - constant|| = 0.015`,
  with realised trajectories `constant` 0.5 -> 0.5, `annealed` 0.5 -> 0.0, `off` 0.0 -> 0.0.

No experiment is queued. The GOV-FANOUT-1 two-leg threshold is now met (this build plus
`mech457_distributional_critic`, implemented the same day), but queueing remains a separate
decision and was explicitly out of scope for this build.

## Related claims

MECH-457 (stays candidate / v3_pending -- this build promotes and demotes nothing), INV-088,
`mech457_competence_bootstrap_explorer` (parent substrate, IMPLEMENTED),
`mech457_distributional_critic` / `mech457_policy_kl_anchor` / `mech457_consummatory_act` (sibling
retention builds).
