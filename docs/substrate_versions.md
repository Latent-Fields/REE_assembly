---
title: Roadmap
nav_order: 7
has_children: true
---

# Substrate Versions: Where REE Is, and Where It Is Going

<div class="ree-doc-intro">
  <p class="ree-eyebrow">Programme route</p>
  <p class="ree-doc-lead">REE has been built four times. This page explains why, what each substrate generation was for, what it proved, what it could not reach, and what has to hold before the next one is honest to build.</p>
  <p class="ree-doc-meta">Architecture note. Exploratory research material; no REE work has been accepted for peer-reviewed publication.</p>
</div>

**Status:** architecture note
**Depends on:** `architecture/ethical_agency_derivation.md`, `architecture/five_axioms_foundations.md`, ARC-059, DEV-NEED-021

---

## Why there is more than one REE

The [derivation](architecture/ethical_agency_derivation.html) turns on a single constraint:

> **A comparator can only operate if the two things it compares are represented as distinct.** The comparator does not create the distinction — it presupposes it. If the architecture has not made a particular distinction, the comparator that would operate on it cannot be built.

That constraint governs the programme as well as the agent. A substrate can only test the questions its own representational distinctions permit. When a generation runs out of distinctions, it runs out of *answerable questions* — and no amount of further experimentation on it will help. The residual failures then name the distinction the next generation has to make.

So the versions are not releases. Each one is a new distinction, and the experiments it can run are the ones that distinction makes computable.

---

## The spine

Underneath the version numbers is a developmental ordering, registered as **ARC-059**:

<p style="font-size:1.25em;font-weight:600;letter-spacing:.02em;margin:1.2em 0;color:#176d65">self &rarr; objects &rarr; others &rarr; language</p>

ARC-059 states why the ordering is load-bearing rather than conventional:

> *(1) self-as-object — action-space discovery via motor experimentation; (2) objects-as-patterns — object-schema formation via experimental action on the world; (3) others-as-special-objects — modelling other agents as objects with their own policies. **The ordering is load-bearing: without a self-model the agent cannot distinguish self-produced from world-produced sensory change; without object-schemas the agent cannot recognise other-agents as a distinguished subclass of objects.***

Its companion **DEV-NEED-021** ("otherness inference after self-stability") names the failure mode for skipping ahead:

> *Social losses mask unresolved self/control faults; empathy and otherness are misattributed to unstable targets.*

Which is a recognisably clinical argument: do not work a relational problem on top of an unstable state, because the relational signal will absorb the blame for the instability.

### Stages are not versions

This is the part most easily misread. The spine is a **developmental** ordering. Versions are **substrate generations**. They interleave.

| Stage (ARC-059) | Carried by |
|---|---|
| **self** | V1 → V2 → V3, *finished in* V4 |
| **objects** | V4 |
| **others** | V5 |
| **language** | V6 |

**Stage one has taken four substrate generations.** That is the honest headline of the programme, and it answers the obvious question — *why are you on the third version of something that still only has one agent in it?* Because separating self from world turned out to be the hard part, exactly as the derivation predicts.

---

## Two kinds of transition

<figure class="ree-architecture-figure">
<svg id="svg-ladder" viewBox="0 0 880 330" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto;padding:1rem;box-sizing:border-box" role="img" aria-labelledby="ladder-t ladder-d">
<title id="ladder-t">Substrate generations and the developmental spine</title>
<desc id="ladder-d">Six substrate generations V1 to V6 on a horizontal track. V1, V2 and V3 are separated by replacement boundaries; V3 through V6 are joined as extensions of one surviving substrate. Below, four developmental stage bands show that the "self" stage spans V1 to V4, "objects" is V4, "others" is V5 and "language" is V6.</desc>
<style>#svg-ladder .vt{font:600 14px "trebuchet ms",verdana,sans-serif;fill:#18211f}
#svg-ladder .vs{font:11px "trebuchet ms",verdana,sans-serif;fill:#59645f}
#svg-ladder .lb{font:600 11px "trebuchet ms",verdana,sans-serif;fill:#59645f;letter-spacing:.06em}
#svg-ladder .sb{font:600 12px "trebuchet ms",verdana,sans-serif;fill:#fff}
</style>

