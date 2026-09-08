# V3-EXQ-1007a NOT QUEUED -- the primary criterion C1 is satisfied by construction, and the reach check that was meant to catch it is window-blind

**Generated:** 2026-09-08T18:40:00Z
**Session:** `w5-freshfill-20260908` (campaign W5 fresh-design queue-fill)
**Chip:** `chip-20260908-exq1007a-reposed-exposure-dv`
**Driver authored, smoke-green, NOT QUEUED:** `ree-v3/experiments/v3_exq_1007a_mech536_eval_persistence_discriminator.py`
**Routing artifact:** `failure_autopsy_V3-EXQ-1007_2026-09-08.{md,json}` (CONFIRMED 2026-09-08T13:52:11Z, REE_assembly `33016d1a2f`; routing user-ratified at its gate)
**Red-team (Step 4.5, model `fable`):** **BLOCKING** -- findings file `scratchpad/redteam_1007a.md`
**Claims involved:** MECH-536 (primary), MECH-535 (read-across). **Neither is moved by this record.**

---

## 0. The one-paragraph statement

The V3-EXQ-1007a driver was authored in full against the six user-ratified changes, and it passes
every mechanical gate: 43 self-test checks, `validate_experiments --strict` clean with zero
warnings across all 37 checks, `--dry-run` exit 0 with all 14 arm ids exercised and the new
pre-screen exercised, `validate_recording --strict` clean. It is **not queued** because the
Step 4.5 adversarial design review returned **BLOCKING** on a finding that survives verification
against the predecessor's own recorded data and against a direct arithmetic check: **the primary
criterion C1 ("the latch abolished the ambitendency two-cycle") is satisfied by construction for
every latch depth k >= 2, and the orbit detector that would have caught this cannot see the
resulting orbit at the episode lengths this phenotype actually produces.** Both halves are
measured below, not argued. The consequence is that the letter's CHANGE (3) -- the per-k
orbit-histogram reach check, which the user ratified -- rests on an empirical premise ("k=4 broke
the orbit in V3-EXQ-1007") that the predecessor's data does not establish.

---

## 1. Finding 1 -- C1 is an arithmetic identity of the manipulation, not a measurement

C1's detector is `period2_cycle_present`, which looks for **strict two-cell alternation**
(`CYCLE_MIN_LEN = 6` steps of it). The manipulation is a **k-step action latch**: the frozen
reader's decision is held for k consecutive steps. Applied to a period-2 approach/withdraw
alternation, a k-latch does not break the orbit -- it **re-periodises it to period 2k over k+1
cells**.

Direct check, run at authoring time against this driver's own imported detectors (synthetic
k-latched trajectory, no substrate involved):

| k | episode len | `period2_cycle_present` | `bounded_orbit_period` (min_repeats=3) | `bounded_orbit_period` (min_repeats=2) | unique cells |
|---|---|---|---|---|---|
| 2 | 19 | **False** | 4 | 4 | 3 |
| 2 | 23 | **False** | 4 | 4 | 3 |
| 3 | 19 | **False** | 6 | 6 | 4 |
| 3 | 23 | **False** | 6 | 6 | 4 |
| 4 | 19 | **False** | **None** | **8** | 5 |
| 4 | 23 | **False** | **None** | **8** | 5 |
| 4 | 40 | **False** | 8 | 8 | 5 |

**`period2_cycle_present` is False in every cell of that table.** C1 passes when it is False, so
**C1 passes for every k >= 2, at every episode length, on a trajectory that is still perfectly
orbiting.** The latch cannot fail C1, because "period 2 becomes period 2k" is arithmetic.

This is the DV-symmetry-invariance failure class named in `REE_Working/CLAUDE.md` "Experiment
Scripts" / the `/queue-experiment` Step 3 table: a manipulation whose DV is invariant under it, so
the reading is fixed before the run. Here it is the mirror image -- the manipulation *trivially
satisfies* rather than *cannot move* the criterion -- but the defect is the same: **no outcome of
the experiment can falsify C1.**

**This is not a defect introduced by the letter.** It is inherited from V3-EXQ-1007 and was not
identified by that run's own red-team, by its confirmed autopsy, or by the six ratified changes.
The letter faithfully implements all six and is still blocked by it.

## 2. Finding 2 -- the reach check that was meant to catch exactly this is blind at the k it would select

