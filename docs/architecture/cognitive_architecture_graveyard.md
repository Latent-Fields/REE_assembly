---
title: Cognitive-Architecture Graveyard — Anti-Patterns REE Must Avoid
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 6
---

# Cognitive-Architecture Graveyard — Anti-Patterns REE Must Avoid

**Created:** 2026-07-09
**Status:** first pass (WS-8 of `evidence/planning/ree_ai_design_critique_plan.md`)
**Purpose:** REE is an "integrate everything into one mind" architecture. That bet has a graveyard. Soar and ACT-R are the two longest-running integrated cognitive architectures in the field; LeCun's 2022 *A Path Towards Autonomous Machine Intelligence* (AMI) is the most cited recent integrated blueprint — and largely *unbuilt*. Studying **how each hit its ceiling** is the cheapest available way to avoid repeating it. This doc extracts concrete anti-patterns and maps each to a specific REE exposure, with special attention to the **governance-mass-vs-cognitive-mass ratio** flagged in the source critique.

**PROMOTES NOTHING.** This is a strategic/architecture study, not a claim change. Nothing here weakens or promotes a registry claim; it defines *risks* and *falsifiable health metrics* the project can watch.

**Caveat.** Written from the primary-source literature plus a light web pass; per-source `/lit-pull` confirmation of the exact critiques is owed before any row is used to justify a governance or substrate change. Treat the historical readings as *load-bearing but un-lit-pulled*.

---

## The thesis in one paragraph

Every integrated cognitive architecture faces the same trap: **structure is cheap to specify and expensive to make competent.** You can draw the boxes — perception, world model, memory, arbitration, a control plane on top — long before any of them earns capability. The graveyard is full of architectures whose *elaboration outpaced their demonstrated competence*, and which the field then walked past because scale-plus-learning delivered the capability the hand-built structure kept promising. Soar and ACT-R spent four decades each becoming ever more architecturally complete while remaining bespoke-per-task and hard to scale; LeCun's AMI is the same elegance frozen one step earlier — a complete diagram whose hardest, most load-bearing module was never built. REE's own conversion-ceiling finding (the fully-integrated all-ON agent forages *below the competence floor* — 0.065 / 0.0 / 0.455 resources/ep on 0/3 seeds; see `failure_autopsy_V3-EXQ-719a`) is this exact trap biting in real time. The graveyard is not a warning about *whether* to integrate — it is a warning about the *order of operations* and the *ratio of bookkeeping to cognition*.

---

## Case study 1 — Soar (Laird, Newell, Rosenbloom)

**What it was.** The purest realization of Newell's "unified theory of cognition." A production-rule system built on the *problem-space hypothesis* (all deliberate behaviour = search in problem spaces), *universal subgoaling* (impasses automatically spawn subgoals), and **chunking** as the single, universal learning mechanism (Laird, Newell & Rosenbloom 1987). One elegant loop, meant to explain everything.

**How it hit its ceiling.**

1. **The knowledge-engineering bottleneck never closed.** Behaviour lived in hand-written productions. Every new competence was a human authoring rules. Chunking was supposed to be the escape hatch — learning would compile experience into new rules — but chunking only *caches* problem-solving the system already did; it does not learn new concepts, new categories, or new perceptual structure (the standard critique; see the knowledge-level analyses below). So the human stayed in the loop for everything genuinely new.

2. **The utility problem: learned structure that made the system *slower*.** Soar's own learning mechanism could degrade performance. Newly chunked rules enlarge the match set; Rete match cost grows with rule count and rule expressiveness, so a system that "learned" could end up *slower* than before — the **expensive-chunks** problem (Tambe, Newell & Rosenbloom 1990; Doorenbos 1993 on match cost at scale). This is the cleanest historical proof that *adding a mechanism to an integrated architecture does not monotonically add capability* — it can subtract it.

