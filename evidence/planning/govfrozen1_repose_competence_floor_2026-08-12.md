# `competence_floor` — GOV-FROZEN-1 fan-out recurrence re-pose (2026-08-12 routing)

- **Generated:** 2026-08-14T01:35Z
- **Chip:** `chip-20260812-govfrozen1-repose-competence-floor`
- **Routed by:** `/governance` 2026-08-12 (session `sd-016-h3-algorithm-3370cd`) from the
  `hypothesis_space_integrity.md` "Fan-out recurrence (ACTIONABLE)" overlay —
  `competence_floor`, 5 labelled GOV-FANOUT-1 portfolios, denominator 7 -> 20, 0 legs alive.
- **Question:** `competence_floor` in `hypothesis_space_registry.v1.json`
- **Claims:** MECH-457, INV-088. **This record promotes and demotes nothing, queues no
  experiment, and makes NO registry edit** (the frozen ledger has a single producer,
  `/failure-autopsy` Step 9b; governance and this chip are derive-only over it).

---

## 0. Stop-check outcome — the recurrence was already worked, and this record does not repeat it

The chip's stop-check (grep the audit overlay) **cannot detect prior remediation**: the overlay is
warn-only and mechanically counts portfolios, so it re-fires forever once N>=3 is reached, whether
or not the recurrence was addressed. It was addressed:

- **`competence_floor_recurrence_repose_2026-08-08.md`** (chip `chip-20260808-competence-floor-refpose`)
  is a full recurrence re-pose of this same qid: portfolio history, why it kept fanning out
  (three independent mechanisms), the re-pose, and a machine-discoverable closure written to the
  qid's new top-level `growth_restriction` field.
- That record's one routed follow-on — a calibrated re-run of the single alive leg — **was executed
  the same day**. `H-consummation-binding` resolved `eliminated` 2026-08-08T16:17:18Z on
  V3-EXQ-821b (BC install dose 300->1200, `USABLE_INSTALL_FLOOR` 10.0, foraging rate reported
  alongside the composite; instrument fix `ree-v3` `0550a2f`). **0 legs alive.**
- The 08-08 record's other recommended follow-on also landed: `/failure-autopsy` SKILL.md now
  reads a target qid's `growth_restriction` before Mode A/B registration and treats it as a STOP
  surfaced at the Step 8 gate (SKILL.md lines 390, 513-524).

So the campaign is closed and the growth side of the anti-recurrence fix is wired. **This record
therefore contributes only what is genuinely still missing**, and is deliberately short:

1. the **honest narrowing pair** the GOV-FROZEN-1 rule requires — never stated in any of the five
   prior `competence_floor` planning documents (§1);
2. the **20-leg table with portfolio attribution** (§2);
3. the **shared presupposition** across the 20 legs — the chip's question 2, which the 08-08 record
   did not ask (it diagnosed the recurrence as a *governance* mis-scoping, not as a scientific
   blind spot) (§3);
4. the **re-pose and work-graph classification** (§4) and the **portfolio-6 verdict** (§5);
5. a **new confirmed finding**: the audit overlay has no acknowledgement mechanism, so it
   re-spawned this chip four days after closure. This chip is the incident (§6).

---

## 1. The honest narrowing pair (required by GOV-FROZEN-1, never previously stated)

| measure | original frozen set | current, including fan-out |
|---|---|---|
| denominator | 7 (`initial_frozen_count_at_registration`) | 20 (`initial_frozen_count`) |
| **surviving (alive)** | **0** | **0** |
| **surviving / denominator** | **0 / 7 = 0.00** | **0 / 20 = 0.00** |
| eliminated | 5 | 14 |
| confirmed | 1 | 4 |
| split (mixed) | 1 | 2 |

**Both ratios are 0.00, so on the surviving-fraction reading the inflation caveat is moot here —
say that plainly rather than quoting the flattering framing.** The rule's concern (a padded
denominator making narrowing look better than it is) does not bite on a campaign that resolved
every leg it enumerated.

**Where the inflation IS visible is in the time axis, and it is stark.** The original 7-leg frozen
set was **fully resolved within two days of registration** — registered 2026-07-13, all seven
carrying a resolution recorded by 2026-07-15 (day-granular backfilled stamps), including a
*confirmed* answer (`H-optim`). The campaign then ran **13 more legs across 5 portfolios over 24
further days**, closing 2026-08-08.

