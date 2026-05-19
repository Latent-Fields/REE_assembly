# Ghost Goal Search

**Status:** design sketch (2026-04-26) + **Retrieval-Cue Reframe (2026-05-19)** -- see Section 0  
**Created:** 2026-04-26  
**Scope:** explicit unresolved-goal traces for awake hippocampal search in V3  
**Related claims:** MECH-216, MECH-217, MECH-230, ARC-051, MECH-269, MECH-284, MECH-285, MECH-291, SD-039, MECH-292, MECH-293, ARC-060

---

## 0. Retrieval-Cue Reframe (2026-05-19)

> Provenance: this section folds in the synthesis of the combined cue-system
> literature pull (`evidence/literature/targeted_review_ghost_goal_search/`,
> 2026-05-18: Nakazawa 2002, Gelbard-Sagiv 2008, Smith & Vela 2001, Flagel
> 2011, Corbit & Balleine 2005/2011, Jasinska 2014, Bouton 2004,
> Maren/Phan/Liberzon 2013, Bouton 2014). Per the biology-before-formal-
> definitions rule the divergences below are **structural constraints, not
> caveats**. This is an interpretive reframe of the existing ARC-060 /
> MECH-292 / MECH-293 / SD-039 cluster: **no new claim is registered, no
> experiment is queued, no claim is promoted, statuses are unchanged.** The
> 2026-04-26 sketch (Sections 1-10) is retained as history; where it
> conflicts with Section 0, Section 0 governs.

### 0.1 Thesis

The ghost-goal bank is not, structurally, a priority queue of deferred
goals. It is a **content-addressed cue -> target retrieval system**:

- the current goal/context is the **retrieval cue**;
- the SD-039 payload preserved on an inactive anchor is the **stored trace**;
- `rank_ghost_goals()` is **cued recall** (`goal_match` is the
  cue-to-trace match score, not a priority weight);
- MECH-293's awake probe is an **internally-triggered retrieval** that
  reinstates and re-pursues the recalled trace.

ARC-060's "continuous wanting field vs discrete unresolved-goal bank" split
is, in this light, the **recognition-vs-recall distinction**: the field
supports gradient-following when a local cue is present; the bank supports
recall of a goal whose local gradient has collapsed, from a partial or
internal cue. The biology is unambiguous that this is a real operation:
CA3 recurrent dynamics complete a partial cue to the full stored trace
(Nakazawa 2002), and an internally generated cue reinstates the
encoding-time trace ahead of report (Gelbard-Sagiv 2008).

### 0.2 Three load-bearing structural constraints

**Constraint 1 -- `goal_match` must DOMINATE a context channel; context is a
conditional fallback, not an always-on additive term.**

- Biology: encoding specificity is real but moderate, and is *outshone* by a
  strong direct cue and *overshadowed* by strong non-contextual encoding
  cues (Smith & Vela 2001). Context-overlap retrieval is the weak regime
  that matters precisely when a strong direct match is absent.
- Design requirement: the cue is currently `z_goal` cosine only. SD-039
  already preserves `arousal_tag`, `last_vs`, and a `cause` tag but the
  match ignores them. A context channel should be built from those
  stored-but-unused payload fields, but it must be **gated to yield to a
  strong `goal_match`**, not summed in with fixed weight. A bank that
  always adds context degrades retrieval (by the outshining result)
  whenever a clean direct match exists.
- Falsifiable prediction: with a strong direct goal match present, adding
  the context channel must not change the top-ranked entry; with direct
  match weak/absent, the context channel must change it.
- Failure mode: an always-on additive context term produces
  context-driven misretrieval in exactly the regime where identity
  matching would have been correct.

**Constraint 2 -- `wanting` and `goal_match` are DISSOCIABLE ADDITIVE
channels, NOT a multiplicative product.**

- Biology: incentive attribution is a dopamine-gated step separable from
  predictive accuracy -- a fully predictive cue can carry near-zero
  wanting and vice versa (Flagel 2011). The substrate double-dissociates:
  BLA -> NAc-shell carries outcome-*specific* transfer (the `goal_match`
  channel), CeA -> NAc-core carries value-*general* invigoration (the
  `wanting` channel), and each fails independently (Corbit & Balleine
  2005/2011).
