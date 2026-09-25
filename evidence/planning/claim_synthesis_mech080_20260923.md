# Claim synthesis -- MECH-080 arm mapping (re-derivation from the 2026-09-23 literature)

- **Claim:** MECH-080 -- "Rollout truncation set-points as psychiatric individual differences substrate (ADHD/anxiety/OCD)" (`candidate`, `mechanism_hypothesis`)
- **Chip:** `chip-20260923-mech080-arm-mapping-resynthesis` (routed by governance cycle `governance-20260923-0717`; the MECH-080-specific user decision is `evidence/decisions/decision_log.v1.jsonl` line 577, inside the bulk hold acceptance `rec-20260923-34f34743`)
- **Finding being resolved:** GFLAG-0431 (evidence_discrepancy). It was closed on 2026-09-23 as *routed to this chip*, not as decided.
- **Evidence:** the five `targeted_review_mech_080` entries (REE_assembly `e363db1b52`, lit_conf 0.682, conflict_ratio 0.667)
- **Session:** `orchc0925-mech080`, subagent of `orchestrate-20260924-1707`, 2026-09-25
- **Applied part:** applied under the user's standing delegation via orchestrate-20260924-1707 (scope: a faithful re-derivation of the arm mapping from the landed literature; no split or merge; no status or confidence change). Everything outside that scope is in section 7, awaiting the user.

## 1. Why this is not a standard /claim-synthesis run (Step 1-3 gate)

`/claim-synthesis` exists to decompose a claim circled by a **cluster of experimental failures**. MECH-080 has no experimental failures: its only experiment proposal (EXP-0818) is `blocked_substrate` (arm 3 has no manipulation lever; the DVs sit behind commit-entry; and ree_core does no waking gradient learning at defaults, GFLAG-0491). The input here is five literature entries that disagree with the claim's **content** while agreeing with its **strategy**. Step 3 classes:

- vacuous criterion / test-design debt: no. No test has run.
- substrate-not-ready: yes for the *experimental* half, which is why no experiment is proposed. It does not bear on the literature half.
- genuine single-point falsification: no. The strategy is supported (section 3), so demotion is not indicated. GFLAG-0431 already said "revise, not promote or retire".
- granularity debt: **partly**. The claim bundles two assertions with different evidential fates, (A) a reductive strategy and (B) a one-disorder-per-arm assignment. That is the only decomposition question, and section 7 Q1 leaves it to the user.

The gate therefore passes only to a **content revision** of the arm mapping. It does not pass to child-claim generation.

## 2. The claim as registered (the mapping being re-derived)

From `claims.yaml` `notes` and `docs/architecture/valenced_hippocampal_map.md#mech-080`:

| Arm (computational signature) | Assigned phenotype | Assigned mechanism |
|---|---|---|
| 1. Truncation-biased: premature commitment | ADHD | BG urgency threshold too low (MECH-075) |
| 2. Extension-biased: over-withholding under uncertainty | Anxiety | Uncertainty chronically high, BG threshold too high (MECH-078) |
| 3. Attractor lock-in: perseveration after reversal | OCD | Abnormally deep basin inside rollout (MECH-076) |

**The V3 falsifier does not carry the clinical labels.** `what_would_answer` tests a *computational* three-way dissociation (premature harmful commits / withheld commits under uncertainty / repeated obsolete actions after reversal) and states that "psychiatric labels are outside V3". The arm re-assignment below therefore leaves the falsifier's logic intact. It changes what a positive V3 result would be *about* clinically, and four design constraints (section 5) that any future test must meet.

The claim has **no `evidence_quality_note`** (the chip brief assumed one exists). This revision adds the first one.

## 3. Evidence, arm by arm

