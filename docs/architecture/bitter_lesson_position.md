---
title: "Bitter-Lesson Position — Why Scale + Search Should Not Eat REE's Structure (and Where It Should)"
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 3
---

# Bitter-Lesson Position — Why Scale + Search Should Not Eat REE's Structure (and Where It Should)

**Created:** 2026-07-09
**Status:** first pass (WS-6 of `evidence/planning/ree_ai_design_critique_plan.md`)
**Companion:** `docs/architecture/formal_ancestor_mapping.md` (WS-4) — supplies the "what stays novel" set this doc turns into a falsifiable bet.
**Promotes/demotes:** nothing. This is a strategic position doc, not a claim. It defines a *demotion discipline* the project should hold itself to; it does not itself change any claim's status.

---

## The question, stated so it can hurt

REE is the maximally structure-first bet in contemporary AI. It carries ~871 hand-authored claims, an architecture specified in advance of the capability that would justify it, and an explicit governance reflex — "demote drift back to biology" — that treats hand-engineered biological structure as the thing to protect. Sutton's **Bitter Lesson** (2019) is the standing argument that this is exactly the class of bet that loses: over seventy years, general methods that scale with computation — **search** and **learning** — have repeatedly and decisively beaten methods that build in human knowledge of the domain [Sutton 2019]. Chess knowledge-engineering lost to search; hand-crafted speech and vision features lost to statistical learning and then deep learning; Go lost to self-play + scaled search.

The uncomfortable local datapoint: the conversion-ceiling campaign's own terminal finding is that the fully-integrated all-ON agent is not behaviourally *competent* — it forages 0.065 / 0.0 / 0.455 resources/episode, below the 1.0 floor, on 0/3 seeds (`failure_autopsy_V3-EXQ-719a_2026-07-08`; `conversion_ceiling_campaign_plan.md`). Structure was specified faster than capability was earned. **That is the Bitter Lesson biting.** A position doc that pretends otherwise is worthless.

So: *why won't scale + search eat this structure?* The honest answer is **most of it should, and the project's job is to let it.** What survives is a small, named, falsifiable set. This doc partitions REE into the part that claims to be a scale-invariant prior and the part that is scaffolding scale is entitled to replace — and states, for each surviving item, the observation that would demote it.

---

## Steelman: the Bitter Lesson, in its strong form

Do not caricature Sutton. The essay is not "structure is bad." Its actual claims are sharper and harder to escape:

1. **Compute grows exponentially and cheaply; human insight does not.** Any capability you get by hand-encoding domain knowledge is a fixed deposit; any capability you get from a method that scales with compute compounds. Over a long enough horizon the scaling method wins by an arbitrary margin, and the horizon keeps getting shorter.
2. **Hand-encoded knowledge actively blocks scaling.** It is not merely that structure fails to help — it "tends to plateau" and gets in the way of methods that would otherwise ride the compute curve. The knowledge-engineered chess and Go systems did not just lose; they *capped* the systems that carried them.
3. **The contents of the mind are "irredeemably complex."** We keep trying to build in *how we think we think* — objects, symbols, spatial relations, our own introspective categories. Sutton's claim is that this content is not a shortcut; it is a decoy. What we should build in is **not the discoveries but the meta-methods that can find them**: general mechanisms for search and learning that can discover arbitrary complexity, so the system can find structure "like we can" rather than being handed the structure we already found.

Point 3 is the one REE must answer directly, because 871 claims *look exactly like* building in the contents of the mind. And points 1-2 are empirically live right now: through 2024-2025, frontier scaling did not politely plateau at the door of "reasoning" — it walked through it (below).

**The strongest single piece of recent evidence for Sutton.** ARC-AGI-1 was designed by Chollet specifically to resist scale — a benchmark on which memorization and brute pattern-matching should fail and only genuine skill-acquisition efficiency should pass. In December 2024, OpenAI's o3 scored **87.5%** on it, tripling the prior best [ARC Prize 2024]. Scale + test-time search ate a benchmark expressly built to be un-eatable by scale. If a priors-benchmark falls to compute, why should REE's priors survive?

**Take this as decisive-looking and keep reading.** The rebuttal is not that o3 failed. It is what the win *cost*, and where it stopped.

