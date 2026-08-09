# Thought Intake: Failure autopsy needs explicit failure-location buckets

**Date:** 2026-08-09
**Raw thought file:** `docs/thoughts/2026-08-09_failure_autopsy_failure_location_buckets.md`
**Registered:** GOV-FAILLOC-1 (candidate, `epistemic_category: governance_rule`)

---

## Verbatim prompt (raw thought, condensed)

> Recent inspection of V3-EXQ-906 suggests that REE failure autopsy does not yet discriminate
> sharply enough between fundamentally different meanings of experimental failure. At minimum, a
> failed experiment should consider four distinct failure locations: **REE FAILED** (fair test,
> mechanism instantiated, measures adequate, environment afforded the opportunity, competence still
> not demonstrated); **THE MECHANISM FAILED** (the specific mechanism under test did not
> instantiate/train/activate/propagate/causally influence as intended); **THE MEASURES FAILED**
> (the phenomenon may have occurred but the assay/metric/instrumentation could not detect it); **THE
> ENVIRONMENT FAILED** (the ecology did not provide a valid opportunity -- inadequate headroom,
> unreachable resources, unsafe spawning, premature termination, confounded incentives, or harm
> becoming effective before the agent has actionable perceptual access to its cause). Categories
> need not be mutually exclusive. Each bucket implies a different successor: REE failure ->
> investigate the organism; mechanism failure -> repair/replace/falsify the mechanism; measurement
> failure -> redesign instrumentation; environment failure -> redesign the ecology before drawing
> conclusions. Suggested action: update the failure-autopsy skill/process so every failed experiment
> explicitly performs failure-location triage across at least these four buckets before assigning
> interpretation, and prevent an experiment from being described as evidence of REE failure unless
> mechanism, measurement, and environmental adequacy have been sufficiently established.

Full text: [`docs/thoughts/2026-08-09_failure_autopsy_failure_location_buckets.md`](../../docs/thoughts/2026-08-09_failure_autopsy_failure_location_buckets.md).

---

## What's new vs existing REE docs (novelty table)

| Element | Already exists? | Where | Gap the thought closes |
|---|---|---|---|
| Per-run diagnostic table separating claim/biology/prerequisite/implementation/environment/measurement/integration/scale | **Yes, richer** | `.claude/skills/failure-autopsy/SKILL.md` Step 5, "Four-layer diagnosis" (8 rows) | The 8-row table is finer-grained than the thought's 4 buckets, but it is framed around **claim alignment** (`weakened`/`strengthened`/`intact`) -- it does not cleanly apply to a **claim-free, organism-level** showcase run (`claim_ids: []`), which is exactly the V3-EXQ-906a case that motivated this thought. |
| A gate requiring mechanism+measurement+environment adequacy before concluding demotion | **Yes, for claim demotion specifically** | SKILL.md Step 7 routing table: "Tested fairly + biology supports the mechanism + still fails -> Recommend governance demotion" + Core principle ("brains are an existence proof for the class... demotion is the highest threshold") | Already the operative rule for **claim-layer demotion**. The thought asks for the same discipline applied to **organism-level ("REE") competence claims that are not tied to any registered claim** -- i.e. the showcase/diagnostic case the existing gate does not reach, because it is written in claims.yaml-demotion terms. |
| A named, reusable 4-way vocabulary (REE / MECHANISM / MEASURES / ENVIRONMENT) applied as an explicit per-observation classification, before interpretation | **No -- until today, informally** | See "Independent validation" below | This is the concrete, genuinely new artifact: a compact, four-cell vocabulary that can be stamped on *any* observation (not just a scored criterion), and that explicitly requires a "none of the above cleanly, so do not charge REE" verdict as a first-class outcome. |
| "Harm effective before actionable perceptual access" as a named environment-failure mode | **No** | -- | Novel, specific environment-failure pattern. Directly validated: the 906a autopsy independently found the harm-onset radius (~11 cells) exceeded the sensory radius (2 cells) -- exactly this failure mode, discovered before the thought was written down but not yet named as a *general* triage category. |

### Independent validation (found during this intake, not anticipated by the raw thought)

The raw thought's proposed vocabulary was **independently and heavily applied in practice the same
day**, by a different session chain, in
[`evidence/planning/observational_review_V3-EXQ-906b_2026-08-09.md`](observational_review_V3-EXQ-906b_2026-08-09.md)
Section 7 ("Four-layer failure-location summary") -- generated 2026-08-09T17:17Z, using the
**exact same four column headers** (`REE FAILED | MECHANISM FAILED | MEASURES FAILED | ENVIRONMENT
FAILED`) against 10 organism-level observations from the V3-EXQ-906b run, concluding explicitly:
*"No observation is cleanly and solely 'REE FAILED.'"* The same document reuses the framing again
at Section 12e ("**Failure-location:** MIXED, same shape as 2b/4 -- not chargeable to REE alone").

