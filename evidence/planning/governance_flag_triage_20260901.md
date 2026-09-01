# Governance-flag triage, 2026-09-01

**Session:** `gov-flagtriage-20260901` (follow-on to governance cycle `gov-cycle-20260901`).
**Scope:** all 33 open flags of type `stale_note` and `evidence_discrepancy`, excluding the two
raised by the governance cycle itself that same day (GFLAG-0107, GFLAG-0108 — both known to still
hold). The 18 `contested_disposition` flags are NOT covered here; they are researched separately.

**Method.** Six read-only agents, partitioned by flag, each asked one question per flag: *does this
flag's assertion still hold against current repo state?* Verdicts are one of STILL-HOLDS,
PARTIALLY-RESOLVED, SUPERSEDED, SELF-RESOLVED, CANNOT-VERIFY. Agents could not edit or resolve
anything. Findings marked **[spot-checked]** below were independently re-verified by the session
before being recorded; the rest are agent-reported with the cited evidence.

---

## Headline result: 0 of 33 self-resolved

| verdict | count |
|---|---|
| STILL-HOLDS | 25 |
| PARTIALLY-RESOLVED | 7 |
| SUPERSEDED | 1 |
| **SELF-RESOLVED** | **0** |
| CANNOT-VERIFY | 0 |

The triage was proposed on the expectation that the backlog was partly inflated with
already-satisfied false positives — the governance cycle that morning had found exactly that shape
in GOV-APPLY-1 (8 of 8 ACTIONABLE rows already applied) and in the substrate-ceiling audit (2 of 2).
**That expectation was wrong for this population.** These flags are live findings that have never
been worked. The backlog is real, not stale.

This matters for how the backlog is read: a large open-flag count here is not evidence of a noisy
detector, and should not be discounted the way the GOV-APPLY-1 / ceiling-audit ACTIONABLE buckets
now must be (GFLAG-0107, GFLAG-0108).

---

## Four flags are wrong about their own cause

The most consequential class found. Acting on any of these literally would have done the wrong work.

- **GFLAG-0070 (MECH-268) — blames an indexer bug that does not exist. [spot-checked]**
  The flag says V3-EXQ-729's two PASS runs are "absent from claim_evidence.v1.json" and that
  "neither manifest carries a scoring_excluded flag", inferring a same-day-requeue bug in
  `build_experiment_indexes.py`. All three points are false: both runs ARE present as MECH-268
  entries, both carry `scoring_excluded: "degenerate"`, and that derives from the manifests' own
  `non_degenerate: false` / `degeneracy_reason: "harm_class_fraction_on: zero spread"`, present
  since their only commit `131b01408f` (2026-07-10) — i.e. already true when the flag was raised.
  This is degeneracy exclusion working as designed.
  **The wrong diagnosis was then written into the registry:** MECH-268's `what_would_answer` now
  asserts "a real indexer gap ... likely a same-day-requeue handling bug in
  build_experiment_indexes.py". That sentence is false and should be corrected.
  The *residual* real question is separate and genuine: can a PASS with `non_degenerate: false`
  discharge MECH-268's ecological bar at all? Neither 729 run has an autopsy.

- **GFLAG-0093 (MECH-457, INV-088) — names the wrong file.**
  It says `generate_current_front.py` reads a `hero.surviving` field that "no longer exists
  anywhere in the registry" and "silently prints a stale cached count". Half true, wrong file:
  that script reads `hypothesis_space.v1.json` (a DERIVED file, regenerated 2026-09-01T07:42:18Z),
  not `hypothesis_space_registry.v1.json`. The figures are freshly derived, not cached. The real
  defect is upstream at `build_hypothesis_space.py:367` — `if synthesis and
  synthesis.get("surviving_label"): surviving = alive + 1` fires unconditionally, ignoring that
  the `competence_floor` question is `decided` (2026-07-25) and `CLOSED TO FURTHER FAN-OUT`
  (2026-08-08). A session "fixing generate_current_front.py" would be editing an innocent file.
  The stale "1 of 20 rivals standing" figure is live in `docs/CURRENT_FRONT.md:18` and in
  `work_graph_debt_classification_20260827.md:14,106` (the latter is hand-written, not generated).