3. **Module accretion.** The clean 1987 loop did not stay clean. Over the following decades Soar bolted on reinforcement learning, semantic memory, episodic memory, appraisal-based emotion, mental imagery, and a **Spatial-Visual System (SVS)** to connect symbols to perception (Laird 2012). Each module closed a gap the previous architecture could not — and each was an admission that the "one universal mechanism" story was incomplete. The recurring external verdict: *too many components; simpler architectures might do as well.*

4. **Symbol grounding as a permanent add-on.** Perception was never native to the symbolic core; SVS was grafted on precisely because the productions had no way to touch continuous space. The symbol/subsymbol seam stayed a seam.

**Concrete anti-patterns (AP-Soar):**
- **AP-1 (hand-authored structure):** competence lives in hand-written units the human must keep writing.
- **AP-2 (learned structure can degrade):** a system's own learning mechanism can lower capability (utility problem).
- **AP-3 (module accretion):** the architecture grows by bolting on modules to patch gaps; integration cost and interference compound.
- **AP-4 (bolted-on grounding):** perception/continuous structure is grafted onto a symbolic core rather than native to it.

---

## Case study 2 — ACT-R (Anderson)

**What it was.** The most empirically successful integrated architecture: a **hybrid** system where discrete production rules (symbolic) fire over modules whose availability is governed by continuous **subsymbolic** equations — base-level activation, spreading activation, production utility, partial matching, latency (Anderson et al. 2004). It fits human reaction-time and error data across hundreds of paradigms. Where Soar chased generality, ACT-R chased *fit to human data*.

**How it hit its ceiling.**

1. **The degrees-of-freedom / identifiability critique.** The subsymbolic layer that makes ACT-R fit so well is also a bank of free parameters. A rich enough model with enough knobs can be tuned to fit almost any RT/accuracy curve, so a good fit is weak evidence for the mechanism (the general form of Roberts & Pashler 2000, *How persuasive is a good fit?*). ACT-R defenders answer that parameters are documented, interdependent, and mostly fixed across models — a *real* defence — but the tension never fully resolves: **a model flexible enough to explain everything explains nothing in particular.**

2. **Models don't compose; each is bespoke.** The architecture is general, but each *published ACT-R model is a hand-built fit to one task* — its productions written for that paradigm, its free parameters tuned to that dataset. There is no ACT-R agent that walks up to a new task and is competent; there is a *modelling methodology* that a researcher applies, per task, by hand. The generality is in the framework, not in any running agent.

3. **The serial-production bottleneck.** ACT-R fires one production per ~50 ms cycle. That serial spine is load-bearing for its timing predictions but structurally cannot capture massively parallel perception or fast subsymbolic pattern completion — a hard architectural commitment that ages badly against learned, parallel systems.

**Concrete anti-patterns (AP-ACT-R):**
- **AP-5 (identifiability / never-loses):** enough free structure that the theory can always be re-tuned to fit, so failures don't falsify — they get absorbed into parameter settings.
- **AP-6 (bespoke-per-task, no transfer):** generality lives in the *framework*, capability must be re-hand-built for each task; no single agent is competent across tasks.
- **AP-7 (load-bearing hard commitment):** a structural choice (serial spine) that carries the theory but caps what it can ever represent.

---

## Case study 3 — LeCun's 2022 AMI blueprint (largely unbuilt)

**What it is.** A modular, fully-integrated design for an autonomous agent: a **configurator** (central controller that reconfigures every other module per task), perception, a **world model** (hierarchical JEPA — joint-embedding predictive architecture), a **cost module** (fixed intrinsic cost + trainable critic), short-term memory, and an actor; with a Mode-2 (deliberative planning) → Mode-1 (reactive) distillation story (LeCun 2022, v0.9.2). It is the most influential recent statement of the integrated-mind bet.

**How it hit its ceiling — before it was even built.**

1. **Only the tractable module got built.** JEPA is real and productive: I-JEPA, V-JEPA, V-JEPA 2 followed. But the *agent* — the integration of all six modules into one autonomous loop — was **not built out**. The blueprint remains, four years on, mostly a position paper.

