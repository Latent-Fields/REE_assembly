# Endogenous readiness-precondition audit (2026-08-25)

**Status:** closed, incident-scoped. No standing-rule change shipped (GOV-HELDOUT-1 threshold not met).

## Motivating finding

V3-EXQ-813 (`v3_exq_813_survival_zeroed_ppo_latent_policy_probe_20260724T143333Z_v3.json`)
declared a readiness precondition `consumption_share_dominates_under_correction`: worst-cell
train-phase `consumption_share` (at the `W3_survival_zeroed` weighting) vs a 0.90 floor. It
**failed on both arms** (0.5717 latent / 0.8097 raw obs) and self-routed the whole run to
`substrate_not_ready_requeue`. The confirmed autopsy
(`failure_autopsy_backlog_2026-07-24.md`, section C3) had to **override this by user judgment**
to use the run's real finding at all: PPO on raw obs clears the D3 floor (9.03) while PPO on
the REE latent does not (0.5) under the identical objective — eliminating `H-policy-learning`
and elevating a representation/observation-interface hypothesis.

**Why the gate is circular.** At `w_survival=0.0` every survival-linked reward family is
deleted by construction (`survival_linked_share` reads exactly 0.0 on all six cells), so the
entire non-consumption residual is `harm`, which `_weighted` never reweights. Harm accrues
per-tick from the environment; consumption accrues only when the arm actually forages. So
consumption share is **low precisely when the arm forages little** — i.e. it is causally
*downstream* of `foraging_competence`, the DV the run existed to measure. The gate penalised
each arm for the very failure the experiment was designed to detect, and self-routed the run
away exactly when the interesting (low-competence) result occurred.

