# DV-headroom, the second direction: is "the null sits below the architectural floor" mechanically detectable?

- **Status:** design record / probe resolution. **No code was changed** (see section 6 -- both target files are owned by another session, and the primary finding removes most of the reason to change them).
- **Written (UTC):** 2026-09-07T17:49Z by session `cool-sutherland-9d984d` (Mac `DLAPTOP`, umbrella worktree; claims `cool-sutherland-9d984d`, `-rec`).
- **Chip:** `chip-20260907-dv-headroom-trivially-satisfiable-direction`.
- **Motivating finding:** `exq_wpfield_h2_dv_range_probe_20260907.md` (leg H-wpfield-zworld-interface; a random 275->32 linear projection retains 78% of the raw decodability lift, so H2's pre-registered null is refuted by Johnson-Lindenstrauss alone).
- **Surfaces examined (read-only):** `ree-v3/validate_experiments.py::criterion_exceeds_achievable_range_lint`, `ree-v3/experiments/_metrics.py::{dv_achievable, dv_headroom_check, p0_readiness_gate}`, `ree-v3/tests/contracts/test_criterion_exceeds_achievable_range_lint.py`.

---

## 1. The question, and the answer

**Question.** The DV-headroom class implements one direction of its defect: a registered threshold ABOVE the range the configuration can produce (unsatisfiable). Is the opposite direction -- the declared null sitting BELOW the architectural floor, so the run is decided by construction -- mechanically detectable, or is it irreducibly a red-team judgement?

**Answer, in three parts:**

1. **The motivating case (H2) needs NO new machinery.** It is not a second direction at all; it is the SAME direction measured against the wrong control arm. The existing, unmodified `dv_headroom_check` refuses it (section 3). What was missing was not a check but the requirement that the control arm be the ARCHITECTURAL FLOOR rather than a null.
2. **A genuinely distinct second sub-direction does exist** -- the floor arm already SATISFIES the load-bearing criterion (section 4) -- and it is recurrent: four historical cases, none of which the existing lint or gate fires on.
3. **Neither is detectable as a STATIC LINT**, and this is a measurement, not an opinion (section 5). 0 true carriers in 1465 drivers; the discriminating fact is never in the source.

Work-graph debt classification (`docs/architecture/work_graph_debt_vocabulary.md`): the node entered as `complex (probe-gated)` and the probe has RESOLVED it. It splits:

| sub-question | resolves to |
|---|---|
| (2a) threshold below the achievable minimum (H2) | **not debt at all** -- already covered; a documentation/authoring gap, not a build |
| (2b) floor arm already satisfies the criterion | `complicated (buildable)` -- a small opt-in runtime check, blocked only on file ownership |
| (2b) as a static lint | `mystery (known data)` -- the source is all there and no additional fact makes it work; the resolution is to REFRAME to the runtime/design stage, not to gather more |

---

## 2. What the chip's framing got wrong, and why it matters

The chip described H2 as "the criterion is TRIVIALLY SATISFIABLE and the run is decided by construction in the eliminate direction". Read against the driver-level criterion that H2's pre-registration implies -- `zworld_lift <= NULL_TOL` -- that is the wrong way round:

- H2's criterion is trivially **VIOLATED**, not trivially satisfied. The architectural floor forces `lift >= ~0.145`, so a bar at ~0.02 is **unsatisfiable**.
- What is trivially reached is the **complementary verdict** ("H2 eliminated"). That is a consequence of the criterion being unsatisfiable, not a separate defect.

So H2 is the existing class's own defect -- *the registered threshold lies outside the range the configuration can produce* -- with the threshold below the achievable MINIMUM instead of above the achievable MAXIMUM. The class is even named for the general form: "criterion exceeds achievable RANGE".

This matters because it changes the remedy from "build a new gate" to "pass the right arm", which is a much cheaper and much more reliable fix.

---

## 3. H2 is caught by the EXISTING gate, unmodified

`dv_headroom_check`'s `control_values` is documented as "the CONTROL arm's realised dynamic range". Nothing in it requires the control arm to be a null -- that was an authoring convention, not an API constraint. Pass the ARCHITECTURAL FLOOR arm instead, and the required movement from that floor to the bar becomes the threshold:

```python
floor = [0.185, 0.155, 0.145, 0.173, 0.177]      # untrained SplitEncoder, 5 seeds (probe record)
required_drop = mean(floor) - NULL_TOL           # 0.1670 - 0.02 = 0.1470
dv_headroom_check("dv_headroom_h2_null_reachable_from_floor",
                  dv_name="zworld direction-decodability lift (drop from architectural floor)",
                  criterion_threshold=required_drop, control_values=floor, statistic="range")
```

Executed against the shipped `_metrics.py` at ree-v3 HEAD:

```
floor mean    = 0.1670
required drop = 0.1470
achievable    = 0.0400   (the floor arm's own realised range)
met           = False     -> 3.7x shortfall
GATE          : P0NotReady raised -> substrate_not_ready_requeue
```

and the reason string composes correctly with no changes:

> DV HEADROOM UNMET: zworld direction-decodability lift (drop from architectural floor) can only reach 0.04 in this configuration (range over 5 finite value(s)), against a required 0.147 (criterion threshold 0.147 x margin 1) -- a 3.7x shortfall. No outcome of this run could have shown the registered effect.

**Therefore: no extension is owed for (2a).** The owed artefact is guidance -- in `/queue-experiment`'s "measure the DV range at probe scale before pre-registering" step and in `dv_headroom_check`'s docstring -- saying that **when a criterion's passing side requires movement AWAY from an information-free configuration, the control arm must BE that configuration**, not a null.

---

## 4. The genuinely distinct sub-direction (2b), and its four historical cases

Distinct defect: **the floor arm already SATISFIES the load-bearing criterion**, so the passing verdict is reachable without the manipulation. The existing gate cannot express this -- it asks only whether the DV can MOVE far enough, never whether an information-free configuration has already arrived.

Corpus cases, in the corpus's own words:

| run | criterion | what the corpus recorded |
|---|---|---|
| **V3-EXQ-622** (2026-06-01) | `approach_commit_rate >= 0.01` | "trivially satisfied by 2/3 seeds ... despite z_goal at 1e-14 and 1e-3 ... cannot distinguish z_goal-driven approach from approach by other means with collapsed z_goal" |
| **V3-EXQ-723** (2026-07-09) | `compactness < 0.10`, `retention >= 0.80` | "trivially satisfied by any weak nonzero linear signal ... by any weak nonzero linear ridge map in a 112-dim latent" |
| **V3-EXQ-884** (2026-08-03) | `n_subgoal_credits > 0` (readiness gate) | "the gate's own bar is trivially satisfied by 2 credits, which is nowhere near the MANY discrete credit events the design requires" |
| **V3-EXQ-920a** (2026-08-16) | -- | "the criterion cannot fail when the mechanism it monitors never fires" |

And the **positive control** -- the design that got it right, and the precedent that would justify a harness abstraction:

**V3-EXQ-1002** carries a `zworld_untrained` NEGATIVE CONTROL matched in construction, parameter count (21,381, identical to the verdict arm's adapter), data, adapter and standardiser, and sets its effective per-seed bar to

    max(AGREEMENT_BAR, trivial_baseline + AGREEMENT_ELEVATION_MIN, untrained_control + UNTRAINED_CONTROL_MARGIN)

recorded as `interpretation.effective_pass_threshold_per_seed`, with an explicit `untrained_clears` flag carried into the verdict grid. Its own rationale states the principle: *"This converts an absolute-threshold design -- which requires knowing every shortcut's ceiling in advance -- into a DIFFERENTIAL one, which does not."* That flag IS the (2b) detector, hand-rolled and twice red-teamed.

This is the same precedent shape the DV-headroom class used to justify itself (V3-EXQ-777a having hand-rolled the guard locally). It is therefore a legitimate argument for a harness abstraction -- see section 6 for the proposed shape and why it was not built here.

---

## 5. Why a STATIC LINT is refused (measured, not asserted)

Two scans over all 1465 `experiments/*.py` at HEAD:

| scan | result |
|---|---|
| load-bearing CEILING criterion on a derived-range statistic (`gap`/`lift`/`delta`/...) with a positive constant threshold -- the naive "null bar" shape | **2 files (0.1%)**, and **both are false positives**: `COORD_WRITE_TOL = 1e-9`, `EPS_RULE = 1e-7`, `EPS_RESIDUE = 1e-6` are numerical-tolerance assertions, not scientific nulls |
| ANY load-bearing ceiling criterion with a positive constant threshold | 33 files (2.3%); threshold distribution **18 at <= 1e-6** (OFF-arm silence assertions: `FROZEN_SILENCE_EPS`, `C1_OFF_INACTIVE_CEIL`), 24 above 0.05 (absolute-level bars), 9 in the 1e-3..0.05 band |

**True carriers of either sub-direction: zero.** Every case in section 4 was caught POST-HOC by a failure autopsy; H2 and V3-EXQ-1005 were caught PRE-HOC by an explicit DV-range probe at design time, before a driver existed.

The structural reason a lint cannot work, and the part to keep if this is ever revisited:

> **The discriminating fact -- what value an information-free configuration produces -- is never in the source.** In V3-EXQ-622 the source says `>= 0.01`; nothing in the file says a collapsed `z_goal` already yields 1.0. In V3-EXQ-723 nothing says any weak linear map clears the bar in a 112-dim latent. In H2 nothing says a random projection retains 78% of the lift. That number comes from RUNNING something.

And the same source shape carries opposite verdicts: for `FROZEN_SILENCE_EPS` the architectural floor is exactly 0 by construction (a disabled channel emits nothing -- no defect, and 18 of the 33 ceiling criteria are this), while for H2's lift the floor is +0.167 (defect). A lint distinguishing them would need a per-experiment domain model, which is precisely the "worse than none" outcome the chip named.

**Refused. Do not re-propose a static lint for this class.** The lever is the design stage -- `/queue-experiment` Step 4.5 red-team and the "measure the DV range at probe scale before pre-registering" rule -- plus the runtime check in section 6.

---

## 6. What is owed, and why it was not built in this session

**Proposed shape (2b), for whoever picks it up.** A sibling constructor in `experiments/_metrics.py`, keeping `kind: "dv_headroom"` so the lint and the gate stay ONE feature (the contract file's stated constraint) and the REE_assembly indexer needs no change (it recomputes `met` from measured/threshold/direction and is kind-agnostic):

```
dv_floor_control_check(name, *, dv_name, criterion_threshold, floor_values,
                       criterion_sense: "floor" | "ceiling", separation_margin=..., ...)
    measured  = separation of the floor arm from the bar, signed so that
                LARGER == SAFER:
                  criterion_sense="floor"   (pass is `m >= T`):  T - max(floor)
                  criterion_sense="ceiling" (pass is `m <= T`):  min(floor) - T
    threshold = separation_margin
    direction = "lower"          # met iff separation >= margin
    achievable_statistic = "floor_separation"   # new label, refused by
                                                # dv_achievable() exactly as
                                                # "explicit" already is
```

Two properties are load-bearing and must survive:

- **`direction` stays `"lower"`**, so `_validate_dv_headroom_check`'s UPPER-bound refusal -- a contract-tested safety property whose docstring explains that an upper bound "would pass a pinned DV and fail a live one" -- is untouched. Expressing the check as a signed separation rather than as a bound on the floor value is what buys this.
- **`criterion_sense` is REQUIRED, never inferred.** The two senses give opposite signs and there is no safe default.

The check consumes the floor arm's values; it does not construct them. Constructing an information-free surrogate for a given manipulation is a domain judgement and stays with the author -- the same posture `dv_headroom_check` already takes toward the control arm.

**Why not built here.** Both target files are held by another session under an atomic coordinator claim:

| file | owner | task |
|---|---|---|
| `ree-v3/validate_experiments.py` | `peaceful-kare-a6a78f-993a` (2026-09-07T17:29Z) | campaign W4-HK bundle B item 4 |
| `ree-v3/experiments/_metrics.py` | `peaceful-kare-a6a78f-dvreason` (2026-09-07T17:37Z) | W4-HK item 5 -- recomposing `dv_headroom_check`'s refusal reason |

`task_claim.py open` returned NOT OWNER on both. The stop is also substantively right, not merely procedural: HK-B item 5 is actively rewriting the very function a floor-control sibling would sit beside, so landing on top of it would be a read-modify-write collision on in-flight work.

Follow-on is chipped rather than inlined, per the CLAUDE.md chip rule (this is `/implement-substrate` work, not `/governance` or `/failure-autopsy` work).

---

## 7. GOV-HELDOUT-1 record

Checked the proposed (2b) wording against historical cases it was NOT written from. The seven canonical DV-headroom specimens (981 1.154, 993 13.1x, 994 25.6x, ...) are all the OPPOSITE direction and are **degenerate** here -- old and new give the same answer -- so none was counted. The motivating case (H2) was likewise excluded.

**Four non-degenerate cases** (old wording silent, proposed wording fires):

| case | why the EXISTING lint/gate is silent | proposed (2b) |
|---|---|---|
| V3-EXQ-622 | `approach_commit_rate >= 0.01` carries no `_DERIVED_RANGE_NAME_TOKENS` token, and is not multiplicative -- neither sub-case matches | fires: floor (collapsed `z_goal`) yields 1.0, clearing a 0.01 bar |
| V3-EXQ-723 | `compactness < 0.10` is a ceiling; `_compare_legs` normalises it so the "measured" side is the constant `0.10`, whose `leaf_names` is empty -- skipped | fires: any weak linear map clears both conjuncts |
| V3-EXQ-884 | `n_subgoal_credits > 0` has threshold 0, and scan 2 requires `t > 0` | fires: the floor (2 credits) satisfies the gate |
| V3-EXQ-920a | criterion monitors a mechanism that never fires; no threshold shape to match | fires: floor arm satisfies it vacuously |

**Negative control (must NOT fire):** V3-EXQ-1002, whose `untrained_control + UNTRAINED_CONTROL_MARGIN` conjunct puts the untrained floor at 0.695 against a 0.80 bar -- a 0.105 separation. The proposed check is silent there, which is the required behaviour: the rule must not fire on the design that already solved this.

**Outcome: PASSED** (4 differing cases + 1 negative control, threshold is 3). The check did not narrow the proposed wording; it did confirm that the (2a) half of the chip's framing was over-broad, which is recorded in section 2 rather than shipped.

Also re-run, per the chip: the corpus fire-count / non-vacuity guard on the existing lint. **1465 files, 111 fired = 7.6%** (pinned band 2.0%-15.0%, build-time 7.7%); both named specimens still fire. Unmoved -- **no re-pin owed**, and nothing in this session touched the lint.

---

## 8. What the next session inherits

- **Do NOT build a static lint for this class** (section 5, measured refusal).
- **(2a) is closed** -- it needs guidance, not code. The one-line rule: *when a criterion's passing side requires movement away from an information-free configuration, `control_values` must be that configuration's realised values, not a null.* Natural homes: `dv_headroom_check`'s docstring and `/queue-experiment`'s DV-range step.
- **(2b) is `complicated (buildable)`** and blocked only on W4-HK bundle B releasing `experiments/_metrics.py`. Shape in section 6; a new adopter must also be added to `KNOWN_DV_HEADROOM_ADOPTERS` in the contract file, in the same commit.
- V3-EXQ-1002's driver is the reference implementation to read before building it.