- Design requirement: `ghost_priority` must be a sum of independently
  gateable channels. **This is already true in the landed substrate**
  (`ghost_goal_bank.py:168`, `priority = w_w*wanting + w_m*goal_match +
  w_s*staleness + w_r*recoverability`). The drift is in this document:
  the 2026-04-26 sketch wrote the product form `ghost_priority ~ wanting x
  goal_match x staleness x recoverability` (Sections 4.2 and 6.2). **That
  product form is SUPERSEDED.** The additive implemented form is the
  biologically correct one; this reframe ratifies it rather than changing
  it.
- Falsifiable prediction: the three dissociated states must be inducible
  -- (a) intact match, absent vigor (entries recalled, not pursued); (b)
  nonspecific vigor, absent match (diffuse re-probing not tied to any
  recalled goal); (c) match present but un-actionable because the
  invigoration channel is offline at retrieval time.
- Failure mode: a multiplicative score cannot represent any of the three;
  it silently zeroes a recalled-but-unwanted (or wanted-but-unmatched)
  trace that biology keeps distinct.

**Constraint 3 -- `recoverability` cannot be inhibition-only, and cannot be
a cutoff that accumulates suppression evidence toward "retire this
anchor".**

- Biology: extinction never erases; the original trace is preserved and
  re-expressed under context change (renewal, spontaneous recovery,
  reinstatement, rapid reacquisition -- Bouton 2004). The recoverability
  gate is a hippocampus-amygdala-vmPFC context-selection circuit, and
  gate-stuck-open *is* the mechanism of intrusion/relapse (PTSD,
  addiction, schizophrenia -- Maren/Phan/Liberzon 2013). Critically,
  accumulated suppression evidence does **not** close the gate: 36 vs 4
  sessions of elimination produced identical return, and resurgence
  returns a "resolved" goal the moment a competitor stops paying off
  (Bouton 2014). Cue-reactivity can *incubate* -- a long-blocked trace
  becomes *more* compelling with time, inverting a monotonic
  staleness-decay prior (Jasinska 2014).
- Design requirement: (i) `recoverability` is context-selection between
  competing active/inactive traces, not a decay scalar; (ii) it must not
  integrate "evidence of hopelessness" toward a retire decision -- biology
  shows that inference to be false; (iii) "a competitor is winning" is
  **not** a safe retire condition (resurgence); (iv) do not assume
  staleness monotonically decays pull (incubation).
- Falsifiable prediction: rumination/intrusion is the *predicted
  equilibrium* of an inhibition-only design -- a bank with no explicit
  abandon path, run long enough in a blocked-decoy environment, must
  drift toward perseverative re-probing of hopeless traces.
- Failure mode: a recoverability cutoff that closes on accumulated
  suppression evidence will be confidently, systematically wrong, and
  will under-weight exactly the incubating traces most likely to capture
  the agent.

### 0.3 The deliberate divergence point

> **RESOLVED 2026-05-19 by the goal-disengagement biology-before pull
> (`targeted_review_goal_disengagement/`). The framing below is INVERTED;
> see ARC-079 / MECH-340 / Q-053.**

The reframe originally stated this as a *deliberate divergence*: biology
has no erase operation, rumination/intrusion is the structural price, and
REE should add an explicit abandon path while forbidding any
accumulated-hopelessness justification. The goal-disengagement pull shows
that framing is backwards in two ways:

1. **Maier & Seligman 2016 (load-bearing inversion):** passivity /
   disengagement is the *unlearned default*; what is learned and gated is
   *control*. So the gated, evidence-requiring operation is **persistence**
   (continuing to treat an entry as an active re-probe target), not
   abandonment. Disengagement is what happens when the persistence gate
   does not fire.