That is the precise shape of "the denominator outruns the eliminations," and it is not the shape
the phrase usually suggests: nothing survived, everything resolved, and the question still did not
close. **Twenty rivals enumerated, twenty resolved, and the frozen set's own exhaustion on day 2
bought no closure at all.** If the answer were inside the space being enumerated, the original
seven — which included a confirmed leg — would plausibly have ended it.

---

## 2. The 20 legs

Portfolios are numbered by the audit's labelled-fan-out ordering. P0 = the original registration
set (not a fan-out event).

| # | leg | axis | portfolio | state | resolving run(s) |
|---|---|---|---|---|---|
| 1 | `H-rep` | representation | P0 (07-13) | eliminated | 747, 749, 748a |
| 2 | `H-explore` | exploration | P0 (07-13) | split | 748 |
| 3 | `H-optim` | algorithm | P0 (07-13) | **confirmed** | 751 |
| 4 | `H-credit` | credit-assignment | P0 (07-13) | eliminated | 752 |
| 5 | `H-return` | return-policy | P0 (07-13) | eliminated | 753 |
| 6 | `H-curric` | curriculum | P0 (07-13) | eliminated | 754 |
| 7 | `H-arbitr` | arbitration | P0 (07-13) | eliminated | 755 |
| 8 | `H1-drive-schedule` | drive | P1 `V3-EXQ-769` (07-17) | eliminated | 770 |
| 9 | `H2-reward-coupling` | environment | P1 `V3-EXQ-769` (07-17) | eliminated | 771 |
| 10 | `H3-credit-horizon` | measurement | P1 `V3-EXQ-769` (07-17) | eliminated | 772 |
| 11 | `H-bc-prior` | learning-signal | P2 `770-771-772` (07-18) | split | 780 |
| 12 | `H-approach-primitive` | intrinsic-architecture | P2 `770-771-772` (07-18) | eliminated | 781 |
| 13 | `H-retention-critic` | algorithm | P3 `mech457_retention_portfolio` (07-18) | **confirmed** | 788 |
| 14 | `H-retention-consolidation` | policy | P3 (07-18) | **confirmed** | 792, 792a |
| 15 | `H-retention-auxiliary-decay` | learning-signal | P3 (07-18) | eliminated | 789 |
| 16 | `H-consummation-binding` | intrinsic-architecture | P3 (07-18) | eliminated | **821b (08-08)** |
| 17 | `H-zworld-trained-instrument` | instrumentation | P4 `batch-793a-817-819` (07-26) | **confirmed** | 819a |
| 18 | `H-mech475-baseline-reversal` | algorithm | P5 `mech476-mech475-cluster` (07-29) | eliminated | 837 |
| 19 | `H-mech476-dose-response` | curriculum | P5 (07-29) | eliminated | 836, 836a |
| 20 | `H-mech476-novelty-tagging` | drive | P5 (07-29) | eliminated | 836c, 836d |

Growth: P1 +3, P2 +2, P3 +4, P4 +1, P5 +3 = **+13**, 7 -> 20. Matches
`initial_frozen_count_at_registration` -> `initial_frozen_count` exactly.

(The 2026-08-08 record's census reads 5 confirmed / 12 eliminated / 1 alive / 1 voided because it
counts `H-bc-prior`'s *children* separately and was written before 821b landed. The table above is
the mechanical registry-level state as of today; the two are consistent, at different grain.)

---

## 3. The shared presupposition

**Yes, there is one, and the campaign's own closing sentence names it.**

Read the axis column: representation, exploration, algorithm, credit-assignment, return-policy,
curriculum, arbitration, drive, environment, measurement, learning-signal, intrinsic-architecture,
policy, instrumentation. Nineteen of the twenty legs vary something *inside the learner* (what it
represents, how it credits, how it consolidates, how it explores, what drive it carries, how it is
measured). Exactly one — `H2-reward-coupling` — reaches outside the learner, and it does so by
swapping the environment wholesale for a metabolic forage-to-survive variant rather than by
manipulating the reward specification as a graded axis.