- **GFLAG-0075 (MECH-205) — universal-vacuity rider overstated. [spot-checked]**
  The code finding HOLDS: `pe_surprise_threshold` is still `0.001` (the known-vacuous value) at
  `ree-v3/ree_core/utils/config.py:3175`, `:6803`, `:8130`, and `git log -S` shows exactly one
  commit ever touching it (`fab7693769`, 2026-04-09). But the rider — that any run enabling
  `surprise_gated_replay` at the default "writes ZERO ... and reads vacuously green" — is not
  universal: V3-EXQ-887/887a/887b record `surprise_write_count` 2602/3554/3208 (writes fire; 887b
  is a PASS/supports), while only V3-EXQ-432 shows the vacuity mode (`n_surprise_writes_d2: 0`).
  The vacuity is PE-scale-dependent. Note also that flipping the default is NOT behaviour-neutral:
  the 887 family's baselines were run at 0.001 with live writes.

- **GFLAG-0071 (ARC-058 half) — a misreading.**
  It says ARC-058's `live_status` cites `failure_autopsy_V3-EXQ-445h_2026-06-19`, whose
  `targets[].claim_ids` is "['SD-032b'] only". That autopsy has FOUR targets, the fourth being
  `claim_ids: ["ARC-058"]`, `failed_criterion: "not_tested"`,
  `recommended_evidence_direction: "non_contributory"` — present since its only content commit
  `8c85851508`, whose message even ends "ARC-058 untested." The pointer is accurate.
  The flag's SD-048 half does still hold (see the table).

---

## Two flags badly understate their own scope

- **GFLAG-0064 — names 3 claims, affects 16. [spot-checked]**
  `SD-003` is `status: superseded` (2026-04-18, by MECH-256 + SD-029). The flag names INV-076,
  MECH-341 and SD-013 as carrying a dead `depends_on` edge to it. Sixteen claims do: SD-013,
  ARC-037, MECH-025b, MECH-205, MECH-206, SD-032b, MECH-258, MECH-273, ARC-059, MECH-276,
  MECH-277, ARC-081, MECH-341, INV-076, ARC-096, INV-102.
  **And the obvious repoint is wrong for SD-013:** both successors already depend on it
  (`MECH-256.depends_on = [ARC-033, SD-013]`, `SD-029.depends_on = [SD-011, ARC-033, SD-013,
  MECH-256]`), so repointing SD-013 -> MECH-256/SD-029 creates a cycle. For SD-013 the right move
  is probably to DROP the edge, which is a decision, not a substitution.
  `scripts/validate_claims.py` has no check for a superseded `depends_on` target, which is why the
  class accumulated silently — adding one would stop it recurring.

- **GFLAG-0072 — one leg fixed, three not.**
  The MECH-440 leg IS discharged: V3-EXQ-955 (2026-08-29) ran at `class_floor_used: 5`,
  `non_degenerate: true`, giving the lineage its first non-degenerate conversion test, and
  MECH-440's `pending_retest_after_substrate` is now false. ARC-065, MECH-439 and MECH-441 are
  NOT: the `support_preserving_min_first_action_classes` default is still 2
  (`ree-v3/ree_core/utils/config.py:2294`) across 276 driver call sites, and MECH-439's newest
  evidence run (V3-EXQ-571b, 2026-09-01) still hard-sets floor 2. MECH-441 has zero experimental
  entries.

---

## One duplicate pair

**GFLAG-0053 and GFLAG-0061 are the same finding** on the same single field
(`arc_062_rule_apprehension:GAP-B` `resume_condition`), raised a day apart. The stale string
occurred exactly once in the file, so one edit discharged both. **[spot-checked]** Both resolved
this pass.

---

## The pattern behind several of these: self-documented, never applied

Repeatedly, the session that RAISED a flag also wrote the finding into the affected claim's own
text minutes beforehand. Commit `711da29a02` (2026-08-28 06:47Z) lands ~3 minutes before three
separate flags from the same lineage; `25c05dbd6e` does the same for GFLAG-0062; GFLAG-0060's
retest was written into `what_would_answer` by its own raising session.

The effect is that a claim now *documents its own defect* while the defect stands — and the
documentation usually lands in a DIFFERENT field from the wrong one. GFLAG-0073 is the sharpest
case: its "its own block hides this" complaint was discharged 3 minutes before the flag was raised,
while the two fields it names (`live_status`, `evidence_quality_note`) are still stale.