2. **Bouton's no-erase result is about the trace, not pursuit.** The
   SD-039 trace is preserved (no erase) -- which *matches* biology, so the
   "deliberate divergence" premise is weakened. "Abandonment" is just the
   persistence gate not firing -> MECH-292 rank decays -> the entry stops
   being re-probed while the trace survives, exactly like Bouton's
   preserved-but-inhibited memory.

Net: the right design **gates persistence** (a control/efficacy detector,
MECH-340) rather than bolting on an abandon trigger; the gate must avoid
keying on accumulated failure / bare effort-cost (that reproduces learned
helplessness, the over-disengaged pole). The goal-disengagement pull
**narrows Q-053 without closing it**: the licit gate signal's *front-runner*
is an internal control/efficacy *unattainability appraisal* (Wrosch input
semantics + Maier form; vmPFC->DRN *not* imported); an external/world
invalidation signal is demoted to an *input* to that appraisal, not the
gate; a self-model-obsolescence write stays genuinely open. Whatever the
signal, it opens or withholds a brief reengagement-coupled disengagement
*state* (Klinger), never a one-shot flag, and the operation it triggers
must itself be reengagement-coupled (Wrosch/Klinger: abandon-without-redirect
is itself a pathology). The hard-erase sub-question is now **split**: the
SD-039 *trace* needs no explicit erase (lean NO, Bouton -- ungated MECH-292
rank-decay of a preserved trace suffices), but *disengagement itself*
likely needs a dedicated operation distinct from tuning the MECH-292 knobs
(lean YES, Koster). The computation of the appraisal remains the open core
of Q-053.

### 0.4 What this reframe changes and does not change

| Aspect | Status |
|---|---|
| ARC-060 / MECH-292 / MECH-293 / SD-039 | reframed interpretation + revised falsifiable predictions; **status, phase, confidence unchanged** |
| `ghost_priority` product formula (old Sections 4.2 / 6.2) | **SUPERSEDED** by the additive form already in the substrate |
| Context channel from SD-039 payload fields | **IMPLEMENTED 2026-05-19** (Constraint 1 / MECH-339): smallest substrate step -- arousal_tag context channel gated by goal_match in `ghost_goal_bank.py` (`use_composite_cue_outshining`, default off); `last_vs`/`cause` deferred. Diagnostic validation V3-EXQ-594 queued. See ree-v3/CLAUDE.md "MECH-339 C1". |
| Three-state dissociation validation | **new falsifiable battery** (Constraint 2); not queued |
| Explicit abandon path | **RESOLVED + INVERTED 2026-05-19** (0.3): persistence is gated, disengagement is the default, trace preserved; registered as ARC-079 / MECH-340 / Q-053 |
| New claims | **ARC-078 + MECH-339** (cue-system, 2026-05-19) and **ARC-079 + MECH-340 + Q-053** (persistence-gate / C3 resolution, 2026-05-19); see 0.5 |
| Experiments / promotion | **none** -- registration only, no experiment queued, no promotion |

### 0.5 Claim cluster (registered 2026-05-19)

The genuinely-new content of the reframe was registered as a small cluster
(interpretive sharpening of the existing claims stayed in their reframe
notes; see 0.4):

- **ARC-078** (parent, architecture_hypothesis, candidate / v3_pending):
  "the unresolved-goal bank is a content-addressed cue-addressed retrieval
  system" satisfying C1-C3. **ARC-060 specializes into ARC-078**
  (`ARC-060.depends_on += ARC-078`).
- **MECH-339** (mechanism_hypothesis, candidate / v3_pending): the
  composite cue + outshining gate of Constraint 1; `depends_on` ARC-078 /
  SD-039 / MECH-230 / MECH-292. **Substrate IMPLEMENTED 2026-05-19**
  (smallest step: arousal_tag context channel gated by goal_match in
  `ghost_goal_bank.py`, default off; `last_vs`/`cause` deferred). Diagnostic
  validation EXQ queued; status stays candidate / v3_pending (implementation
  is not evidence).
