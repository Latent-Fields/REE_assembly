# The unrunnable-falsifier population: 121 claims whose falsifier cannot be run and that nothing is building for

**Date:** 2026-08-28 · **Session:** `elated-nobel-914234` (continuation of `insights-7fd98a`)
**Status:** FINDING -- registry measurement. Nothing registered, no claim status changed, no substrate change.
**Prompted by** the user, 2026-08-26: *"There should be a way of falsifying even if it means building new substrate designing around it. If it's [unfalsifiable] then it must be some sort of vacuous claim, ridiculousness itself surely."*
**Related:** GFLAG-0054 already names the mechanical half ("nothing routes a written falsifier to anyone"). This puts a number on it and identifies a shared cause.

---

## 1. The user's point, and why it is a measurement question

The position is normative and sharp: an unfalsifiable claim is a vacuous claim,
so the honest response to "this cannot be tested yet" is to build the substrate
that makes it testable -- not to file it under a status that makes the
untestability permanent and tidy.

REE has a category for exactly this: a claim may declare a NON-DEGENERACY
PRECONDITION that is currently unmet, with `epistemic_category:
substrate_conditional` and a `substrate_not_ready` self-route for any run that
tries anyway. The design intent is a **queue** -- build it, then test. The
question the user's remark raises is whether it functions as a queue or as a
**parking lot**.

## 2. Measurement

Registry as of 2026-08-28: **1064 claims**, of which **507 carry a written
`what_would_answer`**.

| | count |
|---|---|
| claims with a written falsifier | 507 |
| ...that self-declare an unmet precondition / `substrate_not_ready` route | **185** |
| ...of those, routed by `substrate_queue.unblocks_claims` | 47 (25%) |
| ...routed by EITHER `substrate_queue` OR named anywhere in the IGW ledger/assignments | 64 (35%) |
| **...with NO route on either channel** | **121 (65%)** |

The second channel is counted **generously** -- any appearance of the claim id
anywhere in `igw_routine_ledger.json` or `igw_assignments.json` counts as routed,
which over-counts rather than under-counts.

Unrouted, by phase: **v3 43**, v4 38, unset 34, v5 4, post_v5 1, v6 1.
Unrouted, by status: candidate 102, provisional 7, **active 6**, open 3,
retired 2, implemented 1.

The six **active** claims with an unmet falsifier precondition and no build
route: `ARC-003` ("E3 selects and commits trajectories"), `Q-007`, `Q-015`,
`INV-025`, `INV-028`, `INV-029`.

Age since registration, where recorded (n=88): median **69 days**, p90 129,
max 152. Buckets: <30d 26, 30-90d 36, **>90d 26**.

**The 43 v3-phase unrouted claims** -- the subset REE itself assigns to the
current substrate generation, so the ones where "build it so it can be tested"
most clearly applies:

MECH-071, MECH-092, MECH-121, MECH-124, ARC-038, MECH-165, MECH-186, INV-062,
MECH-209, MECH-210, MECH-212, ARC-059, MECH-278, SD-048, SD-050, Q-043, ARC-079,
Q-067, SD-069, MECH-395, MECH-426, ARC-109, ARC-111, MECH-452, MECH-454,
MECH-463, MECH-475, MECH-476, MECH-478, Q-086, Q-089, MECH-480, MECH-482,
MECH-483, SD-093, Q-090, Q-092, INV-101, SD-097, SD-098, MECH-488, Q-093,
MECH-496.

## 3. The honest counterweight -- not every unrouted claim is a scandal

Two qualifications, both of which cut the headline number down and neither of
which removes the finding.