**Operational consequence: "the note mentions it" must never be read as "it was applied."** That
inference is what a triage pass is most likely to get wrong, in the direction of retiring live work.

---

## Applied this pass (7 flags resolved)

| flag | what was done |
|---|---|
| GFLAG-0050 | 944a ERROR record -> `evidence_direction: superseded` naming V3-EXQ-944b, BOTH flat and run-pack copies, `superseded_by` set. Zero scoring effect (0 occurrences in `claim_evidence.v1.json`). Dry-run gate run first. |
| GFLAG-0053 | GAP-B `resume_condition` corrected (654h RAN TERMINAL FAIL 2026-06-21T17:57Z); original retained as HISTORY; node `last_updated` 2026-08-01 -> 2026-09-01. Node stays `in-progress`. |
| GFLAG-0061 | Discharged by the same edit. Its second assertion (MECH-309's claims.yaml block is current) verified true; no claims.yaml change owed. |
| GFLAG-0060 | MECH-257 `evidence_quality_note` records the EXQ-452a retest (2 runs 2026-05-05, `pe_harm_surprise_corr` 0.182/-0.021, later run superseded). No status/confidence move — both runs diagnostic, `genuine_exp_count` stays 0. |
| GFLAG-0089 | `arc004_timescale_stratification_probe_20260826.md` annotated in place: the "-0.159 points the wrong way" direction claim withdrawn as non-reproducible (`CausalGridWorld()` is unseeded; re-runs give -0.125, -0.097; the 20260828 topology probe gives +0.034..+0.102 with a clean fidelity check). **FAIL verdict unaffected and strengthened.** |
| GFLAG-0092 | Closed as a bookkeeping desync — Q-040's own note has said "OVERTAKEN ... and resolved" since 2026-08-29 while the flag record still read open. The literal 862a -> `superseded` write was deliberately NOT made: 862b produced no valid replacement reading, so asserting a substitution would be false. |
| GFLAG-0094 | `MECH-439` added to `INV-090.depends_on`. Dependency-tracking gap only. Comment records that MECH-439's premise is now REGIME-DEPENDENT (`failure_autopsy_V3-EXQ-571b_2026-09-01`), not the flat 88-89% in its title. |

---

## Still open, with the work each actually needs

Effort and judgement columns are the agents'. "Judgement" means it requires choosing between
defensible dispositions rather than correcting a fact.

| flag | claims | verdict | what it actually needs | effort | judgement |
|---|---|---|---|---|---|
| GFLAG-0054 | MECH-464 | STILL-HOLDS | `build_experiment_indexes.py:6151` zero-evidence branch only emits for `open_question`; every other claim_type falls to `continue`. ~8 claims invisible to /lit-pull. | moderate | yes |
| GFLAG-0056 | MECH-465 | STILL-HOLDS | Reachability declared settled on a pooled-across-seeds rv distribution not reproducible within-seed; `epistemic_category` promotion rests on it. Adjudicate WITH 0057. | moderate | yes |
| GFLAG-0057 | MECH-465 | STILL-HOLDS | Extends 0056: two July spikes reach the opposite conclusion, never cited. | moderate | yes |
| GFLAG-0058 | MECH-263, SD-033b | STILL-HOLDS | Notes end at 485m; the FULLSTACK handoff they make (714, 719a, competence_floor closure) is never closed out. Narrative gap — no untagged run. | moderate | yes |
| GFLAG-0062 | SD-054 | STILL-HOLDS | `pending_retest_after_substrate` comment cites 603h; lineage is now at 603l/603o/603v. Which is the current blocker is the call. | trivial | yes |
| GFLAG-0063 | Q-042 | (contested — researched separately) | | | |
| GFLAG-0064 | INV-076, MECH-341, SD-013 | STILL-HOLDS | See scope note above: 16 claims, and SD-013 needs a DROP not a repoint. | trivial-moderate | yes (SD-013 + sweep scope) |
| GFLAG-0066 | MECH-317 + | (contested — researched separately) | | | |
| GFLAG-0067 | MECH-091 | PARTIAL | 944b review DONE; GAP-7 node still `blocked` and the substrate_queue `validation_note` still describes the FAILED 944. Whether a 5-of-6-seed PASS discharges the node is the call. | moderate | yes |
| GFLAG-0069 | ARC-108, MECH-450, MECH-439 | STILL-HOLDS | Two nodes read `blocked_on_upstream` on an instrument that landed 2026-08-19 (`ree-v3 c309bc6486`). Residual is an unmade 713x re-letter decision; no decision-log entry exists. | moderate | yes |
| GFLAG-0070 | MECH-268 | STILL-HOLDS | Diagnosis refuted (above). Real question: does a `non_degenerate: false` PASS discharge the ecological bar? Also correct the false indexer-bug sentence in the registry. | moderate | yes |
| GFLAG-0071 | ARC-058, SD-048 | PARTIAL | ARC-058 half is a misreading. SD-048 half holds: the 512a manifest was corrected 2026-08-28 but SD-048's note still says "PASSED ... evidence_direction supports". | moderate | yes |
| GFLAG-0072 | ARC-065, MECH-440/441/439 | PARTIAL | MECH-440 leg fixed; other three legs need a raised-floor re-test, or the flag narrows to MECH-440 and closes. | moderate | yes |
| GFLAG-0073 | MECH-322 | PARTIAL | Arithmetic holds (1 of 2 scoring entries; 896 is the only non-excluded one). `live_status` + `evidence_quality_note` still stop at 892. | trivial (+ owed run) | no for the note edits |
| GFLAG-0074 | MECH-092, MECH-205, MECH-121, MECH-209 | STILL-HOLDS | **[spot-checked]** `_do_replay` assigns `replay_trajs` at `agent.py:10418`/`:10425` and the function ends; no consumer exists anywhere in `ree_core/`. Real substrate build. | deep | yes (what the consumer should do) |
| GFLAG-0075 | MECH-205 | STILL-HOLDS | Code finding holds; rider overstated (above). Either promote 1e-5 or record a decision to keep 0.001. | trivial to make, moderate to land | yes |
| GFLAG-0078 | SD-069 | STILL-HOLDS | Got HARDER: V3-EXQ-963 (2026-08-30) re-ran at the SAME 2400 cap the claim says to exceed, starved worse (16 cells), and hit a new `tonic_axis_live` precondition failure. Now gated on SD-PROBE-WARMUP validation too. | deep | yes |
| GFLAG-0079 | MECH-090 | STILL-HOLDS | Routed substrate landed 2026-08-01 under a sibling queue id; the prescribed retest was never queued (`experiment_queue.json` items is empty). | deep | yes |
| GFLAG-0081 | ARC-088, MECH-463 | STILL-HOLDS | ARC-088 has NO `evidence_quality_note` field at all and 1 literature entry; the contradicting 785a result lives only on MECH-463. | moderate | yes |
| GFLAG-0082 | MECH-441, MECH-440 | PARTIAL | Retired ARC-110/707 hold still in both claims' routing notes; replacement ARMED-CONVERSION hold written into `what_would_answer` only. Cited 707b is itself superseded by 707c. | moderate | yes |
| GFLAG-0083 | ARC-071 | STILL-HOLDS | `implemented_validated` rests on contract tests only; the behavioural DV (`n_genuine_commits/n_e3_ticks`) has never been measured. Claim also points at a dead sd_id. | moderate (trivial for the sd_id) | yes for the relabel |
| GFLAG-0090 | MECH-520, MECH-522 | STILL-HOLDS | Both lean on ARC-004's unmet premise; MECH-522 names ARC-004 in its argument without declaring it in `depends_on`. Sequence after the ARC-004 call (0055/0088). | moderate | yes (no for the depends_on fix) |
| GFLAG-0093 | MECH-457, INV-088 | STILL-HOLDS | Wrong file named (above). Real fix is `build_hypothesis_space.py:367` plus a hand edit to a non-generated doc. | deep | yes |
| GFLAG-0095 | MECH-424, MECH-373, MECH-422 | STILL-HOLDS | Precondition names MECH-373/MECH-422; neither in `depends_on`. But MECH-424's own notes deliberately class MECH-373 as a cross-reference — promoting it contradicts a recorded editorial decision. | trivial | yes |
| GFLAG-0096 | MECH-521 | STILL-HOLDS | The owed toy WAS run (2026-08-26) and named a missing third ingredient (shared normalisation budget); the claim still says "Nothing in the record names this probe." | moderate | no for the amendment itself |
| GFLAG-0097 | Q-007 | STILL-HOLDS | V3-EXQ-643a measured the blocking range at 0.22 and PASSED, but carries `claim_ids: []` so it reaches no claim. Whether 643a's range is Q-007's z_beta requirement is the call. | moderate | yes |
| GFLAG-0098 | ARC-105, Q-083, MECH-425 | STILL-HOLDS | Three genuine orphans, no owner in queue/ledger/code. But each claim's own text already says "do not build in V3" — arguably the current state IS the disposition. | moderate | yes |
| GFLAG-0099 | MECH-521, ARC-134, MECH-448 | STILL-HOLDS | Resume brief's "S9.9d still open" is stale; GFLAG-0096's amendment unapplied; MECH-448 wrong-population finding not on the claim. Parked across 9 sessions on one build-commission call. | moderate | yes |

---

## Cheapest next actions, if the backlog is worked further

Ordered by value per unit effort, judgement-free first:

1. **Correct the false indexer-bug sentence in MECH-268's `what_would_answer`** (GFLAG-0070) — the
   registry currently asserts a bug that does not exist.
2. **GFLAG-0073 note edits** — advance `live_status` and append the 896 paragraph. No judgement.
3. **GFLAG-0096 amendment** — the derivation doc's own recommendation, endorsed by GFLAG-0099.
4. **GFLAG-0064's two mechanical repoints** (INV-076, MECH-341) — leaving SD-013 and the other 13
   for a decision.
5. **Add a superseded-`depends_on`-target check to `scripts/validate_claims.py`** — stops the
   GFLAG-0064 class recurring at all.

---

## What this record deliberately does not do

No claim status, confidence, `epistemic_category` or `v3_pending` moved in this pass. The seven
resolutions above are fact corrections and one bookkeeping close; every disposition question is
left open for governance. The 18 `contested_disposition` flags are out of scope here.

---

# Part 2 — contested dispositions researched (12 flags)

Same session, second pass. Five read-only agents, partitioned by CLUSTER rather than
arbitrarily, because several flags are two views of one decision. Each was asked for a decision
BRIEF, not a verdict: verified premises, the real question, mutually exclusive options with the
strongest argument against each, and whether the call is decidable on desk evidence or needs a
run. Of the 18 open `contested_disposition` flags, 6 already have owners (GFLAG-0101..0105
chipped to `/claim-synthesis` this cycle; GFLAG-0109 is the recorded MECH-479 residual), leaving
these 12.

**Nothing in Part 2 was applied.** These are briefs for governance to decide from.

## Reclassifications — two flags are not what they are filed as

- **GFLAG-0063 is NOT contested.** It quotes a promotion trigger that is ALREADY APPLIED — Q-042
  reads `status: candidate_resolved` and has since 2026-05-08. The trigger it actually needs is
  the next sentence in the same field. Its cited evidence is wrong twice over (it asserts a
  five-run retest cohort "ran to completion under StepHarness"; the cohort autopsy's own section 1
  records that three of the five were never queued), but its recommendation survives on evidence
  it did not cite. Near-mechanical promotion to `resolved` plus a bookkeeping correction.
- **GFLAG-0080 is contested, but about a far narrower question than it states.** Its central
  assertion — "the graded arbitration weight has never been built" — is REFUTED: SD-081/MECH-477
  landed `_arbitrate_dual_system` (ree-v3 `e3_selector.py:1390`, gated at `:2834`) on 2026-07-22,
  and V3-EXQ-811a PASSed on it 2026-07-24, five weeks before the flag. What survives is real but
  narrow: SD-081 arbitrates DEPTH under UNCERTAINTY, whereas MECH-235 claims arbitration on
  URGENCY and commitment. Different independent variables.

## The registry-contamination finding (extends Part 1's "self-documented, never applied")

Part 1 found that flags' raising sessions write findings into the affected claim's own text. Part 2
shows the same mechanism carrying FALSE statements into the registry. Four confirmed:

| claim | registered text asserts | why false |
|---|---|---|
| MECH-268 | "a real indexer gap ... likely a same-day-requeue handling bug in `build_experiment_indexes.py`" | No such bug; the runs are correctly degeneracy-excluded (Part 1, GFLAG-0070). |
| MECH-235 | "a graded arbitration WEIGHT ... must exist and be readable per-tick. IT DOES NOT, as of 2026-08-28." | Built 2026-07-22, validated by a PASS 2026-07-24. |
| Q-042 | the named retest cohort "ran to completion under StepHarness ... in all five" | Three of five never queued, per the cohort autopsy's own section 1. |
| ARC-004 | MECH-058 "was directly tested in V3-EXQ-019 via lag-k autocorrelation -- it FAILED and the claim was retired" | Retirement PREDATES that run by two days and rested on a learning-rate ablation; the lag-k run's TIMESCALE criteria (C1, C2) both PASSED. The FAIL came from a reafference criterion (C3) and an underpowered step count (C4, n=969 < 3000). |

The ARC-004 case is the most consequential: GFLAG-0055 uses that precedent as its central argument
for supersession, and the precedent's real shape -- a claim retired on an ill-posed test and
reframed -- cuts the other way. The bad citation also propagates into at least one other planning
artifact.

## Per-cluster outcomes

### ARC-004 depth-is-timescale (GFLAG-0055, 0088) — DECIDABLE NOW
- The falsifier could NOT have passed: the depth cascade is three parallel first-order filters
  sharing one hardcoded time constant applied to three within-tick functions of the same input.
  ARC-004's registered non-degeneracy precondition describes wiring that has never existed.
- WIRING, NOT TRAINING, is the binding constraint: on the real stack with UNTRAINED encoders,
  serial smoothing reaches ARC-004's own PASS bar at d-b = +4.342 vs a 0.510 bar, 10/10 seeds,
  fidelity check max|manual - stack.encode()| = 0.000e+00. This is what makes it a
  "wrongly implemented" rather than "false" question.
- Blast radius on RATE is 4 of 38 dependents, not the 36 quoted in the claim's own text; the other
  ~34 depend on the stack being layered and differentiated, which the FAIL branch preserves.
- ARC-004 has NO `evidence_quality_note` field and 0 entries in `claim_evidence.v1.json`. Whatever
  is decided must CREATE the record, not amend one.
- Brief recommends narrow + reclassify to `substrate_conditional` (medium confidence) over
  supersede. THE PIVOT, stated by the brief: if "L-space IS a multi-timescale latent stack" is read
  as the claim's assertion rather than its framing, supersede or split is correct instead.
- Three corrections are owed regardless of disposition: create the `evidence_quality_note`; fix the
  MECH-058 citation; add ARC-004 to MECH-522's `depends_on` (undeclared, GFLAG-0090's).