2. **The hardest module was hand-waved.** The **configurator** is the linchpin: it is what makes the architecture an *agent* rather than a pile of modules, because it sets every other module's parameters and goals per situation. It is also the least specified part of the paper — no learning rule, no concrete mechanism, no implementation. The elegant diagram spent its precision on the parts that were already tractable (the world model) and left the load-bearing controller as a box with an arrow.

3. **The lesson is the cheapest one in the graveyard.** An integrated blueprint is *cheap to draw and cheap to admire*. The gap between "here is the complete architecture of a mind" and "here is a competent agent" is almost entirely in the modules you were most tempted to hand-wave — the controller that has to make the integration actually pay.

**Concrete anti-patterns (AP-AMI):**
- **AP-8 (the beautiful unbuilt whole):** a complete, elegant, integrated diagram substitutes for a demonstrated capability; admiration of the design displaces building it.
- **AP-9 (hand-waved linchpin):** the module that makes integration *pay* (the controller) is the one left least specified, because it is the hardest.

---

## The core deliverable — anti-pattern → REE exposure

Each row: the graveyard anti-pattern, the specific REE surface that is exposed to it, the *evidence it may already be biting*, and a **falsifiable health metric** to watch.

| # | Anti-pattern | REE exposure | Is it biting yet? | Health metric to watch |
|---|---|---|---|---|
| AP-1 | Hand-authored structure the human keeps writing | 871 hand-authored claims; every MECH/ARC is human-specified structure. This is the maximal version of the Soar bottleneck. | **Partially.** WS-6 (Bitter-Lesson rebuttal) is the open answer. The competence floor (WS-1) is "structure specified faster than capability was earned." | Ratio of claims that have *lifted a capability metric on a competent substrate* to claims *registered*. Currently near-zero on the conversion-ceiling lineage. |
| AP-2 | A mechanism can *subtract* capability | The all-ON stack. Adding E1/E2/E3 + commitment gating did **not** monotonically help — the integrated agent forages *worse than the 1.0 floor* (`failure_autopsy_V3-EXQ-719a`). | **Yes — confirmed.** This is Soar's expensive-chunks problem in REE's own data: integration overhead is currently *negative*. | Per-mechanism capability delta on a substrate already above the competence floor (the WS-3 yardstick). Any mechanism whose ON delta is ≤ 0 is an expensive chunk. |
| AP-3 | Module accretion / interference | Steady stream of no-op-default substrate flags: `cross_stream_binder`, disinhibitory settling, ascending-spiral gain, `use_closure_commit_entry`, MEL consumer… each closes one gap. | **At risk.** Interference is exactly where the all-ON stack fails; each new flag enlarges the interaction surface the all-ON run must survive. | Number of *always-OFF-in-practice* flags (built, never lifted anything) vs flags with a positive validated ON result. The former is accreted dead mass. |
| AP-4 | Bolted-on grounding / symbol-subsymbol seam | REE imposes *typed* structure — the commit boundary (MECH-061), the imagination/real tag (MECH-094), incommensurable channels (ARC-021), discrete `committed_class` selection in E3 — on a learned z_world that may not carry the structure. | **Likely biting.** 719a's dominant diagnosis is a *behavioural-competence / training-regime* gap: thin P1 (90-ep bias-head-only REINFORCE, **frozen encoder**). The typed selection sits on top of a perception loop that was never trained to be competent. That is a symbol-grounding failure in REE dialect. | Does capability survive when the encoder is *trained end-to-end* rather than frozen? If typed structure only works on a hand-frozen substrate, the seam is unearned. |
| AP-5 | Identifiability / the theory that never loses | 34 claims carry `substrate_ceiling`, 64 carry `pending_retest_after_substrate`; a failed discrimination is explicitly *not* a falsification; 72% of 871 claims are `candidate`. | **Structurally present; partially mitigated.** This is precisely the ACT-R degrees-of-freedom critique at the registry level. Per-arm envelope-floor calibration adds more knobs. | The WS-2 demotion rule: is any claim *ever demoted* for hitting the ceiling N times without a positive result? If the count of ceiling-demotions stays 0 while the ceiling-parked count grows, the registry is an unfalsifiable ACT-R. |
| AP-6 | Bespoke-per-task, no transfer | Each experiment is a hand-built script + hand-tuned readiness gates + per-(arm,seed) calibration, fitting one narrow question. No agent is competent across the task family. | **Yes.** There is no REE agent that is competent on CausalGridWorld *and* transfers; there is a methodology applied per experiment. Same shape as "ACT-R has models, not an agent." | Existence of a *single frozen agent* that clears the WS-3 capability suite across ≥2 task variants without per-task re-tuning. Currently: none. |
| AP-7 | Load-bearing hard commitment that caps representation | The strong incommensurable-channels claim (ARC-021: the three channels *cannot* share a scalar) and the hard typed commit boundary are structural commitments carrying much of the theory. | **Watch.** These are REE's genuine bets; the risk is they become the serial-spine — right for the story, wrong for capability under scale. | Is the incommensurability *demonstrated to buy capability*, or asserted? A forced-shared-loss ablation that shows collapse (see WS-4 MECH-069 row) would earn it; absence of that test leaves it a hard commitment on faith. |
| AP-8 | The beautiful unbuilt whole | REE's philosophical payoff — ethics from modelling others as self-like, love as mechanism — is **V5, multi-agent, and untouched by running code** (WS-10). The axioms do philosophical, not computational, work. | **Yes — this is the AMI trap exactly.** The most load-bearing part of the thesis is the least built. | Fraction of the *central thesis* (the ethics/social claims) with *any* executing code putting load on it. Currently ≈ 0 (single-agent V3). WS-10's minimal 2-agent world is the first down-payment. |
| AP-9 | Hand-waved linchpin (the controller that makes integration pay) | REE's control plane — modes as regimes over shared machinery (ARC-016), the precision→commitment configurator — is the analogue of LeCun's configurator: the thing that has to make the integration *pay*. | **At risk.** If capability only appears when a human hand-configures the arms/phasing per experiment, the "control plane" is doing what the researcher does, not what an autonomous configurator would. | Can the mode/precision control plane *select its own regime* and thereby lift a capability metric, with no per-experiment hand-configuration? If not, the linchpin is still a box with an arrow. |

