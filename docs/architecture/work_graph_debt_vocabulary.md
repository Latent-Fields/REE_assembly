---
title: Work-graph debt vocabulary (gated vs blocked, made precise)
parent: "Foundations & Rationale"
grandparent: Architecture
nav_order: 19
---

# Work-graph debt vocabulary (gated vs blocked, made precise)

*Registered 2026-07-10. Methodology vocabulary for how we classify any unfinished node
in the REE work graph (experiment queue, substrate_queue, closure plans, autopsy
routing, "gated on X" language). PROMOTES/DEMOTES NOTHING — this is how we talk about
the work, not a claim about the agent.*

## The problem this fixes

We were using "blocked" for two different things: (1) a node that is buildable but
sitting behind other buildable work, and (2) a node we genuinely cannot build yet.
Collapsing them hides the only distinction that matters for *what to do next*. A
buildable chain — however deep — is just **labour**; it rewards *doing*, not thinking.
A node that terminates in an **unknown** rewards *inquiry* — research, hypotheses,
experiments, deduction. The interesting cognition lives on the unknowns. So we name
them apart, and we name them the same way every time.

**Razor:** recurse "and is *that* buildable?" down the dependency chain. You are only
ever *blocked* when you hit a link that is **not buildable on demand** — an unknown.
Everything above that link is execution; the block *is* the unknown.

## The tokens (the bracket is part of the token — never write the bare word)

Every unfinished node is exactly one of these. Always write the token **with** its
bracket, so the meaning travels and nobody has to remember which is which.

| Token | Bracket names… | Do this | Debt kind |
|---|---|---|---|
| **complicated (buildable)** | the response | build it | execution debt |
| **complex (probe-gated)** | the response | run a spike (a REE diagnostic) | discovery debt |
| ↳ **puzzle (known rules)** | what you keep → so hunt **data** | run the experiment; get the fact | discovery debt |
| ↳ **mystery (known data)** | what you keep → so hunt the **frame** | re-operationalize / reframe | discovery debt |
| **aleatoric (irreducible)** | it's noise | hedge / robustify — do **not** research | not debt |

Two mnemonics, so the brackets are self-documenting:

