---
closure_plan:
  id: basal_ganglia_assembly_map
  title: "Basal-Ganglia Assembly Map + ARC-106 Divergence Ledger (BG-as-built vs BG-as-in-nature)"
  registered: 2026-06-22
  last_updated: 2026-06-22
  generation: v3
  scope_claims: [ARC-107, ARC-106, MECH-439, MECH-448, MECH-449, MECH-447, MECH-260, MECH-090, MECH-320, MECH-203, Q-078]
  sibling_plans: [conversion_ceiling_campaign, arc_062_rule_apprehension, commitment_closure, biology_grounding_convergence_v4]
  derived_from: "session review 2026-06-22 (broad BG overview: missing-pieces map + deviation audit), grounded against e3_selector.py + the ARC-107 lineage"
  purpose: >
    Single durable home for the BG-as-built-vs-BG-in-nature analysis so the
    learning is not lost across sessions. Two products: (A) the missing-pieces
    ASSEMBLY MAP (afferents / internal architecture / efferents / learning that
    REE has not yet built), and (B) the ARC-106 DIVERGENCE LEDGER (places REE has
    built something but in a way that diverges from biology and may be an
    incorrect design choice). Most rows here are assembly frontier, not closure
    gaps. The canonical living ledger remains ARC-106 docs/architecture
    s5; the canonical completeness tracker remains the ARC-107 design-note s6b.
    This doc is the consolidated map + the four previously-SILENT divergences +
    the detailed top-three repair-vs-defensible note.
  nodes:
    - id: "basal_ganglia_assembly_map:AFFERENTS"
      title: "Missing afferents (data sources): thalamostriatal salience, amygdala/hippocampus->ventral striatum loop channel, dopaminergic RPE INTO the gating weights"
      phase: "Assembly frontier. Selector inputs are F (88-89% monopolist) + the modulatory bias channels + the candidate pool. Biology's distinct striatal salience afferent (CM/Pf) and limbic loop channel are folded into bias signals, not routed as selector inputs; the dopaminergic learning afferent is absent (gating does not learn). See A-map below."
      status: assembling
      severity: load-bearing
      awaiting: "unified dopamine substrate (BG-LEARN) + decision on loop segregation"
      assembly_status: queued
      owner_exq: "null -- not yet a build queue entry"
    - id: "basal_ganglia_assembly_map:EFFERENTS"
      title: "Missing drains (data sinks): GPi->lateral-habenula negative-RPE drain, SNr->colliculus fast subcortical motor drain, thalamic cognitive-loop (working-memory) gating drain"
      phase: "Assembly frontier. REE has one output path (the committed trajectory) + the de-commit release. Biology's negative-teaching drain (habenula), fast cortex-bypassing motor drain, and cognitive-loop output-gating are all absent. See A-map below."
      status: assembling
      severity: load-bearing
      awaiting: "BG-LEARN (habenula is the negative-RPE drain) + a stance on cognitive-loop gating"
      assembly_status: queued
      owner_exq: "null"
    - id: "basal_ganglia_assembly_map:LEARN"
      title: "Missing learning: dopamine-gated three-factor plasticity on the gating/arbitration layer (the single biggest gap; the conversion ceiling restated)"
      phase: "Assembly frontier + the highest-leverage item. The ARC-107 selection CONSTITUTION (MECH-448/449/447, the authority rescale) is pure arithmetic with no learned parameters. Valuation heads (harm_eval/benefit_eval) learn; the ARBITRATION does not. Biology learns BOTH via dopaminergic RPE x Hebbian (D1-LTP / D2-LTD). F-dominance (MECH-439) is the predicted failure of a system that selects but cannot learn to select."
      status: assembling
      severity: load-bearing
      awaiting: "design decision: learned-gating vs the current arithmetic envelope as the next MECH-439 attack"
      assembly_status: queued
      owner_exq: "null -- candidate design note + claim registration is the next step"
    - id: "basal_ganglia_assembly_map:DIVERGENCE-LEDGER"
      title: "Eight divergence rows; four were SILENT (ARC-106 zero-silent-divergence violation): Go/No-Go additive collapse, RPE-as-unsigned-variance, count-based recency, 5-HT-before-DA"
      phase: "Each row needs: enter into the ARC-106 living ledger (s5) with the load-bearing-vs-decorative ablation test + the psychiatric-failure-mode column; then a disposition (tracked-divergence | repair-target | defensible-V3-simplification). The top three carry a detailed disposition note below."
      status: assembling
      severity: load-bearing
      awaiting: "ARC-106 s5 ledger rows + per-row disposition"
      assembly_status: in_progress
      owner_exq: "null -- documentation/governance, not an experiment"
---

# Basal-Ganglia Assembly Map + Divergence Ledger

