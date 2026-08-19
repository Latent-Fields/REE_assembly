# MECH-236 CEM wanting causal ablation -- ALREADY DISCHARGED by V3-EXQ-931; residual routes to /implement-substrate

**Status: AWAITING USER REVIEW.**

- Author: headless metaworker chip `chip-20260816-mech236-cem-wanting-causal-ablation`
- Date: 2026-08-19T08:16:36Z
- Session: `metaworker-chip-20260816-mech236-cem-wanting-causal-ablation` (DLAPTOP, umbrella worktree)
- Outcome: **NO EXPERIMENT QUEUED, deliberately.** The named work is already done; queueing
  another run would duplicate V3-EXQ-931 and would violate a standing readiness gate that the
  same governance cycle ratified 92 minutes before it spawned this chip.

---

## 0. One-paragraph summary

Chip `chip-20260816-mech236-cem-wanting-causal-ablation` asks a `/queue-experiment` session to
queue the experiment specified by
`evidence/planning/cem_wanting_weight_causal_ablation_design_2026-08-14.md`. **That experiment was
already queued as V3-EXQ-931 on 2026-08-14 and has already RUN** -- a real (not dry-run) 5-arm x
5-seed execution on `ree-cloud-2`, 1446.7s, `outcome: FAIL`, `evidence_direction:
non_contributory`, with all four readiness gates P0/P1/P2/P3 PASSing and non-degenerate. Its
predecessor chip `chip-20260812-cem-wanting-weight-causal-ablation` is `status: done` recording
exactly that. The 2026-08-16 governance cycle that spawned *this* chip had the result in hand:
its own human-gated autopsy routes V3-EXQ-931 to **`implement-substrate`**, not to
`queue-experiment`. This chip is therefore a **misrouted duplicate**, and the genuinely owed
follow-on is a substrate build that is presently staged nowhere.

---

## 1. Evidence that the named experiment is already discharged