- **Cynefin pair** (`complicated (buildable)` / `complex (probe-gated)`): the bracket
  names *what you do*. Complicated is knowable by analysis, so you can build your way
  there; complex is knowable only in retrospect, so you must probe it with a
  safe-to-fail experiment. (Snowden's Cynefin framework.)
- **Treverton pair** (`puzzle (known rules)` / `mystery (known data)`): the bracket
  names *what you already hold* — and therefore what you're missing. A **puzzle** has a
  definite answer (you keep the *rules*) and lacks only a *fact* → go get it. A
  **mystery** has the information already (you keep the *data*) and lacks a *frame* →
  find the lens; more data won't help. The pair is complementary: **rules ↔ data.**

**"Gated on X" is well-formed only if X resolves to one of these tokens.** "Gated" then
stops being vague: *gated on a `complicated (buildable)` node* = just build it; *gated
on a `complex (probe-gated) / puzzle (known rules)` node* = the answer is a spike away.

## The reducibility carve-out

Not all unknowns reward inquiry. Borrowing the ML distinction between epistemic
(reducible) and aleatoric (irreducible) uncertainty: only **reducible** unknowns are
`complex (probe-gated)` discovery debt. A genuinely `aleatoric (irreducible)` node —
real noise, a multivalued response — is resolved by robustifying against it, not by
researching it. The boundary is *fluid*: a good reframe can convert an
`aleatoric (irreducible)` node into a `mystery (known data)` one (which is exactly what
"finding a frame" means). So the classification is a live judgement, re-made as
understanding improves — not a permanent label.

## Spikes = REE diagnostics

The operational primitive for discharging a `complex (probe-gated)` node already has a
name in agile practice: the **spike** — a time-boxed investigation whose deliverable is
"knowledge, not shippable code." That is precisely what a REE
`experiment_purpose=diagnostic` run is. A spike's whole job is to **convert a
`complex (probe-gated)` node into `complicated (buildable)` backlog**: before the spike,
you don't know if the thing is worth building or joins the mechanism; after it lands,
there's no unknown left in the line and it's pure execution. Discipline to keep from
agile: a spike is *time-boxed* — it buys a decision, it does not become the build.

## Why this is REE-native, not an import

This is the **epistemic-value term of expected free energy** (see
`active_inference_bridge.md`), applied to the *work graph* instead of the agent's
actions. Active inference already tells the agent to prefer actions that resolve
uncertainty (epistemic value) over pure goal-seeking (pragmatic value). The same
ordering applies to *our* choices about what to work on: **prefer surfacing
`complex (probe-gated)` discovery-debt nodes over `complicated (buildable)` execution
ones, because only the former convert effort into information.** Execution backlog can
wait; an unresolved reducible unknown is where more thinking changes the outcome.

## Worked examples (from the conversion-ceiling campaign)

- **The owed actor-critic action-learning substrate (MECH-457):** the isolated build is
  `complicated (buildable)` — buildable now; nothing missing. It sits behind exactly one
  `complex (probe-gated) / puzzle (known rules)` node: *is the actor the right target,
  or is the observation encoder the problem (H1 vs H2)?* We keep the rules (the
  actor-critic frame is well-posed) and lack a fact. **V3-EXQ-737 is the spike** that
  discharges it. A green 737 converts the whole line to `complicated (buildable)`
  backlog.
- **V3-EXQ-738** already discharged part of that node: it refuted strong-H2 (the 1.0
  floor *is* reachable from the agent's 5x5 local view) — a spike that removed one leg
  of the unknown.
- **V3-EXQ-723a (compact-vs-diffuse workspace):** started as a `puzzle (known rules)`
  but the competence-floor confound turned it into a `mystery (known data)` — no
  additional run settles it; the move is a reframe (competence-first re-operationalize),
  not more data. A clean example of a node migrating between tokens as understanding
  improved.

## Naming note (avoid a live collision)

Do **not** call the discovery-debt node "epistemic debt." That term is already taken and
means the *opposite-in-time*: the accumulated **opacity of systems you already built but
can no longer understand** (Ponnusamy & Nembhard 2019). Ours is a *pre*-construction
unknown; theirs is *post*-construction opacity. Keep them apart.

## Wiring status (what uses this, and what still owes it)

**Wired (2026-07-10, session modest-faraday-58b67a):**
- `REE_Working/CLAUDE.md` (General Rules) — startup pointer + tokens + razor + the
  prefer-discovery-debt stance.
- `/failure-autopsy` routing — classify the node into a token before routing (the token
  *is* the routing decision).
- `/queue-experiment` Step 2.5 — `blocked_substrate` == `complicated (buildable)` → build,
  not experiment; queue only `complex (probe-gated)` spikes; "gated on X" must name a token.

**Wired (2026-07-10, session optimistic-babbage-363511 — the two formerly-owed pieces):**
- `/governance` — Step 3 (the recommendation / next-work sweep) now classifies each open
  node *by token* and surfaces `complex (probe-gated)` discovery-debt AHEAD of
  `complicated (buildable)` execution backlog (prefer-discovery-debt, applied at the point
  work is prioritised); Step 6a wires `node_class` into the schema block, the autopsy-create
  field list, and the 6a-vi report. Mirrored byte-identical to both skill dirs.
- `substrate_queue.json` schema — per-entry `node_class` field (one of the five tokens);
  documented in `_schema_notes` (allowed values, default reading = `complicated (buildable)`,
  gated-on rule, populated-by). `scripts/verify_governance_cycle.py` check I validates it
  (warn/info only, never blocks): invalid value → warn, "gated on" phrase without a
  resolving token → warn, unmarked entries → aggregate info. Historical entries are
  backfilled lazily as a governance cycle next touches each entry.

Nothing further owed: every surface named in this section is now wired.

## References

- Snowden & Boone, "A Leader's Framework for Decision Making," *HBR* 2007 (Cynefin
  complicated vs complex; probe-sense-respond; safe-to-fail experiments).
- Treverton, *Reshaping National Intelligence for an Age of Information* (2001) —
  puzzles vs mysteries; popularized by Gladwell, "Open Secrets," *The New Yorker* 2007.
- Hüllermeier & Waegeman, "Aleatoric and epistemic uncertainty in machine learning,"
  *Machine Learning* 110 (2021) — reducible vs irreducible uncertainty.
- Agile "spike" (Cohn/XP practice) — time-boxed investigation; deliverable is knowledge.
- Olah & Carter, "Research Debt," *Distill* 2017 — the adjacent post-hoc "knowledge
  debt" (distillation), distinct from the pre-build discovery debt named here.
- Ponnusamy & Nembhard, "Epistemic Debt: A Concept and Measure of Technical Ignorance
  in Smart Manufacturing," 2019 — the colliding "epistemic debt" (system opacity).