### Replay & consolidation family (GFLAG-0076, 0086) — 3 of 4 sub-decisions DECIDABLE NOW
- The alleged MECH-092/MECH-205 contradiction DISSOLVES twice over. Textually they address
  different stages (anchor-selection vs proposal-distribution), each claim saying so itself.
  Substantively, MECH-289's anti-recency is wired NOWHERE: SD-038 is `ready: false`, hint reads
  "not implemented", and no anti-recency code exists in `ree_core/`. At most one exists.
- THE REAL CONTRADICTION IS INTRA-CLAIM: MECH-092's `functional_restatement` says "standard
  experience replay" while its own `notes` say "NOT standard experience replay" -- and MECH-289's
  notes assert this was corrected 2026-04-24. It was not.
- GFLAG-0086's reverse-dep list is 4; the real count is 25.
- UNOWNED BLOCKER, named by no flag: `_do_replay` (`agent.py:10418/:10425`) computes replay
  trajectories and discards them; no consumer exists anywhere in `ree_core/`, and the gap has NO
  `substrate_queue.json` entry despite being cited by four claims.
- "Building the consumer unblocks all four" is HALF TRUE: it unblocks MECH-092's benefit half and
  MECH-205 leg (iii); MECH-121 and MECH-209 stay blocked on unbuilt balanced-replay scheduling AND
  the MECH-439 conversion ceiling. Those two have zero experimental entries between them.

