# Thought Intake: Prospective navigation through goal topology

**Date:** 2026-08-08
**Status:** Stage 2 structured analysis complete; SD-098 registered 2026-08-09 (user-confirmed disposition, see Section 6).
**Raw thought file:** `docs/thoughts/2026-08-08_prospective_navigation_through_goal_topology.md`
**Related registered claims:** SD-097 (2026-08-07, general typed-relation possibility topology); SD-098 (2026-08-09, this thought's own novel remainder)
**Origin:** User-directed, dialogue-assisted refinement of the 2026-08-07 goal-topology thought, prompted by external evidence about hippocampal prospective activity.
**Provenance rule:** Per the raw thought file's own "Evidence status" note, this thought's prose is dialogue-assisted synthesis rather than verbatim user wording -- it should be treated as a secondary formulation of a new idea, not primary evidence on the same footing as a direct quotation. The 2026-08-07 thought's verbatim quotations remain the primary evidence for the earlier, separate goal-topology proposal.

---

## 1. What this thought adds, and does not restate

The 2026-08-07 thought (registered as SD-097) proposed that goals may be represented in a
changing relational topology rather than a fixed hierarchy, with pursuit of a goal able to
reveal subgoals, superordinate goals, or orthogonal possibilities retained at low salience.
This 2026-08-08 thought does not restate that. It adds a narrower computational hypothesis,
prompted by new external evidence (a press report of hippocampal activity rapidly sweeping
through possible future trajectories during navigation, preferentially toward remembered
goals): the relevant hippocampal-like contribution may be not only representing a topology,
but **prospectively traversing** it.

The thought decomposes this into four operations: (1) representing a relational space,
(2) privileging some state within it as a destination, (3) prospectively generating paths
through the space capable of reaching that destination, and (4) selecting among the resulting
candidate trajectories. It proposes a provisional REE division of labour across these four
operations (goal/commitment mechanisms privilege a destination; hippocampal-like machinery
maintains the topology and generates candidate routes; E3 selects among them; precision/
attention regulates which parts of the topology get processed) and a further claim that
goal/subgoal status is a **relational property** of the conjunction of current state, active
commitment, privileged destination, and trajectory under consideration -- not an intrinsic,
permanent label on a represented node.

## 2. Reconciliation against existing REE architecture

A focused pass over `claims.yaml` found that the four-operation decomposition this thought
proposes as new architecture is, to a substantial degree, **already the registered design** --
just not previously named as a single four-stage pipeline with an explicit biological citation
for stage (3). None of the pieces below are implemented; all are `candidate`/`provisional`,
V3-pending.

| Thought's operation | Existing REE element | Existing function | Relationship to this thought |
|---|---|---|---|
| (1) Represent the relational space | `SD-097` | General typed-relation possibility topology (requires/enables/is_part_of/prevents/conflicts_with/substitutes_for/...), the active goal hierarchy as a temporary executive projection from it. | This IS the thought's operation (1). Already registered 2026-08-07 from the parent thought; not new here. |
| (2) Privilege a destination | `MECH-236` | Hippocampal trajectory proposals must be conditioned on a goal signal (`z_goal`) injected from E3 via a dedicated channel; without it the module generates only position-based trajectories, not goal-directed ones. | REE already separates destination-privileging (E3/goal signal) from the machinery that navigates toward it -- the exact division of labour this thought proposes as new. |
| (2) Privilege a destination (multi-goal case) | `SD-046` | Multi-slot GoalState (N>=2 simultaneously active goal slots, per-slot `z_goal`); a dACC-style arbitrator selects which slot's best trajectory commits this tick. | Existing mechanism for how competing candidate destinations are arbitrated, v4-scoped. |
| (3) Prospectively generate candidate paths | `MECH-289` | The hippocampal SWR trajectory generator has anti-recency weighting; novel-path sequences never behaviourally executed are actively generated from available path segments. | This is functionally the thought's "prospective traversal" operation -- generative, not retrieval-only. Already registered, unimplemented. |
| (3) Prospectively generate candidate paths (retrieval variant) | `MECH-325`, `MECH-326` | Content-addressable trajectory library retrieved via PFC context/goal cues; PFC top-down bias steers which stored templates are retrieved. | A retrieval-based route to candidate generation, complementary to MECH-289's generative route. |
| (3), reverse-credit variant | `MECH-290` | At trajectory completion, a backward temporal credit sweep propagates the outcome retroactively through preceding states (Foster & Wilson 2006 reverse replay). | Same generative substrate, a different temporal direction of sweep than the thought's forward prospective sweep. |
| (3), anchoring/gating | `MECH-269` | Proposer anchor selection and anchor-reset: trajectory proposals anchor on latent streams whose regional verisimilitude exceeds threshold; a probe channel inverts the gate for low-verisimilitude/high-PE regions. | Governs which parts of represented state the generative sweep is allowed to anchor on -- adjacent to, not identical with, the thought's "precision/attention regulates which parts of the topology receive processing." |
| (3), mode-conditioning | `MECH-267` | `HippocampalModule.propose_trajectories` must condition on operating mode (external_task / internal_planning / internal_replay / offline_consolidation), each proposing structurally different trajectory content. | Governs which of several proposal regimes operation (3) runs in; not addressed by the 08-08 thought at all. |
| (4) Select among candidates | `MECH-125` | E3 trajectory selection implements multi-constraint viability evaluation (veto-level check across goal/harm/identity/resource space) rather than scalar reward maximisation. | This IS the thought's operation (4). Pre-existing, unchanged by this thought. |

**Conclusion of the reconciliation:** the thought's four-stage decomposition and its proposed
division of labour is not new architecture -- REE already separates these four concerns across
SD-097 / MECH-236 (+ SD-046) / MECH-289 (+ MECH-290, MECH-325, MECH-326, MECH-267, MECH-269) /
MECH-125. What the reconciliation does not find anywhere already stated is the thought's
**relational-role thesis for goal/subgoal status** (Section 3 below), and it does not find any
existing claim carrying the **specific new biological citation** this thought is prompted by
(Section 4).

## 3. The apparent novel remainder: goal/subgoal-ness as a relational property

SD-097's own title states that "the active goal/subgoal hierarchy is a temporary,
context-sensitive executive projection from this larger structure, discovered and revised
through action rather than merely traversed" -- close to, but not identical with, this
thought's sharper claim:

> Goal-ness and subgoal-ness may be relational properties arising from the conjunction of the
> agent's present state, its active commitments, its currently privileged destination, and the
> trajectory under consideration -- rather than a fixed label stored on a node.

SD-097 asserts the *hierarchy as a whole* is a temporary projection; this thought asserts that
*individual node status* (is this particular represented state currently a goal, a subgoal, or
merely an available possibility) is itself computed at read-time from the same four
ingredients, and specifically denies that `goal`/`subgoal` should be implemented as a stored
node-type field at all. That is a narrower, more implementation-relevant claim than SD-097
states, and it survives the reconciliation in Section 2 -- none of MECH-236/267/269/289/290/325/
326/125 make this assertion; they assume *some* upstream mechanism marks a state as the current
destination but do not say whether that marking is a stored property or a computed relation.

## 4. The apparent novel remainder: new biological grounding for the generative-sweep design

The prompting evidence (a 2026-08 press report of a specific neuronal mechanism for hippocampal
prospective sweeps toward remembered goals during navigation) is not cited by MECH-236 or
MECH-289 today. If it names a citable primary source, it would strengthen the biological
grounding for exactly the generative half of those two already-candidate claims (destination-
conditioned, forward-sweeping trajectory generation) -- the same role Whittington 2020 / Park,
Miller & Boorman 2021 / Khetarpal 2020 / Veeriah 2021 play for SD-097's `what_would_answer`.
The raw thought's own "Epistemic boundary" section is explicit that the evidence demonstrates
this only for physical spatial navigation, and that generalising the same primitive to abstract
goal-directed cognition remains an unverified architectural hypothesis, not something the
evidence itself shows -- MECH-236/MECH-289 already operate over SD-004's action-object space O
(not raw physical space), so the generalisation these claims already assume is not new, but a
primary source for the biological precedent motivating it would be a genuine addition were it
formally lit-pulled (see Section 7, Next steps).

## 5. What this reconciliation does NOT support registering

- A new claim restating "hippocampal machinery represents and traverses a topology toward a
  goal" would substantially duplicate SD-097 + MECH-236 + MECH-289. Per the same discipline
  SD-097's own registration followed (fold overlapping content into existing entries; register
  only the narrow novel remainder), this should not be registered as a new SD-/MECH- entry.