- **C2** carries no new claim -- it is MECH-292's ratified additive form.
- **C3 was resolved 2026-05-19** by the goal-disengagement biology-before
  pull (`targeted_review_goal_disengagement/`: Maier & Seligman 2016,
  Klinger 1975, Wrosch 2003, Koster 2011, Gillan 2021/2016, Husain &
  Roiser 2018, Treadway 2012, Brandstatter 2013), which *inverted* the
  framing (see 0.3) and registered:
  - **ARC-079** (architecture_hypothesis, candidate / v3_pending): the
    persistence-is-gated / disengagement-is-default inversion; child of
    ARC-078, resolves its C3.
  - **MECH-340** (mechanism_hypothesis, candidate / v3_pending): the
    per-entry persistence/efficacy gate; absence = default disengagement
    via MECH-292 rank decay (trace preserved, no erase).
  - **Q-053** (question, open; **narrowed 2026-05-19** from the same pull):
    the licit gate signal. Ruled-out signals fixed (accumulated failure,
    bare effort-cost, staleness, within-crisis devalued value) plus a
    ruled-out operation-shape (abandon without coupled reengagement).
    Candidate set narrowed: front-runner = internal control/efficacy
    unattainability *appraisal* (Wrosch+Maier, a structural collapse of two
    prior candidates); external invalidation demoted to an input;
    self-model-obsolescence still open. The single hard-erase sub-Q is
    split -- trace-erase lean NO (Bouton), dedicated-disengage-op lean YES
    (Koster). Narrowing is structural, not experimental; exp_conf 0.0, lit
    parallel-only.
  The cluster is the mirror image of the unregistered interrupted-task /
  Zeigarnik resumption gap (resume <-> disengage); Q-053 must be reconciled
  with that gap when it is registered (after its own biology-before pull),
  not in parallel.

Status/phase/confidence of ARC-060 / MECH-292 / MECH-293 / SD-039 remain
unchanged; the cluster is candidate / v3_pending with `exp_conf = 0`
(lit_conf is a parallel signal only, never blended).

---

## 1. Why this note exists

`ree-v3` already has three important ingredients:

1. A persistent goal latent (`z_goal`) and wanting-related terrain signals.
2. A dual-trace anchor substrate with inactive anchors preserved instead of erased.
3. A staleness readout that says which regions remain epistemically unresolved.

What it does **not** yet have is an explicit representation of "what was still
wanted there" when an anchor becomes inactive or when a path remains blocked.
Current waking search can therefore answer:

- where the current terrain looks good
- where verisimilitude is stale

but it cannot reliably answer:

- which stale regions still correspond to a live but currently blocked goal
- which deferred goals should receive probe budget before random exploration

This note defines the missing layer.

## 2. Existing substrate and current gap

### Present in V3

- `GoalState` gives a recurrent positive attractor in `z_goal` space.
- `VALENCE_WANTING` can bias hippocampal scoring.
- `AnchorSet` preserves active and inactive anchors (`mark_inactive`, not erase).
- `StalenessAccumulator` provides a graded unresolved-region signal.
- `SleepReplaySampler` already draws from active + inactive anchors using staleness.

### Missing in V3

- Anchors preserve `z_world`, but not an explicit goal snapshot.
- There is no ranked bank of unresolved or deferred goals.
- Waking `propose_trajectories()` does not seed from inactive/high-wanting/high-
  staleness anchors.
- Between ticks, `generate_trajectories()` mostly reuses cached candidates
  instead of running cheap probe refreshes around unresolved goals.

## 3. Core proposal

Add an explicit **ghost-goal layer** on top of the existing wanting and anchor
substrates.

The term "ghost goal" means:

- a goal that is still motivationally live
- but is not currently executable through the active plan
- and therefore survives as a preserved unresolved trace rather than as the
  current committed trajectory

This is not a replacement for ARC-051's emergent wanting hierarchy. It is a
complement to it. ARC-051 says that wanting can emerge as a multi-scale field.
The ghost-goal layer adds a discrete memory of unresolved goal traces when a
continuous field is too lossy.

## 4. New claim stack

### SD-039: anchor goal snapshot payload

When anchors are written, remapped, or invalidated, they should preserve not
just `z_world` but also a compact "what was being wanted here" payload:

