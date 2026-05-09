# Targeted lit-pull synthesis: ARC-062 / MECH-309 / ARC-063 — rule-apprehension layer

**Pulled** 2026-05-09 (8 entries).
**Target claims** MECH-309 (monomodal collapse without rule-apprehension), ARC-062 (weak reading, V3 architectural slot), ARC-063 (strong reading, V4 deferred).
**Author** lit-pull session `lit-pull-arc062-rule-apprehension-2026-05-09T1904Z`.
**Plan-of-record** to be drafted from this synthesis: `evidence/planning/arc_062_rule_apprehension_plan.md`.

---

## Verdict 1 — R1 (discriminator input streams)

**Default flipped to multi-stream.** ARC-062's discriminator should read `z_world + z_self + z_harm_a` rather than `z_world` alone. Three converging anchors:

| Source | What it shows | R1 implication |
|---|---|---|
| Miller & Cohen 2001 ([DOI 10.1146/annurev.neuro.24.1.167](https://doi.org/10.1146/annurev.neuro.24.1.167)) | PFC bias signals "establish the proper mappings between **inputs, internal states, and outputs**" — explicit multi-stream commitment | Foundational endorsement of multi-stream integration |
| Rigotti et al. 2013 ([DOI 10.1038/nature12160](https://doi.org/10.1038/nature12160)) | PFC neurons exhibit **mixed selectivity** to multiple task variables in single-cell representations; mixture is the rule, not the exception | Single-cell-level evidence for multi-stream integration |
| Mitchell et al. 2016 ([DOI 10.1523/JNEUROSCI.0810-16.2016](https://doi.org/10.1523/JNEUROSCI.0810-16.2016)) | Macaque MD network includes an **insular cluster** as a first-class member, not as an afterthought | Anatomical anchor: interoceptive integration site is part of the rule-context substrate |

**Architectural commitment for the plan-doc:** R1 default = `(z_world, z_self, z_harm_a)`. Single-stream `z_world` only is the impoverished case and should be the FAIL-route in the Phase 2 experiment, not the default. Phase 2 acceptance can include an input-ablation arm: ARM_1a (`z_world` only) vs ARM_1b (`z_world + z_self`) vs ARM_1c (full three-stream) — predicted ARM_1c clears the falsifier most cleanly; ARM_1a may collapse to ARM_0 baseline.

---

## Verdict 2 — R3 (gating site)

**No single primary site; default to score_bias level (option iii) for engineering reasons; recognise distributed-multi-site as the V3 end-state target.** Three sites all exist biologically; the architectural commitment is a routing choice, not a metaphysical one.

| Site | Anchor | Strength |
|---|---|---|
| (i) Score-aggregation level (BG-side gate on candidate scoring) | Gurney/Humphries/Redgrave 2015 ([DOI 10.1371/journal.pbio.1002034](https://doi.org/10.1371/journal.pbio.1002034)) — cortico-striatal synapse as action-reinforcement interface; D1/D2 cooperative-then-competitive dynamics | Strong; mechanism well-grounded |
| (ii) Trajectory-proposal level (hippocampal preplay biasing which futures get generated) | Pfeiffer & Foster 2013 ([DOI 10.1038/nature12112](https://doi.org/10.1038/nature12112)) — goal-biased forward sequence in rat CA1 before navigation | Strong; the architectural commitment ARC-063 strong reading bakes in |
| (iii) Score_bias level (PFC top-down per-candidate additive bias) | Miller & Cohen 2001; Bongard & Nieder 2010 ([DOI 10.1073/pnas.0909180107](https://doi.org/10.1073/pnas.0909180107)) — PFC rule-coding units controlling information flow between input/memory/output layers | Strong; current SD-033a substrate |
| Distributed multi-site (all three in parallel) | Mitchell 2016 (anatomical), Erez & Duncan 2015 ([DOI 10.1523/JNEUROSCI.1134-15.2015](https://doi.org/10.1523/JNEUROSCI.1134-15.2015)) (functional task-driven), Capkova/Mansouri 2025 ([DOI 10.1523/ENEURO.0117-25.2025](https://doi.org/10.1523/ENEURO.0117-25.2025)) (lesion dissociation) | The biologically faithful answer |

**Architectural commitment for the plan-doc:** R3 Phase 1 default = option (iii) score_bias level, consuming the existing SD-033a substrate. Engineering reasons dominate: SD-033a's `lateral_pfc_analog.compute_bias()` is wired, the `rule_state` buffer exists, the gradient path through E3 score-aggregation is clean. The biology supports option (iii) as a real site (Miller-Cohen, Bongard-Nieder) without prescribing it as primary. Phase 4 / GAP-E is the place where multi-strategy scaling and substrate enrichment surface whether option (i) or (ii) routing is needed in addition.

**Falsification chain:**
- ARC-062 PASS at option (iii) → Phase 3 closure of GAP-1 in `commitment_closure_plan.md`; GAP-E becomes the next-thing-to-try when generalisation breaks.
- ARC-062 FAIL at option (iii) → route discriminator output to option (i) BG-side first (cheaper to retry than (ii)), then option (ii) trajectory-proposal, then ARC-063 strong reading.

---

## Verdict 3 — R2 (discrete heads vs continuous gating)

**Substrate-constrained at Phase 1; biology pulls toward continuous mixed selectivity at scale.** The SD-054 reef-vs-forage substrate is a 2-mode partition by experimental construction, so 2 discrete heads is the right Phase 1 commitment regardless of biology. The R2 caveat is a Phase 4 / V4 flag, not a Phase 1 blocker.

Rigotti et al. 2013 establish that PFC's biological mechanism is high-dimensional mixed selectivity, not discrete head selection. ARC-062 weak reading's two-head + soft-discriminator architecture is a *low-dimensional approximation* of this. At SD-054's two-mode scale the approximation is harmless; at multi-strategy scaling (Phase 4 / GAP-E in the cluster plan) the approximation is expected to break, at which point ARC-063 strong reading's distributed `CandidateRule` field with continuous tolerance gates becomes the natural successor architecture.

**Architectural commitment for the plan-doc:** R2 = N=2 heads at Phase 1. Phase 4 / GAP-E test is the falsification path for "two heads is enough"; failure routes the cluster toward ARC-063 strong reading.

---

## Verdict 4 — R4 (calibration target — secondary)

Not arbitrated by this pull. The 7 entries are anchored on neuroscience substrate, not behavioural ecology. Pull B ("behavioural ecology of refugia-vs-forage strategy partitioning in vertebrates") is the appropriate place for R4.

---

## Cross-claim implications

### MECH-309 (monomodal collapse without rule-apprehension)

The pull *supports* MECH-309's logical-necessity claim with two distinct anchors:

1. **Bongard & Nieder 2010** establishes that lateral PFC has rule-coding units that encode rules at an *abstract* level, generalising to unseen instances. The capacity MECH-309 says strict Bayesian / parametric-policy learners lack — abstraction over the hypothesis space — biology has it. The architectural implication is that ARC-062's discriminator should be designed to develop rule-cell-like representations under training pressure, not just to provide a soft gating weight in [0, 1].

2. **Capkova/Mansouri 2025** establishes that distinct frontal regions make dissociable contributions to rule-guided decision-making. Rule-context modulation is *distributed*, not concentrated at a single site. The architectural implication is that ARC-062 weak reading is a useful Phase 1 simplification but not a complete instantiation of the rule-apprehension layer biology actually implements — ARC-063 strong reading's distributed multi-site commitment is on the long path.

### ARC-062 (V3 architectural slot, weak reading)

The pull *supports* the architectural commitment in principle (rule-coding units exist, bias projections are real, adaptive coding by behavioural relevance is the operating mechanism). It does not *prescribe* the specific two-head + soft-discriminator instantiation — that is engineering choice. The pull *qualifies* the commitment with three caveats captured in the failure signatures:

- (Rigotti) Discrete heads under-utilise the dimensionality biology achieves with mixed selectivity. Phase 4 / GAP-E flag.
- (Bongard-Nieder) Rule-coding units depend on abstraction pressure under training. ARC-062 may need an explicit rule-discrimination loss on the encoder rather than relying on policy-loss back-propagation alone.
- (Capkova/Mansouri) Single-site instantiation is biologically incomplete. Rule-value updating (OFC analog), rule maintenance (PS / SD-033a analog), and mode-switching from negative feedback (ACC / dACC analog) dissociate. ARC-062 weak reading addresses only the rule-maintenance leg.

### ARC-063 (V4 strong reading, deferred)

The pull *supports* the eventual V4 commitment with three converging anchors:

- (Mitchell, Erez-Duncan) Distributed multi-site adaptive coding network is the V3-end-state target.
- (Pfeiffer-Foster, also pulled previously for MECH-307) Trajectory-proposal-level rule biasing IS biologically primary, not just an abstract architectural option.
- (Capkova/Mansouri) The distinct frontal sub-functions imply distinct claim substrates that ARC-063's `CandidateRule` distributed field naturally accommodates.

The pull does not change ARC-063's V4 implementation_phase — V4 deferral remains correct because the strong reading is a heavy multi-module commitment. It strengthens the case that V4 *will* be needed, which is the persistent-flag function ARC-063 already serves in the registry.

---

## Discharged debt

The MECH-309 `evidence_quality_note` registered 2026-05-08 stated:

> "Biology-before-formal-definitions lit-pull on the broader rule-apprehension cluster (hippocampal rollout selection, basal ganglia commitment, sleep-vs-waking refinement) is recommended before promoting MECH-309 from candidate."

This pull *partially* discharges that debt:

- ✓ Hippocampal rollout selection — Pfeiffer & Foster 2013
- ✓ Basal ganglia commitment — Gurney/Humphries/Redgrave 2015
- ✗ Sleep-vs-waking refinement — *not* covered by Pull A (Pull B is a separate behavioural-ecology focus; sleep-vs-waking refinement remains as a recommended future pull, deferred to ARC-063 V4 work).

Plus: PFC rule-coding (Bongard-Nieder, Miller-Cohen), PFC mixed selectivity (Rigotti), distributed MD network (Mitchell), MD adaptive coding (Erez-Duncan), and frontal lesion dissociation (Capkova/Mansouri) — all biologically grounded anchors for the cluster.

**Action:** update MECH-309 `evidence_quality_note` to mark this lit-pull discharged, point at this directory, and add the sleep-vs-waking refinement debt as a remaining future ARC-063 V4 pull rather than a MECH-309 promotion blocker.

---

## Next steps post-pull

1. Rebuild the evidence index (`build_experiment_indexes.py`) — `lit_conf` updates expected on MECH-309 (0.0 → ~0.85), ARC-062 (0.0 → ~0.85), ARC-063 (0.0 → ~0.80). Quadrant transitions: all three move from `speculative` toward `plausible_unproven` since experimental confidence is still 0.
2. Update MECH-309 `evidence_quality_note` per the "Action" above.
3. Draft `evidence/planning/arc_062_rule_apprehension_plan.md` per the proposed sketch in the parent session, using verdicts 1/2/3 above as the resolved-default values for R1/R2/R3 in the plan's Open Questions section.
4. Update `commitment_closure_plan.md` GAP-1 row to depend on `rule_apprehension:GAP-A/B`.
5. Pull B (behavioural ecology of refugia-vs-forage strategy partitioning) — sequential, separate target_review_ directory, addresses R4.

---

## Entries summary

| entry_id | source | direction | confidence | primary R-question |
|---|---|---|---|---|
| `..._pfc_rule_as_bias_miller2001` | Miller & Cohen 2001 *Annu Rev Neurosci* | supports | 0.85 | R1 + R3-(iii) foundational |
| `..._mixed_selectivity_rigotti2013` | Rigotti et al. 2013 *Nature* | mixed | 0.74 | R1 + R2 caveat |
| `..._hippocampal_goal_preplay_pfeiffer2013` | Pfeiffer & Foster 2013 *Nature* | supports | 0.82 | R3-(ii) trajectory-proposal |
| `..._corticostriatal_action_gate_gurney2015` | Gurney/Humphries/Redgrave 2015 *PLoS Biol* | supports | 0.78 | R3-(i) BG-side score-aggregation |
| `..._frontal_lesion_rule_dissociation_capkova2025` | Capkova/Mansouri/Buckley 2025 *eNeuro* | supports | 0.84 | R3 distributed multi-site (PS/OFC/ACC) |
| `..._macaque_md_network_mitchell2016` | Mitchell et al. 2016 *J Neurosci* | supports | 0.72 | R1 insular + R3 distributed multi-site |
| `..._pfc_rule_cells_bongard2010` | Bongard & Nieder 2010 *PNAS* | supports | 0.81 | R3-(iii) PFC rule-coding units |
| `..._md_adaptive_coding_erez2015` | Erez & Duncan 2015 *J Neurosci* | supports | 0.74 | R3 adaptive-coding mechanism |