**Defect class.** This is distinct from the three magnitude/vacuity defect classes
`/queue-experiment` Step 3.5 already covers:
- NOT the V3-EXQ-643 magnitude-vs-range mismatch (statistic is correctly formed and correctly
  measured here — the problem is what it's measured *on*, not its shape).
- NOT the V3-EXQ-785 structural vacuity (unsatisfiable-from-pre-registered-config; this gate
  IS satisfiable, by a competent arm).
- NOT the V3-EXQ-779b worst-cell/mean or two-sided-bound issues (worst-cell reporting here is
  correct).

The missing property is **independence**: a readiness statistic must not be causally
downstream of the DV it gates.

**Forward fix already shipped**, scoped to this one driver: V3-EXQ-948
(`ree-v3` `189c4025ad`, `v3_exq_948_observation_interface_re_representation_probe.py`) replaced
the gate with `survival_linked_share_zeroed` (a **structural** assertion — worst-cell
`survival_linked_share` for the arm is exactly `<= 1e-9`, true by construction whenever the
correction actually landed, independent of the arm's foraging competence) plus
`harm_share_negligible_on_control` (measured on the `local_view_greedy` **positive control**,
never on an arm under test). Confirmed in the V3-EXQ-948 manifest: `survival_linked_share_zeroed`
measures `0.0` against `1e-9` on all four arms, `met: true`.

## Scope of this chip

Given the fix is scoped to one driver, this audit asked whether the *pattern* — a readiness
statistic computed per-arm from that arm's own training/eval outcome, where the statistic is
plausibly caused by (rather than independent of) the arm's performance on the run's own
load-bearing DV — recurs elsewhere in the corpus, per CLAUDE.md's GOV-HELDOUT-1 discipline: a
standing-rule addition needs >=3 genuine historical instances where old and new wording give
different answers, or it should ship as an incident write-up, not a general rule.

## Method

Scanned all `interpretation.preconditions[]` entries with `kind: "readiness"` across
`REE_assembly/evidence/experiments/*.json` (941 manifest files; 37 are pre-schema
free-text `interpretation` and carry no structured preconditions, correctly out of scope) and
all `PreconditionSpec(..., kind="readiness", ...)` declarations under `ree-v3/experiments/*.py`.
315 manifests carry at least one readiness precondition; 513 unique precondition names.

**Signature searched for:** a readiness statistic (a) computed on the SAME arm under test,
(b) from that arm's own trajectory/outcome during the same phase the load-bearing DV is drawn
from, and (c) plausibly caused by — rather than independent of — the arm's performance on that
DV. Excluded by construction: statistics measured on a fixed anchor/oracle/positive-control arm
(`greedy_oracle`, `local_view_greedy`, `ARM_POSCTRL`, etc.), manipulation checks measured on a
phase temporally/causally *prior* to the DV's phase (e.g. "did the BC install take before RL
began"), structural/config assertions, and instrument-liveness/non-degeneracy checks (variance
of a diagnostic channel exists at all) which gate on the mechanism being *exercisable*, not on
the arm's competence.

Grepped all 513 precondition-name/control-text pairs for self-referential phrasing ("for this
arm", "this arm's own", "\_share", "\_dominates", "\_rate", "supra_floor" family, "clears_floor"
family, "reproduces_incompetence", "install_took") and inspected each family's full
description/control text plus, for ambiguous cases, the arm's criteria in a representative
manifest.

## Candidates examined and disposition

| Precondition | Why it is NOT the pattern |
|---|---|
| `consumption_share_dominates_under_correction` (V3-EXQ-813, 1 run, 2 arms) | **THE confirmed instance.** Already fixed forward (V3-EXQ-948). |
| `post_bc_install_took` / `install_took_strict_majority` (n=18, n=18 across ~11 runs) | Measured **pre-RL** (post-BC warm-start), a manipulation check temporally/causally *prior* to the DV phase (retention/consolidation after sleep or RL). "Did the treatment take" is upstream of, not downstream of, the outcome under test. |
| `episode_outcome_spread_supra_floor`, `chunk_buffer_supports_size_range` (V3-EXQ-810a family) | Explicitly asserts the SAME statistic the load-bearing gate routes on, per the V3-EXQ-643 rule, but on a **structural enabling condition** (does the task have enough per-episode variance / episode length for the mechanism to fire at all) — not on the arm's competence axis. Description states this explicitly ("structurally impossible on a flat outcome stream"). |
| `replay_high_value_candidate_seed_fraction` (V3-EXQ-873a/892/896, "same validated gate") | Fraction of seeds producing *any* qualifying candidate — an enabling precondition for the mint decision (C2) to be attemptable at all, not a measure of whether the mint decision was correct. Upstream of the causal chain the DV sits in, not downstream. |
| `baseline_reproduces_incompetence`, `control_reproduces_incompetence`, `bias_head_reproduces_incompetence_at_d0` | Measured on the **baseline/control arm** (A0), whose designed role is to fail — a manipulation check on the reference condition, not on the treatment arm under test. |
| `weighting_sweep_changes_realised_composition` (V3-EXQ-808 lineage) | Measures the cross-level **RANGE** of `consumption_share` (a positive control: W3 vs W0 must differ by construction), not an absolute per-arm floor. Confirmed via V3-EXQ-808's own `n_term_families_nontrivial` precondition, which is explicitly `applies_to`-scoped OFF at `w_survival=0` specifically to avoid this class of defect (V3-EXQ-785 reasoning applied pre-emptively). |
| `d3_oracle_clears_floor`, `greedy_oracle_clears_floor_at_d3`, `local_view_greedy_clears_floor_at_d3`, `d0_greedy_oracle_clears_floor`, `easy_oracle_clears_floor`, etc. (n=10-35 each) | All measured on a **fixed oracle/greedy anchor policy**, never on the arm under test. |
| `pre_deval_approach_rate_supra_floor` (n=6) | Explicitly documented as "a positive control by construction, since the outcome is still valuable there" — measured on the pre-manipulation half of the same episode, functionally an anchor period. |
| `*_route_range_supra_floor`, `*_spread_supra_floor` families (channel/instrument liveness, n=1-19 each) | Gate on whether a diagnostic channel has any variance at all (is the instrument alive), not on the arm's task competence. |

No other family in the 513-name corpus matched the exclusion-narrowed signature.

## Disposition (GOV-HELDOUT-1)

**1 genuine instance found corpus-wide** (V3-EXQ-813's `consumption_share_dominates_under_correction`),
already superseded by a scoped forward fix in V3-EXQ-948. This is well short of the >=3
non-degenerate historical cases the held-out check requires before shipping a general rule to
`/queue-experiment` Step 3.5's diagnostic-adjudication question list.

**Per the held-out rule's own instruction: this absence of recurrence is itself the finding.**
No edit was made to `.claude/skills/queue-experiment/SKILL.md` or
`.agents/skills/queue-experiment/SKILL.md`. The defect is recorded here as incident-scoped
rather than generalised. If a second and third genuine instance surface in future runs, revisit
and add a Step 3.5 bullet at that point (draft wording, for reuse if that happens): *"Is the
readiness statistic independent of the load-bearing DV — measured on a positive control, an
anchor, or a structural/config property — rather than computed per-arm from the arm's own
outcome during the same phase the DV is drawn from? A per-arm outcome statistic that is caused
by (rather than independent of) low performance on the DV will fail precisely when the
interesting result occurs, self-routing the run away from its own finding (V3-EXQ-813)."*

No completed run's manifest was retro-edited; V3-EXQ-813's pre-registered emission stands as
recorded, with the autopsy override as the corrective record.