**What this is.** A consolidated, durable record of how REE's basal-ganglia
substrate (the ARC-107 E3-selector constitution) compares to the basal ganglia as
it works in the brain, derived from a 2026-06-22 session review grounded against
`ree-v3/ree_core/predictors/e3_selector.py` and the ARC-107 build lineage.

**Why it lives here.** Per the assembly-vs-closure keystone, this is assembly
frontier work — a map of pieces to assemble and design choices to adjudicate, not
a set of closure verdicts to force. It rests in `status: assembling` and is
credited on the assembly axis, off the closure %.

**Relationship to the existing ledgers (single source of truth).**
- The **canonical living divergence ledger** is ARC-106 §5
  (`docs/architecture/arc_106_biology_grounding_framework.md`). The four
  previously-silent rows below should be entered there.
- The **canonical completeness tracker** is the ARC-107 design-note §6b
  (`arc_107_selector_constitution_design_2026-06-20.md`), incl. its V4-axes
  "stated bet" table. The missing-pieces map below extends that table with the
  afferent/efferent/learning items it does not yet enumerate.
- This doc is the **consolidated map + the new rows + the detailed top-three
  disposition note**; it does not replace either ledger.

---

## A. Missing-pieces assembly map (afferents / internal / efferents / learning)

What REE has built for the BG is a genuinely faithful **functional** rendering of
*selection*: eligibility-then-arbitrate (MECH-448), bounded Go/No-Go opponency
(MECH-449), conflict-graded hold (MECH-447 / MECH-439 Factor A), a pallidal
permission gate rather than bare argmax, a commit/release latch (MECH-090 +
SD-034 + MECH-342 + the rung-6 occupancy lever). The gaps are concentrated in
*learning*, *loop structure*, and the *input/output* periphery.

### A.1 Afferents (data sources) — what feeds the selector

| BG afferent | REE status | Note |
|---|---|---|
| Cortico-striatal candidate input | **built** | Hippocampal CEM proposer -> `cand_world_summaries` (via `e2.world_forward`, ARC-065 GAP-A / SD-056). |
| Primary value (F) | **built (monopolist)** | F = reality+harm+benefit+goal cost; 88-89% of committed-selection variance (V3-EXQ-571). The conversion-ceiling root. |
| Modulatory afferents | **built** | dACC (SD-032b), lPFC (SD-033a), OFC (SD-033b), MECH-295 liking, MECH-314 curiosity, MECH-320 vigor, MECH-341 entropy, route-range coherence. |
| **Thalamostriatal salience (CM/Pf intralaminar)** | **MISSING** | Biology has a distinct salience/arousal striatal afferent. REE folds this into dACC/AIC biases; there is no separate striatal salience input. |
| **Dopaminergic RPE INTO the gating weights** | **MISSING** | The learning afferent. Absent — the arbitration layer has no learned parameters (see A.4). |
| **Amygdala / hippocampus -> ventral striatum loop channel** | **MISSING (as a selector channel)** | SD-035 BLA/CeA and hippocampal context exist but feed the salience coordinator, not a limbic *loop of the selector*. |

### A.2 Internal architecture

| BG element | REE status | Note |
|---|---|---|
| Direct/Go (D1) | **built (as a scoring sign)** | `benefit_eval_head` subtraction; MECH-449 Go-promote. |
| Indirect/No-Go (D2) | **built (as a scoring sign)** | `harm_eval_head` / `lambda_ethical`; MECH-260; MECH-449 No-Go suppress. |
| Hyperdirect/STN conflict-hold | **built (scalar `gap_norm`)** | MECH-447 / MECH-439 Factor A. STN reduced to one scalar. |
| Pallidal permission gate (GPi/SNr) | **built (provisional)** | MECH-448 eligibility envelope. |
| **D1/D2 population split (opposite DA sensitivity)** | **MISSING** | Go/No-Go is a scoring *sign*, not two populations with asymmetric dopamine gain. Blocks the Parkinson/dyskinesia/Huntington/ICD disease axis (ARC-106 EARNS failure). |
| **FSI feedforward inhibition / winner-sharpening** | **MISSING** | `argmin` substitutes a hard global max for fast lateral inhibition. |
| **Cholinergic TAN pause (plasticity-window gating)** | **MISSING** | The TAN-pause-coincident-with-DA-burst defines the learning window; absent even before DA is added. |
| **Parallel segregated loops (motor/assoc/limbic)** | **MISSING (collapsed)** | One E3 selector; the dACC/OFC/lPFC analogs feed in as biases, not as separate loops. See Deviation D2 of §B and the loop-segregation question of §D. |

### A.3 Efferents (data drains) — where the output goes