| Entry | Dir / conf | Speaks to |
|---|---|---|
| Huys 2012, Pavlovian pruning (healthy adults, sequential tree task) | supports / 0.68 | **Strategy**: search depth is a real, individually varying parameter that tracks sub-clinical mood. Nothing on the three disorders. Truncation is *conditional* (triggered by a large loss), not an unconditional horizon cap. |
| Hauser 2017a, NSPN population cohort, information sampling | mixed / 0.62 | **Strategy**: one threshold-like parameter, dimensionally graded, gives over-withholding. **Arm 2**: the effect loads on *compulsivity* specifically, not on the affective dimensions. Mechanism: *delayed urgency emergence*, not a raised static bound. |
| Hauser 2017b, juvenile OCD vs controls (n=16/16); same group as 2017a (the clinical companion) | mixed / 0.55 | **Arm 2**: diagnosed OCD over-samples before committing, with accuracy preserved or *improved* (not a competence loss). Urgency emerges later, *raising the effective decision threshold*. **Arm 3**: OCD shows the arm-2 phenotype, which the claim routes elsewhere. |
| Voon 2015, OCD / binge eating / methamphetamine, two-step task | supports / 0.60 | **Arm 3 DV**: contingency-insensitive, model-free-dominant behaviour in OCD, with a caudate/mOFC correlate. The effect is *transdiagnostic* (also binge eating and methamphetamine use), so it does not pick out OCD specifically. **Arm 3 mechanism**: a *rival* account (the planner is bypassed by a habit system) that predicts the same behaviour as the claim's deep-basin-inside-rollout account. |
| Huang-Pollock 2017, ADHD vs controls (n=97/39), diffusion model, go/no-go | weakens / 0.70 | **Arm 1**: ADHD's excess errors decompose onto *reduced drift rate* plus an increased starting point, **not** a lowered boundary. Drift rate is competence, so that half falls inside MECH-080's own "reduces to lost competence" exclusion. The starting-point shift, though, is itself a set-point-like prior bias toward committing. Limits: one paediatric study (transfer 0.40); go/no-go has no forward rollout, so rollout depth is untested; the boundary is an analog of the E3 commit threshold, not `rollout_horizon`. |

## 4. Re-derived arm mapping (what the evidence supports)

| Arm | Registered occupant | Occupant the evidence supports | Status after revision |
|---|---|---|---|
| Strategy (one set-point family gives dissociable commitment-timing phenotypes; search depth is an individual-difference dimension) | -- | Supported by Huys 2012 and Hauser 2017a. Neither measures all three disorders. | **Retained, supported** |
| 2. Extension / over-withholding | Anxiety | **Compulsivity / OCD** (Hauser 2017a, population cohort, specific to compulsivity rather than affective dimensions; Hauser 2017b, diagnosed juvenile OCD, n=16/16, conf 0.55). Mechanism: urgency rises late, which raises the *effective* threshold. The evidence is on the time course, not only a static bound. | **Re-assigned: anxiety -> compulsivity/OCD** (two designs from one group agree; no pulled entry supports anxiety on any arm, so no competing assignment) |
| 3. Lock-in / perseveration after reversal | OCD | OCD shows the DV, and so do binge eating and methamphetamine use (Voon 2015, transdiagnostic). Mechanism unresolved: deep basin inside rollout (claim) vs habit dominance with rollout bypassed (rival). | **Occupant retained (not OCD-specific), mechanism contested** (two mechanisms, no evidential winner) |
| 1. Truncation / premature commitment | ADHD | Not supported as registered. The *boundary* reading of the named mechanism (low BG urgency threshold) found no difference. The signature is drift (competence, excluded) plus starting point (a set-point-like prior bias). Two readings survive and nothing discriminates them. A rollout-*depth* version is untested (no rollout in the task). | **Occupant and mechanism contested**: ADHD kept provisionally; the boundary reading is unsupported; drift-vs-starting-point-bias left open (Q7); at risk of the competence exclusion |
| (Anxiety) | Arm 2 (via MECH-078) | No arm supported by the pulled evidence. Hauser 2017a's specificity result counts against anxiety on arm 2. Huys 2012 (mood-linked, *loss-triggered* truncation) hints at an arm-1-like conditional variant, but was measured in sub-clinical mood, not anxiety. | **Unassigned pending evidence** (not dropped; see Q2). The arm-2 uncertainty grounding in MECH-078 goes with it: that link is now unexercised, not refuted. |

**The one-disorder-per-arm assumption is withdrawn.** On this evidence OCD occupies *two* arms at different phases of a decision: over-sampling before commitment (arm 2, checking) and perseveration after it (arm 3, ritual). These are not mutually exclusive, as Hauser 2017b notes. The claim's reductive strategy survives this. Its clinical three-way assignment does not.

