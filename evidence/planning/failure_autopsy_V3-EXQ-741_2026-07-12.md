# Failure Autopsy — V3-EXQ-741 (MECH-095 agency-comparator VALID test-bed on SD-047)

- **Generated:** 2026-07-12T09:34:33Z
- **Scope:** single
- **Status:** confirmed
- **Run:** `v3_exq_741_mech095_agency_comparator_testbed_sd047_20260711T234706Z_v3`
- **Queue:** V3-EXQ-741
- **Claim:** MECH-095 (`tpj.agency_detection_comparator`; candidate / substrate_ceiling / pending_retest_after_substrate)
- **Invoked:** inline from the /governance cycle IGW-20260712-001 (Step 1.5c route A), under the governance session claim.

## 1. Facts (no interpretation)

The SD-047 agency-comparator test-bed (built by `/implement-substrate agency_comparator_testbed_sd047`,
the substrate the re-derive brake demanded after 047m) **ran validly**: `non_degenerate: True`, all four
intensity arms (ARM_0 OFF / ARM_1 0.25x / ARM_2 1.0x / ARM_3 4.0x) passed BOTH guards the 047-lineage
lacked — the probe-partition floor (`n_no_contact >= 5`) and the self/world-balance floor
(`min(n_self,n_world) >= 5`). `valid_arms = [ARM_0, ARM_1, ARM_2, ARM_3]`. The 047l/047m
measurement-degeneracy is fixed.

Result on the valid test-bed (4 seeds/arm):

- `best_improvement = 0.028` (below the 0.04 discrimination floor — no arm discriminates)
- `mean_valid_improvement_A = -0.114` — ROUTED_A (gradient BCE head reshaping z_world) **HURTS** recall
- `mean_valid_improvement_B = +0.003` — ROUTED_B (query-time efference-copy read-out) **neutral**
- `baseline_carries_contact = True` — baseline recall already 0.75–0.93 across arms
- `b_beats_a = True`
- Script self-route: `evidence_direction = weakens`, `decision = woo_spelke_route_substrate_conditional_v4_1`.

**Failed criterion:** discrimination (no arm shows routing improvement > 0.04). Absolute/negative-control
(baseline competence, probe validity) all pass — the substrate-ceiling fingerprint.

## 2. Claim layer

MECH-095 = TPJ agency-detection comparator distinguishing self-caused from other-/world-caused change.
`claim_type: MECH`, status candidate, `epistemic_category: substrate_ceiling`,
`pending_retest_after_substrate: True`, `implementation_phase: v3` (see §7 — this is now a confirmed
misclassification). Prior positive evidence is **narrow**: the only MECH-095 PASS is V3-EXQ-047k, a single
thin-env operationalisation. 047l and 047m were both `non_contributory / measurement_degeneracy`
(n_ceiling_hits stayed 0). So the claim's support is single-pathway; this autopsy does not create illusory
conflict resolution — it is recorded against a claim whose positive base is thin.

**Did the test let the claim express itself?** No. See §4.

## 3. Biological reference

- **Closest mechanism:** temporoparietal junction (TPJ) agency-detection comparator — self- vs
  other-generated event attribution. Lit grounding already strong (~0.907; not a pure formal import).
- **Load-bearing regime:** in brains the comparator matters for **other-agent** attribution (social
  cognition / ToM), i.e. when there is a *structurally-distinct OTHER* whose actions must be separated from
  self-action and from passive environment.
- **Divergence (secondary learning):** the 047-lineage operationalises the comparator as an auxiliary
  gradient BCE head reshaping z_world (ROUTED_A) — which HURTS. MECH-095's own notes describe a
  query-time **read-out** (efference-copy-predicted vs observed z_self), which is ROUTED_B — merely
  neutral, never harmful. The read-out is the biology-faithful translation; the gradient head is plausibly
  the wrong one. This is a carry-forward operationalisation learning, not evidence the distinction is wrong.

## 4. Four-layer diagnosis

| Layer | Status | Notes |
|---|---|---|
| Claim alignment | unclear | test could not let the claim express — no structurally-distinct OTHER present |
| Biological reference | clear | TPJ; failure matches the missing-dependency (no OTHER agent) signature exactly |
| Prerequisites / dependency | missing | the "structurally-distinct OTHER" (multi_agent_ecology MAE-1/MAE-2) is absent |
| Implementation completeness | partial | ROUTED_A gradient head plausibly wrong translation; ROUTED_B read-out is the faithful one |
| Environment adequacy | wrong pressures | SD-047 multi-source dynamics (drift/weather) are NOT an other agent; baseline pre-empts the comparator |
| Measurement adequacy | adequate | valid this time — probe-partition + self/world-balance guards all pass (test-bed rebuild worked) |
| Integration / scale | n/a | — |

**Dominant diagnosis → `epistemic_category: substrate_ceiling`.** Environment adequacy (missing
structurally-distinct OTHER) is the load-bearing layer. This is the **1st VALID ceiling hit** for MECH-095
(the test-bed now validly exercises the comparator; the ceiling is real, not a measurement artifact).
n_ceiling_hits 0 → 1.

## 5. Learning extracted