### MECH-317 absorption (GFLAG-0066, 0084, 0087) — ONE DESK SESSION AWAY
- The absorbing claim is NOT a validated survivor: ARC-071 has `genuine_exp_count 0`,
  `exp_conf 0.0`, quadrant `plausible_unproven` -- THE SAME QUADRANT as MECH-317. The evidence-tree
  discriminator that decided the 2026-08-15 orphan adjudication does not separate them at parent
  level.
- The children's support reduces to one un-autopsied scored FAIL (829) and one PASS degenerate on
  its load-bearing criterion: 829a's `interpretation.criteria_non_degenerate.C2 = False`, with
  `all_iso_on_cells_sit_on_forced_bar: true` and rho = 0.9999999999999998 -- an arithmetic identity,
  not a measurement. Note the run's TOP-LEVEL `non_degenerate` reads True, so the run-level gate
  reports clean while the criterion carrying the verdict is degenerate.
- A PRIOR ADJUDICATION already exists and no flag cites it: EXP-0263/EVB-0227 was gated
  2026-08-02 with `gating_reason` recommending exactly `superseded_by ARC-071/MECH-323/MECH-324`,
  25 days before GFLAG-0066.
- `SD-083` IS A CROSS-REGISTRY ID COLLISION: `claims.yaml` SD-083 is
  `consolidation.offline_policy_consolidation_window`; `substrate_queue.json` sd_id SD-083 is the
  MECH-324 reacquisition read. The 2026-09-01 V4 cut already reads it through the wrong lens. Any
  action on "SD-083" without disambiguation hits the wrong object.