| BG drain | REE status | Note |
|---|---|---|
| GPi -> thalamus (VA/VL) -> cortex -> motor | **built** | The committed trajectory = the env action. |
| De-commit release | **built** | beta-gate release; SD-034 closure; MECH-342; rung-6 occupancy release. |
| **GPi/border -> lateral habenula negative-RPE drain** | **MISSING** | The "worse than expected" teaching output. A `VALENCE_NEGATIVE_SURPRISE` channel exists in the residue field (MECH-307) and a "dread" comment, but there is no habenula analog *as a BG-output drain*. |
| **SNr -> superior colliculus / brainstem fast subcortical motor drain** | **MISSING** | REE has one output path. MECH-091 urgency-interrupt is the nearest analog (a release, not an output channel). |
| **Thalamic cognitive-loop (working-memory) output gating** | **MISSING** | Biology gates PFC working-memory updating, not just motor action. REE's selector gates actions; there is no thalamus module (the `thalam` code hits are comments). |

### A.4 Learning (the single biggest missing part)

The ARC-107 selection **constitution** is pure arithmetic with **no
dopamine-gated plasticity**. Confirmed: every arbitration lever (MECH-448
envelope, MECH-449 Go/No-Go, MECH-447 conflict-grade, the authority rescale) is a
pure-arithmetic regulator with no learned parameters and no gradient flow.
Learning exists at the **valuation** layer (`harm_eval_head`, `benefit_eval_head`,
`reality_scorer`, `ethical_scorer` are trained nn.Modules on `z_world`) but **not
at the gating/arbitration layer**.

In the brain, the cortico-striatal weights that decide *which channel wins
selection authority* are themselves learned via three-factor plasticity (Hebbian
co-activation × dopaminergic RPE), with the signature asymmetry that dopamine
potentiates D1/Go (LTP) and depresses D2/No-Go (LTD).

**This is the conversion ceiling, restated.** F monopolises 88-89% of selection
variance precisely because there is no learned striatal weighting that can
re-weight channels through experience — the diversity channels are fixed-magnitude
biases competing against a fixed primary score. The lever-by-lever campaign
(seven successive GAP-A amends; the per-channel floor dances 654h/485i/485j that
drove the MECH-448 adaptive-floor amend) is, in effect, hand-emulating with
arithmetic envelopes what biology solves with one learning rule.

### A.5 Assembly sequencing (recommended)

1. **Unified dopamine substrate** consolidating the scattered RPE/vigor/incentive
   functions, emitting a **signed three-factor teaching signal into the gating
   layer** — turning MECH-448/449 from hand-tuned arithmetic into learned
   cortico-striatal weights. Highest leverage; directly attacks MECH-439. (This
   also supplies the habenula negative-RPE drain, A.3.)
2. **D1/D2 population split with asymmetric dopamine gain** — required to *earn*
   the psychiatric-failure-mode mapping ARC-106 demands.
3. **Lateral-habenula negative-RPE drain** (falls out of (1)).
4. **Loop-segregation decision** — whether the single-arena collapse is itself
   contributing to F-dominance (see §D).

Start with **(1)**: the dopamine-into-gating question is the one that bears
directly on the live MECH-439 root.

---

## A.6 The dopaminergic control layer (biology check, 2026-06-22)

**Prompted by:** "our control plane is meant to have an input here and we forgot
to include it … we should check biology … dopaminergic equivalents are prime
candidates." This section is the literature check that followed.

**Finding (one line):** REE built the commit/maintain/release **machinery** of the
control plane (beta-gate latch + refractory, SD-034 closure operator, MECH-091
urgency interrupt, MECH-090 R-c readiness conjunction) but **not its dopaminergic
driver**. In the brain, dopamine drives *all four phases* of action commitment;
REE's control plane runs those phases off hand-specified arithmetic readiness
signals (`running_variance`, score margin, nav-competence, rule-state stability)
instead. It is a control body without its neuromodulator — and the user's instinct
is correct: several of the control-plane *bits* are not instantiated at all, not
merely missing an input.

**The four dopaminergic control-plane functions (lit-grounded) vs. what REE has:**

