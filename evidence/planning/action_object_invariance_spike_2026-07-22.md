# Scoping spike: is E2's action-object near-invariance a defect or a property?

**Date:** 2026-07-22T04:05:16Z
**Session:** `epic-burnell-995d28`
**Type:** SCOPING SPIKE (probe, not a build). No substrate change landed.
**Substrate:** ree-v3 `7f10f441a6` (spike ran against this tree)
**Prior:** ree-v3 `6064f9075f` "Action-object round trip is NOT an action source + CEM elite floor"

---

## 1. Question

Given that the `a -> E2.action_object(a) -> action_object_decoder` round trip is not
invertible (landed 2026-07-22, selection defect closed), is the action-object embedding
SUPPOSED to be action-discriminative?

- **(a) NOT A DEFECT.** Per ARC-018 / SD-004, O is the space of action *consequences*.
  Two actions with the same consequence SHOULD embed alike. Predicts
  **consequence-structured** variance.
- **(b) IS A DEFECT.** The CEM searches a space whose coordinates barely move under
  the thing it optimises, capping planning quality generally. Predicts **near-zero**
  variance regardless of consequence.

**Verdict: neither, as posed. It IS a defect, but the mechanism is the opposite of (b)'s
diagnosis.** The embedding is not action-invariant. It is **state-invariant**: a frozen
random re-encoding of the action label that carries essentially no information about the
world state whose consequences it is supposed to represent. Reading (a) is falsified on
its own prediction.

---

## 2. What the design INTENDS (Task 1)

| Source | Intended property |
|---|---|
| `sd_004_sd_005_encoder_codesign.md` Sec.4 | `o_t` encodes "the world-directed **consequence** of taking action `a_t` from `z_world_t`"; CEM in O is "more tractable" because O is "lower-dimensional and **semantically grounded in world-effects**" |
| same, "SD-004 + SD-005 co-design" | "action objects should encode **genuine world-effects**, not perspective shifts" |
| `hippocampal_systems.md` (ARC-018 reframe) | "E2's latent space is action **consequences** (action objects), not sensory state transitions" |
| `frontal_cue_integration.md` | "The action-object representation determines the **affordance manifold**"; SD-016 `action_bias` "elevates the apparent affordance of **avoidance** action-objects and attenuates **approach** action-objects" |
| `efficiency_dimensionality_hypothesis.md` | "SD-004 implements a **learned compression** from z_world-level effects to 16-dim action objects" |

The intended invariance is therefore **consequence-invariance**, and it is explicitly
**state-CONDITIONED**: `o_t = f(z_world_t, a_t)`. The same action in different world
states must produce different action-objects, or "world-effect" is vacuous. SD-016's
"avoidance action-objects" vs "approach action-objects" presupposes that O has regions
picked out by consequence, not by action label.

Note the doc says "**learned** compression". Nothing learns it (Sec. 4).

---

## 3. Measurements (Task 2)

