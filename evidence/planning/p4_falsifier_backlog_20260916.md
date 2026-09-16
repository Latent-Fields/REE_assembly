# P4 falsifier-authoring backlog (queuefloor g10, paced governance item)

Date: 2026-09-16. Session: `bold-swanson-1789a0` (chip `chip-20260916-p4-falsifier-authoring-tranche1`).
Plan of record: `queuefloor_recurrence_rootcause_staged_20260915.md` section 3, proposal P4
("commission a falsifier-authoring pass on the ~60 claims with no `what_would_answer`"),
APPROVED by the user 2026-09-16 as a PACED item: first tranche of 15 now, the rest as a paced
backlog reviewed at each `/governance` cycle. This document is that backlog.

## What landed in tranche 1

REE_assembly `35ac348a3b` (on `origin/master`): `what_would_answer` authored on 15 claims,
narrow edit (90 insertions, one file). Each field carries NON-DEGENERACY PRECONDITION /
CONFIRMING / FALSIFYING / SUBSTRATE (named `ree_core` module, or an explicit "not built" with
the build named) / Disposition, following the thought-digestion house form.
Governance flag: **GFLAG-0298** (`promotion_review`, REE_assembly `40537bf056`).

| rank | claim | status | disposition written into the field |
|---|---|---|---|
| 1 | MECH-005 | provisional | testable now; 1018 design + the seven successor changes in `exq1026_mech005_nu_path_authority_refusal_20260911.md`; fresh EXQ number |
| 2 | MECH-021 | provisional | testable now (theta_buffer_size / rollout_horizon pair; anticipatory-restraint fraction) |
| 3 | MECH-023 | provisional | testable now (matched-state ranking divergence with equal-mass-elsewhere control) |
| 4 | MECH-024 | provisional | testable now but expensive (3x3 cross-lesion coupling matrix); queue after MECH-023 |
| 5 | MECH-028 | provisional | testable now (intact / mode-locked / reset-on-switch) |
| 6 | MECH-034 | provisional | testable now under the MECH-284 staleness reading of "viability"; substrate caveat stated |
| 7 | MECH-067 | provisional | complex (probe-gated): write-audit spike first; the permission matrix itself is unbuilt (substrate_conditional for the comparator arm) |
| 8 | INV-022 | candidate | testable now once SD-063 head clears R2 >= 0.2 precondition and the graded precision consumer is verified live |
| 9 | INV-023 | candidate | testable now for the precision half on the V3-EXQ-541c (MECH-204) instrument; residue half inherits MECH-018's gap |
| 10 | INV-024 | candidate | testable now and cheap (hash ledger around one sleep cycle + commit-lineage audit) |
| 11 | INV-069 | candidate | testable now under the per-stream V_s proxy; substrate_conditional for the full V(t) reading (ARC-053 unbuilt) |
| 12 | MECH-017 | candidate | testable now (budget-matched offline vs online consolidation); shares instrument with MECH-423 / V3-EXQ-680 lineage |
| 13 | MECH-018 | candidate | substrate_conditional: `ResidueField.integrate` exists but is not called from `SleepLoopManager._run_cycle` |
| 14 | MECH-038 | candidate | substrate_conditional: no multi-agent env, no signalling affordance, no AF-analog routing; research-direction decision first |
| 15 | MECH-042 | candidate | testable now and cheap; sub-claim (1) is contract-test shaped, sub-claim (2) is the experiment |

Dispositions that need a governance apply: `epistemic_category: substrate_conditional` on
MECH-018 and MECH-038 (and, for the comparator arm only, MECH-067); nothing was regenerated
(`claims.json` is stale until the next `/governance` cycle rebuilds it).

## How the population was derived (and one correction to the chip's STOP-CHECK)

Population = eligible experimental proposals (`status == proposed`,
`proposal_type == experimental`, passing `scripts/proposal_routine_tick.py`'s own
`_eligibility()` -- queue-gate, v3-testable, FILTER D/C, already-run, FILTER B) whose claim has
no non-empty `what_would_answer`. Computed by importing the minter, not re-implementing it.
Result on 2026-09-16 (post-governance `db6d20ebee0`): 184 proposed experimental, 75 eligible,
**59** claims with no falsifier (48 `mechanism_hypothesis`), matching the plan doc's 60/74.

