# `competence_floor` — recurrence re-pose (GOV-FROZEN-1, chip-20260808-competence-floor-refpose)

- **Generated:** 2026-08-08T08:51:01Z
- **Trigger:** `hypothesis_space_integrity.md` "Fan-out recurrence (ACTIONABLE)" — 5 labelled fan-out
  portfolios on `competence_floor`, denominator 7 -> 20, 1 leg alive. Spawned as a standalone
  chip from the 2026-08-08 `/governance` cycle (worktree `heuristic-mccarthy-7498cc`), by
  explicit user instruction to work this outside the live governance walk.
- **Question:** `competence_floor` in `hypothesis_space_registry.v1.json`
- **Claims:** MECH-457 (candidate / v3_pending), INV-088 (candidate / pending_substrate_reconfirmation)
  — **this record promotes and demotes nothing.** It closes a discrimination campaign and routes
  its one residual thread; no `claims.yaml` state changes.
- **Predecessor documents (read in full, not duplicated here):**
  `competence_floor_reposing_2026-07-19.md` (the first re-pose: title, bifurcation, D1-D6),
  `mech457_retention_portfolio_2026-07-18.md` (portfolio 3, and the standing rule this record
  finally acts on — see section 2), `competence_floor_instrument_audit_2026-08-07.md` (the
  measurement-instrument forensics this record builds on directly — see section 3).

---

## 0. Headline

**The campaign is not mis-posed by its hypotheses; it is mis-scoped by its qid boundary, and
that boundary was never closed even after its own standing rule said it should be.** All four
original discrimination axes (capacity, drive-schedule, reward-coupling, credit-horizon) were
eliminated by portfolios 1-2. Retention was DECIDED 2026-07-25 (value estimator + update
constraint, PROCESS family). The two claims that were later split off this campaign by
`/claim-synthesis` — MECH-475 (baseline informativeness) and MECH-476 (consolidation
dose/interval/novelty) — have **both since been fully retired** (2026-07-29 and 2026-08-01
respectively), each on its own pre-registered falsifier. `H-bc-prior` child 3 (the apparent
z_world non-install) was **voided as an instrument artifact** 2026-08-07. What is left alive in
the 20-hypothesis ledger is **exactly one leg**: `H-consummation-binding` — and the 2026-08-07
instrument audit already showed its `eliminated` reading was itself an artifact (two arms tied
at the absolute floor, install at 14% of ceiling, not a discrimination).

So as of this morning, `competence_floor`'s **discrimination job is finished**. Every rival
mechanism the campaign was built to discriminate among has a resolved answer. What recurred was
not the science; it was the **qid's willingness to keep absorbing new claim-synthesis children
as growth events** rather than being closed once its own decision was reached. This record
closes that gap: it retires `competence_floor` as an open hero campaign eligible for further
GOV-FANOUT-1 portfolios, routes its one live thread as a build-and-rerun (not a discrimination),
and — because the same absorption mechanism will recur on the next split claim in this lineage
(MECH-459, MECH-460 both still carry `depends_on: [MECH-457, ...]`) — adds a machine-discoverable
restriction to the qid itself, not another planning document nobody re-reads at the moment it
matters.

---

## 1. Full portfolio history, and what each one actually decided