<text x="12" y="22" class="lb">SUBSTRATE GENERATIONS</text>

<rect x="12"  y="34" width="118" height="58" rx="5" fill="#edf3ef" stroke="#d7ded8"/>
<text x="71" y="58" class="vt" text-anchor="middle">V1</text>
<text x="71" y="76" class="vs" text-anchor="middle">14 experiments</text>

<rect x="164" y="34" width="118" height="58" rx="5" fill="#edf3ef" stroke="#d7ded8"/>
<text x="223" y="58" class="vt" text-anchor="middle">V2</text>
<text x="223" y="76" class="vs" text-anchor="middle">15 experiments</text>

<rect x="316" y="34" width="140" height="58" rx="5" fill="#fff" stroke="#176d65" stroke-width="2"/>
<text x="386" y="58" class="vt" text-anchor="middle">V3 &middot; active</text>
<text x="386" y="76" class="vs" text-anchor="middle">2,181 experiments</text>

<rect x="470" y="34" width="126" height="58" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="533" y="58" class="vt" text-anchor="middle">V4</text>
<text x="533" y="76" class="vs" text-anchor="middle">individual mind</text>

<rect x="610" y="34" width="126" height="58" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="673" y="58" class="vt" text-anchor="middle">V5</text>
<text x="673" y="76" class="vs" text-anchor="middle">social mind</text>

<rect x="750" y="34" width="118" height="58" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="809" y="58" class="vt" text-anchor="middle">V6</text>
<text x="809" y="76" class="vs" text-anchor="middle">linguistic mind</text>

<path d="M136 63 L158 63" stroke="#a94732" stroke-width="2" marker-end="url(#ar)"/>
<path d="M288 63 L310 63" stroke="#a94732" stroke-width="2" marker-end="url(#ar)"/>
<path d="M456 63 L466 63" stroke="#176d65" stroke-width="2" marker-end="url(#at)"/>
<path d="M596 63 L606 63" stroke="#176d65" stroke-width="2" marker-end="url(#at)"/>
<path d="M736 63 L746 63" stroke="#176d65" stroke-width="2" marker-end="url(#at)"/>

<defs>
<marker id="ar" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#a94732"/></marker>
<marker id="at" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#176d65"/></marker>
</defs>

<text x="147" y="112" class="vs" text-anchor="middle" fill="#a94732">replace</text>
<text x="299" y="112" class="vs" text-anchor="middle" fill="#a94732">replace</text>
<text x="620" y="112" class="vs" text-anchor="middle" fill="#176d65">extend &mdash; V3 is never retired</text>

<line x1="12" y1="136" x2="868" y2="136" stroke="#d7ded8"/>
<text x="12" y="162" class="lb">DEVELOPMENTAL STAGE (ARC-059)</text>

<rect x="12"  y="174" width="584" height="34" rx="4" fill="#176d65"/>
<text x="304" y="196" class="sb" text-anchor="middle">self &mdash; spans four generations</text>

<rect x="470" y="216" width="126" height="34" rx="4" fill="#355f9a"/>
<text x="533" y="238" class="sb" text-anchor="middle">objects</text>

<rect x="610" y="216" width="126" height="34" rx="4" fill="#a94732"/>
<text x="673" y="238" class="sb" text-anchor="middle">others</text>

<rect x="750" y="216" width="118" height="34" rx="4" fill="#59645f"/>
<text x="809" y="238" class="sb" text-anchor="middle">language</text>

<text x="12" y="286" class="vs">The stage bands do not line up with the generation boxes. That misalignment is the point:</text>
<text x="12" y="304" class="vs">V4 both finishes the self stage and begins the objects stage.</text>
</svg>
<figcaption>Substrate generations against the ARC-059 developmental spine. Experiment counts are manifests on disk; V4-V6 are planned, not built.</figcaption>
</figure>