**The chip's STOP-CHECK snippet is vacuous as written**: it reads `p.get("claim_ids") or
p.get("primary_claim_ids")`, but every eligible proposal carries the singular key `claim_id`, so
the snippet always prints `0` missing and its "STOP if under 20" fires spuriously (it did, in
this session). The tranche-2 chip carries the same check with `claim_id` substituted and a
dict-valued `what_would_answer` tolerated. Nothing else in the check was changed.

**Ranking** (per the brief): proposal priority, then number of proposals citing the claim, then
claim status (active > provisional > candidate), then proposal id. Every eligible proposal is
`medium` with exactly one proposal per claim, so the rank reduces to status then proposal id --
which is the minter's own drain order within each status band. Chip state (`chip-proposal-exp-*`
done / withdrawn) was recorded but NOT used as a key: EXP ids are renumbered on regen
(`chip-20260903-proposal-tick-unstable-expid`), so the chip that "consumed" a proposal id
frequently belongs to a different claim.

## Ranked remainder (ranks 16-59): the paced backlog

One line each on why it is hard, so the next tranche can be ordered by value rather than by
proposal id if governance prefers. **Suggested reorder for tranche 2** (cheap and substrate-live
first): SD-086, MECH-468 + MECH-469 (one instrument), MECH-064 + MECH-066 (share tranche 1's
write-audit spike), MECH-237, MECH-221, MECH-115, MECH-136, MECH-467, MECH-049, MECH-050, SD-070,
SD-081, MECH-078 + MECH-233. Governance should also consider **re-typing SD-088 / SD-089 / SD-090**
out of the experimental proposal pool (they are registry-tooling design decisions, not V3
experiments) and **re-typing MECH-170** as a clinical-literature claim.

| rank | claim | status / type | why it is hard |
|---|---|---|---|
| 16 | MECH-049 | candidate / mechanism_hypothesis | Phase compartmentalisation: needs a "collapse the phases" lesion (proposal / evaluation / veto / update in one gradient) against the heartbeat-separated default; readout = ethical-constraint independence (veto rate unchanged under reward-gradient pressure). Buildable, design-heavy. |
| 17 | MECH-050 | candidate / mechanism_hypothesis | Functional locality without anatomical columns: abstract structural claim; needs an attribution-locality readout on `entities/object_file_buffer.py`; the "without columns" clause is unfalsifiable as stated -- narrow to "locality suffices". |
| 18 | MECH-064 | candidate / mechanism_hypothesis | Typed store separation blocks exteroceptive writes into POL / ID stores: same write-audit instrument as INV-024 / MECH-067 (tranche 1); author after that spike runs so the DV is grounded in what the audit actually observes. |
| 19 | MECH-066 | candidate / mechanism_hypothesis | Shared representations, separated durable writes: same audit family as MECH-064; the "bounded coupling" clause needs a coupling measure (read-only reuse allowed) the audit does not yet record. |
| 20 | MECH-078 | candidate / mechanism_hypothesis | BLA bootstraps valence for unmapped territory: `amygdala/bla.py` exists; needs an "unmapped territory" definition on the hippocampal map and an over-valencing knob; keep the anxiety-disorder clause OUT of the falsifier (clinical analogy, no DV). |
| 21 | MECH-079 | candidate / mechanism_hypothesis | Selfhood as artefact of stable map geometry: overlaps INV-069 (tranche 1); needs a map-geometry perturbation that leaves the self process intact, to dissociate from INV-069's process reading. |
| 22 | MECH-080 | candidate / mechanism_hypothesis | Rollout truncation set-points as psychiatric differences: `rollout_horizon` is a live knob, but the psychiatric mapping (ADHD / anxiety / OCD) has no V3 DV; narrow to behavioural signatures (impulsivity / avoidance / perseveration proxies). |
| 23 | MECH-082 | candidate / mechanism_hypothesis | Map distortion biases E1 sampling via E2 without E1 retraining: E1 has no attentional-sampling channel to read; substrate-thin. |
| 24 | MECH-084 | candidate / mechanism_hypothesis | NA as attentional snap / E1-E2 sampling-ratio modulator: depends on MECH-005 (tranche 1) resolving first; the E1/E2 sampling ratio is not a live knob. |
| 25 | MECH-109 | candidate / mechanism_hypothesis | Respiratory handle on the E3 clock: no respiratory channel in V3; substrate absent -- substrate_conditional at best, or re-type as physiology literature. |
| 26 | MECH-110 | candidate / mechanism_hypothesis | Laughter as hypothesis-tag cycling: no incongruity-plus-resolution stimulus structure; behavioural-human claim with no V3 analog. |
| 27 | MECH-115 | candidate / mechanism_hypothesis | Tag reliability degrades with z_self dispersion: testable -- MECH-094 leak rate (simulated content reaching residue) vs z_self D_eff; pairs with INV-024's audit; needs a dispersion manipulation. |
| 28 | MECH-131 | candidate / mechanism_hypothesis | vmPFC-analog activates aversive residue anticipatorily: no vmPFC analog in `ree_core/pfc/` (OFC, lateral, frontopolar, infralimbic exist); ARC-035 substrate unbuilt -- four claims (131-134) share one build. |
| 29 | MECH-132 | candidate / mechanism_hypothesis | vmPFC-analog activates social / identity constraints as live gates: same ARC-035 gap, plus no social constraint store. |
| 30 | MECH-133 | candidate / mechanism_hypothesis | vmPFC-analog safety memories compete with threat attractors: `safety/conditioned_safety_store.py` exists but the vmPFC activation path does not; ARC-035 gap. |
| 31 | MECH-134 | candidate / mechanism_hypothesis | vmPFC-analog goal approach pull distinct from goal representation: ARC-035 gap; the G-represented-but-not-pulled dissociation needs a goal-pull readout (MECH-112). |
| 32 | MECH-136 | candidate / mechanism_hypothesis | E3 agency-gain correction for E2's attenuation of agent-caused PE: testable on the SD-003 pipeline, but the precondition (E2 attenuation actually present and measured) can dominate the criterion -- design carefully. |
| 33 | MECH-159 | candidate / mechanism_hypothesis | Intergenerational moral progress: multi-generation multi-agent lives; no substrate; far. |
| 34 | MECH-167 | candidate / mechanism_hypothesis | z_harm_a and drive_level share one motif: a dynamics-matching test is cheap but risks vacuity (both are leaky integrators by construction) -- the falsifier must name a divergence that is NOT true by construction. |
| 35 | MECH-170 | candidate / mechanism_hypothesis | Sleep restoration in early MCI: clinical prediction with no V3 analog of MCI; re-type as clinical-literature claim rather than author a V3 falsifier. |
| 36 | MECH-190 | candidate / mechanism_hypothesis | Cooperative predator defence without language: same multi-agent-environment gap as MECH-038 (tranche 1); substrate_conditional on the same research-direction decision. |
| 37 | MECH-208 | candidate / mechanism_hypothesis | Valence-asymmetric replay drives approach / avoidance bias: MECH-285 sampler exists but replay is staleness-weighted, not valence-weighted; needs a harm-salience replay weight; inherits sleep GAP-2's behavioural-diversity block. |
| 38 | MECH-211 | candidate / mechanism | Title is a slug (`schema_consolidation_as_search_grammar`) with no claim text; needs a statement before a falsifier; in the sleep plan's scope_claims. |
| 39 | MECH-221 | candidate / mechanism_hypothesis | Continuous z_world residualisation against z_self predictions: testable if the substrate does NOT already do it every tick -- check `latent/stack.py` first; then a per-tick vs query-time-only pair. |
| 40 | MECH-223 | candidate / mechanism_hypothesis | Animated-agency over-attribution needs calibration: needs animate / moving entities with non-agentive causes in the environment; substrate-thin. |
| 41 | MECH-227 | candidate / mechanism_hypothesis | Anaesthesia as D_V collapse: depends on ARC-053 TCL (unbuilt, as INV-069's field records); clinical; substrate_conditional. |
| 42 | MECH-233 | candidate / mechanism_hypothesis | Asymmetric valence pathways into hippocampal terrain: BLA exists; needs the approach pathway's write path identified; pair with MECH-078. |
| 43 | MECH-237 | candidate / mechanism_hypothesis | z_goal attractor globally reachable: cheap basin-of-attraction sweep from random latent starts (`hippocampal/ghost_goal_bank.py`, SD-012); precondition = an attractor exists at all. Good tranche-2 candidate. |
| 44 | MECH-239 | candidate / mechanism_hypothesis | Time cells tiling elapsed time in the hippocampal index: no temporal-cell substrate (anchor relations are typed but not time-tiled); substrate_conditional. |
| 45 | MECH-246 | candidate / mechanism_hypothesis | Pareidolia from degraded input: needs a noisy-input arm and a false-structure DV on E1; keep to false-positive structure detection, not "psychosis". |
| 46 | MECH-247 | candidate / mechanism_hypothesis | Hypervigilant priors produce psychotic-like symptoms: blocked on the same gap that refused the MECH-027 probe (V3-EXQ-979: precision channel had no graded runtime consumer). |
| 47 | MECH-249 | candidate / mechanism_hypothesis | ACh / NA balance as a continuous write-profile variable: no ACh variable in V3; substrate_conditional. |
| 48 | MECH-328 | candidate / mechanism_hypothesis | Synthetic and real z_goal on one manifold for play-to-real transfer: play mode is unimplemented in V3 (memory `project_playmode_cluster_substrate_blocked`); substrate-blocked. |
| 49 | MECH-468 | candidate / mechanism_hypothesis (standard) | Anchor topology carries information beyond payloads: typed relations exist in `hippocampal/anchor_set.py`; a topology-scramble ablation with payloads fixed is a clean design. Good tranche-2 candidate. |
| 50 | MECH-469 | candidate / mechanism_hypothesis (standard) | Relation types not collapsible to one adjacency: same instrument as MECH-468 (collapse-types vs scramble arms); author the two together. |
| 51 | SD-070 | candidate / design_decision (standard) | z_world P0 anti-collapse recipe: built and in use (`latent/zworld_p0.py`); check the 978 -> 1040 lineage for existing collapse-metric evidence before authoring -- may already be answered. |
| 52 | SD-081 | candidate / design_decision | Dual-system uncertainty arbitration: the falsifier is a build-verification plus a behavioural arbitration readout; check whether `e3.dualsystem_uncertainty_arbitration` landed (MECH-477 lineage) first. |
| 53 | SD-086 | candidate / design_decision | z_harm_a readout must be a calibrated scalar not the latent norm: cheap -- correlation of norm vs calibrated valuation with realised harm on `affect/harm_suffering_accumulator.py`. Good tranche-2 lead. |
| 54 | SD-088 | candidate / design_decision | Claims-index source-dependence between supports: a registry-tooling decision, not a V3 experiment -- should leave the experimental proposal pool (FILTER C / proposal_type). |
| 55 | SD-089 | candidate / design_decision | Claim-origin provenance classes: registry tooling, same as SD-088. |
| 56 | SD-090 | candidate / design_decision | Mechanism functional-role classification: registry tooling, same as SD-088. |
| 57 | MECH-467 | candidate / mechanism_hypothesis (standard) | Three dissociable distractor-resistance failure modes: SD-033a / MECH-262 lateral-PFC substrate exists; a three-way dissociation design is heavy but buildable. |
| 58 | MECH-137 | candidate / mechanism_hypothesis | Commit token with two temporal registers: no commit-token object in `ree_core` (`preservation/token.py` is unrelated); substrate_conditional on MECH-061's token. |
| 59 | MECH-139 | candidate / mechanism_hypothesis | Commitment as a multi-second pre-movement trajectory: needs multi-step actions -- MECH-057a already records that single-step atomic grid actions give no "action in progress" state; substrate-blocked on the same gap. |

## Pacing

Tranche 2 is chipped (`chip-20260916-p4-falsifier-authoring-tranche2`, kind `work`, headless
origin) and takes the next 15 by the rank above unless governance reorders it per the suggestion.
Each tranche re-derives the population with the corrected check, skips ids that already carry a
field, and lands one governance flag. Expected remaining tranches after this one: three.