- MECH-312b is a second orphaned consumer of MECH-317, named in no flag's `claim_ids`.
- Brief recommends: write the absorption-check memo FIRST (the in-house MECH-318 template, no run
  needed, and the owning closure node already owes it) and apply its verdict; do not apply a
  disposition ahead of the memo. These three flags are five decisions; three are independent and
  should be lifted out.

### Standalone dispositions (GFLAG-0051, 0080, 0085, 0091)
- **GFLAG-0051 is contested EXACTLY as stated** -- the one clean case in Part 2. A decision was
  routed once (2026-08-18) and explicitly deferred by GFLAG-0043's resolution. Its cost estimate is
  TOO HIGH, not too low: `Trajectory` already carries `action_objects` into `e3.select`, so no
  signature change or threading remains -- only a nonlinear scoring term and the semantic decision.
- **GFLAG-0085**: ARC-027 has 100% run overlap with SD-010 (6 of 6 entries shared, 0 independent),
  and its 6 reverse-deps -- not the 2 the flag lists -- all already hold SD-010. Independent of the
  merge question there is a LIVE SCORING ERROR: ARC-027's `confirmed_established` badge and
  `lit_conf 0.821` are fed by nociception-anatomy literature the claim's own text declares out of
  domain. Both of its nominated precedence signatures are compromised (one is another claim's
  `weakens` entry; one came from a frozen-encoder run).