CHANGE (3) exists because the autopsy recognised the re-periodisation risk at k=2 ("a k=2 latch on
a period-2 alternation is period-4 by construction"). The mitigation was a per-k **reach check**
reading `bounded_orbit_incidence`, so that an arm still orbiting is reported but not eligible to
carry the verdict. That mitigation does not work, for a reason visible in the table above.

`bounded_orbit_period` requires a window of `min_repeats * p` consecutive positions
(`BOUNDED_ORBIT_MIN_REPEATS = 3`, so **24 positions for p = 8**) and `break`s out of the search
when the episode is shorter. A k=4 latched orbit has period 8. **V3-EXQ-1007's `persist_k4` short
episodes are 19, 19, 19, 22, 22, 23, 23 steps** -- every one below 24.

From the predecessor's own manifest
(`evidence/experiments/v3_exq_1007_mech536_eval_persistence_discriminator_20260907T072349Z_v3.json`,
`persist_k4`, seed 42), all 20 episodes:

```
orbit_period_histogram: {"none": 20}      bounded_orbit_incidence: 0.0
n_steps 19  cycle False  orbit None  stationary 0.00  uniq 5
n_steps 22  cycle False  orbit None  stationary 0.10  uniq 5
n_steps 23  cycle False  orbit None  stationary 0.05  uniq 8
n_steps 200 cycle False  orbit None  stationary 0.98  uniq 4     <- wall-press
n_steps 200 cycle False  orbit None  stationary 0.96  uniq 9     <- wall-press
   ... (9 of 20 episodes are 200-step presses at stationary 0.84-0.98)
```

So `bounded_orbit_incidence` is **0.0** for `persist_k4` -- and the reach check reads exactly that
number. The check would therefore mark k=4 **ELIGIBLE**, and (per the smallest-eligible-k rule)
k=2 and k=3 **ineligible**, since at those periods (4 and 6) the window *does* fit and the orbit
*is* detected.

**The reach check would elect as "the k that breaks the orbit" precisely the one k whose orbit it
is unable to see.** That is a gate selecting on its own blind spot, and it is worse than having no
gate at all, because it manufactures the appearance of having checked.

## 3. What this does to the ratified premise

The autopsy's routing note states, and the user ratified, that "k=2 is EXCLUDED as a verdict arm
... k=3 is untested; k=4 broke the orbit in 1007". Sections 1 and 2 above show the third clause is
**not established by the data**: `orbit_period: None` on 20/20 k=4 episodes is fully explained by
the detector window (24 required, 19-23 available) and is exactly what a *still-orbiting* period-8
trajectory produces at those lengths. The distinction between "k=4 broke the orbit" and "k=4
re-periodised to period 8, undetectably" was never measurable in that run.

Correspondingly, the differential treatment of k=2 (excluded a priori) and k=4 (promoted to
candidate) is not supported: **both re-periodise; only one was long enough to be caught.**

## 4. Why this was NOT fixed in-session, and what would have to change

A mechanical repair of section 2 alone is trivial (run the reach check at `min_repeats = 2`, which
the table shows recovers period 8 at 19 steps). **It was deliberately not applied, because it
would have made the run worse, not better**: with a working reach check and no k that breaks the
orbit, every candidate arm becomes ineligible and the run self-routes `non_contributory` on both
claims at a cost of several hours of fleet time -- a guaranteed-null run.

Repairing section 1 is not a threshold change. It requires **re-posing C1 itself** -- from "no
period-2 alternation" to something like "no bounded orbit at any period, detected with a window
that fits the episodes this phenotype produces". That is a change to the **primary, user-ratified
criterion**, and to the scientific content of the discriminator rather than to its instrumentation.
Per `CLAUDE.md` Session Land Protocol, an autopsy's routing is a *proposal* until `/governance`
Step 2b ratifies it, and a queue-fill session that silently redefined the load-bearing criterion
would be racing ahead of the confirmation the six ratified changes already went through. So the
work stops here and goes back to governance with the measurement in hand.

## 5. What a successor needs (for the session that picks this up)

1. **Re-pose C1 on a period-agnostic orbit criterion.** The natural form: the latched arm shows no
   bounded orbit at ANY period in `2..max_period`, with `min_repeats` chosen so the window fits the
   episode lengths the phenotype produces (2 is sufficient at p=8 for a 19-step episode; 3 is not).
   Note this makes C1 *harder*, which is correct -- the current C1 is unfailable.
2. **Settle whether ANY k can break the orbit, or whether the latch family is the wrong
   manipulation.** The table in section 1 suggests re-periodisation is generic to a fixed-k latch
   on a two-cycle. If so, the discriminator MECH-536's notes name ("an eval-time action-persistence
   wrapper ... scored on cycle incidence AND resources/episode") cannot be realised with a fixed-k
   latch, and the question needs a different persistence operator -- e.g. one whose hold duration is
   state- or margin-dependent (`switch_cost`, already an arm here, is the obvious candidate and is
   NOT subject to the period-2k identity because its hold length is not fixed).
3. **Keep the other five changes.** CHANGES (1), (2), (4), (5) and (6) are implemented, smoke-green
   and independently sound in the authored driver; nothing in this record touches them. The
   re-posed exposure DV in particular ((2)) is verified by self-test to refuse the exact
   straight-run-then-press shape that fooled the predecessor.
4. **The authored driver is retained, not discarded**, at
   `ree-v3/experiments/_scratch/v3_exq_1007a_mech536_eval_persistence_discriminator.py.blocked`
   so the successor starts from the implemented six changes rather than from V3-EXQ-1007.

## 6. Governance follow-on

Recommend a `governance_flag.py` entry so this reaches the next cycle rather than resting in this
file: the confirmed `failure_autopsy_V3-EXQ-1007_2026-09-08` carries a routing whose third clause
("k=4 broke the orbit in 1007") is contradicted by the target run's own manifest, and the
correction changes which successor is buildable. **No claim direction changes on this record** --
MECH-536 and MECH-535 are untouched, because the finding is that the predecessor measured less
than it appeared to, not that either claim is weakened.

---

**Bottom line:** the six ratified changes were implemented in full and are sound; the letter is
blocked by an inherited defect none of them addressed, and the fix requires re-ratifying the
primary criterion. One banked measurement (section 1's table, seconds of compute) replaced what
would have been a multi-hour guaranteed-null fleet run.
