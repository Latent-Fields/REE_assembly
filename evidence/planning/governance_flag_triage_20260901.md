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