---

## The rebuttals that actually hold

### 1. No Free Lunch: "zero priors" is not on the menu; only *which* priors

Chollet's **On the Measure of Intelligence** (2019, arXiv:1911.01547) reframes the whole debate. Intelligence is **skill-acquisition efficiency** measured *relative to priors, experience, and generalization difficulty*. His central lemma, downstream of the No-Free-Lunch theorems: **unlimited priors *or* unlimited experience both let you "buy" arbitrary skill in a way that masks a system's actual generalization power** [Chollet 2019]. Scale is the second lever. Buying skill with 172× compute is the same category of move as buying it with hand-coded rules — it inflates *skill* without demonstrating *efficient generalization*.

The consequence is fatal to the naive Bitter-Lesson reading: there is no priors-free system. A scaled transformer has enormous, opaque, *implicit* priors baked into its architecture and data distribution. The real question was never "structure vs no structure." It is **"which priors are general enough to pay for themselves across a wide scope of tasks, at bounded cost."** Chollet's own answer — the **Core Knowledge priors** (objectness, agentness, elementary number, elementary geometry/topology) — is that a *small, ancient, general* set of priors is exactly what makes efficient generalization possible [Chollet 2019; Spelke & Kinzler 2007]. That is a structure-first thesis, from the person who built the benchmark scale just "beat."

### 2. The o3-on-ARC hinge cuts *for* the priors argument, not against it

Read the December 2024 result completely:

- o3 hit 87.5% only in a high-compute configuration using **1,024 samples per task at ~$4,500 per task**, roughly **172× the compute** of its own low-compute setting [ARC Prize 2024].
- On **ARC-AGI-2** (2025), redesigned to defeat exactly this brute-search strategy, the best o3 configuration scored **under 3%** [ARC Prize 2025; arXiv:2505.11831].

This is the cleanest empirical statement available of *some priors pay*: the search **did not acquire the general prior**. It pattern-matched harder, at a cost that scales with the task's search space, and when the next benchmark closed the specific loophole the capability evaporated. **The right prior is precisely the thing that converts unbounded, cost-scaling search into bounded, transferable competence.** A system with the object/agent/number priors solves ARC tasks cheaply and transfers; a system without them can be dragged to the same score by 172× compute but does not transfer one benchmark over. That gap is the entire value proposition of structure, measured in dollars.

### 3. Sutton's own carve-out: meta-structure is *endorsed*, not forbidden

Point 3 of the steelman says: build in the meta-methods, not the discovered contents. This is a scalpel, not a hammer, and it cuts REE into exactly two pieces. A hand-authored *mechanism that lets the system discover and own its consequences* is meta-structure — the kind Sutton says to build in. A hand-authored *table of what the consequences are* is discovered content — the kind he says to leave to search. The Bitter Lesson does not tell you to delete structure; it tells you **which** structure to delete. The partition below is that cut applied honestly.

---

## The partition (the actual deliverable)

REE's structure divides into three bins. The discipline is: **default items to (ii); admit an item to (i) only with a stated falsifier; carry (grey) items as open bets with equal weight on the sceptical reading.**

### Bin (i) — Claimed scale-invariant priors: scale should *not* be able to replace these

The candidate set is the "what should stay novel" list from `formal_ancestor_mapping.md` §"What should stay novel". The claim for admission to (i) is uniform and specific: **each is a constraint on the optimizer, or a property of the objective itself — not a function the optimizer produces from more data.** Scale + search optimizes a fixed objective over a fixed distribution; it cannot manufacture a structure whose defining property is orthogonal to, or in tension with, that optimization.