---

## The special one — governance-mass vs cognitive-mass

The source critique's sharpest single observation: **REE spends heavily on claim-registry / queue / sync machinery.** This is a *different* mass sink from anything in the classical graveyard, and it deserves its own reading.

**What each architecture spent its mass on.**
- **Soar / ACT-R** spent their mass on **knowledge** — productions, models, parameter sets. That is *cognitive* mass: units that (attempt to) directly produce behaviour. Their failure was that cognitive mass grew faster than demonstrated competence.
- **REE** carries that same cognitive-mass load (871 claims are the direct analogue of Soar's rule base) **plus a second, unusual mass sink: the coordination and governance apparatus itself** — `claims.yaml` + the `governance.sh` derive pipeline, the experiment queue + validators, the coordinator/`sync_daemon` (by the critique's own count, ~60–77% of recent `master`/`main` commits are *machine-written coordination data*), `TASK_CLAIMS`, `review_tracker`, the IGW routine, closure dashboards, evidence manifests, the promotion/demotion machinery. This is **meta-mass: effort spent managing the theory rather than producing cognition.**

**Why this is a distinct risk, not just "more overhead."** In Soar, every unit of mass at least *tried* to be behaviour. In REE, a large fraction of total mass is bookkeeping *about* the claims — claims about claims, evidence about evidence, the accounting of an epistemic project. The graveyard warning specializes to: **a cognitive architecture whose commits are mostly coordination data and whose artifacts are mostly claims-about-claims is at risk of being an elaborate epistemic-accounting system wrapped around a thin cognitive core** — and the thin cognitive core here is the V3 agent that cannot forage above the 1.0 floor.

**The health metric this yields.** Define, roughly:

