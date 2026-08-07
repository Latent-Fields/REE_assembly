# Thought intake: non-terminal need pressure and minimal launch scaffolds

**Date:** 2026-06-04 (raw); intake written 2026-06-05
**Status:** intake / design hypothesis. NOT an active work item; NOT a change to current
REE-v3 acceptance criteria. Becomes relevant only for future transfer-world / nursery work.
**Raw thought file:** `docs/thoughts/2026-06-04_Non_terminal_need_launch.md`
**Origin:** user observation that a virtual REE organism need not face biological death-
pressure. Failure can be made *meaningful but non-terminal*: a scaffold rescues, logs the
failure, and uses it to shape later autonomy -- "soft enough to prevent fatal collapse, hard
enough to make learning necessary."
**Anchors:** the cue-ecology / weaning intake `thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md`,
`goal_pipeline:GAP-2` (foraging-contact ceiling), `scaffolded_sd054_onboarding`, SD-057 /
MECH-347 (cue recall), SD-012 (homeostatic drive).

---

## 1. Core idea

Replace biological death-pressure with **non-terminal need pressure**. Distinguish four
failure grades for transfer-world launch:
- **terminal failure** -- organism dies / run ends;
- **soft failure** -- organism enters a rescue/scaffold state (restored, but failure logged);
- **developmental failure** -- organism survives but does not earn autonomy promotion;
- **autonomous success** -- organism restores itself without scaffold intervention.

A transfer launch profile should **minimise terminal failure while preserving developmental
failure as a real signal**. The "minimal launch kit" lists the bootstrapping primitives a new
ecology must supply (body-need/depletion, restoration, harm, contact-consequence,
cue-to-restoration token, cue-to-harm token, orient/survey primitive, protected consolidation
window, non-terminal rescue state).

## 2. What is new vs what REE already has

| Element | Already in REE? | Verdict |
|---|---|---|
| Nursery scaffolding, protected consolidation, forced feeding (Stage-0/0b) | **Yes** -- `scaffolded_sd054_onboarding`, goal-pipeline stages | Confirms the substrate exists |
| Weaning arc (feeding -> consolidation -> token -> cue recall -> contact -> autonomous) | **Yes** -- the cue-ecology intake names exactly this closure path | Confirms; this thought explicitly says it does NOT change that path |
| Cue-to-restoration / cue-to-harm tokens, orient/survey primitive | **Partial** -- incentive-token bank (SD-057), orient/survey is itself an orphan thought (`2026-06-04_Orienting_surveying_drive.md`) | Cross-link |
| **Graded non-terminal failure taxonomy** (terminal / soft / developmental / autonomous) as an explicit launch-profile criterion | **No** | **NOVEL** -- the contribution |
| **Forgiveness-vs-drive balance** as a design risk (too soft -> no drive forms) | **Implicit** in drive work (SD-012) but not stated as a launch-tuning constraint | **Extension** |
| Portable "minimal launch kit" of primitives for transfer to non-grid ecologies | **No** | **NOVEL** -- forward-looking (V4+ transfer), not V3 |

**Verdict: the failure-grade taxonomy and the minimal-launch-kit are genuinely new framing;
everything they sit on already exists.** The thought is correctly self-scoped as future
transfer-world design, not current V3 work.

## 3. Candidate claims / artifacts

**REGISTERED 2026-06-10 as Q-071 (`transfer.non_terminal_failure_profile`) -- confirmed 2026-08-07.**
The line below reading "None registered this pass" was true when written and is now stale: the
four-grade failure taxonomy was picked up as node DRV-* of
`evidence/planning/drives_motivation_v4_plan.md` and registered as **Q-071**
(`claim_type: design_decision`, `status: candidate`, `epistemic_category: substrate_conditional`,
`implementation_phase: v4`, `v3_pending: true`, depends_on SD-012 + SD-054, "DO NOT build in V3").
Q-071's own notes fold in the third bullet ("carries the open forgiveness-vs-drive tradeoff
question"), so the Candidate Q below has a home too. The second bullet
(`nursery.non_terminal_rescue_state`) is deliberately NOT separately minted -- it is the
`scaffolded_sd054_onboarding` substrate already named in section 4, and Q-071 depends on SD-054
directly rather than duplicating it.

- **Candidate design criterion** (transfer.non_terminal_failure_profile) -- a launch profile
  is evaluated on the four-grade taxonomy: minimise terminal, preserve developmental as
  signal. *[design-decision class; V4/transfer scope]*
- **Candidate SD/ARC** (nursery.non_terminal_rescue_state) -- a rescue/scaffold state that
  restores viability while logging failure and gating autonomy promotion. *[partly exists in
  onboarding scaffold; would formalise the "logs failure + blocks promotion" semantics]*
- **Candidate Q** (development.forgiveness_drive_tradeoff) -- how forgiving can the world be
  before depletion stops producing meaningful drive? *[empirical, transfer-world]*

None registered this pass -- this is a forward-design note, off the V3 critical path.

## 4. Affected existing claims / docs

- `scaffolded_sd054_onboarding`, goal-pipeline plan (`evidence/planning/goal_pipeline_plan.md`),
  SD-057 / MECH-347, SD-012.
- Sibling orphan `2026-06-04_Orienting_surveying_drive.md` (supplies the orient/survey
  primitive listed in the launch kit) -- and the cue-ecology intake's section 8
  ("safe weaning as its own layer"), which is the same family of concern.

## 5. Next steps (gated -- explicitly future)

1. **Containment, not build.** Per memory `feedback_ree_assembly_externalised_cognition`, keep
   V4/transfer ideas off the V3 critical path. No substrate work now.
2. Revisit when transfer-world / new-ecology work is actually scheduled; at that point the
   four-grade taxonomy becomes the acceptance scaffold for a launch profile.
3. Bundle with the orient/survey and safe-weaning notes as the "transfer/weaning design" group.

## 6. Cross-references

- Raw: `docs/thoughts/2026-06-04_Non_terminal_need_launch.md`.
- Siblings: `docs/thoughts/2026-06-04_Orienting_surveying_drive.md`,
  `thought_intake_2026-06-04_cue_ecology_weaning_nursery_to_forager.md` (esp. section 8).
- Claims/substrate: `scaffolded_sd054_onboarding`, SD-057, MECH-347, SD-012,
  `goal_pipeline:GAP-2`.