The ladder has a discontinuity in it, and it is not a representational one.

**V1 → V2 → V3 were replacements.** Build the substrate outright, test it, hit a wall, retire it, build the next. That gave roughly fifteen shots per generation before the substrate ran out of answerable questions.

**V3 → V4 → V5 → V6 are extensions.** V3 is not retired when it fails. A failure is filed as a substrate debt and the substrate is amended in place.

What changed was not the architecture but the **method**, and the record dates it precisely:

| Event | Date |
|---|---|
| V2 experiment series closed on three hard-stop criteria | **2026-03-19** |
| `scripts/governance.sh` first commit | **2026-03-20** |
| `evidence/experiments/review_tracker.json` first commit | **2026-03-20** |
| `evidence/planning/substrate_queue.json` first commit | 2026-04-09 |

The governance machinery was built the day after V2 closed. V2's real lesson was not about `z_gamma`; it was that a cognitive architecture cannot be specified once and then verified. It has to be grown against evidence, with a claims registry, an experiment-evidence pipeline, and a substrate queue that lets the substrate absorb its own failures.

The effect is visible in the raw counts on the diagram above: **14, then 15, then 2,181**.

One consequence is worth stating plainly, because readers reasonably expect otherwise: **there will not be a V3 → V4 transition of the kind that happened at V2.** V4 does not replace V3. It layers onto it, under an explicit rule — the [version-layering doctrine](architecture/version_layering_doctrine.html) — that *no higher-version code may change V3 default execution behaviour*. That rule exists because a V4 change once crash-burned a V3 experiment, and it only makes sense in a programme where generations coexist rather than succeed one another.

---

## The ladder so far

### V1 — `ree-v1-minimal` — qualification baseline

A deliberately narrow substrate: stateless grid world, minimal recurrent E1/E2 stack. It was never an architecture target. It asked one question — *do moral residue, precision-routed control and commitment-boundary separation produce real, replicable directional effects, or noise?*

Several mechanisms passed: precision-channel separation, residue accumulating along the trajectory rather than only at the endpoint, commitment-boundary reclassification, write-locus separation.

**The wall:** E2 had been conflated with hippocampal trajectory search, so experiments that froze E2 were also freezing trajectory proposal, and several results became uninterpretable. V1 closed by registering three substrate debts — SD-001, SD-002, SD-003 — which are the specification for V2.

*Full detail: [V1 progress and learning](V1_PROGRESS_AND_LEARNING.html).*

### V2 — `ree-v2` — closed

Fifteen experiments. It cleanly separated E2 from the hippocampus and demonstrated qualitative three-loop structure.

**The wall:** V2 represented the agent's state as a single fused latent, `z_gamma`, which conflated body-state with world-state. That made self-attribution not merely hard but *not computable*: you cannot ask "did I cause this, or would it have happened anyway?" when your own causal footprint and ambient world dynamics live on the same undifferentiated signal. The self-attribution experiment returned a calibration gap of **-0.004** — indistinguishable from an untrained control.

V2 had defined three hard-stop criteria in advance. All three fired. The series closed on 2026-03-19.

**V2 is the most instructive generation on this page**, and not because it failed. It was retired *by its own pre-registered criteria*, on evidence, without argument — and the response was to change how REE is built, not merely what is built.

### V3 — `ree-v3` — active

V3 made the distinction V2 lacked: `z_gamma` split into **`z_self`** and **`z_world`** (SD-005, implemented), with action objects (SD-004) and multi-rate loop execution (SD-006) co-designed alongside it.