- `z_goal_snapshot`
- `wanting_strength`
- `arousal_tag`
- optional `last_vs` / `staleness_at_write`
- cause tag: `boundary`, `reset`, `blocked`, `goal_relocated`

Without this payload, staleness only says "this region is unresolved", not
"this unresolved region still matches a live goal".

### MECH-292: ghost-goal bank

Inactive or strained anchors with preserved goal payloads are ranked into a
bank of unresolved goals. This bank is not the same as the replay sampler's
broad pool:

- the broad pool is about seed eligibility
- the ghost bank is about motivational relevance under current goals

The bank should rank by something like:

`ghost_priority ~ wanting x goal_match x staleness x recoverability`

> **SUPERSEDED by Section 0 (2026-05-19, Constraint 2).** This product form
> is biologically wrong: `wanting` and `goal_match` are dissociable
> channels, not factors. The landed substrate already uses the correct
> additive form; see Section 0.2 Constraint 2.

where:

- `wanting` says how motivationally live the trace was
- `goal_match` compares current `z_goal` to stored `z_goal_snapshot`
- `staleness` says the region remains unresolved
- `recoverability` prevents rumination on hopeless regions

### MECH-293: awake ghost-centered probe search

Waking hippocampal search should allocate a minority proposal budget to top
ghost-goal traces. This means:

- not pure current-anchor CEM only
- not pure random noise probing
- but a mixed proposal policy that can revisit blocked/deferred goals

The probe channel remains MECH-094-tagged and should not update the viability
map until realized validation.

### ARC-060: explicit unresolved-goal hierarchy

A good agent needs both:

- the continuous wanting landscape of ARC-051
- a discrete bank of unresolved goal traces

The first supports smooth navigation over known gradients. The second preserves
goals that remain important even when local gradients collapse.

## 5. Data model

### 5.1 Anchor payload extension

Suggested extension to `Anchor`:

```python
@dataclass
class GhostGoalPayload:
    z_goal_snapshot: Optional[torch.Tensor]
    wanting_strength: float
    arousal_tag: float
    last_vs: float
    staleness_at_write: float
    cause: str
    tick_written: int

@dataclass
class Anchor:
    ...
    ghost_payload: Optional[GhostGoalPayload] = None
```

### 5.2 Ranked ghost-goal view

Suggested derived view in `HippocampalModule`:

```python
@dataclass
class GhostGoalRef:
    anchor_key: AnchorKey
    z_world_anchor: torch.Tensor
    z_goal_snapshot: Optional[torch.Tensor]
    wanting_strength: float
    arousal_tag: float
    staleness: float
    goal_match: float
    recoverability: float
    priority: float
```

This view can be rebuilt on demand from `AnchorSet + StalenessAccumulator +
GoalState`; it does not need to be a separately persisted store on day one.

## 6. Search policy

### 6.1 Proposal mixture

At each waking E3 tick, split candidate budget into:

- `base_current`: proposals from current terrain prior
- `ghost_probe`: proposals seeded from top ghost-goal anchors
- `novelty_tail`: small residual random or anti-recency exploration budget

Initial conservative default:

- `base_current = 0.70`
- `ghost_probe = 0.20`
- `novelty_tail = 0.10`

Later, replace fixed fractions with a dynamic `ghost_pressure` gate.

### 6.2 Ghost priority

> **SUPERSEDED by Section 0 (2026-05-19).** The multiplicative `priority`
> below violates Constraint 2 (additive dissociable channels); the
> `recoverability = sigmoid(... - a2*staleness)` form violates Constraint 3
> (recoverability must not integrate suppression/staleness evidence toward
> a retire decision; incubation can invert the staleness sign). The landed
> substrate uses the additive form (`ghost_goal_bank.py`); this block is
> retained only as the original sketch.

Recommended first-pass scoring:

```python
goal_match = cosine(curr_z_goal, ghost.z_goal_snapshot).clamp(min=0.0)
recoverability = sigmoid(a0 + a1 * ghost.last_vs - a2 * ghost.staleness)
priority = (
    ghost.wanting_strength
    * max(goal_match, eps)
    * math.sqrt(max(ghost.staleness, eps))
    * max(recoverability, eps)
)
```

Important constraint: do **not** reward low `V_s` alone. Otherwise the system
will ruminate over incoherent traces instead of probing recoverable blocked
goals.

### 6.3 Between-ticks micro-search

Current `generate_trajectories()` returns cached candidates between E3 ticks.
The minimal extension is:

- if `ghost_pressure <= threshold`: keep current cache behavior
- if `ghost_pressure > threshold`: refresh only the ghost-probe slice of the
  cache with a tiny budget

This preserves MECH-090 commitment stability while allowing unresolved goals to
stay computationally live between full replans.

## 7. Implementation order

### Phase 1: preserve goal identity

Files:

- `ree-v3/ree_core/hippocampal/anchor_set.py`
- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/agent.py`

Tasks:

- add goal payload fields to anchors
- snapshot current `z_goal`, wanting, and arousal on anchor writes/remaps
- expose a `build_ghost_goal_refs()` helper

This is SD-039 only. No search behavior changes yet.

### Phase 2: rank unresolved goals

Files:

- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/utils/config.py`

Tasks:

- compute `goal_match`, `recoverability`, and `priority`
- add diagnostics:
  - `n_ghost_candidates`
  - `mean_ghost_priority`
  - `top_ghost_goal_match`
  - `top_ghost_staleness`

This is MECH-292.

### Phase 3: wake-time probe budget

Files:

- `ree-v3/ree_core/hippocampal/module.py`
- `ree-v3/ree_core/agent.py`
- `ree-v3/ree_core/utils/config.py`

Tasks:

- add ghost-seeded proposal branch to `propose_trajectories()`
- add budget split config
- ensure ghost probes carry strengthened hypothesis tagging

This is MECH-293.

### Phase 4: between-ticks micro-refresh

Files:

- `ree-v3/ree_core/agent.py`

Tasks:

- permit tiny ghost-only refresh between full E3 ticks when ghost pressure is high
- preserve current default when feature flags are off

This is still MECH-293, but should land after the full-tick path is stable.

### Phase 5: downstream consumers

Not first-pass critical, but high leverage later:

- BLA retrieval bias can up-rank emotionally tagged ghost goals
- sleep replay can use goal payloads in addition to staleness
- self-model writeback can mark certain ghost goals resolved or obsolete

## 8. Falsifiable predictions

### Primary

In a blocked-goal or relocated-reward environment, ghost-goal search should:

- increase proposals concentrated on the previously wanted path
- shorten recovery latency after path invalidation
- avoid pure monostrategy lock better than current-anchor-only search

### Secondary

Compared with flat random probes, ghost probes should show:

- higher goal-match with current `z_goal`
- higher realized recovery yield
- lower wasted probes into fully incoherent stale regions

### Failure mode

If ghost-goal search only increases revisitation of impossible regions, then the
recoverability term is wrong and the system is implementing rumination, not good
planning.

## 9. Recommended experiment stack

1. **Payload diagnostic**
   Show that blocked/replaced anchors retain `z_goal_snapshot` and non-zero
   wanting.
2. **Ranking diagnostic**
   Inactive anchors associated with current goals rank above unrelated stale
   anchors.
3. **Probe-allocation ablation**
   Compare current-only vs current+ghost vs current+random-probe.
4. **Recovery task**
   Reward relocation or blocked corridor task with recovery-latency and
   strategy-diversity metrics.
5. **Rumination guardrail**
   Environment with permanently impossible decoys to ensure recoverability gate
   suppresses hopeless probes.

## 10. Short recommendation

The right next stack is:

1. SD-039 first
2. MECH-292 second
3. MECH-293 third
4. only then consider sleep-side goal-aware replay refinements

The decisive architectural point is simple: `ree-v3` already knows how to mark
regions as unresolved, but it does not yet preserve which unresolved regions
still correspond to a live goal. That is the exact gap this stack closes.