> **governance-mass : cognitive-mass** ≈ (effort in registry + queue + sync + governance derive + review bookkeeping) : (effort that moved a *capability metric* on a competent substrate).

The critique's estimate that most commits are coordination data means this ratio is currently **very high**. That is not automatically fatal — much of the coordination mass is *machine-generated* by `sync_daemon`, which is cheap to emit. But cheap-to-emit is not free: it is still (a) attention mass for every human and agent who must read, reconcile, and not-corrupt it, and (b) a standing temptation to mistake *governance activity* (a governance cycle ran, a claim was registered, a brake fired) for *cognitive progress* (the agent got more competent). The two can — and on the conversion-ceiling lineage currently **do** — move in opposite directions: governance is busy and rigorous while foraging competence sits at zero.

**The falsifiable form.** REE should be able to answer, at any time: *"In the last N cycles, how much of our mass moved a capability metric versus managed the registry?"* If, cycle after cycle, the answer is "governance was active, capability was flat," the architecture is spending its life the way late-period Soar did — becoming ever more complete and self-consistent while the field's capability frontier moves elsewhere (WS-6's Bitter Lesson). **The governance mass is only justified if it is demonstrably *in service of* earning capability — as a falsification engine that kills dead structure — and not a substitute for it.**

---

## Where REE already has antibodies (the honest other side)

The graveyard is a warning, not a verdict. REE has three defences the classical architectures lacked — each real, each incomplete:

1. **An explicit falsification/brake apparatus.** Re-derive brakes, the `substrate_ceiling` vs falsification distinction, and the WS-2 demotion rule are a direct antidote to the ACT-R "never-loses" problem (AP-5) — *if enforced*. The 21×-fired ARC-062 brake shows the machinery runs. The open question (WS-2) is whether it ever *demotes*, not just *parks*.

2. **A learned substrate, not a pure production system.** REE builds on torch, learned encoders, and JEPA-style E1/E2 world models — it is not Soar's hand-written-rules-all-the-way-down. This blunts AP-1/AP-4 *in principle*. The exposure (AP-4) is specifically the **typed structure imposed on top** of the learned substrate, and the **frozen encoder** in the failing training regime — i.e. REE is currently running its learned substrate in a *hand-frozen* mode that forfeits this antibody.

