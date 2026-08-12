---
nav_exclude: true
---

# Thought Intake: Ecological succession as a developmental curriculum for REE

**Raw thought file:** `docs/thoughts/2026-08-11_ecological_succession_as_developmental_curriculum.md`
**Session:** jovial-shannon-35d300, 2026-08-12
**Status:** processed, 3 claims registered (MECH-491, ARC-127, SD-100)

---

## Verbatim prompt

See the raw thought file for the full text. Core proposal, condensed: treat REE's environment
itself as a developmental curriculum that grows in ecological complexity as REE becomes capable
of learning more complicated regularities -- rather than simply adding more hazards. Concrete
sub-proposals: (1) **scent** as a new sensory modality -- REE emits a slowly-decaying self-scent
trail, creating potential conflicts between internal memory and external scent evidence;
individual-specific scent identifies nearby organisms; (2) **competitor/REE-like NPC
organisms** with individual-specific scent trails, territories, and behavioural histories that
differ despite visual similarity; (3) **transient hidden states** in NPCs (e.g. a competitor
that becomes aggressive for a period after seeing REE eat nearby, marked by an "angry" scent),
giving a learning progression from association through hidden-state inference to causal
prediction; (4) **conditional danger** rather than fixed per-class valence (e.g. jellyfish
dangerous only at certain times/states/combinations); (5) **circadian ecology and
environment-embedded sleep** -- a diurnal cycle (reduced food/competitor activity/visibility at
night) making sleep onset ecologically sensible, interacting with existing homeostatic/
circadian/surprise/threat sleep-onset factors; (6) a design principle that the environment
should be used to EXPOSE limitations in existing machinery rather than pre-emptively adding
mechanisms; (7) **periodic comparative ethology** -- asking what real organism best matches
REE's current demonstrated repertoire (currently: zebrafish), as a heuristic distinct from its
actual developmental regime; (8) **environmental epoch transitions** -- a "fish-world ->
mouse-world -> dog-world" sequence of qualitatively different social/ecological demands; (9) a
**developmental naming scheme** -- "Steve" for a dog-level social-animal lineage, "Adam" for a
later linguistic, person-like stage with language grounded in the system's own lived experience.

---

## What's New vs. Existing REE Docs (novelty table)

| Existing doc/claim | What it already covers | What this thought adds |
|---|---|---|
| **`ARC-047`** (SocialGridWorld, v5, unbuilt, `claim_type: architectural_commitment`, status `candidate`, confidence 0.0) | A 7-channel gradient-scent design (wanting/seeking/alarm/harm_stress/direction/celebration/defense) for **OTHER-agent** state-leakage scent, emitted by full REE-instance agents in a multi-agent social-cognition test harness, to empirically ground `ARC-010` mirror modelling and `MECH-041` affective expression. | **Substantial pre-existing overlap on the "competitor organisms with transient state-linked scent" sub-proposal (3)** -- ARC-047 already specifies exactly this pattern (internal state -> scent channel -> observed by others -> interpreted via mirror modelling) for multi-agent REE instances. What is genuinely NEW relative to ARC-047: (a) **self-scent as an external memory trace** -- ARC-047 is entirely about OTHER agents' scent, never REE's own trail re-encountered by itself; this is a different subject (memory, not social cognition) with no multi-agent dependency. (b) Simpler, non-REE-instance **competitor NPCs** (ordinary fish, not full REE agents) -- a lighter-weight environment feature than ARC-047's multi-REE-instance harness, closer to extending the existing hazard/food-field pattern than to building ARC-047's social-cognition test rig. |
| `INV-050` (sleep phase architecture: circadian timing, homeostatic pressure, Model Error Load) | The **internal** regulation of sleep-phase timing and sufficiency -- three drives, none of which currently responds to any external ecological/environmental circadian signal because the v3 fish-world environment has no time-of-day structure at all. | An **external** environmental substrate (diurnal food/competitor/visibility cycle) for those internal drives to respond to. Distinct subject (environment substrate vs. internal regulation), explicitly designed to interact with INV-050 rather than duplicate it. |
| `SD-054` (reef substrate) | The nearest existing example of an environment substrate deliberately engineered to create two competing behavioural attractors and break monomodal policy collapse. | Confirms the general PATTERN this thought's proposals follow (purpose-built environmental structure to expose/pressure-test existing cognitive machinery) is already validated methodology in this codebase, not a new kind of intervention. |
| No existing claim | -- | **Conditional/contextual hazard valence** (jellyfish dangerous only under specific conditions) -- no existing REE hazard mechanism implements context-dependent valence; current hazards carry fixed valence per object class. Genuinely new. |
| No existing claim | -- | **Periodic comparative-ethology benchmarking** as a standing REE-Assembly process (ask "what organism best matches REE's current repertoire" on a schedule) -- genuinely new as a PROCESS proposal, not an empirical claim. |
| No existing claim | -- | **Environmental epoch transitions** (fish-world/mouse-world/dog-world) and the **developmental naming scheme** ("Steve", "Adam") -- genuinely new; both are naming/roadmap proposals rather than falsifiable claims about REE's substrate. `grep` across `claims.yaml` for "zebrafish"/"comparative ethology"/"mouse-world"/"dog-world" as a NAMING SCHEME found only unrelated zebrafish-biology citations, not this proposal. |