Probe: `CausalGridWorldV2` size=6, seed 42, `alpha_world=0.9`, `self_dim=world_dim=32`,
`action_object_dim=16`, `action_dim=5`. 120 sampled world states with forced periodic
resets (so state diversity is not one trajectory's corner). For each state, all 5 actions
are applied to a `deepcopy` of the env to obtain **ground-truth consequences** (agent
displacement, transition type, harm signal, full next observation). Arms: untrained and
40-episode canonical warmup. `world_forward` measured alongside as a **trained-sibling
calibration reference** (it IS in the warmup optimizer; SD-056's known collapse site).

### 3.1 Headline table

| Measure | untrained | warmed 40ep | reads as |
|---|---|---|---|
| **M0** `action_object_head` param delta L2 after warmup | 0.0 | **0.0** | head is bit-identical; zero gradient |
| **M5** `r2_explained_by_action_alone` (ao) | 0.9944 | **0.9947** | ao is 99.5% a function of the action label alone |
| **M5** pairwise-distance CV across 120 states (ao) | 0.0089 | 0.0095 | the 5-action distance matrix is the SAME in every state (<1% variation) |
| **M6** within-action-pair consequence Spearman (ao) | 0.085 | **-0.013** | ~zero, sign unstable: no consequence structure |
| **M2** linear probe: action class from state-centred ao | **1.00** | **1.00** | the action IS fully present (chance 0.20) |
| **M1** action-signal-to-offset ratio (ao) | 0.365 | 0.366 | signal rides on a large constant offset |
| M5 `r2_explained_by_action_alone` (**world_forward**) | 0.791 | **0.558** | trained sibling BECOMES state-dependent |
| M1 action_var_fraction (**world_forward**) | 0.793 | **0.561** | same direction |

Control: z_world does vary across the sampled states (total var 0.0031, mean per-dim std
0.0096, mean norm 0.42), so `between_state_var` on ao being ~6e-05 is **not** an artefact
of a collapsed z_world — the same z_world variation moves `world_forward` fine.

### 3.2 Reading (a) is falsified

(a) predicts consequence-structured variance. Consequence structure **requires** state
dependence: the same action has different consequences in different states. Measured
state dependence is **0.5% of ao variance**, and the 5x5 pairwise-distance matrix varies
by **<1%** across 120 states. An embedding that is the same in every state cannot encode
state-conditioned consequences. Within-pair consequence correlation is **-0.013**.

**A trap this spike had to control for.** The naive consequence contrast (M3: same- vs
different-consequence action pairs, pooled) appears to IMPROVE with training, cohen's d
-0.21 -> +0.48, Spearman 0.16 -> 0.26. That is an artefact, and M0 proves it: the head's
parameters are **bit-identical** (delta L2 exactly 0.0), so the embedding cannot have
acquired structure. What changed is the agent's behaviour, hence which states are visited,
hence how the same/different consequence LABELS redistribute over a distance matrix that
is itself fixed. Partialling out action-pair identity (M6) removes the signal entirely.
Anyone re-running the pooled contrast alone will get a false positive for reading (a).

### 3.3 Reading (b) is right in verdict, wrong in mechanism

(b) predicts "near-zero variance regardless". False: actions move the coordinates plainly
(action variance fraction 0.996, linear probe 100%). The coordinates that do **not** move
are the **state** coordinates. So the CEM is not searching a space unresponsive to the
action; it is searching a space unresponsive to the **world**.

### 3.4 Root cause: `action_object_head` receives zero gradient, from every path

Confirmed three independent ways:

1. **Code.** `action_object_head` occurs in exactly two places in ree-v3: its construction
   (`e2_fast.py:144`) and its use (`e2_fast.py:602`). No loss in `ree_core/` or
   `experiments/_lib/` names `action_object`.
2. **Optimizer.** The canonical warmup (`experiments/_lib/goal_pipeline_tier1.warmup_train`)
   builds Adam over `e1`, `e2.world_transition + e2.world_action_encoder`,
   `e3.harm_eval_head`, `latent_stack`. `action_object_head` is in none of them.
3. **Empirical.** Parameter delta L2 after 40 episodes = **exactly 0.0**.

So `o_t` is a frozen random projection of `[z_world, a]` fixed at init, and the "learned
compression" SD-004 describes does not exist. The `world_forward` column is the control
that makes this legible: the *same* measurement on a sibling head that IS trained moves
0.79 -> 0.56 in exactly the expected direction, while the ao head does not move at all.

### 3.5 Refinement to the landed round-trip write-up

The landed note says "The decoder is NOT the degenerate component: fed N(0,1) inputs it
spans all classes." True but materially misleading, and worth amending:

- On N(0,1) the decoder puts **1362/2000 (68%)** of inputs on class 3. It spans all
  classes only in the weak sense that each gets nonzero count.
- Real `ao` inputs have per-dim std **0.036** against the probe's 1.0 — the health check
  is run **28x out of domain**.
- Measured on the 5 one-hot actions: ao norms 0.328-0.421 (genuinely different), decoder
  logit std across them 0.007-0.017, against class-mean gaps up to 0.33. Argmax pins to 3.

The accurate statement is that **neither component is individually degenerate; the
composition is**, because both are untrained and the ao distribution is a small ball far
from the decoder's decision boundaries. This does **not** disturb the landed decision:
not using the round trip is still correct, and training the decoder alone is still the
wrong fix — a decoder cannot recover consequences from an embedding that never encoded them.

### 3.6 Blast radius

`propose_trajectories` (`module.py:1113`) searches **in O**: initialise `ao_mean` from the
terrain prior, sample, decode to actions, roll out, refit. The elite refit
(`module.py:1372-1381`) reads back **`traj.get_action_object_sequence()`** — the
E2-computed action-objects, not the sampled ones. So the CEM's search distribution over O
is refit against a near-state-blind embedding, closing the loop through the frozen head.

Downstream implications **flagged, not measured** (each needs its own check):

- **SD-016 / MECH-151** additive `action_bias` presumes O has approach/avoidance regions.
  If O is indexed by action label, a cue-indexed bias cannot select consequence classes.
- **ARC-063 / ARC-064** mint `rule_embedding` from "context + action-object"; a frozen
  random function of the action label carries no regularity to detect.
- **SD-004's own PASS (EXQ-003, TERRAIN harm 0.0010 vs RANDOM 0.0896, 6x survival)** was
  obtained on this same frozen head. So the 6x result was **not** produced by semantic
  grounding in O. Either O's structure is not load-bearing for it (and SD-004's stated
  rationale needs reframing), or it is and the result has another explanation. This is the
  load-bearing open question, and it is what the falsifier below targets.

---

## 4. Recommendation (Task 3)

**IS A DEFECT** — register a claim, propose a falsifier, build nothing from this spike.

The defect is a **missing training objective**, not a wrong architecture. The head, its
call sites, and its consumers are all correctly placed; nothing ever trains it toward the
world-effect objective SD-004 asserts. Per the debt vocabulary: the *fix* is now
`complicated (buildable)` (the spike removed the unknown); whether the fix improves
planning remains `complex (probe-gated)` and is what the falsifier below resolves.

Do **not** widen this into a substrate change without the falsifier. SD-004 is `implemented`
and carries a PASS; overturning its rationale needs evidence, not inference.

### 4.1 Claim to register

`REE_assembly/docs/claims/claims.yaml` is held by an ACTIVE claim from another session
(`cool-sutherland-623d3f`), so this spike did **not** write it. Ready-to-paste block:

```yaml
- id: SD-080
  subject: e2.action_object_consequence_grounding
  claim_type: design_decision
  status: candidate
  implementation_phase: v3
  statement: >
    E2.action_object_head receives zero gradient from every REE training path, so the
    action-object space O is a frozen random projection fixed at initialisation rather
    than the learned world-effect compression SD-004 specifies. Measured 2026-07-22:
    99.5% of action-object variance is explained by the action label alone, the 5-action
    pairwise-distance matrix varies <1% across 120 world states, within-action-pair
    consequence correlation is ~0, and the head's parameters are bit-identical after 40
    warmup episodes (delta L2 exactly 0.0). O is therefore state-invariant, not
    consequence-structured; the hippocampal CEM searches and refits in it.
  depends_on: [SD-004, ARC-018, SD-056]
  falsifier: see evidence/planning/action_object_invariance_spike_2026-07-22.md Sec 4.2
  evidence: evidence/planning/action_object_invariance_spike_2026-07-22.md
```

Relation to **SD-056**: same failure FAMILY, different site. SD-056 fixed action-collapse
in `world_forward` with a contrastive objective, having diagnosed the cause as "under
reconstruction-shaped training the state-dominated solution is the local minimum". The
action-object head has the identical input geometry (`Linear(world_dim + action_dim, ...)`,
action = 4/36 of the input) but a *stronger* form of the same problem: it has no training
signal at all, so it never even reaches a local minimum. SD-056's remedy is the natural
template, but its objective is not directly reusable — SD-056 pushes *actions apart*, and
the ao head's deficiency is that *states* are not represented.

### 4.2 Proposed falsifier

**Design.** 3 arms, matched seeds, `CausalGridWorldV2`, EXQ-003-comparable DVs.

- `ARM_0` baseline: current substrate, frozen head.
- `ARM_1` consequence-grounded: train `action_object_head` with an auxiliary loss making
  `o_t` predict the realised world-effect (next-state delta and/or transition type) from
  `(z_world_t, a_t)`.
- `ARM_2` parameter control: train the head against a **shuffled/permuted** consequence
  target. Same added parameters and gradient traffic, no consequence structure. Without
  this arm an ARM_1 win is confounded with "more trained parameters".

**Primary (substrate-side, cheap, must fire first as a gate):**
`r2_explained_by_action_alone` on ao falls well below 0.99, and within-action-pair
consequence Spearman (M6) rises materially above 0 — **in ARM_1 only**. If ARM_1 does not
move these, the objective failed and the behavioural read is uninterpretable; stop there.

**Secondary (behavioural):** harm_rate and survival vs ARM_0, matching the DVs SD-004's
EXQ-003 PASS rests on.

**Both directions declared.**
- *Defect confirmed:* ARM_1 beats ARM_0 and ARM_2 behaviourally. O's semantic grounding is
  load-bearing and was absent; SD-080 promotes and SD-004's mechanism is repaired.
- *Defect is real but not load-bearing:* ARM_1 moves the substrate DVs but not behaviour.
  This is a **genuine and important** result, not a null: it would mean SD-004's stated
  rationale ("semantically grounded", "planning horizon extension") is **not** what
  produced EXQ-003's 6x survival, and the actual mechanism is terrain/residue navigation.
  SD-004 gets reframed and its efficiency rationale demoted; SD-080 stays candidate as a
  correctness-not-capability finding.

**Cheaper prior probe, worth running first.** Re-run the EXQ-003 TERRAIN-vs-RANDOM
contrast with the ao head re-initialised at several different random seeds. If the 6x
survival result is invariant to O's *content*, that is strong, near-free evidence that
O's structure is not load-bearing for SD-004's PASS — and it re-prices the whole falsifier
before any training objective is written.

---

## 5. Artifacts

- Probe: `ao_invariance_spike.py` (session scratchpad; not landed in `experiments/` —
  this is a spike, and `experiments/` is reserved for the `/queue-experiment` path)
- Raw arrays + results JSON alongside it (`raw_untrained.npz`, `raw_warmed_40ep.npz`,
  `ao_invariance_spike_results.json`)