| Control-plane phase | Dopaminergic signal in biology | Evidence | REE today | Gap |
|---|---|---|---|---|
| **Commit threshold / readiness** (how readily / how fast to commit; response latency & vigor) | **Tonic DA = average reward rate = opportunity cost of time** sets response vigor/latency (the value of acting now vs deliberating) | Niv 2007 [1]; refined to effort-value by Zénon 2016 [2] | MECH-320 tonic-vigor is a score-*bias*; ARC-068 opportunity-cost is registered-but-unbuilt (collapsed onto vigor). It does **not** set the commit threshold (the `running_variance` gate). | **MISSING:** tonic-DA → commit-threshold/latency. |
| **Commit "go" / gate-open signal** (when to update/commit the selected program) | **Phasic DA "locks the gate to working memory"** — gates PFC updating via targeted striatal disinhibition (the PBWM go-signal) | Gruber 2006 [3]; Rac-Lubashevsky 2017 (ebEBR ~ striatal DA tracks gate-open) [4] | The commit gate (beta-gate) opens on `running_variance < threshold` + the R-c conjunction. No DA go-signal gates it. | **MISSING:** phasic-DA go/update gate. |
| **Commitment maintenance** (sustaining drive across a multi-step program / toward a distant goal) | **DA ramps scaled to goal proximity & value** provide sustained motivational drive; release-ramps = motivation (distinct from spiking = learning) | Howe 2013 [5]; Mohebi 2019 [6] | Maintenance is a **fixed bistable latch + refractory + the rung-6 occupancy lever** — flat, not proximity-scaled. | **MISSING:** DA-ramp-as-maintenance. **Directly implicates deviation B6** (the 460h ~2400-step monolithic hold): biology maintains via a ramp that peaks-then-declines with proximity, so it cannot monopolise; a flat latch can. |
| **Pre-initiation gate / invigoration** (whether & how vigorously to launch the chosen action) | **DA activity *before* movement gates + invigorates the future action**; DA required for the striatal vigor representation; depletion → bradykinesia / failure-to-act | Alves da Silva 2018 [7]; Panigrahi 2015 [8]; nuance Cai 2024 (fast DA dispensable for movement *per se* but required for vigor/motivation) [9] | Commit-entry (MECH-090 R-c) gates on decisiveness + nav-competence, not a pre-initiation DA gate/vigor term. | **MISSING:** pre-initiation DA gate — and with it the **Parkinsonian bradykinesia/avolition failure mode** (no DA to deplete → ARC-106 EARNS gap). |
| **De-commit / abort** (withdraw a committed program that is going worse than expected) | **Lateral habenula → RMTg → DA inhibition = negative RPE** drives abort/withhold + inhibitory learning | Matsumoto 2007 [10]; Hong 2011 (RMTg relay) [11]; Sosa 2021 (reward-omission inhibitory learning) [12] | The entire de-commit side (MECH-342, SD-034 closure, the 460d–j lineage, the parked rung-6) is engineered with refractory timers / latch-hold yield clauses — **with no negative-RPE driver at all.** | **MISSING:** habenula/negative-RPE-driven de-commit. The de-commit machinery has been built without its teaching signal. |

### Two implications that change the earlier analysis

1. **The "unified dopamine substrate" (A.4 / A.5 item 1) has *two co-equal jobs*, not one.** Before this check it was framed as the learned-gating teaching signal for *selection* (the MECH-439 attack). The biology shows it is *also* the driver of the *control plane*: commit-threshold (tonic), go-signal (phasic gate), maintenance (ramp), and de-commit (habenula negative RPE). The dopamine substrate is the single missing piece that closes **both** the selection-learning gap **and** the control-plane-driver gap. That raises its priority further — it is upstream of two otherwise-separate problem areas.

2. **The de-commit struggle (the 460d–j lineage, the parked rung-6) and the global-latch monopoly (deviation B6) are the *same* missing piece seen from two ends.** REE has spent ~10 iterations engineering de-commit with refractory timers and latch-hold yield clauses; biology de-commits via a negative-RPE (habenula) signal and maintains via a proximity-scaled DA ramp. Both the "hold never releases / monopolises" (B6, 460h) and the "de-commit has no authority / non-dissociable" (rung-6 park) symptoms are predicted by *maintenance-and-release driven by a fixed latch instead of a dopaminergic ramp+habenula pair*. **This makes the dopamine substrate a concrete candidate fix for the parked rung-6 — not just the MECH-439 selection problem.**

### Citations (this biology check)