<figure class="ree-architecture-figure">
<svg id="svg-split" viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto;padding:1rem;box-sizing:border-box" role="img" aria-labelledby="split-t split-d">
<title id="split-t">The V2 to V3 representational split</title>
<desc id="split-d">On the left, V2's single fused latent z_gamma feeds a self-attribution comparator that cannot compute, because the agent's causal footprint and ambient world dynamics are on the same signal. On the right, V3 splits it into z_self and z_world, which lets the counterfactual comparator subtract one from the other and yield a causal signature.</desc>
<style>#svg-split .dt{font:600 13px "trebuchet ms",verdana,sans-serif;fill:#18211f}
#svg-split .dm{font:11px "trebuchet ms",verdana,sans-serif;fill:#59645f}
#svg-split .dh{font:600 11px "trebuchet ms",verdana,sans-serif;fill:#59645f;letter-spacing:.06em}
#svg-split .dc{font:600 12px "trebuchet ms",verdana,sans-serif;fill:#fff}
</style>

<text x="12" y="20" class="dh">V2</text>
<rect x="12" y="32" width="180" height="46" rx="5" fill="#59645f"/>
<text x="102" y="53" class="dc" text-anchor="middle">z_gamma</text>
<text x="102" y="69" class="dm" text-anchor="middle" fill="#e8ece9">self + world, fused</text>

<path d="M102 82 L102 108" stroke="#a94732" stroke-width="2" marker-end="url(#ar2)"/>
<rect x="12" y="112" width="180" height="44" rx="5" fill="#fff" stroke="#a94732" stroke-dasharray="4 3"/>
<text x="102" y="132" class="dt" text-anchor="middle" fill="#a94732">self-attribution</text>
<text x="102" y="148" class="dm" text-anchor="middle" fill="#a94732">cannot be computed</text>
<text x="102" y="184" class="dm" text-anchor="middle">"Did I cause this?" has no</text>
<text x="102" y="200" class="dm" text-anchor="middle">subtraction to perform &mdash; both</text>
<text x="102" y="216" class="dm" text-anchor="middle">terms are the same signal.</text>
<text x="102" y="238" class="dm" text-anchor="middle" fill="#a94732">calibration gap &minus;0.004</text>

<line x1="248" y1="24" x2="248" y2="238" stroke="#d7ded8" stroke-dasharray="3 4"/>

<text x="292" y="20" class="dh">V3</text>
<rect x="292" y="32" width="180" height="46" rx="5" fill="#176d65"/>
<text x="382" y="59" class="dc" text-anchor="middle">z_self</text>
<rect x="500" y="32" width="180" height="46" rx="5" fill="#355f9a"/>
<text x="590" y="59" class="dc" text-anchor="middle">z_world</text>

<path d="M382 82 L448 108" stroke="#176d65" stroke-width="2" marker-end="url(#at2)"/>
<path d="M590 82 L524 108" stroke="#355f9a" stroke-width="2" marker-end="url(#ab2)"/>

<rect x="378" y="112" width="216" height="44" rx="5" fill="#fff" stroke="#176d65" stroke-width="2"/>
<text x="486" y="132" class="dt" text-anchor="middle">counterfactual comparator</text>
<text x="486" y="148" class="dm" text-anchor="middle">E2 &middot; E3 joint pipeline</text>

<path d="M486 160 L486 182" stroke="#176d65" stroke-width="2" marker-end="url(#at2)"/>
<text x="486" y="200" class="dm" text-anchor="middle">harm(a_actual) &minus; harm(a_counterfactual)</text>
<text x="486" y="222" class="dm" text-anchor="middle">Two distinct terms exist, so the</text>
<text x="486" y="238" class="dm" text-anchor="middle">subtraction is now defined.</text>

<defs>
<marker id="ar2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#a94732"/></marker>
<marker id="at2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#176d65"/></marker>
<marker id="ab2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#355f9a"/></marker>
</defs>
</svg>
<figcaption>Why V3 exists. The split is not a refactor: it is what makes a comparator definable that was previously undefinable.</figcaption>
</figure>