- A new claim restating "destination-privileging is separate from trajectory generation" would
  duplicate MECH-236's existing `z_goal`-injection design.
- A new claim restating "precision/attention gates which topology regions get processed" would
  substantially overlap MECH-269's anchor-selection/anchor-reset gating.

## 6. Candidate claim-shaped ideas -- dispositions confirmed and applied 2026-08-09

The user confirmed both proposed dispositions via `AskUserQuestion` on 2026-08-09. Applied:

1. **Registered `SD-098`** for the Section 3 relational-role thesis: goal/subgoal status is
   computed at read-time from (state, active commitment, privileged destination, trajectory)
   rather than stored as a node-type field. `depends_on: [SD-097, MECH-236]`.
   `epistemic_category: substrate_conditional` (both dependencies are unimplemented). Full
   `what_would_answer` in `claims.yaml` follows this intake's confirmed/falsified shape:
   confirmed if a relationally-computed implementation correctly re-classifies a node's
   goal/subgoal status across a destination shift with no explicit re-label write where a
   stored-node-type-field implementation needs one (or misclassifies); falsified if the
   stored-field implementation achieves the same re-classification for free, as a side effect
   of the ordinary destination-shift update MECH-236 already requires.
2. **No new claim registered** for the four-stage division of labour (Section 2) -- instead a
   dated cross-reference addendum was added to SD-097's `notes` field tying SD-097 / MECH-236
   (+ SD-046) / MECH-289 (+ MECH-290/325/326/267/269) / MECH-125 together as the already-
   registered instantiation of this pipeline, and pointing to SD-098 for the one genuine
   remainder.