| fact | source |
|---|---|
| The design doc's own section 7 says "**QUEUED as `V3-EXQ-931`** (2026-08-14), via `/queue-experiment`" | `evidence/planning/cem_wanting_weight_causal_ablation_design_2026-08-14.md` (REE_assembly `e27ae08756`) |
| Script exists and is on trunk | `ree-v3/experiments/v3_exq_931_cem_wanting_weight_selection_authority.py`, `ree-v3` `ff69ac7e85` (2026-08-14T12:09:23Z) |
| It was POSTed to the coordinator (the design doc's one open operator action) | chip `chip-20260814-exq931-coordinator-post`, `status: done` |
| **It RAN, for real** | manifest `v3_exq_931_cem_wanting_weight_selection_authority_20260814T123949Z_v3.json` -- `dry_run: false`, `machine: ree-cloud-2`, `elapsed_seconds: 1446.75`, `seeds: [42,43,45,46,47]`, `substrate_commit a57e6dd832` clean |
| The run was fully gated and non-vacuous | `interpretation.criteria`: P0/P1/P2/P3 all `passed: true`; `criteria_non_degenerate` all `true`; the single load-bearing criterion `C_AUTH_operating_weight_has_authority` `passed: false` |
| It has been governance-reviewed and autopsied | `failure_autopsy_931-932-wanting-authority-cluster_2026-08-16.{md,json}`, `status: confirmed`, `human_gate.confirmed_utc 2026-08-16T18:41:10Z` |
| Its failure record is filed against the substrate entry | `substrate_queue.json` -> `modulatory-bias-selection-authority.failure_record`, `added_utc 2026-08-16T19:11:21Z`, `resolved: "open"` |

The predecessor chip's resolution note is unambiguous: *"DONE. Design landed + experiment queued as
V3-EXQ-931 (renamed from 929 after a live ID collision)."*

**Nothing here is machine-local.** Every artifact above is git-tracked and shared, so the headless
"absence is only evidence on the owning box" caveat does not apply -- and the chip's `origin_host`
is `DLAPTOP`, which is this box anyway.

## 1a. What V3-EXQ-931 actually measured

Reproduced here so a future session does not have to re-derive it:

- `selection_flip_rate = 0.0` in **5/5 seeds** at `wanting_weight = 0.5` (the value
  `HippocampalConfig`'s docstring prescribes for goal-directed navigation).
- **In-run positive control clears**: `ARM_W5000` flips the CEM elite-selection argmin on
  43/104 and 96/98 *genuine* refits, so the null is demonstrated non-vacuous.
- `wanting_authority_ratio ~= 0.0037` -- the wanting term's cross-candidate spread is ~270x too
  small to move the argmin at the operating weight.
- `c_behav_proximity_gap_vs_ablated`: `ARM_W05 0.0`, `ARM_W50 0.0`, `ARM_W500 0.00033`,
  `ARM_W5000 0.0` -- i.e. **bit-identical behaviour even at w=5000 with 80% of argmins flipped**,
  because `REEAgent.select_action` re-scores the pool downstream with `self.e3.last_scores`.

That last line is the finding that matters for what comes next: **AUTHORITY and behavioural
THROUGHPUT are independent failures.** Fixing authority alone buys flipped picks and no
behavioural change.

---

## 2. Why no further experiment was queued (the load-bearing judgment)

Three independent reasons, any one of which is sufficient:

1. **It would be a duplicate.** The design named as "the spec" by this chip *is* V3-EXQ-931.
   Re-queueing it reproduces a null that is already measured, understood, autopsied and filed.

2. **The same governance cycle routed it elsewhere.** `failure_autopsy_931-932-wanting-authority-cluster_2026-08-16`
   (confirmed, human-gated 18:41:10Z) sets, for the V3-EXQ-931 target,
   `routing: "implement-substrate"` and `recommended_substrate_queue_entry.action: "amend"`
   against `modulatory-bias-selection-authority`. The sibling target V3-EXQ-932 is the one routed
   `queue-experiment` -- and that is a *different* chip
   (`chip-20260816-932a-coupling-reinstrument`), which was running concurrently with this one.

3. **A new behavioural falsifier would violate a gate this cycle just ratified.** The autopsy's
   `implementation_hint_addendum` pre-registers a standing readiness assertion:

   > "a scoring-layer lever must report the ratio of its own cross-candidate spread to the
   > dominant term's, and that ratio must be COMPETITIVE (not merely nonzero) **before any
   > behavioural falsifier is queued**."

   The measured ratio is `0.0037`. It is not competitive. And per the throughput finding, a
   behavioural DV **cannot be read off the CEM elite stage at all** until throughput is fixed --
   which is precisely what the chip's own brief warns ("Any DV must not be read off the CEM elite
   stage unless throughput is also addressed") and what its escape clause anticipates ("if the fix
   is in flight, your run may need to gate on it"). The fix is **not** in flight: the failure
   record is `resolved: "open"` and nothing is staged.

## 3. Process finding -- the chip contradicts its own cycle's ratified routing

Governance cycle `cranky-driscoll-126a36` on 2026-08-16 did all three of the following, in order:

| time (UTC) | action |
|---|---|
| 18:41:10Z | confirmed the autopsy at the human gate, routing V3-EXQ-931 -> `implement-substrate` |
| 19:11:21Z | appended V3-EXQ-931's failure record to `modulatory-bias-selection-authority` (its FOURTH confirmed call site) |
| 20:13:40Z | spawned **this** chip, asking a `/queue-experiment` session to queue the already-run design |

This is worth recording because the chip has now consumed **three** dispatch cycles without
producing an experiment, and the first two failures were each diagnosed as something narrower
than the real defect:

- an earlier worker gated on `GFLAG-0033` still being open, found it RESOLVED, and stopped;
- `/metaworker-repair` (2026-08-19T07:51:47Z) correctly fixed *that* trap by amending the
  stop-check -- but the amendment asserts "a genuinely owed experiment" is being abandoned, which
  is the half that does not hold. The flag's own resolution note, quoted in the amended brief,
  already recites V3-EXQ-931's completed results.

**The generalisable lesson:** a stop-check that names only a *flag* or a *design doc* cannot
detect that the design's experiment has already run. The cheap discriminator is to read the design
doc's own queue-status section and then look for the run_id in
`evidence/experiments/` -- which is what this session did, and it took one command.

---

## 4. What IS owed, and where it is staged

**Owed:** `/implement-substrate` on the 2026-08-16 amend to `modulatory-bias-selection-authority`
(`substrate_queue.json`), covering the two independent failures the autopsy names:

- **(a) AUTHORITY** -- extend the existing E3.select authority fix *upstream* to
  `HippocampalModule._score_trajectory`'s CEM elite selection, which the 2026-08-13 autopsy had
  already flagged as out of reach of the implemented fix ("flagged for a future session if this
  call site recurs" -- it has now recurred, with a dose-response and a positive control).
- **(b) THROUGHPUT** -- either propagate the CEM elite pick into E3's committed selection, or
  **document the CEM elite stage as advisory-only** so no future experiment reads a behavioural DV
  off it. The autopsy is explicit that (b) matters more than (a).
- **(c)** add the standing "competitive spread ratio" readiness assertion above.

**Staged nowhere, as of this writing.** Verified: no open chip in `TASK_CHIPS.json` names this
build; the only IGW ledger entry for the `sd_id` is `IGW-20260603-024`
(`completed_resumable` / `USEFUL_LANDED`, the original 2026-06-03 implementation), so IGW
auto-discovery has not staged the new amend either. A chip has therefore been recorded for it by
this session -- see the resolution note.

**Not owed here, but noted:** V3-EXQ-914b (the ghost-probe successor the 2026-08-13 autopsy routed)
has no script and no queue entry. That is a different lineage and a different chip's scope; it is
recorded only so the gap is visible.

---

## 5. Provenance

- All checks run from `/Users/dgolden/REE_Working` on `DLAPTOP`, 2026-08-19T08:11Z-08:16Z.
- `ree-v3/experiment_queue.json` held **0 items** at check time (queue fully drained), so the
  absence of a MECH-236/wanting entry there is not evidence either way; the evidence is the
  manifest and the git history, both cited above.
- This session opened its claim with `--allow-overlap` against a concurrent claim on
  `ree-v3/experiment_queue.json` held by `chip-20260816-932a-coupling-reinstrument`. That is a
  genuinely different experiment (the V3-EXQ-932 sibling target of the same autopsy, routed
  `queue-experiment`), not duplicated work. In the event this session appended nothing to the
  queue at all.