3. **No-op-default flag discipline + the flag-inertness harness** (`ree-v3/tests/test_flag_inertness.py`, landed 2026-07-09) is a real antidote to AP-3 module-accretion interference: every new flag is byte-identical OFF, so accretion cannot silently corrupt the baseline. Its limit: inertness proves a flag *does no harm when OFF*, not that it *does good when ON*. Dead-but-inert mass is still mass (AP-3's health metric above).

4. **Bottleneck fan-out over sequential retry** (`GOV-FANOUT-1`, landed 2026-07-10). The graveyard's subtlest failure is *sequential retry*: when a discrimination is stuck, the reflex is one more re-posed lettered probe — which burns compute circling one root (the 719a→724→732→732a competence chain) and, worse, can inherit the prior confound and return a confident-but-wrong verdict that then gets *built on*. That is AP-3/AP-6 in the experiment stream — motion mistaken for progress. GOV-FANOUT-1 is the antidote: when a brake fires on a discrimination, escalate to a **diverse parallel portfolio** (≥K legs on different design axes, each with a declared null, design-audited for coverage + verdict-aliasing before queuing). Its limit: the rule forces the *reflex* and the *audit*, but the *axes* still take judgment. Unlike antibodies 1–3, its first application already acted — the 737/738/739 portfolio, where the cheapest leg (P-B) refuted H2 before the sequential chain could have produced any answer.

The pattern across all four: REE has *built the antibody* and must now *let it act*. A demotion rule that never demotes, a learned substrate run frozen, and an inertness harness that never asks "did ON help" are antibodies held in reserve — GOV-FANOUT-1 is the one that has already fired once, and the test is whether the *next* bottleneck triggers a fan-out without a human prompting it.

---

## Recommendations (falsifiable, cheap, no substrate needed)

1. **Adopt the two health ratios as first-class, reported numbers** — `capability-earning claims : registered claims` and `governance-mass : cognitive-mass` — surfaced alongside the closure dashboard. Making the ratio *visible* is the whole mitigation; you cannot manage the graveyard's central failure if you never measure it. **[Implemented 2026-07-09.]** Ratio #2 is now live on the closure dashboard (`docs/closure_dashboard.md`, regenerated every governance run) via `scripts/graveyard_health_ratios.py` — the cheap commit-classification proxy (currently **65 %** of commits are machine-written coordination data; **~22 : 1** governance-mass : cognitive-mass by the coarse prefix bucketing). Ratio #1's *denominator* (registered claims) reports now; its *numerator* is not yet measurable and is scoped in the design note below (§ *Ratio #1 — the missing capability-earning flag*).
2. **Feed AP-2 / AP-4 straight into WS-1.** The competence-floor experiment should explicitly test the *frozen-encoder* hypothesis: does end-to-end training clear the floor the typed structure sits on? That is the symbol-grounding test in REE dialect.
3. **Wire AP-5 into WS-2.** The demotion rule is only an antibody if the ceiling-demotion count can go above zero. Pre-register N.
4. **Name the configurator risk (AP-9) against the control plane (ARC-016).** Before building more of the mode/precision machinery, state the falsifier: *can the control plane select its own regime and lift a metric with no per-experiment hand-configuration?* If not, it is LeCun's configurator.
5. **Treat AP-8 as the reason WS-10 exists.** The ethics thesis being untouched by code is the single most AMI-shaped exposure REE has; the minimal 2-agent world is the down-payment that keeps it from being a beautiful unbuilt whole.

---

## Ratio #1 — the missing capability-earning flag (design note)

Ratio #2 (governance-mass : cognitive-mass) was computable from `git log` the day it was proposed — commit prefixes already carry the signal. Ratio #1 (**capability-earning claims : registered claims**) is not, and the gap is itself diagnostic: **REE tracks whether a claim has been *registered, reviewed, promoted, demoted, or ceiling-parked* in fine detail, but has no field for whether it ever *lifted a capability metric*.** The registry measures its own epistemic bookkeeping, not cognition delivered. That absence is the AP-1/AP-5 exposure made concrete.

**What the numerator means (precise definition).** A registered claim is *capability-earning* iff there exists at least one experiment in which the claim's mechanism, switched **ON**, produced a **positive** delta on a claim-agnostic capability metric (foraging competence, survival horizon, goal-reach rate, planning depth — the WS-3 yardstick suite) on a substrate that is **already above the competence floor** (WS-1). Both qualifiers are load-bearing:
- *Positive ON-delta* rules out flags that are merely inert-when-OFF (the flag-inertness harness proves no-harm-OFF; it says nothing about good-ON). A capability-earning claim must have *done good when ON*, not just *no harm when OFF*.
- *On a competent substrate* rules out the conversion-ceiling trap, where a mechanism's "lift" is measured on a hand-frozen substrate that never cleared the floor (AP-4). A lift on an incompetent substrate is unearned.

**Why it is ~0 today.** On the live conversion-ceiling lineage the all-ON agent forages *below* the 1.0 competence floor (`failure_autopsy_V3-EXQ-719a`), so no ON-delta measured there is "above the floor." Selection-face lifts (MECH-448/449 on GAP-A) exist but on a substrate not shown competent at the foraging task. The honest current numerator is therefore near-zero — which is exactly the number the graveyard predicts and exactly why it must be *visible*, not hidden inside per-experiment manifests.

**The missing field (proposed schema, PROMOTES NOTHING to add).** A per-claim, evidence-backed record — not a hand-set boolean:

```yaml
capability_lift:            # optional; absent == not-yet-earned (numerator excludes it)
  earned: true
  metric: foraging_competence        # one of the WS-3 yardstick metrics
  on_delta: 0.42                      # positive ON-minus-OFF delta on the metric
  substrate_run_id: v3_exq_NNN_..._v3 # the run that measured it
  above_competence_floor: true        # substrate cleared the WS-1 floor in that run
  recorded_by: <governance cycle / failure_autopsy id>
```

**How it gets populated (not by hand).** The flag is *derived*, mirroring how `evidence_direction` and the ceiling audit already work:
1. WS-3 lands the capability-eval block so every experiment reports the yardstick metrics + whether the substrate cleared the floor (already in flight as `ree-v3/experiments/_lib/capability_eval.py`, V3-EXQ-727).
2. A governance-side derive step (extend `check_substrate_ceiling_audit.py` or add a sibling) scans confirmed `failure_autopsy_*.json` + reviewed manifests for `(claim_id, metric, on_delta > 0, above_floor == true)` tuples and writes `capability_lift` onto the matching claim.
3. `scripts/graveyard_health_ratios.py` `count_registered_claims()` already reports the denominator; add a `count_capability_earning_claims()` that counts `capability_lift.earned == true` and the ratio completes itself — no schema change to this script's public surface.

**Gate.** Step 1 (WS-3) is the prerequisite: you cannot mark a claim capability-earning until there is a substrate above the floor to measure the lift against. Until then the dashboard honestly reports the numerator as **UNMEASURED** and the denominator as the live registered-claim count. That honesty *is* the instrument — a blank numerator against a four-digit denominator is the graveyard warning in one line.

---

## Cross-links

- **Source roadmap:** `evidence/planning/ree_ai_design_critique_plan.md` (WS-8; pairs with WS-1 competence floor, WS-2 demotion rule, WS-3 capability yardstick, WS-6 Bitter-Lesson rebuttal, WS-10 minimal 2-agent world).
- **Sibling deliverable:** `docs/architecture/formal_ancestor_mapping.md` (WS-4) — where the graveyard maps the *failure modes*, WS-4 maps the *formal ancestry*; AP-7 (incommensurable channels) and the JEPA E1/E2 row are the shared seams.
- **The bite, in REE's own evidence:** `evidence/planning/failure_autopsy_V3-EXQ-719a_2026-07-08.md` — the all-ON competence floor is AP-2 + AP-4 in the project's own data.

---

## Sources (primary; per-source `/lit-pull` confirmation owed)

- Laird, Newell & Rosenbloom (1987). *Soar: An Architecture for General Intelligence.* Artificial Intelligence 33(1).
- Tambe, Newell & Rosenbloom (1990). *The problem of expensive chunks and its solution by restricting expressiveness.* Machine Learning 5.
- Doorenbos (1993). *Matching 100,000 learned rules* (Rete match cost at scale). AAAI.
- Laird (2012). *The Soar Cognitive Architecture.* MIT Press (the module-accretion record: RL, semantic/episodic memory, appraisal, SVS).
- Lieto, Lebiere & Oltramari (2018). *The knowledge level in cognitive architectures: current limitations and possible developments.* Cognitive Systems Research 48 (Soar/ACT-R knowledge-level critique).
- Anderson, Bothell, Byrne, Douglass, Lebiere & Qin (2004). *An integrated theory of the mind.* Psychological Review 111(4) (ACT-R hybrid symbolic/subsymbolic).
- Roberts & Pashler (2000). *How persuasive is a good fit? A comment on theory testing.* Psychological Review 107(2) (the degrees-of-freedom critique).
- LeCun (2022). *A Path Towards Autonomous Machine Intelligence*, v0.9.2, OpenReview `BZ5a1r-kVsf` (the AMI blueprint; configurator + cost module + H-JEPA).
- Web pass (2026-07-09): Lieto et al. knowledge-level limitations ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1389041716302121)); ACT-R degrees-of-freedom debate ([arXiv 2410.18055](https://arxiv.org/pdf/2410.18055)); AMI reviews ([OpenReview PDF](https://openreview.net/pdf?id=BZ5a1r-kVsf), [Shaped](https://www.shaped.ai/blog/yann-lecun-a-path-towards-autonomous-machine-intelligence)).
