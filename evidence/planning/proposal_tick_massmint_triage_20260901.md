# proposal_tick mass-mint: validity pass and prioritisation

Generated 2026-09-01T20:49:35Z by orchestrate-20260901-curate-r3 (/metaworker-orchestrate), at user request.

## What happened

`proposal_tick` minted **166 `chip-proposal-exp-*` chips between 20:27Z and 20:29Z**, one per
proposal recorded as V3-testable with no completed run. Each is titled "Queue experiment for
EXP-NNNN (CLAIM)", so the queue-starvation preempt in `dispatch_candidate_order.py` promotes
ALL of them into the science tier. With dispatcher leases live that would have committed the
fleet to 166 Opus `/queue-experiment` sessions overnight, on a day the account had already hit
its monthly spend limit. Dispatch was paused and the user directed a prioritisation pass
instead: take the 10 most useful now, pace the remainder over the coming week.

The FINDING is sound -- 166 untested V3 proposals is real and worth knowing. The DELIVERY is
not: one chip per registry row is ledger volume, not a research plan.

## Validity pass (all 166)

- All 166 claim ids resolve in `claims.yaml`. No orphans.
- Status: 149 `candidate`, 17 `provisional`. All genuinely untested.
- Spot-checked the top 14 against `claim_evidence.v1.json`: **0 existing runs each**, so the
  "no completed run" assertion holds where it was checked.
- **27 are NOT V3-testable** (`implementation_phase` v4/v5) despite the chips asserting they
  are. The producer's predicate does not check `implementation_phase`. These are listed
  separately below and must NOT be queued as V3 work.
- **NONE of the 166 appears in `CURRENT_FRONT.md`.** They are all off the live front. That is
  not a reason to discard them -- it is the reason they can be paced rather than rushed.

## Ranking method

Ordered by DEPENDENT COUNT: how many other claims list this claim in their `depends_on`.
A claim many others rest on is the one whose falsification propagates furthest, so testing it
buys the most information. Ties broken by phase (explicit `v3` first) and status.

**What this ranking does NOT check, and a consumer must:** whether runnable substrate exists
for each claim. That is a per-claim question `/queue-experiment` answers at authoring time
(its Step 2.5c substrate-overlap gate). A high-dependent claim with no substrate is not
actionable, and any of the 10 below may turn out that way -- that is an acceptable and
informative outcome, not a failure of the pick.

## TIER 1 -- the 10 to run now

| # | dependents | claim | phase | status | EXP | chip_ref | title |
|---|---|---|---|---|---|---|---|
| 1 | 19 | ARC-019 | - | provisional | EXP-0436 | `chip-proposal-exp-0436` | REE requires staged developmental training with explicit curriculum gates. |
| 2 | 16 | MECH-031 | - | provisional | EXP-0812 | `chip-proposal-exp-0812` | Derived social tags and empathy coupling via control-plane knobs. |
| 3 | 9 | MECH-039 | - | provisional | EXP-0824 | `chip-proposal-exp-0824` | Modes are stable regions in control-channel space, not separate modules. |
| 4 | 9 | INV-077 | - | candidate | EXP-0749 | `chip-proposal-exp-0749` | Evaluation channels are evidence-producing boundaries, not world-state affordances: no agentic subsy |
| 5 | 7 | MECH-043 | - | provisional | EXP-0829 | `chip-proposal-exp-0829` | Dopamine-like modulation of precision-weighting for unsigned prediction errors. |
| 6 | 6 | MECH-035 | - | candidate | EXP-0817 | `chip-proposal-exp-0817` | VALENCE is vector-valued and ranked without scalar collapse. |
| 7 | 6 | MECH-027 | - | provisional | EXP-0808 | `chip-proposal-exp-0808` | Pathological modes reflect mis-tuned control-plane regimes. |
| 8 | 6 | INV-086 | - | candidate | EXP-0755 | `chip-proposal-exp-0755` | goal_maintenance_feedback_necessity |
| 9 | 5 | MECH-127 | - | candidate | EXP-0876 | `chip-proposal-exp-0876` | Counterfactual other-cost-aversion activates cooperative behavior as a motivational surrogate when t |
| 10 | 5 | MECH-081 | - | candidate | EXP-0853 | `chip-proposal-exp-0853` | E2 sufficiency constraint reduces E1 effective dimensionality target. |

