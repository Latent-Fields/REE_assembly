# Failure Autopsy — V3-EXQ-543i (ARC-062 differential-heads falsifier)

- generated_utc: 2026-05-19T01:13:33Z
- scope: single (resolves the V3-EXQ-543i diff-OFF non-reproduction the GAP-B resume_condition flagged)
- status: confirmed (interactive gate answered 2026-05-19)
- supersedes_chain: V3-EXQ-543h -> V3-EXQ-543g
- claim_ids: ARC-062, MECH-309, INV-074, MECH-334 (+ MECH-333, the instrument under test)

## 1. Why this autopsy exists

`arc_062_rule_apprehension_plan.md` GAP-B (status: blocked, 2026-05-18) set the resume
condition: GAP-B stays blocked until (1) the V3-EXQ-543i /failure-autopsy explains the
diff-OFF non-reproduction, then (2) a post-substrate retest returns a contributory
result. This artifact discharges (1).

## 2. Facts — two runs, opposite pre-registered branches

| | `...063711Z` (06:37Z) | `...191052Z` (19:10Z) |
|---|---|---|
| Elapsed | 690 s (~11.5 min) | 12 386 s (~3.4 h) |
| Episode budget | P0=40 + P1=60 + P2=8 x 12 arms x 3 seeds -- impossible in 690 s | full budget executed |
| diff_off_reproduced_collapse | false (diff-OFF arms 0 inert) | true (543g signature reproduced) |
| diff_on_escape | true (all diff-ON 0 inert) | false (all 4 diff-ON arms 3/3 inert) |
| repro_543g_signature | true (vacuously -- nothing trained) | true (valid sanity baseline) |
| interpretation_branch | (c) c_diff_off_collapse_not_reproduced_substrate_drift | (e) e_collapse_survives_structure_MECH309_strong_ARC063_required |
| evidence_direction | non_contributory x4 | mixed: ARC-062 weakens / MECH-309 supports / INV-074, MECH-334 non_contributory |

diff-ON arm detail (19:10Z): ARM_8/9/10/11 all n_inert_gating_seeds = 3/3, mean_abs_rho
0.14-0.38, reef ~0.41-0.45 -- collapsed to inert exactly like the diff-OFF arms.

## 3. Explanation of the diff-OFF non-reproduction (the GAP-B question)

The 06:37Z run is a **truncated-training artifact, not a substrate finding**. The
head_0==head_1 collapse is an attractor reached only under *sustained* full-length P1
outcome-coupled REINFORCE (established by the 543g and 543h autopsies). A ~690 s run
executes a tiny fraction of the 108-episode-per-arm-seed budget, so no arm -- diff-OFF
or diff-ON -- trains into the attractor. Every arm shows 0 inert simply because nothing
trained; `diff_off_reproduced_collapse=false` is therefore *vacuous*, not a sanity-baseline
failure. The experiment's own pre-registered Branch (c) correctly classified this as
substrate/seed drift -> all non_contributory. **The diff-OFF non-reproduction is a
truncated/aborted run, fully explained; it carries no scientific weight and should not
gate GAP-B.**

The full 19:10Z run reproduced the diff-OFF collapse cleanly
(`diff_off_reproduced_collapse=true`, `repro_543g_signature=true`), making it a **valid
single-variable test** and the load-bearing result.

## 4. Scientific result (19:10Z, pre-registered Branch e -- contributory)

The MECH-333 differential-heads fix -- `delta_hat = scale * delta(x) /
(||delta(x)||_K + eps)`, candidate-axis L2 pinned to differential_bias_scale=0.1 so
`delta==0` is a *structural* non-equilibrium with a non-vanishing REINFORCE escape
gradient at w=0.5 -- **does not prevent head collapse under full outcome-coupled
REINFORCE.** Every gated arm (diff-OFF, diff-ON, xtal, non-xtal) collapses to inert
(3/3 seeds, TV < 0.05). The structural inductive bias is insufficient; the
monomodal-collapse equilibrium survives it. This is exactly pre-registered Branch (e):
MECH-309 strong confirmation; ARC-062 weak reading weakened; a genuine distributed
rule-apprehender (ARC-063 / V4) required.

## 5. Biological-reference triage

- Closest reference: PFC rule-cells / mixed-selectivity / corticostriatal rule-gating.
  Lit-pull **present and rich**: `targeted_review_arc_062_rule_apprehension` (8 entries
  -- Miller-Cohen 2001, Rigotti 2013, Mitchell 2016, Bongard 2010, ...). Biology supports
  the **class** of mechanism (rule-conditioned policy gating is real).
- This is **not** a formal-definition-import / biology-divergence failure (not the SD-003
  mode). The architecture is biologically grounded; the lit exists.
- Failure matches a **missing-dependency signature**: real PFC rule-cells acquire
  differentiation from supervised/contextual signals and corticostriatal gating, not from
  a single shared scalar return. The V3 implementation trains two heads + a sigmoid
  discriminator with a byte-identical *shared-return* outcome-coupled REINFORCE loss and
  no per-context advantage / discriminator supervision. Canonical **"symbol of the
  mechanism but not its functional role."** The differential-heads fix tried to
  substitute *structure* for the missing differentiation/context-routing training signal
  and was empirically insufficient.

## 6. Four-layer diagnosis