**The presupposition none of the twenty questioned: that the reward specification the agent is
actually paid to maximize is a fixed, correct given, and that any gap between it and
`foraging_competence` (resources/episode) is not the explanandum.**

Three independent pieces of the campaign's own record converge on this, none of which was treated
as a leg:

- **The registry states it outright, at the moment of closure.** `H-consummation-binding`'s
  resolution basis: *"the total ... erosion is attributable to the **fixed approach-drive reward
  coefficient (untested as an axis here, held identical across both arms)**, not to an unaddressed
  confound in this leg. ... Any follow-on question about approach-drive reward magnitude is OUT OF
  SCOPE for this qid."* The campaign's last act was to name an untested factor as the attributed
  cause and route it elsewhere. Legs turned the approach drive **on** (`H-approach-primitive`,
  `approach_coef=1.0`), changed its **extinction dynamics** (`H-consummation-binding`), and changed
  its **annealing schedule** (`H1-drive-schedule`) — but its **magnitude was held constant across
  all twenty legs**.
- **The instrument audit found the agent optimizing the specification, not failing at the task.**
  `competence_floor_instrument_audit_2026-08-07.md` §4 (via the 08-08 record §2c): V3-EXQ-781's
  "approach-without-consummation" reading — the finding that motivated the campaign's most
  invasive build — was **proximity-camping**, parking near a resource and passively collecting a
  shaping term. That is a Goodhart of the reward shaping. The discriminating metric
  (`planning_depth`, 0.42x of control) was **collected and never read**.