**Net assessment:** a large, V4/V5-scoped vision document. Three of its nine sub-proposals are
concretely claim-shaped once separated from the surrounding roadmap material (self-scent
memory, conditional danger, circadian ecology). One (competitor NPC scent) substantially
overlaps the already-registered `ARC-047` and is not separately registered. The remainder
(design principle, comparative-ethology process, epoch transitions, naming scheme) are
process/roadmap proposals without a falsification condition and are not registered as claims.

---

## Key formulations (preserved for later reference, not separately registered)

- **Design principle:** "Do not add a new cognitive mechanism merely because a more
  complicated environment would benefit from it. Instead, introduce an ecological pressure that
  existing machinery may or may not be able to solve. Observe the failure or adaptation. Then
  determine whether the result justifies a developmental or architectural addition." -- worth
  treating as a standing house rule for future environment-design proposals, analogous in spirit
  to existing REE-Assembly discipline against premature abstraction.
- **Comparative-ethology heuristic:** the ecological/cognitive analogue (what organism REE's
  repertoire currently resembles) and the developmental regime (what process REE is actually
  raised under) are two separate dimensions that should not be conflated -- a fish-comparable
  repertoire could still be raised under a more mammalian-like protected/progressive-exposure
  regime.
- **Epoch sequence sketch:** fish-world (currents, reefs, food patches, jellyfish, chemical
  gradients, scent trails, competitors, territories, diurnal cycles, primitive sleeping
  locations) -> mouse-world (burrows, nests, mazes, caches, territorial scent, predators,
  richer spatial structure, manipulable objects) -> dog-world (individual relationships,
  attachment, cooperation, play, social learning, communicative gestures).
- **Naming scheme:** REE (architecture/early organism) -> Steve (sufficiently sophisticated
  social-animal developmental lineage) -> Adam (linguistic, person-like system with language
  grounded in its own memories/goals/relationships/predictions/affective states/lived
  experience, not merely an attached language model). Explicitly not an evolutionary-ladder
  claim -- fish/mice/dogs/humans are not rungs on a hierarchy.

---

## Affected existing claims

`ARC-047` -- unaffected in status; overlap with sub-proposal (3) noted above and explicitly
distinguished from the newly-registered `MECH-491` (self-scent memory) in that claim's
`depends_on` notes.
`INV-050`, `SD-017` -- unaffected in status; cited as the internal regulation the newly
registered `SD-100` is designed to interact with, not duplicate.
`SD-054` -- unaffected in status; cited as the validated precedent pattern for
purpose-built environmental pressure.

No existing claim's evidence, status, or confidence is altered by this intake.

---

## Candidate claims

Three claims registered (2026-08-12), full text in `docs/claims/claims.yaml`:

- **`MECH-491`** -- self-scent-as-external-memory-trace (`substrate_conditional`, v4).
- **`ARC-127`** -- conditional/contextual danger generalisation (`substrate_conditional`, v4).
- **`SD-100`** -- environment-embedded circadian ecology motivating sleep
  (`substrate_conditional`, v4, `depends_on: [INV-050, SD-017]`).

**Not registered, with reasons:**
- Competitor/REE-like NPC transient-state scent -- substantially overlaps `ARC-047`; no new
  claim needed, existing claim already covers the pattern (multi-agent scope difference noted
  above but not judged to warrant a separate id).
- Design principle ("environment as experimental instrument") -- a methodology/process rule,
  not a falsifiable claim about REE's substrate.
- Periodic comparative-ethology benchmarking -- a standing-process proposal, not a claim; no
  observation could confirm or refute "REE should be compared against real organisms
  periodically."
- Environmental epoch transitions (fish/mouse/dog-world) and the naming scheme (Steve/Adam) --
  roadmap/naming proposals, not falsifiable claims; revisit if/when REE's repertoire actually
  approaches a mouse-world-scale comparison, at which point a concrete environment-design claim
  could be drafted for that specific transition.

---

## Next steps

1. MECH-491, ARC-127, SD-100 registered; `build_claims_json.py` run after this intake session's
   edits land.
2. None of the three registered claims are queued via `/queue-experiment` in this pass -- all
   three are `substrate_conditional` on environment features that do not yet exist in the v3
   fish-world (self-scent deposit/decay, conditional-valence hazards, diurnal cycle). Building
   any of them is V4-scoped substrate work, not queued here.
3. The design principle and comparative-ethology heuristic are recorded above for future
   reference (e.g. as candidate additions to a V4/V5 environment-design plan-of-record
   document) but no such document is created in this pass -- flagged as a follow-on, not
   performed (Scope Discipline).
4. No lit-pull performed -- these are REE-internal architecture/environment-design proposals,
   not claims requiring citation-backed biological grounding (unlike, e.g., `INV-074`).