**Why this counts as "obvious" under the delegation.** The one re-assignment (arm 2) moves an occupant where two designs agree and nothing in the pulled evidence competes. Every other change only lowers a support label to *contested* or *unassigned* and picks no replacement. Every place where the evidence supports two readings stays open, not decided: arm 1's drift-vs-starting-point reading, arm 3's mechanism, anxiety's new home, ADHD's rollout-depth version. (The red-team caught a first draft that marked arm 1's mechanism "withdrawn"; that picked one reading and was corrected to "contested".) No claim is split or merged, `status` stays `candidate`, and no confidence field is touched (lit_conf and conflict_ratio are indexer-derived).

## 5. Design constraints for any future test (recorded; the falsifier is NOT amended)

These follow from the literature and bind whoever eventually unblocks EXP-0818. They are recorded in the claim's revision block. Folding them into `what_would_answer` is a falsifier change and is left to the user (Q5).

1. **Arm 2: manipulate the urgency *time course*, not only the static commit bound** (Hauser 2017a/b). A raised bound and a slowed urgency ramp give different trajectories; only the ramp is evidenced.
2. **Arm 2 valid positive: shifted draws-to-commit with accuracy held or improved** (Hauser 2017b). The same shift with an accuracy drop is the competence-loss pattern, which the falsifier already excludes and which V3 is currently most likely to produce.
3. **Arm 1: separate drift from threshold.** Any arm-1 positive must show that the premature-commit effect is not carried by degraded evidence accumulation (Huang-Pollock 2017). Otherwise it models a competence reduction and gives it a clinical name. Also note Huys 2012: `rollout_horizon` is an unconditional cap and Pavlovian pruning is loss-conditional. They are different manipulations, and REE has no loss-triggered pruning knob.
4. **Arm 3: a second measurement of rollout-to-policy coupling** (Voon 2015). `steps_since_world_rule_shift` perseveration alone is satisfied equally by a deep-basin agent and by an agent whose rollout has stopped contributing to action selection. Under the conversion ceiling the second is the likelier failure mode. The readout exists today (`world_rule_shift_*` on the causal grid world); the missing piece is the lever, not the DV.

No experiment is proposed (substrate-blocked; see section 1).

## 6. What is applied (MECH-080 only; commit sha recorded in WORKSPACE_STATE and the chip resolution)

- `notes`: rewritten to state the re-derived mapping. The original mapping sentence is kept verbatim, marked superseded in part.
- New `arm_mapping_revised_2026_09_25` block: a per-arm occupant / status / grounding table, the withdrawn one-disorder-per-arm assumption, the four design constraints, and the open questions with a pointer to this doc.
- New `evidence_quality_note`: the first one for this claim. It covers the strategy-vs-content split and names the mapping-fidelity discounts (0.50-0.60) as the numbers to read rather than the headline directions.
- **Unchanged:** `title`, `status`, `live_status`, `depends_on`, `what_would_answer`, `epistemic_category` (none set), `subject`.
- `docs/architecture/valenced_hippocampal_map.md#mech-080` (the claim's `location` and `source`): each Condition cell in the differential-profile table gets its 2026-09-25 status, and a dated revision note under the table says that `claims.yaml` `arm_mapping_revised_2026_09_25` is the record. The original rows stay readable as the hypothesis as first registered. This keeps the two records from disagreeing, which is the shape GFLAG-0431 flagged in the first place.
- GFLAG-0431 is already `resolved` (closed as routed to this chip). It is not reopened. A new `contested_disposition` flag points `/governance` at section 7.

## 7. OPEN for the user (not applied)

- **Q1 -- Split into a strategy claim plus an arm-assignment claim?** (split = outside the delegation.) *Recommendation: do not split now.* The arm-assignment half has no V3 `what_would_answer`: the registered falsifier already says psychiatric labels are outside V3. A separate assignment claim would therefore be untestable in the substrate, which fails `/claim-synthesis`'s testability rail. The per-arm status table inside one claim carries the same information with no new id. Revisit if the assignment half acquires its own literature programme.
- **Q2 -- Where does anxiety go?** Three readings: (a) drop anxiety from MECH-080's scope; (b) re-home it to a *loss-conditional truncation* variant (Huys 2012), which would make it an arm-1 relative and flip its direction from extension to truncation; (c) leave it unassigned and commission a targeted lit-pull on anxiety / intolerance of uncertainty in information-sampling tasks. *Recommendation: (c)*, because (b) rests on one sub-clinical-mood study that never measured anxiety. The claim now records anxiety as unassigned, which is (c)'s state and does not foreclose (a) or (b).
- **Q3 -- Arm 3 mechanism: deep basin inside rollout (claim) vs habit dominance with rollout bypassed (Voon 2015).** They are behaviourally convergent and no pulled evidence discriminates them. The claim keeps its account as the hypothesis and records the rival. Constraint 4 is the discriminating measurement. No decision needed now unless you want the rival registered as its own claim.
- **Q4 -- Ownership overlap on arm 2.** Two registered claims already touch the re-assigned arm-2 content:
  - **MECH-434** (epistemic commitment timing; urgency/threshold failure poles, `claims.yaml` ~72446) *already* cites Hauser 2017's raised-threshold OCD over-gathering as its "epistemic-freezing pole", through the same urgency/threshold mechanism. This is the closer overlap: MECH-080 arm 2 and MECH-434's freezing pole now assert the same thing about the same paper.
  - **MECH-497** (checking degrades the confidence that gates stopping; accuracy preserved) predicts the same phenotype through a different mechanism. Its self-distinction is against MECH-080's *arm-3* lock-in account, and that distinction still holds.
  Also downstream: **MECH-088** (`depends_on` MECH-080) carries its own ADHD account (NA inconsistent sampling plus DA unstable attractor commitment), which the arm-1 status change touches.
  Decide whether arm 2's content is owned by MECH-434, by MECH-080 as its rollout-level instance, or recorded as an explicit edge. The revision block cites MECH-434 so the overlap is visible; no edge was wired.
- **Q5 -- Fold the section-5 design constraints into `what_would_answer`?** That is a falsifier change, so it was not applied. *Recommendation: yes, at the point EXP-0818 is next reviewed for unblocking, not before.*
- **Q7 -- Arm 1: drift (competence, excluded) vs starting-point bias (a set-point).** Huang-Pollock 2017 reports both. Only the second is a MECH-080-type set-point, and no pulled entry separates their contributions to ADHD prematurity. Left open. A targeted lit-pull on ADHD starting-point / prior-bias findings would bear on it.
- **Q6 -- Title.** "(ADHD/anxiety/OCD)" still lists all three as scope. Under the revision one is unassigned and one is contested. *Recommendation: leave the title until Q2 is answered.*

## 8. Red-team (Step 6b)

One independent pass, run on a **different model (Fable)** from the session model (Opus 5.5). It was given the proposal, the five entries, `claims.yaml` and the architecture doc, and returned findings only.

| Item | Verdict | Action taken |
|---|---|---|
| Section 6 in past tense before the apply; GFLAG-0431 already resolved | CONTESTED (sequencing) | Section 6 reworded; new flag raised instead of reopening 0431 |
| Gate (content revision, not demotion or decomposition) | CONFIRMED | -- |
| Arm 2 anxiety -> compulsivity/OCD | CONFIRMED on occupant; CONTESTED on wording | "two independent designs" -> "two designs, one group"; "not a raised bound" -> "not only a static bound"; n and conf added |
| Arm 1 threshold mechanism "withdrawn" | CONTESTED -- the starting-point shift is a second, set-point-like reading, so "withdrawn" picked a side | Changed to **contested**; new Q7 |
| Arm 3 occupant kept, mechanism contested | CONFIRMED | Transdiagnostic caveat added |
| Anxiety unassigned | CONFIRMED | Severed MECH-078 link now recorded |
| One-disorder-per-arm withdrawn | CONFIRMED | -- |
| Ownership: Q4 missed MECH-434 (same paper, same mechanism) and MECH-088 downstream | CONTESTED | Q4 extended |
| Arch-doc table left asserting the old mapping | CONTESTED | Table rows now carry status; note says claims.yaml is the record |
| Decision citation | hygiene | Decision-log line 577 cited |

Net: the red-team caught one over-reach in the applied set (arm 1). It was corrected before the apply. Nothing was left for the user that should have been applied, apart from the arch-doc consistency, which is now applied.