| # | Structure | Why scale should not produce it | **Falsifier (what demotes it to (ii))** |
|---|-----------|--------------------------------|------------------------------------------|
| i.1 | **The residue field** — persistent, non-erasable, owned-consequence traces written at the `z_world` location of a committed action, reshaping the terrain future trajectories are scored against (REE's model of guilt/regret/moral learning). | Non-erasability is an **anti-optimization constraint**. Gradient descent's entire function is to reduce a loss — to *erase* whatever does not lower it. A trace that must persist *against* optimization pressure, cannot be zeroed, optimized away, or reset between episodes, is by construction not something more optimization yields. RL has no primitive for a memory the optimizer is forbidden to remove. It is a constraint imposed *on* the learner, not a capability *of* the learner. | A purely scaled RL/search agent, with no architectural residue primitive, spontaneously develops persistent owned-consequence representations that (a) survive optimization pressure and episode resets and (b) reshape future valuation in the residue-field's direction. If more compute *induces* non-erasable ownership, the prior is redundant. |
| i.2 | **The commit boundary + hypothesis tag** as a first-class typed object (MECH-061/MECH-094) — the structural difference between imagined harm and committed harm; the boundary where simulation becomes owned action; whose failure mode is a *named pathology* (confabulation = sim encoded as real). | Scale learns to *predict*. The claim is that prediction alone cannot manufacture the **agency/ownership boundary** that makes some predictions "committed" and others "merely imagined." Dyna and model-based RL already separate imagined from real — by bookkeeping, invisibly. REE's claim is that the boundary is *load-bearing*: remove the tag and you do not get a slightly worse predictor, you get a *specific pathology*. That is a claim about a discontinuity scale smooths over, not sharpens. | A scaled generative/world-model agent that, under distribution shift and with **no** explicit commit boundary, never confabulates (never acts on simulated content as if owned) and cleanly gates commitment — i.e. the boundary emerges as a byproduct of scale. Concretely, this is the WS-11 early-gating-vs-late-judging demonstration run against a scaled late-judge baseline: if the late judge matches the commit-gate on the vmPFC/EVR "correct-knowledge, catastrophic-choice" task, the boundary is not doing structural work. |
| i.3 | **The axiomatic ethics derivation** (ARC-043 stack; INV-001 "no explicit ethics module or moral scoring layer") — ethics as a *consistency condition* on being a mortal, uncertain, mutually-modelling agent, rather than a reward term, a constitution, or a late filter. | This is **category-orthogonal to the Bitter Lesson.** Sutton's lesson is about *capability per compute* — winning games, predicting tokens, maximizing a given objective. Ethics-as-consistency-condition is a claim about **the structure of the objective itself** — about what *ought* to be optimized. Scale + search takes the objective as *given* and optimizes it superbly; it does not *derive* it. A system cannot search its way to the constraint that defines what a valid search target is. This is the strongest (i) claim: it is not a capability REE is hand-coding, it is a normative-architectural commitment the Bitter Lesson has nothing to say about. | Two routes. (a) A scaled system trained with a **late** value layer (RLHF / Constitutional-AI-style post-hoc scoring) achieves the same corrigibility and care properties REE claims are *structural* to the commit-boundary — showing derivation-from-axioms buys nothing over a bolt-on objective (again WS-11 / WS-7 corrigibility positioning). (b) The axiom chain is shown to smuggle its ethical content in as a premise (WS-13 red-team), in which case it is not a derivation and the "no module" invariant is cosmetic. |
| i.4 | **Three *incommensurable* error channels** (the strong form) — sensory PE, motor-sensory error, and harm/goal error cannot share a single scalar objective *at all* (ARC-021 / MECH-069). | Doya (1999) already argues distinct learning *rules* per structure; REE's stronger claim is non-collapsibility onto any scalar. If true, it is a statement that a single-objective learner is *structurally* mis-specified for this agent — a limit on what scaling one objective can reach. | **This is the (i) item most exposed to the Bitter Lesson, and it is admitted here provisionally.** A single scalar objective with enough capacity and data that routes credit correctly across all three channels — i.e. a scaled multi-head-free agent that passes the **forced-shared-loss ablation** named in `formal_ancestor_mapping.md` (ARC-021 row) without cross-channel credit leakage — demotes it. Flagged as the first candidate to fall. |

**The unifying test for bin (i):** an item earns its place only if you can name an experiment where a *scaled, searched, structure-free* baseline either **fails outright** or **pays unbounded (cost-scaling) price** for what the structure delivers at bounded cost. i.1 and i.3 make that test cleanly (anti-optimization constraint; objective-structure). i.2 is testable via WS-11 and is the flagship falsifiable win the project should hunt. i.4 is on probation.

### Bin (ii) — Scaffolding: scale legitimately would (and should) replace these

Named honestly, because the credibility of bin (i) depends on bin (ii) being large and real:

- **Hand-tuned arbitration weights, gains, thresholds** — the Daw-style MB/MF arbitration weighting, precision scalars (ARC-016), `frontopolar_gain`, the many hand-set commitment/latch thresholds. `formal_ancestor_mapping.md` already prescribes the fix: adopt the ancestor's formalism as the null and *learn* the parameters; test only deviations. Fixed gains are scaffolding by definition.
- **Fixed-field binders and hand-specified feature maps** — e.g. the `cross_stream_binding_substrate` fixed additive field, whose own build record flags "V4 learned binder" as the successor (`TASK_CLAIMS` reverent-clarke). The fixed version is scaffolding for a learned one.
- **Specific predictor architectures** — the E1/E2 slow/fast wiring as *implemented*. JEPA / Dreamer / MuZero show these can be learned end-to-end (`formal_ancestor_mapping.md` ARC-001/002 row). The *typed* split may be a prior (grey, below); the hand-drawn architecture is scaffolding.
- **Training-regime / curriculum specifics** — the thin P1 90-episode bias-head-only REINFORCE with a frozen encoder that produced the competence floor (`failure_autopsy_V3-EXQ-719a`). This is *pure* scaffolding, and its inadequacy **is** the Bitter Lesson biting. WS-1's competence-floor program (earn capability with a competent substrate, then re-introduce structure and measure the delta) is the correct, Bitter-Lesson-compliant response.
- **The 871 claims *as individual mechanisms*** — most are bets about implementation detail that a competent learned substrate would discover, override, or render moot. The registry-of-hypotheses is scaffolding for knowledge REE hopes to *earn*. The **demotion discipline** (WS-2) is precisely the mechanism that lets scale eat the mechanisms that do not pay. This doc's partition is not in tension with the registry; it is the registry's exit criterion.

### Bin (grey) — Open bets, carried with equal weight on the sceptical reading

- **The BG-like loop decomposition, Go/NoGo, wanting/liking** (ARC-030 / MECH-112/116/117) — these have clean formal ancestors (Frank 2005; Berridge & Robinson 1998). Whether the *specific* biological decomposition is a scale-invariant prior or merely one convenient basis a scaled system would replace with its own is **unresolved**. The convergence argument — biology-first derivation landing on the same structure as an independent formal program — is *evidence* the structure is necessary rather than chosen (the KAUST / Neural-Computers argument REE already makes), but convergence is support, not proof. Do not smuggle these into (i).
- **The successor-representation viability map** (ARC-007/018) — SR is *learnable* (Stachenfeld et al. 2017), so the map itself is grey; only the **residue reshaping the map** (i.1) is a clean (i) claim. Keep the two separate.
- **Global-workspace access channel** (SD-064) — GWT/GNW is a well-aligned re-derivation with a measurable signature (ignition); whether the capacity-limited bottleneck is a necessary prior or an artifact a scaled system routes around is open.

---

## The falsifiable stance (one paragraph, so it can be quoted)

**REE's structure-first bet is falsifiable and mostly *expected to lose*.** The scaffolding (bin ii — parameters, binders, predictor wiring, curriculum, and most of the 871 mechanisms as specified) *should* be eaten by scale + search, and the project's demotion discipline exists to feed it in. The bet is confined to bin (i): that a small set of structures — the **non-erasable residue field**, the **typed commit boundary**, the **axiomatic ethics derivation**, and (provisionally) **incommensurable error channels** — are *not* functions an optimizer produces from more data, because they are constraints *on* the optimizer (i.1, i.4), a discontinuity scale smooths over (i.2), or a property of the objective scale takes as given (i.3). Each carries a named falsifier; if a scaled, searched, structure-free baseline produces the same behaviour at bounded cost, that item demotes to (ii). i.4 is flagged as the first likely casualty. **If all four demote, the Bitter Lesson has won cleanly and REE was wrong to be structure-first.** The position is not "scale won't work"; it is "here are the four places we predict it pays an unbounded price, and here is how you would prove us wrong."

---

## What this commits REE to (design discipline)

1. **Bin (ii) is not defended.** When an ancestor formalism exists (per `formal_ancestor_mapping.md`), the hand-tuned version is a null to beat, not an asset to protect. "Demote drift back to biology" must never shield a fixed parameter that should be learned.
2. **Bin (i) must earn its keep against a scaled baseline, not against ablations of itself.** The current experiments mostly ablate REE-vs-REE. The Bitter-Lesson-honest test is REE-structure vs a *scaled, structure-free* competitor on the same task (WS-3 capability yardstick provides the denominator; WS-11 is the flagship). Until that comparison is run, bin (i) is a *hypothesis*, not a result.
3. **The competence floor is answered first (WS-1).** You cannot demonstrate that a commitment prior pays on an agent that cannot forage. Earn the capability floor with a deliberately dumb, competent substrate; *then* re-introduce structure and measure the delta. This is the Bitter Lesson used as a design tool, not an enemy.
4. **The demotion rule (WS-2) is the release valve.** A structure-first project without a pre-registered "this mechanism is inert, let scale have it" rule fills its registry with beautiful unkillable hypotheses. The demotion rule is what makes this whole position honest rather than motivated.

---

## References

**External**
- Sutton, R. (2019). *The Bitter Lesson.* incompleteideas.net/IncIdeas/BitterLesson.html.
- Chollet, F. (2019). *On the Measure of Intelligence.* arXiv:1911.01547. (Skill-acquisition efficiency; priors/experience/generalization; Core Knowledge priors; the "buying skill" argument.)
- Spelke, E. & Kinzler, K. (2007). *Core knowledge.* Developmental Science 10(1):89-96. (The Core Knowledge priors ARC is built on.)
- Wolpert, D. & Macready, W. (1997). *No Free Lunch Theorems for Optimization.* IEEE Trans. Evolutionary Computation. (Formal ground for "no priors-free learner.")
- ARC Prize (2024). *OpenAI o3 Breakthrough High Score on ARC-AGI-Pub* and *Analyzing o3 with ARC-AGI.* arcprize.org/blog. (87.5% high-compute; ~$4,500/task; 172× compute; 1,024 samples/task.)
- ARC Prize / Chollet et al. (2025). *ARC-AGI-2: A New Challenge for Frontier AI Reasoning Systems.* arXiv:2505.11831; arcprize.org/arc-agi/2. (o3 < 3%.)
- Doya, K. (1999). *What are the computations of the cerebellum, the basal ganglia and the cerebral cortex?* Neural Networks 12. (Distinct learning rules per structure — the weaker form of i.4.)
- LeCun, Y. (2022). *A Path Towards Autonomous Machine Intelligence.* (Structure-first world-model position; JEPA — relevant to the E1/E2 scaffolding call.)

**Internal**
- `docs/architecture/formal_ancestor_mapping.md` (WS-4) — the ancestor table and the "what should stay novel" set (the bin-(i) candidates).
- `evidence/planning/ree_ai_design_critique_plan.md` — WS-1 (competence floor), WS-2 (demotion rule), WS-3 (capability yardstick), WS-7 (corrigibility), WS-11 (early-gating demo), WS-13 (ethics red-team).
- `evidence/planning/failure_autopsy_V3-EXQ-719a_2026-07-08.md` and `conversion_ceiling_campaign_plan.md` — the competence-floor finding (the Bitter Lesson already biting on scaffolding).
- Claims: ARC-043 (ethics conceptual stack), INV-001 (no explicit ethics module), MECH-061 / MECH-094 (commit boundary + hypothesis tag), ARC-021 / MECH-069 (incommensurable channels), ARC-007/018 (viability map / residue), ARC-030 / MECH-112/116/117 (Go/NoGo, wanting/liking), SD-064 (global workspace).

---

*First pass. The four bin-(i) falsifiers should each become a concrete experiment design; i.2 (WS-11) and i.4 (forced-shared-loss ablation) are the two runnable now against a scaled baseline once the WS-1 competence floor is cleared. Until a scaled-baseline comparison exists, bin (i) is a stated bet, not a demonstrated result — and this doc's job is only to make the bet honest and losable.*
