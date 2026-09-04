# Failure autopsy -- V3-EXQ-1001 (EXT-005 / SD-031 OOD attribution robustness under causal-structure shift)

**Status: `awaiting_human_confirmation`** (staging mode -- drafted by a subagent of
`/governance` session `governance-20260904-1347`; the Step 8 interactive gate is OWED and has
not been held, and Step 9b is drafted-only: `hypothesis_space_registry.v1.json` was NOT written.)

Generated 2026-09-04T14:11:17Z. Scope: single. Raw reconstruction with every number and the
per-seed / per-arm tables: `facts_V3-EXQ-1001.md` alongside this file.

---

## 1. One-paragraph summary

V3-EXQ-1001 is the out-of-distribution sequel to V3-EXQ-995. 995 established that SD-031's
single-pass comparator residual discriminates externally-caused from self-caused world change
in-distribution (MOVE_OK AUROC 0.644). Richens & Everitt (ICLR 2024) prove that an
in-distribution score cannot separate a genuine causal model from a correlational shortcut --
only robustness, or rapid re-derivability, under distributional shift can. 1001 supplied that
shift: a one-time 4-cycle rotation of the environment's action->displacement map, holding
surface statistics fixed (measured deviation 0.0079 against a 0.05 tolerance). Both load-bearing
criteria failed. Frozen, the comparator is at chance and at parity with its own action-shuffled
control. Readapted on a brief pass, it is above chance and above its own shuffled control in 5/5
seeds -- consistently, many-sigma, and roughly four times below the pre-registered 0.05 absolute
floor. **The autopsy narrows the manifest's `weakens` on SD-031 to `mixed`**, because one of the
two load-bearing criteria is analytically undecidable in this environment and the other is decided
by an absolute floor that has no positive-control anchor, against a re-adaptation budget that is
1.82% of the original fit in optimizer steps. What the run does contribute, and contributes
cleanly, is a 5/5-seed dissociation: the same brief pass recovered 44.2% of the shift-induced
forward-model error but only 17.0% of the discrimination. Routing is `/queue-experiment` as a
fan-out portfolio, not another letter.

---

## 2. Facts (condensed -- full tables in `facts_V3-EXQ-1001.md`)

Real run (`dry_run: false`); `check_dry_run_citations.py` clean on 1001, 995 and 783;
`excluded_dry_run_ids: []`. `validate_recording.py`: **OK, 0 always-core gaps**. One minor
recording gap: the run-pack `metrics.json` carries an empty `values` map (pack `manifest.json`
does carry `evidence_direction` + `evidence_direction_per_claim`, so scoring is not blocked).

**All ten readiness preconditions MET**, `gate_green: true`, `criteria_non_degenerate` true for
both criteria, `non_degenerate: true`. This includes the positive control
(`zworld_encodes_exogenous_change` 0.9954 vs a 0.8 floor), the negative control
(`move_ok_confound_absent` 0.4295, inside [0.4, 0.6]), the class-count floor (6132 vs 500), the
manipulation check (`shift_degrades_frozen_forward_fit` +0.0323), the readapt non-vacuity check
(`readapt_does_not_regress_frozen_fit` +0.0118), and the in-distribution positive anchor
(`pre_base_in_distribution_signature`: chance-gap 0.1437, bare-gap 0.2036).

### The verdict numbers

| criterion | vs bare | vs chance | vs shuffled-action | verdict |
|---|---|---|---|---|
| **D1** frozen | +0.0777 (sd 0.0096) PASS | **+0.0198** (sd 0.0036) FAIL | **-0.0040** (sd 0.0061) FAIL | FAIL |
| **D2** readapted | +0.0987 (sd 0.0078) PASS | **+0.0408** (sd 0.0040) FAIL | **+0.0117** (sd 0.0047) FAIL | FAIL |

Requirement for every clause is `max(0.05, 1.0*sd)`. **In every failing clause the absolute floor
0.05 binds**; the noise-aware half would require only 0.0036-0.0061, all cleared several times over.
Both floors were pre-registered in the driver's `THRESH_CHANCE_ABS_FLOOR` /
`THRESH_ACTION_ABS_FLOOR` constants and stamped into the manifest's `pre_registered_thresholds`.
They were added at authoring time by the 2026-09-03 red-team pass, i.e. **before** the run --
this is not a post-hoc bar.

Derived: pre-shift AUROC 0.6437; frozen degradation 0.1239; readapt recovery over frozen 0.0210.

### Four facts that shape the reading