What V3 is: **a single organism-like mind in a sole world.** It commits and de-commits, avoids harm, sleeps (a minimal two-phase offline consolidation, SD-017), follows apprehended rules, maintains behavioural diversity, and carries a goal/drive cascade. It scaffolds five of the six [necessary comparators](architecture/ethical_agency_derivation.html) the derivation identifies. The sixth — other-representation — is architecturally anticipated but has no other to exercise it.

Live progress is tracked on the [Closure Dashboard](closure_dashboard.html); the [Status Log](roadmap.html) carries the nightly detail.

---

## What comes next

### V4 — the individual mind

Fourteen planned workstreams: object representation, self-model integration, memory lifecycle, hippocampal planning depth, drives and motivation, affect and expression, perceptual adaptors, plasticity windows, play and the externalised default-mode network.

The common misreading is that V4 introduces the shared world. **It does not.** V4 completes the individual mind to the point where an *other* becomes representable at all. The V5 plans state the dependency directly:

> *Otherness inference REQUIRES object-permanence AND a stable self, both V4.*

An other is a persistent object that additionally has policy, welfare, body state and goal dynamics. You cannot have the subclass before you have the class. That is why object permanence — not social machinery — is the V4 pillar.

### V5 — the social mind

Six planned workstreams: multi-agent ecology, mirror modelling (others modelled by reusing the self-model), fast empathy as stream-binding, relational harm and moral semantics, ethics-as-coherence, and loveability internalisation.

This is where the shared world arrives, and where the derivation's sixth comparator finally has something to compare.

### V6 — the linguistic mind

Five planned workstreams: language emergence from social ecology, grammar-primitive mining, a language-affect adaptor, abstract relational reasoning, and language-mediated trust, deception and institutions.

V6 is gated hard and deliberately:

> *Language work is gated behind every pre-linguistic primitive (object / action / self / other / rule) being grounded first.*

The standing instruction on the grammar workstream is to **mine** existing language models for primitives, **not** to import their architecture.

---

## Self-attribution is built three times

The clearest illustration of why stages and versions interleave is the capacity the whole programme is named for.

| Generation | What "self-attribution" means there |
|---|---|
| **V3** | **The causal comparator.** "Did I cause this change in the world, or would it have happened without me?" Requires only `z_self` and `z_world`. |
| **V4** | **The materialised self-model.** `z_self` becomes a first-class scored object rather than an encoder channel — self-as-object. |
| **V5** | **The moral comparator.** "Did I cause *their* harm?" Requires the same machinery applied to a represented other. |

Only the third is what the phrase usually means. The derivation already implies this: its self-attribution comparator asks a purely *causal* question, while the ethical content arrives with the sixth comparator, which needs another agent's harm and goal states represented in the same currency as one's own.

So it is expected — not a delay — that the self-attribution workstream is partly open in V3 with pieces explicitly deferred to V4. The trinity of self, world and other is not assembled until V5, and until it is, self-attribution is a real but pre-moral capacity.

---

## The single gate

<figure class="ree-architecture-figure">
<svg id="svg-gate" viewBox="0 0 700 240" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto;padding:1rem;box-sizing:border-box" role="img" aria-labelledby="gate-t gate-d">
<title id="gate-t">MECH-163 as the shared entry gate</title>
<desc id="gate-d">Three planned generations, V4, V5 and V6, all depend on a single unbuilt V3 capability: MECH-163, multi-step hippocampal planning, described in the plans as the V4-social entry gate.</desc>
<style>#svg-gate .gt{font:600 13px "trebuchet ms",verdana,sans-serif;fill:#18211f}
#svg-gate .gm{font:11px "trebuchet ms",verdana,sans-serif;fill:#59645f}
#svg-gate .gw{font:600 13px "trebuchet ms",verdana,sans-serif;fill:#fff}
</style>

<rect x="60"  y="16" width="160" height="42" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="140" y="42" class="gt" text-anchor="middle">V4 individual</text>
<rect x="268" y="16" width="160" height="42" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="348" y="42" class="gt" text-anchor="middle">V5 social</text>
<rect x="476" y="16" width="160" height="42" rx="5" fill="#fff" stroke="#d7ded8" stroke-dasharray="4 3"/>
<text x="556" y="42" class="gt" text-anchor="middle">V6 linguistic</text>