1. The V3 single-agent substrate — even SD-047's rich multi-source dynamics — cannot make an agency
   comparator load-bearing, because "world-caused" drift is not a structurally-distinct OTHER and the
   baseline representation already carries contact recall. This is the **empirical confirmation** of
   `multi_agent_ecology_v5:MAE-3`'s standing hypothesis (its `blocking_on` / `completion_note` already
   predicted exactly this from the EXQ-121 V3 failure).
2. The read-out operationalisation (ROUTED_B) is the biology-faithful translation; the gradient-BCE-head
   (ROUTED_A) is not (it actively harms). Carry the read-out framing into the eventual MAE-3 retest.
3. The test-bed rebuild the re-derive brake demanded (agency_comparator_testbed_sd047) **worked** — the
   degeneracy that killed 047l/047m is gone. The brake's producer→consumer loop functioned as designed.

## 6. Re-derive brake

**FIRED** — this is the 3rd `non_contributory` reading on MECH-095 (047l, 047m, now 741; threshold 2).
BUT the brake's prior demand was *honored*: the test-bed was rebuilt as ordered and 741 validly ran on it.
So the brake does not re-block a re-test of the same design — it **re-points** the ceiling from the (now
built + validly exercised) test-bed to the **multi-agent ecology** (MAE-1 → MAE-2 → MAE-3).
`refused_requeue: True` — REFUSE a 4th single-agent SD-047 letter (047n). The only sanctioned next
experiment is the MECH-095 retest queued against a **built multi-agent substrate** (MAE-3).

## 7. Routing + recommended governance writes

- **evidence_direction:** `non_contributory` (NOT the script's self-routed `weakens`). The valid test-bed
  confirms the env lacks the pressure the comparator handles; the result is informative (confirms the
  substrate dependency) but does not weigh against the claim's correctness.
- **epistemic_category:** `substrate_ceiling` (retained; 1st valid ceiling hit).
- **pending_retest_after_substrate:** `True`, re-pointed from `agency_comparator_testbed_sd047` (done) to
  `multi_agent_ecology_v5:MAE-3`.
- **implementation_phase reassignment v3 → v5 (user-confirmed).** 741 turns MAE-3's *architectural*
  v4→v5 reassignment flag into an *empirically grounded* one. Under phase-follows-dependency, MECH-095's
  functional demonstration genuinely depends on a V5 substrate (the multi-agent ecology), so
  implementation_phase v3 is a confirmed misclassification. Governance sets `implementation_phase: v5` and
  binds the ceiling to `multi_agent_ecology_v5:MAE-3`. This removes MECH-095 from V3-completion accounting.
- **substrate_queue:** `amend` `agency_comparator_testbed_sd047` with the 741 failure_record (records the
  valid exercise + the ceiling confirmation). No NEW substrate_queue SD entry is minted — the enabling
  substrate is the already-tracked closure-plan node `multi_agent_ecology_v5:MAE-3`, not a bare build task.
- **No fanout, no lit-pull, no demotion.** Single unambiguous route (the multi-agent ecology). Lit already
  strong. Not falsified (highest threshold not reached — the test could not express the claim).

### Draft `evidence_quality_note` (governance writes verbatim or as revised)

> 2026-07-12 (V3-EXQ-741, /governance IGW-20260712-001 inline autopsy): the SD-047 agency-comparator
> test-bed (agency_comparator_testbed_sd047) ran VALIDLY for the first time (non_degenerate:True; all 4
> intensity arms pass the probe-partition + self/world-balance guards the 047l/047m lineage lacked). On
> the valid test-bed the comparator does no functional work: no arm discriminates (best routing
> improvement +0.028 < 0.04 floor), ROUTED_A gradient-head HURTS recall (mean -0.114), ROUTED_B
> efference-copy read-out neutral (+0.003), baseline already carries contact recall (0.75-0.93).
> evidence_direction non_contributory (NOT weakens): SD-047's "world-caused" drift is not a
> structurally-distinct OTHER, so the env cannot make the comparator load-bearing and the baseline
> pre-empts it — the test could not let the claim express its value. This EMPIRICALLY CONFIRMS
> multi_agent_ecology_v5:MAE-3's standing prediction (MECH-095 is intrinsically relational; needs a
> genuine second agent). 1st VALID substrate_ceiling hit (n_ceiling_hits 0->1; 047l/047m were
> measurement-degeneracy, uncounted). Re-derive brake FIRED (3rd non_contributory) but its test-bed-rebuild
> demand was honored; it re-points the ceiling from the (done) test-bed to the multi-agent ecology and
> REFUSES a 4th single-agent SD-047 letter. Secondary learning: the read-out framing (ROUTED_B) is the
> biology-faithful translation; the gradient-BCE-head (ROUTED_A) is not. Positive base is narrow (only
> 047k). implementation_phase reassigned v3 -> v5 (phase-follows-dependency; the multi-agent ecology is the
> enabling substrate). pending_retest_after_substrate stays true, re-pointed to multi_agent_ecology_v5:MAE-3.
> PROMOTES/DEMOTES NOTHING (stays candidate / substrate_ceiling / pending_retest).