| # | Portfolio (source) | Date | Axes opened | Axes' fate | Event class (mechanical) |
|---|---|---|---|---|---|
| 1 | `failure_autopsy_V3-EXQ-769` | 07-17 | H1 drive-schedule, H2 reward-coupling, H3 credit-horizon | all 3 eliminated (770/771/772) | `partial_re_entry` |
| 2 | `failure_autopsy_MECH-457-fanout-770-771-772` | 07-18 | H-bc-prior, H-approach-primitive | bc-prior SPLIT (acquisition confirmed); approach-primitive eliminated | `refining` (fresh `constitution` territory) |
| 3 | `mech457_retention_portfolio_2026-07-18` | 07-18 | H-retention-critic, -consolidation, -auxiliary-decay, H-consummation-binding | critic + consolidation CONFIRMED (2026-07-25); auxiliary-decay eliminated; consummation-binding eliminated -> **reopened `alive` 2026-08-07** | `circling` (re-entered `process`/`constitution`, defended in the portfolio's own §3 as principled — different explanandum, same locus) |
| 4 | `failure_autopsy_batch-793a-817-819` | 07-26 | H-zworld-trained-instrument | CONFIRMED (weak positive, 819a) | `circling` (re-entered `instrumentation`; the portfolio's own text asserts "instrument-validity, not circling" but records no axis-family exception) |
| 5 | `failure_autopsy_mech476-mech475-cluster` | 07-29 | H-mech475-baseline-reversal, H-mech476-dose-response, H-mech476-novelty-tagging | **all 3 eliminated**; MECH-475 WITHDRAWN 07-29; MECH-476 WITHDRAWN 08-01 (after redesigned 836a/836d/836e) | `circling` (all 3 re-entered `process`, no axis-family exception argued anywhere in the source) |

Mechanically-derived `convergence.convergence_class` for the qid is `circling`, and the growth-event
log (`hypothesis_space.v1.json`) shows **3 of the last 3 growth events** (#3, #4, #5) scored
`circling` at the axis-family level — portfolio 3 argued (and this record does not relitigate)
that its circling reading is a locus-taxonomy limitation, not genuine non-convergence; portfolio 4
asserted an exception without adding one; portfolio 5 argued nothing at all. **All three,
independent of that dispute, ended in DECISIVE closure** (retention decided; MECH-475/476
withdrawn) — so whatever the axis-family verdict on any one of them, none left an open question
behind. The recurrence flag counted five open-looking portfolios; ground truth today is zero.

---

## 2. Why it kept fanning out — three distinct mechanisms, not one

**(a) `/claim-synthesis` children were absorbed into the parent qid by theme, not audited
against the qid's own decision state.** `/failure-autopsy` Step 9b's rule for a fan-out is
explicit: *"New question (the fan-out opens a scientific question not already a qid — match by
`claims` + theme against existing questions)."* MECH-475 and MECH-476 were registered 2026-07-22
as **formally distinct claims** with their own `claim_id`, their own `what_would_answer`
falsifier spec, and `split_from: MECH-457` — but their `claims` set is not a strict superset of
`competence_floor`'s registered `claims: [MECH-457, INV-088]`, and Step 9b's matching rule has no
clause for "the candidate claim is a `/claim-synthesis` child of an already-decided sibling
question." Theme-matching (same substrate lineage, same narrative of "competence") did the rest:
both children's first autopsy (2026-07-29) folded their legs into `competence_floor` under Mode B
rather than asking whether either child's own falsifier spec warranted its own qid. It happened
to be harmless here because both claims converged fast and decisively on their own terms — but
that is luck in the design, not a property of it.

**(b) The campaign's own standing anti-recurrence rule was written as prose in a planning
document, never as something a future session would mechanically re-check.**
`competence_floor_reposing_2026-07-19.md` §7 states explicitly: *"If the four retention legs
resolve and a fifth portfolio is proposed on the retention operationalization, treat the
recurrence flag as BLOCKING — that is the pattern it exists to catch."* The four retention legs
resolved 2026-07-25. Portfolio 5 (mech476-mech475-cluster, 07-29) opened three legs squarely in
the `process` family the retention decision had just closed — MECH-475's own registration text
names "the leading candidate ROOT of the erosion this claim characterises" as the *same*
uninformative-baseline mechanism `H-retention-critic` had just confirmed a fix for. This is
precisely the condition the 07-19 rule named. Nothing in the mech476-mech475-cluster autopsy, nor
in `/failure-autopsy` Step 9b, nor in the integrity audit, references that standing rule or
checks it. A rule that lives only in one planning document's prose is not discoverable at the
moment a different session, three weeks later and working a different claim, is about to trip it.
This record's §5 fixes that concretely.

**(c) The measurement instrument itself manufactured ambiguous signal that fed the enumeration
— demonstrated, not inferred.** `competence_floor_instrument_audit_2026-08-07.md` §4 traces one
concrete case end to end: `H-approach-primitive`'s eliminating run (V3-EXQ-781) recorded a
"load-bearing positive finding" — approach reward earned continuously while foraging was
suppressed, read as "the appetitive drive becoming terminal rather than instrumental." That
reading is what motivated `H-consummation-binding`, which cost a dedicated build
(`mech457_consummatory_act`, invasive — changes `action_space_size`) and an experiment
(V3-EXQ-821). The audit shows the run's *own* `planning_depth` metric — collected, never read —
falls to 0.42x of control under the same manipulation: the treated agent's directed approach
*collapsed*, it did not persist. The actual behaviour was proximity-camping (parking near a
resource and passively collecting a shaping term), a Goodhart of the reward shaping, not an
approach-without-consummation phenomenon at all. **A fan-out leg — and the campaign's most
invasive, most expensive build — was seeded by an instrument that discarded the one metric that
would have discriminated the correct reading from the wrong one at zero additional cost.** The
composite DV (`foraging_competence` = resources/episode) compounds this: §2 of the audit shows it
conflates foraging *rate* with episode *duration*, which are anti-correlated at the floor in this
environment (the most survivable policy is the least competent one), so a flat composite can hide
a real rate effect or manufacture an apparent one.

These three mechanisms are independent and each sufficient on its own; together they explain why
five individually-legitimate portfolios (each cleared GOV-FROZEN-1's per-portfolio conditions
(a)-(c)) still produced a campaign that read as non-convergent until this week.

---

## 3. Ground truth as of 2026-08-08 — the discrimination job is done

Leg census (20 hypotheses; per current registry, post the 2026-08-07 governance-applied edits):

| state | count | legs |
|---|---|---|
| confirmed | 5 | H-optim, H-retention-critic, H-retention-consolidation, H-zworld-trained-instrument, H-bc-prior child 1 (acquisition) |
| eliminated | 12 | H-rep, H-credit, H-return, H-curric, H-arbitr, H1-drive-schedule, H2-reward-coupling, H3-credit-horizon, H-approach-primitive, H-retention-auxiliary-decay, H-mech475-baseline-reversal, H-mech476-dose-response, H-mech476-novelty-tagging |
| split (mixed) | 1 | H-explore |
| **alive** | **1** | **H-consummation-binding** (reopened 2026-08-07 — observation-bottleneck, not a live rival) |
| voided (instrument artifact) | 1 | H-bc-prior child 3 |

The one alive leg is not a discrimination candidate among rivals — it is a single named
substrate-and-remeasurement gap. `mech457_consummatory_act` is **already built** (`ree-v3`
`upbeat-hugle-0dd183`, 2026-07-25); the one run against it (V3-EXQ-821) was underpowered by
construction (both arms installed at 14% of ceiling vs 44% elsewhere in the campaign, so neither
arm ever cleared a usable floor to erode from). This is `complicated (buildable)` work — build a
stronger install + the corrected instrument, then re-run once — not `complex (probe-gated)`
work needing a fan-out portfolio.

Both claims that were split off this campaign are closed on their own falsifiers, independent of
anything in this record:

- **MECH-475** — `status: retired` (`live_status.as_of: 2026-07-29`). V3-EXQ-837 substituted the
  confirmed distributional critic on 2/3 named destructive instances; the destructive
  competence-below-control inversion got 3.4x *worse*, not better, on all 6 scorable seeds.
  WITHDRAWN per the claim's own pre-registered criterion.
- **MECH-476** — `status: retired` (`live_status.as_of: 2026-08-01`). All three redesigned
  falsifier arms (dose/836a, novelty/836d, interval/836e — noise-scaled margins, n>=10 seeds)
  independently confirmed retention invariant to the manipulated variable, 2 of 3 leave-one-out
  robust at 10/10 seeds. WITHDRAWN per the claim's own pre-registered criterion.

Neither withdrawal narrows MECH-457 or INV-088: both children's registration text is explicit
that a WEAKENED/invariant outcome folds back into the already-confirmed value-estimator +
update-constraint retention mechanism (MECH-459/460), which stands untouched.

---

## 4. The re-pose

**`competence_floor` is retired as an open hero discrimination campaign.** It is not deleted —
GOV-FROZEN-1 has no shrinkage operation and this record does not invoke one; the qid, its 20
hypotheses, and their resolutions stay exactly as they are. What changes is the qid's *forward*
disposition: it is no longer a live target for a sixth GOV-FANOUT-1 portfolio, because there is
no remaining discrimination — every rival mechanism this campaign was built to adjudicate among
has a resolved answer, and the two claims it spawned are independently closed.

**The re-posed question is not a rewrite of the retention question (already answered) — it is a
sharper, single, decisive re-test of the one open thread, stated so it cannot spawn another
rival:**

> Once retention is measured on an instrument that (a) reports foraging **rate** (resources/tick)
> alongside the composite resources/episode count, so episode-duration effects are not silently
> multiplied in, and (b) is preceded by a BC install strong enough to clear a usable floor (the
> campaign's own installs range 20.9-38.3 forage/episode; V3-EXQ-821's install was 4.77, ~14% of
> its own ceiling) — does gating the approach drive to extinguish on contact and hand off to a
> distinct consummatory act change the retention outcome, or does retention remain fully
> explained by the already-confirmed value-estimator and update-constraint mechanisms?

This is decidable in **one** re-run, not a portfolio: there are no rival hypotheses left to
discriminate among on this leg — only a measurement floor to clear before the existing
alive/eliminated call can be trusted either way.

**Routing:** `complicated (buildable) -> /queue-experiment`, not `/failure-autopsy` fan-out.
Two preconditions, both already scoped by the 2026-08-07 audit and neither requiring new
science:

1. Land the one-line probe-function fix (`make_probe_fn` / `install_bc_prior` in
   `experiments/_lib/baselines/mech457_retention.py` return the full `evaluate_seed` row, not
   the single `foraging_competence` projection) — additive, every existing caller's verdict is
   byte-identical.
2. Re-run `V3-EXQ-821`'s successor at a BC install dose calibrated to land the install in the
   20-40 forage/episode range this campaign's other legs used, under the fixed instrument, with
   `foraging_competence` (composite), rate/tick, and `survival_horizon` all reported as separate
   DVs per the audit's §7 recommendation.

This record does **not** open that substrate-queue entry or requeue the experiment — flagging
per CLAUDE.md scope discipline; that action item belongs to whichever session next queues
`/implement-substrate` or `/queue-experiment` work on this lineage. It is named here so it is not
lost, and — per the anti-recurrence fix below — so it is the *only* thing that qid may still
generate.

---

## 5. Anti-recurrence fix — machine-discoverable, not a fourth planning document

The 2026-07-19 repose's standing rule (§2b above) was correct and was not followed, because it
lived only in prose in a file nobody re-reads at the moment a new claim's first autopsy is about
to grow an existing qid. This record puts the restriction on the qid itself, in the registry's
own free-text fields (`fanout_growth_note`, already used for exactly this kind of narrative
caveat; `decision.observation_bottleneck`, already used on this same qid for a standing
per-leg measurement requirement) — a location every future `/failure-autopsy` Step 9b invocation
and `/governance` walk already reads, rather than a fifth document added to the pile.

**Concrete registry edits made by this session** (both fields already exist on this qid; no new
top-level schema key besides one — see below):

- `fanout_growth_note` — replaced with a summary of this closure and an explicit, checkable
  restriction: *no further GOV-FANOUT-1 discrimination portfolio on this qid; a claim in this
  lineage whose `depends_on` includes MECH-457/459/460/475/476 registers its own qid by default
  unless its target axis family is one this qid's `decision` block still lists as undecided
  (there is currently none).*
- `decision.observation_bottleneck` — appended the 2026-08-07 finding (H-consummation-binding's
  `eliminated` reading was an artifact of a 14%-of-ceiling install, not a discrimination) and the
  §4 re-posed decisive re-test.
- `decision.distance_phrase` — appended a closing clause recording that MECH-475/476 are both
  retired and the campaign's discrimination phase is complete.
- **New top-level field `growth_restriction`** (string) — this qid has no existing field for a
  standing structural restriction distinct from a per-leg measurement requirement
  (`decision.observation_bottleneck` is per-leg/per-decision; this is per-qid and forward-looking).
  Precedent for a bespoke per-question top-level field is already established elsewhere in the
  registry (`curiosity_subflavour_authority.provenance_note`,
  `mech204-sd076-calibration-loop-drift-source-exposure-gap.registration_note`,
  `arc071-commit-latch-postfix-persistence.observation_bottleneck` at top level rather than
  nested) — this follows that pattern rather than inventing a new mechanism. It carries no
  invariant of its own and is not read by `check_hypothesis_space_integrity.py` today; it is
  documentation, the same status the audit's own proposed riders have until a session wires a
  check to it. **Recommended follow-on** (flagged, not started, per scope discipline): teach
  `/failure-autopsy` Step 9b to read a target qid's `growth_restriction` before Mode A/B
  registration and refuse growth silently — surface the restriction to the user at the Step 8
  gate instead.

**What this record deliberately does NOT do:**

- No hypothesis `state`/`resolution` changes — all 20 legs' resolutions are exactly as the
  2026-08-07 governance-applied edits left them.
- No `initial_frozen_count` change — this is not fan-out or discovery growth; nothing is added
  to `hypotheses[]`.
- No `claims.yaml` writes — MECH-457/INV-088 status is unaffected by this record; MECH-475/476
  are already `retired` via their own governance cycles, cited not altered.
- No `is_hero` flip — there is no established meaning for un-hero-ing a campaign in this schema,
  and the qid's history is exactly why it is a hero; closure is expressed via `growth_restriction`
  instead, which is additive and legible without redefining an existing flag's semantics.

---

## 6. Answer to the chip's question

**Is the observable underspecified? Yes** — `foraging_competence` conflates rate and duration,
verified quantitatively for both confirmed retention mechanisms (§3a/3b of the 2026-08-07 audit).
**Does the campaign conflate two mechanisms? No longer** — the one candidate conflation
(retention vs installability) was already split by the 2026-07-19 repose (D5, H-bc-prior), and
installability's own remaining thread was voided as an instrument artifact 2026-08-07, so there
is nothing left to bifurcate into a second live qid. **Is the elimination bar too strict or too
loose? Neither** — every elimination in the 12-eliminated set stands on re-audit (2026-08-07 §5c,
"0 of 20 legs need re-opening on z_world grounds"); the one leg that needed a bar correction
(`H-consummation-binding`) already got one. **What was actually missing** was a qid-level
closure mechanism: nothing in this pipeline ever asks "has this hero campaign's decision been
reached, and should it still accept new growth" — Step 9b only asks "does a new leg belong to an
existing qid by theme," never "should this qid still be open." That is the gap this record
closes, and it is a governance-process finding as much as a scientific one.

---

## Provenance

- Data re-derived from: `hypothesis_space_registry.v1.json` (`competence_floor` entry, all 20
  hypotheses), `hypothesis_space.v1.json` (`convergence` block), `hypothesis_space_integrity.md`
  (2026-08-08 fan-out recurrence section), `docs/claims/claims.yaml` (MECH-475/476 `retired`
  entries), `substrate_queue.json` (`mech457_consummatory_act`).
- Builds directly on, and does not repeat: `competence_floor_reposing_2026-07-19.md`,
  `mech457_retention_portfolio_2026-07-18.md`, `competence_floor_instrument_audit_2026-08-07.md`.
- No experiment run, queued, or requeued. No substrate change. No compute.
- Registry writes by this session: `fanout_growth_note`, `decision.observation_bottleneck`,
  `decision.distance_phrase`, new top-level `growth_restriction` — all on the `competence_floor`
  question only. No hypothesis-level state changes.
- Chip: `chip-20260808-competence-floor-refpose`.