**(a) Some of these are legitimately `aleatoric (irreducible)`.** The work-graph
debt vocabulary already distinguishes a claim that needs a build from one that
needs a hedge. `INV-025` ("irreducible uncertainty is an epistemological
constraint that cannot be engineered away") does not owe a substrate build, and
`INV-028` / `INV-029` are dispositional/ethical commitments. A claim of that
type having no queue entry is correct, not neglect. **No audit currently
separates these**, which is itself the actionable gap: there is no field saying
"this claim's untestability is irreducible" versus "this claim's untestability is
a build away".

**(b) Many DO name their blocker -- in prose.** Spot-checking the v3 unrouted
set, `MECH-092`, `MECH-121`, `MECH-165` and `ARC-038` each state a specific
upstream blocker (SD-006 phase-2 async execution, a consumer for consolidated
value, a diverse-repertoire precondition) inside their own
`what_would_answer` or `notes`. So the intent is recorded. It is simply
recorded **where no work-routing process reads it**.

## 4. The shared cause, which this session hit four separate times

The measurement above is one instance of a single structural pattern:

> **REE's claims carry load-bearing structural assertions in PROSE fields --
> preconditions, dependencies, blockers -- that no machine-readable field
> mirrors. Nothing routes them, checks them, or walks them.**

Four independent instances, all found in one session:

1. **ARC-004's non-degeneracy precondition** asserts "z_delta reads only
   z_theta's history". That is a checkable factual claim about source; nothing
   checked it; it has been false since ree-v3's initial commit, which made the
   claim vacuously false and its falsifier a foregone conclusion. (GFLAG-0088)
2. **MECH-522's dependency on ARC-004** is stated in its argument text and
   absent from `depends_on`, so the propagation is invisible to any dependency
   walk. (GFLAG-0090)
3. **MECH-520's cross-horizon requirement** is stated in its title with no gate
   field, so nothing connects it to ARC-004's measured status. (GFLAG-0090)
4. **121 claims** whose unmet precondition -- and often the specific blocker --
   is stated in prose with no entry in any routing channel.

The user's normative point and the mechanical finding meet exactly here. "There
should be a way of falsifying even if it means building new substrate" **is**
REE's policy: the claims say, in detail, what they need. The policy is not
executable because what they need is written in a paragraph.

## 5. What would follow, if governance wants it

Deliberately not built here, and offered rather than proposed:

- **A machine-readable `blocked_on` (or `precondition_refs`) field** on claims
  that declare an unmet precondition, naming the claim ids / substrate items /
  source facts the precondition depends on. That single field would make the
  121 walkable, would have made instances 1-3 above detectable by a lint rather
  than by a session that happened to read the prose, and is the smallest change
  that turns the stated policy into an executable one.
- **An `irreducible: true` marker** (or reuse of the debt vocabulary's
  `aleatoric (irreducible)`) so that qualification (a) is recorded rather than
  re-litigated by every audit.
- **A precondition lint.** ARC-004's precondition was a checkable statement about
  source. Where a precondition makes such a statement, checking it is cheaper
  than running the falsifier and would have caught the largest finding of this
  session before the falsifier was ever written.

## 6. Limits

- **Detection is keyword-based** on `what_would_answer` + `notes`
  (`currently unmet`, `all unmet`, `substrate_not_ready`,
  `substrate_conditional`, `not currently met/testable`). Six spot-checks were
  all genuine, but the recall of this detector is unmeasured -- claims that
  express the same state in other words are missed, so 185 is a **lower bound**
  on the population.
- **Routing detection is by claim-id mention**, generous on the IGW side and
  therefore over-counting "routed". A claim could also be routed through a chip
  or a planning doc this does not read, so 121 is an **upper bound** on the
  unrouted count.
- The two bounds run in the same direction as each other only by coincidence;
  the honest reading is "on the order of 100+, certainly dozens", not "121
  exactly".
- No claim status is changed and nothing is queued here.

---

## 7. Addendum (same session, user-prompted): matching prerequisites to claims, and the orphans

The user's extension: *"prerequisites could be matched to existing claims and where
there are orphan prerequisites this may need further investigation as it could be
enlightening."*

Matching each of the 185 claims' precondition blocks against the registry -- does the
precondition name any registered claim id?

| | count |
|---|---|
| precondition names >= 1 registered claim (matched) | **155** |
| precondition names **no** registered claim (orphan prerequisite) | **30** |

The 30, phase in brackets: ARC-007(-), Q-007(-), ARC-018(-), MECH-035(-), MECH-037(-),
MECH-048(-), INV-090(-), MECH-342(v3), Q-062(v4), Q-065(v4), Q-066(post_v5), Q-069(-),
Q-072(v4), Q-073(v5), MECH-424(v6), MECH-425(v4), MECH-426(v3), MECH-427(v3),
ARC-105(v4), MECH-453(v4), Q-083(v4), Q-086(v3), Q-089(v3), MECH-481(v3), MECH-489(v3),
MECH-490(v3), Q-092(v3), SD-097(v3), Q-093(v3), MECH-521(v4).

**The set is not homogeneous, and separating the kinds is the finding.** Three
spot-checks show at least two kinds:

- **Kind A -- runtime-state precondition, correctly claim-free.** `ARC-007` ("the
  residue field must carry live non-flat structure in A0"; "the A0->A1 harm gap must
  reproduce EXQ-114's magnitude") and `ARC-018` ("`e2_world_r2 >= 0.6` measured IN-RUN";
  "rollout-derived scores must carry non-zero cross-candidate variance") assert what a
  RUN must exhibit. They reference no claim because there is nothing to reference.
  Not a finding.
- **Kind B -- a genuine orphan: a named substrate that no claim owns.** `Q-007`
  (status `active`) reads: *"Substrate-blocked on the candidate-differentiated
  modulatory-variance substrate (per-candidate modulatory variance + range-not-magnitude
  readiness gate seeded by the 643 autopsy)"*. That names a specific substrate, in
  prose, with no claim id, no `substrate_queue` entry, and therefore no owner anywhere.

Kind B is the enlightening case and the reason this is worth a pass of its own: **the
registry's own falsifiers may collectively be pointing at substrate nobody has
registered**, and if several orphans point at the *same* missing thing, that is a claim
waiting to be written. Classifying all 30 and running that search is chipped as
`chip-20260828-orphan-prerequisite-investigation` (`task_256fc89c`) rather than done
here.

**Minor, related.** Five ids are cited inside precondition blocks and are absent from
`claims.yaml`: `GAP-2` (x4), `GAP-7` (x3), `GAP-1`, `GAP-14`, `GAP-3b`. These are
almost certainly plan-namespaced pipeline gaps whose home is a `*_plan.md` status table
rather than the claims registry, so they are **not** broken references -- but per
CLAUDE.md a GAP id should be written qualified with its owning plan
(`goal_pipeline:GAP-2`), and bare they are ambiguous across plans. Folded into the same
chip as a hygiene note.

**Limit:** "names a registered claim id" is a weak proxy for "has a matched
prerequisite". A precondition can name a claim in passing without depending on it, and
can depend on one without naming it -- MECH-522's undeclared ARC-004 dependency (S4
instance 2) is exactly the second case. So 155/30 is a partition of *citation*, not of
*dependency*, and the chip's manual classification is what turns it into the latter.
