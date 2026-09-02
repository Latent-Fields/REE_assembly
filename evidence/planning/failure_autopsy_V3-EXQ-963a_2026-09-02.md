# Failure autopsy -- V3-EXQ-963a / MECH-063 (ii) + SD-069 tonic-phasic dissociation

Generated 2026-09-02T05:04:59Z. Status: **confirmed** (interactive gate, 2026-09-02).
Red-team pass: Fable, verdict **CONTESTED** -- the contest was accepted and this artifact was
rewritten. The superseded reading is recorded below rather than deleted.

## What this autopsy first concluded, and why it was wrong

The first draft read the failure as **sampling starvation**: 16 of 20 cells hit the
`MAX_ENV_STEPS_PER_CELL` 2400 cap, the R5 capability gate failed on one cell by 4.6e-4, and the
manifest's own `sampling_shortfall` block warns that a step-cap shortfall "is a SAMPLING failure,
not a substrate capability failure". That reading is **withdrawn**. It also re-charged a claim the
predecessor autopsy `failure_autopsy_V3-EXQ-963_2026-08-30` had already refuted on the identical
16/20 profile, without engaging it -- the exact re-adjudication failure the skill warns about.

Two pillars, both recomputed from the manifests' own cells, refute it.

### Pillar 1 -- the phasic burst no longer decays

Event-tick rate (`n_event_ticks / n_e3_selects`) on PHASIC-ON cells, same burst config:

| seed | 963a T0P1 | 963a T1P1 | 779a T0P1 | 779a T1P1 |
|---|---|---|---|---|
| 11 | 0.546 | 0.496 | 0.083 | 0.132 |
| 17 | 0.647 | **0.847** | 0.085 | 0.076 |
| 23 | 0.390 | **0.884** | 0.012 | 0.007 |
| 29 | 0.513 | 0.480 | 0.072 | 0.079 |
| 37 | 0.466 | 0.501 | 0.136 | 0.105 |

Seed 23 T1P1 fires on 1489 of 1684 selections. A "transient" occupying up to 88% of ticks is a
quasi-sustained regime. This is why C2's dominance clause (driver:864-866) fails on seeds 11 and
23 by 5-13x off hundreds of event ticks, and why the single quiescent-tick shortfall (seed 23
T1P1, 195/200) exists at all -- **it is a symptom of the burst never decaying, not a sampling
accident.**

### Pillar 2 -- the warmed baseline has no entropy headroom

T0P0 `S_sustained_entropy`, against the 0.02-0.98 band:

| seed | 963a | 779a |
|---|---|---|
| 11 | 0.0611 | 0.2979 |
| 17 | **0.0195** | 0.5108 |
| 23 | 0.1530 | 0.6095 |
| 29 | 0.1154 | 0.2784 |
| 37 | 0.0771 | 0.1523 |

A 3-26x collapse on **every** seed under the SD-074 warmup. The R5 failure is reproducible and
structural across 963 and 963a; seed 17 is the tail of a systematic collapse, not a fluke.

## Consequences

- **The named fix cannot produce a result.** Raising the step cap can at best rescue seeds 29 and
  37, giving 3/5 against `MIN_SEEDS 4`.
- **The near-miss framing was misleading.** Had seed 17 cleared 0.02, the driver would have
  emitted FAIL / **weakens** on 1/5 dissociating seeds (driver:1041-1046), not a positive.
- **What the run does establish positively:** the 963 `probe_warmup` repair worked. R3
  `tonic_axis_live` 1.0, lift 1.000 on 10/10 TONIC-ON cells (computed from applied temperature,
  `agent.py:12551`; it was 0.0 in 963). This discharges the SD-PROBE-WARMUP failure record.

## Process defects recorded

- The label logic (driver:1005-1034) **never reads** the `sampling_shortfall` block it ships
  (computed :1003, stored passively); the bare `if capability_unmet:` gives capability-kind
  unconditional precedence. So the emitted `substrate_not_ready_requeue` is unreliable in *both*
  directions.
- SD-069's own `what_would_answer` prescribed raising the 2400 cap and **explicitly forbade** the
  `substrate_not_ready_requeue` label for a starvation run. The driver honoured neither. Nothing
  enforces `what_would_answer` anywhere.
- `substrate_stable_across_run: false` -- the on-disk hash drifted mid-run (3 `ree_core` commits
  inside the run window).
- Carried forward from 779b and not closed: `statistics.pstdev` robustness idiom (driver:841-844)
  despite `_lib/robustness_bars.py` existing; and no `=== HYPOTHESES UNDER TEST ===` block.

## Four-layer diagnosis

| Layer | Status |
|---|---|
| Claim alignment | intact (untested) -- neither axis measurable |
| Biological reference | clear -- LC tonic/phasic dual-mode gain control |
| Prerequisites | present (R1-R4 met) |
| Implementation | **partial** -- tonic lever fixed; phasic regulator does not decay |
| Environment | adequate |
| Measurement | misleading -- asked to find a transient that never ends |
| Integration | coupled but unstable |
| Scale | adequate (readiness floors met >=17x) |

**Failure-location (GOV-FAILLOC-1): MIXED (MECHANISM + MEASURES).** Not chargeable to REE.

## Re-derive brake -- FIRES

MECH-063's 5th hit (threshold 2). The first draft released the brake on the sampling theory; that
release is **withdrawn**. This target owes a substrate build, so the R3 instrument carve-out does
not apply. **A V3-EXQ-963b that merely raises the step cap is REFUSED.** A successor is admissible
only after the burst is shown to decay on a warmed agent and R5 headroom is restored.

## Routing (confirmed at gate)

`implement-substrate`. Create `sd_phasic_burst_decay_and_warmup_headroom` (priority 1, severity
corrupting): bound the burst duty cycle, and either restore warmup headroom or re-derive R5's band
for warmed agents. Both verified before any further 963-lineage letter.