- **The DV conflates rate with duration, and they are anti-correlated at the floor.** Audit §2:
  `foraging_competence` = resources/**episode** multiplies foraging rate by episode length, and in
  this environment the most survivable policy is the least competent one. So the DV can hide a
  real rate effect or manufacture an apparent one — and it is the DV every one of the twenty legs
  was adjudicated on.

One corroborating anomaly worth naming without over-reading it: `H2` and `H1` were eliminated on a
**single shared floor reading** ("treatment arm forages at the floor ~0-1, indistinguishable from
`random_walk`, on BOTH z_world and raw"). A floor reading in an environment where *survival
requires foraging* is itself anomalous — it was adjudicated as an axis elimination rather than
investigated as an instrument signal. That is the one place the campaign brushed the
specification, and it read the result as being about the mechanism.

---

## 4. The re-pose, and the work-graph classification

**The re-posed question:**

> Is the retention deficit a property of the agent at all, or is it a **specification gap** — a
> mismatch between the objective the agent is paid to maximize (shaped approach reward + survival)
> and the dependent variable competence is scored on (`foraging_competence` = resources/episode,
> which multiplies rate by duration)? Concretely: under a reward specification whose optimum is
> the DV's optimum, and on an instrument that reports rate and duration separately, does a
> retention deficit exist to explain?

**Classification: `mystery (known data)`, not `puzzle (known rules)`.** Per
`docs/architecture/work_graph_debt_vocabulary.md`, a mystery needs reframing rather than gathering,
and that is the diagnosis here on positive evidence, not by elimination:

- The **data that would answer it is already collected.** `planning_depth` was recorded on the run
  whose misreading seeded the campaign's most expensive leg, and never consumed. Rate and duration
  are both already inside the composite DV. Nothing new needs to be gathered to see the
  specification gap — the existing runs contain it.
- Five rounds of enumeration inside one framing produced 20 resolved legs and no closure. That is
  the signature of asking a well-formed question of a mis-specified space, not of missing one more
  fact.
- **It is emphatically not `complex (probe-gated)`.** A probe would license portfolio 6. There is
  no rival mechanism left to discriminate between: every axis family this qid tracks (process,
  constitution, instrumentation, representation, world) carries a resolved answer.

**The residual is `complicated (buildable)`, and it is already scoped and out of this qid's
scope**: the approach-drive reward-magnitude axis the registry itself routes to *its own qid*.
That is a new question with its own frozen set, not a sixth portfolio on this one.

---

## 5. Verdict on portfolio 6: **REFUSE**

Refused on four independent grounds, any one sufficient:

1. **The qid is formally closed to further fan-out.** `competence_floor.growth_restriction`
   (2026-08-08) states it and names its own exception condition: a claim in the
   MECH-457/459/460/475/476 lineage registers its **own** qid unless its target axis family is one
   this qid's `decision` block still lists as undecided — *"there is currently none."* The
   exception is unavailable by inspection.
2. **There is nothing left to discriminate.** 0 of 20 legs alive; every axis family resolved. A
   fan-out portfolio pre-registers rivals; there are no rivals.
3. **The re-pose (§4) is a reframe, not an enumeration.** Answering it requires reading data
   already collected under a corrected instrument — not a new rival set. Opening a portfolio would
   be the denominator-side twin of re-running a braked experiment harder, which is exactly what
   the recurrence rule exists to stop.
4. **The one live thread is out of scope by the campaign's own closing act** — approach-drive
   reward magnitude, explicitly routed to a separate qid by `H-consummation-binding`'s resolution.

**If a new leg in this lineage is proposed**, the correct disposition is a **new qid**, pre-registered
by `/failure-autopsy` Step 9b (the single producer), whose frozen set should include the
specification-gap axis §3 identifies as never having been a leg. **This record does not register
it** — that is Step 9b's job and this session is derive-only over the ledger.

---

## 6. New finding: the recurrence overlay has no closure mechanism, and it re-spawned this chip

**Confirmed, with this chip as the incident.** `check_hypothesis_space_integrity.py` fires the
fan-out recurrence overlay on `len(fanout_sources) >= FANOUT_RECURRENCE_N`. The count never
decreases (GOV-FROZEN-1 has no shrinkage operation, correctly), and **the script does not read
`growth_restriction`** — verified: zero occurrences of that identifier in the file. So a qid that
has been fully re-posed, formally closed to fan-out, and had every leg resolved goes on emitting an
ACTIONABLE line indistinguishable from a live one.

`/failure-autopsy` SKILL.md line 524 already states the asymmetry from the other side: *"a
restricted question grown by an otherwise well-formed labelled fan-out clears the audit cleanly.
This step is the only place the field is read."* The converse is the gap here — a **closed**
question never clears the *recurrence* overlay.

Cost, measured: `/governance` read that line on 2026-08-12 and routed a re-pose chip for a
campaign that had closed on 2026-08-08 — **four days after the fact, and after the routed
follow-on had itself been executed.** This is a duplicate-work generator that fires once per
governance cycle per closed hero campaign, and it is precisely the alarm-fatigue Goodhart vector
GOV-FROZEN-1's own design notes warn about (governance SKILL.md line 1130).

**Routing (flagged, not built — scope discipline; and it is not this chip's task):** teach the
overlay to *acknowledge* rather than suppress. Suggested shape, deliberately conservative: when a
qid carries a non-empty `growth_restriction` **and** has 0 alive legs, keep emitting the line but
move it to an **advisory/acknowledged** bucket citing the restriction, so it stays visible and
auditable without routing work. Do **not** make it clear silently — the overlay's warn-only,
never-gating design is correct, and a rule that could erase its own alarm is worse than a noisy
one. This needs a session that owns `check_hypothesis_space_integrity.py`; note that any such
change touches the audit, not the ledger, so it adds no second registry producer.

---

## Provenance

- Derived from: `hypothesis_space_registry.v1.json` (`competence_floor`, all 20 hypotheses and the
  `growth_restriction` / `fanout_growth_note` / `title_repose_note` fields),
  `hypothesis_space_integrity.md` (fan-out recurrence overlay),
  `check_hypothesis_space_integrity.py`, `.claude/skills/failure-autopsy/SKILL.md` (Step 9b
  growth-restriction check), `.claude/skills/governance/SKILL.md` (Step 5c / GOV-FROZEN-1).
- Builds on and does not repeat: `competence_floor_recurrence_repose_2026-08-08.md`,
  `competence_floor_instrument_audit_2026-08-07.md`, `competence_floor_reposing_2026-07-19.md`
  (+ `-07-20`, `-07-25`), `mech457_retention_portfolio_2026-07-18.md`.
- **No registry edit. No `claims.yaml` write. No experiment queued or run. No substrate change.**
  The §4 re-pose and the §5 new-qid recommendation are routed to `/failure-autopsy` Step 9b; §6 is
  routed to a session owning the integrity audit.
- Chip: `chip-20260812-govfrozen1-repose-competence-floor`.