| Layer | Status | Note |
|---|---|---|
| Claim alignment | ARC-062 weakened at V3 substrate level, NOT architecturally falsified; MECH-309 strengthened but NARROW | collapse is the only evidence; zero positive trained-policy evidence (narrow_supports_flag already set) |
| Biological reference | present; missing-dependency match | shared-return REINFORCE lacks the differentiation/context-routing signal real PFC rule-cells depend on |
| Prerequisites | missing | GAP-C (discriminator->LateralPFC routing) / GAP-D (trainable rule-bias head in E3 optimiser) pre-positioned 2026-05-17 but never wired live |
| Implementation | partial / symbol-not-function | heads+discriminator present, differentiation driver absent; MECH-333 structural fix falsified as sufficient |
| Environment | adequate | diff-OFF collapse reproduced in the full run -> env carries the pressure |
| Measurement | adequate | matched-pair single-variable design + Branch-c logic correctly caught the truncated run |
| Integration | discriminator isolated | no functional consumer of head divergence (GAP-C unvalidated) |
| Scale / budget | resolved | truncated-vs-full training budget *was* the two-run contradiction |

Recommended `epistemic_category`: **substrate_ceiling** for ARC-062 (already set; the
V3 gated-heads-via-shared-REINFORCE substrate cannot carry the head differentiation the
weak reading asserts, even with the structural non-equilibrium fix). MECH-333 (the fix
itself): **falsified as a sufficient remedy** for the collapse -- retained as a
partial/insufficient mechanism, not deleted. MECH-309: strong-but-narrow confirmation
(`narrow_supports_flag` already set). ARC-063/V4 already brought forward 2026-05-18.

## 7. Learning extracted

1. The GAP-B-flagged "diff-OFF non-reproduction" was a truncated/aborted ~690 s run, not
   a substrate signal -- fully explained; it does not gate GAP-B.
2. The full 19:10Z run is a valid single-variable Branch-e result: the MECH-333
   `use_differential_heads` structural non-equilibrium does **not** escape the
   MECH-309 monomodal-collapse equilibrium under full outcome-coupled REINFORCE.
3. Diagnosis is missing-dependency / symbol-not-function, NOT architectural
   falsification of ARC-062 (biology supports the class) and NOT biology-divergence.
4. A single-machine Branch-e is PROVISIONAL by the experiment's own pre-registration and
   governance rule -- the 543g->h->i chain exists *because of* cross-machine bistability
   (ACTIVE host-A / INERT cloud-3+cloud-4).

## 8. Routing (user-confirmed at interactive gate, 2026-05-19)

- **Gate ARC-062 governance on V3-EXQ-543j first.** 543j is already queued (byte-identical
  to 543i, pinned ree-cloud-4, priority 5) explicitly to clear the single-machine caveat.
  branch-e CONFIRMS -> ARC-062 weak-reading demotion + ARC-063/V4 escalation may proceed;
  branch-a CONTRADICTS -> 543i was itself a single-machine basin artifact, do NOT demote,
  escalate to a >=2-machine matrix; branch-c -> drift, non_contributory.
- **MECH-333 recorded as falsified as a sufficient remedy** for the collapse
  (use_differential_heads delta-pinning does not prevent inert collapse under full
  outcome-coupled REINFORCE). Retained as partial/insufficient, not deleted.
- Any ARC-062 substrate_ceiling recommendation stays paired with
  `pending_retest_after_substrate=true` and the existing `narrow_supports_flag`
  (MECH-309 "supports" is single-pathway -- collapse is the only evidence; confirming or
  voiding the cluster is NOT conflict resolution).
- Per-run governance writes: 543i_063711Z -> non_contributory (truncated-run artifact;
  add evidence_direction_note); 543i_191052Z -> mixed, PROVISIONAL pending 543j.

## 9. Draft evidence_quality_note (for /governance to write, NOT written here)

ARC-062 (append): "V3-EXQ-543i (full run 20260518T191052Z, Branch e) confirmed: the
MECH-333 use_differential_heads structural non-equilibrium does NOT escape the
MECH-309 monomodal-collapse equilibrium under full outcome-coupled REINFORCE (all 4
diff-ON gated arms 3/3 inert; diff-OFF reproduced the 543g collapse -> valid
single-variable test). The companion 20260518T063711Z run was a truncated ~690 s
artifact (Branch c, non_contributory) -- the diff-OFF non-reproduction it showed is
explained by truncated training, not a substrate signal (failure_autopsy_V3-EXQ-543i_
2026-05-19). Diagnosis: substrate_ceiling / missing-dependency (no per-context
differentiation signal; GAP-C/GAP-D routing never wired live), NOT architectural
falsification -- biology supports the rule-gating class (targeted_review_arc_062_
rule_apprehension, 8 entries). ARC-062 weak-reading demotion + ARC-063/V4 escalation
GATED on V3-EXQ-543j cross-machine confirmation (ree-cloud-4). narrow_supports_flag
retained; pending_retest_after_substrate retained."

MECH-333 (append): "V3-EXQ-543i (20260518T191052Z) falsifies use_differential_heads as
a *sufficient* remedy for the MECH-309 head-collapse: delta_hat with candidate-axis L2
pinned to differential_bias_scale=0.1 does not prevent inert collapse under full
outcome-coupled REINFORCE (all diff-ON arms 3/3 inert). MECH-333 retained as a
partial/insufficient mechanism; a differentiation/context-routing training signal
(GAP-C/GAP-D) remains the unmet dependency."