- **GFLAG-0091**: the population is ~155, not 121 -- but 2 of the 6 named claims are DETECTOR FALSE
  POSITIVES (INV-025's testable leg is built, run and passing; INV-026 likewise), and 103 of the
  155 ALREADY carry the `substrate_conditional` label the flag proposes, none of them routed. The
  gap is a missing EDGE, not a missing status. Brief recommends an edge-first policy staged behind
  a dry-run measurement (one session, no run) that would convert "155 unrouted" into "N genuinely
  ownerless, M merely unlinked" -- the ratio every option is implicitly priced against and that
  nobody currently has.

## Two corrections that went against the reporting session

Recorded because they bear on how much weight Part 2 should carry.

1. The session's spot-check of 829a's degeneracy read `criteria_non_degenerate` at TOP level and
   got `None`, appearing to contradict the agent. The agent was right: the field lives under
   `interpretation.criteria_non_degenerate` and does record `C2: False`. The session looked in the
   wrong place.
2. The session wrote "the resolved GFLAG-0097" into an agent's prompt. GFLAG-0097 is `open`. The
   agent checked rather than reasoning from the false premise, and said so.

## Cheapest next actions from Part 2

1. Correct the four false registry statements above. Independent of every disposition.
2. Register the missing replay-consumer `substrate_queue` entry -- a blocker cited by four claims
   that nothing is scheduled to build.
3. Rename the colliding `substrate_queue` sd_id off `SD-083`, and close that entry: the build it
   gates landed 2026-07-31 with contract tests and a validating run.
4. Promote Q-042 to `resolved` with the cohort correction (GFLAG-0063 -- reclassify out of
   contested first).
5. Write the MECH-317 absorption memo. No run; unblocks the largest cluster.