**(a) The "beats bare" clause both criteria pass is hollow.** Post-shift bare change-magnitude
AUROC in the scored stratum is 0.4370-0.4550 -- **below chance in 5/5 seeds and in every arm**
(pre-shift bare is likewise 0.4295-0.4473). A comparator carrying literally zero information
(AUROC 0.500) would clear a 0.05 gap-vs-bare floor against a 0.444 reference automatically. This
is exactly the effect governance recorded on EXT-005 for 995 ("the bare reference sits at 0.43,
below chance, so ~0.07 of the C2 gap is the bare delta anti-discriminating"), and it is why the
2026-09-03 red-team added the chance and shuffled clauses. **The tasking question -- is
"beats bare" hollow while gap-vs-chance is the real bar? -- is answered YES, and the driver had
already reached the same conclusion prospectively.** Both operative clauses fail.

**(b) D1 cannot discriminate the hypothesis, by construction.** The driver's own SCOPE LIMITATION
states it: the environment's physics *is* a four-entry action->displacement lookup table, and
"no model -- causal or correlational -- can be zero-shot invariant to a relabelled lookup table
(this is explicit in the design above: FROZEN is EXPECTED to degrade)". So D1's FAIL is predicted
identically by the shortcut hypothesis and by the genuine-causal-model hypothesis. A criterion
whose failure both hypotheses predict carries no discriminating information -- it is the
"gate that cannot discriminate by construction" shape, and it is stamped `load_bearing: true`.
The combination rule (`PASS = D1 OR D2`) means D1 does not cause the FAIL on its own; but the
FAIL is reported as 0/2 and the label reads `no_readaptation_recovery`, so the artifact must say
plainly that only D2 was ever informative.

**(c) D2's floor has no anchor, and the budget is 7x smaller than the manifest's framing implies.**
The driver names this itself as an OPEN RESIDUAL LIMITATION and deliberately declined to fix it:
there is no scratch-model or unshifted-env control establishing what magnitude of recovery a
same-budget re-derivation *should* produce. The two cheaper gates it substituted rule out the
degenerate zero-recovery case only -- and both passed, while the criterion they stood in for
failed. Compounding this: the manifest describes the readapt budget as "~13% of the original epoch
budget" (8/60 epochs), which is literally true and materially misleading. The pre-shift fit ran
`ceil(28000/256) = 110` optimizer steps x 60 epochs = **6600 steps**; the readapt pass ran
`ceil(3600/256) = 15` x 8 = **120 steps**. That is **1.82%**, because a post-shift epoch is 7.3x
smaller. Corroborated by the loss curves: readapt ends at 0.0372-0.0470, still above the pre
fit's epoch-60 losses of 0.0279-0.0321.

**(d) The run's genuine, non-confounded finding is a dissociation, 5/5 seeds.**

| quantity | PRE | FROZEN | READAPT | degradation | recovery | recovered |
|---|---|---|---|---|---|---|
| held-out forward MSE | 0.03038 | 0.06427 | 0.04929 | 0.03389 | 0.01498 | **44.2%** |
| MOVE_OK AUROC | 0.64366 | 0.51977 | 0.54078 | 0.12389 | 0.02101 | **17.0%** |

Per seed: MSE-recovered [0.42, 0.48, 0.39, 0.40, 0.52]; AUROC-recovered
[0.17, 0.19, 0.13, 0.16, 0.20]. MSE recovery exceeds AUROC recovery in every seed, ratio ~2.6x.
**The residual's discriminative content does not track its forward-prediction quality under
re-derivation.** This is not explained by budget starvation alone -- the same 120 steps moved MSE
substantially. It is the one thing here that a shortcut reading predicts and a
genuine-model reading does not, and it is what keeps the direction off `non_contributory`. Caveat
stated rather than buried: MSE and AUROC are different scales and a 44%/17% comparison is a
signal, not an identity. The successor should *record the recovery curve* rather than leave this
to an endpoint inference.

### Two provenance facts a reader would otherwise get wrong

**1001's PRE_BASE arm is a bit-identical REPRODUCTION of 995's BASE arm, not a replication.**
MOVE_OK AUROC 0.64365963683816507 in both (17 significant figures); gap-vs-bare identical to
one ulp; same seeds, same budget, same deterministic code path. It therefore adds **no independent
statistical weight** to 995's in-distribution result and must not be counted as a second
supporting run. What it does establish, and this is worth keeping, is that the result survived
the substrate change between commits `e82e328` and `1a82903` (different `substrate_hash`)
unchanged. The gap-vs-shuffled differs at the fourth decimal only because the shuffle draws its
own RNG stream.

**The manipulation is n=1.** All five seeds apply the identical `rotation_offset=1` 4-cycle. One
of the 24 permutations of the four movement actions is sampled; seed variance measures env/init
noise, not shift-instance variance.

---

## 3. Claim-layer mapping -- which of the four claims did this run actually exercise?

**The run already answered this itself, correctly, and the manifest is more accurate than the
tasking brief.** `evidence_direction_per_claim` reads
`{SD-031: weakens, ARC-037: non_contributory, MECH-095: non_contributory, EXT-005: non_contributory}`,
set by the driver's own red-team finding 7 fix. `build_experiment_indexes.py` line 3612 reads
`run.evidence_direction_per_claim.get(claim_id, inferred_direction)`, so the per-claim map is
honoured by the indexer and only SD-031 receives `weakens`. **Correction on the record: the brief's
premise that the manifest currently reads `weakens` for all four claims is false.**

| claim | type / status | exercised? | verdict |
|---|---|---|---|
| **SD-031** | design_decision, candidate, `standard`, v3_pending, phase v3 | **YES** -- E2WorldForward IS SD-031's comparator; this is the only claim the run touches | direction narrowed `weakens` -> **`mixed`** |
| **ARC-037** | architectural_commitment, candidate, no epistemic_category, phase v3 | **NO** -- ARC-037 asserts an anterior-insula-analogue routing circuit gating errors into E3 vs E1. The agent is constructed and never driven; the comparator is scored offline on RandomPolicy transitions. The manifest says so verbatim: "ARC-037's own E3/E1 routing/gating is NOT exercised here" | `non_contributory` |
| **MECH-095** | candidate, `substrate_ceiling`, phase **v5**, `pending_retest_after_substrate: true` | **NO** -- MECH-095 is the TPJ agency comparator on the z_self/z_world interface, parked as a substrate ceiling and mapped to SD-047. No TPJ comparator is instantiated, no routed/baseline contrast is run | `non_contributory`, peripheral co-tag -- see section 6 |
| **EXT-005** | external_failure_mode, subject `llm.causal_attribution`, candidate, `standard` | **NO** -- no V3 run observes an LLM. The manifest's own `attribution_caveat` states a FAIL "does not weaken the LLM-side assertion" | `non_contributory` |

**Did the experiment test SD-031 under conditions where the claim could express itself?**
Partly. SD-031's registered `what_would_answer` names a two-part non-degeneracy precondition:
(1) `world_dim >= 128` -- MET (128 here); (2) "ARC-065 behavioural diversity active in the main
agent path (balanced agent-caused vs externally-caused world events)" -- recorded as NOT met.
This run does not instantiate ARC-065, but it satisfies the *intent* of (2) by a different route:
RandomPolicy draws uniformly over the action set, and the resulting class balance is confirmed
empirically at 6132 minimum-class events in the scored stratum. So the gate is functionally
cleared and the FAIL is not a "premature test" artefact.

But SD-031's own falsifier is about **in-distribution** discrimination -- "residual magnitude for
self-caused events is not measurably smaller than for externally-caused ones" -- and that is
exactly what 995 passed and what this run's own PRE_BASE arm reproduces. The property that failed
here (robustness or cheap re-derivability of the action-conditioned component under structural
relabelling) is **not asserted by SD-031's registered text**. That does not make the FAIL
irrelevant: if the in-distribution discrimination is a memorised action->effect lookup, then
SD-031's substantive reading -- "the agent's run-time causal signature in latent space", the basis
for moral attribution of non-harm consequences -- is weaker even in-distribution, which is precisely
the Richens & Everitt point and why the sequel was run. It does mean the FAIL bears on an
unregistered sub-property via an inference, not on the claim's own falsifier directly, and that
the strength of that inference is exactly what (b) and (c) above undercut.

**Out-of-domain check (the V3-EXQ-698 / MECH-175 trap):** EXT-005 is the candidate here -- a
clinical-adjacent, external-system claim about LLMs, tested in a gridworld. It is not stamped
`out_of_domain` because the run correctly declares itself `non_contributory` to it rather than
attempting a claim-layer verdict; the reading is scoped to the REE-side remedy exactly as 995's
caveat requires. No reclassification is recommended.

---

## 4. Biological-reference triage

**Closest mechanism.** Corollary-discharge / efference-copy comparison on the world-consequence
stream: posterior-parietal and MD-thalamus/colliculus outcome-prediction loops (Sommer & Wurtz,
named in SD-031's own `functional_restatement`), with right supramarginal gyrus showing a decoding
*preference* for self-other attribution over sensorimotor information (Ohata et al. 2020,
Cereb Cortex, in `targeted_review_sd_031`).

**Is the mechanism a formal import? No -- but the failing CRITERION is.** This is the
load-bearing finding of the triage and it is worth stating carefully, because the usual REE
failure mode is a formal definition imported into a *mechanism* (SD-003's Pearl two-pass
counterfactual against Frith/Shergill's single-pass comparator, 28 FAILs before supersession).
Here the mechanism is a faithful biological translation and has already been through that
correction -- SD-031 *is* the single-pass successor to SD-003. **The formal import has moved into
the test.** Richens & Everitt's theorem is a statement about a regret-bounded agent facing a
decision problem; the lit entry's own limitations section says so, and says the bridge to any
other system "requires a bridging argument the paper does not make". This driver applies that
criterion to an offline residual-AUROC probe on RandomPolicy transitions in a four-entry
lookup-table world, with no agent in the loop and no regret bound anywhere. The philosophy
transfers; the mechanism does not. **Formal imports get the philosophy right and the mechanism
wrong at whatever level they enter, and the test level is not exempt.** Register this divergence
as load-bearing, per the skill's default.

**Does the failure resemble a missing dependency of the reference mechanism?** Partially, and in
a way that points at the budget rather than the architecture. Biological corollary-discharge
comparators *do* re-calibrate under sensorimotor remapping -- prism adaptation, visuomotor
rotation -- but over hundreds of error-driven trials. This run supplied a biologically plausible
**data** budget (3600 post-shift transitions) with an implausibly small **optimisation** budget
(120 gradient steps over them). The dependency that looks absent is not a mechanism REE lacks;
it is a plasticity budget the experiment did not give it.

**Ohata 2020 anticipated the measurement this run got right.** That entry's design lesson is
that attribution information is *distributed*, that separating it from sensorimotor information
took a preference analysis, and that "a validation that reads a single residual magnitude and
finds a gap risks recording as 'attribution' something that is partly the motor signal" -- with
the 2026-06-06 activation smoke named as exactly that vulnerable kind. The action-shuffled control
is that separation. Its post-shift value (frozen: -0.004) is therefore the biologically
best-warranted number in the run, and it is the one that goes to zero.

**`lit_status`: present, scoped.** Present for SD-031 (`targeted_review_sd_031`, 3 entries:
Ohata 2020, Wen 2023, Christensen 2018; plus 2 SD-031-naming entries in
`targeted_review_connectome_mech_256`), present for EXT-005 (`targeted_review_ext_005`,
5 entries including the Richens & Everitt paper that motivated this design), present for MECH-095
(`targeted_review_connectome_mech_095`, 14 entries). **ABSENT for ARC-037**, which has no dedicated
targeted review and appears only incidentally inside 3 EXT-005 entries. No `/lit-pull` commission
is issued for the SD-031/EXT-005 side -- the biology is already pulled and it is what the design
used. An ARC-037 lit gap exists but this run did not exercise ARC-037, so commissioning off this
autopsy would be scope creep; it is noted for a future ARC-037-exercising run.

**Novel-discovery quadrant note (never blend `lit_conf` and `exp_conf`):** SD-031 has strong
literature (three targeted entries plus the corollary-discharge cluster) and, after this run,
one PASS and one MIXED on experiment. That is not "under-supported"; the two are reported
separately and neither is averaged into the other.

---

## 5. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | **unclear** | A real negative signal on SD-031's action-conditioned component (readapted advantage over its own shuffled control recovers to 9.8% of pre-shift: 0.0117 vs 0.1194), confounded two ways -- D1 undecidable by construction, D2's floor unanchored against a 1.82%-of-original gradient budget. SD-031's registered falsifier is in-distribution discrimination, which this run's own PRE_BASE arm reproduces. |
| Biological reference | **partial** | Mechanism is a faithful translation (corollary discharge, rSMG attribution preference). The failing criterion is a formal import (regret-bound theorem) applied outside its stated scope. Re-calibration budget is not biologically calibrated. |
| Prerequisites | **present** | P0a moved 4/4 world-encoder tensors (0.371 worst seed, post-SD-070); E2WorldForward implemented 2026-06-06; world_dim 128 satisfies its hard assert; class balance 6132 min-class. |
| Implementation completeness | **complete** | Action pathway live and trained (wiring 0.283-0.399 at init -> 2.15-2.40 trained); `comparator_residual` exercised on every arm; `substrate_hash` present and stable across the run (1 snapshot, no drift). |
| Environment adequacy | **too sparse** | The action->effect structure IS a four-entry lookup table. The Richens shift class -- a structure shift under which a genuine causal model can hold accuracy while a shortcut cannot -- is not instantiable, because a permutation of a four-entry table is equally re-fittable by either. The driver states this itself. |
| Measurement adequacy | **under-instrumented** | (i) No unshifted-env / scratch-model same-budget ceiling (the driver's own OPEN RESIDUAL LIMITATION, deliberately out of scope). (ii) The 0.05 absolute floor is pre-registered and legitimate but arbitrary against what a 120-step budget should achieve. (iii) n=1 on the manipulation axis. |
| Integration adequacy | **isolated** | The agent is constructed but never driven; the comparator is scored offline. ARC-065 behavioural diversity in the main agent path and ARC-037's E3/E1 routing are both outside the loop. |
| Scale / capacity | **adequate (PRE), likely insufficient (READAPT)** | 6600 optimizer steps over 28000 transitions vs 120 steps over 3600. The "~13% of the epoch budget" framing overstates the gradient budget 7.3x. |

### Failure-location summary (GOV-FAILLOC-1)

Semantics used, stated so a reader can check the call: `established` means that layer
independently reads adequate/complete and therefore cannot excuse the failure -- this is the
reading forced by the skill's operative sentence, "reach REE FAILED only when Implementation,
Measurement and Environment above each independently read adequate/complete."

| bucket | reads from | verdict |
|---|---|---|
| MECHANISM | Implementation completeness = `complete` | **established** |
| MEASURES | Measurement adequacy = `under-instrumented` | **not_established** |
| ENVIRONMENT | Environment adequacy = `too sparse` | **not_established** |
| REE FAILED | all three | **false** |

**Failure-location: MIXED (MEASURES + ENVIRONMENT) -- not chargeable to REE, and not to SD-031's
mechanism on this evidence.** The implementation is complete and the readiness gates all passed,
so a half-built comparator is not the excuse; but two of the three independent layers read
inadequate, so the REE FAILED reading is unreachable, and so is a clean single-bucket MECHANISM
charge.

### Why this is NOT `substrate_ceiling`, despite wearing its fingerprint

Every absolute, negative-control and readiness criterion passed while both discrimination
criteria failed. That is the textbook substrate-ceiling tell, and it should be said out loud
rather than quietly declined. It is declined here for three reasons, and the third is the one
with consequences:

1. **The discrimination criterion is not known to be at a ceiling** -- it is known to be
   un-anchored. Without a same-budget positive control there is no evidence that *any* budget
   fails, only that this one landed at 0.041 above chance.
2. **The environment, not the substrate, is what cannot carry the criterion.** A ceiling reading
   would point at building more comparator; the diagnosis points at a test bed whose causal
   structure is a lookup table.
3. **Stamping `substrate_ceiling` has mechanical consequences that this evidence does not
   license.** It would put SD-031 into `_EPI_SUPPRESS_PROPOSAL` (excluded from GOV-GRAN-1
   surfacing) and make it not-v3-testable in `_claim_v3_testable` (starving it of experiment
   lanes), and it would open a re-derive-brake tally on a claim currently sitting at **0** hits --
   all on a finding with an identified, cheap, non-substrate repair. `standard` with the diagnosis
   in the note fields is the behaviour-preserving mapping the skill prescribes for the
   measurement / test-design family.

**Conditional-category check.** SD-031's stored `epistemic_category` is `standard` and its own
2026-08-28 note records *why* it moved off `substrate_ceiling` (GFLAG-0059: the dim=32 granularity
basis was refuted by V3-EXQ-783, and `check_substrate_ceiling_audit.py` had reported it as
genuinely orphaned). There is no stale conditional stamp with an unmet re-check trigger. Putting
`substrate_ceiling` back would reverse a deliberate 2026-08-28 governance correction on evidence
that does not reach it. Recommendation: `standard` stands.

**Failure-mode labels** (for the note fields, never the category):
`criterion_unanchored_absolute_floor`, `environment_cannot_instantiate_shift_class`,
`formal_import_at_the_test_level`.

---

## 6. Recurrence, the re-derive brake, and the peripheral co-tag

**Granularity-debt recurrence trigger: DOES NOT FIRE for SD-031, ARC-037 or EXT-005.**
Read with `granularity_debt_cluster.py`, counting tagging targets (never a prose grep):

| claim | tagging targets | alignment distribution | trigger |
|---|---|---|---|
| SD-031 | 1 -- `failure_autopsy_V3-EXQ-783_2026-07-18` (run `v3_exq_783_zworld_granularity_training_crossing_...`, claim_ids [Q-002, SD-031], `diagnostic_no_direction` / `instrument_validated_cause_discriminated`) | **intact=1** | does not fire -- the reader's own rule: no target reads `weakened`, so this is measurement or implementation debt, not granularity debt |
| ARC-037 | 0 | -- | does not fire |
| EXT-005 | 0 | -- | does not fire |
| MECH-095 | 17 across 6 files | other=6, weakened=4, unclear=3, intact=2, n/a=2 | **would fire** -- but this run does not exercise MECH-095; see below |

This autopsy sets SD-031's alignment to `unclear`, not `weakened`, so SD-031's cluster after this
target reads intact=1 / unclear=1 -- still no `weakened`, still not granularity debt.

**Re-derive brake: DOES NOT FIRE.** R1-R3 recipe run verbatim from `/Users/dgolden/REE_Working`
over confirmed-status artifacts:

| claim | ceiling hits | threshold | brake |
|---|---|---|---|
| **SD-031** | **0** | 2 | does not fire -- a redesign re-queue is permitted |
| ARC-037 | 0 | 2 | does not fire |
| EXT-005 | 0 | 2 | does not fire |
| MECH-095 | **12** | 2 | already far past this threshold, and past GOV-CEIL-1's N=3 |

### The peripheral co-tag, and why it is handled the way it is

MECH-095's 12 hits are `047m`, `741`, and ten grandfathered cluster targets (`047i`, `047j`,
`089` x2, `098b` x3, `121`, `011`, `510` x2). **This target contributes no thirteenth hit**, and
that is by construction, not by special-casing the counter: with the blanket
`recommended_epistemic_category` = `standard` and blanket `recommended_evidence_direction` =
`mixed`, the R1-R3 `counts()` predicate returns `False` for every one of the four claims on this
target. Verified by running the recipe.

**MECH-095 is deliberately OMITTED from `recommended_epistemic_category_per_claim`, and the
omission is the point.** Declaring `substrate_ceiling` for it -- the obvious move if the goal were
to record "its stored value stands" -- would satisfy the counter's first guard and make this
peripheral target count as a thirteenth ceiling hit, which is exactly the miscount the
peripheral-co-tag rule exists to prevent. Declaring `standard` for it would risk governance
overwriting a stored value this run has no business moving. So it is omitted, its
`per_claim_recommendation.change` is `STANDS`, and the JSON carries a
`recommended_epistemic_category_per_claim_note` saying in terms that MECH-095's stored
`substrate_ceiling` and `pending_retest_after_substrate: true` **stand unchanged** and that the
blanket `standard` is not an instruction to overwrite them.

**What MECH-095's state implies, surfaced not adjudicated** (`read_across_not_adjudicated` in the
JSON). MECH-095 sits at 12 ceiling hits with a stored `substrate_ceiling`,
`pending_retest_after_substrate: true`, `implementation_phase: v5`, a granularity-debt cluster of
17 targets that *does* contain `weakened` readings, and an evidence note recording an OWED retest
("queue the agency-detection retest on the SD-047 multi-source substrate") whose two attempts
(047l, 047m) both died of measurement degeneracy -- so the owed positive-discrimination retest has
still never validly run. That is simultaneously a GOV-CEIL-1 exhaustion question and a
`/claim-synthesis` granularity-debt referral, and it deserves to be in front of the user as its
own governance item. It is **not** adjudicated here: V3-EXQ-1001 does not exercise MECH-095 in
any respect, and folding a twelve-hit ceiling question into a comparator-robustness autopsy that
never touched it would be exactly the kind of inherited-tag error this section exists to catch.

---

## 7. Learning extracted

1. **Measurement gap (primary).** An absolute PASS floor on a recovery-under-shift DV is
   uninterpretable without a same-budget positive-control ceiling. The driver named this as its
   OPEN RESIDUAL LIMITATION and shipped anyway; the run then failed on exactly that clause. The
   two cheaper non-vacuity gates it substituted rule out the degenerate zero-recovery case and
   nothing more -- and both passed while the criterion they stood in for failed. That is the
   general lesson: a non-vacuity gate is not a substitute for a ceiling.
2. **Measurement gap (secondary).** A budget stated in epochs is not a budget. 8/60 epochs reads
   as 13%; in optimizer steps it is 120/6600 = 1.82%. Pre-register re-derivability budgets in
   optimizer steps or gradient-sample counts, never in epochs across differently-sized datasets.
3. **Environment gap.** The Richens criterion needs an environment with causal structure to be
   robust *about*. In a four-entry lookup table it degenerates. The driver diagnosed this
   correctly and narrowed the claimed interpretation -- but a narrowed interpretation only
   prevents over-reading a PASS; the same honesty is owed when reading a FAIL, and this autopsy
   supplies it.
4. **Biology divergence, load-bearing.** This is the SD-003 pattern relocated from the mechanism
   to the test. SD-003 imported a formal definition into a mechanism and burned 28 FAILs. Here
   the mechanism is already the biological correction, and the formal import is the criterion.
   Register the divergence rather than treating it as a caveat to refine.
5. **The finding worth keeping.** 44.2% of forward-MSE degradation recovered against 17.0% of
   AUROC degradation, 5/5 seeds, MSE > AUROC in every seed. The comparator's discriminative
   content does not track its forward-prediction quality under re-derivation. Make this a
   *recorded readout* (a per-epoch recovery curve on both quantities) in the successor, not an
   endpoint inference.
6. **Measurement caveat for the whole 995/1001 family.** Bare change-magnitude AUROC in the
   MOVE_OK stratum is below chance pre- and post-shift, in all 15 arm rows. The gap-vs-bare
   clause certifies nothing on its own. Carry this into EXT-005's evidence note as a standing
   caveat rather than a per-run observation.
7. **Recording gap, minor.** The run-pack `metrics.json` is an empty values map. Adjudication was
   not blocked, but no headline metric reaches the pack's metrics channel. Cite the Experimental
   Recording Standard (`evidence/planning/experimental_recording_standard_2026-07-12.md`) and
   populate it in the successor.
8. **Design coverage.** Five seeds of one permutation is n=1 on the manipulation axis. Sample
   several permutations.
9. **Provenance.** A same-driver reproduction of a predecessor's arm is not corroboration. It is
   a valuable substrate-stability datum and must not be counted as a second independent support.

---

## 8. Repair pathway and routing

**Work-graph classification: `complex (probe-gated) / puzzle (known rules)`.** The frame is
well-posed and a *fact* is missing -- what recovery a same-budget re-derivation should achieve,
and whether recovery scales with budget. Not `complicated (buildable)`: no substrate is unbuilt
and every readiness gate passed. Not `mystery (known data)`: more of the right data genuinely
would settle it. Not `aleatoric`: the effects are many-sigma and consistent in sign.

**Routing: `/queue-experiment`, as a NEW EXQ number, as a fan-out portfolio.**

New number, not a `1001a`: an alphabetic iteration is for a same-question implementation fix, and
a `1001a` would re-pose the same undecidable D1 in the same lookup-table environment. The question
being asked next -- what does the recovery-vs-budget curve look like against a same-budget
ceiling, and can this test bed discriminate at all -- is a different scientific question.

The re-derive brake does not fire for SD-031 (0 hits vs threshold 2), so a re-queue is permitted
and no refusal is owed. A portfolio is nevertheless preferred over a single re-pose because the
open question is a **discrimination** among three live hypotheses (GOV-FANOUT-1).

**`recommended_substrate_queue_entry.action: none`.** SD-031's entry exists and reads
`implemented`; the E2WorldForward implementation is complete and verified live in this run. The
repair is an experiment redesign, not a substrate build. Recorded explicitly rather than left
blank so the IGW workset's `_retest_blockers` does not read an omission as an unfilled entry. If
the H3 leg later confirms that environment richness is the binding constraint, *that* is the
substrate entry -- but it is a live hypothesis today, not a diagnosed gap, and creating one now
would pre-commit the fan-out's answer.

### Fan-out portfolio (GOV-FANOUT-1) -- three legs, three axis families

| leg | hypothesis | axis (family) | probe | declared null |
|---|---|---|---|---|
| H1 | the residual's discrimination IS a correlational shortcut riding the training-time action->effect map | `measurement` (instrumentation) | add an **unshifted-env control arm**: same PRE_BASE weights, same 15% / 8-epoch pass, on post-collection data from an UNMODIFIED `_action_map`. That arm's gap-vs-shuffled is the same-budget ceiling. Also emit per-epoch AUROC *and* MSE recovery curves | shifted-readapt gap-vs-shuffled >= unshifted-control gap-vs-shuffled - 1 sd (refutes H1) |
| H2 | re-derivation is real but starved | `curriculum` (process) | **budget ladder**: {2, 8, 30, 60} epochs x {5%, 15%, 50%, 100%} of post-shift transitions; DV = gap-vs-shuffled and gap-vs-chance as a function of realised optimizer steps | d(gap-vs-shuffled)/d(log optimizer steps) indistinguishable from zero over a 100x range (refutes H2, leaves H1 standing) |
| H3 | the environment cannot instantiate the criterion at all | `environment` (world) | repeat frozen/readapt in an environment whose action->effect mapping is **state-dependent or compositional**, shifting only a SUBSET of the structure so a model that learned the composition can hold accuracy on the unshifted subset | frozen gap-vs-shuffled on the unshifted structural subset == gap on the shifted subset, within 1 sd |

Three distinct axis families, none re-entered -- this opens fresh territory rather than circling.
**Do not queue a straight power-bump** (more seeds of the same rotation at the same budget): it
inherits both the missing ceiling and the undecidable D1. H1 and H2 share the readapt machinery
and could ride one driver with the control arm and the ladder as separate arm sets, which is
cheaper and keeps them paired on the same seeds -- if so, keep their declared nulls distinct in
the manifest so the legs resolve independently. Design-audit for coverage and verdict-aliasing
before queuing.

### Recommended per-claim dispositions

Current stored values were read before drafting each tail (see `facts_V3-EXQ-1001.md` section 2i).

| claim | direction | epistemic_category | `change` tail | why the tail is storable and not-yet-true |
|---|---|---|---|---|
| **SD-031** | `weakens` -> **`mixed`** | `standard` (unchanged) | `-> stamp failure_autopsy_V3-EXQ-1001_2026-09-04` | `live_status.evidence.from` currently cites `failure_autopsy_V3-EXQ-783_2026-07-18`, so the new stamp is not yet true and clears by provenance. `epistemic_category: standard` was NOT used as the tail because it is already the stored value. |
| **ARC-037** | `non_contributory` | set **`standard`** | `-> epistemic_category: standard` | ARC-037 carries **no** `epistemic_category` field at all today -- storable and not yet true, so this clears both by value and by provenance. |
| **MECH-095** | `non_contributory` | (omitted -- stored `substrate_ceiling` stands) | `STANDS` | Genuinely nothing for governance to write. `STANDS` is skipped by GOV-APPLY-1, which is correct. |
| **EXT-005** | `non_contributory` | `standard` (unchanged) | `-> stamp failure_autopsy_V3-EXQ-1001_2026-09-04` | `epistemic_category: standard` is already stored (an already-true tail would clear the row falsely); `live_status` carries no `evidence` block at all, so the stamp is storable and not yet true. |

`recommended_diagnostic_evidence_adjudicated` is **not** set on any claim: `experiment_purpose`
is `evidence`, and the skill restricts that flag to `diagnostic` / `baseline` targets -- setting
it here would paper over a genuine evidence gap on a claim that should accumulate scoring entries.

`pending_retest_after_substrate` is **false** for SD-031, ARC-037 and EXT-005 (no substrate gap
is diagnosed; the repair is an experiment). MECH-095's existing `true` is untouched. Per the
skill's standing rule, no `non_contributory` / substrate-limitation recommendation is being made
without that pairing -- and the check on whether the remaining supports are narrow is: SD-031's
only experimental support is V3-EXQ-995, single-pathway, and this run's PRE_BASE arm is a
reproduction of it rather than a second pathway. Stated plainly so the "illusory conflict
resolution" trap is closed: SD-031 has **one** independent experimental support, not two.

### Draft `evidence_quality_note`

The exact text governance should write is in the JSON at
`targets[0].recommended_evidence_quality_note`. It is not restated here to avoid the two copies
drifting.

---

## 9. Step 7b fires and their disposition

`autopsy_pre_routing_checks.py --artifact <draft>.json --json`, as-of `generated_utc`
2026-09-04T14:11:17Z. **First pass: 5 fires. After acting on C1 and C2: 3 fires, all C3.**
Full dispositions are also stored machine-readably at `targets[0].pre_routing_checks`.

| check | names | disposition |
|---|---|---|
| **C1** | `v3_exq_011_mech095_tpj_proxy`, `v4_sd031_e2_world_forward_stub` | **DISMISS both, reasons read off the files.** `v4_sd031_e2_world_forward_stub.py` is an explicit non-runnable design stub -- its docstring says "THIS IS NOT A RUNNABLE V3 EXPERIMENT" and "DO NOT QUEUE THIS SCRIPT", and it raises `NotImplementedError` at substrate construction. It was written in April 2026 as a V4 placeholder before E2WorldForward existed; the substrate landed 2026-06-06 and 995/1001 are the real drivers. It never scored because it cannot run. `v3_exq_011_mech095_tpj_proxy.py` is MECH-095's z_self efference-copy proxy -- its Condition B is explicitly that z_self does NOT discriminate causal origin, so z_world routing is necessary -- a different mechanism on a different stream; and a run_id `v3_exq_011_mech095_tpj_proxy_20260317T204144Z_v3` does appear as a MECH-095 cluster target, so the "never scored" clause is about run_id shape. Neither implements any of the three recommended probes, all of which need arms this repo has no code for. Fire cleared once both were named. |
| **C2** | `agency_comparator_testbed_sd047` | **ACT.** The pointer was correct: an entry unblocking one of this target's claims existed and the draft did not mention it. It is a MECH-095 test-bed for the 047l/047m label-saturation defect, priority 2, already `implemented`, unrelated to SD-031's comparator. It does not change the `none` action, but the artifact owed the reader the check; now named and dispositioned in `recommended_substrate_queue_entry.note`. Fire cleared. |
| **C3** x3 | `targeted_review_sd_031` (3), `targeted_review_connectome_mech_095` (14), `targeted_review_ext_005` (5) | **DISMISS all three -- the documented scope-blindness.** C3 matches the literal token ABSENT anywhere in `lit_status` and cannot read scope. This artifact declares literature PRESENT for exactly the three claims C3 names, with the entry counts C3 itself reports, and ABSENT only for ARC-037 -- which genuinely has no dedicated review (verified by grep over `evidence/literature/`; it appears only inside 3 EXT-005 entries). The one claim actually declared absent is not among the fires. **Not dismissed as noise:** each fire was re-checked against the filesystem first, and had ARC-037 turned out to have a review this would have been an ACT. Per the skill, this disposition is carried to the Step 8 gate rather than settled mechanically -- the user is the one who tells a flatly-false `absent` from a correctly-scoped one. |
| **C5** | -- | Reported `inapplicable` on the first pass ("prose-keyed check, but no sibling .md narrative") because this file did not exist yet; re-run after it landed. **`inapplicable` is not `no fire`** -- a structurally-blind check means Step 7c carries that load. |
| **C6-narrow** | -- | **No fire, and hand-checked anyway for the mirror case C6 cannot see** (a metric constant where the design requires it to vary). MOVE_BLOCKED bare-delta AUROC is exactly 1.0000 in all 15 arm rows and STAY bare-delta is 0.9954-0.9972 -- both structurally saturated, but both non-verdict-bearing by design and neither enters any criterion. Every verdict-bearing MOVE_OK metric varies across seeds and every criterion's sd is strictly positive. One genuine minority dissent found and reported in the prose rather than smoothed: POST_FROZEN's gap-vs-shuffled is positive in seed 43 (+0.0054) and negative in the other four; the artifact states the mean as -0.0040 and makes no uniform-sign claim. |

**Step 7c (adversarial red-team) was NOT run by this subagent** -- the parent `/governance`
session owns it, per its tasking. Note for whoever runs it: the driver itself already carried
**two** Fable red-team passes at authoring time (pass 1 BLOCKING, pass 2 CONTESTED, plus a third
non-red-teamed closure pass), which is why the design is unusually clean and why the productive
attack surface here is the **routing and the direction call**, not the arithmetic. The three
specific things to attack: (i) is `mixed` right, or is `weakens` defensible given that D2's
operative clauses failed by 4x? (ii) is the 44%/17% MSE-vs-AUROC dissociation load-bearing, or is
it a scale artefact of comparing a squared-error ratio with a rank-statistic ratio? (iii) does
declining `substrate_ceiling` under-weight the fact that every control passed while both
discrimination criteria failed?

---

## 10. Open question this draft could not settle

**Is the 0.05 absolute floor the right bar for a re-derivability DV, and if not, what is?**
The floor is pre-registered, legitimate, and binding -- and there is no principled basis in the
record for its value on *this* DV, because nothing establishes what a same-budget re-derivation
should achieve. That is precisely the H1 probe's job, and it is why the direction call is `mixed`
rather than `weakens`. If the user judges that a 4x miss on both operative clauses is decisive
regardless of the missing anchor, `weakens` is the defensible alternative and the routing does
not change. This is the question to put at the Step 8 gate.

---

## 11. Apply checklist for `/governance` (nothing below is applied by this skill)

1. SD-031: `evidence_direction` narrowed `weakens` -> `mixed`; `epistemic_category` stays
   `standard`; append the drafted `evidence_quality_note`; move `live_status.evidence` onto
   `failure_autopsy_V3-EXQ-1001_2026-09-04`.
2. ARC-037: `non_contributory`; set `epistemic_category: standard` (the field is absent today).
3. **MECH-095: change nothing.** Stored `substrate_ceiling` and
   `pending_retest_after_substrate: true` STAND. The blanket `standard` in this artifact is an
   adjudication-scope value for this run and the brake counter, not a storage instruction.
4. EXT-005: `non_contributory`; append the OOD-sequel result and the standing below-chance-bare
   caveat to the 995-based note; open a `live_status.evidence` citation.
5. Apply the Step 9b `hypothesis_space_ledger_pending` block: register the new question
   `sd031_causal_signature_shortcut_vs_model` (3 hypotheses, Mode A, all `alive`). No
   `axis_families.map` delta is needed -- `measurement`, `curriculum` and `environment` are all
   already mapped. Then run `build_hypothesis_space.py` and
   `check_hypothesis_space_integrity.py` and clear any flag before committing.
6. Chip the fan-out portfolio to `/queue-experiment` **after** ratifying this routing at Step 2b
   -- not before, and not from this autopsy (this session spawns nothing). Check
   `igw_routine_ledger.json` / `igw_assignments.json` first in case auto-discovery already staged it.
7. Separately, and not as part of this item: put MECH-095's 12-ceiling-hit state in front of the
   user as its own governance question (GOV-CEIL-1 exhaustion and/or `/claim-synthesis`
   granularity-debt referral, plus the still-never-validly-run SD-047 retest).


## Red-team pass (Step 7c) and revision -- 2026-09-04T14:48:02Z

**Reviewer:** Fable 5.1 (separate agent, reasoning withheld, JSON-first). **Verdict: CONTESTED. All six findings ACCEPTED** by the confirming governance session (governance-20260904-1347). Arithmetic survived in full (1.82% readapt budget; 44.2% vs 17.0% recovery; post-shift bare AUROC 0.437-0.455, below chance 5/5; MECH-095 at 12 R1-R3 hits; floors pre-registered; D1 undecidable by construction; PRE_BASE bit-identical to 995's BASE).

- **F1 (routing, changes the portfolio).** The H1 leg's unshifted-env control has nothing to recover (PRE_BASE was fit on the canonical map), so its declared null (readapt >= unshifted - 1 sd, i.e. >= ~0.113) is already falsified ~10x by this run's 0.0117. Replaced by the **scratch-initialised same-budget arm** (driver OPEN RESIDUAL LIMITATION option 1): H1 predicts readapt-from-PRE_BASE <= scratch (no positive transfer); H2 predicts readapt >> scratch. The unshifted arm is kept only as the asymptote row.
- **F2 (evidence base).** V3-EXQ-995 tagged EXT-005 only; SD-031's genuine experimental record is V3-EXQ-1001 alone. The draft's "one PASS and one MIXED" framing was wrong; the stake is that `weakens` would make one unanchored run SD-031's entire record.
- **F3 (prohibition collision).** SD-031's `what_would_answer` carries a STANDING PROHIBITION (GAP-6 two-part gate; ARC-065 half NOT met) and the plan says "Do NOT queue ... would be vacuous". The draft's prose argued the RandomPolicy construction-balanced design functionally clears the diversity half (as 995 did) but nothing carried that into the registry. Added `apply_checklist_additions_2026_09_04`: governance must either amend `what_would_answer` + GAP-6 to accept construction-balanced comparator-only designs, or rule the substitute inadequate (then 1001 is precondition-unmet -> non_contributory for SD-031). Decision owed at the Step 8 gate; recommendation (a).
- **F4 (numbers).** gap_vs_chance is 0.0408 vs 0.05 = 1.23x below the floor, not ~4x (gap_vs_shuffled is the 4.3x miss). ~75% of the readapt AUROC gain is action-conditioned (-0.004 -> +0.0117): the better basis for `mixed` than the MSE/AUROC dissociation, which is itself shortcut-consistent. H2 is a hypothesis, stated as such.
- **F5 (measurement).** The shuffled-action control is ONE permutation draw per arm; 995-vs-1001 PRE_BASE shuffled deltas reach 0.0103 per seed, the same order as D2's 0.0117. Learning item added; the portfolio must use >= 5 draws.
- **F6 (co-tag mechanics).** MECH-095's non-counting depended on the blanket `mixed`; with a blanket `non_contributory` it would have become a silent 13th ceiling hit. `recommended_epistemic_category_per_claim.MECH-095 = standard` is now declared explicitly (peripheral, not exercised), which the counter honours regardless of the blanket.

Withdrawn readings recorded under `withdrawn_readings_2026_09_04` in the JSON. Direction: `mixed` for SD-031 remains the recommendation; `weakens` is equally defensible on the pre-registered falsifier and is put to the user at the gate on the corrected facts.


## Confirmation -- 2026-09-04T18:55:13Z

Status **confirmed** at the /governance Step 8 gate (session governance-20260904-1347, user present). Decisions: {"Q1": "Apply all four as revised", "Q2_SD031_gate": "Amend SD-031 what_would_answer + self_attribution GAP-6 to accept construction-balanced (RandomPolicy, offline-scored) comparator-only designs for the ARC-065 diversity half", "Q3": "Add 6 buildable v3 substrate stubs", "Q4": "Apply the three August staging-autopsy ledger blocks now", "recommendation_agreement": "3 of 4 recommended options selected (Q4 against); logged via record_recommendation_outcome.py"}
