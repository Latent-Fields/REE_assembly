# Decide-whether-to-build — CPKT-TONIC-EXPLORATION-NOISE-20260618 (MECH-440 / MECH-441)

- **Decision date (UTC):** 2026-06-27T10:53Z
- **Packet:** `evidence/planning/convergence_packets/inbox/2026-06-18_cpkt_tonic_exploration_noise.json` (decision_due 2026-07-02; met early)
- **Session:** decide-build-tonic-noise-cpkt-20260627T1050Z
- **Verdict:** **BUILD BOTH** (MECH-440 + MECH-441) — user decision, per the packet's `hybridize` recommendation.
- **Adjudicator recommendation (overridden):** DEFER-pending-ARC-110.
- **Promotes:** nothing. Both claims stay `candidate / substrate_ceiling / v3_pending`.

## Claims

| Claim | Mechanism | External analog | Biology anchor (lit-pull) |
|---|---|---|---|
| MECH-440 | state-conditioned self-annealing **weight-noise** floor at the E3 selection head (substrate (a)) | NoisyNet (Fortunato 2018) | Aston-Jones & Cohen 2005 (0.78) + **Tervo 2014 (0.82, causal)** |
| MECH-441 | per-candidate self-annealing **E2 model-disagreement** directed curiosity (substrate (b)) | RND (Burda 2018) / Plan2Explore (Sekar 2020) | Daw 2006 (0.72, substrate-existence only — weakest) |

## Gate checks at adjudication

- **Biology-before-formal-definitions: PASSED.** All three anchors exist with substantive summaries under `evidence/literature/targeted_review_connectome_mech_313/` and `_mech_314/`. Tervo 2014 is *causal* (LC-NE→ACC gating of stochastic choice under uncertainty, suppressed when model-based strategy wins) and directly grounds the state-conditioned + self-annealing shape; MECH-313's state-independent framing is biologically under-specified. All three honestly flag that none addresses the REE-side *propagation* question — left to each candidate's falsifier.
- **ARC-106 (biology grounding):** load-bearing-vs-decorative ablation = OFF reproduces the 687 non-propagation, ON propagates. Divergence to log in the ARC-106 ledger: NoisyNet's per-parameter learned sigma is one level of description below biology's systems-level tonic/phasic mode gate — **disclosed, not silent.**

## Material context the build proceeds despite (recorded, not re-litigated)

The **same-day** confirmed cluster autopsy `failure_autopsy_704b-706b-conversion-ceiling_2026-06-27` (applied in REE_assembly master `c95a4fb128`, ~10:19Z — it postdates this packet's framing) re-rooted the committed-action-class conversion ceiling **deeper** than the 687 non-propagation: to the **single-arena collapse → ARC-110 (v4_loop_segregation)**, corroborated by two structurally independent mechanisms (MECH-451 finer-channel 704b + MECH-314 curiosity 706b, both re-derive-braked; MECH-314 brake-LOCKED at 8). This is the packet's own pre-registered `could_be_wrong_if` **#4** (the F-dominance/arena monopoly subsumes the injection-locus fix), now the live twice-corroborated diagnosis. 706b in particular was a *fair* double-gated test where the curiosity channel works but cannot convert because the arena, not the channel, is the bottleneck — which weakens the standalone case for MECH-441.

## Build constraints carried into /implement-substrate + /queue-experiment

1. Both no-op default (flag OFF / sigma_init=0 = bit-identical), per V3-primacy version-layering.
2. The falsifiers **MUST** run on the current SOTA conversion stack — **569i top-k shortlist + MECH-448 `use_f_eligibility_demotion`** — not the un-armed 687 config.
3. Each falsifier **MUST** disambiguate the injection-site / channel-mechanism axis from the single-arena/ARC-110 axis.
4. If a falsifier reproduces the single-arena ceiling (MECH-440 thrash-not-carve; MECH-441 no-conversion), route to `/implement-substrate` on **ARC-110**, NOT a deeper noise/curiosity build. MECH-441 is very likely gated on ARC-110 landing first.
5. Coordinate with — do not duplicate — the empirical 687-successor (GAP-C leg) + the 705/705b/706/706b curiosity-conversion lineage.

## Follow-on

`/implement-substrate` (MECH-440 selection-head weight noise; MECH-441 E2-disagreement curiosity readout) → `/queue-experiment` the corrected 4-arm tonic-noise ablation falsifier(s) on the propagating-noise + demotion substrate, with a `dacc_max_suppression>0` non-vacuity precondition.

## Plan / claim edits applied this session (promotes nothing)

- `claims.yaml`: removed `ceiling_decision: deferred` from MECH-440 + MECH-441; rewrote `ceiling_routing_note` to record BUILD APPROVED + the ARC-110 risk + the build constraints.
- `behavioral_diversity_isolation:GAP-C-build`: status `deferred → in-progress`; owner_exq set to the build-decision routing; `build_decision_2026_06_27` note added; cross_plan_link += `v4_loop_segregation:ARC-110`.
- `behavioral_diversity_isolation:GAP-C`: refreshed stale `owner_exq` + `resume_condition` (603q ran PASS 2026-06-17); `governance_2026_06_27` note.
- `arc_062_rule_apprehension:GAP-H`: H2-leg owner_exq updated to the build decision + ARC-110 context.
- `decision_log.v1.jsonl`: appended MECH-440 + MECH-441 build-decision entries.