- [1] [Tonic dopamine: opportunity costs and the control of response vigor](https://consensus.app/papers/details/aded550af38f576db3279838bd2a39b1/?utm_source=claude_code) (Niv et al., 2007, Psychopharmacology, 1116 cites)
- [2] [Dopamine Manipulation Affects Response Vigor Independently of Opportunity Cost](https://consensus.app/papers/details/0f105448d7535f31806cdf553e0783f3/?utm_source=claude_code) (Zénon et al., 2016, J Neurosci)
- [3] [Dopamine modulation in the basal ganglia locks the gate to working memory](https://consensus.app/papers/details/d9a2bc7815ab5506887b840bd7bbf422/?utm_source=claude_code) (Gruber et al., 2006, J Comput Neurosci)
- [4] [Tracking Real-Time Changes in Working Memory Updating and Gating with the Event-Based Eye-Blink Rate](https://consensus.app/papers/details/25fccacf3c4755fab190388471cbfaac/?utm_source=claude_code) (Rac-Lubashevsky et al., 2017, Sci Rep)
- [5] [Prolonged Dopamine Signalling in Striatum Signals Proximity and Value of Distant Rewards](https://consensus.app/papers/details/310046782a0c5993a130a17f6c8a9471/?utm_source=claude_code) (Howe et al., 2013, Nature, 521 cites)
- [6] [Dissociable dopamine dynamics for learning and motivation](https://consensus.app/papers/details/c99ffd7a25a75b068097dc1bb684fdea/?utm_source=claude_code) (Mohebi et al., 2019, Nature, 621 cites)
- [7] [Dopamine neuron activity before action initiation gates and invigorates future movements](https://consensus.app/papers/details/6c75e9407c4f55c68cd444c926d8ae63/?utm_source=claude_code) (Alves da Silva et al., 2018, Nature, 485 cites)
- [8] [Dopamine Is Required for the Neural Representation and Control of Movement Vigor](https://consensus.app/papers/details/fe55a65ac3bf51a09171a295d6206c17/?utm_source=claude_code) (Panigrahi et al., 2015, Cell)
- [9] [Dopamine dynamics are dispensable for movement but promote reward responses](https://consensus.app/papers/details/fac6f77758b45a5c93690367a26267b4/?utm_source=claude_code) (Cai et al., 2024, Nature)
- [10] [Lateral habenula as a source of negative reward signals in dopamine neurons](https://consensus.app/papers/details/78284a5f25ee56d9afd2696e701f3606/?utm_source=claude_code) (Matsumoto & Hikosaka, 2007, Nature, 1270 cites)
- [11] [Negative reward signals from lateral habenula to dopamine neurons are mediated by RMTg](https://consensus.app/papers/details/ff08d06b3c875b7186ac15d1b589ecd6/?utm_source=claude_code) (Hong et al., 2011, J Neurosci)
- [12] [The Role of the Lateral Habenula in Inhibitory Learning from Reward Omission](https://consensus.app/papers/details/7b5cbcc964365fa1b7e90ab1bfc27709/?utm_source=claude_code) (Sosa et al., 2021, eNeuro)

*A formal ARC-106 L2 lit-pull synthesis (`evidence/literature/targeted_review_*`) is the follow-on if these anchors need to ground a registered claim's confidence; the citations above are sufficient to carry the assembly-map finding.*

---

## B. Divergence ledger (eight rows)

Active design choices that diverge from biology in a way that *may be wrong* —
distinct from the coarse-graining of §A. Ranked by likely load-bearing impact on
the live conversion-ceiling problem. **Only row B2 is currently in a divergence
ledger; B1, B3-B8 are SILENT** — an ARC-106 "zero *silent* divergence" violation
independent of whether any individual choice is ultimately correct.

Each row: REE does / nature does / why it may be wrong / symptom in REE /
tracked-where.

### B1. One-shot feed-forward `argmin`/softmax, not a recurrent settling competition  — REPAIR TARGET (see §C)
- **REE:** per-tick scoring -> `argmin` (committed) / `multinomial(softmax)` (uncommitted). Stateless, instantaneous, global.
- **Nature:** selection is a recurrent dynamical *settling* over the cortico-striatal-pallidal-thalamic loop — soft, local, mutually-inhibitory, extended in time (Cisek affordance competition; GPi tonic-inhibition -> focal disinhibition).
- **Why it may be wrong:** a hard `argmin` over an F-dominated score *always* returns the F-winner — that is the conversion ceiling. A settling competition with lateral inhibition can *flip the attractor*; an argmin can only be pre-filtered.
- **Symptom:** seven successive pre-filters bolted onto the argmin (shortlist -> envelope -> authority-rescale -> top-k) instead of the competition doing the work. ARC-107's own "thalamocortical recurrence" target is the one BG translation target named and not built.
- **Tracked:** partially — ARC-106 §6 worked example (argmin-monopoly) + ARC-107 §6b V4-axes "Thalamocortical recurrence." The *recurrent-settling-competition* framing (vs "thalamocortical oscillation") is sharper than what is there.

### B2. MECH-448 *deletes* F from the commit argmin ("behead the monarch") — TRACKED (load-bearing divergence, see §C)
- **REE:** F decides eligibility only; "F REMOVED from the final committed argmin."
- **Nature:** divisive normalisation (Carandini-Heeger; Louie/Khaw/Glimcher) is order-preserving and pooled-symmetric — the dominant value stays in the competition; the BG modulates its gain/threshold via indirect/hyperdirect.
- **Why it may be wrong:** removing the primary axis entirely is a stronger, non-biological operation than the BG performs.
- **Symptom:** endless per-channel floor recalibration (485i, 654h all-admit no-op, the 689d floor, then the mean-adaptive amend) — the adaptive-floor amend is converging back toward "relative, not absolute," i.e. back toward biology.
- **Tracked:** YES — ARC-106 §6.3 + ARC-107 §3.1 + §6b component 4 (the CDQ-003 QD/MAP-Elites justification).

### B3. Selection-as-pick vs selection-as-disinhibition; missing surround inhibition — REPAIR TARGET (see §C)
- **REE:** default = pick the best; `_modulatory_accum` is an additive blend of channel biases.
- **Nature:** default = everything inhibited (GPi tonic); selection = release the brake on one channel with **surround inhibition** of neighbours (Mink focal-Go + surround-No-Go). Surround inhibition exists precisely to prevent co-activation/blending.
- **Why it may be wrong:** the additive `_modulatory_accum` blend is exactly what surround inhibition is built to prevent — channels summing instead of one winning and suppressing rivals.
- **Symptom:** MECH-449's No-Go is a filter on an eligible set, not the surround-inhibition geometry, so it cannot deliver the clean single-channel commit disinhibition provides.
- **Tracked:** partially — ARC-106 §6.2 notes "winner emerges by disinhibition, not scalar comparison." The surround-inhibition / additive-blend-defeats-it point is NOT explicit.

### B4. Go and No-Go collapsed into one additive scalar — SILENT (enter ledger)
- **REE:** `score = f + λ·m + ρ·Φ − β·b` — benefit (Go) and harm (No-Go) summed into one cost.
- **Nature:** D1/direct and D2/indirect are parallel opponent pathways (different routing, dopamine sign, temporal profile) that remain dissociable.
- **Why it may be wrong:** additive collapse makes high-Go+high-No-Go (approach-avoidance conflict) indistinguishable from low-Go+low-No-Go (indifference) — a representational loss.
- **Psychiatric failure mode it blocks:** anxiety / approach-avoidance conflict / the OCD CSTC axis cannot be modelled because the architecture pre-sums it away (ARC-106 EARNS failure).
- **Tracked:** NO.

### B5. "Dopamine RPE" rendered as unsigned prediction-*variance* (ARC-016) — SILENT (enter ledger)
- **REE:** ARC-016 uses E3 prediction-error *variance* for precision / commit threshold — the closest thing to an RPE in the loop.
- **Nature:** dopaminergic RPE is a **signed** scalar (better/worse than expected) that drives the D1-LTP / D2-LTD asymmetry. Variance is an unsigned magnitude (a precision signal — a fine ARC-016, but not RPE).
- **Why it may be wrong:** an unsigned variance cannot supply the directional teaching term any future learned gating needs — it cannot tell Go-up from No-Go-up. A category substitution that will silently block three-factor learning.
- **Tracked:** NO (ARC-107 §6b V4-axes registers "Dopaminergic RPE learning signal" as a v4 bet but not the wrong-signal-type point).

### B6. Single *global* bistable commit latch (MECH-090) — SILENT framing (partly tracked)
- **REE:** one global bistable beta-gate for the whole agent.
- **Nature:** action maintenance is per-channel/per-effector; beta is a population rhythm, not a clean global binary.
- **Why it may be wrong:** the 460h "monolithic ~2400-step hold swamps everything" problem is the direct symptom of a *global* latch — a per-channel latch would not monopolise, and the rung-6 occupancy-release machinery would be unnecessary.
- **Tracked:** partially — ARC-106 §5 latch row notes "refractory dynamics tuned, not bio-sourced" + ARC-107 §6b component 5 OPEN. The *global-vs-per-channel* framing is NOT explicit.

### B7. MECH-260 anti-perseveration is count-based recency, not value-based switching — SILENT (enter ledger)
- **REE:** `suppression = count(action in history)/len(history)` — flat recency penalty.
- **Nature:** dACC/Scholl-Kolling anti-recency suppresses recently-*rewarded* choices when exploration is warranted — outcome/value-gated, not raw-recency-gated.
- **Why it may be wrong:** a pure count penalty suppresses a repeatedly-*correct* action just for being repeated (closer to inhibition-of-return/habituation than exploratory switching). Now propagated into the constitution because MECH-449 *reuses* MECH-260 as its perseveration No-Go axis.
- **Tracked:** NO.

### B8. Serotonin built before dopamine (modulatory partner without the principal) — SILENT (enter ledger)
- **REE:** MECH-203/204 implement the 5-HT sleep/consolidation neuromodulator; there is no dopamine substrate (confirmed — only biological-basis comments).
- **Nature:** 5-HT and DA are opponent BG neuromodulators (Cools/Dayan), but DA is the principal for the BG's core action-selection/learning function.
- **Why it may be wrong:** building the opponent before the principal is a sequencing inversion — the 5-HT modulation has nothing to oppose, and the scattered DA functions never cohere.
- **Tracked:** NO.

### The meta-pattern

Seven of these collapse to **one root deviation**: REE renders the basal ganglia
as a *stateless, feed-forward, hard-decision scoring function with hand-specified
arbitration*, when biology is a *recurrent, stateful, soft-competitive,
dopamine-learning dynamical system*. The conversion ceiling, the per-channel
floor dances, the global-latch monopoly, and the additive-blend washout are all
downstream symptoms of that one choice.

---

## C. Detailed disposition note — the top three

For each: is it a **defensible V3 simplification** (a deliberate, bounded cut we
keep) or a **genuine repair target** (a wrong choice to fix before the next
MECH-439 attack)?

### C1. Recurrent settling competition vs one-shot argmin (Deviation B1)

**Verdict: genuine repair target — and the single most likely to move the live problem.**

The argmin is not merely a coarse-graining of the BG; it is a *different
computation*. A settling competition with lateral inhibition has a property the
argmin structurally lacks: a sufficiently strong modulatory channel can flip the
selected attractor even when the primary value disagrees, because the winner is
decided by mutual inhibition over time, not by a single global comparison. This is
exactly the capability the conversion-ceiling campaign has been trying to
synthesise with a stack of pre-filters.

The evidence that this is the right repair is the *shape of the failure history*:
gain-calibration was falsified (514t regression), candidate-pool was falsified
(569h diverse-input/flat-output), and the only positive lever was *structural
bounding* (569i top-k). "Structural bounding works, parametric tuning does not" is
the signature of a system that needs a different *selection rule*, not a better
*scoring weight*. Each new pre-filter (shortlist, envelope, authority-rescale,
top-k) is an attempt to approximate, in front of the argmin, what a recurrent
competition would do natively.

**Why not just keep patching the argmin?** Because the patches compound: every new
lever needs its own per-channel calibration (the floor dances), and the
composition of levers is itself now an open experiment (the P-comp node:
demotion × Go/No-Go, interaction unknown). A recurrent competition would make the
composition emergent rather than hand-specified.

**Caveat / scope:** a full BG-thalamo-cortical settling loop is a large build and
plausibly couples to the dopamine-learning gap (A.4) — the lateral-inhibition
weights are themselves learned in biology. The minimal V3 version is a **bounded
iterative settling step** over the existing eligible set (a few rounds of
mutual-inhibition updates on `_modulatory_accum` before the commit) — strictly
more than the argmin, strictly less than a full learned loop. Recommend scoping
that minimal version as the experiment, with the full learned loop as the V4 bet.

**Disposition:** repair target; minimal-settling-step as the V3 experiment;
register as a candidate mechanism under ARC-107; sequence *after or alongside* the
dopamine-into-gating question (they are coupled).

### C2. F-deletion from the argmin exceeds canonical divisive normalisation (Deviation B2)

**Verdict: tracked load-bearing divergence; keep for now, but treat the recurring floor recalibration as the evidence it is over-strong.**

This is the one divergence already in the ledger, and it was a *deliberate,
justified* departure (the CDQ-003 QD/MAP-Elites rationale: F decides eligibility,
the modulator decides within-set order). It is not silent and not careless.

But the disposition should be updated with what the lineage has shown: a fixed
"delete F above an absolute floor" rule does not generalise across channels (485i,
654h all-admit no-op, the bespoke 689d floor), and the fix each time has pushed
the rule back toward *relative/adaptive* normalisation (the mean-adaptive floor
amend). That trajectory is REE rediscovering that the biological operation is
**learned relative re-weighting**, not absolute deletion at a floor. So:

- **Short term (V3):** keep the demotion lever — it is face-validated (689d) and
  is the only fully-landed constitution component. The adaptive floor is the right
  incremental move.
- **Medium term:** recognise that the "behead the monarch" framing is a stand-in
  for "the monarch's weight should be *learned down* in contexts where the
  modulator matters." That is the dopamine-into-gating repair (A.4 / C is coupled
  to A.4 again). When learned gating lands, the F-deletion lever should be
  re-examined: it may become unnecessary (learning re-weights F naturally) or
  reduce to a faithful pooled-symmetric normalisation.

**Disposition:** keep as tracked divergence; do *not* add more absolute-floor
letters; fold the long-term resolution into the dopamine-into-gating design note.

### C3. Selection-as-pick vs selection-as-disinhibition; additive blend vs surround inhibition (Deviation B3)

**Verdict: genuine repair target on the *blend*; the polarity itself is a defensible V3 simplification.**

Two separable claims are bundled here. Treat them differently:

- **The polarity (default-inhibit-then-disinhibit vs default-pick):** this is a
  *defensible V3 simplification*. The disinhibition architecture and the
  pick-the-eligible-winner architecture can be made behaviourally equivalent for a
  single committed action; the tonic-inhibition default mainly matters for
  multi-channel/multi-effector concurrency, which V3 does not have (one action per
  tick). Register it as a stated bet ("V3 has one effector, so default-inhibit vs
  default-pick is behaviourally equivalent") rather than a repair.

- **The additive blend (`_modulatory_accum` summing channel biases):** this is a
  *genuine repair target*, and it is the same root as B1. Surround inhibition is
  the mechanism that prevents competing channels from *co-activating/blending*;
  REE's additive sum is precisely a blend. The symptom is that the modulator field
  produces a weighted average rather than a winner, which is why a strong
  modulator dilutes into the F-dominated sum instead of capturing the commit.
  Crucially, the *minimal-settling-step* repair proposed in C1 fixes this too: a
  few rounds of mutual inhibition over the eligible set turn the additive blend
  into a competitive winner-take-most. So B3-blend and B1 should be repaired by
  the **same** V3 experiment.

**Disposition:** split the row. Polarity -> stated-bet (defensible V3
simplification). Additive blend -> repair target, **merged with C1** (the
minimal-settling-step experiment addresses both).

### Summary of dispositions

| Deviation | Disposition |
|---|---|
| B1 recurrent-vs-argmin | **repair target** — minimal settling step (V3); full loop (V4); coupled to A.4 |
| B2 F-deletion | **tracked divergence** — keep; no more floor letters; resolve via learned gating |
| B3 polarity | **defensible V3 simplification** — register as stated bet |
| B3 additive blend | **repair target** — merged into the C1 settling-step experiment |
| B4 Go/No-Go additive collapse | enter ledger; repair coupled to D1/D2 split (A.2) |
| B5 RPE-as-variance | enter ledger; repair = signed RPE in the dopamine substrate (A.4) |
| B6 global latch | enter ledger; per-channel latch is a V4 bet unless V3 multi-effector lands |
| B7 count-recency | enter ledger; repair = value-gated suppression (cheap, V3-tractable) |
| B8 5-HT before DA | enter ledger; resolved by building the dopamine substrate (A.4) |

---

## D. Open question — loop segregation

Biology runs ~5 parallel segregated cortico-BG-thalamic loops (motor,
oculomotor, dorsolateral-associative, lateral-OFC, limbic/ACC). REE collapses them
into one E3 selector, with the dACC/OFC/lPFC analogs feeding in as *biases* rather
than each owning a striatal loop. **Hypothesis worth testing:** the F-dominance
ceiling may be partly an artefact of this collapse — every channel competes in one
F-dominated arena instead of winning within its own loop and then being
arbitrated. This is registered in ARC-107 §6b as a V4 bet ("V3 collapses all loops
into one shared commitment interface"); this note flags it as a *candidate
contributor to the live problem*, which would pull it forward if the
settling-step + learned-gating repairs do not fully resolve MECH-439.

---

## E. Next steps (governance)

1. **Enter the four silent rows** (B4, B5, B7, B8) into the ARC-106 §5 living
   ledger with the load-bearing-vs-decorative ablation test + psychiatric-failure
   column; sharpen B1, B3, B6 framing in the rows that partly exist.
2. **Register the missing-piece architectural claims** into `claims.yaml` as
   candidate / substrate_conditional, wired into ARC-107 `depends_on` with the
   ARC-106 psychiatric-failure-mode column: a **unified dopamine substrate**
   (signed RPE -> learned gating + habenula drain), a **D1/D2 population split**,
   a **minimal recurrent settling step** (B1+B3-blend). (Per the intake-reap rule,
   this is the proper home for these — not future-registration prose.)
3. **Draft the dopamine *control-layer* design note** (broadened from
   "dopamine-into-gating" after the A.6 biology check). The unified dopamine
   substrate has two co-equal jobs: (a) the learned-gating teaching signal for
   *selection* (the MECH-439 attack); (b) the *control-plane driver* —
   commit-threshold (tonic/opportunity-cost), go-signal (phasic PBWM gate),
   maintenance (goal-proximity ramp), and de-commit (habenula negative RPE).
   Highest-leverage item; resolves A.4, A.6, B2-long-term, B5, B6, B8 — and is a
   concrete candidate fix for the parked rung-6 de-commit problem (A.6
   implication 2). **DONE 2026-06-22:**
   [`dopamine_into_gating_design_2026-06-22.md`](dopamine_into_gating_design_2026-06-22.md)
   — decision: **build the minimal learned gate (signed-RPE δ_t → learned
   per-channel selection weight `w_chan`, distinct from ARC-016 unsigned variance
   B5), COMPOSED on the arithmetic envelope (not replacing it), COUPLED to a
   minimal learned-`W_lat` settling step (B1+B3-blend); pre-registered 2×2
   falsifier with a signed-vs-unsigned ablation; V3-minimal vs V4-full-loop scope
   bet.** PROMOTES NOTHING; claim-mint is the §8 follow-on.
4. **Hold** the loop-segregation (§D) and the cognitive-loop gating drain as V4
   bets unless (1)-(3) leave MECH-439 unresolved.

---

*Derived 2026-06-22 from a session BG overview grounded against
`ree-v3/ree_core/predictors/e3_selector.py` + the ARC-107 lineage. Companion to
`arc_107_selector_constitution_design_2026-06-20.md` (§6b completeness tracker)
and `docs/architecture/arc_106_biology_grounding_framework.md` (§5 living
divergence ledger).*