Two sessions converging independently on the same four-way split, the same day, from the same
motivating cluster (V3-EXQ-906a/b), is unusually strong practical corroboration for a
methodology proposal that has not yet been formalized anywhere -- it was invented once (this
thought, ~08:00Z) and reinvented once more within the same session lineage (~17:17Z) without
either session citing the other. Neither instance registered a claim or amended the skill.

---

## Key formulations

1. **Failure-location is a classification act that should happen BEFORE interpretation**, not be
   inferred after the fact from which routing looks convenient. The existing four-layer table
   already asks the diagnosing session to fill in per-layer status; what's missing is (a) making the
   REE/mechanism/measures/environment framing explicit and *reportable* as its own summary row/column,
   and (b) extending it to organism-level, claim-free observations, where the existing table's
   claim-alignment framing doesn't apply.
2. **Non-exclusivity is load-bearing.** A single failed observation can be MIXED (mechanism +
   environment, e.g.) -- both the raw thought and the independent 906b validation explicitly use a
   "MIXED" / multi-tick verdict rather than forcing one bucket. This matches the existing skill's
   general posture ("almost every REE FAIL is contributory... state the interpretable signal
   explicitly") rather than requiring a new mechanism.
3. **"REE FAILED" should be the HARDEST bucket to reach, not the default one.** This is not new in
   principle (Core principle: "Claim falsification is the highest threshold") but the thought
   proposes making the *precondition check itself* (mechanism instantiated + measures adequate +
   environment afforded the opportunity) an explicit, required, reportable step for every failed
   run -- not only for runs that are about to demote a registered claim.

---

## Affected existing claims / docs

- No existing `claims.yaml` claim describes this failure-location vocabulary. Nearest neighbors are
  process/governance claims about autopsy discipline: **GOV-DIAG-1** (diagnostic-chain recurrence --
  a different axis, about *repeated* circling, not *locating* a single failure) and **GOV-CEIL-1**
  (ceiling-exhaustion demotion counter). Neither overlaps; both are `depends_on` candidates since the
  new rule would sit alongside them in the same Step 5-7 sequence of `.claude/skills/failure-autopsy/SKILL.md`.
- `.claude/skills/failure-autopsy/SKILL.md` Step 5 (four-layer diagnosis table) and Step 7 (routing +
  demotion gate) are the sections a formalization would extend, not replace -- see Next steps.
- `evidence/planning/observational_review_V3-EXQ-906b_2026-08-09.md` Section 7/12e is now the primary
  worked example / precedent for what the formalized version should look like in practice.

---

## Candidate claims

### GOV-FAILLOC-1 (registered in `claims.yaml`, this session)

- `claim_type: governance_rule`, `epistemic_category: governance_rule`, `status: candidate`
- Asserts: before an experimental observation (scored-criterion FAIL, or an unscored organism-level
  observation in a claim-free diagnostic) is described as evidence that REE itself failed, the
  autopsy/review must explicitly classify it against four failure-location buckets -- REE /
  MECHANISM / MEASURES / ENVIRONMENT, non-exclusive -- and reach REE-failed only when mechanism
  instantiation, measurement adequacy, and environmental opportunity have each been separately
  established (or explicitly could not be, in which case the verdict is MIXED/uncertain, not
  REE-failed).
- Not minted as an `EXP-####` proposal: this is a process/methodology rule, not a REE-internal
  empirical mechanism -- no falsifying experiment applies (same posture as GOV-HELDOUT-1, GOV-DIAG-1).

---

## Next steps

1. **Formalize into `.claude/skills/failure-autopsy/SKILL.md`** (and mirror to
   `.agents/skills/failure-autopsy/SKILL.md`) -- most naturally as an explicit summary
   row/requirement attached to Step 5's four-layer table (map: Implementation~MECHANISM,
   Measurement~MEASURES, Environment~ENVIRONMENT, and a new top-line REE-competence read gated on
   all three), and an explicit statement in Step 7 that the existing demotion gate's precondition
   ("tested fairly + biology supports the mechanism") applies equally to an organism-level
   "REE failed" read on a claim-free diagnostic, not only to claims.yaml demotion.
   **This is a standing-rule change and CLAUDE.md's held-out check applies before shipping it**:
   validate the proposed wording against >=3 historical autopsies where the old (implicit) and new
   (explicit-gate) wording would give different answers -- not just cases the four-layer table
   already handles identically. Good candidates to check against, found during this intake:
   `failure_autopsy_V3-EXQ-906a_894b_2026-08-09.md` (the direct motivating case),
   `observational_review_V3-EXQ-906b_2026-08-09.md` (the independent reinvention, non-autopsy format),
   and one or two older `substrate_ceiling` autopsies where a claim-layer demotion was recommended,
   to confirm the explicit gate would not have changed the historical call.
2. **Not started in this session** (thought-intake scope only, per CLAUDE.md Scope Discipline) --
   flagged as a candidate chip for a dedicated session once the held-out check above is run.
3. No experiment queueing follows from this (process claim, not an empirical one).