<path d="M140 62 L322 108" stroke="#a94732" stroke-width="1.6" marker-end="url(#ag)"/>
<path d="M348 62 L348 108" stroke="#a94732" stroke-width="1.6" marker-end="url(#ag)"/>
<path d="M556 62 L374 108" stroke="#a94732" stroke-width="1.6" marker-end="url(#ag)"/>

<rect x="196" y="112" width="304" height="52" rx="5" fill="#a94732"/>
<text x="348" y="134" class="gw" text-anchor="middle">MECH-163</text>
<text x="348" y="152" class="gm" text-anchor="middle" fill="#f4e6e2">multi-step hippocampal planning</text>

<text x="348" y="190" class="gm" text-anchor="middle">Status: candidate &middot; implementation phase: V3 &middot; not yet built</text>
<text x="348" y="212" class="gm" text-anchor="middle">Every V5 and V6 plan calls it "the V4-social entry gate".</text>

<defs>
<marker id="ag" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#a94732"/></marker>
</defs>
</svg>
<figcaption>One unbuilt V3 capability sits underneath all three planned generations.</figcaption>
</figure>

Every V5 and V6 plan carries the same prerequisite, and it is not a V5 item. It is **MECH-163** — multi-step hippocampal planning — still a candidate claim in V3.

The reason is structural rather than administrative: modelling another agent's welfare means modelling how your trajectory affects their harm and goal state *over time*. A one-step greedy policy cannot represent that. So other-modelling is inaccessible until planning has depth, which makes a single unbuilt V3 capability the load-bearing prerequisite for the individual, social and linguistic tiers alike.

---

## How this returns to the axioms

The [eight axioms](architecture/five_axioms_foundations.html) are ordered as a dependency chain, and the version ladder is paced by that chain rather than decorated with it:

| Axiom | Becomes live in |
|---|---|
| **1** — I think, therefore I am | V1–V4: the self stage, ending in a materialised self-model |
| **2, 3, 4** — existence has value; irreducible uncertainty; agency with vulnerability | V3: harm gradients, precision machinery, the commit gate |
| **5** — others exist and are sufficiently like me | **V5**: mirror modelling; the axiom the derivation calls the representational isomorphism requirement |
| **6, 7** — responsibility for others; love as its mechanism | **V5**: relational harm, ethics-as-coherence, loveability |
| **8** — language recognises and repairs similarity | **V6** |

Axiom 5 is the only axiom that is explicitly *learned* rather than assumed. That is why it cannot be installed early: the agent has to discover that others are like it, using machinery built for itself, on a substrate stable enough that the discovery means something.

---

## Read further

| Document | What it covers |
|---|---|
| [V1 progress and learning](V1_PROGRESS_AND_LEARNING.html) | The V1 substrate in full: experiments, passes, informative failures, substrate debts |
| [V2 → V3 transition roadmap](architecture/v2_v3_transition_roadmap.html) | What V2 could and could not test; the hard-stop criteria; V3 prerequisites |
| [REE-v2 implementation spec](architecture/ree_v2_spec.html) | The V2 substrate as specified |
| [V3 / V4 transition boundary](architecture/v3_v4_transition_boundary.html) | V3 static setpoints that become V4 dynamic mechanisms |
| [V4 planning index](architecture/v4_planning_index.html) | Entry point for V4 planning documents |
| [V4 spec](architecture/v4_spec.html) | Canonical V4 substrate primitives |
| [Substrate roadmap](architecture/substrate_roadmap.html) | V3-tractable enrichments (what V3 can still absorb) |
| [Version-layering doctrine](architecture/version_layering_doctrine.html) | Why higher-version work may never change V3 default behaviour |
| [Closure Dashboard](closure_dashboard.html) | Live V3 progress by plan |
| [Status Log](roadmap.html) | Nightly programme snapshots |