3. **Primary literature located and cited** (Section 7): added as dated addenda to MECH-236's
   and MECH-289's existing `notes`/evidence fields, not as a new claim.

## 7. Next steps -- literature found, not a full lit-pull

The user asked to look for the primary source behind the medicalxpress prompting evidence
before deciding whether it grounds anything. Found via WebFetch + WebSearch, 2026-08-09:

- **Yu et al. 2026**, "Hippocampal theta sweeps indicate goal direction during navigation",
  *Nature Neuroscience*, DOI 10.1038/s41593-026-02365-2 (preprint:
  biorxiv.org/content/10.1101/2025.08.21.671551).
- **Tang et al. 2026**, "Goal-directed hippocampal theta sweeps during memory-guided
  navigation", *Nature Neuroscience*, DOI 10.1038/s41593-026-02364-3 (preprint:
  biorxiv.org/content/10.1101/2025.08.26.672489).

Both report hippocampal theta sweeps forming vectors toward remembered goal locations,
independent of the animal's current movement or head direction, with stronger goal-modulation
preceding correct navigational choices; Tang et al. additionally report these theta sequences
are preferentially replayed during sharp-wave ripples, directly linking the online (theta) and
offline (SWR) modes MECH-289 already distinguishes. A related commentary
(`nature.com/articles/s41593-026-02366-1`, "Just how goal-directed are hippocampal theta
sweeps, anyway?") could not be read -- it sits behind Nature's authentication wall and was not
pursued further given scope.

**Follow-up, same session: formal `/lit-pull` completed 2026-08-09.** The user confirmed it was
worth doing properly. New directory `targeted_review_hippocampal_theta_sweeps_goal_navigation/`,
4 entries:

1. **Pfeiffer & Foster 2013** (Nature, DOI 10.1038/nature12112) -- the canonical foundational
   result (hippocampal place-cell sequences depict future paths to remembered goals), predating
   and underlying both 2026 papers.
2. **Yu et al. 2026** (Nat Neurosci, DOI 10.1038/s41593-026-02365-2) -- the primary source behind
   the medicalxpress prompting evidence; full verbatim abstract obtained (Honeycomb maze
   dissociation design). `confidence 0.72`.
3. **Tang et al. 2026** (Nat Neurosci, DOI 10.1038/s41593-026-02364-3) -- full preprint text
   accessed via a PMC mirror; links theta-sweep goal-direction to SWR replay and PFC coordination,
   directly grounding MECH-289's dual-mode (online/offline) generative-substrate claim.
   `confidence 0.75`.
4. **Schmidt, Gagliardi & Redish 2026** (Nat Neurosci commentary, DOI 10.1038/s41593-026-02366-1)
   -- deliberately sought out as the skeptical/non-degeneracy counterweight (per this repo's
   discipline, cf. SD-097's own inclusion of Kinny & Georgeff 1991), framing the two empirical
   papers as first steps toward resolving an active controversy rather than settled science.
   Full text could not be reached (Nature auth wall, no preprint mirror for a commentary); rests
   on search-engine paraphrase only. `confidence 0.35`, held deliberately low for that reason.

All four entries deliberately exclude **SD-098** from `claim_ids_tested` -- none of this
literature speaks to the node-type-storage question SD-098 actually asks; it grounds only the
destination-privileging/generative-sweep premises (MECH-236/MECH-289) SD-098 depends on. Index
rebuilt with `build_experiment_indexes.py --index-only`; `claim_evidence.v1.json` now shows
`literature_confidence: 0.825` for both MECH-236 and MECH-289. `REE_assembly` `8e0357d28b`,
pushed.

**Process note on the regen:** the first, non-`--index-only` regen run touched 50 files -- an
unrelated experiment-corpus regen backlog (new INDEX.md/experiment.md pages for several other
sessions' already-landed experiments) that had nothing to do with this lit-pull. Per CLAUDE.md's
"Narrow Edits Only" rule, reverted it and re-ran with `--index-only`, which is scoped to exactly
`claim_evidence.v1.json` + `evidence/literature/INDEX.md`. One sub-mistake during the revert: a
blanket `rm -rf` on the untracked-looking experiment-type directories actually deleted TRACKED
`runs/*/{manifest,metrics,summary}` files that happened to live inside them (real committed
evidence, not regen output) -- caught immediately via `git status` showing ` D` entries and
restored with `git checkout HEAD -- <paths>` before anything was committed. No data was lost, but
worth naming rather than quietly correcting: a blanket `rm -rf` on a directory is not a safe way
to remove "just the untracked files" in it when the directory can also hold tracked content.

Both raw thought files' Stage 1 headers were updated earlier in this session (Section 8 below
covers the earlier claim-opening-order process gap).

## 8. Session note: resource contention, and a claim-opening process gap

At the start of this session, `TASK_CLAIMS.json` showed an active claim
(`mel-dose-sweep-inv-051-6b93d7`, opened 2026-08-09T18:10:05Z) on `claims.yaml`,
`docs/assets/data/claims.json`, and `WORKSPACE_STATE.md` for unrelated thought-intake work
(`thought_intake_2026-08-09_failure_autopsy_failure_location_buckets.md`). Per the umbrella
`CLAUDE.md` arbitration rule (`task_claim.py open`/`check`), that session owned those three
resources at that moment; this session was not the owner and did not write to them while the
claim was active -- this intake file and the two raw-thought header updates (different paths)
were written in the meantime. A re-check at 2026-08-09T18:22Z found the contention had cleared.

**Process gap, noted for honesty rather than corrected retroactively:** this session ran
`task_claim.py check` (read-only) before editing `claims.yaml`, confirmed no contention, and
proceeded directly to the `SD-098` registration and the SD-097/MECH-236/MECH-289 addenda --
without first running `task_claim.py open`, which the umbrella `CLAUDE.md` Session Startup
Protocol step 4 requires BEFORE editing any claimed resource, not just before a final commit.
The claim was opened afterward, once this gap was noticed, before the commit landed. No harm
resulted (no concurrent writer touched these paths in the interval, per a repeat `check`
immediately before commit), but the ordering was wrong and the correct sequence is: open the
claim first, then edit.

## 9. Provenance note

The 2026-08-08 raw thought file states its own prose is dialogue-assisted synthesis, not
verbatim user wording, and that the 2026-08-07 thought's verbatim quotations remain the primary
evidence for the earlier, distinct proposal. This intake preserves that distinction: Section 1
above restates the 08-08 thought's own framing rather than treating it as a fresh primary
source, and Sections 2-4 are this session's reconciliation against the current registry, not
part of the original thought.