## TIER 2 -- paced over the coming week (129)

**RE-RANKED 2026-09-02 FOR BUILDABILITY, not depth.** The original order was by dependent count,
on the reasoning that falsifying a load-bearing claim buys the most information. That is sound
information theory and exactly wrong for *buildability*: measured across the whole proposals file,
BLOCKED proposals average **4.96 dependents (median 3)** against **1.86 (median 1)** for available
ones -- the most depended-upon claims are the foundational, architectural ones whose substrate has
not been built. Ranking by depth therefore selected FOR un-buildability, and the first batch drawn
that way blocked at ~67% against a 4.6% population rate (EXP-0418/0812/0817/0829 all
`blocked_substrate`, all four of that date's blocks).

The order below now favours concrete leaf mechanisms: low dependent count, MECH over ARC, explicit
v3 phase. Entries already proven `blocked_substrate`, or already executed/queued, are sunk to the
bottom rather than deleted -- a block is a fact about today's substrate, not a permanent verdict,
and they become eligible again once the owed builds land.

Withdrawn from the live ledger to keep the dispatcher on curated work.

**THIS IS AUTOMATED -- do not hand re-mint from this table.** `scripts/proposal_backlog_dripfeed.py`
(launchd `com.ree.proposaldripfeed`, hourly, Mac-only) reads THIS TABLE as its source of truth and
tops the open proposal-chip count back up to a floor of 10, highest-dependents-first, at most 5 per
run. It is a TOP-UP, not a scheduled batch: it mints only when the fleet has worked some off, so the
real pacing is throughput, not a clock, and a busy or stopped fleet simply gets nothing new.

Two properties worth knowing before editing this table:
- Each paced item is re-minted under a derived `<orig_ref>-paced` chip_ref, because `chip_ledger`
  resolution is MONOTONE ("a chip never reopens", chip_ledger.py:1115) -- the withdrawn originals
  cannot be revived. That suffix is also the idempotency key, so re-running is always safe.
- The parser requires the row shape below exactly. Claim ids with a letter suffix (e.g. `SD-033d`)
  are supported -- an earlier pattern silently dropped exactly one row, which would then never have
  been paced back in at all.

| dependents | claim | phase | EXP | chip_ref | title |
|---|---|---|---|---|---|
| 0 | MECH-530 | v3 | EXP-1153 | `chip-proposal-exp-1153` | E3's decision-outcome signals to any downstream consumer (including a future... |
| 0 | MECH-494 | v3 | EXP-1121 | `chip-proposal-exp-1121` | The criterion for abandoning an inferred context is PERSISTENT, STRUCTURED evidence... |
| 0 | MECH-474 | v3 | EXP-1110 | `chip-proposal-exp-1110` | LEARNING-MECHANISM META-SELECTION (narrow form): the control plane selects among the... |
| 0 | MECH-470 | v3 | EXP-1107 | `chip-proposal-exp-1107` | Topological position improves ghost-goal reactivation ranking: MECH-292/293 rank... |
| 0 | MECH-426 | v3 | EXP-1079 | `chip-proposal-exp-1079` | progress_velocity_maintenance |
| 0 | MECH-384 | v3 | EXP-1045 | `chip-proposal-exp-1045` | Lightweight self-narration trace/debug scaffold: an optional traceable field set... |
| 0 | MECH-167 | v3 | EXP-0903 | `chip-proposal-exp-0903` | z_harm_a (harm-driven affective accumulation) and drive_level (energy-depletion... |
| 0 | MECH-136 | v3 | EXP-0886 | `chip-proposal-exp-0886` | E3 harm evaluation must apply an agency-gain correction to counteract E2's systematic... |
| 0 | MECH-115 | v3 | EXP-0870 | `chip-proposal-exp-0870` | Hypothesis tag (MECH-094) reliability degrades with z_self dispersion; high D_eff... |
| 0 | MECH-109 | v3 | EXP-0865 | `chip-proposal-exp-0865` | Voluntary respiratory modulation provides the one top-down deliberate handle on the E3... |
| 1 | MECH-469 | v3 | EXP-1105 | `chip-proposal-exp-1105` | Relation types are NOT collapsible to one adjacency structure: collapsing all edge... |
| 1 | MECH-464 | v3 | EXP-1099 | `chip-proposal-exp-1099` | D1/D2 opponent dopamine gain is ORDER-CHANGING, not a uniform scalar: because it gains... |
| 1 | MECH-239 | v3 | EXP-0947 | `chip-proposal-exp-0947` | The hippocampal indexing substrate includes a temporal dimension implemented via time... |
| 1 | MECH-237 | v3 | EXP-0944 | `chip-proposal-exp-0944` | The z_goal attractor must be globally reachable across the z_goal sub-space —... |
| 1 | MECH-222 | v3 | EXP-0926 | `chip-proposal-exp-0926` | Failure of continuous z_self residualization produces self-attribution contamination... |
| 1 | MECH-213 | v3 | EXP-0920 | `chip-proposal-exp-0920` | e1_e2_joint_rem_calibration |
| 1 | MECH-208 | v3 | EXP-0913 | `chip-proposal-exp-0913` | Valence-asymmetric replay causally drives approach/avoidance bias: harm-path replay is... |
| 1 | MECH-206 | v3 | EXP-0911 | `chip-proposal-exp-0911` | CA1 acts as a PE-proportional comparator that writes episodes to the surprise buffer:... |
| 1 | MECH-162 | v3 | EXP-0901 | `chip-proposal-exp-0901` | z_resource (SD-015, object-identity encoding) and z_world (spatial-contextual... |
| 1 | MECH-160 | v3 | EXP-0897 | `chip-proposal-exp-0897` | The E2 action_bias pathway (MECH-151, OFC analog) and E3 terrain_weight pathway... |
| 1 | MECH-125 | v3 | EXP-0872 | `chip-proposal-exp-0872` | E3 trajectory selection implements multi-constraint viability evaluation rather than... |
| 0 | SD-081 | v3 | EXP-1216 | `chip-proposal-exp-1216` | e3.dualsystem_uncertainty_arbitration. An explicit arbitration weight over the HABIT... |
| 0 | SD-075 | v3 | EXP-1212 | `chip-proposal-exp-1212` | Episode-boundary continuity for the SD-069 phasic surprise-EMA baseline, plus... |
| 0 | SD-074 | v3 | EXP-1210 | `chip-proposal-exp-1210` | Trained-enough agent substrate for read-only control-plane telemetry probes: a... |
| 0 | SD-033d | v3 | EXP-1176 | `chip-proposal-exp-1176` | Premotor/SMA-analog (sequence execution substrate): module that holds candidate action... |
| 0 | MECH-328 | - | EXP-1005 | `chip-proposal-exp-1005` | Synthetic and real z_goal vectors must lie in the same latent manifold for... |
| 0 | MECH-250 | - | EXP-0965 | `chip-proposal-exp-0965` | The end of exhalation (expiration phase) provides a hard, periodic release signal for... |
| 0 | MECH-247 | - | EXP-0959 | `chip-proposal-exp-0959` | Trauma-shaped hypervigilant priors can generate psychotic-like symptoms by structuring... |
| 0 | MECH-246 | - | EXP-0957 | `chip-proposal-exp-0957` | Psychotic-like symptoms can arise from signal-degradation pareidolia: sufficiently... |
| 0 | MECH-234 | - | EXP-0941 | `chip-proposal-exp-0941` | DMS (goal-directed) and DLS (habitual) corticostriatal circuits can produce... |
| 0 | MECH-233 | - | EXP-0939 | `chip-proposal-exp-0939` | Threat and approach valence enter hippocampal terrain through mechanistically... |
| 0 | MECH-227 | - | EXP-0935 | `chip-proposal-exp-0935` | Anaesthesia as D_V collapse: general anaesthesia abolishes consciousness by disrupting... |
| 0 | MECH-190 | - | EXP-0907 | `chip-proposal-exp-0907` | Cooperative predator defense emerges without language when defense scent pressure is... |
| 0 | MECH-157 | - | EXP-0892 | `chip-proposal-exp-0892` | External vs internal cognition modes are controlled by precision-routing... |
| 0 | MECH-134 | - | EXP-0884 | `chip-proposal-exp-0884` | A vmPFC-analog substrate must activate goal approach pull as a distinct property from... |
| 0 | MECH-133 | - | EXP-0882 | `chip-proposal-exp-0882` | A vmPFC-analog substrate must activate safety memories with sufficient force to... |
| 0 | MECH-132 | - | EXP-0880 | `chip-proposal-exp-0880` | A vmPFC-analog substrate must activate social and identity constraints as live... |
| 0 | MECH-079 | - | EXP-0849 | `chip-proposal-exp-0849` | Phenomenological continuous selfhood is an artefact of stable hippocampal map geometry |
| 0 | MECH-078 | - | EXP-0847 | `chip-proposal-exp-0847` | Amygdala bootstraps novel valence for unmapped hippocampal territory; anxiety... |
| 0 | MECH-050 | - | EXP-0833 | `chip-proposal-exp-0833` | Functional locality supports attribution without requiring anatomical columns |
| 0 | MECH-049 | - | EXP-0831 | `chip-proposal-exp-0831` | Temporal phase compartmentalisation preserves ethical constraint independence |
| 0 | MECH-042 | - | EXP-0827 | `chip-proposal-exp-0827` | Telemetry exposure channels report internal control-plane state for diagnostics |
| 0 | MECH-038 | - | EXP-0822 | `chip-proposal-exp-0822` | Arcuate-like sequence-to-motor channel nudges language emergence |
| 0 | MECH-028 | - | EXP-0810 | `chip-proposal-exp-0810` | Ethical behavior depends on mode transitions and learning preservation |
| 0 | MECH-023 | - | EXP-0804 | `chip-proposal-exp-0804` | Responsibility is geometric and path-dependent |
| 0 | MECH-021 | - | EXP-0802 | `chip-proposal-exp-0802` | Subjective now is a control surface across temporal horizons |
| 0 | MECH-013 | - | EXP-0788 | `chip-proposal-exp-0788` | Language failure modes and pathologies |
| 0 | MECH-012 | - | EXP-0786 | `chip-proposal-exp-0786` | Language and institutions interplay |
| 0 | MECH-002 | - | EXP-0774 | `chip-proposal-exp-0774` | Precision control analogues shape cognitive regimes |
| 0 | INV-040 | v3 | EXP-0731 | `chip-proposal-exp-0731` | A minimal sensory cue pattern in z_world is sufficient to activate the appropriate... |
| 2 | MECH-495 | v3 | EXP-1123 | `chip-proposal-exp-1123` | The objective for hippocampal/episodic memory organisation is RELATIONAL... |
| 2 | MECH-251 | v3 | EXP-0967 | `chip-proposal-exp-0967` | z_goal projects to a precision template vector that is additively written to the E1... |
| 2 | MECH-221 | v3 | EXP-0924 | `chip-proposal-exp-0924` | z_world must be continuously residualized against z_self predictions; efference-copy... |
| 2 | MECH-161 | v3 | EXP-0899 | `chip-proposal-exp-0899` | Ready vigilance (MECH-026) requires an arousal regulator that maintains an optimal... |
| 1 | SD-086 | v3 | EXP-1222 | `chip-proposal-exp-1222` | z_harm_a's functional readout must be a calibrated scalar valuation, not the latent... |
| 1 | SD-071 | v3 | EXP-1206 | `chip-proposal-exp-1206` | First-order consolidation-phase readouts validated: the NREM slot-filling and SWS... |
| 1 | MECH-327 | - | EXP-1003 | `chip-proposal-exp-1003` | During sensorimotor play, E1 prediction-error locus upweights probe-action selection:... |
| 1 | MECH-249 | - | EXP-0963 | `chip-proposal-exp-0963` | Acetylcholine/noradrenaline balance implements action-mode-specific hippocampal write... |
| 1 | MECH-248 | - | EXP-0961 | `chip-proposal-exp-0961` | Source monitoring (frontoparietal network; Johnson-Raye tradition) is a candidate... |
| 1 | MECH-170 | - | EXP-0905 | `chip-proposal-exp-0905` | Sleep architecture restoration in early MCI should produce dissociated cognitive... |
| 1 | MECH-159 | - | EXP-0895 | `chip-proposal-exp-0895` | Moral progress in REE is hypothesised to be intergenerational: childhood plasticity... |
| 1 | MECH-131 | - | EXP-0878 | `chip-proposal-exp-0878` | A vmPFC-analog substrate must activate stored aversive residue as an anticipatory... |
| 1 | MECH-082 | - | EXP-0855 | `chip-proposal-exp-0855` | Hippocampal map distortion propagates through E2 to bias E1 attentional sampling... |
| 1 | MECH-067 | - | EXP-0845 | `chip-proposal-exp-0845` | A machine-checkable phase/store/actor permission matrix is required to enforce... |
| 1 | MECH-066 | - | EXP-0843 | `chip-proposal-exp-0843` | Pre-commit and post-commit channels may share representations but must stay separated... |
| 1 | MECH-064 | - | EXP-0839 | `chip-proposal-exp-0839` | Typed authority/control-store separation blocks direct exteroceptive writes into... |
| 1 | MECH-034 | - | EXP-0815 | `chip-proposal-exp-0815` | Viability mapping updates are distinct from residue curvature updates |
| 1 | MECH-024 | - | EXP-0806 | `chip-proposal-exp-0806` | Selfhood, personality, and ethics converge structurally |
| 1 | MECH-017 | - | EXP-0796 | `chip-proposal-exp-0796` | Reality consolidation during sleep |
| 1 | MECH-016 | - | EXP-0794 | `chip-proposal-exp-0794` | Precision recalibration during sleep |
| 1 | MECH-015 | - | EXP-0792 | `chip-proposal-exp-0792` | Trust and deception dynamics |
| 1 | MECH-014 | - | EXP-0790 | `chip-proposal-exp-0790` | Minimal signalling channel requirements |
| 1 | MECH-003 | - | EXP-0776 | `chip-proposal-exp-0776` | Precision must be tau-scoped with lossy projections |
| 1 | INV-093 | v3 | EXP-0760 | `chip-proposal-exp-0760` | Skill optimisation must NOT trade harm sensitivity for competence (learning-side... |
| 1 | INV-092 | v3 | EXP-0758 | `chip-proposal-exp-0758` | Distractor suppression must remain SELECTIVELY PERMEABLE to harm and other-agent... |
| 3 | MECH-468 | v3 | EXP-1103 | `chip-proposal-exp-1103` | Hippocampal anchor TOPOLOGY carries functional information not present in local anchor... |
| 3 | MECH-110 | v3 | EXP-0867 | `chip-proposal-exp-0867` | Laughter is rapid repeated hypothesis-tag cycling — threat activation followed... |
| 3 | MECH-105 | v3 | EXP-0860 | `chip-proposal-exp-0860` | Hippocampal sequence completion drives BG beta release via subiculum-NAc-VTA... |
| 0 | SD-088 | - | EXP-1224 | `chip-proposal-exp-1224` | The claims index must represent source-dependence between supporting judgements. Two... |
| 0 | INV-095 | - | EXP-0763 | `chip-proposal-exp-0763` | Existence has value sufficient to justify its continuation |
| 0 | INV-063 | - | EXP-0736 | `chip-proposal-exp-0736` | minimum_entropy_intake_sleep_dependency |
| 0 | INV-022 | - | EXP-0707 | `chip-proposal-exp-0707` | Trust/precision allocation must remain heterogeneous, not a single scalar |
| 0 | IMPL-027 | - | EXP-0683 | `chip-proposal-exp-0683` | Technical comparison: REE versus Meta AI/KAUST Neural Computers roadmap |
| 0 | IMPL-026 | - | EXP-0681 | `chip-proposal-exp-0681` | Medication classification by predicted attribution pipeline effect: a reference table... |
| 0 | IMPL-025 | - | EXP-0679 | `chip-proposal-exp-0679` | Cross-version hook surface contract and registry |
| 0 | IMPL-016 | - | EXP-0669 | `chip-proposal-exp-0669` | Trajectory selection detail for E3 |
| 0 | EXT-008 | - | EXP-0607 | `chip-proposal-exp-0607` | Meta-agent evaluation-boundary exploitation: under strong optimisation pressure,... |
| 0 | EXT-007 | - | EXP-0605 | `chip-proposal-exp-0605` | Context amnesia: no consolidation mechanism for a persistent world-model across... |
| 0 | EXT-006 | - | EXP-0603 | `chip-proposal-exp-0603` | Other-model collapse: no homologous model of other agents' internal states |
| 0 | EXT-005 | - | EXP-0601 | `chip-proposal-exp-0601` | Causal attribution gap: language describes causation without a causal signature... |
| 0 | EXT-004 | - | EXP-0599 | `chip-proposal-exp-0599` | Goal misgeneralization: causal consequences do not carry forward across contexts |
| 0 | EXT-002 | - | EXP-0595 | `chip-proposal-exp-0595` | Hallucination: no persistent error residue accumulates to shape future outputs |
| 0 | EXT-001 | - | EXP-0578 | `chip-proposal-exp-0578` | Sycophancy: approval-seeking displaces principled goal pursuit |
| 2 | MECH-223 | - | EXP-0928 | `chip-proposal-exp-0928` | Animated agency attribution overweighting: systematic bias toward attributing... |
| 2 | MECH-211 | - | EXP-0917 | `chip-proposal-exp-0917` | schema_consolidation_as_search_grammar |
| 2 | MECH-084 | - | EXP-0858 | `chip-proposal-exp-0858` | Noradrenaline as attentional snap and E1/E2 sampling ratio modulator |
| 2 | MECH-080 | - | EXP-0851 | `chip-proposal-exp-0851` | Rollout truncation set-points as psychiatric individual differences substrate... |
| 2 | MECH-018 | - | EXP-0798 | `chip-proposal-exp-0798` | Residue integration during sleep |
| 2 | MECH-011 | - | EXP-0784 | `chip-proposal-exp-0784` | Language and learning dynamics |
| 2 | MECH-005 | - | EXP-0780 | `chip-proposal-exp-0780` | Path authority and interruptibility via norepinephrine-like control |
| 2 | MECH-004 | - | EXP-0778 | `chip-proposal-exp-0778` | Signal-to-knob wiring map for control plane |
| 4 | MECH-107 | v3 | EXP-0862 | `chip-proposal-exp-0862` | Exhalation is the physiological instantiation of E3 trajectory-abandonment — each... |
| 1 | INV-069 | - | EXP-0742 | `chip-proposal-exp-0742` | The self is defined as the dynamically sustained process maintaining high... |
| 1 | IMPL-019 | - | EXP-0675 | `chip-proposal-exp-0675` | Self-first, social-later developmental testing order heuristic |
| 1 | IMPL-008 | - | EXP-0657 | `chip-proposal-exp-0657` | Program phases, repository roles, and phase-gate criteria |
| 3 | SD-077 | v3 | EXP-1214 | `chip-proposal-exp-1214` | Common-mode-invariant (centered) super-ordinal goal-anchor cue key: the MECH-189... |
| 3 | SD-070 | v3 | EXP-1204 | `chip-proposal-exp-1204` | z_world P0 anti-collapse encoder-training recipe: a mini-batched P0 that trains the... |
| 3 | MECH-126 | - | EXP-0874 | `chip-proposal-exp-0874` | Specific modes of REE state abstraction failure -- overmerge, oversplit, temporal... |
| 3 | MECH-055 | - | EXP-0837 | `chip-proposal-exp-0837` | Affective channel separation keeps hedonic tone, valence, and signed PE distinct |
| 0 | ARC-121 | v3 | EXP-0560 | `chip-proposal-exp-0560` | REE's mechanisms increasingly converge on maintaining and consuming a SHARED... |
| 0 | ARC-052 | v3 | EXP-0504 | `chip-proposal-exp-0504` | harm_precision_weighting |
| 2 | SD-090 | - | EXP-1228 | `chip-proposal-exp-1228` | Mechanism functional-role classification, and a removal-justification vocabulary. Five... |
| 2 | SD-089 | - | EXP-1226 | `chip-proposal-exp-1226` | Claim-origin provenance: the registry records the epistemic origin class of each... |
| 2 | INV-024 | - | EXP-0711 | `chip-proposal-exp-0711` | Offline consolidation and online commitment must remain isolated at... |
| 2 | INV-023 | - | EXP-0709 | `chip-proposal-exp-0709` | Protected offline recalibration/integration regimes are structurally required |
| 2 | IMPL-023 | - | EXP-0677 | `chip-proposal-exp-0677` | REE-v2 representation-interface-first spec and phase gate |
| 4 | MECH-019 | - | EXP-0800 | `chip-proposal-exp-0800` | Control plane shapes modes of cognition, not discrete choices |
| 1 | ARC-037 | v3 | EXP-0494 | `chip-proposal-exp-0494` | REE requires a causal attribution routing circuit (anterior insula equivalent) that... |
| 3 | EXT-003 | - | EXP-0597 | `chip-proposal-exp-0597` | Reward hacking: scalar reward conflates incommensurable error signals |
| 5 | MECH-065 | - | EXP-0841 | `chip-proposal-exp-0841` | Reality-coherence conflict lane modulates loop precision and commitment thresholds... |
| 5 | MECH-037 | - | EXP-0820 | `chip-proposal-exp-0820` | Papez-like loop provides provenance gating and reality filtering |
| 0 | ARC-061 | - | EXP-0515 | `chip-proposal-exp-0515` | Self-attribution is implemented via a family of forward-model comparators at motor,... |
| 2 | ARC-120 | v3 | EXP-0557 | `chip-proposal-exp-0557` | Behavioural/write authority in REE is (and should remain) EARNED through demonstrated... |
| 3 | ARC-131 | v3 | EXP-0573 | `chip-proposal-exp-0573` | Installability is a competence dissociable from isolated component-level validation: a... |
| 5 | INV-072 | - | EXP-0746 | `chip-proposal-exp-0746` | Violence corollary: violence is conditionally permissible only when an agent is not... |
| 5 | EXT-009 | - | EXP-0609 | `chip-proposal-exp-0609` | Similarity-gated care collapse (REFLEXIVE / self-directed failure mode): because REE... |
| 2 | ARC-073 | - | EXP-0519 | `chip-proposal-exp-0519` | Play-to-real transition is triggered by competence saturation (d(PE)/dt < threshold)... |
| 5 | ARC-044 | - | EXP-0501 | `chip-proposal-exp-0501` | Context-dependent neuromodulatory gain is a single unifying mechanism expressed at... |
| 4 | ARC-008 | - | EXP-0418 | `chip-proposal-exp-0418` | Commitment eligibility is gated by tau, rho, and phi |
## NOT V3-TESTABLE -- do not queue as V3 work (27)

| dependents | claim | phase | EXP | chip_ref | title |
|---|---|---|---|---|---|
| 7 | MECH-278 | v4 | EXP-0976 | `chip-proposal-exp-0976` | Stage-2 specialisation of MECH-276: once the agent can distinguish self-produced from... |
| 5 | MECH-300 | v4 | EXP-0988 | `chip-proposal-exp-0988` | Cognitive map traversal via theta sequences operates at the agent's active abstraction... |
| 5 | MECH-228 | v4 | EXP-0937 | `chip-proposal-exp-0937` | Field-level coherence support (ephaptic coupling): extracellular electric field... |
| 3 | MECH-299 | v4 | EXP-0986 | `chip-proposal-exp-0986` | Theta-cycle content scales with the agent's current substrate abstraction vocabulary:... |
| 3 | MECH-274 | v4 | EXP-0971 | `chip-proposal-exp-0971` | V4-reserved. The sleep-dependent aggregation pattern of MECH-273 extends to... |
| 2 | ARC-031 | v4 | EXP-0473 | `chip-proposal-exp-0473` | HippocampalModule navigates z_self trajectory space (deliberation sequences) in... |
| 1 | MECH-296 | v4 | EXP-0980 | `chip-proposal-exp-0980` | Prototype-readout operator computes a softmax-attention match between the current... |
| 1 | MECH-145 | v5 | EXP-0888 | `chip-proposal-exp-0888` | Prescriptive ethical trajectory certification in REE requires a Control Barrier... |
| 1 | INV-039 | v4 | EXP-0729 | `chip-proposal-exp-0729` | Schema-primed rapid assimilation: any hippocampal planning system with a stable prior... |
| 1 | ARC-083 | v4 | EXP-0529 | `chip-proposal-exp-0529` | Others-as-object (PILLAR 4 of ARC-080): each other agent j gets its own token-keyed... |
| 1 | ARC-055 | v4 | EXP-0510 | `chip-proposal-exp-0510` | Verisimilitude signal availability: V(t) and D_V must be explicitly available to E3... |
| 0 | SD-044 | v4 | EXP-1184 | `chip-proposal-exp-1184` | Motor primitive substrate at the bottom of the action-representation hierarchy: a... |
| 0 | SD-043 | v4 | EXP-1182 | `chip-proposal-exp-1182` | vmPFC analogue gains an abstract task-structure encoding capacity that compresses... |
| 0 | SD-041 | v4 | EXP-1180 | `chip-proposal-exp-1180` | An explicit thalamic-routing substrate (reuniens/MD-analogue) gates and amplifies... |
| 0 | MECH-301 | v4 | EXP-0990 | `chip-proposal-exp-0990` | Priority-weighted anchor replay (MECH-285) runs not only during sleep but also during... |
| 0 | MECH-298 | v4 | EXP-0984 | `chip-proposal-exp-0984` | Event-gated frontal write at goal-instantiation moments: when GoalState transitions... |
| 0 | MECH-297 | v4 | EXP-0982 | `chip-proposal-exp-0982` | Type-V_s gating extends MECH-269's per-stream / per-region V_s with a per-type V_s... |
| 0 | MECH-255 | v4 | EXP-0969 | `chip-proposal-exp-0969` | Template compilation is implemented by vmPFC value-content projection composed with... |
| 0 | MECH-243 | v4 | EXP-0955 | `chip-proposal-exp-0955` | A dedicated hippocampal output pathway (analogous to vCA1 to nucleus accumbens shell)... |
| 0 | MECH-242 | v4 | EXP-0953 | `chip-proposal-exp-0953` | Hippocampal trajectory construction operates via two dissociable mechanisms: (1)... |
| 0 | MECH-241 | v4 | EXP-0951 | `chip-proposal-exp-0951` | During active goal pursuit, hippocampal and OFC-analogue representations of... |
| 0 | MECH-240 | v4 | EXP-0949 | `chip-proposal-exp-0949` | SD-012 homeostatic drive_level dynamically scales z_goal attractor basin width — high... |
| 0 | MECH-226 | v4 | EXP-0933 | `chip-proposal-exp-0933` | TCL substrate: Temporal Coherence Loop is implemented as a distributed system... |
| 0 | MECH-224 | v4 | EXP-0930 | `chip-proposal-exp-0930` | harm_eval.piecewise_gradient_structure: E3 harm_eval learns both continuous intensity... |
| 0 | MECH-218 | v4 | EXP-0922 | `chip-proposal-exp-0922` | interoceptive_predictive_wanting |
| 0 | MECH-146 | v5 | EXP-0890 | `chip-proposal-exp-0890` | Diagnostic ethical trajectory verification in REE (counterfactual case, MECH-127)... |
| 0 | ARC-082 | v4 | EXP-0527 | `chip-proposal-exp-0527` | Tools/affordances as object->action binding (PILLAR 3 of ARC-080): an object's... |
