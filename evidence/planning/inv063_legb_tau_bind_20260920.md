# INV-063 leg B: headroom and the asserted direction trade off against each other in tau

**Status: AWAITING USER REVIEW. Nothing here has been written to claims.yaml or any other
registry. The four-arm intake ladder was NOT queued.**

- Session `metaworker-science-20260919-inv063-four-arm-intake-ladder` (ree-cloud-4), 2026-09-20,
  acting on the green branch of the V3-EXQ-1069 go/no-go.
- V3-EXQ-1071 was reserved for the ladder and is **UNUSED** -- no script, no queue entry.
- **This is the THIRD stop on this item. Per the campaign's own "two stops means stop" rule I am
  REPORTING rather than raising a third decision chip.**

---

## 1. What went right, and it is most of it

V3-EXQ-1069 PASSED on linux (`inv063_p1_intake_ladder_gradeable`, `non_degenerate: true`,
go/no-go **green**, 6.57h). P1 held on seeds 42 and 456 (registered spread 0.3939 and 1.6914)
and failed on 123 (0.2410, just under the 0.25 bar) -- exactly the 2/3 the `power_note` said to
expect on linux.

Worth recording: **the episode-truncation confound flagged by 1069's red-team does not explain
its result.** On both P1-passing seeds the late-in-episode MEL gradient is *stronger* than the
raw one (seed 42: 0.9117 late vs 0.3939 raw; seed 456: 3.1774 vs 1.6914). On the failing seed
123 the late gradient inverts (-0.2176). The `mel_mean_pe_late_in_episode` telemetry added for
that red-team finding is what makes this visible.

A feasibility probe then confirmed that **798a's configuration plus the full sleep stack lights
up every instrument P1-P5 and leg A need**: 221 VALENCE_SURPRISE writes over 240 waking steps,
`_pe_ema` 0.00622 so the realised `surprise_weight` is 0.0311 and **not** pinned at its 0.3
fallback, `sws_n_writes` 5.0, `rem_n_rollouts` 10.0, `cross_module_consolidation_updates_e2_world`
8.0, cycle fired, MEL variance non-zero. None of that is the problem.

## 2. A correction to my own alarm, before the actual finding

The feasibility probe measured InfoNCE = 23.99 at `tau = 1e-3` against `ln(64) = 4.159` and I
read it as numerical breakdown, i.e. as the pinned tau failing to transfer from the dims-16 /
5x5 regime where I measured it to 798a's dims-32 / 12x12 regime.

**That reading was wrong and I am withdrawing it.** The probe ran with no P0. On a *converged*
798a-config base the battery's diagonal squared distance falls 0.2149 -> 0.00217, and at
`tau = 1e-3` the readout sits at **18.54% headroom below ln(K)** -- comfortably above the 5%
floor. The user's ratified pin is NOT numerically broken in the regime the ladder would use.

## 3. The actual finding: no tau satisfies both constraints

Measured on 798a's configuration, seed 42, converged base (`conv_rel_drop` 0.9899, P0 = 1800
E3-selection steps), one sleep cycle, K = 64 so `ln(K)` = 4.1589:

| tau | headroom (% of ln K) | readable (>5%)? | across-sleep delta | direction as asserted? |
|---|---|---|---|---|
| 10 | 0.01% | no | +1.76e-05 | yes |
| 1 | 0.06% | no | +1.75e-04 | yes |
| 0.1 (shipped) | 0.62% | no | +1.55e-03 | yes |
| 0.03 | 2.02% | no | +3.56e-03 | yes |
| **0.01** | **5.65%** | **yes** | **-7.18e-04** | **no** |
| **0.003** | **14.61%** | **yes** | **-7.68e-02** | **no** |
| **0.001 (the pin)** | **18.54%** | **yes** | **-3.89e-01** | **no** |
| 1e-4 | -282% | no (breakdown) | -4.40 | no |

**Readability requires `tau <= 0.01`. A positive across-sleep delta requires `tau >= 0.03`.
There is no overlap.** The crossover sits between them.

INV-063 C1 leg B is "the ACROSS-SLEEP **IMPROVEMENT** in world-forward prediction error ...
falls monotonically with intake". At every readable tau the improvement is **negative** -- which
is the same condition that disqualified the 701b MSE readout and was the entire reason leg B was
re-pointed to InfoNCE (staged doc `inv063_legb_dv_readability_staged_20260919.md` sec 2, and
GFLAG-0364).

**Why this looks structural rather than a tuning accident.** As `tau -> 0` the softmax sharpens
toward a hard nearest-neighbour test, which a sleep pass makes worse because it perturbs an
MSE-converged head (the E1-vs-E2 argument in GFLAG-0360). As `tau -> infinity` the loss flattens
toward `ln(K)`, where every delta is tiny and positive but the readout carries no information.
Headroom and direction are therefore expected to trade off in tau, not to have a window.

### 3a. Limits of this measurement, stated rather than papered over

- **n = 1 seed.** Seed 123's P0 was still running when the shell timeout fired; only seed 42
  completed. The *shape* of the trade-off is clear on that seed; its exact crossover is not
  established across seeds.
- **P0 was 1800 steps, not the 5400** the ladder would use. `conv_rel_drop` already reached
  0.9899, but further convergence changes the distance scale and could move the crossover.
- **One sleep cycle**, not the multi-cycle design.

So this is enough to say "do not spend ~8h on a design whose leg B may be unreadable", and not
enough to say "leg B is unreadable, convert the claim".

## 4. Options, recommendation first

**(c) RECOMMENDED -- fold the question into the ladder run instead of spending another
diagnostic.** Pin `tau = 1e-3` as ratified (it has the headroom the user asked for), but ALSO
record the across-sleep delta at the full tau ladder in every cell -- that is re-evaluating a
fixed distance matrix, microseconds per cell -- and PRE-REGISTER that if leg B's delta is
negative at the pinned tau across arms, the run self-routes to a `leg_b_dv_sign_inverted` label
and does NOT read C1 leg B. That spends the compute once, cannot produce a false F1, and leaves
the data to re-read leg B at another tau without re-running. It does require accepting a new
REFUSAL route, which is why it is the user's call and not mine.

**(b) Pin `tau = 0.03`** -- the largest tau with a positive delta (+3.56e-03). Costs readability:
2.02% headroom, below the 5%-of-ln(K) floor. That floor is *my* construct (V3-EXQ-1063's
`INFONCE_HEADROOM_FLOOR_FRAC`), not registered and not user-ratified, so relaxing it is a
legitimate call -- but it is a call, and the readout would then be carrying a signal ~4% of its
own available range.

**(a) Pin `tau = 1e-3` and read the DEGRADATION** rather than the improvement -- i.e. test
whether the across-sleep *loss* varies monotonically with intake. Informative, but it inverts
leg B's sign convention and is not what the registered text says.

**(e) Convert INV-063 to `substrate_conditional`** via its own escape hatch. Leg B has now
failed to produce a readable across-sleep improvement on BOTH readouts -- 701b MSE negative on a
converged base (9/9 cells), SD-056 InfoNCE negative at every readable tau (n=1). The claim's own
text calls this conversion "a legitimate, useful outcome". On n=1 I would not recommend it yet.

## 5. What was NOT done

No experiment script was written and no queue entry appended. `V3-EXQ-1071` is reserved and
unused. `claims.yaml`, `substrate_queue.json` and `experiment_proposals.v1.json` are untouched.
GFLAG-0364 stands as raised.
